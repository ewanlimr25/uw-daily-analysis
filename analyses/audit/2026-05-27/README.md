# Audit — `uw` CLI ⇄ `mcp__uw-pp__*` migration (2026-05-27)

Audit of whether the new `uw` CLI can replace the `mcp__uw-pp__*` MCP tools across all three repo commands, with output-equivalence verification and a migration plan.

| File | What's in it |
|---|---|
| `cli-migration-audit.md` | **Main deliverable.** Same-binary proof, the 1:1 mapping rule, argument reconciliation, per-command step-by-step tool→CLI walkthrough (daily / weekly / calibration), and the 11-group equivalence verification with caveats. |
| `cli-migration-plan.md` | Phased migration plan (Phase 0 prereqs → Phase 5 decommission), call convention, rollback, effort/risk table. |
| `mcp-to-cli-mapping.tsv` | Machine-readable 61-row table: `MCP_TOOL → CLI_COMMAND` + each tool's domain flags. |
| `verification-evidence.txt` | Recorded normalized-diff results backing the "verified identical" claim (pre-migration). |
| **`migration-verification.md`** | **Post-migration verification** (what was migrated, criteria 1/2/4 evidence, the 2026-05-26 data-anchor A/B table). |
| **`behaviors-off.md`** | **Anomalies found** (criterion 3) — chiefly the `institutional-accumulation` fiction `lookback_days` param; + informational field-shape notes. |
| `migrate_mcp_to_cli.py`, `fix_mcp_prose.py`, `fix_flag_hints.py`, `fix_call_notation.py` | The deterministic migration scripts (TSV-driven token swap + prose/flag/notation corrections). Re-runnable; auditable. |

## Execution status (2026-05-27)

**DONE.** All 4 phases executed. `mcp__uw-pp__*` tool references in the 3 commands + 15 agents → `uw` CLI (537 token swaps + 53 prose/flag/notation fixes); 61/61 generated `uw <group> <sub>` forms validate against the TSV; 0 residual tool refs in commands/agents. Data-anchor A/B vs the 2026-05-26 baseline reproduces exactly (GEX byte-identical, VRP/regime/0DTE exact; `validate_decision.py` passes; 171 script tests green). Migration coverage **100% (> 95%)** → the `uw-pp` MCP server was **unregistered** from `.mcp.json` and `mcp__uw-pp__*` removed from `.claude/settings.json` (`Bash(uw:*)` added). `mcp__yahoo-finance__*` retained. One inert residual: `mcp__uw-pp__*` still in `.claude/settings.local.json` (auto-mode guardrail blocks editing that file — needs a one-line manual removal; harmless, matches nothing).

## Bottom line

The `uw` CLI and the `uw-pp` MCP are **the same Go binary tree** (the MCP shells out to the CLI). All **61 tools map 1:1**, arguments are **identical kebab-case flags**, and output is **equivalent** across all 11 server groups (byte-identical for pure-parquet tools; live-quote and tied-order differences are wall-clock/sort artifacts present in *both* faces, not port discrepancies). The one mutating op — watchlist write-back — shares a single XDG state file across both faces, so migration needs **zero data migration**. Migration is a mechanical front-end swap: `mcp__uw-pp__X(args)` → `uw <group> <sub> --flags --json --quiet`.

**Coverage:** all 57 distinct tools used by the 3 commands are tied to a CLI call; 12 tools across all 11 groups empirically diff-verified.
