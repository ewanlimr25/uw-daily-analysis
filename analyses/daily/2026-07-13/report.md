# Daily Market Analysis — 2026-07-13

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL (trend UPTREND) — SPY 749.17, above 20/50 SMA (+3.27% 30d, −1.48% from 90d high) but breadth decisively bearish (33.8% bullish flow, 2116 bull / 4149 bear). VIX 17.13 **spiking +2.1**. SPY **and** QQQ both **FULLY_NEGATIVE GEX (short-gamma)** into the open → amplification, not pinning. Sector lean defensive: DP money into Energy/Healthcare/Utilities, out of Technology (−$516M DP).
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half` (P0.6 guard; moot — no name cleared the LOW floor).
- **Next-session GEX (SPY/QQQ):** SPY short-gamma, ZGL null/unreliable, call wall 760 / put shelf 740 → favor debit verticals / long premium over CPI, not premium-selling. QQQ short-gamma, call wall 730 / downside air-pocket to 700. Advisory, see §2.
- **Top swing build:** **None.** Empty conviction board — all 6 confluence-passing names scored ≤1 raw (below the raw-3 LOW floor). 8th consecutive thin/empty board.
- **Top LEAP candidate:** **None.** IBIT clears 6-of-8 gates only marginally (recent-30d convexity add, not settled accumulation) → watch, not size.
- **Biggest risk:** **CPI tomorrow (2026-07-14)** into a short-gamma, VIX-spiking, breadth-bearish tape. Institutions are already printing protection (SPX collar rolls, SPY put flys, VIX call spreads). The candidate union is substantially one AI-semis factor bet (SMH/DRAM 0.93 corr). Prior-group **NVDA is an exit-candidate on adverse flow reversal**.

> **No-edge day.** This is the frozen rubric (v2026-06-12) behaving as calibrated on a defensive pre-CPI tape — not a pipeline failure. Every candidate is either a non-directional vol/pin structure earning a single +1, or a directional thesis its own 30-day flow contradicts. §3 and §4 are intentionally empty; §1/§2 carry the advisory reads.

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend UPTREND, but breadth bearish: 33.8% bullish flow across 6,265 optionable tickers (2,116 bull / 4,149 bear). Guidance: half sizes, defined-risk, iron condors in range.
- **Per-index gamma (current-state EOD book):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall/shelf |
|---|---|---|---|---|---|---|
| SPY | 749.27 | null (unreliable) | −$1.18B | FULLY_NEGATIVE | 760 (+120M) | 740 (−131M); 748–750 at-the-money short-gamma |
| QQQ | 712.14 | null (unreliable) | −$759M | FULLY_NEGATIVE | 730 (+46M) | 710 (at-money); 700 discrete magnet |
| IWM | ~293 | grid-artifact (use total_gex sign) | −$1.04B | short-gamma (deepening 6 sessions) | — | — |

- **`uw options-flow dte-volume-share`:** 0DTE 38.4% / weeklies 30.4% / monthlies 19.2% / LEAPs 4.3% — **BALANCED** (neither retail-blowout nor institutional-positioning extreme).
- **`uw historical vrp` (SPY):** FAIR (VRP −0.0109; IV30 14.39% vs realized 15.47%). Slight premium-buying tilt, no clean vol edge either way.
- **Macro backdrop (`scripts/fred_macro.py`):** yield curve normal (+0.36 10y2y); **core CPI 2.96% / core PCE 3.41% — sticky/elevated**; unemployment 4.2%, payrolls **+57k (soft)**; 10Y 4.56% (flat 30d); **USD strengthening**; fed funds 3.62%. Sticky inflation + softening labor + strong dollar = a headwind for risk and for long-duration growth.
- **Forward event risk (Tier-1, next ~10 sessions):** **CPI Tue 7/14**, Fed Chair Warsh testimony 7/14–15, PPI Wed 7/16, Retail Sales + Jobless Claims Thu 7/17, **monthly OPEX Fri 7/17**, U-Mich sentiment Fri 7/18, **FOMC Jul 28–29**.

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, prose-only, 0 rubric points, no backtested predictive claim.** EOD dealer-gamma book read forward as the *prior* for the 7/14 open. Scope SPY/QQQ only.

Both indices are **FULLY_NEGATIVE (short-gamma)** — dealers sell weakness / buy strength, so tomorrow's tape **amplifies** moves rather than pinning. ZGL is null on both (expected in FULLY_NEGATIVE regime) → `zgl_reliable=false`; use total_gex sign + spot-vs-wall instead.

| Index | Regime | Call wall | Put wall / shelf | One-line structure bias |
|---|---|---|---|---|
| **SPY** (spot 749.27) | short-gamma | **760** (+120M, +1.43%) | **740** (−131M, −1.24%); no clean discrete downside wall — air-pocket below ~745 to 740/735 | Short-gamma → **debit verticals / long premium over CPI**, not iron flies. Reclaim 754+ pre-market would re-check for a POSITIVE flip. |
| **QQQ** (spot 712.14) | short-gamma | **730** (+46M, +2.51%) | **710** (at-money); **700** discrete magnet | Short-gamma → directional 0DTE / debit verticals / long-vol lean. Downside has no clean wall until 700. |

**Regime freshness:** both names have flipped POSITIVE↔NEGATIVE↔FULLY_NEGATIVE 5–6× in the last 8 sessions — an **unsettled, fast-moving gamma regime**, not a held one. The 7/10 SPY POSITIVE flip (ZGL 754.15) already round-tripped by 7/13.

**Mandatory caveats:** (1) EOD is a **prior, not a target** — fresh 0DTE OI re-computes the ZGL/walls in the first 30–60 min. (2) **Gap risk is elevated and specific: CPI prints tomorrow** — a surprise can gap spot through the walls before the cash open; the short-gamma read is *consistent with* amplification into that print, not a hedge against it. (3) ZGL null on both = FULLY_NEGATIVE, expected not a data gap. (4) `gex --dte-max 1` errors — this is the 0–45 DTE book, a proxy for the D+1 expiry. (5) ETF book, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — the validated stack)
**STAND ASIDE both SPY and QQQ.** `sell_premium=false`, `size_scalar=0.0` on both. Stand-aside reason: **VIX spiking (+2.1) — short-vol left-tail regime.** QQQ additionally flags **front-end backwardation (0DTE IV 1.64× VIX) — event/gap risk, half size.** Advisory, delta-neutral, 0 rubric points — and today the setup itself says do not sell 0DTE premium into a spiking-VIX, short-gamma tape ahead of CPI. SPY implied move 1.06% / expected range 1.25%; QQQ implied move 1.77% / expected range 1.91%. **SPY ≈ SPX** (trade either); **QQQ weaker** (Nasdaq index book unavailable).

## 2a. Swing Dealer Positioning (1–4 weeks)
**No mechanized DEX flip anywhere in the fleet.** SPY/QQQ/IWM all show DEX **sign whipsaw** (3+ sign changes in 5 sessions) — exactly the artifact the ≥3-consecutive-prior-session rule excludes. No vanna squeeze fires: **VIX is rising** (dated Yahoo ^VIX +2.13 from 7/10→7/13), which invalidates the falling-VIX squeeze mechanism and instead reframes the put-heavy QQQ/IWM books as **vanna-driven selling pressure**.

- **SPY:** DEX NEGATIVE but near-zero (−$94M, 0.005× trailing median) — no directional persistence. Swing bias **FLAT**.
- **QQQ:** DEX NEGATIVE (−$16.97B), put-heavy book, but VIX rising → vanna *pressure* not squeeze. **Front-end IV ratio 1.143 (BACKWARDATION) — front panicked** (CPI pricing). Swing bias FLAT, cautious lean.
- **IWM:** most internally consistent — DEX deteriorating (4 of 5 sessions negative), total_gex deepening negative 6 straight sessions, front-end ratio **1.387 (sharply panicked)**. Swing bias **SHORT-leaning (informational, not scored)** — small-caps carrying the most acute rate-sensitive CPI risk.

*Data-quality carry-forward: QQQ/IWM `zero_gamma_level` shows the recurring sub-320 / sub-200 grid artifact; use total_gex sign. The `regime` field on gex-time-series frequently disagrees with the total_gex sign — treat regime as unreliable, use the sign.*

## 2b. Sector Rotation
**Rotation regime: `no_change` (low confidence).** No canonical pattern clears the ≥3-day persistence bar on both legs. There are early, uncorroborated (1-day) signs of a cyclical/growth → defensive/value tilt — plausibly pre-CPI de-risking — but it fails the hard 3-day rule on the outflow leg.

**The real finding is a divergence, resolved:** the apparent "Tech inflow" in options net premium (+$1.2B) is **concentration in a handful of mega-caps** (MSFT/TSM/AMAT/QCOM each ~+$6–8M) sitting on top of heavy internal selling (**NVDA −$189M, SNDK −$76M, INTC −$55M**), a flat-to-negative XLK ETF (−$2.2M), and the −$516M DP outflow. Not sector-wide rotation — dispersion.

Two sectors carry genuine cross-instrument confirmation (watch, not headline):
- **Healthcare** — real but narrow (managed care/services: UNH, CNC, DVA); biotech (XBI −$10.6M) diverges bearish.
- **Energy** — fails the strict options-flow magnitude gate but confirmed via DP inflow + **fz RS/new-high refiner cluster (MPC, VLO, PSX, DINO, PBF, OII)** + screener cross-confirm on DINO. Alt-data-led, not options-flow-led. Leaders: XOM, CVX, DINO.

**ETF flow tape (advisory):** XLF +$20.4M (BULLISH, agrees GICS Financials); SMH +$12.2M / XLK −$2.2M (both MIXED, blocks sold below mid — disagree with the GICS Tech "inflow"); XBI −$10.6M / GDX −$9.9M (BEARISH). No new rubric points.

## 3. Swing Setups (1–6 weeks)
**Empty.** No name cleared the raw-3 LOW floor. The full quant audit is in §7. The single-signal candidates that surfaced but failed the ≥2-agent confluence gate are in §8.

For journaling, the near-misses and their kill reasons:
- **SMH** — clean bearish sweep (3/5 persistence, distribution/short-call opening + ask-side put buying), but sweep-persistence earns 0 rubric points and no second agent confirmed a directional thesis → single-signal.
- **SOFI** — the cleanest coordinated structure on the tape (multileg Jul-31 bull call spread into a confirmed earnings kink, risk capped at debit) — but single-agent, so watch-only.
- **FIG / FAST** — genuine quiet accumulation (accumulation-hunter, 3–4 aligned signals each, clean timestamps outside the closing-cross and 21:22:55Z basket-print artifacts) — but single-agent, and neither cleared the $50M flow-magnitude floor.

**Near-term sweeps (informational):** the mega-cap/index sweep book (SPXW/QQQ/SPY/TSLA/AAPL/MSFT all bearish 4–5/5) is directionally consistent with the net-bearish tape but is textbook hedge flow (30d cum-flow MIXED on every name) — filtered out of conviction. **No clean bullish primary sweep survived corroboration today.**

## 4. LEAP Builds (6–24 months)
**None sized.** `leap-positioning-radar` ran the full 9-gate stack. Only **IBIT** cleared 6-of-8 scorable gates, and marginally — a far-OTM Dec-2028 $70C build (+218% OI, 92% ask-side) layered on a genuine but **recent-30-day** bullish premium accretion. Reads as a leveraged BTC convexity add, not a settled multi-quarter accumulation (Gate 3 rolls = 0; Gate 7 institutional-accumulation NEUTRAL all 5 sessions). **Watch, not size** — re-check if the $70C strike recurs as a top-5 daily mover.

Disqualified: WOLF (cum-flow BEARISH both windows, flow_conflict), IREN (put build, conviction-matrix MIXED), RIVN (matrix 2.6%), GRAB (matrix 1%, 90d BEARISH), HOOD (bid-dominant = covered-call writing), F/FRMI (immaterial size).

## 5. Volatility Surface
Rich absolute IV everywhere, but **VRP discipline kills most sell-vol expressions** and CPI/PPI/OPEX contaminate the front bucket (every name reads mechanical BACKWARDATION):
- **NFLX** — clean earnings kink at 7/17 confirmed vs 7/16 PM earnings; **positive VRP (+0.1367, PREMIUM_SELLING)**, implied move 6.86%. The cleanest earnings-vol structure on the board (short strangle/condor at ~1× move, **after** the print). Belongs in the earnings book; does not carry a conviction row.
- **MSFT** — kink at 7/31 vs 7/29 earnings, but **VRP FAIR** → a calendar/structure play, not a vol-richness sale.
- **NBIS** — largest VRP in scan (+0.2906) but **flat curve, no kink** → no structural edge to trade; and its 88% high-IV realisation rate is a **caution against shorting vol into CPI**.
- **SMH** — 98th-pct IV but **negative VRP (−0.0615, PREMIUM_BUYING) + TAIL_HEDGING skew** → do not sell premium; realized is outrunning implied.
- **ARQQ** — most extreme absolute IV (125–197%) but **negative VRP (−0.65)** → not rich vs realized; no trade.
- *Calendar-spread bucket empty:* every backwardated name has front-end-iv-ratio >1.10 with **no confirmed-falling time series** and CPI/PPI/OPEX still ahead → event-driven holds, not calendar fades. Re-check post-CPI. *All percentile reads n=63 (provisional, < 120-day first-class floor).*

**Bank-earnings vol book (7/14–7/16, earnings-scout):** cleanest SELL-VOL setups are **BAC** and **WFC** (full size — tail-hedged back-month confirms the crush edge), then C (moderate), MS/GS/JPM (half, front-only kink), NFLX/TSM (half). **UNH — SKIP** (idiosyncratic gap-risk override; small BUY VOL at most). These are delta-neutral vol plays outside the directional conviction rubric.

## 6. Risk & Correlation
**Macro headline:** sticky core inflation (CPI 2.96% / PCE 3.41%) + soft payrolls (+57k) + strengthening USD, into a **CPI print tomorrow** — a binary Tier-1 event inside every conceivable swing horizon. FOMC 7/28–29 behind it.

**Empty board → hygiene mode.** Net delta 0, nothing sized.

- **Correlation (candidate union, for the record):** **SMH/DRAM 0.93 = one position** (`semis_beta_cluster`, gate armed if either resurfaces). A soft-watch web NVDA/NBIS/SMH/DRAM/NFLX/FIG/MSFT all 0.60–0.69 — the union is substantially **one AI-semis factor bet**, consistent with the −$516M Tech DP outflow.
- **Adverse-flow exit scan (prior group `conviction_2026-07-10` = NVDA, EWZ):**
  - **NVDA → EXIT-CANDIDATE.** Adverse flow reversal vs the 7/10 long watch: net options flow −$189.4M bearish, $293M single DP print, +399,788 net OI shift; 90d cum-flow −$350M; the 7/10 bull-call thesis (Jul17 expiry) now sits on OPEX Friday into CPI. Flow-driven exit tag (no adverse fundamentals field).
  - **EWZ → HOLD-watch (on-thesis).** Alerts confirming (net flow +$1.6M bullish, PCR 0.51); one headwind — strengthening USD is a drag on EM/Brazil.
- **Gate verdicts (board-level, all 9 keys):** `regime` no-op · `vrp` no-op (FAIR) · `panic` no-op (not re-read) · `cluster` record-only (SMH/DRAM 0.93) · `sector` record-only (Tech DP −$516M adverse tag) · `fundamentals` n/a · **`event_risk` LIVE-relevant** (CPI T+1 would fire −1 tier on any non-event swing; OPEX T+4; FOMC ~T+10) · `debate` n/a · `rubric_regime` moot (OUT-OF-REGIME half-cap, 0 sized rows).
- **Breadth cross-check (`fz`, advisory):** 273 advancers / 230 decliners, **pct_green 54.27%** (avg change −0.02%). Price breadth modestly green vs the **uw flow-breadth bearish (33.8%)** — a divergence: price holding while options flow leans bearish is a mild distribution tell, consistent with the defensive DP rotation. Advisory, does not change sizing.

**Hedge sleeve (for any legacy/discretionary exposure into the CPI→OPEX→FOMC gauntlet — defined-risk, starter-size, long-convexity only; NOT a backdoor directional short):**
1. **SPY put butterfly** ~745/735/725, Jul-24 exp — defined-risk through CPI (T+1) and OPEX (T+4); a fly (not an outright) because short-gamma FULLY_NEGATIVE caps the vol bill.
2. **VIX call spread** Aug ~19/25 — VIX already spiking; Aug bridges the 7/28–29 FOMC; mirrors the institutional VIX call spreads on the tape.
3. **Do not sell premium** anywhere into tomorrow — FAIR VRP gives no cushion, both indices short-gamma, NBIS 88% realisation generalizes the warning.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**Empty — no name reached MEDIUM (raw ≥ 7) or even LOW (raw ≥ 3).**

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: N/A this session — no sized calls and no closed conviction calls to compute per-tier payoff over. Carried context from the most recent audit (2026-07-04): the empty-book/refuse-to-size behavior is the system's best-graded discipline (sized book realized 36.1% vs paper 45.2%; DROP pile 0.477 > traded book 0.406).

Full quant audit of the 6 confluence-passing names (all DROP):

| Ticker | Raw | Score components | Dominant class | win_rate (n, src) | Pre-risk | Why DROP |
|---|---|---|---|---|---|---|
| NFLX | 1 | +1 earnings-scout SELL VOL (7/16, move 6.86%, VRP +0.14); vol-surface kink NOT double-scored (C13) | earnings_vol | NA(substrate) | skip | Cleanest structure on board; dies on rubric floor, lives in earnings book |
| XLF | 1 | +1 OPEX top-5 pin (55); sector-leader +1 failed $50M floor ($19.8M) | opex_pin | NA(substrate) | skip | Pin thesis → OPEX book prose |
| NVDA | 1 | +1 OPEX pin (200); multileg +2 withheld (leg unresolved) | opex_pin | NA(substrate) | skip | 90d −$350M + internal selling lean distribution |
| MSFT | 1 | +1 earnings-scout SELL VOL half; vol/single-leg 0 pts | earnings_vol | NA(substrate) | skip | 30d −$727M + Tier-1 bearish floor put = distribution lean |
| NBIS | 0 | sweep line deprecated; vol +1 failed (flat curve) | high_iv_rank | 0.80 cap (n=164, backtest_clean) | skip | 88% high-IV realisation is ADVERSE to short-vol; nothing scores |
| UNH | −1 | sector-leader failed gates b+c; **−1 flow_conflict_lite** (30d −$16.7M MIXED vs LONG) | sector_rotation | NA(substrate) | skip | Healthcare-leader thesis contradicted by its own 30d/90d flow |

Recurring kill-patterns all fired: C13 routing (NFLX/MSFT earnings kink not double-scored), the $50M sector-leader magnitude floor (XLF, UNH), unresolved/mixed structures earning zero (NVDA multileg, NBIS rolls).

### Conviction-scoring rubric (v2026-06-12, frozen) — embedded for audit
```
Daily conviction score = Σ:
 +1 dealer-positioning MECHANIZED DEX flip / vanna-squeeze (verified sign change, |net_dex| ≥ 0.25× trailing-10 median; dated evidence)
 +3 accumulation-hunter 3+ aligned (DP+OI+smart-positioning, block-stratified inst-tier) — CONJUNCTION: full +3 only if cum_flow_30d aligned AND ≥$50M; else halved to +1
 +1 multi-day OI build (oi-trend BUILDING, --days ≥5)
 +1 conviction-matrix DIRECTIONAL_LONG conf>70 — CONDITIONAL: only when dominant_signal_class == leap_directional
 +1 cum-premium-flow net directional accretion (30d) — INTENT-SCREENED (no distribution_flag; not ex-div deep-ITM sub-parity)
 +1 sector-rotation single-name leader — CONDITIONAL: persistence ≥0.6 AND cum_flow aligned AND |cum_flow_30d| ≥ $50M
 +1 earnings-scout BUY VOL or SELL VOL
 +2 multileg-strategist directional structure (term-structure-anchored)
 +1 vol-surface-scout KINKED/BACKWARDATION with VRP-aligned bias
 +1 opex-pin-strategist ranks top-5 (OPEX week only)
 -2 contrarian overcrowded long + rising pc-ratio-zscore (informed-flow continuation penalty)
 -3 flow_conflict (cum-flow 30d clearly opposite dominant_signal_class)
 -1 flow_conflict_lite (cum-flow MIXED / bottom-quartile) — mutually exclusive with flow_conflict
 [TIER GATES, risk-monitor 2d, not score points]: -1 tier corr cluster ≥0.70; -1 tier regime conflict
Tiers: ≥9 HIGH (full) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 drop
```

## 8. Watch-only — single signal, no confluence
Surfaced from one agent, failed the ≥2-agent confluence gate. **For journaling, not trade entry today.**

| Ticker | Agent | Signal |
|---|---|---|
| SMH | sweep-tracker | Clean bearish (3/5 persistence, short-call opening + ask-side put buying) — 0 rubric points |
| SOFI | multileg-strategist | Bull call spread Jul-31 C20/C23 into confirmed earnings kink (MEDIUM structure, risk capped at debit) |
| DRAM | multileg-strategist | Bear put spread Aug-14 P50/P30, elevated vol (directional-bearish) |
| WEN | multileg-strategist | Bear put spread Jul-24 P8/P7 into a 165%-IV binary (speculative, small) |
| FIG | accumulation-hunter | 4 aligned signals (clean $62.7M mega-block, 5-day OI build, DP defense $23.05–$23.70); ⚠ distribution_flag present (Aug/Sep $25C OI closing — reads as strike-ladder roll) |
| FAST | accumulation-hunter | 3–4 aligned signals (block-tier accumulation, 5-day OI build, DP defense $46.85–$47.05) |
| ET | opex-pin-strategist | #1 pin (strike 20, +66M GEX wall, <1% distance) — best pin to hold into Friday |
| AMZN | opex-pin-strategist | #3 pin (250) — HIGH fragility to Thu Retail Sales |
| IBIT | leap-positioning-radar | Marginal 6-of-8 gates; Dec-2028 $70C convexity add (recent-30d, not settled) |
| BAC/WFC/C/GS/JPM/MS/TSM | earnings-scout | Bank/mega-cap earnings SELL-VOL book (delta-neutral); BAC/WFC cleanest (full size) |
| XOM/CVX/DINO | sector-rotation | Energy leaders (DP + fz RS refiner cluster confirmed) |
| MSFT/ORCL/MSTR/WMT/T/BSX | sweep-tracker (single-leg C19) | Tier-1 FLOOR_PUT_BLOCK bearish (advisory, 0 points) |

---
*Pipeline: 12 Phase-1 agents (OPEX week) → signal-confluence-quant (empty board) → risk-monitor (hygiene mode). Fundamentals-gate (2b) and bull/bear debate (2c) skipped — no HIGH/MEDIUM names to disconfirm. Steps 6/6.5/8.5 (deep-dive, batch-scan, deep-dive hand-off) skipped — no sized names.*
