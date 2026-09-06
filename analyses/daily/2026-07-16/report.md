# Daily Market Analysis — 2026-07-16

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL (trend UPTREND) — SPY 750.72 above 20/50 SMA but −1.27% off the 90d high; breadth weak (37.2% bullish flow, fz 36.4% green under a flat tape = distribution tell). VIX 16.73 (LOW). **Both index gamma books read SHORT-GAMMA into tomorrow's monthly OPEX** (SPY total_gex −$1.15B, QQQ FULLY_NEGATIVE). Sector lean: Tech/Comm-Svcs inflow on the tape, but the *directional urgency* on semis is bearish (opening puts).
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`. Moot today — nothing sized.
- **Next-session GEX (SPY/QQQ):** SPY short-gamma (ZGL unreliable/broken, ATM 750 gamma pocket, call wall 760 / put support 740) → favor directional/long-gamma over ATM premium-selling. QQQ FULLY_NEGATIVE (no call wall, ATM 705 pocket, support 700) → long gamma or stand aside. Advisory, see §2.
- **Top swing build:** **None.** Zero names reached even LOW tier (top raw_score = 2). This is the 12th consecutive thin/no-edge conviction board.
- **Top LEAP candidate:** **None.** No name cleared the strict 6-of-9 LEAP gate (AAPL was closest at 6/9 but failed the required cum-flow accretion gate + carries near-dated earnings).
- **Biggest risk:** an **8-name semis/memory correlation cluster** (TSM/AMD/SNDK/MU/INTC/TXN/ON/COHR, pairwise corr to 0.93) — the entire bearish-semis theme is *one bet*, not five. Book is flat, so no mechanical hedge fires; advisory posture is a starter QQQ defined-risk put vertical as cheap-vol insurance into FOMC (QQQ negative VRP).

**Bottom line:** A no-edge OPEX-eve tape. The one genuinely interesting signal — the clean `bearish_flow` class carries +17.4pp excess over same-window SPY-short (n=132) right now, and TSM/AMD have aligned net-bearish 30d flow — but the frozen rubric's thin bearish scoring means no name accumulates enough points to trade. The rest of the tape is dominated by OPEX-week financing artifacts (an SPX box spread = ~99% of structured dollar tape, an MU conversion, a DRAM wash) and pre-earnings vol-sell setups into the late-July mega-cap cluster. Trade nothing directional; harvest nothing overnight.

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend UPTREND (SPY 750.72 > 20SMA 744.9 > 50SMA 743.99; −0.54% 30d, −1.27% from 90d high). Tool guidance: half sizes, defined-risk, iron condors in range. **Breadth is the tell:** only 2,340 bullish vs 3,957 bearish flow tickers (37.2% bullish) — a distribution skew hiding under an uptrending index.
- **Per-index gamma (current-state EOD 0–45d book):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 750.13 | 360.62 (broken/unreliable) | −$1.15B | **Short-gamma** (label POSITIVE but total_gex negative) | 760 | 740 (real support; 750 is an ATM pocket) |
| QQQ | 705.26 | null | −$1.15B | **FULLY_NEGATIVE** | none credible | 700 (705 is ATM pocket) |
| IWM | 295.7 | broken on most dates | negative | short-lean, low conviction | — | — |

- **`uw options-flow dte-volume-share` (MARKET):** 0DTE 31.9%, weeklies 12.1%, monthlies 15.4%, LEAPs 5.0% → BALANCED, not retail-dominated. Rotation calls keep full conviction weighting (no uniform downgrade).
- **`uw historical vrp`:** SPY FAIR (−0.0187, IV30 13.7% ≈ realised 15.6%); **QQQ PREMIUM_BUYING** (−0.057, IV30 24.8% vs realised **30.5%** — Nasdaq vol genuinely cheap vs realised; index-vs-constituent dispersion).
- **Macro backdrop (`fred_macro`):** yield curve NORMAL (+0.41); core CPI 2.81% / **core PCE 3.41% (sticky)**; unemployment 4.2%, payrolls +57k; **10Y 4.55% RISING + USD strengthening** = mild risk-off pressure on long-duration/growth. Forward `event_risk`: **OPEX 07-17 (T+1), FOMC + SEP 07-28/29 (T+8/T+9), Q2 GDP advance 07-30, Core PCE 07-31**, weekly claims each Thursday — plus the late-July mega-cap earnings cluster.

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book read forward as the *prior* for tomorrow's (2026-07-17, monthly OPEX) open. Prose-only, 0 rubric points, no backtested predictive claim. SPY/QQQ only.

**SPY — short-gamma into OPEX.** `total_gex` is net **−$1.15B** while the tool's regime label reads POSITIVE off a broken deep-OTM ZGL (360.62, >50% below spot) — per the reliability rule, trust the total_gex sign: **short-gamma bias**, `zgl_reliable=false`. The single largest gamma print (−$457M) sits at **750, essentially AT spot** — a short-gamma amplifier / pin magnet at the money, not a floor. Call wall **760** (+1.3%) caps upside; real put support isn't until **740** (−1.4%). A wide, asymmetric range with the pin sitting on a short-gamma pocket.
- **Structure bias:** favor directional / long-gamma (debit verticals or a cheap 0DTE straddle) over ATM premium-selling at 750; if selling premium, keep shorts outside 740/760 (condor wings), **not** an ATM iron fly on 750.

**QQQ — FULLY_NEGATIVE.** Every strike net-negative gamma, no positive-GEX pocket, ZGL null. The cleanest short-gamma signal on the board, deepest pocket (−$340.8M) right on top of spot (705) into OPEX. Stacks with the QQQ PREMIUM_BUYING VRP read toward vol expansion. No credible call wall (nominal 725 magnitude is trivial).
- **Structure bias:** avoid premium-selling/pin structures; favor long gamma (long straddle/strangle) or directional 0DTE debit verticals, stop below 700 / above 710.

**Mandatory caveats:** EOD book is a *prior*, re-computed by fresh 0DTE OI in the first 30–60 min; **07-17 is monthly OPEX** — heaviest OI resolution of the month, the map shifts materially intraday; overnight/Tier-1 gap risk voids the prior; uw-pp cannot isolate the D+1 expiry (this is the 0–45d proxy); this is the SPY/QQQ **ETF** book, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup (`zerodte_setup` — the validated stack)
> Advisory, delta-neutral, **0 rubric points**. NOT a guaranteed edge — the validation sample has no vol shock, so the short-vol left tail is UNSAMPLED. The §2 GEX walls are a map, not a pin.

| Index | Sell premium? | Vol state | Implied / expected range | Net PnL (gross) | Size scalar | Structure & entry |
|---|---|---|---|---|---|---|
| **SPY** | Yes (verdict GO_PREMIUM_SELL_INTRADAY) | LOW (VIX 16.73) | 0.9% / 1.22% | **+0.188%** (gross +0.288%) | 0.5 | Wider iron condor ±1.22%, delta-neutral. Win-open 93.3% (n=60). |
| **QQQ** | Yes | LOW | 1.72% / 1.88% | **+0.297%** (gross +0.397%) | 0.25 | Wider iron condor ±1.88%. **Caution: front-end backwardation (0DTE IV 1.63× VIX) → gap risk, half size.** |

- **Lead with NET.** `pnl_basis` = % of underlying spot notional, GROSS of costs — tiny in absolute terms and negatively skewed. Enter at/after the open once the gap resolves; **hold to the close; never carry overnight** (overnight PnL is negative). Stand aside if it gaps beyond the wings.
- **Conflict to respect:** the §2 GEX read is **short-gamma** on both indices (wider realized range likely), which fights an ATM premium-sell. Keep wings wide and size down; on QQQ (FULLY_NEGATIVE), prefer to stand aside. **SPY ≈ SPX** (trade either); QQQ weaker (Nasdaq index book unavailable). Direction: none — delta-neutral.

## 2a. Swing Dealer Positioning (1–4 weeks)
`dealer-positioning-strategist` found **two mechanized DEX sign-flips, both bearish, both on semis** — but both sit in tension with the names' bullish net-premium tags (call-side rolls), and neither scores enough to trade:
- **TSM — SHORT** (higher conviction). Verified DEX flip: +0.73B (7/10) → −0.25B (7/13) → −2.78B (7/16), prior-3 positive, total_gex deepening negative whole window (32/50 strikes negative). front-end-iv-ratio 1.384 is a near_dte=0 OPEX-eve artifact, not confirmation.
- **MU — SHORT** (medium). DEX flip +8.58B (7/14) → −1.18B (7/15) → −6.76B (7/16). But 30d flow is firmly bullish (+$225.9M) → flow_conflict.
- **No vanna squeezes** — every book is put-heavy (vanna pressure, not squeeze) and VIX ticked *up* on the last print (16.50→15.67→16.73), disqualifying the falling-VIX leg.
- **AMD** — positive DEX monotonically deteriorating (11.8B→3.3B) but **no verified sign-flip yet** — early-warning watch, not actionable.
- SPY/QQQ/IWM: no clean swing thesis (whipsaw / grid-artifact ZGLs).

## 2b. Sector Rotation
`sector-rotation-strategist`: **rotation regime = no_change (low confidence).** 7 of 11 GICS sectors sit at persistence 1.0 — the absolute gate is non-binding, so a market-relative bar was applied. Financials (value) + Comm Svcs (growth-adjacent) + Healthcare (defensive) all inflow simultaneously → no clean style-axis rotation.
- **Rotating in (standouts):** Comm Services (+$683M, persistence 1.0), Healthcare (+$295M, diffuse — size as a basket), Financials (+$170M).
- **Single-name leaders clearing the conditional +1 gate:** **NBIS** (Comm Svcs — but see below, the bullish read was *disproven* by a mega-tier sell block) and **BRKB** (Financials, +$70.8M/30d aligned). Only these two clear persistence≥0.6 + 30d-alignment + $50M magnitude.
- **Emerging bearish (watch, not yet a call):** Technology single-day swung −$3.36B (persistence still 0.8), and **SMH cross-confirms** — largest ETF outflow in the 21-name universe (−$103.7M/5d) with aggressive put-buying ($62.5M 500p, 0DTE 650/655p). Needs Tech persistence to break <0.6 with dominant-outflow for 2+ sessions before it's a call. GDX/Basic Materials also bearish-agree.

**ETF flow tape (advisory)** — top movers:

| ETF | Net prem dir (5d) | Persistence | DP positioning | Options urgency | GICS agreement | Note |
|---|---|---|---|---|---|---|
| SMH | **outflow −$103.7M** (largest) | BEARISH | mixed | **aggressive put-buying** | agree (emerging) | Cross-confirms Tech single-day reversal |
| GDX | outflow −$20.7M | BEARISH | below-mid (distribution) | matched put-spreads | agree (Basic Materials) | — |
| XBI | outflow −$8.0M | BEARISH | thin | put-lean | disagree (Healthcare) | Biotech sold while broad healthcare bought |
| EWY | inflow +$27.5M | BULLISH | creation/redemption | mixed | n/a (geographic) | — |
| XLI | inflow +$4.1M | BULLISH | near-mid | long-dated 2027 calls | **disagree** (Industrials GICS) | ETF tape does NOT confirm the aggregate reversal |

## 3. Swing Setups (1–6 weeks)
**No sized swing setups today — every candidate is drop-tier (raw ≤2).** The names below are documented for journaling; none is a trade.

### 3a. Long swings (regime-aligned)
- **BRKB** (raw 2, watch-only) — cleanest long on the board: Financials rotation leader, all three conditional-gate legs clear (+$70.8M/30d, persistence 1.0). Fails the ≥2-agent confluence gate (single agent) and sits one point under LOW. Watch for a second agent. *Data note: BRK.B returns no UW data; BRKB is the working symbol.*
- **ASTS** (raw 0, watch-only) — the strongest *genuine* accumulation read: real mid-day mega/block buying ($295M block 86% buy + $77M mega, verified non-cross), buying the dip on a name −48.9%/30d, DP support $54–66. But 30d options-flow accretion is negligible ($10.6M) → the +3 conjunction halves and a lite-conflict cancels it to 0. ⚠ Falling knife until flow confirms.
- **DIS** (raw 0, watch-only) — steady block-tier DP accumulation defending $97.15 (now $99.71), but the DP buy read has **no options-flow confirmation** on any window (30d −$9.65M, 90d −$42.6M both net-bearish).
- **SPCX** (raw 0, watch-only) — sweep-tracker-only bullish (4/5, $586M calls, 330C ask 29.99×), but the sweep line scores 0 points and no co-flag corroborates.

### 3b. Short / fade swings (defined risk only)
The bearish-semis theme lives here, but it splits cleanly on 30d flow and nothing scores:
- **AMD** (raw 1) — the most internally-consistent bearish name: net-bearish 30d flow (−$222.2M, 2.3× median), a $1.31B opening-confirmed put book (500-strike, 82–88% ΔOI), IVR 100, DEX deteriorating. No bullish flow to fight — but no verified DEX flip and the sweep line scores 0, so raw is only 1. **Invalidation: 740-level put strikes breaking on continuation; a verified DEX positive flip.**
- **TSM** (raw 2) — DEX flip + aligned −$159.7M/30d flow + $525M opening puts; top of the semis correlation cluster. **Invalidation: DEX reverses positive ≥3 sessions.**
- **SNDK** (raw −2) — carries the **largest** persistent opening-put book on the tape ($2.07B, 5/5 sessions) but 30d/90d flow is firmly bullish (+$558.7M/+$2.0B) and contrarian's dip-buy divergence agrees → sized short this is *fading a put wall against the flow*; flow_conflict −3. Watch, not a short.
- **NBIS** (raw −3) — the cleanest DP-distribution-vs-paper divergence on the tape: a genuine 20:39Z mega-tier 100%-SELL block ($506M) + $575M opening puts vs bullish options flow (+$96.9M/30d). Only 2 aligned bearish signals (not 3+). **Flagged as an adverse-flow EXIT** (carried long since 07-09; thesis now dead).

**Persistence-first sweeps (informational, 0 pts):** SNDK bearish 5/5 ($2.07B puts), AMD bearish 5/5 ($1.31B puts), NBIS bearish 4/5 ($575M puts), TSM bearish 3/5 ($525M puts), SPCX bullish 4/5 ($586M calls). ORCL flagged conflicting (call-side OI building vs net-bearish tape) — do not size.

## 4. LEAP Builds (6–24 months)
**None.** `leap-positioning-radar`: zero candidates clear the strict 6-of-9 gate.
- **AAPL** — closest (6/9 individually-passing) but the **required** cum-flow accretion gate FAILS (90d MIXED +$463M net = 3.7% of gross; 30d reversed to −$85M) and next earnings is only 2 weeks out (dated catalyst → not a clean multi-quarter LEAP thesis). Re-check post-earnings if the 883-DTE 450C ask-dominance persists.
- **GOOGL** DIRECTIONAL_SHORT (buy_ratio 0.365 selling); **IBM** put-dominant collar/hedge; **TSM** put-writing; **ZTS** explicit DISTRIBUTION; **VOD/PDD** flat/waning cum-flow. All disqualified.
- Context: LEAP DTE share is only 5.0% of tape; rising 10Y + strong USD is a structural headwind for long-duration growth LEAPs.

## 5. Volatility Surface
The board's real activity is pre-earnings vol into the late-July cluster. All single-agent, all drop-tier, all defined-risk / advisory:
- **SELL VOL (earnings kink, crush target):** **AAPL** (07-30, SELL VOL FULL — the only TAIL_HEDGING-confirmed setup, but carries a C28 call-unwind distribution flag), **MSFT** (07-29, kink 57.2% dte14, IVR 99 — also the only OPEX pin clearing gate at 400), **GOOGL** (07-22, coin-flip flat back-month), **META** (07-29, FOMC contaminates the crush read), **INTC** (07-23, flow/skew tension, ~14% implied), **NOW** (07-22, richest front premium, big-mover), **TXN** (07-22, modest positive tail lean).
- **VRP-aligned sells (vol genuinely rich vs realised):** **BE** (07-28, +0.44 PREMIUM_SELLING, IVR 100 — cleanest VRP alignment), **COHR** (08-12, +0.19).
- **BUY VOL (the one long-vol name):** **ON** — real earnings-aligned kink (08-03) but **negative VRP −0.10** (vol cheap vs realised despite the IVR-100 badge; own-history-rank ≠ rich-vs-realised). A long straddle, not the default sell.
- **NFLX** — reported 07-16, −10.94%, IVR 100, backwardation still elevated one session post-print (front-end 1.561) — not yet crushed; post-event, out of scope for new entries.
- **CAT** — the tradeable item is its 30d put-skew TAIL_HEDGING (skew_ratio 1.101), not its (artifact) term-structure kink.
- **Front-end-iv-ratio hygiene:** the default `--near-dte 1` misreads OPEX-eve (near_dte_actual=0) both directions — falsely FLAT on MSFT (1.042 → corrected 1.254), falsely inflated on TXN. All ratios above use earnings-adjacent tenors.
- **`uw insights analyst-vs-flow` returned no analyst field this run** — the analyst-vs-flow disqualifier could not be evaluated; treat SELL VOL calls as an open blind spot, not a clean pass.

## 6. Risk & Correlation
**Macro headline:** sticky core PCE 3.41%, 10Y 4.55% rising, USD strengthening = mild risk-off on duration. **Forward event risk inside any swing horizon: OPEX 07-17 (T+1), FOMC + SEP 07-28/29 (T+8/T+9), Q2 GDP 07-30, Core PCE 07-31.**

- **Correlation clusters (`uw risk portfolio-correlation`, 30d):**
  - **`semis_memory_cluster`** (8 names, one connected component): TXN/ON 0.932, AMD/INTC 0.887, SNDK/MU 0.871, TSM/AMD 0.838, AMD/MU 0.817, TSM/INTC 0.816, INTC/COHR 0.806 → **{TSM, AMD, SNDK, MU, INTC, TXN, ON, COHR}. The entire bearish-semis theme is ONE bet.** (Kept member for gating: TSM.)
  - `software_megacap_cluster`: MSFT/NOW 0.825.
- **Regime confirmation:** TRANSITIONAL/UPTREND confirmed from Step 0. VRP SPY FAIR / QQQ PREMIUM_BUYING. QQQ front-end 1.63× VIX backwardation = event/gap risk.
- **Fundamentals verdicts / debate:** **n/a — stages 2b and 2c were SKIPPED** per the zero-LOW empty-board protocol (the fundamentals gate and debate only *cut* size on names that would be sized; nothing reached LOW). Phase-1 already supplied the distribution reads and earnings dates.
- **Breadth cross-check (fz, advisory):** advancers 183 / decliners 191, pct_green **36.38%** — **divergence_flag TRUE**: an UPTREND-labeled, roughly-flat index with <50% green constituents corroborates uw's bearish flow skew. A distribution tell hidden by the single regime label.
- **Adverse-flow EXIT candidates (prior conviction carries):** **NBIS** (carried long 07-09 — strong adverse reversal: mega-tier 100% SELL $506M + $575M opening puts + inst-accum ratio 0.31; the carried bullish thesis is dead → **flatten**), **TSM** (carried 07-08 — DEX flip + $525M opening puts → **exit**), **SNDK** (carried 07-08 — exit-lean/monitor, largest opening-put book vs dip-buyers, unresolved → do not re-add), **NVDA** (carried 07-10 — monitor, mild bearish net_flow). Groups conviction_07-11→07-15 don't exist (empty write-back streak).
- **Hedge sleeve:** book net delta = 0 (nothing sized) → no mechanical hedge fires. Advisory posture: the aligned reads (QQQ negative VRP = cheap vol vs 30.5% realised; persistent semis put flow; 37% breadth; FOMC T+9) all point one way — a **starter-size QQQ defined-risk put vertical (2–4wk, through FOMC)** is the correct cheap-vol expression (long-vol into negative VRP; defined-risk is event-gate exempt). Do **not** sell naked QQQ vol (negative VRP + 1.63× front-end backwardation). SPY premium-selling only via the intraday 0DTE setup (defined-risk, never overnight, half size).

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**Empty.** No ticker reached MEDIUM (raw ≥7) or even LOW (raw ≥3). Top raw_score on the board is **2** (TSM, MSFT, BRKB). Per the empty-board protocol, the top-5-by-raw were carried through the Phase-2 hygiene pass (risk-monitor) but none is a sizing recommendation; stages 2b/2c were skipped.

**Expectancy lens (advisory — C31):** no per-tier expectancy to display — zero calls reached a sizeable tier this session, and the prior conviction groups (07-13→07-15) were also empty write-backs, so there is no rolling closed-call set to compute payoff ratio over. `[advisory — expectancy is not yet a live sizing axis]`

**Procedural top-5-by-raw (NOT trades — for audit continuity):**

| # | Ticker | Dir | Raw | Dominant class | Why it topped a no-edge board | Final size |
|---|---|---|---|---|---|---|
| 1 | TSM | short | 2 | bearish_flow | DEX flip + aligned −$159.7M/30d flow — only name where two signal quantities agree with direction | skip |
| 2 | MSFT | vol_short | 2 | earnings_vol | earnings SELL VOL + the only OPEX pin clearing gate (400 iron fly) | skip |
| 3 | BRKB | long | 2 | sector_rotation | Financials leader, all conditional gates pass; single-agent | skip |
| 4 | AMD | short | 1 | bearish_flow | 2.3×-median aligned bearish flow + $1.31B opening puts + DEX deterioration | skip |
| 5 | AAPL | vol_short | 1 | earnings_vol | FULL-conviction SELL VOL (TAIL_HEDGING) but carries a C28 distribution flag | skip |

**Note for the desk / next audit:** the clean `bearish_flow` class carries **+17.4pp market-excess over same-window SPY-short (n=132, WR 0.5455)** right now — a real, currently-live bearish edge — yet no name accumulates enough rubric points to act on it (the rubric has exactly one positive bearish line, the mechanized DEX flip at +1). This is a standing structural gap worth a register item, not something to improvise around under the freeze.

### Conviction-scoring rubric (Step 4, FROZEN 2026-06-12) — embedded for audit
```
Daily conviction score = Σ:
  +1  dealer-positioning MECHANIZED DEX flip / vanna-squeeze in trade direction (verified sign change, evidence cited)
  +3  accumulation-hunter 3+ aligned signals (DP+OI+smart-positioning, block-stratified institutional) — CONJUNCTION: full +3 only when cum_flow_30d confirms (aligned AND |cum_flow_30d| ≥ $50M); else halved +3→+1
  +1  multi-day OI build (oi-trend BUILDING, --days ≥ 5)
  +1  conviction-matrix DIRECTIONAL_LONG >70 — CONDITIONAL: only when dominant_signal_class == leap_directional, else 0
  +1  cum_premium_flow net accretion in trade direction (30d) — INTENT-SCREENED (no C28 distribution_flag; not dividend-capture arb)
  +1  sector-rotation single-name leader — CONDITIONAL: persistence ≥ 0.6 AND cum_flow_30d aligned AND |cum_flow_30d| ≥ $50M
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored)
  +1  vol-surface-scout KINKED / BACKWARDATION with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week)
  -2  contrarian overcrowded long + rising pc-ratio-zscore (VRP positive)
  -3  flow_conflict — cum_flow_30d clearly opposite dominant_signal_class (sign flip + magnitude > union-median, or explicit OPPOSITE)
  -1  flow_conflict_lite — cum_flow_30d MIXED (near zero, or aligned but bottom-quartile magnitude). Mutually exclusive with flow_conflict.
  [TIER GATES, risk-monitor 2d — 0 pts, not score_components]: −1 tier correlation cluster; −1 tier regime conflict.
Tiers: ≥9 HIGH (full) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 drop. HIGH cut carries NO validated ranking claim (failed re-confirmation 2026-06-12); OUT-OF-REGIME half-cap active.
```

## 8. Watch-only — single signal, no confluence
Surfaced by one agent, failed the ≥2-agent confluence gate — journaling only, NOT trade entry:
- **BRKB** (sector-rotation long, +$70.8M/30d) — cleanest long, one point under LOW; watch for a second agent.
- **ASTS / DIS** (accumulation-hunter longs) — genuine DP block buying but zero/negative options-flow confirmation.
- **SPCX** (sweep-tracker long, $586M calls) — sweep line scores 0.
- **CRNX** (accumulation, contradicted) — single block, all flow windows bearish, +153%/30d extended.
- **MU** (dealer-positioning short) — DEX flip but flow_conflict −3; the "bearish" 1050P is a conversion artifact.
- **The vol-surface / earnings cluster** (GOOGL, META, INTC, NOW, TXN, BE, COHR, ON) — each a single vol-agent flag; see §5.

**Structural artifacts explicitly excluded from scoring (context, 0 pts):** SPX +$2.24B "bullish net-prem" = a **box spread** (7000C/8000P matched 11,200-lot across Dec-2027 + Sep-2026 = ~$4.69B, ~99% of the structured dollar tape); MU 1050P $160M = deep-ITM conversion; DRAM P64 $50M = wash print (P&L ≈ 0); META 700C block ($112M+$110M same leg, no_side matched) = roll/cross; the Tier-1 single-leg whale puts (16/18 DTE=1, delta −0.85 to −0.995) = OPEX financing pollution. None represents directional conviction.

---
*Fleet: 12 Phase-1 agents (OPEX week incl. opex-pin-strategist) → signal-confluence-quant → risk-monitor hygiene. Stages 2b (fundamentals-gate) and 2c (bull/bear debate) skipped per the zero-LOW empty-board protocol. Rubric frozen 2026-06-12; OUT-OF-REGIME sizing cap active. Envelope: `decision.json` (schema 1.3, validated).*
