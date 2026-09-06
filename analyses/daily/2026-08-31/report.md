# Daily Market Analysis — 2026-08-31

## Executive Summary

- **Regime + GEX state:** TRANSITIONAL / PULLBACK_IN_UPTREND. SPY 767.05 (−0.30%, below the 20sma 769.68, above the 50sma 754.36). **SPY dealer gamma is SHORT (`total_gex` −$1.03B)** — the `regime` label prints POSITIVE and contradicts its own sign for the 5th session this month; trust the sign. QQQ is long-gamma pinned at 717. VIX 14.92 (+3.40% on the day, −5.87% over 5d). Breadth is genuinely weak — 136 advancers / 362 decliners, **27.04% green**, `uw` bullish-flow 33.8%. **Narrow tape: XLE +2.04% and XLK +0.44% are the only green sectors; RSP (equal-weight) −0.59% underperforms SPY −0.30%.**
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL/PULLBACK_IN_UPTREND) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** SPY — short-gamma, ZGL unreliable (305.49, extrapolated), call wall 780 (+1.7%), **put wall 765 sitting only 0.25% below spot** with −$228M and almost no cushion beneath it → trend/breakout bias, not premium-selling. QQQ — long-gamma, ZGL unreliable (212.59), **call wall 717 essentially ON spot** (+$207M concentrated in one strike), put wall 700 (−2.26%) → pin / mean-reversion bias. Advisory, see §2.
- **Top swing build:** **None.** No name reached the LOW floor.
- **Top LEAP candidate:** **None.** `leap-positioning-radar` returned zero candidates; among C12-passing names every fresh DTE≥180 OI increase today is a **put**.
- **Biggest risk:** Not a position — an **absence** of one. The concentration worth naming is structural: the four `vol_short` earnings names (SNOW/MDB/LULU/MDT) are all short vega into the **same 2026-09-04 expiry, which is NFP morning** — one risk expressed four times, and invisible to a price-correlation matrix (max pairwise 0.670, no pair ≥0.70).

> **NO-EDGE DAY. Zero positions sized. Zero watchlist writes.** All 8 candidates scored `raw_score ≤ 2` against a LOW floor of 3 — the board was 100% DROP *before any risk gate fired*. This is the **39th consecutive empty daily board** (re-derived mechanically by globbing `analyses/daily/*/decision.json`; 68 daily envelopes, last sized session **2026-07-07**).

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity"**, trend **PULLBACK_IN_UPTREND**, guidance *"Half position sizes. Favor defined-risk strategies."* Market breadth 2,124 bullish / 4,164 bearish of 6,288 tickers with options = **33.8% bullish**.

| Index | Spot | Zero-gamma (ZGL) | ZGL reliable | `total_gex` | Regime (SIGN, not label) | Call wall | Put wall |
|---|---|---|---|---|---|---|---|
| SPY | 766.92 | 305.49 | **false** | **−$1,034,244,205** | **SHORT GAMMA** | 780 (+1.7%) | **765 (−0.25%)** |
| QQQ | 716.17 | 212.59 | **false** | +$197,229,817 | LONG GAMMA | **717 (+0.12%)** | 700 (−2.26%) |
| IWM | 293.93 | not trustworthy this window | false | −$1.56B (most negative of 11-session window) | SHORT GAMMA, deepening | — | — |

**Substrate defect, reconfirmed and worse than the documented baseline.** The GEX `regime` label contradicted its own `total_gex` sign on SPY today *and* on 08-19, 08-24, 08-25 and 08-26 — 5 of the last ~15 sessions, against a documented "3 of 4" baseline. QQQ decouples less often but not never (08-18, 08-20). **Every read above uses the `total_gex` sign as ground truth.** Both ZGLs are extrapolated garbage (305 and 213 against spots of 767 and 716), so both carry `zgl_reliable: false`.

**DTE volume share:** 0DTE 37.9% · weeklies 23.2% · monthlies 19.2% · LEAPs 4.1% — `regime_hint: BALANCED`. No institutional-vs-retail thumb on the scale.

**VRP:** SPY **FAIR** (−0.0006; IV30 11.87% vs realised 11.93%) · QQQ **FAIR-negative** (−0.0439; IV30 16.67% vs realised 21.05%). At the index, **IV sits at-or-below realised — the tape pays for *buying* vol, not selling it.** Hold that thought against a board whose only confluence-passing conviction was four short-vol names.

**Macro backdrop** (`scripts/fred_macro.py`): curve **normal** (10y2y +0.41) · core CPI 2.79% YoY · **core PCE 3.34% YoY (sticky)** · unemployment 4.1% · **payrolls −23k MoM (negative)** · 10Y **4.73% and rising** (+0.06 over 30d) · USD weakening (−2.04 over 30d) · fed funds 3.63%. Sticky core inflation against a deteriorating labour print with long rates rising — a **stagflation-tinged** backdrop.

**Forward event risk (T+0 = 2026-08-31):**

| Event | Date | Trading days out | Tier |
|---|---|---|---|
| JOLTS | 2026-09-02 | T+2 | 2 |
| **Non-farm payrolls** | **2026-09-04** | **T+4** | **1** |
| PPI | 2026-09-10 | T+8 | 1 |
| **CPI** | **2026-09-11** | **T+9** | **1** |
| **FOMC decision** | **2026-09-15/16** | **T+11/12** | **1** |

Four Tier-1 binaries inside twelve trading days. Any 1–6 week swing sized today carries all of them.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book, built from open interest that persists overnight, read forward as the *prior* for the next session's open. **Prose-only, 0 rubric points, no backtested predictive claim.** Predictive validation lives in `/weekly-analysis`'s rolling §2 backtest. Scope is SPY and QQQ only.

**SPY — short gamma, spot sitting on the put wall.** `total_gex` −$1.03B. The negative-GEX cluster is not diffuse: strikes 760–770 bracket spot and each carries −$60M to −$228M, so dealers are hedged short exactly where price is. The put wall at 765 is **0.25% below spot**, and beneath it the next shelf (760, −$170M) offers little cushion — a break below 765 has acceleration risk. The call wall at 780 (+$71.5M) is the first real positive-GEX resistance. **Structure bias:** debit verticals / directional 0DTE / long straddle over premium-selling. If premium is sold anyway, keep it defined-risk and narrow — dealer hedging amplifies rather than dampens here.

**QQQ — long gamma, at-the-money pin.** `total_gex` +$197M, and nearly the entire net-positive book is concentrated in the single 717 strike sitting on spot (716.17). Classic pin setup: vol suppression and mean-reversion toward 716–717, with real downside support only near 700. **Structure bias:** iron fly / short straddle / butterfly centred 716–717; condor wings can extend toward 700.

Note the two indices are in **opposite gamma regimes tonight** while both quote a "POSITIVE" label — a clean illustration of why the label cannot be trusted without the sign check.

**Mandatory caveats:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and re-computes the ZGL and walls.
- **ZGL reliability.** Both ZGLs are extrapolated (SPY 305.49, QQQ 212.59 vs spots of 767 and 716) → `zgl_reliable: false` on both. The reads rest on the `total_gex` sign plus spot-vs-wall position only.
- **Gap risk voids the prior.** NFP is T+4; no Tier-1 print lands before the next open, but the book is jumpy into it.
- **Tooling limit.** `uw` cannot isolate the D+1 expiry (`gex --dte-max 1` errors). This is the standing **0–45 DTE** book.
- **ETF book**, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup

`scripts/zerodte_setup.py` returns `GO_PREMIUM_SELL_INTRADAY` on both indices — **and that verdict is unconditional and must not be read as a live green light today.**

| | `sell_premium` | vol_state | VIX | implied move | expected range | size_scalar | Suggested structure |
|---|---|---|---|---|---|---|---|
| SPY | true | **LOW** | 14.92 | 0.63% | 1.09% | 0.5 | Wider iron condor, wings ≈ ±1.09% (short-gamma: wider/trendier) — or reduce / stand aside |
| QQQ | true | **LOW** | 14.92 | 0.94% | 1.37% | 0.5 | Iron fly / short straddle centred 717.0, wings ≈ ±1.37% (long-gamma) |

**The LOW-VIX caveat is the whole story.** Report the PnL on its real basis — `mean_pnl_open_pct` is **percent-of-underlying-spot-notional, GROSS**, not premium-collected and not margin-relative. Net of the assumed 0.100% round-trip cost, and read at the **observed** vol state rather than unconditionally:

| | LOW tercile (gross) | net of cost | MID | HIGH |
|---|---|---|---|---|
| SPY | 0.142% | **+0.042% — essentially ZERO** | 0.202% | 0.331% |
| QQQ | 0.202% | **+0.102%** | 0.326% | 0.493% |

VIX 14.92 sits in the **LOW** tercile (bounds 15.8 / 17.3). The headline gross win-rates (SPY 86.7%, QQQ 85.0%, n=60) overstate a negatively-skewed seller's edge; **the edge lives in the MID/HIGH terciles, not here.** Worse, SPY's dealer book is short-gamma tonight, which directly contradicts a premium-selling posture. **Entry rule if traded anyway:** enter at/after the open once the gap resolves, hold to the close, never carry overnight (overnight entry backtested +0.024% on SPY, −0.107% on QQQ). Stand aside if it gaps beyond the wings.

**Promotion bar (P1.8):** this lane stays advisory / 0 rubric points **permanently** until both a vol-shock day enters the sample (the short-vol left tail is currently UNSAMPLED — worst day −1.4% SPY / −2.45% QQQ) and net expectancy clears a tail-aware bar. Win-rate is explicitly NOT the promotion metric.

---

## 2b. Swing Dealer Positioning (1–4 weeks)

**Zero mechanized DEX flips qualify today.** `scripts/dex_flip.py` returned `qualifies: false` on all six names tested (SPY, QQQ, IWM, MU, PANW, TSLA). No `vanna_squeeze_flag` fires anywhere — the falling-VIX leg broke today (^VIX 08-24 15.85 → 08-28 14.43, four consecutive declines, then **08-31 14.92, +3.40%**).

| Name | DEX (08-31) | 5d trajectory | `sign_changes` | Verdict |
|---|---|---|---|---|
| SPY | +$13.54B | choppy, peaked +$32.2B (08-27) | 4, **whipsaw** | FLAT |
| QQQ | +$16.63B | receding from +$31.5B | 2 | FLAT — GEX oscillates across ZGL **3× in 10 sessions** (instability marker) |
| **IWM** | **−$9.02B** | **deteriorating, 3 sessions accelerating** | 3 | **SHORT** (qualitative, see below) |
| MU | +$7.88B | rising magnitude ~2.4× | **0** | FLAT — **LEVEL, NOT FLIP** |
| PANW | +$1.16B | choppy around an 08-27 spot dislocation | 0 | FLAT — level, not flip |
| TSLA | +$5.91B | no usable trend | **8 of 11, whipsaw** | DISQUALIFIED — noise |

**IWM is the one live swing thesis, and it is a `watch_only` short.** DEX −$9.02B is the most negative of the 11-session window with put-dex −$16.51B against call-dex +$7.49B; GEX −$1.56B likewise the most negative of the window. But **the mechanized line does not fire**: the actual sign flip happened **2026-08-24, six sessions ago**, and the trigger requires a sign change on the *latest* session. This is a **level, not a flip** — and the book is put-heavy (net_vanna +118,764), which would be a textbook vanna-squeeze *long* setup if VIX were still falling. It is not. Flagged as **"vanna pressure, not squeeze."**

**MU is explicitly flagged as level-not-flip** — `sign_changes_in_window: 0`, net call-long every session in the 11-day window. This is the exact pattern that caused the 2026-06-11 mis-scoring which demoted this rubric line from +3 to +1 and mechanized it. It earned zero.

---

## 2c. Sector Rotation

**Rotation regime call: `no_change`.** Technology is the only fully-confirmed rotation-in sector; no confirmed offsetting outflow leg exists, so no canonical two-sided pattern is available.

**Direction comes only from the netted source.** `uw risk market-regime.sector_rotation`:
- **IN:** Technology +$150.1M · Consumer Cyclical +$77.1M · Consumer Defensive +$14.1M
- **OUT:** Industrials −$65.2M · Communication Services −$25.7M · Basic Materials −$9.1M

| Sector | Netted (authoritative) | Gross `sector-flow` | Persistence | Agreement |
|---|---|---|---|---|
| Technology | **IN +$150.1M** | +$2,141.2M | 1.00 | **agree → CALL** |
| Consumer Cyclical | IN +$77.1M | +$558.1M | 0.80 | agree, below standout bar → watch |
| Consumer Defensive | IN +$14.1M | +$18.0M | 0.80 | agree, below standout bar → watch |
| Industrials | **OUT −$65.2M** | **+$142.1M** | 0.80 | **DISAGREE → watch_only** |
| Communication Services | **OUT −$25.7M** | **+$232.5M** | 0.80 | **DISAGREE → watch_only** |
| Basic Materials | **OUT −$9.1M** | **+$64.4M** | 1.00 | **DISAGREE → watch_only** |
| Energy, Financials, Healthcare, Utilities, Real Estate | **unmeasurable** (outside the netted top-3/bottom-3 truncation) | — | 1.00 / 0.80 | n/a |

**Substrate defect, reconfirmed:** `sector-flow-persistence` fired **INFLOW / persistence_score 1.0 on 11 of 11 sectors**. It is sign-agnostic gross turnover and is **one source with `sector-flow`, not two** — a durability filter that cannot express direction. Today's contradiction makes this concrete: gross reads Industrials and Basic Materials as INFLOW while netted reads both as OUTFLOW.

**Technology's rotation-in is SEMIS/AI-INFRA led, not broad tech.** Leaders: MU (+$71.6M), NVDA (+$31.6M), LITE (+$16.3M), COIN (+$15.5M), PLTR (+$13.9M), SNDK (+$13.3M), CRWD (+$11.8M), APP (+$11.7M). **Laggards inside the same GICS bucket:** AAPL (−$18.6M), MSFT (−$11.2M), SNOW (−$14.5M), TTD (−$13.4M), AMD (−$8.1M), PANW (−$7.6M), MRVL (−$6.7M), INTU (−$6.1M).

### ETF flow tape (advisory — 0 rubric points)

Ranked by 5d `cumulative-premium-flow` across the canonical universe (33 `uw` calls, under the 40 cap):

| ETF | Net premium dir | DP positioning | Options urgency | GICS agreement | Leaders |
|---|---|---|---|---|---|
| **SMH** | **inflow +$36.98M** | Large prints ($10–14M), mostly below-mid (hedging/creation) | Mixed: Nov $530P sold ($24.9M) vs $550P bought ($16.6M), net bullish-noisy | **agree** (Tech) | MU, NVDA, LITE, SNDK |
| **XLK** | **inflow +$10.95M** | Mostly above-mid (buy-side lean) | Short-dated (9/4) call buying 140/145/155, modest | **agree** (Tech) | same |
| **IGV** | inflow +$6.47M | Mixed, below-mid | Thin, mild bullish | **agree** (Tech) | same |
| XOP | **outflow −$12.28M** | Small, buy-side lean (~$4M) | Thin, LEAP calls only | n/a (Energy unmeasurable) | — |
| GDX | outflow −$10.58M | Large ($10–22M), mixed sign | No clean urgency | agrees with netted Basic Materials OUT | — |
| EWY | outflow −$7.88M | Mixed | $10.3M Nov $155P (protective hedge) | n/a (geographic) | — |

**Energy reconciliation — the most important thing this lane did today.** XLE closed **+2.04%, the day's best sector**, and the `fz` new-high lane is 6-of-9 energy refiners (CVI, DINO, SLB, VLO, DK, MPC). That is the most rotation-*looking* signal on the tape. But **the multi-day options flow does not confirm it**: XLE's own 5d net flow is flat (−$0.05M) and **XOP is −$12.28M outflow**. Energy also sits outside the netted top-3/bottom-3 truncation, so it has *no* netted direction available. **Verdict: single-day price momentum in refiners, not a flow-confirmed multi-day rotation. Appendix only — not called.**

---

## 3. Swing Setups (1–6 weeks)

**Empty. No name reached the LOW floor (raw_score ≥ 3).** The full scored board appears in §7.

### 3a. Long swings (regime-aligned)

**None sized.** The two long-side names both failed on their own evidence:

- **NVDA** (raw 2, `vol_long`) — the long-gamma thesis rested on a −13.8pp VRP gap that the debate **falsified**. See §7.
- **MU** (raw 1, `vol_long`) — the day's most-cited bullish name (screener +$71.6M, funnel confluence 5 with `bullish_flow`/`dp_accumulation`/`oi_building` factors), and **every one of those bits failed verification against a 30-day window**: cum_flow_30d is **−$49.6M** (5d −$30.8M, consistently negative) against a single session's +$71.6M; `oi_building` is **5-of-6 top adds being PUTS**; `dp_accumulation` sits behind a **61.7% closing-cross top-bucket share** on month-end with a confirmed basket print in the tape. The sector-leader gate fails both (b) *and* (c) — it misses the $50M floor by $0.4M and is on the wrong side anyway. The one surviving point is a genuine vol dislocation (IV **32.7pp** under RV, the widest on the board) — a real long-gamma observation that earns prose, not a position.

**Distribution cautions (C28, advisory — 0 points, no sizing impact):** ⚠ **AAPL** 325C −2,413 ($6.67M), 310C −1,878, 320C −1,829, 300C −1,627 — institutional-size call-OI closing. ⚠ **META** 270319C700 −1,686 ($5.78M), 260918C600 −1,394 ($5.98M). ⚠ **NVDA** call-side closes ~134k contracts vs put-side ~49k (3:1). ⚠ **TSLA** call-side, smaller magnitude. These are the names carrying the loudest (contamination-driven) "ACCUMULATION" dark-pool labels today.

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only` (2026-08-01 P0 #1) — routing, not suppression.** Theses are generated, scored, fully gate-verdicted and serialized so the counterfactual keeps resolving.

- **IWM — SHORT, `watch_only`.** DEX −$9.02B and GEX −$1.56B, both the most negative of an 11-session window and both still deteriorating. **Kill:** the mechanized flip is six sessions stale (08-24), so `dex_flip.py` says `qualifies: false` — a level, not a flip. raw_score **0**. Additionally the carried 08-21 IWM short is now an **exit candidate** (see §6). Note the irony: IWM appears as a fresh short today while the carried short is being tagged for adverse flow.
- **PANW — SHORT, `watch_only`.** Entered under the generation floor with **zero positive Phase 1 agent flags**. Its whole case is a Tier-1 `OPENING_PUT_PRIME` ($400P, dte=4, $1.61M, size/OI 5.44), which is **permanently 0 rubric points** (C19 closed as REFUTED), plus a −$7.58M bearish screener print. Against it, `flow_conflict_lite` fires: 30d cum-flow **+$13.5M runs against** the short, and the staleness falsifier came back the *other* way — 5d is +$14.16M, so essentially all of the opposing flow is **fresh**. raw_score **−1**, the only negative on the board. See the beta flag in §7.
- **Contrarian lane: EMPTY**, for three independent and individually sufficient reasons. (1) VRP is not positive on SPY (−0.0006) or QQQ (−0.0439) — a blanket exclusion, not a QQQ-specific one. (2) No single name reached ±2σ with divergence. The two that flagged were both disqualified on inspection: **GLD** z=2.715 but `price-vs-flow` shows **alignment**, not divergence, and the closing activity is call-side profit-taking into a rally (structural hedge bid, not crowd euphoria); **XAR** z=2.241 is a thin-book artifact ($67K call premium vs $5.5M put) with `oi decrease-with-volume` returning **zero rows**. (3) LOW VIX + TRANSITIONAL is not a fade backdrop. Index P/C z-scores: SPY 0.651, QQQ 1.743 — both NORMAL. Closest single names: PLTR 1.958, GS −1.948, CRWD −1.81 — none clear.

### Sweeps (informational — 0 rubric points)

The sweep-persistence rubric line was removed 2026-05-23 (P0.3) after two consecutive audits measured −22pp marginal contribution. Ranked persistence-first:

| Rank | Ticker | 5d dir | Persist | 5d premium | Read |
|---|---|---|---|---|---|
| 1 | MU | bearish (net) | 5/5 | $2.34B | **Contradicts** — today's tape is mixed-side calls, both ask and bid, high trade counts |
| 2 | MSTR | bearish (net) | 5/5 | $838.9M | Mixed; LEAP call bid $3.99M vs near-term call ask $3.43M |
| 3 | SPCX | bullish | 5/5 | $617.4M | **Direct contradiction** — today's largest print is a **$46.0M PUT ask**, 1,498 size, 270 trades |
| 4 | PLTR | bearish (net) | 5/5 | $480.6M | 2027-03 call spread structure — not a directional sweep |
| 5 | **MSFT** | **bullish** | 4/5 | $891.4M | **The only name where persistence, cum_flow_30d (+$782.8M) and the mega-cap filter all agree** |
| 6 | AMD | bearish | 4/5 | $464.7M | Call bid $8.2M, 14 trades — block, not sweep |

**Headline: no name has a same-direction confirmed sweep today that also matches its 5-day persistence tag.** Hedge-flow demotions: SPY (sweep bearish 5/5 vs cum_flow **+$63.5M bullish**), QQQ (bearish 5/5 vs **+$503.4M bullish**), TSLA (bullish 5/5 vs **−$483.2M bearish**). Disqualified as mixed-direction: NVDA, META, SNDK, AMZN, AAPL.

**The tape-wide fact that frames all of this:** today's raw single-leg whale scan is **102 of 155 `CLOSING_ANTISIGNAL` (66%)**. Two-thirds of large single-leg prints are position *closing*, not opening. Pan-Poteshman: only opening flow predicts.

---

## 4. LEAP Builds (6–24 months)

**Empty. Zero candidates pass the 6-of-9 gate.**

Among C12-passing names, **every fresh DTE≥180 OI increase today is a put** — IBIT ($35P/$30P), PCG ($10P), XLF ($30P), IWM ($285P), SPCX ($115P). There is no fresh bullish LEAP call build in the top of funnel.

Disqualification trail on the five names tested:

| Name | 30d cum-flow | 90d cum-flow | Decay verdict | `conviction-matrix` | Result |
|---|---|---|---|---|---|
| MSFT | +$782.8M | +$427.6M | **DECAY** — day 31–90 was −$355.2M; rate collapses $26.1M/d → $4.75M/d | MIXED, 3.9% | DQ |
| SPCX | +$27.1M | **−$298.8M** | **DECAY** — sign reverses | MIXED, 6.7% | DQ |
| LITE | +$82.2M | +$57.0M | **DECAY** in miniature | DIRECTIONAL_LONG but **24.5%** ≪ 70 | DQ |
| GOOG | −$146.6M | −$115.8M | bearish both windows | **DIRECTIONAL_SHORT, 38%** (DP buy_ratio 0.179) | DQ |
| SNDK | +$963.5M | +$2,756.8M | **PASSES** ($32.1M/d vs $30.6M/d) | MIXED, 7.4% | DQ — own long-dated print is a $1,340 **PUT** |

The **decay falsifier** (cum-flow that shrinks as the window widens is not accumulation — a real program does the opposite) killed four of five and is cheaper and sharper than the contamination screen. `oi-trend BUILDING` fired **5-of-5 (100%)** here, reconfirming its zero discrimination.

---

## 5. Volatility Surface

**Substrate hygiene is the headline.** `scripts/term_structure_hygiene.py` (`min_contracts=15` — a **named, tunable parameter that is NOT audit-frozen**; reported, not treated as settled): raw labels said **BACKWARDATION on 8 of 10** names; after dropping the 0DTE/expired bucket and thin tenors, **7 of 10 flipped** on the kink-aware shape and **5 of 10** on the monotonic base shape. Corrected distribution: **BACKWARDATION 3 / KINKED 7**.

Two further substrate findings:
- **`iv_outliers` is 100% contaminated** — all 20 cached rows sit on the 2026-08-31 (0DTE) expiry, so the 50–956% max-IV readings are 0DTE-wing artifacts. **No usable single-contract outlier today.**
- **`iv-percentile-zscore` short-delivered its lookback** — `dates_used = 98` against a 120-day floor. **Every IV percentile in this report is PROVISIONAL.**

### BUY VOL — the unconstrained lane (where the measured edge lives)

| Ticker | raw → shape (base) | kink dte / prom | front-end @7d | VRP | IV30 vs RV30 | implied move |
|---|---|---|---|---|---|---|
| **NVDA** | BACKWARDATION → **KINKED** (FLAT) | 11 / 7.7% | 0.852 CONTANGO | **−0.1385** | 31.4% vs 45.2% (−13.8pp) | 5.86% |
| **MU** | BACKWARDATION → **KINKED** (CONTANGO) | 4 / 12.8% | 0.767 CONTANGO | **−0.3273** | 60.4% vs 93.2% (**−32.7pp**) | 6.98% |
| **AMD** | BACKWARDATION → **KINKED** (CONTANGO) | 4 / 5.8% † | 1.005 FLAT | **−0.2517** | 48.2% vs 73.4% (−25.2pp) | 6.32% |

† AMD's kink prominence barely clears the 5.0% threshold — marginal. AMD also **fails the confluence gate** (single agent) and is a sector-rotation *laggard*.

`vol_long` is explicitly **unconstrained** and is the lane with measured edge: **+9.5pp against unselected same-date single-name peers (n=43, paired McNemar p=0.0034), 5-for-5 on every sized row in the corpus.** That makes the NVDA debate finding below genuinely costly — this was the right lane, and the evidence still did not hold.

### Index level

SPY and QQQ both raw CONTANGO → **KINKED**, with kink candidates at **dte 4 (NFP), 11 (CPI) and 18 (FOMC)**. This is the forward event stack showing up in the surface, **not a mispricing**. QQQ carries a mild BUY VOL tilt (VRP −0.0439, IV percentile ~0, provisional). Not sized at index level.

### SELL VOL — all routed `watch_only`

| Ticker | shape / base | front-end @7d | VRP | Earnings | implied move | Verdict |
|---|---|---|---|---|---|---|
| MDT | BACKWARDATION / BACKWARDATION | 2.174 | +0.1168 | 09-01 AM (T+1) | 4.72% | SELL VOL → `watch_only` |
| MDB | BACKWARDATION / BACKWARDATION | **2.279** | +0.217 | 09-01 PM (T+1) | 13.52% | SELL VOL → `watch_only` |
| SNOW | → KINKED / BACKWARDATION | 2.148 | **+0.3025** | 09-02 PM (T+2) | 10.12% | SELL VOL → `watch_only` |
| LULU | → KINKED / BACKWARDATION | 2.082 | +0.1832 | 09-03 PM (T+3) | 8.56% | SELL VOL → `watch_only` |
| PANW | BACKWARDATION / BACKWARDATION | 2.207 | +0.0276 **FAIR** | 09-01 PM (T+1) | 7.81% | **SKIP** — no vol edge |

**`front-end-iv-ratio` fired 5-of-5 = 100% population rate.** Per the population-firing-rate rule this is **non-discriminating** — it fires before every event (Dubinsky et al.) — so VRP sign was the only real discriminator, and it is what separated PANW (FAIR +0.0276 → SKIP) from the other four.

**SNOW and LULU flip to KINKED, but their kinks are NOT at earnings** — both land at `kink_dte=18` = **2026-09-18, September OPEX**, 16 and 15 days after their prints. That is open-interest concentration, not an event hump. **Kink-at-earnings is explicitly not claimed for either name**, which removes what would normally be the strongest corroboration for a rich-vol read.

**Every one of these four has its front tenor on the 2026-09-04 expiry — NFP morning.** A short-vega structure there is short an earnings print *and* a Tier-1 macro release in one expiry.

**Cross-lane discrepancy, recorded:** `vol-surface-scout` derived higher implied moves from front-tenor IV than `earnings-scout` took from the cached field (MDB 20.7% vs 13.52%; SNOW 15.07% vs 10.12%; PANW 14.6% vs 7.81%; MDT 6.49% vs 4.72%; LULU 12.43% vs 8.56%). The earnings-scout figures are serialized as primary — all five names report within ≤4 days, which keeps `implied_move_perc` inside its valid bucket and avoids the documented pre-event-tenor defect. It changes no decision; all four route to `watch_only` regardless. **A third estimate exists and is higher still:** the SNOW bear found Bloomberg pricing the Sept-2 move at **~12%** vs the fleet's 10.12%.

### Multi-leg structures

- **QQQ collar — 715P / 740C, both 2026-12-31 (122 DTE), 38,000 lots each leg, identical timestamp 15:29:49Z, both `no_side`.** Parity test **passes both legs** (715P time value $29.61 = 99% extrinsic; 740C $24.36 = 100%). **$20.9M net debit** ($550/contract, 0.77% of notional) — a real-cost collar, which argues genuine downside-protection intent rather than a passive overlay. Term structure is clean CONTANGO with no dislocation at the back tenor → **event hedge, explicitly not a vol-mispricing play and not directional alpha.** It spans the entire NFP → CPI → FOMC cluster. `repeat_count: 1` — **repeat filter not cleared.**
- **GLD put vertical — 330P / 335P, 2027-01-15 (137 DTE), ~50,100 lots each**, both ~18–19% OTM against $408.42 spot. Parity test passes (100% time value both legs). **Direction unresolved** — no `side` tag available and neither leg reaches the top-premium endpoint, so buy-vs-sell cannot be mechanically confirmed. Structure confidence HIGH, direction confidence MEDIUM. Raw BACKWARDATION was **overridden as 0DTE contamination** (0DTE bucket 83.9% IV on 15,441 contracts vs a 22–30% band elsewhere) → clean curve reads **FLAT**.
- **Screened and skipped:** SPY 665P (highest-ranked line but no pairable leg → structure not cleanly inferable); PCG (candidate call builds at 17 vs 17.5 don't pair — watch item, genuine BACKWARDATION with thick tenors); **LULU returned zero multileg rows at top-500 / ratio 0.0** — today's −$5.75M bearish flow is single-leg by construction.

---

## 6. Risk & Correlation

**Macro headline:** stagflation-tinged — core PCE 3.34% sticky, payrolls −23k MoM, 10Y 4.73% and rising, USD weakening, curve normal +0.41. **Forward event risk:** NFP T+4, PPI T+8, CPI T+9, FOMC T+11/12 — four Tier-1 binaries in twelve trading days.

**Correlation.** `uw risk portfolio-correlation` run against **today's candidate union**, not the static watchlist. **No pair reaches the ≥0.70 mechanical threshold. Zero cluster penalties applied.** Four pairs sit in the 0.60–0.70 soft-watch band: SNOW/MDB 0.670, MDB/PANW 0.662, SNOW/PANW 0.618, NVDA/PANW 0.601. None upgraded — discretionary upgrades are exactly what the 2026-05-15 audit removed. Diversifying negatives: MDT/MU −0.540, NVDA/MDT −0.526. *(`sector_breakdown` returned `{"Unknown": 8}` with the spurious 100%-concentration warning — discarded per the known defect, not reported as a finding.)*

**The real concentration is invisible to that matrix, and it deserves naming.** SNOW, MDB, LULU and MDT are **short vega into the same 2026-09-04 expiry**. Their 30d *price* correlations are 0.54–0.67 and LULU/MDT barely correlate with the tech pair at all — yet a single vol-expansion event on 09-04 hits all four short-vega books simultaneously and in the same direction, regardless of relative share-price moves. That is **one risk expressed four times**, and a price-correlation tool structurally cannot see it because it measures underlying returns, not vega exposure to a shared event date. Recorded as an a-priori structural cluster (`vol_short_0904_expiry_cluster`); **not** converted into a mechanical deduction, because the gate's threshold is price-based and no pair clears it. Moot today — all four are `watch_only` — but this is the concentration that would not show up if a future board ever sized two of them.

**Fundamentals verdicts (top-5).** No VETOs.

| Ticker | Verdict | Reason | Tier adj | Contradicting fact | Next earnings |
|---|---|---|---|---|---|
| NVDA | **CAUTION** | `insider_selling_cluster` | −1 | Insider MSPR −98.61 (3mo avg) into a long thesis — though −95 to −100 for **17 consecutive months** reads as a routine 10b5-1 program, not distress. Revenue +70.68% YoY, EPS +110.34%, 3/3 beats, net margin 62.97% all corroborate | 2026-11-17 (78d) |
| SNOW | CONFIRM | — | 0 | — (only CONFIRM of the four vol_short names) | 2026-09-02 PM |
| MDB | **CAUTION** | `other` | −1 | **+64.0% and +50.1% EPS surprises the last two quarters** vs +10–13% before — that surprise variance is the reason to doubt whether a priced 13.52% move covers the tail on a T+1 print. Fresh PT raises (Cantor $540, DA Davidson $465) and a "~14% rally" headline sitting almost exactly at the priced move | 2026-09-01 PM |
| LULU | **CAUTION** | `earnings_surprise_streak_negative` | −1 | Most recent quarter **missed (−1.49%)**, breaking the streak. **MODERATE squeeze pressure** (short float 10.43%, 3.17 days-to-cover) — a beat could produce a covering-amplified gap beyond the priced 8.56%, the tail a short-vega seller is least protected against. Insider MSPR **+78.42 (net buying)** is a genuine bullish counter-tell | 2026-09-03 PM |
| MDT | CONFIRM | — | 0 | Most recent insider read (Aug-2026) is **+99.83 MSPR, +1.3M change** — the blended −33.39 3mo average understates the current tell | 2026-09-01 AM |

*`fz` analyst axis (`recom` / `upside_to_target_pct`) returned `null` on all five due to the documented upstream Finviz quote-parser gap — reported as NA-by-defect, not absent-by-choice.*

**Debate-disconfirmation cuts.** Run on the **top-2 only** — a documented reduction from the specified top-5, on the grounds that every name is DROP and the debate can only *cut* size (precedent: 2026-08-28). The other six carry `null` residuals, and **a null is recorded as "not evaluated", never as a passed gate.**

| Ticker | bull (advocate) | bear (kill) | Gate |
|---|---|---|---|
| NVDA | 0.40 | **0.65** | **−1 tier** |
| SNOW | 0.25 | **0.75** | **−1 tier** |

Both advocates were **sub-coin-flip on their own trade**. And both debates killed their own name's load-bearing evidence — detail in §7.

*Direction-adjustment note: the gate `bear_residual ≥ bull_residual ⇒ −1 tier` is written in long-oriented framing and **inverts on non-long calls**. On SNOW (`vol_short`) the trade-advocate is the bull (0.25) and the kill side is the bear (0.75); both scalars were direction-adjusted at prompt construction and are directly comparable, so the gate applies as written. This is the documented 2026-08-28 defect, still not mechanized — registered, not patched.*

**Adverse-flow exit candidates.** No `conviction_2026-08-28` group exists (that board was empty too), so the last populated group — **`conviction_2026-08-21` (IWM)** — was checked.

> **IWM — EXIT CANDIDATE.** `watchlist scan` reads `flow_direction: **bullish**`, net_flow **+$19.4M**, dp_total_premium $1.54B / 2,479 trades, `oi_net_change` **+432,438**, IV rank **1.10**, P/C 1.676. Three alerts: `LARGE_DARK_POOL` **high** ($256.9M single print), `OI_SHIFT` **high** (+432,438), `LOW_IV_RANK` medium. The carried short thesis is facing bullish net flow, a quarter-billion-dollar dark-pool print and a half-million-contract OI build. The −$266.4M/30d bearish read that would otherwise support it is **stale** — trailing 5d is **+$14.2M MIXED**. `fz quote-drift` shows no adverse fundamentals drift, so the exit tag rests entirely on the flow reversal. Note IWM's IV rank of **1.10**: if IWM downside is wanted later, options are historically cheap and buying optionality beats shorting delta into NFP/CPI/FOMC.

**Hedge sleeve: none required — there is no book to hedge.** Net delta is zero; every call routes to `skip` or `watch_only`, so the directional-skew trigger cannot be reached. For context only: the market is putting on precisely this hedge (the QQQ 715P/740C Dec-31 collar, $20.9M net debit, §5). If the desk carries legacy long exposure from outside this fleet, the NFP/CPI/FOMC stack argues for defined-risk protection on that book — but that is not a call this fleet is making today.

**Breadth (advisory, 0 points, no sizing impact).** 136 advancers / 362 decliners, **27.04% green**, median constituent −0.69%, average −0.64% (n=503). Top mover CRWD +5.77%; worst EIX −23.07%. **`divergence_flag: false`** — `uw` reports 33.8% bullish-flow tickers and the tape is red; both independent lineages agree breadth is weak, so there is no hidden-distribution divergence today. Only two green sectors, and RSP (−0.59%) underperforming SPY (−0.30%) confirms this is a narrow tape holding up on cap weight.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Empty — no name reached MEDIUM (7) or even LOW (3).** The full board is reproduced below for the audit trail.

**Expectancy lens `[advisory — expectancy is not yet a live sizing axis]`** — realised per-tier expectancy and payoff ratio from the 2026-08-30 `/calibration-audit` (§3.6):

| Tier | n | Expectancy | Payoff ratio (avg win / \|avg loss\|) |
|---|---|---|---|
| HIGH | 7 | −2.441% | 0.720 |
| MEDIUM | 19 | **+0.104%** | 0.948 |
| LOW | 125 | −2.141% | 0.906 |
| DROP | 542 | −5.964% | 0.601 |

Display-only context; the live sizer remains the win-rate ladder. Two things worth holding onto: the tier ordering is **non-monotone** (MEDIUM is the only positive-expectancy tier, and HIGH realises 14.3% WR against DROP's 38.0%), and **DROP's payoff ratio of 0.601 is far worse than LOW/MEDIUM** — the names the floor rejects lose badly when they lose, which is a mild independent vindication of a day like today.

### Full scored board (all 8 = DROP)

| # | Ticker | Dir | Raw | Tier | Class | WR | Source | Excess | Pre-risk | Fund | Debate (bull/bear) | **Final** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NVDA | vol_long | 2 | DROP | vol_term_dislocation | null | NA(substrate) | null | skip | CAUTION | 0.40 / 0.65 | **skip** |
| 2 | SNOW | vol_short | 2 | DROP | earnings_vol | null | NA(substrate) | null | watch_only | CONFIRM | 0.25 / 0.75 | **watch_only** |
| 3 | MDB | vol_short | 2 | DROP | earnings_vol | null | NA(substrate) | null | watch_only | CAUTION | — | **watch_only** |
| 4 | LULU | vol_short | 2 | DROP | earnings_vol | null | NA(substrate) | null | watch_only | CAUTION | — | **watch_only** |
| 5 | MDT | vol_short | 2 | DROP | earnings_vol | null | NA(substrate) | null | watch_only | CONFIRM | — | **watch_only** |
| 6 | MU | vol_long | 1 | DROP | vol_term_dislocation | null | NA(substrate) | null | skip | NA | — | **skip** |
| 7 | IWM | short | 0 | DROP | dealer_positioning | null | NA(substrate) | null | watch_only | NA | — | **watch_only** |
| 8 | PANW | short | **−1** | DROP | bearish_flow | **0.518** | backtest_clean (n=139) | **−0.0504** | watch_only | NA | — | **watch_only** |

### Why the board is empty — the structural reason

**Every point on this board came from two rubric lines, and both fired on ~100% of the population they screened:**
- **vol-surface +1** (KINKED/BACKWARDATION, VRP-aligned) — corrected labels were BACKWARDATION 3 / KINKED 7 = **10 of 10 scanned names**.
- **earnings-scout +1** (BUY VOL or SELL VOL) — fired 4 of 5 (80%); its own `front-end-iv-ratio` input fired **5-of-5 = 100%**, flagged non-discriminating by the owning agent.

Six names cluster at exactly 2 points made **entirely of non-discriminating evidence**, and the DROP floor is doing the real work. Meanwhile **every genuinely discriminating line was zero**: accumulation +3 (zero candidates market-wide), DEX-flip +1 (`qualifies:false` on all six), oi-trend +1 (direction-verification came back put-heavy against the long theses), multileg +2 (only a hedge and an unresolved-direction structure), conviction-matrix +1 (no LEAP), cum-flow +1 (intent screen failed or no accretion).

The rubric is **frozen at `2026-06-12`**, so both lines were awarded exactly as written rather than zeroed on a same-day observation — that is the discipline the freeze exists to enforce. Two findings are **registered for the next `/calibration-audit`, not acted on**:
1. **The vol-surface +1 needs a population-firing-rate grade** — it is the sole or joint source of every point on this board.
2. **The sector-leader +1 leaks around the cum-flow intent screen.** On NVDA the cum-flow +1 was zeroed by the C28 `distribution_flag`, and then the sector-leader line **paid out on the identical 30d cum-flow bit the screen had just disqualified** — its (b)/(c) conditions test the same field and the same $50M threshold. One bit, two rubric lines, and the screen leaked around itself. This is the single most defensible weight edit on today's board.

### Per-ticker detail — the two debated names

**NVDA — raw 2 — `skip`.** Components: **+1** vol-surface (`uw options-structure term-skew`) — KINKED dte=11, prominence 7.7%, VRP −0.1385, BUY VOL is VRP-aligned. **+1** sector-leader conditional (`uw options-flow sector-flow-persistence`) — Tech persistence 1.00 ✓, cum_flow_30d +$236.4M LONG-aligned ✓, ≥$50M ✓ (and it is **fresh** — $142.6M of the $236.4M landed in the last 5 sessions, so the staleness falsifier does not bite). Everything else zero, including the cum-flow +1 which the **C28 intent screen failed** (`distribution_flag` present, closing_side=call, ~134k call closes vs ~49k put, 3:1). Σ = 2 ✓.

> **The debate falsified the load-bearing number.** The bear pulled NVDA's daily bars and found **RV30 45.2% is 51.3% driven by three sessions** — the 08-27/08-28 earnings pair (+8.74%, −4.57%) and 07-27 (−4.99%); those two earnings days alone are **79.2% of the 10-day variance**. Strip the >4% outlier days and NVDA's ex-outlier realised vol over 27 sessions is **32.9% — essentially on top of the 31.4% IV30**, not 13.8pp beneath it. With earnings **78 days out**, that gap event **cannot recur inside an 11-day structure**; the artifact is mechanically rolling *out* of the RV window, so the measured "dislocation" shrinks toward fair over the coming sessions. Separately, the dte=11 kink **coincides with CPI (09-11)** and SPY/QQQ carry kink candidates at the *same* dte 4/11/18 — so this is **shared macro beta, not NVDA-specific edge**: a CPI-vol bet in an NVDA wrapper, bought at NVDA's earnings-contaminated entry price. The bull conceded the sector-leader double-count outright and could not refute that cheap vol can stay cheap (IVR 1.32, VIX −5.87% over 5d). **Bull 0.40 / bear 0.65.** The bear's own unrefuted point cuts the other way and is recorded: SPY confirmed short-gamma (−$1.03B) under a stacked NFP/PPI/CPI/FOMC calendar is a genuine forward amplification mechanism, independent of the RV-artifact finding.

**SNOW — raw 2 — `watch_only`.** Components: **+1** vol-surface (positive VRP + SELL VOL = aligned), **+1** earnings-scout SELL VOL (VRP-confirmed). Σ = 2 ✓. VRP **+0.3025** was the strongest on the board.

> **The debate falsified the richness claim using name-level data.** The bull's one unrefuted challenge was that class-level evidence does not prove *SNOW's own* +0.3025 VRP is mispriced. The bear met it directly: the IV30-vs-RV30 comparison is a **tenor mismatch** — RV30 is a trailing quiet-period measure with no earnings gap in it, while IV30 prices the coming gap, so the "VRP" partly measures the event's existence rather than its mispricing. Then the record: **SNOW's realised move exceeded its priced move in 4 of the last 8 quarters**, including **2026-05-27 at 41.1% realised against 12.2% implied — a 3.4× blowout** on the same beat-streak setup. And Bloomberg puts the Sept-2 expected move at **~12%** vs the fleet's 10.12%, meaning the "richest VRP on the board" may partly be a **low front-tenor IV input**. The bull conceded that SNOW's 4/4 double-digit beat streak "fits the mechanism uncomfortably well" and that it had "no mechanism-level rebuttal to why SNOW escapes the sign error rather than exemplifying it." **Bull 0.25 / bear 0.75** — the widest advocate/kill spread on the board. The bear conceded in return that LOW squeeze pressure (5.61% short float) genuinely removes the covering-driven tail, and that the CONFIRM fundamentals are real.

**PANW — raw −1 — `watch_only` — the only name with a live measured win-rate, and it is beta.**

> Full P0.3 clean-query protocol: `bearish_flow` **is** one of the five supported classes. `--top-n 200` pinned; latest data date 2026-08-31, so a 5-day forward window needs `signal_date ≤ 2026-08-24`. **160 rows → 149 kept** (11 dropped as forward-window-clamped), then the **C12 liquidity floor dropped 10 more** (CAR at $46.5M ADV; NDX as an index with no share volume) → **139 kept rows**, 43 distinct tickers, spanning 2026-07-07 → 2026-08-24. Graded on `pct_change` versus the **class** direction (DOWN), never the per-row `direction` field (which is `sign(pct_change)`, 100% by construction). **Clean WR = 72/139 = 0.518.** The tool headline (50.6% on 160 signals) was **never quoted**. Benchmark: a same-direction SPY short over the **same 139 windows** fell **79/139 = 0.568**. **`market_excess` = 0.518 − 0.568 = −0.0504.** Shorting the index over those windows beat the signal. That is **negative selection alpha** — the calibrated-but-beta profile the short-routing P0 exists for. Four independent mechanisms agree on the outcome: ladder said half, the excess gate cut to half, raw_score −1 puts it in DROP, and short routing makes it `watch_only`.

### Gate verdicts (all 9 keys, every call)

Full `gate_verdicts` blocks are serialized in `decision.json`. Summary of what actually fired:

| Ticker | regime | vrp | panic | cluster | sector | fundamentals | event_risk | debate | rubric_regime |
|---|---|---|---|---|---|---|---|---|---|
| NVDA | no-op | **−1** | no-op | no-op | no-op | **−1** | **−1** | **−1** | cap half |
| MU | no-op | no-op (supports) | no-op | no-op | no-op | no-op (NA) | −0.5 | not evaluated | cap half |
| SNOW | **−1** | no-op | **−1** | no-op | no-op | no-op | −0.5 | **−1** | cap half |
| MDB | **−1** | no-op | **−1** | no-op | no-op | **−1** | −0.5 | not evaluated | cap half |
| LULU | **−1** | no-op | **−1** | no-op | no-op | **−1** | −0.5 | not evaluated | cap half |
| MDT | **−1** | no-op | **−1** | no-op | no-op | no-op | −0.5 | not evaluated | cap half |
| IWM | **−1** | no-op | no-op | no-op | no-op | no-op (NA) | **−1** | not evaluated | cap half |
| PANW | **−1** | no-op | **−1** | no-op | no-op | no-op (NA) | **−1** | not evaluated | cap half |

Three gates ran on **defective substrate** and are recorded as non-informative rather than banked as passed checks: `front_end_iv_ratio` fired 5-of-5 (100% population rate — earnings humps, not panic; applied mechanically per C24, which says never loosen a gate on thin data); `sector-flow-persistence` returned INFLOW/1.0 on 11-of-11 sectors (making the adverse-rotation condition **structurally unfireable in either direction**); `sector_breakdown` returned `{"Unknown": 8}` (discarded).

### Conviction scoring rubric (Step 4, verbatim — rubric_version `2026-06-12`, FROZEN)

```
Daily conviction score = Σ:
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna-squeeze in trade direction —
      must be a verified SIGN CHANGE, not a level: sign(net_dex) on the latest session opposite to ≥3
      consecutive prior sessions, |net_dex| on the flip day ≥ 0.25× the trailing-10-session median.
      Computed by scripts/dex_flip.py — never by hand.
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified
      institutional-tier confirmed) — C11 CONJUNCTION: full +3 only when cum_premium_flow_30d confirms
      (sign aligned AND |cum_flow_30d| ≥ $50M); else halved to +1.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: only when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +1  uw historical cumulative-premium-flow net directional accretion (30d) — INTENT-SCREENED:
      (a) no C28 distribution_flag on the name, AND (b) not deep-ITM sub-parity dividend-capture.
  +1  sector-rotation-strategist names ticker as single-name leader — CONDITIONAL on
      (a) sector persistence_score ≥ 0.6 AND (b) cum_flow_30d aligned AND (c) |cum_flow_30d| ≥ $50M.
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising pc-ratio-zscore (VRP positive) —
      an INFORMED-FLOW CONTINUATION penalty, not a "fade the crowd" signal.
  -3  flow_conflict — cum_premium_flow 30d direction clearly opposite dominant_signal_class
  -1  flow_conflict_lite — 30d cum_premium_flow read is MIXED
      (the -3 and -1 are MUTUALLY EXCLUSIVE — apply ONE, never both)
  # TIER GATES applied by risk-monitor in 2d — contribute 0 to raw_score, never appear in score_components:
  -1  [TIER GATE] correlation cluster (pairwise corr ≥ 0.70) — −1 TIER
  -3  [TIER GATE] market-regime conflicts with trade direction — −1 TIER
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | HIGH | full (subject to the Step 3a load-bearing gate + win-rate gate) |
| 7–8 | MEDIUM | half |
| 3–6 | LOW | starter / watch-only |
| ≤ 2 | **drop** | filtered by the quant's drop floor |

*Tier-cut status: the ≥9 HIGH cut failed its scheduled re-confirmation on 2026-06-12 and is retained under the freeze without a validated ranking claim. The 2026-08-30 audit records a **tenth consecutive cycle with zero decided HIGH and zero decided MEDIUM post-freeze** — 546 resolved rows without a single gradeable HIGH. The P0.6 out-of-regime guard caps all sizing at half in the interim.*

*The Step 3a HIGH-tier load-bearing-tool gate (3-of-4 among `dark-pool block-stratified`, `cumulative-premium-flow`, `institutional-accumulation`, `dex`) **never had to run today** — no name came within 7 points of the ≥9 cut. Recorded so the skip is not read as an omission.*

---

## 8. Watch-only — single signal, no confluence

Surfaced by exactly one Phase 1 agent; **excluded from the rubric**. Listed for journaling, not entry.

| Ticker | Flagging agent | Signal | Why it failed confluence |
|---|---|---|---|
| **AMD** | vol-surface-scout | BUY VOL — VRP −0.2517, IV30 48.2% vs RV30 73.4% (−25.2pp), KINKED dte=4 | Single agent. Kink prominence 5.8% barely clears the 5.0% threshold; AMD is a sector-rotation **laggard** (−$8.1M) and sweep-tracker has it Tier-2 **bearish** 4/5 |
| **MSFT** | sweep-tracker | The only name where 4/5 sweep persistence, cum_flow_30d (+$782.8M) and the mega-cap hedge filter all agree | Single agent, and sweep-persistence earns **0 rubric points** by construction (removed 2026-05-23 P0.3). Also failed the LEAP decay falsifier badly (90d +$427.6M < 30d +$782.8M) |
| LITE, COIN, PLTR, SNDK, CRWD, APP | sector-rotation-strategist | Named Tech single-name leaders | Single agent each |
| **GLD** | multileg-strategist | 330P/335P Jan-2027 vertical, ~50,100 lots | Direction **unresolved** (no `side` tag). Contrarian flagged z=2.715 then **disqualified** it — price/flow aligned, closing is call-side profit-taking |
| **PCG** | multileg-strategist | Two candidate bullish call builds; genuine BACKWARDATION with thick tenors | Strikes don't pair (17 vs 17.5); no confirmed calendar leg. Flagged as a watch item for the vol lanes |
| **QQQ** | multileg-strategist | 715P/740C Dec-31 collar, 38,000 lots, $20.9M net debit | An **event hedge, not directional alpha**; `repeat_count: 1` fails the repeat filter |

**Energy refiners (VLO, MPC, DINO, SLB, DK)** — surfaced via the `fz` new-high lane and XLE +2.04%, but deliberately **not** carried as candidates: the multi-day options tape contradicts the price move (XOP −$12.28M outflow, XLE 5d flat), and Energy has no netted direction available. Appendix only.

**C12 liquidity floor:** 81 names passed; **6 failed** and were dropped fail-closed — `^VIX` (index, no share volume — expected), GPRE ($22.8M ADV), SHOO ($40.7M), KBH ($45.7M), STDN ($10.2M), CVI ($33.4M). Note CVI and STDN both appeared on the `fz` new-high lane and were removed by the floor.

---

## Appendix — substrate defects observed this session

Recorded so the next `/calibration-audit` can grade them; none were patched (rubric frozen).

1. **GEX `regime` label contradicts its own `total_gex` sign** — fired on SPY today and on 08-19, 08-24, 08-25, 08-26 (5 of ~15 sessions, worse than the documented 3-of-4 baseline). QQQ decouples less often (08-18, 08-20). Both indices' ZGLs extrapolated to nonsense (305.49, 212.59).
2. **`oi-trend BUILDING` fired 6-of-6 and 5-of-5 = 100%** across two independent agents. Zero discrimination, reconfirmed twice.
3. **`front-end-iv-ratio` fired 5-of-5 = 100%** of the earnings population at `--near-dte 7`.
4. **`sector-flow-persistence` returned INFLOW / 1.0 on 11-of-11 sectors** — gross turnover, sign-agnostic, structurally unfireable as an adverse-rotation gate in either direction.
5. **`iv_outliers` 100% contaminated** — all 20 cached rows on the 0DTE expiry.
6. **`iv-percentile-zscore` short-delivered** — `dates_used = 98` vs a 120-day floor. All percentiles provisional.
7. **`analyst-vs-flow` has no analyst leg** — 0 of 5 rows carried one. Reconfirmed.
8. **`portfolio-correlation.sector_breakdown`** returned `{"Unknown": 8}` plus a spurious 100%-concentration warning.
9. **`fz screen` doubled-first-letter ticker bug** on every bulk surface (SSLB→SLB, VVLO→VLO, CCRWD→CRWD, DDINO→DINO, CCVI→CVI, DDK→DK, AABEO, AACHC…). Per-ticker `fz_enrich` is healthy. `fz` analyst axis (`recom`/`upside_to_target_pct`) null on all five enriched names — upstream quote-parser gap.
10. **Month-end dark-pool contamination, two stacked mechanisms** — closing-cross top-bucket shares of 69.8% (NVDA), 61.7% (MU), 58.3% (WMT), 53.4% (AAPL), 37.5% (META), **plus a confirmed basket/program print at 20:55:04Z**: MSFT $500,000,242.70 / GOOG $500,000,047.33 / NVDA $500,000,024.44 — identical ~$500M notionals to the dollar, with GOOGL $499,999,986.75 one minute earlier alongside SNDK $427.5M and CVX $307.4M.
11. **`signal-backtest` supports only 5 classes** — `vol_term_dislocation`, `earnings_vol` and `dealer_positioning` are not among them, so **7 of 8 names today are structurally unmeasurable** (`NA(substrate)`). That is correct terminal behaviour, not a data failure; no proxy was substituted.
12. **Debate gate direction-inversion** — `bear_residual ≥ bull_residual ⇒ −1 tier` is written in long-oriented framing and inverts on non-long calls. Handled by direction-adjusting at prompt construction; still not mechanized.
