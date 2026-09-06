# Daily Market Analysis — 2026-06-17

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / PULLBACK_IN_UPTREND. SPY 740.96 (below 20SMA 746.8, above 50SMA 728.24, −2.56% from 90d high). Both SPY & QQQ flipped **net short-gamma** into the next session (amplification-prone). VIX 18.44 **spiking +2.0** on Warsh's first FOMC (rates held, hawkish-hold). Breadth very weak — 38.1% bullish, `fz` pct_green **14.31%** (430 decliners vs 72 advancers). Sector lean: Tech/Comm Services rotating OUT; Financials/Industrials/Materials/gold persistent inflows.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half` (P0.6 guard active; risk-monitor enforced).
- **Next-session GEX (SPY/QQQ):** SPY — short-gamma, ZGL unreliable (302.47, deep-OTM), put wall **740** (at spot), call wall 755 → directional/long-vol over short straddles. QQQ — **FULLY_NEGATIVE**, put wall **720**, call wall 735 → breakout/trend-prone, cleanest short-gamma book. Both fresh (1–2 session) flips, gap risk elevated post-FOMC. *Advisory — see §2.*
- **Top swing build:** **None.** No long cleared confluence + scoring; the single scored name is a LOW-tier SPY July bear-put-vertical **short-hedge**, gated to skip/token by the FOMC-day panic gate.
- **Top LEAP candidate:** **None.** Entire DTE>180 board is ETF/index macro hedging — zero single-name LEAP conviction.
- **Biggest risk:** `beta_equity_cluster` (SPY/IWM 0.838, SPY/NVDA 0.749) — high-beta/semis move as one. Front-end IV panic (SPY feir **1.548**) + May PCE 2026-06-25 inside any swing horizon. **Posture: sit on hands.** No long edge, no high-conviction short.

> **Verdict — a "no-edge" defensive day.** Accumulation found zero longs (headline semis dark-pool prints are mega-tier *sells* — distribution, not accumulation). LEAP radar zero. Contrarian zero fades (event-IV regime, not crowding). The institutional single-leg whale tape is uniformly **bearish puts on mega-cap tech**, but it is overwhelmingly OPEX/FOMC hedge flow (cum-flow MIXED → demoted). Nothing reaches MEDIUM (raw ≥7), let alone HIGH. The honest output is **small/no exposure** carried as a token defined-risk hedge, not a conviction book.

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** TRANSITIONAL — *"Mixed signals, reduce position size, wait for clarity."* Trend: **PULLBACK_IN_UPTREND**. Trading guidance: half position sizes, defined-risk, iron condors in range. SPY 740.96: above the 50SMA (728.24) but below the 20SMA (746.8), +0.31% / 30d, −2.56% from the 90d high. 10-day tape: 757.09 → 740.96 (**−2.1%**), IV-rank 12.5 → 26.5, latest flow bearish. QQQ 10-day: 740.61 → 722.51, IV-rank **41 → 72** (vol re-pricing into the FOMC). Breadth is the tell — **38.1% bullish** (2,391 bull / 3,882 bear of 6,273) and `fz` advance-decline at **14.31% green** (avg constituent −1.67%): the index is held up by a thin mega-cap bid while the average name is down nearly a full point more — a distribution-under-the-veneer signature.

**Per-index gamma (EOD current-state book):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 741.28 | 302.47 *(unreliable)* | −1.116B | short-gamma (net-neg; "POSITIVE" label conflicts with sign) | 755 (+1.85%) | **740 (≈spot, −168M)** |
| QQQ | 723.55 | null | −537M | **FULLY_NEGATIVE** | 735 (+1.58%) | **720 (−0.49%, −91M)** |
| IWM | ~290.16 | whipsaw | −687M | short-gamma wing below spot | 291/292 flip | 279–281 zone |

**`uw options-flow dte-volume-share` (MARKET):** 0DTE 29.8% / weeklies 34.5% / monthlies 23.6% / LEAPs 4.9% — **BALANCED** (no retail-dominated thumb on the scale; rotation calls keep benefit-of-the-doubt).

**`uw historical vrp` (SPY):** **FAIR** — IV30 0.1526 vs realised σ30 0.1494 (VRP +0.0032). No vol edge either direction from VRP alone.

**Macro backdrop (`scripts/fred_macro.py`):** yield curve **normal** (10Y−2Y +0.29); core CPI **2.96%** YoY, core PCE **3.29%** YoY (sticky); unemployment 4.3%, payrolls +172k; 10Y **4.43% falling** (−16bp/30d); USD **strengthening**; fed funds 3.63%. **Forward `event_risk` (next ~10 trading days):** **FOMC 2026-06-17 = TODAY** — Kevin Warsh's first meeting as Chair; rates held but signaled a *possible hike* (hawkish) — the source of today's VIX spike & risk-off tape. Initial jobless claims **2026-06-18** & **2026-06-25**. **May PCE 2026-06-25** (Tier-1, Fed's preferred gauge). Next CPI ~2026-07-14 (outside window).

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book read forward as the *prior* for next session's open. Prose-only, **0 rubric points**, no backtested predictive claim. Scope: SPY/QQQ only.

| Index | Regime | ZGL | Call wall | Put wall | One-line structure bias |
|---|---|---|---|---|---|
| **SPY** | short-gamma (total_gex −1.116B; net-neg despite "POSITIVE" tag) | 302.47 — **zgl_reliable=false** (deep-OTM extrapolation) | 755 (+1.85%) | **740 (≈spot, −168M — densest short-gamma strike)** | Spot sits on the heaviest put wall with the 730–749 zone net-negative; **directional/debit-vertical or long-vol over short straddles**. Loss of 740 → 730 air pocket (dealer selling amplifies). Stabilizes only above ~750 toward the 755 cap. |
| **QQQ** | **FULLY_NEGATIVE** | null (correct on a fully-negative book) | 735 (+1.58%) | **720 (−0.49%, −91M)** | Cleanest short-gamma book — dealer hedging amplifies both ways, no internal damping. Wider realized range than SPY. **Long-vol / breakout posture; do NOT sell the 720 straddle** (the amplification strike). 720↔735 is a trend corridor, not a fade range. |

**Trajectory:** both flips are **fresh (1–2 sessions), not held** — SPY briefly went clean-positive 6/15 then re-broke negative 6/16–6/17; QQQ flipped POSITIVE→FULLY_NEGATIVE *today*. Fresh short-gamma empirically precedes realized-vol expansion → do not treat any wall as a hard pin.

**Mandatory caveats:** EOD is a *prior*, not a target (fresh 0DTE OI re-computes ZGL/walls in the first 30–60 min). ZGL unreliable on SPY (fell back to total_gex sign + spot-vs-wall). **Gap risk elevated** — FOMC just landed + May PCE 6/25 ahead. This is the **SPY/QQQ ETF book, not the cleaner SPX/NDX index book**; `uw` cannot isolate the D+1 expiry (0–45d proxy).

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — validated stack)

> Advisory, delta-neutral, **0 rubric points**. NOT a guaranteed edge — the validation sample has no vol shock, so the short-vol left tail is UNSAMPLED.

**Both SPY and QQQ → STAND ASIDE today.** `stand_aside_reason: "VIX spiking (+2.0) — short-vol left-tail regime."` size_scalar 0.0. The rolling backtest verdict is `GO_PREMIUM_SELL_INTRADAY` historically, but **today's signal is stand-aside** — you do not sell premium into a vol spike.

| Index | sell_premium | vol_state / VIX | implied move | exp range | net PnL basis | caution |
|---|---|---|---|---|---|---|
| SPY | **false** | MID / 18.44 | 1.41% | 1.24% (short-gamma) | gross +0.293% / **net +0.193%** (% spot notional) | VIX spiking — stand aside |
| QQQ | **false** | MID / 18.44 | 2.02% | 1.89% (short-gamma) | gross +0.379% / **net +0.279%** | + front-end **backwardation** (0DTE IV 1.74× VIX) — half size if traded |

SPY ≈ SPX (validated identical). QQQ weaker (NDX book unavailable). **Direction: none** — delta-neutral. *Entry rule (if it were live): enter at/after the open once the gap resolves, hold to the close, never carry overnight.*

## 2a (cont). Swing Dealer Positioning (1–4 weeks)

`dealer-positioning-strategist`: **No mechanized DEX flip on any index; no confirmed vanna squeeze (VIX rising disqualifies all three put-heavy books).** The **+1 dealer-positioning rubric line does NOT fire.** The complex flipped NEG→POS on 6/11 (now 4 sessions stale → fails the "latest-session opposite to ≥3 prior" test). DEX is decaying toward zero on all three (SPY +9.8B, QQQ +30.5B, IWM −4.1B). **Swing posture: NEUTRAL with a fragility tilt lower**, strongest on QQQ (Tech rotation OUT + GEX re-flip to negative-gamma today). **Watch item: IWM is one negative print away from a 3-session run that would mechanize a SHORT DEX flip — re-pull 6/18.**

## 2b. Sector Rotation

`sector-rotation-strategist`: **rotation_regime = defensive→cyclical (value tilt), medium confidence.** Rotating IN (persistence 1.0, 5d): **Financials, Industrials, Basic Materials, Real Estate.** Rotating OUT: Technology (−$71M today, −$456M on the synthesis measure), Comm Services (flipped −$636M today after 4 inflow days), Consumer Defensive/Healthcare. Single-name leaders (liquidity-screened): **COF, KKR, HWM, VRT, FCX, NEM, AEM.**

**The critical tension:** the ETF *options* tape **disagrees** with the GICS aggregate on the cyclical side — XLF/XLI/XLB are flat-to-negative on the 5d window even as their GICS sectors print 1.0 persistence. That downgrades the rotation from high to **medium**, and means **the single names carry the thesis, not the ETF wrappers.**

**ETF flow tape (advisory — 0 rubric points):**

| ETF | Net prem dir | Persistence | DP positioning | Options urgency | GICS agreement | Leaders |
|---|---|---|---|---|---|---|
| **GDX** | inflow +35.6M | strong BULLISH | large below-mid blocks | 0DTE 78–82C ask sweeps (directional) | agree (Materials 1.0) | NEM, AEM, GOLD |
| EWY | inflow +29.3M | BULLISH | $102M block + Aug call ladder | call ladder dominant | **n/a** (Korea) | instrument-only |
| SMH | inflow +11.7M *(MIXED)* | weak | mixed | heavy Jul put-bid **hedging** | **disagree** (Tech out) → watch | — |
| XBI | inflow +5.77M | BULLISH | rank-only | rank-only | partial → instrument | biotech bid |
| XLF | **outflow −2.85M** | MIXED | creation blocks + Jul-50C bid | mixed | **disagree** (Financials GICS 1.0) | COF/KKR carry it |
| XLK | outflow −8.95M | BEARISH | creation | 0DTE deep-ITM roll noise | agree (Tech out) | — |

**GDX is the standout of the entire tape** (gold-miner inflow + directional sweep urgency). Swing implication: long cyclical/value single names (HWM, COF, FCX) + gold (GDX/NEM/AEM) as the *instrument* leg; do **not** short SMH (semis are hedged, not distributed). **All half-size / tactical** — none of these cleared the conviction floor today (see §8).

---

## 3. Swing Setups (1–6 weeks)

### 3a. Long swings (regime-aligned)
**NONE.** Accumulation-hunter returned **zero** qualifying long candidates — the headline semis dark-pool prints (AVGO $3.17B, NVDA $249M, MU $264M) are **mega-tier SELLS** (AVGO institutional buy_ratio 0.000, NVDA 0.010), and the conviction-matrix reads DIRECTIONAL_SHORT / DISTRIBUTION / MIXED across the board — not a single DIRECTIONAL_LONG. The sector-rotation single-name leaders (COF/HWM/FCX/GDX) are real but each is **single-agent** and fails the cum-flow magnitude gate (all 30d flows < $50M) → §8 watch-only. **No long entered the book today.**

### 3b. Short / fade swings (defined risk only)

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **SPY** | raw 3 (LOW) | Multi-day institutional July bear-put verticals (repeat_count 3), sitting in the dealer short-gamma wing; breadth-distribution + hawkish-hold | July bear put vertical 712P/709P (defined-risk, **token short-hedge sleeve**) | Reclaims 20SMA 746.8 / 755 call wall and holds; PCE 6/25 benign + breadth recovers | **skip / token-hedge** (panic −1 floored starter→skip; rubric_regime half-cap) |
| IWM | raw 1 (DROP) | July bear put vertical 281P/279P in short-gamma wing; DEX rolling toward a short flip | put vertical (defined-risk) | Reclaims 291 (positive gamma) | skip (cluster dup of SPY) |
| AVGO | raw 2 (DROP) | $3.17B mega-tier 100%-SELL block (−6.26 below mid) + Tier-1 opening put + DIRECTIONAL_SHORT | — (avoid long / no new short) | — | **skip** — fundamentals **CAUTION** (see §6) |

**Fade tape (contrarian-scanner): zero clean fades.** Every crowded-P/C name (PEP, CBOE, ACI) has flow **aligned** with falling price (informed continuation, not a fade) and is in event-driven BACKWARDATION; with VRP marginal (+0.0032) and VIX rising, fading the hedge into FOMC/PCE is exactly the trade the rubric exists to prevent.

**Sweep tape (sweep-tracker, informational — 0 points):** directional skew is **bearish/put-side** (SMH/NBIS/MRVL/SNDK put-side OI-confirmed-opening, plus index/mega-cap put hedges) but the mega-cap cohort's 30d cum-flow is MIXED → **demoted to hedge-flow watch-only**. No first-class scorable sweep candidate. Read: OPEX-week + FOMC-day put hedging, not a directional momentum book.

---

## 4. LEAP Builds (6–24 months)

**NONE.** `leap-positioning-radar`: zero candidates pass the 6-of-9 gate stack. The entire DTE>180 board is **ETF/index macro hedging and financing structure** (IWM puts, TLT calls, FXI calls, EEM/EFA puts, SLV straddle) — slow money is buying protection and expressing rates/China macro views, **not** initiating single-name multi-quarter longs into a Warsh FOMC + spiking VIX. The Step-0 semis OI builds (NVDA +220k, MU +82k, MRVL +70k, AVGO +66k) are confirmed **near-dated OPEX, not LEAP**, and largely put-dominated.

Disqualified near-misses: **NOK** ($20C 212-DTE was bid-side/sold; conviction MIXED, 90d cum-flow −$46M) · **FRMI** (9-month IPO, insider-dominated micro-float — un-sizeable as a LEAP; → accumulation-hunter for a shorter-horizon look) · **FXI** (conviction DISTRIBUTION, 90d −$26.8M bearish; ETF macro structure).

---

## 5. Volatility Surface

`vol-surface-scout` — **one actionable surface, MU:**

| Ticker | Structure (hygiene-clean) | Kink expiry | IV %ile (z) | VRP | Catalyst | Bias |
|---|---|---|---|---|---|---|
| **MU** | KINK (earnings hump 7/2–7/17) | 2026-07-02 / 07-17 | 85.1 *(z+1.17, PROVISIONAL n=47)* | **NEG −0.101** | **ER 6/24 +7d PM** | **BUY VOL / own the move** (negative VRP → vol is cheap vs realised; do not sell the front) |

**Substrate-hygiene note (P1.3):** 9 of 9 names scanned returned bare `BACKWARDATION` — entirely the 0DTE/FOMC wing, which carries **zero discriminating power** on a FOMC-OPEX Friday. Stripping the 0DTE bucket: TSM/WDC/NBIS are actually CONTANGO/flat (event-driven only → not calendar candidates). MRVL/INTC have genuine front backwardation but **negative VRP** (don't sell the front). SNDK is the only positive-VRP backwardation but fails the falling-panic gate (VIX rising). **Zero clean calendar candidates. Zero IV-outlier whale hedges** (the `iv-outliers` tape is all 0DTE pin-noise at penny strikes). The semi IV-rank cluster (80–100) is real, but "high rank → sell premium" is **blocked** by the VIX spike — correct posture is patience, not premium-selling. *(Advisory: MU back-month skew is call-rich/COMPLACENT — lottery flag, prose only.)*

---

## 6. Risk & Correlation

**Macro headline:** sticky core PCE (3.29%) + hawkish-hold (Warsh signaled a possible hike) + falling 10Y + strengthening USD. **Forward event_risk: May PCE 2026-06-25 (Tier-1) lands inside any 1–4wk swing horizon; jobless claims 6/18 & 6/25.**

**Correlation clusters (`uw risk portfolio-correlation`, 30d):** **`beta_equity_cluster`** — SPY/IWM **0.838**, SPY/NVDA **0.749** (treat as one position; SPY is the kept member by score). Soft-watch (no penalty): AVGO/MU 0.673, SPY/MU 0.64.

**Gates applied:**
- **PANIC GATE FIRES** — SPY front-end-iv-ratio **1.548** (BACKWARDATION; ≫ 1.10 threshold) — FOMC-day front-end fear. **−1 tier on everything.**
- **rubric_regime — capped half** (OUT-OF-REGIME: rubric fitted UPTREND, current TRANSITIONAL).
- **event_risk** — May PCE 6/25 = T+5 from today; defined-risk verticals get the lighter −0.5 touch.
- **VRP / sector** — no-op (FAIR; no sector-flow-persistence ≥0.6 penalty trigger).

**Fundamentals verdicts (top-5):**
- **NVDA → VETO** (drops to watch-only): 3/3 beat-streak + elite growth (ROE 112%, D/E 0.05) + AI-supercycle catalyst + **+$175M bullish 30d flow** all contradict the bearish/distribution read; the lone insider-selling leg is routine programmatic comp. *The bearish flow was de-grossing/hedging, not distribution.*
- **AVGO → CAUTION** (−1 tier): fundamentals fight the short — +32% rev / +126% EPS, **JPMorgan aggressive-buy into the −20% dip**, 1.33 strong-buy, +33% to target; earnings only mixed (last q −0.87% miss), insider neutral.
- **MU → CONFIRM:** ER 2026-06-24 (7d) is the vol thesis itself; 4/4 explosive beats, price 7.6% **above** consensus target = genuine two-sided risk into the print (feeds the SELL-VOL-vs-BUY-VOL conflict).
- SPY/IWM → NA (index).

**Debate-disconfirmation cuts:** SPY {anti-short 0.55 / pro-short 0.65} → short-hedge modestly survives (no cut). AVGO {buy-dip 0.65 / pro-short 0.75} → both sides converged on **"avoid the long / don't aggressively press a new short"** → watch-only.

**Adverse-flow exit list:** **None** — the rolling `conviction_2026-06-16` watchlist group is empty (cold start); `watchlist alerts`/`scan` returned nothing to exit.

**Breadth cross-check (`fz`, advisory):** 72 advancers / 430 decliners, pct_green **14.31%**, avg −1.67%. **No green-tape divergence** — the tape is red and *agrees* with the bearish regime label (a red tape with weak breadth confirms, rather than contradicts, the TRANSITIONAL call). Top mover MRNA +11.55%, worst CVNA −10.25%.

**Hedge sleeve:** the conviction book carries **no net long exposure to hedge.** The token SPY July bear-put-vertical *is* the entire directional footprint — **do not add a separate VIX/QQQ leg** (front-end IV is already 1.548; buying short-dated vol here is buying the panic high). **Recommendation: sit on hands; carry the four watchlist names and re-measure tomorrow.**

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**NONE.** No ticker reached MEDIUM (raw ≥ 7) or HIGH (raw ≥ 9). This is a legitimate no-conviction defensive day, not a failure. The full scored ledger (for audit):

| Ticker | raw | tier | class | win_rate (n, source) | pre-risk | fund. | debate (bull/bear) | gates applied | final | invalidation |
|---|---|---|---|---|---|---|---|---|---|---|
| **SPY** | 3 | LOW | multileg_directional (SHORT) | null (NA-substrate) | starter | NA | 0.55 / 0.65 | panic −1 · event_risk −0.5 · rubric_regime half · cluster kept · debate cleared | **skip/token-hedge** | reclaims 746.8/755 & holds; PCE benign |
| AVGO | 2 | DROP | bearish_flow (SHORT) | 0.40 (140, backtest_clean) | skip | **CAUTION −1** | 0.65 / 0.75 (avoid-long) | panic −1 · fundamentals −1 | skip | — |
| MU | 1 | DROP | earnings_vol (neutral) | n/a (vol) | skip | CONFIRM | — | event_risk exempt (ER=thesis) | skip | back-month skew flips to tail-hedging pre-print |
| IWM | 1 | DROP | multileg_directional (SHORT) | null (NA-substrate) | skip | NA | mirrors SPY | panic −1 · cluster −1 | skip | reclaims 291 |
| NVDA | −1 | DROP | bearish_flow (SHORT) | 0.40 (140, backtest_clean) | skip | **VETO** | — | fundamentals VETO override | **watch-only** | n/a (thesis killed) |

`market_excess`: NA for SPY/IWM (multileg_directional has no backtest substrate). `bearish_flow` clean WR **0.40 (n=140, market-wide)** — below the 0.50 floor; positive market-excess (+0.164) does not rescue it (downgrade-only gate).

**Expectancy lens `[advisory — expectancy is not yet a live sizing axis]`:** no per-tier expectancy printed this run — the rolling `conviction_2026-06-16` group is empty (cold start), and there is no resolved-call history to compute payoff_ratio/expectancy from. The live sizer remains the win-rate ladder; the C3 fractional-Kelly sizer stays advisory pending n≥30 closed calls with monotone tier×expectancy.

<details>
<summary>Conviction-scoring rubric (Step 4) — FROZEN version 2026-06-12</summary>

```
Daily conviction score = Σ:
  +1  dealer-positioning MECHANIZED DEX flip / vanna-squeeze in trade direction (sign-change, not level)
  +3  3+ aligned accumulation signals (DP+OI+smart-positioning, block-stratified institutional) — CONJUNCTION:
      full +3 only when cum_premium_flow_30d confirms (aligned AND |cum_flow_30d| ≥ $50M); else halved to +1
  +1  multi-day OI build (oi-trend BUILDING, ≥5 days)
  +1  conviction-matrix DIRECTIONAL_LONG >70 — CONDITIONAL: only when dominant_signal_class == leap_directional
  +1  cum_premium_flow net directional accretion in trade direction (30d) — INTENT-SCREENED (no distribution_flag;
      no deep-ITM ex-div arb)
  +1  sector-rotation single-name leader — CONDITIONAL: persistence ≥0.6 AND cum_flow_30d aligned AND ≥$50M
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored)
  +1  vol-surface KINKED or BACKWARDATION with VRP-aligned bias
  +1  opex-pin-strategist top-5 (OPEX week only)
  -2  contrarian overcrowded long with rising pc-ratio-zscore (informed-flow continuation penalty; C13-routed)
  -3  flow_conflict — 30d cum-flow clearly OPPOSITE dominant_signal_class
  -1  flow_conflict_lite — 30d cum-flow MIXED (mutually exclusive with flow_conflict)
  [TIER GATES, applied by risk-monitor 2d, 0 score points]: correlation cluster −1 tier; regime conflict −1 tier
Tiers: ≥9 HIGH (full) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 drop
```
*Out-of-regime guard (P0.6): rubric fitted in UPTREND (ended 2026-06-12); current TRANSITIONAL → all sizing capped at half until a `/calibration-audit` records ≥30 resolved post-2026-06-12 calls.*

</details>

---

## 8. Watch-only — single signal, no confluence

Surfaced by one agent, failed the ≥2-agent confluence gate (and/or the cum-flow magnitude gate). For journaling, **NOT for trade entry today.**

| Ticker | Sole agent | Note |
|---|---|---|
| COF | sector-rotation | Financials leader, +11.9M today / 30d +39.6M (< $50M floor) |
| GDX | sector-rotation | Gold-miner ETF, +35.6M (standout instrument), 30d +47.1M (just misses $50M) |
| HWM | sector-rotation | Industrials leader, PCR 0.09 clean call, 30d +7.3M |
| FCX | sector-rotation | Materials leader, PCR 0.31, IVR 61, 30d +10.0M MIXED |
| KKR / VRT / NEM / AEM | sector-rotation | Cyclical/gold leaders, all sub-$50M 30d flow |
| MU | vol-surface + earnings *(2 agents, direction-conflicted)* | SELL VOL vs BUY VOL into 6/24 ER — vol play, not a directional conviction call → not scored |
| NKE | earnings-scout | SELL VOL half, ER 6/30 (single agent) |
| FDX | earnings-scout | SKIP — extreme front panic 1.21 + bearish flow, ER 6/23 |
| XLF | opex-pin | Pin 55 broken-wing fly (delta-neutral, not directional) |
| AAPL | opex-pin | Conditional pin 300 (flips short-gamma <296.5; delta-neutral) |
| NVDA | — | **VETO'd** from the short book (fundamentals overwhelmingly contradict the bearish read) |

**OPEX pin book (opex-pin-strategist, OPEX 6/19):** only two liquid names carry a *genuine long-gamma* pin — **XLF** (pin 55, +153.7M wall, broken-wing fly) and **AAPL** (pin 300, conditional). SPY/QQQ/IWM "pins" are short-gamma **anti-pins** (negative GEX at strike) → no pinning mechanism, dropped. VIX-spike → half-size, defined-risk only.

---

*Generated by `/daily-analysis` — 12-agent two-phase fleet (OPEX week). Rubric FROZEN 2026-06-12. Decision envelope: `decision.json`.*
