# Daily Market Analysis — 2026-06-23

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / PULLBACK_IN_UPTREND. SPY 733.58 (below 20-DMA 746.56, above 50-DMA 732.03; −3.53% off the 90-day high). **VIX 19.49, spiking +2.2.** Both SPY and QQQ closed in **FULLY_NEGATIVE 0DTE gamma** with **mechanized DEX flips negative** — dealers now amplify moves, not dampen them. Options-flow breadth bearish (34.2% bullish). The driver: a **hard semi/AI selloff on the SK Hynix HBM-expansion slowdown** (MU −13.6%, NVDA −3.7%, INTC −5.9%, SOXL −23%). Smart money is rotating *out* of semis into defensives (Cons. Defensive / Healthcare / Real Estate).
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL/PULLBACK_IN_UPTREND) — sizing capped at half` (P0.6 guard; 0/30 post-freeze calls resolved).
- **Next-session GEX (SPY/QQQ):** SPY — FULLY_NEGATIVE, ZGL null, put wall **735 (at spot)**, call wall 755; short-gamma → trend/breakout, **do not sell the straddle**, debit verticals on a 733 break. QQQ — FULLY_NEGATIVE + front backwardation, put wall **715 (at spot)**, no real call wall to 735; most trend-prone, long-vol/directional only. Advisory, see §2.
- **Top swing build:** *None at conviction.* This is a **no-edge tape** — nothing clears MEDIUM. The book is **net-short/defensive, starter-only**: NFLX short (cleanest single name — 4/4 miss-streak + 52-wk low, CONFIRM), NVDA short (express **relative vs SMH/SOXX**, +18.5pp class excess), SPY/IWM index hedges into PCE. MU is a **defined-risk SELL-VOL** into tomorrow's print, half size.
- **Top LEAP candidate:** *None.* Every long-dated build fails the cumulative-flow accretion gate (NVDA 90d −$374M); the DTE>180 tape is macro/rate hedges, not single-name conviction.
- **Biggest risk:** **One correlation book.** {MU, NVDA, SMH, INTC, SNDK} + index legs {SPY, QQQ} are all ≥0.91 correlated — a single HBM-scare position. Two Tier-1 binaries land in 48h: **MU earnings 06-24 AMC** and **Core PCE 06-25**. Hedge sleeve = **upside-tail insurance** (small SPY call vertical), because the book is already net-short.

---

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend PULLBACK_IN_UPTREND. SPY 733.58, above 50-DMA (732.03) but lost the 20-DMA (746.56); −1.23% over 30d, −3.53% from the 90d high. Breadth on the options tape is **bearish: 34.2% bullish** (2,132 bullish vs 4,104 bearish tickers of 6,236). Guidance: *half sizes, defined-risk, iron condors in range.*
- **Per-index gamma (current EOD book):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 734.36 | null | −1.80B | **FULLY_NEGATIVE** | 755 | **735 (at spot)** |
| QQQ | 715.04 | null | −0.67B | **FULLY_NEGATIVE** | 735 | **715 (at spot)** |
| IWM | 295.61 | null | negative | short-gamma (whipsaw) | — | 280/275 well |

  §2 carries the forward, next-session advisory read of SPY/QQQ with concrete 0DTE structure.
- **`uw options-flow dte-volume-share` (MARKET):** 0DTE 31.7% · weeklies 29.1% · monthlies 21.9% · LEAPs 5.0% → **BALANCED**, mildly institutional-leaning (0DTE < 50%, no retail-tape downgrade forced).
- **`uw historical vrp` (SPY):** **FAIR** — IV30 16.67% vs realized 15.03% (VRP +0.0164). No premium-selling edge at the index level; the only rich vol is single-name earnings (MU), which is crush risk, not edge.
- **Macro backdrop (`fred_macro`):** yield curve **normal** (10Y−2Y +0.34); **core CPI 2.96% / core PCE 3.29% YoY — sticky, above target**; unemployment 4.3%, payrolls +172k; 10Y 4.51% (flat 30d); **USD strengthening**; fed funds 3.63%. Sticky-inflation + strong-USD = a headwind for high-multiple semis. Forward `event_risk`: **MU earnings 06-24 AMC** · **Core PCE (May) + Final Q1 GDP + Initial Jobless Claims 06-25 (Thu, Tier-1)** · U-Mich sentiment 06-26 · NFP (June) ~07-02.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book read forward as the *prior* for the 06-24 open. Prose-only, 0 rubric points, no backtested predictive claim. SPY/QQQ only.

Both indices closed the standing 0–45d book **FULLY_NEGATIVE** — every strike carries negative net GEX, ZGL is `null`, total GEX deeply short (SPY −1.80B, QQQ −0.67B). Textbook short-gamma / vol-amplification prior: dealers sell into weakness and buy into strength, **accelerating** directional moves. No pin to lean on. This is the *recurring* chop-range state, not a fresh-and-clean structural short.

| Index | Regime | ZGL | Call wall | Put wall | Next-session 0DTE structure bias |
|---|---|---|---|---|---|
| **SPY** | short-gamma (FULLY_NEGATIVE), total −1.80B | null (unreliable) | 755 (+2.8%) | **735 (≈ spot)** | Trend/breakout. A break of 733–734 invites dealer selling toward 730/725 air pocket; reclaim 740 before any +GEX (747+) damping. **Debit verticals / directional 0DTE / long straddle on a 733 break — do NOT sell the straddle.** |
| **QQQ** | short-gamma (FULLY_NEGATIVE) + front backwardation, total −0.67B | null (unreliable) | 735 (no real wall) | **715 (≈ spot)** | Most trend-prone. Loss of 715 opens the 700 air pocket with little support; backwardation amplifies the short-gamma trend. **Long-vol / debit puts / long straddle on a 715 break.** |

**Mandatory caveats:** EOD is a *prior*, not a target — fresh 0DTE OI re-computes the map in the first 30–60 min. **Gap risk is elevated** — MU 06-24 AMC and Core PCE 06-25 sit one session out; the 06-24 tape already skews heavily to puts. ZGL is `null` (FULLY_NEGATIVE) → use total-GEX sign + spot-vs-wall, `zgl_reliable=false`. This is the SPY/QQQ **ETF** book (noisier than SPX/NDX), and the 0–45d aggregate (cannot isolate the D+1 expiry). Regime is recurring, not newly-formed.

### 2a. Next-session 0DTE premium-selling setup (`zerodte_setup`)
**Verdict: STAND ASIDE both SPY and QQQ.** The rolling backtest still grades `GO_PREMIUM_SELL_INTRADAY` (SPY mean +0.308% gross / **+0.208% net**, win 94%; QQQ +0.403% gross / **+0.303% net**, win 90% — % of spot notional, gross-of-cost basis), **but the live setup overrides it to stand-aside**: VIX 19.49 **spiking +2.2** is the short-vol left-tail regime the strategy must avoid (`sell_premium=false`, `size_scalar=0`). QQQ additionally carries **front-end backwardation (0DTE IV 1.99× VIX)** — event/gap risk. Delta-neutral only; no directional tilt; never carry overnight. **Permanent advisory / 0 rubric points** (tail unsampled). Today the engine's instruction is simply: don't sell 0DTE premium into a spiking VIX.

## 2a. Swing Dealer Positioning (1–4 weeks)
- **`dealer-positioning-strategist`:** Index dealer positioning **flipped to negative gamma / short-delta-hedge** this session — both SPY and QQQ qualify the mechanized DEX-flip trigger, GEX-regime-flip-confirmed 06-22:
  - **SPY — swing_bias SHORT.** net_dex +5.2B (6/18) → −10.1B (6/22) → **−42.1B (6/23)**, preceded by 5 consecutive positive sessions; flip ≥ 0.25× trailing-median (2.6× by 6/23). front-end-iv-ratio **1.249** (backwardation, front panicked).
  - **QQQ — swing_bias SHORT (cleanest flip).** net_dex +12.0B (6/22) → **−24.9B (6/23)**, prior 6 sessions positive, |flip| 3.5× median. front-end-iv-ratio **1.443** (highest of the complex; MU sits directly under QQQ).
  - **IWM — NEUTRAL.** DEX whipsaws below the magnitude floor; no clean flip.
- **No vanna-squeeze fires** — all three index books are put-heavy (squeeze *fuel*) but **VIX is rising**, so the falling-VIX leg fails. This is vanna **pressure**, not a squeeze. *The single most important toggle:* if VIX rolls over for ≥3 sessions with the books still put-heavy, this flips to a LONG vanna-squeeze setup.
- This is **practitioner narrative (Karsan/SqueezeMetrics), not validated edge** at the 1–4wk horizon — a modest SHORT/defensive lean that gives the pullback mechanical fuel into MU (06-24) and the 06-25 macro cluster.

## 2b. Sector Rotation
- **`sector-rotation-strategist`: `rotation_regime = no_change` (confidence low).** No sector clears the market-relative bar (top-third persistence + above-median magnitude + uncontradicted). The tape is a broad pullback-in-uptrend, not a clean rotation.
- **Tech divergence resolved as distribution.** Raw call-premium shows Tech +$3.85B inflow, but the DP/smart-money lens shows Tech **−$546M outflow**, and the SMH ETF tape is distribution-flavored (below-mid DP prints + 540/600 puts against a deep-ITM Jan-27 400C) → hedged/rolled, not directional accumulation. Tech is **downgraded**.
- **Only directionally-clean read is de-risk:** Consumer Cyclical (−$293M, the lone net-negative sector; TSLA/AMZN/RCL bleeding) and Healthcare outflow. Appendix watches, not trades.
- **No single-name leader clears the conditional +1 gate** (every candidate |cum_flow_30d| < $50M).

**ETF flow tape (advisory)** — instrument layer the GICS aggregates can't see:

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| SMH | inflow (+$138M, #1) | strong/5d | below-mid (distribution) | Jan-27 400C ask + 540/600P | **disagree** (Tech DP −$546M) | n/a (downgraded) |
| XLP | inflow (+$18.3M) | bullish | at/above-mid | deep-ITM 105P hedge | n/a → Cons. Def | — |
| GDX | inflow (+$14.4M) | bullish | at/above-mid (real accum) | 80P Sep hedge | partial (Materials) | NEM, WPM |
| XLV | outflow (−$4.9M) | bearish | above-mid | mixed C + 2028 160P | **agree** (HC outflow) | JNJ, BSX, PFE |
| EWY | outflow (−$3.9M) | mixed→bearish | above-mid (creation) | 190/200/215 PUTS | n/a (geographic) | — |
| XLI | outflow (−$1.8M) | bearish | below-mid | 177/179 put-heavy | **disagree** (Industrials 1.0 inflow) | — |

Two GICS↔ETF disagreements (SMH↔Tech, XLI↔Industrials) force both nominal rotating-in candidates to **watch-only**. ETF tape is advisory — 0 rubric points.

## 3. Swing Setups (1–6 weeks)
**No name cleared MEDIUM conviction.** Everything below is **starter or watch-only** under the P0.6 half-cap. Invalidations anchor to dark-pool levels where available (C34).

### 3a. Long swings (regime-aligned) — *all watch-only; longs fight a negative-gamma down-tape*
| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| INTC | 2 (DROP) | CONFIRM long — 4/4 beats, **Apple chip partnership** + BofA semi-upgrade + bullish ITM call ladder (06-26 event). But still GAAP-unprofitable; long into a semi down-tape. | 06-26 call ladder / debit call spread | Loses event bid; MU 06-24 read-through breaks the complex | **watch-only** (regime −1, cluster −1, event_risk −1) |
| CART | 1 (DROP) | Lone clean accumulation — DP mega+block buy_ratio 1.0, 5-day OI build, conviction DIRECTIONAL_LONG @55. Single agent; sub-$50M flow. | starter call / stock | Loses **$46.09 DP shelf** (then $45.37); OI turns flat 2+ sessions | **watch-only** (single signal, regime −1) |
| SMH | 1 (DROP) | Multileg **barbell** — long Jan-27 400C LEAP + 540/600 put hedge (structurally bullish, tactically hedged). | defined-risk barbell | Breaks 540 (put hedge ITM) + 400C OI bleeds | **watch-only** (cluster −1 vs INTC, regime −1) |

### 3b. Short / fade swings (defined-risk only)
| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **NFLX** | 2 (DROP) | **Cleanest single name.** CONFIRM short — 4/4 **miss-streak** + insider selling + 52-wk low ($72.82, −45.7% off high) + margin-warning narrative. NOT in the semi cluster. | Put diagonal (KINKED 07-17 earnings) — sell elevated event vol, short delta | RSI 21 short-cover bounce; a beat snapping the 4-miss streak on 07-16 AMC | **starter** (half-cap) |
| **NVDA** | 1 (DROP) | Bearish distribution — Tier-1 OPENING_PUT_PRIME 220P (size/OI 2.36, $9.99M) + DP mega buy_ratio 0.063 ($1.29B single sell print @$200.04) + cum-flow 90d −$374M. Class excess **+18.5pp** vs SPY-short. But IV-rank only 30, OI tape is call-lotto-heavy (250C +32.6k); business fights the short (squeeze risk). | **Express RELATIVE: NVDA short vs SMH/SOXX pair** (nets the shared semi beta); cap notional | A strong MU 06-24 guide reverses the semi tape → squeeze; any AI-capex re-acceleration headline | **starter, relative** |
| **SPY** | 2 (DROP) | Regime-aligned index short — mechanized DEX flip + FULLY_NEGATIVE gamma; cum-flow −$1.5B aligned. | Tactical hedge-short / defined-risk put spread | Reclaim of 740 (+GEX damping); benign PCE 06-25 | **starter** (half-cap, event_risk −1) |
| **IWM** | 2 (DROP) | Macro downside hedge into **Core PCE 06-25** — 07-17 285/283/281/280 put ladder sitting in IWM's deepest dealer short-gamma well. | Defined-risk put spread (07-17) | IWM holds 285 through PCE; ladder OI unwinds | **starter** (defined-risk, half-cap) |

**Near-term sweeps (informational, 0 rubric points):** **SPCX** — 4/5 persistence, opening-confirmed bullish call build (OI +419k, 8:1 inc:dec) — the one clean directional opening build, but flow conflicts with a 90d-bearish accretion (leap-radar disqualified); **watch-only**. **SNDK** — 4/5 bullish opening build but semi-adjacent (MU readthrough = event vol). The entire 5/5 top of the book (SPY/QQQ/IWM/TSLA/NVDA/MSFT/META) is **index hedge flow** (sweep-bearish but cum-flow flat) — regime color, not directional shorts.

## 4. LEAP Builds (6–24 months)
**ZERO qualifying LEAP candidates.** Every DTE>180 single-name build fails **Gate 4 (cumulative-premium-flow accretion)** — flat, MIXED, or wrong-direction:

| Ticker | Long-dated build | First failing gate | Reason |
|---|---|---|---|
| NVDA | C460 Jun-2027 (lotto) | Gate 4 — **90d −$374M bearish** | wrong-direction flow; deep-OTM tail |
| AMD | P290 Jun-2027 | Gate 4 + put-side | 30d −$160M reversing; the long-dated build is a *put* |
| TSM | none | Gate 4 — 90d +$344M but 30d −$199M | recent flow rolling over |
| CMPS | C10/C20 Jan-2027 | Gate 8 — COVERED_CALL | yield-enhancement, not a LEAP buy |
| DRAM | C115 Jan-2027 | Gate 8 — MIXED | (Roundhill Memory ETF, not a single name) |
| IBM | none (DTE≥180) | Gate 2 — no fresh LEAP build | only Step-0 name BULLISH 90d (+$290M) but reverts MIXED 30d |

The long-dated tape is dominated by **macro/rate hedges** (IEF/TLT/LQD/HYG, XLE/XLU/FXI puts) and index insurance — financing artifacts, not conviction. Correct call: **abstention.**

## 5. Volatility Surface
- **MU is the single live event** — IV-rank 100, front-ratio 1.681, ±10.9% implied, **06-24 AMC**. It drags the whole IV-100 semi complex (SMH/SOXX/AMD/TSM/LRCX/AMAT/WDC/NBIS/EWY/EEM) by sympathy. **This is earnings backwardation that WILL crush — not a free calendar.** Verdict from earnings-scout: **SELL VOL, HALF SIZE, defined-risk iron fly only** — front 192.8% IV collapses toward the ~115% 31-DTE shelf, *but* the 1y back-month skew is **COMPLACENT (−0.01)** — the tail is not priced, so naked short-vol is dangerous (see §6 debate).
- **No tradeable clean calendar today.** VRP is FAIR (no sell-vol tailwind); every backwardation name is event-pending at front-ratio > 1.10 — panic-persisting holds, not panic-resolving calendars.
- **WDC — the one genuine surface dislocation:** an isolated **07-17 220% IV kink** (vs ~105% neighbors, thick 6,115-contract tenor). But it sits inside the IV-100 semis complex with front-ratio 1.475 and overlaps monthly OPEX — **do not trade it as a short-the-kink calendar** until a catalyst is confirmed in that window; otherwise an OPEX liquidity artifact that normalizes.
- **SMH is the only back-month TAIL_HEDGING name** (1y skew +0.065) — index-level put-hedging demand across the semi ETF while every single-name semi back-month is COMPLACENT. Regime color (consistent with PULLBACK + VIX +2.2), not a single-name dislocation.
- **Data caveat:** `iv-percentile-zscore` returned nulls (`dates_used: 50` < the ≥120 floor) — the robust Goyal-Saretto percentile is dark today; all IV-rank-100 reads are raw/provisional.

## 6. Risk & Correlation
- **Macro headline:** sticky core PCE 3.29% / core CPI 2.96%, USD strengthening, 10Y 4.51% flat — restrictive-leaning into **Core PCE (May) 06-25** and **MU earnings 06-24 AMC**, both Tier-1 binaries inside 48h.
- **Correlation — ONE book.** `portfolio-correlation` on today's union: **AI_semi_cluster {MU, NVDA, SMH, INTC, SNDK} + index legs {SPY, QQQ}**, all pairwise ≥0.91 (NVDA/QQQ 0.998, MU/SMH 0.968, SPY/QQQ 0.940). Treat as a single HBM-scare position. INTC is the kept long (highest-scored), SMH/CART/SNDK auto −1 as lower-scored cluster longs; NVDA's short is the cluster-aware **relative vs SMH/SOXX** expression that nets the shared beta. IWM (small-cap-rate) is the least-correlated index leg.
- **Fundamentals verdicts (top names):** MU **CAUTION** (−1; vol-short into an un-cleanly-priced binary — −13.6% pre-print gap, BofA $1,500 PT, Anthropic AI-memory deal = fat two-sided tail) · NVDA **CAUTION** (−1; insider MSPR −63.8 + DP sell-tape support the short, but 3/3 beats / +70% growth / 64% margin fight it — squeeze risk, **not a VETO**) · INTC **CONFIRM** · NFLX **CONFIRM** (every axis supports the short). **No VETOs.**
- **Event-risk flags:** MU 06-24 (own earnings, T+1) on the whole semi cluster; Core PCE 06-25 (T+2) on every undefined-risk swing; NFLX 07-16 (outside today's structures).
- **Debate-disconfirmation cuts:** NVDA **0.65/0.65 TIE** → −1 tier (did not clear; both sides → express relative, cap notional, MU 06-24 = invalidation checkpoint). MU **0.65/0.65 TIE** → −1 tier (both flag the fat two-sided tail + complacent skew → wide defined-risk wings, not a high-conviction harvest).
- **Adverse-flow exits** (carried `conviction_2026-06-22` = [MU, SPY, WDC, FDX, BSX]): **WDC = EXIT** (a 06-18 bullish-kink carry now shows bearish flow + IV-rank 100 — flow flipped against the thesis). FDX/BSX = exit if carried long (adverse flow). MU/SPY short-theses re-confirmed.
- **Breadth cross-check (fz, advisory):** 286 advancers / 216 decliners, **pct_green 56.86%** — the broad equity tape is mildly *green* while the options-flow tape is heavily *bearish* (34.2% bullish). No hard divergence flag (pct_green > 50), but the split is a distribution-into-strength tell worth noting; worst mover SNDK −13.64%, top AXON +5.61%. Advisory, does not change sizing.
- **Hedge sleeve:** the post-gate book is **net-SHORT/defensive** (SPY + IWM + NFLX + NVDA-relative shorts vs a defined-risk MU vol play; every long floored to watch). Correct tilt for a negative-gamma down-tape → the hedge is **upside-tail insurance**: a small SPY ~1-week ~3% OTM call vertical to cap a gap-up if PCE 06-25 prints benign or MU 06-24 blows out. **Do not add downside hedges** — that doubles the directional bet.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**None.** No name reached MEDIUM (raw ≥ 7) this session. The top score is **MU raw=3 (LOW)**.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no qualifying tier-population this session to compute realised per-tier expectancy; the live sizer remains the win-rate ladder (Step 5) and the C3 fractional-Kelly sizer stays advisory (tier×expectancy not yet monotone on n≥30). The single salient expectancy fact today is the **bearish_flow class clean WR 0.4519 (n=135) with market_excess +18.5pp** — single-name shorts beat the SPY-short over the same windows, but a sub-0.50 absolute hit-rate floors every bearish_flow short at *starter*.

**Per-name audit (the only scored single name + the starter shorts):**

| Ticker | Dir | raw | tier | dominant_class | win_rate (n, source) | mkt_excess | fund. | debate (bull/bear) | gates applied | final size |
|---|---|---|---|---|---|---|---|---|---|---|
| MU | vol_short | 3 | LOW | earnings_vol | NA(substrate) | NA | CAUTION (−1) | 0.65 / 0.65 (−1) | event_risk(own ER, exempt-but-noted), rubric_regime(half) | **starter, defined-risk wide-wing fly** |
| SPY | short | 2 | DROP | gamma_breakout | NA(substrate) | NA | NA (ETF) | not debated | event_risk(PCE −1), rubric_regime(half) | starter (tactical hedge) |
| IWM | short | 2 | DROP | multileg_directional | NA(substrate) | NA | NA (ETF) | not debated | event_risk(PCE, defined-risk exempt), rubric_regime(half) | starter |
| NFLX | short | 2 | DROP | multileg_directional | NA(substrate) | NA | CONFIRM | not debated | rubric_regime(half) | starter |
| NVDA | short | 1 | DROP | bearish_flow | 0.4519 (135, backtest_clean) | **+0.1852** | CAUTION (−1) | 0.65 / 0.65 (−1) | cluster(relative expr), rubric_regime(half) | starter, **relative vs SMH/SOXX** |
| INTC | long | 2 | DROP | multileg_directional | NA(substrate) | NA | CONFIRM | not debated | regime −1, cluster −1, event_risk −1 | watch-only |
| CART | long | 1 | DROP | dark_pool_accumulation | NA(substrate) | NA | — | not debated | regime −1, single-signal | watch-only |
| SMH | long | 1 | DROP | multileg_directional | NA(substrate) | NA | — | not debated | cluster −1, regime −1 | watch-only |
| QQQ | short | 0 | DROP | gamma_breakout | NA(substrate) | NA | NA (ETF) | not debated | redundant w/ SPY | skip |

**Watchlist write-back:** `conviction_2026-06-23 = [MU, SPY, IWM, INTC, NFLX]` (mechanical top-5 by raw_score; no VETOs). NVDA carried as a relative-pair starter but not written to the group.

### Conviction-scoring rubric (Step 4, frozen `2026-06-12`) — embedded for audit
```
Daily conviction score = Σ:
  +1  dealer-positioning MECHANIZED DEX flip / vanna-squeeze in trade direction (verified sign change; demoted +3→+1, 2026-06-12 P0.4)
  +3  3+ aligned accumulation (DP+OI+smart-positioning, block-stratified institutional) — CONJUNCTION (C11): full +3 only if cum_flow_30d sign-aligned AND |cum_flow_30d|≥$50M; else halved +3→+1
  +1  multi-day OI build (oi-trend BUILDING, --days ≥5)
  +1  conviction-matrix DIRECTIONAL_LONG conf>70 — CONDITIONAL (leap_directional only)
  +1  cum-premium-flow net directional accretion (30d) — INTENT-SCREENED (no C28 flag; no div-capture)
  +1  sector-rotation single-name leader — CONDITIONAL (persistence≥0.6 AND cum_flow aligned AND |cum_flow_30d|≥$50M)
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored)
  +1  vol-surface-scout KINKED/BACKWARDATION with VRP-aligned bias
  +1  opex-pin-strategist top-5 (OPEX week only)
  -2  contrarian overcrowded long + rising pc-ratio-zscore (informed-flow continuation penalty)
  -3  flow_conflict (30d cum-flow clearly opposite dominant class) / -1 flow_conflict_lite (MIXED) — mutually exclusive
  [TIER GATES, risk-monitor 2d]: -1 tier correlation cluster; -1 tier regime conflict (NOT score points)
Tiers: ≥9 HIGH (full) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 drop.
Sweep-persistence = 0 points. signal-confluence = funnel-seed only (not scored, not a gate).
P0.6 OUT-OF-REGIME guard ACTIVE: all conviction-tier sizes capped at half.
```

## 8. Watch-only — single signal, no confluence
For journaling, **not** for trade entry today:
- **SPCX** — sweep-tracker only: 4/5 persistence bullish, opening-confirmed (OI +419k). Flow conflicts with 90d-bearish accretion; leap-radar disqualified. fz fundamentals unreliable.
- **SNDK** — sweep-tracker only: 4/5 bullish opening build, but semi-adjacent (MU 06-24 readthrough = event vol); was today's worst breadth mover (−13.6%).
- **WDC** — vol-surface only: isolated 07-17 220% IV kink, flagged "do not trade as calendar" (OPEX/event artifact). **Also the adverse-flow EXIT** from yesterday's conviction group.
- **CART** — accumulation-hunter only (single agent): clean DP buying ($46.09 shelf) but sub-$50M flow and no second confirming agent → fails the confluence gate.
- **INTC / SMH** — multi-agent but cluster/regime-gated to watch (see §3a).

---
*Generated 2026-06-23 post-close · rubric `2026-06-12` (frozen) · OUT-OF-REGIME (half-cap) · 11 Phase-1 agents + Phase-2 quant→fundamentals→debate→risk. No HIGH/MEDIUM names — a valid "no-edge" day.*
