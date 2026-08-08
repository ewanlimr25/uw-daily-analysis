---
description: Run the full post-market daily intelligence report — regime + GEX + sector flow + sweeps + dark pool + OI + vol surface + LEAP + earnings, organized by trade horizon (0DTE / Swing / LEAP). Two-phase agent fleet with formal conviction scoring, backtest-weighted sizing, and watchlist write-back. Invoke whenever the user asks for an end-of-day or post-market analysis, a daily market report, an EOD briefing, or types `/daily-analysis`. Do NOT trigger for single-ticker deep dives, single-tool queries (e.g. "show me sweeps"), pre-market only briefings (use `uw playbook daily-synthesis` directly), or weekly summaries (use `/weekly-analysis`).
---

# Daily Market Analysis

Run a full post-market intelligence report by trade horizon (0DTE / Swing / LEAP). Two phases: Phase 1 spawns **11 alpha-finding agents** (12 in OPEX week) in parallel against a shared macro context (including a FRED macro snapshot + forward event-risk calendar); Phase 2 runs `signal-confluence-quant` for an audited conviction score, then a `fundamentals-gate` cross-check and a bounded `bull-researcher`/`bear-researcher` debate on the top-5, then `risk-monitor` to gate and size. Every ticker is scored against a formal conviction rubric, top names are backtested for win-rate and fundamentally vetted before sizing, the top 5 are written back to the watchlist, and a machine-readable `decision.json` envelope is emitted beside the report. Each run gets its own folder: `analyses/daily/YYYY-MM-DD/` holding `report.md` + `decision.json`.

## Data access — the `uw` CLI

All Unusual Whales data comes from the **`uw` CLI** (`/Users/ewan/.local/bin/uw`; override with `$UW_PP_CLI`), invoked via Bash. Canonical convention for **every** call in this command and **every spawned agent**:

```
uw <group> <subcommand> [--flag value …] --json --quiet
```

- `--json` is **mandatory** (the CLI defaults to a rendered table); `--quiet` drops banners so stdout is pure JSON. Parse with `jq` / `json.loads`.
- Pin point-in-time tools to the data date with `--date <YYYY-MM-DD>`.
- For tie-prone lists (`sector-flow-persistence`, any `--top-n` with score ties) **sort by an explicit key** — Go map order is non-deterministic.
- Trim large payloads with `--select <dotted,paths>` / `--compact` to save tokens.
- Fundamentals enrichment still uses the **yfinance MCP** (`mcp__yahoo-finance__*`) and `scripts/finnhub_enrich.py` — unaffected by this CLI path.
- **Non-flow context** (short interest, days-to-cover, float, analyst consensus, breadth, insider clusters) comes from the **`fz` CLI** (`finviz-pp-cli`), invoked via Bash as `fz <group> … --agent`, and the `scripts/fz_enrich.py` wrapper. It is a fundamentals/screening/breadth augment **beside** the flow engine — it adds **zero** options flow / greeks / dark pool / GEX / OI and replaces no `uw` tool. Every `fz` lane is **advisory (0 rubric points)** and **graceful-skip**: if `fz` is unavailable the report completes unchanged. See `analyses/audit/2026-05-27-fz-edge/`.

## Model routing

Fleet models and effort are pinned per-agent in `.claude/agents/*.md` frontmatter (`model:` + `effort:`) — the single source of truth; do **not** restate model assignments in spawn prompts (prompt-text "Model:" lines are mechanically inert). Current pins (re-evaluated 2026-08-08 for the Claude 5 generation — Opus 5 / Sonnet 5): `signal-confluence-quant` and `risk-monitor` = opus/high (the envelope-writing + state-mutating choke points; formerly fable — the Opus 5 move also removes the fable credit-wall fragility of 2026-07-07); rest of the fleet = sonnet — **high** for the synthesis-heavy agents (accumulation-hunter, dealer-positioning-strategist, sector-rotation-strategist, earnings-scout, contrarian-scanner, multileg-strategist, bull/bear-researcher — the debate pair stays symmetric), **medium** for the mechanized/script-driven ones (sweep-tracker, leap-positioning-radar, fundamentals-gate, vol-surface-scout, gamma-flip-tracker, opex-pin-strategist). `multileg-strategist`'s former opus pin was relative to the older sonnet; Sonnet 5 clears that bar. Run the orchestrating session itself on **opus minimum (Opus 5 or better)** — Step 0, the confluence gate, rubric application, and report/envelope authoring live in the main loop. Original rationale + escalation triggers: `analyses/audit/2026-07-03/agent-model-effort-audit.md`; the next `/calibration-audit` must grade this model transition (quant-input compliance, debate residuals vs baseline, Σ spot-checks) as it did for the 2026-07-03 pins.

**Scope discipline (orchestrator):** spawn exactly the agents this command names, in the batches it names — 11 Phase 1 agents (12 in OPEX week) in one message, then the four Phase 2 stages sequentially. Do not spawn additional subagents to verify, re-check, or parallelize work the main loop owns, and do not add pipeline steps beyond those written here. The validator scripts and gate stack are the verification layer; no extra passes.

## When to invoke

- Post-market daily report ("EOD analysis", "end of day report", "wrap up the day", "daily intel")
- Slash command `/daily-analysis`
- "Morning briefing" — but only if it should integrate Phase 1 specialist agents. For a fast sub-2-minute briefing, just call `uw playbook daily-synthesis` directly without spawning the fleet.

## When NOT to invoke

- "What's NVDA doing?" → `uw insights deep-dive`, not the full pipeline.
- "Show me today's sweeps" → `uw options-flow sweeps` directly.
- "Find earnings plays this week" → spawn `earnings-scout` alone.
- "Build me a watchlist" → `uw watchlist manage` directly.
- "Recap the week" → `/weekly-analysis`, not `/daily-analysis`.

## Operating principle: prefer multi-day metrics over single-day snapshots

Every spawned agent must prefer multi-day persistence tools over single-day equivalents wherever the CLI supports it. Specifically: `uw historical oi-trend` over `uw oi biggest-increases`, `uw hot-chains sweep-persistence` over `uw options-flow sweeps` for ranking (informational ranking / prose only — the sweep-persistence rubric line was removed 2026-05-23 P0.3; it earns 0 points), `uw options-flow sector-flow-persistence` over `uw options-flow sector-flow` for rotation calls, `uw historical pc-ratio-zscore` over the deprecated `uw screener put-call-extremes`, and — for the quant ONLY — `uw historical signal-backtest` under the P0.3 clean-query protocol before sizing any trade (2026-06-12: the tool is quarantined; Phase 1 agents must not call it and its raw headline is never quoted). Single-day signals are noise; multi-day persistence is the edge. Pass this instruction through to every spawned agent.

---

## Step 0 — Preflight & shared macro context

This step builds the shared context every Phase 1 agent receives. **Do not skip any sub-step** — agents that lack the macro anchor produce inconsistent calls.

1. **Date** — run `date +%F` to get today's `YYYY-MM-DD`. This is the report filename, the `conviction_<date>` watchlist group key, and the date passed to every `uw` call.

1a. **Shared-payload cache — fetch every market-wide payload ONCE.** After the date and coverage check, run:
   ```
   mkdir -p analyses/daily/<date>
   python3 scripts/step0_cache.py --date <date> --regime <bull|bear|neutral>
   ```
   It writes ~22 market-wide payloads to `analyses/daily/<date>/step0_cache/*.json` and prints a manifest with a `paths` map (`{logical_name: file_path}`), the exact `command` behind each file, and a `failed[]` list. Cached files are **reused** on re-invocation unless `--refresh` is passed, so a resumed or re-run report reads the same tape instead of re-querying a moving one. Every payload graceful-skips — a failure is recorded and the run continues. `python3 scripts/step0_cache.py --date <date> --list` prints the registry.

   **Why this exists (measured, not theoretical):** on 2026-07-24 `earnings-scout` and `vol-surface-scout` each independently fetched `screener earnings-catalyst` and produced **byte-identical 528,504-byte payloads** (md5 `162d3b906dd245556774478ac665fb73`) in the same run; `expiry-heatmap`, `iv-rank` and `iv-outliers` have 2–4 declared consumers each and were re-pulled after Step 0 had already fetched them. The registry only holds payloads that are **market-wide** (no `--symbol`, so one fetch genuinely serves everyone) **and** declared by **≥2 consumers** — per-symbol pulls stay with the owning agent, since caching those would just relocate the work.

   **HARD RULE to pass to every Phase 1 agent:** hand each agent the cache **file paths** for the payloads it needs and instruct it to `Read`/parse those files rather than re-issue the command. This extends the existing no-re-fetch rule (which already covers `market-regime`, `daily-synthesis`, `vrp`, `front-end-iv-ratio`) to the full shared set. An agent that re-fetches a cached market-wide payload is burning wall-clock on a parallel critical path for a byte-identical result.

1b. **`fz` health probe (2026-05-27 `fz`-edge Phase 0).** Run `fz --version` (and optionally `fz doctor --agent`). If it returns non-zero or the binary is missing, set `fz_available=false` and **graceful-skip every `fz` lane** in this run (the breadth cross-check, the squeeze/RS funnel lanes, the fundamentals-gate `fz_enrich` call, the accumulation insider-cluster co-flag, and the debate analyst context) — exactly like the yahoo-broken / Finnhub-403 skip pattern. **Never hard-fail the report on `fz`.** When `fz_available=true`, the lanes below run; all remain **advisory (0 rubric points)**.

2. **Coverage check** — call `uw historical available-dates`. Confirm today's date is present. If the latest date lags more than one trading day, abort and tell the user "UW data is stale by N days — re-export from Unusual Whales before running."

3. **One-call briefing** — call `uw playbook daily-synthesis` with today's date. This returns the regime classification, top bullish/bearish confluence tickers, and watchlist alerts in a single call — the shared context anchor for every Phase 1 agent. **Pass this synthesis output to every agent in Step 1** so they don't redundantly re-call `uw risk market-regime` or `uw insights signal-confluence`.

4. **Macro layer** — call these in parallel and capture the readings:
   - `uw risk market-regime` — SPY/VIX trend + breadth classification (will be the top-line of §1 of the report).
   - `uw options-flow dte-volume-share` — share by 0DTE / weekly / monthly / LEAP. High 0DTE share = retail-dominated tape; high monthly+ share = institutional positioning. This is the regime hint Phase 1 agents need to interpret their own findings.
   - `uw historical vrp` — IV30 vs realised σ30. Whether the day is a premium-selling or premium-buying environment changes which Phase 1 agents you trust most (selling environment → vol-surface-scout & contrarian-scanner; buying environment → gamma-flip-tracker & earnings-scout).
   - **Breadth cross-check (`fz`, advisory — 2026-05-27 `fz`-edge A2; skip if `fz_available=false`):** `fz breadth --group sector --agent` returns `{advancers, decliners, pct_green, avg_change, median_change, top_mover, worst_mover, total}` — a free, independent, **logged** advance-decline series from a different data lineage than `uw risk market-regime`. Capture it as `breadth_cross_check`. **Cross-check vs the `uw` regime label**: a green index with `pct_green < 50` (more decliners than advancers) is a breadth-divergence / distribution tell the single regime label hides — surface that divergence in §6 prose. Advisory only — it does **not** override the `uw` regime and earns 0 points.

5. **Sector layer** — call in parallel:
   - `uw options-flow sector-flow` — single-day sector premium balance (snapshot).
   - `uw options-flow sector-flow-persistence` — multi-day rotation persistence score (the durability check that gates §2 of the report).

   These two are **GICS-aggregate** (no symbol input) — they are the shared anchor. The **ETF instrument-level flow tape** (the canonical ETF universe defined in `sector-rotation-strategist.md`) is swept **per-symbol by the agent in Step 1**, not here — do **not** add the ~21 per-symbol ETF calls to preflight. The agent owns the ranked deep-pull; Step 0 stays GICS-aggregate.

6. **Top-of-funnel screens** — all of these are in the Step-0 shared cache (sub-step 0), so read the cached files rather than re-issuing them:
   - `uw screener bullish-bearish --direction bullish|bearish --top-n 25` (top 25 each side) — net premium leaderboard. → `screener_bullish.json` / `screener_bearish.json`
   - `uw insights signal-confluence --direction bullish|bearish --min-score 3 --top-n 25` — multi-factor scoring; agents start their hunts here. → `signal_confluence_*.json`
   - `uw screener volume-vs-average --top-n 25 --min-volume-ratio 3` — flow anomalies vs 30-day baseline. → `volume_vs_average.json`
   - **`uw screener iv-rank --mode high|low --top-n 25`** (top 25 high, top 25 low) — premium-selling and premium-buying candidates. → `iv_rank_high.json` / `iv_rank_low.json`
     > ⚠ **CLI FLAG TRAP — this subcommand takes `--mode`, NOT `--direction`.** Its neighbours `screener bullish-bearish` and `insights signal-confluence` both take `--direction`, so flag-transfer is the natural error and it cost two failed calls on 2026-07-24. There is no `--direction` on `iv-rank`; passing it errors out.
   - **`fz` squeeze + RS lanes (advisory — 2026-05-27 `fz`-edge A4; skip if `fz_available=false`):** the `uw` funnels above are all *flow-derived* — they only see names that already lit up the options tape. Add two **orthogonal, non-flow** entry axes via Finviz screens, server-side liquidity-pre-filtered:
     - **Squeeze lane:** `fz screen --filter sh_short_o20,sh_price_o5,sh_avgvol_o500 --view ownership --agent` — short float > 20%, price > $5, avg volume > 500k. Returns per row `{Ticker, Short Float, Short Ratio, Float, Price, Volume, …}` — squeeze candidates the flow screener misses until too late.
     - **RS / breakout lane:** `fz screen --signal ta_newhigh --filter sh_price_o5,sh_avgvol_o500 --agent` — relative-strength leaders / new-high breakouts.

     Tag squeeze rows `source: fz_squeeze` and RS rows `source: fz_rs`, then **union them into the candidate set fed to the Phase-1 agents** (they still need ≥2-agent confluence in Step 3 to enter the rubric — these are candidate *surface*, not pre-scored calls). The `fz` filters pre-enforce a coarse liquidity floor; the authoritative C12 floor below still applies to every unioned name.

   **Liquidity floor (2026-05-25 register C12) — apply to every screened name before handing to agents.** Each candidate must clear **price ≥ $5 AND 20-day dollar-ADV ≥ $50M** (or notional-equivalent). Use the screener `close` for price and a 20-day dollar-volume estimate (equity `volume × close`, or yahoo `get_historical_stock_prices` for the underlying; "notional-equivalent" = options dollar volume where equity ADV is unavailable). **Fail closed:** a name whose liquidity cannot be verified is dropped, not passed. ADV is **dollar** volume (shares × close), *not* a raw share count. Drop sub-floor names from the funnel entirely — they pollute the candidate set, the confluence breadth, and the win-rate denominator. **This floored set is the funnel every downstream step consumes** — the OPEX guard (sub-step 7), all Phase 1 agents (Step 1), and the quant's win-rate denominator (Step 5) operate on the floored names, never the raw screener output. Rationale: the `volume_spike` screen returns micro-ETFs (GIF/BLCN/PEX/IGLD/UTHY/ESGE — all sub-$50M ADV) the desk cannot fill at size; Barbon & Buraschi show flow effects are strongest (and least exitable) in exactly these illiquid names.

   **Run the floor, do not hand-roll it:**
   ```
   python3 scripts/market_data.py --as-of <date> --symbols "<comma-separated funnel names>"
   ```
   **Always pass `--as-of <report date>`.** The chart API otherwise returns the latest sessions, so a re-run or a later `/calibration-audit` would measure a different tape than the report claims. This is the same `--date` discipline every `uw` call follows. Verified: `--as-of 2026-07-24` reproduces that run's verdicts exactly (CBRG `price 4.27 < 5.00`; LXU/UTI/NVCR/TRLV sub-$50M ADV), whereas an unpinned call one day later passes CBRG at $5.25.
   It fetches OHLCV from the raw Yahoo chart API (verified working and correctly year-anchored — closes reconcile exactly against the `uw` screener) and returns `c12_pass[]`, `c12_fail[{symbol, reason}]`, plus per-symbol `last_close`, `adv_usd_millions`, `change_1d_pct`, `change_5d_pct` and `realized_vol_pct`. It is **fail-closed**: an unfetchable symbol is reported as a C12 FAIL with a reason, never silently dropped or passed. The decision logic lives in `scripts/excess_winrate.py:apply_liquidity_floor`; `market_data.py` is the acquisition half — note that `uw historical trend` carries **no open/high/low and no share volume**, so the ADV numerator cannot be built from the `uw` CLI at all, and the yahoo **MCP** path is the one recorded as year-anchored/unreliable.

   **Use the same call for the tape framing.** The `change_1d_pct` / `change_5d_pct` columns are how you tell a broad rally from a cap-weighted decline. On 2026-07-24 this distinction was outcome-relevant and was nearly missed: `fz` breadth showed 72% of S&P names green, but QQQ closed **−1.12%** and the AI/semis complex fell 7–15% (NBIS −15.0%, BE −14.9%, SOXL −13.1%, SNDK −10.8%, MU −7.0%). "Broad bounce" and "rotation out of one complex" are opposite reads and only the OHLC separates them — check it **before** writing the framing into agent prompts. Include `SPY,QQQ,IWM,RSP,^VIX` plus the sector ETFs in the same batch; it is one call. Note that index symbols (`^VIX`, `^GSPC`) carry **no share volume**, so their ADV is 0 and they always show as a C12 FAIL — that is correct and expected, they are tape context, not funnel candidates.

7. **OPEX guard** — if today is within 5 calendar days of the third Friday, also call `uw oi pin-risk` and `uw oi opex-concentration` for SPY/QQQ/IWM and any name in the top of step 6. Pinning candidates feed the `opex-pin-strategist` scored book (§3 / §7) — **not** the §2 advisory, which is SPY/QQQ next-session GEX only.

8. **Macro & event-risk layer** — `uw risk market-regime` gives a regime *label*, not a *calendar*. A swing book sized Tuesday with CPI Wednesday carries un-priced event risk. Build the macro layer once here (it respects the no-re-fetch hard rule — fetch once, pass down):
   - **Macro snapshot** — run `python3 scripts/fred_macro.py` via Bash. It returns a JSON `macro_snapshot` with latest prints + derived signals (yield-curve sign, core CPI/PCE YoY, unemployment, payrolls, 10Y level + 30d direction, USD direction, fed funds). If it returns `available:false` (no `FRED_API_KEY`), note the skip and continue — fall back to the regime label only.
   - **Forward catalyst calendar** — build `event_risk`: the Tier-1 US macro releases in the next ~10 trading days (CPI, PPI, PCE, FOMC/SEP, NFP/jobless claims) with their dates. Use `WebSearch` to confirm the scheduled dates (FRED has no forward-calendar endpoint). Tag each `{event, date, impact}`. Per-name earnings dates are added later in Phase 2 from the fundamentals enrichment — they are not known yet at Step 0.

9. **Next-session 0DTE setup (SPY/QQQ)** — run `python3 scripts/zerodte_setup.py --symbols SPY,QQQ --days 60 --json` via Bash and capture it as `zerodte_setup`. This is the **validated** 0DTE stack (the GEX-wall *pin* idea backtested NO_GO and is NOT used): it returns a rolling premium-selling `backtest` (front-IV implied move vs realized, open-entry vs overnight, GEX→range, VIX-level conditioning, `verdict`) plus a per-index `setup` (`sell_premium`, `vol_state`, `size_scalar`, `expected_range_pct`, `suggested_structure`, `entry_rule`, `stand_aside_reason`). It is **advisory, delta-neutral, 0 rubric points** — it sizes/structures a premium-selling 0DTE plan, not a directional bet, and is NOT a guaranteed edge (validation sample has no vol shock → tail unsampled). If it returns `available:false` (no duckdb / no parquet), note the skip and continue. Feeds §2 directly.

The output of Step 0 is a compact JSON-shaped context block: `{date, fz_available, regime, vrp_classification, dte_share, sector_summary, sector_persistence, top_bullish, top_bearish, confluence, volume_outliers, iv_extremes, breadth_cross_check, fz_squeeze_candidates, fz_rs_candidates, opex_pin_candidates, macro_snapshot, event_risk, zerodte_setup}`. Every Phase 1 agent receives this verbatim; `macro_snapshot` + `event_risk` are consumed primarily by `risk-monitor` in Phase 2, but agents may use them to gate directional calls against an imminent print. The `fz_*` fields are advisory (0 rubric points) and absent/empty when `fz_available=false`.

---

## Step 1 — Phase 1: alpha-finding agents (parallel, single batch)

Spawn these **11 agents simultaneously** — a single message with 11 Agent tool calls (12 in OPEX week, see opex-pin-strategist below). Hand each one the Step 0 context block and the explicit `uw` CLI command list below. The named tools are the minimum each agent must consult; agents can pull additional tools from their own descriptions if their finding is surprising.

**Hard rule:** no agent re-fetches `uw risk market-regime`, `uw playbook daily-synthesis`, `uw historical vrp`, or `uw options-structure front-end-iv-ratio` — those come from Step 0 context only. Re-fetching corrupts the shared anchor and burns tokens.

**Hard rule (extended, Step 0 sub-step 1a):** the same prohibition covers **every payload in the Step-0 cache**. Hand each agent the `paths` entries it needs from the `step0_cache.py` manifest and require it to read those files. The cached market-wide set is: `daily_synthesis, market_regime, dte_volume_share, sector_flow, sector_flow_persistence, screener_bullish, screener_bearish, signal_confluence_bullish, signal_confluence_bearish, iv_rank_high, iv_rank_low, volume_vs_average, earnings_catalyst, expiry_heatmap, iv_outliers, greek_screener, top_premium_trades, most_active, oi_smart_positioning, single_leg, vrp_spy, vrp_qqq`. Per-symbol pulls (`--symbol`) are NOT cached and remain each agent's own work.

### gamma-flip-tracker — next-session 0DTE GEX map for SPY/QQQ ONLY
Scope is the **next session's 0DTE** dealer-gamma prior for **SPY and QQQ only** — read off the standing EOD 0–45d gamma book (OI persists overnight). This is the §2 **advisory** (prose-only, 0 rubric points, no backtested predictive claim). Do **not** cover IWM or single names in this read, and do **not** encroach on swing-horizon DEX/vanna/charm/GEX-trajectory work (owned by `dealer-positioning-strategist`).

Tools required:
- `uw options-structure gex` — **PRIMARY**. Per-strike GEX (default `dte_max=45`), `zero_gamma_level`, `regime`, `total_gex`. The call wall = largest +GEX strike above spot; put wall = most −GEX strike below. Lead every SPY/QQQ read with this. (Do **not** lead with `today_gamma_flip` — it locks to the snapshot's already-expired same-day expiry and its ZGL is unreliable.)
- `uw historical gex-time-series` — `regime_flip_dates` + multi-day ZGL trajectory to judge whether the regime is fresh (just flipped) or held.
- `uw options-flow expiry-heatmap` — context: confirm near-dated expiries hold meaningful share.
- `uw options-flow greek-screener` — `min_gamma` filter for the highest-impact near-dated contracts.

ZGL handling: trust `zero_gamma_level` only when it sits within ~5% of spot; when `null` or extrapolated, fall back to the `total_gex` sign + spot-vs-wall position and mark `zgl_reliable=false`. State the mandatory caveats from §2 (EOD = prior refreshed after the open; gap risk; ETF-not-index book; uw-pp cannot isolate the D+1 expiry).

Output: for **SPY and QQQ** — `{symbol, spot, zero_gamma_level, zgl_reliable, regime, total_gex, call_wall, put_wall, read, structure_bias, caveats}` (the §2 advisory + the `next_session_gex` envelope block).

### dealer-positioning-strategist — swing-horizon dealer flows (NEW)
Scope is **1–4 week** dealer positioning shifts. Owns DEX/vanna/charm/GEX-trajectory work that GF can no longer carry alongside 0DTE.

Tools required:
- `uw options-structure dex` (DEX) — dated-call snapshots; the "flips precede price moves" framing (Karsan / SqueezeMetrics) is practitioner hypothesis, not validated evidence (2026-06-12 P0.4) — only the MECHANIZED sign-change trigger in `dealer-positioning-strategist.md` feeds the scored line, and it is computed by `scripts/dex_flip.py` (not by hand).
- `uw options-structure vanna-charm` — vanna-squeeze setup detector (put-heavy book + falling VIX → BUY setup).
- `uw historical gex-time-series` (lookback 10–30d) — multi-day ZGL trajectory; flag any regime flip across the window.
- `uw options-structure gex` (default `dte_max=45`) — confirm DEX flip is not a single-strike artifact.
- `uw options-structure front-end-iv-ratio` — ratio > 1.05 confirms front panic; consume from Step 0 if available.

Output: SPY/QQQ/IWM and single-name swing dealer reads — DEX state + 5d trajectory, vanna-squeeze flags, ZGL trajectory, regime-flip detections, swing bias for next 1–4 weeks.

### sector-rotation-strategist — durable rotation calls + named single-name leaders (NEW)
Scope is multi-week sector rotation with single-name leaders extracted within each rotating sector. Enforces ≥3-day persistence — single-day sector flow is filtered out.

Tools required (GICS layer — the shared anchor, cross-checks the ETF tape):
- `uw options-flow sector-flow-persistence` — multi-day rotation persistence per sector (PRIMARY).
- `uw options-flow sector-flow` — week-end skew within the persistence narrative (consume from Step 0 if available).
- `uw screener bullish-bearish` — filter by sector to extract single-name leaders.
- `uw options-flow dte-volume-share` — institutional vs retail DTE share. **MARKET-level only (returns `{symbol: MARKET}`), NOT per-sector (2026-06-12 P1.5)** — use as a market-wide regime overlay (high monthly+ share = institutional-positioning tape, rotation calls get the benefit of the doubt; high 0DTE share = retail tape, downgrade all rotation conviction uniformly), not a per-sector split the tool cannot produce.

ETF instrument-level flow tape (per-symbol — GICS tools cannot see ETFs, especially thematics/geographics). Run the **canonical ETF universe** constant in `sector-rotation-strategist.md`, **cap ≤ 40 added `uw` calls**:
- **RANK (≤21):** `uw historical cumulative-premium-flow` (`--symbol <ETF> --days 5`) for every universe ETF — rank by net-premium direction × multi-day persistence. Weight ETF **options** flow above ETF DP. Graceful-skip thin names.
- **DEEP-PULL top 3 inflow + 3 outflow only (≤12):** `uw dark-pool largest` (`--symbol`, positioning/persistence tell — **not** single-name accumulation) + `uw options-flow sweeps` (`--symbol`, directional urgency).
- **CROSS-CONFIRM:** GICS sector + its representative ETF agree w/ persistence → high-conviction; disagree → watch-only. No-GICS thematics → instrument-only (`gics_agreement: n/a`).

Output: rotation regime call (defensive→cyclical / cyclical→defensive / growth→value / value→growth / no_change), per-sector persistence scores, named single-name leaders within each rotating sector, `etf_flow_tape[]` (ranked inflow/outflow ETFs + GICS-agreement + leaders), and a one-line swing-book implication. The ETF tape is **advisory** — it strengthens the existing conditional sector-leader +1 via `gics_agreement`/cum_flow alignment, adds **no new rubric points**.

### opex-pin-strategist — CONDITIONAL: only spawn within 5 days of monthly third-Friday (NEW)
**Conditional spawn.** If TODAY is within 5 calendar days of the monthly third-Friday OPEX, include this agent (12 agents total). Otherwise omit — the orchestrator must not spawn it outside the window.

Tools required:
- `uw oi pin-risk` — pin candidates with strike + `pin_score` (the tool's composite; **there is NO `probability` field** — 2026-06-12 P1.5).
- `uw oi opex-concentration` — OI mass at OPEX strikes; cross-ref against uw oi pin-risk for ranking.
- `uw options-structure gex` — confirm pin strike sits inside / adjacent to a long-gamma wall.

Output: ranked OPEX book — top 5–10 names with `{ticker, pin_strike, distance_pct, oi_mass_at_pin, gex_at_pin, ranked_score, suggested_structure}` (iron flies, short straddles, broken-wing butterflies anchored to pin mechanics).

### sweep-tracker — aggressive directional flow
Tools required:
- `uw options-flow sweeps` (today's top 25 by side and premium).
- `uw hot-chains sweep-ratio` — high sweep-to-volume contracts.
- `uw hot-chains smart-money-flow` — ask vs bid imbalance.
- `uw hot-chains sweep-persistence` — rank by persistence count (≥3 of last 5 days). Single-day sweeps are deprioritised.
- `uw options-flow top-premium-trades` (top 20) — the day's whale tickets.
- `uw hot-chains most-active` — for context.

Output: urgency-ranked sweep ledger with side, premium, expiry, persistence count.

### accumulation-hunter — quiet institutional builds
Tools required:
- `uw dark-pool ticker-summary` (top 30 by premium).
- `uw dark-pool largest` (top 25 with NBBO context).
- `uw dark-pool block-stratified` — tier breakdown so retail noise is filtered out of the institutional signal.
- `uw dark-pool price-levels` — institutional support/resistance for any flagged name.
- `uw insights institutional-accumulation` (a 5-day window) — primary signal.
- `uw oi smart-positioning` — bullish/bearish OI inference.
- `uw historical oi-trend` (`--days 5`) — multi-day OI build verification (BUILDING required).
- `uw dark-pool extended-hours` — overnight/pre-market activity that primed the day.
- `uw oi decrease-with-volume` (`--min-volume 500`) — **distribution counter-signal (C28)**: bullish-side OI being *closed* on high volume on a long-thesis name = accumulation-as-distribution tell. Advisory, 0 points; emits `distribution_flag`.

Output: tickers with ≥3 aligned signals across DP, OI, and accumulation_detector, each with an advisory `distribution_flag` (the C28 direct-flow distribution check).

### contrarian-scanner — overcrowded fades
Tools required:
- `uw historical pc-ratio-zscore` — statistical sentiment extremes (±2σ flags BULLISH_EXTREME / BEARISH_EXTREME). Use this; do **not** use the deprecated `uw screener put-call-extremes`.
- `uw insights price-vs-flow` — when smart money disagrees with price.
- `uw options-flow iv-outliers` — high-IV contracts where flow may be exhausted.
- `uw oi decrease-with-volume` — capitulation / profit-taking detection.
- `uw screener iv-rank --mode high` (extreme high) — premium ripe to fade (flag is `--mode`, NOT `--direction`).

Output: fade candidates gated on regime — short calls in TRANSITIONAL/RISK_OFF, condors in PIN, no naked shorts in TREND.

### earnings-scout — pre-event flow & vol plays
Tools required:
- `uw screener earnings-catalyst` — upcoming earnings + elevated IV (next 14 days).
- `uw insights earnings-play` — pre-earnings setups with OI positioning.
- `uw options-structure iv-term-structure` — BACKWARDATION = imminent event; KINKED = binary expiry kink.
- `uw options-structure term-skew` — back-month put/call skew at the earnings DTE.
- `uw options-structure front-end-iv-ratio` — quick panic detector. **Read it at `--near-dte 7`, never the default `1`** (the default snaps to `near_dte_actual: 0` on an expiry-day snapshot). Confirm any kink-at-the-event claim through `scripts/term_structure_hygiene.py` — it is the same module `vol-surface-scout` uses, so the two lanes stop re-deriving the filter independently (they each did on 2026-07-24).
- `uw insights analyst-vs-flow` — analyst-vs-flow disagreement is the highest-EV setup.

Output: BUY VOL / SELL VOL / SKIP per upcoming print with implied move and IV crush expectation.

### vol-surface-scout — IV dislocations & calendars
Tools required:
- `uw options-structure iv-term-structure` — KINKED / BACKWARDATION / CONTANGO classifier.
- `uw options-structure term-skew` — multi-month skew.
- `uw options-flow iv-outliers` — single-contract IV outliers.
- `uw historical iv-percentile-zscore` — outlier-robust IV percentile (Goyal-Saretto). Use this instead of raw IV rank where possible.
- `uw options-flow expiry-heatmap` — premium concentration by expiry; calendar-spread candidate identification.
- `uw screener iv-rank --mode high|low` — extremes for ranking (flag is `--mode`, NOT `--direction`).

**MANDATORY substrate hygiene — run `scripts/term_structure_hygiene.py`, do not classify from the raw label.** Raw `uw options-structure iv-term-structure` returned **BACKWARDATION on 39 of 41 names** on 2026-07-24; re-deriving the shape after dropping the 0DTE/expired bucket and sub-15-contract tenors flipped **14 of them**. The `dte_approx: 0` bucket carries 250–480% avg IV on any expiry-day snapshot (AKAM: 393.3%), which inverts every front-vs-back comparison. Likewise `front-end-iv-ratio` at its default `--near-dte 1` snaps to `near_dte_actual: 0` and returns meaningless 2.3–8.7 ratios; the module re-reads at `--near-dte 7`.
```
python3 scripts/term_structure_hygiene.py --file <{ticker: iv-term-structure payload}.json>
```
Per ticker it returns `raw_shape`, the kink-aware `shape`, the monotonic `base_shape` (**both**, because a curve can be a contango base *with* an earnings kink and neither label alone describes it), `flipped`/`base_flipped`, `front_end_ratio` + the tenors used, `kink_dte`/`kink_expiry`/`kink_prominence_pct`, `kink_candidates[]` (including sub-threshold near-misses so they stay auditable), and the `dropped[]` tenors each with a `drop_reason`. Verified against the 2026-07-24 tape: front-end ratios reproduce exactly (BE 1.434, VLO 1.230, FSLR 1.169, FTNT 1.551) and the base-shape CONTANGO count reproduces the 13 names that run named.
**`NO_NEAR_TENOR` is not `FLAT`.** When no surviving tenor sits at/under 21 DTE (WHR/DIOD/LDOS/COHU on 2026-07-24 — WHR's first tenor is 28 DTE with earnings 3 days out), the front end is **unmeasurable**; a 1.000 ratio there means "no data", never "calm". `min_contracts` (default 15) is a **named, tunable parameter, NOT audit-frozen** — it was introduced ad hoc and has not cleared a pre-registered bar, so report it rather than treating it as settled.

Output: KINKED names, BACKWARDATION calendars, IV outliers with multi-month percentile context.

### multileg-strategist — institutional structure inference
Tools required:
- `uw hot-chains multileg` — primary signal.
- `uw options-flow top-premium-trades` filtered to ≥$1M premium.
- `uw options-flow greek-screener` — directional / vol / vega bets by Greek profile.
- `uw options-flow expiry-heatmap` — concentration by expiry to spot calendar/diagonal builds.

Output: per-ticker structure read (vertical / calendar / fly / condor / ratio / diagonal) with directional thesis and built-in risk caps.

### leap-positioning-radar — long-dated conviction
Tools required:
- `uw oi biggest-increases` (`min_dte=180`) — fresh LEAP positions only.
- `uw oi position-rolls` — same-day near→far DTE rolls.
- `uw historical oi-trend` (`--days 10`) BUILDING required.
- `uw historical cumulative-premium-flow` (default 90d) — LEAP-grade slow accretion signature.
- `uw insights institutional-accumulation` (a 10-day window) — secondary check.
- `uw insights conviction-matrix` — must show DIRECTIONAL_LONG with confidence > 70.

Output: LEAP candidates that pass strict filters — disqualify and explain anything that doesn't.

---

## Step 2 — Phase 2: quant → fundamentals gate → bull/bear debate → risk-monitor (sequential)

Phase 2 runs in four sequential stages. The quant produces the audited score (2a); the fundamentals gate cross-checks the top-5 against the underlying (2b); a bounded bull/bear debate stress-tests those same names (2c); then the risk officer gates and sizes against regime/VRP/correlation **plus** the fundamentals verdict and debate residuals (2d). Do not collapse them — the separation is the entire point of having auditable, disconfirmed conviction. Stages 2b and 2c operate on the **top 5 by `raw_score` only** (quota-trivial, and the only names that get sized at HIGH/MEDIUM).

### Step 2a — signal-confluence-quant (runs first)

Once **all** Phase 1 agents return, collect every candidate ticker into a single union list with each candidate's flagging agents and named signals. Spawn `signal-confluence-quant` with that union plus the conviction rubric (Step 4 below) as input. It must:

- ~~Run `uw insights signal-confluence` per ticker~~ — **REMOVED 2026-06-12 audit P0.2.** The tool is funnel-only (Step 0 #6); the quant must not call it. `confluence_score` in the output is carried from the Step 0 funnel result when the ticker appeared there (informational only), else `null`.
- Run `uw historical signal-backtest` **per dominant signal class under the P0.3 clean-query protocol** (see `signal-confluence-quant.md` "Signal-backtest substrate quarantine"): `--top-n 200` pinned, rows post-filtered to **complete forward windows only** (`signal_date` ≥ `lookback_days` trading days before the latest data date — the tool's own `truncated_signals` are silently INCLUDED in its headline, so the headline `win_rate` field must never be quoted directly), WR recomputed from the kept rows with the kept `n`. The tool is **market-wide per class** (it has no `--symbol` flag) — label `win_rate_source` accordingly; never present the number as ticker-specific. If the clean protocol cannot be completed for a class, emit `win_rate: null, win_rate_source: "NA(substrate)"` and size by tier default capped at half.
- Pull `uw historical cumulative-premium-flow` (30d and 90d) for tie-breaking and supplemental directional context.
- Compute `raw_score` per ticker against the Step 4 rubric, identify `dominant_signal_class`, attach `win_rate`, and emit `final_size_recommendation_pre_risk` (full / half / starter / skip) with a full audit trail per ticker.

Output: a sorted list of `{ticker, raw_score, score_components[], dominant_signal_class, confluence_score, cum_premium_flow_30d/90d, win_rate, win_rate_uncapped, win_rate_n, win_rate_source, final_size_recommendation_pre_risk, audit_trail}`. **The quant does not gate on regime/correlation** — that's risk's job in 2d.

### Step 2b — fundamentals-gate (top 5; runs after the quant)

The microstructure fleet is **fundamentally blind** — it cannot tell genuine accumulation from smart-money distribution into a deteriorating name. Spawn `fundamentals-gate` with the quant's **top 5 by `raw_score`**, each with its `dominant_signal_class` and inferred thesis direction, plus the Step 0 `as_of` date. For each name it runs `python3 scripts/finnhub_enrich.py --ticker <T> --date <as_of>` and cross-references earnings-surprise streak, insider MSPR, growth/leverage, and the news catalyst stack against the thesis direction.

Output: per-ticker `{ticker, fundamentals_verdict (CONFIRM/CAUTION/VETO/NA), tier_adjustment (0/−1/veto), earnings_trend, insider_signal, next_earnings_date, days_to_earnings, catalyst_support, reasons[], key_risks[]}`. Each name's `next_earnings_date` is fed into risk-monitor's event-risk gate. **NA never penalizes** (data unavailable ≠ evidence against). The verdict block hands to risk-monitor (2d).

### Step 2c — bull/bear debate (top 5; runs after the fundamentals gate)

Conviction scoring is **additive** — crowded consensus names score highest and break hardest, and no agent is tasked to kill the trade. Insert a bounded disconfirmation step. For each of the **top 5 by `raw_score`**, spawn `bull-researcher` and `bear-researcher` for **1 round** (escalate to a 2nd round only when the two residual confidences are within one bin of each other and ≥0.75 — i.e. a genuine disagreement worth a rebuttal). Hand both sides: the ticker's `score_components`, the Step 2b fundamentals enrichment, and the Step 0 macro/event context. Run the 5 names' debates in parallel; within a name, bull then bear is sequential.

Output: per-ticker `{ticker, bull_residual, bear_residual, bull_strongest_unrefuted, bear_strongest_unrefuted}`. The residual pair hands to risk-monitor (2d), which cuts size when the bear's residual ≥ the bull's (the debate did not clear the trade). The debate can only **cut** size, never add it.

### Step 2d — risk-monitor (runs last, consumes quant output + fundamentals verdict + debate residuals)

Spawn `risk-monitor` with (a) the quant's sorted score list, (b) the Step 2b fundamentals verdicts, (c) the Step 2c debate residuals, and (d) the Step 0 macro context (including `macro_snapshot` + `event_risk`). It must:

- Run `uw risk portfolio-correlation` against today's candidates (not the static watchlist) — risk is measured against what we're actually considering.
- Confirm `uw risk market-regime` from Step 0 (do not re-fetch).
- Apply the full sizing-gate stack from `risk-monitor.md`: VETO → watch-only (fundamentals); −1 tier each for regime conflict, `uw options-structure front-end-iv-ratio > 1.10` panic, VRP-vs-trade-type contradiction, corr-cluster duplication, adverse sector rotation, `fundamentals_verdict == CAUTION`, a Tier-1 macro/earnings event inside the trade horizon (event-risk gate), and bear residual ≥ bull residual (debate gate). Emit an explicit `gate_verdicts` line per call — **all 9 keys**, including `fundamentals`, `event_risk`, `debate`, and the new `rubric_regime` verdict (2026-06-12 P0.6) — even when each no-op's.
- Pull `uw watchlist alerts` and `uw watchlist scan` against the rolling `conviction_<yesterday>` group — surface adverse-flow exit candidates.
- Persist today's top-5 conviction names (post-gate, **excluding any VETO'd name**) via `uw watchlist manage --action add --group conviction_<date> --tickers <top_5_by_score>`.

Output: correlation clusters (corr > 0.7 = treat as one position), regime conflicts, VRP / panic gates applied, fundamentals verdicts, event-risk flags, debate-disconfirmation cuts, adverse-flow exit list, hedge sleeve recommendation, and a final sizing table per ticker that consumes the quant's `final_size_recommendation_pre_risk` and applies the gate stack.

---

## Step 3 — Confluence gate

Before scoring, apply the **confluence gate**: a ticker only enters the conviction rubric if **at least two distinct Phase 1 agents flag it positively**. Names flagged by a single agent are noted in §8 ("Watch-only — single signal") and excluded from the high-conviction list. This rule prevents single-tool false positives from contaminating the trade book.

> **2026-06-12 audit P0.2 — the `uw insights signal-confluence` entry path was REMOVED.** The prior "OR one Phase 1 agent + `signal-confluence` ≥4" alternative is gone: the tool is a server-side composite of the same quantities the rubric scores (live factor list: `dp_accumulation`, `oi_building`, `bullish_flow`, `low_pcr`, …), so it can never be the *second* opinion on a name one agent already flagged — it is the first opinion re-aggregated. It also has no per-ticker mode (top-N screener only), which made the path non-deterministic. The tool now has exactly **one role in the whole pipeline: the Step 0 #6 funnel seed.** Do not consult it at entry, scoring, or HIGH-gate stages.

### Step 3a — HIGH-tier load-bearing-tool gate (2026-05-09 audit P0; 3-of-4 as of 2026-06-12 audit P0.2)

After scoring, before any candidate enters the HIGH-tier section of §3 / §7 (i.e. anything that would be sized as `full` post-quant), the call must additionally cite at least **3 of the 4 LOAD-BEARING tools**:

- `uw dark-pool block-stratified` (institutional-vs-retail filter)
- `uw historical cumulative-premium-flow` (30d directional accretion)
- `uw insights institutional-accumulation`
- `uw options-structure dex` (DEX)

A call that scores raw_score ≥ 9 (HIGH-tier under the 2026-05-30 P1.3 cut) but cites fewer than 3 of these four tools must be **demoted to MEDIUM tier**.

# `uw insights signal-confluence` REMOVED from this gate 2026-06-12 audit P0.2 (had been added 2026-05-23).
# Reason: the tool is a composite of the other gate members' own quantities (dp_accumulation / oi_building /
# bullish_flow factors verified live), so citing it added correlated citation breadth, not evidence
# independence — and the +19.5pp (n=12) that justified adding it was selection-confounded (candidates were
# funnel-seeded and gate-admitted on the same score). The 2026-05-30 meta-audit had already found the tool's
# marginal contribution method-unstable (+17.2pp → −1.0pp under path-aware grading).
# Known limitation (2026-06-12 plan, deliberately accepted): the remaining 4 tools are still downstream of one
# actor's footprint — this gate guards against *thin* HIGH calls, not against correlated ones. The structural
# fix (a cross-QUANTITY independence requirement) is pre-registered for a future cycle, not improvised here.

---

## Step 4 — Conviction scoring rubric (applied by signal-confluence-quant in Step 2a)

> **RUBRIC FROZEN — version `2026-06-12` (audit P0.1).** Weights, tier cuts, and gate membership below are frozen as of the 2026-06-12 audit. No line may be promoted, demoted, added, or re-binned until a change clears a **pre-registered, cross-regime, Benjamini-Hochberg-surviving** bar (the same discipline the C-register already applies to C6/C8/C19). Audits **grade** this rubric; they do not retune it. Rationale: six prior cycles re-weighted correlated lines on n=8–31 single-regime marginal contributions whose CIs straddle zero; the cum-flow +2→+3→+1 whipsaw was a realized false positive of that process, and the ≥9 HIGH cut failed its scheduled re-confirmation on 2026-06-12 (HIGH realized 0.222 vs claimed 0.774 on the first post-UPTREND window). Every emitted envelope stamps `rubric_version: "2026-06-12"` so /calibration-audit can stratify by rubric era mechanically.

The rubric below is what `signal-confluence-quant` consumes in Step 2a to produce the audited score. The quant attaches every signed point to a named source agent + tool in `score_components`. Risk-monitor in Step 2d applies the regime / VRP / cluster / fundamentals / event-risk / debate gates **on top of** this score.

```
Daily conviction score = Σ:
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna-squeeze setup in trade direction — the trigger must be a verified SIGN CHANGE, not a level: sign(net_dex) on the latest session opposite to ≥3 consecutive prior sessions, read from dated `uw options-structure dex --date` calls (≥4 to verify the prior-session sign run; ~11 for the trailing-median floor), with |net_dex| on the flip day ≥ 0.25× the trailing-10-session median |net_dex|; the evidence string must cite both dated values. **Compute this with `python3 scripts/dex_flip.py --symbol <T> --dates <d1,d2,...>` (or `--file` with a `{symbol: [{date, net_dex}]}` payload) — do NOT do the arithmetic by hand.** It returns `qualifies`, `direction`, the dated `prior_run_*`, `trailing_median_abs_net_dex`, `magnitude_floor`, `magnitude_ratio`, a ready-made `evidence` string citing both sides, and `sign_changes_in_window` / `whipsaw_warning` (the caveat both 2026-07-24 passers needed: MU and NBIS each cleared the floor while changing sign 4–5× in 14 sessions). Dates must be ISO `YYYY-MM-DD`; non-ISO rows are dropped rather than mis-sorted. Vanna disjunct additionally requires a dated VIX source (Yahoo chart API ^VIX) for the falling-VIX leg — no out-of-band VIX fills.   # DEMOTED +3→+1 and MECHANIZED 2026-06-12 audit P0.4: the 2026-06-11 book awarded the +3 to MU/MRVL/ASML with no DEX sign change anywhere in their 10d windows (level scored as flip — the tool returns a snapshot with no flip field); no peer-reviewed support exists for DEX/vanna flips as 1–4wk directional signals (hedging pressure is intraday-mean-reverting per Baltussen et al. 2021), and a positive DEX *level* in an up-tape is beta (dealer_positioning ran −7pp excess, 2026-05-30 audit). Restore toward +3 only via a pre-registered dex-flip backtest (pattern: scripts/single_leg_whale.py) showing forward excess across ≥2 regimes.
  +3  3+ aligned signals in accumulation-hunter (DP + OI + uw oi smart-positioning, uw dark-pool block-stratified institutional-tier confirmed) — CONJUNCTION (2026-05-25 register C11): full +3 only when cum_premium_flow_30d confirms (sign aligned with thesis AND |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1. Reason: additive DP+accum+matrix manufactured false HIGH conviction (tier inversion HIGH 60.0% < MED 62.5%, n=49); the ≥0.80 WR is a conjunction (DP-block ∧ cum_flow ∧ institutional-accum). Distinct from flow_conflict/−lite (those subtract on opposing/MIXED flow; this reduces the +3 accumulation award to +1 on non-confirming flow — both may fire). A sub-$50M flow that halves this line does not separately qualify as "net directional accretion" for the +1 cum_flow line (demoted from +3, 2026-06-06 P1.4). See signal-confluence-quant.md "Conditional dark_pool_accumulation conjunction".   # was +2; promoted 2026-05-15 audit P1.2 — Phase 4 +27.8pp marginal contribution (LOAD-BEARING)
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)                       # was +2; reduced 2026-05-09 (Phase 4 +5pp marginal — supportive, not load-bearing; correlated with the LOAD-BEARING components above)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL ONLY (2026-05-23 audit P1.1): award +1 only when dominant_signal_class == leap_directional; in all non-LEAP contexts contribution is 0. Phase 4: marginal contribution −23pp (n=8) on swing horizon; the DIRECTIONAL_LONG/>70 signature appears to be a mean-reversion-fade (top-pick) signature outside LEAP. LEAP gate in leap-positioning-radar still consumes this tool — only the swing-rubric award is gated to leap_directional.
  +1  uw historical cumulative-premium-flow shows net directional accretion in trade direction (30d window) — INTENT-SCREENED (2026-06-06 audit P1.4): award the +1 only when the premium passes an intent screen: (a) no C28 distribution_flag present on the name (uw oi decrease-with-volume closing signature), AND (b) on dividend payers inside an ex-div window, the accreting prints are NOT deep-ITM sub-parity calls (dividend-capture arb, not conviction — the NEE 2026-06-04 false-bullish). Screen failed or unevaluated on a flagged name → 0.   # DEMOTED +3→+1 2026-06-06 audit P1.4 — most-cited tool in the book (n=136) and NO-INFO across three consecutive path-aware audits (−3.5pp MC); demoted-not-removed (reconstructed-citation provenance caps at P1; tool stays in the LB gate (3-of-4 as of 2026-06-12 P0.2)). Original promotion (+2→+3, 2026-05-15, +24.2pp) was a close-only-method artifact.
  # +2 line for uw insights signal-confluence ≥4 REMOVED 2026-06-12 audit P0.2 (had been added 2026-05-23 P1.2 on +19.5pp, n=12)
  # Reason: live factor-list probe shows the tool is a server-side RE-COUNT of already-scored quantities
  # (factors: dp_accumulation ↔ the +3 accumulation line, oi_building ↔ the +1 oi-trend line, bullish_flow ↔
  # the +1 cum-flow line) — "second-agent confirmation" was the same tape re-aggregated, near-deterministic
  # for any name with the accumulation stack lit. The promotion evidence was selection-confounded (entry gate
  # and funnel keyed on the same score) and the CLI has no per-ticker mode, so the ≥4 check was non-deterministic
  # (membership in a top-N list). Tool keeps exactly ONE role: the Step 0 #6 funnel seed. It earns no points,
  # gates no entry, and sits in no HIGH-tier gate.
  # +1 line for uw hot-chains sweep-persistence top-5 REMOVED 2026-05-23 audit P0.3
  # Reason: marginal contribution −22pp two consecutive audits (n=15); mega-cap suppression rule from 2026-05-15 P1.1 was insufficient.
  # Tool remains informational — sweep-tracker still surfaces persistence-ranked sweeps in §3/§7 prose — but contributes 0 points to raw_score.
  # If the call merits a multileg or accumulation co-flag, those tools earn the score instead.
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector — CONDITIONAL (2026-05-23 audit P1.5): award +1 only when (a) sector persistence_score ≥ 0.6 (the tool's 0–1 sign-consistency scale = ≥3-of-5-days; 2026-05-25 fix — was an unsatisfiable `≥3`) AND (b) cum_premium_flow_30d direction aligned with thesis direction AND (c) |cum_flow_30d| ≥ $50M. Default 0. Phase 4: sector_persistence marginal +2.8pp standalone (NO-INFO); when paired with cum_flow alignment, it was the difference between HON-W21 (+4.9% WIN) and WMT-W19 (−10.4% LOSS, flow disagreed).
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)   # was +1; promoted 2026-05-09 (Phase 4 +8pp marginal; multileg-vs-batch_strategy disagreements correctly resolved 5/5 in dataset)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising uw historical pc-ratio-zscore (VRP positive)   # MECHANISM (2026-06-12 P1.5, re-attributed per P4): an INFORMED-FLOW CONTINUATION penalty, not a "crowd is wrong, fade it" signal. Single-name P/C extremes predict continuation, not reversal (Pan-Poteshman 2006; Ge-Lin-Pearson 2016) — a crowded long sits on the side informed flow tends to continue, so a LONG resting on crowded-euphoria evidence is the riskier long and gets docked. "Rising" needs a multi-date z trajectory (no single-call path). Frozen at −2 (P0.1); routed through the C13 router so it never double-counts with a flow read.
  -3  flow_conflict — signal-confluence-quant applies mechanically when uw historical cumulative-premium-flow 30d direction is *clearly opposite* dominant_signal_class (signed-sum sign flip + magnitude > today's union-median |cum_flow_30d|, or explicit OPPOSITE label)   # 2026-05-15 audit P0 — see signal-confluence-quant.md "Mechanical flow_conflict deduction" rule; 2026-05-23 audit P1.3: mutually exclusive with flow_conflict_lite (apply ONE, never both)
  -1  flow_conflict_lite — signal-confluence-quant applies when the 30d cum_premium_flow read is MIXED (signed sum near zero, or aligned but bottom-quartile magnitude in today's union)   # 2026-05-15 audit P0; 2026-05-23 audit P1.3: mutually exclusive with flow_conflict (apply ONE, never both)
  # 2026-05-09 -2 generic flow_conflict line replaced with the mechanical -3 / -1 split above (Phase 3 2026-05-15 audit: 30% missed-gate rate at the generic line; NVDA 2026-05-08 raw=10 LOSS dominated by un-penalised flow_conflict against −$17.89M cum_flow_30d)
  # The two lines below are NOT score_components — they are risk-monitor TIER gates applied in Step 2d, listed here only
  # to document the full deduction stack. They contribute 0 to raw_score and never appear in score_components (verified
  # 0/151 envelope calls, 2026-06-12 audit P1/F5 — the quant is forbidden from gating on regime/correlation, risk-monitor
  # acts on tiers not points, and the validator locks Σ score_components == raw_score). Keeping them inside the score block
  # made the rubric overstate its own score-level discipline; they live here as gate documentation, outside the Σ.
  -1  [TIER GATE, 2d] risk-monitor flags in correlation cluster (pairwise corr ≥ 0.70) — −1 TIER, not −1 point
  -3  [TIER GATE, 2d] uw risk market-regime conflicts with trade direction — −1 TIER (regime gate), not −3 points

# Removed from swing/LEAP scoring 2026-05-09 (Phase 4 audit, NO-INFO ±0pp on swing horizon):
#   gamma-flip-tracker 0DTE breakout setup (regime flip + flow alignment) — formerly +2.
#   The signal drives §2 (Next-Session GEX Map — SPY/QQQ advisory) directly, but does NOT earn rubric
#   points on any row. §2 is advisory / prose-only and contributes 0 points to raw_score by design
#   (the next_session_gex envelope block is kept OUT of calls[] so it cannot enter the rubric). This
#   component also double-counted with dealer-positioning's DEX-flip line (then +3, now +1 mechanized — 2026-06-12 P0.4).
```

**Conviction tiers (2026-05-15 audit P0; supersedes prior `≥ 5` HIGH cut and the deferred R-09 from 2026-05-09):**

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | **HIGH** | full size (subject to Step 3a load-bearing-tool gate + Step 5 win-rate gate) |
| 7 – 8 | **MEDIUM** | half size (subject to Step 5 win-rate gate) |
| 3 – 6 | **LOW** | starter / watch-only — supporting candidate in §3/§4, not surfaced in Executive Summary or §7 |
| ≤ 2 | drop | filtered by quant's drop floor |

Surface every **HIGH and MEDIUM** ticker in the Executive Summary and §7 (High-Conviction Cross-Ref). LOW tier names appear in §3/§4 as supporting candidates only. **Tier-cut status (2026-06-12):** the ≥9 HIGH cut (2026-05-30 P1.3, set in-sample on UPTREND data where the ≥9 bin realised 0.774 n=31) **failed its scheduled re-confirmation on 2026-06-12** — bands inverted on the first post-UPTREND window (HIGH 0.222 / MED 0.214 / LOW 0.444, close-only 5d). The cuts are retained under the P0.1 freeze (re-binning on another thin window repeats the documented failure mode) but carry no validated ranking claim; the P0.6 out-of-regime guard caps all sizing at half in the interim.

---

## Step 5 — Backtest-weighted sizing

For each HIGH or MEDIUM tier ticker (raw_score ≥ 7 under the 2026-05-15 cuts), identify its dominant signal class — typical labels: `dark_pool_accumulation`, `multi_day_sweep`, `gamma_breakout`, `oi_build`, `leap_directional`, `bullish_flow`, `bearish_flow`, `multileg_directional`. Obtain the class win-rate **only via the P0.3 clean-query protocol** (2026-06-12 audit; see Step 2a and `signal-confluence-quant.md` "Signal-backtest substrate quarantine") — the raw tool headline is quarantined: its forward windows clamp to the latest bar (complete-window WR 0.485 vs clamped 0.733 on the same class, measured 2026-06-12) and its quote swings 30pp across `--top-n` choices. Apply this sizing map (**2026-05-15 audit PC.1**; full-size threshold tightened 0.65 → 0.70):

| `win_rate` (clean protocol) | Position size |
|---|---|
| ≥ 0.70 | full size |
| 0.65 – 0.70 | half size |
| **0.55 – 0.65** | **starter** — anti-predictive band floor (2026-07-25 audit P1 #4). This band predicted ~0.58 and realised **0.179 overall / 0.133 on 15 post-freeze rows** — worse than the sub-0.50 bucket the rubric is honest about — and **0.55 is the modal post-freeze quote (14 rows)**. Downgrade-only; the quote itself is unchanged so the reliability diagram still bins the true statement. Enforced at emission by `signal-confluence-quant.md`. |
| 0.50 – 0.55 | half size |
| < 0.50 | starter / skip (the quant's authoritative floor — `signal-confluence-quant.md` enforces `win_rate < 0.50 ⇒ pre_risk ∈ {starter, skip}` at emission; never half/full) |
| `null` (newly covered, no history) | starter — matches the quant's sizing map |
| `NA(substrate)` (clean protocol could not complete) | tier default capped at half (HIGH → half, MEDIUM → half, LOW → starter), then gates |

For non-directional signals (`high_iv_rank`, `volume_spike`) the backtest returns `vol_realisation_rate` instead — same thresholds, same clean protocol. Note the win_rate explicitly next to each top call **with its `win_rate_source` and kept `n`**.

**Vol-lane class ceilings (2026-08-01 audit P1 #3).** `earnings_vol` caps at **0.55**, `high_iv_rank` caps at **0.60** — tightening-only, applied on top of the N-cap and the 0.80 absolute ceiling, tightest wins. Both then land in the `[0.55, 0.65)` band, so the anti-predictive floor caps size at `starter`; that stacking is intended. These are the only two classes that survive BH correction as miscalibrations, for a 4th–5th consecutive audit: post-freeze `earnings_vol` realises **0.449 on n=78** and `high_iv_rank` **0.562 on n=16**, while **all 9 post-freeze ≥0.80 quotes in the corpus are this vol lane pinned at exactly 0.80** — the 2026-06-06 ceiling is working (zero quotes exceed it) but it had become these classes' default quote rather than a rare maximum. Levels are **pre-registered** for re-grading (cross-regime ∧ n≥30/arm ∧ BH-surviving); enforced at emission by `signal-confluence-quant.md`.

**SHORT-direction routing — `watch_only`, never sized (2026-08-01 audit P0 #1; register #1 CLEARED).** Before the ladder above is applied, any call whose `direction == short` routes to **`watch_only`** regardless of tier, `raw_score`, or `win_rate`. Instrument-agnostic — single name or index/ETF (the 2026-06-27 ruling withdrew that distinction). This is **routing, not suppression**: keep generating short theses, keep scoring them, keep the full 9-key `gate_verdicts`, and keep serializing them into `decision.json` so `/calibration-audit` continues resolving them and the counterfactual stays gradeable. §3b of the report still runs. **Out of scope:** short legs inside defined-risk spreads, vol structures, and the explicit portfolio beta-hedge sleeve — those are hedge/structure *uses*, not directional short alpha. **Evidence:** paired McNemar `ALL / short` **p=0.0115, BH-surviving** (b=24 vs c=46, n=163), row-matched so the C49 excess-denominator artifact cannot explain it; both tape arms clear n≥30 and agree (**UP −13.0pp n=92 / DOWN −14.1pp n=71**) — the deficit is identical in rising and falling tape, so this is mis-selection rather than mistiming, which retires the "shorts regain edge in a real downtrend" clause the 06-27 ruling was waiting on. Direction-call accuracy 36.0% in a falling tape; sized book 0.294 vs DROP 0.411 in that tape. The **long** book is untouched and carries the mirror result (`ALL / long` p=0.0046, BH-surviving, n=204). `risk-monitor` and `signal-confluence-quant` both enforce this so a short cannot be re-sized by a later gate.

**Out-of-regime guard (2026-06-12 audit P0.6, downgrade-only):** the rubric was fitted entirely in the UPTREND regime that ended 2026-06-12. Until a `/calibration-audit` records **≥30 resolved post-2026-06-12 calls** and re-validates the tiers, every conviction-tier size is **capped at half** regardless of win_rate, and the Executive Summary must carry the line `Rubric regime status: OUT-OF-REGIME (fitted UPTREND; current <regime>) — sizing capped at half`. risk-monitor enforces the cap (its `rubric_regime` gate) — the lift happens by editing this block when the named audit clears it, not by discretion.

**On top of this ladder the quant applies four downgrade-only guards** — all stack, none ever upgrades (see `signal-confluence-quant.md` "Market-excess gate" + the N-conditional cap): (1) the `n < 10` cap is **0.69** (below the 0.70 full line — a small-N up-week class sizes at most half), and (2) a **market-excess gate** — if a class does not beat the same-direction SPY bet over the same windows (`excess ≤ 0`), cap at half; `excess ≤ −0.10` → starter. Beta in an up-tape is not edge. The win-rate denominator is computed only over liquidity-floor-passing names (C12). Reusable: `scripts/excess_winrate.py:size_decision`. **(3, register C4)** a `bullish_flow`/`bearish_flow` class also caps at half when the flow is **not OI-confirmed-opening** (Pan-Poteshman: only opening flow predicts) — `uw historical oi-trend` BUILDING or ΔOI ≥ 20% of day volume; flat/falling OI vs high volume = churn → cap half. Reusable: `scripts/oi_opening.py:opening_gate_size`. **(4, 2026-07-25 audit P1 #4)** the anti-predictive **[0.55, 0.65) band floor** in the table above caps at `starter`. Reusable: `scripts/excess_winrate.py:anti_predictive_band_gate` (already wired into `size_decision`). All four guards are downgrade-only and may stack.

---

## Step 6 — Deep dive on the top 3 by conviction

For each of the **top 3 tickers by conviction score**:
1. Call `uw insights deep-dive` — full Yahoo + UW data for full thesis verification.
2. Call `uw historical trend` (`--days 10`) — confirm the multi-day price/flow trend.

This step is the synthesis bridge from "signal" to "thesis" — without it, conviction scores are abstract.

---

## Step 6.5 — Batched strategy synthesis on the conviction list

For the entire **HIGH and MEDIUM tier** list (raw_score ≥ 7), make a **single** `uw playbook batch-scan` call with the full ticker list. This replaces per-ticker `uw playbook suggest-strategy` calls — one batch call is materially cheaper and produces consistent strategy logic across the book.

Cross-reference each batched recommendation against any named structure from `multileg-strategist`. **Prefer the multileg read** when the two disagree (multileg saw the actual coordinated flow; the rule-based scan is a heuristic) and note the disagreement in §3 / §7 of the report.

---

## Step 7 — Write the report

Synthesize into the structured markdown below. The report is organized **by trade horizon**, not by agent. Use tables for data-dense sections and full sentences for thesis sections. Tone: institutional desk strategist — precise, assertive, no filler. Match each section's length to its substance — no filler sections, no restated Step 0 context, no summary-of-the-summary; an empty section states that it is empty in one line.

```markdown
# Daily Market Analysis — YYYY-MM-DD

## Executive Summary
- **Regime + GEX state:** <one line — regime label, SPY/QQQ/IWM gamma, VIX, breadth, sector lean>
- **Rubric regime status:** <`IN-REGIME` or `OUT-OF-REGIME (fitted UPTREND; current <regime>) — sizing capped at half` — the P0.6 guard line; mandatory while the 2026-06-12 freeze block in Step 5 is active>
- **Next-session GEX (SPY/QQQ):** <per index: regime (long/short-gamma) · ZGL · call wall / put wall · one-line structure bias> — advisory, see §2
- **Top swing build:** <ticker, thesis, structure, invalidation, win_rate, size>
- **Top LEAP candidate:** <ticker, scenario, structure, invalidation, win_rate, size>
- **Biggest risk:** <correlation cluster name, members, hedge sleeve>

## 1. Regime & Gamma State
- `uw risk market-regime` reading + breadth narrative
- Per-index gamma table: spot | zero-gamma | total GEX | regime | call wall | put wall (rows: SPY/QQQ/IWM). This is the **current-state** EOD book; §2 carries the forward, next-session **advisory** read of these same levels for SPY/QQQ with concrete 0DTE structure guidance.
- `uw options-flow dte-volume-share` summary (institutional vs retail share)
- `uw historical vrp` classification
- **Macro backdrop** (`scripts/fred_macro.py` `macro_snapshot`): yield-curve sign, core CPI/PCE YoY, unemployment + payrolls, 10Y level/direction, USD direction — one line. Plus the forward `event_risk` calendar: Tier-1 prints in the next ~10 trading days.

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — built from open interest that **persists overnight** — read forward as the *prior* for next session's open. It is **prose-only, contributes 0 points** to the conviction rubric (Step 4), and makes **no backtested predictive claim**. The predictive validation of these levels lives in `/weekly-analysis`'s rolling §2 backtest (`scripts/gex_next_session_backtest.py`), not here. Scope is **SPY and QQQ only** — no IWM, no single names.

Lead with `gamma-flip-tracker`'s next-session read for **SPY and QQQ** (primary tool `uw options-structure gex`, default `dte_max=45` — **not** `today_gamma_flip`, which locks to the snapshot's already-expired same-day expiry and returns an unreliable ZGL):

| Field | Source | How to read it |
|---|---|---|
| spot · zero-gamma (ZGL) · regime | `uw options-structure gex` | **long-gamma** (spot ≥ ZGL, `total_gex` > 0) → mean-revert / pin / vol suppression; **short-gamma** (spot < ZGL, `total_gex` < 0) → trend / breakout / vol expansion. Distance spot-to-ZGL scales conviction; sitting on the flip = NEAR_FLIP, do not fade. |
| call wall · put wall | `uw options-structure gex` `per_strike` | call wall = largest +GEX strike above spot (cap / upside magnet); put wall = most −GEX strike below (support). Distance-to-wall sets the realistic next-session range and whether the 0DTE straddle is rich (walls tight) or cheap (walls wide). |
| regime freshness | `uw historical gex-time-series` `regime_flip_dates` | flag whether the regime just flipped (fresh, unstable) vs held for several sessions. |

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

- **Whether (VRP):** the front-expiry implied move systematically exceeds the realized next-day open-to-close move. Report `sell_premium` + the rolling `backtest.verdict`. **2026-06-12 P1.8 — quote the PnL on its real basis and net of cost:** the `mean_pnl_open_pct` is **% of underlying spot notional, GROSS** (`pnl_basis` field spells this out) — it is NOT premium-collected and NOT margin-relative, so a "+0.30%/day" figure is tiny in absolute terms. Report `mean_pnl_open_net_pct` (gross minus the assumed `round_trip_cost_pct_assumed` half-spread+fees) **alongside** the win-rate, and lead with net — Vilkov (2024) found an unconditional 0DTE condor flips to negative net Sharpe once costs are charged, so the gross win-rate overstates a negatively-skewed seller's edge.
- **How much (GEX vol-suppression, Barbon-Buraschi):** long-gamma → quieter next-day range → tighter wings; short-gamma → wider range → wings out or stand aside. Use `expected_range_pct` for wing width.
- **Size (VIX level):** scale by `size_scalar` / `vol_state` — bigger when VIX rich, skip when VIX low (thin edge).
- **When:** `entry_rule` — **enter at/after the open once the gap resolves; hold the 0DTE to the close; never carry overnight** (overnight entry backtested negative — the gap erases the edge). If it gaps beyond the wings, stand aside.
- **Stand aside** when `stand_aside_reason`/`caution` is set (VIX spiking or front-end backwardation — the regime where short-vol blows up).
- **Direction:** none — this is delta-neutral. Do not add a directional tilt.

Per index, surface `{sell_premium, vol_state, size_scalar, expected_range_pct, suggested_structure, entry_rule, stand_aside_reason}` plus `{mean_pnl_open_pct (gross), mean_pnl_open_net_pct, pnl_basis}`. **SPY ≈ SPX** (validated identical — trade either); **QQQ is weaker** (Nasdaq index book unavailable) — flag its lower confidence. **Promotion bar (P1.8):** this lane stays advisory / 0 rubric points **permanently** until BOTH a vol-shock day enters the sample (the short-vol left tail is currently UNSAMPLED) AND **net** expectancy clears a tail-aware bar — win-rate is explicitly NOT the promotion metric for a negatively-skewed short-vol strategy.

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
**Invalidation discipline (C34):** where the name carries a dark-pool price-levels read (`uw dark-pool price-levels`, already pulled by accumulation-hunter), anchor the `Invalidation` to the **real institutional level** ("loses the 731.50 DP shelf") rather than a guessed percentage — the level the size actually defends is more actionable than a round-number stop. Fall back to a % / DEX-reversal rule only when no DP level exists.
Subdivide into:
- **3a. Long swings (regime-aligned)** — accumulation + multileg directional + earnings BUY VOL + dealer-positioning vanna-squeeze + sector-rotation leaders. For any long name carrying a `distribution_flag` (bullish-side OI being closed on the tape — accumulation-hunter C28), add a one-line **distribution caution** ("⚠ 720C OI −61.6k on 69.9k vol — watch for accumulation-as-distribution") — advisory, 0 points, does not change the sizing.
- **3b. Short / fade swings (defined risk only)** — contrarian + earnings SELL VOL + analyst-vs-flow disagreement + dealer-positioning DEX-flip-short. **All directional shorts print as `watch_only` (2026-08-01 P0 #1)** — the section still runs and still carries full theses, structures and invalidations, but no directional short is sized. Short-vol structures (SELL VOL) and defined-risk short legs are unaffected; the routing rule governs directional short *alpha* only.

Surface the urgency-ranked, persistence-first near-term **sweeps** from `sweep-tracker` here as well (relocated from §2; informational — 0 rubric points unless the name also earns a scored co-flag).

## 4. LEAP Builds (6–24 months)
leap-positioning-radar — DIRECTIONAL_LONG only with full disqualification notes for near-misses.

## 5. Volatility Surface
vol-surface-scout — KINKED names, BACKWARDATION calendars, IV outliers, calendar-spread candidates with implied move per name.

## 6. Risk & Correlation
risk-monitor consuming today's Phase 1 candidate union and the quant's audited score (not the static watchlist) — clusters, regime conflicts, VRP / panic gates applied, **fundamentals verdicts** (CONFIRM/CAUTION/VETO per top-5 name with the contradicting facts), **event-risk flags** (Tier-1 macro / earnings inside a trade's horizon), **debate-disconfirmation cuts**, hedge sleeve recommendations. Lead with the `macro_snapshot` headline + forward `event_risk` calendar. When `breadth_cross_check` is present, add one line on breadth: advancers/decliners + `pct_green`, and **flag any divergence** from the `uw` regime label (green tape with `pct_green < 50` = distribution tell) — advisory, does not change sizing.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
Per-ticker breakdown sourced from the `signal-confluence-quant` audit trail: `raw_score` | `score_components[]` (with named source agent + tool per component) | `dominant_signal_class` | `win_rate` (with `n` + source) | pre-risk size | `fundamentals_verdict` | bull/bear residuals | risk-monitor gates applied (`gate_verdicts`) | final size | invalidation level. Note any VETO'd name here with the distribution evidence (`distribution_flag` when present) even though it drops to watch-only.

**Expectancy lens (advisory — C31).** Above the per-ticker table, print a one-row-per-tier line: **realised per-tier expectancy and payoff ratio** (avg win / |avg loss|) from the most recent `/calibration-audit` (`phase_3_calibration` table) or, if unavailable, computed over the rolling `conviction_<date>` closed calls via `scripts/kelly_sizing.py` (`payoff_ratio` / `expectancy`). This is **display-only context, not a sizing input** — the live sizer remains the win-rate ladder (Step 5); the C3 fractional-Kelly sizer stays ADVISORY until tier×expectancy is monotone on n≥30. Its purpose is to keep the desk honest about *where the book's edge actually lives*: a high hit-rate with a sub-1 payoff loses money, and a coin-flip with a 1.5 payoff makes it. Label it `[advisory — expectancy is not yet a live sizing axis]`.

Embed the conviction-scoring rubric (Step 4) verbatim at the bottom of §7 so future readers can audit the scores.

## 8. Watch-only — single signal, no confluence
Candidates that surfaced from one agent but failed the confluence gate. Listed for journaling, NOT for trade entry today.
```

---

## Step 8 — Confirm watchlist write-back (handled by risk-monitor in Step 2d)

The top-5 watchlist write-back is performed inside `risk-monitor` during Step 2d — the agent calls `uw watchlist manage --action add --group conviction_<YYYY-MM-DD> --tickers <top_5_by_score>` with today's top 5 by conviction score (excluding any VETO'd name). **Do not double-write here.**

Confirm the write-back happened by checking the `risk-monitor` output for the explicit `watchlist_write_back_confirmation` field. If missing, call `uw watchlist manage --action add --group conviction_<YYYY-MM-DD> --tickers <top_5_by_score>` directly as a fallback.

If any name was already on a manually-curated group, leave that membership alone — write only to the date-stamped group. This closes the feedback loop: today's high-conviction names become tomorrow's correlation universe, and tomorrow's RM automatically pulls `uw watchlist alerts` against them to flag adverse-flow exit candidates.

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
   - Top level: `{schema_version: "1.3", rubric_version: "2026-06-12", report_date, report_kind: "daily", regime, vrp_classification, macro_snapshot_signals (the fred_macro signals object), macro_event_risk (the event_risk calendar), watchlist_write_back (the persisted top-5), next_session_gex, next_session_0dte_setup, breadth_cross_check, report_path}`. (`1.3` adds the `rubric_version` era stamp, 2026-06-12 audit P0.1 — update the literal only when the frozen rubric is formally re-versioned; `1.2` added the advisory per-call `distribution_flag`; older envelopes remain valid.)
   - `breadth_cross_check` (advisory, 2026-05-27 `fz`-edge A2): the Step-0 `fz breadth` block — `{advisory: true, source: "finviz", advancers, decliners, pct_green, divergence_flag (true when the index is green but pct_green < 50), note}`. Emit `null` when `fz_available == false`. Like the other advisory blocks it is top-level, **not** in `calls[]`, and contributes 0 points.
   - `next_session_gex` (schema_version 1.1): the **advisory** §2 GEX-map block — `{advisory: true, as_of_eod_date: <report_date>, next_session_date, indices: [{symbol, spot, zero_gamma_level, zgl_reliable, regime, total_gex, call_wall, put_wall, read, structure_bias, caveats}]}` for **SPY and QQQ only**.
   - `next_session_0dte_setup` (schema_version 1.1): the **advisory** §2a premium-selling block, copied from Step 0 `zerodte_setup` — `{advisory: true, as_of_eod_date: <report_date>, backtest_verdict, indices: [{symbol, sell_premium, vol_state, vix, implied_move_pct, expected_range_pct, size_scalar, suggested_structure, entry_rule, stand_aside_reason, caution}]}` for **SPY and QQQ only**. Emit `null` if `zerodte_setup.available == false`.
   - **Both** advisory blocks are deliberately top-level fields, **not** members of `calls[]` — §2/§2a are prose-only and must contribute 0 points to any `raw_score`. **Do not** add a `horizon: "0DTE"` entry to `calls[]` for this content.
   - `calls[]`: one object per HIGH/MEDIUM/LOW call (and watch-only / VETO'd names) carrying the quant's audit fields verbatim — `ticker, horizon, section, direction, tier, raw_score, score_components[], dominant_signal_class, confluence_score, cum_premium_flow_30d/90d, win_rate, win_rate_uncapped, win_rate_n, win_rate_source, market_excess, pre_risk_size, final_size, gate_verdicts, fundamentals_verdict, debate_residual_confidence (the bull residual), debate_residuals ({bull, bear}), implied_move, dp_block_to_float_ratio, insider_cluster_flag, structure, entry_or_trigger, invalidation, key_risks[], thesis`. **2026-07-25 audit P1 #5 — the last three are the instrumentation trio and this enumeration is why they went missing.** They shipped into the schema on 2026-06-20 (register C43) and into the quant's output contract on 2026-07-04, but were never added to *this* list, so envelopes from 2026-07-20 onward dropped them entirely and **C16 (float-normalized DP block) and C18 (insider-cluster conjunction) have now been untestable for three consecutive audits.** They are **mandatory-when-source-present, explicit-`null` otherwise** — never simply absent: `implied_move` on every vol row (`vol_long`/`vol_short`/`earnings_vol`/`high_iv_rank`, from the scout's front-expiry expected move; without it the audit can only resolve vol on the RV-direction proxy), `dp_block_to_float_ratio` on every `dark_pool_accumulation` row (accumulation-hunter's largest institutional-tier block ÷ `fz` float; `null` when `fz` float is unavailable — never block on it), `insider_cluster_flag` carried verbatim from accumulation-hunter's `insider_cluster_present` (`null` only when the `fz` lane was skipped, `false` when checked-and-absent). All three are advisory, **0 rubric points**, and never `score_components` lines — they exist so the *next* audit can grade gates this one could not. **2026-06-12 P1.1 (schema 1.3):** `gate_verdicts` carries **all 9 keys** (`regime, vrp, panic, cluster, sector, fundamentals, event_risk, debate, rubric_regime`) on every non-DROP call — the validator rejects a 1.3 envelope missing any (the `debate` key had silently been absent on 0/151 prior calls because the schema rejected it; root cause fixed). `market_excess` surfaces the C2 result per call (negative = beta, not edge). `debate_residuals` carries both sides so the debate gate's discrimination is measurable; `debate_residual_confidence` stays as the bull-residual scalar for backward compatibility. For any top-5 name carry the fundamentals-gate's `fz_context` block (short-interest / float / squeeze / analyst — advisory, 0 points); omit or set `{available:false}` otherwise. For any **long** name that the accumulation-hunter flagged with bullish-side OI being closed, carry its `distribution_flag` block (`{present, closing_side, closing_premium, oi_decrease, note}` — advisory, 0 points, 0 tier impact, C28); omit or set `{present:false}` otherwise. It is **not** a `score_components` line — it lives only on the call object so the Σ-invariant is untouched.
   - **Invariant:** `Σ score_components[].points == raw_score` for every call (the quant already guarantees this — the validator enforces it).
   - **Author from the schema, not this prose.** Every object in `schemas/decision_envelope.schema.json` is `additionalProperties: false` with explicit `required` lists and enums — read the `$defs` (`call`, `fz_context`, `distribution_flag`, `next_session_gex`, `next_session_0dte_setup`) for the exact allowed keys, and copy the shape of the most recent valid envelope. The field lists above are a guide, **not** the contract: do **not** add keys the schema doesn't define (seen in practice: `audit_trail` on a call, `pnl_basis`/`mean_pnl_open_pct` on `next_session_0dte_setup`, `analyst_target`/`close`/`beta` on `fz_context`, a top-level `backtest_verdict` on `next_session_gex`), and keep prose out of typed/enum fields — `regime` is the enum `[POSITIVE, NEGATIVE, FULLY_NEGATIVE, FULLY_POSITIVE]` (descriptive text goes in `read`), `watchlist_write_back` is an array of ticker strings, and GEX/0DTE backtest detail folds into the `read` / `suggested_structure` prose. `fz_context` requires `available`.
3. **Validate it:** run `python3 scripts/validate_decision.py --file analyses/daily/YYYY-MM-DD/decision.json` via Bash. If it exits non-zero, fix the envelope (not the validator) until it passes — a malformed envelope silently degrades the calibration loop. Set the envelope's `report_path` to `analyses/daily/YYYY-MM-DD/report.md`.
4. Confirm both files were written (the Write tool errors loudly on failure — no need to re-Read).
5. Print the **Executive Summary** section to chat. Nothing else — the user opens the file for the rest.

---

## Failure modes & recovery

- **Phase 1 agent times out** — re-spawn just that agent with the same context block. If it fails twice, write its section as `[agent timed out — see <agent-name> logs]` and proceed; do not let one agent block the report.
- **`uw playbook daily-synthesis` returns empty** — fall back to manually composing the macro context from `uw risk market-regime` + `uw insights signal-confluence` + `uw watchlist alerts` and continue.
- **`uw historical available-dates` shows stale data** — abort and ask the user to re-export from Unusual Whales. Do not proceed with stale data.
- **No tickers clear the confluence gate** — produce a report whose §3 and §4 are explicitly empty, with the §1 regime + §2 next-session GEX advisory still populated. A "no edge" day is a valid output, not a failure.

---

## Single-Leg Whale Signal (Phase 1 advisory — permanently 0 points; C19 CLOSED 2026-07-25)

After **Step 0** establishes the directional regime, run the single-leg whale
tier scan once on the session tape (post-close):

```
uw options-flow single-leg --regime <step0_regime> --json --quiet
```

This grades clean single-leg, ask-side, ≥$500K, common-stock opening prints by
the empirically-backtested **Signal Quality Hierarchy** (see
`analyses/audit/2026-05-29/single_leg_whale_implementation_plan.md`):

| Tier | Label | Setup | Backtest | Action |
|---|---|---|---|---|
| 1 | `OPENING_PUT_PRIME` | put, size/OI≥2, DTE≤30 | WR 63.5%, +26pp, p<0.001 (n=266) | `CONTRARIAN_SHORT` |
| 1 | `FLOOR_PUT_BLOCK` | put, slft/slcn, DTE≤30 | WR 61.0%, +23.5pp, p<0.001 (n=328) | `CONTRARIAN_SHORT` |
| 2 | `OPENING_PUT_STRONG` | put, size/OI≥2, DTE>30 | edge decays | context only |
| 3 | `CALL_BETA_NOEDGE` / `CALL_UNVALIDATED` | any call | −9.7pp in bull; unmeasured else | context only |
| 4 | `CLOSING_ANTISIGNAL` (size/OI<0.5) / `CALL_BETA_FADE_CHASE` | closing / bull call-chase | 43.7% / −9.7pp | **AVOID / FADE** |

**Routing:**
- **`accumulation-hunter`** — a Tier-1 opening/floor PUT on a name also showing
  dark-pool distribution (`dark_pool_block_stratified`) is the strongest bearish
  co-confirmation; surface as a bearish co-flag.
- **`contrarian-scanner`** — Tier-1 short-DTE puts feed single-name short theses
  alongside a crowding put/call read.
- **`risk-monitor` / debate** — `CALL_BETA_FADE_CHASE` is a **veto** on bullish
  conviction resting on "big call flow"; `CLOSING_ANTISIGNAL` weakens a
  same-direction thesis.

**Grading:** advisory, **0 conviction-rubric points — permanently.** Neither the put
tier nor the call tier is ever auto-scored from this signal.

**2026-07-25 audit — C19 CLOSED as REFUTED (register C53). There is no accrual to run.**
The promotion criterion is retired, not merely blocked. Six audits carried
"`bearish_flow` shows positive excess but scores 0" as evidence of an unscoreable
down-tape edge; Phase 3d showed **71.1% of the excess column's variance is the
benchmark**, not the book. On the cross-regime dataset (159 up-tape / 281 down-tape
decided) `bearish_flow` books **0.533 up-tape / 0.526 down-tape** — stationary — and
realises **0.49 against a 0.48 claim on n=94 (p=0.96)**, the best-calibrated large class
in the book; its down-tape paired McNemar is **ns (p=0.2478)**. The 2026-07-11 "+29.4pp"
headline and the 2026-07-18 "sign reversed" headline were the same rows under a moved
denominator (SPY-short path base 0.176 vs 0.588).
- **What this does NOT refute:** the 2026-05-29 Tier-1 PUT backtest in the table above
  (WR 63.5%, n=266, p<0.001). That was a **different measurement on a different
  substrate** — raw single-print Parquet rows graded next-session, not scored fleet
  calls graded on a path-aware 0.5-ATR window. Keep running the scan; keep using the
  tier labels as routing context. Only the *graduation claim* is dead.
- **Do not re-open C19** under its old ≥58% / ≥60-day / ≥2-regime wording, and do not
  report a "June cohort 0.632 (n=19)" or any rolling-WR figure as accrual progress. A
  scored bearish line now requires a **new** C-numbered pre-registration naming its own
  substrate and its own cross-regime ∧ n≥30-per-arm ∧ BH-surviving bar.
- **Short-sale-constraint conditioning (advisory):** weight a Tier-1 put co-flag
  higher when the name shows borrow constraint — `fz` `short_ratio` (days-to-cover)
  / `short_float` from the fundamentals-gate `fz_context`. Rationale: the published
  channel for bearish-option informativeness is short-sale cost (Johnson & So 2012;
  Ofek-Richardson-Whitelaw 2004) — the put edge should concentrate in
  harder-to-short names. Advisory color only — permanently (C19 closed).
- **Regime-tag the call-side read:** `CALL_BETA_NOEDGE` (−9.7pp) was measured in a
  bull window, and the best signed-flow study found opening *call* buys the most
  informative leg (Ge-Lin-Pearson 2016) — treat "calls are beta" as
  **bull-regime-conditional, not structural**. In non-bull regimes report the call
  tier as `CALL_UNVALIDATED` rather than fading it by default.
