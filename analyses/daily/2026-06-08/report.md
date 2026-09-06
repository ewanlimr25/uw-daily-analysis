# Daily Market Analysis — 2026-06-08

## Executive Summary
- **Regime + GEX state:** **TRANSITIONAL / PULLBACK_IN_UPTREND** — SPY 739.22 (below 20-SMA 746.37, above 50-SMA 715.39, −2.79% from 90d high), bullish_pct 34%, breadth red (181 adv / 321 dec, 36% green), VIX 18.92. **Index gamma is FULLY_NEGATIVE (short-gamma) across SPY/QQQ/IWM since the 06-05 selloff** — dealers amplify moves both ways. Sector lean: Tech (semis) owns net premium but the broad-index ETF wrappers (XLK/IGV/XLY) are being sold. VRP FAIR (+0.035).
- **Next-session GEX (SPY/QQQ):** **SPY** — short-gamma, ZGL null (unreliable), total_gex −1.32B, call wall **755** (+2.1%) / put wall **735** (−0.6%); a break of 738 accelerates toward 735→730. **QQQ** — weak short-gamma, total_gex −209M, call wall **735** / put wall **700**, soft +GEX floor 712–715. *Advisory, see §2.*
- **Top swing build:** **None at conviction.** Highest quant score is MU at raw 6 (LOW tier) — there are **no HIGH/MEDIUM names today.** Every sizable long (MU, MRVL, LRCX) failed the bull/bear disconfirmation (bear ≥ bull) and was cut by the CPI-at-T+2 event gate.
- **Top LEAP candidate:** **None.** `leap-positioning-radar` returned a clean null — zero names pass the 6-of-9 gate; the long-dated tape is index/rate hedging, not single-name conviction.
- **Biggest risk:** **AI-semis correlation cluster** {MU, LRCX, AMD, SNDK} (pairwise corr 0.71–0.80) collapses four longs into one bet — into a FULLY_NEGATIVE-gamma pullback with **CPI at T+2 (Jun 10)** and **FOMC at T+9 (Jun 16-17)**. Hedge sleeve: SMH Jun-19 put spread.
- **Book verdict:** **NEAR-FLAT / no new directional risk.** A "no edge" day. The only regime-coherent expression is delta-neutral premium-selling (§2a) and a defensive semis hedge. Re-engage directional semis after CPI clears.

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend = **PULLBACK_IN_UPTREND.** SPY 739.22, above 50-SMA (715.39) but below 20-SMA (746.37); −2.79% from the 90-day high; +1.04% over 30d. Breadth is decisively red: 2,120 bullish vs 4,108 bearish flow tickers (bullish_pct 34%). Guidance: half position sizes, defined-risk, iron condors in range.

**Per-index gamma (current-state EOD book):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 739.44 | null (unreliable) | **−1.32B** | FULLY_NEGATIVE (short-γ) | 755 (+2.1%) | 735 (−0.6%) |
| QQQ | 716.11 | null (unreliable) | **−209M** | FULLY_NEGATIVE (short-γ, mild) | 735 (+2.6%) | 700 (−2.2%) |
| IWM | ~284.4 | null | **−780M** | FULLY_NEGATIVE (short-γ) | — | — |

All three indices flipped POSITIVE→FULLY_NEGATIVE on **06-05** (the −2.7% SPY / −4.6% QQQ selloff, VIX +40% to 21.5). This is a **fresh, unstable short-gamma regime**, not a held one — the most trend-prone *and* the most whipsaw-prone configuration. §2 reads these levels forward as the next-session prior.

**`uw options-flow dte-volume-share`:** 0DTE 39.1% / weeklies 24.6% / monthlies 23.4% / LEAPs 5.4%. regime_hint BALANCED — moderate institutional share; 0DTE-heavy enough to flag a retail-dominated intraday tape (esp. QQQ).

**`uw historical vrp` (SPY):** +0.035, **FAIR** — IV30 15.58% vs realized30 12.08%. Vol is neither cheap nor rich; no VRP edge at the index level. *(Single names tell a different story — see §5; LRCX/AMD/MRVL IV ranks 83–93.)*

**Macro backdrop (`scripts/fred_macro.py`):** Yield curve **normal** (+0.41 10Y-2Y). Core CPI **2.99%** YoY, core PCE **3.29%** YoY — sticky, above target. Unemployment 4.3%, payrolls +172k. 10Y at **4.55% and rising** (+0.19/30d); USD **strengthening** (+1.98/30d); fed funds 3.62%. A **rates-pressured, sticky-inflation backdrop** — a headwind to long-duration growth and rate-sensitive longs.

**Forward event calendar (`event_risk`):**

| Event | Date | Proximity | Impact |
|---|---|---|---|
| **CPI (May)** | Jun 10 | **T+2** | HIGH |
| Jobless claims + PPI | Jun 11 | T+3 | Medium |
| **FOMC + SEP / dot-plot** | Jun 16–17 | **T+9** | VERY HIGH |
| OPEX (monthly) | Jun 19 | T+11 | Structural |
| MU earnings (AMC) | Jun 24 | T+16 | Name binary |

Three named Tier-1 binaries (CPI, FOMC, MU earnings) sit inside the swing horizon. **This is the dominant fact of the book** — it drives the systemic event-risk cut in §6.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book (open interest persists overnight) read forward as the prior for the 06-09 open. Prose-only, **0 rubric points**, no backtested predictive claim. SPY/QQQ only.

| Index | Spot | ZGL | Regime | Total GEX | Call wall | Put wall | Structure bias (next-session 0DTE) |
|---|---|---|---|---|---|---|---|
| **SPY** | 739.44 | null (`zgl_reliable=false`) | short-gamma | −1.32B | **755** (+2.1%) | **735** (−0.6%) | Short-gamma, spot inside a uniformly negative grid; no +GEX shelf until 750+. A break below **738** likely accelerates to 735→730 (dense −GEX at 735 −144M / 740 −124M); 755 is the first place hedging flips supportive. Favor **directional debit verticals on a confirmed break of 738**, not iron flies; topside fade only above 755. |
| **QQQ** | 716.11 | null (`zgl_reliable=false`) | short-gamma (mild) | −209M | **735** (+2.6%) / 730 (+1.9%) | **700** (−2.2%) | Weakly short-gamma, more two-sided. A **+GEX shelf at 712–715 is a soft floor** under spot; a clean push through **716** (largest local amplifier, −47M) has trend potential toward 730/735. Favor **directional / long-premium on a decisive break of 716**; fade an intraday flush at 712–715. |

**Regime freshness:** both flipped FULLY_NEGATIVE on **06-05** off the selloff — fresh and unstable, not a durable multi-session level.

**Mandatory caveats:**
- **EOD = prior, not target.** Fresh 0DTE OI floods in during the first 30–60 min and re-computes the ZGL/walls.
- **ZGL unreliable on both** (null on FULLY_NEGATIVE days) — regime read derived from `total_gex` sign + spot-vs-wall, not a ZGL crossover.
- **Gap risk is elevated.** CPI Jun 10 (+2d) can gap spot through the walls before any hedging engages; short-gamma books gap *harder*. The −1.32B SPY total_gex is a powder-keg prior into a known catalyst.
- **ETF book, not SPX/NDX index book** — structurally noisier.
- **Cannot isolate the D+1 expiry** (`gex --dte-max 1` errors) — this is the standing 0–45d proxy.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — validated stack)
The walls above are a map (advisory "where"), not a pin. What validates is **delta-neutral premium-selling.** Advisory, **0 rubric points**, NOT a guaranteed edge (validation sample has no vol shock → short-vol tail unsampled). Backtest verdict for both: **GO_PREMIUM_SELL_INTRADAY.**

| Index | Sell premium | Vol state | VIX | Implied move | Expected range | Size scalar | Structure | Caution |
|---|---|---|---|---|---|---|---|---|
| **SPY** | yes | HIGH | 18.92 | 1.09% | ±1.04% | **1.5** | Iron condor, wings ≈ ±1.04% | — |
| **QQQ** | yes | HIGH | 18.92 | 1.69% | ±1.52% | **0.75** | Wider iron condor, wings ≈ ±1.52% | **Front-end backwardation (0DTE IV 1.42×VIX) → half size** |

- **Whether:** front implied move systematically exceeds realized open-to-close (95% / 92.5% premium-sell open-win in the rolling backtest).
- **Size:** VIX HIGH → bigger (SPY 1.5×); QQQ trimmed to 0.75× on backwardation.
- **When:** enter at/after the open once the gap resolves; **hold the 0DTE to the close, never carry overnight** (overnight backtested negative); stand aside if it gaps beyond the wings — and given **CPI lands the morning of Jun 10**, the 06-09 session is the cleaner premium-sell window; stand aside into the CPI gap.
- **Direction:** none — delta-neutral. SPY ≈ SPX (validated identical); QQQ weaker (Nasdaq index book unavailable) — lower confidence.

## 2a. Swing Dealer Positioning (1–4 weeks)
`dealer-positioning-strategist` — the 06-05 selloff drove SPY/QQQ/IWM into FULLY_NEGATIVE gamma and flipped index DEX negative for the first time in the window (broad-based: 35/50 SPY strikes negative). Dealers are short gamma across the complex → 1–4wk realized vol stays elevated into CPI/FOMC.

- **Swing LONG (semi dip-buy cohort — positive DEX HELD through the selloff, dealers buy dips):** **MU** (strongest, +24.3B DEX held), **NVDA** (+12.3B, charm-supported), **AMD** (lean), **MRVL** (lean). Carried into §3 with the `dealer-positioning` tag.
- **Swing SHORT:** **IWM** (cleanest index short — negative DEX held + rate headwind), **META** (cleanest single-name short — fresh DEX flip held −4.38B, put-heavy), **MSTR** (lower-conviction, already-mature short improving toward zero).
- **NEUTRAL / stand-aside:** **QQQ** — recovered-positive DEX disagrees with panicked front-end backwardation + FULLY_NEGATIVE gamma; no clean thesis. SPY a defensive short-lean while DEX sub-zero but recovering (−46.6B→−11.4B).
- **No valid vanna squeezes anywhere** — every put-heavy index book is "vanna pressure, not squeeze" (VIX spiked 15.4→21.5→18.9, failing the falling-VIX gate). **Watch trigger:** if VIX mean-reverts under ~16 for 3 sessions while SPY/IWM stay put-heavy, the largest latent vanna-squeeze BUY setup in the complex arms — would flip SPY/IWM bias SHORT→LONG.

## 2b. Sector Rotation
`sector-rotation-strategist` — **rotation_regime: `no_change`** (low confidence). Every GICS sector prints persistence_score ≥0.8 INFLOW; **no sector rotating OUT by sign.** This is a bull-tape-wide melt-up with intra-sector dispersion, not a rotation. The synthesis "OUT = CommSvc/Healthcare/Industrials" is a WoW-magnitude-decay read, not a direction flip.

- **Daily-accelerating (watch, not rotation):** Consumer Cyclical (TSLA re-accel +679M today, ROST), Financial Services (IBKR), Healthcare (UNH cheap @ IVR 15, ABT — firming despite the synthesis "OUT" tag).
- **Conditional sector +1 gate: NO name qualifies** — only TSLA cleared |cum_flow_30d| ≥ $50M ($184.8M) but its direction is MIXED. All leaders feed the book at **base weight, no +1.**

**ETF flow tape (advisory — instrument layer GICS can't see):**

| ETF | Net prem dir | Persistence | DP positioning | Options urgency | GICS agreement | Leaders |
|---|---|---|---|---|---|---|
| **EWT** +5.24M | inflow | firm | near-ask constructive | Dec/Mar LEAP calls | n/a (Taiwan) | instrument-only |
| **XLV** +3.76M | inflow | bullish | +0.13 above mid (buy-lean) | call sweeps incl 2028 LEAP | **agree** (HC firming) | UNH, ABT, OSCR |
| **XOP** +3.36M | inflow | bullish | −0.28 below mid (C/R noise) | mixed | agree (Energy) — downgrade | — |
| **IGV** −26.0M | **outflow** | bearish | 723K sh −0.72 below mid (distribution) | mixed | **disagree** (GICS-Tech inflows) → watch-only | — |
| **XLK** −8.1M | **outflow** | bearish | below mid | LEAP-call dip-buying | **disagree** → watch-only | — |
| **XLY** −3.50M | **outflow** | bearish | below mid | **2027 Jan 120/115 puts $2M+$1.5M** | **disagree** → watch-only | — |

**Key divergence:** XLK/IGV/XLY ETF wrappers print net-bearish options tape **against** their inflowing GICS sectors → the melt-up is single-name-led (semis); the broad index wrappers are being **hedged/distributed.** Trade the names, not the wrapper. Advisory — adds no rubric points.

---

## 3. Swing Setups (1–6 weeks)

**No conviction entries today.** The fleet surfaced five LOW-tier candidates; the gate stack (debate disconfirmation + CPI-at-T+2 + AI-semis cluster) floored **all of them to SKIP/watch-only.** Listed for the record with the gates that killed them:

| Ticker | Score | Dir | Thesis | Structure | Invalidation | Final size |
|---|---|---|---|---|---|---|
| **MU** | 6 (LOW) | long | Swing-DEX dip-buy (+24.3B held) + July earnings-vol calendar; fundamentals CONFIRM (4/4 beats, +85.6% rev) | (if forced) vol calendar sell Jul-2 152% / buy Jul-24 105% | gap-down through CPI; 90d flow stays −$306M | **SKIP** — debate (bear 0.65 ≥ bull 0.65) −1, event_risk −1 (CPI T+2, earnings 06-24 T+16) |
| **MRVL** | 5 (LOW) | long | Call-dominant OI build ($261M call vs $31M put, 8.4:1) + S&P-500 inclusion Jun 22; CONFIRM | — | post-inclusion (06-22) sell-off; RSI<60 | **SKIP** — debate −1, event_risk −1 (CPI T+2), bullish_flow 0-for-7 floored |
| **LRCX** | 4 (LOW) | long | The only clean accumulation flag — DP mega buy_ratio 1.000 ($499M), 5/5 OI build, raised WFE guidance; CONFIRM | (if forced) starter long defended at $324.45 DP shelf | **loses the $324.45 DP shelf**; China export-curb headline | **SKIP** — debate −1, cluster −1 (AI-semis), event_risk −1 (CPI T+2) |
| **AMD** | 4 (LOW, watch) | long | DEX-lean long + strongest cum-flow (+$475.7M); CONFIRM but PE 160, late +46.5%/30d | — | put-dominant OI resolves bearish; close < 30d-rally base | **WATCH-ONLY** — single-agent, cluster −1, event_risk −1 |

### 3a. Long swings (regime-aligned)
All four longs above are AI-semiconductor names — **one correlated bet** (corr 0.71–0.80), and that bet is into a FULLY_NEGATIVE-gamma pullback, at/above analyst targets, on a `bullish_flow` signal class that **backtested 0-for-7 (0.0%) into this exact regime.** No distribution_flag fired on LRCX (C28 clean — verified real buying, not distribution). No long carries a distribution caution today.

### 3b. Short / fade swings (defined risk only)
- **META** (raw 4, watch-only) — `dealer-positioning` cleanest single-name SHORT (fresh DEX flip held −4.38B, put-heavy). **But fundamentals-gate CAUTION (−1):** the short fights healthy fundamentals (4/4 beats, +26% rev, recom 1.26, +40% to consensus target, Loeb added Q1). This is a **technical/momentum short** (price −26% from high, below all SMAs, RSI 39.5, Muse Spark AI delay), not a fundamental one. Single-agent → fails confluence gate → **SKIP/watch-only.** Tight invalidation on an SMA reclaim if traded at all.
- **NVDA** (raw 2) — `contrarian-scanner` fade-short-the-put-crowd (z +2.40 BEARISH_EXTREME, price-vs-flow +$29.5M bullish divergence) = directional-*bullish* fade. But `sweep-tracker` tags NVDA bearish 5/5 hedge tape and cum_flow_30d −$74.5M → **flow_conflict_lite −1**, nets to raw 2, below floor. Watch-only.

**Near-term sweeps (`sweep-tracker`, informational — 0 rubric points):** **MRVL** 5/5 persistence (CONTESTED — Aug 260/270C call build vs Jun-12 165P near-term hedge; debate adjudicated the call leg as the real opening conviction on dollar-weighting, 8.4:1). **SNDK** 3/5 bullish + deep-OTM downside insurance. **INTC** 3/5 genuinely two-sided (Jun-12 60P vs Jul-02 120C). **ORCL DISQUALIFIED** — earnings Jun 10 (T+2); the put build is pre-earnings hedging, route to §5 not a momentum short. Mega-cap index sweeps (SPY/NVDA/IWM/QQQ/TSLA 5/5 bearish) are **hedge flow**, not directional.

---

## 4. LEAP Builds (6–24 months)

**NO QUALIFYING CANDIDATES.** `leap-positioning-radar` ran the full 9-gate stack on the biggest LEAP-OI increases and every Step-0 bullish leader — **zero pass the 6-of-9 threshold.** A regime-consistent null: TRANSITIONAL/PULLBACK with a rising-10Y / sticky-PCE discount-rate headwind is structurally hostile to fresh long-duration accretion (LEAP DTE-share only 5.4%).

- The long-dated tape is **index/rate hedging, not single-name conviction** — SPX 8180-8190 Dec-2026 calls + 8000 puts, TLT/SHY/LQD put structures, IBIT downside puts.
- Every single-name 90d bull/bear cum-flow ratio sits within ±6% of 1.0 (no slow-accretion signature); NVDA and MU are actually net-*bearish* on 90d. Not one name produced conviction-matrix DIRECTIONAL_LONG>70 (max was MSFT 14.9%, and MSFT was flagged DISTRIBUTION).
- The CVNA Jan-2028 $2M whale (Step-0) is an OPENING_PUT — long-dated bearish hedge, correctly excluded.

**Re-scan when** regime resolves out of PULLBACK_IN_UPTREND, or a single name flips conviction-matrix DIRECTIONAL_LONG AND opens a >5% bull/bear cum-flow gap that widens across sessions.

---

## 5. Volatility Surface

`vol-surface-scout` — the entire liquid surface is in **mechanical front-end backwardation** from CPI (+2d) + FOMC (+9d); that is the null hypothesis, not a signal. One genuine dislocation:

- **MU — genuine July earnings-KINK** (classifier tagged BACKWARDATION, but it's a localized kink). Sawtooth: Jul-2 **152.3%** / Jul-10 110.7% / Jul-17 **150.9%** / Jul-24 105.3% — two ~25-vol-pt spikes flanking lows = earnings-expiry pinning around the **Jun-24 AMC print.** IV percentile 95th (z +1.37). **Play: calendar — sell Jul-2 (152%) / buy Jul-24 (105%)**, harvesting the earnings premium in the spiked expiry. (This is the same name surfaced as a swing-DEX long in §3 — but the *defensible* leg is the vol calendar, not the directional dip-buy.) Invalidation: kink flattens (event re-dated), or June front rises above July (panic migrated forward, not earnings).

**Event-mechanical backwardation (DISQUALIFIED as dislocations — do NOT fade now):** SOXX (z +2.60), STM (+2.38), FSLR (+2.23), EWY (+2.24), TXN (+1.90), ON (+1.59), KLAC (+1.96) — all smooth monotone CPI/FOMC decay with rising front-end ratios. **Revisit Jun 18 (post-FOMC):** if the front collapses and these flip to clean contango with a falling ratio, they become legitimate front-vol sales.

**Single-day earnings → route to earnings-scout (not surface dislocations):** ORCL (Jun 10), CHWY (Jun 10), RH (Jun 11), ADBE (Jun 11), SJM (Jun 9), CASY (Jun 9), ACN (Jun 18), KMX (Jun 17). `earnings-scout` reads: **no aggressive SELL VOL anywhere** (every name has complacent/flat back-month skew + front-end ratio >1.10 extreme panic). Cleanest expressions are **CALENDARS** on the extreme-panic megacaps (ORCL 2.11, CHWY 2.03, RH 1.99 bullish-lean, ADBE 1.94) — sell the panicked front, own the cheap complacent back. Half-size SELL VOL only on the lowest-panic names (ACN 1.48, SJM, CASY, KMX).

**No single-contract IV outliers** — all `iv-outliers` hits are 0DTE far-OTM quote-snapshot artifacts (fail the C12 liquidity floor). **Advisory (0 pts):** MU + TXN hit the lottery/expensive-skew composite (high IV-rank ∧ COMPLACENT call-rich skew) — color only; the C6 −2 fade line stays withheld (UPTREND regime fails the non-UPTREND gate).

---

## 6. Risk & Correlation

**Macro headline:** rates-pressured, sticky-inflation, **FULLY_NEGATIVE-gamma pullback.** Core PCE 3.29% / 10Y 4.55% rising / USD strengthening. **Forward calendar: CPI Jun 10 (T+2, HIGH), FOMC+SEP Jun 16-17 (T+9, VERY HIGH), OPEX Jun 19, MU earnings Jun 24 (T+16).** Three named Tier-1 binaries inside the swing horizon — the single largest force in today's book.

**Breadth cross-check (`fz`, advisory):** 181 advancers / 321 decliners, **pct_green 35.98%**, avg −0.26%; top INTC +11.19%, worst AKAM −4.99%. Red tape, **breadth-confirmed — no green/breadth divergence** (index is red and breadth is red, consistent). Does not change sizing.

**Correlation clusters (`uw risk portfolio-correlation`):**

| Pair | Corr | Action |
|---|---|---|
| LRCX/AMD | **0.798** | cluster |
| MU/SNDK | **0.778** | cluster |
| MU/LRCX | **0.714** | cluster |
| MRVL/LRCX | 0.664 | soft-watch (no penalty) |

→ **`AI_semis_cluster` = {MU, LRCX, AMD, SNDK}** (transitively linked ≥0.70). **MU is the kept member** (highest raw_score); LRCX and AMD take −1 cluster tier. MRVL escapes (0.664 soft-watch). Of today's longs, only MU and MRVL are *not* hard-clustered — and they carry the heaviest event/debate cuts. **Four longs are effectively one bet.**

**Fundamentals verdicts (2b):** MU **CONFIRM** (earnings 06-24, 16d) · MRVL **CONFIRM** (S&P add 06-22) · LRCX **CONFIRM** (real buying verified, raised WFE guidance; China export-curb risk) · META **CAUTION −1** (short fights 4/4 beats + recom 1.26 + Loeb) · AMD **CONFIRM** (overextended, PE 160). No VETO. **All four longs sit at-or-above analyst price target** — consensus-overextended (FZ advisory).

**Event-risk gate:** CPI at **T+2** is a named Tier-1 binary inside every horizon → **systemic −1 across the book** on insurance grounds (P1.2 re-scope: firing on a dated binary, not atmosphere). MU additionally carries its own 06-24 earnings inside the window.

**Debate-disconfirmation cuts:** MU, MRVL, LRCX all **bear residual ≥ bull residual (0.65 = 0.65)** → the disconfirmation did not clear any trade → **−1 each.** The bears' points are mutually reinforcing: above target, 0-for-7 bullish_flow regime, binary inside the window, negative gamma.

**`market_excess` (C2):** MRVL/LRCX/META/AMD all carry the **`beta`** tag (zero/negative excess vs SPY same-window). META's short is also beta (−0.10) — the "shorts = alpha" pattern does not apply to a technical short fighting its own fundamentals. **No clean-alpha name in today's book.**

**Adverse-flow exits** (carried `conviction_2026-06-05` = SMH/IWM/LLY/QQQ/JNJ): **QQQ** flow flipped bearish (net −10.2M, P/C 1.06) into negative index gamma → EXIT. **SMH** bearish, IV rank 98.9, P/C 2.68 → EXIT (off-thesis semis-long proxy). **IWM** bearish (P/C 1.49) into FULLY_NEGATIVE small-cap gamma → EXIT. JNJ soft exit-watch. LLY holds (flow bullish). No adverse alert on today's new longs.

**Hedge sleeve:** the residual long delta is a single AI-semis cluster bet — **SMH Jun-19 put spread (1–2% OTM, defined-risk)** hedges it directly and is cheap to structure against IV rank 98.9. Alternatively a VIX Jun call ladder for the CPI/FOMC tail. Given the book is near-flat post-gate, **lean SMH put-spread only — do not over-hedge.**

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**No HIGH or MEDIUM tier names today.** The highest quant raw_score is **6 (MU, LOW)** — nothing reaches the raw-7 MEDIUM cut. §7 is therefore empty of high-conviction calls; this is a defensive, low-conviction tape read, not a coverage gap.

**Expectancy lens (advisory — C31):** `[advisory — expectancy is not yet a live sizing axis]` — moot today (no HIGH/MEDIUM calls to size). Per the most recent `/calibration-audit` (2026-06-06), the ≥9 HIGH bin realized 0.774 (n=31, path-aware) vs MED (7–8) ~0.54; today's book sits entirely below those bins.

**Top-5 by raw_score (all LOW tier — below the §7 threshold, journaled for transparency, none sized):**

| Ticker | raw | dominant_signal_class | win_rate (n, src) | pre-risk | fundamentals | bull resid | gates applied | final |
|---|---|---|---|---|---|---|---|---|
| MU | 6 | earnings_vol | 0.80 (10, backtest, capped) | half | CONFIRM | 0.65 | event_risk −1, debate −1 | **SKIP** |
| MRVL | 5 | multi_day_sweep | 0.0 (7, backtest) | starter | CONFIRM | 0.65 | event_risk −1, debate −1 | **SKIP** |
| LRCX | 4 | dark_pool_accumulation | 0.636 (11, **fallback_proxy**) | half | CONFIRM | 0.65 | cluster −1, event_risk −1, debate −1 | **SKIP** |
| META | 4 | bearish_flow | 0.80 (10, backtest, capped) | starter | **CAUTION** | — | fundamentals −1, event_risk −1 | **SKIP** |
| AMD | 4 | bullish_flow | 0.0 (7, backtest) | starter | CONFIRM | — | cluster −1, event_risk −1 | **WATCH** |

Key audit flag: **`bullish_flow` class backtested 0.0% (n=7, all down) into this pullback** — every long-flow-dominant name is starter-floored by the sub-0.50 win-rate gate. The long book is structurally beta in an up-tape; today the up-tape isn't there.

**Conviction-scoring rubric (Step 4, verbatim — for audit):**
```
+3 dealer-positioning DEX flip / vanna-squeeze in trade direction
+3 3+ aligned accumulation (DP+OI+smart-pos, block-stratified inst) — C11: full +3 only if cum_flow_30d sign-aligned AND |≥$50M|; else +1
+1 multi-day OI build (oi-trend BUILDING, ≥5d)
+1 conviction-matrix DIRECTIONAL_LONG conf>70 — only when dominant_class==leap_directional; else 0
+1 cum-premium-flow net directional accretion 30d — intent-screened (no distribution_flag; not div-capture arb); else 0
+2 signal-confluence ≥4 (second-agent confirmation)
+1 sector-rotation single-name leader — persistence≥0.6 AND cum_flow aligned AND |≥$50M|
+1 earnings-scout BUY VOL / SELL VOL
+2 multileg directional structure (term-structure-anchored)
+1 vol-surface KINKED/BACKWARDATION with VRP-aligned bias
-2 contrarian overcrowded long w/ rising pc-ratio-zscore (VRP+)
-3 flow_conflict (30d cum_flow clearly opposite class) | -1 flow_conflict_lite (MIXED) — mutually exclusive
-1 correlation cluster (corr>0.7, applied 2d) | -3 regime conflict (applied 2d)
[gamma-flip 0DTE = 0 pts; sweep-persistence = 0 pts standalone]
TIERS: ≥9 HIGH | 7-8 MEDIUM | 3-6 LOW | ≤2 drop
```

---

## 8. Watch-only — single signal / unconfluenced / conflicted

Surfaced by one agent or killed by a flow conflict — **journaling only, NOT for trade entry today:**

- **META** (raw 4) — `dealer-positioning` SHORT only; single agent, no confluence ≥4; fundamentals CAUTION. Technical short, fights healthy fundamentals.
- **AMD** (raw 4) — `dealer-positioning` DEX-lean only (accumulation REJECTED MIXED); late +46.5%/30d, PE 160.
- **NVDA** (raw 2) — 2 bullish agents (dealer LONG + contrarian fade) but **flow_conflict_lite −1** (cum_flow −$74.5M, bearish sweep 5/5) drops it below floor.
- **MSTR** (raw 1) — direction CONFLICT: `dealer-positioning` SHORT (mature/decaying) vs `multileg` LONG (29,425-lot Aug-125C bid block). flow_conflict_lite −1.
- **MSFT** (raw 1) — `multileg` call-calendar LONG vs `accumulation` **DISTRIBUTION** (DP sell 5.43M vs buy 2.94M, px −3.08%/30d). flow_conflict_lite −1.
- **GOOGL** (raw −1) — `multileg` Aug 415/450 call vertical LONG, but **flow_conflict −3** (cum_flow −$298.8M clearly opposite). Drop.
- **SNDK** (raw 1) — `sweep-tracker` 3/5 only; single agent, fails confluence gate.
- **CBRS** — single-leg whale C19 Tier-1 **OPENING_PUT_PRIME** (bearish, size/OI 9.07, $625K, strike 240, DTE 18). Advisory **0 rubric points** (pending 60-day cross-regime validation); conflicts with CBRS bullish net premium — stands as a standalone advisory single-name short, not scored.

---

*Generated by `/daily-analysis` — 10 Phase-1 alpha-finders → quant → fundamentals-gate → bull/bear debate → risk-monitor. No HIGH/MEDIUM conviction names; near-flat book is the verdict. Watchlist `conviction_2026-06-08` = MU, MRVL, LRCX, META, AMD (persisted for tomorrow's correlation/adverse-flow loop).*
