---
description: Run the full Friday-evening or Sunday-prep weekly intelligence note in the voice of a top-tier institutional desk strategist (JPM/GS Friday note). Persistence-weighted conviction rubric over a 5-day window with WoW regime delta, intra-week thesis scorecard (WIN/LOSS/INCONCLUSIVE per ticker), sector rotation persistence, vol-surface evolution, LEAP roll detection, OPEX-week pin map, and 2-week earnings lookahead. Output is tiered High/Medium/Low conviction with backtest-weighted sizing. Invoke whenever the user asks for a weekly recap, week-ahead prep, Sunday strategy session, weekly market intelligence note, or types `/weekly-analysis`. Do NOT trigger for single-day reports (use `/daily-analysis`), single-ticker analyses (use `uw insights deep-dive`), or month/quarter horizons.
---

# Weekly Market Intelligence

Run a full weekly intelligence note in the voice of a top-tier institutional desk strategist. Uses the same agent fleet as `/daily-analysis` but wired to week-range inputs and a persistence-weighted conviction rubric. **All data is pulled fresh via the `uw` CLI — no dependency on prior daily analysis files.** Phase 1 spawns **11 agents** (12 in OPEX week) in parallel against a shared week-baseline context (including a FRED macro snapshot + forward event-risk calendar). Phase 2 runs `signal-confluence-quant` for audited scoring, then a `fundamentals-gate` cross-check and a bounded `bull-researcher`/`bear-researcher` debate on the top-5, then `risk-monitor` for gating, against the union of the week's candidates. Score conviction formally with explicit tiers, backtest and fundamentally vet top names, write winners back to the watchlist, emit a machine-readable `decision.json` envelope, and save the report to its own folder `analyses/weekly/YYYY-WW/` holding `report.md` + `decision.json`.

## Data access — the `uw` CLI

All Unusual Whales data comes from the **`uw` CLI** (`/Users/ewan/.local/bin/uw`; override with `$UW_PP_CLI`), invoked via Bash. Canonical convention for **every** call in this command and **every spawned agent**:

```
uw <group> <subcommand> [--flag value …] --json --quiet
```

- `--json` is **mandatory** (the CLI defaults to a rendered table); `--quiet` drops banners so stdout is pure JSON. Parse with `jq` / `json.loads`.
- Pin point-in-time tools to a covered date with `--date <YYYY-MM-DD>`; multi-day tools take `--days` / `--lookback-days` over the week range.
- For tie-prone lists (`sector-flow-persistence`, any `--top-n` with score ties) **sort by an explicit key** — Go map order is non-deterministic.
- Trim large payloads with `--select <dotted,paths>` / `--compact` to save tokens.
- Fundamentals enrichment still uses the **yfinance MCP** (`mcp__yahoo-finance__*`) and `scripts/finnhub_enrich.py` — unaffected by this CLI path.
- **Non-flow context** (short interest, days-to-cover, float, analyst consensus, breadth, insider clusters) comes from the **`fz` CLI** (`finviz-pp-cli`), invoked via Bash as `fz <group> … --agent`, and `scripts/fz_enrich.py`. It augments **beside** the flow engine — adds **zero** options flow / greeks / dark pool / GEX / OI, replaces no `uw` tool. Every `fz` lane is **advisory (0 rubric points)** and **graceful-skip**: if `fz` is unavailable the note completes unchanged. See `analyses/audit/2026-05-27-fz-edge/`.

## When to invoke

- "Weekly recap", "week in review", "weekly intelligence note"
- "Sunday prep", "week-ahead prep", "what should I watch next week"
- Friday-evening review of the trading week
- Slash command `/weekly-analysis`

## When NOT to invoke

- "Wrap up today" / "EOD report" → `/daily-analysis`.
- "What's NVDA doing this week?" → `uw insights deep-dive` + `uw historical trend` for that one ticker.
- Month-over-month or quarterly horizons — call `uw historical cumulative-premium-flow` with `--days 30` (or 90) and let the user drive the synthesis manually.

## Model routing

The orchestrator running this skill must use **`opus` with extended thinking on**. It performs the cross-agent synthesis, conviction rubric application, and report writing — tasks that degrade materially on a smaller model. Sub-agents are cheaper and have narrower mandates; assign models as follows when spawning each agent:

| Agent | Model | Thinking | Why |
|---|---|---|---|
| gamma-flip-tracker | sonnet | off | Next-session GEX advisory for SPY/QQQ only (ZGL, regime, call/put walls); prose-only, 0 rubric points, no backtested edge |
| dealer-positioning-strategist | sonnet | **on** | Multi-signal synthesis: DEX trajectory + vanna squeeze + GEX time series across the week — reasoning depth required |
| sweep-tracker | sonnet | off | Filter and rank by `uw hot-chains sweep-persistence` count — no synthesis |
| accumulation-hunter | sonnet | off | Pattern match across DP + OI over 5d/10d, with `uw dark-pool block-stratified` gate |
| contrarian-scanner | sonnet | off | Trajectory computation — rising vs falling `uw historical pc-ratio-zscore`, VRP gate |
| earnings-scout | sonnet | **on** | Dual mandate: judgment-heavy recap grading + multi-signal lookahead ranking with term-skew |
| vol-surface-scout | sonnet | off | Analytical WoW delta — systematic flagging, `uw historical iv-percentile-zscore` + VRP bias |
| multileg-strategist | sonnet | **on** | Hardest Phase 1 task: inferring institutional intent from repeated cross-week structures + term-structure context |
| leap-positioning-radar | sonnet | **on** | Multi-signal synthesis over 10d+ window + rolling detector + uw historical cumulative-premium-flow accretion classification |
| sector-rotation-strategist | sonnet | off | Persistence-gated rotation calls + leader extraction; mostly mechanical |
| opex-pin-strategist (conditional) | sonnet | off | OPEX-week only; ranking + structure suggestion is rule-based |
| signal-confluence-quant (Phase 2a) | sonnet | **on** | Audited per-ticker scoring with explicit component breakdown — reasoning required for tie-breaking and audit-trail prose |
| fundamentals-gate (Phase 2b) | sonnet | off | Mechanical cross-check: runs `finnhub_enrich.py` on top-5, maps assessment vs thesis direction to CONFIRM/CAUTION/VETO |
| bull-researcher (Phase 2c) | sonnet | **on** | Adversarial steelman of the long case — reasoning + honest residual confidence |
| bear-researcher (Phase 2c) | sonnet | **on** | Adversarial steelman of the bear case — the disconfirmation the additive score lacks |
| risk-monitor (Phase 2d) | sonnet | off | Systematic: correlation matrix + cluster flagging + full gate stack (incl. fundamentals / event-risk / debate) |

Pass the model assignment in each agent's prompt header (e.g. `Model: claude-sonnet-4-6, extended_thinking: false`).

## Operating principle: persistence beats a single print

Single-day signals are noise; multi-week persistence is the edge. Every agent in this run must consume week-range data wherever the CLI supports it. Specifically:

- `uw hot-chains sweep-persistence` over `uw options-flow sweeps`
- `uw historical oi-trend` with `--days 5` over `uw oi biggest-increases`
- `uw historical cumulative-premium-flow` over single-day premium totals
- `uw historical pc-ratio-zscore` over the deprecated `uw screener put-call-extremes`
- `uw historical iv-percentile-zscore` over raw IV rank for outlier robustness
- `uw historical gex-time-series` over single-day GEX snapshots
- `uw options-flow sector-flow-persistence` over single-day `uw options-flow sector-flow`
- `uw historical signal-backtest` is **quant-only and quarantined** (2026-06-12 P0.3): only `signal-confluence-quant` calls it, only under the clean-query protocol (pinned `--top-n 200`, complete-window post-filter — see its "Signal-backtest substrate quarantine"). Phase 1 agents must NOT call it; its raw headline is never quoted

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

   These four variables — `ISO_WEEK`, `MONDAY`, `WEEK_END`, `TODAY` — are the canonical anchors for this run. The run folder is `analyses/weekly/$ISO_WEEK/` (holding `report.md` + `decision.json`) and the watchlist group key is `conviction_week_$ISO_WEEK`.

1b. **`fz` health probe (2026-05-27 `fz`-edge Phase 0).** Run `fz --version` (and optionally `fz doctor --agent`). If non-zero / binary missing, set `fz_available=false` and **graceful-skip every `fz` lane** (breadth cross-check, squeeze/RS funnel, fundamentals-gate `fz_enrich`, accumulation insider-cluster co-flag, debate analyst context) — like the yahoo-broken / Finnhub-403 skip pattern. **Never hard-fail the note on `fz`.** All `fz` lanes are **advisory (0 rubric points)**.

2. **Coverage list** — call `uw historical available-dates` and filter to dates in `[MONDAY, WEEK_END]`. Call this filtered list `covered_dates`. **Rules:**
   - If `covered_dates` is empty → abort and report "No UW data available for the current trading week."
   - If any calendar weekday Mon–Fri is missing from `covered_dates`, note the gap explicitly — agents must not assume a full 5-day window. Pass `covered_dates` (not the computed calendar range) as the authoritative list to every Phase 1 agent.

3. **Regime baseline** — call `uw risk market-regime` twice: once for `TODAY` and once for `covered_dates[0]`. Compute the WoW regime delta. This **week regime baseline** — regime today vs week-open, and whether it improved / deteriorated / held — is passed to every Phase 1 agent. Agents must gate their directional calls against it.

   **Breadth cross-check (`fz`, advisory — 2026-05-27 `fz`-edge A2; skip if `fz_available=false`):** `fz breadth --group sector --agent` (optionally `--days 5` for a week trend) returns `{advancers, decliners, pct_green, …}` from a different data lineage than `uw risk market-regime`. Capture as `breadth_cross_check`; flag a breadth divergence (green tape with `pct_green < 50`) in §7 prose. Advisory — does not override the `uw` regime, 0 points.

4. **Vol regime** — call `uw historical vrp` for the most recent date in `covered_dates`. Classify the week as a premium-selling environment (VRP positive) or premium-buying environment (VRP negative). This shapes which agents you trust most: VRP-positive weeks favour vol-surface-scout & contrarian-scanner; VRP-negative weeks favour gamma-flip-tracker & earnings-scout.

5. **Sector & flow-share baseline** — call in parallel:
   - `uw options-flow sector-flow-persistence` over the full week range. This is the durability check that gates §2 of the report (sector rotation narrative).
   - `uw options-flow sector-flow` for `WEEK_END` — single-day snapshot for week-end skew within the persistence narrative.
   - `uw options-flow dte-volume-share` for each covered date (or `WEEK_END` only if a faster pass is needed) — institutional vs retail share trend across the week. Feeds §1.

   These are **GICS-aggregate** (no symbol input) — the shared anchor. The **ETF instrument-level flow tape** (the canonical ETF universe defined in `sector-rotation-strategist.md`) is swept **per-symbol by the agent in Step 1**, not here — do **not** add the ~21 per-symbol ETF calls to preflight. The agent owns the ranked deep-pull; Step 0 stays GICS-aggregate.

6. **Top-of-funnel screens** — run in parallel for `WEEK_END`:
   - `uw screener bullish-bearish` (top 25 each side) — week-end leaderboard.
   - `uw insights signal-confluence` (`min_score=4`, top 25 each direction) — multi-factor scoring at higher threshold than daily.
   - `uw screener iv-rank` (top 25 high, top 25 low) — premium-selling vs premium-buying candidates for next week.
   - `uw screener earnings-catalyst` — upcoming earnings + elevated IV (next 14 days) — feeds §6.
   - `uw screener volume-vs-average` (top 25, `--min-volume-ratio 3`) — flow anomalies vs 30-day baseline; cross-reference against multi-day persistence for §3.
   - `uw hot-chains sweep-ratio` — high sweep-to-volume contracts at week-end; cross-reference against `uw hot-chains sweep-persistence` in sweep-tracker.
   - **`fz` squeeze + RS lanes (advisory — 2026-05-27 `fz`-edge A4; skip if `fz_available=false`):** orthogonal, non-flow entry axes the flow funnel misses. **Squeeze:** `fz screen --filter sh_short_o20,sh_price_o5,sh_avgvol_o500 --view ownership --agent` (short float > 20%, returns `{Ticker, Short Float, Short Ratio, Float, Price, …}`). **RS / breakout:** `fz screen --signal ta_newhigh --filter sh_price_o5,sh_avgvol_o500 --agent`. Tag rows `source: fz_squeeze` / `source: fz_rs`, **union into the candidate set fed to Phase-1 agents** (they still need ≥2-agent confluence to enter the rubric). The C12 floor below still applies to every unioned name.

   **Liquidity floor (2026-05-25 register C12) — apply to every screened name before handing to agents.** Each candidate must clear **price ≥ $5 AND 20-day dollar-ADV ≥ $50M** (or notional-equivalent). Use the screener `close` for price and a 20-day dollar-volume estimate (equity `volume × close`, or yahoo `get_historical_stock_prices` for the underlying; "notional-equivalent" = options dollar volume where equity ADV is unavailable). **Fail closed:** a name whose liquidity cannot be verified is dropped, not passed. ADV is **dollar** volume (shares × close), *not* a raw share count. Drop sub-floor names from the funnel entirely — they pollute the candidate set, the confluence breadth, and the win-rate denominator. **This floored set is the funnel every downstream step consumes** — all Phase 1 agents (Step 1) and the quant's win-rate denominator (Step 5) operate on the floored names, never the raw screener output. Rationale: the `volume_spike` screen returns micro-ETFs (GIF/BLCN/PEX/IGLD/UTHY/ESGE — all sub-$50M ADV) the desk cannot fill at size; Barbon & Buraschi show flow effects are strongest (and least exitable) in exactly these illiquid names. The reusable filter is `scripts/excess_winrate.py:apply_liquidity_floor`.

7. **OPEX guard** — if `WEEK_END` is within 7 calendar days of the third Friday, also call `uw oi pin-risk` for SPY/QQQ/IWM and the top 10 from step 6, plus `uw oi opex-concentration` for the same set. Pinning candidates feed §9 (Setups for Next Week).

8. **Macro & event-risk layer** — `uw risk market-regime` gives a label, not a calendar; a week-ahead book needs to know which prints land next week. Build it once here:
   - **Macro snapshot** — run `python3 scripts/fred_macro.py` via Bash → `macro_snapshot` JSON (yield-curve sign, core CPI/PCE YoY, unemployment + payrolls, 10Y level/direction, USD direction, fed funds). If `available:false`, note the skip and fall back to the regime label.
   - **Forward catalyst calendar** — build `event_risk`: Tier-1 US macro releases over the **next two calendar weeks** (CPI, PPI, PCE, FOMC/SEP, NFP/jobless claims) confirmed via `WebSearch`, each tagged `{event, date, impact}`. Per-name earnings dates are added in Phase 2 from the fundamentals enrichment and cross-referenced against the §6 lookahead.

9. **§2 GEX-advisory rolling backtest** — the §2 / §9 next-session GEX map for SPY/QQQ is shipped as an *advisory* in `/daily-analysis` with **no** predictive claim; this is where that claim is tested. Run `python3 scripts/gex_next_session_backtest.py --symbols SPY,QQQ --days 60 --json` via Bash and capture it as `gex_advisory_backtest`. It reconstructs the trailing EOD GEX book (via the `uw` CLI) and reports, vs a 50% baseline: **H1** spot-vs-ZGL → next-session realised vol (theory: short-gamma > long-gamma) and **H2** whether the next close lands *closer* to the nearest EOD wall (walls-as-magnet), with `n`, binomial `p`, and a coarse `verdict` (`GO_WALLS_PREDICTIVE` / `NO_GO_NO_EDGE` / `INSUFFICIENT_SAMPLE`). If it returns `available:false` (CLI/data unavailable), note the skip and continue. **As of the last gate run the verdict was `NO_GO_NO_EDGE`** (walls were not magnets — next close moved *away* more than chance; H1 ran backwards) — so the GEX walls are dealer context only, never a backtested edge.

   Then run `python3 scripts/zerodte_setup.py --symbols SPY,QQQ --days 60 --json` and capture it as `zerodte_setup` — the **validated** 0DTE stack (delta-neutral premium-selling): rolling `backtest` (front-IV implied move vs realized open-to-close, open-entry vs overnight, GEX→range vol-suppression, VIX-level conditioning, `verdict` ∈ {`GO_PREMIUM_SELL_INTRADAY`/`NO_GO_NO_EDGE`/`INSUFFICIENT_SAMPLE`}) plus a per-index `setup`. This is the part that *did* validate (unlike the GEX walls) — but it is still **advisory, 0 rubric points, and NOT a guaranteed edge** (no vol shock in sample → tail unsampled). `available:false` → note the skip.

10. **Compose the week-baseline context block** — this compact JSON-shaped block is passed verbatim to every Phase 1 agent: `{iso_week, monday, week_end, today, covered_dates, fz_available, regime_today, regime_monday, regime_delta, vrp_classification, sector_persistence, top_bullish, top_bearish, confluence, iv_extremes, breadth_cross_check, fz_squeeze_candidates, fz_rs_candidates, earnings_lookahead, opex_pin_candidates, macro_snapshot, event_risk, gex_advisory_backtest, zerodte_setup}`. The `fz_*` fields are advisory (0 rubric points) and absent/empty when `fz_available=false`.

---

## Step 1 — Phase 1: alpha-finding agents (parallel, single batch)

Spawn these **11 agents simultaneously** — a single message with 11 Agent tool calls (12 in OPEX week — see opex-pin-strategist). Hand each one: (a) the week-baseline context block from Step 0, (b) the count of covered days (so agents know whether they have a full 5-day window or a shorter one), and (c) the explicit tool list below. Each agent must restrict queries to `covered_dates` and favour multi-day tools over single-day equivalents.

**Hard rule:** no agent re-fetches `uw risk market-regime`, `uw historical vrp`, or `uw options-structure front-end-iv-ratio` — those come from Step 0 context only.

### gamma-flip-tracker — next-session GEX advisory, SPY/QQQ only (sonnet, thinking off)
Do **NOT** produce intraday 0DTE calls. Forecast next session's / next week's zero-gamma level, regime, and call/put walls for **SPY and QQQ only** (drop IWM and single names), read off the standing EOD 0–45d GEX book (OI persists overnight). This is the §9 **advisory** — prose-only, **0 conviction-rubric points**, and **no backtested predictive claim** (its predictive value is tested by the Step 0 `gex_advisory_backtest`; present accordingly). **Swing-horizon DEX/vanna/charm/GEX-trajectory work is owned by `dealer-positioning-strategist` (next agent below) — do not duplicate.**

Tools required:
- `uw options-structure gex` (default `dte_max=45`) — **PRIMARY**: per-strike GEX, `zero_gamma_level`, `regime`, `total_gex`, call wall (largest +GEX strike above spot), put wall (most −GEX strike below). Do **not** lead with `uw options-structure today-gamma-flip` (it locks to the snapshot's expired same-day expiry with an unreliable ZGL).
- `uw historical gex-time-series` — `regime_flip_dates` + multi-day ZGL trajectory across `covered_dates`: regime fresh vs held.
- `uw options-flow expiry-heatmap` — confirm near-dated expiries hold meaningful volume share.
- `uw options-flow greek-screener` — `min_gamma` filter for the highest-impact near-dated contracts.

ZGL rule: trust `zero_gamma_level` only within ~5% of spot; when null/extrapolated, fall back to `total_gex` sign + spot-vs-wall and set `zgl_reliable=false`.

Output: §9 next-session regime + ZGL + call/put wall for SPY and QQQ, with a one-line structure bias and the mandatory caveats (EOD = prior refreshed after the open; gap risk; ETF-not-index book; uw-pp cannot isolate the D+1 expiry).

### dealer-positioning-strategist — swing-horizon dealer flows (sonnet, thinking **on**) (NEW)
Owns the multi-day DEX / vanna / charm / GEX-trajectory work. Surfaces 1–4 week swing setups GF cannot see at the 0DTE horizon.

Tools required:
- `uw options-structure dex` — DEX trajectory week-over-week via dated calls (the "flips precede price" framing is practitioner hypothesis, not validated evidence — 2026-06-12 P0.4; only the MECHANIZED sign-change trigger in `dealer-positioning-strategist.md` feeds the scored line).
- `uw options-structure vanna-charm` — vanna-squeeze detection (put-heavy book + falling VIX → BUY setup).
- `uw historical gex-time-series` (`--days 10`, also 30d) — multi-day ZGL trajectory; flag any regime flip across the week.
- `uw options-structure gex` (default `dte_max=45`) — confirm DEX flip is not a single-strike artifact.
- `uw options-structure front-end-iv-ratio` — secondary panic gate; consume from Step 0 if available.

Output: per-ticker swing dealer reads — DEX state + 5d/10d trajectory, vanna-squeeze flags, ZGL trajectory week-over-week, regime-flip detections, swing bias for next 1–4 weeks. Feeds §3 (Swing Book) with the `vanna_squeeze` / `dex_flip_long` / `dex_flip_short` signal classes.

### sector-rotation-strategist — durable rotation calls + named single-name leaders (sonnet, thinking off) (NEW)
Owns multi-week sector rotation + leader extraction. Enforces ≥3-day persistence — primary feed for §2 of the report.

Tools required (GICS layer — the shared anchor, cross-checks the ETF tape):
- `uw options-flow sector-flow-persistence` — multi-day rotation persistence per sector across `covered_dates` (PRIMARY).
- `uw options-flow sector-flow` for `WEEK_END` — single-day skew within the persistence narrative.
- `uw screener bullish-bearish` — filter by sector to extract single-name leaders.
- `uw options-flow dte-volume-share` per covered date — institutional vs retail DTE share trend. **MARKET-level only (`{symbol: MARKET}`), NOT per-sector (2026-06-12 P1.5)** — a market-wide regime overlay across the week (rising monthly+ = institutional tape; rising 0DTE = retail tape, downgrade rotation conviction uniformly), not a per-sector split.

ETF instrument-level flow tape (per-symbol — GICS tools cannot see ETFs, especially thematics/geographics). Run the **same canonical ETF universe** constant in `sector-rotation-strategist.md` with **identical agreement logic** to the daily, **cap ≤ 40 added `uw` calls**:
- **RANK (≤21):** `uw historical cumulative-premium-flow` (`--symbol <ETF> --days 5`, extend to the covered-week range) for every universe ETF — rank by net-premium direction × multi-day persistence. Weight ETF **options** flow above ETF DP. Graceful-skip thin names.
- **DEEP-PULL top 3 inflow + 3 outflow only (≤12):** `uw dark-pool largest` (`--symbol`, positioning/persistence tell — **not** single-name accumulation) + `uw options-flow sweeps` (`--symbol`, directional urgency).
- **CROSS-CONFIRM:** GICS sector + its representative ETF agree w/ persistence → high-conviction; disagree → watch-only. No-GICS thematics → instrument-only (`gics_agreement: n/a`).

Output: rotation regime call (defensive→cyclical / cyclical→defensive / growth→value / value→growth / no_change), per-sector persistence scores, named single-name leaders, `etf_flow_tape[]` (ranked inflow/outflow ETFs + GICS-agreement + leaders), swing-book implication. Feeds §2 (Sector Rotation) directly. The ETF tape is **advisory** — it strengthens the existing conditional sector-leader +1 via `gics_agreement`/cum_flow alignment, adds **no new rubric points**.

### opex-pin-strategist — CONDITIONAL: only spawn within 7 days of monthly third-Friday (sonnet, thinking off) (NEW)
**Conditional spawn.** If `WEEK_END` is within 7 calendar days of the monthly third-Friday OPEX, include this agent (12 agents total). Otherwise omit.

Tools required:
- `uw oi pin-risk` — pin candidates with strike + `pin_score` (the tool's composite; **there is NO `probability` field** — 2026-06-12 P1.5).
- `uw oi opex-concentration` — OI mass at OPEX strikes.
- `uw options-structure gex` — confirm pin strike sits near a long-gamma wall.

Output: ranked OPEX book — top 5–10 names with `{ticker, pin_strike, distance_pct, oi_mass_at_pin, gex_at_pin, ranked_score, suggested_structure}`. Feeds §9 (Setups for Next Week) when the upcoming week is OPEX week.

### sweep-tracker — multi-day persistence (sonnet, thinking off)
Use `uw hot-chains sweep-persistence` as the **primary** signal. Surface tickers swept on **≥3 of 5** trading days this week.

Tools required:
- `uw hot-chains sweep-persistence` (primary).
- `uw hot-chains smart-money-flow` — ask vs bid colour for each persistence-flagged ticker.
- `uw options-flow sweeps` — supplementary (week-end snapshot only).
- `uw options-flow top-premium-trades` (top 30, week range) — whale-ticket validation.
- `uw hot-chains most-active` — per-ticker contract-level conviction.

Single-day sweeps alone are insufficient for a weekly recommendation. Rank candidates by persistence count first.

### accumulation-hunter — expanded window (sonnet, thinking off)
Run with a 5-day window (and a 10-day secondary pass).

Tools required:
- `uw insights institutional-accumulation` (a 5-day window and a 10-day window).
- `uw dark-pool ticker-summary` (top 30 by premium across each covered date — aggregated).
- `uw dark-pool largest` (top 30 across the full week range).
- `uw dark-pool block-stratified` — institutional vs retail tier filtering.
- `uw dark-pool price-levels` — institutional support/resistance built up across the week.
- `uw dark-pool extended-hours` — overnight/pre-market block activity.
- `uw oi smart-positioning` — OI bullish/bearish inference.
- `uw historical oi-trend` (`--days 5`) — multi-day OI build verification (BUILDING required for full points).
- `uw oi decrease-with-volume` (`--min-volume 500`) — **distribution counter-signal (C28)**: bullish-side OI closed on high volume across the week on a long-thesis name = accumulation-as-distribution. Advisory, 0 points; emits `distribution_flag` (persistence makes the weekly read stronger than a single-day daily flag).

Output: tickers with quiet multi-day OI build sustained across the full week with both DP and OI confirmation, each with an advisory `distribution_flag` (C28).

### contrarian-scanner — pc_ratio trajectory (sonnet, thinking off)
Tools required:
- `uw historical pc-ratio-zscore` — compute the trajectory of uw historical pc-ratio-zscore across `covered_dates`. This is the primary signal. **Do NOT use the deprecated `uw screener put-call-extremes`.**
- `uw insights price-vs-flow` (week-range) — when smart money disagrees with price.
- `uw options-flow iv-outliers` (week aggregated) — high-IV contracts where flow may be exhausted.
- `uw oi decrease-with-volume` — capitulation / profit-taking detection.
- `uw screener iv-rank` (extreme high) — premium ripe to fade.

Flag names where crowdedness is **rising** (deteriorating contrarian setup) vs **falling** (crowding unwinding — potential fade entry). Gate every fade call against the week-regime baseline.

### earnings-scout — DUAL MANDATE: recap + lookahead (sonnet, thinking **on**)
Two sub-tasks:

**(a) Recap.** For each earnings event that printed this week (extract from `covered_dates` flow data), evaluate flow reaction vs pre-event thesis:
- `uw insights earnings-play` — pre-event positioning & post-event flow.
- Grade each play as confirming or disconfirming (BUY VOL → IV crush realised? SELL VOL → directional move trapped? etc.).

**(b) Lookahead.** Scan the next two calendar weeks for earnings catalysts:
- `uw screener earnings-catalyst` (next 14 days).
- `uw options-structure iv-term-structure` per candidate — KINKED/BACKWARDATION alignment.
- `uw options-structure term-skew` — back-month skew at the earnings DTE.
- `uw options-structure front-end-iv-ratio` — quick panic detector.
- `uw insights analyst-vs-flow` — analyst-vs-flow disagreement is the highest-EV setup.

Output: §6 earnings recap + ranked 2-week lookahead with IV term-structure alignment + analyst disagreement scores.

### vol-surface-scout — WoW term-structure & skew evolution (sonnet, thinking off)
Tools required:
- `uw options-structure iv-term-structure` for `WEEK_END` and `covered_dates[0]` — compute the WoW shape change.
- `uw options-structure term-skew` for `WEEK_END` and `covered_dates[0]` — WoW skew change.
- `uw options-structure front-end-iv-ratio` (current) — single-number panic check.
- `uw historical iv-percentile-zscore` (`--lookback-days 252`) — outlier-robust per-ticker IV percentile (Goyal-Saretto). Use this instead of raw IV rank where possible.
- `uw options-flow iv-outliers` (week aggregated) — single-contract outliers.
- `uw options-flow expiry-heatmap` — week-level concentration; calendar-spread candidate identification.

Flag names that went from NORMAL to KINKED or into BACKWARDATION across the week. These are §5.

### multileg-strategist — full-week sample (sonnet, thinking **on**)
Tools required:
- `uw hot-chains multileg` across the **full week** (not just today). Structures repeated on **≥2 days** carry materially higher directional inference weight than single-day prints.
- `uw options-flow top-premium-trades` filtered to ≥$1M premium (week range).
- `uw options-flow greek-screener` — directional / vol / vega bets by Greek profile.
- `uw options-flow expiry-heatmap` — concentration by expiry to spot calendar/diagonal builds.
- `uw hot-chains most-active` — per-ticker context.

Output: per-ticker structure read with directional thesis, repeated-on-N-days count, and built-in risk caps.

### leap-positioning-radar — rolling detector + 10d window (sonnet, thinking **on**)
Tools required:
- `uw oi position-rolls` across each covered date — surface conviction shifts (rolls forward into 2027/2028 LEAPs, rolls up in strike, large new LEAP OI initiations).
- `uw oi biggest-increases` (`min_dte=180`) — fresh LEAP positions only.
- `uw historical oi-trend` (`--days 10`) — BUILDING required for full points.
- `uw historical cumulative-premium-flow` (`--days 30` or default 90) — LEAP-grade slow-accretion signature.
- `uw insights institutional-accumulation` (a 10-day window).
- `uw insights conviction-matrix` — must show DIRECTIONAL_LONG with confidence > 70.

Output: §4 LEAP candidates that pass strict filters; explicit disqualification notes for any contender that doesn't.

---

## Step 2 — Phase 2: quant → fundamentals gate → bull/bear debate → risk-monitor (sequential, consumes Phase 1 union)

Phase 2 runs in four stages: the quant produces the audited score (2a); the fundamentals gate cross-checks the top-5 against the underlying (2b); a bounded bull/bear debate stress-tests them (2c); then risk gates and sizes against regime/VRP/correlation **plus** the fundamentals verdict and debate residuals (2d). Stages 2b–2c operate on the **top 5 by `raw_score` only**.

### Step 2a — signal-confluence-quant (sonnet, thinking **on**)

Once **all** Phase 1 agents return, collect the **union** of every candidate ticker surfaced across all 11 (or 12) agents for the full week. Spawn `signal-confluence-quant` with that union plus the Step 4 weekly conviction rubric. It must:

- ~~Run `uw insights signal-confluence` per ticker~~ — **REMOVED 2026-06-12 audit P0.2** (funnel-only tool; no per-ticker mode exists). Carry `confluence_score` from the Step 0 funnel when present, else `null`.
- Run `uw historical signal-backtest` per dominant signal class **under the P0.3 clean-query protocol** (`--top-n 200` pinned; complete forward windows only — the tool silently includes truncated windows in its headline; recompute WR from kept rows; market-wide per class, never presented as ticker-specific; protocol details in `signal-confluence-quant.md` "Signal-backtest substrate quarantine"). Protocol incomplete → `win_rate: null, win_rate_source: "NA(substrate)"`.
- Pull `uw historical cumulative-premium-flow` (30d and 90d) for tie-breaking and supplemental directional context.
- Compute `raw_score` per ticker against the weekly persistence-weighted rubric (Step 4), identify `dominant_signal_class`, attach `win_rate`, emit `final_size_recommendation_pre_risk`, and produce a full audit trail per ticker.

Output: sorted list `{ticker, raw_score, score_components[], dominant_signal_class, confluence_score, cum_premium_flow_30d/90d, win_rate, win_rate_n, win_rate_source, final_size_recommendation_pre_risk, audit_trail}`.

### Step 2b — fundamentals-gate (top 5; sonnet, thinking off)

The microstructure fleet is fundamentally blind. Spawn `fundamentals-gate` with the quant's **top 5 by `raw_score`**, each with `dominant_signal_class` + thesis direction, plus `WEEK_END` as the `as_of` date. It runs `python3 scripts/finnhub_enrich.py --ticker <T> --date <WEEK_END>` per name and cross-references earnings-surprise streak, insider MSPR, growth/leverage, and the news catalyst stack against the thesis direction, emitting `{ticker, fundamentals_verdict (CONFIRM/CAUTION/VETO/NA), tier_adjustment, next_earnings_date, days_to_earnings, catalyst_support, reasons[], key_risks[]}`. Cross-check `next_earnings_date` against the §6 earnings lookahead. NA never penalizes. Hands to 2d.

### Step 2c — bull/bear debate (top 5; sonnet, thinking on)

The persistence-weighted score is still additive — crowded multi-week consensus names score highest. For each **top 5 by `raw_score`**, spawn `bull-researcher` and `bear-researcher` for **1 round** (2nd round only on genuine disagreement: residuals within one bin and ≥0.75). Hand both sides the ticker's `score_components`, the 2b fundamentals enrichment, and the Step 0 macro/event context. Debates run in parallel across names; bull-then-bear within a name. Output per ticker: `{bull_residual, bear_residual, bull_strongest_unrefuted, bear_strongest_unrefuted}`. The debate can only cut size, never add it.

### Step 2d — risk-monitor (sonnet, thinking off)

Spawn `risk-monitor` with (a) the quant's sorted score list, (b) the 2b fundamentals verdicts, (c) the 2c debate residuals, and (d) the week-baseline context block from Step 0 (incl. `macro_snapshot` + `event_risk`). It must:

- Run `uw risk portfolio-correlation` against the week-candidate set — flag corr > 0.7 sub-groups as concentration risks.
- Confirm `uw risk market-regime` from Step 0 (already pinned; do not re-fetch).
- Apply the full gate stack: VETO → watch-only (fundamentals); −1 tier each for regime conflict, panic (`uw options-structure front-end-iv-ratio > 1.10`), VRP-vs-trade-type contradiction, corr-cluster duplication, adverse sector rotation, `fundamentals_verdict == CAUTION`, a Tier-1 macro/earnings event inside the trade horizon (event-risk gate), and bear residual ≥ bull residual (debate gate). Emit an explicit `gate_verdicts` line per call — **all 9 keys** including the new `rubric_regime` verdict (2026-06-12 P0.6).
- Pull `uw watchlist alerts` and `uw watchlist scan` against the prior `conviction_week_<previous>` group — surface adverse-flow exit candidates.
- Persist this week's top 5 conviction names (post-gate, excluding VETO'd names) via `uw watchlist manage --action add --group conviction_week_<ISO_WEEK> --tickers <top_5_by_score>`.

Output: §7 risk & correlation — clusters, regime conflicts, VRP / panic gates applied, fundamentals verdicts, event-risk flags, debate cuts, adverse-flow exit list, hedge sleeve recommendation, final sizing table per ticker that consumes the quant's pre-risk size.

---

## Step 3 — Confluence gate

Before scoring, apply the **confluence gate**: a ticker only enters the conviction rubric if **at least two distinct Phase 1 agents flag it positively across the week**. Names flagged by a single agent are noted in §10 ("Watch-only — single signal") and excluded from the high-conviction list. This rule prevents single-tool false positives from contaminating the trade book.

> **2026-06-12 audit P0.2 — the `uw insights signal-confluence` entry path was REMOVED** (it had also drifted internally: gate ≥5 here vs ≥4 in the Step 4 rubric line, an undecidable award). The tool is a server-side composite of the same quantities the rubric scores and has no per-ticker mode — it cannot be a second opinion and cannot be queried deterministically per candidate. Its single remaining role in the whole pipeline is the Step 0 #6 funnel seed. Do not consult it at entry, scoring, or HIGH-gate stages.

### Step 3a — HIGH-tier load-bearing-tool gate (2026-05-09 audit P0; 3-of-4 as of 2026-06-12 audit P0.2)

After scoring, before any candidate enters the HIGH-tier section of §3 / §8 (i.e. anything that would be sized as `full` post-quant), the call must additionally cite at least **3 of the 4 LOAD-BEARING tools**:

- `uw dark-pool block-stratified` (institutional-vs-retail filter)
- `uw historical cumulative-premium-flow` (30d directional accretion)
- `uw insights institutional-accumulation`
- `uw options-structure dex` (DEX)

A call that scores raw_score ≥ 9 (HIGH-tier under the 2026-05-30 P1.3 cut) but cites fewer than 3 of these four tools must be **demoted to MEDIUM tier**.

# `uw insights signal-confluence` REMOVED from this gate 2026-06-12 audit P0.2 (added 2026-05-23): the tool is a
# composite of the other gate members' own quantities (dp_accumulation / oi_building / bullish_flow factors,
# verified live), so citing it added correlated citation breadth, not evidence independence; its +19.5pp (n=12)
# promotion evidence was selection-confounded and method-unstable (+17.2 → −1.0 under path-aware grading,
# 2026-05-30). Known accepted limitation: the remaining 4 tools are still downstream of one actor's footprint —
# the gate guards thin HIGHs, not correlated ones; the cross-QUANTITY independence requirement is pre-registered
# for a future cycle.

---

## Step 4 — Weekly conviction score (persistence-weighted rubric, applied by signal-confluence-quant in Step 2a)

> **RUBRIC FROZEN — version `2026-06-12` (audit P0.1).** Same freeze as the daily rubric: no promote/demote/re-bin until a change clears a pre-registered, cross-regime, BH-surviving bar. Audits grade; they do not retune. Every emitted envelope stamps `rubric_version: "2026-06-12"`. (Context: the ≥9 HIGH cut failed its scheduled 2026-06-12 re-confirmation — HIGH realized 0.222 on the first post-UPTREND window — and six prior cycles of re-weighting on n=8–31 single-regime samples are the documented failure mode.)

For every ticker that cleared the confluence gate, the quant computes the weekly conviction score against this rubric. Every signed point gets attached to a named source agent + tool in `score_components`.

```
Weekly conviction score = Σ:
  # +3 line for swept on ≥3 of 5 days REMOVED 2026-05-23 audit P0.3
  # Reason: uw hot-chains sweep-persistence marginal contribution −22pp two consecutive audits; multi_day_sweep signal class realised 0.43 vs claimed 0.70 (+27pp overstatement).
  # Tool remains informational — sweep-tracker still surfaces persistence-ranked sweeps in §3/§8 prose — but contributes 0 points to raw_score.
  # Directional confirmation must come from accumulation, multileg, or cum_flow_30d instead.
  +3  uw historical oi-trend BUILDING for the full week, --days ≥ 5 (accumulation-hunter / leap-positioning-radar)   # WEEKLY-ONLY +3 vs DAILY +1 (daily reduced +2→+1 on 2026-05-09 as 'correlated with the LOAD-BEARING components'). Documented divergence (2026-06-12 P1.2): the weekly weight is intentionally higher because BUILDING sustained across a full 5-day covered week is a materially stronger persistence read than a single daily ≥5-day-lookback snapshot — but the same correlated-component concern the daily demote cited applies here too (OI build co-moves with the +3 accumulation conjunction and historically with cum-flow). FROZEN at +3 (P0.1); a candidate over-weight is PRE-REGISTERED for decision at a future cross-regime audit: hypothesis 'weekly OI +3 double-counts with the accumulation conjunction', acceptance bar = cross-regime ∧ n≥30 per arm ∧ BH-surviving, decision window post-2026-06-12 TRANSITIONAL accrual.
  +3  3+ aligned signals in accumulation-hunter sustained across week, uw dark-pool block-stratified institutional-tier confirmed — CONJUNCTION (2026-05-25 register C11): full +3 only when cum_premium_flow_30d confirms (sign aligned with thesis AND |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1. Reason: additive DP+accum+matrix manufactured false HIGH conviction (tier inversion HIGH 60.0% < MED 62.5%, n=49); the ≥0.80 WR is a conjunction (DP-block ∧ cum_flow ∧ institutional-accum). Distinct from flow_conflict/−lite (those subtract on opposing/MIXED flow; this reduces the +3 accumulation award to +1 on non-confirming flow — both may fire). A sub-$50M flow that halves this line does not separately qualify as "net directional accretion" for the +1 cum_flow line (demoted from +3, 2026-06-06 P1.4). See signal-confluence-quant.md "Conditional dark_pool_accumulation conjunction".   # was +2; promoted 2026-05-15 audit P1.2 — Phase 4 +27.8pp marginal contribution (LOAD-BEARING)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70, stable WoW — CONDITIONAL ONLY (2026-05-23 audit P1.1): award +1 only when dominant_signal_class == leap_directional; in all non-LEAP contexts contribution is 0. Phase 4: marginal contribution −23pp (n=8) on swing/weekly horizon (e.g. BL LOSS, MA LOSS both cited this tool). LEAP gate in leap-positioning-radar still consumes this tool — only the swing/weekly award is gated to leap_directional.
  +2  uw oi position-rolls shows institutional roll forward into longer-dated LEAP (per-covered-date)
  +1  uw historical cumulative-premium-flow shows net directional accretion across the week — fresh-thesis (sharp 30d) or thesis-extension (smooth 90d) — INTENT-SCREENED (2026-06-06 audit P1.4): award the +1 only when the premium passes an intent screen: (a) no C28 distribution_flag present on the name (uw oi decrease-with-volume closing signature), AND (b) on dividend payers inside an ex-div window, the accreting prints are NOT deep-ITM sub-parity calls (dividend-capture arb, not conviction — the NEE 2026-06-04 false-bullish). Screen failed or unevaluated on a flagged name → 0.   # DEMOTED +3→+1 2026-06-06 audit P1.4 — most-cited tool in the book (n=136) and NO-INFO across three consecutive path-aware audits (−3.5pp MC); demoted-not-removed (reconstructed-citation provenance caps at P1; tool stays in the LB gate (3-of-4 as of 2026-06-12 P0.2)). Original promotion (+2→+3, 2026-05-15, +24.2pp) was a close-only-method artifact.
  # +2 line for uw insights signal-confluence ≥4 at WEEK_END REMOVED 2026-06-12 audit P0.2 (added 2026-05-23 P1.2)
  # Reason: live factor-list probe shows it is a server-side RE-COUNT of already-scored quantities
  # (dp_accumulation / oi_building / bullish_flow); it also contradicted the Step 3 gate threshold (≥5 vs ≥4 —
  # undecidable as written) and the CLI has no per-ticker mode. Funnel-seed role only (Step 0 #6); no points,
  # no entry path, no LB-gate slot.
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna squeeze in trade direction across the week — verified SIGN CHANGE only, not a level: sign(net_dex) on the latest session opposite to ≥3 consecutive prior sessions, read from dated `uw options-structure dex --date` calls (≥4 to verify the prior-session sign run; ~11 for the trailing-median floor) across covered_dates, flip-day |net_dex| ≥ 0.25× trailing-10-session median |net_dex|, both dated values cited in evidence; vanna leg requires a dated VIX source (Yahoo chart API ^VIX)   # DEMOTED +2→+1 and MECHANIZED 2026-06-12 audit P0.4 — the 06-11 daily book awarded the flip line to three names with no sign change in their windows (level-as-flip); no peer-reviewed support at the 1–4wk horizon; restore weight only via a pre-registered dex-flip backtest showing cross-regime forward excess
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector — CONDITIONAL (2026-05-23 audit P1.5): award +1 only when (a) sector persistence_score ≥ 0.6 (the tool's 0–1 sign-consistency scale = ≥3-of-5-days; 2026-05-25 fix — was an unsatisfiable `≥3`) AND (b) cum_premium_flow_30d direction aligned with thesis direction AND (c) |cum_flow_30d| ≥ $50M. Default 0. Phase 4: sector_persistence marginal +2.8pp standalone (NO-INFO); when paired with cum_flow alignment it carried HON-W21 (+4.9% WIN) vs WMT-W19 (−10.4% LOSS).
  +1  in earnings-scout BUY VOL or SELL VOL for next 2 weeks (uw options-structure term-skew aligned for full size)
  +2  multileg-strategist directional structure repeated on ≥2 days (term-structure-anchored play type)   # was +1; promoted 2026-05-09 (Phase 4 +8pp marginal)
  +1  vol-surface-scout flags KINKED or BACKWARDATION, worsening WoW; uw historical iv-percentile-zscore extreme; VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner crowded long with rising uw historical pc-ratio-zscore trajectory (VRP positive)   # MECHANISM (2026-06-12 P1.5, re-attributed per P4): an INFORMED-FLOW CONTINUATION penalty, not a "crowd is wrong, fade it" signal. Single-name P/C extremes predict continuation, not reversal (Pan-Poteshman 2006; Ge-Lin-Pearson 2016) — a crowded long sits on the side informed flow tends to continue, so a LONG resting on crowded-euphoria evidence is the riskier long and gets docked. The weekly already reads a multi-date z "trajectory" (correct — the rising/falling path the daily must reconstruct from dated calls). Frozen at −2 (P0.1); routed through the C13 router so it never double-counts with a flow read.
  -3  flow_conflict — signal-confluence-quant applies mechanically when uw historical cumulative-premium-flow 30d direction is *clearly opposite* dominant_signal_class (signed-sum sign flip + magnitude > today's union-median |cum_flow_30d|, or explicit OPPOSITE label)   # 2026-05-15 audit P0 — see signal-confluence-quant.md "Mechanical flow_conflict deduction" rule; 2026-05-23 audit P1.3: mutually exclusive with flow_conflict_lite (apply ONE, never both)
  -1  flow_conflict_lite — signal-confluence-quant applies when the 30d cum_premium_flow read is MIXED (signed sum near zero, or aligned but bottom-quartile magnitude)   # 2026-05-15 audit P0; 2026-05-23 audit P1.3: mutually exclusive with flow_conflict (apply ONE, never both)
  # 2026-05-09 -2 generic flow_conflict line replaced with the mechanical -3 / -1 split above (Phase 3 2026-05-15 audit: 30% missed-gate rate at the generic line)
  # The two lines below are NOT score_components — they are risk-monitor TIER gates applied in Step 2d, documented here
  # for the full deduction stack. They contribute 0 to raw_score and never appear in score_components (2026-06-12 P1/F5,
  # verified 0/151 daily+weekly envelopes — the quant cannot gate on regime/correlation, risk acts on tiers, validator locks Σ).
  -2  [TIER GATE, 2d] risk-monitor flags in week-candidate correlation cluster (pairwise corr ≥ 0.70) — −1 TIER, not −2 points
  -3  [TIER GATE, 2d] WoW uw risk market-regime flip conflicts with trade direction — −1 TIER (regime gate), not −3 points
```

### Conviction tiers (2026-05-15 audit P0; supersedes prior ≥9 / 6–8 / 3–5 cuts)

Map every ticker to a tier:

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | **HIGH** | full size (subject to win_rate gate in Step 5) |
| 7 – 8 | **MEDIUM** | half size (subject to win_rate gate) |
| 3 – 6 | **LOW** | starter / watch-only — paper trade or wait for daily confirmation |
| ≤ 2 | drop | not surfaced in the report's trade book |

Surface every HIGH and MEDIUM tier ticker in the Executive Summary headline and §8 (High-Conviction Cross-Ref). LOW tier goes into a separate "Watchlist for next week" section (§9). **Tier-cut status (2026-06-12):** the ≥9 HIGH cut (2026-05-30 P1.3, set in-sample on UPTREND data where the ≥9 bin realised 0.774 n=31) **failed its scheduled re-confirmation on 2026-06-12** — bands inverted on the first post-UPTREND window (HIGH 0.222 / MED 0.214 / LOW 0.444). The cuts are retained under the P0.1 freeze (re-binning on another thin window would repeat the documented failure mode) but carry no validated ranking claim; the P0.6 out-of-regime guard caps all sizing at half in the interim.

---

## Step 5 — Backtest-weighted sizing (gates the tier sizing)

For each HIGH or MEDIUM tier ticker, identify its dominant signal class — typical labels: `multi_day_sweep`, `oi_build`, `dark_pool_accumulation`, `leap_roll`, `multileg_repeat`, `bullish_flow`, `bearish_flow`, `vanna_squeeze`. Obtain the class win-rate **only via the P0.3 clean-query protocol** (2026-06-12 audit; Step 2a + `signal-confluence-quant.md` "Signal-backtest substrate quarantine" — the raw tool headline includes clamped forward windows and is pagination-unstable). Apply the win-rate gate **on top of** the tier sizing (**2026-05-15 audit PC.1**; full-size threshold tightened 0.65 → 0.70):

| `win_rate` (clean protocol) | Multiplier |
|---|---|
| ≥ 0.70 | × 1.0 (keep tier sizing) |
| 0.50 – 0.70 | × 0.5 (one tier down — HIGH→half, MEDIUM→starter) |
| < 0.50 | × 0 → watch-only (no live capital — equivalent to the daily 'skip'; consistent with the quant's authoritative `win_rate < 0.50 ⇒ starter/skip` floor applied at emission. 2026-06-12 P1.2: this is a downstream win-rate-gate multiplier, not a competing floor — both resolve to no-capital) |
| `null` (newly covered, no history) | starter — matches the quant's sizing map |
| `NA(substrate)` (clean protocol could not complete) | tier default capped at half, then gates |

For non-directional signals (`high_iv_rank`, `volume_spike`) the backtest returns `vol_realisation_rate` instead — same thresholds, same clean protocol. Note the win_rate explicitly next to each call in the Swing Book (§3) and LEAP Book (§4) **with `win_rate_source` and kept `n`**.

**Out-of-regime guard (2026-06-12 audit P0.6, downgrade-only):** the rubric was fitted entirely in the UPTREND regime that ended 2026-06-12. Until a `/calibration-audit` records **≥30 resolved post-2026-06-12 calls** and re-validates the tiers, every conviction-tier size is **capped at half**, and the Executive Summary must carry `Rubric regime status: OUT-OF-REGIME (fitted UPTREND; current <regime>) — sizing capped at half`. risk-monitor enforces the cap (its `rubric_regime` gate); the lift happens by editing this block when the named audit clears it.

**On top of this ladder (2026-05-25 register C2), the quant applies two downgrade-only guards** (see `signal-confluence-quant.md` "Market-excess gate" + the N-conditional cap): (1) the `n < 10` cap is **0.69** (below the 0.70 full line — a small-N up-week class sizes at most half), and (2) a **market-excess gate** — if a class does not beat the same-direction SPY bet over the same windows (`excess ≤ 0`), cap at half; `excess ≤ −0.10` → starter. Beta in an up-tape is not edge. The win-rate denominator is computed only over liquidity-floor-passing names (C12). Reusable: `scripts/excess_winrate.py:size_decision`. **(3, register C4)** a `bullish_flow`/`bearish_flow` class also caps at half when the flow is **not OI-confirmed-opening** (Pan-Poteshman: only opening flow predicts) — `uw historical oi-trend` BUILDING or ΔOI ≥ 20% of day volume; flat/falling OI vs high volume = churn → cap half. Reusable: `scripts/oi_opening.py:opening_gate_size`. All three guards are downgrade-only and may stack.

---

## Step 6 — Thesis scorecard: intra-week signal performance

For every ticker surfaced by any Phase 1 agent this week, check whether signals present at the **start** of the week resolved in their predicted direction by **week-end**. This is derived entirely from fresh `uw` CLI queries — no daily analysis files are read.

For each ticker, run these checks using `covered_dates[0]` and `covered_dates[1]` as early-week reference dates and `covered_dates[-1]` (today / Friday) as the resolution date:

1. **Sweep signals** — `uw hot-chains sweep-persistence` (`sessions_in_top`) + a **directional corroboration** from `uw hot-chains smart-money-flow` or a multi-date cum-flow read (2026-06-12 P1.5: sweep-persistence exposes no per-day directional series — `consistency_score` is `sessions_in_top/5`, a participation share, and `dominant_direction` is the window net, not a per-day path; do not infer day-1-vs-2 directional continuation from it alone). Did the persistence + corroborated direction sustain to week-end or reverse?
2. **OI-build signals** — `uw historical oi-trend` (`--days 5`). Did OI continue building (BUILDING → WIN) or roll off (LOSS)?
3. **Premium flow signals** — `uw historical cumulative-premium-flow` for the full week range. Did net premium align with the directional thesis?
4. **Direction confirmation** — `uw historical trend` over the week range. Did price action confirm or contradict the early-week signal direction?

Grade each ticker:
- **WIN** — signal direction confirmed by end-of-week flow and price trend.
- **LOSS** — price/flow moved against the early-week direction.
- **INCONCLUSIVE** — insufficient price movement or contradictory signals (excluded from hit-rate denominator).

Summarise in a table: `| Ticker | Signal type | Early-week direction | Week-end outcome | Grade | Note |`

Compute the week's hit rate: `wins / (wins + losses)`. This headline goes in the Executive Summary as **Signal performance**.

---

## Step 7 — Strategy synthesis on the conviction list

For each **HIGH and MEDIUM** tier ticker (after the win-rate gate):
1. Call `uw insights deep-dive` — full Yahoo + UW data for full thesis verification.
2. Call `uw historical trend` (`--days 10`) — multi-week price/flow trend confirmation.

For the entire HIGH and MEDIUM tier list (in one call):
3. Call `uw playbook batch-scan` with the ticker list — get rule-based options-strategy suggestions. Cross-reference against multileg-strategist's named structures; prefer the multileg read if there's disagreement and note the conflict.

This step is the synthesis bridge from "signal" to "trade structure" — without it, conviction scores are abstract.

---

## Step 8 — Write the report

Synthesize into the structured weekly note below. Use **full narrative sentences** in qualitative sections (Executive Summary, Regime & WoW Delta, Risk, Setups for Next Week) and **tables** for data-dense sections (Signal Performance, Swing Book, LEAP Book, High-Conviction Cross-Ref). Tone: institutional desk strategist — precise, assertive, no filler.

Before writing: run `mkdir -p analyses/weekly/$ISO_WEEK` via Bash (creates the run folder).

````markdown
# Weekly Market Intelligence — Week of YYYY-MM-DD (ISO YYYY-WW)

## Executive Summary
- **Week regime + WoW Δ:** <regime today vs Monday — improved / deteriorated / held — plus VRP classification, one line>
- **Rubric regime status:** <`IN-REGIME` or `OUT-OF-REGIME (fitted UPTREND; current <regime>) — sizing capped at half` — the P0.6 guard line; mandatory while the 2026-06-12 freeze block in Step 5 is active>
- **Signal performance:** <X of Y early-week signals confirmed (hit rate %)>
- **Top swing build for next week:** <ticker, thesis, invalidation, win_rate, tier, size>
- **Top LEAP build:** <ticker, scenario, invalidation, win_rate, tier, size>
- **Biggest emerging risk:** <correlation cluster name + members, OR adverse flow, OR regime flip>

## 0. Week in Review — Intra-Week Signal Performance
[Table: Ticker | Signal type | Early-week direction | Week-end outcome | Grade | Note. Hit rate headline. Sourced from uw hot-chains sweep-persistence, uw historical oi-trend, uw historical cumulative-premium-flow, uw historical trend — no daily files read.]

## 1. Regime & WoW Delta
- `uw risk market-regime` today + Monday baseline; WoW delta narrative
- `uw historical vrp` classification — premium-selling vs premium-buying environment
- `uw options-flow dte-volume-share` aggregated across the week — institutional vs retail share trend
- **Macro backdrop** (`scripts/fred_macro.py` `macro_snapshot`): yield-curve sign, core CPI/PCE YoY, unemployment + payrolls, 10Y/USD direction — plus next-two-weeks `event_risk` calendar (Tier-1 prints)
- Implications for next week's bias

## 2. Sector Rotation
- `sector-rotation-strategist` output: rotating-into / rotating-out-of sectors with persistence scores (≥3 days)
- Rotation regime call (defensive→cyclical / cyclical→defensive / growth→value / value→growth / no_change) with regime confidence
- Named single-name leaders within each rotating sector
- Rotation narrative for next week + swing-book implications

**ETF flow tape (advisory)** — instrument-level layer the GICS aggregates can't see. Surface `etf_flow_tape[]` as a ranked table:

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|

Lead with top-3 inflow / top-3 outflow ETFs. Call out **GICS-vs-ETF agreement** explicitly (agree → high-conviction rotation; disagree → watch-only; `n/a` → instrument-only thematic/geographic read). Frame as advisory: ETF DP is a positioning/persistence tell (creation/redemption & hedging), **not** single-name accumulation; ETF options flow is weighted above ETF DP. The tape **strengthens** the existing conditional sector-leader +1 (via `gics_agreement` + cum_flow alignment) — it adds **no rubric points**.

## 3. Swing Book (1–6 weeks) — ranked by weekly conviction score
[Table: Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure | Invalidation. Subdivide into 3a long swings (regime-aligned) and 3b short/fade swings (defined risk only). **Invalidation (C34):** anchor to the institutional `uw dark-pool price-levels` shelf where one exists, not a guessed %. **Distribution caution (C28):** for any long name carrying a `distribution_flag` (bullish-side OI closed across the week), add a one-line ⚠ note — advisory, 0 points, no size change.]

## 4. LEAP Book (6–24 months)
[Table: Ticker | Tier | Score | Win-rate | Final size | Scenario | Invalidation. leap-positioning-radar with `uw oi position-rolls` highlights and `uw historical cumulative-premium-flow` accretion. DIRECTIONAL_LONG only.]

## 5. Volatility Surface — WoW Term Structure & Skew Evolution
- vol-surface-scout: names that shifted to KINKED or BACKWARDATION across the week
- WoW IV term-structure delta with `uw options-structure iv-term-structure` snapshots from `covered_dates[0]` and `WEEK_END`
- Skew change narrative; calendar-spread candidates
- `uw historical iv-percentile-zscore` outliers (multi-month percentile context)

## 6. Earnings — Recap & 2-Week Lookahead
- (a) Recap of this week's prints with flow reaction grades
- (b) Ranked lookahead to next 2 weeks with IV kink alignment and analyst-vs-flow disagreement scores

## 7. Risk & Correlation (week-candidate universe)
- risk-monitor consuming the full week-candidate union — not the static watchlist
- `uw risk portfolio-correlation` clusters with member tickers and corr coefficients
- **Macro & event risk**: `macro_snapshot` headline + next-two-weeks `event_risk` calendar
- **Fundamentals verdicts**: per top-5 name — CONFIRM/CAUTION/VETO with the contradicting facts (insider MSPR, miss/beat streak, earnings date)
- **Debate-disconfirmation cuts**: names where the bear residual ≥ bull residual
- **Breadth cross-check** (when `breadth_cross_check` present): advancers/decliners + `pct_green`; flag any divergence from the `uw` regime label (green tape with `pct_green < 50` = distribution tell) — advisory, no size impact
- Concentration risks + recommended hedge sleeve

## 8. High-Conviction Cross-Ref (HIGH and MEDIUM tier)
[Per-ticker breakdown: tier | score components | win_rate (with n + source) | `fundamentals_verdict` | bull/bear residuals | gate_verdicts | final size | invalidation level | `distribution_flag` when present. One paragraph per HIGH-tier name. Note any VETO'd name with its distribution evidence.

**Expectancy lens (advisory — C31):** lead §8 with a per-tier expectancy + payoff-ratio line (avg win / |avg loss|) from the latest `/calibration-audit` `phase_3_calibration`, or computed over the rolling `conviction_<date>` closed calls via `scripts/kelly_sizing.py`. Display-only — the live sizer stays the win-rate ladder (Step 5); C3 Kelly remains ADVISORY until tier×expectancy is monotone on n≥30. It keeps the desk honest about where the week's edge lives (asymmetry, not hit-rate).]

Embedded rubric (for audit):

[Embed the Step 4 conviction rubric verbatim here.]

## 9. Setups for Next Week
- gamma-flip-tracker next-session GEX **advisory** (SPY/QQQ only) — regime, zero-gamma level, call/put walls, one-line structure bias + mandatory caveats. Lead with the Step 0 `gex_advisory_backtest` verdict (`GO_WALLS_PREDICTIVE` / `NO_GO_NO_EDGE` / `INSUFFICIENT_SAMPLE`, with n + walls-as-magnet hit-rate vs 50%) so the advisory is framed by its current out-of-sample track record, not presented as a proven edge.
- **Next-session 0DTE premium-selling setup** (from Step 0 `zerodte_setup`, the validated stack): per index `{sell_premium, vol_state, size_scalar, expected_range_pct, suggested_structure, entry_rule, stand_aside_reason}` plus the rolling `backtest.verdict` and **both** `mean_pnl_open_pct` (gross) and `mean_pnl_open_net_pct` (net of the assumed round-trip cost). Delta-neutral, advisory, 0 rubric points. Key rules: sell only when front IV rich (size by VIX level), wing width from the GEX vol-suppression range, **enter at the open / never carry overnight**, stand aside on a VIX spike or front-end backwardation. SPY≈SPX (trade either); QQQ weaker. **2026-06-12 P1.8: quote PnL on its real basis** — `mean_pnl_open_pct` is **% of underlying spot notional, GROSS** (`pnl_basis` field), not premium-collected/margin; lead with the **net** line (Vilkov 2024: unconditional 0DTE condor flips negative net of costs). **Promotion bar:** advisory/0 points **permanently** until a vol-shock day enters the sample AND net expectancy clears a tail-aware bar — win-rate is NOT the promotion metric (negatively-skewed short vol). Flag the unsampled-tail caveat every time.
- dealer-positioning-strategist swing setups — DEX flips, vanna squeezes, regime flips for the next 1–4 weeks
- Pin vs trend regime call
- 2–3 highest-conviction actionable setups for the coming week (HIGH-tier names)
- LOW-tier names to track for daily-analysis confirmation
- OPEX-week ranked book if `opex-pin-strategist` was spawned — pin candidates with `suggested_structure` per name (iron flies, short straddles, broken-wing butterflies)
- **Deep-dive hand-off** (optional): for the top 2 HIGH-tier names (post-gate, non-VETO), if the `stock-deep-dive` skill is available invoke `/stock-deep-dive <TICKER>` and record the report path here; otherwise emit the recommendation verbatim (`Recommended deep dive: /stock-deep-dive <TICKER>`). Skip on a no-edge week.

## 10. Watch-only — single signal, no confluence
[Names that surfaced from one agent but failed the confluence gate. Listed for journaling, NOT for trade entry next week.]
````

---

## Step 9 — Confirm watchlist write-back (handled by risk-monitor in Step 2d)

The top-5 watchlist write-back is performed inside `risk-monitor` during Step 2d — the agent calls `uw watchlist manage --action add --group conviction_week_<ISO_WEEK> --tickers <top_5_by_score>` with this week's top 5 by conviction score (excluding any VETO'd name). **Do not double-write.**

Confirm the write-back happened by checking the `risk-monitor` output for the explicit `watchlist_write_back_confirmation` field. If missing, call `uw watchlist manage --action add --group conviction_week_<ISO_WEEK> --tickers <top_5_by_score>` directly as a fallback.

If any name was already on a manually-curated group, leave that membership alone — write only to the week-stamped group. This closes the feedback loop: this week's high-conviction names become next week's correlation universe; next week's RM automatically pulls `uw watchlist alerts` and `uw watchlist scan` against the prior week's group to flag adverse-flow exits.

---

## Step 10 — Save, emit decision envelope, and confirm

1. Use Write to save the report to `analyses/weekly/$ISO_WEEK/report.md`.
2. **Emit the structured decision envelope** at `analyses/weekly/$ISO_WEEK/decision.json` (with `report_path` set to `analyses/weekly/$ISO_WEEK/report.md`), conforming to `schemas/decision_envelope.schema.json` (the machine-resolvable sidecar `/calibration-audit` Phase 1 reads). Top level: `{schema_version: "1.3", rubric_version: "2026-06-12", report_date: <WEEK_END>, report_kind: "weekly", iso_week: <ISO_WEEK>, regime, vrp_classification, macro_snapshot_signals, macro_event_risk, watchlist_write_back, next_session_gex, next_session_0dte_setup, breadth_cross_check, report_path}` (`1.3` adds the `rubric_version` era stamp, 2026-06-12 audit P0.1; `1.2` added the advisory per-call `distribution_flag`, C28; older versions stay valid); `calls[]` carries the quant audit fields + `fundamentals_verdict` + `debate_residual_confidence` (bull residual) + `debate_residuals` ({bull, bear} — 2026-06-12 P1.1, so the debate gate's discrimination is measurable) + `market_excess` (C2 result per call, negative = beta not edge — P1.1) + `gate_verdicts` (**all 9 keys** `regime, vrp, panic, cluster, sector, fundamentals, event_risk, debate, rubric_regime` on every non-DROP call; the validator rejects a 1.3 envelope missing any — the `debate` key had been silently absent on 0/151 prior calls, root cause now fixed) + (for top-5) the advisory `fz_context` block per call + (for long names with bullish-side OI being closed) the advisory `distribution_flag` block (`{present, closing_side, closing_premium, oi_decrease, note}` — 0 points, 0 tier impact, never a `score_components` line). `breadth_cross_check` (advisory, top-level, 0 points): `{advisory: true, source: "finviz", advancers, decliners, pct_green, divergence_flag, note}` — `null` when `fz_available == false`. Two **advisory** top-level blocks (SPY/QQQ only), **not** `calls[]` members (prose-only, 0 points): `next_session_gex` (`{advisory: true, as_of_eod_date: <WEEK_END>, next_session_date, indices: [{symbol, spot, zero_gamma_level, zgl_reliable, regime, total_gex, call_wall, put_wall, read, structure_bias, caveats}]}`) and `next_session_0dte_setup` (copied from `zerodte_setup`: `{advisory: true, as_of_eod_date: <WEEK_END>, backtest_verdict, indices: [{symbol, sell_premium, vol_state, vix, implied_move_pct, expected_range_pct, size_scalar, suggested_structure, entry_rule, stand_aside_reason, caution}]}`; `null` if `available:false`). Invariant: `Σ score_components[].points == raw_score` per call.
3. **Validate it:** `python3 scripts/validate_decision.py --file analyses/weekly/$ISO_WEEK/decision.json` via Bash. If it exits non-zero, fix the envelope until it passes.
4. Confirm both files were written.
5. Print the **Executive Summary** section to chat. Nothing else — the user opens the file for the rest.

---

## Failure modes & recovery

- **Phase 1 agent times out** — re-spawn just that agent with the same context block. If it fails twice, write its section as `[agent timed out — see <agent-name> logs]` and proceed; do not let one agent block the report.
- **`uw historical available-dates` shows fewer than 3 covered weekdays** — produce a "limited-data weekly" with that explicit caveat in the Executive Summary. **2026-06-12 P1.2 — do NOT lower the tier cuts** (the prior rule dropped HIGH to 8+, which is backwards: thinner data widens uncertainty on every persistence read, so the response is *more* evidence required, not less). Keep the frozen cuts (HIGH ≥9 / MED 7–8 / LOW 3–6) and instead **tighten on the evidence side**: require the confluence gate to clear **3 distinct Phase-1 agents** (not 2) for any HIGH/MEDIUM call, and **cap every size one notch tighter** (HIGH→half, MEDIUM→starter, all else watch-only) on top of the P0.6 out-of-regime cap. A thin week should produce fewer, smaller calls — never the same production rate at a lower bar.
- **`uw risk market-regime` errors on Monday baseline** — fall back to `covered_dates[1]` and note the substitution.
- **No tickers clear the confluence gate** — produce a report whose §3, §4, §8 are explicitly empty, with §0 (scorecard), §1 (regime), §2 (sector), §5 (vol surface), §6 (earnings), §7 (risk), and §9 (setups) still populated. A "no edge" week is a valid output, not a failure.

---

## Single-Leg Whale Persistence (advisory — criterion C19)

Run the tier scan across each of the week's sessions:

```
uw options-flow single-leg --regime <weekly_regime> --date <YYYY-MM-DD> --json --quiet
```

- **Persistence:** flag names that throw **repeat** Tier-1 opening/floor PUT
  prints across the 5-day window — repeat informed positioning outranks one-offs.
- **OOS scoreboard:** track the realized next-session hit-rate of each week's
  Tier-1 signals; this is the live out-of-sample accrual toward C19 graduation
  (promote to a scored bearish line once rolling WR ≥58% over ≥60 days / ≥2 regimes).

Validated edge (bull window, Mar–May 2026): Tier-1 opening put WR 63.5% (+26pp vs
SPY, p<0.001); floor-put block 61.0%. Calls = beta (−9.7pp). size/OI<0.5 = anti-signal.
Advisory only — 0 rubric points. See
`analyses/audit/2026-05-29/single_leg_whale_implementation_plan.md`.

**2026-06-12 audit P0.5 re-validation + refinements:** refreshed-window re-run holds —
Tier-1 PRIME 0.600 (n=295, +21.9pp, p≈0), month-stable, **June/TRANSITIONAL cohort
0.632 (n=19)** — the second-regime accrual the graduation gate requires has begun.
(a) Weight repeat Tier-1 put names higher when `fz_context` shows borrow constraint
(`short_ratio` / `short_float`) — the published bearish-information channel is
short-sale cost (Johnson & So 2012). (b) "Calls = beta" is **bull-regime-conditional**
(Ge-Lin-Pearson 2016 found opening calls the most informative leg on signed data) —
outside bull regimes report `CALL_UNVALIDATED`, not a default fade. Promotion to a
scored bearish line happens ONLY through the pre-registered gate (rolling WR ≥58%,
≥60 days, ≥2 regimes), at the audit that certifies it.
