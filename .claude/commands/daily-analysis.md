---
description: Run the full post-market daily intelligence report — regime + GEX + sector flow + sweeps + dark pool + OI + vol surface + LEAP + earnings, organized by trade horizon (0DTE / Swing / LEAP). Two-phase agent fleet with formal conviction scoring, backtest-weighted sizing, and watchlist write-back. Invoke whenever the user asks for an end-of-day or post-market analysis, a daily market report, an EOD briefing, or types `/daily-analysis`. Do NOT trigger for single-ticker deep dives, single-tool queries (e.g. "show me sweeps"), pre-market only briefings (use `playbook_daily_synthesis` directly), or weekly summaries (use `/weekly-analysis`).
---

# Daily Market Analysis

Run a full post-market intelligence report by trade horizon (0DTE / Swing / LEAP). Two phases: Phase 1 spawns **11 alpha-finding agents** (12 in OPEX week) in parallel against a shared macro context; Phase 2 runs `signal-confluence-quant` to produce an audited conviction score per candidate, then `risk-monitor` to gate and size. Every ticker is scored against a formal conviction rubric, top names are backtested for win-rate before sizing, and the top 5 are written back to the watchlist so tomorrow's run measures correlation against today's calls. Save to `analyses/YYYY-MM-DD.md`.

## When to invoke

- Post-market daily report ("EOD analysis", "end of day report", "wrap up the day", "daily intel")
- Slash command `/daily-analysis`
- "Morning briefing" — but only if it should integrate Phase 1 specialist agents. For a fast sub-2-minute briefing, just call `mcp__uw-pp__playbook_daily_synthesis` directly without spawning the fleet.

## When NOT to invoke

- "What's NVDA doing?" → `mcp__uw-pp__insights_deep_dive`, not the full pipeline.
- "Show me today's sweeps" → `mcp__uw-pp__options_flow_sweeps` directly.
- "Find earnings plays this week" → spawn `earnings-scout` alone.
- "Build me a watchlist" → `mcp__uw-pp__watchlist_manage` directly.
- "Recap the week" → `/weekly-analysis`, not `/daily-analysis`.

## Operating principle: prefer multi-day metrics over single-day snapshots

Every spawned agent must prefer multi-day persistence tools over single-day equivalents wherever the MCP supports it. Specifically: `mcp__uw-pp__historical_oi_trend` over `mcp__uw-pp__oi_biggest_increases`, `mcp__uw-pp__hot_chains_sweep_persistence` over `mcp__uw-pp__options_flow_sweeps` for ranking, `mcp__uw-pp__options_flow_sector_flow_persistence` over `options_flow_sector_flow` for rotation calls, `mcp__uw-pp__historical_pc_ratio_zscore` over the deprecated `screener_put_call_extremes`, and `mcp__uw-pp__historical_signal_backtest` before sizing any trade. Single-day signals are noise; multi-day persistence is the edge. Pass this instruction through to every spawned agent.

---

## Step 0 — Preflight & shared macro context

This step builds the shared context every Phase 1 agent receives. **Do not skip any sub-step** — agents that lack the macro anchor produce inconsistent calls.

1. **Date** — run `date +%F` to get today's `YYYY-MM-DD`. This is the report filename, the `conviction_<date>` watchlist group key, and the date passed to every MCP tool.

2. **Coverage check** — call `mcp__uw-pp__historical_available_dates`. Confirm today's date is present. If the latest date lags more than one trading day, abort and tell the user "UW data is stale by N days — re-export from Unusual Whales before running."

3. **One-call briefing** — call `mcp__uw-pp__playbook_daily_synthesis` with today's date. This returns the regime classification, top bullish/bearish confluence tickers, and watchlist alerts in a single call — the shared context anchor for every Phase 1 agent. **Pass this synthesis output to every agent in Step 1** so they don't redundantly re-call `risk_market_regime` or `insights_signal_confluence`.

4. **Macro layer** — call these in parallel and capture the readings:
   - `mcp__uw-pp__risk_market_regime` — SPY/VIX trend + breadth classification (will be the top-line of §1 of the report).
   - `mcp__uw-pp__options_flow_dte_volume_share` — share by 0DTE / weekly / monthly / LEAP. High 0DTE share = retail-dominated tape; high monthly+ share = institutional positioning. This is the regime hint Phase 1 agents need to interpret their own findings.
   - `mcp__uw-pp__historical_vrp` — IV30 vs realised σ30. Whether the day is a premium-selling or premium-buying environment changes which Phase 1 agents you trust most (selling environment → vol-surface-scout & contrarian-scanner; buying environment → gamma-flip-tracker & earnings-scout).

5. **Sector layer** — call in parallel:
   - `mcp__uw-pp__options_flow_sector_flow` — single-day sector premium balance (snapshot).
   - `mcp__uw-pp__options_flow_sector_flow_persistence` — multi-day rotation persistence score (the durability check that gates §2 of the report).

6. **Top-of-funnel screens** — run in parallel:
   - `mcp__uw-pp__screener_bullish_bearish` (top 25 each side) — net premium leaderboard.
   - `mcp__uw-pp__insights_signal_confluence` (`min_score=3`, top 25 each direction) — multi-factor scoring; agents start their hunts here.
   - `mcp__uw-pp__screener_volume_vs_average` (top 25, `min_ratio=3`) — flow anomalies vs 30-day baseline.
   - `mcp__uw-pp__screener_iv_rank` (top 25 high, top 25 low) — premium-selling and premium-buying candidates.

7. **OPEX guard** — if today is within 5 calendar days of the third Friday, also call `mcp__uw-pp__oi_pin_risk` and `mcp__uw-pp__oi_opex_concentration` for SPY/QQQ/IWM and any name in the top of step 6. Pinning candidates feed §2 (0DTE) directly.

The output of Step 0 is a compact JSON-shaped context block: `{date, regime, vrp_classification, dte_share, sector_summary, sector_persistence, top_bullish, top_bearish, confluence, volume_outliers, iv_extremes, opex_pin_candidates}`. Every Phase 1 agent receives this verbatim.

---

## Step 1 — Phase 1: alpha-finding agents (parallel, single batch)

Spawn these **11 agents simultaneously** — a single message with 11 Agent tool calls (12 in OPEX week, see opex-pin-strategist below). Hand each one the Step 0 context block and the explicit MCP tool list below. The named tools are the minimum each agent must consult; agents can pull additional tools from their own descriptions if their finding is surprising.

**Hard rule:** no agent re-fetches `risk_market_regime`, `playbook_daily_synthesis`, `historical_vrp`, or `options_structure_front_end_iv_ratio` — those come from Step 0 context only. Re-fetching corrupts the shared anchor and burns tokens.

### gamma-flip-tracker — today's 0DTE / intraday gamma map ONLY
Scope is **today's expiry** (0DTE) plus the 0–45d gamma frame for tactical intraday. Swing-horizon DEX/vanna/charm/GEX-trajectory work goes to `dealer-positioning-strategist` (see below) — do not duplicate.

Tools required:
- `mcp__uw-pp__options_structure_today_gamma_flip` — 0DTE zero-gamma + ATM flip for SPY/QQQ/IWM and any name with significant 0DTE volume from Step 0.
- `mcp__uw-pp__options_structure_gex` — per-strike GEX, default `dte_max=45`. Flag the call wall and put wall.
- `mcp__uw-pp__options_flow_expiry_heatmap` — confirm today owns the volume (else the 0DTE frame doesn't apply).
- `mcp__uw-pp__options_flow_greek_screener` — `min_gamma` filter to surface highest-impact 0DTE contracts.
- `mcp__uw-pp__hot_chains_most_active` — which strikes flow is targeting today.

Output: per-index regime label (PIN / TREND / NEAR_FLIP), single-name 0DTE pin candidates, today's flip strikes for SPY/QQQ/IWM.

### dealer-positioning-strategist — swing-horizon dealer flows (NEW)
Scope is **1–4 week** dealer positioning shifts. Owns DEX/vanna/charm/GEX-trajectory work that GF can no longer carry alongside 0DTE.

Tools required:
- `mcp__uw-pp__options_structure_dex` (DEX) — pre-directional signal; DEX flips precede price moves (Karsan / SqueezeMetrics).
- `mcp__uw-pp__options_structure_vanna_charm` — vanna-squeeze setup detector (put-heavy book + falling VIX → BUY setup).
- `mcp__uw-pp__historical_gex_time_series` (lookback 10–30d) — multi-day ZGL trajectory; flag any regime flip across the window.
- `mcp__uw-pp__options_structure_gex` (default `dte_max=45`) — confirm DEX flip is not a single-strike artifact.
- `mcp__uw-pp__options_structure_front_end_iv_ratio` — ratio > 1.05 confirms front panic; consume from Step 0 if available.

Output: SPY/QQQ/IWM and single-name swing dealer reads — DEX state + 5d trajectory, vanna-squeeze flags, ZGL trajectory, regime-flip detections, swing bias for next 1–4 weeks.

### sector-rotation-strategist — durable rotation calls + named single-name leaders (NEW)
Scope is multi-week sector rotation with single-name leaders extracted within each rotating sector. Enforces ≥3-day persistence — single-day sector flow is filtered out.

Tools required:
- `mcp__uw-pp__options_flow_sector_flow_persistence` — multi-day rotation persistence per sector (PRIMARY).
- `mcp__uw-pp__options_flow_sector_flow` — week-end skew within the persistence narrative (consume from Step 0 if available).
- `mcp__uw-pp__screener_bullish_bearish` — filter by sector to extract single-name leaders.
- `mcp__uw-pp__options_flow_dte_volume_share` — institutional vs retail share by sector (institutional rotation only counts at high monthly+ share).

Output: rotation regime call (defensive→cyclical / cyclical→defensive / growth→value / value→growth / no_change), per-sector persistence scores, named single-name leaders within each rotating sector, and a one-line swing-book implication.

### opex-pin-strategist — CONDITIONAL: only spawn within 5 days of monthly third-Friday (NEW)
**Conditional spawn.** If TODAY is within 5 calendar days of the monthly third-Friday OPEX, include this agent (12 agents total). Otherwise omit — the orchestrator must not spawn it outside the window.

Tools required:
- `mcp__uw-pp__oi_pin_risk` — pin candidates with strike + probability.
- `mcp__uw-pp__oi_opex_concentration` — OI mass at OPEX strikes; cross-ref against oi_pin_risk for ranking.
- `mcp__uw-pp__options_structure_gex` — confirm pin strike sits inside / adjacent to a long-gamma wall.

Output: ranked OPEX book — top 5–10 names with `{ticker, pin_strike, distance_pct, oi_mass_at_pin, gex_at_pin, ranked_score, suggested_structure}` (iron flies, short straddles, broken-wing butterflies anchored to pin mechanics).

### sweep-tracker — aggressive directional flow
Tools required:
- `mcp__uw-pp__options_flow_sweeps` (today's top 25 by side and premium).
- `mcp__uw-pp__hot_chains_sweep_ratio` — high sweep-to-volume contracts.
- `mcp__uw-pp__hot_chains_smart_money_flow` — ask vs bid imbalance.
- `mcp__uw-pp__hot_chains_sweep_persistence` — rank by persistence count (≥3 of last 5 days). Single-day sweeps are deprioritised.
- `mcp__uw-pp__options_flow_top_premium_trades` (top 20) — the day's whale tickets.
- `mcp__uw-pp__hot_chains_most_active` — for context.

Output: urgency-ranked sweep ledger with side, premium, expiry, persistence count.

### accumulation-hunter — quiet institutional builds
Tools required:
- `mcp__uw-pp__dark_pool_ticker_summary` (top 30 by premium).
- `mcp__uw-pp__dark_pool_largest` (top 25 with NBBO context).
- `mcp__uw-pp__dark_pool_block_stratified` — tier breakdown so retail noise is filtered out of the institutional signal.
- `mcp__uw-pp__dark_pool_price_levels` — institutional support/resistance for any flagged name.
- `mcp__uw-pp__insights_institutional_accumulation` (`lookback_days=5`) — primary signal.
- `mcp__uw-pp__oi_smart_positioning` — bullish/bearish OI inference.
- `mcp__uw-pp__historical_oi_trend` (`lookback_days=5`) — multi-day OI build verification (BUILDING required).
- `mcp__uw-pp__dark_pool_extended_hours` — overnight/pre-market activity that primed the day.

Output: tickers with ≥3 aligned signals across DP, OI, and accumulation_detector.

### contrarian-scanner — overcrowded fades
Tools required:
- `mcp__uw-pp__historical_pc_ratio_zscore` — statistical sentiment extremes (±2σ flags BULLISH_EXTREME / BEARISH_EXTREME). Use this; do **not** use the deprecated `screener_put_call_extremes`.
- `mcp__uw-pp__insights_price_vs_flow` — when smart money disagrees with price.
- `mcp__uw-pp__options_flow_iv_outliers` — high-IV contracts where flow may be exhausted.
- `mcp__uw-pp__oi_decrease_with_volume` — capitulation / profit-taking detection.
- `mcp__uw-pp__screener_iv_rank` (extreme high) — premium ripe to fade.

Output: fade candidates gated on regime — short calls in TRANSITIONAL/RISK_OFF, condors in PIN, no naked shorts in TREND.

### earnings-scout — pre-event flow & vol plays
Tools required:
- `mcp__uw-pp__screener_earnings_catalyst` — upcoming earnings + elevated IV (next 14 days).
- `mcp__uw-pp__insights_earnings_play` — pre-earnings setups with OI positioning.
- `mcp__uw-pp__options_structure_iv_term_structure` — BACKWARDATION = imminent event; KINKED = binary expiry kink.
- `mcp__uw-pp__options_structure_term_skew` — back-month put/call skew at the earnings DTE.
- `mcp__uw-pp__options_structure_front_end_iv_ratio` — quick panic detector.
- `mcp__uw-pp__insights_analyst_vs_flow` — analyst-vs-flow disagreement is the highest-EV setup.

Output: BUY VOL / SELL VOL / SKIP per upcoming print with implied move and IV crush expectation.

### vol-surface-scout — IV dislocations & calendars
Tools required:
- `mcp__uw-pp__options_structure_iv_term_structure` — KINKED / BACKWARDATION / CONTANGO classifier.
- `mcp__uw-pp__options_structure_term_skew` — multi-month skew.
- `mcp__uw-pp__options_flow_iv_outliers` — single-contract IV outliers.
- `mcp__uw-pp__historical_iv_percentile_zscore` — outlier-robust IV percentile (Goyal-Saretto). Use this instead of raw IV rank where possible.
- `mcp__uw-pp__options_flow_expiry_heatmap` — premium concentration by expiry; calendar-spread candidate identification.
- `mcp__uw-pp__screener_iv_rank` — extremes for ranking.

Output: KINKED names, BACKWARDATION calendars, IV outliers with multi-month percentile context.

### multileg-strategist — institutional structure inference
Tools required:
- `mcp__uw-pp__hot_chains_multileg` — primary signal.
- `mcp__uw-pp__options_flow_top_premium_trades` filtered to ≥$1M premium.
- `mcp__uw-pp__options_flow_greek_screener` — directional / vol / vega bets by Greek profile.
- `mcp__uw-pp__options_flow_expiry_heatmap` — concentration by expiry to spot calendar/diagonal builds.

Output: per-ticker structure read (vertical / calendar / fly / condor / ratio / diagonal) with directional thesis and built-in risk caps.

### leap-positioning-radar — long-dated conviction
Tools required:
- `mcp__uw-pp__oi_biggest_increases` (`min_dte=180`) — fresh LEAP positions only.
- `mcp__uw-pp__oi_position_rolls` — same-day near→far DTE rolls.
- `mcp__uw-pp__historical_oi_trend` (`lookback_days=10`) BUILDING required.
- `mcp__uw-pp__historical_cumulative_premium_flow` (default 90d) — LEAP-grade slow accretion signature.
- `mcp__uw-pp__insights_institutional_accumulation` (`lookback_days=10`) — secondary check.
- `mcp__uw-pp__insights_conviction_matrix` — must show DIRECTIONAL_LONG with confidence > 70.

Output: LEAP candidates that pass strict filters — disqualify and explain anything that doesn't.

---

## Step 2 — Phase 2: signal-confluence-quant THEN risk-monitor (sequential)

Phase 2 runs in two stages. The quant produces the audited score; the risk officer gates and sizes against regime/VRP/correlation. Do not collapse them — the separation is the entire point of having auditable conviction math.

### Step 2a — signal-confluence-quant (runs first)

Once **all** Phase 1 agents return, collect every candidate ticker into a single union list with each candidate's flagging agents and named signals. Spawn `signal-confluence-quant` with that union plus the conviction rubric (Step 4 below) as input. It must:

- Run `mcp__uw-pp__insights_signal_confluence` per ticker — confirm or contradict Phase 1 flags.
- Run `mcp__uw-pp__historical_signal_backtest` per ticker, per dominant signal class — pull historical win-rate (or `vol_realisation_rate` for non-directional signals).
- Pull `mcp__uw-pp__historical_cumulative_premium_flow` (30d and 90d) for tie-breaking and supplemental directional context.
- Compute `raw_score` per ticker against the Step 4 rubric, identify `dominant_signal_class`, attach `win_rate`, and emit `final_size_recommendation_pre_risk` (full / half / starter / skip) with a full audit trail per ticker.

Output: a sorted list of `{ticker, raw_score, score_components[], dominant_signal_class, confluence_score, cum_premium_flow_30d/90d, win_rate, final_size_recommendation_pre_risk, audit_trail}`. **The quant does not gate on regime/correlation** — that's risk's job in 2b.

### Step 2b — risk-monitor (runs second, consumes quant output)

Spawn `risk-monitor` with (a) the quant's sorted score list and (b) the Step 0 macro context. It must:

- Run `mcp__uw-pp__risk_portfolio_correlation` against today's candidates (not the static watchlist) — risk is measured against what we're actually considering.
- Confirm `mcp__uw-pp__risk_market_regime` from Step 0 (do not re-fetch).
- Apply the sizing-gate rules from `risk-monitor.md`: −1 tier for regime conflict, −1 tier for `options_structure_front_end_iv_ratio > 1.10` panic, −1 tier for VRP-vs-trade-type contradiction, −1 tier for corr-cluster duplication, −1 tier for adverse sector rotation.
- Pull `mcp__uw-pp__watchlist_alerts` and `mcp__uw-pp__watchlist_scan` against the rolling `conviction_<yesterday>` group — surface adverse-flow exit candidates.
- Persist today's top-5 conviction names via `mcp__uw-pp__watchlist_manage(action="add", group="conviction_<date>")`.

Output: correlation clusters (corr > 0.7 = treat as one position), regime conflicts, VRP / panic gates applied, adverse-flow exit list, hedge sleeve recommendation, and a final sizing table per ticker that consumes the quant's `final_size_recommendation_pre_risk` and applies the gate stack.

---

## Step 3 — Confluence gate

Before scoring, apply the **confluence gate**: a ticker only enters the conviction rubric if **at least two distinct Phase 1 agents flag it positively** OR **one Phase 1 agent flags it AND `mcp__uw-pp__insights_signal_confluence` rates it ≥4**. Names with only one signal class but no confluence backing are noted in §8 ("Watch-only — single signal") and excluded from the high-conviction list. This rule prevents single-tool false positives from contaminating the trade book.

### Step 3a — HIGH-tier load-bearing-tool gate (2026-05-09 audit P0, hardened 2026-05-15 audit P1.3, expanded to 3-of-5 by 2026-05-23 audit P0.2)

After scoring, before any candidate enters the HIGH-tier section of §3 / §7 (i.e. anything that would be sized as `full` post-quant), the call must additionally cite at least **3 of the 5 LOAD-BEARING tools** (added `insights_signal_confluence` on 2026-05-23):

- `dark_pool_block_stratified` (institutional-vs-retail filter)
- `historical_cumulative_premium_flow` (30d directional accretion)
- `insights_institutional_accumulation`
- `options_structure_dex` (DEX)
- `insights_signal_confluence` (second-agent confirmation — added 2026-05-23 P0.2; Phase 4 +19.5pp marginal, LOAD-BEARING)

A call that scores raw_score ≥ 10 (HIGH-tier under the 2026-05-15 cuts) but cites fewer than 3 of these five tools must be **demoted to MEDIUM tier**. Phase 3 of the 2026-05-23 audit detected tier inversion (HIGH 60.0% < MED 62.5%) under the prior 3-of-4 gate; Phase 5 W21 holdout shows the 3-of-5 gate restores tier monotonicity (HIGH 0.80 / MED 0.50 / LOW 0.50). Half-baked "accumulation only" HIGH calls (e.g. MA 5/18, BL 5/19) demote to MED — both lost in resolved outcomes, so the demote is correct in retrospect.

---

## Step 4 — Conviction scoring rubric (applied by signal-confluence-quant in Step 2a)

The rubric below is what `signal-confluence-quant` consumes in Step 2a to produce the audited score. The quant attaches every signed point to a named source agent + tool in `score_components`. Risk-monitor in Step 2b applies the regime / VRP / cluster gates **on top of** this score.

```
Daily conviction score = Σ:
  +3  dealer-positioning-strategist flags DEX flip or vanna-squeeze setup in trade direction
  +3  3+ aligned signals in accumulation-hunter (DP + OI + oi_smart_positioning, dark_pool_block_stratified institutional-tier confirmed)   # was +2; promoted 2026-05-15 audit P1.2 — Phase 4 +27.8pp marginal contribution (LOAD-BEARING)
  +1  multi-day OI build (historical_oi_trend BUILDING, lookback ≥ 5 days)                       # was +2; reduced 2026-05-09 (Phase 4 +5pp marginal — supportive, not load-bearing; correlated with the LOAD-BEARING components above)
  +1  insights_conviction_matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL ONLY (2026-05-23 audit P1.1): award +1 only when dominant_signal_class == leap_directional; in all non-LEAP contexts contribution is 0. Phase 4: marginal contribution −23pp (n=8) on swing horizon; the DIRECTIONAL_LONG/>70 signature appears to be a mean-reversion-fade (top-pick) signature outside LEAP. LEAP gate in leap-positioning-radar still consumes this tool — only the swing-rubric award is gated to leap_directional.
  +3  historical_cumulative_premium_flow shows net directional accretion in trade direction (30d window)   # was +2; promoted 2026-05-15 audit P1.2 — Phase 4 +24.2pp marginal contribution (LOAD-BEARING)
  +2  insights_signal_confluence ≥4 (second-agent confirmation)   # NEW 2026-05-23 audit P1.2 — Phase 4 +19.5pp marginal contribution (n=12, LOAD-BEARING); also added to the 3-of-5 LB gate in Step 3a
  # +1 line for hot_chains_sweep_persistence top-5 REMOVED 2026-05-23 audit P0.3
  # Reason: marginal contribution −22pp two consecutive audits (n=15); mega-cap suppression rule from 2026-05-15 P1.1 was insufficient.
  # Tool remains informational — sweep-tracker still surfaces persistence-ranked sweeps in §2/§3/§7 prose — but contributes 0 points to raw_score.
  # If the call merits a multileg or accumulation co-flag, those tools earn the score instead.
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector — CONDITIONAL (2026-05-23 audit P1.5): award +1 only when (a) sector persistence_score ≥3 AND (b) cum_premium_flow_30d direction aligned with thesis direction AND (c) |cum_flow_30d| ≥ $50M. Default 0. Phase 4: sector_persistence marginal +2.8pp standalone (NO-INFO); when paired with cum_flow alignment, it was the difference between HON-W21 (+4.9% WIN) and WMT-W19 (−10.4% LOSS, flow disagreed).
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)   # was +1; promoted 2026-05-09 (Phase 4 +8pp marginal; multileg-vs-batch_strategy disagreements correctly resolved 5/5 in dataset)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising historical_pc_ratio_zscore (VRP positive)
  -3  flow_conflict — signal-confluence-quant applies mechanically when historical_cumulative_premium_flow 30d direction is *clearly opposite* dominant_signal_class (signed-sum sign flip + magnitude > today's union-median |cum_flow_30d|, or explicit OPPOSITE label)   # 2026-05-15 audit P0 — see signal-confluence-quant.md "Mechanical flow_conflict deduction" rule; 2026-05-23 audit P1.3: mutually exclusive with flow_conflict_lite (apply ONE, never both)
  -1  flow_conflict_lite — signal-confluence-quant applies when the 30d cum_premium_flow read is MIXED (signed sum near zero, or aligned but bottom-quartile magnitude in today's union)   # 2026-05-15 audit P0; 2026-05-23 audit P1.3: mutually exclusive with flow_conflict (apply ONE, never both)
  # 2026-05-09 -2 generic flow_conflict line replaced with the mechanical -3 / -1 split above (Phase 3 2026-05-15 audit: 30% missed-gate rate at the generic line; NVDA 2026-05-08 raw=10 LOSS dominated by un-penalised flow_conflict against −$17.89M cum_flow_30d)
  -1  risk-monitor flags in correlation cluster (corr > 0.7) — applied in 2b on top of raw score
  -3  risk_market_regime conflicts with trade direction — applied in 2b

# Removed from swing/LEAP scoring 2026-05-09 (Phase 4 audit, NO-INFO ±0pp on swing horizon):
#   gamma-flip-tracker 0DTE breakout setup (regime flip + flow alignment) — formerly +2.
#   The signal continues to drive §2 (0DTE / Intraday Plays) directly, but does NOT earn rubric points
#   on swing or LEAP rows. This component double-counted with dealer-positioning's +3 DEX flip.
```

**Conviction tiers (2026-05-15 audit P0; supersedes prior `≥ 5` HIGH cut and the deferred R-09 from 2026-05-09):**

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 10 | **HIGH** | full size (subject to Step 3a load-bearing-tool gate + Step 5 win-rate gate) |
| 7 – 9 | **MEDIUM** | half size (subject to Step 5 win-rate gate) |
| 3 – 6 | **LOW** | starter / watch-only — supporting candidate in §3/§4, not surfaced in Executive Summary or §7 |
| ≤ 2 | drop | filtered by quant's drop floor |

Surface every **HIGH and MEDIUM** ticker in the Executive Summary and §7 (High-Conviction Cross-Ref). LOW tier names appear in §3/§4 as supporting candidates only. These cuts align daily with weekly tiering; the gap between the prior daily HIGH (≥5) and weekly HIGH (≥9) was the largest source of inter-skill inconsistency in the 2026-05-15 audit.

---

## Step 5 — Backtest-weighted sizing

For each HIGH or MEDIUM tier ticker (raw_score ≥ 7 under the 2026-05-15 cuts), identify its dominant signal class — typical labels: `dark_pool_accumulation`, `multi_day_sweep`, `gamma_breakout`, `oi_build`, `leap_directional`, `bullish_flow`, `bearish_flow`, `multileg_directional`. Call `mcp__uw-pp__historical_signal_backtest` with that signal class and the ticker. Apply this sizing map (**2026-05-15 audit PC.1**; full-size threshold tightened 0.65 → 0.70 after Phase 3 quintile data showed only Q5 raw≥9 realised >0.65; Q4 raw 6–8 realised 0.571 — sub-0.65, deserves half not full):

| `win_rate` | Position size |
|---|---|
| ≥ 0.70 | full size |
| 0.50 – 0.70 | half size |
| < 0.50 | starter / skip |

For non-directional signals (`high_iv_rank`, `volume_spike`) the backtest returns `vol_realisation_rate` instead — use the same thresholds. Note the win_rate explicitly next to each top call.

---

## Step 6 — Deep dive on the top 3 by conviction

For each of the **top 3 tickers by conviction score**:
1. Call `mcp__uw-pp__insights_deep_dive` — full Yahoo + UW data for full thesis verification.
2. Call `mcp__uw-pp__historical_trend` (`lookback_days=10`) — confirm the multi-day price/flow trend.

This step is the synthesis bridge from "signal" to "thesis" — without it, conviction scores are abstract.

---

## Step 6.5 — Batched strategy synthesis on the conviction list

For the entire **HIGH and MEDIUM tier** list (raw_score ≥ 7), make a **single** `mcp__uw-pp__playbook_batch_scan` call with the full ticker list. This replaces per-ticker `playbook_suggest_strategy` calls — one batch call is materially cheaper and produces consistent strategy logic across the book.

Cross-reference each batched recommendation against any named structure from `multileg-strategist`. **Prefer the multileg read** when the two disagree (multileg saw the actual coordinated flow; the rule-based scan is a heuristic) and note the disagreement in §3 / §7 of the report.

---

## Step 7 — Write the report

Synthesize into the structured markdown below. The report is organized **by trade horizon**, not by agent. Use tables for data-dense sections and full sentences for thesis sections. Tone: institutional desk strategist — precise, assertive, no filler.

```markdown
# Daily Market Analysis — YYYY-MM-DD

## Executive Summary
- **Regime + GEX state:** <one line — regime label, SPY/QQQ/IWM gamma, VIX, breadth, sector lean>
- **Top 0DTE play:** <ticker, structure, thesis, invalidation> or "no edge"
- **Top swing build:** <ticker, thesis, structure, invalidation, win_rate, size>
- **Top LEAP candidate:** <ticker, scenario, structure, invalidation, win_rate, size>
- **Biggest risk:** <correlation cluster name, members, hedge sleeve>

## 1. Regime & Gamma State
- `risk_market_regime` reading + breadth narrative
- Per-index gamma table: spot | zero-gamma | total GEX | regime | call wall | put wall (rows: SPY/QQQ/IWM)
- `options_flow_dte_volume_share` summary (institutional vs retail share)
- `historical_vrp` classification

## 2. 0DTE / Intraday Plays
- gamma-flip-tracker per-ticker plays (PIN / TREND / NEAR_FLIP) for **today**
- Urgency-ranked sweeps from sweep-tracker with near-term expiry (persistence-ranked first)
- OPEX-week pinning candidates from `opex-pin-strategist` if applicable (with suggested structure per name)

## 2a. Swing Dealer Positioning (1–4 weeks)
- `dealer-positioning-strategist` outputs: DEX flips, vanna-squeeze flags, ZGL trajectory regime flips
- Names with `swing_bias=LONG/SHORT` get carried into §3 with the dealer-positioning tag

## 2b. Sector Rotation
- `sector-rotation-strategist`: rotating-into / rotating-out-of sectors with persistence scores
- Rotation regime call (defensive→cyclical / cyclical→defensive / growth→value / value→growth / no_change)
- Single-name leaders feed §3 with the `sector_rotation` tag

## 3. Swing Setups (1–6 weeks)
Ranked by conviction score. Table: Ticker | Score | Thesis | Structure | Invalidation | Sizing.
Subdivide into:
- **3a. Long swings (regime-aligned)** — accumulation + multileg directional + earnings BUY VOL + dealer-positioning vanna-squeeze + sector-rotation leaders.
- **3b. Short / fade swings (defined risk only)** — contrarian + earnings SELL VOL + analyst-vs-flow disagreement + dealer-positioning DEX-flip-short.

## 4. LEAP Builds (6–24 months)
leap-positioning-radar — DIRECTIONAL_LONG only with full disqualification notes for near-misses.

## 5. Volatility Surface
vol-surface-scout — KINKED names, BACKWARDATION calendars, IV outliers, calendar-spread candidates with implied move per name.

## 6. Risk & Correlation
risk-monitor consuming today's Phase 1 candidate union and the quant's audited score (not the static watchlist) — clusters, regime conflicts, VRP / panic gates applied, hedge sleeve recommendations.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
Per-ticker breakdown sourced from the `signal-confluence-quant` audit trail: `raw_score` | `score_components[]` (with named source agent + tool per component) | `dominant_signal_class` | `win_rate` | pre-risk size | risk-monitor gates applied | final size | invalidation level.

Embed the conviction-scoring rubric (Step 4) verbatim at the bottom of §7 so future readers can audit the scores.

## 8. Watch-only — single signal, no confluence
Candidates that surfaced from one agent but failed the confluence gate. Listed for journaling, NOT for trade entry today.
```

---

## Step 8 — Confirm watchlist write-back (handled by risk-monitor in Step 2b)

The top-5 watchlist write-back is performed inside `risk-monitor` during Step 2b — the agent calls `mcp__uw-pp__watchlist_manage(action="add", group="conviction_<YYYY-MM-DD>")` with today's top 5 by conviction score. **Do not double-write here.**

Confirm the write-back happened by checking the `risk-monitor` output for the explicit `watchlist_write_back_confirmation` field. If missing, call `mcp__uw-pp__watchlist_manage(action="add", group="conviction_<YYYY-MM-DD>", tickers=[<top_5_by_score>])` directly as a fallback.

If any name was already on a manually-curated group, leave that membership alone — write only to the date-stamped group. This closes the feedback loop: today's high-conviction names become tomorrow's correlation universe, and tomorrow's RM automatically pulls `watchlist_alerts` against them to flag adverse-flow exit candidates.

---

## Step 9 — Save and report

1. Use Write to save the report to `analyses/YYYY-MM-DD.md`.
2. Confirm the file was written (the Write tool errors loudly on failure — no need to re-Read it).
3. Print the **Executive Summary** section to chat. Nothing else — the user opens the file for the rest.

---

## Failure modes & recovery

- **Phase 1 agent times out** — re-spawn just that agent with the same context block. If it fails twice, write its section as `[agent timed out — see <agent-name> logs]` and proceed; do not let one agent block the report.
- **`playbook_daily_synthesis` returns empty** — fall back to manually composing the macro context from `risk_market_regime` + `insights_signal_confluence` + `watchlist_alerts` and continue.
- **`historical_available_dates` shows stale data** — abort and ask the user to re-export from Unusual Whales. Do not proceed with stale data.
- **No tickers clear the confluence gate** — produce a report whose §3 and §4 are explicitly empty, with the regime + 0DTE sections still populated. A "no edge" day is a valid output, not a failure.
