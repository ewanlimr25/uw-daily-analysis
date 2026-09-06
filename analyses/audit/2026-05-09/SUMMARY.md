# Calibration Audit — 2026-05-09

> **DATASET-SIZE-RELAXED**: 7 daily + 2 weekly reports below the 10/3 default thresholds. ~52 of 131 calls had resolvable forward windows. Read every number below as directional, not statistical. Structural findings (rubric weights, gate compliance, tool tiers) are higher confidence than numerical findings (Brier, per-class win-rates).

The fleet is structurally sound. Tier monotonicity holds (HIGH 92% > MED 89% > LOW 80% realised). The W18 (85.7%) and W19 (88.2%) directional accuracy numbers are real — *we are calling the market well*. Two failure modes leak through anyway: the rubric is too proud at the top end (claimed 100% on calls that realise 80%) and the gate stack erodes silently in the long tail of the book.

## Top 3 schema flaws

1. **`today_gamma_flip` worth +2 in the swing rubric** is a NO-INFO contribution (±0pp marginal) — the tool is right for 0DTE pin-vs-trend reads only, but it bleeds into swing scores and inflates them. Restricting to 0DTE alone (R-04, P0) drops AAPL 2026-05-08 from raw=9 to raw=7, AMZN 2026-05-08 from raw=5 to raw=3 — both consistent with their actual conviction.
2. **`claimed_win_rate=1.00` in the audit trail** drives the LOSS-row Brier penalty almost single-handedly. Capping at 0.90 (R-01, P0) mechanically halves the dominant residual. Cheapest single change in the audit.
3. **`flow_conflict` has no rubric weight** — Q5 quintile dipped because NVDA 2026-05-08 raw=10 LOSS had flow_conflict flagged in the audit trail but received no point penalty. Risk-monitor docked the trade to starter via the gate stack; the score remained 10. Add −2 (R-05, P0).

## Top 3 tool-tier surprises

1. **`dp_block_size_stratified` is the alpha** — +18pp marginal contribution. Every dark-pool accumulation call without it is institutional-grade only by accident; promote to required citation (R-08, P0).
2. **`oi_trend` (the most-cited tool, n=28) is supportive, not load-bearing** — only +5pp marginal because it's correlated with the actual load-bearing tools. Reduce its rubric weight from +2 to +1 (R-07, P0). Counterintuitive: the tool the agents lean on hardest is doing the least independent work.
3. **`conviction_matrix > 70%` is uncrossable in TRANSITIONAL** — 0 LEAP candidates cleared the threshold across the dataset despite confirmed multi-day OI builds and DP defenses. Either the gate is over-specified or the conviction-matrix tool is computing wrong; either way, the LEAP pipeline produces zero entries every single day. Audit before next week's run (R-10, P1).

## What we'd do Monday

Apply the 8 P0 recommendations to the agent files before next week's run. The two highest-leverage changes are R-01 (cap claimed_win_rate at 0.90) and R-03 (force explicit VRP verdict per call in risk-monitor) — both purely mechanical, both fix Brier or drift directly. Defer the tier re-bin (R-09, HIGH ≥ 8 instead of ≥ 5) until we accumulate 50+ more resolved calls — the data trend supports it but N=52 is too thin to lock in. The conviction-matrix LEAP gate (R-10) needs a separate investigation of the matrix tool's internals before we either lower the threshold or rewrite the gate logic; until then we keep producing zero LEAP entries every day.

The desk's 88% W19 hit-rate is genuine. The recommended changes don't turn this into a different system — they tighten what already works.

*— Calibration Audit, 2026-05-09. Seven phases, propose-only, all checkpoints in this directory.*

---

**P0 APPLIED 2026-05-09.** All 8 P0 recommendations (R-01 through R-08) shipped to `.claude/agents/signal-confluence-quant.md`, `.claude/agents/risk-monitor.md`, `.claude/commands/daily-analysis.md`, and `.claude/commands/weekly-analysis.md`. Notable scope decisions: R-04 was daily-only (weekly's gamma-flip-tracker is already demoted to forward-looking §9 with no rubric weight); R-07 was daily-only (weekly's +3 `oi_trend` weight is justified by full-week observation window vs daily's ≥5-day lookback). P1 / P2 items remain DEFERRED pending N ≥ 100 resolved calls. See `phase_7_recommendations.md` for the per-rec status table.
