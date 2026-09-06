# Daily Market Analysis — 2026-07-15

## Executive Summary

- **Regime + GEX state:** TRANSITIONAL (trend UPTREND, SPY 754.81 above both 20/50 SMA, +1.76% 30d, −0.74% off the 90d high) but breadth is soft — only **35.3% of optionable tickers show bullish flow** (2,219 bullish vs 4,069 bearish). VIX 15.67 (LOW). SPY sits **on** its zero-gamma level (755.26 vs spot 754.37) — a coin-flip book. QQQ dealer gamma is net short (−$354.6M). 0DTE share 40.6% = retail-driven tape. OPEX Friday is T+2 (07-17).
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** SPY — spot 754.37 · ZGL **755.26 (reliable)** · call wall 755 / put wall 750 · walls tight, spot on the flip, do not pre-position. QQQ — spot 717.41 · ZGL **unreliable (300.35 artifact)** · call wall 730 / put wall 700 · short-gamma, wide walls, trend-prone. Advisory, see §2.
- **Top swing build:** **NONE.** No name reached even the LOW tier (raw ≥ 3). Highest raw score on the board = **2**.
- **Top LEAP candidate:** **NONE.** Best candidate scored 4-of-9 gates.
- **Biggest risk:** Not a position — it's the **tape**. **92% of today's multileg premium is mechanical artifact** (worse than the ~85% prior baseline). The single largest "bullish" number in the entire funnel, `SPX +$5.907B`, is a **box spread** — a financing trade, not conviction.

**This is an ALL-DROP board — the 3rd ever, and the 11th consecutive near-empty board.** Nothing was sized. Nothing was written to the watchlist. That is the output, and on today's evidence it is the correct one.

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — mixed signals, reduce position size, wait for clarity.** Trend UPTREND. Guidance: *"Half position sizes. Favor defined-risk strategies. Iron condors in range."*

The headline tension: SPY is above both moving averages and within 0.74% of its 90-day high, yet **only 35.3% of optionable names carry bullish flow**. A tape that grinds up on narrow participation is the classic TRANSITIONAL signature, and it is why the regime label disagrees with the trend label.

### Per-index gamma (current-state EOD book)

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 754.37 | **755.26** (reliable, 0.12% from spot) | +$1.203B | NEGATIVE (label) | 755 (+$516.7M) | 750 (−$117.2M) |
| QQQ | 717.41 | ~~300.35~~ **artifact — unusable** | −$354.6M | POSITIVE (label) → **NEGATIVE** (fallback) | 730 (+$67.0M) | 700 (−$107.0M) |
| IWM | 295.72 | **null** — uncomputed | — | — | — | — |

**Two tool contradictions to record, not paper over:**
1. **SPY:** `total_gex` is aggregate-**positive** (+$1.2B) while the tool's `regime` label says **NEGATIVE**. The label is driven by the local spot-vs-ZGL crossing (spot fractionally below 755.26) even though the book is net long-gamma in aggregate. The gap is inside bid-ask/data-timing noise — do not over-read the label.
2. **QQQ:** the tool label says **POSITIVE** while `total_gex` is **negative** (−$354.6M). Per the ZGL-unreliable protocol we fall back to the `total_gex` sign → **NEGATIVE**. This is a fallback inference, not a tool-native read.

**IWM's ZGL is `null` and its 10-day history shows values of 155/194/199/130/150 against spot ~293–300** — the same sub-half-spot artifact class as QQQ, worse. IWM's regime series is unusable this window.

### Flow structure & vol

- `uw options-flow dte-volume-share`: 0DTE **40.6%**, weeklies 28.4%, monthlies 19.3%, LEAPs **4.1%**. `regime_hint: RETAIL_DRIVEN`. Institutional positioning share is thin; LEAP share is the thinnest slice on the board.
- `uw historical vrp`: **SPY FAIR (−0.0234** — IV30 13.18% vs realised 15.52%); **QQQ PREMIUM_BUYING (−0.0709** — IV30 23.12% vs realised **30.21%**).

**Both indices are negative VRP: realised vol is running above implied.** Premium is *cheap*, not rich. This structurally disadvantages every premium-selling fade today and is the direct cause of contrarian-scanner's abort (§3b).

### Macro backdrop

Yield curve **normal** (10y2y +0.42). Core CPI **2.81% YoY**, core PCE **3.41% YoY** — PCE running 60bp above CPI, and both above target. Unemployment 4.2%, payrolls **+57k** (soft). 10Y **4.58%, rising** (+10bp/30d). USD **strengthening**. Fed funds 3.63%.

Rising 10Y + strengthening USD + soft payrolls + sticky core PCE is a mildly hostile backdrop for duration-sensitive longs.

**Forward event risk:**

| Event | Date | Distance | Impact |
|---|---|---|---|
| **Monthly OPEX** | 2026-07-17 | **T+2** | mechanical — dominates this entire report |
| CPI | 2026-07-14 | released | — |
| **FOMC (no SEP)** | 2026-07-28/29 | T+9/T+10 | high — outside every gate window |
| Jobless claims | Thursdays | weekly | low |

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book (open interest persists overnight) read forward as the *prior* for next session's open. **Prose-only, 0 rubric points, no backtested predictive claim.** Predictive validation lives in `/weekly-analysis`'s rolling §2 backtest. Scope is SPY and QQQ only.

### SPY — spot on the flip, walls tight

Spot 754.37 sits **$0.89 below** the ZGL at 755.26 — a razor's-edge crossing, with the single largest dealer gamma concentration (+$516.7M) parked at exactly 755. Walls are **tight: 750–755, five handles**.

**Structure bias:** genuinely a coin-flip open. Holding ≥755 keeps the long-gamma pin thesis intact (mean-revert toward 755, vol suppressed) → tight iron fly / short straddle centred 754–755. A print below ~754 hands dealers a short-gamma book and opens a fast slide to the 750 put wall four handles down → flip to debit verticals or a long straddle. **Do not default-size the fly.** Wait for the first 30–60 minutes to confirm which side of 755 dealers are hedging from.

### QQQ — short gamma, wide walls, ZGL unusable

ZGL returns **300.35 against spot 717.41** — 58% below spot, physically nonsensical, and a **recurrence of the pre-registered sub-320 GEX-grid artifact**. Discarded. Falling back to `total_gex` sign (−$354.6M) → dealers net short gamma → trend/breakout-prone, not pin-prone. Consistent with QQQ's richer implied move (1.41% vs SPY's 0.68%) and its PREMIUM_BUYING VRP.

Walls at **700/730 are wide** (30 handles, ~4.2%) — they will not cap a trending move the way SPY's tight band would.

**Structure bias:** short-gamma + wide walls → favour debit verticals / long-premium over short premium. If selling premium at all, size defensively and centre inside 700–730 rather than tight to spot.

### Mandatory caveats

- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 min and re-computes the ZGL/walls.
- **ZGL reliability.** SPY's is reliable (0.12% from spot). **QQQ's is a known artifact — do not surface 300.35 as a level.** IWM's is `null`.
- **Gap risk voids the prior.** Cross-check the event calendar; OPEX is T+2.
- **Tooling limit.** `uw` cannot isolate the D+1 expiry (`gex --dte-max 1` errors). This is the standing 0–45 DTE book — the best available proxy.
- **ETF book**, not the cleaner SPX/NDX index book.
- **OPEX-loaded.** `expiry-heatmap` confirms 07-17 is QQQ's 2nd-largest premium expiry ($275M) and 07-16 its 3rd ($162M); SPY carries $148M on 07-17 and $188M on 07-16. Next-session flow is a mix of tomorrow's own gamma **plus** OPEX-week unwind — not a clean single-expiry read.

### 2a. Next-session 0DTE premium-selling setup (the validated stack)

> The GEX walls above are a **map, not a pin** — wall-as-magnet backtested NO_GO, as did every directional 0DTE signal. What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, NOT a guaranteed edge.

| Field | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` / VIX | LOW / 15.67 | LOW / 15.67 |
| `implied_move_pct` | 0.68% | 1.41% |
| `expected_range_pct` | 0.78% | 1.89% |
| `size_scalar` | **0.5** | **0.25** |
| Structure | iron fly / short straddle @ 754.47, wings ≈ ±0.78% | wider iron condor, wings ≈ ±1.89% — or reduce / stand aside |
| `caution` | none | **Front-end backwardation (0DTE IV 1.43× VIX) — event/gap risk; half size** |

**Rolling backtest — quote net, not gross:**

| Metric | SPY | QQQ |
|---|---|---|
| `verdict` | GO_PREMIUM_SELL_INTRADAY | GO_PREMIUM_SELL_INTRADAY |
| win-rate (open entry, gross) | 93.3% | 88.3% |
| `mean_pnl_open_pct` (GROSS) | +0.292% | +0.402% |
| **`mean_pnl_open_net_pct`** | **+0.192%** | **+0.302%** |
| `mean_pnl_overnight_pct` | −0.15% | −0.365% |
| `worst_day_open_pct` | −1.4% | −2.453% |

`pnl_basis`: **percent-of-underlying-spot-notional, GROSS** — not premium-collected, not margin-relative. Net figures charge the assumed 0.1% round-trip cost.

- **Whether:** front-expiry implied move systematically exceeds realised next-day open-to-close. Both GO.
- **How much:** long-gamma → quieter range → tighter wings; short-gamma → wider. Use `expected_range_pct`.
- **Size:** VIX 15.67 is LOW → **thin edge**. SPY scalar 0.5, QQQ 0.25.
- **When:** enter at/after the open once the gap resolves; **hold to the close; never carry overnight** (overnight entry backtested negative).
- **Direction:** none. Delta-neutral. Do not add a tilt.

**SPY ≈ SPX** (validated identical). **QQQ is weaker** (NDX book unavailable) — lower confidence, and it carries an explicit backwardation caution today.

**Promotion bar:** stays advisory / 0 points **permanently** until BOTH a vol-shock day enters the sample (the short-vol left tail is currently **UNSAMPLED**) AND net expectancy clears a tail-aware bar. Win-rate is explicitly **not** the promotion metric for a negatively-skewed short-vol strategy.

---

## 2b. Swing Dealer Positioning (1–4 weeks)

**No mechanized DEX flip fired anywhere in SPY/QQQ/IWM.** This is the expected and correct answer — reported plainly rather than dressed up as a level.

| Ticker | DEX state (07-15) | Mechanized flip? | Vanna squeeze | Swing bias |
|---|---|---|---|---|
| SPY | POSITIVE (+$29.58B), choppy | **No** — prior 3 sessions mixed sign (+16.36B / −0.09B / +42.50B) | No — book is **call-heavy** (net_vanna −86,659), wrong side | NEUTRAL |
| QQQ | NEGATIVE (−$3.86B) | **No** — prior 3 mixed (+3.27B / −16.97B / +13.76B); magnitude clears the 0.25× floor ($3.49B vs median $13.96B) but the **sign-run precondition fails** | **YES** — put-heavy (net_vanna +14,584; put_dex −33.4B) + VIX down 3 sessions | LONG (**hypothesis only**) |
| IWM | NEGATIVE (−$0.59B), 7-of-10 sessions negative | **No** — same sign as prior 3, that's a sustained state not a reversal; magnitude is **below** the 0.25× floor ($0.59B vs $0.61B) = sub-threshold noise | YES, weaker | LONG-lean, weak |
| AAPL/GOOGL/META/AMZN/MSFT | POSITIVE (beta) | Not evaluated | No — all call-heavy | NEUTRAL |

**The VIX leg is dated and verified.** Yahoo chart API `^VIX` returned 07-08 16.90 → 07-09 15.84 → 07-10 15.03 → 07-13 **17.16** → 07-14 **16.50** → 07-15 **15.67**, matching Step 0 exactly. **Three consecutive down-closes.** The API works correctly for 2026 dates — consistent with the 07-11 audit's refutation of the "2025-anchored" note. Recording that the chart-API path is confirmed healthy again.

The QQQ/IWM vanna-squeeze flags are **practitioner hypothesis, not validated edge** (2026-06-12 P0.4). A positive DEX *level* in an up-tape is **beta**. The mega-caps' uniformly positive DEX is exactly that and earns nothing.

## 2c. Sector Rotation

**Rotation regime call: `no_change` (confidence: LOW).**

This is broad multi-bloc inflow — growth, value, cyclical *and* defensive sectors all showing sector-level inflow simultaneously, with **no offsetting persistent outflow leg**. That is the non-discriminating trending-tape signature, not rotation. There is no canonical defensive↔cyclical or growth↔value pattern to name.

**The persistence gate is non-binding.** `sector-flow-persistence` returned **9 of 11 sectors tied at persistence_score = 1.0**; Industrials 0.8, Basic Materials 0.6. The ≥0.6 gate clears 10 of 11 — it discriminates nothing. (Reconfirms the 06-12 audit finding.)

### ⚠ Technology sign contradiction — RESOLVED

The fleet's two sector tools disagreed on **both sign and scale** for Technology:

| Tool | Technology reading |
|---|---|
| `uw options-flow sector-flow` (the fleet's PRIMARY) | **+$2,256,090,914** (inflow) |
| `uw risk market-regime` → `sector_rotation` | **−$82,213,369** (outflow) |

**Verdict: trust the smaller, negative reading. Technology is NOT a rotation-in.** Three independent lines converge:
1. **Every mega-cap Tech name checked is net-bearish on 30-day cumulative flow** — MSFT −$882M, GOOGL −$341M, AMZN −$246M, ORCL −$210M, AAPL −$93M, IBM −$46M.
2. **XLK — the sector's own ETF** — shows persistent 5-day bearish options flow **plus explicit long-dated put-hedge buying at the 170 strike in both 2027 and 2028 expiries** (ask-side).
3. **Scale.** Tens of millions is a plausible single-session net-institutional figure for a mega-cap sector; billions sustained with **zero corroborating single-name accumulation** is not.

**Mechanism:** `sector-flow` appears to sum signed premium across all contracts without netting against OI — it measures **gross turnover / activity intensity** ("where the volume is"), not **net positioning** ("who's accumulating"). On high-volume days it is dominated by whichever side of massive two-sided mega-cap flow is marginally larger in raw dollars. **This is a genuine methodology gap, and the noisier tool is the fleet's designated PRIMARY.** → `/calibration-audit`.

### Single-name leader gate — 16 names checked, 2 pass

Gate = persistence ≥ 0.6 **AND** cum_flow_30d direction aligned **AND** |cum_flow_30d| ≥ $50M.

| Ticker | Sector | 30d flow | Result |
|---|---|---|---|
| **META** | Comm Services | +$206.9M | **PASS** (all 3) |
| **BABA** | Consumer Cyclical | +$376.8M | **PASS** (all 3) |
| AAPL / MSFT / GOOGL / ORCL / IBM / AMZN / UNH | Tech, Comm, Cons Cyc, HC | all negative | FAIL — wrong direction |
| PYPL / GS / JPM / SLS / BSX | Fin, HC | +$4.6M to +$45.0M | FAIL — under $50M |

**Rotating into:** Communication Services (HIGH — META passes) · Financial Services (HIGH — no mega-cap passes, but **KRE** confirms via DP + sweeps) · Consumer Cyclical (MEDIUM — BABA passes).
**Excluded despite clearing the mechanical bar:** Technology (contradicted three ways above) and Healthcare (**XBI is persistently bleeding** — the inflow doesn't extend to biotech; no single name clears the gate).
**Rotating out of:** none — no sector shows ≥3-day persistent negative dominant flow.

### ETF flow tape (advisory — 0 rubric points)

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Leaders |
|---|---|---|---|---|---|---|
| **EWY** (Korea) | +$46.3M | BULLISH-persistent | buy-side blocks (+0.28 to +0.85 vs mid) | net call-buying Aug/Sep | n/a (geographic) | — |
| **XLI** | +$3.9M, thin | BULLISH | **seller-dominant** (−1.13 vs mid) — conflicts | — | agree (weak/conflicted) | — |
| **KRE** | +$2.6M | BULLISH-persistent | buy-side ($37.5M block, +0.065) | calls 75/80, ask-side | **agree** | **the real Financials leader** |
| **XBI** | −$12.2M | BEARISH-persistent | today-only call blip | — | **disagree** | Healthcare inflow ≠ biotech |
| **GDX** | −$10.5M | BEARISH | seller-tilted | 2028 LEAP calls vs near-term puts | agree (both inconclusive) | — |
| **XLK** | −$4.9M | BEARISH-persistent | flat/noisy | **2027 + 2028 LEAP puts @ 170, ask-side** | **DISAGREE** | the Tech contradiction, instrumented |

**Swing-book implication:** no clean rotation regime to trade. **Fade the Technology inflow headline.** Financials rotation is real but expressed through KRE, not a mega-cap name. Size tactically — the 40.6% 0DTE share is a retail-tilted tape and warrants a uniform conviction discount.

---

## 3. Swing Setups (1–6 weeks)

### 3a. Long swings (regime-aligned)

**EMPTY.** No long swing candidate reached the LOW tier.

`accumulation-hunter` — the primary engine for this section — **returned an empty list**, and the reason is the finding:

> **The entire mega-cap dark-pool board is one closing-cross print each.**

| Ticker | Dominant DP price level | Timestamp | Shares |
|---|---|---|---|
| NVDA | 212.50 | 20:00:00–20:31:35Z | 5.03M |
| MSFT | 395.63 | 20:00:00–21:26:12Z | 3.57M |
| AMZN | 254.96 | 20:00:01–21:23:05Z | 2.81M |
| GOOG | 370.21 | 20:00:09–20:36:53Z | 2.42M |
| AAPL | 327.50 | 19:59:54–20:33:57Z | 2.07M |
| META | 681.31 | 20:00:06–21:26:12Z | 1.19M |
| AMD | 529.14 | 20:00:00–20:11:04Z | 1.09M |
| TSLA | 394.46 | 20:00:00–20:11:05Z | 0.90M |
| COST | 916.54 | 20:00:07–21:23:05Z | 0.66M |
| LLY | 1156.63 | 20:02:58–21:02:22Z | 0.36M |

Every one of these names' `block-stratified` mega-tier buy ratio (NVDA 1.0, LLY 1.0, AMD 0.98, MSFT 0.89, AAPL 0.87, GOOG 0.87) is **real but entirely artifact-explained** by a single 20:00–21:56Z closing-cross block. **This now confirms the artifact leaks into `uw insights institutional-accumulation`'s own `top_price_levels` AND into `uw dark-pool extended-hours`** (which classifies post-16:00-ET as "extended hours" — here that just means the closing cross itself). Third-plus recurrence of the 2026-07-02-class artifact. → `/calibration-audit`: the tool should exclude that window in its own aggregation rather than leave it to the caller.

**PPG** (the Step 0 funnel's best bullish confluence hit, score 5) was checked directly and rejected: only 34 total DP trades, dominant level 115.31 **also timestamped 20:01:31–20:01:50Z**; `oi-trend` BUILDING but `consecutive_build_days: 1`; `smart-positioning` returned one contract, **inferred bearish** (104C bid-heavy = call-selling). Clears 0–1 genuine signals, not 3.

### 3b. Short / fade swings (defined risk only)

**EMPTY — `contrarian-scanner` aborted on the VRP gate.**

Both indices are negative VRP (SPY −0.0234, QQQ −0.0709). Realised is running *above* implied on both benchmarks: **premium is cheap, not rich.** No premium-selling fade structure is justified.

Even setting VRP aside, there is no setup:
- **No index-level fear extreme.** `pc-ratio-zscore`: SPY z = **−0.176 NORMAL**, QQQ z = **−1.532 NORMAL**. Nowhere near ±2σ.
- **Every liquid single-name candidate is in BACKWARDATION at 2 DTE — which *is* OPEX Friday.** RAL, WRBY, HACK, ALL, W, AAP all show front-week IV at 2–4× back-month. That's an event being priced, not a crowd being wrong. Five of six also show "price up, flow bearish" — protective hedging into the event.
- **WRBY's z = +10.8 BEARISH_EXTREME** is the textbook trap: a name that rallied 11.2%, in backwardation, into OPEX, IV rank 94.7 → that's a **hedge bid, not crowd euphoria.** Precisely what the informed-flow-continuation mechanism warns against (Pan-Poteshman 2006; Ge-Lin-Pearson 2016 — single-name P/C extremes predict *continuation*, not reversal).

**Artifacts dropped:** **MD (PCR 860)** — call volume **7** vs put volume 6,022. **MORN (PCR 331)** — call volume **1**. Divide-by-tiny, not sentiment. **HRMY** fails the C12 liquidity floor (~$28M ADV).

### Sweeps (informational — 0 rubric points)

Ranked by `sweep-persistence`. **Note:** `consistency_score` is exactly `sessions_in_top/5` — a *participation* share, not a directional-agreement check.

| Ticker | Side | Persistence | Cum. premium 5d | Note |
|---|---|---|---|---|
| **SNDK** | Bearish | 5/5 | $2.17B | Best-formed on the sweep tape — 07-17 puts $49M bid-side, opening-confirmed (+27,831 net OI). **But see §7 — the quant's net-flow check reversed this.** |
| **ORCL** | Bearish | 4/5 | $534M | 07-17 puts $20.2M, opening-confirmed (+92,249) |
| SPX | Bullish | 5/5 | $2.47B | **REFUTED — box spread, see §7** |
| SPCX | "Bullish" | 4/5 | $591M | **Thesis already in question** — today's tape is put-heavy with `no_side` blocks + simultaneous LEAP call+put OI build = collar, not a directional bet |
| TSM | Bearish | 3/5 | $525M | Weakest — flagship line is `trade_count=1`, a single block, not a sweep |
| SPY / QQQ / SPXW / TSLA / AMZN | mixed | 4–5/5 | $0.7–9.1B | **Hedge-flow signature** — all cum_flow_30d MIXED, not directional |
| MU / NVDA / META / AAPL / AMD / MSFT / INTC / IWM | **mixed direction on the same name** | 5/5 | — | Persistent in *participation*, not in *thesis*. Disqualified. |

**OPEX-week OI-build is non-discriminating.** Every ticker checked — candidates and controls alike — shows `consecutive_build_days: 5` with strongly positive net OI. Do not over-credit `opening_confirmed: true` this week.

---

## 4. LEAP Builds (6–24 months)

**EMPTY BOOK. Zero candidates clear the 6-of-9 gate.** LEAP share of the tape is 4.1% — the thinnest slice.

| Candidate | Gates | Disqualification |
|---|---|---|
| **SOFI** | **4 of 9** | `cum-premium-flow` 90d **−$51.4M** / 30d −$17.5M = wrong direction (hard disqualifier). `conviction-matrix` = **COVERED_CALL** (explicit auto-reject), confidence 24.8%. "Dark pool buying + call selling — yield enhancement, capping upside." |
| **XLF** | **4 of 9** | Headline was the biggest on the list (+32,459 contracts, **+1,417%** on the 2027-01-15 61C) — but per-date checks found **rolls on 4 of 7 covered dates** with wildly inconsistent balance_ratios (0.033 / 0.203 / 0.152 / 0.793) = mechanical OPEX-week roll contamination. `conviction-matrix` = BULLISH_ACCUMULATION ≠ DIRECTIONAL_LONG, confidence 25.7%. The LEAP strike itself is **bid-dominant** (ask 44 vs bid 117). |
| **TLT** | **~2 of 9** | 90d flow **−$125.9M**, 30d −$121.1M BEARISH. Today's roll is a **protective PUT roll-forward** — the opposite side from the bullish call-OI read. `conviction-matrix` MIXED, confidence **8.6%**. |

**Screen-stage disqualifications:** CGC (**$0.955** — fails the $5 floor), FRMI (`prev_bid_volume: 0`, no lit-tape confirmation), EQPT (micro-float), LCID (a **put**, bid-dominant), VFC/EWY/QQQ/EEM (all **puts**, all bid-dominant — bearish hedges, structurally wrong for a DIRECTIONAL_LONG mandate). **DRAM** (4 strikes, OI changes up to **+14,131%**) — `fz` confirms it is the *Roundhill Memory ETF, IPO'd 2026-04-02*; the percentages are a **new-fund base-effect artifact**.

> **⚠ Meta-finding — `oi-trend` carries zero information this week.** `uw historical oi-trend --days 10` returned `consecutive_build_days: 10` **identically for every ticker tested**, including deliberate zero-tape controls (AAPL, KO, IBM, TSLA). This extends accumulation-hunter's independent `--days 5` finding (uniform BUILDING across every mega-cap). **A uniform reading cannot establish name-specific persistence — Gate 1 was scored FAIL for every candidate regardless of its raw number.** → `/calibration-audit`.

---

## 5. Volatility Surface

### The VIX-vs-realised contradiction — RESOLVED (real, not an artifact)

VIX at 15.67 (LOW) alongside QQQ realised vol of 30.2% looks like a data error. It isn't. Manual recompute from `uw historical trend` closes:

- **SPY:** 30-sample daily stdev → **15.3% annualised** (matches Step 0's 15.52%). **1 day** with |ret| > 2% in the trailing 30.
- **QQQ:** 30-sample daily stdev → **29.8% annualised** (matches Step 0's 30.21%). **6 days** with moves ≥ 2.4% — 06-05 (−4.9%), 06-11 (+3.3%), 06-15 (+3.1%), 06-18 (+2.5%), 06-23 (−3.35%), 06-29 (+2.5%).

**Mechanism: genuine index-vs-constituent dispersion.** QQQ's concentrated mega-cap-tech weighting means a handful of violent single-name-driven days blow up its close-to-close realised vol, while SPY's 500-name diversification smooths the same days into a single >2% print. QQQ's 30d IV (23.12%) has **not** repriced to reflect it — the market is pricing mean-reversion of the chop. **The negative VRP is real. The QQQ buy-vol tilt is trustworthy.**

### Earnings vol — control band first

`front-end-iv-ratio` on **already-reported banks** (pure-OPEX control, near_dte=2 / far=30):

| JPM | BAC | WFC | GS | MS | C |
|---|---|---|---|---|---|
| 1.490 | 1.459 | **2.198** | 2.160 | 1.602 | 1.712 |

**Control band = 1.49–2.198 (mean ≈ 1.77).** These names have **no upcoming event** — this is pure OPEX mechanics. It is *wider* than the prior 1.38–1.75 finding: **the OPEX distortion is worse this cycle.** Any candidate must clear this band on matched methodology to count as signal.

| Ticker | ER | Days | Default ratio | vs band | Tenor-matched | Verdict |
|---|---|---|---|---|---|---|
| **NFLX** | 07-16 pm | **1** | **2.963** | **EXCEEDS top by 35%** | n/a (near leg already matches) | **SELL VOL** (half) |
| **GOOGL** | 07-22 | 7 | 1.609 (near_dte=**0**, artifact) | discard | **1.379** | BUY VOL |
| **META** | 07-29 | 14 | 1.670 (near_dte=**0**, artifact) | discard | **1.338** | BUY VOL |
| **MSFT** | 07-29 | 14 | 0.979 **FLAT** | below (mismatched tenor) | **1.299** | SKIP → **see below** |
| TSM | 07-16 | 1 | 1.642 | **WITHIN band** | — | SKIP — ER expiry *is* the OPEX expiry; inseparable |
| NOW | 07-22 | 7 | 1.035 FLAT | mismatched | 1.424 | SKIP — zero flow confirmation |
| INTC | 07-23 | 8 | 1.200 | below | 1.299 | SKIP — whole curve elevated; skew disagrees with flow |
| CDNS | 07-27 | 12 | 0.970 FLAT | mismatched | ~flat | SKIP — no kink shape exists |
| TXN | 07-22 | 7 | 1.864 | within band | — | SKIP — smooth monotonic decay, no localized bump |
| IBM | 07-22 | 7 | 1.359 | below | — | SKIP — event tenor is *lower* than the OPEX tenor |

**Only NFLX clears the control band.** Everyone else in the 1.3–1.4× tenor-matched range is a *moderate*, non-extreme event premium — real, but not rich.

**NFLX — SELL VOL, half size.** Front tenor (dte=2, exp 07-17, spans the print) avg_iv **147.8%** (n=27,021) → dte=9 74.5%. Ratio **2.963**. Back-month skew (dte=90) **COMPLACENT** (−0.0052) — **no tail hedge behind the front crowding**, which is why it's half size not full. Implied move **7.59%**. Structure: short iron condor on 07-17 (short ~68/80, long ~62/88 wings). Invalidation: back-month skew flips to TAIL_HEDGING pre-print, or the realised move exceeds 7.59%.

**MSFT — a genuine kink the earnings lane's tool structurally cannot see.** `front-end-iv-ratio` reads MSFT **FLAT (0.979)** — but that tool samples only curve *endpoints*. The raw `term_structure` array shows dte=12 (07-27, pre-event) **37.4%** (n=1,616) → dte=16 (07-31, first expiry after the event) **56.3%** (n=6,152) → dte=23 (08-07) back to 50.8%. A clean, well-populated **local peak in the belly**, bracketing a **double catalyst: earnings 07-29 + FOMC 07-28/29.** VRP positive (+0.0988). This is a real find — but MSFT carries **−$882M of 30-day bearish flow**, the hardest flow contradiction on the board, and it scored raw 1. Logged, not traded.

### Data verdicts on the anomalies

- **NFLX $73.68 — REAL.** 66-day series smooth and continuous ($95 → $73 over 4 months, no discontinuities); independently confirmed by `earnings-catalyst`. Tradeable.
- **SNDK $1,615 — REAL.** The apparent 615.83 → 1070.20 jump sits exactly on a **systemic `uw historical trend` data gap (~2026-03-27 → 2026-04-27, a full month of trading days absent)** — that's the artifact, not a 74% one-day move. Excluding it, SNDK genuinely traded $1,400–$2,270 over 6–8 weeks. **iv30d 141.8% ≈ realised 142.1%.**
  > **Corrective: SNDK's `iv_rank = 100` is a context flag, not a signal.** VRP is **FAIR (−0.0028)** — the curve is uniformly extreme because realised vol has genuinely been that violent, not because options are overpriced. No catalyst (ER 08-05). **No trade.**
- **`uw historical trend` data gap (~03-27 → 04-27)** present in both QQQ's and SNDK's series. Verified not to contaminate today's 30d window, but flag it for any calculation spanning it. → `/calibration-audit`.

### CRM adjudication

`multileg` found a **REAL, fresh, $88M delta-neutral strangle** (165P ×40,000 / 175C ×37,500 @ 2026-09-18; prior OI 3,106/7,556 vs 40k/37.5k traded = unambiguously fresh; all legs at 18:19:54) sitting on a kinked 09-18 expiry.

**Verdict: NOT actionable.** Three reasons: (1) **`side = no_side` on every leg** — long-vs-short vol is genuinely **undetermined**, and that matters enormously for risk (long = capped at the $88M debit; short = undefined). (2) The 09-18 hump is **confounded by quarterly quad-witching** — `expiry-heatmap` shows 09-18 is the **single largest premium-concentration expiry market-wide ($7.88B**, ahead of even monthly OPEX's $7.16B); quarterly OPEX pulls in more far-OTM strike listings, and `avg_iv` is **unweighted over strikes**, so the hump is at least partly contract-density. (3) VRP **FAIR (+0.0447)** — no edge. Net delta **+835 on ~17,000/side ≈ 0 → there is no directional thesis to extract.** Advisory only.

### Buckets

- **backwardation_calendars: EMPTY (honest).** Every liquid raw-BACKWARDATION name (MSFT, CDNS, CRM) has a front-end ratio at or below 1.0 — FLAT, not falling-from-panic. There's no panic to resolve.
- **skew_mispricings: none extreme.** MSFT dte=16 mildly COMPLACENT (0.973), NFLX dte=9 (0.956), CRM/SNDK NORMAL (1.035/1.047).
- **iv_outliers: all parity/wing noise.** CRM 90C/95C @ 2DTE (309–409% IV — **77–87pts ITM** vs $167 spot = parity artifact); NFLX $40C @ 2DTE (404% IV, **$33.68 ITM** = same class); NFLX $5P (1271% IV, **$300** premium); SNDK 550–760P (300–560% IV, **<$11K each** = lottery wings).

**VRP bias for the book — bifurcated, not uniform.** Broad-index/Nasdaq vol (QQQ −0.0709, verified) → **BUY VOL** tilt. Single-name event vol with genuine kinks (NFLX +0.1494, MSFT +0.0988) → **SELL VOL** tilt. **Do not extend the sell-vol instinct to SNDK/CRM just because raw IV rank reads 100 — VRP disconfirms it in both.**

---

## 6. Risk & Correlation

**Macro headline:** curve normal (+0.42), core CPI 2.81% vs core PCE **3.41%**, payrolls **+57k** (soft), 10Y **4.58% rising**, USD **strengthening** — mildly hostile to duration-sensitive longs. **Forward:** OPEX **T+2** (07-17); FOMC **T+9/T+10** (07-28/29) — outside every gate window; CPI released 07-14.

**Breadth cross-check (`fz`, advisory — independent lineage from `uw`):** advancers **257** vs decliners **246**, `pct_green` **51.09%**, avg change −0.16%, median +0.03%. Top mover PYPL +17.2%, worst PNR −15%. **No divergence flag** — the tape is genuinely flat-to-mixed, and this *agrees* with the TRANSITIONAL label. Note it does **not** corroborate `uw`'s much starker 35.3% bullish-flow reading — but those measure different things (price advance/decline vs options-flow direction), so this is a scope difference, not a conflict.

### Correlation clusters (against today's candidate union, not the static watchlist)

| Cluster | Members | Verdict |
|---|---|---|
| **megacap_tech_software** | MSFT/CRM **0.772** | CLUSTER — would keep MSFT (raw 1 > 0) |
| **NDX_beta_chain** | NVDA/QQQ **0.762**, QQQ/SNDK **0.750** | CLUSTER (chained via QQQ) — would keep NVDA. **Directionally heterogeneous** (NVDA opex_pin, QQQ vanna_squeeze, SNDK bearish_flow) — had any been sized, this was **one NDX-beta position, not three theses** |
| soft watch (0.60–0.70) | AMZN/GOOGL 0.695, AMZN/MSFT 0.694, NFLX/MSFT 0.645 | no penalty, surfaced only |
| inverse | CRM/SNDK **−0.607** | opposite bet, not a cluster |

> **⚠ `portfolio-correlation` data caveat:** `sector_breakdown` returned **100% "Unknown"** for all 13 names — the CLI's sector-metadata lookup is degraded today, so its CONCENTRATION warning is a metadata artifact, not a real read. Price correlations themselves populated normally. → `/calibration-audit`.

### Gate verdicts (all 9 keys — documentation; every gate is moot beneath an all-skip floor)

| Gate | Verdict |
|---|---|
| `regime` | n/a-moot — TRANSITIONAL confirmed from Step 0; no sized direction to conflict |
| `vrp` | n/a-moot — **would have −1 tier'd all four opex_pin names** (NVDA/IBIT/AMZN/PFE): their short-gamma pin structures fight a tape where realised (QQQ 30.2%) exceeds IV (23.1%) |
| `panic` | n/a-not-fetched — zero sized calls, and `front-end-iv-ratio` at OPEX EOD is a documented false-panic artifact this week. Fetching a known-contaminated number to gate nothing adds noise, not audit value |
| `cluster` | **evaluated** — two mechanical clusters found, zero actions (all members already skip) |
| `sector` | n/a-moot — nothing sized to penalize |
| `fundamentals` | **NA — stage 2b SKIPPED** (all-DROP precedent; gate operates on names that would be sized, can only cut size, nothing reached LOW) |
| `event_risk` | **documented, moot** — OPEX 07-17 = T+2 (≤T+3, **would fire −1 tier on any non-pin swing held through it**; the 4 pin names are the event play = exempt). FOMC T+9/T+10 = outside window, no-op |
| `debate` | **NA — stage 2c SKIPPED** (same precedent). `debate_residuals: {bull: null, bear: null}` board-wide — cause is stage-skip, **not instrumentation failure** |
| `rubric_regime` | **capped half** (OUT-OF-REGIME: rubric fitted UPTREND, current TRANSITIONAL, <30 post-freeze calls resolved) — moot, the skip floor binds first |

### Watchlist state — a correction to the standing record

> **The watchlist is NOT "globally empty/drained."** `~/.config/unusual-whales-pp-cli/watchlist.json` holds **86 tickers across 49 groups** back to `conviction_2026-05-11`. **Groups do not auto-expire** — "aged out" applies to the rolling 7-day *read window*, not the file.
>
> What *is* true: **no `conviction_2026-07-13` and no `conviction_2026-07-14` groups exist** — both empty write-backs were correctly executed. **What drained is the write-back stream, which is the system working as designed.** Latest daily group = `conviction_2026-07-10`; latest weekly = `conviction_week_2026-W28`.

**Rolling 7d universe:** 07-08 [SPY, PLTR, AMZN, SNDK, TSM] · 07-09 [NBIS] · 07-10 [NVDA, EWZ] · W28 [SNDK, NVDA, JPM, SOFI, META].

**Alerts — artifact-dominated, do not action.** Every name fired LARGE_DARK_POOL and/or OI_SHIFT, but **both alert types are contaminated by today's documented artifacts**: the LARGE_DARK_POOL prints (SPY $1.81B, AMZN $300M, NBIS $197M, EWZ $192M, META $181M, NVDA $164M) are the 20:00–21:56Z closing-cross leak, and the OI_SHIFT "net increasing" reads sit on the uniform-BUILDING `oi-trend` artifact. **Residual signal worth noting:** IV rank clusters at extremes across the carried tech names (SNDK 100, NBIS 100, META 98.5, TSM 80.7) into OPEX + earnings — options are expensive everywhere the fleet has looked, consistent with the contrarian abort.

**`fz` drift tripwire: SKIPPED (correctly)** — it runs against `conviction_2026-07-14`, which doesn't exist. No prior cohort to diff.

**Adverse-flow exit candidates: NONE.** There are no positions. The rolling groups are watch-only carries, never sized. **An exit candidate requires an entry.**

**Hedge sleeve: NONE.** The book is empty — net delta 0, directional skew undefined. There is no exposure to hedge, and buying index protection against a nonexistent book is a spend against nothing. Tail protection for non-system holdings is a portfolio decision outside this gate.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**EMPTY. No name reached HIGH or MEDIUM. No name reached even LOW.** Highest raw score on the board = **2**.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: not computable this session — zero calls sized, and the rolling `conviction_<date>` groups have no post-freeze closed calls at HIGH/MEDIUM to compute per-tier expectancy or payoff ratio from. This has now been the case for **four consecutive audit cycles** (the freeze-lift is blocked on exactly this: 0 post-freeze HIGH/MED calls).

### Full board (all DROP) — for the audit trail

| # | Ticker | Raw | Dominant class | 30d flow | Win rate (source) | Final |
|---|---|---|---|---|---|---|
| 1 | **BABA** | **2** | sector_rotation | **+$376.8M BULLISH** | null `NA(substrate)` | skip |
| 2 | **META** | **2** | earnings_vol | +$206.9M MIXED | null `NA(substrate)` | skip |
| 3 | **NFLX** | **2** | earnings_vol | −$166.6M BEARISH | null `NA(substrate)` | skip |
| 4 | ORCL | 1 | bearish_flow | −$210.3M MIXED | **0.5194** `backtest_clean` n=129 | skip |
| 5 | NVDA | 1 | opex_pin | −$222.1M MIXED | null | skip |
| 6 | IBIT | 1 | opex_pin | +$285.1M BULLISH | null | skip |
| 7 | AMZN | 1 | opex_pin | −$246.4M MIXED | null | skip |
| 8 | PFE | 1 | opex_pin | −$14.5M BEARISH | null | skip |
| 9 | GOOGL | 1 | earnings_vol | −$340.9M MIXED | null | skip |
| 10 | MSFT | 1 | earnings_vol | **−$882.1M BEARISH** | null | skip |
| 11 | CRM | 0 | multileg_directional | +$87.6M MIXED | null | skip |
| 12 | QQQ | **−1** | vanna_squeeze | −$234.8M MIXED | null | skip |
| 13 | SNDK | **−2** | bearish_flow | **+$817.6M BULLISH** (opposes short) | 0.5194 `backtest_clean` n=129 | skip |

Union median |cum_flow_30d| = **$234.8M** (n=13, all verified by direct pull).

### The tier-deciding judgements

**META (raw 2, one point from LOW).** The **+1 cum-flow accretion line was NOT awarded**, and that decided the tier. Verified 30d: net +$206.9M on **$19.49B gross = 1.06% net/gross**, and the tool's own label is **MIXED** (bullish $9.849B vs bearish $9.642B). Per the standing TSM precedent — *"net directional accretion" is not satisfied by a near-zero net against a huge gross* — a 1% imbalance on $19B of churn is not accretion.

> **The rubric ambiguity that decided a tier, again.** The sector-leader gate leg and the cum-flow accretion line **look at the same META flow and disagree**: the sector gate asks only "sign aligned AND |flow| ≥ $50M" (passes), while the accretion line asks whether the flow *is* accretion (fails on net-vs-gross). Both were applied as frozen. This is the **third consecutive session** where "net directional accretion" having no near-zero-vs-gross definition has been outcome-determinative. → `/calibration-audit`.

**SNDK (raw −2) — the board's biggest reversal.** sweep-tracker's $2.17B is **gross bearish** premium. The **net** 30d tape is **+$817.6M the other way** (90d +$1.93B bullish) → mechanical **−3 flow_conflict** against the short thesis. *Caveat for the audit:* that net is only **1.65% of a $49.6B gross** — the deduction fired on the union-median magnitude rule as written, on a number that is itself near-zero-vs-gross. **The same net-vs-gross ambiguity that spared META a deduction fired a −3 on SNDK.** That asymmetry is worth a look.

**QQQ (raw −1).** Cleared the confluence gate on two agents, then died on mechanization: the vanna/DEX **+1 does not fire** (no verified sign change — the agent itself reported `dex_flip_detected: FALSE`), and vol-surface's BUY VOL tilt earns nothing (the +1 line needs a KINKED/BACKWARDATION watch; QQQ's read is a **VRP level, not a term-structure dislocation**). Then **−1 flow_conflict_lite**: −$234.8M vs the LONG bias at **−0.34% of $68.8B gross** = MIXED; magnitude **exactly equals** the union median, so the −3 branch's strict `> median` test fails → lite.

### ⚠ Step 0 funnel contamination — the finding of the day

`multileg-strategist` proved the **single largest number in the funnel is financing**, with arithmetic:

> **`SPX +$5.907B` is a BOX SPREAD.**
> 2026-09-18: `650.52 − 52.42 − 29.52 + 422.42 = ` **991.00** → guaranteed 1000 → **5.21%/yr**
> 2027-12-17: `1259.90 − 355.50 − 617.50 + 649.50 = ` **936.40** → guaranteed 1000 → **4.72%/yr** (10Y = **4.58%**)
>
> Those are money-market rates. **All four legs tag "bullish"** (calls at ask, puts at bid) — which is exactly why the screener reports it as conviction. It is not.

**Today's multileg artifact share: 92.0% of premium (95.5% ex-0DTE)** — materially worse than the ~85% prior baseline. Only **$89.4M of $9.55B (0.94%)** is a real structure.

| Category | Premium | % |
|---|---|---|
| SPX **box financing** | $8.461B | **88.6%** |
| 0DTE (dropped per hygiene) | $0.349B | 3.7% |
| Ambiguous / unresolvable | $0.307B | 3.2% |
| Rolls (AAPL, GOOGL, EQT, HYG) | $0.194B | 2.0% |
| **REAL** | **$0.089B** | **0.94%** |
| Wash artifact (DRAM) | $0.064B | 0.7% |
| Buy-write / stock combo | $0.030B | 0.3% |
| Jelly roll (SOUN) | $0.027B | 0.3% |
| Deep-ITM financing (TLT) | $0.011B | 0.1% |

**Other Step 0 headline numbers that dissolved on inspection:**

- **AAPL +$112M and GOOGL +$83.6M are ROLLS**, proven on prior-OI. AAPL: 8/21 345C prior OI **93,187**, traded 73,133 → 10/16 360C prior OI 1,623, traded 72,486 (sizes match to **0.9%**) = roll up-and-out. GOOGL: 8/21 415C prior OI 57,845, traded 58,050 — **99.6%, the entire book** → 9/18 410C = roll out-and-down. **Not new money.** This directly refutes earnings-scout's GOOGL flow-alignment leg.
- **sweep-tracker's SPX 7000C triple-print** (3× $130.1M @ 15:44:38 / :38 / :39Z) is confirmed but **misclassified** — these are **child fills of the 10,000-lot C7000 box leg** at identical price $650.52, **not** a stale-NBBO cross. Same exclusion, different reason.
- **DRAM** — the largest single-name structure on the tape (137k contracts) — is a **WASH print**: open 14:40:41 buy 75C/sell 100C ×67,000 @ **$2.56 debit**; close 17:59:26 sell 75C/buy 100C ×66,999 @ **$2.56 credit**. Identical prices 3h19m apart **while DRAM fell 6.3%**. P&L exactly zero, EOD position = 1 spread. Its 137,939 volume is a **double-count**.
- **TLT 80C/80.5C printed $0.49 on a $0.50-max spread (98% of max)** — the INTC 80C/81C financing pattern exactly. Risk $0.49 to win $0.01.
- **SOUN's "bearish −$26.8M net flow" is a jelly roll** — the 10P leg's $16.78M got tagged bearish. Same class as the dividend-capture blind spot.
- **Step 0's C19 single-leg scan returned IBM 275P (spot 213.71, δ −0.973) and MSFT 450P (spot 396.58, δ −0.968) as "Tier-1 CONTRARIAN_SHORT"** — both are **deep-ITM near-parity = financing/stock-substitution, not conviction**. The C19 scan has no parity filter. → `/calibration-audit`.

### C19 accrual note (advisory, 0 points)

The `bearish_flow` class returned **WR 0.5194 (n=129, clean protocol)** vs a same-window SPY-short benchmark of 0.3333 → **market excess +18.6pp**. Second consecutive positive read for a class that scores ~0 rubric points. **Accrue to the register; do not act** — the rubric is frozen and this is exactly the pre-registration discipline the freeze exists to enforce.

**Backtest substrate defect:** `signal-backtest` shows SNDK `price_on_signal ≈ 1674` vs the verified real **$73.68** — the series behind the tool appears to be a different/unadjusted SNDK listing. Direction grading is internally consistent (same series both ends) so the 7 SNDK rows were kept, but this belongs in the next audit's substrate caveats.

### Conviction-scoring rubric (verbatim, frozen `2026-06-12`)

```
Daily conviction score = Σ:
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna-squeeze setup in trade direction
      — trigger must be a verified SIGN CHANGE, not a level: sign(net_dex) on the latest session opposite to
      ≥3 consecutive prior sessions, read from dated `uw options-structure dex --date` calls (≥4 to verify the
      prior-session sign run; ~11 for the trailing-median floor), with |net_dex| on the flip day ≥ 0.25× the
      trailing-10-session median |net_dex|; evidence string must cite both dated values. Vanna disjunct
      additionally requires a dated VIX source for the falling-VIX leg — no out-of-band VIX fills.
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified institutional-tier
      confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms (sign aligned AND
      |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1.
  +1  multi-day OI build (oi-trend BUILDING, --days ≥ 5)
  +1  conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: only when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +1  cumulative-premium-flow shows net directional accretion in trade direction (30d) — INTENT-SCREENED:
      award only when (a) no C28 distribution_flag on the name, AND (b) on dividend payers inside an ex-div
      window, the accreting prints are NOT deep-ITM sub-parity calls. Screen failed or unevaluated → 0.
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector — CONDITIONAL:
      (a) sector persistence_score ≥ 0.6 AND (b) cum_flow_30d direction aligned AND (c) |cum_flow_30d| ≥ $50M.
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising pc-ratio-zscore (VRP positive)
      — an INFORMED-FLOW CONTINUATION penalty, not "crowd is wrong, fade it".
  -3  flow_conflict — cum_premium_flow 30d direction *clearly opposite* dominant_signal_class (signed-sum sign
      flip + magnitude > today's union-median |cum_flow_30d|, or explicit OPPOSITE label)
  -1  flow_conflict_lite — 30d cum_premium_flow read is MIXED (signed sum near zero, or aligned but
      bottom-quartile magnitude in today's union)   [mutually exclusive with flow_conflict — apply ONE]
  # TIER GATES (risk-monitor, Step 2d) — contribute 0 to raw_score, never appear in score_components:
  -1  [TIER GATE] risk-monitor flags in correlation cluster (pairwise corr ≥ 0.70) — −1 TIER
  -3  [TIER GATE] market-regime conflicts with trade direction — −1 TIER (regime gate)
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | **HIGH** | full (subject to Step 3a load-bearing gate + win-rate gate) |
| 7–8 | **MEDIUM** | half (subject to win-rate gate) |
| 3–6 | **LOW** | starter / watch-only |
| ≤ 2 | **drop** | filtered by the quant's drop floor |

**Tier-cut status (2026-06-12):** the ≥9 HIGH cut **failed its scheduled re-confirmation** — bands inverted on the first post-UPTREND window (HIGH 0.222 / MED 0.214 / LOW 0.444). Cuts retained under the P0.1 freeze but carry **no validated ranking claim**; the P0.6 out-of-regime guard caps all sizing at half in the interim.

---

## 8. Watch-only — single signal, no confluence

For journaling. **Not for entry.**

| Ticker | Flagging agent | Signal | Why it stopped here |
|---|---|---|---|
| **BABA** | sector-rotation only | Passes all 3 sector-leader gate legs; **+$376.8M / +$696.9M BULLISH 30d/90d — the cleanest directional flow on the entire board** | One agent. Raw 2 < 3 floor. **The most interesting name of the session — genuinely worth watching for a second agent to confirm.** |
| **MSFT** | vol-surface only | Real belly kink at 07-31 (56.3%, n=6,152) bracketing ER 07-29 + FOMC 07-28/29; VRP +0.0988 | One agent (earnings-scout independently SKIP'd it). **−$882M 30d bearish flow** is the hardest contradiction on the board. |
| **GOOGL** | earnings-scout only | Real kink dte=9 (54.6%, n=7,308), ER 07-22 | **Actively refuted twice** — multileg proved the flow is a roll; sector-rotation fails it on −$341M wrong-direction flow. |
| **NVDA** | opex-pin only | Rank 1: pin 215, dist 1.19%, OI 99,100, gex_at_pin **+$134.2M** | One agent. accumulation-hunter rejected it (closing-cross); sweep-tracker Tier 3 (mixed direction). |
| **IBIT** | opex-pin only | Rank 2: pin 37, dist **0.56%** — tightest on the board, gex_at_pin +$111.7M | One agent. Pin thesis is delta-neutral — the +$285.1M bullish flow earns nothing without a directional co-flag. |
| **AMZN** | opex-pin only | Rank 3: pin 250, dist 1.91%, gex_at_pin +$49.6M | One agent. sweep-tracker's bullish 4/5 **failed** the hedge-flow screen (−$246M MIXED). |
| **PFE** | opex-pin only | Rank 4: pin 25, dist 0.83%, gex_at_pin +$10.9M | One agent. |
| **SNDK** | sweep-tracker only | Tier-1 bearish 5/5, $2.17B gross, opening-confirmed | vol-surface says **NO TRADE** (iv_rank 100 is context, not signal; VRP FAIR). Quant's net-flow check fired **−3**. |
| **ORCL** | sweep-tracker only | Tier-1 bearish 4/5, 07-17 puts $20.2M, `oi-trend` BUILDING 7 days | One agent. **Note the build is two-sided** (8/14 115P *and* 150C ×2). |
| **CRM** | multileg (real) / vol-surface (rejected) | Fresh $88M delta-neutral strangle on a kinked 09-18 | **Delta-neutral — no directional thesis exists to extract.** Quad-witching confound. |
| **KRE** | sector-rotation (ETF tape) | The real Financials rotation leader — buy-side DP ($37.5M block) + ask-side calls at 75/80 | ETF-tape lane is **advisory, 0 points**. |
| **EWY** | sector-rotation (ETF tape) | Top ETF inflow +$46.3M, BULLISH-persistent, buy-side blocks | Advisory. Geographic — no GICS leader extraction. |

### OPEX pin book (ranked, for reference — none scored above raw 1)

| Rank | Ticker | Pin | Spot | Dist | OI@pin | gex_at_pin | Structure |
|---|---|---|---|---|---|---|---|
| 1 | NVDA | 215 | 211.94 | 1.19% | 99,100 | +$134.2M | Broken-wing fly biased to 215 |
| 2 | IBIT | 37 | 36.80 | 0.56% | 46,274 | +$111.7M | Iron fly @ 37 |
| 3 | AMZN | 250 | 254.79 | 1.91% | 44,205 | +$49.6M | Broken-wing fly biased to 250 |
| 4 | PFE | 25 | 24.73 | 0.83% | 58,006 | +$10.9M | Iron fly @ 25 |

**The index "pins" that usually anchor an OPEX book are NOT credible this week — flag to the desk explicitly:**
- **IWM (290, 1.93%)** looked best on distance, but `gex_at_pin = **−$117.3M**` — the near-money strike sits in a **negative-gamma pocket**. The high OI there is not a magnet, it's a **short-gamma landmine**. This is the clearest case of "pin_score looks good, gamma sign says no."
- **SPY (720, 4.61%), TLT (88, 4.48%), QQQ (700, 2.44%), HYG (78, 2.25%)** — all far-OTM OI mass, not enforceable 2-day pins.
- **EEM (65), NFLX (75)** — FULLY_NEGATIVE GEX at the pin strike.
- **ET, TSLA, MSFT** — passed distance and gamma sign, but sit in the **bottom tercile of `pin_score`**.
- `uw oi opex-concentration` was **unusable** — unfiltered output is 100% sub-$2 microcap junk (CALC, ALEC @ $1.50, JSPR @ $0.70, SGMOQ, HUYA, SSTI), zero overlap with the liquid pin universe.

---

## Appendix — tool caveats logged this session (for `/calibration-audit`)

| # | Tool | Finding | Severity |
|---|---|---|---|
| 1 | `uw options-flow sector-flow` (**fleet PRIMARY**) | Reports **gross turnover, not net positioning**. Says Tech **+$2.26B** while `market-regime` says **−$82M** — opposite sign, ~27× scale. Refuted 3 ways (every mega-cap net-bearish 30d; XLK persistently bearish + 2027/2028 LEAP put hedges; scale implausibility). **The designated primary is the noisier tool.** | **HIGH** |
| 2 | `uw historical oi-trend` | Returns `BUILDING` / `consecutive_build_days: 5` (and `10` on `--days 10`) **uniformly across every name tested, including zero-tape controls**. Carries **zero discriminating information** during OPEX week. Independently found by both accumulation-hunter and leap-radar. | **HIGH** |
| 3 | `uw insights institutional-accumulation` + `uw dark-pool extended-hours` | **Closing-cross leak confirmed** — the 20:00–21:56Z print dominates `top_price_levels`; `extended-hours` re-serves the same prints (classifying post-16:00-ET as "extended hours"). Whole mega-cap board affected. **The tool should exclude the window in its own aggregation.** 3rd+ recurrence. | **HIGH** |
| 4 | `uw options-flow single-leg` (C19) | **No parity filter.** Returned IBM 275P (spot 213.71, δ −0.973) and MSFT 450P (spot 396.58, δ −0.968) as "Tier-1 CONTRARIAN_SHORT" — both deep-ITM financing legs. Only **4 of 453** raw signals scored, and 2 of the top ones are artifacts. | **HIGH** |
| 5 | `uw options-structure gex` — QQQ | **Sub-320 ZGL artifact RECURS** (300.35 vs spot 717.41, 58% below). Also: **tool `regime` label contradicts `total_gex` sign** (POSITIVE label, −$354.6M) — a *new* second failure mode. | **MEDIUM** |
| 6 | `uw options-structure gex` — IWM | **ZGL `null`**; 10d history shows 155/194/199/130/150 against spot ~293–300. Worse than QQQ. `regime_flip_dates` returns null. | **MEDIUM** |
| 7 | `uw options-structure gex` — SPY | `total_gex` **positive** (+$1.2B) while `regime` label says **NEGATIVE**. Label tracks local spot-vs-ZGL crossing, not book aggregate. | **MEDIUM** |
| 8 | `uw options-structure front-end-iv-ratio` | (a) **Default near-dte is blind to events >2–3 days out** — reads FLAT on 8/10 names with verified real kinks. (b) **`near_dte_actual=0` silently substitutes today's 0DTE bucket** (META, GOOGL) — a *distinct* second failure mode from the known Friday-EOD snap. (c) **Endpoint-only sampling structurally cannot see mid-curve/belly kinks** (MSFT). | **HIGH** |
| 9 | `uw options-structure iv-term-structure` | **`kink_expiry` returned `null` on 10 of 10 names** despite manually-verified real kinks (NFLX, MSFT, META, GOOGL, NOW, INTC). **Field is unusable as a gate**; all kink detection done by hand off the raw array. Independently confirmed by two agents. | **HIGH** |
| 10 | `implied_move_perc` vs `avg_iv` | Gap measured live: **NFLX ~1.4×, GOOGL ~4.7×, META ~5.7×** — **ticker/tenor-dependent, NOT a fixed 10–40×**. Scales with far-OTM illiquid strike count (`avg_iv` is unweighted over strikes). Use `avg_iv` for **shape only**, never move-size. | **MEDIUM** |
| 11 | `uw historical iv-percentile-zscore` | **Every call returned `dates_used: 65`** — below the 120-day floor. **All percentile reads this session are provisional**, not an isolated case. | **MEDIUM** |
| 12 | `uw historical trend` | **Systemic data gap ~2026-03-27 → 2026-04-27** (a full month of trading days absent) in both QQQ's and SNDK's series. Creates a **fake 74% jump** in SNDK. Verified not to contaminate today's 30d window. | **MEDIUM** |
| 13 | `uw historical signal-backtest` | **SNDK `price_on_signal ≈ 1674` vs verified real $73.68** — the underlying series appears to be a different/unadjusted listing. Direction grading internally consistent, rows kept. | **MEDIUM** |
| 14 | `uw risk portfolio-correlation` | `sector_breakdown` returned **100% "Unknown"** for all 13 names — metadata lookup degraded; its CONCENTRATION warning is an artifact. Price correlations fine. | **MEDIUM** |
| 15 | `fz screen` (**NEW**) | **Ticker field duplicates the leading character** — CPIX→`CCPIX`, MRVI→`MMRVI`, DAVE→`DDAVE`, NET→`NNET`, CRWD→`CCRWD`, QLYS→`QQLYS`, ABCL→`AABCL`. **100% of rows, both `--view ownership` and `--signal` lanes.** Deterministic → de-duped mechanically this session; lanes are advisory/0-points so no scored impact. | **MEDIUM** |
| 16 | `uw oi opex-concentration` | Unfiltered output is **100% sub-$2 microcap junk** (CALC, ALEC, JSPR, SGMOQ, HUYA) with **zero overlap** with the liquid pin universe. Unusable for cross-ref without a liquidity pre-filter. | **LOW** |
| 17 | `uw insights analyst-vs-flow` | **Returned zero analyst data for all 6 names queried** — only `options_flow` populated. Confirms the standing "analyst-vs-flow unwired" note. The analyst-divergence leg of the earnings playbook is **currently unusable**. | **MEDIUM** |
| 18 | `uw hot-chains sweep-persistence` | `consistency_score` is exactly `sessions_in_top/5` — a **participation share, not a directional-agreement check**. `dominant_direction` is a window net tilt, not verified per-day agreement. | **LOW** |
| 19 | `uw options-flow sector-flow-persistence` | **9 of 11 sectors tied at persistence_score 1.0**; the ≥0.6 gate clears 10 of 11 → **non-binding**. Reconfirms 06-12. | **MEDIUM** |
| 20 | Rubric — "net directional accretion" | **Third consecutive session it decided a tier with no near-zero-vs-gross definition.** Today it *withheld* +1 from META (1.06% of $19.49B) while a **−3 flow_conflict fired on SNDK at 1.65% of $49.6B**. Same ambiguity, **opposite directions.** | **HIGH** |
| 21 | `uw historical vrp` | Requires `--symbol` (errors without). The command doc's Step-0 example omits it. | **LOW** |
| 22 | Yahoo chart API `^VIX` | **Confirmed WORKING for 2026 dates** — returned 15.67 for 07-15, matching Step 0 exactly, plus a clean dated series. Re-confirms the 07-11 refutation of the "2025-anchored" note. | **RESOLVED** |
| 23 | Watchlist state | **"Globally empty/drained" is FALSE** — the state file holds **86 tickers across 49 groups** back to 2026-05-11. Groups **do not auto-expire**; "aged out" refers to the rolling 7-day read window. The *write-back stream* drained (no 07-13/07-14/07-15 groups) — that is correct behaviour. | **CORRECTION** |
