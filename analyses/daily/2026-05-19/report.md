# Daily Market Analysis — 2026-05-19

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / UPTREND. SPY 733.73 (above 20/50 SMA, +3.53% 30d, −2.11% from 90d high). VIX 18.14, breadth weak 34.7% bullish. **Front-end IV ratios PANIC across all majors** (SPY 1.147 / QQQ 1.290 / IWM 1.142). SPY/QQQ/IWM all FULLY_NEGATIVE GEX 0–45d. **Cyclical→Defensive rotation** confirmed by 5d trajectory decay in Tech ($7.8B→$3.3B) + Cyclical ($2.15B→$464M) vs acceleration in Consumer Defensive ($54M→$122M) and Real Estate ($7M→$54M).
- **Top 0DTE play:** AAPL iron fly 295/300/305 expiring 2026-05-20 — dominant +GEX wall at 300 (295B), POSITIVE regime, spot 298.43 already in pin zone; invalidate >302 with volume.
- **Top swing build:** **BL (Blackline)** — raw_score 12 (only HIGH-tier name), 8/9 LEAP gates passed, Dec-18-26 C27.5 +13,016 OI dominant strike (ask-side 12,013 vs bid 2,697), DP B/S 10.77, DIRECTIONAL_LONG conviction 87.53%, cum prem flow +$12.8M 90d ALL recent (fresh thesis), buy-the-dip institutional ladder on −9.66% 30d. **Starter size** (forced by null backtest floor — no MCP signal-type for `leap_directional`). Structure: Dec-26 27.5/40 debit call spread. Invalidation: close below $25.80 DP floor or conviction matrix flips.
- **Top LEAP candidate:** Same as above — **BL** is the sole LEAP-grade name today. **NBIS** LEAP ladder is structurally similar but only 5/9 gates (failed cum_premium_flow direction).
- **Biggest risk:** Long-duration credit cluster (TLT/HYG corr 0.78) → keep TLT only. **Universal panic gate fired** (all 3 majors front-IV >1.10) → −1 tier applied to every directional name. **Net book is long-skewed 0.7** → hedge sleeve mandatory: QQQ 1-month put spread + VIX 22/27 call vertical.

---

## 1. Regime & Gamma State

**Regime classification:** TRANSITIONAL — Mixed signals, reduce position size, wait for clarity. SPY in UPTREND but breadth weak (34.7% bullish across 6,124 optionable tickers — 3,997 bearish). VIX 18.14, IV rank 14 (cheap vol).

**Per-index gamma table:**

| Ticker | Spot | 0DTE Zero-Gamma | Total GEX (0–45d) | Regime | Call Wall | Put Wall |
|---|---|---|---|---|---|---|
| SPY | 734.22 | 682.67 | −8.67T (FULLY_NEGATIVE) | **TREND** | 732/733/734 stacked + 738 (lone +GEX node) | 738 / 730 floor |
| QQQ | 701.52 | 596.77 | −1.15T (FULLY_NEGATIVE) | **TREND** | 698 / 700 | 704 / 705 |
| IWM | 272.38 | 259.14 | −0.95T (NEGATIVE) | **TREND** | 270–274 capped | none below until 259 ZGL |

**DTE share (institutional vs retail):** 0DTE 28% / weekly 28% / monthly 26% / LEAP 7% — BALANCED. Institutional weight modest; favors swing/LEAP over 0DTE today.

**VRP SPY:** FAIR (IV30d 0.1587 vs realised 0.1232, vrp=0.0355) — no premium-selling edge; vol-buyers also lack structural edge.

**Front-end IV panic:** SPY 1.147 / QQQ 1.290 / IWM 1.142 — **ALL > 1.10**. Universal panic gate fired by risk-monitor → −1 tier on every directional position.

---

## 2. 0DTE / Intraday Plays

**Per-index 0DTE setups (from gamma-flip-tracker):**

| Index | Setup | Structure | Invalidation |
|---|---|---|---|
| SPY | 732–738 chop band; long-gamma scalp through stacked walls | Long 735C/733P strangle first 90 min, harvest into lunch | Pins inside 733.50–734.50 >2h |
| QQQ | Negative GEX chase above 702.50 → 704/705 magnet | Long 0DTE 703C, scale at 704 | Rejection 702.50 + tick below 700 (flip to long 700P) |
| AAPL | Pin at 300 (dominant +GEX 295B, spot 298.43) | Iron fly 295/300/305 exp 2026-05-20 | Prints >302 with volume — cut at 301.50 |
| IWM | Below 270.50 → no dealer brake until 259 ZGL | Long 269P 0DTE on first close <271 | Reclaim 272 with rising breadth |

**0DTE single-name pin candidates:** NVDA 221 (today_expiry 5/22, +GEX 964B, walls 225/230/235/240 above), META 605 (today_expiry 5/20, NEAR_FLIP — mean-revert toward 610–615 if it clears 608).

**Surprises:** SPY 738 is the only long-gamma node above spot within 6pts → expect magnet/pin at 738 rather than continuation. VIX 65C (Jun) printed 201k volume **at the bid** = sold, not bought → far-OTM tail hedges monetized into 18 VIX print = "TREND but not panic."

---

## 2a. Swing Dealer Positioning (1–4 weeks)

**Per-index swing read (from dealer-positioning-strategist):**

| Ticker | DEX | DEX Traj 5d | Vanna-Squeeze | ZGL Traj 10d | Regime Flips | Swing Bias |
|---|---|---|---|---|---|---|
| SPY | −$53.4T | DETERIORATING (put accretion) | PRESSURE-only (book put-heavy, VIX rising) | FLAT-NEG | NO | NEUTRAL (LONG only on VIX roll) |
| QQQ | −$17.0T | DETERIORATING | PRESSURE-only | ZGL crashed 742→209 then nullified | **2 flips: POS→NEG 5/11, NEG→POS 5/18** | NEUTRAL (whipsaw) |
| IWM | −$8.0T | DETERIORATING | **PRESSURE-only (largest put-vanna ratio on board)** | FALLING 173→85 | **YES — POS today after FULLY_NEG yesterday** | **LONG IF VIX rolls** (best mechanical squeeze candidate) |

**Single-name swing standouts:**
- **MSFT (LONG)** — cleanest mega-cap: DEX +$10.1T, GEX rocketed 227B→627B today, ZGL stable at 418 (right at spot 424 = pin-magnet), POSITIVE 3 sessions. NOT on whale-alert list = pure dealer-positioning alpha.
- **NVDA (LONG, conflicted)** — DEX +$23.7T, GEX 379B→1.157T 10d (rising hard), charm massively POSITIVE. BUT: 5/5 bearish sweep persistence $7.18B 5d → internal conflict.
- **AAPL (LONG)** — DEX +$6.5T, GEX exploded to $813B today (4x yesterday) sitting on top of $148.5M DP print + 98K OI.
- **AMD (SHORT-flag)** — DEX/GEX **just flipped NEGATIVE today** (first negative in 10d). Contradicts bullish tape; smart money lifting puts.
- **TLT (LONG-pressure)** — DEX −$434B (put-heavy), TRUE vanna-squeeze setup but VIX/MOVE rising → SETUP, not TRIGGER.

**Vanna-squeeze candidates (gated on VIX roll):** IWM > TLT > QQQ > SPY. All in BUILDING phase — entry requires 3-session VIX decline AND front-IV ratio under 1.05.

---

## 2b. Sector Rotation

**Rotation regime call: CYCLICAL → DEFENSIVE** (medium confidence). All sectors raw persistence_score=1 but trajectory decisive.

| Sector | 5d Trend | Trajectory | Institutional Lean |
|---|---|---|---|
| Technology | 7.8B → 3.3B (−58%) | **DECAYING** | INSTITUTIONAL but cooling |
| Consumer Cyclical | 2.15B → 464M (−78%) | **DECAYING** | INSTITUTIONAL exiting |
| Industrials | 471M → 135M (−71%) | DECAYING | weakening |
| Healthcare | 510M → 152M (−70%) | DECAYING | cooling |
| Consumer Defensive | 54M → 122M (+126%) | **ACCELERATING** | INSTITUTIONAL (purest signal) |
| Real Estate | 7M → 54M (+643%) | **ACCELERATING** | INSTITUTIONAL (27% LEAP share — highest) |
| Energy | 208M → 230M (choppy, 556M spike 5/18) | STABLE-ACCEL | mixed |
| Utilities | 42M → 25M | STABLE | INSTITUTIONAL |

**Single-name leaders within rotating sectors:**
- **Defensive longs (high conviction):** COST (+$2.7M), WMT (+$1.45M), HRL (IVR 100 — contrarian institutional bottom-fish)
- **Real Estate longs:** AMT (+$1.01M tower REIT), DLR (+$780k data-center)
- **AI-power survivors:** GEV (+$4.2M), OKLO (+$4.1M), NRG (+$855k)
- **Defensive pharma:** LLY (+$6.5M), ABBV (+$2.1M)
- **Mega-cap tech distribution (short candidates):** AMD −$30.3M, NVDA −$27.5M, TSM −$21M, INTU −$18.2M, ASML −$16.1M

**Swing-book implication:** Net short cyclicals, net long defensives + AI-power-infra. Best long pair: COST/WMT/AMT/DLR. Best short pair: AMD/NVDA put spreads against the rotation. Thematic survivor sleeve (GEV/OKLO/VRT/RKLB) sized tighter — idiosyncratic flow in decaying sectors. **Invalidation:** Defensive 5d <$80M/day for 2 sessions, or Tech snaps back above $5B/day with renewed AMD/NVDA bullish premium.

---

## 3. Swing Setups (1–6 weeks)

### 3a. Long swings (regime-aligned)

| Ticker | Raw Score | Tier | Thesis | Structure | Final Size | Invalidation |
|---|---|---|---|---|---|---|
| **BL** | 12 | HIGH (LEAP) | 8/9 LEAP gates, DEC-18 C27.5 dominant strike ask-side 12k, DP B/S 10.77, 30d cum flow all recent +$12.8M, DIRECTIONAL_LONG 87.53%, buy-the-dip institutional ladder. 10d price 25.23→30.03 (+19%); 7 of 10 bullish flow days. | LEAP debit spread Dec-18-26 27.5/40 (~$5.50 debit, $7 max) | **starter** | Close below $25.80 DP floor, OR conviction matrix flips, OR cum_premium_flow turns net negative 10+ sessions |
| **TLT** | 10 | MED | DP mega 92.9% + block 69.1% buy, $697M, OI BUILDING 5/5 +1.75M, accumulation B/S 2.56, put-write 76/80 + call-buy ladder 85/86/87, vanna-pressure setup. Defensive rotation tailwind. Price 86.08→82.99 −3.6% 10d but flow accreting bullish. | Jul-26 ATM calls or 90/95 call spread | **starter** | TLT < 89.50 OR cyclical rotation reverses |
| **AAPL** | 8 | MED | DP mega 62.5% buy $1.81B, OI BUILDING 5/5, DEX +$6.5T, GEX vaulted $813B, pre-mkt cluster $297-298 above NBBO mid, +$473.8M 30d cum flow BULLISH. OI build at 300C (10 DTE +8,355), Jan-28 LEAP 300C +6,982 financed by Jan-28 250P short +6,414 (LEAP synthetic-long with put-write). | Jun-26 ATM calls; tight stop | **starter** | AAPL < 200 OR SPY breaks 720 |
| **WMT** | 3 | MED | Consumer Defensive accelerating, +$101M 30d cum flow BULLISH, IVR 67, earnings catalyst | Jun-26 ATM calls | **starter** | WMT < 95 OR Defensive rotation reverses |
| **NBIS** | 8 | MED | LEAP call ladder (140C 28-Jan, 180C 28-Dec, 210C 27-Jan) no_side 3800/4300 = synthetic long. IV 90.4 alert. | Skipped: regime/panic/sector triple penalty | **skip** | n/a |
| **MSFT** | 7 | MED | Dealer-positioning alpha only; DEX +$10.1T, GEX 227B→627B, ZGL pinning at spot. NOT on whale-alert list. | Skipped: Tech sector decay penalty | **skip** | n/a |
| **NVDA** | 7 | MED | DEX +$23.7T, GEX rising hard. CONFLICTED with sweep-bear 5/5. | Skipped: regime conflict + sector decay | **skip** | n/a |
| **META** | 6 | MED | Single mega-print $354M at $611 (DP 100% buy ratio). BUT 30d cum flow −$501M OPPOSITE. | Skipped: opposing flow + sector | **skip** | n/a |
| **MU** | 6 | MED | LEAP synthetic-long via multileg; KINK at 6/26. BUT 30d cum flow −$719M OPPOSITE | **skip / adverse-flow exit from yesterday's conviction** | n/a | Exit if held |
| **PANW** | 6 | MED | Bull call diagonal Jun + Sep/Oct calendar; earnings 5/21 | Skipped: panic + sector | **skip** | n/a |

### 3b. Short / fade swings (defined risk only)

| Ticker | Raw Score | Thesis | Final | Why |
|---|---|---|---|---|
| **TSLA** | 6 | 5/5 bearish sweep persistence $8.13B 5d | **skip** | 30d cum_flow +$938M BULLISH OPPOSITE the short |
| **AMD** | 4 | DEX/GEX flipped NEGATIVE today (first in 10d) | **skip** | 30d cum_flow +$344M BULLISH OPPOSITE |
| **TSM** | 4 | ZGL stubbornly above spot (414 vs 392), regime FULLY_NEG 8/10 | **skip** | 30d cum_flow +$546M BULLISH OPPOSITE |
| **STX** | 4 | BEARISH_EXTREME contrarian z=+3.44 → defined-risk BULL PUT SPREAD (fade the put bid) | Skipped: panic + sector | **skip** |

**Net short book today: zero** — every short candidate is over-ridden by adverse cumulative flow >$300M. The bearish premium tape is real but flow accretion remains long; risk-monitor refuses naked-short entries.

---

## 4. LEAP Builds (6–24 months)

**Sole LEAP-grade qualifier: BL (Blackline)** — see §3a row 1. 8/9 gates passed (only missed: position rolls = 0 today, which is neutral not failure). Cum prem flow signature is **fresh-thesis**: 30d window equals 90d window → all $12.8M bullish accretion is in the last 30 days. Dominant strike Dec-18-26 C27.5 has 12,013 ask-side volume vs 2,697 bid-side. IV rank 64.6 → use debit spread (27.5/40) rather than naked long calls.

**Position rolls detected today (informational, none LEAP-bullish):**
- VIX put 76,267 rolled fwd (tail hedge, macro)
- DVN call 11,077 rolled (energy thesis-extension, balance 0.594 below 0.7)
- NU put 8,964 + TOST put 5,724 (put protection extended)

**Disqualified near-misses (5-of-9 LEAP gates):**
- **NVDA** — OI BUILDING 10/10 +3.83M. Fails: conviction matrix MIXED @ 3.18%, calls ASK 468K vs BID 522K (net call SELLING into strength); 90d cum prem MIXED.
- **AMZN** — OI BUILDING 10/10. Fails: MIXED conviction, MIXED 90d.
- **CRWD** — OI BUILDING 10/10. Fails: MIXED conviction, 90d flow ≈0.
- **NBIS** — 3 LEAP call ladder blocks present but cum_premium_flow direction failed; 5/9.
- **MU** — OI BUILDING 10/10. Fails: 90d cum flow −$720M (heavy put hedging, wrong-direction signature). **Hard disqualifier.**

**Rejected outright:** META (COVERED_CALL conviction + 90d −$501M), HAL (DISTRIBUTION today despite +$5.3M 90d), ONTO (UNWINDING 5d OI).

---

## 5. Volatility Surface

**Universal observation:** Every scanned earnings name prints BACKWARDATION — pure earnings calendars, not panic backwardations. **All KINKED candidates are pre-earnings event humps.**

**KINK watch (earnings event humps):**

| Ticker | Earnings | Structure | R/R | Final |
|---|---|---|---|---|
| **ZS** | 5/27 | Long straddle 5/29 (29-May IV 123.2% > 22-May 98.5% > 5-Jun 101.9% = clean event kink riding inside broader backwardation) | 1.5:1 | **starter** (gated by panic) |
| **ZM** | 5/21 | Long ATM straddle 5/22 (implied 8.1% underprices 10% historical median) | 1.5:1 | **starter** |
| **ROST** | 5/21 | Calendar short 5/22 / long 6/18 ATM (front/far 2.48 EXTREME) | 1.8:1 | **starter** (defensive sector tailwind keeps it) |
| **WDAY** | 5/21 | Calendar (front/far 2.37) | 2:1 | skip (Tech sector decay penalty) |
| **ULTA** | 6/02 | Reverse calendar long 6/5 / short 6/12 (kink at 6/5 > 5/29 + 6/12) | 2:1 | skip (Cyclical decay) |
| **MU** | 6/24 (KINK at 6/26) | Long Jun26 / short Jul17 straddle — clean mid-curve event isolation | 2:1 | flagged but MU long thesis dies on flow_conflict |
| **CIEN** | 6/04 (bulge 6/5) | Long 6/5 / short 5/29 straddle | 2:1 | skip (sector) |
| **MRVL** | 5/27 (bulge 5/29) | Sell 5/29 / buy 6/12 straddle | 2:1 | skip (sector) |
| **ADI** | 5/20 | Iron condor 5/22 ±7% | 2:1 if move ≤ implied | skip (sell-vol into panic backwardation = wrong side) |
| **DLTR** | 5/28 | Short iron fly 5/29 ATM | n/a | skip (sell-vol vs panic) |
| **S** | 5/28 | Short strangle 5/29 ±10% | n/a | skip (sell-vol vs panic) |

**Long-dated skew dislocation:** All scanned AI-semi names (AMD/MU/MRVL/NBIS) show back-month CALL skew (25Δ call IV > 25Δ put IV by 7–9 vol pts) = no tail hedging priced into LEAPs. **Portfolio overlay opportunity:** cheap to roll LEAP put protection here for any net-long book — long-dated put wing structurally underbid.

**Single-contract IV outliers:** NVGS $1C 6/26 IV 986% size $1.38M = potential M&A whisper (flag for desk callback); WULF $8C 5/22 IV 1094% confirms crypto-miner squeeze setup.

**VRP-aligned bias:** With VRP=FAIR, neither short-vol nor long-vol has structural edge → favor **event-isolation calendars** (ZS, ZM, ROST kept; WDAY, CIEN, MRVL killed by sector gate); **avoid outright short premium** on back-month (no VRP cushion).

---

## 6. Risk & Correlation

**Universal gate fired:** Front-end IV ratios SPY 1.147 / QQQ 1.290 / IWM 1.142 → ALL > 1.10 PANIC → **−1 tier on every directional name** (no exceptions).

**Correlation clusters identified (>0.7 hard):**

| Cluster | Pair | Corr | Keep | Drop |
|---|---|---|---|---|
| C1 Long-duration credit | HYG/TLT | **0.78** | TLT (higher DP conviction) | HYG (−1 tier) |
| C2 Defensive retail | COST/WMT | **0.738** | WMT (higher flow +$101M) | COST (−1 tier) |

**Sub-threshold but flagged:** META/NVDA 0.642; META/MSFT 0.599; HYG/WULF 0.616 — noted, not cluster-penalized.

**Adverse-flow exits from yesterday's `conviction_2026-05-18`:**
- **MU** — adverse 30d cum flow −$719M OPP, IV rank 81 (vol expensive). **EXIT-CANDIDATE.**
- **TSM** — intraday flow flipped bearish (−$21M, P/C 1.31), $29.7M DP, +46K OI. **EXIT-CANDIDATE.**
- **TTWO** — IV 85 expensive, vol-crush risk post-thesis. **REDUCE.**
- **PLTR** — mixed (bearish flow but +71K OI). **HOLD.**
- **MA** — neutral, no action.

**Hedge sleeve (book is long-skewed 0.7 net):**
- **Primary:** QQQ 1-month 480/465 put spread (QQQ has highest backwardation ratio 1.29 → biggest crash optionality; size ~30% of long-book notional).
- **Secondary:** VIX 22/27 call vertical 30 DTE (lottery on second backwardation leg; size ~0.5% of book).
- TLT long itself acts as ~20% partial duration hedge to equity drawdown.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

Per-ticker breakdown sourced from `signal-confluence-quant` audit trail:

### BL — raw_score 12, HIGH tier
- **score_components:** +3 LEAP DIRECTIONAL_LONG @ 87.53% (leap-positioning-radar) · +3 OI BUILDING 10/10 +19,612 dominant Dec-18-26 C27.5 (oi_smart_positioning) **LOAD-BEARING** · +3 cum_premium_flow +$12.8M 90d BULLISH 4.96:1 (30d = 90d fresh) **LOAD-BEARING** · +2 dp_block_stratified B/S 10.77 **LOAD-BEARING** · +1 LEAP DTE 213 · +1 buy-dip −9.66% 30d institutional ladder
- **dominant_signal_class:** leap_directional · **win_rate:** NA (null backtest → starter floor)
- **load-bearing cited:** 4/4 (dp_block_stratified, cum_premium_flow, accumulation_via_oi, oi_smart_positioning) → P1.3 PASS
- **pre-risk size:** starter · **risk-monitor gates:** panic −1 (floor-held: LEAP 4/4 citations) · **final size:** starter
- **structure:** LEAP debit call spread Dec-18-26 27.5/40 · **invalidation:** close < $25.80 DP floor / conviction matrix flips / cum flow turns net negative 10+ sessions

### TLT — raw_score 10, MEDIUM tier (P1.3 implicit demote: cum_flow_30d MIXED → load-bearing tools only 3/4 positive)
- **score_components:** +3 accumulation 3+ signals (DP mega 92.9% + block 69.1%) **LOAD-BEARING** · +2 dp_block_stratified $697M **LOAD-BEARING** · +2 OI BUILDING 5/5 +1.75M · +2 oi_smart_positioning BULLISH (put-write 76/80 + call-buy 85/86/87) **LOAD-BEARING** · +2 multileg defensive complex · +2 dealer-positioning vanna-pressure put-heavy 2.4x · **−1 flow_conflict_lite** (30d $+8.1M MIXED, near zero)
- **dominant_signal_class:** dark_pool_accumulation · **win_rate:** NA
- **load-bearing cited:** 3/4 positive (cum_premium_flow not positive contributor)
- **pre-risk size:** starter · **gates:** panic −1 (floor-held: defensive rotation aligned) · **final size:** starter
- **structure:** Jul-26 ATM calls OR 90/95 call spread · **invalidation:** TLT < 89.50 / cyclical→defensive rotation reverses

### HYG — raw_score 8, MEDIUM tier
- **score_components:** +3 accumulation 3+ signals (DP mega 63.7% + block 70.7%) **LOAD-BEARING** · +2 dp_block_stratified $1.10B **LOAD-BEARING** · +2 OI BUILDING 5/5 +955k · +2 multileg credit-spread widening hedge · **−1 flow_conflict_lite** (30d −$32M BEARISH, magnitude below $50M threshold)
- **dominant_signal_class:** dark_pool_accumulation · **win_rate:** NA
- **load-bearing cited:** 2/4 → P1.3 cap MEDIUM
- **gates:** panic −1 + cluster −1 (dropped vs TLT) · **final size:** **skip**
- **batched-strategy disagreement note:** `playbook_batch_scan` returned "No Clear Edge — Stay Flat" → CONFIRMS skip.

### AAPL — raw_score 8, MEDIUM tier
- **score_components:** +2 accumulation Tier-2 (B/S 1.42 borderline) **LOAD-BEARING** · +2 dp_block_stratified mega 62.5% buy $1.81B **LOAD-BEARING** · +2 OI BUILDING 5/5 · +2 dealer-positioning LONG DEX +$6.5T / GEX vaulted $813B **LOAD-BEARING (dex)** · +2 cum_premium_flow +$473.8M 30d BULLISH **LOAD-BEARING** · +1 0DTE pin at 300 (gamma-flip pre-mkt cluster $297-298)
- **dominant_signal_class:** dark_pool_accumulation · **win_rate:** NA
- **load-bearing cited:** 4/4 (dp_block_stratified, cum_premium_flow, accumulation_detector, dex) → P1.3 PASS
- **pre-risk size:** starter · **gates:** panic −1, sector −1 (Tech decay; floor-held: +$473M flow override) · **final size:** starter
- **structure:** Jun-26 ATM calls; tight stop · **invalidation:** AAPL < 200 OR SPY breaks 720
- **batched-strategy disagreement note:** `playbook_batch_scan` returned "No Clear Edge — Stay Flat" — DISAGREES with multi-source institutional flag; prefer multi-agent confluence (DP+DEX+cum_flow all aligned bullish) per spec.

### NBIS — raw_score 8, MEDIUM tier
- **score_components:** +3 LEAP call ladder (140C 28-Jan, 180C 28-Dec, 210C 27-Jan) no_side 3800/4300 (multileg) · +2 whale alert IV 90.4 + $27M DP + 60K OI · +2 cum_premium_flow +$79.2M 30d **LOAD-BEARING** · +1 oi_smart_positioning synthetic-long
- **dominant_signal_class:** leap_directional · **win_rate:** NA
- **load-bearing cited:** 2/4
- **gates:** regime −1 (high-beta AI in TRANSITIONAL) + panic −1 + sector −1 (Tech decay) · **final size:** **skip**
- **batched-strategy disagreement note:** `playbook_batch_scan` flagged BEARISH_FLOW + HIGH_IV → BEAR CALL SPREAD; DISAGREES with multileg LEAP ladder read; prefer multileg (saw actual coordinated flow). Skip resolves the disagreement either way.

### MSFT — raw_score 7, MEDIUM tier
- **score_components:** +3 dealer-positioning DEX +$10.1T **LOAD-BEARING (dex)** · +2 GEX 227B→627B · +1 ZGL stable at 418 pin-magnet · +1 regime POSITIVE 3 sessions · +2 cum_premium_flow +$652M 30d MIXED but signed positive **LOAD-BEARING** · −1 flow_conflict_lite (MIXED label) · −1 not on accumulation list (dealer-only alpha)
- **dominant_signal_class:** gamma_breakout · **win_rate:** NA (gamma_breakout no MCP signal-type)
- **load-bearing cited:** 2/4
- **gates:** panic −1, sector −1 (Tech decay) · **final size:** **skip**

### NVDA — raw_score 7, MEDIUM tier
- **score_components:** +3 dealer-positioning DEX +$23.7T, GEX 379B→1.157T 10d **LOAD-BEARING (dex)** · +2 charm +$23.5B · +1 DP $11.3M block + 476K OI · +2 cum_premium_flow +$111M 30d **LOAD-BEARING** · **−3 flow_conflict** internal sweep 5/5 bearish vs long DEX
- **dominant_signal_class:** gamma_breakout · **win_rate:** NA
- **load-bearing cited:** 2/4
- **gates:** regime −1 (internal conflict) + panic −1 + sector −1 · **final size:** **skip**
- **batched-strategy alignment:** `playbook_batch_scan` flagged BEARISH_FLOW — confirms the internal multi-agent conflict; skip is correct.

---

### Conviction-scoring rubric (Step 4, embedded for auditability)

```
Daily conviction score = Σ:
  +3  dealer-positioning DEX flip / vanna-squeeze in direction
  +3  3+ aligned signals in accumulation (DP+OI+oi_smart, dp_block_stratified institutional-tier confirmed)
  +1  multi-day OI build (historical_oi_trend BUILDING ≥5d)
  +1  insights_conviction_matrix DIRECTIONAL_LONG, confidence > 70 (LEAP gate; demoted as positive scorer)
  +3  historical_cumulative_premium_flow net directional accretion (30d aligned)
  +1  sweep-tracker top 5 by hot_chains_sweep_persistence count [SUPPRESSED for SPY/QQQ/IWM + top-10 mega-caps unless cum_flow_30d aligned]
  +1  sector-rotation single-name leader within rotating sector (persistence ≥ 3)
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored)
  +1  vol-surface-scout KINKED or BACKWARDATION with VRP-aligned bias
  +1  opex-pin-strategist top-5 (OPEX week only)
  −2  contrarian-scanner overcrowded long with rising pc_zscore (VRP positive)
  −3  flow_conflict — cum_premium_flow 30d direction clearly opposite dominant_signal_class
  −1  flow_conflict_lite — 30d cum flow MIXED (signed sum near zero, or aligned but bottom-quartile magnitude)
  −1  risk-monitor correlation cluster (corr > 0.7) — applied in 2b
  −3  risk_market_regime conflicts with trade direction — applied in 2b

Tiers (2026-05-15 P0):  ≥10 HIGH (full) · 7–9 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 drop

P1.3 HIGH-tier load-bearing-tool gate: raw_score ≥ 10 requires ≥3 of {dark_pool_block_stratified, historical_cumulative_premium_flow, insights_institutional_accumulation, options_structure_dex} as positive scorers → else demote to MEDIUM
```

---

## 8. Watch-only — single signal, no confluence

Names that surfaced from a single Phase 1 agent but failed the confluence gate (single-tool flag, no second agent or insights_signal_confluence ≥4 backing). Listed for journaling — NOT for trade entry today:

- **AVGO** — only sweep-tracker (3/5 bull persistence $393M); cum_flow_30d +$56.8M signed positive but mixed label.
- **WULF** — sweep + multileg agreement on structure, but raw 6 with 1/4 load-bearing; size pinned by 28.1% win_rate proxy → starter then skipped by gates.
- **AMZN** — sweep + multileg agreement; raw 5; cum_flow $+92.5M aligned but won't survive panic + sector gates.
- **COST, GEV, AMT, DLR, OKLO, LLY** — sector-rotation pure-plays (single-signal); AMT/DLR/OKLO/LLY dropped at raw_score < 3 floor.
- **HRL, NBIS, NVGS (M&A whisper)** — vol-surface outliers without flow confirmation.
- **CRWD** — contrarian z=+1.98 just below ±2σ gate; watch for tomorrow's print.

---

## 9. Watchlist Write-Back

**`watchlist_write_back_confirmation: SUCCESS`**

Top-5 by post-risk conviction written to group `conviction_2026-05-19`:
- **BL** (raw 12, starter)
- **TLT** (raw 10, starter, defensive rotation aligned)
- **AAPL** (raw 8, starter, +$473M flow override)
- **ZS** (raw 4, starter, long-vol earnings)
- **WMT** (raw 3, starter, defensive sector accelerating)

Tomorrow's run will automatically pull `watchlist_alerts` against these five and flag adverse-flow exit candidates.

---

## 10. Operator notes

- **All 3 majors front-end IV >1.10** is the single most binding gate today. If front-end ratio collapses to <1.05 tomorrow, re-evaluate the universally-skipped MSFT / NBIS / META / AAPL roster — most of these had multi-source confluence killed only by the panic + sector double-hit.
- **Vanna-squeeze trigger watch:** IWM > TLT > QQQ > SPY. Enter LONG when VIX prints lower for 3 consecutive sessions AND front-end IV ratio rolls under 1.05. Currently VIX 18.14 and rising — setup BUILDING, not TRIGGERING.
- **AMD DEX/GEX flipped negative today** = first warning sign for the AI-semi mega-cap leg. Watch for confirmation tomorrow; if it persists, short-spread entry on AMD becomes the cleanest contrarian play against consensus longs (NVDA carries similar risk but with massive +$23.5B charm tailwind still intact).
- **MU exit-candidate from yesterday's conviction** — 30d cum flow now $-719M OPPOSITE the long thesis despite continued OI BUILDING. Treat as adverse-flow exit, not a hold.
