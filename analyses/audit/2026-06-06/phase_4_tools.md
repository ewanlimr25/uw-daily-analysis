# Phase 4 — Tool Attribution (2026-06-06 · C23 BH · C32 ubiquity · provenance cap)

## ⚠️ Provenance + significance caveats (govern EVERYTHING below)

1. **Citations remain majority-reconstructed.** 379 of 432 decided rows are legacy prose;
   only **53 decided rows carry verbatim envelope `source_tool`** (first run with any — the
   05-30 run had zero). 53 verbatim rows cannot re-base a 432-row tool table, so every tier
   below is **structural/qualitative → Phase-7 cap at P1** (C23). The verbatim subset becomes
   decisive around mid-June as June envelopes close their windows.
2. **Benjamini-Hochberg kills every flag again (C23).** ~27 simultaneous MC tests, **zero
   survive BH at FDR 0.10**. Tool tiers are hypotheses, not facts — third run confirming.
3. **C32 ubiquity does not fire** (max cite_frac 0.31, `cumulative-premium-flow`); citations
   are sparse enough that the CONFOUNDED detector structurally cannot fire either.

## Tool tier list (N ≥ 5) — with 05-30 MC beside it

| Tool | N | MC (pp) | 05-30 MC | Tier | Stability |
|---|---|---|---|---|---|
| `uw options-structure today-gamma-flip` | 10 | +65.6 | +63.2 | LOAD-BEARING | tiny-N, stable |
| `uw options-structure multileg-activity` | 9 | +52.9 | +50.6 | LOAD-BEARING | tiny-N, stable |
| `historical_cumulative_premium_flow` (LEAP accretion label) | 8 | +26.9 | — | LOAD-BEARING | thin |
| `uw options-flow multi-day-sweep-persistence` | 10 | +26.4 | +22.3 | LOAD-BEARING | stable |
| `uw insights earnings-play` | 9 | +20.8 | +13.9 | LOAD-BEARING | up |
| `uw historical sweep-persistence` | 8 | +18.6 | — | LOAD-BEARING | thin |
| **`uw dark-pool block-stratified`** | **67** | **+17.0** | +14.0 | **LOAD-BEARING** | **durable, 3 runs** |
| **`uw options-structure dex`** | **70** | **+11.1** | +14.0 | **LOAD-BEARING** | **durable, 3 runs** |
| `uw historical iv-rank` | 11 | +9.3 | — | SUPPORTIVE | |
| `uw options-structure term-skew` | 62 | +6.7 | +7.9 | SUPPORTIVE | vol-proxy-coupled |
| `uw options-flow sector-flow-persistence` | 49 | +5.4 | +15.5 | SUPPORTIVE | faded |
| `uw options-structure iv-term-structure` | 31 | +2.4 | — | SUPPORTIVE/NO-INFO | |
| `uw historical oi-trend` | 73 | −0.5 | +0.4 | NO-INFO | durable NO-INFO |
| **`uw historical cumulative-premium-flow`** | **136** | **−3.5** | +1.7 | **NO-INFO** | **durable, 3 runs, most-cited** |
| `uw insights signal-confluence` | 44 | −6.2 | −1.0 | NEGATIVE (mild) | drifting − |
| `uw hot-chains sweep-persistence` | 32 | −7.2 | −2.6 | NEGATIVE (mild) | drifting − |
| `uw hot-chains multileg` | 27 | −15.5 | — | NEGATIVE | |
| `uw insights institutional-accumulation` | 15 | −23.0 | −15.1 | NEGATIVE | durable − |
| `uw historical gex` / `options-structure gex` | 8/13 | −31.9 / −50.0 | −33 / −50 | NEGATIVE | durable − |
| `uw historical pc-ratio-zscore` | 9 | −33.3 | — | NEGATIVE | |
| `uw insights conviction-matrix` | 7 | −45.2 | −53.1 | NEGATIVE (thin) | durable − |

(Thin-N 5–7 provisional: `dealer-delta-exposure` +6.2, `vrp` −10.8, `top-premium-trades`
−10.8, `iv-percentile-zscore` −17.1, `front-end-iv-ratio` −25.3. 26 tools INSUFFICIENT_N < 5.)

## Desk commentary (market-maker quant)

- **The two durable LOAD-BEARING tools are now three-run stable: `dark-pool block-stratified`
  (+25 → +14 → +17) and `options-structure dex` (+15.5 → +14 → +11).** Both fire on winners
  *and* losers at scale (n=67/70). These remain the only evidence tools a desk could defend.
- **`cumulative-premium-flow` is the book's most-cited tool (n=136) and is NO-INFO for the
  third straight run (−3.5pp).** It's the reflexive comfort citation. The NEE dividend-arb
  miss (2026-06-04, memory: deep-ITM ex-div call sweeps counted as bullish premium) shows
  *why*: the tool counts premium without classifying intent.
- **The negative cluster is durable and got more negative:** `gex` variants (−32/−50),
  `conviction-matrix` (−45), `institutional-accumulation` (−23), `pc-ratio-zscore` (−33).
  GEX-as-evidence keeps firing on losers — consistent with the repo's own decision to hold
  §2 GEX at 0-point advisory. `signal-confluence` and `hot-chains sweep-persistence` drifted
  from NO-INFO to mildly negative.
- **No tool tier change is BH-significant; no tier change ships as P0.**

## `fz` advisory dimensions (C15–C18) + C28 — first decided data

| Axis (criterion) | Decided N | Finding | Verdict |
|---|---|---|---|
| squeeze_pressure (C15) | **0** (no decided call met SI≥20% ∧ DTC≥5) | — | INSUFFICIENT_N — stay advisory |
| float-normalized blocks (C16) | 0 (block-%-of-float never recorded per call) | — | NOT COMPUTABLE yet — needs the block-size write-back |
| **analyst divergence (C17)** | **17** longs w/ target data | Longs fighting analyst targets (`upside_to_target_pct < 0`): **2/10 = 20% WR**; aligned longs: **4/7 = 57%** → divergence ≈ **−37pp** | **First signed evidence, direction matches C17.** Below promotion floor (n<5 per cell after split is false, but single-test, thin) — **stay advisory, re-test at n≥30** |
| insider clusters (C18) | 0 | — | INSUFFICIENT_N — stay advisory |
| breadth_cross_check | 4 report-level flags, 1 followed by next-session drawdown | — | INSUFFICIENT_N |
| **C28 `distribution_flag`** | **9 decided flagged longs** | **3/9 = 33% WR vs 54.9% long book (−22pp)** | Signed in the C28 direction (flag finds losers). Thin-N, single regime — **stay advisory**, promote-track if it holds at n≥20 |

**No C15–C18 promotion clears its threshold.** But two advisory lanes (C17 analyst-divergence,
C28 distribution_flag) produced their first *signed* outcome evidence this run, both in the
hypothesized direction — these are the two to re-test first when the June envelope cohort
closes (~2026-06-12+).

## Output
- `phase_4_tools.jsonl` — full table with `mc_pp`, `p`, `bh_significant`, `cite_frac`,
  `thin_n`. `phase4_tools.py` — reproducible.
