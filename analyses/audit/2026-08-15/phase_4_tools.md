# Phase 4 — Tool Attribution (2026-08-15)

## Provenance basis (C23)

**569 / 672 rows (84.7%) carry verbatim `score_components[].source_tool` read directly from
the decision envelope. Zero rows used prose-reconstructed citations.** The C23
reconstructed-citation priority cap therefore does **not** bind this cycle; the remaining P0
constraints (cross-regime, BH-surviving, decided-N) still do — and they bind hard, see below.

1,225 citation instances across 572 decided rows.

## Headline: the 11th consecutive BH-null tool table

**Zero tools survive Benjamini-Hochberg at FDR 0.10 across 29 simultaneous tests.** The
smallest p in the entire sweep is **0.077**, on `iv-term-structure hygiene` at **n = 6**.

Eleven audit windows, spanning every regime this system has observed (uptrend, pullback,
choppy, transitional), ~20–30 tests each, and **no `uw` CLI tool has ever survived multiple-
hypothesis correction as an outcome discriminator.** At n = 572 decided rows this is no
longer an underpowered question. The rubric's founding premise — that more corroborating tool
citations raise conviction — has been tested to exhaustion and is not supported.

## Atomic tool table (n ≥ 5, class-conditional marginal contribution)

Citation strings are **atomized** this cycle (see data-quality note below): `"uw a + uw b"` is
credited to both `a` and `b` rather than to a distinct label `"a_+_b"`. This is the correct
denominator and recovers 155 citation instances that were previously trapped in n < 5 labels.

| tool | n | marginal | WR with | WR w/o | ubiquity | p | BH | tier |
|---|---|---|---|---|---|---|---|---|
| `screener bullish-bearish` | 5 | +36.5pp | 0.60 | 0.41 | 0.01 | 0.679 | n | load-bearing *(prov)* |
| `scripts/term_structure_hygiene.py` | 9 | +34.1pp | 0.67 | 0.41 | 0.02 | 0.223 | n | LOAD-BEARING |
| `risk market-regime` | 5 | +29.1pp | 0.60 | 0.41 | 0.01 | 0.679 | n | load-bearing *(prov)* |
| `options-structure gex` | 8 | +21.7pp | 0.38 | 0.41 | 0.01 | 1.000 | n | LOAD-BEARING |
| `oi decrease-with-volume` | 5 | +21.7pp | 0.60 | 0.41 | 0.01 | 0.679 | n | load-bearing *(prov)* |
| `scripts/dex_flip.py` | 6 | +19.4pp | 0.50 | 0.41 | 0.01 | 0.967 | n | load-bearing *(prov)* |
| `dark-pool block-stratified + insights inst-accum` | 5 | +18.3pp | 0.60 | 0.41 | 0.01 | 0.679 | n | load-bearing *(prov)* |
| `historical cumulative_premium_flow` (dated variant) | 10 | +14.3pp | 0.60 | 0.41 | 0.02 | 0.371 | n | LOAD-BEARING |
| `insights institutional-accumulation` | 37 | +7.7pp | 0.49 | 0.41 | 0.06 | 0.429 | n | SUPPORTIVE |
| `historical vrp` | 8 | +7.6pp | 0.50 | 0.41 | 0.01 | 0.873 | n | SUPPORTIVE |
| `historical iv-percentile-zscore` | 13 | +6.7pp | 0.46 | 0.41 | 0.02 | 0.930 | n | SUPPORTIVE |
| `options-structure front-end-iv-ratio` (short form) | 5 | +6.5pp | 0.40 | 0.41 | 0.01 | 1.000 | n | supportive *(prov)* |
| **`historical cumulative-premium-flow`** | **304** | +5.5pp | 0.43 | 0.40 | **0.53** | 0.341 | n | SUPPORTIVE |
| **`dark-pool block-stratified`** | 29 | **+3.0pp** | 0.45 | 0.41 | 0.05 | 0.832 | n | SUPPORTIVE |
| `options-structure iv-term-structure` | 43 | −1.1pp | 0.40 | 0.42 | 0.08 | 0.913 | n | NO-INFO |
| `insights signal-confluence` | 46 | −2.8pp | 0.39 | 0.42 | 0.08 | 0.852 | n | NO-INFO |
| `historical oi-trend` | 169 | −2.9pp | 0.42 | 0.41 | 0.30 | 0.886 | n | NO-INFO |
| `screener earnings-catalyst` | 11 | −4.3pp | 0.36 | 0.42 | 0.02 | 0.981 | n | NO-INFO |
| `hot-chains multileg` | 86 | −4.3pp | 0.37 | 0.42 | 0.15 | 0.411 | n | NO-INFO |
| `options-structure term-skew` | 71 | −7.2pp | 0.35 | 0.42 | 0.12 | 0.274 | n | NEGATIVE |
| `options-flow sector-flow-persistence` | 80 | −7.3pp | 0.36 | 0.42 | 0.14 | 0.328 | n | NEGATIVE |
| `options-structure front-end-iv-ratio` | 26 | −7.3pp | 0.35 | 0.42 | 0.05 | 0.596 | n | NEGATIVE |
| **`options-structure dex`** | 61 | **−9.4pp** | 0.43 | 0.41 | 0.11 | 0.929 | n | NEGATIVE |
| `insights earnings-play` | 7 | −15.0pp | 0.29 | 0.42 | 0.01 | 0.771 | n | negative *(prov)* |
| `term-skew` (short form) | 5 | −16.4pp | 0.20 | 0.42 | 0.01 | 0.619 | n | negative *(prov)* |
| `iv-term-structure hygiene` | 6 | −39.7pp | 0.00 | 0.42 | 0.01 | **0.077** | n | negative *(prov)* |
| `hot-chains sweep-persistence` | 5 | −49.9pp | 0.00 | 0.42 | 0.01 | 0.134 | n | negative *(prov)* |

Lower-case tiers are `THIN_N` (n 5–7) and **provisional** — never the sole basis for a Phase-7
recommendation (C23).

## Desk commentary

**`historical cumulative-premium-flow` (n=304, ubiquity 0.53) — SUPPORTIVE, but read the
ubiquity column.** It is cited on **53% of decided rows**, right under the 60%
`ubiquity_confounded` threshold. At that saturation `with` ≈ `without` by construction: its
+5.5pp is measured against a "without" pile that is itself half the book. This is not evidence
the tool is dead; it is evidence the tool is the base-rate citation. Do not deprecate it on
this number — but equally, do not credit the +5.5pp as edge.

**`dark-pool block-stratified` — the six-cycle collapse completes: +15.9 → −2.3 → +1.6 →
+1.8 → +2.1 → +3.0pp.** WR-with 0.45 against WR-without 0.41 on n=29. Market-maker read: *"the
institutional/retail filter is doing exactly what it says on the tin — it splits the tape into
block prints and everything else — and both piles then win at the same rate. It's a clean
classifier of trade type and a null classifier of outcome. Keep it (it is structurally the
only retail filter in the stack), grant it no ranking weight."* Note the C34 caveat still
stands: the top `dark-pool price-levels` bucket is the closing cross on every liquid name, so
premium-ranked DP reads remain ~2× inflated.

**`options-structure dex` — NEGATIVE at −9.4pp on n=61, and this is its third negative
reading.** Its mechanized wrapper `scripts/dex_flip.py` reads **+19.4pp on n=6** (provisional,
p=0.967). Those two facts together are the interesting part: the mechanized, sign-flip-gated
path is not obviously worse than the raw tool, which is what the 2026-06-12 mechanization was
supposed to achieve. But n=6 is n=6 — this is a *watch*, not a finding.

**`options-flow sector-flow-persistence` — NEGATIVE at −7.3pp on n=80,** and it feeds the
worst realised class in the book (`sector_rotation`, 0.282 on n=39, Phase 3). This is
consistent with the standing structural finding that the tool measures **gross turnover, not
netted direction** — it fired INFLOW/1.0 on 11-of-11 sectors on 2026-08-14. A sign-agnostic
turnover metric cannot express direction, and a −7.3pp marginal is what that looks like when
you score it as if it could.

**`insights signal-confluence` — NO-INFO at −2.8pp on n=46.** The tool the rubric is named
after does not discriminate outcomes. Consistent with the 2026-06-12 collapse to funnel-only.

**`hot-chains sweep-persistence` (0-for-5) and `iv-term-structure hygiene` (0-for-6)** are the
two largest negative readings and the smallest p-values in the sweep — and both are n≤6. They
are flagged for accrual, nothing more. Note the tension with `scripts/term_structure_hygiene.py`
at **+34.1pp on n=9**: the same hygiene concept reads +34 under one citation label and −40
under another. That is a labelling artifact, not two opposing effects — see below.

## Data-quality finding: citation-label fragmentation

**122 distinct raw citation strings across 1,225 instances; 60 of them appear exactly once;
52 contain a `+` concatenation.** Agents are writing `source_tool` as free text —
`"uw options-structure iv-term-structure + uw options-structure term-skew + scripts/term_structure_hygiene.py"`
is a single label with n=2, while its three constituent tools each have real N elsewhere.
Nineteen rows have *every* citation concatenated.

Consequences, all live:
1. **155 citation instances were trapped in n<5 labels** and excluded from tiering under the
   raw parse. Atomizing recovers them and lifts the testable tool count from 23 → 29.
2. The same tool appears under multiple labels with **opposite** tiers
   (`scripts/term_structure_hygiene.py` +34.1 vs `iv-term-structure hygiene` −39.7;
   `insights earnings play` −10.0 vs `insights earnings-play` −15.0;
   `options-structure front-end-iv-ratio` −7.3 vs `front-end-iv-ratio` +6.5). No tool tier
   built on the raw labels is trustworthy.
3. This is a **measurement defect in the audit substrate, not in the tools** — and it has
   been silently degrading Phase 4 for eleven cycles.

→ Phase 7 recommendation: constrain `score_components[].source_tool` to a single canonical
tool identifier, one component per tool.

## `fz` advisory lanes (C15–C18 promotion gates)

| criterion | status | evidence |
|---|---|---|
| **C15** squeeze / short-interest | **INSUFFICIENT_N — and structurally starved** | 20 short-thesis rows carry `fz` context; **`n_hi_si` = 0**. Squeeze-pressure distribution is `LOW` 106 / `MODERATE` 11 / `unknown` 50 — **zero `HIGH` observations in 167 populated rows.** The gate's own trigger condition (`short_float ≥ 20% ∧ dtc ≥ 5`) has never once been met. |
| **C16** float-normalized DP block | **NA — cannot be computed** | per-call DP-block/float ratio is not emitted into the envelope. Starved, not refuted. |
| **C17** flow-vs-analyst divergence | **scored** | n=14 divergent rows, WR 0.571 vs book 0.414. Directionally supportive, **below the N≥5-per-arm-plus-BH bar**. Keep advisory. |
| **C18** insider clusters | **NA — field not carried** | `insider_cluster_flag` is absent from the envelope `calls[]` entirely and absent from the gate-verdict key union. Last cycle's finding stands: 15 prior observations, all `False`. Zero variance cannot gate a conjunction at any n. |
| breadth cross-check | advisory / structural | flag present on 177 of 555 rows. No outcome test at this N. |

**No `fz` criterion clears its promotion threshold. All remain advisory at 0 rubric points**,
as they have for every cycle since registration. C15 and C18 are now distinguishable from
"awaiting data": C15's trigger has never fired in 167 observations and C18's field is not
emitted at all. Both are candidates for **retirement rather than continued accrual** — a
criterion that cannot fire is not pending, it is dead.

**Output:** `phase_4_tools.jsonl` (raw-label pass) · `phase_4_tools_atomic.jsonl` (atomized
pass, canonical for this cycle's tiers).
