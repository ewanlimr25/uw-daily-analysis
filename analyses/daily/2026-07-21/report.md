# Daily Market Analysis — 2026-07-21

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL (half-size, defined-risk) on an UPTREND tape — SPY 748.28 (>20/50-SMA) but **short-gamma-adjacent** (spot below ZGL 759.2); QQQ 708.81 short-gamma (below ZGL 741.94, thin +$81M book); IWM GEX feed inconsistent (flagged). VIX 17.05 (MID). Breadth **divergent** — index green but only 45.5% of S&P names advanced (271 decliners > 229 advancers, median −0.18%) = distribution tell. Flow is Tech-led (+$2.46B) but the tape is **hedging/de-risking into the FOMC/GDP/PCE cluster**, not building conviction.
- **Rubric regime status:** OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL/UPTREND) — sizing capped at half. *(Moot today — nothing sized.)*
- **Next-session GEX (SPY/QQQ):** SPY short-gamma-adjacent · ZGL 759.2 · call wall 755 / put wall 740 → keep any 0DTE fly **tight inside 740–755**, de-risk on a break. QQQ short-gamma · ZGL 741.94 (edge of band) · 709 call wall is essentially ATM (pin candidate) / put wall 690 · size down vs SPY. **Both books are alternating regime almost daily** (noisy) — advisory, see §2.
- **Top swing build:** **NONE.** All-DROP conviction board — no name reached LOW, let alone HIGH/MEDIUM. Top raw score = 2 (NBIS, which also fails the ≥2-agent confluence gate).
- **Top LEAP candidate:** **NONE** — 0 of 13 semis/tech names qualified (all `cumulative-premium-flow` MIXED <5% of gross; META resolves to COVERED_CALL, TSM to persistent put-hedge).
- **Biggest risk:** the **AI-capex semis cluster** — 7 of today's 8 candidates (all but TLT) are transitively **one position** (pairwise corr 0.75–0.86; ETN trades as a semi). No book to hedge — the empty board *is* the hedge.

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL — "mixed signals, reduce position size, wait for clarity"; **trend UPTREND**. SPY 748.28, above 20-SMA (744.98) and 50-SMA (744.88), +0.21% 30d, −1.59% from the 90d high. Bullish flow tickers 2,350 vs bearish 3,914 → **bullish_pct 37.5%** (more names sold than bought). Guidance: half size, defined-risk, iron condors in range.
- **Per-index gamma (EOD current-state book):**

| Index | Spot | Zero-γ (ZGL) | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 748.19 | 759.2 (reliable) | +$399M | short-γ near spot (spot < ZGL) | 755 (+0.91%) | 740 (−1.09%) |
| QQQ | 708.81 | 741.94 (edge of band, 4.68%) | +$81M (thin) | short-γ (spot < ZGL) | 709 (ATM, pin) | 690 (−2.65%) |
| IWM | ~n/a | 196.03 (artifact) | −$371M | **feed inconsistent** — label "POSITIVE" contradicts negative total_gex; call wall 300 nonsensical → flagged for calibration-audit, not used |

  Both SPY and QQQ books have **flipped regime almost every session since 07-08** (NEGATIVE/POSITIVE/FULLY_NEGATIVE alternating) — a genuinely noisy gamma book that argues against high-conviction pin/fly sizing on gamma grounds alone.
- **`uw options-flow dte-volume-share` (MARKET):** 0DTE 29.9% · weeklies 30.9% · monthlies 23.3% · LEAPs 3.5% → **BALANCED** tape (institutional monthly+ share 26.8%), not retail-dominated.
- **`uw historical vrp`:** SPY **FAIR** (IV30 14.1% vs RV30 13.9%, VRP +0.0018) · QQQ **FAIR** (IV30 24.0% vs RV30 28.0%, VRP −0.0395 — realised > implied, a mild premium-*buy* tilt on QQQ). Neither side offers a clean VRP edge.
- **Macro backdrop (`fred_macro`):** yield curve **normal** (+0.37 10y2y); **core CPI 2.81% / core PCE 3.41% YoY (sticky)**; unemployment 4.2%, payrolls +57k; **10Y 4.60% and rising** (+0.14 30d); **USD strengthening** (+1.14 30d); fed funds 3.63%. Mildly hawkish/tight.
- **Forward event risk (Tier-1, inside any swing horizon):** jobless claims **07-23** (T+2) · **FOMC 07-29** (T+6 trading days, **no SEP**) · **Q2 GDP advance 07-30** (T+7) · **core PCE 07-31** (T+8). A dense three-day macro cluster 07-29→07-31 — the single most important feature of the tape.

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book (OI persists overnight) read forward as the prior for the next open. Prose-only, **0 rubric points**, no backtested predictive claim. SPY/QQQ only.

**SPY** — spot 748.19, ZGL 759.2 (reliable), regime read **short-gamma near spot** even though aggregate 0–45d total_gex is nominally +$399M (that positive GEX is carried by strikes *above* spot; the price zone itself is short-gamma). Call wall **755** (soft cap), put wall **740** (real support floor). *Read:* short-gamma character means hedging flows **amplify** moves near spot rather than dampen them. *Structure bias:* keep any 0DTE premium-selling fly **tight inside 740–755** rather than sizing wings toward the 759 ZGL; treat a break of 740 or acceleration through 755 as a de-risk signal, not a level to defend.

**QQQ** — spot 708.81, ZGL 741.94 (4.68% away, edge of the ~5% reliability band → directional-only), regime **short-gamma**, total_gex barely positive (+$81M, thin) after a fresh flip out of a 3-session FULLY_NEGATIVE stretch — a marginal, unstable flip, not a settled long-gamma book. The "call wall" at **709** is ~ATM (3 cents from spot) → reads as a **pin/magnet candidate** for the open, not far-OTM resistance; the next real +GEX cluster is 715–725. Put wall **690** (−2.65%). *Structure bias:* short-gamma + the front-end backwardation caution (below) raise the odds of a wing breach — **size QQQ down vs SPY**; treat 690 as the realistic downside stop level.

**Mandatory caveats:** EOD is a *prior, not a target* (fresh 0DTE OI recomputes the ZGL/walls in the first 30–60 min); **gap risk from FOMC/GDP/PCE (07-29→31) can jump spot through the walls** before any hedging mechanic engages; these are the SPY/QQQ **ETF** books, not the cleaner SPX/NDX index books; uw cannot isolate the D+1 (07-22) expiry — this is the 0–45 DTE proxy (07-22 confirmed 2nd/3rd-largest near-dated premium bucket, so the proxy is representative).

### 2a. Next-session 0DTE premium-selling setup (`zerodte_setup` — the validated stack)
Advisory, delta-neutral, **0 rubric points**; NOT a guaranteed edge (validation sample has no vol shock → the short-vol left tail is UNSAMPLED). Both indices verdict **GO_PREMIUM_SELL_INTRADAY**, VIX 17.05 (MID tercile):

| Index | Sell premium? | Vol state | Structure | Wings | Size | Net PnL/day (gross) | Win% | Stand-aside |
|---|---|---|---|---|---|---|---|---|
| **SPY** | yes | MID | iron fly @ 748.14 | ±0.79% | 1.0× | **+0.169%** (gross +0.269%) | 93.3% | none |
| **QQQ** | yes | MID | iron fly @ 708.76 | ±1.36% | 0.5× | **+0.296%** (gross +0.396%) | 88.3% | **front-end backwardation caution** |

`pnl_basis`: % of underlying spot notional, **gross** of costs; leading with **net** (gross − 0.10% assumed round-trip). Enter at/after the open once the gap resolves; **hold to the close, never carry overnight** (overnight entry backtests negative). Stand aside if it gaps beyond the wings. **SPY ≈ SPX** (validated identical). **QQQ weaker** (Nasdaq index book unavailable) + carries the backwardation caution — lower confidence. *This lane stays advisory permanently until a vol-shock day enters the sample AND net expectancy clears a tail-aware bar.* **The GEX §2 read (short-gamma) is a caveat on this stack — the fly's short-vol wings are less protected than a clean long-gamma day, and the FOMC/GDP/PCE gap risk sits directly inside the window.**

## 2a. Swing Dealer Positioning (1–4 weeks)
`dealer-positioning-strategist`: **no mechanized DEX flip anywhere at the index level** (SPY/QQQ/IWM all persistent negative-sign DEX with shrinking magnitude — no sign change). Two single-name flips surfaced (MU, TSM) but **both disqualified**: DEX (bullish) and vanna (call-heavy → bearish-if-IV-falls) disagree on direction, and both are **coincident with an already-realized double-digit gap** (MU +12%, TSM +5.3% same session = post-earnings) → reactive dealer-hedge catch-up, not a leading 1–4wk signal. NVDA/AMD carry positive DEX *levels* (beta, not scored flips). **No vanna squeeze fires** — VIX fell only 2 sessions (need ≥3); SPY/QQQ/IWM put-heavy books are *building* setups, not confirmed. **Swing bias: NEUTRAL.** (IWM `gex-time-series` is internally inconsistent — regime label contradicts total_gex sign on every pulled day; flagged for calibration-audit.)

## 2b. Sector Rotation
`sector-rotation-strategist`: **rotation regime = no_change** (low confidence) — Consumer Cyclical (cyclical) and Healthcare (defensive) both inflowing simultaneously fits no canonical rotation pattern. All 11 GICS sectors clear the absolute ≥0.6 persistence gate again (non-binding in a trending tape). Applying the market-relative bar, standouts were Comm Services, Consumer Cyclical, Financial Services, Healthcare — but **Financial Services was downgraded to watch-only**: 30d GICS window shows outflow, XLF (−$5.2M) and KRE (−$10.0M, with an $88.7M block sold 2.7pts below mid) both bearish, and the 5d "inflow" is a handful of crypto/fintech names (CRCL/MARA/BMNR) masking broad-financials distribution.

**Only NBIS clears the full single-name conditional gate** (Comm Services, persistence ≥0.6, cum_flow_30d +$216M aligned, ≥$50M). TSLA fails (cum_flow_30d −$391M contradicts the 5d thesis — the recurring mega-cap flow_conflict). Short-side: KRE (regional banks, high-conviction bearish confirm), Industrials leaders SPCX/RKLB/BA (but Industrials is stabilizing — a fading short, not a fresh one).

**ETF flow tape (advisory — 0 rubric points):**

| ETF | Net premium | Persistence | DP / options read | GICS agreement | Note |
|---|---|---|---|---|---|
| XLY | +$10.2M | inflow | thin urgency ($100K call sweep) | agrees (Consumer Cyclical) | direction confirmed, weak conviction |
| XOP | +$3.0M | inflow | call-sweep confirmed | Energy at median, 30d outflow | tactical-only |
| IGV | +$4.2M | inflow | top sweep is a $2.1M **put** | Tech 2nd-tier persistence | internally mixed |
| KRE | −$10.0M | outflow | $88.7M block sold below mid, put-dominated | disagrees w/ Fin Svcs GICS | high-conviction bearish |
| XLF | −$5.2M | outflow | short-dated call rolls/hedges | disagrees w/ Fin Svcs GICS | not high-conviction |

## 3. Swing Setups (1–6 weeks)
**EMPTY — no name cleared the conviction rubric into HIGH/MEDIUM/LOW.** The board is all-DROP (top raw 2). The two names passing the ≥2-agent confluence gate (STX, LRCX) are **SELL-VOL / calendar earnings-week vol plays that scored raw 1** (C13 single-owner routing stops the earnings kink from paying twice) — watch-only, not swing setups. See §5 for the vol reads and §7/§8 for the audit trail.

- **3a. Long swings (regime-aligned):** none.
- **3b. Short / fade swings (defined risk only):** none. The one index-level crowding extreme (QQQ pc-z 3.07 BEARISH_EXTREME) **aborts** on two independent gates — negative VRP + BACKWARDATION at the exact 8–10 DTE tenor lining up with FOMC/GDP/PCE = a real event-hedge bid, not a fadeable crowd.

**Near-term sweep tape (informational, 0 points):** the day's loudest single-name flow is **bearish/protective** — GOOGL $670M put sweeps (3/5 persistence), **SMH** the cleanest opening-confirmed build (two ask-side put sweeps, 520P OI +83.5k = 76% fresh opening) but 5d-mixed, and MU $213M put sweeps reading as collar/hedge against its +12% gap. Index put sweeps (SPY/QQQ/SPXW) are largely **OI-declining unwinds** (closing, not fresh opening) and contaminated by SPX box-spread/collar prints (identical size+timestamp call/put pairs — the 07-15 box signature again).

## 4. LEAP Builds (6–24 months)
**EMPTY.** `leap-positioning-radar`: 0 of 13 candidates reach 6-of-9 gates. The required `cumulative-premium-flow` (90d) returned **MIXED for every single name** (net 0.1–8% of gross — no slow-accretion signature; consistent with LEAP DTE share only 3.5% of tape). Notable disqualifications:
- **META** (closest near-miss) — genuine multi-session Jan-2027 750C OI persistence + real DP accumulation, but `conviction-matrix` explicitly resolves it to **COVERED_CALL** (call-selling for yield against the stock position, capping upside) → hard reject.
- **TSM** — persistent long-dated **put** build = downside hedge, wrong direction.
- **SNDK** — no LEAP call signature; corroborates the standing distribution flag (insider MSPR, prior heavy put premium).
- NVDA — zero LEAP-dated activity in the tape at all (100% near-dated).

## 5. Volatility Surface
Semis earnings week — IV rank pinned at **100 across the complex** (LRCX, AMAT, KLAC, NXPI, STX, MU, SNDK, NOW, TEL, ETN, TJX). Raw IV-rank saturates (19/20 at 100 = zero discriminating power); percentile-z reads are **provisional** (only 69/252 lookback days). Cleanly separating genuine dislocations from mechanical "IV-100-because-earnings-tomorrow":

| Ticker | Class | Earnings | Verdict | VRP | Note |
|---|---|---|---|---|---|
| NOW | BACKWARDATION (real) | 07-22 | **SKIP** | +0.218 sell | front-end ratio 2.19 = extreme panic, event pending — do not short into it |
| STX | BACKWARDATION (real, earnings-aligned) | 07-28 | **SELL VOL ½** | +0.195 sell | corrected ratio 1.26 (naive 1.53 mis-snapped to a pre-earnings tenor); flow confirms |
| LRCX | BACKWARDATION (real) | **07-29 = FOMC** | **CALENDAR** | +0.079 weak | crush read contaminated by same-day macro cluster |
| ETN | choppy/marginal | 07-31 | **SELL VOL ½** | FAIR | tiny 3.3% implied move; vol-surface dropped it |
| AMD | BACKWARDATION (choppy) | 08-04 | **SELL VOL ½** | FAIR | cleanest **macro-isolated** print (after the cluster) |
| MXL | complacent, lottery-shape | 07-23 | earnings-scout | +0.190 sell | 32% implied move into a 2-day print (advisory C6 lottery color) |
| KLAC/NXPI/TEL/WHR/SIMO | **UNREADABLE** | this week | hand to earnings-scout | mixed | **no near-dated tenor** (first bucket dte≈31) — kink shape unconfirmable (the recurring RMBS/SANM class gap) |
| MU / TJX / AMAT | mechanical artifacts | — | **DROP** | — | MU neg-VRP + robust percentile 68th NORMAL contradicts raw IVR100; TJX ratio 5.29 on a 177-contract wing; AMAT flat at the true 08-13 tenor |

**Calendar-spread bucket: empty** (every genuine backwardation has a catalyst inside 2 weeks or an elevated-not-falling front ratio). No single-contract whale IV-outlier hedges in the watchlist names (outlier scan is all sub-$5 penny/crypto-miner wings).

## 6. Risk & Correlation
- **Macro headline:** sticky core PCE (3.41% YoY), 10Y rising to 4.60%, USD strengthening → a mildly hawkish backdrop into a **no-SEP FOMC (07-29) + GDP (07-30) + core PCE (07-31)** three-day cluster. Any swing/vol structure held past 07-28 carries compounded, un-priced macro event risk.
- **Correlation (`uw risk portfolio-correlation` on today's candidate union):** **7 of 8 candidates are effectively one position** — AI-capex semis cluster, pairwise 0.746–0.858 (LRCX/MU 0.86, AMD/TSM 0.85, LRCX/AMD 0.84). **ETN trades as a semi** (0.79–0.80) — the AI-datacenter-capex correlation swallows the industrial label. **TLT is the only genuine diversifier.**
- **Fundamentals verdicts (top-5 by raw, hygiene — advisory, nothing sized):**
  - **NBIS — CAUTION.** Insider MSPR −78 3mo (chairman sold $1.4M into today's +18.8% NVDA-stake spike); earnings 07-29 (8d) at IV rank 93.7 → **distribution-into-strength**; corroborates Phase-1's refuted DP print + bearish-extreme pc-z. Beat streak + strong growth keep it short of VETO.
  - **AMD — CAUTION.** Insider selling **accelerating** (MSPR −85, monotonic) coincident with accumulation-hunter's RTH distribution tilt — two independent axes point to distribution under bullish-looking headline flow.
  - **STX / LRCX / ETN — CONFIRM.** Fundamentals corroborate or are neutral; insider selling reads as chronic/routine. **LRCX flagged: 07-29 earnings = FOMC day (dual-event).**
  - No VETOs. `fz` lane fully upstream-gapped (SI/float/analyst all null) — analyst axis NA-by-gap.
- **Breadth cross-check (advisory):** advancers 229 / decliners 271, **pct_green 45.53%** under a green index — **divergence flag TRUE** (distribution tell; consistent with the insider-selling verdicts).
- **Gate stack:** all 9 gates no-op/moot (nothing sized). Panic gate clean (SPY front-IV 0.763 = CONTANGO). rubric_regime half-cap remains in force (freeze-lift blocked 5 consecutive audits) but has nothing to cap.
- **Adverse-flow exit (watch-only carries):** **META** (conviction_week_2026-W28) has flipped flow-bearish (−$13.6M) into its own 07-29 earnings + FOMC week — advisory exit flag, no position. NVDA/JPM/SOFI on-thesis, quiet.
- **Hedge sleeve: NONE.** The book is empty — no net delta to hedge, and the tape is already paying up for protection (SMH P/C 4.26, HYG P/C 5.16, IV 90–100 across semis). Buying index protection here is buying what is crowded. **On an all-DROP board the empty book is the hedge** — the audited best-graded behavior of this system (DROP pile 43.3% > traded book 41.1%, 2026-07-18 audit).

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**None. Zero names reached MEDIUM or HIGH.** This is another all-DROP conviction board — the ~16th consecutive session without a sized conviction name. For completeness, the full scored board (all DROP):

**Expectancy lens** *(advisory — expectancy is not yet a live sizing axis)*: no tiered book exists this session, so per-tier realized expectancy is not computable from today's calls; the standing reference (2026-07-18 audit) is that the DROP pile has outperformed the traded book (43.3% vs 41.1%), which is why an empty board is the correct output, not a failure.

| Ticker | Raw | Tier | Components (agent · tool) | Class | Win-rate (n, src) | Fund. | Confluence gate | Pre-risk |
|---|---|---|---|---|---|---|---|---|
| NBIS | 2 | DROP | +1 sector-leader (sector-rotation · sector-flow-persistence) · +1 cum-flow accretion +$216M (quant · cum-premium-flow) | sector_rotation | NA(substrate) | CAUTION | **fails** (1 agent) | skip |
| STX | 1 | DROP | +1 earnings SELL VOL (earnings-scout · front-end-iv-ratio); vol-surface KINKED routed to 0 (C13) | earnings_vol | NA(substrate) | CONFIRM | **passes** (2 agents) | skip |
| LRCX | 1 | DROP | +1 earnings CALENDAR (earnings-scout); vol-surface KINKED routed to 0 (C13) | earnings_vol | CONFIRM* | **passes** (2 agents) | skip |
| AMD | 1 | DROP | +1 earnings SELL VOL (earnings-scout); DEX level = beta, 0 pts | earnings_vol | NA(substrate) | CAUTION | fails (1) | skip |
| ETN | 1 | DROP | +1 earnings SELL VOL (earnings-scout) | earnings_vol | NA(substrate) | CONFIRM | fails (1) | skip |
| TLT | 1 | DROP | +2 multileg directional (Jan-2028 bull call spread, macro bonds-up) −1 flow_conflict_lite (−$111M 30d opposes) | multileg_directional | NA(substrate) | NA | fails (1) | skip |
| TSM | 0 | DROP | dealer flip disqualified; leap put-hedge = 0 pts | bearish_flow | 0.581 (136, clean) | NA | — | skip |
| SMH | −1 | DROP | sweep/multileg = protection (0 pts) −1 flow_conflict_lite | bearish_flow | NA | NA | — | skip |
| MU | −1 | DROP | all lanes disqualified −1 flow_conflict_lite (+$725M MIXED, 0.8% of gross) | bearish_flow | NA | NA | — | skip |

\*LRCX CONFIRM but earnings 07-29 = FOMC day (dual-event). Σ score_components == raw_score verified on all 9 rows. `bearish_flow` clean-protocol WR **0.5809 (n=136), market-excess +11.76pp** — 5th consecutive positive clean read for the class, still scores 0 points (C19 accrual, no scored bearish line exists).

**Conviction-scoring rubric (frozen `2026-06-12`), embedded for audit:**
```
Daily conviction score = Σ:
 +1 dealer MECHANIZED DEX flip / vanna-squeeze in trade direction (verified SIGN CHANGE only)
 +3 accumulation-hunter 3+ aligned (DP+OI+smart-positioning, block-stratified) — HALVED→+1 unless cum_flow_30d confirms (aligned & ≥$50M)
 +1 multi-day OI build (oi-trend BUILDING, days≥5)
 +1 conviction-matrix DIRECTIONAL_LONG conf>70 — ONLY if dominant_signal_class==leap_directional
 +1 cum-flow net directional accretion 30d — intent-screened (0 on C28 distribution_flag / div-capture arb)
 +1 sector-rotation single-name leader — ONLY if persistence≥0.6 AND cum_flow_30d aligned AND ≥$50M
 +1 earnings-scout BUY VOL or SELL VOL
 +2 multileg-strategist directional structure (term-structure-anchored)
 +1 vol-surface-scout KINKED/BACKWARDATION with VRP-aligned bias
 -2 contrarian overcrowded long with rising pc-z (VRP positive)
 -3 flow_conflict (cum_flow_30d clearly opposite dominant class) | -1 flow_conflict_lite (MIXED) — mutually exclusive
 [TIER GATES, risk-monitor 2d]: -1 tier corr-cluster ≥0.70 | -3→ -1 tier regime conflict
Tiers: ≥9 HIGH (full) · 7-8 MEDIUM (half) · 3-6 LOW (starter/watch) · ≤2 drop.
Out-of-regime guard (P0.6): all conviction sizing capped at half until a calibration-audit re-validates post-2026-06-12.
```

## 8. Watch-only — single signal, no confluence
Names that surfaced from one agent but failed the ≥2-agent confluence gate — journaling only, **not for trade entry**:
- **NBIS** — sector-rotation single-name leader (only qualifying name), cum_flow_30d +$216M, but accumulation-hunter *refuted* the DP print (below-mid closing-cross artifact), contrarian flagged pc-z 2.065 BEARISH_EXTREME, and fundamentals returned CAUTION (chairman distribution into the spike). Watch into 07-29 earnings.
- **AMD** — earnings-scout SELL VOL (08-04, macro-isolated) but CAUTION on accelerating insider + RTH distribution.
- **ETN** — earnings-scout SELL VOL (07-31); tiny implied move, vol-surface dropped it.
- **TLT** — the one real directional multileg (Jan-2028 bull-call spread, macro bonds-up into FOMC) but 30d/90d flow both lean against it; possible financing-vintage DTE.
- **SMH** — cleanest opening-confirmed *bearish* put build (OI +83.5k) but hedge-shaped and ETF (correlation cluster).

---
*Data: `uw` CLI (Unusual Whales) + FRED macro + Finnhub fundamentals + `fz` Finviz breadth. 10 Phase-1 alpha-finders → quant → fundamentals gate → risk-monitor (debate skipped, empty board). VETO'd/DROP names excluded from watchlist per convention; write-back empty.*
