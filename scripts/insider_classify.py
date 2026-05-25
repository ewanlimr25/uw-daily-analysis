#!/usr/bin/env python3
"""Opportunistic-vs-routine insider classification — register criterion C10.

Stdlib-only. Cohen, Malloy & Pomorski (2012, JF 67:1009) "Decoding Inside Information": a
portfolio of **opportunistic** insiders earns ~82bps/month abnormal; **routine** insiders earn
~0. Routine trades are calendar-scheduled (the insider sells in the same month every year — a
liquidity/diversification pattern carrying ~zero information); opportunistic trades are the ones
that predict future news and earnings-announcement returns. `fundamentals-gate` currently uses
raw MSPR (all insiders equally weighted), which dilutes the signal — C10 splits them.

**Routine rule:** an insider's trade in calendar month M is ROUTINE if that insider also traded
in month M in **>= 3 distinct prior years** (a fixed-calendar pattern). Otherwise OPPORTUNISTIC.

Status: the classification logic ships + is tested here; **verdict accuracy vs outcome is measured
at the next audit** (forward). On the current build the Finnhub insider endpoints returned empty
(`insider_signal: unknown` for every name in the 2026-05-22 run), so `fundamentals-gate` cannot yet
exercise the opportunistic-only MSPR live — it falls back to the existing neutral/unknown handling
(NA never penalises). Wiring is best-effort: `/stock/insider-transactions` (per-trade, per-insider)
may require a paid Finnhub plan; when unavailable, the gate uses raw MSPR exactly as today.
"""

from __future__ import annotations

from dataclasses import dataclass

MIN_PRIOR_YEARS_FOR_ROUTINE = 3


@dataclass(frozen=True)
class InsiderTxn:
    insider: str
    year: int
    month: int       # 1..12
    shares: float    # +buy / -sell (net share change)


def is_routine(trade_month: int, prior_year_months: list[tuple[int, int]],
               min_prior_years: int = MIN_PRIOR_YEARS_FOR_ROUTINE) -> bool:
    """Routine if the insider traded in the SAME calendar month in >= min_prior_years distinct years."""
    years_in_same_month = {y for (y, m) in prior_year_months if m == trade_month}
    return len(years_in_same_month) >= min_prior_years


def classify_transactions(txns: list[InsiderTxn],
                          min_prior_years: int = MIN_PRIOR_YEARS_FOR_ROUTINE) -> list[dict]:
    """Tag each transaction routine|opportunistic using only PRIOR-year history of the same insider.

    A transaction is judged against the same insider's trades in earlier years (look-back only — the
    current and future years never inform the label), so the classification is point-in-time.
    """
    by_insider: dict[str, list[tuple[int, int]]] = {}
    for t in txns:
        by_insider.setdefault(t.insider, []).append((t.year, t.month))

    out = []
    for t in txns:
        prior = [(y, m) for (y, m) in by_insider[t.insider] if y < t.year]
        routine = is_routine(t.month, prior, min_prior_years)
        out.append({"insider": t.insider, "year": t.year, "month": t.month,
                    "shares": t.shares, "class": "routine" if routine else "opportunistic"})
    return out


def opportunistic_signal(txns: list[InsiderTxn],
                         min_prior_years: int = MIN_PRIOR_YEARS_FOR_ROUTINE) -> dict:
    """Net buy/sell + an MSPR-like score (-100..100) computed from OPPORTUNISTIC trades only.

    MSPR-like score = 100 * net_opportunistic_shares / gross_opportunistic_shares (so +100 = all
    opportunistic buying, -100 = all opportunistic selling). None when there are no opportunistic
    trades to score (caller treats as 'unknown' — never a penalty, per the gate's NA rule).
    """
    classified = classify_transactions(txns, min_prior_years)
    opp = [c for c in classified if c["class"] == "opportunistic"]
    net = sum(c["shares"] for c in opp)
    gross = sum(abs(c["shares"]) for c in opp)
    score = round(100.0 * net / gross, 2) if gross > 0 else None
    return {
        "n_opportunistic": len(opp), "n_routine": len(classified) - len(opp),
        "net_opportunistic_shares": net,
        "opportunistic_mspr_like": score,
        "signal": ("unknown" if score is None
                   else "buying" if score >= 20 else "selling" if score <= -20 else "neutral"),
    }
