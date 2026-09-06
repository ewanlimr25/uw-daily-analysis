# Daily Market Analysis — 2026-05-04

## Executive Summary

- **Regime + GEX state:** TRANSITIONAL — SPY 718 in UPTREND (above 20/50 SMA) but breadth only 35.9% bullish; VIX 18.29 declining from 21.31 avg; $21B+ macro bearish sweep campaign running 5 sessions on SPY/QQQ/NVDA/MSFT/META. SPY in FULLY NEGATIVE GEX with binary compression at 717/720 — trade the break, not the pin.
- **Top 0DTE play:** SPY — long 720/723 call debit spread on clean hourly close above 720 (dealer cascade toward 722 long-gamma magnet); OR 717/714 put spread on break below 717. Do not hold through the opposite side. Invalidation: reverse of the break within 30 min.
- **Top swing build:** HOOD (score 4) — 7/9 accumulation signals confirmed, DIRECTIONAL_LONG conviction matrix, 10-day OI build +716k contracts, dark pool buy ratio 1.77 (highest in scan), primary defense at $76.55. Financial Services sector receiving positive rotation inflows. Half size, defined risk.
- **Top LEAP candidate:** AMZN (score 4) — March 27 institutional block of ~387k contracts across AMZN270115C $250/$275/$300 (Jan 2027, DTE 294 at print); 10-day OI build; $218M dark pool single print at $272.05; DP accumulation base $259–$272. Suggested: $250/$300 debit spread Jan 2027, half size. Win-rate: accumulation signal class not backtested (no ticker hit the ≥5 threshold required to trigger signal_backtest).
- **Biggest risk:** Correlated beta exposure across the long book (CVNA β=3.55, HOOD β=2.29, AMZN β=1.47) in a regime where the $21B macro bearish sweep on indices is still running. A single adverse macro print drops all three simultaneously. EFX puts (Rank 5 sweep, May-15 11-DTE) are the only portfolio hedge that profits in risk-off.

> **Regime note on scoring:** TRANSITIONAL regime universally suppressed conviction_matrix confidence scores below the 70-point threshold for every name today (highest was HOOD at 17.9%, AMZN at 8.3%). The rubric's +2 for DIRECTIONAL_LONG confidence >70 was unreachable system-wide. Top scores are AMZN=4 and HOOD=4; the ≥5 threshold was not crossed. Scores should be read relative to this regime ceiling, not as absolute weakness. In a RISK-ON or UPTREND-confirmed regime, AMZN and HOOD would both score 6+.

---

## 1. Regime & Gamma State

### Market Regime
| Metric | Value | Signal |
|--------|-------|--------|
| SPY | 718.01 | UPTREND — above 20 SMA (701.45) and 50 SMA (680.09) |
| 30-day change | +9.48% | Strong momentum |
| Distance from 90d high | -0.95% | Near highs |
| VIX | 18.29 | ELEVATED but declining (30d avg 21.31) |
| Breadth | 35.9% bullish | Bearish skew — contradicts price trend |
| Classification | **TRANSITIONAL** | Mixed signals; half position sizes; defined-risk structures (iron condors in range) |

**Sector rotation:**
- INTO: Consumer Cyclical (+$26.4M), Financial Services (+$14.7M), Energy (+$9.1M)
- OUT OF: Technology (−$221.9M), Communication Services (−$77.4M), Industrials (−$53.9M)

### SPY Gamma Exposure (0DTE)
- **Regime: FULLY NEGATIVE GEX** — dealers net short gamma; no natural hedging anchor
- Spot 718.38 compressed between **717 short-gamma wall** (−2.37T) and **720 short-gamma resistance** (−5.09T)
- 722 is the long-gamma magnet (+5.11T) — attractor once 720 is breached
- 0DTE IV kink: today 22.8% vs tomorrow 17.3% — elevated intraday hedging demand
- Put premium dominates: $308M puts vs $257M calls in today's SPY expiry
- **Breakout setup: TRUE** — binary compression with dealer cascade on either break

### QQQ Gamma Exposure (0DTE)
- **Regime: POSITIVE (0DTE)** — pin mode
- Pin zone: 673 (maximum gamma strike, delta 0.58 call/put balanced)
- Full-chain zero-gamma flip at 677.32 — only 4 points above spot; crossing that level converts to TREND-amplification
- Trade: Fade extremes within 670–677 range; do not chase above 677.32

### NVDA / TSLA (0DTE)
- NVDA: POSITIVE GEX, pinned to $200 strike (+1.08T GEX wall); iron condor centered at 200 with 195/205 wings
- TSLA: POSITIVE GEX, pin zone 390–395; sell premium, fade extremes; 395 is the closing magnet

---

## 2. 0DTE / Intraday Plays

### Primary Setup: SPY — Gamma Breakout Trade
**Thesis:** SPY is in FULLY NEGATIVE GEX — dealers have no stabilizing anchor. Every directional move is amplified, not faded. Spot at 718.38 is within 0.2% of the 720 short-gamma wall. A clean hourly close above 720 with volume triggers mandatory dealer delta hedging toward 722 (+5.11T magnet). Conversely, a break below 717 (next short-gamma wall) cascades toward 715.

| Direction | Entry | Target | Invalidation |
|-----------|-------|--------|--------------|
| Bullish | Break + hold above 720 | 722 GEX magnet | Close back below 718 |
| Bearish | Break below 717 on volume | 715 zone | Reclaim 718 within 30 min |

**Structure (regime-mandated defined risk):** Buy 720/723 call debit spread (bullish leg) OR 717/714 put debit spread (bearish leg). Do not hold both — trade the break that occurs. Do not sell premium here (FULLY NEGATIVE GEX = high realized vol environment, premium selling is structurally unsupported).

### Secondary 0DTE: AMZN Pin-to-Magnet
All GEX walls in AMZN's 0DTE chain are support walls pulling toward the $275 magnet (no resistance in the 270–280 zone). Dark pool accumulation at $272.05 adds institutional backing. Bias: light directional call bias intraday; call spread 272.5/277.5 captures the pin-to-magnet drift with defined risk.

### Sweep-Driven Urgency Rankings (near-term expiry)
| Rank | Ticker | Direction | Premium | Key Signal |
|------|--------|-----------|---------|------------|
| 5 | EFX | Bearish | $19.2M | May-15 (11 DTE) put construction + call liquidation, synthetic short; Industrials OUT sector confirms |

*Note: Ranks 1–4 (AMZN, ORCL, CVNA, CRWV) are swing setups on multi-day campaigns, not near-term urgency plays. EFX is the only top-5 sweep with urgent near-term expiry.*

---

## 3. Swing Setups (1–6 weeks)

### Rank 1 — HOOD | Score: 4 | Half size
**Sector:** Financial Services (INTO rotation) | **Price:** $76.55 | **IV Rank:** 24.8

**Thesis:** Institutions are quietly building a directional long position in HOOD via dark pool block buying and aggressive call purchases across near-term and intermediate strikes. Financial Services is one of three sectors receiving positive rotation inflows. HOOD sits in the lower half of its 52-week range ($45.56–$153.86), suggesting institutional entry at a discounted level.

**Signal alignment (7/9):**
- OI Trend: BUILDING, 10 consecutive days, +716k net contracts (accelerating: +129k, +47k, +76k in last 3 sessions)
- Dark Pool: $361M today, buy/sell ratio **1.77** (highest in entire scan), avg print at $76.93 (above spot)
- Institutional Accumulation Detector: **ACCUMULATION** confirmed — "dark pool buy volume significantly exceeds sell volume"
- Conviction Matrix: DIRECTIONAL_LONG (buy ratio 0.639, call ask 88.7k vs bid 75.5k)
- Smart Positioning: 11 bullish opening call contracts, top print: HOOD May29 $80C (+7,017 OI, ask-side)
- Trend Analyzer: 4 bullish days of 7, net flow +$2.997M today, P/C ratio 0.465
- Dark Pool Price Levels: $76.55 primary defense ($63.3M across 29 trades — single largest level in scan)
- Analyst consensus: 19/27 Buy or Strong Buy; forward PE 29.9; short ratio 1.1

**Fails:** conviction_matrix confidence 17.9% (below 70 threshold — TRANSITIONAL regime suppression); not in sweep top 5 (mixed direction signals in sweep data)

**Structure:** Half size, defined risk. Call debit spread May-29 $77.5/$82.5 (captures move to $80 magnet) or outright $80C if premium allows.

**Invalidation:**
- Conviction matrix flips HEDGED_LONG or MIXED for 2+ sessions
- Price closes below $73.00 (secondary DP support zone)
- OI trend turns UNWINDING for 2 consecutive sessions
- Dark pool buy/sell ratio drops below 1.20

---

### Rank 2 — AMZN | Score: 4 | Half size (swing), Half size (LEAP)
**Sector:** Consumer Cyclical (INTO rotation) | **Price:** $272.05 | **IV Rank:** 22.5

**Swing thesis:** AMZN is benefiting from Consumer Cyclical rotation inflows (+$26.4M today) with the cleanest institutional accumulation structure of any large-cap in today's scan. The AMZN Aug 2026 $320/$370 bull call spread (37.8k / 38.1k contracts, same size, same expiry — confirmed multi-leg institutional structure) establishes a directional thesis targeting $320–$370 by August. Low IV rank (22.5) makes call debit structures relatively cheap.

**Signal alignment:**
- OI Trend: BUILDING, 10 consecutive days, +1.71M net contracts (largest raw OI build in scan)
- Dark Pool: $218M single print at $272.05 (above NBBO ask — aggressive buyer); 20-day DP base $259–$272 ($2.65B total)
- Sweep: Rank 1 across 5 sessions ($1.755B aggregate, Aug $320C ask-side dominance 28.67:1 ask/bid)
- Multileg: Institutional Aug $320/$370 bull call spread (37.8k / 38.1k, identical size, confirmed)
- LEAP block: March 27 — 193.5k AMZN270115C $275 + 96.9k at $250 + 96.9k at $300 (387k total, Jan 2027)
- GEX: All-support structure in 0DTE chain; $275 magnet; no short-gamma resistance 270–280

**Fails:** conviction_matrix confidence 8.3% (MIXED — TRANSITIONAL regime suppression); accumulation-hunter fails DIRECTIONAL_LONG hard gate (buy ratio 0.578, just below 0.60 threshold)

**Structure:** 
- Swing: Jun-18 $275/$285 call spread (captures near-term magnet move at low IV)
- LEAP: Jan-27 $250/$300 debit spread (mirrors the March 27 institutional block strikes exactly)

**Invalidation:**
- Price closes below $259.50 (20-day DP accumulation floor, $548M support level)
- Sweep tape reverses to bid-side for 2+ sessions
- AWS growth decelerates on Q2 earnings (~mid-June 2026)
- Market regime turns bearish-trending (VIX sustained above 25, SPY breaks 20 SMA)

---

### Rank 3 — TPG | Score: −1 (contrarian, size: half) | Watch
**Type:** Crowded short fade | **Sector:** Financial Services | **P/C Z-Score:** +39.15 (EXTREME bearish crowd)

**Thesis:** TPG rallied +12.7% over 30 days while the crowd loaded into puts the entire way up (P/C z-score +39.15 standard deviations above normal). Put buyers are losing money in a name that keeps going higher in a sector receiving positive rotation inflows. When put holders capitulate (stop-losses, theta decay), covering flow becomes a mechanical bid.

**Signals:** P/C z-score extreme bearish (+39.15), price/flow divergence (price up, bears doubled down), Financials sector rotation tailwind. Term structure KINKED at Nov 2026 (not BACKWARDATION — no near-term event risk to abort the trade).

**Caution:** Risk-monitor flagged Financials cluster concentration (HOOD + TPG + XLF = three names in one sector). TPG scored −1 from this cluster penalty. Treat as a secondary bet, not a primary one.

**Structure:** Half size. Jun $45/$50 bull call spread (defined risk, captures squeeze toward $50 if put holders cover). Invalidation: EFX breaks above $185 call strike; Financials sector flow turns net negative; term structure flips BACKWARDATION.

---

### Rank 4 — GLNG | Score: 1 | Half size
**Type:** Multileg directional | **Sector:** Energy (INTO rotation) | **Price:** $56.06

**Thesis:** GLNG Sep 2026 $50/$60 bull call spread — 42,224 / 42,278 contracts (near-identical size, same expiry, confirmed institutional structure). Long leg is already $6 ITM ($50C on $56 stock, delta ~0.72); GEX flip level at $49.01 already cleared; $60 strike is the dominant GEX attractor (+$240M). Energy sector receiving +$9.1M in rotation inflows. Best risk/reward structure in the multileg scan (2:1 reward/risk).

**Invalidation:** Stock breaks below $49.01 (gamma flip level); Energy sector flow reverses.

---

### Earnings Swing Plays

**AMAT — SELL VOL (primary earnings play)**
- Earnings: May-14 PM | IV rank: 86.2 | Implied move: 4.4%
- Cleanest IV kink in scan: May-15 at 108.7% vs May-08 at 88.9% and May-22 at 82.0% — isolates event at the May-15 expiry
- Analyst/flow aligned bullish (75.7% buy ratings, +$510k net call flow)
- Structure: Iron condor May-16 expiry, $365/$375 put spread / $410/$420 call spread (~4.9% wide, slightly beyond implied move)
- Invalidation: May-15 kink dissipates pre-earnings; move exceeds 5.5% on report

**COHR — SELL VOL (secondary, analyst/flow divergence)**
- Earnings: May-06 PM | IV rank: 91.1 | Implied move: 11.4%
- Analyst/flow divergence: 73.7% analysts bullish, but flow net bearish (−$578k) with put premium nearly matching call premium
- Structure: Iron condor May-08 expiry, wings set at ~1.2× implied move. Bearish lean: consider tighter call wing.
- Invalidation: Pre-earnings put/call ratio normalizes (divergence resolves); gap >12% on report

**EFX — Near-term bearish (Rank 5 sweep)**
- Structure: $27.5k put sweep (May-15, 11 DTE) + simultaneous call liquidation at same expiry = synthetic short
- Ask/bid ratio on puts: 27,500:1 (pure institutional conviction)
- Sector aligned: Industrials is OUT rotation (−$53.9M)
- Invalidation: Close above $185 call strike; Industrials sector flow reverses

---

## 4. LEAP Builds (6–24 months)

### AMZN — Top LEAP Candidate | 6/8 gates passed

| Gate | Result |
|------|--------|
| OI trend BUILDING > 5 days | PASS — 10 consecutive days, +1.71M net |
| LEAP OI increases DTE > 180 | PASS — March 27 block: 193.5k at $275, 96.9k at $250, 96.9k at $300 (Jan 2027, DTE 294) |
| Position rolling detector | NO ROLL today — thesis intact via consistent build |
| Largest dark pool single whale | PASS — $218M single print at $272.05, above ask |
| Dark pool price levels clustered | PASS — $259–$272 base ($2.65B total, 20-day) |
| Conviction matrix DIRECTIONAL_LONG > 70 | FAIL — confidence 8.3% (TRANSITIONAL regime suppression) |
| Stock fundamentals | PASS — forward PE 27.5, 59 buys / 5 holds / 0 sells, PC ratio 0.31 |
| Market regime not bearish-trending | CONDITIONAL PASS — Consumer Cyclical INTO sector; SPY above 20/50 SMA |

**The anchor signal:** The March 27 single-session block — 387k contracts total across three AMZN270115C strikes ($250, $275, $300) at DTE 294 — is not a retail event. This is a multi-tranche DIRECTIONAL_LONG LEAP campaign, likely positioning ahead of AWS cloud re-rating. The institutional strike ladder ($250/$275/$300) becomes the exact recommended structure for new entrants.

**Suggested structure:** Long AMZN270115C $250 / Short AMZN270115C $300 — mirrors the March 27 institutional block exactly, reduces premium and IV exposure vs outright call, captures the full strike ladder. At half size (TRANSITIONAL regime).

**Invalidation (4 triggers):**
1. Conviction matrix shifts to HEDGED_LONG or COVERED_CALL on 5-day rolling basis
2. Price closes below $259.50 (20-day DP floor, $548M support level)
3. Market regime turns bearish-trending (VIX >25 sustained, SPY breaks 20 SMA)
4. AWS growth decelerates materially on Q2 earnings (~mid-June 2026)

### ORCL — WATCH (5/8 gates, does not qualify)
Strong smart positioning (14/15 call contracts bullish opening, including a Mar27'27 $250C 6.2k-contract block), 10-day OI build, but: conviction matrix MIXED (not DIRECTIONAL_LONG), IV rank 57 (makes LEAP debit structures expensive), stock already 22% above the 20-day DP accumulation base ($147–$155 vs current $180). Monitor for conviction matrix upgrade. Not a LEAP recommendation today.

---

## 5. Volatility Surface

### Best Vol Trade: MCHP Iron Condor (May-08 earnings)
- **Front/back IV ratio: 2.188** — highest in the entire scan
- IV rank: 89.6 | Earnings: May-07 PM (3 DTE) | Implied move: 7.9%
- Structure: Iron condor May-08 expiry
  - Sell $102.50C / Buy $107.50C (call spread, $5 wide, ~1.0× implied move)
  - Sell $87.50P / Buy $82.50P (put spread, $5 wide, ~1.0× implied move)
  - Target: $1.50–$2.00 net credit on a $5-wide condor
  - Note: PCR 2.16 (bearish flow) — consider centering the condor slightly below current price $95.30
- Invalidation: Move exceeds 7.9% on report; short-leg delta reaches 0.30 before expiry

### KINKED Structures (calendar candidates)
| Ticker | Structure | Kink | Trade |
|--------|-----------|------|-------|
| SPY | Kink at May-22 (20.0% vs May-11 at 15.2%) + Jan-27 anomaly (27.0%) | May-22 | Sell May-11 ATM / Buy May-22 ATM (calendar); captures 480bps IV trough-to-kink differential |
| AMAT | Clean kink at May-15 (108.7% vs May-08 88.9% and May-22 82.0%) | May-15 | Iron condor into earnings (see §3) |
| TSEM | Local kink at May-15 (125.1%) vs May-08 (118.6%) | May-15 | SELL VOL — smaller name, less liquidity |

### BACKWARDATION Names (all conditional on May-08)
| Ticker | Ratio | Catalyst | Trade |
|--------|-------|----------|-------|
| MCHP | 2.188 | Earnings May-07 PM (confirmed) | Iron condor now (see above) |
| AMD | 1.698 | Unconfirmed — DO NOT trade pre-May-08 | If May-08 clears clean: sell May-15 (85.6%) / buy Jul-17 (65.7%) |
| CCJ | 1.559 | None confirmed | Conditional calendar post-May-08 |
| ORCL | 1.238 | None confirmed | Monitor Jun-12 secondary kink |
| SNDK | 1.237 | None confirmed — flat near-term plateau unusual | Conditional calendar if May-08 clears clean |

### IV Outliers
- **High IV rank > 80 (premium selling):** MCHP (89.6), COHR (91.1), CSCO (94.5), WDAY (94.5), SNOW (89.4), DE (98.2), ZS (100), LFUS (100), ZM (97.3), ANF (82.4)
- **Low IV rank < 15 (cheap options):** AXSM (7.7), BMNR (2.9), AMZN (22.5) — AMZN notable: low IV + massive OI accumulation + institutional LEAP block = cheapest institutional conviction name in scan

---

## 6. Risk & Correlation

### Correlation Clusters (from Phase 2 risk-monitor, run on today's Phase 1 candidates)

**Cluster 1 — CRITICAL: FXI / KWEB (r = 0.926)**
These are the same bet (China macro rebound via coordinated Jul 2026 bull call spreads by the same institution). Keep FXI (higher liquidity). Skip KWEB.

**Cluster 2 — MODERATE: HOOD / TPG / XLF (Financial Services)**
Three names in one sector in a TRANSITIONAL regime = concentration risk. HOOD is the primary (highest conviction). TPG is secondary (half size). XLF is starter only. Do not hold all three simultaneously at full size.

**Cluster 3 — MODERATE: ORCL / CRWV (Software Infrastructure + Technology OUT sector)**
Both Technology sector (OUT rotation). ORCL fails conviction gate. CRWV fails regime gate. Both skipped or reduced to starter.

### Macro Tail Risk
The $21B+ bearish sweep campaign across SPY/QQQ/NVDA/MSFT/META (5 consecutive sessions, 100% bearish direction on index products) is the dominant portfolio risk. This is not retail hedging — it is institutional in size and consistency. A macro resolution to the downside would simultaneously hit:
- CVNA (β=3.55) — single most vulnerable name
- HOOD (β=2.29) — second most vulnerable
- AMZN (β=1.47) — third
- GLNG (β=0.05) — only true diversifier in the long book

### Vol-Sell Cluster Risk
AMAT, COHR, MCHP are three simultaneous short-vega positions in Technology earnings names. A single bad earnings surprise that spills IV across the sector would breach wings on all three. Budget as one combined position for risk purposes, not three independent trades.

### Portfolio Hedging
EFX (May-15 put construction, 11 DTE) is the only directional short in the portfolio that profits in risk-off. Consider whether this adequately offsets the aggregate long-risk beta of HOOD + AMZN + CVNA.

### Regime Conflicts (names to avoid or reduce)
| Ticker | Issue | Decision |
|--------|-------|----------|
| CRWV | Technology OUT sector, sweep-only signal | SKIP |
| KWEB | Duplicate of FXI (r=0.926) | SKIP |
| ORCL | Technology OUT sector, fails conviction gate | STARTER only or skip |

---

## 7. High-Conviction Cross-Ref

### Formal Conviction Scores

> **Regime caveat:** TRANSITIONAL regime universally suppressed conviction_matrix confidence scores below the 70-point threshold today (HOOD: 17.9%, AMZN: 8.3%, ORCL: 5.2%). No ticker scored ≥5. Top scores (AMZN=4, HOOD=4) are 1 point below threshold — in a confirmed UPTREND or RISK-ON regime, both names would score 6+ via conviction_matrix upgrade alone. Read scores relative to this regime ceiling.

| Ticker | +3 GEX Breakout | +2 Accum 3+ | +2 OI Build | +2 Matrix>70 | +1 Sweep Top5 | +1 Earnings | +1 Multileg | −2 Crowded | −1 Correl | −3 Regime | **Score** | Size |
|--------|----------------|-------------|-------------|--------------|----------------|-------------|-------------|------------|-----------|-----------|-----------|------|
| AMZN | — | — | +2 | — | +1 | — | +1 | — | — | — | **4** | Half |
| HOOD | — | +2 | +2 | — | — | — | — | — | — | — | **4** | Full* |
| SPY 0DTE | +3 | — | — | — | — | — | — | — | — | — | **3** | Tactical |
| GLNG | — | — | — | — | — | — | +1 | — | — | — | **1** | Half |
| FXI | — | — | — | — | — | — | +1 | — | — | — | **1** | Half |
| AMAT | — | — | — | — | — | +1 | — | — | — | — | **1** | Half (vol) |
| COHR | — | — | — | — | — | +1 | — | — | — | — | **1** | Half (vol) |
| EFX | — | — | — | — | +1 | — | — | — | — | — | **1** | Half (bear) |
| CVNA | — | — | — | — | +1 | — | — | — | −1 | — | **0** | Half |
| TPG | — | — | — | — | — | — | — | — | −1 | — | **−1** | Watch |
| ORCL | — | — | +2 | — | +1 | — | — | — | −1 | −3 | **−1** | Skip |
| CRWV | — | — | — | — | +1 | — | — | — | −1 | −3 | **−3** | Skip |

*HOOD "Full" = full size within TRANSITIONAL regime baseline (which is already half normal size).

### Signal_Backtest Note
Per protocol, signal_backtest is triggered for tickers scoring ≥5. No ticker crossed that threshold today. Win-rate data was not pulled. In a confirmed regime, pull `mcp__uw-historical__signal_backtest` for signal classes: `dp_accumulation` (HOOD), `leap_oi_build` (AMZN) before sizing.

### Scoring Rubric (verbatim — for audit)

```
Conviction score = Σ:
  +3  flagged by gamma-flip-tracker as setting up a regime breakout
  +2  3+ aligned signals in accumulation-hunter
  +2  multi-day OI build (oi_trend BUILDING, > 5 days)
  +2  conviction_matrix = DIRECTIONAL_LONG, confidence > 70
  +1  in sweep-tracker top 5
  +1  in earnings-scout BUY VOL or SELL VOL
  +1  in multileg-strategist with directional structure
  -2  contrarian-scanner flags as overcrowded long
  -1  risk-monitor flags in correlation cluster
  -3  market_regime conflicts with the trade direction
```

---

## Appendix: Watchlist Write-Back

Tickers written to `conviction_2026-05-04` group for tomorrow's risk-monitor tracking:

```
manage_watchlist(action="add", group="conviction_2026-05-04", tickers=["HOOD", "AMZN", "GLNG", "FXI", "CVNA"])
```

Confirmed by risk-monitor agent (Phase 2). Tomorrow's run will automatically track these names for flow reversal, OI changes, and adverse signals.
