# Daily Market Analysis — 2026-07-28

## Executive Summary

- **Regime + GEX state:** `TRANSITIONAL / CHOPPY`. SPY 740.86, **below both its 20SMA (746.65) and 50SMA (744.86)**, −2.57% from the 90d high. VIX 18.21. **SPY and QQQ are both FULLY_NEGATIVE short-gamma** (total GEX −$947M / −$1,077M); QQQ has **no call wall at all** in the visible book. Price breadth 70.97% green — but **options-flow breadth is only 36.9% bullish**. Sector lean: healthcare/staples/financials **in**, AI-semis violently **out**.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL/CHOPPY) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** SPY short-gamma · ZGL `null`/unreliable · no clean call wall (741 nominal, real resistance 748/760) · put wall 735 → trend/breakout, not pin. QQQ short-gamma · ZGL `null` · **no call wall** · put wall 675 (at spot) → the more dangerous book. Advisory, see §2.
- **Top swing build:** **NONE.** No name survived the gate stack.
- **Top LEAP candidate:** **NONE.** Zero candidates reached 6-of-9 gates.
- **Biggest risk:** **FOMC decision + Chair Warsh press conference tomorrow, 2026-07-29, 2:00/2:30pm ET**, into sticky core PCE (3.41% YoY) and a 10Y at 4.65% (+27bp/30d) — a hawkish-risk setup landing on a short-gamma index book. Secondary: the entire semis candidate set is **one position** (AMAT/KLAC 0.916, SNDK/MU 0.904, KLAC/SMH 0.906).

> **The board is empty. Zero sized calls. This is the 20th consecutive empty conviction board, and it is the intended output of the gate stack, not a failure of it.** The most recent audit (2026-07-25) measured the DROP pile at **0.431** against a sized book at **0.402 (LOW)** and **0.143 (HIGH)** — the names this system refuses have outperformed the names it grades tradeable for four consecutive audits.

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — mixed signals, reduce position size, wait for clarity.** Trend **CHOPPY**. SPY 740.86, below both moving averages, +1.63% over 30d but −2.57% from the 90d high. Flow breadth **2,320 bullish vs 3,959 bearish tickers (36.9%)** of 6,279 with options.

**The tape framing is the single most important read of the day, and the headline number is misleading.** Measured OHLCV (`scripts/market_data.py --as-of 2026-07-28`):

```
RSP +1.17%   >   SPY +0.24%   >   QQQ −0.97%        XLK −1.84%   SMH −3.45%   SOXL −14.52%
```

Equal-weight beat cap-weight by 93bp. This was **not a broad rally** — it was a violent AI/semis de-rating inside a green-breadth rotation.

| Down (1d) | | Up (1d) — the rotation destination | |
|---|---|---|---|
| SNDK | −14.25% | KNSA | +25.03% |
| GLW | −12.10% | CLS | +10.04% |
| BE | −11.34% | INCY | +9.30% |
| NBIS | −9.68% | THC | +7.92% |
| TSEM | −9.46% | GLOB | +7.57% |
| MU | −8.85% | SOLV | +7.08% |
| AMAT / GFS | −7.82% | BKNG | +6.70% |
| WDC | −6.91% | HPQ | +6.55% |
| KLAC | −6.18% | IBM | +5.21% |
| PLTR | −6.08% | KO | +5.00% |

Five-day damage in the complex: SNDK −31.04, SOXL −30.91, BE −26.26, GLW −22.41, NBIS −21.77, TSEM −19.10, TSLA −18.87, INTC −18.16, GFS −17.46, AMAT −15.60, MU/WDC −15.48, CRWV −15.43, SMH −9.33. **This is week 2 of the de-rating.**

**Per-index gamma (current-state EOD book; §2 carries the forward read):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 740.95 | `null` (unreliable) | −$947.1M | FULLY_NEGATIVE | none clean (741 nominal; 748 / 760 real) | 735 |
| QQQ | 675.97 | `null` (unreliable) | −$1,076.6M | FULLY_NEGATIVE | **NONE** | 675 (at spot) |
| IWM | — | `null` (unreliable) | negative all 10 sessions | negative | — | — |

**`uw options-flow dte-volume-share`:** 0DTE 30.5% · weeklies 30.7% · monthlies 20.7% · LEAPs 3.3% → `regime_hint: BALANCED`. Neither retail-dominated (0DTE < 50%) nor institutionally tilted; no uniform conviction adjustment applied.

**`uw historical vrp`:** SPY **FAIR** (iv30 0.1534 vs realised 0.1258, vrp +0.0277) · QQQ **FAIR** (0.2617 vs 0.2562, +0.0055). No index-level premium edge in either direction — every vol call below had to stand on single-name structure.

**Macro backdrop** (`scripts/fred_macro.py`): yield curve **normal** (10Y−2Y +0.35) · core CPI **2.81%** YoY · core PCE **3.41%** YoY (sticky) · unemployment 4.2% · payrolls +57k MoM · 10Y **4.65%, rising +27bp/30d** · broad USD **weakening** · fed funds effective 3.63%. **Sticky core PCE with a rising long end into an FOMC is a hawkish-risk configuration.**

**Forward `event_risk`:**

| Date | Event | Impact |
|---|---|---|
| **2026-07-29 (T+1)** | **FOMC decision 2:00pm ET + Chair Warsh presser 2:30pm ET** | **HIGH** |
| 2026-07-30 | Initial jobless claims | LOW/MED |
| 2026-07-31 (T+3) | PCE (June) | HIGH |
| 2026-08-07 | Nonfarm payrolls (July) | HIGH |
| ~2026-08-12 | CPI (July) | HIGH |

The book is buying that protection: the **08-07 (NFP) expiry carries $1.18B in puts vs $717M in calls**; 07-31 (PCE) $2.50B puts vs $1.98B calls.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, prose-only, 0 rubric points, no backtested predictive claim.** Predictive validation of these levels lives in `/weekly-analysis` §2 (`scripts/gex_next_session_backtest.py`), not here. Scope is SPY and QQQ only.

### SPY — short-gamma, no clean ceiling
`spot 740.95 · zero_gamma_level null (zgl_reliable: false) · total_gex −$947,116,699 · regime FULLY_NEGATIVE`
Dealers are net short gamma across essentially the whole 716–765 strike grid. The nominal max-positive strike is 741 (+$72.1M) — 0.01% above spot, i.e. **noise, not a gate**. Real resistance clusters at **748 (+$69.4M)** and **760 (+$64.3M)**; the put wall is **735 (−$141.8M, −0.80%)**.
**Structure bias:** trend/breakout, not pin. Moves through 735 down or 748/760 up get *amplified* by hedging, not dampened. Favour debit verticals / defined-risk directional 0DTE. **Avoid naked short premium at the money.**

### QQQ — the more dangerous book
`spot 675.97 · zero_gamma_level null (zgl_reliable: false) · total_gex −$1,076,555,000 · regime FULLY_NEGATIVE`
Deeper negative than SPY and cleaner — essentially **no positive GEX anywhere** in the 651–700 grid (only sub-$6M ATM noise). **There is no call wall**, so dealer hedging will not lean against an upside squeeze. The put cluster at **675 sits on top of spot**, with a second pocket at 680 (−$130.4M) and 660 (−$72.7M).
**Structure bias:** debit verticals or long straddle/strangle. **Explicitly avoid iron flies/condors — there is no wall discipline to anchor them to.**

**Mandatory caveats:**
1. **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and re-computes the ZGL/walls.
2. **ZGL is unreliable on both names** (`null` on FULLY_NEGATIVE). Reads fall back to `total_gex` sign + spot-vs-wall. This is structural, not a one-off: `gex-time-series` logged SPY's 07-16 flip with `zero_gamma_level: 360.62` against a ~740 spot, and IWM rows labelled `regime: POSITIVE` while carrying **negative** `total_gex`. **The `regime`/`zero_gamma_level` fields of that tool are broken** — confirmed today on AMAT, WDC, INTC, IBM, ADBE and NOW as well.
3. **Gap risk voids this prior outright.** FOMC 2:00pm + presser 2:30pm tomorrow is a scheduled repricing event *inside* the session this book describes. A negative-gamma book walking into a Fed decision is close to worst-case for prior stability.
4. **Tooling limit:** `gex --dte-max 1` errors, so uw cannot isolate the D+1 expiry. This is the standing 0–45 DTE book as proxy. (The 07-29 expiry does carry real weight — ~$2.43B premium, vs 07-31 ~$4.48B.)
5. **This is the SPY/QQQ ETF gamma book**, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — the validated stack)

The GEX walls above are a **map, not a pin** — wall-as-magnet backtested NO_GO, as did every directional 0DTE signal. What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, and explicitly **not a guaranteed edge**.

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` / VIX | HIGH / 18.21 | HIGH / 18.21 |
| `implied_move_pct` | 1.23% | 2.14% |
| `expected_range_pct` | 1.19% | 1.99% |
| `size_scalar` | 1.50 | **0.75** |
| `suggested_structure` | wider iron condor, wings ≈ ±1.19% (short-gamma → wider/trendier) — or reduce/stand aside | wider iron condor, wings ≈ ±1.99% — or reduce/stand aside |
| `stand_aside_reason` | null | null |
| `caution` | null | **Front-end backwardation (0DTE IV 1.86× VIX) — event/gap risk; half size** |
| Backtest verdict | GO_PREMIUM_SELL_INTRADAY (n=60) | GO_PREMIUM_SELL_INTRADAY (n=60) |
| `mean_pnl_open_pct` (**GROSS**) | +0.258% | +0.380% |
| **`mean_pnl_open_net_pct`** | **+0.158%** | **+0.280%** |
| Worst day | −1.40% | −2.453% |

**`pnl_basis`: percent-of-underlying-spot-notional, GROSS of costs** — *not* premium-collected, *not* margin-relative. Lead with the net figure: **+0.158% (SPY) / +0.280% (QQQ)** after the assumed 0.10% round-trip. Vilkov (2024) found an unconditional 0DTE condor flips to negative net Sharpe once costs are charged, so the 91.7%/86.7% gross win-rates overstate a negatively-skewed seller's edge.

**Entry rule:** enter at/after the open once the gap resolves; **hold to the close; never carry overnight** (overnight entry backtested +0.06% SPY / **−0.073% QQQ**). If it gaps beyond the wings, stand aside.

⚠ **Two live tensions to weigh before putting this on tomorrow.** First, both index books are **short-gamma**, which argues for wider wings or standing aside — the script's own structure string says exactly that. Second, and more important: **this is an FOMC day.** The validation sample contains **no vol shock**, so the short-vol left tail is **UNSAMPLED**. Selling premium into a Fed decision on a short-gamma book is precisely the untested regime. **SPY ≈ SPX** (validated identical); **QQQ is weaker** (Nasdaq index book unavailable) and additionally flagged for front-end backwardation.

**Promotion bar:** this lane stays advisory / 0 rubric points **permanently** until BOTH a vol-shock day enters the sample AND **net** expectancy clears a tail-aware bar. Win-rate is explicitly not the promotion metric.

---

## 2b. Swing Dealer Positioning (1–4 weeks)

**Zero names qualify for the +1 mechanized DEX-flip line today, and zero vanna squeezes fire.** Both are clean, mechanically-derived negatives.

**The DEX flip that matters already happened — on 2026-07-24.** `scripts/dex_flip.py` over 14 dated sessions confirms a genuinely **synchronized, sector-wide** flip on that date:

| Ticker | Evidence (verbatim from `dex_flip.py`) | Whipsaw |
|---|---|---|
| MU | `07-23 +4,958,363,698 → 07-24 −4,056,289,162; prior 3 sessions positive; |flip| 4.06B vs floor 1.22B` | false |
| NBIS | `07-23 +1,344,132,751 → 07-24 −587,475,340; |flip| 587M vs floor 226M` | **true** (4 sign changes) |
| AMAT | `07-23 +41,008,378 → 07-24 −358,443,941; |flip| 358M vs floor 93M` | false |
| WDC | `07-23 +376,179,240 → 07-24 −109,161,890; |flip| 109M vs floor 83M` | false |
| INTC | `07-23 +585,195,650 → 07-24 −863,783,812; prior 5 sessions positive; |flip| 864M vs floor 136M` | false |

All five are now **4 sessions past the flip**, so the latest session shares sign with its priors and `qualifies=false`. **This is the discipline working, not a scoring bug** — a stale flip is a level, and levels are beta. `gex-time-series` independently confirms the same 07-24 turn on `total_gex` sign for all five, holding negative and **deepening** into today's print; per-strike GEX confirms it is not a single-strike artifact.

**Vanna:** every put-heavy book (SPY, QQQ, IWM, MU, NBIS, AMAT, WDC, INTC, KLAC, PLTR) reads **"vanna pressure, not squeeze"** — the falling-VIX leg fails. Dated ^VIX: **07-24 18.58 → 07-27 18.67 → 07-28 18.21** is a whipsaw, not a ≥3-session decline.

**Index swing bias:** SPY NEUTRAL/bearish-lean (DEX −26.08B, negative since 07-17, easing; front-end IV 1.023 = no panic). QQQ NEUTRAL/bearish-lean, **more urgent** (DEX −47.84B re-deepening today; **front-end IV 1.092 = confirmed front panic**). IWM NEUTRAL — dealer flow and price are in tension (DEX negative, but the equal-weight rotation bid is lifting it).

**Front-end IV panic readings** (`--near-dte 7`, never the default 1): **BE 1.345 · SNDK 1.364 · TSLA 1.280 · AMAT 1.270 · WDC 1.250 · QQQ 1.092 · NBIS 1.089 · MU 1.070 · INTC 1.034 · SPY 1.023 · IBM 0.993.**
⚠ **KLAC reads 1.000 — this is `NO_NEAR_TENOR` degenerate, not "calm."** `near_dte_actual == far_dte_actual == 24`; there is no near-dated tenor to measure.

**Rotation destinations:** **IBM is the best-confirmed swing long in the book** — DEX +541.6M (a 5× jump off +101.8M on 07-27), DEX **and** GEX both flipped NEGATIVE→POSITIVE on 07-24 and held 3 sessions, front-end IV **0.993 = calm** (i.e. not chasing an already-panicked tape, unlike NOW at 1.096). Its 07-24 DEX sign-change **failed the magnitude floor at the time** (|103,596,360| < 167,927,920, ratio 0.62) — a near-miss that never qualified, which matters for §7.

**PLTR** carries the most extreme front-end panic in the universe (**1.331**) but its `total_gex` shows only a **single-day** negative print on 07-24 sandwiched between positive sessions — the explicit single-day-flip disqualifier. No swing thesis.

---

## 2c. Sector Rotation

**Rotation regime call: `cyclical→defensive`, confidence MEDIUM.** But the honest read is that today is **two overlapping stories the GICS aggregate cannot separate**:

1. **A genuine, multi-day defensive bid** — Healthcare (+$206.0M, persistence 1.0), Consumer Defensive (+$112.5M, 1.0), partially Financials (+$167.0M, 1.0). XLV +2.36%, XLP +1.99% confirm on price, and the `fz` new-high/RS list is dominated by healthcare/defensives (KNSA, INCY, THC, LH, GEHC, UHS, KO, PM, ALL, GM, PCAR, LTH, RLI). **This side is fully confirmed across three independent lineages.**
2. **An AI/semis growth de-rating that GICS reports as bullish.**

> ⚠ **Known tool defect, reconfirmed three times today.** `uw options-flow sector-flow-persistence` `net_flow` is **gross call$ − put$ and sign-agnostic with respect to aggressor.** It scores **Technology `1.0 INFLOW`** on a day XLK fell 1.84% and SMH fell 3.45% — the "inflow" is +$34.2M net on **$7.11B call / $7.08B put gross**, i.e. churn. The same defect hits **Energy** (`1.0 INFLOW` vs XLE −1.35% price and −$29.1M ETF flow) and inflates Comm Services. **Do not read rotation direction off persistence alone.**

The **≥0.6 persistence gate is non-binding again**: 7 of 11 sectors sit at 1.0 and the other 4 at 0.8, so every sector clears and the gate discriminates nothing. A market-relative bar (top-third persistence AND signed magnitude above the $48.09M cross-sector median) was applied instead.

**ETF flow tape (advisory — instrument-level layer the GICS aggregates cannot see):**

| ETF | Net premium dir | 5d net flow | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|---|
| **IGV** | inflow | **+$18.0M** | BULLISH | 67% above-mid ($58.0M) | **+$34.7M call-over-put** | n/a (Tech aggregate contaminated) | NOW, ADBE, INTU, CRWD, RNG, PCOR |
| XLY | inflow (weak) | +$8.8M | BULLISH | 53% below-mid | weak, put-dominant | disagree | RCL (long), TSLA (short) |
| **XLV** | inflow | +$2.9M | BULLISH | 52% above-mid ($302.6M) | sweeps **100% call** | **agree** | GEHC, UHS |
| XLP | inflow | +$1.1M | BULLISH | — | — | **agree** | LW, KVUE |
| XLI | outflow | −$1.7M | BEARISH | — | — | **agree** | BE, HWM |
| XLC | outflow | −$2.4M | BEARISH | — | — | **disagree** → watch-only | GOOGL |
| KRE | outflow | −$2.2M | BEARISH | — | — | disagree (regionals ≠ insurers) | — |
| EWY | outflow | −$10.6M | MIXED | 74% above-mid (creation/hedging, **not** accumulation) | −$5.8M put-over-call | n/a | Korea/memory de-risk |
| **XLE** | outflow | **−$29.1M** | BEARISH | 60% below-mid | −$3.3M put-over-call | **disagree** (3rd defect instance) | — |
| **SMH** | **outflow** | **−$42.3M (largest)** | MIXED label, but DP+sweeps+price unambiguously bearish | **71% below-mid on $778.8M** (largest DP print in the scan) | **−$55.1M put-over-call** | **disagree** — the defect's clearest illustration | SNDK, BE, GLW, NBIS, INTC, MU, WDC, AMAT |

**The headline the GICS layer misses entirely: a software/semis split inside "Technology."** IGV is a genuine bullish pocket (+$18.0M, 67% above-mid DP, sweeps +$34.7M call-over-put) while SMH is the clearest de-risking signal on the tape. The price tape agrees — NOW +4.79, ADBE +4.81, INTU +2.99, RNG +6.01, PCOR +4.85 against SMH −3.45.

**Scored sector-leader +1 (all three sub-conditions):** only **TSLA** (−$650.2M) and **BE** (−$214.7M) clear. **Both are shorts.** Every long leader fails condition (c): GEHC +$2.97M, UHS +$1.14M, KVUE +$1.31M, THC +$4.2M, KNSA +$0.6M, RCL +$29.2M — all under the $50M bar. LW is *MIXED* (−$0.29M) and INCY is outright misaligned (−$1.1M bearish). The rotation is real on price and breadth but **has not yet accreted enough options premium to score.**

---

## 3. Swing Setups (1–6 weeks)

### **EMPTY — no name survived the gate stack.**

Three names cleared the quant's LOW floor. All three died in Phase 2:

| Ticker | Dir | Score | Tier | Pre-risk | Kill mechanism | Final |
|---|---|---|---|---|---|---|
| **BE** | short | 4 | LOW | starter | **Fundamentals VETO** — reported AH *today*: 165% revenue surge, first GAAP profit, **raised 2026 guidance**; JPM PT $267→$346 | **watch-only** |
| **SNDK** | long | 4 | LOW | starter | VRP −1 · panic −1 (1.364) · fundamentals CAUTION −1 (MSPR −100.0) · debate −1 (bear 0.45 ≥ bull 0.25) | **skip** |
| **TSLA** | short | 3 | LOW | starter | panic −1 (1.280) · event_risk −1 (FOMC T+1, PCE T+3) · debate −1 (bear 0.45 ≥ bull 0.35) | **skip** |

**BE is the cleanest catch of the run.** A short scored at raw-4 — the top of the book — hours before the company delivered a blowout print with raised guidance. Two independent mechanisms caught it: `fundamentals-gate` (VETO) and the debate's bull residual (0.65, the only bull to prevail today). It also retroactively explains `sweep-tracker`'s dissent — BE showed the **only genuine multi-exchange ask-side call sweep in the entire book** (2,059 trades on the 8/21 230C, 197 on the 9/18 370C), which reads as informed positioning ahead of a real beat rather than noise. BE's 10-day slide from 239.38 → 166.84 (−30%) was the market pricing a guide-down that did not arrive.

**3a. Long swings (regime-aligned):** none. `accumulation-hunter` flagged **zero** names — no ticker met the ≥3-aligned-signal bar with `institutional-accumulation` confirming.

**3b. Short / fade swings (defined risk only):** none. `contrarian-scanner` returned **zero** qualifying fades, and critically **no `BULLISH_EXTREME` z-score exists anywhere in the candidate set**, so the −2 overcrowded-long line was unclaimable on every name.

**Invalidation discipline (C34):** not applicable — no positions. The one usable dark-pool level set produced today was NBIS: **$165.16 ($52.4M) · $169.38 ($40.65M) · $171.26 ($38.3M) · $168.50 ($36.8M) · $164.99 ($20.9M)**, a defended zone of roughly **$165–171**. Recorded for journaling.

### Sweep ledger (informational — 0 rubric points)

`sweep-tracker` ranks persistence-first. Only two names showed genuine sweep character: **AMD** (5-of-5 bearish persistence, $1.50B 5d cum, genuine two-way ask/bid across strikes 31–234 DTE) and **BE** (3-of-5, the ask-side call sweep above). **INTC** carries a contradiction worth flagging: the persistence tool tags it bearish 5-of-5, but today's actual sweep tape is **100% call**, concentrated at 72/73 strike expiring tomorrow — that reads as 1DTE gamma scalping around the Fed, not a thesis. **SMH and NBIS both broke their prior bullish persistence tags** — today's tape is put-heavy on both.

Mega-cap/index sweeps are all **hedge signatures** and were demoted: SPY bearish 5/5 but cum_flow_30d differs by 2.6%; QQQ by 0.03%; TSLA by 0.02%; NVDA by 0.66%. Dead-flat two-sided churn carries no directional claim.

---

## 4. LEAP Builds (6–24 months)

### **EMPTY — zero candidates reached the 6-of-9 gate bar.**

This is the expected outcome on a day when LEAPs were **3.3% of volume**, and the data confirms it decisively rather than marginally.

- **Gate 2 (`oi biggest-increases --min-dte 180`):** the market-wide top-20 contained **zero** names from either target list (top slots: IEF, XLE, MARA, LBTYA, TLT, XLF, WOLF, WBD). Per-symbol queries across 26 tickers found every DTE>180 "increase" trivial (54–2,504 contracts against multi-billion-dollar underlyings), frequently **put-side and bid-dominant** — i.e. writing into the bid, not aggressive buying. Examples: AMAT 960C `oi_diff=127` with ask 42 / bid 223; IBM 210P `oi_diff=707` with ask 4 / bid 753.
- **Gate 3 (`position-rolls`):** `rolls_detected: 0` on **every single name checked** (15 names). No forward rolls, no backward rolls, no thesis extension anywhere.
- **Gate 4 (`cumulative-premium-flow` 90d, the accretion gate):** the discriminator, and it is unambiguous — bullish and bearish legs sit within single-digit percent of each other on every name. **MU: $100.57B bullish vs $100.25B bearish.** That is two-sided churn, not slow directional accretion.
- **Gate 8 (`conviction-matrix`):** not one name cleared 70. Best readings were GEHC **25** and IBM **16.2**. **AMAT returned `DISTRIBUTION` (12.9)** and **PLTR returned `COVERED_CALL` (14.1)** — both explicit disqualifiers independent of gate count.

**Near-miss disqualifications:** **GEHC** (~3/9) had the cleanest dark-pool print in the set — ACCUMULATION, buy/sell 1.72, $31.8M premium, a clustered $12.5M block at $64.11 — but trivial fresh LEAP OI (54–156 contracts), zero rolls, and only $2.97M of 30d accretion on an ~$85B name. **IBM** (~3/9) showed real size ($527M DP premium, $102M cluster) but its 30d flow flips to MIXED and its fresh OI is trivial and put-side.

> **Method note carried forward:** `uw historical oi-trend --days 10` returned **BUILDING on 13-of-13** names (`consecutive_build_days` 42–75). Critically, **the tool is not DTE-filtered** — it aggregates OI across all expiries, and today's tape was 61% 0DTE+weekly, so headline figures like MU 1.57M and INTC 1.56M contracts are almost entirely short-dated churn, not LEAP-tenor build.

---

## 5. Volatility Surface

**The dispersion is the story.** Index realized vol is compressed to single digits while the AI complex realizes 60–190%:

```
SPY rv20 9.5   RSP 9.3   IWM 11.0   XLF 14.1
   vs
SOXL 170.6   SNDK 141.9   NBIS 138.1   BE 123.3   IBM 108.6*   WDC 95.3
TSEM 93.9   CRWV 91.9   GLW 86.4   MU 85.9   KLAC 81.5   INTC 78.6   AMAT 73.6
```
\* IBM's 108.6 is a backward-window artifact — see disqualifiers.

**MANDATORY substrate hygiene was run** (`scripts/term_structure_hygiene.py`, `min_contracts=15`, `--near-dte 7`) over 18 names. **Raw `iv-term-structure` said BACKWARDATION on 17 of 18. After dropping the 0DTE/expired bucket and sub-15-contract tenors, 9 flipped.** Post-hygiene: 9 BACKWARDATION, 6 KINKED, **3 `NO_NEAR_TENOR`**.

| Ticker | raw → shape (base) | kink DTE / prom% | ivpz (PROVISIONAL) | VRP | FEIR | Attribution |
|---|---|---|---|---|---|---|
| SNDK | BACKWARD (BACKWARD) | — | 91.9 / 1.67 | **−0.0997 BUY** | 1.275 | own earnings 08-05 |
| GLW | BACKWARD (BACKWARD) | 24d 4.5% sub-thresh | 70.3 / 0.40 | **−0.2894 BUY** | 1.164 | complex sympathy |
| BE | BACKWARD (BACKWARD) | — | 85.1 / 1.57 | **+0.2723 SELL** | **1.345** | unresolved at scan time |
| NBIS | BACKWARD (BACKWARD) | — | 91.9 / 1.91 | **+0.2714 SELL** | 1.089 | own earnings 08-06 |
| **MU** | BACKWARD → **KINKED** (FLAT) *flipped* | **08-07 / 23.5%** | 48.7 / 0.37 | **−0.1308 BUY** | 1.039 | **macro — NFP 08-07, NOT MU earnings** |
| WDC | BACKWARD (BACKWARD) | — | 82.4 / 1.36 | −0.0681 BUY (weak) | 1.250 | own earnings 08-05 |
| CRWV | BACKWARD → KINKED (BACKWARD) | 08-14 / 6.1% | 100 / 2.60 | **+0.2646 SELL** | 1.009 | own earnings 08-11 |
| TSEM | BACKWARD → KINKED (**CONTANGO**) *flipped* | 08-07 / 5.8% | 91.9 / 1.49 | +0.1081 SELL | 1.308 | own earnings 08-04; **thin backend, 2 tenors dropped** |
| QCOM | BACKWARD → KINKED (BACKWARD) | 09-18 / 10.8% | 39.2 / 0.13 | +0.1549 SELL | 1.256 | **earnings TOMORROW**; Sep kink = monthly-OPEX gravity |
| TSLA | BACKWARD → KINKED (BACKWARD) | 08-05 16.1% & 08-14 9.7% | 59.5 / 0.47 | **−0.1838 BUY** | 0.97 | **macro — FOMC/NFP + sympathy** |
| SMH | BACKWARD → KINKED (FLAT) *flipped* | 08-07 / 14.3% | 90.5 / 1.21 | 0.0228 FAIR | 0.978 | **dispersion aggregation** — constituent earnings |
| **GFS · KLAC · NXPI** | **`NO_NEAR_TENOR`** | — | 100/94.6/93.2 | — | **unmeasurable** | **data gap — no listed expiry ≤21 DTE** |

⚠ **`NO_NEAR_TENOR` is not `FLAT`.** GFS, KLAC and NXPI have no surviving tenor at or under 21 DTE — their `front_end_ratio: 1.000` means **"no data," never "calm."** `min_contracts` (default 15) is a **named, tunable parameter, NOT audit-frozen.**

**Calendar candidates:** none qualify. Only a single snapshot of `front-end-iv-ratio` was available, so "ratio falling" could not be confirmed for any name, and the disqualifier ("BACKWARDATION with ratio > 1.10 and *rising* — event still pending, don't fade") applies conservatively. **BE** (FEIR 1.345, VRP +0.2723, no scheduled catalyst *at scan time*) was the closest to a pure calendar — and the fundamentals gate subsequently revealed exactly why the front end was bid.

**Disqualifiers applied:** **IBM excluded despite the largest VRP magnitude in the set (−0.4325)** — iv30 42.4% vs realized 85.7% is **backward-window contamination**, driven by the already-resolved +5.21% move sitting inside the trailing window. Forward FEIR is 0.993 (flat) — post-event settling, not cheap forward vol. **AMAT/KLAC/INTC/SMH/SOXL** disqualified on VRP FAIR.

**IV outliers:** no matches in the target complex. The cached top-20 is dominated by **same-day-expiry contracts at 2,000–7,000% IV** (QQQ 07-28 C495 at 5,349%) — the identical 0DTE-bucket artifact the hygiene module exists to strip. Unusable.

**Data-quality flag:** `uw historical iv-percentile-zscore` returned `dates_used: 74` on **all 18 names** — short of both the 252 requested and the 120-day first-class floor. **Every percentile and z-score above is PROVISIONAL.**

---

## 6. Risk & Correlation

**Macro headline:** core PCE **3.41%** YoY sticky, 10Y **4.65% rising +27bp/30d**, USD weakening, curve normal +0.35, fed funds 3.63%. **FOMC T+1, PCE T+3** — two Tier-1 binaries inside every swing horizon on this board.

**Correlation — one cluster, and it is the whole book.** `uw risk portfolio-correlation` on today's actual candidates:

```
AMAT/KLAC 0.916   KLAC/SMH 0.906   SNDK/MU 0.904   SNDK/SMH 0.875
AMAT/MU   0.865   AMAT/SMH 0.864   MU/SMH   0.856   SNDK/AMAT 0.850
SNDK/KLAC 0.794   KLAC/MU  0.791
soft watch: BE/SMH 0.687 · BE/NBIS 0.623 · NBIS/SMH 0.623
```
**MU, SNDK, AMAT, KLAC, SMH, NBIS, WDC, BE are effectively ONE position.** A structural oddity worth recording: **BE (short) and SNDK (long) are 0.687-linked members of the same complex on opposite directional axes** — had both sized, they would have been one contested cluster bet, not two positions. Moot post-gate. TSLA and IBM show no pair ≥0.60 against this set.

**Gates applied:** the panic gate is **hot across the entire tradeable set** — BE 1.345, SNDK 1.364, TSLA 1.280, AMAT 1.270, WDC 1.250, MU 1.070. Everything tradeable is in front-end backwardation. VRP is FAIR at index level, so no vol tailwind; single-name VRP in the AI complex is **negative** (SNDK −0.0997 against realized 141.9), which is why SNDK's Jan-27 **credit** spread drew a −1: it is short vol into negative VRP.

**Fundamentals verdicts (top 5):**

| Name | Verdict | Adj | The contradicting/confirming fact |
|---|---|---|---|
| **BE** | **VETO** | veto | Reported AH today: 165% revenue surge, first GAAP profit, raised 2026 guidance, JPM PT $267→$346 |
| SNDK | CAUTION | −1 | Insider MSPR **−100.0** 3mo avg, near −100 nearly every month since early 2025, through a ~20× run |
| TSLA | CONFIRM | 0 | eps_growth **−37.66%** vs revenue +11.75% on a **319× PE**; −36.43% miss; MSPR −45.35 |
| IBM | CONFIRM | 0 | eps_growth +82.66%, PE 19.8×, Open Secure AI Alliance catalyst 07-27 |
| WDC | CAUTION | −1 | Insider MSPR **−97.4** sustained 12+ months; China CXMT memory-pricing risk |

**Event-risk flags:** BE own earnings T+0 (delivered) · SNDK and WDC earnings 2026-08-05 (T+6) · FOMC T+1 and PCE T+3 on everything. SNDK's event gate was a **no-op** — its scored structure is a defined-risk Jan-2027 credit spread capped at $7.9M, and its own earnings fall outside the T+5 window.

**Debate-disconfirmation cuts — the gate fired on 4 of 5:**

| Ticker | bull | bear | Verdict |
|---|---|---|---|
| BE | **0.65** | 0.35 | no cut — and on a *short*, a prevailing bull **corroborates the VETO** |
| SNDK | 0.25 | **0.45** | **CUT** — `BOTH_SIDES_LOW`, neither advocate cleared a coin flip |
| TSLA | 0.35 | **0.45** | **CUT** — `BOTH_SIDES_LOW` |
| IBM | 0.35 | **0.75** | **CUT**, largest margin in the book |
| WDC | 0.35 | **0.45** | **CUT** |

The IBM debate produced the sharpest single finding of Phase 2: the bear demonstrated that the bull's headline evidence — a **"$102M dark-pool cluster at $227.55"** — is the *same* 20:00Z closing-cross print tagged `extended_hours_trade`, and that IBM's 07-24 DEX flip **never cleared its magnitude floor in the first place** (ratio 0.62 against the 1.0 bar). Two of the bull's three "independent" lanes dissolved on inspection.

**Breadth cross-check (`fz`, advisory, 0 points):** 357 advancers / 145 decliners / 1 unchanged of 503; `pct_green` **70.97%**; avg +1.06%, median +1.39%; top IQV +13.94%, worst SNDK −14.25%. **No `divergence_flag`** (index green AND pct_green > 50). But the *inverse* divergence is the day's real tell: **price breadth 70.97% green against options-flow breadth 36.9% bullish** — the tape is green while the options tape is defensive.

**Adverse-flow exit list:** **none.** `uw watchlist alerts` and `uw watchlist scan` against `conviction_2026-07-27` both return **empty** — yesterday's board was also empty and correctly wrote nothing. No carried positions, no exits.

**Hedge sleeve:** **not required.** The post-gate book is empty — net delta zero, nothing to hedge.

**`watchlist_write_back_confirmation`: NOTHING WRITTEN.** No name survived at LOW tier or better (BE = VETO/watch-only; SNDK, TSLA = skip; all others quant DROP). Per the corrected 2026-07-23 rule, DROP/skip names are **never** persisted — they poison tomorrow's correlation loop. `conviction_2026-07-28` does not exist, and that is the intended outcome.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

### **EMPTY — zero names reached raw_score 7.** Board: **3 LOW · 0 MEDIUM · 0 HIGH.**

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`, from `/calibration-audit` 2026-07-25 `phase_3_calibration`:

| Tier | n | Realised WR | Mean P&L | Payoff ratio | Half-Kelly |
|---|---|---|---|---|---|
| HIGH | 7 | **0.143** | −2.441 | 0.720 | 0.0 |
| MEDIUM | 19 | 0.526 | +0.104 | 0.948 | 0.0132 |
| LOW | 87 | 0.402 | −0.874 | **1.170** | 0.0 |
| **DROP** | **327** | **0.431** | −2.190 | 0.871 | 0.0 |

**Fourth consecutive audit with `HIGH < LOW`, and DROP (0.431) beats LOW (0.402).** The names the system refuses have outperformed the names it grades tradeable. All 7 HIGH calls are pre-freeze; the frozen rubric has produced none. This is the empirical backdrop against which today's empty board should be read.

**The three LOW rows, full audit trail** (none sized; shown because there is nothing above them):

| | **BE** | **SNDK** | **TSLA** |
|---|---|---|---|
| Direction / horizon | short / swing | long / swing | short / swing |
| `raw_score` | **4** | **4** | **3** |
| `score_components[]` | +1 sector-leader (`sector-rotation-strategist` / `sector-flow-persistence`) · +1 vol-surface (`vol-surface-scout` / `term-skew`) · +1 cum-flow accretion (`cumulative-premium-flow`) · +1 oi-trend BUILDING (`historical oi-trend`) | +2 multileg (`multileg-strategist` / `hot-chains multileg`) · +1 vol-surface · +1 oi-trend · **+0 cum-flow — intent screen FAIL** | +1 sector-leader · +1 cum-flow accretion · +1 oi-trend |
| `dominant_signal_class` | `sector_rotation` | `multileg_directional` | `sector_rotation` |
| `confluence_score` | null | null | null |
| `cum_premium_flow_30d / 90d` | −$214.7M / −$492.6M | +$777.1M / +$2,397.0M | −$650.2M / +$9.7M |
| `win_rate` (n, source) | null (—, **`NA(substrate)`**) | null (—, `NA(substrate)`) | null (—, `NA(substrate)`) |
| `market_excess` | null | null | null |
| Pre-risk size | starter | starter | starter |
| `fundamentals_verdict` | **VETO** | CAUTION | CONFIRM |
| Debate {bull, bear} | {0.65, 0.35} | {0.25, 0.45} | {0.35, 0.45} |
| Gates applied | fundamentals **VETO** | vrp −1 · panic −1 · fundamentals −1 · debate −1 | panic −1 · event_risk −1 · debate −1 |
| **Final size** | **watch_only** | **skip** | **skip** |
| Invalidation | n/a — VETO'd; short re-entry carries post-beat squeeze risk | SNDK < 1079 at Jan-2027 (breakeven; 1.7% cushion vs rv20 141.9) | net_dex turns and holds positive ≥3 sessions, or FOMC relief squeeze |

**Why `win_rate` is null on every row:** the quarantined `uw historical signal-backtest` supports only `bullish_flow | bearish_flow | high_iv_rank | volume_spike | dark_pool_accumulation`. Both surviving classes (`sector_rotation`, `multileg_directional`) are **outside that set**, so the P0.3 clean protocol structurally cannot complete → `NA(substrate)` → tier-default sizing capped at half, LOW → starter. **No headline win_rate was quoted anywhere.**

**Step 3a load-bearing gate:** no-ops (no raw ≥9). Recorded, not skipped — and it could not have passed regardless: `institutional-accumulation` returned NEUTRAL or DISTRIBUTION on every candidate and there were zero DEX flips, so at most **2 of 4** load-bearing tools were citable on any name.

**Deep-dive hand-off:** skipped — no HIGH-tier names. (`/stock-deep-dive` is reserved for the top-2 post-gate HIGH names; there are none.)

### Conviction scoring rubric (verbatim, `rubric_version: 2026-06-12`, FROZEN)

```
Daily conviction score = Σ:
  +1  MECHANIZED DEX flip or vanna-squeeze in trade direction — verified SIGN CHANGE, not a level;
      computed by scripts/dex_flip.py, never by hand. Vanna disjunct needs a dated VIX source.
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified
      institutional tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d
      confirms (sign aligned AND |cum_flow_30d| ≥ $50M); else halved to +1.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: award only
      when dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +1  cumulative-premium-flow net directional accretion (30d) — INTENT-SCREENED: no C28
      distribution_flag, and not deep-ITM sub-parity ex-div calls. Screen failed/unevaluated → 0.
  +1  sector-rotation-strategist names ticker a single-name leader — CONDITIONAL on ALL of:
      (a) persistence_score ≥ 0.6, (b) cum_flow_30d aligned, (c) |cum_flow_30d| ≥ $50M. Default 0.
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored play type)
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner overcrowded long with RISING pc-ratio-zscore (VRP positive) — an
      INFORMED-FLOW CONTINUATION penalty, not "fade the crowd" (Pan-Poteshman 2006; Ge-Lin-Pearson 2016).
  -3  flow_conflict — cum_premium_flow 30d clearly opposite dominant_signal_class (sign flip +
      magnitude > union-median |cum_flow_30d|, or explicit OPPOSITE label)
  -1  flow_conflict_lite — 30d read MIXED (signed sum near zero, or aligned but bottom-quartile)
      [-3 and -1 are mutually exclusive — apply ONE, never both]
  # TIER GATES (risk-monitor, Step 2d) — 0 points, NOT score_components:
  -1  [TIER] correlation cluster (pairwise corr ≥ 0.70)
  -3  [TIER] market-regime conflicts with trade direction
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | HIGH | full (subject to Step 3a + Step 5 win-rate gate) |
| 7–8 | MEDIUM | half (subject to Step 5) |
| 3–6 | LOW | starter / watch-only |
| ≤ 2 | drop | filtered by quant's drop floor |

**Tier-cut status:** the ≥9 HIGH cut failed its scheduled re-confirmation on 2026-06-12 and has now inverted for four consecutive audits. Cuts are retained under the P0.1 freeze but **carry no validated ranking claim**; the P0.6 out-of-regime guard caps all sizing at half in the interim.

---

## 8. Watch-only — single signal, no confluence

Listed for journaling. **NOT for trade entry.**

**Failed the ≥2-agent confluence gate (single positive agent):**

| Ticker | Sole flagging agent | Signal | Note |
|---|---|---|---|
| **SMH** | `multileg-strategist` +2 | Jan-27 650/800 call debit spread, 8,000×, **$18.8M debit**, max $120M, δ+0.204 | `sector-rotation` flags SMH **SHORT** — opposite axis. Repeat **4 sessions**; machine-confirmed #2 in market on `position-rolls` (near put OI −96,319 / far +15,392) |
| **INTC** | `multileg-strategist` +2 | **Nov-20 C70 OI 8,354 → 73,263 (+64,909 OPENING)**, δ+0.76, ~$218M | Largest OI-confirmed opening build in the dataset. Repeat **5 sessions** — but the campaign has been **chasing the stock down** (strikes 120/125/135/150 → 120/130 while spot fell ~$100 → $86.87) |
| **HPQ** | `multileg-strategist` +2 | Sep-18 P26 OI 487 → 12,203, **85% bid-side (9,023 bid vs 1,581 ask) = puts SOLD** → bull put spread, $1.46M credit, risk capped $2.16M | **The bearish confluence-5 tag is INVERTED — HPQ is LONG.** Notional only ~$2M |
| **PLTR** | `earnings-scout` +1 | **BUY VOL**, earnings 08-03, kink 08-07 (15.4% prom), clean CONTANGO base, implied move 4.07% | Genuinely clear of FOMC/PCE. Suggested: Aug-7 put-skewed strangle (120P/128C vs $123.53) |
| **AAPL** | `earnings-scout` +1 | SELL VOL (half), earnings 07-30, kink 07-31 prom 32.7%, **back-month TAIL_HEDGING** | implied move **3.23%** |
| **AMZN** | `earnings-scout` +1 | SELL VOL (half), earnings 07-30, kink 07-31 prom 14.3%, back-month flat | implied move **5.95%** |
| **SHOP** | `earnings-scout` +1 | SELL VOL (half), earnings 08-05, kink 08-07 prom 18.6% | implied move **4.07%**; ⚠ PCR 0.131 vs bearish net premium — aggressor ambiguous |
| **DDOG** | `earnings-scout` +1 | SELL VOL (half), earnings 08-06, kink 08-07 prom 15.1%, iv_rank 96.7 | implied move **5.57%** |
| **QCOM** | `vol-surface-scout` +1 | SELL VOL, VRP +0.1549, **earnings TOMORROW 07-29** | implied move **7.64%** |
| **GLW** | `vol-surface-scout` +1 | BUY VOL, **VRP −0.2894** (largest clean magnitude in the set) | no scheduled catalyst |
| **TSEM** | `vol-surface-scout` +1 | SELL VOL, VRP +0.1081, earnings 08-04 | implied move **8.66%**; thin backend |
| **CRWV** | `vol-surface-scout` +1 | SELL VOL, VRP +0.2646, earnings 08-11 | implied move **7.72%** |
| **NBIS** | vol/dealer/accum disagree | No two agents agree on a direction | DP zone $165–171; **C28 fires**: 165C −1,158 (~$4.0M) and 220C −731 (~$3.77M) institutional-size **call** OI closing |
| **MU** | vol vs dealer, opposite axes | BUY VOL (kink 08-07, **NFP macro not MU earnings**) vs SHORT lean | implied move **16.29%** |
| **IBM** | 3 lanes, but 2 dissolved | raw 2, below floor | See §6 — DP cluster is a closing-cross artifact; DEX flip never cleared its floor |
| **WDC** | dealer + multileg, raw 1 | 07-31 P540/P490 deep-ITM vertical, $10.4M debit, near-zero vega | Structure expires **before** the 08-05 print — event-matched to FOMC/PCE |
| **KLAC** | dealer + multileg, raw 0 | Aug P218 / Sep P190 diagonal, $4.5M debit, δ−0.24 | Cleanest bearish structure in the complex, but `NO_NEAR_TENOR` = unanchorable, single-session |
| **AMD** | `sweep-tracker` | 5-of-5 bearish persistence, $1.50B 5d cum, genuine two-way | Cleanest real persistent bearish name |
| **TSM** | `multileg-strategist` | Aug-21 425/450/475 call fly (11,250:22,500:11,250) + Sep 4/18 double diagonal (13,613 each) | **NEUTRAL — explicitly do not fade despite the −$35.8M bearish tag.** Kink is monthly-OPEX gravity, not an event |
| **GEHC** | `leap-radar` / sector | ACCUMULATION 1.72, $31.8M DP, $12.5M block at $64.11 | Cleanest DP print in the set; fails $50M accretion bar |

---

## Notes, artifacts and data-quality findings

**Artifacts that would have produced false calls if inherited uncritically:**

1. **SNDK +$146.4M "bullish"** = one `no_side` **$124.5M** 2027-06-17 C1020 clip (1 trade) **+ ~$41M of deep-ITM 07-31 put SALES**. `multileg-strategist` proved the mechanism **cross-session**: the 07-31 P1390/P1500 pair **opened as a matched put spread on 07-24**, then printed **bid-side in size at 19:42:28 on 07-28** at δ−0.96/−0.91. Monetizing a deep-ITM put registers as large *positive* net premium. **Hedge unwind, not conviction.**
2. **MU +$28.6M / AMAT +$28.0M** = systematic **laddered put WRITING** across 10 and 5 tenors in the last 30 minutes (~$52M / ~$29.5M collected, **uncapped**). MU sells into a back-end hump (52d 112%, 80d 122%); AMAT sells the *cheapest* tenor available (52d 95% → 80d 89%) — structurally the worse trade.
3. **GFS +$7.9M / GEV +$11.4M** = **one put-write ticket each** (GFS 7,938× Jun-27 P45; GEV 200× Dec-28 P1420). No structure at all.
4. **SPX −$2,986M "bearish"** = **53.7%** paired same-timestamp/same-size deep-ITM C7000 + P8000 **conversions/boxes**, plus a **$1.818B δ0.95 C4000** stock-replacement. **Financing, not direction.** The largest bearish number in the entire funnel carries no directional information.
5. **Closing-cross contamination is systemic, not per-name.** MU's mega-tier 0.803 buy ratio is **72% two prints** at 20:08–20:10Z tagged `extended_hours_trade` (**$2.264B on 2,759,188 shares** + $432M of $3.73B). Same for SNDK, AMZN, AAPL, SPY, IVV, QQQ, IBM, ADBE, NOW, UHS, WDC. **Use block-tier, not mega-tier** — MU block **0.442 sell-lean**, SNDK block 0.458.
6. **All five up-day "bearish confluence" tags are false positives.** HPQ is **LONG** (85% bid-side put prints = puts sold + ITM call stock replacement); BKNG's tag is manufactured by a 4-leg Dec-2028 package, **~$75.9M gross netting ~$0.3M**, delta/vega-neutral; IP is a 13-delta tail hedge six months out; ALL and GLOB are sub-$700K noise.
7. **Un-split-adjusted / non-standard strike grids** (excluded): MU 2028-12 P2110/P2390/P2470/P2480/P2500; SNDK 2028-09 P2450/P2460/P2470; WDC 08-28 & 09-04 P860. *(BKNG's 169.6 strike is a legitimate post-split adjustment — kept.)*
8. **Broken NBBO:** BE's mega print shows trade $166.84 against a quoted bid of $183.32 — a $16 gap. Unusable. `KLMN` and `FINA` in `dark-pool largest` carry `nbbo_bid = nbbo_ask = 0` — synthetic/non-standard instruments.

**Zero-discrimination signals (all fired near-universally today):**
- `+1 oi-trend BUILDING` — **13-of-13** and **16-of-16** (C47, third consecutive confirmation). Also **not DTE-filtered**, so its totals are dominated by short-dated churn.
- `LARGE_DARK_POOL` watchlist alert — fires on **~85 of 86** names.
- `iv_rank` — **20+ names at exactly 100**. No discrimination at the top.
- `sector-flow-persistence` ≥0.6 gate — all 11 sectors clear.
- `trend_direction` on `cumulative-premium-flow` — **MIXED on 9 of 9** (only IBM's 90d differed).

**Tool defects recorded:**
- **`uw insights analyst-vs-flow` returned no analyst field** on all 13 payloads — the analyst-vs-flow divergence lane was **unavailable this run**.
- **`gex-time-series` `zero_gamma_level` / `regime` fields are broken** (SPY ZGL 360.62 vs ~740 spot; IWM `POSITIVE` label on negative `total_gex`). Now confirmed on AMAT/WDC/INTC/IBM/ADBE/NOW.
- **`fz`** ticker column has systematic **first-character duplication** (IINCY=INCY, TTHC=THC, AABR=ABR) and the squeeze screen is **alphabetically truncated to A/B names** — squeeze lane unusable; RS lane de-mangled via the Company column and used advisory-only. `fz_enrich` returned `upstream_gaps: [earnings, recom, short_interest, target_price]` on all five top-5 names, so **C15–C18 remain untestable**.
- **`uw risk portfolio-correlation` takes `--symbols`, not `--tickers`.**
- **`uw screener iv-rank` takes `--mode`, not `--direction`** (flag-transfer trap from its neighbours).

**Process notes:**
- **Not OPEX week** (third Friday was 2026-07-17; next 2026-08-21) → `opex-pin-strategist` correctly not spawned. **10 Phase 1 agents ran.** The command header says "11 agents (12 in OPEX week)", but its own agent sections total 11 *including* the conditional OPEX agent — so the correct non-OPEX count is 10. Minor doc inconsistency worth fixing.
- **Step 6.5 batch-scan skipped** — `uw playbook batch-scan` operates on the raw ≥7 list, which is empty.
- **Step 0 cache:** 22 market-wide payloads fetched once (`step0_cache/`), eliminating the duplicate-fetch waste measured on 2026-07-24.
- `earnings-scout` and `vol-surface-scout` both ran `term_structure_hygiene.py`, and `earnings-scout` additionally caught that **4 of 9 hygiene-reclassified "KINKED" names have their kink at the wrong tenor** (META 17 DTE, ARM 24 DTE, COIN 52 DTE, AMD 17 DTE — none at the earnings expiry). It correctly refused the entire day-1 earnings cohort (MSFT, META, ARM, LRCX, FTNT all report **on FOMC day**, making front-end IV macro-inseparable).

**Single-leg whale scan** (advisory, **0 rubric points — permanently**; C19 CLOSED as REFUTED 2026-07-25): 446 raw signals, of which **`CLOSING_ANTISIGNAL` = 344 (77%)** — the tape was dominated by position *closing*, independently corroborating the unwind read. Tier-1: **BE** `OPENING_PUT_PRIME` $2.02M 24 DTE size/OI 3.146 · **FTNT** $1.08M · **CAT** $750K 3 DTE · **RSI**, **VRNS**, **HUM** floor blocks. A long-dated bearish AI-infra put cluster also printed: AMD 542d, VRT 871d, GEV 871d, COHR 542d, CRDO 542d.

---

*Rubric `2026-06-12` (frozen) · schema `1.3` · generated by `/daily-analysis`, 10 Phase 1 agents + 4-stage Phase 2.*
