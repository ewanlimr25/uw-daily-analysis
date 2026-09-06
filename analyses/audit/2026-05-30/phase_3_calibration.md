# Phase 3 — Calibration Audit (2026-05-30 · C21 excess · C23 BH/N≥8 · C25 reliability+log-loss)

**Decided:** 365 (WIN+LOSS). **Brier-scored:** 166 (rows with `claimed_win_rate`).
All rates are **daily-bar path-aware** (Phase 2 C20) and **single-regime (UPTREND, Apr–May 2026)**.
`signal-backtest` is **not** quoted as a benchmark (C22) — the honest point-in-time benchmark is
the **SPY same-window same-direction base rate** below.

## 1. Per-signal-class — claimed vs realised vs **benchmark-excess** (N ≥ 8, C23)

Sorted by **excess** (the column that separates edge from beta). 🚩 = divergence survives
Benjamini-Hochberg (FDR 0.10) across the class set **and** |div| > 10pp.

| Signal class | N | Claimed | Realised | **Excess vs SPY** | SPY base | Div (cl−re) | 🚩 |
|---|---|---|---|---|---|---|---|
| hedge | 8 | — | 37.5% | **+33.3pp** | (short) | — | |
| **bearish_flow** | 32 | 38.3% | 34.4% | **+21.4pp** ✅ | 14% | +3.9 | |
| contrarian_fade | 8 | 60.0% | 12.5% | +14.3pp | 0% | +47.5 | 🚩 (thin, n=8) |
| **dealer_positioning** | 28 | 78.2% | **71.4%** | **−7.1pp** | 79% | +6.8 | (honest) |
| earnings_vol | 74 | 60.6% | 44.6% | −11.1pp | 67% | +16.0 | 🚩 |
| multileg_directional | 18 | 63.8% | 50.0% | −16.7pp | 67% | +13.8 | |
| **bullish_flow** | 87 | 63.4% | 51.7% | **−20.0pp** | 72% | +11.6 | 🚩 |
| **dark_pool_accumulation** | 49 | 76.2% | 63.3% | **−20.8pp** | 85% | +13.0 | 🚩 |
| vol_surface | 32 | 80.2% | 53.1% | n/a (vol) | — | +27.1 | 🚩 |
| gamma_pin | 20 | 63.9% | 35.0% | n/a (vol) | — | +28.9 | 🚩 |

*No THIN_N (5–7) classes this run — every canonical class cleared N≥8.*

## 2. Per-tier reliability

| Tier | N | Realised WR |
|---|---|---|
| HIGH | 49 | 55.1% |
| MEDIUM | 147 | **49.0%** |
| LOW | 97 | 51.5% |

**Monotone? NO** — MEDIUM (49.0%) is the trough, below LOW (51.5%). HIGH now sits *above* LOW
(55.1% > 51.5%; the 05-29 run had HIGH **below** LOW), so the inversion **softened** under
path-aware resolution but the ladder still does not cleanly rank.

## 3. Brier + reliability diagram + log-loss (C25)

**Brier = 0.316** (05-29: 0.34) · **Log-loss = 1.030** (a calibrated coin-flip = 0.69; 1.03
means confident-and-wrong is being punished hard). The scalar Brier hides *where* the lie is —
the reliability diagram localizes it precisely:

| Claimed bucket | Predicted | **Realised** | N | Read |
|---|---|---|---|---|
| 0.00–0.40 | 25% | **52%** | 31 | under-confident (shorts/hedges win more than quoted) |
| 0.40–0.50 | 43% | 43% | 14 | calibrated |
| 0.50–0.60 | 56% | 50% | 8 | ~ok |
| 0.60–0.70 | 64% | 44% | 9 | over |
| 0.70–0.80 | 74% | 56% | 45 | over |
| 0.80–0.90 | 82% | **62%** | 21 | **over by 20pp** |
| **0.90–1.01** | **96%** | **53%** | **38** | **over by 43pp — the ≥0.90 quotes are coin-flips** |

**This is the single clearest picture in the audit.** The rubric is *under-confident on shorts*
(0.00–0.40 bucket realises 52% vs 25% quoted) and *grossly over-confident on its high quotes*
(the 38 calls quoted ≥0.90 realise 53%). Every point of the Brier excess lives in the ≥0.80
tail — capping those quotes is the highest-leverage Brier fix and it is now pinned to a decile,
not asserted.

## 4. Conviction-vs-outcome quintiles (raw_score)

| Quintile | Score range | N | Realised WR |
|---|---|---|---|
| Q1 | −2 … 3 | 52 | 50.0% |
| Q2 | 3 … 4 | 52 | 51.9% |
| Q3 | 4 … 5 | 52 | 48.1% |
| Q4 | 5 … 7 | 52 | 51.9% |
| **Q5** | **7 … 13** | 56 | **69.6%** |

**New vs 05-29.** The close-only run found the score→WR slope "nearly flat" (Q5 53.5%). Under
path-aware resolution **the top quintile (score ≥ 7) realises 69.6%** — a genuine +18pp lift
over the Q1–Q4 plateau (~50%). The raw score **does** carry discriminating information, but only
at the top — the middle of the scale (Q1–Q4) is noise. This argues for *raising* the HIGH cut to
capture the score-≥7 cohort, not flattening the rubric.

## 5. C3 — expectancy table & fractional-Kelly gate (terminal no-stop move, directional)

| Tier | N | WR | Terminal expectancy/trade | Payoff R | Capped ½-Kelly |
|---|---|---|---|---|---|
| HIGH | 44 | 59.1% | **−1.24%** | 0.71 | 0.008 |
| MEDIUM | 107 | 53.3% | **+3.18%** | 1.47 | 0.108 |
| LOW | 65 | 50.8% | −0.97% | 0.80 | 0.000 |

> Note on payoff: the path-aware walk exits at ±R, so its bracketed payoff is ~1.0 by construction.
> The table above uses **terminal (no-stop, window-end) returns** to recover the real asymmetry —
> the same lens as 05-29, so the comparison holds.

**Kelly live-activation gate → `ADVISORY_ONLY`** (n=214 ≥ 30, but tier expectancy
**non-monotone**: HIGH −1.24% < MEDIUM +3.18%). **Do not flip the half-Kelly sizer live.** This
finding is **identical to 05-29** and robust to the method change: the MEDIUM tier carries the
book's asymmetry (payoff 1.47); the HIGH tier has **negative** expectancy. Conviction is still
inversely related to realised payoff.

## Verdict

### (a) Where the rubric is honest
- **`dealer_positioning` (78% claimed / 71% realised, n=28)** — the one well-calibrated,
  high-WR class. *DEX-flip / vanna / charm still trades closest to its backtest.* Even so its
  benchmark-excess is **−7pp** — it's the *least-beta* long class, not a tape-beater.
- **`bearish_flow` (38% claimed / 34% realised)** — honestly low-claimed; the desk distrusts its
  own shorts and that humility is the calibration win. The 0.00–0.40 reliability bucket confirms
  it's actually *under*-confident.

### (b) Where it lies to itself
- **The ≥0.90 quote bucket is the fiction (n=38, realises 53%).** `vol_surface` (80→53),
  `gamma_pin` (64→35), `dark_pool_accumulation` (76→63), `bullish_flow` (63→52) all survive BH.
  Capping the ≥0.80 quotes to realised collapses most of the 0.316 Brier and the 1.03 log-loss.
- **`gamma_pin` / `vol_surface`** remain over-claimed, but their realised rates here are partly
  an **RV-proxy artifact** (Phase 2) — discount the magnitude, not the sign.

### (c) Tier inversions / High-tier overconfidence
- Tier ladder still **non-monotone** (MED 49% trough). **HIGH-tier directional expectancy negative
  (−1.24%)** — unchanged from 05-29. The fix is in the *weights feeding HIGH*, not just the cuts:
  Q5 (score ≥7) realises 69.6%, so the discrimination exists but the tier mapping isn't capturing it.

### (d) ⭐ Calibrated-but-beta — the C21 read the 05-29 run was blind to
- **Every long-side class has negative benchmark-excess.** `dark_pool_accumulation` looks *better*
  on calibration than 05-29 implied (63% realised, not 51%) — but it is **−20.8pp vs simply buying
  SPY**. `bullish_flow` −20.0pp. `multileg_directional` −16.7pp. Even honest `dealer_positioning`
  is −7.1pp. **The entire long book rode the tape and lagged it.** A desk that "calibrated" these
  quotes to realised would still be sizing **negative-edge beta**.
- **The alpha is on the short side.** `bearish_flow` **+21.4pp excess** (and hedges +33pp). The
  book's *short selection* beats the index-short base rate by a wide margin; its *long selection*
  destroys value vs the index. **Lead the desk read with edge, not calibration: fix the longs
  (they're beta) before re-quoting the win-rates (they're merely dishonest).**

## Output
- `phase_3_calibration.jsonl` — per-class numerics incl. `excess`, `spy_wr`, BH flags, reliability
  deciles, tier/quintile/expectancy scalars, Kelly gate. `phase3_calibration_v2.py` — reproducible.
