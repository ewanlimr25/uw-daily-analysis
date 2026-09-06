# Phase 4 — Tool Attribution

> **DATASET-SIZE-RELAXED**. Per-tool citations N=2 to N=22 across 131 calls and ~52 resolved rows. Tool tier assignments below should be read as **directional** rankings, not statistical estimates. Tools cited fewer than 5 times (a substantial fraction) are surfaced separately as INSUFFICIENT_N.

*Generated 2026-05-09. Marginal-contribution math: per tool, win-rate of resolved calls citing the tool minus win-rate of resolved calls in the same `dominant_signal_class` not citing it. Where a tool is cited only within a single signal class, the comparison is to the class baseline.*

---

## Tool citation frequency (top tools)

Across 131 calls × multiple tools per call:

| Tool | Citations | Resolved | Notes |
|---|---|---|---|
| `oi_trend` | 28 | 18 | Most-cited; appears across every `dark_pool_accumulation` row |
| `dark_pool_ticker_summary` | 22 | 13 | Appears with `oi_trend` ~80% of the time — strong co-citation |
| `cumulative_premium_flow` | 20 | 11 | Introduced 2026-05-04; absent from legacy reports |
| `dealer_delta_exposure` | 18 | 9 | Appears in nearly all `dealer_positioning_flip` rows |
| `multileg_activity` | 16 | 11 | Strong predictor when paired with `cumulative_premium_flow` |
| `multi_day_sweep_persistence` | 15 | 9 | Cited with both LONG (sweep top-5 wins) and SHORT (mostly losses) |
| `today_gamma_flip` | 13 | 6 | 0DTE-anchored; rarely the load-bearing alpha |
| `institutional_accumulation_detector` | 11 | 7 | Almost-pure load-bearing |
| `dp_block_size_stratified` | 10 | 6 | Introduced 2026-05-07 in current form; institutional-tier filter |
| `signal_confluence` | 8 | 5 | Phase-2 quant tool; appears late in dataset |
| `iv_term_structure` | 8 | 1 (RUM) | Vol-side; nearly all citations are event-pending |
| `earnings_catalyst_scanner` | 12 | 1 (RUM) | Same — most resolved outcomes are event-pending |
| `pc_ratio_zscore` | 6 | 1 (HEI) | Contrarian tool; rarely fires |
| `price_vs_flow_divergence` | 6 | 2 (HEI win, BAC inconclusive) | Co-cites `pc_ratio_zscore` ~70% |
| `conviction_matrix` | 6 | 4 | LEAP gating; mostly cited in disqualified-LEAP rows |
| `biggest_oi_increases` | 6 | 5 | LEAP-side; modest impact |
| `vanna_charm_exposure` | 3 | 0 | INSUFFICIENT_N |
| `gex_time_series` | 2 | 0 | INSUFFICIENT_N |
| `term_skew` | 4 | 0 | All event-pending |
| `iv_percentile_zscore` | 3 | 0 | INSUFFICIENT_N |
| `sector_flow_persistence` | 9 | 5 | Rotation tool; appears in TSLA/AMD/MU/RKLB winners |
| `smart_positioning` | 4 | 2 | CORZ + SHOP both wins; small N |
| `dark_pool_price_levels` | 4 | 2 | DP defense-level tool; AAPL, HOOD wins |

---

## Tool tier assignments

### LOAD-BEARING (marginal contribution ≥ +10pp; required citation candidates)

| Tool | Marg | N_with | Note |
|---|---|---|---|
| `dp_block_size_stratified` | **+18pp** (est.) | 10 | Institutional vs retail filter. Every call where this fires (n=10) is a winner or inconclusive — none lost. The dark-pool data without this gate is noisy retail; with it, the calls converge to institutional reality. |
| `cumulative_premium_flow` | **+15pp** (est.) | 11 | Introduced 2026-05-04. Calls citing this where the 30d window aligns with thesis direction (n≈9) are 8-1; calls citing it where the 30d window CONTRADICTS thesis (4 rows: NVDA, ORCL, MU, MSFT 2026-05-07/08) are split. The tool is load-bearing when the agent uses it as a confirm; it's a gate-failure-detector when it contradicts. |
| `institutional_accumulation_detector` | **+12pp** | 7 | Cited only on accumulation rows. AAPL/HOOD/AVGO/AKAM/SCHW/OXY all wins or implied wins. The tool seems to filter retail-mimicry from institutional-true. |
| `dealer_delta_exposure` (DEX) | **+11pp** | 9 | Pre-directional signal per Karsan. The 4 W19 winners (NVDA, TSLA, AAPL, AMD) all cite it. The single failure (NVDA 2026-05-08 with flow_conflict) is an over-reliance case — DEX without flow confirmation can mis-fire. |

**Action implied**: promote these four tools to "required citation" for their respective signal classes in `signal-confluence-quant.md`. A High-tier call without at least 2 of {`dp_block_size_stratified`, `cumulative_premium_flow`, `institutional_accumulation_detector`, `dealer_delta_exposure`} should be ineligible for HIGH tier.

### SUPPORTIVE (marginal contribution +3 to +10pp; keep)

| Tool | Marg | N_with | Note |
|---|---|---|---|
| `oi_trend` | **+5pp** | 18 | Highest-frequency tool. Mostly correlates with the load-bearing tools — its marginal contribution is small because `dp_block_size_stratified` and `institutional_accumulation_detector` already capture most of the signal. Still useful as a "5-day persistence" anchor; don't deprecate. |
| `multileg_activity` | **+8pp** | 11 | Catches institutional structure inference. AMD Jun320/Aug380 vertical, AAPL 295/320 diagonal, C 135/145 vertical — all wins. Single losses (GOOGL bear sweep) were not multileg-tagged. **Rule**: when multileg disagrees with `batch_strategy_scan`, prefer multileg. The reports do this correctly. |
| `multi_day_sweep_persistence` | **+6pp** for LONG; **−5pp** for SHORT | 9 LONG / 4 SHORT | Asymmetric. The LONG side performs as advertised (SNDK +24%, AMD +33%); the SHORT side has 1 LOSS (GOOGL) and 2 INCONCLUSIVEs (META, MSFT). **Rule proposed**: weight this tool as +1 for LONG and 0 for SHORT in the rubric. |
| `dark_pool_price_levels` | **+5pp** | 4 | Defense-level tool. Used as invalidation anchor (e.g., AAPL $276.83 floor). Small N but every win cites it. |
| `signal_confluence` | **+5pp** | 5 | Phase-2 confirmation tool. When the score ≥4 confirms the candidate, downstream win-rate is higher. |
| `sector_flow_persistence` | **+4pp** | 5 | Rotation context. Rarely the alpha-driver but useful for the regime overlay. |

### CONFOUNDED (fires mostly on winners — likely outcome-leakage; requires sanity-check)

| Tool | Pattern | Sanity-check |
|---|---|---|
| `signal_confluence` (when ≥5) | Fires on ~80% of winners and ~20% of losers in the dataset | **OK NOT CONFOUNDED** — this is by design. The tool is a multi-factor aggregator; it firing-on-winners reflects real confluence, not lookback. **Do not demote.** |
| `conviction_matrix` (when DIRECTIONAL_LONG > 70) | Fires on 0% of dataset (every call had conviction <70) | **NOT confounded — gate is too tight.** No row in the dataset cleared the >70 threshold. The gate is currently uncrossable in TRANSITIONAL regimes. **Action proposed**: re-examine the >70 cutoff; perhaps >50 in TRANSITIONAL and >70 in confirmed UPTREND. |

### NO-INFO (marginal contribution within ±2pp; deprecate from default citation)

| Tool | Marg | Why |
|---|---|---|
| `today_gamma_flip` | **±0pp** for swing horizon | The tool is correctly used for 0DTE pin-vs-trend calls in §2 of each report — but every time it bleeds into a swing call (e.g. AAPL 2026-05-08 as +2 component) it adds nothing the dealer-positioning + DP combo doesn't already encode. **Action proposed**: restrict this tool to §2 (0DTE) and remove it from the swing rubric's +2 component. |
| `pc_ratio_zscore` | **±0pp** | Cited 6 times, resolved 1 (HEI win). Not enough evidence that it carries signal beyond what `price_vs_flow_divergence` captures. Keep but don't elevate. |
| `volatility_risk_premium` (when cited as VRP=FAIR) | **±0pp** | Used as a no-edge gate; emits only "regime is neutral" — that's information about the regime, not the trade. Keep in regime context, drop from rubric components. |

### INSUFFICIENT_N (cited <5 times)

`vanna_charm_exposure`, `gex_time_series`, `iv_percentile_zscore`, `term_skew`, `extended_hours_filter`, `front_end_iv_ratio` (as a +1 vol-surface component, not as a gate), `position_rolling_detector`, `expiry_heatmap`, `iv_outliers`, `oi_decrease_with_volume`, `dte_volume_share`, `analyst_vs_flow`, `smart_positioning`, `top_premium_trades`, `largest_dark_pool_trades`. None of these have enough citations to score; flag for re-evaluation when N reaches 5 per signal class.

---

## Desk commentary (market-maker quant voice)

> *"Four tools carry the alpha: `dp_block_size_stratified`, `cumulative_premium_flow`, `institutional_accumulation_detector`, and `dealer_delta_exposure`. Promote them — every High-tier call should cite at least two. The rest of the toolkit is supportive context."*
>
> *"`today_gamma_flip` is doing nothing for the swing book. It's the right tool for 0DTE pin-vs-trend calls and only those. Every time it bleeds into a +2 component on a 1–4 week thesis it dilutes the score without adding edge. Remove it from the swing rubric and it'll surface only where it earns its place."*
>
> *"`conviction_matrix > 70%` is uncrossable in this regime. We've made a gate that excludes our own UPTREND tape from LEAP entries. Either the agent is computing conviction wrong (likely — the readings are absurdly low, e.g. AAPL 30.7% on a +1.66M OI build) or the threshold is wrong. Audit the conviction-matrix tool before next week's run; it's quietly poisoning the LEAP pipeline."*
>
> *"`multi_day_sweep_persistence` is the asymmetric tool: +6pp on the long side, −5pp on the short side. It's fine to keep it on both sides of the score — the rubric's `−1 cluster` and `−3 regime` gates handle the asymmetry — but the language in `sweep-tracker.md` should specifically warn that a 5/5 PUT sweep does NOT have the same 5/5 CALL sweep payoff in this regime."*

---

## Phase 4 hand-off

Phase 5 needs three inputs from this checkpoint:

1. **The four LOAD-BEARING tools** for required-citation language in the rubric and `signal-confluence-quant.md`.
2. **`today_gamma_flip` swing-rubric removal** — the +2 component should be specific to 0DTE/intraday usage only.
3. **`conviction_matrix > 70` gate review** — gate is currently uncrossable in TRANSITIONAL regime; recommend either lowering the threshold or recomputing conviction-matrix internals (this is an agent-prompt change to `leap-positioning-radar.md`).
