# Phase 4 — Tool Attribution (2026-09-05)

## Provenance basis (governs the priority ceiling, C23)

**100% verbatim.** Every citation is read from `decision.json` `score_components[].source_tool`
and `tools_cited[]`. Zero prose reconstruction on 878 rows / 751 decided. The reconstructed-
citation P0 cap **does not bind this cycle**.

Atomic coverage: **44 distinct atomic tool ids over 1,558 row-instances**; 26 scored at N ≥ 5;
18 ids / 32 instances (2.1%) below the floor. Base book WR = 0.394 (n=751).

## The atomic table (composite ids split on `+`)

| tool | n | marg | with | w/o | ubiquity | p | BH | tier |
|---|---|---|---|---|---|---|---|---|
| `uw screener bullish-bearish` | 5 | +31.7 | 0.60 | 0.39 | 0.01 | 0.388 | n | load-bearing (prov) |
| `uw oi decrease-with-volume` | 6 | +30.3 | 0.67 | 0.39 | 0.01 | 0.219 | n | load-bearing (prov) |
| `scripts/dex_flip.py` | 24 | +12.7 | 0.50 | 0.39 | 0.03 | 0.299 | n | LOAD-BEARING |
| `uw insights institutional-accumulation` | 56 | +11.0 | 0.46 | 0.39 | 0.07 | 0.273 | n | LOAD-BEARING |
| `uw options-flow single-leg` | 6 | +10.4 | 0.50 | 0.39 | 0.01 | 0.686 | n | load-bearing (prov) |
| `uw oi pin-risk` | 8 | +7.2 | 0.62 | 0.39 | 0.01 | 0.276 | n | SUPPORTIVE |
| `uw dark-pool block-stratified` | 40 | +5.7 | 0.45 | 0.39 | 0.05 | 0.517 | n | SUPPORTIVE |
| `uw insights signal-confluence` | 50 | +4.7 | 0.44 | 0.39 | 0.07 | 0.473 | n | SUPPORTIVE |
| `uw oi biggest-increases` | 11 | +4.4 | 0.45 | 0.39 | 0.01 | 0.761 | n | SUPPORTIVE |
| `uw historical cumulative-premium-flow` | 399 | +3.0 | 0.41 | 0.37 | **0.53** | 0.088 | n | SUPPORTIVE ⚠ubiquity |
| `uw options-structure iv-term-structure` | 78 | +2.7 | 0.37 | 0.40 | 0.10 | 0.729 | n | SUPPORTIVE |
| `uw options-structure gex` | 11 | +1.7 | 0.55 | 0.39 | 0.01 | 0.359 | n | NO-INFO |
| `uw screener earnings-catalyst` | 21 | +0.5 | 0.33 | 0.40 | 0.03 | 0.659 | n | NO-INFO |
| `uw historical iv-percentile-zscore` | 15 | +0.4 | 0.33 | 0.40 | 0.02 | 0.794 | n | NO-INFO |
| `uw options-structure dex` | 75 | −2.0 | 0.41 | 0.39 | 0.10 | 0.724 | n | NO-INFO |
| `uw options-flow sector-flow-persistence` | 86 | −2.6 | 0.38 | 0.40 | 0.11 | 0.912 | n | NO-INFO |
| `uw historical oi-trend` | 243 | −2.8 | 0.40 | 0.39 | **0.32** | 1.000 | n | NO-INFO ⚠ubiquity |
| `uw historical vrp` | 15 | −3.1 | 0.33 | 0.40 | 0.02 | 0.794 | n | NO-INFO |
| `uw options-structure front-end-iv-ratio` | 52 | −6.4 | 0.29 | 0.40 | 0.07 | 0.119 | n | NEGATIVE |
| `uw risk market-regime` | 20 | −6.4 | 0.30 | 0.40 | 0.03 | 0.495 | n | NEGATIVE |
| `uw insights earnings-play` | 12 | −7.1 | 0.33 | 0.40 | 0.02 | 0.774 | n | NEGATIVE |
| `uw hot-chains multileg` | 117 | −7.9 | 0.40 | 0.39 | 0.16 | 0.850 | n | NEGATIVE |
| **`uw options-structure term-skew`** | **117** | **−10.8** | 0.27 | 0.42 | 0.16 | **0.002** | **Y** | see 4.1 |
| **`scripts/term_structure_hygiene.py`** | **49** | **−20.5** | 0.18 | 0.41 | 0.07 | **0.001** | **Y** | see 4.1 |
| `uw oi smart-positioning` | 5 | −21.8 | 0.20 | 0.40 | 0.01 | 0.654 | n | negative (prov) |
| `uw hot-chains sweep-persistence` | 5 | −50.0 | 0.00 | 0.40 | 0.01 | 0.164 | n | negative (prov) |

**2 of 26 tools survive Benjamini-Hochberg at FDR 0.10.** Both are vol-lane readers. §4.1 is
the only place in this phase that matters.

## 4.1 — The two BH survivors, lane-controlled. One washes out; one does not.

Last cycle established the confound and it applies again: a tool cited overwhelmingly on
`vol_short` inherits `vol_short`'s −29pp deficit whether or not the tool contributes anything.
The test is the marginal contribution **inside the lane**.

### `uw options-structure term-skew` — **confounded. Do not demote.**

91 of its 105 decided citing rows are VOL rows, against a 30% VOL base rate.

| stratum | with | WR | without | WR | marginal |
|---|---|---|---|---|---|
| overall | 105 | 0.276 | 646 | 0.413 | **−13.7pp** |
| inside VOL | 91 | 0.297 | 131 | 0.366 | −7.0pp |
| **inside `vol_short`** | 76 | 0.263 | 70 | 0.243 | **+2.0pp** |
| inside `vol_long` | 15 | 0.467 | 61 | 0.508 | −4.2pp |

Inside the lane that actually loses, the tool is **positive**. Its headline negativity is
composition, exactly as last cycle warned. **This is not a tier change and must not become
one.** The one genuinely poor stratum is `INSIDE DIRECTIONAL` (0.143 with vs 0.421 without,
n=14) — that is a **scope** observation, not a quality one: a term-structure reader cited on a
directional thesis is a tool being used outside its remit.

### `scripts/term_structure_hygiene.py` — **does NOT wash out, and still cannot be acted on.**

| stratum | with | WR | without | WR | marginal |
|---|---|---|---|---|---|
| overall (atomic) | 49 | 0.18 | — | 0.41 | −20.5pp |
| inside VOL | 21 | 0.143 | 201 | 0.358 | −21.5pp |
| inside `vol_short` | 10 | **0.000** | 136 | 0.272 | −27.2pp |
| inside `vol_long` | 11 | 0.273 | 65 | 0.538 | −26.6pp |
| inside DIRECTIONAL | 10 | 0.300 | 510 | 0.416 | −11.6pp |

Negative **within every lane it is cited on**, including the one where `term-skew` turns
positive. That is a real signal about the tool, not its neighbours.

**C61's bar is still nowhere near met, and it went backwards.** 27 of 31 citing decided rows
are **August**; non-August accrual is **n = 4 of a required 30** (last cycle: 7). 22 of 31 are
a single regime bucket. A −20pp finding concentrated in one month and one regime is a month,
not a tool. **C61 stays open. No recommendation.**

## 4.2 — Ubiquity confounds (flagged, not scored)

`uw historical cumulative-premium-flow` is cited on **53%** of decided rows and
`uw historical oi-trend` on **32%**. Their `with ≈ without` readings are arithmetic, not
evidence — they *are* the base rate. Neither reads as dead; both are unscoreable by this
method. `uw historical oi-trend` carries the separate, already-documented defect that
`consecutive_build_days` is censored by `--days`, making its BUILDING label near-tautological.

## 4.3 — `fz` advisory lanes (C15–C18)

| criterion | state | verdict |
|---|---|---|
| **C15** squeeze / short-interest | `n_hi_si = 0`; distribution LOW 155 / MODERATE 22 / unknown 57 | **INSUFFICIENT_N** — the high-SI arm has never once fired |
| **C16 / C62** float-normalised DP block | populated 16, decided 14, above-threshold arm **n=2** | **OPEN** — 14 of 30 decided, 2 of 10 upper arm |
| **C17** flow-vs-analyst divergence | n=14 divergent, WR 0.571 | scored, below promotion N |
| **C18** insider cluster | `insider_cluster_flag` populated 30, **all `False`** | **DEAD — zero variance, second cycle** |

**C62 note.** The upper arm reads 2-for-2 (WR 1.000) against 2-for-12 (0.167) below. That is a
44-row-equivalent effect on **n=2** and must not be quoted as promising — it is one coin
landing twice. The pre-registered, un-refit **0.0010** threshold is held fixed, as required.

**C18 has a contradiction worth naming.** `insider_cluster_flag` is `False` on all 30
populated rows — no variance, nothing to conjoin — while the newly-instrumented
`fundamentals_verdict_reason` shows **`insider_selling_cluster` is the single most common
CAUTION reason: 9 of 15 post-change rows**. Two insider signals in the same fleet, one
uniformly silent and one dominant. They read different sources (`fz insider-clusters` vs the
Finnhub MSPR path in `fundamentals-gate`), but nothing in the schema says so, and a reader
comparing them would draw the wrong conclusion.

## 4.4 — New instrumentation, working as designed

`fundamentals_verdict_reason` (last cycle's P1 #1) is populated on **15 rows, all
post-2026-08-30**, exactly as specified. Reasons: `insider_selling_cluster` 9,
`news_catalyst_contradicts_thesis` 2, `earnings_surprise_streak_negative` 2, `other` 2.
Null on every prior envelope **by design**. Do not grade it until it has its own N — but it is
already earning its keep: it is the field that surfaced the C18 contradiction above.

## Desk read

The tool table is **BH-null in substance for the 13th consecutive cycle.** Two survivors
appeared; one is composition and the other is one month of August. No tool tier moves, no
required-citation list changes, and no agent file is touched on tool evidence this cycle.
`scripts/dex_flip.py` (+12.7pp, n=24) and `uw insights institutional-accumulation` (+11.0pp,
n=56) clear the LOAD-BEARING threshold on effect size but neither survives BH — they are the
two worth watching, not promoting.
