# Phase 1 — Inventory & Parse (2026-07-18)

**Source: verbatim decision envelopes** (`decision.json` `score_components[]`) — not prose. Provenance is verbatim on every scored row; legacy prose-only reports (pre-2026-05-25 daily) predate the envelope and are a known coverage gap already resolved by prior audits.

## Coverage
- **463 call-rows** from **46 envelopes** (38 daily + 8 weekly). Up from 396 rows / 40 envelopes at 07-11 (+67 rows, +6 envelopes: dailies 07-13→07-17 + W29, plus late-June fills).
- **143 unique tickers**; 141 OHLC-resolved. 2 fetch failures — `BRKB` (Yahoo wants `BRK-B`; ticker-notation) and `SPX` (index, no chart endpoint) → both tag INCONCLUSIVE/`data_unavailable`, never LOSS.
- **0 `Σ score_components.points ≠ raw_score`** violations (validator-clean; 46/46 envelopes pass `validate_decision.py`).

## Rubric-era strata (never pooled)
| Era | Rows |
|---|---|
| **2026-06-12 (FROZEN)** | 312 |
| era_0530_0605 | 69 |
| era_0525_0529 | 54 |
| pre_freeze_post_0606 | 28 |

## Regime-bucket strata (new dimension since 06-27)
uptrend 171 · pullback_in_uptrend 128 · transitional_other 124 · choppy 40. **First cycle where the non-uptrend buckets (292) outnumber pure uptrend (171)** — the audit finally has real regime diversity.

## Tier / horizon / direction
- **Tier:** DROP 348 · LOW 88 · MEDIUM 20 · HIGH 7. **Post-freeze tier dist: DROP 286 / LOW 26 — ZERO HIGH, ZERO MEDIUM.** All 7 HIGH + 20 MEDIUM are pre-freeze.
- **Horizon:** swing 342 · vol 113 · LEAP 8.
- **Direction:** long 197 · short 139 · vol_short 80 · neutral 26 · vol_long 21.
- **Final size:** watch_only 219 · skip 193 · starter 34 · half 12 · veto 4 · **full 1**. The fleet sized 47 of 463 rows; it dropped/watched 90%.

## Signal-class distribution (top)
bearish_flow 95 · earnings_vol 80 · multileg_directional 60 · dark_pool_accumulation 52 · bullish_flow 51 · high_iv_rank 26 · sector_rotation 21 · multi_day_sweep 10 · dealer_positioning 9 · opex_pin 9 · oi_build 9.

## Data-quality flags
- `win_rate_source` breakdown: `NA(substrate)` 148 (post-quarantine frozen era — no numeric quote), `backtest` 84, `backtest_clean` 81, `NA` 62, none 55, `fallback_proxy` 33. **The frozen era carries no numeric `win_rate`** — calibration (Brier/log-loss) is computable only on the 178 pre-quarantine graded rows.
- Fragmented class labels (`dealer*`, `*distribution`, `single_leg_*`) collapsed via `canonical_class` in Phase 2.

Outputs: `phase_1_inventory.jsonl` (463 rows), `_tickers.json`.
