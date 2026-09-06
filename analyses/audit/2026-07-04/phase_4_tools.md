# Phase 4 — Tool Attribution · 2026-07-04

**Provenance: verbatim envelope on 335/335 rows** (zero prose-reconstruction) — findings are not provenance-capped. **But no tool survives Benjamini-Hochberg at FDR 0.10 — the 5th consecutive audit.** Every tier label below is therefore descriptive, not actionable: no promotion, demotion, or gate-membership change is authorized this run (best p: `front_end_iv_ratio` 0.079, `historical_cumulative_premium_flow` 0.102 — both fail BH).

## Tier table (class-controlled marginal, decided n≥5; thin-N 5–7 = provisional lower-case)

| Tool | n | Marginal | with/without | Ubiquity | Tier |
|---|---|---|---|---|---|
| hot_chains_multileg | 45 | **+26.5pp** | 0.42/0.44 | 0.17 | LOAD-BEARING† |
| historical_cumulative_premium_flow | 149 | +13.7pp | 0.48/0.38 | **0.56** | LOAD-BEARING† (base-rate flag) |
| insights_institutional_accumulation | 26 | +12.5pp | 0.46/0.44 | 0.10 | **LOAD-BEARING** |
| screener_earnings_catalyst | 7 | +9.5pp | — | 0.03 | supportive (prov) |
| options_structure_iv_term_structure | 11 | +8.3pp | 0.46/0.44 | 0.04 | SUPPORTIVE |
| insights_signal_confluence | 50 | +6.1pp | 0.44/0.44 | 0.19 | SUPPORTIVE |
| dark_pool_block_stratified | 22 | +5.8pp | 0.46/0.44 | 0.08 | SUPPORTIVE |
| options_structure_gex | 6 | +0.9pp | — | 0.02 | no-info (prov) |
| options_flow_sector_flow_persistence | 36 | +0.1pp | 0.44/0.44 | 0.14 | NO-INFO |
| insights_earnings_play | 11 | −6.5pp | 0.36/0.44 | 0.04 | NEGATIVE |
| options_structure_dex | 43 | −6.9pp | 0.42/0.44 | 0.16 | NEGATIVE |
| historical_oi_trend | 69 | −9.2pp | 0.42/0.45 | 0.26 | NEGATIVE |
| options_structure_term_skew | 24 | −10.5pp | 0.29/0.45 | 0.09 | NEGATIVE |
| options_structure_front_end_iv_ratio | 11 | **−20.9pp** | 0.18/0.45 | 0.04 | NEGATIVE |

17 further tools at n<5 = INSUFFICIENT_N (incl. `options_flow_single_leg` n=3 — C19 stays advisory by construction).

## Market-maker quant commentary

- **`hot_chains_multileg` +26.5pp is a sign whipsaw, not a discovery.** 06-20: BH-surviving *negative*; 06-27: −12.7pp; today: +26.5pp on a shifted class mix. Three audits, three signs — this is the method-instability signature the meta-audit warned about (marginal contributions on small, drifting class-conditional cells). Zero weight should move on it (C40 carry). A tool whose measured contribution oscillates ±39pp between windows is telling you about the window, not the tool.
- **`insights_institutional_accumulation` +12.5pp (n=26) — the one stable positive.** +13.6pp on 06-27, +12.5pp now, low ubiquity, fires on winners *and* losers (no confound asymmetry). Still BH-null, so it keeps its tier and earns the routing lean (Phase 7), nothing more. Paired gate `dark_pool_block_stratified` +5.8pp — consistent, boring, fine.
- **`historical_cumulative_premium_flow` +13.7pp at ubiquity 0.56** — the base-rate citation problem (C45) persists just under the 0.60 auto-flag. W27 §7 logged the mechanism in the wild: SPY's "+1 cum-flow aligned" was a window-selection artifact on a $159B two-way tape the tool itself labels MIXED. The +13.7 is inflated by being the default confirmation cite on winners. Re-measure on the low-ubiquity sub-sample per C45's bar before believing it.
- **The vol-structure desk is still the negative pocket:** `front_end_iv_ratio` −20.9, `term_skew` −10.5, and `insights_earnings_play` −6.5 — all feeding the two BH-surviving liar classes (`earnings_vol`, `high_iv_rank`). Same caveat as 06-27: these fire on an RV-proxy-resolved substrate, so they are honestly reporting a vol lane the audit cannot yet price correctly (needs `implied_move`, C43/C42(b)). Do not rip them out; do not trust them for direction either.
- **`historical_oi_trend` −9.2pp (n=69) deserves a flag:** this is the tool behind the weekly rubric's **+3 BUILDING** line — its biggest single weight — and W27 §7 caveat (4) documents `consecutive_build_days` ceiling-saturation on liquid names (Gate-1 saturates at `--days`). A +3 weight riding a −9pp tool with a known saturation artifact is Phase-5 pre-registration material (folded into C46-adjacent grading, see Phase 5 §1).
- **`options_structure_dex` −6.9pp** — C44's evidence softened (was −19.8pp) but stays negative for the third read. Register stands.

## fz advisory (C15–C18 Phase-B gates) — same tier discipline, N≥5 floor

| Item | This run | Verdict |
|---|---|---|
| **C15** squeeze-trap (short-thesis, SI≥20% ∧ DTC≥5) | 0 hi-SI shorts in dataset (squeeze_pressure: LOW 70 / MODERATE 2) | **INSUFFICIENT_N — NO-GO**, stays advisory |
| **C16** float-normalized block | per-call `dp_block_to_float_ratio` still absent from `calls[]` | **NA — enabler C43 still open** |
| **C17** flow-vs-analyst divergence | **first scored read: n=13, WR 0.615** vs short-book 0.422 (+19.3pp); all 13 are mega-cap-tech shorts vs recom ≤2.0, 2 regime buckets | **NO-GO for promotion** (n=13, single-direction, not BH-tested) — but first positive sign; keep collecting |
| **C18** insider-cluster conjunction | flag still absent from `calls[]` | **NA — enabler C43 still open** |
| breadth_cross_check | divergence flag on 69/247 decided rows | advisory/structural only |

**No `fz` criterion clears its promotion threshold. All stay Phase-A advisory, 0 rubric points.**

Machine-readable: `phase_4_tools.jsonl`.
