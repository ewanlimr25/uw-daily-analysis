# Phase 1 — Inventory & Parse (2026-08-15)

**11th calibration audit.** Dataset threshold cleared without relaxation: **75 daily / 16 weekly**
reports on disk (floor is 10 daily OR 3 weekly). No `DATASET-SIZE-RELAXED` banner applies.

## Source: structured decision envelopes (authoritative)

| | reports on disk | `decision.json` present | validate clean |
|---|---|---|---|
| daily | 75 | 58 | 58 / 58 |
| weekly | 16 | 12 | 12 / 12 |
| **total** | **91** | **70** | **70 / 70** |

`scripts/validate_decision.py` run over all 70 envelopes: **zero failures**. No report fell back
to prose parsing. Envelope coverage runs `2026-05-25 → 2026-08-14` (daily) and `2026-W22 → 2026-W33`
(weekly).

**Coverage gap (known, not new):** 17 daily reports (`2026-04-30 → 2026-05-22`) and 4 weeklies
(`W18–W21`) predate the envelope schema and are prose-only legacy. They carry no
`score_components` / `win_rate` / `rubric_version` and are excluded from every calibration,
tier and tool table below. They were resolved by the 2026-05-09/05-15 audits and are not
re-derived here.

## Extraction

**672 rows** (one per `report_date × ticker × kind`), up from 626 at the 2026-08-08 audit —
**+46 new rows** across 5 new sessions (`2026-08-10 … 2026-08-14`). 179 unique tickers.

| dimension | breakdown |
|---|---|
| kind | daily 599 · weekly 73 |
| horizon | swing 493 · vol 168 · LEAP 11 |
| section | watch_only 326 · swing_long 112 · swing_short 109 · vol_short 87 · vol_long 34 · leap_disqualified 3 · leap 1 |
| tier | DROP 523 · LOW 122 · MEDIUM 20 · HIGH 7 |
| direction | long 272 · short 201 · vol_short 112 · neutral 44 · vol_long 43 |
| final_size | skip 315 · watch_only 300 · starter 35 · half 12 · veto 9 · **full 1** |
| fundamentals verdict | NA 224 · (absent) 193 · CAUTION 117 · CONFIRM 114 · VETO 24 |

### Rubric-era stratification (never pooled — schema ≥1.3 / era-banded)

| era | rows |
|---|---|
| **`2026-06-12` (FROZEN)** | **521** |
| `era_0530_0605` | 69 |
| `era_0525_0529` | 54 |
| `pre_freeze_post_0606` | 28 |

**Post-freeze tier distribution: 461 DROP / 60 LOW / 0 MEDIUM / 0 HIGH.** All 7 HIGH and all
20 MEDIUM rows in the entire corpus are *pre-freeze*. This is the ninth consecutive cycle in
which the frozen rubric has produced no MEDIUM or HIGH call — see Phase 5 for the freeze-lift
consequence.

### Regime coverage (the cross-regime requirement)

| bucket | rows |
|---|---|
| uptrend | 258 |
| transitional_other | 203 |
| pullback_in_uptrend | 130 |
| choppy | 81 |

`out_of_regime` (P0.6 half-cap active): **44 rows** (30 DROP / 14 LOW). The 5 new sessions are
39 uptrend / 7 transitional — this window is a **rising tape**, which matters for every
excess-column reading in Phase 3 (C49).

### Signal classes (top of the long tail)

`bearish_flow` 129 · `earnings_vol` 125 · `multileg_directional` 94 · `bullish_flow` 69 ·
`dark_pool_accumulation` 62 · `sector_rotation` 43 · `high_iv_rank` 30 · `oi_build` 17 ·
`multi_day_sweep` 13 · `dealer_positioning` 12 · `gamma_breakout` 11 · `event_vol` 11 ·
`opex_pin` 9 · `leap_directional` 8 · `dealer_positioning_flip` 7 — then 16 singleton/near-
singleton classes (`dealer_short` 4, `vanna_squeeze` 4, and 12 classes at n≤2).

## Provenance basis (governs Phase 4 / Phase 7 priority caps — C23)

- **569 / 672 rows (84.7%) carry verbatim `score_components[].source_tool`** read directly from
  the envelope. **Zero rows** in this audit used prose-reconstructed citations.
- `Σ score_components.points == raw_score`: **0 violations across 569 scored rows.**
- 241 rows carry a `claimed_win_rate`.
- `win_rate_source`: `NA(substrate)` 306 · `backtest_clean` 126 · `backtest` 84 · `NA` 67 ·
  (absent) 56 · `fallback_proxy` 33.

Verbatim provenance means Phase 4 tool findings are **not** priority-capped at P1 by C23. The
remaining constraints on P0 (cross-regime, BH-surviving, n) still apply.

## Advisory `fz` / breadth coverage

`fz_squeeze_pressure` present on 201 rows · `fz_short_float_pct` 147 · `fz_recom` 78 ·
`breadth_cross_check` 654. Gate-verdict key universe: `cluster, debate, event_risk, excess,
fundamentals, panic, regime, rubric_regime, sector, vrp` — 10 gates, unchanged.

## Data-quality flags

1. **`BRKB` and `SPX` have no Yahoo chart history** (404 / no `timestamp` field). Both resolve
   INCONCLUSIVE `data_unavailable` in Phase 2 — never LOSS. 177 / 179 tickers fetched with real
   OHLC; SPY through `2026-08-14`, 85 bars, `real_ohlc: True`.
2. **`insider_cluster_flag` is absent from the gate-verdict key union entirely** — carried as a
   `fz`/envelope field, not a gate. Its zero-variance problem (15 observations, all `False`) is
   re-tested in Phase 4/6.
3. **No duplicate `(date, ticker, kind)` rows; no null tickers.** Parser integrity clean.
4. **`vol` horizon is 168 rows but `implied_move` is not carried per-call** — those resolve on
   RV-direction proxy and are tagged `rv_direction_proxy` (C: never treated as calibrated
   IV-vs-RV outcomes).
5. **31 signal classes, 16 of them at n ≤ 4.** The long tail is class-label drift
   (`dealer_positioning_flip` / `dealer_flip` / `dex_flip_long` / `dealer-positioning_dex_flip`
   are four labels for one mechanism). Flagged for Phase 7; they fall below the C23 decided-N ≥ 8
   floor individually and therefore never reach the headline table.

**Output:** `phase_1_inventory.jsonl` (672 rows) · `_tickers.json` (179) · `_ohlc/` (177 symbol
files) · `_ohlc_manifest.json`.
