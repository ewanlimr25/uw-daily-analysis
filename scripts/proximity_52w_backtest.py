#!/usr/bin/env python3
"""52-week-high proximity swing backtest — register criterion C8.

Stdlib-only. George & Hwang (2004, JF 59:2145): *nearness to the 52-week high* dominates
past-return momentum in forecasting power, does not reverse long-run, and is profitable in
18 of 20 international markets (an anchoring effect). The flow book has flow-momentum but no
price-structure anchor; this tests whether to add one.

The (d) acceptance gate (C8): swing-long forward win-rate for candidates **>95% of the 52-week
high** must beat candidates **<80% of it** by **>= 10pp on n >= 15** before a conditional `+1`
(near-high long / far-from-high short) ships. Below that bar the gate stays withheld / advisory.

Inputs (same split as the PEAD backtest): a ``{ticker: {date: close}}`` price map (>= ~1y history,
yahoo ``get_historical_stock_prices`` period=1y), an ``entry_date``, and the forward window in
TRADING days. ``pct_of_52w_high`` = entry close / max(trailing-252-session high). Forward return is
the close-to-close move over ``fwd_days`` sessions after entry. Look-ahead guard: only sessions
<= entry_date feed the 52w high; only sessions in (entry, entry+fwd] feed the forward return.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

NEAR_HIGH = 0.95      # >= 95% of the 52-week high
FAR_FROM_HIGH = 0.80  # < 80% of the 52-week high
MIN_N = 15
MIN_SPLIT = 0.10      # near-WR - far-WR must be >= 10pp
FWD_TRADING_DAYS = 10
TRAILING_SESSIONS_52W = 252


def pct_of_52w_high(series: dict, entry_date: str,
                    trailing: int = TRAILING_SESSIONS_52W) -> float | None:
    """Entry close as a fraction of the trailing-52w high (sessions <= entry_date only)."""
    upto = sorted(d for d in series if d <= entry_date)
    if not upto:
        return None
    window = upto[-trailing:]
    closes = [series[d] for d in window if isinstance(series[d], (int, float))]
    if not closes:
        return None
    hi = max(closes)
    entry = series.get(entry_date)
    if not isinstance(entry, (int, float)) or hi <= 0:
        return None
    return entry / hi


def forward_return(series: dict, entry_date: str, fwd_days: int = FWD_TRADING_DAYS) -> float | None:
    after = sorted(d for d in series if d > entry_date)
    if len(after) < fwd_days:
        return None
    entry = series.get(entry_date)
    exit_close = series[after[fwd_days - 1]]
    if not (isinstance(entry, (int, float)) and isinstance(exit_close, (int, float))) or entry <= 0:
        return None
    return exit_close / entry - 1.0


def run_backtest(prices: dict, entry_date: str, fwd_days: int = FWD_TRADING_DAYS,
                 min_n: int = MIN_N, min_split: float = MIN_SPLIT) -> dict:
    """Split candidates into near-high (>=95%) vs far-from-high (<80%); compare forward WR."""
    near, far = [], []
    for ticker, series in prices.items():
        if not isinstance(series, dict):
            continue
        pct = pct_of_52w_high(series, entry_date)
        ret = forward_return(series, entry_date, fwd_days)
        if pct is None or ret is None:
            continue
        row = {"ticker": ticker, "pct_of_52w_high": round(pct, 4), "fwd_return_pct": round(ret * 100, 3)}
        if pct >= NEAR_HIGH:
            near.append(row)
        elif pct < FAR_FROM_HIGH:
            far.append(row)

    def _wr(rows):
        if not rows:
            return None
        return round(sum(1 for r in rows if r["fwd_return_pct"] > 0) / len(rows), 4)

    near_wr, far_wr = _wr(near), _wr(far)
    n = len(near) + len(far)
    split = round(near_wr - far_wr, 4) if (near_wr is not None and far_wr is not None) else None

    if near_wr is None or far_wr is None or n < min_n:
        verdict = "INSUFFICIENT_SAMPLE"
    elif split >= min_split:
        verdict = "GO_SHIP_CONDITIONAL_PLUS_ONE"
    else:
        verdict = "NO_GO_WITHHOLD"

    return {
        "entry_date": entry_date, "fwd_trading_days": fwd_days,
        "n_near": len(near), "n_far": len(far), "n_total": n, "min_n": min_n,
        "near_high_wr": near_wr, "far_from_high_wr": far_wr, "wr_split": split, "min_split": min_split,
        "verdict": verdict,
        "reason": (
            f"near(>=95%) WR={near_wr} (n={len(near)}), far(<80%) WR={far_wr} (n={len(far)}); "
            f"split={split} (>= {min_split}? {split is not None and split >= min_split}); "
            f"n={n} (>= {min_n}? {n >= min_n})"
        ),
        "near": sorted(near, key=lambda r: r["pct_of_52w_high"], reverse=True),
        "far": sorted(far, key=lambda r: r["pct_of_52w_high"]),
    }


def main() -> int:
    p = argparse.ArgumentParser(description="52-week-high proximity swing backtest (C8)")
    p.add_argument("--prices-file", required=True, help="JSON {ticker: {date: close}}, >=1y history")
    p.add_argument("--entry-date", required=True)
    p.add_argument("--fwd-days", type=int, default=FWD_TRADING_DAYS)
    args = p.parse_args()
    prices = json.loads(Path(args.prices_file).read_text(encoding="utf-8"))
    print(json.dumps(run_backtest(prices, args.entry_date, args.fwd_days), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
