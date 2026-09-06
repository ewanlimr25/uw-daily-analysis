# Phase 3 — Calibration Audit (2026-09-05)

## Header, printed before any class commentary (C49 requirement)

| statistic | value | reading |
|---|---|---|
| strata cells (n ≥ 8) | 32 | |
| `sd(book WR)` | 0.1058 | |
| `sd(benchmark WR)` | 0.1377 | |
| **dispersion ratio** | **0.768** | book moves less than its denominator |
| OLS `excess_pp = +34.3 − 80.8 × spy_wr` | **R² = 0.541** | |
| implied β(bookWR \| spyWR) | +0.19 | |
| **benchmark share of excess variance** | **54.1%** | |

Phase 3d, run separately over a wider cell set, puts it at **65.9%** (slope −85.3, R² 0.595,
dispersion ratio 0.719). **Over half of this cycle's excess column is the denominator moving.**
Every excess number below is annotated, never leads, and never by itself carries a priority
above P2. The row-matched McNemar is the finding.

Better than last cycle (71.1%) but the mechanism is unchanged: book WR ranges [0.200, 0.700]
across cells while SPY ranges [0.211, 0.778]. Names regress toward a coin flip against their
own ATR; the benchmark does the moving.

## 3.1 — Class table, led by the row-matched test

Decided-N ≥ 8 (C23). Divergence p-values BH-controlled at FDR 0.10 across the class set.

| class | n | realised | claimed | div pp | spyWR | excess | BH |
|---|---|---|---|---|---|---|---|
| earnings_vol | 160 | 0.33 | 0.87 | 54.6 | 0.667 | −34.2 | **Y** |
| bearish_flow | 141 | 0.42 | 0.51 | 9.0 | 0.550 | −13.2 | **Y** |
| multileg_directional | 105 | 0.41 | 0.56 | 14.5 | 0.379 | +3.1 | **Y** |
| bullish_flow | 66 | 0.44 | 0.52 | 7.5 | 0.318 | +12.1 | n |
| dark_pool_accumulation | 63 | 0.41 | 0.55 | 14.2 | 0.371 | +4.2 | **Y** |
| sector_rotation | 51 | 0.31 | 0.54 | 22.2 | 0.314 | 0.0 | **Y** |
| dealer_positioning | 35 | 0.49 | 0.60 | 11.1 | 0.486 | 0.0 | n |
| high_iv_rank | 32 | 0.44 | 0.75 | 31.7 | — | — | **Y** |
| oi_build | 23 | 0.39 | — | — | 0.273 | +11.9 | n |
| vol_term_dislocation | 23 | 0.35 | — | — | 1.000 | −65.2 | n |
| multi_day_sweep | 11 | 0.64 | 0.38 | −25.7 | 0.300 | +33.6 | n |
| opex_pin (**C64 settlement**) | 11 | 0.64 | — | — | — | — | n |
| gamma_breakout | 10 | 0.20 | 0.51 | 31.1 | 0.600 | −40.0 | n |
| event_vol | 10 | 0.40 | — | — | 0.000 | +40.0 | n |

THIN_N appendix (5–7): **empty** this cycle.

### Primary edge test — paired McNemar, BH *within* the pre-registered family

Primary family = the 7 pre-registered direction × tape cells. Exploratory = the per-class
sweep. Pooling the two would be a post-hoc power tax on the pre-registered hypotheses.

| cell | n | bookWR | spyWR | b | c | p | BH |
|---|---|---|---|---|---|---|---|
| DOWN / long | 168 | 0.381 | 0.238 | 42 | 18 | **0.0027** | **YES** |
| DOWN / short | 88 | 0.466 | 0.693 | 12 | 32 | **0.0037** | **YES** |
| ALL / long | 284 | 0.426 | 0.324 | 66 | 37 | **0.0055** | **YES** |
| ALL / short | 232 | 0.401 | 0.522 | 34 | 62 | **0.0056** | **YES** |
| UP / short | 144 | 0.361 | 0.417 | 22 | 30 | 0.3317 | no |
| UP / long | 116 | 0.491 | 0.448 | 24 | 19 | 0.5424 | no |
| ALL | 516 | 0.415 | 0.413 | 100 | 99 | 1.0000 | no |

**The long book beats its own row-matched benchmark and the short book loses to it — for the
fourth consecutive audit, on 516 paired rows.** The `ALL/short` p-value has run 0.0115
(08-01) → 0.0038 (08-30) → **0.0056** (today). It is not decaying.

**Where the two sides are not symmetric:** `ALL` pooled is 0.415 vs 0.413, p=1.00. The book in
aggregate is *exactly* its benchmark. The edge is entirely a **composition** result — long
rows beat SPY-long, short rows lose to SPY-short, and they cancel. A desk should read that as
"we have one tradeable side and one that pays for it," not as "we have alpha."

### 3.2 — The vol lane, peer-controlled (last cycle's P0, +18 rows)

The benchmark is the unselected same-date single-name peer set, **not SPY** — the index
benchmark is ~8pp conservative because an index's realised range compresses against its own
constituents. Paired McNemar against the same-date peer majority:

| lane | n | book WR | peer WR | excess | b | c | p |
|---|---|---|---|---|---|---|---|
| **`vol_short`** | **129** | **0.287** | 0.581 | **−29.4pp** | **2** | **73** | **1.5 × 10⁻¹⁹** |
| `vol_long` | 56 | 0.500 | 0.415 | **+8.5pp** | 17 | 1 | 1.5 × 10⁻⁴ |

Per regime bucket, `vol_short` is negative **and individually significant in 4 of 4**:
uptrend −32.5pp (p<0.0001, n=54), transitional −24.7pp (p<0.0001, n=40), pullback −36.7pp
(p=0.0034, n=18), choppy −22.8pp (p=0.0020, n=17). Last cycle: −25.1pp on n=111. **More rows,
larger deficit, same sign, same four buckets.** This is the most robust single result in the
corpus and it survived a fourth window.

Caveat repeated: RV-direction proxy. It prices **selection, never P&L**.

### 3.3 — `earnings_vol` is not a class. It is the vol lane wearing a label.

Last cycle listed "earnings_vol claims 0.87, realises 0.33 (n=144, BH-surviving)" as flaw #2,
separate from the vol P0. **Decomposed, it is the same rows:**

| earnings_vol split | n | WR |
|---|---|---|
| thesis = `vol_short` | 99 | **0.232** |
| thesis = `vol_long` | 27 | **0.630** |

125 of 172 `earnings_vol` rows carry a `vol_short` thesis. The class-level 0.325 is a weighted
average of the lane the fleet is already forbidden to size and the lane it can't score. There
is **no independent `earnings_vol` calibration problem** — reporting it as one double-counts
the vol P0 across two headline slots. The 0.87 claim rests on **13 quoting rows, all
May–July**; quoting stopped, the lane did not.

### 3.4 — Tier reliability. The ladder is a fossil.

| tier | n | realised |
|---|---|---|
| HIGH | 7 | **0.143** |
| MEDIUM | 19 | 0.526 |
| LOW | 132 | 0.402 |
| DROP | 593 | 0.391 |

HIGH last of four, **fifth consecutive audit, and the same 7 rows every time.** Every HIGH and
MEDIUM row in this corpus is **pre-freeze**. Post-freeze the table is `LOW 71 / DROP 533`,
`HIGH n=0 / MEDIUM n=0`. **The freeze-lift test cannot run for the seventh consecutive cycle**
— and Phase 5 shows why, which is new.

Post-freeze book WR 0.379 (n=604), excess −0.8pp. LOW 0.366 vs DROP 0.381 — **the drop pile
still beats the book it was filtered out of.**

### 3.5 — Brier, log-loss, reliability

**Brier 0.2852 · log-loss 0.7883 · n = 251.** Log-loss above `ln 2 = 0.693` means the quotes
are **worse than forecasting a flat 0.5 on every row**. Brier ≥ 0.25 is "no better than a coin
flip." Both agree, and both are unchanged from last cycle (0.286 / 0.790).

| bucket | n | predicted | realised |
|---|---|---|---|
| [0.00,0.50) | 77 | 0.39 | 0.44 |
| [0.50,0.55) | 68 | 0.53 | 0.47 |
| **[0.55,0.60)** | 35 | 0.57 | **0.23** |
| **[0.60,0.65)** | 19 | 0.61 | **0.26** |
| [0.65,0.70) | 7 | 0.66 | 0.57 |
| [0.70,0.80) | 8 | 0.77 | 0.75 |
| **[0.80,0.90)** | 31 | 0.83 | **0.45** |
| [0.90,1.01) | 6 | 0.93 | 0.50 |

The anti-predictive mid-band [0.55,0.65) — floored to `starter` by the 2026-07-25 P1 #4 — is
**re-confirmed at 0.23 / 0.26 on 54 rows**, worse than the sub-0.50 bucket. The ≥0.80 tail
realises 0.45 on a 0.83 claim. The floor is earning its keep; do not lift it.

**Coverage warning.** `claimed_win_rate` emission is collapsing: **69% (May) → 50% → 24% →
21% → 9% (September, 7 of 81 rows)**. That is the honest-null discipline working as designed
(`win_rate_source: NA(substrate)`), but it means Brier/log-loss/reliability now describe a
**shrinking, non-random residue** — the rows where a clean backtest happened to be available.
Report the N beside every scalar; do not read the flat Brier as stability.

### 3.6 — Score → outcome. No slope.

`0 → 0.39 (n140) · 1 → 0.39 (n215) · 2 → 0.33 (n128) · 3 → 0.41 (n69) · 4 → 0.40 (n43) ·
5 → 0.57 (n14) · 7 → 0.71 (n7) · 8 → 0.29 (n7) · 9 → 0.67 (n6) · 10 → 0.00 (n3) ·
11 → 0.33 (n3) · 12 → 0.00 (n1)`

Flat from 0 to 4 — which is **99% of the post-freeze book** — then noise on single digits of N.
Scores 10–12 are **1-for-7 across every audit that has measured them.**

### 3.7 — Half-cap and the 08-01 short P0

Out-of-regime half-cap: OOR 0.326 (n=43) vs in-regime 0.398, **−23.5pp excess**. Negative in
every audit that has measured it — **ninth consecutive**. Keep it.

The 2026-08-01 short-routing P0, graded on its own post-change rows:

| arm | n | WR | McNemar |
|---|---|---|---|
| short, ≤ 2026-08-01 | 182 | 0.429 | b=27 c=51, **p=0.0088** |
| short, > 2026-08-01 | 51 | **0.294** | b=7 c=11, p=0.4807 |

**Read this carefully.** The post-P0 p-value is non-significant, but the win rate got *worse*
(0.429 → 0.294) and the sign is unchanged. The significance moved because **n fell**, not
because the deficit did. Post-P0 rows are paper — every one routed to `watch_only` — so this
is the counterfactual still resolving exactly as the P0 predicted. **Nobody should read
p=0.48 as "the short problem resolved."**

## Verdict

**(a) Where the rubric is honest.** Provenance, arithmetic, and routing. 88/88 envelopes
validator-clean, 0 `Σpoints ≠ raw_score` in 878 rows, zero prose reconstruction, both P0s at
**100% routing compliance** with generation intact. The `NA(substrate)` null is being emitted
rather than a circular number — 91% of September rows quote nothing, which is the correct
answer when the substrate can't support one.

**(b) Where it lies to itself.** The confidence quotes. Log-loss 0.788 > ln 2 says the quoted
win rates carry **negative information** — a flat 0.5 would score better. The [0.55,0.65) band
realises 0.23–0.26 against a 0.57–0.61 claim, and the [0.80,0.90) band realises 0.45 against
0.83. And `earnings_vol`'s 54.6pp divergence, the largest in the table, is **the vol P0 in a
costume** — a class label that has been carrying a second headline slot for a problem already
counted once.

**(c) Tier inversion / overconfidence.** HIGH 0.143, last of four tiers, fifth cycle, same 7
fossilised pre-freeze rows. DROP (0.391) ≈ LOW (0.402) — the filter is not separating. No
post-freeze row has ever reached MEDIUM. Phase 5 establishes that this is arithmetic, not
market conditions.

**(d) Calibrated-but-beta.** `dealer_positioning` (realised 0.486, spy 0.486, excess 0.0,
McNemar p=1.00 on n=35) and `sector_rotation` (0.314 vs 0.314, excess 0.0, p=1.00 on n=51) —
both pass the row-matched test *and* the excess column *and* agree. They are honest and they
are pure tape. `bearish_flow` (−12.9pp, p=0.033 exploratory, not BH-surviving in its family)
is the same story with a worse number.

## Kelly gate — ADVISORY_ONLY

`n = 27 closed of a required 30`, and tier × expectancy is **not** monotone
(LOW −1.784 / MEDIUM −2.239 / HIGH −1.965). Gate returns **ADVISORY_ONLY**. The win-rate
ladder stays live. **Do not flip `signal-confluence-quant` or `risk-monitor` to the Kelly
sizer.** Tier expectancy: HIGH −2.441 (n=7), MEDIUM +0.104 (n=19), LOW −2.059 (n=132),
DROP −5.111 (n=593) — the only positive-expectancy tier is the one the frozen rubric can no
longer produce.
