# Daily Market Analysis — 2026-05-20

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL — UPTREND. SPY $741.25 (+5.28% 30d, −1.1% from 90d high), above 20/50 SMA. Breadth WEAK at 39.5% bullish (3,714 bear vs 2,425 bull tickers). Tech +$4.3B dominates sector flow; all 11 sectors net-positive 5d (broad-inflow, low-discrimination). SPY 0DTE NEAR_FLIP at 738-743 pin with 0-45d ZGL at $744.12 (just above spot — DEX regime flip NEG→POS today after 9 sessions FULLY_NEGATIVE). QQQ front-end IV ratio 1.455 SEVERE BACKWARDATION = panic gate active across the complex.
- **Top 0DTE play:** AAPL 300/302.5 pin — highest-confidence single-name 0DTE pin in the book. Sell 298/302.5 strangle or 300 fly. Invalidate < 297.5 with sustained IV expansion.
- **Top swing build:** AAPL — common stock or Jun 19 ATM call. raw_score 13 (HIGH, all 4 load-bearing tools cited). $2.49B DP today + 5/5 BUILDING OI (+601k 10d) + 94% call-DEX dominance + Jan-2028 300C $54M ASK clean LEAP. Pre-risk HALF, post-risk **STARTER** (QQQ panic gate −1). Invalidation: close <$298 on +1.5σ volume.
- **Top LEAP candidate:** **None pass leap-positioning-radar's 6-of-9 gate.** LEAP DTE share only 6.4% — institutions are short-dating. TLT (raw_score 10, DEMOTED to MEDIUM at 3a-gate) is the closest LEAP-grade structural setup: Jan-2028 $105/$120 LEAP call vertical 35k size, put-heavy DEX −$111B + vanna +$10.4M + per-strike-confirmed $84-86 gamma wall. Final size **STARTER**. Invalidation: close <$82 for ≥3 sessions OR 10Y >4.85%.
- **Biggest risk:** Concentration. 8 of top-15 quant scores are QQQ-correlated mega-cap or semi names; QQQ 1.455 SEVERE BACKWARDATION = vol is panicking ahead of macro. Cluster cap fires on **MSFT/GOOG/AMZN/META/NVDA/AMD/MU/INTC/TSM/SNDK** — all gated to SKIP. Recommended hedge sleeve: VIX Jun-17 25C/32C long + 2× 45C short (or 32/42/45 May-27 condor like multileg-strategist flagged institutions are already buying), sized to 0.25R.

---

## 1. Regime & Gamma State

**Macro tape:** Regime = **TRANSITIONAL — Mixed signals, reduce position size, wait for clarity.** Trend = UPTREND. SPY $741.25 above 20SMA ($728) and 50SMA ($694), +5.28% 30d but only −1.1% from 90d high — late-cycle exhaustion candidate. Breadth weak at 39.5% bullish (60.5% bearish), confirming narrow tech-driven leadership.

**Per-index gamma (0DTE + 0-45d):**

| Ticker | Spot | 0DTE ZG | 0-45d ZG | Regime | Call Wall | Put Wall | 0-45d Total GEX |
|---|---|---|---|---|---|---|---|
| SPY | 738.87 | 649.34 | 744.12 | NEAR_FLIP | 740 | 730 | +$748B (regime flipped NEG→POS TODAY) |
| QQQ | 709.28 | 585.15 | 729.13 | NEAR_FLIP | 710 | 700 | +$39B (third regime flip in 10d — unstable) |
| IWM | 277.74 | 259.24 | none | TREND | 279 | 275 | −$212B (FULLY_NEGATIVE 0-45d, no ZGL) |

**DTE share (`options_flow_dte_volume_share`):** 28.8% 0DTE / 28.3% weekly / 25.8% monthly / 6.4% LEAP → **BALANCED** regime hint (institutional + retail mix). LEAP share LOW = institutions short-dating conviction.

**VRP (`historical_vrp` SPY):** **FAIR** at +0.046 (IV30 = 15.3%, RV30 = 10.65%). Mild premium overpricing, but not punitive — neither premium-sell-favored nor premium-buy-favored cleanly. SELL-VOL trades need ≥ +0.10 clean positive to size; today's tape penalizes pure premium-selling structures via risk-monitor's VRP gate.

**Front-end IV ratios (panic gate):** SPY 1.12 BACKWARDATION, QQQ **1.455 SEVERE BACKWARDATION** (compounding panic — every QQQ-correlated name takes −1 tier in risk gate), IWM 1.138 BACKWARDATION.

---

## 2. 0DTE / Intraday Plays

**Index pins (gamma-flip-tracker):**
- **SPY 736-743 cage** — sell premium inside, but pre-position a long-gamma tail above $744 (ZGL reclaim) and below $735 (where 0-45d short-gamma frame dominates). Iron fly 738-742 or fade extremes inside 736-743.
- **QQQ 707-712 cage** — sell premium inside, stop pin trade if 706 fails.
- **IWM** — TREND not PIN. Long-gamma chase on break of 275 (0-45d fully short gamma — dealers chase down). Pin 278-280 only while above 277.

**Single-name 0DTE pins:**
- **AAPL 300/302.5 cage** — spot pasted on stacked 0DTE call wall ($1.38T GEX at 302.5C, $874B at 300C, 295 resistance). Sell 298/302.5 strangle or 300 fly. AAPL 300C in hot-chains top-15 (132k vol). Highest confidence in the book.
- **META 600/605 NEAR_FLIP** — spot $603.71 directly on 605 wall ($61B GEX) with 600/595 as RESISTANCE walls below. Sell 605/610 premium while above 603; flip-to-long-gamma below 600 (dealers invert).
- **TSLA 410-415 PIN** — spot $411.78 in a deep gamma sandwich (415 stacked $1.43T, 410/412.5 support $457B/$328B). 415C dominated hot-chains (309k vol, $39M premium). Sell 408/415 iron condor.

**Sweep ledger (sweep-tracker, persistence-ranked):** Today's tape contaminated by $9.4B SPX deep-ITM C6000 boxes / calendar rolls / diagonals — STRUCTURAL not directional. Strip them out and the real directional ledger is thin. Highest-conviction directional sweep: **AMD 5-of-5 bullish persistence** (LEAP-led Jan-2027 C410 $14.8M + Jul C380 $8.6M ASK) and **INTC 5-of-5 bullish persistence** (Jan-2027 C20 LEAP $11M + Jun C95 swing; no hedge-flow filter since not top-10 mega-cap).

**OPEX guard:** N/A — 5 trading days past 2026-05-15 monthly OPEX. No opex-pin-strategist spawned.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

`dealer-positioning-strategist` flagged today as a structural hinge:

- **SPY — DEX regime flip NEG→POS on 2026-05-20** (+$748B GEX, ZGL $744.12 vs spot $739). 9 of prior 10 sessions FULLY_NEGATIVE; today's clean regime flip is the pre-directional signal Karsan framework calls out. Spot reclaiming ZGL converts dealer hedging from acceleration-buying to mean-reversion-selling — caps upside near $748-755 but locks in the bounce. Front-end 1.12 BACKWARDATION confirms tape just dehedged; charm +$5.2B adds tailwind over the next 5-10 sessions. **Swing bias LONG**. Invalidation: DEX flips negative for ≥3 sessions OR front-end IV ratio extends >1.20.
- **QQQ — three regime flips in 10 sessions + front-end 1.455 SEVERE BACKWARDATION = unstable whipsaw**. Stand aside.
- **IWM — classic vanna-squeeze SETUP** (put-heavy DEX −$1.37T, vanna +$29M, ZGL grinding lower 173→85). Trigger has NOT FIRED because front-end 1.138 backwardation = VIX still bid. Watchlist long; mature only on VIX compression. Risk-monitor REJECTED for sizing today (full flow_conflict + TREND-acceleration risk).
- **NVDA — highest call-DEX dominance in the swing set: +$49.7T DEX (86% call-side), +$72B charm**. Post-OPEX charm decay is a 5-10 session structural tailwind. **CONFLICT: accumulation-hunter DEMOTED NVDA** (mega buy_ratio 0.302 NET SELLER on +21.5% 30d rally). Risk-monitor SKIPPED on binary 5/27 earnings + cluster duplication.
- **TLT — highest-conviction single-name SWING LONG**: put-heavy DEX −$111B, positive vanna +$10.4M, multi-strike positive-gamma wall $84-86 (confirmed via per-strike GEX, not single-strike artifact). ZGL $84.74 sits $1 above spot $83.81. Any rate-vol compression forces dealer covering into $84-86. 1-4wk target $86-87 if spot reclaims ZGL.
- **AAPL — 94% call-DEX dominance** ($14.5T calls vs −$0.8T puts), charm +$4.3B. Most call-tilted book in the swing set.
- **MU/PLTR/AMD — secondary LONGs** with charm tailwind; AMD lowest conviction (thinnest call-dominance in semis).
- **META — dealer NEUTRAL/SKIP** (DEX positive but barely; most balanced book; charm only +$192M).

---

## 2b. Sector Rotation

`sector-rotation-strategist` verdict: **broad-inflow LOW-DISCRIMINATION** day. All 11 sectors print 5d `persistence_score=1` (every sector positive net flow every day). The canonical persistence ≥3 single-direction gate can't fire from sign-flips — translate to relative day-over-day magnitude changes:

| Sector | 5d avg | Today | Δ vs avg | Direction |
|---|---|---|---|---|
| Technology | $4,860M | $4,300M | −12% | Still dominant absolute |
| Comm Services | $751M | $497M | **−34%** | Clear deceleration |
| Industrials | $321M | $275M | −14% (but +103% vs yest $135M) | **Re-accelerating D/D** |
| Cons Cyclical | $713M | $761M | +7% (vs yest $464M +64%) | **Re-accelerating D/D** |
| Energy | $483M | $295M | **−39%** | Decelerating |
| Cons Defensive | $80M | $52M | −35% | Decelerating |
| Healthcare | $240M | $155M | −35% | Stabilizing low |

**Rotation regime call:** `broad_inflow_low_discrimination`, with secondary tilt = `cyclical_leadership_emerging`. Tech still absolute volume king but losing share; ConsCyc + Industrials re-accelerating day-over-day; Energy decelerating −39%.

**Single-name leaders within rotating sectors (institutional DTE check, monthly+ ≥27%, 0DTE = 0):** **AMD** (38% monthly+, leader 5), **MU** (37%), **SNDK** (48% — highest inst share), **LRCX** (52% — semi-capex), **CRWD** (49% — cyber), **ORCL** (44%), **RCL** (88% non-weekly — institutional travel bet), **GE** (37%), **BA** (44%), **RKLB** (31%).

Swing-book implication per agent: long the semi capex cluster (AMD/MU/SNDK + LRCX) + aerospace pair (GE/BA) + RCL as best-quality ConsCyc; NO short side — broad-inflow tape offers no clean rotating-out sector. (Risk-monitor subsequently gated most of these out on cluster duplication.)

---

## 3. Swing Setups (1–6 weeks)

Ranked by `signal-confluence-quant` audited score, post `risk-monitor` gate-stack. **Only candidates surviving the full gate stack are listed for sizing; gated names appear in §7 for transparency.**

### 3a. Long swings (regime-aligned)

| Ticker | raw_score | tier_final | Structure | Final size | Invalidation |
|---|---|---|---|---|---|
| **AAPL** | 13 | HIGH | Common stock or Jun 19 ATM call (delta proxy) | **STARTER** | close <$298 on +1.5σ volume |
| **TLT** | 10 (DEMOTED) | MEDIUM | Common stock or Sep/Dec ATM call; consider Jan-2028 $105/$120 LEAP call vertical (mirror the 35k institutional print) | **STARTER** | close <$87 for ≥3 sessions OR 10Y >4.85% |
| **CRWD** | 7 | MEDIUM | **Iron condor 5-7% wide around spot, May 30 expiry (POST-print)** — IV-99 says SHORT premium; FAIR VRP forbids naked straddle. Batch-scan + risk-monitor both prefer condor over earnings-scout's BUY-VOL straddle (multileg-strategist had no direct CRWD read; deferring to credit-spread per overall regime). | **STARTER** | move >7% in either direction post-print = thesis breaks |
| **ULTA** | 6 | LOW (gate survivor) | Jun 4 long straddle/strangle ATM — earnings Jun 4; implied 2.2% vs realized 6-9%. ConsCyc re-acceleration tailwind. | **HALF** | move <2% by May 28 = IV decay risk; cut at 30% premium decay |

**Gated out (cluster + panic stack):** MSFT (3a 3-of-4 PASS but duplicate of AAPL at corr 0.63+), GOOG (same), AMZN (same), META (dealer-NEUTRAL + cluster dup), NVDA (binary 5/27 + distribution + cluster), AMD (sweep-LONG vs accumulation-DISTRIBUTION + cluster), TSM (cluster carrier dropped on panic gate), MU (cluster + flow_conflict −3 already in score), INTC (cluster), SNDK (cluster), SPY (TLT carries macro), IWM (full flow_conflict + TREND-down risk).

### 3b. Short / fade swings (defined risk only)

| Ticker | raw_score | tier_final | Structure | Final size | Invalidation |
|---|---|---|---|---|---|
| **VLO** | 3 | LOW (gate survivor) | Short call spread or long put spread Jun expiry — Energy decel −39% vs 5d tailwind | **STARTER** | crude rebound above prior pivot |
| **NBIS** | 4 | LOW (gate survivor) | Long put or put spread Jun expiry — small-cap bear with no-cluster | **STARTER** | break of recent swing high |
| **TTWO** | 6 | LOW (size-reduced) | May 22 short strangle, reduced to STARTER (1R cap) — SELL VOL into FAIR VRP is audit's flagged anti-pattern | **STARTER** | move >5% pre-expiry |

**Gated out:** WDAY (regime + panic + cluster −3), DE (regime + cluster), XLE (cluster dup VLO), XLI (regime — Industrials re-accelerating), SNOW (size SKIP — contrarian conflict).

---

## 4. LEAP Builds (6–24 months)

**No LEAP-grade candidates today.** `leap-positioning-radar` returned zero names passing the 6-of-9 gate — `insights_conviction_matrix` flagged every mega-cap as MIXED with confidence <8% DIRECTIONAL_LONG. Today's heaviest >180-DTE OI build was POET DEC-2028 $40C at 26,943 contracts ASK-led, but the stock is a +143% 30d micro-cap moonshot — momentum chase, not durable institutional thesis. AAPL had 612d call/put pairs (volatility structure, not directional). MSFT's OI build is entirely 0-60 DTE. TLT carries the closest-to-LEAP-grade thesis but was demoted at Step 3a gate (cited 2-of-4 load-bearing tools) — sized in §3 as MEDIUM swing rather than LEAP.

`CPNG` flagged as potential LEAP-PUT candidate (DIRECTIONAL_SHORT, but only 52% confidence — below 70% gate). Watchlist for the 2026-05-21 run.

---

## 5. Volatility Surface

`vol-surface-scout` finds an **earnings-week tsunami** dominating the surface — virtually the entire single-name watchlist sits in BACKWARDATION ahead of the May 21–Jun 3 print cluster (WDAY/ZM/DE/TTWO tomorrow; ZS/SNOW/CRM/MRVL May 26-27; GTLB/PANW/DG/ULTA early June). SPY/QQQ backwardation is single-name-driven, not macro panic; index back-month skew NORMAL.

**KINKED names (post-event calendar candidates):**

| Ticker | Kink DTE | Front IV | Structure |
|---|---|---|---|
| GTLB | Jun 5 | 112% | Long Jun 5/Jun 18 ATM calendar at $27 — earnings 6/2 |
| MU | Jun 26 | 116% | Long Jun 18/Jul 17 ATM calendar — earnings ~6/25 (Jun 26 IS the kink, avoid as leg) |
| NVDA | Dec 18 | 55% | Secondary kink (Q4 catalyst overlap); back-month skew COMPLACENT (0.9 ratio) — tail underpriced |
| ULTA | Jun 5 | 63% | Long Jun 5 straddle (BUY VOL — FLAT 1.01 term, RICHEST VRP +0.249) |
| ZS | May 29 | 122% | Long May 29/Jun 12 calendar — earnings 5/26 |

**BACKWARDATION calendars (sector ETF cluster):**
- **SOXL** Jun 5/Jul 17 ATM (NVDA 5/27 + MRVL 5/27 + AVGO 6/3 cluster crush)
- **SMH** May 29/Jun 18 ATM (NVDA proxy)

**IV percentile corrections (Goyal-Saretto):** MU (rank 88 → zscore_pct 78), SNOW (88 → 71), NVDA (high → 64), SMH (med → 75). Raw IV rank inflates conviction on these — size accordingly.

**Pre-event short-premium (today's prints):** ULTA Jun 2 (richest VRP +0.249), TTWO 5/22 (+0.214), GTLB 6/2 (+0.20), WDAY 5/22 (+0.20 BUT directional bear flow disqualifies SELL VOL), ZS 5/26 (+0.17). Only ULTA + TTWO + GTLB survive the desk filter for short premium today.

**BUY VOL on underpriced earnings moves (highest EV):** ULTA (FLAT term + 6-9% realized), GTLB (4% implied vs 10-15% realized), OKTA (3.6% vs 6-8%), ADSK (2.6% vs 4-6%), CRWD ($24M aligned bull flow + 12/8/-5/18 realized history).

**No BUY-VOL setups except AMD/INTC where front-end backwardation conflicts with negative single-name VRP** (−0.19 / −0.16) — avoid both per vol-surface-scout.

---

## 6. Risk & Correlation

`risk-monitor` consumed quant's union and applied the gate stack:

**Correlation clusters (corr > 0.7 = treat as one position):**
- **MEGA_CAP_TECH** = {AAPL, MSFT, GOOG, AMZN, META} — META/MSFT 0.634; GOOG/SPY 0.597. Cluster cap: one FULL → AAPL retained, others stepped to HALF/SKIP.
- **SEMI_CLUSTER** = {NVDA, AMD, TSM, MU, SNDK, INTC} — MU/SNDK 0.726 HIGH; AMD/INTC 0.655; NVDA/TSM 0.654. TSM was cluster carrier (cleanest tape, non-binary) but panic gate took it to SKIP.
- **INDEX_RATES** = {SPY, IWM, TLT} — IWM/SPY 0.891 HIGH; IWM/TLT 0.817 HIGH; SPY/TLT 0.789 MODERATE. **TLT promoted on diversification grounds** (rates path uncorrelated to equity panic gate); SPY/IWM both stepped down.
- **CYBER_SOFTWARE** = {CRWD, PANW, ZS, WDAY} — CRWD/PANW 0.869 HIGH; CRWD/ZS 0.715 HIGH. CRWD carrier (only real earnings catalyst at IV-99).
- **ENERGY** = {VLO, XLE} — 0.856 HIGH. VLO single-stock carrier.
- **INDUSTRIALS_BEAR** = {DE, XLI} — 0.764 HIGH. Both gated out (Industrials re-accelerating).

**Regime gates fired:**
- **Panic gate (front-end IV ratio > 1.10):** QQQ 1.455 → ALL QQQ-correlated names took −1 tier (AAPL, MSFT, GOOG, AMZN, META, NVDA, AMD, TSM, MU, SNDK, INTC, CRWD, PANW, ZS, WDAY).
- **Regime conflict:** IWM (vanna long into weak-breadth UPTREND), WDAY/SNOW (SKIP-bearish vs UPTREND), NBIS (BEAR), XLI/DE (BEAR vs Industrials re-accelerating).
- **VRP-vs-trade-type contradiction:** TTWO SELL-VOL into FAIR VRP −1 tier; CRWD short-premium-lean −1 tier.
- **Cluster duplication:** AAPL retained, four mega-caps gated; TSM retained then panic-gated; CRWD retained, three cyber gated.
- **Sector rotation drag:** XLI/DE bear penalized for adverse sector tape.

**Adverse-flow exit candidates (from yesterday's `conviction_2026-05-19`):**
- **WMT** — BEARISH flow_direction with $246M DP + 98k OI add + 1.65x vol + P/C 1.40. **EXIT-CANDIDATE if held long.**
- **BL** — P/C 0.00 + 2.4x vol but only $978k DP = retail-call chase, NOT institutional. DOWNGRADE.
- **ZS** — IV-99 expensive AND CRWD/ZS 0.715 correlation = redundant with CRWD primary book. EXIT-CANDIDATE: roll into CRWD.
- **TLT** — Confirming-bullish ($945M DP + 382k OI + 1.6x vol) — REINFORCES today's promotion.
- **AAPL** — Reinforcing ($2.49B DP + 98k OI). No exit.

**Hedge sleeve:** Book net delta is LONG-skewed (AAPL HIGH + TLT STARTER + ULTA HALF + CRWD STARTER, ballast shorts in VLO/NBIS/TTWO; net ~+0.65 long delta). Weak breadth + SPY 1.12 + QQQ 1.455 says vol is pricing a downside catalyst the tape hasn't recognized. **Recommended: VIX Jun-17 25C/32C long + 2× 45C short (or the 32/42/45 May-27 condor multileg-strategist showed institutions already buying today)**, sized to 0.25R of book notional. Supplementary SPY 720/710 Jun-6 put spread overlay optional.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

Per-ticker breakdown from `signal-confluence-quant` audit trail + `risk-monitor` final sizing. Components are tagged with `(source-agent, source-tool)` per the 2026-05-09 audit requirement.

### AAPL — raw 13 / HIGH / final STARTER
- +3 (accumulation-hunter, dark_pool_block_stratified + insights_institutional_accumulation): 5-of-5 signals, ACCUM 2.05, MEGA buy_ratio 0.794, $246M DP + $230M ext-hours both above-mid, BUILDING 5/5 +601k OI, institutional-tier
- +3 (dealer-positioning-strategist, options_structure_dex): 94% call-DEX dominance, $14.5T calls vs $0.8T puts, charm +$4.3B
- +3 (accumulation-hunter, historical_cumulative_premium_flow): 90d net +$487.5M BULLISH accretion
- +2 (sweep-tracker, options_flow_sweeps): Jan-2028 300C $54M ASK = clean LEAP accumulation counter to broader bear tape
- +1 (gamma-flip-tracker, options_structure_today_gamma_flip): PIN 300/302.5 — highest-confidence 0DTE pin
- +1 (insights_signal_confluence): watchlist alert $246M DP + 98k OI
- **Step 3a load-bearing: 4-of-4 PASS** — HIGH retained.
- Dominant signal: `dark_pool_accumulation`. `win_rate` NA (no class history) → fallback volume_spike 0.541 → pre-risk HALF.
- Risk-gate: QQQ panic −1 → final STARTER.
- Structure: common stock or Jun 19 ATM call. Invalidation: close <$298 on +1.5σ volume.

### MSFT — raw 11 / HIGH / final SKIP
- +3 accumulation 5-of-5 STRONGEST mega buy 0.895 (accumulation-hunter, dark_pool_block_stratified)
- +3 90d cum_flow +$667M (historical_cumulative_premium_flow)
- +2 multileg bullish $435/$450/$500C (multileg-strategist)
- +2 Tech sector leader persistence (sector-rotation)
- +1 top-of-funnel confluence
- 3a 3-of-4 PASS (DEX-absent flagged but compensated).
- Risk-gate: panic −1 + mega-cap cluster dup −1 (AAPL is carrier) → **SKIP**. Kept on watchlist as feedback calibration.

### TLT — raw 10 / HIGH-then-MEDIUM / final STARTER
- +3 dealer HIGHEST CONVICTION DEX/vanna structural (dealer-positioning-strategist, options_structure_dex + vanna_charm)
- +2 Jan-2028 LEAP call vertical 35k size pension trade (multileg-strategist, hot_chains_multileg)
- +3 watchlist $189M DP + 382k OI + 1.6x vol (watchlist_alerts + oi_biggest_increases)
- +2 TBT inverse proxy confluence (insights_signal_confluence)
- **Step 3a load-bearing: 2-of-4 FAIL → DEMOTED to MEDIUM.**
- `win_rate` 0.312 bullish_flow fallback → pre-risk STARTER.
- Risk-gate: no penalty (rates uncorrelated to equity panic) → final STARTER.
- Structure: common or Sep/Dec ATM call; consider mirroring Jan-2028 $105/$120 LEAP call vertical at 0.5-1R notional. Invalidation: close <$87 ≥3 sessions OR 10Y >4.85%.

### GOOG — raw 9 / MEDIUM / final SKIP
- +3 accumulation 5-of-5 cluster (dark_pool_block_stratified + insights_institutional_accumulation)
- +3 90d +$331M BULLISH accretion
- +2 multileg $400/$410C
- +1 GOOG/GOOGL class-share arb (GOOG accumulating, GOOGL distributing)
- 3a 3-of-4 PASS. Risk-gate: panic −1 + cluster dup −1 → **SKIP**.

### AMZN — raw 9 / MEDIUM / final SKIP
- Mega 0.601 + 4 signals + +527k OI on $277.5-290 forward calls + sector leader + $14M top-of-funnel. 3a 3-of-4 PASS. Same panic + cluster gate → SKIP.

### MU — raw 9 (net after −3 flow_conflict) / MEDIUM / final SKIP
- +3 dealer +$3.9T DEX, +3 mega buy 0.657 + +725k OI LARGEST in screen, +2 semi leader #2, +1 KINKED Jun 26 116%, +1 BUY VOL Jun 26, +2 watchlist; **−3 FLOW_CONFLICT (90d cum_flow −$664M BEARISH vs LONG OI-build, magnitude >> $60M median)**. Risk-gate: panic + semi cluster → SKIP.

### NVDA — raw 8 / MEDIUM / final SKIP
- +3 dealer +$49.7T DEX strongest charm tailwind, +2 multileg bull ratio call fly 5/22 expiry into 5/27 earnings, +1 sweep two-sided NTM (mega-cap hedge-flow filter conditionally passed since 90d cum_flow +$135M aligned), +1 top-of-funnel; **+0 accumulation-hunter REPORTED DISTRIBUTION (mega buy_ratio 0.302 net seller on +21.5% 30d rally — surfaced as risk component)**, **−1 flow_conflict_lite**.
- 3a 2-of-4 FAIL. Risk-gate: panic + semi cluster + binary 5/27 earnings → **SKIP**.

### AMD — raw 8 / MEDIUM / final SKIP
- +3 sweep 5-of-5 bullish persistence LEAP-led (only first-class bull sweep in mega-cap tech; hedge-flow filter passed since cum_flow aligned), +3 90d +$411M accretion, +2 semi leader #1, +1 dealer LONG low-conviction, +1 top-of-funnel; **−2 accumulation-hunter DISTRIBUTION (mega buy 0.374 net seller into 30d rally — flagged conflict)**.
- 3a 2-of-4 borderline. Risk-gate: panic + cluster → SKIP.

### META — raw 8 / MEDIUM / final SKIP
- +3 accumulation 4 signals MEGA 0.601, +2 named confluence score=5 BULLISH (direct insights_signal_confluence hit), +1 gamma NEAR_FLIP 605, +2 watchlist $74M DP, +1 'best risk/reward — price has not moved' note; −1 dealer NEUTRAL SKIP conflict; **−1 flow_conflict_lite (90d −$491M; softened from full −3 because direct insights_signal_confluence=5 cross-confirms)**.
- 3a 3-of-4 PASS. Risk-gate: panic + cluster dup → SKIP.

### SPY — raw 7 / MEDIUM / final SKIP
- +3 dealer DEX REGIME FLIP NEG→POS today + vanna structural, +1 0DTE pin 738-743, +1 top-of-funnel #3, +0 contrarian SHORT-CALL-SPREAD CONFLICT surfaced, +3 1.12 BACKWARDATION panic-gate-active structural LONG-vol context, **−1 flow_conflict_lite (90d −$522M MIXED label)**.
- 3a 2-of-4 borderline. Risk-gate: self-panic −1 + index cluster (TLT carrier) −1 → SKIP.

### IWM — raw 7 / MEDIUM / final SKIP
- +3 vanna-squeeze SETUP, +1 backwardation 1.138 (trigger NOT FIRED), −1 TREND-acceleration gamma, −1 266P single-leg hedge, −1 top-of-funnel bearish $-16M, **−3 FLOW_CONFLICT FULL** (90d −$1.005B vs LONG setup).
- 3a 1-of-4 FAIL. Risk-gate: regime + panic + cluster → confirmed SKIP (quant pre-flagged for rejection).

### INTC — raw 7 / MEDIUM / final SKIP
- +3 sweep 5-of-5 LEAP-led non-mega-cap clean (hedge-flow filter not applied), +3 90d +$222M accretion, +1 top-of-funnel #6, +0 negative single-name VRP −0.16 = BUY VOL constraint surfaced.
- 3a 1-of-4 FAIL. Risk-gate: panic + semi cluster → SKIP. **NB: NEGATIVE VRP says debit structure only** — if revisiting, June ATM call debit spread half-size.

### TSM — raw 7 / MEDIUM / final SKIP (cluster carrier)
- +2 4-of-5 sweep cooled (today MIXED Jul P390 hedge), +3 90d +$547M BULLISH, +2 watchlist $26M DP + 43k OI.
- 3a 2-of-4. Risk-gate: panic alone takes STARTER to SKIP.

### SNDK — raw 7 / MEDIUM / final SKIP
- +2 sweep 4-of-5 MIXED (today $22M ASK + $22M BID Jun-2027 box), +3 90d +$784M BULLISH (highest in semi complex), +1 semi-leader 48% inst share, +1 top-of-funnel #5.
- 3a 1-of-4 FAIL. Risk-gate: panic + cluster → SKIP.

### CRWD — raw 7 / MEDIUM / final STARTER (only original FULL pre-risk in book)
- +3 earnings-scout BUY VOL Jun 3, last 4 prints 12/8/−5/18 vs implied small (insights_earnings_play + iv_term_structure)
- +2 $24M institutional bull flow aligned (options_flow_top_premium_trades)
- +1 cyber sector leader 49% inst share (sector-rotation)
- +1 top-of-funnel #9
- 3a 1-of-4 (earnings_vol class doesn't lean on accumulation gates). `win_rate` 0.825 high_iv_rank vol_realisation → pre-risk FULL.
- Risk-gate: panic −1 + VRP-vs-short-vol-lean −1 → **STARTER**.
- Structure: **iron condor 5-7% wide, May 30 expiry (POST-print)**. AVOID naked short straddle given FAIR VRP. Invalidation: post-print move >7% in either direction.

---

### Conviction-scoring rubric (embedded for audit reference)

```
Daily conviction score = Σ:
  +3  dealer-positioning DEX flip / vanna-squeeze in trade direction
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart_positioning, dark_pool_block_stratified institutional-tier)
  +1  multi-day OI BUILDING (≥5 days)
  +1  insights_conviction_matrix = DIRECTIONAL_LONG, confidence > 70
  +3  historical_cumulative_premium_flow shows net directional accretion in trade direction (30d window)
  +1  in sweep-tracker top 5 by hot_chains_sweep_persistence  [P1.1: SUPPRESSED for SPY/QQQ/IWM/SPXW + top-10 mega-caps unless cum_flow_30d aligns]
  +1  sector-rotation names ticker as single-name leader (persistence ≥ 3)
  +1  earnings-scout BUY VOL / SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored)
  +1  vol-surface KINKED/BACKWARDATION with VRP-aligned bias
  +1  opex-pin-strategist top-5 (OPEX week only)
  -2  contrarian-scanner overcrowded long with rising PCR z-score (VRP positive)
  -3  flow_conflict — 30d cum_flow direction clearly OPPOSITE dominant signal class, magnitude > today's union-median |cum_flow_30d|
  -1  flow_conflict_lite — 30d cum_flow MIXED (signed sum near zero or aligned but bottom-quartile magnitude)
  -1  risk-monitor flags in correlation cluster (corr > 0.7) — applied in 2b
  -3  risk_market_regime conflicts with trade direction — applied in 2b

Conviction tiers (2026-05-15 audit P0):
  ≥ 10 = HIGH (full size, subject to Step 3a 3-of-4 load-bearing gate + Step 5 win-rate gate)
  7-9  = MEDIUM (half size, subject to win-rate gate)
  3-6  = LOW (starter / watch-only)
  ≤ 2  = drop
```

---

## 8. Watch-only — single signal, no confluence

Candidates that surfaced from one Phase 1 agent but failed the confluence gate (≥2 distinct agents OR 1 agent + confluence ≥4). Listed for journaling, NOT for trade entry today:

- **POET** — DEC-2028 $40C 26,943 contracts ASK-led ($12M premium) — fresh LEAP OI build but stock +143% 30d micro-cap; conviction matrix only 30.5% DIRECTIONAL_LONG. Momentum chase.
- **CPNG** — potential LEAP-PUT (DIRECTIONAL_SHORT, only 52% confidence). Monitor for next session.
- **PANW** — earnings-scout BUY VOL Jun 2 ($9.4M net call buying) but failed confluence gate after CRWD cluster cap.
- **OKTA** — earnings-scout BUY VOL May 28 (3.6% implied vs 6-8% realized). Single-tool, no confluence — journal only.
- **ADSK** — earnings-scout BUY VOL May 28 (FLAT term, 2.6% implied). Journal only.
- **DG** — earnings-scout BUY VOL Jun 2 (2.6% vs 8% realized). Journal only.
- **HPE** — CALENDAR Jun 1 (5-Jun kink 98%). Single-tool. Journal.
- **GTLB** — BUY VOL Jun 2 (4.1% vs 10-15% realized) + KINKED Jun 5. Earnings-scout + vol-surface only — would qualify if a third agent picks up before 6/2.
- **ZS** — CALENDAR May 26 (May 29 kink 122%). Risk-monitor flagged as exit candidate (CRWD correlation 0.715 makes it redundant).
- **PLTR** — dealer LONG +$812B DEX only. Single-agent.
- **RCL / GE / BA / RKLB** — sector-rotation single-tool flags.
- **KWEB** — accumulation-hunter REJECTED (b/s 0.20 DISTRIBUTION) despite low PCR + $145M DP. Headline alert misleading; watchlist drop.
- **LRCX** — DISTRIBUTION b/s 0.48 despite top sweep premium. Drop.
- **SPX** — $9.4B C6000 box / calendar / diagonal complex is STRUCTURAL not directional; excluded per Phase 1 note.

---

## Watchlist write-back confirmation

`risk-monitor` confirmed: `mcp__uw-pp__watchlist_manage(action="add", group="conviction_2026-05-20", tickers=["AAPL","TLT","CRWD","MSFT","GOOG"])` succeeded. The five entries persisted include MSFT/GOOG despite today's gate-out — keeping them in the date-stamped group lets tomorrow's run measure whether the panic gate was correctly conservative or over-tight on duplicate accumulation. Verified by `watchlist_manage(action="list")`: `conviction_2026-05-20` = `["AAPL","TLT","CRWD","MSFT","GOOG"]`.

---

## Desk summary

Today is a study in **concentration risk colliding with a panic gate**. The quant produced an unusually deep candidate set (15 names at MEDIUM+ tier) but eight of the top scores are QQQ-correlated mega-cap or semi names, and QQQ's 1.455 SEVERE BACKWARDATION fires the panic gate on every one of them. The risk-monitor's cluster + panic stack cuts the equity-long book to **one carrier per cluster** — AAPL for mega-cap accumulation, TLT for the rates-diversifier role (promoted on uncorrelated thesis despite 3a-gate demotion), CRWD for cyber/software (re-structured from BUY-VOL straddle to iron condor under FAIR VRP), and ULTA as a gate-survivor on ConsCyc re-acceleration. Tiny ballast shorts in VLO (Energy decel) and NBIS (small-cap bear) round out the book. The hedge-sleeve recommendation is a small VIX call ladder, sized at 0.25R, on the read that institutions are already paying for tail (multileg-strategist surfaced a VIX 32/42/45 May-27 condor today). LEAP horizon is empty — institutions are short-dating their conviction (6.4% LEAP share). Tomorrow's `conviction_2026-05-20` group will tell us whether AAPL/TLT/CRWD continue accumulating and whether the panic gate stays valid or needs softening.
