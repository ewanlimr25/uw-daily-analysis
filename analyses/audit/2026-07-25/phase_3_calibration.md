# Phase 3 — Calibration Audit (2026-07-25)

Provenance: **verbatim** (52/52 envelopes). Decided N = 440. Headline floor decided-N ≥ 8 (C23);
Benjamini-Hochberg FDR 0.10 across the class set.

---

## 3.1 Per-signal-class table

| class | n | realised | claimed | div (pp) | SPY base | excess | p | BH |
|---|---|---|---|---|---|---|---|---|
| bearish_flow | 94 | 0.49 | 0.48 | −0.8 | 0.598 | **−10.8** | 0.960 | n |
| earnings_vol | 78 | 0.44 | 0.88 | **+44.1** | 0.667 | −23.1 | 0.000 | **Y** |
| multileg_directional | 58 | 0.40 | 0.56 | **+15.8** | 0.302 | +9.5 | 0.022 | **Y** |
| bullish_flow | 50 | 0.42 | 0.54 | +12.3 | 0.280 | +14.0 | 0.108 | n |
| dark_pool_accumulation | 46 | 0.41 | 0.55 | +14.1 | 0.378 | +3.5 | 0.076 | n |
| sector_rotation | 25 | 0.24 | 0.54 | **+29.6** | 0.167 | +7.3 | 0.005 | **Y** |
| high_iv_rank | 24 | 0.50 | 0.82 | **+32.1** | — | — | 0.001 | **Y** |
| dealer_positioning | 23 | 0.48 | 0.60 | +11.8 | 0.478 | 0.0 | 0.344 | n |
| multi_day_sweep | 9 | 0.67 | 0.38 | −28.7 | 0.250 | +41.7 | 0.156 | n |
| opex_pin | 9 | 0.11 | — | — | — | — | 1.000 | n |
| oi_build | 9 | 0.33 | — | — | 0.333 | 0.0 | 1.000 | n |

THIN_N appendix (5–7, never headline): `gamma_breakout` n=7, WR 0.286.

**Four classes are BH-significantly miscalibrated, and they are the same four as the
last three audits**: `earnings_vol` (claims 0.88, realises 0.44), `high_iv_rank`
(0.82 → 0.50), `sector_rotation` (0.54 → 0.24), `multileg_directional` (0.56 → 0.40).
These are stable, replicated lies. They are also — critically — the *vol* and
*rotation* lanes, where the quoted win rate comes from `NA(substrate)` or
`fallback_proxy` sources rather than `backtest_clean`.

---

## 3.2 Per-tier reliability — **inversion, 4th consecutive audit**

| tier | n | WR |
|---|---|---|
| HIGH | 7 | **0.143** |
| MEDIUM | 19 | 0.526 |
| LOW | 87 | 0.402 |
| DROP | 327 | **0.431** |

`HIGH > MEDIUM > LOW` **fails**. HIGH is the worst tier in the book, and **DROP beats
LOW** — the names the system refused outperformed the names it graded tradeable.

By era (inversion is not an artifact of one rubric generation):

| era | HIGH | MEDIUM | LOW | DROP |
|---|---|---|---|---|
| era_0525_0529 | 0.25 (4) | 0.556 (9) | 0.579 (19) | 0.571 (21) |
| era_0530_0605 | 0.00 (2) | 0.500 (10) | 0.400 (25) | 0.419 (31) |
| pre_freeze_post_0606 | 0.00 (1) | — (0) | 0.353 (17) | 0.500 (8) |
| **2026-06-12 (frozen)** | **— (0)** | **— (0)** | **0.308 (26)** | **0.419 (267)** |

All 7 HIGH calls are pre-freeze. The frozen rubric has produced none.

---

## 3.3 Brier, log-loss, reliability diagram

**Brier = 0.2899** · **log-loss = 0.8055** · graded n = 192.

Brier ≥ 0.25 is the skill's own "no better than coin-flip" line. The rubric is over it.

| claimed bucket | n | predicted | realised |
|---|---|---|---|
| [0.00,0.50) | 63 | 0.38 | 0.44 |
| [0.50,0.55) | 50 | 0.52 | 0.54 |
| **[0.55,0.60)** | **19** | **0.56** | **0.16** |
| **[0.60,0.65)** | **9** | **0.62** | **0.22** |
| [0.65,0.70) | 7 | 0.66 | 0.57 |
| [0.70,0.80) | 8 | 0.77 | 0.75 |
| **[0.80,0.90)** | **30** | **0.83** | **0.43** |
| [0.90,1.01) | 6 | 0.93 | 0.50 |

The diagram localizes the damage precisely, and it is **not** a smooth overconfidence
slope — it is bimodal. The rubric is *honest* below 0.55 and in the 0.65–0.80 band. It
is catastrophically wrong in **[0.55,0.65)** (n=28, predicted ~0.58, realised ~0.18) and
in **[0.80,0.90)** (n=30, predicted 0.83, realised 0.43). A quote in the 0.55–0.65
band is currently *anti-predictive* — those names did worse than the ones the system
was unsure about.

---

## 3.3b Post-freeze isolate — **the cap works; the mid-band does not**

The class table above pools eras. Isolating the 92 post-freeze rows that carry a quote
changes the verdict materially:

| | all eras | **post-freeze only** |
|---|---|---|
| Brier | 0.2899 | **0.2681** |
| log-loss | 0.8055 | **0.7329** |
| n | 192 | 80 |
| max quote emitted | 0.93 | **0.80 (exactly)** |

**All 23 quotes above 0.80 in the dataset are pre-freeze.** The 2026-06-06 P0.1
emission cap (0.69 for `win_rate_n` < 10, 0.80 absolute ceiling) is **binding perfectly**:
zero post-freeze violations, zero small-n violations across 206 quoted rows. The
`earnings_vol` 0.88 and `high_iv_rank` 0.82 headline claims are **legacy artifacts of
the pre-cap era, not live defects** — a correction to how the last three audits have
narrated this class.

What *is* live:

| post-freeze class | n | claim | realised | divergence |
|---|---|---|---|---|
| bearish_flow | 61 | 0.519 | 0.491 | **+2.9pp** ✅ |
| bullish_flow | 21 | 0.499 | 0.250 | **+24.9pp** ⚠ |
| high_iv_rank | 8 | 0.800 | 0.500 | +30.0pp *(at the ceiling, still too high)* |

And the inverted mid-band is **worse** under the frozen rubric, not better:

| [0.55,0.65) band | n | realised |
|---|---|---|
| pre-freeze | 13 | 0.231 |
| **post-freeze** | **15** | **0.133** |

0.55 is the single most common post-freeze quote (14 rows). The rubric's modal
confidence statement is currently its least reliable one. This is the live calibration
defect — not the pre-cap 0.88s.

---

## 3.4 Conviction-vs-outcome by raw score

`-3: 0.40(15) · -2: 0.67(9) · -1: 0.34(35) · 0: 0.45(94) · 1: 0.45(115) · 2: 0.39(59) ·
3: 0.40(35) · 4: 0.35(31) · 5: 0.56(9) · 6: 0.42(12) · 7: 0.67(6) · 8: 0.29(7) ·
9: 0.67(6) · 10: 0.00(3) · 11: 0.33(3) · 12: 0.00(1)`

No slope. Score 0 and score 4 are indistinguishable; scores 10–12 are 0-for-4.

---

## 3.5 Expectancy + fractional-Kelly live-activation gate

**Gate status: `ADVISORY_ONLY`.** n = 26 closed sized calls (< 30 required). Tier ×
expectancy *is* now monotone (HIGH −1.97 ≥ MED −2.24 ≥ LOW −2.40) — but monotone in
the sense that all three tiers are **negative**, ordered least-bad to worst. The
half-Kelly sizer stays off; the win-rate ladder remains live. **Do not flip
`signal-confluence-quant` / `risk-monitor` to Kelly.**

| tier | mean P&L | payoff ratio | half-Kelly | n |
|---|---|---|---|---|
| HIGH | −2.441 | 0.720 | 0.0 | 7 |
| MEDIUM | +0.104 | 0.948 | 0.0132 | 19 |
| LOW | −0.874 | 1.170 | 0.0 | 87 |
| DROP | −2.190 | 0.871 | 0.0 | 327 |

---

## Verdict

### (a) Where the rubric is honest
Below 0.55 and in the 0.65–0.80 band the reliability diagram is close to the diagonal.
`bearish_flow` is the single best-calibrated large class in the book (claims 0.48,
realises 0.49, n=94, p=0.96) — a genuinely honest quote. The Σ-points audit trail is
perfect (0/434 violations). The system's *arithmetic* is not the problem.

### (b) Where it lies to itself
The pooled table says `earnings_vol` claims 0.88 and realises 0.44 (n=78, BH-surviving)
and `high_iv_rank` claims 0.82 / realises 0.50. **Both are pre-cap legacy** (§3.3b) — the
P0.1 emission ceiling has held at exactly 0.80 for every post-freeze quote, and prior
audits mis-narrated this as a live defect.

The genuine live lie is the **[0.55,0.65) band, which is inverted and getting worse**:
15 post-freeze rows quoting ~0.58 realised **0.133**. Since 0.55 is the modal
post-freeze quote, the rubric's most-used confidence statement is anti-predictive.
Post-freeze `bullish_flow` (claims 0.499, realises 0.250 on n=20) is the class driving it.

### (c) Tier inversions
Fourth consecutive audit with `HIGH < LOW`. HIGH is 0.143 on n=7, and **DROP (0.431)
beats LOW (0.402)** overall and by a wider margin post-freeze (0.419 vs 0.308). The
conviction ladder does not order outcomes at any cut.

### (d) "Calibrated-but-beta" — **and the deeper problem**
`bearish_flow` is the cleanest case of calibrated-but-negative-excess: claimed ≈
realised ≈ 0.49, benchmark-excess **−10.8pp**. On the raw table it is honest and
worthless.

**But this audit's central finding is that the excess column itself cannot bear the
weight three audits have put on it.** See `phase_3d_excess_artifact.md`: **71% of the
variance in benchmark-excess across strata is the SPY base rate moving, not the book.**
The regression of excess on the SPY base rate has slope **−80pp per unit** (pure
artifact = −100), R² = 0.64, and implied **β(book WR | SPY WR) = +0.20**. Book win rates
are pinned near 0.42 while the benchmark swings 0.00 → 0.80.

The concrete demonstration: `bearish_flow` books **0.533 on up-tape and 0.526 on
down-tape** — a 0.7pp difference — while its excess moves **15.6pp**. `dark_pool_accumulation`
books **0.400 in both tapes** while its excess moves **23.3pp**.

The "non-stationary edge sign" that headlined 2026-07-11 (+29.4pp), 2026-07-18 (−3.2pp)
and appears here (−10.8pp) is, for three of four classes tested, **the benchmark moving
under a stationary book**. Lead the desk with that, not with the sign of the month.

Outputs: `phase_3_calibration.jsonl`, `phase_3b_regime.jsonl`, `phase_3c_tape.jsonl`,
`phase_3d_excess_artifact.jsonl`.
