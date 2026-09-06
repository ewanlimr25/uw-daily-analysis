# Phase 6 — Decision-Process Audit

Clinical post-mortem on whether `signal-confluence-quant` and `risk-monitor` actually executed the documented procedure. Compliance is only checkable on rows carrying structured `score_components` / `gate_verdicts`.

## Quant compliance (`signal-confluence-quant`)

| Check | Result |
|---|---|
| Rows with **structured** (dict) components | 63 |
| Rows with **prose-string** components (not machine-checkable) | 190 |
| `Σ score_components.points == raw_score` | **63 / 63 (100%)** |
| All components carry named `source_agent` + `source_tool` | 51 / 63 (12 legacy rows have anonymous components) |

**The Σ-invariant is perfect wherever it can be checked.** The 2026-05-23 audit's "5-of-58 rows components≠raw_score" defect is **resolved** — the rubric-line-keyed component format (shipped after that audit) holds. The real limitation: **75% of component-bearing rows (190/253) are legacy prose strings**, so the scoring math is *unauditable* on the bulk of history. This is not a compliance failure; it is a **data-completeness gap that the decision-envelope rollout (this week, 54 structured calls) directly closes.** Post-rollout reports are 100% machine-auditable.

## Sizing-map compliance

Backtest sizing map (`≥0.65→full, 0.50–0.65→half, <0.50→starter/skip`), allowing legitimate gate **downgrades**:

| Check | Result |
|---|---|
| Rows with win_rate + pre_risk_size | 213 |
| Compliant or correctly-downgraded | **201 / 213 (94.4%)** |
| Apparent upgrade violations | 12 |

The 12 flagged are mostly **not real violations**:
- **W18 MU / INTC sized `quarter`** against win_rate 0.78–0.80 — these are *downgrades* (quarter < full) misflagged because `quarter` is an unmapped size string in the audit's order map. **False positive** (and a note: `quarter` is a size bucket the rubric emits but the documented map only defines full/half/starter/skip — add `quarter` to the map).
- **CELH / WRBY / DDOG / ABNB 05-06 sized `half` at win_rate 0.0** — earnings vol-crush condors inheriting the *directional* `bearish_flow` 0.0 WR. The 0.0 doesn't govern a vol structure, but the rubric applied a directional rate to a vol trade. **Classification leak, not a sizing breach** (the C13 router should prevent directional WR attaching to vol classes).
- **MU 05-11 sized `full` at win_rate 0.0** — the one genuine violation worth a look.

Net: sizing discipline is sound; the noise is vol-structures inheriting directional win-rates and an unmapped `quarter` bucket.

## Risk-monitor gate firing (32 envelope rows with `gate_verdicts`)

| Gate | Fired / applicable |
|---|---|
| event_risk | **21 / 32 (66%)** |
| fundamentals | 17 / 30 (57%) |
| regime | 8 / 32 |
| cluster | 8 / 32 |
| vrp | 5 / 32 |
| sector | 4 / 32 |
| panic | 4 / 32 |

The gate stack is **active and differentiated** — event_risk and fundamentals are the workhorses (the dense June macro calendar + the Finnhub cross-check doing real CAUTION/VETO work). No gate is dead. This is healthy: the risk layer is not a rubber stamp.

## Missed-gate ledger (event_risk)

8 envelope swing/weekly calls carried a **high-impact event inside the horizon** with a `no-op` event_risk verdict:

| Date | Ticker | Event | Event date |
|---|---|---|---|
| 05-28 | SMH, ASTS, P, MSFT, BRKR | NFP (May) | 06-05 |
| 05-29 | MSFT, SMH | NFP (May) | 06-05 |
| W22 | MSFT | AVGO earnings (amc) | 06-03 |

These are all events at **T+4 to T+5 trading days**. The 05-26 book shows event_risk *does* fire at T+2 (PCE). The pattern suggests the gate applies a **tight T+2 window** and under-weights events at T+3–T+5, which for a 1–4-week **swing** horizon are squarely in-window. **Missed-gate rate ≈ 8/29 applicable ≈ 28% — above the 20% drift threshold** → `risk-monitor.md`'s event_risk window should be widened from ~T+2 to the full swing horizon (or apply a graduated −0.5/−1 by proximity). This is the one actionable drift finding.

## Verdict

The decision *process* is compliant where instrumented: the scoring math is exact (Σ-invariant 100%), sizing is 94% disciplined, and the risk gates fire with real differentiation. The two findings:
1. **Auditability is the constraint, not compliance** — 75% of history is prose-only; the envelope rollout fixes this going forward (no agent patch needed, just continued rollout).
2. **event_risk gate window is too tight** for the swing horizon (28% miss on T+3–T+5 high-impact events) → `risk-monitor.md` patch (Phase 7).

## Output
- `phase_6_decision_audit.jsonl` — compliance numerics + missed-gate ledger. `phase6_decision.py` — reproducible.
