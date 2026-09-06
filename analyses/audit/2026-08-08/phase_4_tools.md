# Phase 4 — Tool Attribution (2026-08-08)

## Provenance header (C23)

**Verbatim, 100%.** Every `tools_cited` value is read from `decision.json`
`score_components[].source_tool` — none reconstructed from prose. 523 of 626 rows carry at
least one citation. Under the reconstructed-citation rule this does **not** cap priority;
findings here may reach P0 if the statistics support it. They do not.

## Tool tier table (n ≥ 5; BH FDR 0.10 across the sweep)

| tool | n | marginal | WR with | WR w/o | ubiquity | p | BH | tier |
|---|---|---|---|---|---|---|---|---|
| `screener bullish-bearish` | 5 | +43.3 | 0.60 | 0.41 | 0.01 | 0.379 | n | load-bearing *(prov)* |
| `historical oi-trend --days 5` | 8 | +29.3 | 0.38 | 0.41 | 0.01 | 0.849 | n | LOAD-BEARING |
| `options-structure gex` | 9 | +15.5 | 0.33 | 0.41 | 0.02 | 0.647 | n | LOAD-BEARING |
| `insights institutional-accumulation` | 34 | +8.2 | 0.47 | 0.40 | 0.06 | 0.441 | n | SUPPORTIVE |
| `hot-chains multileg` | 80 | +7.7 | 0.41 | 0.41 | 0.15 | 0.925 | n | SUPPORTIVE |
| `historical cumulative-premium-flow` | 284 | +7.2 | 0.43 | 0.38 | **0.52** | 0.208 | n | SUPPORTIVE *(ubiquity-confounded)* |
| `insights signal-confluence` | 50 | +4.0 | 0.44 | 0.40 | 0.09 | 0.626 | n | SUPPORTIVE |
| `screener earnings-catalyst` | 7 | +3.5 | 0.43 | 0.41 | 0.01 | 0.910 | n | supportive *(prov)* |
| `dark-pool block-stratified` | 26 | +2.1 | 0.42 | 0.41 | 0.05 | 0.871 | n | SUPPORTIVE |
| `options-structure iv-term-structure` | 24 | +0.6 | 0.46 | 0.41 | 0.04 | 0.606 | n | NO-INFO |
| `options-flow sector-flow-persistence` | 60 | −0.9 | 0.37 | 0.41 | 0.11 | 0.492 | n | NO-INFO |
| `options-structure term-skew` | 66 | −1.7 | 0.38 | 0.41 | 0.12 | 0.609 | n | NO-INFO |
| `historical oi-trend` | 148 | −2.5 | 0.42 | 0.40 | 0.27 | 0.746 | n | NEGATIVE |
| `options-structure dex` | 57 | −7.3 | 0.42 | 0.41 | 0.10 | 0.829 | n | NEGATIVE |
| `sector-flow-persistence + cum-premium-flow` | 14 | −7.7 | 0.21 | 0.41 | 0.03 | 0.136 | n | NEGATIVE |
| `options-structure front-end-iv-ratio` | 22 | −9.2 | 0.32 | 0.41 | 0.04 | 0.383 | n | NEGATIVE |
| `iv-term-structure + iv-percentile-zscore` | 7 | −11.8 | 0.29 | 0.41 | 0.01 | 0.508 | n | negative *(prov)* |
| `insights earnings-play` | 12 | −19.7 | 0.33 | 0.41 | 0.02 | 0.596 | n | NEGATIVE |
| `hot-chains sweep-persistence` | 5 | −42.3 | 0.00 | 0.41 | 0.01 | 0.062 | n | negative *(prov)* |
| `options-structure dex via scripts/dex_flip.py` | 6 | −47.3 | 0.17 | 0.41 | 0.01 | 0.227 | n | negative *(prov)* |

47 further citation strings fall below the n≥5 floor and are marked INSUFFICIENT_N.

## The finding: a **10th consecutive BH-null tool table**

Not one tool in the sweep survives Benjamini-Hochberg at FDR 0.10. The smallest p-value in
the entire table is **0.062** (`hot-chains sweep-persistence`, n=5 — a THIN_N cell whose
"0.00 win rate" is five coin flips landing the same way). Ten independent windows, ~20
simultaneous tests each, and **zero tools have ever been shown to discriminate outcomes**.

The desk read: the rubric's implicit premise — that citing more corroborating tools raises
the probability a call works — has now failed to find support across ten audits and every
regime this system has seen. That is no longer an underpowered-sample story. It is a
result. **No tier movements are recommended, for a 10th cycle.**

## Per-tool commentary (market-maker quant)

**`historical cumulative-premium-flow` — ubiquity-confounded, do not read as dead.**
Cited on 284 rows, **52% of the corpus** — past the 60%-in-class threshold in several
classes. Its `with`≈`without` reading (+7.2pp, p=0.21) is arithmetic, not evidence: it *is*
the base-rate citation. It remains the fleet's most-used evidence line and the audit
cannot grade it by this method.

**`dark-pool block-stratified` — the collapse is complete and stable.** +15.9 → −2.3 → +1.6
→ +1.8 → **+2.1pp**, with WR-with 0.42 against WR-without 0.41 on n=26. A gate that splits
the book into two piles of statistically identical win rate is not a filter. The 07-11
"isolate it" pre-registration stays refuted; the tool stays in the toolkit (it is the
institutional/retail discriminator by construction, and its *absence* would let retail
prints into `dark_pool_accumulation`) but it earns no ranking and no required-citation
status.

**`options-structure dex` and `scripts/dex_flip.py` both read negative.** −7.3pp (n=57) and
−47.3pp (n=6). The mechanized DEX-flip script — added precisely to make the +1 rubric line
testable — has fired 6 times and won once. That is a watch-item feeding pre-registration
**C50** (which grades the +3 conjunction, not the +1 line), not an action; n=6 cannot
carry a recommendation and the tape-conditioned split in Phase 5 is what C50 actually needs.

**`options-flow sector-flow-persistence` reads NO-INFO (−0.9pp, n=60)** — consistent with
the C55 diagnosis that it measures gross turnover and cannot express direction. The
conjunction `sector-flow-persistence + cumulative-premium-flow` reads −7.7pp on n=14, the
worst non-thin cell in the table. Both corroborate the re-sourcing that was applied at
08-01; neither is significant.

**The three "LOAD-BEARING" rows are artifacts of the tier definition, not findings.**
`screener bullish-bearish` (+43.3pp) sits on n=5. `historical oi-trend --days 5` clears
+29.3pp marginal while its own WR-with (0.38) is *below* WR-without (0.41) — the marginal
figure is class-weighted and the class mix is doing the work. Neither survives BH; neither
is promoted. The tier labels are printed for continuity with prior audits and should not
be read as recommendations.

## `fz` advisory lanes — the C15–C18 promotion gates

| criterion | evidence | verdict |
|---|---|---|
| **C15** squeeze / short-interest | 18 short rows carry `fz_context`; **0** clear `short_float ≥20% ∧ dtc ≥5`. Distribution: LOW 95 / unknown 46 / MODERATE 10 | **INSUFFICIENT_N — third consecutive cycle** |
| **C16** float-normalized DP block | populated on **1 of 11** accumulation rows carrying the key — the only row where `fz` actually ran | **NA — 5th untestable audit, but throughput-limited not plumbing-limited** |
| **C17** flow-vs-analyst divergence | n=14 divergent, WR 0.571 | scored, below n≥30 promotion bar |
| **C18** insider-cluster conjunction | `insider_cluster_flag` populated on 15 rows — **all 15 are `False`** | **NA — zero variance, not a sample-size problem** |
| breadth divergence | flag on 169 of 525 rows | advisory; structural only |

**C15 should be retired or re-scoped, not merely re-run.** Zero of 18 short rows clear the
threshold, for a third cycle. This is untestable *by construction* on a mega-cap flow
universe — the names this fleet trades do not carry 20% short float. Re-running it a fourth
time will produce the same zero.

**C16/C18 — see Phase 6 §6.7, which corrects the 08-01 audit's measurement.** That audit
reported C18 "unblocked, populates 44/44"; the figure counted **key presence across all
signal classes**, but both fields are only defined for `dark_pool_accumulation` rows. On
the correct denominator (57 accumulation rows, 11 carrying the keys): the **emitter fix
works** — the one post-fix row where the `fz` lane actually ran (GOOGL, 2026-08-03) is
correctly populated at 4.37e-05, and the nulls elsewhere are contract-mandated
graceful-skips. C16 is therefore **throughput-limited**, not broken. **C18 is genuinely
blocked**: 15 populated values, all `False`, so the flag has zero variance and cannot gate
a conjunction at any n.

## Outputs

`phase_4_tools.jsonl`
