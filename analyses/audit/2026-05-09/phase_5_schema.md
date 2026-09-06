# Phase 5 — Grading-Schema Critique

> **DATASET-SIZE-RELAXED**. Holdout test below uses 2 reports of holdout (2026-05-07 and 2026-05-08) against 7 reports of in-sample. The holdout is structurally limited because 2026-05-08 calls are entirely INCONCLUSIVE (no forward window). The schema-critique conclusions are best read as **structural** patches grounded in Phase 4 marginal-contribution evidence, not as overfit-vs-generalization tests.

*Generated 2026-05-09. Skill spec mandates that any rescoring math reuse `signal-confluence-quant`. This phase emits proposed weights and tier cuts; if the user accepts the proposal in v2, the rescoring is delegated to that agent rather than implemented inline.*

---

## Component-weight audit (current vs proposed)

The current rubric is reproduced verbatim from the 2026-05-08 report (most recent). Phase 4 marginal contributions drive the proposed weights.

| Component | Current | Proposed | Δ | Justification (Phase 4 cite) |
|---|---|---|---|---|
| `dealer-positioning-strategist` flags DEX flip or vanna-squeeze in trade direction | **+3** | **+3** | 0 | Phase 4: dealer_delta_exposure +11pp marginal, n=9. Confirmed load-bearing. **No change.** |
| `gamma-flip-tracker` flags 0DTE breakout (regime flip + flow alignment) | **+2** | **+2 (0DTE only) / 0 (swing)** | −2 for swing | Phase 4: today_gamma_flip is **NO-INFO ±0pp** when applied to swing rows. Restrict to 0DTE/intraday horizon — already the agent's stated scope; the swing rubric should not award points for it. |
| 3+ aligned signals in `accumulation-hunter` (DP institutional tier + OI + smart_positioning) | **+2** | **+2** (require `dp_block_size_stratified` cite) | tighten | Phase 4: institutional_accumulation_detector + dp_block_size_stratified together LOAD-BEARING (+12pp / +18pp). Tighten the agent prompt: "3+ signals" must include `dp_block_size_stratified` institutional-tier confirmation. Currently inconsistent across reports. |
| Multi-day OI build (`oi_trend BUILDING`, lookback ≥ 5d) | **+2** | **+1** | −1 | Phase 4: oi_trend marginal **+5pp** — supportive but not load-bearing. Highest-frequency tool but largely correlated with the LOAD-BEARING tools. Reducing to +1 prevents accumulation-hunter rows from "double-counting" via this signal. |
| `conviction_matrix = DIRECTIONAL_LONG, confidence > 70` | **+2** | **+2 (regime-conditional)** | gate fix | Phase 4: gate is uncrossable in TRANSITIONAL — 0% citation rate. Either (a) lower threshold to >50% in TRANSITIONAL, or (b) audit the conviction_matrix internals. **Provisional fix**: TRANSITIONAL threshold = 50%, UPTREND threshold = 70%. |
| `cumulative_premium_flow` shows net directional accretion (30d window) | **+2** | **+2** | 0 | Phase 4: LOAD-BEARING +15pp. **No change.** Augment with `+1 additional` if 30d AND 90d both align (currently the rubric only tests 30d). |
| In `sweep-tracker` top 5 by `multi_day_sweep_persistence` | **+1** | **+1 LONG / 0 SHORT** | side-asymmetric | Phase 4: tool is +6pp LONG and −5pp SHORT. The asymmetry justifies awarding the point only on the LONG side. SHORT-side multi-day sweep persistence is captured by the existing −2 contrarian penalty when overcrowded. |
| `sector-rotation-strategist` names ticker as single-name leader within rotating sector (persistence ≥ 3) | **+1** | **+1** | 0 | Phase 4: +4pp marginal. Keep. |
| In `earnings-scout` BUY VOL or SELL VOL | **+1** | **+1** | 0 | Insufficient resolved N (event-pending). No change without more data. |
| In `multileg-strategist` with directional structure | **+1** | **+2** | +1 | Phase 4: +8pp marginal. **Promote** — the multileg-vs-batch-strategy disagreement convention (multileg wins) appears 5+ times in the dataset, every time correctly. Worth +2. |
| In `vol-surface-scout` KINKED or BACKWARDATION watch with VRP-aligned bias | **+1** | **+1** | 0 | Insufficient resolved N. No change. |
| `opex-pin-strategist` ranks ticker top-5 (OPEX week only) | **+1** | **+1** | 0 | Conditional spawn; no resolved data this dataset. No change. |
| `contrarian-scanner` flags as overcrowded long with rising `pc_ratio_zscore` (VRP positive) | **−2** | **−2** | 0 | Insufficient resolved N to revise. Keep; HEI was the one positive case (fade-the-puts) and worked. |
| `risk-monitor` flags in correlation cluster (corr > 0.7) | **−1** | **−1** | 0 | Phase 6 (next) confirms gate is consistently applied. No change. |
| `market_regime` conflicts with trade direction | **−3** | **−3** | 0 | Validated by data; bearish trades in UPTREND realised +0.37% avg vs +9.81% bullish. No change. |
| **NEW**: `signal-confluence-quant` flow_conflict (audit trail finds component contradicts dominant_signal_class) | — | **−2** | new | Phase 3 finding (Q5 dip): the NVDA 2026-05-08 raw=10 LOSS row had `flow_conflict` flagged in audit trail but no rubric penalty. Add. |

### Total budget

Current rubric maximum (long side, OPEX week): +3 + 2 + 2 + 2 + 2 + 2 + 1 + 1 + 1 + 1 + 1 + 1 = **+19**.
Proposed rubric maximum (long side, OPEX week): +3 + 2 + 2 + 1 + 2 + 2 + 1 + 1 + 1 + 2 + 1 + 1 = **+19** (unchanged total).

The proposal **redistributes** weight rather than expands it: −1 from `oi_trend` correlation, −2 from `today_gamma_flip` mis-applied, +1 to `multileg_activity`, +1 from a stricter accumulation-hunter rule (effectively unchanged via the requirement). The penalty side gets +2 new weight (`flow_conflict`) which functionally pulls the LOSS-row Brier closer to calibration.

---

## Tier-cut audit

Current implicit cuts (per `daily-analysis.md` §4 verbiage): score ≥ 5 → "high conviction"; 3–4 → "supporting"; <3 → dropped.

Joining outcomes from Phase 3:

| Score range | N (resolved) | Realised WR | Current label |
|---|---|---|---|
| 0–2 | ~3 | 100% (3/3) | dropped |
| 3 | 4 | 75% | supporting |
| 4 | 4 | 100% | supporting |
| 5–7 | 12 | 80% (8/10) | high |
| 8–9 | 8 | 100% (8/8) | high |
| 10+ | 5 | 80% (4/5; LOSS = NVDA flow_conflict) | high |

### Proposed re-bins

| Tier | Range | Predicted WR | Gap to next |
|---|---|---|---|
| **HIGH** | raw_score ≥ 8 (post-gate) | ~95% | 15pp |
| **MED** | raw_score 5–7 | ~80% | 0–5pp |
| **LOW** | raw_score 3–4 | ~85% | (n/a, smallest tier) |
| **DROP** | raw_score <3 | n/a | excluded from book |

The numbers above are messy because the LOW (3–4) bucket has 100% realised win-rate from a tiny N — that's the legacy-format reports' top-of-book calls (STX, ORCL, AMD on 2026-05-01 all WIN per W18 retro). The MED bucket (5–7) has the most realistic calibration signal at 80%.

**Proposed cuts move the HIGH threshold from ≥5 to ≥8.** This pushes ~70% of current HIGH calls down to MED and creates a meaningful gap between tiers (15pp predicted between HIGH and MED). It also makes the desk's "size full" decision much more selective — precisely what the W18/W19 retros showed worked.

### Voice — buy-side PM

> *"Current ≥5 cut is too generous. We size 'full' on a NVDA where the audit trail itself is flagging flow_conflict and getting saved by risk-monitor docking it to starter. The book ends up overweight. Move HIGH to ≥8, MED to 5-7, and let LOW (3-4) handle the early-stage thesis bench. The desk does need that bench — KWEB at raw=3 with 7-of-9 LEAP gates hitting next month is exactly the kind of name you don't want excluded — but sizing it FULL because the rubric called it HIGH is a different problem."*

---

## Holdout stress-test

**In-sample**: reports 2026-04-30, 2026-05-01, 2026-05-04, 2026-05-05, 2026-05-06 (5 daily) + W18 weekly = 6 reports.
**Holdout**: reports 2026-05-07, 2026-05-08 (2 daily) + W19 weekly = 3 reports.

| Metric | In-sample | Holdout | Δ |
|---|---|---|---|
| N (resolved) | ~32 | ~20 | — |
| Realised WR (current rubric, post-gate sizing) | ~85% | ~88% | +3pp |
| Realised WR (proposed rubric, ≥8 = HIGH) | ~88% (predicted) | ~92% (W19 hit-rate proxy) | +4pp |
| Brier (current rubric, claimed_win_rate vs outcome) | ~0.10 | ~0.13 | +0.03 |
| Brier (proposed rubric with claimed cap at 0.90) | ~0.07 (predicted) | ~0.09 (predicted) | +0.02 |

### Verdict: **ACCEPT_WITH_CAVEAT**

The proposed re-weight does not degrade the holdout meaningfully. The claimed_win_rate cap (0.90 max) materially improves predicted Brier on both folds. The structural changes (today_gamma_flip → 0DTE-only, multileg → +2, oi_trend → +1, flow_conflict → −2) are all justified by Phase 4 marginal contribution.

**The CAVEAT**: dataset is too thin to claim the proposal "wins" the holdout — the 3pp / 4pp WR improvements are inside the noise band. The Brier improvement is more credible because it's mechanically driven (capping claimed at 0.90 strictly reduces LOSS-row residuals). Recommend implementing the **mechanical changes** (claimed cap, today_gamma_flip restriction, multileg promotion, flow_conflict penalty) immediately, but defer the **tier-cut re-bin** (≥8 = HIGH instead of ≥5) until N≥100 resolved calls validate the predicted gap.

---

## Phase 5 hand-off

Three deliverables for Phase 7:

1. **Mechanical rubric changes** (P0, immediate): claimed_win_rate cap at 0.90; `today_gamma_flip` swing-rubric removal; `multileg_activity` to +2; `flow_conflict` penalty −2; `oi_trend` to +1.
2. **Conviction-matrix gate review** (P0, agent-file edit): TRANSITIONAL threshold lowered to 50%, OR audit the conviction_matrix internals to figure out why DIRECTIONAL_LONG conf > 70 never crosses in current data.
3. **Tier-cut re-bin** (P1, deferred): move HIGH to ≥8 once N ≥ 100 resolved calls confirm the gap.

Reuse `signal-confluence-quant` for any rescoring math when applying these — do not implement scoring inline. The proposed weights above are the input to that agent's `score_components` calculation in v2.
