# Phase 3 — Calibration Audit (2026-08-01)

## C49 HEADER — read this before any excess number below

Per C49 the dispersion ratio and the OLS of excess on the benchmark are printed **first**,
so every excess sentence downstream is calibrated against them.

| C49 header statistic | 2026-08-01 | 2026-07-25 |
|---|---|---|
| strata cells (n≥8) | 20 | 34 |
| sd(book WR) | 0.1032 | — |
| sd(benchmark WR) | 0.1518 | — |
| **dispersion ratio sd(book)/sd(bench)** | **0.679** | 0.68 |
| OLS `excess_pp = a + b × spy_wr` | **+36.5 − 81.9 × spy_wr** | +36.5 − 80.0 × spy_wr |
| **R²** | **0.611** | 0.636 |
| implied β(bookWR \| spyWR) | +0.18 | +0.20 |
| **benchmark share of excess variance** | **68.4%** | 71.1% |

**C49 replicates almost exactly on an independent window.** Slope −81.9 against a
pure-artifact value of −100; book WR ranges 0.233–0.667 across cells while the SPY
benchmark ranges 0.174–0.800. Roughly **two-thirds of every excess number in this
document is the denominator moving.** Excess is annotated colour here, never a headline.

## 3.1 Signal-class table (decided ≥ 8)

Primary columns are realised WR and the paired-McNemar result (§3.4). Excess is shown
beside its own `spyWR`, as C49 requires.

| class | n | realised | claimed | div (pp) | spyWR | excess | p | BH |
|---|---|---|---|---|---|---|---|---|
| `bearish_flow` | 106 | 0.500 | 0.49 | −1.0 | 0.632 | −13.2 | 0.918 | no |
| **`earnings_vol`** | 97 | **0.44** | **0.88** | **+43.4** | 0.667 | −22.3 | **0.000** | **YES** |
| `multileg_directional` | 70 | 0.43 | 0.56 | +12.6 | 0.373 | +5.5 | 0.046 | no |
| `bullish_flow` | 51 | 0.41 | 0.54 | +12.8 | 0.275 | +13.7 | 0.091 | no |
| `dark_pool_accumulation` | 47 | 0.40 | 0.55 | +15.0 | 0.370 | +3.5 | 0.055 | no |
| **`sector_rotation`** | 32 | **0.25** | 0.54 | **+28.6** | 0.219 | +3.1 | **0.002** | **YES** |
| `dealer_positioning` | 27 | 0.52 | 0.60 | +7.8 | 0.481 | +3.7 | 0.523 | no |
| **`high_iv_rank`** | 24 | **0.50** | **0.82** | **+32.1** | — | — | **0.001** | **YES** |
| `multi_day_sweep` | 11 | 0.64 | 0.38 | −25.7 | 0.222 | +41.4 | 0.152 | no |
| `oi_build` | 11 | 0.46 | — | — | 0.273 | +18.2 | 1.000 | no |
| `opex_pin` | 9 | 0.11 | — | — | — | — | 1.000 | no |
| `gamma_breakout` | 8 | 0.25 | 0.51 | +26.1 | 0.500 | −25.0 | 0.260 | no |

Thin-N appendix (decided 5–7): empty this cycle.

### Desk commentary

**`earnings_vol` — the same lie, for the fifth audit running.** Claims 0.88, realises
0.44 on n=97, BH-surviving at p<0.001. This is now the single largest and most durable
miscalibration in the book. Anyone reading an 0.88 quote off an earnings-vol name is
being told a coin-flip is a near-certainty. It has survived every re-measurement since
2026-06-06; it is not noise and it is not regime.

**`sector_rotation` — new entrant to the BH-significant list, and it's ugly.** Realises
**0.25 on n=32** against a 0.54 claim. Not merely miscalibrated — it is the worst realised
win rate of any class with real N in the book. The class rides `sector-flow-persistence`,
which the project already knows is a **turnover** metric, not a net-accumulation one. A
desk trading rotation calls off this line is picking the wrong side about three times in four.

**`high_iv_rank` — 0.82 quoted, 0.50 realised (n=24), BH-surviving.** The second vol-lane
BH-significant lie, reconfirmed for a fourth audit. Both vol-lane offenders are quoting in
the ≥0.80 band that the 2026-06-06 cap was supposed to close; see §3.3.

**`bearish_flow` — the best-calibrated large class in the system.** 0.500 realised vs
0.49 claimed on n=106, p=0.918. This is the third consecutive window in which
`bearish_flow` is honest about itself, and it is the direct confirmation that closing
**C19 as refuted** (registered C53 at 07-25) was correct: the class has no hidden edge to
graduate, it just tells the truth.

**`multi_day_sweep` — the only class quoting *under* itself.** Claims 0.38, realises 0.64
on n=11. Under-confident, but n=11 and BH-null; C46 stays registered, not promoted.

## 3.2 Tier reliability

| Tier | n | realised WR |
|---|---|---|
| HIGH | 7 | **0.143** |
| MEDIUM | 19 | 0.526 |
| LOW | 91 | 0.418 |
| DROP | 384 | **0.440** |

**Tier order fails for a 5th consecutive audit.** HIGH 0.143 < LOW 0.418 < DROP 0.440.
Every HIGH and MEDIUM row in the corpus is **pre-freeze** — the frozen rubric has emitted
neither for seven cycles — so this is a verdict on the *old* cut, re-confirmed, not new
evidence about the live one.

Era × tier (inversion persistence):

| era | HIGH | MEDIUM | LOW | DROP |
|---|---|---|---|---|
| `era_0525_0529` | 0.25 (4) | 0.556 (9) | 0.579 (19) | 0.571 (21) |
| `era_0530_0605` | 0.00 (2) | 0.500 (10) | 0.400 (25) | 0.419 (31) |
| `pre_freeze_post_0606` | 0.00 (1) | — | 0.353 (17) | 0.500 (8) |
| **`2026-06-12` (live)** | — (0) | — (0) | 0.367 (30) | 0.432 (324) |

**DROP has out-realised the traded book in every single era.** That is the empty-board
discipline grading correct for a 7th cycle, not a bug.

## 3.3 Brier, log-loss, reliability

**Brier = 0.2864** · **log-loss = 0.7973** · graded n = 199.

Brier sits just past the 0.25 "no better than coin-flip" line. Log-loss at 0.797 against
a 0.693 coin-flip baseline confirms the damage is concentrated in confident-and-wrong
quotes rather than spread evenly.

| bucket | n | predicted | realised | verdict |
|---|---|---|---|---|
| [0.00,0.50) | 64 | 0.38 | 0.44 | under-confident, honest |
| [0.50,0.55) | 50 | 0.52 | 0.54 | **well calibrated** |
| **[0.55,0.60)** | 22 | 0.57 | **0.27** | **anti-predictive** |
| **[0.60,0.65)** | 12 | 0.62 | **0.33** | **anti-predictive** |
| [0.65,0.70) | 7 | 0.66 | 0.57 | thin |
| [0.70,0.80) | 8 | 0.77 | 0.75 | good |
| **[0.80,0.90)** | 30 | 0.83 | **0.43** | **−40pp, legacy pre-cap** |
| [0.90,1.01) | 6 | 0.93 | 0.50 | legacy pre-cap |

### 3.3b The [0.55,0.65) band — and whether the 07-25 fix worked

The band remains anti-predictive: **34 rows, realised ≈0.29 against ~0.58 predicted.**
That is an improvement on 07-25 (0.179) but still a confidence statement that is worse
than useless — a quote in this band is negatively informative.

**The applied fix is binding, but only on sizing.** Of the 15 quoted rows written after
commit `c69a359`:

- **15/15 carry `win_rate_source = backtest_clean`** — the provenance requirement is live
  and 100% enforced (corpus-wide the field is `NA(substrate)` on 232 rows).
- **11/15 quote inside [0.55,0.65)** — and **all 11 size to `skip`**. Not one reached the
  half rung. The sizing floor works exactly as specified.
- But the band's *share of emissions rose* from 25.0% (post-freeze, pre-fix) to **73.3%**.

So the desk got the protection it asked for and none of the accuracy. The rubric's modal
confidence statement is still a number the data says to invert; it simply no longer
carries size. That is the right order of operations, but the emission itself is unfixed.

## 3.4 PRIMARY EDGE TEST — paired McNemar (C49)

Row-matched: each row's own outcome against its own same-window SPY outcome, so the
benchmark cancels pairwise. BH (FDR 0.10) applied **within family** — a 7-cell
pre-registered primary family and a separate exploratory class sweep. (Pooling the two
would be a post-hoc power tax, not a result.)

| cell | n | book WR | spy WR | excess | b (book-only) | c (SPY-only) | p | BH |
|---|---|---|---|---|---|---|---|---|
| **ALL / long** | 204 | 0.412 | 0.289 | +12.3 | 49 | 24 | **0.0046** | **YES** |
| **ALL / short** | 163 | 0.460 | 0.595 | −13.5 | 24 | 46 | **0.0115** | **YES** |
| **UP / long** | 78 | 0.487 | 0.308 | +17.9 | 23 | 9 | **0.0201** | **YES** |
| UP / short | 92 | 0.402 | 0.533 | −13.0 | 12 | 24 | 0.0652 | no |
| DOWN / long | 126 | 0.365 | 0.278 | +8.7 | 26 | 15 | 0.1173 | no |
| DOWN / short | 71 | 0.535 | 0.676 | −14.1 | 12 | 22 | 0.1214 | no |
| ALL | 367 | 0.433 | 0.425 | +0.8 | 73 | 70 | 0.8672 | no |

**This is the headline of the audit.** For the first time the system produces a
BH-surviving row-matched result on *both* sides, and they point in opposite directions:

1. **The long book has real, replicated edge.** `ALL / long` p=0.0046 (was p=0.0081 at
   07-25 on n=186; now n=204). It wins 49 pairs where a same-window SPY long lost and
   loses only 24 the other way. Two independent windows, same sign, both BH-surviving.
2. **The short book has real, significant *negative* edge.** `ALL / short` p=0.0115,
   b=24 vs c=46 — the fleet's selected shorts lose to a naive same-window index short by
   roughly 2:1 on discordant pairs. At 07-25 this was only suggestive (DOWN/short
   p=0.1214, flagged "ns — not proven"). **With 61 more decided rows it is now proven.**

Note the direction of the tape does *not* rescue the shorts: UP/short −13.0pp and
DOWN/short −14.1pp are nearly identical. The short book is not mistimed, it is
mis-selected — it underperforms an index short by the same margin whether the market
rises or falls. That is a selection defect, not a regime defect.

Exploratory family: no class-level cell survives BH. `bearish_flow` at p=0.0649 is the
nearest, and its book WR is stationary across tapes (0.449 UP / 0.544 DOWN) — consistent
with C53's closure of C19.

## 3.5 Score → win-rate monotonicity

`{-3: 0.39(18), -2: 0.70(10), -1: 0.39(41), 0: 0.45(100), 1: 0.42(134), 2: 0.41(74),
3: 0.47(40), 4: 0.40(35), 5: 0.56(9), 6: 0.46(13), 7: 0.71(7), 8: 0.29(7), 9: 0.67(6),
10: 0.00(3), 11: 0.33(3), 12: 0.00(1)}`

Flat and non-monotone across the working range 0→4 (0.45 → 0.42 → 0.41 → 0.47 → 0.40).
The raw score still carries almost no ordering information about outcomes. Cells at
score ≥7 are n≤7 and unusable.

## 3.6 C3 expectancy + Kelly activation gate

| Tier | mean realised P&L | payoff ratio | half-Kelly | n |
|---|---|---|---|---|
| HIGH | −2.441 | 0.72 | 0.0 | 7 |
| MEDIUM | +0.104 | 0.948 | 0.0132 | 19 |
| LOW | −0.583 | 1.197 | 0.0 | 91 |
| DROP | −2.270 | 0.824 | 0.0 | 384 |

**Kelly gate: `ADVISORY_ONLY`.** n=27 closed < 30 required, and tier × expectancy is
non-monotone (LOW −1.784 > HIGH −1.965 > MEDIUM −2.239). Do **not** flip
`signal-confluence-quant` or `risk-monitor` to the Kelly sizer. The win-rate ladder
stays live.

## Verdict

**(a) Where the rubric is honest.** `bearish_flow` (0.500 vs 0.49, n=106) — the
best-calibrated large class in the system. The [0.50,0.55) decile (0.54 realised vs 0.52
predicted, n=50). The sub-0.50 bucket, which is under-confident in the safe direction.
The 2026-06-06 emission cap binds perfectly: **zero post-freeze quote exceeds 0.80.**

**(b) Where it lies to itself.** `earnings_vol` at +43.4pp divergence (n=97) and
`high_iv_rank` at +32.1pp (n=24) — both BH-surviving, both vol-lane, both re-confirmed
for a 4th–5th audit. `sector_rotation` joins them this cycle at +28.6pp with a realised
0.25. And the [0.55,0.65) band, which is the rubric's modal confidence statement and is
**negatively** informative.

**(c) Tier inversion / HIGH-tier overconfidence.** HIGH 0.143 (n=7) below DROP 0.440
(n=384), 5th consecutive audit. All HIGH/MEDIUM rows pre-date the freeze; the live rubric
has emitted none in seven cycles, so the lift test remains structurally unrunnable.

**(d) Calibrated-but-beta.** `bearish_flow` qualifies on the strict C49 reading:
calibration ✅ (p=0.918), paired McNemar non-significant (p=0.0649, BH-null), excess ≤ 0
(−13.2pp). The row-matched test agrees with the excess column, so this is a genuine class
finding and not a denominator reading — the class is honest, and it does not beat the tape.
`dealer_positioning` (+3.7pp, p=1.000, n=27) and `dark_pool_accumulation` (+4.3pp,
p=0.8238, n=46) are likewise indistinguishable from beta.

Output: `phase_3_calibration.jsonl`, `phase_3b_regime.jsonl`, `phase_3c_tape.jsonl`,
`phase_3c_mcnemar.jsonl`, `phase_3d_excess_artifact.jsonl`.
