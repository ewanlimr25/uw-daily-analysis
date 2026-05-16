---
description: Run the full Friday-evening or Sunday-prep weekly intelligence note in the voice of a top-tier institutional desk strategist (JPM/GS Friday note). Persistence-weighted conviction rubric over a 5-day window with WoW regime delta, intra-week thesis scorecard (WIN/LOSS/INCONCLUSIVE per ticker), sector rotation persistence, vol-surface evolution, LEAP roll detection, OPEX-week pin map, and 2-week earnings lookahead. Output is tiered High/Medium/Low conviction with backtest-weighted sizing. Invoke whenever the user asks for a weekly recap, week-ahead prep, Sunday strategy session, weekly market intelligence note, or types `/weekly-analysis`. Do NOT trigger for single-day reports (use `/daily-analysis`), single-ticker analyses (use `mcp__uw-pp__insights_deep_dive`), or month/quarter horizons.
---

# Weekly Market Intelligence

Run a full weekly intelligence note in the voice of a top-tier institutional desk strategist. Uses the same two-phase agent fleet as `/daily-analysis` but wired to week-range inputs and a persistence-weighted conviction rubric. **All data is pulled fresh from MCP tools — no dependency on prior daily analysis files.** Phase 1 spawns **11 agents** (12 in OPEX week) in parallel against a shared week-baseline context. Phase 2 runs `signal-confluence-quant` for audited scoring, then `risk-monitor` for gating, against the union of the week's candidates. Score conviction formally with explicit tiers, backtest top names, write winners back to the watchlist, and save the report to `analyses/weekly/YYYY-WW.md`.

## When to invoke

- "Weekly recap", "week in review", "weekly intelligence note"
- "Sunday prep", "week-ahead prep", "what should I watch next week"
- Friday-evening review of the trading week
- Slash command `/weekly-analysis`

## When NOT to invoke

- "Wrap up today" / "EOD report" → `/daily-analysis`.
- "What's NVDA doing this week?" → `mcp__uw-pp__insights_deep_dive` + `mcp__uw-pp__historical_trend` for that one ticker.
- Month-over-month or quarterly horizons — call `mcp__uw-pp__historical_cumulative_premium_flow` with `lookback_days=30` (or 90) and let the user drive the synthesis manually.

## Model routing

The orchestrator running this skill must use **`opus` with extended thinking on**. It performs the cross-agent synthesis, conviction rubric application, and report writing — tasks that degrade materially on a smaller model. Sub-agents are cheaper and have narrower mandates; assign models as follows when spawning each agent:

| Agent | Model | Thinking | Why |
|---|---|---|---|
| gamma-flip-tracker | sonnet | off | Mechanical: today's 0DTE flip + pin strikes; demoted to forward-looking only this week |
| dealer-positioning-strategist | sonnet | **on** | Multi-signal synthesis: DEX trajectory + vanna squeeze + GEX time series across the week — reasoning depth required |
| sweep-tracker | sonnet | off | Filter and rank by `hot_chains_sweep_persistence` count — no synthesis |
| accumulation-hunter | sonnet | off | Pattern match across DP + OI over 5d/10d, with `dark_pool_block_stratified` gate |
| contrarian-scanner | sonnet | off | Trajectory computation — rising vs falling `historical_pc_ratio_zscore`, VRP gate |
| earnings-scout | sonnet | **on** | Dual mandate: judgment-heavy recap grading + multi-signal lookahead ranking with term-skew |
| vol-surface-scout | sonnet | off | Analytical WoW delta — systematic flagging, `historical_iv_percentile_zscore` + VRP bias |
| multileg-strategist | sonnet | **on** | Hardest Phase 1 task: inferring institutional intent from repeated cross-week structures + term-structure context |
| leap-positioning-radar | sonnet | **on** | Multi-signal synthesis over 10d+ window + rolling detector + historical_cumulative_premium_flow accretion classification |
| sector-rotation-strategist | sonnet | off | Persistence-gated rotation calls + leader extraction; mostly mechanical |
| opex-pin-strategist (conditional) | sonnet | off | OPEX-week only; ranking + structure suggestion is rule-based |
| signal-confluence-quant (Phase 2a) | sonnet | **on** | Audited per-ticker scoring with explicit component breakdown — reasoning required for tie-breaking and audit-trail prose |
| risk-monitor (Phase 2b) | sonnet | off | Systematic: correlation matrix + cluster flagging + gate stack application |

Pass the model assignment in each agent's prompt header (e.g. `Model: claude-sonnet-4-6, extended_thinking: false`).

## Operating principle: persistence beats a single print

Single-day signals are noise; multi-week persistence is the edge. Every agent in this run must consume week-range data wherever the MCP supports it. Specifically:

- `mcp__uw-pp__hot_chains_sweep_persistence` over `mcp__uw-pp__options_flow_sweeps`
- `mcp__uw-pp__historical_oi_trend` with `lookback_days=5` over `mcp__uw-pp__oi_biggest_increases`
- `mcp__uw-pp__historical_cumulative_premium_flow` over single-day premium totals
- `mcp__uw-pp__historical_pc_ratio_zscore` over the deprecated `screener_put_call_extremes`
- `mcp__uw-pp__historical_iv_percentile_zscore` over raw IV rank for outlier robustness
- `mcp__uw-pp__historical_gex_time_series` over single-day GEX snapshots
- `mcp__uw-pp__options_flow_sector_flow_persistence` over single-day `options_flow_sector_flow`
- `mcp__uw-pp__historical_signal_backtest` before sizing any trade

The week is the minimum unit of analysis. Pass this instruction through to every spawned agent.

---

## Step 0 — Preflight: week boundaries, coverage, regime baseline

This step builds the shared week-baseline context every Phase 1 agent receives. **Do not skip any sub-step** — agents that lack the week anchor produce inconsistent calls.

1. **Pin the trading-week boundaries** — run these shell commands to get authoritative date anchors. Do not infer dates from context:

   ```bash
   TODAY=$(date +%F)
   ISO_WEEK=$(date +%G-W%V)

   # Monday of the current ISO week (macOS date)
   DOW=$(date +%u)               # 1=Mon … 7=Sun
   MONDAY=$(date -v-$((DOW - 1))d +%F)

   # End of week: Friday (or today if before Friday)
   FRIDAY=$(date -v-$((DOW - 5))d +%F 2>/dev/null || echo "$TODAY")
   WEEK_END=$([ "$DOW" -le 5 ] && echo "$TODAY" || echo "$FRIDAY")

   echo "ISO_WEEK=$ISO_WEEK  MONDAY=$MONDAY  WEEK_END=$WEEK_END  TODAY=$TODAY"
   ```

   These four variables — `ISO_WEEK`, `MONDAY`, `WEEK_END`, `TODAY` — are the canonical anchors for this run. The filename is `analyses/weekly/$ISO_WEEK.md` and the watchlist group key is `conviction_week_$ISO_WEEK`.

2. **Coverage list** — call `mcp__uw-pp__historical_available_dates` and filter to dates in `[MONDAY, WEEK_END]`. Call this filtered list `covered_dates`. **Rules:**
   - If `covered_dates` is empty → abort and report "No UW data available for the current trading week."
   - If any calendar weekday Mon–Fri is missing from `covered_dates`, note the gap explicitly — agents must not assume a full 5-day window. Pass `covered_dates` (not the computed calendar range) as the authoritative list to every Phase 1 agent.

3. **Regime baseline** — call `mcp__uw-pp__risk_market_regime` twice: once for `TODAY` and once for `covered_dates[0]`. Compute the WoW regime delta. This **week regime baseline** — regime today vs week-open, and whether it improved / deteriorated / held — is passed to every Phase 1 agent. Agents must gate their directional calls against it.

4. **Vol regime** — call `mcp__uw-pp__historical_vrp` for the most recent date in `covered_dates`. Classify the week as a premium-selling environment (VRP positive) or premium-buying environment (VRP negative). This shapes which agents you trust most: VRP-positive weeks favour vol-surface-scout & contrarian-scanner; VRP-negative weeks favour gamma-flip-tracker & earnings-scout.

5. **Sector & flow-share baseline** — call in parallel:
   - `mcp__uw-pp__options_flow_sector_flow_persistence` over the full week range. This is the durability check that gates §2 of the report (sector rotation narrative).
   - `mcp__uw-pp__options_flow_sector_flow` for `WEEK_END` — single-day snapshot for week-end skew within the persistence narrative.
   - `mcp__uw-pp__options_flow_dte_volume_share` for each covered date (or `WEEK_END` only if a faster pass is needed) — institutional vs retail share trend across the week. Feeds §1.

6. **Top-of-funnel screens** — run in parallel for `WEEK_END`:
   - `mcp__uw-pp__screener_bullish_bearish` (top 25 each side) — week-end leaderboard.
   - `mcp__uw-pp__insights_signal_confluence` (`min_score=4`, top 25 each direction) — multi-factor scoring at higher threshold than daily.
   - `mcp__uw-pp__screener_iv_rank` (top 25 high, top 25 low) — premium-selling vs premium-buying candidates for next week.
   - `mcp__uw-pp__screener_earnings_catalyst` — upcoming earnings + elevated IV (next 14 days) — feeds §6.
   - `mcp__uw-pp__screener_volume_vs_average` (top 25, `min_ratio=3`) — flow anomalies vs 30-day baseline; cross-reference against multi-day persistence for §3.
   - `mcp__uw-pp__hot_chains_sweep_ratio` — high sweep-to-volume contracts at week-end; cross-reference against `hot_chains_sweep_persistence` in sweep-tracker.

7. **OPEX guard** — if `WEEK_END` is within 7 calendar days of the third Friday, also call `mcp__uw-pp__oi_pin_risk` for SPY/QQQ/IWM and the top 10 from step 6, plus `mcp__uw-pp__oi_opex_concentration` for the same set. Pinning candidates feed §9 (Setups for Next Week).

8. **Compose the week-baseline context block** — this compact JSON-shaped block is passed verbatim to every Phase 1 agent: `{iso_week, monday, week_end, today, covered_dates, regime_today, regime_monday, regime_delta, vrp_classification, sector_persistence, top_bullish, top_bearish, confluence, iv_extremes, earnings_lookahead, opex_pin_candidates}`.

---

## Step 1 — Phase 1: alpha-finding agents (parallel, single batch)

Spawn these **11 agents simultaneously** — a single message with 11 Agent tool calls (12 in OPEX week — see opex-pin-strategist). Hand each one: (a) the week-baseline context block from Step 0, (b) the count of covered days (so agents know whether they have a full 5-day window or a shorter one), and (c) the explicit tool list below. Each agent must restrict queries to `covered_dates` and favour multi-day tools over single-day equivalents.

**Hard rule:** no agent re-fetches `risk_market_regime`, `historical_vrp`, or `options_structure_front_end_iv_ratio` — those come from Step 0 context only.

### gamma-flip-tracker — DEMOTED, forward-looking only (sonnet, thinking off)
Do **NOT** produce intraday or 0DTE calls. Instead: forecast next week's zero-gamma level and key pin strikes for SPY/QQQ/IWM and any liquid name with significant near-dated GEX from Step 0. **Swing-horizon DEX/vanna/charm/GEX-trajectory work is owned by `dealer-positioning-strategist` (next agent below) — do not duplicate.**

Tools required:
- `mcp__uw-pp__options_structure_today_gamma_flip` — current day zero-gamma + flip strike (latest).
- `mcp__uw-pp__options_structure_gex` (default `dte_max=45`) — per-strike GEX, call wall, put wall.
- `mcp__uw-pp__options_flow_expiry_heatmap` — confirm next-week expiry holds the volume share for the forecast.
- `mcp__uw-pp__options_flow_greek_screener` — `min_gamma` filter for the highest-impact next-week contracts.

Output: §9 next-week pin vs trend regime call, key SPY/QQQ/IWM pin strikes for next week.

### dealer-positioning-strategist — swing-horizon dealer flows (sonnet, thinking **on**) (NEW)
Owns the multi-day DEX / vanna / charm / GEX-trajectory work. Surfaces 1–4 week swing setups GF cannot see at the 0DTE horizon.

Tools required:
- `mcp__uw-pp__options_structure_dex` — DEX trajectory week-over-week (directional pressure ahead of price).
- `mcp__uw-pp__options_structure_vanna_charm` — vanna-squeeze detection (put-heavy book + falling VIX → BUY setup).
- `mcp__uw-pp__historical_gex_time_series` (`lookback_days=10`, also 30d) — multi-day ZGL trajectory; flag any regime flip across the week.
- `mcp__uw-pp__options_structure_gex` (default `dte_max=45`) — confirm DEX flip is not a single-strike artifact.
- `mcp__uw-pp__options_structure_front_end_iv_ratio` — secondary panic gate; consume from Step 0 if available.

Output: per-ticker swing dealer reads — DEX state + 5d/10d trajectory, vanna-squeeze flags, ZGL trajectory week-over-week, regime-flip detections, swing bias for next 1–4 weeks. Feeds §3 (Swing Book) with the `vanna_squeeze` / `dex_flip_long` / `dex_flip_short` signal classes.

### sector-rotation-strategist — durable rotation calls + named single-name leaders (sonnet, thinking off) (NEW)
Owns multi-week sector rotation + leader extraction. Enforces ≥3-day persistence — primary feed for §2 of the report.

Tools required:
- `mcp__uw-pp__options_flow_sector_flow_persistence` — multi-day rotation persistence per sector across `covered_dates` (PRIMARY).
- `mcp__uw-pp__options_flow_sector_flow` for `WEEK_END` — single-day skew within the persistence narrative.
- `mcp__uw-pp__screener_bullish_bearish` — filter by sector to extract single-name leaders.
- `mcp__uw-pp__options_flow_dte_volume_share` per covered date — institutional vs retail share by sector trend across the week.

Output: rotation regime call (defensive→cyclical / cyclical→defensive / growth→value / value→growth / no_change), per-sector persistence scores, named single-name leaders, swing-book implication. Feeds §2 (Sector Rotation) directly.

### opex-pin-strategist — CONDITIONAL: only spawn within 7 days of monthly third-Friday (sonnet, thinking off) (NEW)
**Conditional spawn.** If `WEEK_END` is within 7 calendar days of the monthly third-Friday OPEX, include this agent (12 agents total). Otherwise omit.

Tools required:
- `mcp__uw-pp__oi_pin_risk` — pin candidates with strike + probability.
- `mcp__uw-pp__oi_opex_concentration` — OI mass at OPEX strikes.
- `mcp__uw-pp__options_structure_gex` — confirm pin strike sits near a long-gamma wall.

Output: ranked OPEX book — top 5–10 names with `{ticker, pin_strike, distance_pct, oi_mass_at_pin, gex_at_pin, ranked_score, suggested_structure}`. Feeds §9 (Setups for Next Week) when the upcoming week is OPEX week.

### sweep-tracker — multi-day persistence (sonnet, thinking off)
Use `mcp__uw-pp__hot_chains_sweep_persistence` as the **primary** signal. Surface tickers swept on **≥3 of 5** trading days this week.

Tools required:
- `mcp__uw-pp__hot_chains_sweep_persistence` (primary).
- `mcp__uw-pp__hot_chains_smart_money_flow` — ask vs bid colour for each persistence-flagged ticker.
- `mcp__uw-pp__options_flow_sweeps` — supplementary (week-end snapshot only).
- `mcp__uw-pp__options_flow_top_premium_trades` (top 30, week range) — whale-ticket validation.
- `mcp__uw-pp__hot_chains_most_active` — per-ticker contract-level conviction.

Single-day sweeps alone are insufficient for a weekly recommendation. Rank candidates by persistence count first.

### accumulation-hunter — expanded window (sonnet, thinking off)
Run with `lookback_days=5` (and `lookback_days=10` as a secondary pass).

Tools required:
- `mcp__uw-pp__insights_institutional_accumulation` (`lookback_days=5` and `lookback_days=10`).
- `mcp__uw-pp__dark_pool_ticker_summary` (top 30 by premium across each covered date — aggregated).
- `mcp__uw-pp__dark_pool_largest` (top 30 across the full week range).
- `mcp__uw-pp__dark_pool_block_stratified` — institutional vs retail tier filtering.
- `mcp__uw-pp__dark_pool_price_levels` — institutional support/resistance built up across the week.
- `mcp__uw-pp__dark_pool_extended_hours` — overnight/pre-market block activity.
- `mcp__uw-pp__oi_smart_positioning` — OI bullish/bearish inference.
- `mcp__uw-pp__historical_oi_trend` (`lookback_days=5`) — multi-day OI build verification (BUILDING required for full points).

Output: tickers with quiet multi-day OI build sustained across the full week with both DP and OI confirmation.

### contrarian-scanner — pc_ratio trajectory (sonnet, thinking off)
Tools required:
- `mcp__uw-pp__historical_pc_ratio_zscore` — compute the trajectory of historical_pc_ratio_zscore across `covered_dates`. This is the primary signal. **Do NOT use the deprecated `screener_put_call_extremes`.**
- `mcp__uw-pp__insights_price_vs_flow` (week-range) — when smart money disagrees with price.
- `mcp__uw-pp__options_flow_iv_outliers` (week aggregated) — high-IV contracts where flow may be exhausted.
- `mcp__uw-pp__oi_decrease_with_volume` — capitulation / profit-taking detection.
- `mcp__uw-pp__screener_iv_rank` (extreme high) — premium ripe to fade.

Flag names where crowdedness is **rising** (deteriorating contrarian setup) vs **falling** (crowding unwinding — potential fade entry). Gate every fade call against the week-regime baseline.

### earnings-scout — DUAL MANDATE: recap + lookahead (sonnet, thinking **on**)
Two sub-tasks:

**(a) Recap.** For each earnings event that printed this week (extract from `covered_dates` flow data), evaluate flow reaction vs pre-event thesis:
- `mcp__uw-pp__insights_earnings_play` — pre-event positioning & post-event flow.
- Grade each play as confirming or disconfirming (BUY VOL → IV crush realised? SELL VOL → directional move trapped? etc.).

**(b) Lookahead.** Scan the next two calendar weeks for earnings catalysts:
- `mcp__uw-pp__screener_earnings_catalyst` (next 14 days).
- `mcp__uw-pp__options_structure_iv_term_structure` per candidate — KINKED/BACKWARDATION alignment.
- `mcp__uw-pp__options_structure_term_skew` — back-month skew at the earnings DTE.
- `mcp__uw-pp__options_structure_front_end_iv_ratio` — quick panic detector.
- `mcp__uw-pp__insights_analyst_vs_flow` — analyst-vs-flow disagreement is the highest-EV setup.

Output: §6 earnings recap + ranked 2-week lookahead with IV term-structure alignment + analyst disagreement scores.

### vol-surface-scout — WoW term-structure & skew evolution (sonnet, thinking off)
Tools required:
- `mcp__uw-pp__options_structure_iv_term_structure` for `WEEK_END` and `covered_dates[0]` — compute the WoW shape change.
- `mcp__uw-pp__options_structure_term_skew` for `WEEK_END` and `covered_dates[0]` — WoW skew change.
- `mcp__uw-pp__options_structure_front_end_iv_ratio` (current) — single-number panic check.
- `mcp__uw-pp__historical_iv_percentile_zscore` (`lookback_days=252`) — outlier-robust per-ticker IV percentile (Goyal-Saretto). Use this instead of raw IV rank where possible.
- `mcp__uw-pp__options_flow_iv_outliers` (week aggregated) — single-contract outliers.
- `mcp__uw-pp__options_flow_expiry_heatmap` — week-level concentration; calendar-spread candidate identification.

Flag names that went from NORMAL to KINKED or into BACKWARDATION across the week. These are §5.

### multileg-strategist — full-week sample (sonnet, thinking **on**)
Tools required:
- `mcp__uw-pp__hot_chains_multileg` across the **full week** (not just today). Structures repeated on **≥2 days** carry materially higher directional inference weight than single-day prints.
- `mcp__uw-pp__options_flow_top_premium_trades` filtered to ≥$1M premium (week range).
- `mcp__uw-pp__options_flow_greek_screener` — directional / vol / vega bets by Greek profile.
- `mcp__uw-pp__options_flow_expiry_heatmap` — concentration by expiry to spot calendar/diagonal builds.
- `mcp__uw-pp__hot_chains_most_active` — per-ticker context.

Output: per-ticker structure read with directional thesis, repeated-on-N-days count, and built-in risk caps.

### leap-positioning-radar — rolling detector + 10d window (sonnet, thinking **on**)
Tools required:
- `mcp__uw-pp__oi_position_rolls` across each covered date — surface conviction shifts (rolls forward into 2027/2028 LEAPs, rolls up in strike, large new LEAP OI initiations).
- `mcp__uw-pp__oi_biggest_increases` (`min_dte=180`) — fresh LEAP positions only.
- `mcp__uw-pp__historical_oi_trend` (`lookback_days=10`) — BUILDING required for full points.
- `mcp__uw-pp__historical_cumulative_premium_flow` (`lookback_days=30` or default 90) — LEAP-grade slow-accretion signature.
- `mcp__uw-pp__insights_institutional_accumulation` (`lookback_days=10`).
- `mcp__uw-pp__insights_conviction_matrix` — must show DIRECTIONAL_LONG with confidence > 70.

Output: §4 LEAP candidates that pass strict filters; explicit disqualification notes for any contender that doesn't.

---

## Step 2 — Phase 2: signal-confluence-quant THEN risk-monitor (sequential, consumes Phase 1 union)

Phase 2 runs in two stages: the quant produces the audited score, then risk gates and sizes.

### Step 2a — signal-confluence-quant (sonnet, thinking **on**)

Once **all** Phase 1 agents return, collect the **union** of every candidate ticker surfaced across all 11 (or 12) agents for the full week. Spawn `signal-confluence-quant` with that union plus the Step 4 weekly conviction rubric. It must:

- Run `mcp__uw-pp__insights_signal_confluence` per ticker (`min_score=5` for weekly).
- Run `mcp__uw-pp__historical_signal_backtest` per ticker, per dominant signal class.
- Pull `mcp__uw-pp__historical_cumulative_premium_flow` (30d and 90d) for tie-breaking and supplemental directional context.
- Compute `raw_score` per ticker against the weekly persistence-weighted rubric (Step 4), identify `dominant_signal_class`, attach `win_rate`, emit `final_size_recommendation_pre_risk`, and produce a full audit trail per ticker.

Output: sorted list `{ticker, raw_score, score_components[], dominant_signal_class, confluence_score, cum_premium_flow_30d/90d, win_rate, final_size_recommendation_pre_risk, audit_trail}`.

### Step 2b — risk-monitor (sonnet, thinking off)

Spawn `risk-monitor` with (a) the quant's sorted score list and (b) the week-baseline context block from Step 0. It must:

- Run `mcp__uw-pp__risk_portfolio_correlation` against the week-candidate set — flag corr > 0.7 sub-groups as concentration risks.
- Confirm `mcp__uw-pp__risk_market_regime` from Step 0 (already pinned; do not re-fetch).
- Apply the gate stack: −1 tier per regime conflict, panic (`options_structure_front_end_iv_ratio > 1.10`), VRP-vs-trade-type contradiction, corr-cluster duplication, adverse sector rotation.
- Pull `mcp__uw-pp__watchlist_alerts` and `mcp__uw-pp__watchlist_scan` against the prior `conviction_week_<previous>` group — surface adverse-flow exit candidates.
- Persist this week's top 5 conviction names via `mcp__uw-pp__watchlist_manage(action="add", group="conviction_week_<ISO_WEEK>")`.

Output: §7 risk & correlation — clusters, regime conflicts, VRP / panic gates applied, adverse-flow exit list, hedge sleeve recommendation, final sizing table per ticker that consumes the quant's pre-risk size.

---

## Step 3 — Confluence gate

Before scoring, apply the **confluence gate**: a ticker only enters the conviction rubric if **at least two distinct Phase 1 agents flag it positively across the week** OR **one Phase 1 agent flags it AND `mcp__uw-pp__insights_signal_confluence` rates it ≥5 at WEEK_END**. Names with only one signal class but no confluence backing are noted in §10 ("Watch-only — single signal") and excluded from the high-conviction list. This rule prevents single-tool false positives from contaminating the trade book.

Note: the threshold here is `insights_signal_confluence ≥ 5` (vs `≥ 4` in `/daily-analysis`) because weekly recommendations carry more capital and need a stricter prior.

### Step 3a — HIGH-tier load-bearing-tool gate (2026-05-09 audit P0)

After scoring, before any candidate enters the HIGH-tier section of §3 / §8 (i.e. anything that would be sized as `full` post-quant), the call must additionally cite at least **2 of the 4 LOAD-BEARING tools**:

- `dark_pool_block_stratified` (institutional-vs-retail filter)
- `historical_cumulative_premium_flow` (30d directional accretion)
- `insights_institutional_accumulation`
- `options_structure_dex` (DEX)

A call that scores raw_score ≥ 10 (HIGH-tier under the 2026-05-15 cuts) but cites fewer than 2 of these four tools must be **demoted to MEDIUM tier**. The Phase 4 audit found these four tools carry the load (+11pp to +18pp marginal contribution each); any HIGH-tier call without two of them is structurally unsupported even if the rubric points add up.

---

## Step 4 — Weekly conviction score (persistence-weighted rubric, applied by signal-confluence-quant in Step 2a)

For every ticker that cleared the confluence gate, the quant computes the weekly conviction score against this rubric. Every signed point gets attached to a named source agent + tool in `score_components`.

```
Weekly conviction score = Σ:
  +3  swept on ≥3 of 5 days (sweep-tracker via hot_chains_sweep_persistence)
  +3  historical_oi_trend BUILDING for the full week, lookback_days ≥ 5 (accumulation-hunter / leap-positioning-radar)
  +2  3+ aligned signals in accumulation-hunter sustained across week, dark_pool_block_stratified institutional-tier confirmed
  +2  insights_conviction_matrix = DIRECTIONAL_LONG, confidence > 70, stable WoW
  +2  oi_position_rolls shows institutional roll forward into longer-dated LEAP (per-covered-date)
  +2  historical_cumulative_premium_flow shows net directional accretion across the week — fresh-thesis (sharp 30d) or thesis-extension (smooth 90d)
  +2  dealer-positioning-strategist flags DEX flip or vanna squeeze in trade direction across the week
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector (persistence ≥ 3)
  +1  in earnings-scout BUY VOL or SELL VOL for next 2 weeks (options_structure_term_skew aligned for full size)
  +2  multileg-strategist directional structure repeated on ≥2 days (term-structure-anchored play type)   # was +1; promoted 2026-05-09 (Phase 4 +8pp marginal)
  +1  vol-surface-scout flags KINKED or BACKWARDATION, worsening WoW; historical_iv_percentile_zscore extreme; VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner crowded long with rising historical_pc_ratio_zscore trajectory (VRP positive)
  -3  flow_conflict — signal-confluence-quant applies mechanically when historical_cumulative_premium_flow 30d direction is *clearly opposite* dominant_signal_class (signed-sum sign flip + magnitude > today's union-median |cum_flow_30d|, or explicit OPPOSITE label)   # 2026-05-15 audit P0 — see signal-confluence-quant.md "Mechanical flow_conflict deduction" rule
  -1  flow_conflict_lite — signal-confluence-quant applies when the 30d cum_premium_flow read is MIXED (signed sum near zero, or aligned but bottom-quartile magnitude)   # 2026-05-15 audit P0
  # 2026-05-09 -2 generic flow_conflict line replaced with the mechanical -3 / -1 split above (Phase 3 2026-05-15 audit: 30% missed-gate rate at the generic line)
  -2  risk-monitor flags in week-candidate correlation cluster (corr > 0.7) — applied in 2b
  -3  WoW risk_market_regime flip conflicts with trade direction — applied in 2b
```

### Conviction tiers (2026-05-15 audit P0; supersedes prior ≥9 / 6–8 / 3–5 cuts)

Map every ticker to a tier:

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 10 | **HIGH** | full size (subject to win_rate gate in Step 5) |
| 7 – 9 | **MEDIUM** | half size (subject to win_rate gate) |
| 3 – 6 | **LOW** | starter / watch-only — paper trade or wait for daily confirmation |
| ≤ 2 | drop | not surfaced in the report's trade book |

Surface every HIGH and MEDIUM tier ticker in the Executive Summary headline and §8 (High-Conviction Cross-Ref). LOW tier goes into a separate "Watchlist for next week" section (§9). Phase 3 of the 2026-05-15 audit found the MED-vs-LOW gap was only 1.1pp at the prior cuts (noise); the new cuts restore tier monotonicity (HIGH ≥10 realised 0.85 vs the prior HIGH ≥9 realised 0.667).

---

## Step 5 — Backtest-weighted sizing (gates the tier sizing)

For each HIGH or MEDIUM tier ticker, identify its dominant signal class — typical labels: `multi_day_sweep`, `oi_build`, `dark_pool_accumulation`, `leap_roll`, `multileg_repeat`, `bullish_flow`, `bearish_flow`, `vanna_squeeze`. Call `mcp__uw-pp__historical_signal_backtest` with that signal class and the ticker. Apply the win-rate gate **on top of** the tier sizing:

| `win_rate` | Multiplier |
|---|---|
| ≥ 0.65 | × 1.0 (keep tier sizing) |
| 0.50 – 0.65 | × 0.5 (one tier down — HIGH→half, MEDIUM→starter) |
| < 0.50 | × 0 (drop to watch-only regardless of conviction tier) |

For non-directional signals (`high_iv_rank`, `volume_spike`) the backtest returns `vol_realisation_rate` instead — use the same thresholds. Note the win_rate explicitly next to each call in the Swing Book (§3) and LEAP Book (§4).

---

## Step 6 — Thesis scorecard: intra-week signal performance

For every ticker surfaced by any Phase 1 agent this week, check whether signals present at the **start** of the week resolved in their predicted direction by **week-end**. This is derived entirely from fresh MCP queries — no daily analysis files are read.

For each ticker, run these checks using `covered_dates[0]` and `covered_dates[1]` as early-week reference dates and `covered_dates[-1]` (today / Friday) as the resolution date:

1. **Sweep signals** — `mcp__uw-pp__hot_chains_sweep_persistence` per-day breakdown. Did sweeps on days 1–2 continue (sustained conviction) or reverse (fading signal)?
2. **OI-build signals** — `mcp__uw-pp__historical_oi_trend` (`lookback_days=5`). Did OI continue building (BUILDING → WIN) or roll off (LOSS)?
3. **Premium flow signals** — `mcp__uw-pp__historical_cumulative_premium_flow` for the full week range. Did net premium align with the directional thesis?
4. **Direction confirmation** — `mcp__uw-pp__historical_trend` over the week range. Did price action confirm or contradict the early-week signal direction?

Grade each ticker:
- **WIN** — signal direction confirmed by end-of-week flow and price trend.
- **LOSS** — price/flow moved against the early-week direction.
- **INCONCLUSIVE** — insufficient price movement or contradictory signals (excluded from hit-rate denominator).

Summarise in a table: `| Ticker | Signal type | Early-week direction | Week-end outcome | Grade | Note |`

Compute the week's hit rate: `wins / (wins + losses)`. This headline goes in the Executive Summary as **Signal performance**.

---

## Step 7 — Strategy synthesis on the conviction list

For each **HIGH and MEDIUM** tier ticker (after the win-rate gate):
1. Call `mcp__uw-pp__insights_deep_dive` — full Yahoo + UW data for full thesis verification.
2. Call `mcp__uw-pp__historical_trend` (`lookback_days=10`) — multi-week price/flow trend confirmation.

For the entire HIGH and MEDIUM tier list (in one call):
3. Call `mcp__uw-pp__playbook_batch_scan` with the ticker list — get rule-based options-strategy suggestions. Cross-reference against multileg-strategist's named structures; prefer the multileg read if there's disagreement and note the conflict.

This step is the synthesis bridge from "signal" to "trade structure" — without it, conviction scores are abstract.

---

## Step 8 — Write the report

Synthesize into the structured weekly note below. Use **full narrative sentences** in qualitative sections (Executive Summary, Regime & WoW Delta, Risk, Setups for Next Week) and **tables** for data-dense sections (Signal Performance, Swing Book, LEAP Book, High-Conviction Cross-Ref). Tone: institutional desk strategist — precise, assertive, no filler.

Before writing: run `mkdir -p analyses/weekly` via Bash if the directory does not exist.

````markdown
# Weekly Market Intelligence — Week of YYYY-MM-DD (ISO YYYY-WW)

## Executive Summary
- **Week regime + WoW Δ:** <regime today vs Monday — improved / deteriorated / held — plus VRP classification, one line>
- **Signal performance:** <X of Y early-week signals confirmed (hit rate %)>
- **Top swing build for next week:** <ticker, thesis, invalidation, win_rate, tier, size>
- **Top LEAP build:** <ticker, scenario, invalidation, win_rate, tier, size>
- **Biggest emerging risk:** <correlation cluster name + members, OR adverse flow, OR regime flip>

## 0. Week in Review — Intra-Week Signal Performance
[Table: Ticker | Signal type | Early-week direction | Week-end outcome | Grade | Note. Hit rate headline. Sourced from hot_chains_sweep_persistence, historical_oi_trend, historical_cumulative_premium_flow, historical_trend — no daily files read.]

## 1. Regime & WoW Delta
- `risk_market_regime` today + Monday baseline; WoW delta narrative
- `historical_vrp` classification — premium-selling vs premium-buying environment
- `options_flow_dte_volume_share` aggregated across the week — institutional vs retail share trend
- Implications for next week's bias

## 2. Sector Rotation
- `sector-rotation-strategist` output: rotating-into / rotating-out-of sectors with persistence scores (≥3 days)
- Rotation regime call (defensive→cyclical / cyclical→defensive / growth→value / value→growth / no_change) with regime confidence
- Named single-name leaders within each rotating sector
- Rotation narrative for next week + swing-book implications

## 3. Swing Book (1–6 weeks) — ranked by weekly conviction score
[Table: Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure | Invalidation. Subdivide into 3a long swings (regime-aligned) and 3b short/fade swings (defined risk only).]

## 4. LEAP Book (6–24 months)
[Table: Ticker | Tier | Score | Win-rate | Final size | Scenario | Invalidation. leap-positioning-radar with `oi_position_rolls` highlights and `historical_cumulative_premium_flow` accretion. DIRECTIONAL_LONG only.]

## 5. Volatility Surface — WoW Term Structure & Skew Evolution
- vol-surface-scout: names that shifted to KINKED or BACKWARDATION across the week
- WoW IV term-structure delta with `options_structure_iv_term_structure` snapshots from `covered_dates[0]` and `WEEK_END`
- Skew change narrative; calendar-spread candidates
- `historical_iv_percentile_zscore` outliers (multi-month percentile context)

## 6. Earnings — Recap & 2-Week Lookahead
- (a) Recap of this week's prints with flow reaction grades
- (b) Ranked lookahead to next 2 weeks with IV kink alignment and analyst-vs-flow disagreement scores

## 7. Risk & Correlation (week-candidate universe)
- risk-monitor consuming the full week-candidate union — not the static watchlist
- `risk_portfolio_correlation` clusters with member tickers and corr coefficients
- `insights_signal_confluence` flags
- Concentration risks + recommended hedge sleeve

## 8. High-Conviction Cross-Ref (HIGH and MEDIUM tier)
[Per-ticker breakdown: tier | score components | win_rate | final size | invalidation level. One paragraph per HIGH-tier name.]

Embedded rubric (for audit):

[Embed the Step 4 conviction rubric verbatim here.]

## 9. Setups for Next Week
- gamma-flip-tracker next-week GEX forecast — zero-gamma level, key pin strikes for SPY/QQQ/IWM
- dealer-positioning-strategist swing setups — DEX flips, vanna squeezes, regime flips for the next 1–4 weeks
- Pin vs trend regime call
- 2–3 highest-conviction actionable setups for the coming week (HIGH-tier names)
- LOW-tier names to track for daily-analysis confirmation
- OPEX-week ranked book if `opex-pin-strategist` was spawned — pin candidates with `suggested_structure` per name (iron flies, short straddles, broken-wing butterflies)

## 10. Watch-only — single signal, no confluence
[Names that surfaced from one agent but failed the confluence gate. Listed for journaling, NOT for trade entry next week.]
````

---

## Step 9 — Confirm watchlist write-back (handled by risk-monitor in Step 2b)

The top-5 watchlist write-back is performed inside `risk-monitor` during Step 2b — the agent calls `mcp__uw-pp__watchlist_manage(action="add", group="conviction_week_<ISO_WEEK>")` with this week's top 5 by conviction score. **Do not double-write.**

Confirm the write-back happened by checking the `risk-monitor` output for the explicit `watchlist_write_back_confirmation` field. If missing, call `mcp__uw-pp__watchlist_manage(action="add", group="conviction_week_<ISO_WEEK>", tickers=[<top_5_by_score>])` directly as a fallback.

If any name was already on a manually-curated group, leave that membership alone — write only to the week-stamped group. This closes the feedback loop: this week's high-conviction names become next week's correlation universe; next week's RM automatically pulls `watchlist_alerts` and `watchlist_scan` against the prior week's group to flag adverse-flow exits.

---

## Step 10 — Save and confirm

1. Use Write to save the report to `analyses/weekly/$ISO_WEEK.md`.
2. Confirm the file was written.
3. Print the **Executive Summary** section to chat. Nothing else — the user opens the file for the rest.

---

## Failure modes & recovery

- **Phase 1 agent times out** — re-spawn just that agent with the same context block. If it fails twice, write its section as `[agent timed out — see <agent-name> logs]` and proceed; do not let one agent block the report.
- **`historical_available_dates` shows fewer than 3 covered weekdays** — produce a "limited-data weekly" with that explicit caveat in the Executive Summary, and downgrade tier thresholds (HIGH = 8+, MEDIUM = 6–7, LOW = 3–5) for the smaller window. (Downgrade preserves the same relative gap to the 2026-05-15 default cuts of HIGH ≥10 / MED 7–9 / LOW 3–6.)
- **`risk_market_regime` errors on Monday baseline** — fall back to `covered_dates[1]` and note the substitution.
- **No tickers clear the confluence gate** — produce a report whose §3, §4, §8 are explicitly empty, with §0 (scorecard), §1 (regime), §2 (sector), §5 (vol surface), §6 (earnings), §7 (risk), and §9 (setups) still populated. A "no edge" week is a valid output, not a failure.
