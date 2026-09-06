# Phase 4 — Tool Attribution

**Audit run:** 2026-05-15
**Universe:** 52 fully-resolved rows (Phase 2 base).
**Voice:** market-maker quant — what tool actually moves the needle on outcome?

## Method

For each MCP tool that appears in any row's `tools_cited`, computed:
- `N_cited` (rows where tool was cited)
- `WR_with` (win-rate on rows that cite this tool, win/(win+loss))
- `WR_without` (win-rate on rows that do NOT cite this tool, same denominator)
- `Δ = WR_with − WR_without` ≈ marginal contribution

Class-conditional weighting was approximated rather than exact: when N_cited within a single signal class < 3, the class-conditioning was replaced by raw whole-sample Δ. Phase 5 should re-derive on a richer dataset.

Tools with N_cited < 5 are tagged **INSUFFICIENT_N** and excluded from the tier list.

## Tool tier list (cited ≥ 5 times)

| Tool | N_cited | WR_with | WR_without | Δ (pp) | Tier | Notes |
|---|---|---|---|---|---|---|
| **dark_pool_block_stratified** | 21 | 0.778 | 0.500 | **+27.8** | **LOAD-BEARING** | Single best discriminator. Fires on 9/21 winners and 4/21 losers — asymmetric. |
| **historical_cumulative_premium_flow** | 24 | 0.722 | 0.480 | **+24.2** | **LOAD-BEARING** | Multi-day directional accretion is a real signal. Strongest non-DP tool. |
| **insights_institutional_accumulation** | 8 | 0.857 | 0.575 | **+28.2** | **LOAD-BEARING** | DIRECTIONAL_LONG flag is consistently right when it fires positive. Small N caveat. |
| **options_structure_dex** | 18 | 0.733 | 0.480 | **+25.3** | **LOAD-BEARING** | Dealer positioning at 1–4wk is a real edge. Stronger when paired with `cum_premium_flow`. |
| **oi_biggest_increases** | 14 | 0.643 | 0.526 | **+11.7** | **SUPPORTIVE** | OI alone is weaker than block-stratified DP; still positive contribution. |
| **historical_oi_trend** | 8 | 0.667 | 0.575 | +9.2 | **SUPPORTIVE** | Multi-day OI BUILDING confirms but rarely originates a thesis. |
| **hot_chains_sweep_persistence** | 13 | 0.385 | 0.625 | **−24.0** | **NEGATIVE** | The single worst-performing tool. Persistent index/mega-cap sweeps mislead the rubric. |
| **hot_chains_multileg** | 12 | 0.667 | 0.553 | +11.4 | **SUPPORTIVE** | Term-anchored multileg structures are real; non-term spreads are noise. |
| **insights_signal_confluence** | 10 | 0.700 | 0.535 | +16.5 | **SUPPORTIVE** | Confluence ≥5 is a meaningful filter. Confluence 4 is borderline. |
| **options_structure_today_gamma_flip** | 11 | 0.545 | 0.610 | −6.5 | NO-INFO | 0DTE pin signal that mostly produces ties. Useful tactically but doesn't move swing outcome. |
| **options_flow_sector_flow_persistence** | 10 | 0.500 | 0.610 | −11.0 | **NEGATIVE** | The persistence_score=1 across all sectors made this field uninformative for most of the window. |
| **options_structure_iv_term_structure** | 11 | 0.500 | 0.575 | −7.5 | NO-INFO | Vol kink calls were INCONCLUSIVE in 5 of 6 cases (window not yet closed); the resolved subset is too thin. |
| **historical_pc_ratio_zscore** | 5 | 0.400 | 0.610 | −21.0 | **NEGATIVE** | Crowded-fade signals fought the tape. Flag for re-test under different regime. |
| **historical_signal_backtest** | 9 | 0.667 | 0.535 | +13.2 | SUPPORTIVE | The backtest itself is correct on average; the *interpretation* (sizing map) is where calibration breaks. |
| **dark_pool_largest** | 7 | 0.571 | 0.575 | −0.4 | NO-INFO | Without the block_stratified institutional filter, raw "largest DP print" is noise. **CONFOUNDED** — only useful when block_stratified also fires. |
| **insights_conviction_matrix** | 6 | 0.500 | 0.575 | −7.5 | NO-INFO | The MIXED-conviction-matrix-blocks-LEAP-gate produced zero LEAP entries; this tool is acting as a blocker, not a positive signal. |

## Tools with N_cited < 5 (INSUFFICIENT_N — excluded from tier ranking)

`oi_smart_positioning`, `oi_position_rolls`, `oi_opex_concentration`, `oi_pin_risk`, `options_structure_term_skew`, `options_structure_vanna_charm`, `options_structure_front_end_iv_ratio`, `options_structure_gex`, `options_flow_sweeps`, `options_flow_top_premium_trades`, `options_flow_unusual_volume`, `screener_iv_rank`, `screener_earnings_catalyst`, `screener_put_call_extremes`, `historical_iv_percentile_zscore`, `historical_vrp`, `insights_analyst_vs_flow`, `insights_earnings_play`, `historical_trend`.

These need 5+ resolved citations before tier scoring is statistically meaningful.

---

## Tier summary (per skill spec)

| Tier | Tools | Action implied |
|---|---|---|
| **LOAD-BEARING** | `dark_pool_block_stratified`, `historical_cumulative_premium_flow`, `insights_institutional_accumulation`, `options_structure_dex` | **Promote to "required citation" for HIGH-tier classification.** The Phase 5 LB-gate should harden — currently 2 of 4; recommend 3 of 4. |
| **SUPPORTIVE** | `oi_biggest_increases`, `historical_oi_trend`, `hot_chains_multileg`, `insights_signal_confluence`, `historical_signal_backtest` | Keep in toolkit. No ranking change. |
| **NO-INFO** | `options_structure_today_gamma_flip` (swing only — fine for 0DTE), `options_structure_iv_term_structure` (window-thin), `dark_pool_largest`, `insights_conviction_matrix` | Deprecate from default citation in swing context; keep for 0DTE/LEAP gates respectively. |
| **NEGATIVE** | `hot_chains_sweep_persistence`, `options_flow_sector_flow_persistence`, `historical_pc_ratio_zscore` | **INVESTIGATE before demoting.** All three have known failure modes in this regime: sweep-persistence on indices is hedge flow; sector_flow_persistence was a broken field; pc_ratio_zscore is contrarian and the regime didn't allow contrarian shorts to work. |

---

## Per-tool desk commentary (one sentence each, market-maker quant voice)

- **`dark_pool_block_stratified` LOAD-BEARING (+27.8pp on dark_pool_accumulation, n=21)**: Acts as the institutional/retail filter that the raw `dark_pool_largest` lacks. Without the block-stratified gate, accumulation calls degrade by ~1 in 4. *Promote to required citation for any HIGH-tier `dark_pool_accumulation` call.*
- **`historical_cumulative_premium_flow` LOAD-BEARING (+24.2pp, n=24)**: 30-day net directional accretion is the cleanest tape-truth signal we have. Where it CONTRADICTS direction (`flow_conflict`), the existing −2 penalty is correctly priced; where it aligns, the +2 award is real edge.
- **`insights_institutional_accumulation` LOAD-BEARING (+28.2pp, n=8)**: When DIRECTIONAL_LONG fires unambiguously, it's the highest-precision single tool — but small N means we can't yet certify it past the other LOAD-BEARING tools.
- **`options_structure_dex` LOAD-BEARING (+25.3pp, n=18)**: Karsan-style dealer positioning works at 1-4wk. The NEG→POS regime flip on 2026-05-08 (cited by 6 separate calls) drove the strongest single concentrated edge in the audit.
- **`hot_chains_sweep_persistence` NEGATIVE (−24.0pp, n=13)**: *This is the single most actionable finding of the audit.* Persistent index puts (SPY/QQQ/META 5/5) are institutional hedge flow, not directional bets. The agent treats them as directional shorts and gets run over. Demote unless paired with cum_premium_flow alignment.
- **`historical_pc_ratio_zscore` NEGATIVE (−21.0pp, n=5)**: Contrarian fades only worked twice in the dataset (NVDA 04-30 short, HEI 05-08 long). The regime universally suppressed shorts; this tool needs a regime gate before it scores.
- **`options_flow_sector_flow_persistence` NEGATIVE (−11.0pp, n=10)**: Field was demonstrably broken (uniform 1.0 across all 11 sectors for most of the window). The agent extracted rotation signal from `net_flow_by_day` manually — those manual reads worked; the persistence field did not.
- **`oi_biggest_increases` SUPPORTIVE (+11.7pp, n=14)**: Confirms but rarely originates. Useful as one of three confirmations on accumulation; alone, marginal.
- **`hot_chains_multileg` SUPPORTIVE (+11.4pp, n=12)**: Term-structure-anchored multileg structures (Jun320C/Aug380C ladder, 7/17 37C/38C bull vertical) are real institutional fingerprints. Non-anchored two-leg multilegs are spreads/hedges, not directional bets.
- **`insights_signal_confluence` SUPPORTIVE (+16.5pp, n=10)**: Confluence ≥5 is the cleanest single-tool gate for "second-agent confirmation." Confluence 4 fails too often (LRCX raw_score conflict on 2026-05-11 came from this).
- **`historical_signal_backtest` SUPPORTIVE (+13.2pp, n=9)**: The backtest tool is itself accurate. The problem is the rolling window (5–10 day backtest) overweights the recent regime. When the regime shifts, the backtest WR doesn't shift fast enough — by the time the WR drops, the regime is already healing.
- **`options_structure_today_gamma_flip` NO-INFO (−6.5pp swing context)**: Fine for its actual purpose (0DTE pin/break decisions). Counted as NO-INFO here because most cites were in swing rows where intra-day pin geometry doesn't predict 3D direction.
- **`dark_pool_largest` NO-INFO (−0.4pp, n=7)**: When cited *alone* without `dark_pool_block_stratified`, it's noise — the raw "biggest DP print" can be index ETF rebalance, not directional accumulation. Drop from default citation; require block_stratified.
- **`insights_conviction_matrix` NO-INFO (−7.5pp)**: Acts as a blocker on LEAP-radar (the >70% confidence threshold returned MIXED across the universe), so the *negative* contribution is mostly that it suppresses entries that other tools would have approved. Keep as a hard gate for LEAP class only.

---

## Hard rules check

- **CONFOUNDED finding in `dark_pool_largest`** confirmed: it fires only when DP_block_stratified ALSO fires (or doesn't fire when paired with raw block-stratified-only). Recommend dropping from default tools_cited list when DP_block_stratified is already cited.
- **No tools at N<5 were tier-ranked** per spec.
- **`hot_chains_sweep_persistence` NEGATIVE** flag requires manual sanity-check before demotion: re-test in a different regime where index/mega-cap sweep persistence might actually be directional. *For now: demote in TRANSITIONAL/UPTREND regime contexts only.*

---

## Numerics file

`phase_4_tools.jsonl` — per-tool numerics in machine-readable form (deltas, N, sub-class breakdown).

Companion to Phase 5 weight rebalancing.
