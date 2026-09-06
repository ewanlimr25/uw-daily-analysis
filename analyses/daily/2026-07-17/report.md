# Daily Market Analysis — 2026-07-17

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / CHOPPY, risk-off — SPY 743.29 below 20/50 SMA (−0.94% 30d), breadth 38.4% bullish (fz 29.2% green, 147 adv / 356 dec). SPY & QQQ both **FULLY_NEGATIVE / short-gamma** (SPY total GEX −$2.27B, QQQ −$1.96B — deepest of the month). VIX 18.77 spiking +2.0. Sector lean: no durable rotation (all 5-day persistence weak); real move is a **semiconductor de-risking** (SMH −$159.6M 5d) masked by OPEX call-premium inflation.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL/CHOPPY) — sizing capped at half`.
- **Next-session GEX (SPY/QQQ):** SPY — short-gamma, ZGL null (unreliable), call wall 760 (+2.3%) / put wall 742 (at spot, no floor below); bias: favor debit verticals / long premium, fade only pokes >760. QQQ — short-gamma, ZGL null, **no call wall in-grid** / put wall 695 (at spot); bias: long straddle / directional debit, no wing-selling. Both advisory — see §2. **0DTE premium-selling = STAND ASIDE (VIX spiking, size_scalar 0.0).**
- **Top swing build:** **NONE.** 4th-ever all-DROP board — top raw_score = 2, nothing reaches even the LOW band (3–6). No name is sized.
- **Top LEAP candidate:** **NONE** — LEAP board empty (0 names clear 6-of-9 gates; every DTE>180 grower fails the cum-flow or conviction-matrix gate).
- **Biggest risk:** the entire candidate board minus GEV is **one semiconductor position** (SMH/AMD/INTC/MU/SNDK/NVDA pairwise corr 0.78–0.94) riding an IV-rank-100 earnings-vol wall through a two-week binary gauntlet (GEV 07-22, INTC 07-23, CDNS 07-27, FOMC 07-28/29, STX 07-28, PCE ~07-31, AMD 08-04, SNDK 08-05). Book is empty, so no hedge is triggered; advisory sleeve for external tech-beta is a defined-risk SPY 745/725 put vertical bracketing FOMC.

## 1. Regime & Gamma State
`uw risk market-regime`: **TRANSITIONAL — "Half position sizes. Favor defined-risk strategies. Iron condors in range." Trend CHOPPY.** SPY 743.29, below 20-SMA (745.02) and 50-SMA (744.38), −0.94% 30d, −2.25% from the 90-day high. Breadth is risk-off: 2,420 bullish vs 3,878 bearish flow tickers (38.4% bullish). The fz independent advance-decline series corroborates hard — 147 advancers / 356 decliners, 29.2% green, median −0.87%, worst mover ISRG −14.15% (earnings). No green-tape divergence today; the tape is simply red.

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 742.95 | null (unreliable) | −$2.27B | FULLY_NEGATIVE | 760 (+2.3%) | 742 (at spot) |
| QQQ | 695.66 | null (unreliable) | −$1.96B | FULLY_NEGATIVE | none in-grid | 695 (at spot) |
| IWM | 294.05 | null (unreliable) | negative | chronic short-γ | — | 290 (−1.4%) |

**DTE volume share (MARKET):** 0DTE 0% (OPEX-parquet artifact), weeklies 20.5%, monthlies 17.3%, LEAPs 4.1% — regime hint BALANCED, no retail/institutional tilt to apply. **VRP:** SPY FAIR (IV30 15.4% vs RV30 15.7%, −0.003); QQQ FAIR (IV30 26.5% vs RV30 30.7%, −0.042) — no premium edge either way.

**Macro backdrop:** yield curve normal (10y-2y +0.37); core CPI 2.81% / core PCE 3.41% (sticky above target); unemployment 4.2%, payrolls +57k; **10Y 4.57% rising** (+0.14 30d), USD strengthening; fed funds 3.63% — a genuine headwind for longs. **Forward event risk (next ~10 td):** GEV earnings 07-22, INTC 07-23 AMC, CDNS 07-27, **FOMC 07-28/29 (HIGH, no SEP)**, STX 07-28, core PCE ~07-31, AMD 08-04, SNDK 08-05; weekly jobless claims 07-23 & 07-30. CPI (07-14) and PPI (07-15) already printed.

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> Advisory, prose-only, **0 rubric points**, no backtested predictive claim. EOD 0–45d book read forward as the prior for Monday 07-20's open. Scope SPY & QQQ only.

**SPY** — regime **short-gamma / FULLY_NEGATIVE**, third straight negative session and the deepest (total GEX −$1.15B on 07-16 → −$2.27B on 07-17). ZGL is null (disqualified; the 07-16 print of 360.62 is the known extrapolation artifact) → `zgl_reliable=false`, fall back to total_gex sign + walls. Dealers are short gamma across nearly the whole strip; the single heaviest concentration (−$498.7M) sits **at the money (742)**, so there is no real cushion below — a break of 740 has nothing under it until 735/730. Call wall 760 (+2.3%) is the lone long-gamma pocket and cross-validates the OPEX pin board. **Structure bias:** short-gamma trend/breakout — favor debit verticals / long premium with defined risk over any wing-selling; the only mean-revert expression is fading pokes above 760.

**QQQ** — regime **short-gamma / FULLY_NEGATIVE**, same entrenchment (−$1.15B → −$1.96B). ZGL null. Heaviest cell (−$977.3M) sits **at the money (695)**; no positive-GEX pocket anywhere in the visible grid (672–719) → **no call wall identified** (a data-coverage gap, not "no resistance"). This is the more amplification-prone book of the two. **Structure bias:** short-gamma with no visible upside cap — long straddle / directional debit verticals; a condor/iron-fly pin trade is not supported (no positive wall to anchor short strikes).

**Mandatory caveats:** EOD is a prior, not a target (fresh 0DTE OI floods in at Monday's open and re-computes the map, especially post-OPEX as Friday's strikes roll off); no scheduled macro catalyst Fri→Mon but spiking VIX raises weekend gap odds; these are ETF books, not the cleaner SPX/NDX; uw-pp cannot isolate the D+1 expiry (0–45d proxy). QQQ's missing call wall is inconclusive, not "no resistance."

### 2a. Next-session 0DTE premium-selling setup — **STAND ASIDE**
`zerodte_setup` (advisory, delta-neutral, 0 rubric points): **both SPY and QQQ = STAND ASIDE.** `sell_premium=false`, `size_scalar=0.0`. Stand-aside reason: **VIX spiking +2.0 (18.77) → short-vol left-tail regime.** Vol state HIGH, short-gamma (wider next-day range). Expected range SPY 1.21% / QQQ 1.93%. The rolling backtest verdict is GO_PREMIUM_SELL_INTRADAY (SPY gross +0.279%/net +0.179% of spot notional, 93.3% open-win, n=60; QQQ gross +0.389%/net +0.289%, 88.3%, n=60 — `pnl_basis` = % of underlying spot notional, GROSS; net leads), but the **live gate says do not sell premium into a spiking VIX** — the exact regime where a negatively-skewed short-vol book blows up (sample has no vol shock; left tail unsampled). SPY≈SPX; QQQ weaker (NDX book unavailable). No directional tilt — delta-neutral only. **This lane is permanently advisory / 0 points until a vol-shock day enters the sample AND net expectancy clears a tail-aware bar.**

## 2a. Swing Dealer Positioning (1–4 weeks)
No mechanized DEX flip qualifies anywhere today — every candidate is a persistent level or a stale/low-magnitude whipsaw, none a verified sign-change on the latest session. **No valid vanna squeeze** market-wide: all three indices carry a put-heavy book, but dated Yahoo ^VIX is rising 3 straight sessions (15.67 → 16.73 → 18.77) → vanna *pressure, building*, not a squeeze. SPY/QQQ have deepened into their most-negative GEX/DEX prints of the trailing month into OPEX (SPY DEX −34.4B, QQQ −48.0B) — a short-gamma, vol-amplifying backdrop. Single-name reads (all unscored — no flip): **SMH** shows the cleanest 4-session bearish DEX grind (−4B → −12B, 4-for-4); **NVDA** positive DEX decaying fast (+15B → +3.9B in 3 sessions, fading long); **SNDK** dealer flow NEGATIVE throughout and spot −21% over 4 sessions — **directly contradicts its single-day bullish funnel tag**; **MU** turned bearish 3 sessions ago and held into its earnings-vol cluster.

## 2b. Sector Rotation
**Rotation regime: `no_change`, low confidence.** Broad de-risking, not a rotation — 7 of 11 SPDRs net-negative on a genuine 5-day basis. All 8 GICS sectors sit at persistence_score = 1.0 simultaneously (a saturated, non-discriminating axis); the single-day Tech +$1.17B is OPEX call-premium inflation, and the ETF instrument tape refutes it (XLK 5d MIXED, **SMH 5d BEARISH −$159.6M**). None of the four canonical rotation patterns fit. **Sector-leader +1 rubric gate = 0 for every sector.**

**ETF flow tape (advisory — 0 rubric points):**

| ETF | Net premium (5d) | Persistence | DP positioning | Options urgency | GICS agreement |
|---|---|---|---|---|---|
| EWY | inflow +$32.2M | BULLISH | spread, largest $50M @18:15Z | mixed (hedge put + call buys) | n/a (geo) |
| XLI | inflow +$4.27M (small) | BULLISH | dominant $165.4M @20:28Z (**closing-cross — discount**) | thin, no urgency | n/a |
| EWT | inflow +$1.5M | BULLISH | spread | modest | n/a (geo) |
| **SMH** | **outflow −$159.6M** (largest) | BEARISH | clean $162.9M @13:44Z midday | **strong: $66M + $64M ask-side 07-31 put sweeps** | disagree vs GICS single-day |
| GDX | outflow −$24.6M | BEARISH | mostly clean | mixed (put buy vs put sell) | n/a |
| KRE | outflow −$10.1M | BEARISH | clean | modest ask-side put buys | agree ("OUT Financials") |

Top-3 inflow (EWY/XLI/EWT) are geographic/thematic with no GICS confirmation and small magnitude; the real, cross-confirmed signal is **SMH outflow** with genuine put-sweep urgency — a semi de-risking tell, not a rotation trade. Semi single names remain bifurcated (bullish flow NVDA/CDNS/SNDK/STX vs bearish SMH/SOXX/MU) — dispersion, not a uniform sector short.

## 3. Swing Setups (1–6 weeks)
**EMPTY — no name is sized today.** Five names cleared the ≥2-agent confluence gate (STX, INTC, SNDK, SMH, NVDA) but the frozen long-biased rubric scored them all at raw ≤2 (DROP floor). The day's genuinely edged signal is **bearish** — `bearish_flow` clean class WR 0.553 (n=132, **+15.2pp** over same-window SPY-short) — but it scores 0 (C19 unpromoted) and the desk's standing no-short-alpha-sizing ruling applies regardless. No long-swing setup regime-aligned; no defined-risk short clears the bar. See §7 for the full scored board and §8 for single-signal watch-only names.

`sweep-tracker` persistence ledger (informational, 0 points): cleanest reads are **bearish** — INTC (5/5, cum_flow −$786M co-flag, opening-confirmed 92.5P), AMD (5/5, fresh 07-24 280P crash-hedge), NBIS (5/5, 140P). SNDK/SMH/TSM flagged `flow_conflict` (persistence vs today's OI build disagree). MU largest premium ($4.89B) but mixed → disqualified. Index/mega-cap tape is hedge/box-spread artifact.

## 4. LEAP Builds (6–24 months)
**EMPTY.** Zero names clear 6-of-9 gates. Every non-ETF DTE>180 OI grower fails the required cum-flow gate (Gate 4) or conviction-matrix (Gate 8): DRAM (90d −$69.9M + simultaneous 10.9k-contract far-dated put roll), AAPL (30d flips negative, closing-cross-contaminated DP), RKT/NOK/CMCSA/BE (all net-bearish 90d/30d flow), IREN (conviction-matrix DISTRIBUTION). Closest near-miss FHN (genuine 30d-weighted bullish accretion) reads as a covered-call/overwrite program (100% bid-side, paired far-far same-day sizing), not institutional conviction — re-check next session if the bid/ask skew flips.

## 5. Volatility Surface
The day's surface story is a genuine, near-uniform **IV-rank-100 semiconductor earnings-vol wall** (memory + logic chips reporting 07-22 → 08-05): INTC (07-23, dte6 kink 137.3%, COMPLACENT back-month), GEV (07-22, 92.4%), STX (07-28, dte13 124.7%), CDNS (07-27), SNDK (08-05, 169.9%, best-behaved cone), WDC/BE/PLTR/TSEM. These are expected pre-earnings backwardations that mean-revert post-print (NFLX, already reported, IV39 / flat-contango, is the resolved template). **No clean, liquidity-confirmed calendar-spread candidate cleared** — ADI (08-19) and MU (robust Goyal-Saretto percentile only 77.6/NORMAL despite raw IV 92) are the only non-earnings candidates and both fail a liquidity/tenor floor pending a front-end-iv-ratio recheck. **FORM and SANM** are unreadable (front-end chain sub-15-contract floor — do not trade off their raw BACKWARDATION label). The one structural (non-earnings) signal is **SMH TAIL_HEDGING** (skew ratio 1.16, put premium 8:1 at 07-31) — a correctly-priced hedge, not a mispricing.

Earnings-scout verdicts (all SELL VOL capped at **half** — no name shows tail-hedging back-months): INTC, GEV, STX, SNDK SELL VOL; CDNS/AMD/TSEM/WDC/SANM/FORM SKIP. IV crush into the print is the thesis; none is a directional trade.

## 6. Risk & Correlation
**Macro headline:** sticky inflation (core PCE 3.41%), 10Y rising to 4.57%, USD firm — a headwind for longs; **FOMC 07-28/29** is the dominant forward catalyst, sitting inside every named earnings this book touched. Breadth cross-check: 147 adv / 356 dec, 29.2% green — no divergence (red tape, red breadth, consistent).

**Correlation cluster (the whole risk story):** `uw risk portfolio-correlation` on the candidate union returns one dominant **semiconductor cluster** — SMH/AMD 0.941, INTC/SMH 0.914, SMH/MU 0.894, INTC/AMD 0.892, SNDK/MU 0.874, SNDK/SMH 0.855, MU/AMD 0.814, SMH/NVDA 0.779. Members {SMH, AMD, INTC, MU, SNDK, NVDA} are **one position, not six**; had anything sized, only INTC (highest raw) would have been allowed and the rest auto-demoted −1 tier. GEV is the only non-cluster name on the board.

**Fundamentals verdicts (top-5):** NVDA **VETO → watch-only** (2-of-3 legs fight the short: 4/4 beats, rev +70.7% YoY, 63% net margin; multileg reads as a collar, so direction itself is unresolved — the recurring mega-cap "fundamentals kill the bearish flow" pattern). STX/INTC/SNDK **CAUTION**: STX insider MSPR −51.9 (negative 16/19 months) + distribution_flag = accumulation-as-distribution risk; INTC unprofitable (net margin −5.9%) but a beat-streak + SeekingAlpha upgrade fight the short; SNDK insider MSPR −100 (max intensity) under a −21% 4-day drop and conflicted flow. GEV **CONFIRM** (rev +10.3%, EPS +395%, Bernstein $1,206 PT). *fz note: total upstream miss today — short-interest/float/analyst all null, screen-fallback empty; a broader fz degradation to log for the next audit.*

**Debate:** bear residual ≥ bull on all five names (STX 0.65/0.55, INTC 0.65/0.55, GEV 0.65/0.55, NVDA 0.55/0.55, **SNDK 0.75/0.55** — SNDK the widest, on max-intensity insider selling). The GEV and SNDK bulls actually conceded below the 0.55 residual floor (~0.35) — recorded at the 0.55 schema minimum in the envelope. The disconfirmation step uniformly confirms the empty board.

**Adverse-flow exits:** none — the `conviction_2026-07-16` group does not exist (yesterday's board was also all-DROP), so there are no carried positions to monitor.

**Hedge sleeve:** conviction book is empty → net delta 0 → **no book-derived hedge is triggered.** For external discretionary tech-beta, the advisory sleeve given SPY/QQQ short-gamma + VIX 18.77 spiking + FOMC at T+7/T+8 + VRP FAIR: a **defined-risk SPY ~745/725 put vertical, Aug-01 or Aug-07 expiry** (bracketing FOMC + PCE), sized to the external book's net delta — cleaner than a VIX call ladder because FAIR VRP means convexity isn't cheap. Not a system call.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**NONE.** No name reached MEDIUM (raw ≥7) or HIGH (raw ≥9). The Step 3a load-bearing-tool gate did not evaluate (no HIGH-band candidate). Full scored board recorded below for the calibration loop (all DROP; every `final_size = skip` except NVDA watch-only).

**Expectancy lens (advisory — C31, display-only, not a sizing input):** the most recent `/calibration-audit` (2026-07-11) found the **DROP pile outperformed the traded book (0.477 vs 0.406)** — i.e. empty-board discipline is validated, refusing to size a thin choppy tape has been the correctly-graded behavior. `[advisory — expectancy is not yet a live sizing axis]`

| Ticker | raw | class | win_rate (n, src) | mkt_excess | pre-risk | fundamentals | debate (b/br) | gates fired | final |
|---|---|---|---|---|---|---|---|---|---|
| STX | 2 | earnings_vol | null NA(substrate) | null | skip | CAUTION −1 | 0.55/0.65 | fund, event, debate, rubric-half | **skip** |
| INTC | 2 | bearish_flow | 0.553 (132, clean) | +0.152 | skip | CAUTION −1 | 0.55/0.65 | fund, event, debate, rubric-half | **skip** |
| GEV | 1 | earnings_vol | null NA(substrate) | null | skip (gate-FAIL) | CONFIRM 0 | 0.55/0.65 | debate, rubric-half | **skip** |
| NVDA | 1 | multileg_directional | null NA(substrate) | null | skip | **VETO** | 0.55/0.55 | fundamentals VETO | **watch-only** |
| SNDK | 1 | earnings_vol | null NA(substrate) | null | skip | CAUTION −1 | 0.55/0.75 | cluster, fund, event, debate, rubric-half | **skip** |
| SMH | −1 | bearish_flow | 0.553 (132, clean) | +0.152 | skip | (not in top-5) | — | cluster, no-short-alpha | **skip** |
| CDNS | 0 | dark_pool_accumulation | null NA | null | skip (gate-FAIL) | (not in top-5) | — | flow opposes accumulation | **skip** |
| NBIS | −3 | bearish_flow | 0.553 (132, clean) | +0.152 | skip | (not in top-5) | — | flow_conflict −3 | **skip** |

Invalidation anchors (for the record, were any revived): INTC — reclaim/hold above the beat-streak squeeze level into 07-23 kills the short-vol/short thesis; STX — loses 740–746 DP shelf (long) or 07-28 print resolves the distribution question; SNDK — bulls need a hold above the −21% capitulation low with insider selling abating; NVDA — resolve the collar-vs-short ambiguity (net calls in Sep18 = it was a hedge). None actionable today.

*Conviction rubric (Step 4, frozen v2026-06-12) is embedded in `.claude/commands/daily-analysis.md`; every score_component above cites its source agent + tool in the decision.json audit trail.*

## 8. Watch-only — single signal, no confluence
Surfaced by one agent, failed the ≥2-agent confluence gate — journaling only, **not** trade entry:
- **CDNS** — accumulation-hunter LONG (cleanest accumulation of the day: mega buy-ratio 0.76, ACCUM 1.68, zero retail, clean intraday tape, OI BUILDING +5,804, buying into −19.8% weakness, DP levels 327–331). Zeroed by the rubric on non-confirming −$72M 30d flow (BEARISH vs the long) + flow_conflict_lite. Earnings 07-27. The board's most "real" long that the flow won't confirm.
- **ASTS** — accumulation-hunter LONG (strongest ACCUM 2.51, mega buy 1.0, OI BUILDING +160,804, dip-buy into −46%, levels 57.75–61). Single-agent; cum_flow +$41M sub-$50M.
- **AMD** — sweep-tracker bearish 5/5 (fresh 07-24 280P crash-hedge, opening 98%); accumulation label rejected (closing-cross MOC); earnings 08-04. Single clean agent; semi-cluster member.
- **GEV** — earnings-scout SELL VOL half (implied move 9.5%); the only fundamentals CONFIRM on the board but single-agent gate-FAIL. Earnings 07-22.
- **NBIS** — sweep-tracker bearish 5/5 (140P opening) fighting +$143.8M of net-bullish 30d flow (flow_conflict −3).
- **MU** — mixed/conflicted (sweep disqualified $4.89B, dealer bearish, DP-buy-vs-bearish-flow divergence, robust IV percentile 77.6 NORMAL despite raw 92). No clean directional read.
- **BE** — accumulation **distribution_flag** (330C OI −18,184 on 20,465 vol, $26.4M closing premium + bearish call-writing). Funnel-bullish +$20M is not conviction — avoid.

---
*Data date 2026-07-17 (July monthly OPEX). 11 Phase-1 agents + quant/fundamentals/debate/risk. All `uw` reads pinned `--date 2026-07-17`. No watchlist write-back (all DROP). Machine-readable envelope: `decision.json`.*
