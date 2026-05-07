---
description: Run the full post-market daily intelligence report — regime + GEX + sector flow + sweeps + dark pool + OI + vol surface + LEAP + earnings, organized by trade horizon (0DTE / Swing / LEAP). Two-phase agent fleet with formal conviction scoring, backtest-weighted sizing, and watchlist write-back. Invoke whenever the user asks for an end-of-day or post-market analysis, a daily market report, an EOD briefing, or types `/daily-analysis`. Do NOT trigger for single-ticker deep dives, single-tool queries (e.g. "show me sweeps"), pre-market only briefings (use `daily_synthesis` directly), or weekly summaries (use `/weekly-analysis`).
---

# Daily Market Analysis

Run a full post-market intelligence report by trade horizon (0DTE / Swing / LEAP). Two phases: Phase 1 spawns 8 alpha-finding agents in parallel against a shared macro context; Phase 2 runs `risk-monitor` against the candidate set Phase 1 surfaced. Every ticker is scored against a formal conviction rubric, top names are backtested for win-rate before sizing, and the top 5 are written back to the watchlist so tomorrow's run measures correlation against today's calls. Save to `analyses/YYYY-MM-DD.md`.

## When to invoke

- Post-market daily report ("EOD analysis", "end of day report", "wrap up the day", "daily intel")
- Slash command `/daily-analysis`
- "Morning briefing" — but only if it should integrate Phase 1 specialist agents. For a fast sub-2-minute briefing, just call `mcp__uw-playbook__daily_synthesis` directly without spawning the fleet.

## When NOT to invoke

- "What's NVDA doing?" → `mcp__uw-insights__stock_deep_dive`, not the full pipeline.
- "Show me today's sweeps" → `mcp__uw-options-flow__sweep_detector` directly.
- "Find earnings plays this week" → spawn `earnings-scout` alone.
- "Build me a watchlist" → `mcp__uw-watchlist__manage_watchlist` directly.
- "Recap the week" → `/weekly-analysis`, not `/daily-analysis`.

## Operating principle: prefer multi-day metrics over single-day snapshots

Every spawned agent must prefer multi-day persistence tools over single-day equivalents wherever the MCP supports it. Specifically: `mcp__uw-historical__oi_trend` over `mcp__uw-oi__biggest_oi_increases`, `mcp__uw-hotchains__multi_day_sweep_persistence` over `mcp__uw-options-flow__sweep_detector` for ranking, `mcp__uw-options-flow__sector_flow_persistence` over `sector_flow_summary` for rotation calls, `mcp__uw-historical__pc_ratio_zscore` over the deprecated `put_call_ratio_extremes`, and `mcp__uw-historical__signal_backtest` before sizing any trade. Single-day signals are noise; multi-day persistence is the edge. Pass this instruction through to every spawned agent.

---

## Step 0 — Preflight & shared macro context

This step builds the shared context every Phase 1 agent receives. **Do not skip any sub-step** — agents that lack the macro anchor produce inconsistent calls.

1. **Date** — run `date +%F` to get today's `YYYY-MM-DD`. This is the report filename, the `conviction_<date>` watchlist group key, and the date passed to every MCP tool.

2. **Coverage check** — call `mcp__uw-historical__available_dates`. Confirm today's date is present. If the latest date lags more than one trading day, abort and tell the user "UW data is stale by N days — re-export from Unusual Whales before running."

3. **One-call briefing** — call `mcp__uw-playbook__daily_synthesis` with today's date. This returns the regime classification, top bullish/bearish confluence tickers, and watchlist alerts in a single call — the shared context anchor for every Phase 1 agent. **Pass this synthesis output to every agent in Step 1** so they don't redundantly re-call `market_regime` or `signal_confluence`.

4. **Macro layer** — call these in parallel and capture the readings:
   - `mcp__uw-risk__market_regime` — SPY/VIX trend + breadth classification (will be the top-line of §1 of the report).
   - `mcp__uw-options-flow__dte_volume_share` — share by 0DTE / weekly / monthly / LEAP. High 0DTE share = retail-dominated tape; high monthly+ share = institutional positioning. This is the regime hint Phase 1 agents need to interpret their own findings.
   - `mcp__uw-historical__volatility_risk_premium` — IV30 vs realised σ30. Whether the day is a premium-selling or premium-buying environment changes which Phase 1 agents you trust most (selling environment → vol-surface-scout & contrarian-scanner; buying environment → gamma-flip-tracker & earnings-scout).

5. **Sector layer** — call in parallel:
   - `mcp__uw-options-flow__sector_flow_summary` — single-day sector premium balance (snapshot).
   - `mcp__uw-options-flow__sector_flow_persistence` — multi-day rotation persistence score (the durability check that gates §2 of the report).

6. **Top-of-funnel screens** — run in parallel:
   - `mcp__uw-screener__bullish_bearish_screener` (top 25 each side) — net premium leaderboard.
   - `mcp__uw-insights__signal_confluence` (`min_score=3`, top 25 each direction) — multi-factor scoring; agents start their hunts here.
   - `mcp__uw-screener__volume_vs_average` (top 25, `min_ratio=3`) — flow anomalies vs 30-day baseline.
   - `mcp__uw-screener__iv_rank_screener` (top 25 high, top 25 low) — premium-selling and premium-buying candidates.

7. **OPEX guard** — if today is within 5 calendar days of the third Friday, also call `mcp__uw-oi__pin_risk_screener` and `mcp__uw-oi__opex_concentration` for SPY/QQQ/IWM and any name in the top of step 6. Pinning candidates feed §2 (0DTE) directly.

The output of Step 0 is a compact JSON-shaped context block: `{date, regime, vrp_classification, dte_share, sector_summary, sector_persistence, top_bullish, top_bearish, confluence, volume_outliers, iv_extremes, opex_pin_candidates}`. Every Phase 1 agent receives this verbatim.

---

## Step 1 — Phase 1: alpha-finding agents (parallel, single batch)

Spawn these 8 agents **simultaneously** — a single message with 8 Agent tool calls. Hand each one the Step 0 context block and the explicit MCP tool list below. The named tools are the minimum each agent must consult; agents can pull additional tools from their own descriptions if their finding is surprising.

### gamma-flip-tracker — dealer hedging map (0DTE & intraday)
Tools required:
- `mcp__uw-options-structure__today_gamma_flip` — 0DTE zero-gamma + ATM flip for SPY/QQQ/IWM and any name with significant 0DTE volume from Step 0.
- `mcp__uw-options-structure__gamma_exposure_profile` — per-strike GEX, default `dte_max=45`. Flag the call wall and put wall.
- `mcp__uw-options-structure__dealer_delta_exposure` (DEX) — pre-directional move signal; DEX flips often precede price moves (Karsan / SqueezeMetrics).
- `mcp__uw-options-structure__vanna_charm_exposure` — vanna-squeeze setup detector; flag put-heavy book + falling VIX.
- `mcp__uw-historical__gex_time_series` (lookback 10–30 days) — multi-day ZGL trajectory for context.
- `mcp__uw-options-structure__front_end_iv_ratio` — ratio > 1.05 confirms backwardation / panic.

Output: per-index regime label (PIN / TREND / NEAR_FLIP), single-name pin candidates, vanna-squeeze flags.

### sweep-tracker — aggressive directional flow
Tools required:
- `mcp__uw-options-flow__sweep_detector` (today's top 25 by side and premium).
- `mcp__uw-hotchains__sweep_ratio_scanner` — high sweep-to-volume contracts.
- `mcp__uw-hotchains__smart_money_flow` — ask vs bid imbalance.
- `mcp__uw-hotchains__multi_day_sweep_persistence` — rank by persistence count (≥3 of last 5 days). Single-day sweeps are deprioritised.
- `mcp__uw-options-flow__top_premium_trades` (top 20) — the day's whale tickets.
- `mcp__uw-hotchains__most_active_contracts` — for context.

Output: urgency-ranked sweep ledger with side, premium, expiry, persistence count.

### accumulation-hunter — quiet institutional builds
Tools required:
- `mcp__uw-darkpool__dark_pool_ticker_summary` (top 30 by premium).
- `mcp__uw-darkpool__largest_dark_pool_trades` (top 25 with NBBO context).
- `mcp__uw-darkpool__dp_block_size_stratified` — tier breakdown so retail noise is filtered out of the institutional signal.
- `mcp__uw-darkpool__dark_pool_price_levels` — institutional support/resistance for any flagged name.
- `mcp__uw-insights__institutional_accumulation_detector` (`lookback_days=5`) — primary signal.
- `mcp__uw-oi__smart_positioning` — bullish/bearish OI inference.
- `mcp__uw-historical__oi_trend` (`lookback_days=5`) — multi-day OI build verification (BUILDING required).
- `mcp__uw-darkpool__extended_hours_filter` — overnight/pre-market activity that primed the day.

Output: tickers with ≥3 aligned signals across DP, OI, and accumulation_detector.

### contrarian-scanner — overcrowded fades
Tools required:
- `mcp__uw-historical__pc_ratio_zscore` — statistical sentiment extremes (±2σ flags BULLISH_EXTREME / BEARISH_EXTREME). Use this; do **not** use the deprecated `put_call_ratio_extremes`.
- `mcp__uw-insights__price_vs_flow_divergence` — when smart money disagrees with price.
- `mcp__uw-options-flow__iv_outliers` — high-IV contracts where flow may be exhausted.
- `mcp__uw-oi__oi_decrease_with_volume` — capitulation / profit-taking detection.
- `mcp__uw-screener__iv_rank_screener` (extreme high) — premium ripe to fade.

Output: fade candidates gated on regime — short calls in TRANSITIONAL/RISK_OFF, condors in PIN, no naked shorts in TREND.

### earnings-scout — pre-event flow & vol plays
Tools required:
- `mcp__uw-screener__earnings_catalyst_scanner` — upcoming earnings + elevated IV (next 14 days).
- `mcp__uw-insights__earnings_play_analyzer` — pre-earnings setups with OI positioning.
- `mcp__uw-options-structure__iv_term_structure` — BACKWARDATION = imminent event; KINKED = binary expiry kink.
- `mcp__uw-options-structure__term_skew` — back-month put/call skew at the earnings DTE.
- `mcp__uw-options-structure__front_end_iv_ratio` — quick panic detector.
- `mcp__uw-insights__analyst_vs_flow` — analyst-vs-flow disagreement is the highest-EV setup.

Output: BUY VOL / SELL VOL / SKIP per upcoming print with implied move and IV crush expectation.

### vol-surface-scout — IV dislocations & calendars
Tools required:
- `mcp__uw-options-structure__iv_term_structure` — KINKED / BACKWARDATION / CONTANGO classifier.
- `mcp__uw-options-structure__term_skew` — multi-month skew.
- `mcp__uw-options-flow__iv_outliers` — single-contract IV outliers.
- `mcp__uw-historical__iv_percentile_zscore` — outlier-robust IV percentile (Goyal-Saretto). Use this instead of raw IV rank where possible.
- `mcp__uw-options-flow__expiry_heatmap` — premium concentration by expiry; calendar-spread candidate identification.
- `mcp__uw-screener__iv_rank_screener` — extremes for ranking.

Output: KINKED names, BACKWARDATION calendars, IV outliers with multi-month percentile context.

### multileg-strategist — institutional structure inference
Tools required:
- `mcp__uw-hotchains__multileg_activity` — primary signal.
- `mcp__uw-options-flow__top_premium_trades` filtered to ≥$1M premium.
- `mcp__uw-options-flow__greek_screener` — directional / vol / vega bets by Greek profile.
- `mcp__uw-options-flow__expiry_heatmap` — concentration by expiry to spot calendar/diagonal builds.

Output: per-ticker structure read (vertical / calendar / fly / condor / ratio / diagonal) with directional thesis and built-in risk caps.

### leap-positioning-radar — long-dated conviction
Tools required:
- `mcp__uw-oi__biggest_oi_increases` (`min_dte=180`) — fresh LEAP positions only.
- `mcp__uw-oi__position_rolling_detector` — same-day near→far DTE rolls.
- `mcp__uw-historical__oi_trend` (`lookback_days=10`) BUILDING required.
- `mcp__uw-historical__cumulative_premium_flow` (default 90d) — LEAP-grade slow accretion signature.
- `mcp__uw-insights__institutional_accumulation_detector` (`lookback_days=10`) — secondary check.
- `mcp__uw-insights__conviction_matrix` — must show DIRECTIONAL_LONG with confidence > 70.

Output: LEAP candidates that pass strict filters — disqualify and explain anything that doesn't.

---

## Step 2 — Phase 2: risk monitor (sequential, consumes Phase 1)

Once **all** Phase 1 agents return, collect every candidate ticker each agent surfaced into a single union list. Spawn `risk-monitor` with that union as input. It must:

- Run `mcp__uw-risk__portfolio_correlation` against today's candidates (not the static watchlist) — risk is measured against what we're actually considering.
- Re-confirm `mcp__uw-risk__market_regime` and tag any candidate whose direction conflicts with regime.
- Run `mcp__uw-insights__signal_confluence` over the candidate union to flag aligned clusters.

Output: correlation clusters (corr > 0.7 = treat as one position), regime conflicts, and an adverse-flow flag per ticker.

---

## Step 3 — Confluence gate

Before scoring, apply the **confluence gate**: a ticker only enters the conviction rubric if **at least two distinct Phase 1 agents flag it positively** OR **one Phase 1 agent flags it AND `mcp__uw-insights__signal_confluence` rates it ≥4**. Names with only one signal class but no confluence backing are noted in §8 ("Watch-only — single signal") and excluded from the high-conviction list. This rule prevents single-tool false positives from contaminating the trade book.

---

## Step 4 — Conviction scoring (formal rubric)

For every ticker that cleared the confluence gate, compute the conviction score:

```
Daily conviction score = Σ:
  +3  flagged by gamma-flip-tracker as setting up a regime breakout (DEX flip or vanna-squeeze)
  +2  3+ aligned signals in accumulation-hunter (DP + OI + smart_positioning)
  +2  multi-day OI build (oi_trend BUILDING, lookback ≥ 5 days)
  +2  conviction_matrix = DIRECTIONAL_LONG, confidence > 70
  +1  in sweep-tracker top 5 by persistence count
  +1  in earnings-scout BUY VOL or SELL VOL
  +1  in multileg-strategist with directional structure
  +1  in vol-surface-scout KINKED or BACKWARDATION watch
  -2  contrarian-scanner flags as overcrowded long with rising pc_ratio_zscore
  -1  risk-monitor flags in correlation cluster (corr > 0.7)
  -3  market_regime conflicts with the trade direction
```

Surface every ticker with **score ≥ 5** in the Executive Summary and §7 (High-Conviction Cross-Ref). Tickers with score 3–4 go into §3/§4 as supporting candidates. Tickers below 3 are dropped.

---

## Step 5 — Backtest-weighted sizing

For each ticker scoring ≥ 5, identify its dominant signal class — typical labels: `dark_pool_accumulation`, `multi_day_sweep`, `gamma_breakout`, `oi_build`, `leap_directional`, `bullish_flow`, `bearish_flow`, `multileg_directional`. Call `mcp__uw-historical__signal_backtest` with that signal class and the ticker. Apply this sizing map to every conviction ≥5 call:

| `win_rate` | Position size |
|---|---|
| ≥ 0.65 | full size |
| 0.50 – 0.65 | half size |
| < 0.50 | starter / skip |

For non-directional signals (`high_iv_rank`, `volume_spike`) the backtest returns `vol_realisation_rate` instead — use the same thresholds. Note the win_rate explicitly next to each top call.

---

## Step 6 — Deep dive + strategy synthesis on the top 3

For each of the **top 3 tickers by conviction score**:
1. Call `mcp__uw-insights__stock_deep_dive` — full Yahoo + UW data for full thesis verification.
2. Call `mcp__uw-historical__trend_analyzer` (`lookback_days=10`) — confirm the multi-day price/flow trend.
3. Call `mcp__uw-playbook__suggest_strategy` — get the rule-based options-strategy recommendation. Use this as the structure suggestion in the Executive Summary unless it conflicts with a named call from multileg-strategist (in which case prefer the multileg read and note the disagreement).

This step is the synthesis bridge from "signal" to "trade" — without it, conviction scores are abstract.

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
- `market_regime` reading + breadth narrative
- Per-index gamma table: spot | zero-gamma | total GEX | regime | call wall | put wall (rows: SPY/QQQ/IWM)
- `dte_volume_share` summary (institutional vs retail share)
- `volatility_risk_premium` classification

## 2. 0DTE / Intraday Plays
- gamma-flip-tracker per-ticker plays (PIN / TREND / NEAR_FLIP)
- Urgency-ranked sweeps from sweep-tracker with near-term expiry
- OPEX-week pinning candidates if applicable

## 3. Swing Setups (1–6 weeks)
Ranked by conviction score. Table: Ticker | Score | Thesis | Structure | Invalidation | Sizing.
Subdivide into:
- **3a. Long swings (regime-aligned)** — accumulation + multileg directional + earnings BUY VOL.
- **3b. Short / fade swings (defined risk only)** — contrarian + earnings SELL VOL + analyst-vs-flow disagreement.

## 4. LEAP Builds (6–24 months)
leap-positioning-radar — DIRECTIONAL_LONG only with full disqualification notes for near-misses.

## 5. Volatility Surface
vol-surface-scout — KINKED names, BACKWARDATION calendars, IV outliers, calendar-spread candidates with implied move per name.

## 6. Risk & Correlation
risk-monitor consuming today's Phase 1 candidate union (not the static watchlist) — clusters, regime conflicts, hedge sleeve recommendations.

## 7. High-Conviction Cross-Ref (score ≥ 5)
Per-ticker breakdown: score components | win_rate | size | invalidation level.

Embed the conviction-scoring rubric verbatim at the bottom of §7 so future readers can audit the scores.

## 8. Watch-only — single signal, no confluence
Candidates that surfaced from one agent but failed the confluence gate. Listed for journaling, NOT for trade entry today.
```

---

## Step 8 — Watchlist write-back

Take the top 5 tickers by conviction score (descending) and persist them so tomorrow's `risk-monitor` automatically tracks today's calls:

```
mcp__uw-watchlist__manage_watchlist(
  action="add",
  group="conviction_<YYYY-MM-DD>",
  tickers=[<top_5_by_score>]
)
```

If any name was already on a manually-curated group, leave that membership alone — write only to the date-stamped group. This closes the feedback loop: today's high-conviction names become tomorrow's correlation universe.

---

## Step 9 — Save and report

1. Use Write to save the report to `analyses/YYYY-MM-DD.md`.
2. Confirm the file was written (the Write tool errors loudly on failure — no need to re-Read it).
3. Print the **Executive Summary** section to chat. Nothing else — the user opens the file for the rest.

---

## Failure modes & recovery

- **Phase 1 agent times out** — re-spawn just that agent with the same context block. If it fails twice, write its section as `[agent timed out — see <agent-name> logs]` and proceed; do not let one agent block the report.
- **`daily_synthesis` returns empty** — fall back to manually composing the macro context from `market_regime` + `signal_confluence` + `watchlist_alerts` and continue.
- **`available_dates` shows stale data** — abort and ask the user to re-export from Unusual Whales. Do not proceed with stale data.
- **No tickers clear the confluence gate** — produce a report whose §3 and §4 are explicitly empty, with the regime + 0DTE sections still populated. A "no edge" day is a valid output, not a failure.
