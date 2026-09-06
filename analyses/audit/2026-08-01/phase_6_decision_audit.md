# Phase 6 — Decision-Process Audit (2026-08-01)

Buy-side PM post-mortem voice. Population: 578 envelope rows, 100% verbatim provenance.

## 6.1 Quant compliance (`signal-confluence-quant`)

| check | result |
|---|---|
| `Σ score_components.points == raw_score` | **480/480 — zero violations** |
| Every component carries `source_agent` + `source_tool` | **complete** |
| Backtest sizing-map upgrade violations | **1** |

The single violation: **2026-06-05 LLY**, `claimed_wr = 0.392` → map implies
`starter/skip`, emitted `pre_risk_size = half`. That is an *upgrade* above the
win-rate-implied size, which is the only direction the rule forbids. It is a **pre-freeze**
row under the era-correct map, and it is the only one in 480 scored calls.

Sizing-map grading used the era-correct thresholds per the skill's era rule: rows before
2026-07-25 graded against `[0.55,0.65) → half`, rows after against
`[0.55,0.65) → starter`. Grading post-fix rows against the old map (or vice versa) would
manufacture false positives; it did not.

## 6.2 Gate firing rates

| gate | fired / present | rate |
|---|---|---|
| event_risk | 343/352 | 0.974 |
| panic | 323/339 | 0.953 |
| regime | 327/344 | 0.951 |
| cluster | 324/343 | 0.945 |
| debate | 224/237 | 0.945 |
| sector | 315/338 | 0.932 |
| vrp | 314/339 | 0.926 |
| fundamentals | 275/346 | 0.795 |
| rubric_regime | 244/244 | 1.000 |

## 6.3 Gate **effectiveness** (C24) — does the gate find losers?

A useful downgrade gate is one whose *fired* arm realises **lower** WR than its
*not-fired* arm. Every evaluable gate does.

| gate | fired WR | not-fired WR | Δ | status |
|---|---|---|---|---|
| cluster | 0.408 (282) | 0.688 (16) | **−28.0pp** | effective |
| vrp | 0.414 (273) | 0.571 (21) | −15.7pp | effective |
| panic | 0.421 (278) | 0.562 (16) | −14.1pp | effective |
| debate | 0.409 (181) | 0.538 (13) | −12.9pp | effective |
| sector | 0.419 (272) | 0.524 (21) | −10.5pp | effective |
| fundamentals | 0.412 (243) | 0.500 (58) | −8.8pp | effective |
| regime | 0.426 (284) | 0.467 (15) | −4.1pp | effective |
| event_risk | 0.421 (299) | 0.750 (8) | −32.9pp | **ADVISORY** (n=8) |
| rubric_regime | 0.413 (201) | — (0) | — | ADVISORY (no arm) |

**All nine gates grade correct or advisory. None is anti-effective.** `cluster` at
−28.0pp is the standout — the correlation gate is finding genuinely worse names, not
taxing good ones.

## 6.4 VETO false-positive rate

| verdict | realised WR | n |
|---|---|---|
| VETO | **0.562** | 16 |
| CAUTION | 0.369 | 84 |
| CONFIRM | 0.476 | 82 |

`veto_fp_rate = 0.562` on n=16 — VETO'd names won *more* than the book (0.435), which
reads anti-effective on its face. Three reasons this is **not** a recommendation to loosen
the gate:

1. n=16 is barely past the C24 floor of 10, and the skill's hard rule explicitly forbids
   loosening a gate on thin effectiveness data.
2. The same agent's **CAUTION** verdict grades correctly and strongly (0.369 vs 0.476
   CONFIRM) — the gate's discrimination is real; it is the top-severity bin that reads odd.
3. Most VETO'd names were also killed by other gates, so their counterfactual is not
   "would have been sized."

**Monitor. Do not loosen.** The VETO caught the merger-arb blind spot (NUVL) and the
ORCL/Pentagon short save; its value is insurance against the regime not in the dataset.

## 6.5 Debate-gate effectiveness

| outcome | WR | n |
|---|---|---|
| bear won (−1 downgrade fired) | 0.361 | 61 |
| bull won | 0.500 | 6 |

The adversarial debate is **signal, not theatre** — names where the bear carried the
argument realised 14pp worse. n=6 on the bull arm is thin, so this is directional.

## 6.6 Missed-gate ledger — C54 decomposition

**The C54 correction is doing exactly what it was registered to do.** The raw
DROP-inclusive aggregate would again read ~30–32% on four gates and flag `risk-monitor.md`
for drift. Decomposed:

| gate | HIGH | MEDIUM | LOW | **non-DROP rate** | DROP (own line) |
|---|---|---|---|---|---|
| regime | 0/7 | 0/20 | 0/104 | **0.0%** | 234/447 |
| panic | 0/7 | 0/20 | 0/104 | **0.0%** | 239/447 |
| event_risk | 0/7 | 0/20 | 0/104 | **0.0%** | 226/447 |
| vrp | 0/7 | 0/20 | 1/104 | 0.8% | 238/447 |
| cluster | 0/7 | 0/20 | 1/104 | 0.8% | 234/447 |
| sector | 0/7 | 0/20 | 1/104 | 0.8% | 239/447 |
| fundamentals | 0/7 | 0/20 | 2/104 | 1.5% | 230/447 |
| debate | 7/7 | 20/20 | 62/104 | **67.9%** | 252/447 |

Aggregate non-DROP: **94 misses across 1,048 gate-row checks = 8.97%**, entirely
attributable to `debate`.

### The `debate` exception is an era artifact, not drift

| era | debate missing, non-DROP |
|---|---|
| `era_0525_0529` | 32/32 = **100%** |
| `era_0530_0605` | 38/38 = **100%** |
| `pre_freeze_post_0606` | 19/19 = **100%** |
| **`2026-06-12` (live)** | **0/42 = 0.0%** |

The bull/bear debate stage was wired into the envelope at the freeze. Every "miss" is a
row that predates the stage's existence. Grading pre-freeze rows against a post-freeze
gate is the same denominator error C54 was registered to fix, one axis over.

### Live-rubric compliance (the number that matters)

Restricting to the frozen `2026-06-12` era, non-DROP rows (n=42):

| gate | non-DROP missed | rate |
|---|---|---|
| regime, vrp, event_risk, fundamentals, panic, cluster, sector, debate, rubric_regime | **0/42 each** | **0.0%** |

**Zero drift on the live rubric across all nine gates.** No agent file requires patching.
`risk-monitor.md` and `signal-confluence-quant.md` are executing their documented
procedure exactly.

## 6.7 Applied-recommendation verification (2026-07-25 → live)

| 07-25 rec | status | evidence |
|---|---|---|
| P0 #1 — demote excess, promote McNemar | **APPLIED (auditor)** | Phase 3 §3.4 / 3d; C49 replicates (slope −81.9, R² 0.611) |
| P1 #2 — close C19 as REFUTED (C53) | **APPLIED + confirmed** | `bearish_flow` 0.500 vs 0.49 (n=106, p=0.918); negative excess in both tapes |
| P1 #3 — C54 missed-gate denominator | **APPLIED + confirmed** | §6.6: aggregate would misread ~31%; decomposed = 0.0% non-DROP |
| P1 #4 — `[0.55,0.65)` floor + provenance | **APPLIED, partially effective** | 15/15 post-fix quotes `backtest_clean`; 11/11 in-band rows size to `skip`. **But** band share rose 25.0% → 73.3% and realised WR is still ≈0.29 → **C56** |
| P1 #5 — envelope fields | **HALF APPLIED** | `debate_residuals` floor 0.55→0.15 ✅ (22 rows now carry sub-0.55); `insider_cluster_flag` on 44/44 post-fix calls ✅ (C18 unblocked); **`dp_block_pct_of_float` still absent → C16 untestable a 4th cycle** ❌ |
| P1 #6 — keep freeze + half-cap | **APPLIED** | Phase 5 §5.3 / §5.4; half-cap −12.0pp, protective |

Output: `phase_6_decision_audit.jsonl`, `phase_6_missed_gate_c54.jsonl`,
`phase_6_live_rubric_compliance.jsonl`, `phase6_decision.py`.
