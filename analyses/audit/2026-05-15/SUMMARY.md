# Calibration Audit — 2026-05-15

*Window: 2026-04-30 → 2026-05-15. Dataset: 12 daily reports + 3 weekly reports = 15 reports, 205 trade rows extracted, 132 with price coverage, 52 fully resolved on 3D and not skipped. Regime: TRANSITIONAL/UPTREND throughout — every finding below is regime-conditioned and may not generalize to a bear or risk-off tape.*

## Top 3 schema flaws

1. **`multi_day_sweep` quoted at 0.71 WR, realised 0.33 (n=6) — the worst-calibrated single class in the dataset.** Persistent index/mega-cap sweep flow is institutional hedging on long books, not directional bets; the rubric treats it as directional. Phase 4 cite. Patch P1.1 (filter index/mega-cap sweeps unless `cum_premium_flow` aligns).
2. **`flow_conflict` -2 deduction is narrative-only — missed-gate rate 30%.** Three of ten cases on 2026-05-08 should have triggered −2 but were noted in prose without affecting the numeric score. Phase 6 cite. Patch P0.1 (mechanize flow_conflict deduction).
3. **`claimed_win_rate=1.00` quoted across the entire 2026-05-08 HIGH-tier book on backtests of n<20.** Realised 0.64–0.75. Brier score 0.45 on that single date. Phase 3 cite. Patch P0.2 (cap WR at 0.75 when backtest n<10, 0.85 when n<20).

## Top 3 tool-tier surprises

1. **`hot_chains_sweep_persistence` is NEGATIVE (−24.0pp marginal contribution, n=13).** The single worst-performing tool in the rubric. Demote from positive scoring on swing horizon (P1.1). Phase 4 cite.
2. **`dark_pool_block_stratified` is the single best discriminator (+27.8pp on `dark_pool_accumulation`, n=21).** Beats every other tool including `historical_cumulative_premium_flow` (+24.2pp). Promote to required citation, weight from +2 to +3. Phase 4 + P1.2 cite.
3. **`options_flow_sector_flow_persistence` field is broken.** Returned uniform persistence_score=1 across all 11 sectors for most of the audit window; agents extracted rotation signal manually from `net_flow_by_day` instead. Marginal contribution −11.0pp because the field is uninformative. Patch P2.3 — re-introduce only after the upstream MCP field is fixed.

## What we'd do Monday

The calibration is honest at the top — HIGH-tier (raw ≥10 under proposed cuts) realised 0.85 win-rate, and the LOAD-BEARING tool quartet (`dark_pool_block_stratified`, `historical_cumulative_premium_flow`, `insights_institutional_accumulation`, `options_structure_dex`) is doing exactly what we expect institutional positioning to do. The system is profitable. The miscalibration is in the middle of the score distribution and in the WR field — every quoted 1.00 win-rate is a backtest-window artifact, every persistent index put-sweep is a hedge masquerading as a directional short, and every unconfronted flow_conflict is a thesis that the tape is already disagreeing with. Apply the three P0 patches before next Monday's `/daily-analysis` run, harden the LB-gate to 3-of-4 (P1.3), and we'd expect Brier to drop from 0.218 to ≈0.184 with no overfit penalty (Phase 5 holdout test passed). Don't extrapolate any of these calibrations to a non-TRANSITIONAL regime — the dataset has zero risk-off prints, and `bearish_flow` realised 0.17 in this tape would print very differently in a regime where the index actually rolls over.
