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
| `/daily-analysis` | Full post-market two-phase agent fleet report; conviction scoring + risk gating; saves to `analyses/YYYY-MM-DD.md` |
| `/weekly-analysis` | Full week-in-review + week-ahead note; persistence-weighted rubric; saves to `analyses/weekly/YYYY-WW.md` |
| `/skill-creator` | Create, modify, and evaluate skills; runs evals, benchmarks variance, optimizes trigger descriptions |
| `/prompt-optimize` | Analyze a draft prompt and output an ECC-enriched optimized version ready to use |
| `/eval-harness` | Formal evaluation framework implementing eval-driven development (EDD) principles |
| `/orchestrate` | Sequential and tmux/worktree orchestration patterns for multi-agent workflows |
| `/plan` | Restate requirements, assess risks, create step-by-step implementation plan before touching code |

## Agents

**13 project-local agents** (14 in OPEX week with `opex-pin-strategist`), defined in `.claude/agents/`. Split into Phase 1 alpha-finders (parallel) and Phase 2 scoring + risk (sequential).

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

### Phase 2 — scoring then risk (sequential)

| Agent | Focus |
|---|---|
| `signal-confluence-quant` | Audited per-ticker conviction score — `score_components`, `win_rate`, pre-risk size; runs first |
| `risk-monitor` | Consumes quant output; applies regime / VRP / correlation / sector gate stack; watchlist write-back |

## Commands

Commands live in `.claude/commands/` and invoke the agent fleet:

- `daily-analysis.md` — Orchestrates 11–12 Phase 1 agents in parallel, then Phase 2 sequentially
- `weekly-analysis.md` — Same fleet wired to 5-day persistence metrics and WoW regime delta

## Output

Reports are saved to `analyses/YYYY-MM-DD.md` (daily) and `analyses/weekly/YYYY-WW.md` (weekly).

## MCP Servers Required

All `uw-*` MCP servers must be running (configured globally in `~/.claude.json`).
