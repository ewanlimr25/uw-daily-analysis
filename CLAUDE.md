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
| `sector-rotation-strategist` | Multi-week rotation regime calls with single-name leaders; enforces ≥3-day `options_flow_sector_flow_persistence` |
| `opex-pin-strategist` | OPEX-week-only pin mechanics; ranked gamma-weighted book with iron flies, straddles, butterflies |

### Phase 2 — scoring → fundamentals → debate → risk (sequential)

| Agent | Stage | Focus |
|---|---|---|
| `signal-confluence-quant` | 2a | Audited per-ticker conviction score — `score_components`, `win_rate`, pre-risk size; runs first |
| `fundamentals-gate` | 2b | Finnhub cross-check on top-5 (earnings-surprise streak, insider MSPR, leverage, news catalysts); CONFIRM / CAUTION / VETO vs the flow thesis — catches distribution dressed as accumulation |
| `bull-researcher` / `bear-researcher` | 2c | Bounded 1–2 round adversarial debate on top-5; honest residual confidence; the disconfirmation the additive score lacks |
| `risk-monitor` | 2d | Consumes quant + fundamentals + debate; applies regime / VRP / correlation / sector / fundamentals / event-risk / debate gate stack; watchlist write-back |

## Scripts & schemas

Stdlib-only Python helpers in `scripts/` (no pip installs; run via the already-allowed `Bash(python3:*)`). Keys resolve via `scripts/_env.py`: env → repo `.env` → sibling fallback (the Finnhub key stays in `claude-trading-agents/.env`).

- `scripts/fred_macro.py` — FRED macro snapshot (12 series + derived signals) for Step 0 `macro_snapshot`. Needs `FRED_API_KEY` (free).
- `scripts/finnhub_enrich.py` — per-ticker fundamentals for the `fundamentals-gate` agent. Falls back to the sibling repo's `FINNHUB_API_KEY`.
- `scripts/validate_decision.py` — validates the decision envelope against `schemas/decision_envelope.schema.json` + cross-field invariants (Σ component points == raw_score; tier ≤ score band; VETO ⇒ skip).
- Tests: `python3 -m unittest discover -s scripts/tests -p 'test_*.py'`.

## Commands

Commands live in `.claude/commands/` and invoke the agent fleet:

- `daily-analysis.md` — Orchestrates 11–12 Phase 1 agents in parallel, then Phase 2 (quant → fundamentals → debate → risk) sequentially; emits a `decision.json` envelope and optionally hands the top-2 to `/stock-deep-dive`
- `weekly-analysis.md` — Same fleet wired to 5-day persistence metrics and WoW regime delta

## Output

Each report gets its own per-id run folder holding two generically-named files: `analyses/daily/YYYY-MM-DD/{report.md, decision.json}` (daily) and `analyses/weekly/YYYY-WW/{report.md, decision.json}` (weekly). The `decision.json` is the machine-resolvable envelope, validated against `schemas/decision_envelope.schema.json` and consumed by `/calibration-audit` Phase 1 (its `report_path` field points at the sibling `report.md`). Audit checkpoints stay under `analyses/audit/YYYY-MM-DD/`.

## MCP Server Required

All Unusual Whales data is served by a **single consolidated MCP server, `uw-pp`**, defined in `.mcp.json`. It bundles into one binary the capabilities previously split across multiple `uw-*` servers (dark pool, historical, hot chains, insights, OI, options flow, options structure, playbook, risk, screener, watchlist) — this is faster and cheaper on tokens than running them as separate processes.

Tools are namespaced `mcp__uw-pp__<tool>`, where `<tool>` keeps its domain prefix (e.g. `mcp__uw-pp__dark_pool_block_stratified`, `mcp__uw-pp__options_flow_sector_flow_persistence`, `mcp__uw-pp__historical_signal_backtest`). Access is granted via the `mcp__uw-pp__*` permission in `.claude/settings.json`.
