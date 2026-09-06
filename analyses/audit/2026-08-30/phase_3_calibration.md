# Phase 3 — Calibration Audit (2026-08-30)

## C49 header — read this before any excess sentence below

| statistic | value | reading |
|---|---|---|
| strata cells (n ≥ 8) | 31 | |
| sd(book WR) | 0.1102 | |
| sd(benchmark WR) | 0.1402 | |
| **dispersion ratio** | **0.786** | best of the three cycles measured (0.63 → 0.73 → 0.79) |
| OLS `excess_pp` on `spy_wr` | **+28.6 − 68.7 × spy_wr**, R² **0.476** | |
| implied β(bookWR \| spyWR) | +0.31 | |
| **benchmark share of excess variance** | **47.6%** | down from 71.1% (2026-07-25) and 65.2% on the wide-cell cut |

Roughly **half** of this cycle's excess column is still the denominator. That is materially
better than the 71% that forced C49, but it is not clean. Every excess figure below is
printed with its `spy_benchmark_wr` and is subordinate to a row-matched paired McNemar.

---

## 3.1 PRIMARY EDGE TEST — tape-conditioned book WR + paired McNemar

BH applied **within** the 7-cell pre-registered direction × tape family (per 2026-08-01:
BH *within* a pre-registered family, not pooled with the exploratory sweep).

| cell | n | book WR | SPY WR | excess | b | c | p | BH |
|---|---|---|---|---|---|---|---|---|
| **DOWN / long** | 159 | 0.377 | 0.220 | **+15.7pp** | 40 | 15 | **0.0010** | **YES** |
| **ALL / long** | 271 | 0.417 | 0.317 | **+10.0pp** | 64 | 37 | **0.0093** | **YES** |
| **ALL / short** | 213 | 0.408 | 0.521 | **−11.3pp** | 32 | 56 | **0.0138** | **YES** |
| **DOWN / short** | 82 | 0.488 | 0.671 | **−18.3pp** | 12 | 27 | **0.0237** | **YES** |
| UP / short | 131 | 0.359 | 0.427 | −6.9pp | 20 | 29 | 0.2529 | no |
| UP / long | 112 | 0.473 | 0.455 | +1.8pp | 24 | 22 | 0.8830 | no |
| ALL (blended) | 484 | 0.413 | 0.407 | +0.6pp | 96 | 93 | 0.8844 | no |

**Fifth consecutive cycle** confirming the same two-sided structure: a **real long edge**
and a **real short deficit**, both row-matched, both BH-surviving. `ALL/long` p has held
0.0003 → 0.0093 and `ALL/short` 0.0026 → 0.0138 — softer than last cycle but the same sign,
and the softening is exactly what the halved short-generation rate predicts (fewer rows).

**The mechanism, stated plainly.** Direction-call accuracy: on UP tape the book was
positioned with the tape on **116/248 = 46.8%**; on DOWN tape **84/245 = 34.3%**. The fleet
is *worse than a coin flip* at picking the side of the tape, and worst precisely when the
tape falls. It makes money on the long book because longs win on their own ATR regardless,
not because it forecasts direction.

## 3.2 THE FINDING — the vol lane's SHORT side is inverted, and it is 42% of all risk ever taken

The vol lane was the one book with **no benchmark at all**. C21 gave directional rows a SPY
same-window base rate and left vol resolved against its own trailing range, which made "the
vol book lost" indistinguishable from "vol moved." Built this cycle, two benchmarks:

1. **SPY-RV** — would the identical vol bet on SPY have won over the same window?
2. **Unselected single-name peers** — the *same-date* RV-contraction rate across the whole
   190-name OHLC universe, and the same-date **peer-median** name as a row-matched partner.

Restricted to **complete 10-bar windows** (the conservative cut; the loose cut is worse):

| lane | n | book WR | **peer rate** | vs peers | SPY | vs SPY | McNemar vs peer-median |
|---|---|---|---|---|---|---|---|
| **`vol_short`** | **111** | **31.5%** | **56.6%** | **−25.1pp** | 58.6% | −27.0pp | **b=2 c=57, p < 0.0001** |
| `vol_long` | 43 | 53.5% | 44.0% | **+9.5pp** | 32.6% | +20.9pp | b=12 c=1, **p = 0.0034** |

**Every regime bucket, same sign, individually significant against the peer benchmark:**

| regime | n | book | peers | Δ | McNemar p |
|---|---|---|---|---|---|
| uptrend | 36 | 33.3% | 53.5% | −20.2pp | 0.0018 |
| pullback-in-uptrend | 18 | 16.7% | 51.8% | −35.1pp | 0.0034 |
| choppy | 17 | 41.2% | 64.7% | −23.5pp | 0.0020 |
| transitional/other | 40 | 32.5% | 58.0% | −25.5pp | 0.0000 |

**4 of 4 regime buckets. 3 of 4 months** (Jun −37.0 p=0.0002, Jul −11.0 p<0.0001,
Aug −60.8 p=0.0005; May n=6 thin). Loose-window `vol_short` overall: **−33.6pp, n=134,
McNemar b=12 c=57, p<0.0001, BH-surviving** in the pre-registered vol family.

**Three falsification attempts, all failed to kill it:**

- *"It's the tape."* No. August was a short-vol **paradise** at the index — mean SPY RV
  ratio **0.738**, only **12%** of windows expanded. The book's names went the other way
  (mean ticker RV ratio **1.199**). The confound runs opposite to the excuse.
- *"Single names are structurally more volatile than the index, so the SPY benchmark is
  rigged."* Partly true and it makes the finding **stronger**: on the same entry dates SPY
  contracts on 62.8% and the median single name on 79.1%. Swapping to the correct
  single-name peer benchmark still leaves **−25.1pp**.
- *"The selected names were just high-vol names."* Then `vol_long` would lose too. It gains
  **+9.5pp**. Selected short-vol names ran a mean RV ratio of **1.132** against a same-date
  peer median of **0.962**; selected long-vol names **1.037** against 0.965.

**Read it as a sign error, not a dead lane.** The scouts locate vol-expansion candidates
correctly — that is what `vol_long` at +9.5pp and 5-of-5 sized WINs says. On the short leg
the same identification is used to sell vol into the expansion.

**This is not paper.** `vol_short` is **20 of the 48 sized rows in the entire corpus — 42% of
every position the fleet has ever taken** (1 full, 7 half, 12 starter), against 5 for
`vol_long` (5 WIN / 5). The sized `vol_short` book realised **35.0% (n=20)**; the sized
`vol_long` book **100% (n=5)**.

**Instrument caveat, stated not buried.** Vol rows resolve `vol_resolution =
"rv_direction_proxy"` — RV direction, **not** IV-vs-RV. A premium seller can lose this test
and still book P&L if IV sat above realised. The proxy therefore cannot price a short-vol
trade and **the 31.5% must never be quoted as a P&L claim**. What it *can* price is
**selection**, because both benchmark columns remove the common component — and the
selection reading is what −25.1pp is.

## 3.3 Per-signal-class calibration (decided N ≥ 8)

| class | n | realised | claimed | div (pp) | SPY WR | excess | p | BH |
|---|---|---|---|---|---|---|---|---|
| **earnings_vol** | 144 | 0.33 | **0.87** | **+54.5** | 0.667 | −34.0 | 0.000 | **Y** |
| bearish_flow | 134 | 0.42 | 0.51 | +8.2 | 0.545 | −11.9 | 0.071 | n |
| multileg_directional | 97 | 0.40 | 0.56 | +15.3 | 0.370 | +3.2 | 0.004 | **Y** |
| bullish_flow | 66 | 0.44 | 0.52 | +7.5 | 0.318 | +12.1 | 0.270 | n |
| dark_pool_accumulation | 59 | 0.41 | 0.55 | +14.8 | 0.368 | +3.8 | 0.032 | **Y** |
| **sector_rotation** | 49 | 0.29 | 0.54 | **+25.0** | 0.292 | −0.6 | 0.001 | **Y** |
| dealer_positioning | 32 | 0.50 | 0.60 | +9.7 | 0.484 | +1.6 | 0.349 | n |
| **high_iv_rank** | 32 | 0.44 | **0.75** | **+31.7** | — | — | 0.000 | **Y** |
| oi_build | 21 | 0.43 | — | — | 0.300 | +12.9 | 1.000 | n |
| multi_day_sweep | 11 | 0.64 | 0.38 | −25.7 | 0.300 | +33.6 | 0.152 | n |
| **opex_pin** | 11 | **0.18** ⚠ | — | — | — | — | 1.000 | n |
| gamma_breakout | 10 | 0.20 | 0.51 | +31.1 | 0.600 | −40.0 | 0.094 | n |
| event_vol | 10 | 0.40 | — | — | 0.000 | +40.0 | 1.000 | n |

⚠ **`opex_pin` 18.2% is an artifact of the auditor's own resolver** — 63.6% under the C59
settlement rule (Phase 2). Do not act on it.

*THIN_N appendix (5–7):* `vol_term_dislocation` n=7, realised 0.000. Never in a headline.

**Desk note — `earnings_vol`.** *"Claims 0.87, realises 0.33 on n=144 — the widest lie in the
book, and it is the same 110 rows as the short-vol bleed above. Anyone quoting 87% into an
earnings vol sale is selling a coin-flip at eight-to-one odds on their own marketing."*

**Desk note — `sector_rotation`.** *"0.54 claimed, 0.29 realised, and its SPY base is 0.292 —
so it isn't even beta, it's beta minus friction. Three cycles of this. It buys the sector the
netted rotation already paid out on."*

**Calibrated-but-beta (verdict section d).** `dealer_positioning` — calibration honest
(0.50 vs 0.60), McNemar ns (p=1.0000), excess +1.6pp ≈ 0. Rides the tape. `multileg_directional`
and `dark_pool_accumulation` clear BH on divergence but their excess (+3.2 / +3.8pp) has
**no** McNemar support — under C49 that is a denominator reading, not a class finding.

## 3.4 Tier reliability — the inversion is now at the top AND the bottom

| tier | n | WR |
|---|---|---|
| HIGH | 7 | **14.3%** |
| MEDIUM | 19 | 52.6% |
| LOW | 125 | 40.0% |
| DROP | 542 | 38.0% |

`HIGH < DROP` by 23.7pp. Monotonicity requires HIGH > MEDIUM > LOW; it fails at the top.
**Era-stratified (never pooled):**

| era | HIGH | MEDIUM | LOW | DROP |
|---|---|---|---|---|
| era_0525_0529 | 0.250 (4) | 0.556 (9) | 0.579 (19) | 0.571 (21) |
| era_0530_0605 | 0.000 (2) | 0.500 (10) | 0.400 (25) | 0.419 (31) |
| pre_freeze_post_0606 | 0.000 (1) | — | 0.353 (17) | 0.500 (8) |
| **2026-06-12 (FROZEN)** | **— (0)** | **— (0)** | **0.359 (64)** | **0.367 (482)** |

**Tenth consecutive cycle with zero decided HIGH and zero decided MEDIUM post-freeze.** The
≥9 HIGH cut has now gone 546 resolved post-freeze rows without producing a single gradeable
HIGH. The inversion evidence is entirely pre-freeze; the freeze is not the blocker (Phase 5).

## 3.5 Brier, log-loss, reliability deciles

**Brier = 0.2857** (graded n=245) — above the 0.25 "no better than coin-flip" line.
**Log-loss = 0.790** vs 0.693 for a constant 0.5 forecast: **the rubric's confidence is worse
than saying nothing.**

| bucket | n | predicted | realised | gap |
|---|---|---|---|---|
| [0.00,0.50) | 77 | 0.39 | 0.44 | +0.05 ✅ |
| [0.50,0.55) | 62 | 0.53 | 0.48 | −0.05 ✅ |
| **[0.55,0.60)** | 35 | 0.57 | **0.23** | **−0.34** 🚩 |
| **[0.60,0.65)** | 19 | 0.61 | **0.26** | **−0.35** 🚩 |
| [0.65,0.70) | 7 | 0.66 | 0.57 | −0.09 |
| [0.70,0.80) | 8 | 0.77 | 0.75 | −0.02 ✅ |
| **[0.80,0.90)** | 31 | 0.83 | **0.45** | **−0.38** 🚩 |
| [0.90,1.01) | 6 | 0.93 | 0.50 | −0.43 |

The rubric is **well calibrated below 0.55 and above 0.70**, and catastrophically wrong in
the two bands where it expresses moderate-to-high confidence. Log-loss > Brier's implied
severity confirms the damage sits in the confident tail.

**C56 — the `[0.55,0.65)` anti-predictive band.** Pooled realised **0.241 (n=54)**;
post-fix (≥2026-07-25) **0.190 on 21 of a required 30**. Advanced 19 → 21 in a week. **0
post-fix rows sized above starter — perfect compliance, 14 cycles.** Still short of its bar;
still wait.

## 3.6 C3 — expectancy + Kelly activation gate

| tier | n | expectancy | payoff ratio | half-Kelly |
|---|---|---|---|---|
| HIGH | 7 | −2.441% | 0.720 | 0.0 |
| MEDIUM | 19 | +0.104% | 0.948 | 0.0132 |
| LOW | 125 | −2.141% | 0.906 | 0.0 |
| DROP | 542 | −5.964% | 0.601 | 0.0 |

**KELLY GATE: `ADVISORY_ONLY`.** n=27 closed sized calls vs a required 30; tier × expectancy
non-monotone (LOW −1.784 > HIGH −1.965 > MEDIUM −2.239). **Do not** flip
`signal-confluence-quant` / `risk-monitor` to the Kelly sizer. Win-rate ladder stays live.

**Second cycle of the payoff-ratio note:** DROP's payoff ratio (0.601) is far worse than
LOW/MEDIUM (0.906/0.948) and DROP's expectancy is worst by 3.8pp. The eight-cycle
"the trades we refuse beat the trades we take" reading rests on **hit rate alone** and does
not survive a payoff-aware metric. Not yet actionable (DROP is unsized by construction), but
it materially weakens the standing inversion narrative.

## Verdict

**(a) Where the rubric is honest.** Below 0.55 and in [0.70,0.80) the reliability diagram is
tight. `dealer_positioning` and `bearish_flow` quote close to what they realise. Σpoints
reconciliation is exact on 675 component rows.

**(b) Where it lies to itself.** `earnings_vol` claims 0.87 and realises 0.33 (n=144).
`high_iv_rank` claims 0.75, realises 0.44. `sector_rotation` claims 0.54, realises 0.29.
All three BH-surviving. These are the three classes that feed the vol lane and the rotation
lane — the two lanes with negative measured edge.

**(c) Tier inversion / high-tier overconfidence.** HIGH 14.3% < DROP 38.0%, and the
[0.80,0.90) reliability bucket realises 0.45 against a 0.83 claim. The rubric's confidence
signal is inverted exactly where a desk would lean on it.

**(d) Calibrated-but-beta.** `dealer_positioning` — honest, ns McNemar, excess ≈ 0. Rides the
tape. `multileg_directional` / `dark_pool_accumulation` positive excess with no row-matched
support: denominator, not edge.

## Outputs

`phase_3_calibration.jsonl` · `phase_3b_regime.jsonl` · `phase_3c_tape.jsonl` ·
`phase_3c_mcnemar.jsonl` · `phase_3d_excess_artifact.jsonl` ·
**`phase_3e_vol_mcnemar.jsonl`** (new) · **`phase_3f_peer_control.json`** (new).
