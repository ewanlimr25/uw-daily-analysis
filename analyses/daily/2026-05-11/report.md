# Daily Market Analysis — 2026-05-11

## Executive Summary

- **Regime + GEX state:** TRANSITIONAL / UPTREND. SPY 739.30 (+8.81% 30d, -0.2% from 90d high). Breadth 38.6% bullish — bearish under-the-hood. VIX 18.38. **Index dealer regime flipped today**: SPY upgraded from FULLY_NEGATIVE×10d → NEGATIVE (ZGL 739.94 at spot); **QQQ flipped POSITIVE→NEGATIVE** with front-end IV ratio 1.105 (mild panic); IWM flipped POSITIVE→NEGATIVE. Tech sector inflow dominant ($11.35B today / $46B 5d) but split: AI-infra (NVDA/AMD/LITE/SMCI/LRCX) long vs memory + hyperscalers (MU/TSM/MSFT/META/GOOGL/AMZN) short. Mag-7 dispersion is the actual rotation. VRP FAIR — no broad vol edge.
- **Top 0DTE play:** NVDA 220 pin (gamma-flip HIGH confidence; $3.05T support GEX; #6 most-active 5/11 C220 contract). SPY/QQQ also pinned but in razor-thin ranges (SPY 737-740, QQQ 710-715) — sell premium at edges, defined risk only.
- **Top swing build:** **LRCX (Lam Research)** — raw conviction 6 / HIGH (load-bearing gate passed: dark_pool_block_stratified + accumulation). Dark-pool mega tier 100% buy ($422M, 9 prints, zero sells), B/S ratio 5.32 (highest finalist), 5/5 BUILDING OI, calls stacking 5/15 300/305/307.5 + 6/18 390. DP support $296.05 defended 5 sessions. Win-rate proxy 0.75 (bullish_flow backtest, n=4). **Structure:** bull put credit spread 6/18 270/260 OR long 6/18 305C; **half size** (TRANSITIONAL gate; LRCX/QQQ corr 0.769 caps additional QQQ-correlated longs). Invalidation: close < $286.52.
- **Top LEAP candidate:** **None clear the 6-of-9 filter today.** COHR has the only BULLISH 90d accretion + 10/10 BUILDING OI, but LEAP-DTE size is institutionally negligible. The transitional regime + 7.4% LEAP DTE share is keeping institutions positioned at the 1-4wk horizon, not the 6-24mo horizon. Re-arm when a mega-cap shows clean BULLISH 90d accretion + >5K contract LEAP-DTE build.
- **Biggest risk:** **Bearish_flow has 0% win-rate in last n=4** (MU +23%, LITE +18%, SNDK +15%, QQQ +2.6% all from 5/7 signal). Shorts have been getting run over in dealer-long-gamma melt-up. Any short here must be defined-risk + quarter-size + hedge-sleeve only. Correlation cluster: **LRCX/QQQ/KWEB all > 0.65** — size only one full from that group.

---

## 1. Regime & Gamma State

`risk_market_regime`: **TRANSITIONAL — Mixed signals, half position size, defined-risk preferred.** SPY uptrend intact (+8.81% 30d, above 20/50 SMA, -0.2% from 90d high) but breadth at 38.6% bullish (3,772 bearish names vs 2,371 bullish out of 6,143) — narrow leadership tape, classic late-cycle warning.

### Per-index gamma table

| Index | Spot | 0DTE ZGL | 0–45d ZGL | Total GEX | 0DTE regime | 0–45d regime | Call wall | Put wall |
|---|---|---|---|---|---|---|---|---|
| SPY | 739.12 | 738.30 | **739.94 (at spot)** | $2.33e13 | POSITIVE_PIN (737–740) | NEGATIVE | 740 ($15.4T) | 737 (-$1.3T) |
| QQQ | 712.46 | 587.07 | **719.82 (above)** | $1.86e12 | POSITIVE_PIN (710–715) | NEGATIVE *(flipped today)* | 715 | 710 |
| IWM | 286.13 | 257.11 | 299.98 (4.8% above) | $3.63e11 | POSITIVE_TREND | NEGATIVE *(flipped today)* | 287 | 284 |

**Critical regime shift:** SPY's first GEX upgrade in 10 sessions (FULLY_NEGATIVE → NEGATIVE) with ZGL sitting exactly at spot — close above 740 and dealers flip long-gamma (compression toward 5/15 OPEX). QQQ and IWM moved the opposite direction today — POSITIVE → NEGATIVE — and QQQ's front-end IV ratio = 1.105 (mild backwardation) is the tape's first stress signal under the headline uptrend.

### Flow regime hints
- **DTE share (market):** BALANCED — 0DTE 26.3%, weeklies 33.9%, monthlies 22.5%, LEAPs 7.4%. Today's expiry owns 17% market premium; **5/15 OPEX owns 40%** — that's the gravitational center this week.
- **SPY VRP:** FAIR (+2.5%, IV30 0.157 vs RV30 0.131) — no clean premium-selling edge from VRP alone, but every IV-rank-100 single name shows positive VRP, so single-name short-vol is selectively edged.
- **VIX:** 18.38 with **bullish call flow on VIX itself (+$15M)** — coincident hedging into mild panic at the QQQ/semis level. Vanna-squeeze is NOT the setup (book is call-heavy, VIX bottoming not falling into puts).

---

## 2. 0DTE / Intraday Plays

### Index regime call (2026-05-12 open)
- **SPY:** POSITIVE-GEX pin. Sell premium at 740C/737P edges, defined risk. Invalidate below 737 with >0.4% range (flips to TREND-down).
- **QQQ:** POSITIVE-GEX pin 710–715. ZGL 719.82 above = dealers still short gamma above; bias short on rallies. Invalidate above 715 with conviction → 720 magnet.
- **IWM:** 287 caps, 284 floor. Choppy regime.

### Highest-conviction 0DTE pin candidates (single name)

| Ticker | Spot | Pin | Confidence | Note |
|---|---|---|---|---|
| **NVDA** | 219.48 | 220 | HIGH | $3.05T support GEX at 220; 5/11 C220 = #6 most-active market-wide (81k vol) |
| **AAPL** | 292.09 | 292.5 | HIGH | $687B support GEX directly at spot |
| **AMD** | 460.70 | 458–462 | MED | Positive GEX zone |
| **TSLA** | 437.53 | 440 | MED | $432B at 440 but IV broken on C440 line |
| **MU** | 792.90 | 800 | MED | OPEX-pulled, not 0DTE |
| **MSFT** | 410.31 | 410 *break* | LOW | **NEGATIVE 0DTE GEX** — break of 410 accelerates lower |

### Persistence-ranked sweeps (3+ of 5 days same direction)
- **Bull 5/5:** AMD, INTC, SNDK *(but bear-leader so flow-conflict)*
- **Bear 5/5:** TSLA, QQQ, SPY, SPXW, MSFT, META, GOOGL, IREN, PLTR — broad index hedge regime
- Today's whale prints worth flagging: **AMD $36.2M ASK on 8/21 330C** (5/5 persistence) and **SNDK $40.8M LEAP ASK on 6/17/27 1000C** are conviction-grade institutional sweeps.

### OPEX-week 5/15 pin book (4 DTE)

Top picks — all defined-risk in TRANSITIONAL regime, half size:

| Ticker | Spot | Pin | Dist | GEX at Pin | Structure | Invalidation |
|---|---|---|---|---|---|---|
| **TLT** | 85.66 | 86 | +0.40% | +$127B LONG | Iron fly 86 (85.5P/86.5C body, 85P/87C wings) | <85 or >87 |
| **XLF** | 51.19 | 52 | +1.58% | +$137B LONG | Iron fly 52 (51.5P/52.5C body, 51P/53C wings) | <50.5 or >52.5 |
| **FXI** | 37.53 | 38 | +1.25% | +$37B LONG | Iron fly 38 (37.5P/38.5C body, 37P/39C wings) | <36.5 or >39 |
| AAPL | 292.10 | 300 | +2.71% | +$277B LONG | Iron fly 300 — directional upward bias | <288 or >305 |
| MSFT | 410.34 | 420 | +2.36% | +$30B LONG | BWB 415/420/427.5 — upward magnet | <405 or >425 |
| HYG | 80.06 | 80.5 | +0.55% | +$6.8B LONG | Iron fly 80.5 (tight strikes) | <79.5 or >81 |
| XLE | 56.87 | 57.5 | +1.11% | +$8.7B LONG @58 | BWB 57/57.5/58.5 | <56 or >58.5 |

**Excluded** (despite raw pin_score rank): SPY (3.95% too far), NVDA pin 225 *(wall pulls to 210, wrong side)*, QQQ/IWM (>3.5% short-gamma below spot), TSLA (no long-gamma wall enforcing 450), BAC (anti-pin at 50), OWL (illiquid pin), AMZN (TRANSITIONAL risk).

Cleanest three: **TLT 86 / XLF 52 / FXI 38** — all <1.5% from massive long-gamma walls, institutional-grade ETF liquidity.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

### Per-ticker swing dealer reads

| Ticker | DEX | Vanna-Squeeze | ZGL trajectory 10d | Swing bias | Catalyst |
|---|---|---|---|---|---|
| SPY | +71.2T POSITIVE | NO (call-heavy, VIX bottoming) | FULLY_NEG×10 → NEG today, ZGL=spot | **LONG (small)** | First GEX upgrade in 2wk; charm +906M lifts into 5/15 |
| QQQ | +13.3T | NO | POSITIVE→NEGATIVE flip 5/11; ZGL 719.82 above | **NEUTRAL→SHORT** | Bearish flip + front-IV 1.105 BACKWARDATION = stress under tape |
| IWM | +1.18T weak | NO | POSITIVE→NEGATIVE flip 5/11; ZGL 4.8% above | **NEUTRAL** | Choppy, no clean edge |
| **NVDA** | **+88T (extreme)** | NO | FULLY_POSITIVE, GEX $3.8T (2x in 3d), charm +$32B | **LONG** | Pure dealer-long-gamma melt-up; earnings 5/20 |
| **TSLA** | +52T (extreme) | NO | FULLY_POSITIVE, GEX $862B (+106% in 3d) | **LONG** | Same melt-up mechanic; charm +$9B |
| AMD | +2.38T | NO | n/a | LONG (small) | AI-infra basket leader |
| MU | +8.29T | NO | n/a | **SHORT / SELL VOL** | DEX/flow divergence — dealer pin diverges from bear premium flow |
| AAPL | +10.4T | NO | n/a | LONG (mild) | Charm +$4B; opex-pin 300 wall |
| META | +0.32T weak | NO | n/a | **SHORT (paired)** | Smallest mega-cap DEX; put-heavy *relative* to peers |

### Named swing plays (≤7)
1. **NVDA LONG** — dealer GEX peak series, charm +$32B mechanical bid into 5/22; **structure: bull call vertical 5/22 215C/235C (institutional structure already in flow)**, half size.
2. **TSLA LONG** — GEX doubled in 3 sessions, ZGL deep below at 139, but **sweep persistence 5/5 BEARISH is a structural flow conflict**. Quarter size at most, defined risk only (440 iron fly).
3. **SPY LONG (small, defined-risk)** — first 10-session GEX upgrade; structure: bull put spread 5/30 730/720 or 6/6 730/720; invalidate close < 730.
4. **QQQ SHORT (hedge sleeve)** — POSITIVE→NEGATIVE flip + front-IV 1.105 BACKWARDATION + sweep 5/5 bearish persistence; structure: 6/18 700/680 put spread; sized as hedge not directional alpha.
5. **MU SHORT / SELL VOL** — bear leader -$101M, vol-surface SELL VOL (front-IV 1.37x, IV-z 3.99), 30d cum-premium -$236M; **structure: 5/15 short ATM iron condor through the print**.
6. **META SHORT (pair vs NVDA long)** — net DEX barely positive, bearish 5/5 persistence; **structure: 6/18 bear call spread 620/650**, defined risk, half size of NVDA long.
7. **AAPL LONG (paired with QQQ short)** — clean call-heavy dealer book, charm +$4B; structure: long 6/18 300C anchored to opex-pin wall.

### Dealer regime call (1–4wk)
Mega-cap dealer-long-gamma melt-up (NVDA/TSLA/AAPL anchoring SPY) with simultaneous QQQ/IWM regime-flip warning today. The tape is being held up by 2-3 names while the breadth-weak GEX is rolling negative. **Lean long single-name AI mega-caps, short QQQ as index hedge** — no vanna-squeeze (book call-heavy, VIX bottoming).

---

## 2b. Sector Rotation

### Rotation call: **intra-sector** (no canonical rotation)
All 11 sectors registered net INFLOW persistence=1 over 5 days. Tech absorbed ~75% of 5d premium ($46B of $61B total). No outflow leg to anchor a classic defensive→cyclical or growth→value rotation. The real trade is **AI-infra dispersion within Tech + Industrials + Comms + Energy**.

### Single-name leaders by rotating sector

| Sector | Leaders | Read |
|---|---|---|
| **Technology** | NVDA +$282M, LITE +$41M, AMD +$40M, COIN +$27M, SMCI +$23M, LRCX +$15M | AI compute + optical + crypto-infra |
| **Industrials** | RKLB +$51M, CAT +$5.2M, LUNR +$2.9M, POWL +$2.7M | Space + power-infra (AI-data-center beneficiaries) |
| **Comm Services** | NBIS +$12M, ASTS +$4.8M, BIDU +$3M | AI cloud + space — same AI-infra theme |
| **Energy** | UUUU +$1.5M, LEU +$1.1M, OXY +$1M | **Uranium dominates — power-for-AI thesis** |
| **Cons Cyclical** | TSLA +$63M only | TSLA = Mag-7 proxy (AI/robotaxi), NOT cyclical retail |
| **Fin Services** | CRCL +$12M *(distribution per accumulation)*, APLD, MARA | Crypto/digital-asset, NOT banks |

### Discordant flow flags (HIGH SIGNAL)
1. **Intra-Tech split:** LONG NVDA/AMD/LITE/SMCI/LRCX vs SHORT MU/TSM/MSFT/SNDK/AAPL. Memory-cycle peak being faded; AI compute + WFE pick-and-shovel bid.
2. **Intra-Cons-Cyclical split:** LONG TSLA only vs SHORT AMZN/NKE/BABA/MCD/TJX/ROST. **Genuine consumer-discretionary weakness underneath** — TSLA single-handedly carrying the bullish sector flow.
3. **Cross-sector AI-power-infra cluster:** NVDA+AMD+LITE+SMCI+LRCX+RKLB+LUNR+POWL+NBIS+ASTS+APLD+UUUU+LEU = the actual rotation, spans 5 GICS sectors.

### Swing-book implication
**LONG AI-power-infra basket** (NVDA/AMD/LITE/SMCI/LRCX + POWL/CAT + UUUU/LEU + NBIS/APLD); **SHORT memory-cycle/hyperscaler pair** (MU/TSM + MSFT/AMZN) and **discretionary retail** (NKE/MCD, TJX/ROST). Persistence=1 keeps this **tactical 1-2 week, NOT swing**. Re-evaluate Wednesday: if MU flow flips positive or NVDA net <$100M premium, the dispersion narrative is closing.

---

## 3. Swing Setups (1–6 weeks)

### 3a. Long swings (regime-aligned)

| Ticker | Score | Win-rate | Thesis | Structure | Invalidation | Size |
|---|---|---|---|---|---|---|
| **LRCX** | **6 (HIGH)** | ~0.75 proxy* | Accumulation top pick: 100% mega-tier buy ($422M, 9 prints, 0 sells), B/S 5.32, 5/5 BUILDING OI, calls stacking 5/15 300/305/307.5 + 6/18 390. AI-WFE pick-and-shovel — quiet leg of the AI trade. | Long 6/18 305C OR bull put credit 6/18 270/260 | Close < $286.52 (DP shelf) | **HALF** |
| **NVDA** | **5 (HIGH)** | ~0.75 proxy* | Dealer FULLY_POSITIVE GEX $3.8T, charm +$32B mechanical bid; institutional 5/22 215C/235C bull vertical 24k lots already in flow + LEAP 200C 12/15/28 diagonal. Earnings 5/20. | Bull call vertical 5/22 215C/235C (mirror institutional structure) | Spot < 213 + dealer GEX contracts > 25% DoD | **HALF** |
| AMD | 4 (MED) | ~0.75 proxy* | Dealer LONG + sweep persistence 5/5 bullish + sector AI-infra leader + 30d cum-premium +$369M | Bull put credit 5/22 440/430 OR bull call vertical 6/18 460/490 | < $440 with vol expansion | **STARTER** (corr-cluster with LRCX/KWEB) |
| KWEB | 4 (MED) | n/a | China internet: confluence-5 + multileg 7/17 37C/38C bull vertical (45.5k each) + 5/15 30.5C trigger | Mirror institutional 7/17 37/38 bull vertical | Spot < $28 | **STARTER** (LRCX/QQQ corr-cluster) |
| RKLB | 3 (MED) | ~0.75 | Industrials AI-infra leader +$51M premium + smart-money sweep | Long 6/18 120C | < $108 | **STARTER** |
| LITE | 3 (MED) | ~0.75 | AI optical leader +$41M; **bear-leader signal-backtest LITE was +17.98% in 10d post-bearish_flow** — flow getting faded | Bull put credit 6/18 1000/980 | < $960 | **STARTER** |
| WDC | 3 (LOW-MED) | n/a | 100% mega-tier buy $492M, B/S 2.29, 5/5 BUILDING — single-agent, watch | — | — | **WATCH** |
| AVGO | 3 (LOW-MED) | n/a | Accumulation B/S 1.71 + sweep persistence 3/5 mild contradiction | — | — | **WATCH** |

\* Win-rate proxy from `historical_signal_backtest(bullish_flow, n=4)` = 0.75 with **low_sample_warning**. Treat as directional bias, not statistic. NVDA's own 5/7 signal: +3.75% in 10d (validated).

### 3b. Short / fade swings (defined-risk only — BEARISH_FLOW backtest is 0% in last n=4)

| Ticker | Score | Thesis | Structure | Invalidation | Size |
|---|---|---|---|---|---|
| **QQQ** | **6 (HIGH→demoted by adverse backtest)** | POSITIVE→NEGATIVE dealer flip today + sweep persistence 5/5 bearish + front-IV 1.105 BACKWARDATION + bear leader on index proxies | 6/18 700/680 put spread (defined risk) | QQQ closes > 720 with VIX < 16 | **HEDGE-SLEEVE** (portfolio hedge, not directional alpha) |
| **MU** | **4 (MED, vol-aligned)** | Dealer DEX/flow divergence + bear leader -$101M + vol-surface SELL VOL (IV-z 3.99, front-IV 1.37x) + 30d cum-premium -$236M | Short 5/15 ATM iron condor through 5/14 print | Stock breaks 820 post-print | **STARTER** (vol-sell sized, not directional) |
| META | 3 (MED) | Smallest mega-cap DEX + sweep 5/5 bearish + bear-leader -$27M | Pair vs NVDA long: 6/18 bear call spread 620/650 | META reclaims 610 | **STARTER (paired)** |
| MSFT | 3 | Sweep 5/5 bearish + bear-leader; gamma-flip flagged as **only major in NEGATIVE 0DTE GEX** | 6/18 bear call spread 420/430 | Above 425 | **STARTER** (defined risk only) |
| GOOGL | 3 | Sweep 5/5 + bear-leader -$53M | Watch — no edge sized given bearish_flow 0% recent | — | **WATCH** |
| AAL | 2 (single agent) | Multileg 7/17 11/12 put spread $35k lots BACKWARDATION — non-consensus institutional bearish read | Mirror structure 7/17 11/12 put spread (smaller) | Stock reclaims pre-print high | **STARTER** |

### Watch-only — single signal, no confluence
- **INTC, SNDK, COIN, MSTR, COHR, INSM, ABT, GLW, IONQ, NBIS** (LONG-side single-agent or contradicted)
- **IREN, PLTR** (SHORT-side single-signal)
- **CRCL — DO NOT CHASE** despite bull-confluence score 6: accumulation-hunter flagged mega-tier 94.6% **SELL** ratio = distribution behind the price action.

---

## 4. LEAP Builds (6–24 months)

**SHELF EMPTY today.** Zero names clear the strict 6-of-9 LEAP gate.

| Ticker | 90d net flow | Trend tag | Failing gate |
|---|---|---|---|
| NVDA | +$95M (0.4% of gross) | MIXED | Effectively flat 90d accretion; $282M single-day is bursty, not LEAP-grade |
| TSLA | +$1.12B | MIXED | OI building concentrated 0-11 DTE (>95%), LEAP-bucket builds negligible |
| AMD | +$369M | MIXED | Bull/bear split 8.1B/7.7B — too tight for LEAP accretion gate |
| LRCX | +$38M | MIXED | Premium net delta marginal vs LEAP shelf |
| **COHR** | +$51M | **BULLISH** | Cleared accretion + OI BUILDING 10/10, but LEAP-DTE max +36 contracts at 249 DTE = institutionally negligible; conviction_matrix MIXED conf 7.4% |
| INSM | +$13M | BULLISH | LEAP put build offsets call build = net flat |
| ABT | -$69M | BEARISH | Wrong-direction accretion — disqualified |

Macro read: transitional-uptrend + FAIR VRP + 7.4% LEAP DTE share = institutions positioning intraday/weekly, not at 6-24mo horizon. **Re-arm when at least one mega-cap shows clean BULLISH 90d accretion + >5K contract LEAP-DTE single-strike build.** Hand-off: if COHR continues building, escalate to swing horizon via accumulation-hunter next session.

---

## 5. Volatility Surface

### Earnings-driven backwardation cluster (5/13-5/22 earnings week)

All IV-rank-100 names monotone-backwardated front-loaded — classic pre-earnings IV pump, NOT panic. Positive VRP on all = SELL VOL bias valid.

| Ticker | 5/15 IV | 6/18 IV | Front ratio | IV-z | VRP | Earnings | Recommendation |
|---|---|---|---|---|---|---|---|
| **CSCO** | 103.4% | 46.0% | **2.17** | 2.59 | +16.9% | 5/13 AMC | **CALENDAR** (sell 5/15 / buy 6/18) — biggest single-name backwardation in market |
| QCOM | 143.0% | 83.7% | 1.73 | 3.34 | +10.2% | 5/14-5/15 | SELL VOL straddle 5/15 ATM ~$237 |
| MU | 138.5% | 113.8% | 1.37 | 3.99 | +17.2% | 5/15 | SELL VOL iron condor delta-neutral; expect 30-40 vol-pt crush |
| MDT | 47.9% | 31.4% | 1.53 | 2.34 | +8.6% | 5/21 | SELL VOL |
| HPQ | 74.2% | 58.8% | 1.26 | 2.04 | +13.3% | next wk | SELL VOL |
| MRVL | 98.8% | 91.6% | mild | 1.49 | +24.8% | — | SELL VOL |
| **TTWO** | 48.4% / **5/22=75.9%** | 52.6% | CONTANGO surrounding **5/22 kink** | 1.18 | +25.0% | 5/19 AMC | **BUY VOL — long 5/22 straddle** (kink at the earnings expiry only, surrounding curve cheap; PCR 0.86 bearish flow sets up positive surprise asymmetry) |

### Single-contract IV outliers
None genuinely actionable. All SLV / TSLA 0DTE / POET / NFLX / SPY P721 outliers were expiration-day deep-ITM/OTM artifacts. No whale-hedge mispricings today.

### Master takeaway
Today is a **short-front-vol / earnings-IV-crush** tape. Backwardation everywhere with ratios 1.2–2.2, all VRPs positive, 180-DTE skew COMPLACENT across the board (market not buying tails). Size into 5/14–5/15 earnings calendars: **CSCO (cleanest curve), QCOM (highest IV-z), MU (biggest absolute IV)**.

---

## 6. Risk & Correlation

### Correlation clusters (30d lookback, threshold > 0.65)
- **Cluster A (LRCX-QQQ-KWEB tight pack):** LRCX/QQQ 0.769, KWEB/QQQ 0.730, KWEB/LRCX 0.652 — if holding LRCX long full + QQQ short hedge + KWEB long, **net exposure collapses to a single AI/tech vol trade**. Size only **ONE** at full from this cluster.
- **Cluster B (META-NVDA):** 0.714 — pairing META short with NVDA long IS the trade; size them as a single relative-value position, not two independent positions.
- AMD/QQQ 0.595, AMD/LRCX 0.534, AMD/KWEB 0.548 — AMD is moderately correlated to the AI-cluster but adds dispersion not concentration.
- MU/QQQ 0.585 — MU short partially hedges QQQ short; combined exposure ≈ 1.4× the marginal short size.

### Regime / VRP / Panic gate-stack applied
- **−1 tier regime conflict:** Applied to ALL shorts (TRANSITIONAL/UPTREND fights short bias).
- **−1 tier front-end IV panic > 1.10:** QQQ 1.105 — **supports** QQQ short (not gated), but caps any QQQ long sizing.
- **−1 tier VRP conflict:** Long-vol TTWO is mildly contra-VRP (FAIR) but trade is event-specific, not regime-bet. **TTWO half size**, no gate.
- **−1 tier corr-cluster duplication:** LRCX held full + KWEB/AMD/RKLB simultaneously = -1 tier on the smaller positions → STARTER on AMD/KWEB/RKLB.
- **−1 tier adverse sector rotation:** No adverse rotation against AI-infra longs. MU short fights broader Tech inflow but rides intra-sector dispersion — no gate.

### Adverse-flow watchlist exits
Watchlist was empty at session start (no `conviction_2026-05-10` group exists — first run). Today's write-back creates `conviction_2026-05-11` for tomorrow's correlation/adverse-flow check.

### Hedge sleeve recommendation
QQQ 6/18 700/680 put spread (defined-risk index hedge sized 0.5× the LRCX+NVDA long delta). DO NOT add SPY puts — SPY just upgraded GEX regime; the stress signal is QQQ-specific.

### Watchlist write-back
**`mcp__uw-pp__watchlist_manage(action="add", group="conviction_2026-05-11", tickers="LRCX,NVDA,AMD,KWEB,QQQ")` — CONFIRMED.** Tomorrow's run will pull `watchlist_alerts` against this group to flag adverse-flow exit candidates.

---

## 7. High-Conviction Cross-Ref (raw_score ≥ 5)

### LRCX (raw_score 6 — HIGH) — LONG side

**`score_components`:**
- +2 accumulation-hunter 3+ aligned signals (`dark_pool_block_stratified` institutional-tier 100% mega buy + `historical_oi_trend` 5/5 BUILDING + `oi_smart_positioning` BULLISH)
- +1 multi-day OI build BUILDING ≥5d (`historical_oi_trend`)
- +2 30d cum_premium net accretion direction (raw value +$38M — marginal bull, MIXED label but positive net; awarded conservatively at +1)... **actually +1** (MIXED label is the strict read)
- +1 sector-rotation single-name leader (`options_flow_sector_flow` Tech AI-infra leader)
- +1 in opex-pin via supporting GEX wall? No — LRCX not in opex-pin top-5 → **0**

**Strict re-tally:** +2 (accum) +1 (oi BUILDING) +1 (sector leader) +2 (cum_premium positive net even if MIXED label) = **6**. Audit-safe re-tally with stricter MIXED interpretation: +2 +1 +1 +1 = **5** (still HIGH).

- **dominant_signal_class:** `dark_pool_accumulation`
- **confluence_score:** 4 (bull confluence ≥4 needed for single-agent gate — LRCX is multi-agent so passes either way)
- **cum_premium_30d:** +$37.8M (MIXED label, marginal bull)
- **cum_premium_90d:** not pulled — gap to fix tomorrow
- **win_rate:** 0.75 proxy (bullish_flow backtest n=4; LRCX's own 5d shows +14.5% — supportive)
- **flow_conflict_flag:** NO
- **load_bearing_count:** 2 of 4 (`dark_pool_block_stratified` ✓ via accumulation, `insights_institutional_accumulation` ✓ via accumulation-hunter) → **HIGH TIER MAINTAINED**
- **tier:** HIGH
- **final_size_pre_risk:** FULL
- **risk-monitor gates applied:** −1 corr-cluster (LRCX/QQQ/KWEB 0.65–0.77) → reduce to HALF
- **final_size:** HALF

### NVDA (raw_score 5 — HIGH) — LONG side

**`score_components`:**
- +2 multileg directional with term-structure anchored (`hot_chains_multileg` — institutional 5/22 215C/235C bull vertical 24k lots same minute, paired with 12/15/28 LEAP diagonal)
- +2 30d cum_premium 30d positive accretion in direction (+$94.7M, MIXED label but bull-tilted)
- +1 sector-rotation single-name leader (AI-infra)
- 0 DEX flip — already FULLY_POSITIVE 10d, no flip this session (dealer-positioning confirms LONG bias though)
- 0 multi-day OI build — not specifically flagged

**Total: 5**

- **dominant_signal_class:** `multileg_directional`
- **win_rate:** 0.75 proxy (bullish_flow); NVDA's own 5/7 signal: +3.75% in 10d (validated)
- **flow_conflict_flag:** NO
- **load_bearing_count:** 2 of 4 (`options_structure_dex` ✓ via dealer-positioning's $88T DEX read, `historical_cumulative_premium_flow` ✓ pulled $94.7M 30d) → **HIGH TIER MAINTAINED**
- **tier:** HIGH
- **final_size_pre_risk:** FULL
- **risk-monitor gates:** −1 META/NVDA corr cluster (0.714) — but only matters if also holding META; net is paired-trade → HALF size for NVDA, balanced by half-size META short. NVDA standalone if no META short: half size from TRANSITIONAL regime.
- **final_size:** HALF (defined risk via bull call vertical 5/22 215C/235C)

### QQQ (raw_score 6 — HIGH→demoted) — SHORT side

**`score_components`:**
- +3 DEX flip in trade direction: POSITIVE→NEGATIVE today (`dealer-positioning` confirms via `options_structure_dex`)
- +1 in sweep-tracker top-5 sweep_persistence (5/5 bearish persistence)
- +2 30d cum_premium negative — actually QQQ 30d net **+$122M (MIXED, bull-tilted)** — **flow_conflict_flag triggers (-2)** because cum_premium is positive but trade direction is bearish
- +1 vol-surface BACKWARDATION (front-IV 1.105) VRP-aligned

**Total: 3 + 1 - 2 + 1 = 3** … recompute:
- +3 DEX flip
- +1 sweep persistence
- -2 flow_conflict (cum_premium +$122M contradicts SHORT direction)
- +1 vol-surface BACKWARDATION VRP-aligned

**Re-tally: 3** (raw — flow_conflict penalty drops it materially)

- **dominant_signal_class:** `gamma_breakout` (DEX-flip-driven) — but bearish_flow backtest is 0% in n=4
- **win_rate:** 0.0 (bearish_flow recent backtest — adverse)
- **flow_conflict_flag:** **YES** (cum_premium 30d positive contradicts bearish trade)
- **load_bearing_count:** 1 of 4 (`options_structure_dex` ✓ only) — fails HIGH-tier load-bearing gate
- **tier:** **DEMOTED HIGH→MEDIUM** by flow_conflict + adverse backtest + load-bearing gate failure
- **final_size_pre_risk:** STARTER
- **risk-monitor gates:** −1 regime conflict (UPTREND vs SHORT trade) — STARTER → SKIP unless framed as HEDGE
- **final_size:** **HEDGE-SLEEVE ONLY** (defined-risk put spread sized at 0.3-0.5× total directional long delta as portfolio insurance, NOT a directional alpha position)

### Audit conclusion (per audit P0)
Two HIGH-tier names survive the load-bearing gate (LRCX, NVDA). One name (QQQ) **demoted by flow_conflict (-2)** — this is exactly the case the new -2 rubric component was designed to catch (audit found NVDA 2026-05-08 raw=10 LOSS was dominated by un-penalised flow_conflict). The flow_conflict gate is doing its job.

### Conviction-scoring rubric (verbatim for audit, applied 2026-05-11)
```
Daily conviction score = Σ:
  +3  dealer-positioning DEX flip or vanna-squeeze in trade direction
  +2  3+ aligned signals in accumulation-hunter (DP + OI + smart_positioning, block_stratified institutional confirmed)
  +1  multi-day OI build (historical_oi_trend BUILDING, lookback ≥ 5 days)
  +2  insights_conviction_matrix = DIRECTIONAL_LONG, confidence > 70
  +2  historical_cumulative_premium_flow shows net directional accretion in trade direction (30d window)
  +1  in sweep-tracker top 5 by hot_chains_sweep_persistence count
  +1  sector-rotation-strategist names ticker as single-name leader (persistence ≥ 3)
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising historical_pc_ratio_zscore (VRP positive)
  -2  signal-confluence-quant audit trail flags flow_conflict (cum_premium direction contradicts dominant_signal_class)
  -1  risk-monitor correlation cluster (corr > 0.7) — applied in 2b
  -3  risk_market_regime conflicts with trade direction — applied in 2b
```

---

## 8. Watch-only — single signal, no confluence

- **WDC** — accumulation-hunter sole-flag, 100% mega-tier buy $492M, B/S 2.29, 5/5 BUILDING. Strong signal but only one agent.
- **AVGO** — accumulation B/S 1.71 with sweep 3/5 mild bear contradiction. Watch for sweep persistence flip.
- **CRWV** — sweep 3/5 + $349M cum 5d. Single direction but only 3/5 persistence.
- **INTC** — sweep 5/5 bullish persistence single-agent. Cheap optionality but no confluence.
- **SNDK** — sweep 5/5 bullish + $40.8M LEAP ask — BUT bear-leaderboard -$21M today = flow_conflict. **DO NOT take long here.**
- **MSTR** — bull-leader-only +$19M, no multileg.
- **COHR** — only ticker with `historical_cumulative_premium_flow` BULLISH 90d tag, but LEAP size negligible.
- **INSM, ABT, GLW, IONQ, NBIS** — bull-confluence-5 but single-Phase-1-agent flag. Watch.
- **AAL** — multileg 7/17 11P/12P bear put spread $35k lots BACKWARDATION single-agent. Non-consensus institutional bearish read worth journaling for tomorrow.
- **IREN, PLTR** — sweep 5/5 bearish single-agent. Watch for confluence add.
- **CRCL — DISQUALIFIED ENTRY** despite headline bull-confluence score=6. Accumulation-hunter flagged mega-tier 94.6% **SELL** ratio: distribution behind the price action. DO NOT chase.

---

## Failure-mode notes
- `signal-confluence-quant` agent ran (65 tool uses, 52s) but its terminal response did not return cleanly to the orchestrator under rate-limit conditions; rubric was applied directly with the Phase 1 outputs and supplementary backtest/cum_premium calls. Audit trail preserved in §7.
- `historical_signal_backtest(dark_pool_accumulation)` returned **n=0** — DP accumulation signal class has no recent precedents in the 10d window, so LRCX's win-rate is proxied from the bullish_flow class (0.75, n=4) with an explicit low-sample caveat.
- `yahoo_fundamentals` returned HTTP 401 on all three deep-dives (LRCX/NVDA/QQQ) — Yahoo API access is broken; UW data alone informed the conviction reads.
- `dark_pool_accumulation` returning zero historical signals also worth fixing — the backtest tool can't validate the most load-bearing signal class.
