# Weekly Market Intelligence — Week of 2026-07-20 (ISO 2026-W30)

## Executive Summary

- **Week regime + WoW Δ:** TRANSITIONAL / CHOPPY **held** Monday to Friday — no regime flip, but the internals deteriorated: bullish-flow breadth slipped 34.1% → 33.0%, and SPY closed 738.93, below both its 20-day (746.15) and 50-day (745.07) SMA for the second consecutive week. VRP is **FAIR/NEUTRAL** on both indices (SPY +0.0177, QQQ −0.0138) — IV ≈ realised, so there is no premium-selling or premium-buying edge at the index level this week.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL/CHOPPY) — sizing capped at half`.
- **Signal performance:** **1 of 4 resolved (hit rate 0/1 = 0%); 3 INCONCLUSIVE excluded; 4 total calls in universe (4 from envelopes, 0 reconstructed).** The single resolved non-DROP call — MU long, 07-23 — was a **LOSS** (−6.99%, 0.97×ATR against thesis). It was sized `watch_only`, so no capital was lost. See §0 for the supplementary DROP-discipline check, which is the more informative read this week.
- **Top swing build for next week:** **INTC short** — starter size, **defined-risk structure mandated**. Invalidation: a daily close back above the **$95.95–$97.00** dark-pool supply shelf. `win_rate` 0.5985 (n=132, `backtest_clean`), `market_excess` +0.0379. Tier LOW.
- **Top LEAP build:** **None.** Zero of seven candidates cleared 6-of-9 gates; every ticker tested returned `trend_direction: MIXED` on cumulative premium flow.
- **Biggest emerging risk:** **The event stack, not a correlation cluster.** FOMC lands T+2 (07-29), Q2 GDP + Core PCE T+3 (07-30), and MSFT+META (07-29 post) plus AAPL+AMZN (07-30 post) — the four largest index weights — print inside 48 hours, straddling both macro releases. Secondarily, INTC/TSLA correlate at **0.964**, which is why only one of the two is sized.

> **The 20-week empty-board streak ends this week, narrowly.** One name — INTC — survives the full gate stack at starter size. That is not a conviction call; it is the first time in five months that a name has cleared scoring, fundamentals, debate, and risk simultaneously.

---

## 0. Week in Review — Intra-Week Signal Performance

**Universe:** the union of `calls[]` across this week's five daily `decision.json` envelopes — the only hindsight-free record of what was actually committed. All five envelopes exist, so **nothing was reconstructed**. 58 total calls; **4 non-DROP**.

Resolution runs from each call's own envelope date forward to 2026-07-24. Grade threshold is 0.5 × ATR(14) measured as-of the call date.

### Primary scorecard — non-DROP calls

| Ticker | Direction | Source | Move vs ATR | Flow/OI | Grade | Note |
|---|---|---|---|---|---|---|
| MU | long | envelope 07-23 | −6.99%, **−0.97×ATR** | 30d cum-flow +$725M (bullish, against a long that still lost); Friday's tape flipped to ask-side put buying | **LOSS** | Only call all week with a forward window. Sized `watch_only` — no capital at risk. |
| TSLA | short | envelope 07-24 | 0.00%, 0.00×ATR | — | INCONCLUSIVE | 0 forward sessions (called on week-end) |
| AKAM | vol_short | envelope 07-24 | 0.00%, 0.00×ATR | — | INCONCLUSIVE | 0 forward sessions |
| FSLR | vol_short | envelope 07-24 | 0.00%, 0.00×ATR | — | INCONCLUSIVE | 0 forward sessions |

**Headline: 1 of 4 resolved (hit rate 0/1 = 0%); 3 INCONCLUSIVE excluded; 4 total in universe (4 envelope-anchored, 0 reconstructed).** A denominator of one carries no information. The board was empty by construction, so the primary scorecard cannot say much — which is precisely why the supplementary check below matters.

### Supplementary — DROP-pile discipline check (n=31 directional DROP calls, 14 resolved)

This is not part of the formal scorecard; it grades what the desk *declined* to trade, the way `/calibration-audit` does. It is the informative result this week.

| Side | Record | Hit rate |
|---|---|---|
| **LONG** | 1W / 10L | **9.1%** |
| **SHORT** | 4W / 0L | **100%** |

Every loss was a long. Every short that resolved, won — and **all four short wins carried `dominant_signal_class: bearish_flow`**:

| Call | Date | Move | ×ATR | Grade |
|---|---|---|---|---|
| GOOG short | 07-22 | −6.67% | −2.13 | WIN |
| SNDK short | 07-23 | −10.79% | −0.95 | WIN |
| SMH short | 07-21 | −3.92% | −0.81 | WIN |
| ORCL short | 07-23 | −4.21% | −0.77 | WIN |
| JPM long | 07-22 | +1.44% | +0.64 | WIN (only long win) |
| SHOP long | 07-20 | −8.62% | −1.82 | LOSS |
| NBIS long | 07-21 | −13.44% | −1.19 | LOSS |
| MU long | 07-23 | −6.99% | −0.97 | LOSS |
| DRAM long | 07-22 | −7.91% | −0.90 | LOSS |
| AMD long | 07-22 | −5.50% | −0.79 | LOSS |
| TLT long | 07-21 | −0.49% | −0.76 | LOSS |
| NVDA long | 07-22 | −2.46% | −0.70 | LOSS |
| LULU long | 07-20 | −2.05% | −0.58 | LOSS |
| SPCX long | 07-20 | −3.99% | −0.54 | LOSS |

**Read this honestly.** n=15 with heavy cross-correlation — the losses are almost entirely one tech/semis complex in one selloff. This is approximately **one tape event, not fifteen independent trials.** The DROP pile's 35.7% directional hit rate means dropping was correct on aggregate; that is a different (and weaker) claim than "the desk has short alpha."

What it does establish, for the seventh consecutive window, is that **the frozen rubric is long-biased and structurally under-scores `bearish_flow`** — the class that has now won repeatedly while contributing zero dedicated scored points (it accrues only toward criterion C19). The rubric's large positive lines (+3 accumulation conjunction, +2 LEAP rolls, +1 conviction-matrix) are all long-shaped. That is a documented limitation for the next calibration audit, not a licence to retune under the freeze.

---

## 1. Regime & WoW Delta

The week opened and closed in the same place — **TRANSITIONAL / CHOPPY**, `uw risk market-regime` guidance "half position sizes, favour defined-risk strategies, iron condors in range" — but that stability masks a deteriorating tape. Bullish-flow tickers fell from 2,140 to 2,074 against 4,135 → 4,215 bearish, dragging breadth from 34.1% to 33.0%. SPY spent the entire week beneath both its 20- and 50-day moving averages, finishing 2.82% below its 90-day high. This is the second consecutive week in a genuine non-uptrend tape, and the first time in months the desk has had two such weeks back to back.

**A methodological caution worth recording:** `uw risk market-regime` returned an **identical `spy` price block** (738.93, SMA20 746.15, SMA50 745.07) for both 2026-07-20 and 2026-07-24. The tool appears to return current spot regardless of `--date`. Do not read a week-over-week price delta off it; the breadth sub-fields *do* vary correctly by date, and dated prices must come from `uw historical trend` or `scripts/market_data.py`.

**Volatility.** VRP is FAIR on both indices — SPY +0.0177 (IV30 15.34% vs RV 13.57%), QQQ −0.0138 (IV30 26.19% vs RV 27.57%). The tool's own verdict is "IV close to realised — no clear edge from VRP alone", and it is right. The QQQ side being marginally negative was enough to force contrarian-scanner to abort its entire fade book. VIX finished at 18.58, having spiked +2.06 on 07-23 and never given it back — the trailing three sessions ran 16.64 → 18.70 → 18.58, i.e. **rising then flat**, which is why zero vanna squeezes qualified this week.

**Institutional vs retail share.** `uw options-flow dte-volume-share` at MARKET level reads BALANCED: weeklies 24.1%, monthlies 13.8%, LEAPs 2.1%. The reported `share_0dte` of 0.0 is a data quirk, not a real zero — do not lean on it in either direction. No uniform conviction upgrade or downgrade applies.

**Macro backdrop** (`scripts/fred_macro.py`): the curve is normal at +36bp (10Y 4.71%, 2Y 4.37%), but **core PCE is running 3.41% YoY — above core CPI at 2.81%**, meaning the Fed's own preferred gauge is the hotter of the two. The 10Y has added 21bp over 30 days, the 2Y the same (a parallel shift), the broad dollar is strengthening, and payrolls printed a soft +57k with unemployment at 4.2%. Fed funds sit at 3.63% effective (target 3.50–3.75%), held through multiple 2026 meetings on above-target PCE.

That combination — sticky inflation, rising long rates, a firm dollar, softening labour — is a stagflation-lite backdrop, and it argues directly against adding beta-long duration risk here. It is also a genuine headwind for LEAP-length bets on high-multiple names, since rising long rates compress the present value of long-duration equity claims.

**Forward event risk (next two weeks):**

| Date | Event | Impact |
|---|---|---|
| 07-28 | US Consumer Confidence (Conference Board) | medium |
| **07-29** | **FOMC decision 2:00pm ET + Powell presser. No SEP / no dot plot at this meeting.** | **high** |
| **07-30** | **Q2 GDP (advance) + PCE / Core PCE + initial claims, 8:30am ET** | **high** |
| 07-31 | Employment Cost Index | medium |
| 07-29 / 07-30 | **MSFT + META (07-29 post), AAPL + AMZN (07-30 post)** — four largest index weights inside 48 hours | high |
| 08-07 | Nonfarm Payrolls | high |

**Implication for next week's bias:** this is the densest event stack of the quarter. Any swing position carried into 07-29/07-30 is implicitly a macro position as well as a single-name one, and the IV being sold or bought is priced for both. Defined risk is not a stylistic preference this week — it is the only structurally sound way to hold anything through it.

---

## 2. Sector Rotation

**Rotation regime call: `no_change`. Confidence: LOW.**

The honest answer is that there was no clean GICS sector rotation this week. What actually happened was a **cap-weight versus equal-weight split** that manifests *inside* sectors as bifurcation rather than *between* them as rotation. Equal-weight breadth on Friday was 72.2% green (363 advancers vs 140 decliners, median +0.97%) while cap-weighted SPY closed below both its moving averages with only 33% bullish flow tickers. That is rotation out of the mega-cap index leaders into the broad market — **not broad distribution, and not broad risk-on**.

### The Technology contradiction — resolved

Two `uw` tools flatly disagreed about the most important sector of the week, and the resolution is worth recording because it changes how a core tool should be read.

- `uw options-flow sector-flow-persistence` reported Technology as **INFLOW, persistence 1.0, +$966.7M** on 07-24 — positive every single day.
- `uw risk market-regime`'s own `sector_rotation` block reported Technology as **money flowing OUT, −$392.5M** on the same date.

`sector-rotation-strategist` resolved this by exact arithmetic. The persistence tool's `net_flow` equals `total_premium_call − total_premium_put` — verified to the dollar: $5,696,361,467 − $4,729,697,393 = $966,664,074. **That is a raw, sign-agnostic gross call-dollar-vs-put-dollar skew.** It does not classify whether contracts were bought or sold, opened or closed. Heavy call-side turnover — covered-call writing, spread legs, market-maker inventory, or simply the higher notional of mega-cap call books — reads as "inflow" even when nobody is accumulating.

The market-regime figure, by contrast, is aggressor-*classified* net premium, using the same methodology as the screener's own `bullish_premium − bearish_premium` (verified exactly on AAPL: $281.8M − $250.6M = $31.19M). Reconstructing the classified figure across the 17 largest Technology movers nets to **−$296.0M** — the same sign and order of magnitude as market-regime's −$392.5M, and corroborated by the price tape (META −7.87%, GOOGL −7.79%, ORCL −9.03%, PLTR −7.15%, AMZN −6.12% on the week).

**Verdict: Technology saw net distribution this week.** The "+$966M inflow, persistence 1.0" headline measures turnover, not accumulation. Technology is a **bifurcated tape** — a narrow long leg against a broad, gate-confirmed short leg.

A second structural problem: **9 of 11 sectors tied at `persistence_score` 1.0**, so the absolute ≥0.6 gate is again non-discriminating. Signal had to be recovered by filtering on magnitude above the cross-sector median ($77.97M, Energy).

### Per-sector detail and gate-confirmed leaders

The sector-leader +1 requires all three of: `persistence_score` ≥ 0.6, `cum_flow_30d` aligned with thesis, and `|cum_flow_30d|` ≥ $50M.

| Sector | Trend | Persistence | Gate-confirmed leaders |
|---|---|---|---|
| **Technology** | bifurcated (contested) | 1.0 | **Long:** IBM (+$61.8M), CBRS (+$92.0M). **Short:** INTC (−$801.4M), ORCL (−$243.5M), AMD (−$137.2M), TSM (−$59.4M) |
| **Consumer Cyclical** | ROTATING | 0.6 | **Short:** TSLA (−$562.4M) — but idiosyncratic, see below |
| **Industrials** | OUTFLOW | 0.8 | **Short:** BE (−$219.1M). XLI ETF tape agrees |
| **Financial Services** | INFLOW (artifact) | 1.0 | **None** — see below |
| **Healthcare** | INFLOW | 1.0 | **None** — LLY (+$25.5M) and SMMT (+$8.4M) both fail magnitude |

Three failures worth naming explicitly:

- **MU (+$725.1M) and SNDK (+$785.4M)** both carry 30-day flow running *opposite* their bearish single-day tags — **flow-conflict, do not short**, despite both firing mechanized DEX flips.
- **Financial Services' "inflow" is a GICS mis-tag artifact.** The screener files WULF and HUT — crypto-mining names — under Financial Services, inflating the bucket away from genuine bank/insurance flow. Zero leaders clear the gate, and the XLF ETF tape disagrees (−$2.19M against +$145.1M GICS). Downgraded to appendix.
- **Consumer Cyclical's outflow is TSLA-idiosyncratic, not sector-wide.** AMZN and LULU show no confirming pattern, and **XLY itself is bullish (+$15.08M)**, disagreeing with the GICS outflow. The analyst who produced the +1 for TSLA explicitly disclaims the sector reading behind it.

### ETF flow tape (advisory — 0 rubric points)

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| **SMH** | inflow +$106.2M | BULLISH 5d | $50.4M block at 21:52Z — closing-cross-timed, not accumulation | Large OTM put sweeps ($55.5M/$43.2M/$37.3M, mostly `no_side`) — **hedging tell** | agree (weak) | see Technology |
| **IGV** | inflow +$17.2M | BULLISH 5d | $61.25M block near VWAP (creation-unit consistent); one print shows a stale-NBBO anomaly, discarded | **Genuine ask-side call sweep, $19.27M — real directional urgency** | **agree (strong)** | best-corroborated ETF of the week |
| **XLY** | inflow +$15.1M | BULLISH 5d | Two large closing blocks | Minimal — no urgency | **DISAGREE** vs Consumer Cyclical GICS outflow | confirms TSLA is idiosyncratic |
| **XLE** | outflow −$16.1M | BEARISH 5d | NBBO-anomalous block, discount | Modest mixed-side put hedging | disagree (Energy at-median anyway) | — |
| **EWY** | outflow −$8.0M | MIXED 5d | Largest block of the six ($89.2M); second print stale-NBBO — **third occurrence** | Moderate OTM put hedging across 4 expiries | n/a (no GICS map) | — |
| **XBI** | outflow −$5.7M | BEARISH 5d | Clean, modest | Small, near-noise | disagree (weak) | — |
| **XLI** | outflow −$3.1M | BEARISH 5d | rank-only | rank-only | **agree — corroborates Industrials rotation-out** | BE |
| **XLF** | mixed −$2.2M | MIXED 5d | rank-only | rank-only | **disagree — undercuts the Financial Services inflow** | — |
| XLK / XLV | mixed | weak | rank-only | rank-only | agree (immaterial magnitude) | — |
| XLU/XLP/XLB/XLRE/XOP/KRE/ITB/GDX/EWT/TAN | mixed | all <$2M | — | — | immaterial | — |

The **stale-NBBO artifact appeared three times** in a single pass (IGV, XLE, EWY — bid/ask inversions like EWY's bid $158 vs ask $163.50). That is systemic, not incidental, and it should be registered.

**Next-week narrative and swing-book implication.** No sector-wide rotation trade is available to size. Macro (core PCE above core CPI, 10Y rising, USD firm, payrolls soft) argues for a defensive lean, but the flow data does not yet confirm one with tradeable size. The only individually gate-confirmed, persistence-backed shorts are BE and TSLA — and BE is VETO'd on fundamentals while TSLA is deduplicated by correlation. Technology is best expressed as a **pair** (long IBM/CBRS vs short AMD/ORCL/INTC/TSM) rather than as a directional sector bet, and explicitly **not** by shorting MU or SNDK.

---

## 3. Swing Book (1–6 weeks)

### 3a. Long swings — **EMPTY**

No long cleared the confluence gate with a survivable fundamentals verdict. IBM was the only two-agent long and it was gated to `skip` (see §8).

### 3b. Short / fade swings — defined risk only

| Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure | Invalidation |
|---|---|---|---|---|---|---|---|
| **INTC** | LOW | 6 | 0.5985 (n=132, `backtest_clean`), excess +0.0379 | **starter, defined-risk mandated** | Cleanest short mechanics on the board: mechanized DEX sign-flip at 6.35× the magnitude floor with `whipsaw_warning` FALSE, the largest aligned 30-day bearish accretion in the union (−$801.4M), Technology short-leg gate passed, and — uniquely — **earnings already behind it** (printed 07-23, next print 89 days out) | Debit put vertical, **August tenor**. Playbook independently flags `has_edge: true` and prefers a bear *call* credit spread at iv_rank 70.97 — noted as a conflict, see below | **Daily close above the $95.95–$97.00 dark-pool supply shelf** (97.00 @ $17.4M, 96.00 @ $16.8M, 96.20 @ $14.0M, 95.95 @ $13.1M) |
| TSLA | LOW | 5 | 0.5985 (n=132) | **watch_only** (deduped) | Consumer Cyclical outflow −$562.4M, P/C z-score crossed BEARISH_EXTREME (+2.22) Friday on 1.9M puts, fundamentals CONFIRM on a real −35.33% EPS miss | — | Close above the **315.24 / 318.34** dark-pool prints ($16.7M / $16.9M) |

**Structure conflict, stated rather than buried.** `uw playbook batch-scan` recommends a **bear call credit spread** on INTC, reasoning that IV is elevated (iv_rank 70.97) and flow is bearish — i.e. sell the rich vol rather than buy it. Risk-monitor mandated a **debit put vertical**. Both are defined-risk, so both satisfy the event-risk exemption. The genuine trade-off: a credit spread is short vega and profits if IV crushes post-FOMC even on a flat tape, but it caps upside at the credit; a debit vertical pays the directional thesis but bleeds if price stalls and IV mean-reverts from 70.97. The desk convention is to prefer the structural read over the playbook heuristic, so the debit vertical stands — but at iv_rank 71 into a vol-crush catalyst, **the playbook's objection is substantive and a practitioner may reasonably prefer the credit structure.**

**Distribution caution (C28):** no long name in the book carries a `distribution_flag`. COPX (watch-only, §10) carries an immaterial one — a $543k 0DTE same-day-expiry call closure, mechanical expiry, not a conviction unwind.

---

## 4. LEAP Book (6–24 months) — **EMPTY**

Zero candidates cleared 6-of-9 gates.

| Ticker | Gates passed | Fatal gate(s) | Note |
|---|---|---|---|
| WULF | 2/9 | #4 (cum-flow **net bearish** −$49.7M/30d, −$87.1M/90d), #7, #8 | Best fresh-LEAP-OI recurrence in the pool, but flow runs the wrong way against a −27% 5-day decline; a competing Jan-28 $15 put build reads as a hedge overlay |
| MU | ~1/9 | #3 (0 rolls), #4 (flat/MIXED flow), #7 (NEUTRAL), #8 (MIXED, 5.9%) | LEAP OI is scattered deep-OTM lottery strikes ($1,180 and $2,500 against $866–921 spot) |
| NFLX | 0/9 | Non-directional at gate 2, #4 | Matched call+put build at the identical $75 strike, DTE 875 — a long-dated straddle, not a directional LEAP |
| NVDA / ORCL / IREN / AMZN | not deep-dived | #4 (all MIXED, near-zero or negative net) | REQUIRED gate fails before further work is justified |

**A finding worth registering:** **every ticker tested — 7 of 7 — returned `trend_direction: MIXED`** with net flow amounting to a rounding error against gross two-way notional. That is either a genuine reflection of the CHOPPY regime (no name seeing coherent net accretion in either direction) or evidence that the tool's MIXED threshold is simply very tight on high-notional liquid names. The data cannot distinguish these. Either way, **the LEAP-grade slow-accretion signature is absent everywhere in this week's funnel**, and the rising-10Y backdrop argues against fighting that with a fresh long-duration long.

---

## 5. Volatility Surface — WoW Term Structure & Skew Evolution

**The headline is a measurement finding, and it is the most important thing in this section.**

The raw `uw options-structure iv-term-structure` label read **BACKWARDATION on 26 of 26 names on 07-24 — 100% saturated** (every name dropped an expired `dte -1` bucket), against 24 of 26 on 07-20. A naive week-over-week diff of raw labels would therefore report only 2 changes and conclude "nothing moved". **The raw label cannot move and is uninformative in both directions.**

Running both snapshots through `scripts/term_structure_hygiene.py` recovers the real picture:

| Metric | Changed / 26 | Read |
|---|---|---|
| Raw label WoW | 2 | Near-meaningless — saturated |
| **`base_shape`** (monotonic) WoW | **7** | AMD, DELL, NBIS, ONON, QQQ, SNDK, VRTX — genuine slope changes |
| **Kink-aware `shape`** WoW | **10** | IWM, NBIS, NVDA, ONON, QQQ, SNDK, SOXX, SPY, TSM, VLO |

`multileg-strategist` independently found 15 of 18 names flipped versus their raw label. This is the same defect that motivated the hygiene script (39-of-41 on 07-24 in the daily fleet), now in its most extreme form. **Never difference raw labels.**

**Event vol is correctly priced, not dislocated.** The index kinks land exactly on the macro calendar — SPY at 13 DTE (08-07, NFP), QQQ at 34 DTE, IWM at 6 DTE (07-31, the day after FOMC and PCE). Front-end ratios are rising into the prints on BSX (1.33→1.50), FTNT (1.37→1.55) and BE (1.39→1.43). This is event premium building correctly ahead of a known catalyst. **Do not fade it** — a "rich front end" this week is the market pricing FOMC + GDP + PCE + four mega-cap prints, and it is right to do so.

**Calendar candidates — one.** Only **IREN** cleanly clears the gate: BACKWARDATION both weeks, no earnings-catalyst match, front-end ratio **falling** 1.106 → 1.047 (panic resolving). ONON, TSM and SOXX are all disqualified — ONON's ratio is *rising* (0.865 → 0.937, panic still building), and TSM's and SOXX's readings are mixed or rest on thin tenors.

**Notable de-risking:**
- **NBIS** lost its kink entirely (KINKED @27d, 6.6% prominence → FLAT) with earnings still ~13 days out; front-end IV compressed 179% → 168%. Event premium is cooling *ahead of schedule* — pointing opposite to the bearish flow thesis on the name.
- **META**'s front-end ratio compressed sharply (1.466 → 1.162) even as its 07-29 earnings drew closer. Unusual; flagged.
- **TSM**'s front-end ratio fell hard (1.310 → 1.093) while a **new 13.8%-prominence kink appeared at 20 DTE (08-14) with no catalyst match**. Neither a clean event story nor a clean calendar story. Flagged, not sized — and it contributed to the decision not to trade TSM.
- **ORCL** carries a **65.1%-prominence kink at 2026-08-21 on a thick 12,374-contract tenor** (IV 1.126 against 0.680 and 0.682 either side). That is the largest term-structure anomaly across all 18 names classified — an order of magnitude above the next (MU 24.7%, AMZN 15.8%, SMH 13.3%) — and **ORCL has no scheduled earnings in that window**. Something binary is being priced into 08-21 that this fleet has not identified. The fundamentals news pass did not resolve it either. **Treat as unresolved risk in both directions; do not size ORCL through 08-21 without an explanation.**

**Single-contract IV outliers: none.** The entire cached outlier list (ALT, HTZ, PURR, BBAI, GRAB, MPT) is sub-$2-strike penny-option noise failing the C12 liquidity floor.

**Substrate caveat:** `uw historical iv-percentile-zscore --lookback-days 252` returned `dates_used: 72` for **all 26 names with no exceptions** — a global data-availability cap (~72 trading days in the source parquet), not a per-ticker gap. **Every IV percentile and z-score in this report is PROVISIONAL**, well under the 120-day first-class bar.

---

## 6. Earnings — Recap & 2-Week Lookahead

### (a) Recap — what actually printed inside the covered week

Only **two** of the eleven names carrying vol theses in the week's daily envelopes actually reported before Friday's close. The rest report next week or later and are not gradable.

| Ticker | Daily thesis | Pre → post | Realized | Implied | IV30d crush | Grade |
|---|---|---|---|---|---|---|
| **INTC** | vol_short, DROP raw-2 (07-20; print 07-23 AMC) | $100.23 → $92.32 | **−7.89%** | 11.6% | 100.9% → 84.1% (iv_rank 95.8 → 70.9) | **CONFIRMING** — move stayed inside the implied, IV crushed ~17 vol points. Direction was right; never sized (raw 2 < LOW floor of 3). |
| **NOW** | vol_short, DROP raw-1, single-agent watch (07-20; print 07-22 AMC) | $95.46 → $91.94, rebounding to $98.78 | −3.69% next day, net +3.5% by 07-24 | not priced (watch-only) | 76.0% → 57.1% (iv_rank 97.4 → 60.2) | **CONFIRMING** on the vol dimension — a non-directional seller profits; a directional short round-trips. Never sized. |

Both vol theses were directionally correct and neither was sized. That is the empty-board discipline working as designed on the downside — but it is also two consecutive weeks of correct vol calls left on the table because the scoring floor rejected them.

### (b) Lookahead — next two weeks

**Of 35 candidate names across the heaviest earnings week of the quarter, five clear the kink gate, and only one has genuine back-month tail confirmation.**

| Ticker | Earnings | DTE | IV rank | Implied move | Hygiene shape | Front-end ratio | Back-month skew | Play type | Macro overlap | Conviction |
|---|---|---|---|---|---|---|---|---|---|---|
| **AAPL** | 07-30 AMC | 6 | 71.1 | **4.2%** | KINKED (matches) | 1.315 | **TAIL_HEDGING** | **SELL VOL (half)** | **GDP + Core PCE same day** | LOW-MED |
| PLTR | 08-03 AMC | 10 | 74.8 | 12.1% | KINKED (matches) | 0.79 (artifact) | COMPLACENT | SELL VOL (half) | clean | LOW |
| DIS | 08-05 pre | 12 | 77.0 | 7.2% | KINKED (prom 20.4%) | 0.715 (artifact) | NORMAL | SELL VOL (half) | clean | LOW |
| UBER | 08-05 pre | 12 | 85.1 | 8.6% | KINKED (prom 8.7%) | 0.836 (artifact) | NORMAL | SELL VOL (half), caution | clean | LOW |
| SHOP | 08-05 pre | 12 | 84.2 | 13.5% | KINKED (prom 9.5%) | 0.836 (artifact) | NORMAL | SELL VOL (small/watch) | clean | LOW |
| MSFT | 07-29 AMC | 5 | 87.1 | 7.4% | KINKED (matches) | 1.541 (extreme) | **COMPLACENT** | **STAND ASIDE** | FOMC ~2h before print | — |
| META | 07-29 AMC | 5 | 79.7 | 9.4% | KINKED (matches) | 1.162 | **COMPLACENT** | **STAND ASIDE** | FOMC same day | — |
| AMZN | 07-30 AMC | 6 | 70.1 | 6.9% | KINKED (matches) | 1.526 | NORMAL | **STAND ASIDE** | GDP + Core PCE same day | — |
| BE / STX / V | 07-28 AMC | 4 | 88.0 / 89.1 / 64.8 | 25.3 / 14.1 / 4.1% | BACKWARDATION, no localized kink | 1.434 / 1.287 / 1.377 | NORMAL / NORMAL / TAIL_HEDGING | CALENDAR (watch-only) | FOMC eve | LOW |
| PYPL/GLW/F/BA/KO/UPS | 07-28 | 4 | 61.5–83.2 | 3.3–11.9% | extreme front panic (1.17–1.73) | all >1.10 | mixed | **STAND ASIDE** | FOMC eve | — |
| ARM/QCOM/LRCX/HOOD/CVNA/BSX | 07-29 | 5 | 58.3–95.4 | 8.5–14.5% | no localized kink / mismatched | 1.23–1.50 | NORMAL/COMPLACENT | **STAND ASIDE** | FOMC same day | — |
| AMD | 08-04 AMC | 11 | 85.4 | 12.7% | kink at 07-31, **mismatched** | 1.047 (flat) | NORMAL | **STAND ASIDE** — no signal yet | clean | — |
| SNDK | 08-05 AMC | 12 | 77.3 | 23.7% | KINKED, marginal (prom 5.1%) | 1.065 | NORMAL | **STAND ASIDE from vol** — flag to directional | clean | — |
| LLY | 08-05 pre | 12 | 73.0 | 11.3% | no kink, extreme ratio | **1.835 — most extreme in scan** | NORMAL | STAND ASIDE — mechanical panic | clean | — |
| WDC | 08-05 AMC | 12 | 86.9 | 18.3% | **CONTANGO — no event premium at all** | 1.095 | COMPLACENT | STAND ASIDE — uniformly rich baseline vol | clean | — |
| NBIS | 08-06 (unconfirmed) | 13 | 92.6 | 25.6% | FLAT, no kink | 1.038 | NORMAL | **SKIP** — no premium concentration, date unconfirmed | NFP next day | — |

**Every one of the 13 names printing on 07-29 or 07-30 — including MSFT, META, AAPL and AMZN — is capped or disqualified by the FOMC/GDP/PCE stack.** MSFT and META do kink at their earnings tenor, but their back-months are COMPLACENT: the front is bid and the tail is not, which is the textbook "front-only kink, riskier short" case, compounded here by a Fed decision landing roughly two hours before the print. AAPL is the single structurally clean setup in the entire scan — kink confirmed, back-month genuinely TAIL_HEDGING, front ratio only moderately extreme — and it *still* only earns half size because it shares its print day with Core PCE.

**Two substrate failures found in this lane, both material:**

1. **The screener's `implied_move` is broken for mega-caps.** It reports AAPL at $0.61 on a $333 stock six days before earnings (0.18%), AMZN 0.21%, MSFT 0.26%, META 0.29%. `implied_move_perc` is internally *consistent* with `implied_move / close`, so this is **not a units bug** — the underlying value itself is wrong for high-priced liquid names, while remaining plausible for smaller ones (WHR 14.3%). Independently re-derived from the earnings-spanning tenor's `avg_iv` via `move% ≈ 0.8 × IV × √(DTE/365)`, the sane values are **AAPL 4.2%, MSFT 7.4%, META 9.4%, AMZN 6.9%**. The same defect reproduced on INTC in the Step 7 deep-dive (implied_move $0.33 = 0.36% on a $92 stock). **Do not quote the screener field for mega-caps.** This directly affects criterion C43, which emits `implied_move`.
2. **`uw insights analyst-vs-flow` is degraded** — it now returns only an `options_flow` block with **no analyst-rating field at all**. The analyst-versus-flow disagreement leg, which the rubric identifies as the highest-EV earnings setup, was **unmeasurable on all 35 names this week**.

---

## 7. Risk & Correlation

**Correlation clusters** (`uw risk portfolio-correlation`, 30-day, run against the week-candidate set):

- **`INTC_TSLA_earnings_crash_cluster` — pairwise 0.964.** Both names' 30-day paths are dominated by same-week post-earnings crashes; mechanically this is one bet. INTC kept on `raw_score` 6 > 5; **TSLA auto-deduplicated to watch-only.** No discretion applied.
- **Soft watch (0.60–0.70): TSM/BE at 0.697** — surfaced, no penalty (0.003 under the mechanical bar; per the 2026-05-15 ruling, no discretionary upgrade however same-bet the pair feels).
- INTC/BE 0.501 — below the surfacing bar. Notably **INTC/TSM did not surface at ≥0.50**: TSM finished +1.27% on the week against INTC's −2.86%, so the semis pair actually decorrelated in this window.
- Qualitatively, 4 of 5 candidates are semis-adjacent or high-beta shorts. In a correlated risk-off gap this book is roughly **1.5 independent bets, not 5** — though the VETOs and the cluster gate already collapse it to a single sized name.

**Macro & event risk:** covered in §1. The operative fact is that FOMC lands at **T+2** and Core PCE at **T+3** from a Monday 07-27 entry, so the ≤T+3 event-risk arm fires on every undefined-risk position in the book. **Defined risk is therefore mandatory on anything sized this week** — that is the only path through the gate.

**Fundamentals verdicts (top 5):**

| Ticker | Verdict | The contradicting facts |
|---|---|---|
| **BE** | **VETO** | 4-of-4 EPS beat streak (+228.6%, +40.7%, +55.1%, +800.9% surprises), revenue +56.53% YoY, and **JPMorgan reiterated Overweight and raised its PT to $346 on 07-21 — mid-week of the short entry.** Bullish news flow, no negative BE-specific catalyst. Insider selling (MSPR −27.19) supports the short but is outvoted 2-of-3. Binary print in 2 sessions at ~247% front IV on a name with a clean beat history, after the short is already 14% paid. |
| **INTC** | **CONFIRM** | Revenue +1.36% YoY, net margin −5.9%, insider MSPR −1.8 (neutral, no dip-buying). Earnings already printed and resolved bearish. No fresh binary for 89 days. Caveat: the `beat_streak` label is inflated by tiny estimate denominators ($0.014 est → $0.29 actual = 1971% "surprise") and should not be leaned on. |
| **TSLA** | **CONFIRM** | Q2 EPS **missed by −35.33%** ($0.33 vs $0.51 est), `eps_growth_yoy` −37.66%, insider MSPR 3-month −45.35 including a −99.9 MSPR ~96M-share April sale. All three axes align — the −17.81% week was fundamentally driven, not sentiment. |
| **TSM** | **VETO** | 4-of-4 beat streak with a blowout most-recent print, revenue +31.41% YoY, EPS +55.21% YoY, and gross/operating/net margins of 64.46% / 56.38% / 50.70% — the direct opposite of the margin deterioration a short requires. Uniformly bullish semis supply-chain news. |
| **IBM** | **CAUTION (−1 tier)** | The most recent quarter (reported ~07-22) **MISSED by −2.72%** ($2.93 vs $3.0119) — the "3-of-4 beat streak" is a trailing-window label hiding the fact that the single most relevant print was a miss, immediately before the dark-pool buying that generated the long thesis. Current ratio 0.9557. No IBM-specific catalyst in the news stack. |

**`fz` degradation:** `fz_enrich` returned only `market_cap` for all five names — `recom`, `short_interest`, `target_price` and `earnings` are all in `upstream_gaps` (the known quote-grid truncation). Every `fz_context` is analyst/squeeze-axis NA **by data gap, not by choice**. Separately, `fz screen` returned the known synthetic-ticker artifact (doubled first letters: `TTRV`→TRV, `NNVCR`→NVCR, `OOII`→OII), so the squeeze and relative-strength candidate lanes were skipped entirely this week. All `fz` lanes are advisory and 0 rubric points, so the report completes unchanged.

**Debate-disconfirmation:** no gate fired — but only under a **direction-aware reading**, and that is a live rubric defect (see §8).

**Breadth cross-check (advisory):** 363 advancers vs 140 decliners, **72.17% green**, median +0.97%, against a cap-weighted SPY closing below both moving averages and only 33% bullish flow tickers. `divergence_flag: true` — but this is the **inverse** of the usual distribution tell. Green equal-weight breadth plus heavy mega-cap-tech outflow is **rotation**, not distribution. Read every breadth figure this week against cap-weighted prints before calling it risk-on.

**Adverse-flow exits.** `conviction_week_2026-W29` **does not exist** — last week's weekly board was empty and nothing was written (weekly groups stop at W28). The carried universe is the daily groups:

- **MU** (long watch, 07-23) — **EXIT.** Flow bearish (−$139.2M net), PCR 1.23, IV rank 82.5, OI +113k into the decline; the thesis already graded LOSS. The $452M single dark-pool print in the alert is the known closing-cross class — do not read direction off it.
- **TSLA** (short watch, 07-24) — **CONFIRMED**, carried into W30 (bearish flow −$103.4M agrees with thesis).
- **AKAM / FSLR** (vol_short watches, 07-24) — **intact**, both still iv_rank 100. The premium has not crushed yet, so the vol shorts have not paid, but there is no adverse reversal.

**Hedge sleeve.** The book is 100% short-skewed, but the only live position is a starter defined-risk put vertical whose maximum loss is the debit — the structural hedge is already inside the trade. A proportionate sleeve against the FOMC-relief / mega-cap-beat gap-up scenario would be a **QQQ 2026-08-07 ATM/+3% call debit spread sized to ~50% of the INTC spread's net short delta**; at starter size this is de minimis and can be skipped if the INTC debit is ≤0.25% NAV. **Do not express the hedge as short puts** — VRP is FAIR and the left tail is unsampled.

---

## 8. High-Conviction Cross-Ref

**No HIGH-tier names. No MEDIUM-tier names survive gating.** BE scored 7 (MEDIUM) but was VETO'd on fundamentals. The section below covers the full scored book for audit completeness.

**Expectancy lens (advisory — C31, display-only).** From the 2026-07-18 `/calibration-audit` `phase_3_calibration`:

| Tier | n | Win rate | Mean PnL | Payoff ratio | Half-Kelly |
|---|---|---|---|---|---|
| HIGH | 7 | 0.143 | −2.441% | 0.72 | 0.0 |
| MEDIUM | 19 | 0.526 | **+0.104%** | 0.948 | 0.0132 |
| LOW | 86 | 0.407 | −0.795% | **1.173** | 0.0 |
| DROP | 282 | 0.433 | −2.306% | 0.849 | 0.0 |

**The tier inversion persists** — HIGH (0.143) < LOW (0.407) < DROP (0.433) < MEDIUM (0.526), and **MEDIUM is the only tier with positive expectancy**. Note that LOW carries the best payoff ratio (1.173) despite a sub-coin-flip hit rate, meaning what edge exists in this book lives in asymmetry, not accuracy. Display-only; the live sizer remains the win-rate ladder.

### INTC — short — LOW — raw 6 — **starter, defined-risk**

The one call that survived everything. Its four score components: +3 `oi-trend` BUILDING (SATURATED 5/5 — a floor, not a count, and the top builds are all 0DTE expiry churn, so this is the weakest possible qualifying read); +1 mechanized DEX flip (net_dex 07-23 +$585.1M → 07-24 −$863.8M, prior 5 sessions all positive, 6.35× the $136.1M floor, `whipsaw_warning` FALSE, `total_gex` flipping negative the same session); +1 Technology sector short leg; +1 aligned 30-day cumulative premium flow (−$801.4M, the largest in the union at 4.1× median).

`win_rate` 0.5985 on n=132 under the clean protocol, with **`market_excess` +0.0379** measured against a same-direction (short) SPY benchmark over the same 132 windows — a thin but genuine 3.8 points of skill over simply shorting the tape. `gate_verdicts`: regime no-op, vrp no-op, panic no-op (front-end ratio 0.912, CONTANGO), cluster no-op (kept member), sector favourable, fundamentals CONFIRM, event_risk conditional no-op **via the defined-risk exemption**, debate no-op, rubric_regime capped half.

**The unresolved contradiction, stated plainly.** On the same −7.89% session, institutions bought a coordinated OTM call-spread ladder — Aug 120/130, Sep 135/155, Oct 145/160, Nov 130/150, four exact-size verticals, $33.1M after artifact screening, side-confirmed (Aug C120 at 72.3% ask bought, C130 at 18.9% ask sold, ~$0.77 debit on a 10-wide = 13:1). Strikes require +30% to +73% moves through November. It failed the ≥2-day repeat bar (`repeat_count` 1) so it scored nothing, and fundamentals-gate searched for an explaining catalyst and **found none**.

The debate resolved this as far as the evidence allows. The bull's strongest attack was that the −$801M is only a 5.83% net tilt on a $13.74B two-way gross tape, and that `cumulative-premium-flow` has no box-spread filter while **82.7% of INTC's raw multileg premium ($364.5M of $441M) was financing artifacts** — deep-ITM 1-point call pairs priced at $1.44 on a $1-wide spread, arbitrage-impossible, on OI of 1–126 against 24,000–42,000 lots traded.

The bear's rebuttal is the better argument, on two grounds. First, **comparative**: INTC's 5.83% net/gross tilt is **7.2× MU's 0.81%** — and MU's 0.81% was material enough for the quant to apply a −3 flow_conflict. It is 4.3× TSLA's 1.34%. By the desk's own revealed standard, INTC's skew is among the *cleanest* in the book, not the weakest. Second, **structural**: a box has legs on both sides, so artifact volume inflates *gross* symmetrically without manufacturing a *net* skew. Strip $364.5M from both buckets and the $801M net barely moves.

The bear conceded honestly that the symmetry argument rests on an assumption about the UW classifier's convention — if short-call legs are dropped rather than bucketed symmetrically, contamination could be asymmetric. That is unverifiable without the classifier source and is the single weakest link in the short case.

Residuals: **bull 0.55 (schema floor), bear 0.75.**

### TSLA — short — LOW — raw 5 — **watch_only (correlation-deduped)**

Fundamentals CONFIRM on a real, large EPS miss. Deduplicated purely on the 0.964 correlation with INTC — this is the same bet. The bull's genuine contribution: the institutional block footprint from the last 10 sessions sits at $378.93 ($852M), $380.84 ($444M), $369.57 ($432M), $374.01 ($398M), $396.18 ($390M), $394.46 ($360M) — **all $56–83 above Friday's $313.03 close**, i.e. entry is a chase after a >1.5σ weekly move on rv20 of 77.5%.

The bear's rebuttal was empirical and decisive: block-tier `buy_ratio` ran **0.47 (net selling)** across 380 trades and $704M premium, and the top-100 largest prints on 07-24 split **$216.7M sell-side vs $141.0M buy-side (60.6% sell)** — the opposite of a defended floor. The mega-tier consisted of exactly 2 trades that cancel each other. The bear also checked the closing-cross hypothesis honestly and *rejected* it (prints span 12:44Z–21:51Z, not concentrated in the 20:00–20:25Z window), resting the argument on the buy/sell split instead.

Residuals: **bull 0.55 — but the bull explicitly stated its honest number is 0.35–0.40 and that 0.55 is a schema artifact** — bear 0.65.

### BE — short — raw 7 (MEDIUM) — **VETO → watch_only**

The highest-scoring name of the week, killed by fundamentals. Score: +3 oi-trend (SATURATED, and its largest single build is `BE260731P00105000` at +21,366 — a P105 against spot 184.89, which is the documented **un-split-adjusted strike-grid artifact class**); +2 multileg put ladder (the cleanest repeated directional structure of the week, and the only name to throw a **repeat Tier-1 C19 opening put**); +1 Industrials sector leg; +1 aligned 30-day accretion.

Every gate that mattered pointed the wrong way for a live position: panic **would have fired** (front-end ratio 1.434), event_risk **would have fired** (own earnings at T+1 plus FOMC at T+2), and fundamentals VETO'd on a 4-of-4 beat streak, +56.5% revenue growth, and a JPMorgan PT raise to $346 delivered mid-week. A short already 14% paid, facing a coin-flip print in two sessions at 247% front IV, is not a risk-adjusted trade regardless of how well it scored.

### TSM — short — raw 4 — **VETO → watch_only**

Clean mechanized DEX flip (4.41× floor, `whipsaw_warning` FALSE) sitting on essentially flat 30-day flow (−$59.4M, clearing the $50M magnitude bar by only $9.4M) — dealer repositioning without premium-flow conviction behind it. It took a **−1 `flow_conflict_lite`** for bottom-quartile magnitude while simultaneously earning **+1** for the sector-leader gate on the same flow number. That is a genuine internal tension in the frozen rubric, recorded here; both awards are mechanical and correctly applied. Fundamentals VETO'd on 50–64% margins and 31%/55% growth. The unexplained 08-14 kink remains unresolved after the news pass.

### IBM — long — raw 3 — **skip**

The weakest call in the book and the only long. +3 saturated oi-trend riding 0–3 DTE weekly churn, +1 sector leg at its floor, −1 `flow_conflict_lite` for bottom-quartile magnitude. The accumulation narrative was **un-told by the agent that produced it**: the headline $210.50 shelf ($110M premium, 80 trades) was built on Tuesday — the same session `institutional-accumulation` labelled DISTRIBUTION at a 0.52 sell ratio. The honest description is "sold off Mon–Tue, stabilized and modestly bought back Thu–Fri", not "quietly accumulated all week". Fundamentals CAUTION on a −2.72% miss in the most recent quarter, plus an ex-dividend expected in early August inside the horizon. Gated to skip; excluded from write-back.

### Two rubric defects surfaced this week

1. **The debate gate is direction-blind.** The rubric fires it when "bear residual ≥ bull residual" — wording that assumes a long book where the bear is the disconfirming voice. **Four of five calls this week were shorts, where the bull is the disconfirming voice.** Applied literally, the gate would have fired precisely when the debate *confirmed* the trade. It was applied direction-aware (for a short: fires when bull ≥ bear), so neither INTC (0.55 vs 0.75) nor TSLA (0.55 vs 0.65) tripped it. **The literal reading is rejected and the wording needs fixing.**
2. **The `debate_residuals` schema floor erases signal.** The enum is literally `[0.55, 0.65, 0.75, 0.85, 0.95, null]` — there is no bin below 0.55. **Both bulls hit it independently this week**: INTC's called 0.55 "the floor of the available bins," and TSLA's stated its honest number is 0.35–0.40. This is the third observation of the defect (it erased TSLA's 0.42/0.40 signal on 07-24 and was flagged in the 2026-07-18 audit). It systematically inflates recorded disconfirmation and makes the debate gate's discrimination unmeasurable at the low end.

### Embedded rubric (for audit)

```
Weekly conviction score = Σ:
  # +3 line for swept on ≥3 of 5 days REMOVED 2026-05-23 audit P0.3
  +3  uw historical oi-trend BUILDING for the full week, --days ≥ 5   # WEEKLY-ONLY +3 vs DAILY +1; C47 registered
  +3  3+ aligned signals in accumulation-hunter sustained across week, uw dark-pool block-stratified institutional-tier
      confirmed — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms (sign aligned AND
      |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70, stable WoW — CONDITIONAL: award only
      when dominant_signal_class == leap_directional; else 0
  +2  uw oi position-rolls shows institutional roll forward into longer-dated LEAP (per-covered-date)
  +1  uw historical cumulative-premium-flow shows net directional accretion across the week — INTENT-SCREENED
      (no C28 distribution_flag; no deep-ITM sub-parity ex-div call arb)
  # +2 line for uw insights signal-confluence ≥4 REMOVED 2026-06-12 audit P0.2
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna squeeze in trade direction — verified
      SIGN CHANGE only, via scripts/dex_flip.py; whipsaw_warning mandatory to report
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector — CONDITIONAL:
      persistence_score ≥ 0.6 AND cum_flow_30d aligned AND |cum_flow_30d| ≥ $50M
  +1  in earnings-scout BUY VOL or SELL VOL for next 2 weeks (uw options-structure term-skew aligned)
  +2  multileg-strategist directional structure repeated on ≥2 days (term-structure-anchored play type)
  +1  vol-surface-scout flags KINKED or BACKWARDATION, worsening WoW; iv-percentile-zscore extreme; VRP-aligned
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner crowded long with rising pc-ratio-zscore trajectory (VRP positive)
      # INFORMED-FLOW CONTINUATION penalty on LONGS, not a fade signal
  -3  flow_conflict — cum_premium_flow 30d direction clearly opposite dominant_signal_class
  -1  flow_conflict_lite — 30d cum_premium_flow MIXED (near zero, or aligned but bottom-quartile magnitude)
      # -3 and -1 are MUTUALLY EXCLUSIVE — apply exactly one
  # TIER GATES (Step 2d, 0 points, never in score_components):
  -1 TIER  risk-monitor correlation cluster (pairwise corr ≥ 0.70)
  -1 TIER  WoW regime flip conflicting with trade direction
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | HIGH | full size (subject to win_rate gate) |
| 7 – 8 | MEDIUM | half size (subject to win_rate gate) |
| 3 – 6 | LOW | starter / watch-only |
| ≤ 2 | drop | not surfaced |

**Rubric version `2026-06-12`, FROZEN. Status OUT-OF-REGIME — all sizing capped at half.** The ≥9 HIGH cut failed its scheduled re-confirmation on 2026-06-12 and carries no validated ranking claim; the freeze is retained because re-binning on another thin window would repeat the documented failure mode.

---

## 9. Setups for Next Week

### Next-session GEX advisory — SPY / QQQ (advisory, 0 rubric points)

**Lead with the verdict: `NO_GO_NO_EDGE`.** The rolling 60-day backtest found the next close landed closer to the nearest EOD wall only **22.0% of the time (n=118) against a 50% baseline** — materially *worse* than chance, p=1.0 one-sided. Walls behaved as **anti-magnets**. H1 (short-gamma → wider realized moves) also ran backwards pooled (0.787 vs 0.835), though the SPY leg alone satisfied it. Nothing below is a forecast.

**SPY** — spot 738.52, `zero_gamma_level` **null** (`zgl_reliable: false`; the tool returns None on FULLY_NEGATIVE by design), regime **FULLY_NEGATIVE**, `total_gex` **−$1.56B**. Call wall 739 (+$64.3M) is effectively at-the-money and negligible; the next real positive cluster is 760 (+$62.1M), ~2.9% away. Put wall 735 (−$155.0M), with 730 (−$147.8M) and 720 (−$140.9M) forming a dense negative-gamma shelf. Regime **HELD but noisy** — briefly NEGATIVE on 07-21 (ZGL 759.20, plausible) before reverting. Structure bias: short-gamma logic favours debit verticals over premium selling on a break, but given NO_GO, the defensible read is simply **avoid GEX-wall-anchored premium-selling structures into next week**.

**QQQ** — spot 684.16, ZGL **null**, regime **FULLY_NEGATIVE**, `total_gex` **−$1.75B**. **Effectively no call wall** — nearest strikes above spot are near-zero or negative (701 +$0.65M, 709 +$0.32M, 696 −$0.12M). Put wall 680 (−$128.3M) with 684 (−$117.1M) essentially at spot, sloping continuously to 660. More unstable than SPY: the 07-22 "POSITIVE" print carried `zero_gamma_level: 352.82`, a textbook instance of the known **ZGL-grid artifact** (~48% below spot) and must be disregarded, not read as a regime flip.

**Mandatory caveats:** this is Friday's EOD 0–45d book, refreshed within 30–60 minutes of Monday's open; gap risk is live; it is the **ETF** book, not the cleaner SPX/NDX index book; `uw` cannot isolate the D+1 expiry (`--dte-max 1` errors); and a gamma map built on last week's book has essentially no forecasting value across a Fed decision plus the four largest index constituents reporting within 48 hours.

### Next-session 0DTE premium-selling setup (advisory, 0 rubric points)

Rolling backtest verdict **`GO_PREMIUM_SELL_INTRADAY`** — the part of the stack that *did* validate.

| Index | n | Win % (gross) | Mean PnL gross | **Mean PnL NET** | Worst day | Vol state | VIX | Implied move | Expected range | Size scalar | Structure |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 60 | 93.3% | +0.275% | **+0.175%** | −1.4% | HIGH | 18.58 | 0.62% | 1.18% | 1.5 | Wider iron condor, wings ≈ ±1.18% |
| QQQ | 60 | 88.3% | +0.404% | **+0.304%** | −2.453% | HIGH | 18.58 | 1.10% | 1.95% | 1.5 | Wider iron condor, wings ≈ ±1.95% |

**Quote the net line, on its real basis.** `mean_pnl_open_pct` is **% of underlying spot notional, GROSS** — not premium-collected, not margin-relative. Net of an assumed 0.1% round-trip cost, SPY is +0.175% and QQQ +0.304%. Rules: sell only when the front IV is rich, size by VIX level, take wing width from the GEX vol-suppression range, **enter at the open once the overnight gap resolves, and never carry overnight**; stand aside on a VIX spike or front-end backwardation. SPY ≈ SPX (trade either); QQQ is the weaker leg.

**The unsampled tail is the whole story this week.** The validation sample contains **no vol shock**, so the short-vol left tail is entirely unsampled — and next week's calendar (FOMC 07-29, GDP + Core PCE 07-30, MSFT/META/AAPL/AMZN) is precisely that scenario. **Do not lean on the 1.5× HIGH-vol size scalar into those sessions.** The entry rule — enter at the open, never carry overnight — is doing the real risk work, not the scalar. This lane is advisory and 0 rubric points **permanently** until a vol-shock day enters the sample and net expectancy clears a tail-aware bar; win rate is explicitly not the promotion metric for a negatively-skewed short-vol strategy.

### Swing setups — dealer positioning

Five names fired mechanized DEX sign-flips, **all short**, and — a genuine cross-tool corroboration — **all five also flipped or deepened `total_gex` negative on the same session (07-24)**:

| Ticker | Flip magnitude | Sign changes | Whipsaw | 30d flow | Verdict |
|---|---|---|---|---|---|
| **INTC** | 6.35× floor | 3 | FALSE | −$801M **aligned** | **The only one where flow reinforces. Sized.** |
| **TSM** | 4.41× floor | 3 | FALSE | −$59.4M (flat) | Clean flip, no conviction behind it. VETO'd. |
| MU | 3.34× floor | 5 | **TRUE** | +$725M **conflict** | Killed |
| SNDK | 4.69× floor | 4 | **TRUE** | +$785M **conflict** | Killed |
| NBIS | 2.60× floor | 4 | **TRUE** | +$168M **conflict** | Killed — thesis already spent |

**Vanna squeezes: zero qualified.** The dated VIX series (Yahoo chart API `^VIX`, confirmed working for 2026 dates) ran 18.77 → 18.65 → 17.05 → 16.64 → **18.70 → 18.58** — the trailing three sessions rising then flat, not falling. Every put-heavy book correctly flags "vanna pressure, not squeeze."

**Pin vs trend regime call:** neither. Both indices are short-gamma with no meaningful call-side structure, but the wall-as-magnet hypothesis is measurably false in this sample. Trade the catalysts, not the gamma map.

### The two or three actionable setups

1. **INTC short — starter, defined-risk August put vertical.** The only sized call. Invalidation: daily close above the $95.95–$97.00 dark-pool shelf. Weigh the playbook's preference for a bear call credit spread at iv_rank 71 (§3b).
2. **AAPL sell-vol into the 07-30 print — half size at most.** The single structurally clean earnings setup in a 35-name scan (kink confirmed at the earnings tenor, back-month genuinely TAIL_HEDGING). But it prints the same day as Core PCE and GDP, which is exactly why it earns half and not full.
3. **Stand aside on the 07-29 cohort entirely.** MSFT and META kink at their tenors but their back-months are COMPLACENT, and the Fed decision lands roughly two hours before both prints.

### LOW-tier names to track for daily confirmation

TSLA (short, watch-only — deduped at 0.964 correlation to INTC; becomes live if INTC invalidates and the correlation breaks), plus the §10 list.

### OPEX

**Not applicable.** `opex-pin-strategist` was deliberately not spawned. Monthly third-Friday OPEX was 2026-07-17 — *last* week — and the coming week (07-27 → 07-31) contains no monthly expiry; the next is 2026-08-21. `WEEK_END` sits exactly 7 calendar days after the July OPEX, which satisfies the literal spawn condition, but the agent's output feeds "Setups for Next Week" and would have produced a pin book for an expiry that already printed. Ten agents ran this week rather than eleven.

### Deep-dive hand-off

No HIGH-tier names post-gate, so the standard top-2 hand-off does not apply. For the single sized name: **`Recommended deep dive: /stock-deep-dive INTC`**.

---

## 10. Watch-only — single signal, no confluence

Names surfaced by exactly one Phase 1 agent, or flagged by many agents that all declined to recommend them. **For journaling, not entry.**

| Ticker | Direction | Sole agent / status | Note |
|---|---|---|---|
| **COPX** | long | accumulation-hunter (MEDIUM) | **The cleanest accumulation signature of the week** — mega-tier DP fired 4/5 days at buy_ratio 1.00, and the signal *survives* closing-cross exclusion (Wednesday's 9.78 buy-ratio is 83% contaminated and discounted; Tue/Thu/Fri remain clean at 4.08/3.69/4.08). C34 shelf **$77.70–$78.60** (the $80.37 print is closing-adjacent — do not anchor to it). OI genuinely spread across tenors, unlike the 0DTE churn elsewhere. Fails the gate on one agent only. |
| **WULF** | long | multileg (HIGH) **vs** leap-radar (DISQUALIFIED) | **A direct, unresolved contradiction on the same option book.** multileg sees a delta-raising roll — Jan-27/Jan-28 C22/C25 → C20/C25 across 3 days, 99.6% ask-side, OI evidence of an existing book rolled down-strike and out-tenor, 3.4:1 payoff. leap-radar sees a hedge overlay: cum-flow **net bearish** at both 30d (−$49.7M) and 90d (−$87.1M) against a −27% weekly decline, plus a competing Jan-28 $15 put build. Both readings are internally coherent. Not scored. |
| **ORCL** | short | sector-rotation only (C19 is an advisory lane, not an agent) | Would have scored ~5 (LOW). Carries the **unexplained 65.1%-prominence 08-21 kink** on a 12,374-contract tenor with no scheduled earnings — do not size through 08-21 without an explanation. |
| **AAPL** | vol_short | earnings-scout only | The one structurally clean earnings setup in the scan; half-size-capped by the same-day Core PCE/GDP overlap. Its dark-pool tape was 59–100% closing-cross contaminated and correctly rejected as accumulation. |
| **AMD** | short | sector-rotation only | Sector short leg passes (−$137.2M), but the 07-31 kink is mismatched to its 08-04 print and the front-end ratio is flat — no event premium yet. |
| **CBRS** | long | sector-rotation only | +$92.0M bullish 30d flow, but **+15.19% already printed this week** on rv20 of 124% — entering after that move is a materially different trade. |
| **IREN** | vol / calendar | vol-surface only | The **only** clean calendar candidate of the week (BACKWARDATION, no catalyst, front-end ratio falling 1.106→1.047). A vol structure, not a directional call — and its underlying flow is bearish. |
| MU / SNDK / NBIS | short | 6 agents each, **0 positive** | Flagged everywhere, recommended nowhere. All three fired mechanized DEX flips *and* carried whipsaw warnings *and* had 30-day flow running against the short. NBIS's thesis was already realized and monetized — the operator sold the P180 on 07-24 and bought 08-07 C220 at 93.6% ask, rotating to the upside. **Do not re-enter.** |
| SMH / SOXX | — | multileg | **Sector-internal contradiction:** SMH's $146.8M package tilts long-downside (an event hedge sitting exactly on the 07-31 kink) while SOXX resolves to a bull put credit spread — short downside — in the same sector, same week. At least one is not a thesis. Neither is scored as a directional semis view. |

---

## Appendix — substrate and tooling findings this week

Recorded for `/calibration-audit`. None of these changed a score; several changed what a score *means*.

1. **`sector-flow-persistence` measures turnover, not accumulation.** Its `net_flow` = `total_premium_call − total_premium_put`, sign-agnostic and unclassified by aggressor. Verified to the dollar. This is a different quantity from `market-regime`'s classified net premium and the two can point opposite ways on the same sector, same day. **Highest-value finding of the week.**
2. **`implied_move` is broken for mega-caps** (AAPL $0.61 on a $333 stock). Not a units bug — `implied_move_perc` is internally consistent. Affects criterion C43.
3. **`analyst-vs-flow` no longer returns an analyst field** — the highest-EV earnings lane was unmeasurable on all 35 names.
4. **`iv-percentile-zscore` is globally capped at ~72 days** regardless of `--lookback-days 252`. All percentiles this week are provisional.
5. **`pc-ratio-zscore` has no `--date` flag** — it returns only today's snapshot. Multi-date trajectories must be reconstructed from `uw historical trend`'s daily `put_call_ratio` (formula verified reproducible against the live tool: current-day P/C vs mean/std of the trailing 20 sessions excluding today).
6. **`market-regime` returns current spot regardless of `--date`** — the `spy` block was byte-identical for 07-20 and 07-24. Breadth sub-fields *do* vary correctly.
7. **Raw `iv-term-structure` label was 100% saturated** (BACKWARDATION 26/26). Always classify through `term_structure_hygiene.py`.
8. **`fz screen` returns synthetic tickers** (doubled first letters). **`fz_enrich` returns only `market_cap`** — analyst/short-interest/target fields are all upstream gaps.
9. **Stale-NBBO artifact appeared 3× in one ETF pass** (IGV, XLE, EWY). Systemic.
10. **~$7.9B of raw multileg premium was financing, not opinion** — SPX/SPXW conversion-reversals (~$7.5B), INTC deep-ITM 1-point call pairs ($364.5M of $441M), TSLA P400/P380 box ($126.9M), GOOGL P390 parity ($57.9M), MRVL P240 parity ($24.9M). **The four largest raw single-name multileg figures (INTC $441M, NVDA $791M, TSLA $183M, GOOGL $94M) are majority artifact.** Any ranking off raw `hot-chains multileg` premium without a parity check badly mis-ranks this week.
11. **Un-split-adjusted strike grids confirmed again, now in the single-leg feed too** — MU P550/P60, NBIS P105, BE P110/P105, SMH P325, MSTR Jan-27 P390, LULU P280, TSLA 2028 P760.
12. **C47 accrues further evidence:** the +3 `oi-trend` line was SATURATED on **5 of 5** scored names (16 of 16 last week) — two consecutive weeks of zero discrimination from a +3 line, and on BE its largest build sits on an artifact strike.
13. **`zero_gamma_level` unreliable across SPY/QQQ/IWM/MU and NBIS/SNDK/TSM/INTC** — values like 5, 23.88, 130.52, 352.82 against spots of $92–$1,440. Use `total_gex` sign only.
14. **Yahoo chart API confirmed working for 2026 dates** (both `^VIX` and equity OHLC; verified MU closes matching `uw historical trend` exactly). The "2025-anchored" caution applies to the MCP path, not the raw chart API.
15. **C19 single-leg advisory:** 17 Tier-1 signals, **all puts**, count ramping 1 / 0 / 2 / 8 / 6 across Mon–Fri. Only one repeat name (**BE**). Next-session hit rate **8/11 = 72.7%** (7/9 = 77.8% on the size/OI ≥ 2 PRIME subset). Positive out-of-sample accrual, but n=11 in a single correlated down-tape week. Still advisory, 0 rubric points.
