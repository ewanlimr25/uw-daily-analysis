# Phase 5 — Grading-Schema Critique · 2026-06-20

> **RUBRIC FREEZE (2026-06-12) — this phase GRADES the frozen rubric; it does not retune.** No re-weighted components, no re-binned cuts. The only output is a frozen-weight grading table + tier-cut monotonicity + **pre-registrations**.

## Two structural blockers to grading (state first — they cap everything below)

1. **The dataset is 100% single-regime.** Every decided call entered some `TRANSITIONAL — UPTREND / PULLBACK_IN_UPTREND` variant; **zero BEAR/DOWNTREND** rows exist. There is exactly **one regime stratum** — so "per-regime stratified grading" yields one column, and the **cross-regime acceptance bar for every pre-registration is structurally unmeetable by this data.** This is not a defect of the audit; it is the empirical fact that justifies the P0.6 out-of-regime half-cap.
2. **The frozen rubric has no gradeable outcomes.** 18 frozen-era (06-12+) calls are decided, but **0 are raw ≥9** and all sit on window-contaminated short horizons. The frozen `≥9` HIGH cut has **zero resolved calls in its own era**. So the outcome evidence below grades the **pre-freeze** weights that produced these scores — *different weights from the ones now frozen*. Every grade is therefore advisory-on-the-wrong-era and can only feed a pre-registration.

## Frozen-weight grading (component → measured contribution, single-regime, BH-null)

| Frozen rubric line | wt | Mapped Phase-4 evidence | Read |
|---|--:|---|---|
| accumulation conjunction (oi-trend BUILDING ≥5d + DP-block + cum-flow) | +3 | `dark_pool_block_stratified` **+18** (load-bearing) vs `historical_oi_trend` **−14.1** (negative); class realised 0.48 / **excess +14.8** | **Split**: the DP-block leg earns the excess; the oi-trend leg drags. Conjunction nets positive *edge* but its legs disagree. |
| multileg directional (term-structure-anchored) | +2 | `hot_chains_multileg` **−5.2**; class `multileg_directional` realised **0.17** (n=12), claimed 0.56, **BH-SURVIVING −38.8pp**, excess −8.3 | **Most outcome-contradicted positive weight.** Only directional miscalibration to survive BH. |
| vol: earnings-scout SELL VOL / vol-surface KINKED-VRP | +1/+2 | `term_skew` **−34.6**, `front_end_iv_ratio` **−50.0**; classes `earnings_vol`/`high_iv_rank` realised 0.38 vs claimed 0.84–0.86 | Points at the **substrate-fabricated ≥0.80 quotes** (Phase 3 §b). RV-proxy-resolved → cannot grade the *weight* until substrate + true IV-vs-RV land. |
| cum-premium-flow accretion (intent-screened) | +1 | `cumulative_premium_flow` **ubiquity-confounded** (cited 66%) | Ungradeable by construction; measurement-hygiene item, not a weight verdict. |
| sector-rotation single-name leader (persist ≥0.6) | +1 | `sector_flow_persistence` **+3.2** (supportive) | Weakly earning; no change. |
| accumulation-hunter DP-block co-flag | +2 | `dark_pool_block_stratified` **+18** | Earning — the credible leg of the accumulation stack. |
| opex-pin top-5 (OPEX week) | +1 | 3 pin calls, window-open | INSUFFICIENT_N. |
| flow_conflict / flow_conflict_lite | −3 / −1 | penalties on conflicted names | not separately gradeable (few decided); structurally sound (penalizes contradiction). |

## Tier-cut monotonicity (frozen cuts: HIGH ≥9 / MED 7–8 / LOW 3–6 / DROP ≤2)

Graded on pre-freeze decided scores (the only ones with outcomes):

| Band | WIN/n | WR |
|---|--:|--:|
| HIGH (≥9) | 5/13 | **38.5%** |
| MED (7–8) | 6/13 | 46.2% |
| LOW (3–6) | 28/62 | 45.2% |
| DROP (≤2) | 32/72 | 44.4% |

**Flat, with HIGH mildly inverted.** The frozen cuts do not separate outcomes on the available data — the same non-monotonicity that triggered the freeze (and the 06-12 re-confirmation failure). But this is pre-freeze substrate, single-regime, n=13 at the top — **insufficient to assert the *frozen* cuts are wrong**, and the freeze exists precisely to stop a single-window re-bin. Grade: **non-monotone, freeze correctly in force, re-confirmation deferred.**

## Pre-registrations (C-numbered; decided by a FUTURE audit on data that does not yet exist)

- **C40 — `+2 multileg_directional` weight is too high.** *Direction:* reduce toward +1 or gate on a confirmation leg. *Mechanism:* term-structure-inferred direction is not predicting realised direction (class 0.17 / n=12, BH-surviving, excess −8.3). *Acceptance bar:* cross-regime ∧ n≥30 per arm ∧ BH-surviving at FDR 0.10. *Decision window:* the first audit after 30 resolved multileg_directional calls accrue, ≥1 of them out-of-UPTREND. **Strongest-evidenced pre-registration in this audit.**
- **C41 — re-confirm the `≥9` HIGH cut.** *Direction:* the cut must demonstrate HIGH-band WR ≥ MED-band WR. *Mechanism:* second consecutive audit (06-12, 06-20) shows HIGH ≤ MED. *Acceptance bar:* n≥30 resolved raw-≥9 post-freeze calls, cross-regime, HIGH≥MED monotone. *Decision window:* future audit once ≥30 post-freeze ≥9 calls resolve (today: **zero**). Until then **keep the freeze and the half-cap.**
- **C42 — vol-component weights ungradeable pending substrate + IV-vs-RV.** *Direction:* hold. *Mechanism:* vol classes' claims are substrate-fabricated (Phase 3 §b) and outcomes are RV-proxy. *Acceptance bar:* (a) substrate quarantine lifted with a clean cross-regime backtest **and** (b) envelopes carry `implied_move` for true IV-vs-RV resolution. *Decision window:* after both land.
- **C43 (schema-additive, enables C16/C18).** Carry per-call `dp_block_to_float_ratio` and `insider_cluster_flag` in `calls[]` so the `fz` C16/C18 promotion gates become *testable* (today: NA). Additive, backward-compatible; not a promotion.

## Freeze-lift check (mandatory)
This audit accrued **<30 resolved post-2026-06-12 calls** (18 decided, 0 raw-≥9, all window-contaminated; **single-regime**). The P0.6 out-of-regime half-cap (daily/weekly Step 5 + risk-monitor `rubric_regime` gate) **cannot be graded for lift** and — given the dataset never once leaves UPTREND — its insurance value is by definition untested here. **Recommendation: KEEP the freeze, KEEP the half-cap.** No tier-monotonicity evidence supports a lift; the §-above inversion argues the opposite.

## Output
- `phase_5_schema.jsonl` — component grading rows, frozen-cut band table, and the C40–C43 pre-registrations with acceptance bars.
