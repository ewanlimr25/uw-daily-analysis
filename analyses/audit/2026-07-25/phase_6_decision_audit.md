# Phase 6 — Decision-Process Audit (2026-07-25)

Voice: buy-side PM running a post-mortem. Provenance verbatim.

## 6.1 Quant compliance — `signal-confluence-quant`

| check | result |
|---|---|
| `Σ score_components.points == raw_score` | **434 / 434 (100%)** |
| Every component carries `source_agent` **and** `source_tool` | **complete** |
| Backtest sizing-map honored (≥0.70 full / 0.50–0.70 half / <0.50 starter-skip, `quarter` in-order) | **1 upgrade violation** |

The single violation: **2026-06-05 LLY**, `claimed_wr` 0.392 → implied `starter`, but
`pre_risk_size` = `half`. Pre-freeze, pre-model-pin, and already noted in prior audits.
No post-freeze violations. **`signal-confluence-quant` is clean.**

The 2026-07-03 model pins (quant + risk-monitor on fable/high, multileg on opus/high)
remain clean at their second checkpoint: 434/434 Σ, full provenance, zero sized blowups.

## 6.2 Gate firing rates — `risk-monitor`

| gate | present / fired | rate |
|---|---|---|
| regime | 281 / 296 | 0.949 |
| vrp | 270 / 291 | 0.928 |
| panic | 275 / 291 | 0.945 |
| cluster | 279 / 295 | 0.946 |
| sector | 269 / 290 | 0.928 |
| fundamentals | 238 / 298 | 0.799 |
| event_risk | 296 / 304 | 0.974 |
| debate | 176 / 189 | 0.931 |
| rubric_regime | 196 / 196 | 1.000 |

## 6.3 Gate **effectiveness** (C24) — does the gate find losers?

A useful downgrade gate produces a **negative** delta: the names it fires on do worse.

| gate | fired WR | not-fired WR | delta | status |
|---|---|---|---|---|
| regime | 0.417 (n=235) | 0.467 (n=15) | −5.0pp | OK |
| vrp | 0.402 (n=224) | 0.571 (n=21) | −16.9pp | OK |
| panic | 0.410 (n=229) | 0.562 (n=16) | −15.2pp | OK |
| cluster | 0.395 (n=233) | 0.688 (n=16) | **−29.3pp** | OK |
| sector | 0.408 (n=223) | 0.524 (n=21) | −11.6pp | OK |
| fundamentals | 0.402 (n=204) | 0.500 (n=48) | −9.8pp | OK |
| event_risk | 0.412 (n=250) | 0.750 (n=8) | −33.8pp | ADVISORY (n<10) |
| debate | 0.386 (n=132) | 0.538 (n=13) | −15.2pp | OK |
| rubric_regime | 0.395 (n=152) | — (n=0) | — | ADVISORY |

**Every gate with an evaluable arm is effective.** Not one is anti-effective. The
`cluster` gate is the standout at −29.3pp. This is the most unambiguously positive
result in the audit: the risk stack is doing exactly what it is designed to do, and the
gates are the reason the DROP pile outperforms the traded book.

## 6.4 VETO false-positive rate — **the one anti-effective finding**

| verdict | WR | n |
|---|---|---|
| **VETO** | **0.545** | 11 |
| CAUTION | 0.375 | 72 |
| CONFIRM | 0.449 | 69 |
| *book baseline* | *0.425* | *440* |

`veto_fp_rate` = **0.545** — VETO'd names won *more often* than the book. All 11:

| date | ticker | dir | tier | outcome |
|---|---|---|---|---|
| 2026-06-01 | META | short | LOW | LOSS |
| 2026-06-02 | MU | short | MEDIUM | **WIN** |
| 2026-06-09 | MU | short | DROP | LOSS |
| 2026-06-11 | MSFT | short | LOW | **WIN** |
| 2026-06-17 | NVDA | short | DROP | LOSS |
| 2026-06-29 | CG | long | DROP | **WIN** |
| 2026-07-01 | TSM | short | DROP | **WIN** |
| 2026-07-02 | MRNA | long | LOW | **WIN** |
| 2026-07-17 | NVDA | short | DROP | LOSS |
| 2026-07-22 | GOOG | short | DROP | **WIN** |

n=11 is *barely* at the C24 ≥10 actionable floor, 8 of the 11 were DROP/LOW (killed by
other gates anyway), and `CAUTION` — the same agent's softer verdict — grades correctly
at 0.375. **Per the skill's hard rule, this is NOT a recommendation to loosen the
fundamentals VETO.** A gate's value is insurance against the regime not yet in the
dataset, and 11 names is not a mandate. Filed as a monitored pre-registration.

## 6.5 Missed-gate ledger — **it is an auditor bug, not agent drift**

Raw missed-gate rates looked alarming: regime 34.1%, vrp 35.1%, event_risk 32.7%,
fundamentals 33.4% — all far past the 20% drift threshold. Decomposed by tier:

| gate | HIGH | MEDIUM | LOW | DROP |
|---|---|---|---|---|
| regime | 0/7 | 0/20 | 0/94 | **211/374** |
| vrp | 0/7 | 0/20 | 1/94 | **215/374** |
| event_risk | 0/7 | 0/20 | 0/94 | **206/374** |
| fundamentals | 0/7 | 0/20 | 2/94 | **207/374** |

**Every single miss is a DROP row.** HIGH, MEDIUM and LOW are essentially 100%
gate-complete (3 misses across 121 rows). DROP names are eliminated *before* the full
risk stack runs — which is correct, efficient behaviour, not drift.

The prior audits' missed-gate rates were computed on a denominator that included DROP
rows and therefore measured the fleet's early-exit optimization as non-compliance.
**No agent-prompt drift is detected. `risk-monitor.md` needs no patch.** Registered as
auditor fix **C54**.

## 6.6 Debate-gate effectiveness

bear_won WR 0.346 (n=52) vs bull_won WR 0.333 (**n=3**). The bull arm is n=3 — the
comparison is uninformative. What *is* informative: the debate gate as a firing
mechanism grades −15.2pp (§6.3), so the debate is contributing. Its *directional*
resolution cannot be graded until more names survive to a bull verdict.

**Schema defect carried from 2026-07-23 (still unfixed):** `debate_residuals` has no
bin below 0.55, which erased TSLA's 0.42/0.40 residuals on 2026-07-23. Any residual
below 0.55 is currently unrepresentable. Filed in Phase 7.

Outputs: `phase_6_decision_audit.jsonl`.
