---
description: Run the full post-market daily intelligence report — regime + GEX + sector flow + sweeps + dark pool + OI + vol surface + LEAP + earnings, organized by trade horizon (0DTE / Swing / LEAP). Two-phase agent fleet with formal conviction scoring, backtest-weighted sizing, and watchlist write-back. Invoke whenever the user asks for an end-of-day or post-market analysis, a daily market report, an EOD briefing, or types `/daily-analysis`. Do NOT trigger for single-ticker deep dives, single-tool queries (e.g. "show me sweeps"), pre-market only briefings (use `playbook_daily_synthesis` directly), or weekly summaries (use `/weekly-analysis`).
---

# Daily Market Analysis

Run a full post-market intelligence report by trade horizon (0DTE / Swing / LEAP). Two phases: Phase 1 spawns **11 alpha-finding agents** (12 in OPEX week) in parallel against a shared macro context (including a FRED macro snapshot + forward event-risk calendar); Phase 2 runs `signal-confluence-quant` for an audited conviction score, then a `fundamentals-gate` cross-check and a bounded `bull-researcher`/`bear-researcher` debate on the top-5, then `risk-monitor` to gate and size. Every ticker is scored against a formal conviction rubric, top names are backtested for win-rate and fundamentally vetted before sizing, the top 5 are written back to the watchlist, and a machine-readable `decision.json` envelope is emitted beside the report. Each run gets its own folder: `analyses/daily/YYYY-MM-DD/` holding `report.md` + `decision.json`.

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

   These two are **GICS-aggregate** (no symbol input) — they are the shared anchor. The **ETF instrument-level flow tape** (the canonical ETF universe defined in `sector-rotation-strategist.md`) is swept **per-symbol by the agent in Step 1**, not here — do **not** add the ~21 per-symbol ETF calls to preflight. The agent owns the ranked deep-pull; Step 0 stays GICS-aggregate.

6. **Top-of-funnel screens** — run in parallel:
   - `mcp__uw-pp__screener_bullish_bearish` (top 25 each side) — net premium leaderboard.
   - `mcp__uw-pp__insights_signal_confluence` (`min_score=3`, top 25 each direction) — multi-factor scoring; agents start their hunts here.
   - `mcp__uw-pp__screener_volume_vs_average` (top 25, `min_ratio=3`) — flow anomalies vs 30-day baseline.
   - `mcp__uw-pp__screener_iv_rank` (top 25 high, top 25 low) — premium-selling and premium-buying candidates.

   **Liquidity floor (2026-05-25 register C12) — apply to every screened name before handing to agents.** Each candidate must clear **price ≥ $5 AND 20-day dollar-ADV ≥ $50M** (or notional-equivalent). Use the screener `close` for price and a 20-day dollar-volume estimate (equity `volume × close`, or yahoo `get_historical_stock_prices` for the underlying; "notional-equivalent" = options dollar volume where equity ADV is unavailable). **Fail closed:** a name whose liquidity cannot be verified is dropped, not passed. ADV is **dollar** volume (shares × close), *not* a raw share count. Drop sub-floor names from the funnel entirely — they pollute the candidate set, the confluence breadth, and the win-rate denominator. **This floored set is the funnel every downstream step consumes** — the OPEX guard (sub-step 7), all Phase 1 agents (Step 1), and the quant's win-rate denominator (Step 5) operate on the floored names, never the raw screener output. Rationale: the `volume_spike` screen returns micro-ETFs (GIF/BLCN/PEX/IGLD/UTHY/ESGE — all sub-$50M ADV) the desk cannot fill at size; Barbon & Buraschi show flow effects are strongest (and least exitable) in exactly these illiquid names. The reusable filter is `scripts/excess_winrate.py:apply_liquidity_floor`.

7. **OPEX guard** — if today is within 5 calendar days of the third Friday, also call `mcp__uw-pp__oi_pin_risk` and `mcp__uw-pp__oi_opex_concentration` for SPY/QQQ/IWM and any name in the top of step 6. Pinning candidates feed the `opex-pin-strategist` scored book (§3 / §7) — **not** the §2 advisory, which is SPY/QQQ next-session GEX only.

8. **Macro & event-risk layer** — `risk_market_regime` gives a regime *label*, not a *calendar*. A swing book sized Tuesday with CPI Wednesday carries un-priced event risk. Build the macro layer once here (it respects the no-re-fetch hard rule — fetch once, pass down):
   - **Macro snapshot** — run `python3 scripts/fred_macro.py` via Bash. It returns a JSON `macro_snapshot` with latest prints + derived signals (yield-curve sign, core CPI/PCE YoY, unemployment, payrolls, 10Y level + 30d direction, USD direction, fed funds). If it returns `available:false` (no `FRED_API_KEY`), note the skip and continue — fall back to the regime label only.
   - **Forward catalyst calendar** — build `event_risk`: the Tier-1 US macro releases in the next ~10 trading days (CPI, PPI, PCE, FOMC/SEP, NFP/jobless claims) with their dates. Use `WebSearch` to confirm the scheduled dates (FRED has no forward-calendar endpoint). Tag each `{event, date, impact}`. Per-name earnings dates are added later in Phase 2 from the fundamentals enrichment — they are not known yet at Step 0.

9. **Next-session 0DTE setup (SPY/QQQ)** — run `python3 scripts/zerodte_setup.py --symbols SPY,QQQ --days 60 --json` via Bash and capture it as `zerodte_setup`. This is the **validated** 0DTE stack (the GEX-wall *pin* idea backtested NO_GO and is NOT used): it returns a rolling premium-selling `backtest` (front-IV implied move vs realized, open-entry vs overnight, GEX→range, VIX-level conditioning, `verdict`) plus a per-index `setup` (`sell_premium`, `vol_state`, `size_scalar`, `expected_range_pct`, `suggested_structure`, `entry_rule`, `stand_aside_reason`). It is **advisory, delta-neutral, 0 rubric points** — it sizes/structures a premium-selling 0DTE plan, not a directional bet, and is NOT a guaranteed edge (validation sample has no vol shock → tail unsampled). If it returns `available:false` (no duckdb / no parquet), note the skip and continue. Feeds §2 directly.

The output of Step 0 is a compact JSON-shaped context block: `{date, regime, vrp_classification, dte_share, sector_summary, sector_persistence, top_bullish, top_bearish, confluence, volume_outliers, iv_extremes, opex_pin_candidates, macro_snapshot, event_risk, zerodte_setup}`. Every Phase 1 agent receives this verbatim; `macro_snapshot` + `event_risk` are consumed primarily by `risk-monitor` in Phase 2, but agents may use them to gate directional calls against an imminent print.

---

## Step 1 — Phase 1: alpha-finding agents (parallel, single batch)

Spawn these **11 agents simultaneously** — a single message with 11 Agent tool calls (12 in OPEX week, see opex-pin-strategist below). Hand each one the Step 0 context block and the explicit MCP tool list below. The named tools are the minimum each agent must consult; agents can pull additional tools from their own descriptions if their finding is surprising.

**Hard rule:** no agent re-fetches `risk_market_regime`, `playbook_daily_synthesis`, `historical_vrp`, or `options_structure_front_end_iv_ratio` — those come from Step 0 context only. Re-fetching corrupts the shared anchor and burns tokens.

### gamma-flip-tracker — next-session 0DTE GEX map for SPY/QQQ ONLY
Scope is the **next session's 0DTE** dealer-gamma prior for **SPY and QQQ only** — read off the standing EOD 0–45d gamma book (OI persists overnight). This is the §2 **advisory** (prose-only, 0 rubric points, no backtested predictive claim). Do **not** cover IWM or single names in this read, and do **not** encroach on swing-horizon DEX/vanna/charm/GEX-trajectory work (owned by `dealer-positioning-strategist`).

Tools required:
- `mcp__uw-pp__options_structure_gex` — **PRIMARY**. Per-strike GEX (default `dte_max=45`), `zero_gamma_level`, `regime`, `total_gex`. The call wall = largest +GEX strike above spot; put wall = most −GEX strike below. Lead every SPY/QQQ read with this. (Do **not** lead with `today_gamma_flip` — it locks to the snapshot's already-expired same-day expiry and its ZGL is unreliable.)
- `mcp__uw-pp__historical_gex_time_series` — `regime_flip_dates` + multi-day ZGL trajectory to judge whether the regime is fresh (just flipped) or held.
- `mcp__uw-pp__options_flow_expiry_heatmap` — context: confirm near-dated expiries hold meaningful share.
- `mcp__uw-pp__options_flow_greek_screener` — `min_gamma` filter for the highest-impact near-dated contracts.

ZGL handling: trust `zero_gamma_level` only when it sits within ~5% of spot; when `null` or extrapolated, fall back to the `total_gex` sign + spot-vs-wall position and mark `zgl_reliable=false`. State the mandatory caveats from §2 (EOD = prior refreshed after the open; gap risk; ETF-not-index book; uw-pp cannot isolate the D+1 expiry).

Output: for **SPY and QQQ** — `{symbol, spot, zero_gamma_level, zgl_reliable, regime, total_gex, call_wall, put_wall, read, structure_bias, caveats}` (the §2 advisory + the `next_session_gex` envelope block).

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

Tools required (GICS layer — the shared anchor, cross-checks the ETF tape):
- `mcp__uw-pp__options_flow_sector_flow_persistence` — multi-day rotation persistence per sector (PRIMARY).
- `mcp__uw-pp__options_flow_sector_flow` — week-end skew within the persistence narrative (consume from Step 0 if available).
- `mcp__uw-pp__screener_bullish_bearish` — filter by sector to extract single-name leaders.
- `mcp__uw-pp__options_flow_dte_volume_share` — institutional vs retail share by sector (institutional rotation only counts at high monthly+ share).

ETF instrument-level flow tape (per-symbol — GICS tools cannot see ETFs, especially thematics/geographics). Run the **canonical ETF universe** constant in `sector-rotation-strategist.md`, **cap ≤ 40 added MCP calls**:
- **RANK (≤21):** `mcp__uw-pp__historical_cumulative_premium_flow` (`--symbol <ETF> --days 5`) for every universe ETF — rank by net-premium direction × multi-day persistence. Weight ETF **options** flow above ETF DP. Graceful-skip thin names.
- **DEEP-PULL top 3 inflow + 3 outflow only (≤12):** `mcp__uw-pp__dark_pool_largest` (`--symbol`, positioning/persistence tell — **not** single-name accumulation) + `mcp__uw-pp__options_flow_sweeps` (`--symbol`, directional urgency).
- **CROSS-CONFIRM:** GICS sector + its representative ETF agree w/ persistence → high-conviction; disagree → watch-only. No-GICS thematics → instrument-only (`gics_agreement: n/a`).

Output: rotation regime call (defensive→cyclical / cyclical→defensive / growth→value / value→growth / no_change), per-sector persistence scores, named single-name leaders within each rotating sector, `etf_flow_tape[]` (ranked inflow/outflow ETFs + GICS-agreement + leaders), and a one-line swing-book implication. The ETF tape is **advisory** — it strengthens the existing conditional sector-leader +1 via `gics_agreement`/cum_flow alignment, adds **no new rubric points**.

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

## Step 2 — Phase 2: quant → fundamentals gate → bull/bear debate → risk-monitor (sequential)

Phase 2 runs in four sequential stages. The quant produces the audited score (2a); the fundamentals gate cross-checks the top-5 against the underlying (2b); a bounded bull/bear debate stress-tests those same names (2c); then the risk officer gates and sizes against regime/VRP/correlation **plus** the fundamentals verdict and debate residuals (2d). Do not collapse them — the separation is the entire point of having auditable, disconfirmed conviction. Stages 2b and 2c operate on the **top 5 by `raw_score` only** (quota-trivial, and the only names that get sized at HIGH/MEDIUM).

### Step 2a — signal-confluence-quant (runs first)

Once **all** Phase 1 agents return, collect every candidate ticker into a single union list with each candidate's flagging agents and named signals. Spawn `signal-confluence-quant` with that union plus the conviction rubric (Step 4 below) as input. It must:

- Run `mcp__uw-pp__insights_signal_confluence` per ticker — confirm or contradict Phase 1 flags.
- Run `mcp__uw-pp__historical_signal_backtest` per ticker, per dominant signal class — pull historical win-rate (or `vol_realisation_rate` for non-directional signals).
- Pull `mcp__uw-pp__historical_cumulative_premium_flow` (30d and 90d) for tie-breaking and supplemental directional context.
- Compute `raw_score` per ticker against the Step 4 rubric, identify `dominant_signal_class`, attach `win_rate`, and emit `final_size_recommendation_pre_risk` (full / half / starter / skip) with a full audit trail per ticker.

Output: a sorted list of `{ticker, raw_score, score_components[], dominant_signal_class, confluence_score, cum_premium_flow_30d/90d, win_rate, win_rate_n, win_rate_source, final_size_recommendation_pre_risk, audit_trail}`. **The quant does not gate on regime/correlation** — that's risk's job in 2d.

### Step 2b — fundamentals-gate (top 5; runs after the quant)

The microstructure fleet is **fundamentally blind** — it cannot tell genuine accumulation from smart-money distribution into a deteriorating name. Spawn `fundamentals-gate` with the quant's **top 5 by `raw_score`**, each with its `dominant_signal_class` and inferred thesis direction, plus the Step 0 `as_of` date. For each name it runs `python3 scripts/finnhub_enrich.py --ticker <T> --date <as_of>` and cross-references earnings-surprise streak, insider MSPR, growth/leverage, and the news catalyst stack against the thesis direction.

Output: per-ticker `{ticker, fundamentals_verdict (CONFIRM/CAUTION/VETO/NA), tier_adjustment (0/−1/veto), earnings_trend, insider_signal, next_earnings_date, days_to_earnings, catalyst_support, reasons[], key_risks[]}`. Each name's `next_earnings_date` is fed into risk-monitor's event-risk gate. **NA never penalizes** (data unavailable ≠ evidence against). The verdict block hands to risk-monitor (2d).

### Step 2c — bull/bear debate (top 5; runs after the fundamentals gate)

Conviction scoring is **additive** — crowded consensus names score highest and break hardest, and no agent is tasked to kill the trade. Insert a bounded disconfirmation step. For each of the **top 5 by `raw_score`**, spawn `bull-researcher` and `bear-researcher` for **1 round** (escalate to a 2nd round only when the two residual confidences are within one bin of each other and ≥0.75 — i.e. a genuine disagreement worth a rebuttal). Hand both sides: the ticker's `score_components`, the Step 2b fundamentals enrichment, and the Step 0 macro/event context. Run the 5 names' debates in parallel; within a name, bull then bear is sequential.

Output: per-ticker `{ticker, bull_residual, bear_residual, bull_strongest_unrefuted, bear_strongest_unrefuted}`. The residual pair hands to risk-monitor (2d), which cuts size when the bear's residual ≥ the bull's (the debate did not clear the trade). The debate can only **cut** size, never add it.

### Step 2d — risk-monitor (runs last, consumes quant output + fundamentals verdict + debate residuals)

Spawn `risk-monitor` with (a) the quant's sorted score list, (b) the Step 2b fundamentals verdicts, (c) the Step 2c debate residuals, and (d) the Step 0 macro context (including `macro_snapshot` + `event_risk`). It must:

- Run `mcp__uw-pp__risk_portfolio_correlation` against today's candidates (not the static watchlist) — risk is measured against what we're actually considering.
- Confirm `mcp__uw-pp__risk_market_regime` from Step 0 (do not re-fetch).
- Apply the full sizing-gate stack from `risk-monitor.md`: VETO → watch-only (fundamentals); −1 tier each for regime conflict, `options_structure_front_end_iv_ratio > 1.10` panic, VRP-vs-trade-type contradiction, corr-cluster duplication, adverse sector rotation, `fundamentals_verdict == CAUTION`, a Tier-1 macro/earnings event inside the trade horizon (event-risk gate), and bear residual ≥ bull residual (debate gate). Emit an explicit `gate_verdicts` line per call — including the new `fundamentals`, `event_risk`, and `debate` verdicts — even when each no-op's.
- Pull `mcp__uw-pp__watchlist_alerts` and `mcp__uw-pp__watchlist_scan` against the rolling `conviction_<yesterday>` group — surface adverse-flow exit candidates.
- Persist today's top-5 conviction names (post-gate, **excluding any VETO'd name**) via `mcp__uw-pp__watchlist_manage(action="add", group="conviction_<date>")`.

Output: correlation clusters (corr > 0.7 = treat as one position), regime conflicts, VRP / panic gates applied, fundamentals verdicts, event-risk flags, debate-disconfirmation cuts, adverse-flow exit list, hedge sleeve recommendation, and a final sizing table per ticker that consumes the quant's `final_size_recommendation_pre_risk` and applies the gate stack.

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

The rubric below is what `signal-confluence-quant` consumes in Step 2a to produce the audited score. The quant attaches every signed point to a named source agent + tool in `score_components`. Risk-monitor in Step 2d applies the regime / VRP / cluster / fundamentals / event-risk / debate gates **on top of** this score.

```
Daily conviction score = Σ:
  +3  dealer-positioning-strategist flags DEX flip or vanna-squeeze setup in trade direction
  +3  3+ aligned signals in accumulation-hunter (DP + OI + oi_smart_positioning, dark_pool_block_stratified institutional-tier confirmed) — CONJUNCTION (2026-05-25 register C11): full +3 only when cum_premium_flow_30d confirms (sign aligned with thesis AND |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1. Reason: additive DP+accum+matrix manufactured false HIGH conviction (tier inversion HIGH 60.0% < MED 62.5%, n=49); the ≥0.80 WR is a conjunction (DP-block ∧ cum_flow ∧ institutional-accum). Distinct from flow_conflict/−lite (those subtract on opposing/MIXED flow; this reduces the +3 accumulation award to +1 on non-confirming flow — both may fire). A sub-$50M flow that halves this line does not separately qualify as "net directional accretion" for the +3 cum_flow line. See signal-confluence-quant.md "Conditional dark_pool_accumulation conjunction".   # was +2; promoted 2026-05-15 audit P1.2 — Phase 4 +27.8pp marginal contribution (LOAD-BEARING)
  +1  multi-day OI build (historical_oi_trend BUILDING, lookback ≥ 5 days)                       # was +2; reduced 2026-05-09 (Phase 4 +5pp marginal — supportive, not load-bearing; correlated with the LOAD-BEARING components above)
  +1  insights_conviction_matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL ONLY (2026-05-23 audit P1.1): award +1 only when dominant_signal_class == leap_directional; in all non-LEAP contexts contribution is 0. Phase 4: marginal contribution −23pp (n=8) on swing horizon; the DIRECTIONAL_LONG/>70 signature appears to be a mean-reversion-fade (top-pick) signature outside LEAP. LEAP gate in leap-positioning-radar still consumes this tool — only the swing-rubric award is gated to leap_directional.
  +3  historical_cumulative_premium_flow shows net directional accretion in trade direction (30d window)   # was +2; promoted 2026-05-15 audit P1.2 — Phase 4 +24.2pp marginal contribution (LOAD-BEARING)
  +2  insights_signal_confluence ≥4 (second-agent confirmation)   # NEW 2026-05-23 audit P1.2 — Phase 4 +19.5pp marginal contribution (n=12, LOAD-BEARING); also added to the 3-of-5 LB gate in Step 3a
  # +1 line for hot_chains_sweep_persistence top-5 REMOVED 2026-05-23 audit P0.3
  # Reason: marginal contribution −22pp two consecutive audits (n=15); mega-cap suppression rule from 2026-05-15 P1.1 was insufficient.
  # Tool remains informational — sweep-tracker still surfaces persistence-ranked sweeps in §3/§7 prose — but contributes 0 points to raw_score.
  # If the call merits a multileg or accumulation co-flag, those tools earn the score instead.
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector — CONDITIONAL (2026-05-23 audit P1.5): award +1 only when (a) sector persistence_score ≥ 0.6 (the tool's 0–1 sign-consistency scale = ≥3-of-5-days; 2026-05-25 fix — was an unsatisfiable `≥3`) AND (b) cum_premium_flow_30d direction aligned with thesis direction AND (c) |cum_flow_30d| ≥ $50M. Default 0. Phase 4: sector_persistence marginal +2.8pp standalone (NO-INFO); when paired with cum_flow alignment, it was the difference between HON-W21 (+4.9% WIN) and WMT-W19 (−10.4% LOSS, flow disagreed).
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)   # was +1; promoted 2026-05-09 (Phase 4 +8pp marginal; multileg-vs-batch_strategy disagreements correctly resolved 5/5 in dataset)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising historical_pc_ratio_zscore (VRP positive)
  -3  flow_conflict — signal-confluence-quant applies mechanically when historical_cumulative_premium_flow 30d direction is *clearly opposite* dominant_signal_class (signed-sum sign flip + magnitude > today's union-median |cum_flow_30d|, or explicit OPPOSITE label)   # 2026-05-15 audit P0 — see signal-confluence-quant.md "Mechanical flow_conflict deduction" rule; 2026-05-23 audit P1.3: mutually exclusive with flow_conflict_lite (apply ONE, never both)
  -1  flow_conflict_lite — signal-confluence-quant applies when the 30d cum_premium_flow read is MIXED (signed sum near zero, or aligned but bottom-quartile magnitude in today's union)   # 2026-05-15 audit P0; 2026-05-23 audit P1.3: mutually exclusive with flow_conflict (apply ONE, never both)
  # 2026-05-09 -2 generic flow_conflict line replaced with the mechanical -3 / -1 split above (Phase 3 2026-05-15 audit: 30% missed-gate rate at the generic line; NVDA 2026-05-08 raw=10 LOSS dominated by un-penalised flow_conflict against −$17.89M cum_flow_30d)
  -1  risk-monitor flags in correlation cluster (corr > 0.7) — applied in 2d on top of raw score
  -3  risk_market_regime conflicts with trade direction — applied in 2d

# Removed from swing/LEAP scoring 2026-05-09 (Phase 4 audit, NO-INFO ±0pp on swing horizon):
#   gamma-flip-tracker 0DTE breakout setup (regime flip + flow alignment) — formerly +2.
#   The signal drives §2 (Next-Session GEX Map — SPY/QQQ advisory) directly, but does NOT earn rubric
#   points on any row. §2 is advisory / prose-only and contributes 0 points to raw_score by design
#   (the next_session_gex envelope block is kept OUT of calls[] so it cannot enter the rubric). This
#   component also double-counted with dealer-positioning's +3 DEX flip.
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

**On top of this ladder (2026-05-25 register C2), the quant applies two downgrade-only guards** (see `signal-confluence-quant.md` "Market-excess gate" + the N-conditional cap): (1) the `n < 10` cap is **0.69** (below the 0.70 full line — a small-N up-week class sizes at most half), and (2) a **market-excess gate** — if a class does not beat the same-direction SPY bet over the same windows (`excess ≤ 0`), cap at half; `excess ≤ −0.10` → starter. Beta in an up-tape is not edge. The win-rate denominator is computed only over liquidity-floor-passing names (C12). Reusable: `scripts/excess_winrate.py:size_decision`. **(3, register C4)** a `bullish_flow`/`bearish_flow` class also caps at half when the flow is **not OI-confirmed-opening** (Pan-Poteshman: only opening flow predicts) — `historical_oi_trend` BUILDING or ΔOI ≥ 20% of day volume; flat/falling OI vs high volume = churn → cap half. Reusable: `scripts/oi_opening.py:opening_gate_size`. All three guards are downgrade-only and may stack.

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
- **Next-session GEX (SPY/QQQ):** <per index: regime (long/short-gamma) · ZGL · call wall / put wall · one-line structure bias> — advisory, see §2
- **Top swing build:** <ticker, thesis, structure, invalidation, win_rate, size>
- **Top LEAP candidate:** <ticker, scenario, structure, invalidation, win_rate, size>
- **Biggest risk:** <correlation cluster name, members, hedge sleeve>

## 1. Regime & Gamma State
- `risk_market_regime` reading + breadth narrative
- Per-index gamma table: spot | zero-gamma | total GEX | regime | call wall | put wall (rows: SPY/QQQ/IWM). This is the **current-state** EOD book; §2 carries the forward, next-session **advisory** read of these same levels for SPY/QQQ with concrete 0DTE structure guidance.
- `options_flow_dte_volume_share` summary (institutional vs retail share)
- `historical_vrp` classification
- **Macro backdrop** (`scripts/fred_macro.py` `macro_snapshot`): yield-curve sign, core CPI/PCE YoY, unemployment + payrolls, 10Y level/direction, USD direction — one line. Plus the forward `event_risk` calendar: Tier-1 prints in the next ~10 trading days.

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — built from open interest that **persists overnight** — read forward as the *prior* for next session's open. It is **prose-only, contributes 0 points** to the conviction rubric (Step 4), and makes **no backtested predictive claim**. The predictive validation of these levels lives in `/weekly-analysis`'s rolling §2 backtest (`scripts/gex_next_session_backtest.py`), not here. Scope is **SPY and QQQ only** — no IWM, no single names.

Lead with `gamma-flip-tracker`'s next-session read for **SPY and QQQ** (primary tool `options_structure_gex`, default `dte_max=45` — **not** `today_gamma_flip`, which locks to the snapshot's already-expired same-day expiry and returns an unreliable ZGL):

| Field | Source | How to read it |
|---|---|---|
| spot · zero-gamma (ZGL) · regime | `options_structure_gex` | **long-gamma** (spot ≥ ZGL, `total_gex` > 0) → mean-revert / pin / vol suppression; **short-gamma** (spot < ZGL, `total_gex` < 0) → trend / breakout / vol expansion. Distance spot-to-ZGL scales conviction; sitting on the flip = NEAR_FLIP, do not fade. |
| call wall · put wall | `options_structure_gex` `per_strike` | call wall = largest +GEX strike above spot (cap / upside magnet); put wall = most −GEX strike below (support). Distance-to-wall sets the realistic next-session range and whether the 0DTE straddle is rich (walls tight) or cheap (walls wide). |
| regime freshness | `historical_gex_time_series` `regime_flip_dates` | flag whether the regime just flipped (fresh, unstable) vs held for several sessions. |

Per index, state **regime + ZGL + call wall + put wall + a one-line structure bias for the next session's 0DTE**:
- **Long-gamma, walls tight to spot:** straddle rich → iron fly / short straddle / butterfly centred on the pin (ZGL or dominant wall).
- **Long-gamma, walls wide:** iron condor with shorts just inside each wall; fade pokes beyond the call wall (strike selection just beyond the wall so the wall does the work).
- **Short-gamma:** straddle cheap → debit verticals / directional 0DTE in the trend direction; long straddle if spot sits on the flip with walls wide.

**Mandatory caveats — state them, do not bury them:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 min and re-computes the ZGL/walls; the map orients the open, it is not a static level to trade blindly.
- **ZGL reliability.** Trust the ZGL only when it sits near spot (within ~5%); it is `null` on FULLY_NEGATIVE days and occasionally returns an extrapolated deep-OTM value. When unreliable, fall back to the `total_gex` sign + spot-vs-wall position and mark `zgl_reliable=false`.
- **Gap risk voids the prior.** Overnight macro (Asia/Europe), earnings, and Tier-1 prints can gap spot through the walls before any hedging mechanic engages — cross-check the Step 0 `event_risk` calendar.
- **Tooling limit.** uw-pp cannot isolate the D+1 expiry (`gex --dte-max 1` errors). This is the standing **0–45 DTE** book — the best available proxy for the next-session prior, not the isolated next-session expiry.
- **ETF book.** This is the SPY/QQQ ETF gamma book, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup (from `scripts/zerodte_setup.py` — the validated stack)
The GEX **walls above are a map (advisory "where"), not a pin** — wall-as-magnet backtested NO_GO, as did every directional signal (charm, vanna, intraday momentum). What *did* validate is a **delta-neutral premium-selling** edge. Surface the `zerodte_setup` block from Step 0 for **SPY and QQQ** (still advisory, **0 rubric points**, NOT a guaranteed edge — the validation sample has no vol shock, so the short-vol tail is unsampled):

- **Whether (VRP):** the front-expiry implied move systematically exceeds the realized next-day open-to-close move. Report `sell_premium` + the rolling `backtest.verdict` / win-rate so the read carries its own track record.
- **How much (GEX vol-suppression, Barbon-Buraschi):** long-gamma → quieter next-day range → tighter wings; short-gamma → wider range → wings out or stand aside. Use `expected_range_pct` for wing width.
- **Size (VIX level):** scale by `size_scalar` / `vol_state` — bigger when VIX rich, skip when VIX low (thin edge).
- **When:** `entry_rule` — **enter at/after the open once the gap resolves; hold the 0DTE to the close; never carry overnight** (overnight entry backtested negative — the gap erases the edge). If it gaps beyond the wings, stand aside.
- **Stand aside** when `stand_aside_reason`/`caution` is set (VIX spiking or front-end backwardation — the regime where short-vol blows up).
- **Direction:** none — this is delta-neutral. Do not add a directional tilt.

Per index, surface `{sell_premium, vol_state, size_scalar, expected_range_pct, suggested_structure, entry_rule, stand_aside_reason}`. **SPY ≈ SPX** (validated identical — trade either); **QQQ is weaker** (Nasdaq index book unavailable) — flag its lower confidence.

Near-term directional **sweeps** are surfaced in §3 (swing setups), not here. **OPEX-week pin mechanics** (when `opex-pin-strategist` is spawned) flow through the conviction rubric into §3 / §7 like any other scored name — they are not part of this advisory.

## 2a. Swing Dealer Positioning (1–4 weeks)
- `dealer-positioning-strategist` outputs: DEX flips, vanna-squeeze flags, ZGL trajectory regime flips
- Names with `swing_bias=LONG/SHORT` get carried into §3 with the dealer-positioning tag

## 2b. Sector Rotation
- `sector-rotation-strategist`: rotating-into / rotating-out-of sectors with persistence scores
- Rotation regime call (defensive→cyclical / cyclical→defensive / growth→value / value→growth / no_change)
- Single-name leaders feed §3 with the `sector_rotation` tag

**ETF flow tape (advisory)** — instrument-level layer the GICS aggregates can't see. Surface `etf_flow_tape[]` as a ranked table:

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|

Lead with top-3 inflow / top-3 outflow ETFs. Call out **GICS-vs-ETF agreement** explicitly (agree → high-conviction rotation; disagree → watch-only; `n/a` → instrument-only thematic/geographic read). Frame as advisory: ETF DP is a positioning/persistence tell (creation/redemption & hedging), **not** single-name accumulation; ETF options flow is weighted above ETF DP. The tape **strengthens** the existing conditional sector-leader +1 (via `gics_agreement` + cum_flow alignment) — it adds **no rubric points**.

## 3. Swing Setups (1–6 weeks)
Ranked by conviction score. Table: Ticker | Score | Thesis | Structure | Invalidation | Sizing.
Subdivide into:
- **3a. Long swings (regime-aligned)** — accumulation + multileg directional + earnings BUY VOL + dealer-positioning vanna-squeeze + sector-rotation leaders.
- **3b. Short / fade swings (defined risk only)** — contrarian + earnings SELL VOL + analyst-vs-flow disagreement + dealer-positioning DEX-flip-short.

Surface the urgency-ranked, persistence-first near-term **sweeps** from `sweep-tracker` here as well (relocated from §2; informational — 0 rubric points unless the name also earns a scored co-flag).

## 4. LEAP Builds (6–24 months)
leap-positioning-radar — DIRECTIONAL_LONG only with full disqualification notes for near-misses.

## 5. Volatility Surface
vol-surface-scout — KINKED names, BACKWARDATION calendars, IV outliers, calendar-spread candidates with implied move per name.

## 6. Risk & Correlation
risk-monitor consuming today's Phase 1 candidate union and the quant's audited score (not the static watchlist) — clusters, regime conflicts, VRP / panic gates applied, **fundamentals verdicts** (CONFIRM/CAUTION/VETO per top-5 name with the contradicting facts), **event-risk flags** (Tier-1 macro / earnings inside a trade's horizon), **debate-disconfirmation cuts**, hedge sleeve recommendations. Lead with the `macro_snapshot` headline + forward `event_risk` calendar.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
Per-ticker breakdown sourced from the `signal-confluence-quant` audit trail: `raw_score` | `score_components[]` (with named source agent + tool per component) | `dominant_signal_class` | `win_rate` (with `n` + source) | pre-risk size | `fundamentals_verdict` | bull/bear residuals | risk-monitor gates applied (`gate_verdicts`) | final size | invalidation level. Note any VETO'd name here with the distribution evidence even though it drops to watch-only.

Embed the conviction-scoring rubric (Step 4) verbatim at the bottom of §7 so future readers can audit the scores.

## 8. Watch-only — single signal, no confluence
Candidates that surfaced from one agent but failed the confluence gate. Listed for journaling, NOT for trade entry today.
```

---

## Step 8 — Confirm watchlist write-back (handled by risk-monitor in Step 2d)

The top-5 watchlist write-back is performed inside `risk-monitor` during Step 2d — the agent calls `mcp__uw-pp__watchlist_manage(action="add", group="conviction_<YYYY-MM-DD>")` with today's top 5 by conviction score (excluding any VETO'd name). **Do not double-write here.**

Confirm the write-back happened by checking the `risk-monitor` output for the explicit `watchlist_write_back_confirmation` field. If missing, call `mcp__uw-pp__watchlist_manage(action="add", group="conviction_<YYYY-MM-DD>", tickers=[<top_5_by_score>])` directly as a fallback.

If any name was already on a manually-curated group, leave that membership alone — write only to the date-stamped group. This closes the feedback loop: today's high-conviction names become tomorrow's correlation universe, and tomorrow's RM automatically pulls `watchlist_alerts` against them to flag adverse-flow exit candidates.

---

## Step 8.5 — Deep-dive hand-off on the top conviction names (optional)

The fleet is breadth-first and stops at one report row per name. For the **top 2 HIGH-tier names** (post-gate, non-VETO), hand off to the single-name deep-dive engine, which shares this repo's Phase-1 agents so integration is near-zero:

- If the `stock-deep-dive` skill is available in the session, invoke `/stock-deep-dive <TICKER>` for each (sequentially, to avoid spawning two long fleets at once). Record the produced report path under a `## Deep-dive hand-off` note in §7.
- If the skill is **not** available, do not block — emit the recommendation verbatim in §7 (`Recommended deep dive: /stock-deep-dive NVDA`) so the user can run it.

Skip this step entirely on a "no edge" day (no HIGH-tier names). Keep it to the top 2 — deep dives are expensive and the marginal value drops fast past the top of the book.

---

## Step 9 — Save, emit decision envelope, and report

0. **Create the run folder** — `mkdir -p analyses/daily/YYYY-MM-DD` via Bash. Both output files live inside it; the date lives in the folder name, so the files are generically named (`report.md`, `decision.json`).
1. Use Write to save the report to `analyses/daily/YYYY-MM-DD/report.md`.
2. **Emit the structured decision envelope** beside the report at `analyses/daily/YYYY-MM-DD/decision.json`, conforming to `schemas/decision_envelope.schema.json`. This is the machine-resolvable sidecar `/calibration-audit` Phase 1 reads instead of re-parsing prose. Build it from the data already produced — do not re-derive:
   - Top level: `{schema_version: "1.1", report_date, report_kind: "daily", regime, vrp_classification, macro_snapshot_signals (the fred_macro signals object), macro_event_risk (the event_risk calendar), watchlist_write_back (the persisted top-5), next_session_gex, next_session_0dte_setup, report_path}`.
   - `next_session_gex` (schema_version 1.1): the **advisory** §2 GEX-map block — `{advisory: true, as_of_eod_date: <report_date>, next_session_date, indices: [{symbol, spot, zero_gamma_level, zgl_reliable, regime, total_gex, call_wall, put_wall, read, structure_bias, caveats}]}` for **SPY and QQQ only**.
   - `next_session_0dte_setup` (schema_version 1.1): the **advisory** §2a premium-selling block, copied from Step 0 `zerodte_setup` — `{advisory: true, as_of_eod_date: <report_date>, backtest_verdict, indices: [{symbol, sell_premium, vol_state, vix, implied_move_pct, expected_range_pct, size_scalar, suggested_structure, entry_rule, stand_aside_reason, caution}]}` for **SPY and QQQ only**. Emit `null` if `zerodte_setup.available == false`.
   - **Both** advisory blocks are deliberately top-level fields, **not** members of `calls[]` — §2/§2a are prose-only and must contribute 0 points to any `raw_score`. **Do not** add a `horizon: "0DTE"` entry to `calls[]` for this content.
   - `calls[]`: one object per HIGH/MEDIUM/LOW call (and watch-only / VETO'd names) carrying the quant's audit fields verbatim — `ticker, horizon, section, direction, tier, raw_score, score_components[], dominant_signal_class, confluence_score, cum_premium_flow_30d/90d, win_rate, win_rate_n, win_rate_source, pre_risk_size, final_size, gate_verdicts, fundamentals_verdict, debate_residual_confidence (the bull residual), structure, entry_or_trigger, invalidation, key_risks[], thesis`.
   - **Invariant:** `Σ score_components[].points == raw_score` for every call (the quant already guarantees this — the validator enforces it).
3. **Validate it:** run `python3 scripts/validate_decision.py --file analyses/daily/YYYY-MM-DD/decision.json` via Bash. If it exits non-zero, fix the envelope (not the validator) until it passes — a malformed envelope silently degrades the calibration loop. Set the envelope's `report_path` to `analyses/daily/YYYY-MM-DD/report.md`.
4. Confirm both files were written (the Write tool errors loudly on failure — no need to re-Read).
5. Print the **Executive Summary** section to chat. Nothing else — the user opens the file for the rest.

---

## Failure modes & recovery

- **Phase 1 agent times out** — re-spawn just that agent with the same context block. If it fails twice, write its section as `[agent timed out — see <agent-name> logs]` and proceed; do not let one agent block the report.
- **`playbook_daily_synthesis` returns empty** — fall back to manually composing the macro context from `risk_market_regime` + `insights_signal_confluence` + `watchlist_alerts` and continue.
- **`historical_available_dates` shows stale data** — abort and ask the user to re-export from Unusual Whales. Do not proceed with stale data.
- **No tickers clear the confluence gate** — produce a report whose §3 and §4 are explicitly empty, with the §1 regime + §2 next-session GEX advisory still populated. A "no edge" day is a valid output, not a failure.
