# Daily Market Analysis — 2026-07-08

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL (trend UPTREND; "reduce size, defined-risk"). SPY 745.40 above 20/50 SMA but **breadth strongly divergent — only 22.3% of S&P names green, 391 decliners vs 112 advancers, avg −1.1%.** VIX 16.9 (LOW). Both SPY (FULLY_NEGATIVE, total_gex −1.18B) and QQQ books are short-gamma. Sector lean: Tech net +$2.84B (mega-cap/semi-led, narrow).
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`. (Moot today — the entire book floors to SKIP / watch-only before the cap binds.)
- **Next-session GEX (SPY/QQQ):** SPY — short-gamma, ZGL null/unreliable, put wall 740 / call wall 760, walls wide → favor debit/long-straddle 0DTE over premium-selling. QQQ — regime-label anomaly (POSITIVE label vs −372.6M total_gex), treat short-gamma-leaning, put wall 700 / call wall 730. Advisory, see §2.
- **Top swing build:** *None.* The only scored directional call — **SPY SHORT (raw 3, LOW, +14.9pp measured market-excess)** — gates to **SKIP** on the regime + debate + CPI-event stack. If expressed at all, defined-risk put spread only.
- **Top LEAP candidate:** *None.* LEAP board empty (no name clears 6-of-9 gates in a narrow tape).
- **Biggest risk:** A narrow, breadth-divergent (22% green) tape sitting on a fully-negative-gamma dealer book with a fresh SPY DEX flip to short and CPI (07-14, T+4) two-sided into it. Short-gamma + low-VIX complacency = classic air-pocket setup — but a dovish CPI squeezes shorts just as violently. **No edge sized today.**

> **No-edge day.** No name cleared the confluence gate into a sizeable tier. The dominant, corroborated signal is index-level bearish/hedging, not a single-name trade. Report §3/§4 are intentionally near-empty; §1/§2 (regime + next-session GEX advisory) stand.

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity" (trading guidance: half size, defined-risk, iron condors in range). Trend flag UPTREND. SPY 745.40 (above 20SMA 741.6 / 50SMA 739.64, +1.06% 30d, −1.97% from 90d high). Flow breadth 32.6% bullish (2043 bull vs 4216 bear tickers).
- **Breadth cross-check (`fz`, advisory):** 112 advancers / 391 decliners, **pct_green 22.3%**, avg −1.1%, median −1.26%. **DIVERGENCE FLAG** — index green under a broadly red tape. Distribution underneath a mega-cap/semi-led top. Does not change sizing; frames every long as suspect.

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 744.98 | null (unreliable) | −$1.18B | FULLY_NEGATIVE | 760 | 740 |
| QQQ | 710.25 | null (garbage 300.24) | −$372.6M | POSITIVE* (anomaly) | 730 | 700 |
| IWM | 293.19 | null (garbage 194.16) | negative | label unreliable | — | — |

\*QQQ regime label reads POSITIVE while total_gex is negative — tool anomaly, treat short-gamma-leaning. This is the **current-state** EOD book; §2 reads it forward for the next session.

- **`uw options-flow dte-volume-share`:** 0DTE 39.6% / weeklies 22.8% / monthlies 25.7% / LEAPs 4.5% — BALANCED, mildly retail-tilted.
- **`uw historical vrp` (SPY):** IV30 14.03% vs realized 15.27%, VRP −0.0124 → **FAIR** (realized slightly *above* implied — index premium is not rich; no clean premium-selling edge).
- **Macro backdrop:** Yield curve normal (10y2y +0.35); core CPI 2.96% / core PCE 3.41% YoY (both above target); unemployment 4.2%, payrolls +57k (soft); 10Y 4.55% flat; USD strengthening; fed funds 3.63%. **Forward event risk:** CPI 07-14 (T+4, Tier-1), PPI 07-15 (T+5), Beige Book 07-15, jobless claims 07-16, FOMC 07-28.

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not scored.** EOD dealer-gamma book (OI persists overnight) read forward as the prior for the next open. Prose-only, 0 rubric points, no backtested predictive claim. SPY/QQQ only.

**SPY** — regime **FULLY_NEGATIVE** (total_gex −1.18B), ZGL null/unreliable. Deepest negative pocket sits *at spot* (745 strike, −487.6M). Dealers short gamma across the whole visible range → hedging **amplifies** moves through the pin in either direction (not a mean-revert setup). Put wall **740** (~0.7% below, thin/close); call wall **760** (~2.0% above, far/thin). **Structure bias:** short-gamma with wide asymmetric walls → favor debit verticals / long-straddle-leaning 0DTE over premium selling; a short straddle at 745 is mispriced (dealers chase, not dampen). Book chronically unstable — flipped regime 6 of last 8 sessions.

**QQQ** — **regime-label anomaly**: tool says POSITIVE but total_gex is −372.6M and ZGL (300.24) is garbage (>50% from spot). Treat as short-gamma-leaning in a noisy strike band (700–715 flips strike-to-strike). Put wall **700** (~1.4% below, firm support); call wall **730** (~2.8% above, far/thin, upside uncapped). **Structure bias:** do not trade a clean long-gamma pin off the POSITIVE label; prefer a defined-risk condor bracketing 700–730.

**Mandatory caveats:** EOD is a *prior*, not a target (fresh 0DTE OI re-computes it in the first 30–60 min); ZGL unreliable on both (fall back to total_gex sign + spot-vs-wall); gap risk voids the prior (no scheduled overnight print — CPI is 07-14); uw cannot isolate the D+1 expiry (0–45d proxy, validated by 07-09/07-10 holding dominant expiry share); this is the ETF book, not SPX/NDX.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — the validated stack)
Backtest verdict **GO_PREMIUM_SELL_INTRADAY** (delta-neutral, advisory, 0 rubric points; short-vol left tail UNSAMPLED — no vol shock in the 60-day window).

| Index | Sell premium | Vol state | VIX | Implied move | Exp. range | Size scalar | PnL open (gross / **net**) | Win% |
|---|---|---|---|---|---|---|---|---|
| SPY | yes | LOW | 16.9 | 0.91% | 1.23% | 0.5 | +0.308% / **+0.208%** | 95.0% |
| QQQ | yes | LOW | 16.9 | 1.66% | 1.89% | 0.25 | +0.399% / **+0.299%** | 88.3% |

- **Whether (VRP):** front-expiry implied move systematically exceeds realized next-day open-to-close. **Lead with net** — PnL is % of underlying spot notional, GROSS; net of 0.1% assumed round-trip cost the edge is tiny in absolute terms.
- **How much (GEX):** both short-gamma → wider next-day range → wings out (SPY ±1.23%, QQQ ±1.89%).
- **Size (VIX):** LOW vol state → thin edge → scale down (SPY 0.5, QQQ 0.25).
- **When:** enter at/after the open once the gap resolves; hold to the close; **never carry overnight** (overnight entry backtested negative). Stand aside if it gaps beyond the wings.
- **QQQ caution:** front-end backwardation (0DTE IV 1.56× VIX) — event/gap risk; half size. SPY ≈ SPX (validated identical); QQQ weaker (Nasdaq index book unavailable) — lower confidence.

## 2a. Swing Dealer Positioning (1–4 weeks)
- **SPY — MECHANIZED DEX FLIP CONFIRMED → swing_bias SHORT.** Sign series (06-24→07-08, $B): −28.2, −30.1, −31.8, +7.7, +26.2, +8.1, **+2.0, +30.3, +3.7, −6.6**. Flip: 3 straight positive sessions (07-02/06/07) → sign reversal to −6.56B today; |flip| 6.56B ≥ 4.28B floor (0.25× trailing-10 median 17.12B). Per-strike GEX confirms it's not a single-strike artifact. This is the "dealer hedge flips before price" setup the mandate is built to catch — price still up, dealer flow turned bearish underneath a narrow tape. Feeds the +1 scored line.
- **QQQ — no flip** (whipsaw: prior-3 sessions not same-sign). Front-end IV 1.195 (BACKWARDATION) — already panicked. swing_bias NEUTRAL.
- **IWM — no flip** (continuation, deepening negative DEX −7.46B; front-end 1.238 BACKWARDATION). Lean short but UNSCORED (no sign change).
- **Vanna:** all three index books put-heavy but **no vanna squeeze** — VIX rose 3 sessions (15.6→16.1→16.9), disqualifying the falling-VIX leg. Flagged "vanna pressure, not squeeze" (reinforces bearish direction, not a melt-up).
- **Single names:** SNDK DEX negative all week (corroborates the bearish/whale side of its flow conflict); NVDA +11.9B DEX today (beta level intensification, no flip).

## 2b. Sector Rotation
- **Rotation regime call: `no_change` (low confidence).** GICS 5-day persistence is structurally undifferentiated — 9 of 11 sectors score 1.0, and **every sector is labeled INFLOW** (no outflow side to classify a rotation against). This is the narrow-tape continuation artifact, not rotation.
- **Named single-name leaders:** none clear the 3-gate +1 check (persistence ≥0.6 AND cum_flow_30d aligned AND ≥$50M). NVDA (Tech leader) 30d cum_flow −$152M (misaligned); ASTS/MRNA aligned but sub-$50M; RCL misaligned. **No sector-leader +1 fires.**

**ETF flow tape (advisory)** — instrument layer the GICS aggregates can't see:

| ETF | Net prem dir | Persistence | DP positioning | Options urgency | GICS agreement | Note |
|---|---|---|---|---|---|---|
| XLF | +$19.1M | BULLISH | blocks near mid | **aggressive bull call sweeps** ($10.8M Aug50C, $10.0M Jul50C) | AGREE (Financials) | strongest ETF confirm |
| KRE | +$24.4M | BULLISH | mixed | low | AGREE (Financials) | Financials just misses standout cutoff |
| XLE | +$4.4M | BULLISH | mixed | low | AGREE (Energy, weak) | borderline |
| XLI | −$2.9M | BEARISH | at/above ask | **bearish put sweeps** (Aug 180/185P) | **DISAGREE** → watch-only | GICS Industrials 0.8 INFLOW but ETF bearish |
| XOP | −$1.3M | BEARISH | below mid | small bull | **DISAGREE** (sub-industry) | E&P diverges bearish vs broad Energy |
| EWT | −$4.4M | BEARISH | block well below mid ($15.4M) | thin | n/a | Taiwan-specific, not a semis rotation tell |

- **fz RS energy-refiner cluster** (MPC/VLO/DINO/PBF/DK/CLMT new highs) gets only partial flow confirmation — VLO/MPC are top-of-sector but Energy sits at the cross-sector median and E&P (XOP) is outright bearish. Read as a **name-level refining-crack-spread strength story, not a sector rotation.** Watch, not a call.

## 3. Swing Setups (1–6 weeks)
Ranked by conviction score.

### 3a. Long swings (regime-aligned)
**None sized.** No bullish name cleared the confluence gate into a sizeable tier. The accumulation board is **empty** — see §6. Strongest bullish *watch-only*: **PLTR** (single-agent, §8).

### 3b. Short / fade swings (defined risk only)

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **SPY** | 3 (LOW) | Mechanized DEX flip SHORT under a 22%-green breadth-divergent tape on a fully-negative-gamma book; 5/5 bearish sweep persistence + aligned 30d cum-flow + index-hedging multileg stack. +14.9pp measured edge. | **Defined-risk put debit spread** (e.g. buy 743P / sell 735P, 1–2wk) — never naked. | Reclaims 745 pin with DEX flipping positive ≥3 sessions, or dovish CPI 07-14 squeezes through 750. | **SKIP** — regime −1 + debate −1 + event −0.5 stack floors it. |

**Sweep ledger (§3 context, informational — 0 points):** PLTR (bullish 3/5, cleanest, OI-confirmed opening — but single-agent, §8); AMZN (bearish 4/5, aligned — single-agent, §8); SPXW (bearish 5/5 but deep-ITM call-selling = dealer hedging, not directional). Mega-caps (MU/NVDA/META/AMD/AAPL) all mixed 0DTE churn. **SNDK CONFLICTED** — 5/5 persistence labeled bullish but today's tape genuinely two-sided (see §7/§8).

## 4. LEAP Builds (6–24 months)
**Empty board.** No name clears 6-of-9 gates. Every long-dated OI "top contract" checked (RIVN, RXRX, IBIT, WEN, AAL, AMD, NVDA) is a single-day spike, not multi-day accretion at a fixed strike. IBIT was the only clean bullish 90d cum-flow (+$265M) but failed persistence (Gate 1), institutional-accumulation NEUTRAL (Gate 7), and conviction-matrix MIXED 6.1% (Gate 8). WBD (largest OI-diff +63k) = merger-arb blind spot, excluded. A narrow, bearish-divergent tape is a poor LEAP-initiation environment — an empty board is the honest read.

> **Tool caveat (for /calibration-audit):** `uw historical oi-trend` `consecutive_build_days` is a whole-chain aggregate (returned max 10 for every name regardless of whether the long-dated contract itself was building) — not usable as LEAP Gate-1 evidence without a per-contract trace.

## 5. Volatility Surface
Governing finding: front-tenor `iv-term-structure` is **artifact-contaminated** tonight (all 22 names read bare BACKWARDATION / kink_expiry=null; per-strike avg_iv runs 1.2–3.4× the screener's iv30d because unweighted OTM wings dominate). **Do not size off raw dte2 reads** — CAT (3.36×), CLF (2.69×), AMAT dte9 (2.30×) are severe artifacts. MSFT is the tell: front-end ratio flipped 2.229→0.963 the instant the 0DTE bucket was excluded.

**VRP overrides IV rank** — several IVR-100 names are *not* actually rich:

| Bias | Names |
|---|---|
| **Buy-vol** (IVR-100 but VRP-negative, realized > implied — do NOT fade) | DELL (−0.281), MU (−0.273), GLW (−0.172), ON (−0.132), SMH (−0.057) |
| **Sell-vol** (positive VRP) | BE (+0.444, but crowded pcr 3.44), FTNT (+0.306), NBIS (+0.255), ALAB (+0.174), ANET (+0.122) |

**Earnings-vol (§5 watch, hand-off to earnings-scout):**
- **SELL VOL (kink + tail-hedging back-month, near-full):** JPM (07-14, kink +16.6%, impl 1.31%), WFC (07-14, impl 1.56%), CAG (07-15, strongest tail ratio 1.2, impl 2.62%), MS (07-15, impl 1.93%), TXN (07-22, thin edge). **All four bank prints sit on top of CPI 07-14 / PPI 07-15 — some front-end elevation is compounded macro vol, not pure single-name.**
- **Half-size (front-only kink, flat back-month):** NFLX (07-16), ASML (07-15), NOW (07-22), TSM (07-16 — lean CALENDAR), JNJ (07-15), SMPL (07-09, impl 14%).
- **Best non-event calendar:** **ANET** (z=4.386 highest, clean front-end ratio 1.117, VRP +0.122, no earnings inside 25d) — pending next-session falling-front-end confirmation.
- **SKIP:** GS (front panic 2.283 = thin-book artifact, flat back), BLK (CONTANGO despite print).

> **Tool caveats:** `uw insights analyst-vs-flow` returned no analyst fields for any name (broken yfinance join — flag for audit). `iv-percentile-zscore` returned n=60 (< 120 floor) — all percentiles provisional.

## 6. Risk & Correlation
- **Macro headline:** core CPI 2.96% / core PCE 3.41% still above target; USD strengthening; 10Y flat 4.55%. **Forward:** CPI 07-14 (T+4), PPI 07-15 (T+5) — Tier-1 two-sided prints inside any swing horizon sized today.
- **Breadth divergence:** 22.3% green / 391 decliners vs 112 advancers under a green-index UPTREND label — narrow mega-cap/semi tape masking broad distribution. Advisory; does not change sizing but caps long conviction and corroborates the index short.
- **Correlation clusters:** `SPY_TSM` corr **0.744** fires (cluster) → TSM takes −1 tier (moot, already DROP). No other pair reached the 0.60 soft-watch floor.
- **Gates applied:** panic no-op (front-end ratio 1.036 FLAT); VRP FAIR (no vol bias); regime −1 on all shorts vs the UPTREND label; **P0.6 OUT-OF-REGIME cap at half** (moot, book floors below half).
- **Fundamentals verdicts (top-5):** PLTR **CONFIRM** (4/4 beats, +67.7% rev; earnings 08-03); AMZN **CONFIRM** for the short (2 straight misses, insider selling, $25B bond sale framed as AI-boom warning; earnings 07-30); SNDK **CAUTION** (−1 tier: persistent −100 insider MSPR + China domestic-memory margin threat; earnings 08-12); TSM CONFIRM (low-confidence ADR; earnings 07-16 imminent); SPY NA (index).
- **Event-risk flags:** CPI 07-14 inside SPY/PLTR horizons (defined-risk requirement); TSM own earnings 07-16 (the event play itself); AMZN structure (Jul13 weekly puts) expires before CPI — no exposure.
- **Debate-disconfirmation:** SPY bear 0.65 ≥ bull 0.40 (short side wins but both flag CPI as two-sided → defined-risk, reduced size); PLTR bear 0.65 ≥ bull 0.55 (debate did NOT clear the long).
- **Adverse-flow exits:** `conviction_2026-07-07` group does not exist in the store (cold start) — no prior watchlist to scan.
- **Hedge sleeve:** none warranted — the sized book is empty (no net delta). Standing color: if any long book forms tomorrow, the breadth divergence argues for a cheap SPY/QQQ put-spread overlay over naked long delta.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**No HIGH or MEDIUM tier names today.** The full book is LOW (SPY, gated to SKIP), DROP (TSM), and watch-only. Per-name audit for the scored/substantive names:

**Expectancy lens (advisory — C31):** no realized per-tier expectancy printed — the rolling `conviction_<date>` group is a cold start (no closed calls to compute payoff ratio / expectancy). `[advisory — expectancy is not yet a live sizing axis]`

| Ticker | raw | tier | dominant_class | win_rate (n, src) | pre-risk | fund | debate (bull/bear) | gates | final | invalidation |
|---|---|---|---|---|---|---|---|---|---|---|
| SPY | 3 | LOW | bearish_flow | 0.575 (134, backtest_clean) · excess +14.9pp | starter | NA | 0.40 / 0.65 | regime −1, event −0.5, debate −1, rubric_regime cap-half | **SKIP** | 745 reclaim + DEX flip +3sess / dovish CPI |
| TSM | 1 | DROP | earnings_vol | NA(substrate) | skip | CONFIRM | — | vrp −1, cluster −1 (moot) | **SKIP** | kink dissipates pre-07-16 print |
| PLTR | 0 | watch | bullish_flow | NA (confluence-fail) | — | CONFIRM | 0.55 / 0.65 | debate −1 (moot) | **WATCH** | loses intraday shelf / sweeps flip |
| AMZN | 0 | watch | bearish_flow | NA (confluence-fail) | — | CONFIRM | — | regime −1 (moot) | **WATCH** | cum_flow flips bullish |
| SNDK | 0 | watch | bearish_flow | NA (advisory C19) | — | CAUTION | — | fund −1 (moot) | **WATCH** | conflicted; whale put entry ~1621 underwater |

**SPY** is the only name carrying measured directional edge (+14.9pp over a matched SPY-short benchmark), yet the gate stack — not the score — kills it. This continues the fleet's recent run of near-empty conviction books.

### Conviction-scoring rubric (Step 4, verbatim — FROZEN 2026-06-12)
```
Daily conviction score = Σ:
  +1  dealer-positioning MECHANIZED DEX flip / vanna-squeeze in trade direction (verified SIGN CHANGE, dated)
  +3  3+ aligned accumulation signals (DP + OI + smart-positioning, block-stratified institutional-tier);
      CONJUNCTION — full +3 only when cum_flow_30d confirms (aligned AND |cum_flow_30d| ≥ $50M); else +1
  +1  multi-day OI build (oi-trend BUILDING, --days ≥ 5)
  +1  conviction-matrix DIRECTIONAL_LONG >70 — LEAP context only (else 0)
  +1  cum_premium_flow net directional accretion in trade direction (30d) — intent-screened
  +1  sector-rotation single-name leader — CONDITIONAL (persistence ≥0.6 AND cum_flow aligned AND ≥$50M)
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored)
  +1  vol-surface KINKED/BACKWARDATION with VRP-aligned bias
  +1  opex-pin-strategist top-5 (OPEX week only)
  -2  contrarian overcrowded long with rising pc-ratio-zscore (informed-flow continuation penalty)
  -3  flow_conflict (30d cum_flow clearly opposite dominant class) — mutually exclusive with lite
  -1  flow_conflict_lite (30d cum_flow MIXED) — mutually exclusive with flow_conflict
  [TIER GATES, risk-monitor 2d, not score points]: −1 tier correlation cluster; −1 tier regime conflict
Tiers: ≥9 HIGH (full) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 drop
```

## 8. Watch-only — single signal, no confluence
Candidates from one agent (or conflicted) — for journaling, NOT trade entry today:
- **PLTR** (LONG) — sweep-tracker Tier-A cleanest, OI-confirmed opening call sweeps across the curve, fundamentals CONFIRM. Failed confluence (accumulation-hunter NEUTRAL, no DP confirm); debate did not clear. Re-check if a 2nd signal confirms tomorrow.
- **AMZN** (SHORT) — bearish sweep persistence + fundamentals CONFIRM (2 misses). Single-agent; also in the 13:03Z artifact cluster.
- **SNDK** (CONFLICTED) — Tier-1 OPENING_PUT_PRIME (1770P, $1.24M, size/OI 6.17, C19 advisory short-lean) vs noise-level bullish net-flow headline; multi-strike protective-put ladder reads as post-crash hedging; fundamentals CAUTION. Whale entry ~1621 already underwater vs 1727 close.
- **FTNT** (SELL-VOL / bearish) — vol-surface best sell-vol-into-earnings (VRP +0.306, 07-29); contrarian flagged bearish divergence but disqualified as a fade (backwardation/event).
- **SOC / MARA** (LONG) — multileg bull call spreads, LOW conviction (repeat_count=1, no whale). **UAA** (SHORT) — multileg bear put diagonal, same caveat.
- **§5 vol watch:** JPM / WFC / MS / CAG / TXN (SELL VOL into 07-14/07-15 bank earnings, macro-overlapped); ANET (best calendar candidate).

---

### Data-integrity flags for /calibration-audit
1. **13:03Z stale-NBBO batch-print artifact (NEW, systemic):** a cluster of large DP prints stamped within the same 2-second pre-open window (13:02:59–13:03:01Z) across ≥8 unrelated large-caps (MU/NVDA/QCOM/AAPL/AMZN/GOOGL/KLAC/INTC), each above the contemporaneous NBBO ask — inflated every affected name's institutional-accumulation buy-ratio uniformly. Largely responsible for the semis reading "ACCUMULATION" today. Plus the known 20:00–20:25Z closing-cross twin-print duplicates (MU/NVDA/PLTR/GOOGL). **This appears to be a systemic feed/vendor batch-recovery signature — check whether it recurs at the same clock time.**
2. LRCX watchlist alert ($10.7M DP print) = **false positive** — executes in the 20:00:06Z closing cross, 100% SELL (mega buy_ratio 0).
3. GEV / GLW: bullish net flow but institutional-accumulation reads DISTRIBUTION (mega buy_ratio 0.07 / 0.00) — smart money selling into the "bullish" options print.
4. QQQ/IWM `gex-time-series` regime-label anomaly (POSITIVE label vs negative total_gex; ZGL prints far from spot).
5. `iv-term-structure` 0DTE-bucket contamination (front-end ratio flips FLAT once dte≤0 excluded — MSFT 2.229→0.963). `analyst-vs-flow` broken (no analyst fields). `oi-trend consecutive_build_days` whole-chain aggregate unusable for LEAP Gate-1.
