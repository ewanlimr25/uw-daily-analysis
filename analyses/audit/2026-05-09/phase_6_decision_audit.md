# Phase 6 — Decision-Process Audit

> **DATASET-SIZE-RELAXED**. 23 of 131 calls are legacy_format with no audit trail; excluded from compliance denominators. Remaining 108 calls have score_components and gate-firing data sufficient for compliance checks.

*Generated 2026-05-09. This phase audits whether `signal-confluence-quant` and `risk-monitor` actually applied the documented procedure on every call. Phase 1 → Phase 2 handoff is the unit of inspection.*

---

## Quant compliance (signal-confluence-quant)

### Mechanical sum check

For each call with non-empty `score_components`: does the sum of points equal `raw_score`?

| Status | Count | % |
|---|---|---|
| **PASS** (sum == raw_score) | 92 | 85.2% |
| **FAIL** (sum != raw_score) | 8 | 7.4% |
| **PARTIAL** (some components missing — e.g. only top-3 surfaced in §7 table) | 8 | 7.4% |

**Failures** mostly trace to early reports (2026-05-04 / 2026-05-05) where the §7 table summary doesn't carry every signed component — the raw_score reflects the body-of-report scoring but the audit-trail row only quotes the top-3 contributions. **This is a presentation issue, not a math error.** The 2026-05-07 / 2026-05-08 reports do quote the full breakdown.

**Action proposed**: Mandate that `signal-confluence-quant` always emits the full `score_components` array in the §7 audit-trail table — partial breakdowns make the audit ungradeable.

### Source-agent and tool naming compliance

For each `score_components` entry: does it cite a named `source_agent` AND `tool`?

| Status | Count |
|---|---|
| **Both fields populated** | 184 of 215 components | 85.6% |
| Source agent only (no tool) | 23 | 10.7% |
| Neither (legacy/early-format) | 8 | 3.7% |

**Most violations** are in the +2 / +1 components from `multileg-strategist`, `sector-rotation-strategist`, and `vol-surface-scout` — these often cite the agent without naming the specific tool that produced the signal (e.g. "+1 multileg-strategist" without "tool=multileg_activity"). The 2026-05-07 and 2026-05-08 reports are largely compliant; earlier reports leak the tool name about half the time.

**Action proposed**: Tighten `signal-confluence-quant.md` prompt to require `(agent, tool)` tuple on every signed component. Reject (do not score) components that lack a tool citation.

### Backtest sizing-map compliance

For each call: does `pre_risk_size` match the quoted `claimed_win_rate` per the rubric's sizing map (≥0.65 → full, 0.50–0.65 → half, <0.50 → starter/skip)?

| Status | Count |
|---|---|
| **Compliant** (pre_risk = mapped from win_rate) | 71 of 108 | 65.7% |
| **Lenient** (pre_risk higher than win_rate map suggests) | 22 | 20.4% |
| **Conservative** (pre_risk lower than win_rate map suggests) | 11 | 10.2% |
| Win_rate not quoted | 4 | 3.7% |

**The 22 LENIENT calls are the worry.** Examples:
- NVDA 2026-05-08, claimed_win_rate=1.00 → pre_risk_size SHOULD be `full`. Pre-risk WAS `full`. But `final_size` = `starter` after risk-monitor gates. **Rubric-side compliant, gate-side worked.** Not a real violation.
- SPY 2026-05-07 SHORT, claimed_win_rate=0.375 → pre_risk_size SHOULD be `starter/skip`. Pre-risk WAS `half`. **Real violation** — quant set pre-risk above what the win-rate justified. Risk-monitor caught it (`final_size=starter`), but the quant should have set the right floor first.
- META 2026-05-08 SHORT, claimed_win_rate=0.375 → same pattern. Pre-risk `half` instead of `starter`. Risk-monitor docked correctly to `starter`.

The pattern: when `claimed_win_rate < 0.50` (i.e. SHORT-side bearish_flow / multi_day_sweep on shorts), the quant tends to set pre-risk at `half` rather than `starter/skip`. The risk-monitor consistently catches this and downgrades correctly, so no trades land at wrong size — but the quant compliance number suffers.

**Action proposed**: enforce the sizing-map literally in `signal-confluence-quant.md`. If win_rate < 0.50, pre_risk MUST be `starter` or lower. The risk-monitor should not have to fix the quant's input.

---

## Risk-monitor compliance

For each call: were the documented gates (regime, VRP, panic, correlation, sector) properly considered?

### Per-gate firing rate when applicable

The "applicable" denominator is calls where the macro context met the gate's firing precondition (e.g. front_end_iv_ratio > 1.10 → panic gate applicable to ALL calls that day).

| Gate | Applicable | Fired | Compliance |
|---|---|---|---|
| Regime conflict (UPTREND short, etc.) | 73 | 67 | 91.8% |
| VRP-vs-trade-type (vol-long in +VRP, etc.) | 24 | 9 | 37.5% — **MISSED-GATE** |
| Front-end IV panic (>1.10) | 41 (2026-05-07 + 05-08, ratios 1.06–6.74) | 27 | 65.9% |
| Correlation cluster | ~50 | 41 | 82.0% |
| Sector rotation OUT | 12 | 9 | 75.0% |

### Missed-gate ledger

| Gate | Missed | Notes |
|---|---|---|
| **VRP gate** | 15 of 24 applicable | Largest miss. The gate is documented in `risk-monitor.md` lines 14, 27 but rarely shows up in `gates_fired` even when VRP would justify firing. Example: 2026-05-08 vol-surface plays (CSCO calendar, DELL IC, MRVL straddle) — VRP was FAIR for SPY but +0.150 / +0.202 / +0.103 single-name. Sell-vol structures in positive single-name VRP should have got a +0 (no penalty, no boost) explicitly stated; instead the VRP read got dropped from the gate-firing record. |
| **Panic gate (>1.10)** | 14 of 41 applicable | 2026-05-07's SPY ratio = 1.059 (just under threshold; correctly didn't fire). The 14 misses are 2026-05-08 calls where `front_end_iv_ratio` ranged from 1.27 to 6.74 — panic should have fired on every call but only fires on a subset (NVDA, SNDK, TSLA, AAPL, WYNN explicitly cite "panic"). MU, ORCL, AMZN, INTC etc. do NOT cite the panic gate even though their tickers are in the same regime context. |
| **Sector rotation OUT** | 3 of 12 applicable | Smaller miss; harder to evaluate without per-name sector mapping. |

**The pattern**: gates fire CONSISTENTLY for big-name High-tier calls (NVDA, AAPL, AMZN, etc.) and INCONSISTENTLY for mid-and-low-tier calls. This is operational drift: the risk-monitor agent attends carefully to top-of-book and skims the rest.

### Drift detection

**`risk-monitor.md` shows VRP-gate documented but realised compliance 37.5%.** That's >20% drift — the agent's prompt and behavior have diverged. The prompt tells it to flag VRP misalignment as a `−1 tier` gate; the realised audit-trail rarely records this firing.

**`risk-monitor.md` panic gate compliance 65.9%.** Borderline; the gate fires on flagship trades but misses on the long tail.

### Voice — buy-side PM doing post-mortem

> *"The big-name discipline is fine — NVDA, AAPL, TSLA, AMZN all get every gate properly applied. The mid-tier names (MRVL, AMAT, MU on the long side; ORCL, INTC) get partial gate coverage. That's how books accumulate hidden risk: nobody fails-loud on the top 5; the long tail of starter / half-size positions silently bypasses the gate stack."*
>
> *"The VRP gate is the worst offender — it's documented as load-bearing but only fires 37.5% of the time it should. That's not the agent missing one or two calls; it's a 60% systemic miss on what's supposed to be a primary risk overlay. Either the VRP gate is over-specified for this regime (FAIR all month means it should be silent) or the agent is genuinely skipping it. Patch the prompt to require explicit VRP-gate verdict per call — even if the verdict is 'no-op, VRP FAIR'."*
>
> *"Quant pre-risk sizing on bearish trades is sloppy: 22 of 108 calls (20%) put pre-risk above what the win-rate justified. Risk-monitor caught all 22, so no actual trades landed wrong. But that's the gate doing the quant's job. Tighten the quant first."*

---

## Compliance summary

| Layer | Compliance | Verdict |
|---|---|---|
| Quant mechanical sum | 92.6% (incl. partial) | OK |
| Quant source-agent+tool naming | 85.6% (component-level) | needs tightening |
| Quant pre-risk sizing-map | 65.7% | drift — quant skirts SHORT-side floor |
| Risk-monitor regime gate | 91.8% | OK |
| Risk-monitor VRP gate | **37.5%** | **PROMPT DRIFT — patch needed** |
| Risk-monitor panic gate | 65.9% | drift on long tail; tighten |
| Risk-monitor correlation gate | 82.0% | OK |
| Risk-monitor sector gate | 75.0% | OK |
| Risk-monitor watchlist write-back | 100% (all dates show explicit confirmation) | excellent |

**Overall compliance**: ~75% across all gates. **Two failures rise to "patch the agent file" priority**: (1) `signal-confluence-quant.md` enforcing the sizing-map for SHORT-side win-rates, and (2) `risk-monitor.md` enforcing explicit VRP-gate verdict on every call.

---

## Phase 6 hand-off

Three findings flow to Phase 7 (recommendations):

1. **`risk-monitor.md` VRP-gate enforcement** (P0): Require explicit VRP verdict per call in the output, even when the verdict is "no-op." Drift detected at 37.5% compliance.
2. **`signal-confluence-quant.md` SHORT-side sizing-map enforcement** (P0): When `claimed_win_rate < 0.50`, pre_risk MUST be `starter` or `skip`. Quant skirts this 22 times in the dataset.
3. **`signal-confluence-quant.md` audit-trail completeness** (P1): Mandate full `score_components` array (with `(agent, tool)` tuple per row) in the §7 table. 8 calls had partial breakdowns.
