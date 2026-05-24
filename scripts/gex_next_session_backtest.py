#!/usr/bin/env python3
"""Rolling predictive backtest for the §2 next-session GEX advisory (SPY/QQQ).

The /daily-analysis §2 "Next-Session GEX Map" is shipped as an *advisory* — it
states the EOD dealer-gamma levels (zero-gamma, call/put wall, regime) that carry
overnight, but it makes **no** predictive claim. This script is where that claim
is actually *tested*, on a rolling trailing window, so /weekly-analysis can report
whether the advisory has earned predictive weight yet.

Two hypotheses, both vs a 50% / "no edge" baseline:
  * **H1** — spot-vs-EOD-ZGL predicts next-session realised vol. Dealer theory:
    short-gamma days (spot < ZGL) print *higher* next-day |return| than long-gamma
    days (spot >= ZGL). Only sessions with a *sane* ZGL (near spot) are testable.
  * **H2** — EOD walls act as next-session magnets: the next close lands *closer*
    to the nearest EOD wall (pin chosen with day-D info only — no look-ahead).

Data substrate: the same uw-pp CLI binary the ``uw-pp`` MCP server wraps. We shell
out to it (stdlib ``subprocess`` + ``json`` — no third-party dependency, no pip
install), so this helper runs on a bare Python 3.12 the same way the other
``scripts/`` helpers do. Override the binary path with ``UW_PP_CLI``.

Usage:
    python3 scripts/gex_next_session_backtest.py --symbols SPY,QQQ --days 60 --json
Exit 0 = ran (see ``available``); 2 = usage error. A missing CLI / empty data is
reported as ``{"available": false, ...}`` with exit 0 so the weekly pipeline can
note the skip rather than abort (mirrors scripts/fred_macro.py).
"""

from __future__ import annotations

import argparse
import json
import math
import os
import subprocess
from pathlib import Path
from typing import Any, Iterable

DEFAULT_CLI = Path.home() / "printing-press" / "library" / "unusual-whales" / "unusual-whales-pp-cli"

# A ZGL is only trusted (H1-testable) when it sits within this fraction of spot —
# beyond it the value is an extrapolated/deep-OTM crossing artifact, not a real flip.
ZGL_SANE_BAND = 0.05


# ---------- pure computation (unit-tested; no I/O) --------------------------


def binom_p(k: int, n: int, p: float = 0.5) -> float:
    """One-tailed P(X >= k) for X~Binomial(n, p), normal approximation.

    A small ``p`` means "k successes is surprisingly high vs the baseline"; a value
    near 1.0 means the observed count is *below* chance (the magnet ran backwards).
    """
    if n <= 0:
        return float("nan")
    mu = n * p
    sd = math.sqrt(n * p * (1 - p))
    if sd == 0:
        return 1.0
    z = (k - 0.5 - mu) / sd
    return 0.5 * math.erfc(z / math.sqrt(2))


def nearest_wall(spot: float, call_wall: float | None, put_wall: float | None) -> float | None:
    """The wall nearest to spot at day D — the predetermined H2 pin (no look-ahead)."""
    cands = [w for w in (call_wall, put_wall) if w is not None]
    if not cands:
        return None
    return min(cands, key=lambda w: abs(w - spot))


def _zgl_sane(spot: float, zgl: float | None) -> bool:
    return zgl is not None and spot > 0 and abs(zgl - spot) / spot <= ZGL_SANE_BAND


def _tally(sessions: list[dict[str, Any]]) -> dict[str, Any]:
    """Raw H1/H2 counters over the consecutive (D, D+1) pairs of ONE symbol.

    Kept separate from formatting so pooling can sum counters across symbols
    rather than re-pairing a date-merged multi-symbol list (which would compare
    one ticker's spot to another's — meaningless).
    """
    sessions = sorted(sessions, key=lambda s: s["date"])
    counts = {"h2_n": 0, "closer": 0, "dir_hit": 0, "contained": 0, "dom_closer": 0}
    long_g: list[float] = []
    short_g: list[float] = []

    for d, nxt in zip(sessions, sessions[1:]):
        s, nc = d.get("spot"), nxt.get("spot")
        if s is None or nc is None or s <= 0:
            continue

        cw, pw = d.get("call_wall"), d.get("put_wall")
        pin = nearest_wall(s, cw, pw)
        if pin is not None and cw is not None and pw is not None:
            counts["h2_n"] += 1
            if abs(nc - pin) < abs(s - pin):
                counts["closer"] += 1
            if (pin - s) * (nc - s) > 0:
                counts["dir_hit"] += 1
            lo, hi = sorted((pw, cw))
            if lo <= nc <= hi:
                counts["contained"] += 1
            dom = d.get("dom_strike")
            if dom is not None and abs(nc - dom) < abs(s - dom):
                counts["dom_closer"] += 1

        zgl = d.get("zero_gamma_level")
        if _zgl_sane(s, zgl):
            ret = abs(nc / s - 1) * 100.0
            (long_g if s >= zgl else short_g).append(ret)

    return {**counts, "long_g": long_g, "short_g": short_g}


def _format(tally: dict[str, Any]) -> dict[str, Any]:
    """Turn raw counters into the public hit-rate result shape."""
    n = tally["h2_n"]
    long_g, short_g = tally["long_g"], tally["short_g"]

    def _mean(xs: list[float]) -> float | None:
        return sum(xs) / len(xs) if xs else None

    long_mean, short_mean = _mean(long_g), _mean(short_g)
    h1_correct = (
        short_mean > long_mean
        if (long_mean is not None and short_mean is not None)
        else None
    )

    def _pct(k: int) -> float | None:
        return round(100.0 * k / n, 1) if n else None

    return {
        "h2_n": n,
        "closer_to_nearest_wall": {"k": tally["closer"], "pct": _pct(tally["closer"]), "p_vs_50": round(binom_p(tally["closer"], n), 4) if n else None},
        "closer_to_dominant_gex": {"k": tally["dom_closer"], "pct": _pct(tally["dom_closer"]), "p_vs_50": round(binom_p(tally["dom_closer"], n), 4) if n else None},
        "moved_in_pin_direction": {"k": tally["dir_hit"], "pct": _pct(tally["dir_hit"])},
        "contained_within_walls": {"k": tally["contained"], "pct": _pct(tally["contained"])},
        "h1_zgl_testable_n": len(long_g) + len(short_g),
        "h1_long_gamma_mean_abs_ret": round(long_mean, 3) if long_mean is not None else None,
        "h1_short_gamma_mean_abs_ret": round(short_mean, 3) if short_mean is not None else None,
        "h1_short_gt_long_as_theory": h1_correct,
    }


def evaluate(sessions: list[dict[str, Any]]) -> dict[str, Any]:
    """Compute H1 + H2 hit-rates over date-sorted ``sessions`` (one symbol).

    Each session dict needs: ``date, spot, zero_gamma_level, regime, total_gex,
    call_wall, put_wall, dom_strike``. Pairs are consecutive (D, D+1).
    """
    return _format(_tally(sessions))


def pool(per_symbol: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    """Pool by SUMMING per-symbol counters (never by merging sessions across
    symbols — consecutive pairs must stay within one ticker)."""
    agg = {"h2_n": 0, "closer": 0, "dir_hit": 0, "contained": 0, "dom_closer": 0}
    long_g: list[float] = []
    short_g: list[float] = []
    for sessions in per_symbol.values():
        t = _tally(sessions)
        for key in agg:
            agg[key] += t[key]
        long_g.extend(t["long_g"])
        short_g.extend(t["short_g"])
    return _format({**agg, "long_g": long_g, "short_g": short_g})


def verdict(result: dict[str, Any]) -> str:
    """Coarse GO/NO-GO/INSUFFICIENT label for the pooled result (advisory gate)."""
    n = result.get("h2_n") or 0
    if n < 20:
        return "INSUFFICIENT_SAMPLE"
    cw = result.get("closer_to_nearest_wall", {})
    pct = cw.get("pct")
    p = cw.get("p_vs_50")
    if pct is None or p is None:
        return "INSUFFICIENT_SAMPLE"
    # Walls are magnets only if next close lands closer materially more than chance.
    if pct >= 55 and p <= 0.05:
        return "GO_WALLS_PREDICTIVE"
    return "NO_GO_NO_EDGE"


# ---------- CLI I/O shell (thin; not unit-tested) ---------------------------


def _cli_path() -> Path:
    return Path(os.environ.get("UW_PP_CLI", str(DEFAULT_CLI)))


def _run_cli(cli: Path, *args: str) -> dict[str, Any]:
    try:
        out = subprocess.run(
            [str(cli), *args, "--json", "--quiet"],
            capture_output=True, text=True, timeout=120,
        )
    except (OSError, subprocess.SubprocessError):
        return {}
    try:
        return json.loads(out.stdout)
    except (json.JSONDecodeError, ValueError):
        return {}


def _walls_from_per_strike(per_strike: Iterable[dict[str, Any]], spot: float) -> dict[str, float | None]:
    """Call wall = max positive net_gex strike above spot; put wall = min (most
    negative) net_gex strike below spot; dom = strike of max |net_gex| overall."""
    above = [(r["strike"], r["net_gex"]) for r in per_strike if r["strike"] >= spot]
    below = [(r["strike"], r["net_gex"]) for r in per_strike if r["strike"] < spot]
    allr = [(r["strike"], r["net_gex"]) for r in per_strike]
    return {
        "call_wall": max(above, key=lambda x: x[1])[0] if above else None,
        "put_wall": min(below, key=lambda x: x[1])[0] if below else None,
        "dom_strike": max(allr, key=lambda x: abs(x[1]))[0] if allr else None,
    }


def reconstruct(cli: Path, symbol: str, days: int, dte_max: int) -> list[dict[str, Any]]:
    """Reconstruct per-session EOD GEX for ``symbol`` over the trailing window."""
    series = _run_cli(cli, "historical", "gex-time-series", "--symbol", symbol,
                      "--days", str(days), "--dte-max", str(dte_max))
    sessions: list[dict[str, Any]] = []
    for point in series.get("trajectory", []):
        date = point.get("date")
        if not date:
            continue
        gex = _run_cli(cli, "options-structure", "gex", "--symbol", symbol,
                       "--date", date, "--dte-max", str(dte_max))
        per_strike = gex.get("per_strike")
        spot = gex.get("underlying_price", point.get("spot"))
        if not per_strike or spot is None:
            continue
        walls = _walls_from_per_strike(per_strike, spot)
        sessions.append({
            "date": date,
            "spot": spot,
            "zero_gamma_level": gex.get("zero_gamma_level", point.get("zero_gamma_level")),
            "regime": gex.get("regime", point.get("regime")),
            "total_gex": gex.get("total_gex", point.get("total_gex")),
            **walls,
        })
    return sessions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--symbols", default="SPY,QQQ", help="Comma-separated (default SPY,QQQ).")
    parser.add_argument("--days", type=int, default=60, help="Trailing sessions to reconstruct.")
    parser.add_argument("--dte-max", type=int, default=45)
    parser.add_argument("--json", action="store_true", help="Emit JSON only.")
    args = parser.parse_args()

    cli = _cli_path()
    symbols = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]
    if not cli.exists():
        payload = {"available": False, "reason": f"uw-pp CLI not found at {cli} (set UW_PP_CLI)"}
        print(json.dumps(payload) if args.json else payload["reason"])
        return 0

    per_symbol: dict[str, list[dict[str, Any]]] = {}
    per_symbol_result: dict[str, Any] = {}
    for sym in symbols:
        sessions = reconstruct(cli, sym, args.days, args.dte_max)
        per_symbol[sym] = sessions
        per_symbol_result[sym] = evaluate(sessions)

    total = sum(len(v) for v in per_symbol.values())
    if total == 0:
        payload = {"available": False, "reason": "no sessions reconstructed (stale/empty data)"}
        print(json.dumps(payload) if args.json else payload["reason"])
        return 0

    pooled = pool(per_symbol)
    payload = {
        "available": True,
        "symbols": symbols,
        "days_requested": args.days,
        "dte_max": args.dte_max,
        "zgl_sane_band": ZGL_SANE_BAND,
        "per_symbol": per_symbol_result,
        "pooled": pooled,
        "verdict": verdict(pooled),
    }

    if args.json:
        print(json.dumps(payload, indent=2))
        return 0

    print(f"§2 next-session GEX advisory — rolling backtest (baseline 50%, n={pooled['h2_n']} pooled)")
    print(f"  verdict: {payload['verdict']}")
    for sym, r in per_symbol_result.items():
        cw = r["closer_to_nearest_wall"]
        print(f"  {sym}: closer→nearest-wall {cw['pct']}% (n={r['h2_n']}, p={cw['p_vs_50']}) | "
              f"in-pin-dir {r['moved_in_pin_direction']['pct']}% | "
              f"contained {r['contained_within_walls']['pct']}% | "
              f"H1 short>long? {r['h1_short_gt_long_as_theory']} (n={r['h1_zgl_testable_n']})")
    cw = pooled["closer_to_nearest_wall"]
    print(f"  POOLED: closer→nearest-wall {cw['pct']}% (p={cw['p_vs_50']}) | "
          f"closer→dom|GEX| {pooled['closer_to_dominant_gex']['pct']}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
