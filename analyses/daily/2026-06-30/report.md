# Daily Market Analysis — 2026-06-30

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL (trend UPTREND) — SPY 746.77 (>20/50-SMA, −1.28% 30d, −1.79% from 90d high), VIX 16.45 (LOW). SPY next-session gamma NEAR-FLIP/short-gamma at ZGL 749; QQQ day-1 long-gamma pin 735–737. Breadth **divergent** — `uw` bullish 38%, `fz` pct_green 41.75% (210 adv / 292 dec): a distribution tell under a narrow, Tech/semis-led tape.
- **Rubric regime status:** **OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half.** The 2026-06-12 freeze is still live (0/30 post-freeze HIGH/MED resolved; freeze-lift cannot run).
- **Next-session GEX (SPY/QQQ):** advisory, see §2. **SPY** — NEAR-FLIP tilted short-gamma · ZGL 749.07 (reliable) · call wall 750 / put wall 735 · lean pin into the 747–750 shelf, but respect a break of 745. **QQQ** — day-1 LONG-gamma (fragile) · ZGL 734.55 · call wall 737 / functional floor 735 / thin put wall 715 · pin 735–737, abandon below 734.55.
- **Top swing build:** **None.** Zero names cleared to a sized conviction trade. SNDK was the only confluence-gate pass (raw 3, LOW) and was cut starter→**watch** by three independent gates (fundamentals CAUTION, NFP at T+2, debate bear≥bull).
- **Top LEAP candidate:** **None.** The long-dated tape is defensive (ETF put/credit hedges — HYG/XLE/IBIT); every call-side name failed the cum-flow or conviction-matrix gate.
- **Biggest risk:** **NFP (June jobs) Thursday July 2 — T+2 trading days** — a Tier-1 binary inside every swing horizon, into a beta-heavy, narrow-breadth tape. No correlation cluster formed (semis pairs sub-0.60); no hedge sleeve required because post-gate directional exposure ≈ 0. **Standing flat is the position.**

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend UPTREND; SPY 746.77 above both the 20-SMA (742.24) and 50-SMA (735.87); −1.28% over 30d; −1.79% from the 90d high. Breadth: 2,372 bullish vs 3,873 bearish tickers (38% bullish) — **weak participation under a green index**. Guidance: half sizes, defined-risk, iron condors in range.

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 746.55 | 749.07 (reliable) | +$740M | NEAR-FLIP / short-gamma | 750 | 735 |
| QQQ | 736.09 | 734.55 (reliable) | +$558M | LONG-gamma (day-1) | 737 | 715 (thin) |
| IWM | 300.43 | 299.61 (noisy) | weak + | POSITIVE (noisy) | — | — |

- **`uw options-flow dte-volume-share`:** 0DTE 28.5% / weeklies 28.9% / monthlies 22.8% / LEAPs 4.9% → **BALANCED** (neither retail-0DTE-dominated nor institutional-monthly-dominated).
- **`uw historical vrp` (SPY):** IV30 13.9% vs realized 15.4% → **VRP −1.5%, FAIR** (realized slightly *exceeds* implied — a mild long-vol/premium-buying bias at the index; a headwind to blanket premium-selling).
- **Macro backdrop (`fred_macro`):** yield curve normal (+0.30, 10Y−2Y), Core CPI 2.96% / **Core PCE sticky 3.41%** YoY, unemployment 4.3% / payrolls +172k, 10Y 4.38% (falling 30d), USD strengthening, Fed funds 3.63%. Sticky inflation + falling-10Y + strong-USD = the transitional texture — risk-on but fragile. **Forward `event_risk`:** ISM Mfg ~Jul 1 (T+1), **NFP Thu Jul 2 (T+2, HIGH)**, CPI Jul 14, FOMC Jul 28–29.

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book (open interest that persists overnight), read forward as the *prior* for the next open. Prose-only, **0 rubric points**, no backtested predictive claim. Scope: SPY & QQQ only.

Both ETFs just exited the **same 4-session FULLY_NEGATIVE selloff (06-22→06-26)** and are in freshly-flipped, unstable gamma regimes — treat both pin biases as low-conviction and be ready to flip to a trend read if spot loses its ZGL at the open.

**SPY** — spot 746.55 · ZGL **749.07** (reliable, +0.34%) · total GEX +$740M · NEAR-FLIP, tilted short-gamma (spot just under ZGL). Dense +GEX magnet cluster **747–750** on top of spot; call wall 750, put wall 735 (distant, −1.55%), negative pockets at 745/740. **Read:** knife-edge — a push through 749 tips into clean long-gamma → pin toward 750; a break of 745 opens the 745/740 pocket toward the 735 put wall. **Structure bias:** lean pin / short-vol into 747–748 (aligns with the §2a iron-fly @746.14), keep TIGHT given fresh-regime instability + NFP gap; fade pokes above 750, but *buy* (don't fade) a break of 745.

**QQQ** — spot 736.09 · ZGL **734.55** (reliable, +0.21%) · total GEX +$558M · LONG-gamma but **flipped only today (day-1, fragile)**. Biggest gamma mass 735/736/737 straddles spot; call wall 737, functional +GEX floor 735/730, thin distant put wall 715. **Read:** strong pin/vol-suppression magnet 735–737, dealers buy dips / sell rips here; day-1 fragility + front-end IV backwardation (1.41× VIX) means a NFP gap can re-flip it straight back to short-gamma if it loses 734.55. **Structure bias:** pin structures centred 735–737 (aligns with §2a iron-fly @735.68), size DOWN, abandon below 734.55.

**Mandatory caveats:** EOD is a prior not a target (fresh 07-01 0DTE OI re-anchors the walls in the first 30–60 min); ZGL trusted only near spot; **gap risk voids the prior — NFP is 2 sessions out**; these are the SPY/QQQ ETF books, not the cleaner SPX/NDX index books; `uw` cannot isolate the D+1 expiry (0–45d proxy).

### 2a. Next-session 0DTE premium-selling setup (`zerodte_setup` — the validated stack)
Delta-neutral premium-selling, **advisory / 0 rubric points**, NOT a guaranteed edge (validation sample has no vol shock → short-vol left tail unsampled). Backtest verdict both indices: **GO_PREMIUM_SELL_INTRADAY**, but VIX 16.45 = **LOW vol state → thin edge, small size.**

| Index | Sell prem | Vol state | Implied move | Exp. range | Size scalar | Structure | Net PnL/day |
|---|---|---|---|---|---|---|---|
| SPY | yes | LOW | 0.78% | 0.77% | 0.5× | iron fly @746.14, wings ±0.77% | +0.212% (gross +0.312%, % of spot notional) |
| QQQ | yes | LOW | 1.47% | 1.26% | 0.25× | iron fly @735.68, wings ±1.26% | +0.312% (gross +0.412%) |

- **Whether (VRP):** front-expiry implied move exceeds realized open-to-close; **but** report PnL net of cost and on its real basis — the figures are % of underlying spot notional, GROSS; net-of-half-spread is SPY +0.212% / QQQ +0.312% per day. Tiny in absolute terms; a negatively-skewed seller's gross win-rate (94.5% / 89.1%) overstates the edge.
- **Size (VIX):** LOW vol state → both size down (SPY 0.5×, QQQ 0.25×); the edge is thin when VIX is cheap.
- **When:** enter at/after the open once the gap resolves; **hold the 0DTE to the close, never carry overnight**; if it gaps beyond the wings, stand aside.
- **QQQ caution:** front-end backwardation (0DTE IV 1.41× VIX) = event/gap risk → half size. **SPY ≈ SPX** (validated identical); QQQ weaker (Nasdaq index book unavailable). Promotion bar: stays advisory permanently until a vol-shock day enters the sample AND net expectancy clears a tail-aware bar.

## 2a. Swing Dealer Positioning (1–4 weeks)
`dealer-positioning-strategist` — three scored DEX flips, all mega-cap tech, all LONG (mechanized P0.4 sign-change rule, both dated values cited):

- **NVDA — cleanest flip in the fleet.** Strict *latest-session* flip 06-30: net_dex −1.05B → +4.25B, 5 prior sessions negative, |flip| ≈ 1.0× trailing-10 median; artifact-checked (distributed gamma 197.5–210). Swing bias LONG — **but see §6: the +1 flip is swamped by −$523M/30d opposing flow → the name nets to raw −2 and is rejected for a long.**
- **QQQ — strongest index flip.** Fired 06-29 (−25.36B → +13.11B, |flip| 0.52× median), confirmed 06-30 (+36.21B), independently corroborated by a **GEX regime flip 06-30 (neg→pos)**. LONG.
- **SPY — marginal flip.** Fired 06-29 (−31.79B → +7.74B, |flip| only 0.27× median — barely clears the floor), confirmed 06-30; GEX positive-flip imminent (spot 2.5pts under ZGL 749). LONG (tempered, weakest magnitude).
- **No flip:** IWM (whipsaw, no run — coherent with the breadth divergence: dealer bullishness is concentrated in mega-cap tech, small-caps absent). **AMD & TSM: persistently-positive DEX *levels* = beta, explicitly NOT flips** (do not score).
- **No vanna squeeze anywhere** — every book is call-heavy; the dated falling-VIX series (18.89→16.45) makes vanna a mild *selling headwind*, not a squeeze. Every name except SPY carries a panicked front-end IV into NFP (QQQ 1.083, IWM 1.174, NVDA 1.226) → near-term vol air-pocket risk on all longs.

## 2b. Sector Rotation
`sector-rotation-strategist` — **rotation regime: `no_change` (low confidence).** The GICS-aggregate tape is the textbook broad-tape trap: all 11 sectors INFLOW, persistence tied at 1.0. On the market-relative bar (> cross-sector median net premium), the ETF-instrument tape *filters* the GICS standouts — and the only coherent thread is a **narrow AI/semiconductor concentration, not a macro sector-pair rotation.**

- **Rotating IN — Technology/semis** (net +5.98B, accelerating 2.38B→5.98B/5d; ETF-confirmed SMH +112M / IGV +82M / XLK +10M). Single-name leaders **with the conditional +1** (30d cum-flow aligned ≥$50M): **SNDK** (30d +$1.04B), **MRVL** (+$216M), **DELL** (+$228M). **AMD / TSM / AVGO get NO +1** — today's call-pop sits on **30d net distribution** (AMD −134M, TSM −248M, AVGO −25M) → tactical only.
- **Rotating OUT — Healthcare/biotech** (XBI −11.2M, XLV −3.4M; GICS inflow *not* ETF-confirmed): net-bearish single names RVMD, LLY, ABBV, MRNA. Industrials (XLI −1.25M) and homebuilders (ITB −2.2M) de-risking, no strong single-name book.

**ETF flow tape (advisory, 0 points):**

| ETF | Net prem dir | Persistence | DP positioning | Options urgency | GICS agreement | Leaders |
|---|---|---|---|---|---|---|
| SMH +112.4M | inflow | BULLISH 5/5 | 701M 2-way blocks, mild sell-lean | balanced | **agree** (Tech) | semis |
| IGV +81.6M | inflow | BULLISH 5/5 | 625M blocks | put-heavy = 1 Jan-27 hedge → net constructive | **agree** (Tech) | software |
| GDX +37.0M | inflow | BULLISH 5/5 | 97M, slight sell-lean | collar on a bid | disagree | gold |
| XBI −11.19M | outflow | BEARISH 5/5 | — | today call-lean = bounce inside de-risk | **disagree** | biotech |
| XLV −3.37M | outflow | BEARISH | — | thin | **disagree** | — |
| ITB −2.19M | outflow | BEARISH | — | — | **disagree** | homebuilders |

Swing-book implication: long the 30d-accumulation-confirmed semis leaders (SNDK/MRVL/DELL) *in principle*, treat AMD/TSM/AVGO call-pops as tactical only, fade biotech beta (XBI) — **but every one of these is gated down to watch below** (single-signal and/or NFP T+2). This is a narrow concentration to *observe*, not a rotation to *size*.

## 3. Swing Setups (1–6 weeks)
**No sized swing trades today.** The confluence gate (≥2 distinct Phase-1 agents) admitted exactly one name — **SNDK** — and Phase-2 cut it to watch. All other candidates are single-signal (§8).

### 3a. Long swings (regime-aligned)
| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **SNDK** | 3 (LOW) | Semis/storage: sweep 5/5 + sector-rotation Tech-leader (30d +$1.04B) say LONG **but** the DP tape reads distribution/churn and insiders are selling into a +10.89% blow-off | (would be a defined-risk call vertical if taken) | Loses the choppy 2050–2090 shelf (06-26/06-29 closes); DEX/OI build stalls | **WATCH** (cut by fundamentals CAUTION + NFP T+2 + debate) |

SNDK 10-day trend is **choppy, not accumulating**: 2335 (06-25) → 2050 (06-29) → 2273 (+10.89% today), 5 bull / 5 bear days, iv30d ~107%, iv-rank ~82 — a whipsawing high-vol momentum vehicle, not a clean build.

**Single-name leaders carried for context (single-signal → §8, not sized):** MRVL, DELL (sector-rotation +1, both fundamentals CAUTION on insider selling); NKTR (accumulation-hunter sole qualifier — block-tier DP $17.95M 100%-buy, DIRECTIONAL_LONG@56.8, but 30d options flow flat/MIXED so it fails the conjunction and stays LOW). EWZ, BMY, BKNG carried in §5/§8.

### 3b. Short / fade swings (defined risk only)
**None.** `contrarian-scanner` returned **zero fades** — a disciplined triple-gate abort: negative VRP (don't fade cheap-to-realized vol), universal front-end BACKWARDATION into NFP (event pending, not crowding), and no index-level fear extreme. The lone statistical extreme, **BKNG** (z −2.30 BULLISH_EXTREME with a bearish net-premium divergence −$1.24M on a +14.9% run), is held as an **informed-continuation watch**, not a short — single-name call-heavy extremes predict continuation, and it's backwardated into NFP. Would flip to a defined-risk short candidate only if term structure resolves to CONTANGO post-NFP AND the bearish divergence persists AND price rolls below ~155 AND VRP turns positive.

**Near-term sweeps (informational, 0 rubric points):** the persistence-ranked sweep tape is dominated by **pre-NFP hedging** — the entire bearish index-sweep book (SPXW $13.3B, QQQ $10.5B, SPY $9.4B, TSLA, NVDA) is Jul-2-dated protection with MIXED 30d cum-flow, not directional shorts. SMH ($781M) and MSTR ($748M) are bearish put *hedges* against the semis longs; INTC is a direction conflict (bearish persistence vs today's bullish call build); MU ($8.6B two-way) is event/straddle positioning. Only SNDK (bullish) and BE (Bloom Energy, Aug/Sep OTM call accumulation) carried bullish co-flags — both single-signal.

## 4. LEAP Builds (6–24 months)
**None.** `leap-positioning-radar` found zero DIRECTIONAL_LONG builds clearing 6-of-9 gates. The DTE>180 tape is a **risk-off / hedging tape** — dominant long-dated OI growth is ETF put / credit-protection (HYG P70/75/80 Jan-27 + a 249k-contract far-dated put roll; XLE P52.5; IBIT put-dominated; ARKK/HTZ distressed puts). The semis leadership is expressed in shorter-dated flow, absent from the long-dated book. Disqualified near-misses: NKE (MIXED conviction, 30d BEARISH), DRAM (event-vol straddle), FXI (DIRECTIONAL_SHORT), SLS/ERAS (COVERED_CALL financing), STLA (balanced lotto calls).

## 5. Volatility Surface
`vol-surface-scout` — **no clean vol-surface trade.** Every ivr100 name is high-IV for a reason, not a mispricing: the front-end is uniformly NFP-loaded (Jul-2, bare backwardation = mechanical pre-event), and per-name VRP is FAIR on AMD (−0.008), TXN (+0.040), GEV (+0.033), T/VZ (≈0).

- **FTNT** — the **one genuinely rich name**: VRP +0.28 (IV 70% vs realized 42%), 30d put-skew TAIL_HEDGING, but the tradeable rich vol is the **Aug-05 earnings hump**, not the Jul-2 NFP front — an earnings-vol structure, not a naked front sale. Implied move 2.69%.
- **TXN** — headline Jul-17 "kink" (100.2%) is a 3rd-Friday **monthly-wing artifact**, not an earnings kink (earnings Jul-28); front-end FLAT 1.037. Do not size it.
- **GEV** — most extreme front (116%) but that's NFP + 2DTE noise rising into the event (earnings Jul-22); not a calendar.
- **IV outliers:** empty — all actionable outliers are 0DTE Jun-30 pin artifacts or sub-$10 microcaps that fail the liquidity floor.
- **Earnings vol (light pre-Q2 window):** `earnings-scout` — **GIS SELL VOL** (3/4 size, reports 7/1 premarket; rich 43% front + stretched back-month tail, ~10-vol-pt crush; cleanest short of the set) and **FDS SELL VOL** (half size, 7/1 premarket, thinner back-month). PENG/PEP SKIP (flat back-month / NFP-CPI-confounded front). **No BUY VOL.** Note the VRP headwind: selling vol into a mildly-negative-VRP tape is slightly cheap-to-realized — size accordingly.

## 6. Risk & Correlation
`risk-monitor` — **conclusion: zero conviction-tier trades; standing flat is the position.**

- **Macro headline:** sticky Core PCE 3.41% + falling 10Y + strengthening USD; **NFP Thu Jul 2 (T+2) is the dominant near-term binary**, ISM Mfg T+1, CPI Jul 14 — stacked named events inside every swing horizon.
- **Correlation (`uw risk portfolio-correlation`, 30d):** the expected semis cluster **did not form** — strongest pair NVDA/MRVL 0.555 (< 0.60), EWZ/XLB 0.565 (opposite-direction = partial hedge). No pair ≥0.70 → cluster gate no-ops on every name.
- **Regime / VRP / panic:** regime permits longs but no longer rewards them (long edge is uptrend-conditional per the 06-27 audit). VRP FAIR (mild short-vol headwind → matters for GIS/FDS). **SPY front-end 0.903 CONTANGO — no panic**, gate no-ops.
- **Fundamentals verdicts (top-5):** **SNDK CAUTION** (insider MSPR −100 ×3mo + DP distribution into a target-triple FOMO blow-off; strong fundamentals prevent VETO); **DELL CAUTION** (insiders dumping millions of shares/mo + AI-server margin compression); **BMY CONFIRM** (earnings 7/30 vol play, carries a fresh 6/30 House China-clinical-trial probe + Medicare price-negotiation overhang); EWZ / XLB NA (ETFs). **No VETOs.**
- **Event-risk flags:** NFP T+2 fires −1 tier on every held-through swing name; GIS/FDS report 7/1 (the earnings *is* the play → event-exempt but VRP-headwind).
- **Debate cut:** SNDK bull 0.55 / **bear 0.75** — disconfirmation did not clear the trade (the "4× confluence" is one opening-call footprint absorbing unanimous insider distribution).
- **Breadth divergence:** `fz` pct_green 41.75% (210 adv / 292 dec) under a green index — advisory distribution tell; corroborates the narrow leadership, does not change sizing.
- **Adverse-flow watch (`uw watchlist` on `conviction_2026-06-29`):** PEP (IV-rank 84.3 — "don't buy premium here" caution, flow reads continuation not reversal) and BABA (accumulation) — no hard exits. **NVDA scan confirms bearish net flow today** → stays rejected.
- **Hedge sleeve:** post-gate directional exposure ≈ 0 → none warranted. If a tactical SNDK starter were taken against discretion, express it defined-risk (call vertical) through NFP.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**Empty — there are no HIGH or MEDIUM tier names today.** The highest scored name is SNDK at raw 3 (LOW), cut to watch. This is a valid "no edge" output.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: not applicable today — no conviction-tier trades were sized, so there is no book expectancy to display. The live sizer remains the win-rate ladder (Step 5); the fractional-Kelly sizer stays advisory until tier×expectancy is monotone on n≥30. For the record, the one scored class in play (SNDK `bullish_flow`) backtested WR 0.478 (n=138, clean) with market_excess −0.080 — a losing, sub-beta class, correctly sized to starter-then-watch.

**Conviction-scoring rubric (frozen `2026-06-12`)** is embedded verbatim in `.claude/commands/daily-analysis.md` Step 4 (weights/tier-cuts/gate membership frozen under the P0.1 freeze; the ≥9 HIGH cut failed its scheduled re-confirmation on 2026-06-12 and carries no validated ranking claim in the interim; the P0.6 out-of-regime guard caps all sizing at half).

## 8. Watch-only — single signal, no confluence
Candidates that surfaced from one Phase-1 agent (or failed the 2-agent confluence gate). **For journaling, NOT for trade entry today.**

| Ticker | Sole signal | Raw | Note |
|---|---|---|---|
| **NVDA** | dealer-positioning DEX flip LONG (cleanest in fleet) | −2 | Flip swamped by −$523M/30d flow conflict; watchlist scan confirms bearish net flow → **reject** |
| **DELL** | sector-rotation Tech-leader +1 (30d +$228M) | 1 | Fundamentals CAUTION (insider selling + margin compression) |
| **MRVL** | sector-rotation Tech-leader +1 (30d +$216M) | 1 | Single-signal; semis beta |
| **NKTR** | accumulation-hunter sole qualifier (block DP $17.95M 100% buy) | 1 | Conjunction fails — 30d options flow flat/MIXED (+$797K); DP support $69.81 |
| **EWZ** | multileg bullish call calendar + risk-reversal (repeat×2) | 2 | Cleanest multileg structure; NFP T+2; Brazil political catalyst (advisory) |
| **BMY** | multileg bullish call calendar 62.5 (into 7/30 earnings) | 2 | Fundamentals CONFIRM; carries China-probe + Medicare risk |
| **XLB** | multileg double put calendar (mild-bearish Materials, Aug) | 2 | Short = beta only (no short alpha in any decided regime, 06-27 audit) |
| **BKNG** | multileg bullish diagonal / contrarian bearish-extreme (conflict) | 1 | Informed-continuation watch; not a fade, not a sized long |
| **GIS** | earnings-scout SELL VOL (reports 7/1) | 1 | Cleanest earnings short (3/4 size) but VRP headwind |
| **FDS** | earnings-scout SELL VOL (reports 7/1) | 1 | Half size; thin back-month tenor |
| **FTNT** | vol-surface rich VRP +0.28 (Aug-05 earnings) | 1 | Earnings-vol structure, not a front sale |
| **BE** | sweep-tracker bullish 3/5 (Aug/Sep OTM call accumulation) | 0 | Sweep-persistence = 0 points; no scored co-flag |

---
*Fleet: 10 Phase-1 alpha-finders (parallel) → signal-confluence-quant → fundamentals-gate → bull/bear debate (SNDK) → risk-monitor. Rubric frozen `2026-06-12`; OUT-OF-REGIME half-cap active. Watchlist `conviction_2026-06-30` = SNDK, EWZ, BMY, XLB, DELL.*
