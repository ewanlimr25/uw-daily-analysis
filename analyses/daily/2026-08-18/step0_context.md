# STEP 0 SHARED CONTEXT — 2026-08-18 (daily-analysis)

## Date / availability
- report date / --date for every uw call: **2026-08-18**
- UW data current (2026-08-18 present in `available-dates`). fz_available = **true**
- **OPEX WEEK**: monthly third-Friday = 2026-08-21 (3 calendar days out)

## Regime (from cached market_regime / daily_synthesis — DO NOT RE-FETCH)
- regime label: **TRANSITIONAL — Mixed signals, reduce position size, wait for clarity**
- trend: **UPTREND**; SPY 767.45, above 20SMA (758.68) and 50SMA (749.84), +3.42% 30d, −1.53% from 90d high
- market breadth (uw): bullish_pct **31.5%** (1,990 bullish vs 4,326 bearish tickers of 6,316)
- trading_guidance (uw): "Half position sizes. Favor defined-risk strategies. Iron condors in range."

## TAPE FRAMING — READ THIS BEFORE INTERPRETING ANY FLOW (raw Yahoo OHLC, --as-of 2026-08-18)
**Today was a SEMIS/AI-LED RISK-OFF, not broad selling.**
- SPY −0.68% · QQQ −1.69% · IWM −1.26% · **RSP −0.45%** (equal-weight BEAT cap-weight ⇒ damage is concentrated, not broad)
- Semis complex destroyed: **SOXX −4.96% · SMH −4.09% · SOXL −14.8% · EWY −8.13% (Korea/semis) · XLK −2.47%**
- Single names: SNDK −9.01%, LITE −9.87%, STX −9.16%, MU −7.02%, INTC −6.58%, NBIS −7.60%, CRWV −12.10%, KLAC −5.33%, META −4.45%, AMD −4.27%, TSM −4.07%, AVGO −3.17%, CEG −4.09%
- Bid: **XLE +1.76% · XLV +1.60% · XLP +1.06% · XLF +0.45%**; LLY +3.60%, INTU +4.41%, ULTA +4.75%, AAPL +1.45%, BABA +2.76%, NFLX +2.30%, NKE +2.48%, TRGP +7.13%
- VIX **15.84, +4.28%** (still a LOW absolute level)
⇒ Treat "bullish tech flow" claims with suspicion today; treat energy/defensive strength as the actual rotation.

## VRP (cached — DO NOT RE-FETCH)
- SPY: **FAIR**, vrp +0.0079 (IV30 13.30% vs RV30 12.51%)
- QQQ: **FAIR**, vrp **−0.0292** (IV30 19.87% vs RV30 **22.79%**) ⇒ QQQ IV is BELOW realized — premium-BUYING tilt in Nasdaq names, premium-selling has no edge there.

## DTE volume share (cached — DO NOT RE-FETCH)
0DTE 25.6% · weeklies 34.3% · monthlies 24.2% · LEAPs 4.5% → regime_hint **BALANCED** (MARKET-level only; there is no per-sector split)

## Sector layer — NETTED vs GROSS DISAGREE (important)
- **NETTED (authoritative for DIRECTION — `market-regime.sector_rotation`, top3/bottom3 truncated):**
  OUT: **Technology −$409.99M · Communication Services −$141.57M · Consumer Cyclical −$53.44M**
  IN: **Energy +$1.44M · Consumer Defensive +$1.32M · Real Estate −$1.85M**
- **GROSS turnover (`sector-flow`, sign-agnostic, NOT direction):** Technology +$1.807B, Energy +$994M, Comm Svcs +$273M, Fin Svcs +$217M, Healthcare +$192M, Cons Cyc +$182M, Industrials +$169M, RE +$72M, Cons Def +$55M, Materials +$29M, Utilities +$8M
- ⇒ **Technology: netted says OUTFLOW, gross says INFLOW ⇒ DISAGREEMENT ⇒ any Tech rotation call is `watch_only`.**
- **`sector-flow-persistence` fired INFLOW / persistence_score 1.0 on 11 of 11 sectors** (Real Estate 0.8). This is a **gross-turnover durability filter with zero discrimination today** — it is NOT evidence of direction and must NOT be cited as such. It and `sector-flow` are ONE source, not two.

## Breadth cross-check (fz — ADVISORY, 0 rubric points)
advancers 224 / decliners 275 / unchanged 3 of 502 · **pct_green 44.62%** · avg_change −0.45% · median −0.19% · top TRGP +7.14% · worst COHR −12.75%
→ index red AND pct_green < 50 ⇒ **consistent, no divergence flag** (this is not the hidden-distribution case).

## Macro snapshot (scripts/fred_macro.py)
yield curve **normal** (10Y−2Y +0.52) · core CPI **2.79%** YoY · **core PCE 3.29%** YoY (hot) · unemployment **4.1%** · **payrolls −23k MoM (NEGATIVE)** · 10Y **4.72%, RISING** (+0.17 in 30d) · USD **weakening** (−1.41 in 30d) · fed funds 3.63%
→ Stagflation-ish tint: core PCE 3.29% well above target WHILE payrolls contract and 10Y rises.

## FORWARD EVENT RISK — HEAVY. Gate every swing horizon against this.
| Date | Event | Impact |
|---|---|---|
| **2026-08-19 (D+1)** | **FOMC Minutes** (Jul 28–29 mtg), 2:00pm ET | HIGH |
| 2026-08-20 (D+2) | Initial jobless claims | MEDIUM |
| **2026-08-21 (D+3)** | **Monthly OPEX expiry** | HIGH (mechanical) |
| **2026-08-26 (D+6)** | **PCE / Personal Income & Outlays (July)**, 8:30am | HIGH |
| 2026-08-27 (D+7) | Jobless claims; Q2 GDP 2nd est; **Jackson Hole begins** | MEDIUM/HIGH |
| **2026-08-28 (D+8)** | **Jackson Hole keynote — Kevin Warsh's FIRST speech as Fed Chair** | HIGH |
| 2026-09-04 | NFP (August employment situation) | HIGH |
| 2026-09-11 | CPI (August) | HIGH |
⇒ **Every 1–6 week swing carries PCE + Jackson Hole + a brand-new Fed Chair's debut keynote.** There is no clean window.

## Next-session 0DTE setup (scripts/zerodte_setup.py — ADVISORY, 0 rubric points)
SPY: sell_premium=true, vol_state **LOW**, VIX 15.84, implied_move 0.70%, expected_range 1.23%, size_scalar 0.5, verdict GO_PREMIUM_SELL_INTRADAY, mean_pnl_open 0.212% gross / **0.112% net**
QQQ: sell_premium=true, vol_state **LOW**, VIX 15.84, implied_move 1.17%, expected_range 2.08%, size_scalar 0.5, mean_pnl_open 0.331% gross / **0.231% net**
**⚠ LOW-VIX CAVEAT (known defect): `sell_premium:true` is UNCONDITIONAL. The conditional table is what matters — `mean_pnl_by_vix_state.LOW` = SPY +0.01% / QQQ +0.07% GROSS; net of the 0.1% round-trip cost both are ≈ZERO-TO-NEGATIVE. Edge lives only in MID/HIGH VIX terciles. Today is LOW. Treat as STAND-ASIDE.**

## C12 LIQUIDITY FLOOR (price ≥ $5 AND 20d dollar ADV ≥ $50M) — authoritative, fail-closed
**PASSED** (tradeable universe): SPY QQQ IWM RSP VOO XLK XLE XLF XLV XLI XLY XLP XLU XLB XLRE XLC SMH SOXX SOXL GLD IAU EWY EWZ JETS QTUM · AAPL NVDA COIN LLY NOW STX AMZN NBIS MSFT INTU ET BABA DDOG AMD NFLX COST AS HAL CEG NKE SNDK META MU TSLA LITE AVGO KLAC SNOW ORCL INTC AMAT GOOG CRWD TSM CRWV · ULTA DE TJX EL ROST BURL DELL DG HEI ASND BN LII SON PCG USB DB GRMN FRSH EXE CHYM · AMLX HAE TRGP CLMT HTFL
**FAILED (DROPPED — do not analyse, do not score):** ^VIX (index, no share vol — tape context only) · YINN $31.9M · ROM $8.6M · DRLL $0.5M · ACAD $48.3M · NTLA $37.4M · NMAX $11.0M · ALKT $24.8M · JMIA $12.3M · HLF $18.2M · PUMP $44.6M · XNCR $23.3M · PAYS $8.3M · KURA $15.8M · MSOX ($2.53 < $5) · BORR ($4.43 < $5) · SPRX/FULC/CAAP/SATA/BLBD/BLOX/CLYM/BCI/SSPC/CANE/HDSN (sub-floor / unverifiable)
**NOTE:** the entire top of `signal_confluence_bullish` (NTLA, NMAX, MSOX) is sub-floor. Only **AS** survives from the top 4.

## Top-of-funnel (cached — READ THE FILES, DO NOT RE-ISSUE)
- `screener_bullish` top: AAPL +$27.5M, NVDA +$15.9M, COIN +$12.6M, LLY +$12.1M, NOW +$10.6M, STX +$10.0M, AMZN +$8.8M, QQQ +$8.5M, NBIS +$6.8M, MSFT +$5.3M, INTU +$5.3M, ET +$4.4M, BABA +$3.5M, DDOG +$3.5M, AMD +$3.4M, NFLX +$3.4M, COST +$3.3M, AS +$3.0M, HAL +$2.8M, CEG +$2.7M, NKE +$2.7M
- `screener_bearish` top: SPX −$638.6M, SNDK −$139.1M, META −$124.4M, MU −$92.1M, SPY −$51.2M, TSLA −$49.1M, SMH −$46.9M, SOXL −$32.6M, IWM −$28.2M, EWY −$25.3M, LITE −$22.0M, SOXX −$19.7M, AVGO −$19.4M, KLAC −$19.2M, SNOW −$13.0M, ORCL −$12.5M, INTC −$12.3M, GLD −$12.2M, AMAT −$12.2M, GOOG −$11.9M, CRWD −$11.7M, TSM −$11.6M, CRWV −$11.6M
- `signal_confluence_bullish` (floor-surviving): **AS score 6** (bullish_flow, low_pcr, volume_spike x14.68, dp_accumulation, oi_building, low_iv_cheap_options); MSFT 5; NKE 5; PCG 5; EWZ 5; USB 5; CHYM 5; DB 5; EXE 5; IAU 5; FRSH 5; GRMN 5
- `signal_confluence_bearish` (floor-surviving): **ULTA 6** (bearish_flow, high_pcr, volume_spike, dp_distribution, oi_building_puts, high_iv_sell_premium, iv_rank 74.0); DE 5 (iv_rank 74.6); TJX 5 (iv_rank 82.5, vol ratio 9.01); EL 5; ROST 5 (iv_rank 95.3); BURL 4; DELL 4 (iv_rank 74.3); DG 4; HEI 4; ASND 4; BN 4; LII 4; SON 4; JETS 4; QTUM 4
- `volume_vs_average`: essentially ALL sub-floor micro-ETFs (FALN, IRIX, SPXE, HEWJ, QRMI, UTHY…) — **no usable candidate survives C12 from this screen today**
- `iv_rank_high`: VIRT, ALMS, PACB, BLOX, TENX, BBD, NABL, SPWH, CINT, MYO, AWRE, IOND (100 IVR) — nearly all sub-floor; VIRT ($61.05) is the notable liquid one
- `iv_rank_low`: OKLO, ALLY, JOBY, PTON, SMR, GEO, XLRE, BLSH, WEAV, ECHO (IVR 0)

## fz orthogonal candidate surface (ADVISORY, 0 rubric points)
⚠ **The `fz screen` bulk funnel has a known UPSTREAM doubled-first-letter ticker bug (20/20 rows corrupt).** Tickers below are DE-DOUBLED via company name. Per-ticker `fz_enrich` is healthy.
- `fz_rs` (new-high / RS leaders, C12-passing): **AMLX** +63.84% (Amylyx, $80.5M ADV), **HAE** +15.93% (Haemonetics, $74.5M), **TRGP** +7.13% (Targa, $323.4M), **HTFL** +7.84% (Heartflow, $61.6M), **CLMT** +5.09% (Calumet, $60.7M). Dropped sub-floor: XNCR, KURA, PAYS, SMJF, ATTO.
- `fz_squeeze` (short float > 20%): all rows returned corrupt tickers with sub-$50M-ADV profiles; **no C12-surviving squeeze candidate today** — treat lane as empty.

## HARD RULES FOR EVERY AGENT
1. **DO NOT re-fetch** `uw risk market-regime`, `uw playbook daily-synthesis`, `uw historical vrp`, `uw options-structure front-end-iv-ratio`, or ANY payload in the Step-0 cache. Read the cached file paths handed to you.
2. Cache dir: `analyses/daily/2026-08-18/step0_cache/` — files: daily_synthesis, market_regime, dte_volume_share, sector_flow, sector_flow_persistence, screener_bullish, screener_bearish, signal_confluence_bullish, signal_confluence_bearish, iv_rank_high, iv_rank_low, volume_vs_average, earnings_catalyst, expiry_heatmap, iv_outliers, greek_screener, top_premium_trades, most_active, oi_smart_positioning, single_leg, vrp_spy, vrp_qqq (all `.json`).
3. Every `uw` call: `uw <group> <sub> [--flags] --json --quiet`, pinned `--date 2026-08-18` where the tool is point-in-time.
4. **Prefer multi-day persistence tools over single-day snapshots** (`historical oi-trend` > `oi biggest-increases`; `hot-chains sweep-persistence` > `options-flow sweeps` for RANKING).
5. **Only analyse C12-PASSING names.** Sub-floor names are dropped, not discussed.
6. **`iv-rank` takes `--mode high|low`, NOT `--direction`.**
7. **NO FILE WRITES. NO WATCHLIST MUTATION.** Return your findings as your final message only.
8. `uw historical signal-backtest` is QUARANTINED for Phase 1 — do not call it.
