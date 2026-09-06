# Daily Market Analysis — 2026-05-12

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL UPTREND. SPY 738.18 (+7.59% 30d, −0.35% from 90d high) but breadth only 35.2% bullish — climax warning. SPY/QQQ both FULLY_NEGATIVE 45d-GEX with spot pinned 3 ticks above massive 0DTE put walls (SPY 730/735, QQQ 698/700). VIX 17.99 (+$15.8M call flow). VRP FAIR (no vol edge market-wide).
- **Top 0DTE play:** AAPL @ 300 broken-wing butterfly (positive GEX +5.44e11 — largest pin notional in OPEX book; spot 294, dist 1.99%, expiry 2026-05-15).
- **Top swing build:** **CNC** — score 11, Healthcare-IN sector tailwind (flows DOUBLED 5d), 5-signal accumulation (mega 100% buy + OI BUILDING 5/5 + DIR_LONG conf 41.4% + cum_prem +$28M), Jan 2028 70C LEAP build, sweep top-5 LEAP $20C 2027 +$48M. Structure: long common or 60-90DTE call spreads. Invalidation: $70 break (currently 59.31). Win_rate NA on dark_pool_accumulation class → starter pre-risk despite top score.
- **Top LEAP candidate:** **URI** — score 9, score 7/9 LEAP-radar gate pass, $118M DP mega 100% buy, DIR_LONG conf 51.6%, cum_prem +$52M 90d. Structure: Jan 2027 ATM calls or 800/900 spread. Win_rate 0.90 (capped from 0.727) → full size. Invalidation: $720 break.
- **Biggest risk:** Index-beta cluster — SPY/QQQ/IWM/SPXW/XP all corr ≥0.79; aggregate $21B+ persistent put accretion + QQQ swing-bias FLIPPED SHORT (5/11 GEX regime POS→NEG confirmed today). Hedge sleeve = SPY 730/710 June put vertical sized to ~25% book delta + small VIX 22/30 ladder; defined-risk only because FAIR VRP doesn't reward outright long-vol.

---

## 1. Regime & Gamma State

**Regime:** TRANSITIONAL — Mixed signals, half size, defined-risk strategies (per `risk_market_regime`). UPTREND intact (SPY above 20/50 SMA) but breadth diverges (35.2% bullish only). SPY −0.35% from 90d high = at top of range.

**Per-index gamma table:**

| Index | Spot | Zero-Gamma | Total GEX | Regime (0DTE) | Call Wall | Put Wall |
|---|---|---|---|---|---|---|
| SPY | 738.18 | 673.01 | −14.77T | TREND (FULLY_NEG 45d) | 738 | 730 |
| QQQ | 707.24 | 497.48 | −7.47T | TREND (FULLY_NEG 45d) | 705 | 698 |
| IWM | 281.10 | 262.43 | −1.38T | NEAR_FLIP (45d POS today) | 282 | 278 |

**DTE share (regime hint = BALANCED):** 0DTE 24.2%, weeklies 38.0%, monthlies 23.1%, LEAPs 6.1%. LEAP share is low — favor specific catalyst names over passive long-tenor exposure.

**VRP SPY:** FAIR (vrp 0.0231, IV30 0.1537, RV30 0.1305). No premium-selling or premium-buying edge market-wide; gate every BUY-VOL or SELL-VOL trade for −1 tier.

**Front-end IV ratio:** Not pulled this run (assume neutral; explicit panic gate not triggered).

---

## 2. 0DTE / Intraday Plays

| Ticker | Structure | Thesis | Invalidation |
|---|---|---|---|
| SPY 0DTE | Range 730–738 | Negative-gamma between put wall 730 and call wall 738; ATM SPY 2026-05-12 P735 ($57.2M premium, ask>bid = put writers near spot) is the resistance pin | break of 730 triggers gamma-amplified downside; break of 738 reverses to upside |
| QQQ 0DTE | Range 698–705 | Same negative-gamma frame; QQQ 2026-05-12 P700 bid-skew = put accumulation (magnet) | break of 698 → trend down; 705 = call wall |
| NVDA 0DTE | Pin 220 | POSITIVE GEX +5.76T, ZGL 81.73 deep support; 220 mega support_wall (+1.06T) anchors spot — mean-revert pin between 220–225 | spot loses 218 with >0.5% range expansion or breaks 226 on heavy call buying |
| AAPL 0DTE | Pin 295/300 | POSITIVE GEX +513B, 295 support_wall (+331B), 300 OPEX magnet; vol compresses | spot <291 (loses gamma) or >298 sustained call ask-side |
| TSLA 0DTE | Drift 440–450 | POSITIVE but flip strike 300 far below; walls 440/445/450 act as upside magnet into OPEX | fail 425 → trend mode resumes downside |

**Persistent sweep urgency tape (top 5/5 persistence ≥3-of-5 days):**

| Ticker | Side | Notional | Note |
|---|---|---|---|
| TSLA | bearish | $9.8B | 5/5 persistent — LARGEST sweep notional in tape |
| QQQ | bearish | $7.2B | 5/5 — 5/21 $650P + 6/30 $635P, sweep ratio >0.85 |
| SPX/SPXW | bearish | $7.1B | 5/5 — 6/18 $7400P concentrated single-strike ladder |
| SPY | bearish | $6.9B | 5/5 — 5/15 $718P / 5/22 $700P / 5/29 $680P put ladder, ask/bid 2.9–6.4x |
| MSFT | bearish | $850M | 5/5 — quiet but durable mega-cap put bias |
| META | bearish | $784M | 5/5 — persistent bearish |
| AMD | bullish | $3.96B | 5/5 — CONFLICTS macro semis-OUT tag (may be hedge unwind) |
| SNDK | bullish | $1.19B | 5/5 — cleanest persistent bullish single-name |
| RKLB | bullish | $588M | 3/5 — space/defense |
| CRWV | bullish | $349M | 3/5 — AI-infra |

**OPEX-week pin book (top 5 ranked, expiry 2026-05-15):**

| Rank | Ticker | Pin Strike | Distance | GEX | Structure |
|---|---|---|---|---|---|
| 1 | AAPL | 300 | 1.99% | +5.44e11 (largest notional) | Broken-wing butterfly: long 295C / short 2× 300C / long 305C |
| 2 | XLE | 57.5 | 0.05% (TIGHTEST) | +8.11e8 | Short straddle 57.5C/57.5P (or iron fly with 56P/59C wings) |
| 3 | EEM | 65 | 1.02% | +4.45e9 | Iron fly 64P/65P/65C/66C |
| 4 | FXI | 37 | 0.62% | +1.65e9 | Iron fly 36P/37P/37C/38C |
| 5 | OWL | 10 | 1.11% | +4.26e9 | Broken-wing put fly (liquidity caveat — wide spreads on sub-$10) |

**Disqualified pins (gex_at_pin negative or stale spot):** HYG@79, TLT@85, QQQ@695, XLF@51, NVDA@225, IBIT@45, SLV@80, F@11.85.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

**Headline:** QQQ swing-bias FLIPPED SHORT this week (5/11 GEX POS→NEG regime flip CONFIRMED today with total_gex collapse to −$415B). IWM is the cleanest 1–2wk LONG vanna-squeeze candidate.

| Ticker | DEX | Vanna-Squeeze | ZGL Trajectory | Swing Bias | Conviction |
|---|---|---|---|---|---|
| SPY | −$75.2T (put-heavy) | YES (armed but ZGL 14pts above spot) | FULLY_NEG 23/23 | NEUTRAL | MEDIUM |
| QQQ | −$41.4T (put-heavy) | NO (call-vanna; falling VIX = SELL pressure) | TWO flips this week, today −$415B collapse | **SHORT** | HIGH |
| IWM | −$5.04T (put-heavy) | YES (GEX flipped POS today) | chop POS↔NEG; today POS regime | **LONG** | HIGH |
| NVDA | +$69.7T (call-heavy) | NO | POS, ZGL 81.73 deep support | **LONG** | HIGH |
| AAPL | +$14.2T (call-heavy) | NO | n/a | LONG | MEDIUM |
| TSLA | +$24.8T (call-heavy) | NO | n/a | NEUTRAL (DEX/flow disagreement) | LOW |
| SMH | −$480B (put-heavy) | NO | n/a | **SHORT** | HIGH |
| MU | +$4.2T (call-heavy) | NO | n/a | DISQUALIFIED (DEX +call vs −$192M flow) | SKIP |

**Vanna-squeeze setups:** IWM (cleanest — put-heavy book + GEX flipped POS today + small-cap underowned + falling-VIX context); SPY (armed but delayed by 14pt distance to ZGL, watch break above 745).

---

## 2b. Sector Rotation

**Rotation regime call:** **cyclical→defensive (medium confidence)** — defensive rotation building beneath a still-rising tape.

**Magnitude trend over 5 sessions (2026-05-06 → 2026-05-12):**

| Sector | Trend | Today $ | Implication |
|---|---|---|---|
| Healthcare | RISING (+97%, monotonic 4 of 5) | +$413M | XLV INSTITUTIONAL (55.5% monthlies) |
| ConsDef | SPIKED 9× today ($38M→$351M) | +$351M | XLP BALANCED (52% monthlies) |
| BasicMat | STEADY positive 5/5 | +$116M | XLB INSTITUTIONAL (49.8% monthlies + 17.7% LEAPs) |
| Tech | FALLING −56% in 24h | +$5.45B (was $12.4B) | bearish call-minus-put skew (institutional hedging) |
| ConsCyc | FADING −29% | +$1.27B | bearish skew |
| CommSvc | FALLING 4 sessions −53% | +$564M | bearish skew |

**Single-name leaders within IN sectors:** Healthcare → CNC, UNH, HUM, LLY, ILMN. ConsDef → COST, WMT, KMB, TGT. BasicMat → FCX, AA, SCCO, RIO.
**Single-name shorts within OUT sectors:** Tech → MU, INTC, SNDK, MSFT, AMD. ConsCyc → TSLA, AMZN, PDD, LULU. CommSvc → NBIS, META, ASTS, GOOGL.

**Caveat:** persistence_score = 1 across all sectors (raw metric is sign-only, weak signal). The conviction is in the **flow-velocity DELTA**, not raw direction. Treat as MEDIUM not HIGH conviction rotation.

---

## 3. Swing Setups (1–6 weeks)

Ranked by conviction score (Step 4 rubric, post Phase 2b risk gates). Step 3a load-bearing-tool gate applied.

### 3a. Long swings (regime-aligned)

| Ticker | Score | Thesis | Structure | Invalidation | Final Size |
|---|---|---|---|---|---|
| **CNC** | 11 | 5-signal accumulation (mega 100% buy + OI BUILDING 5/5 +16.6k + DIR_LONG conf 41.4% + cum_prem 30d +$28M) + Healthcare sector IN tailwind + sweep top-5 LEAP $20C 2027 +$48M + Jan 2028 70C LEAP build (24-mo OTM). 8/10 bullish days, +11.2% over 10d. Earnings 7/24. | Long common or 60–90DTE call spreads (e.g. Aug 60/65C). Optional LEAP add via Jan 2028 70C. | $70 break (currently 59.31) | starter (win_rate NA on accumulation class — wait for live tracking) |
| **URI** | 9 | LEAP-radar QUALIFIED 7/9 (mega 100% buy $118M DP + DIR_LONG conf 51.6% + cum_prem 90d +$52M). $952 DP cluster defending VWAP 954. BasicMat-adjacent industrial. Mixed daily flow (4/10 bullish) but today bullish + strong magnitude. | Jan 2027 ATM calls (940C) or 800/900 spread. | $720 break | **full** (win_rate 0.90 capped from 0.727) |
| **AAPL** | 8 | LEAP-radar QUALIFIED 7/9 ($4.2B DP at VWAP 294, 8/10 bullish days, +9.1% over 10d, cum_prem 90d +$437M). DEX +$14.2T LONG MEDIUM. Major OI build 9/18 350C (+25k). Earnings 7/30. | 60–180DTE call spreads (e.g. Sep 300/320C); sized half due to Tech-OUT sector gate. | $285 break | **half** (sector gate −1 tier from full) |
| **NVDA** | 7 | DEX +$69.7T LONG HIGH (deepest call-skew in book), ZGL 81.73 = strong support. POSITIVE GEX 220 pin. Cum_prem 30d +$136M. Watchlist alert: $9.1B DP + 340k OI shift today. Macro net flow +$42M. | 30–60DTE call verticals (e.g. Jun 220/235C). 7/17 220C is the institutional anchor. | $210 break (gamma flip pivot) | **half** (sector gate −1 tier) |
| **TGT** | 5 | Block 87.6% buy + BUILDING 5/5 + DIR_LONG conf 24.1% + ConsDef sector IN (9× spike today). | Common or 90DTE calls (Aug 125/135C). | $135 break | starter+ (sector tailwind) |
| **ILMN** | 5 | Block 58.7% buy + BUILDING 5/5 + DIR_LONG conf 43.9% + Healthcare IN. | Common stock (1Q+ horizon). | $95 break | starter |
| **PCG** | 5 | Multileg call vertical 9/18 20C/23C $8.4M (institutional debit spread). Macro confluence score 6. | Replicate 9/18 20C/23C call vertical. | $18 break | starter (flow-conflict cap; cum_prem 30d −$3.4M) |
| **IWM** | 5 | Vanna-squeeze HIGH (put-heavy book + GEX flipped POS today + falling-VIX tailwind). | 30DTE call vertical (Jun 280/290C). | $220 break | starter (flow-conflict cap; multileg sees BEARISH put-condor stack $71M; cum_prem −$1B) |
| **SNDK** | 4 → demoted MEDIUM | 5/5 persistent BULLISH $1.2B sweep + cum_prem 30d +$816M. **Step 3a gate: cited only 1 load-bearing tool (cum_prem) → demoted from HIGH to MEDIUM**. Batch_scan ALSO disagrees (calls SNDK bearish credit-spread); deferring to multileg/sweep read but at reduced size. | 30–60DTE call spreads (Jun 1500/1600C). | $1380 break | half (after demote) |

**Watch-only (failed score floor or skipped by risk-monitor):** UNH (90d cum_prem −$133M overrides today's mega DP — quarantine), TTMI, CORZ, HD, WEN, COST, LLY, HUM.

### 3b. Short / fade swings (defined risk only)

Every short except GTLB took −1 tier from regime gate (SHORT in TRANSITIONAL UPTREND). Most floor to skip; standalone short conviction is structurally compromised this tape.

| Ticker | Score | Thesis | Structure | Final Size |
|---|---|---|---|---|
| **GTLB** | 6 | Macro bear confluence score 6 (top of bearish board); 6 aligned factors. | If forced: defined-risk put debit spread Jun 22/19P. Else skip. | **skip** (floored by regime gate) |
| **MU** | 5 | $440M LEAP put diagonal 850P/1000P (3-min coordinated whale ticket); Tech OUT sector confirms; cum_prem 30d −$429M aligned. | Replicate institutional Jan 2027 850P/1000P diagonal at retail size. Otherwise skip. | **skip** (floored despite quality structure — risk-monitor regime gate) |
| **XP** | 5 | PCR z+14.24σ contrarian SHORT-FADE survivor (only fade clearing event filter). | Bear call spread 20C/22.5C 5/22 (defined-risk credit). | **skip** (triple-gated: regime + corr-cluster + flow conflict) |
| **TSLA** | 4 | 5/5 BEARISH sweep $9.8B (largest in tape). | — | **skip** (cum_prem +$1.06B BULLISH = sweep is hedge flow, not directional; recent bullish_flow signals delivered +5.26%/+8.71%) |
| **MRVL** | 3 | Earnings BEARISH analyst-vs-flow disagreement (highest-EV non-vol setup). | Defined-risk put debit Jun 160/150P if forced. | skip (regime gate) |

**Index hedges (non-standalone):** SPY/QQQ/SPXW/META/MSFT shorts collapse into the **hedge sleeve** (SPY 730/710 June put vertical sized ~25% of book delta + small VIX 22/30 June ladder).

---

## 4. LEAP Builds (6–24 months)

LEAP-positioning-radar passed only 3 names (DTE > 180, 6-of-9 gates).

| Ticker | DTE | Score | Cum_prem 90d | Structure | Notes |
|---|---|---|---|---|---|
| **CNC** | 248–619 | 8.5 | +$28M | Jan 2028 70C (+925 OI today) + Jan 2027 67.5C (+449). 24-mo LEAP signature. | Healthcare-IN sector + 81% 30d move + fresh-thesis. Cleanest fingerprint. |
| **AAPL** | 252 | 8.0 | +$437M | Jan 2027 240P (33,930 OI build 5/8) + Aug/Sep 2026 320C/350C (+92k combined). | Thesis-extension. $4.2B DP at VWAP 294. Best clean LEAP add: AAPL 270115C (delta ~0.7 ITM near 280 strike). |
| **URI** | 254 | 7.0 | +$52M | Jun 2027 1240C (+20) + Jan 2028 950P (+17). Thin volume — size as 1100/1240 debit call spread, not naked. | Industrials adjacency to BasicMat IN. |

**LEAP REJECTED with explanation:**
- **MDT** — 5/9 gates passed but conviction_matrix=MIXED, accumulation NEUTRAL (DP buy 0.471 sell-heavy), DP price 30d −11.34%. Healthcare tailwind insufficient when DP is distributing.
- **UNH** — REQUIRED 90d cum_prem gate FAILED at −$133M directional premium against the position. Today's mega DP is a chase against persistent 90d distribution.
- **NVDA** — 90d flow MIXED (50.3/49.7 split = noise). Massive Dec 2028 200C build is offset by simultaneous Jan 2027 180/240P put build = hedged-long collar, NOT directional LEAP.
- **QCOM** — MIXED 90d flow (52/48 split, +$129M on $3.3B base = noise).

**LEAP rolls detected:** AAPL near→Aug 320C (+66.7k); AAPL near→Sep 350C (+25k); V <21 DTE→>21 DTE call (3,778 size, balance 0.961 = clean institutional roll).

---

## 5. Volatility Surface

**KINKED earnings names (sell event-week calendar):**

| Ticker | Kink DTE | IV Jump | Structure |
|---|---|---|---|
| MRVL | 17 | +21.1pp 5/22→5/29 | Sell 5/29 ATM straddle (105% IV) / buy 6/18 ATM (91%) |
| ULTA | 24 | +14.6pp 5/29→6/5 | Sell 6/5 ATM call (53%) / buy 6/12 ATM (49%) |
| CIEN | 24 | +16.6pp 5/29→6/5 | Sell 6/5 ATM (107%) / buy 6/19 ATM |
| GTLB | 24 | +13.1pp 5/29→6/5 | Sell 6/5 ATM (96%) / buy 6/12 ATM (89%) |
| TGT | 7 | 5/15(91%)→5/29(56%) | Earnings 5/21 — front-loaded event premium |
| HD | 7 | 5/15(58%)→5/22(48%) | Earnings 5/19–20 |

**BACKWARDATION (no clean event kink):**
- QCOM: front 124.7% / back 54.1% — STEEP, post-event hangover. Only clean no-catalyst calendar candidate (sell 5/15 / buy 6/18 ATM, conditional on falling front_end_iv_ratio).
- INTC: front 123.6% / back 84.7% — DO NOT FADE (entire curve elevated, structural).
- SOXX: front 67.6% / back 47.4% — sector-level vol unwind candidate.
- AMD: smooth 90.8%→71.5% — no event kink.

**IV outliers (synthetic financing, NOT vol mispricings — flagged for transparency):** NVDA 6/18 0.5C ($9.88M premium @ 678% avg IV), NFLX 5/15 1C ($1.83M @ 3247% avg), APLX small-cap multi-strike call sweep.

**Earnings vol plays (size-gated by FAIR VRP −1 tier):**
- **TTWO** — BUY VOL long straddle 5/22 226 (implied move 2.85% historically LOW for TTWO; complacent tail; bullish flow). Final size: **half**.
- **ULTA** — BUY VOL long calendar (sell 5/15 / buy 6/5 ATM). Final size: **half**.
- **CSCO** — SELL VOL iron fly 5/15 half-size (front IV 116% post-print decay; back-skew NORMAL gates full size). Final size: **starter**.

---

## 6. Risk & Correlation

**Correlation clusters detected (corr > 0.7 = treat as one position):**

| Cluster | Members | Survivor | Dropped |
|---|---|---|---|
| C1 — Index-beta | SPY, QQQ, IWM, XP, SPXW (corr 0.79–0.91) | **IWM** (only LONG; vanna-squeeze differentiation) | SPY, QQQ, XP, SPXW |
| C2 — Semi-beta | MU, SNDK (corr 0.77) | **Both retained** as natural pair-trade hedge (MU short / SNDK long opposing) | — |
| C3 — Megacap tech | NVDA, META, MSFT (corr 0.57–0.66) | **NVDA** (long, score 7) | META, MSFT |

**Regime conflicts (−1 tier on every short):** GTLB, MU, XP, TSLA, QQQ, SPY, META, MSFT, SPXW, MRVL — all SHORTs in TRANSITIONAL UPTREND.

**VRP gates (FAIR VRP, no vol-buying or vol-selling edge):** TTWO −1 tier, ULTA −1 tier, CSCO −1 tier.

**Adverse sector rotation gates:** AAPL −1 tier (LONG in Tech OUT), NVDA −1 tier (LONG in Tech OUT). All shorts in OUT sectors get NO penalty (confirms thesis).

**Adverse-flow exit list (rolling watchlist):**
- **AMD** — BEARISH net flow −$24.9M, IV rank 87 (options expensive), long thesis decaying — **priority stop-loss review**.
- **QQQ** — BEARISH −$43.2M, P/C 1.01, +795k OI = institutional puts accreting; swing-bias confirmed SHORT.
- **LRCX** — softening (volume_ratio 0.71 below avg, IV 76).
- **NVDA, KWEB** — thesis confirmed, retain.

**Hedge sleeve recommendation:** Book net-delta is LONG-skewed after gates (CNC/URI/AAPL/NVDA long survive, all shorts ex GTLB skip). Macro shows climax warning (SPY +7.6% 30d w/ 35.2% breadth, QQQ swing flip SHORT, $21B aggregate index put accretion, dealer SPY DEX −$75T put-heavy). **Hedge:** SPY 730/710 June put vertical sized to ~25% of book delta (defined risk; captures QQQ regime flip without paying VIX call vol). Add SMALL VIX 22/30 June call ladder sized 0.5% NLV as tail insurance for bearish-breadth-into-OPEX. **Avoid outright VIX longs while VRP FAIR — defined-risk verticals only.** IWM long is natural offset to SPY put hedge.

---

## 7. High-Conviction Cross-Ref (score ≥ 5)

Per-ticker breakdown sourced from `signal-confluence-quant` audit trail. Each component cites named source agent + tool. **Step 3a load-bearing-tool gate applied** — HIGH-tier (sized full post-quant) calls require ≥2 of {dark_pool_block_stratified, historical_cumulative_premium_flow, insights_institutional_accumulation, options_structure_dex}.

| # | Ticker | Side | Raw Score | Dominant Class | Win Rate | Pre-Risk | Risk Gates Applied | Final Size | Load-Bearing Cited | Invalidation |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CNC | long | 11 | dark_pool_accumulation | NA | starter | none | starter | dark_pool_block_stratified ✓, historical_cumulative_premium_flow ✓ | $70 |
| 2 | URI | long | 9 | leap_directional | 0.90 | full | none | **full** | dark_pool_block_stratified ✓, historical_cumulative_premium_flow ✓ | $720 |
| 3 | AAPL | long | 8 | leap_directional | 0.90 | full | sector −1 (Tech OUT) | **half** | options_structure_dex ✓, historical_cumulative_premium_flow ✓ | $285 |
| 4 | NVDA | long | 7 | gamma_breakout | 0.90 | full | sector −1 (Tech OUT) | **half** | options_structure_dex ✓, historical_cumulative_premium_flow ✓ | $210 |
| 5 | GTLB | short | 6 | bearish_flow | 0.259 | starter | regime −1 | skip | — | n/a |
| 6 | IWM | long | 5 | vanna_squeeze | 0.90 | half | flow_conflict −1 | starter | options_structure_dex ✓ (DPS), historical_cumulative_premium_flow (conflict) | $220 |
| 7 | PCG | long | 5 | multileg_directional | 0.90 | half | flow_conflict −1 | starter | hot_chains_multileg only (no LB), historical_cumulative_premium_flow (conflict) | $18 |
| 8 | TGT | long | 5 | dark_pool_accumulation | NA | starter | sector +TAILWIND | starter+ | dark_pool_block_stratified ✓ | $135 |
| 9 | ILMN | long | 5 | dark_pool_accumulation | NA | starter | none | starter | dark_pool_block_stratified ✓ | $95 |
| 10 | UNH | long | 5 | dark_pool_accumulation | NA | starter | flow_conflict −1, LEAP-rejected −3 | skip | dark_pool_largest, historical_cumulative_premium_flow (conflict) | n/a (quarantine) |
| 11 | MU | short | 5 | multileg_directional | 0.259 | starter | regime −1 | skip | hot_chains_multileg, historical_cumulative_premium_flow ✓ (aligned) | n/a |
| 12 | XP | short | 5 | bearish_flow | 0.259 | starter | regime −1, cluster −1, flow_conflict −1 | skip | historical_pc_ratio_zscore, historical_cumulative_premium_flow (conflict) | n/a |

**Demotion log:** SNDK (score 4 → MEDIUM tier per Step 3a — only 1 of 4 load-bearing tools cited).

### Conviction-scoring rubric (verbatim per Step 4)

```
+3  dealer-positioning DEX flip / vanna-squeeze in trade direction
+2  3+ aligned signals in accumulation-hunter (DP+OI+oi_smart_positioning, dark_pool_block_stratified institutional-tier)
+1  multi-day OI build (historical_oi_trend BUILDING, lookback ≥ 5)
+2  insights_conviction_matrix = DIRECTIONAL_LONG, conf > 70 (50–70: +1)
+2  historical_cumulative_premium_flow net directional accretion (30d) in trade direction
+1  in sweep-tracker top 5 by hot_chains_sweep_persistence
+1  sector-rotation single-name leader (persistence ≥3)
+1  earnings-scout BUY VOL or SELL VOL
+2  multileg-strategist directional structure (term-anchored)
+1  vol-surface-scout KINKED/BACKWARDATION VRP-aligned
+1  opex-pin-strategist ranks ticker top-5 (OPEX week)
−2  contrarian-scanner overcrowded long with rising historical_pc_ratio_zscore
−2  audit-trail flow_conflict (cum_prem direction contradicts dominant_signal_class)
−1  risk-monitor correlation cluster (corr > 0.7) — applied 2b
−3  risk_market_regime conflicts trade direction — applied 2b
```

**Sizing map:** win_rate ≥0.65 → full; 0.50–0.65 → half; <0.50 → starter/skip.

---

## 8. Watch-only — single signal, no confluence

Below conviction floor (score <3) or single-source signals — journal, do NOT enter:

- **CORZ** (score 2): 5-signal accumulation but flow_conflict (cum_prem 30d −$15.8M)
- **TTMI** (score 2): soft accumulation only, no DEX/sweep/multileg confirmation
- **AMD** (score 0): DISQUALIFIED — parabolic +120% 30d chase, accumulation NEUTRAL, semis OUT
- **SMH** (score 0): conflict — sweep bullish vs dealer-positioning HIGH SHORT vs sector OUT
- **WEN** (score 2): single multileg structure only
- **HD** (score 1): single bullish flow $3.9M only
- **BAC, WFC, XLF** (score 1): single sweep cluster only
- **INTC** (score 2): tech-out sector + bearish flow but no quality confirmation
- **AMZN, NBIS** (score 1): sector rotation only
- **ORCL** (score 1): single 4/5 sweep only
- **OWL@10 pin** (score 2): liquidity caveat from opex-pin-strategist

**Watchlist write-back:** confirmed by risk-monitor and verified — `conviction_2026-05-12 = [CNC, URI, AAPL, NVDA, GTLB]`. Yesterday's `conviction_2026-05-11 = [LRCX, NVDA, AMD, KWEB, QQQ]` retained for tomorrow's adverse-flow audit.

---

*Generated 2026-05-12 post-market. Two-phase agent fleet (12 Phase 1 alpha-finders incl. opex-pin-strategist, then signal-confluence-quant + risk-monitor). All sizing pre-risk per signal-confluence-quant; final size after risk-monitor gate stack. Multi-day persistence preferred over single-day snapshots throughout.*
