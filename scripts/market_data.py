#!/usr/bin/env python3
"""Underlying equity market data: OHLC, 20-day dollar ADV, realized vol — register criterion C12.

Stdlib-only. Closes a **documented acquisition gap**: ``excess_winrate.py`` already owns the C12
liquidity-floor *decision* (``passes_liquidity_floor``), but its docstring delegates the *data* to
"yahoo ``get_historical_stock_prices``" — i.e. the orchestrator hand-rolled the fetch every run,
and the named yahoo-MCP path is the one recorded as year-anchored/unreliable. There is no OHLC or
equity-volume source anywhere else in this repo: ``uw historical trend`` returns ``close`` plus
options fields only (no open/high/low, no share volume), so the C12 dollar-ADV numerator cannot be
built from the ``uw`` CLI at all.

Source is the **raw Yahoo chart API** (``query1.finance.yahoo.com/v8/finance/chart``), which is
verified working and correctly year-anchored — closes reconcile exactly against the ``uw`` screener
(2026-07-24: SMMT 13.66, BE 184.89, NBIS 187.77).

Three consumers, one fetch:
  0. **Caveat — index symbols have no share volume.** ``^VIX``/``^GSPC`` return volume 0, so their
     dollar ADV is 0 and they ALWAYS fail C12. That is correct (an index is not a tradable name); use
     them for tape framing only and do not read their C12 row as a liquidity finding.
  1. **Step 0 funnel (C12)** — ``price >= $5`` AND ``20d dollar ADV >= $50M``, fail-closed. This is
     the gate every downstream step consumes; a polluted funnel inflates confluence breadth and the
     win-rate denominator (Barbon & Buraschi: flow effects are strongest and least exitable in
     exactly the illiquid names the screeners surface).
  2. **Tape framing** — per-symbol ``d1``/``d5`` returns. Cap-weighted index prints can fall while
     equal-weight breadth rises; without OHLC the two are indistinguishable and a "broad bounce"
     read can be shipped into agent prompts before it is checked.
  3. **Realized vol** — close-to-close annualized RV over a window, the denominator the debate
     needs to judge whether an implied move is rich (Goyal-Saretto style IV-vs-RV comparison).

Always exits 0 and prints a valid JSON object; a symbol that cannot be fetched or measured emits
``available: false`` with a ``reason`` and is reported as C12 **FAIL** (fail-closed), never dropped
silently. Network access is injected via ``fetch``, so tests never touch the network.
"""

from __future__ import annotations

import argparse
import http.client
import json
import math
import statistics
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Callable, Iterable, Sequence

from excess_winrate import MIN_ADV_USD, MIN_PRICE

CHART_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range={range}&interval=1d"

# Yahoo's public chart endpoint 403s a default urllib agent; a browser UA is required.
DEFAULT_USER_AGENT = "Mozilla/5.0"
DEFAULT_TIMEOUT_S = 20.0

# 20 sessions is the C12 window; fetch 2mo so a holiday-shortened month still yields 20 rows.
ADV_WINDOW = 20
DEFAULT_RANGE = "2mo"
TRADING_DAYS_PER_YEAR = 252

# Realized-vol windows the debate lane quotes (short + medium).
DEFAULT_RV_WINDOWS = (20, 60)

Fetcher = Callable[[str], str]


@dataclass(frozen=True)
class Bar:
    """One daily OHLCV bar. ``date`` is the UTC calendar date of the session stamp."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: float


@dataclass(frozen=True)
class SymbolData:
    """Measured market data for one symbol, or ``available=False`` with a reason."""

    symbol: str
    available: bool
    reason: str | None = None
    bars: tuple[Bar, ...] = field(default_factory=tuple)

    # --- derived (None when not measurable) ---
    last_date: str | None = None
    last_close: float | None = None
    adv_usd: float | None = None
    adv_window_n: int | None = None
    change_1d_pct: float | None = None
    change_5d_pct: float | None = None
    realized_vol: dict[str, float | None] = field(default_factory=dict)

    def c12_verdict(
        self, min_adv: float = MIN_ADV_USD, min_price: float = MIN_PRICE
    ) -> tuple[bool, str]:
        """Return ``(passes, reason)`` for the C12 floor. Fail-closed on unmeasurable data."""
        if not self.available:
            return False, self.reason or "unavailable"
        if self.last_close is None or self.adv_usd is None:
            return False, "price or adv_usd not measurable"
        if self.last_close < min_price:
            return False, f"price {self.last_close:.2f} < {min_price:.2f}"
        if self.adv_usd < min_adv:
            return False, f"adv ${self.adv_usd / 1e6:.1f}M < ${min_adv / 1e6:.0f}M"
        return True, "pass"


def _http_get(url: str, timeout: float = DEFAULT_TIMEOUT_S) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": DEFAULT_USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310 (fixed https host)
        return resp.read().decode("utf-8")


def parse_chart(payload: str) -> tuple[Bar, ...]:
    """Parse a Yahoo chart response into complete bars, oldest first.

    Rows with a null close or null volume are dropped — Yahoo emits placeholder nulls for
    halted sessions and for the in-progress bar, and a null would silently zero an ADV term.
    Raises ``ValueError`` on a payload that is not a usable chart response.
    """
    try:
        doc = json.loads(payload)
    except (json.JSONDecodeError, TypeError) as exc:
        raise ValueError(f"not JSON: {exc}") from exc

    chart = (doc or {}).get("chart") or {}
    if chart.get("error"):
        raise ValueError(f"chart error: {chart['error']}")
    results = chart.get("result") or []
    if not results:
        raise ValueError("no chart.result")

    node = results[0] or {}
    stamps = node.get("timestamp") or []
    quotes = (node.get("indicators") or {}).get("quote") or [{}]
    q = quotes[0] or {}
    opens, highs = q.get("open") or [], q.get("high") or []
    lows, closes, vols = q.get("low") or [], q.get("close") or [], q.get("volume") or []

    def at(seq: Sequence[float | None], i: int) -> float | None:
        return seq[i] if i < len(seq) else None

    bars: list[Bar] = []
    for i, ts in enumerate(stamps):
        c, v = at(closes, i), at(vols, i)
        if c is None or v is None:
            continue
        o, h, lo = at(opens, i), at(highs, i), at(lows, i)
        bars.append(
            Bar(
                date=datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d"),
                open=float(o if o is not None else c),
                high=float(h if h is not None else c),
                low=float(lo if lo is not None else c),
                close=float(c),
                volume=float(v),
            )
        )
    if not bars:
        raise ValueError("no complete bars")
    return tuple(bars)


def dollar_adv(bars: Sequence[Bar], window: int = ADV_WINDOW) -> tuple[float | None, int]:
    """Mean ``close * volume`` over the trailing ``window`` bars. Returns ``(adv, n_used)``.

    Deliberately DOLLAR volume (shares x close), not a share count — the C12 floor is notional.
    Uses however many bars exist when fewer than ``window`` are available and reports ``n_used``
    so a short history is visible rather than hidden.
    """
    if not bars:
        return None, 0
    tail = list(bars)[-window:]
    return statistics.fmean(b.close * b.volume for b in tail), len(tail)


def pct_change(bars: Sequence[Bar], sessions: int) -> float | None:
    """Percent change of close over ``sessions`` bars back. ``None`` when history is too short."""
    if sessions <= 0 or len(bars) < sessions + 1:
        return None
    prior = bars[-(sessions + 1)].close
    if not prior:
        return None
    return 100.0 * (bars[-1].close / prior - 1.0)


def realized_vol(bars: Sequence[Bar], window: int) -> float | None:
    """Annualized close-to-close realized vol (%) over ``window`` sessions.

    Population stdev of log returns x sqrt(252). ``None`` when fewer than 3 returns are
    available (a 2-point stdev is not a vol estimate).
    """
    tail = list(bars)[-(window + 1) :]
    rets = [
        math.log(b.close / a.close)
        for a, b in zip(tail, tail[1:])
        if a.close > 0 and b.close > 0
    ]
    if len(rets) < 3:
        return None
    return statistics.pstdev(rets) * math.sqrt(TRADING_DAYS_PER_YEAR) * 100.0


def measure(
    symbol: str,
    fetch: Fetcher | None = None,
    adv_window: int = ADV_WINDOW,
    rv_windows: Iterable[int] = DEFAULT_RV_WINDOWS,
    range_: str = DEFAULT_RANGE,
    as_of: str | None = None,
) -> SymbolData:
    """Fetch and measure one symbol. Never raises — failures become ``available=False``.

    ``as_of`` (``YYYY-MM-DD``) truncates the series to bars on or before that date, so a re-run or a
    later ``/calibration-audit`` reproduces the same C12 verdict instead of silently measuring a
    newer tape. Every other call in the pipeline pins ``--date``; this is the equivalent. Without it
    the chart API always returns the latest sessions.
    """
    getter = fetch or _http_get
    # safe="^" keeps index tickers (^VIX) intact. NOTE: it also drops "/" from the default safe
    # set, so a class-share ticker would encode as %2F — Yahoo's own convention is BRK-B, not BRK/B,
    # so normalize upstream if a slashed symbol ever reaches here.
    url = CHART_URL.format(
        symbol=urllib.parse.quote(symbol, safe="^"),
        range=urllib.parse.quote(range_, safe=""),
    )
    try:
        bars = parse_chart(getter(url))
    except (
        ValueError,
        urllib.error.URLError,
        # http.client.HTTPException is NOT an OSError subclass (verified), so IncompleteRead /
        # BadStatusLine on a mid-response connection drop would otherwise escape and break the
        # module's always-exit-0 contract.
        http.client.HTTPException,
        OSError,
        TimeoutError,
    ) as exc:
        return SymbolData(
            symbol=symbol, available=False, reason=f"{type(exc).__name__}: {exc}"[:200]
        )

    if as_of:
        bars = tuple(b for b in bars if b.date <= as_of)
        if not bars:
            return SymbolData(
                symbol=symbol, available=False, reason=f"no bars on or before as_of {as_of}"
            )

    adv, n_used = dollar_adv(bars, adv_window)
    return SymbolData(
        symbol=symbol,
        available=True,
        bars=bars,
        last_date=bars[-1].date,
        last_close=bars[-1].close,
        adv_usd=adv,
        adv_window_n=n_used,
        change_1d_pct=pct_change(bars, 1),
        change_5d_pct=pct_change(bars, 5),
        realized_vol={f"rv{w}": realized_vol(bars, w) for w in rv_windows},
    )


def _row(d: SymbolData, min_adv: float, min_price: float) -> dict:
    passes, reason = d.c12_verdict(min_adv, min_price)
    return {
        "symbol": d.symbol,
        "available": d.available,
        "reason": d.reason,
        "last_date": d.last_date,
        # 4dp preserves sub-penny ETF quotes without leaking float32 noise from the API.
        "last_close": round(d.last_close, 4) if d.last_close is not None else None,
        "adv_usd": round(d.adv_usd, 2) if d.adv_usd is not None else None,
        "adv_usd_millions": round(d.adv_usd / 1e6, 1) if d.adv_usd is not None else None,
        "adv_window_n": d.adv_window_n,
        "change_1d_pct": round(d.change_1d_pct, 2) if d.change_1d_pct is not None else None,
        "change_5d_pct": round(d.change_5d_pct, 2) if d.change_5d_pct is not None else None,
        "realized_vol_pct": {
            k: (round(v, 1) if v is not None else None) for k, v in d.realized_vol.items()
        },
        "c12_pass": passes,
        "c12_reason": reason,
    }


def build_report(
    symbols: Sequence[str],
    fetch: Fetcher | None = None,
    min_adv: float = MIN_ADV_USD,
    min_price: float = MIN_PRICE,
    adv_window: int = ADV_WINDOW,
    rv_windows: Iterable[int] = DEFAULT_RV_WINDOWS,
    as_of: str | None = None,
) -> dict:
    """Measure every symbol and split it by the C12 floor. Always returns a valid payload."""
    rv_windows = tuple(rv_windows)
    rows = [
        _row(measure(s, fetch, adv_window, rv_windows, as_of=as_of), min_adv, min_price)
        for s in symbols
        if s.strip()
    ]
    return {
        "source": "yahoo_chart_api",
        "as_of": as_of,
        "min_price": min_price,
        "min_adv_usd": min_adv,
        "adv_window": adv_window,
        "n_requested": len(rows),
        "c12_pass": [r["symbol"] for r in rows if r["c12_pass"]],
        "c12_fail": [
            {"symbol": r["symbol"], "reason": r["c12_reason"]} for r in rows if not r["c12_pass"]
        ],
        "symbols": rows,
    }


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--symbols", required=True, help="Comma-separated symbols (e.g. SPY,QQQ,^VIX)")
    p.add_argument("--min-adv", type=float, default=MIN_ADV_USD)
    p.add_argument("--min-price", type=float, default=MIN_PRICE)
    p.add_argument("--adv-window", type=int, default=ADV_WINDOW)
    p.add_argument(
        "--rv-windows",
        default=",".join(str(w) for w in DEFAULT_RV_WINDOWS),
        help="Comma-separated realized-vol windows in sessions",
    )
    p.add_argument(
        "--as-of",
        help="Pin to YYYY-MM-DD: drop bars after this date so the run is reproducible. "
        "Every other pipeline call pins --date; do the same here.",
    )
    p.add_argument("--compact", action="store_true", help="Drop the per-symbol detail rows")
    args = p.parse_args(argv)

    try:
        rv_windows = tuple(int(w) for w in args.rv_windows.split(",") if w.strip())
    except ValueError:
        rv_windows = DEFAULT_RV_WINDOWS

    report = build_report(
        [s.strip().upper() for s in args.symbols.split(",")],
        min_adv=args.min_adv,
        min_price=args.min_price,
        adv_window=args.adv_window,
        rv_windows=rv_windows,
        as_of=args.as_of,
    )
    if args.compact:
        report.pop("symbols", None)
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
