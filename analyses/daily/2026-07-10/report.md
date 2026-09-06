# Daily Market Analysis — 2026-07-10

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / UPTREND (SPY 754.95, above 20/50 SMA, +2.43% 30d, −0.72% from 90d high). SPY next-session gamma **long/pinned at a dominant 755 wall**; QQQ **short-gamma** below its ZGL (breakout-prone). VIX ~15. Breadth split: price breadth strong (67.2% green) but options **flow breadth bearish** (33.4% bullish tickers). Sector premium leans to Tech/Comm-Services but persistence is nil.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half` (P0.6 guard active; 0/30 post-2026-06-12 calls resolved).
- **Next-session GEX (SPY/QQQ):** SPY — POSITIVE/long-gamma, ZGL 754.15, **single-strike 755 pin** (call wall 755, put wall 740) → iron fly/short straddle @755, size small; fresh/unstable flip. QQQ — NEGATIVE/short-gamma (ZGL unreliable), call wall 730, put wall 705 → debit verticals / long straddle around 725–730; premium-selling disfavored. Advisory, see §2.
- **Top swing build:** **None sized.** Highest raw score NVDA (4, LOW) is single-agent watch-only, cut by the event-risk (CPI T+2) and debate (bear 0.75 ≥ bull 0.55) gates.
- **Top LEAP candidate:** **None.** Empty LEAP board — no name cleared the 6-of-9 gate.
- **Biggest risk:** CPI (June) prints **Tue 2026-07-14 — 2 trading sessions out** — into a short-gamma QQQ tape and bearish flow breadth. Semi/tech cluster (SNDK/AMD corr 0.751) is the only correlation flag; the whole board is watch-only, so book delta = 0, no hedge required.

> **No-edge day.** 7th consecutive effectively-empty conviction book: **zero sized positions.** One name (AMD) cleared the ≥2-agent confluence gate and still scored −1 on the mechanical flow_conflict. Two LOW names (NVDA, EWZ) written to the watchlist for continuity; nothing else sized. This is the frozen rubric behaving as calibrated in a TRANSITIONAL, bearish-flow-breadth tape into a macro print — not a pipeline failure.

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL (mixed — half size, defined-risk, iron condors in range); trend UPTREND. Market breadth (flow): 2,094 bullish / 4,167 bearish tickers = **33.4% bullish**. SPY 754.95 (SMA20 743.81, SMA50 741.24).
- **Per-index gamma (EOD current-state / next-session prior — see §2):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 754.93 | 754.15 (reliable) | +$3.18B | POSITIVE / long-gamma | 755 (+$2.03B, dominant pin) | 740 |
| QQQ | 725.62 | n/a (artifact) | +$0.083B | NEGATIVE / short-gamma | 730 | 705 |
| IWM | ~296 | whipsaw/artifact | −$1.92B | flat/neg (noisy) | — | — |

- **`uw options-flow dte-volume-share`:** 0DTE 49.7% / weeklies 26.6% / monthlies 14.0% / LEAPs 3.7% → **RETAIL_DRIVEN** tape (one tick from the 50% hard-downgrade line). Swing/LEAP conviction gets no institutional benefit of the doubt.
- **`uw historical vrp`:** SPY **FAIR** (IV30 12.6% vs RV 15.4%, vrp −0.028); QQQ **PREMIUM_BUYING** (IV30 22.5% vs RV 29.7%, vrp −0.073 — vol cheap vs realized, favor premium buying on Nasdaq names).
- **Macro backdrop (`scripts/fred_macro.py`):** yield curve normal (+0.35 10y–2y); core CPI 2.96% / core PCE 3.41% YoY (sticky); unemployment 4.2%, payrolls +57k (soft); 10Y 4.54% flat; USD strengthening; fed funds 3.62%. **Forward event risk:** CPI (June) **Tue 07-14 (HIGH, T+2)**, PPI 07-15 (T+3), Retail Sales + Claims 07-16, Monthly OPEX 07-17, FOMC+SEP 07-29 (HIGH).

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> Advisory, prose-only, **0 rubric points**, no backtested predictive claim. EOD dealer-gamma book read forward as the prior for the next session's open. Scope SPY/QQQ only.

**SPY — long-gamma, single-strike 755 pin.** Spot (754.93) sits essentially on ZGL (754.15), but the book is dominated by one enormous 755 wall (+$2.03B, ~64% of total GEX). Dealers sell rallies / buy dips tightly around 754–756 into the open → mean-revert / pin behavior. A decisive gap through 755 turns the wall into a re-hedge accelerant (thin below 748; 740 is the next real support ~2% down). **Structure bias:** iron fly / short straddle @755 or a 750/755/760 call fly — **size small**, a one-strike wall flips local flow fast on a 0DTE break. Regime is a **fresh, unstable** flip (SPY whipsawed POSITIVE/NEGATIVE/FULLY_NEGATIVE nearly every session last week).

**QQQ — short-gamma.** Spot (725.62) well below the reported ZGL (752.1) with thin total_gex → dealers amplify moves (sell drops, buy rallies). Combined with QQQ PREMIUM_BUYING VRP this favors trend/breakout over a pin. Nearby +$130M cluster at 725 is the soft cushion; below it air is thin to the 705 put wall. **Structure bias:** debit verticals / directional 0DTE in the early trend, or a long straddle around 725–730. Avoid premium-selling.

**Mandatory caveats:** EOD prior only (redrawn by fresh 0DTE OI in the first 30–60 min); **QQQ ZGL is unreliable** (recurring GEX-grid artifact — do not quote it); **CPI 07-14 gap risk** builds across the long weekend and is *amplified* in QQQ's short-gamma regime; SPY/QQQ ETF books, not SPX/NDX; `gex --dte-max 1` not isolable (0–45d proxy). ZGL data-quality artifact (sub-320 QQQ/IWM ZGL prints) flagged for the next `/calibration-audit`.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — validated stack)
Both indices: **GO_PREMIUM_SELL_INTRADAY**, but VIX ~15 (LOW vol state) = **thin edge, half size** (SPY size_scalar 0.5, QQQ 0.5). Advisory, delta-neutral, **0 rubric points** — NOT a guaranteed edge (short-vol left tail UNSAMPLED). Lead with **net**:

| Index | sell_premium | VIX | implied move | exp. range | mean PnL open (GROSS / NET) | open win-rate | structure |
|---|---|---|---|---|---|---|---|
| SPY | true | 15.0 LOW | 0.39% | 0.79% | +0.286% / **+0.186%** | 95.0% | iron fly @754.97, wings ±0.79% |
| QQQ | true | 15.0 LOW | 0.80% | 1.34% | +0.386% / **+0.286%** | 88.3% | iron fly @725.81, wings ±1.34% |

PnL basis = % of underlying spot notional, GROSS; net = minus assumed 0.1% round-trip. **Enter at/after the open once the gap resolves; hold to close; never carry overnight.** SPY ≈ SPX (trade either); QQQ weaker (NDX book unavailable) — lower confidence. **Tension to respect:** the EOD GEX book reads QQQ **short-gamma**, which argues *against* a short-vol 0DTE structure — if QQQ opens trending, defer to the short-gamma read and stand aside. Monday's open also carries a weekend gap + building CPI risk.

## 2b. Swing Dealer Positioning (1–4 weeks)
- **No index-level mechanized DEX flip; no confirmed vanna squeeze.** SPY DEX +$42.5B POSITIVE but prior 3 sessions not sign-uniform (no flip); QQQ +$13.8B choppy; both vanna SHORT-leaning (call-heavy, falling-IV = selling pressure, not a squeeze).
- **IWM is one session from a vanna-squeeze** — put-heavy book already in place, VIX fell 07-08→07-10 (16.90→15.03) but only 2 consecutive down-closes (needs a 3rd), and its front-end IV ratio (1.354) is still panicked-not-falling. Watch-only; one more down-VIX close + a front-end rollover triggers a live LONG.
- **LRCX** is the only genuine mechanized DEX flip found (net_dex −$0.36B→+$0.23B, prior 3 sessions negative, 0.46× trailing median, persisted 2 sessions) — but **disqualified**: DEX (now bullish) and vanna (bearish/selling) disagree, and front-end IV 2.89 is already past the 1.10 invalidation threshold. It also directly conflicts its own Tier-1 bearish opening put — logged as a cross-signal curiosity, not a call.

## 2c. Sector Rotation
- **`rotation_regime: no_change` (low confidence).** GICS persistence is non-discriminating — all sectors tied at persistence_score 1.0, so nothing clears the market-relative bar. Best-confirmed single leg is **Healthcare outflow** (GICS + XBI ETF + put-tilted urgency all agree) but there is no clean opposing leg.
- Every 30-day cum-flow check contradicted the same-day screener direction: **TSLA** 30d −$271.6M (vs +$39.7M today's tick), **SOFI** flat −$0.7M, **LLY** +$50.0M (contradicts a Healthcare short). Single-day tape is noise vs the month-long trend. **No single-name leader passes the conditional +1 gate.**

**ETF flow tape (advisory)** — top movers, but the DP/options-urgency layer contradicts the headline cum-flow direction on nearly every deep-pulled name:

| ETF | Net prem (5d) | Trend | DP positioning | Options urgency | GICS agreement |
|---|---|---|---|---|---|
| XLF | +$21.1M | BULLISH | blocks near mid | balanced (roll/spread) | weak agree |
| EWY | +$19.3M | BULLISH | largest print sold below mid (redemption tell) | LEAP protective puts dominate | n/a |
| XLY | +$0.65M | BULLISH | sold below mid | puts dominate sweep tape | agree, urgency diverges |
| XBI | −$10.4M | BEARISH | mixed | slight put edge | agree (Healthcare outflow) |
| GDX | −$5.7M | BEARISH | thin/noisy | puts > calls | disagree (gold-miner idiosyncratic) |

SMH (+$49.7M, largest $ move) is labeled **MIXED** — high notional, non-persistent chop, consistent with the heavily-bearish tech/semi single-leg tape.

## 3. Swing Setups (1–6 weeks)
**None sized.** No name cleared to HIGH/MEDIUM; every candidate is DROP or LOW watch-only. The board's directional candidates and why they don't size:

### 3a. Long swings (regime-aligned) — all watch-only
| Ticker | Score | Tier | Thesis (why it didn't size) | Invalidation |
|---|---|---|---|---|
| **NVDA** | 4 | LOW | Jul17 210/215 bull call spread (+2) + 5/5 call-led OI build (+1) + $157M 30d flow (+1). **Single-agent**; 90d flow −$161M (recent pop, not structural); event-risk (CPI T+2) + debate (bear 0.75) cut it. | 30d flow rolls negative / loses the 210 short-strike |
| **EWZ** | 3 | LOW | Dec18 Brazil bullish combo (+2) + OI build (+1). Single-agent; USD strengthening headwind; no Brazil catalyst; CPI T+2 cut. | DXY breakout / EWZ < 33 (put legs ITM) |
| **SNDK** | 2 | DROP | Loudest tape on the board ($2.16B, 5/5 opening-confirmed sweep, +$1.04B 30d) + strongest fundamentals (CONFIRM) — but the sweep line earns **0 points** and no 2nd agent co-flagged. Parabolic (+4678% off low, beta 4.91); debate bear 0.85 (widest on board). | cum_flow flips negative / memory catalyst rolls |
| **SOFI** | 2 | DROP | Jul31 20/23 earnings-event spread (+2) + OI build (+1) − flow_conflict_lite (flat −$0.7M flow). Spread rides un-hedgeably through the 07-29 print; unprofitable off a recent miss (CAUTION −1). 14.9% short-float squeeze fuel noted. | flat/neg flow persists / 2nd earnings miss |
| **SMCI** | 2 | DROP | Jul17 29.5/31.5 spread (+2, expires before Aug5 print) + OI build (+1) − flow_conflict_lite (−$38.7M against). News stack (dilution/legal overhang) contradicts the flow (CAUTION −1). | flow deepens negative / legal-dilution escalation |
| **AMD** | −1 | DROP | **Only name to clear the ≥2-agent confluence gate** (sweep 5/5 + accumulation mega-block 0.898). Killed by the mechanical −3 flow_conflict (30d −$96.3M against the long, 2.5× median) + ⚠ distribution_flag (133DTE $800C OI −425, $10.4M closed). | 30d flow flips positive / mega buy_ratio < 0.5 / < $548.50 DP shelf |

⚠ **Distribution caution (AMD):** bullish-side 133DTE $800 call OI −425 on 2,639 vol ($10.4M) closed — accumulation-as-distribution contradiction on the strongest mega-block name (advisory, 0 points).

### 3b. Short / fade swings — none
**contrarian-scanner returned zero fade candidates.** Every name (XLY z+2.56, Q z+6.6, SOXX, MSFT, MRNA, FTNT…) disqualified — either ALIGNED bearish (continuation, not divergence — textbook Pan-Poteshman) or BACKWARDATION into the Jul-14 CPI catalyst (event-driven, don't fade). No index-level fear extreme (SPY z −1.16, QQQ z +0.62, both NORMAL).

**Sweep ledger (informational, 0 points):** first-class bullish persistence — **SNDK** (5/5, $2.16B), **AMD** (5/5, but 30d flow flat), **NBIS** (3/5, put-side OI ambiguity). Mega-caps (SPY/QQQ/TSLA/AAPL/MSFT bearish sweeps) demoted to hedge-flow (cum-flow doesn't confirm). Single-leg Tier-1 whale scan is **heavily bearish tech/semi**: MSFT floor-put block ($5.99M), INTC/LRCX/LITE/FTNT opening-put primes (WR 0.61–0.64, advisory C19, 0 points).

## 4. LEAP Builds (6–24 months)
**Empty board.** No name clears the 6-of-9 gate (LEAP DTE share only 3.7% of tape). Screened & disqualified: **QXO** (single-day spike, 90d flow BEARISH, conviction 30%), **ACI** (conviction DISTRIBUTION, DP sell/buy 0.39; merger-arb blind-spot flag), **TLT** (conviction COVERED_CALL, 90d BEARISH), **VALE** (COVERED_CALL, stale print). Step-0 mega-caps (NVDA/META/TSLA/AMD/SNDK/IBIT) show only chain-wide 0DTE/weekly churn, not isolated long-dated builds; 90d cum-flow MIXED on all except IBIT (whose LEAP OI adds are trivially sized).

## 5. Volatility Surface
- **SELL VOL (VRP-aligned kinks):** **FTNT** (KINKED @Jul31 earnings Jul29, VRP **+0.301 strong**, front-end 0.648 CONTANGO) — strongest vol edge on the board, but note a **Tier-1 opening put whale on the same name** = directional tail risk to a short-straddle. **AKAM** (KINKED @Aug7, VRP +0.263, size down — thin 160-contract basis). **MRNA** (KINKED @Jul31, VRP +0.088 mild, worst mover −10.83% today; carries the 07-01 VETO precedent).
- **Bank earnings SELL VOL (earnings-scout):** full-size (kink + confirmed TAIL_HEDGING back-month) **ABT** (7/16), **WFC** (7/14), **MS** (7/15), **CTAS** (7/15); half-size **JNJ, GS, NFLX, ASML, AEHR, TXN, STM**. SKIP: TSM (negative back-skew), CLF, GE, BLK.
- **META / MSFT:** KINKED @Jul31 but VRP **FAIR** (no edge) → calendar-only, not a directional condor.
- **SOXX:** TAIL_HEDGING put-rich (skew 1.263), PREMIUM_BUYING (buy-vol), front-end 1.047 FLAT — genuine protective/tail-hedge flow, not a fade.
- *Substrate hygiene:* raw `iv-term-structure` labeled everything BACKWARDATION off 0DTE contamination; after dropping the 0DTE bucket, 5 of 6 flip to CONTANGO with an earnings-adjacent kink. All IV percentiles PROVISIONAL (n=62 < 120-day floor). `front-end-iv-ratio` default snaps to 0DTE on Friday EOD (false >1.10 panic) — flagged for the audit.

## 6. Risk & Correlation
- **Macro headline:** sticky core inflation (CPI 2.96% / PCE 3.41%), soft labor (+57k payrolls, 4.2% unemployment), 10Y flat 4.54%, USD strengthening. **Event risk: CPI Tue 07-14 (T+2)** hits every swing horizon on the board; PPI 07-15, Retail Sales 07-16, OPEX 07-17, FOMC 07-29.
- **Correlation:** **CLUSTER `SNDK_AMD_semi_pair` (corr 0.751 ≥ 0.70)** — keep SNDK (higher raw), AMD auto −1 tier (academic — both already DROP). Soft watch NVDA/NBIS 0.670 (no penalty). Sector metadata returned 100% "Unknown" (concentration read unusable; coefficients intact).
- **Fundamentals verdicts (top-5):** NVDA **CONFIRM**, EWZ **NA** (ETF; USD headwind), SNDK **CONFIRM** (strongest on board; valuation/crowding risk), SOFI **CAUTION −1** (rides through 07-29 print, unprofitable, recent miss), SMCI **CAUTION −1** (mixed earnings, dilution/legal overhang, flow leans bearish). **No VETO.**
- **Debate:** bear residual ≥ bull on all four debated names (NVDA 0.55/0.75, SNDK 0.65/0.85, SOFI 0.55/0.85, SMCI 0.55/0.85) — the debate gate cut each; EWZ not debated (ETF).
- **Panic gate:** no-op — SPY front-end headline 1.183 was a 0DTE-EOD-Friday artifact; robust 5/28-DTE read 0.714 CONTANGO. No front-end panic.
- **Breadth cross-check (advisory):** fz 338 adv / 163 dec, **67.2% green** — no pct_green<50 distribution tell. But it diverges from the options **flow** breadth (33.4% bullish): price broadly green while options premium leans net bearish — a flow/price split worth watching, not a same-lineage divergence.
- **Adverse-flow exits (`conviction_2026-07-09`):** **NBIS = EXIT CANDIDATE** — scan shows bearish net flow (−$6.03M), HIGH_IV_RANK 94.4 (options top-decile expensive), OI +34,616; today's board independently demoted NBIS to raw-2 DROP. fz quote-drift shows no fundamentals change — flow-driven only.
- **Hedge sleeve:** **None required** — zero sized positions, book net delta = 0. If the desk carries discretionary residual long tech into CPI, the tape-consistent hedge is a defined-risk QQQ put vertical expiring 07-17 (CPI/PPI/Retail Sales all inside), sized to that external delta.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**Empty.** No HIGH or MEDIUM names today — the 7th consecutive effectively-empty conviction board. The full audited score list (top-of-book NVDA 4, EWZ 3, then a cluster at 2, AMD −1) is carried in `decision.json` with per-call `score_components`, `gate_verdicts` (all 9 keys), fundamentals verdicts, and debate residuals. Every `win_rate` is `NA(substrate)` — the `dark_pool_accumulation` backtest class is empty (total_signals=0) and `multileg_directional`/`multi_day_sweep`/`earnings_vol` have no `--signal-type` mapping; `market_excess` null everywhere. No numeric win-rate quote exists anywhere in this book.

**Expectancy lens** *(advisory — expectancy is not yet a live sizing axis)*: no per-tier expectancy computed today — zero sized calls, and the most recent audit (2026-07-04) recorded sized-book realized 36.1% vs paper 45.2%. Refusing to size into a TRANSITIONAL, bearish-flow-breadth tape with CPI two sessions out is the system behaving as graded.

**Conviction rubric (frozen `2026-06-12`):** score = Σ [ +1 mechanized DEX flip / vanna-squeeze · +3 accumulation conjunction (halved to +1 if 30d cum-flow non-confirming) · +1 multi-day OI build · +1 conviction-matrix DIRECTIONAL_LONG (LEAP only) · +1 intent-screened 30d cum-flow accretion · +1 sector-leader (conditional) · +1 earnings BUY/SELL VOL · +2 multileg directional · +1 vol-surface KINKED/BACKWARDATION VRP-aligned · +1 OPEX pin (OPEX wk) · −2 crowded-long P/C · −3 flow_conflict / −1 flow_conflict_lite (mutually exclusive) ]. Tiers: ≥9 HIGH (full), 7–8 MEDIUM (half), 3–6 LOW (starter/watch), ≤2 drop. Sizing capped at half while OUT-OF-REGIME (P0.6). Removed lines earn 0: sweep-persistence, `signal-confluence` ≥4, gamma-flip 0DTE breakout. Tier gates (0 points, applied by risk-monitor): −1 tier correlation cluster, −1 tier regime conflict.

## 8. Watch-only — single signal, no confluence
Only **AMD** cleared the ≥2-agent confluence gate (and still scored −1). Every other name below is single-agent by construction — journaling only, **not for trade entry today**:
- **Long/flow:** SNDK (sweep, board's strongest tape — dropped by design, sweep line = 0 pts), NVDA & EWZ & SOFI & SMCI & NVDA-adjacent (multileg, LOW/DROP above), META (accumulation mega 0.63 + net-prem $133M, but 90d flow −$368M and distribution_flag; raw 1), KR (thin accumulation 3.16, raw 1), NBIS (sweep 3/5, put-side ambiguity — also flagged as an adverse-flow EXIT on yesterday's group).
- **Vol/short:** FTNT / AKAM / MRNA (vol-surface SELL VOL, raw 1); bank-earnings SELL-VOL cluster ABT/WFC/MS/CTAS/JNJ/GS/NFLX/ASML/AEHR/TXN/STM (earnings-scout, raw 1); SOXX (tail-hedge, raw 0); VIX bear-put-spread (multileg, raw 2 DROP); IREN (side-ambiguous LEAP strangle, raw 0).
- **Bearish single-leg (advisory C19, 0 pts):** MSFT/INTC/LRCX/LITE/FTNT Tier-1 opening/floor puts — the most coherent directional read on the tape, but structurally advisory pending C19 graduation.

---
*Fleet: 10 Phase-1 alpha-finders (non-OPEX) → signal-confluence-quant → fundamentals-gate → bull/bear debate (top-5) → risk-monitor. Rubric frozen 2026-06-12. Watchlist write-back: NVDA, EWZ → `conviction_2026-07-10`. Envelope: `decision.json` (schema 1.3, validated).*
