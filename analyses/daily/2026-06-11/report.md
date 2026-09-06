# Daily Market Analysis — 2026-06-11

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / PULLBACK_IN_UPTREND. SPY 737.76 (>50sma 721, <20sma 745.4; −2.98% from 90d high). VIX **19.56** (elevated, HIGH tercile). Breadth divergence: options flow only **40.8% bullish** (defensive) vs price tape **63.6% green** — price up, flow hedging. Tech headline inflow (+$2.1B) **masks a semis-specific de-risk** (SMH −$151.6M 5d, $20M+ opening PUT sweeps, IV-rank 100). Defensive-quality bid (XLP) running beside it.
- **Next-session GEX (SPY/QQQ):** **SPY short-gamma** (ZGL null/FULLY_NEGATIVE, total_GEX −372M but decompressing off −2.5B · call wall 750 / put wall 720) → trend/breakout prior, debit verticals. **QQQ marginal long-gamma** (fresh 1-session flip, +31M razor-thin · call wall 720 / put wall 700) → low-conviction pin 715–720. The two indices **disagree** on tomorrow's vol regime. Advisory, see §2.
- **Top swing build:** **NONE.** No name clears the gate stack. Top scorer AAPL is raw-6 LOW and was demoted to SKIP (fundamentals CAUTION + debate cut + panic gate). The desk call is **stand aside.**
- **Top LEAP candidate:** **NONE.** Zero names cleared the 6-of-9 LEAP gate (thin 4.8% LEAP tape; what exists is hedges + covered-call supply).
- **Biggest risk:** **FOMC + SEP/dot-plot Wed 2026-06-17 (T+3)** sits inside every horizon in the book; front-end IV already in backwardation (SPY ratio 1.555). Candidate cluster is semis-concentrated (MU/MRVL/ASML) on a semis-de-risking day. Hedge sleeve = SPY/QQQ or SMH put **debit spread** through 6/18 (sell the rich front vol), contingency-only — the gated book carries ~zero new delta.

> **No-edge day.** Every scored name gated to SKIP or WATCH-ONLY. The only positive-alpha, real-backtest call (MSFT short, 0.567 WR, +17.8pp excess) was VETO'd by fundamentals because the bearish flow fights a strong-buy, oversold, accelerating underlying. The right trade today is patience through the FOMC print.

---

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend **PULLBACK_IN_UPTREND**. SPY 737.76, above 50sma (721.07), below 20sma (745.40), −2.98% from the 90d high, 30d flat (−0.06%). Guidance: half size, defined-risk, iron condors in range.
- **Breadth:** `uw` flow breadth **40.8% bullish** (3,690 bearish vs 2,548 bullish flow tickers — defensively tilted tape). `fz` price breadth (advisory, independent lineage): **320 adv / 181 dec, pct_green 63.62%** over 503 names. No `pct_green < 50` distribution flag, **but a real flow-vs-price split**: price grinding green while options flow leans defensive — a hedging-into-strength tell consistent with the pre-FOMC posture.

**Per-index gamma (current EOD book):**

| Index | Spot | Zero-gamma (ZGL) | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 737.64 | null (unreliable) | −372.5M | FULLY_NEGATIVE | 750 | 720 |
| QQQ | 715.92 | 192.9 (garbage) | +31.1M | POSITIVE (fresh flip) | 720 | 700 |
| IWM | ~153 | 153.27 | −226.8M | POSITIVE | — | — |

(The forward, next-session read of SPY/QQQ is in §2.)

- **`uw options-flow dte-volume-share`:** 0DTE 31.1% / weeklies 44.4% / monthlies 13.1% / LEAPs 4.8% — BALANCED, weekly-dominated retail tape; thin long-dated activity (the LEAP-radar headwind).
- **`uw historical vrp` (SPY):** **FAIR** (+0.0262; IV30 16.43% vs realised 13.81%) — IV modestly rich, no clean directional VRP edge.
- **Macro backdrop (`scripts/fred_macro.py`):** yield curve **normal** (10Y−2Y +0.40), core CPI **2.96%** / core PCE **3.29%** YoY (sticky), unemployment 4.3%, payrolls +172k, **10Y 4.55% RISING**, **USD strengthening**, fed funds 3.62%. Rising-rate + strong-USD = mild headwind for high-multiple/long-duration tech. **Forward `event_risk`:** **FOMC decision + SEP/dot-plot 2026-06-17 (HIGH)** and Retail Sales (May) ~6/17; May CPI/PPI already printed; June CPI 7/14 (outside window).

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book read forward as the prior for the **2026-06-12** open. Prose-only, **0 rubric points**, no backtested predictive claim. SPY/QQQ only.

### SPY — short-gamma into the open
- **regime FULLY_NEGATIVE · ZGL null (zgl_reliable=false) · total_GEX −372.5M** (the *least* negative print in 5 sessions — was −2.51B on 06-10; short-gamma decompressing on the +1.5% bounce off the 06-10 low).
- **call wall 750** (+64.6M, +1.7% / ~12pts up) — first durable upside cap. *Ignore the +189M pillar at 737* — that is the expiring 06-11 0DTE strike, it rolls off overnight.
- **put wall 720** (−105.6M, −2.4% / ~18pts down); 730/725 are downside accelerant shelves.
- **structure bias:** Short-gamma → dealers hedge *with* direction, moves extend not mean-revert. A break of 730 invites a slide toward 720. Upside contested until spot reclaims 745–750. **Debit verticals / directional 0DTE on a clean break of 730 (down) or 745 (up)** — prefer verticals over outright straddles (VIX 19.56 already elevated, VRP FAIR). Iron-fly/fade-the-poke NOT supported (no +GEX walls bracketing spot below 745).

### QQQ — marginal long-gamma (fresh flip)
- **regime POSITIVE but freshly flipped TODAY** from 4 straight FULLY_NEGATIVE sessions · **ZGL 192.9 garbage (zgl_reliable=false)** · **total_GEX +31.1M razor-thin.**
- **call wall 720** (+42.4M, +0.6% / ~4pts up); **put wall 700** (−60.3M, −2.2% / ~16pts down). Spot wedged inside a +GEX pocket (715 shelf / 720 cap).
- **structure bias:** Marginal long-gamma → mild pin/mean-revert toward 715–720 IS the base case, but **low conviction** (regime 1 session old, +31M thin, any down-gap reopens the short-gamma trapdoor to 700). Iron fly / 715–720 butterfly, small, hard stop; abandon the pin if it loses the 714/715 shelf.

**Cross-read:** SPY short-gamma vs QQQ long-gamma is a **divergence, not a confirmation** — itself an argument against high conviction either way. Shared signal: short-gamma intensity is *decompressing* across both books.

**Mandatory caveats:** EOD is a prior, not a target (first 30–60 min of 0DTE OI redraws the levels — esp. the SPY 737 pillar). **Gap risk into FOMC 6/17** voids the prior (QQQ already in front-end backwardation, 0DTE IV 2.01× VIX). ZGL unreliable on both (null/extrapolated). ETF book, not the cleaner SPX/NDX index book. `uw` cannot isolate the D+1 expiry — this is the 0–45d proxy.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — validated stack)
Advisory, **delta-neutral, 0 rubric points** (validation sample has no vol shock → short-vol tail unsampled). Both indices backtest **GO_PREMIUM_SELL_INTRADAY**.

| Index | sell_premium | vol_state / VIX | implied move | exp. range | size_scalar | structure | entry |
|---|---|---|---|---|---|---|---|
| **SPY** | YES (open WR 95.3%, n=43) | HIGH / 19.56 | 1.45% | ±1.22% | **1.5×** | wider iron condor ±1.22% (short-gamma: wider/trendier) | at/after open once gap resolves; hold to close, never overnight |
| **QQQ** | YES (open WR 90.7%, n=43) | HIGH / 19.56 | 2.48% | ±1.19% | **0.75×** | iron fly / short straddle @716, wings ±1.19% (long-gamma) | same; **CAUTION: front-end backwardation (0DTE IV 2.01× VIX) — event/gap risk, half size** |

Direction: none (delta-neutral). **SPY ≈ SPX** (trade either); **QQQ weaker** (Nasdaq index book unavailable) + flagged caution. Stand aside on either if it gaps beyond the wings.

## 2b. Swing Dealer Positioning (1–4 weeks)
A **coordinated index-wide DEX flip to POSITIVE printed today (06-11)** — SPY +9.3B, QQQ +32.6B, IWM +7.6B — riding on top of a week-long FULLY_NEGATIVE GEX regime (vol shock 06-05, VIX 15.4→21.5). **It is 1 session old and unconfirmed** → indices NEUTRAL pending a 2nd–3rd confirming session, and it sits 3 days before FOMC. **All vanna-squeeze flags FALSE** (VIX elevated/choppy, no sustained ≥3-session decline — every put-heavy book is "vanna pressure, not squeeze").

| Name | DEX | 5d trajectory | Swing bias | Conv | Note |
|---|---|---|---|---|---|
| **MU** | +33.5B | positive-persistent (held thru selloff) | **LONG** | MED-HIGH | only clean swing-long structure; GEX +38.8M no-flip; +9.7% today |
| MRVL | +6.0B | positive-persistent | LONG | MED | confirms semis-up DEX theme |
| ASML | +3.5B | improving | LONG | LOW-MED | smaller magnitude |
| QQQ | +32.6B | whipsaw→recover | NEUTRAL→LONG-pending | LOW-MED | cleanest DEX+GEX dual-flip but call-heavy + front panic + FOMC |
| SPY / IWM | +9.3B / +7.6B | whipsaw | NEUTRAL | LOW | 1-session flip into FOMC |
| NVDA | +10.2B | **deteriorating** | NEUTRAL (SHORT if DEX<0) | — | positive but eroding fast; watch the cross |
| MSFT | **−5.95B** | deteriorating | NEUTRAL (DQ) | — | DEX bearish but vanna-conflict → fails clean-thesis gate |
| META | −6.26B | deteriorating | NEUTRAL (DQ) | — | bearish but move already played (−9.4%) |

## 2c. Sector Rotation
- **`uw options-flow sector-flow-persistence`:** rotation regime **`no_change`** (low confidence). Nearly all sectors INFLOW ps=1; **Consumer Cyclical ROTATING ps 0.6** (today −$326M, was +$89M → rotating OUT) but **contradicted by XLY ETF inflow** → no clean cyclical→defensive call. Tech ps=1 but **DECELERATING** (3.8B→2.1B). This is a defensive-quality bid (XLP) beside Tech/semis de-risking — internal repositioning, not a regime rotation.
- **Rotating into:** Consumer Defensive (XLP +$7.6M 5d, agree) — leaders **DG/KO/GIS**. **Rotating out:** Utilities (XLU −$4.5M, both layers agree); **Tech/semis** (SMH −$151.6M, the largest outflow + $20M+ opening PUT sweeps).

**ETF flow tape (advisory — 0 rubric points):**

| ETF | Net prem dir | Persist. | DP positioning | Options urgency | GICS agreement | Leaders |
|---|---|---|---|---|---|---|
| XLP | inflow +7.6M | BULLISH 5d | $18M+ DP prints (positioning) | put-skewed (hedges) | agree (Staples) | DG, KO, GIS |
| XLY | inflow +2.3M | BULLISH 5d | $10.3M DP | call sweeps 115/116C | **disagree** (GICS Cyclical OUT) → watch | BKNG, AMZN, MELI |
| XLC | inflow +2.0M | BULLISH 5d | $2.7M DP | thin | agree | GOOG, TMUS |
| **SMH** | **outflow −151.6M** | **BEARISH 5d** | $58M below-mid DP | **$20M+ opening PUT sweeps** (545/525/475P) | agree-w-decel (Tech) | semis |
| KRE | outflow −22.0M | BEARISH 5d | $24.7M DP | mixed | disagree → watch | regional banks |
| IGV | outflow −15.4M | BEARISH 5d | $12.3M below-bid DP | put-heavy sweeps | agree-w-decel | software |

**Swing implication:** the cleanest reads are *short/short-vol Utilities* and *fade semis bounces* — the SMH put wall flags Tech's headline inflow as decelerating and internally bearish. No swing-book rotation trade; these are individual tilts inside a pullback.

---

## 3. Swing Setups (1–6 weeks)
**Every name below is gated to SKIP or WATCH-ONLY.** Ranked by conviction; the table documents *why nothing trades*, not what to put on.

| Ticker | Score / Tier | Dir | Thesis | Structure (if it cleared) | Invalidation | Final size |
|---|---|---|---|---|---|---|
| AAPL | 6 / LOW | long | DP block accumulation $290–296 + OI build + confluence-4 | (debit call spread) | loses $290.4 DP shelf / flow flips net-seller | **SKIP** |
| MU | 5 / LOW | long | DEX +33.5B persistent + memory up-cycle, +$207M flow leader | (call spread, trim pre-6/24) | gaps below entry post-ER / loses memory bid | **SKIP** |
| MRVL | 4 / LOW | long | DEX +6.0B + S&P-500 inclusion 6/22 | (call spread) | S&P 6/22 sell-the-news fade | **SKIP** |
| ASML | 4 / LOW | long | DEX +3.5B + confluence-5, EUV monopoly | (call spread) | flow_conflict deepens / RSI-69 unwind thru $1,826 | **SKIP** |

### 3a. Long swings (regime-aligned)
None survive. AAPL carries a **distribution caution** (⚠ C28): upside call OI unwound −3,577 + a fresh 10k-lot 170P opened *into* the dark-pool "accumulation," and insiders sold 3 straight months (MSPR −50.5) — the accumulation-as-distribution tell. The semis longs (MU/MRVL/ASML) are real DEX-flow structures but all are: negative market-excess (beta, not alpha), sub-0.50 backtest win-rate, priced *above* analyst targets, into a semis-de-risking tape and FOMC T+3.

### 3b. Short / fade swings (defined risk only)
**MSFT short — WATCH-ONLY (VETO'd).** The strongest flow short on the desk (accumulation DISTRIBUTION mega_br 0.03, Tier-1 $20.1M opening-put whale, DEX −5.95B, +0.178 market-excess, 0.567 WR) — but fundamentals VETO it: 4/4 beats, +17.9% rev / +29.8% EPS accelerating, Recom 1.23 strong-buy, +43% to target, RSI 36.8 oversold. Shorting an oversold, strong-buy, accelerating mega-cap into a 43% upside gap is the squeeze-loss pattern; the bearish flow reads as FOMC-week hedging on the biggest index weight, not directional conviction. **No short.**

**Contrarian fades:** NONE. The 3 statistical extremes (CL z+4.5, ISRG z+3.6, MSFT z+3.1) are all **BACKWARDATION into FOMC** — event-driven insurance bids, not exhausted crowding → abort.

**Near-term sweeps (informational, 0 points):** the entire mega-cap/index sweep-persistence book (SPXW/SPY/QQQ/NVDA/MSFT/META all bearish 5/5) is **FOMC-week downside hedging** — cum_flow MIXED on all 12, demoted to hedge-flow watch. Only **INTC** (call sweeps, DIRECTIONAL_LONG, DP co-flag, opening-confirmed) and **MRVL** (5/5 persistence, MIXED conviction) carried directional sweep signal — and both scored out below the floor (see §7/§8).

---

## 4. LEAP Builds (6–24 months)
**ZERO qualifying candidates.** No DTE>180 build cleared the 6-of-9 gate. Disqualifications:
- **SCHW** — 10 consecutive build days on $105/$125 Dec-26 calls, but cum-flow −$15.6M (90d) BEARISH + conviction-matrix **COVERED_CALL** (yield enhancement / call-overwrite, not conviction). Hard reject ×2.
- **DKNG** — passed the flow gate (cum-flow +$27M/+$31M fresh-thesis accretion, $33 Jan-27 call build) but conviction-matrix **MIXED 6.2%** (balanced bid/ask tape, neutral DP). Routed to accumulation-hunter for a swing look; not a LEAP.
- **Step-0 semis/tech leaders (MU/SNDK/ASML/MRVL/GOOG)** — none appear in DTE>180 builds; their premium is short-dated day-flow. GOOG is actively DISTRIBUTION.
- Regime overlay (rising 10Y 4.55%, sticky PCE 3.29%, strong USD) is a structural headwind for long-duration calls anyway. **Stand aside on new LEAP exposure** until LEAP-DTE tape recovers >8–10%.

---

## 5. Volatility Surface
The headline is a **semis vol complex bid by FOMC 6/17 + MU earnings 6/24 read-through**, not name-specific euphoria (NVDA z-score −0.35 NORMAL confirms it's memory/WFE-specific). The cleaner book is **earnings short-vol**:

| Ticker | Print | Verdict | Size | Event IV (expiry) | Back-mo skew | Implied move | Note |
|---|---|---|---|---|---|---|---|
| **FDX** | 6/23 AMC | **SELL VOL** | **Full** | 56% (6/26) | +0.056 TAIL_HEDGING | ~2.8% | cleanest — front kink AND tail both priced; 6/18 is a post-FOMC trough |
| **MU** | 6/24 AMC | SELL VOL | Half | 128% (6/26) | −0.012 COMPLACENT | ~4.3% | DTE-1 152% is FOMC, *not* the print; sell only the 6/26 leg, skew to calls |
| **ADBE** | reported 6/11 AMC | SELL VOL | Half | 223% (6/12) | −0.025 COMPLACENT | ~7–8% | IV-crush 223→70%; complacent back = half only (CFO Dan Durn → Marvell) |
| **ACN** | 6/18 AM | SELL VOL | Half | 110% (6/18) | +0.029 NORMAL | ~2.1% | front-only kink; half |
| **AMAT** | none <30d | SELL VOL | (post-FOMC) | — | COMPLACENT | — | VRP +0.077 PREMIUM_SELLING, z+3.28 — cleanest VRP; enter post-6/24 |
| **LRCX** | 7/29 (out) | SELL VOL | (post-FOMC) | — | COMPLACENT | — | VRP +0.068, z+3.37; enter post-6/24 |
| JBL | 6/17 AM | SKIP | — | 103% | NORMAL | — | back-month too thin to hedge |
| KLAC | 7/30 (out) | lean SELL | — | — | COMPLACENT | — | **VRP data corrupt — do not size** |

**No clean no-catalyst calendars and no IV-outlier whale hedges today** — every BACKWARDATION name's front is explained by a dated event (FOMC/MU). Wait for the **post-6/24** window when the front collapses and the back is clean before putting on the AMAT/LRCX premium-sells. These earnings/vol plays score only +1 in the directional rubric (structurally under-scored); they are surfaced here, not as conviction calls.

---

## 6. Risk & Correlation
**Macro headline:** sticky core inflation (CPI 2.96% / PCE 3.29%), 10Y 4.55% rising, USD strengthening — a mild high-multiple-tech headwind. **`event_risk`: FOMC + SEP/dot-plot Wed 2026-06-17 (T+3) sits inside every horizon in the book**; Retail Sales (May) ~6/17; MU earnings 6/24 (T+13) is a second in-window binary on the top semis long.

- **Correlation (`uw risk portfolio-correlation`, 30d):** **no cluster fires** (no pair ≥0.70). MRVL/ASML **0.664 = soft-watch** (monitor, no deduction); MU/ASML 0.566. Semis-concentration risk handled at the book level (hedge sleeve), not a discretionary cluster upgrade.
- **Gate stack outcome:** the **front-end panic gate FIRES (SPY ratio 1.555)** → −1 all names; the **debate gate FIRES on all 5** (bear residual ≥ bull — disconfirmation cleared zero trades); the **event-risk gate FIRES** (FOMC T+3) on all four swing longs; **AAPL** adds fundamentals **CAUTION −1**; **MSFT** is **VETO'd** to watch-only. Net: every name → SKIP or WATCH-ONLY.
- **Fundamentals verdicts:** AAPL CAUTION (insider sell + distribution), MU CONFIRM (ER 6/24 in-window), MRVL CONFIRM (S&P 6/22 sell-the-news), MSFT **VETO** (short fights accelerating strong-buy underlying), ASML CONFIRM (flow_conflict_lite).
- **Adverse-flow exit candidates** (`uw watchlist alerts/scan` vs conviction_2026-06-10): **SMH** (P/C 5.32, IV-rank 100, $58M DP, $20M+ put sweeps — exit/avoid any long semis carry), **LRCX** (bearish flow, $128M DP), **TSLA** (−$4.2M flow, OI shift).
- **Breadth divergence (advisory):** price green (pct_green 63.6%) while flow only 40.8% bullish — defensive hedging into strength; no `pct_green<50` distribution flag, does not change sizing.
- **Hedge sleeve (contingency):** the gated book carries ~zero new delta, so **no delta hedge is mechanically required.** Against any *pre-existing* semis carry into 6/17: SPY/QQQ **put debit spread** through 6/18 (buy ~1–2% OTM, sell ~4–5% OTM to finance the rich front-end vol), or a small **SMH put spread** (net-short the over-bid IV-rank-100 skew). **Avoid long VIX calls / naked premium** — front vol is already paying for the event.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**EMPTY.** No name reached MEDIUM (raw ≥7), so there is no high-conviction cross-ref today. The top of the book is documented below as **LOW-tier / watch-only context** for journaling.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no closed `conviction_2026-06-11` calls exist yet (group just written); per-tier realised expectancy is carried from the last `/calibration-audit` and is not recomputed on a zero-trade day. The desk's structural reminder stands: this book's longs have run ~−22pp benchmark excess (beta), its shorts ~+20pp (alpha) — today's only alpha signal (MSFT short) was the one fundamentals vetoed.

**LOW-tier / dropped audit trail (from `signal-confluence-quant`):**

| Ticker | raw | dom. class | win_rate (n, src) | cum_flow 30d/90d | fund. | bull/bear | gates | final |
|---|---|---|---|---|---|---|---|---|
| AAPL | 6 | dark_pool_accumulation | 0.424 (85, fallback) | +82.8M / +413.9M | CAUTION | 0.55/0.75 | panic, fund −1, event, debate | **SKIP** |
| MU | 5 | dealer_positioning(DEX) | 0.479 (71, backtest) | +312M / −244M | CONFIRM | 0.65/0.65 | panic, event(FOMC+ER6/24), debate | **SKIP** |
| MRVL | 4 | dealer_positioning(DEX) | 0.479 (71) | +138M / +126M | CONFIRM | 0.65/0.75 | panic, event, debate | **SKIP** |
| MSFT | 4 | bearish_flow (SHORT) | 0.567 (67, backtest) | −107.9M / +644.8M | **VETO** | 0.55/0.85 | fundamentals VETO, debate kill | **WATCH** |
| ASML | 4 | dealer_positioning(DEX) | 0.479 (71) | −59M / −88M | CONFIRM | 0.65/0.65 | panic, event, debate, flow_conflict_lite | **SKIP** |

**Dropped below floor (raw ≤2):** INTC (raw 1 — C11 halved + flow_conflict_lite; cum_flow −20.6M opposes the long), AMZN (raw 1 — flow_conflict FULL −3, cum_flow −172.9M opposes), BTDR (raw 2 — multileg call-ratio; liquidity actually passes at $207M ADV, but uncapped short-gamma >$30 is a standing risk flag).

**Score-component detail** (Σ = raw, validated): **AAPL** +3 accumulation-C11-confirmed [accumulation-hunter/block-stratified] +1 OI build [oi-trend] +2 confluence=4 [signal-confluence]. **MU** +3 DEX [dealer-positioning/dex] +1 SELL VOL [earnings-scout] +1 cum_flow +312M clean [cum-premium-flow]. **MRVL** +3 DEX +1 cum_flow +138M. **MSFT** +3 distribution-C11-mirror [block-stratified] +1 cum_flow −107.9M (short-aligned). **ASML** +3 DEX +2 confluence=5 −1 flow_conflict_lite.

### Conviction-scoring rubric (Step 4 — embedded for audit)
```
+3 dealer DEX flip / vanna-squeeze in trade direction
+3 3+ aligned accumulation (DP+OI+smart-positioning, block-stratified institutional) — C11 conjunction: full +3 only if cum_flow_30d sign-aligned AND |cum_flow_30d|≥$50M, else halved →+1
+1 multi-day OI build (oi-trend BUILDING, ≥5d)
+1 conviction-matrix DIRECTIONAL_LONG conf>70 — CONDITIONAL: only when dominant_signal_class==leap_directional
+1 cum_premium_flow net directional accretion (30d) — INTENT-SCREENED: only if no distribution_flag AND not ex-div arb
+2 signal-confluence ≥4 (second-agent confirmation)
+1 sector-rotation single-name leader — CONDITIONAL (persistence≥0.6 AND cum_flow aligned AND ≥$50M)
+1 earnings-scout BUY/SELL VOL
+2 multileg directional structure (term-structure-anchored)
+1 vol-surface KINKED/BACKWARDATION VRP-aligned
−2 contrarian overcrowded long + rising pc-ratio-zscore (VRP+)
−3 flow_conflict (cum_flow 30d clearly opposite dominant class) | −1 flow_conflict_lite (MIXED) — mutually exclusive
−1 correlation cluster (corr>0.7, risk 2d) | −3 regime conflict (risk 2d)
Tiers: ≥9 HIGH (full) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 drop.
```

---

## 8. Watch-only — single signal, no confluence
For journaling, NOT for entry today:
- **SMCI** — accumulation-hunter RANK1 (6 internal signals: block_br 0.82, ACCUMULATION 3.81, 5-day all-call OI build, DP support $29.25–29.65, DIRECTIONAL_LONG) but **failed the confluence gate** (`uw insights signal-confluence` = 3 < 4; single-agent) and Step-0 net premium was mildly bearish (−$7.4M). The strongest *internal* accumulation fingerprint on the tape, but no second-agent confirmation.
- **INTC** — sweep DIRECTIONAL_LONG + DP accumulation co-flag + opening-confirmed (2 agents) but cum-flow −$20.6M *opposes* the long → scored to raw 1.
- **AMZN** — accumulation RANK2 (confluence gate passed) but cum-flow −$172.9M full flow_conflict → raw 1.
- **BTDR** — multileg call-ratio spread (financed-bullish $20–25); raw 2, uncapped short-gamma tail >$30.
- **Single-leg whale bearish tape (advisory C19, 0 points):** MSFT (Tier-1 opening put $20.1M, the only one with DP co-confirm), ISRG ($6.5M opening put — no DP co-confirm), ABT ($4.9M floor put — DP actually *accumulating*, likely protective).

---
*Generated by the two-phase agent fleet (10 Phase-1 alpha-finders → quant → fundamentals → bull/bear debate → risk). No OPEX agent (8 days from third-Friday). Outside the validated regime for the single-leg whale edge (TRANSITIONAL vs bull). The honest desk call: **stand aside, no new risk, patience through FOMC 6/17.***
