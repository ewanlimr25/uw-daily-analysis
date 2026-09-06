# Calibration Audit — 2026-08-01

Dataset: **578 verbatim envelope calls** (58 `decision.json`, 48 daily + 10 weekly; 58/58
validate clean), 158/160 tickers OHLC-resolved path-aware, **501 decided**, **0
`Σpoints≠raw_score` violations**. Strata never pooled: pre-freeze 05-25 (54) / 05-30 (69)
/ post-0606 (28) / **FROZEN 2026-06-12 (427)**. 9th edge audit; second consecutive cycle
with both tapes in size (232 up / 269 down).

## Top 3 schema flaws

1. **The short book has a statistically significant NEGATIVE edge — and it is
   regime-independent.** `ALL / short` paired McNemar **p=0.0115, BH-surviving**, b=24 vs
   c=46 (n=163): the fleet's shorts lose discordant pairs to a naive same-window index
   short ~2:1. UP −13.0pp, DOWN −14.1pp — near-identical, so this is mis-*selection*, not
   mistiming. Direction-call accuracy 36.0% in a falling tape; sized book 0.294 vs a DROP
   pile of 0.411. At 07-25 this was "suggestive, not proven" (p=0.1214). **C52's bar is
   now met.** Phase 3 §3.4 / 3c / 5.6. → **P0**.
2. **`sector_rotation` realises 0.25 on n=32 against a 0.54 claim** (BH, p=0.002) — the
   worst realised win rate of any class with real N. Corroborated by the
   `sector_persistence` 0-point line at −44.2pp. Mechanism is already known: the class
   reads a **gross-turnover** metric as net accumulation. Phase 3 §3.1 / 5.1. → C55, P1.
3. **The frozen rubric has emitted 0 HIGH and 0 MEDIUM for a 7th straight cycle** (427
   post-freeze rows → 42 LOW, 385 DROP; **one** `full`-size call in the entire corpus).
   Freeze-lift is not unsatisfied, it is *structurally unrunnable*. Tier order fails a 5th
   time: HIGH 0.143 < LOW 0.418 < DROP 0.440. Phase 3 §3.2 / 5.3. → Keep freeze, P1.

## Top 3 tool-tier surprises

1. **9th consecutive BH-null tool table** — smallest p in the sweep is 0.197. Nine windows,
   zero tools that survive correction as outcome discriminators. The rubric's premise that
   citing more tools raises conviction has no support in the data. Phase 4.
2. **`dark-pool block-stratified` completes its collapse**: +15.9 → −2.3 → +1.6 → **+1.8pp,
   with WR-with 0.42 against WR-without 0.44.** A gate splitting the book into two piles of
   identical win rate. Phase 4.
3. **The 07-25 fixes are verifiable in the live output.** `insider_cluster_flag` now
   populates 44/44 post-fix calls (**C18 unblocked**); the debate-residual bin floor works
   (22 sub-0.55 rows recovered); 15/15 post-fix quotes are `backtest_clean` and all 11
   in-band rows size to `skip`. Only `dp_block_pct_of_float` was missed — **C16 is on its
   4th untestable audit.** Phase 6 §6.7.

## What we'd do Monday

For the first time in nine audits there is a P0 against the *subject*, not the auditor.
The long book's row-matched edge replicated and strengthened (`ALL / long` p=0.0046,
n=204, b=49/c=24) — that finding is now two-for-two across independent windows. Its mirror
is that the short book is significantly worse than a naive index short, in both tapes, by
the same margin. **Route short theses to watch-only rather than sizing them** — as routing,
not suppression, so the counterfactual keeps resolving and the next audit can grade it.
That is the one change worth making before the next session; it is also the audit's most
invasive proposal, and the short lane should not be deleted on n=163.

Everything else holds. Keep the freeze (0 of 17 component lines survive BH, 9th cycle),
keep the out-of-regime half-cap (−12.0pp on n=43, negative in all four measurements),
keep every risk gate (all nine effective; `cluster` −28.0pp; zero drift — **0/42 missed
gates on the live rubric**), leave Kelly off at n=27. C49 replicates almost exactly on an
independent window (slope −81.9, R² 0.611, 68.4% of excess variance is the benchmark), so
the demotion of raw excess stands and `bearish_flow`'s honesty — 0.500 realised vs 0.49
claimed on n=106 — confirms C19 was correctly closed as refuted. Then fix the two things
the fleet is still telling itself: the 0.88 `earnings_vol` quote that realises 0.44, and
the [0.55,0.65) band that is now 73% of all emissions and negatively informative.
