# UW Daily Analysis

Post-market daily analysis powered by Unusual Whales MCP data.

## Purpose

Produces a structured daily market intelligence report covering:
- Options flow and sweep activity
- Dark pool institutional positioning
- Market regime and risk
- Contrarian / fade setups
- Earnings plays

## Agents

The fleet is **13 agents** (14 in OPEX week with `opex-pin-strategist`), split into Phase 1 alpha-finders (parallel) and Phase 2 scoring + risk (sequential).

### Phase 1 — alpha-finding (parallel)

| Agent | Focus |
|---|---|
| `sweep-tracker` | Multi-day persistent options sweeps (`multi_day_sweep_persistence` is primary) |
| `accumulation-hunter` | Quiet institutional accumulation via DP + OI; `dp_block_size_stratified` filters retail tier |
| `contrarian-scanner` | Overcrowded fades using `pc_ratio_zscore` (replaces deprecated `put_call_ratio_extremes`); VRP-gated |
| `earnings-scout` | Pre-earnings flow + vol plays anchored to term-structure kink + `term_skew` + `front_end_iv_ratio` |
| `gamma-flip-tracker` | Today's 0DTE / intraday gamma map only (`today_gamma_flip` primary) |
| `dealer-positioning-strategist` | Swing-horizon dealer flows (DEX, vanna, charm, GEX time series) — 1–4 week setups |
| `multileg-strategist` | Institutional spread inference; term-structure-anchored play type; multi-day repeat count |
| `vol-surface-scout` | Vol-surface dislocations; `iv_percentile_zscore` + VRP bias |
| `leap-positioning-radar` | DTE > 180 institutional builds; `cumulative_premium_flow` accretion gate; 6-of-9 gates |
| `sector-rotation-strategist` | Multi-week sector rotation with single-name leaders; ≥3-day persistence required |
| `opex-pin-strategist` | OPEX-week-only pin mechanics; ranked book with `suggested_structure` (iron flies, short straddles) |

### Phase 2 — scoring + risk (sequential)

| Agent | Focus |
|---|---|
| `signal-confluence-quant` | Audited per-ticker conviction score with `score_components`, `dominant_signal_class`, `win_rate`, pre-risk size |
| `risk-monitor` | Regime / VRP / panic / correlation / sector gate stack; watchlist write-back |

## Commands

- `/daily-analysis` — Run full post-market report and save to `analyses/YYYY-MM-DD.md`
- `/weekly-analysis` — Run full Friday-evening / Sunday-prep weekly note and save to `analyses/weekly/YYYY-WW.md`

## Output

Reports are saved to `analyses/YYYY-MM-DD.md` for historical reference.

## MCP Servers Required

All `uw-*` MCP servers must be running (configured globally in `~/.claude.json`).
