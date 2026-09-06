# Phase 3 — Calibration Audit · 2026-07-04

All tables stratify or era-band by `rubric_version`; the frozen rubric (2026-06-12) has produced only LOW/DROP outcomes, so every HIGH/MEDIUM number below is **pre-freeze era evidence** and is graded as such.

## 1. Per-signal-class table (decided-N ≥ 8; canonical classes; BH FDR 0.10 across the set)

| Class | n | Realised | Claimed | Div (pp) | SPY-bench WR | **Excess (pp)** | p | BH |
|---|---|---|---|---|---|---|---|---|
| bearish_flow | 59 | 0.49 | 0.44 | −5.1 | 0.704 | **−21.2** | 0.508 | — |
| **earnings_vol** | 40 | **0.35** | **0.88** | **+52.7** | 0.667 | **−31.7** | <0.001 | **🚩 Y** |
| dark_pool_accumulation | 36 | 0.42 | 0.55 | +13.8 | 0.371 | +4.5 | 0.136 | — |
| bullish_flow | 34 | 0.50 | 0.58 | +8.5 | 0.303 | **+19.7** | 0.406 | — |
| multileg_directional | 30 | 0.40 | 0.56 | +15.5 | 0.348 | +5.2 | 0.129 | — |
| dealer_positioning | 18 | 0.44 | 0.60 | +15.2 | 0.556 | −11.1 | 0.282 | — |
| **high_iv_rank** | 12 | **0.42** | **0.82** | **+40.7** | — | — | 0.004 | **🚩 Y** |
| sector_rotation | 9 | 0.33 | 0.54 | +20.2 | 0.250 | +8.3 | 0.378 | — |
| **multi_day_sweep** | 8 | **0.88** | 0.38 | **−49.6** | 0.286 | **+58.9** | 0.012 | **🚩 Y** |

Thin-N appendix (5–7, never headline): `gamma_breakout` n=7 realised 0.286.

**Desk commentary (flow-trader voice):**
- `earnings_vol` — *fifth audit, same lie:* quotes 0.88, realises 0.35, and now carries the worst excess on the board (−31.7pp). Anyone sizing vol off this quote is paying 88-cent dollars for 35-cent outcomes. RV-proxy clouds the exact figure, not the direction. The C42 emission cap now clamps these quotes at 0.80 — the cap is working (see Phase 6) but a capped lie is still a lie; the class needs its substrate re-validated, not just capped.
- `high_iv_rank` — same family, 0.82 claimed → 0.42 realised. The three 07-02 quotes hit the 0.80 ceiling from an uncapped 0.9207. All DROP/skip, so no capital burned — the empty-book protocol is what saved the desk here, not the quote.
- `multi_day_sweep` — **first BH-surviving *under*-claim in audit history** (+58.9pp excess). Before anyone celebrates: the 8 decided rows are **4 underlyings** — MRVL×3, SNDK×3 (serial repeat prints of the same setups), AMD, MU — and two of the winners carry `claimed_win_rate = 0.0`, which is an emission bug, not a forecast. Effective independent N ≈ 4. This is a pre-registration (C46, Phase 5), not a promotion. A desk that sizes up on 4 correlated tickers' repeat prints deserves what it gets.
- `bearish_flow` — honest-but-beta inverted: realised 0.49 *beats* its 0.44 claim, but −21.2pp against a 70% SPY-short base. The short book "wins" less often than a coin that just shorts the index. Selection is negative-alpha; unchanged from 06-27.
- `bullish_flow` — the quiet spot: +19.7pp excess (n=34, BH-null). Consistent with the long-edge-in-uptrend story; not statistically separable from tape.

**(d) Calibrated-but-beta:** `bearish_flow` (calibration fine, excess −21.2) and `dealer_positioning` (mild over-claim, excess −11.1). Both ride tape they don't beat — the edge problem leads, per the C21 discipline.

## 2. Per-tier reliability — **tier inversion, 4th consecutive audit**

| Tier | n | Realised WR |
|---|---|---|
| HIGH | 7 | **0.143** |
| MEDIUM | 19 | 0.526 |
| LOW | 72 | 0.444 |
| DROP | 166 | 0.440 |

HIGH < everything, again — and the number is *identical* (0.143) to 06-20/06-27 because **zero new HIGH-tier calls have been emitted post-freeze**. The inversion is a fossil of the pre-freeze era that the freeze already contains. Era × tier: pre-freeze eras all inverted; frozen era emits only LOW (0.455, n=11) / DROP (0.415, n=106).

## 3. Brier / log-loss / reliability deciles (n=146 graded)

**Brier 0.3005** (coin-flip band) · **log-loss 0.8364**. Both marginally worse than 06-27 — the confident tail is still the cause:

| Claimed bucket | n | Pred | Realised |
|---|---|---|---|
| [0.00,0.50) | 50 | 0.36 | 0.50 |
| [0.50,0.55) | 29 | 0.52 | 0.48 |
| [0.55,0.60) | 9 | 0.57 | 0.22 |
| [0.60,0.65) | 9 | 0.62 | 0.22 |
| [0.65,0.70) | 7 | 0.66 | 0.57 |
| [0.70,0.80) | 8 | 0.77 | 0.75 |
| **[0.80,0.90)** | **28** | **0.83** | **0.43** |
| [0.90,1.01) | 6 | 0.93 | 0.50 |

The miscalibration still lives ≥0.80 (all legacy-substrate vol/flow quotes, pre-cap). New wrinkle at the *bottom*: the [0,0.50) bucket under-claims (0.36 → 0.50) — partly the `claimed_win_rate=0.0` emission bug (two multi_day_sweep winners quoted 0.0), partly DROP-tier paper trades doing better than their pessimistic quotes. The rubric now lies in both directions at the extremes.

## 4. Conviction-vs-outcome (raw score → WR)

`5: 0.62(n8) · 6: 0.42(n12) · 7: 0.67(n6) · 8: 0.29(n7) · 9: 0.67(n6) · 10: 0.00(n3) · 11: 0.33(n3) · 12: 0.00(n1)` — non-monotone above 7, all pre-freeze, all single-digit N. The score ladder still has no positive slope where it matters.

## 5. Expectancy + Kelly live-activation gate

**Gate: ADVISORY_ONLY** — n=25 closed sized calls < 30 floor. Tier expectancy is *monotone for the first time* (HIGH −1.97 ≥ MED −2.24 ≥ LOW −2.77 on sized-closed) but every tier is **negative**, so monotonicity here is three flavors of losing. Paper-book expectancy: HIGH −2.44 / MED +0.10 / LOW +0.29 / DROP −4.61; payoff ratios sub-1.0 except LOW (1.33). **Do not flip the sizer to Kelly.** Win-rate ladder stays live.

## Verdict

- **(a) Honest:** `bearish_flow` calibration (claims low, realises low); the sub-0.55 quote band; the empty-book refusal to size (the frozen rubric quoting nothing ≥ MEDIUM *is* calibration working).
- **(b) Lies to itself:** `earnings_vol` + `high_iv_rank` (5th consecutive, both BH-surviving, both also negative-excess — edge problem first); the 0.0-claim emission bug (lying pessimistically).
- **(c) Tier inversions:** HIGH 0.143 fossil persists; nothing new post-freeze to re-grade it — C41 stays uncleared.
- **(d) Calibrated-but-beta:** `bearish_flow`, `dealer_positioning`. The whole short book remains the desk's structural negative-alpha pocket.

Machine-readable: `phase_3_calibration.jsonl`, `phase_3b_regime.jsonl` (regime strata, half-cap grading, freeze-lift inputs).
