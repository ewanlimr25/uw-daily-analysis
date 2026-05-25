#!/usr/bin/env python3
"""Post-Earnings Announcement Drift (PEAD) backtest — register criterion C7.

Stdlib-only. Tests the most-replicated anomaly in finance (Bernard & Thomas 1989/1990:
top-minus-bottom SUE decile ~= 18% annualised over the 60 days post-announcement) on THIS
repo's data, to decide whether the fleet should ship a scored ``earnings_drift`` swing-long
line in ``earnings-scout``.

The (d) acceptance gate (C7): a positive-SUE cohort's **10-trading-day forward EXCESS return
over SPY** must be positive with **hit-rate > 0.55 on n >= 10** before the scored line ships.
Below that bar the generator is advisory-only (0 rubric points) and the scored line is re-opened.

Data split (deliberate, given the constraints):
  - Earnings events + surprise%: Finnhub ``/stock/earnings`` (this script can fetch directly —
    free tier, stdlib urllib, key via _env). The ``period`` field is the report date.
  - Prices: supplied as a JSON ``{ticker: {"YYYY-MM-DD": close}}`` map (incl. "SPY"), fetched
    by the caller from yahoo ``get_historical_stock_prices`` (MCP, not stdlib-reachable).
    Yahoo ``get_earning_dates`` is broken on the current build — earnings dates come from
    Finnhub, NOT yahoo.

Forward window is counted in TRADING days (entries in the sorted price series), so weekends /
holidays are handled naturally. Entry = first close strictly AFTER the report date; exit =
``fwd_days`` sessions later. Look-ahead guard: events with report_date > --as-of are dropped.

Usage:
    # pure-aggregate mode (events + prices supplied):
    python3 scripts/pead_backtest.py --events-file ev.json --prices-file px.json --as-of 2026-05-22
    # fetch surprises from Finnhub for a ticker list, prices still supplied:
    python3 scripts/pead_backtest.py --tickers AMD,NVDA,... --prices-file px.json --as-of 2026-05-22
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _env import get_key  # noqa: E402

# C7 (d) acceptance thresholds
MIN_N = 10
MIN_HIT_RATE = 0.55
FWD_TRADING_DAYS = 10
BENCHMARK = "SPY"


@dataclass(frozen=True)
class EarningsEvent:
    ticker: str
    report_date: str   # YYYY-MM-DD (Finnhub /stock/earnings `period`)
    surprise_pct: float


def _sorted_dates(series: dict) -> list[str]:
    return sorted(series.keys())


def forward_return(series: dict, report_date: str, fwd_days: int) -> float | None:
    """Return over the fwd_days TRADING-day window starting the first session AFTER report_date.

    None if there is no post-report session or fewer than fwd_days sessions remain.
    """
    dates = _sorted_dates(series)
    after = [d for d in dates if d > report_date]
    if len(after) <= fwd_days:
        return None
    entry_close = series[after[0]]
    exit_close = series[after[fwd_days]]
    if not (isinstance(entry_close, (int, float)) and isinstance(exit_close, (int, float))) or entry_close <= 0:
        return None
    return exit_close / entry_close - 1.0


def event_excess(event: EarningsEvent, prices: dict, fwd_days: int = FWD_TRADING_DAYS) -> dict | None:
    """Per-event forward return, SPY-benchmark return over the same window, and excess.

    The benchmark window is anchored to the SAME post-report calendar dates as the name (so the
    market move being subtracted is contemporaneous). None if either leg can't be computed.
    """
    name_series = prices.get(event.ticker)
    spy_series = prices.get(BENCHMARK)
    if not isinstance(name_series, dict) or not isinstance(spy_series, dict):
        return None
    name_dates = [d for d in _sorted_dates(name_series) if d > event.report_date]
    if len(name_dates) <= fwd_days:
        return None
    entry_date, exit_date = name_dates[0], name_dates[fwd_days]

    name_ret = forward_return(name_series, event.report_date, fwd_days)
    # SPY benchmark over the identical [entry_date, exit_date] calendar span.
    if entry_date not in spy_series or exit_date not in spy_series:
        return None
    spy_entry, spy_exit = spy_series[entry_date], spy_series[exit_date]
    if not (isinstance(spy_entry, (int, float)) and isinstance(spy_exit, (int, float))) or spy_entry <= 0:
        return None
    spy_ret = spy_exit / spy_entry - 1.0
    if name_ret is None:
        return None
    return {
        "ticker": event.ticker, "report_date": event.report_date,
        "surprise_pct": event.surprise_pct, "entry_date": entry_date, "exit_date": exit_date,
        "fwd_return_pct": round(name_ret * 100, 3), "spy_return_pct": round(spy_ret * 100, 3),
        "excess_pct": round((name_ret - spy_ret) * 100, 3),
    }


def run_backtest(events: list[EarningsEvent], prices: dict, as_of: str,
                 fwd_days: int = FWD_TRADING_DAYS, min_n: int = MIN_N,
                 min_hit_rate: float = MIN_HIT_RATE) -> dict:
    """Positive-SUE cohort 10d-forward excess-return backtest + C7 (d) verdict."""
    positive = [e for e in events if e.surprise_pct > 0 and e.report_date <= as_of]
    # Strict point-in-time: drop any event whose forward window EXITS after as_of — we must
    # not consume prices that postdate the as-of (matters when as_of falls mid-window).
    rows = [
        r for e in positive
        if (r := event_excess(e, prices, fwd_days)) is not None and r["exit_date"] <= as_of
    ]
    n = len(rows)
    if n == 0:
        return {"n": 0, "verdict": "INSUFFICIENT_SAMPLE", "mean_excess_pct": None,
                "hit_rate": None, "rows": [], "reason": "no positive-SUE events with a full forward window"}

    wins = sum(1 for r in rows if r["excess_pct"] > 0)
    hit_rate = round(wins / n, 4)
    mean_excess = round(sum(r["excess_pct"] for r in rows) / n, 4)

    if n < min_n:
        verdict = "INSUFFICIENT_SAMPLE"
    elif mean_excess > 0 and hit_rate > min_hit_rate:
        verdict = "GO_SHIP_SCORED_LINE"
    else:
        verdict = "NO_GO_ADVISORY_ONLY"

    return {
        "n": n, "wins": wins, "hit_rate": hit_rate, "mean_excess_pct": mean_excess,
        "fwd_trading_days": fwd_days, "min_n": min_n, "min_hit_rate": min_hit_rate,
        "verdict": verdict,
        "reason": (
            f"n={n} (>= {min_n}? {n >= min_n}), hit_rate={hit_rate} (> {min_hit_rate}? {hit_rate > min_hit_rate}), "
            f"mean_excess={mean_excess}% (> 0? {mean_excess > 0})"
        ),
        "rows": sorted(rows, key=lambda r: r["excess_pct"], reverse=True),
    }


# ---------- Finnhub fetch (optional; prices always supplied) -----------------


def fetch_events(tickers: list[str], as_of: str, key: str, getter: "object | None" = None) -> list[EarningsEvent]:
    """Fetch trailing EPS-surprise events per ticker from Finnhub /stock/earnings."""
    import finnhub_enrich as fe  # local module, same dir

    getter = getter or fe._http_get_json
    out: list[EarningsEvent] = []
    for t in tickers:
        sym = t.strip().upper()
        if not sym or not fe.is_us_ticker(sym):
            continue
        try:
            resp = fe.finnhub_get("/stock/earnings", {"symbol": sym, "limit": 8}, key, getter)
        except fe.FinnhubError:
            continue
        for r in fe.summarize_earnings(resp, as_of):
            sp = r.get("surprise_pct")
            period = r.get("period", "")
            if isinstance(sp, (int, float)) and period:
                out.append(EarningsEvent(ticker=sym, report_date=str(period), surprise_pct=float(sp)))
    return out


def _events_from_json(payload: object) -> list[EarningsEvent]:
    out = []
    rows = payload.get("events", payload) if isinstance(payload, dict) else payload
    for r in rows if isinstance(rows, list) else []:
        if isinstance(r, dict) and "ticker" in r and "report_date" in r and "surprise_pct" in r:
            out.append(EarningsEvent(r["ticker"].upper(), str(r["report_date"]), float(r["surprise_pct"])))
    return out


def main() -> int:
    p = argparse.ArgumentParser(description="PEAD 10d-forward excess-return backtest (C7)")
    p.add_argument("--prices-file", required=True, help="JSON {ticker: {date: close}} incl SPY")
    p.add_argument("--events-file", help="JSON {events:[{ticker,report_date,surprise_pct}]}")
    p.add_argument("--tickers", help="comma list to fetch surprises from Finnhub")
    p.add_argument("--as-of", required=True)
    p.add_argument("--fwd-days", type=int, default=FWD_TRADING_DAYS)
    args = p.parse_args()

    prices = json.loads(Path(args.prices_file).read_text(encoding="utf-8"))

    if args.events_file:
        events = _events_from_json(json.loads(Path(args.events_file).read_text(encoding="utf-8")))
    elif args.tickers:
        key = get_key("FINNHUB_API_KEY")
        if not key:
            print(json.dumps({"available": False, "skip_reason": "FINNHUB_API_KEY not set"}))
            return 0
        events = fetch_events([t for t in args.tickers.split(",")], args.as_of, key)
    else:
        p.error("supply --events-file or --tickers")

    print(json.dumps(run_backtest(events, prices, args.as_of, args.fwd_days), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
