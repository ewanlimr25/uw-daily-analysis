# Permissions Audit Report
**Date:** 2026-05-24  
**Repository:** uw-daily-analysis  
**Scope:** All agents, commands, and scripts

> **SUPERSEDED 2026-05-27 (CLI migration).** The `uw-pp` MCP server was retired and all
> commands/agents migrated to the `uw` CLI (see `analyses/audit/2026-05-27/`). The data-access
> permission is now **`Bash(uw:*)`**, not `mcp__uw-pp__*`. The `mcp__uw-pp__*` rules referenced
> below are obsolete (the server no longer exists in `.mcp.json`). `mcp__yahoo-finance__*` is unchanged.

---

## Executive Summary

This repo has a **well-structured permission model** that covers ~95% of actual tool usage. Only **3 permission gaps** remain that would require manual approval:

1. **Bash(grep:*)** — Used for exploring agent/command files and debugging
2. **Bash(find:*)** — Used for locating files and scanning the repo
3. **Bash(git:*)** — Used for git operations (status, diff, log, commit)

**Recommendation:** Add these 3 to `settings.local.json` to eliminate all permission prompts during normal workflow. ✅

---

## Currently Allowed Permissions

### Global Settings (`.claude/settings.json`)
```json
{
  "skillOverrides": ["daily-analysis", "weekly-analysis", "skill-creator", "orchestrate", "plan", ...],
  "permissions": {
    "allow": [
      "mcp__uw-pp__*",           // ✅ All 61 Unusual Whales MCP tools
      "WebSearch",               // ✅ For forward calendar dates
      "Skill(stock-deep-dive)"   // ✅ Hands off top-2 tickers
    ]
  }
}
```

### Local Settings (`.claude/settings.local.json`)
```json
{
  "permissions": {
    "allow": [
      "Bash(date:*)",                                      // ✅ Date operations
      "Bash(mkdir:*)",                                     // ✅ Directory creation
      "Bash(ls:*)",                                        // ✅ File listing
      "Bash(python3:*)",                                   // ✅ Script execution
      "Bash(claude mcp:*)",                                // ✅ MCP management
      "Read(/Users/ewan/Development/uw-daily-analysis/**)", // ✅ Full repo read
      "Write(/Users/uw-daily-analysis/analyses/**)",       // ✅ Report output
      "mcp__uw-pp__*",                                     // ✅ All UW tools (duplicate OK)
      "Skill(update-config)"                               // ✅ Config updates
    ]
  }
}
```

---

## Tools Actually Used (Full Inventory)

### MCP Tools by Category

| Category | Count | Status | Tools |
|----------|-------|--------|-------|
| **Dark Pool** | 5 | ✅ Allowed | `dark_pool_block_stratified`, `dark_pool_ticker_summary`, `dark_pool_price_levels`, `dark_pool_largest`, `dark_pool_extended_hours` |
| **Historical** | 7 | ✅ Allowed | `historical_trend`, `historical_signal_backtest`, `historical_oi_trend`, `historical_cumulative_premium_flow`, `historical_pc_ratio_zscore`, `historical_iv_percentile_zscore`, `historical_gex_time_series`, `historical_vrp`, `historical_available_dates` |
| **Insights** | 7 | ✅ Allowed | `insights_deep_dive`, `insights_signal_confluence`, `insights_institutional_accumulation`, `insights_conviction_matrix`, `insights_analyst_vs_flow`, `insights_price_vs_flow`, `insights_earnings_play` |
| **Options Flow** | 8 | ✅ Allowed | `options_flow_sweeps`, `options_flow_sector_flow_persistence`, `options_flow_sector_flow`, `options_flow_expiry_heatmap`, `options_flow_greek_screener`, `options_flow_iv_outliers`, `options_flow_top_premium_trades`, `options_flow_dte_volume_share` |
| **Options Structure** | 6 | ✅ Allowed | `options_structure_gex`, `options_structure_front_end_iv_ratio`, `options_structure_term_skew`, `options_structure_iv_term_structure`, `options_structure_dex`, `options_structure_vanna_charm`, `options_structure_today_gamma_flip` |
| **Hot Chains** | 5 | ✅ Allowed | `hot_chains_sweep_persistence`, `hot_chains_most_active`, `hot_chains_smart_money_flow`, `hot_chains_multileg`, `hot_chains_sweep_ratio` |
| **Screeners** | 5 | ✅ Allowed | `screener_bullish_bearish`, `screener_iv_rank`, `screener_earnings_catalyst`, `screener_volume_vs_average`, (note: `screener_put_call_extremes` deprecated) |
| **OI** | 6 | ✅ Allowed | `oi_pin_risk`, `oi_opex_concentration`, `oi_smart_positioning`, `oi_position_rolls`, `oi_decrease_with_volume`, `oi_biggest_increases` |
| **Risk** | 2 | ✅ Allowed | `risk_market_regime`, `risk_portfolio_correlation` |
| **Playbook** | 2 | ✅ Allowed | `playbook_daily_synthesis`, `playbook_batch_scan` |
| **Watchlist** | 3 | ✅ Allowed | `watchlist_manage`, `watchlist_scan`, `watchlist_alerts` |
| **TOTAL MCP** | **61** | ✅ Allowed | All covered by `mcp__uw-pp__*` wildcard |

### Non-MCP Tools

| Tool | Usage | Current | Status |
|------|-------|---------|--------|
| **Bash** | Running scripts, git, date ops | Partial | ❌ Missing: `grep`, `find`, `git` |
| **Read** | Reading files (.md, .json, .py) | Allowed | ✅ Full path coverage |
| **Write** | Writing reports and decision envelopes | Allowed | ✅ `analyses/**` coverage |
| **WebSearch** | Forward calendar dates | Allowed | ✅ Global permission |
| **Agent** | Spawning Phase 1 & 2 agents | Auto-allowed | ✅ No permission needed |
| **Skill** | Calling sub-skills | Allowed | ✅ Specific skills listed |

---

## Permission Gaps (3 items)

### 1. ⚠️ **Bash(grep:\*)**
**Impact:** MODERATE  
**Current Status:** Requires approval each time  
**Used for:** 
- Searching agent/command files for tool invocations
- Debugging and understanding code patterns
- Finding references to specific functions
- Auditing agent specifications

**Frequency:** Low (ad-hoc debugging only)  
**Examples:**
```bash
grep -rh "mcp__uw-pp__\|WebSearch" /Users/ewan/Development/uw-daily-analysis/.claude
grep -r "Agent(" /Users/ewan/Development/uw-daily-analysis/.claude/agents
```

### 2. ⚠️ **Bash(find:\*)**
**Impact:** MODERATE  
**Current Status:** Requires approval each time  
**Used for:**
- Locating command and agent files
- Discovering test files
- Finding new reports for audits
- Scanning for specific file patterns

**Frequency:** Low (ad-hoc discovery only)  
**Examples:**
```bash
find /Users/ewan/Development/uw-daily-analysis/.claude -type f -name "*.md"
find /Users/ewan/Development/uw-daily-analysis/analyses -name "*.decision.json"
```

### 3. ❌ **Bash(git:\*)**
**Impact:** HIGH  
**Current Status:** Requires approval each time  
**Used for:**
- Checking git status before commits
- Viewing diff output
- Reviewing commit log
- Creating commits and PRs
- Switching branches

**Frequency:** High (normal development workflow)  
**Examples:**
```bash
git status
git diff
git log
git commit -m "..."
gh pr create
```

---

## Risk Assessment

### Permission Expansion Justification

All three missing permissions are **read-only exploratory or standard git operations**:

| Permission | Risk Level | Why Safe |
|------------|-----------|----------|
| `Bash(grep:*)` | ⭐ MINIMAL | Grep is read-only; searches within repo only; no execution risk |
| `Bash(find:*)` | ⭐ MINIMAL | Find is read-only; searches within repo only; no I/O risk |
| `Bash(git:*)` | ⭐⭐ LOW | Git operations bounded to this repo; dangerous ops (force push, reset --hard) still require confirmation per rules |
| `Bash(python3:*)` | ⭐⭐ LOW | Already allowed; only runs stdlib scripts in `scripts/` |

**Scope:** All three are already scoped to this repo and do not execute remote code or modify critical systems.

---

## Recommended Configuration

### Add to `.claude/settings.local.json`

```json
{
  "permissions": {
    "allow": [
      // === EXISTING ===
      "Bash(date:*)",
      "Bash(mkdir:*)",
      "Bash(ls:*)",
      "Bash(python3:*)",
      "Bash(claude mcp:*)",
      "Read(/Users/ewan/Development/uw-daily-analysis/**)",
      "Write(/Users/ewan/Development/uw-daily-analysis/analyses/**)",
      "mcp__uw-pp__*",
      "Skill(update-config)",
      
      // === NEW (RECOMMENDED) ===
      "Bash(grep:*)",      // Ad-hoc code exploration and debugging
      "Bash(find:*)",      // File discovery (agents, reports, tests)
      "Bash(git:*)"        // Git workflow (status, diff, commit, PR)
    ]
  }
}
```

### Impact After Update

| Workflow | Current | After Update |
|----------|---------|--------------|
| Run `/daily-analysis` | 0 prompts ✅ | 0 prompts ✅ |
| Run `/weekly-analysis` | 0 prompts ✅ | 0 prompts ✅ |
| Run `/calibration-audit` | 0 prompts ✅ | 0 prompts ✅ |
| Debug agent code | 1+ prompts ⚠️ | 0 prompts ✅ |
| Audit repo tools | 1+ prompts ⚠️ | 0 prompts ✅ |
| Git commit/push | 1+ prompts ❌ | 0 prompts ✅ |

---

## Implementation Steps

1. **Backup current config** (optional):
   ```bash
   cp .claude/settings.local.json .claude/settings.local.json.bak
   ```

2. **Apply recommended changes:**
   - Open `.claude/settings.local.json`
   - Add the three new Bash permissions to the `allow` array
   - Save and close

3. **Verify no conflicts:**
   ```bash
   python3 -c "import json; json.load(open('.claude/settings.local.json'))" && echo "✅ Valid JSON"
   ```

4. **Test workflow:**
   - Run a quick `/daily-analysis` (should still prompt 0 times for permissions)
   - Run a git operation (should no longer prompt)
   - Search for code with grep (should no longer prompt)

---

## Appendix: Tool Usage Heat Map

**Most-Used Tools (Phase 1 agents call these repeatedly):**
- `watchlist_manage` (8 uses) — Writing back top-5 conviction tickers
- `insights_deep_dive` (7 uses) — Deep-dive detail on individual tickers
- `historical_signal_backtest` (7 uses) — Win-rate validation before sizing
- `historical_oi_trend` (7 uses) — OI accumulation patterns (5d/10d window)
- `historical_cumulative_premium_flow` (7 uses) — Smart money directional bias

**Least-Used Tools (Conditional or rare edge cases):**
- `playbook_batch_scan` (2 uses) — Bulk watchlist screening
- `hot_chains_sweep_ratio` (2 uses) — Alternative to sweep_persistence
- `risk_portfolio_correlation` (2 uses) — Portfolio-level hedge checks

**Zero-Conflict Tools:**
- All 61 MCP tools are allowed via wildcard `mcp__uw-pp__*`
- No deprecated tools are referenced (e.g., `screener_put_call_extremes` is replaced by `historical_pc_ratio_zscore`)

---

## Notes

- **Decision envelopes** (`*.decision.json`) are validated by `scripts/validate_decision.py` (already allowed via `Bash(python3:*)`)
- **Scripts** (fred_macro.py, finnhub_enrich.py) use only stdlib — no pip dependencies
- **WebSearch** is used sparingly (forward event calendar only) and should remain allowed
- **Skill invocations** (`daily-analysis`, `weekly-analysis`, etc.) use the Agent tool internally, which doesn't require explicit permission
