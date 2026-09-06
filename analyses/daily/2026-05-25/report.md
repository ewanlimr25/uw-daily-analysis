# Daily Market Analysis — 2026-05-25

> **Run note (regression A/B).** 2026-05-25 is Memorial Day (US markets closed). This report runs on the latest available UW data, **2026-05-22**, and is a same-data A/B of the existing `2026-05-22.md` (prior rubric) against the **new 2026-05-25 rubric** (C11 accumulation conjunction, C12 liquidity floor, C2 market-excess + tightened N-cap). It also smoke-tests the decision-envelope emission (C1). Not a fresh tradeable call — sizing reflects the gate logic, not a live market open. The next live session is 2026-05-26.

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / UPTREND. SPY 745.64 (+5.25% 30d, above 20+50 SMA) but **breadth thin (38.1% bullish)** — a narrow, late-stage up-tape. VIX 16.7 (LOW), VRP FAIR (+0.039). 10Y 4.57% rising + USD strengthening = mild rates headwind. SPY/QQQ both freshly flipped POSITIVE-gamma on 05-22 (one session old, fragile).
- **Next-session GEX (SPY/QQQ):** SPY long-gamma, ZGL 744.70, 745 pin, call wall 750 / put wall 730 — mean-revert/pin while >744.7. QQQ long-gamma but spot *on* the ZGL (717.82), call wall 718 — fragile pin. Advisory, see §2.
- **Top swing build:** *None sized.* The highest scorer (AMD, raw 9) gated to **skip** — see below.
- **Top LEAP candidate:** *None.* Zero names cleared the 6-of-9 LEAP gate.
- **Biggest risk:** No directional book to hedge — the only surviving position is a delta-neutral PANW earnings vol leg (half).

**The one-line read:** a genuine no-edge day, and the new rubric handled it conservatively. The crowded high-scorer (AMD) was correctly cut by the very gates this rubric strengthened — the C2 market-excess gate (its 92.9% win-rate is up-tape beta, not edge), the bull/bear debate (bear ≥ bull), and the single-name VRP gate.

## 1. Regime & Gamma State
- **`risk_market_regime`:** TRANSITIONAL — UPTREND. SPY 745.64, +5.25% 30d, above 20SMA (731.58) / 50SMA (696.68), −0.52% from 90d high. Breadth weak: 2,353 bullish vs 3,818 bearish tickers (38.1% bullish) — a narrow melt-up, not broad participation.
- **Per-index gamma (EOD 05-22):** SPY spot 745.92 · ZGL 744.70 · +1.528B GEX · POSITIVE · call wall 750 / put wall 730. QQQ spot 717.85 · ZGL 717.82 · +430M GEX · POSITIVE · call wall 718 / put wall 700. Both flipped POSITIVE only on 05-22.
- **DTE share:** BALANCED (weeklies 23.8%, monthlies 17.6%, LEAP 5.7%, 0DTE n/a in EOD) — institutional/swing tenor, not retail-0DTE-dominated.
- **VRP:** FAIR (SPY IV30 0.145 vs RV30 0.106, +0.039) — no index-level vol edge. *Single-name VRP is where the edges and the gates are* (see §6).
- **Macro backdrop (FRED):** yield curve normal (+0.43), core CPI 2.99% / core PCE 3.2% YoY, unemployment 4.3%, payrolls +115k, 10Y 4.57% **rising** (+0.27 30d), USD **strengthening**, fed funds 3.62%. Forward `event_risk`: **Core PCE ~5/29**, dense late-May earnings cluster (ZS 5/26, HPQ/SNOW 5/27, DELL/OKTA 5/28, QCOM 5/29, PANW 6/2).

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> Advisory, **0 rubric points**, no backtested predictive claim. EOD prior for the 05-26 open, refreshed by fresh 0DTE OI in the first 30–60 min. SPY/QQQ only.

- **SPY** — long-gamma, ZGL **744.70** (reliable, 0.16% below spot). 745 is the gravity pin (+814M single strike). Call wall **750** (+0.55%), put wall **730** (−2.1%). Read: dealers sell rallies / buy dips around 745 → mean-revert/vol-suppress *while spot holds ≥744.7*; a clean break below drops into the 730–738 short-gamma shelf where hedging amplifies. Structure: iron fly / short straddle on the 745 pin, lower wing inside 738.
- **QQQ** — long-gamma but spot **on** the ZGL (717.82); +430M GEX (~3.5× smaller than SPY). Call wall **718** (one tick above spot), put wall **700** (−2.5%). Read: pin-to-715/718, vol-suppressed, with low-conviction downside-trend risk only if it loses 717 cleanly (thin negative shelf below). Smaller/weaker pin → size lighter.
- **Caveats:** both regimes flipped POSITIVE only 05-22 (one session old; the prior tape whipsawed 5–6× in 30 days) — **fragile**. A holiday-weekend gap through 744.7 (SPY) / 717.8 (QQQ) inverts the hedging sign. EOD prior, ETF (not index) book, D+1 expiry not isolable.

### 2a. Next-session 0DTE premium-selling setup (validated stack)
Both indices **GO_PREMIUM_SELL_INTRADAY** (backtest n=30; SPY open-entry win 96.7%, QQQ 93.3%; advisory, 0 rubric points, tail unsampled).
- **SPY:** sell premium, VIX 16.7 (LOW), implied move 0.57% / expected range 0.75%, size_scalar 0.5, iron fly @745.9 ±0.75%. Enter at/after the open; hold to close; never carry overnight.
- **QQQ:** sell premium, VIX 16.7, implied move 0.80% / expected range 1.22%, size_scalar 0.5, iron fly @717.6 ±1.22%. Weaker than SPY (Nasdaq index book unavailable); flip one tick from spot.

## 2a. Swing Dealer Positioning (1–4 weeks)
- **No vanna squeeze anywhere** — every book is call-heavy with VIX falling, so the vanna vector is *decay pressure*, not a squeeze (the disqualifier firing as designed).
- **NVDA swing SHORT** (highest-conviction single-name dealer read): positive GEX collapsing 93% (2.02B→133M) into falling price (235→215); dealers short gamma at 215 ATM → downside acceleration. **MU / AMD swing LONG** (GEX expanding on breakouts). **IWM swing LONG** (clean GEX floor-building out of a FULLY_NEGATIVE stretch, +351k OI). SPY/QQQ/META NEUTRAL.

## 2b. Sector Rotation
- **Rotation regime: defensive→cyclical (medium confidence).** All 11 sectors net-INFLOW (persistence saturated at 1.0 — a melt-up tell, not a clean rotation), so ranking falls to magnitude/acceleration.
- **Regression catch:** GICS **Technology** (dominant inflow, $6.19B accelerating) **disagrees with every Tech ETF wrapper** — XLK −1.8M, SMH −82M (530P sweep $39.6M), IGV −8.6M. The GICS aggregate is inflated by mega-cap single-name call premium while the index vehicles are being put-hedged → **Tech downgraded to watch-only** per the GICS-vs-ETF cross-confirm rule.
- **Confirmed cyclical inflow (GICS+ETF agree):** Consumer Cyclical (XLY +20M → TSLA, CVNA) and Industrials (XLI +16M, but put-hedged → RKLB, UAL, HON, GE). **De-risking:** Energy (XLE, decelerating to ~zero → XOM, CCJ).

## 3. Swing Setups (1–6 weeks)
**Net: no swing position survives the gate stack.** The scored book and why each was cut:

| Ticker | Score | Tier | Thesis | Pre-risk | Final | Why cut |
|---|---|---|---|---|---|---|
| **AMD** | 9 | MEDIUM | bullish_flow / accumulation LONG | half | **skip** | C2 excess (beta WR) → half; debate bear≥bull → −1; single-name VRP −0.208 contradiction → −1 |
| **NVDA** | 4 | LOW | dealer swing SHORT | starter | **skip** | regime conflict (UPTREND vs short) −1; fundamentals fight the short (CAUTION) −1 |
| **F** | 3 | LOW | multileg diagonal LONG | half | **skip** | fundamentals CAUTION (unprofitable, D/E 4.54) −1; event-risk −1 (earnings-date mismatch: Finnhub 7/28 vs the diagonal's assumed 6/26 kink) |

Dropped at the quant layer (raw < 3): **MU** (−3 flow_conflict, cum_flow −$576M opposes long), **IWM** (−3 flow_conflict, cum_flow −$1.09B BEARISH), **ASTS** (raw 1; C11 halved + flow_conflict_lite — DP block buying but bearish sweeps and cum_flow −$32M).

Near-term **sweeps** (informational, 0 points): the 5-day tape is net hedging/bearish-skewed; the largest tickets are SPX downside-financing/collars and SMH protective puts. The only name with a scorable accumulation co-flag was ASTS (dropped).

## 4. LEAP Builds (6–24 months)
**Empty book.** Zero names cleared the 6-of-9 LEAP gate. The big OI builds (NVDA +412k, IWM +351k, etc.) are near/mid-dated, not >180 DTE. Filtered to fresh LEAPs: CMCSA (+73k call build is *bid-side*/sold, cum_flow bearish), FXI (put-dominated), NVDA LEAP (COVERED_CALL), AAPL (lead >180 build is a PUT). Closest miss: **KWEB** (fresh +180 DTE C30 build, cum_flow +$23M bullish) but conviction_matrix MIXED → watch, not buy.

## 5. Volatility Surface
- **PANW** — cleanest vol play: 100th-pctile IV, **VRP +0.211 (PREMIUM_SELLING)**, FLAT front (no panic), complacent back-month skew. Earnings 6/2. *The +0.211 VRP argues for a premium-SELLING expression (iron fly/credit), not a long straddle.*
- **QCOM** — VRP **trap**: high IV rank screams "sell," but VRP −0.12 (PREMIUM_BUYING) says vol is cheap vs realised. Do NOT sell premium. Earnings 5/29.
- **NTAP** — VRP +0.13, 100th-pctile, 06-18 event expiry carries all the bid. **DELL** — earnings 5/28, IV 123% 5/29 with complacent back-month → calendar, not naked short. **CRDO** — whole curve 100%+, back-month genuinely stretched → BUY VOL calendar lean.
- Single-contract IV-outlier screen: **none qualify** — all expiry-day (0DTE) gamma artifacts on leveraged-ETF/meme names (C12 junk).

## 6. Risk & Correlation
- **Regime/panic/VRP:** panic gate CLEAR (SPY front_end_iv 0.653 CONTANGO). Market VRP FAIR. **Single-name VRP is the decisive gate** this session — it cut AMD (−0.208 contradiction) and halved PANW (+0.211 makes a long-vol structure adverse).
- **Correlation:** AMD/NVDA measured 30d return corr **0.379** (<0.60) and are opposite-direction — no cluster penalty (the "both semis" 0.819 price-level corr is a shared-uptrend artifact; not applied).
- **Fundamentals verdicts:** AMD **CONFIRM** (genuine accumulation, $10B AI catalyst, earnings 73d out); NVDA **CAUTION** (fundamentals fight the short); PANW **CAUTION** (event handoff, 6/2); F **CAUTION** (earnings-date integrity 7/28 vs 6/26, unprofitable, D/E 4.54). No VETOs.
- **Debate:** AMD bull 0.65 / bear 0.65 — both converged that the win-rate is beta, not edge; debate did not clear → size cut.
- **Adverse-flow exits** (prior `conviction_2026-05-21`): NVDA (bearish, −$97M — confirms today's short read), META (bearish, −$48M), SNDK (bearish). MSFT still constructive (+$7M).
- **Hedge sleeve:** none required — the only sized position (PANW) is delta-neutral; no directional skew to hedge.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**AMD — raw 9, MEDIUM, FINAL: skip.** `score_components`: +3 cum_flow 30d (+$354M LONG ≥$50M) · +3 **C11 accumulation conjunction FULL** (5d OI BUILDING + smart_positioning BULL + DP mega buy_ratio 0.945, cum_flow confirms) · +2 dealer swing LONG (GEX expanding on 415→468 breakout, +81k OI) · +1 insights_signal_confluence. `dominant_signal_class`: bullish_flow. `win_rate`: 0.85 (n=14, backtest) — **but C2 market-excess gate found excess ≈ −0.07 (92.9% raw WR is up-tape beta; SPY itself a +0.59% signal in the set) → pre-risk demoted full→half.** LB-gate 5/5. `fundamentals`: CONFIRM. `debate`: bull 0.65 / bear 0.65 (did not clear → −1). `gate_verdicts`: vrp −1, debate −1 → **skip**. Invalidation: GEX rolls toward zero ≥3 sessions / spot loses 446 / regime flips RISK-OFF (beta 2.47).

*This is the regression headline: the strongest additive scorer is correctly gated out — C2 caught the beta win-rate, the debate caught the crowding, the VRP gate caught the structure mismatch. Under the prior rubric AMD's 0.85 WR would have full-sized.*

No other HIGH/MEDIUM names. PANW/NVDA/F (LOW) detailed in §3/§5.

**Embedded rubric:** see `.claude/commands/daily-analysis.md` Step 4 (the conviction rubric verbatim, incl. the C11 conjunction line).

## 8. Watch-only — single signal, no confluence
Failed the confluence gate (1 agent, no confluence≥4): CRDO (earnings BUY VOL), DELL/OKTA (earnings calendars), NTAP (vol SELL), QCOM (vol BUY VOL / VRP trap), SMH (bearish multileg — but a portfolio hedge against long semis, not directional). Micro-cap confluence names (SKYT, TE, QSI, CGC, IMRX) were **excluded by the C12 liquidity floor** — sub-$50M ADV, un-fillable.

---
*Decision envelope: `analyses/2026-05-25.decision.json` (schema 1.1, 4 calls, validates). Watchlist write-back: AMD, PANW, NVDA, F → `conviction_2026-05-25`.*
