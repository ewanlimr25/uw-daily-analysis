# Daily Market Analysis — 2026-07-07

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL (trend UPTREND). SPY 747.71 (above 20SMA 741.29 / 50SMA 739.01, −1.24% 30d, −1.67% from 90d high). VIX 16.13 (LOW). Flow breadth bearish-tilted (bullish_pct 34%) against green price breadth (56% advancers) — a mild distribution tell. Next-session SPY/QQQ gamma both FULLY_NEGATIVE (short-gamma), but the regime label is whipsawing daily — low confidence. Sector tape: broad risk-on inflow, no rotation; today a single-day chip-sector rout (Strait-of-Hormuz oil spike).
- **Rubric regime status:** OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half. Moot this session — empty board.
- **Next-session GEX (SPY/QQQ):** SPY short-gamma, ZGL null/unreliable, call wall 760 / put wall 747 (spot trapped in a 747–748 short-gamma trench); QQQ short-gamma, ZGL null, call wall 730 / put wall 700 (deepest −GEX print 710 at-the-money). Both advisory, see §2 — and heavily caveated: a large share of today's negative gamma is 0DTE OI expiring tonight, and the regime has flipped almost daily.
- **Top swing build:** **None.** Empty conviction board — all 5 rubric-eligible names dropped below the raw≥3 floor.
- **Top LEAP candidate:** **None.** No name cleared the 6-of-9 LEAP gate (all failed the 90d accretion signature).
- **Biggest risk:** `semis_beta_cluster` = {MRVL, SMH} (corr 0.813, +NVDA soft-watch 0.665) — had any been sized, front-end panic (SMH FEIR 1.529, META 1.112) on the one-day oil-driven chip rout is exactly the concentration the cluster/panic gates down-tier. The empty book already carries zero of that risk.

**Bottom line:** A correctly empty board. The three bullish mega-caps (NVDA, PLTR, META) all carry net-bearish 30-day premium flow that mechanically triggers flow_conflict against their long theses; MRVL is clean but one point short of LOW; SMH is a genuine flow-vs-dealer divergence. No sizing, no hedge, no watchlist write-back. This continues the empty-board streak (07-01, 07-02, W27, 07-06).

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend UPTREND. Market breadth: 2,127 bullish / 4,131 bearish flow tickers (bullish_pct 34%). Guidance: half position sizes, favor defined-risk, iron condors in range.
- **Per-index next-session gamma** (EOD 0–45d book, advisory — see §2):

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 747.49 | null (unreliable) | −951.2M | FULLY_NEGATIVE | 760 (+1.7%) | 747 (spot in 747–748 trench) |
| QQQ | 709.68 | null (unreliable) | −1,003.2M | FULLY_NEGATIVE | 730 (+2.9%) | 700 |

  (IWM omitted from the next-session advisory by design — SPY/QQQ only.)
- **`uw options-flow dte-volume-share`:** 0DTE 31.7% / weeklies 29.2% / monthlies 26.5% / LEAP 4.8% → BALANCED (regime_hint). Neither retail-blowout nor institutional-positioning extreme.
- **`uw historical vrp` (SPY):** −0.0162, regime FAIR (IV30 13.66% vs realized 15.28% — IV marginally below realized, no clean premium-selling edge).
- **Macro backdrop** (`scripts/fred_macro.py`): yield curve normal (+0.36 10Y-2Y), core CPI 2.96% YoY, core PCE 3.41% YoY (sticky-above-target), unemployment 4.2%, payrolls soft +57k, 10Y 4.48% (falling 30d), USD strengthening, fed funds 3.63%. Net: disinflation stalling, labor softening — a "hold" backdrop into the Jul 28–29 FOMC.
- **Forward event risk (Tier-1, T+0 = 2026-07-07):** CPI ~Jul 14 (T+5) · PPI ~Jul 15 (T+6) · retail sales ~Jul 16 (T+7) · FOMC minutes Jul 8 · FOMC decision Jul 28–29 (~T+15). Any swing sized this week carries un-priced CPI/PPI risk.

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, prose-only, 0 rubric points, no backtested predictive claim.** EOD dealer-gamma book read forward as the prior for the next open.

**SPY** — Short-gamma / trend regime. The book is negative from ~726 through 750; dealers are short gamma directly at spot (747–748 trench), so hedging *amplifies* whichever direction breaks first — vol expansion / trend continuation on a break, not the pin/mean-revert of a positive-GEX day. No meaningful positive floor below spot (740, 735 are air pockets); the only positive pocket is the thin 760 call wall (a deceleration point, not a hard cap). **Structure bias:** short-gamma normally argues for debit verticals / directional 0DTE, but this cuts against the Step-0 premium-sell base case (§2a) and the multi-day book is too unstable to override the VRP read — size small, prefer defined-risk directional if trading the GEX read directly.

**QQQ** — Same pattern: deepest −GEX print (710, −395M) sits essentially ATM (spot 709.68), a short-gamma trench not a floor. 700 is a secondary air pocket; 730 (+27.6M) is weak resistance likely blown through on a real move. Same tension with the premium-sell base case.

**Regime-freshness cross-check (critical qualifier):** SPY flipped POSITIVE→FULLY_NEGATIVE→NEGATIVE→POSITIVE→FULLY_NEGATIVE across the last 10 sessions with a reliable ZGL on only a handful. Today's FULLY_NEGATIVE is **one noisy print in a fast-oscillating book, not a stable structural regime** — treat the trend/expansion read with real skepticism.

**Mandatory caveats:** EOD is a prior refreshed by fresh 0DTE OI in the first 30–60 min; a large share of today's negative gamma is 0DTE OI expiring tonight (the true D+1 prior is likely less extreme once that clears — `gex --dte-max 1` cannot isolate it); gap risk voids the map (cross-ref the CPI/PPI calendar); ZGL null/unreliable on both (FULLY_NEGATIVE), fall back to total_gex sign + spot-vs-wall; this is the SPY/QQQ ETF book, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — the validated stack)
The GEX walls above are a map, not a pin (wall-as-magnet backtested NO_GO). What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, NOT a guaranteed edge (validation sample has no vol shock — short-vol left tail UNSAMPLED). Backtest verdict: **GO_PREMIUM_SELL_INTRADAY** (both indices).

| Index | Sell premium | Vol state | VIX | Implied move | Expected range | Size scalar | Gross / Net PnL (%spot, per day) | Structure |
|---|---|---|---|---|---|---|---|---|
| SPY | yes | LOW | 16.13 | 0.76% | 1.24% | 0.50 | +0.308% / **+0.208% net** (win 94.9%, n=59) | wider iron condor, wings ≈ ±1.24% |
| QQQ | yes | LOW | 16.13 | 1.63% | 1.90% | 0.25 | +0.399% / **+0.299% net** (win 88.1%, n=59) | wider iron condor, wings ≈ ±1.9% — **half size** |

- **Lead with net, not the win-rate:** the gross win-rate overstates a negatively-skewed short-vol edge; net figures are gross minus an assumed 0.10% round-trip cost. SPY ≈ SPX (trade either); **QQQ weaker/lower-confidence** (Nasdaq index book unavailable) and flagged **front-end backwardation (0DTE IV 1.60× VIX) → event/gap risk, half size**.
- **When:** enter at/after the open once the gap resolves; hold to the close; **never carry overnight** (overnight entry backtested negative). If it gaps beyond the wings, stand aside.
- **Direction:** none — delta-neutral. **Promotion bar:** stays advisory permanently until a vol-shock day enters the sample AND net expectancy clears a tail-aware bar.

## 2a. Swing Dealer Positioning (1–4 weeks)
`dealer-positioning-strategist` — **no mechanized DEX flip anywhere** (the scored rubric line is unfed today). Every put-heavy book fails the vanna-squeeze test because VIX *upticked* into the close (15.57→16.13) — "vanna pressure, not squeeze."

| Ticker | DEX state | Flip? | Vanna | GEX regime | Swing bias |
|---|---|---|---|---|---|
| SPY | POSITIVE, deteriorating (+3.7B ← +30.3B) | no | CALL-HEAVY | whipsaw/artifact | NEUTRAL |
| QQQ | NEGATIVE, whipsaw | no | PUT-HEAVY | whipsaw/artifact | NEUTRAL |
| IWM | NEGATIVE, deepening (3 straight, 2.5× median) | no (continuation) | PUT-HEAVY | whipsaw/artifact | SHORT lean |
| META | POSITIVE, improving (+3.24B→+7.81B) | no | CALL-HEAVY | clean POSITIVE | LONG lean (FEIR 1.112 backwardation = earnings window) |
| PLTR | POSITIVE, stable | no | CALL-HEAVY | clean POSITIVE | LONG lean (FEIR 0.976 flat) |
| **SMH** | **NEGATIVE, deepening (−10.97B)** | no | PUT-HEAVY | **clean FULLY_NEGATIVE 10-session** | **SHORT lean** (FEIR 1.529 steep) |

**Key divergence — SMH:** Step-0 tags it "top bullish flow" (put-selling), but the dealer book is decisively negative and deepening, GEX FULLY_NEGATIVE across all 10 sessions, front-end panic the steepest of any name. A level/trajectory read (not a mechanized flip → 0 scored points), but a real flow-vs-dealer divergence.

## 2b. Sector Rotation
`sector-rotation-strategist` — **rotation_regime: no_change (low confidence).** All 11 GICS sectors show INFLOW with persistence tied at 1.0 (Energy 0.8) — a broad risk-on tape with nothing being sold to fund the buying, so no sector-vs-sector rotation to call. Tech's aggregate options-premium surge ($19.28B/5d, the largest) is **single-name concentrated, NOT confirmed by its own instrument tape** (XLK MIXED, SMH MIXED/put-heavy, IGV outflow) → concentrated mega-cap/semi single-name buying, not a broad Tech rotation.

**Only two single names clear the conditional sector-leader +1 gate** (persistence ≥0.6 AND 30d cum-flow aligned AND ≥$50M): **MRVL** (+$197.4M) and **LLY** (+$65.6M). Every other today's-leader (PLTR −$177M, META −$71M, GOOG −$171M, AMZN −$311M) is a fresh reversal against a bearish 30-day base, or too small (MCD, CNC, UMC).

**ETF flow tape (advisory):**

| ETF | Net prem dir (5d) | Persistence | DP positioning | GICS agreement | Note |
|---|---|---|---|---|---|
| XLV (Healthcare) | inflow | BULLISH +$3.36M | — | agree | leaders LLY, CNC |
| XLY (Cons. Cyclical) | inflow | BULLISH +$2.01M | — | agree | leaders AMZN, MCD |
| SMH (Tech/semis) | mixed | MIXED +$11.6M | strong buy-blocks BUT top-5 sweeps all bid-side puts | **disagree** — Tech's $19B GICS surge NOT ETF-confirmed | |
| XLK (Tech) | mixed | MIXED +$0.77M | — | **disagree** | Tech SPDR flat vs GICS aggregate |
| EWT (Taiwan) | **outflow** | BEARISH −$4.86M | strong seller-aggression | n/a | de-risking watch |
| EWY (Korea) | **outflow** | MIXED −$6.78M (worst of 21) | seller-aggression | n/a | de-risking watch |
| XBI (Biotech) | **outflow** | BEARISH −$4.67M | mixed | disagree (XLV agrees) | Healthcare/biotech bifurcation |
| XLI (Industrials) | outflow | BEARISH −$3.28M | — | disagree | |

Rotating-out candidates are ETF-instrument-only (EWT, EWY, XBI, XLI) — none maps to a GICS sector in aggregate outflow. Watch as short-vol/short candidates if persistence turns.

## 3. Swing Setups (1–6 weeks)
**No high-conviction swing setups today.** All five rubric-eligible names dropped below the raw≥3 floor. The scored breakdown is in §7; the read on each:

### 3a. Long swings (regime-aligned)
- **MRVL (raw 2 — DROP):** the cleanest long on the board and still one point short of LOW. +1 sector-leader + +1 cum-flow accretion (+$197.4M 30d, intent-screened clean). Killed by the raw floor; even if it cleared, the dominant `bullish_flow` class backtests WR 0.457 (n=140) with market_excess **−0.107** (index-beta, not edge → floored to starter). Debate: bull 0.55 / bear 0.85 (did not clear). Fundamentals CONFIRM. Today's freshest OI-build is a 240P (put) contradicting the 5d bullish window.
- **NVDA (raw −1 — DROP):** the strongest *structure* on the tape — multileg bullish call diagonal (long Sep 195C / short Jul 200C, ratio 0.96, repeat 3, +2) — but fully swamped by −3 flow_conflict on −$337.2M net 30d premium opposing the long. Fundamentals CAUTION (insider MSPR −65, but reads as the standing 10b5-1 cadence, not fresh distribution). The canonical un-penalised-flow-conflict case.
- **META (raw −1 — DROP):** dealer LONG lean + Muse AI product pop, but −1 flow_conflict_lite (−$71M), panic gate FIRES (FEIR 1.112), fundamentals CAUTION ($1.4T litigation trial Aug; earnings 07-29 stacks a CPI→PPI→earnings corridor).
- **PLTR (raw −3 — DROP):** drops hardest — zero positive scored lines, −3 flow_conflict on −$177M. Fundamentals CONFIRM (4/4 beats, DA Davidson upgrade PT $175) — the bearish flow reads as profit-taking after June's −25% drawdown, not deterioration, but the rubric correctly won't size a long against −$177M of opposing premium.

### 3b. Short / fade swings (defined risk only)
- **Contrarian-scanner: zero fades.** VRP negative (no premium cushion) + single-name-continuation discipline block every P/C extreme. **SMH** carries a genuine dealer-short/tail-hedge divergence (see §2a) but is contested by bullish put-selling — watch, not a sized short. **LMT** flagged as a short-continuation watch (informed bearish flow −$1.29M vs flat tape). **IWM** dealer SHORT lean. All watch-only.

**Near-term sweeps (informational, 0 points):** cleanest directional sweeps were SNDK (bullish put-selling 5/5), SMH (bullish, contested), PLTR (bullish 3DTE urgency). Index names (SPXW/SPX/SPY) are collar / synthetic-long / box structures, not directional — narrative color only.

## 4. LEAP Builds (6–24 months)
**Empty.** `leap-positioning-radar` — no candidate reaches the 6-of-9 gate. Every DTE>180 name failed Gate 4 (90d cumulative-premium-flow accretion signature — all MIXED/flat/wrong-direction). Two structural hard-rejects: **RIVN** (HEDGED_LONG — collared long, stock + 2028 protective put), **IREN** (COVERED_CALL — yield enhancement, capped upside). NFLX/META/PLTR/SNDK all MIXED conviction-matrix. Re-screen after CPI (Jul 14) / FOMC (Jul 28–29) clears — pre-event long-dated books stay noisy/hedged.

## 5. Volatility Surface
`vol-surface-scout` — **one coherent semis/AI-complex event building into Fri 2026-07-10.** Every AI/semis name (INTC, SMH, AMD, BE, DELL, LRCX, WDC, SNDK, ARM) shows *rising* front-end-iv-ratio over the last 3 sessions; QQQ flipped CONTANGO→BACKWARDATION while SPY stayed CONTANGO — a tech/semis-specific event risk, not a broad-market print. **Zero calendar candidates authorized** (panic escalating, not resolving — the disqualifier fires on all).

| Name | Structure | IV context | VRP | Implied move | Bias |
|---|---|---|---|---|---|
| **WDC** | genuine KINK at 07-17 (avg_iv humps 180%→242%→111%) | z 3.24, iv_rank 100 | FAIR | ~16.3% | HOLD — unexplained event (earnings 07-29 doesn't align) |
| **BE** | BACKWARDATION | z 4.51 (largest), iv_rank 161 | **PREMIUM_SELLING +0.45** (strongest) | ~16.9% | back-month (30–45 DTE) short only — rising front panic blocks front-week sale |
| INTC/AMD/SMH/DELL/LRCX/SNDK/ARM | rising backwardation, no catalyst alignment | z 1.3–3.8, iv_rank ~100 | FAIR / mixed (DELL −0.39 provisional realized-overhang) | 8–15.5% | HOLD across the board — no calendar entry, no clean VRP sell |

**Earnings vol (`earnings-scout`, next 14d):** **PEP** SELL VOL full size (07-09 print, clean 2× event kink, TAIL_HEDGING back-skew, implied move 3.33%). Half-size SELL VOL: JNJ (07-15), MS (07-15), SCHW (07-21), GM (07-21), IBKR (07-21), STT (07-16), ELV (07-15) — **but their FEIR>1.10 is the systemic CPI/PPI Jul 14–15 macro cluster, not name-specific** (re-check at entry as CPI clears). SKIP: GS (no kink, FEIR 2.68 CPI-conflation), TSM/ASML (sector vol shock swamps earnings signal), NFLX (data-quality ambiguity).

*Percentile caveat: all `iv_percentile: 100` reads are provisional (n=59 < 120-day floor); z-scores are the more trustworthy number.*

## 6. Risk & Correlation
`risk-monitor` — **empty board, correctly empty.**
- **Macro headline:** disinflation stalling (core CPI 2.96% / PCE 3.41% sticky), labor softening (+57k payrolls), a "hold" backdrop into FOMC Jul 28–29. Forward: CPI Jul 14 (T+5), PPI Jul 15, retail sales Jul 16.
- **Correlation cluster:** `semis_beta_cluster` = {**MRVL** (kept, raw 2), **SMH** (−1 tier)} at **corr 0.813** — SMH literally contains NVDA/MRVL, a true same-bet overlap. NVDA/SMH 0.665 = soft-watch (no penalty). Had these been sized, the concentration is exactly what today's oil-driven chip rout hit.
- **Panic gate FIRES:** SMH (FEIR 1.529, outright front-end panic) −1; META (FEIR 1.112) −1.
- **Fundamentals verdicts:** MRVL CONFIRM, PLTR CONFIRM, NVDA CAUTION (−1, insider −65), META CAUTION (−1, insider −22.6 + $1.4T litigation + stacked earnings corridor), SMH NA. **No VETOs.**
- **Event-risk flags:** CPI at T+5 (−0.5 on any undefined-risk swing held through it); META stacks its own 07-29 earnings inside a 3-week corridor (−1). All moot on the empty board.
- **Debate cut:** MRVL bear 0.85 ≥ bull 0.55 → −1 tier (did not clear).
- **Adverse-flow exits:** none — `conviction_2026-07-06` does not exist (yesterday also empty); last populated group `conviction_2026-07-02` = [IBIT]. Watchlist empty, no carried positions.
- **Hedge sleeve:** none required — no sized book, net delta ≈ 0.
- **Breadth cross-check (advisory, finviz):** 283 advancers / 218 decliners, pct_green 56.26 — green tape, **no green-but-pct<50 divergence flag**. But note the *flow* breadth (bullish_pct 34%) diverges from *price* breadth (56% green) — a mild distribution tell the single regime label hides. Advisory, does not change sizing.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**None.** No name reached MEDIUM (raw ≥ 7) or even LOW (raw ≥ 3). The full audited breakdown of the five rubric-eligible DROP names is in the decision envelope (`decision.json`); the scores:

| Ticker | raw | dominant class | win_rate (n, source) | market_excess | fundamentals | debate (bull/bear) | final |
|---|---|---|---|---|---|---|---|
| MRVL | 2 | bullish_flow | 0.457 (140, backtest_clean) | −0.107 (beta) | CONFIRM | 0.55 / 0.85 | SKIP |
| SMH | 1 | vanna_squeeze (contested) | NA(substrate) | — | NA | — | SKIP |
| NVDA | −1 | multileg_directional | NA(substrate) | — | CAUTION | — | SKIP |
| META | −1 | bullish_flow | 0.457 (140) | −0.107 | CAUTION | — | SKIP |
| PLTR | −3 | bullish_flow | 0.457 (140) | −0.107 | CONFIRM | — | SKIP |

**Expectancy lens** *(advisory — expectancy is not yet a live sizing axis)*: no closed conviction calls to compute per-tier expectancy this cycle (empty-board streak; last populated group `conviction_2026-07-02` = [IBIT], unresolved). The live sizer remains the win-rate ladder; the C3 fractional-Kelly sizer stays advisory.

### Conviction-scoring rubric (frozen v2026-06-12) — embedded for audit
```
Daily conviction score = Σ:
  +1  MECHANIZED DEX flip / vanna-squeeze in trade direction (verified sign change, not level)
  +3  3+ aligned accumulation signals (DP+OI+smart-positioning, block-stratified institutional) — CONJUNCTION: full +3 only when cum_flow_30d confirms (aligned AND |≥$50M|), else +1
  +1  multi-day OI build (oi-trend BUILDING, --days ≥5)
  +1  conviction-matrix DIRECTIONAL_LONG >70 — LEAP context only
  +1  cum-premium-flow net directional accretion (30d) — intent-screened (no distribution_flag; not div-capture arb)
  +1  sector-rotation single-name leader — conditional (persistence ≥0.6 AND cum_flow aligned AND ≥$50M)
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg directional structure (term-structure-anchored)
  +1  vol-surface KINKED/BACKWARDATION with VRP-aligned bias
  +1  opex-pin-strategist top-5 (OPEX week only)
  -2  contrarian overcrowded-long with rising pc-ratio-zscore (informed-flow continuation penalty)
  -3  flow_conflict (cum-flow 30d clearly opposite dominant class)
  -1  flow_conflict_lite (MIXED / bottom-quartile magnitude)
  [TIER GATES, 2d, risk-monitor — not score points]: -1 tier correlation cluster; -1 tier regime conflict
Tiers: ≥9 HIGH (full) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 drop
OUT-OF-REGIME guard (P0.6): all conviction sizing capped at HALF until a post-2026-06-12 audit re-validates the tiers.
```

## 8. Watch-only — single signal, no confluence
Surfaced from one agent, failed the ≥2-agent confluence gate. For journaling, NOT trade entry today:
- **SNDK** (long) — sweep-tracker bullish put-selling 5/5 + Step-0 top-flow; vol-surface HOLD (rising backwardation, not a trade). cum-flow +$780M 30d but 90d MIXED.
- **LLY** (long) — sector-rotation Healthcare leader, PASSED the conditional +1 gate (30d +$65.6M) but single-agent.
- **WULF** (long) — multileg Sep 24/30 call debit spread, repeat 3.
- **TLT** (long bonds) — multileg near-dated 81–82 call cluster, a dovish-CPI (Jul 14) catalyst bet, single-day.
- **LMT** (short) — contrarian short-continuation watch (informed bearish flow vs flat tape).
- **IWM** (short) — dealer-positioning SHORT lean.
- **WBD** (short) — multileg bearish put roll + contrarian (disqualified as hedge) + extreme backwardation (M&A/event) — all hedge/roll/event, not a directional short.

---
*Empty-board session. Pipeline ran in full: 10 Phase-1 alpha-finders + Phase-2 quant → fundamentals gate → MRVL debate → risk-monitor. The system's refusal to size is the call.*
