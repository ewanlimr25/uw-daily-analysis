# Phase 1 — Inventory & Parse (2026-08-01)

**9th calibration audit.** Provenance is **100% verbatim**: all 58 decision envelopes
(48 daily + 10 weekly) validate clean against `schemas/decision_envelope.schema.json`,
so every row below is read from `calls[]` — zero prose re-parsing, zero reconstructed
tool citations. Under C23 that lifts the P0 eligibility cap.

Threshold: 65 daily / 14 weekly reports on disk, far past the 10-daily floor. No
DATASET-SIZE-RELAXED banner.

## Corpus

| | |
|---|---|
| Envelopes parsed | **58** (48 daily, 10 weekly) — 58/58 validate clean |
| Call rows extracted | **578** (519 daily, 59 weekly) |
| Unique tickers | 160 |
| `Σ score_components.points ≠ raw_score` | **0** |
| Rows carrying `claimed_win_rate` | 221 |
| New since 2026-07-25 | 6 envelopes / 52 rows (07-27 → 07-31) |

## Stratification (never pooled)

| Rubric era | rows | note |
|---|---|---|
| `era_0525_0529` | 54 | pre-freeze |
| `era_0530_0605` | 69 | pre-freeze; raw-9 recorded MEDIUM (validator era-band) |
| `pre_freeze_post_0606` | 28 | post-cap, pre-freeze |
| **`2026-06-12` (FROZEN, live)** | **427** | the rubric actually in production |

| Regime bucket | rows |
|---|---|
| transitional_other | 190 |
| uptrend | 179 |
| pullback_in_uptrend | 128 |
| choppy | 81 |

`OUT-OF-REGIME` (P0.6 half-cap) rows: **44**.

## Distribution

- **Tier** — DROP 447, LOW 104, MEDIUM 20, HIGH 7. **Post-freeze: 385 DROP / 42 LOW /
  0 MEDIUM / 0 HIGH** — a 7th consecutive cycle in which the frozen rubric has emitted
  no HIGH and no MEDIUM call.
- **Horizon** — swing 429, vol 139, LEAP 10.
- **Section** — watch_only 301, swing_short 94, swing_long 85, vol_short 74, vol_long 20,
  leap_disqualified 3, leap 1.
- **Direction** — long 230, short 185, vol_short 99, neutral 36, vol_long 28.
- **Final size** — skip 269, watch_only 252, starter 35, half 12, veto 9, **full 1**.
- **Fundamentals verdict** — NA 183, CONFIRM 95, CAUTION 91, VETO 19, absent 190.
- **`win_rate_source`** — NA(substrate) 232, backtest_clean 106, backtest 84, NA 67,
  fallback_proxy 33, absent 56.

Top signal classes: `bearish_flow` 122, `earnings_vol` 106, `multileg_directional` 78,
`bullish_flow` 56, `dark_pool_accumulation` 55, `sector_rotation` 34, `high_iv_rank` 26.

## Data-quality flags

1. **Class-label fragmentation persists.** 31 distinct `dominant_signal_class` strings,
   of which 12 appear ≤2 times (`dealer-positioning_dex_flip`, `dex_flip_long`,
   `multileg_repeat`, `directional_conflict`, …). Phase 2 collapses these via
   `canonical_class`; the raw label field is still not enum-constrained in the schema.
2. **`dp_block_pct_of_float` (C16) is still absent from the schema** — the 2026-07-25
   P1 #5 recommendation was only half-applied. C16 is untestable for a **4th** audit.
3. `BRKB` and `SPX` have no Yahoo chart series (share-class ticker / index). 5 rows tagged
   `data_unavailable` → INCONCLUSIVE, never LOSS.
4. Legacy prose-only reports (pre-2026-05-25 daily, pre-W22 weekly) remain outside the
   envelope corpus — resolved by earlier audits, no `score_components`/`win_rate`.

## Applied-recommendation tracking (2026-07-25 → live)

Six envelopes were written *after* commit `c69a359` applied the 07-25 P0+P1 set. They are
tagged for the Phase 3/6 verification pass:

- `insider_cluster_flag` now present on **44/44** post-07-27 calls (was 20.1% corpus-wide).
- `debate_residuals` bin floor lowered 0.55 → 0.15 — **22 rows** now carry a sub-0.55
  residual that the old floor would have erased.
- `win_rate_source` = `backtest_clean` on **15/15** post-07-27 quoted rows.

Output: `phase_1_inventory.jsonl` (578 rows), `_tickers.json`, `phase1_parse.py`.
