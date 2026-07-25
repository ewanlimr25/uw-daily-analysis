#!/usr/bin/env python3
"""Mechanized DEX sign-flip test for the +1 dealer-positioning rubric line (2026-06-12 audit P0.4).

Stdlib-only. This is the ONLY script in ``scripts/`` that computes a **scored** rubric line, and it
exists because the un-mechanized version produced a documented scoring failure: the 2026-06-11 book
awarded the then-+3 dealer-positioning line to MU/MRVL/ASML with **no DEX sign change anywhere in
their 10-day windows** — a positive DEX *level* in an up-tape was scored as a "flip". The tool
returns a snapshot with no flip field, so the level/flip distinction has to be computed, and P0.4
both demoted the line +3 -> +1 and specified it mechanically:

    sign(net_dex) on the latest session is OPPOSITE to >= 3 consecutive prior sessions,
    AND |net_dex| on the flip day >= 0.25 x the trailing-10-session median |net_dex|.

Rationale for the magnitude floor: without it, a name whose DEX oscillates around zero prints a
"flip" every other session. There is no peer-reviewed support for DEX/vanna flips as 1-4wk
directional signals (hedging pressure is intraday-mean-reverting per Baltussen et al. 2021), which
is why the line is only +1 and why the evidence string must cite dated values on both sides.

Deliberate extra output: ``sign_changes_in_window``. Both 2026-07-24 passers (MU 5 sign changes in
14 sessions, NBIS 4) needed a whipsaw caveat that previously depended on an agent remembering to
look for it. Emitting it as a field makes the caveat data-driven; ``whipsaw_warning`` fires when the
name changes sign more often than ``WHIPSAW_MAX_SIGN_CHANGES`` over the supplied history.

Series input is ``uw options-structure dex --symbol T --date D`` called once per session (the tool
has no range mode). ``--fetch`` shells out to the ``uw`` CLI for a symbol; otherwise a
``{symbol: [{date, net_dex}, ...]}`` JSON file is read, so the test is verifiable offline.

Consumed by ``dealer-positioning-strategist`` (Phase 1) to decide the +1, and by
``signal-confluence-quant`` to verify the cited evidence.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import statistics
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import date
from typing import Callable, Sequence

# --- P0.4 frozen parameters. Changing any of these changes a SCORED line: do not tune casually. ---
MIN_PRIOR_RUN = 3           # consecutive opposite-signed sessions required before the flip day
MEDIAN_WINDOW = 10          # trailing sessions for the |net_dex| median
MAGNITUDE_FLOOR_FRAC = 0.25 # flip-day |net_dex| must be >= this x the trailing median
RUBRIC_POINTS = 1           # +1 since the 2026-06-12 P0.4 demotion (was +3)

# Advisory only — does not affect the pass/fail decision, surfaces the whipsaw caveat.
WHIPSAW_MAX_SIGN_CHANGES = 3

UW_CLI = os.environ.get("UW_PP_CLI", "uw")

Runner = Callable[[Sequence[str]], str]


@dataclass(frozen=True)
class Observation:
    """One dated DEX reading. ``net_dex`` of exactly 0.0 is treated as sign-less (see _sign)."""

    date: str
    net_dex: float


@dataclass(frozen=True)
class FlipResult:
    symbol: str
    qualifies: bool
    reason: str
    direction: str | None = None  # "short" on a positive->negative flip, "long" on negative->positive
    points: int = 0
    flip_date: str | None = None
    flip_net_dex: float | None = None
    prior_run_dates: tuple[str, ...] = field(default_factory=tuple)
    prior_run_values: tuple[float, ...] = field(default_factory=tuple)
    prior_run_length: int = 0
    trailing_median_abs: float | None = None
    magnitude_floor: float | None = None
    magnitude_ratio: float | None = None
    sign_changes_in_window: int = 0
    whipsaw_warning: bool = False
    evidence: str | None = None

    def to_dict(self) -> dict:
        return {
            "symbol": self.symbol,
            "qualifies": self.qualifies,
            "reason": self.reason,
            "direction": self.direction,
            "points": self.points,
            "flip_date": self.flip_date,
            "flip_net_dex": self.flip_net_dex,
            "prior_run_dates": list(self.prior_run_dates),
            "prior_run_values": list(self.prior_run_values),
            "prior_run_length": self.prior_run_length,
            "trailing_median_abs_net_dex": self.trailing_median_abs,
            "magnitude_floor": self.magnitude_floor,
            "magnitude_ratio": (
                round(self.magnitude_ratio, 2) if self.magnitude_ratio is not None else None
            ),
            "sign_changes_in_window": self.sign_changes_in_window,
            "whipsaw_warning": self.whipsaw_warning,
            "evidence": self.evidence,
        }


def _first_present(row: dict, keys: Sequence[str]):
    """First key whose value is not None. Avoids the eager-``.get(k, default)`` trap where a present
    key holding an explicit null shadows a usable fallback key."""
    for k in keys:
        v = row.get(k)
        if v is not None:
            return v
    return None


def _sign(v: float) -> int:
    """Strict sign. Exactly 0.0 returns 0 and can neither start nor break a run."""
    return (v > 0) - (v < 0)


def count_sign_changes(obs: Sequence[Observation]) -> int:
    """Number of sign transitions across the series, ignoring zero readings."""
    signs = [s for s in (_sign(o.net_dex) for o in obs) if s != 0]
    return sum(1 for a, b in zip(signs, signs[1:]) if a != b)


_ISO_DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}\Z")


def _is_iso_date(s: str) -> bool:
    """True iff ``s`` is a strict ``YYYY-MM-DD`` calendar date.

    A regex gate is required, not just ``date.fromisoformat``: since Python 3.11 that accepts the
    full ISO-8601 grammar including week-dates, so ``"2026-W30-5"`` both parses AND has length 10
    (verified) while sorting lexicographically nowhere near its true chronological position. The
    whole series order — and therefore which session counts as "latest" — depends on this.
    """
    if not isinstance(s, str) or not _ISO_DATE_RE.match(s):
        return False
    try:
        date.fromisoformat(s)
    except (TypeError, ValueError):
        return False
    return True


def normalize(raw: Sequence[dict]) -> tuple[Observation, ...]:
    """Coerce ``[{date, net_dex}, ...]`` to observations sorted OLDEST FIRST.

    Rows with a missing/unparseable ``net_dex`` are dropped — a silently-coerced null would
    fabricate a sign. Dates MUST be strict ``YYYY-MM-DD``: sorting is lexicographic (correct and
    stable for ISO), so a non-ISO label would silently mis-order the series and therefore mis-read
    which session is "latest" — the same class of wrong-input-wrong-scored-line bug that P0.4 was
    written to fix. Non-ISO rows are dropped rather than best-effort parsed.

    Sorting is explicit because the caller collects dated calls in arbitrary order (the CLI has no
    range mode, so these are N separate invocations).
    """
    out: list[Observation] = []
    for row in raw or []:
        if not isinstance(row, dict):
            continue
        raw_date = row.get("date") or row.get("as_of") or row.get("trade_date")
        val = _first_present(row, ("net_dex", "net_delta_exposure"))
        if not raw_date or val is None:
            continue
        # Tool payloads sometimes carry a timestamp; keep the calendar-date prefix only.
        d = str(raw_date)[:10]
        if not _is_iso_date(d):
            continue
        try:
            out.append(Observation(date=d, net_dex=float(val)))
        except (TypeError, ValueError):
            continue
    return tuple(sorted(out, key=lambda o: o.date))


def evaluate(
    symbol: str,
    raw: Sequence[dict],
    min_prior_run: int = MIN_PRIOR_RUN,
    median_window: int = MEDIAN_WINDOW,
    floor_frac: float = MAGNITUDE_FLOOR_FRAC,
) -> FlipResult:
    """Apply the P0.4 mechanized flip test. Fail-closed: insufficient history never qualifies."""
    obs = normalize(raw)
    changes = count_sign_changes(obs)
    whipsaw = changes > WHIPSAW_MAX_SIGN_CHANGES
    base = dict(sign_changes_in_window=changes, whipsaw_warning=whipsaw)

    need = min_prior_run + 1
    if len(obs) < need:
        return FlipResult(
            symbol, False, f"insufficient history: {len(obs)} dated sessions, need >= {need}", **base
        )

    latest = obs[-1]
    latest_sign = _sign(latest.net_dex)
    if latest_sign == 0:
        return FlipResult(symbol, False, "latest net_dex is exactly 0 — no sign", **base)

    # The prior run must be >= min_prior_run consecutive sessions ALL of the opposite sign.
    run_vals: list[Observation] = []
    for o in reversed(obs[:-1]):
        if _sign(o.net_dex) == -latest_sign:
            run_vals.append(o)
        else:
            break
    run_vals.reverse()

    if len(run_vals) < min_prior_run:
        return FlipResult(
            symbol,
            False,
            (
                f"no sign change: prior run of opposite sign is {len(run_vals)} session(s), "
                f"need >= {min_prior_run} (a DEX *level* is not a flip)"
            ),
            prior_run_dates=tuple(o.date for o in run_vals),
            prior_run_values=tuple(o.net_dex for o in run_vals),
            prior_run_length=len(run_vals),
            **base,
        )

    # Trailing median |net_dex| EXCLUDES the flip day: the floor is a bar the flip must clear,
    # so including the flip day would let a large flip inflate its own threshold.
    hist = [abs(o.net_dex) for o in obs[:-1]][-median_window:]
    median_abs = statistics.median(hist) if hist else None
    floor = median_abs * floor_frac if median_abs is not None else None
    ratio = (abs(latest.net_dex) / floor) if floor else None

    direction = "short" if latest_sign < 0 else "long"
    evidence = (
        f"{symbol} net_dex {run_vals[-1].date} {run_vals[-1].net_dex:+,.0f} -> "
        f"{latest.date} {latest.net_dex:+,.0f}; prior {len(run_vals)} sessions "
        f"({', '.join(f'{o.date} {o.net_dex:+,.0f}' for o in run_vals)}) all "
        f"{'positive' if latest_sign < 0 else 'negative'}; "
        f"|flip| {abs(latest.net_dex):,.0f} vs floor {floor:,.0f} "
        f"({floor_frac:g}x trailing-{len(hist)} median {median_abs:,.0f})"
        if floor
        else f"{symbol} sign change {run_vals[-1].date} -> {latest.date}; magnitude floor unavailable"
    )

    common = dict(
        direction=direction,
        flip_date=latest.date,
        flip_net_dex=latest.net_dex,
        prior_run_dates=tuple(o.date for o in run_vals),
        prior_run_values=tuple(o.net_dex for o in run_vals),
        prior_run_length=len(run_vals),
        trailing_median_abs=median_abs,
        magnitude_floor=floor,
        magnitude_ratio=ratio,
        evidence=evidence,
        **base,
    )

    if floor is None:
        return FlipResult(symbol, False, "magnitude floor not computable (no prior history)", **common)
    if abs(latest.net_dex) < floor:
        return FlipResult(
            symbol,
            False,
            (
                f"sign change present but magnitude below floor: |{latest.net_dex:,.0f}| < "
                f"{floor:,.0f} ({floor_frac:g}x trailing median {median_abs:,.0f}) — whipsaw around zero"
            ),
            **common,
        )
    return FlipResult(symbol, True, "PASS: mechanized sign change clears the magnitude floor",
                      points=RUBRIC_POINTS, **common)


def _default_runner(argv: Sequence[str]) -> str:
    """Run the `uw` CLI and return stdout, raising on a non-zero exit.

    The returncode check is deliberate and mirrors ``step0_cache.py``: a degraded invocation that
    exits non-zero while still printing a plausible-looking JSON body would otherwise be accepted as
    a genuine ``net_dex`` reading for a SCORED rubric line. Garbage-in-silently-scored is precisely
    the failure class the 2026-06-12 P0.4 mechanization exists to prevent.
    """
    proc = subprocess.run(  # noqa: S603 (fixed binary, no shell)
        list(argv), capture_output=True, text=True, timeout=60, check=False
    )
    if proc.returncode != 0:
        raise OSError((proc.stderr or f"exit {proc.returncode}").strip()[:200])
    return proc.stdout


def fetch_series(
    symbol: str, dates: Sequence[str], runner: Runner | None = None
) -> tuple[list[dict], list[str]]:
    """Pull one dated ``uw options-structure dex`` call per date. Returns ``(rows, errors)``.

    Graceful-skip per date: an unparseable or empty response is recorded in ``errors`` and omitted,
    never fabricated. ``net_dex`` is read from the documented key with fallbacks.
    """
    run = runner or _default_runner
    rows: list[dict] = []
    errors: list[str] = []
    for d in dates:
        argv = [UW_CLI, "options-structure", "dex", "--symbol", symbol, "--date", d, "--json", "--quiet"]
        try:
            doc = json.loads(run(argv) or "")
        except (json.JSONDecodeError, TypeError, OSError, subprocess.SubprocessError) as exc:
            errors.append(f"{d}: {str(exc)[:120]}")
            continue
        if not isinstance(doc, dict):
            errors.append(f"{d}: unexpected payload type")
            continue
        val = _first_present(doc, ("net_dex", "net_delta_exposure"))
        if val is None:
            errors.append(f"{d}: no net_dex field")
            continue
        rows.append({"date": doc.get("date") or d, "net_dex": val})
    return rows, errors


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--file", help="JSON: {symbol: [{date, net_dex}, ...]} — offline mode")
    p.add_argument("--symbol", help="Symbol to fetch (with --dates)")
    p.add_argument("--dates", help="Comma-separated YYYY-MM-DD sessions, oldest or newest first")
    p.add_argument("--min-prior-run", type=int, default=MIN_PRIOR_RUN)
    p.add_argument("--median-window", type=int, default=MEDIAN_WINDOW)
    p.add_argument("--floor-frac", type=float, default=MAGNITUDE_FLOOR_FRAC)
    args = p.parse_args(argv)

    results: list[dict] = []
    errors: list[str] = []

    if args.file:
        try:
            with open(args.file, encoding="utf-8") as fh:
                payload = json.load(fh)
        except (OSError, json.JSONDecodeError) as exc:
            print(json.dumps({"available": False, "error": str(exc)[:200], "results": []}, indent=2))
            return 0
        for sym, rows in (payload or {}).items():
            results.append(
                evaluate(sym, rows, args.min_prior_run, args.median_window, args.floor_frac).to_dict()
            )
    elif args.symbol and args.dates:
        dates = [d.strip() for d in args.dates.split(",") if d.strip()]
        rows, errors = fetch_series(args.symbol, dates)
        results.append(
            evaluate(args.symbol, rows, args.min_prior_run, args.median_window, args.floor_frac).to_dict()
        )
    else:
        p.error("provide --file, or --symbol with --dates")

    print(
        json.dumps(
            {
                "available": True,
                "rubric_line": f"+{RUBRIC_POINTS} dealer-positioning MECHANIZED DEX flip (2026-06-12 P0.4)",
                "params": {
                    "min_prior_run": args.min_prior_run,
                    "median_window": args.median_window,
                    "magnitude_floor_frac": args.floor_frac,
                },
                "qualifying": [r["symbol"] for r in results if r["qualifies"]],
                "errors": errors,
                "results": results,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
