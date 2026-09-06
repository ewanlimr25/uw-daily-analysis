# Phase 5 — Grading-Schema Critique

## A. Component-weight audit (Phase-4-driven, sign-preserving, budget-neutral)

The current rubric is additive with these load-bearing lines. Mapping each to its realised Phase-4 marginal contribution exposes two budget mis-allocations:

| Rubric line (current) | Tool | Phase-4 MC | Verdict | Proposed |
|---|---|---|---|---|
| `+3 cumulative-premium-flow net accretion (30d)` | `historical cumulative-premium-flow` | **+2.0pp (n=76)** | NO-INFO — biggest score-inflator that doesn't earn it | **+3 → +1** |
| `+3 accumulation conjunction (DP block ∧ flow)` | `dark-pool block-stratified` | **+25.4pp** | LOAD-BEARING — but the **win-rate label** is the fiction, not the gate | keep **+3**; cap the WR *quote* (§D) |
| `+3/+2 dealer DEX flip` | `options-structure dex` | **+15.5pp** | LOAD-BEARING (the one honest class) | keep / consider **+3 floor** |
| `+2 multileg directional` | `hot-chains multileg` | −7.0pp | NEGATIVE | **+2 → +1** |
| `±N vol-surface / term-skew` | `options-structure term-skew` | **−13.4pp (n=56)** | NEGATIVE — feeds the vol_surface 80%→47% miscalibration | **demote to advisory (0)** pending agent-prompt fix |
| sweep persistence | `hot-chains sweep-persistence` / `multi-day-sweep-persistence` | +19.5 / +31.9pp | LOAD-BEARING — *under-weighted* | **introduce +2 persistence line** |

**Net effect is budget-neutral**: the −2 removed from `cumulative-premium-flow` and −1 from `multileg` are re-allocated to a new `+2 multi-day sweep-persistence` line and a `+1` floor on `dex`. Sign of every retained component is preserved; no weak-data sign flips invented.

> ⚠️ A full normalized refit-and-rescore (spawning `signal-confluence-quant` on proposed weights, per the skill) is **deferred to a future `apply` pass** — on close-only outcome data a precise weight refit would overfit. These are targeted, justified moves, each citing a Phase-4 MC with n.

## B. The LOAD-BEARING-tool gate is mis-specified

The HIGH-tier gate requires "3 of 5 LOAD-BEARING tools": `dark-pool block-stratified`, `cumulative-premium-flow`, `insights institutional-accumulation`, `insights signal-confluence`, `options-structure dex`. **Phase 4 says 2 of those 5 are not load-bearing:**

- `cumulative-premium-flow` = **NO-INFO (+2pp)**
- `insights institutional-accumulation` = **NEGATIVE (−12.6pp)**

A gate that admits a NEGATIVE tool can be *satisfied by anti-predictive evidence*. **Proposed gate set** (all Phase-4 LOAD-BEARING): `dark-pool block-stratified` (+25.4), `options-structure dex` (+15.5), `hot-chains sweep-persistence` (+19.5), `historical oi-trend` (+12.2), `insights signal-confluence` (+17.2). Swap out the two failures for `sweep-persistence` + `oi-trend`.

## C. Tier-cut audit

Per-integer-score realised WR (n in parens): 3→41% (29) · 4→53% (38) · 5→52% (46) · 6→54% (24) · 7→47% (19) · 8→**30%** (10) · 9→**70%** (10) · 10→63% (8) · 11→33% (3) · 12→50% (2) · 13→100% (2). The 7–8 band is the trough; the real lift starts at 9.

| | HIGH | MED | LOW | Monotone? |
|---|---|---|---|---|
| **Current** (≥10 / 7–9 / 3–6) | 60.0% (n=15) | 48.7% (n=39) | 50.9% (n=161) | ❌ MED<LOW |
| **Proposed** (≥9 / 4–8 / <4) | **64.0% (n=25)** | **50.4% (n=137)** | **47.2% (n=53)** | ✅ HIGH>MED>LOW |

Lowering the HIGH cut **10→9** (capturing the strong score-9 cohort) and the LOW floor **3→4** (shedding the weak score-3 cohort, 41%) restores monotonicity with a **13.6pp HIGH-MED gap**.

## D. Win-rate *quote* caps (the highest-impact fix)

Phase 3's −31.6pp / −33.2pp divergences are quote-inflation, not selection. Floor the **quoted** `win_rate` (the number that drives sizing) to the realised audit rate per class:

| Class | Current quote | Realised | Proposed quote cap |
|---|---|---|---|
| dark_pool_accumulation | up to 0.83 | 0.51 | **≤ 0.55** |
| vol_surface | up to 0.80 | 0.47 | **≤ 0.50** |
| gamma_pin | 0.64 | 0.30 | **≤ 0.40** |
| bullish_flow | 0.65 | 0.46 | **≤ 0.55** |
| dealer_positioning | 0.84 | 0.80 | keep (honest) |
| bearish_flow | 0.43 | 0.44 | keep (honest) |

This alone collapses the Brier from 0.34 toward ~0.20 (overconfidence is the dominant Brier term).

## E. Holdout stress-test → **ACCEPT_WITH_CAVEAT**

Held out the most-recent **6 reports** (20%); refit cuts on the older 21.

| | HIGH | MED | LOW |
|---|---|---|---|
| In-sample (train, refit ≥10/4–9) | 69.2% | 52.0% | 49.0% (monotone ✅) |
| Holdout | **n/a (0 resolved HIGH)** | 50.0% | 25.0% |

Brier *improved* out-of-sample (0.353 → 0.302). **But the holdout cannot validate the HIGH tier**: the most-recent 20% are this week's envelope reports, which are almost entirely `window_open` (swings/LEAPs not yet resolved) — there are **zero resolved HIGH-tier calls in the holdout**. The proposed re-cut is therefore **accepted with the caveat that HIGH-tier monotonicity is confirmed in-sample only**; it cannot be falsified out-of-sample until this week's calls resolve (~2026-06-12). Verdict: **ACCEPT_WITH_CAVEAT** — ship the WR-quote caps (D) and the LB-gate fix (B) as the high-confidence changes; stage the tier-cut move (C) as P1-pending-holdout.

## Output
- `phase_5_schema.jsonl` — per-score WR, current/proposed cuts, holdout numerics. `phase5_schema.py` — reproducible.
