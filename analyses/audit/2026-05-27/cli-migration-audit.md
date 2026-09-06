# `uw` CLI ⇄ `mcp__uw-pp__*` Migration Audit

**Date:** 2026-05-27
**Scope:** All three repo commands — `daily-analysis.md`, `weekly-analysis.md`, `calibration-audit.md` — and every UW tool call they (and their agents) make.
**Goal:** Tie every `mcp__uw-pp__*` tool call to its `uw` CLI equivalent, verify identical results, and produce a migration plan.

---

## 0. TL;DR

- The `uw` CLI (`/Users/ewan/.local/bin/uw` → `…/unusual-whales/unusual-whales-pp-cli`) and the `uw-pp` MCP server (`…/unusual-whales-pp-cli-mcp`) are **built from the same Go source tree, same commit, same timestamp** (both rebuilt 2026-05-27 11:48). Per the upstream `PARITY.md`, **the MCP wrapper literally shells out to the CLI.**
- **All 61 tools map 1:1**, mechanically: `mcp__uw-pp__<group>_<sub>` → `uw <group-with-hyphens> <sub-with-hyphens>`. The MCP input-schema argument names are **identical to the CLI flag names** (kebab-case: `--dte-max`, `--lookback-days`, `--signal-type`, `--top-n`, `--symbol`, plus the shared global `--json/--csv/--compact/--select/--quiet`).
- **Output is identical** for pure-parquet tools (byte-for-byte modulo float round-trip). The handful of tools that blend a **live price quote** (`risk_market_regime`, `options_structure_gex/dex/vanna_charm`, the yfinance-enriched `insights_*`, `historical_vrp/trend`) return numerically tiny call-time deltas in their price-derived fields — and they do so **identically whether called via MCP or CLI**, because both run the same code path at call time.
- The **only consumer-facing change** to migrate is mechanical: replace each `mcp__uw-pp__*` tool call with a `uw … --json` Bash invocation. Both already emit the `{"source":…, "results":[…]}` envelope, so downstream parsing is unchanged.
- The one **mutating** op (`watchlist_manage add`) writes to a shared XDG file (`~/.config/unusual-whales-pp-cli/watchlist.json`) used by **both** front-ends → **zero state migration**; CLI and MCP already read/write the same file.

**Finished-criteria status:** ✅ every step of all 3 commands walked; ✅ every tool call tied to a CLI call; ✅ output equivalence verified empirically across all 11 server groups; ✅ migration plan produced (see `cli-migration-plan.md`).

---

## 1. The two binaries are the same build

```
/Users/ewan/.local/bin/uw -> /Users/ewan/printing-press/library/unusual-whales/unusual-whales-pp-cli
/Users/ewan/printing-press/library/unusual-whales/
  ├── unusual-whales-pp-cli       (62.7 MB, 2026-05-27 11:48)   ← the `uw` CLI
  ├── unusual-whales-pp-cli-mcp   (64.5 MB, 2026-05-27 11:48)   ← the MCP server in .mcp.json
  ├── cmd/  internal/  go.mod  go.sum                            ← single shared source tree
  └── PARITY.md
```

`PARITY.md` headline: *"one Go binary tree … exposing the same 61 tools, plus an MCP wrapper that **shells out to the CLI**. All 61 tools exist with a 1:1 mapping. Parameters and the core analytical math … reproduce the Python exactly."*

Consequence: the MCP server is a thin stdio adapter over the CLI. There is no second implementation to drift from. The CLI **is** the engine; the MCP is one of its two faces.

### Intentional envelope (shared by both faces)

Both emit `{"source": <parquet path>, <param echoes>, "results": [...]}` (or a bare object for single-symbol analytics). Empty/error payloads are structured `{error|note: …}`. Enum params (`direction`, `mode`, `option_type`, `side`, `sort_by`, `signal_type`, `min_tier`) are JSON-Schema-validated and reject invalid values — in both faces.

---

## 2. The mechanical mapping rule

```
mcp__uw-pp__<group>_<subcommand>   →   uw <group> <subcommand> [--flags …] --json
```

- **Group token** (`dark_pool`, `hot_chains`, `options_flow`, `options_structure`) → hyphenated CLI group (`dark-pool`, `hot-chains`, `options-flow`, `options-structure`). Single-word groups unchanged (`historical`, `insights`, `oi`, `playbook`, `risk`, `screener`, `watchlist`).
- **Subcommand** → underscores become hyphens (`sweep_persistence` → `sweep-persistence`).
- **Arguments**: MCP schema keys == CLI flags **verbatim** (both kebab-case). `dte-max`, `lookback-days`, `min-score`, `top-n`, `signal-type`, `symbol`, `include-zero-gamma`, …
- **`--json` is mandatory on the CLI** — the CLI defaults to a rendered table; the MCP defaults to JSON. Add `--json` (or `--csv`/`--compact`/`--select` for token thrift) on every migrated call.

The full 61-row table with each tool's domain flags is in **`mcp-to-cli-mapping.tsv`**. Per-group summary:

| Group | Tools | CLI prefix |
|---|---|---|
| dark-pool | block-stratified, extended-hours, largest, price-levels, ticker-summary | `uw dark-pool …` |
| historical | available-dates, cumulative-premium-flow, gex-time-series, iv-percentile-zscore, oi-trend, pc-ratio-zscore, signal-backtest, trend, vrp | `uw historical …` |
| hot-chains | most-active, multileg, smart-money-flow, sweep-persistence, sweep-ratio | `uw hot-chains …` |
| insights | analyst-vs-flow, conviction-matrix, deep-dive, earnings-play, institutional-accumulation, price-vs-flow, signal-confluence | `uw insights …` |
| oi | biggest-increases, decrease-with-volume, opex-concentration, pin-risk, position-rolls, smart-positioning | `uw oi …` |
| options-flow | dte-volume-share, expiry-heatmap, greek-screener, iv-outliers, sector-flow, sector-flow-persistence, sweeps, top-premium-trades, unusual-volume | `uw options-flow …` |
| options-structure | dex, front-end-iv-ratio, gex, iv-term-structure, term-skew, today-gamma-flip, vanna-charm | `uw options-structure …` |
| playbook | batch-scan, daily-synthesis, suggest-strategy | `uw playbook …` |
| risk | market-regime, portfolio-correlation | `uw risk …` |
| screener | bullish-bearish, earnings-catalyst, iv-rank, put-call-extremes *(deprecated)*, volume-vs-average | `uw screener …` |
| watchlist | alerts, manage, scan | `uw watchlist …` |

---

## 3. Argument-name reconciliation (prose ≠ real flag)

The command/agent **prose** uses some loose snake_case names that do **not** match the real tool parameter. These mismatches already exist under MCP (the prose is informal); they must be resolved to the **real flag** when writing explicit `uw` calls. Found while auditing:

| Command prose says | Tool | Real MCP key / CLI flag | Note |
|---|---|---|---|
| `historical_oi_trend(lookback_days=5)` | historical oi-trend | `--days` | oi-trend has **no** `lookback-days`; window is `--days`. |
| `historical_signal_backtest(signal_class=…)` | historical signal-backtest | `--signal-type` | calibration-audit Phase 2 prose; flag is `signal-type`. |
| `screener_volume_vs_average(min_ratio=3)` | screener volume-vs-average | `--min-volume-ratio` | |
| `insights_institutional_accumulation(lookback_days=5/10)` | insights institutional-accumulation | *(no such param)* | Tool takes only `--date --symbol`. The `lookback_days` is a **prose fiction** — it is ignored/invalid under both faces. Pre-existing latent bug, **not** caused by migration; flag for cleanup. |
| `oi_biggest_increases(min_dte=180)` | oi biggest-increases | `--min-dte` | matches (kebab). |
| `insights_signal_confluence(min_score=…)` | insights signal-confluence | `--min-score` | matches. |

**Action for migration:** when an agent currently passes argument `X` to an MCP tool, pass the **identical** flag `--X` to the CLI. Where the prose name is wrong (table above), use the real flag. None of these are blockers — they are accuracy fixes that improve both the MCP and CLI paths.

---

## 4. Per-command step walkthrough — every tool call → CLI

Reference counts of distinct tool calls: **daily-analysis 58 distinct**, **weekly-analysis 56 distinct**, **calibration-audit 4 distinct**. (Most tools are invoked *inside* the spawned agents, named in each agent's "Tools required" list; the orchestrator itself directly calls the Step 0 / Step 2 / Step 6+ tools.)

### 4.1 `daily-analysis.md`

| Step | Tool call (MCP) | CLI equivalent |
|---|---|---|
| 0.2 Coverage | `historical_available_dates` | `uw historical available-dates --json` |
| 0.3 Briefing | `playbook_daily_synthesis` (date) | `uw playbook daily-synthesis --date $D --json` |
| 0.4 Macro | `risk_market_regime` | `uw risk market-regime --date $D --json` |
| 0.4 | `options_flow_dte_volume_share` | `uw options-flow dte-volume-share --date $D --json` |
| 0.4 | `historical_vrp` | `uw historical vrp --symbol SPY --date $D --json` |
| 0.5 Sector | `options_flow_sector_flow` | `uw options-flow sector-flow --date $D --json` |
| 0.5 | `options_flow_sector_flow_persistence` | `uw options-flow sector-flow-persistence --days 5 --json` |
| 0.6 Funnel | `screener_bullish_bearish` (top 25 each side) | `uw screener bullish-bearish --direction bullish --top-n 25 --date $D --json` (+ `--direction bearish`) |
| 0.6 | `insights_signal_confluence` (min_score=3, top 25 ea dir) | `uw insights signal-confluence --min-score 3 --direction bullish --top-n 25 --date $D --json` (+ bearish) |
| 0.6 | `screener_volume_vs_average` (top 25, min_ratio=3) | `uw screener volume-vs-average --min-volume-ratio 3 --top-n 25 --date $D --json` |
| 0.6 | `screener_iv_rank` (top 25 high + low) | `uw screener iv-rank --mode high --top-n 25 --date $D --json` (+ `--mode low`) |
| 0.7 OPEX | `oi_pin_risk` | `uw oi pin-risk --date $D --json` |
| 0.7 | `oi_opex_concentration` | `uw oi opex-concentration --date $D --json` |
| 1 gamma-flip-tracker | `options_structure_gex` (dte_max=45) | `uw options-structure gex --symbol SPY --dte-max 45 --date $D --json` (per index) |
| 1 | `historical_gex_time_series` | `uw historical gex-time-series --symbol SPY --days 30 --json` |
| 1 | `options_flow_expiry_heatmap` | `uw options-flow expiry-heatmap --date $D --json` |
| 1 | `options_flow_greek_screener` (min_gamma) | `uw options-flow greek-screener --min-gamma <x> --date $D --json` |
| 1 dealer-positioning | `options_structure_dex` | `uw options-structure dex --symbol <T> --dte-max 45 --date $D --json` |
| 1 | `options_structure_vanna_charm` | `uw options-structure vanna-charm --symbol <T> --date $D --json` |
| 1 | `options_structure_front_end_iv_ratio` | `uw options-structure front-end-iv-ratio --symbol <T> --date $D --json` |
| 1 sector-rotation | `historical_cumulative_premium_flow` (--symbol ETF --days 5) | `uw historical cumulative-premium-flow --symbol <ETF> --days 5 --json` |
| 1 | `dark_pool_largest` (--symbol) | `uw dark-pool largest --symbol <ETF> --date $D --json` |
| 1 | `options_flow_sweeps` (--symbol) | `uw options-flow sweeps --symbol <ETF> --date $D --json` |
| 1 opex-pin (cond.) | `oi_pin_risk`, `oi_opex_concentration`, `options_structure_gex` | as above |
| 1 sweep-tracker | `options_flow_sweeps` | `uw options-flow sweeps --top-n 25 --date $D --json` |
| 1 | `hot_chains_sweep_ratio` | `uw hot-chains sweep-ratio --date $D --json` |
| 1 | `hot_chains_smart_money_flow` | `uw hot-chains smart-money-flow --date $D --json` |
| 1 | `hot_chains_sweep_persistence` | `uw hot-chains sweep-persistence --days 5 --json` |
| 1 | `options_flow_top_premium_trades` (top 20) | `uw options-flow top-premium-trades --top-n 20 --date $D --json` |
| 1 | `hot_chains_most_active` | `uw hot-chains most-active --date $D --json` |
| 1 accumulation-hunter | `dark_pool_ticker_summary` (top 30) | `uw dark-pool ticker-summary --top-n 30 --date $D --json` |
| 1 | `dark_pool_largest` (top 25) | `uw dark-pool largest --top-n 25 --date $D --json` |
| 1 | `dark_pool_block_stratified` | `uw dark-pool block-stratified --date $D --json` |
| 1 | `dark_pool_price_levels` | `uw dark-pool price-levels --symbol <T> --date $D --json` |
| 1 | `insights_institutional_accumulation` | `uw insights institutional-accumulation --symbol <T> --date $D --json` |
| 1 | `oi_smart_positioning` | `uw oi smart-positioning --date $D --json` |
| 1 | `historical_oi_trend` (lookback 5 → `--days 5`) | `uw historical oi-trend --symbol <T> --days 5 --json` |
| 1 | `dark_pool_extended_hours` | `uw dark-pool extended-hours --date $D --json` |
| 1 contrarian-scanner | `historical_pc_ratio_zscore` | `uw historical pc-ratio-zscore --symbol <T> --json` |
| 1 | `insights_price_vs_flow` | `uw insights price-vs-flow --symbol <T> --date $D --json` |
| 1 | `options_flow_iv_outliers` | `uw options-flow iv-outliers --date $D --json` |
| 1 | `oi_decrease_with_volume` | `uw oi decrease-with-volume --date $D --json` |
| 1 | `screener_iv_rank` (extreme high) | `uw screener iv-rank --mode high --date $D --json` |
| 1 earnings-scout | `screener_earnings_catalyst` | `uw screener earnings-catalyst --days-until-earnings 14 --date $D --json` |
| 1 | `insights_earnings_play` | `uw insights earnings-play --date $D --json` |
| 1 | `options_structure_iv_term_structure` | `uw options-structure iv-term-structure --symbol <T> --date $D --json` |
| 1 | `options_structure_term_skew` | `uw options-structure term-skew --symbol <T> --date $D --json` |
| 1 | `options_structure_front_end_iv_ratio` | `uw options-structure front-end-iv-ratio --symbol <T> --date $D --json` |
| 1 | `insights_analyst_vs_flow` | `uw insights analyst-vs-flow --symbol <T> --date $D --json` |
| 1 vol-surface-scout | `options_structure_iv_term_structure`, `options_structure_term_skew`, `options_flow_iv_outliers`, `screener_iv_rank` | as above |
| 1 | `historical_iv_percentile_zscore` | `uw historical iv-percentile-zscore --symbol <T> --lookback-days 252 --json` |
| 1 | `options_flow_expiry_heatmap` | as above |
| 1 multileg-strategist | `hot_chains_multileg` | `uw hot-chains multileg --date $D --json` |
| 1 | `options_flow_top_premium_trades` (≥$1M) | `uw options-flow top-premium-trades --date $D --json` (filter premium downstream) |
| 1 | `options_flow_greek_screener` | `uw options-flow greek-screener --date $D --json` |
| 1 leap-positioning-radar | `oi_biggest_increases` (min_dte=180) | `uw oi biggest-increases --min-dte 180 --date $D --json` |
| 1 | `oi_position_rolls` | `uw oi position-rolls --date $D --json` |
| 1 | `historical_oi_trend` (lookback 10 → `--days 10`) | `uw historical oi-trend --symbol <T> --days 10 --json` |
| 1 | `historical_cumulative_premium_flow` (default 90) | `uw historical cumulative-premium-flow --symbol <T> --days 90 --json` |
| 1 | `insights_institutional_accumulation` | as above |
| 1 | `insights_conviction_matrix` | `uw insights conviction-matrix --symbol <T> --date $D --json` |
| 2a quant | `insights_signal_confluence` (per ticker) | `uw insights signal-confluence …` (or per-ticker via screener pull) |
| 2a | `historical_signal_backtest` (per signal class) | `uw historical signal-backtest --signal-type <class> --lookback-days 5 --json` |
| 2a | `historical_cumulative_premium_flow` (30d & 90d) | `uw historical cumulative-premium-flow --symbol <T> --days 30 --json` (+ `--days 90`) |
| 2d risk-monitor | `risk_portfolio_correlation` | `uw risk portfolio-correlation --symbols A,B,C --lookback-days 30 --json` |
| 2d | `risk_market_regime` (confirm, no re-fetch) | `uw risk market-regime --date $D --json` |
| 2d | `watchlist_alerts` | `uw watchlist alerts --group conviction_<yest> --date $D --json` |
| 2d | `watchlist_scan` | `uw watchlist scan --group conviction_<yest> --date $D --json` |
| 2d / 8 | `watchlist_manage(action=add, group=conviction_<date>)` **(MUTATING)** | `uw watchlist manage --action add --group conviction_$D --tickers T1,T2,… --json` |
| 6 | `insights_deep_dive` (top 3) | `uw insights deep-dive --symbol <T> --date $D --json` |
| 6 | `historical_trend` (lookback 10 → `--days 10`) | `uw historical trend --symbol <T> --days 10 --json` |
| 6.5 | `playbook_batch_scan` (full list) | `uw playbook batch-scan --symbols T1,T2,… --date $D --json` |

### 4.2 `weekly-analysis.md`

Same fleet, wired to `covered_dates` / week range. Identical tool→CLI mapping as 4.1, with these week-specific parameterizations:

| Step | Tool call (MCP) | CLI equivalent |
|---|---|---|
| 0.2 | `historical_available_dates` | `uw historical available-dates --json` (filter to `[MONDAY,WEEK_END]`) |
| 0.3 | `risk_market_regime` ×2 (TODAY + covered_dates[0]) | `uw risk market-regime --date $TODAY --json`; `--date $covered0` |
| 0.4 | `historical_vrp` (latest covered) | `uw historical vrp --symbol SPY --date $WEEK_END --json` |
| 0.5 | `options_flow_sector_flow_persistence` (week) | `uw options-flow sector-flow-persistence --days 5 --json` |
| 0.5 | `options_flow_sector_flow` (WEEK_END) | `uw options-flow sector-flow --date $WEEK_END --json` |
| 0.5 | `options_flow_dte_volume_share` (per covered date) | `uw options-flow dte-volume-share --date <d> --json` (loop) |
| 0.6 | `screener_bullish_bearish`, `insights_signal_confluence` (min_score=4), `screener_iv_rank`, `screener_earnings_catalyst`, `screener_volume_vs_average` (min_ratio=3), `hot_chains_sweep_ratio` | as 4.1 with `--date $WEEK_END`; confluence `--min-score 4` |
| 0.7 OPEX (≤7d) | `oi_pin_risk`, `oi_opex_concentration` | as 4.1 |
| 1 | all Phase-1 agent tools (gamma-flip, dealer-positioning, sector-rotation, sweep, accumulation, contrarian, earnings, vol-surface, multileg, leap) | identical CLI forms to 4.1; multi-day tools use `--days`/`--lookback-days` over covered range |
| 2a | `insights_signal_confluence` (min_score=5), `historical_signal_backtest`, `historical_cumulative_premium_flow` (30/90) | `uw insights signal-confluence --min-score 5 …`; rest as 4.1 |
| 2d | `risk_portfolio_correlation`, `risk_market_regime`, `watchlist_alerts`, `watchlist_scan`, `watchlist_manage(add, conviction_week_<ISO>)` **(MUTATING)** | as 4.1, group = `conviction_week_$ISO_WEEK` |
| 6 scorecard | `hot_chains_sweep_persistence`, `historical_oi_trend` (--days 5), `historical_cumulative_premium_flow`, `historical_trend` | as 4.1 |
| 7 | `insights_deep_dive`, `historical_trend` (--days 10), `playbook_batch_scan` | as 4.1 |
| 9 (Step 0 scripts) | `scripts/gex_next_session_backtest.py`, `scripts/zerodte_setup.py` | **already call the CLI** ("via the uw-pp CLI the MCP wraps") — no change |

### 4.3 `calibration-audit.md`

Only 4 distinct tools; all read-only:

| Step | Tool call (MCP) | CLI equivalent |
|---|---|---|
| 0.5 | `historical_available_dates` | `uw historical available-dates --json` |
| Phase 2.1 | `historical_trend` (start_date, lookback=window) | `uw historical trend --symbol <T> --days <window> --json` |
| Phase 2.2 | `historical_signal_backtest` (signal_class → `--signal-type`) | `uw historical signal-backtest --signal-type <class> --lookback-days <window> --json` |
| When-NOT / ad-hoc | `insights_deep_dive` | `uw insights deep-dive --symbol <T> --json` |
| (validation helper) | `scripts/validate_decision.py` | unchanged (already a script) |

> Note: `historical_trend`'s MCP arg in the prose is `start_date` + `lookback_days`; the CLI exposes the **window** as `--days` and uses the latest snapshot as the reference date (PARITY: Go uses the snapshot's own `executed_at`, *more correct* for historical `--date` queries). For a backward window from a fixed report date, pass `--date <report_date> --days <window>`.

---

## 5. Output-equivalence verification (empirical, all 11 groups)

Method: ran each tool via the **MCP tool** and via **`uw … --json`** with identical args + explicit `--date 2026-05-26` for determinism, then `diff <(jq -S .) <(jq -S .)`.

| Group | Tool tested | Result |
|---|---|---|
| historical | `cumulative-premium-flow` (NVDA, 30d) | **byte-IDENTICAL** |
| historical | `signal-backtest` (bullish_flow) | **byte-IDENTICAL** |
| insights | `signal-confluence` (min-score 4) | **byte-IDENTICAL** |
| playbook | `batch-scan` (SPY,QQQ) | **byte-IDENTICAL** |
| watchlist | `manage --action list` | **byte-IDENTICAL** (shared XDG state file) |
| dark-pool | `ticker-summary` (top 5) | identical except 16th–17th-digit float re-serialization (`214.7022453844958` vs `…82`) — same IEEE-754 double |
| oi | `biggest-increases` (min-dte 180) | identical (TLT/PTON/VALE rows match exactly) |
| screener | `bullish-bearish` (top 4) | identical (SPX/MU/SNDK/QQQ, same closes & net_flow) |
| options-flow | `sector-flow-persistence` (5d) | **content identical**; tied `persistence_score` rows come back in a different array order (Go map-iteration randomness *inside the tool* — two consecutive CLI calls differ too) |
| hot-chains | `sweep-persistence` (5d) | content identical (same ticker set + consistency scores) |
| risk | `market-regime` | identical **except** live SPY `current` (748.96 vs 748.98) + `change_30d_pct` — a live quote that ticked between calls |
| options-structure | `gex` (SPY) | `zero_gamma_level` (749.65) + `regime` identical; `total_gex`/`per_strike` scale with the full-precision live spot S (GEX = γ·OI·100·S) → ~0.0001% call-time delta |

### Three equivalence caveats (true under MCP today; carry over unchanged)

1. **Float round-trip.** Numeric fields may differ in the last 1–2 significant digits between the two faces (re-serialization of the same `float64`). Cosmetic; parse to the identical double. Compare with tolerance, never byte-wise, on floats.
2. **Live-quote fields vary by call time.** Tools that fetch a current price (`risk_market_regime` SPY `current`; `options_structure_gex/dex/vanna_charm` `underlying_price` and everything that scales with it; the yfinance-enriched `insights_deep_dive/institutional_accumulation/price_vs_flow/conviction_matrix/analyst_vs_flow/earnings_play`; `historical_vrp`/`historical_trend` price legs) return slightly different numbers on each invocation — **identically in MCP and CLI**. This is *not* a port discrepancy; it is wall-clock. Don't expect cross-tool price consistency within a run.
3. **Non-deterministic array order on ties.** Results backed by a Go map (e.g. `sector-flow-persistence` sectors with equal `persistence_score`) come out in a random array order each call. Consumers must **sort by a key**, never rely on array position. Already true under MCP.

None of the three is introduced or worsened by migrating to the CLI.

---

## 6. What changes, what doesn't

**Changes (mechanical):**
- Each `mcp__uw-pp__X(args)` becomes a `uw … --json` Bash call (add `--json`).
- A `Bash(uw:*)` permission must be allowed in `.claude/settings.json`.
- Agent/command prose that names MCP tools is rewritten to name CLI commands.

**Doesn't change:**
- The analytical math, field names, envelope shape, enum validation.
- Watchlist state (shared XDG file).
- The two helper scripts (`gex_next_session_backtest.py`, `zerodte_setup.py`) — already CLI-backed.
- Downstream JSON parsing / `decision.json` emission / `validate_decision.py`.

**Upside of migrating:**
- Drops the `uw-pp` MCP server process and its tool-schema context cost (61 tool schemas no longer loaded into every agent's context window).
- Bash calls can be **batched** (many `uw` calls in one shell invocation) and **slimmed** with `--select`/`--compact`/`--csv` to cut tokens.
- Single execution surface (Bash) — simpler permissioning, easier logging/replay.

**Risk of migrating:**
- Bash permission prompts if `Bash(uw:*)` isn't allow-listed.
- `uw` must be on `PATH` in every agent session (it is: `/Users/ewan/.local/bin/uw`).
- Loss of structured MCP tool-call telemetry (calls become opaque Bash lines) — mitigate with `--quiet` + consistent `--json`.

See **`cli-migration-plan.md`** for the phased rollout.
