# Phase 1 — Inventory & Parse

**Audit run:** 2026-05-15
**Dataset:** 12 daily reports (2026-04-30 → 2026-05-15) + 3 weekly reports (W18, W19, W20)
**Threshold check:** N_daily=12 ≥ 10, N_weekly=3 ≥ 3 — PASS, no relax_threshold banner needed.
**UW data freshness:** current through 2026-05-15 — no stale-data abort.

## Summary counts

| Tier | Daily | Weekly | Total |
|---|---|---|---|
| Sized long (full / half / starter) | 88 | 18 | 106 |
| Sized short / fade | 26 | 2 | 28 |
| Vol long (BUY VOL / calendar) | 19 | 4 | 23 |
| Vol short (SELL VOL / IC) | 11 | 1 | 12 |
| LEAP-disqualified watch | 12 | 2 | 14 |
| Skipped/dropped post-gate (kept for compliance audit) | 18 | 4 | 22 |
| **Total trade-rows kept** | **174** | **31** | **205** |

Watch-only single-signal names (§8 of each report) are NOT extracted as trade rows — they have no structure/invalidation. They are referenced only by the decision-process audit (Phase 6) for "did the rubric correctly exclude them?" checks.

## Format coverage gaps

- **Legacy format:** `2026-04-30.md` is the only legacy-format report. No §7 raw_score, no `score_components`, no `claimed_win_rate`. Calls extracted from §3 (Sweeps), §4 (Accumulation), §5 (Contrarian), §6 (Earnings), §8 (Watchlist). Tagged `legacy_format=true`. Direction, structure, invalidation are all readable; only the rubric tally is missing.
- **Rubric drift mid-window:** the conviction rubric expanded between 2026-05-04 (10 line items, max raw ~12) and 2026-05-07 (13 line items including +3 dealer-positioning, +2 cum_premium_flow, max raw ~17). A second drift on 2026-05-11 added the −2 flow_conflict component. Phase 5 must re-fit on the *current* (most recent) rubric; older calls are scored on whatever rubric was live at the time.
- **Win-rate field:** present on every report from 2026-05-05 onward; null for 04-30 and 05-01 (which used the older sizing language "FULL backtest × HALF regime" without an explicit win_rate number).
- **GOOG / GOOGL share-class confusion:** 2026-05-04 cites GOOG, 2026-05-05 cites both, weekly W18 cites GOOG. Treated as two distinct rows when explicit (one wins, one loses ⇒ kept separate). Same trade direction in every case (LONG).
- **Re-citation across reports:** AAPL appears in 11 of 12 daily reports plus W19, W20 — same rolling thesis. Each is one row keyed by (report_date, ticker). Outcome resolution windows differ (each entry resolved on its own forward window), so this is not double-counting.

## Data-quality flags (carried forward to Phase 2)

- 2026-04-30 GEX permission-denied; iv_term_structure permission-denied for BWA/CRUS
- 2026-05-01 risk-monitor hit usage cap mid-run; downstream gates may be incomplete
- 2026-05-08 watchlist write-back tickers verified
- 2026-05-11 dark_pool_accumulation backtest n=0 — proxied from bullish_flow throughout downstream
- 2026-05-13 sector_flow_persistence broken (uniform 1.0 across sectors); oi_position_rolls parquet error
- 2026-05-15 yfinance fundamentals 401 — UW-only data informed reads

## Per-report row counts (sanity)

| Report | Trade rows | LEAP | Vol long | Vol short |
|---|---|---|---|---|
| 2026-04-30 | 22 | 0 | 0 | 2 (POWL, MNDY) |
| 2026-05-01 | 13 | 0 | 4 | 1 |
| 2026-05-04 | 12 | 1 (AMZN LEAP) | 0 | 2 |
| 2026-05-05 | 21 | 0 | 2 | 5 |
| 2026-05-06 | 14 | 0 | 0 | 4 |
| 2026-05-07 | 28 | 0 | 6 | 1 |
| 2026-05-08 | 22 | 0 | 0 | 5 |
| 2026-05-11 | 14 | 0 | 0 | 0 |
| 2026-05-12 | 17 | 3 | 2 | 1 |
| 2026-05-13 | 8 | 0 | 9 | 1 |
| 2026-05-14 | 13 | 0 | 2 | 0 |
| 2026-05-15 | 19 | 0 | 5 | 1 |
| W18 | 11 | 3 | 0 | 0 |
| W19 | 12 | 0 | 1 | 0 |
| W20 | 8 | 1 | 0 | 0 |

No non-empty report yielded zero rows — parser sanity check passed.

## Sized-call distribution by horizon and tier

| Horizon | High | Med | Low/Starter | Skip-but-tracked | Total |
|---|---|---|---|---|---|
| 0DTE / pin | 0 | 4 | 8 | 0 | 12 |
| Swing (1–6w) | 13 | 22 | 51 | 17 | 103 |
| LEAP | 1 | 2 | 1 | 8 | 12 |
| Vol (long+short) | 0 | 12 | 19 | 4 | 35 |
| Weekly horizon | 4 | 6 | 17 | 4 | 31 |

## Dominant signal-class distribution

| Signal class | N |
|---|---|
| dark_pool_accumulation | 36 |
| bullish_flow | 31 |
| gamma_breakout | 17 |
| dealer_positioning_flip | 14 |
| multi_day_sweep | 14 |
| multileg_directional | 13 |
| leap_directional | 11 |
| bearish_flow | 12 |
| vol_kink_long / earnings_buyvol | 19 |
| earnings_sellvol / kinked_calendar | 11 |
| vanna_squeeze | 4 |
| contrarian_fade | 3 |
| pin / opex_pin | 8 |
| (legacy / unclassified) | 22 |

## Desk-style observation

Two structural facts of the dataset that Phase 3–6 must respect:

1. **The dataset is regime-stationary.** Every single one of the 15 reports is classified TRANSITIONAL/UPTREND. There is **no bear regime, no risk-off, no VIX shock** in the window. Win-rate calibrations from this dataset cannot be extrapolated to a different regime — Phase 7 must say this explicitly.

2. **The win-rate field migrated from 0.77/0.80 (W18) → 1.00 (early May) → 0.40–0.78 (mid May).** This is not a model improvement — it is a *backtest-window drift* as recent winners overweighted, then the regime turned slightly choppier and the rolling backtest reverted. Phase 3 must compare the **claimed** win rate at each point against the **realised** outcome rather than the win rate the report would have quoted with hindsight.

JSONL companion file: `phase_1_inventory.jsonl`.
