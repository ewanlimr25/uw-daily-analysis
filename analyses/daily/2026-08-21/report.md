# Daily Market Analysis — 2026-08-21

*Monthly third-Friday OPEX. August monthlies expired at today's close.*

## Executive Summary

- **Regime + GEX state:** TRANSITIONAL (trend UPTREND). SPY 765.72 (+0.41%), above 20/50 SMA, −1.75% from the 90d high. SPY dealer gamma **FULLY_NEGATIVE** (`total_gex` −$894.8M, short-gamma for 5 straight sessions); QQQ 713.44 near flat at −$18.7M with its regime label contradicting its own sign. IWM 299.96 (+0.77%) pinned on ZGL 299.43. VIX 15.13 (−5.5% today, **+6.18% on the week**). Price breadth broad-green (66% of S&P, RSP +0.63% > SPY) but **options-flow breadth is 39.2% bullish — 2-to-1 bearish underneath**. Sector lean: netted Technology **−$328.6M, the largest outflow**, against **+$4.04B of gross Tech turnover ranked #1**.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** **SPY** — FULLY_NEGATIVE · ZGL null (`zgl_reliable=false`) · call wall 780 / durable put wall 760 · short-gamma trend/breakout prior, favour long gamma over short premium. **QQQ** — label POSITIVE but `total_gex` **negative** (−$18.7M, trust the sign) · ZGL 207.89 vs spot 713 is a 71% miss (`zgl_reliable=false`) · call wall 730 / put wall 700 · near-zero book, range structures only. **Advisory, 0 rubric points — see §2, and note tonight's OPEX unwind degrades both priors more than a normal session.**
- **Top swing build:** **None sized.** The only name clearing the drop floor is **IWM (raw_score 3, LOW)** — a Sep-11/Sep-18 282–295 put ladder, fresh-opening and re-struck lower four sessions running, corroborated by an independent 634k-contract put OI build at the same strikes, `historical trend` printing **9 bearish days of 10**, cf30 −$346.1M, bought at an IV rank of **6.07**. It is a **directional short**, so it routes to `watch_only` and is never sized (2026-08-01 P0 #1). Its `win_rate` is `NA(substrate)` — `multileg_directional` is not a measurable class.
- **Top LEAP candidate:** **None.** `leap-positioning-radar` qualified nothing — 1 of 9 gates passed on its only in-universe name (IBIT), whose 90d cum-flow net is **3.4% of gross** and whose conviction-matrix confidence is **1.1%** against a >70 bar.
- **Biggest risk:** `Nasdaq_semis_beta_cluster` **{IWM, QQQ, INTC, MRVL, AVGO}** — five of nine candidates in one ≥0.70 correlation component (QQQ/INTC **0.870**, IWM/QQQ 0.804). The board is one Nasdaq-beta bet expressed five ways. Hedge sleeve notional today: **$0** — there is no beta to hedge.

**Sized book: EMPTY. One `watch_only`, eight `skip`, zero dollars deployed.**

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity"**, trend **UPTREND**. SPY 765.72, above both the 20-SMA (762.33) and 50-SMA (751.75), +3.73% over 30 days, −1.75% off the 90-day high. Guidance: *"Half position sizes. Favor defined-risk strategies. Iron condors in range."*

**The breadth split is the day's most important single fact.** Two breadth measurements disagree, and they are measuring different things:

| Source | Measure | Reading |
|---|---|---|
| `fz breadth --group sector` (advisory) | **Price** breadth | 332 advancers / 169 decliners, **66% green**, avg +0.59%, median +0.60% |
| `uw risk market-regime` | **Options-flow** breadth | 2,479 bullish / 3,837 bearish of 6,316 optionable, **39.2% bullish** |

A broad-green price tape sitting on 2-to-1 bearish options-flow breadth is a hedging/distribution signature. There is **no price-breadth divergence** (green index, 66% green — `divergence_flag: false`), so the advisory `fz` lane confirms the tape; the divergence is between price and flow, which is the more interesting one.

**Per-index gamma (current-state EOD book; §2 carries the forward read):**

| Index | Spot | Zero-gamma | `total_gex` | Regime (adjudicated) | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 765.69 | null (`zgl_reliable=false`) | −$894,775,820 | **FULLY_NEGATIVE** (label agrees with sign) | 780 (+1.9%) | 760 (−0.7%) durable |
| QQQ | 713.23 | 207.89 → **71% miss**, `zgl_reliable=false` | −$18,741,957 | **NEGATIVE** (label says POSITIVE — **contradicts its own sign**; sign trusted) | 730 (+2.4%) | 700 (−1.9%) |
| IWM | 299.95 | **299.43** — spot sits 0.17% away, the tightest pin of the three | — | POSITIVE, dealers net long gamma | — | $1.75B +GEX wall at 300 |

The SPY grid shows a −$678M spike at the 765 strike and QQQ +$143M at 713 — both are the **expiring ATM OPEX straddle**, not durable dealer positioning. They are excluded from the wall reads above.

**`uw options-flow dte-volume-share`:** 0DTE **45.9%**, weeklies 20.1%, monthlies 19.0%, LEAPs 3.6% → `regime_hint: RETAIL_DRIVEN`. This is a market-level overlay only (the tool returns `{symbol: MARKET}` and has no per-sector split) and it downgrades rotation and swing conviction **uniformly**.

**`uw historical vrp`:** SPY **FAIR** +0.0016 (IV30 12.7% vs realised 12.54%). QQQ **NEGATIVE −0.0307** (IV30 19.28% vs realised **22.35%**) — the Nasdaq complex is a premium-**buying** environment; implied is trading below delivered. Note QQQ rv20 21.8 vs SPY 12.8, an unusually wide index-vol spread.

**Macro backdrop** (`scripts/fred_macro.py`) — **stagflationary tint**: curve normal at +0.50 (10Y 4.69 / 2Y 4.19), core CPI **2.79% YoY**, core PCE **3.29% YoY** (well above target), unemployment 4.1%, payrolls **contracted −23k MoM**, 10Y **rising** (+0.06 over 30d), USD **weakening** (−1.41 over 30d), fed funds 3.63 — a barely positive real policy rate. Payrolls contracting while core PCE runs 3.29% is the worst backdrop for levered-beta longs and the best for owning convexity.

**Forward event risk** (trading-day offsets from today):

| Event | Date | Offset | Confidence |
|---|---|---|---|
| Weekly jobless claims | 2026-08-27 | T+4 | standard cadence |
| **Core PCE (July)** | 2026-08-28 | **T+5** | inferred (last Friday of month) |
| **NFP / Employment Situation (August)** | 2026-09-04 | **T+10** | inferred (first Friday) |
| **CPI (August)** | 2026-09-10 | **T+13** | inferred |
| **FOMC decision + SEP + presser** | **2026-09-16** | **T+17** | **CONFIRMED — federalreserve.gov** |

Labor Day 2026-09-07 is excluded from the offsets. Only the FOMC date is confirmed; the four inferred dates follow standard release cadence and are flagged as such rather than presented as verified.

**Tape framing (raw Yahoo chart API OHLCV, `--as-of` pinned).** Today was a **broad bounce inside a down week**. RSP +0.63% > SPY +0.41% — equal-weight led, so this was a genuinely broad advance, not cap-weighted:

| | SPY | QQQ | IWM | RSP | VIX | XLB | XLV | XLY | XLF | XLI | XLK | XLU |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **1d %** | +0.41 | +0.35 | +0.77 | +0.63 | −5.50 | +2.14 | +1.29 | +1.15 | +0.93 | +0.27 | +0.11 | −2.28 |
| **5d %** | −1.37 | −2.41 | −1.68 | −0.49 | +6.18 | +1.90 | **+4.33** | −0.15 | −1.17 | −3.36 | **−3.53** | −3.48 |

The week is a **tech de-rating** — XLK worst at −3.53% — with healthcare (+4.33%) and energy (+2.79%) leading and utilities (−3.48%) lagging. VIX fell 5.5% today but is **up 6.18% on the week**.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** Prose-only, **0 rubric points**, no backtested predictive claim. Scope is SPY and QQQ only.

**OPEX degradation — state this first.** The `expiry_heatmap` shows today's expiring 2026-08-21 bucket carrying **$6.56B in premium** (20.85M call + 14.05M put contracts), the second-largest in the entire book behind Sept-18's $7.21B. All of it vanishes at tonight's close. Tonight's EOD book is therefore a **materially degraded prior** versus a normal session: a large slice of what is being read here disappears overnight, and Monday's real hedging book will be September monthlies plus freshly minted weeklies.

| Index | Regime | ZGL | Call wall | Put wall | Structure bias |
|---|---|---|---|---|---|
| **SPY** | **FULLY_NEGATIVE**, `total_gex` −$894.8M — label and sign **agree** | null, `zgl_reliable=false` (FULLY_NEGATIVE days return null by design) | **780** (+$73.8M; secondary 770 +$66.9M, 785 +$62.5M) | **760** (−$192.2M) — the 765 strike (−$678M) is the contaminated expiring ATM straddle, not a level | Short-gamma → dealer hedging amplifies moves. Favour debit verticals / directional 0DTE / long gamma **over premium-selling** |
| **QQQ** | **NEGATIVE** — label prints POSITIVE, `total_gex` is −$18.7M. **Label/sign disagree; trust the sign** | 207.89 vs spot 713.23 — a **71% miss**, deep-OTM extrapolation. `zgl_reliable=false` | **730** (+$56.5M; 735 +$55.2M) | **700** (−$71.3M; 705 −$45.1M) | Near-zero magnitude = effectively a coin-flip book. Range structures bounded 700–730, small size |

**Regime freshness** (`gex-time-series`): SPY has held short-gamma for **5 straight sessions** (08-17 → 08-21) — entrenched, not fresh. QQQ has been nominally negative for 4 sessions but its magnitude is **collapsing toward a flip** (−$524M → −$777M → −$18.7M), so it is transitioning, not a regime to lean on.

**Mandatory caveats:** EOD is a prior, not a target — fresh 0DTE OI floods in during the first 30–60 minutes and re-computes both ZGL and walls. Both ZGLs are unreliable tonight and the fallback is the `total_gex` sign plus spot-vs-wall position. Overnight gap risk voids the prior; the nearest Tier-1 print is Core PCE at T+5, so near-term gap risk is low but not zero. `uw` cannot isolate the D+1 expiry (`gex --dte-max 1` errors) — this is the standing 0–45 DTE book. And this is the SPY/QQQ **ETF** gamma book, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup

> Advisory, delta-neutral, **0 rubric points**. Not a guaranteed edge — the validation sample contains no vol shock, so the short-vol left tail is **unsampled**.

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` / VIX | **LOW** / 15.13 | **LOW** / 15.13 |
| implied move | 0.38% | 0.66% |
| `expected_range_pct` | 1.18% | 1.98% |
| `size_scalar` | 0.5 | 0.5 |
| Rolling backtest | 86.7% win, `GO_PREMIUM_SELL_INTRADAY` | 85.0% win, `GO_PREMIUM_SELL_INTRADAY` |
| mean PnL open, **gross** | +0.202% | +0.336% |
| mean PnL open, **NET** of 0.1% cost | **+0.102%** | **+0.236%** |

**Override the `sell_premium: true` flag — it is unconditional and must not be taken at face value.** VIX 15.13 sits in the **LOW tercile** (bounds 16.0 / 17.3). Reading `mean_pnl_by_vix_state[LOW]` net of the assumed 0.1% round-trip cost:

- **SPY: 0.06% gross − 0.10% cost = −0.04% — NET NEGATIVE.**
- **QQQ: 0.151% gross − 0.10% cost = +0.05% — marginal.**

The validated edge lives in the MID and HIGH VIX terciles only. `pnl_basis` is percent-of-underlying-spot-notional, **gross** — not premium-collected and not margin-relative, so the headline figures are small in absolute terms and the gross win-rate overstates a negatively skewed seller's edge. There is also a direct conflict with §2: a desk reading SPY's FULLY_NEGATIVE gamma book would not want to be short premium into a short-gamma amplification regime. **Stand aside on SPY. QQQ is marginal at half the already-halved `size_scalar`.** SPY ≈ SPX (validated identical); QQQ is the weaker of the two (the Nasdaq index book is unavailable). This lane stays advisory permanently until a vol-shock day enters the sample **and** net expectancy clears a tail-aware bar — win-rate is explicitly not the promotion metric.

## 2b. Swing Dealer Positioning (1–4 weeks)

**Zero names earn the mechanized +1 DEX-flip line.** All 13 tickers were run through `scripts/dex_flip.py` across the 11 ISO sessions 2026-08-07 → 2026-08-21; every result returned `qualifies: false`.

**No valid vanna-squeeze anywhere.** The dated ^VIX series (raw Yahoo chart API) — 08-14 14.25, 08-17 15.19, 08-18 15.84, 08-19 14.89, 08-20 16.01, 08-21 15.13 — contains **no 3-consecutive-session decline**, so the falling-VIX leg fails market-wide. Put-heavy books that are squeeze-*shaped* (IWM, INTC, AVGO) are flagged as "vanna pressure, not squeeze".

| | SPY | QQQ | IWM |
|---|---|---|---|
| DEX (08-21) | +$24.64B | +$13.94B | +$1.87B |
| 5d trajectory | **−63%** vs 08-14 | **−73%** vs 08-14 | **−83%** vs 08-14 |
| Vanna | SHORT (−18,004, call-heavy) | SHORT (−13,414, call-heavy) | **LONG (+22,611, put-heavy)** |
| front-end ratio @7DTE | 0.854 CONTANGO | 0.914 CONTANGO | — |
| Swing bias | NEUTRAL, cautious | NEUTRAL, cautious | NEUTRAL / watch-for-squeeze-trigger |

All three indices show fast-decaying but still net-positive DEX. A call-heavy vanna book on SPY/QQQ means a falling-IV event would trigger dealer **selling**, not buying.

**Two genuine but stale flips** — informative, explicitly non-scoring:
- **INTC** — genuine sign flip on **08-19** (three consecutive positive priors 08-14/17/18, magnitude cleared the floor). `total_gex` went deeply negative the same day (−67.6M → −634M) while the CLI's regime label *still prints POSITIVE* — the known label/sign contradiction. The most coherent bearish multi-signal setup in the book, and it earns nothing because the flip is not on the latest session.
- **AVGO** — flip on **08-14**, seven sessions stale; negative every session since. FULLY_NEGATIVE gamma 4-of-5 sessions, spot 423 → 368 (−13%) across the window. An established regime, not a fresh signal.

**Flow-vs-book conflicts flagged for Phase 2:** PLTR (persistently call-heavy dealer book against the most bearish net premium in the funnel, −$255.9M) and MU (front-end **1.19 BACKWARDATION, panicked**, on a still-net-positive decaying DEX book with −$116.9M bearish premium underneath). TSLA and LULU both carry `whipsaw_warning: true` (4 sign changes in 11 sessions) and are skipped as noise.

## 2c. Sector Rotation

**`rotation_regime: no_change`, confidence LOW.**

The governing fact today is a headline **netted-vs-gross disagreement**. Direction reads only off the netted `uw risk market-regime.sector_rotation` (a top-3/bottom-3 truncation); `sector-flow` and `sector-flow-persistence` are one **gross-turnover** source, sign-agnostic, and are durability filters that cannot express direction.

| Sector | Netted | Gross | Agreement | Persistence |
|---|---|---|---|---|
| Healthcare | **IN** +$38.0M | +$568.7M | agree | 1.0 |
| Basic Materials | **IN** +$16.6M | +$302.2M | agree | 1.0 |
| Financial Services | **IN** +$15.7M | +$444.4M | agree | 1.0 |
| **Technology** | **OUT −$328.6M** | **+$4,037.1M (#1)** | **DISAGREE** | 0.8 |
| Consumer Cyclical | OUT −$16.3M | +$1,122.1M | **DISAGREE** | 0.8 |
| Consumer Defensive | OUT −$10.9M | +$0.5M | **DISAGREE** | 1.0 |

Sectors outside those six have **no netted direction available** and none was inferred. **Technology is the flagged case: $4.04B of gross churn masking $328.6M of net distribution** → `watch_only`, per the disagreement rule. Consumer Cyclical and Consumer Defensive likewise.

`sector-flow-persistence` fired **INFLOW on 10 of 11 sectors** (six at score 1.0, Utilities ROTATING at 0.6) — the documented near-zero-discrimination failure mode. Used strictly as a durability filter, never as confirmation.

**ETF flow tape (advisory, adds no rubric points).** 21 ranking calls + 12 deep-pulls = 33, under the 40 cap.

| ETF | 5d net flow | Trend | GICS sector | Netted dir | `gics_agreement` | Deep-pull colour |
|---|---|---|---|---|---|---|
| SMH | +$15.76M | MIXED | Technology | OUT | disagree | — |
| **XLK** | +$7.41M | BULLISH | Technology | OUT | **disagree** | Sweeps thin and mixed — does not resolve the conflict |
| **XLV** | +$4.95M | BULLISH | Health Care | **IN** | **agree** | Sweeps call-skewed (0DTE 158c, LEAP 200c/145c). Largest DP print $340.6M at 17:57:38 ET — **closing-cross contamination**, stripped |
| XLY | +$2.34M | BULLISH | Consumer Cyclical | OUT | disagree | All-call sweeps — deepens the churn read |
| KRE | +$1.75M | BULLISH | Fin. Services (regional) | IN | agree | — |
| XLC | +$0.70M | BULLISH | Comm. Services | n/a | agree vs gross | — |
| XLI | −$0.84M | BEARISH | Industrials | n/a | — | — |
| XLU | −$1.48M | BEARISH | Utilities | n/a | — | Confirmed by price: worst sector 1d (−2.28%) and 5d (−3.48%) |
| XLP | −$3.33M | BEARISH | Consumer Defensive | OUT | agrees w/ **netted** | — |
| **XLB** | −$4.89M | BEARISH | Basic Materials | **IN** | **disagree** | — |
| XBI | −$4.99M | BEARISH | Health Care (biotech) | IN | disagree | The Healthcare inflow is large-cap pharma, **not biotech** |
| XOP | −$8.40M | BEARISH | Energy (sub) | n/a | — | Put-dominated sweeps (2027 150p/130p, largest $4.5M) — confirms |
| **XLF** | −$13.91M | BEARISH | Fin. Services | **IN** | **disagree** | Call-heavy sweeps today — single-day countersignal vs a persistent 5d bearish tape |
| EWY | −$13.70M | MIXED | no GICS | n/a | instrument-only | — |
| **GDX** | **−$26.40M** | BEARISH | Basic Materials (gold) | **IN** | **disagree** | Heavy LEAP-dated call buying today (92c/95c/90c/91c) against a persistent 5d bearish tape — emerging reversal to watch |

**Net effect:** **Healthcare is the only sector where netted + gross + representative ETF (XLV) + sweep urgency all triangulate.** Financial Services and Basic Materials clear the GICS-only bar but are **downgraded to `watch_only`** because XLF, XLB and GDX are persistently bearish against the netted-IN read.

**Single-name leaders — the conditional +1 gate, checked explicitly:**

| Name | Sector | (a) persistence ≥0.6 | (b) 30d direction aligned | (c) \|cf30\| ≥ $50M | Verdict |
|---|---|---|---|---|---|
| JNJ | Healthcare | met (1.0) | met (+$32.7M BULLISH) | **FAILED** ($32.7M < $50M) | No |
| MRNA | Healthcare | met (1.0) | **FAILED** (−$24.4M MIXED) | n/a | No |

**Zero names qualify.** MRNA's failure on (b) is independently corroborated by XBI's persistently bearish ETF flow. Note that condition (a) is satisfied by **11 of 11 sectors** and is therefore non-discriminating — (b) and (c) do all the work, which is the documented double-count concern in action.

**Swing-book implication:** no sector-rotation-driven sizing this session. Watch XLV for a qualifying name. The 45.9% 0DTE / RETAIL_DRIVEN overlay downgrades every rotation call uniformly, including the Healthcare read.

---

## 3. Swing Setups (1–6 weeks)

**Nothing is sized.** One name clears the drop floor; it is a directional short and routes to `watch_only`.

### 3a. Long swings (regime-aligned)

**Empty.** No long-side name survived the gate stack.

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **MSTR** | 2 (DROP) | Levered BTC proxy; latest-session OI build is the cleanest long-side build on the board (**96.0% call share**, +104,580 calls), on a ~20%-in-3-days BTC rally | Dec-2028 100C/110C LEAP vertical (~$595M) | Loses the $112.39 prior-session close, or BTC reverses | **`skip`** |
| **GDX** | −1 (DROP) | Aug-28 100–108 call ladder rolling up from 92/95, 104C accreting $1.8M → $9.6M over 2 sessions | Call ladder, Aug-28 | Ladder stops accreting session-over-session | **`skip`** |

**MSTR — why it dies.** The structure is the kill shot: a 100/110 vertical against spot **119.25** is deep ITM on **both** legs, so the convexity a LEAP vertical exists to buy has already been spent — you pay near-max debit for near-max payoff. `multileg-strategist` itself tagged it **ROLL provenance** (near-dated legs expiring the same day), the identical signature it used to *exclude* +2 on XLF, FIGR and PLTR. The Aug-28 build sits at C115/C117/C120/C121/C123 — ATM against a spot that just ran **+6.10% today and +28.17% over five sessions**: a momentum chase, not positioning. cf90 is **−$453.0M against the thesis**. `accumulation-hunter` reviewed it and returned NEUTRAL; `sweep-tracker` reads bearish 3/5. Fundamentals **CAUTION (−1)**: EPS missed by −222.96%, −770.41% and −1517.91% in three of the last four quarters; net margin −6102.96%; **insider selling six consecutive months, continuing straight through the +28% rip**. Sector gate fires (Tech netted-OUT, adverse to a Tech long). Debate gate fires hardest on the board (bear 0.75 vs bull 0.25).

**GDX — the only negative score.** The mechanical `flow_conflict` fires on both formulations: cf30 **−$140.5M** opposes the long thesis at **6.6× the union median**, the tool's own trend label is explicitly BEARISH, and it is −8.27% of gross (a real net imbalance, not churn). Triply corroborated — the tool label, `sector-rotation-strategist`'s independent −$26.4M 5d ETF read, and an OI build that is **put-dominated at 37.2% call share**. GDX ran **+14.29% over five sessions** to 102.83; the accompanying flow is net put-buying and call-ladder rolling. That is hedging and monetising a rally, not initiating one.

### 3b. Short / fade swings (defined risk only)

> **All directional shorts print as `watch_only` (2026-08-01 P0 #1).** This is **routing, not suppression** — theses, structures, invalidations, scores and all nine gate verdicts are generated and serialized so the counterfactual keeps resolving. Short legs inside defined-risk spreads, short-vol structures and an explicit portfolio beta-hedge sleeve are out of scope of the rule.

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **IWM** | **3 (LOW)** | The one genuinely interesting structure on the board — see below | Sep-11 / Sep-18 **282–295 put ladder**, ~$28.3M | Reclaims and holds **above 289** into Sept OPEX; or the ladder fails to add a session / rolls **up** in strike | **`watch_only`** |
| **QQQ** | 2 (DROP) | Dec-18 put spread on a Tech complex showing netted distribution | Dec-18 **725P/650P** (~$64.8M), defined-risk debit vertical | QQQ reclaims 730 (the call wall); or netted Tech flow turns positive | **`skip`** |
| **INTC** | 1 (DROP) | Largest \|cf30\| in the union at −$440.2M, 30d and 90d agree; DEX + GEX both flipped negative 08-19 | Not specified — a directional flow read, not a risk-defined package | cf30 narrows toward flat; or the call-side OI build resolves into price | **`skip`** |

**IWM — the honest tension in today's book.** *For:* a $28.3M put ladder that is **fresh-opening and re-struck lower four sessions running** (08-18 → 08-21), the only 4-session-repeating structure in the entire scan; an **independent** 634,263-contract put-side OI build landing on the *same* strike complex (P285 Sep-11 +55,992, P295 Sep-11 +54,576, P283 Sep-18 +51,452, P285 Sep-18 +23,262, P275 Oct-16 +10,564) with ex-0DTE call share at **9.0% over five days and 3.2% on the latest session**; `uw historical trend --days 10` printing **9 bearish days out of 10**; cf30 −$346.1M at **16× the union median** with cf90 confirming at −$436.8M; put/call ratio 1.842; dated two sessions ahead of a **confirmed FOMC**; and bought at an **IV rank of 6.07 — the cheapest options on the board**.

*Against:* the trend is UP and IWM sits only **−1.71% off its 52-week high and +11.13% above its 200-SMA**; spot 299.96 is pinned on ZGL 299.43 with a $1.75B dealer-long gamma wall at 300; dealer `net_vanna` is **+22,611, put-heavy and squeeze-shaped** (unarmed only because VIX has no 3-session decline); IWM was **today's strongest major index at +0.77%**; and `win_rate` is **null** — `multileg_directional` is not a supported backtest class, so **there is no measured edge here at all**, only a well-formed story.

The bull's own concession is the fair summary: the ladder *"could simply be early and right."* Early and right is not a size.

**QQQ — the deep-dive contradicts its own thesis.** `uw historical trend --days 10` returns **6 bullish days vs 4 bearish**, and today's `flow_direction` is **bullish** at net **+$22.6M** (08-20 was also bullish at +$99.9M). Today's 0DTE tape ran 53–60% ask-side **call**. Against that: the put OI build is overwhelming and one-sided (505,323 puts vs 103,053 calls ex-0DTE, **latest session 0.0% call share**, concentrated at Sep-18 685P +44,751 and 660P +34,107), and the netted Technology outflow is the largest of any sector. The structure repeated only **one** session against IWM's four.

**Near-term sweeps** (`sweep-tracker`, informational — **0 rubric points** since the sweep-persistence line was removed 2026-05-23 after two consecutive −22pp audits):

| Ticker | Side | 5d cum. premium | Persistence | Note |
|---|---|---|---|---|
| SPY | bearish (put) | $5.15B | 5/5 | 0DTE layer is OPEX churn; the **Sep-18 728P at 91.4% ask** (22,289 ask / 2,087 bid) is the genuine print underneath |
| QQQ | bearish | $5.69B | 5/5 | **Today's tape contradicts the week** — 0DTE calls 53–60% ask-side |
| SNDK | bearish | $2.45B | 5/5 | Cleanest non-index bearish persistence; absent from today's OPEX churn |
| SPCX | bearish | $1.30B | 5/5 | Term-structured, not 0DTE |
| AMD | bearish | $1.15B | 5/5 | Consistent with the semis de-rating |
| INTC | bearish | $675M | 4/5 | — |
| MRNA · MSTR | bearish | $1.10B · $764M | 3/5 | Threshold |
| GLD · MRVL | **bullish** | $686M · $346M | 3/5 | Only bullish persistent names ≥3/5 |
| AVGO | bearish sweep vs **bullish** cf30 | $345M | 3/5 | **Demoted to hedge-flow** — the two lenses disagree |

Disqualified as mixed-direction despite 5/5 persistence: **TSLA, MU, NVDA, AAPL**. The market-wide `top_premium_trades` / `most_active` caches were ~100% SPX/NDX index legs and 0DTE OPEX churn — the largest ticket in the tape was a $1.3B SPX 7000-strike call structure spanning Feb-2027 and Sep-2026, a calendar/roll, and out of the C12 universe.

---

## 4. LEAP Builds (6–24 months)

**Nothing qualifies.** This is a clean negative result, not a gap.

`uw oi biggest-increases --min-dte 180` returned 20 rows; **12 of 20 (60%) fall outside the tradeable universe** (QXO, BKLN, TLT, RKT, IOVA, BULL, EEM). Only **IBIT** survives.

`uw oi position-rolls` returned 121 rows. Twelve match the universe (SPCX, XLF, KLAR, AVGO, XLK, SOXX, FIGR, ARM, RGTI, XLI, BA, XLU) and **all twelve are put-side or low-balance**; only KLAR (0.822), SOXX (0.898) and XLI (0.983) clear the 0.7 balance threshold and **all three are put rolls** — de-risking, not a bullish build. None appears in the fresh-opening list, so **there is zero fresh capital behind any of them**: they are August-expiry maintenance, exactly the OPEX artifact anticipated.

**IBIT — disqualification detail:**

| Gate | Result |
|---|---|
| Direction-verified OI build | **FAIL** — `BUILDING` 10 consecutive days, but calls **and** puts build near-equally at the same $45 strike (29,717 call OI vs 24,100 put OI added same day, both ask-heavy). A straddle/collar/AP-hedging signature, not directional |
| 90d cum-flow accretion | **FAIL** — MIXED, net $233.8M against $3.60B bullish / $3.37B gross = **net 3.4% of gross**. Noise, not slow accretion |
| 30d cum-flow | **FAIL** — flips **negative** at −$15.2M |
| Institutional accumulation | **FAIL** — NEUTRAL, buy/sell ratio 1.04 |
| Conviction matrix | **FAIL** — MIXED, confidence **1.1%** against a >70 bar |
| **Gates passed** | **1 of 9** (the bare `BUILDING` label, which is known to fire 14-of-14 and carries no information) |

The put-sale netting check was run as mandated and IBIT's net/gross ratio of 3.4% is precisely what it is designed to catch. Recommend re-running this screen on a non-OPEX session.

---

## 5. Volatility Surface

**The headline finding is substrate, not signal: 18 of 20 names (90%) flipped from their raw term-structure label.** Raw `iv-term-structure` returned BACKWARDATION on **19 of 20**; only SPY and QQQ printed raw CONTANGO. After `scripts/term_structure_hygiene.py` dropped the 0DTE/expired bucket and sub-15-contract tenors:

- **Kink-aware shape:** KINKED 13 · BACKWARDATION 2 (HPQ, DOW — genuine) · FLAT 2 (SKHY, CBRS) · **NO_NEAR_TENOR 3 (NTAP, SRE, RRC — front end unmeasurable, *not* calm)**
- **Monotonic base shape:** CONTANGO 9 · BACKWARDATION 6 · FLAT 2 — meaning **9 of the 13 KINKED names are contango-base with an event bump layered on**, and neither label alone describes them.

Today is the worst-case day for this defect: the `dte_approx: 0` bucket runs **250–860% average IV** on an expiry-day snapshot. `min_contracts=15` is a tunable parameter, **not audit-frozen**, and is reported rather than treated as settled.

**Two substrate lanes are unusable today:**
- **`iv_outliers` — 100% unusable.** All 20 cached rows carry `expiry: 2026-08-21` (today's expiring 0DTE) with zero C12-universe matches. **No single-contract IV outlier signal exists this session.**
- **`iv-percentile-zscore` short-delivered on every name** — `dates_used` maxed at 92 against a 120-day floor (SKHY 28, CBRS 66). **Every percentile below is PROVISIONAL.**

**Genuine dislocations:**

| Ticker | Hygiene shape | Base | Front-end @7DTE | Kink DTE / prominence | Implied move | Structural read |
|---|---|---|---|---|---|---|
| **HPQ** | **BACKWARDATION** (genuine, 14 tenors) | BACKWARDATION | **1.547** — highest in the book | — | **10.1%** | ATM IV 90.8% @7DTE vs 58.7% next month; back-skew 1.032 COMPLACENT; iv_pctile 94.57 (provisional) |
| **SNOW** | KINKED | **CONTANGO** (flipped) | 0.506 | **14 / 23.0%** | **15.0%** | Kink at Sep-4 matches Sep-2 postmarket earnings cleanly. A second hump at 28DTE sits right after the **Sept-16 FOMC** — rate-event risk, not a second earnings signal |
| **MRVL** | BACKWARDATION (genuine) | BACKWARDATION | **1.274** | — | **12.0%** | ATM IV 108.2% @7DTE on the deepest chain in the scan (14,634 contracts); back-skew **−0.0407**, genuinely complacent — the market is pricing *no* tail into a 6-DTE print |
| **LULU** | KINKED | **CONTANGO** (flipped) | 0.698 | **14 / 14.1%** | **11.2%** | An isolated kink on a calm contango base — higher-quality than broad panic. Flow **strongly bearish**, −$54.6M at ~8:1 put premium |
| **NVDA** | KINKED (strong) | CONTANGO (flipped) | **1.392** | 7 / 14.8% | — | Highest-conviction kink+catalyst alignment in the vol scan |
| **SOFI** | KINKED | BACKWARDATION | 0.856 | 28 / **25.3% — highest prominence in the set** | — | **No matching catalyst** — earnings are typically late Oct/Nov. Unexplained at face value |
| **AVGO** | KINKED | CONTANGO (flipped) | 0.818 — front **not** panicked | 14 / 12.7% | **null** | Kink aligns to Sep-2 earnings, but no straddle-derived expected move exists |
| **MU** | KINKED (strong) | CONTANGO (flipped) | 1.19 | 7 / 18.6% | — | Real event premium on a low-percentile base; catalyst date needs confirmation |
| NTAP · SRE · RRC | **NO_NEAR_TENOR** | — | **null** | — | — | Front end **unmeasurable**. A 1.000 ratio here means "no data", never "calm" |

**Earnings verdicts** (6 names survive `earnings_catalyst` ∩ C12): **HPQ CALENDAR** (2026-08-26, 5 DTE) · **MRVL CALENDAR** (2026-08-27, 6 DTE) · **SNOW BUY VOL** (2026-09-02, 12 DTE) · **LULU BUY VOL** (2026-09-03, 13 DTE) · **NTAP SKIP** (chain jumps 0DTE → 28DTE; no straddle quotable at the event) · **DCI SKIP** (best tenor carries 9 contracts).

**Zero SELL VOL calls, and that is the regime-consistent outcome** — QQQ's negative VRP means the Nasdaq complex is a premium-buying environment, and every one of these names carries meaningful Nasdaq beta. HPQ and MRVL route to CALENDAR rather than SELL VOL precisely because their front-end panic (1.547, 1.274) sits far above the 1.10 line while back-month skew is flat-to-complacent — both explicit disqualifiers for aggressive short vol.

**Note:** `uw insights analyst-vs-flow` returned **zero analyst-leg data on all six names** (payload is exactly `{options_flow, symbol}`). The known defect is confirmed live; it contributed nothing and is not presented as agreement or disagreement.

---

## 6. Risk & Correlation

**Macro headline:** stagflationary tint — payrolls **contracting −23k MoM** while core PCE runs **3.29% YoY** above target; 10Y at 4.69 and rising; USD weakening; fed funds 3.63 for a barely positive real policy rate. **Forward calendar:** Core PCE T+5 (2026-08-28), NFP T+10 (09-04), CPI T+13 (09-10), **FOMC + SEP T+17 (2026-09-16, confirmed)**.

**Breadth (advisory):** 332 advancers / 169 decliners, **66% green**, avg +0.59%. Top mover HOOD +13.7%; worst MRVL −5.57%. **No price-breadth divergence** — the green index is confirmed by green breadth (`divergence_flag: false`). The divergence that *does* exist is price-vs-flow: 66% of names green on **39.2% bullish options-flow breadth**. Advisory, does not change sizing.

**Correlation clusters** (`uw risk portfolio-correlation` run against today's nine candidates, not the static watchlist):

**`Nasdaq_semis_beta_cluster` — {IWM, QQQ, INTC, MRVL, AVGO}**

| Pair | corr | Pair | corr |
|---|---|---|---|
| **QQQ / INTC** | **0.870** | QQQ / MRVL | 0.732 |
| **IWM / QQQ** | **0.804** | QQQ / AVGO | 0.715 |
| MRVL / INTC | 0.799 | AVGO / INTC | 0.739 |

Kept member: **IWM** (highest raw_score, 3). QQQ, AVGO, MRVL and INTC each take −1 tier. Structurally, IWM enters this component only through the IWM/QQQ 0.804 edge — its direct correlation to the semis leg is soft (IWM/INTC 0.621). **The board is one Nasdaq-beta bet expressed five ways, and its highest-scored member is a short while three others are long-vol.**

Soft watch, no penalty: MSTR/GDX 0.645 (shared weak-USD driver), IWM/INTC 0.621. Below flag: MSTR/MRVL 0.559, AVGO/MRVL 0.525. **HPQ and SNOW are the only two names carrying no cluster tax** — genuinely idiosyncratic single-name earnings vol.

*Substrate note:* `sector_breakdown` returned `{"Unknown": 9}` with a spurious *"100% concentration in Unknown"* warning — the tool failed to classify every symbol. The warning was ignored as a defect and the Step-0 netted sector map used instead.

**Gates applied.** Panic fired on **4 of 9 measured** (HPQ 1.547, NVDA 1.392, MRVL 1.274, MU 1.19 vs AVGO 0.818, SNOW 0.506, INTC 1.004, SPY 0.854, QQQ 0.914) — the gate is **discriminating today**, not exhibiting its degenerate near-universal firing. Event-risk fired on **3 of 9 (33%)**, with six principled exemptions (four event-plays where the print *is* the thesis, two defined-risk structures). Sector fired only on MSTR — Tech outflow is *adverse* to a Tech long but *aligned* with a Tech short, and firing it on the non-directional vol structures would double-count the VRP gate.

**Fundamentals verdicts (top-5):**

| Ticker | Verdict | Adj | Contradicting facts |
|---|---|---|---|
| **IWM** | **NA — by instrument type** | 0 | Russell 2000 ETF; no per-issuer fundamentals exist. Index context argues **against** the short: −1.71% off 52w high, +11.13% above sma200, dtc 3.06 |
| **QQQ** | **NA — by instrument type** | 0 | Nasdaq-100 ETF. −4.70% off 52w high, +9.29% above sma200, dtc 1.71. NVDA earnings is an ETF-level binary the gate cannot quantify |
| **MSTR** | **CAUTION** | **−1** | EPS miss streak 3-of-4q (−222.96% / −770.41% / −1517.91%); net margin −6102.96%; **insider selling 6 consecutive months** through the +28% rally; −17.16% below sma200; beta 3.56 |
| **AVGO** | CONFIRM | 0 | Revenue +32.29% YoY, EPS +125.78% YoY, GM 68.35%. **Risks:** insider MSPR **−94.62**, near −100 every month since Jan-2025; **~$70B debt-deal headline dated today** — if acquisition financing, pro-forma leverage moves off 0.80 D/E |
| **HPQ** | CONFIRM | 0 | Earnings improving into the print (+19.78%, +4.95%). **Risks:** insider MSPR −50.39; 52w high on 08-14, +31.49% above sma200; **dtc 4.29, highest on the board** |

The distinction between **NA-by-instrument-type** (the two ETFs — no such data can exist) and NA-by-missing-data is recorded explicitly; they are different failures. SNOW, MRVL, INTC and GDX sat outside the top-5 and are marked `NA (gate not run)` rather than as clean CONFIRMs. **Substrate gap:** the `fz` analyst leg (`recom`, target price, upside) was **unrecoverable on all five names** — an upstream gap, not a data-absence signal.

**Debate-disconfirmation.** Semantics: `bull` = residual confidence in the **long-direction** case, `bear` = the **short-direction** case. For a short thesis the bear is the *supporting* side; the gate cuts when the residual **opposing** the thesis direction ≥ the residual **supporting** it.

| Ticker | Thesis dir | bull | bear | Gate |
|---|---|---|---|---|
| IWM | short | 0.35 | 0.55 | no-op — supporting 0.55 > opposing 0.35 |
| QQQ | short | 0.45 | 0.65 | no-op — supporting 0.65 > opposing 0.45 |
| **MSTR** | long | **0.25** | **0.75** | **−1 tier** — widest spread on the board |
| **AVGO** | vol-long | 0.35 | 0.55 | **−1 tier** |
| **HPQ** | vol | 0.35 | 0.65 | **−1 tier** |

No round-2 escalation: no pair was both within one bin and ≥0.75. In all three names the gate cut, **the building agent or the supporting advocate conceded the decisive point against itself** — MSTR's bull volunteered the six-month insider-selling streak; AVGO's bull admitted no `implied_move` exists so "cheap versus merely elevated" is unresolvable; and on HPQ, `earnings-scout` — the agent that *built* the thesis — had already labelled its own entry disqualified (*"front_end 1.547 disqualifies full-size SELL VOL: wait for it to start unwinding"*), while both debaters independently re-pulled `term-skew` at 1.032 NORMAL, confirming the back leg is flat and **half the calendar's economic logic is simply absent**.

**Adverse-flow exit candidates: EMPTY.** The `conviction_2026-08-20` group exists and holds exactly `["IWM"]`. Alerts returned `LARGE_DARK_POOL` (high, **$449,962,208 single trade**), `OI_SHIFT` (high, **+361,659 contracts**) and `LOW_IV_RANK` (medium, 6.07). Scan shows `flow_direction: bearish`, net −$28.19M, P/C **1.842**. **Flow persists in-thesis; it did not reverse — this is corroboration, not an exit.** Two caveats: the $449.96M single dark-pool print is very likely a **basket/program artifact** (yesterday's session carried a documented ~$500M basket print hitting dozens of unrelated names in a 90-second window at almost exactly this notional, on an index ETF) and is stripped from the assessment; and `fz quote-drift` reports **no field changes** for IWM between snapshots — no adverse fundamentals drift.

**Hedge sleeve: $0 notional.** The book's net delta is zero; there is nothing to hedge. A hedge against an empty book is a naked directional macro bet wearing a hedge's clothing. **Conditional recommendation applying only to pre-existing book beta carried from outside this report:** a defined-risk QQQ or SPY put vertical dated past 2026-09-16 (Sep-18 or Oct-16 monthly), 3–5% OTM, debit-financed, **sized strictly to measured net delta**. Not a VIX call ladder — VIX 15.13 sits in the LOW tercile where roll decay is punishing and no gamma is delivered until a shock arrives; the negative-VRP read argues for owning *index* premium (implied cheap against delivered), not *VIX* premium (term structure against you).

One structural observation: the IWM Sep-18 put ladder is **exactly the shape a desk buys as a portfolio hedge** — index puts, below spot, dated two sessions past the FOMC, re-struck lower four sessions running, at the cheapest IV rank on the board. The short-routing rule explicitly exempts an explicit portfolio beta-hedge sleeve. If this desk carried real long beta, IWM's structure would be a legitimate *hedge use* rather than blocked directional short alpha. It is blocked today for the correct reason: **there is no beta to hedge.**

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**EMPTY. No name reached raw_score 7.** The board's maximum is 3.

**Expectancy lens `[advisory — expectancy is not yet a live sizing axis]`** (from `/calibration-audit` 2026-08-15, `phase_3_calibration`):

| Tier | n | Realised WR | Mean P&L | Payoff ratio |
|---|---|---|---|---|
| HIGH | 7 | **0.143** | −2.441% | 0.72 |
| MEDIUM | 19 | 0.526 | +0.104% | 0.948 |
| LOW | 108 | 0.389 | −1.963% | 1.008 |
| DROP | 438 | 0.420 | −2.870% | 0.787 |

Realised order **MEDIUM > DROP > LOW > HIGH** — tier inversion for the **7th consecutive cycle**, present in every era stratum. The C3 Kelly gate remains `ADVISORY_ONLY` (n=27 closed sized calls, below the 30 floor, and tier × expectancy is non-monotone). The live sizer remains the win-rate ladder. Display-only.

### Full audited board (all below the §7 threshold — shown for auditability)

| # | Ticker | Dir | Class | Raw / Tier | `win_rate` (n, source) | `market_excess` | Pre-risk | Gates fired | **Final** |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | short | multileg_directional | **3 / LOW** | null · NA(substrate) | null | watch_only | regime −1, event_risk −1, rubric_regime cap | **`watch_only`** |
| 2 | QQQ | short | multileg_directional | 2 / DROP | null · NA(substrate) | null | skip | regime −1, cluster −1, rubric_regime cap | `skip` |
| 3 | MSTR | long | multileg_directional | 2 / DROP | null · NA(substrate) | null | skip | sector −1, fundamentals −1, debate −1, rubric_regime cap | `skip` |
| 4 | AVGO | vol_long | high_iv_rank | 1 / DROP | **0.60** ceiling-bound (uncapped 0.7877, n=146, `backtest_clean`) | **+0.548 ⚠ benchmark-mismatched** | skip | cluster −1, debate −1, rubric_regime cap | `skip` |
| 5 | HPQ | vol_short | earnings_vol | 1 / DROP | null · NA(substrate) | null | skip | vrp −1, panic −1, debate −1, rubric_regime cap | `skip` |
| 6 | SNOW | vol_long | earnings_vol | 1 / DROP | null · NA(substrate) | null | skip | rubric_regime cap only | `skip` |
| 7 | MRVL | vol_short | earnings_vol | 1 / DROP | null · NA(substrate) | null | skip | vrp −1, panic −1, cluster −1, rubric_regime cap | `skip` |
| 8 | INTC | short | bearish_flow | 1 / DROP | 0.5448 (n=134, `backtest_clean`) | **+0.0075 → beta** | skip | regime −1, cluster −1, event_risk −1, rubric_regime cap | `skip` |
| 9 | GDX | long | multileg_directional | **−1** / DROP | null · NA(substrate) | null | skip | event_risk −1, rubric_regime cap | `skip` |

**Two numbers that must not be misread.** AVGO's **+0.548 market_excess is a benchmark mismatch**, not alpha — it compares a single-name vol class against SPY *realised* vol, and single names are structurally more volatile than the index. The 2026-07-25 C49 finding is that the excess column is ~71% denominator artifact; this is a textbook instance, and the gate no-ops here only because it is downgrade-only. INTC's **+0.0075 is beta** — a 0.75pp edge on n=134 over simply shorting SPY, statistically indistinguishable from nothing — and its **C4 opening gate FAILED**: the OI build is **77% calls against a short thesis**. Passing the *raw* `oi-trend` label would have returned a false `opening_confirmed: true`; direction-verification reversed it.

**Substrate finding worth registering: seven of nine rows are `NA(substrate)`.** `earnings_vol` and `multileg_directional` — the two classes carrying today's entire book — are both outside the five `--signal-type` values the CLI accepts. **The desk currently cannot measure a win rate for either of its two most productive signal generators.**

### Conviction scoring rubric (frozen, version `2026-06-12`) — embedded verbatim for audit

```
Daily conviction score = Σ:
  +1  MECHANIZED DEX flip or vanna-squeeze in trade direction (verified SIGN CHANGE on the
      LATEST session vs ≥3 consecutive prior sessions, |net_dex| ≥ 0.25× trailing-10 median;
      computed by scripts/dex_flip.py, never by hand)
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified
      institutional-tier confirmed) — CONJUNCTION (C11): full +3 only when cum_flow_30d confirms
      (sign aligned AND |cum_flow_30d| ≥ $50M); else halved to +1
  +1  multi-day OI build (oi-trend BUILDING, --days ≥ 5) — award only on a DIRECTION-VERIFIED build
  +1  conviction-matrix DIRECTIONAL_LONG confidence > 70 — CONDITIONAL: only when
      dominant_signal_class == leap_directional
  +1  cumulative-premium-flow net directional accretion (30d) — INTENT-SCREENED (no C28
      distribution_flag; not dividend-capture deep-ITM sub-parity calls in an ex-div window)
  +1  sector-rotation single-name leader — CONDITIONAL on ALL of (a) persistence ≥ 0.6,
      (b) cum_flow_30d direction aligned, (c) |cum_flow_30d| ≥ $50M
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored play type)
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner overcrowded long with RISING pc-ratio-zscore (VRP positive) — an
      INFORMED-FLOW CONTINUATION penalty, not a "fade the crowd" signal
  -3  flow_conflict — cum-flow 30d direction clearly OPPOSITE dominant_signal_class
  -1  flow_conflict_lite — 30d cum-flow read is MIXED
      (flow_conflict and flow_conflict_lite are MUTUALLY EXCLUSIVE — apply ONE, never both)
  # NOT score_components — risk-monitor TIER gates in 2d, contributing 0 to raw_score:
  -1  [TIER GATE] correlation cluster (pairwise corr ≥ 0.70) — −1 TIER
  -3  [TIER GATE] market-regime conflicts with trade direction — −1 TIER
# REMOVED: sweep-persistence +1 (2026-05-23 P0.3, −22pp × 2 audits);
#          signal-confluence ≥4 +2 (2026-06-12 P0.2, re-count of already-scored quantities)

Tiers: ≥9 HIGH (full) | 7–8 MEDIUM (half) | 3–6 LOW (starter/watch) | ≤2 DROP
```

**Rubric lines that scored 0 across the entire board today, with cause:**

| Line | Why |
|---|---|
| +1 DEX flip / vanna-squeeze | `qualifies: false` on all 13 names across 11 sessions. Only genuine flips are stale (INTC 08-19, AVGO 08-14). No 3-session VIX decline anywhere → vanna leg fails market-wide |
| +3 accumulation conjunction | `accumulation-hunter` cleared **no** ticker at the ≥3-signal bar after decontamination. **The C11 conjunction gate was never reached — it had no candidate to test** |
| +1 conviction-matrix | LEAP-conditional; `leap_directional` is not the dominant class on any row. IBIT's confidence was 1.1% vs a >70 bar |
| +1 sector leader | Zero names qualified — JNJ failed (c), MRNA failed (b). Condition (a) is satisfied by 11 of 11 sectors and is non-discriminating |
| +1 opex-pin top-5 | No forward-tradeable book exists (see below) |
| **−2 overcrowded long** | **UNEVALUABLE, not zero-by-measurement.** Zero ±2σ extremes across 34 tickers (closest GEV −1.906, AVGO −1.855). `pc-ratio-zscore` has **no `--date` flag**, so `z_trajectory_available = false` universally and the RISING condition cannot be tested at all. Not applied speculatively |

---

## 8. Watch-only — single signal, no confluence

Surfaced by exactly one Phase 1 agent; failed the ≥2-agent confluence gate. **Journaling only — not for trade entry today.**

| Ticker | Sole flagging agent | Signal |
|---|---|---|
| **LULU** | earnings-scout | BUY VOL, kink 14DTE/Sep-4 prom 14.1%, implied move 11.2%, flow **strongly bearish −$54.6M at ~8:1 put premium** |
| **NVDA** | vol-surface-scout | KINKED, front_end **1.392**, highest-conviction kink+catalyst in the vol scan — but `sweep-tracker` explicitly **disqualified** it as mixed/no-thesis |
| **MU** | vol-surface-scout | KINKED prom 18.6%, front-end 1.19 panicked — but `accumulation-hunter` **invalidated** it (OI put-dominated 1,342c/2,451p, cum-flow 5d −$358.2M, C28 flag present) |
| **SOFI** | vol-surface-scout | **Highest kink prominence in the entire population (25.3%)** with **no matching catalyst** — earnings are typically late Oct/Nov. Unexplained; worth a follow-up |
| **COIN** | accumulation-hunter | 2 of 3 legs decontamination-clean (OI 31,614c/4,949p at DTE-7; cum-flow +$55.8M) but the DP leg is closing-cross contaminated. Second-tier shelf $182.71 |
| SNDK · SPCX · AMD | sweep-tracker | Bearish 5/5 persistence each |
| GLD | sweep-tracker | Bullish 3/5 persistence |
| MRNA | sweep-tracker | Bearish 3/5; also failed the sector-leader gate on (b) |
| JNJ | sector-rotation-strategist | Healthcare leader candidate; failed gate (c) at $32.7M < $50M |
| CG · GEO | multileg-strategist | Term-structure-anchored +2 structures but **1 session only**; CG additionally carries a −$11.0M bearish funnel flow conflict |
| KLAR | vol-surface-scout | Marginal calendar candidate, kink at the prominence floor (5.6%) |
| XLF | multileg-strategist | Aug-21 → Sep-18 50C **identical-strike roll** (FOMC-anchored hold, no new information); sector `watch_only` |
| PLTR | multileg-strategist | Legacy deep-ITM 35C roll that **contradicts** PLTR's −$255.9M bearish tape; vol surface shows no edge (skew 0.999) |
| HUT | accumulation-hunter | Naive label says ACCUMULATION; reads as **DISTRIBUTION** — price −8.79%, OI put-dominated, cum-flow BEARISH −$7.6M, C28 call-closing $696K |
| SRE | vol-surface-scout | NO_NEAR_TENOR (front unmeasurable), skew 1.126 TAIL_HEDGING, ivr 89.7, bearish confluence score 5 |
| NTAP · DCI | earnings-scout | Both **SKIP on measurability**, not vol judgement — a third of this cycle's C12-liquid earnings candidates have unmeasurable event vol at the CLI's 15-contract floor |

**OPEX pin book — no forward-tradeable candidates.** `uw oi pin-risk` has **no expiry-selection flag** (only `--dte-max`, `--max-distance-pct`, `--min-total-oi`, `--top-n`, `--date`), so it returns the nearest expiry per ticker and all 20 top rows came back `dte_to_opex: 0` — today's expiring monthlies. `uw oi opex-concentration` scanned 100 rows and surfaced exactly **one** non-today candidate in the universe: **DCI, 2026-09-18, strike 90, 3.44% away, total OI 1,976** — disqualified on both distance and liquidity. A diagnostic worth recording: today's "pins" were **never gamma-enforced** — SPY's 750 strike carries net_gex ≈ **−47M** and QQQ's 700 ≈ **−71M**. Both are short-gamma, not walls, which is exactly the documented `nearest_high_oi_strike` trap.

**Post-expiry structural consequence.** OI draining at today's close (±5% of spot, front monthly): SPY 5,262,187 · QQQ 3,823,253 · IWM 3,004,994 · NVDA 2,245,708 · XLF 1,667,989 · AAPL 1,241,067 · GLD 1,211,268. Against that, `expiry_heatmap` shows the **2026-09-18 monthly already at $7.21B** versus today's expiring $6.56B, and the 2026-08-28 weekly at $2.58B — so the forward book is **not thin in aggregate; September has already out-built the expiring cycle.** What it lacks is *concentration*: none of it has piled into a single near-the-money strike hard enough to register. Tonight's roll removes a large **short-gamma** pocket near spot on SPY (750/765) and QQQ (700) that was **amplifying** moves rather than pinning them, so its removal costs no real pin — it clears hedging noise. Expect the post-OPEX gamma profile to open **flatter and less pin-prone** into early next week, historically associated with wider realised range, until fresh near-dated OI concentrates over the next few sessions.

---

*Rubric version `2026-06-12` (frozen). Envelope `schema_version 1.3`. All 22 Step-0 market-wide payloads served from cache (zero failures). C12 liquidity floor: 77 of 87 names passed; 10 dropped (SWBI $6.1M, MNSO $7.9M, PENN $49.9M, TDOC $41.0M, MRVI $25.3M, OMER $39.4M, TX $37.8M, SNDX $27.0M, HYMC $44.5M ADV; ^VIX index, no share volume).*
