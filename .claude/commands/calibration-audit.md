---
description: Retrospectively audit `/daily-analysis` and `/weekly-analysis` plus their backing UW `uw` CLI tools, using the historical reports in `analyses/daily/*/report.md` and `analyses/weekly/*/report.md` as the dataset. Seven discrete phases — each writes a resumable checkpoint under `analyses/audit/<YYYY-MM-DD>/phase_<N>_<slug>.md`. Frame every judgment from a desk perspective (buy-side PM, sell-side flow trader, market-maker quant). Propose-only — emits patch *intentions* and never auto-edits agent files. Invoke whenever the user asks for a calibration audit, a backtest of the daily/weekly skills, "how well are we calling the market," win-rate calibration, score-rubric audit, CLI-tool tier list, or types `/calibration-audit`. Do NOT trigger for single-day reports (use `/daily-analysis`), single-ticker deep dives (use `uw insights deep-dive`), or general code review of the agent files.
model: opus
defaults:
  outcome_windows:
    "0DTE": same-day close vs entry
    swing: 3D-and-10D
    LEAP: 30D-and-90D
    weekly: 5D-and-10D
  min_dataset:
    daily: 10
    weekly: 3
  disposition: propose-only
  cadence: on-demand
  win_threshold: ">=+1R in thesis direction without -1R prior drawdown"
  relax_threshold: false
---

# Calibration Audit

Audit the `/daily-analysis` and `/weekly-analysis` skills against their own historical output. The reports under `analyses/daily/<date>/` and `analyses/weekly/<iso-week>/` are the dataset; forward-resolved outcomes are the truth set; the audit asks whether the conviction rubric, the `uw` CLI tools cited as evidence, and the Phase-1→Phase-2 decision process actually deliver the desk-grade discipline they claim to.

The audit is **propose-only**. It emits patch intentions — never auto-edits agent files, score rubrics, or commands. Recommendations cite the phase and the data point that justifies them. No vibes.

> **Method register (2026-05-30 meta-audit, `analyses/audit/2026-05-30/calibration_meta_audit.md`).** Auditor-method fixes applied: **C20** daily-OHLC path-aware resolution (replaces the non-executable `uw historical trend --date`/high-low spec); **C21** benchmark-excess (realised − SPY same-window) as a first-class Phase-3 column — the audit now measures *edge*, not just calibration; **C22** removes look-ahead from the truth-set (`signal-backtest` has no `--date`); **C23** decided-N≥8 floor + Benjamini-Hochberg across flagged class/tool stats + reconstructed-citation priority cap; **C24** Phase-6 gate *effectiveness* (downgrade-effectiveness, VETO false-positive rate) on top of gate firing; **C25** reliability diagram + log-loss beside Brier. These are *method* changes to the auditor; the audit it runs stays propose-only and never edits the subjects.

## Data access — the `uw` CLI

All Unusual Whales data comes from the **`uw` CLI** (`/Users/ewan/.local/bin/uw`; override with `$UW_PP_CLI`), invoked via Bash: `uw <group> <subcommand> [--flag value …] --json --quiet`. `--json` is mandatory (the CLI defaults to a table); `--quiet` keeps stdout pure JSON. For a backward window from a fixed report date, pass `--date <report_date> --days <window>`. `scripts/validate_decision.py` is unchanged.

## When to invoke

- "Audit the daily-analysis skill" / "calibrate our scoring" / "are our win-rates real?"
- "Backtest the agent fleet" / "tool tier list" / "schema audit"
- Slash command `/calibration-audit`

## When NOT to invoke

- Single-ticker forward outlook → `uw insights deep-dive`
- Single-day post-market report → `/daily-analysis`
- Weekly recap → `/weekly-analysis`
- Code review of agent prompts (no outcome data needed) → `code-reviewer` agent
- "Did NVDA work last week?" → ad-hoc `uw historical trend` call

## Operating principle: outcome-driven, not opinion-driven

Every claim in this audit must trace to a parseable data point: a ticker call extracted from a report, a forward-resolved outcome from `uw historical trend` / `uw historical signal-backtest`, a tool citation extracted from an audit-trail row. Where data is thin, the skill says so explicitly and downgrades conclusions to "structural / qualitative" — never silently extrapolates.

The persona for every phase is a composite **elite desk reviewer**: buy-side PM (does this generate alpha?), sell-side flow trader (does this match how flow actually trades?), market-maker quant (do the weights match the realised marginal contribution?). A grading schema is only credible if it survives all three readings.

---

## Step 0 — Preflight

1. **Date** — `date +%F` for today's `YYYY-MM-DD`. This is the audit run-id and the output directory: `analyses/audit/<YYYY-MM-DD>/`. `mkdir -p` it.

2. **Inventory** — list `analyses/daily/*/report.md` (daily) and `analyses/weekly/*/report.md` (weekly). Count both. (Each report lives in its own per-id run folder `analyses/daily/<date>/` or `analyses/weekly/<iso-week>/`, alongside its `decision.json`.)

3. **Threshold check** — defaults: 10 daily OR 3 weekly required. If neither passes:
   - If `relax_threshold=false` (default): **abort** with the exact message:
     > "Insufficient calibration history: N_daily=<X>, N_weekly=<Y>. Below thresholds (10 daily OR 3 weekly). Calibration math is noise-dominated below this floor. Re-run after collecting more reports, or set `relax_threshold=true` to override (results will be flagged DATASET-SIZE-RELAXED throughout)."
   - If `relax_threshold=true`: proceed with a **DATASET-SIZE-RELAXED** banner stamped at the top of every checkpoint and re-printed at the start of `SUMMARY.md`.

4. **Resume detection** — if `analyses/audit/<YYYY-MM-DD>/phase_<N>_*.md` already exists, resume from the next phase rather than re-running. Each checkpoint is self-contained; never re-derive earlier phases.

5. **Available-dates check** — `uw historical available-dates`. Phase 2 needs forward outcomes; if the latest UW data is more than one trading day stale relative to the most recent ticker call, abort and tell the user to re-export from UW.

---

## Phase 1 — Inventory & Parse

**Goal.** Enumerate every report and extract structured per-call data into a normalized JSONL alongside the markdown checkpoint.

### Read order

Process daily reports oldest→newest, then weekly reports oldest→newest. Use `Read` directly when total report count is ≤30; otherwise route through the `iterative-retrieval` skill (the analyses folder grows linearly with calendar time and will eventually exceed comfortable single-pass context).

### Prefer the structured decision envelope (machine-resolvable)

Before parsing any report prose, check for a sidecar **decision envelope** beside the report in the same run folder: `analyses/daily/<date>/decision.json` (daily) or `analyses/weekly/<iso-week>/decision.json` (weekly). When present:

1. Validate it first: `python3 scripts/validate_decision.py --file <path>`. If it fails validation, note the data-quality flag and fall back to prose parsing for that report.
2. Load `calls[]` directly — each object **already is** the normalized per-call row below (`ticker`, `horizon`, `section`, `tier`, `raw_score`, `score_components[]`, `dominant_signal_class`, `win_rate` + `win_rate_n` + `win_rate_source`, `pre_risk_size`, `final_size`, `gate_verdicts`, `fundamentals_verdict`, `debate_residual_confidence`, `structure`, `invalidation`, `thesis`, `key_risks[]`). No prose re-parsing, no `Σ points` reconciliation needed (the validator guarantees it). Map `gate_verdicts` keys to `gates_fired`, and carry `fundamentals_verdict` / `debate_residual_confidence` as new audit dimensions (e.g. did VETO'd names that were nonetheless tracked actually fail? did high bear-residual names underperform?).
2b. **`fz` advisory dimensions (2026-05-27 `fz`-edge).** Also carry, when present (additive — no schema break): each call's `fz_context` (`short_float_pct`, `days_to_cover`, `float_shares`, `squeeze_pressure`, `recom`, `upside_to_target_pct`) and the top-level `breadth_cross_check`. These are the outcome inputs that authorize (or kill) the Phase-B promotions of `fz` criteria **C15–C18** (`analyses/audit/2026-05-25/improvement_criteria.md`): tag whether each call carried high short-interest, a flow-vs-analyst divergence, or an insider cluster, so Phase 4 can score those axes against realised outcomes.
3. The top-level `macro_event_risk` and `macro_snapshot_signals` give the macro context at entry — use them to test whether event-risk-flagged calls drew down around the print.

The envelope is the authoritative source when it exists; the markdown report is its human-readable rendering. Only fall back to the prose-extraction below for **legacy reports that predate the envelope** (no `.decision.json` sidecar).

### Per-report extraction (legacy prose fallback)

For every ticker mentioned in §3 (Swing Setups), §4 (LEAP Builds), §5 (Volatility Surface — when it produces a sized vol trade), §7 (High-Conviction Cross-Ref), and the Executive Summary's top-call lines, capture:

```jsonc
{
  "report_date": "2026-05-08",
  "report_kind": "daily",                      // "daily" | "weekly"
  "ticker": "NVDA",
  "section": "swing_long",                     // 0DTE | swing_long | swing_short | leap | vol_long | vol_short | watch_only
  "horizon": "swing",                          // 0DTE | swing | LEAP | weekly
  "tier": "HIGH",                              // High/Medium/Low when explicit; derived from final size when not
  "raw_score": 10,                             // null if legacy report has no rubric score
  "score_components": [                        // [] if not surfaced in the report
    {"points": 3, "source_agent": "dealer-positioning-strategist", "tool": "uw options-structure dex"},
    {"points": 2, "source_agent": "gamma-flip-tracker",            "tool": "uw options-structure today-gamma-flip"}
  ],
  "dominant_signal_class": "dealer_positioning_flip",   // null if absent
  "claimed_win_rate": 1.00,                    // null if absent
  "pre_risk_size": "full",                     // full|half|starter|skip|null
  "final_size": "starter",                     // post-risk-monitor; null if same as pre_risk_size
  "structure": "Long July 720/730 call debit spread",
  "thesis_direction": "long",                  // long | short | vol_long | vol_short
  "invalidation": "breadth deteriorates <30%, OR DEX reverses",
  "agents_flagged_by": ["dealer-positioning-strategist","gamma-flip-tracker","sweep-tracker"],
  "tools_cited":  ["uw options-structure dex","uw options-structure today-gamma-flip","uw options-structure gex","uw hot-chains sweep-persistence"],
  "regime_at_entry": "TRANSITIONAL UPTREND",
  "vrp_at_entry": "FAIR",
  "front_iv_ratio_at_entry": 1.273,
  "gates_fired": ["regime", "panic_1.27"],     // [] if none
  "raw_excerpt": "<<≤200-char quote from the row in §7 — provenance>>"
}
```

Legacy reports (early format, e.g. `2026-04-30.md`) lack `raw_score` / `score_components` / `claimed_win_rate`. Tag those calls `legacy_format=true` and let downstream phases handle them — they still have a section, ticker, direction, structure, and invalidation, which is enough for outcome resolution and tool attribution.

### Output

- `phase_1_inventory.md` — desk-style summary: total calls extracted, breakdown by horizon, tier, signal class; format coverage gaps; data-quality flags (e.g. "GOOG / GOOGL share-class confusion"; "two reports cite same call differently").
- `phase_1_inventory.jsonl` — one JSON object per call, machine-readable.

### Hard rules

- Never invent fields. If `claimed_win_rate` is not in the report, leave it `null`.
- One row per (report_date, ticker) — if the same ticker appears in §3 and §7, prefer §7's audited row.
- Watch-only / disqualified-LEAP candidates are kept (`section="watch_only"` or `"leap_disqualified"`) — they are part of the decision audit even though they aren't trade calls.
- Abort early if extraction yields zero rows from any single non-empty report — that's a parser bug, not an empty day.

---

## Phase 2 — Outcome Resolution

**Goal.** Resolve every call from Phase 1 to WIN / LOSS / INCONCLUSIVE on a horizon-matched window.

### Horizon-to-window map (defaults; overridable in frontmatter)

| Horizon | Windows |
|---|---|
| 0DTE | same-day close vs entry close |
| swing | 3D AND 10D (both must agree on direction; disagreement = INCONCLUSIVE unless 10D is decisive) |
| LEAP | 30D AND 90D |
| weekly | 5D AND 10D |

### Win threshold (encoded in frontmatter, restated in checkpoint)

> ≥ +1R move in thesis direction within window **without** −1R drawdown first, where R is the structure's defined risk per the report's `structure` field. For tickers without a structure-implied R, default to **0.5 × ATR(14)** at entry.

This is a **path-aware** definition — a +2% gain that came after a -1.5% drawdown is a LOSS (or at best INCONCLUSIVE), not a WIN. Path matters because the report's invalidation rule would have stopped the trade before the move arrived.

**Resolution granularity — daily OHLC, not close-only (C20).** The path rule is only real if you can see the intra-window low (for a long) or high (for a short). Resolve on **daily OHLC bars** — `mcp__yahoo-finance__get_historical_stock_prices` returns `open/high/low/close` per day (verified: the daily bar carries `high` and `low`; only intraday-tick range is unavailable). Compute `ATR(14)` as **true range** — `max(high−low, |high−prev_close|, |low−prev_close|)` averaged over the 14 bars before entry — not the close-to-close range proxy. Then walk the window bar-by-bar: a long is a LOSS the first day `low` breaches `entry − R` *before* any day's `high` reaches `entry + R`; symmetric for a short. This recovers ~80% of the true path rule. Record `max_adverse_excursion_pct` from the daily extreme, not the daily close. **Do not** silently degrade to close-to-close — if a ticker has no daily OHLC, tag it INCONCLUSIVE (`data_unavailable`), never a LOSS. The earlier "close-only is the only option" framing was wrong: daily high/low is available and the path rule must use it.

### Tool calls

For each row in Phase 1:

1. **Price window (the WIN/LOSS resolver) — daily OHLC.** `mcp__yahoo-finance__get_historical_stock_prices` for `ticker`, spanning `report_date` through `report_date + horizon_window` (trading days). Capture per-bar `high`/`low`/`close`; compute entry = the `close` on `report_date` (or next session if the report is post-close), `R` = 0.5 × true-range-ATR(14) at entry, intra-window MAE from the daily extremes, and end-of-window close. **`uw historical trend` is NOT a price-window tool** — it has no `--date` flag and returns options-flow metrics + daily close only (no high/low). Use it, if at all, only to read the *flow context* at entry, never to resolve outcomes. (Earlier versions of this skill specified `uw historical trend --date … capture intra-window high/low`; that method is not executable — the flags and fields don't exist. Do not reintroduce it.)
2. **Signal-class context — NOT a point-in-time benchmark (C22).** `uw historical signal-backtest --signal-type <dominant_signal_class>` returns *general* class behaviour over all available history. **It has no `--date` flag**, so it cannot be quoted as "the realised win-rate as of the report's date" — doing so injects look-ahead (the rate is computed partly on data that postdates the call). Carry it only as `general_class_behaviour` colour. The honest point-in-time benchmark for Phase 3 calibration is the **SPY same-window same-direction base rate** (C21), computed in Phase 3 — not this tool.
3. **Vol calls (vol_long / vol_short)** — resolve against realised-vol direction: did realised σ over the window exceed (long) or fall below (short) the implied move quoted at entry? Use the daily OHLC highs/lows to compute realised σ and compare to the report's `implied_move` **when present**. Legacy reports without an `implied_move` field cannot do a true IV-vs-RV resolution — resolve on RV-direction only and tag `vol_resolution="rv_direction_proxy"` so Phase 3 never treats these as calibrated IV-vs-RV outcomes.

Cap external price calls per phase: at most 2 per row (one OHLC window pull + one same-window SPY pull for the C21 benchmark). If a price pull fails (delisted, no history), tag the row INCONCLUSIVE with `inconclusive_reason="data_unavailable"` — never tag as LOSS.

### Output

- `phase_2_outcomes.md` — desk summary by tier and signal class: WIN / LOSS / INCONCLUSIVE counts with explicit win-threshold and INCONCLUSIVE definitions reprinted verbatim. Include a per-horizon breakdown.
- `phase_2_outcomes.jsonl` — Phase 1 rows extended with `outcome`, `outcome_window`, `realised_return_pct`, `max_adverse_excursion_pct` (from daily extremes, C20), `inconclusive_reason` (if applicable), `general_class_behaviour_winrate` (the no-`--date` `signal-backtest` rate — colour only, look-ahead-contaminated, **not** a benchmark; C22), and `spy_benchmark_win` (boolean: did a same-direction SPY bet entered the same day clear +1R over the same window — the per-row input to the C21 benchmark-excess statistic).

**C3 — populate the realised-P&L envelope fields (advisory expectancy record).** For every CLOSED call, write back the new envelope fields so the closed-loop expectancy record accrues: `realized_pnl_pct` = the resolved `realised_return_pct`; `payoff_ratio` = avg WIN return / |avg LOSS return| for that `dominant_signal_class` over closed calls (`scripts/kelly_sizing.py:payoff_ratio`); `expectancy_pct` (`kelly_sizing.py:expectancy`); `kelly_fraction` = `kelly_sizing.py:capped_half_kelly(realised_winrate, payoff_ratio)`. These are **advisory** — recorded for the Phase 3 gate below, NOT yet a live sizing input. Leave them `null` for still-open calls.

INCONCLUSIVE rows are **excluded from win-rate denominators** in subsequent phases.

---

## Phase 3 — Calibration Audit

**Goal.** Compare claimed win-rate per signal class to realised win-rate. Quantify miscalibration.

### Calculations

1. **Per-signal-class table.** For each `dominant_signal_class` with **decided-N ≥ 8** in the dataset (C23 — raised from 5; a divergence on n=5–7 is noise, and the 2026-05-29 run tabled −40pp on n=1 claims that should never have reached a reader):
   - Claimed win-rate (mean of `claimed_win_rate` field, where present)
   - Realised win-rate (WIN / (WIN+LOSS), excluding INCONCLUSIVE)
   - **Realised benchmark-excess (C21)** = realised WR − SPY same-window same-direction WR, via `scripts/excess_winrate.py:market_excess(realised_wr, spy_benchmark_wr)`, where `spy_benchmark_wr` = the fraction of that class's rows whose `spy_benchmark_win` (Phase 2) fired. **This is the column that separates edge from beta.** A class can be perfectly calibrated (claimed ≈ realised) and still have **zero or negative excess** — i.e. it only "wins" because the tape rose. In a single-regime UPTREND dataset this is the most important number on the table: a 50% long WR against a 55% SPY up-day base rate is **negative edge dressed as a coin-flip**. Report excess with its sign; flag any class with calibration ✅ but excess ≤ 0 as **"calibrated-but-beta."** (This mirrors the *subject's* own C2 market-excess gate — the audit must hold the system to the same bar the system holds itself.)
   - N (decided)
   - Divergence (claimed − realised, in pp)
   - **Flag with multiple-hypothesis control (C23).** Computing a divergence p-value per class across ~10 classes inflates false positives. After computing a two-sided binomial p-value for each class's realised-vs-claimed divergence, apply **Benjamini-Hochberg** (FDR 0.10) across the whole class set; only 🚩 a divergence that survives BH. Classes with decided-N in 5–7 go to an **appendix table** marked `THIN_N` and never appear in the headline table or the SUMMARY.

2. **Per-tier reliability diagram (text table).** For each conviction tier (HIGH / MEDIUM / LOW), show realised win-rate. **A monotone tier order requires HIGH > MEDIUM > LOW.** Flag inversions explicitly — they are a desk-quitting signal.

3. **Brier score + reliability curve + log-loss (C25).** Across all calls with both `claimed_win_rate` (or the rubric-implied prior for legacy) and an outcome:
   - `Brier = (1/N) × Σ (claimed − realised_outcome)²` where realised_outcome ∈ {0, 1}. Lower is better; ≥ 0.25 is "no better than coin-flip," ≤ 0.10 is "professionally calibrated." Brier is a *single* number that **conflates calibration and resolution** — it can't tell you *where* on the confidence scale the rubric lies.
   - **Reliability diagram** — bucket `claimed_win_rate` into deciles (0.5–0.55, 0.55–0.60, …, ≥0.90); for each bucket report predicted-mean vs realised-hit-rate and N. This localizes the miscalibration: the 2026-05-29 run's overconfidence lives entirely in the ≥0.80 buckets (dark-pool/vol-surface quoting 0.80+ and realising ~0.50). A desk reads the diagram, not just the scalar Brier.
   - **Log-loss** = `−(1/N) × Σ [y·ln(p) + (1−y)·ln(1−p)]` (clamp `p` to [0.01, 0.99]). Log-loss punishes confident-and-wrong far harder than Brier, so a rubric that quotes 0.85 and is wrong is penalised the way a desk actually feels it. Report both; if log-loss and Brier disagree on direction across iterations, the confident tail is the cause.

4. **Conviction-vs-outcome scatter.** Bucket `raw_score` into quintiles; report realised win-rate per quintile. The slope from low to high score should be positive and monotone. If quintile-3 win-rate exceeds quintile-5 win-rate, that's a tier-inversion buried inside the score.

5. **C3 — expectancy table + fractional-Kelly live-activation gate.** Hit-rate alone lost discriminating power (the 05-23 raw_score→WR slope was nearly flat at 58–64%); a payoff-aware metric may restore an actionable ordering. For each tier, report **mean realised P&L (expectancy)**, the signal-class `payoff_ratio` (avg win / |avg loss|), and the advisory **capped half-Kelly** fraction. Then run the **live-activation gate** `scripts/kelly_sizing.py:tier_expectancy_monotone(closed_calls)`: the half-Kelly sizer may go **live only when tier × expectancy is monotone (HIGH ≥ MED ≥ LOW) on n ≥ 30 closed calls** — below that it stays **ADVISORY** and the win-rate ladder remains the live sizer (per register C3, mirroring Kelly's "50–100 trades for stable estimates"). Report the gate's `status` (LIVE / ADVISORY_ONLY) and `reason`. **Do not flip `signal-confluence-quant` / `risk-monitor` to the Kelly sizer until this gate returns LIVE.**

### Output

- `phase_3_calibration.md` — the desk reads the class table (now carrying **benchmark-excess**), the per-tier diagram, the **reliability deciles**, Brier + **log-loss**, and a written verdict. The verdict has **four** sections: (a) "where the rubric is honest," (b) "where it lies to itself," (c) "tier inversions or overconfidence on High-tier," and **(d) "calibrated-but-beta" — classes whose claimed≈realised but whose benchmark-excess ≤ 0 (they ride the tape, they don't beat it).** (d) is the new desk-critical read: a class can pass calibration and still be worthless edge.
- `phase_3_calibration.jsonl` — per-signal-class numerics incl. `realised_excess`, `spy_benchmark_wr`, BH-adjusted p-values, the reliability-decile array, and per-tier + log-loss/Brier scalars.

### Desk-style commentary required

For every flagged divergence, write one sentence in the voice of a sell-side flow trader: *"`bullish_flow` claims 100% but realised 71% (n=14) — flow chasers who think every sweep is a confirmed signal will cap at this rate; size accordingly."* No spreadsheet-language. This is a desk note.

---

## Phase 4 — Tool Attribution

**Goal.** For each `uw` CLI tool cited as evidence, compute marginal contribution to outcome. Identify load-bearing tools, confounded-on-winners tools (only fire on winners — likely outcome-leakage), and indiscriminate tools (no information).

### Per-tool computation

For each `tool` appearing in any row's `tools_cited`:

- N_with = calls where the tool was cited
- N_without = calls where it was not cited (within the same `dominant_signal_class` to control for class)
- `winrate_with` − `winrate_without` per signal class, weighted by N
- Net **marginal contribution** = average of class-conditional differences, weighted by class-N

### Tool tier definitions (use exactly these)

| Tier | Criterion | Action implied |
|---|---|---|
| **LOAD-BEARING** | marginal_contribution ≥ +10pp, fires on both winners and losers | Promote to "required citation" for that signal class |
| **SUPPORTIVE** | marginal_contribution +3pp to +10pp | Keep in the toolkit; no ranking change |
| **CONFOUNDED** | fires on ≥80% of winners and ≤30% of losers (suspiciously asymmetric) | Demote — the tool may be a post-hoc lookup, not a real-time signal |
| **NO-INFO** | marginal_contribution within ±2pp | Deprecate from default citation; cite only when meaningful |
| **NEGATIVE** | marginal_contribution ≤ −5pp | Investigate — the tool may be misinterpreted by an agent |

### Output

- `phase_4_tools.md` — tool tier list with desk commentary per tool. Voice: market-maker quant. Format example: *"`uw dark-pool block-stratified` LOAD-BEARING (+18pp on `dark_pool_accumulation`, n=22). Acts as the institutional/retail filter that the raw `uw dark-pool ticker-summary` lacks. Without this gate, accumulation calls degrade by ~1 in 5."*
- `phase_4_tools.jsonl` — tool-level numerics.

### `fz` advisory fields / clusters / breadth (2026-05-27 `fz`-edge — gates the Phase-B promotions)

Score the `fz` signals on the **same** LOAD-BEARING / SUPPORTIVE / NO-INFO / NEGATIVE tier scale as the `uw` tools, so the data authorizes (or kills) each Phase-B promotion:

- **`fz_context.squeeze_pressure` (short interest / days-to-cover)** → gates **C15**: among SHORT-thesis calls, do high-SI names (`short_float ≥ 20% ∧ days_to_cover ≥ 5`) underperform the short-class baseline (squeeze trap)? Among LONG-momentum calls, do they outperform (squeeze tailwind)?
- **`fz_context.float_shares`** → gates **C16**: does a float-normalized dark-pool-block / OI threshold (block as % of float) separate accumulation winners from churn better than the dollar-tier filter alone (effect ≥ the C11 conjunction)?
- **`fz_context.recom` / `upside_to_target_pct` (analyst divergence)** → gates **C17**: does flow-vs-analyst disagreement have sign on outcomes (downside-only)?
- **insider clusters (`fz insider-clusters`)** → gates **C18**: does the 3-way conjunction (insider cluster ∧ DP block ∧ cum-flow) beat the 2-way C11 baseline?
- **`breadth_cross_check`** → does a breadth divergence (`pct_green < 50` on a green-tape day) precede regime flips / predict next-session drawdown?

Report each with `marginal_contribution`, `n`, and a GO/NO-GO verdict on the corresponding C-item's promotion threshold. **Do not promote** a `fz` criterion that has not cleared its threshold here — until then it stays advisory (Phase A) and earns 0 points (the repo's calibration discipline — `improvement_criteria.md`).

### Hard rules

- A "CONFOUNDED" finding requires manual sanity-check before recommending demotion — some tools genuinely fire only when conviction is high (e.g. `uw insights signal-confluence ≥ 5`). Note this in the per-tool commentary.
- Do not score tools cited fewer than 5 times — N is too small. Mark as "INSUFFICIENT_N" and exclude from tier ranking. **`fz` fields obey the same N≥5 floor** — on the tiny current dataset they will be INSUFFICIENT_N for several audits; that is expected and keeps them advisory.
- **Multiple-hypothesis control (C23).** The tool table runs ~20 simultaneous `winrate_with − winrate_without` tests. Apply Benjamini-Hochberg (FDR 0.10) across the tool set before declaring any tier *change*; a single tool clearing +10pp on n=9 in a 20-test sweep is one expected false positive. Tools cited 5–7 times are `THIN_N` and tier-rated **provisionally** (lower-case tier label) — never the sole basis for a Phase-7 recommendation.
- **Ubiquity confound (C32 precursor).** A tool cited on a large fraction of rows (e.g. `cumulative-premium-flow` at n=76) will read NO-INFO by construction — `with`≈`without` because it's the base-rate citation, not because it carries no signal. When a tool is cited on >60% of rows in its class, flag `ubiquity_confounded` and say so in the commentary rather than declaring it dead.
- **Provenance governs priority (the reconstructed-citation rule).** For any audit where `tools_cited` on the majority of rows was **reconstructed from prose** (not read verbatim from `decision.json` `score_components[].source_tool`), every tool-tier finding is **structural/qualitative**. Such a finding may inform a Phase-7 recommendation but **cannot be rated above P1** — a P0 (calibration-breaking, act-now) tool change requires verbatim envelope provenance on ≥ the N used. State the provenance basis (verbatim vs reconstructed, and the N of each) in the phase header. This prevents the failure mode where a tool is caveated to "qualitative" and then ripped out of a live gate at P0 on the same breath.

---

## Phase 5 — Grading-Schema Critique

**Goal.** Audit the `signal-confluence-quant` rubric (the `+3 dealer-positioning, +2 accumulation, …` table) against realised marginal contribution. Propose a re-weighted rubric and re-binned tier cuts. Stress-test on holdout.

### Component-weight audit

For each signed point in the rubric (e.g. `+3 dealer-positioning DEX flip`):

1. Identify which (agent, tool) combination produces that point in the audit trail.
2. Pull its marginal contribution from Phase 4.
3. Compute the **calibrated weight** ∝ marginal_contribution × class-prevalence.
4. Normalize to keep the rubric on the same total-points scale.

Output a "current vs proposed" table side-by-side. The proposed weights must satisfy: (a) sum-to-same-budget, (b) preserve the sign of every signed component (don't invent +/− flips on weak data), (c) include a "source: Phase 4 marginal_contribution = +Xpp, n=N" justification per change.

### Tier-cut audit

The current rubric uses High/Medium/Low cuts implicit at score ≥ 5 / 3–4 / <3. Compute realised win-rate per integer score and propose new cuts that **maximize tier-monotonicity** (HIGH realised > MEDIUM realised > LOW realised, with the largest gap between HIGH and MEDIUM).

### Holdout stress-test

Hold out the **most recent 20% of reports** (rounded up; minimum 2 reports). Refit the proposed rubric on the older 80%; re-score the holdout. Compare:

- In-sample vs holdout realised win-rate per tier
- Brier in-sample vs holdout

If the holdout Brier degrades by >50% vs in-sample, the proposal is overfit — flag it and propose a more conservative re-weight (closer to the original).

### Output

- `phase_5_schema.md` — the three deliverables: weight table (current vs proposed with justifications), tier-cut table (current vs proposed), holdout stress-test result with verdict (ACCEPT / REJECT / ACCEPT_WITH_CAVEAT). Voice: market-maker quant — precise, no hand-waving.
- `phase_5_schema.jsonl` — proposed rubric in the same shape `signal-confluence-quant` consumes, ready for a future `apply` mode.

### Hard rules

- **Reuse `signal-confluence-quant` for any rescoring math.** If you need to recompute a score under proposed weights, spawn that agent rather than implementing scoring inline. Pass the proposed rubric as input.
- Never propose a rubric the holdout test rejects — escalate to a more conservative proposal instead.

---

## Phase 6 — Decision-Process Audit

**Goal.** Trace the Phase-1 → Phase-2 handoff inside `/daily-analysis`. Verify that `signal-confluence-quant` and `risk-monitor` actually applied the documented procedure on every call.

### Per-call compliance checks

For each row in Phase 1 with `score_components` and `gates_fired`:

1. **Quant compliance**:
   - Sum of `score_components.points` equals `raw_score`? (mechanical check)
   - Every component has a named `source_agent` and `tool`?
   - Backtest sizing-map honored? Check against the **live** subject map (`signal-confluence-quant.md`): **≥0.70 → full, 0.50–0.70 → half, <0.50 → starter/skip** (the full-size line was tightened 0.65→0.70 by the 2026-05-23 register; auditing against the old 0.65 mis-flags compliant half-sizes). The size vocabulary the rubric actually emits is **`full | half | quarter | starter | skip`** — `quarter` sits between half and starter; include it in the order map so a legitimate `quarter` downgrade is not flagged as a violation (this caused several false positives in the 2026-05-29 run). Gate-driven downgrades below the map size are always allowed; only an *upgrade* above the win-rate-implied size is a violation.

2. **Risk-monitor compliance**:
   - For each gate documented in `risk-monitor.md` (regime, VRP-vs-trade-type, front_iv panic, correlation, sector), was the gate **considered** for this call? A documented gate that should have fired (per Phase 1 macro context) but didn't appear in `gates_fired` is a **missed gate**.
   - Did `final_size` correctly reflect the gate stack on top of `pre_risk_size`?

### Compliance metrics

- `quant_compliance_rate` = compliant_calls / total_calls
- `risk_compliance_rate` = same, for risk-monitor
- Per-gate firing rate: how often did each gate fire when it was applicable?
- **Missed-gate ledger**: every call where a gate should have fired but didn't, with the specific gate and the macro condition that triggered the obligation.

### Gate effectiveness — does the gate HELP, not just FIRE (C24)

Firing rate measures *compliance*; it says nothing about whether the gate improves outcomes. A gate that fires perfectly and downgrades winners is destroying edge with full procedural compliance. For each gate, measure effectiveness against resolved outcomes (Phase 2):

1. **Downgrade-effectiveness.** Within each `dominant_signal_class`, compare realised WR (and benchmark-excess, C21) of calls the gate **downgraded** vs comparable calls it **left alone**. A *useful* downgrade gate is one whose downgraded names realise *lower* WR/excess than the ungated peers — i.e. the gate found the losers. If downgraded names win *as often or more*, the gate is **anti-effective** (it's taxing good trades) — flag it for the desk; that is a far more expensive error than a missed firing.
2. **VETO false-positive rate (the fundamentals-gate cost).** Among `fundamentals_verdict == VETO` (and CAUTION) names that were nonetheless tracked, compute the fraction that *would have won* had they been sized. A VETO is only earning its keep if VETO'd names lose materially more than the book. Report `veto_fp_rate` = WIN / (WIN+LOSS) among VETO'd-but-resolved names. A high FP-rate means the gate is killing alpha on a fundamentals story that the flow was right to ignore.
3. **Debate-gate effectiveness.** Among names where `bear_residual ≥ bull_residual` fired the −1 debate downgrade, did they underperform names where bull won? If not, the adversarial debate is theatre, not signal.

**Activation discipline.** These effectiveness numbers need resolved outcomes — on a dataset with few decided gated names they will be **INSUFFICIENT_N (< 10 decided per gate)**. Report them as **advisory** below that floor; do **not** recommend loosening or removing a gate on thin effectiveness data (a gate's *insurance* value shows up only in the regime that hasn't happened yet — removing it in a calm tape is how desks blow up in the next one). The finding becomes actionable for Phase 7 only at ≥10 decided names per gate.

### Agent-prompt drift detection

If the missed-gate rate for any specific gate exceeds 20%, that's evidence the agent's prompt and its realised behavior have diverged. Identify which agent file needs patching (`risk-monitor.md` for risk gates; `signal-confluence-quant.md` for scoring math).

### Output

- `phase_6_decision_audit.md` — compliance rates, missed-gate ledger, **gate-effectiveness table (downgrade-effectiveness per gate + `veto_fp_rate` + debate-gate effectiveness, C24)**, per-agent drift findings. Voice: buy-side PM doing post-mortem on a fund — clinical, specific, names the agent file. State the decided-N behind every effectiveness number; mark `< 10` as advisory.
- `phase_6_decision_audit.jsonl` — per-call compliance flags + per-gate effectiveness numerics.

### Hard rules

- Never **patch** the agent file in this phase. Drift findings are inputs to Phase 7's recommendation list.
- If `score_components` is empty (legacy report), tag the call `compliance_check=skipped_legacy` and exclude from compliance rate denominators.

---

## Phase 7 — Recommendations

**Goal.** Emit a prioritized propose-only patch list. Every recommendation cites the phase and the data point that justifies it.

### Required deliverables

1. **Agent-file edits** (file path + diff intent, NOT full rewrites):
   - For each agent file flagged by Phase 6 drift detection: the specific behavior to tighten, the rule to add, the prompt section to revise.
   - For each tool tier change from Phase 4: which agent files cite that tool, and what change of language is implied.

2. **Score-rubric edits**:
   - Re-weighted components from Phase 5 — both the new weights and a rationale for each change with the Phase 4 marginal contribution.
   - Re-binned tier cuts from Phase 5.

3. **CLI tool tier movements**:
   - Promote to required: tools that are LOAD-BEARING per Phase 4.
   - Demote: tools that are NO-INFO per Phase 4.
   - Gate behind confluence: tools that are CONFOUNDED.

4. **Process changes**:
   - Confluence-gate adjustments (e.g. "require 2 independent tools cited per High-tier call" if Phase 6 shows the existing single-tool-with-confluence-≥4 escape hatch produces inferior calibration).
   - Backtest-sizing-map adjustments if Phase 3 shows the current thresholds don't match realised quintile win-rates.

### Recommendation format

Each recommendation is one heading + one paragraph. Required fields:

- **What** — one-sentence description of the change.
- **File** — `.claude/agents/<file>.md` or `.claude/commands/<file>.md` (path).
- **Phase / Data** — `Phase 4: uw dark-pool block-stratified marginal_contribution +18pp, n=22.`
- **Priority** — P0 (calibration-breaking), P1 (clear improvement), P2 (polish).
- **Risk** — what could go wrong if applied, framed for the desk.

### Output

- `phase_7_recommendations.md` — prioritized patch list. Voice: chief of staff at a multi-strat fund.

### Hard rules

- **Propose-only.** Never call `Edit` or `Write` against any file outside `analyses/audit/<YYYY-MM-DD>/`. The skill emits intentions; the user (or a separate, human-approved upgrade pass) does the editing. This is invariant — auditing the system and *editing* the system are different jobs, and the audit must never silently mutate the thing it grades.
- Every recommendation cites the phase + the data point. No vibe-driven recommendations.
- If a finding has no data behind it (data-thin pilot run), file it as P2-polish with an explicit "low confidence, needs N≥<threshold> before action" note rather than dropping it silently.
- **Provenance caps priority (C23).** A recommendation derived from **reconstructed** (prose-parsed) tool citations or from a single regime **cannot be rated P0**, regardless of effect size — P0 means "act before next session," which demands verbatim-envelope provenance at the cited N. Downgrade such findings to P1 with the provenance basis stated. (The 2026-05-29 run violated this — it proposed P0 gate-surgery off explicitly-reconstructed citations.)
- **Edge before calibration in the verdict.** When a class is both miscalibrated (Phase 3 claimed-vs-realised) *and* calibrated-but-beta (excess ≤ 0, C21), lead with the **edge** problem — a desk loses money on negative-excess long before it loses on an honest-but-wrong win-rate quote.
- **Never recommend loosening/removing a risk gate on thin effectiveness data (C24).** Gate-removal proposals require ≥10 decided gated names showing the gate is anti-effective. A gate's value is insurance against the regime not yet in the dataset; absence of evidence in a calm tape is not evidence of absence.

---

## Step 8 — Executive Summary

After all seven phases complete, write `analyses/audit/<YYYY-MM-DD>/SUMMARY.md` (≤400 words, desk-strategist voice). Required structure:

```markdown
# Calibration Audit — <date>

[DATASET-SIZE-RELAXED banner if applicable]

## Top 3 schema flaws
1. <one-line finding>. Phase 5 cite. Patch P<X>.
2. ...
3. ...

## Top 3 tool-tier surprises
1. <one-line finding>. Phase 4 cite.
2. ...
3. ...

## What we'd do Monday
<one-paragraph recommendation in JPM-Friday-note voice — what a desk would actually change next session.>
```

The summary is the document the user actually reads first. Make every word count.

---

## Failure modes & recovery

- **Phase 2 data-fetch failure mid-batch** — checkpoint partial outcomes; resume from last completed ticker on next invocation. Phase 2 is the only phase that should ever appear with a `_partial` suffix.
- **`uw historical available-dates` shows stale UW data** — abort at Step 0 (preflight). Don't compute outcomes against stale data.
- **Phase 1 yields fewer rows than expected** — if any non-empty report yields zero rows, that's a parser bug. Abort with the report path so the parser can be fixed.
- **Holdout stress-test rejects the proposal** — Phase 5 must propose a more conservative re-weight; never ship a rejected proposal forward to Phase 7.
- **Less than 5 calls in the dataset for any single signal class** — flag and exclude from per-class statistics; do not treat single-digit N as a signal.

---

## Step 9 — Save and report

1. All seven phase checkpoints written under `analyses/audit/<YYYY-MM-DD>/`.
2. `SUMMARY.md` written.
3. Print `SUMMARY.md` to chat. Nothing else — the user opens the audit folder for the rest.
