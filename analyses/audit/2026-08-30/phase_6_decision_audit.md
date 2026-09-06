# Phase 6 — Decision-Process Audit (2026-08-30)

## 6.1 Quant compliance (`signal-confluence-quant`)

| check | result |
|---|---|
| `Σ score_components[].points == raw_score` | **675 / 675** ✅ |
| every component carries `source_agent` **and** `source_tool` | **complete** ✅ |
| sizing-map upgrade violations (era-correct map per `report_date`) | **1** |

The single violation is **2026-06-05 LLY** — `claimed_wr` 0.392 implies `starter`, emitted
`half`. Pre-freeze era, 12 weeks stale, already-superseded map. No live defect.

`quant_compliance_rate = 674/675 = 99.85%`.

## 6.2 Risk-monitor compliance — gate firing

| gate | present / fired | rate |
|---|---|---|
| regime | 499/516 | 0.967 |
| vrp | 486/511 | 0.951 |
| panic | 495/511 | 0.969 |
| cluster | 496/515 | 0.963 |
| sector | 487/510 | 0.955 |
| fundamentals | 429/518 | 0.828 |
| event_risk | 515/524 | 0.983 |
| debate | 396/409 | 0.968 |
| rubric_regime | 416/416 | **1.000** |

## 6.3 Missed-gate ledger — **C54 denominator (DROP excluded from the headline)**

| gate | HIGH | MEDIUM | LOW | **NON-DROP** | DROP (own line) |
|---|---|---|---|---|---|
| regime | 0/7 | 0/20 | 0/133 | **0/160 = 0.000** | 273/629 = 0.434 |
| vrp | 0/7 | 0/20 | 1/133 | **1/160 = 0.006** | 277/629 = 0.440 |
| panic | 0/7 | 0/20 | 0/133 | **0/160 = 0.000** | 278/629 = 0.442 |
| cluster | 0/7 | 0/20 | 1/133 | **1/160 = 0.006** | 273/629 = 0.434 |
| sector | 0/7 | 0/20 | 1/133 | **1/160 = 0.006** | 278/629 = 0.442 |
| fundamentals | 0/7 | 0/20 | 2/133 | **2/160 = 0.013** | 269/629 = 0.428 |
| event_risk | 0/7 | 0/20 | 0/133 | **0/160 = 0.000** | 265/629 = 0.421 |
| debate | — | — | 0/71 | **0/71 = 0.000** | 229/567 = 0.404 |
| rubric_regime | — | — | 0/71 | **0/71 = 0.000** | 222/567 = 0.392 |

**HEADLINE: 5 missed gates across 1,262 non-DROP gate-obligations = 0.40%.**
**No gate exceeds the 20% drift threshold. No agent-file drift finding this cycle.**

(For contrast, the DROP-inclusive naive aggregate is 2671/7101 = **37.6%** — the figure C54
forbids as a drift headline, because DROP names are eliminated before the full stack runs.
That is the fleet's intended early-exit optimization, not non-compliance.)

## 6.4 Gate effectiveness (C24) — does the gate HELP, not just FIRE

| gate | fired WR | not-fired WR | Δ | status |
|---|---|---|---|---|
| event_risk | 0.358 (452) | 0.778 (9) | **−42.0pp** | advisory (n<10 in arm) |
| cluster | 0.349 (433) | 0.632 (19) | −28.3pp | ✅ effective |
| debate | 0.331 (335) | 0.538 (13) | −20.7pp | ✅ effective |
| panic | 0.356 (432) | 0.562 (16) | −20.6pp | ✅ effective |
| vrp | 0.352 (423) | 0.520 (25) | −16.8pp | ✅ effective |
| sector | 0.356 (424) | 0.478 (23) | −12.2pp | ✅ effective |
| regime | 0.360 (436) | 0.471 (17) | −11.1pp | ✅ effective |
| fundamentals | 0.358 (372) | 0.398 (83) | −4.0pp | ✅ weakly effective |
| rubric_regime | 0.338 (355) | — (0) | — | advisory (no unfired arm) |

**Every measurable gate is effective** — downgraded names underperform ungated peers by
−4.0 to −42.0pp. Eighth consecutive cycle. **Recommend no loosening or removal of any gate**
(C24 forbids it on thin data regardless; here the data is not even thin).

### The fundamentals VETO is now clearly anti-effective

| verdict | WR | n |
|---|---|---|
| **VETO** | **0.524** | 21 |
| CONFIRM | 0.376 | 117 |
| CAUTION | 0.328 | 131 |

`veto_fp_rate = 0.524`. **VETO'd names win 14.8pp MORE than CONFIRM'd names** and 19.6pp more
than CAUTION'd names — the ordering is exactly inverted. The trajectory across cycles:
0.562 → 0.500 → 0.474 → 0.545 → **0.524**, and this is the second cycle where VETO > CONFIRM.
Decided n=21, past the ≥10 actionability floor.

**Do not loosen the gate on this** — C24's insurance argument holds and a fundamentals VETO
is the mechanism that caught the merger-arb and dividend-capture blind spots in the memory
register. But it is no longer defensible to leave the gate uninstrumented: the audit can see
*that* names are VETO'd, never *why*. **Instrument the reason, then grade the reasons
separately** — that is the P1 below, not a gate change.

### Debate gate is inverted, thinly

`bear_won` names 0.315 (n=146) vs `bull_won` 0.154 (n=13). Names where the bear won the
debate outperform names where the bull won. The bull arm is **n=13** — advisory only, and the
direction is confounded (a bull win routes toward sizing, which routes into the gates). Note
and re-measure; no action.

## 6.5 Follow-through on prior recommendations

### The 2026-08-22 P1 #1 generation floor — **it worked, decisively**

| period | short share of board |
|---|---|
| pre-P0 (< 2026-08-03) | 185/578 = **32.0%** |
| post-P0, pre-fix (08-03 … 08-21) | 28/159 = **17.6%** |
| **POST-FIX (≥ 2026-08-22)** | **23/52 = 44.2%** |

Fisher, pre-fix vs post-fix: **p = 0.0003**. **Regime-controlled at `uptrend`** (the 08-22
audit's own control): 31.3% → 17.4% → **60.0%**, Fisher **p = 0.0007**. The starvation
identified last cycle is reversed on the first week of data after the edit.

**Watch item, not yet a finding.** Post-fix short share is now *above* the pre-P0 baseline —
overall 44.2% vs 32.0% (p = 0.0896, ns) but at fixed `uptrend` regime **60.0% vs 31.3%
(p = 0.0422)**. n=15 uptrend rows. A generation *floor* becoming a generation *quota* would
be the mirror-image defect. **Re-measure next cycle before touching anything.**

### The 2026-08-01 P0 (shorts → `watch_only`) — clean a 4th cycle

51 post-P0 short rows: **46 `watch_only`, 4 `skip`, 1 `veto`. 0 sizing violations.**
Counterfactual serialization preserved on 45/51; the 6 exceptions are **all DROP rows**
(5 carry the full 9-key `gate_verdicts` with `raw_score = 0` and no components — legitimate
early exit under C54; 1 is a DROP `SPY` row with no gate keys). No non-DROP short is
under-serialized. The counterfactual that keeps the P0 falsifiable is intact.

### Other prior recs

| rec | status |
|---|---|
| **REC 3 (08-15 P1)** — fix `earnings_vol` / `high_iv_rank` WR quotes | ✅ working. `earnings_vol`: 13 quoted rows @ mean 0.871 pre, **0 quoted rows post**. `high_iv_rank`: mean claim 0.818 → **0.600**, and source moved to `backtest_clean` on 6/6. The 0.87 lie in Phase 3.3 is **entirely historical**. |
| **REC 4 (C56)** — `[0.55,0.65)` band | ✅ compliant. Post-fix in-band sizes: `watch_only` 5, `skip` 6 — **zero sized above starter**. Band still realises 0.100 (n=10 post-fix). |
| **REC 5** — `dp_block_to_float_ratio` emission | ✅ fixed within class (10/13 August accumulation rows; 0/55 before). See Phase 4.4. |
| **REC 5b** — `insider_cluster_flag` | ❌ **UNTESTABLE — zero variance.** 30 populated, every value `False`. C18 confirmed dead. |
| **REC 9** — class-enum drift | ✅ 31 → **17** distinct classes; the only off-list survivor (`vol_long` ×5) is pre-fix and now aliased. **0 off-list in 52 post-fix rows.** |

## 6.6 Compliance verdict

`quant_compliance_rate` **99.85%** · `risk_compliance_rate` (non-DROP) **99.60%** ·
**no agent-file drift finding.** Three of the four prior-cycle recommendations verified
working; the fourth (`insider_cluster_flag`) is confirmed unfixable and should be retired
rather than re-recommended.

Outputs: `phase_6_decision_audit.jsonl` · `phase_6_missed_gate_c54.jsonl` ·
`phase_6b_p0_compliance.json`
