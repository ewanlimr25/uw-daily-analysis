# Phase 4 — Tool Attribution (2026-07-25)

Provenance: **verbatim** — every citation read from `score_components[].source_tool`.
N ≥ 5 floor; Benjamini-Hochberg FDR 0.10 across the tool set.

## Tool table

| tool | n | marginal | WR with | WR w/o | ubiquity | p | BH | tier |
|---|---|---|---|---|---|---|---|---|
| `screener bullish-bearish` | 5 | +45.0 | 0.60 | 0.42 | 0.01 | 0.426 | n | load-bearing *(prov)* |
| `options-structure gex` | 8 | +14.6 | 0.38 | 0.43 | 0.02 | 0.773 | n | LOAD-BEARING |
| `insights institutional-accumulation` | 32 | +9.5 | 0.44 | 0.42 | 0.07 | 0.882 | n | SUPPORTIVE |
| `historical cumulative-premium-flow` | 233 | +7.3 | 0.44 | 0.41 | **0.53** | 0.442 | n | SUPPORTIVE ⚠ubiquity |
| `insights signal-confluence` | 50 | +4.0 | 0.44 | 0.42 | 0.11 | 0.820 | n | SUPPORTIVE |
| `options-structure term-skew` | 58 | +3.4 | 0.43 | 0.42 | 0.13 | 0.921 | n | SUPPORTIVE |
| `hot-chains multileg` | 67 | +2.0 | 0.40 | 0.43 | 0.15 | 0.692 | n | NO-INFO |
| `dark-pool block-stratified` | 26 | +1.6 | 0.42 | 0.42 | 0.06 | 0.984 | n | NO-INFO |
| `screener earnings-catalyst` | 7 | −0.8 | 0.43 | 0.42 | 0.02 | 0.985 | n | no-info *(prov)* |
| `options-flow sector-flow-persistence` | 50 | −3.7 | 0.34 | 0.44 | 0.11 | 0.197 | n | NEGATIVE |
| `historical oi-trend` | 101 | −3.9 | 0.42 | 0.43 | 0.23 | 0.832 | n | NEGATIVE |
| `options-structure iv-term-structure` | 18 | −8.5 | 0.39 | 0.43 | 0.04 | 0.752 | n | NEGATIVE |
| `options-structure front-end-iv-ratio` | 17 | −8.6 | 0.35 | 0.43 | 0.04 | 0.540 | n | NEGATIVE |
| `options-structure dex` | 53 | −9.6 | 0.41 | 0.43 | 0.12 | 0.876 | n | NEGATIVE |
| `insights earnings-play` | 11 | −15.7 | 0.36 | 0.43 | 0.03 | 0.677 | n | NEGATIVE |

28 further tools cited < 5 times → INSUFFICIENT_N, excluded from tier ranking.

## The finding: **8th consecutive BH-null tool table**

**Not one tool survives multiple-hypothesis correction.** No p-value is below 0.197.
This is the eighth straight audit with that result, and Phase 3d now supplies the
mechanism: these marginals are class-outcome noise re-attributed per window, and the
window's benchmark is what moves.

The sign instability is again total:

| tool | 2026-07-11 | 2026-07-18 | 2026-07-25 |
|---|---|---|---|
| `insights institutional-accumulation` | −22.2pp | +18.2pp | +9.5pp |
| `dark-pool block-stratified` | +15.9pp | −2.3pp | +1.6pp |
| `options-structure front-end-iv-ratio` | — | −21.3pp | −8.6pp |

The 2026-07-11 pre-registration "isolate `block-stratified` as the load-bearing
accumulation gate" was refuted at 07-18 and stays refuted: +1.6pp on n=26, WR-with
0.42 vs WR-without 0.42 — a *perfectly* uninformative gate.

## Ubiquity confound

`historical cumulative-premium-flow` is cited on **53% of all rows**. Its +7.3pp reads
SUPPORTIVE but is structurally unreliable — `with` ≈ the base rate by construction. Do
not read this as evidence the tool works; read it as the tool being the default
citation. Flagged `ubiquity_confounded`, as in every prior audit.

## The one stable negative

`options-structure front-end-iv-ratio` has been negative in both audits that measured
it (−21.3pp, −8.6pp) and it is the tool behind the **panic gate**. This remains a
structural/qualitative concern rather than an act-now finding: n=17, BH-null, and the
gate it feeds grades *effective* in Phase 6 (fired 0.410 vs not-fired 0.562). A gate
that correctly identifies bad trades will show a negative marginal — that is the gate
working, not failing. Do not demote it on this evidence.

## `fz` advisory lanes (C15–C18 promotion gates)

| criterion | result | verdict |
|---|---|---|
| **C15** squeeze / short-interest on SHORT theses | 18 short rows carry `fz_context`; **0** clear the high-SI threshold (`short_float ≥20% ∧ dtc ≥5`) | **INSUFFICIENT_N — no promotion** |
| **C16** float-normalized DP block | per-call block/float ratio not carried in the envelope | **NA — cannot test** |
| **C17** flow-vs-analyst divergence | n=14 divergent, WR 0.571 | scored, **below N≥5-per-arm reliability; no promotion** |
| **C18** insider clusters | flag not carried in `calls[]` | **NA — cannot test** |
| breadth divergence | flag on 130 / 423 rows | advisory, structural only |

`squeeze_pressure` distribution: LOW 91, unknown 36, MODERATE 6 — the universe the
fleet trades simply does not contain high-short-interest names, so **C15 is untestable
by construction on mega-cap flow, not merely under-powered.** Recommend re-scoping C15
rather than continuing to accrue toward a threshold this universe cannot reach.

**All four `fz` criteria stay advisory (0 rubric points).** Three consecutive audits
have now failed to test C16 and C18 because the envelope does not carry the fields —
that is a schema gap, filed in Phase 7.

Outputs: `phase_4_tools.jsonl`.
