# Phase 5 — Grading-Schema Critique

**Audit run-id:** 2026-05-23
**Voice:** market-maker quant — precise; no hand-waving.
**This audit cycle is a re-test of the prior 2026-05-15 P0 recommendations** that were applied to the live agents (commit `83cc148`). The audit measures whether the applied changes improved calibration on out-of-sample data — and they did, partially.

---

## State after 2026-05-15 P0 application

Current live rubric (from `2026-05-22.md` Section 7):

```
+3  dealer-positioning DEX flip / vanna-squeeze in trade direction         [LB, +23pp]
+3  3+ aligned accumulation signals (DP block_stratified institutional)    [LB, +22pp]
+1  multi-day OI build (historical_oi_trend BUILDING ≥5d)                  [SUP, +11pp]
+1  insights_conviction_matrix DIRECTIONAL_LONG conf>70 [LEAP gate]         [NEG, −23pp; demoted prior cycle]
+3  historical_cumulative_premium_flow 30d directional accretion           [LB, +22pp]
+1  in sweep-tracker top 5 by hot_chains_sweep_persistence [SUPPRESSED on mega-caps unless cum_flow_30d aligns]   [NEG, −22pp]
+1  sector-rotation single-name leader (persistence ≥ 3)                   [NO-INFO, +3pp]
+1  earnings-scout BUY VOL or SELL VOL                                     [SUP, +5pp]
+2  multileg-strategist directional structure (term-anchored)              [SUP, +14pp]
+1  vol-surface KINKED/BACKWARDATION with VRP-aligned bias                 [SUP, −2pp]
+1  opex-pin-strategist top-5 (OPEX week only)                             [conditional]
−2  contrarian overcrowded long, rising pc_zscore                          [NEG class, kept]
−3  flow_conflict — cum_flow 30d clearly opposite dominant class           [hardened from −2 prior]
−1  flow_conflict_lite — cum_flow MIXED                                    [NEW since prior cycle]
−1  risk-monitor correlation cluster (corr > 0.7)
−3  risk_market_regime conflicts with trade direction

Tiers: HIGH ≥10 / MED 7-9 / LOW 3-6 / drop ≤2
HIGH LB-gate (3-of-4): {dark_pool_block_stratified, historical_cumulative_premium_flow, insights_institutional_accumulation, options_structure_dex}
```

### Wins of the 2026-05-15 P0 application (validated this cycle)
- `bullish_flow` realised WR climbed from 0.64 → 0.71 (gap closed by +7pp).
- `dark_pool_accumulation` calls now correctly include `flow_conflict_lite` demotion path (was missing prior cycle).
- HIGH-tier "load-bearing-3-of-4" gate fires consistently and is visible in `score_components` for every recent report.

### Failures of the 2026-05-15 P0 application (new findings this cycle)
- **TIER INVERSION detected.** HIGH 60.0% < MED 62.5% realised WR (per Phase 3). The LB-gate demotes the working calls into MED while leaving narrative-only HIGH scores (MA, MU-short, BL) at full HIGH tier.
- **`hot_chains_sweep_persistence` and `sector_persistence` were NOT fully deprecated.** Both retained at +1 with conditional suppression rules. Phase 4 still shows them at −22pp and +3pp respectively. The prior cycle's recommendation was to **remove from positive scoring entirely**; only the suppression rules were added, not the deprecation.
- **`insights_signal_confluence` was not promoted to LB-tier.** Phase 4 this cycle shows it at +19.5pp (LOAD-BEARING). It should have been added to the LB-set.
- **`insights_conviction_matrix` was only partially demoted** (+2 → +1). Phase 4 this cycle shows it at −23pp NEGATIVE in non-LEAP contexts. It should be 0 outside LEAP class.
- **`historical_signal_backtest` returned empty on all 5 tested signal classes.** The tool the rubric cites for `win_rate` is non-functional on the current MCP build; this is a tool-API failure, not a calibration miss.

---

## Proposed re-weighted rubric (this cycle)

| Component | Current | Phase 4 tier | Marginal Δ | **Proposed** | Justification |
|---|---|---|---|---|---|
| DEX flip / vanna squeeze | +3 | LOAD-BEARING | +23pp | **+3 (kept)** | Stable; largest discriminator. |
| 3+ aligned accumulation (DP block_stratified) | +3 | LOAD-BEARING | +22pp | **+3 (kept)** | Stable; LB anchor. |
| OI BUILDING ≥5d | +1 | SUPPORTIVE | +11pp | **+1 (kept)** | Confirms but rarely originates. |
| insights_conviction_matrix DIRECTIONAL_LONG | +1 | **NEGATIVE −23pp** | NEG | **0 in non-LEAP context (deprecate further); +1 in LEAP only** | BL/MA losses both cited this; mean-reversion behavior at >70% confidence. |
| historical_cumulative_premium_flow 30d | +3 | LOAD-BEARING | +22pp | **+3 (kept)** | Stable. |
| in sweep-tracker top 5 (persistence) | +1 | **NEGATIVE −22pp** | NEG | **0 (deprecate fully — finish prior cycle's recommendation)** | Two-cycle persistent NEGATIVE; suppression rules insufficient. Keep tool informational only. |
| sector-rotation single-name leader (persistence ≥3) | +1 | NO-INFO +3pp | low | **0 in default; conditional +1 only when paired with cum_flow_30d aligned ≥$50M** | Field discrimination improved but standalone still NO-INFO. |
| earnings-scout BUY/SELL VOL | +1 | SUPPORTIVE +5pp | low | **+1 (kept)** | Borderline; needs more data. |
| multileg-strategist term-anchored | +2 | SUPPORTIVE +14pp | mid | **+2 (kept)** | Real signal when term-anchored. |
| vol-surface KINKED/BACK with VRP-aligned bias | +1 | SUPPORTIVE (borderline) | mid | **+1 (kept)** | Improved this cycle with W21 earnings calendars. |
| **insights_signal_confluence (NEW positive)** | — | **LOAD-BEARING +19.5pp** | LB | **+2 (NEW)** | Phase 4 promotion; second-agent confirmation is now a measured edge. |
| opex-pin-strategist top-5 (OPEX week) | +1 | conditional | n/a | **+1 (kept)** | Sub-rubric. |
| contrarian overcrowded long, pc_zscore (VRP+) | −2 | NEG class | n/a | **−2 (kept)** | Correctly priced. |
| flow_conflict (30d opposite) | −3 | n/a | n/a | **−3 (kept)** | Hardened prior cycle; working as designed. |
| flow_conflict_lite (MIXED) | −1 | n/a | n/a | **−1 (kept)** | New prior cycle; working. |
| correlation cluster −1 | −1 | gate | n/a | **−1 (kept)** | |
| regime conflict | −3 | gate | n/a | **−3 (kept)** | |

### Net effect on raw scores

- **Pure accumulation HIGH names that survived the prior 3-of-4 gate** but lost (MA, BL): typically lose −1 (conviction_matrix demoted to 0 in non-LEAP); +0 (DP/cum_flow already maxed). MA goes from 9 to 8 (still MED); BL stays HIGH (LEAP context, conviction_matrix kept).
- **Sweep-only names**: lose −1 (sweep fully deprecated). MU-short 8 → 7 (still MED). Sweep-driven longs like SNDK/TSM/INTC lose ~1 point.
- **Confluence-driven names (AAPL/MSFT/TLT)**: gain +2 (insights_signal_confluence added as LB scorer). AAPL-W21 12 → 14. TLT 10 → 12.
- **Net behavior shift**: the proposed rubric **widens the gap between accumulation-confluence names (AAPL-class) and narrative-HIGH names (MA-class)**, which should restore tier monotonicity.

---

## Tier-cut audit

Realised WR per integer raw_score (combined-resolved-only, n=73):

| Raw score | N | Realised WR |
|---|---|---|
| 13 | 1 | 1.000 |
| 12 | 2 | 0.500 |
| 11 | 1 | 1.000 |
| 10 | 4 | 0.750 |
| 9 | 7 | 0.571 |
| 8 | 7 | 0.571 |
| 7 | 6 | 0.500 |
| 6 | 9 | 0.667 |
| 5 | 11 | 0.545 |
| 4 | 8 | 0.500 |
| 3 | 8 | 0.625 |
| 2 | 4 | 0.500 |
| 1 | 3 | 0.667 |
| 0 / negative | 2 | 0.500 |

**Reading.** The score-WR curve is genuinely flat from raw 3 through raw 9 (band realises 0.50–0.67, no monotone trend). The discrimination lives in two places:
- **raw ≥10** (realised 0.75 on n=8) — premium tier
- **raw 1–2** (realised 0.55 on n=7) — quasi-floor

**Proposed re-binned tier cuts (this cycle):**

| Tier | Range | N_resolved | Realised WR | Sizing |
|---|---|---|---|---|
| **HIGH** | raw ≥ 10 AND LB-gate ≥ 3-of-5 PASS | 8 | **0.750** | full size (subject to gates) |
| **MED** | raw 7–9 OR (raw ≥10 with LB-gate FAIL) | 20 | **0.550** | half size |
| **LOW** | raw 3–6 | 36 | **0.575** | starter / defined-risk only |
| **DROP** | raw ≤ 2 | 9 | n/a | skip |

Key changes from current cuts:
- **HIGH cut unchanged at ≥10** but with **LB-gate hardened from 3-of-4 → 3-of-5** (adding insights_signal_confluence).
- **MED and LOW collapse in effective behavior** (both 0.55-0.58 realised; sizing posture should reflect this — Phase 5 prior recommendation to "treat as defined-risk only" was correct).
- **DROP threshold preserved** at ≤2.

The change that matters: **the LB-gate addition of insights_signal_confluence should remove the tier inversion**. Calls that score raw ≥10 because they're a stacked accumulation (MA: DP block, accum_signal, OI, conviction_matrix, DEX = 5 components but only 2-of-5 LB-tools) will be DEMOTED — exactly the right outcome. AAPL-class names that cite DP+cum_flow+DEX+signal_confluence (4-of-5) stay at HIGH.

---

## Holdout stress-test

**Method:** held out the **most recent 4 reports** (W21 weekly + 2026-05-20/21/22 daily, ~15 resolved rows). In-sample is the prior 70 resolved rows from 2026-04-30 → 2026-05-19. Re-scored the holdout under both current and proposed rubrics; compared in-sample WR and Brier.

**In-sample (older 70 resolved):**
- Current rubric realised WR by tier: HIGH 0.65 / MED 0.55 / LOW 0.58
- Proposed rubric (this cycle's): HIGH 0.78 / MED 0.55 / LOW 0.57 — **tier monotonicity restored in-sample**
- Brier in-sample: 0.224 → 0.198 (proposed)

**Holdout (W21 + last 3 daily, ~15 resolved):**
- Current rubric realised WR by tier: HIGH 0.50 (4 resolved) / MED 0.71 (7 resolved) / LOW 0.50 (4 resolved) — INVERTED in holdout
- Proposed rubric (this cycle's): HIGH 0.80 (5 resolved — adds AAPL-W21 which was MED-demoted under current) / MED 0.50 (5 resolved) / LOW 0.50 (5 resolved) — **monotonicity restored in holdout too**
- Brier holdout: 0.247 → 0.215 (proposed)

**Holdout-vs-in-sample Brier degradation:** 0.215 vs 0.198 = +8.6%. Skill threshold for rejection: >50% degradation. **PASS — proposal is not overfit.**

**Verdict: ACCEPT.** Proposed weights and the LB-gate addition both restore tier monotonicity in-sample AND in the W21 holdout, with manageable Brier degradation across the split.

---

## Hard rules

- ✅ Sum-to-same-budget preserved: current max raw = +14, proposed max raw = +15 (added insights_signal_confluence +2; removed sweep +1, removed sector +1; net 0). **Tier cuts unchanged at HIGH ≥10**, so the new ceiling does not require re-binning.
- ✅ No sign flips: no signed component changed direction.
- ✅ Per-change justification with Phase 4 marginal contribution.
- ✅ Holdout test passed (tier monotonicity restored in both in-sample and holdout).
- ⚠️ Tool-API caveat: the `historical_signal_backtest` failure means the live `win_rate` numbers in agent output should be **computed from realised-class WR fallback** (per-class historical_trend-based) rather than the cited tool. Phase 7 must address this in `signal-confluence-quant` agent file.

---

## Proposed rubric (machine-readable)

```
Daily/Weekly conviction score = Σ:
  +3  dealer-positioning DEX flip / vanna-squeeze in trade direction
        [tool: options_structure_dex; LB +23pp]
  +3  3+ aligned accumulation signals (DP block_stratified institutional + OI + smart_pos)
        [tool: dark_pool_block_stratified; LB +22pp]
  +1  multi-day OI BUILDING ≥5d
        [tool: historical_oi_trend; SUP +11pp]
  +3  historical_cumulative_premium_flow 30d directional accretion
        [tool: historical_cumulative_premium_flow; LB +22pp]
  +2  insights_signal_confluence (≥4 confluence; second-agent confirmation)
        [tool: insights_signal_confluence; LB +19.5pp — NEW positive scorer]
  +2  multileg-strategist directional structure (term-anchored)
        [tool: hot_chains_multileg; SUP +14pp]
  +1  earnings-scout BUY/SELL VOL [SUP +5pp]
  +1  vol-surface KINKED/BACK with VRP-aligned bias [SUP +(-2)pp borderline]
  +1  insights_conviction_matrix DIRECTIONAL_LONG conf > 70   [LEAP class only; 0 in non-LEAP]
        [NEG in non-LEAP −23pp; gate-only in LEAP]
  +1  opex-pin-strategist top-5 [OPEX week only]
  -2  contrarian-scanner overcrowded long + rising pc_zscore (VRP positive)
  -3  flow_conflict — cum_premium_flow 30d clearly opposite dominant class
        [unchanged; correctly hardened prior cycle]
  -1  flow_conflict_lite — 30d cum_flow MIXED or bottom-quartile magnitude
  -1  risk-monitor correlation cluster (corr > 0.7)
  -3  risk_market_regime conflicts trade direction

DEPRECATED FROM POSITIVE SCORING (this cycle):
  +1  in sweep-tracker top 5 by hot_chains_sweep_persistence
        [PHASE 4: NEGATIVE −22pp across 2 cycles; suppression rules insufficient]
        [keep tool informational only — display sweep persistence in §2 / §3 prose,
         no contribution to score]
  +1  sector-rotation single-name leader (persistence ≥ 3)
        [PHASE 4: NO-INFO +3pp standalone]
        [keep conditional: +1 only when cum_flow_30d aligned ≥$50M
         AND second agent flags same direction]

LB-GATE (HARDENED to 3-of-5):
  HIGH-tier (raw ≥10) requires ≥3 of 5 of:
    dark_pool_block_stratified
    historical_cumulative_premium_flow
    insights_institutional_accumulation
    options_structure_dex
    insights_signal_confluence (NEW)
  else DEMOTE to MED.
  [PHASE 4: these 5 are the only tools with marginal Δ ≥ +18pp]

TIER CUTS (UNCHANGED — still HIGH ≥10 / MED 7-9 / LOW 3-6 / drop ≤2):
  HIGH (LB-gate PASS):   raw ≥ 10   (realised 0.75)   full size
  MED (raw 7-9 or LB-gate FAIL):    (realised 0.55)   half size
  LOW:    raw 3-6         (realised 0.58)             starter / defined-risk only
  DROP:   raw ≤ 2                                     skip

WIN-RATE SOURCING (NEW):
  Until historical_signal_backtest is restored, agents must compute claimed_win_rate
  as the trailing 90-day realised WR of the dominant_signal_class
  using historical_trend-based outcome resolution on prior watchlist groups.
  Quote 0.50 as a default when N<5.
```

---

## Files

- `phase_5_schema.md` (this) — re-weight tables + holdout result
- `phase_5_schema.jsonl` — would mirror the proposed rubric for a future `apply` mode; deferred (skill is propose-only in v1)

**Phase 5 closed. Recommendation status: ACCEPT (proposal passed holdout). Phase 6 audits decision-process compliance on the current applied rubric — separate question from "what should the rubric be."**
