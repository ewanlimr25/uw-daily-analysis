#!/usr/bin/env python3
"""Step-0 shared-payload cache — fetch each market-wide `uw` payload ONCE per run.

Stdlib-only. This is an **orchestration** fix, not an analysis one. Phase 1 spawns 10-12 agents in
parallel and several of them independently pull the same market-wide payload, because each agent's
tool list names it separately. Measured on 2026-07-24: ``earnings-scout`` and ``vol-surface-scout``
both fetched ``screener earnings-catalyst`` and produced **byte-identical 528,504-byte files**
(md5 ``162d3b906dd245556774478ac665fb73``) in the same run. ``expiry-heatmap``, ``iv-rank`` and
``iv-outliers`` have 2-4 declared consumers each and were likewise re-pulled after Step 0 had
already fetched them.

The registry below therefore holds only payloads that are (a) **market-wide** — no ``--symbol``, so
one fetch genuinely serves everyone — and (b) declared by **2 or more** consumers. Per-symbol pulls
stay with the owning agent: they are not shareable and caching them would just move the work.

Contract for callers: run this once in Step 0, then pass agents the **file paths** from the manifest
plus a hard rule not to re-fetch those commands. Cached files are reused on re-invocation unless
``--refresh`` is given, which also makes a resumed or re-run report reproducible instead of
re-querying a moving tape.

Every payload graceful-skips: a failed fetch is recorded in the manifest with its error and the run
continues, exactly like the ``fz`` / Finnhub skip pattern. Always exits 0.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Sequence

UW_CLI = os.environ.get("UW_PP_CLI", "uw")
DEFAULT_TIMEOUT_S = 120.0

Runner = Callable[[Sequence[str]], str]


@dataclass(frozen=True)
class Payload:
    """One shareable Step-0 fetch.

    ``args`` is the ``uw`` argv after the binary, with ``{date}`` substituted at fetch time.
    ``consumers`` documents WHY it is in the registry — the 2-or-more rule is the entry bar, so a
    single-consumer entry is a registry bug.
    """

    name: str
    args: tuple[str, ...]
    consumers: tuple[str, ...]
    note: str = ""


# Ordered roughly as Step 0 consumes them. Every entry is market-wide (no --symbol).
SHARED_PAYLOADS: tuple[Payload, ...] = (
    Payload(
        "daily_synthesis",
        ("playbook", "daily-synthesis", "--date", "{date}"),
        ("orchestrator-step0", "all-phase1-agents"),
        "The shared context anchor. Agents are already forbidden from re-fetching it.",
    ),
    Payload(
        "market_regime",
        ("risk", "market-regime"),
        ("orchestrator-step0", "risk-monitor"),
        "risk-monitor must CONFIRM, not re-fetch.",
    ),
    Payload(
        "dte_volume_share",
        ("options-flow", "dte-volume-share", "--date", "{date}"),
        ("orchestrator-step0", "sector-rotation-strategist"),
        "MARKET-level only; never a per-sector split (2026-06-12 P1.5).",
    ),
    Payload(
        "sector_flow",
        ("options-flow", "sector-flow", "--date", "{date}"),
        ("orchestrator-step0", "sector-rotation-strategist"),
    ),
    Payload(
        "sector_flow_persistence",
        ("options-flow", "sector-flow-persistence",),
        ("orchestrator-step0", "sector-rotation-strategist"),
    ),
    Payload(
        "screener_bullish",
        ("screener", "bullish-bearish", "--direction", "bullish", "--top-n", "25", "--date", "{date}"),
        ("orchestrator-step0", "sector-rotation-strategist"),
        "NOTE: this subcommand takes --direction. `screener iv-rank` takes --mode instead.",
    ),
    Payload(
        "screener_bearish",
        ("screener", "bullish-bearish", "--direction", "bearish", "--top-n", "25", "--date", "{date}"),
        ("orchestrator-step0", "sector-rotation-strategist"),
    ),
    Payload(
        "signal_confluence_bullish",
        ("insights", "signal-confluence", "--direction", "bullish", "--min-score", "3",
         "--top-n", "25", "--date", "{date}"),
        ("orchestrator-step0-funnel-seed",),
        "Funnel seed ONLY (2026-06-12 P0.2) — earns no points and gates no entry.",
    ),
    Payload(
        "signal_confluence_bearish",
        ("insights", "signal-confluence", "--direction", "bearish", "--min-score", "3",
         "--top-n", "25", "--date", "{date}"),
        ("orchestrator-step0-funnel-seed",),
    ),
    Payload(
        "iv_rank_high",
        ("screener", "iv-rank", "--mode", "high", "--top-n", "25", "--date", "{date}"),
        ("orchestrator-step0", "vol-surface-scout", "contrarian-scanner", "earnings-scout"),
        "FLAG IS --mode, NOT --direction. Guessing --direction cost two failed calls on 2026-07-24.",
    ),
    Payload(
        "iv_rank_low",
        ("screener", "iv-rank", "--mode", "low", "--top-n", "25", "--date", "{date}"),
        ("orchestrator-step0", "vol-surface-scout"),
        "FLAG IS --mode, NOT --direction.",
    ),
    Payload(
        "volume_vs_average",
        ("screener", "volume-vs-average", "--top-n", "25", "--min-volume-ratio", "3", "--date", "{date}"),
        ("orchestrator-step0", "contrarian-scanner"),
        "2026-07-24: every row was sub-$50M-ADV micro; expect the C12 floor to empty this.",
    ),
    Payload(
        "earnings_catalyst",
        ("screener", "earnings-catalyst", "--date", "{date}"),
        ("earnings-scout", "vol-surface-scout"),
        "THE measured duplicate: both agents fetched an identical 528,504-byte payload on 2026-07-24.",
    ),
    Payload(
        "expiry_heatmap",
        ("options-flow", "expiry-heatmap", "--date", "{date}"),
        ("gamma-flip-tracker", "vol-surface-scout", "multileg-strategist"),
    ),
    Payload(
        "iv_outliers",
        ("options-flow", "iv-outliers", "--date", "{date}"),
        ("vol-surface-scout", "contrarian-scanner"),
    ),
    Payload(
        "greek_screener",
        ("options-flow", "greek-screener", "--date", "{date}"),
        ("gamma-flip-tracker", "multileg-strategist"),
    ),
    Payload(
        "top_premium_trades",
        ("options-flow", "top-premium-trades", "--top-n", "20", "--date", "{date}"),
        ("sweep-tracker", "multileg-strategist"),
    ),
    Payload(
        "most_active",
        ("hot-chains", "most-active", "--date", "{date}"),
        ("sweep-tracker", "multileg-strategist"),
    ),
    Payload(
        "oi_smart_positioning",
        ("oi", "smart-positioning", "--date", "{date}"),
        ("accumulation-hunter", "multileg-strategist"),
    ),
    Payload(
        "single_leg",
        ("options-flow", "single-leg", "--regime", "{regime}"),
        ("orchestrator-step0", "accumulation-hunter", "contrarian-scanner"),
        "C19 advisory, 0 rubric points. Root key is `signals` (not `results`/`trades`).",
    ),
    Payload(
        "vrp_spy",
        ("historical", "vrp", "--symbol", "SPY"),
        ("orchestrator-step0", "vol-surface-scout", "contrarian-scanner"),
        "vrp REQUIRES --symbol; there is no market-wide mode.",
    ),
    Payload(
        "vrp_qqq",
        ("historical", "vrp", "--symbol", "QQQ"),
        ("orchestrator-step0", "vol-surface-scout", "contrarian-scanner"),
    ),
)

BY_NAME = {p.name: p for p in SHARED_PAYLOADS}


def _default_runner(argv: Sequence[str]) -> str:
    proc = subprocess.run(  # noqa: S603 (fixed binary, no shell)
        list(argv), capture_output=True, text=True, timeout=DEFAULT_TIMEOUT_S, check=False
    )
    if proc.returncode != 0:
        raise OSError((proc.stderr or "non-zero exit").strip()[:200])
    return proc.stdout


def build_argv(payload: Payload, date: str, regime: str = "neutral") -> list[str]:
    """Materialize the argv, substituting ``{date}`` / ``{regime}`` and appending JSON flags."""
    args = [a.format(date=date, regime=regime) for a in payload.args]
    return [UW_CLI, *args, "--json", "--quiet"]


def fetch_one(
    payload: Payload,
    date: str,
    out_dir: Path,
    runner: Runner | None = None,
    regime: str = "neutral",
    refresh: bool = False,
) -> dict:
    """Fetch (or reuse) one payload. Returns a manifest entry; never raises."""
    path = out_dir / f"{payload.name}.json"
    argv = build_argv(payload, date, regime)
    entry = {
        "name": payload.name,
        "path": str(path),
        "command": " ".join(argv),
        "consumers": list(payload.consumers),
        "note": payload.note or None,
    }

    if path.exists() and not refresh:
        # Re-parse on a cache HIT: a run killed mid-write could otherwise leave a truncated file that
        # a later run silently treats as good. A bad cache entry falls through to a fresh fetch.
        try:
            with open(path, encoding="utf-8") as fh:
                json.load(fh)
            return {**entry, "ok": True, "cached": True, "bytes": path.stat().st_size}
        except (OSError, ValueError):
            pass

    try:
        text = (runner or _default_runner)(argv)
        json.loads(text)  # reject a non-JSON body before it lands on disk
        path.parent.mkdir(parents=True, exist_ok=True)
        # Write-then-rename: os.replace is atomic, so a crash cannot publish a partial file.
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(text, encoding="utf-8")
        os.replace(tmp, path)
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        return {**entry, "ok": False, "cached": False, "error": str(exc)[:200]}
    return {**entry, "ok": True, "cached": False, "bytes": len(text)}


def build_cache(
    date: str,
    out_dir: str | Path,
    runner: Runner | None = None,
    regime: str = "neutral",
    only: Sequence[str] | None = None,
    refresh: bool = False,
) -> dict:
    """Fetch every registered shared payload into ``out_dir``. Returns the manifest."""
    out = Path(out_dir)
    selected = [BY_NAME[n] for n in only if n in BY_NAME] if only else list(SHARED_PAYLOADS)
    unknown = sorted(set(only or []) - set(BY_NAME))
    entries = [fetch_one(p, date, out, runner, regime, refresh) for p in selected]
    return {
        "available": True,
        "date": date,
        "regime": regime,
        "cache_dir": str(out),
        "n_requested": len(entries),
        "n_ok": sum(1 for e in entries if e["ok"]),
        "n_failed": sum(1 for e in entries if not e["ok"]),
        "unknown_names": unknown,
        "failed": [{"name": e["name"], "error": e.get("error")} for e in entries if not e["ok"]],
        "paths": {e["name"]: e["path"] for e in entries if e["ok"]},
        "entries": entries,
    }


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--date", required=True, help="Report date YYYY-MM-DD")
    p.add_argument(
        "--out-dir",
        help="Cache directory (default analyses/daily/<date>/step0_cache)",
    )
    p.add_argument("--regime", default="neutral", help="bull|bear|neutral for the single-leg scan")
    p.add_argument("--only", help="Comma-separated subset of registry names")
    p.add_argument("--refresh", action="store_true", help="Re-fetch even when a cached file exists")
    p.add_argument("--list", action="store_true", help="Print the registry and exit")
    args = p.parse_args(argv)

    if args.list:
        print(
            json.dumps(
                {
                    "n_payloads": len(SHARED_PAYLOADS),
                    "payloads": [
                        {"name": q.name, "consumers": list(q.consumers), "note": q.note or None}
                        for q in SHARED_PAYLOADS
                    ],
                },
                indent=2,
            )
        )
        return 0

    out_dir = args.out_dir or f"analyses/daily/{args.date}/step0_cache"
    only = [s.strip() for s in args.only.split(",")] if args.only else None
    print(
        json.dumps(
            build_cache(args.date, out_dir, regime=args.regime, only=only, refresh=args.refresh),
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
