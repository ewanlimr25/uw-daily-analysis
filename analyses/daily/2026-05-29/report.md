# Daily Market Analysis — 2026-05-29

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / UPTREND — SPY 756.48 (+6.31% 30d, −0.21% from 90d high, above 20/50 SMA), VIX 15.32 LOW, both indices **long-gamma**. Breadth is the tell: only 36.3% bullish flow and `fz` 195 advancers / 308 decliners (pct_green 38.8) → **breadth-divergence flag TRUE** (green index, red breadth = distribution). Tech call-flow dominant (+$11.6B) but semis (SMH) bleeding — intra-tech dispersion, not clean risk-on. Half-size / defined-risk regime.
- **Next-session GEX (SPY/QQQ):** SPY long-gamma · ZGL 755.93 (reliable, spot sits **on** it) · call wall 757 / put wall 750 → pin-and-suppress, tight. QQQ long-gamma (ZGL unreliable/extrapolated) · pin band 738–740 · call wall 760 / put wall 720. Advisory, see §2.
- **Top swing build:** **MSFT — LONG, HALF size.** The only name to clear the full Phase-2 gate stack. Mega-tier DP buy (94% at 450.24, $4.83B), cum-flow +$770M/30d, GEX regime flip N→P held, fundamentals CONFIRM (4/4 beats), earnings Jul-29 clear. raw_score 9 (MEDIUM), win_rate 0.65. Structure: defined-risk call debit spread. Invalidation: loses 450.24 DP shelf / cum-flow flips.
- **Top LEAP candidate:** **None qualify.** MSFT (Dec'27 720C/610C builds) and BRKR both clear 7-of-9 structural gates but fail conviction-matrix confidence>70 (35.1 / 39.4). Watchlist-promote, not size-now. Thin 5.9% LEAP tape + event cluster argues patience.
- **Biggest risk:** Event density — **four Tier-1 prints inside a 2-week swing horizon** (NFP Jun-5, CPI ~Jun-10, PPI ~Jun-11, FOMC+SEP Jun-16/17), plus ORCL earnings Jun-16 and HPE Jun-1. No correlation cluster ≥0.70 (MSFT/ORCL soft-watch 0.625). Post-gate book is a single half-size long → no mandated hedge; optional QQQ put vertical into NFP.

> **Net posture: a "no edge" day on the long-conviction book.** Three of four scored names floored to SKIP — two shorts (SMH, HPE) fight the uptrend into catalysts, the ORCL long is event/leverage/debate-cut. Only MSFT survives, at HALF. Correct response to a TRANSITIONAL tape with a distribution-tell breadth divergence into a four-print fortnight is a thin, defensive book.

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend UPTREND. SPY 756.48, above 20-SMA (739.34) and 50-SMA (703.65), +6.31% 30d, −0.21% off the 90d high. **Market breadth: 2,247 bullish vs 3,940 bearish flow tickers (36.3% bullish).** Trading guidance: half position sizes, defined-risk, iron condors in range.

**Per-index gamma (current-state EOD book; §2 carries the forward read):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 756.66 | 755.93 (reliable) | +1.219B | POSITIVE (long-γ) | 757 | 750 |
| QQQ | 738.40 | 308.67 (**unreliable**) | +0.676B | POSITIVE (long-γ) | 760 | 720 |
| IWM | 290.13 | 295.30 | negative | **flipped P→N 05-29** | — | — |

IWM is the one fresh regime flip — small-caps entered dealer short-gamma 05-29 (spot below ZGL), most exposed to the rate-event stack. Watch, not actionable.

**`uw options-flow dte-volume-share`:** 0DTE **40.8%**, weeklies 21.2%, monthlies 18.2%, LEAPs 5.9% → **RETAIL_DRIVEN**. High 0DTE share = no institutional benefit-of-doubt for swing/LEAP positioning; thin long-dated tape.

**`uw historical vrp`:** SPY **FAIR** (vrp +0.0265; IV30 12.68% vs realised 10.02%); QQQ **FAIR** (vrp +0.0435; IV30 20.17% vs realised 15.82%). No broad vol-edge either direction — premium-selling edge is single-name, not index-wide.

**Macro backdrop (`scripts/fred_macro.py`):** Yield curve **normal** (+0.46, 10Y−2Y). Core CPI **2.99%** YoY / Core PCE **3.29%** (sticky, above target). Unemployment 4.3%, payrolls +115k (softening labor). 10Y **4.45% and rising** (+0.09 30d), USD **strengthening**, fed funds 3.62%. Rising-10Y + strong-USD is a mild headwind to long-duration tech multiples.

**Forward event-risk calendar (Tier-1, next ~10 trading days):** NFP **Jun-5**, CPI **~Jun-10**, PPI **~Jun-11**, FOMC + SEP **Jun-16/17**. All four land inside a 2–3 week swing horizon. *(Dates confirmed against standard 2026 release cadence; FOMC mid-month.)*

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD 0–45d dealer-gamma book (open interest persists overnight), read forward as the *prior* for Monday's open. Prose-only, **0 conviction points**, no backtested predictive claim (that validation lives in `/weekly-analysis`). SPY/QQQ only.

**SPY** — spot 756.66 · ZGL **755.93 (reliable**, sits 0.1% under spot) · regime **POSITIVE / long-gamma** · total_gex **+1.219B** · **call wall 757** (+396M, dense 755–757 shelf) · **put wall 750** (shallow). Spot is sitting essentially *on* the ZGL under a tight call-wall stack → pin-and-suppress: dealers sell into 757, buy dips toward 755, compressing realized vol. The call wall at 757 is the dominant magnet; a poke through hits 760 before resistance thins. **Structure bias:** iron fly / short straddle / butterfly centred 756–757; the 0DTE straddle is rich vs this compressed range. If spot loses 755 at the open, the long-gamma thesis voids → 755 is the short-gamma trigger toward 750.

**QQQ** — spot 738.40 · ZGL **308.67 (UNRELIABLE** — extrapolated garbage, do not quote) · regime **POSITIVE / long-gamma** (total_gex +675.9M) · effective pin band **738–740** (heaviest +GEX) · call wall 760 · put wall 720 (thin/far). Inferred long-gamma from positive total_gex with spot embedded in the heaviest +GEX strikes. Treat ~736 as the practical flip line — a clean break under 735–736 opens a thin −GEX air pocket toward 720 with little support. **Structure bias:** iron fly / short straddle centred 738–739; condor wings lean on 750 (upper shelf) and 730–735. QQQ VRP richer (better-compensated wings), but downside is asymmetric — size the put wing for the 720 gap, not a graceful 730 catch.

**Regime stability:** SPY POSITIVE but *whippy* (8 flips in 30d; re-flipped to POSITIVE 05-28 — fresh, fragile, sitting on its ZGL). QQQ POSITIVE and *stickier* (held since ~04-30) — better-established long-gamma prior despite the unreliable ZGL.

**Mandatory caveats:** EOD = prior, not target (first 30–60 min of fresh 0DTE OI re-computes the walls, esp. SPY's tight 757 cap) · gap risk voids the prior (no event before Monday open, but NFP/CPI/FOMC ahead can gap spot off the ZGL) · this is the **ETF** book, not the cleaner SPX/NDX index book · uw-pp cannot isolate the D+1 expiry (this is the 0–45d aggregate proxy) · QQQ ZGL specifically void — flip read inferred from +GEX mass + total_gex sign only.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — the validated stack)

> The GEX walls above are a **map (advisory "where"), not a pin** — wall-as-magnet and every directional 0DTE signal backtested NO_GO. What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, NOT a guaranteed edge (no vol shock in the validation sample → short-vol tail unsampled).

Backtest verdict both indices: **GO_PREMIUM_SELL_INTRADAY** (SPY 97.1% open-entry win, n=34; QQQ 94.1%, n=34).

| Index | Sell premium | Vol state | VIX | Implied move | Exp. range | Size scalar | Suggested structure |
|---|---|---|---|---|---|---|---|
| SPY | ✅ | LOW | 15.32 | 0.48% | 0.70% | 0.5 | Iron fly / short straddle @ 756.72, wings ≈ ±0.7% (long-γ: quieter, mean-reverting) |
| QQQ | ✅ | LOW | 15.32 | 0.80% | 1.19% | 0.5 | Iron fly / short straddle @ 738.49, wings ≈ ±1.19% (long-γ) |

- **When:** enter at/after the open once the overnight gap resolves; **hold to the close, never carry overnight** (overnight entry backtested negative). If it gaps beyond the wings, stand aside.
- **Size:** LOW vol state → `size_scalar` 0.5 (thinner edge at low VIX). No stand-aside / caution flag set on either index.
- **Direction:** none — delta-neutral. **SPY ≈ SPX** (validated identical); **QQQ weaker** (Nasdaq index book unavailable) — flag lower confidence.

## 2b. Swing Dealer Positioning (1–4 weeks)

`dealer-positioning-strategist`: every index book is **call-heavy / net-long-DEX** (SPY +75.6B, QQQ +72.3B, IWM +10.5B) → **no vanna squeezes anywhere** (call-heavy book + VIX not in a ≥3-session downtrend = vanna *pressure to sell on IV drops*, not a squeeze).

- **SPY** — DEX positive, vol-suppressed grind; swing_bias NEUTRAL-to-mild-LONG. Invalidation: closes <753 ZGL ≥2 sessions.
- **QQQ** — cleanest long-gamma perch (POSITIVE every session since 05-22); swing_bias mild-LONG. Invalidation: <730.
- **IWM** — **fresh 05-29 P→N regime flip**; swing_bias NEUTRAL with downside-vol risk into the rate stack. Invalidation of bearish-vol read: reclaims 295.30 ZGL.
- **SMH** — the clean single-name swing **SHORT**: only probed name with a balanced/put-heavy dealer book, broad short-gamma 8/10 sessions, genuine 28d backwardation, IVR 89, distribution + put-OI building. (Carried into §3b; gated to SKIP below.)
- **MSFT** — swing **LONG**: confirmed GEX regime flip 05-28 N→P + total_gex surge to +721M on the post-earnings move; dealer long-gamma now supporting.
- **ORCL** — swing LONG but choppy ZGL (4 flips/10d, lower conviction). **PLTR/TSLA** — momentum/no dealer edge, NEUTRAL.

## 2c. Sector Rotation

`sector-rotation-strategist`: **rotation_regime = `no_change`** (confidence low). Every GICS sector shows persistence_score 1.0 (max) but **uniformly INFLOW** — when everything rotates in, nothing rotates. No out-leg = no canonical defensive↔cyclical pattern. Beta-on melt-up signature, not rotation. The regime tool's "money-flowing-out" list (Basic Materials / Comm Svcs / Cons Cyclical) is contradicted by both the persistence tool and single-day sector-flow → discarded as uncorroborated.

**ETF flow tape (advisory — 0 rubric points). The signal lives in the intra-Tech dispersion the GICS aggregate masks:**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| IGV (software) | +$49.4M | BULLISH 5/5 | $113M below-mid (hedge tell) | mixed-bearish (Aug put-buying) | agree | MSFT, DELL, ORCL |
| XLK (tech) | +$20.5M | BULLISH 5/5 | $153M+ below-mid | bullish-leaning (Jun 160C block) | agree | MSFT, DELL, ORCL |
| XLF (financials) | +$4.2M | BULLISH 5/5 | — | — | agree | GS, BAC |
| **SMH (semis)** | **−$70.0M** | **BEARISH 5/5** | $153M below-mid | **bearish-urgent (Jun/Jul ask-side puts)** | **DISAGREE** | — |
| XOP (E&P) | −$3.8M | BEARISH 5/5 | thin | put-leaning | disagree (XLE +$11M inflow) | — |

**Read:** software/mega-cap tech (XLK/IGV, 5/5 inflow) over **semis (SMH −$70M, 5/5 bearish, urgent put-buying)** — an *intra-Tech* rotation the "Technology +$11.6B" aggregate completely hides. Energy: integrated majors (XLE) over E&P (XOP). Tactical only while 0DTE share 40.8%.

---

## 3. Swing Setups (1–6 weeks)

### 3a. Long swings (regime-aligned)

| Ticker | Score | Tier | Thesis | Structure | Invalidation | Final size |
|---|---|---|---|---|---|---|
| **MSFT** | 9 | MEDIUM | Mega-tier DP buy 94% @450.24 ($4.83B) + cum-flow +$770M/30d + GEX flip N→P held; fundamentals CONFIRM (4/4 beats, +17.9% rev, D/E 0.26); analyst Recom 1.23 (+24% target). The cleanest flow-fundamentals confluence on the board. | Defined-risk call debit spread (regime caps at half; batch-scan's "aggressive long calls" downgraded to defined-risk per TRANSITIONAL). DP support 450.24. | Loses 450.24 DP shelf (next 426.99); cum-flow flips MIXED/bearish; GEX regime back to negative. | **HALF** |
| ORCL | 8 | MEDIUM | Bullish flow +$60M + cum-flow +$145M/30d + GEX flip N→P; software leader; win_rate 0.793. **But:** earnings Jun-16 inside horizon, D/E 4.67 debt headlines, 90d cum-flow −$217M (30d is a reversal), only +7.9% to target. | — | — | **SKIP** (fundamentals −1, event-risk −1, debate −1) |

**MSFT is the lone survivor.** ORCL: high win_rate but market-excess gate flags it as beta-in-uptrend (0.793 < SPY 1.00), and three independent gates cut it — viable only as a pre-earnings momentum scalp de-risked before Jun-16, not a held swing.

### 3b. Short / fade swings (defined risk only)

| Ticker | Score | Tier | Thesis | Disposition |
|---|---|---|---|---|
| **SMH** | 10 | HIGH | Multileg put-spread (repeat 5, 540P Jun05 / 590P Jul17 + wings, backwardation) + dealer short-gamma 8/10 + sector outflow −$70M 5/5 + cum-flow −$77.7M + DP distribution. Highest raw_score on the board. | **SKIP** — regime −1 (short vs UPTREND) + debate −1 (anti-short 0.65 ≥ pro-short 0.55). DEX +3B call-long *contradicts* the short (LB-gate 4/5); win_rate 0.433 (sub-coin-flip); shorting 2% from 52w high into a Dell/Micron AI-server melt-up. Watch-don't-touch. |
| HPE | 4 | LOW | DP distribution mega 30% buy $519M into +62.8%/30d strength; insider selling −14.77%; RSI 83; price 29% above analyst target. | **SKIP** — regime −1 + fundamentals −1 + event-risk −1 + debate −1. Shorting a 4/4 beat-streak name into a 2-trading-day-out print (Jun-1) with SI 5.14% / 3.85d-cover squeeze fuel = hard pass. |

**Near-term sweeps (`sweep-tracker`, informational — 0 rubric points):** **MRVL** cleanest bullish confirm (3/5 persistence, call-side opening OI build 200–230C, `opening_confirmed`). INTC bearish (3/5, Jun 80P opening). AMD bearish 5/5 but decaying (today's tape flipped MIXED). Demoted on thesis-conflict (persistence tag vs put-heavy OI): ASTS, MU, SNDK. All mega-cap NVDA/SPY/QQQ/TSLA/META sweeps = hedge-flow (cum_flow_90d MIXED), 0 points.

**Single-leg whale (advisory C19, 0 points):** Tier-1 bearish — **ISRG** FLOOR_PUT_BLOCK 520P Jun18 (+ DP distribution = strongest bearish co-confirm), **AXTI** / **AAOI** OPENING_PUT_PRIME. No call signals scored (calls are beta in bull regime).

---

## 4. LEAP Builds (6–24 months)

**No name qualifies for a size-now LEAP.** Two structural survivors, both fail the conviction-matrix confidence>70 gate:

- **MSFT** — 7/9 structural gates: Dec-17-2027 (DTE 567) 720C +7,889 / 610C +7,756 genuinely fresh (oi_change 32–59×, ask-side), 5d BUILDING, $4.2B DP lift at 450.24, ACCUMULATION bsr 4.42. **Fails Gate 8: conviction-matrix confidence 35.1 (<70).** Fresh-thesis profile (88% of 90d flow in last 30d). Watchlist-promote.
- **BRKR** — 7/9: Dec-18-2026 40C deep-ITM +932, cleanest BULLISH cum-flow tag (sign-consistent 90d), 167k-share DP print at 58.29. **Fails Gate 8: confidence 39.4.** Entry-extended (+44.7%/30d) on expensive 61% IV.

**Disqualified near-misses:** GS (cum-flow 90d −$8.5M wrong-direction), ORCL (90d −$217M, near-dated OI not LEAP), PLTR (30d −$82M sign-reversal, put-heavy long-dated build).

Thin 5.9% LEAP tape + NFP/CPI/FOMC cluster → patience over initiating long-dated convexity into the next two weeks.

---

## 5. Volatility Surface

`vol-surface-scout` + `earnings-scout`: the entire high-IV cohort is **earnings-IV-crush** (positive VRP, IV-pctile 100), not genuine term dislocation. **No clean no-catalyst calendar today** — the ULTA (ratio 4.03) and SMH (2.50) "BACKWARDATION" flags are dead-0DTE artifacts (exclude the expiring contract → clean downward slopes), disqualified as calendars. **Universal caveat:** back-month 25Δ skew is COMPLACENT (calls bid over puts) on every large-cap → tail unpriced → every SELL VOL is **half-size max**.

| Ticker | ER date | Verdict | Size | Kink / VRP | Note |
|---|---|---|---|---|---|
| HPE | Jun-1 | SELL VOL | half | Jun-5 kink 166%, VRP +0.314 (richest) | Bearish flow caveat; NFP Jun-5 lands on the front expiry |
| PANW | Jun-2 | SELL VOL | half (light) | Jun-5 kink 104% | −$20M bearish flow = watch (lean put-side) |
| GTLB | Jun-2 | SELL VOL | half | Jun-5 kink 151%, flattest tail | Riskiest; small-cap defined-risk only |
| **ORCL** | Jun-10 | SELL VOL | half | Kink correctly at Jun-12/18 ER expiry | Cleanest ER-aligned kink; deepest liquidity |
| ADBE | Jun-11 | SELL VOL | half | Jun-12 kink 71% | Cleanest curve, lowest juice |
| NTSK | Jun-3 | SELL VOL | ~full | Backwardation, **back-skew +0.072 NORMAL** | Only name with tail independently priced → near-full size |
| SAIL | Jun-9 | SELL VOL | half | Backwardation, mild tail pricing | Thin liquidity |
| **CRWD** | early Jun | **SKIP** | — | Bimodal (Jun5 106% / Jun18 122%) | Event expiry ambiguous — no clean kink to sell |

**DELL is the lone PREMIUM_BUYING name** (VRP −0.408, realized > implied post-earnings) — do not sell DELL premium. Single-contract IV outliers (SOXL/S/SMCI/SPCE) are all 0DTE expiry-day lottery prints — advisory, not tradeable surface dislocations.

---

## 6. Risk & Correlation

**Macro headline:** sticky core inflation (CPI 2.99% / PCE 3.29%) + rising 10Y (4.45%) + strengthening USD = mild duration headwind. **Forward calendar: NFP Jun-5, CPI ~Jun-10, PPI ~Jun-11, FOMC+SEP Jun-16/17 — four Tier-1 prints inside the swing horizon.** Per-name earnings inside horizon: HPE Jun-1 (~2 trading days), ORCL Jun-16 (collides with FOMC). MSFT Jul-29 clear.

**Correlation (`uw risk portfolio-correlation` on today's 4 candidates):** only two pairs surface, both in the 0.60–0.70 **soft-watch** band — **no cluster, no penalty.** MSFT/ORCL 0.625 (same software-megacap bet — monitor), ORCL/HPE 0.58 (below threshold). SMH short does not cluster (≥0.70) with the MSFT/ORCL longs → neither a mechanical conflict nor a credited hedge; it stands as an independent (gate-cut) line.

**Fundamentals verdicts (Phase 2b):** MSFT **CONFIRM** (4/4 beats, +17.9% rev, analyst Recom 1.23 / +24% target, earnings 60d out). SMH **NA** (ETF — semis tape bullish *against* the short, but NA never demotes). ORCL **CAUTION −1** (Jun-16 earnings inside horizon + D/E 4.67 / debt headlines; fundamentals direction itself supports the long). HPE **CAUTION −1** (Jun-1 earnings + 4/4 beat-streak squeeze + SI 5.14%/3.85d-cover; insider selling/overextension lean toward the short but the imminent catalyst is hazardous).

**Debate-disconfirmation cuts (Phase 2c):** SMH, ORCL, HPE all **cut** (against-trade residual ≥ for-trade). MSFT **clears** (pro-long 0.75 > kill 0.65 — both sides called it a sizing/timing caveat, not a direction kill).

**Breadth cross-check (`fz`, advisory):** 195 advancers / 308 decliners, pct_green 38.8 — **divergence vs the green index (distribution tell)**. Does not change mechanical sizing, but corroborates every CAUTION/debate-cut and argues against adding long beta at full size.

**Adverse-flow exit candidates (carried `conviction_2026-05-28`):** **SMH** — P/C 9.18, net −$13.6M, OI +199k, flow flipped hard bearish → exit / do-not-hold-long. **ASTS** — flow bearish, net −$55.1M, IVR 90.5, 3× volume → exit. MSFT flow still bullish (thesis intact). BRKR 16.4× volume spike but bullish anomaly (monitor, not adverse).

**Hedge sleeve:** post-gate book = MSFT half-long only → below the 0.6 net-delta threshold → **no mandated index hedge.** Discretionary: given the breadth-divergence + rising-10Y backdrop, a small defined-risk QQQ put vertical (1–2% of the long's notional delta) into NFP Jun-5 is reasonable — advisory.

---

## 7. High-Conviction Cross-Ref (HIGH & MEDIUM tier — raw_score ≥ 7)

| Ticker | raw_score | Tier | Dir | Dominant class | win_rate (n, src) | Pre-risk | Fund. | Debate (for) | Gates fired | **Final** | Invalidation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **SMH** | 10 | HIGH | short | multileg_directional | 0.433 (30, backtest) | starter | NA | 0.55 | regime −1, debate −1 | **SKIP** | Reclaims 590 + positive-GEX ≥3 sessions |
| **MSFT** | 9 | MEDIUM | long | dark_pool_accumulation | 0.65 (28, proxy) | half | CONFIRM | 0.75 | none (MSFT/ORCL soft-watch) | **HALF** | Breaks 450.24 DP shelf; cum-flow flips |
| **ORCL** | 8 | MEDIUM | long | bullish_flow | 0.793 (29, backtest) | starter | CAUTION | 0.65 | fundamentals −1, event −1, debate −1 | **SKIP** | Below 197 ZGL; de-risk before Jun-16 |

**Score components (quant audit trail):**
- **SMH (10):** +3 multileg put-spread (repeat 5, backwardation) · +3 cum-flow −$77.7M SHORT-aligned 30d (2.1× union median) · +2 signal-confluence bearish 5 · +1 sector outflow leader (all 3 gates pass) · +1 accumulation distribution co-flag.
- **MSFT (9):** +3 cum-flow +$770M LONG 30d (21× median) · +3 accumulation C11 conjunction FULL (cum-flow ≥$50M LONG confirms DP+OI+smart-pos) · +2 signal-confluence bullish 5 · +1 software sector leader. (conviction-matrix DIRECTIONAL_LONG = 0 pts, non-LEAP gate.)
- **ORCL (8):** +3 cum-flow +$145M LONG 30d (reversal of 90d −$217M; 30d-scoped, no flow_conflict) · +2 signal-confluence · +2 dealer GEX flip N→P · +1 software sector leader.

**Quant-dropped (raw_score ≤2 floor) — watch-only:** **LRCX** (raw 2: +3 DP distribution +2 confluence **−3 flow_conflict** — extreme distribution but +$58.9M *bullish* 30d flow opposes the short; the NVDA-failure-mode catch). **GS** (raw 2: C11 accum halved at $14.6M<$50M + confluence − flow_conflict_lite). **BRKR** (raw 2). **LQDA** (raw 2, micro-tier).

> **Conviction-scoring rubric (Step 4, verbatim for audit):**
> `+3` dealer DEX-flip/vanna-squeeze in trade dir · `+3` accumulation 3+ aligned (DP+OI+smart-pos, block-stratified) — **C11 conjunction: full +3 only if cum_flow_30d sign-aligned AND |cum_flow|≥$50M; else +1** · `+1` multi-day OI BUILDING · `+1` conviction-matrix DIRECTIONAL_LONG conf>70 — **LEAP context only** · `+3` cum-premium-flow net directional accretion (30d) · `+2` signal-confluence ≥4 · `+1` sector single-name leader — **conditional: persistence≥0.6 AND cum_flow aligned AND |cum_flow|≥$50M** · `+1` earnings BUY/SELL VOL · `+2` multileg directional · `+1` vol-surface KINKED/BACKWARDATION VRP-aligned · `+1` opex top-5 (OPEX wk) · `−2` contrarian overcrowded long · `−3` flow_conflict (cum-flow clearly opposite class) / `−1` flow_conflict_lite (MIXED) — *mutually exclusive* · `−1` corr-cluster (2d) · `−3` regime conflict (2d). Tiers: ≥10 HIGH · 7–9 MEDIUM · 3–6 LOW · ≤2 drop.

*No HIGH-tier post-gate name → Step 8.5 deep-dive hand-off skipped (MSFT is MEDIUM).*

---

## 8. Watch-only — single signal / sub-threshold

Not for trade entry today — journaling only:

- **AAPL** — multileg bull call vertical (320C/345C Aug21, repeat 2, CONTANGO, HIGH structural conviction) but single-agent, no confluence.
- **MRVL** — bullish sweep persistence 3/5 + call-side opening OI build (200–230C, `opening_confirmed`); single-agent. Cleanest bullish sweep on the tape.
- **IGV** — multileg put-write (90P/85P Aug bid) financing 90C Dec18 = bullish carry/risk-reversal; MEDIUM, uncapped risk.
- **ISRG / AXTI / AAOI** — single-leg whale Tier-1 bearish puts (advisory C19, 0 points); ISRG strongest (FLOOR_PUT_BLOCK + DP distribution, −9.5%/30d downtrend).
- **INTC** (bearish sweep 3/5 + Jun 80P opening), **AMD** (bearish 5/5 decaying), **PLTR** (signal-confluence dp_accumulation but accumulation agent culled as MIXED/NEUTRAL DP; dealer NEUTRAL), **DELL** (RS new-high + sector leader but earnings done, watch-only tag).
- **LRCX / GS / BRKR / LQDA** — quant-floored (raw 2); see §7.
- **IWM** — fresh 05-29 dealer-gamma regime flip P→N; track for short-gamma follow-through into the rate stack.

---

*Generated by `/daily-analysis` — 10 Phase-1 alpha-finders → quant → fundamentals-gate → bull/bear debate → risk-monitor. Watchlist `conviction_2026-05-29` written: SMH, MSFT, ORCL, HPE.*
