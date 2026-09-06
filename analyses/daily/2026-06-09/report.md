# Daily Market Analysis — 2026-06-09

> **Desk call: stand-aside-and-trim. Carry near-zero directional risk into tomorrow's CPI.** The quant handed up an all-LOW-tier slate (no HIGH, no MEDIUM). After the gate stack the only defensible position is a **starter SPY short (~0.25R)**; every other candidate is gated to skip or watch-only. The job tomorrow is to *react* to CPI, not to be positioned ahead of it.

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / PULLBACK_IN_UPTREND. SPY 737.05 (below 20sma 746.26, above 50sma 717.45, −3.1% off the 90d high). **All three indices (SPY/QQQ/IWM) are FULLY_NEGATIVE short-gamma** — a 4-session-held regime flip — the worst gamma posture to carry into a CPI print. VIX 19.87. Breadth defensive: **35% bullish options flow under a green equity tape** (fz 73.8% green) = the rally is being *hedged into*, not chased. Sector lean: Tech distribution under positive headline call premium; no coherent rotation-in.
- **Next-session GEX (SPY/QQQ):** **SPY** short-gamma, ZGL null (FULLY_NEGATIVE), pivot **735** (largest node, at spot), upside shelf 750/755 — structure bias: directional/debit, *not* a pin to sell. **QQQ** short-gamma, nodes 700/705/710, no positive shelf nearby, front-end backwardation (0DTE IV 1.85× VIX) → the cleaner long-vol/breakout vehicle for the CPI reaction. Advisory, see §2.
- **Top swing build:** **None worth size.** The lone clean long, **CZR** (raw 3, LOW), is a **merger-arb** ($31 cash Fertitta deal) with capped +5.3% upside vs a ~−30% break tail over a 12-month regulatory clock — gated to skip; if expressed at all, own the common, not the theta-dead July calls (CZR IVR 3.78).
- **Top short:** **SPY short, STARTER only** — dealer DEX −20.99B put-heavy, regime flip held 4 sessions, 7-of-10 bearish flow days, market-excess +0.19. Regime-aligned but held over CPI; short-gamma squeezes *up* on a cool print, hence starter not half.
- **Top LEAP candidate:** **None.** LEAP tape thin (4.8% share); long-dated book is hedging-heavy/bearish. UNM the only near-miss (6-of-9 gates, conviction 56.9 < 70).
- **Biggest risk:** **Event gauntlet into a short-gamma, defensively-positioned tape** — CPI tomorrow (Jun-10), PPI Jun-11, FOMC+SEP Jun-16/17. Correlation: SPY/IWM/MSFT/QQQ are one high-beta cluster (SPY/QQQ 0.91). 4 of 5 names from yesterday's long-semi conviction book (MU/MRVL/LRCX/AMD) flipped bearish overnight = **distribution**, corroborating the short bias.

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity."** Trend **PULLBACK_IN_UPTREND**. SPY 737.05, below the 20-day (746.26), above the 50-day (717.45), −3.07% from the 90-day high, ~flat over 30d (−0.08%). Market breadth is the tell: **2,180 bullish-flow tickers vs 4,050 bearish (35% bullish)** — defensive positioning. The `fz` advance-decline cross-check (independent data lineage) shows the *equity* tape green (**371 advancers / 131 decliners, 73.8% green, +0.96% avg**). That divergence — green price, defensive flow — is a **distribution / hedged-rally** signature the single regime label hides.

**Per-index gamma (current-state EOD book):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Pivot / nodes | Upside shelf |
|---|---|---|---|---|---|---|
| **SPY** | 736.2 | null (FULLY_NEGATIVE) | −1.74B | short-gamma | 735 (−219.9M, at spot), 730 (−153.0M) | 750 (+24.3M) / 755 (+47.2M) |
| **QQQ** | 705.93 | null (FULLY_NEGATIVE) | −0.73B | short-gamma | 700 (−98.5M), 705 (−69.1M), 710 (−84.3M) | none nearby (725 +4.4M negligible) |
| **IWM** | 285.02 | null (FULLY_NEGATIVE) | −0.82B | short-gamma | ~275/276 (deepest neg) | unanchored |

All three flipped FULLY_NEGATIVE ~Jun-04/05 and have **held negative 4 sessions** — a genuine dealer-short-gamma regime (broadly distributed across strikes, not a single-strike OPEX artifact; SPY's top node is only ~13% of total). Dealers sell weakness / buy strength → moves get amplified.

`uw options-flow dte-volume-share`: **0DTE 34.5% / weeklies 28.3% / monthlies 25.6% / LEAPs 4.8%** → **BALANCED** (not 0DTE-retail-dominated, not institutional-monthly-skewed). LEAP tape genuinely thin.

`uw historical vrp`: **SPY FAIR** (IV30 0.165 vs realized 0.121, VRP +0.043) · **QQQ FAIR** (IV30 0.263 vs realized 0.215, VRP +0.048). Modest premium-selling lean, no strong directional-vol edge.

**Macro backdrop** (`fred_macro.py`): yield curve **normal** (+0.4), Core CPI **2.99%** / Core PCE **3.29%** YoY (sticky-high, disinflation stalling), unemployment 4.3%, payrolls +172k, **10Y 4.56% RISING**, **USD STRENGTHENING**, Fed funds 3.62%. Net **restrictive and worsening** — a hot CPI tomorrow re-prices the FOMC dots and is the live tail.

**Forward event risk (Tier-1, named & dated):** **CPI(May) 2026-06-10 (T+1, HIGH)** · **PPI(May) 2026-06-11 (T+2, HIGH)** · jobless claims 6/11 (MED) · **FOMC+SEP 2026-06-16/17 (T+5, HIGHEST)**. Every swing sized today is held over both the CPI and FOMC windows.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book read forward as the *prior* for the next open. Prose-only, **0 rubric points**, no backtested predictive claim. Scope: SPY & QQQ only.

**Both indices enter tomorrow's open SHORT GAMMA / FULLY_NEGATIVE — there is no positive-gamma pin anchoring either tape.** This is the worst gamma posture to be carrying into a CPI print: dealer hedging will *amplify* the reaction, not dampen it.

| Index | Spot | ZGL (reliable?) | Regime | Call wall / upside | Put wall / pivot | Structure bias (next-session 0DTE) |
|---|---|---|---|---|---|---|
| **SPY** | 736.2 | null (not reliable; FULLY_NEGATIVE) | short-gamma, total GEX −1.74B | **750 (+24.3M)**, then **755 (+47.2M)** — only real +GEX shelf, begins at 746 | **735 (−219.9M)** = largest node, the short-gamma *pivot* sits 0.2pt below spot; **730 (−153.0M)** next accel node | Debit verticals / directional 0DTE / long straddle into the CPI flip. **Not** a short-straddle/iron-fly tape — no pin to sell. A break of 735 accelerates toward 730/725; a reclaim of 746 hands flow to dealers who buy into 750/755. |
| **QQQ** | 705.93 | null (not reliable) | short-gamma, total GEX −0.73B | **710 (−84.3M)** is the nearest *friction* (accel node, not a +GEX wall); no true call wall until well above 720 — upside unanchored | **700 (−98.5M)** dominant node ~6pt below spot; **705 (−69.1M)** at spot | Directional 0DTE / debit verticals / long straddle on the flip. With front-end backwardation (0DTE IV ~1.85× VIX), QQQ is the **cleaner long-vol / breakout vehicle** for the CPI reaction — a push through 710 or flush through 700 self-reinforces with no dealer brake. |

**Mandatory caveats:** (1) **EOD is a prior, not a target** — fresh 0DTE OI (today 0DTE was 34.5% of share, ~$1.78B premium) re-racks the ZGL/walls in the first 30–60 min. (2) **Gap risk is elevated** — CPI 8:30 ET tomorrow can re-rack the entire short-gamma book before walls matter; PPI Jun-11 and FOMC Jun-16/17 compound. (3) **ZGL is null** on both (FULLY_NEGATIVE) — regime read taken from total_gex sign + spot-vs-node position, `zgl_reliable=false`. (4) **ETF book**, not the cleaner SPX/NDX index book. (5) uw cannot isolate the D+1 expiry (`gex --dte-max 1` errors) — this is the standing 0–45 DTE proxy.

### 2a. Next-session 0DTE premium-selling setup (`zerodte_setup.py` — the validated stack)

> Advisory, delta-neutral, **0 rubric points**. NOT a guaranteed edge — the validation sample contains no vol shock, so the short-vol left tail is **UNSAMPLED**. The GEX walls above are a *map*, not a pin (wall-as-magnet backtested NO_GO).

Backtest verdict both indices: **GO_PREMIUM_SELL_INTRADAY** (SPY premium-sell win 95.1% open, mean +0.31%; QQQ 90.2%, mean +0.40%). VIX 19.87 = **HIGH** vol state (rich premium). **But both are short-gamma → wider expected range, trendier tape**, and the CPI print sits dead ahead.

| Index | sell_premium | vol_state | size_scalar | Implied / expected range | Suggested structure | Entry rule | Caution |
|---|---|---|---|---|---|---|---|
| **SPY** | yes | HIGH | **1.5** | implied 1.38% / expected ±1.15% | Wider iron condor, wings ≈ ±1.15% — or reduce/stand aside | Enter at/after the open once the gap resolves; hold to close; **never carry overnight** | — |
| **QQQ** | yes | HIGH | **0.75** | implied 2.31% / expected ±1.75% | Wider iron condor, wings ≈ ±1.75% | Same — intraday only | **Front-end backwardation (0DTE IV 1.85× VIX) — event/gap risk; half size** |

**Desk overlay:** this is delta-neutral VRP harvest **only after the CPI gap resolves**. Do not pre-position the condor ahead of the 8:30 print; if it gaps beyond the wings, stand aside. SPY ≈ SPX (validated identical); QQQ is the weaker book (Nasdaq index unavailable) — flag lower confidence. Given short-gamma + a Tier-1 print, the honest read is **small or stand-aside**.

## 2a. Swing Dealer Positioning (1–4 weeks)

`dealer-positioning-strategist`: the indices are in a **sustained dealer-short-gamma regime, NOT a vanna squeeze.** SPY/QQQ/IWM all FULLY_NEGATIVE, DEX deeply put-heavy (SPY −20.99B, QQQ −1.55B, IWM −5.05B), GEX deteriorating off the late-May positive shelf (SPY +1.76B on 6/2 → −1.74B on 6/9). Net charm is negative across the board → put-side charm bleed adds **downward** delta-hedge pressure into the 6/19 OPEX.

**Why it is NOT a vanna squeeze (disqualifier applied):** every index shows a put-heavy book (positive net vanna) — the *first* half of a squeeze setup — **but VIX is 19.87 and elevated, not falling.** Put-heavy book + rising/elevated VIX = *vanna pressure (downside-hedge fuel)*, not a squeeze-up trigger. `vanna_squeeze_flag = FALSE` on all names. **Reversal trigger to watch:** if VIX *collapses* post-FOMC (6/17), these same put-heavy books flip into genuine squeeze fuel — that is the regime hinge.

| Name | DEX | Regime flip | Vanna | swing_bias (1–4wk) |
|---|---|---|---|---|
| **SPY** | −20.99B put-heavy | 6/05 → FULLY_NEGATIVE, held 4 sessions | put-vanna +145k (pressure, VIX elevated) | **SHORT** (cleanest) |
| **QQQ** | −1.55B put-heavy | 6/05 (Tech outflow −615M confirms) | +51.6k (pressure) | **SHORT** |
| **IWM** | −5.05B put-heavy | 6/04 (deepest, whippiest ZGL history) | +97.3k (pressure) | **SHORT (lighter)** |
| **MSFT** | −2.87B put-heavy | GEX negative −6.9M **6/9 ONLY** | +12.4k | **SHORT (watch — needs 2nd-session confirmation)** |
| MU / GOOGL / NVDA / TSLA | call-heavy POSITIVE-gamma | none | short (call-heavy) | **NEUTRAL — disqualified** (dealers dampening; MU put flow is being *absorbed*, not amplified) |

## 2b. Sector Rotation

`sector-rotation-strategist`: **rotation_regime = `no_change` (low confidence).** No canonical pattern. The rotation-**out** side is clean and persistent (**Technology** — XLK −11.5M, IGV −24.8M, both 5-day BEARISH, confirming the synthesis −615M Tech delta), but the rotation-**in** side forms **no coherent defensive or value cluster**: Healthcare (XLV +3.8M) and Staples (XLP +7.2M) lean in, but Utilities (XLU −2.5M) leans *out* alongside Tech, breaking the defensive thesis, and Industrials (the synthesis's top momentum-in sector, +54M) shows its ETF **XLI −3.2M BEARISH** — GICS and ETF disagree. This is **idiosyncratic de-grossing of Tech, not a regime rotation.** DTE share BALANCED (not retail-chasing) → the Tech-out signal is institutionally credible.

> GICS `sector-flow-persistence` is **degenerate today** — every sector scored persistence 1.0 (net-call positive all 5 days, zero discrimination) — so the read rests on the synthesis momentum delta + the ETF tape.

**ETF flow tape (advisory — strengthens no rubric points; no sector-leader +1 awarded, no name cleared the $50M cum-flow floor):**

| ETF | Net premium | Persistence | DP / options tell | GICS agreement | Note |
|---|---|---|---|---|---|
| **XLP** | +7.2M inflow | BULLISH | Sep-78p $8.9M hedge underneath | agree (Staples) | DP buying but put-hedged — mixed |
| **XLV** | +3.8M inflow | BULLISH | rank-only | agree (Healthcare) | Cleanest persistent inflow; leaders RVMD/HUM/ABBV |
| **GDX** | +9.7M inflow | BULLISH | DP below mid + Sep-80p $10M bid | agree but **tape contradicts** → downgrade | |
| **SMH** | mixed (+28.5M on $1.05B base) | MIXED | mega DP $99M block + **put-dominated** Jul sweeps $90M+ | agree (Tech) → **bearish tilt** | Semis hedged |
| **IGV / XLK** | −24.8M / −11.5M outflow | BEARISH | DP below mid, heavy put sweeps | agree (Tech) ✓✓ | Confirms Tech-out |
| **KRE** | −21.6M outflow | BEARISH | $130M redemption block + **bid-side call** sweeps | agree (Financials) → downgrade (mechanical) | Don't initiate a short until call-bid clears |

**Swing-book implication:** no regime trade. Tactical only — fade Tech bounces (XLK/IGV hedged under positive headline call premium). Industrials single-names (GWW/CAR/VRT/BE) are strong but **ETF-unconfirmed** → trade as idiosyncratic, not a sector bet.

---

## 3. Swing Setups (1–6 weeks)

**Ranked by conviction. After the full gate stack, nothing carries swing size today.** The table below is the gated book; the lone live position is a starter SPY short.

| Ticker | Dir | Score / Tier | Pre-risk | Gates applied | **Final size** | Invalidation |
|---|---|---|---|---|---|---|
| **SPY** | SHORT | 4 / LOW | half | event_risk −1 (CPI T+1 + FOMC T+5) | **STARTER (~0.25R)** | Reclaim 20sma (746) / gamma flips +GEX / dealer DEX turns net-long |
| **IWM** | SHORT | 4 / LOW | starter | cluster −1 (SPY/IWM 0.885, SPY kept) + event_risk −1 | **SKIP** | n/a — redundant to SPY, WR 0.333 |
| **MSFT** | SHORT | 4 / LOW | half | fundamentals −1 (CAUTION) + event_risk −1 | **SKIP** | Needs ≥2 more sessions confirming the 6/9 DEX/GEX flip |
| **CZR** | LONG | 3 / LOW | starter | regime −1 (long fights pullback) + wrong-expression | **SKIP** (if expressed, own common) | Deal-break / antitrust headline → re-rate to ~$20 |
| **MU** | SHORT | 0 / drop | — | **fundamentals VETO** | **WATCH-ONLY** | — |

### 3a. Long swings (regime-aligned)
**None sized.** The only clean accumulation flag of the day was **CZR**, and the fundamentals gate reframed it as a **merger-arb** (§6) — not a directional long. `uw historical trend` confirms 8-of-10 bullish flow days and a grind from 29.2 → 29.45 toward the $31 deal price, but **IV rank is 3.78** (vol dead — the name is pinned to the binary deal outcome, which is exactly why the flagged **July $30 calls are a theta-dead expression**). KVUE (DP buy/sell 4.9) was a Tier-2 near-miss but its only OI build is protective puts — OI does not confirm the long. SNDK / NVDA carried bullish flow but both dropped (SNDK raw 2; NVDA raw −1 on a clean −$157.9M flow_conflict against the long).

### 3b. Short / fade swings (defined risk only)
The regime-aligned side, but **gated out by event risk**. SPY short is the lone survivor (starter). MSFT short is fundamentally fought (4/4 beats, 47% margin, analyst recom 1.24) and rests on a *single unconfirmed* dealer flip → skip. **MU** carried the desk's strongest bearish *microstructure* co-flag — Tier-1 OPENING_PUT_PRIME (905P, size/OI 5.86, +26pp) ∧ mega-tier DP distribution (br 0.094, $1.6B) — but it is **VETO'd**: 4/4 beats, +85% rev / +412% EPS into an **imminent 6/24 earnings binary (IVR 100)**, and the dealer book is positive-gamma (absorbing the puts). If the desk wants the valuation-extension downside (price 11% above consensus target, +174% YTD), it belongs as a **defined-risk pre-6/24 put-spread, not an outright short.**

**`contrarian-scanner`: NO QUALIFYING FADES.** The entire crowded-mega-cap universe (MU, TSM, AMD, MRVL, MSFT, AMZN, AAPL + all IVR-100 semis) is in **BACKWARDATION into the CPI/PPI/FOMC stack** — structural event-vol insurance, not crowded euphoria, and the rubric forbids fading it. The statistical extremes that *did* fire (TSLA z+3.85, AAPL z+2.09, IONQ z+3.02) are all **BEARISH_EXTREME** (crowd buying puts) with aligned bearish flow + Tier-1 whale puts — nothing to fade. **Re-arm post-FOMC (Jun-18+):** MU/TSM/AMD/MRVL carry the divergence + IVR-100 + whale interest; the only missing ingredient is contango, which the event stack is suppressing.

**Near-term sweeps** (`sweep-tracker`, informational): the 5-day persistence book is **overwhelmingly bearish hedge-flow** — SPXW/QQQ/SPY 5/5 bearish but with *balanced 30d cum_flow* (not directional — pure index hedging into the print). The two genuinely scorable bullish persistent names, **MRVL (5/5 call build)** and **SNDK (4/5)**, are contested: MRVL's bullish call OI is being **closed** on the tape (decrease-with-volume 230C −1,866 / $30M, 280C −560) = distribution dressed as a sweep — the quant flagged it (`distribution_flag=TRUE`) and dropped it to raw 1.

---

## 4. LEAP Builds (6–24 months)

**No clean LEAP build today.** `leap-positioning-radar` returned zero names passing the strict 6-of-9 gate set with the required conviction (>70) and persistence (build-days ≥5). LEAP share of volume was 4.8% (genuinely thin), and the long-dated book was **hedging-heavy/bearish**: QQQ P725 dte373 ($66.7M ask-side), TLT P80 rate-hedge, IREN P20/P15 dte829 ($13.8M, contradicting its call note), CCL/AAL/LASR puts.

**Single near-miss — UNM (watch, not sized):** C105 dte192 build (+9,637 OI, $2.25M ask-lean), cum_flow 90d +$2.48M / 30d +$2.39M (fresh-thesis), DP accumulation buy/sell 2.04 defended at $88. **Clears 6 of 9 gates but fails the two that define LEAP-grade:** conviction-matrix confidence **56.9 < 70** and consecutive build-days **3 < 5** (the LEAP build is a one-day spike). Re-check tomorrow for build-day continuation + a conviction lift above 70. Mega-caps NVDA/AMD/ARM/VRT show 10-day builds but **no dte>180 contracts** — swing-horizon, not LEAP.

---

## 5. Volatility Surface

`vol-surface-scout`: the surface is **saturated by the macro week** — every name classifies BACKWARDATION with front IV lifted by CPI/PPI/FOMC, so the tag alone is noise. The signal is the **back-month kink shape** — which names re-elevate IV at a *specific later expiry* (real single-name earnings) vs a monotone-decaying front (pure macro). VRP is FAIR at the index → size event trades on the kink, not on a vol-direction bet.

**KINKED with catalyst (earnings-scout hand-offs):**

| Ticker | Earnings | Implied move | VRP | FEIR (panic) | Back-mo skew | Verdict |
|---|---|---|---|---|---|---|
| **ORCL** | 6/10 AMC | 10.6% | +0.057 | 2.28 (extreme) | −0.064 COMPLACENT | **SKIP short** (binary cloud/AI print — *own* vol, don't sell; speculative BUY-VOL only) |
| **ADBE** | 6/11 AMC | 8.0% | +0.126 | 2.23 (extreme) | −0.020 COMPLACENT | SELL VOL post-event only (6/12 IC ±8%); SKIP pre-print |
| **JBL** | 6/17 BMO | 4.4% | **+0.157 (richest)** | 1.13 (no panic) | −0.004 COMPLACENT | vol-surface: cleanest sell-vol; **earnings-scout: SKIP** (flow one-sided PCR 4.05) — split read |
| **ACN** | 6/18 BMO | 3.5% | +0.132 | 1.26 | **+0.026 NORMAL** (only put-bid skew) | **SELL VOL — HALF SIZE** (cleanest kink-at-earnings, tail also priced) |
| **KMX** | 6/17 BMO | 11.4% | — | 1.75 | **+0.047 NORMAL** | **SELL VOL — HALF SIZE** (sharp standalone 6/18 kink) |

**No full-size SELL VOL exists** — flat back-month skew (downside tail unpriced) + macro contamination caps every short to half. The extreme-FEIR names (ORCL/ADBE/RH/CHWY > 2.2) are explicit "do not short into the panic."

**Calendar candidate — MU (only one):** 7/10 → 7/17 (front IV 110% below back 147% = clean calendar at the fiscal-Q3 earnings kink). **Sell 7/10 trough, buy 7/17 kink** — VRP-neutral by construction (single-name VRP −0.029 forbids a naked short). The semis complex back-month skew is **COMPLACENT (call-rich)** — MU the standout (retail chasing calls into the print), which argues *against* paying up for MU upside calls.

**IV outliers:** none actionable — the tape is fully absorbed by SPY/QQQ 0DTE/2DTE index macro-hedges; the 3 non-index survivors are micro-cap/penny-strike junk. **NXPI explicitly excluded from any premium-sale: VRP −0.34 (vol cheap) → a buy-vol name, not a fade.**

---

## 6. Risk & Correlation

**Macro headline:** restrictive and worsening (10Y 4.56% rising, USD strengthening, Core PCE 3.29% sticky) into a **Tier-1 event gauntlet — CPI Jun-10 (T+1), PPI Jun-11, FOMC+SEP Jun-16/17 (T+5).** Every swing sized today is held over both windows; the event-risk gate is the dominant gate and fires −1 tier on all directional swings.

**Breadth cross-check (advisory):** `fz` shows **371 advancers / 131 decliners (73.8% green)** against `uw` 35%-bullish options flow — a **distribution / hedged-rally divergence** (green price, defensive flow). Does not change sizing; reinforces the light, short-biased posture.

**Correlation clusters (`uw risk portfolio-correlation`):** **`index_highbeta_cluster` FIRES** — SPY/QQQ **0.914**, SPY/IWM **0.885**, IWM/QQQ **0.771**. SPY/IWM (and QQQ context) are **one position**. Kept member: **SPY** (highest market-excess +0.19, WR 0.545); IWM dropped (−1 tier, WR 0.333). **CZR is the genuine uncorrelated diversifier** (merger-arb, deal-pinned, sub-0.50 to everything).

**Fundamentals verdicts (top names):**
- **CZR — CONFIRM (0).** Reframed as **merger-arb**: signed $31.00/share all-cash Fertitta deal ($17.6B, 5/29, 49% premium), **outside close May-2027 (extendable Nov-2027)**. Standalone fundamentals (4/4 EPS misses, D/E 7.1x, −4.2% margin) are **moot** under a fixed cash price — the "accumulation into a deteriorating balance sheet" alarm is a deliberate false positive. **Key risk = deal-break / antitrust** (HSR + multi-state gaming approvals, likely property divestitures) → re-rate toward ~$20 / 52w-low 17.86. Asymmetry: capped **+5.3%** vs **~−30%** break tail; ~5–6% annualized over a 12-month clock.
- **MSFT — CAUTION (−1).** Fundamentals fight the short: 4/4 beats, +18% rev / +30% EPS, 47% op margin, D/E 0.26, analyst recom 1.24 / +38% to target, RSI 41.8 (much already priced). The short rests on a single unconfirmed 6/9 dealer flip inside a macro tech selloff.
- **MU — VETO → watch-only.** Full 3-of-3 contradiction (4/4 beats, +85% rev / +412% EPS, 48% margin) into an **imminent 6/24 earnings binary (IVR 100)**. The bearish DP-distribution + Tier-1 whale put are real but the 30d tape (+$76.9M) and dealer book both lean against the short; the quant already dropped it to raw 0.
- SPY / IWM / QQQ — NA (index ETFs).

**Debate (CZR):** bull residual **0.85** > bear **0.65** → **no debate size-cut.** Both sides converge: real-but-low-IRR arb, capped, and the July $30 calls are the wrong instrument (deal closes 2027 — own common). Bear's strongest unrefuted point: a committed all-cash buyer ($450M reverse-termination fee, no financing condition) makes a slow grind to $31 likelier than a break — it's a capital-efficiency kill, not a break thesis.

**Adverse-flow exit list** (vs yesterday's `conviction_2026-06-08` long-semi book): **MU, MRVL, LRCX, AMD all flipped bearish** into rich vol overnight (MU net −$122M IVR 100; MRVL −$22.9M IVR 90; AMD −$41M IVR 95) — **the long-semi book is being distributed.** META the lone survivor (bullish +$2.5M, thesis intact). This semi-distribution corroborates the index/tech short bias.

**Hedge sleeve:** **none needed.** The gated book has no net long skew — the only live exposure is a single SPY short starter (≈ short delta), already its own hedge. Directional skew well under the ±0.6 trigger. *If* the desk overrides and adds long-semi off the carried names, a 1-week QQQ put spread or VIX 22/28 call ladder into FOMC would be warranted.

**Book-level posture:** **Carry near-zero directional risk into CPI. Net new swing exposure ≈ 0.25R, SPY short starter only.** FULLY_NEGATIVE short-gamma is double-edged over the print — a hot CPI amplifies down (good for the short), a cool/in-line CPI triggers a mechanical dealer squeeze *up* that runs over a starter short fast. That asymmetry is why this is a starter, not a half. React to CPI; don't pre-position.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**None this run.** The quant produced **no HIGH (≥9) or MEDIUM (7–8) names** — the entire surviving slate is LOW tier (raw 3–4), consistent with the 35%-bullish defensive breadth and the event-week hedging tape. The Step-3a HIGH-tier load-bearing-tool gate and the win-rate full-size gate are therefore moot.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no closed-call expectancy table is surfaced (no HIGH/MEDIUM book to size; live sizer remains the win-rate ladder). Per-tier expectancy from the most recent `/calibration-audit` (2026-06-06) stands: HIGH (≥9) realised ~0.77, MED (7–8) ~0.54 — neither bin is populated today.

**LOW-tier audit detail (the four survivors + the marquee drops):**

| Ticker | Dir | raw | score_components | dom. class | win_rate (n, src) | pre-risk | fund. verdict | bull/bear | gates | final | invalidation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **SPY** | SHORT | 4 | +3 dealer DEX (dealer-positioning / `options-structure dex`), +1 cum_flow_30d −$1.15B (`cumulative-premium-flow`) | dealer_short | 0.545 (11, backtest proxy) | half | NA | — | event −1 | **STARTER** | reclaim 746 / +GEX flip |
| **IWM** | SHORT | 4 | +3 dealer DEX, +1 cum_flow_30d −$231M | dealer_short | 0.333 (6) | starter | NA | — | cluster −1, event −1 | **SKIP** | — |
| **MSFT** | SHORT | 4 | +3 dealer DEX (6/9 only), +1 cum_flow_30d −$76.5M | dealer_short | 0.50 (6) | half | CAUTION | — | fund −1, event −1 | **SKIP** | 2nd-session flip confirmation |
| **CZR** | LONG | 3 | +1 accum (halved, `institutional-accumulation`), +1 OI build (`oi-trend`), +2 confluence 5 (`signal-confluence`), −1 flow_conflict_lite | dark_pool_accumulation (→ merger_arb) | 0.50 (0, fallback proxy) | starter | CONFIRM | 0.85 / 0.65 | regime −1, expression | **SKIP** | deal-break → ~$20 |
| MRVL | LONG | 1 | +1 OI build only (+1 cum_flow **screened to 0** by `distribution_flag=TRUE`) | multi_day_sweep | 0.00 (1) | — | — | — | — | **DROP** (distribution) | — |
| MU | SHORT | 0 | accum +1 halved, −1 flow_conflict_lite (no dealer +3 — disqualified) | bearish_flow / single_leg_put | 0.438 (16) | — | **VETO** | — | — | **WATCH** | earnings 6/24 |
| NVDA | LONG | −1 | +2 multileg (`hot-chains multileg`), **−3 flow_conflict** (−$157.9M vs long) | multileg_directional | — | — | — | — | — | **DROP** | — |

**Σ-invariant:** every call's `score_components[]` sums to its `raw_score` (validator-enforced).

**Conviction-scoring rubric (Step 4, verbatim):**
```
+3  dealer-positioning DEX flip / vanna-squeeze in trade direction
+3  3+ aligned accumulation signals (DP+OI+smart-positioning, block-stratified institutional-tier)
    — CONJUNCTION: full +3 only when cum_flow_30d confirms (sign aligned AND |cum_flow_30d|≥$50M); else halved to +1
+1  multi-day OI build (oi-trend BUILDING, days≥5)
+1  conviction-matrix DIRECTIONAL_LONG conf>70 — CONDITIONAL: only when dominant_signal_class==leap_directional; else 0
+1  cum-premium-flow net directional accretion in trade dir (30d) — INTENT-SCREENED: 0 if distribution_flag present
    or deep-ITM sub-parity dividend-capture calls
+2  signal-confluence ≥4 (second-agent confirmation)
+1  sector-rotation names ticker as single-name leader — CONDITIONAL: persistence≥0.6 AND cum_flow_30d aligned AND ≥$50M
+1  earnings-scout BUY VOL or SELL VOL
+2  multileg-strategist directional structure (term-structure-anchored)
+1  vol-surface-scout KINKED/BACKWARDATION watch with VRP-aligned bias
-2  contrarian overcrowded long w/ rising pc-ratio-zscore (VRP positive)
-3  flow_conflict — cum_flow_30d clearly OPPOSITE dominant_signal_class (sign flip + magnitude > union-median, or OPPOSITE)
-1  flow_conflict_lite — 30d cum_flow MIXED (near zero, or aligned but bottom-quartile magnitude)
    (flow_conflict and flow_conflict_lite are mutually exclusive — apply ONE)
-1  correlation cluster (corr>0.7) — applied in 2d
-3  market-regime conflicts with trade direction — applied in 2d
Tiers: ≥9 HIGH (full) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 drop.
```

---

## 8. Watch-only — single signal, no confluence

For journaling, **not** for entry today:
- **SNDK** (raw 2) — bullish 4/5 sweep persistence + opening_confirmed OI build (+23,954) + net-premium bullish leader; no second-agent confluence. Largest aligned flow (+$1.16B). Carried to the watchlist for tomorrow's correlation loop.
- **KVUE** (raw 2) — DP accumulation 4.9 ($78.5M block) + confluence 5, but the only OI build is protective puts (OI does not confirm the long).
- **UNM** — LEAP near-miss (6-of-9 gates; conviction 56.9 < 70, build-days 3 < 5). Re-check for build continuation.
- **ACN / KMX / JBL** (raw 2 / 1) — SELL-VOL half-size candidates if the desk wants single-name event-vol post-FOMC; not directional.
- **GWW / CAR / VRT / BE** — Industrials single-names, strong but ETF-unconfirmed → idiosyncratic only.
- **ORCL** — speculative BUY-VOL into tomorrow's 6/10 AMC print (binary cloud/AI guide); do not sell its vol.

---

### Watchlist write-back
`conviction_2026-06-09 = [SPY, IWM, MSFT, CZR, SNDK]` — written (top-5 by raw_score, VETO'd MU excluded; SNDK as highest raw-2 by aligned flow). Tomorrow's run measures correlation + adverse-flow vs these. Exit-tagged off `conviction_2026-06-08`: MU, MRVL, LRCX, AMD (adverse reversal / distribution).

*No HIGH-tier names → no `/stock-deep-dive` hand-off this run (per the no-edge-day rule).*
