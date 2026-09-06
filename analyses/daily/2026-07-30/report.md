# Daily Market Analysis — 2026-07-30

## Executive Summary

- **Regime + GEX state:** **TRANSITIONAL / CHOPPY.** SPY 741.69 (+1.68%) but still **below both** its 20SMA (745.58) and 50SMA (744.72); QQQ 683.55 (+3.30%); IWM 292.59 (+1.39%). VIX **17.09, −17.28%** — a violent post-FOMC vol crush. SPY holds **short gamma** (7 straight sessions, `total_gex` −366.9M); QQQ's regime **flipped today** and is fresh/unstable. Breadth is the story: equal-weight **RSP −0.16%**, only **39.2% of S&P names green**, **median stock −0.64%**. Sector lean: Technology +$2.47B one-day flow, ~2.5× its own 5-day ceiling — but concentrated in two earnings names plus a semis short-cover.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** **SPY** — short-gamma (FULLY_NEGATIVE), ZGL null/unreliable, call wall **744** (+0.29%), put wall **730** (−1.60%) → trend-amplifying with upside capped close-in and more room below. **QQQ** — regime flipped today (fresh, unstable), ZGL 729.40 **unreliable** (6.68% from spot), call wall **685** (+0.18%, the largest strike on the grid), put wall **660** (−3.48%) → tight overhead pin candidate, distant downside support. Advisory, see §2.
- **Top swing build:** **NONE.** Zero names survive the gate stack — the post-gate conviction book is empty. Verified against the envelope history: **every run from 2026-07-21 through 2026-07-29 also sized zero positions** (07-23 and 07-24 wrote back watch-only names but sized nothing). Phase 2 agents asserted "20th consecutive"; that exact count is **unverified** and conflicts with the stored note recording the prior streak ending 2026-07-24, so it is not repeated as fact here.
- **Top LEAP candidate:** **NONE.** Zero of 20 market-wide DTE>180 builds cleared the 6-of-9 gate; the instructive near-miss (PDD) is a **COVERED_CALL** at 17.5% confidence — dark-pool buying financed by call-selling, upside capped.
- **Biggest risk:** **`AI_memory_semis_cluster` = {MU, SNDK, AMD, NBIS, BE}** — pairwise **MU/SNDK 0.923**, SNDK/AMD 0.872, MU/AMD 0.828. One bet wearing five tickers. Hedge sleeve: SPY Aug-21 706/695 put debit spread (index IV at the 34th percentile with skew at 1.482 — the cheap side of the surface).

> **Two facts that reframe today.** (1) **AMZN and AAPL both report after tonight's close** — neither appears in `uw screener earnings-catalyst`'s 14-day window, and both were detected only from their 1DTE IV structure. Tomorrow's open carries a mega-cap AI-capex gap the EOD gamma map cannot see. (2) The tape's "rally" was **cap-weighted only**: SPY +1.68% / XLK +5.50% against RSP −0.16% and a −0.64% median stock, with **68% of single-leg whale prints (417/610) carrying the CLOSING signature.** This was short-covering, not accumulation.

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity"**, trend **CHOPPY**. SPY 741.69, below the 20SMA (745.58) and 50SMA (744.72), −0.68% on 30 days, −2.46% from its 90-day high. UW flow breadth **35.7% bullish** (2,241 bullish vs 4,036 bearish tickers). Verbatim guidance: *"Half position sizes. Favor defined-risk strategies. Iron condors in range."*

**The breadth divergence is the day's central fact.** Three independent lineages agree the tape was narrow:

| Measure | Reading |
|---|---|
| SPY / QQQ / XLK (cap-weighted) | **+1.68% / +3.30% / +5.50%** |
| RSP (equal-weight S&P) | **−0.16%** |
| `fz` breadth (Finviz, independent source) | 197 advancers / 304 decliners, **39.17% green**, median **−0.64%** |
| `uw` flow breadth | **35.7% bullish** |
| Single-leg whale prints | **68% CLOSING signature** (417 of 610) |

A +1.68% index day with a −0.64% median stock is a two-name-plus-semis squeeze. The 5-day column proves it: every squeezed name is still deeply negative on the week.

| Ticker | 1d | 5d | | Ticker | 1d | 5d |
|---|---|---|---|---|---|---|
| CORT | +27.29% | +22.41% | | MSFT | **+15.51%** | **+18.22%** |
| NBIS | +27.13% | −14.73% | | LITE | +15.09% | −16.84% |
| BE | +26.49% | −4.68% | | AMD | +13.00% | −10.06% |
| SNDK | +25.99% | **−20.52%** | | CIEN | +12.62% | −8.70% |
| SOXL | +24.71% | **−27.16%** | | META | **−7.95%** | −11.07% |
| MU | +18.36% | −11.67% | | ALNY | **−28.31%** | −23.54% |

**MSFT is the only name up on both horizons** — and that is the earnings gap, not a trend.

**Per-index gamma table (current-state EOD book):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 741.86 | `null` (unreliable) | −366,905,704 | FULLY_NEGATIVE (7 sessions) | 744 (+0.29%) | 730 (−1.60%) |
| QQQ | 683.77 | 729.40 (unreliable, 6.68% away) | +72,652,993 | NEGATIVE (**flipped today**) | 685 (+0.18%) | 660 (−3.48%) |
| IWM | 292.59 | — | — | alternates POSITIVE/FULLY_NEGATIVE nearly every session — **too choppy to classify** | — | — |

**`uw options-flow dte-volume-share`:** 0DTE 26.4% / weeklies 31.0% / monthlies 24.5% / LEAPs 3.5% → **BALANCED**. No institutional benefit-of-the-doubt, no retail downgrade. LEAP share of 3.5% explains the thin long-dated board.

**`uw historical vrp`:** SPY **FAIR +0.0126** (IV30 14.40% vs realised 13.14%); QQQ **FAIR −0.0057** (IV30 25.31% vs realised **25.88% — realised above implied**). The QQQ complex sits in **negative VRP**, which correctly aborted every contrarian fade in that complex and argues against selling QQQ-complex vol overnight.

**Macro backdrop** (`scripts/fred_macro.py`): yield curve **normal** (10Y−2Y +45bp); core CPI **2.81%** YoY, core PCE **3.29%** YoY (sticky, above target); unemployment 4.2%, payrolls **+57k** (soft); 10Y **4.67% and rising** (+29bp over 30 days); USD weakening; fed funds 3.63%. This is a **stagflation-lite** mix — the bond market repricing hawkish into a softening labour market. A rising long-end discount rate is a direct headwind to long-duration equity and was weighed against every LEAP thesis.

**Forward event risk (next ~10 trading days):**

| Event | Date | Impact |
|---|---|---|
| **AMZN + AAPL earnings** | **2026-07-30, tonight post-close** | **HIGH** — absent from `earnings-catalyst`; detected from 1DTE IV structure |
| XOM earnings (premarket) | 2026-07-31 | medium |
| ISM Manufacturing / PLTR earnings | 2026-08-03 | medium |
| AMD earnings (postmarket) | 2026-08-04 | medium |
| ISM Services / SNDK earnings | 2026-08-05 | medium |
| **Nonfarm Payrolls (July)** | **2026-08-07** | **HIGH** |
| **CPI (July)** | **2026-08-12** | **HIGH** |
| PPI (July) | 2026-08-13 | medium |

FOMC concluded 2026-07-29; the next meeting is ~mid-September, outside the window. **SPY, QQQ and IWM all kink their term structure at exactly 2026-08-07** — the index complex is hedging the NFP→CPI corridor.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book (open interest persists overnight) read forward as the *prior* for the next open. **Prose-only, 0 rubric points, no backtested predictive claim.** Predictive validation lives in `/weekly-analysis`'s rolling §2 backtest. Scope is SPY and QQQ only.

**SPY — short gamma, held 7 sessions, asymmetric walls.**
`total_gex` −366.9M (vs −2.78B yesterday — the magnitude collapsed ~87% on the VIX crush but the sign never changed). FULLY_NEGATIVE has now held **07-22 → 07-30**; this is **not** a fresh flip. ZGL is `null` → `zgl_reliable=false`, so the read falls back to the `total_gex` sign plus spot-vs-wall position, exactly as the reliability rule requires. Short gamma means dealers sell into declines and buy into rallies → **trend-amplifying, not mean-reverting.** The call wall at **744 sits only +0.29% above spot** while real support is absent until **730 (−1.60%)**, with a secondary pressure strike at 740 barely below. Upside is capped close-in; downside has room before dealer hedging turns supportive.
**Structure bias:** debit call spreads capped at 744–746, or a directional 0DTE put on a break of 740. If selling premium, skew it short-delta (put-heavy condor) rather than a centred iron fly — the wall distances are not symmetric.

**QQQ — regime flipped today; fresh and unstable.**
07-23 → 07-29 was FULLY_NEGATIVE for five straight sessions; **07-30 flipped to NEGATIVE with `total_gex` turning positive (+72.7M)** as the −17.3% VIX crush unwound dealer short-put decay from the MSFT/META earnings squeeze. **Do not treat this as a settled regime.** The call wall at **685 (+0.18%) is the single largest strike on the entire grid (+102.5M)** — a genuine pin candidate for the first 30–60 minutes if fresh 0DTE OI doesn't blow through it. Put-side support is distant at 660 (−3.48%). ZGL 729.40 sits 6.68% from spot, outside the ~5% trust band → `zgl_reliable=false`. Given the sign mismatch and the unreliable ZGL, read this as *short-gamma-legacy with a tight overhead wall*, not a clean flip to stabilising long gamma.
**Structure bias:** fade pokes just above 685 with defined risk (685/690 call spread) rather than a full iron fly. Keep any 0DTE straddle small — the VIX crush already priced out much of tomorrow's expected move and QQQ VRP is negative.

**Mandatory caveats:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and re-computes the ZGL and walls. QQQ's flip today shows how fast this book moves.
- **ZGL reliability:** SPY `null` → fallback used. QQQ 6.68% from spot → flagged unreliable, `total_gex` sign used only as a secondary cross-check.
- **GAP RISK IS ELEVATED TONIGHT — this corrects the agent's own read.** `gamma-flip-tracker` concluded "no Tier-1 macro event before tomorrow's open… low incremental gap risk." That is **wrong**: **AMZN and AAPL both report after today's close**, a combined ~$7T of market cap and a direct AI-capex read-across to the entire complex. The walls above can be gapped through before any hedging mechanic engages. Treat this prior as low-confidence for tomorrow's open specifically.
- **Tooling limit:** `uw options-structure gex --dte-max 1` errors — this is the standing **0–45 DTE** book, the best available proxy, not an isolated D+1 expiry.
- **ETF book**, not the cleaner SPX/NDX index book.
- **Live data-quality artifact:** on both names the categorical `regime` label contradicts the raw grid — SPY's "all strikes negative" description prints alongside *positive* per-strike GEX at 736–765 (744: +79.8M; 760: +71.5M), and QQQ's "NEGATIVE / dealers net short gamma" label sits on a *positive* `total_gex`. **Treat `total_gex` sign + the per-strike distribution as ground truth over the label.** All wall readings above use per-strike values.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py`)

The GEX walls above are a **map, not a pin** — wall-as-magnet backtested NO_GO, as did every directional 0DTE signal. What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, not a guaranteed edge.

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` / VIX | MID / 17.09 | MID / 17.09 |
| implied move | 1.02% | 1.86% |
| `expected_range_pct` | 1.20% | 1.36% |
| `size_scalar` | 1.0 | **0.5** |
| structure | wider iron condor, wings ≈ ±1.2% (short-gamma: wider/trendier) — or reduce/stand aside | iron fly / short straddle centred 686.34, wings ≈ ±1.36% |
| `caution` | — | **front-end backwardation** |
| backtest verdict | GO_PREMIUM_SELL_INTRADAY | GO_PREMIUM_SELL_INTRADAY |
| win rate (open entry) | 90.0% | 86.7% |
| mean P&L **gross** | +0.246% | +0.376% |
| mean P&L **NET** (after 0.10% assumed cost) | **+0.146%** | **+0.276%** |
| worst day | −1.40% | −2.453% |

**`pnl_basis`: percent-of-underlying-spot-notional, GROSS of costs — NOT premium-collected, NOT margin-relative.** Lead with the net figure: **+0.146% (SPY) / +0.276% (QQQ)** of spot notional per day. Vilkov (2024) found an unconditional 0DTE condor flips to negative net Sharpe once costs are charged; the gross win-rate overstates a negatively-skewed seller's edge.

**Entry rule:** enter at/after the open once the overnight gap resolves; if it gaps beyond the wings, **stand aside**. Hold to the close — **never carry overnight** (overnight entry backtested negative; QQQ's overnight mean is −0.113%). **SPY ≈ SPX** (validated identical). **QQQ is weaker** — the Nasdaq index book is unavailable — flag its lower confidence, and note its `size_scalar` is already halved with a backwardation caution.

**Tonight specifically: the standing-aside condition is live.** AMZN + AAPL report post-close, and QQQ VRP is negative. Do not sell QQQ-complex overnight vol into a double mega-cap print; the short-vol left tail is **unsampled** in this validation set.

**Promotion bar:** this lane stays advisory / 0 rubric points **permanently** until BOTH a vol-shock day enters the sample AND **net** expectancy clears a tail-aware bar. Win-rate is explicitly **not** the promotion metric.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

**Exactly one mechanized DEX flip qualified fleet-wide, and no vanna squeeze qualified anywhere.**

**The VIX gate killed every vanna-squeeze candidate.** Dated ^VIX (Yahoo chart API): 07-23 **18.70** → 07-24 18.58 → 07-27 18.67 → 07-28 18.21 → 07-29 **20.66 (FOMC spike)** → 07-30 **17.09**. That is **one** down session after a one-day spike — a post-event crush, not the ≥3-session decline the setup requires. SPY (+70,251), QQQ (+41,950), IWM (+61,790), META and LRCX all carry put-heavy books that look like the precondition; all are **"vanna pressure, not squeeze."**

| Symbol | DEX state + 5d trajectory | `dex_flip.py` | ZGL trajectory | front-end IV | Swing bias |
|---|---|---|---|---|---|
| **MU** | −4.06B → −5.41B → −9.12B → −16.58B → **+1.44B** | **QUALIFIES, long** — magnitude ratio **1.11×** (barely), `sign_changes=4`, **`whipsaw_warning=TRUE`** | raw ZGL values are a known artifact; label sequence POSITIVE→NEG→FULLY_NEG→POSITIVE is real | **1.362 BACKWARDATION — extreme panic, still building** | LONG, **LOW CONVICTION** |
| SPY | −38.4B → −34.5B → −26.1B → −75.2B → −1.8B (magnitude −97%, sign unchanged) | no flip | FULLY_NEGATIVE all 10 sessions | 0.945 CONTANGO | NEUTRAL |
| QQQ | −48.3B → −41.0B → −47.8B → −65.0B → −7.8B | no flip | one 7/22 flip reverted next session | 1.06 BACKWARDATION | NEUTRAL, watch 729 |
| IWM | −10.2B → −6.9B → −6.5B → −15.6B → −5.7B | no flip | alternates nearly every session — **choppy disqualifier** | 0.929 CONTANGO | NEUTRAL |
| NBIS | −587M → −745M → −1.61B → −2.60B → −160M | no flip; `whipsaw_warning=TRUE` | FULLY_NEGATIVE, no in-window flip | 1.049 FLAT | NEUTRAL — vanna FLAT/slightly short **contradicts** the bullish read |
| **MSFT** | +1.03B → +2.84B → +3.60B → +2.94B → **+20.5B** | **no flip — a LEVEL, `sign_changes=0` → 0 points** | 4 flips in 10 sessions, too choppy | 1.217 BACKWARDATION | **DISQUALIFIED** — DEX/vanna disagree |
| META | −321M → −159M → +327M → −361M → **−5.97B** | no flip | `total_gex` ground from +93M (7/17) to −51M | 1.059 BACKWARDATION | **DISQUALIFIED** — DEX/vanna disagree |
| LRCX | −452M → −550M → −873M → −1.13B → −32M | no flip; **7 sign changes / 16 sessions — worst whipsaw in the set** | 7 straight FULLY_NEGATIVE then defined NEGATIVE today | 1.151 BACKWARDATION | NEUTRAL |

**MSFT's vanna mechanic deserves emphasis** because it cuts against the day's most bullish-looking name: `net_vanna` **−50,766** is the largest call-heavy read in the fleet. Dealers are net short calls; **if IV keeps falling they must cut long-stock hedges — mechanical selling pressure.** VIX already fell 17.3%. The trigger condition is firing now, not hypothetically.

## 2b. Sector Rotation

**Rotation regime call: `no_change`, confidence LOW.**

No canonical pattern fits. Technology (growth) and Financials/Energy (value/cyclical) are inflowing simultaneously — ruling out growth→value and value→growth. Consumer Cyclical is outflowing while Financials and Energy, also cyclical, inflow — ruling out defensive→cyclical in either direction. This is catalyst-driven dispersion, not a regime shift.

**Turnover caveat applied throughout.** `sector-flow-persistence` `net_flow` is gross call$ − put$ — **turnover, not directional accumulation** — and `persistence_score` is a 0–1 sign-consistency scale, not a 0–5 count. Today reconfirms why: **Communication Services still reads trend "INFLOW" while today's actual print flipped to −$582M** after four positive days. Seven sectors tie at 1.0, so the absolute gate is non-binding and a magnitude filter (|net_flow| above the $110M cross-sector median) was required.

| Sector | Persistence | 5d trend | Today | Verdict |
|---|---|---|---|---|
| Technology | 1.0 | INFLOW 5/5 | **+$2.47B** | Rotating IN — **but see distortion note** |
| Financial Services | 1.0 | INFLOW 5/5, smoothly rising 145→150→167→188→264M | +$264M | Rotating IN — cleanest persistence shape of the day |
| Energy | 1.0 | INFLOW 5/5 | +$207M | Rotating IN |
| Consumer Cyclical | 1.0 | OUTFLOW 5/5 | −$483M | **Rotating OUT** |
| Communication Services | 0.8 | flipped today | −$582M | Watch-only — single-day reversal |
| Industrials | 0.8 | OUTFLOW, noisy | −$110M | Watch-only |
| Healthcare / Utilities / Cons. Defensive / Basic Materials / Real Estate | 0.6–1.0 | mixed | < median | Appendix |

**Technology's headline is a distortion.** +$2.47B is ~2.5× its own 5-day ceiling ($967M) and ~70× its floor ($34M). Testing the natural leaders against the full three-gate stack:

| Name | `cum_flow_30d` | Gate result |
|---|---|---|
| **MU** | **+$673.4M** | **PASSES all three** |
| **SNDK** | **+$993.0M** | **PASSES all three** |
| MSFT | −$34.0M MIXED | **FAILS** (a) direction and (c) magnitude |
| ORCL | −$263.5M | FAILS direction |
| AMD | −$163.7M | FAILS direction |
| NVDA | −$63.0M | FAILS direction |
| MDB | +$23.1M | FAILS magnitude |

So the genuine multi-week Technology accumulation is a **narrow memory/storage sub-theme (MU, SNDK)** — not broad tech, and explicitly **not MSFT**, which drove the entire headline number on an earnings pop. Financial Services and Energy are sector-confirmed but produced **no single-name leader clearing the $50M bar** (JPM +$41.4M missed by $8.6M; VLO +$14.9M).

**ETF flow tape (advisory — strengthens the conditional sector-leader +1, adds no points):**

| ETF | Net premium (5d) | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| IGV | +$25.2M | BULLISH | prints near/above mid | **$11.2M Nov 90P + $3.9M Aug 90P protective** | **agree** | software — bullish base, defensive urgency |
| EWY | +$20.1M | BULLISH | — | Jun-27 160C $36M, 245C $20M | n/a (Korea) | instrument-only |
| **SMH** | +$12.1M | **MIXED** | **blocks crossed BELOW mid (selling)** | put-heavy incl. **$26.8M Jan-28 500P** | **disagree** | **corroborates short-cover, not accumulation** |
| XOP | +$3.9M | BULLISH | — | — | agree | confirms GICS Energy |
| XLY | +$4.2M | BULLISH | — | — | **disagree** | TSLA-driven divergence |
| XLK | +$1.6M | MIXED (thin) | — | — | **disagree/weak** | confirms 2-name concentration |
| XLE | −$11.1M | BEARISH | — | — | **disagree** | XOP agrees, XLE doesn't — split |
| GDX | −$11.4M | BEARISH | mixed | thin | **disagree** | — |
| KRE | −$2.9M | BEARISH | — | — | **disagree** | money-centre up, regionals down |
| XLI | −$4.9M | BEARISH | — | — | agree | reinforces Industrials watch-short |

**The SMH read is the most important line in this table:** the semis ETF shows dark-pool blocks crossing *below* mid — genuine selling pressure — plus a $26.8M Jan-2028 500 put, while its constituents ripped 13–27%. That is distribution into strength, and it is why the memory/storage flow case did not survive.

**Swing-book implication:** the only names clearing the full persistence + 30d-flow + magnitude stack are MU and SNDK — and both were subsequently killed downstream (§6). Financials are sector-confirmed without a name. Consumer Cyclical shorts (RH, CVNA, LCID) are persistent but sit in §8.

---

## 3. Swing Setups (1–6 weeks)

### **EMPTY. Zero names survive the gate stack.**

This is a valid output, not a failure. Two names carried a live pre-risk size out of the quant; both were gated to `skip`.

**3a. Long swings (regime-aligned):** none.

**MU** was the only single name with a live size, and the arithmetic is not close:

| Step | Effect |
|---|---|
| Quant raw_score 4 → LOW → pre-risk **starter** | — |
| `panic` gate: front-end-iv-ratio **1.362** > 1.10, backwardation still **building** | −1 tier → **skip [floor]** |
| `fundamentals` gate: **CAUTION** (MSPR −33.33; 14-of-17-month insider selling persists unchanged since 2026-07-23; "Michael Burry Adds To His NVDA And MU Shorts" same day) | −1 tier |
| `debate` gate: bear **0.65** ≥ bull **0.35**, recommendation KILL_THE_LONG | −1 tier |
| C2 market excess: `bullish_flow` clean WR **0.4016** (n=127) vs same-window SPY-long **0.4646** = **−6.3pp** | beta, not edge |

Three independent −1 gates against a starter position. Even a full-size pre-risk would have died (full −3 = skip). **Final: SKIP / watch-only.**

The one mechanical trigger — the DEX sign-flip — cleared its magnitude floor by **1.11×** while flipping sign **four times** in the window, and `dealer-positioning-strategist` itself rated it LOW CONVICTION with `whipsaw_warning=TRUE`. MU's own bull conceded: *"+18.36% is not where I'd want to be initiating fresh size, full stop,"* and described its case against the negative class excess as *"a thin, narrative-based override, not a statistical one."*

> **The CXMT inversion — the sharpest thing on the board.** CXMT's Shanghai IPO debuted **+466%**, raising ~$8.6B, and is the dated cause of the memory complex's collapse (SNDK from >$2,350 in late June to $1,279.96 — down >45% in a month). **CXMT is a DRAM producer.** MU is DRAM-primary; **SNDK is NAND.** The market punished SNDK hardest, but the competitive read-through is **more direct to MU** — and the flow is long both. One outlet argues Wall Street conflated NAND with DRAM. Either way the narrative is unresolved and collides with SNDK's earnings in 6 days. This is an affirmative reason not to soften MU's CAUTION.

**3b. Short / fade swings (defined risk only):** none sized.

`contrarian-scanner` returned **zero qualifying fade candidates**. No index-level P/C extreme exists (SPY z 0.383, QQQ z 0.341, IWM z 0.746 — all NORMAL); the one single-name extreme (TRMB, z **2.995**, PCR 12.1) reads as **informed-flow short-continuation, not a fade** — crowd and smart money agree — and `vol-surface-scout` disqualified it as a thin-book artifact (`NO_NEAR_TENOR`: nearest tenor 22 DTE with 29 contracts, despite earnings in 6 days). The entire QQQ/semis complex where genuine price-vs-flow divergences exist was **aborted by the negative-QQQ-VRP rule**.

Three bearish structures are real but are **hedge inventory, not alpha** — the 2026-06-27 audit found index-ETF shorts **0-for-4** at HIGH tier and narrowed the ruling to *"no short alpha-sizing anywhere"*:

- **SPY Aug-21 P706/P695 debit spread** — BUY P706 at **89.2:1** ask-side ($7.02M), SELL P695 ($4.04M), ~$3.0M net debit, $11 wide. `repeat_count` 3, ticker present 5/5 days. Anchored to the post-hygiene **KINKED 2026-08-07 (NFP)** tenor, 8.8% prominence. OI-confirmed opening. Defined risk.
- **IWM Aug-21 put-spread collar** — **`repeat_count` 4, the strongest campaign in the entire book**, present 5/5 days. BUY P278 at **22.5:1**, SELL P275, SELL C298 at 0.034 (the collar cap), roll of P277. Kink at 8/7 = NFP. *"A bet against the median stock, not against the index headline"* — which is precisely what today's breadth says.
- **NVDA Aug-07 bear call spread** — SELL C200/C205, BUY C207.5/C210, plus SELL Aug-21 C200 ($27.02M) and BUY Sep-18 P180 ($13.82M). **This explicitly contradicts the bullish funnel**: NVDA's +$21.19M "bullish" net premium is inflated by 0/1DTE gross turnover, with Jul-31 C195/197.5/200 all bid-side heavy (ratios 0.87–0.90) = selling/closing. NVDA rose only +2.65% against SMH +6.88% and is −6.57% on 5 days.

**Sweep ledger (persistence-first; informational, 0 rubric points).** The persistence line was removed 2026-05-23 P0.3.

| Rank | Ticker | Side | Persistence | 5d premium | Opening vs closing | Read |
|---|---|---|---|---|---|---|
| 1 | AMD | bearish (tag) | 5/5 | $1.72B | OI-confirmed opening, but fresh OI is **call**-led | **CONTRADICTION** — the bearish tag describes the drawdown, not today's tape |
| 2 | INTC | bearish (tag) | 5/5 | $967M | opening; fresh OI **overwhelmingly call-side** | **CONTRADICTION** — same pattern |
| 3 | SPCX | bullish | 5/5 | $837M | concentrated in one contract | **ARTIFACT** — $330 strike vs $112.25 spot (~194% OTM) at 1–8 DTE, priced in nickels; spot flat despite $837M "bullish" premium |
| 4 | **NBIS** | bullish | 4/5 | $861M | **OI-confirmed opening**; $225P sold on the bid, $155C/$180C bought | **Genuine** — put-selling and call-buying *through* the drawdown, not today's chase |
| 5 | **BE** | bullish | 4/5 | $732M | **OI-confirmed opening**, clean ask-side call buying Sep–Jan | **Genuine** — 5d only −4.68% vs peers −15/−27%; today's +26.5% is the payoff of pre-existing positioning |
| 6 | SOXL | bullish (tag) | 3/5 | $314M | mixed | **CONTRADICTION (soft)** — put-dominated tape, net lean is put-*selling*; 3× leverage amplifies mechanically |

Every mega-cap and index name (SPY, QQQ, SPXW, SPX, TSLA, NVDA, META, AMZN, GOOGL, MSFT, AAPL, IWM) was **demoted by the hedge-flow gate** — all returned `cum_flow_30d` MIXED, none aligned with their claimed sweep direction. MU, SNDK and SMH carry 5/5 persistence and the largest premium books on the tape ($5.28B, $2.46B, $1.29B) but all three return `dominant_direction: MIXED` — **no directional thesis is extractable from the biggest flow signals in the fleet.**

---

## 4. LEAP Builds (6–24 months)

### **EMPTY. Zero candidates passed.**

`uw oi biggest-increases --min-dte 180` returned only **20 rows market-wide**, consistent with LEAPs being 3.5% of today's DTE volume. Full disqualification record:

| Ticker | Build | Failing gate | Detail |
|---|---|---|---|
| WOLF | 322d $50C | **Gate 4 (required)** | `cum_flow_90d` **−$129.8M BEARISH**; the 744× OI spike was **bid-dominated** (prev_ask 104 vs prev_bid 25,215) — premium sold into buyers, not bought |
| TLT | 351d/540d $89C | **Gate 4 (required)** | `cum_flow_90d` −$149.9M MIXED. Also macro-inconsistent: a long-dated TLT call bets on falling long yields against a 10Y **rising** +29bp/30d |
| **PDD** | 322d $130C | **Gate 8 — hard veto** | Clears 5/9 on paper (DP blocks at $87.44, price-level clustering, ACCUMULATION 2.03, 90d +$379.0M) but `conviction-matrix` returns **COVERED_CALL, confidence 17.5** — *"dark pool buying + call selling — yield enhancement, capping upside."* Corroborated by the bid-dominated call print. **Absolute veto regardless of gate count.** Its 30d flow is −$5.8M MIXED (thesis-extension, aging), and it sits in a 5/5-day OUTFLOW sector |
| INTC | 322d $75P | Gate 4 + wrong instrument | `cum_flow_90d` −$753M; build is a **PUT** — cannot clear DIRECTIONAL_LONG |
| VFC | 232d $14P | Gate 4 + wrong instrument | −$6.55M BEARISH; **PUT**, ask-dominated = buying protection |
| TECH, NOK | 232d calls | Gate 8 pattern-match | Both bid-dominated (calls sold, not bought) — same covered-call signature. NOK additionally flagged for the dividend-capture blind spot |
| COMP, SBET, JBLU, CDE, IWM, QQQ, IBIT, WULF | various | C12 / signal quality | Sub-floor prices ($6.08–$15.40); IWM/QQQ builds are index **puts** (portfolio hedges); IBIT/CDE had ask+bid < 20 contracts — direction uncharacterisable |

**Blind-spot checks run:** no merger-arb/tender signature (PDD's price levels disperse $86.00–$88.33, ruling out a locked tender price); dividend-capture flagged on NOK only.

**Coverage gap worth logging:** `multileg-strategist` independently found a genuine 540-DTE build in **DRAM** — a 2028-01-21 call-spread ladder, ~$11.6M debit against ~$55.8M max payoff, whose four legs total **127,163 contracts against a prior standing call OI of 89,949 at that expiry** (decisively opening), traded at IV 0.863–0.877, the cheapest vol on the entire surface. `leap-positioning-radar` never saw it because the `--min-dte 180` screen truncates at 20 market-wide rows. DRAM nonetheless scored 2 and dropped: `conviction-matrix` returns **MIXED at 8.7 confidence** and 30d/90d flows are −$47.9M/−$74.0M. Real structure, uncorroborated tape.

---

## 5. Volatility Surface

**Substrate hygiene is the headline.** `scripts/term_structure_hygiene.py` was run across 23 names by `vol-surface-scout` and 12 by `earnings-scout`. **The raw label flipped on 13 of 23** (SPY, QQQ, SMH, MU, NVDA, META, AAPL, MDB, ORCL, SHOP, PLTR, COHU, TRMB) — mostly raw BACKWARDATION → hygiene-adjusted KINKED once the 0DTE bucket was dropped. `base_shape` flipped to CONTANGO on SHOP and PLTR.

**`uw historical iv-percentile-zscore` returned `dates_used=76` on 0 of 23 tickers** — none cleared the 120-day bar. **Every percentile and z-score in this section is PROVISIONAL.**

**The structural read: index vol is cheap, single-name vol is genuinely rich.** SPY IV30d 14.4% sits at the **34th percentile (z −0.49)** while constituents that moved 8–27% today carry IV30d of 45–216% at the 55th–100th percentile. SPY's skew ratio (**1.482, TAIL_HEDGING**) is *higher* than QQQ's (1.285) despite far lower absolute vol — hedgers are buying cheap SPY tail protection while chasing the semis melt-up. That is a textbook **long-dispersion** setup (short index vol / own single-name vol). Critically, VIX crushed 17.3% yet single-name front-end ratios remain elevated (AMZN 1.72, DDOG 1.51, MU 1.36, CIEN 1.40, SOXX 1.18) — these are **real event-anchored dislocations that survived the systematic vol wash**, not crush debris.

**KINKED with catalyst alignment:**

| Ticker | Kink | Prominence | Robust pctile (raw) | Front ratio | Skew | Implied move | Read |
|---|---|---|---|---|---|---|---|
| **PLTR** | 8/7 (8d) | **18.7%** | 97.4 / z1.82 (79.1) | 1.34 | NORMAL 1.023 | **2.25%** | Earnings 8/3; **no listed weekly before 8/7**, so this expiry spans earnings **AND** NFP |
| **MU** | 8/7 (8d) | **25.6% — largest in the set** | **39.5** / z0.13 (77.7) | 1.084 | NORMAL 1.022 | ~20% | Raw rank says "elevated", robust says **median** — base vol is NOT stretched, so a 25.6% kink on a normal baseline is the cleanest true dislocation. But **no confirmed catalyst** → NFP/macro |
| SHOP | 8/7 (8d) | 5.9% — marginal | 98.7 / z1.73 (88.0) | 1.10 | NORMAL 1.099 | 2.36% | Barely clears the floor; back skew **unmeasurable** |
| SPY | 8/7 (8d) | 8.8% | 34.2 / z−0.49 (20.8) | 0.945 | **TAIL_HEDGING 1.482** | ~2.5% | NFP premium is modest; hedgers already own downside |
| QQQ | 8/7 (8d) | 5.4% | 68.4 / z0.55 | 1.06 | TAIL_HEDGING 1.285 | ~4.3% | NFP |
| SMH | 8/7 (8d) | 9.3% | 56.6 / z0.36 (79.5) | 1.09 | TAIL_HEDGING 1.135 | ~10.0% | Macro-shared across the complex |
| **META** | 8/7 (8d) | 11.8% | 64.5 / z−0.13 | 0.947 | **COMPLACENT 0.963** | ~8.5% | **Post-crash and nobody is hedging** — 25Δ calls bid over puts after an 8% drop. Don't buy this dip's vol |
| NVDA | 8/10 (11d) | 9.6% | 85.5 / z1.28 | **0.918** | NORMAL | ~8.75% | Sub-1.0 front ratio **undercuts** the KINKED label — weak |

**AMD — the algorithm missed a real dislocation.** The module reports plain BACKWARDATION, but that is an artifact of the prominence test: AMD's 4dte (8/3, 80.1% IV) expires *before* its 8/4 print, while 6dte (8/5, 110.3%) and 8dte (8/7, 106.1%) **both straddle the event** — a genuine two-tenor elevated plateau, not a single spike, which the local-max-vs-both-neighbours test under-detects (measured prominence 4.0%, just under the 5.0% floor). Robust pctile 76.3. Skew **COMPLACENT 1.015** — no directional put lean. Implied move **3.48%** is small against >100% front IV, meaning **the straddle is already efficiently priced — buying here is expensive vol, not cheap vol.**

**BACKWARDATION / calendar candidates** (all watch-only — a single snapshot cannot confirm the front ratio is *falling*):

- **MSFT** — the cleanest rationale in the batch. Front ratio **1.243**, elevated 6dte IV 43.5% vs back-month 33–35% one day after the print = **post-earnings vol-decay lag, not forward risk**. Skew TAIL_HEDGING 1.11. Implied 6-day range ~5.6%. Needs T+1 confirmation the ratio decays rather than re-inflates.
- **SNOW** — best "panic resolving" candidate: front ratio **0.917, already sub-1**.
- **DDOG** — front ratio **1.512, the most extreme in the set**, IV rank 95.5, but **no confirmed kink** and back skew unmeasurable → calendar (sell 8/7 / buy 8/28 at ~$268) rather than a naked short.
- CIEN (1.402, thin — 3 tenors dropped), SOXX (1.175), SOXL (1.156), LRCX (1.151).
- **SNDK (1.297) and APP (1.387) are disqualified from the calendar bucket** — event-pending, earnings 8/5.
- **ORCL and AAPL kinks are mechanical, not fundamental** — ORCL's 22dte kink is August OPEX; AAPL's 50dte kink is September quad-witch. AAPL's *overall* IV percentile (97.4) is genuinely extreme, which the earnings-tonight discovery now explains.

**Single-contract IV outliers: none genuine.** The entire cached top set is 0DTE/1DTE QQQ wing prints (strikes 660–693, nominal IV 250–4,200%, sub-$1M premium, sub-800 volume) plus EOSE/DNUT/SNAP micro-cap noise — exactly the 0DTE-wing artifact class.

**Disqualified — headline numbers are liquidity artifacts:**
- **COHU** — raw IV rank 99.7, robust z **2.845 (most extreme in the batch)**, but `NO_NEAR_TENOR`: only 2 tenors survive (22dte/334 contracts, 50dte/141). The chain has **no listed expiry inside 22 DTE at all**. The headline vol is computed off a monthly-only thin book.
- **TRMB** — raw IV rank 100, PCR 12.1, `NO_NEAR_TENOR` (nearest 22dte, 29 contracts) **despite confirmed earnings in 6 days**. Cross-tool discrepancy: `earnings-catalyst` reports an 8.6% implied move off a different strike grid, uncorroborated by any tradable listed tenor. The extreme PCR is very likely a thin-book artifact.

**`NO_NEAR_TENOR` is not `FLAT`.** Where no surviving tenor sits at or under 21 DTE the front end is **unmeasurable**; a 1.000 ratio there means "no data," never "calm." `min_contracts` (default 15) is a named tunable that has **not** cleared a pre-registered bar — reported, not treated as settled.

**Earnings vol verdicts** (`earnings-scout`, 12 names screened):

| Ticker | Earnings | DTE | Verdict | Implied move | Shape / base_shape | Front ratio |
|---|---|---|---|---|---|---|
| XOM | 7/31 pre | 1 | **SELL VOL (full)** | 1.94% | BACKWARDATION / BACKWARDATION | 1.232 |
| PLTR | 8/3 post | 4 | **SELL VOL (half)** | 2.25% | KINKED@8d / CONTANGO | 1.34 |
| AMD | 8/4 post | 5 | **BUY VOL** | 3.48% | BACKWARDATION (kink under-detected) | 1.255 |
| UBER | 8/5 pre | 6 | **SELL VOL (half)** | 1.56% | KINKED@8d / CONTANGO | 1.428 |
| NET | 8/6 post | 7 | **SELL VOL (half)** | 2.41% | KINKED@8d / CONTANGO | 1.416 |
| DDOG | 8/6 pre | 7 | **CALENDAR** | 3.32% | BACKWARDATION | 1.512 |
| ON / CAT / MCD / SHOP / SNDK / NBIS | 8/3–8/12 | 4–13 | **SKIP** | 0.98–7.83% | various | 1.049–1.94 |

Only **XOM** cleared the full-size bar — back-month skew **+0.056 TAIL_HEDGING** (skew ratio 1.199) confirms the front kink is event-local. **UBER's back skew is −0.1107 COMPLACENT** — actively complacent, the explicit "riskier short" case. **CAT is a flagged substrate trap:** its raw KINKED label points at `kink_expiry 2026-09-18` (50 DTE) — a September-OPEX cluster with 47.6% prominence that has **nothing to do with its 8/4 print**. Exactly the "kink label ≠ kink at the event" failure the hygiene module exists to catch.

**A broad artifact worth recording:** the `dte=1` (7/31) tenor is inflated across **every** name scanned, including tickers with no near-term catalyst (CAT 180% IV, SNDK/NBIS 234–235%). That is a post-VIX-crush thin-weekly artifact, not name-specific event pricing, and it is correctly excluded from kink detection (a boundary tenor has no two interior neighbours). Separately, today's −17.3% VIX crush likely compressed *back*-tenor IV more than front, which **mechanically inflates every front-end ratio above** — treat the higher readings (CAT 1.94, DDOG 1.51, SNDK 1.30) as partly a denominator effect.

---

## 6. Risk & Correlation

**Macro headline:** stagflation-lite — core PCE **3.29%** sticky above target, 10Y **4.67% and rising** (+29bp/30d), payrolls **+57k** soft, curve normal +45bp, USD weakening, fed funds 3.63%. The bond market is repricing hawkish into a softening labour market. **Forward calendar:** AMZN + AAPL **tonight**, XOM 7/31, ISM Mfg + PLTR 8/3, AMD 8/4, ISM Svcs + SNDK 8/5, **NFP 8/7 (HIGH)**, **CPI 8/12 (HIGH)**, PPI 8/13.

**Breadth cross-check (advisory, `fz`):** 197 advancers / 304 decliners, **39.17% green**, median −0.64%. **`divergence_flag: true`** — the index closed **green** with fewer than half the constituents participating. This is the distribution tell the single regime label hides, and it is independently corroborated by RSP −0.16%, `uw` flow breadth 35.7%, and the 68% closing signature. Advisory; does not change sizing.

**Correlation clusters (`uw risk portfolio-correlation`, 30d, today's 13 candidates):**

**`AI_memory_semis_cluster` = {MU, SNDK, AMD, NBIS, BE}** — one bet, five tickers.

| Pair | ρ | | Pair | ρ |
|---|---|---|---|---|
| **MU / SNDK** | **0.923** | | AMD / NBIS | 0.755 |
| SNDK / AMD | 0.872 | | NBIS / BE | 0.719 |
| MU / AMD | 0.828 | | SNDK / NBIS | 0.709 |
| AMD / BE | 0.770 | | | |

Kept member by raw score: **MU (4)**; all others take −1 tier (confirmatory — all already sat at DROP or the raw floor). **MU/SNDK at 0.923 is functionally the same ticker this week** — there was never a world where both passed. Soft watch, no penalty: MU/NBIS 0.695, MU/BE 0.684. Edge case recorded: SPY/AMD prints 0.707, over threshold, but SPY is a *bear* spread against a long cluster — opposite-sign P&L, i.e. a hedge of the cluster rather than a duplicate; the dedup penalty lands on AMD either way (SPY raw 3 > AMD raw 2).

**Fundamentals verdicts (top-5 single names):** the raw top-5 by score included SPY and IWM, which are index ETFs with no fundamentals substrate; the gate was run on the top five **single names** instead.

| Ticker | Verdict | Adj | Contradicting facts |
|---|---|---|---|
| **MU** | **CAUTION** | −1 | Insider MSPR 3mo **−33.33**; **14-of-17-month selling pattern persists unchanged since the 2026-07-23 CAUTION**; same-day "Michael Burry Adds To His NVDA And MU Shorts". Offsetting: 4/4 beats, revenue **+166.98%** YoY, GM 72.6%, D/E 0.27, earnings 9/21 (53 days, outside window) |
| **SNDK** | **CAUTION** | −1 | MSPR **−100.0**; **15 of 17 months near-total-sell** — the most extreme in the batch. Earnings **8/5 (6 days, un-de-risked)** on a **beta-4.26** name. Catalyst stack contradictory: CXMT competition vs "mammoth run" pieces |
| **NVDA** | **CAUTION** | −1 | Fundamentals **fight the short**: 4/4 beats, revenue +70.68% YoY, GM 74.15%, D/E 0.05. Beat *magnitude* decelerating (4.34→3.62→1.99→2.13%) is the only genuinely bearish signal, and it is soft. Earnings 8/26 |
| **MSFT** | **CONFIRM** | 0 | 4/4 beats (+9.53%), revenue +17.79% YoY, EPS +31.56% YoY, op margin 46.73%, D/E 0.24, earnings 10/27 (89 days). Catalyst real and dated |
| **AMD** | **CONFIRM** | 0 | 3/4 beats, revenue +34.97% YoY, EPS +123.4% YoY, D/E 0.05. Today's +13% is partly AMD-specific (Susquehanna PT raise, 2.5GW AI infrastructure agreement), not pure beta. Earnings **8/4 (5 days)** |

**No VETOs.** None hit the mechanical ≥2-of-3 contradiction; MU's and SNDK's insider contradiction is real but isolated (1-of-3).

**Event-risk flags:** AMD 8/4 (T+3) and SNDK 8/5 (T+4) sit inside any swing window. XOM 8/31 is T+1. NFP 8/7 = T+6, CPI 8/12 = T+9 — both inside a 2–4 week horizon. AMZN/AAPL tonight is an ambient read-across across the whole AI complex.

**Debate-disconfirmation cuts — all three fired:**

| Ticker | Bull | Bear | Gate | Bear recommendation |
|---|---|---|---|---|
| MU | 0.35 | **0.65** | **−1 tier** | KILL_THE_LONG |
| MSFT | 0.45 | **0.65** | **−1 tier** | KILL_THE_LONG |
| SNDK | 0.25 | **0.75** | **−1 tier** | KILL_THE_LONG |

Notably, **no bear recommended an outright short** — each independently concluded that the same beta and event risk that kills the long also makes a naked short dangerous. The bull concessions are the most useful output: MSFT's bull **withdrew the accumulation claim outright** (*"a stale 90-day aggregate that predates this catalyst doesn't retroactively become multi-week accumulation… It's a continuation bet on a confirmed catalyst"*), and SNDK's bull conceded the flow is *"more likely late than early"* on CXMT. Debates were **not run** on NVDA, AMD and PLTR — all three sit at `skip`, and a gate that can only cut size cannot change them; their `debate` verdict is `not_run`, not `pass`.

**Adverse-flow exit list: none.** `conviction_2026-07-29` is **empty** — yesterday was also an empty board, so there are no carried positions to exit. The `fz` quote-drift tripwire skipped cleanly on cold start.

**Hedge sleeve.** The post-gate book is empty, so net delta is 0 and no mandatory hedge trigger fires. For residual portfolio exposure carried into tonight and the NFP→CPI corridor:

1. **SPY Aug-21 706/695 put debit spread** — SPY IV30d at the 34th percentile while its skew (1.482) shows tail-hedgers paying up: the cheap side of the surface, defined risk, kinked to NFP, and it hedges the exact narrow-breadth failure mode this tape displays.
2. **QQQ Aug-14 put spread** spanning tonight's prints through NFP into CPI-eve — QQQ VRP is *negative* (realised 25.88% > implied 25.31%), so owning QQQ downside is not overpaying by construction.
3. **Do NOT sell QQQ-complex overnight vol into tonight's double print.** Negative VRP plus front-end backwardation means the short-vol left tail is live and **unsampled** in the 0DTE validation set. The §2a structures are intraday-only and expire before the prints.
4. **VIX call ladder — declined.** VIX just crushed 17.3% post-FOMC and the ^VIX resolution path is unverifiable per the standing data note; the SPY spread expresses the same convexity verifiably.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

### **EMPTY — zero names reached raw_score ≥ 7.** Highest on the board was MU at 4.

The Step 3a HIGH-tier load-bearing-tool gate never engaged (it requires raw ≥ 9). Step 6.5's batched strategy synthesis was skipped — `uw playbook batch-scan` takes the raw ≥ 7 list, which is empty. Step 8.5's deep-dive hand-off is skipped per its own rule (no HIGH-tier names).

**Expectancy lens `[advisory — expectancy is not yet a live sizing axis]`** — realised per-tier figures from the most recent `/calibration-audit` (2026-07-25, `phase_3_calibration`):

| Tier | n | Realised WR | Mean P&L | Payoff ratio |
|---|---|---|---|---|
| HIGH | 7 | **0.143** | −2.441 | 0.720 |
| MEDIUM | 19 | 0.526 | +0.104 | 0.948 |
| LOW | 87 | 0.402 | −0.874 | **1.170** |
| DROP | 327 | **0.431** | −2.190 | 0.871 |

`HIGH > MEDIUM > LOW` **fails for the fourth consecutive audit**, and **DROP (0.431) beats LOW (0.402)** — the names the system refused have outperformed the names it graded tradeable. Post-freeze the gap widens: DROP 0.419 (n=267) vs LOW 0.308 (n=26). The frozen rubric has produced **zero** HIGH calls. Tier × expectancy is now technically monotone (HIGH −1.97 ≥ MED −2.24 ≥ LOW −2.40) but monotone in the sense that all three are **negative, ordered least-bad to worst** — the half-Kelly sizer stays **off**, the win-rate ladder stays live.

Read against that table, today's empty board is the system working as designed, not failing.

### Full scored board (for the audit record)

| # | Ticker | Raw | Tier | Class | win_rate (src, n) | excess | Pre-risk | Fund. | Debate | Final |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MU | 4 | LOW | bullish_flow | 0.4016 (backtest_clean, 127) | **−6.3pp** | starter | CAUTION | 0.35/0.65 | **skip** |
| 2 | SPY | 3 | LOW | multileg_directional (bear) | null NA(substrate) | — | starter | NA | not_run | **watch (hedge)** |
| 3 | SNDK | 3 | DROP | sector_rotation | null NA(substrate) | — | skip | CAUTION | 0.25/0.75 | skip |
| 4 | IWM | 3 | DROP | multileg_directional (bear) | null | — | skip | NA | not_run | watch (hedge) |
| 5 | NVDA | 3 | DROP | multileg_directional (bear) | null | — | skip | CAUTION | not_run | skip |
| 6 | MSFT | 2 | DROP (raw floor) | multileg_directional (bull) | null | — | skip | CONFIRM | 0.45/0.65 | skip |
| 7 | AMD | 2 | DROP (raw floor) | earnings_vol | null | — | skip | CONFIRM | not_run | skip |
| 8 | PLTR | 2 | DROP (raw floor) | earnings_vol | null | — | skip | NA | not_run | skip |
| 9 | NBIS | 2 | DROP | bullish_flow | 0.4016 (class-level) | −6.3pp | skip | NA | not_run | skip |
| 10 | XOM | 2 | DROP | earnings_vol | null | — | skip | NA | not_run | skip |
| 11 | DRAM | 2 | DROP | leap_directional | null | — | skip | NA | not_run | watch |
| 12 | AVGO | 1 | DROP | dark_pool_accumulation | null (class empty) | — | skip | NA | not_run | skip |
| 13 | MA | 1 | DROP | dark_pool_accumulation | null (class empty) | — | skip | NA | not_run | skip |
| 14 | BE | 0 | DROP | multi_day_sweep | null | — | skip | NA | not_run | skip |

**Notable scoring decisions:**

- **MSFT (raw 2)** is today's cleanest test of the C13 router and the Σ-invariant. The fleet's single highest-conviction structure — a **$228M diagonal call roll** (SELL Aug-21 C390 $122.07M / BUY Nov-20 C420 $105.98M, identical size 19,500 and identical timestamp `14:47:25Z`, **$16.09M net credit**) — earned exactly its +2 line. `vol-surface-scout`'s calendar read expresses the *same* sell-rich-front/buy-cheap-back trade, so C13 assigned the points to multileg rather than double-counting. The MIXED 30d flow (−$34.0M) then took the −1 lite deduction. Direction is **inferred**, not observed (`no_side` on both legs). And the bear's decisive point stands: the structure **cuts delta 0.939 → 0.707 (−25%) and books $16M of credit** — a desk de-risking after a win, not pressing.
- **PLTR's vol-lane conflict was resolved, not split.** `earnings-scout` (SELL VOL) and `vol-surface-scout` (BUY VOL) agree on every substrate fact — same 8/7 kink, same 18.7% prominence, same 2.25% implied move — and disagree only on sign. That is **one observation with two interpretations, never two confirmations**. C13 assigned ownership to earnings-scout, which additionally carried the back-month discipline (45dte skew 0.0134 flat → front-only kink → half size). The compounding matters: PLTR has **no listed weekly before 8/7**, so that expiry spans both its earnings *and* NFP — short two events in one tenor.
- **AMD's −$163.7M 30d flow did NOT trigger flow_conflict.** Its `dominant_signal_class` is `earnings_vol` — a long straddle whose P&L is |move|, not sign — so the non-directional branch governs. Recorded, not deducted.
- **AVGO and MA** both fired the C11 conjunction halving (+3 → +1) *and* the lite deduction. That is intended, not double-counting: one governs the positive award's magnitude, the other is the direction penalty. AVGO additionally carries `distribution_flag: present=true` (call-side OI closing).

### Rubric (Step 4) — embedded verbatim for audit

```
Daily conviction score = Σ:
  +1  MECHANIZED DEX flip or vanna-squeeze in trade direction — verified SIGN CHANGE only, never a level;
      computed by scripts/dex_flip.py (sign(net_dex) latest session opposite ≥3 consecutive prior sessions,
      |net_dex| on flip day ≥ 0.25× trailing-10-session median |net_dex|). Vanna disjunct requires a dated VIX source.
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified institutional-tier
      confirmed) — CONJUNCTION (C11): full +3 ONLY when cum_premium_flow_30d confirms (sign aligned AND
      |cum_flow_30d| ≥ $50M); else halved (floored) +3 → +1.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix DIRECTIONAL_LONG conf > 70 — CONDITIONAL: award ONLY when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +1  cum_premium_flow net directional accretion (30d) — INTENT-SCREENED: award only when (a) no C28
      distribution_flag AND (b) on dividend payers in an ex-div window the accreting prints are NOT deep-ITM
      sub-parity calls. Screen failed or unevaluated on a flagged name → 0.
  +1  sector-rotation-strategist names ticker single-name leader — CONDITIONAL, ALL THREE required:
      (a) persistence_score ≥ 0.6, (b) cum_flow_30d direction aligned with thesis, (c) |cum_flow_30d| ≥ $50M.
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored play type)
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist top-5 (OPEX week only)                    [N/A — not OPEX week]
  -2  contrarian-scanner overcrowded long with RISING pc-ratio-zscore (VRP positive)
  -3  flow_conflict — cum_premium_flow 30d direction CLEARLY opposite dominant_signal_class
      (signed-sum sign flip + magnitude > today's union-median |cum_flow_30d|, or explicit OPPOSITE label)
  -1  flow_conflict_lite — 30d cum_flow read MIXED (signed sum near zero, or aligned but bottom-quartile magnitude)
      [flow_conflict and flow_conflict_lite are MUTUALLY EXCLUSIVE — apply ONE, never both]
  # TIER GATES applied by risk-monitor in Step 2d — contribute 0 to raw_score, never in score_components:
  -1  [TIER GATE] correlation cluster (pairwise corr ≥ 0.70)
  -3  [TIER GATE] uw risk market-regime conflicts with trade direction — −1 TIER
```

Tiers: **≥9 HIGH** (full) / **7–8 MEDIUM** (half) / **3–6 LOW** (starter/watch) / **≤2 drop**.
Rubric version **`2026-06-12`**, FROZEN. **P0.6 out-of-regime guard ACTIVE** — fitted UPTREND, current TRANSITIONAL → all sizing capped at half (non-binding today; nothing reached half).

---

## 8. Watch-only — single signal, no confluence

Failed the ≥2-agent confluence gate. Listed for journaling, **not for trade entry**.

| Ticker | Sole flagging agent | Note |
|---|---|---|
| **SNDK** | sector-rotation | Best flow on the board — 30d **+$993.0M**, 90d **+$2.58B**, all three leader gates. Killed by: gate fail, MSPR −100, earnings 8/5, CXMT, ρ 0.923 vs MU |
| **NBIS** | sweep-tracker | 4/5 bullish persistence, **OI-confirmed opening**, put-selling + call-buying *through* the drawdown. "Best risk/reward on this list" — but one agent only |
| **BE** | sweep-tracker | 4/5 persistence, clean ask-side call buying Sep–Jan, +369K net OI. 5d only −4.68% vs peers −15/−27% |
| **DRAM** | multileg | 2028 LEAP ladder, decisively opening (127,163 contracts vs 89,949 standing OI), cheapest vol on the surface. **leap-radar coverage gap** |
| **IWM** | multileg | Strongest campaign in the book (`repeat_count` 4, 5/5 days). Hedge inventory |
| **AVGO** | accumulation-hunter | 3 signals, institutional-tier confirmed, mid-session print (**not** closing-cross). Conjunction fails (+$21.8M MIXED). **`distribution_flag: true`**. DP support **$387.84 / $387.61 / $370.32** |
| **MA** | accumulation-hunter | Strongest block ratio in the scan (0.812), `distribution_flag: false`, clean tape. Conjunction fails ($14.0M < $50M); 90d **−$55.6M** disagrees with the 30d. Already +17.1% 30d — not "quiet". DP support **$577.35 / $563.32** |
| **NVDA** | multileg | Bear call spread explicitly contradicting the bullish funnel |
| **XOM** | earnings-scout | SELL VOL **full size** — only name with confirming back-month TAIL_HEDGING skew (+0.056). Earnings 7/31 |
| **UBER / NET / DDOG** | earnings-scout | SELL VOL half / SELL VOL half / CALENDAR. UBER's back skew −0.1107 COMPLACENT; NET's and DDOG's unmeasurable |
| **AMZN / AAPL** | vol-surface | Robust pctile **100 (z 2.279)** and **97.4** — the two most extreme in the batch. **Both report tonight → not actionable in a post-market report; the event is resolving now** |
| **SNOW** | vol-surface | Best "panic resolving" candidate (front ratio 0.917). But accumulation-hunter **rejected** it — mega-tier 100% sell; the $20.1M alert print **is** a sell |
| **SHOP** | vol-surface | BUY VOL low conviction (prominence 5.9%). accumulation-hunter returns explicit **DISTRIBUTION** |
| **SKHY** | multileg | Diagonal put roll, protection reset lower+longer. **NOT defined-risk** — the Aug07 P100 leg sits ~1:2 vs P125; downside re-opens below ~$75 |
| **IGV** | multileg | Put calendar **demoted to hedge** — Jan-27 P/C 6.423, puts = 25.24% of total OI = standing systematic software-hedge book. Still notable: software downside extended in duration while XLK ripped +5.50% and IGV managed +1.02% |
| **RH / CVNA / LCID** | sector-rotation | Consumer Cyclical persistent 5/5 OUTFLOW. RH bearish:bullish ~10:1 |
| **CORT** | funnel only | Dual-lane (uw confluence 5 + `fz` new-high), +27.29% 1d / +22.41% 5d — **no Phase 1 agent flagged it** |
| **TRMB** | contrarian | z **2.995** BEARISH_EXTREME but "not a fade — crowd and smart money agree". vol-surface disqualified it as a thin-book artifact |
| **SOXX / SOXL / SMH** | vol-surface / sweep | SMH DP blocks below mid = selling pressure |

### Explicit drops (rejected by ≥1 agent, zero positive flags)

- **META** — rejected independently by **five** agents. accumulation-hunter (cum_flow −$21.8M MIXED, NEUTRAL detector, "bullish premium on a −7.95% miss day = put-selling/hedge-unwind"); dealer-positioning (DISQUALIFIED — DEX −$5.97B today against a put-heavy vanna book); vol-surface (**skew COMPLACENT 0.963 after an 8% single-day drop — nobody is hedging**; "don't buy this dip's vol"); multileg (**deep-ITM put parity artifact CONFIRMED: 2028-01-21 P1020 at $485.00 vs intrinsic $486.80 — trading *below* parity**, which mechanically explains META's anomalous bullish net premium); sweep-tracker (Aug-21 post-miss hedges).
- **LRCX** — accumulation-hunter reject: mega-tier buy_ratio **0.0** (4 trades, 100% SELL, $162M), −20.43% 30d. **The $100.7M watchlist "alert" print is a SELL.**
- **INTC** — sweep contradiction flag; leap-radar disqualified (`cum_flow_90d` −$753M).
- **SPCX** — artifact: $330 strike vs $112.25 spot at 1–8 DTE, priced in nickels.
- **CSCO** — closing-cross artifact: 76% of daily DP volume in one 20:05:06Z print; `cum_flow_30d` −$0.76M contradicts the single-day ACCUMULATION read.
- **COHU** — `NO_NEAR_TENOR`; no listed expiry inside 22 DTE.
- **WOLF / TLT / PDD / VFC** — leap-radar disqualified (see §4).

---

## Appendix — substrate defects found today

Logged for `/calibration-audit`. Several are decision-relevant, not cosmetic.

1. **`uw historical oi-trend` BUILDING has zero discrimination.** Fired **6-of-6** (accumulation-hunter), **5-of-5** (leap-radar, 9–10 consecutive build days each), and **11-of-11** (quant). Reproduces the 2026-07-24 16-of-16 finding. The +1 line was awarded mechanically per the frozen rubric and flagged non-discriminating on every row — **it is not evidence.**
2. **`uw historical pc-ratio-zscore` has no `--date` flag.** Current-day only, no historical path. **Every z-score this run is a LEVEL, not a trajectory** — so the −2 "overcrowded long with *rising* z" rubric line was **unscoreable for every ticker today**. Recorded as not-applied; a level was not substituted for a trajectory.
3. **`uw screener earnings-catalyst` coverage gap.** **AMZN and AAPL both report after today's close** yet neither appears in its 14-day window, and `earnings_date` is `null` on every row it *does* return. Two ~$7T-combined names were detected only from their 1DTE IV structure by two agents independently.
4. **The SPX/SPXW "signal" is a box/jelly-roll.** $1.20B = **55% of all multileg premium today**: four legs, identical size 5,000, identical timestamp 18:40:45Z, deep-ITM, **positive theta (+0.12)** on the Sep P8000. Zero directional content. Anyone ranking multileg by raw premium gets this as their #1.
5. **`uw hot-chains multileg` default `--top-n 20` is unusable** — the entire top 20 is VIX/SPXW/IWM/SPY/index. **Every single-name structure found today (MSFT, DRAM, SKHY, IGV, NVDA) sits below rank 20.**
6. **`uw options-flow unusual-volume` is degenerate** — the entire top-20 is MSFT strikes with **OI = 1 or 2**, producing vol/OI of 1,711–3,893.
7. **`multileg_ratio > 1.0`** — mathematically impossible (multileg volume exceeding total volume): NN Sep18 C30 **2.892**, C18 1.975; SKHY Dec18 C210 1.997; TLT Aug21 P82 1.600. None scored.
8. **`uw historical iv-percentile-zscore` returned `dates_used=76` on 0 of 23 tickers** — none cleared the 120-day first-class bar. All percentiles/z-scores provisional.
9. **GEX regime-label vs `total_gex`-sign mismatch on BOTH indices.** SPY's "all strikes negative" description prints against positive per-strike GEX at 736–765; QQQ's "NEGATIVE / net short gamma" label sits on a positive `total_gex`. A live classifier artifact — trust the sign and the per-strike grid, not the label.
10. **`fz screen` returns tickers with a DUPLICATED LEADING CHARACTER** — `CCORT`=CORT, `GGKOS`=GKOS, `PPBF`=PBF, `AABEO`=ABEO, `IING`=ING, `BBBVA`=BBVA. Verified against the company-name field. `fz_enrich.py` called with an explicit ticker is unaffected.
11. **`fz_enrich` C17 quote-grid regression hits mega/large-caps uniformly** — `available:true` but the entire `derived` block null on all five gated names (`upstream_gaps: [earnings, recom, short_interest, target_price]`). The squeeze/analyst axis was NA across the board; small/mid-caps appear to hit the screener-fallback recovery path that these did not. **C16 and C18 remain untestable.**
12. **`uw options-flow single-leg` per-row `tier_label` serializes as `null`** even though `tier_label_counts` is populated (CLOSING_ANTISIGNAL 417, CALL_UNVALIDATED 75, PUT_CONTEXT 38, OPENING_PUT_STRONG 37, OPENING_PUT_PRIME 33, FLOOR_PUT_BLOCK 10). Labels could not be read per row.
13. **Month-end closing-cross contamination is broad.** SPY mega-tier DP buy_ratio **0.036**, QQQ **0.019** — both ~100% SELL in mega tier, driven by 4–5 prints all timestamped 20:00–20:25Z. Stale-NBBO crosses confirmed on **AAPL** (21:45:14Z, price $333.43 vs NBBO ask $309.73) and **AMZN** (21:07:00Z, $235.50 vs ask $252.80).
14. **`dte=1` tenor inflation is universal today** — 180–235% IV on names with no near-term catalyst (CAT, SNDK, NBIS). A post-VIX-crush thin-weekly artifact. Correctly excluded from kink detection; noted because it inflates every front-end ratio read off today's snapshot.
15. **Deep-ITM put parity artifacts persist** (the LULU-260218-P300 class from 2026-07-24): META 2028-01-21 P1020 at $485.00 vs intrinsic **$486.80 — below parity**; Aug-21 P800 at $268.82 vs $267.63; single-leg TSLA 400P and META 765P at 1DTE against spots of $308.85 and $539.03; CRWV size/OI = 999 on a near-zero denominator.

---

## Advisory — single-leg whale scan (0 rubric points, permanently)

`uw options-flow single-leg --regime neutral`. **C19 was CLOSED as REFUTED on 2026-07-25** — this is routing context only and accrues toward nothing.

**The headline is the composition, not any single print: 417 of 610 raw prints (68%) carry the `CLOSING_ANTISIGNAL` signature (size/OI < 0.5).** On a +3.30% QQQ melt-up, the dominant single-leg footprint is **position closing, not fresh opening conviction** — the single strongest corroboration of the short-cover read.

Tier-1 CONTRARIAN_SHORT puts: **GOOGL 300P, 29 DTE, size/OI 3.175** is the only clean one (spot 333.66, genuinely OTM, DTE ≤ 30). **TSLA 400P (1DTE, spot 308.85), META 765P (1DTE, spot 539.03) and CRWV 128P (size/OI 999) are all artifact-suspect** — deep ITM at 1 DTE, or a near-zero OI denominator. Per the regime rule, calls read **`CALL_UNVALIDATED`** in this non-bull tape, not a fade — "calls are beta" was measured in a bull window and is bull-regime-conditional, not structural.

---

*Generated by `/daily-analysis`. Phase 1: 10 alpha-finding agents in parallel (opex-pin-strategist not spawned — July third Friday was 2026-07-17, August is 2026-08-21, neither within 5 days). Phase 2: signal-confluence-quant → fundamentals-gate → bull/bear debate → risk-monitor. Rubric version `2026-06-12` (frozen). Envelope: `decision.json`.*
