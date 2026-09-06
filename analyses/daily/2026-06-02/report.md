# Daily Market Analysis — 2026-06-02

## Executive Summary
- **Regime + GEX state:** **TRANSITIONAL / UPTREND** at the highs — SPY 759.57 (+5.4% 30d, −0.11% from 90d high, >20 & 50 SMA), VIX 15.77 (LOW). SPY/QQQ are **long-gamma** (vol-suppressed pin); IWM sits **un-pinned at zero-gamma**. The tell of the day: **options-flow breadth is only 37.4% bullish** (2,322 bull / 3,881 bear of 6,203) at index highs — mega-cap distribution beneath a green tape. Sector lean: memory/semis/optical bid, mega-cap software/platform distributed.
- **Next-session GEX (SPY/QQQ) — advisory, see §2:** SPY long-gamma, ZGL unreliable (effective flip ~754), **call wall 760** (dominant magnet) / **put wall 754** — *fresh & unstable (5 flips in 7 sessions)*. QQQ long-gamma, **call wall 747 / put wall 742** — *stable (8 sessions held)*. Both → premium-selling iron flies; SPY lighter (knife-edge).
- **Top swing build:** **None at size.** Every directional swing gates to **skip** — NFP at T+3 cuts each one tier, the bull/bear debate failed to clear all four crowded longs (bear ≥ bull on TSLA/AMD/MRVL/SNDK), TSLA is fundamentally CAUTION'd, and the long book is **beta, not alpha** (market-excess −0.23). The highest *score* is TSLA (raw 9 — recorded **MEDIUM** under the validator's conservative ≥10-HIGH band; the P1.3 ≥9-HIGH cut is in-sample-only, pending the ~06-12 re-confirm) but it does not survive the gate stack regardless.
- **Top LEAP candidate:** **None.** No name clears 6-of-9; POET is the lone near-miss (5/9, conviction-matrix 12.2%). All theme names are MIXED on 90d cum-flow — short-horizon flow, not long-dated accumulation.
- **Only positions that survive at size:** the two **earnings-vol plays — AVGO (half, calendar) and MDT (half, sell-vol)** — and only because they *are* the event and resolve 06-03, before NFP.
- **Biggest risk:** **Event density + a beta book.** NFP (06-05) → CPI (~06-10) → FOMC (06-16/17) inside any swing horizon, into a market at highs with 37.4% bullish flow breadth. The marquee trap — **MU "distribution" looked like a short but fundamentals VETO it** (4/4 beats, rev +85%, shortage-to-2030); **SNDK's +$1.2B "bullish premium" is actually 4.3× put-writing distribution.** Carry the institutional risk-off hedge (HYG bear-put-spread + VIX call ratio are already on the tape).

---

## 1. Regime & Gamma State
- **`uw risk market-regime`:** **TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity."** Trend **UPTREND**. SPY 759.57, +5.4% 30d, −0.11% from 90d high, above 20-SMA (743.31) and 50-SMA (707.84). Breadth: **37.4% bullish flow** (2,322 bullish / 3,881 bearish of 6,203 optionable). Guidance: **half position sizes, defined-risk, iron condors in range.** A green index with sub-38% bullish flow breadth = distribution into strength.

- **Per-index gamma (current-state EOD book):**

| Index | Spot | Zero-gamma (ZGL) | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 759.48 | unreliable (327; eff. flip ~754) | **+1.757B** | long-gamma (deepest of month) | **760** (dominant +1.358B magnet) | **754** (flip just below spot) |
| QQQ | 745.80 | unreliable (305) | **+462M** | long-gamma (held 8 sessions) | **747** (746/747 ATM cluster) | **742** |
| IWM | 291.66 | ≈ at spot (un-pinned) | **≈ −3M (zero-gamma)** | NEAR_FLIP / short-lean | call shelf 290–295 | put-gamma hole 274–282 |

  SPY/QQQ hedging dampens vol (mean-revert/pin); **IWM is the one index where a directional break is *un-cushioned / trend-amplified*** — and its swing DEX deteriorated −27% over 5 days. §2 carries the forward read of SPY/QQQ.

- **`uw options-flow dte-volume-share`:** 0DTE 19.6% / weeklies 31.2% / monthlies 33.5% / LEAP 6.9% — **BALANCED** (monthlies+ 40.4% = healthy institutional share; not a retail-dominated tape).
- **`uw historical vrp`:** SPY **0.037 — FAIR** (no edge); QQQ **0.059 — PREMIUM_SELLING** (IV30 0.214 vs realized 0.155). Tech vol is rich vs realized → premium-selling / calendar bias on QQQ-complex names.
- **Macro backdrop (`scripts/fred_macro.py`):** Yield curve **normal +0.41** (10Y–2Y). Core CPI **2.99%** YoY / headline **3.95%** (Apr, ~2mo lag — sticky, above target). Unemployment **4.3%**, payrolls **+115k** MoM. 2Y **4.05** (+0.17 30d), 10Y **≈4.46** (derived; FRED daily 10Y/USD/PCE series 429-throttled this run). Late-cycle, sticky-inflation, no recession signal.
- **Forward `event_risk` (next ~10 sessions):** **NFP Fri 06-05 [HIGH, T+3]** · CPI ~06-10/11 [HIGH] · PPI ~06-11/12 [MED] · **FOMC + SEP 06-16/17 [HIGH]** · PCE ~06-26 [MED] · jobless claims weekly Thu. Single-name: **AVGO 06-03 PM, MDT 06-03 AM, CIEN/DOCU 06-04, MU 06-24.** An **event-dense fortnight** — every swing book opened today eats NFP → CPI → FOMC.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book (OI persists overnight) read forward as the prior for the next open. Prose-only, **0 conviction points**, no backtested predictive claim. SPY & QQQ only.

| Index | Regime · ZGL | Call wall / Put wall | One-line structure bias (next-session 0DTE) |
|---|---|---|---|
| **SPY** | **long-gamma** · ZGL unreliable (eff. flip ~754) · total GEX +1.757B | **760** (dominant +1.358B magnet, ~0.07% above spot) / **754** (top of −GEX shelf, ~0.7% below) | Walls tight (~0.8% band) → **iron fly / short straddle centered ~760** (the magnet). **754 is the hard invalidation** — lose it and drop into the short-gamma shelf (flip to debit put vertical). |
| **QQQ** | **long-gamma** · ZGL unreliable · total GEX +462M | **747** (GEX peak; 746/747 ATM cluster) / **742** | Walls slightly wider (~1.2% band) → **iron fly ~746–747 / tight condor** fading pokes toward 750/755. QQQ VRP = PREMIUM_SELLING doubly supports. |

**Asymmetry:** QQQ's long-gamma regime is **durable** (held POSITIVE 8 straight sessions); **SPY's is one-day-fresh and whipsaw-prone** (flipped NEG→POS today, 5th flip in 7 sessions, spot oscillating ±$1 around the flip). Size SPY lighter; respect 754.

**Mandatory caveats:** (1) **EOD = prior, not target** — fresh 0DTE OI re-computes ZGL/walls in the first 30–60 min; re-read after the open. (2) **Gap risk** — the **06-05 (NFP) expiry is already #1 by volume**; an overnight macro gap can blow through these walls. (3) **ETF book, not the cleaner SPX/NDX index book.** (4) **Tooling can't isolate the D+1 expiry** (`gex --dte-max 1` errors) — this is the standing 0–45 DTE proxy.

### 2a. Next-session 0DTE premium-selling setup (validated stack — `scripts/zerodte_setup.py`)
> Advisory, **delta-neutral, 0 rubric points.** NOT a guaranteed edge (validation sample has no vol shock → short-vol tail unsampled). Backtest verdict: **GO_PREMIUM_SELL_INTRADAY** (SPY 97.2% / QQQ 94.4% open-entry win rate).

| Index | Sell premium? | Vol state · VIX | Implied / expected range | Size | Structure | Entry rule |
|---|---|---|---|---|---|---|
| **SPY** (≈SPX, validated identical) | **Yes** | LOW · 15.77 | 0.66% / 0.69% | **0.5×** | iron fly / short straddle @ **759.88**, wings ≈ ±0.69% (long-gamma: quieter) | Enter at/after open once gap resolves; hold to close; **never overnight**. Stand aside if it gaps beyond the wings. |
| **QQQ** (weaker — Nasdaq index book unavailable) | **Yes** | LOW · 15.77 | 1.12% / 1.18% | **0.5×** | iron fly / short straddle @ **746.8**, wings ≈ ±1.18% | Same. |

No stand-aside flag fired (VIX not spiking, no front-end backwardation at index level). **Direction: none — delta-neutral.** Half-size because VIX is LOW (thin edge). Note: this is intraday-only and orthogonal to the directional book below.

## 2a. Swing Dealer Positioning (1–4 weeks)
- **Indices:** SPY **NEUTRAL-LONG** (net DEX +61B, total_gex deepest +gamma of the month, front-end IV 0.965 calm) — positive-gamma pin at highs by inertia. QQQ **NEUTRAL** (DEX +71B but gamma cushion fading to +462M, the week's lowest). IWM **NEUTRAL → SHORT-lean** (net DEX +9.7B, **−27% over 5d**, sitting at zero-gamma — un-cushioned).
- **No DEX sign-flips and no vanna squeezes anywhere** — every index book is call-heavy (wrong side for a squeeze) AND VIX bottomed 05-29 then ticked up, so the squeeze precondition fails twice. The `gex-time-series` regime-flip dates are ZGL-crossing artifacts (demoted).
- **Single names (DEX confirms the rotation):** **MU** DEX +41.8B *accelerating* long (but earnings backwardation + Tier-1 bearish put tension — see §3/§6); **MRVL** DEX doubling +8.8B; **AMD** DEX +18.4B accreting — all confirm the semis bid. **MSFT SHORT-lean: DEX 5×'d (+11.5B) while the stock *fell*** with bearish premium (−$91M) and **front-end IV 1.834 (extreme real panic, no earnings)** — trapped call-longs / genuine downside fear (the cleanest mega-cap-software short read, though it does not survive the flow-conflict gate — see §6).

## 2b. Sector Rotation
- **`sector-rotation-strategist` regime call: `no_change` (low confidence).** All 11 GICS sectors print 5-day persistence_score = 1.0 (every sector net-inflow — direction non-discriminating; rank by magnitude/acceleration). No canonical defensive↔cyclical or growth↔value pattern (growth Tech + cyclical Energy + defensive Utilities all rising at once). **The real, tradeable rotation is intra-sector**, not top-level.
- **Intra-tech:** OUT of mega-cap software/platform (MSFT, META, GOOGL, NVDA, PLTR, NOW net bearish premium) → INTO memory/semis/optical (SNDK +335M, MU +55M, MRVL +53M, LITE +31M, AMD +13M). **Energy** (HAL +45M; +$0.35B sector, a 5× jump) and **Utilities** (+$0.13B, 2.5× jump — GEV/TLN/OKLO power-and-nuclear) accelerating.

**ETF flow tape (advisory — 0 rubric points; instrument layer the GICS aggregates can't see):**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| **IGV** (software) | inflow (+28.3M) | BULLISH (5d) | top print passive/redemption-lean | Aug 110C/115C accumulation | **agree** (Tech) — but software *not* abandoned wholesale; the OUT is mega-cap-platform-specific | MSFT/NOW/ORCL/CRM basket |
| **XLE** (energy) | inflow (+16.4M) | BULLISH (5d) | creation prints at/below mid | Jan 45C 10k-lot synthetic long + Jun 60C chase | **agree** (Energy), accelerating → high-conviction | HAL, DVN, CVX |
| **KRE** (regional banks) | inflow (+2.1M) | BULLISH (5d) | 53.8M block (hedging/creation) | **Jun 70.5C/73C ask-side urgency** | **agree** (Financials, ETF-surfaced edge) | regional banks |
| **XLY** (US discretionary) | **outflow (−4.5M)** | BEARISH (5d) | redemption-flavored | lone 110P hedge | agree w/ OUT (US-disc); China ADRs (BABA/PDD) are a *separate* inflow book — do NOT short them | basket |
| **EWT** (Taiwan) | outflow (−1.1M) | BEARISH | prints below mid | mixed | n/a (geographic) — corroborates SMH softness | basket |
| **SMH** (semis) | **mixed (−56.0M, largest mag)** | MIXED (no persistence) | prints at/above mid | **hedged two-sided** (700C buy AND 600P/520P buy) | **disagree** → **watch-only** — confirms intra-tech churn (broad basket trimmed/hedged while single-name memory/optical pulls fresh inflow) |

---

## 3. Swing Setups (1–6 weeks)
**Every directional swing gates to `skip` today** — this is a gate-the-book day, not a deploy-the-book day. Ranked by conviction score; sizing is the post-gate result.

### 3a. Long swings (regime-aligned) — all SKIP

| Ticker | Score / Tier | Thesis | Structure (rule-based) | Invalidation | Sizing |
|---|---|---|---|---|---|
| **TSLA** | 9 / MED† | Institutional DP accumulation (mega all-buy, b/s 1.87), +$378M/30d cum-flow, OI +1.27M 5/5, signal-confluence 5 — but on a 404× PE / −39% EPS name | Long call / call debit spread (IV cheap, rank 17) | **Loses the $423.74 DP defense shelf** | **skip** (CAUTION −1, event_risk −1, debate −1) |
| **AMD** | 8 / MED | DEX +18.4B, +$476M/30d, beat-streak EPS +123%, MI450/agentic-AI; sector leader | Bull put spread (IV rank 92) | Loses ~$500 / DEX rolls under +13B | **skip** (event_risk −1, debate −1; **beta** market-excess −0.23) |
| **MRVL** | 7 / MED | DEX doubling, sweep Tier-1 OI-opening, Huang "next trillion-$" Computex catalyst; rev +34%, net 29% | Bull put spread (IV rank 97) | RSI 86, **+22% past mean target** — loses the Computex gap | **skip** (event_risk −1, debate −1; beta; extreme RSI) |
| **SNDK** | 5 / LOW | Largest sector net-flow +$1.2B/30d, 4/4 huge beats, $3,250 PT — **BUT the +$1.2B is 4.3× PUT premium / put-writing; DP accumulation NEUTRAL (sells > buys); dealer DEX neutral** | — (conflicted) | Beta 5.01, +4,640% off low, RSI 70 (parabolic) | **skip** (cluster −1, event_risk −1, debate −1; flow is distribution) |
| **ORCL** | 4 / LOW | +$206M/30d cum-flow, OI +390k — but call OI being closed (distribution_flag) | — | earnings ~06-10 | **skip** (flow flipped **bearish** vs prior thesis — exit candidate) |
| **INTC** | 4 / LOW | Tier-1 bullish sweep 4/5 + OI +184k, +$157M/30d | — | ⚠ **corporate-action price distortion late May — verify before any execution** | **skip** (event_risk −1; data caveat) |
| **KRE** | 4 / LOW | Multileg Jun18 73C call spread + signal-confluence 4 (regional banks) | Call spread | — | **skip** (event_risk −1 — NFP is a direct regional-bank rate driver) |
| **HAL** | 3 / LOW | Energy rotation leader, PCR 0.019, signal-confluence 4 | — | — | **skip** (event_risk −1) |

> **Distribution caution (C28, advisory):** **TSLA** carries a `distribution_flag` — OTM 500–600C OI being closed for profit while the thesis reads accumulation. 0 points, does not change sizing, but it sharpens the CAUTION. **ORCL/INTC** also show upside-call OI closing.

### 3b. Short / fade swings (defined-risk only) — SKIP / watch-only
- **MU — SHORT → 🛑 watch-only (fundamentals VETO).** The headline conflict: bullish momentum/DEX/sector vs **bearish institutional DP distribution (mega/block 0.479/0.459 into a +137% run) + Tier-1 OPENING_PUT_PRIME (1070P $5.0M) + 610P +22.7k OI opening + cum-flow −$60M/30d, −$188M/90d (flow confirms bearish).** The quant scored the short raw 7. **But fundamentals VETO it 3-of-3:** 4/4 earnings beats (most recent +27%), rev +85% / EPS +412%, SK Hynix shortage-to-2030 — the "distribution" is profit-taking/hedging on an *improving* name, and **earnings 06-24 (22d) sit inside any swing horizon** as a beat-streak catalyst the short must survive. Both debaters landed at 0.55: **no size either side until after 06-24.**
- **MSTR — SHORT → skip.** Tier-1 opening put + bearish_extreme +4.55σ (smart-money-confirmed hedge, not a fade), cum-flow −$54M/30d. Gated: regime conflict (UPTREND vs short) −1 + event_risk −1.

**Near-term sweeps (informational, 0 rubric points):** genuine persistent, OI-opening-confirmed urgency was narrow — **MRVL (4/5 bullish, call-side OI +60k)** and **INTC (4/5 bullish, OI +184k)** were the only first-class directional builds; everything mega-cap (SPX-complex, TSLA, NVDA, META, AMD) was hedge flow that failed the cum-flow alignment gate. The sharpest *directional* tell on the tape was bearish: **MU's 610P +22.7k OI opening** and **SNDK's tape flipping to puts** against its own bullish persistence label.

---

## 4. LEAP Builds (6–24 months)
**No qualifying LEAP builds — zero names clear 6-of-9 gates.**
- **POET — NEAR-MISS (5/9), REJECTED.** Fresh ask-side Jan-2027 40C (OI 3,483 → 34,365, $6.2M) + 10/10 OI build + cum-flow +$55M/90d + DP price-level defense $13.82 + ACCUMULATION — **but conviction-matrix confidence is only 12.2%** (hard-fail >70), and the 90d accretion is entirely concentrated in the last 30d = a fresh-thesis breakout spike, not smooth multi-quarter LEAP accumulation. A speculative microcap (IV rank 59, +34% 30d round-trip), not an institutional LEAP profile. → Hand to `accumulation-hunter`'s shorter-horizon read, not a LEAP sizing.
- **Theme names disqualified:** MU, MRVL, LITE, COHR, CIEN are all **MIXED on 90d cum-flow** (MU −$188M, LITE −$39M) — the semis/optical bullishness is short-horizon flow, not long-dated accumulation. GM 270617C100 and SNDK far-dated lines were **bid-side (call-writing / protective puts)**, not directional longs.

---

## 5. Volatility Surface
The whole semis/memory complex is in **steep event-driven BACKWARDATION** — front (3-DTE = 06-05) IV bid 1.2×–2.4× over 30-DTE on a synchronized NFP + AVGO/CIEN/DOCU/ULTA earnings cluster; every name at iv-percentile 100. This is **not** a clean calendar-harvest surface — front-end ratios are *elevated into* pending binaries (>1.10 disqualifier fires), so the tradeable vol-sell is the **back-week earnings kink and post-event crush**, not the front.

- **MU — the only true KINK:** the 06-18 earnings expiry IV (141%) sits *above* both the 06-12 (116%) and the front 06-05 (129%) → **calendar: short 06-18 / long 07-17** harvests the term normalization. (Note: MU is directionally VETO'd; this is a vega-neutral structure, not a short.)
- **AVGO — CALENDAR (sized half, §6):** front-end ratio **1.99** (panic, not naked-shortable) + complacent back skew → sell 06-05 (131% IV) / buy 06-18 (86%) to harvest the steep backwardation past the print. Bearish-flow confluence (−$14.5M).
- **MDT — SELL VOL (sized half):** cleanest low-base crush (front 75% / back 34%, ratio 2.19 on a low IV base) → 06-05 iron condor at ±1.0× implied move.
- **CIEN / DOCU / AI — SKIP:** extreme front panic (193–243% IV) + crowded/uncoverable tails; CIEN has bullish-flow conflict (+$9.5M).
- **SMH / SOXX / AMD / STM — calendars disqualified** (front bid is NFP-driven, not idiosyncratic). **Re-evaluate 06-06 post-NFP:** if front-end ratio collapses toward 1.0, the calendar re-opens cleanly under QQQ PREMIUM_SELLING VRP.
- **Index:** QQQ/SPY front-end IV flat (1.015) — no index vol dislocation; the 06-05 bump is NFP only.

---

## 6. Risk & Correlation
**Macro headline:** late-cycle, sticky-inflation (core CPI 2.99%, curve normal +0.41, unemp 4.3%), no recession signal — but an **event-dense fortnight (NFP 06-05 → CPI ~06-10 → FOMC 06-16/17)** into a market at highs with 37.4% bullish flow breadth. This is the binding constraint on the whole book.

**Correlation (`uw risk portfolio-correlation`, 30d):**
- **`memory_cycle_cluster` = {MU, SNDK}, pairwise corr 0.743 (≥0.70) → treat as ONE position.** SNDK takes the −1 cluster cut (lower-scored member; MU is VETO'd, so neither leg trades at size).
- AMD / INTC corr 0.655 = **soft-watch (0.60–0.70), no penalty.** MRVL / AVGO 0.54.
- **Correction to the "all-semis = one cluster" prior:** the pairwise data does NOT support it — only MU/SNDK clears 0.70. But **book-level sector concentration is real** (the candidate book is ~entirely semis/memory + satellites) → feeds the HALF-size guidance and the hedge sleeve.

**Fundamentals verdicts (top-5):**
- **MU — 🛑 VETO** (short): 4/4 beats, rev +85% / EPS +412%, shortage-to-2030, mean target +28% above price (stale). Zero fundamental support for a short. Earnings 06-24 = hard event either direction.
- **TSLA — ⚠ CAUTION (−1):** EPS −39% YoY, PE 404, contested robotics catalyst (Nvidia/OpenAI robotics arming Optimus rivals, TX SB 2807), Recom 2.50 HOLD, distribution_flag.
- **AMD / MRVL / SNDK — ✅ CONFIRM (0):** fundamentals back the longs (AMD EPS +123%; MRVL Huang catalyst; SNDK 4/4 huge beats) — but all three are **overbought/parabolic** (RSI 75 / 86 / 70, SNDK beta 5.01), and SNDK's *flow* is distribution.

**Event-risk gate:** NFP at **T+3 hits every directional swing** (−1 each). AVGO/MDT report **06-03** (the vol plays *are* the event; they close before NFP). MU earnings 06-24 inside horizon.

**Debate-disconfirmation cuts:** bear ≥ bull on **all four** crowded longs (TSLA 0.65/0.75, AMD 0.65/0.65, MRVL 0.65/0.75, SNDK 0.65/0.75) → −1 each. The classic additive-confluence trap: the highest-scored names are the most crowded and the debate cleared none of them.

**Adverse-flow exits (prior `conviction_2026-06-01` = ORCL, MSFT, AVGO, IBM, SNOW):** **ORCL** flow flipped BEARISH (net −1.7M) vs its long thesis → exit. **MSFT** strong adverse reversal (net −91M) → exit / stay out. AVGO reclassified (stale long → vol play). IBM/SNOW theses intact (still bullish flow). `fz` quote-drift shows no adverse-fundamentals signal — exits are flow-driven.

**Breadth cross-check (`fz`, advisory):** 257 advancers / 245 decliners, **51.1% green**, avg +0.18%; top HPE +19.5%, worst TTD −9.1%. No hard divergence (pct_green > 50) — **but the equity breadth (51% green) is far more constructive than the options-flow breadth (37.4% bullish)**, a flow-vs-price divergence consistent with mega-cap distribution. Advisory; does not change sizing.

**Hedge sleeve:** institutions are already hedging risk-off — **HYG bear-put-spread (Aug 80P/76P, repeat 2 days)** + **VIX Oct 50C ratio** on the structured tape. Since the gated book has near-zero net sized delta (two market-neutral vol plays), the hedge is **macro-event insurance**, not a delta offset:
1. **SPY put vertical** through NFP→CPI (~06-12/13, 2–3% OTM long / 5–6% OTM short, ~0.5–1.0% NAV).
2. **Optional VIX call ladder** (Jul/Aug 25C/35C) mirroring the institutional VIX flow.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no fresh `/calibration-audit` per-tier expectancy table is available this run; the live sizer remains the win-rate ladder (Step 5). Standing context from the 2026-05-30 audit: the **long book runs ≈ −22pp benchmark-excess (beta)** while the **short book runs ≈ +20pp (alpha)** — and today the one short worth having (MU) is fundamentally VETO'd, so **there is no clean alpha expression on the board.** Keep the book honest: a high hit-rate that is pure beta makes no money the index wouldn't.

| Ticker | Dir | raw | Components (source · tool) | Class | Win-rate (n, src) | Cum-flow 30d/90d | Pre-risk | Fund. | Bull/Bear | Gates applied | Final | Invalidation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **TSLA** | long | **9** MED† | +3 accum-conjunction (acc-hunter·block-stratified) · +3 cum-flow (quant·cum-prem-flow) · +2 signal-confluence (quant·signal-confluence) · +1 OI (acc-hunter·oi-trend) | dark_pool_accum | 0.6364 (66, proxy) | +$378M / +$998M | half | **CAUTION −1** | 0.65 / **0.75** | fundamentals −1, event_risk −1, debate −1 | **skip** | loses $423.74 DP shelf |
| **AMD** | long | **8** MED | +3 DEX (dealer-pos·dex) · +3 cum-flow (quant·cum-prem-flow) · +1 OI (sweep·oi-trend) · +1 sector-leader (sector-rot·sector-flow-persist) | bullish_flow | 0.7714 (35, backtest) → **beta** | +$476M / +$301M | starter | CONFIRM | 0.65 / 0.65 | event_risk −1, debate −1, market-excess → starter | **skip** | loses ~$500 / DEX < +13B |
| **MRVL** | long | **7** MED | +3 DEX (dealer-pos·dex) · +2 signal-confluence (quant·signal-confluence) · +1 OI (sweep·oi-trend) · +1 sector-leader (sector-rot·sector-flow-persist) | bullish_flow | 0.7714 (35, backtest) → **beta** | +$145M / +$138M | starter | CONFIRM | 0.65 / **0.75** | event_risk −1, debate −1, beta | **skip** | RSI 86, +22% past target |
| **MU** | **short** | **7** MED | +3 cum-flow short (quant·cum-prem-flow) · +3 distribution-conjunction (acc-hunter·block-stratified) · +1 OI put-side (sweep·oi-trend) | bearish_flow | 0.3333 (36, backtest) | −$61M / −$188M | starter | **🛑 VETO** | 0.55 / 0.55 | **fundamentals VETO**, cluster, event_risk (06-24) | **watch-only** | thesis dead — short unsupportable; revisit post-06-24 |

**† Tier-band note:** TSLA's raw 9 maps to HIGH under the command's P1.3 rubric (≥9 HIGH) but is recorded **MEDIUM** here — `scripts/validate_decision.py` still enforces the conservative pre-P1.3 band (≥10 HIGH), and P1.3's ≥9 cut is flagged in-sample-only pending the ~06-12 re-confirm. The conservative band governs the persisted envelope; it is moot for sizing today (TSLA gates to skip regardless). *Repo follow-up: sync the validator band to P1.3, or formally defer P1.3 until re-confirmed — the rubric and validator currently disagree.*

**Deep-dive hand-off:** none triggered — no name survives the gate stack to `skip`, so this is a no-edge execution day (per Step 8.5, the `/stock-deep-dive` hand-off is skipped). If the desk wants single-name depth on the highest *scored* name despite the gate: `Recommended deep dive: /stock-deep-dive TSLA`.

### Conviction scoring rubric (verbatim, for audit)
```
+3 dealer-positioning DEX flip / vanna-squeeze in trade direction
+3 3+ aligned accumulation signals (DP+OI+smart-positioning, block-stratified institutional-tier) — CONJUNCTION: full +3 only when cum_flow_30d confirms (sign aligned AND |cum_flow_30d| ≥ $50M); else halved +3→+1
+1 multi-day OI build (oi-trend BUILDING, --days ≥ 5)
+1 conviction-matrix DIRECTIONAL_LONG conf > 70 — CONDITIONAL: only when dominant_signal_class == leap_directional; else 0
+3 cumulative-premium-flow net directional accretion in trade direction (30d)
+2 signal-confluence ≥ 4 (second-agent confirmation)
+1 sector-rotation single-name leader — CONDITIONAL: persistence ≥ 0.6 AND cum_flow_30d aligned AND |cum_flow_30d| ≥ $50M; else 0
+1 earnings-scout BUY VOL or SELL VOL
+2 multileg-strategist directional structure (term-structure-anchored)
+1 vol-surface KINKED/BACKWARDATION with VRP-aligned bias
-2 contrarian overcrowded long with rising pc-ratio-zscore (VRP positive)
-3 flow_conflict — cum_flow_30d clearly OPPOSITE dominant_signal_class  [mutually exclusive with -1]
-1 flow_conflict_lite — 30d cum-flow MIXED / bottom-quartile  [mutually exclusive with -3]
(sweep-persistence +1 line REMOVED 2026-05-23; §2 GEX + §2a 0DTE setup contribute 0 points)
Tiers: ≥9 HIGH (full, subject to 3-of-5 LB-tool gate + win-rate gate) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 drop
Sizing ladder: win_rate ≥0.70 full / 0.50–0.70 half / <0.50 starter. Downgrade-only: market-excess ≤0 → cap half (≤−0.10 → starter); n<10 → cap 0.69; non-OI-confirmed flow → cap half.
```

---

## 8. Watch-only — single signal, no confluence
Listed for journaling, **not** for trade entry today.
- **AMAT** — accumulation-hunter's *cleanest* institutional buy (mega 0.826 buy, b/s 3.45, 5/5 OI, $490.05 DP defense) — **but flow doesn't confirm** (+$29.95M cum-flow, sub-$50M and below bottom-quartile → conjunction halved + flow_conflict_lite) AND only 1 agent flagged it → **fails the confluence gate.** The strongest single-agent signal on the board that the cross-checks killed.
- **BE** — mega all-buy DP (b/s 5.06, $302.85 defense) **but cum-flow −$142M OPPOSES the long** (full flow_conflict −3, raw −1) — distribution dressed as accumulation. Single agent → fails confluence gate.
- **LITE** — optical sector leader (+$31M premium) but 30d cum-flow −$23M (bearish), single agent → fails confluence gate.
- **POET** — LEAP near-miss (5/9; conviction-matrix 12.2%; fresh-thesis microcap) — see §4.
- **Energy/Utilities single-name leaders** (sector-rotation only, 1 agent): DVN, CVX, GEV, TLN, OKLO — rotation context, no confluence backing.

---
*Generated by `/daily-analysis` — 11-agent Phase 1 fleet (10 spawned; OPEX agent omitted, not OPEX week) → quant → fundamentals gate → bull/bear debate → risk gate. Data: `uw` CLI (Unusual Whales) + `fz` CLI (Finviz, advisory) + FRED macro. §2/§2a advisory (0 points). This is a defensively-tilted, event-dense, low-clean-edge day: the long book is beta into three macro events, the only short worth having is fundamentally VETO'd, and the only sized survivors are two earnings-vol plays that resolve before NFP.*
