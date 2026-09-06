# Daily Market Analysis — 2026-05-07

## Executive Summary

- **Regime + GEX state**: TRANSITIONAL — SPY 731.58 in price uptrend (+8.22% 30d) but breadth POOR (33.3% bullish, 2046 bull / 4098 bear tickers) with VIX ELEVATED at 17.08. **SPY GEX flipped POSITIVE → NEGATIVE today** (-$434B 45-DTE, ZGL 729.88 just below spot) after only one session above the flip. **IWM FULLY_NEGATIVE 13/15 sessions** (-$663B), no ZGL anchor — cleanest trend vehicle. QQQ NEAR_FLIP at ZGL 699.39 vs spot 696.44, but DEX +19.5T call-heavy supports single-name dip-buying. SPY front-end IV ratio 1.059 — within 5% of 1.10 panic trip. Tech leads on magnitude ($6.09B net 5/5-day inflow); intra-Tech rotation: AI infra/software BID, memory/merchant silicon FADED. Half size, defined risk only.
- **Top 0DTE play**: SPY 730/735 knife-edge — buy gamma into a break of 736 (long) or 730 (short). NVDA 212.5 PIN with three top-30 active 0DTE strikes at 210/212.5/215 — clean magnet trade.
- **Top swing build (1-4w)**: **AAPL** — score 13, dark-pool-accumulation class, **win-rate 90%**, full size. Mega-tier 87% buy ratio, $499M single DP print, 5/5 OI BUILDING (4,506,856 → 4,951,152 contracts), 295/320 5/22-6/19 long diagonal $128M coordinated. Structure: 6/19 295/305 call debit spread or long 6/19 300C. Invalidation: $276.83 multi-day DP floor.
- **Top LEAP candidate**: **None qualified** — leap-positioning-radar passed zero of nine gates today (binding constraint: conviction_matrix < 70% confidence across the universe). Closest miss: **DKNG** 5/9 gates (failed conviction 19.6% + IV 64). Tripwire: re-run when DKNG IV rank drops below 50 + conviction crosses 70 with 30C/37.5C Nov-2026 builds extending ASK-side.
- **Biggest risk**: **Dark-pool-accumulation Tech cluster** (AAPL + QCOM + MSTR same dominant signal class, 90% backtest win-rate) is a single trade. AAPL/QCOM kept full size; MSTR cut to half. **Hedge sleeve = 3-4% notional**: IWM put debit spread post-OPEX + SMH calendar (only put-heavy DEX in the single-name universe).

---

## 1. Regime & Gamma State

**Macro readings**:
- `market_regime`: TRANSITIONAL — UPTREND, VIX ELEVATED, breadth 33.3% bullish (2046 / 6144 names with bullish flow). Money rotated INTO Cons Cyclical / Cons Defensive / Energy on the daily; OUT of Tech / Financial Services / Communication Services per the regime classifier — but the multi-day persistence read disagrees and is the durable signal.
- `dte_volume_share`: BALANCED — 0DTE 22.9%, weeklies 28.6%, monthlies 34.0%, LEAPs 6.2%. Institutional anchor at the monthly bucket; today's 5/22 and 6/19 monthly expiries dominate the multileg book.
- `volatility_risk_premium` (SPY): VRP -0.0119 = FAIR. IV30 14.75% vs realised σ 15.94%. No clear edge for premium-buying or premium-selling at the index — single-name VRPs override.

### Per-index gamma table

| Ticker | Spot | Zero-Gamma | Total GEX (45D) | Regime | Call Wall | Put Wall | Read |
|---|---|---|---|---|---|---|---|
| **SPY** | 733.60 | n/a (FULLY_NEG) | -$434B | **TREND** | 735 (+$6.1T 0DTE) | 730 (-$5.86T) | Knife edge 730-736; sustained > 736 = trend up to 740, sustained < 730 = acceleration to 727/725 |
| **QQQ** | 696.44 | 699.39 | +$2.80T (today +$2.47T) | **NEAR_FLIP** | 700 (+$1.6T) | 692 | Spot 3 pts BELOW flip; 700 magnet from below; CONTANGO term structure supports pinning |
| **IWM** | 284.66 | n/a (FULLY_NEG) | -$663B | **TREND** | 286 | 282 | FULLY_NEGATIVE 13/15 sessions; cleanest momentum/trend vehicle of the three |

### Single-name 0DTE pins

| Ticker | Spot | Pin Strike | Distance | Thesis |
|---|---|---|---|---|
| NVDA | 212.15 | 212.5 | 0.16% | Dense +GEX 210/212.5/215 (+$2.4-2.9T each); 3 of top 30 active 0DTE strikes |
| AAPL | 289.97 | 290 | 0.01% | Total GEX +$2.84T; +$1.0T support at 290 + $1.03T at 295. ZGL 136.71 deep below |
| TSLA | 410.12 | 410 | 0.03% | Three stacked walls 410/415/420 all positive. Dealer-stabilized 410-420 corridor |
| AMZN | 273.17 | 275 | 0.67% | +$121B at 275, but -$98B at 270 = vulnerable below 272.5 |
| ORCL | 197.09 | 200 | 1.48% | Asymmetric drift — +$58B wall at 200 vs +$5B at 195 |

---

## 2. 0DTE / Intraday Plays

**Indices**: SPY 730-736 is THE level. QQQ 700 is the tech-tape governor (reclaim unlocks bullish pin). IWM 286 / 282 — pure trend, no walls.

**Sweep urgency-rank (multi-day persistence FIRST, today's premium SECOND)**:

| Rank | Ticker | Side | 5d Persistence | Today | Note |
|---|---|---|---|---|---|
| 1 | **SNDK** | BULL | 5/5 | call-led | Cleanest single-name BULL persistence ($1.21B 5d) but DP buy_ratio 0.487 NEUTRAL — accumulation-hunter excludes |
| 2 | **ORCL** | BULL | 5/5 | call-led | Watchlist heat; PIN 200 magnet aligned |
| 3 | **AMZN** | BEAR | 5/5 | put-led | Bear persistence in mega-cap CONFLICTS with accumulation-hunter $2.06B DP build — dropped from book |
| 4 | **MSFT** | BEAR | 5/5 | bid-side calls SOLD | Today's $32M Jun 450C + $13.5M Nov 575C SOLD on bid CONFIRMS bear; accumulation-hunter flags MSFT DISTRIBUTION (mega 35.8% buy ratio) — dropped, contradiction |
| 5 | **META** | BEAR | 5/5 | put-led | Confirmed by deep-ITM 5/15 put stacking $54M+ ASK — half-size short |

**OPEX**: 8 days from May 15 — outside the 5d window, no `opex-pin-strategist` spawn.

---

## 2a. Swing Dealer Positioning (1-4 weeks)

**Index DEX bifurcation** is the central read:
- **SPY**: PUT-HEAVY DEX -2.5T, **regime FLIP today** (POSITIVE → NEGATIVE GEX); failed to hold the one-day positive-gamma window (5/6 ZGL 729.88). Front-end IV ratio 1.059 = mild backwardation, panic-adjacent. **Swing bias: BEARISH-TO-NEUTRAL**, defined-risk SPY put spreads 30-45 DTE post-OPEX.
- **QQQ**: CALL-HEAVY DEX +19.5T (the swing tailwind). Spot below ZGL = whipsaw zone. Long calendars / wide iron flies preferred over directional.
- **IWM**: PUT-HEAVY DEX -892B, FULLY_NEGATIVE 13/15 sessions, no ZGL anchor. **Cleanest negative-GEX expression** = primary hedge carrier.

**Single-name DEX standouts**:
- **NVDA** — extreme call-heavy DEX +115T (largest in book), POSITIVE GEX 11T, ZGL 11.78 deep below spot 211.5 = strongest dealer-long-gamma cushion. **Buy dips, sell vol on rallies.**
- **AAPL** — POSITIVE GEX 3.6T, +27T DEX, 290 call wall = strong pin-and-grind setup.
- **AMD** — gamma compressed -88% in 24 hours (5/6 → 5/7); semi hedge cluster headwind. Not directional alpha; fade.
- **SMH** — only put-heavy DEX in the single-name universe (-89B). **Sole vanna-squeeze geometry** if VIX breaks 15. Confirms institutional semi hedging through ETF.

**No clean vanna-squeeze longs** — every megacap is call-heavy negative-vanna, so falling VIX would trigger dealer SELLING, not buying.

---

## 2b. Sector Rotation

**Regime call**: `sub_sector_rotation` — no sector-level rotation (all 11 sectors persistence 1.0 INFLOW; Real Estate 0.8). The decisive rotation is **WITHIN Tech**: AI infra / software BID (NVDA, MSFT, QCOM, AAPL, ORCL, CRWD, NOW), memory + merchant silicon FADED (MU -$115M, SNDK -$37M, AMD -$19M, MRVL, WDC, LITE).

| Sector | Top 3 Long | Top 3 Short | Persistence | Inst DTE % | Sub-sector note |
|---|---|---|---|---|---|
| Technology | NVDA, MSFT, QCOM | MU, SNDK, AMD | 1.0 | 74.6% | AI-infra LEAD; memory + merchant silicon FADE |
| Cons Cyclical | TSLA, CVNA, HD | AMZN, GME, MCD | 1.0 | 92.2% | TSLA-driven; HD/LEN housing bid; e-comm faded |
| Financial | IREN, BRKB, COF | C, JPM, GS | 1.0 | 84.7% | Money-center banks FADED; crypto-adj + insurance bid |
| Healthcare | MRNA, UNH, TMO | LLY, CNC, SYK | 1.0 | 84.4% | GLP-1 (LLY/NVO) UNWIND continues |
| Comm Services | NFLX, GOOG, DIS | GOOGL, META, ASTS | 1.0 | 27.4% (BAL) | NFLX cleanest; META distribution; GOOG/GOOGL class-share noise |
| Energy | DVN, LNG, CVX | XOM, COP, FANG | 1.0 | 65.6% | Upstream/E&P bid; majors sold — counter-rotation within Energy |
| Industrials | CODI, AAON, AXON | RKLB, BE, UAL | 1.0 | 89.8% | Defense + HVAC bid; airlines + space FADED |

---

## 3. Swing Setups (1-6 weeks)

Ranked by post-risk size (full > half > starter). All quoted sizes are post-gate.

### 3a. Long swings (regime-aligned)

| Ticker | Score | Thesis | Structure | Invalidation | Size |
|---|---|---|---|---|---|
| **AAPL** | 13 | Mega-tier 87% buy / $499M single DP / 5/5 OI BUILDING (4.51M → 4.95M) / 290 call wall pin / 295/320 5/22-6/19 long diagonal $128M same-second exec. Cum-prem 30d +$428M. Aug C320 ASK $56M today. Dom class: dark_pool_accumulation, **WR 90%**. | **6/19 295/305 call debit spread** — defined-risk equivalent of multileg's diagonal | $276.83 multi-day DP floor or mega buy_ratio < 0.55 | **FULL** |
| **QCOM** | 12 | Mega 100% buy 8 prints / $1.9B DP / 5/5 BUILDING / multi-month ladder (6/19 180C + 7/17 270C + 8/21) / Step 0 confluence 5 / Tech AI-infra leader / vol-surface KINKED 5/22 z=+3.14. IV 100 = expensive vega — **prefer Bull Put Spread NOT long calls** (matches batch_strategy_scan). Cum-prem 30d +$106M. **WR 90%.** | **Bull put spread 195P / 185P 5/22** — collect rich premium with defined risk; or 6/19 200/210 call debit spread for cheaper-vega expression | $192.57 reactivation level / mega ratio drops below 0.7 | **FULL** |
| **NVDA** | 11 | DEX +115T LARGEST in tape / POSITIVE GEX 11T / PIN 212.5 / 217.5/225 5/15 bull vertical (60k contracts each leg, $33M) / 5/22 KINKED earnings (May 19 next print). Today bullish $43M 5/8 205C ASK + $10M 5/15 225C ASK. **Earnings 12 days out — vol play overlays directional**. Dom class: gamma_breakout, WR 75%. **Multileg overrides batch_strategy "no edge"** (saw the actual coordinated 60k+ vertical). | **Layer**: (a) directional 217.5/225 5/15 call vertical (multileg-confirmed, 8 DTE); (b) earnings vol structure 5/22 short ATM fly + 6/18 wings (vol-surface KINKED) | DEX flips call-heavy → put-heavy / 200 ZGL band breaks | **FULL** |
| **GOOG** | 9 | Step 0 confluence 5 / Comm Svc leader / cum-prem 30d +$322M / DP $21M + OI +77k. **Diversifies the Tech-heavy book** (Comm Svc not Tech). WR 75%. Use GOOG share class only; GOOGL class shows divergent flow (-$120M 30d) — see §8. | **6/19 400/420 call debit spread** | < 50d SMA / cum-prem flips bear | **FULL** |
| **MSTR** | 9 | Mega 100% buy 5 prints / $741M DP / 5/5 BUILDING / 7/17 C180 +13k 2-day persistent / IV pct=0 z=-2.45 (cheap vega vs own history). Dom class: dark_pool_accumulation. **CLUSTER GATE** with AAPL/QCOM (same signal class) → cut full → half. Beta 3.595 high, regime gate also fires. | **8/21 ATM call** — cheap vega LONG | $179.84 anchor break | **HALF** |
| **TSLA** | 7 | DEX +69T 2nd largest / pin 410-420 corridor / IV rank 8 cheap vega / cum-prem 30d +$980M / Cyclical leader. Regime gate (high-beta, breadth-poor) → full → half. WR 75%. | **Long 6/19 ATM call or 410/430 debit spread** | Below 400 with no positive gamma support | **HALF** |
| **SHOP** | 8 | Smart-positioning extreme bullish (9/18 C160/C195 ASK-side opens, OI +241k today) / cum-prem 30d +$116M / Tech leader. DP NEUTRAL is the caveat. Regime gate (high-beta software) → half. | **9/18 ATM call** — LEAP-style cheap vega | DP turns DISTRIBUTION / 9/18 calls show next-session unwinding | **HALF** |
| **ORCL** | 6 | 5/5 BULL sweep persistence ($677M) / DEX +3.5T / PIN 200 / watchlist $156M DP. Cum-prem 30d -$320M is a CONFLICT (today's sweep dominates but historical net-bear caps to half). | **Bull put spread 190P / 180P 6/19** | Sweep persistence breaks / VWAP fails 90 min | **HALF** |
| **CORZ** | 8 | Highest Step 0 confluence score (6) / single-day 9/18 27C 286x ASK / IV 14 cheap. Microcap-liquidity capped to starter. WR 75-90%. | **Long 9/18 27C** (define risk via call debit spread if liquidity allows) | Single-day flow doesn't persist; reverses | **STARTER** |
| **C** | 7 | Multileg HIGH (135/145 5/15 bull vertical, 52k each leg ratio 0.99) / DP $165M. **CLUSTER GATE** with SPY-short (corr 0.817) — same broad-beta book — cut to starter. Batch_strategy says BEARISH; prefer multileg (saw the 52k coordinated vertical). | **5/15 135/145 call vertical** at quoted strikes | Below 132 by 5/12 | **STARTER** |
| **CODI** | 6 | LEAP whale 1/15/27 10C/20C 97x and 52x ASK ratios; clean LEAP vertical $10 wide on $12 stock = ~5x payoff. Microcap floor. | **1/15/27 10/20 LEAP call spread** | Below $10 by 7/17 / no follow-through | **STARTER** |
| **ON** | 6 | Mega 96% buy / $918M DP / single $331M print +$0.74 above mid / 9/18 C145 LEAP-style ladder. Cluster gate (ADI dup analog-semi) → half → starter. | **9/18 ATM/OTM call ladder, defined risk** | $102.67 multi-day pivot / mega exhausts | **STARTER** |

### 3b. Short / fade swings (defined risk only)

| Ticker | Score | Thesis | Structure | Invalidation | Size |
|---|---|---|---|---|---|
| **IWM** | 4 | FULLY_NEGATIVE GEX 13/15 sessions, no ZGL anchor, put-heavy DEX -892B, cum-prem 30d -$994M. CONFLICT: today's sweep saw bullish put-selling. Bearish flow backtest WR 37.5% in this UPTREND tape. **Primary hedge carrier**. | **IWM put debit spread, 21-30 DTE post-OPEX, 5-10% OTM, 10-pt wide** | SPY breadth recovers > 40% / IWM reclaims 286 with momentum | **HALF** |
| **META** | 4 | Multileg HIGH bear: deep-ITM 5/15 710/730/750P stacked $54M+ ASK = synthetic short / sweep 5/5 BEAR persistence $893M / cum-prem 30d -$562M. NVDA-long pair (corr 0.735) — net AI-mega flat. | **5/22 600/580 put debit spread** | META reclaims $640 within 5 days | **HALF** |
| **SPY** | 5 | Dealer GEX FLIP (POSITIVE → NEGATIVE today) + put-heavy DEX -2.5T + sweep 5/5 BEAR $7.2B 5d + 5/29 710/675 bear put $28.6M. Dealer-flip is FRESH not yet 2nd-session-confirmed. Bear flow WR 37.5%. | **5/29 705/685 bear put spread** (post-OPEX expiry preferred to manage gamma) | SPY reclaims and holds > 736; OR front-end IV ratio prints < 1.04 | **STARTER** |
| **MU** | 4 | Multileg HIGH bear: 7/17 850P deep-ITM stacked $77M ASK / memory rotation FADED / cum-prem 30d -$384M. CAUTION: MU 5/5 bullish_flow backtest +1.07% (squeeze). | **6/19 600/550 put debit spread** | Memory rotation flips / today's 850P stacking unwinds | **STARTER** |
| **SMH** | 3 | Only put-heavy DEX (-89B) in single-name universe / institutional semi hedge inference. **Hedge sleeve only**, not directional alpha. Cluster gate (SPY/SMH 0.819). | **6/19 530/510 put debit spread** | DEX flips call-heavy / VIX < 15 → vanna-squeeze risk | **STARTER (hedge)** |

**Risk-monitor DROPPED for regime/correlation conflict**:
- **KWEB**: cluster duplicate of FXI (0.93 corr) — only one survives.
- **FXI**: institutional LONG flow today (5.2x volume + $75M DP + P/C 0.09 retail call mania). Multileg flagged it as LONG covered-call ladder — fighting the tape. **DROP entirely**; the contrarian thesis (overcrowded long + IV 70) is overridden by the structural read.

---

## 4. LEAP Builds (6-24 months)

**ZERO names qualified the 6-of-9 gate today.** The conviction matrix gate (>70% confidence) is the binding constraint — across the entire macro big-OI builder universe and the 25-name fresh-LEAP-OI top list, no ticker registered DIRECTIONAL_LONG > 70%.

**Closest miss**: **DKNG** — 5/9 gates passed.
- ✓ 197 DTE 30C/37.5C fresh build +60k contracts ASK-side
- ✓ Not a roll; ✓ BUILDING 10 days +217k OI; ✓ +$12.1M cum-prem 90d bullish; ✓ institutional ACCUMULATION DP buy/sell 1.87, $28.5M premium clustered $24.56-25.22
- ✗ conviction_matrix DIRECTIONAL_LONG only **19.6%** (need > 70)
- ✗ IV rank 64.3 (need < 60 for LEAP-cheap-vega)
- **Tripwire**: re-run when IV rank drops below 50 + conviction crosses 70 with the 30C/37.5C Nov 2026 builds extending ASK-side.

Other near-misses (each failed gate 6 / conviction matrix):
- **PCG** — 5/9 short-side; conviction DIRECTIONAL_SHORT 67.7% (just below 70). Watch for fresh PUT-LEAP ASK-side prints to confirm.
- **CPNG** — 4/9; covered-call scenario at 20.4% (yield enhancement, not LEAP buying).
- **IREN, AUR, NOK, TSM, GOOG, AMZN, NVDA, AAPL, TSLA, AMD, SHOP, HOOD, FTNT, SNDK, JOBY** — all conviction matrices returned MIXED or COVERED_CALL with confidence < 20%. The mega-cap tape today is dominated by call-overwriting against existing long stock, NOT directional call-buying.

**Bottom line**: no LEAP positions to take.

---

## 5. Volatility Surface

### KINKED with catalyst alignment

| Ticker | Kink DTE | Read | Trade |
|---|---|---|---|
| **NVDA** | 5/22 (15D) | 5/15 IV 44.8% → 5/22 IV **57.2%** → 5/29 IV 52.7%. NVDA earnings ~5/19 = textbook event kink. Implied move ~7.5%. | Sell 5/22 ATM iron fly vs long 6/18 wings (double diagonal) |
| **MRVL** | 5/29 (22D) | 5/22 74.3% → **92.6%** → 88.1%. MRVL earnings late May. IV pct 89, z +1.23 | Short 5/29 / long 7/17 ATM straddle calendar |
| **QCOM** | 5/22 (15D) | 5/15 82.6% → **103.5%** → 67.6%. Anomaly z=+3.14. Likely event/catalyst-priced expiry | Long 5/15 / short 5/22 calendar (sell the kinked expiry) |
| **FUTU** | 6/05 (29D) | 5/29 57.9% → **75.5%** → 63.1% +18pt jump = earnings 6/05. z=+5.15 (extreme outlier) | Sell 6/05 / buy 7/17 ATM straddle (5σ rich) |

### Backwardation calendars (no catalyst)

| Ticker | Term state | Trade |
|---|---|---|
| **MCHP** | 5/15 85% → 5/22 71% → 7/17 58% — 27pt collapse in 60 days. IV pct 100 z=+1.77 | Sell 5/15 / buy 7/17 strangle |
| **INTC** | Persistent 81-94% across all expiries — structural elevation, no kink. IV pct 89 | Sell 5/29 / buy 9/18 strangle (defined risk; tail risk binary) |
| **HD** | 5/15 33.8% → 5/22 38.6% → 9/18 31.8% — earnings kink at 5/22. IV rank 93. Earnings ~5/19. **Earnings-scout BUY VOL conflict with vol-surface SELL VOL** — half size, defined-risk only. | Earnings BUY VOL: long 5/22 ATM straddle. Calendar SELL: short 5/22 / long 7/17. **Choose ONE.** |

### Calendar long premium (cheap vega buys)

| Ticker | Why cheap | Trade |
|---|---|---|
| **PFE** | IV30 19.3%, percentile 0, **z=-4.28** historic low | Long 9/18 ATM straddle |
| **TLT** | IV pct 5, z=-1.06 — rates vol cheapest in a year | Long 9/18 ATM straddle |
| **MSTR** | IV pct 0, z=-2.45 — even at IV 64% it's at MSTR's lowest | Long 8/21 strangle |
| **UNH** | IV pct 0, z=-1.34 — earnings vol crushed | Long 9/18 ATM call (cum-prem -$156M is a caveat — VOL_LONG only, not directional) |

### Skew / tail-hedge note

Every back-month skew is COMPLACENT (calls priced ≥ puts at 25-delta) **except SOXL**. With VIX 17 ELEVATED, this is a divergence: front-month vol rich, tail hedging absent. Long-dated 25-delta puts on **TSLA (skew_ratio 0.867 most complacent), QCOM, MU, NVDA** are systematically underpriced vs calls — asymmetric tail-hedge candidates if regime turns.

---

## 6. Risk & Correlation

### Correlation clusters (corr > 0.7 = treat as one position)

| Cluster | Members | Evidence | Sizing implication |
|---|---|---|---|
| **China_Long** | KWEB, FXI | KWEB/FXI 0.931 | DROP both — institutional LONG flow vs short thesis |
| **Broad_Beta_Short** | SPY, IWM, C | SPY/IWM 0.917, SPY/C 0.817, C/IWM 0.734 | C-long competes with SPY/IWM-short → C cut to starter; IWM is primary short carrier |
| **SMH_Hedge** | SMH, SPY, IWM | SPY/SMH 0.819, IWM/SMH 0.792 | SMH stays starter hedge — don't double-up index shorts |
| **Analog_Semi** | ON, ADI | ON/ADI 0.77 | ADI primary, ON to starter |
| **AI_Mega_Pair** | NVDA, META | 0.735 | Intentional pair (NVDA long / META short) — feature not bug |
| **DP_Accumulation_Tech** | AAPL, QCOM, MSTR | Same dom class + Tech sector clustered | AAPL + QCOM full; MSTR cut to half |

### Gates fired (per ticker, see §7 audit trail for full stack)

- **Regime gate**: TSLA, MSTR, CORZ, SPY, KWEB, FXI (UPTREND breadth-poor squeeze risk OR fighting institutional flow)
- **VRP-vs-trade-type**: All vol_long candidates (NBIS, ADI, HD, DE, PFE, TLT) require defined-risk debit spreads (slightly negative VRP makes vega expensive)
- **Front-end IV panic gate**: 1.059 (NOT triggered, threshold 1.10) — within 5%, escalate hedge if it trips tomorrow
- **Sector gate**: ON not in faded memory (analog ≠ memory); MU short = crowded but valid
- **Cluster gate**: KWEB, GOOGL DROPPED; MSFT, AMD, AMZN dropped from confluence due to internal long-vs-short contradictions

### Adverse-flow exit list (existing rolling watchlist)

| Ticker | Adverse signal | Action |
|---|---|---|
| AMD | $203M DP + 184k OI but bearish flow -$19M, dropped from confluence | CUT or convert to defined-risk |
| SNDK | $475M DP, IV 73, P/C 1.10, -$36M flow bearish | CUT — bearish flow + expensive vol |
| STX | IV 79 + P/C 1.23 + -$4.9M flow | CUT — memory/storage rotation faded |
| AMZN | -$22.9M flow + accumulation/sweep contradiction | TRIM longs |
| HOOD | -$9.5M flow despite OI build | TRIM, monitor |
| RDDT | IV rank 9 (cheap) + -$2.4M flow | HOLD shares; CONSIDER cheap LEAP calls |
| FIS | IV 87 + 5.4x volume earnings vol | HOLD with caution; credit structures only |

### Hedge sleeve recommendation (3-4% notional)

| Leg | Instrument | Size | Rationale |
|---|---|---|---|
| Primary | IWM put debit spread, 21-30 DTE post-OPEX, 5-10% OTM, 10-pt width | 2-3% | Cleanest negative-GEX expression (13/15 sessions); defined risk caps decay |
| Secondary | SMH calendar — sell front-week put / buy June put 5% OTM | 0.5-1% | Only single-name with put-heavy DEX; defined risk |
| AVOID | Naked SPY puts | — | VRP fair → no edge selling; IV 14.75% not cheap to buy |
| AVOID | VIX calls | — | Already 17, vol-of-vol pricing the risk |

**Escalation trigger**: if SPY front-end IV ratio prints > 1.10 OR SPY confirms second NEGATIVE GEX session OR breadth drops < 30% — bump hedge to 6%+ and cut all naked-short premium.

---

## 7. High-Conviction Cross-Ref (score ≥ 5)

Per-ticker audit trail from `signal-confluence-quant`. Every signed point names source agent + tool. Risk-monitor's gate stack applied on top.

### LONGS

| # | Ticker | Raw | Direction | Components (points × source × tool) | Dom class | WR | Pre-risk | Gates fired | **Final** | Invalidation |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | **13** | LONG | +3 dealer-pos / dealer_delta_exposure (+27T DEX, ZGL 161 cushion); +2 gamma-flip / today_gamma_flip (PIN 290); +2 accumulation / dp_block_size_stratified (mega 87% buy, $499M DP); +2 accumulation / oi_trend (5/5 BUILDING); +2 quant / cumulative_premium_flow (+$428M 30d); +1 sweep / multi_day_sweep_persistence (today $56M Aug 320C ASK); +1 multileg / multileg_activity (295/320 long diagonal $128M) | dark_pool_accumulation | 90% | full | none | **FULL** | $276.83 multi-day DP floor / mega buy_ratio < 0.55 |
| 2 | **QCOM** | **12** | LONG | +2 accumulation / dp_block_size_stratified (mega 100% 8 prints); +2 accumulation / oi_trend (5/5 BUILDING); +2 quant / signal_confluence (score 5); +2 quant / cumulative_premium_flow (+$106M); +1 multileg / multileg_activity (term-anchored 6/19+7/17 ladder); +1 sector-rotation / sector_flow_persistence (Tech AI infra leader); +1 vol-surface / term_skew (KINKED 5/22 z=+3.14); +1 earnings / iv_term_structure (BUY VOL pre-earn) | dark_pool_accumulation | 90% | full | none | **FULL** | $192.57 reactivation level |
| 3 | **NVDA** | **11** | LONG | +3 dealer-pos / dealer_delta_exposure (+115T DEX, GEX 11T); +2 gamma-flip / today_gamma_flip (PIN 212.5); +2 accumulation+sweep / dp + sweeps; +1 sweep / multi_day_sweep_persistence; +1 multileg / multileg_activity (217.5/225 5/15 vertical $33M); +1 sector-rotation; +1 vol-surface / term_skew (KINKED 5/22); +1 earnings / iv_term_structure | gamma_breakout | 75% | full | none | **FULL** | DEX flips put-heavy / 200 ZGL band breaks |
| 4 | **MSTR** | **9** | LONG | +2 accumulation / dp (mega 100% 5 prints); +2 accumulation / oi_trend (5/5); +2 quant / signal_confluence (score 5); +2 quant / cumulative_premium_flow (+$272M); +1 vol-surface / iv_percentile_zscore (z=-2.45 cheap vega) | dark_pool_accumulation | 90% | full | regime (high-beta) + cluster (dp_accum dup) | **HALF** | $179.84 anchor break |
| 5 | **GOOG** | **9** | LONG | +2 accumulation / dp_block_size_stratified; +2 quant / signal_confluence (score 5); +2 quant / cumulative_premium_flow (+$322M); +2 accumulation / oi_trend (5/5 BUILDING via class share); +1 sector-rotation / sector_flow_persistence (Comm Svc) | bullish_flow | 75% | full | none | **FULL** | < 50d SMA / cum-prem flips |
| 6 | **CORZ** | **8** | LONG | +2 quant / signal_confluence (score 6); +2 accumulation / oi_trend; +1 sweep / multi_day_sweep_persistence (single-day 286x); +1 leap / biggest_oi_increases; +2 accumulation / smart_positioning | bullish_flow | 75-90% | full | regime (microcap, breadth-poor) → starter | **STARTER** | Single-day flow doesn't persist |
| 7 | **SHOP** | **8** | LONG | +2 accumulation / smart_positioning; +2 accumulation / oi_trend; +2 quant / cumulative_premium_flow (+$116M); +1 leap / biggest_oi_increases (9/18 LEAP-tier); +1 sector-rotation | leap_directional | 75% | full | regime (high-beta software) | **HALF** | DP turns DISTRIBUTION |
| 8 | **C** | **7** | LONG | +2 quant / cumulative_premium_flow (+$27M); +1 multileg / multileg_activity (135/145 vertical 52k); +2 accumulation / dp_block_size_stratified ($165M DP); +2 accumulation / oi_trend | multileg_directional | 75% | half | cluster (SPY/C 0.817) | **STARTER** | Below 132 by 5/12 |
| 9 | **TSLA** | **7** | LONG | +3 dealer-pos / dealer_delta_exposure (+69T DEX); +2 quant / cumulative_premium_flow (+$980M); +1 multileg / multileg_activity (5/8-5/22 diagonal); +1 sector-rotation | gamma_breakout | 75% | full | regime (high-beta breadth-poor) | **HALF** | Below 400 with no positive gamma support |
| 10 | **ORCL** | **6** | LONG | +1 sweep / multi_day_sweep_persistence (5/5 $677M); +3 dealer-pos / dealer_delta_exposure (+3.5T); +2 gamma-flip / today_gamma_flip (PIN 200) | multi_day_sweep | 75% | half | none | **HALF** | Sweep persistence breaks |
| 11 | **CODI** | **6** | LONG | +1 sweep / multi_day_sweep_persistence (LEAP whale 286x); +1 multileg / multileg_activity ($30M LEAP vertical); +2 quant / cumulative_premium_flow (+$36M, ratio 45:1); +2 leap / biggest_oi_increases | leap_directional | 75% | starter | none | **STARTER** | Below $10 by 7/17 |
| 12 | **ON** | **6** | LONG | +2 accumulation / dp_block_size_stratified (mega 96%, $331M +$0.74); +2 accumulation / oi_trend; +2 leap / biggest_oi_increases | dark_pool_accumulation | 90% | half | cluster (ADI dup) | **STARTER** | $102.67 multi-day pivot |
| 13 | **GOOGL** | **5** | LONG | (mostly duplicate exposure of GOOG; class-share split shows -$120M 30d flow divergence) | dark_pool_accumulation | 90% | starter | duplicate of GOOG | **SKIP** | n/a — trade GOOG |

### VOL LONG (cheap vega + KINK setups)

| Ticker | Raw | Components | Dom class | WR | **Final** |
|---|---|---|---|---|---|
| **NBIS** | 5 | +1 earnings / iv_term_structure; +1 vol-surface; +2 quant / cum-prem +$63M; +1 earnings / BUY_VOL | vol_kink_long | 75% | **HALF (defined-risk)** |
| **ADI** | 5 | +1 earnings / iv_term_structure (KINKED 5/22); +1 earnings / analyst_vs_flow; +1 vol-surface / term_skew; +2 quant / cum-prem +$11M | vol_kink_long | 75% | **HALF (defined-risk)** |
| **HD** | 4 | +1 earnings / iv_term_structure; +1 earnings / analyst_vs_flow; +1 sector-rotation; +1 vol-surface / iv_percentile (rank 93) | vol_kink_long | 75% | **HALF (defined-risk)** — earnings BUY VOL conflicts with vol-surface SELL VOL; pick one |
| **DE** | 3 | +1 earnings / iv_term; +1 vol-surface / term_skew; +1 earnings | vol_kink_long | 75% | **STARTER** |
| **PFE** | 3 | +1 vol-surface / iv_percentile_zscore (z=-4.28); +2 quant / signal_confluence (score 5) | vol_kink_long | 75% | **STARTER** |
| **TLT** | 3 | +1 vol-surface / iv_percentile (rates vol 12-mo low); +2 quant / signal_confluence (score 5) | vol_kink_long | 75% | **STARTER** |

### VOL SHORT

| Ticker | Raw | Components | **Final** |
|---|---|---|---|
| **MRVL** | 3 | +1 vol-surface / iv_term_structure (KINKED 5/29); +1 earnings / iv_term; +1 vol-surface / iv_percentile_zscore (pct=89) | **STARTER (defined-risk calendar only — no naked short straddles)** |

### SHORTS

| Ticker | Raw | Components | Dom class | WR | Pre-risk | Gates | **Final** | Invalidation |
|---|---|---|---|---|---|---|---|---|
| **SPY** | 5 | +3 dealer-pos / dealer_delta_exposure (FULLY_NEGATIVE GEX -434B regime FLIP); +1 sweep / multi_day_sweep_persistence (5/5 BEAR $7.2B); +1 multileg / multileg_activity (5/29 710/675 bear put $28.6M) | bearish_flow | 37.5% (dealer-flip override) | half | regime (dealer-flip fresh) | **STARTER** | Reclaim 736 / IV ratio drops < 1.04 |
| **META** | 4 | +1 sweep (BEAR 5/5 $893M); +1 multileg (deep-ITM puts $54M+ ASK); +2 quant / cumulative_premium_flow (-$562M) | multi_day_sweep | 37.5% | half | none | **HALF** | Reclaims $640 / 5 days |
| **MU** | 4 | +1 multileg (7/17 850P stacked $77M ASK); +1 sector-rotation (memory faded); +2 quant / cum-prem (-$384M) | multileg_directional | 37.5% | starter | sector (crowded short) | **STARTER** | Memory rotation flips |
| **IWM** | 4 | +3 dealer-pos / dealer_delta_exposure (FULLY_NEGATIVE 13/15); +2 quant / cum-prem (-$994M) | bearish_flow | 37.5% | half | none | **HALF** | Breadth > 40% / reclaim 286 |
| **SMH** | 3 | +3 dealer-pos / dealer_delta_exposure (only put-heavy DEX) | bearish_flow | 37.5% | starter | cluster (SPY/SMH 0.819) | **STARTER (hedge)** | DEX flips call-heavy |
| **KWEB** | 3 | (cluster duplicate of FXI) | bearish_flow | 37.5% | starter | cluster + regime | **DROPPED** | n/a |
| **FXI** | 3 | (institutional LONG flow today) | bearish_flow | 37.5% | starter | regime (fighting tape) | **DROPPED** | n/a |

### Conviction-scoring rubric (verbatim, for audit)

```
Daily conviction score = Σ:
  +3  dealer-positioning-strategist flags DEX flip or vanna-squeeze setup in trade direction
  +2  gamma-flip-tracker flags 0DTE breakout setup (regime flip + flow alignment)
  +2  3+ aligned signals in accumulation-hunter (DP institutional tier + OI + smart_positioning)
  +2  multi-day OI build (oi_trend BUILDING, lookback ≥ 5 days)
  +2  conviction_matrix = DIRECTIONAL_LONG, confidence > 70
  +2  cumulative_premium_flow shows net directional accretion in trade direction (30d window)
  +1  in sweep-tracker top 5 by multi_day_sweep_persistence count
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector (persistence ≥ 3)
  +1  in earnings-scout BUY VOL or SELL VOL
  +1  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only — N/A today)
  -2  contrarian-scanner flags as overcrowded long with rising pc_ratio_zscore (VRP positive)
  -1  risk-monitor flags in correlation cluster (corr > 0.7) — applied in 2b on top of raw score
  -3  market_regime conflicts with trade direction — applied in 2b
```

### Strategy disagreements (multileg vs batch_strategy_scan)

| Ticker | Multileg read | Batch scan read | Resolution |
|---|---|---|---|
| **NVDA** | bull vertical 217.5/225 5/15, 60k each leg | "No Clear Edge — Stay Flat" | **PREFER MULTILEG** — saw the actual coordinated 60k×60k vertical |
| **C** | bull vertical 135/145 5/15, 52k each leg | "Follow Smart Money — flow bearish" | **PREFER MULTILEG** — 52k×52k coordinated print is conviction signal |
| **META** | deep-ITM bear puts $54M+ ASK | "No Clear Edge" | **PREFER MULTILEG** — synthetic short structure observed |
| **ADI** | (no read) | "Bear Call Spread (DP_DISTRIBUTION)" | **PREFER EARNINGS-SCOUT BUY VOL** (kink at 5/22, analyst 75% bullish vs bearish flow) — vol play not directional |
| **ORCL** | (no detailed) | "No Clear Edge" | Sweep + dealer-pos LONG thesis stands |

---

## 8. Watch-only — single signal, no confluence

Names that surfaced from one Phase 1 agent but failed the confluence gate. NOT for trade entry today.

| Ticker | Signal source | Why excluded |
|---|---|---|
| **AMZN** | accumulation HIGH (mega 80%, $2.06B DP, 5/5 BUILDING, 1/27 C300 LEAP) | sweep BEAR 5/5 + sector SHORT contradicts |
| **MSFT** | sweep BEAR 5/5 ($943M) + accumulation DISTRIBUTION (mega 35%) | dealer-pos / multileg LONG contradicts |
| **AMD** | dealer-pos SHORT (gamma -88% 24h) + sector memory faded | multileg diagonal LONG roll-up + cum-prem +$167M bullish contradicts |
| **PLTR** | sweep BEAR 5/5 only | bullish_flow backtest 5/5 = +0.85% squeeze |
| **LLY** | accumulation HIGH (mega 98.8%, BUY/SELL 8.22) | sector-rotation flags SHORT (GLP-1 unwind) |
| **XOM** | accumulation HIGH (counter-trend) | sector-rotation flags SHORT (DVN preferred) |
| **DVN** | sweep single-day BULL + sector leader | only 2 signals, cum-prem +$4M flat |
| **CRWD** | sector-rotation cyber leader | cum-prem -$46M BEAR contradicts |
| **NOW** | sector-rotation tech leader | only 2 signals, cum-prem +$8M flat |
| **MRNA** | sector-rotation Healthcare leader | cum-prem -$56M BEAR contradicts |
| **NFLX** | sector-rotation Comm Svc leader | cum-prem -$95M BEAR contradicts |
| **AMAT** | earnings BUY VOL HIGH | accumulation flags DISTRIBUTION (mega 26.4%) |
| **GLD** | multileg HIGH put diagonal $46M | today $34M 7/17 400P SOLD = bullish reversal |
| **UNH** | vol-surface cheap vega (z=-1.34) | cum-prem -$156M BEARISH undermines long |
| **RDDT** | vol-surface cheap vega (IV pct=0 z=-1.88) | only 2 signals, cum-prem +$20M weak |
| **FUTU** | contrarian PCR z=+12.9; vol-surface KINKED 6/05 | mixed signal (extreme PCR + bearish flow + IV 86) — observe only |
| **FLNG** | contrarian medium (PCR z=+6.76, IV 88) | liquidity caveat |
| **DKNG** | leap-radar near-miss 5/9 gates | conviction 19.6% + IV rank 64 |
| **INDV** | $39.99M single mega print | confirmed SINGLE-BLOCK STUFFING (1 trade, mega buy_ratio 0.0, sell-side) — distribution not accumulation |
| **AMAT distribution** | mega 26.4% buy ratio | net-seller signature |

---

**Watchlist write-back confirmed**: `conviction_2026-05-07` = [AAPL, QCOM, NVDA, MSTR, GOOG]. Will feed tomorrow's correlation universe for adverse-flow alerts.
