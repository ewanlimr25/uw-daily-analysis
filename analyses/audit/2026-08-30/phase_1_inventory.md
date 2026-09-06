# Phase 1 — Inventory & Parse (2026-08-30)

**13th calibration audit.** Threshold check: **85 daily / 18 weekly reports** vs the 10-daily-OR-3-weekly
floor. **PASS** — no `DATASET-SIZE-RELAXED` banner. `uw historical available-dates` latest darkpool
date = **2026-08-28**, identical to the newest report date ⇒ truth set is not stale.

## Provenance basis (C23)

**100% verbatim decision-envelope.** 789 rows parsed from **82 `decision.json` sidecars**
(68 daily + 14 weekly). **82/82 pass `scripts/validate_decision.py`** — zero schema failures,
zero cross-field invariant failures. **Zero rows reconstructed from prose.** Under C23 this
lifts the P0 provenance cap: findings resting on these citations may be rated P0 if they
also clear cross-regime + BH.

| | this cycle | prior (08-22) | Δ |
|---|---|---|---|
| envelope rows | **789** | 737 | +52 |
| envelopes | **82** | 76 | +6 |
| unique tickers | **192** | 185 | +7 |
| `Σ score_components.points ≠ raw_score` | **0** | 0 | — |
| validator failures | **0/82** | 0/76 | — |

New material since the last audit: `analyses/daily/2026-08-{24,25,26,27,28}` and
`analyses/weekly/2026-W35` — **52 new rows** (48 DROP, 4 LOW; 23 short / 12 long / 15 vol / 2 neutral).

## Rubric-era stratification (never pooled — 2026-06-12 P0.1)

| era | rows |
|---|---|
| **`2026-06-12` (FROZEN)** | **638** |
| `era_0530_0605` | 69 |
| `era_0525_0529` | 54 |
| `pre_freeze_post_0606` | 28 |

Post-freeze rows **638** (was 586). `OUT-OF-REGIME` half-cap rows: **44**.

## Regime diversity (the cross-regime bar)

| regime bucket | rows |
|---|---|
| uptrend | 338 |
| transitional / other | 211 |
| pullback-in-uptrend | 159 |
| choppy | 81 |

Four buckets, none dominant — **6th cross-regime cycle**. The single-regime caveat that
capped 2026-06→07 findings does not apply.

## Composition

- **Horizon** — swing 561, vol 212, LEAP 16.
- **Section** — watch_only 343, swing_short 140, swing_long 133, vol_short 112, vol_long 52, leap_disqualified 7, leap 2.
- **Tier** — DROP 629, LOW 133, MEDIUM 20, HIGH 7. Post-freeze: **DROP 567 / LOW 71 / MEDIUM 0 / HIGH 0**.
- **Final size** — skip 397, watch_only 333, starter 35, half 12, veto 11, **full 1**.
- **Fundamentals verdict** — NA 253, absent 239, CAUTION 142, CONFIRM 125, VETO 30.
- **Signal class (top)** — earnings_vol 156, bearish_flow 150, multileg_directional 109, bullish_flow 73,
  dark_pool_accumulation 68, sector_rotation 48, high_iv_rank 35, oi_build 24, dealer_positioning 16.

## Instrumentation follow-through (prior-cycle fixes, graded)

1. **Citation atomicity (2026-08-15 P1 #1) — HOLDING, 2nd cycle.** Concatenated citation
   strings: pre-08-15 **8.8%** (108/1225) → 08-15…08-21 **0.0%** (0/134) → post-08-22
   **0.0%** (0/97). 231 consecutive atomic citations. No regression.
2. **`vol_long` canonicalization (2026-08-22 P1 #2) — HOLDING.** Off-list
   `dominant_signal_class` labels post-fix: **0 of 52 new rows**. Historical off-list total
   stays 35 (envelopes are correctly not rewritten). The 5 `vol_long` rows of 2026-08-18 are
   the last of the lineage; `vol_term_dislocation` now carries 6 new rows.

## Data-quality flags

- **Legacy prose coverage gap (unchanged, already resolved by prior audits):** 17 daily
  (2026-04-30 → 2026-05-22) and 4 weekly (W18–W21) reports predate the envelope and are
  excluded. They lack `score_components` / `win_rate` and cannot enter compliance or
  calibration denominators.
- **`win_rate_source` composition:** `NA(substrate)` 398, `backtest_clean` 151, `backtest` 84,
  `NA` 67, null 56, `fallback_proxy` 33. The 84 `backtest` + 33 `fallback_proxy` rows are
  **pre-quarantine substrate-contaminated quotes** (era-banded, down-weighted in Phase 3).
- **266 rows carry a non-null `claimed_win_rate`** — the Brier / log-loss / reliability
  denominator.
- **675 rows carry `score_components`** (535 post-freeze) — the Phase 4/5/6 denominator.

## Outputs

- `phase_1_inventory.jsonl` — 789 normalized rows.
- `_tickers.json` — 192-ticker universe for the Phase-2 OHLC fetcher.
