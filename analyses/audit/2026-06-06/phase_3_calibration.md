# Phase 3 — Calibration Audit (2026-06-06 · C21 excess · C23 BH/N≥8 · C25 reliability+log-loss)

**Decided:** 432 (WIN+LOSS). **Brier-scored:** 216 (rows with `claimed_win_rate`).
All rates **daily-bar path-aware** (C20). Dataset now spans **two regime states**: the Apr–May
melt-up *plus* the 2026-06-05 risk-off break (SPY −2.0%, VIX 16→21.5). `signal-backtest` not
quoted (C22); the point-in-time benchmark is the SPY same-window same-direction base rate.

## 1. Per-signal-class — claimed vs realised vs benchmark-excess (N ≥ 8, C23)

Sorted by excess. 🚩 = divergence survives Benjamini-Hochberg (FDR 0.10) and |div| > 10pp.

| Signal class | N | Claimed | Realised | **Excess vs SPY** | SPY base | Div (cl−re) | 🚩 |
|---|---|---|---|---|---|---|---|
| hedge | 15 | — | 20.0% | **+33.3pp** ✅ | 0% (short) | — | |
| contrarian_fade | 8 | 60.0% | 12.5% | +14.3pp | 0% | **+47.5** | 🚩 |
| **bearish_flow** | 44 | 38.3% | 38.6% | **+7.5pp** ✅ | 30% | −0.3 | (honest) |
| **dealer_positioning** | 30 | 73.9% | 73.3% | **−3.3pp** | 77% | +0.6 | (honest) |
| earnings_vol | 80 | 72.5% | 43.8% | −11.1pp | 67% | **+28.7** | 🚩 |
| dark_pool_accumulation | 61 | 69.5% | 57.4% | **−14.8pp** | 72% | +12.1 | 🚩 |
| **bullish_flow** | 108 | 63.4% | 49.1% | **−17.9pp** | 67% | +14.3 | 🚩 |
| multileg_directional | 20 | 60.1% | 45.0% | −20.0pp | 65% | +15.1 | |
| vol_surface | 33 | 80.2% | 54.5% | n/a (vol proxy) | — | +25.7 | 🚩 |
| gamma_pin | 20 | 63.9% | 35.0% | n/a (vol proxy) | — | +28.9 | 🚩 |

THIN_N appendix (5–7 decided): `sector_rotation` (n=6) — excluded from headline.

**Run-over-run (vs 2026-05-30):**
- `bearish_flow` excess **collapsed +21.4pp → +7.5pp** — the 06-05 spike lifted the SPY-short
  base rate (14% → 30%) while book shorts barely moved. Short alpha was partly regime timing.
- `dealer_positioning` improved to near-perfect calibration (Δ +0.6pp) and the *least* negative
  excess (−3.3pp) of any long class. Still doesn't beat the tape.
- `earnings_vol` got **worse**: claimed drifted up (60.6 → 72.5%) while realised fell — the
  newest reports quote *higher* earnings win-rates into a class realising 43.8%.
- `contrarian_fade` +47.5pp divergence now survives BH on its own (8 decided, 1 win).

## 2. Per-tier reliability

| Tier | N | Realised WR |
|---|---|---|
| HIGH | 54 | 51.9% |
| MEDIUM | 169 | 49.1% |
| LOW | 131 | 47.3% |

**Monotone for the first time** (05-30 had MEDIUM as the trough; 05-29 had HIGH below LOW) —
but the full ladder spans **4.6pp**, within noise at these N. The ladder no longer *inverts*;
it still doesn't meaningfully *rank*.

## 3. Brier + reliability diagram + log-loss (C25)

**Brier = 0.312** (05-30: 0.316) · **Log-loss = 0.983** (05-30: 1.030; calibrated coin-flip = 0.69).

| Claimed bucket | Predicted | **Realised** | N | Read |
|---|---|---|---|---|
| 0.00–0.40 | 26% | **50%** | 36 | under-confident (shorts/hedges) |
| 0.40–0.50 | 43% | 36% | 22 | mild over |
| 0.50–0.60 | 54% | 41% | 22 | over |
| 0.60–0.70 | 64% | 36% | 14 | over by 28pp |
| 0.70–0.80 | 75% | 60% | 52 | over by 15pp |
| 0.80–0.90 | 83% | 55% | 31 | **over by 28pp** |
| **0.90–1.01** | **96%** | **51%** | **39** | **over by 45pp — ≥0.90 quotes are coin-flips** |

Same shape as 05-30, now on more N: **everything quoted ≥0.60 is overconfident, and the ≥0.90
tail (n=39) realises 51%**. The under-confident 0.00–0.40 bucket (mostly bearish quotes)
realising 50% is the mirror image — the rubric distrusts its shorts and over-trusts its longs,
in exactly the configuration the C21 excess column predicts.

## 4. Conviction-vs-outcome quintiles (raw_score)

| Quintile | Score range | N | Realised WR |
|---|---|---|---|
| Q1 | −2 … 3 | 64 | 53.1% |
| **Q2** | 3 … 5 | 64 | **40.6%** |
| Q3 | 5 … 6 | 64 | 46.9% |
| Q4 | 6 … 7 | 64 | 53.1% |
| **Q5** | **7 … 13** | 67 | **64.2%** |

Q5 (score ≥ 7) keeps its lift (+~14pp over the field; 05-30: 69.6%), but a **new inversion
appeared: Q1 (53.1%) > Q2 (40.6%)** — the score's middle is not just flat, it dips. The
discriminating information still lives only at score ≥ 7.

## 5. C3 — expectancy & fractional-Kelly gate (terminal no-stop, directional)

| Tier | N | WR | Terminal expectancy | Payoff R | Capped ½-Kelly |
|---|---|---|---|---|---|
| HIGH | 49 | 55.1% | **−1.85%** | 0.58 | 0.000 |
| MEDIUM | 125 | 52.0% | **+1.28%** | 1.25 | 0.068 |
| LOW | 94 | 46.8% | −3.28% | 0.67 | 0.000 |

**Kelly gate → `ADVISORY_ONLY`** (n=265 ≥ 30 ✓, but tier expectancy non-monotone:
HIGH −1.85% < MEDIUM +1.28%). Third consecutive audit with **negative HIGH-tier expectancy**
— and it *worsened* (−1.24% → −1.85%, payoff 0.71 → 0.58). The 06-05 drawdown hit the
highest-conviction names hardest. **Do not flip the half-Kelly sizer live.**

## Verdict

### (a) Where the rubric is honest
- **`dealer_positioning`** (73.9 claimed / 73.3 realised, n=30) — the one class that is both
  high-WR and calibrated, for the second audit running. Least-beta long class at −3.3pp.
- **`bearish_flow`** (38.3 / 38.6, n=44) — dead-on calibration, and still the only scaled
  directional class with positive excess (+7.5pp).

### (b) Where it lies to itself
- **The ≥0.90 quote bucket (n=39 → 51%)** remains the fiction, now BH-confirmed across four
  classes (`vol_surface`, `gamma_pin`, `dark_pool_accumulation`, `bullish_flow`) plus
  `earnings_vol` and `contrarian_fade`. The entire Brier excess lives at quotes ≥ 0.60.
- **`earnings_vol` divergence is widening** (+16.0pp → +28.7pp) — the newest envelopes quote
  higher while the class realises lower. This is drift in the wrong direction *after* the
  prior audit flagged it.
- **`contrarian_fade` is 1-for-8 against a 60% claim.** The fade engine's claims have no
  contact with its realised outcomes.

### (c) Tier inversions / High-tier overconfidence
- Tier ladder technically monotone for the first time, but spans 4.6pp — and **HIGH-tier
  expectancy is negative for the third straight audit** with a *deteriorating* payoff (0.58).
  Whatever the rubric is loading into HIGH carries hit-rate but no asymmetry: the +R hits
  cluster small, the failures run far past −R on the terminal read.
- Q1 > Q2 quintile inversion is new — low-score calls (often shorts/hedges, honestly quoted)
  outperform the 3–5 score band.

### (d) ⭐ Calibrated-but-beta
- **Every long-side class still has negative excess** — `dark_pool_accumulation` −14.8pp,
  `bullish_flow` −17.9pp, `multileg_directional` −20.0pp, even honest `dealer_positioning`
  −3.3pp. Confirmed now across a melt-up *and* a risk-off Friday.
- The short side's edge **compressed to +7.5pp** the first time the tape actually broke —
  treat short alpha as regime-conditional, not structural.

## Output
- `phase_3_calibration.jsonl` — per-class numerics incl. excess, BH flags, reliability deciles,
  tier/quintile/expectancy scalars, Kelly gate. `phase3_calibration.py` — reproducible.
