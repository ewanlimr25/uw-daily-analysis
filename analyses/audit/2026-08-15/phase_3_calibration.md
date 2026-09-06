# Phase 3 — Calibration Audit (2026-08-15)

## HEADER (C49 — read before any class commentary)

**Excess-column artifact regression**, 36 strata cells (n ≥ 8 each):

```
OLS  excess_pp = +35.4 − 81.1 × spy_wr        R² = 0.557
     sd(bookWR) = 0.1022   sd(spyWR) = 0.1365   DISPERSION RATIO = 0.748
     var(excess)=220.1  var(bookWR)=104.4  var(spyWR)=186.4
     benchmark share of excess variance = 64.1%
     book WR range [0.222, 0.700] spread 0.478 · spy WR range [0.186, 0.778] spread 0.592
```

A slope of −81.1 against the −100 pure-artifact line, R² 0.557, dispersion 0.748: **64% of
this cycle's excess column is the benchmark moving, 36% is the book.** Marginally better than
07-25's 64% / R² 0.636 and 08-08's reading, but the verdict is unchanged — **every excess
number below is annotated, none leads a finding, and none may carry a priority above P2.**
(The 31-cell McNemar-family variant reads R² 0.329 / dispersion 0.886; the 36-cell figure
above is the canonical C49 statistic and the conservative one.)

**Primary edge test is the tape-conditioned book WR + row-matched paired McNemar below.**

---

## 3.1 Per-class table (decided N ≥ 8; BH at FDR 0.10 across the class set)

| class | n | realised | claimed | divergence | spyWR | excess ⚠ | p | BH |
|---|---|---|---|---|---|---|---|---|
| bearish_flow | 120 | 0.458 | 0.50 | 4.5pp | 0.585 | −12.6pp | 0.374 | n |
| **earnings_vol** | 109 | **0.394** | **0.87** | **47.7pp** | 0.667 | −27.2pp | **0.000** | **Y** |
| **multileg_directional** | 80 | **0.375** | 0.56 | **18.0pp** | 0.356 | +1.9pp | **0.002** | **Y** |
| bullish_flow | 57 | 0.421 | 0.53 | 10.4pp | 0.315 | +10.6pp | 0.149 | n |
| dark_pool_accumulation | 53 | 0.434 | 0.55 | 12.0pp | 0.420 | +1.4pp | 0.105 | n |
| **sector_rotation** | 39 | **0.282** | 0.54 | **25.4pp** | 0.306 | −2.4pp | **0.002** | **Y** |
| dealer_positioning | 28 | 0.536 | 0.60 | 6.1pp | 0.481 | +5.4pp | 0.635 | n |
| **high_iv_rank** | 27 | **0.481** | **0.79** | **31.2pp** | — | — | **0.001** | **Y** |
| oi_build | 13 | 0.462 | — | — | 0.333 | +12.8pp | 1.000 | n |
| multi_day_sweep | 11 | 0.636 | 0.38 | −25.7pp | 0.300 | +33.6pp | 0.152 | n |
| gamma_breakout | 10 | 0.200 | 0.51 | 31.1pp | 0.556 | −35.6pp | 0.094 | n |
| opex_pin ⚠ | 9 | 0.111 | — | — | — | — | 1.000 | n |
| event_vol | 8 | 0.500 | — | — | — | — | 1.000 | n |

> **⚠ CORRECTION (applied 2026-08-15, post-publication — C59 resolved in-cycle).** The
> `opex_pin` 0.111 is a **measurement artifact of the auditor, not a result about the lane.**
> Re-resolving the same 9 rows under the settlement rule (distance from entry at window END,
> which is what an iron fly / short straddle actually pays on) instead of the touch rule (any
> ±1R intraday excursion = LOSS) gives **0.667**, and **5 of 9 rows diverge** — clearing C59's
> pre-registered bar of ≥3. The mechanism is stark: **PFE settled at 0.00% from entry and was
> scored LOSS** on a 3.34% intraday brush; XLF settled 0.05%, NVDA 0.12% and 0.21%. The headline
> table above is left on the touch rule so this cycle stays comparable with the prior ten
> audits; `phase_2_outcomes.jsonl` now carries **both** (`outcome` = touch, `outcome_settle` =
> settlement, `pin_rule_divergent`). **The next audit should switch the headline to
> `outcome_settle` for pin rows.** Nothing else in this phase is affected — `opex_pin` is 9 of
> 572 decided rows and enters no other statistic.

THIN_N appendix (decided 5–7): **empty** this cycle.

**Four BH-surviving divergences, all in the same direction: the rubric quotes high and
delivers ~0.40.**

## 3.2 PRIMARY EDGE TEST — paired McNemar (row-matched, C49)

BH applied **within** pre-registered families (7 primary direction × tape cells; per-class
sweep is exploratory). Family pooling would be a post-hoc power tax — this is the 2026-08-01
lesson and it is honoured here.

| cell | n | bookWR | spyWR | Δ | b | c | p | BH | family |
|---|---|---|---|---|---|---|---|---|---|
| **ALL / short** | 183 | 0.426 | 0.557 | **−13.1pp** | 27 | 51 | **0.0088** | **YES** | primary |
| **ALL / long** | 216 | 0.426 | 0.329 | **+9.7pp** | 49 | 28 | **0.0220** | **YES** | primary |
| UP / short | 114 | 0.368 | 0.491 | −12.3pp | 15 | 29 | 0.0488 | no | primary |
| UP / long | 97 | 0.485 | 0.371 | +11.3pp | 24 | 13 | 0.0989 | no | primary |
| DOWN / short | 69 | 0.522 | 0.667 | −14.5pp | 12 | 22 | 0.1214 | no | primary |
| DOWN / long | 119 | 0.378 | 0.294 | +8.4pp | 25 | 15 | 0.1539 | no | primary |
| ALL | 399 | 0.426 | 0.434 | −0.8pp | 76 | 79 | 0.8724 | no | primary |
| *CLASS bearish_flow* | 118 | 0.466 | 0.585 | −11.9pp | 20 | 34 | 0.0759 | no | expl |
| *POST-FREEZE / short* | 139 | 0.446 | 0.547 | −10.1pp | 23 | 37 | 0.0925 | no | expl |

**The short deficit survives BH for a third consecutive cycle** (p = 0.0115 → 0.0038 →
**0.0088**) and its long mirror for a third (+9.7pp, p = 0.0220 — identical to last cycle).
Critically, the deficit is **again near-identical in both tapes** (−12.3pp up / −14.5pp
down). That is the **mis-selection** signature, not mistiming: if the book were merely early
or late, one arm would carry the damage.

**Direction-call accuracy** confirms it independently: in an UP tape the book positioned with
the tape on 114/234 = **48.7%**; in a DOWN tape, 69/188 = **36.7%**. The fleet is a coin-flip
on side-selection in a rising tape and materially worse than a coin-flip in a falling one.

## 3.3 Reliability diagram (the miscalibration is localized, not diffuse)

| bucket | n | predicted | realised | |
|---|---|---|---|---|
| [0.00,0.50) | 69 | 0.39 | 0.43 | ✅ honest |
| [0.50,0.55) | 50 | 0.52 | 0.54 | ✅ honest |
| **[0.55,0.60)** | 34 | 0.57 | **0.23** | 🚩 |
| **[0.60,0.65)** | 15 | 0.62 | **0.27** | 🚩 |
| [0.65,0.70) | 7 | 0.66 | 0.57 | ok |
| [0.70,0.80) | 8 | 0.77 | 0.75 | ✅ |
| **[0.80,0.90)** | 31 | 0.83 | **0.45** | 🚩 |
| [0.90,1.01) | 6 | 0.93 | 0.50 | 🚩 thin |

**Brier = 0.2866 · log-loss = 0.7946 · graded n = 220.** Brier is past the 0.25
"no-better-than-coin-flip" line and log-loss confirms the cause is the confident tail: the
≥0.80 bucket (n=37) realises **0.459**, and it is 14 `high_iv_rank` + 12 `earnings_vol` rows.

**The `[0.55,0.65)` band, third cycle running: n=49, mean prediction 0.586, realised
0.245** (one-sided binomial p = 1×10⁻⁶). This is not noise and it is not drifting — it is a
stable, strongly *anti*-predictive band. The 2026-07-25 starter-floor is holding on the
sizing side (all 5 post-2026-08-01 in-band rows resolved `skip`/`watch_only`, zero sized),
but the **quoted number has still never been re-derived**.

## 3.4 Tier reliability — inversion, 7th consecutive cycle

| tier | n | WR |
|---|---|---|
| HIGH | 7 | **0.143** |
| MEDIUM | 19 | **0.526** |
| LOW | 108 | 0.389 |
| DROP | 438 | 0.420 |

Realised order **MEDIUM > DROP > LOW > HIGH**. Stratified by era, the inversion is present in
every one:

| era | HIGH | MEDIUM | LOW | DROP |
|---|---|---|---|---|
| era_0525_0529 | 0.250 (4) | 0.556 (9) | 0.579 (19) | 0.571 (21) |
| era_0530_0605 | 0.000 (2) | 0.500 (10) | 0.400 (25) | 0.419 (31) |
| pre_freeze_post_0606 | 0.000 (1) | — | 0.353 (17) | 0.500 (8) |
| **2026-06-12 (FROZEN)** | **— (0)** | **— (0)** | **0.319 (47)** | **0.410 (378)** |

By regime bucket the same shape holds (uptrend HIGH 0.200 n=5 vs DROP 0.448 n=134;
transitional_other LOW 0.200 n=10 vs DROP 0.388 n=160).

## 3.5 Score → win-rate (the ordering the rubric claims to produce)

`−3: 0.37(19) · −2: 0.70(10) · −1: 0.40(47) · 0: 0.44(111) · 1: 0.41(150) · 2: 0.36(91) ·
3: 0.40(53) · 4: 0.40(40) · 5: 0.55(11) · 6: 0.46(13) · 7: 0.71(7) · 8: 0.29(7) · 9: 0.67(6) ·
10: 0.00(3) · 11: 0.33(3) · 12: 0.00(1)`

Across the mass of the distribution (scores −1 … 4, n=402) realised WR sits in a **0.36–0.44
band with no slope**. The high scores that look good (7 → 0.71, 9 → 0.67) sit on n=7 and n=6
against 10 → 0.00 and 12 → 0.00. The score carries no usable ordering information.

## 3.6 P0.6 out-of-regime half-cap grading (6th measurement)

| | n | WR | excess ⚠ |
|---|---|---|---|
| out_of_regime | 43 | **0.326** | −23.5pp |
| in_regime | 529 | 0.422 | +1.3pp |
| rubric_regime gate FIRED | 252 | 0.377 | −8.4pp |
| rubric_regime ungated | 320 | 0.444 | +4.8pp |

Out-of-regime rows underperform by **−9.6pp** on n=43 decided — negative in all six
measurements taken. **Keep the half-cap.**

## 3.7 C3 — expectancy + Kelly live-activation gate

| tier | n | mean P&L | payoff ratio | capped ½-Kelly |
|---|---|---|---|---|
| HIGH | 7 | −2.441% | 0.72 | 0.0 |
| MEDIUM | 19 | +0.104% | 0.948 | 0.0132 |
| LOW | 108 | −1.963% | 1.008 | 0.0 |
| DROP | 438 | −2.870% | 0.787 | 0.0 |

**GATE STATUS: `ADVISORY_ONLY`.** Reason: n = 27 closed sized calls (< 30 floor) **and**
tier × expectancy is non-monotone (LOW −1.784 > HIGH −1.965 > MEDIUM −2.239 on the gate's
own sized-call basis). Do **not** flip `signal-confluence-quant` / `risk-monitor` to the Kelly
sizer. The win-rate ladder stays live.

---

## Verdict

### (a) Where the rubric is honest

The **low half of the confidence scale is well calibrated**: [0.00,0.50) predicts 0.39 and
delivers 0.43 (n=69); [0.50,0.55) predicts 0.52 and delivers 0.54 (n=50); [0.70,0.80)
predicts 0.77 and delivers 0.75 (n=8). `bearish_flow` (claim 0.50 → realised 0.458, n=120)
and `dealer_positioning` (0.60 → 0.536, n=28) are honest quotes. When this system says
"probably a coin flip," it is telling the truth.

### (b) Where it lies to itself

Four BH-surviving divergences, all overconfident. **`earnings_vol` quotes 0.87 and realises
0.394 on n=109 — a 47.7pp lie and its fifth consecutive appearance.** The mechanism is
unchanged and still verifiable from the envelope: 12 of the 13 quoted rows cite
`win_rate_source: backtest`, but `uw historical signal-backtest` supports only five signal
classes and **`earnings_vol` is not among them** — that number was never measured.
`high_iv_rank` is the identical defect (0.79 → 0.481, n=27; 8 of 16 quoted rows cite
`backtest`). `sector_rotation` is the worst realised class in the book at **0.282 on n=39**
against a 0.54 quote. `multileg_directional` quotes 0.56 and delivers 0.375 on n=80.

Desk read: *"`earnings_vol` prints 0.87 on the ticket and settles at four-in-ten across a
hundred and nine names. That is not a model that drifted — the substrate it claims to have
queried does not carry the class. Anyone sizing off that number is sizing off a typo that has
survived five audits."*

And on rotation: *"`sector_rotation` calls 0.54 and books 0.282 across thirty-nine names. A
28% hit rate is not a weak signal, it's a signal with the sign on backwards — you'd have made
money fading the desk's own rotation calls."*

### (c) Tier inversions / High-tier overconfidence

Seventh consecutive cycle of inversion; HIGH is the **worst** bucket in the corpus at 0.143
(n=7) while DROP — the names the fleet explicitly refuses — books 0.420 on n=438. The
inversion is present in all four rubric eras and all four regime buckets. It is not a
small-sample artifact of the HIGH bucket alone: LOW (0.389, n=108) also loses to DROP.
The score→WR ladder has no slope across the region carrying 70% of the mass.

### (d) Calibrated-but-beta

Per C49 this label requires calibration ✅ **and** a non-significant paired McNemar **and**
excess ≤ 0 — the row-matched test agreeing with the excess column.

- **`bearish_flow` — CALIBRATED-BUT-BETA.** Claim 0.50 / realised 0.458 (honest, p=0.374);
  McNemar p = 0.0759 (non-significant); excess −12.6pp. All three agree. It rides the tape;
  it does not beat it. Note its book WR barely moves between tapes (0.413 up → 0.527 down)
  while its excess sits at −11.1pp / −12.7pp — **stable book, stable deficit**.
- **`dark_pool_accumulation` — CALIBRATED-BUT-BETA, and the cleanest example in the corpus.**
  McNemar exactly p = 1.000 with b = c = 11, excess **+0.0pp**, book WR 0.42 vs spy 0.42.
  A row-matched dead heat on n=50.
- **`sector_rotation`** is *not* calibrated-but-beta — it is miscalibrated *and* the worst
  performer, but its McNemar is p = 1.000 (excess −2.8pp). Its problem is the **quote**, not
  the edge: it does not underperform SPY, it underperforms its own advertised number by 25pp.
- **`multileg_directional`** likewise: BH-miscalibrated, but McNemar p = 0.678 and excess
  +4.1pp. Quote problem, not edge problem.

**Edge-before-calibration (C21/C49):** the one genuine *edge* finding in this phase is the
row-matched short-book deficit (**−13.1pp, p = 0.0088, BH-surviving, both tape arms
near-identical**) and its long mirror (**+9.7pp, p = 0.0220, BH-surviving**). Everything else
above is a calibration finding — the fleet's numbers are wrong, but its *selection* is only
demonstrably bad on the short side, where the 2026-08-01 P0 already routes it to watch-only.

**Output:** `phase_3_calibration.jsonl` · `phase_3b_regime.jsonl` · `phase_3c_tape.jsonl` ·
`phase_3c_mcnemar.jsonl` · `phase_3d_excess_artifact.jsonl`.
