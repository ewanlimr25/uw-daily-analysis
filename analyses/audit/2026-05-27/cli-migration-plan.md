# Migration Plan — `mcp__uw-pp__*` → `uw` CLI

**Date:** 2026-05-27
**Companion:** `cli-migration-audit.md` (mapping + verification), `mcp-to-cli-mapping.tsv` (61-tool table)

The audit established that the CLI and MCP are the **same binary tree** (MCP shells out to the CLI), tools map **1:1**, arguments are **identical kebab-case flags**, and output is **equivalent** (verified across all 11 groups). Migration is therefore a mechanical front-end swap with a small, well-bounded blast radius. This plan sequences it to keep `/daily-analysis`, `/weekly-analysis`, and `/calibration-audit` green at every step.

---

## Guiding decisions

1. **Run both faces in parallel during transition.** Do *not* remove the `uw-pp` MCP server from `.mcp.json` until the final phase. Each migrated agent/step can be A/B'd against the MCP path on the same date.
2. **One canonical call convention** (mirrors the proven `scripts/gex_next_session_backtest.py:_run_cli`):
   ```bash
   uw <group> <sub> [--flag value …] --json --quiet
   ```
   `--json` (CLI defaults to a table), `--quiet` (drop banners/progress so stdout is pure JSON). Parse with `jq`/`json.loads`. Honour a `UW_PP_CLI` / `PATH` override (`uw` resolves to `/Users/ewan/.local/bin/uw`).
3. **Token thrift, opt-in.** Add `--select <dotted,paths>` or `--compact` once a step is migrated and its output shape is known — this is the migration's main *upside* (the MCP can't trim like this without loading the whole result).
4. **Sort, never index.** Where a step consumes a list with tie-prone ordering (`sector-flow-persistence`, any `--top-n` with score ties), sort by an explicit key — Go map order is non-deterministic in both faces.
5. **Floats with tolerance.** A/B comparisons compare floats with tolerance (≥1e-6 rel) and **exclude live-quote fields** (regime SPY `current`; gex/dex/vanna `underlying_price` + scaled fields; yfinance `insights_*`; `vrp`/`trend` price legs) which legitimately tick by wall-clock — see audit §5 caveat 2.

---

## Phase 0 — Prerequisites (no behavior change)

| Task | Detail |
|---|---|
| **P0.1 Permission** | Add `"Bash(uw:*)"` to `.claude/settings.json` `allow` (currently: `mcp__uw-pp__*`, `mcp__yahoo-finance__*`, `WebSearch`, `Skill(stock-deep-dive)`). Keep `mcp__uw-pp__*` for now. |
| **P0.2 PATH check** | Confirm `uw` resolves in a spawned-agent shell: `command -v uw` → `/Users/ewan/.local/bin/uw`. Document the `UW_PP_CLI` fallback for agents that prefer the absolute binary. |
| **P0.3 Smoke test** | `uw historical available-dates --json --quiet` returns valid JSON; date coverage matches the MCP `historical_available_dates`. |
| **P0.4 A/B harness** | Add `scripts/ab_compare.py` (stdlib): given a tool + args, run the CLI and (optionally) the recorded MCP output, normalize (jq -S, sort tie-prone arrays, float-tolerance, drop live-quote fields), assert equivalence. Reuse the `_run_cli` shape already in `gex_next_session_backtest.py`. |

**Exit:** `uw` is allow-listed and smoke-tested; A/B harness green on the 12 tools spot-checked in the audit.

---

## Phase 1 — Pilot: orchestrator-direct Step 0 calls (lowest risk)

The Step 0 preflight in both `/daily-analysis` and `/weekly-analysis` is run **by the orchestrator itself** (it already shells `python3 scripts/*.py` there), so these are the easiest to move and the highest-leverage (every agent consumes their output).

Migrate these **read-only** calls to `uw`:
- `historical available-dates`, `risk market-regime`, `options-flow dte-volume-share`, `historical vrp`, `options-flow sector-flow`, `options-flow sector-flow-persistence`, `playbook daily-synthesis`, and the four funnel screens (`screener bullish-bearish`, `insights signal-confluence`, `screener volume-vs-average`, `screener iv-rank`), plus the OPEX-guard `oi pin-risk` / `oi opex-concentration`.

**How:** edit the Step 0 prose in `daily-analysis.md` / `weekly-analysis.md` to specify the `uw … --json --quiet` invocation in place of each `mcp__uw-pp__*` reference. Keep the JSON-context block shape (`{date, regime, …}`) byte-identical so Phase 1 agents need no change yet.

**Validate:** run `/daily-analysis` for a recent date with Phase 1 on the MCP path; confirm the Step 0 context block is equivalent to a prior MCP-only run (regime label, sector persistence, funnel tickers). Diff the resulting `decision.json` top-level fields.

**Exit:** Step 0 fully on CLI; one clean daily report produced; `validate_decision.py` passes.

---

## Phase 2 — Phase-1 agents, group by group (read-only)

Each of the 11 alpha-finding agents names its tools in a "Tools required" list inside `.claude/agents/<agent>.md`. Migrate those lists to CLI invocations. **Order by blast radius (smallest first):**

| Wave | Agents | Groups touched | Why this order |
|---|---|---|---|
| 2a | `sweep-tracker`, `accumulation-hunter` | hot-chains, options-flow, dark-pool, oi | Pure-parquet, deterministic; dark-pool/oi verified byte-identical. |
| 2b | `contrarian-scanner`, `vol-surface-scout` | historical, options-flow, options-structure, screener | historical verified identical; options-structure has the live-S caveat (ZGL stable). |
| 2c | `multileg-strategist`, `sector-rotation-strategist` | hot-chains, options-flow, dark-pool, historical | sector-rotation's ETF tape already loops `historical cumulative-premium-flow` per symbol — natural CLI batch. |
| 2d | `gamma-flip-tracker`, `dealer-positioning-strategist` | options-structure, historical, options-flow | Live-S fields (`underlying_price`, `total_gex`) — apply float-tolerance + don't cross-compare price. ZGL/regime verified stable. |
| 2e | `earnings-scout`, `leap-positioning-radar` | screener, insights, options-structure, oi, historical | insights tools blend yfinance (live) — verify *structure* not exact price. |
| 2f | `opex-pin-strategist` (conditional) | oi, options-structure | Only in OPEX week; migrate last. |

**Per-agent procedure:**
1. Rewrite the "Tools required" list to CLI form (from the audit §4 table / mapping TSV).
2. Add the canonical convention note (`--json --quiet`, sort tie-prone arrays).
3. Spawn the agent on CLI; A/B its surfaced candidate set against an MCP-path run on the same date — **candidate tickers and signal classes must match**; numeric fields match within tolerance (live-quote fields excluded).

**Exit:** all 11 (12 in OPEX week) Phase-1 agents on CLI; a full `/daily-analysis` run reproduces the MCP-path candidate union (set equality on tickers; tier assignments stable).

---

## Phase 3 — Phase-2 + mutating watchlist write-back

| Step | Tool | Migration note |
|---|---|---|
| 2a quant | `insights signal-confluence`, `historical signal-backtest`, `historical cumulative-premium-flow` | signal-backtest + cum-flow verified byte-identical → safe. |
| 2d risk | `risk portfolio-correlation`, `risk market-regime`, `watchlist alerts`, `watchlist scan` | read-only; portfolio-correlation takes `--symbols A,B,C`. |
| 2d/8 risk | **`watchlist manage --action add --group conviction_$D --tickers …`** *(MUTATING)* | **Verified shared XDG state** (`~/.config/unusual-whales-pp-cli/watchlist.json`) — CLI and MCP read/write the same file, so the write-back is state-compatible with prior MCP-written groups. Migrate with confidence; A/B by listing the group via both faces after the write. Set `UW_WATCHLIST_PATH` only if test isolation is wanted. |
| 6 / 6.5 | `insights deep-dive`, `historical trend`, `playbook batch-scan` | batch-scan + trend safe; deep-dive blends yfinance (structure-compare). |

**Validate:** a full daily run writes `conviction_<date>`; `uw watchlist manage --action list` shows it alongside historical MCP-written groups (continuity confirmed). `decision.json` `watchlist_write_back` matches.

**Exit:** `/daily-analysis` and `/weekly-analysis` fully on CLI end-to-end, including the mutating write-back.

---

## Phase 4 — `calibration-audit.md` (4 tools, read-only)

Smallest command. Migrate:
- `historical available-dates` (Step 0.5),
- `historical trend` (Phase 2.1) — use `--date <report_date> --days <window>`,
- `historical signal-backtest` (Phase 2.2) — use `--signal-type <class>` (fix the prose `signal_class`),
- `insights deep-dive` (when-NOT / ad-hoc).

`scripts/validate_decision.py` is unchanged (already a script, and Phase 1 prefers the `decision.json` envelope over tool calls).

**Exit:** a calibration-audit run resolves outcomes via CLI; per-class realised win-rates match an MCP-path run within float tolerance.

---

## Phase 5 — Decommission & document

| Task | Detail |
|---|---|
| **P5.1** | Remove `"mcp__uw-pp__*"` from `.claude/settings.json` allow (keep `Bash(uw:*)`). Optionally leave `mcp__yahoo-finance__*` (separate server, unaffected). |
| **P5.2** | Remove the `uw-pp` server block from `.mcp.json` (keep `yahoo-finance`). This is the real payoff: the 61 tool schemas stop loading into every agent's context. |
| **P5.3** | Update `CLAUDE.md` "MCP Server Required" → "CLI Required": document `uw` (`/Users/ewan/.local/bin/uw`), the `--json --quiet` convention, the `UW_PP_CLI` override, and that the yfinance MCP remains. |
| **P5.4** | Update all three command files' front-matter `description` and "When NOT to invoke" lines that name `mcp__uw-pp__*` (e.g. "use `playbook_daily_synthesis` directly" → "run `uw playbook daily-synthesis`"). |
| **P5.5** | Grep sweep: `grep -rn 'mcp__uw-pp__' .claude/` returns zero (agents + commands fully migrated). |

**Exit:** zero `mcp__uw-pp__*` references in `.claude/`; both reports + the audit run produce on the CLI alone; context cost reduced by the dropped tool schemas.

---

## Rollback

Every phase is reversible by re-adding `mcp__uw-pp__*` to the allow-list and reverting the edited agent/command files (git). Because both faces share the same data backend and the same watchlist file, a half-migrated state is **safe** — a run can mix MCP and CLI calls with no data divergence. This is what makes the parallel-run strategy (decision #1) zero-risk.

---

## Effort & sequencing summary

| Phase | Files touched | Risk | Gate |
|---|---|---|---|
| 0 Prereqs | `.claude/settings.json`, new `scripts/ab_compare.py` | none | smoke + A/B green |
| 1 Step 0 | `daily-analysis.md`, `weekly-analysis.md` | low | Step-0 context block equivalent |
| 2 P1 agents | 11–12 `.claude/agents/*.md` | low–med | candidate union set-equal |
| 3 P2 + write-back | `signal-confluence-quant.md`, `risk-monitor.md`, commands | med (mutating) | watchlist continuity |
| 4 calibration | `calibration-audit.md` | low | per-class WR match |
| 5 decommission | `.mcp.json`, `.claude/settings.json`, `CLAUDE.md`, commands | low | zero MCP refs |

Recommended cadence: Phases 0–1 in one session (fast, high-leverage); Phase 2 across waves 2a→2f with an A/B per wave; Phases 3–5 once Phase 2 is fully green.
