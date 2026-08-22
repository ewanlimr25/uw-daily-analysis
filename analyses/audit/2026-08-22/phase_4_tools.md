# Phase 4 — Tool Attribution (2026-08-22)

## Provenance basis (C23) — and the first cycle where the table is measurable

**100% verbatim envelope citations** (`score_components[].source_tool`); zero prose
reconstruction. But verbatim ≠ measurable, which is what the 2026-08-15 audit found and fixed.

| | distinct labels | instances | trapped in n<5 labels |
|---|---|---|---|
| 2026-08-15 raw-string table | **122** | 1,225 | 155 (**12.7%**) |
| **this cycle, atomized** (`phase4_atomic.py`) | **43** | 1,353 | 33 (**2.4%**) |

`phase4_atomic.py` splits concatenated citations on `+ , / and via over`, strips per-call
argument suffixes (`--symbol X`, `--days N`, `--date …`), and maps 60+ spellings onto canonical
`uw <group> <sub>` / `scripts/*.py` ids. **24 tools now clear the N ≥ 5 floor** and the
fragmented-denominator caveat that qualified eleven consecutive tool tables is largely retired.

The raw-string table (`phase_4_tools.jsonl`) is retained for continuity; **the atomic table
below is authoritative** (`phase_4_tools_atomic.jsonl`).

## Tool tier table — atomic, class-conditional, BH FDR 0.10

Base book WR = **0.402** on n = 637 decided.

| tool | n | marg (pp) | WR with | WR w/o | ubiquity | p | BH | tier |
|---|---|---|---|---|---|---|---|---|
| `uw screener bullish-bearish` | 5 | +34.4 | 0.60 | 0.40 | 0.01 | 0.396 | n | load-bearing *(prov)* |
| `uw oi decrease-with-volume` | 5 | +21.7 | 0.60 | 0.40 | 0.01 | 0.396 | n | load-bearing *(prov)* |
| `uw insights institutional-accumulation` | 48 | **+9.5** | 0.46 | 0.40 | 0.08 | 0.381 | n | SUPPORTIVE |
| `uw options-structure gex` | 10 | +9.0 | 0.30 | 0.40 | 0.02 | 0.749 | n | SUPPORTIVE |
| `uw oi biggest-increases` | 6 | +8.9 | 0.50 | 0.40 | 0.01 | 0.689 | n | supportive *(prov)* |
| **`uw dark-pool block-stratified`** | **37** | **+7.8** | 0.46 | 0.40 | 0.06 | 0.503 | n | SUPPORTIVE |
| `uw historical vrp` | 11 | +7.2 | 0.45 | 0.40 | 0.02 | 0.764 | n | SUPPORTIVE |
| `uw risk market-regime` | 15 | +6.4 | 0.40 | 0.40 | 0.02 | 1.000 | n | SUPPORTIVE |
| `scripts/dex_flip.py` | 18 | +6.4 | 0.44 | 0.40 | 0.03 | 0.811 | n | SUPPORTIVE |
| `uw historical cumulative-premium-flow` | **346** | +4.8 | 0.42 | 0.37 | **0.54** | 0.059 | n | SUPPORTIVE ⚠️ ubiquity |
| `uw insights signal-confluence` | 50 | +4.4 | 0.44 | 0.40 | 0.08 | 0.566 | n | SUPPORTIVE |
| `uw hot-chains multileg` | 100 | +2.5 | 0.40 | 0.40 | 0.16 | 1.000 | n | SUPPORTIVE |
| `uw historical iv-percentile-zscore` | 14 | −2.4 | 0.36 | 0.40 | 0.02 | 0.792 | n | NO-INFO |
| `uw historical oi-trend` | **217** | −3.4 | 0.39 | 0.41 | 0.34 | 0.679 | n | NO-INFO |
| `uw screener earnings-catalyst` | 20 | −3.5 | 0.35 | 0.40 | 0.03 | 0.820 | n | NO-INFO |
| `uw options-structure iv-term-structure` | 64 | −4.8 | 0.36 | 0.41 | 0.10 | 0.525 | n | NO-INFO |
| **`uw options-flow sector-flow-persistence`** | 84 | **−5.0** | 0.36 | 0.41 | 0.13 | 0.375 | n | NEGATIVE |
| `uw options-structure dex` | 72 | −7.7 | 0.43 | 0.40 | 0.11 | 0.630 | n | NEGATIVE |
| `uw oi pin-risk` | 6 | −9.9 | 0.17 | 0.40 | 0.01 | 0.412 | n | negative *(prov)* |
| `uw options-structure front-end-iv-ratio` | 40 | −10.4 | 0.30 | 0.41 | 0.06 | 0.198 | n | NEGATIVE |
| `uw options-structure term-skew` | 93 | −10.5 | 0.31 | 0.42 | 0.15 | 0.045 | n | NEGATIVE |
| `uw insights earnings-play` | 12 | −11.2 | 0.33 | 0.40 | 0.02 | 0.772 | n | NEGATIVE |
| **`scripts/term_structure_hygiene.py`** | **42** | **−16.9** | **0.19** | 0.42 | 0.07 | **0.003** | **YES** | **NEGATIVE** |
| `uw hot-chains sweep-persistence` | 5 | −50.0 | 0.00 | 0.41 | 0.01 | 0.085 | n | negative *(prov)* |

## Desk commentary

**The twelve-cycle BH-null streak breaks — with one survivor, and it needs a hard look before
anyone touches it.** `scripts/term_structure_hygiene.py` reads **−16.9pp on n=42, p=0.003,
BH-surviving at FDR 0.10** — rows citing it win 19% against a 42% book. Three reasons this is a
**pre-registration and not an action**:

1. **Recency concentration.** 36 of its 42 rows are **August 2026**, and the August book is the
   weakest month in the corpus (0.318, n=107, vs 0.401 July / 0.410 June). The script was
   mechanized 2026-07-25 and adoption ramped after.
2. **Sign reversal under re-normalization.** The same script read **+34.1pp (n=9)** in the
   2026-08-15 atomic view and **−39.7pp** under its other spelling in the same table. This
   cycle's number is the first computed on a *unified* denominator — which is the point of the
   P1 #1 fix, but it also means there is exactly **one** clean measurement of it.
3. **A hygiene script cannot itself be wrong about direction.** It re-derives the IV term
   structure after dropping 0DTE and thin tenors — i.e. it *corrects* a label. A negative
   marginal contribution most plausibly says the fleet **acts too eagerly on the corrected
   label**, not that the correction is bad.

The within-cohort controls do survive, which is why it is worth registering rather than
dismissing: **within August alone**, hygiene rows read 0.194 (n=36) vs 0.380 (n=71); **within
August vol rows alone**, 0.174 (n=23) vs 0.348 (n=23). Direction cut: `vol_short` with-hygiene
**0.071 (n=14)** vs 0.352 without (n=108).

*"`uw dark-pool block-stratified` climbs back to SUPPORTIVE (+7.8pp, n=37) once you stop
splitting its citations five ways — the six-cycle 'collapse' to +2–3pp was partly a denominator
artifact, and the honest read is that it has been a modest, stable filter all along, never the
+18pp load-bearer the 2026-05 table claimed."*

*"`uw historical cumulative-premium-flow` is cited on 54% of decided rows. It reads +4.8pp with
the lowest p in the SUPPORTIVE band (0.059) — but at that ubiquity `with` ≈ `without` by
construction. Flag `ubiquity_confounded`; do not read it as dead, and do not read it as proven."*

*"`uw options-flow sector-flow-persistence` reads −5.0pp on n=84 and feeds `sector_rotation`,
the worst class in the book (0.29, n=48, BH). Third consecutive cycle of the same pairing. This
is exactly what scoring a **gross-turnover** metric as if it carried direction looks like —
C55 already forced direction onto the netted `market-regime.sector_rotation`; the persistence
metric remains a durability filter and the data keeps saying it is not more than that."*

*"The whole vol-surface toolchain is negative in a block: `term-skew` −10.5 (n=93),
`front-end-iv-ratio` −10.4 (n=40), `iv-term-structure` −4.8 (n=64), `hygiene` −16.9 (n=42),
`insights earnings-play` −11.2 (n=12). Vol rows realise 36.7% against a 40.2% book and
`vol_short` realises 34.0%. The tools are not independently broken — **the vol lane is**, and
these tools are its fingerprint."*

**`uw options-structure gex` at +9.0pp on n=10 is not a promotion signal** — its `WR with` is
0.30, *below* the 0.40 book. The positive marginal contribution comes entirely from
class-conditioning against even weaker peers. Read the two columns together or you will promote
a losing tool.

## `fz` advisory lanes (C15–C18)

| criterion | status | this cycle |
|---|---|---|
| **C15** squeeze / short-interest | **RETIRED 2026-08-15** | Confirmed dead: `squeeze_pressure` = LOW 127 / MODERATE 19 / unknown 52, **zero HIGH readings on 198 populated rows**; `n_hi_si` = **0** of 22 short rows carrying `fz_context`. The trigger has never once been met. |
| **C16** float-normalized DP block | **OPEN — first sign of life in 8 cycles** | The 08-15 backfill duty **worked**: `dp_block_to_float_ratio` now populates on **10 calls (9 decided)**, all post-2026-08-03. Aggregate WR 0.222 (n=9) vs 0.397 accumulation baseline — but with **perfect rank separation**: the two largest ratios (0.0023 NBIS, 0.0022 SNDK) are the only WINs, all seven rows ≤0.00058 are LOSS (random-assignment p = 0.028). **Post-hoc threshold on n=9 — pre-registered as C62, NOT promoted.** Emission is still the blocker: 10 populated of 275 calls carrying the key, and the validator caught a fresh null on 2026-08-17 GLD. |
| **C17** flow-vs-analyst divergence | **OPEN, scored, thin** | n = 14 divergent rows, WR **0.571** vs 0.402 book (+16.9pp). Above the N≥5 floor but far below anything actionable; **not BH-tested, single-regime.** Accruing. |
| **C18** insider clusters | **RETIRED 2026-08-15** | Confirmed dead: flag not carried in `calls[]`; the 20 historical observations were `False` 20/20. |
| **breadth_cross_check** | advisory | `divergence_flag` present on 191 of 620 rows. Structural only — no outcome-linked verdict at this N. |

**No `fz` promotion is authorized this cycle.** C16 and C17 stay advisory at 0 rubric points.

## Hard-rule compliance

- **BH FDR 0.10 applied across the 24-tool set.** One survivor (`term_structure_hygiene.py`).
  Every other tier label in the table is **descriptive, not inferential**.
- Tools cited 5–7 times carry lower-case *(prov)* tiers and are **never** the sole basis for a
  Phase-7 recommendation.
- `ubiquity_confounded` flagged on `cumulative-premium-flow` (0.54) per C32.
- 19 atomic ids remain below N=5 (33 instances, 2.4%) — marked INSUFFICIENT_N, excluded from
  tier ranking.
