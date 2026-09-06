# Daily Market Analysis — 2026-05-27

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / UPTREND — SPY 750.46 (>20/50 SMA, +4.93% 30d, -0.22% from 90d high), VIX 16.29 LOW, VRP FAIR. Breadth is the tell: only **37.1% bullish options flow** and S&P **pct_green 46.9%** (more decliners than advancers) into a near-high tape — a mild distribution / breadth-divergence signal under the uptrend. Half-size guidance. Sector: software/megacap bid (XLK/IGV), semis hedged (SMH protective puts), cyclicals (XLY/XLI) the cleanest inflow; Energy the lone persistent outflow.
- **Next-session GEX (SPY/QQQ):** **SPY** — knife-edge **fresh NEGATIVE flip**, spot 750.62 ~on ZGL 751.87 (reliable); razor-tight call wall **752** (+0.18%) vs wide put wall **730** (-2.75%); bias = pin/iron-fly ~751, flip to debit puts only on a clean break below 751.87. **QQQ** — **POSITIVE held 4 sessions** (ZGL unreliable/discarded), spot 729.48 buffered inside a 731/735/740 +GEX shelf; call wall **740** / put wall **715**; bias = range/pin ~730. *Advisory only — see §2.*
- **Top swing build:** **AMZN — starter long** (raw 7 MED, the ONLY name to clear the bull/bear debate, bull 0.75 > bear 0.55). Opening-confirmed Jul 290/300C OTM call build + confluence 5 + ConsCyclical sector leader; fundamentals CONFIRM strongest in set (strong-buy 1.24, +16.8% to target, rev +14.2%/EPS +36.5%). Structure: Jun/Jul call debit spread, starter size. Invalidation: loses 265 / Jul 290-300C OI build reverses. win_rate 0.525 (n=120). **Cut to starter on the PCE T+2 event gate.**
- **Top LEAP candidate:** **NONE.** Zero names cleared the 6-of-9 LEAP gate. The only genuine long-dated OI builds (CORZ/WOLF) are *bearish* (DIRECTIONAL_SHORT / put-inclusive); mega-cap "BUILDING" flags are near-dated flow, not LEAP accretion.
- **Biggest risk:** **PCE (April), 2026-05-29, T+2** — a Tier-1 inflation print inside every swing horizon, hit the entire book with a -1 event-risk cut. Compounding: a clean **adverse-flow reversal** — all five carried `conviction_2026-05-26` names (NVDA, AMD, SNDK, INTC, QQQ) flipped to bearish flow today. Correlation cluster: IWM/SMH 0.749 (one position). The genuine edge today is the **0DTE intraday premium-sell sleeve**, flat into PCE by construction.

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity"**, trend **UPTREND**. SPY 750.46, above 20SMA (735.29) and 50SMA (700.07), +4.93% 30d, -0.22% from the 90d high. Market breadth by flow: **2,291 bullish / 3,881 bearish tickers (37.1% bullish)** across 6,172 names — a bearish-leaning tape beneath a rising index. Trading guidance: half position sizes, defined-risk, iron condors in range.

**Per-index gamma (current-state EOD book; §2 carries the forward read):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 750.62 | 751.87 (reliable) | +821M | NEGATIVE (fresh flip today) | 752 (+0.18%) | 730 (-2.75%) |
| QQQ | 729.48 | 247.87 (unreliable, discarded) | +128M | POSITIVE (held 4 sessions) | 740 (+1.44%) | 715 (-1.98%) |
| IWM | 290.42 | — | +21M (thin) | POSITIVE (held since 05-22) | — | — |

**DTE volume share:** BALANCED — 0DTE 29.0% / weeklies 24.8% / monthlies 25.4% / LEAPs 6.6%. No retail-0DTE or institutional-LEAP regime tilt.

**VRP:** FAIR — SPY IV30 13.8% vs realised 10.1% (VRP +3.71%). "IV close to realised — no clear edge from VRP alone." No standalone vol-direction edge at the index.

**Macro backdrop** (`scripts/fred_macro.py`): yield curve **normal** (10y-2y +0.48); **sticky inflation** — core CPI 2.99% YoY, core PCE 3.2% (both above target); labor solid — unemployment 4.3%, payrolls +115k; **10Y 4.5% and rising**, **USD strengthening** = a mild risk-off / duration headwind on growth; fed funds 3.62%. **Forward event-risk (Tier-1, next ~10 trading days):** PCE (April) **2026-05-29 (T+2)**, NFP (May) 2026-06-05, CPI (May) 2026-06-10, FOMC + dots 2026-06-17 (inside the 2-4wk swing horizon).

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book (OI persists overnight), read forward as the *prior* for the 2026-05-28 open. **Prose-only, 0 rubric points, no backtested predictive claim.** Predictive validation lives in `/weekly-analysis` §2. Scope: SPY & QQQ only.

**SPY — knife-edge, fresh NEGATIVE flip.** Spot 750.62 is sitting essentially *on* the ZGL (751.87, reliable) after a same-day POSITIVE→NEGATIVE flip, yet `total_gex` is net **+821M** with the entire near-money +GEX stack (750/751/752 = +180/+206/+209M) at/above spot. Dealers are knife-edge gamma-neutral. **751.87–752 is the hinge:** a hold above keeps them long-gamma (mean-revert / pin into the +209M call wall at 752); a clean break below tips them short-gamma toward the wide 730 put wall. Walls are asymmetric — call wall razor-tight (+0.18%), put wall wide (-2.75%).
- **Structure bias:** long-gamma-while-above-ZGL favors a **pin / iron-fly centred ~751** (aligns with the 0DTE setup's 750.85 centre). If 751.87 breaks decisively at the open, abandon the fly → debit put vertical toward 740/735.

**QQQ — stable POSITIVE (held 4 sessions).** Reported ZGL 247.87 is a deep-OTM extrapolation artifact → **discarded** (`zgl_reliable=false`). Falling back to `total_gex` +128M (net long-gamma) + spot-vs-wall: spot 729.48 sits buffered inside a 731/735/740 +GEX shelf, channeled between the **715 put wall** and **740 call wall**. Genuinely stable long-gamma, unlike SPY's same-day flip.
- **Structure bias:** range / pin — **iron fly ~730** (0DTE centre 729.76) or a wider condor selling the 740 call wall and 715 put wall. No reliable intraday short-gamma trigger; use a 715 break as the proxy.

**Mandatory caveats:** (1) EOD is a *prior*, not a target — fresh 0DTE OI re-computes the ZGL/walls in the first 30-60 min. (2) **ZGL reliability** — SPY reliable (near spot); QQQ unreliable (extrapolated, marked false). (3) **Gap risk voids the prior** — PCE (T+2, 05-29) + Jobless Claims (T+1, 05-28) can gap spot through the tight SPY 752 call wall before hedging engages; QQQ (higher beta, rate-sensitive) gaps harder on a hot print with 10Y rising. (4) **Tooling limit** — cannot isolate the D+1 expiry; this is the 0–45 DTE proxy. (5) **ETF book**, not the cleaner SPX/NDX index book. SPY regime is a *fresh* flip (May tape whippy — flips 05-06/07/08/11/22/27); low regime persistence, fragile ZGL.

### 2a. Next-session 0DTE premium-selling setup (the validated stack — `scripts/zerodte_setup.py`)

The GEX walls above are a **map, not a pin** (wall-as-magnet backtested NO_GO). What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, NOT a guaranteed edge (validation sample has no vol shock → short-vol tail unsampled). Backtest verdict: **GO_PREMIUM_SELL_INTRADAY** (n=32).

| Index | Sell premium | Vol state | Implied move | Exp. range | Size scalar | Structure | Open-win (backtest) |
|---|---|---|---|---|---|---|---|
| **SPY** | Yes | LOW (VIX 16.29) | 0.70% | 0.71% | 0.5 | iron fly / short straddle centred **750.85**, wings ±0.71% | 96.9% |
| **QQQ** | Yes | LOW | 1.16% | 1.19% | 0.5 | iron fly / short straddle centred **729.76**, wings ±1.19% | 93.8% (lower confidence — Nasdaq index book unavailable) |

- **When:** enter at/after the open once the overnight gap resolves; **hold the 0DTE to the close; never carry overnight** (overnight entry backtested negative). If it gaps beyond the wings, stand aside.
- **Stand-aside:** none flagged today (no VIX spike / front-end backwardation). **SPY ≈ SPX** (validated identical); QQQ is the weaker read. Direction: none — delta-neutral. **This sleeve is flat into PCE by construction** and is the genuine edge today.

## 2a. Swing Dealer Positioning (1–4 weeks)

`dealer-positioning-strategist`: **the defining feature of this tape is that every book is call-heavy** (net vanna negative) — SPY, QQQ, IWM and all eight mega-caps. The falling VIX (18.06→16.29 over 6 sessions) is therefore a vanna *headwind* (dealer de-hedge selling), the **inverse of a squeeze — zero vanna-squeeze setups exist today.**

- **QQQ — mild LONG**, **IWM — mild LONG**: both flipped to positive-gamma on 05-22 and *held* it (QQQ stayed positive through today; IWM ran 282→290). Thin total_gex (QQQ +128M, IWM +21M) = a single risk-off session can re-flip.
- **SPY — NEUTRAL / caution**: re-flipped POSITIVE→NEGATIVE today as spot slipped below a rising ZGL, with a dense +GEX wall stacked 750-760 acting as overhead resistance.
- **Single names** (NVDA charm +2.07M, TSLA +1.65M, AAPL +1.11M all positive): single-snapshot DEX only, no per-day trajectory → NEUTRAL, not tradable swing theses per disqualifier rules.
- **Note:** the IWM mild-LONG dealer read directly **conflicts** with the multileg bearish put-ladder thesis (§3b) — flagged to risk. FOMC 2026-06-17 sits inside the 4-week horizon; any QQQ/IWM long carry is event-gated.

## 2b. Sector Rotation

`sector-rotation-strategist`: **rotation regime = `no_change` (low confidence).** Every GICS sector shows persistence_score 1.0 INFLOW — cyclicals AND defensives bid simultaneously = index-level call accumulation in an uptrend, **not** a clean rotation (the defensive leg isn't de-risking). One leg of the canonical pattern matches; disqualifier hit.

**Tech divergence resolved** (the Step-0 flag): options-premium netflow shows Tech **+8.5B** while the regime tool flags Tech **-433M outflow** — both correct on different sub-universes. The ETF tape splits Tech cleanly: **software/megacap is genuinely bid** (XLK +26.3M, IGV +20.1M, both 5d BULLISH; APP/AAPL/ORCL call premium) while **semis are being hedged/de-risked** (SMH -29.1M with the day's largest put sweeps — Aug-530P $10.9M, Aug-475P $10.6M, Jun-530P $8.1M ask-side, plus two bid-side DP sells at 595.5). Actionable read: **long software / hedge semis** — do not treat Tech as one leg.

**ETF flow tape (advisory — strengthens the conditional sector-leader +1, adds no rubric points):**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agree | Named leaders |
|---|---|---|---|---|---|---|
| EWY | inflow #1 | 5d BULLISH +29.7M | $69M closing prints upside-tilted | collar (Jan27 130C + Jun 200P hedge) | n/a (Korea) | — |
| XLK | inflow | 5d BULLISH +26.3M | $108M print BELOW mid (redemption tilt) | low-conviction bullish | agree (software) | APP, AAPL, ORCL, AXTI |
| IGV | inflow | 5d BULLISH +20.1M | $23M BELOW mid | bullish call-tilt | agree (software) | APP, ORCL |
| XLI | inflow | 5d BULLISH +15.9M | — | — | agree (Industrials) | CAT, UAL, VRT |
| XLY | inflow (cleanest skew) | 5d BULLISH +13.0M | — | — | agree (Cons Cyclical) | TSLA, AMZN, HD, MELI |
| **SMH** | **outflow #1** | 5d MIXED **-29.1M** | bid-side sells @595.5 (distribution) | **HIGH bearish** (Aug/Jun 530P ask) | **disagree → semis watch-only** | ADI, LRCX, CIEN |
| XLE | outflow | 5d BEARISH -5.5M | $151.6M @57.17 neutral | mixed | agree (Energy) | SU, SEDG |
| XOP | outflow | 5d BEARISH -4.1M | thin | low | agree (Energy) | SU |

**Swing-book implication:** no rotation regime to trade. Cleanest single-sector cyclical longs = XLY (TSLA/AMZN/HD) + XLI (CAT/UAL/VRT); long software (XLK/IGV); **avoid/hedge semis** (SMH protective-put tape); Energy the lone persistent outflow (SU/SEDG short-vol candidates, but idiosyncratic — no canonical counterpart).

---

## 3. Swing Setups (1–6 weeks)

Ranked by conviction score, post-gate. **The PCE T+2 event-risk cut and the disconfirming debate round compressed nearly the entire book** — only AMZN survived as a sized directional position.

### 3a. Long swings (regime-aligned)

| Ticker | Score | Tier | Thesis | Structure | Invalidation | Final size |
|---|---|---|---|---|---|---|
| **AMZN** | 7 | MED | Opening-confirmed Jul 290/300C OTM call build (4/5 sweep persistence) + confluence 5 + ConsCyclical leader; CONFIRM fundamentals (strong-buy 1.24, +16.8% upside, rev +14.2%/EPS +36.5%, AWS-AI catalysts: UBS $333, Snowflake $6B AWS today). **Only name to clear the debate (bull 0.75 > bear 0.55).** | Jun/Jul call debit spread | Loses 265; Jul 290-300C OI build reverses | **starter** (half −1 PCE event gate) |
| AAPL | 11 | HIGH | Mega-tier DP accumulation (br 0.87 n20) + OI BUILDING 5/5 +131k call-heavy + institutional-accumulation 1.77 DIRECTIONAL_LONG + cum-flow +494.5M, defending 310.85 DP shelf ($645M/168 trades) under 52w high 311.82. Batch-scan: "Aggressive Long Calls". | Long calls / Jun call spread | Breaks 310.85 DP support; OI build stalls | **watch-only** (half −3: CAUTION + debate-tie + PCE) |
| TSLA | 7 | MED | +1144M 30d cum-flow (largest in set) + confluence 4 + ConsCyclical leader; batch-scan "Long Call / debit spread", low IV rank 16. | Call debit spread | Loses 50SMA; flow rolls | **skip** (half −2: debate-tie + PCE) |

**Cross-ref / disagreements:** `uw playbook batch-scan` flags **edge on AAPL and TSLA but `has_edge=false` on AMZN** — the rule-based scan disagrees with the fleet's promotion of AMZN (which rests on sweep-persistence + confluence-5 + sector-leader, not a coordinated multileg structure; multileg saw AMZN as *single-leg* directional, no inferable spread). Treat AMZN's starter sizing as appropriately cautious given this disagreement. Per the multileg-vs-batch rule we'd prefer the multileg read — but multileg surfaced no AMZN structure, so the batch-scan's no-edge flag stands as a genuine caution.

**Persistence-ranked sweeps (informational, 0 rubric points):** the sweep book is hedge-dominated today — every high-persistence mega-cap (TSLA/SPY/NVDA/MSFT/META) failed the cum-flow alignment check (bearish sweep vs MIXED 30d signature = hedge, not short), and the $8.1B whale tape is an SPX deep-ITM 6000/7000C financing/roll block, not directional. **AMZN** (4/5, opening-confirmed) and **MRVL** (3/5 pure call-side build, but no co-flag → failed confluence gate, watch-only) are the only genuine directional builds.

### 3b. Short / fade swings (defined risk only)

| Ticker | Score | Tier | Thesis | Structure | Final size |
|---|---|---|---|---|---|
| **IWM** | 6 | LOW | Bearish Jun18 put ladder 282/277/270P (**repeat ×3**, highest-conviction structure on tape) + 30d cum-flow -145.7M; macro tailwind (10Y rising, USD strengthening = small-cap pressure). | Jun put spread | **watch-only** (half −2: debate + PCE) |
| **SMH** | 6 | LOW | Bearish 530P put calendar (**repeat ×3**, front IV 80.8% vs back 58%) + confluence 4 + backwardation; semis OUTFLOW -29.1M, DP distribution @595.5. | Put calendar (hedge) | **watch-only** (half −3: debate + cluster + PCE) |

**Both shorts were revealed by the debate as more-hedge-than-conviction** (bear 0.75 > bull 0.55 on each): win_rate 0.500 (coin-flip), the put structures are more plausibly downside insurance on long books than directional shorts, and IWM fights both a 52w-high uptrend and long-gamma dealers. SMH's cum-flow (-49.6M) fails its own $50M floor. **Contrarian-scanner surfaced ZERO clean fades** — ADI looked like one (BEARISH_EXTREME z+2.357) but is a PCE hedge (backwardation into 05-29), correctly aborted.

---

## 4. LEAP Builds (6–24 months)

**NONE.** Zero candidates cleared the 6-of-9 gate; none even passed the two required hard filters (bullish 90d cum-premium-flow + DIRECTIONAL_LONG conviction>70). Two failure modes:
- **Mega-cap "BUILDING" mirage** (META/TSLA/AMZN/GOOGL/AVGO/APP): all flag `BUILDING` but long-dated (>180d) share is 0.7–6.0% — the build is 0DTE/weekly/monthly flow, not LEAP accretion; conviction-matrix MIXED (conf 3.5–9.6).
- **Genuine LEAP builds that are BEARISH** (CORZ -39.9M / WOLF -60.4M 90d, GME COVERED_CALL, F DIRECTIONAL_SHORT): WOLF's fresh C65 10k-lot LEAP build is dealer/sell-side OI written *against* institutional put-buying — long-dated call OI that means the opposite of conviction. **Flag WOLF/CORZ for the bear cross-reference.** Regime gate itself is fine (UPTREND) — this is a genuine absence of bullish slow-accretion, consistent with the duration headwind.

---

## 5. Volatility Surface

`vol-surface-scout`: **no mispriced dislocation today — the surface is rich but correctly rich** into a dense 2026-05-28 earnings night. Indices calm (SPY CONTANGO 0.884, QQQ FLAT 1.034). VRP FAIR gives no index vol edge.

- **The entire IVR-100 list is one earnings-driven backwardation cluster** around the 05-28 print (MDB front ratio 3.22, DLTR 2.55, AMBA 2.75, MU 1.34, PANW 1.86, HPE 1.12, RDW 1.62) — every one with `kink_expiry=null` and a **COMPLACENT** back-month tail. Per the disqualifier (front-only panic + flat back-month = coin flip; ratio >1.10 = wait), **no name earns an aggressive SELL VOL.** The edge is the **CALENDAR** (sell panicked front, own normalized back).
- **Best calendars** (highest term-richness-to-implied-move): GTLB (ratio 2.0 / 3.3% move), PANW (1.86 / 3.1%), CIEN (1.97 / 5.5%).
- **Data-quality flag:** `iv-percentile-zscore` window is only 32 days, not 252 — "iv_percentile 100" means top-of-32, not a true 1y rank; the **z-score is the honest signal**.
- **RDW disqualified** (z 3.18, no defined catalyst). **Single-contract IV outliers: empty of signal** — all 20 are 0DTE/1DTE gamma artifacts. **Back-month skew uniformly COMPLACENT** — tail-hedge demand absent, consistent with LOW-VIX uptrend.

---

## 6. Risk & Correlation

**Macro headline:** sticky inflation (core CPI 2.99%, core PCE 3.2% above target), solid labor, **10Y 4.5% rising + USD strengthening = mild duration/growth headwind**. **Forward event-risk: PCE (April) 2026-05-29 (T+2)** — Tier-1, inside every swing horizon; then NFP 06-05, CPI 06-10, FOMC 06-17.

**Breadth cross-check (advisory):** S&P 500 — 236 advancers / 263 decliners, **pct_green 46.92%**, median change -0.05%, top mover APP +10.42%, worst BSX -12.46%. **Divergence flagged:** more decliners than advancers while the index sits near highs = a mild distribution tell that the single UPTREND label hides. Advisory, does not change sizing — but it corroborates the bearish 37% flow breadth and the half-size posture.

**Correlation clusters** (`uw risk portfolio-correlation`, 30d): one cluster fired — **IWM/SMH 0.749 (≥0.70)** → treat as one position; SMH cut as the lower-flow member (cum-flow -49.6M vs IWM -145.7M). Crucially, **AAPL/AMZN/TSLA did NOT mechanically cluster** (all pairs <0.57) — the long book is differentiated bets, not one stacked mega-cap trade (no discretionary upgrade applied). The IWM/SMH shorts correlate weakly (<0.57) to the longs → partial hedges, not duplicates — but both collapsed to watch-only, so the hedge value is moot. Soft-watch: IWM/CIEN 0.641.

**Fundamentals verdicts (top 5):**
- **AAPL — CAUTION (-1):** persistent insider net selling (MSPR -50.5 3mo: May -100 / Apr -30 / Mar -21) *into* the dark-pool accumulation; analyst upside exhausted (+1.68% to target), RSI 78.85. Not a VETO (4/4 EPS beats, +12.8% rev / +29% EPS, earnings 63d out) — but the cleanest distribution-vs-accumulation counter-signal on the board.
- **TSLA — CONFIRM (0):** no distribution signature; carry the flow-vs-analyst divergence (spot 10.25% *above* the $395 target, hold-rec; EPS -39% YoY, PE 422) — momentum long, no fundamental floor.
- **AMZN — CONFIRM (0):** strongest confluence (strong-buy 1.24, +16.79% to target, rev +14.2%/EPS +36.5%, ROE 23.3%, D/E 0.22; AWS-AI catalysts). Cleanest name.
- **IWM / SMH — NA (0):** ETF structural/hedge theses, no fundamental cross-check.

**Event-risk flags:** PCE T+2 applied -1 to ALL five swing names. DLTR earnings **tomorrow 05-28** (the event play — not gated). CIEN 06-04 (NFP 06-05 the next day).

**Debate-disconfirmation cuts:** AAPL (tie 0.65/0.65), TSLA (tie 0.65/0.65), IWM (bear 0.75 > bull 0.55), SMH (bear 0.75 > bull 0.55) — all cut -1. **Only AMZN cleared** (bull 0.75 > bear 0.55).

**Adverse-flow exit list:** all five carried `conviction_2026-05-26` names flipped bearish today — **NVDA** (-66.3M, $712M DP block + OI +555k), **AMD** (-85.5M, IVR 90), **SNDK** (-62.3M, PCR 1.35), **INTC** (-15.4M), **QQQ** (-31.3M). A clean adverse reversal across the prior semis/index book — tag all exit-candidate, do not carry forward.

**Hedge sleeve:** with one starter-size long (AMZN) and no sized shorts, book skew is well under 0.6 — **no dedicated hedge warranted.** Recommended sleeve is the **0DTE intraday premium-sell** (SPY/QQQ iron-flies, hold-to-close, never overnight), which is flat into PCE by construction.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

| Ticker | Raw | Tier | Dominant class | win_rate (n, src) | Pre-risk | Fund. | Bull/Bear | Gates applied | Final size | Invalidation |
|---|---|---|---|---|---|---|---|---|---|---|
| **AAPL** | 11 | HIGH | dark_pool_accumulation | 0.65 (n=5, **fallback proxy**) | half | CAUTION (-1) | 0.65 / 0.65 | fund -1, debate -1, event -1 | **watch-only** | breaks 310.85; OI build stalls |
| **TSLA** | 7 | MED | bullish_flow | 0.525 (n=120, backtest) | half | CONFIRM | 0.65 / 0.65 | debate -1, event -1 | **skip** | loses 50SMA; flow rolls |
| **AMZN** | 7 | MED | bullish_flow | 0.525 (n=120, backtest) | half | CONFIRM | **0.75 / 0.55** | event -1 (debate CLEARED) | **starter** | loses 265; Jul 290-300C OI reverses |

**AAPL score_components** (Σ = 11): +3 accumulation conjunction (accumulation-hunter / institutional-accumulation; mega-tier DP br0.87 + OI BUILDING 5/5 + cum_flow +494.5M aligned ≥$50M → full) · +3 cum-flow accretion 30d (quant / cumulative-premium-flow; +494.5M, 9.97× union median) · +2 signal-confluence 4 (quant / signal-confluence) · +2 multileg Sep ITM call ladder (multileg / hot-chains multileg) · +1 OI build 7d (accumulation-hunter / oi-trend). LB-gate: 4 of 5 cited (block-stratified, cum-flow, institutional-accumulation, signal-confluence) → HIGH preserved. **win_rate is an n=5 fallback proxy (CI ~0.22–0.94), not a backtest** — the bear's strongest unrefuted point; sizes half then gated to watch.

**TSLA score_components** (Σ = 7): +3 cum-flow accretion (+1144M, 23× median) · +2 signal-confluence 4 · +1 OI build 7d · +1 sector leader (ConsCyclical persistence 1.0 + cum-flow aligned + ≥$50M). C2 excess +0.03 (barely beats SPY beta), C4 OI opening confirmed.

**AMZN score_components** (Σ = 7): +3 cum-flow accretion (+65.5M ≥$50M) · +2 signal-confluence 5 · +1 OI build 7d (Jul 290/300C opening-confirmed) · +1 sector leader (3 gates pass). C2 excess +0.03, C4 opening confirmed.

**LOW-tier supporting (raw 4–6):** IWM (6, watch), SMH (6, watch), DLTR (4, earnings-vol starter — prints 05-28), CIEN (4, earnings-vol starter — 06-04).

**Deep-dive hand-off:** the only HIGH-tier name (AAPL) is gated to watch-only, so no full deep-dive fleet is launched (thin-edge day). Recommended manual deep dives if desired: `/stock-deep-dive AAPL` and `/stock-deep-dive AMZN`.

**VETO'd names:** none.

<details><summary>Conviction-scoring rubric (Step 4, verbatim for audit)</summary>

```
Daily conviction score = Σ:
  +3  dealer-positioning DEX flip / vanna-squeeze in trade direction
  +3  3+ aligned accumulation signals (DP+OI+smart-positioning, block-stratified) — C11 conjunction: full +3 only when cum_flow_30d sign-aligned AND |cum_flow_30d|≥$50M; else +1
  +1  multi-day OI build (oi-trend BUILDING, days≥5)
  +1  conviction-matrix DIRECTIONAL_LONG conf>70 — CONDITIONAL: only when dominant_signal_class==leap_directional; else 0
  +3  cum-premium-flow net directional accretion (30d)
  +2  signal-confluence ≥4 (second-agent confirmation)
  +1  sector-rotation single-name leader — CONDITIONAL: persistence≥0.6 AND cum_flow aligned AND |cum_flow_30d|≥$50M
  +1  earnings-scout BUY/SELL VOL
  +2  multileg directional structure (term-anchored)
  +1  vol-surface KINKED/BACKWARDATION VRP-aligned
  +1  opex-pin top-5 (OPEX week only)
  -2  contrarian overcrowded long + rising pc-ratio-zscore (VRP positive)
  -3  flow_conflict (30d cum-flow clearly opposite dominant class)
  -1  flow_conflict_lite (MIXED / bottom-quartile) — mutually exclusive with flow_conflict
  -1  correlation cluster (corr>0.7) — applied in 2d
  -3  regime conflict — applied in 2d
  [sweep-persistence = 0 points, deprecated 2026-05-23]
Tiers: ≥10 HIGH (full) · 7-9 MED (half) · 3-6 LOW (starter/watch) · ≤2 drop.
Step 3a: HIGH must cite ≥3 of 5 load-bearing tools (block-stratified, cum-flow, institutional-accumulation, dex, signal-confluence) or demote to MED.
Step 5 sizing: win_rate ≥0.70 full / 0.50-0.70 half / <0.50 starter. C2: n<10 cap 0.69; market-excess gate; C4 OI-opening gate. All downgrade-only.
```
</details>

---

## 8. Watch-only — single signal, no confluence

Surfaced from one agent / failed the confluence gate. For journaling, **not trade entry today**:
- **MRVL** — clean 3/5 call-side sweep build, opening-confirmed, but single-agent + no co-flag + bullish confluence <4 → failed confluence gate.
- **SOFI** — accumulation watch (block-tier, no mega-tier; 30d cum-flow -32.7M contradicts).
- **GTLB, AMBA** — earnings calendars, single-agent.
- **NTAP** — earnings BUY VOL/SKIP divergence (RSI 84.6 at 52w high, analyst target -18%).
- **IREN** — squeeze + leaderboard but MIXED conviction, put OI building.
- **VKTX** — DIRECTIONAL_LONG but sub-institutional (20 DP trades, $3.4M).
- **HPE** — earnings SKIP (non-monotone curve, second-event hump).
- **CAT, SU** — dropped on flow_conflict_lite (cum-flow not aligned).

**Distribution / avoid (confirmed):** **META** (bullish leaderboard +61.7M but mega-tier DP SELLING br 0.238 = distribution; flow_conflict_lite, dropped) · **NVDA** (flow_conflict -3, cum-flow -386M opposes bullish multileg) · GOOGL/GOOG/COST/MSFT (mega-tier DP selling) · LRCX/SEDG/ADI (ADI = PCE hedge, not a fade) · CVS (COVERED_CALL).
