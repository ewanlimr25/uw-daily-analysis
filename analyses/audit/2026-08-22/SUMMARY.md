# Calibration Audit — 2026-08-22

**737 verbatim envelope calls** (76 `decision.json`, 76/76 clean), 183/185 tickers OHLC-resolved
path-aware, **637 decided**, **0 `Σpoints ≠ raw_score` violations, 0 prose reconstruction**.
Eras never pooled (FROZEN `2026-06-12`: 586). 12th audit, 5th cross-regime cycle. **Third
straight cycle whose correct output is no new P0.**

## Top 3 schema flaws

1. **The vol lane is where the book bleeds — four instruments agree.**
   `vol_term_structure(+/−)` reads **−10.3pp on n=137, negative in *both* tapes** (−6.1/−13.4),
   so not a denominator artifact. Matches Phase 4's uniformly negative vol toolchain, the lane's
   WR (vol 36.7%, **`vol_short` 34.0%** vs 40.2% book) and `earnings_vol` 0.87→0.38 (n=130, BH
   p<0.001). Phase 5.1 → **C60**; procedure fix **P1 #3**.
2. **The ladder is monotone right up to where it claims most confidence:**
   `[0.395 DROP → 0.417 LOW → 0.500 MED → 0.385 HIGH]` — it breaks **only at the ≥9 cut**, 9th
   failed re-confirmation. Post-freeze: 489 resolved, **0 decided HIGH, 0 MEDIUM**. Phase 5.2 →
   keep freeze; the lift is unrunnable a 10th cycle and the freeze isn't the blocker.
3. **`[0.55,0.65)` still anti-predictive, still un-actionable.** Pooled 0.250 (n=52); the
   *correct* post-fix denominator is **19 of a required 30, unmoved**. All 22 post-fix in-band
   rows unsized, 13 cycles. Phase 3.3 → wait.

## Top 3 tool-tier surprises

1. **The 12-cycle BH-null streak breaks, on last cycle's own fix.** P1 #1 cut citations from
   **122 strings / 9.9% concatenated** to **17 / zero**; atomized, 43 ids, 2.4% trapped (was
   12.7%). `scripts/term_structure_hygiene.py` reads **−16.9pp, n=42, p=0.003, BH-surviving** —
   but 36/42 rows are August (weakest month) and the sign is opposite last cycle's +34.1pp/n=9.
   First clean measurement ⇒ **C61, not P0**.
2. **`dark-pool block-stratified`'s "six-cycle collapse" was partly denominator** — **+7.8pp
   (n=37)** unified. A modest, stable filter all along; never the 2026-05 +18pp.
3. **C16 lives after 8 cycles.** `dp_block_to_float_ratio` populates (9 decided) with **perfect
   rank separation** — the two largest ratios are the only WINs (p=0.028). Post-hoc on n=9 ⇒
   **C62, threshold fixed at 0.0010**, not promoted.

## What we'd do Monday

**Nothing to the book — one thing to the process.** The 08-01 short-routing P0 is perfectly
compliant a third cycle (0 sizing violations, counterfactual 28/28) and its evidence keeps
strengthening (`ALL/short` **p 0.0088→0.0026**; `ALL/long` **+13.9pp, p 0.0220→0.0003**, BH a
4th cycle in both tapes). But short-thesis *generation* has **halved** — 32.0%→17.6%, and
**at fixed uptrend regime 31.3%→17.4%, Fisher p=0.0045**. The P0 says *routing, not
suppression*; the drift starves the counterfactual keeping it honest. That's **P1 #1**. Rest is
instrumentation: canonicalize `vol_long` (5 rows); log *why* fundamentals VETOs, whose FP rate
has inverted past the book (0.562→0.500→0.474→**0.545**, VETO > CONFIRM — **watch, don't
loosen**); make float-ratio emission mandatory so C62 is testable in 4 weeks not 15. Keep freeze,
half-cap (−8.2pp, 7th straight negative), all nine gates (every measurable one effective, −8.8
to −39.8pp), Kelly off (n=27, non-monotone). New note: **payoff ratio orders the tiers where hit
rate doesn't** — DROP 0.647 vs LOW 0.929 / MED 0.948. Eight cycles of "the trades we refuse beat
the trades we take" may be a hit-rate illusion.
