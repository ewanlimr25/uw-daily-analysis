# Phase 3 — Calibration Audit

**Decided sample:** 328 (WIN+LOSS). **Brier-scored sample:** 142 (rows with a `claimed_win_rate`). All win-rates close-to-close, path-aware (see Phase 2 method/limitation).

## 1. Per-signal-class — claimed vs realised (N ≥ 5)

| Signal class | N | Claimed WR | Realised WR | Divergence | Flag |
|---|---|---|---|---|---|
| dark_pool_accumulation | 43 | 82.8% | **51.2%** | **−31.6pp** | 🚩 |
| vol_surface | 34 | 80.2% | **47.1%** | **−33.2pp** | 🚩 |
| gamma_pin | 20 | 63.9% (n=2) | **30.0%** | **−33.9pp** | 🚩 (thin claim) |
| contrarian_fade | 5 | 80.0% (n=1) | 40.0% | −40.0pp | 🚩 (thin claim) |
| bullish_flow | 67 | 64.5% | **46.3%** | **−18.3pp** | 🚩 |
| earnings_vol | 72 | 57.6% | 43.1% | −14.6pp | 🚩 |
| multileg_directional | 16 | 67.2% | 56.2% | −10.9pp | 🚩 |
| **dealer_positioning** | 20 | 84.4% | **80.0%** | −4.4pp | ✅ honest |
| **bearish_flow** | 25 | 42.5% | 44.0% | +1.5pp | ✅ honest |
| hedge | 16 | — | 37.5% | — | (no claim) |
| sector_rotation | 5 | — | 60.0% | — | (no claim) |

## 2. Per-tier reliability diagram

| Tier | N | Realised WR |
|---|---|---|
| HIGH | 41 | 53.7% |
| MEDIUM | 124 | **46.0%** |
| LOW | 86 | **55.8%** |

**Monotone? NO.** Inversion: **MEDIUM ≤ LOW** (46.0% < 55.8%), and HIGH (53.7%) sits *below* LOW. The conviction tier does not rank outcomes — a desk-quitting signal. The rubric's ordering is noise.

## 3. Brier score

**Brier = 0.34** (n=142). The ≥0.25 line is "no better than a coin-flip"; ≤0.10 is "professionally calibrated." At **0.34 the rubric is *anti*-calibrated** — its stated confidences are systematically worse than quoting a flat base rate, because the high claimed win-rates (80–85% on dark-pool/vol-surface/dealer) collide with ~50% realised outcomes.

## 4. Conviction-vs-outcome quintiles (raw_score)

| Quintile | Score range | N | Realised WR |
|---|---|---|---|
| Q1 | −1 … 3 | 43 | 48.8% |
| Q2 | 3 … 4 | 43 | 53.5% |
| Q3 | 4 … 5 | 43 | **46.5%** |
| Q4 | 5 … 7 | 43 | 53.5% |
| Q5 | 7 … 13 | 43 | 53.5% |

The slope from Q1→Q5 is **+4.7pp, non-monotone** (Q3 dips below Q1). The raw score carries almost **no** discriminating information about direction outcomes — confirming and extending the 05-23 finding that the score→WR slope is "nearly flat at 58–64%." On the larger sample it is flatter still and centered lower (~50%).

## 5. C3 — expectancy table & fractional-Kelly gate (directional signed, n=188)

| Tier | N | Realised WR | Expectancy/trade | Payoff R | Capped ½-Kelly |
|---|---|---|---|---|---|
| HIGH | 36 | 55.6% | **−1.52%** | **0.06** | 0.000 |
| MEDIUM | 79 | 48.1% | **+1.93%** | 6.12 | 0.198 |
| LOW | 54 | 55.6% | +0.19% | 0.90 | 0.032 |

**Kelly live-activation gate → `ADVISORY_ONLY`.** n=169 clears the 30-closed floor, but tier expectancy is **non-monotone** (HIGH −1.52% < MEDIUM +1.93% < … not ordered). The half-Kelly sizer **must not** go live; the win-rate ladder stays the live sizer — *but note that ladder is itself broken* (§2 tier inversion).

The HIGH-tier number is the alarm: **HIGH-conviction directional calls have negative expectancy and a 0.06 payoff ratio** — they win small and lose big. The book's positive aggregate expectancy (+0.50%/trade, Phase 2) is carried entirely by the **MEDIUM** tier (payoff 6.1). Conviction is inversely related to realised payoff here.

## Verdict

### (a) Where the rubric is honest
- **`dealer_positioning` (84% claimed / 80% realised, n=20)** is the one class that does what it says — and it's the highest realised win-rate in the book. *"DEX-flip / vanna / charm calls are the only flow signal that trades like the backtest promises."*
- **`bearish_flow` (42.5% / 44.0%)** is honestly *low*-claimed and delivers — the desk correctly distrusts its own shorts, and that humility is the calibration win. The truth-set backtest agrees (41.9%).

### (b) Where it lies to itself
- **`dark_pool_accumulation` is the flagship fiction: 82.8% claimed → 51.2% realised (−31.6pp, n=43).** *"Every desk that bought the '100% dark-pool win-rate' headline is sizing a coin-flip at full conviction. This is the single most dangerous number in the rubric."* The truth-set tool can't even compute a rate for it (N=0) — the 80%+ figure has no backtest spine.
- **`vol_surface` (80%→47%) and `gamma_pin` (64%→30%)** are the same disease: KINKED/calendar and pin trades quoted at high confidence, realising coin-flip-or-worse. The vol_short/pin bleed from Phase 2 (30.9% WR) lives here.
- **`bullish_flow` (64.5%→46.3%)** — *"sweep-chasers who think every ask-side print is a confirmed signal cap at ~46%; the truth-set says 76–83% but that's a forward-snapshot on survivors, not these entries."*

### (c) Tier inversions / High-tier overconfidence
- The tier ladder is **inverted** (MED < LOW, HIGH < LOW) and **Brier 0.34** confirms the confidences are anti-calibrated.
- **HIGH-tier directional expectancy is negative (−1.52%).** The most dangerous structural flaw in the schema: the rubric's top conviction bucket is its worst-paying. This is what Phase 5 must fix — either the weights feeding HIGH or the tier cuts themselves.

## Output
- `phase_3_calibration.jsonl` — all numerics. `phase3_calibration.py` — reproducible.
