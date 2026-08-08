# UW Daily Analysis

Post-market daily analysis powered by Unusual Whales MCP data.

## Purpose

Produces a structured daily market intelligence report covering:
- Options flow and sweep activity
- Dark pool institutional positioning
- Market regime and risk
- Contrarian / fade setups
- Earnings plays

## Skills

User-invocable via `/skill-name`. Core skills for this project:

| Skill | Purpose |
|---|---|
| `/daily-analysis` | Full post-market two-phase agent fleet report; conviction scoring + risk gating; saves to `analyses/daily/YYYY-MM-DD/report.md` |
| `/weekly-analysis` | Full week-in-review + week-ahead note; persistence-weighted rubric; saves to `analyses/weekly/YYYY-WW/report.md` |
| `/skill-creator` | Create, modify, and evaluate skills; runs evals, benchmarks variance, optimizes trigger descriptions |
| `/prompt-optimize` | Analyze a draft prompt and output an ECC-enriched optimized version ready to use |
| `/eval-harness` | Formal evaluation framework implementing eval-driven development (EDD) principles |
| `/orchestrate` | Sequential and tmux/worktree orchestration patterns for multi-agent workflows |
| `/plan` | Restate requirements, assess risks, create step-by-step implementation plan before touching code |

## Agents

**16 project-local agents** (17 in OPEX week with `opex-pin-strategist`), defined in `.claude/agents/`. Split into Phase 1 alpha-finders (parallel) and Phase 2 scoring → fundamentals → debate → risk (sequential).

### Phase 1 — alpha-finding (parallel)

| Agent | Focus |
|---|---|
| `sweep-tracker` | Aggressive options sweeps and smart money flow for short-term directional momentum |
| `accumulation-hunter` | Quiet institutional accumulation via DP prints + OI buildup; `dark_pool_block_stratified` gates out retail |
| `contrarian-scanner` | Overcrowded fades via `historical_pc_ratio_zscore` + flow divergence from price; aborts in negative VRP |
| `earnings-scout` | Earnings plays via IV term-structure kink + `options_structure_term_skew` + `options_structure_front_end_iv_ratio` + flow alignment |
| `gamma-flip-tracker` | Today's 0DTE/intraday gamma map only — zero-gamma level, regime, per-strike walls; NOT for swing |
| `dealer-positioning-strategist` | Swing-horizon (1–4wk) DEX trajectory, vanna/charm exposure, GEX time series; NOT for 0DTE |
| `multileg-strategist` | Institutional spread structure inference; play type anchored to term-structure; multi-day repeat filter |
| `vol-surface-scout` | Vol-surface dislocations — KINKED/BACKWARDATION names, IV outliers, skew mispricings, VRP bias |
| `leap-positioning-radar` | DTE > 180 institutional builds; `historical_cumulative_premium_flow` accretion gate; requires 6-of-9 signal gates |
| `sector-rotation-strategist` | Multi-week rotation regime calls with single-name leaders. **Direction reads off the NETTED `uw risk market-regime.sector_rotation` (2026-08-01 C55)**; `options_flow_sector_flow_persistence` is a durability filter only — it and `sector-flow` are one *gross-turnover* source and cannot express direction. Netted-vs-gross disagreement ⇒ watch_only |
| `opex-pin-strategist` | OPEX-week-only pin mechanics; ranked gamma-weighted book with iron flies, straddles, butterflies |

### Phase 2 — scoring → fundamentals → debate → risk (sequential)

| Agent | Stage | Focus |
|---|---|---|
| `signal-confluence-quant` | 2a | Audited per-ticker conviction score — `score_components`, `win_rate`, pre-risk size; runs first |
| `fundamentals-gate` | 2b | Finnhub cross-check on top-5 (earnings-surprise streak, insider MSPR, leverage, news catalysts); CONFIRM / CAUTION / VETO vs the flow thesis — catches distribution dressed as accumulation |
| `bull-researcher` / `bear-researcher` | 2c | Bounded 1–2 round adversarial debate on top-5; honest residual confidence; the disconfirmation the additive score lacks |
| `risk-monitor` | 2d | Consumes quant + fundamentals + debate; applies regime / VRP / correlation / sector / fundamentals / event-risk / debate gate stack; watchlist write-back. **Directional SHORTs route to `watch_only` and are never sized (2026-08-01 P0 #1)** — routing, not suppression: theses are still generated, scored and serialized so the counterfactual keeps resolving. Hedge legs / defined-risk spreads / short-vol structures are out of scope |

## Scripts & schemas

Stdlib-only Python helpers in `scripts/` (no pip installs; run via the already-allowed `Bash(python3:*)`). Keys resolve via `scripts/_env.py`: env → repo `.env` → sibling fallback (the Finnhub key stays in `claude-trading-agents/.env`).

- `scripts/fred_macro.py` — FRED macro snapshot (12 series + derived signals) for Step 0 `macro_snapshot`. Needs `FRED_API_KEY` (free).
- `scripts/finnhub_enrich.py` — per-ticker fundamentals for the `fundamentals-gate` agent. Falls back to the sibling repo's `FINNHUB_API_KEY`.
- `scripts/fz_enrich.py` — per-ticker short-interest / float / analyst context via the `fz` CLI (see below) for the `fundamentals-gate` agent. No key. Advisory (0 rubric points); graceful-skips when `fz` is unavailable.
- `scripts/step0_cache.py` — fetches the ~22 market-wide `uw` payloads once per run into `analyses/daily/<date>/step0_cache/`; agents read the cached paths instead of re-issuing the commands (a measured 528KB duplicate on 2026-07-24).
- `scripts/market_data.py` — raw Yahoo chart API OHLCV for the **C12 liquidity floor** (price ≥ $5, 20d dollar ADV ≥ $50M), the cap-weighted-vs-equal-weight tape check, and realized vol. The `uw` CLI has no OHLC or share-volume source.
- `scripts/dex_flip.py` — the mechanized +1 DEX sign-flip rubric line (2026-06-12 P0.4); emits a rubric-ready evidence string plus a whipsaw warning.
- `scripts/term_structure_hygiene.py` — re-derives IV term structure after dropping the 0DTE bucket and thin tenors (raw label was BACKWARDATION on 39/41 names on 2026-07-24; 14 flipped).
- `scripts/validate_decision.py` — validates the decision envelope against `schemas/decision_envelope.schema.json` + cross-field invariants (Σ component points == raw_score; tier ≤ score band; VETO ⇒ skip).
- Tests: `python3 -m unittest discover -s scripts/tests -p 'test_*.py'`.

## Commands

Commands live in `.claude/commands/` and invoke the agent fleet:

- `daily-analysis.md` — Orchestrates 11–12 Phase 1 agents in parallel, then Phase 2 (quant → fundamentals → debate → risk) sequentially; emits a `decision.json` envelope and optionally hands the top-2 to `/stock-deep-dive`
- `weekly-analysis.md` — Same fleet wired to 5-day persistence metrics and WoW regime delta

## Output

Each report gets its own per-id run folder holding two generically-named files: `analyses/daily/YYYY-MM-DD/{report.md, decision.json}` (daily) and `analyses/weekly/YYYY-WW/{report.md, decision.json}` (weekly). The `decision.json` is the machine-resolvable envelope, validated against `schemas/decision_envelope.schema.json` and consumed by `/calibration-audit` Phase 1 (its `report_path` field points at the sibling `report.md`). Audit checkpoints stay under `analyses/audit/YYYY-MM-DD/`.

## CLI Required (`uw`)

All Unusual Whales data is served by the **`uw` CLI** — a single Go binary at `/Users/ewan/.local/bin/uw` (override with `$UW_PP_CLI`). It exposes the same 61 tools previously reached through the `uw-pp` MCP server (dark pool, historical, hot chains, insights, OI, options flow, options structure, playbook, risk, screener, watchlist); in fact the now-retired MCP server was just a stdio wrapper that shelled out to this CLI. Migrated 2026-05-27 (see `analyses/audit/2026-05-27/`): dropping the MCP server stops loading 61 tool schemas into every agent's context.

Invoke via Bash with the canonical convention:

```
uw <group> <subcommand> [--flag value …] --json --quiet
```

`--json` is mandatory (the CLI defaults to a rendered table); `--quiet` keeps stdout pure JSON. Commands are the mechanical 1:1 of the old tool names: `mcp__uw-pp__<group>_<sub>` → `uw <group-hyphenated> <sub-hyphenated>` (e.g. `uw dark-pool block-stratified`, `uw options-flow sector-flow-persistence`, `uw historical signal-backtest`). Access is granted via the `Bash(uw:*)` permission in `.claude/settings.json`. Trim payloads with `--select`/`--compact`. The mutating `uw watchlist manage` shares the same XDG state file (`~/.config/unusual-whales-pp-cli/watchlist.json`) the MCP used.

Fundamentals enrichment still uses the **yfinance MCP** (`mcp__yahoo-finance__*`), which remains in `.mcp.json`.

## CLI (`fz`) — non-flow context augment

Non-flow context the UW microstructure fleet is structurally blind to — **short interest, days-to-cover, float, institutional/analyst positioning, market breadth, insider clusters** — comes from the **`fz` CLI** (`finviz-pp-cli`, Go binary at `/Users/ewan/.local/bin/fz`; override with `$FZ_PP_CLI`). Free, no-auth public Finviz HTTP. Invoke via Bash as `fz <group> <sub> … --agent` (`--agent` = `--json --compact --no-input --no-color --yes`). Added 2026-05-27 (see `analyses/audit/2026-05-27-fz-edge/`).

**Scope discipline:** `fz` adds **zero** options flow / greeks / dark pool / IV term-structure / GEX/DEX / OI — it cannot replace any `uw` tool; it augments *beside* the flow engine. Every `fz` lane is **advisory (0 rubric points)** and **graceful-skips** if the binary is missing (the report completes unchanged). Short interest is the exchange semi-monthly settlement figure (~2-week lag) — squeeze context, not a live borrow signal; no borrow-fee/HTB field. Scored-gate promotions are registered as criteria **C15–C18** and stay advisory until `/calibration-audit` clears each threshold. Access requires a `Bash(fz:*)` permission in `.claude/settings.json`.

## `uw options-flow single-leg` — single-leg whale tier scan

`uw options-flow single-leg --regime <bull|bear|neutral> [--option-type put] --json --quiet`
grades clean single-leg, ask-side, ≥$500K, common-stock **opening** prints by the
backtested Signal Quality Hierarchy: **Tier-1 opening/floor PUT (size/OI≥2 or
floor, DTE≤30)** is the validated edge (next-session WR 61–64%, +23–26pp vs SPY,
p<0.001, bull regime); calls are beta (−9.7pp); `size/OI<0.5` is a closing
anti-signal. **Advisory, 0 rubric points — permanently, unless a NEW criterion is
registered.** The old accrual criterion **C19 was CLOSED as REFUTED on 2026-07-25**
(register C53): six audits carried "`bearish_flow` shows positive excess but scores 0"
as an unscoreable down-tape edge, and Phase 3d showed the excess swing was the
**benchmark**, not the book — `bearish_flow` books 0.533 up-tape / 0.526 down-tape
(stationary), realises 0.49 vs a 0.48 claim on n=94 (p=0.96, the best-calibrated large
class in the book), and its down-tape paired McNemar is ns (p=0.2478). **This does not
refute the 2026-05-29 backtest above** — that was a different measurement on a different
substrate (raw single-print Parquet rows graded next-session, not scored fleet calls
graded on a path-aware 0.5-ATR window). The scan stays live and useful as context; it is
simply no longer accruing toward a scored line. Built into the `uw` Go binary
(`internal/analysis/singleleg.go` + `internal/cli/single_leg.go`). The research /
backtest harness remains `scripts/single_leg_whale.py`. See
`analyses/audit/2026-05-29/single_leg_whale_implementation_plan.md`.
