# Daily Market Analysis — 2026-05-28

## Executive Summary
- **Regime + GEX state:** **TRANSITIONAL** ("reduce size, defined-risk, iron condors in range") over a TREND **UPTREND** — SPY 754.6 (>20/50-SMA, +6.0% 30d, −0.07% off 90d high), VIX **15.74 (LOW)**. SPY & QQQ both close **long-gamma** (pin-favorable). Breadth is the tell: flow-breadth 40.6% bullish and `fz` **pct_green 47.3%** (238 adv / 264 dec, median −0.07%) — a **narrow-participation / distribution divergence** under the green index. Sector flow is broad risk-on (all 11 GICS sectors persistence 1.0 INFLOW, Tech-led $35.5B 5d) but the ETF tape shows an **intra-Tech rotation: software (XLK/IGV) IN, semis (SMH −$65.3M) OUT.**
- **Next-session GEX (SPY/QQQ):** *advisory, see §2.* **SPY** long-gamma, ZGL 754.31 (reliable, spot sits *on* it) · call wall 755 (huge +$535M) · put wall 740 / floor 730 → **pin 754–755 if it opens ≥754; a gap below re-arms short-gamma toward 740** (regime flipped only today — fragile). **QQQ** long-gamma (stable 6 sessions) · ZGL unreliable · call wall 736 · flip ~728 → **cleaner 736 pin.**
- **Top swing build:** **ASTS** (AST SpaceMobile) — dark-pool accumulation +$89.3M 30d + opening-confirmed +134k call-OI build + 20% short-float squeeze, raw 8/MEDIUM, win_rate 0.65 (proxy). **Cut to STARTER** by fundamentals CAUTION (insiders selling −9.7%, analyst target −33% below spot, RSI 78) + a debate that did not clear (bull 0.65 = bear 0.65). Structure: **bull put spread** below the $128 DP shelf (sell the 119% IV, don't buy it). The only directional long with genuine confluence today.
- **Top LEAP candidate:** **None.** The DTE>180 tape is index hedges (QQQ Dec puts), LEAP puts (MCHP), and sold strangles (SPX) — no slow-accretion directional long cleared 6-of-9 gates + conviction>70. Watch AMD (cleanest LEAP call ladder, but MIXED conviction).
- **Biggest risk:** No correlation cluster ≥0.70 (SMH/MU 0.69 soft-watch only). The live risk is **macro event stacking** — NFP 06-05, CPI 06-10, FOMC 06-16/17 — into an overbought, negative-gamma-prone semis complex on thin breadth. **AAPL flagged as an adverse-flow exit** (flow flipped bearish vs yesterday's long). No hedge sleeve required — the book is tiny and near-flat (SMH starter short ⊕ ASTS starter long).

> **Day verdict: low-edge, defensive.** Only **two names clear above watch, both at STARTER:** SMH (semis hedge) and ASTS (spec long, debate-cut). TRANSITIONAL already imposes a half-size baseline; nothing today earns a full-size slot.

---

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity"; trend UPTREND. SPY 754.6 (20-SMA 737.4, 50-SMA 701.8; +6.03% 30d; −0.07% from 90d high). Flow breadth 40.6% bullish (2,512 bull / 3,669 bear of 6,181 optionable tickers). Guidance: **half position sizes, defined-risk, iron condors in range.**
- **Per-index gamma (current-state EOD book; §2 carries the forward read):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 754.71 | 754.31 (reliable) | +$1.31B | POSITIVE (long-γ, **fresh/unstable**) | 755 (+$535M) | 740 → floor 730 |
| QQQ | 735.73 | null (unreliable) | +$0.74B | POSITIVE (long-γ, stable 6d) | 736 (cluster 735–740) | ~728 → support 715 |
| IWM | — | — | POSITIVE all 10d | POSITIVE (no flip) | — | — (front-end-iv 1.09 = hedged) |

- **`uw options-flow dte-volume-share`:** **BALANCED** — 0DTE 18.9% / weeklies 30.1% / monthlies 28.8% / LEAPs 7.1%. Monthly+ 35.9% = institutional-leaning, not a retail 0DTE tape.
- **`uw historical vrp`:** SPY **FAIR** (+0.031; IV30 13.2% vs RV30 10.0%) · QQQ **FAIR** (+0.049; IV30 20.7% vs RV30 15.8%). Mildly positive (IV>RV) but no strong premium-selling or premium-buying edge.
- **Macro backdrop:** `scripts/fred_macro.py` was **DEGRADED** today — FRED returned HTTP 504 on 11 of 12 series (two attempts). Only live print: **10Y Treasury 4.48%, RISING (+0.13 over 30d, from 4.35%)** — a mild headwind to long-duration/high-beta longs (ASTS 2.74β). Yield-curve sign, CPI/PCE YoY, payrolls, USD all unavailable; falling back to the regime label. **Forward `event_risk` (Tier-1, next ~10 td):** NFP **2026-06-05**, CPI **2026-06-10**, FOMC+SEP **2026-06-16/17** (just beyond the 10-day window). Weekly jobless claims Thursdays.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book (OI persists overnight) read forward as the *prior* for the 2026-05-29 open. **Prose-only, 0 conviction points, no backtested predictive claim** (predictive validation lives in `/weekly-analysis`). SPY/QQQ only.

**SPY — long-gamma but sitting ON the flip.** ZGL 754.31 vs spot 754.71 (0.05% — **reliable**), total_gex +$1.31B. The 755 strike is a wall in a class of its own (+$535M, 4.7× the next strike) → call wall + powerful pin magnet ~$0.30 above spot. Put wall / short-gamma flip begins at 740 (−$34M), deeper floor 730 (−$73M). **Asymmetry: pinned tight to the upside, a vacuum below 740.** Caveat: SPY only flipped NEG→POS *today* and has whipsawed across the ZGL on 3 of the last 5 sessions — **fresh, unstable**; a gap-down through 754 re-arms short gamma immediately.

**QQQ — stable long-gamma.** Reported ZGL 174.79 is **garbage (extrapolated, >76% from spot) → zgl_reliable=false**; fall back to +GEX sign + spot-vs-wall. Spot embedded in a thick positive 735–740 shelf; call-wall/pin 736 (+$154M), flip ~728, support 715. Negative gamma below is thin/scattered → weaker downside-trend potential than SPY. QQQ has **held POSITIVE 6 straight sessions** — a cleaner, more established pin than SPY.

**Structure bias (next-session 0DTE):** both long-gamma with pin magnets essentially on spot → **mean-revert / vol-suppression / pin** favored (consistent with §2a GO + VIX 15.74). SPY-specific caution: gap-down through 754 flips it to short-gamma/trend fast.

**Mandatory caveats:** EOD is a *prior*, not a target — fresh 0DTE OI re-computes the map in the first 30–60 min. ZGL reliable for SPY, unreliable for QQQ (sign+wall fallback used). No scheduled macro overnight (NFP 06-05 is the next), but any unscheduled gap through SPY 754 / QQQ 728 voids the pin. This is the **ETF** book, not the cleaner SPX/NDX index book. `uw` cannot isolate the D+1 expiry (`gex --dte-max 1` errors) — standing 0–45 DTE proxy.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — the validated stack)
The walls above are a **map, not a pin to trade** (wall-as-magnet + every directional 0DTE signal backtested NO_GO). What validated is a **delta-neutral premium-selling** edge. Advisory, **0 conviction points**, NOT a guaranteed edge (validation sample has no vol shock → short-vol tail unsampled).

| Index | Sell premium? | Vol state | Implied/expected range | Size scalar | Suggested structure | Entry |
|---|---|---|---|---|---|---|
| **SPY** | **Yes** | LOW (VIX 15.74) | ±0.72% | 0.5 | iron fly / short straddle centred **755.45**, wings ≈ ±0.72% (long-γ: quieter) | at/after open once gap resolves; hold to close, never overnight |
| **QQQ** | **Yes** | LOW | ±1.2% | 0.5 | iron fly / short straddle centred **736.25**, wings ≈ ±1.2% | same |

Rolling backtest verdict: **GO_PREMIUM_SELL_INTRADAY** (SPY 97.0% open-win n=33; QQQ 93.9% n=33). VIX LOW = **thin edge → size 0.5, no stand-aside today.** SPY ≈ SPX (validated identical — trade either); **QQQ weaker** (Nasdaq index book unavailable — lower confidence). Direction: **none** (delta-neutral). Stand aside if it gaps beyond the wings.

## 2a. Swing Dealer Positioning (1–4 weeks)
`dealer-positioning-strategist`: **NEUTRAL across the entire board.** Books are **call-heavy everywhere** (positive DEX, negative net vanna) — the *inverse* of a vanna-squeeze setup. **No DEX sign-flip on any name.** With VRP FAIR and a low/falling VIX, the vanna mechanic leans dealer-*selling*, not a self-reinforcing rally. **No name carries a LONG or SHORT swing dealer-positioning tag today.**
- **SPY** NEUTRAL — 3 GEX regime flips in 10d (05-22/05-27/05-28) = chop, not a tradable flip.
- **QQQ** weak NEUTRAL-LONG advisory — one clean 05-22 NEG→POS flip, POSITIVE 6 sessions (positive-GEX grind-up, no accelerant).
- **SMH** NEUTRAL, flagged **"vanna pressure / vol-expansion risk, NOT a squeeze"** — FULLY_NEGATIVE gamma 6/10 sessions, front-end-iv **1.83** (deep backwardation), put-heavy on DP/pcr — a 1–2wk vol-expansion *hazard to monitor*, not a directional short (no DEX flip). Elevated single-name front-end ratios (MU 1.45, AMD 1.33, IWM 1.09) = front panicked → caution on chasing, consistent with the breadth divergence.

## 2b. Sector Rotation
`sector-rotation-strategist`: **rotation_regime = `no_change`** (regime_confidence low). Every GICS sector prints persistence 1.0 INFLOW (Healthcare 0.8); no sector in persistent outflow → **broad risk-on beta, Tech-led leadership, not a clean macro rotation.** No defensive sector is bleeding (XLU/XLP/XLRE marginally positive). Breadth divergence (pct_green 47.3% vs flow-breadth 40.6%) confirms the beta is **narrow** — mega-cap concentration. The actionable edge is **intra-Tech**, visible only at the ETF-instrument layer.

**ETF flow tape (advisory — 0 rubric points):**

| ETF | Net premium dir | Persist | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| **XLK** +$21.4M | inflow | BULLISH 5d | $276M DP (below-mid = hedge) | call-skew sweeps 4.83/3.12 | **agree** (Tech) | MSFT, ORCL, PLTR |
| **IGV** +$19.4M | inflow | BULLISH 5d | $93M DP balanced | call-skew 6.85/2.34 (strong) | **agree** (software) | ORCL, SNOW, NOW, CRM |
| **XLI** +$16.6M | inflow | BULLISH 5d | $238M DP (hedge) | no sweeps (flow only) | **agree** (Industrials) | UNP, CAR, AXON |
| **SMH** −$65.3M | **outflow** | BEARISH 5d (largest) | $186M DP | **put-skew sweeps 23.85/66.21** | **disagree** (GICS Tech inflow) → watch-only | semis de-risking |
| GDX −$7.3M | outflow | BEARISH 5d | $83M DP above-mid | call-skew 8.29/0.36 (conflict) | disagree → watch | mixed |
| XOP −$4.0M | outflow | BEARISH 5d | $26M DP | mild call-skew | disagree → watch | — |

**Headline:** XLK/IGV software (+$40.8M combined, call-sweep urgency) vs **SMH −$65.3M with heavy put-sweep urgency** — both Technology-GICS. The aggregate's "Tech 1.0 inflow" masks an **intra-Tech rotation: large-cap software/platform IN, semis OUT** — invisible to the GICS layer, the highest-information signal on the tape. SMH/XLK *disagree* → **watch-only** until a 2nd session confirms semis-specific de-risk vs index hedging. Swing implication: long software leaders (MSFT, ORCL, IGV-basket) into a Tech-led tape; SMH put-sweep urgency is the one short/short-vol candidate. **Size leaders individually — beta is narrow, do not chase the basket.**

## 3. Swing Setups (1–6 weeks)

### 3a. Long swings (regime-aligned)
| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **ASTS** | 8 (MED) | Dark-pool accumulation +$89.3M 30d (≈90d → fresh build), opening-confirmed +134k call-OI 5d, DP support $128 vs spot $133, 20.2% short float (MODERATE squeeze fuel). Real catalyst stack (SpaceX-IPO proxy, UFO ETF >$1B, NASA event, 2X ASTY fund). | **Bull put spread** below ~$128 DP shelf (batch-scan: HIGH_IV+BULLISH_FLOW → sell the 119% IV, defined risk; do NOT buy premium) | Close below DP VWAP ~$128 / accumulation-shelf break, or insider-selling acceleration, or dilutive raise headline | **STARTER** (cut from half: fundamentals CAUTION −1 + debate not cleared −1) |

*Note: ASTS is the only directional long with genuine ≥2-agent confluence today. The debate flagged that 6-of-8 raw points are one double-counted accumulation/cum-flow confluence in the single class (`dark_pool_accumulation`) whose `uw` backtest returned empty — the 0.65 win_rate is a borrowed proxy. Spec name, size accordingly.*

**Sector-beta menu (watch-only — broad beta, no idiosyncratic edge):** MSFT (CONFIRM fundamentals — 4/4 beats, Dell/DoD $9.7B tailwind — but market_excess −0.12 = pure UPTREND beta, raw 4), ORCL (**dropped −3 flow_conflict**: cum_flow −$158M opposes long despite the software-leader tag + BULLISH_EXTREME complacency), PLTR (sub-floor: cum_flow +$34M <$50M gate), UNP (Industrials leader but cum_flow −$2.3M opposes).

### 3b. Short / fade swings (defined risk only)
| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **SMH** | 12 (HIGH) | Semis de-risk **hedge** (NOT a conviction directional short): FULLY_NEGATIVE gamma 6/10d, front-end-iv 1.83, put-skew sweeps 23.85/66.21, OI +97k puts, pcr 7.26, IV-rank 84.6, largest ETF outflow −$65.3M (intra-Tech rotation out of semis). 6/10 bearish flow days, today −$21M. | **Bear call spread** above spot (batch-scan: HIGH_IV+BEARISH_FLOW → sell call spread; defined risk) — the book's defensive expression on a parabolic semis tape | SMH reclaims/holds prior-day high with pcr normalizing <1.5 and IV-rank rolling off 84 → hedge thesis broken, cover | **STARTER** (win_rate 0.49 sub-floor; hedge, not conviction; all gates no-op) |

*The semis short is the most cross-corroborated thesis on the tape (sector outflow + 3-day-repeat 550/530 put spread + negative-gamma mechanics + breadth divergence) — but the originating dealer desk disowned the gamma as directional ("vol-expansion hazard, not a short"), and the directional backtest is sub-coin-flip. Its EV lives in path/vol convexity + the rotation, not a clean directional bet. Hold as a defined-risk hedge into the macro window.*

**Near-term sweeps (`sweep-tracker`, informational — 0 points):** the tape was **hedge-dominated**, not momentum. Whale tickets were SPX deep-ITM 6000/7000 bid-side calls (synthetic-stock/overwrite) + SPY/SPX put ladders (collars). The **only clean directional sweep was ASTS** (4/5 persistence, opening-confirmed call-OI, +$153M 5d). Mega-cap cohort (NVDA/AMD/MSFT/TSLA/QQQ/AAPL/META) all failed the cum_flow-30d alignment gate = hedge-flow footnotes. No persistent sweep name appeared in the volume-vs-average top-30 (no confirming underlying-volume urgency).

## 4. LEAP Builds (6–24 months)
`leap-positioning-radar`: **NO QUALIFYING LEAP.** Zero names cleared 6-of-9 gates **AND** DIRECTIONAL_LONG conviction >70 **AND** the slow-accretion signature. The DTE>180 tape is risk-management flow, not directional accumulation — consistent with the breadth divergence.
- **BRKR** — closest (6 raw gates) but conviction only 31.9% (<70) and the LEAP OI build is sub-200 contracts / ~$1M (sub-institutional, fresh-thesis spike not multi-quarter accretion). → handed to accumulation-hunter (1–4wk horizon), not a LEAP.
- **TSLA** (281215C800 +14,976 OI, $114M) / **AMD** (clean LEAP call ladder out to 750 DTE) — large directional-call builds but **MIXED conviction** (5.5% / 2%) inside balanced two-way flow, no accretion. **Watch AMD** — promote if cum-flow flips BULLISH and conviction clears 65.
- Disqualified hedges/shorts: **QQQ 261218P660** (+98,514 OI, index put wall — the Step-0 hedge), **MCHP** LEAP puts (DIRECTIONAL_SHORT), **SPX** sold strangles (premium collection), **BULL** sold-to-open calls (DISTRIBUTION).

## 5. Volatility Surface
`vol-surface-scout`: **no tradable vol dislocation clears the gates today** — the surface is event-saturated. Index/broad (SPY/QQQ/IWM) = CONTANGO; single names = uniform BACKWARDATION with COMPLACENT (call-bid, tail-unpriced) back-month skew = the melt-up signature.
- **Front-end panic is RISING, not resolving** on SMH (1.84), MU (1.20), AMD (1.16) → **NOT tradable calendars; do NOT fade.** NVDA is the lone falling-panic name but its curve is cheap-and-flat (no front richness to sell) — note only.
- **S/SentinelOne** = textbook event crush (5/29 IV 365.8%, reports tonight) → earnings, not a vol sale. **No clean calendar candidate.**

**Earnings-vol plays (`earnings-scout`, single-agent → §5 watch, not in the conviction book):**

| Ticker | ER | Kink | Front-end | Back-skew | Flow vs analyst | Verdict |
|---|---|---|---|---|---|---|
| **CIEN** | 06-04 AM | +36.2pp | 1.67 | +0.080 stretched | bearish vs price 22% above target | **BUY VOL (put-tilt)** ★ |
| **VEEV** | 06-03 PM | +18.8pp | 1.00 FLAT | flat | bearish vs analyst +61% target | **BUY VOL** ★ (11.1% implied move) |
| **ADBE** | 06-11 PM | +9.4pp | 1.20 | flat | bearish vs analyst +32% target | **BUY VOL (build in)** ★ — next to CPI 06-10 |
| **HPE** | 06-01 PM | +21.1pp | 1.95 | −0.108 stretched | bearish, price above target | **SELL VOL (½ size)** — only clean short |

Board is otherwise structurally un-shortable (PANW FE 2.72, GTLB 5.22, MDT 3.10 trip the >1.10 front-panic disqualifier; near-universal flat back-skew blocks sized premium-selling). The 3 BUY-VOL names are all analyst-bullish / flow-bearish divergences — own the move, don't sell it.

## 6. Risk & Correlation
**Macro headline:** macro_snapshot DEGRADED (FRED 504s) — only 10Y **4.48% rising** usable (mild duration headwind). **Forward event_risk: NFP 06-05, CPI 06-10, FOMC+SEP 06-16/17** — three Tier-1 catalysts into an overbought, negative-gamma-prone semis complex; all five book names' earnings are 61–75d out (earnings gate **no-op**), so the macro calendar is the live event risk.

**Breadth cross-check (`fz`, advisory):** 238 advancers / 264 decliners, **pct_green 47.32%**, median −0.07% — **DIVERGENCE flagged**: more decliners than advancers under a green index in an UPTREND = a distribution / narrow-participation tell the single regime label hides. Advisory — does not change sizing, reinforces the defensive posture.

**Correlation (`uw risk portfolio-correlation` on today's union):** only flagged pair **SMH/MU corr 0.69** → 0.60–0.70 **soft-watch band, NO penalty** (and MU was already dropped; SMH-short vs MU-long aren't the same bet). **No pair ≥0.70 → cluster gate fires on nothing.** The expected SMH/MSFT/semis cluster did not materialize.

**Fundamentals verdicts (top-5):**

| Ticker | Verdict | tier_adj | Contradicting / confirming facts |
|---|---|---|---|
| SMH | **NA** | 0 | ETF — semis complex is the market leader, not broken (RSI 71, +55% vs 200DMA); put flow = protective hedge. NA never penalizes. |
| ASTS | **CAUTION** | −1 | Insider selling −9.74%, analyst target $88.75 = **−33% below** spot, RSI 78. 20.2% short float = MODERATE squeeze tailwind. Pre-revenue (4/4 EPS misses, structural). No VETO. |
| P/Everpure | **CAUTION** | −1 | **Issuer correction** — NYSE:P is **Everpure (AI-storage), NOT SiriusXM/Pandora**. Beat 05-27 but **gapped −16% on weak guide** — the DP accumulation ran *into* a binary that broke against it. Fundamentals healthy + PT raises → no VETO. |
| MSFT | **CONFIRM** | 0 | 4/4 beats, rev +18% YoY, Dell/DoD $9.7B MSFT-procurement tailwind, Recom 1.23 / +31% target. But pure UPTREND beta — confirms, doesn't manufacture edge. |
| BRKR | **CAUTION** | −1 | Flat growth +0.36%, thin/negative margins, RSI 81, analyst target **−9.6% below** spot. Real product catalyst (18T MRI) but accumulating above fair value. |

**No VETOs.** **Event-risk flags:** all earnings clear of horizon; NFP/CPI flagged for any *new* directional swing this week. **Debate cuts:** ASTS −1 (LONG, bear 0.65 ≥ bull 0.65 — not cleared); SMH none (SHORT, direction-aware: bear ≥ bull confirms the hedge, kept at starter). **Adverse-flow exits (vs `conviction_2026-05-27`):** **AAPL = exit-candidate** (flow flipped bearish, net −$2.35M, $818M DP block, vs yesterday's long thesis); IWM soft-watch (pcr 1.73 put-hedging building). TSLA/AMZN theses intact. **Hedge sleeve: none required** — book skew well under 0.6 (SMH starter short ⊕ ASTS starter long, offsetting and tiny). Optional small defined-risk SPY put vertical into NFP 06-05 if the desk wants macro cover; not mandated.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

### SMH — raw 12 · HIGH · SHORT/defensive hedge (ETF)
- **score_components:** +3 dealer-positioning/`options-structure dex` (FULLY_NEGATIVE γ 6/10d, front-end-iv 1.83) · +3 quant/`cumulative-premium-flow` (30d −$64.7M SHORT-aligned ≥$50M) · +2 multileg/`hot-chains multileg` (put spread 550/530, 3-day repeat) · +2 quant/`signal-confluence` (bearish confluence 4) · +1 sector-rotation/`sector-flow-persistence` (semis outflow −$65.3M) · +1 vol-surface/`term-skew` (front-end-iv 1.83 KINKED). **Σ = 12.**
- **dominant_signal_class:** bearish_flow · **confluence_score:** 4 · **cum_flow:** 30d −$64.7M / 90d −$100.1M
- **win_rate:** 0.49 (n=55, `backtest`) — sub-0.50 floor · **market_excess:** +0.205 (beats SPY-short)
- **LB-gate 3a:** 3/5 ✓ (cum_flow_30d, dex, signal-confluence≥4) → HIGH preserved
- **pre-risk:** starter · **fundamentals:** NA · **debate (bull resid):** 0.65 · **gates:** all no-op · **final: STARTER**
- **invalidation:** SMH reclaims/holds prior-day high, pcr <1.5, IV-rank rolling off 84 → cover.

### ASTS — raw 8 · MEDIUM · LONG (spec ~$133)
- **score_components:** +3 accumulation-hunter/`institutional-accumulation` (C11 conjunction FULL, cum_flow +$89.3M ≥$50M) · +3 quant/`cumulative-premium-flow` (30d +$89.3M LONG) · +1 sweep-tracker/`oi-trend` (opening-confirmed +134k call-OI 5d) · +1 sector-rotation/`sector-flow-persistence` (Comm-Svc leader). **Σ = 8.**
- **dominant_signal_class:** dark_pool_accumulation · **confluence_score:** n/a · **cum_flow:** 30d +$89.3M / 90d +$85.3M
- **win_rate:** 0.65 (n=26, `fallback_proxy` — `uw` backtest empty for dark_pool_accumulation; edge borrowed not measured)
- **pre-risk:** half · **fundamentals:** CAUTION (−1) · **debate (bull resid):** 0.65 (bear 0.65 ≥ bull → −1) · **final: STARTER**
- **fz_context:** 20.21% short float, 2.92 DTC (MODERATE squeeze), Recom 2.71 / target −33.3%, RSI 77.99 *(advisory, 0 pts)*
- **invalidation:** close below DP VWAP ~$128 / accumulation-shelf break / insider-selling acceleration / dilutive raise.

*LOW-tier watch (raw < 7, not sized): P/Everpure (4, CAUTION, issuer-correction adverse catalyst), MSFT (4, CONFIRM but pure beta), BRKR (3, CAUTION, flat-growth/RSI 81). All WATCH-ONLY.*

**Recommended deep-dive hand-off** *(the `/stock-deep-dive` skill is not available in this session)*: `Recommended deep dive: /stock-deep-dive SMH` (top HIGH-tier name) and `/stock-deep-dive ASTS` (top directional long).

### Conviction-scoring rubric (Step 4, embedded for audit)
```
Daily conviction score = Σ:
 +3 dealer-positioning DEX flip / vanna-squeeze in trade direction
 +3 3+ aligned accumulation signals (DP+OI+smart-positioning, block-stratified institutional) — C11 conjunction: full +3 only when cum_flow_30d confirms (sign-aligned AND |flow|≥$50M); else halved +3→+1
 +1 multi-day OI build (oi-trend BUILDING, ≥5d)
 +1 conviction-matrix DIRECTIONAL_LONG conf>70 — CONDITIONAL: only when dominant_signal_class==leap_directional; else 0
 +3 cum_premium_flow net directional accretion (30d)
 +2 signal-confluence ≥4 (second-agent confirmation)
 +1 sector-rotation single-name leader — CONDITIONAL: persistence≥0.6 AND cum_flow_30d aligned AND |flow|≥$50M
 +1 earnings-scout BUY VOL / SELL VOL
 +2 multileg directional structure (term-anchored)
 +1 vol-surface KINKED/BACKWARDATION with VRP-aligned bias
 -2 contrarian overcrowded long w/ rising pc-ratio-zscore (VRP+)
 -3 flow_conflict (cum_flow_30d clearly opposite class) | -1 flow_conflict_lite (MIXED) — mutually exclusive
 -1 correlation cluster (corr>0.7) [risk 2d] | -3 regime conflict [risk 2d]
Tiers: ≥10 HIGH (full) · 7–9 MEDIUM (half) · 3–6 LOW (watch) · ≤2 drop.
Sizing ladder (win_rate): ≥0.70 full · 0.50–0.70 half · <0.50 starter. C2 guards: n<10 cap 0.69; market-excess≤0 cap half / ≤−0.10 starter; bullish/bearish_flow not OI-opening-confirmed cap half.
```

## 8. Watch-only — single signal, no confluence
*Listed for journaling, NOT for trade entry today.*
- **P/Everpure** — accumulation + confluence-6 but fundamentals CAUTION (issuer-correction; −16% post-earnings gap already fired); raw 4, watch-only.
- **MSFT** — sector + bullish-leader but pure UPTREND beta (market_excess −0.12), no idiosyncratic edge; raw 4, watch-only.
- **BRKR** — block-tier accumulation + confluence-5 but flat growth / RSI 81 / analyst −9.6%; raw 3, flow_conflict_lite, watch-only.
- **CIEN / VEEV / ADBE / HPE** — earnings-vol plays (single-agent earnings-scout); surfaced in §5, not the conviction book.
- **PLTR** — sector leader but cum_flow +$34M < $50M gate; sub-floor.
- **AMD** — contrarian price-vs-flow divergence (price +86% vs flow −$29M) but no clean direction; accumulation REJECTED (late-stage); LEAP-watch.
- **UNP** — Industrials leader but cum_flow −$2.3M opposes long; sub-floor.
- **ORCL / MU** — dropped on flow_conflict (−3 each): ORCL cum_flow −$158M and MU −$447M both clearly oppose the bullish thesis. Mechanical deduction working as designed.
- **AAPL** — adverse-flow **exit-candidate** from yesterday's conviction group (flow flipped bearish).

---
*Generated by `/daily-analysis`. Phase 1: 10 alpha-finding agents (non-OPEX). Phase 2: quant → fundamentals-gate → bull/bear debate → risk-monitor. Watchlist `conviction_2026-05-28 = [SMH, ASTS, P, MSFT, BRKR]` persisted & verified. Decision envelope: `decision.json` (schema 1.1).*
