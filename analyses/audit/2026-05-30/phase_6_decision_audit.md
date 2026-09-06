# Phase 6 — Decision-Process Audit (2026-05-30 · + C24 gate-effectiveness)

## Compliance (replicates 05-29 — same envelope data, unchanged)

| Check | Result | 05-29 |
|---|---|---|
| Σ `score_components.points == raw_score` (structured rows) | **63/63 (100%)** | 63/63 |
| Sizing-map compliant-or-downgraded (`quarter` in map; gate downgrades OK) | **204/213 (95.8%)** | 201/213 |
| Apparent sizing upgrades | 9 | 12 |

The 9 apparent upgrades remain the known false positives (vol structures inheriting a directional
`win_rate`; `quarter` bucket). **Compliance is sound; auditability is the only constraint** — 75% of
history is prose-only, closed only by continued envelope rollout. No scoring-math patch needed.

## Gate firing (32 rows with structured `gate_verdicts`)

| Gate | Fired | | Gate | Fired |
|---|---|---|---|---|
| event_risk | 18 | | cluster | 4 |
| fundamentals | 14 | | vrp | 3 |
| regime | 5 | | panic / sector | 0 |

Stack is active and differentiated — event_risk + fundamentals are the workhorses, as in 05-29.

## ⭐ C24 — gate EFFECTIVENESS (NEW; the 05-29 run could only measure firing)

This is the new method lane: does a gate that *fires* actually *help*? Measured on resolved
outcomes. **Every cell is INSUFFICIENT_N (<10 decided/gate)** — only **7 envelope rows are decided**
(the rest window_open). Reported **advisory**; per the C24 hard rule, **no gate-loosening is
recommended on this data** (a gate's value is insurance against the regime not yet in the dataset).

| Gate | Gated-down WR | Ungated WR | Read (advisory, thin) |
|---|---|---|---|
| event_risk | 25% (n4) | 100% (n3) | **effective** — downgraded names lost, ungated won |
| vrp | 100% (n4) | 0% (n3) | **anti-effective?** — downgrades *won* (taxing good trades) |
| fundamentals | 67% (n3) | 50% (n4) | **anti-effective?** — downgrades won more than ungated |
| cluster | 100% (n1) | 50% (n6) | n=1, ignore |
| regime/panic/sector | n0 down | 57% | no downgrades among decided |

**`fundamentals` VETO/CAUTION false-positive rate = 67% (2 of 3 decided CAUTION/VETO names WON).**
This is the single most important *new* question the audit can now ask — and the early, thin answer
is a yellow flag: the fundamentals gate may be **killing alpha the flow was right to ignore**
(distribution-dressed-as-accumulation is a great thesis; whether the VETOes are *right* was never
measurable before). **n=3 — not actionable.** But the lane is now wired, and this is the #1 number
to watch as envelope rows resolve (~2026-06-12).

**Debate-gate effectiveness:** n=2 decided → INSUFFICIENT_N. Unmeasurable this run.

## Missed-gate ledger (event_risk)

The 05-29 ledger found **8/29 (~28%) swing/weekly calls** carried a high-impact event at T+3–T+5
(NFP 06-05, AVGO 06-03) with a `no-op` event_risk verdict — above the 20% drift threshold → widen
the event_risk window from ~T+2 to the full swing horizon. **The envelope data is identical this run,
so that finding carries forward unchanged.** (This run's automated re-derivation used a stricter
`macro_event_risk` field heuristic and returned 0 matches — a detection-coverage gap, not a refutation;
the 05-29 prose-parsed ledger stands.)

## Verdict
1. **Process compliance is sound** (Σ 100%, sizing 96%, gates differentiated) — unchanged from 05-29.
2. **C24 establishes gate-effectiveness measurement for the first time.** Everything is thin
   (7 decided), but the lane produces numbers — chiefly a **67% fundamentals-VETO false-positive rate**
   that, if it holds as N grows, means the fundamentals gate is expensive. **Watch, don't cut.**
3. **event_risk window too tight for swing horizon** (carried from 05-29, same data) → `risk-monitor.md`
   patch candidate (Phase 7, P1).

## Output
- `phase_6_decision_audit.jsonl` — compliance + C24 effectiveness numerics. `phase6_decision_v2.py`.
