# Phase 3 — Calibration Audit (2026-07-18)

## Per-class realised WR + benchmark-excess (C21) — decided-N ≥ 8, BH FDR 0.10
BH here tests **claimed-vs-realised divergence** (calibration). `excess` = realised − SPY same-window same-direction (edge).

| Class | N | Real WR | Claim | Div (pp) | SPY-base | **Excess** | p | BH |
|---|---|---|---|---|---|---|---|---|
| bearish_flow | 81 | 0.56 | 0.47 | −8.9 | 0.588 | **−3.2** | 0.136 | n |
| earnings_vol | 64 | 0.38 | 0.88 | **+50.2** | (vol) | −29.2 | 0.000 | **Y** |
| multileg_directional | 51 | 0.41 | 0.56 | +14.3 | 0.304 | **+10.7** | 0.057 | n |
| bullish_flow | 48 | 0.42 | 0.55 | +13.0 | 0.295 | **+12.1** | 0.097 | n |
| dark_pool_accumulation | 44 | 0.39 | 0.55 | +16.8 | 0.386 | **0.0** | 0.037 | **Y** |
| high_iv_rank | 22 | 0.46 | 0.82 | +36.6 | (vol) | — | 0.000 | **Y** |
| dealer_positioning | 21 | 0.52 | 0.60 | +7.3 | 0.550 | −2.6 | 0.639 | n |
| sector_rotation | 21 | 0.24 | 0.54 | +29.8 | 0.158 | +8.0 | 0.011 | **Y** |
| multi_day_sweep | 9 | 0.67 | 0.38 | −28.7 | 0.250 | +41.7 | 0.156 | n |
| opex_pin | 9 | 0.11 | — | — | — | — | — | n |
| oi_build | 9 | 0.33 | — | — | 0.333 | 0.0 | — | n |

*THIN_N appendix (5–7): gamma_breakout (7, 0.286).*

### (a) Where the rubric is honest
The frozen era quotes **no numeric win-rate** (`NA(substrate)`), so it cannot lie about calibration — that is the correct posture, not a gap. The four BH-surviving calibration divergences (earnings_vol +50pp, high_iv_rank +37pp, sector_rotation +30pp, dark_pool_accumulation +17pp) are **all pre-quarantine / pre-freeze `win_rate` quotes**. The vol pair resolves on RV-proxy in an RV-*expanding* tape, which mechanically deflates realised vs the old backtest quote.

### (b) Where it lies to itself
`dark_pool_accumulation` still claims 0.55 and realises 0.39 (+16.8pp div, p=0.037, BH-SURVIVES) — the accumulation lane remains **badly calibrated**. But its **excess washed from −29.2pp (07-11) to 0.0pp** — as the up-tape flattened, the beta it was riding disappeared and it landed exactly on the SPY base. This is the C48 mechanism confirming itself: *accumulation ≈ beta; kill the beta and the "edge" is neither positive nor negative, just gone.*

### (c) Tier inversion / High-tier overconfidence
Pooled: HIGH **0.143** (n7) < MEDIUM 0.526 (n19) < LOW 0.407 (n86) ≈ DROP 0.433 (n282). Inversion persists, but **every HIGH and MEDIUM call is pre-freeze** — the frozen era's only tiers are LOW (0.32, n25) and DROP (0.419, n222). The inversion is the pre-freeze index/semis-short artifact the freeze already halted. Do not re-bin.

### (d) CALIBRATED-BUT-BETA & the non-stationarity read (desk-critical)
- **The excess sign is NOT stationary.** long +10.8pp / short −7.2pp this window vs **the exact opposite at 07-11**. In the two large regime buckets: uptrend long **+20.0pp** / short −26.7pp; pullback long +5.9pp / short −22.7pp. In the small choppy/transitional buckets the sign flips again (transitional short +52.4pp, n21). **No directional excess claim survives across audit windows** — it is dominated by window regime-composition and by the 0.5-ATR path threshold, which for shorts touches the tight lower barrier first ~56% of the time regardless of trend.
- **This REFUTES the 07-11 "bearish edge is accruing" narrative.** `bearish_flow` went +29.4pp (BH-survives, 07-11) → **−3.2pp ns (07-18)**. The one class the prior audit called "real, significant edge" evaporated in one window. C19 must not graduate (Phase 5/7).

## Brier / log-loss / reliability
**Brier 0.2894, log-loss 0.8071 (n=178 graded)** — still >0.25 (coin-flip band). Reliability deciles localize the damage in the confident tail:

| claimed bucket | n | pred | realised |
|---|---|---|---|
| [0.50,0.55) | 46 | 0.52 | 0.59 |
| [0.80,0.90) | **30** | 0.83 | **0.43** |
| [0.90,1.01) | 6 | 0.93 | 0.50 |

The ≥0.80 quotes (vol-lane substrate) realise 0.43 — the same overconfident tail every prior audit flagged, now on more n. Post-freeze: no numeric quote → not computable (correct).

## raw_score → WR (all eras pooled; frozen era is a near-single point at raw=3)
Non-monotone and noisy: raw=10 → 0.00 (n3), 11 → 0.33 (n3), 12 → 0.00 (n1) — the high scores (all pre-freeze) lose. Frozen-era raw=3 → 0.41 (n34). No ladder.

## Kelly gate & half-cap
- **Kelly gate: ADVISORY_ONLY** (n=26 closed < 30). Win-rate ladder stays the live sizer. Do not flip quant/risk-monitor to Kelly.
- **P0.6 OUT-OF-REGIME half-cap is now ACTIONABLE (n=34 ≥ 10) and PROTECTIVE:** out-of-regime names realise 0.324 / **−14.3pp excess** vs in-regime 0.436 / +5.4pp. First cycle the half-cap crossed the n≥10 floor with a decisive protective signal. See Phase 3b.

Outputs: `phase_3_calibration.jsonl`, `phase_3b_regime.jsonl`.
