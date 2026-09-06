# Phase 1 — Inventory & Parse

> **DATASET-SIZE-RELAXED**: 7 daily reports + 2 weekly reports, below the default min_dataset thresholds (10 daily OR 3 weekly). All downstream calibration math is noise-dominated; conclusions are flagged structural / qualitative throughout.

*Generated 2026-05-09. Total ticker-calls extracted: **131**.*

---

## Coverage

| Source | Count | Date Range |
|---|---|---|
| Daily reports | 7 | 2026-04-30 → 2026-05-08 |
| Weekly reports | 2 | 2026-04-27 (W18), 2026-05-04 (W19) |
| **Total calls** | **131** | |

## Call counts by horizon

| Horizon | N |
|---|---|
| swing | 110 |
| weekly | 17 |
| LEAP | 4 |

## Call counts by section

| Section | N |
|---|---|
| swing_long | 75 |
| swing_short | 18 |
| vol_long | 16 |
| vol_short | 16 |
| leap | 3 |
| leap_disqualified | 2 |
| sweep_top | 4 (legacy 2026-04-30) |

## Call counts by dominant signal class

| dominant_signal_class | N |
|---|---|
| dark_pool_accumulation | 23 |
| bullish_flow | 26 |
| earnings_buy_vol | 11 |
| earnings_sell_vol | 12 |
| contrarian_fade | 9 |
| dealer_positioning_flip | 11 |
| multi_day_sweep | 6 |
| multileg_directional | 5 |
| gamma_breakout | 4 |
| vol_kink_long | 8 |
| bearish_flow | 5 |
| leap_directional | 5 |
| earnings_directional_short | 2 |
| vol_kink_short | 1 |
| (legacy / null) | 3 |

## Format coverage gaps

The first two daily reports (`2026-04-30.md`, `2026-05-01.md`) **predate** the formal `score_components` audit-trail format introduced in `2026-05-04.md`. 23 calls (~17.6% of the dataset) carry `legacy_format=true` and lack:

- `raw_score` (the +3/+2/+1 breakdown)
- `score_components[]` (per-point provenance)
- `claimed_win_rate` (the backtest-derived sizing input)

Phase 6 (decision-process audit) excludes these from compliance-rate denominators. Phase 4 (tool attribution) keeps them — the `tools_cited` field is recoverable from the body of the report even when the audit-trail row is absent.

## Data-quality flags

1. **GOOG / GOOGL ambiguity (W18 weekly + 2026-05-07 daily)**: GOOG and GOOGL are scored separately. On 2026-05-07 they explicitly diverge — GOOG raw=9 / GOOGL raw=5 with a $120M 30d net flow split — and the report calls out the class-share noise. The audit treats them as distinct rows, but desk reviewers should expect aggregate exposure analysis to lift one and flag the other as duplicate.
2. **AMZN double-counted on 2026-05-04**: appears once as `swing_long` (raw=4) and once as `leap` (raw=4) for the same Jan-27 250/300 LEAP block. Both rows kept; outcome resolution will use horizon-matched windows so they don't bias the same way.
3. **AAPL Apr-30 contradictory signals**: simultaneously HIGH-conviction accumulation candidate (in W18 weekly retro, ranked WIN +6.0%) AND HIGH-conviction contrarian fade in the 2026-04-30 report. The fade entry was sized starter / call credit spread — non-conflicting structurally, but worth noting.
4. **NVDA flip-flop**: NVDA flagged HIGH-conviction SHORT (contrarian) on 2026-04-30 and 2026-05-01, then HIGH-conviction LONG (raw=11–13) on 2026-05-07 → 2026-05-08, then SHORT-AND-LONG on 2026-05-08 (raw=10 long with flow_conflict gate, simultaneously down-graded to starter). Outcome resolution will key on the entry-date direction for each row independently.
5. **Single-row legacy sweep extracts (2026-04-30)**: AMZN/GOOGL/SLB/PAGP shown only as sweep-tracker callouts without a structure or invalidation in the report — outcomes resolvable by ticker direction but no R-multiple defined. Phase 2 will use 0.5×ATR(14) as the default R, per skill spec.
6. **VOL trade direction confusion**: A few vol_long rows (e.g. AAPL 2026-05-04 weekly cell) are actually `vol_short` (iron condor). Phase 1 took the report's own labeling; Phase 2 will resolve against `realised_vol` vs `implied_move`, so mislabeling is recoverable downstream.

## High-conviction (raw_score ≥ 5) population

41 calls. Counts by ticker (top 10):

| Ticker | High-conv calls | Note |
|---|---|---|
| AAPL | 6 | Most frequent; 4 LONG, 2 ambiguous |
| AMD | 5 | All LONG; correlation cluster recurring |
| TSLA | 4 | 3 LONG (later week), 1 SHORT (2026-05-01) |
| NVDA | 4 | 2 LONG, 2 SHORT — direction flipped mid-window |
| ORCL | 4 | All LONG |
| SHOP | 3 | 1 LONG raw=4 (close to threshold), 2 raw≥5 LONG |
| AMZN | 3 | 2 LONG swing + 1 LEAP |
| QCOM | 1 | raw=12 (highest single-name score in dataset) |
| MSTR | 2 | LONG; cluster-gated |
| MU | 3 | LONG (raw=8) and SHORT (raw=4) — direction inverted same week |

## Conviction-tier coverage

The early reports (Apr 30, May 1, May 4) used a *narrow* 0–3 raw-score range, which produces a tier distribution skewed to LOW. From May 6 onward the rubric expanded its cumulative_premium_flow component (+2 weight) and the dealer-positioning-strategist agent (+3 weight), enabling raw scores up to 13.

This **is itself an audit finding**: scores from May 6+ are not directly comparable to scores from Apr 30 / May 1 because the underlying rubric expanded. Phase 5 (schema critique) and Phase 6 (decision audit) must control for this — the rubric is a moving target across the dataset.

---

## Hand-off to Phase 2

`phase_1_inventory.jsonl` is the truth set. Phase 2 reads it row-by-row and resolves outcomes against the horizon map:
- 0DTE → same-day close (no rows in this dataset; 0DTE plays were not extracted as standalone calls — they're embedded in §2 of each report and don't have a structure-and-invalidation that resolves cleanly to WIN/LOSS)
- swing → 3D + 10D
- LEAP → 30D + 90D
- weekly → 5D + 10D

INCONCLUSIVE assignment when (a) trend_analyzer cannot resolve, (b) the 3D and 10D windows disagree on direction without 10D being decisive, (c) the call's invalidation triggered intra-window without a +1R move first.

The skill spec mandates outcomes be path-aware: a +2% gain after a -1.5% drawdown is a LOSS or INCONCLUSIVE, not a WIN.
