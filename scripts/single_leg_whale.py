#!/usr/bin/env python3
"""Single-leg large-premium options print scanner + next-session backtest.

Identifies single-leg, ask-side, large-premium prints on individual common stocks
from the UW All Options Parquet data, and backtests whether they predict next-day
price moves in the direction of the trade.

Academic basis
--------------
Pan & Poteshman (2006, RFS 19:871): ONLY opening buy option volume predicts stock
returns — ~+40bps next day / +1%/week for opening calls/puts. Closing flow predicts
nothing. Key discriminator: size >> open_interest = opening position.

Easley, O'Hara & Srinivas (1998): Large option trades contain private information,
especially when the order aggressively hits the ask.

Chakravarty, Gulen & Mayhew (2004): Price discovery in options markets concentrates
in single-leg directional trades, not spread activity.

OPRA condition code taxonomy
-----------------------------
Single-leg electronic : auto, slan, isoi, slai   — clean signal lane
Single-leg floor/neg  : slft, slcn               — institutional blocks
Multi-leg             : mlet, mlat, mlft, mfsl,  — spreads/hedges/rolls; NOT directional
                        mesl, masl, mlct
Cabinet (cbmo)        : deep-OTM near-zero value — portfolio restructuring; TRASH
Two-leg               : tlet, tlat, tlft, tlct   — ambiguous; excluded

Usage
-----
  python3 scripts/single_leg_whale.py --scan-date 2026-05-28 [--json]
  python3 scripts/single_leg_whale.py --backtest [--min-premium 500000] [--json]

Exit 0 always; ``available:false`` signals data/dependency missing.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

try:
    import duckdb as _duckdb  # installed alongside the uw CLI (Parquet substrate)
    _DUCKDB_OK = True
except ImportError:
    _DUCKDB_OK = False

# ─── constants ────────────────────────────────────────────────────────────────

DATA_DIR = Path.home() / "Documents" / "Stocks" / "All Options"
DEFAULT_MIN_PREMIUM = 500_000
DEFAULT_TOP_N = 25

SINGLE_LEG_CONDITIONS = frozenset(["auto", "slan", "isoi", "slft", "slai", "slcn"])
ELECTRONIC_CONDITIONS = frozenset(["auto", "isoi"])
AUCTION_CONDITIONS    = frozenset(["slan", "slai"])
FLOOR_CONDITIONS      = frozenset(["slft", "slcn"])

# Index/ETF symbols to exclude from single-stock analysis
_EXCLUDE = frozenset(["SPX", "SPXW", "NDX", "RUT", "SPY", "QQQ", "IWM", "DIA",
                       "XSP", "VIX", "VXST"])

# Backtest verdict thresholds
_VERDICT_MIN_N       = 20
_VERDICT_MIN_WR      = 0.60
_VERDICT_MIN_EXCESS  = 0.05


# ─── data types ───────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class WhaleSignal:
    ticker: str
    option_type: str        # 'call' | 'put'
    strike: float
    expiry: date
    dte: int
    signal_price: float     # underlying_price at time of print
    option_price: float
    size: int
    premium: float
    open_interest: int
    size_oi_ratio: float    # size / max(OI, 1); OI=0 → 999.0
    delta: float
    implied_volatility: float
    paid_over_ask: float    # option_price − nbbo_ask; ≥ 0 = aggressive fill
    condition: str
    condition_class: str    # 'electronic' | 'auction' | 'floor'
    executed_at: str
    trade_date: date


@dataclass
class GradedSignal:
    signal: WhaleSignal
    next_close: float | None = None
    holding_return: float | None = None   # positive = trade direction won
    won: bool | None = None


# ─── pure computation ─────────────────────────────────────────────────────────

def _size_oi_bucket(ratio: float) -> str:
    if ratio >= 2.0:  return "2_plus"
    if ratio >= 1.0:  return "1_to_2"
    if ratio >= 0.5:  return "0.5_to_1"
    return "0_to_0.5"


def _dte_bucket(dte: int) -> str:
    if dte <=  7: return "0_to_7"
    if dte <= 30: return "8_to_30"
    if dte <= 90: return "31_to_90"
    return "91_plus"


def _condition_class(cond: str) -> str:
    if cond in ELECTRONIC_CONDITIONS: return "electronic"
    if cond in AUCTION_CONDITIONS:    return "auction"
    return "floor"


def _binom_p(k: int, n: int, p: float = 0.5) -> float:
    """One-tailed P(X ≥ k) for X ~ Binomial(n, p), normal approximation."""
    if n <= 0:
        return float("nan")
    mu = n * p
    sd = math.sqrt(n * p * (1 - p))
    if sd == 0:
        return 1.0
    z = (k - 0.5 - mu) / sd
    return 0.5 * math.erfc(z / math.sqrt(2))


def _tally(graded: list[GradedSignal]) -> dict[str, Any]:
    scored = [g for g in graded if g.won is not None]
    n    = len(scored)
    wins = sum(1 for g in scored if g.won)
    wr   = round(wins / n, 4) if n else None
    return {"n": n, "wins": wins, "losses": n - wins, "win_rate": wr}


def _verdict(stats: dict, excess: float | None) -> str:
    if stats["n"] < _VERDICT_MIN_N:
        return "INSUFFICIENT_SAMPLE"
    wr = stats["win_rate"] or 0.0
    if wr >= _VERDICT_MIN_WR and excess is not None and excess >= _VERDICT_MIN_EXCESS:
        return "GO_SIGNAL_HAS_EDGE"
    if wr >= 0.55:
        return "MARGINAL_EDGE_VERIFY"
    return "NO_GO_NO_EDGE"


# ─── data discovery ───────────────────────────────────────────────────────────

def _discover_dates() -> list[date]:
    if not DATA_DIR.exists():
        return []
    dates: list[date] = []
    for f in DATA_DIR.glob("bot-eod-report-*.parquet"):
        try:
            dates.append(date.fromisoformat(f.stem.replace("bot-eod-report-", "")))
        except ValueError:
            pass
    return sorted(dates)


def _parquet_path(dt: date) -> Path:
    return DATA_DIR / f"bot-eod-report-{dt}.parquet"


def _consecutive_pairs(dates: list[date]) -> list[tuple[date, date]]:
    """(D, D+1) pairs where D+1 is within 4 calendar days — excludes data gaps."""
    return [
        (dates[i], dates[i + 1])
        for i in range(len(dates) - 1)
        if (dates[i + 1] - dates[i]).days <= 4
    ]


# ─── parquet loaders ──────────────────────────────────────────────────────────

def _load_signals(dt: date, min_premium: float) -> list[WhaleSignal]:
    """Extract clean single-leg whale signals from one day's All Options parquet."""
    p = _parquet_path(dt)
    if not p.exists():
        return []
    cond_list = ", ".join(f"'{c}'" for c in SINGLE_LEG_CONDITIONS)
    excl_list = ", ".join(f"'{s}'" for s in _EXCLUDE)
    con = _duckdb.connect()
    rows = con.execute(f"""
        SELECT
            underlying_symbol,
            option_type,
            CAST(strike AS DOUBLE)          AS strike,
            CAST(expiry  AS DATE)           AS expiry,
            CAST(price              AS DOUBLE) AS opt_price,
            CAST(size               AS BIGINT) AS sz,
            CAST(premium            AS DOUBLE) AS prem,
            COALESCE(CAST(open_interest AS BIGINT), 0) AS oi,
            CAST(implied_volatility AS DOUBLE) AS iv,
            CAST(delta              AS DOUBLE) AS delta,
            CAST(price - nbbo_ask   AS DOUBLE) AS paid_over_ask,
            CAST(underlying_price   AS DOUBLE) AS underlying_price,
            upstream_condition_detail,
            CAST(executed_at AS VARCHAR)       AS executed_at
        FROM read_parquet('{p}')
        WHERE canceled = false
          AND equity_type = 'Common Stock'
          AND underlying_symbol NOT IN ({excl_list})
          AND upstream_condition_detail IN ({cond_list})
          AND side = 'ask'
          AND premium >= {min_premium}
          AND underlying_price >= 5.0
        ORDER BY premium DESC
    """).fetchall()

    signals: list[WhaleSignal] = []
    for row in rows:
        (sym, opt_type, strike, expiry_dt, opt_price, sz, prem,
         oi, iv, delta, poa, underlying_price, condition, exec_at) = row
        if expiry_dt is None or not underlying_price or underlying_price <= 0:
            continue
        dte = (expiry_dt - dt).days
        if dte < 0:
            continue
        ratio = round(sz / max(oi, 1), 4)
        if oi == 0 and sz > 0:
            ratio = 999.0
        signals.append(WhaleSignal(
            ticker=sym,
            option_type=opt_type,
            strike=float(strike),
            expiry=expiry_dt,
            dte=dte,
            signal_price=float(underlying_price),
            option_price=float(opt_price),
            size=int(sz),
            premium=float(prem),
            open_interest=int(oi),
            size_oi_ratio=ratio,
            delta=float(delta) if delta is not None else 0.0,
            implied_volatility=float(iv) if iv is not None else 0.0,
            paid_over_ask=float(poa) if poa is not None else float("nan"),
            condition=condition,
            condition_class=_condition_class(condition),
            executed_at=str(exec_at),
            trade_date=dt,
        ))
    return signals


def _load_closes(dt: date, tickers: set[str]) -> dict[str, float]:
    """Last underlying_price per ticker as an EOD close proxy."""
    p = _parquet_path(dt)
    if not p.exists():
        return {}
    ticker_list = ", ".join(f"'{t}'" for t in tickers | {"SPY"})
    con = _duckdb.connect()
    rows = con.execute(f"""
        SELECT underlying_symbol,
               LAST(underlying_price ORDER BY executed_at) AS last_price
        FROM read_parquet('{p}')
        WHERE underlying_symbol IN ({ticker_list})
          AND canceled = false
        GROUP BY underlying_symbol
    """).fetchall()
    return {r[0]: float(r[1]) for r in rows if r[1] is not None}


# ─── deduplication ────────────────────────────────────────────────────────────

def _dedup(signals: list[WhaleSignal]) -> list[WhaleSignal]:
    """One signal per (ticker, option_type) per day — largest premium print wins.

    Prevents double-counting when many block fills happen on the same contract.
    A ticker can have both a call AND a put signal on the same day (each is kept).
    """
    best: dict[tuple[str, str], WhaleSignal] = {}
    for s in signals:
        key = (s.ticker, s.option_type)
        if key not in best or s.premium > best[key].premium:
            best[key] = s
    return list(best.values())


# ─── scan mode ────────────────────────────────────────────────────────────────

def scan(scan_date: date, min_premium: float, top_n: int) -> dict:
    if not _DUCKDB_OK:
        return {"available": False, "reason": "duckdb not installed"}
    signals = _dedup(_load_signals(scan_date, min_premium))
    signals.sort(key=lambda s: (-s.premium, -s.size_oi_ratio))

    out = []
    for s in signals[:top_n]:
        out.append({
            "ticker": s.ticker,
            "option_type": s.option_type,
            "strike": s.strike,
            "expiry": s.expiry.isoformat(),
            "dte": s.dte,
            "dte_bucket": _dte_bucket(s.dte),
            "signal_price": round(s.signal_price, 2),
            "option_price": round(s.option_price, 4),
            "size": s.size,
            "premium_usd": round(s.premium),
            "open_interest": s.open_interest,
            "size_oi_ratio": s.size_oi_ratio,
            "size_oi_bucket": _size_oi_bucket(s.size_oi_ratio),
            "delta": round(s.delta, 4),
            "implied_volatility": round(s.implied_volatility, 4),
            "paid_over_ask": round(s.paid_over_ask, 3) if not math.isnan(s.paid_over_ask) else None,
            "aggression": "aggressive" if (not math.isnan(s.paid_over_ask) and s.paid_over_ask >= 0) else "passive",
            "condition": s.condition,
            "condition_class": s.condition_class,
            "directional_bias": "bullish" if s.option_type == "call" else "bearish",
            "executed_at": s.executed_at,
        })

    return {
        "available": True,
        "scan_date": scan_date.isoformat(),
        "min_premium_usd": min_premium,
        "total_signals_raw": len(_load_signals(scan_date, min_premium)),
        "deduped_signals": len(signals),
        "signals": out,
    }


# ─── backtest mode ────────────────────────────────────────────────────────────

def backtest(min_premium: float) -> dict:
    if not _DUCKDB_OK:
        return {"available": False, "reason": "duckdb not installed"}

    all_dates = _discover_dates()
    pairs = _consecutive_pairs(all_dates)
    if not pairs:
        return {"available": False, "reason": "no consecutive trading day pairs in data"}

    gaps_skipped = [
        {"from": all_dates[i].isoformat(), "to": all_dates[i + 1].isoformat(),
         "calendar_days": (all_dates[i + 1] - all_dates[i]).days}
        for i in range(len(all_dates) - 1)
        if (all_dates[i + 1] - all_dates[i]).days > 4
    ]

    all_graded: list[GradedSignal] = []
    days_with_signals = 0

    # Gather SPY closes per date (reuse across pairs)
    spy_closes: dict[date, float] = {}
    for dt in all_dates:
        c = _load_closes(dt, set())  # SPY is always added inside _load_closes
        if "SPY" in c:
            spy_closes[dt] = c["SPY"]

    for d0, d1 in pairs:
        raw = _load_signals(d0, min_premium)
        if not raw:
            continue
        signals = _dedup(raw)
        tickers = {s.ticker for s in signals}
        closes_d1 = _load_closes(d1, tickers)
        days_with_signals += 1

        for s in signals:
            next_close = closes_d1.get(s.ticker)
            if next_close is None or s.signal_price <= 0:
                all_graded.append(GradedSignal(signal=s))
                continue
            raw_ret = (next_close - s.signal_price) / s.signal_price
            # Puts win on DOWN moves: flip sign so positive = win for any direction
            holding_return = raw_ret if s.option_type == "call" else -raw_ret
            all_graded.append(GradedSignal(
                signal=s,
                next_close=round(next_close, 2),
                holding_return=round(holding_return, 4),
                won=holding_return > 0,
            ))

    # SPY baseline: fraction of trading-day pairs where SPY moved in each direction
    spy_call_wins = spy_put_wins = spy_n = 0
    for d0, d1 in pairs:
        s0, s1 = spy_closes.get(d0), spy_closes.get(d1)
        if s0 and s1 and s0 > 0:
            spy_n += 1
            if (s1 - s0) > 0:
                spy_call_wins += 1
            else:
                spy_put_wins += 1
    spy_call_wr = round(spy_call_wins / spy_n, 4) if spy_n else None
    spy_put_wr  = round(spy_put_wins  / spy_n, 4) if spy_n else None

    graded = [g for g in all_graded if g.won is not None]
    n    = len(graded)
    wins = sum(1 for g in graded if g.won)
    wr   = round(wins / n, 4) if n else None

    calls = [g for g in graded if g.signal.option_type == "call"]
    puts  = [g for g in graded if g.signal.option_type == "put"]
    call_stats = _tally(calls)
    put_stats  = _tally(puts)

    def _excess(stats: dict, baseline: float | None) -> float | None:
        if stats["win_rate"] is None or baseline is None:
            return None
        return round(stats["win_rate"] - baseline, 4)

    call_exc = _excess(call_stats, spy_call_wr)
    put_exc  = _excess(put_stats,  spy_put_wr)

    def _strat(key_fn: Any) -> dict[str, Any]:
        groups: dict[str, list[GradedSignal]] = {}
        for g in graded:
            groups.setdefault(key_fn(g.signal), []).append(g)
        return {k: _tally(v) for k, v in sorted(groups.items())}

    # Sample: most recent 3 pairs, highest premium
    recent_d0s = {p[0] for p in pairs[-3:]}
    recent = sorted(
        [g for g in all_graded if g.signal.trade_date in recent_d0s and g.won is not None],
        key=lambda g: -g.signal.premium,
    )[:10]
    sample_out = [
        {
            "trade_date":      g.signal.trade_date.isoformat(),
            "ticker":          g.signal.ticker,
            "option_type":     g.signal.option_type,
            "strike":          g.signal.strike,
            "dte":             g.signal.dte,
            "premium_usd":     round(g.signal.premium),
            "size_oi_ratio":   g.signal.size_oi_ratio,
            "condition":       g.signal.condition,
            "signal_price":    round(g.signal.signal_price, 2),
            "next_close":      g.next_close,
            "holding_return":  g.holding_return,
            "won":             g.won,
        }
        for g in recent
    ]

    return {
        "available": True,
        "backtest_type": "single_leg_whale_next_session",
        "as_of_date": all_dates[-1].isoformat(),
        "parameters": {
            "min_premium_usd": min_premium,
            "single_leg_conditions": sorted(SINGLE_LEG_CONDITIONS),
            "side_filter": "ask",
            "equity_type_filter": "Common Stock",
            "aggregate_method": "max_premium_print_per_ticker_per_option_type_per_day",
        },
        "data_coverage": {
            "trading_days_available": len(all_dates),
            "consecutive_pairs_used": len(pairs),
            "days_with_signals": days_with_signals,
            "total_graded_signals": n,
            "ungraded_no_next_day_data": len(all_graded) - n,
            "gaps_skipped": gaps_skipped,
        },
        "spy_baseline": {
            "n_days": spy_n,
            "call_baseline_win_rate": spy_call_wr,
            "put_baseline_win_rate":  spy_put_wr,
        },
        "overall": {
            "n": n, "wins": wins, "losses": n - wins, "win_rate": wr,
            "p_value_vs_50pct": round(_binom_p(wins, n), 4) if n else None,
        },
        "calls": {
            **call_stats,
            "spy_baseline":  spy_call_wr,
            "excess":        call_exc,
            "p_value":       round(_binom_p(call_stats["wins"], call_stats["n"]), 4),
            "verdict":       _verdict(call_stats, call_exc),
        },
        "puts": {
            **put_stats,
            "spy_baseline":  spy_put_wr,
            "excess":        put_exc,
            "p_value":       round(_binom_p(put_stats["wins"], put_stats["n"]), 4),
            "verdict":       _verdict(put_stats, put_exc),
        },
        "by_size_oi_ratio":    _strat(lambda s: _size_oi_bucket(s.size_oi_ratio)),
        "by_dte":              _strat(lambda s: _dte_bucket(s.dte)),
        "by_condition_class":  _strat(lambda s: s.condition_class),
        "by_aggression":       _strat(lambda s: "aggressive" if (
                                   not math.isnan(s.paid_over_ask) and s.paid_over_ask >= 0
                               ) else "passive"),
        "by_option_type":      {"call": call_stats, "put": put_stats},
        "sample_recent_signals": sample_out,
    }


# ─── CLI ──────────────────────────────────────────────────────────────────────

def _print_scan(r: dict) -> None:
    print(f"\n=== Single-Leg Whale Signals — {r['scan_date']} ===")
    print(f"Min premium ${r['min_premium_usd']:,.0f}  |  Deduped signals: {r['deduped_signals']}\n")
    hdr = f"{'Ticker':<8} {'Type':<5} {'Strike':>8} {'Expiry':<12} {'DTE':>4}  "
    hdr += f"{'Prem $M':>7}  {'Size/OI':>7}  {'Cond':<8}  {'Aggrn':<10}  {'Bias'}"
    print(hdr)
    print("-" * 82)
    for s in r["signals"]:
        print(
            f"{s['ticker']:<8} {s['option_type']:<5} {s['strike']:>8.0f} "
            f"{s['expiry']:<12} {s['dte']:>4}  "
            f"{s['premium_usd']/1e6:>7.2f}  {s['size_oi_ratio']:>7.3f}  "
            f"{s['condition']:<8}  {s['aggression']:<10}  {s['directional_bias']}"
        )


def _print_backtest(r: dict) -> None:
    cov = r["data_coverage"]
    ov  = r["overall"]
    spy = r["spy_baseline"]
    print(f"\n=== Single-Leg Whale Backtest — as of {r['as_of_date']} ===")
    print(f"Data: {cov['trading_days_available']} days  |  {cov['consecutive_pairs_used']} pairs  |  {cov['total_graded_signals']} graded signals\n")
    print(f"OVERALL       n={ov['n']:>4}  WR={ov['win_rate']}  p={ov['p_value_vs_50pct']}")
    c = r["calls"]
    p = r["puts"]
    print(f"CALLS         n={c['n']:>4}  WR={c['win_rate']}  SPY={spy['call_baseline_win_rate']}  excess={c['excess']:+.4f}  {c['verdict']}")
    print(f"PUTS          n={p['n']:>4}  WR={p['win_rate']}  SPY={spy['put_baseline_win_rate']}  excess={p['excess']:+.4f}  {p['verdict']}")
    for section, data in [
        ("Size/OI ratio", r["by_size_oi_ratio"]),
        ("DTE bucket",    r["by_dte"]),
        ("Condition",     r["by_condition_class"]),
        ("Aggression",    r["by_aggression"]),
    ]:
        print(f"\n{section}:")
        for k, v in data.items():
            print(f"  {k:<18}  n={v['n']:>4}  WR={v['win_rate']}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Single-leg whale scanner + backtest.")
    parser.add_argument("--scan-date", metavar="YYYY-MM-DD")
    parser.add_argument("--backtest", action="store_true")
    parser.add_argument("--min-premium", type=float, default=DEFAULT_MIN_PREMIUM, metavar="USD")
    parser.add_argument("--top-n", type=int, default=DEFAULT_TOP_N)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    if not args.scan_date and not args.backtest:
        parser.error("specify --scan-date YYYY-MM-DD or --backtest")

    if args.scan_date:
        try:
            dt = date.fromisoformat(args.scan_date)
        except ValueError:
            parser.error(f"invalid date: {args.scan_date}")
        result = scan(dt, args.min_premium, args.top_n)
    else:
        result = backtest(args.min_premium)

    if args.as_json:
        print(json.dumps(result, indent=2, default=str))
    else:
        if not result.get("available"):
            print(f"[unavailable] {result.get('reason', '')}")
        elif "signals" in result:
            _print_scan(result)
        else:
            _print_backtest(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())

# ── Production note ───────────────────────────────────────────────────────────
# This module is the RESEARCH / BACKTEST harness (it owns the D→D+1 grading).
# The production per-session scan is now the `uw` CLI subcommand:
#     uw options-flow single-leg --regime <bull|bear|neutral> --json --quiet
# which applies the same single-leg condition-code + size/OI + DTE filters and
# grades each print by the Signal Quality Hierarchy (internal/analysis/singleleg.go).
# See analyses/audit/2026-05-29/single_leg_whale_implementation_plan.md.
