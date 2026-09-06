# Phase 4 — Tool Attribution (2026-08-01)

**Provenance: 100% verbatim.** Every `tools_cited` entry is read from
`decision.json → calls[].score_components[].source_tool`. Zero prose reconstruction, so
the C23 reconstructed-citation priority cap does not bind this cycle.

Multiple-hypothesis control: Benjamini-Hochberg, FDR 0.10, across the 18 tools clearing
the N≥5 floor. Tools cited 5–7 times are `THIN_N` and tier-rated **provisionally**
(marked `prov`, lower-case reading) — never the sole basis for a Phase 7 item.

## Tool table

| tool | n | marginal | WR with | WR w/o | ubiquity | p | BH | tier |
|---|---|---|---|---|---|---|---|---|
| `screener bullish-bearish` | 5 | +41.5 | 0.60 | 0.43 | 0.01 | 0.455 | no | load-bearing (prov) |
| `historical oi-trend --days 5` | 5 | +24.9 | 0.60 | 0.43 | 0.01 | 0.455 | no | load-bearing (prov) |
| `iv-term-structure + iv-percentile-zscore` | 5 | +16.5 | 0.60 | 0.43 | 0.01 | 0.455 | no | load-bearing (prov) |
| `options-structure gex` | 9 | +14.3 | 0.33 | 0.44 | 0.02 | 0.534 | no | LOAD-BEARING |
| `insights institutional-accumulation` | 33 | +11.1 | 0.46 | 0.43 | 0.07 | 0.816 | no | LOAD-BEARING |
| `historical cumulative-premium-flow` | 268 | +7.3 | 0.46 | 0.41 | **0.54** | 0.331 | no | SUPPORTIVE ⚠ubiquity |
| `insights signal-confluence` | 50 | +3.6 | 0.44 | 0.43 | 0.10 | 0.942 | no | SUPPORTIVE |
| `historical oi-trend` | 127 | +2.4 | 0.47 | 0.42 | 0.25 | 0.326 | no | SUPPORTIVE |
| `dark-pool block-stratified` | 26 | +1.8 | 0.42 | 0.44 | 0.05 | 0.899 | no | NO-INFO |
| `hot-chains multileg` | 77 | −0.4 | 0.43 | 0.44 | 0.15 | 0.900 | no | NO-INFO |
| `options-flow sector-flow-persistence` | 57 | −1.0 | 0.39 | 0.44 | 0.11 | 0.426 | no | NO-INFO |
| `options-structure iv-term-structure` | 23 | −1.1 | 0.48 | 0.43 | 0.05 | 0.669 | no | NO-INFO |
| `screener earnings-catalyst` | 7 | −1.6 | 0.43 | 0.43 | 0.01 | 0.972 | no | no-info (prov) |
| `options-structure term-skew` | 64 | −6.2 | 0.39 | 0.44 | 0.13 | 0.442 | no | NEGATIVE |
| `options-structure front-end-iv-ratio` | 20 | −9.9 | 0.35 | 0.44 | 0.04 | 0.433 | no | NEGATIVE |
| `options-structure dex` | 57 | −14.7 | 0.42 | 0.44 | 0.11 | 0.820 | no | NEGATIVE |
| `insights earnings-play` | 11 | −16.0 | 0.36 | 0.44 | 0.02 | 0.629 | no | NEGATIVE |

47 further tool strings fall below N=5 and are `INSUFFICIENT_N` — largely conjunction
labels (`A + B + C`) that the agents emit as a single composite `source_tool` string.

## Desk commentary — market-maker quant

**Ninth consecutive BH-null tool table.** The smallest p-value in the sweep is **0.194**;
nothing is close. Across nine audits not one `uw` tool has ever survived multiple-hypothesis
correction as a discriminator of outcome. That is now a structural finding rather than a
run of bad luck: **the tools identify *what is happening*; they do not, individually,
predict *what happens next*.** The rubric's premise — that citing more tools raises
conviction — has no support in nine windows of data.

**`dark-pool block-stratified` completes its collapse.** +15.9pp (06-27) → −2.3 (07-11)
→ +1.6 (07-25) → **+1.8pp now, with WR-with 0.42 against WR-without 0.44.** A gate that
splits the book into two piles of identical win rate is not a filter, it is a coin sorted
by colour. The 07-11 "isolate block-stratified" pre-registration stays refuted for a
third cycle.

**`options-structure dex` at −14.7pp on n=57 is the most expensive line in the table**,
and it is the tool behind the mechanized DEX-flip rubric point (C50). Sign has been
unstable window-to-window, and it is BH-null (p=0.820) — so this is *not* a
recommendation to cut it. It is a reason C50 must clear a real per-tape acceptance bar
before that +3 is ever trusted.

**`cumulative-premium-flow` is ubiquity-confounded** — cited on 268 rows, 54% of its
class. Its +7.3pp reads high for a base-rate citation but `with`≈`without` by construction.
Do not read it as a live discriminator either way.

**The three `load-bearing (prov)` entries are n=5 artifacts.** `screener bullish-bearish`
at +41.5pp on five citations is exactly the false positive the C23 THIN_N rule exists to
quarantine. Reported, not actionable.

## `fz` advisory promotion gates (C15–C18)

| criterion | status | evidence |
|---|---|---|
| **C15** squeeze-pressure on shorts | **INSUFFICIENT_N — untestable by construction** | 18 short rows carry `fz_context`; **0** clear `short_float ≥20% ∧ days_to_cover ≥5`. Distribution: LOW 91 / unknown 44 / MODERATE 6. |
| **C16** float-normalized DP block | **NA — field absent** | `dp_block_pct_of_float` still not in the schema. **4th consecutive untestable audit.** |
| **C17** flow-vs-analyst divergence | scored, thin | n=14 divergent, WR 0.571. Below promotion bar. |
| **C18** insider-cluster 3-way conjunction | **NA → newly enabled** | `insider_cluster_flag` now emitted on **44/44** post-07-27 calls (13 non-null corpus-wide). Testable from next audit. |
| breadth divergence | advisory | flag on 153/484 rows; structural only. |

**C15 should be re-scoped or retired, not re-run.** A mega-cap options-flow universe
structurally cannot produce a 20%-short-float name; this is a definitional mismatch, not
under-powering. **C16 is the one live blocker that a one-line schema addition fixes** —
it has now been recommended and not applied once. **C18 is unblocked** as of 07-27 and
should have real N by the next cycle.

## Hard-rule compliance

- No tool tier *movement* is recommended: BH-null across the board (skill hard rule).
- `options-structure gex` reads LOAD-BEARING on a **+14.3pp marginal with WR-with 0.33
  below WR-without 0.44** — the marginal is class-conditional and the raw split inverts.
  Manual sanity-check per the CONFOUNDED hard rule: **do not promote.** n=9.
- Ubiquity flag raised on `cumulative-premium-flow` (0.54) per C32-precursor.

Output: `phase_4_tools.jsonl`, `phase4_tools.py`.
