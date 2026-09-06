# CLI Migration — Verification Record (2026-05-27)

Migration executed per `cli-migration-plan.md`. This file records the post-migration
verification against the criteria set for the task.

## What was migrated

All `mcp__uw-pp__*` tool references in `.claude/commands/*.md` (3 commands) and
`.claude/agents/*.md` (15 agents with UW tools) were mechanically rewritten to the
`uw <group> <subcommand> … --json --quiet` CLI form, driven by the 61-row
`mcp-to-cli-mapping.tsv`. Scripts in `analyses/audit/2026-05-27/`:

- `migrate_mcp_to_cli.py` — token swap (prefixed `mcp__uw-pp__X` + bare snake_case names); 537 references.
- `fix_mcp_prose.py` — 18 data-path "MCP" → "CLI" prose fixes.
- `fix_flag_hints.py` / `fix_call_notation.py` — 35 arg-name / function-call-notation corrections.

A "Data access — the `uw` CLI" convention block was added to all 3 command files;
the `Bash(uw:*)` permission was added to `.claude/settings.json`.

## Criterion 1 — all commands use the CLI

```
grep -rn 'mcp__uw-pp__' .claude/commands .claude/agents | grep -v 'mcp__uw-pp__\*'  → 0
```
- 0 residual `mcp__uw-pp__` tool references in commands + agents.
- 0 residual function-call notation `uw <grp> <sub>(args)`.
- All 61 distinct `uw <group> <sub>` invocations referenced validate against the TSV (61/61, 0 malformed).
- The remaining `mcp__uw-pp__*` strings are the permission wildcard in `settings.json` /
  `settings.local.json` and the doc file `PERMISSIONS_AUDIT.md` — not tool calls.

## Criterion 2 — same results as yesterday's run (data date 2026-05-26)

The migration changes only the **data front-end**. Verified by re-pulling, via the CLI,
the exact data anchors that `analyses/daily/2026-05-26/{report.md,decision.json}` was
built on, and the deterministic script spine that emits the envelope fields.
(A full agent-fleet re-run is not a clean migration test — LLM synthesis is non-deterministic
even on identical data; the audit already proved CLI⇄MCP byte-equivalence across all 11 groups.)

| Anchor | Recorded (MCP-path, 05-26) | CLI re-pull (05-26) | Result |
|---|---|---|---|
| Regime (base) | `TRANSITIONAL` | `TRANSITIONAL` | ✅ exact |
| Breadth bullish_pct | 40.1 | 40.1 | ✅ exact |
| VRP regime | `FAIR` | `FAIR` (vrp 0.0418) | ✅ exact |
| GEX SPY zero_gamma_level | 749.65 | 749.65 | ✅ exact |
| GEX SPY regime | POSITIVE | POSITIVE | ✅ exact |
| GEX SPY total_gex | 1065635926 | 1065635926 | ✅ byte-identical |
| GEX SPY spot | 750.24 | 750.24 | ✅ exact |
| GEX SPY call_wall (derived) | 751 | 751 | ✅ exact |
| GEX SPY put_wall (derived) | 730 | 730 | ✅ exact |
| 0DTE setup SPY (vix/IM/range/structure/entry) | vix 16.94, IM 0.76, range 0.74 | identical | ✅ byte-identical |
| Candidate universe (14 called tickers) | — | 12/14 in core funnel; AVGO, CRDO reachable via vol-surface `term-skew` | ✅ reproduced |
| `validate_decision.py --file …/2026-05-26/decision.json` | — | `OK … validates (14 calls)` | ✅ pass |

**Conclusion:** the migrated CLI commands feed the pipeline byte-identical data and the
deterministic envelope spine (`zerodte_setup.py`, GEX, validator) reproduces exactly.
Migration is result-preserving.

## Criterion 4 — migration coverage

100% of `mcp__uw-pp__*` tool calls in the commands + agents migrated (0 residual).
Well above the 95% threshold → decommission authorized (see `decommission` section in this folder's README / Phase 5 edits).
