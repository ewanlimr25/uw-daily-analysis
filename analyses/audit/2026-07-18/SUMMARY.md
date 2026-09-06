# Calibration Audit — 2026-07-18

Dataset: **463 verbatim envelope calls** (46 `decision.json`; 38 daily + 8 weekly), 141/143 tickers OHLC-resolved path-aware, **394 decided**, **0 `Σpoints≠raw_score` violations**. Strata never pooled: pre-freeze 2026-05-15 (54) / 2026-05-30 (69) / post-0606 (28) / **FROZEN 2026-06-12 (312)**. 7th edge audit — and the **first with real regime diversity** (292 non-uptrend rows vs 171 uptrend), which changes the story.

## Top 3 schema flaws
1. **The benchmark-excess sign is non-stationary — the last audit's headline reversed.** `bearish_flow` went +29.4pp (BH-survives, 07-11) → **−3.2pp ns**; the long/accumulation complex went −29pp → **+10.8pp**. Same rows, benchmark flipped when the tape stopped rising. Phase 3. → **C19 graduation BLOCKED** (P1); no directional line is scorable.
2. **The +3 accumulation conjunction's negative excess was beta all along.** dark_pool_accumulation excess washed −29.2pp → **0.0pp** as the up-tape flattened; still BH-miscalibrated (claims 0.55, realises 0.39). Phase 3/5. C48 mechanism confirmed; a down-tape decides the sign. Patch: carry, P1.
3. **The frozen rubric has produced 0 HIGH/MED for a 5th straight cycle.** Post-freeze tiers are LOW (0.32, n25) and DROP (0.419, n222) only. Freeze-lift structurally cannot run. Phase 1/3b. Keep freeze, P1.

## Top 3 tool-tier surprises
1. `insights institutional-accumulation` flipped **−22.2pp → +18.2pp**; `dark-pool block-stratified` flipped **+15.9pp → −2.3pp** — the 07-11 "isolate block-stratified" pre-register is refuted. Phase 4.
2. **7th consecutive BH-null tool table** — zero tools survive multiple-hypothesis correction; the whole surface is class-outcome noise re-attributed per window.
3. `options-structure front-end-iv-ratio` **−21.3pp** — the one stable negative, the panic-gate tool with three documented failure modes. Structural, not act-now.

## What we'd do Monday
Nothing to the live files — and, again, that is the finding. Regime diversity finally arrived and it did not reveal an edge; it dissolved the ones the last audit thought it had. Every significant sign moved. The two things that *did* firm up both argue for standing pat: the out-of-regime **half-cap crossed into actionable territory and grades protective** (−14.3pp excess, n=34), and the **2026-07-03 model pins cleared** (97/97 quant compliance, stable debate residuals, zero sized blowups through a −10% pullback the fleet correctly dropped). The DROP pile (43.3%) again beat the traded book (41.1%) and the sized book (38.6%) — the system's best decision remains the trades it refuses to make. Keep the freeze, keep the half-cap, reset the bearish-line accrual, and wait for a genuine down-tape — it is still the only experiment that separates edge from beta, and we still haven't had one.
