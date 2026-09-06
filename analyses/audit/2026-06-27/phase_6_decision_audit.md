# Phase 6 — Decision-Process Audit (2026-06-27)

Provenance: verbatim envelope `gate_verdicts` + `score_components`. Voice: buy-side PM post-mortem.
Gate-effectiveness needs ≥10 decided/arm; below that = advisory (C24).

## 1. Quant compliance — near-perfect, no drift

- **Σ score_components.points == raw_score: 205 / 205.**
- **Provenance complete (every component has source_agent + tool): TRUE.**
- **Sizing-map violations (upgrade above win-rate-implied size): 1 / 205.** Only `LLY 2026-06-05`
  (claimed_wr 0.392 → implied `starter`, sized `half`). One borderline half vs starter on a 0.39 quote;
  immaterial. The size vocabulary (`full|half|quarter|starter|skip`) and the 0.70 full-line are honored
  everywhere else. **`signal-confluence-quant` is executing its documented procedure.** No scoring drift.

## 2. Gate firing rates (present / fired)

| gate | rate | | gate | rate |
|---|---|---|---|---|
| event_risk | 0.948 | | cluster | 0.889 |
| rubric_regime | 1.000 | | panic | 0.886 |
| regime | 0.897 | | sector | 0.849 |
| vrp | 0.850 | | fundamentals | 0.762 |
| | | | debate | 0.658 |

All gates fire when applicable. `rubric_regime` (the freeze/half-cap gate) fires 100%.

## 3. Gate effectiveness (C24) — every gate is net-protective; none anti-effective

"Fired" = the gate produced a non-pass verdict. A *useful* downgrade gate makes fired-WR **lower** than
not-fired-WR (it found the losers). Every gate clears that bar:

| gate | fired WR (n) | not-fired WR (n) | Δ pp | status |
|---|---|---|---|---|
| cluster | 0.421 (107) | 0.786 (14) | −36.5 | OK |
| panic | 0.453 (106) | 0.727 (11) | −27.4 | OK |
| vrp | 0.436 (101) | 0.688 (16) | −25.2 | OK |
| sector | 0.450 (100) | 0.625 (16) | −17.5 | OK |
| regime | 0.464 (110) | 0.583 (12) | −11.9 | OK |
| fundamentals | 0.465 (99) | 0.520 (25) | −5.5 | OK |
| event_risk | 0.455 (123) | 0.857 (7) | −40.2 | advisory (notfired n=7) |
| debate | 0.556 (9) | 0.750 (8) | −19.4 | advisory |
| rubric_regime | 0.542 (24) | — (0) | — | advisory |

**Read carefully:** negative Δ = the gate is *working* (flagged names underperform). **No gate is
anti-effective** (none has fired-WR ≥ not-fired-WR on adequate N), so there is **no data basis to loosen
or remove any gate** — and per C24 discipline you don't loosen insurance in a calm-then-pulling-back
tape anyway. The not-fired buckets are small (the gates fire on almost everything), so treat the
*magnitudes* as advisory; the *sign* is consistent and protective.

### The P0.6 OUT-OF-REGIME half-cap — first protective evidence (thin, n=10)
| arm | n | WR | excess |
|---|---|---|---|
| out_of_regime (half-capped) | 10 | **0.30** | **−16.7pp** |
| in_regime | 195 | 0.477 | +2.5pp |

The names the half-cap down-sized realised 30% WR / −16.7pp — **they were bad trades, and the cap
limited the loss.** This is the first audit with direct evidence the half-cap *protects* rather than
taxes (n=10, right at the floor → advisory, but it points the safe direction). **Keep the half-cap.**

### VETO / fundamentals-gate cost
VETO_wr 0.40 (n=5) · CAUTION 0.50 (n=38) · CONFIRM 0.51 (n=35). VETO'd-but-tracked names underperform
CONFIRM (0.40 vs 0.51) — the gate is mildly protective. n=5 VETO → advisory; **veto_fp_rate not
actionable, do not loosen.**

### Debate-gate — possible theatre, but n=7
Bear-won names (residual ≥ bull) realised 0.857 (n=7); bull-won n=0 this slice. On its face the −1
debate downgrade flagged names that *won* — anti-effective — but n=7 is far below the floor. **Advisory
only; flag for re-test, do not act.**

## 4. Missed-gate ledger

| gate | scored-dir rows missing the key | rate |
|---|---|---|
| vrp | 62 / 200 | 0.31 |
| regime | 58 / 200 | 0.29 |
| fundamentals | 55 / 200 | 0.275 |
| event_risk | 52 / 200 | 0.26 |

These ~30% "missing-key" rates exceed the 20% drift threshold **on paper**, but the cause is structural,
not drift: the missing-key rows are overwhelmingly **watch_only / DROP** candidates that never entered
the Phase-2 risk stack, so `gate_verdicts` is legitimately empty for them. Among *sized/considered*
rows the keys are present. **This is a measurement artifact of including watch-only rows in the
denominator — not evidence that `risk-monitor.md` skips gates.** (To make this a clean drift metric, a
future audit should restrict the denominator to `final_size ∈ {sized}` rows.)

## Verdict

The decision process is **executing as documented.** Scoring math reconciles 205/205, provenance is
complete, sizing discipline holds (1 immaterial exception), every risk gate fires and every one is
net-protective, and the half-cap now has its first (thin) protective data point. There is **no agent
drift to patch and no gate to loosen.** The system's problem is not process compliance — it is that the
*rubric it faithfully executes* mis-ranks conviction at the top (Phase 3). Fix the rubric inputs (Phase
5/7), not the operators.

**Output:** `phase_6_decision_audit.jsonl`.
