# Phase 6 — Decision-Process Audit (2026-08-22)

## 6.1 — `signal-confluence-quant` compliance

| check | result |
|---|---|
| `Σ score_components.points == raw_score` | **634 / 634 ✅** (0 violations, 12th clean cycle) |
| every component carries `source_agent` + `source_tool` | **complete ✅** |
| backtest sizing-map honored (upgrades only are violations) | **1 violation in 634** |

The single violation is unchanged from the prior two cycles: **2026-06-05 LLY**, `claimed_wr`
0.392 → map-implied `starter`, emitted `pre_risk_size: half`. Graded against the map live on its
own `report_date`. It is a June row; nothing post-freeze repeats it. Not actionable.

## 6.2 — `risk-monitor` gate firing

| gate | present / fired | rate |
|---|---|---|
| event_risk | 463 / 472 | 0.981 |
| panic | 443 / 459 | 0.965 |
| debate | 344 / 357 | 0.964 |
| regime | 447 / 464 | 0.963 |
| cluster | 444 / 463 | 0.959 |
| sector | 435 / 458 | 0.950 |
| vrp | 434 / 459 | 0.946 |
| fundamentals | 380 / 466 | 0.815 |
| rubric_regime | 364 / 364 | **1.000** |

## 6.3 — Missed-gate ledger (C54 decomposition — DROP excluded from the headline)

| gate | HIGH | MEDIUM | LOW | **NON-DROP** | DROP (own line) |
|---|---|---|---|---|---|
| regime | 0/7 | 0/20 | 0/129 | **0/156 = 0.000** | 273/581 = 0.470 |
| vrp | 0/7 | 0/20 | 1/129 | **1/156 = 0.006** | 277/581 = 0.477 |
| panic | 0/7 | 0/20 | 0/129 | **0/156 = 0.000** | 278/581 = 0.478 |
| cluster | 0/7 | 0/20 | 1/129 | **1/156 = 0.006** | 273/581 = 0.470 |
| sector | 0/7 | 0/20 | 1/129 | **1/156 = 0.006** | 278/581 = 0.478 |
| fundamentals | 0/7 | 0/20 | 2/129 | **2/156 = 0.013** | 269/581 = 0.463 |
| event_risk | 0/7 | 0/20 | 0/129 | **0/156 = 0.000** | 265/581 = 0.456 |
| debate | 0/0 | 0/0 | 0/67 | **0/67 = 0.000** | 229/519 = 0.441 |
| rubric_regime | 0/0 | 0/0 | 0/67 | **0/67 = 0.000** | 222/519 = 0.428 |

**HEADLINE: 5 missed gates across 1,226 non-DROP obligations = 0.41%.** No gate approaches the
20% drift threshold. **No agent-prompt drift finding on any risk gate.**

*(The DROP-inclusive naive aggregate is 2,671/6,633 = 40.3%. C54 forbids that as a drift
headline — it measures the fleet's intended early-exit optimization as non-compliance. The 39
post-P0 rows carrying an entirely empty `gate_verdicts` block are **39/39 DROP tier**, i.e.
exactly that optimization, not a serialization bug.)*

## 6.4 — Gate effectiveness (C24): does the gate find the losers?

| gate | fired WR (n) | not-fired WR (n) | Δ | verdict |
|---|---|---|---|---|
| event_risk | 0.380 (397) | 0.778 (9) | **−39.8pp** | effective, **ADVISORY** (n=9 < 10) |
| cluster | 0.370 (378) | 0.632 (19) | **−26.2pp** | **effective** |
| panic | 0.379 (377) | 0.562 (16) | −18.3pp | **effective** |
| debate | 0.357 (280) | 0.538 (13) | −18.1pp | **effective** |
| vrp | 0.375 (368) | 0.520 (25) | −14.5pp | **effective** |
| sector | 0.379 (369) | 0.478 (23) | −9.9pp | **effective** |
| regime | 0.383 (381) | 0.471 (17) | −8.8pp | **effective** |
| fundamentals | 0.383 (321) | 0.405 (79) | −2.2pp | marginal |
| rubric_regime | 0.363 (300) | — (0) | — | ADVISORY (no unfired arm) |

**Every gate with a measurable arm is effective** — gated names realise materially *lower* WR
than the ungated peers. Not one gate is anti-effective. **No gate may be loosened or removed
(C24).**

### 6.4a — The fundamentals VETO is now the one gate going the wrong way

| verdict | WR | n |
|---|---|---|
| **VETO** | **0.545** | 22 |
| CONFIRM | 0.391 | 110 |
| CAUTION | 0.342 | 120 |
| *book baseline* | *0.402* | *637* |

`veto_fp_rate` has now converged from below the book to **above** it, three cycles running:
**0.562 → 0.500 → 0.474 → 0.545**. VETO'd names out-win CONFIRM'd names by **15.4pp** and the
book by 14.3pp. On n=22 this is not yet a finding — but the *ordering* (VETO > CONFIRM >
CAUTION) is now inverted end to end, and the fundamentals gate is simultaneously the weakest
effectiveness reading in 6.4 (−2.2pp). **Two independent instruments on the same gate.** Per
C24 this cannot justify loosening it; it justifies **registering it and watching**.

### 6.4b — Debate gate is inverted, but at the advisory floor

`bear_won` (the −1 downgrade fired): **0.318 on n=129.** `bull_won`: **0.100 on n=10.** The gate
assumes bull-won names are the better book; the data says the opposite. **n=10 is exactly the
C24 advisory floor** — report, do not act. Note this cuts *against* loosening the gate, since
the downgrade arm is the better-performing one.

## 6.5 — 2026-08-01 P0 short-routing: compliance perfect, **intent drifting**

**Letter of the rule: clean, third consecutive cycle.**

| check | result |
|---|---|
| post-P0 short calls (2026-08-03+) | 28 |
| `final_size` distribution | `watch_only` 25, `skip` 3 |
| **shorts sized above `watch_only`** | **0 violations ✅** |
| counterfactual preserved | `raw_score` 28/28, `dominant_signal_class` 28/28, `gate_verdicts` 27/28 |

**Spirit of the rule: a real, statistically clear drift.** The P0 is written as *routing, not
suppression* — "theses are still generated, scored and serialized so the counterfactual keeps
resolving." The fleet has instead **roughly halved its short-thesis generation rate**:

| cohort | short share of board | Fisher two-sided p |
|---|---|---|
| pre-P0, all regimes | 185/578 = **32.0%** | |
| post-P0, all regimes | 28/159 = **17.6%** | **0.00035** |
| **pre-P0, uptrend only** | **56/179 = 31.3%** | |
| **post-P0, uptrend only** | **25/144 = 17.4%** | **0.0045** |

**Regime does not explain it.** Holding the regime bucket fixed at `uptrend`, the short share
still falls 31.3% → 17.4% (p = 0.0045). The Phase-3 evidence that justified the P0
(`ALL/short` McNemar p = 0.0026, −14.5pp, symmetric across tape) **depends on shorts continuing
to be generated and resolved**. At the current rate the counterfactual accrues ~28 rows per
5 weeks instead of ~60, and the statistic that keeps the P0 honest decays. **This is the one
genuine drift finding this cycle** → Phase 7 P1 #1.

## 6.6 — Follow-through on the 2026-08-15 recommendations

| rec | status | evidence |
|---|---|---|
| **P1 #1** canonical tool ids | **LANDED ✅** | post-fix: 17 ids / 134 instances, **0 concatenations** (was 122 ids / 1,225, 9.9% concatenated). Phase 4's atomic table is measurable for the first time in 12 cycles. |
| **P1 #2** class-support check on `win_rate_source` | **LANDED ✅** | post-fix **0 unsupported-class backtest quotes** (was 37 corpus-wide); `earnings_vol` quoted **0 of 21 rows**; `high_iv_rank` now quotes 0.600 mean on `backtest_clean` only (was 0.818 on mixed `backtest`). |
| **P1 #4** retire C15 / C18 | **LANDED ✅** | C15 trigger confirmed never met (0 HIGH squeeze readings in 198 populated rows; `n_hi_si` = 0 of 22 short rows). C18 `insider_cluster_flag` **`False` 22/22** — zero variance confirmed. |
| **P1 #3** `[0.55,0.65)` re-derivation | **WITHDRAWN, correctly** | C56's post-fix denominator is **19 of a required 30** and did not advance. In-band share of quotes rose 22% → **35%** and realises **0.125 (n=8)** post-P0; sizing discipline holds (all post-fix in-band rows `skip`/`watch_only`). |
| **P2 #7** `dominant_signal_class` enum | **HALF-LANDED ⚠️** | off-list labels collapsed 14 → 1, but the survivor is **new**: `vol_long` on 5 post-fix rows (2026-08-18 LITE/NBIS/AMAT/CRWV/SNDK). The emitter learned a fresh off-list label after the fix. |
| **P1 #5** keep freeze | **HELD ✅** | Phase 5.2: cuts still non-monotone at ≥9; post-freeze HIGH n=0 / MEDIUM n=1. |

### C16 — first sign of life in eight cycles

`dp_block_to_float_ratio` is **now populated on 10 calls (9 decided)** — the 08-15 backfill-duty
sharpening worked. WR 0.222 (n=9) vs a 0.397 `dark_pool_accumulation` baseline. But look at the
ordering, not the average:

| ratio | ticker | outcome |
|---|---|---|
| 0.0023 | NBIS | **WIN** |
| 0.0022 | SNDK | **WIN** |
| 0.00058 | CRWV | LOSS |
| 0.00036 | SE | LOSS |
| 0.0001 | NOW | LOSS |
| 0.0001 | MSFT | LOSS |
| 7.4e-05 | AXON | LOSS |
| 4.4e-05 | GOOGL | LOSS |
| 1.1e-05 | AAPL | LOSS |

**Perfect rank separation at ~0.001** — the two largest float-normalized blocks are the only two
winners (random-assignment p = 1/C(9,2) = 0.028). This is a **post-hoc threshold on n=9** and
must not be promoted. It is exactly what a pre-registration is for → **C62** (Phase 5.4).

## Verdict — buy-side PM post-mortem

Procedurally this fleet is in the best shape it has been in twelve audits. **0/634 scoring-math
errors, 5/1,226 missed non-DROP gates (0.41%), one June-era sizing violation, nine gates all
effective or advisory, and four of five shipped recommendations landed clean and verifiable in
the very next cohort.** That last item is new and it matters: this is the first cycle where the
audit could *confirm its own prior prescriptions took* rather than re-litigate them.

The two things a PM would actually raise in the meeting are both about **intent, not
compliance**: the short book is being quietly written out of existence (6.5) at the exact moment
its counterfactual is the strongest statistic the system owns, and the fundamentals VETO has
inverted against its own book (6.4a). Neither is a rule violation. Both are the kind of drift
that only shows up if you grade the spirit of a rule alongside its letter.
