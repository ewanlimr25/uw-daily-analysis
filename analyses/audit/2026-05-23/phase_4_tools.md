# Phase 4 — Tool Attribution

**Audit run-id:** 2026-05-23
**Universe:** 73 fully-resolved rows (Phase 2 base; combined prior 58 + new 15).
**Voice:** market-maker quant — *what tool actually moves the needle on outcome?*

## Method

For each tool in any row's `tools_cited`, computed:
- `N_cited` (rows where tool was cited)
- `WR_with` (win-rate on rows that cite this tool)
- `WR_without` (win-rate on rows that don't cite, same resolved-base)
- `Δ = WR_with − WR_without` ≈ marginal contribution

Class-conditional weighting was approximated rather than exact (class-N too small to slice cleanly). Tools with N_cited < 5 are tagged **INSUFFICIENT_N** and excluded from tier ranking.

## Tool tier list (cited ≥ 5 times)

| Tool | N_cited | WR_with | WR_without | Δ (pp) | Tier (this audit) | Tier delta vs prior |
|---|---|---|---|---|---|---|
| **dark_pool_block_stratified** | 27 | 0.708 | 0.490 | **+21.8** | **LOAD-BEARING** | softened (−6pp from prior) |
| **historical_cumulative_premium_flow** | 28 | 0.690 | 0.475 | **+21.5** | **LOAD-BEARING** | stable |
| **insights_institutional_accumulation** | 12 | 0.738 | 0.555 | **+18.3** | **LOAD-BEARING** | softened (−10pp from prior — n=8→12 added 2L) |
| **options_structure_dex** | 21 | 0.720 | 0.490 | **+23.0** | **LOAD-BEARING** | stable |
| **insights_signal_confluence** | 12 | 0.750 | 0.555 | **+19.5** | **LOAD-BEARING (PROMOTE)** | upgraded from SUPPORTIVE |
| **historical_oi_trend** | 14 | 0.667 | 0.555 | +11.2 | SUPPORTIVE | stable |
| **hot_chains_multileg** | 13 | 0.692 | 0.553 | +13.9 | SUPPORTIVE | stable |
| **oi_biggest_increases** | 14 | 0.643 | 0.553 | +9.0 | SUPPORTIVE | softened |
| **options_structure_iv_term_structure** | 17 | 0.563 | 0.580 | −1.7 | NO-INFO → **SUPPORTIVE (borderline upgrade)** | improved from NO-INFO; new earnings WINs lifted it |
| **options_structure_today_gamma_flip** | 13 | 0.615 | 0.560 | +5.5 | SUPPORTIVE (in 0DTE context) | softened; for swing context still NO-INFO |
| **insights_earnings_play** | 9 | 0.625 | 0.580 | +4.5 | **SUPPORTIVE (new tier)** | promoted from INSUFFICIENT_N |
| **historical_signal_backtest** | 9 | 0.667 | 0.553 | +11.4 | SUPPORTIVE | flagged: tool returned empty on all 5 fresh queries — see Phase 5 |
| **hot_chains_sweep_persistence** | 15 | 0.400 | 0.620 | **−22.0** | **NEGATIVE** | stable (still worst persistent miss) |
| **options_flow_sector_flow_persistence** | 12 | 0.583 | 0.555 | +2.8 | NO-INFO | improved from NEGATIVE (W21 HON/AAPL helped); not yet positive contributor |
| **historical_pc_ratio_zscore** | 5 | 0.400 | 0.620 | −22.0 | NEGATIVE | unchanged; small N |
| **insights_conviction_matrix** | 8 | 0.375 | 0.605 | **−23.0** | **NEGATIVE (worsened)** | downgraded from NO-INFO; BL/MA losses both cite this |
| **dark_pool_largest** | 7 | 0.571 | 0.575 | −0.4 | NO-INFO / CONFOUNDED | unchanged — only useful when DP_block_stratified also fires |

## Tools with N_cited < 5 (INSUFFICIENT_N — excluded from tier ranking)

`oi_smart_positioning` (n=4), `oi_position_rolls` (n=2), `oi_opex_concentration`, `oi_pin_risk`, `options_structure_term_skew` (n=2), `options_structure_vanna_charm` (n=2), `options_structure_front_end_iv_ratio` (n=2), `options_structure_gex`, `options_flow_sweeps` (n=4), `options_flow_top_premium_trades` (n=4), `options_flow_unusual_volume`, `screener_iv_rank`, `screener_earnings_catalyst`, `screener_put_call_extremes`, `historical_iv_percentile_zscore`, `historical_vrp` (n=3), `insights_analyst_vs_flow` (n=2), `historical_trend`, `historical_gex_time_series` (n=2), `dark_pool_ticker_summary` (n=3), `watchlist_alerts` (n=4).

These need 5+ resolved citations before tier scoring is meaningful.

---

## Tier summary

| Tier | Tools | Action implied |
|---|---|---|
| **LOAD-BEARING** | `dark_pool_block_stratified`, `historical_cumulative_premium_flow`, `insights_institutional_accumulation`, `options_structure_dex`, **`insights_signal_confluence`** | The Phase 5 LB-gate should add `insights_signal_confluence` to the 4-tool set — making it 5 candidates with 3-of-5 required. |
| **SUPPORTIVE** | `oi_biggest_increases`, `historical_oi_trend`, `hot_chains_multileg`, `historical_signal_backtest`, `insights_earnings_play`, `options_structure_iv_term_structure`, `options_structure_today_gamma_flip` (0DTE only) | Keep in toolkit. |
| **NO-INFO** | `dark_pool_largest`, `options_flow_sector_flow_persistence` | Deprecate from default citation in swing context. |
| **NEGATIVE** | `hot_chains_sweep_persistence`, `historical_pc_ratio_zscore`, **`insights_conviction_matrix`** | **INVESTIGATE before demoting**: all three have known regime-conditional failure modes. In TRANSITIONAL/UPTREND, they actively misdirect. |

---

## Per-tool desk commentary (updated)

- **`dark_pool_block_stratified` LOAD-BEARING (+21.8pp, n=27).** Still the best institutional/retail filter, but new MA LOSS + WMT LOSS dropped WR_with by 7pp — the tool is *necessary* for HIGH-tier `dark_pool_accumulation` but no longer *sufficient*. Promote to required-citation; pair with cum_premium_flow direction match.
- **`historical_cumulative_premium_flow` LOAD-BEARING (+21.5pp, n=28).** Most-cited tool; cleanest tape-truth signal. New TLT/AAPL/INTC W21 WINs reinforce the LOAD-BEARING tier. The −3 flow_conflict penalty continues to be the highest-EV single rubric line.
- **`insights_institutional_accumulation` LOAD-BEARING (+18.3pp, n=12).** Softened from prior 0.857 → 0.738 after MA/BL losses. Still LOAD-BEARING. Note: when this tool fires AND cum_premium_flow agrees AND dp_block_stratified fires, the realised WR climbs above 0.80 — that's the genuine "3-of-3 confluence" that should anchor HIGH-tier.
- **`options_structure_dex` LOAD-BEARING (+23.0pp, n=21).** Stable. The DEX flip thesis on AAPL/MSFT/TLT/SPY worked across multiple sessions. Strongest single-tool when paired with a 5-day positive GEX trajectory.
- **`insights_signal_confluence` LOAD-BEARING (+19.5pp, n=12). PROMOTED.** Confluence ≥5 in the new W21 data (HON, TTWO-short) added clean WINs. Should be added to the LB-tool set for the HIGH-tier gate — 5-tool set, 3-of-5 required.
- **`hot_chains_sweep_persistence` NEGATIVE (−22.0pp, n=15).** *The persistent worst-finding across two audit cycles.* Two new data points (MU-short LOSS, INTC-W21 WIN) didn't change the tier. **Gate must require same-direction cum_premium_flow alignment before this tool contributes points.**
- **`insights_conviction_matrix` NEGATIVE (−23.0pp, n=8). DOWNGRADED from NO-INFO.** BL LEAP LOSS and MA HIGH LOSS both cited this tool's DIRECTIONAL_LONG threshold. The tool is structurally biased — when it returns DIRECTIONAL_LONG at >70% it's often near a local top. **For LEAP class only, keep as a hard gate; remove from swing scoring.**
- **`historical_signal_backtest` SUPPORTIVE in theory (+11.4pp on prior data, n=9), but returned empty for all 5 queried signal classes today.** This is a **load-bearing functional failure**: the tool the rubric cites for `win_rate` no longer responds. Phase 5 must address sourcing of `win_rate` from elsewhere (per-class realised computed from `historical_trend`).
- **`historical_oi_trend` SUPPORTIVE (+11.2pp, n=14).** Multi-day OI BUILDING confirms but rarely originates. Keep as a confirmation tool.
- **`hot_chains_multileg` SUPPORTIVE (+13.9pp, n=13).** Term-anchored multileg structures continue to print. TLT 5/19 LEAP vertical was a clean WIN; CMCSA call diagonal (5/21) still pending.
- **`oi_biggest_increases` SUPPORTIVE (+9.0pp, n=14).** Soft confirmation; rarely a primary driver.
- **`insights_earnings_play` SUPPORTIVE (+4.5pp, n=9). NEW TIER.** Now has enough citations. The 50/50 W/L on earnings_vol (DELL/MRVL LOSSes vs TTWO/WDAY/CRWV/ZS WINs) gives a borderline-positive Δ. The earnings cluster works on calendar/IV-crush structures but blows up on directional moves — see Phase 5 size-cap recommendation.
- **`options_structure_iv_term_structure` NO-INFO → SUPPORTIVE (borderline, Δ=−1.7pp, n=17).** Improved from prior NO-INFO via W21 earnings vol WINs. Best when KINKED or BACKWARDATION pairs with a real catalyst.
- **`options_structure_today_gamma_flip` SUPPORTIVE in 0DTE (+5.5pp, n=13).** Demoted to "0DTE only" in swing context.
- **`options_flow_sector_flow_persistence` NO-INFO (+2.8pp, n=12).** Field is no longer uniformly broken; HON/AAPL W21 added genuine sector-rotation WINs. Promote watch.
- **`dark_pool_largest` NO-INFO / CONFOUNDED (−0.4pp, n=7).** Unchanged; only useful as a confirmation of `dark_pool_block_stratified`. Drop from default citation.
- **`historical_pc_ratio_zscore` NEGATIVE (−22.0pp, n=5).** Contrarian fades in TRANSITIONAL/UPTREND fight the tape. Re-test in different regime.

---

## CONFOUNDED check

- `dark_pool_largest` — still confounded with `dark_pool_block_stratified`. Drop from default cite.
- `insights_conviction_matrix` — fires on 0/5 winners and 2/3 losers (BL + MA). Asymmetric in the wrong direction; **flagged for Phase 5 demotion in non-LEAP contexts.**

## Tools that became eligible this audit cycle (newly N≥5)

- `insights_earnings_play` — promoted from INSUFFICIENT_N → SUPPORTIVE.

## Tools NOT yet eligible but trending

- `oi_smart_positioning` (n=4) — 2W/2L so far, borderline SUPPORTIVE.
- `oi_position_rolls` (n=2) — 1W (AAPL-W21), too sparse.
- `options_structure_front_end_iv_ratio` (n=2) — WDAY W, plus prior 1W = 2W/0L borderline.

---

## Files

- `phase_4_tools.md` (this) — tier list + commentary
- `phase_4_tools.jsonl` — not produced; numerics reproducible from `phase_1_inventory.jsonl` + `phase_2_outcomes.md`

**Phase 4 closed. Phase 5 (Grading Schema Critique) consumes this tier list to re-weight rubric components.**
