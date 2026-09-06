# Phase 4 — Tool Attribution (2026-08-30)

## Provenance header (C23)

**100% verbatim** `decision.json` `score_components[].source_tool`. **Zero prose reconstruction.**
Citation atomicity, graded across three windows:

| window | concatenated citation strings |
|---|---|
| ≤ 2026-08-14 | **8.8%** (108/1225) |
| 2026-08-15 … 08-21 | **0.0%** (0/134) |
| ≥ 2026-08-22 | **0.0%** (0/97) |

The 2026-08-15 P1 #1 fix **holds for a second cycle** — 231 consecutive atomic citations, no
regression. Atomic coverage: **43 distinct tool ids / 1455 row-instances**; only **2.1%**
(30 instances across 18 ids) fall below the N≥5 floor.

Base book WR = **0.385** on n=693 decided.

## Tool tier table (BH at FDR 0.10 across the 25 scored tools)

| tool | n | marginal | with | w/o | ubiquity | p | BH | tier |
|---|---|---|---|---|---|---|---|---|
| `uw screener bullish-bearish` | 5 | +35.0 | 0.60 | 0.38 | 0.01 | 0.379 | n | *load-bearing (prov)* |
| `uw oi decrease-with-volume` | 5 | +22.5 | 0.60 | 0.38 | 0.01 | 0.379 | n | *load-bearing (prov)* |
| `uw options-flow single-leg` | 6 | +10.1 | 0.50 | 0.38 | 0.01 | 0.682 | n | *load-bearing (prov)* |
| `uw dark-pool block-stratified` | 38 | +10.0 | 0.47 | 0.38 | 0.05 | 0.245 | n | SUPPORTIVE |
| `uw insights institutional-accumulation` | 51 | +9.5 | 0.45 | 0.38 | 0.07 | 0.314 | n | SUPPORTIVE |
| `uw oi biggest-increases` | 11 | +7.8 | 0.45 | 0.38 | 0.02 | 0.759 | n | SUPPORTIVE |
| `scripts/dex_flip.py` | 20 | +7.0 | 0.45 | 0.38 | 0.03 | 0.647 | n | SUPPORTIVE |
| `uw options-structure gex` | 11 | +6.0 | 0.36 | 0.39 | 0.02 | 1.000 | n | SUPPORTIVE |
| `uw insights signal-confluence` | 50 | +4.9 | 0.44 | 0.38 | 0.07 | 0.387 | n | SUPPORTIVE |
| **`uw historical cumulative-premium-flow`** | **372** | **+3.8** | 0.42 | 0.35 | **0.54** | **0.008** | **Y** | SUPPORTIVE |
| `uw historical iv-percentile-zscore` | 15 | +2.7 | 0.33 | 0.39 | 0.02 | 0.795 | n | SUPPORTIVE |
| `uw screener earnings-catalyst` | 20 | +2.2 | 0.35 | 0.39 | 0.03 | 0.822 | n | SUPPORTIVE |
| `uw oi pin-risk` | 8 | −0.1 | 0.25 | 0.39 | 0.01 | 0.719 | n | NO-INFO |
| `uw historical vrp` | 15 | −0.7 | 0.33 | 0.39 | 0.02 | 0.795 | n | NO-INFO |
| `uw options-structure dex` | 72 | −1.1 | 0.43 | 0.38 | 0.10 | 0.396 | n | NO-INFO |
| `uw risk market-regime` | 19 | −1.4 | 0.32 | 0.39 | 0.03 | 0.641 | n | NO-INFO |
| `uw hot-chains multileg` | 111 | −1.7 | 0.40 | 0.38 | 0.16 | 0.770 | n | NO-INFO |
| `uw historical oi-trend` | 232 | −2.2 | 0.39 | 0.38 | 0.33 | 0.736 | n | NO-INFO* |
| `uw options-flow sector-flow-persistence` | 84 | −3.9 | 0.36 | 0.39 | 0.12 | 0.578 | n | NO-INFO* |
| `uw insights earnings-play` | 12 | −7.4 | 0.33 | 0.39 | 0.02 | 0.777 | n | NEGATIVE |
| `uw options-structure iv-term-structure` | 65 | −7.5 | 0.31 | 0.39 | 0.09 | 0.165 | n | NEGATIVE |
| `uw options-structure front-end-iv-ratio` | 47 | −7.7 | 0.28 | 0.39 | 0.07 | 0.134 | n | NEGATIVE |
| **`uw options-structure term-skew`** | **103** | **−8.3** | 0.28 | 0.40 | 0.15 | **0.012** | **Y** | NEGATIVE |
| **`scripts/term_structure_hygiene.py`** | **48** | **−14.2** | 0.19 | 0.40 | 0.07 | **0.003** | **Y** | NEGATIVE |
| `uw hot-chains sweep-persistence` | 5 | −50.2 | 0.00 | 0.39 | 0.01 | 0.164 | n | *negative (prov)* |

\* labelled SUPPORTIVE by the raw script threshold; re-tiered NO-INFO here — both sit inside ±3pp.

**3 BH survivors** — the second cycle with any, after twelve consecutive null tables.

## 4.1 The vol toolchain is negative as a block, but the block is one lane

Six vol-surface tools, every one negative: `term-skew` −8.3 · `front-end-iv-ratio` −7.7 ·
`iv-term-structure` −7.5 · `insights earnings-play` −7.4 · `term_structure_hygiene.py` −14.2.
Third cycle of the same signature. Phase 3.2 now supplies the mechanism these tables could
not: **the tools are cited overwhelmingly on vol rows, and the vol lane's short leg is the
part that is inverted.** A term-structure reader is not directionally wrong; the fleet's use
of its output on the sell side is.

Decomposed by lane, `uw options-structure term-skew` shows this cleanly:

| lane | with | without | marginal |
|---|---|---|---|
| `vol_short` | 30.3% (66) | 25.0% (68) | **+5.3pp** |
| `vol_long` | 38.5% (13) | 45.5% (44) | −7.0pp |
| `short` (directional) | 11.1% (9) | 42.0% (207) | −30.9pp |

Inside the `vol_short` lane the tool is mildly *positive*. Its headline −8.3pp is the lane's
base rate, not the tool's contribution. **Do not demote the term-structure readers on this
table** — the defect Phase 3 localizes is the direction the lane trades, not the instrument.

## 4.2 C61 — **cannot be decided; the confound got worse, not better**

Registered 2026-08-22 for `scripts/term_structure_hygiene.py`. Bar: **n ≥ 30 NON-August rows**,
≥2 regime buckets, BH-surviving on a month-stratified denominator.

| | last cycle | this cycle |
|---|---|---|
| n | 42 | 48 |
| marginal | −16.9pp | −14.2pp |
| p (raw) | 0.003 | 0.003 |
| **non-August rows** | 6 | **7** |

Month split: **2026-07 n=7 (14.3%) · 2026-08 n=35 (20.0%)**. The tool is essentially an
August-only instrument. **Non-August n = 7 against a required 30 — C61 stays OPEN**, and it
gained one row in a week. Its BH survival is real but rests almost entirely on the single
weakest month in the corpus; the sign is still opposite the +34.1pp/n=9 reading of two cycles
ago under looser normalization.

**This matters for last cycle's shipped rule.** The 2026-08-22 P1 #3 confirmation-leg
requirement on hygiene-corrected labels shipped on evidence that has **not** cleared its own
bar and shows no sign of doing so. The rule is protective and reversible in one edit, and
Phase 3.2 independently indicts the same lane, so **keep it** — but it should be recorded as
*standing on C61's promissory note, not on C61*.

Note the one datum that does **not** fit a pure lane story: within the vol lane the hygiene
script is negative on **both** legs (`vol_short` −30.6pp n=13, `vol_long` −32.4pp n=15) while
positive on directional longs (+3.7pp n=11). If that survives to a non-August denominator it
is a genuine tool finding rather than a lane finding. n is far too small to say now.

## 4.3 `uw historical cumulative-premium-flow` — BH-surviving, but read the ubiquity column

+3.8pp on **n=372 of 693 decided rows (ubiquity 0.54)**, p=0.008, BH-surviving. Just under the
C32 60% flag. A +3.8pp effect on a tool cited on more than half the book is what a *base-rate
citation* looks like when the "without" arm becomes a small, unusual residual (n=321, WR 0.35).
**Read as SUPPORTIVE and structurally confounded, not as a promotion candidate.** The memory
register's deep-ITM parity netting blind spot applies to this field in both directions and is
not visible in this statistic.

## 4.4 `fz` advisory criteria — C15/C16/C17/C18

| criterion | status | evidence |
|---|---|---|
| **C15** squeeze / short-interest | **INSUFFICIENT_N** | 24 short calls carry `fz`; **0** clear the `short_float ≥ 20% ∧ dtc ≥ 5` bar. Distribution: LOW 142, MODERATE 20, unknown 56 — the fleet simply does not pick high-SI names. |
| **C16 / C62** float-normalized DP block | **OPEN — but the starvation is fixed** | see below |
| **C17** flow-vs-analyst divergence | scored, thin | n=14 divergent, WR 0.571 vs book 0.385. Below the action floor; keep advisory. |
| **C18** insider clusters | **NA** | `insider_cluster_flag` populates 30/789. Dead since 2026-08-08 (zero variance across 15 populations). |
| breadth divergence | advisory | flag present on 211/671; structural only. |

**C16/C62 — the emission fix worked, the bar did not move.** The 2026-08-22 P2 rec to make
float-ratio emission mandatory has taken hold *within the target class*:

| month | `dark_pool_accumulation` rows carrying `dp_block_to_float_ratio` |
|---|---|
| 2026-05 | 0 / 9 |
| 2026-06 | 0 / 31 |
| 2026-07 | 0 / 15 |
| **2026-08** | **10 / 13** |

Corpus-wide 13 populated (was 10). **C62 test at the pre-registered, un-refit threshold 0.0010:**

| arm | n decided | WR |
|---|---|---|
| **≥ 0.0010** | **2** | 100.0% |
| < 0.0010 | 9 | 11.1% |

Separation **+88.9pp** and the rank ordering still holds (the two largest ratios, NBIS 0.00233
and SNDK 0.00224, remain the only WINs; every row ≤ 0.000578 lost except MSFT 0.000008).
Out-of-sample since registration: 3 rows, 1 decided — AVGO at 0.000068, **LOSS**, arm-consistent.

**C62 REMAINS OPEN. 11 of a required 30 decided; 2 of a required 10 in the upper arm; 2 of a
required ≥2 regime buckets ✅.** The 88.9pp separation is *the same n=9 post-hoc pattern that
was registered*, plus one confirming low-arm row. **Do not promote.** The blocker is no longer
emission — it is that `dark_pool_accumulation` produces ~3 calls/week and only a handful ever
clear 0.0010.

**Harness note (auditor-side).** `phase4_tools.py` reported C16 as *"NA — per-call DP-block/float
ratio not in envelope"*: it reads `fz_context.dp_block_to_float_ratio`, but the schema and the
emitters write **`calls[].dp_block_to_float_ratio`**. The field was present and the harness was
looking in the wrong place. Corrected here; the numbers above are from the schema path. Any
prior-cycle "not emitted" claim sourced from that helper should be treated as unverified.

## 4.5 Tools with no measurable contribution

`uw options-structure dex` (−1.1, n=72) and `uw hot-chains multileg` (−1.7, n=111) are flat
despite being the evidence behind two of the largest frozen rubric awards (+1 mechanized DEX,
+2 multileg). `uw historical oi-trend` −2.2 on n=232 — a third cycle consistent with the
memory register's finding that `oi-trend` BUILDING fires with near-zero discrimination.
**No tier movement recommended on any of these** — all BH-null, and the frozen rubric is not
retuned from a single window.

## Outputs

`phase_4_tools.jsonl` · `phase_4_tools_atomic.jsonl`
