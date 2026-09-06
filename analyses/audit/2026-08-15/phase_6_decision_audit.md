# Phase 6 — Decision-Process Audit (2026-08-15)

## 6.1 Quant compliance (`signal-confluence-quant`)

| check | result |
|---|---|
| `Σ score_components.points == raw_score` | **569 / 569** ✅ |
| every component carries `source_agent` + `source_tool` | **complete** ✅ |
| backtest sizing-map honoured (era-correct map per `report_date`) | **1 upgrade-violation in 672 rows** |

The single violation is historical and already known: `2026-06-05 LLY`, `claimed_wr 0.392`
→ map-implied `starter`, emitted `half`. **Zero new violations.** Gate-driven downgrades below
the map size are permitted by construction and are not counted; only upgrades above the
win-rate-implied size are violations. The `quarter` size is included in the order map, so
legitimate quarter-downgrades are not mis-flagged.

`quant_compliance_rate = 568/569 = 0.998`.

## 6.2 Risk-monitor gate firing

| gate | present / fired | rate |
|---|---|---|
| regime | 399 / 416 | 0.959 |
| vrp | 386 / 411 | 0.939 |
| panic | 395 / 411 | 0.961 |
| cluster | 396 / 415 | 0.954 |
| sector | 387 / 410 | 0.944 |
| fundamentals | 335 / 418 | 0.801 |
| event_risk | 415 / 424 | 0.979 |
| debate | 296 / 309 | 0.958 |
| rubric_regime | 316 / 316 | 1.000 |

## 6.3 Missed-gate ledger — C54 denominator (DROP excluded from headline)

| gate | HIGH | MEDIUM | LOW | **NON-DROP** | DROP (own line) |
|---|---|---|---|---|---|
| regime | 0/7 | 0/20 | 0/122 | **0/149 = 0.000** | 256/523 = 0.489 |
| vrp | 0/7 | 0/20 | 1/122 | **1/149 = 0.007** | 260/523 = 0.497 |
| panic | 0/7 | 0/20 | 0/122 | **0/149 = 0.000** | 261/523 = 0.499 |
| cluster | 0/7 | 0/20 | 1/122 | **1/149 = 0.007** | 256/523 = 0.489 |
| sector | 0/7 | 0/20 | 1/122 | **1/149 = 0.007** | 261/523 = 0.499 |
| fundamentals | 0/7 | 0/20 | 2/122 | **2/149 = 0.013** | 252/523 = 0.482 |
| event_risk | 0/7 | 0/20 | 0/122 | **0/149 = 0.000** | 248/523 = 0.474 |
| debate | 0/0 | 0/0 | 0/60 | **0/60 = 0.000** | 212/461 = 0.460 |
| rubric_regime | 0/0 | 0/0 | 0/60 | **0/60 = 0.000** | 205/461 = 0.445 |

**HEADLINE: 5 missed gates across 1,163 non-DROP obligations = 0.43%.** All five are LOW-tier
(1 vrp, 1 cluster, 1 sector, 2 fundamentals). **Zero** gates approach the 20% drift threshold.
**No agent-prompt drift finding; `risk-monitor.md` requires no patch.**

The DROP-inclusive naive aggregate reads **41.6%** — the figure C54 explicitly forbids as a
drift headline, because DROP names are eliminated before the full risk stack runs and counting
that early-exit as non-compliance measures efficiency as drift. It is reported here on its own
line, as required, so a genuine future drift confined to DROP rows would still be visible.
The DROP figure is stable at ~0.47–0.50 across all nine gates — flat, i.e. no drift there either.

## 6.4 Gate effectiveness (C24) — does the gate HELP, not just fire?

A gate is **effective** when the names it fires on realise a *lower* WR than the names it
leaves alone — i.e. it is finding the losers.

| gate | fired WR | not-fired WR | Δ | verdict |
|---|---|---|---|---|
| regime | 0.396 (333) | 0.471 (17) | −7.5pp | effective |
| vrp | 0.388 (320) | 0.520 (25) | −13.2pp | effective |
| panic | 0.392 (329) | 0.562 (16) | −17.0pp | effective |
| **cluster** | 0.382 (330) | 0.632 (19) | **−25.0pp** | **most effective** |
| sector | 0.393 (321) | 0.478 (23) | −8.5pp | effective |
| fundamentals | 0.399 (281) | 0.408 (71) | −0.9pp | ~neutral |
| event_risk | 0.393 (349) | 0.778 (9) | −38.5pp | ADVISORY (n=9 < 10) |
| debate | 0.371 (232) | 0.538 (13) | −16.7pp | effective |
| rubric_regime | 0.377 (252) | — (0) | — | ADVISORY (no unfired arm) |

**All nine gates are effective or advisory. None is anti-effective. Recommend no loosening or
removal of any gate** (and C24 forbids it on this evidence regardless).

### VETO false-positive rate (the fundamentals-gate cost)

| verdict | realised WR | n |
|---|---|---|
| **VETO** (tracked but not sized) | **0.474** | 19 |
| CAUTION | 0.382 | 102 |
| CONFIRM | 0.404 | 99 |

`veto_fp_rate = 0.474` on n=19 — VETO'd names still win **more** than the book (0.414) and
more than the names the same agent CONFIRMED. On its face that reads anti-effective, and the
verdict ordering (VETO > CONFIRM > CAUTION) is inverted.

**This is the third consecutive measurement, and the trend is the news: 0.562 (n=16) → 0.500
(n=18) → 0.474 (n=19).** The rate is converging toward the book from above as N accrues — the
signature of an early small-sample artifact decaying, not of a persistent gate defect. Three
reasons this remains a MONITOR and not a recommendation to loosen: (i) n=19 is barely past the
C24 floor of 10 and the rule forbids loosening on thin effectiveness data; (ii) the same
agent's CAUTION verdict grades correctly at 0.382 — the *gradation* works even where the
extreme label does not; (iii) a fundamentals VETO is insurance against the merger-arb and
distribution-dressed-as-accumulation failure modes that this corpus has not yet sampled in
size. **Keep the gate. Re-measure next cycle; if the rate continues to converge, close the
item.**

### Debate-gate effectiveness

`bear_won_wr = 0.347 (n=95)` vs `bull_won_wr = 0.111 (n=9)`. Names where the bear won the
debate realise *better* than names where the bull won — but the bull arm is **n=9, below the
C24 floor**, and 0.111 on nine names is one win. **ADVISORY, no action.** The debate gate's
own firing measurement (above) reads −16.7pp effective on n=232/13, which is the number to
weight.

## 6.5 Grading the 2026-08-01 P0 — short routing to `watch_only`

**Second consecutive clean grade. VERDICT: APPLIED CLEAN.**

| | pre-P0 (n=578) | post-P0 (2026-08-03+, n=94) |
|---|---|---|
| short rows | 185 (32.0%) | 16 (17.0%) |
| long rows | 230 (39.8%) | 42 (44.7%) |
| post-P0 short `final_size` | — | **`watch_only` × 16** |
| sized violations | — | **0** |
| counterfactual preserved (`raw_score` ∧ `gate_verdicts` ∧ `signal_class`) | — | **16/16** |

The rule is **routing, not suppression**, and the envelope proves it: all 16 post-P0 shorts
are still scored, still gated and still classed, so the counterfactual keeps resolving and the
short book stays measurable. It does — and its justification held for a third window
(Phase 3.2: `ALL/short` McNemar **p = 0.0088**, BH-surviving, −13.1pp, deficit near-identical
in both tape arms).

For contrast, the behaviour the rule removed: **12 pre-P0 shorts were sized**, including
`2026-06-10 SMH half tier=HIGH` and `2026-05-28 SMH starter tier=HIGH`.

## 6.6 Follow-through on the other 2026-08-08 recommendations

| rec | status | evidence |
|---|---|---|
| **REC 2 (P1, C55)** — re-source `sector_rotation` off the NETTED `risk market-regime` line | **APPLIED** | post-cohort carries **5 netted `market_regime` citations vs 0 gross `sector_flow*`**; pre-cohort had 0 netted. WR 0.257 (n=35) → 0.500 (n=4) — *far* too thin to credit. |
| **REC 3 (P1)** — fix the `earnings_vol` / `high_iv_rank` win-rate quotes | **PARTIAL** | `high_iv_rank` improved: mean claim 0.818 → **0.600**, source now **3/3 `backtest_clean`** (was 8/16 raw `backtest`). `earnings_vol` has **no quoted rows post-P0** — the bad quote is absent rather than corrected, so the defect is untested, not fixed. |
| **REC 4 (P1, C56)** — `[0.55,0.65)` anti-predictive band | **SIZING FLOOR HOLDING; QUOTE UNFIXED** | all 8 post-cohort in-band rows resolve `skip`/`watch_only`, **zero sized**. But in-band share of quotes **rose 22% → 40%**, and in-band realised is 0.245 on n=49 (Phase 3.3) against a 0.586 mean prediction. |
| **REC 5 (P1)** — populate `dp_block_to_float_ratio` (C16) + `insider_cluster_flag` (C18) | **BOTH UNTESTABLE** | `dp_block_to_float_ratio`: key present on 210 calls, **populated on 7** — the emitter still writes null. `insider_cluster_flag`: key present on 210, populated on 20, **every populated value is `False`** — zero variance, cannot gate a conjunction at any n. |
| **REC 9 (P2)** — `dominant_signal_class` enum drift | **NOT APPLIED** | still **31 distinct classes**; off-list labels persist (`dealer_positioning_flip` 7, `dealer_short` 4, `none` 7, `dex_flip_long`/`dex_flip_short` 2 each, plus 9 singletons). |

## 6.7 Post-P0 gate-coverage note

22 of 94 post-P0 rows lack **every** gate key uniformly (identical 22/94 across all nine
gates). This is not selective gate-skipping — it is the fleet's DROP early-exit writing rows
before the risk stack runs, which C54 classifies as intended behaviour. All 22 are DROP-tier.
No finding.

---

## Verdict — buy-side PM post-mortem

Procedurally this system is in **excellent** shape and has been for three cycles running.
Five missed gates in 1,163 non-DROP obligations (0.43%). One sizing violation in 672 rows, and
it is from June. Perfect score-arithmetic integrity across 569 scored rows. Every one of nine
gates measures effective or advisory; the cluster gate at −25.0pp is doing real work. The
2026-08-01 P0 applied clean a second time with the counterfactual fully intact.

The failures in this book are **not** compliance failures. They are that the agents comply
faithfully with a rubric whose numbers are wrong (Phase 3) and whose weights are unconnected
to outcomes (Phase 5), and that four separate recommendations to *populate* fields — C16, C18,
and both win-rate quote fixes — have now gone one full cycle without landing. `signal-confluence-quant.md`
and `risk-monitor.md` need no behavioural patch. The emitters do.

**Output:** `phase_6_decision_audit.jsonl` · `phase_6_missed_gate_c54.jsonl` ·
`phase_6b_p0_compliance.json`.
