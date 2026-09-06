# Calibration Audit — 2026-05-23

Second audit cycle. The 2026-05-15 P0 patches landed in production (commit `83cc148`); this cycle measures what they fixed and what they didn't, on 73 newly-resolved calls across 17 daily + 4 weekly reports.

## Top 3 schema flaws

1. **Tier inversion detected: HIGH 60.0% < MED 62.5% realised WR (n=49).** The 3-of-4 load-bearing-tool gate filters working calls (AAPL, TLT, MSFT — all demoted to MED, all won) and leaves narrative-only HIGH scores (MA, MU-short, BL — all stayed HIGH, all lost). Phase 3 cite. **Patch P0.2** — add `insights_signal_confluence` to the LB set; require 3-of-5.

2. **`historical_signal_backtest` MCP tool returns empty for every queried signal class** (`dark_pool_accumulation`, `bullish_flow`, `bearish_flow`, `volume_spike`, `high_iv_rank`). The tool `signal-confluence-quant` cites for `win_rate` is non-functional on the current MCP build. Every reported win-rate in the past month is agent-fabricated proxy. Phase 2 cite. **Patch P0.1** — document realised-WR fallback path.

3. **`hot_chains_sweep_persistence` remains in the rubric as +1.** The 2026-05-15 audit recommended deprecation; only mega-cap suppression rules were added. Tool is NEGATIVE −22pp across two audit cycles; `multi_day_sweep` class still claims 0.70 realises 0.43. Phase 4 cite. **Patch P0.3** — remove the +1; keep tool informational only.

## Top 3 tool-tier surprises

1. **`insights_signal_confluence` PROMOTED to LOAD-BEARING (+19.5pp, n=12).** Was SUPPORTIVE prior cycle; new W21 wins (HON, TTWO-short) closed the gap. Becomes the 5th LB-tool. Phase 4 cite.

2. **`insights_conviction_matrix` DOWNGRADED to NEGATIVE (−23pp, n=8) in non-LEAP context.** Was NO-INFO prior cycle. BL LEAP LOSS and MA HIGH LOSS both cited this tool. The DIRECTIONAL_LONG>70% threshold appears to be a top-pick mean-reversion fade signature. Keep as LEAP gate only. Phase 4 cite.

3. **`dark_pool_block_stratified` softened from +27.8pp to +21.8pp.** Still LOAD-BEARING; still the best single discriminator. But the top-precision tool is no longer untouchable — MA / BL / WMT losses all cited it. The "DP block + cum_flow alignment" pair is now the actual edge, not DP alone. Phase 4 cite.

## What we'd do Monday

Land the P0 stack as a single PR: (1) `signal-confluence-quant.md` gets a realised-WR fallback when the backtest tool returns empty, plus the 3-of-5 LB-gate including `insights_signal_confluence`; (2) the embedded rubric in `daily-analysis.md` and `weekly-analysis.md` drops the `+1 hot_chains_sweep_persistence` line; (3) `insights_conviction_matrix` becomes LEAP-only as a positive scorer. The mechanical flow_conflict −3 and the gate-output discipline patches from prior cycle are confirmed working (100% and 89% compliance respectively) — preserve those. Re-run `/calibration-audit` after one full week of post-patch reports (target 2026-05-30) to confirm tier monotonicity is restored on out-of-sample data.
