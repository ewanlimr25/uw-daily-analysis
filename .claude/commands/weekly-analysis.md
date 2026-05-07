---
description: Run the full Friday-evening or Sunday-prep weekly intelligence note in the voice of a top-tier institutional desk strategist (JPM/GS Friday note). Persistence-weighted conviction rubric over a 5-day window with WoW regime delta, intra-week thesis scorecard (WIN/LOSS/INCONCLUSIVE per ticker), sector rotation persistence, vol-surface evolution, LEAP roll detection, OPEX-week pin map, and 2-week earnings lookahead. Output is tiered High/Medium/Low conviction with backtest-weighted sizing. Invoke whenever the user asks for a weekly recap, week-ahead prep, Sunday strategy session, weekly market intelligence note, or types `/weekly-analysis`. Do NOT trigger for single-day reports (use `/daily-analysis`), single-ticker analyses (use `mcp__uw-insights__stock_deep_dive`), or month/quarter horizons.
---

# Weekly Market Intelligence

Run a full weekly intelligence note in the voice of a top-tier institutional desk strategist. Uses the same two-phase agent fleet as `/daily-analysis` but wired to week-range inputs and a persistence-weighted conviction rubric. **All data is pulled fresh from MCP tools — no dependency on prior daily analysis files.** Phase 1 spawns 8 agents in parallel against a shared week-baseline context. Phase 2 runs `risk-monitor` against the union of the week's candidates. Score conviction formally with explicit tiers, backtest top names, write winners back to the watchlist, and save the report to `analyses/weekly/YYYY-WW.md`.

## When to invoke

- "Weekly recap", "week in review", "weekly intelligence note"
- "Sunday prep", "week-ahead prep", "what should I watch next week"
- Friday-evening review of the trading week
- Slash command `/weekly-analysis`

## When NOT to invoke

- "Wrap up today" / "EOD report" → `/daily-analysis`.
- "What's NVDA doing this week?" → `mcp__uw-insights__stock_deep_dive` + `mcp__uw-historical__trend_analyzer` for that one ticker.
- Month-over-month or quarterly horizons — call `mcp__uw-historical__cumulative_premium_flow` with `lookback_days=30` (or 90) and let the user drive the synthesis manually.

## Model routing

The orchestrator running this skill must use **`opus` with extended thinking on**. It performs the cross-agent synthesis, conviction rubric application, and report writing — tasks that degrade materially on a smaller model. Sub-agents are cheaper and have narrower mandates; assign models as follows when spawning each agent:

| Agent | Model | Thinking | Why |
|---|---|---|---|
| gamma-flip-tracker | sonnet | off | Mechanical: fetch GEX trajectory, output zero-gamma + pin strikes |
| sweep-tracker | sonnet | off | Filter and rank by persistence count — no synthesis |
| accumulation-hunter | sonnet | off | Pattern match across dark pool + OI over 5d/10d |
| contrarian-scanner | sonnet | off | Trajectory computation — rising vs falling pc_ratio_zscore |
| earnings-scout | sonnet | **on** | Dual mandate: judgment-heavy recap grading + multi-signal lookahead ranking |
| vol-surface-scout | sonnet | off | Analytical WoW delta — systematic flagging, no ambiguity |
| multileg-strategist | sonnet | **on** | Hardest Phase 1 task: inferring institutional intent from repeated cross-week structures |
| leap-positioning-radar | sonnet | **on** | Multi-signal synthesis over 10d+ window + rolling detector requires reasoning depth |
| risk-monitor (Phase 2) | sonnet | off | Systematic: correlation matrix + cluster flagging |

Pass the model assignment in each agent's prompt header (e.g. `Model: claude-sonnet-4-6, extended_thinking: false`).

## Operating principle: persistence beats a single print

Single-day signals are noise; multi-week persistence is the edge. Every agent in this run must consume week-range data wherever the MCP supports it. Specifically:

- `mcp__uw-hotchains__multi_day_sweep_persistence` over `mcp__uw-options-flow__sweep_detector`
- `mcp__uw-historical__oi_trend` with `lookback_days=5` over `mcp__uw-oi__biggest_oi_increases`
- `mcp__uw-historical__cumulative_premium_flow` over single-day premium totals
- `mcp__uw-historical__pc_ratio_zscore` over the deprecated `put_call_ratio_extremes`
- `mcp__uw-historical__iv_percentile_zscore` over raw IV rank for outlier robustness
- `mcp__uw-historical__gex_time_series` over single-day GEX snapshots
- `mcp__uw-options-flow__sector_flow_persistence` over single-day `sector_flow_summary`
- `mcp__uw-historical__signal_backtest` before sizing any trade

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

2. **Coverage list** — call `mcp__uw-historical__available_dates` and filter to dates in `[MONDAY, WEEK_END]`. Call this filtered list `covered_dates`. **Rules:**
   - If `covered_dates` is empty → abort and report "No UW data available for the current trading week."
   - If any calendar weekday Mon–Fri is missing from `covered_dates`, note the gap explicitly — agents must not assume a full 5-day window. Pass `covered_dates` (not the computed calendar range) as the authoritative list to every Phase 1 agent.

3. **Regime baseline** — call `mcp__uw-risk__market_regime` twice: once for `TODAY` and once for `covered_dates[0]`. Compute the WoW regime delta. This **week regime baseline** — regime today vs week-open, and whether it improved / deteriorated / held — is passed to every Phase 1 agent. Agents must gate their directional calls against it.

4. **Vol regime** — call `mcp__uw-historical__volatility_risk_premium` for the most recent date in `covered_dates`. Classify the week as a premium-selling environment (VRP positive) or premium-buying environment (VRP negative). This shapes which agents you trust most: VRP-positive weeks favour vol-surface-scout & contrarian-scanner; VRP-negative weeks favour gamma-flip-tracker & earnings-scout.

5. **Sector & flow-share baseline** — call in parallel:
   - `mcp__uw-options-flow__sector_flow_persistence` over the full week range. This is the durability check that gates §2 of the report (sector rotation narrative).
   - `mcp__uw-options-flow__sector_flow_summary` for `WEEK_END` — single-day snapshot for week-end skew within the persistence narrative.
   - `mcp__uw-options-flow__dte_volume_share` for each covered date (or `WEEK_END` only if a faster pass is needed) — institutional vs retail share trend across the week. Feeds §1.

6. **Top-of-funnel screens** — run in parallel for `WEEK_END`:
   - `mcp__uw-screener__bullish_bearish_screener` (top 25 each side) — week-end leaderboard.
   - `mcp__uw-insights__signal_confluence` (`min_score=4`, top 25 each direction) — multi-factor scoring at higher threshold than daily.
   - `mcp__uw-screener__iv_rank_screener` (top 25 high, top 25 low) — premium-selling vs premium-buying candidates for next week.
   - `mcp__uw-screener__earnings_catalyst_scanner` — upcoming earnings + elevated IV (next 14 days) — feeds §6.
   - `mcp__uw-screener__volume_vs_average` (top 25, `min_ratio=3`) — flow anomalies vs 30-day baseline; cross-reference against multi-day persistence for §3.
   - `mcp__uw-hotchains__sweep_ratio_scanner` — high sweep-to-volume contracts at week-end; cross-reference against `multi_day_sweep_persistence` in sweep-tracker.

7. **OPEX guard** — if `WEEK_END` is within 7 calendar days of the third Friday, also call `mcp__uw-oi__pin_risk_screener` for SPY/QQQ/IWM and the top 10 from step 6, plus `mcp__uw-oi__opex_concentration` for the same set. Pinning candidates feed §9 (Setups for Next Week).

8. **Compose the week-baseline context block** — this compact JSON-shaped block is passed verbatim to every Phase 1 agent: `{iso_week, monday, week_end, today, covered_dates, regime_today, regime_monday, regime_delta, vrp_classification, sector_persistence, top_bullish, top_bearish, confluence, iv_extremes, earnings_lookahead, opex_pin_candidates}`.

---

## Step 1 — Phase 1: alpha-finding agents (parallel, single batch)

Spawn these 8 agents **simultaneously** — a single message with 8 Agent tool calls. Hand each one: (a) the week-baseline context block from Step 0, (b) the count of covered days (so agents know whether they have a full 5-day window or a shorter one), and (c) the explicit tool list below. Each agent must restrict queries to `covered_dates` and favour multi-day tools over single-day equivalents.

### gamma-flip-tracker — DEMOTED, forward-looking only (sonnet, thinking off)
Do **NOT** produce intraday or 0DTE calls. Instead: forecast next week's zero-gamma level and key pin strikes for SPY/QQQ/IWM and any liquid name with significant LEAP-grade GEX from Step 0.

Tools required:
- `mcp__uw-options-structure__today_gamma_flip` — current day zero-gamma + flip strike (latest).
- `mcp__uw-options-structure__gamma_exposure_profile` (default `dte_max=45`) — per-strike GEX, call wall, put wall.
- `mcp__uw-historical__gex_time_series` (`lookback_days=10`) — multi-day ZGL trajectory; flag any regime flip across the week.
- `mcp__uw-options-structure__dealer_delta_exposure` — DEX trajectory (week-over-week directional pressure).
- `mcp__uw-options-structure__vanna_charm_exposure` — vanna-squeeze setup detection (put-heavy book + falling VIX → BUY setup).

Output: §9 next-week GEX outlook — pin vs trend regime, key strikes, DEX/vanna squeeze flags.

### sweep-tracker — multi-day persistence (sonnet, thinking off)
Use `mcp__uw-hotchains__multi_day_sweep_persistence` as the **primary** signal. Surface tickers swept on **≥3 of 5** trading days this week.

Tools required:
- `mcp__uw-hotchains__multi_day_sweep_persistence` (primary).
- `mcp__uw-hotchains__smart_money_flow` — ask vs bid colour for each persistence-flagged ticker.
- `mcp__uw-options-flow__sweep_detector` — supplementary (week-end snapshot only).
- `mcp__uw-options-flow__top_premium_trades` (top 30, week range) — whale-ticket validation.
- `mcp__uw-hotchains__most_active_contracts` — per-ticker contract-level conviction.

Single-day sweeps alone are insufficient for a weekly recommendation. Rank candidates by persistence count first.

### accumulation-hunter — expanded window (sonnet, thinking off)
Run with `lookback_days=5` (and `lookback_days=10` as a secondary pass).

Tools required:
- `mcp__uw-insights__institutional_accumulation_detector` (`lookback_days=5` and `lookback_days=10`).
- `mcp__uw-darkpool__dark_pool_ticker_summary` (top 30 by premium across each covered date — aggregated).
- `mcp__uw-darkpool__largest_dark_pool_trades` (top 30 across the full week range).
- `mcp__uw-darkpool__dp_block_size_stratified` — institutional vs retail tier filtering.
- `mcp__uw-darkpool__dark_pool_price_levels` — institutional support/resistance built up across the week.
- `mcp__uw-darkpool__extended_hours_filter` — overnight/pre-market block activity.
- `mcp__uw-oi__smart_positioning` — OI bullish/bearish inference.
- `mcp__uw-historical__oi_trend` (`lookback_days=5`) — multi-day OI build verification (BUILDING required for full points).

Output: tickers with quiet multi-day OI build sustained across the full week with both DP and OI confirmation.

### contrarian-scanner — pc_ratio trajectory (sonnet, thinking off)
Tools required:
- `mcp__uw-historical__pc_ratio_zscore` — compute the trajectory of pc_ratio_zscore across `covered_dates`. This is the primary signal. **Do NOT use the deprecated `put_call_ratio_extremes`.**
- `mcp__uw-insights__price_vs_flow_divergence` (week-range) — when smart money disagrees with price.
- `mcp__uw-options-flow__iv_outliers` (week aggregated) — high-IV contracts where flow may be exhausted.
- `mcp__uw-oi__oi_decrease_with_volume` — capitulation / profit-taking detection.
- `mcp__uw-screener__iv_rank_screener` (extreme high) — premium ripe to fade.

Flag names where crowdedness is **rising** (deteriorating contrarian setup) vs **falling** (crowding unwinding — potential fade entry). Gate every fade call against the week-regime baseline.

### earnings-scout — DUAL MANDATE: recap + lookahead (sonnet, thinking **on**)
Two sub-tasks:

**(a) Recap.** For each earnings event that printed this week (extract from `covered_dates` flow data), evaluate flow reaction vs pre-event thesis:
- `mcp__uw-insights__earnings_play_analyzer` — pre-event positioning & post-event flow.
- Grade each play as confirming or disconfirming (BUY VOL → IV crush realised? SELL VOL → directional move trapped? etc.).

**(b) Lookahead.** Scan the next two calendar weeks for earnings catalysts:
- `mcp__uw-screener__earnings_catalyst_scanner` (next 14 days).
- `mcp__uw-options-structure__iv_term_structure` per candidate — KINKED/BACKWARDATION alignment.
- `mcp__uw-options-structure__term_skew` — back-month skew at the earnings DTE.
- `mcp__uw-options-structure__front_end_iv_ratio` — quick panic detector.
- `mcp__uw-insights__analyst_vs_flow` — analyst-vs-flow disagreement is the highest-EV setup.

Output: §6 earnings recap + ranked 2-week lookahead with IV term-structure alignment + analyst disagreement scores.

### vol-surface-scout — WoW term-structure & skew evolution (sonnet, thinking off)
Tools required:
- `mcp__uw-options-structure__iv_term_structure` for `WEEK_END` and `covered_dates[0]` — compute the WoW shape change.
- `mcp__uw-options-structure__term_skew` for `WEEK_END` and `covered_dates[0]` — WoW skew change.
- `mcp__uw-options-structure__front_end_iv_ratio` (current) — single-number panic check.
- `mcp__uw-historical__iv_percentile_zscore` (`lookback_days=252`) — outlier-robust per-ticker IV percentile (Goyal-Saretto). Use this instead of raw IV rank where possible.
- `mcp__uw-options-flow__iv_outliers` (week aggregated) — single-contract outliers.
- `mcp__uw-options-flow__expiry_heatmap` — week-level concentration; calendar-spread candidate identification.

Flag names that went from NORMAL to KINKED or into BACKWARDATION across the week. These are §5.

### multileg-strategist — full-week sample (sonnet, thinking **on**)
Tools required:
- `mcp__uw-hotchains__multileg_activity` across the **full week** (not just today). Structures repeated on **≥2 days** carry materially higher directional inference weight than single-day prints.
- `mcp__uw-options-flow__top_premium_trades` filtered to ≥$1M premium (week range).
- `mcp__uw-options-flow__greek_screener` — directional / vol / vega bets by Greek profile.
- `mcp__uw-options-flow__expiry_heatmap` — concentration by expiry to spot calendar/diagonal builds.
- `mcp__uw-hotchains__most_active_contracts` — per-ticker context.

Output: per-ticker structure read with directional thesis, repeated-on-N-days count, and built-in risk caps.

### leap-positioning-radar — rolling detector + 10d window (sonnet, thinking **on**)
Tools required:
- `mcp__uw-oi__position_rolling_detector` across each covered date — surface conviction shifts (rolls forward into 2027/2028 LEAPs, rolls up in strike, large new LEAP OI initiations).
- `mcp__uw-oi__biggest_oi_increases` (`min_dte=180`) — fresh LEAP positions only.
- `mcp__uw-historical__oi_trend` (`lookback_days=10`) — BUILDING required for full points.
- `mcp__uw-historical__cumulative_premium_flow` (`lookback_days=30` or default 90) — LEAP-grade slow-accretion signature.
- `mcp__uw-insights__institutional_accumulation_detector` (`lookback_days=10`).
- `mcp__uw-insights__conviction_matrix` — must show DIRECTIONAL_LONG with confidence > 70.

Output: §4 LEAP candidates that pass strict filters; explicit disqualification notes for any contender that doesn't.

---

## Step 2 — Phase 2: risk monitor (sequential, consumes Phase 1 union | sonnet, thinking off)

Once **all** Phase 1 agents return, collect the **union** of every candidate ticker surfaced across all 8 agents for the full week — not a single day's set. Spawn `risk-monitor` with this week-candidate union as input. It must:

- Run `mcp__uw-risk__portfolio_correlation` against this set — flag sub-groups where correlation > 0.7 as concentration risks.
- Run `mcp__uw-insights__signal_confluence` over the candidate union to identify aligned clusters within the week's universe.
- Re-confirm `mcp__uw-risk__market_regime` (today) and tag any candidate whose direction conflicts with the WoW regime delta.

Output: §7 risk & correlation — clusters, regime conflicts, hedge sleeve recommendations.

---

## Step 3 — Confluence gate

Before scoring, apply the **confluence gate**: a ticker only enters the conviction rubric if **at least two distinct Phase 1 agents flag it positively across the week** OR **one Phase 1 agent flags it AND `mcp__uw-insights__signal_confluence` rates it ≥5 at WEEK_END**. Names with only one signal class but no confluence backing are noted in §10 ("Watch-only — single signal") and excluded from the high-conviction list. This rule prevents single-tool false positives from contaminating the trade book.

Note: the threshold here is `signal_confluence ≥ 5` (vs `≥ 4` in `/daily-analysis`) because weekly recommendations carry more capital and need a stricter prior.

---

## Step 4 — Weekly conviction score (persistence-weighted rubric)

For every ticker that cleared the confluence gate, compute the weekly conviction score:

```
Weekly conviction score = Σ:
  +3  swept on ≥3 of 5 days (multi_day_sweep_persistence)
  +3  oi_trend BUILDING for the full week (lookback_days ≥ 5)
  +2  3+ aligned signals in accumulation-hunter sustained across week
  +2  conviction_matrix = DIRECTIONAL_LONG, confidence > 70, stable WoW
  +2  position_rolling_detector shows institutional roll forward into longer-dated LEAP
  +2  cumulative_premium_flow shows ≥$X net directional accretion across the week (LEAP signature)
  +1  in earnings-scout BUY VOL or SELL VOL for next 2 weeks
  +1  multileg-strategist directional structure repeated on ≥2 days
  +1  vol-surface-scout flags KINKED or BACKWARDATION, worsening WoW
  +1  vanna_charm_exposure or dealer_delta_exposure shifts week-over-week in trade direction
  -2  contrarian-scanner crowded long with rising pc_ratio_zscore trajectory
  -2  risk-monitor flags in week-candidate correlation cluster (corr > 0.7)
  -3  WoW market_regime flip conflicts with trade direction
```

### Conviction tiers

Map every ticker to a tier:

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | **HIGH** | full size (subject to win_rate gate in Step 5) |
| 6–8 | **MEDIUM** | half size (subject to win_rate gate) |
| 3–5 | **LOW** | starter / watch-only — paper trade or wait for daily confirmation |
| ≤ 2 | drop | not surfaced in the report's trade book |

Surface every HIGH and MEDIUM tier ticker in the Executive Summary headline and §8 (High-Conviction Cross-Ref). LOW tier goes into a separate "Watchlist for next week" section (§9).

---

## Step 5 — Backtest-weighted sizing (gates the tier sizing)

For each HIGH or MEDIUM tier ticker, identify its dominant signal class — typical labels: `multi_day_sweep`, `oi_build`, `dark_pool_accumulation`, `leap_roll`, `multileg_repeat`, `bullish_flow`, `bearish_flow`, `vanna_squeeze`. Call `mcp__uw-historical__signal_backtest` with that signal class and the ticker. Apply the win-rate gate **on top of** the tier sizing:

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

1. **Sweep signals** — `mcp__uw-hotchains__multi_day_sweep_persistence` per-day breakdown. Did sweeps on days 1–2 continue (sustained conviction) or reverse (fading signal)?
2. **OI-build signals** — `mcp__uw-historical__oi_trend` (`lookback_days=5`). Did OI continue building (BUILDING → WIN) or roll off (LOSS)?
3. **Premium flow signals** — `mcp__uw-historical__cumulative_premium_flow` for the full week range. Did net premium align with the directional thesis?
4. **Direction confirmation** — `mcp__uw-historical__trend_analyzer` over the week range. Did price action confirm or contradict the early-week signal direction?

Grade each ticker:
- **WIN** — signal direction confirmed by end-of-week flow and price trend.
- **LOSS** — price/flow moved against the early-week direction.
- **INCONCLUSIVE** — insufficient price movement or contradictory signals (excluded from hit-rate denominator).

Summarise in a table: `| Ticker | Signal type | Early-week direction | Week-end outcome | Grade | Note |`

Compute the week's hit rate: `wins / (wins + losses)`. This headline goes in the Executive Summary as **Signal performance**.

---

## Step 7 — Strategy synthesis on the conviction list

For each **HIGH and MEDIUM** tier ticker (after the win-rate gate):
1. Call `mcp__uw-insights__stock_deep_dive` — full Yahoo + UW data for full thesis verification.
2. Call `mcp__uw-historical__trend_analyzer` (`lookback_days=10`) — multi-week price/flow trend confirmation.

For the entire HIGH and MEDIUM tier list (in one call):
3. Call `mcp__uw-playbook__batch_strategy_scan` with the ticker list — get rule-based options-strategy suggestions. Cross-reference against multileg-strategist's named structures; prefer the multileg read if there's disagreement and note the conflict.

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
[Table: Ticker | Signal type | Early-week direction | Week-end outcome | Grade | Note. Hit rate headline. Sourced from multi_day_sweep_persistence, oi_trend, cumulative_premium_flow, trend_analyzer — no daily files read.]

## 1. Regime & WoW Delta
- `market_regime` today + Monday baseline; WoW delta narrative
- `volatility_risk_premium` classification — premium-selling vs premium-buying environment
- `dte_volume_share` aggregated across the week — institutional vs retail share trend
- Implications for next week's bias

## 2. Sector Rotation
- `sector_flow_persistence` — which sectors saw sustained inflows vs outflows across the full week
- Persistence score per sector + named single-name leaders within each rotating sector
- Rotation narrative for next week

## 3. Swing Book (1–6 weeks) — ranked by weekly conviction score
[Table: Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure | Invalidation. Subdivide into 3a long swings (regime-aligned) and 3b short/fade swings (defined risk only).]

## 4. LEAP Book (6–24 months)
[Table: Ticker | Tier | Score | Win-rate | Final size | Scenario | Invalidation. leap-positioning-radar with `position_rolling_detector` highlights and `cumulative_premium_flow` accretion. DIRECTIONAL_LONG only.]

## 5. Volatility Surface — WoW Term Structure & Skew Evolution
- vol-surface-scout: names that shifted to KINKED or BACKWARDATION across the week
- WoW IV term-structure delta with `iv_term_structure` snapshots from `covered_dates[0]` and `WEEK_END`
- Skew change narrative; calendar-spread candidates
- `iv_percentile_zscore` outliers (multi-month percentile context)

## 6. Earnings — Recap & 2-Week Lookahead
- (a) Recap of this week's prints with flow reaction grades
- (b) Ranked lookahead to next 2 weeks with IV kink alignment and analyst-vs-flow disagreement scores

## 7. Risk & Correlation (week-candidate universe)
- risk-monitor consuming the full week-candidate union — not the static watchlist
- `portfolio_correlation` clusters with member tickers and corr coefficients
- `signal_confluence` flags
- Concentration risks + recommended hedge sleeve

## 8. High-Conviction Cross-Ref (HIGH and MEDIUM tier)
[Per-ticker breakdown: tier | score components | win_rate | final size | invalidation level. One paragraph per HIGH-tier name.]

Embedded rubric (for audit):

```
Weekly conviction score = Σ:
  +3  swept on ≥3 of 5 days (multi_day_sweep_persistence)
  +3  oi_trend BUILDING for the full week (lookback_days ≥ 5)
  +2  3+ aligned signals in accumulation-hunter sustained across week
  +2  conviction_matrix = DIRECTIONAL_LONG, confidence > 70, stable WoW
  +2  position_rolling_detector shows institutional roll forward
  +2  cumulative_premium_flow shows net directional accretion (LEAP signature)
  +1  in earnings-scout BUY VOL or SELL VOL for next 2 weeks
  +1  multileg-strategist directional structure repeated on ≥2 days
  +1  vol-surface-scout flags KINKED or BACKWARDATION, worsening WoW
  +1  vanna_charm_exposure or dealer_delta_exposure shifts WoW in trade direction
  -2  contrarian-scanner crowded long with rising pc_ratio_zscore
  -2  risk-monitor flags in week-candidate correlation cluster (corr > 0.7)
  -3  WoW market_regime flip conflicts with trade direction

Tiers: ≥9 HIGH | 6–8 MEDIUM | 3–5 LOW | ≤2 drop
```

## 9. Setups for Next Week
- gamma-flip-tracker next-week GEX forecast — zero-gamma level, key pin strikes for SPY/QQQ/IWM
- Pin vs trend regime call
- 2–3 highest-conviction actionable setups for the coming week (HIGH-tier names)
- LOW-tier names to track for daily-analysis confirmation
- OPEX-week flags if applicable (`pin_risk_screener` + `opex_concentration` results)

## 10. Watch-only — single signal, no confluence
[Names that surfaced from one agent but failed the confluence gate. Listed for journaling, NOT for trade entry next week.]
````

---

## Step 9 — Watchlist write-back

Take the top 5 tickers by weekly conviction score (descending) and persist them:

```
mcp__uw-watchlist__manage_watchlist(
  action="add",
  group="conviction_week_<YYYY-WW>",
  tickers=[<top_5_by_score>]
)
```

If any name was already on a manually-curated group, leave that membership alone — write only to the week-stamped group. This closes the feedback loop: this week's high-conviction names become next week's correlation universe.

---

## Step 10 — Save and confirm

1. Use Write to save the report to `analyses/weekly/$ISO_WEEK.md`.
2. Confirm the file was written.
3. Print the **Executive Summary** section to chat. Nothing else — the user opens the file for the rest.

---

## Failure modes & recovery

- **Phase 1 agent times out** — re-spawn just that agent with the same context block. If it fails twice, write its section as `[agent timed out — see <agent-name> logs]` and proceed; do not let one agent block the report.
- **`available_dates` shows fewer than 3 covered weekdays** — produce a "limited-data weekly" with that explicit caveat in the Executive Summary, and downgrade tier thresholds (HIGH = 7+, MEDIUM = 5–6, LOW = 3–4) for the smaller window.
- **`market_regime` errors on Monday baseline** — fall back to `covered_dates[1]` and note the substitution.
- **No tickers clear the confluence gate** — produce a report whose §3, §4, §8 are explicitly empty, with §0 (scorecard), §1 (regime), §2 (sector), §5 (vol surface), §6 (earnings), §7 (risk), and §9 (setups) still populated. A "no edge" week is a valid output, not a failure.
