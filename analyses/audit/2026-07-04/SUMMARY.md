# Calibration Audit — 2026-07-04

**Dataset:** 335 calls / 34 envelopes (verbatim provenance, first time at 100%) · 264 decided (43.9% WR) · choppy stratum decided for the first time · zero post-pin fleet runs (model pins 07-03 → transition checks carried forward with baselines frozen).

## Top 3 schema flaws
1. **The frozen rubric's sized book has negative edge** — post-freeze book excess −8.8pp (n=117), sized book 36.1% vs paper 45.2%. The system's best current behavior is refusing to size (the empty-book protocol), and the outcomes agree. Phase 3b. Hold rulings P1.
2. **Win-rate emission now lies at both ends:** the ≥0.80 cap is fixed and verified (0 leaks post-06-29), but the substrate emits `claimed_win_rate=0.0` on live setups (two multi_day_sweep winners) — pessimistic mirror of the old leak. Phase 6 §1. Patch P1.
3. **The weekly +3 oi-trend line rides a −9.2pp tool** (n=69, negative in 3/4 strata) with a documented saturation artifact (W27 §7(4)). Largest weekly weight, weakest substrate. Phase 5 §1. Pre-reg C47, P2.

## Top 3 tool-tier surprises
1. **`hot_chains_multileg` whipsawed to +26.5pp** — third sign in three audits (BH-neg → −12.7 → +26.5). The instability is the finding; C40 unmoved. Phase 4.
2. **`multi_day_sweep` is the first BH-surviving *under*-claim** (realised 0.88 vs claimed 0.38, +58.9pp excess) — deflated to 4 underlyings' repeat prints with two 0.0-claim quotes. Register C46, don't chase. Phase 3/4.
3. **No tool survives BH for the 5th consecutive audit** — while the one boring constant, `insights_institutional_accumulation`, holds +12.5pp (was +13.6). Still the only weight earning its points. Phase 4/5.

## What we'd do Monday
Nothing gets braver. The 06-27 P1s all verified in the wild: shorts still bleed (−22.9pp), the long edge is still rented from the uptrend (+29.1pp there, −33.3pp first choppy read), and the out-of-regime half-cap crossed its evidence floor as *protective* (0.25 WR / −21.5pp on n=20 — keep it, actionably now). Freeze stays (HIGH/MED still structurally empty, 4th audit). The two edits worth ink: kill the 0.0-quote emission bug, and ship the three C43 schema fields (`implied_move`, float-ratio, insider flag) so the vol book and two fz gates stop being unmeasurable. Then re-audit early — ~five post-pin envelopes (~07-10) — because the fleet changed brains on 07-03 and every compliance baseline in this file is the yardstick for whether anything degraded.
