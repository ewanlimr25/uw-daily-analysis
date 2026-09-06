# Daily Market Analysis — 2026-07-29

## Executive Summary

- **Regime + GEX state:** **TRANSITIONAL / CHOPPY** on FOMC decision day. SPY 729.46 (−1.54%), below both the 20-SMA (745.79) and 50-SMA (744.66); VIX **20.66, +13.45% 1d / +24.16% 5d**. Breadth 32.5% bullish flow (`uw`), 36.2% green (`fz`, 182 advancers / 321 decliners) — the two lineages agree, no divergence. **Both SPY and QQQ dealer-gamma books are FULLY_NEGATIVE with `zero_gamma_level` null** — no positive-GEX strike anywhere in the 0–45 DTE book, so no gamma cushion in either index. Sector lean: cyclical→defensive with a violent semis-specific unwind on top.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL/CHOPPY) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** **SPY** — FULLY_NEGATIVE, ZGL `null` (unreliable), `total_gex` −2.78B, amplification strikes 730 above / 725 below (both within 1% of spot) · trend/breakout prior, no pin. **QQQ** — FULLY_NEGATIVE, ZGL `null`, `total_gex` −1.18B, 665 above / **660 just 32bp below spot and the single largest-magnitude strike in the grid** · asymmetric downside-accelerant. Advisory, prose-only — see §2.
- **Top swing build:** **NONE.** Zero names cleared the conviction floor. This is the **20th consecutive empty board.**
- **Top LEAP candidate:** **NONE.** Zero of 7 evaluated candidates cleared 6-of-9 gates.
- **Biggest risk:** **June Core PCE, Friday 2026-07-31 — two sessions out, Tier-1, core PCE already running 3.41% YoY** — inside every swing horizon on the board, with both index gamma books fully negative and no cushion. The correlation cluster that mattered was `AI_semis_power_cluster` (INTC/SMH **0.900**, BE/INTC 0.782, BE/SMH 0.711) — three of five candidates were one bet. **Carrying zero new risk into Friday is the trade.**

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** *"TRANSITIONAL — Mixed signals, reduce position size, wait for clarity."* Trend **CHOPPY**. SPY 729.46, −1.56% over 30 days, −4.07% from the 90-day high, below both the 20- and 50-day SMAs. Market breadth: 2,043 bullish-flow tickers vs **4,236 bearish** across 6,279 optionable names = **32.5% bullish**. Tool guidance: *"Half position sizes. Favor defined-risk strategies."*

**The tape framing is the most important call of the day, and it is not "broad selloff."** Equal-weight **RSP closed −0.90% and is +1.42% over 5 days**, while cap-weighted **SPY is −1.54% / −2.40%**. Defensives are green on the week. What actually happened is a concentrated de-rating of the AI-capex/semis complex:

| Index / ETF | 1d | 5d | rv20 |
|---|---|---|---|
| SPY | −1.54% | −2.40% | 10.4 |
| QQQ | −2.04% | **−6.18%** | 20.1 |
| IWM | −1.64% | −1.78% | 12.0 |
| **RSP** (equal-weight) | **−0.90%** | **+1.42%** | 10.0 |
| VIX | **+13.45%** | **+24.16%** | — |
| **SMH** | **−4.79%** | **−14.09%** | 45.8 |
| **SOXX** | **−5.38%** | **−16.29%** | 55.3 |
| XLK | −2.64% | −7.60% | 27.0 |
| XLI | −3.19% | −1.22% | 16.2 |
| XLV | −0.61% | **+4.27%** | 19.7 |
| XLP | **+0.34%** | **+3.53%** | 19.2 |
| XLE | **+1.88%** | −0.93% | 20.6 |
| XLRE | −0.11% | **+2.11%** | 14.4 |
| XLB | −1.15% | **+1.81%** | 18.5 |

Five-day single-name carnage inside that complex: **SNDK −36.5%, NBIS −32.1%, MOD −28.7%, ACMR −27.1%, FORM −26.4%, ONTO −26.1%, DOCN −25.2%, BE −25.0%, MU −23.0%, INTC −20.2%, TSLA −20.2%, NVMI −19.3%, MTSI −19.1%, DELL −16.3%, TLN −16.2%.** Against that, the day's up-moves were **GRMN +16.23%** (top S&P mover), CAKE +13.6%, CLH +7.5%, ASH +7.1%, CHEF +5.4%, TEVA +9.6%, CVE +5.1% — Industrials, Consumer Defensive, Basic Materials, Healthcare, Energy. That is rotation, not capitulation.

**Per-index gamma (current-state EOD book; §2 carries the forward read):**

| Symbol | Spot | Zero-gamma | `total_gex` | Regime | "Call wall" | "Put wall" |
|---|---|---|---|---|---|---|
| SPY | 729.21 | **`null`** (unreliable) | **−2,777,514,095** | **FULLY_NEGATIVE** | 730 (−271.5M) | 725 (−233.7M) |
| QQQ | 662.13 | **`null`** (unreliable) | **−1,183,452,664** | **FULLY_NEGATIVE** | 665 (−76.9M) | **660 (−209.3M)** |
| IWM | — | — | — | toggling POSITIVE/FULLY_NEGATIVE with no clean crossing; ZGL degenerate (155–196 vs ~290 spot) | — | — |

**There is no classic call wall on either index today.** Both books are negative at *every* strike in the 0–45 DTE grid, so the conventional "largest +GEX strike above spot" does not exist. The levels above are re-labelled **amplification strikes** — the heaviest negative-GEX clusters flanking spot, where dealers hedge *with* the move rather than against it.

**`uw options-flow dte-volume-share`:** 0DTE **34.8%**, weeklies 27.2%, monthlies 20.9%, LEAPs 3.0% — `regime_hint: BALANCED`. On an FOMC day, monthly+ share of only **23.9%** means institutional positioning share is diluted; every single-day directional read in this report is discounted accordingly.

**`uw historical vrp`:** SPY **+0.0511 PREMIUM_SELLING** (IV30 17.3% vs realised 12.19%); QQQ **+0.0357 FAIR** (27.66% vs 24.09%). **Read this with the caveat, not the headline:** the realised leg is a 30-day trailing window that *pre-dates today's vol expansion*. A VIX that just jumped 13.45% to 20.66 is not in that 12.19% number. Premium-selling is **stale and weakened, not confirmed** — and `zerodte_setup` independently returns `size_scalar 0.0` / stand-aside on both indices.

**Macro backdrop (`scripts/fred_macro.py`):** Yield curve **normal** (10Y−2Y +0.45). Core CPI **2.81% YoY** but core PCE **3.41% YoY** — the Fed's preferred gauge running well above target and above core CPI. Unemployment 4.2%, payrolls soft at **+57k**. **10Y at 4.61% and RISING (+23bp/30d)**; 2Y 4.26% (+19bp); USD weakening; fed funds 3.63%. This is a **stagflation-lite** mix, and rising long rates against decelerating labour is the single worst backdrop for long-duration/high-multiple equity — which is precisely what sold off.

**Forward `event_risk` (next ~10 trading days):**

| Event | Date | Impact | Note |
|---|---|---|---|
| FOMC decision + presser | **2026-07-29** | **Tier-1** | **TODAY — realised.** Source of today's vol expansion. |
| Q2 GDP (advance) + jobless claims | 2026-07-30 | Tier-2 | T+1 |
| **June PCE / Core PCE + ECI** | **2026-07-31** | **Tier-1** | **T+2 — inside EVERY swing horizon** |
| July nonfarm payrolls | 2026-08-07 | Tier-1 | T+7 |
| July CPI | 2026-08-12 | Tier-1 | T+10 |
| July PPI | 2026-08-13 | Tier-2 | T+11 |
| FOMC (September) | 2026-09-15 | Tier-1 | Outside window; relevant to LEAP/monthly |

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — open interest that persists overnight — read forward as the *prior* for the next session's open. It is **prose-only, contributes 0 points** to the conviction rubric, and makes **no backtested predictive claim**. Predictive validation of these levels lives in `/weekly-analysis`'s rolling §2 backtest, not here. Scope is **SPY and QQQ only.**

### SPY — FULLY_NEGATIVE, no cushion
`spot 729.21` · `zero_gamma_level null` · `zgl_reliable false` · `total_gex −2,777,514,095` · amplification strikes **730** (−271.5M, 0.11% above — essentially ATM) and **725** (−233.7M, 0.71% below), secondary **720** (−213.9M, 1.26% below).

**Read:** dealers are short gamma at *every* strike in the book — there is no mean-reversion cushion overnight. Spot sits pinned between two deeply negative strikes; a break of either **accelerates rather than absorbs**. This is a trend/breakout prior, not a pin prior.

**Structure bias:** short-gamma with walls straddling spot and no positive-GEX brake → directional debit verticals, or a long/wide straddle if the overnight gap is large. **Explicitly NOT iron fly / short straddle / condor** — there is no gamma cushion to sell against.

### QQQ — FULLY_NEGATIVE, asymmetric to the downside
`spot 662.13` · `zero_gamma_level null` · `zgl_reliable false` · `total_gex −1,183,452,664` · amplification strikes **665** (−76.9M, 0.43% above; secondary 680 at −67.4M) and **660** (−209.3M, **0.32% below**; secondary 650 at −93.1M).

**Read:** the same fully-negative picture, but deeper and closer *below* spot than above. **660 is the single largest-magnitude strike in the entire QQQ grid and sits 32bp under spot** after today's −2.04% semis-led drubbing. A break of 660 meets the least dealer resistance of any level in the book; 665 overhead is materially smaller. Asymmetric downside-accelerant into the open.

**Structure bias:** skew any directional structure to the downside (put debit verticals), or a long straddle on a wide gap. No condor, no iron fly.

### Regime freshness — HELD, not fresh
From `uw historical gex-time-series`: both books have been **FULLY_NEGATIVE essentially every session since 2026-07-17 (SPY) and 2026-07-16 (QQQ)**, with only isolated self-reverting blips on 07-21/07-22 that did not hold. **Today's FOMC deepened an entrenched regime rather than triggering it:** SPY `total_gex` hit **−2.78B, its most negative print of the trailing window** (prior deepest −2.47B on 07-23); QQQ deepened from −1.08B to −1.18B. This read therefore carries more standing evidence than a fresh flip would — but it is a deteriorating regime, not a setup.

### Mandatory caveats
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and re-computes the ZGL and these strikes before the open even settles.
- **ZGL is `null` and unreliable on both indices** (FULLY_NEGATIVE regime). This read leans entirely on the `total_gex` sign plus strike concentration — there is no distance-to-flip calculation available.
- **Gap risk voids the prior.** June Core PCE prints **Friday 2026-07-31**, two sessions out. Do not extend this map past tomorrow's session.
- **Tooling limit.** `uw-pp` cannot isolate the D+1 expiry (`gex --dte-max 1` errors). This is the standing **0–45 DTE** book, diluted by monthly/LEAP OI — the best available proxy, not the isolated next-session expiry.
- **ETF book.** These are the SPY/QQQ **ETF** gamma books, not the cleaner SPX/NDX index books.

### 2a. Next-session 0DTE premium-selling setup — **STAND ASIDE BOTH INDICES**

> Advisory, delta-neutral, **0 rubric points**, and explicitly **not** a guaranteed edge — the validation sample contains **no vol shock, so the short-vol left tail is UNSAMPLED**, and today is precisely that regime.

The rolling backtest verdict remains `GO_PREMIUM_SELL_INTRADAY` on both (SPY n=60, win 90.0%, `mean_pnl_open_pct` **+0.242% gross → +0.142% net** of an assumed 0.10% round-trip cost, worst day −1.40%; QQQ win 86.7%, **+0.369% gross → +0.269% net**, worst day −2.453%). **`pnl_basis`: percent-of-underlying-spot-notional, GROSS** — not premium-collected, not margin-relative, so lead with the net figure and note it is tiny in absolute terms.

**But the live setup is OFF on both:**

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | **false** | **false** |
| `vol_state` / VIX | HIGH / 20.66 | HIGH / 20.66 |
| `implied_move_pct` | 1.50% | 2.46% |
| `expected_range_pct` | 1.21% | 2.02% |
| **`size_scalar`** | **0.0** | **0.0** |
| `suggested_structure` | wider iron condor ±1.21% — *or reduce / stand aside* | wider iron condor ±2.02% — *or reduce / stand aside* |
| `entry_rule` | enter at/after the open once the gap resolves; hold to the close; never carry overnight | same |
| **`stand_aside_reason`** | **VIX spiking (+2.4) — short-vol left-tail regime** | **VIX spiking (+2.4) — short-vol left-tail regime** |
| `caution` | — | **front-end backwardation (0DTE IV 1.89× VIX) — event/gap risk; half size** |

**The GEX read in §2 independently corroborates the stand-aside:** a FULLY_NEGATIVE book with no positive-gamma strike anywhere offers no cushion to sell premium against. **SPY ≈ SPX** (validated identical). **QQQ is the weaker of the two** (Nasdaq index book unavailable) — flag its lower confidence. Direction: **none** — this lane is delta-neutral; do not add a directional tilt.

**Promotion bar unchanged:** this lane stays advisory / 0 rubric points **permanently** until BOTH a vol-shock day enters the sample AND **net** expectancy clears a tail-aware bar. Win-rate is explicitly not the promotion metric for a negatively-skewed short-vol strategy.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

**Zero names earn the mechanized +1 DEX-flip line, and zero vanna squeezes are valid.** All 14 names tested through `scripts/dex_flip.py` (SPY, QQQ, IWM, NVDA, MU, AMD, MSFT, META, GOOGL, AMZN, TSM, MRVL, ASML, SMH) returned `qualifies: false`.

The dominant reason is instructive: **many names did flip mid-window, but not on the latest session.** NVDA flipped 07-27; AMD and GOOGL 07-28; MU, TSM and MRVL 07-24; ASML 07-22. By 07-29 the sign had already settled for 1–2 sessions, so there is no *fresh* opposite-sign run immediately preceding today — correct per the frozen P0.4 definition (a settled level is not a flip). **Whipsaw warnings** fired on GOOGL (4 sign changes in the window) and ASML (4).

**No vanna squeeze is available book-wide today, structurally.** The frozen definition requires a put-heavy book **and falling VIX**. VIX *rose* 13.45%. Every put-heavy name is therefore flagged "vanna pressure, not squeeze" — SPY, QQQ, IWM, NVDA, MU, AMD, META, AMZN, TSM, MRVL, ASML, SMH. Only MSFT (`net_vanna` −7,297) and GOOGL (−1,280) are call-heavy, which makes them non-candidates under any VIX regime.

Dated `net_dex` (07-22 → 07-29, USD):

| Ticker | Trajectory | Read |
|---|---|---|
| SPY | −8.71B → −50.52B → −38.43B → −34.52B → −26.08B → **−75.23B** | Negative, deepened sharply on FOMC |
| QQQ | −14.74B → … → **−65.02B** | Negative, deepening |
| IWM | −5.76B → … → **−15.58B** | Negative, FOMC spike |
| **SMH** | −4.27B → −4.68B → −8.98B → −13.66B → −15.52B → **−22.52B** | **Monotonic every session, ZERO sign changes, no whipsaw — the cleanest multi-day dealer-flow deterioration in the entire book**, matching −14.09% 5d spot. GEX also monotonic FULLY_NEGATIVE, −193M → −334.6M. |
| MU | +3.60B → +4.96B → −4.06B → −5.41B → −9.12B → **−16.58B** | Flipped NEG 07-24 (stale), monotonically deepening |
| TSM | +1.51B → … → **−3.19B** | Flipped NEG 07-24 (stale), deepening |
| MRVL | +0.69B → … → **−1.17B** | Flipped NEG 07-24 (stale), deepening |
| NVDA | +10.75B → … → **−5.39B** | Flipped NEG 07-27 (stale) |
| AMD | +7.66B → … → **−2.98B** | Flipped NEG 07-28 (stale) |
| **MSFT** | +2.81B → +0.71B → +1.03B → +2.84B → +3.60B → **+2.94B** | **POSITIVE all window — a LEVEL, never a flip.** Textbook illustration of the failure mode the 2026-06-12 P0.4 audit exists to prevent. |
| **GOOGL** | −0.10B → −4.44B → −2.29B → −0.21B → +0.94B → **+1.54B** | Flipped POS 07-28 (stale), improving; GEX recovering 3 straight sessions (50.8M → 70.6M → 90.4M) |
| META | +3.46B → … → −0.36B | Whipsaw, 3 sign changes, no trend; `total_gex` cushion thinning 131M → 16M |
| AMZN | +2.36B → … → −0.68B | Whipsaw; flip on FOMC day itself = noise |
| ASML | +0.40B → … → −0.90B | Flipped 07-22, thin single-digit-million GEX against a $1,551 underlying — low confidence |

**Front-end IV ratio at `--near-dte 7`** (>1.05 = front panic): AMZN **1.689** (highest, and the earnings scout resolved it — AMZN reports 07-30 postmarket), MSFT **1.544**, META **1.345**, ASML **1.282**, AMD **1.206**, TSM **1.16**, QQQ **1.129**, MU **1.084**, SMH 1.054, MRVL 1.047, GOOGL 1.039, SPY 1.029, IWM 1.002, NVDA 0.980.

**Swing bias:** every name **NEUTRAL**, all unscored. Notable advisory reads — **SMH** is the highest-priority flag (cleanest bearish dealer-flow deterioration in the book, but blocked from a directional call by the frozen vanna/DEX-disagreement rule since the put-heavy book is a latent *long* vanna mechanism). **GOOGL** is the one name where DEX trajectory, GEX recovery and the call-heavy vanna mechanism all point the same way with a non-panicked front end — advisory LONG at low-to-moderate confidence, explicitly not a scored flip.

**A regime-label defect worth recording:** on NVDA, AMD and MRVL the `gex-time-series` **regime label stayed POSITIVE while `total_gex` had already gone negative**. Treat the `total_gex` sign as ground truth, not the label. The ZGL values on SPY/QQQ/IWM/MU are the known degenerate-grid artifact (QQQ ZGL 352.82 against a ~706 spot) — do not trust the numeric level on those four.

---

## 2b. Sector Rotation

**Rotation regime call: `cyclical→defensive`, with a distinct semis-specific growth unwind layered on top. Confidence MEDIUM.**

**Durable on the SHORT/OUT leg; air-pocket-leaning on the LONG/IN leg.** The out-side is confirmed multi-day, cross-instrument (ETF options flow agrees) and single-name (30d cum-flow agrees). The in-side is **GICS-aggregate only** — XLF is flat (−$0.47M), XLC is *bearish* (−$2.29M), KRE is *bearish* (−$3.07M), and **zero single names clear the full 3-leg conditional on the long side.** Today reads as *"sell the losers with conviction; nobody is funding a matching long book yet."* The fundamental case for durability is real (10Y +23bp/30d, core PCE 3.41%, soft payrolls all compress long-duration multiples) — but it is not funded yet.

**⚠ Two measurement traps, both caught live today:**

1. **`persistence_score` is saturated and non-discriminating.** 8 of 11 sectors sit at the 1.0 ceiling, 2 at 0.8, 1 at 0.6. The conditional +1 gate requires ≥0.6, so it fires for essentially the whole board and **cannot rank within the top group.** The discriminating leg today was signed net-flow magnitude vs the cross-sector median (**$100.15M**) combined with aggressor-classified direction.
2. **`sector-flow-persistence` `net_flow` is gross call$ − put$ and is sign-agnostic to aggressor side — it measures TURNOVER, not accumulation.** Caught in two places: **(a) Technology's "+$223M inflow"** — aggressor-classified names inside Technology sum to +$269.5M bullish vs −$239.3M bearish = net **≈+$30M**, nowhere near the gross headline, and it masks a clean software-vs-semis bifurcation rather than sector-wide accumulation. **(b) Energy's persistent 5-day "inflow" ($61–104M/day)** is contradicted by its own aggressor-classified instrument — **XLE 5d options net-flow −$17.0M BEARISH** with price −0.93% 5d. Treat GICS "Energy inflow" as a **false positive.**

| Sector | `persistence_score` | 07-29 net_flow | vs median $100.1M | Standout |
|---|---|---|---|---|
| Communication Services | 0.8 | +$364.8M | above | yes |
| Consumer Cyclical | 1.0 | **−$313.3M** | above | **yes (outflow)** |
| Technology | 1.0 | +$223.1M | above | flagged — gross-turnover trap, not clean |
| Financial Services | 1.0 | +$188.1M | above | yes (but XLF/KRE disagree) |
| Industrials | 0.8 | **−$151.0M** | above | **yes (outflow)** |
| Consumer Defensive | 1.0 | +$100.1M | = median | no |
| Healthcare | 1.0 | +$88.1M | below | no |
| Energy | 1.0 | +$61.0M | below | no — **XLE contradicts** |
| **Utilities** | **0.6** | **−$23.6M** | below | **contradicts the defensive pattern** — persistence decaying, last two sessions net outflow; XLU −$0.96M BEARISH agrees. Rising-10Y duration sensitivity. |
| Basic Materials | 1.0 | +$18.7M | below | no |
| Real Estate | 1.0 | +$13.3M | below | no |

**Single-name leaders, tagged on the full 3-leg conditional** (persistence ≥0.6 ∧ cum_flow_30d direction aligned ∧ |cum_flow_30d| ≥ $50M):

| Ticker | Sector | Today | `cum_flow_30d` | Aligned | ≥$50M | **All 3?** |
|---|---|---|---|---|---|---|
| **TSLA** | Consumer Cyclical | −$11.5M | **−$751.8M** | ✓ | ✓ | **PASS** |
| **AMZN** | Consumer Cyclical | −$45.2M | **−$248.7M** | ✓ | ✓ | **PASS** |
| **BE** | Industrials | −$28.2M | **−$225.7M** | ✓ | ✓ | **PASS** |
| CVNA | Consumer Cyclical | −$17.8M | **+$52.6M BULLISH** | ✗ | ✓ | FAIL — 30d flow diverges; today looks like a pullback inside a longer accumulation |
| CAT | Industrials | −$9.9M | +$34.7M MIXED | ✗ | ✗ | FAIL |
| GOOGL | Comm Services | +$37.3M | +$29.1M MIXED | ✓ | **✗** | FAIL |
| META | Comm Services | +$27.7M | **−$65.5M** | **✗** | ✓ | FAIL — 30d flow net bearish despite a bullish print today |
| CRBG | Financials | — | −$1.7M BEARISH | ✗ | ✗ | FAIL |

**No long single name clears the conditional today.** The long leg is an index/GICS-aggregate story only.

**ETF flow tape (advisory — strengthens the conditional +1 via `gics_agreement`; adds NO rubric points):**

| ETF | Net premium (5d) | Trend | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| **IGV** | **+$21.38M** | BULLISH | 57% below-mid (sell-skewed) | **66% put premium** — hedging on top of a bullish trend | agree (Tech software leg) | MSFT, NOW, ADBE, CRM |
| XLY | +$8.74M | BULLISH | 72% sell-skewed | negligible | **disagree** — trivial vs Consumer Cyclical's −$4.66B 5d GICS outflow; **noise, do not read as rotation-in** | none extracted |
| **EWY** | +$3.69M | MIXED | **80% BUY-skewed on the largest print total of the deep-pull set ($360M)** | put premium executed **at the bid** (put-selling = bullish) | n/a (geographic) | — |
| XLV | +$2.80M | BULLISH | — | — | agree | — |
| XOP | +$2.35M | BULLISH | — | — | n/a (diverges from XLE) | — |
| XLRE | +$0.18M | BULLISH | — | — | agree | — |
| XLF | −$0.47M | MIXED | — | — | **disagree** — does not confirm Financials' $188M inflow | — |
| XLK | −$0.77M | MIXED | — | — | disagree/flat — confirms the Tech bifurcation | — |
| XLU | −$0.96M | BEARISH | — | — | agree — confirms genuine Utilities de-risking | — |
| XLC | −$2.29M | BEARISH | — | — | **disagree** — contradicts Comm Services' inflow | — |
| **XLI** | **−$2.47M** | BEARISH | — | — | **agree** — confirms Industrials outflow | BE |
| KRE | −$3.07M | BEARISH | — | — | disagree — regional banks cracking inside the Financials "inflow" | BANC, BAC, TPG |
| GDX | −$10.63M | BEARISH | 63% sell-skewed | — | n/a — undercuts a safe-haven narrative | — |
| **XLE** | **−$17.03M** | BEARISH | mild sell-skew | small/mixed | **disagree — the sign-agnostic trap caught live** | — |
| **SMH** | **−$26.58M** | MIXED | — | **94% put premium ($157.0M put vs $9.8M call)** | **disagree at GICS level, but this is the trustworthy read** | — |

**EWY is the most interesting instrument-level divergence on the tape** — genuine buy-side conviction in the Korea/Samsung/SK-Hynix semis supply chain while SMH is being sold. Instrument-only (`gics_agreement: n/a`), advisory.

**Swing-book implication:** the confirmed short leg (TSLA / AMZN / BE, all three legs cleared) plus SMH as instrument-level context is the only funded side. **Stand aside on the long defensive/value leg.** Downgrade everything uniformly for FOMC-day 0DTE dilution.

---

## 3. Swing Setups (1–6 weeks)

### **EMPTY. Zero names cleared the conviction floor.**

Four candidates entered Phase 2; all scored **DROP** (≤2). The board is flat for the **20th consecutive session.**

| Ticker | Direction | `raw_score` | Tier | Fundamentals | Debate (bull/bear) | Final |
|---|---|---|---|---|---|---|
| TSLA | short | **1** | DROP | CONFIRM | 0.30 / **0.55** | **skip** |
| BE | short | **1** | DROP | **VETO** | 0.30 / **0.40** | **watch-only** |
| TWLO | vol_short | **1** | DROP | CONFIRM | **0.72\*** / 0.25\* | **skip** |
| INTC | long | **−1** (+2 −3) | DROP | CONFIRM | 0.30 / **0.65** | **skip** |
| SMH | short | **−3** (0 positive, −3) | DROP | NA (ETF) | 0.32 / **0.65** | **skip / context** |

\* TWLO polarity is inverted — see §7.

**The debate gate fired on all five names.** Bear beat bull on all four directional calls, and on TWLO the anti-thesis side won decisively.

### 3a. Long swings (regime-aligned) — **none**

The only long thesis on the board was **INTC**, and it failed the Step 3 confluence gate (exactly one agent flagged it positively) before the score even mattered. It is documented in §7 and §8 as the day's most substantive near-miss.

Three accumulation candidates surfaced and all three were **HALVED by the C11 conjunction** (`cum_flow_30d` far below the $50M confirmation threshold), leaving them single-agent and below the floor:

| Ticker | 1d / 5d | DP evidence | `cum_flow_30d` | Conjunction | DP shelf (C34) | `distribution_flag` |
|---|---|---|---|---|---|---|
| **TEVA** | **+9.6% / +15.1%** | block `buy_ratio` 0.74 ($32.3M, 11 trades); **228 DP trades spread 13:38Z–20:08Z with no closing-cross clustering**; `institutional-accumulation` ACCUMULATION `buy_sell_ratio` 1.85; oi-trend BUILDING 5 consecutive days, today +4,533 = 63.8% of top-contract volume, call-leaning 3,419 call-lots vs 241 put-lots | **+$4.44M** | **HALVED_1** (fails $50M by ~11×) | **$34.71** | present but mild (Sep-18 35C, OI −753, ~$152K) |
| **CVE** | **+5.1% / +0.3%** | mega `buy_ratio` 1.0 ($12.27M @21:20:41Z at NBBO ask); block 0.922 ($13.4M, 4 trades); `buy_sell_ratio` 6.2; BUILDING 5d | **−$1.45M — WRONG SIGN** | **HALVED_1 + contradicts** | **$29.07** | absent |
| **SNN** | +0.3% / +9.1% | mega `buy_ratio` 1.0 ($26.0M, 2 trades at NBBO ask, `trade_vs_mid` +0.315); `buy_sell_ratio` 7.93 | +$8,997 (noise) | **HALVED_1** (fails by >5,000×) | **$32.66** | absent |

**SNN's OI leg is confounded and should not be credited:** today's +10,001 OI is *entirely* a 5,000-call + 5,000-put simultaneous open at the **same Aug-21 $35 strike** — that is a **straddle, not a directional bet.** The BUILDING label is technically true and substantively meaningless.

**Rejected accumulation candidates, with the artifact that killed each** — these negatives are the most useful output of the lane today:

- **MMM** — closing-cross contamination (block prints cluster 20:04:36–20:12:50Z at an identical $177.95) **plus a synchronized twin-print artifact**: the 20:04:38Z, 18,938-share, $3,370,017.10 print appears **twice**, identical timestamp + size + price.
- **EA** — the mega tier ($20.9M) is a **matched/crossed trade**: 50,000 buy / 50,000 sell at 13:44:20Z–13:44:52Z, `buy_ratio` exactly **0.5**, net zero signal. The apparent 0.928 block buy ratio is entirely closing-cross prints at an identical $208.91.
- **CAKE** — internal DP-tier disagreement: one clean mega buy ($16.4M @15:39:40Z, ratio 1.0) against a **net-selling block tier (0.477)** with prints 15–25¢ below mid. A single large print does not outweigh broader intraday distribution.
- **SOLV, LBRT, SMTC, LW, CZR, CRBG** — institutional-tier size failure. All C12-pass and all tagged `dp_accumulation`+`oi_building` by the funnel, but direct `block-stratified` queries cap `highest_tier` at "block" on 1–3 trades each, total DP premium $6–16M. Too thin to distinguish from noise.

### 3b. Short / fade swings (defined risk only) — **none sized**

**`contrarian-scanner` returned an empty fade book.** Index-level: SPY z **+1.839** (elevated fear-side but under 2σ), QQQ z −0.708 — the index-fear-fade condition is unmet, and the literature only supports a standalone fade at index level. **DOCN** was the sole single-name BEARISH_EXTREME (z **+2.303**, P/C 2.921 vs 20d mean 0.722) and disqualified on three counts: single-name extremes are a *continuation* caution not a fade signal; `price_vs_flow` `divergence=FALSE` (price −38.7% and flow both bearish, no smart-money contradiction to lean on); and earnings in 6 days makes it pre-earnings put positioning rather than clean crowding.

**The semis complex reads NEITHER bullish- nor bearish-extreme.** The ETF proxies sit in NORMAL despite a −16% 5-day cash move — **SOXX z −0.623, SOXL z −1.489** — i.e. *the options crowd has not reached a statistical positioning extreme even though price has.* Only two single names cross ±2σ and they point in **opposite directions**: **MU BULLISH_EXTREME (z −2.726)** and DOCN BEARISH_EXTREME. There is no coherent complex-wide sentiment extreme to trade in either direction.

**MU is the only name in the fleet earning the −2 contrarian penalty.** P/C 0.692 vs a 20d mean of 1.030 (σ 0.124) — unusually *call*-crowded in the middle of a −23% 5-day / −27% 30-day decline. Classic dip-buy-via-calls. Critically, `price_vs_flow` shows `divergence=FALSE`: price and flow are **aligned bearish**, so there is no smart-money divergence backing the call buyers. Per Pan-Poteshman (2006) and Ge-Lin-Pearson (2016), single-name P/C extremes predict **continuation, not reversal** — this call-crowd sits on the side informed flow tends to run over. **Any long MU thesis anywhere in the book carries this penalty.**

### Sweeps (informational — 0 rubric points)

The `sweep-persistence` rubric line was **removed 2026-05-23 (P0.3)** after a −22pp marginal contribution across two consecutive audits. Sweeps earn nothing unless the name independently earns a scored co-flag.

| Ticker | 5d dominant side | Persistence | Expiry / DTE | Strike | 5d premium | Smart-money read today |
|---|---|---|---|---|---|---|
| SNDK | bearish | 5/5 | 07-31 / 2 | 1390P | $2.057B | **Contradicts itself** — today's screener net flow flipped to **+$107.9M, the single largest bullish print in the entire book**, against a −7.32% day and −36.5% week |
| AMD | bearish | 5/5 | 08-07 / 9 | 400P | $1.597B | **Contradicts** — the dominant OI-build (400P, +16,921, ~92% of volume) is **bid-side dominant** (2,680 ask vs 15,655 bid) = put-*writing*, a bullish/neutral signature |
| INTC | bearish | 5/5 | 09-18 / 51 | 100C | $1.048B | Aggregate confirms (−$30.2M) but the two biggest OI-builds are **both calls** — three-way conflict, low confidence |
| NBIS | bullish | 3/5 | 08-14 / 16 | 220P | $628.7M | **Cleanest in the ledger** — screener +$12.3M agrees; dominant OI-build (220P, +7,026, ~99% of volume) bid-dominant = put-writing |
| BE | bullish | 3/5 | 08-21 / 23 | 130P | $538.7M | **Label is stale and wrong-footed** — screener −$28.2M, a Tier-1 `OPENING_PUT_PRIME` 125P, and a 130P OI build of **+24,577 (~88% of volume) ask-dominant** all say bearish |

**Every mega-cap/index name that hit `sessions_in_top: 5` failed the hedge-flow alignment check** — SPY, QQQ, SPXW, SPX, IWM, AAPL, TSLA, NVDA, AMZN, META, MSFT, GOOGL all returned `cum_flow_30d` **MIXED/near-zero-net** against tens of billions gross (SPY net −$1.4B on $59.7B gross; QQQ −$0.1B on $63.3B). Annotate all as hedge-flow, not directional. Today's raw tape is dominated by 0DTE SPY/NVDA/AAPL/QQQ contracts — textbook FOMC gamma-chasing.

**MU carries the `CLOSING_ANTISIGNAL`-adjacent read** (770P dte 2, size/OI 0.825 = near-closing signature) and, at $4.74B, the largest 5-day sweep premium in the book — but its direction is MIXED and it is disqualified.

---

## 4. LEAP Builds (6–24 months)

### **EMPTY. Zero of 7 candidates cleared 6-of-9 gates.**

This is a genuine finding, not missing data: every name with a real long-dated OI build failed the required **Gate 4** (`cumulative-premium-flow`) hard disqualifier, and the one name that cleared Gate 4 failed on institutional-accumulation and conviction-matrix.

| Ticker | Fresh LEAP build | Gate 4 (`cum_premium_flow`) | Gate 8 (`conviction-matrix`) | Verdict |
|---|---|---|---|---|
| **INTC** | **Yes — the most genuine fresh-LEAP-call signature of the day.** 2027-03-19 $100C +5,053 (ask 5,228 vs bid 649 = **89% ask-dominant**); 2027-06-17 $100C +4,356 (**87% ask**); 2027-06-17 $45C deep-ITM (delta 0.891, size/OI 9.49, opening). Gate 1 PASS (`consecutive_build_days` 10). Not roll-driven (absent from today's 7-name roll list). | **HARD FAIL** — 90d **−$756.1M** on $29.4B gross; 30d **−$966.7M**, `trend_direction` explicitly **BEARISH** | **HARD FAIL** — **COVERED_CALL, confidence 19.6%** ("dark pool buying + call selling — yield enhancement, capping upside"), an outright-reject scenario | **DISQUALIFIED — highest-value near-miss on the board** |
| SNDK | Gate 1 PASS (10 build days) | **The only Gate 4 PASS** — 90d **+$2.505B**, 30d +$868.5M, with a genuinely *smooth* accretion shape (~$27.3M/day early vs ~$28.9M/day late = thesis extension, not a spike) | **FAIL** — MIXED, 5.2%. Also **Gate 7 FAIL**: `institutional-accumulation` **NEUTRAL**, `buy_sell_ratio` **0.81** (sell-side > buy-side) | **DISQUALIFIED** — and see the artifact below |
| NVDA | 2027-12-17 $215C +3,989, but ask/bid near-balanced (2,657/3,046, ~46% ask) — not a clean fresh-buy | FAIL — 90d −$339.8M, 30d −$110.0M, flat/noise vs $86B gross | FAIL — MIXED, 0.3% | DISQUALIFIED |
| PLTR | 2028-01-21 $210C +7,797 is the largest call-OI increase at that expiry, but **ask 313 vs bid 7,885 = 96% BID-dominant — the call was SOLD** (covered-call supply). Simultaneously a 2028-12-15 $120P build +2,796: writing calls *and* buying puts = net bearish-to-neutral | FAIL — 90d −$218.8M, 30d −$205.3M | FAIL — MIXED, 4.9% | DISQUALIFIED (Gate 2 effectively fails too) |
| MU | **Does not appear in the top-60 fresh LEAP OI list at all** — no genuine long-dated build. The 2027-09-17 $1100C ($9.1M, size/OI 0.687 = borderline-closing) is a single context-only print | FAIL-as-flat — 90d +$270.9M / 30d +$336.2M against **>$100B gross both windows** = noise | FAIL — MIXED, 1.2% | DISQUALIFIED |
| BE | 2027-06-17 $300C +3,998 ($17.6M) but ~85% OTM vs $163.75 spot | FAIL — 90d −$520.8M, 30d −$225.7M | FAIL — MIXED, 7.6% | DISQUALIFIED |
| TLT | 2028-01-21 $70C, small ($7.4M); mechanically a rate-cut bet, not an equity-LEAP thesis | FAIL — 90d −$148.4M, 30d −$93.3M, explicitly **BEARISH** | — | DISQUALIFIED |

**SNDK's Gate-4 pass is very likely an artifact, and this is worth recording.** The largest SNDK long-dated block (2027-06-17 $1000 strike, executed 19:53:08) is a **matched call+put pair — same size (1,700), same timestamp** — $72.5M call side=**bid (SOLD)** plus $65.3M put side=`no_side`. That is a straddle/strangle combo block, **not a directional call buy, and the call leg was sold.** This is very plausibly what inflates SNDK's `cumulative_bullish` gross into a "bullish" net without real directional accumulation underneath — while the stock fell **36.5% in five days.**

**Where the call-heavy LEAP premium concentration actually comes from.** The expiry heatmap shows genuinely heavy long-dated premium — 2027-01-15 **$2.16B** (call-heavy $1.26B vs $0.90B), 2028-12-15 **$1.83B** ($1.03B vs $0.80B), 2027-06-17 $1.47B (put-heavy), 2028-01-21 $1.16B ($0.71B vs $0.45B). Attribution against today's fresh flow:

- **2027-01-15** — no single name appears in today's top-60 fresh-OI list at dte 170. **This bucket's size is almost entirely pre-existing standing OI, not today's incremental flow.**
- **2028-01-21** — dominated by **PLTR's $210C, which is 96% bid-side (SOLD)** = covered-call supply capping upside, not conviction buying. Secondary names small and mixed.
- **2028-12-15** — dominated by **GME** (two OTM strikes, $27/$30 vs $21.83 spot) and **SOFI** ($30C vs $15.24 spot) — classic retail lottery-ticket profile.

**Conclusion: fragmented and mixed-intent — retail speculation, covered-call/yield-enhancement supply, and standing OI — NOT a single institutional actor "buying duration into the drawdown."** The one coherent institutional signature (INTC) sits at different expiries than all three flagged buckets and dies on Gates 4 and 8 regardless.

**Rate-sensitivity note (fleet-wide):** 10Y at **4.61% and rising (+23bp/30d)** with core PCE **3.41% YoY** is a direct headwind to any long-duration LEAP thesis. Not decisive today since nothing survived, but it is the standing macro objection to this lane.

---

## 5. Volatility Surface

### Substrate contamination hit the predicted maximum today — and this is the section's headline

Today was **both an FOMC day and the largest expiry on the board** ($7.2B premium / 24.3M contracts at the 2026-07-29 expiry). Raw `iv-term-structure` labels were correspondingly useless, confirmed independently by **three** agents:

| Agent | Names | Raw label | After `term_structure_hygiene.py` | Flipped |
|---|---|---|---|---|
| `vol-surface-scout` | 19 | **17 BACKWARDATION (89%)**, 2 FLAT | 3 BACKWARDATION / 6 KINKED / **10 NO_NEAR_TENOR** | **16 of 19** |
| `multileg-strategist` | 12 | **12 BACKWARDATION (100%)** | 5 BACKWARDATION / 7 KINKED | **7 of 12** |
| `earnings-scout` | 22 | mostly BACKWARDATION | 4 KINKED / 9 BACKWARDATION / **9 NO_NEAR_TENOR** | — |

This reproduces and **exceeds** the 2026-07-24 finding (39/41 raw, 14 flipped). The `dte_approx: 0` bucket carries 250–480% average IV on an expiry-day snapshot and inverts every front-vs-back comparison.

**Genuine IV outliers after filtering: ZERO.** **19 of 20** rows in the cached `iv_outliers` payload are *today's* expiry — pin/expiry-day noise (UNG 8.5C `max_iv` **376%**, MU 840P **280%**, NVDA 195P **233%**, INTC 91P 222%). The single non-today row (EOSE 07-31) **fails C12** at $3.14 < $5.00.

**`NO_NEAR_TENOR` is not `FLAT`.** Ten of nineteen names have no surviving tenor at/under 21 DTE — the front end is **unmeasurable**, and a 1.000 ratio there means "no data," never "calm." This affects **9 of 22 earnings names (41% of the universe)**, whose screener-quoted implied moves are therefore **not tradable prices**: PWR (**earnings tomorrow**, quoted 10.63% off an absent near tenor), FSS (tomorrow, 11.37%, one surviving tenor at 23dte/42ct), WTW (tomorrow, 6.8%, 31ct), BR (6.75%), MTSI (17.34%), NVMI (16.39%), **ONTO (20.01% — largest quoted move in the scan)**, QSR (5.23%), SOLV (7.24%). `min_contracts` (default 15) is a **named tunable that is explicitly NOT audit-frozen.**

### Term-structure detail (measurable shapes only)

| Ticker | `shape` | `base_shape` | `front_end_ratio` (near-dte 7) | Kink | iv30d vs realised | `vrp` | Verdict |
|---|---|---|---|---|---|---|---|
| **TWLO** | **KINKED** | **CONTANGO** (both flipped) | **1.491** raw → **1.376** hygienic | dte 9, **2026-08-07**, prominence **20.6%** on only **44 contracts** | 83.6% vs 39.7/38.3 → **+44 to +45, richest in scan** | **+0.4391** | CALENDAR → §7 |
| **DOCN** | **KINKED** | **CONTANGO** (both flipped) | 1.326 | dte 9, 2026-08-07, prominence 8.8% on **1,966 contracts** (genuinely liquid) | 117.4% vs 85.8/90.7 → +27 to +32 | +0.3153 | **SKIP — the trap** |
| SOXL | KINKED | BACKWARDATION | 1.131 | dte 23, prominence 5.5% (weak) | 196.8% vs 188.0/166.5 — **the two realised windows disagree by 21pp** | +0.0878 | SKIP — pure levered macro beta |
| DELL | KINKED | BACKWARDATION | 1.11 | dte 51, prominence 11.1% | 86.8% vs 74.4/82.1 → **+4.7 to +12.5, near-fair** | +0.1246 | SKIP — kink unaligned to any catalyst |
| TLN | KINKED | BACKWARDATION | 1.222 | dte 37, prominence 8.1% on **81 contracts (thin)** | 71.3% vs 58.2/56.4 | +0.1306 | **kink is NOISE** — 09-04 does not align with 08-05 earnings; `iv_percentile` z **2.66, highest in scan**; skew **1.169 TAIL_HEDGING** |
| AMBA | KINKED | BACKWARDATION | **0.956** (near *below* far — internally inconsistent) | dte 30, prominence 5.1% (at floor) | 113.5% vs **116.4** (vrp −0.0294 FAIR) **/ 85.2** (rv20) — **sources disagree sharply** | −0.0294 | SKIP |
| ACMR | BACKWARDATION | — | 1.197 | none — smooth monotonic decay | 125.8% vs 122.3 → **essentially FAIR** despite iv_rank 100 | +0.0356 | SKIP — bare backwardation is not signal |
| SOXX | BACKWARDATION | — | 1.092 | none | 65.5% vs 65.3 → **+0.0018, FAIR** (contradicts the naive rv20 read) | +0.0018 | SKIP — but skew **1.157 TAIL_HEDGING** is legit sector context |
| NRG | BACKWARDATION | — | **1.186** hygienic (raw tool returned **1.298** off a 30dte tenor with only **5 contracts**) | none | 57.9% vs 43.4 | +0.1448 | context → earnings |

**The `high IV rank = cheap vol` hypothesis does not survive contact with the data.** Of the 16 iv_rank-100 names checked, only DELL (+4.7 vs rv20) and AMBA (VRP −0.03) are anywhere near fair; **every other name is genuinely rich versus realised** (TWLO +45, MTSI/NVMI/FORM/ONTO ≈+26–34, ACMR/NRG/DOCN +13–32). This cohort is earnings-season event premium priced roughly correctly, not a giveaway.

**Genuine cheap vol lives in the defensive iv_rank-0 cohort:**
- **EDU** — the cleanest BUY VOL candidate in the scan, **double-confirmed**: `iv_percentile` **1.33%, z −1.85 (LOW_IV)** *and* `vrp` **−0.179** (largest negative in the set). No catalyst — pure vol mispricing. Liquidity thin under 21dte; structure at 23dte+.
- **GIS** — `vrp` **−0.093** (rv20 confirms, −10.8) = cheap versus its *current* realised move (part of the defensive-rotation repricing, XLP +3.53% 5d), but `iv_percentile` is mid-range (**50.67%, z −0.09**) — not unusual versus its own trailing-IV history. The two lenses disagree; VRP is the richness test that matters. BUY VOL, size down.
- **IRDM** — `vrp` **−0.573**, the most extreme in the scan, but **rejected as an artifact**: every tenor carries 4–10 contracts, the options market is untradable.

**BACKWARDATION calendar candidates: none.** No prior-session `front-end-iv-ratio` was pulled, so "falling" cannot be confirmed for any name; NRG (1.19) and ACMR (1.20) both exceed 1.10 unconfirmed-falling and are excluded by the disqualifier; SOXX (1.09) is borderline but its skew is TAIL_HEDGING — *rising* hedging demand, the opposite of panic resolving.

**Every `iv_percentile_zscore` this run is PROVISIONAL** — `dates_used` **75**, below the 120-date floor. Affects TWLO (98.67), DOCN (100), TLN (100), ACMR (100), SOXL (100), DELL (100).

**No rubric point was claimed by this lane.** No name cleared both catalyst-alignment and a clean VRP-aligned bias at adequate liquidity.

---

## 6. Risk & Correlation

**Macro headline:** stagflation-lite. Core PCE **3.41% YoY** running above core CPI 2.81% and far above target; **10Y 4.61% and rising +23bp/30d**; payrolls soft **+57k**; unemployment 4.2%; curve normal +0.45; USD weakening. Rising long rates against decelerating labour is the worst available mix for long-duration equity — and long-duration equity is exactly what unwound.

**Forward event risk:** Q2 GDP + claims **07-30 (T+1)**; **June Core PCE 07-31 (T+2, Tier-1)**; NFP **08-07 (T+7)**; CPI **08-12 (T+10)**; PPI 08-13. **The PCE print at T+2 fires the event-risk gate on every directional candidate on the board.**

**Breadth cross-check (`fz`, advisory, 0 points):** 182 advancers / 321 decliners, **`pct_green` 36.18%**, avg change −0.89%, median −0.69%, top mover GRMN +16.24%, worst LII −20.97%. **`divergence_flag: false`** — breadth agrees with the red tape and independently corroborates `uw`'s 32.5% bullish-flow reading. No green-tape-with-weak-breadth distribution tell today.

### Correlation clusters — `uw risk portfolio-correlation` against today's candidates

**`AI_semis_power_cluster` — three of five candidates were one bet:**

| Pair | corr | Class |
|---|---|---|
| **INTC / SMH** | **0.900** | cluster (≥0.70) |
| **BE / INTC** | **0.782** | cluster |
| **BE / SMH** | **0.711** | cluster |

INTC is a top-10 SMH constituent (0.90 pairwise = structurally the same semis exposure); **BE is AI-power-adjacent** — its bid is the same AI-capex narrative that is unwinding. Kept member by `raw_score` is **BE (1)**, which is itself **VETO'd**, so cluster exposure nets to zero either way. INTC and SMH each took the mechanical −1 cluster tier. TSLA and TWLO surfaced no pair ≥0.60.

### Gates applied

- **`panic` — FIRES BOOK-WIDE.** QQQ `front-end-iv-ratio` **1.129 > 1.10** while SPY is 1.029 FLAT: panic is concentrated in tech duration, which is where all five candidates live. Per-name corroboration: AMZN 1.689, MSFT 1.544, TWLO **1.376** (hygienic), META 1.345, AMD 1.206.
- **`vrp` — no mechanical firing**, but flagged: the premium-selling signal is stale (realised leg pre-dates the vol expansion), `zerodte_setup` is stand-aside on both indices, and TWLO's `+44` iv−rv gap is partly paid-for protection rather than mispricing.
- **`event_risk` — 4 of 4 evaluable names.** Core PCE 07-31 = T+2. SMH stacks additionally on a constituent-earnings cluster at T+4 → T+7.
- **`sector` — INTC only** (adverse: semis rotating OUT, SMH ETF −$26.58M 5d, 94% put-premium sweeps). TSLA/BE/SMH shorts are *aligned* with the rotation, so no penalty.
- **`fundamentals` — 1 VETO (BE).**
- **`debate` — 5 of 5.**
- **`rubric_regime` — capped half on all** (OUT-OF-REGIME).
- **`regime`, `cluster`** — regime 0 mechanical conflicts; cluster fired on INTC and SMH.

### Fundamentals verdicts (top 5)

- **TSLA — CONFIRM.** Latest quarter (period 2026-06-30) **missed by −36.4%** after three straight beats. Insider MSPR 3mo avg **−45.35** (April −99.9 on **−$96.0M** of real dollars). Revenue +11.75% YoY but **EPS growth −37.66%** = margin compression (gross 18.85% / op 4.22% / net 3.67%). **PE 319x.** News flow uniformly bearish, **zero contradicting catalyst** — the fundamentals reinforce the short rather than fighting it.
- **BE — VETO.** See §7; this is the day's most consequential single finding.
- **TWLO — CONFIRM.** Earnings **2026-08-06** confirmed (T+6). 4-for-4 beat streak, revenue +15.67% YoY, D/E 0.13. Insider MSPR **−75.59** (persistent selling into the print). Fresh BTIG Buy, PT raised to $245.
- **INTC — CONFIRM** mechanically (no 2-of-3 contradiction: beat streak strong, insider **neutral** at −1.8, revenue +7.47%, no imminent earnings) — but still **net-margin negative −19.79%**, ROE −10.76%, and the "4-for-4 beat streak" runs off a near-zero base (+92.9%, **+1971%**, +80.9%, **+2200%**), i.e. estimates were ~0, not that the business is compounding. `fz` drift: market cap **−$51B (−11.0%)** since 07-24.
- **SMH — NA** (sector ETF; no company fundamentals exist). Substantive deliverable is the **stacked constituent-earnings cluster 08-04 → 08-07**: AMD 08-04; ONTO/NVMI/MTSI/NBIS 08-06; ACMR 08-07 — with **NFP landing 08-07 alongside three of those prints.**

**`fz` lane note:** `fz` was available and the breadth aggregate was used, but **every per-name `fz` field came back null this run** (`short_float`, `short_ratio`, `float`, `recom`, `target`) — an upstream gap. Squeeze and analyst axes are **NA by tool failure, not by choice**, so `dp_block_to_float_ratio` is `null` on every accumulation row and **C16/C18 remain untestable for a fourth consecutive audit.** `fz` also emitted the **doubled-first-character synthetic-ticker artifact** (GGRMN→GRMN, CCAKE→CAKE, AABEO→ABEO, IIEX→IEX); the squeeze lane returned only an alphabetical first page rather than a ranked list and was **unusable**.

### Adverse-flow exit candidates

**`conviction_2026-07-28` does not exist** — verified. No group was written 07-25 → 07-28, consistent with the empty-board streak and the corrected LOW+-only write-back rule. Alerts were run against the groups that do exist:

- **INTC** (`conviction_week_2026-W30` carry) — **EXIT CANDIDATE.** Flow bearish, net −$30.2M today, 30d cum **−$966.7M** explicitly BEARISH, sweep-persistence bearish 5/5 ($1.048B). Market cap **−11.0%** since 07-24. Both tripwire legs adverse.
- **MU** (`conviction_2026-07-23` carry) — **off-thesis decay, flag.** Bearish net −$49.8M; DP $10.8B premium across 36,852 trades; today's contrarian **−2** (call-crowd z −2.726 into a continuing −23% 5d decline). Market cap −17.1% since 07-24. The 07-23 watch-only framing is stale.
- **TSLA** (`conviction_2026-07-24` carry) — LARGE_DARK_POOL $59.6M print + OI_SHIFT +202,595, flow bearish. **Consistent with, not adverse to,** today's short-side read. Not an exit flag.
- **AKAM / FSLR** (07-24 carry) — flow bearish with high-IV-rank alerts (99.2 / 91.1), mid-single-digit-$M DP prints, volume ratios 0.91 / 0.45 (no urgency). Advisory decay flags only.

### Hedge sleeve

**The conviction book is empty — there is no net delta to hedge. The flat book IS the position into Friday's PCE.**

1. **Add nothing short-premium anywhere.** Both index books FULLY_NEGATIVE with null ZGL, VIX +24% over 5 days, `size_scalar` 0.0, and a Tier-1 print at T+2. There is no gamma cushion and the short-vol left tail is the unsampled regime.
2. If the desk carries **legacy long-tech exposure outside this book**, the overlay is a **defined-risk QQQ put debit vertical** — e.g. short-dated **660/645**, where 660 is the largest-magnitude negative-GEX strike in the grid and sits 32bp under spot, i.e. the level where a break meets least dealer resistance. Size to legacy net delta only; defined-risk through 07-31. **Prefer this to a VIX call ladder** — VIX at 20.66 after +24% in 5 days has already repriced that convexity.
3. **Do not extend any gamma-map level past tomorrow's session.** PCE can void the EOD prior entirely.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — `raw_score` ≥ 7)

### **No HIGH or MEDIUM tier calls. The section is empty by construction.**

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`. Carried from the most recent `/calibration-audit` (2026-07-25) and its predecessors; **payoff ratio is not computable this cycle** (zero closed calls in the interval, 20 consecutive empty boards):

| Tier | Realised (most recent audits) | Payoff ratio | Note |
|---|---|---|---|
| HIGH | **0.143** (2026-06-27, n=7) | n/a | Tier inversion, 3rd consecutive; the 7 HIGH calls were 4 index-ETF shorts (0-for-4) + 2 faded longs |
| MEDIUM | 0.214 (2026-06-12) | n/a | — |
| LOW | 0.444 (2026-06-12) | n/a | Bands **inverted** on the first post-UPTREND window |
| **DROP (not traded)** | **0.433** (2026-07-18) | n/a | **DROP 43.3% > book 41.1% > sized 38.6%** — the empty-board discipline grades correct |
| `win_rate` [0.55, 0.65) band | **0.179** overall / **0.133** post-freeze (2026-07-25) | n/a | Anti-predictive; floored to `starter` at emission |

The honest reading: **the desk's edge does not currently live in its sized book.** The DROP pile has out-performed the traded book across the last two audits, which is why an empty board is a result rather than a failure.

### Why each candidate died — full audit trail

**TSLA — `raw_score 1`, DROP, `skip`**
`score_components`: **+1** — `sector-rotation-strategist` / `sector-flow-persistence` + `cumulative-premium-flow`: Consumer Cyclical rotating OUT, persistence 1.0 ≥ 0.6, `cum_flow_30d` **−$751.8M** sign-aligned SHORT, magnitude ≫ $50M. Σ = 1. ✓
`dominant_signal_class` sector_rotation · `win_rate` **null / `NA(substrate)`** · `market_excess` null · `cum_flow_90d` **−$1.8M (flat)**
`gate_verdicts`: regime no-op · vrp no-op · **panic −1** · cluster no-op · sector no-op (aligned) · fundamentals **CONFIRM** · **event_risk −1** (PCE T+2) · **debate −1** (bear 0.55 ≥ bull 0.30) · rubric_regime capped-half
**Invalidation (C34):** loses the **$298.32** DP shelf ($152.7M / 511,987 sh / 78 trades), secondary **$297.95** ($60.2M / 5 prints). Note the shelf **equals today's close exactly** — this is live support, not a distant stop.
**The debate's substantive finding:** the bull argued exhaustion — daily net flow decelerating 07-23 **−$247.3M** → −$103.4M → −$71.3M → −$24.0M → **−$11.5M**, into a close $0.50 above the 52-week low. The bear **separated the premium legs and refuted it**: bearish premium fell 76% and bullish premium fell **73%** over the same window — both legs collapsing in lockstep is *total participation cratering*, not a bid returning. **The bearish share never dipped below 50.6% on any of the five sessions.** `price-vs-flow` returns `divergence: false` ("price and flow are aligned"). And no DP tier is net buying: mega `buy_ratio` **0.251**, block 0.432, large 0.485 — the "$152.7M absorbed at $298.32" the bull cited is the *same* flow read from the sell side, i.e. distribution into bids.

**BE — `raw_score 1`, DROP, `watch-only` (VETO)** — **the day's most consequential finding**
`score_components`: **+1** — `sector-rotation-strategist`: Industrials rotating OUT, persistence 0.8, `cum_flow_30d` **−$225.7M** aligned, ≫$50M. Σ = 1. ✓
`gate_verdicts`: **fundamentals VETO → watch-only** · **debate −1** (bear 0.40 ≥ bull 0.30, **BOTH_SIDES_LOW — neither advocate cleared a coin flip**) · remaining gates n/a under VETO
**`multileg-strategist` flagged BE's 2-day tenor pricing 227% IV with "a pending catalyst I could not confirm"** (BE was absent from the cached `earnings_catalyst` payload). **The fundamentals gate resolved it: BE reported Q2 this morning — actual $0.78 vs $0.418 estimate, a +86.6% surprise**, 4-for-4 beat streak (+86.6%, +228.6%, +40.7%, +55.1%), revenue **+56.53% YoY and accelerating**, with a same-day sell-side wall (JPM Overweight, UBS Buy, BTIG Buy $295 PT, one upgrade). A flow-driven short into a name that just beat by 86.6% is the same pattern class as the 2026-07-23 ORCL Pentagon-contract save.

**But the price tape complicates the veto, and both debaters converged on the same nuance.** BE closed **−1.85% at $163.75 and is −24.96% over 5 days.** The bull resolved the paradox with the close series — 226.26 (7/21) → 218.22 → 217.30 → 184.89 → 188.18 → **166.84 (7/28)** → 163.75 (today): **~92% of the week's −27.6% drawdown happened *before* the print landed**, the single worst session was **7/28 at −11.4%, the day before earnings**, and today's beat-day decline **decelerated to −1.85%** while `iv_rank` collapsed **100 → 67.1** (textbook post-catalyst vol crush). So the market did not reject the beat; it had already de-grossed a crowded IV-rank-100, beta-3.95 name into an FOMC day, and the beat **stopped the bleeding.**

**The bear's rebuttal is the strongest single piece of evidence produced anywhere in today's fleet.** After the beat was public, after the sell-side wall, after the IV crush: the **Aug-21 130P went from 1,535 to 26,112 OI — a +24,577 print, +1601% in one session**, at an average fill of $12.72 = **~$31.3M of fresh premium on a 20%-OTM, 23-day put**, dated *past* Friday's PCE. It cannot be a roll — prior OI was 1,535. The next-largest build was the 230C at +16,921 (~$16.95M), so **puts out-built calls in new premium ~1.84:1 on the beat day.** And **6 of the 7 largest OI decreases are calls closing** (Sep-18 370C −23,169; Sep-18 330C −4,975; Aug-21 210C −3,556; Aug-7 230C −654; Aug-21 300C −634; Aug-7 205C −398) — a coherent rotation: longs exiting upside calls into the pop while size opens fresh downside. Top-20 sweep tape: put buying $27.99M vs put selling $10.16M, call buying $18.23M vs call *selling* $23.62M ≈ **$23.2M net bearish tilt.** On beat quality: a +86.6% surprise is a **$0.362/share absolute beat** on a **0.25% net margin** and 2.67% op margin with **D/E 3.73** — at that thinness a single one-time item swings the surprise percentage without saying anything about durability, and the op-to-net gap is being eaten by debt service on a **beta-3.95** name into a rising 10Y.
**Net:** the VETO correctly blocks the short, and the long is not ready to size either. **Watch-only is the right answer, and the reasoning matters more than the verdict.**

**TWLO — `raw_score 1`, DROP, `skip`** — **and a probable instrumentation defect**
`score_components`: **+1** — `earnings-scout`: SELL VOL, earnings 2026-08-06, `shape` KINKED on `base_shape` CONTANGO, kink at 2026-08-07, prominence 20.6%. Σ = 1. ✓ (`vol-surface-scout` reached the same CALENDAR structure but **explicitly declined its rubric point**, so "two agents agree" overstates the consensus.)
`dominant_signal_class` earnings_vol · `implied_move` **4.08%** · `win_rate` **null / `NA(substrate)`**
`gate_verdicts`: **panic −1** (own hygienic ratio **1.376** > 1.10) · **event_risk −1** (PCE T+2 sits under the short front leg and is *not* the played event) · **debate −1 (polarity-inverted)** · vrp no-op-on-sign but flagged stale · rubric_regime capped-half
**⚠ Polarity note:** the thesis is SELL VOL, so `bull-researcher` was assigned the *kill-the-trade* case and returned **0.72**, while `bear-researcher` argued *for* selling vol and returned **0.25**. The **anti-thesis side won decisively** — the literal `bear ≥ bull` test does not fire only because polarity is reversed. Both residuals are recorded verbatim in the envelope with this note so the audit can re-derive it.
**The bull's lead argument is a register fact, not an opinion:** `earnings_vol` is a **5-consecutive-audit, Benjamini-Hochberg-surviving over-claimer — claimed ~0.88, realised 0.35–0.38, market excess −31.7pp** (one of two confirmed vol BH-lies alongside `high_iv_rank`). It also corrected the front-end ratio: the **1.491** figure used an **11-contract untradable tenor**; re-run through hygienic liquid tenors (9dte vs 23dte, 44 and 108 contracts) it is **1.376** — still breaching the >1.10 disqualifier.
**The bear then found something neither side expected, and it argues against its own case:** TWLO's last four post-earnings close-to-close reactions were **−19.38%, +19.51%, −8.75%, +23.83% — mean absolute move ≈17.9%.** Against that record, a quoted `implied_move_perc` of **4.08%** is not a demanding bar; it is roughly **4–5× too low**. Separately, the front tenor's own priced IV (124.7% at 9 DTE) implies a **~19.6% 1-SD move**, which lines up almost exactly with the realised history rather than with 4.08%. **Two consequences.** First, the surface is pricing TWLO's jump about right and the "+44 iv−rv gap" is a **measurement artifact** — jump-inclusive 30d IV compared against jump-free 20d trailing RV, exactly the comparison that manufactures the overclaim the register keeps catching. Second, and more important for the machinery: **`uw insights earnings-play`'s `implied_move_perc` may be systematically understating jump risk for high-beta names with a recent gap history.** That is a register candidate, not a one-off — and it also means the C43 `implied_move` field, which exists so audits can resolve vol on a true IV-vs-RV basis, may be carrying a biased number. Bear residual **0.25**: it sided closer to the bull.

**INTC — `raw_score −1` (+2 −3), DROP, `skip`** — failed the confluence gate; the day's most substantive near-miss
`score_components`: **+2** — `multileg-strategist` / `hot-chains multileg` + `oi biggest-increases`: same-strike call diagonal + Jun-2027 risk-reversal, all five legs OI-**increases** (Sep-18 100C +27,604 bid-side $25.06M credit; Mar-27 100C +5,053 @89% ask; Jun-27 100C +4,356 @87.5% ask; Jun-27 80P +4,517 sold; Jun-27 85P +2,511 bought), net ~$3.5M **credit** on ~$64M gross, term-structure-anchored to a clean no-kink BACKWARDATION with thick tenors. **−3** — `flow_conflict`: `cum_flow_30d` **−$966.7M** with an explicit BEARISH label, **7.1× the union-median $135.4M**. Σ = −1. ✓
`gate_verdicts`: **panic −1** · **cluster −1** (INTC/SMH 0.900) · **sector −1** (semis rotating OUT) · **event_risk −1** · **debate −1** (bear **0.65** ≥ bull 0.30) · fundamentals CONFIRM · rubric_regime capped-half
**Invalidation (C34):** DP level **$81.88** ($1.53B of $3.05B day premium, 91 trades) — **but caveat it**: the bear flagged this as a reference-price/closing-cross pattern (a $1.02B print at 20:08:23Z), so treat it as a reference level, not proven institutional defense. The real thesis-level invalidation is the **−$966.7M flow itself**; the long is untouchable until that sign flips.
**The bear dismantled both of the bull's "independent confirmations."** (1) **The DP accumulation is 10 prints on top of a sell-dominant tape:** mega tier `buy_ratio` 0.801 on $1.454B across just **10 trades** (avg $145.4M each), while the **block tier — 116 trades, $1–10M, still institutional — reads `buy_ratio` 0.363, i.e. 63.7% net SELL.** And **$1.53B of the day's $3.05B printed at exactly $81.88 (spot) across 91 trades** = a reference-price cross pattern, not organic buying at varying levels. (2) **The DP buying may *be* the dealer hedge of this very structure** — selling 27,604 calls at ~0.30 delta ≈ 828k share-equivalents ≈ $67.8M of long-delta hedging, which mechanically produces the buying cited as independent confirmation. The bull conceded this risk; the tier split turns the concession into a data-backed likelihood. (3) **The +229,371 `net_oi_change` is whole-chain, not structure-specific:** of the top-10 contracts driving 43% of it, **only 2 belong to the structure** (32,657 contracts = **14.2%** of the day's total); three others are **0DTE/2DTE expiry churn** (0DTE 90C +11,432, 0DTE 87C +6,091, 2DTE 90P +5,793) on the largest expiry day of the year. (4) `consecutive_build_days` is actually **76, not 10** — the same zero-discrimination artifact the C47 register flags. (5) The structure is short calls at **three** tenors plus short puts at **two** strikes within 2.3–3.8% of spot — **a range-bound premium-harvest, not a directional long**, which is precisely what `conviction-matrix` labels COVERED_CALL and what LEAP-radar treated as a Gate-8 hard fail.

**SMH — `raw_score −3`, DROP, `skip` / context**
`score_components`: **−3** — `flow_conflict`: `cum_flow_30d` **+$208.27M NET BULLISH** (bullish $4.849B − bearish $4.641B, aggressor-classified), 1.54× the union median, opposing the SHORT; 90d also net positive (+$14.98M). Σ = −3. ✓ **Zero positive lines**: the ETF flow tape is advisory (0 points) and `dealer-positioning-strategist` issued NEUTRAL with no mechanized DEX flip.
**This was a live correction.** The Phase 1 union carried only the **5-day** ETF tape (−$26.58M bearish); the quant re-pulled the full window and found the 30-day aggressor-classified flow is **net bullish**. Someone has been dip-buying semi-ETF options while the complex falls.
`gate_verdicts`: **panic −1** · **cluster −1** (INTC/SMH 0.900) · **event_risk −1 stacked** (PCE T+2 *plus* the constituent cluster T+4→T+7) · **debate −1** (bear 0.65 ≥ bull 0.32) · sector no-op (aligned) · fundamentals NA · rubric_regime capped-half
**Expression constraint (independent of score):** this is an **index/sector-ETF SHORT**, and the 2026-06-27 audit **REFUTED** the "express bearish index-relative" recommendation — the sized index-ETF short book went **0-for-4** at the top of that book while single-name shorts won, narrowing the rule to **no short alpha-sizing anywhere.** Watch-only regardless of score.
**The debate produced the cleanest analytical result of the day — it reconciled two facts that looked contradictory.** How can sweeps be **94% put premium** while the full-tape aggressor split is **net bullish +$34.66M** (gross put $374.0M vs call $134.3M, PCR 1.79)? The bear resolved it at strike level: ~**$60M of put-WRITING** (590P sold at bid $26.2M; 550P sold at bid $17.16M; 500P Dec sold at bid $9.48M; 520P Jan-27 sold at bid $7.23M) against only ~$25–30M of put-buying (550P bought $13.29M; 530P bought $11.72M across 198 small prints). **Both measurements are correct — 94% is a gross-premium/PCR read, net-bullish is an aggressor read that nets put-writing against gross put volume.** The substantive conclusion: **the crowd is put-*writing* into a 96 IV-rank panic at a fresh multi-day low — a vol-mean-reversion/income bet, not a directional bottom call.** And it has a bearish feedback mechanism the bull did not trace: customers sell puts → dealers buy them and run short delta → as SMH grinds lower, dealers hedging that long-put book **sell more stock**, which plausibly *feeds* the monotonic six-session DEX deterioration (−4.27B → −22.52B) rather than contradicting it.
**The bear also killed the bull's "$513.72 buyer paying up" print.** The 245,201-share / $125.97M block at 20:03:34Z printed at $513.72 against an NBBO mid of $503.35 (+$10.37) — **but the same ~$513.7–513.8 price also printed at 18:01:32Z against a mid of $517.10, i.e. $3.31 BELOW mid.** A static reported price against a quote that moved $14 across the session is the fingerprint of a **benchmark/VWAP-referenced block**, not a real-time aggressive cross. Worse: two further prints (20:42:33Z, $67.4M; 21:58:22Z, $41.3M) are tagged at **exactly $504.22 — the day's official closing print, to the cent** — after the bell. Textbook closing-cross/settlement contamination.

### Conviction-scoring rubric (Step 4) — embedded verbatim for audit

> **RUBRIC FROZEN — version `2026-06-12` (audit P0.1).** Weights, tier cuts and gate membership are frozen. No line may be promoted, demoted, added or re-binned until a change clears a **pre-registered, cross-regime, Benjamini-Hochberg-surviving** bar. Audits **grade** this rubric; they do not retune it.

```
Daily conviction score = Σ:
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna-squeeze setup in trade direction
      — must be a verified SIGN CHANGE, not a level: sign(net_dex) on the latest session opposite to ≥3
      consecutive prior sessions, |net_dex| on the flip day ≥ 0.25× the trailing-10-session median.
      Computed by scripts/dex_flip.py, never by hand. Vanna disjunct requires a dated falling-VIX source.
      [DEMOTED +3→+1 and MECHANIZED 2026-06-12 P0.4]
  +3  3+ aligned signals in accumulation-hunter (DP + OI + oi smart-positioning, block-stratified
      institutional-tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms
      (sign aligned AND |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1.
  +1  multi-day OI build (historical oi-trend BUILDING, --days ≥ 5)
  +1  insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: award ONLY when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +1  cumulative-premium-flow net directional accretion in trade direction (30d) — INTENT-SCREENED:
      award only when (a) no C28 distribution_flag on the name, AND (b) on dividend payers in an ex-div
      window the accreting prints are NOT deep-ITM sub-parity calls. [DEMOTED +3→+1 2026-06-06 P1.4]
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector — CONDITIONAL:
      award only when (a) sector persistence_score ≥ 0.6 AND (b) cum_premium_flow_30d direction aligned
      with thesis AND (c) |cum_flow_30d| ≥ $50M. Default 0.
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising pc-ratio-zscore (VRP positive)
      — MECHANISM: an INFORMED-FLOW CONTINUATION penalty, not "the crowd is wrong, fade it."
  -3  flow_conflict — applied mechanically when cumulative-premium-flow 30d direction is clearly opposite
      dominant_signal_class (signed-sum sign flip + magnitude > union-median |cum_flow_30d|, or explicit
      OPPOSITE label). Mutually exclusive with flow_conflict_lite.
  -1  flow_conflict_lite — 30d cum_premium_flow read is MIXED. Mutually exclusive with flow_conflict.
  # REMOVED: insights signal-confluence ≥4 (+2, removed 2026-06-12 P0.2 — server-side re-count of
  #          already-scored quantities); hot-chains sweep-persistence top-5 (+1, removed 2026-05-23 P0.3,
  #          −22pp two consecutive audits); gamma-flip-tracker 0DTE breakout (+2, removed 2026-05-09).
  # TIER GATES (risk-monitor, Step 2d) — contribute 0 to raw_score, never in score_components:
  -1  [TIER GATE] correlation cluster (pairwise corr ≥ 0.70) — −1 TIER
  -3  [TIER GATE] market-regime conflicts with trade direction — −1 TIER
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | **HIGH** | full (subject to Step 3a load-bearing gate + Step 5 win-rate gate) |
| 7–8 | **MEDIUM** | half (subject to Step 5 win-rate gate) |
| 3–6 | **LOW** | starter / watch-only |
| ≤ 2 | **drop** | filtered by the quant's drop floor |

**Tier-cut status (2026-06-12):** the ≥9 HIGH cut **failed its scheduled re-confirmation** — bands inverted on the first post-UPTREND window (HIGH 0.222 / MED 0.214 / LOW 0.444). The cuts are retained under the freeze but carry **no validated ranking claim**, and the P0.6 out-of-regime guard caps all sizing at half in the interim.

---

## 8. Watch-only — single signal, no confluence

Listed for journaling, **not for trade entry today.**

| Ticker | Flagged by | Signal | Why it failed the gate |
|---|---|---|---|
| **INTC** | `multileg-strategist` (+2 LONG, MED-HIGH, "structure of the day") | 5-leg OI-confirmed collar-financed synthetic long | **Exactly one positive flag.** `sweep-tracker` bearish 5/5, LEAP-radar disqualified on Gates 4+8. −3 `flow_conflict` on **−$966.7M** takes it to −1 regardless. See §7. |
| **WOLF** | `multileg-strategist` (+2 SHORT, LOW-MED) | Dec-18 put ratio ladder: BUY 22.5P +4,985 @95% ask; SELL 20P +4,897; BUY 2× 15P +9,992 @92% ask. Net **$3.63M debit**, breakeven ~$12.6 = requires a further **−37%** by 12-18; max payoff 4.5:1. Sits on the flat far end of a steeply backwardated curve (2d 198% → 541d 113%), declining front-end event premium and buying the cheapest vol on the surface. **Flow conflict resolved in favour of bearish**: WOLF shows +$9.8M on the *bullish* screener, but OI shows calls being **written** across the curve (260918C40 −1,179 closing; 260918C50 +194 at 0 ask/500 bid) while puts are bought — the "bullish net premium" is written-call premium miscounted. | **One agent.** $20 distressed name, ~130% IV, −8.32% today / **−31.47% 5d**, in a complex already down 14–16% — crowded short. The 142d tenor carries only **57 contracts**. `multileg` explicitly said do not carry HIGH. |
| **AMZN** | `sector-rotation-strategist` (+1 short) | Clears all 3 conditional legs (persistence 1.0, `cum_flow_30d` −$248.7M, ≫$50M) | **One positive flag.** `dealer-positioning` was explicitly NEUTRAL; `earnings-scout` SKIP. **Earnings 2026-07-30 POSTMARKET — one day out** — which resolves dealer-positioning's "unexplained" 1.689 front-end panic. Two events stacked and inseparable: the only near tenor (2dte, 07-31) prices both the earnings reaction *and* PCE. `implied_move` 5.86%. |
| **TEVA / CVE / SNN** | `accumulation-hunter` | HALVED_1 accumulation (see §3a) | Single-agent; all three fail the $50M conjunction (CVE's flow is additionally **wrong-signed**; SNN's OI leg is a **straddle**). |
| **IRM / VST** | `accumulation-hunter` | Credible bearish co-flags: Tier-1 `OPENING_PUT_PRIME` + DP distribution (IRM block `buy_ratio` **0.0** on $8.35M/3 trades, clean timestamps; VST block 0.276 on $30.5M/14 trades) | Single-agent advisory, 0 points. |
| **DOCN** | `vol-surface-scout` (CALENDAR, no point claimed) | KINKED/CONTANGO, kink 08-07 at 8.8% prominence on 1,966 liquid contracts, `implied_move` 6.53%, earnings 08-04 | `earnings-scout` explicitly **SKIP — the trap**: `term-skew` returned *"insufficient call/put coverage at target DTE"*, so back-month tail pricing is **literally unmeasurable**; and DOCN is on the iv_rank-100 carnage list at **−25.18% 5d**. Selling premium into a falling knife with an unreadable tail is a coin flip. |
| **EDU / GIS** | `vol-surface-scout` (BUY VOL) | EDU double-confirmed cheap (`iv_percentile` 1.33%, z −1.85; `vrp` −0.179). GIS `vrp` −0.093 but mid-range percentile — lenses disagree | Single-agent; both `NO_NEAR_TENOR` (thin under 21dte, structures must sit at 23dte+). |
| **GOOGL** | `dealer-positioning-strategist` (advisory LONG) | DEX flipped POS 07-28 + GEX recovering 3 sessions (50.8→70.6→90.4M) + call-heavy vanna + flat front end (1.039) | Not a scored flip (07-28, not latest session), not a vanna squeeze (call-heavy fails the frozen definition), **whipsaw warning (4 sign changes)**. Sector conditional fails (`cum_flow_30d` +$29.1M < $50M). `multileg` **rejected** its diagonal as **hollow** (55,626 volume vs 299 OI-substrate, OI change −82). |
| **MU** | `contrarian-scanner` (**−2 penalty**) | BULLISH_EXTREME z −2.726 | A **penalty**, not a positive flag. See §3b. |
| **NBIS / SNDK** | `sweep-tracker` | Directionally self-contradictory across agents | NBIS: sweeps bullish/clean but a Tier-1 `OPENING_PUT_PRIME` 120P contradicts, and `earnings-scout` shows the front-end elevation is **purely macro/PCE** (2dte IV 2.2287 ≫ 9dte 1.6533 while earnings is 08-06, not captured by the 2dte bucket) — the 120P is PCE-timed hedging. SNDK: bearish 5/5 persistence vs the largest bullish print in the book, on a −36.5% week. |
| **SMH** | `sector-rotation` + `dealer-positioning` | Passed the confluence gate but scored **−3** | See §7 — and the index-ETF-short expression constraint applies independently of score. |

### Fleet defects and artifacts recorded this run

Twenty items. The ones that changed a conclusion today are marked **★**.

1. **★ `uw historical pc-ratio-zscore` has NO `--date` flag** on this build (verified via `--help`). The rubric's −2 line **requires a multi-date z trajectory** and the tool cannot produce one — so "rising" is **UNESTABLISHED for every name**, fleet-wide. Independently reconfirms a defect registered 2026-07-27.
2. **★ `uw insights analyst-vs-flow` is degraded** — returns only the `options_flow` leg on every symbol tested (NVDA used as a control), with **no analyst-ratings leg at all.** `earnings-scout`'s designated highest-EV signal is currently **unmeasurable.**
3. **★ `uw hot-chains multileg` is hollow today.** Top-60 is dominated by equal-size, high-`multileg_ratio` (>0.95) leg-pairs producing **essentially zero OI**. Cross-checked against the independent OI substrate, the two feeds are irreconcilable by **100–500×**: GOOGL 260918C410 55,626 vs **299** (OI −82); MSTR 260821C95 44,622 vs **172**; KRE 260821P74.5 85,509 vs **absent**; WOLF 260918P22.5 40,006 vs **111**; GLD 260918C400 29,714 vs **767**. The *only* leg where both substrates agree in magnitude (IWM 260821P279: 90,484 vs 50,132, OI **+29,397**) is the one real build of the day. **Require OI confirmation before scoring any multileg structure.**
4. **`uw oi position-rolls` under-reports** — found 7 rolls market-wide and **missed the IWM hedge roll entirely** because that roll mixes same-expiry and cross-expiry legs while the tool is near-vs-far single-day only. Absence from `position-rolls` is not proof of a fresh build.
5. **★ Raw `iv-term-structure` labels are unusable** — three agents independently: 17/19 (89%), 12/12 (100%), and 22-name splits, with **16 of 19** flipping after hygiene. Exceeds the 07-24 finding.
6. **★ `iv_outliers` is 19/20 expiry-day noise**; the one non-today row fails C12. Zero genuine outliers survive.
7. **`uw screener volume-vs-average` is noise** — NWS 523× on 2,686 contracts, LQDH 300× on **20** contracts, GWX 30× on **1** contract. Only CHEF (35.7×, $58.5M ADV) is real; FCF (461×) fails C12 at $15.9M ADV.
8. **★ `sector-flow-persistence` saturates** — `persistence_score` 1.0 on 8 of 11 sectors, so the ≥0.6 gate discriminates nothing.
9. **★ `sector-flow-persistence` is sign-agnostic (turnover, not accumulation)** — caught twice: Technology's +$223M gross vs ~+$30M aggressor-classified; Energy's 5-day "inflow" vs **XLE −$17.0M BEARISH**.
10. **★ Closing-cross contamination is market-wide** — `dark-pool largest` top prints are nearly all 20:00–20:41Z at essentially-mid prices (AAPL 20:08:23Z **$1.10B**, INTC 20:08:23Z **$1.02B**, META $663M, QQQ $661M, SPY $729M). **No mega-cap DP print is a trustworthy accumulation signal today.**
11. **★ Synchronized twin/triplet prints — three instances.** MMM: 20:04:38Z 18,938-share $3,370,017.10 print appears **twice**. BE: three trades at 11:54:20Z, ~$50M/$50M/$45M, same $166.84, `trade_vs_mid` −15.095. SNDK: 2027-06-17 $1000 matched call+put, same size (1,700), same timestamp.
12. **Matched/crossed trades read as mega accumulation** — EA: 50,000 buy / 50,000 sell at 13:44:20–13:44:52Z, `buy_ratio` exactly 0.5.
13. **Broken/stale NBBO quotes** — SNN $3.25M print with bid $25.02 / ask $49.98; BE `trade_vs_mid` −15.095; SOXL sweeps mixing deep-OTM puts struck at 240 against a ~$92 spot.
14. **Un-split-adjusted strike grid recurs** — DRAM 261016C122 / 261120C122 (+18,455 @99.8% ask) price a **122 strike against a $44.74 spot** at $0.30/$0.67. Same class as the 07-24 LULU 261218 P300 artifact.
15. **Parity/box artifacts** — INTC 260731 C66/C67, **29,512 contracts each at IV 202%/195%**, deep-ITM 2DTE at implausible extrinsic (same class as 07-24's INTC C80/C79). HYG 261120 C81: 45,000 lots at IV **1.6%**, OI ~0.
16. **`fz` doubled-first-character synthetic tickers** (GGRMN→GRMN, CCAKE→CAKE, AABEO→ABEO, IIEX→IEX) **plus** a squeeze lane that returned only an alphabetical first page — lane unusable. **And every per-name `fz` field is null this run** (short_float/short_ratio/float/recom/target), so **C16 and C18 remain untestable for a fourth consecutive audit.**
17. **★ NEW — scratchpad filename collision across concurrent Phase 1 agents.** `earnings-scout` wrote hygiene output to a generic `hygiene_out.json` and it was **clobbered mid-run** by a concurrently-running agent sharing the session scratchpad. It re-ran under a unique name and cross-checked, so today's analysis is on verified data — but **generic scratchpad filenames collide.** Recommend mandatory per-agent filename prefixes in every Phase 1 agent brief.
18. **Every `iv_percentile_zscore` is PROVISIONAL** — `dates_used` 75 < the 120 floor (TWLO, DOCN, TLN, ACMR, SOXL, DELL).
19. **Realised-vol sources disagree materially** — SOXL iv−rv +8.8 (vrp 30d) vs +30.3 (rv20); AMBA `vrp` −0.0294 FAIR vs rv20-based +28.3. Do not trust either alone.
20. **★ NEW — `signal-backtest` class-enum gap.** The CLI enum is exactly `bullish_flow | bearish_flow | high_iv_rank | volume_spike | dark_pool_accumulation`. **None of today's dominant classes (`sector_rotation`, `earnings_vol`, `multileg_directional`) exists in the tool**, so the P0.3 clean-query protocol **cannot complete** and every `win_rate` is an honest `NA(substrate)`. Worth registering so audits stop expecting a quote for classes the tool structurally cannot serve.
21. **★ NEW — `uw insights earnings-play`'s `implied_move_perc` may systematically understate jump risk.** TWLO's last four post-earnings reactions were −19.38%, +19.51%, −8.75%, +23.83% (**mean |move| 17.9%**) against a quoted **4.08%**; the front tenor's own 124.7% IV implies ~19.6%, matching the history. Register candidate — and it means the C43 `implied_move` field may be carrying a biased number into the audit trail.
22. **★ `consecutive_build_days` is a zero-discrimination artifact** — INTC returned **76**, not the 10 initially cited. Consistent with the C47 finding that `+1 oi-trend BUILDING` fired 16-of-16.

---

## Watchlist write-back — intentionally SKIPPED

`written: false` · `group: null` · `tickers: []`

**Reason:** the post-gate book is empty — four `skip` and one VETO watch-only, **zero LOW-or-better names.** Per the corrected 2026-07-23 rule, **only LOW+ names are ever written**; writing the raw top-5 (all DROP, one VETO) would poison tomorrow's correlation and adverse-flow loop. **No `conviction_2026-07-29` group was created.**

## Deep-dive hand-off

**Skipped** — no HIGH-tier names post-gate. Step 8.5 does not apply on a no-edge day.

---

*Rubric version `2026-06-12` (frozen). Schema `1.3`. 11 Phase 1 agents (not OPEX week — third Friday was 07-17). C12 liquidity floor pinned to `--as-of 2026-07-29`: 108 pass, 11 fail. Step 0 cache: 22 market-wide payloads fetched once.*
