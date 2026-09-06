# Daily Market Analysis — 2026-05-18

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL UPTREND. SPY 738.65 (+4.01% 30d, above 20/50 SMA, −1.45% from 90d high) but breadth narrow at 35.7% bullish (3947 bear / 2196 bull). SPY GEX deeply negative (−$479B, ZGL gap, regime fully-negative), QQQ negative (-$330B 0–45d, two regime flips in 10d), IWM regime-flippy. VIX 17.82. VRP FAIR (SPY IV30 15.5% vs realised 12.0%, +3.5pp — no premium edge). DTE mix monthly-dominant (institutional). Tech premium decelerating 5d (5.4B→6.6B→7.8B→5.4B→3.5B trough), Energy accelerating (+757% 5d). Rotation call: **growth → commodities**.
- **Top 0DTE play:** **NVDA pin** 220/225 (POSITIVE GEX +$874B, dealer-long magnet to 222.50). Iron-fly 220/225 if spot holds the corridor; invalidation = breach 225 with >1% range expansion, or 220 fails into 217.5–220 negative-gamma pocket.
- **Top swing build:** **MU SHORT** (raw 8, HIGH). Sweep-tracker bear 5/5 ($5.28B 5d), dealer-positioning chaos (4 GEX regime flips in 6d, call-book unwinding), Tech-decel sector tailwind, 30d cum −$821M strongly aligned. win_rate 0.652. **Half size.** Structure: Jun-19 670/620 put vertical (4-week debit, earnings 6/24 catalyst risk — keep behind 6/19 expiry or roll to 7/17). Invalidation: MU reclaims $720 with semis flow flipping positive.
- **Top LEAP candidate:** **None.** Strict 6-of-9 gate stack returned zero qualifying names. Closest miss (5/9) was AAPL — strong DP accumulation but COVERED_CALL conviction matrix caps upside. Stand down LEAP capital today.
- **Biggest risk:** **No correlation cluster >0.7** in candidate set, but soft software-growth cluster (PLTR/WDAY/CRWD/TTWO 0.51–0.61) demoted by gate stack. QQQ front-end IV ratio 1.13 + NVDA 1.73 = front panic — apply panic gate to any tech-orbit long. Recommend SPY Jun 720/710/700/690 put condor + VIX Jun 35C ladder as protective layer (mirror of multileg-detected institutional hedge fabric).

## 1. Regime & Gamma State
- `risk_market_regime`: **TRANSITIONAL — Mixed signals, reduce position size, wait for clarity.** UPTREND on SPY (above 20/50 SMA), breadth 35.7% bullish (narrow, rolling-over risk). Money flowing INTO Consumer Cyclical (+$11.6M), Energy (+$9.1M), Healthcare (+$8.0M); OUT of Technology (−$299.8M, narrow leadership rolling), Communication Services, Basic Materials.

| Index | Spot | Zero-Gamma | Total GEX (0–45d) | Regime | Call Wall | Put Wall |
|---|---|---|---|---|---|---|
| SPY | 737.21 | (no nearby ZGL) | −$479B (FULLY_NEGATIVE) | NEGATIVE / NEAR_FLIP | 741/742 thin | 735 (−$9.1T 0DTE), 736, 737 |
| QQQ | 704.23 | 510.94 (irrelevant) | −$330B (FULLY_NEGATIVE) | NEGATIVE / TRENDING | (no upside wall to 710) | 700 (−$2.13T), 703, 704, 705 |
| IWM | 276.42 | 264.08 / 85.94 | −$1.41T 0DTE | NEGATIVE / PIN-TO-FLIP | 280 thin (+$71B) | 276 (−$723B), 275, 274 |

- `options_flow_dte_volume_share`: 0DTE 5.2%, weeklies 21.2%, monthlies 23.6%, LEAPs 7.2% → **BALANCED, monthly-dominant = institutional positioning, not retail churn.** SPY/QQQ today-expiry shares are materially heavier than the market aggregate (SPY 25.7%, QQQ 24.6%, NVDA 23%+).
- `historical_vrp`: IV30 15.49% / Realised 11.98% / **VRP +3.51pp = FAIR.** No premium-selling edge; non-directional vol trades sized conservatively.

## 2. 0DTE / Intraday Plays
- **SPY:** coiled negative-gamma squeeze inside 735–737 cluster. Break 738 → vacuum to 741. Loss of 734 → flush 732. Trade: buy gamma at the breakout edges, no pin trade today.
- **QQQ:** stacked −GEX 700–705. Spot 704. Asymmetric — no support wall nearby. Break 705.50 unlocks vacuum to 710. Trade: buy gamma upside, fade is intraday-only.
- **NVDA:** **POSITIVE GEX +$874B, classic pin** at 222.50 (dealer-long magnet). Iron-fly 220/225 if range holds; invalidation = 225 breach >1% expansion or 220 fail.
- **TSLA:** intraday short-gamma band 405–412.5, spot inside at 411. Long 410 straddle hedged with 425C if range expands; switch to fade if 410 pin holds through 14:00.
- **IWM disqualified** for 0DTE play (12% today-share insufficient).
- **OPEX pin work:** N/A — post-OPEX +1 trading day, pin mechanics dissolved. `opex-pin-strategist` not spawned this session.
- **Sweep urgency:** NVDA 6/12 200P whale $1.6M (5/5 persistence) and MU 5/22 OPEX put complex remain the most urgent near-term directional tickets, but both sized in §3 not as 0DTE plays.

## 2a. Swing Dealer Positioning (1–4 weeks)
Headline: indices have vanna-squeeze setup architecture (put-heavy DEX) **but VIX-rising / front-end IV backwardation = squeeze invalid → "vanna pressure, not squeeze."** Semis paradox resolved: NVDA dealer book is POSITIVE GEX +$874B absorbing the bearish SMH/SOXL hedges; MU broke down with 4 regime flips in 6d (dealer chaos); AMD call book deflating.

| Ticker | DEX state | 5d DEX | Vanna squeeze | ZGL traj | Front IV | Swing bias |
|---|---|---|---|---|---|---|
| SPY | NEGATIVE −8.59T | deteriorating | NO (VIX rising) | falling, no flip | FLAT 0.97 | **SHORT** |
| QQQ | NEGATIVE −5.97T | deteriorating | NO (front panic 1.13) | flipped POS→NEG 5/11 | BACK 1.13 | **SHORT → mean-revert** |
| IWM | NEGATIVE −4.74T | deteriorating | NO | repeated POS/NEG churn | n/a | NEUTRAL lean SHORT |
| NVDA | POS +23.39T | improving (call-heavy) | NO (IV 1.73 backwardation = panic) | rising hard (153B→874B) | BACK 1.73 | **LONG into print, fade post** (conflicted with sweep) |
| AMD | POS +0.22T | flat → deteriorating | NO | falling 5.5B→2.0B | n/a | NEUTRAL lean SHORT |
| MU | POS +0.36T | violently unstable | NO | **4 regime flips/6 sessions** | n/a | **SHORT** |
| AAPL | POS +3.29T | improving | n/a | n/a | n/a | LONG |
| AMZN | POS +2.05T | improving | n/a | n/a | n/a | LONG |
| META | POS +0.36T thin | weak | n/a | n/a | n/a | NEUTRAL |
| TSLA | POS +1.38T | flat | NO | n/a | n/a | NEUTRAL |

## 2b. Sector Rotation
**Regime call: growth → commodities (medium confidence).** All 11 sectors persistence_score=1 INFLOW — the signal is in trajectory math, not the binary sign.

| Sector | 5d trajectory | Direction | Δ% |
|---|---|---|---|
| Energy | 65→208→1151→183→**557** ($M) | ACCELERATING | +757% |
| Technology | 5454→6610→7814→5440→**3464** ($M) | Decelerating hard (trough) | −37% |
| ConsCyc | 1272→2150→1111→817→**412** ($M) | Decelerating hard | −68% |
| Industrials | 497→472→470→417→**310** ($M) | Decelerating | −38% |
| Healthcare | 413→422→511→200→184 ($M) | Decelerating | −56% |
| CommServ | 564→1239→967→762→766 ($M) | Steady | +36% |

Only Energy is genuinely accelerating against Tech/Industrials/ConsCyc/Healthcare decel. Inside Tech: bearish semi leadership (MU −$123M, NVDA −$62M, SNDK −$56M, ASML, AAOI, FSLR, STX, LITE) drives the decel; non-semi tech (AMD, AVGO, AAPL, NOW, INTC) still bullish but masked. Healthcare is **not** a rotation destination (LEAP-dominant 61% — structural positioning, not active rotation). ConsCyc and Industrials are NOT clean cyclical-on rotations — they're decelerating themselves.

**Energy single-name leaders (sector_rotation tag):** VLO, CCJ (uranium), PSX, SLB, HAL. (All gate-dropped today as single-source confluence — surface in §8 watch-only.)

**Implication for the swing book:** institutional money is leaking from semis-led growth into commodities (Energy + uranium). Defensive baskets are not the destination — pure-cyclical rotation is not yet validated. Use Energy refiners and uranium as the long-side rotation expression once confluence builds.

## 3. Swing Setups (1–6 weeks)

### 3a. Long swings (regime-aligned, post-gate sized)

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **MA** | **9** HIGH→MED (NA bt) | 4/4 load-bearing accumulation stack: block-stratified mega-buy 1.00 ($375.9M after-hours at-ask $505.79), institutional_accumulation 9.52 ratio, OI BUILDING 5/5d (+17,376), DIRECTIONAL_LONG conviction-matrix. 10d price 491→505 grinding up; today flips bullish after 7-day base. Earnings 7/30 (far). | **Aggressive long calls** OR Jun-19 510/525 call vertical (debit, captures 5/22 500/505/525C OI build) | MA loses $505.79 DP support → next defense $499–500; OR conviction_matrix flips to COVERED_CALL/HEDGED_LONG; OR OI starts UNWINDING for 2+ sessions on 5/22-6/18 call strikes | **starter** (NA backtest gates from full despite raw 9) |
| **CRWV** | 4 MED | Vol-surface dislocation: backwardation 1.36 with IV pct only 30.8 (z-0.71, statistically cheap). LEAP put accumulation suggests institutional protection but front-end is mispriced. | **Long calendar** — buy Aug-2026 ATM straddle, sell May-29 ATM straddle (captures front IV crush + holds long vega) | Front IV ratio >1.45 by 5/22 (panic intensifying) OR VRP flips solidly positive | **half** (calendar absorbs panic; sector-decel −1, soft cluster −1) |
| **WDAY** | 5 MED | Earnings 5/21 AMC. Front/far IV ratio 2.21 — most extreme panic on the board. Analyst-bullish base vs bearish premium flow ($4.6M vs $3.7M, PCR 0.51) = market pricing a miss. | **Calendar** — sell 5/22 ATM straddle, buy 6/18 ATM straddle (collects 5/22→6/18 IV normalization regardless of direction) | Front/far ratio stays >1.20 post-print (event still pending — rare on calendars) | **starter** (gates: panic −1, soft cluster −1, sector-decel −1) |

**Supporting candidates (LOW tier, surfaced but not active book):**
- **AMZN** (raw 7, MED, dropped post-gates): dealer-positioning LONG (DEX +2.05T improving), bullish flow flip today (+$48.5M) after 7-day bearish base. 6/18 270C OI build +6612, 5/22 275C +4560. IV cheap at 21. Panic + ConsCyc decel collapsed to skip. Re-rank if QQQ front-end <1.05.
- **TSM** (raw 6, MED, dropped post-gates): sweep bull 3/5 + DP $69M / OI +77K watchlist alert + 30d cum +$567M strongly aligned. Panic + sector-decel gated. Re-rank if semis flow flips positive on persistence basis.
- **PLTR** (raw 5, MED, dropped post-gates): cheap-vol vanna-squeeze setup (IV pct 0.0, VRP −0.059), confluence score 5. Panic + sector-decel gated. Re-rank if QQQ front-end <1.05.
- **CRWD** (raw 6, MED, dropped post-gates): earnings BUY VOL light, bullish flow + multileg context. Panic + cluster + sector triple-gated.
- **AAPL** (raw 4, LOW): dealer-positioning LONG, top bullish premium leader, but HIGH-gate failed 1/4 load-bearing — DP large but COVERED_CALL conviction caps upside. Panic + sector-decel skip.

### 3b. Short / fade swings (defined-risk only — TRANSITIONAL prohibits naked shorts)

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **MU** | **8** HIGH | 3-agent confirmation: sweep bear 5/5 persistent ($5.28B 5d), dealer-positioning chaos (4 GEX regime flips/6d, call-book unwinding), Tech-decel sector tailwind. 30d cum −$821M strongly aligned (largest aligned magnitude in union). 10d price 639→795 peak 5/11 → 681 today (−14% rollover). Top OI: huge deeply-OTM put writes (6/05 45P/40P at $0.01 = premium harvesting), 5/22 400P and 615P closer to spot. Earnings 6/24. | **Bear call spread** Jun-19 700/750 (credit) OR Jul-17 670/620 put debit if you want exposure past earnings catalyst | MU reclaims $720 with semis flow turning net-positive on persistence ≥2d, OR sweep persistence flips to mixed | **half** (win_rate 0.652; no demotion — sector tailwind aligns) |
| **TTWO** | **6** HIGH | Post-earnings IV crush window. Front IV 139% / back 49%, ratio 2.17 — back-skew complacent (call=put 25Δ). Bearish confluence top-table 5: bearish_flow + dp_distribution + oi_building_puts + high_iv_sell_premium + volume_spike. VRP +0.241 = premium-selling regime locally. | **Short 5/22 strangle** (post-event) OR **calendar** sell 5/22 ATM call vs buy 7/17 ATM call | TTWO IV30 reflates >25 pre-realisation; OR stock gaps >1.5σ on print residual | **half** (global TRANSITIONAL −1) |

**Quant SKIP'd shorts (audit visibility):** NVDA (flow_conflict −3: dealer-pos LONG vs sweep+sector SHORT, 30d cum +$139M long while signal says short), QCOM (flow_conflict −3: bullish premium leader vs sweep bear), MSTR (single-source bear vs +$223M long flow), AMD (single-direction agent only).

## 4. LEAP Builds (6–24 months)
**Empty bucket.** Strict 6-of-9 gate stack returned zero qualifiers. Near-misses for journaling:

- **TLT** (4/9) — large OI build (+651K contracts) and BUILDING 10d, but LEAP layer is BIDIRECTIONAL (top adds include 27-Mar P45 +41K, 27-Jun P75 +22K, 28-Jan C92 +7K). This is a rates-vol straddle book, not a directional duration call. MIXED conviction 0.37 confidence. Re-evaluate if puts unwind and call layer dominates.
- **AAPL** (5/9, strongest near-miss) — BUILDING 10d, DP accumulation 2.69 buy/sell, 90d cum +$465M BULLISH. But fresh LEAP put 27-Jun P290 +9,568 ($23.3M premium, bearish) AND conviction = **COVERED_CALL 25.12 confidence** (call-writing on top of stock long = yield enhancement, not LEAP buy). Will qualify if call-write flow rotates to call-buy on the 0.7+ DP buy-ratio base.
- **NVDA** (5/9) — LEAP 27-Jan C240 +7,304 ($25.9M ask-side biased), price +24.83% 30d. But 90d cum MIXED +$139M on $35.6B gross = noise; conviction MIXED 5.85 confidence. Too late in the run; LEAP whales already paid.

No LEAP-grade rolls detected (VIX/CCJ puts unwind, balance ratios <0.25 = de-risking not thesis extension).

## 5. Volatility Surface
- **KINKED** (binary-event expiries detected manually — classifier returned no formal kink): CIEN 6/05 (115.3% IV vs 97.6/109% adjacent), CIEN 12/18, MU 6/26 (107.8% vs 97.3/103.5%), MU 11/20. CIEN 6/5 and MU 6/26 are highest-conviction event-priced.
- **BACKWARDATION watch:** WDAY 2.21 (event), TTWO 2.17 (IV crush imminent — see §3b), GTLB 1.49 (pre-earnings), **CRWV 1.36 (statistically cheap, IV pct 30.8 — the surface dislocation of the day, see §3a)**, MU 1.29 (earnings priced 6/26), SNDK 1.27, STX 1.39. WDAY/GTLB/CIEN handed to earnings-scout; CRWV/TTWO traded.
- **IV outliers:** dominated by 0DTE pin noise + small-cap lottery (FIG, MARA, HIVE). **No institutional-grade single-contract mispricings today.**
- **Cheap-vol long candidates (VRP-negative, low IV pct):** PLTR (IV pct 0.0, VRP −0.059), MELI (IV pct 11.5, VRP −0.116 — largest negative VRP in scan). Both gate-dropped today.

## 6. Risk & Correlation
- **No pair >0.7 correlation in candidate set.** Highest soft cluster: software-growth (PLTR/WDAY 0.61, CRWD/PLTR 0.60, CRWD/WDAY 0.59, PLTR/TTWO 0.51). Treated as soft cluster — max 2 names sized >starter. TTWO/PLTR ranked above CRWD/WDAY for primary sizing; CRWD demoted −1 tier as redundant beta.
- **Regime gate (TRANSITIONAL UPTREND, breadth 35.7%):** global half-size bias applied to all longs; no penalty for short side which aligns with breadth narrowing.
- **Front-end IV panic gate:** QQQ 1.13 + NVDA 1.73 = panic. Applied −1 tier to AMZN/TSM/AAPL/CRWD/PLTR/WDAY (QQQ orbit). Did NOT apply to MU SHORT (panic helps), TTWO (post-event IV crush is normal in FAIR VRP), CRWV (long-back calendar absorbs panic).
- **VRP gate:** FAIR — no structural premium edge. No demotions beyond panic-specific.
- **Adverse sector rotation gate (Tech-decel):** −1 tier on TSM, CRWD, PLTR, WDAY, CRWV, AAPL. AMZN −1 (ConsCyc decel). MU SHORT benefits (no demotion). MA financial-services untouched.
- **Hedge sleeve:** book is delta-balanced (MU short + WDAY/TTWO short-vol vs MA/CRWV long). Book directional skew below 0.6 threshold — no mandatory hedge. **Recommended:** SPY Jun 720/710/700/690 put condor + VIX Jun 35C ladder (mirror of multileg-detected institutional hedge fabric — long upside via SPX 6000C ladder financed by put condor across SPY/IWM/IGV + VIX 35C calendar tail).
- **Adverse-flow exits from `conviction_2026-05-15`:** **NVDA** (net −$61.7M flow, IWM-correlated put hedge load 1.14M put volume, p/c 2.46) → EXIT confirmed (also today's quant-skip). **IWM** put-OI +802K, p/c 2.46, bearish flow → EXIT / treat as macro-hedge instrument only. SNOW HOLD (DP accumulation, do not chase rich premium). ETN HOLD passive. TTWO re-promoted to today's book (short-vol).

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7 + active book)

Active book post-gate (sized today): **MU SHORT (half), TTWO (half), CRWV (half), MA (starter), WDAY (starter).** Below: full audit trail for every name with raw ≥ 7 plus active-book additions.

| Ticker | Raw | Score components (agent:tool:pts) | Dominant signal class | Confl. | Cum flow 30d | Win rate | LB tools | Pre-risk size | Gates applied | Final size | Invalidation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **MA** | **9** | accum:block_stratified +3 / accum:institutional_accumulation +2 / accum:oi_trend +2 / accum:conviction_matrix +2 / dealer:dex +1 / flow_conflict_lite −1 | dark_pool_accumulation | 4 | −$46M (sub-median lite) | NA (newly covered) | 3/4 | starter | none meaningful (no QQQ orbit, sector untouched) | **starter** | Loses $505.79 DP support; conviction flips COVERED_CALL/HEDGED_LONG |
| **MU SHORT** | **8** | sweep:persistence +3 / dealer:gex_time_series +2 / sector:flow_persistence +2 / sweep:top_premium_trades +2 / accum:dp_summary +1 / cum_flow aligned +2 (largest aligned magnitude) | bearish_flow | 3 | −$821M aligned strong | 0.652 | 3/4 | half | regime no-op; panic helps; sector tailwind; no cluster | **half** | MU reclaims $720 with semis flow turning positive ≥2d; OR sweep persistence flips mixed |
| **AMZN** | **7** | dealer:dex +2 / signal_confluence +3 (score 5) / sweep:top_premium_trades +2 / cum_flow aligned 0 (sub-median) | bullish_flow | 5 | +$72M aligned | 0.269 | 2/4 | starter | panic −1; ConsCyc decel −1 | **skip** (gate-stack 2× to floor) | n/a |
| **CRWD** | 6 | earnings:earnings_play +3 / sweep:top_premium_trades +2 / multileg:hot_chains_multileg +2 / flow_conflict_lite −1 | earnings_vol | 3 | −$7M lite | NA (caps 0.90 non-dir) | 1/4 | half | panic −1; cluster −1 (redundant TTWO/PLTR); sector −1 | **skip** | n/a |
| **TSM** | 6 | sweep:persistence +3 / accum:dp_summary +2 / cum_flow aligned strong +1 | bullish_flow | 3 | +$567M aligned strong | 0.269 | 2/4 | starter | panic −1; sector −1 | **skip** | n/a |
| **TTWO** | **6** (HIGH override) | earnings:earnings_play +3 / vol_surface:vrp +2 / signal_confluence +2 (bearish 5) / cum_flow MIXED 0 | earnings_vol | 5 | +$5M MIXED | 0.90 (vol_realisation cap) | 2/4 (n/a directional) | full | global TRANSITIONAL −1 (cluster lead, no double demote) | **half** | TTWO IV30 reflates >25 pre-realisation; OR gap >1.5σ on print residual |
| **PLTR** | 5 | vol_surface:iv_term_structure +2 / signal_confluence +3 (score 5) / cum_flow 0 (sub-median) | vanna_squeeze | 5 | −$17M sub-median | 0.571 | 1/4 | half | panic −1; sector −1 | **skip** | n/a |
| **WDAY** | 5 | earnings:front_end_iv_ratio +3 (2.21 panic) / vol_surface:iv_term_structure +2 (back 2.21) / cum_flow MIXED 0 | earnings_vol | 3 | +$16M MIXED | 0.90 (non-dir cap) | n/a | full | panic −1; cluster −1; sector −1 | **starter** | Front/far ratio >1.20 post-print |
| **CRWV** | 4 | vol_surface:iv_term_structure +3 (back 1.36 + IV pct 30.8 cheap) / gamma_flip:today_gamma_flip +1 / sweep:top_premium_trades +1 / cum_flow 0 (sub-median) | earnings_vol | 3 | +$56M aligned sub-median | 0.90 (non-dir cap) | n/a | full | panic no-op (calendar absorbs); cluster −1; sector −1 | **half** | Front IV ratio >1.45 by 5/22; VRP flips positive |
| **AAPL** | 4 (LOW) | dealer:dex +2 / sweep:top_premium_trades +2 / cum_flow 0 (normal AAPL) | bullish_flow | 3 | +$465M (normal AAPL baseline) | 0.269 | 1/4 (DEX only) | starter | panic −1; sector −1 | **skip** | n/a |
| **NVDA** | **3** | dealer:dex LONG +2 / sweep:persistence BEAR +3 / sector:flow_persistence BEAR +2 / sweep:top_premium +2 / flow_conflict −3 (30d +$139M above median, OPPOSITE bear signals) / cross_agent_conflict −3 | bearish_flow CONFLICTED | 3 | +$139M long (opposite) | 0.652 | 1/4 | skip | n/a — quant-skipped | **skip** | n/a |

### Conviction-scoring rubric (embedded for audit)
```
Daily conviction score = Σ:
  +3 dealer-positioning DEX flip / vanna-squeeze setup in trade direction
  +3 3+ aligned signals in accumulation-hunter (DP + OI + smart_positioning, block_stratified institutional confirmed)
  +1 multi-day OI build (BUILDING ≥5d)
  +1 insights_conviction_matrix DIRECTIONAL_LONG conf >70 (LEAP gate; demoted as positive scorer)
  +3 historical_cumulative_premium_flow 30d net directional accretion in trade direction
  +1 sweep-tracker top-5 by hot_chains_sweep_persistence (P1.1 hedge-flow filter applies to indexes/mega-caps)
  +1 sector-rotation single-name leader (persistence ≥3)
  +1 earnings-scout BUY/SELL VOL
  +2 multileg-strategist directional structure (term-structure-anchored)
  +1 vol-surface KINKED/BACKWARDATION with VRP-aligned bias
  +1 opex-pin-strategist top-5 (OPEX week only — N/A today)
  −2 contrarian-scanner overcrowded long with rising P/C z-score
  −3 mechanical flow_conflict (30d cum opposite direction, above-median magnitude)
  −1 flow_conflict_lite (MIXED 30d cum)
  −1 risk-monitor correlation cluster >0.7
  −3 risk_market_regime conflicts with trade direction

Tiers: ≥10 HIGH (full); 7–9 MEDIUM (half); 3–6 LOW (starter/watch); ≤2 drop.
HIGH-tier gate (Step 3a): requires 3 of 4 {block_stratified inst, cum_premium_flow accretion, institutional_accumulation, DEX bullish-aligned}.
```

## 8. Watch-only — single signal, no confluence

Surfaced for journaling only. Single-agent flag without confluence ≥4 or load-bearing tool support. Re-evaluate if multi-agent confirmation builds tomorrow.

- **Energy rotation leaders (sector_rotation tag, single-source):** VLO ($259, IVR 60, monthlies 43%), CCJ ($105, IVR 53, $2.1M net flow), PSX ($180, IVR 70, refiner pair to VLO), SLB, HAL. Long-bias setup if confluence builds tomorrow on persistence; otherwise the rotation thesis is sector-level, not single-name actionable.
- **Sweep single-source bulls (no confluence support):** NBIS (bull 4/5 sweep, but today's −$20M flow says momentum stalling), AVGO (bull 3/5 sweep, no DP/OI corroboration), ORCL (bull 3/5), SLV (bull 3/5 — aligns with growth→commodities but no second agent), TSM (DP+OI alert but no DEX/accumulation confirmation; on watchlist).
- **Sweep single-source bears:** MSTR (bear 3/5 contradicted by +$223M long cum flow).
- **Single-direction agent shorts:** AMD (dealer SHORT lean only; DP+OI direction-ambiguous in tech-decel tape).
- **Cheap-vol longs (vol-surface only):** MELI (IVR 11.5, VRP −0.116 — largest negative VRP, single agent).
- **High-IV non-earnings:** ZS (IVR 99.8, confluence 0 — earnings 5/26, handed to earnings half-size sell-vol but RM gated to watch).
- **Earnings-scout single-source:** OKTA (sell-vol 5/27 wait), HEI (sell-vol 5/27 full per scout, RM half), KEYS (5/19 sell-vol half), ADI (5/20 calendar only — back-skew flat disqualifier), ZM (5/21 calendar single-agent).
- **LEAP near-miss watch:** AAPL (await COVERED_CALL → DIRECTIONAL_LONG flip), NVDA (await 90d CPF inflection), TLT (await LEAP put unwind).

---

**Watchlist write-back confirmation:** `conviction_2026-05-18 = [MU, TSM, TTWO, MA, PLTR]` written successfully via `mcp__uw-pp__watchlist_manage`. Tomorrow's run will pull adverse-flow alerts against these names to flag exit candidates.

**Agent fleet status:** 10 Phase 1 agents spawned in parallel + 2 Phase 2 sequential. `opex-pin-strategist` skipped (post-OPEX Monday, pin mechanics dissolved). All agents returned. No timeouts. Contrarian-scanner and leap-positioning-radar returned empty buckets — both valid "no-trade" outcomes given TRANSITIONAL regime + FAIR VRP + narrow breadth.
