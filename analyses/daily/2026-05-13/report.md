# Daily Market Analysis — 2026-05-13

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL UPTREND. SPY 742.31 (+6.89% 30d, −0.21% from 90d high) but breadth weak — only 37.1% bullish flow; SPY sitting *on* ZGL 739.29 (NEAR_FLIP) while QQQ trades 0.5% below its ZGL (TREND-negative) and IWM is FULLY_NEGATIVE — index gamma dispersion is the day's defining intraday tell. VIX 17.87, VRP 0.044 FAIR. Tech/Cons-Cyc/Comm-Svcs/Industrials/Healthcare inflow today; Financials/Utilities decelerating. Institutional collar locked: $2.4B SPXW 8100–8170 Dec-26 calls SOLD + $140M SPX 8000P SOLD = pin/range thesis, NOT directional short — but SPX/SPXW puts +$4.05B persistence is real hedge demand underneath the tape.
- **Top 0DTE play:** AAPL 295P/300P/300C/305C iron fly — highest GEX wall in the book (+$2.43T at 300, 0.91% from spot, OI 997K). Credit target 2.40–2.80. Exit Thursday EOD.
- **Top swing build:** **NVDA — full size**, conviction 9/15, win_rate 0.78 (gamma_breakout class), into 5/20 earnings. Dealer gamma stack 7.3x in 10 sessions, OI BUILDING 5/5, DP mega-tier 82% buy on $1.22B, 90d cumulative premium +$208M. Structure: bull put spread 215/210 Jun monthly (per batch_scan) or 230/240 call debit (per dealer-positioning). Invalidation: close < 215 or SPY breaks 735.
- **Top LEAP candidate:** **NONE qualified.** Closest miss IREN (multi-expiry call ladder Jan27/Jan28 110C +20K) but conviction matrix 4.5% rejects and 90d cumulative premium −$23.7M shows distribution not accumulation. TSLA LEAP layer is put-protective (Jan27 180P, Dec28 410P). Macro uptrend already pulled forward LEAP accretion — institutions front-ran.
- **Biggest risk:** Long-book delta skew +0.85 against an UPTREND that has institutional collars and $4B index hedges baked in underneath. **Hedge sleeve required:** SPY 735/720 put spread Jun monthly, 1 contract per $50k long notional. No correlation clusters cleared the 0.70 threshold (highest META/NVDA 0.666) — risk is regime-level, not single-name concentration.

---

## 1. Regime & Gamma State

**Risk Market Regime:** `TRANSITIONAL — Mixed signals, reduce position size, wait for clarity`. Trend UPTREND. SPY 742.31 above 20-SMA (720.03) and 50-SMA (687.62), +6.89% 30d, only −0.21% from 90d high. Breadth divergence: 2,281 bullish-flow tickers vs 3,869 bearish-flow tickers (37.1% bullish). Trading guidance: **half size, defined-risk structures**.

**Per-index 0–45d gamma table**

| Ticker | Spot | Zero-Gamma | Total GEX | Regime | Call Wall | Put Wall |
|---|---|---|---|---|---|---|
| SPY | 739.82 / 742.31* | 739.29 | +$1.37T (POS flip today) | NEAR_FLIP | 743 | 735 |
| QQQ | 711.19 | 714.98 | +$255B (intraday re-flip POS) | TREND (spot below ZGL) | 715 | 710 |
| IWM | 281.68 | none | −$36.2B FULLY_NEGATIVE | TREND (chase) | 283 | 280 |

*intraday vs EOD print discrepancy — both shown.

**Critical SPY context:** 10-day GEX time-series shows 9-of-10 sessions FULLY_NEGATIVE (regime: dealer-short-gamma — accelerate moves), then SLAMMED to POSITIVE +$1.37T today with ZGL pinned at spot. This is a swing-defining regime flip — dealer long-gamma compresses vol into OPEX and into post-OPEX week. Combined with SPX/SPXW collar overwrite (8100–8170C sold against 8000P sold = year-end pin between SPX 7400–8100), the macro is **grind-up into OPEX, then resolve**.

**DTE volume share:** 0DTE 29.3% / weeklies 30.9% / monthlies 23.9% / LEAPs 6.8%. Classification: BALANCED — not retail-dominated 0DTE explosion, but no institutional weighting either.

**VRP (SPY):** IV30 15.34% vs realised σ30 10.93% → VRP 4.41% FAIR. No premium-selling or premium-buying mandate.

**Data quality flag:** `options_flow_sector_flow_persistence` returned persistence_score=1 INFLOW uniformly across all 11 sectors today — field is uninformative. Sector rotation extracted manually from `net_flow_by_day` (see §2b). `oi_position_rolls` errored on parquet schema (ticker ASND cast failure) — gate #2 for LEAP screen not evaluable.

---

## 2. 0DTE / Intraday Plays

**Index plays:**

| Ticker | Regime | Structure | Entry | Invalidation | Thesis |
|---|---|---|---|---|---|
| SPY | NEAR_FLIP | iron fly 738P/740P/740C/743C (or 739/741 short straddle) | 740 | <736 or >743 | 0DTE GEX +$20.6T clustered as support walls 739–743; below 736 the 735P (vol 312K, IV 92%) becomes magnet and pin breaks |
| QQQ | TREND− | put debit spread 710/705 if loses 710.50 | 710 break | reclaim 712 | ZGL 714.98 acts as ceiling; below 710 wall unlocks short-gamma cascade |
| IWM | FULLY_NEG | chase breakouts ONLY, fade nothing | n/a | n/a | every strike short-gamma, hedging is pure accelerant |

**Single-name 0DTE / OPEX-2 pin book** (ranked by GEX-weighted distance × OI mass — opex-pin-strategist):

| Ticker | Spot | Pin | Dist% | OI mass | GEX@pin | Structure | Credit | Invalidation |
|---|---|---|---|---|---|---|---|---|
| **AAPL** | 297.30 | 300 | 0.91 | 996,852 | +$2.43T | iron fly 295P/300P/300C/305C | 2.40–2.80 | break 295 or 303 |
| **IBIT** | 45.03 | 45 | 0.27 | 753,098 | +$41.4B | short straddle 45 (or fly 44/45/45/46) | 0.55–0.70 | <44 or >46.20 |
| **NVDA** | 226.12 | 225 | 0.50 | 1,481,988 | −$1.1M (short-γ at strike) | iron CONDOR 220P/222.5P/227.5C/230C (NOT fly) | 0.90–1.10 | <222 or >230 |
| HYG | 79.92 | 79 | 1.14 | 3,539,351 | n/a (credit ETF) | BWB 78P/79P/80C | 0.10–0.15 debit | spread blowout |
| SLV | 79.69 | 80 | 0.39 | 721,073 | +$459K | iron fly 78P/80P/80C/82C | 0.95–1.10 | <78 or >81 |
| EEM | 67.22 | 67.5 | 0.42 | 475,388 | + | iron fly 66P/67.5P/67.5C/69C | 0.55–0.65 | <66.40 or >68.20 |

**Single-name 0DTE plays** (from gamma-flip-tracker):
- **NVDA 225/227.5 magnet** — POSITIVE 0DTE GEX +$8.0T, 495K vol on 227.5C (largest single contract in market). Sell 222.5/225 put spread OR buy 225/227.5 call vertical for grind-up. Invalidation 222.5.
- **TSLA 445/450/452.5 call fly** — 450C closed at $0.01 (burned), massive support wall +$2.85T GEX at 450. Pin expected. Invalidation 452.5.

**Sweep ledger — protective puts dominate** (sweep-tracker, persistence-first):

5-of-5 persistence (5-day): TSLA puts, MU puts, QQQ puts, SPXW puts, NVDA mixed, SPY puts, AMD mixed, IWM **CALLS (only bullish 5/5)**. Treat index put persistence as institutional hedge stack, NOT directional short. The single bullish-persistence name is IWM — small-cap catch-up vs the index-hedge defense.

**Whale tape (today only — non-persistence):** $2.4B SPXW 8100–8170 Dec-26 CALLS SOLD = institutional overwrite/collar program. $140M SPX 8000P Aug-21 SOLD = bullish premium harvest at 8000 floor. Combined: **institutional collar locked SPX 7400 floor / 8100–8170 ceiling through year-end**. SPX 6000 deep-ITM single-day sweeps are synthetic-stock plumbing, NOT directional.

**OPEX risk note:** OPEX is 2026-05-15 (Friday). Exit all pin structures Thursday EOD or Friday 11am — pin-breakdown risk into the final hour is asymmetric.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

`dealer-positioning-strategist` reads:

| Ticker | DEX state | 5d trajectory | Vanna/Charm | Regime flip? | Swing bias | Thesis |
|---|---|---|---|---|---|---|
| **SPY** | POSITIVE +$87T | improving (2.9x call dom.) | charm +$5.4B (weekend tailwind into OPEX) | **YES — 9-of-10 FULLY_NEG → POS today** | NEUTRAL-TO-LONG with chop | Major regime flip; dealers now long γ → vol compression into OPEX, then directional resolution post-5/16 |
| QQQ | POSITIVE +$30.6T | improving | call-heavy | WHIPSAW (3 flips in 6 sessions) | NEUTRAL — instability | Defer to gamma-flip-tracker; too unstable for swing |
| **IWM** | flat POS +$535B | balanced book | **VANNA-SQUEEZE FLAGGED** (only put-heavy net_vanna +6.87M on the tape) | toggled POS↔FULLY_NEG 4x | **LONG** (3wk) | Unique Karsan setup — falling VIX + put-heavy book → dealer short-put hedges roll OFF, forcing systematic stock buys |
| **NVDA** | +$127T (98% call) | gamma stack 7.3x in 10d | charm +$74B | NO — POS all 10 sessions | LONG | Controlled grind-up, NOT a squeeze. ZGL 109 sits $117 below spot = no flip risk for weeks. Structure: 30–45 DTE 230C or 225/240 debit |
| **AAPL** | +$44.3T (98% call) | improving | charm +$27.2B | NO | LONG | Confluence with watchlist alert; cleanest single-name long behind NVDA |
| TSLA | +$92.4T (call-heavy) | improving | charm +$22.4B | NO | LONG | But conflicts with sweep-tracker 5/5 bearish persistence — flagged in §3 |
| GOOGL | +$4.7T | call-dom | charm +$1.88B | NO | LONG (light) | Conflicts with 3/5 bearish sweep persistence |

**Pair-trade flag:** IWM long vs SPY short — IWM is the ONLY name in the universe with put-heavy dealer book + vanna tailwind, while SPY ZGL sits exactly on spot (binary on next session). Clean expression of dispersion thesis.

---

## 2b. Sector Rotation

**Rotation regime call:** *Growth + Healthcare + Cyclical co-rotation* (late-cycle risk-on barbell with Financials/Utilities funding). NOT a clean defensive→cyclical or growth→value template — Healthcare bid alongside cyclicals is unusual.

**Rotating IN (persistence ≥ 3d, from manual net_flow_by_day extraction):**

| Sector | 5d trend ($M) | Inst. share | Leaders |
|---|---|---|---|
| **Healthcare** | 151 → 236 → 281 → 413 → 422 (monotone +179%) | 91.8% institutional | **LLY, MDT, DHR, MRK, HUM, JNJ, ABBV, REGN, TMO** |
| **Industrials** | 150 → 453 → 824 → 497 → 472 (3x base, durable) | 99.2% non-0DTE | **LMT, BA, CAT, DE, FLR, UNP, PWR, ETN, LUNR** |
| **Cons Cyclical** | 1214 → 1885 → 1782 → 1272 → 2150 (5d peak today) | 78.5% non-0DTE | **TSLA, BABA, JD, RCL, MBLY, F, MELI, BOOT, PDD** |
| **Comm Services** | 797 → 893 → 751 → 564 → **1239 (record)** | 59.8% inst. (XLC BALANCED) | GOOGL, META, NBIS, GOOG, BIDU, LUMN, ASTS — *tactical add, not pure rotation* |

**Rotating OUT:**

| Sector | 5d trend ($M) | Read |
|---|---|---|
| Financial Services | 418 → 458 → 641 → 286 → 220 | Half of 5/11 peak — value/rate-cycle thesis breaking |
| Utilities | 110 → 71 → 93 → 64 → 42 | Monotone decay — defensive-yield bid leaving despite breadth weakness (risk-on tell) |
| Basic Materials | 158 → 177 → 143 → 116 → 123 | Stagnant — losing share |

**Swing book implication:** LONG Healthcare (LLY/MDT/MRK/HUM) and Industrials (CAT/DE/FLR/LMT) leaders. ADD Cons Cyclical China (JD/BABA/BOOT) sized smaller — TSLA-skew risk. FADE / short-vol Financials (KRE in §3 with caveat) and Utilities. Comm Services (GOOGL/META) is growth-tactical add only — XLC mix is balanced not institutional.

**Invalidation:** Healthcare net flow < $200M for 2 sessions OR XLV institutional share < 70% (LEAP rotation breaks). Industrials < $250M for 2 sessions. Financials re-accelerating > $500M flips the OUT leg.

---

## 3. Swing Setups (1–6 weeks)

### 3a. Long swings (regime-aligned)

| Tier | Ticker | Score | Thesis | Structure | Invalidation | Win-rate | Sizing |
|---|---|---|---|---|---|---|---|
| **HIGH** | **NVDA** | 9 | Gamma stack 7.3x in 10d (dealer long-γ controlled grind-up). DP mega 82% buy on $1.22B. OI BUILDING 5/5 (+1.75M contracts). OPEX-2 pin at 225 with 0DTE 227.5C carrying 495K vol. Earnings 5/20 (1 week). | Bull put spread 215/210 Jun monthly OR 225/240 call debit. Defined risk both legs. | Close < 215 OR SPY breaks 735 OR DEX flip | 0.78 (bullish_flow) | **FULL** |
| **HIGH** | **AAPL** | 7 | Charm +$27B + 98% call DEX. OPEX 300C wall +$2.43T (biggest in book). 90d cumulative premium +$436M. Watchlist alert: $713M DP block + 122K OI shift. | 295/305 call debit Jun OR 0DTE iron fly 295P/300P/300C/305C for OPEX harvest. | Close < 290 OR DEX flip | 0.78 | **FULL with caution flag** — day-tape bearish (−$1.58M), multileg ratio 0.53 (mixed), batch_scan says "No Clear Edge — Stay Flat". Per Step 6.5 multileg precedence wins, but size FULL only on the OPEX pin structure; downgrade swing call debit to HALF. |
| MED | META | 6 | DP mega 93% buy (buy/sell 1.74, highest on tape). OI BUILDING 5d (+424K). Sector-rotation Comm Services leader. | Starter long calls 620/640 Jun OR aggressive long calls (per batch_scan). | Flow stays −$574M-trajectory for 2 sessions | null (DP_accum no historical sample) | **STARTER** — flow_conflict −2 (90d cum_premium −$574M strongly contradicts DP signal). DP/macro narrative survives but quantitatively unsupported. |
| MED | LUMN | 6 | Bullish risk-reversal multileg (SELL 8P / BUY 11C Jun). Confluence score 6 (max stack: bullish_flow + low_pcr + vol_spike + DP + OI + cheap_IV). 96% ask smart money on sweeps. | Replicate risk-reversal: SELL 8P / BUY 11C Jun (note: short put is uncapped downside, only for accounts with margin clearance). | LUMN < 8 by 6/18 OR short put gets bought back | 0.78 | **HALF** — Step 3a LB-tool gate failed (0/4). |
| MED | SHOP | 5 | Call condor 140/160/175/195 Sep ($35M coordinated), 99.6% ask whale, 90d cum_premium +$100M. | Long call condor 140/160/175/195 9/18 (max profit 160–175). | Fails to clear 140 by July OR back-IV crash | 0.78 | **HALF** — *flag: batch_scan says BEARISH FLOW today; multileg precedence (term-structure-anchored)* wins. |
| MED | JD | 5 | Cons Cyclical rotation leader. Confluence 5 (bullish_flow + low_pcr + vol_spike + DP + OI). 5.3x volume ratio + 3.75x premium ratio. China consumer pair with BABA/BIDU. | 30 DTE 35/40 call debit. | KWEB flow flips bearish | 0.78 | **HALF** |
| MED | BOOT | 5 | Cons Cyclical leader. Confluence 5. IV rank 79.4 + 0.029 PCR (call-dominated). 20.15x volume ratio = aggressive crowd. | Bull put spread (per batch_scan — IV elevated so credit). | Cons Cyclical persistence flips OR IV rank > 90 (entry premium evaporates) | 0.78 | **HALF** — late-entry risk on 20x vol ratio. |
| MED | FLR | 5 | Industrials leader. Confluence 6 (bullish_flow + low_pcr + vol_spike + DP + OI + low_iv = highest stack). E&C nuclear/data-center capex proxy. 3.5x bull/bear premium. | 30 DTE 45/50 call debit. | Prints below 90d MA | 0.78 | **STARTER** — flow_conflict (90d cum_premium −$4M small but contradicts) + Step 3a LB-tool gate failed. |

### 3b. Short / fade swings (defined risk only)

**`contrarian-scanner` returned ZERO clean fades today.** All IV-rich crowded names (CSCO, MRVL, DLTR, ROST) are in BACKWARDATION into known earnings catalysts — that's event vol, not crowding. Top-bullish mega-caps (TSLA/NVDA/META) show aligned flow and price, no statistical divergence ≥2σ.

**Re-engage when:** VRP turns positive-rich, OR a top-bullish name posts P/C z > +2σ with price/flow divergence, OR post-earnings IV crush leaves CONTANGO + lingering crowded positioning.

**Notable disqualifications carried forward:**
- **TSLA** — score 3, **SKIP**. Dealer-positioning LONG bias, but sweep-tracker 5/5 BEARISH persistence ($10.7B cumulative over 5 sessions) overrides. Likely macro hedge on a high-beta long book.
- **GOOGL** — score 4, STARTER only. Sweep-tracker 3/5 bearish + 90d cum_premium −$87M conflicts with dealer-positioning DEX long.
- **IWM** — score 4, STARTER. Unique vanna-squeeze flag but 90d cum_premium −$1.03B contradicts. Best expressed as PAIR (long IWM vs short SPY).

---

## 4. LEAP Builds (6–24 months)

**Zero LEAP-grade candidates pass the 6-of-9 signal gate today.**

| Near-miss | Disqualifier |
|---|---|
| IREN | LEAP OI stack (Jan27 110C +10K, Jan28 110C +6K, Dec26 110C +3K) is real, OI BUILDING 10/10. **But** 90d cum_premium −$23.7M (calls 73K bid vs 57K — sellers of upside, not buyers). conviction_matrix MIXED 4.5%. |
| NVDA | OI +384K headline is overwhelmingly 0DTE/weekly (NVDA260513C00225000 +22K dominates). Only NVDA261016C00280000 +6.6K qualifies as DTE>180 — too small. Cum_premium 90d +$208M but MIXED (1% net edge on $30B churn). Conviction matrix MIXED 7.98%. |
| TSLA | LEAP OI dominated by PUT side: Jan27 180P (+1.1K), Dec28 410P (+901), Jan28 100P (+694). Largest LEAP build is bearish protection. |
| GOOGL | Top LEAP only +848 contracts (Jan28 610C). Cum_premium 90d −$86.8M NEGATIVE. Conviction 4.71%. |

**Macro read:** SPY +6.89% 30d has already pulled forward LEAP accretion — institutions front-ran the rally rather than slow-accumulating now. Re-engage when MIXED 90d flow on a bullish leader flips net-positive AND conviction matrix returns DIRECTIONAL_LONG conf > 70.

**Watchable for next session:** IREN — if conviction matrix flips DIRECTIONAL_LONG AND 30d premium flow turns net-positive, becomes tier-1.

---

## 5. Volatility Surface

**Entire IV100 slate is May/June earnings-driven BACKWARDATION.** No idiosyncratic vol dislocations. NVDA is the only CONTANGO on the list — dealers willing to write back-month gamma (supports controlled grind-up thesis).

**Calendar candidates (BUY VOL via term-structure normalization):**

| Ticker | Earnings | Front IV | Back IV | F/B ratio | Structure | Notes |
|---|---|---|---|---|---|---|
| **AMAT** | 2026-05-14 (1 DTE) | 186% | 60% | 3.10 | Short 5/15 ATM straddle, long 6/18 ATM straddle | Biggest absolute spread on the board; implied move 6.55% |
| **CIEN** | June | 146% | 92% | 1.59 | Double calendar — short 5/15+5/22 straddles, long 6/05 straddle | Highest z-score on slate (+2.03); cleanest kink |
| **HPQ** | 2026-05-15 binary | 282% | 47% | 5.99 | Calendar 5/15-6/18 ATM | Most extreme front; size LIGHT, hand to earnings-scout |
| **GTLB** | early June | 165% | 71% | 2.34 | Calendar (NOT recommended today) | F/B 2.18 = extreme front per earnings-scout disqualifier; SKIP until front cools |
| **CSCO** | 2026-05-13 (today) | 148% | 38% | 3.89 | Post-print calendar 5/22-6/18 | Already in print; trade is post-print crush |
| **MRVL** | 2026-05-27 | 120% | 78% | 1.54 | Calendar 5/29-6/18 ATM | FLOW_BULLISH +$13.7M, +23K OI build (tier-1 setup) |
| **BIDU** | 2026-05-18 | 108% | 78% | 1.20 | Calendar 5/22-6/18 at 150 strike | 90d cum_premium +$39M bullish kicker |
| **DE** | 2026-05-21 | 88% | 46% | 1.70 | Calendar 5/22-6/18 at 580 strike | Industrials rotation tailwind |
| **TTWO** | 2026-05-21 | 67% | 47% | 1.42 | Short 5/22 strangle 215P/240C **HALF SIZE** | NORMAL skew supports SELL VOL at half size |

**Sell vol (the rare clean candidate):**

| Ticker | Earnings | Why | Structure |
|---|---|---|---|
| **ADI** | 2026-05-20 | ONLY name with TAIL_HEDGING back-month skew (+0.073) — tail IS priced. Implied move 2.23% within range. Front 1.27 elevated but ADI is low-beta mega-cap analog. | Short 5/22 iron condor 410/420/445/455 — **HALF SIZE** |

**Buy vol via divergence (highest-EV non-earnings setup):**

| Ticker | Earnings | Why | Structure |
|---|---|---|---|
| **HD** | 2026-05-19 | Implied move only 1.91% — *cheap* for consumer-cyclical print into TRANSITIONAL regime. FLOW_BEARISH (−$1.1M) vs analyst BULLISH consensus = 2σ divergence. COMPLACENT skew (tail not priced) supports BUY VOL. | Long 5/22 ATM straddle at 302.5 — **QUARTER SIZE** |

**SPY VRP FAIR (0.044)** = no broad mandate to sell or buy vol. Per-name calendar plays are the cleanest expression. Sell-vol bias holds only where front IV is event-priced AND back IV is normal-regime.

---

## 6. Risk & Correlation

**Correlation clusters:** *None above the 0.70 hard threshold.* Highest pair META/NVDA at 0.666 (moderate). Soft-watch cyclical/small-cap cluster (IWM/KRE/DE/BOOT corr 0.50–0.65) — informational only, all already MED/starter so no demotions fire.

**Regime conflicts:** None — all candidates are long in a TRANSITIONAL UPTREND. Short-the-rally would be regime-conflict, no short-the-rally calls today.

**VRP / panic gates:** FAIR (0.044) → no-op for everything. Long-vol earnings plays NOT penalised (FAIR is not negative-VRP); short-vol setups NOT rewarded (FAIR is not positive-VRP). Front-end IV ratio panic gate: VIX 17.87 = no broad panic.

**Adverse sector rotation:** None fire — `options_flow_sector_flow_persistence` returned uniform persistence_score=1 INFLOW (broken signal). Step 0's qualitative "Financials/Utilities decelerating" stands as a soft caveat but does not gate KRE (which carries its own flow_conflict already).

**Hedge sleeve recommendation:**
- **Trigger:** Long-book delta skew ≈ +0.85 exceeds 0.6 threshold; Step 0 flagged $4B SPX/SPXW institutional put bid.
- **Structure:** SPY 735/720 put spread Jun monthly, 1 contract per $50k notional long-delta. Net delta target ≈ −0.3 of long book.
- **Why not VIX calls:** VRP FAIR — no edge buying vol. Put spread cheaper than naked puts given front-IV not in panic.
- **Alternative:** VIX 20/25 call spread Jun — inferior risk/reward at FAIR VRP today.

**Adverse-flow exit candidates from watchlist scan:**
- **AMD** flagged bearish day-tape (−$2.36M) — *exit any AMD long carried from prior session.*
- **AAPL** flagged bearish day-tape (−$1.58M) but $713M DP block + 122K OI shift override → **monitor, do not exit**.
- **URI** P/C 4.75 (heavy puts) + $37M DP — adverse-flag for any prior URI long (no URI long opened today).

**Data quality issues to surface:**
1. `options_flow_sector_flow_persistence` persistence_score=1 INFLOW uniformly for all 11 sectors — the field's discrimination is broken. Manual extraction from `net_flow_by_day` performed throughout.
2. `oi_position_rolls` parquet schema cast error (ticker ASND) — LEAP gate #2 (forward-roll detection) not evaluable.

---

## 7. High-Conviction Cross-Ref (score ≥ 5, all gates applied)

| Ticker | Raw | Signal class | Win-rate | Score components | LB-gate | Risk gates | Final size | Invalidation |
|---|---|---|---|---|---|---|---|---|
| **NVDA** | 9 | gamma_breakout | 0.78 | +3 dealer-positioning DEX/gex flip · +2 accumulation dark_pool_block_stratified (mega 82% institutional-tier) · +1 historical_oi_trend BUILDING 5d · +2 insights_signal_confluence DIRECTIONAL_LONG · +2 historical_cumulative_premium_flow +$208M · +1 opex-pin top-5 | **PASS 3/4** (DP_block_strat + cum_premium + DEX) | regime/VRP/panic/cluster/sector all no-op | **FULL** | <215 or SPY <735 or DEX flip |
| **AAPL** | 7 | vanna_squeeze | 0.78 | +3 dealer-positioning vanna_charm · +1 opex-pin (300 GEX wall) · +2 insights_signal_confluence · +2 historical_cumulative_premium_flow +$436M · DP accumulation 45% mixed (no points; conflict noted) | **PASS 2/4** (DEX + cum_premium) | day-tape bearish OVERRIDDEN by DP block + OI shift; multileg ratio 0.53 caveat | **FULL on pin / HALF on swing** | <290 or DEX flip |
| **META** | 6 | dark_pool_accumulation | null | +2 accumulation dark_pool_block_stratified (mega 93% buy_ratio 1.74) · +1 historical_oi_trend BUILDING · +1 sector-rotation Comm Services · +2 confluence · +2 dealer-positioning charm · **−2 flow_conflict** (90d cum_premium −$574M) | **FAIL 1/4** (cum_premium CONTRADICTS) → DEMOTE MED | flow_conflict already in raw | **STARTER** | flow stays negative 2 sessions |
| **LUMN** | 6 | multileg_directional | 0.78 | +2 multileg bullish risk-reversal · +1 sweep 96% ask · +2 confluence score 6 (max stack) · +1 OI BUILDING | **FAIL 0/4** → DEMOTE MED | no gates fire | **HALF** | <8 by 6/18 or short put bought back |
| **SHOP** | 5 | multileg_directional | 0.78 | +2 multileg call condor $35M term-anchored · +1 sweep 99.6% ask · +2 historical_cum_premium +$100M | **FAIL 1/4** → DEMOTE MED | batch_scan disagreement noted (multileg precedence) | **HALF** | fails to clear 140 by July |
| **FLR** | 5 | bullish_flow | 0.78 | +1 sector-rotation Industrials · +2 confluence score 6 · +2 accumulation DP+OI · +2 vol-spike net long · **−2 flow_conflict** | **FAIL 0/4** | flow_conflict already in raw | **STARTER** | prints below 90d MA |
| **JD** | 5 | bullish_flow | 0.78 | +1 sector-rotation Cons Cyclical · +2 confluence score 5 · +2 DP+OI from confluence | **FAIL 0/4** → DEMOTE MED | no gates fire | **HALF** | KWEB flow flips bearish |
| **BOOT** | 5 | bullish_flow | 0.78 | +1 sector-rotation Cons Cyclical · +2 confluence score 5 · +2 cum_premium +$1.7M | **FAIL 1/4** → DEMOTE MED | 20x vol ratio = late-entry caution | **HALF** | Cons Cyclical persistence flips |

### Scoring rubric (Step 4, applied verbatim — 2026-05-09 calibration)

```
+3  dealer-positioning DEX flip or vanna-squeeze in trade direction
+2  3+ aligned accumulation-hunter signals (DP + OI + smart_positioning + dark_pool_block_stratified institutional-tier)
+1  multi-day OI build (historical_oi_trend BUILDING ≥5d)              # was +2, reduced
+2  insights_conviction_matrix DIRECTIONAL_LONG conf>70
+2  historical_cumulative_premium_flow 30d net directional accretion
+1  sweep-tracker top 5 by hot_chains_sweep_persistence count
+1  sector-rotation names ticker as leader (persistence ≥ 3)
+1  earnings-scout BUY VOL or SELL VOL
+2  multileg-strategist directional structure (term-structure-anchored)  # promoted from +1
+1  vol-surface-scout KINKED/BACKWARDATION + VRP-aligned bias
+1  opex-pin-strategist top-5 (OPEX week only)
−2  contrarian flags overcrowded long with rising P/C z (VRP positive)
−2  flow_conflict (cum_premium_flow contradicts dominant_signal_class)  # NEW
−1  correlation cluster (risk-monitor 2b)
−3  regime conflict (risk-monitor 2b)

Step 3a HIGH-tier load-bearing gate (raw ≥5 must cite ≥2 of):
  dark_pool_block_stratified, historical_cumulative_premium_flow,
  insights_institutional_accumulation, options_structure_dex
```

---

## 8. Watch-only — single signal, no confluence

For journaling, NOT for trade entry today:

- **HUM, MRK, JNJ, ABBV, REGN, TMO, LMT, BA, CAT, UNP, PWR, ETN, LUNR, DHR** — sector-rotation leaders (Healthcare/Industrials) but no DP/OI/multileg/dealer-positioning confluence today. Below raw_score 3 floor.
- **BABA, MELI, RCL, MBLY, F, PDD** — Cons Cyclical leaders, single sector signal.
- **KRE** — score 3, regional banks diagonal $31M from multileg + 99.9% ask whale, BUT 90d cum_premium −$14.5M and KRE on bearish confluence top-30 → flow_conflict pulls to LOW tier starter.
- **RKLB, CRWV** — sweep persistence 3/5 bullish ($588M / $349M), confluence ≥5 (CRWV macro) but no DP/dealer/multileg confluence.
- **NOK, F, KRE call, SHOP call** — today-only smart-money 96–99.9% ask sweeps confirmed but lacking 3-5 day persistence.
- **AMD** — watchlist alert ($280M DP + IV 86 + OI build) but mega tier only 92% buy with weak buy/sell 1.29 — gates to *supporting* not *high-conviction* per accumulation-hunter; flagged adverse-flow today (−$2.36M).
- **NBIS, AVGO** — DP institutional builds, OI BUILDING, but mixed mega-tier (NBIS mega buy 0.70 vs block 0.46; AVGO mega flat). Secondary signals.
- **GTLB** — IV rank 100, watchlist DP+OI, but front-IV ratio 2.18 = extreme front panic disqualifier per earnings-scout. SKIP until front cools.

---

## Watchlist write-back

`mcp__uw-pp__watchlist_manage(action="add", group="conviction_2026-05-13", tickers=[NVDA, AAPL, META, LUMN, SHOP])` — **confirmed by risk-monitor**. Top-5 selection: 2 HIGH (NVDA, AAPL by raw_score) + top 3 MED by Step 3a LB-tool citation count (META 1/4, SHOP 1/4, LUMN 0/4 — but LUMN selected over FLR/JD/BOOT for raw_score 6 vs 5). Tomorrow's watchlist_alerts will measure these against today's calls.
