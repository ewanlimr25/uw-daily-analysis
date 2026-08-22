# Phase 1 — Inventory & Parse (2026-08-22)

**Provenance: 100% verbatim decision-envelope.** 76 `decision.json` sidecars (63 daily +
13 weekly), **76/76 validate clean** against `schemas/decision_envelope.schema.json`
(`scripts/validate_decision.py`, zero fatal errors). No prose re-parsing was performed on any
row. 21 legacy prose-only reports (17 daily 2026-04-30 → 2026-05-22, 4 weekly W18–W21) predate
the envelope and are recorded as a **coverage gap**, not parsed — they carry no
`score_components` / `raw_score` / `win_rate` and were already resolved by prior audits.

- **737 call rows** | 185 unique tickers | report dates **2026-05-25 → 2026-08-21**
- Δ vs 2026-08-15 audit: **+6 envelopes, +65 rows** (daily 08-17…08-21 + weekly W34)
- **0 `Σ score_components.points ≠ raw_score` violations** (12th consecutive clean cycle)
- 252 rows carry a `claimed_win_rate`

## Stratification (never pooled across eras — schema ≥1.3 `rubric_version`)

| rubric era | rows |
|---|---|
| **`2026-06-12` (FROZEN)** | **586** |
| `era_0530_0605` | 69 |
| `era_0525_0529` | 54 |
| `pre_freeze_post_0606` | 28 |

**Post-freeze rows: 586.** Out-of-regime (P0.6 half-cap) rows: 44.

| regime bucket | rows |
|---|---|
| uptrend | 323 |
| transitional_other | 203 |
| pullback_in_uptrend | 130 |
| choppy | 81 |

Four populated regime buckets — **fifth consecutive cross-regime cycle**.

## Distributions

| dimension | breakdown |
|---|---|
| kind | daily 649 / weekly 88 |
| horizon | swing 523 / vol 200 / LEAP 14 |
| section | watch_only 336, swing_long 125, swing_short 120, vol_short 104, vol_long 45, leap_disqualified 5, leap 2 |
| tier | DROP 581, LOW 129, MEDIUM 20, HIGH 7 |
| direction | long 293, short 213, vol_short 130, vol_long 56, neutral 45 |
| final_size | skip 370, watch_only 309, **starter 35, half 12, veto 10, full 1** |
| fundamentals verdict | NA 243, (null) 219, CAUTION 131, CONFIRM 118, **VETO 26** |

**Top signal classes:** `earnings_vol` 146, `bearish_flow` 135, `multileg_directional` 104,
`bullish_flow` 71, `dark_pool_accumulation` 66, `sector_rotation` 48, `high_iv_rank` 35.

**Post-freeze tiers: DROP 519 / LOW 67 / MEDIUM 0 / HIGH 0.** Every HIGH and MEDIUM row in
the corpus predates the freeze. **48 sized calls total; the most recent is 2026-07-24** — the
sized book has not grown in four weeks (34 consecutive empty daily boards).

## Post-fix cohort — grading the 2026-08-15 recommendations

The 08-15 recs landed in commit `c29c268` (2026-08-15 20:38). **Post-fix cohort = 65 rows /
6 envelopes, `report_date ≥ 2026-08-17`.**

### P1 #1 — one canonical tool id per component: **LANDED CLEAN** ✅

| | distinct citation strings | instances | concatenations | trapped in n<5 labels |
|---|---|---|---|---|
| pre-fix (672 rows) | **122** | 1,225 | 60 strings / 121 inst (**9.9%**) | 155 inst (12.7%) |
| **post-fix (65 rows)** | **17** | 134 | **0 / 0 (0.0%)** | 12 inst (9.0%) |

Every post-fix citation is a canonical id. The 122-label fragmentation that made eleven
cycles of tool tiers un-measurable is gone in the new cohort.

### P1 #2 — no `backtest` win_rate on classes `signal-backtest` cannot measure: **LANDED CLEAN** ✅

| | backtest-sourced quotes | unsupported-class quotes | `earnings_vol` quoted |
|---|---|---|---|
| pre-fix | 210 | **37** (earnings_vol 15, dealer_positioning 11, multi_day_sweep 4, multileg 3, gamma_breakout 3, sector_rotation 1) | 13 of 125 rows |
| **post-fix** | 11 | **0** | **0 of 21 rows** |

Post-fix `win_rate_source` is exclusively `NA(substrate)` (54) and `backtest_clean` (11).

### P2 #7 — `dominant_signal_class` canonical enum: **HALF-LANDED** ⚠️

The validator still warns on **5 post-fix rows** (2026-08-18: LITE, NBIS, AMAT, CRWV, SNDK)
emitting the off-canonical label **`vol_long`**. All 5 `vol_long` rows in the entire corpus are
post-fix — the emitter learned a *new* off-list label after the fix shipped. Carried to Phase 7.

## Data-quality flags

1. **`vol_long` off-canonical class label** — 5 post-fix rows (above). Forces the Phase-2
   collapse map to grow again.
2. **C16 still ungradeable** — 2026-08-17 GLD is a `dark_pool_accumulation` row with
   `fz_context.available=true` but `dp_block_to_float_ratio=null`. The 08-15 backfill duty
   sharpening has not yet produced a populated ratio.
3. **2 tickers have no Yahoo OHLC** — `BRKB` (404; share-class ticker, should be `BRK-B`) and
   `SPX` (index, no chart endpoint). Both tag INCONCLUSIVE(`data_unavailable`), never LOSS.
   Same two as the prior cycle — a persistent, bounded 5-row gap.
4. **`fundamentals_verdict` null on 219 rows** — concentrated in DROP rows the fleet
   early-exits before Phase 2b. Expected (C54), not drift.
