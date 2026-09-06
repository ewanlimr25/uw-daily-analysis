# Phase 4 — Tool Attribution · 2026-06-20

**Provenance:** verbatim envelope `score_components[].source_tool` (canonicalized — CLI form `uw historical cumulative-premium-flow` and legacy underscore form `historical_cumulative_premium_flow` are merged; compound " / " citations split). Marginal contribution = class-conditional `wr_with − wr_without` within `canonical_class`, weighted by in-class support. Tools cited <5× = INSUFFICIENT_N. BH FDR 0.10 across the 13 scored tools.

**Headline discipline: NO tool survives Benjamini-Hochberg.** The lowest raw p-values are 0.016 (`front_end_iv_ratio`) and 0.018 (`term_skew`); BH requires the smallest of 13 tests to clear ~0.008. **Every tier label below is structural/qualitative, not statistically established** — identical to the 2026-05-30 finding that tool tiers are method-unstable and zero survive BH. None can drive a tier *change* above P2.

## Tool tier table (marginal contribution, structural)

| tool | n | marg pp | with | w/o | ubiq | p | tier |
|---|--:|--:|--:|--:|--:|--:|---|
| screener_earnings_catalyst | 7 | +28.6 | .57 | .44 | .04 | .49 | load-bearing *(prov)* |
| options_structure_iv_term_structure | 5 | +23.4 | .60 | .44 | .03 | .48 | load-bearing *(prov)* |
| **dark_pool_block_stratified** | 17 | **+18.0** | .53 | .43 | .11 | .45 | **LOAD-BEARING** |
| options_structure_dex | 37 | +13.1 | .43 | .45 | .23 | .87 | LOAD-BEARING |
| historical_cumulative_premium_flow | 105 | +8.8 | .46 | .42 | **.66** | .64 | **UBIQUITY_CONFOUNDED** |
| insights_signal_confluence | 49 | +6.6 | .45 | .44 | .31 | .93 | SUPPORTIVE |
| options_flow_sector_flow_persistence | 26 | +3.2 | .50 | .43 | .16 | .53 | SUPPORTIVE |
| insights_institutional_accumulation | 22 | −2.4 | .50 | .43 | .14 | .57 | ~NO-INFO |
| hot_chains_multileg | 25 | −5.2 | .32 | .47 | .16 | .18 | NEGATIVE |
| insights_earnings_play | 9 | −7.3 | .33 | .45 | .06 | .49 | NEGATIVE |
| historical_oi_trend | 59 | −14.1 | .44 | .45 | .37 | .95 | NEGATIVE |
| **options_structure_term_skew** | 14 | **−34.6** | .14 | .47 | .09 | .018 | NEGATIVE |
| **options_structure_front_end_iv_ratio** | 7 | **−50.0** | .00 | .46 | .04 | .016 | NEGATIVE *(prov)* |

## Desk read (market-maker quant)

- **`dark_pool_block_stratified` is the one credible load-bearer (+18pp, n=17).** It fires the institutional/retail filter that raw DP summary lacks, and this is the *third* audit to put it positive on real directional outcomes (05-30 +, 06-06 +). Even BH-null, it is the most trustworthy tool in the kit — it earns its "required citation" status for `dark_pool_accumulation`. P2-confirm, not a change.
- **`cumulative-premium-flow` is the base-rate citation, not a dead tool.** At n=105 / ubiquity 0.66 it is cited on two-thirds of every tooled row; `with ≈ without` is mechanical, not evidence of no signal (C32 ubiquity confound). Do **not** read its NO-INFO-ish +8.8 as "deprecate." The honest fix is to stop citing it reflexively so it *can* be measured — a measurement-hygiene item, not a tool demotion.
- **The vol-structure tools are the strongest negatives — but on RV-proxy outcomes.** `term_skew` (−34.6, with-WR 0.14) and `front_end_iv_ratio` (−50.0, with-WR 0.00) fire on exactly the `earnings_vol`/`high_iv_rank` rows that Phase 3 found wildly overconfident (claimed 0.84–0.86, realised 0.38). The tools aren't "wrong" — they're correctly tagging the vol classes whose **claimed win-rates are substrate-fabricated** and whose outcomes here are RV-direction-proxy, not true IV-vs-RV. So this is a *claim/substrate* problem surfacing through the tool lens, not a "rip out term_skew" problem. Structural only; RV-proxy-contaminated; cannot exceed P2.
- **`historical_oi_trend` reads −14.1pp (n=59)** — a core accumulation tool landing negative is worth a flag, but it is ubiquity-adjacent (0.37), BH-null, and cited across both accumulation winners and losers. Watch, don't cut.

## `fz` advisory — C15–C18 promotion gates (all remain advisory, 0 points)

| Criterion | Result | Verdict |
|---|---|---|
| **C15** squeeze (short-thesis high-SI) | **0** high-SI shorts in the set (every short is `squeeze_pressure=LOW`; dist: LOW 47, MODERATE 2) | **INSUFFICIENT_N — no promotion** |
| **C16** float-normalized block | per-call DP-block/float ratio not carried in `calls[]` | **NA — data not in envelope** |
| **C17** flow-vs-analyst divergence | n=7 divergent, WR **0.71** — *wrong sign* vs the "downside-only" hypothesis, and n<robust floor | **NO-GO** (divergent names *won*; thesis unsupported) |
| **C18** insider clusters | insider-cluster flag not carried in `calls[]` | **NA — data not in envelope** |
| breadth divergence | 50/143 decided carried a divergence flag | advisory; structural only |

No `fz` criterion clears its threshold — all stay Phase-A advisory at 0 rubric points, consistent with every prior audit. C16/C18 cannot even be tested until the envelope carries the per-call float-block ratio and insider-cluster flag (a schema-additive pre-registration candidate, not a promotion).

## Output
- `phase_4_tools.jsonl` — per-tool numerics (marginal contribution, class contributions, winner/loser fractions, ubiquity, BH) + fz advisory block.
