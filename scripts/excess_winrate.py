#!/usr/bin/env python3
"""Liquidity floor + market-excess win-rate gate for the conviction sizer.

Stdlib-only (no pip installs; runs under the already-allowed ``Bash(python3:*)``).
Two responsibilities, shared by improvement-criteria-register criteria **C12** and **C2**
(``analyses/audit/2026-05-25/improvement_criteria.md``):

  C12 — :func:`apply_liquidity_floor` drops candidates below a 20-day dollar-ADV / price
        floor BEFORE they enter the candidate funnel or the win-rate denominator.
  C2  — :func:`n_conditional_cap` (tightened so ``n < 10`` caps below the full-size line) +
        :func:`market_excess` + :func:`size_decision` turn a raw backtest win-rate into a
        pre-risk size that beta-in-an-up-tape cannot clear.

Why this exists: the UW ``historical_signal_backtest`` tool has no liquidity floor and no
regime control. A ``volume_spike`` probe on 2026-05-20 returned GIF/BLCN/PEX/IGLD/UTHY/ESGE —
micro-ETFs the desk cannot fill at size, which also poison the win-rate denominator. A
``bullish_flow`` probe returned a 100% win-rate over 8 signals dated 05-19/05-20, in an
UPTREND where SPY itself was one of the "signals" — i.e. beta, not edge. This module is the
deterministic, auditable floor + excess gate that catches both.

Academic basis: Barbon & Buraschi (gamma/flow effects strongest in the least-liquid names —
exactly where a flow-follower is least able to exit); Bollerslev-Tauchen-Zhou and
López de Prado (an unconditional, multiply-tested win-rate blends regimes and inflates edge).

The agent populates ``price`` and ``adv_usd`` from yahoo ``get_historical_stock_prices``
(or a screener field) and ``benchmark_win_rate`` from the same-window SPY directional
outcome. This module does the arithmetic so the decision is reproducible and testable.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

# ----- C12 liquidity floor thresholds ---------------------------------------
MIN_ADV_USD = 50_000_000.0  # 20-day average *dollar* volume floor ($50M notional)
MIN_PRICE = 5.0             # sub-$5 / penny floor


@dataclass(frozen=True)
class Candidate:
    """One screened name. ``price``/``adv_usd`` come from yahoo or a screener field.

    ``won`` (when graded) feeds the win-rate denominator; ``None`` means ungraded.
    """

    ticker: str
    price: float | None = None
    adv_usd: float | None = None  # 20-day average dollar volume
    won: bool | None = None       # graded directional outcome, optional


def passes_liquidity_floor(
    c: Candidate, min_adv: float = MIN_ADV_USD, min_price: float = MIN_PRICE
) -> bool:
    """True iff the name clears BOTH the dollar-ADV and price floors.

    Fail-closed: a name whose ``price`` or ``adv_usd`` could not be measured FAILS the
    floor. The desk cannot size what it cannot measure, and an unverifiable name must not
    inflate the win-rate denominator. Legit large-caps always have this data via yahoo, so
    fail-closed only removes names the agent could not confirm are tradable.
    """
    if c.price is None or c.adv_usd is None:
        return False
    return c.price >= min_price and c.adv_usd >= min_adv


def apply_liquidity_floor(
    candidates: list[Candidate],
    min_adv: float = MIN_ADV_USD,
    min_price: float = MIN_PRICE,
) -> tuple[list[Candidate], list[Candidate]]:
    """Split candidates into (kept, excluded) by the liquidity floor.

    Used in two places: (1) the Step-0 funnel, so junk never reaches the agents; and
    (2) the win-rate denominator, so a class is not credited for un-tradable names.
    """
    kept: list[Candidate] = []
    excluded: list[Candidate] = []
    for c in candidates:
        (kept if passes_liquidity_floor(c, min_adv, min_price) else excluded).append(c)
    return kept, excluded


def compute_win_rate(candidates: list[Candidate]) -> tuple[int, int, float | None]:
    """Win-rate over GRADED candidates only. Returns (wins, n_graded, win_rate|None)."""
    graded = [c for c in candidates if c.won is not None]
    wins = sum(1 for c in graded if c.won)
    n = len(graded)
    return wins, n, (wins / n if n else None)


# ----- C2 market-excess + tightened N-conditional cap -----------------------
#
# The sizing ladder (calibrated on RAW win-rate by the 2026-05-15 audit) is preserved:
#   >= 0.70 -> full | 0.50-0.70 -> half | < 0.50 -> starter/skip.
# C2 adds two guards ON TOP of that ladder, neither of which recalibrates the thresholds:
#   1. A TIGHTER N-conditional cap: n < 10 caps at 0.69 (one notch BELOW the 0.70 full line),
#      so an 8-signal up-week class can size at most half. (Was 0.75, which still cleared full.)
#   2. A MARKET-EXCESS gate: if a signal does not beat the same-direction SPY bet over the same
#      windows (excess <= 0), it is beta not edge -> cap at half; materially negative -> starter.
#      The gate can only DOWNGRADE; it never upgrades.
MATERIALLY_NEGATIVE_EXCESS = -0.10  # signal underperforms the market by >= 10pp -> starter

# 2026-05-30 register P1.2 absolute reliability ceiling, enforced here since the
# 2026-06-06 audit P0.1: no class earns a >0.80 quote at ANY sample size (the >=0.90
# claimed bucket realised 51-53%, the 0.80-0.90 bucket 55-62%, across both audits).
ABSOLUTE_WR_CEILING = 0.80

# 2026-07-25 audit P1 #4: the ANTI-PREDICTIVE mid-band. A quote in [0.55, 0.65) is the
# rubric's least reliable statement — and 0.55 is its MODAL post-freeze quote (14 rows).
# Reliability diagram: the band predicted ~0.58 and realised 0.179 overall / 0.133 on the
# 15 post-freeze rows, i.e. WORSE than the [0.00,0.50) bucket the same rubric is honest
# about (pred 0.38 -> realised 0.44). This is a SIZING-PROCEDURE guard, explicitly in
# scope under the 2026-06-12 rubric freeze (the freeze governs rubric weights and tier
# cuts, not the win-rate quote that drives the sizing map), and it is downgrade-only.
ANTI_PREDICTIVE_BAND = (0.55, 0.65)  # [lo, hi) on the EMITTED (capped) quote
ANTI_PREDICTIVE_BAND_MAX_SIZE = "starter"

_SIZE_RANK = {"skip": 0, "starter": 1, "half": 2, "full": 3}


def n_conditional_cap(win_rate: float, n: int) -> float:
    """Cap the quoted win-rate by backtest sample size (2026-05-15 audit, C2-tightened;
    synced to the live 0.80 ceiling by the 2026-06-06 audit P0.1 — was stale at 0.85/0.90).

    n < 10  -> 0.69  (TIGHTENED from 0.75: keeps a single-regime small-N class below the
                      0.70 full-size line so it cannot full-size on an up-week alone)
    n >= 10 -> 0.80  (ABSOLUTE_WR_CEILING — 2026-05-30 register P1.2. The prior
                      0.85 (10<=n<20) / 0.90 (n>=20) tiers silently re-permitted the
                      quotes the ceiling bans; realized 2026-06-06 audit P0.1, where 11
                      post-register vol-lane rows quoted 0.837-0.933 raw backtest rates
                      and the decided ones went 0-for-3.)
    """
    cap = 0.69 if n < 10 else ABSOLUTE_WR_CEILING
    return min(win_rate, cap)


# ----- 2026-06-20 audit P1 #2: ceiling + clean-source emission guard -----------
# Sizing-eligible win_rate sources. The 2026-06-12 P0.3 quarantine RETIRED
# ``backtest`` / ``fallback_proxy`` as sizing sources (substrate-contaminated): the
# 2026-06-20 audit measured 30 pre-freeze envelopes that quoted >=0.80 off exactly
# these sources (earnings_vol 0.86->0.38, high_iv_rank 0.84->0.38, both BH-surviving).
SIZING_ELIGIBLE_SOURCES = frozenset({"backtest_clean", "NA(substrate)", "NA", None})
RETIRED_SUBSTRATE_SOURCES = frozenset({"backtest", "fallback_proxy"})


def sizing_eligible_quote(
    win_rate: float | None, win_rate_source: str | None, win_rate_n: int | None = None
) -> dict:
    """C2 / 2026-06-20 P1 #2 emission guard: bind the 0.80 ceiling AND the clean-source
    requirement at serialization, mirroring the sub-0.50 pre-emit floor in the agent.
    Extended 2026-07-04 audit P1 #1 (register C46, emission half) with the DEGENERATE
    floor: a quote <= 0.0 from an EMPTY/sub-Step-e cell (``win_rate_n`` < 5 kept rows,
    or n unknown) is the substrate degenerating, not a forecast — it must be emitted as
    ``win_rate: null`` / ``win_rate_source: 'NA(substrate)'`` and sized **at most
    starter** (the ladder's None path), never a numeric 0.0 (the MRVL 2026-06-08/06-09
    multi_day_sweep rows serialized 0.0 on live setups and corrupted the low reliability
    buckets — the pessimistic mirror of the >=0.80 ceiling leak).

    A **measured zero** — 0-for-N on ``win_rate_n`` >= 5 kept rows — is a real (terrible)
    quote, NOT degenerate: it stays numeric so the frozen sub-0.50 floor keeps binding it
    to starter/skip. (3-lens review 2026-07-04: nulling a measured zero would re-route it
    to the NA(substrate) tier default and LOOSEN the frozen floor — a 0.00 measurement
    must never size larger than a 0.05 one. Negative rates are impossible measurements
    and are degenerate at any n.)

    Returns an audit dict:
      ``sizing_eligible`` — False when the quote carries a RETIRED substrate source OR is
                            degenerate; such a quote must NOT drive ``pre_risk_size``.
      ``degenerate``      — True when ``win_rate <= 0.0`` and it is not a measured zero
                            (n >= 5). The serialized envelope value must then be null and
                            the size at most starter.
      ``capped_win_rate`` — ``win_rate`` clamped to ABSOLUTE_WR_CEILING (None if input
                            None OR degenerate — a degenerate quote has no emittable value).
      ``ceiling_ok``      — was the input already <= 0.80 (a serialized >0.80 is an envelope bug).
      ``reason``          — human-readable audit string.
    """
    measured_zero = (
        win_rate is not None
        and win_rate == 0.0
        and win_rate_n is not None
        and win_rate_n >= 5
    )
    degenerate = win_rate is not None and win_rate <= 0.0 and not measured_zero
    eligible = win_rate_source in SIZING_ELIGIBLE_SOURCES and not degenerate
    capped = None if (win_rate is None or degenerate) else round(min(win_rate, ABSOLUTE_WR_CEILING), 4)
    ceiling_ok = win_rate is None or win_rate <= ABSOLUTE_WR_CEILING
    if degenerate:
        reason = (
            f"win_rate {win_rate} <= 0.0 with n={win_rate_n} (<5 or unknown) is a DEGENERATE "
            f"substrate cell (2026-07-04 P1 #1 / C46) -> emit win_rate=null, "
            f"win_rate_source='NA(substrate)', size at most starter (ladder None path); "
            f"never serialize a 0.0 forecast"
        )
    elif measured_zero:
        reason = (
            f"win_rate 0.0 MEASURED on n={win_rate_n} kept rows is a real quote -> keep numeric; "
            f"the sub-0.50 floor binds pre_risk_size to starter/skip"
        )
    elif not eligible:
        reason = (
            f"win_rate_source={win_rate_source!r} is RETIRED substrate (2026-06-12 P0.3) -> "
            f"NON-SIZING; size at NA(substrate) tier-default capped half"
        )
    elif not ceiling_ok:
        reason = f"win_rate {win_rate} > {ABSOLUTE_WR_CEILING} ceiling -> clamped to {capped} (envelope bug if serialized raw)"
    else:
        reason = f"win_rate {win_rate} (source {win_rate_source}) <= {ABSOLUTE_WR_CEILING} ceiling -> sizing-eligible"
    return {
        "sizing_eligible": eligible,
        "degenerate": degenerate,
        "capped_win_rate": capped,
        "ceiling_ok": ceiling_ok,
        "reason": reason,
    }


def in_anti_predictive_band(win_rate: float | None) -> bool:
    """True when the EMITTED (post-cap) quote falls in the anti-predictive [0.55, 0.65).

    Tested on the capped value because the capped value is what the envelope serializes
    and what the audit's reliability diagram bins — a raw 0.92 that the n<10 cap pulls to
    0.69 is a 0.69 quote, not a mid-band one.
    """
    if win_rate is None:
        return False
    lo, hi = ANTI_PREDICTIVE_BAND
    return lo <= win_rate < hi


def anti_predictive_band_gate(win_rate: float | None, base_size: str) -> dict:
    """2026-07-25 audit P1 #4 — downgrade-only floor on the anti-predictive mid-band.

    A quote in [0.55, 0.65) may not size above ``starter``. It never upgrades: a quote
    already at ``starter``/``skip`` (e.g. via the sub-0.50 floor or a prior gate) stays
    where it is. The numeric quote itself is UNCHANGED — it stays in ``win_rate`` so the
    reliability diagram keeps binning the true statement; only the size is floored.

    Evidence (2026-07-25 audit Phase 3.3 / 3.3b): [0.55,0.65) realised **0.179 overall**
    and **0.133 on 15 post-freeze rows** against ~0.58 predicted; 0.55 is the modal
    post-freeze quote (14 rows); post-freeze ``bullish_flow`` claims 0.499 and realises
    0.250 (n=20). The band is not merely overconfident — it is anti-predictive: those
    names did worse than the ones the rubric said it was unsure about.
    """
    if not in_anti_predictive_band(win_rate):
        return {
            "band_hit": False,
            "size": base_size,
            "reason": f"win_rate {win_rate} outside anti-predictive band {ANTI_PREDICTIVE_BAND}",
        }
    floored = _min_size(base_size, ANTI_PREDICTIVE_BAND_MAX_SIZE)
    return {
        "band_hit": True,
        "size": floored,
        "reason": (
            f"win_rate {win_rate} in ANTI-PREDICTIVE band [{ANTI_PREDICTIVE_BAND[0]}, "
            f"{ANTI_PREDICTIVE_BAND[1]}) (2026-07-25 P1 #4: predicted ~0.58, realised "
            f"0.179 overall / 0.133 post-freeze) -> capped {ANTI_PREDICTIVE_BAND_MAX_SIZE} "
            f"(was {base_size}); quote itself unchanged"
        ),
    }


def market_excess(signal_win_rate: float, benchmark_win_rate: float) -> float:
    """Market-excess win-rate = signal WR - benchmark WR.

    ``benchmark_win_rate`` MUST be the SAME-DIRECTION bet on SPY over the SAME signal
    windows (long signal -> fraction of windows SPY rose; short signal -> fraction SPY
    fell). This subtracts the beta a signal earns just by agreeing with the tape, so an
    up-tape 100% bullish class (benchmark ~1.0) reads as ~0 excess, not edge.

    Both arguments are the RAW (uncapped) win-rate — apples-to-apples. The N-cap is a
    separate humility guard on the *quoted* win-rate and is deliberately NOT applied here.

    WINDOW-MATCHING RULE (2026-06-12 audit P2.6 — the caller's responsibility, not
    enforced here). ``benchmark_win_rate`` must be computed over **exactly the kept
    windows of the signal side** — i.e. the P0.3 clean-query complete-forward-window set
    (signal_date has >= lookback_days of data after it), NOT whatever windows the caller
    can conveniently build. Two failure modes this rule exists to stop: (1) computing SPY
    over the FULL calendar while the signal side dropped clamped (too-recent) windows ->
    apples-to-oranges excess, sign-flippable near the 0 boundary where the gate is binary;
    (2) reusing SPY's appearance INSIDE the signal class's own backtest set as the
    benchmark -> conflates the signal with its reference. The matched window set is NOT
    reconstructible from ``uw historical signal-backtest`` output alone (it returns per-row
    signal_date but the SPY-side fractions must be rebuilt over those same dates via a
    dedicated SPY ``uw historical trend``); the caller (signal-confluence-quant, under the
    P0.3 protocol) owns that reconstruction and must record the date set in audit_trail.
    """
    return round(signal_win_rate - benchmark_win_rate, 4)


def size_from_winrate(win_rate: float | None) -> str:
    """Map a (capped) win-rate to the calibrated pre-risk size ladder."""
    if win_rate is None:
        return "starter"  # newly covered / no history
    if win_rate >= 0.70:
        return "full"
    if win_rate >= 0.50:
        return "half"
    return "starter"


def _min_size(a: str, b: str) -> str:
    return a if _SIZE_RANK[a] <= _SIZE_RANK[b] else b


def size_decision(
    signal_win_rate: float | None,
    n: int,
    benchmark_win_rate: float | None = None,
    *,
    liquidity_ok: bool = True,
) -> dict:
    """Full C2 sizing decision: liquidity floor -> N-cap -> ladder -> anti-predictive
    band floor (2026-07-25 P1 #4) -> market-excess gate.

    Returns an audit dict. Both the band floor and the market-excess gate can only
    downgrade the ladder size; neither ever upgrades, and neither alters the quote.
    """
    if not liquidity_ok:
        return {
            "capped_win_rate": None, "excess": None, "base_size": "skip",
            "final_size": "skip", "excess_gate": "below_liquidity_floor",
            "band_gate": "n/a (below liquidity floor)", "band_hit": False,
            "reason": "below liquidity floor (price < $5 or 20d $ADV < $50M or unverifiable)",
        }

    capped = None if signal_win_rate is None else round(n_conditional_cap(signal_win_rate, n), 4)
    base = size_from_winrate(capped)

    # 2026-07-25 P1 #4: anti-predictive [0.55, 0.65) floor. Downgrade-only, applied on
    # the EMITTED (capped) quote, before the market-excess gate. Both gates can only cut.
    band = anti_predictive_band_gate(capped, base)
    final = band["size"]

    excess = None
    gate = "no_benchmark"

    if benchmark_win_rate is not None and signal_win_rate is not None:
        excess = market_excess(signal_win_rate, benchmark_win_rate)
        # Branch order matters: the more-negative threshold MUST be checked first, else
        # excess=-0.15 would satisfy `<= 0` and only cap to half instead of starter.
        if excess <= MATERIALLY_NEGATIVE_EXCESS:
            final = _min_size(final, "starter")
            gate = f"excess {excess:+.2f} <= {MATERIALLY_NEGATIVE_EXCESS:+.2f} -> starter (beta, underperforms market)"
        elif excess <= 0:
            final = _min_size(final, "half")
            gate = f"excess {excess:+.2f} <= 0 -> capped half (no edge over same-direction SPY)"
        else:
            gate = f"excess {excess:+.2f} > 0 -> edge confirmed, no excess penalty"

    reason = (
        f"raw {signal_win_rate} n={n} -> N-cap {capped} -> ladder {base}"
        + (f"; anti-predictive band: {band['reason']}" if band["band_hit"] else "")
        + (f"; market-excess gate: {gate} -> {final}" if benchmark_win_rate is not None else "")
    )
    return {
        "capped_win_rate": capped, "excess": excess, "base_size": base,
        "final_size": final, "excess_gate": gate,
        "band_gate": band["reason"], "band_hit": band["band_hit"],
        "reason": reason,
    }


# ----- CLI ------------------------------------------------------------------


def _candidates_from_json(payload: dict) -> list[Candidate]:
    return [
        Candidate(
            ticker=row.get("ticker", "?"),
            price=row.get("price"),
            adv_usd=row.get("adv_usd"),  # DOLLAR volume (shares x close), NOT a share count
            won=row.get("won"),
        )
        for row in payload.get("candidates", [])
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Liquidity-floor a candidate set (C12).")
    parser.add_argument("--file", help="JSON file with {'candidates': [{ticker, price, adv_usd, won?}]}")
    parser.add_argument("--min-adv", type=float, default=MIN_ADV_USD)
    parser.add_argument("--min-price", type=float, default=MIN_PRICE)
    args = parser.parse_args()

    if not args.file:
        parser.error("--file is required")
    payload = json.loads(Path(args.file).read_text(encoding="utf-8"))
    cands = _candidates_from_json(payload)
    kept, excluded = apply_liquidity_floor(cands, args.min_adv, args.min_price)
    print(json.dumps({
        "kept": [c.ticker for c in kept],
        "excluded": [c.ticker for c in excluded],
        "min_adv_usd": args.min_adv,
        "min_price": args.min_price,
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
