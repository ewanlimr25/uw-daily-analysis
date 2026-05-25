#!/usr/bin/env python3
"""Expectancy + fractional-Kelly sizing — register criterion C3 (ADVISORY until n>=30).

Stdlib-only. The conviction ladder sizes purely on hit-rate (>=0.70 full / 0.50-0.70 half).
But a 55% strategy at 3:1 payoff dominates a 70% strategy at 1:1 — desks size on EXPECTED VALUE,
not hit-rate alone. Kelly (1956): the growth-optimal fraction is

    f* = W - (1 - W) / R       (W = win-rate, R = payoff ratio = avg_win / avg_loss)

Half-Kelly captures ~75% of the growth at ~50% of the drawdown, and stable estimates need
~50-100 trades. This module computes the per-call expectancy and the **capped half-Kelly,
floored at 0** that C3 will eventually use as the sizing input.

**Status: ADVISORY-ONLY.** Per the C3 (d) gate, this becomes the live sizer ONLY once
tier x expectancy is monotone on **n >= 30 closed calls**. The repo logs no realised P&L yet
(decision envelopes only just began accruing realised fields), so until n>=30 the existing
win-rate ladder remains the live sizer and these numbers are reported as advisory in the audit.
``tier_expectancy_monotone`` is the gate /calibration-audit evaluates before any live switch.
"""

from __future__ import annotations

from dataclasses import dataclass

MIN_CLOSED_CALLS_FOR_LIVE = 30   # C3 (d): live sizer only at n >= 30 closed calls
DEFAULT_KELLY_FRACTION = 0.5     # half-Kelly
# Single-name allocation cap. Half-Kelly = 0.5*f*, and f* = W - (1-W)/R < 1 for any W < 1 and
# finite R, so half-Kelly < 0.5 always holds and a 0.5 cap would never bind. 0.25 is a meaningful
# desk cap that DOES bind on high-edge bets (no >25% allocation on a single name).
DEFAULT_MAX_FRACTION = 0.25
_TIER_ORDER = ["LOW", "MEDIUM", "HIGH"]


def payoff_ratio(avg_win_pct: float, avg_loss_pct: float) -> float | None:
    """R = avg_win / |avg_loss|. None when there are no losses to form a ratio."""
    denom = abs(avg_loss_pct)
    if denom == 0:
        return None
    return avg_win_pct / denom


def expectancy(win_rate: float, avg_win_pct: float, avg_loss_pct: float) -> float:
    """Per-trade expected value in % = W*avg_win - (1-W)*|avg_loss|."""
    return round(win_rate * avg_win_pct - (1.0 - win_rate) * abs(avg_loss_pct), 4)


def full_kelly(win_rate: float, r: float | None) -> float:
    """Full-Kelly fraction f* = W - (1-W)/R. 0.0 when R is None/<=0 (no edge to size)."""
    if r is None or r <= 0:
        return 0.0
    return round(win_rate - (1.0 - win_rate) / r, 4)


def capped_half_kelly(win_rate: float, r: float | None,
                      kelly_frac: float = DEFAULT_KELLY_FRACTION,
                      max_fraction: float = DEFAULT_MAX_FRACTION) -> float:
    """Capped fractional-Kelly, floored at 0: max(0, min(kelly_frac * f*, max_fraction)).

    Negative full-Kelly (no edge) floors to 0 — do not take the trade.
    """
    f = full_kelly(win_rate, r)
    return round(max(0.0, min(kelly_frac * f, max_fraction)), 4)


def kelly_to_size_bucket(fraction: float, max_fraction: float = DEFAULT_MAX_FRACTION) -> str:
    """Advisory mapping of a capped-half-Kelly fraction to the ladder's size labels.

    Buckets are fractions of ``max_fraction`` so the mapping tracks the cap: >=2/3 -> full,
    >=1/3 -> half, >0 -> starter, 0 -> skip. Advisory only — for side-by-side comparison with
    the live win-rate ladder, not (yet) a live sizing decision.
    """
    if max_fraction <= 0 or fraction <= 0:
        return "skip"
    ratio = fraction / max_fraction
    if ratio >= 2 / 3:
        return "full"
    if ratio >= 1 / 3:
        return "half"
    return "starter"


@dataclass(frozen=True)
class ClosedCall:
    tier: str            # HIGH | MEDIUM | LOW
    realized_pnl_pct: float
    won: bool


def tier_expectancy_monotone(closed: list[ClosedCall],
                             min_n: int = MIN_CLOSED_CALLS_FOR_LIVE) -> dict:
    """C3 (d) live-activation gate: is per-tier mean realised P&L monotone HIGH>=MED>=LOW on n>=min_n?

    Returns the per-tier expectancy, n, monotonicity, and whether the live half-Kelly sizer may
    activate. Below min_n (or non-monotone) the sizer stays ADVISORY and the win-rate ladder is live.

    Closed calls whose ``tier`` is not one of HIGH/MEDIUM/LOW (e.g. DROP/watch_only) are
    intentionally excluded from ``n`` and the tier means — only sized tiers count toward activation.
    """
    by_tier: dict[str, list[float]] = {t: [] for t in _TIER_ORDER}
    for c in closed:
        if c.tier in by_tier:
            by_tier[c.tier].append(c.realized_pnl_pct)
    n = sum(len(v) for v in by_tier.values())
    tier_exp = {t: (round(sum(v) / len(v), 4) if v else None) for t, v in by_tier.items()}

    have_all = all(tier_exp[t] is not None for t in _TIER_ORDER)
    monotone = bool(have_all and tier_exp["HIGH"] >= tier_exp["MEDIUM"] >= tier_exp["LOW"])
    activate_live = bool(n >= min_n and monotone)
    return {
        "n_closed": n, "min_n": min_n, "tier_expectancy": tier_exp,
        "monotone_high_ge_med_ge_low": monotone, "activate_live_sizer": activate_live,
        "status": "LIVE" if activate_live else "ADVISORY_ONLY",
        "reason": (
            f"n={n} (>= {min_n}? {n >= min_n}); monotone HIGH>=MED>=LOW? {monotone} "
            f"({tier_exp}) -> {'live half-Kelly sizer' if activate_live else 'advisory only; win-rate ladder stays live'}"
        ),
    }
