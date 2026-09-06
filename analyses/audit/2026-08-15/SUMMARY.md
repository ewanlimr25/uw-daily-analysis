# Calibration Audit — 2026-08-15

Dataset: **672 verbatim envelope calls** (70 `decision.json`, 58 daily + 12 weekly; **70/70
validate clean**), 177/179 tickers OHLC-resolved path-aware, **572 decided**, **0
`Σpoints ≠ raw_score` violations**, **0 prose-reconstructed citations**. Eras never pooled:
05-25 (54) / 05-30 (69) / post-0606 (28) / **FROZEN 2026-06-12 (521)**. 11th edge audit;
fourth consecutive cross-regime cycle (320 up-tape / 252 down-tape, four populated regime
buckets). **Second consecutive cycle whose job was to grade a prior P0, not find a new one.**

## Top 3 schema flaws

1. **`earnings_vol` quotes 0.87 and realises 0.394 on n=109** — 47.7pp, BH at p<0.001, its
   **fifth** appearance. 12 of 13 quoted rows cite `win_rate_source: backtest`, but
   `signal-backtest` supports five classes and `earnings_vol` is not one — the number was
   never measured. `high_iv_rank` is the same defect (0.79 → 0.481, n=27, BH). Together they
   *are* the confident tail: the ≥0.80 reliability bucket realises **0.459 on n=37** and is 14
   `high_iv_rank` + 12 `earnings_vol` rows. Phase 3.1 / 3.3 → **P1 #2** (half-landed:
   `high_iv_rank` fixed, `earnings_vol` merely stopped quoting).
2. **The `[0.55,0.65)` band realises 0.245 against a 0.586 quote on the pooled corpus (n=49).**
   Third cycle, stable, strongly *anti*-predictive. The 07-25 starter-floor holds on sizing
   (all 8 post-cohort in-band rows `skip`/`watch_only`, zero sized) and the in-band share of
   quotes **rose 22% → 40%**. Phase 3.3 / 6.6. **→ P1 #3 was WITHDRAWN at application time and
   did NOT ship:** n=49 pools across rubric eras, whereas C56's bar counts **post-fix quoted
   rows only — 19 of a required 30**. That is the trap `signal-confluence-quant.md:71` warns
   about in writing, and it has now caught two consecutive audits, this one included.
3. **The freeze-lift is unrunnable by construction — 9th cycle — and the freeze is not the
   blocker.** 425 resolved post-freeze calls (14× the threshold) against **0 decided HIGH, 0
   decided MEDIUM**; 521 post-freeze rows → 461 DROP / 60 LOW, **one** `full`-sized call in
   the whole corpus. Frozen cuts non-monotone at the top (`[0.411, 0.419, 0.500, 0.385]`);
   tier inversion 7th cycle, present in all four eras *and* all four regime buckets, DROP
   (0.420, n=438) again beating LOW (0.389, n=108). Phase 5.3 / 5.4 → Keep freeze, **P1 #5**.

## Top 3 tool-tier surprises

1. **11th consecutive BH-null tool table — and this cycle we learned why the table itself is
   suspect.** Smallest p is 0.077 on n=6. But Phase 4 also found **122 distinct citation
   strings across 1,225 instances, 60 of them singletons, 52 containing `+` concatenations**;
   **155 citation instances were trapped in n<5 labels**. The same tool scores opposite tiers
   under different labels — `scripts/term_structure_hygiene.py` **+34.1pp** vs
   `iv-term-structure hygiene` **−39.7pp**. Eleven cycles of tool tiers rest on fragmented
   denominators. → **P1 #1**.
2. **C15 and C18 are not awaiting data — they cannot fire.** C15's trigger
   (`short_float ≥ 20% ∧ dtc ≥ 5`) has **never once been met**: zero `HIGH` squeeze readings
   in 167 populated rows (`LOW` 106 / `MODERATE` 11). C18's `insider_cluster_flag` is
   populated 20 times and is **`False` every time** — sixth cycle, zero variance. C16 is
   genuinely starved (populated 7 of 210; emitter still writes null). → **P1 #4: retire C15
   and C18.**
3. **`dark-pool block-stratified` completes a six-cycle collapse: +15.9 → −2.3 → +1.6 → +1.8
   → +2.1 → +3.0pp** (WR-with 0.45 vs 0.41, n=29). Meanwhile `options-flow
   sector-flow-persistence` reads **−7.3pp on n=80** and feeds the worst class in the book
   (`sector_rotation`, 0.282 on n=39) — exactly what scoring a gross-turnover metric as if it
   carried direction should look like.

## What we'd do Monday

**Nothing urgent, for the second cycle running — and that is again the finding.** The
2026-08-01 P0 routing shorts to watch-only applied clean a second time: **16/16 `watch_only`,
zero sized violations, counterfactual preserved 16/16**, and its justification held —
`ALL/short` paired McNemar **p = 0.0088** (BH-surviving, −13.1pp) with the deficit
near-identical in both tapes (−12.3pp up / −14.5pp down), the mis-selection signature rather
than mistiming. Direction-call accuracy confirms it independently: the book picks the right
side on 48.7% of up-tape rows and **36.7%** of down-tape ones. Its long mirror survives BH a
third time (+9.7pp, p = 0.0220) — still the only durable positive edge this system has
produced, and still not sized. Compliance is near-perfect: **5 missed gates in 1,163 non-DROP
obligations (0.43%)**, one sizing violation from June, all nine gates effective or advisory
with `cluster` at −25.3pp. The fundamentals VETO rate keeps converging from above
(0.562 → 0.500 → **0.474**, n=19) — monitor, don't touch.

So Monday was emitter work, not desk work — and it is **already done** (see `APPLIED.md`).
Shipped: the citation field is now one canonical tool id per component so Phase 4 can finally
measure something (P1 #1); a class-support check stops the fleet quoting backtest win-rates for
classes `signal-backtest` cannot measure — it catches **37 such quotes** in the corpus (P1 #2);
C15 and C18 are **retired** after six audits of accrual (P1 #4); the `dominant_signal_class`
emitter now points at the schema (P2 #7). All freeze-safe, 70/70 envelopes still validate, 423
tests green. **Withdrawn: the `[0.55,0.65)` re-derivation (P1 #3)** — it rested on a pooled
denominator, and C56's bar is 19 of a required 30 on the correct one. Keep the freeze, keep the
half-cap (out-of-regime −9.6pp on n=43, negative in all six measurements), keep every gate,
leave Kelly off at n=27 and non-monotone. One auditor-side correction landed too: **C59 cleared
its bar in-cycle at 5-of-9 divergent rows — the `opex_pin` 0.111 and `opex-pin-strategist`
−23.7pp are measurement artifacts** (PFE settled 0.00% from entry and was scored LOSS), not
findings about that lane. One thing worth watching: the sized book edged the
paper book for the first time (42.6% vs 41.3%, n=47) and beat DROP in the up tape (0.500 vs
0.419, n=30) while still trailing badly in the down tape (0.294 vs 0.423) — far too thin to
act on, but a second cycle of the same crack in "the trades we refuse beat the trades we take."
