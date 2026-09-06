# Phase 6 — Decision-Process Audit · 2026-06-20

Voice: buy-side PM running a post-mortem. Clinical; names the agent file.

## Quant compliance (`signal-confluence-quant`) — essentially perfect
- **Σ `score_components.points` = `raw_score`: 174/174 (100%).** The validator is doing its job; no arithmetic drift.
- **Component provenance: 454/454 components carry both `source_agent` and `source_tool` (100%).** Every point is attributable.
- **Sizing-map: 1 upgrade-violation in the whole set.** `LLY` 2026-06-05 — claimed WR 0.392 (→ ladder implies `starter`) was pre-sized `half`. One breach; a P2 note, not a pattern. (Vol rows where `tier=DROP` carry `half`/`starter` — e.g. 6 earnings_vol structures on 06-05 — are **not** violations: vol-structure sizing is decoupled from the directional win-rate ladder by design. Worth noting only that the `tier` field is semantically meaningless for vol rows.)

## Gate coverage on sized names — 100%, NO drift
The raw missed-gate scan looked alarming (regime 29.6%, vrp 32%, event_risk 26%, fundamentals 27.8% of *scored directional* rows lack the gate key). **Stratifying by whether the name was actually sized dissolves it:**

| Gate | SIZED missing | BENCHED-scored missing |
|---|--:|--:|
| regime | **0/28** | 54/146 |
| vrp | **0/28** | 58/146 |
| event_risk | **0/28** | 45/146 |
| fundamentals | 2/28 | 49/146 |

`risk-monitor` applies the full stack to the **sized survivors**, not to every benched watch_only/skip candidate — that is the documented design, not a prompt/behaviour divergence. **No agent file needs a coverage patch.** (This is exactly the missed-gate false-positive the audit method warns about; reporting the 30% headline unstratified would have been the error.)

## Gate effectiveness (C24) — the gates fire on everything, so they can't be shown to discriminate

| Gate | fire rate | fired WR (n) | not-fired WR (n) | Δpp | status |
|---|--:|--:|--:|--:|---|
| regime | 0.94 | 0.46 (100) | 0.0 (2) | — | advisory (no control) |
| vrp | 0.92 | 0.44 (94) | 0.60 (5) | −16 | advisory |
| panic | 0.96 | 0.46 (99) | — (0) | — | advisory (no control) |
| cluster | 0.93 | 0.43 (95) | 0.67 (6) | −24 | advisory |
| sector | 0.91 | 0.45 (93) | 0.40 (5) | +5 | advisory |
| **fundamentals** | 0.77 | **0.463 (82)** | **0.455 (22)** | **+0.8** | **OK (both arms ≥10)** |
| event_risk | 0.97 | 0.46 (109) | — (0) | — | advisory (no control) |
| rubric_regime | 1.0 | 0.286 (7) | — (0) | — | advisory |

**The structural finding: most gates fire on 91–100% of rows, leaving a not-fired control arm of n=0–6.** A gate you can't turn off can't be proven to separate winners from losers. `event_risk` (fires 97%, zero control) reproduces the 2026-06-06 "90% firing / zero discrimination" flag — it is a near-constant, not a filter.

The **one** gate with both arms ≥10 — `fundamentals` — discriminates by **+0.8pp** (46.3% fired vs 45.5% not). Effectively zero.

## Fundamentals verdict vs outcome — the three verdicts are indistinguishable
| Verdict | decided WR |
|---|--:|
| CONFIRM | 0.516 (n31) |
| CAUTION | 0.484 (n31) |
| VETO | 0.500 (n4) |

CONFIRM names do **not** out-realise CAUTION names (51.6% vs 48.4%, Δ3pp on n=31/31), and the 4 tracked VETO names won 50% (`veto_fp_rate = 0.50`). On this single-regime sample the **fundamentals gate is not earning its keep on outcomes** — a reversal from the 2026-06-06 read (FP 40%, "working"). **But per the C24 activation discipline I do NOT recommend loosening or removing it:** n is single-regime, VETO n=4 is below the 10-floor, and its insurance value (it caught the NEE dividend-capture distribution dressed as accumulation) shows up in exactly the regime this dataset lacks. Logged as **advisory non-discrimination**, watch at next audit with more VETO outcomes.

## Debate gate — UNGRADEABLE (instrumentation gap)
`debate_residual_confidence` is populated on 61 rows, but the **`debate_residuals.{bull,bear}` pair needed to grade "did bear-residual-wins underperform" is carried on only 5 rows.** Bear won n=1. The debate gate cannot be evaluated from the envelope. This is not drift — it's a **schema-instrumentation gap**: `signal-confluence-quant`/`risk-monitor` should write the bull/bear residual pair into `calls[]` so the debate gate becomes auditable (pre-registration in Phase 7).

## Outputs
- `phase_6_decision_audit.jsonl` — compliance counts, per-gate firing + effectiveness numerics, veto/caution/confirm WRs, debate-gate, missed-gate (raw + the sized/benched stratification governs interpretation).
