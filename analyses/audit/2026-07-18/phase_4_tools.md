# Phase 4 — Tool Attribution (2026-07-18)

**Provenance: verbatim** (`score_components[].source_tool`). Class-controlled marginal contribution, N≥5 floor, BH FDR 0.10, ubiquity confound flagged >0.60.

## Tool tier list (N≥5)
| Tool | N | Marg (pp) | ubq | p | BH | Tier |
|---|---|---|---|---|---|---|
| screener_bullish_bearish | 5 | +47.5 | 0.01 | 0.43 | n | load-bearing (prov, n5) |
| insights_institutional_accumulation | 32 | **+18.2** | 0.08 | 0.90 | n | LOAD-BEARING |
| options_structure_gex | 9 | +12.7 | 0.02 | 0.91 | n | load-bearing (prov) |
| hot_chains_multileg | 63 | +11.7 | 0.16 | 0.97 | n | LOAD-BEARING |
| historical_cumulative_premium_flow | 211 | +8.3 | **0.54** | 0.10 | n | SUPPORTIVE (ubiquity) |
| insights_signal_confluence | 50 | +4.7 | 0.13 | 0.84 | n | SUPPORTIVE |
| options_structure_iv_term_structure | 18 | +3.3 | 0.05 | 0.87 | n | SUPPORTIVE |
| dark_pool_block_stratified | 25 | **−2.3** | 0.06 | 0.78 | n | NEGATIVE |
| options_structure_term_skew | 42 | −4.1 | 0.11 | 0.34 | n | NEGATIVE |
| historical_oi_trend | 97 | −5.1 | 0.25 | 0.58 | n | NEGATIVE |
| options_structure_dex | 49 | −7.1 | 0.12 | 0.73 | n | NEGATIVE |
| options_flow_sector_flow_persistence | 47 | −7.5 | 0.12 | 0.20 | n | NEGATIVE |
| insights_earnings_play | 11 | −9.8 | 0.03 | 0.67 | n | NEGATIVE |
| options_structure_front_end_iv_ratio | 15 | **−21.3** | 0.04 | 0.07 | n | NEGATIVE |

## The finding: tool marginal-contribution signs are non-stationary (7th straight BH-null)
**Nothing survives Benjamini-Hochberg** — the 7th consecutive audit where zero tools clear multiple-hypothesis correction. And the *signs flip window-to-window*:

| Tool | 07-11 marg | 07-18 marg | Δ |
|---|---|---|---|
| `insights institutional-accumulation` | **−22.2pp** | **+18.2pp** | +40pp flip |
| `dark-pool block-stratified` | **+15.9pp** | **−2.3pp** | −18pp flip |
| `historical oi-trend` | −17.8pp | −5.1pp | attenuated |

The market-maker read: *these are not real per-tool edges reversing — they are the same class-outcome noise being re-attributed to whichever tool happens to co-cite the winners this window. On a single-regime slice with 8–30 decided per tool-class cell, the tool table is a coin-sorting exercise.* The **07-11 P2 "isolate block-stratified — does the institutional filter carry the accumulation edge?"** pre-register is **refuted this window** (block-stratified now −2.3pp). No tool-tier change is act-on-able.

## Structurally-stable reads (persist across ≥3 windows)
- `options_structure_front_end_iv_ratio` **−21.3pp** — the panic-gate tool is reliably anti-predictive; consistent with its three documented failure modes (tenor-blind / `near_dte_actual=0` / endpoint-only kink-miss). The one tool whose negative sign has held.
- `historical_cumulative_premium_flow` **ubiquity-confounded** (0.54 of all rows) — its +8.3pp reads mechanically because it is the base-rate citation, not a discriminator.
- `historical_oi_trend` negative across the last three windows (−9.2 → −17.8 → −5.1pp) — direction stable, magnitude not; C47 carries.

## `fz` advisory (C15–C18 gating) — none clear, all stay advisory
- **C15 squeeze (short lane):** 0 hi-SI shorts (`short_float≥20 ∧ dtc≥5`) → INSUFFICIENT_N. squeeze_pressure dist: LOW 90 / unknown 32 / MODERATE 6.
- **C17 flow-vs-analyst divergence:** n=14 divergent, WR 0.571 — nominally "scored" but no BH, n<20, no sign test. Stays advisory.
- **C16 float-normalized block / C18 insider clusters:** NA — the per-call ratio / insider-cluster flag is not carried in `calls[]`. Cannot gate.
- **breadth divergence:** 106/377 flagged; structural/advisory only.

**No `fz` criterion clears its promotion threshold. All remain Phase-A advisory (0 rubric points).**

Output: `phase_4_tools.jsonl`.
