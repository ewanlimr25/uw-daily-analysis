# Phase 3d — Benchmark-excess artifact re-test (C49) — 2026-08-01

C49 was registered at 2026-07-25 off a single window. This phase re-runs the same
decomposition on an independent one (61 additional decided rows, both tapes present) to
test whether the artifact was itself an artifact.

## Result — C49 replicates

| statistic | 2026-08-01 | 2026-07-25 | pure artifact |
|---|---|---|---|
| OLS slope (pp per 1.00 spy_wr) | **−81.9** | −80.0 | −100 |
| R² | **0.611** | 0.636 | 1.000 |
| sd(book WR) | 0.1032 | — | 0 |
| sd(spy WR) | 0.1518 | — | — |
| **dispersion ratio** | **0.679** | 0.68 | 0 |
| implied β(bookWR \| spyWR) | +0.18 | +0.20 | 0 |
| **benchmark share of excess variance** | **68.4%** | 71.1% | 100% |

`var(excess) = 253.1`, `var(bookWR) = 106.4`, `var(spyWR) = 230.5`.

Book WR ranges **[0.233, 0.667]** across the 20 strata cells (spread 0.434) while the SPY
benchmark ranges **[0.174, 0.800]** (spread 0.626). The benchmark moves 1.4× as much as
the book it is subtracted from.

## Mechanism

Names resolve to roughly a coin-flip against their **own** ATR-scaled threshold regardless
of what the index does — the 0.5-ATR first-touch rule normalises away most of the market
move. SPY resolved against *its* own threshold does not: it swings from 0.174 to 0.800
across windows. So the difference of the two is dominated by the term that moves.

## Cells (sorted by excess)

| cell | n | book WR | spy WR | excess |
|---|---|---|---|---|
| era_0525_0529 | 40 | 0.550 | 0.450 | +10.0pp |
| multileg_directional / UP | 41 | 0.488 | 0.415 | +7.3pp |
| pullback / long | 51 | 0.510 | 0.451 | +5.9pp |
| dealer_positioning | 27 | 0.519 | 0.481 | +3.7pp |
| tier=DROP | 262 | 0.439 | 0.427 | +1.1pp |
| era_0530_0605 | 56 | 0.429 | 0.429 | +0.0pp |
| choppy / long | 11 | 0.636 | 0.636 | +0.0pp |
| pre_freeze_post_0606 | 25 | 0.400 | 0.400 | +0.0pp |
| era=2026-06-12 | 246 | 0.419 | 0.423 | −0.4pp |
| tier=LOW | 79 | 0.418 | 0.430 | −1.3pp |
| dark_pool_accumulation / UP | 16 | 0.438 | 0.500 | −6.2pp |
| bearish_flow / DOWN | 57 | 0.544 | 0.667 | −12.3pp |
| UP / short | 92 | 0.402 | 0.533 | −13.0pp |
| bearish_flow | 106 | 0.500 | 0.632 | −13.2pp |
| DOWN / short | 71 | 0.535 | 0.676 | −14.1pp |
| bearish_flow / UP | 49 | 0.449 | 0.592 | −14.3pp |
| pullback / short | 44 | 0.432 | 0.659 | −22.7pp |
| gamma_breakout | 8 | 0.250 | 0.500 | −25.0pp |
| choppy / short | 30 | 0.233 | 0.500 | −26.7pp |
| uptrend / short | 50 | 0.480 | **0.800** | −32.0pp |

Read the bottom of that table the C49 way: `uptrend / short` at −32.0pp is **not** a
finding that the short book collapses in an uptrend — its book WR is 0.480, above the
system average. It is a finding that SPY-short resolved at 0.800 in those windows. The
book barely moved; the denominator did.

## Standing conclusion

C49 holds on an independent window. Raw benchmark-excess stays demoted: annotated
secondary column, never a headline, never above P2 on its own. The paired McNemar in
Phase 3 §3.4 is where edge claims are decided — and it is precisely because McNemar is
row-matched that the long-book and short-book results survive this correction.

Output: `phase_3d_excess_artifact.jsonl`.
