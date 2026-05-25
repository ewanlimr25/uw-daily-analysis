#!/usr/bin/env python3
"""OI-confirmed-opening gate for the scored directional flow classes — register criterion C4.

Stdlib-only. Pan & Poteshman (2006, RFS 19:871): the predictive option-volume signal is built
**only from buy-to-open volume** — low-minus-high opening P/C earns ~+40bps next day / +1%/week.
The edge *disappears* without isolating opening flow. A sweep/print that CLOSES a position or
churns intraday is noise; one that OPENS new institutional risk is signal.

This is the **aggregate** opening gate (buildable today from `historical_oi_trend` /
`oi_biggest_increases` / `oi_decrease_with_volume`): a name's flow is "opening" when its open
interest is rising as net-new positioning, not when high volume churns against flat/falling OI.
The per-contract buy-to-open vs sell-to-open split (tool N1) is deferred until this aggregate
version shows lift at the next audit (per the register's "build N1 only if the interim clears").

Used by `signal-confluence-quant` as a **downgrade-only sizing gate** (parallel to the C2
market-excess gate): when `dominant_signal_class` is `bullish_flow`/`bearish_flow` and opening is
NOT confirmed, the pre-risk size is capped at half — the flow is closing/day-trading, not the
informed opening positioning the class's win-rate was meant to capture. Applies to ALL names,
not just the mega-cap subset that sweep-tracker's existing cum_flow-direction filter covered.
"""

from __future__ import annotations

# ΔOI as a fraction of the day's contract volume above which the flow is opening-dominant.
OPENING_OI_FRACTION = 0.20

_BUILDING = {"BUILDING", "RISING", "INCREASING"}
# ROLLING_OFF = position rolling out of the current strike/expiry = net-closing from here.
_CLOSING = {"FALLING", "DECLINING", "DECREASING", "ROLLING_OFF"}
# Unknown trend strings ("FLAT", "STABLE", "SIDEWAYS", ...) intentionally fall through to the
# ΔOI/volume ratio test rather than confirming or rejecting on the trend label alone.

_SIZE_RANK = {"skip": 0, "starter": 1, "half": 2, "full": 3}


def oi_opening_confirmed(
    delta_oi: float | None,
    day_contract_volume: float | None,
    oi_trend: str | None = None,
    fraction: float = OPENING_OI_FRACTION,
) -> bool:
    """True iff the name's flow is OPENING new positioning (not closing / churn).

    Confirmation logic (aggregate proxy for buy-to-open):
      1. ``historical_oi_trend`` BUILDING (multi-day OI rising) -> confirmed.
      2. ``historical_oi_trend`` FALLING/DECLINING -> NOT confirmed (OI shrinking = closing).
      3. Otherwise fall back to today's ΔOI / contract-volume ratio: opening-dominant when
         ``delta_oi / day_contract_volume >= fraction`` (and ΔOI positive). A high-volume day
         with flat/negative ΔOI is churn/closing -> NOT confirmed.

    Fail-closed: if neither the trend nor the ratio can be evaluated, returns False (the desk
    will not full-size a flow class it cannot confirm is opening).
    """
    if oi_trend:
        t = oi_trend.strip().upper()
        if t in _BUILDING:
            return True
        if t in _CLOSING:
            return False
    if delta_oi is None or not day_contract_volume:
        return False
    if delta_oi <= 0:
        return False
    return (delta_oi / day_contract_volume) >= fraction


def opening_gate_size(
    base_size: str,
    dominant_signal_class: str,
    delta_oi: float | None = None,
    day_contract_volume: float | None = None,
    oi_trend: str | None = None,
    fraction: float = OPENING_OI_FRACTION,
) -> dict:
    """Downgrade-only sizing gate for the directional flow classes (C4).

    Only applies when ``dominant_signal_class`` is ``bullish_flow`` or ``bearish_flow``. When
    opening is unconfirmed the size is capped at ``half`` (never raised). Returns an audit dict.
    """
    applies = dominant_signal_class in ("bullish_flow", "bearish_flow")
    if not applies:
        return {"applies": False, "opening_confirmed": None, "final_size": base_size,
                "reason": f"C4 gate n/a for class {dominant_signal_class!r}"}

    confirmed = oi_opening_confirmed(delta_oi, day_contract_volume, oi_trend, fraction)
    if confirmed:
        return {"applies": True, "opening_confirmed": True, "final_size": base_size,
                "reason": "OI-confirmed opening (Pan-Poteshman) — no C4 cap"}
    # cap at half (downgrade only)
    capped = base_size if _SIZE_RANK[base_size] <= _SIZE_RANK["half"] else "half"
    return {"applies": True, "opening_confirmed": False, "final_size": capped,
            "reason": "opening UNCONFIRMED (flat/falling OI vs day volume = closing/churn) -> cap half"}
