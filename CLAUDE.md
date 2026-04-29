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

Five specialist agents run in parallel for each report:

| Agent | Focus |
|---|---|
| `sweep-tracker` | Aggressive options sweeps, smart money momentum |
| `accumulation-hunter` | Quiet institutional accumulation via dark pool + OI |
| `contrarian-scanner` | Overcrowded positions, fade setups |
| `earnings-scout` | Pre-earnings flow and vol plays |
| `risk-monitor` | Regime, correlation clusters, adverse flow |

## Commands

- `/daily-analysis` — Run full post-market report and save to `analyses/`

## Output

Reports are saved to `analyses/YYYY-MM-DD.md` for historical reference.

## MCP Servers Required

All `uw-*` MCP servers must be running (configured globally in `~/.claude.json`).
