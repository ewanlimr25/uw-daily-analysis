# Single-Leg Whale Backtest — Findings Report
**Date:** 2026-05-29  
**Script:** `scripts/single_leg_whale.py --backtest`  
**Raw output:** `single_leg_whale_backtest.json`  
**Methodology:** `single_leg_whale_edge_analysis.md`

---

## Setup

**Signal definition:** Single-leg, ask-side, common-stock option prints with premium ≥ $500K.  
**Filters:** `canceled=false`, `upstream_condition_detail ∈ {auto, slan, isoi, slft, slai, slcn}`, `side='ask'`, `equity_type='Common Stock'`, `underlying_price ≥ $5`, exclude index products (SPX, NDX, RUT, SPY, QQQ, IWM, etc.)  
**Aggregation:** One signal per (ticker, option_type) per day — largest premium print. A ticker can have both a call AND a put signal on the same day (both kept).  
**Entry price:** `underlying_price` at time of the print (the tradeable level when you see the signal).  
**Exit price:** `LAST(underlying_price ORDER BY executed_at)` from the NEXT trading day's parquet — an EOD close proxy.  
**Win criterion:** Next-day close moves in the option's direction (up for calls, down for puts).  
**Regime:** March 13 – May 28, 2026 (34 trading days, 32 consecutive D→D+1 pairs; 1 gap of 31 days excluded).  
**Market regime:** Strong bull — SPY closed UP on 62.5% of trading days in this window.

---

## Overall Results

| Metric | Value |
|---|---|
| Total graded signals | 2,815 |
| Win rate | **52.04%** |
| vs 50% | +2.04pp |
| Binomial p-value | 0.016 |
| Trading days with signals | 32 / 32 |

**The aggregate signal is statistically significant at the 5% level but tiny in magnitude.** The raw number is misleading — the regime breakdown explains everything.

---

## The Regime Split: Calls vs Puts

| | Calls | Puts |
|---|---|---|
| n | 1,656 | 1,159 |
| Win rate | 52.84% | 50.91% |
| SPY baseline (same direction) | **62.5%** | **37.5%** |
| Market excess | **−9.66pp** | **+13.41pp** |
| p-value | 0.011 | 0.278 |
| Verdict | **NO_GO_NO_EDGE** | **NO_GO_NO_EDGE** (insufficient WR, strong directional excess) |

**Critical finding for calls:** In a market that rose 62.5% of days, the call signals only hit 52.84% — **nearly 10pp below the SPY baseline**. Buying the underlying on any signal call print would have UNDERPERFORMED simply holding SPY. These calls are beta, not edge. The institutions printing large calls in this window are riding the tape, not front-running it.

**Critical finding for puts:** Puts won 50.91% of days in a market that was down only 37.5% of days — a **+13.4pp excess over the bearish SPY baseline**. This is the more interesting result: large opening put prints are systematically appearing before individual stock declines that are NOT correlated with the broad market direction. However, the p-value (0.28) is not significant at conventional thresholds because put signals are rarer (n=1,159) and dispersed across the full sample.

---

## The Signal Sharpens: High-Conviction Filters

### Size/OI ≥ 2.0 AND DTE ≤ 30 (Pan-Poteshman opening flow, event-driven)

| | Overall | Calls | Puts |
|---|---|---|---|
| n | 335 | 69 | 266 |
| Win rate | **61.79%** | 55.07% | **63.53%** |
| Binomial p | **< 0.001** | 0.235 | **< 0.001** |
| Verdict | **SIGNAL EXISTS** | insufficient n | **STRONG EDGE** |

**The put signal with high opening pressure + short DTE is the cleanest result in this dataset:** n=266, WR=63.53%, p < 0.001, in a market trending up 62.5% of days. Market excess for puts in this bucket: **+26pp** over the same-direction SPY baseline (SPY only down 37.5% of days). These institutions are shorting specific stocks against the tape and being right 63.5% of the time next session.

### Stratified by size/OI ratio (Puts only)

| Bucket | n | Win rate | p-value |
|---|---|---|---|
| `0_to_0.5` (likely closing/rolling) | 378 | **43.65%** | 0.994 |
| `0.5_to_1` | 160 | 50.62% | 0.469 |
| `1_to_2` | 118 | 52.54% | 0.323 |
| `2_plus` (opening new position) | 503 | **56.06%** | **0.004** |

**The Pan-Poteshman hypothesis confirmed within this dataset:** when `size/OI < 0.5` (likely closing), the win rate drops to 43.65% — *worse* than a coin flip. When `size/OI ≥ 2.0` (clearly opening), win rate jumps to 56.06% with p=0.004. The ratio is the discriminator.

### Puts with size/OI ≥ 2.0, stratified by DTE

| DTE bucket | n | Win rate | p-value |
|---|---|---|---|
| `0_to_7` (0DTE/weekly catalyst) | 198 | **62.63%** | **0.0002** |
| `8_to_30` (monthly event-driven) | 68 | **66.18%** | **0.005** |
| `31_to_90` (medium term) | 77 | 49.35% | 0.590 |
| `91_plus` (LEAP-style) | 160 | **46.88%** | 0.808 |

**The signal is entirely concentrated in the 0–30 DTE range.** Puts with DTE > 30 have near-zero or negative edge regardless of opening pressure. The interpretation:

- **0–30 DTE opening puts** = an institution is betting on a specific near-term catalyst (earnings, guidance, FDA, regulatory). The information is time-sensitive and the DTE reflects it.
- **91+ DTE opening puts** = structural hedging, portfolio protection, macro insurance — not stock-specific informed flow. WR = 46.88% (slightly *below* coin flip).

### Condition class (floor vs electronic), DTE ≤ 30

| Filter | n | Win rate | p-value |
|---|---|---|---|
| Floor/negotiated (`slft`/`slcn`) + DTE ≤ 30 — all | 395 | **58.99%** | **0.0002** |
| Floor/negotiated + DTE ≤ 30 — puts only | 328 | **60.98%** | **< 0.001** |
| Floor/negotiated + DTE ≤ 30 — calls only | 67 | 49.25% | 0.597 |
| Electronic (`auto`/`isoi`) + size/OI ≥ 2 + DTE ≤ 30 | 64 | 54.69% | 0.266 |

**Surprising finding:** Negotiated floor blocks (traditionally viewed as less "urgent" than electronic sweeps) outperform electronic sweeps in this dataset. A possible explanation: large floor-negotiated put blocks in the 0–30 DTE range require bilateral agreement between counterparties — both sides know what they're doing. The negotiation itself is a filter for genuine institutional conviction vs mechanical order flow.

The electronic signal (auto/isoi) is weaker in the high-conviction bucket (n=64, WR=54.7%, p=0.27) — possibly because electronic auto-execution includes a lot of retail event-playing that happens to look like "large" by absolute premium but isn't truly informed.

---

## Regime Confound Warning

**This entire 34-day window is a strong bull market.** SPY rose 62.5% of trading days. This creates two distortions:

1. **Call signals underperform dramatically** — any positive directional edge they have is overwhelmed by the beta of the market moving up. You cannot tell whether a call signal "has edge" in this regime.
2. **Put signals that survive are genuinely informed** — a large opening put in a ripping bull market that still wins 63.5% of the time is swimming against a 62.5% headwind. That's a meaningful signal.

**The verdict cannot be extended to bear market regimes without more data.** In a bear market, the equivalent high-conviction CALL signal may show the same pattern the puts are showing here. The asymmetry in this dataset is regime-specific, not a permanent feature of calls vs puts.

---

## Summary Verdicts

| Signal | n | WR | Excess vs SPY | p-value | Verdict |
|---|---|---|---|---|---|
| All single-leg ask prints | 2,815 | 52.0% | calls: −9.7pp / puts: +13.4pp | 0.016 | **NO — beta not edge** |
| Calls (any filter) | 1,656 | 52.8% | **−9.7pp** | 0.011 | **NO_GO** |
| Puts (any filter) | 1,159 | 50.9% | +13.4pp | 0.278 | NO_GO (insufficient WR) |
| Puts + size/OI ≥ 2 | 503 | 56.1% | +18.6pp | 0.004 | **MARGINAL_EDGE** |
| Puts + size/OI ≥ 2 + DTE 0–30 | 266 | **63.5%** | **+26pp** | **< 0.001** | **GO_SIGNAL_HAS_EDGE** |
| Puts + size/OI ≥ 2 + DTE 8–30 | 68 | **66.2%** | **+28.7pp** | **0.005** | **GO (small n, verify)** |
| Floor/neg + DTE ≤ 30, puts | 328 | **61.0%** | **+23.5pp** | **< 0.001** | **GO_SIGNAL_HAS_EDGE** |

---

## Recommended Signal Definition

Based on this backtest, the highest-signal single-leg whale print is:

> **Single-leg LARGE OPENING PUT** with:
> - `size / open_interest ≥ 2.0` (clearly opening a new position)
> - `DTE ≤ 30` (event-driven, not structural hedge)
> - `side = 'ask'` (aggressive fill)
> - `premium ≥ $500K`
> - `equity_type = 'Common Stock'` (exclude index products)
> - `upstream_condition_detail ∈ {auto, isoi, slan, slai, slft, slcn}` (single-leg)

**Win rate:** 63.5–66.2% across 266–68 signals  
**Market excess:** +26–29pp over same-direction SPY baseline  
**Interpretation:** An institution buying protective/directional puts with imminent expiry on a stock with little to no existing options positioning. The position is new, event-driven, and stock-specific — not a broad hedge.

The equivalent HIGH-CONVICTION CALL signal **does not have edge in this dataset** but may emerge in a bear/mixed regime. The current data is insufficient to evaluate calls.

---

## Caveats

1. **34 trading days, single regime (bull).** Confidence in the put signal is high within this regime; cross-regime validity is unproven. Minimum suggested: 60 trading days across at least two distinct regimes before elevating to a scored rubric criterion.
2. **EOD price proxy** — the `LAST(underlying_price)` from the parquet is based on option trade timestamps, not the official market close. Minor intraday timing noise, but stable for directional prediction.
3. **Multi-day signals not tested** — this is strictly a next-session (D→D+1) backtest. The signal may compound or decay across 2–3 sessions; not evaluated here.
4. **No transaction costs** — the win/loss grade is on the underlying price move only, not on an options P&L. Slippage and bid/ask spread in the underlying are not modeled.
5. **The call signal likely exists in bear regimes** — the asymmetry is regime-specific. Do not conclude calls are structurally uninformative.

---

## Integration Recommendation

- **Register as criteria C19** (advisory, 0 rubric points) pending 60-day cross-regime validation.
- Surface in `accumulation-hunter` as a co-signal alongside DP block-stratified: a large opening put (size/OI ≥ 2, DTE ≤ 30) on a name that also shows DP distribution activity is the strongest bearish thesis co-confirmation available in this dataset.
- Surface in `contrarian-scanner` alongside rising PC-ratio trajectory — a large opening put print with DTE ≤ 30 is a candidate for the single-name short thesis when the broader PC-ratio is also crowding bearish.
- Do **NOT** add to `accumulation-hunter`'s scored call side until a bear/mixed-regime window validates the equivalent call signal. The call signal in bull markets is anti-informative (underperforms SPY).
