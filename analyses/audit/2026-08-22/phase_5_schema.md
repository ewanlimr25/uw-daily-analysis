# Phase 5 — Grading the FROZEN Rubric (2026-08-22)

> **RUBRIC FREEZE 2026-06-12 (audit P0.1).** This phase **grades** the frozen weights and cuts.
> It emits **no weight edit and no cut edit** — only pre-registered change hypotheses with
> acceptance bars decided by a *future* audit on data that does not yet exist. Every table is
> stratified by `rubric_version`; eras are never pooled into a weight claim.

**Provenance:** 100% verbatim envelope `score_components[]`, 0 prose reconstruction, **0
`Σ points ≠ raw_score` violations** across 737 rows.

## 5.1 — Frozen component grading (marginal contribution per signed point)

BH FDR 0.10 applied **within the 19-line component family**. `[+N]` is the points the line
awarded on that row; `pts` is the signed weight.

| component line | pts | n | WR with | WR w/o | marg (pp) | p | BH | UP tape | DN tape |
|---|---|---|---|---|---|---|---|---|---|
| `oi_trend_building(+1)` | +1 | 181 | 0.381 | 0.410 | −2.9 | 0.477 | n | +2.6 | −6.2 |
| **`vol_term_structure(+/−)`** | **+1** | **137** | **0.321** | 0.424 | **−10.3** | **0.018** | n | −6.1 | −13.4 |
| `cum_flow_intent(+1)` | −1 | 128 | 0.391 | 0.405 | −1.4 | 0.819 | n | +3.8 | −5.9 |
| `cum_flow_intent(+1)` | +1 | 105 | 0.438 | 0.395 | +4.3 | 0.417 | n | +4.2 | +4.3 |
| `multileg_structure(+2)` | +2 | 98 | 0.408 | 0.401 | +0.7 | 0.957 | n | +4.6 | −3.2 |
| `cum_flow_intent(+1)` | −3 | 71 | 0.451 | 0.396 | +5.5 | 0.408 | n | +4.2 | +6.5 |
| `sector_persistence(+1)` | +1 | 55 | 0.418 | 0.400 | +1.8 | 0.888 | n | −2.1 | +4.7 |
| `accumulation_conjunction(+3)` | +1 | 48 | 0.438 | 0.399 | +3.9 | 0.685 | n | +4.2 | +3.7 |
| `signal_confluence(+1)` | +2 | 46 | 0.391 | 0.403 | −1.1 | 1.000 | n | +14.0 | −5.8 |
| `dealer_dex_flip(+1)` | +1 | 45 | 0.489 | 0.395 | **+9.4** | 0.259 | n | −1.2 | +21.7 |
| `cum_flow_intent(+1)` | +3 | 42 | 0.476 | 0.397 | +8.0 | 0.369 | n | — | +10.4 |
| `dealer_dex_flip(+1)` | +3 | 31 | 0.355 | 0.404 | −4.9 | 0.714 | n | −30.9 | +6.4 |
| `earnings_catalyst(+/−)` | +1 | 28 | 0.357 | 0.404 | −4.7 | 0.764 | n | — | −5.3 |
| `oi_trend_building(+1)` | +3 | 27 | 0.481 | 0.398 | +8.3 | 0.489 | n | +16.9 | −1.1 |
| `accumulation_conjunction(+3)` | +3 | 16 | 0.375 | 0.403 | −2.8 | 1.000 | n | — | −2.1 |
| `vol_term_structure(+/−)` | 0 | 10 | 0.500 | 0.400 | +10.0 | 0.735 | n | — | — |
| `dealer_dex_flip(+1)` | +2 | 9 | 0.667 | 0.398 | +26.9 | 0.195 | n | — | — |
| `sector_persistence(+1)` | 0 | 9 | 0.000 | 0.408 | −40.8 | 0.018 | n | — | −40.5 |
| `other: term_structure_hygiene` | +1 | 8 | 0.000 | 0.407 | −40.7 | 0.031 | n | — | −40.4 |

**Zero BH survivors in the component family** — twelfth consecutive cycle. No frozen weight has
produced evidence clearing its own bar. **The freeze is doing exactly what it was built to do.**

### Quant read

The only line with a *material* effect at a *material* n is **`vol_term_structure(+/−)` at
−10.3pp on n=137** (p=0.018 raw, BH-null in-family). It is negative in **both** tapes (−6.1 up,
−13.4 down) — so unlike almost every other reading in this audit, it is not a denominator
artifact. It also lines up with three independent measurements this cycle: the vol toolchain
block in Phase 4 (`term-skew` −10.5, `front-end-iv-ratio` −10.4, `hygiene` −16.9), the vol-lane
outcome gap in Phase 2 (`vol` 36.7% vs book 40.2%, `vol_short` **34.0%**), and the historical
`earnings_vol` / `high_iv_rank` calibration failures in Phase 3. **Four separate instruments
pointing at one lane is the strongest structural signal in this audit** — and it is still not
enough to move a frozen weight on one window's data.

`dealer_dex_flip(+1)` remains the best-looking line (+9.4pp, n=45) and remains BH-null; its
tape split (−1.2 up / **+21.7** down) says whatever it has is a *down-tape* property, which is
also the tape where the long book's edge is largest (+15.5pp). Worth watching together.

The two −40pp lines (n=9, n=8) are **THIN_N noise** and are reported only so they are not
silently dropped.

## 5.2 — Tier-cut monotonicity vs the frozen cuts

Frozen: **HIGH ≥9 / MEDIUM 7–8 / LOW 3–6 / DROP ≤2.** Graded on realised WR per score band.

| band | n | WR |
|---|---|---|
| DROP (≤2) | 478 | 0.395 |
| LOW (3–6) | 132 | 0.417 |
| MEDIUM (7–8) | 14 | 0.500 |
| **HIGH (≥9)** | **13** | **0.385** |

**Monotone ascending DROP→HIGH? NO** — `[0.395, 0.417, 0.500, 0.385]`.

This is a more informative failure than the headline tier inversion. **The score ladder is
monotone through MEDIUM** (0.395 → 0.417 → 0.500) and breaks **only at the ≥9 HIGH cut**, which
collapses to 0.385 on n=13. The rubric orders conviction correctly right up to the point where
it claims its highest confidence. Ninth cycle the ≥9 cut has failed its own re-confirmation.

**Post-freeze only:** DROP 0.383 (n=418) / LOW 0.394 (n=71) / MEDIUM 1.000 (**n=1**) / HIGH
**n=0**. The freeze-lift remains **unrunnable — 10th consecutive cycle** — and, as the last two
audits established, *the freeze is not the blocker*: 489 resolved post-freeze calls (16× the
n≥30 threshold) simply never produced a HIGH or MEDIUM. The fleet's own gates, not the freeze,
are what stop the top of the ladder from being populated.

## 5.3 — P0.6 out-of-regime half-cap

| | n | WR |
|---|---|---|
| out-of-regime | 43 | **0.326** |
| in-regime | 594 | 0.407 |

**Δ = −8.2pp; ACTIONABLE at n=43; the cap is PROTECTIVE. KEEP IT.** Seventh consecutive
negative measurement; excess-side −23.5pp (Phase 3.6). No lift.

## 5.4 — Pre-registrations emitted (no edits)

### C60 — the vol-lane rubric line may be net-negative

```
rubric_line:   vol_term_structure(+/-)  [+1 award]
direction:     reduce toward 0, or make the award conditional on VRP state
mechanism:     the fleet awards a point for a term-structure signal, then trades the
               vol lane on it; the lane realises 36.7% vs a 40.2% book and 34.0% on
               vol_short. Corroborated independently by Phase 4 (term-skew -10.5,
               front-end-iv-ratio -10.4, hygiene -16.9), Phase 2 (lane WR gap) and
               Phase 3 (earnings_vol / high_iv_rank historical miscalibration).
evidence now:  -10.3pp, n=137, p=0.018 raw, BH-NULL in the 19-line component family;
               negative in BOTH tapes (-6.1 up / -13.4 down)
acceptance:    cross-regime (>=3 populated regime buckets) AND n>=30 per tape arm
               AND BH-surviving at FDR 0.10 WITHIN the component family
decision:      2026-10-03 audit or later
```

### C61 — `scripts/term_structure_hygiene.py` tool-level negative

```
tool:          scripts/term_structure_hygiene.py
direction:     investigate how the fleet CONSUMES the corrected label (a hygiene
               script cannot itself be directionally wrong); candidate fix is a
               confirmation requirement on hygiene-corrected KINKED/BACKWARDATION
               labels before a vol structure may be proposed
evidence now:  -16.9pp, n=42, p=0.003, FIRST BH-surviving tool result in 12 cycles.
               CONFOUNDED: 36 of 42 rows are August 2026, the weakest month in the
               corpus (0.318). Within-August control holds (0.194 n=36 vs 0.380 n=71;
               August vol rows 0.174 n=23 vs 0.348 n=23) but is thin and single-regime.
               Sign is opposite the prior cycle's reading (+34.1pp, n=9) under a looser
               normalization -- this is the FIRST clean measurement of it.
acceptance:    n>=30 NON-August rows, >=2 regime buckets, BH-surviving at FDR 0.10 on
               a month-stratified denominator
decision:      2026-10-03 audit or later
```

**No other pre-registration is emitted.** C56 (the `[0.55,0.65)` band) remains **OPEN at 19 of a
required 30** post-fix decided rows and did not advance materially this cycle.

### C62 — float-normalized DP block size may separate accumulation winners (C16's promotion path)

```
criterion:     C16 (fz float-normalized dark-pool block), promotion from advisory
threshold:     PRE-REGISTERED HERE, to be tested OUT OF SAMPLE, not re-fit:
                 dp_block_to_float_ratio >= 0.0010
direction:     rows at/above the threshold outperform the dark_pool_accumulation
               baseline; rows below it underperform
mechanism:     a dollar-tier block filter cannot tell a $50M print in a 400M-share
               float from the same print in a 40M-share float. Normalizing by float
               is what converts "a big print" into "a big position".
evidence now:  the field finally populates (10 calls, 9 decided) after the 2026-08-15
               backfill-duty sharpening. WR 0.222 (n=9) vs 0.397 baseline in aggregate,
               BUT with PERFECT RANK SEPARATION: the two largest ratios (0.0023 NBIS,
               0.0022 SNDK) are the only two WINs; all seven rows <= 0.00058 are LOSS.
               Random-assignment p = 1/C(9,2) = 0.028. POST-HOC THRESHOLD ON n=9 --
               this is a hypothesis, not a result.
acceptance:    n>=30 populated+decided rows with >=10 per arm, >=2 regime buckets,
               BH-surviving at FDR 0.10, threshold FIXED at 0.0010 (no re-fitting;
               a re-fit threshold voids this registration)
decision:      2026-10-03 audit or later
blocker:       emission rate. 10 populated of 275 calls carrying the key. At the
               current ~2/week the bar is ~15 weeks away.
```
