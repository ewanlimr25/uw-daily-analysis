# Daily Market Analysis — 2026-07-27

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / CHOPPY. SPY 739.09 (+0.02%) below both 20SMA (746.66) and 50SMA (745.0), −2.8% from the 90d high. VIX 18.67. **SPY and QQQ are both FULLY_NEGATIVE gamma** (total GEX −$1.59B / −$0.90B) with no computable zero-gamma level on either. Breadth splits hard: `uw` flow breadth is **35.2% bullish** while finviz price breadth is **65.2% green** (328 adv / 175 dec). Sector lean: semis/hardware led down, financials/staples/discretionary led up.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** SPY — FULLY_NEGATIVE · ZGL null (unreliable) · no call wall inside 2.9% (first positive strike 748, cluster 760) · put wall 735 · **short-gamma: debit verticals / long straddles, do NOT sell iron flies**. QQQ — FULLY_NEGATIVE · ZGL null · positive prints negligible everywhere · put wall 680 (ATM) · **short-gamma, and negative VRP independently argues against selling premium**. Advisory, see §2.
- **Top swing build:** **NONE.** Zero names cleared the conviction floor — an **all-DROP board**, the first since the W30 weekly (2026-07-24) sized INTC at `starter`. Stricter than the 07-24 daily, which carried three LOW watch-only names (TSLA, AKAM, FSLR).
- **Top LEAP candidate:** **NONE.** No name in the 61-ticker C12 funnel cleared 6-of-9 LEAP gates.
- **Biggest risk:** Not a position — a **calendar**. FOMC decision + Warsh presser **Wed 7/29**, Core PCE + Q2 GDP **Thu 7/30**. QQQ front-end IV ratio **1.221** (>1.10 panic threshold) is pricing it. The only correlation cluster that mattered (`semis_infra`: SMH/AMD/INTC/MU/SNDK, pairwise 0.76–0.92) would have collapsed a semis-short book into **one** position had anything sized.

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity."** Trend **CHOPPY**. Tool guidance verbatim: *"Half position sizes. Favor defined-risk strategies. Iron condors in range."* Note §2 disagrees with the iron-condor half of that on gamma grounds.

The breadth picture is the day's central tension and it is **not** a distribution tell — it is the inverse. `uw` market-breadth reads 2,208 bullish vs 4,071 bearish flow tickers (**35.2% bullish**), while finviz price breadth reads **65.2% green** with median change +0.82%. Bearish-tilted *flow* against broadly green *price* is hedging and put-buying into a rotation, not selling across the tape.

**Per-index gamma (EOD 0–45 DTE book):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 738.91 | `null` (unreliable) | −$1,589,298,789 | FULLY_NEGATIVE | none reliable; first +strike 748, cluster 760 | 735 (−$153.4M) |
| QQQ | 681.85 | `null` (unreliable) | −$904,798,396 | FULLY_NEGATIVE | none (all positive prints <$5.1M) | 680 (−$151.6M, ~ATM) |
| IWM | 292.91 | grid-corrupt (see caveat) | −$0.37B to −$1.3B across window | negative throughout | — | — |

⚠ **ZGL-grid corruption re-confirmed** on SPY (ZGL 360.62 vs spot 750.13), QQQ (352.82 vs 706.7), IWM (~150–196 vs ~293–296) and INTC (24.3 vs 91.67) — each roughly **half** spot. Discard those regime labels; the `total_gex` sign is the reliable read.

**`uw options-flow dte-volume-share`:** 0DTE **40.6%** · weeklies 27.0% · monthlies 16.5% · LEAPs 2.8% → `regime_hint: RETAIL_DRIVEN`. Only 19.3% of the tape is monthly-or-longer institutional positioning. Every multi-week conviction call sourced from today's flow is downgraded on this alone.

**`uw historical vrp`:** SPY IV30 15.71% vs realised 12.66% → **VRP +0.0305, FAIR**. QQQ IV30 26.02% vs realised 27.69% → **VRP −0.0167, NEGATIVE**. Realised is running hotter than implied on the Nasdaq complex — vol *buying* is the cheaper side there, which inverts the usual high-IV-rank instinct.

**Macro backdrop** (`scripts/fred_macro.py`): curve **normal** +34bp (10Y 4.69 / 2Y 4.33) · core CPI **2.81%** YoY · core PCE **3.41%** YoY · unemployment 4.2% · payrolls **+57k** · 10Y **rising**, +28bp over 30 days · USD **weakening** · fed funds 3.63%, SOFR 3.64. Core PCE running a full 60bp above core CPI and far above target while the long end backs up 28bp into a Fed meeting is a **sticky-inflation, rising-real-rate** setup — structurally hostile to long-duration growth multiples, and consistent with what the semis complex did today.

**Forward `event_risk` (Tier-1, next ~10 sessions):**

| Date | Event | Impact |
|---|---|---|
| 2026-07-28 (T+1) | FOMC two-day meeting begins; CB Consumer Confidence, Case-Shiller | HIGH / MEDIUM |
| **2026-07-29 (T+2)** | **FOMC rate decision 2:00pm ET + Chair Warsh press conference 2:30pm ET** | **HIGH** |
| **2026-07-30 (T+3)** | **Core PCE (June) + Q2 GDP advance + initial claims, 8:30am ET** | **HIGH** |
| 2026-07-31 (T+4) | Employment Cost Index Q2, Chicago PMI, Michigan final | MEDIUM |
| 2026-08-12 | July CPI | HIGH |
| 2026-08-19 | FOMC minutes | MEDIUM |

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — open interest that persists overnight — read forward as the *prior* for the next open. It is prose-only, contributes **0 points** to the conviction rubric, and makes **no backtested predictive claim**. Predictive validation of these levels lives in `/weekly-analysis`'s rolling §2 backtest, not here. Scope is SPY and QQQ only.

**SPY** — spot 738.91 · ZGL `null`, `zgl_reliable: false` · **FULLY_NEGATIVE**, total GEX **−$1.589B**. There is no reliable call wall: the book is negative almost everywhere, the first positive strike is 748 (+$44.9M, 1.2% up) and the largest positive cluster is 760 (+$56.7M, 2.9% up). Put wall 735 (−$153.4M, 0.5% down) — but the single largest negative-GEX concentration sits **at-the-money at 739/740 (−$381.7M combined)**, which is a gravity trough, not support. Top strikes by |GEX|: 740 (−$266.3M), 735 (−$153.4M), 730 (−$149.2M).
**Structure bias:** short-gamma → dealer hedging *amplifies* moves in both directions. Debit verticals or directional 0DTE; long straddle if spot sits on the trough with walls wide. **Do not run an iron fly or condor — there is no gamma cushion to sell against.**

**QQQ** — spot 681.85 · ZGL `null`, `zgl_reliable: false` · **FULLY_NEGATIVE**, total GEX **−$0.905B**. No call wall of any substance (every positive print <$5.1M). Put wall 680 (−$151.6M, essentially ATM); secondary troughs 690 (−$71.9M) and 700 (−$55.6M) are round-number OI concentration, not support. Top strikes: 680, 690, 700.
**Structure bias:** short-gamma **plus** negative VRP (realised 27.69% > implied 26.02%) — two independent arguments against selling premium here. Long straddle/strangle or debit verticals.

**Regime freshness:** both indices **HELD** FULLY_NEGATIVE across 7/23, 7/24 and 7/27 — three straight sessions, not a fresh overnight flip. SPY has not touched POSITIVE since 7/16.

**Mandatory caveats:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and re-computes the ZGL and walls. The 7/28 expiry alone carries ~$1.1B notional per the expiry heatmap.
- **ZGL is `null` on both indices** — the regime is already saturated negative, so the read leans entirely on the `total_gex` sign and per-strike shape. Marked `zgl_reliable: false`.
- **Gap risk voids the prior, and this week it is elevated, not theoretical.** FOMC day-1 is tomorrow; the decision is Wednesday; PCE and GDP are Thursday. A fully-negative book plus a binary macro catalyst is the worst available combination for premium selling.
- **Tooling limit:** `uw` cannot isolate the D+1 expiry (`gex --dte-max 1` errors). This is the standing 0–45 DTE book as proxy.
- **ETF book**, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py`)

The GEX walls above are a **map, not a pin** — wall-as-magnet backtested NO_GO, as did every directional 0DTE signal. What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, and not a guaranteed edge — the validation sample contains no vol shock, so the short-vol left tail is **unsampled**.

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` / VIX | HIGH / 18.67 | HIGH / 18.67 |
| implied move | 0.97% | 1.68% |
| `expected_range_pct` | 1.2% | 2.0% |
| `size_scalar` | 1.5 | 0.75 |
| suggested structure | wider iron condor, wings ≈ ±1.2% | wider iron condor, wings ≈ ±2.0% |
| `stand_aside_reason` | null | null |
| `caution` | null | **Front-end backwardation (0DTE IV 1.43× VIX) — event/gap risk; half size** |
| backtest (n=60) win rate | 91.7% | 86.7% |
| **mean PnL gross** | **+0.258%** | **+0.381%** |
| **mean PnL NET** (after 0.10% assumed round-trip) | **+0.158%** | **+0.281%** |
| worst day | −1.40% | −2.453% |
| `pnl_basis` | \% of underlying spot notional, **GROSS** | same |

Rolling `backtest.verdict` for both: **GO_PREMIUM_SELL_INTRADAY**. Entry rule: enter at/after the open once the overnight gap resolves; if it gaps beyond the wings, **stand aside**; hold to the close; **never carry overnight** (overnight entry backtested negative — SPY +0.046%, QQQ **−0.081%**). Direction: none, this is delta-neutral — do not add a tilt.

> ⚠ **Orchestrator override — the SPY 1.5× size scalar is NOT actionable at face value this week.** That scalar is computed from VIX level alone and is **blind to the FOMC/PCE calendar**. Tomorrow is FOMC day-1, Wednesday is the decision, Thursday is PCE and GDP. Two independent signals say the same thing: both indices are FULLY_NEGATIVE gamma (no cushion to sell against) and QQQ's VRP is negative. **The honest read is that the model wants to sell premium and the calendar says don't.** Take the calendar.
>
> **SPY ≈ SPX** (validated identical — trade either). **QQQ is weaker** (Nasdaq index book unavailable) — lower confidence, and it is the one carrying the backwardation caution. **Promotion bar:** this lane stays advisory / 0 points **permanently** until BOTH a vol-shock day enters the sample AND **net** expectancy clears a tail-aware bar. Win-rate is explicitly not the promotion metric for a negatively-skewed short-vol strategy.

---

## 2b. Swing Dealer Positioning (1–4 weeks)

The `dex_flip.py` mechanized test ran on the six names whose 5-session preview showed a sign change. **Two qualify.** Both are reported with the script's verbatim evidence string, per the mechanization rule.

| Symbol | net_dex latest | Mechanized flip | Direction | mag ratio | sign changes /11 | whipsaw | Swing bias |
|---|---|---|---|---|---|---|---|
| **NVDA** | −3.64B | ✅ **QUALIFIES** | SHORT | 2.67 | **1** | false | SHORT |
| **PLTR** | +947.3M | ✅ **QUALIFIES** | LONG | 3.57 | 2 | false | LONG |
| MU | −5.41B | ❌ flipped 7/24 — continuation | — | — | 3 | false | short continuation |
| SNDK | −6.16B | ❌ flipped 7/24 — continuation | — | — | 2 | false | short continuation |
| INTC | −537.1M | ❌ flipped 7/24 — continuation | — | — | 3 | false | short continuation |
| ASML | −590.6M | ❌ **FAILS on whipsaw** | — | — | **4** | **true** | no clean thesis |
| TSLA | −5.32B | ❌ never changed sign — **level, not flip** | — | — | 0 | — | SHORT (level only) |
| SPY / QQQ / IWM | −34.5B / −41.0B / −6.86B | ❌ no sign change | — | — | — | — | NEUTRAL |

**NVDA** — *"NVDA net_dex 2026-07-24 +3,162,134,515 → 2026-07-27 −3,635,988,005; prior 10 sessions (07-13 +5,807,663,366 … 07-24 +3,162,134,515) all positive; |flip| 3,635,988,005 vs floor 1,363,060,481 (0.25× trailing-10 median 5,452,241,924)"*. Ten straight positive sessions breaking today, GEX regime flipped POSITIVE→NEGATIVE the same day, exposure distributed across dozens of strikes ($115–$230+) so it is not a single-strike artifact. **The cleanest flip on the board.**

**PLTR** — *"PLTR net_dex 2026-07-24 −480,058,776 → 2026-07-27 +947,286,825; prior 3 sessions (07-22 −178,327,379, 07-23 −328,543,917, 07-24 −480,058,776) all negative; |flip| 947,286,825 vs floor 265,499,262.5 (0.25× trailing-10 median 1,061,997,050)"*. GEX flipped positive the same day. Second sign change in 11 sessions — size below NVDA's conviction.

**Zero vanna-squeeze flags anywhere.** The setup requires a falling-VIX leg; the dated ^VIX series reads 07-21 17.05 → 07-22 16.64 → 07-23 18.70 → 07-24 18.58 → 07-27 18.67 — **choppy-to-rising**. Every put-heavy book on the tape (SPY, QQQ, TSLA, MU, SNDK) is sitting on latent vanna *pressure*, not an actionable squeeze.

---

## 2c. Sector Rotation

**Rotation regime call: `growth→value`, medium confidence.** Durable on the value/financials leg; the growth-out leg is real but sits in the semis sub-complex and Consumer Cyclical, not in the Technology GICS aggregate.

⚠ **Trap 1 fired hard today and the read is built around it.** `sector-flow-persistence` measures sign-consistency of gross call$−put$ turnover — it is **not** aggressor-classified and **not** accumulation. **8 of 11 sectors returned `persistence_score = 1.0 / INFLOW` simultaneously** — near-zero discrimination. Most starkly: **Technology reads 1.0 INFLOW with +$367M net flow on a day XLK fell 0.90% and SMH fell 2.25%.** Rejected as a sector call and decomposed instead.

| Sector | Persist. | Trend | Net flow | 1d / 5d ETF | Verdict |
|---|---|---|---|---|---|
| Technology | 1.0 | INFLOW | +$367M | XLK −0.90% / −0.80% | **TRAP 1 — REJECT.** "Inflow" is software(+) netted against semis(−) |
| Financial Services | 1.0 | INFLOW | +$150M | XLF +1.01% / +1.50% | **Rotating IN — confirmed, 5/5 days, price-confirmed** |
| Healthcare | 1.0 | INFLOW | +$85M | XLV +0.51% / +2.61% | **Rotating IN — confirmed, 5/5 days** |
| Consumer Defensive | 1.0 | INFLOW | +$53M | XLP +1.46% / +0.59% | Watch — magnitude at median, fails the bar |
| Energy | 1.0 | INFLOW | +$39M | XLE −2.11% / +0.72% | **TRAP-1 casualty** — ETF tape says clean 5/5 bearish; USO −8.73% |
| Communication Svcs | 0.8 | INFLOW | +$348M | XLC +1.28% / **−2.83%** | Watch — 1d/5d price disagree |
| Industrials | 0.8 | OUTFLOW | −$47M | XLI +0.30% / **+2.85% (best 5d)** | **TRAP 1 — REJECT.** Flow says out, price says best cyclical |
| Consumer Cyclical | 0.6 | ROTATING | **−$386M** | XLY +1.31% / **−3.29% (worst 5d)** | **Rotating OUT — confirmed, 3 consecutive sessions** |

**Single-name leaders — the conditional +1 requires all three legs** (persistence ≥0.6 ∧ `cum_flow_30d` aligned ∧ |`cum_flow_30d`| ≥ $50M). Four names **FIRE**, all bearish: **TSLA** (−$629,546,735), **INTC** (−$836,153,067), **AMD** (−$225,844,347), **AMZN** (−$186,199,912).
Notable failures: **JPM misses leg C by $2M** (+$47,989,672 vs the $50M floor) — the closest miss on the board. And the entire software pop **fails leg B**: PLTR −$203.9M, MSFT −$540.7M, ORCL −$251.8M, GOOGL −$3.7M all carry *negative* 30-day cumulative flow beneath today's +2% to +7% prints. Today's software rally runs against its own 30-day book — short-covering and mean reversion, not accumulation.

**ETF flow tape (advisory — 0 rubric points):**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| IGV | inflow +$17.9M (#1) | BULLISH | blocks below mid (seller-tilted) | biggest sweep is a **Dec-26 $95 put ($9.3M) > $95 call ($6.7M)** — a hedge | agree (weakly — GICS Tech is Trap-1 confounded) | PLTR, MSFT, NOW, ORCL, GOOGL (none pass 30d gate) |
| SMH | +$15.6M but **MIXED** | not persistent | ~$1.2–2.0B blocks below mid at 541.30 then above mid at 548.30 minutes later = creation/redemption | **near-dated 7/31 puts, ~$192M** at 532.5/527.5/530 — clearly bearish | **DISAGREE** | AMD, INTC (fire); NVDA, LRCX (fail) |
| EWY | +$4.8M | MIXED | at/above mid, modest | small, mixed | n/a (geographic) | — |
| **XLE** | **−$29.6M (largest outflow)** | **BEARISH, clean 5/5** | at/below mid | 2027 calls **sold at bid** — overwriting into weakness | **DISAGREE** — GICS Energy says INFLOW | — |
| XLC | −$2.5M | BEARISH | all below mid | thin Sept put buying | disagree, both sides thin — noise | — |
| XBI | −$1.9M | MIXED | below mid, thin | thin | disagree — genuine **within-Healthcare split** (pharma/devices strong, biotech soft) | — |

Thirteen remaining universe ETFs ranked only (all sub-$5M 5-day net flow, no signal). TAN graceful-skipped as thin.

**Swing-book implication:** the durable rotation is into financials and healthcare and out of Consumer Cyclical and semis — but no Financials or Healthcare single name cleared the leader gate (JPM by $2M; LLY +$22.9M, BSX +$16.8M, QGEN +$8.0M all far short). The sector inflow is real and **not yet concentrated in a name**, which is precisely why nothing sizes.

---

## 3. Swing Setups (1–6 weeks)

**Empty. No name cleared the conviction floor.**

Four names passed the ≥2-agent confluence gate; all four then scored ≤2 against the frozen rubric, below the LOW floor of 3.

| Ticker | Score | Direction | Thesis | Why it died | Sizing |
|---|---|---|---|---|---|
| **TSLA** | **2** | short | Sector-rotation leader out of Consumer Cyclical (all 3 legs); 5/5-persistence ask-side **opening** put buying (12/18 560P $20.3M, 12/18 570P $17.2M, 7/31 400P $17.0M, 83% ask-side ex-0DTE); −16.33% over 5d | Only two rubric lines exist for a pure flow-driven short and both measure the same quantity. Sub-floor at 2. | **skip** |
| **PLTR** | **0** | long | Mechanized DEX flip LONG (mag 3.57) + earnings BUY VOL (clean 8/07 kink, IM 4.52%) | **−3 flow_conflict**: `cum_flow_30d` −$203,873,113 against the long. Accumulation rejected it as a closing-cross artifact; sweeps show 1/5 persistence and 76% bid-side today | **skip** |
| **SMH** | **0** | short | 7/31 532.5/527.5 put vertical, 76,400 lots/leg, $11.3M debit, 2.38:1, repeat count 2, ~98% OI-confirmed opening | **−3 flow_conflict** on +$221.8M — **and the deduction is probably an artifact** (see the register note below) | **skip** |
| **INTC** | **0** | long | $127.5M Nov/Sep diagonal, +1.73M shares delta, both legs Black-Scholes-verified to the penny | **−3 flow_conflict** on −$836.2M, explicit BEARISH label, 4.3× the union median. Directional conflict with its own sector line | **skip** |

**Invalidation discipline (C34):** no dark-pool price-level anchors are quoted for these names because `accumulation-hunter` returned an empty board — the only DP levels available were themselves closing-cross contaminated (e.g. JPM's dominant 356.20 level *is* the closing cluster). Anchoring an invalidation to a level manufactured by the closing auction would be worse than quoting no level.

### 3a. Long swings — none
Both long candidates (PLTR, INTC) died on 30-day cumulative flow running against the thesis. No `distribution_flag` cautions to attach, because no long name survived to carry one.

### 3b. Short / fade swings — none
`contrarian-scanner` returned an empty book. **No ticker anywhere on the tape reached a ±2σ P/C z-score** — the highest reading was TSLA at +1.578, inside the NORMAL band. Two structural notes: MSTR and ORCL's "bullish flow" is a 30-day dip-buy pattern (−20.4% and −34.9% over 30d), not blow-off euphoria — the wrong frame entirely for a crowded-long fade. And INTC's heaviest OI-closing is **long calls capitulating**, which confirms a downtrend rather than marking a bottom.

**Sweeps (informational — 0 rubric points; the sweep-persistence line was removed 2026-05-23 P0.3 after −22pp across two audits).** `sweep-tracker` positively flagged **nothing**, and its most useful work was resolving the day's price-vs-flow divergences as **unwind, not dip-buying**:

- **SNDK** (+$58.1M "bullish" net premium, −11.02%) — a mirage. The three largest tickets ($49.0M, $33.8M, $19.3M) are deep-ITM long-dated **puts sold at the bid**: someone closing protection at a profit after the stock fell into the strike. That books as bullish premium received and conveys zero conviction. The one genuinely fresh ticket is **$38.6M buying an OTM put at the ask** — bearish.
- **MU** (+$17.9M, −2.25%) — 5 of 7 top tickets bid-side closing; 30% ask-side.
- **ASML** (+$15.1M, −5.80%) — 28% ask-side, mostly call/put overwrite income, one real $7.5M ask-side call buy.
- **PLTR** (+7.00%) — **only 1 of 5 sessions in the persistence list, and that session reads bearish**; today 76% bid-side. The rip is not sweep-confirmed.
- **MSTR** (+7.61%) — 91% ask-side, but the ask-side flow is mostly **puts**. Buying protection into strength, not chasing it.
- **ORCL** (+4.27%) — same-expiry 7/31 put + call pairing = an FOMC-week strangle. Event hedge, not direction.
- **DELL** (−2.42%) — the only genuine buying: ask-side call buys plus a put sale (bullish risk reversal). But $2–4M tickets, **0/5 persistence**, single-day.

---

## 4. LEAP Builds (6–24 months)

**Empty. Zero tickers cleared the 6-of-9 gate bar.**

No fresh, ask-side, meaningfully-sized DTE>180 **call** open exists anywhere in the 61-name C12 funnel. The only long-dated OI that moved was on the **put** side:

| Ticker | Contract | DTE | ΔOI | Read |
|---|---|---|---|---|
| INTC | 2027-06-17 **P**85 | 325 | +13,503 | Downside hedge; #1 name in the universe-wide min-DTE-180 scan |
| ORCL | 2027-12-17 **P**100 | 508 | +3,999 (ask-side, 3,014 ask vs 1,003 bid) | Protective put buying despite +4.27% |
| AMKR | 2027-03-19 C55 / 2028-01-21 C50 | 235 / 543 | +1,001 / +211 | Real LEAP calls but trivial scale |
| TCOM | 2028-01-21 C105 | 543 | +133 | Noise |
| RF | 2028-01-21 C37 | 543 | +5 | Noise |

**The required Gate 4 (90d slow-accretion) failed across the board.** Every semis name and every mega-cap green leader reads `cumulative-premium-flow` **MIXED** with net flow at 0.1–0.6% of gross two-way volume — MU alone shows $99.1B bullish against $98.9B bearish over 90 days. That is balanced noise, the exact opposite of the accretion signature this lane exists to detect. Conviction-matrix on the strongest partials: **INTC = COVERED_CALL 14.5%** (dark-pool buying sold against via calls — yield enhancement capping upside, an explicit reject scenario), **ORCL = DISTRIBUTION 13.5%**, **AMKR = DIRECTIONAL_SHORT 27.1%**.

⚠ **C47 confirmed a fourth time:** `consecutive_build_days` returned **10/10 for essentially every name checked**. The field aggregates OI change across all expiries and is dominated by 0–25 DTE contracts — it does not discriminate long-dated positioning at all.

Macro framing for the horizon: rising long rates (10Y +28bp/30d to 4.69%) with core PCE at 3.41% compress long-duration valuations. Today's semis drawdown is exactly the tape a genuine LEAP buyer steps into — **and nobody did.**

---

## 5. Volatility Surface

**Headline: index realised vol (SPY rv20 **11.0**, IWM **11.0**) against semis realised vol (SMH 48.1, SOXX 57.7, MU 86.4, SNDK 134.7, SOXL 170.6, NBIS 139.3, BE 124.0) is the widest dispersion on the tape.** That, not any single name, is the vol story.

**Substrate hygiene — the core finding.** 23 names pulled through `scripts/term_structure_hygiene.py` (`min_contracts=15`, a **tunable, not audit-frozen** parameter):
- Raw `iv-term-structure` returned **BACKWARDATION on 21 of 23** names — the near-mechanical default is reconfirmed.
- **14 of 23 flipped** raw→hygiene once the 0DTE bucket and thin tenors were dropped: MU, SNDK, AMD, STX, COHR, ENTG, SOXL, SMH, AMKR, DELL, ARM, PLTR, MSTR, WOLF.
- `base_shape` flipped on 6. **MU, AMD and PLTR are CONTANGO base with a kink riding on top** — a shape the single-label tool cannot express at all.
- **`NO_NEAR_TENOR`: ENTG and AMKR.** Nearest surviving tenor is 25 DTE, past the 21-DTE ceiling. Their front ends are **unmeasurable, not calm** — a 1.000 ratio there means "no data".

⚠⚠ **Two systemic substrate defects surfaced:**
1. **Every `iv-percentile-zscore` read this run carries `dates_used: 73`** — identical n across all 23 tickers, well under the ≥120-day first-class threshold. **All percentile and z-score reads are PROVISIONAL.** Systemic, not a per-name gap.
2. **MU raw `iv_rank` 79.9 vs Goyal-Saretto percentile 42.47 (NORMAL)** — a 37-point divergence. The raw rank was being driven by a single-day spike, and per the data correction that spike was **−2.25%, not −9.09%**. Both facts point the same way: **MU's "elevated IV" is false.** ARM shows the same pattern smaller (86.7 raw vs 68.49 GS).

**KINKED names by prominence:** ARM (**54.2%**, Aug-21) → MU (17.3%, macro) → SOXL (12.5%) → WOLF (11.0%) → PLTR (9.1%, earnings) → DELL (9.0%) → SMH (8.2%) → AMD/COHR/MSTR (~6.5%) → STX (5.5%).

**BACKWARDATION calendar candidates: NONE qualify.** The bucket requires evidence the front-end panic is *resolving*; a single EOD snapshot three sessions before FOMC cannot show that. Every BACKWARDATION name above 1.10 has a catalyst inside its horizon. **HOLD, not a calendar bucket, until post-PCE 7/30 EOD.**

**IV outliers** are all 0DTE 2026-07-27 expiry — MU dominates with 4 strikes, INTC and NVDA 2 each. These are the mechanical tail of today's price action, not whale mispricings.

**Earnings vol** (`earnings-scout`): **one positive flag, PLTR BUY VOL**, and it is the only macro-decontaminated kink in the scan — contango base, isolated 9.1%-prominence kink at the 8/07 expiry (the correct first expiry after the 8/03 PM print), and by 8/3 both FOMC and PCE are resolved history. `front_end_ratio` 0.946 (no front panic), back-month skew 1.01 COMPLACENT (event tail not priced), **implied move 4.52%**. The scout rated it *moderate, not high* — forward premium looks appropriately priced rather than cheap.
Everything else **SKIP**, and the reason is uniform: **STX (7/28), BSX (7/29), LRCX (7/29), MSFT (7/29) are explicit MACRO_FOMC_PCE contamination** with front-end ratios of 1.5–1.94 that belong to the Fed, not the print. **AAPL and AMZN (7/30) have the cleanest-looking kinks in the batch** — contango base, spike at the correct post-print expiry — but report **the same day as Core PCE and Q2 GDP**, so the premium is un-splittable. A SELL VOL there is short a Fed decision.

**Two more data gaps registered:** `uw insights analyst-vs-flow` returned **zero `analyst_recommendation` fields across all 13 tickers** — analyst-vs-flow disagreement is **UNASSESSABLE**, not "none". And `uw historical pc-ratio-zscore` **has no `--date` flag** in the installed build, which makes the −2 contrarian rubric line's "rising z" requirement **unevidenceable**.

---

## 6. Risk & Correlation

**Macro headline:** core PCE 3.41% YoY against core CPI 2.81%, 10Y at 4.69% after +28bp in 30 days, fed funds 3.63%, curve normal +34bp, payrolls +57k, unemployment 4.2%, USD weakening. Sticky inflation into a rising long end, three sessions before the Fed.

**Forward event risk:** FOMC decision + Warsh presser **T+2 (7/29)**; Core PCE + Q2 GDP advance **T+3 (7/30)**; ECI/Chicago PMI/Michigan T+4. **Both Tier-1 events sit inside every swing horizon that could have been opened today** — the event-risk gate fired −1 tier on every name evaluated.

**Panic gate — FIRING.** `front-end-iv-ratio`: SPY **1.062** (sub-threshold) but **QQQ 1.221** (near IV 32.98% vs far 27.01%), above the 1.10 threshold. All six gate-relevant candidates are Nasdaq/tech-complex names, so the QQQ reading is binding market-wide: **−1 tier panic on every name**.

**Correlation — one dominant cluster.** `semis_infra_cluster` = **SMH, AMD, INTC, MU, SNDK**, all pairwise ≥0.70:

| Pair | Corr | | Pair | Corr |
|---|---|---|---|---|
| SMH/AMD | **0.924** | | SMH/MU | 0.864 |
| SMH/INTC | 0.899 | | AMD/SNDK | 0.807 |
| MU/SNDK | 0.892 | | INTC/MU | 0.797 |
| SMH/SNDK | 0.873 | | AMD/MU | 0.779 |
| INTC/AMD | 0.869 | | INTC/SNDK | 0.763 |

Kept member: **AMD** (highest raw_score in cluster). SMH, INTC, MU, SNDK each take the mechanical −1 tier. **A book of SMH-short + AMD-short + INTC would have been one position, not three.** No pair involving TSLA, PLTR, WOLF, NVDA, DELL, GOOGL, AAPL or JPM cleared 0.60.
*Flagged for the next audit, not decided here:* the correlation table is **direction-blind** — SMH was routed SHORT and INTC LONG, which in a real book is a spread, not duplicated risk. The rule was applied literally per the "no discretionary exemptions" instruction.

**Fundamentals verdicts (top-5):**

| Ticker | Dir | Verdict | Adj | The contradicting facts |
|---|---|---|---|---|
| **AMD** | short | **VETO** | veto | Short flow into a **3-of-4 beat streak**, +34.97% revenue / +123.4% EPS growth, and a net-bullish catalyst stack (Wedbush AI upgrade, Microsoft partnership, Helios platform) **8 days before earnings**. Today's −5.17% is sector sympathy, not an AMD event. Squeeze risk. |
| WOLF | short | CAUTION | −1 | Deep unprofitability confirms the short (gross −16.2%, net −72.93%, revenue −6.41%) — **but insiders are net BUYING** (MSPR +33.33; Jul-26 +100 / +38,775 sh) into a $58M put ladder. ⚠ `leverage_flag: low` is a **script mislabel** — raw D/E 6.9952, current ratio 0.3586. The convert-arb / hard-to-borrow alternative for the ladder remains **unresolved**. |
| AMZN | short | CAUTION | −1 | Earnings **7/30 — the same session as Core PCE and Q2 GDP**. The most concentrated binary-event day in the set. Last two quarters flipped from big beats to small misses; insider MSPR −94.28. |
| TSLA | short | CONFIRM | 0 | EPS −37.66% YoY at a 308× PE, most recent quarter −36.43% miss, insider MSPR −45.35 negative five straight months. |
| PLTR | long | CONFIRM | 0 | 4/4 beat streak, +67.71% revenue growth, 84.07% gross margin. **Fundamentals-only** — the flow thesis had already failed upstream. |

`fz_context` is **NA across all five** — `short_interest`, `recom` and `target_price` all landed in `upstream_gaps` with no screen fallback. NA never penalises, but it is a real loss today specifically because four of five are short theses where days-to-cover would matter most. `insider_cluster_flag` is **`null` fleet-wide** (the `fz` insider store is empty market-wide), never `false`.

**Debate (Phase 2c): NOT RUN.** Skipped as a structural no-op — the debate gate can only *cut* size, and there is no size to cut on a flat board. `debate_residuals: null` everywhere; no residuals were fabricated.

**Breadth cross-check (advisory):** 328 advancers / 175 decliners, **65.21% green**, avg +0.77%, median +0.82%, top mover WDAY +9.01%, worst SNDK −11.02%. `divergence_flag: false` in the classic sense (the index is not green on negative breadth) — but there is a **reverse divergence** worth naming: `uw` flow breadth reads 35.2% bullish against 65.2% green price. Bearish flow under green price is hedging into a rotation. Advisory, no sizing impact.

**Adverse-flow exit scan — `conviction_2026-07-24`** (TSLA, AKAM, FSLR; none were ever sized):

| Ticker | 7/24 thesis | Today's alerts | Read |
|---|---|---|---|
| TSLA | SHORT | LARGE_DARK_POOL $93.9M (9,299 trades); OI_SHIFT +369,906; flow bearish −$71.3M | **Confirming.** No exit tag. |
| AKAM | BUY VOL into 8/07 | HIGH_IV_RANK **97.5**; DP $3.1M; flow +$586K | **Working.** Front IV richening is what long vega wants. But at 97.5 IV rank there is little expansion room left — profit-taking watch, not an exit. |
| FSLR | SELL VOL into 7/30 | HIGH_IV_RANK **98.3**; DP $30.0M; flow −$3.7M | **Mild adverse watch.** Short vega with IV near its ceiling three days before earnings **and** PCE/GDP landing the same session — the event stack is compounding, not thinning. |

**Hedge sleeve: none recommended.** The book is 100% flat and the carried watchlist names were never sized. There is no net delta to hedge. Building an SPY/QQQ vertical or VIX ladder against zero notional would *manufacture* exposure, not offset it. The correct posture into T+2 and T+3 is to stay flat and let the events pass.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Empty. No name reached MEDIUM (7) or HIGH (9). The highest confluence-gated score was 2.**

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no per-tier expectancy is printed this run. The most recent `/calibration-audit` (2026-07-25) found the excess column is **71% denominator-driven** (slope −80, R² 0.636), and with zero sized calls today there is no new tier row to add. The live sizer remains the win-rate ladder; the C3 fractional-Kelly sizer stays advisory until tier×expectancy is monotone on n≥30.

### Full scored set (for the audit trail)

| # | Ticker | Raw | Tier | Dir | Components | cum_flow 30d | win_rate (n, source, excess) | Pre-risk | Final |
|---|---|---|---|---|---|---|---|---|---|
| 1 | WOLF | **4** | DROP | short | +2 multileg · +1 oi build · +1 cum-flow accretion | −$71.9M | null · NA(substrate) | skip | **skip** — failed ≥2-agent gate |
| 2 | AMD | **3** | DROP | short | +1 sector · +1 cum-flow · +1 oi build | −$225.8M | 0.6119 (134, backtest_clean, **+0.0224**) | skip | **watch_only** — VETO |
| 3 | TSLA | 2 | DROP | short | +1 sector · +1 cum-flow | −$629.5M | 0.6119 (134, backtest_clean, +0.0224) | skip | skip |
| 4 | AMZN | 2 | DROP | short | +1 sector · +1 cum-flow | −$186.2M | 0.6119 (134, backtest_clean, +0.0224) | skip | skip |
| 5 | DELL | 1 | DROP | long | +1 cum-flow accretion | +$73.8M | 0.3923 (130, backtest_clean, **−0.0385**) | skip | skip |
| 6 | PLTR | 0 | DROP | long | +1 DEX flip · +1 earnings vol · +1 oi build · **−3 flow_conflict** | −$203.9M | null · NA(substrate) | skip | skip |
| 7 | SMH | 0 | DROP | short | +2 multileg · +1 oi build · **−3 flow_conflict** | +$221.8M | null · NA(substrate) | skip | skip |
| 8 | INTC | 0 | DROP | long | +2 multileg · +1 oi build · **−3 flow_conflict** | −$836.2M | null · NA(substrate) | skip | skip |
| 9 | NVDA | 0 | DROP | short | +1 DEX flip · **−1 flow_conflict_lite** | +$22.2M | null · NA(substrate) | skip | skip |
| 10 | MU | 0 | DROP | neutral | none (vol flag withdrawn) | +$536.2M | null · NA | skip | skip |
| 11 | SNDK | 0 | DROP | neutral | none (FLAT shape — rubric gap) | +$753.3M | null · NA | skip | skip |
| 12 | GOOGL | 0 | DROP | neutral | none — **DISTRIBUTION 0.59** on 4,348 trades | −$3.7M | null · NA | skip | skip |
| 13 | AAPL | 0 | DROP | neutral | none — **DISTRIBUTION 0.60** on 9,440 trades | +$21.0M | null · NA | skip | skip |
| 14 | JPM | 0 | DROP | neutral | none — sector fails leg C by $2M; cum-flow fails the same floor **and** the intent screen (C28 flag) | +$48.0M | null · NA | skip | skip |

**Union-median |cum_flow_30d| = $195.04M** (n=14). −3 `flow_conflict` fired on PLTR, SMH, INTC; −1 `flow_conflict_lite` on NVDA. Mutually exclusive throughout — never co-applied.

**Win-rate substrate (P0.3 clean-query protocol, executed — headline never quoted):**

| Class | Headline (**not quoted**) | Clamped dropped | C12 dropped | Kept n | **Clean WR** | SPY same-dir | **Excess** |
|---|---|---|---|---|---|---|---|
| `bearish_flow` | 62.5% / 152 sig / 12 trunc | 12 | 6 | **134** | **0.6119** | 0.5896 | **+0.0224** |
| `bullish_flow` | 35.9% / 153 sig / 12 trunc | 11 | 12 | **130** | **0.3923** | 0.4308 | **−0.0385** |

Complete-window filter `signal_date ≤ 2026-07-20`; 35 unique signal dates 2026-05-29 → 2026-07-20; benchmark rebuilt from a dedicated SPY trend pull over exactly those windows. Market-wide per class — **not ticker-specific**.
`bearish_flow` at 0.6119 with positive excess is the **7th consecutive positive-but-unscoreable read**. **C19 was CLOSED as REFUTED on 2026-07-25**, so this accrues to nothing — noted, not banked, and not reported as progress toward any graduation.

**Σ-check (validator invariant) — all 14 rows pass:**
```
TSLA 1+1=2 ✓   PLTR 1+1+1-3=0 ✓   SMH 2+1-3=0 ✓   INTC 2+1-3=0 ✓
WOLF 2+1+1=4 ✓ AMD 1+1+1=3 ✓      AMZN 1+1=2 ✓    DELL 1=1 ✓
NVDA 1-1=0 ✓   MU 0 ✓  SNDK 0 ✓   GOOGL 0 ✓  AAPL 0 ✓  JPM 0 ✓
```

### Rubric lines that fired ZERO times today (discrimination signal)

| Line | Why |
|---|---|
| **+3 accumulation conjunction (C11)** | `accumulation-hunter` empty board — the closing cross ate the entire mega DP tier. The conjunction gate was never exercised. |
| **+1 conviction-matrix DIRECTIONAL_LONG >70** | Doubly dead: LEAP radar empty, and every conviction-matrix read was COVERED_CALL / DISTRIBUTION / DIRECTIONAL_SHORT. |
| **+1 vol-surface KINKED/BACKWARDATION** | MU withdrawn by the data correction; SNDK's hygiene shape is **FLAT** (outside the line's literal shape list); PLTR's kink routes to earnings-scout under C13. |
| **−2 contrarian overcrowded long** | **Currently UNFIREABLE.** Nothing reached ±2σ, *and* `pc-ratio-zscore` has no `--date` flag so the "RISING" requirement cannot be evidenced at all. Tooling defect. |
| **+1 opex-pin top-5** | N/A — third Friday was 7/17, ten days past. |

⚠ **C47, fourth confirmation:** `+1 multi-day OI build` fired **14 of 14** at the label level (`BUILDING`, `consecutive_build_days` 5). Applying the trade-direction test cut it to **5 of 14**. The rubric line as written would have awarded +1 to fourteen consecutive names — **recommend the audit write the direction test into the line text.**

### Conviction scoring rubric (Step 4, verbatim — frozen version `2026-06-12`)

```
Daily conviction score = Σ:
  +1  MECHANIZED DEX flip or vanna-squeeze in trade direction — verified SIGN CHANGE, not a level:
      sign(net_dex) on the latest session opposite to ≥3 consecutive prior sessions, from dated
      `uw options-structure dex --date` calls; |net_dex| on the flip day ≥ 0.25× trailing-10-session
      median |net_dex|. MUST be computed with scripts/dex_flip.py, not by hand. Report
      sign_changes_in_window / whipsaw_warning. Vanna disjunct requires a dated VIX source.
      # DEMOTED +3→+1 and MECHANIZED 2026-06-12 audit P0.4
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified
      institutional-tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d
      confirms (sign aligned AND |cum_flow_30d| ≥ $50M); else halved to +1.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: award only
      when dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +1  cumulative-premium-flow net directional accretion in trade direction (30d) — INTENT-SCREENED:
      0 if a C28 distribution_flag is present, or if deep-ITM sub-parity ex-div calls.
      # DEMOTED +3→+1 2026-06-06 audit P1.4
  +1  sector-rotation-strategist names ticker as single-name leader in a rotating sector —
      CONDITIONAL: persistence_score ≥ 0.6 AND cum_flow_30d aligned AND |cum_flow_30d| ≥ $50M.
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising pc-ratio-zscore (VRP positive)
      # INFORMED-FLOW CONTINUATION penalty, not "crowd is wrong, fade it". Needs a multi-date z path.
  -3  flow_conflict — cum_premium_flow 30d direction clearly opposite dominant_signal_class
      (sign flip + magnitude > today's union-median |cum_flow_30d|, or explicit OPPOSITE label)
  -1  flow_conflict_lite — 30d cum_flow read is MIXED (near zero, or aligned but bottom-quartile)
      # -3 and -1 are MUTUALLY EXCLUSIVE — apply ONE, never both.
  # REMOVED: sweep-persistence top-5 (2026-05-23 P0.3, −22pp); signal-confluence ≥4 (2026-06-12 P0.2);
  # gamma-flip 0DTE breakout (2026-05-09, §2 is advisory/0 points).
  # TIER GATES (risk-monitor, 2d — 0 points, never score_components):
  -1 tier  correlation cluster (pairwise corr ≥ 0.70)
  -1 tier  market-regime conflicts with trade direction
```
Tiers: **≥9 HIGH** (full) · **7–8 MEDIUM** (half) · **3–6 LOW** (starter/watch) · **≤2 drop**.
**Tier-cut status:** the ≥9 HIGH cut failed its scheduled re-confirmation on 2026-06-12 (bands inverted on the first post-UPTREND window). Retained under the P0.1 freeze but carrying **no validated ranking claim**; the P0.6 out-of-regime guard caps all sizing at half in the interim.

### Deep-dive hand-off
**None.** Step 8.5 is skipped on a no-edge day — there are no HIGH-tier names to hand off.

---

## 8. Watch-only — single signal, no confluence

For journaling only. **Not for trade entry.** Two of these are the strongest individual pieces of evidence on the tape and still correctly failed the gate.

| Ticker | Dir | Flagging agent | The evidence | Why it stops here |
|---|---|---|---|---|
| **NVDA** | short | dealer-positioning | **The cleanest mechanized DEX flip on the board** — 10 straight positive sessions breaking today, mag ratio 2.67, 1 sign change, whipsaw false, GEX flipped same day | **One agent.** vol-surface explicitly declined to flag it; sector-rotation fails leg B (+$22.2M, misaligned); multileg rejected its 7/31 calls as overwriting. Its own +1 was then cancelled by −1 flow_conflict_lite. |
| **WOLF** | short | multileg | **The cleanest aggressor evidence on the tape** — every leg of the $58M 9/18 put ladder carries an explicit ask/bid side across multiple trades; bought the post-kink 9/18 tenor at 131.7% rather than the 149.6% 8/28 kink | **One agent.** Step-0 `confluence_bearish` score 5 is **funnel-seed only, 0 points, not a second opinion** (2026-06-12 P0.2). Fundamentals CAUTION on insider buying. Convert-arb explanation unresolved. |
| MU | — | vol-surface (withdrawn) | BUY VOL flag **withdrawn** — premised on a −9.09% print that was actually −2.25% | One agent, flag withdrawn |
| SNDK | vol long | vol-surface | VRP −0.081, GS percentile 90.41 HIGH_IV, hygiene shape **FLAT** despite 8/5 earnings 9 days out — event premium looks underpriced. IM 11.53% | One agent. **Also a rubric-coverage gap:** the +1 line requires KINKED or BACKWARDATION, and "FLAT when it should be KINKED" is a real setup the frozen rubric cannot score. |
| AMZN | short | sector-rotation | Conditional +1 all legs, −$186.2M | One agent + raw <3. Earnings 7/30 same session as PCE/GDP. |
| AMD | short | sector-rotation | Conditional +1 all legs, −$225.8M, put-dominant OI build — **the only name clearing the C4 opening gate cleanly** | One agent **and fundamentals VETO** |
| GOOGL | — | accumulation-hunter | `institutional-accumulation` **DISTRIBUTION 0.59** on 4,348 trades, mega buy_ratio 0.163 — **not** closing-cross dependent | One agent; the rubric has no distribution deduction line (C28 is an intent screen) |
| AAPL | — | accumulation-hunter | **DISTRIBUTION 0.60** on 9,440 trades, mega buy_ratio 0.094 | Same |
| ARM | vol | vol-surface | Aug-21 kink at **54.2% prominence** (5,472 contracts vs 262/474 neighbours), well past its 7/29 earnings — looks like a discrete positioning print | Watch/investigate, explicitly not a trade rec |
| JPM | — | (none) | Sector leader **misses by $2M**; block-tier buy survives the closing-cross strip but thin | Accumulation-hunter explicitly declined to flag; C28 distribution_flag present |
| DELL | long | sweep-tracker | The only genuine ask-side buying on the tape — call buys + put sale (bullish risk reversal) | $2–4M tickets, **0/5 persistence**, single-day |

---

## Appendix — artifact register for `/calibration-audit`

Twelve distinct data-integrity issues surfaced this run. Recording them is the run's main durable output.

| # | Artifact | Status | Evidence |
|---|---|---|---|
| 1 | **`market_data.py` non-deterministic pct columns** | **NEW — P0** | Same args minutes apart gave MU −9.09%/−2.25%, INTC −8.54%/−0.70%, XLK −2.33%/−0.90%. Closes stable; only the prior-close denominator moved. See `DATA_CORRECTION.md`. **C12 floor unaffected** (uses `last_close` + volume). |
| 2 | **Vertical short legs invert `cumulative-premium-flow` sign** | **NEW** | SMH's bearish 532.5/527.5 put *debit* vertical sells the 527.5P, which UW books as **bullish** premium — ~$65M+ of the +$221.8M that then generated SMH's own −3 flow_conflict. The deduction was partly manufactured by the structure it penalised. |
| 3 | **SPX box / jelly-roll financing in `top_premium_trades`** | **NEW** | >$700M of "premium" is 7000/8000 call-ask + put-bid pairs at identical size and the same second (10/16 2,500×2 @17:34:21; 12/18 1,750×2 @16:33:39; 11/20 1,000×2 @14:00:23). ~Zero directional content. |
| 4 | **Closing-cross 20:00:00Z–20:15:27Z** | Recurring | Ate the entire mega DP tier — MU 0.602→~0.23 stripped; PLTR all 4 mega trades inside 34 seconds; ASML 100% of mega tier = one 20:07:03Z print; GM flips 2.0→0.81. Now confirmed on a **non-quarter-end** session. |
| 5 | **ZGL-grid corruption** | Recurring | SPY 360.62 vs spot 750.13; QQQ 352.82 vs 706.7; IWM ~150–196 vs ~293–296; INTC 24.3 vs 91.67 — each ≈ half spot. |
| 6 | **Un-split-adjusted strike grid** | Recurring | MU tickets at 2110/1710/1810/1300 against a $900 spot; ASML legs 1670–1850. |
| 7 | **`iv-percentile-zscore` n=73 everywhere** | **NEW** | Identical `dates_used: 73` across all 23 tickers, under the ≥120 first-class threshold. All percentile/z reads **provisional**. |
| 8 | **`analyst-vs-flow` returns no `analyst_recommendation`** | **NEW** | Zero across 13 tickers; only the `options_flow` half populates. Disagreement **unassessable**, not absent. |
| 9 | **`pc-ratio-zscore` has no `--date` flag** | **NEW** | Makes the −2 contrarian line's "rising z" requirement **unevidenceable** in the installed build. |
| 10 | **`fz screen` ticker corruption** | Recurring | Leading char doubled: `RRTX`→RTX, `BBBY`→BBY, `CCPAY`→CPAY, `DDYN`→DYN. Breadth endpoint unaffected. |
| 11 | **`fz` insider store empty market-wide** | **NEW** | "No insider data in the local store yet" — `insider_cluster_flag` is `null` fleet-wide, never `false`. C18 remains untestable. |
| 12 | **`fz_enrich` upstream gaps** | Recurring | `short_interest`, `recom`, `target_price` all in `upstream_gaps`, no screen fallback fired for any of the top-5. Costly today — 4 of 5 were short theses needing days-to-cover. |
| 13 | **SMH put-monotonicity violation** | **NEW** | 530P prints $8.15 against the 527.5P's $8.48 — a higher-strike put cannot be worth less. 4-trade average across a moving spot, probably benign, but don't build on the 530 leg. |

**Two rubric-mechanics items escalated by the quant, not acted on under the freeze:**
1. **Extend the 5%-of-gross scale-relative floor from the C11 +3 line to the standalone +1 cum-flow line.** TSLA (1.5% of gross), AMZN (1.5%) and DELL (2.0%) all collected +1 on noise-scale net imbalances against enormous two-way books; only WOLF (19.7%) and INTC (11.5%) were genuinely directional flow reads.
2. **Write the direction test into the `+1 multi-day OI build` line** — 14-of-14 at the label level versus 5-of-14 after the direction test.
