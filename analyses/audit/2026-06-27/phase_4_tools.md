# Phase 4 — Tool Attribution (2026-06-27)

Provenance: **verbatim** (`score_components[].source_tool`). Class-controlled marginal contribution
(`winrate_with − winrate_without` within `canonical_class`, weighted by class-N). N≥5 floor; BH FDR
0.10 across scored tools; ubiquity-confound flag at >60% of rows. Voice: market-maker quant.

## Tool tier list

| tool | n | marg pp | with | w/o | ubq | p | BH | tier |
|---|---|---|---|---|---|---|---|---|
| screener_earnings_catalyst | 6 | +15.2 | 0.50 | 0.47 | 0.03 | 0.874 | n | load-bearing *(prov)* |
| **insights_institutional_accumulation** | 23 | **+13.6** | 0.52 | 0.46 | 0.11 | 0.586 | n | **LOAD-BEARING** |
| options_structure_iv_term_structure | 6 | +10.3 | 0.50 | 0.47 | 0.03 | 0.874 | n | load-bearing *(prov)* |
| historical_cumulative_premium_flow | 120 | +7.8 | 0.50 | 0.42 | 0.58 | 0.280 | n | SUPPORTIVE |
| dark_pool_block_stratified | 20 | +7.7 | 0.50 | 0.47 | 0.10 | 0.765 | n | SUPPORTIVE |
| insights_signal_confluence | 50 | +2.1 | 0.44 | 0.48 | 0.24 | 0.645 | n | SUPPORTIVE |
| insights_earnings_play | 11 | −3.0 | 0.36 | 0.47 | 0.05 | 0.475 | n | NEGATIVE |
| options_flow_sector_flow_persistence | 30 | −3.4 | 0.47 | 0.47 | 0.15 | 0.985 | n | NEGATIVE |
| options_structure_gex | 6 | −4.5 | 0.50 | 0.47 | 0.03 | 0.874 | n | negative *(prov)* |
| historical_oi_trend | 62 | −8.9 | 0.45 | 0.48 | 0.30 | 0.753 | n | NEGATIVE |
| hot_chains_multileg | 31 | −12.7 | 0.39 | 0.48 | 0.15 | 0.325 | n | NEGATIVE |
| options_structure_term_skew | 20 | −18.8 | 0.25 | 0.49 | 0.10 | 0.039 | n | NEGATIVE |
| options_structure_dex | 39 | −19.8 | 0.46 | 0.47 | 0.19 | 0.925 | n | NEGATIVE |
| options_structure_front_end_iv_ratio | 11 | −23.1 | 0.18 | 0.48 | 0.05 | 0.050 | n | NEGATIVE |

(14 more tools INSUFFICIENT_N at <5 cites — excluded from ranking.)

## The governing fact: no tool survives BH — for the 4th audit running

Every tier label is **structural / qualitative.** Not one tool's `with−without` clears Benjamini-
Hochberg at FDR 0.10 across the ~14-test sweep (closest: `term_skew` p=0.039, `front_end_iv_ratio`
p=0.050 — both *negative*, and neither survives BH adjustment). **No tool-tier finding can drive a
Phase-7 change above structural commentary.** Tool tiers are method-unstable here because the dataset
is single-engine (UW flow) and the per-class cells are small; this is a known, repeated limitation, not
a new discovery.

## What the structure still says (read as colour, not as a gate change)

1. **`insights_institutional_accumulation` is the most robust positive (+13.6pp, n=23, not
   provisional).** It is the real-time institutional/retail filter — and it is the tool behind
   `dark_pool_accumulation`'s +9.1pp excess (Phase 3). If any tool earns "keep citing," it's this one.
   `dark_pool_block_stratified` (+7.7pp) is its supporting gate. The accumulation lane's edge is tool-
   coherent.

2. **`historical_cumulative_premium_flow` is ubiquity-adjacent (0.58, just under the 0.60 flag) — read
   its +7.8pp with suspicion of base-rate, not as clean signal.** Cited on 120 rows (58% of decided);
   `with ≈ without` is mechanically muted because it *is* the base citation. It reads SUPPORTIVE here
   but the honest label is "measurement-confounded, probably load-bearing." Do not demote on this
   number — the fix is hygiene (stop citing it reflexively), not removal.

3. **The vol-structure tools are the strongest negatives — and they are faithfully tagging, not
   malfunctioning.** `front_end_iv_ratio` −23.1pp, `dex` −19.8pp, `term_skew` −18.8pp. These fire on
   exactly the `earnings_vol` / `high_iv_rank` substrate that realised 0.37 (Phase 3) — so they look
   "negative" because they are correctly present on the losing vol trades. They are RV-proxy-
   contaminated symptoms, not broken instruments. **Do not investigate them as misinterpreted tools;
   investigate the ≥0.80 vol quote they sit next to.**

## fz advisory (C15–C18 promotion gates — all still advisory)

- **C15 squeeze (short-thesis high-SI):** INSUFFICIENT_N — 0 of 13 fz-tagged shorts cleared the
  short_float≥20 ∧ dtc≥5 bar. squeeze_pressure dist = LOW 59 / MODERATE 2 / unknown 9. No promotion.
- **C17 flow-vs-analyst divergence:** n=10 divergent, WR 0.70 — *directionally encouraging* (flow that
  disagrees with analysts won 70%) but n<<floor for BH. Stays advisory; **do not promote** (0 rubric
  points), re-test next audit.
- **C16 float-normalized block / C18 insider clusters:** NA — the per-call DP-block/float ratio and
  insider-cluster flag are not carried in `calls[]`. Promotion blocked on *envelope schema*, not on
  evidence. (If C16/C18 are to be gradeable, the envelope must emit those fields — a schema pre-reg,
  not a rubric change.)
- **breadth_cross_check:** 50/188 rows flagged divergence; advisory/structural only.

**Verdict:** the tool layer has nothing actionable — no BH survivor, single-engine instability for the
4th time. The one durable structural read is that the **accumulation toolchain
(`institutional_accumulation` + `block_stratified`) is coherent with the only positive-excess long
classes**, and the **vol-structure tools are honest messengers of a bad vol substrate.** Keep both
reads as colour; change no gate on tool evidence this run.

**Output:** `phase_4_tools.jsonl`.
