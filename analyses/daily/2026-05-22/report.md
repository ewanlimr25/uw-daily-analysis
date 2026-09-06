# Daily Market Analysis — 2026-05-22

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL UPTREND / SPY 745.64 (+5.25% 30d, -0.52% from 90d high) / SPY-NEAR-FLIP (ZGL 749.49 with first POSITIVE-leaning print in 30 sessions) / QQQ-PIN at 720 / IWM-PIN at 285 / VIX 16.70 / breadth 38.1% bullish (WEAK) / Tech inflow $6.2B leads accelerating risk-on rotation. SPY front-end IV ratio 1.482 BACKWARDATION = index panic gate FIRED on SPY/IWM; QQQ ratio 0.729 CONTANGO = no transmission to tech single-names.
- **Top 0DTE play:** AAPL 307.5/310/312.5 iron fly (cleanest pin on the tape, 310C carries $8.3T long-gamma — order of magnitude above neighbouring strikes). Sell premium. Invalidation: AAPL move >$2.50 either side.
- **Top swing build:** **AMD** — sweep BULL persistence 5/5 ($1.68B ledger + $89M institutional Aug-380C whale) + $354M 30d cum_flow BULL + Tech sector accel + win_rate 0.90 cap. Aug 380C debit (or 380/420 call spread for defined risk per TRANSITIONAL half-size rule). Invalidation: close < 350 or chip sweep persistence breaks. **Final size: half (full pre-risk).**
- **Top LEAP candidate:** None — leap-positioning-radar found ZERO candidates passing the strict 6-of-9 + DIRECTIONAL_LONG@>70 gate. Best near-miss: NBIS (5/9, HEDGED_LONG flagged the institution as long-stock-with-put-hedge, not LEAP-call thesis). LEAP sleeve: SKIP today, redeploy to swing.
- **Biggest risk:** **chip_complex correlation cluster** (AMD/SMH/QCOM/INTC/GLW/NVDA, max corr 0.842 AMD↔SMH) — book is concentrated long-tech. Hedge sleeve: VIX 21/26 Jun call spread sized to 8-12% of book gross delta (SPY backwardation 1.482 = positive-carry hedge). Quarantine: NVDA + META on flow_conflict -3 (institutional accumulation vs bearish flow direction).

## 1. Regime & Gamma State
- **risk_market_regime:** TRANSITIONAL UPTREND; bullish_pct 38.1% (3,818 bearish vs 2,353 bullish tickers) → breadth divergence under a price uptrend. Trading guidance: "Half position sizes. Favor defined-risk strategies."
- **Per-index gamma table:**

| Index | Spot | 0DTE ZGL | Today regime | Broader 0–45d regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 745.64 | 599.98 (today positive) | NEAR_FLIP at 749.49 (broader ZGL) | NEGATIVE | 750 (\$10.8T) | 745 |
| QQQ | 719.66 | 433.15 (today positive) | PIN at 720 | NEGATIVE (ZGL 739.97) | 720 (\$3.82T) | 718 |
| IWM | 284.84 | 200.02 (today positive) | PIN 285/286 | POSITIVE (huge negative cluster 215–260) | 285 (\$2.1T) | 280 |

- **options_flow_dte_volume_share:** 0DTE 42.9% / weekly 23.4% / monthly 18% / LEAPs 6.2% → **RETAIL_DRIVEN tape** (0DTE share > 40% threshold).
- **historical_vrp:** SPY IV30 14.5% vs realised 30d 10.58%, VRP **+3.92% FAIR** — no clean premium-selling or premium-buying structural bias.

## 2. 0DTE / Intraday Plays
Per gamma-flip-tracker (today's expiry frame only):

| Ticker | Regime | Structure | Trade Bias | Invalidation |
|---|---|---|---|---|
| SPY | NEAR_FLIP 745–750 | Sell premium inside band; only chase breakout >749.49 | Fade extremes | Loses 745 put wall on >$50M put expansion → flip NEGATIVE to 743/742 |
| QQQ | PIN 720 | 718/720/722 iron fly into close | Sell premium | Close <718 or >722 |
| IWM | PIN 285/286 | Fade moves outside 284–287 | Sell premium | Break 280 (short-gamma vacuum to 275) or 287 (melt-up to 290) |
| AAPL | PIN 310 (highest conviction) | 307.5/310/312.5 iron fly OR sell 310 straddle | Sell premium | Move >\$2.50 either side |
| TSLA | PIN 430 | Sell 425/430 strangle OR 425/427.5/430 iron fly | Sell premium | Close >430 (squeeze 432.5/435) or <425 |
| MSFT | PIN 420 | 417.5/420/422.5 iron fly | Sell premium | Close >422.5 or <417.5 |
| META | PIN 610 | 605/610/615 iron fly | Sell premium | Break 615 or 605 |
| AMD | PIN 470 | 465/470/475 iron fly | Sell premium | Break <465 (short-gamma zone to 460) |
| **NVDA** | **NEAR_FLIP 215/220** | **0DTE 215P/220C straddle for breakout OR 215/220 iron condor for pin** | **Buy gamma (cheap wings)** | Break 215 puts → 213; reclaim 220 → magnet flips to 225 |
| **NBIS** | **NEAR_FLIP** | **210P/220C cheap strangle** | **Buy gamma** | Close inside 217.5–220 = pin |

**Urgency-ranked sweeps (persistence-first):**
- **Tier 1 directional alpha:** AMD CALLS (5/5, \$1.68B ledger + \$89M Aug-380C whale ticket today), TSLA PUTS (5/5, \$6.6B), NVDA PUTS (5/5, \$4.7B, call-writes on 217.5C/220C/225C), GOOGL PUTS (5/5 aligned with -$36M), META PUTS (5/5 aligned with -$23M).
- **Tier 2 hedge-flow disqualified:** SPY/SPXW persistent puts (synthetic collar, not directional alpha); AAPL persistent puts (conflicts +$81M bullish Step-0 = hedge); MSFT puts (mega-cap hedge); ASTS/SNDK persistent reads conflict with Step-0 directional flow.

**OPEX:** Today is 7 calendar days past third-Friday OPEX (2026-05-15) — `opex-pin-strategist` was not spawned.

## 2a. Swing Dealer Positioning (1–4 weeks)
- **SPY swing-LONG:** 30d FULLY_NEGATIVE GEX regime flipped today — total GEX moved from -342B (5/19 trough) → +472B in three sessions. First non-null ZGL print (749.49) in 30 sessions. Classic dealer-de-risking flush that historically precedes a 1–4 week grind higher. Target 760–765 on clean reclaim of 750. Invalidation: <740 with GEX re-flipping negative ≥3 sessions.
- **QQQ swing-LONG:** DEX +42T call-heavy; GEX flipped 5/21 -75B → 5/22 +17B with ZGL 739.97. Spot 719.65 still below ZGL = dealers short-gamma below 740. Target 730–735 on reclaim. Smaller size than SPY.
- **IWM VANNA SQUEEZE FLAG:** Only put-heavy book in index complex (+4.6M vanna). Falling VIX forces dealer-buying of IWM to stay delta-neutral. Target 290–295 over 2–4 weeks. **Caveat:** cum_flow -$1.09B BEARISH + SPY backwardation transmits panic → risk-monitor SKIPPED IWM despite the squeeze setup.
- **SMH VANNA SQUEEZE FLAG (single name):** Only ticker in single-name basket with NEGATIVE DEX (-1.06T). Put-heavy book + falling VIX + bearish flow (PCR 9.3) + Tech inflow $6.2B = textbook squeeze. **Caveat:** chip_complex cluster gate dropped SMH (AMD is the KEEP).
- **TSLA swing-LONG:** Largest charm-tailwind name in basket (+2.36B charm), DEX +70.8T call-heavy. 1–2 week horizon. Cluster gate dropped TSLA (F is the KEEP for autos).
- **NVDA swing-SHORT:** GEX exploded 193B→800B while spot dropped 226→217; vanna -94.6M (extreme). Falling VIX = dealer SELL. Target 208–210. **Quarantined** by risk-monitor on flow_conflict + 5/27 earnings 3 sessions away.

## 2b. Sector Rotation
**Rotation regime call: `accelerating_risk_on`** — Tech 5d trajectory $3.46B → $6.19B (+79% accel), Cons.Cyclical $412M → $1.08B (+162% accel), Industrials re-accelerating $135M → $522M, Healthcare volatile inflow rebuild (persistence 0.8). Defensives split: Utilities trickle inflow ($56M → $86M; driven by CEG/NRG AI-power, NOT classic defensive), Financial Services and Energy DECELERATING to flat (rotating OUT).

| Sector | Persistence | Trend | Cleanest institutional leader (DTE-mix) |
|---|---|---|---|
| Technology | 1.0 | ACCELERATING | **PANW** (BALANCED 36.5%/24.8%), QCOM (BALANCED) |
| Cons.Cyclical | 1.0 | ACCELERATING | TSLA tactical (RETAIL_DRIVEN 0DTE 60%), CVNA |
| Industrials | 1.0 | RE_ACCELERATING | **HON** (INSTITUTIONAL 55%/7%), GE, RKLB |
| Healthcare | 0.8 | VOLATILE_REBUILD | **ABT** (INSTITUTIONAL 60.5%/8.3%) |
| Utilities | 1.0 | STEADY_LOW_VOL | CEG (BALANCED) — Tech-correlated AI-power |
| Fin Services | DECEL | OUTFLOW | — (avoid) |
| Energy | DECEL | OUTFLOW | — (avoid) |

**Swing book implication:** Long Industrials (HON, GE, RKLB) + Healthcare quality (ABT) + Tech sub-leaders (PANW, QCOM) at 0.5x size; treat AAPL/DELL/TSLA/LLY mega-cap leaders as tactical only (retail-dominated 0DTE-tape); CEG as Tech-correlated utility long; fund longs by underweight XLF/XLE.

## 3. Swing Setups (1–6 weeks)
Ranked by post-risk-gate final size. Sourced from `signal-confluence-quant` audited rubric + `risk-monitor` gates. No HIGH or MEDIUM tier names today — entire book is LOW tier; the rubric's flow_conflict -3 mechanic and cluster gate dropped the top of the candidate union.

### 3a. Long swings (regime-aligned)

| Ticker | Score | Final Size | Structure | Invalidation | Thesis |
|---|---|---|---|---|---|
| **AMD** | 5 | half | Aug 380C debit OR 380/420 call spread | Close <350; chip sweep persistence breaks | Sweep BULL 5/5 + \$89M institutional Aug-380C whale + \$354M cum_flow BULL + Tech sector accel. Cleanest LONG in the book. **Caveat:** today's net flow is BEARISH -$8.8M; multi-day persistence wins per rubric, but watch for tape rollover. |
| **RKLB** | 5 | half | LEAP 85C Jan-2028 (mirror \$47.5M whale at smaller size) OR 60/85 LEAP spread | Close <50; LEAP 85C 2028 OI build reverses | Single-print institutional whale on Jan-2028 85C + cum_flow +\$96M BULL + Industrials sector re-accel. Idiosyncratic conviction. |
| **TTWO** | 5 | half | 9/18 310C debit OR 290/310 call spread | Close <270; 12.7x vol signal doesn't repeat within 5 sessions | 9/18 310C multileg vertical (ratio 0.99) + 12.7x avg vol spike + 8-of-10 bullish flow days + cum_flow +\$22.6M BULL. GTA-6 catalyst window. Cleanest tape in top-3 (8 bullish days vs 2 bearish over 10d). |
| **F** | 5 | half | 14C/15C diagonal (mirror institutional structure) | Close <12.50; Cons.Cyclical rolls to outflow | 14C/15C diagonal call vertical + Cons.Cyclical sector accel + 4.9x vol + KEEP of autos cluster vs TSLA. |
| **INTC** | 4 | half | 22.5/25 monthly call debit spread | Close <20; chip sweep persistence breaks across sector | Sweep BULL 5/5 + \$236M cum_flow BULL + win-rate 0.90. Secondary chip vehicle behind AMD (cluster gate -1 tier). |
| **PANW** | 4 | full (cal-fly) | 6/02 earnings cal-fly (sell 6/05 wing, long 6/12 wing) | Earnings move >2x implied; cal-fly OI reverses pre-print | Tech sub-leader (BALANCED DTE) + earnings 6/02 with kink on 6/05 + IV rank 95.8. Cleanest event structure on board. **Strategy disagreement:** batch_scan recommends bull put spread (also sell-vol). Compatible. |
| **NBIS** | 6 | starter | Small cash equity or Aug 30/40 call spread (placeholder strikes — see deep dive) | DP accumulation cools; no follow-through OI build in 3 sessions | INSTITUTIONAL accum 5d OI BUILD + 3-of-4 load-bearing + Industrials sub-leader. Starter sized due to small magnitude (\$50M cum_flow) and NEAR_FLIP gamma. |
| **ABBV** | 3 | starter | 200/210 call spread Jul OR small cash position | Healthcare flow rolls negative; DP accumulation stops | Defensive rotation, 100% mega buy ratio, +\$14.5M cum_flow BULL. Sleeve diversification — borderline at floor. |
| **QQQ** | 3 | starter | 720/735 Jul call debit spread (half size) | QQQ ratio rolls to backwardation; DEX flip reverses | DEX flip + cum_flow BULL aligned + own contango 0.729 (no panic). Index expression of the swing-LONG thesis. |
| **QCOM** | 5 | starter | RESTRUCTURE from BUY VOL to short-vol iron condor 220/270 Jun | IV rank <70 pre-print; chip sweep breaks | Quant flagged earnings vol; risk-monitor noted VRP-FAIR-into-IV-96.7 contradiction. Use short-vol structure to monetize the rich premium. -1 cluster + -1 VRP demoted to starter. |

### 3b. Short / fade swings (defined risk only)
| Ticker | Score | Final Size | Structure | Invalidation | Thesis |
|---|---|---|---|---|---|
| **SMH** | 5 | SKIP (cluster) | (would have been Jun put credit spread to fade z=+5.82σ extreme) | n/a — DROPPED on chip_complex cluster | contrarian-scanner fade ranked #1 (z=+5.821σ — 1-in-100M extreme PCR). Cluster gate dropped (AMD captures chip thesis cleaner). |
| **NVDA** | 4 | SKIP (quarantine) | n/a — wait for flow_conflict to resolve | n/a | DP accumulation \$9.73B INSTITUTIONAL + dealer SHORT pressure split. Flow_conflict -3 (\-$167M cum_flow opposite accum LONG). 5/27 earnings in 3 sessions amplifies risk. |
| **META** | 3 | starter (BUY VOL only) | Long strangle Jun monthly (defined risk only) | Flow_conflict resolves to net BEAR (exit); DP accum reverses | Flow_conflict -3 (\-$400M cum_flow), but vol-surface BUY VOL #2 (0th percentile z=-1.02 + 06-12 kink). Pure vol play, not directional. |
| **IWM** | 3 | SKIP | n/a — panic gate fired | n/a | Vanna squeeze setup undermined by -$1.09B BEAR cum_flow + SPY backwardation 1.482 panic transmission + index cluster duplicate. |
| **SPY** | 3 | SKIP | n/a — front-end panic + DISTRIBUTION | n/a | DEX regime flip undermined by DISTRIBUTION (mega buy_ratio 0.058) + front_iv_ratio 1.482 BACKWARDATION panic. |
| **TSLA** | 6 | SKIP (cluster) | n/a — F is autos KEEP | n/a | Dealer LONG vs sweep BEAR 5/5 split. Cluster duplication of F. |

**Dropped at quant <3 floor:** GOOGL (vol play only, sweep aligned BEAR but vol-only +1), IGV (contrarian + multileg crowded), FUTU (BUY VOL into earnings — non-directional, fails floor), MCK (DP 100% mega buy refuted by -$17.7M cum_flow BEAR explicit), SOXX, AAPL (DISTRIBUTION refutes bullish cum_flow), MSFT (DP NET SELLING $1.26B refutes cum_flow), ASTS (3-way internal conflict), GLW (cluster gate).

## 4. LEAP Builds (6–24 months)
**Zero candidates passed the strict 6-of-9 + DIRECTIONAL_LONG@>70 gate.**

The conviction-matrix tool is the binding constraint — in TRANSITIONAL UPTREND with mid-band DP buy ratios, the algorithm structurally cannot produce DIRECTIONAL_LONG @ >70 confidence across the watchlist (AAPL 0.45, AMD 0.56, KWEB 0.49, WMT 0.52, IBM 0.47, MSFT 0.39, NBIS 0.62 — all in the [0.4, 0.6] neutral band).

**Near-miss disqualification audit:**
- **NBIS (5/9)** — HEDGED_LONG @ 15.84% confidence. DP buying paired with heavy put protection (put_ask 48k vs call_ask 25k) = institution accumulating common while hedging downside. NOT a directional LEAP thesis. Hard-rejected by spec.
- **AAPL (5/9)** — MIXED @ 5.26%. LEAP OI build symmetric (2028 300C +7,969 AND 2028 250P +9,568). Volatility/dispersion positioning, not directional.
- **AMD (5/9)** — MIXED @ 5.99%. Stock +89% in 30d → premium flow is post-rip chasing, not slow accretion. Symmetric LEAP call+put builds.
- **MSFT (4/9) HARD DISQUALIFIER** — DISTRIBUTION @ 10.93%. Dark pool NET SELLING $1.26B at $418-419 cluster. LEAP structure is dealer offset of distribution, not accumulation.
- **CMCSA preserved as forensic example** — Headline 2027-01-15 30C +73,028 contracts is a SELL-TO-BID (covered-call overwriter), inverting its apparent signal. 90d flow BEARISH confirms.

**LEAP sleeve recommendation: SKIP today.** Redeploy capital to swing-horizon (AMD/RKLB/TTWO/F/INTC).

## 5. Volatility Surface
Key dislocations from `vol-surface-scout`:

| Ticker | Type | IV Z-score | Trade | Edge |
|---|---|---|---|---|
| **GOOGL** | KINKED 2026-06-12 (55.4% vs 33.9% next) | -1.24 (deepest oversold in watchlist) | Long 2026-06-18 ATM straddle (post-kink) | Cleanest dislocation on the board |
| **META** | KINKED 2026-06-12 (81.0% vs 44.7% next) + 0th percentile | -1.02 | Long 2027-01-15 ATM straddle 39% IV OR 06-12/06-18 calendar straddle | Lowest-cost mega-cap vega in a year |
| **SMH** | BACKWARDATION (sympathy, NVDA-driven) | +0.68 | Short 2026-05-29 ATM straddle / Long 2026-06-18 (basket calendar) | Dispersion: basket IV crushes faster than NVDA single-name post-print |
| **PANW** | Single-expiry kink 2026-11-20 (90.1% vs 51.4% neighbors) | +1.44 | Calendar butterfly — short 2026-11-20, long 10-16 + 12-18 | 37 vol-point single-expiry mispricing. **Verify OI thickness before sizing.** |
| **TSLA** | Complacent 1y skew (0.86) | +0.22 | 2027-01-15 risk reversal — long 25Δ put, short 25Δ call | Tail under-priced on a drawdown-prone name |

**Long-dated portfolio rotation:** TSLA / NVDA / META / SMH all show COMPLACENT 1y skew (0.86–1.00) vs SPY at 1.15 TAIL_HEDGING. Sell SPY put-skew, buy single-name put-skew = cheap dispersion-skew arbitrage.

**Disqualified as vol-surface plays (event-driven, hand off to earnings-scout):** SNOW, ZS, MU (front_iv_ratio >1.10 + named catalysts), NVDA (5/27 print — though vol-surface flags z=-1.20 + 40% kink confluence), QCOM (z=+1.59 2σ outlier).

## 6. Risk & Correlation

**Correlation clusters (from `risk_portfolio_correlation` against today's candidate union):**

| Cluster | Members | Max corr | KEEP | DROP / DEMOTE |
|---|---|---|---|---|
| chip_complex | AMD, SMH, QCOM, INTC, GLW, NVDA | 0.842 (AMD↔SMH) | **AMD** | SMH skip, QCOM starter, INTC half, GLW skip, NVDA skip (also flow_conflict) |
| autos | TSLA, F | n/a (dom-class similarity) | **F** | TSLA skip |
| index_etfs | SPY, QQQ, IWM | 0.918 (QQQ↔SPY) | **QQQ** | SPY skip (panic), IWM skip (panic + cluster) |
| mega_cap_communication | META, NVDA | 0.62 (moderate, monitor) | n/a — both quarantine | Both already starter on flow_conflict |

**Gate stack applied:**
- **Regime conflict:** no -1 anywhere — all BULL trades aligned with UPTREND.
- **Panic gate (front_end_iv_ratio):** SPY 1.482 BACKWARDATION → -1 on SPY (already skip) and -1 on IWM (cluster + panic = skip). QQQ 0.729 CONTANGO → no transmission to tech single-names.
- **VRP gate (FAIR +3.92%):** -1 on QCOM (BUY VOL into IV rank 96.7 = contradiction; restructure to short-vol).
- **Cluster duplication:** -1 on SMH, QCOM, INTC, GLW, NVDA (chip_complex); -1 on TSLA (autos); -1 on SPY, IWM (index).
- **Sector rotation:** no -1 — no candidates in Financial Services or Energy outflow sectors.

**Adverse-flow exits from `conviction_2026-05-21` group `[MSFT, NVDA, META, TLT, SNDK]`:**
- **NVDA**: exit_candidate — flow rolled bearish (-$97M today) while DP still accumulating. Flow_conflict; do NOT add to today's conviction; let it sit as monitor.
- **META**: exit_candidate — same flow_conflict pattern (-$23M today vs DP accumulation).
- **SNDK**: exit_candidate — flow bearish -$48M, removed from today's union.
- **TLT, MSFT**: monitor only (TLT mixed; MSFT bullish flow but dropped from union on raw_score <3).

**Hedge sleeve recommendation:** Net book directional skew ≈ 0.85 long. SPY backwardation 1.482 = front-end vol bid; hedge with **VIX 21/26 Jun call spread sized to 8–12% of book gross delta** (positive-carry hedge under backwardation). Avoid long QQQ vol (CONTANGO = expensive carry). Alt: SPY 740/720 30-DTE put spread.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**NO HIGH OR MEDIUM TIER NAMES TODAY.** Top of the union scored 6 (TSLA, NBIS) — both LOW tier under the 2026-05-15 audit P0 cuts (HIGH = ≥10, MEDIUM = 7–9).

**Why the book is shallow:** The mechanical flow_conflict -3 rule cascaded heavily today — NVDA -3, META -3, SPY -3, MCK -3, IWM -3 all triggered when 30d cum_premium_flow ran clearly opposite the dominant_signal_class. This is exactly what the 2026-05-15 audit P0 rule was designed to catch (prior versions would have surfaced NVDA accumulation as HIGH despite the bearish flow direction). Today's tape is a regime-transition print — institutions accumulating in dark pools while bleeding off options call exposure → genuinely lower conviction.

**LOW-tier book breakdown (final_size sorted, ≥half):**

### AMD — raw_score 5, final_size HALF
- **score_components:**
  - +1 sweep-tracker | `hot_chains_sweep_persistence` | BULL persistence 5/5 (\$1.68B ledger, \$89M Aug-380C whale)
  - +1 accumulation-hunter | `dark_pool_block_stratified` | accum 1.27 NEUTRAL, mega buy_ratio 0.945 (partial signal — would be +3 if accum reached ACCUMULATION threshold)
  - +3 signal-confluence-quant | `historical_cumulative_premium_flow` | 30d net flow +\$353.6M BULL-aligned
- **dominant_signal_class:** multi_day_sweep | **win_rate:** 0.90 (capped from bullish_flow 0.929) | **cum_flow_30d:** +\$354M
- **load_bearing_tools_cited:** 2/4 | **load_bearing_gate_status:** n/a (below HIGH tier)
- **risk-monitor gates:** none applied (KEEP of chip_complex cluster)
- **final size:** half | **structure:** Aug 380C debit OR 380/420 call spread
- **invalidation:** close <350; chip sweep persistence breaks

### RKLB — raw_score 5, final_size HALF
- +1 sector-rotation | Industrials sub-leader; +2 multileg-strategist | LEAP 85C Jan-2028 \$47.5M whale; +3 cum_flow +\$96M BULL.
- dominant_signal_class: leap_directional | win_rate: 0.90 cap | cum_flow_30d: +\$96M
- Gates: none. Final HALF. Structure: LEAP 85C Jan-2028 OR 60/85 LEAP spread. Invalidation: close <50.

### TTWO — raw_score 5, final_size HALF
- +2 multileg-strategist | 9/18 310C vertical (ratio 0.99); +3 cum_flow +\$22.6M BULL trend_direction explicit BULLISH.
- dominant_signal_class: multileg_directional | win_rate: 0.90 cap | 12.7x avg vol watchlist alert.
- Gates: none. Final HALF. Structure: 9/18 310C debit OR 290/310 spread. Invalidation: close <270.

### F — raw_score 5, final_size HALF
- +2 multileg-strategist | 14C/15C diagonal; +3 cum_flow +\$4.3M BULL (consistent 90d).
- dominant_signal_class: multileg_directional | win_rate: 0.90 cap | Cons.Cyclical sector accel | KEEP of autos cluster.
- Gates: none. Final HALF. Structure: 14C/15C diagonal. Invalidation: close <12.50.

### INTC — raw_score 4, final_size HALF
- +1 sweep BULL 5/5; +3 cum_flow +\$236.8M BULL.
- dominant_signal_class: multi_day_sweep | win_rate: 0.90 cap.
- Gates: -1 cluster (chip_complex). Final HALF. Structure: 22.5/25 call debit spread. Invalidation: close <20.

### PANW — raw_score 4, final_size FULL (cal-fly)
- +1 sector Tech sub-leader; +1 earnings SELL VOL; +1 vol-surface cal-fly rank #4; +1 cum_flow +\$14M BULL.
- dominant_signal_class: earnings_vol | win_rate: 0.70 vol_realisation proxy.
- Gates: none. Final FULL on the calendar structure (defined risk by construction). Invalidation: earnings move >2x implied.

**LOW-tier supporting (starter):** QCOM (5, RESTRUCTURE to short-vol IC), NBIS (6, starter; 3/4 load-bearing), TSLA (6, SKIP cluster), SMH (5, SKIP cluster), NVDA (4, SKIP quarantine), META (3, starter BUY VOL only), GLW (4, SKIP cluster), ABBV (3, starter), QQQ (3, starter), SPY/IWM (3, SKIP).

### Conviction-scoring rubric (verbatim from skill, 2026-05-15 audit P0)
```
+3  dealer-positioning DEX flip or vanna-squeeze in trade direction
+3  3+ aligned signals in accumulation-hunter (LOAD-BEARING: dark_pool_block_stratified INSTITUTIONAL tier)
+1  multi-day OI build (historical_oi_trend BUILDING, ≥5d)
+1  insights_conviction_matrix = DIRECTIONAL_LONG, confidence > 70
+3  historical_cumulative_premium_flow net directional accretion 30d (LOAD-BEARING)
+1  sweep-tracker top 5 by sweep_persistence (mega-cap suppression: SPY/QQQ/IWM/SPXW + top-10 mega-caps unless cum_flow aligns)
+1  sector-rotation leader in rotating sector (persistence ≥3)
+1  earnings-scout BUY VOL or SELL VOL
+2  multileg-strategist directional term-structure-anchored play
+1  vol-surface KINKED or BACKWARDATION with VRP-aligned bias
-2  contrarian-scanner overcrowded long + rising PC z-score
-3  flow_conflict — cum_flow 30d clearly opposite dominant_signal_class
-1  flow_conflict_lite — 30d cum_flow MIXED or aligned but bottom-quartile magnitude
-1  risk-monitor correlation cluster (corr > 0.7) — applied in 2b
-3  risk_market_regime conflicts with trade direction — applied in 2b
Tiers: ≥10 HIGH (full), 7–9 MEDIUM (half), 3–6 LOW (starter/watch), ≤2 drop
Step 3a 3-of-4 load-bearing gate: HIGH-tier (≥10) must cite ≥3 of
  {dark_pool_block_stratified, historical_cumulative_premium_flow,
   insights_institutional_accumulation, options_structure_dex} else DEMOTE to MEDIUM
```

## 8. Watch-only — single signal, no confluence
Surfaced by one agent but failed the confluence gate (single-agent + no Step-0 confluence ≥4 backing). NOT for trade entry today; journaled for tomorrow's persistence check:

| Ticker | Single source | Signal |
|---|---|---|
| GLW | accumulation-hunter | score 6, 100% mega buy ratio, 3.82 accum (also cluster-dropped) |
| MCK | accumulation-hunter | score 5, 100% mega buy ratio, accum 30.5 (but cum_flow -$17.7M BEAR explicit → DROP) |
| SOXX | accumulation-hunter | score 5, semis ETF (cum_flow -$12M → DROP) |
| HON, GE | sector-rotation | Industrials best-in-class institutional DTE mix |
| ABT | sector-rotation | Healthcare best-in-class institutional DTE 60.5% |
| CEG | sector-rotation | AI-power utility (BALANCED DTE) |
| NTAP | earnings-scout | CALENDAR (BACKWARDATION) — 5/28 print |
| HPQ | earnings-scout | SELL VOL — 5/27 print, IV 100 |
| OKTA | earnings-scout | SELL VOL — 5/28 print, kink at 5/29 |
| FUTU | earnings-scout | BUY VOL #1 by EV (TAIL_HEDGING back skew 1.137 + 2.3% implied move cheap) — but rubric scored 0 (non-directional BUY VOL) |
| TLT | multileg | LEAP 105C/120C 2028 vertical (long-duration Treasury bull) |
| GLD | multileg | 500C/550C 9/18 vertical (gold bull, $34M long-leg) |
| SMCI | multileg | 36.5C/38.5C 5/29 vertical (AI-server bull, 7DTE) |
| ACHR | multileg | 8C/10C July vertical (eVTOL speculative) |
| DECK, TEM | Step-0 confluence | bullish confluence score 5 (small/mid-cap) |
| MSTR | sweep | 2/5 bearish persistence + multileg disqualified hedge |

---

**Watchlist write-back confirmed:** `conviction_2026-05-22 = [AMD, RKLB, TTWO, F, INTC]` persisted via `mcp__uw-pp__watchlist_manage(add, group="conviction_2026-05-22")`. Tomorrow's run will pull `watchlist_alerts` against this group to flag adverse-flow exits.

**Strategy disagreement notes (multileg-strategist vs playbook_batch_scan):**
- **AMD:** batch_scan recommended **Bear Call Spread** (today's flow BEARISH -\$8.8M, IV 82.4 elevated). Multileg/sweep read says BULL on multi-day persistence + whale ticket. **Preferred multileg (per skill rule)** but today's tape rollover is the risk to watch.
- **RKLB, QQQ:** batch_scan flagged "No Clear Edge" — but multileg LEAP whale (RKLB) and dealer-positioning DEX flip (QQQ) carry the signal. **Preferred multileg/dealer** (rule-based scan blind to LEAP whale prints + DEX trajectories).
- **META:** batch_scan "No Clear Edge" + risk-monitor quarantined BUY VOL only. **Confluence on caution.**
- **PANW:** batch_scan Bull Put Spread aligns with earnings-scout/vol-surface SELL VOL cal-fly. **Consistent.**
- **QCOM:** batch_scan Bull Put Spread aligns with risk-monitor's recommendation to restructure BUY VOL → short-vol. **Consistent.**
