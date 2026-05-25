#!/usr/bin/env python3
"""Vol-regime magnitude scalers — register criteria C5 (VRP percentile) + C9 (term-slope).

Stdlib-only. These are the complementary "level vs slope" vol-regime scalers (ship together):
  C5 — single-name VRP **magnitude** (percentile), not just its sign. Bollerslev-Tauchen-Zhou
       (2009, RFS): the variance risk premium predicts returns and dominates P/E, the default
       spread, and CAY at the quarterly horizon. High VRP -> premium-selling edge; low/negative
       -> premium-buying. The fleet already sizes by VRP *sign* (risk-monitor L16, vol-surface
       L12); C5 adds the continuous *percentile/tercile* dimension that the sign read throws away.
  C9 — IV term-structure **slope** as a graded scaler. Johnson (2017, JFQA 52:2461): the VIX
       term-structure slope (2nd PC) prices variance risk incremental to other VRP proxies.
       Replaces the binary panic gate (front_end_iv_ratio > 1.10) with a graded size scalar.

**Status: ADVISORY-ONLY.** Per the C5/C9 (d) gates the scalers go live only when premium-selling
realised win-rate is **monotone across terciles on n >= 30 observations** — and the per-name VRP /
slope percentile series must *accrue* (>= 30 obs, building from the C1 envelopes onward; one
`historical_vrp` snapshot per date today). Until then the existing VRP *sign* sizing stays live and
these are advisory. C5 also **subsumes the 2026-05-23 P2.2 earnings_vol cap** (COMPLACENT skew ->
0.65): the VRP percentile is the continuous form of that discrete cap — ship C5, retire P2.2.
"""

from __future__ import annotations

LOW_TERCILE = 1 / 3   # <= 33rd percentile
HIGH_TERCILE = 2 / 3  # >= 66th percentile
MIN_OBS_FOR_LIVE = 30
_TERCILE_ORDER = ["LOW", "MID", "HIGH"]


def tercile(percentile: float) -> str:
    """Map a 0..1 percentile to LOW / MID / HIGH terciles."""
    if percentile <= LOW_TERCILE:
        return "LOW"
    if percentile >= HIGH_TERCILE:
        return "HIGH"
    return "MID"


def premium_selling_scalar(vrp_percentile: float | None,
                           slope_percentile: float | None = None) -> dict:
    """Advisory size scalar for a PREMIUM-SELLING (short-vol) structure from VRP + slope percentiles.

    VRP percentile is the primary dimension (C5): sell premium bigger when vol is rich (high VRP
    percentile), smaller / stand aside when cheap (low). Slope percentile (C9) is a secondary
    de-risk: a steeply backwardated front (high slope percentile) trims the short-vol size even when
    VRP is rich. Returns a multiplicative scalar in [0, 1.0] (1.0 = full per the ladder, 0 = skip)
    plus the audit terciles. ADVISORY — not yet wired to live sizing (see module docstring).
    """
    if vrp_percentile is None:
        return {"scalar": None, "vrp_tercile": None, "slope_tercile": None,
                "advisory": True, "reason": "no VRP percentile (needs >=30 accrued obs)"}
    vt = tercile(vrp_percentile)
    base = {"HIGH": 1.0, "MID": 0.5, "LOW": 0.0}[vt]  # rich -> full sell; cheap -> stand aside
    st = None
    if slope_percentile is not None:
        st = tercile(slope_percentile)
        if st == "HIGH":            # steep front backwardation -> de-risk the short
            base = min(base, 0.5)
    return {"scalar": round(base, 4), "vrp_tercile": vt, "slope_tercile": st,
            "advisory": True,
            "reason": f"VRP {vt} tercile -> base {base}" + (f"; slope {st} tercile" if st else "")}


def tercile_winrate_monotone(wr_by_tercile: dict, n_by_tercile: dict,
                             min_n: int = MIN_OBS_FOR_LIVE) -> dict:
    """C5/C9 (d) live-activation gate: is premium-selling WR monotone HIGH>=MID>=LOW on n>=min_n?

    ``wr_by_tercile``/``n_by_tercile`` keyed by LOW/MID/HIGH (computed by /calibration-audit from
    the accrued VRP-percentile-tagged closed calls). Below min_n total, or non-monotone, the scaler
    stays ADVISORY and VRP *sign* sizing remains the live behaviour.
    """
    n = sum(n_by_tercile.get(t, 0) for t in _TERCILE_ORDER)
    have_all = all(wr_by_tercile.get(t) is not None for t in _TERCILE_ORDER)
    monotone = bool(
        have_all and wr_by_tercile["HIGH"] >= wr_by_tercile["MID"] >= wr_by_tercile["LOW"]
    )
    activate = bool(n >= min_n and monotone)
    return {
        "n_obs": n, "min_n": min_n, "wr_by_tercile": wr_by_tercile,
        "monotone_high_ge_mid_ge_low": monotone, "activate_live_scaler": activate,
        "status": "LIVE" if activate else "ADVISORY_ONLY",
        "reason": (
            f"n={n} (>= {min_n}? {n >= min_n}); monotone HIGH>=MID>=LOW? {monotone} "
            f"-> {'live VRP/slope scaler' if activate else 'advisory; VRP-sign sizing stays live'}"
        ),
    }
