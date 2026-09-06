# Daily Market Analysis — 2026-05-15

*Monthly OPEX Friday. Two-phase agent fleet: 11 Phase 1 specialists + Phase 2 quant + risk-monitor. Watchlist write-back to `conviction_2026-05-15`.*

---

## Executive Summary

- **Regime + GEX:** TRANSITIONAL UPTREND. SPY 739.17 (+5.35% 30d, -1.38% from 90d high). VIX-adjacent IV30 15.4% vs RV30 11.9% → VRP **FAIR (+3.5pt)**. Breadth **35.9% bullish — bearish skew under uptrending tape, classic late-cycle divergence**. DTE share 0DTE 44% / wk 22% / mo 20% / LEAP 5% → **RETAIL_DRIVEN**. Indices fully short-gamma inside 45d (SPY ZGL ~744, QQQ ZGL ~710, IWM ZGL ~278 — all NEAR_FLIP or trending). Sectors: ALL 11 persistence_score=1 INFLOW (broad bid, not rotation); Tech + Consumer Cyclical DECELERATING into OPEX.
- **Top 0DTE play:** **EEM iron fly @ 65** (half size). +$10.4B long-gamma at strike, dist 0.12%, OI 185k — HIGHEST-conviction OPEX trade on the board. Backup: **IBIT iron fly @ 45** (+$446B monster wall, dist 0.40%, half size).
- **Top swing build:** **ETN LONG starter** — raw conviction 10, three load-bearing tools cited (DP block-stratified mega 100% buy, cum_premium_flow 10d +$16.6M BULLISH, insights_institutional_accumulation DIRECTIONAL_LONG). $244M dark-pool day @ avg $398.82 with close $400.11 — institutions buying the LOW of the 10d range. Industrial-electrification capex thesis, immune to Tech-slowdown gate.
- **Top vol play:** **SNOW long 5/29 ATM straddle full size** — earnings 5/27, term-structure KINKED@5/29 vs CONTANGO back-month, **implied 0.33% vs 13% historical earnings move (-95% mispricing)**. VRR proxy 0.867 → full size on defined-risk debit structure.
- **Top LEAP candidate:** **NONE qualified.** Strict 6/9 gate stack collapsed on `insights_conviction_matrix` MIXED across the board. Strongest near-misses (4/9): AAPL (90d cum flow +$449M), TSM (+$564M). Wait for post-OPEX clarity.
- **Biggest risk:** **AI/Semis cluster** (NVDA/AMD/SMH/TSM/AVGO corr 0.54–0.79). Risk-monitor skipped TSM, SMH, AMD-cash long and NVDA cash-long entries on Tech-slowdown + regime gates. The IWM Jun-18 put-diagonal stack ($95M, 4-of-5d) is the institutional hedge tell — buy-side paying up for small-cap insurance while indices grind higher. Optional hedge sleeve: **SPY 735/725 PutSpread next-week, 10% of book notional**.

---

## 1. Regime & Gamma State

`risk_market_regime`: **TRANSITIONAL — Mixed signals, reduce position size, wait for clarity**. SPY UPTREND, above 20SMA (723.80) + 50SMA (690.04). Breadth bearish-skewed (3,949 bearish-flow tickers vs 2,207 bullish-flow — 35.9% bullish). Sector rotation (per `risk_market_regime`): money in → Communication Services, Consumer Defensive, Energy; money out → Consumer Cyclical, Financial Services, Technology. (Caveat: gross-premium `sector_flow` shows ALL sectors net-positive — the regime tool reads share-of-flow direction, not absolute premium.)

**Per-index gamma snapshot (0–45d):**

| Ticker | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 739.17 | ~744 | -12.5T | NEGATIVE / NEAR_FLIP | 742 → 745 | 738 → 739 |
| QQQ | 708.86 | ~710 | -4.1T | NEGATIVE | 712 → 715 | 710 → 709 |
| IWM | 277.57 | ~278 | -2.5T | NEGATIVE | 280 (+1.3T support wall) | 278/277/276 stacked |

`options_flow_dte_volume_share`: 0DTE 44% / weeklies 22.1% / monthlies 19.8% / LEAPs 5.4% — RETAIL_DRIVEN hint. Heavy 0DTE share means dealer hedging dominates intraday flow; the institutional swing setups live in monthly+ which is only 25% of the tape.

`historical_vrp` (SPY): IV30d 15.4%, RV30 11.9%, **VRP +3.5pt = FAIR**. No sweeping vol-bias edge market-wide, but single-name VRP is **wide-positive on NVDA (+10.9pt), SMH (+11pt), MU (+8.9pt)** per vol-surface-scout — front-back calendars favored on the chip complex.

---

## 2. 0DTE / Intraday Plays

`gamma-flip-tracker` and `opex-pin-strategist` agree the OPEX-day book has three clean trades and two structural fades. Two named agents disagree on AAPL — resolution below.

### Tradeable OPEX-day pins (long-gamma confirmed)

| Ticker | Pin | Spot | Dist% | GEX@pin | Structure | Size | Invalidation |
|---|---|---|---|---|---|---|---|
| **EEM** | 65 | 65.18 | 0.12 | **+$10.4B LONG** | Iron fly 63/65/67 | half | Spot > 65.7 or < 64.3 |
| **IBIT** | 45 | 44.82 | 0.40 | **+$446B LONG (monster)** | Iron fly 43/45/47 | half | IBIT > 46 or < 44; BTC vol spike |
| **WBD** | 27 | 27.00 | 0.00 | Pending standalone GEX | Iron fly 26/27/28 | starter | Spot > 28 or < 26 |
| **AAPL** | 300 | 300.37 | 0.12 | **+$6.5B LONG support wall** (per gamma-flip-tracker); opex-pin-strategist counters with "flat gamma at strike, no enforcing wall" | Iron fly 297.5/300/302.5 — sized starter due to agent disagreement | starter | Spot > 302.5 or < 297.5 |

**Disagreement resolution (AAPL):** gamma-flip-tracker per-strike GEX shows +$6.5T at 300, +$2.7T at 302.5 — dealers ARE long gamma at the pin. opex-pin-strategist's "flat" read appears to discount the per-strike wall in favor of net 5d gamma series. Position: **the iron fly is tradeable but smaller (starter, not half)** to discount the disagreement.

### Structural fades (the pin breaks)

| Ticker | Pin | Spot | Reason fade | Trade |
|---|---|---|---|---|
| **HYG** | 79 | 79.61 | FULLY_NEGATIVE regime; 80 strike is a **-$1.46T short-gamma cliff**, not a magnet | Long 79.5/81 call spread (cheap dealer-amplified upside) |
| **XLF** | 51 | 51.18 | Pin is **short-gamma valley** (-$49B at 51); long-gamma walls live at 51.5/52 (+$15.9B combined) | Long 51.5/52.5 call spread |

### Urgency-ranked 0DTE / weekly sweeps

| Ticker | Persistence | 5d premium | Side | Action tomorrow |
|---|---|---|---|---|
| **TSLA** | 5/5 | $9.95B | BEARISH | See §3b — primary actionable short |
| **SPY/QQQ/SPXW** | 5/5 each | $7.4B–$7.9B | BEARISH | Index-hedge backdrop, NOT a directional trade |
| **MSFT** | 5/5 | $1.18B | BEARISH | CONTRA_FLOW vs bullish-list ($98M net flow today) — institutional putters dominating — see §3 |
| **AMZN/GOOGL** | 5/5 each | $490M / $461M | BEARISH | §3b actionable shorts |

---

## 2a. Swing Dealer Positioning (1–4 weeks)

**OPEX-day caveat:** every name flipped to FULLY_NEGATIVE GEX on 5/15 — these are OPEX artifacts, not regime flips. Read 5/13–5/14 as the operative state.

| Ticker | DEX | Vanna | ZGL Δ5d | Regime flip? | Front-end IV | Bias | Conv |
|---|---|---|---|---|---|---|---|
| **SPY** | -45.6T (improving) | TRUE put-heavy + falling VIX | rising | YES 5/14 NEG→POS | 1.69 (0DTE artifact) | **LONG** | HIGH |
| **QQQ** | -16.6T (improving) | TRUE put-heavy | rising sharply | YES 5/14 NEG→POS | 0.86 contango | LONG | HIGH |
| **NVDA** | +76T (rocket, call_dex 90T) | call-heavy SHORT | 5d GEX 1.6T→11.6T (7x) | no flip; sustained POS | 0.12 contango | LONG continuation | HIGH (cash skip — Tech slowdown gate) |
| **AAPL** | +46.2T (rising) | call-heavy SHORT | GEX 690B→10.3T | clean POS | n/a | LONG | HIGH (cash skip — Tech slowdown gate) |
| **MSFT** | +34.4T | call-heavy | flip POS 5/14, $190 ZGL | YES 5/14 NEG→POS | n/a | LONG (but volatile, 7 flips/15d) | MED-HIGH (skip — Tech + flow_conflict) |
| **SMH** | **-0.61T (NEG)** | **TRUE vanna squeeze** — only name w/ neg DEX + pos vanna | persistently FULL_NEG | none | **3.27 BACK (extreme panic)** | LONG **squeeze setup** | HIGH (skip — Tech slowdown) |
| **AMD** | +0.57T (weakening) | call-heavy SHORT setup | first FULL_NEG 5/15 | post-OPEX risk | 0.16 contango | NEUTRAL-SHORT | MED (skip — cluster + flow_conflict) |
| **TSLA** | +18.5T (peaked 5/13) | DISAGREES — call-heavy SHORT setup, but DEX still POS | rolled $447→$426 | post-OPEX risk | **1.90 BACK (vol panic!)** | NEUTRAL — divergence | MED |
| **IWM, TSM, AVGO, SOXL** | multi-flip chop | disagreement | erratic | noise | n/a | NEUTRAL | LOW |

**Highest-conviction swing setups (dealer-positioning):** (1) SPY LONG vanna-squeeze 1-3wk target $755–760; (2) SMH LONG squeeze — but skipped on Tech-slowdown gate; (3) NVDA LONG continuation — cash skipped, vol-leg full size.

---

## 2b. Sector Rotation

**Regime call: NO_CHANGE. Broad bid, no actionable rotation.** All 11 sectors registered persistence_score=1 INFLOW over 5 days — that's a broad bid, not a rotation. The diagnostic edge is the day-over-day trajectory, which is decelerating across the size-leaders:

| Sector | Today $M | 5d avg $M | Trajectory | Read |
|---|---|---|---|---|
| Technology | 5,439 | 7,334 | **SLOWING (-52% wk/wk, 11.4B Mon → 5.4B today)** | Mega-cap call premium decaying |
| Consumer Cyclical | 817 | 1,426 | **SLOWING (-62% off mid-week)** | RCL PCR 7.35 = protective hedging, not fresh longs |
| Industrials | 417 | 536 | SLOWING monotonic 5d decline | — |
| Healthcare | 200 | 385 | SLOWING (-61% off 5/14) | — |
| Consumer Defensive | 100 | 123 | **STEADY (+138% vs 5/14)** — only sector with positive d/d delta of size | PEP, MNST, HRL leaders — too small in absolute size (+$58M) to confirm rotation |
| Utilities | 52 | 54 | STEADY | OKLO/VST AI-power thematic, not classic defensive |
| Energy | 183 | one-day 5/14 spike to 1,151 | **CAPITULATION REVERSAL** — single-day spike fully reversed | Not durable |

**Action:** trim Tech / Consumer Cyclical longs into OPEX strength. Run **small PEP/MNST tactical defensive starter (≤25 bps each)**. Re-evaluate Tuesday 2026-05-19 post-OPEX.

---

## 3. Swing Setups (1–6 weeks)

### 3a. Long swings (regime-aligned, defined-risk preferred)

| # | Ticker | Score | Final size | Thesis | Structure | Invalidation |
|---|---|---|---|---|---|---|
| 1 | **ETN** | 10 (HIGH) | **starter** | Industrial-electrification capex play. $244M DP @ avg $398.82 (close 400.11), mega-tier 100% buy ratio at $408.10 anchor. OI BUILDING 5/5d into Jun 410/430C + Jul 480C. 10d cum_flow +$16.6M BULLISH. Conviction_matrix DIRECTIONAL_LONG (conf 18.96). 8/2 bullish flow days last 10. Next earnings 8/4 (no earnings risk). | Long Jun-18 410/430 call vertical OR Jul 480C lottery sleeve. IV rank 53 = cheap options. | Close < $401.53 OR conviction_matrix flips to HEDGED_LONG OR mega-tier disappears from tape. |
| 2 | **IBIT** | 5 → MEDIUM | **half (pin)** | OPEX iron fly @ 45 — +$446B long-gamma monster wall, dist 0.40%, OI 97k. Defined-risk pin trade. | Iron fly 43/45/47, today's expiry. | IBIT > 46 or < 44. BTC vol spike. |
| 3 | **PEP** | 5 → MEDIUM | **starter** | Defensive bid leader, $24M whale Sep-18 155C / 170C bull vertical ($31.6M aggregate, ratio 0.97). Sector-rotation single-name defensive #1. PCR 0.08 extreme call-heavy. | Sep-18 155/170 bull call vertical. | Sector defensive trajectory reverses; close < $145. |

**Skipped after risk gates (Tech slowdown + cluster overlaps):** NVDA cash-long (raw 9, score-rank #2), AAPL (raw 8), MSFT (raw 5 contested), TSM (raw 5), SMH vanna squeeze (raw 6). These names are real but the regime asymmetry says half size or skip. **Vol-leg expressions of NVDA + META are full-size in §5**.

### 3b. Short / fade swings (defined risk only)

| # | Ticker | Score | Final size | Thesis | Structure | Invalidation |
|---|---|---|---|---|---|---|
| 4 | **IWM (short via put-diagonal)** | 6 (HIGH) | **starter** | multileg-strategist HIGHEST CONVICTION institutional theme: $95M aggregate put-diagonal stack 4-of-5d persistence (265P Jun18 / 275P May29 / 270P May27 / 275P May20). Cum_flow_30d **-$1.01B BEARISH (direction-aligned)**. Small-cap downside insurance while indices grind higher. | Long IWM Jun-18 270P / Short May-29 275P diagonal. ~$1.20-1.40/share debit. | IWM > 290 with sector breadth confirming OR multi-day call build flips the pattern. |
| 5 | **TSLA** | 6 → MEDIUM | **starter** | sweep-tracker EXTREME CONVICTION: 5/5 bearish persistence, $9.95B 5d aggregate. Bearish-list leader. cum_flow_30d +$1.04B BULLISH = **flow_conflict (-2 applied)** — desk-honest read: tactical short into earnings cycle, not a hold. | Long Jun-18 410/400 put debit spread. | TSLA closes Mon > today's high OR sweep persistence drops below 3/5. |
| 6 | **GOOGL** | 5 → MEDIUM | **starter** | 5/5 bearish sweep persistence $461M. cum_flow_30d -$98.9M BEARISH (direction-aligned). | Long Jun-18 390/380 put debit spread. | Directional flip in sweep tape OR close > $402. |
| 7 | **QCOM** | 4 | **starter** | 4/5 bearish sweep persistence $685M + today's $750k put sweep ratio 0.86 + SMH 5/22 500P $48.8M corroboration. cum_flow +$123M BULLISH = flow_conflict applied. | Long Jun-18 195/185 put debit spread. | SMH 500P pile collapses OR QCOM holds 195. |
| 8 | **AMZN** | 4 | **starter** | 5/5 bearish sweep $490M, bearish-list flow $24M net. | Long Jun-18 260/250 put debit spread. | Directional flip in sweep tape. |

**Reclassified to LONG-fade then skipped on cluster:** RCL bull-put-spread (contrarian saw +1.75σ put-bid extreme, but IWM correlation 0.626 cut it).

---

## 4. LEAP Builds (6–24 months)

**ZERO qualified candidates.** Strict 6/9 signal-gate stack collapsed on `insights_conviction_matrix` — every candidate returned MIXED with confidence < 10%. OPEX-day roll flow dominates the LEAP-grade signature.

**Top near-misses (4/9 gates passed) — journaled for re-evaluation post-OPEX:**

| Ticker | Gates | Block | Note |
|---|---|---|---|
| **AAPL** | 4/9 | Conviction matrix MIXED 8.74% (spec requires > 70%) | 90d cum_flow **+$449M BULLISH** — slow accretion present. OI BUILDING 10/10. DP buy/sell 1.42. The conviction-matrix gate is unforgiving; flow not yet directionally one-sided enough. |
| **TSM** | 4/9 | Conviction MIXED 0.76% | 90d cum_flow **+$564M BULLISH** (smooth accretion). OI BUILDING 10/10. LEAP OI is hedged (261218 C $580 + P $400) — direction is hedge-pair, not directional. |
| NVDA | 3/9 | Cum_flow 90d MIXED + accumulation NEUTRAL | Single LEAP whale 280616 C $215 ($64M premium) is LEAP-grade tell, but today's OI dominated by 0-7DTE — short-horizon flow. |
| IBIT | 2/9 | Two-sided LEAP build (P $30 hedge), cum_flow -$31M | Hedge structuring, not directional accumulation. |
| TLT | 3/9 | Mixed call/put same day = pin-spread, no direction | — |

**Verdict:** Re-run LEAP scan 2026-05-22 (after post-OPEX roll-flow noise clears) — AAPL or TSM may reset to 5–6/9 once 30d cum_flow trend_direction clarifies out of MIXED.

---

## 5. Volatility Surface

The strongest desk-wide vol trades come from **single-name VRP positives + earnings-week KINKED expiries**:

### Headline calendars (defined-risk, full size on VRR 0.867)

| # | Ticker | Earnings | Structure | Mispricing | Rationale |
|---|---|---|---|---|---|
| 1 | **SNOW** | 5/27 | Long 5/29 ATM straddle (or 5/22 sell / 5/29 buy diagonal) | **-95% (0.33% implied vs 13% historical)** | KINKED@5/29 95–107% vs CONTANGO back-month; back-skew COMPLACENT (-0.03) = tail not priced. **Highest-EV vol play this week.** |
| 2 | **NVDA** | **5/20 (Wed!)** | Long 5/22 / Short Jun-18 ATM debit calendar | KINKED May-22 +51% over Jun neighbor; single-name VRP **+10.9pt** | **Earnings is 3 trading days away.** 5/22 240C OI built +29.4k contracts, 250C +45.6k — institutions positioning LONG into earnings. Front-IV crush + modest spot move = both sides of the calendar pay. |
| 3 | **TTWO** | 5/21 | Long 5/22 ATM straddle | -90% (0.69% implied vs 7% historical) | KINKED@5/22 100% vs 5/29 77%. Skew TAIL_HEDGING 1.35 = downside hedged. Tape-priced bullish $24M whale flow corroborates. |
| 4 | **OKTA** | 5/28 | Long 5/29 ATM straddle | -95% (0.44% implied vs 10% historical) | KINKED@5/29 95% vs 6/5 88%, CONTANGO surface. Cluster-cut to half (corr 0.738 vs SNOW). |
| 5 | **META** | (no near event) | Long 5/29 / Short Jul-17 ATM debit calendar | KINKED 5/29 65.2% vs 5/22 40.9% (+24pt) | Probable FTC/AI hearing or product event ~5/29. Cluster-cut to half (corr 0.609 vs NVDA). |

### Sell-vol setup (half size, defined-risk only)

| Ticker | Earnings | Structure | Rationale |
|---|---|---|---|
| **DE** | 5/21 | 5/22 short iron condor ±4% wings | KINKED but **back-skew COMPLACENT** (0.006) = SELL VOL gate; implied 0.44% vs 5q avg 5%, but defined-risk only per VRP FAIR regime. |

### BACKWARDATION false positives

`TSM 0DTE 186.7% vs 5/22 56.7%` and `SMH 0DTE 168.7% vs 5/22 66.0%` are mechanical expiry-day artifacts, NOT panic. Excluding the 0DTE point, every surface is CONTANGO. **PATIENT_WAIT — do NOT trade SMH/TSM calendars on the OPEX-day front-end spike.**

---

## 6. Risk & Correlation

`risk_portfolio_correlation` against today's candidate union surfaced these clusters (corr > 0.7 = treated as one position):

| Cluster | Tickers | Correlation | Action |
|---|---|---|---|
| Crypto-beta | IBIT / MSTR | 0.843 | KEEP IBIT (pin, defined-risk). DROP MSTR (flow_conflict + lower raw). |
| Semis | AMD / SMH (0.793), SMH / TSM (0.684), AMD / TSM (0.543) | high | KEEP SMH (highest score). DOWNSIZE TSM to skip. AMD-short kept (opposite direction). |
| Small-cap/risk-on | IWM / SMH (0.748), IWM / MSTR (0.669), IWM / RCL (0.626) | high | KEEP IWM-short (only viable directional short with LB=2). DOWNSIZE RCL → skip. |
| Vol-long SaaS | OKTA / SNOW (0.738), MSFT / SNOW (0.55) | high | KEEP SNOW (raw 7). DOWNSIZE OKTA → half. |
| Mega-cap Tech beta | NVDA / TSM (0.627), NVDA / META (0.609) | medium | KEEP NVDA (vol-leg). META-vol-leg → half. TSM dropped above. |
| Industrial cyclical | DE / ETN | 0.654 | KEEP ETN. DE-iron-condor kept (opposite vol-bias). |

**Adverse watchlist exits from prior conviction group:** **CSCO** (flow_direction bearish despite call-heavy P/C 0.23 — flow reversal) and **NBIS** (net_flow -$8.2M bearish, off-thesis decay) flagged for **EXIT**. NVDA flow_direction also bearish today (-$42.6M) despite OI build — risk reduced, not exited.

**Hedge sleeve:** Net book delta ≈ +0.3 long (4 long-cash starters, 2 shorts, 5 vol-longs delta-neutral). Below 0.6 hedge threshold — **no mandatory hedge**. **Optional opportunistic: SPY 735/725 PutSpread next-week expiry, sized 10% of book notional**, justified by breadth divergence (35.9% bullish under uptrending tape).

---

## 7. High-Conviction Cross-Ref (score ≥ 5)

`signal-confluence-quant` audit trail per ticker. `Step 3a HIGH-tier gate`: any raw ≥ 5 with `load_bearing_count < 2` demoted to MEDIUM. Load-bearing tools = `{dark_pool_block_stratified, historical_cumulative_premium_flow, insights_institutional_accumulation, options_structure_dex}`.

| # | Ticker | Raw | LB | Tier | Dom Signal | WR/VRR | Pre-risk | Gates Applied | Final | Invalidation |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ETN** | 10 | 3 | HIGH | dark_pool_accumulation | 0.40 | starter | — | **starter** | < $401.53 OR conviction flips |
| 2 | NVDA-cash | 9 | 3 | HIGH | gamma_breakout | 0.40 | starter | regime -1, Tech-slow -1 | **skip** (vol-leg full) | DEX trajectory rolls neg 3+ sessions |
| 3 | AAPL | 8 | 3 | HIGH | gamma_breakout | 0.40 | starter | regime -1, Tech-slow -1 | **skip** | break < $295 |
| 4 | **SNOW** | 7 | 0 | MED (demoted LB) | vol_kink/earnings | 0.867 | full | — | **full** | 5/29 IV bleeds < 5/22 + 6/5 avg |
| 5 | MA | 6 | 3 | HIGH | dark_pool_accum | 0.40 | starter | flow_conflict -1 | **skip** | cum_flow stays neg 2+ sessions |
| 6 | **TTWO** | 6 | 0 | MED (LB) | vol_kink/earnings | 0.867 | full | — | **full** | 5/22 IV < 5/29 (kink dissipates) |
| 7 | **OKTA** | 6 | 0 | MED (LB) | vol_kink/earnings | 0.867 | full | cluster -1 | **half** | net flow flips sharply bearish |
| 8 | TSLA | 6 | 1 | MED (LB) | multi_day_sweep | 0.478 | starter | — | **starter** (SHORT floor) | sweep < 3/5 OR Mon > today's high |
| 9 | **IWM** | 6 | 2 | HIGH | multileg_directional | 0.478 | starter | — | **starter** | IWM > 290 with breadth |
| 10 | SMH | 6 | 1 | MED (LB) | vanna_squeeze | 0.40 | starter | regime -1, Tech-slow -1 | **skip** | front-end IV > 4.0 (still building) |
| 11 | GOOGL | 5 | 1 | MED | multi_day_sweep | 0.478 | starter | — | **starter** | sweep tape flips |
| 12 | MSFT | 5 | 2 | HIGH | gamma_breakout | 0.40 | starter | regime -1, Tech-slow -1, flow_conflict -1 | **skip** | bullish-list rejoins; CONTRA_FLOW dies |
| 13 | RCL | 5 | 1 | MED | bull_put fade | 0.40 | starter | cluster -1 | **skip** | put-bid extreme reverses |
| 14 | **NVDA-vol-calendar** | 5 | 0 | MED (LB) | vol_kink | 0.867 | full | — | **full** | 5/22 IV crush fails to materialize |
| 15 | META-vol | 5 | 0 | MED (LB) | vol_kink | 0.867 | full | cluster -1 | **half** | 5/29 kink dissipates |
| 16 | DE | 5 | 0 | MED (LB) | earnings_vol_sell | 0.867 | half | — | **half** (defined-risk IC) | implied move repriced higher |
| 17 | **PEP** | 5 | 1 | MED | multileg_directional | 0.40 | starter | — | **starter** | sector defensive reverses, < $145 |
| 18 | **IBIT** | 5 | 0 | MED (LB) | pin | 0.667 | half | — | **half** (pin) | IBIT > 46 or < 44 |
| 19 | TSM | 5 | 1 | MED | bullish_flow | 0.40 | starter | regime -1, Tech-slow -1, cluster -1 | **skip** | post-OPEX flow direction clarifies |
| 20 | MSTR | 5 | 1 | MED | bearish_flow fade | 0.478 | starter | cluster -1, flow_conflict -1 | **skip** | — |

**Post-risk book (bolded names above) — actionable today:**

- **Long starters:** ETN, PEP
- **Short starters:** IWM (put-diagonal), TSLA, GOOGL, QCOM (raw 4), AMZN (raw 4)
- **Vol-long full size:** SNOW, NVDA-calendar, TTWO
- **Vol-long half size:** OKTA, META-calendar
- **Vol-short half size:** DE iron condor
- **Pin half size:** IBIT
- **Pin starters:** EEM, WBD, AAPL (downsized for agent disagreement)
- **Pin fades:** HYG (call spread), XLF (call spread)

### Conviction scoring rubric (Step 4 — embedded verbatim for audit)

```
Daily conviction score = Σ:
  +3  dealer-positioning DEX flip / vanna squeeze in trade direction
  +2  3+ aligned accumulation signals (DP + OI + smart_positioning, dark_pool_block_stratified institutional-tier confirmed)
  +1  multi-day OI build (historical_oi_trend BUILDING, lookback ≥ 5d)
  +2  insights_conviction_matrix DIRECTIONAL_LONG confidence > 70
  +2  historical_cumulative_premium_flow net directional accretion (30d) in trade direction
  +1  in sweep-tracker top 5 by hot_chains_sweep_persistence
  +1  sector-rotation single-name leader (persistence ≥ 3)
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-anchored)
  +1  vol-surface-scout KINKED/BACKWARDATION with VRP-aligned bias
  +1  opex-pin-strategist ranks top-5 (OPEX week only)
  -2  contrarian flags overcrowded long with rising pc_zscore in positive VRP
  -2  flow_conflict (cum_premium_flow contradicts dominant signal class)
  -1  risk-monitor correlation cluster (corr > 0.7) — applied in 2b
  -3  regime conflicts trade direction — applied in 2b
```

---

## 8. Watch-only — single signal, no confluence

Phase 1 surfaced these but they failed the Step 3 confluence gate (only one Phase 1 agent flagged them OR confluence_score < 4). Journaled for tomorrow's correlation check; **not actionable today**.

**Bullish singles:** BOOT (confluence=6, single sector-rotation tag), DXCM (confluence=6 healthcare), STAA (confluence=6 healthcare), HPE-fade-watch (bearish confluence=6 but contradicts breadth thesis), MNST (raw 4 → starter, marginal).

**Bearish singles:** SMH (confluence=5 but ABORTED by contrarian due to full-curve BACKWARDATION = event-driven), INV (confluence=5 financial), ESI (confluence=5 basic mat), MTUM (confluence=5 ETF), ADI (confluence=5 tech earnings-proximate).

**Vol speculation flagged but not earnings:** **GTLB** — IV-100 + 188% 5/22 single-week spike + 2x volume + 0.14 P/C is NOT classic earnings (earnings outside 14d) — likely binary-event speculation (guide-update or buyout rumor). Treat as speculative directional NOT vol play.

---

## Watchlist Write-back

`mcp__uw-pp__watchlist_manage(action="add", group="conviction_2026-05-15", tickers="ETN,NVDA,SNOW,TTWO,IWM")` — **confirmed**. Tomorrow's run will pull `watchlist_alerts` against this group to flag adverse-flow exits.

---

## Failure-mode notes

- All Phase 1 agents returned. No re-spawns required.
- `playbook_daily_synthesis` returned full payload — no fallback composition needed.
- `historical_available_dates` confirmed 2026-05-15 in every data type; data is fresh.
- yfinance fundamentals returned HTTP 401 in deep-dives (ETN, NVDA, AAPL) — non-blocking; UW dark-pool + screener payloads were complete.
- The `dark_pool_accumulation` signal class has no `historical_signal_backtest` history; bullish_flow proxy (WR 0.40) used for ETN and MA. Surfaces a calibration item for the next audit cycle.
