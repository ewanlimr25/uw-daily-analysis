# Daily Market Analysis — 2026-07-20

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / CHOPPY — SPY 742.09 below both SMAs (20d 744.79, 50d 744.55), −2.41% from 90d high, breadth 34.1% bullish (4135 bearish vs 2140 bullish flow tickers); VIX 18.65 (HIGH); **SPY & QQQ both FULLY_NEGATIVE (short-gamma)**; smart-money rotating defensive (Utilities/Energy/Cons Defensive in, Tech −$134M out). Tech tape is bifurcated (MRVL/LRCX/AVGO call-heavy vs a deep semis bear list).
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL/CHOPPY) — sizing capped at half`. Moot this run — nothing sizes above skip.
- **Next-session GEX (SPY/QQQ):** SPY short-gamma · ZGL n/a (FULLY_NEGATIVE) · call wall 760 / put wall 742 (at spot) · **breakout-friendly, no credible upside ceiling**. QQQ short-gamma · ZGL n/a · call wall 720 / put wall 690 · **breakout-friendly, 3 sessions entrenched negative** — advisory, see §2.
- **Top swing build:** **NONE.** 13th consecutive empty conviction board — top raw score = 2 (INTC), zero names reach LOW tier. No swing setup clears the bar.
- **Top LEAP candidate:** **NONE.** LEAP tape is 2.3% of volume and index/ETF-hedge dominated; zero names cleared the 6-of-9 gate (closest: Dominion, killed by conviction-matrix DIRECTIONAL_SHORT + MIXED 90d flow).
- **Biggest risk:** The entire candidate board is functionally **one semis/memory position** — {INTC, TSM, MRVL, SNDK, AVGO, ARM} pairwise 0.75–0.89. Sizing any two of these doubles one macro-semis bet regardless of the sign on the label. No hedge sleeve required (empty book).

**Bottom line:** A no-edge day, and the gates agree with the quant. The only structure worth watching is **INTC earnings-vol into 07-23** (fundamentals CONFIRM, panic-clear, cluster-kept) but at raw 2 it doesn't clear the tier. DROP-pile discipline (43.3% > traded book, per the 07-18 audit) says refusing to size the semis complex is the best-graded behavior.

---

## 1. Regime & Gamma State
`uw risk market-regime`: **TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity"; trend CHOPPY.** SPY 742.09, below 20-SMA (744.79) and 50-SMA (744.55), +0.15% 30d, −2.41% from the 90d high. Market breadth 34.1% bullish (2140 bullish / 4135 bearish flow tickers of 6275). Trading guidance: half position sizes, defined-risk, iron condors in range. Smart-money sector rotation: **IN** Utilities (+$9.5M) / Energy (+$5.8M) / Cons Defensive (+$2.5M); **OUT** Technology (−$134M) / Industrials (−$36M) / Cons Cyclical (−$43M) — a defensive tilt.

**Breadth cross-check (`fz`, advisory):** 164 advancers / 338 decliners, **pct_green 32.6%**, avg −0.48% / median −0.55%; top GPN +5.85%, worst CVNA −4.75%. **No divergence** — the tape is genuinely red AND breadth is weak, so the `fz` A/D lineage confirms the `uw` regime label rather than contradicting it.

### Per-index gamma table (current-state EOD book)
| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 742.33 | null (unresolvable) | −$1.94B | FULLY_NEGATIVE | 760 (thin) | 742 (at spot) |
| QQQ | 696.80 | null (unresolvable) | −$0.70B | FULLY_NEGATIVE | 720 (negligible) | 690 |
| IWM | ~293–297 | null (grid artifact) | negative all-window | short-gamma | — | — (DEX −$7.58B, worst of window) |

**DTE-volume share (MARKET):** 0DTE **40.5%**, weeklies 24.9%, monthlies 20.8%, LEAPs **2.3%** → **RETAIL_DRIVEN** tape → directional conviction downgraded uniformly.

**VRP:** SPY **FAIR** (IV30 15.2% ≈ RV 15.7%, vrp −0.005); QQQ **PREMIUM_BUYING** (IV30 25.7% < RV 30.7%, vrp −0.050 — vol cheap vs realized, favor premium buying / long-vol on QQQ-beta names).

**Macro backdrop (`fred_macro`):** yield curve **normal** (+0.39 10y2y), core CPI 2.81% / **core PCE 3.41% (sticky)**, unemployment 4.2%, payrolls +57k (soft), 10Y **4.55% RISING**, USD **STRENGTHENING**, fed funds 3.63% — tightening financial-conditions drift under a choppy tape, a mild headwind for risk/tech. **Forward event_risk:** INTC earnings 07-23 (T+3) · **FOMC decision 07-29 (T+7, no SEP)** · Q2 GDP advance ~07-30 · **Core PCE (June) ~07-31 (T+9, Tier-1)** · weekly jobless claims 07-23 & 07-30 · July NFP ~08-07. FOMC at T+7 sits inside any swing horizon → event-risk gate live on all multi-week structures held through the print.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book (OI persists overnight) read forward as the prior for the next open. Prose-only, **0 rubric points**, no backtested predictive claim. Scope SPY/QQQ only.

Both indices printed **FULLY_NEGATIVE** with the zero-gamma level unresolvable — this is the disqualifier case the reliability rule anticipates (ZGL disregarded; read falls back to `total_gex` sign + per-strike walls).

| Index | Regime | ZGL | Call wall | Put wall | Next-session 0DTE structure bias |
|---|---|---|---|---|---|
| **SPY** | short-gamma (total_gex −$1.94B), **fresh/unstable** (FULLY_NEGATIVE 2 of last 3 sessions after whipsawing) | null, `zgl_reliable=false` | 760 (+57M, thin, +2.4%) | 742 (−343M, **at spot**); secondary 740 (−333M) | Trend/breakout-friendly. Heaviest negative gamma sits **right at/just below spot (740–742)** — dealers short gamma there will *amplify* a break, not pin. Favor long premium (debit verticals / directional 0DTE); if selling premium (per §2a), keep strikes outside the 735–745 cluster. |
| **QQQ** | short-gamma (total_gex −$0.70B), **entrenched** (FULLY_NEGATIVE 3 straight sessions) | null, `zgl_reliable=false` | 720 (+6M, negligible, +3.3%) | 690 (−122M, −1.0%); secondary 695 (−105M, at spot) | Breakout-friendly, **no real upside ceiling** — a move higher meets little dealer resistance; a break into 690–695 gets amplified. Front-end 0DTE IV at 1.47× VIX (backwardation) already prices some of this instability. |

**Mandatory caveats:** (1) EOD is a *prior, not a target* — fresh 0DTE OI in the first 30–60 min re-computes the map. (2) ZGL unreliable on both (FULLY_NEGATIVE) — used `total_gex` sign + wall position. (3) **Gap risk voids the prior** — FOMC 07-29 / PCE 07-31 sit ahead in the week (not tomorrow, but on the radar). (4) uw-pp cannot isolate the D+1 expiry (`--dte-max 1` errors) — this is the 0–45d proxy. (5) ETF book, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup (`zerodte_setup` — the validated stack)
Delta-neutral premium-selling edge (the wall-as-pin idea backtested NO_GO). Advisory, **0 rubric points**, NOT a guaranteed edge — validation sample has no vol shock (short-vol left tail UNSAMPLED). Both indices: **GO_PREMIUM_SELL_INTRADAY** (VIX 18.65 = HIGH vol_state → richest tercile of the backtest, mean PnL +0.38% HIGH-VIX).

| Index | sell_premium | vol_state | Implied move | Exp range (wings) | Size scalar | Mean PnL/day (net · gross) | Win% (gross) | Structure / caution |
|---|---|---|---|---|---|---|---|---|
| **SPY** (≈SPX) | ✔ | HIGH | 0.98% | ±1.21% | 1.5 | **+0.162%** · +0.262% | 93.3% | Wider iron condor, wings ≈ ±1.21%; short-gamma → keep wings outside 735–745. |
| **QQQ** (weaker) | ✔ | HIGH | 1.73% | ±1.95% | 0.75 | **+0.274%** · +0.374% | 88.3% | Wider iron condor, wings ≈ ±1.95%; **CAUTION: front-end backwardation (0DTE IV 1.47× VIX) → event/gap risk, half size.** |

**Basis (P1.8):** `mean_pnl_open_pct` is % of underlying spot notional, **GROSS**; lead with the **net** (minus 0.1% assumed round-trip cost). Entry: **at/after the open once the gap resolves; hold to the close; never carry overnight** (overnight backtested negative). Delta-neutral — no directional tilt. Lane stays advisory permanently until a vol-shock day enters the sample AND net expectancy clears a tail-aware bar (win-rate is NOT the promotion metric).

## 2a. Swing Dealer Positioning (1–4 weeks)
`dealer-positioning-strategist` (VIX dated ^VIX: 07-14 16.50 → 07-20 18.65, **rising** — invalidates every vanna-squeeze candidate; all six checked books are put-heavy/long-vanna but VIX rising = vanna *pressure*, not squeeze):

- **Three mechanized bearish DEX flips (scored line, +1 each in trade direction):**
  - **TSM — cleanest short.** net_dex 7/10 +$0.73B → 7/13 −$0.25B (prior 3 sessions uniformly positive), |flip| 0.31× trailing-10 median, **held negative 6 consecutive sessions** (7/13→7/20). Per-strike GEX confirmed distributed (not a single-strike artifact). Aligns with the Step-0 bearish semis confluence.
  - **AVGO — SHORT-leaning, fading.** Flip verified but magnitude decayed 88% by 7/20; contradicts its call-heavy retail tag → caution flag, not a standalone short.
  - **MRVL — SHORT-leaning, low-confidence.** Flip verified but per-strike artifact-check unavailable; sweep tape is *bullish* 1/5 (conflict). Treat as caution against chasing the call-heavy tape.
- **SPY/QQQ/IWM:** DEX deteriorating (SPY −$37.3B, QQQ −$30.9B, IWM −$7.58B and never positive in the window) + confirmed negative-GEX regime flip ~07-16, but **no certified DEX flip** (wh, whipsaw-broken prior-3 runs) → descriptive context, unscored. QQQ front-end-iv 1.135 (BACKWARDATION, front panicked); IWM 1.076 (backwardation). No vanna squeeze fires anywhere (VIX rising).

## 2b. Sector Rotation
`sector-rotation-strategist`: **regime call `no_change`, LOW confidence.** The four sectors clearing the market-relative bar span growth, cyclical, value *and* defensive simultaneously (Comm Services $618M, Cons Cyclical $311M, Financials $236M, Healthcare $101M all INFLOW at persistence 1.0) — that is broad-tape breadth, not a rotation axis. Only **Industrials** is cleanly OUT (persistence 0.8). Step-0's smart-money "IN Utilities/Energy" tag is discounted (magnitudes $2.5–9.5M sit far below the $66.3M cross-sector median). **Technology** is net-positive today (+$1.42B raw) but persistence degraded 1.0→0.8 on a −$3.36B reversal (07-16) → unstable, watch-only, not a call either way.

Only **LULU** clears the full sector-rotation-tag gate (Cons Cyclical leader, persistence 1.0 ≥ 0.6, cum_flow_30d +$179.4M LONG-aligned ≥ $50M). Mega-cap financials (JPM/GS/BRKB/AXP/V/MS) show inflow against a persistent **KRE** regional-bank outflow (bifurcation, not sector-wide).

**ETF flow tape (advisory — 0 rubric points):**
| ETF | 5d net | Dir | DP positioning | Options urgency | GICS agreement | Leaders |
|---|---|---|---|---|---|---|
| EWY | +$25.6M | BULLISH | creation/redemption noise | mixed (2027 LEAP call vs Jul31 145P) | n/a | — |
| XLY→Cons Cyc | +$9.9M | BULLISH | near-mid | **distributed put-SELLING** (bullish floor) | **AGREE** | LULU/BABA/ONON/NKE |
| SMH→Tech | −$68.4M | MIXED | buy-aggression late | **heavy OTM put-SELLING** (Jul31 520P) — conflicts outflow | **DISAGREE** — not a confirmed short | MRVL/MSFT/LRCX/AVGO |
| KRE→Financials | −$10.0M | BEARISH | stale-NBBO artifact top print (discount) | mild put-buy | **DISAGREE** (regional-bank drain vs mega-cap in) | — |

---

## 3. Swing Setups (1–6 weeks)
**No scored swing setups today.** Zero names reached LOW tier (raw ≥3); the confluence board is empty. Below are the sub-threshold **watch** candidates (raw ≤2, all `final_size=skip` — journaling only, NOT trade entry):

### 3a. Long swings (watch-only)
| Ticker | Raw | Thesis | Why it fails | Invalidation |
|---|---|---|---|---|
| LULU | 1 | Cons Cyclical rotation leader, cum_flow +$179M, insider BUYING (+78 MSPR) | Single-agent (sector-rotation only); fresh sell-side downgrade stack (Truist cut-to-sell, ~20% downside) fights the long → fundamentals CAUTION | Cons Cyclical persistence <0.6 for 2 sessions |
| SHOP | 1 | multileg bullish call roll-up (Sep100C→Oct135C) | Single-agent; repeat_count=1 (single-day roll = exposure maintenance, not fresh conviction); flow_conflict_lite (cum_flow +$6.8M near-zero) | Prints as net-credit close (pure exit) next session |
| SPCX | −2 | 4/5 bullish sweep persistence, OI building | flow_conflict −3 (cum_flow_30d −$326M BEARISH); $1.59T index-weight caution; win_rate 0.431 sub-floor | — |

### 3b. Short / fade swings (watch-only)
| Ticker | Raw | Thesis | Why it fails | Invalidation |
|---|---|---|---|---|
| TSM | 1 | Mechanized bearish DEX flip (6-session hold); "beat-but-stock-fell" sell-the-news | Lone scored flag; fundamentals CAUTION (beat streak 4/4 + rev +31% fight the short); Tech sector INFLOW is adverse; cluster −1 | DEX reverses positive ≥3 sessions |
| AVGO | 1 | Bearish DEX flip + insider selling accelerating (−100 MSPR) | Flip fading (88% decay); strong growth (+126% EPS) fights it; call-heavy tape argues opposite; cluster −1 | DEX flips back positive ≥3 sessions |
| SNDK | −1 | 5/5 bearish put persistence ($2.33B 5d), insider MSPR −100 ×3mo (real distribution) | **flow_conflict −3** — $2.33B put premium but cum_flow_30d **+$589M BULLISH**; internally contradictory (07-15 wash-print precedent); cluster −1 | — |

**Persistence-first sweeps (informational, 0 points):** SNDK PUT 5/5 (opening-confirmed, $2.33B) · SPCX CALL 4/5 ($750M) · GOOGL PUT 3/5 (demoted, cum_flow MIXED). Index/mega hedge-flow (SPY/QQQ/NVDA/META/AMZN 5/5) filtered out — all cum_flow_30d MIXED/opposite. **SPX top-premium-trades is box-spread financing** (strike 7000/8000 across expiries) — no directional signal.

**OUST (advisory, C19, 0 pts):** the only validated-edge signature on the board — Tier-1 `OPENING_PUT_PRIME` (put, size/OI 41, DTE 4, $551K, bearish). Coherent short (crowding z=3.24 + informed flow + backwardation all agree) but **no dark-pool corroboration** (accumulation-hunter: OUST shows zero mega/block DP tier) — stands alone on the single-leg tape. C19 stays advisory pending the ≥58% / ≥60-day / ≥2-regime gate (unmet; the 07-18 audit blocked graduation).

## 4. LEAP Builds (6–24 months)
**Empty lane.** LEAP share of tape is 2.3% (thin); `oi biggest-increases --min-dte 180` returned only 20 rows, almost all index/leveraged-ETF hedges (IWM/TLT/SOXL/XLU/QQQ puts) or bearish single-name puts (NKE/NFLX/CMCSA/KO). Every Step-0 bull-confluence name (MRVL/AVGO/GOOG/MSFT/LRCX/SMH/CRWV/STX) failed Gate 1 (no persistent single-strike laddering). Closest near-miss: **Dominion (D)** — genuine Jan-2028 call laddering (2/9 gates), but **HARD FAIL** on conviction-matrix (DIRECTIONAL_SHORT, 38.3%) + 90d cum-flow MIXED. A real reject on the two hardest-to-fake gates, not a borderline call.

## 5. Volatility Surface
`vol-surface-scout` — VRP splits the "extreme IV" complex into rich vs cheap (raw IV rank 100 on all, but sign diverges):

- **SELL VOL (KINKED, earnings-aligned):** **INTC** (07-24 kink 168%, VRP +0.058, implied 11.6%, earnings 07-23) · **NOW** (07-24 kink 148.6%, VRP +0.179, earnings 07-22) · **BE** (07-31 kink 248%, **VRP +0.544 richest**, earnings 07-28) · **ARM** (07-31 kink moderate, VRP +0.120, earnings 07-29 = **FOMC day, double event**, smaller size). All carry the front-only-kink / back-month-flat disqualifier → defined-risk condors, not naked short strangles.
- **BUY VOL (premium buying, RV outrunning IV):** **DRAM** (VRP −0.125, realized 118.6% > IV 106.1%) · **SOXL** (VRP −0.273, realized 218.6% > IV 191.3%, leveraged whipsaw) · **SOXX** (VRP −0.103, skew TAIL_HEDGING confirms real hedging demand). Backwardation shape is misleading here — do NOT sell.
- **Calendar candidate:** **OKTA** — mild backwardation, front-end panic resolved (ratio 1.029 FLAT); sell front (07-24, 95.1%) / buy back (07-32, 92.4%). Thin edge (IV percentile only 65th), size small.
- **IV outlier context:** MU 0DTE put cluster ($900P/$895P concentration) — whale-hedge signature consistent with the memory-complex vol event, not a discrete trade. Disqualified as artifacts: CF/MCHP/OUST/QXO (elevated front-end-iv with no catalyst inside the front tenor — unweighted-strike wing contamination); PLXS (degenerate 1–8 contract data); SKHY (only 4 dates of history).

**Data-quality note for the audit:** RMBS/SANM/KLAC/NXPI returned term-structure curves with **no near-dated tenor** (first bucket dte≈32) — earnings land in a dte gap the parquet snapshot doesn't index (no weeklies) → not readable, excluded rather than mis-scored. And `vol-surface-scout` did not emit `implied_move_pct` on BE/NOW/ARM (C43 instrumentation gap, 2nd consecutive session).

## 6. Risk & Correlation
`risk-monitor` — **13th consecutive empty board; gate-record + hygiene pass, no sizing pass.**

- **Macro headline:** sticky core PCE 3.41%, 10Y 4.55% rising, USD strengthening = tightening drift. **Forward event_risk:** INTC 07-23 (T+3), **FOMC 07-29 (T+7)**, Q2 GDP 07-30, **Core PCE 07-31 (T+9)**. FOMC at T+7 → −0.5 size-step on any undefined-risk swing held through the print (would apply to TSM/AVGO/LULU/SHOP had they scored).
- **Panic gate: NO-OP.** SPY front-end-iv-ratio **0.965 FLAT** (near-dte 1); 0.828 CONTANGO at near-dte 7 — orderly term structure despite VIX 18.65.
- **Correlation cluster (mechanical):** **`semis_memory_cluster` — {INTC, TSM, MRVL, SNDK, AVGO, ARM} is ONE position** (INTC/MRVL 0.888, INTC/TSM 0.854, TSM/MRVL 0.818, MRVL/ARM 0.814, SNDK/MRVL 0.789, AVGO/ARM 0.782, INTC/SNDK 0.750). Directionally incoherent (INTC long-vol, TSM/AVGO short, SNDK bearish) — the whole board is functionally one memory/semis bet plus LULU. Kept member = INTC (raw 2); every other member takes −1 tier (all already at skip).
- **Fundamentals verdicts (top-5):** INTC **CONFIRM** (vol thesis, event is the point; beat streak 4/4 but net-margin −5.9%, rev +1.4% — turnaround unconfirmed). TSM/SNDK/LULU/AVGO **CAUTION/−1** — TSM (beat+growth fight the short), SNDK (insider MSPR −100 ×3mo = real distribution but growth intact; flow internally contradictory), LULU (fresh downgrade stack vs insider buying, EPS −16% YoY), AVGO (insider selling accelerating −100 vs strong growth, stretched 62× PE). **`fz_context` unavailable on all 5** (upstream Finviz-grid total-miss — SI/float/analyst all null; the known 07-17 pattern recurring, log for audit).
- **Adverse-flow exits (hygiene vs `conviction_week_2026-W28` {SNDK, NVDA, JPM, SOFI, META} — note `conviction_2026-07-17` never existed, 4th all-DROP board wrote nothing):** **SNDK** (bearish −$5.6M, IV rank 100, $470M DP print — EXIT), **META** (bearish −$19.7M, IV rank 92 — EXIT), **NVDA** (bearish −$45.1M, largest adverse flow — EXIT), SOFI (mild, monitor), JPM (on-thesis, hold).
- **Hedge sleeve:** **not required** — empty book, net delta 0. VIX 18.65 with FLAT/CONTANGO front makes standing long-vol overlays unattractive absent a position.
- **Breadth divergence:** none (fz pct_green 32.6% confirms the weak `uw` regime, no green-tape-with-weak-breadth distribution tell).

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**EMPTY — no HIGH or MEDIUM tier names.** Top raw score on the board is 2 (INTC); zero names reach even LOW (≥3). No names sized above `skip`; no watchlist write-back performed (per the empty-book protocol, DROP names are never persisted).

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no per-tier realized expectancy to display — the last several `/calibration-audit` cycles report the DROP pile (43.3%, 07-18) *out-performing* the traded book (38.6% sized), which is the empirical case for empty-board discipline. There is no live book to compute payoff ratios over this session.

### Conviction-scoring rubric (frozen `2026-06-12`) — embedded for audit
```
Daily conviction score = Σ:
  +1 dealer-positioning MECHANIZED DEX flip / vanna-squeeze in trade direction (verified sign change, dated cites)
  +3 accumulation-hunter 3+ aligned (DP+OI+smart-positioning+block-stratified institutional) — CONJUNCTION: full +3 only if cum_flow_30d sign-aligned AND |cum_flow_30d|≥$50M; else floored +3→+1
  +1 multi-day OI build (oi-trend BUILDING, --days≥5)
  +1 conviction-matrix DIRECTIONAL_LONG conf>70 — ONLY if dominant_signal_class==leap_directional, else 0
  +1 cum-premium-flow net directional accretion in trade dir (30d) — INTENT-SCREENED (no C28 distribution_flag; not deep-ITM sub-parity div-capture); else 0
  +1 sector-rotation single-name leader — ONLY if persistence≥0.6 AND cum_flow_30d aligned AND |cum_flow_30d|≥$50M
  +1 earnings-scout BUY VOL or SELL VOL
  +2 multileg-strategist directional structure (term-structure-anchored)
  +1 vol-surface KINKED or BACKWARDATION with VRP-aligned bias
  +1 opex-pin top-5 (OPEX week only)
  -2 contrarian overcrowded long with rising pc-z (VRP+)
  -3 flow_conflict (cum_flow_30d clearly OPPOSITE dominant_signal_class)
  -1 flow_conflict_lite (MIXED cum_flow) — mutually exclusive with flow_conflict
  [TIER GATES, 2d, not score_components]: -1 tier correlation cluster (corr≥0.70); -1 tier regime conflict
Tiers: ≥9 HIGH (full) · 7-8 MEDIUM (half) · 3-6 LOW (starter/watch) · ≤2 drop
Out-of-regime guard (P0.6): all conviction sizing capped at HALF until a /calibration-audit records ≥30 resolved post-2026-06-12 calls and re-validates tiers.
```

## 8. Watch-only — single signal, no confluence
Surfaced by one agent, failed the ≥2-agent confluence gate — journaling only, NOT trade entry:
- **BE / NOW / ARM** — vol-surface SELL VOL kinks (earnings 07-28 / 07-22 / 07-29). ARM's print is FOMC-day (double event). NOW/ARM also earnings-scout SKIP (neutral/plateau).
- **DRAM / SOXL / SOXX** — vol-surface BUY VOL (RV>IV); ETFs, no directional confluence.
- **OKTA** — vol-surface calendar candidate (panic resolved); thin edge.
- **MRVL** — dealer DEX flip (per-strike unverified → 0 pts) + conflicting bullish sweep tail.
- **SPCX** — 4/5 bullish sweep, but flow_conflict −3 + index-weight caution.
- **OUST** — C19 Tier-1 opening-put advisory (0 pts), no DP corroboration.
- **CFG** — accumulation-hunter near-miss (conviction-matrix DIRECTIONAL_LONG 51.6%) but **rejected by the closing-cross rule** (81% of DP share at the exact $71.50 close, MOC contamination). Flagged so it is NOT re-admitted via a looser filter.

---
*Fleet: 10 Phase-1 agents (opex-pin-strategist omitted — post-monthly-expiry Monday, next monthly Aug 21). Phase 2: quant → fundamentals-gate → risk-monitor. Bull/bear debate (2c) skipped — no name reached LOW tier, so the debate had nothing to gate. Deep-dive/batch-scan (Steps 6/6.5) and deep-dive hand-off (8.5) skipped per empty-board protocol.*
