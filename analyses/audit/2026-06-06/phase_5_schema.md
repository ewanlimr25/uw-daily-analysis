# Phase 5 — Grading-Schema Critique (2026-06-06)

## A. Component re-weight → **DEFERRED again** (posture unchanged from 05-30)

Phase 4 this run is *more* stable than 05-30 (dark-pool +17 / dex +11 durable; the negative
GEX cluster durable) — but **zero tools survive BH for the third run**, and 379/432 decided
rows still carry reconstructed citations. Re-weighting a fixed-budget additive rubric on
BH-null MCs remains chasing noise. **No component re-weight is proposed.** The only durable
re-weight *direction* stays: `cumulative-premium-flow` (most-cited, n=136, NO-INFO 3 runs)
is over-weighted wherever it earns points — P1/P2 in Phase 7, with the NEE dividend-arb
blind spot as qualitative corroboration.

## B. Tier-cut audit — per-integer realised WR (n=323 scored-decided)

| Score | ≤2 | 3 | 4 | 5 | 6 | 7 | 8 | **9** | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WR | 56% | 49% | 40% | 46% | 58% | 53% | 52% | **72%** | 60% | 67% | 50% | 100% |
| n | 25 | 45 | 57 | 56 | 43 | 34 | 23 | **18** | 10 | 6 | 4 | 2 |

The ≥9 lift **persists but compressed**: ≥9 cohort = **67.5% (n=40)** vs 05-30's 77.4%
(n=31) — the June risk-off week took ~10pp off the top cohort. Scores 3–8 remain a 40–58%
plateau; score 4 is the trough (40%, n=57).

| Cut (HIGH≥hi / LOW<lo) | HIGH | MED | LOW | Monotone? | HIGH−MED gap |
|---|---|---|---|---|---|
| Validator-current (≥10 / <3) | 63.6% (n22) | 50.4% (n276) | 56.0% (n25) | ❌ MED<LOW | +13.3 |
| **Live rubric (≥9 / <4, P1.3)** | **67.5% (n40)** | 48.8% (n213) | 51.4% (n70) | ❌ MED<LOW | **+18.7** |
| ≥8 / <4 | 61.9% (n63) | 48.4% (n190) | 51.4% (n70) | ❌ MED<LOW | +13.5 |

**Still no monotone cut, same root cause as 05-30:** LOW beats MED at every cut because the
alpha shorts (`bearish_flow`, honest 38% quotes) score low while the beta longs
(`bullish_flow` / `dark_pool_accumulation`, −15 to −18pp excess) score mid. **The inversion
is a rubric-direction defect, not a cut defect** — the additive score pays for long-side flow
evidence that is beta. Re-binning cannot fix it; directional weighting (or split long/short
scoring) is the structural answer (Phase 7).

## B2. ⚠️ The stale validator band is now contaminating the dataset (P1.3 follow-through)

The live rubric says **≥9 = HIGH**, but `validate_decision.py` still enforces ≥10 — so every
raw-9 envelope call is **recorded MEDIUM**: AMD 05-25 (WIN), MSFT 05-29 (WIN), AVGO W22
(WIN), TSLA 06-02 (LOSS), LLY 06-05 (open). The desk irony: the suppressed raw-9 cohort went
**3/4** while the recorded-HIGH (≥10) envelope calls went **1/5** (AAPL 11 L, SMH 12 L, SMH
10 L, ORCL 10 L, MSFT 11 W). Every audit's tier table mis-buckets these rows until the
validator band matches the live rubric. (Phase 7, P1.)

## C. Holdout stress-test → **REJECT-leaning, still thin**

| | HIGH (≥9) | MED | LOW |
|---|---|---|---|
| Train (22 reports, n=299) | **71.1% (n38)** | 49.0% (n196) | 53.8% (n65) |
| Holdout (recent 5 reports, n=24) | **0.0% (n=2)** | 47.1% (n17) | 20.0% (n5) |

First holdout with *any* decided HIGH calls — and the score-≥9 cohort went **0-for-2 into the
06-05 break** (ORCL 10, TSLA 9). n=2 cannot statistically reject, but the prior two audits'
"P1-pending-holdout" posture on the ≥9 cut now has its first out-of-sample taste and it is
negative. Combined with the in-sample compression (77 → 67.5%), the honest read:

> The ≥9 lift is real in trend tape and **untested-to-negative in risk-off tape**. Since
> P1.3 already shipped the ≥9=HIGH cut live, the actionable follow-up is not a revert
> (n=2!) but a **regime conditioner**: the ≥9 cohort's edge is regime-conditional until the
> June cohort resolves (~12 more decided HIGH calls by mid-June).

## Verdict

- Tier-cut proposal: **HOLD the live ≥9/<4 cut** (no new cut proposed; nothing is monotone
  anyway) — **ACCEPT_WITH_CAVEAT**, caveat upgraded from "no holdout data" to "first holdout
  taste negative (n=2)."
- **The MED<LOW inversion is confirmed for the third run** and remains a rubric-direction
  defect: the score is positively correlated with *beta*, weakly with *edge*.
- Component re-weights: **DEFERRED** until the June envelope cohort closes with verbatim
  provenance (re-test ~2026-06-12+).

## Output
- `phase_5_schema.jsonl` — per-score WR, cut grid, holdout numerics. `phase5_schema.py` — reproducible.
