# STEP 0 SHARED CONTEXT — 2026-07-28 (Tuesday)

`fz_available: true` — **BUT** the `fz` ticker column carries a systematic first-character-duplication
artifact this run (IINCY=INCY, TTHC=THC, AABR=ABR). The squeeze screen is additionally truncated to
A/B names alphabetically and is **unusable**. De-mangle via the Company column or ignore `fz` ticker lists.

## regime
`TRANSITIONAL — Mixed signals, reduce position size, wait for clarity`. trend = **CHOPPY**.
SPY 740.86 — **below 20SMA (746.65) AND below 50SMA (744.86)**, −2.57% from the 90d high, +1.63% 30d.
Options-flow breadth **36.9% bullish** (2,320 bullish vs 3,959 bearish tickers of 6,279).

## vrp_classification
SPY **FAIR** (iv30 0.1534 vs realised 0.1258, vrp +0.0277). QQQ **FAIR** (iv30 0.2617 vs realised 0.2562,
vrp +0.0055). Neither a premium-selling nor a premium-buying edge from VRP alone.

## dte_share
0DTE 30.5% · weeklies 30.7% · monthlies 20.7% · LEAPs 3.3% → `regime_hint: BALANCED`.

## TAPE FRAMING — READ BEFORE INTERPRETING ANY SIGNAL (measured OHLCV, not inferred)

Today is a **violent AI/semis complex unwind inside a green-breadth rotation tape**. Equal-weight beat
cap-weight, which is the whole story:

    RSP +1.17%  >  SPY +0.24%  >  QQQ −0.97%      XLK −1.84%   SMH −3.45%   SOXL −14.52%

**Down hard (1d):** SNDK −14.25, GLW −12.10, BE −11.34, NBIS −9.68, TSEM −9.46, MU −8.85, AMAT −7.82,
GFS −7.82, WDC −6.91, KLAC −6.18, PLTR −6.08, TLN −6.06, EWY −6.05, INTC −5.86, GEV −5.34, CRWV −4.93,
QCOM −4.21, NXPI −3.19.

**Up (1d) — the rotation destination:** KNSA +25.03, CLS +10.04, INCY +9.30, THC +7.92, GLOB +7.57,
SOLV +7.08, BKNG +6.70, HPQ +6.55, RNG +6.01, RCL +5.72, IBM +5.21, KO +5.00, GEHC +4.89, PCOR +4.85,
ADBE +4.81, NOW +4.79, SNN +4.63, UHS +4.34, LH +4.34, ALL +4.27, LTH +4.27, IP +3.96, GM +3.75,
PCAR +3.57, INTU +2.99.

**Sector ETFs (1d):** XLV +2.36 · XLP +1.99 · XLC +1.87 · XLB +1.85 · XLY +1.48 · XLF +1.27 · XLRE +0.55
· XLU −0.35 · XLI −0.39 · XLE −1.35 · XLK −1.84.

**5-day damage in the AI complex:** SNDK −31.04, SOXL −30.91, BE −26.26, GLW −22.41, NBIS −21.77,
TSEM −19.10, TSLA −18.87, INTC −18.16, GFS −17.46, AMAT −15.60, MU −15.48, WDC −15.48, CRWV −15.43,
GEV −12.55, EWY −12.41, KLAC −12.30, SMH −9.33.

> **"Broad rally" is the WRONG read.** This is week 2 of an AI/semis de-rating with money rotating into
> healthcare, staples, financials and cyclicals. Any bullish semis/AI thesis must clear this tape
> explicitly. Any bearish semis thesis must acknowledge it is already 1–2 weeks extended.

## EVENT RISK — the dominant gate this run
| Date | Event | Impact |
|---|---|---|
| **2026-07-29 (TOMORROW)** | **FOMC decision 2:00pm ET + Chair Kevin Warsh press conference 2:30pm ET** | **HIGH** |
| 2026-07-30 | Initial jobless claims | LOW/MED |
| 2026-07-31 | PCE (June) | HIGH |
| 2026-08-07 | Nonfarm payrolls (July) | HIGH |
| ~2026-08-12 | CPI (July) | HIGH |

**FOMC sits inside every swing horizon on this book.** No directional swing thesis is exempt from it.

## macro_snapshot (FRED, as of 2026-07-28)
Yield curve **NORMAL** (10Y−2Y +0.35) · core CPI **2.81%** YoY · core PCE **3.41%** YoY · unemployment
**4.2%** · payrolls **+57k** MoM · 10Y **4.65%, RISING** (+27bp/30d) · broad USD **WEAKENING** (−0.70/30d)
· fed funds effective **3.63%**.
→ Sticky core PCE at 3.41% with a 10Y rising 27bp into an FOMC = **hawkish-risk** setup.

## sector_summary (single-day net premium, $)
Healthcare **+206.0M** · Comm Svcs +184.1M · Financials +167.0M · Consumer Defensive +112.5M ·
Industrials +69.1M · Energy +48.1M · **Technology +34.2M on $7.11B call / $7.08B put gross — near-zero
net on enormous gross = churn, NOT accumulation** · Basic Materials +7.7M · Real Estate +2.7M ·
Utilities −12.0M · **Consumer Cyclical −250.0M**.

## sector_persistence (5d, 0–1 sign-consistency scale)
`persistence_score 1.0` INFLOW: Real Estate, Basic Materials, Healthcare, Consumer Defensive, Technology,
Financial Services, Energy. `0.8` OUTFLOW: Industrials, Consumer Cyclical.

> **Known defect:** `sector-flow-persistence` `net_flow` is gross call$ − put$ and is **sign-agnostic with
> respect to aggressor**. Do NOT read direction off it alone — cross-check the aggressor-classified source.
> Technology scoring `1.0 INFLOW` on the day the complex fell 3–14% is exactly this artifact.

## breadth_cross_check (fz — advisory, 0 rubric points)
357 advancers / 145 decliners / 1 unchanged of 503 · `pct_green` **70.97%** · avg +1.06% · median +1.39% ·
top IQV +13.94% · worst SNDK −14.25%. **No `divergence_flag`** (index green AND pct_green > 50).
But note the *inverse* divergence worth prose: **price breadth 70.97% green vs options-flow breadth 36.9%
bullish** — the tape is green while the options tape is defensive.

## zerodte_setup (advisory, 0 rubric points)
VIX **18.21** → `vol_state HIGH`. SPY: `sell_premium=true`, implied move 1.23%, expected range 1.19%,
`size_scalar 1.5`, verdict GO_PREMIUM_SELL_INTRADAY, net mean +0.158%/day, worst day −1.40%.
QQQ: `sell_premium=true`, implied 2.14%, expected range 1.99%, `size_scalar 0.75`, net +0.28%, worst
−2.453%, **CAUTION: front-end backwardation (0DTE IV 1.86× VIX) → half size.**

## funnel — top_bullish (net premium leaderboard, C12-passed)
SNDK +146.4M · QQQ +123.5M · NBIS +51.7M · GLD +41.3M · AAPL +31.2M · MU +28.6M · AMAT +28.0M ·
NOW +26.6M · MSFT +23.0M · SPY +13.3M · IBM +11.6M · GEV +11.4M · RCL +11.2M · VLO +9.9M · CRWD +9.8M ·
INTU +8.6M · GOOGL +8.3M · GFS +7.9M · CRWV +7.7M · AVGO +6.9M · ADBE +6.6M.

> ⚠ **CRITICAL CONTRADICTION.** SNDK, MU, AMAT, NBIS, GFS, CRWV and GEV top the **bullish** net-premium
> leaderboard while closing **−14.3%, −8.9%, −7.8%, −9.7%, −7.8%, −4.9%, −5.3%**. Positive net call
> premium into a −5 to −14% print is far more consistent with **put-selling, call-overwriting, or
> dip-hedge unwind** than with fresh bullish conviction. Treat "bullish flow" on any of these as
> **suspect until you verify aggressor side and whether the OI is OPENING**.

## funnel — top_bearish (C12-passed)
SPX −2,986M · XYZ −53.1M · TSM −35.8M · SOXL −32.1M · SHOP −30.3M · PLTR −29.0M · AMZN −24.9M ·
TSLA −24.0M · WDC −19.0M · INTC −18.8M · SPCX −18.8M · SMH −16.0M · BE −12.8M · TLN −12.6M · CAT −10.4M ·
GLW −10.3M · EEM −10.0M · IWM −9.9M · QCOM −9.2M · EWY −8.2M · CLS −7.7M.

## funnel — confluence (score ≥ 4, C12-passed only)
**BULLISH:** LW 6 · SBET 5 · RNG 5 · WEN 5 · KVUE 5 · UHS 5 · PCOR 5 · CZR 5 · GEHC 5 · SF 5 · BCS 5 ·
TLT 5 · GLD 5.
**BEARISH:** HWM 6 · KLAC 6 · IP 5 · VRNS 5 · NXPI 5 · ALL 5 · GLOB 5 · HPQ 5 · GNRC 5 · TSEM 5 · PPG 5 ·
OLED 5 · RSI 5 · PTC 5 · BKNG 5 · DTE 4.

> ⚠ **Contradictions to resolve, not inherit.** ALL, GLOB, HPQ, BKNG and IP sit on the **bearish**
> confluence list while closing **+4.27, +7.57, +6.55, +6.70, +3.96%**. ALL is simultaneously an `fz`
> new-high RS leader. `high_pcr` / `oi_building_puts` on a +4 to +7% up-day is far more consistent with
> **protective put buying on a rallying name** (or a collar/covered-call overlay) than with a short
> thesis. Verify aggressor side before calling any of these a fade.

## volume_outliers (C12-passed)
SNN 2885× · HCC 66× · SOLV 53×. (ZUMZ, MRDN, FMAO, AORT, DBI and the rest were C12-FAIL sub-$50M ADV.)

## fz_rs_candidates (de-mangled new-high / RS leaders — advisory, 0 rubric points)
KNSA · INCY · THC · LH · KO · PM · ALL · GM · PCAR · LTH · RLI · FMX · LILA/LILAK.
(C12-FAIL and dropped: FTRE, KFY, ASH, BVS, FNKO, IMMR.)
→ **Healthcare + defensives dominate the new-high list, independently confirming the rotation destination.**

## fz_squeeze_candidates
`[]` — lane UNUSABLE this run (alphabetical truncation + ticker artifact).

## opex_pin_candidates
**N/A — not OPEX week.** Third Friday was 2026-07-17; next is 2026-08-21. `opex-pin-strategist` not spawned.

## C12 liquidity floor — applied, fail-closed
**DROPPED, do not use:** SYBT, APPN, IBX, AMLX, TLRY, ADTN, HURN, ZUMZ, AORT, APAM, FLGT, CENTA, DBI,
OPK, EIG, BVS, FNKO, FTRE, KFY, ASH, IMMR, VCX, MRDN, FMAO, XXI, OTLK, SNDL, MSTU.
(`^VIX` also fails — index, no share volume. Expected; it is tape context, not a candidate.)

## Step-0 cache — READ THESE FILES, DO NOT RE-FETCH
Base: `/Users/ewan/Development/uw-daily-analysis/analyses/daily/2026-07-28/step0_cache/`

`daily_synthesis.json` · `market_regime.json` · `dte_volume_share.json` · `sector_flow.json` ·
`sector_flow_persistence.json` · `screener_bullish.json` · `screener_bearish.json` ·
`signal_confluence_bullish.json` · `signal_confluence_bearish.json` · `iv_rank_high.json` ·
`iv_rank_low.json` · `volume_vs_average.json` · `earnings_catalyst.json` · `expiry_heatmap.json` ·
`iv_outliers.json` · `greek_screener.json` · `top_premium_trades.json` · `most_active.json` ·
`oi_smart_positioning.json` · `single_leg.json` · `vrp_spy.json` · `vrp_qqq.json`
