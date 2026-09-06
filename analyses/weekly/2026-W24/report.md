# Weekly Market Intelligence — Week of 2026-06-08 (ISO 2026-W24)

## Executive Summary
- **Week regime + WoW Δ:** Regime **held TRANSITIONAL / PULLBACK_IN_UPTREND** at both ends of the week — no flip. Breadth improved modestly (bullish-flow share 34.0% Monday → 38.6% Friday, still sub-50%). SPY closed 741.75, below its 20-DMA (745.07) but above its 50-DMA (722.80), −2.45% from the 90-day high. VRP is **FAIR / NEUTRAL** (SPY +0.0125, QQQ +0.0084) — IV ≈ realized, no premium-selling edge. This is a chop tape with a Fed decision at its center, not a trend.
- **Rubric regime status:** **OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL/PULLBACK) — sizing capped at half** (P0.6 guard active until ≥30 resolved post-2026-06-12 calls re-validate the tiers).
- **Signal performance:** **6 of 17 resolved (hit rate 6/17 = 35%); 13 INCONCLUSIVE excluded; 30 total calls in universe (30 envelope-anchored, 0 reconstructed).** The daily fleet was chopped being short semis into a violent semis rip and short indices into a grind-up. The one HIGH-tier daily call of the week (SMH short, half-size) **LOST** (+8.6% against) — tiers inverted again, consistent with the 2026-06-12 calibration finding.
- **Top swing build for next week:** **None.** Zero names cleared the conviction rubric into HIGH or MEDIUM tier. The single name above the 3-point floor (HYG, raw 3, LOW) was resolved to **no capital** by the gate stack (see §8).
- **Top LEAP build:** **None.** leap-positioning-radar returned zero candidates — every contender failed the cumulative-premium-flow accretion gate. Institutions are not expressing multi-quarter directional conviction in a transitional regime.
- **Biggest emerging risk:** A compressed, event-dense next week — **FOMC decision + SEP Wed 06-17** (Warsh's first meeting as Chair, ~98% no-move priced — the dot-plot/tone is the risk), **monthly OPEX pulled to Thu 06-18** (Juneteenth closes Fri 06-19), and an earnings cluster (JBL 06-17, ACN/KR 06-18) all inside a 4-session week. The standing institutional **HYG credit put-spread program** (rolling to Jan-27) is the market's clearest hedge tell.

## 0. Week in Review — Intra-Week Signal Performance

Universe = the union of `calls[]` across this week's five daily `decision.json` envelopes (06-08 → 06-12), keyed by `(ticker, direction)` at the time committed — hindsight-free and survivorship-free. Resolution via fresh `uw historical trend` from each call's report date to 2026-06-12. INCONCLUSIVE = |move| < 0.5×ATR(14). **ATR is a close-to-close proxy** (Yahoo is 2025-anchored in this environment; no intraday 2026 OHLC available — flagged). All 30 rows are envelope-anchored; 0 reconstructed.

| Ticker | Direction | Source | Move % | 0.5×ATR% | Flow lean | Grade | Note |
|---|---|---|---|---|---|---|---|
| MU | LONG | env 06-08 | +3.4 | 2.75 | bullish | **WIN** | early-week semis long, pre-flip |
| MRVL | LONG | env 06-08 | −3.2 | 3.04 | bearish | **LOSS** | semis long that faded |
| LRCX | LONG | env 06-08 | +13.1 | 1.64 | bearish | **WIN** | big semis rip |
| META | SHORT | env 06-08 | −3.1 | 0.92 | bearish | **WIN** | only clean short that worked |
| AMD | LONG | env 06-08 | +4.3 | 1.95 | bullish | **WIN** | semis long |
| NVDA | LONG | env 06-08 | −1.7 | 1.09 | bullish | **LOSS** | drop-tier |
| GOOGL | LONG | env 06-08 | −1.0 | 0.76 | bearish | **LOSS** | drop-tier |
| SPY | SHORT | env 06-09 | +0.6 | 0.28 | bullish | **LOSS** | short into a hold |
| IWM | SHORT | env 06-09 | +2.8 | 0.58 | bullish | **LOSS** | short into small-cap bid |
| MSFT | SHORT | env 06-09 | −3.1 | 1.04 | bearish | **WIN** | short that worked |
| CZR | LONG | env 06-09 | +0.1 | 0.29 | mixed | INCONCLUSIVE | flat |
| MU | SHORT | env 06-09 | +4.9 | 2.77 | mixed | **LOSS** | drop-tier, fought the rip |
| SNDK | LONG | env 06-09 | +20.3 | 2.23 | bullish | **WIN** | biggest winner, drop-tier |
| **SMH** | **SHORT** | **env 06-10** | **+8.6** | **1.33** | bearish | **LOSS** | **the one HIGH-tier (raw-9, half) call — ripped against** |
| TSLA | SHORT | env 06-10 | +6.5 | 1.28 | bearish | **LOSS** | short into rally |
| LRCX | VOL_SHORT | env 06-10 | +14.0 | 1.48 | bearish | **LOSS** | sold vol into a 14% move |
| MSFT | NEUTRAL | env 06-10 | −1.7 | 1.08 | bearish | INCONCLUSIVE | non-directional |
| AAPL | LONG | env 06-11 | −1.5 | 0.67 | mixed | **LOSS** | late-week long, pulled back |
| ASML | LONG | env 06-11 | −1.9 | 1.31 | bullish | **LOSS** | late-week long |
| SMCI | LONG | env 06-11 | −4.7 | 5.03 | bearish | INCONCLUSIVE | move < 0.5×ATR (high vol) |
| ACN/IWM/GOOGL/NVDA/KR/MU/USAR/EFA/XOM/AMZN | various | env 06-12 | — | — | — | INCONCLUSIVE (×10) | committed week-end, no forward window |

**Read:** the fleet's edge this week lived entirely in the **early-week semis longs** (MU, LRCX, AMD, SNDK — all WINs) before it pivoted bearish mid-week. That bearish pivot (SMH/TSLA/LRCX-vol shorts on 06-10, SPY/IWM shorts on 06-09) was badly timed — semis ripped (SMH +8.6%, LRCX +13.1%, SNDK +20.3%) and indices held. Critically, the *sizing discipline* mostly worked: nearly every losing call was sized `skip`/`watch_only`/`starter`, so almost no capital was deployed. The exception that bit was **SMH short at HIGH/half-size** — the only call that slipped to real size, and it lost. That is the tier-inversion story in one trade: a collar/hedge footprint on semis was read as bearish conviction, and the underlying kept ripping.

## 1. Regime & WoW Delta
- **`uw risk market-regime`:** TRANSITIONAL / PULLBACK_IN_UPTREND both Monday (06-08) and Friday (06-12) — regime **held**, no flip. Money-flow breadth improved 34.0% → 38.6% bullish but never crossed 50%. SPY pinned between its 20- and 50-DMA.
- **`uw historical vrp`:** FAIR / NEUTRAL — SPY VRP +0.0125 (IV30 14.9% vs RV 13.6%), QQQ +0.0084 (IV30 24.8% vs RV 23.9%). Marginally positive but classified neutral; no clean premium-selling tailwind, and the −2 crowded-long penalty did not fire this week.
- **`uw options-flow dte-volume-share` (SPY market proxy; MARKET aggregate returns zero-volume in this dataset):** BALANCED — weeklies 17.8%, monthlies 5.2%, 0DTE ~0, LEAP 0.4%. No retail-0DTE distortion; institutional/swing flow gets the benefit of the doubt.
- **Macro backdrop (`macro_snapshot`):** Yield curve **normal** (10Y−2Y +0.39). Core inflation **sticky** — core CPI 2.96% YoY, core PCE 3.29% YoY, both above target. Labor softening — unemployment 4.3%, payrolls +172k. 10Y **flat at 4.45%**, USD **strengthening**, fed funds 3.62%. A sticky-core, soft-labor, strong-dollar mix that keeps the Fed boxed.
- **Forward `event_risk` (next two weeks, Tier-1):** Retail Sales Tue 06-16; **FOMC decision + SEP Wed 06-17** (Warsh's first meeting; ~98% no-move priced — dots/tone are the risk); monthly **OPEX Thu 06-18** (pulled forward from the third Friday because **Juneteenth closes the market Fri 06-19**); **PCE + Michigan final Fri 06-26**.
- **Implication for next week:** A 4-session, event-dense week with a Fed decision and OPEX stacked on Wed–Thu. Bias is *defensive and small* — the regime does not support directional size, and the rubric is out-of-regime. Premium-selling is the only structurally validated edge (0DTE stack, §9), and even that stands aside on a VIX spike.

## 2. Sector Rotation
- **Rotation regime call: `no_change` (low confidence).** This is a **broad risk-on tape** — all 11 GICS sectors registered net options inflow over the full 5-day window (persistence ≈ 1.0 across the board). There is no rotation-*out* leg to anchor a classic rotation; the signal lives only in relative magnitude.
- **Confirmed rotation-in (GICS + ETF agree → higher conviction):**
  - **Communication Services** — persistence 1.0, 5-day avg net +$580M, **XLC agrees**. Leader: **META** (+$269M net, PCR 0.47, #1 bullish flow), with GOOGL and ROKU (new-high RS) secondary.
  - **Financial Services** — persistence 1.0, 5-day avg net +$323M, **XLF agrees**. Leaders: BAC (PCR 0.38), TROW (PCR 0.02), GS, AXP.
- **GICS-only, ETF disagrees → watch-only (the week's most important divergence):**
  - **Technology** posts the largest GICS inflow by 10× ($3.7B/day) — but **XLK is flat and SMH is the single most bearish ETF in the universe (−$121M)**, carrying an institutional **collar** (Sep $620C / Dec $600P / Aug $475P put sweeps). Mega-cap AI/software single-name calls are driving the GICS aggregate while the semis sub-sector is being *hedged*. Treat Tech as watch-only, not rotation-in. (This is exactly the footprint that trapped the daily SMH short — see §0.)
  - **Healthcare** GICS spiked 06-12 ($4.0B call vs $0.18B put — event-concentrated), but **XLV and XBI are both net-outflow** → watch-only.

**ETF flow tape (advisory — 0 rubric points):**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| EWY (Korea) | inflow | strong | $229M EOD blocks (rebalance/creation) | Jul/Jun put hedges | n/a | — (geographic) |
| XLP | inflow | moderate | small mid-price fills | none | partial | — |
| GDX | inflow | moderate | $52M/$36M near-bid blocks | near-term call + 2027/28 put tail | partial (Materials) | — |
| **XLF** | inflow | strong | — | — | **agree** | BAC, TROW, GS, AXP |
| **XLC** | inflow | strong | — | — | **agree** | META, GOOGL, ROKU |
| XBI | outflow | moderate | above-mid | Dec'26/Jan'27 LEAP calls | disagree | — |
| KRE | outflow | moderate | 2M-share creation/redemption arb (noise) | thin | partial disagree | — |
| **SMH** | **outflow (−$121M, largest)** | strong | $47M below-bid blocks (unwind/collar) | synthetic collar + tail hedges | **DISAGREE** | — |

Lead read: **CommSvc and Financials are the only durable, ETF-confirmed rotation-in sectors.** The Tech GICS/ETF split is the signal of the week — long mega-cap AI, hedged semis.

## 3. Swing Book (1–6 weeks) — ranked by weekly conviction score

**Empty. No name cleared the confluence gate into a scored directional swing.** The candidate union was directionally conflicted or single-agent across the board:

- **IWM** — 4 agents, **internally conflicted**: dealer-positioning flagged a *mechanized DEX-flip LONG* (net_dex −12.84B 06-10 → +7.61B 06-11, 4-session negative run, flip-day 0.76× trailing median — the one validated dex_flip this week) while multileg flagged a *3-day-repeat Jun18 276/279 put-vertical BEARISH* and accumulation read *DISTRIBUTION* (dp_buy_ratio 0.345). The scored signals point opposite directions → watch-only.
- **MRVL / INTC** — clean bullish *sweep* persistence (5/5 and 4/5, OI-opening confirmed 80–91%) but single-scored-agent; accumulation read both MIXED/covered-call → watch-only.
- **META** — sector LONG leader but lone scored agent; dealer disqualified it (DEX −5.5B + put-heavy vanna conflict).
- **GS** — contrarian OPENING_PUT_PRIME short vs sector-leader long → conflicted.

> **3a Long swings:** none. **3b Short/fade swings:** none cleared (contrarian found zero qualifying fades — index BACKWARDATION aborts SPY/QQQ fades; VRP-neutral closes the premium-fade gate; IWM at −2σ P/C reads as informed-continuation, not a fade).

**Swing dealer context (advisory, dealer-positioning-strategist):** SPY DEX sign-change present but sub-magnitude (0.17× → watch 06-13); QQQ no mechanized flip; GLD put-heavy vanna book (SHORT/flat advisory). VIX leg of all vanna flags is **CANNOT_VERIFY** (Yahoo API returned 2025-era data — flagged).

## 4. LEAP Book (6–24 months)

**Empty.** leap-positioning-radar cleared zero of the 6-of-9 gates. Every candidate (META, MU, KLAC, SNDK/XYZ, AVGO, PYPL, TSM, GLD, PFE, IWM) failed **Gate 4 — cumulative premium flow must accrete in both the 30-day and 90-day windows.** The notable single event was a ~30k-contract Dec-2026 LEAP block in SNDK on 06-12, but it is a one-session print, not multi-week slow accretion. Institutions are pausing multi-quarter directional expression while the regime is undefined — re-scan post-FOMC.

## 5. Volatility Surface — WoW Term Structure & Skew Evolution
- The entire high-IV cohort (**MU, ACN, JBL, SNX**) is **earnings-driven** front-end loading into the 06-18 expiry, not structural dislocation. After dropping the expired -1 DTE bucket, the 06-08 structures were near-flat/contango; by 06-12 the front loaded into KINKED/elevated front-ratio shapes as earnings approached (ACN front-ratio 1.891, JBL 1.350, KR 1.674, MU 1.149).
- **DRI is the one clean non-event vol dislocation:** stable backwardation, **VRP +11.0pp (highest clean positive in the scan)**, no confirmed catalyst, adequate Jul-17 liquidity → a SELL-VOL / iron-condor candidate at half size. Note: earnings-scout flags DRI back-month as TAIL_HEDGING, so size with care.
- **FDX** post-earnings-resolved → CONTANGO (front-ratio 0.790); premium-selling window open if liquidity holds.
- `uw historical iv-percentile-zscore` returned only a 44-day window (not 252) → all percentiles are **PROVISIONAL** estimates this week.
- Calendar-spread concentration sits at the 06-18 expiry ($18.0B premium, 4.3:1 call-skewed — earnings positioning, not protective hedging).

## 6. Earnings — Recap & 2-Week Lookahead

**(a) Recap.** **ADBE** reported ~06-12 — beat +0.36% ($5.96 vs $5.94), IV crushed as expected, and **mega-tier dark pool bought 100% post-print ($60.8M)** with a COMPLACENT back-month skew → a **PEAD drift candidate (advisory, 0 points)** *if* the 06-13 open held above the pre-print level. No other tracked name printed this week.

**(b) Lookahead (next 2 weeks, fundamentals-confirmed dates):**

| Rank | Ticker | Report | IV Rank | Structure verdict | Fundamentals | Event overlap |
|---|---|---|---|---|---|---|
| 1 | **FDX** | 06-23 PM | 82.9 | **CALENDAR** (cleanest; front not in panic) | — | PCE 06-26 |
| 2 | **ACN** | **06-18 BMO** | 98.9 | CALENDAR (front-ratio 1.891 too hot for naked short) | **CONFIRM** (insider buying MSPR +44.7) | FOMC−1, OPEX day |
| 3 | **KR** | **06-18 BMO** | 77.5 | SELL VOL (half) — COMPLACENT back | **CAUTION** (EPS −57.8% YoY, PT cuts) | FOMC−1, OPEX day |
| 4 | **JBL** | **06-17 BMO** | 96.2 | SELL VOL (half) | **CAUTION** (FOMC same-day; insider selling −9.3%) | **FOMC same day** |
| 5 | **MU** | 06-24 PM | 99.6 | **SKIP** — whole near-term curve elevated, no clean kink | **CAUTION** (4/4 beat streak, 11.6% above PT) | PCE+2 |

The Week-1 earnings (JBL/ACN/KR) all sit inside the FOMC + OPEX bracket → **half size, prefer calendars over naked short vol, close before the FOMC statement.** FDX is the cleaner trade in the post-FOMC window.

## 7. Risk & Correlation (week-candidate universe)
- **Correlation clusters (`uw risk portfolio-correlation`, 30-day):** HYG/IWM **0.853** (the HYG bearish-credit thesis is effectively a short-IWM bet — and W23 alerts show a fresh $495M *bullish* IWM dark-pool print, a direct headwind); MU/SNDK **0.777** and INTC/SNDK 0.695 (semis cluster, all watch-only); IWM/GS **0.807**, JBL/IWM 0.741. No cluster fires a mechanical penalty because no name carries live capital.
- **Macro & event risk:** FOMC Wed 06-17 + OPEX Thu 06-18 are both T+2/T+3 inside any swing horizon → the event-risk gate fires on every directional structure held through them. Sticky core inflation + strong USD keep the macro backdrop restrictive.
- **Fundamentals verdicts (top-5):** HYG **CAUTION** (FOMC dovish-squeeze risk on the Jun18 leg), MU **CAUTION** (beat streak fights the bearish tilt), ACN **CONFIRM** (insider buying), KR **CAUTION** (EPS −57.8%), JBL **CAUTION** (FOMC-same-day compound event, insider selling −9.3%). **No VETOs.**
- **Debate-disconfirmation cut:** **HYG** — bear residual **0.85** ≥ bull residual **0.55**. The bear case is decisive: HYG's rolling put-spread (Jan-27 anchor + accumulation-hunter HEDGED_LONG 52.6% + sub-$50M premium + win-rate 0.468 below the 0.50 floor) is a **standing credit-hedge program, not tradable directional alpha**.
- **Breadth cross-check (advisory):** `fz` pct_green 78.9% (397 advancers / 106 decliners) — green tape, **no divergence** flagged.
- **Adverse-flow exits (W23 watchlist):** IWM shows a $495M bullish dark-pool print + OI build (+185k) — a headwind to any carried bearish-credit/short-small-cap exposure. SPY shows a $500M bullish DP print. **Recommendation: if carrying a legacy HYG put-spread, trim before FOMC** (dovish surprise squeezes the front leg).
- **Hedge sleeve:** none required — zero new capital deployed. The options market is not pricing panic (SPY front-end IV ratio 0.905, contango); a VIX hedge here would be selling into the market's own calm read.

## 8. High-Conviction Cross-Ref (HIGH and MEDIUM tier)

**Empty — no HIGH or MEDIUM tier names this week.** For completeness, the single name above the rubric floor and its full gate resolution:

**HYG — raw_score 3 (LOW) → FINAL SIZE: SKIP / no capital.**
- Signal class: `multileg_directional` (BEARISH credit put-spread). Score: +2 multileg_repeat (4-day rolling put-spread Jun18→Sep18→Jan27, max-negative-GEX zone) + 1 OI-building bearish (net +124.6k opening-dominant new put OI). cum_flow 30d −$17.1M / 90d −$31.0M (aligned but sub-$50M). win_rate **0.4676** (n=139, bearish_flow proxy, below the 0.50 floor → starter pre-risk).
- `fundamentals_verdict`: CAUTION. `debate_residuals`: {bull 0.55, bear 0.85}.
- `gate_verdicts`: regime no-op · vrp no-op · panic no-op · cluster no-op · sector no-op · **fundamentals −1** · **event_risk −1 (FOMC+OPEX T+3)** · **debate −1 (bear≥bull)** · **rubric_regime cap-half (OUT-OF-REGIME)**. Four independent gates each push it to no-capital. Invalidation of the *thesis*: a dovish FOMC compresses HY spreads and squeezes the Jun18 leg.

**Expectancy lens (advisory — C31):** not displayed this week — there is no live tier book to compute per-tier expectancy over, and the rolling `conviction_<date>` closed-call set is what the next `/calibration-audit` will measure. The honest expectancy signal this week is the §0 scorecard: 35% hit on resolved calls with the one HIGH-tier call a loss.

**Embedded rubric (for audit):**

```
Weekly conviction score (FROZEN v2026-06-12) = Σ:
  +3  oi-trend BUILDING full week, --days≥5 (accumulation/leap)
  +3  3+ aligned accumulation signals + block-stratified institutional tier — CONJUNCTION (halve to +1 if cum_flow_30d not sign-aligned & |≥$50M|)
  +1  conviction-matrix DIRECTIONAL_LONG conf>70 stable — ONLY if dominant_signal_class==leap_directional
  +2  oi position-rolls institutional roll forward into longer-dated LEAP
  +1  cumulative-premium-flow net directional accretion — INTENT-SCREENED (0 if distribution_flag or div-capture)
  +1  dealer-positioning MECHANIZED DEX flip / vanna squeeze in trade direction (verified sign-change only)
  +1  sector-rotation single-name leader — only if persistence≥0.6 AND cum_flow aligned AND |≥$50M|
  +1  earnings-scout BUY/SELL VOL next 2wk, term-skew aligned
  +2  multileg-strategist directional structure repeated on ≥2 days
  +1  vol-surface KINKED/BACKWARDATION worsening WoW; iv-pct-zscore extreme; VRP-aligned
  +1  opex-pin-strategist top-5 (OPEX week only)
  -2  contrarian crowded-long, rising pc-ratio-z (VRP positive) — informed-flow continuation penalty
  -3  flow_conflict (cum_flow_30d clearly opposite dominant class)  /  -1  flow_conflict_lite (MIXED)
  [TIER GATES, risk-monitor 2d, 0 score points]: -1 tier corr-cluster ≥0.70; -1 tier WoW regime flip vs direction
Tiers: ≥9 HIGH · 7–8 MEDIUM · 3–6 LOW · ≤2 drop.  (Bands FROZEN; failed re-confirmation 2026-06-12, no validated ranking claim; P0.6 half-cap active.)
```

## 9. Setups for Next Week
- **Next-session GEX advisory (SPY/QQQ only — advisory, 0 points).** Backtest verdict: **`NO_GO_NO_EDGE`** — over 60 sessions the walls were *not* magnets (SPY closed near a wall 27.3% of sessions, QQQ 29.5%, both below the 50% coin-flip). Treat these as dealer context, not a forecast.
  - **SPY** (EOD 06-12, spot 741.8): freshly-flipped POSITIVE regime but **thin and fragile** (total_gex +$39.6M after a full week of FULLY_NEGATIVE). Call wall **742–743** (spot pressing it), put wall **735**. ZGL unreliable (deep-extrapolated). Soft long-gamma pin 735–743 with no OI mass to enforce it.
  - **QQQ** (spot 721.9): POSITIVE, stronger (+$425M). Pinned between 720/723 nodes; range 715–723. Marginally better-supported pin than SPY.
  - Caveats: EOD book = prior refreshed after the open; gap risk elevated into FOMC; ETF-not-index book; cannot isolate the D+1 expiry. By Wednesday the prior is stale without a fresh read.
- **Next-session 0DTE premium-selling setup (validated stack — advisory, 0 points).** Backtest verdict **`GO_PREMIUM_SELL_INTRADAY`** (delta-neutral, n=44). **SPY:** sell premium, vol_state MID (VIX 17.68), expected range ±0.77%, iron fly / short straddle centred 742.5; `mean_pnl_open_pct` **+0.319% GROSS / +0.219% NET** of assumed round-trip cost (basis: **% of underlying spot notional**, not premium-collected). **QQQ:** range ±1.21%, centred 722.8 (weaker than SPY). Rules: sell only when front IV is rich (size by VIX level), wing width from the GEX vol-suppression range, **enter at the open / never carry overnight** (overnight mean −0.193%), stand aside on a VIX spike or front-end backwardation. **Permanently advisory** until a vol-shock day enters the sample and net expectancy clears a tail-aware bar — win-rate is *not* the promotion metric (short vol is negatively skewed; the validation sample has no tail). **Stand-aside flag for next week: FOMC Wed 06-17 is a live vol-shock catalyst — do not run the intraday short-vol on the FOMC session.**
- **Swing dealer setups (advisory):** IWM is the one mechanized DEX-flip-long, but it directly conflicts with a 3-day-repeat bearish put-vertical and a distribution read on the same name — **no clean swing**. Watch the 06-13 SPY DEX print for a possible score-eligible flip confirmation.
- **Pin vs trend:** **Pin-lean into a Fed wildcard.** Thin positive gamma argues mild pin, but FOMC 06-17 + OPEX 06-18 inject binary gap risk that overrides the pin. Prefer defined-risk.
- **OPEX-week ranked book (`opex-pin-strategist`, expiry Thu 06-18 — FOMC 06-17 materially elevates pin-failure risk; prefer iron flies; enter post-FOMC):**

| Rank | Ticker | Pin | Spot | Dist | GEX@pin | Structure |
|---|---|---|---|---|---|---|
| 1 | LQD | 109 | 109.00 | 0.0% | +$276M | Short straddle (post-FOMC) / iron fly pre-FOMC — rate-sensitive, FOMC-binary |
| 2 | HYG | 81 | 79.94 | 1.3% | +$463M (highest pin_score) | Broken-wing butterfly (upward bias) — credit, FOMC-binary |
| 3 | NOK | 15 | 14.78 | 1.5% | +$44M | Iron fly (verify liquidity) |
| 4 | TSLA | 400 | 406.44 | 1.6% | +$11M | Broken-wing butterfly (downward bias to 400) |

  SPY/QQQ/IWM disqualified (negative GEX at their max-OI strike — put walls, not pins).
- **Actionable HIGH-tier setups for the coming week:** none. This is a **stand-aside week** — the regime is transitional, the rubric is out-of-regime, FOMC + OPEX compress the calendar, and the scoring fleet's own intra-week hit rate was 35%. The desk's edge next week is *not deploying directional size into a Fed wildcard.*
- **LOW-tier names to track for daily-analysis confirmation:** the semis-long cohort (MU/LRCX/AMD/SNDK) if the post-flip rip resumes; ACN/FDX earnings-vol calendars; the SPY DEX-flip confirmation.
- **Deep-dive hand-off:** skipped — no HIGH-tier name to hand off on a no-edge week.

## 10. Watch-only — single signal, no confluence
Surfaced by one agent or directionally conflicted — for journaling, **not** trade entry:
- **IWM** — DEX-flip LONG vs put-vertical BEARISH vs accumulation DISTRIBUTION (4 agents, no net direction).
- **META** — CommSvc sector leader (long), but dealer-disqualified and accumulation MIXED.
- **INTC / MRVL** — clean bullish sweep + OI-opening, but single scored agent (semis RS).
- **GS** — contrarian OPENING_PUT_PRIME short vs Financials sector-leader long (conflicted).
- **SNDK** — mixed sweep + event backwardation + single-session LEAP block.
- **XOM** — accumulation near-miss (DIRECTIONAL_LONG 45%, $602M single-session mega-DP, no multi-day persistence).
- **BAC / TROW / AXP** — Financials sector leaders (single agent each).
- **DRI** — clean non-event SELL-VOL candidate (vol-surface only; earnings-scout flags tail-hedging).

---
*Rubric version 2026-06-12 (frozen). Regime status OUT-OF-REGIME — all sizing capped at half. GEX walls advisory NO_GO_NO_EDGE; 0DTE premium-sell advisory GO but stand aside on FOMC 06-17. Generated 2026-06-13.*
