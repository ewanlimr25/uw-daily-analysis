# Daily Market Analysis — 2026-06-25

## Executive Summary
- **Regime + GEX state:** **TRANSITIONAL / PULLBACK_IN_UPTREND** — SPY 734.30 (below 20SMA 744.88, above 50SMA 733.77; −2.17% 30d, −3.43% from 90d high). SPY **and** QQQ dealer books both **FULLY_NEGATIVE / short-gamma** (held 4 sessions). VIX 18.89. Breadth split: price tape green (60.6% advancers) **vs** options positioning bearish (35.4% bullish flow) — a distribution-into-strength tell. Sector signal conflicted (Tech tape-strength, no clean rotation).
- **Rubric regime status:** **OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half.** The rubric was fitted in the UPTREND that ended 2026-06-12; 0 of 30 post-freeze calls are resolved, so the P0.6 guard caps every conviction-tier size at half regardless of win-rate.
- **Next-session GEX (SPY/QQQ):** **SPY** short-gamma, ZGL null, no real call wall, put-wall *acceleration* zone 730/725 → debit-vertical/directional bias, not a pin. **QQQ** short-gamma, ZGL null, knife-edge at 717 (−$230M) / 718 (+$84M), downside air-pocket 705/700 → half-size (front-end backwardation, 0DTE IV 1.73× VIX). Advisory — see §2.
- **Top swing build:** **None at conviction.** The only sized position is a **MU starter (long)** — beta-flagged (market-excess −9.3pp), debate-cut from half. Everything else floors to watch-only.
- **Top LEAP candidate:** **None.** LEAP tape thin (5.2% DTE share) and low-quality — macro-hedging, financing (TLT complex), and distribution dressed as call-OI builds (BSX/WFC). Zero passes.
- **Biggest risk:** semis correlation cluster **{MU, SNDK, AMAT} corr 0.78–0.82** (MU the only sized member); short-gamma books into the **Jul-2 NFP** Tier-1 print. Hedge sleeve: **defined-risk SPY put spread into NFP; no naked vol** (VRP FAIR).

> **Desk bottom line: NO HIGH-CONVICTION TRADES.** Out-of-regime half-cap + debate gate firing on **5 of 5** top names + fundamentals CAUTION on META/NVDA/NKE collapses the entire short book to watch-only. Carry the watch-only book, hold a defined-risk SPY put spread into NFP, do not chase. A "no-edge" day is a valid output — the gate stack correctly refused to manufacture conviction.

---

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity"; trend **PULLBACK_IN_UPTREND**. Breadth: 2,210 bullish / 4,026 bearish flow tickers (35.4% bullish). Trading guidance: half size, defined-risk, iron condors in range.
- **Per-index gamma (current-state EOD book):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 734.16 | null (unreliable) | −1.215B | FULLY_NEGATIVE | none (degraded) | 730 / 725 (acceleration) |
| QQQ | 716.29 | null (unreliable) | −397M | FULLY_NEGATIVE | 718 (+84M) | 717 (−230M) → 705/700 |
| IWM | 298.91 | ~322 (noisy) | +28M | borderline/neutral | — | — |

- **`uw options-flow dte-volume-share`:** 0DTE 30.4% / weeklies 36.5% / monthlies 16.5% / LEAPs 5.2% — regime_hint BALANCED (not retail-dominated; not institutional-positioning either).
- **`uw historical vrp` (SPY):** FAIR (+0.0142; IV30 16.4% vs realised 15.0%) — no directional VRP edge.
- **Macro backdrop (`fred_macro`):** yield curve normal (+0.31); core CPI 2.96% / core PCE 3.41% YoY (sticky, above target); unemployment 4.3%, payrolls +172k; 10Y 4.41% (falling −0.15/30d); USD strengthening; fed funds 3.63%. **Forward event_risk:** **Jul-2 (Thu) JUNE NFP — Tier-1 HIGH** (market closed Fri Jul-3); Jul-1 ISM Mfg + JOLTS; Jul-6 ISM Svcs; Jul-9 FOMC minutes. (May PCE released today; next PCE Jul-30, outside window.)

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal — prose-only, 0 rubric points, no backtested predictive claim.** EOD dealer-gamma book read forward as the prior for the next open. Scope: SPY & QQQ only.

Both indices closed **FULLY_NEGATIVE / short-gamma**, held 4 straight sessions (a *held* regime, not a fresh flip). Dealers hedge pro-cyclically — sell weakness, buy strength — which **amplifies** moves and expands realized range. This is the trend/breakout prior, not the pin prior; the "walls" are acceleration/air-pocket zones, not support.

- **SPY** — spot 734.16, ZGL null (`zgl_reliable=false`), total_gex −1.215B. No meaningful +GEX call wall above; dense negative field overhead (734/735). Put-side acceleration 730 (−129M) → 725 (−122M). **Structure bias:** debit verticals / directional 0DTE in the move's direction; a break of 730 runs to 725. Avoid selling a pin that isn't there. If the §2a sell-premium GO is taken, treat as a tight vol-richness fade and respect 730/725 as run zones.
- **QQQ** — spot 716.29, ZGL null, total_gex −397M (≈3× shallower than SPY). Knife-edge: 717 (−$230M, dominant) flips to 718 (+$84M) across one strike; downside air-pocket 705/700. **Structure bias:** directional 0DTE / debit verticals, **half size** per front-end backwardation (0DTE IV 1.73× VIX); skew downside given 717-down asymmetry.

**Mandatory caveats:** EOD is a *prior*, not a target (re-computed by fresh 0DTE OI in the first 30–60 min). ZGL null in FULLY_NEGATIVE → read off total_gex sign + spot-vs-wall. **Gap risk:** Jul-2 NFP within horizon; short-gamma *amplifies* an overnight gap rather than dampening it. ETF book, not SPX/NDX. Cannot isolate the D+1 expiry (0–45d aggregate proxy).

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — validated stack)
Advisory, **0 rubric points**, delta-neutral, NOT a guaranteed edge (validation sample has no vol shock → short-vol left tail UNSAMPLED). Verdict: **GO_PREMIUM_SELL_INTRADAY** both indices — but the §2 short-gamma book is a desk overlay to size down.

| Index | Sell prem | Vol state | VIX | Implied move | Exp range | Size scalar | Structure | Net/day (gross) | Win |
|---|---|---|---|---|---|---|---|---|---|
| SPY | yes | HIGH | 18.89 | 1.15% | 1.2% | 1.5 | wider IC, wings ≈ ±1.2% | **+0.213%** (gross +0.313%) | 94.2% |
| QQQ | yes | HIGH | 18.89 | 2.06% | 1.91% | 0.75 | wider IC, wings ≈ ±1.91% | **+0.321%** (gross +0.421%) | 90.4% |

PnL basis: % of underlying spot notional, GROSS of cost; lead with the **net** figure (round-trip cost 0.1% assumed). **QQQ caution:** front-end backwardation (0DTE IV 1.73× VIX) → half size. **Desk overlay:** both sit inside a FULLY_NEGATIVE short-gamma book into NFP-week — size down / stand aside; enter at/after the open once the gap resolves, hold to close, never overnight. Promotion bar (P1.8): stays advisory permanently until a vol-shock day enters the sample AND net expectancy clears a tail-aware bar.

## 2b. Swing Dealer Positioning (1–4 weeks)
- **SPY — verified MECHANIZED DEX flip POSITIVE→NEGATIVE on 6/22** (6/18 +5.16B → 6/22 −10.09B; ≥3 prior positive sessions; |flip| 0.36× trailing-10 median, clears the 0.25× floor; multi-strike, not an artifact). GEX regime flipped FULLY_NEGATIVE the same day. **But 3 sessions stale** → confirmation of an in-progress de-risk, *not* a fresh entry trigger ("flips precede price" remains practitioner hypothesis). **swing_bias SHORT/de-risk.**
- **QQQ** — DEX flip does **not** qualify (prior positive run only 2 sessions; fails the ≥3 sign-run test). swing_bias SHORT (lower conviction / beta to mega-cap flow).
- **IWM** — DEX whipsaws around zero; **NEUTRAL**.
- **No vanna squeeze anywhere** — SPY/QQQ books are put-heavy (squeeze-capable) but **VIX is RISING** (17.28 → 18.89 over 3 sessions): "vanna pressure, not squeeze." Charm negative on both (weekend decay leans bearish).

## 2c. Sector Rotation
- **`rotation_regime: no_change` (low confidence).** GICS persistence is non-discriminating today — 10 of 11 sectors print persistence 1.0 (all INFLOW); only **Consumer Cyclical is ROTATING (0.6, −$806M today)**, the lone outflow. No canonical defensive/cyclical/growth/value pattern.
- **Signal conflict (carry forward):** options-flow sector signal (Tech +$3.68B 1-day) **conflicts** with the daily-synthesis DP-based metric (Tech/Comm-Svcs/Industrials *outflow*). Treat the whole sector read as low-conviction.
- **Single-name leaders (conditional +1 gate PASS):** Tech leaders **MU (+$1.12B 30d), SNDK (+$972M), MRVL (+$194M), AMAT (+$80M)** clear persistence≥0.6 + cum-flow-aligned + ≥$50M. **NVDA (−$484M 30d) and AVGO FAIL.** AMZN is the cleanest Consumer-Cyclical short (−$352M 30d).

**ETF flow tape (advisory — 0 rubric points)**

| ETF | Net prem dir | Persistence | DP positioning | Options urgency | GICS agreement | Leaders |
|---|---|---|---|---|---|---|
| SMH | inflow (+$144M, #1) | strong/bullish | $62M/$35M/$22M blocks (hedging tell) | net bullish (+$50.6M) | agree (→Tech) | MU, SNDK, MRVL, AMAT |
| IGV | inflow (+$12.3M) | moderate | $82M block (hedge) | balanced | agree (→Tech) | confirms SMH |
| GDX | inflow (+$34.9M) but mixed | conflicted | $23.6M/$15M prints | net BEARISH (put-ask) | n/a (Materials, noise) | downgraded |

SMH is the single cleanest instrument-level signal (GICS + ETF options + sweeps + persistence all agree) — but with no sector rotating *out* against Tech, it is tape-confirmation, **not a rotation trade**. ETF DP is a positioning tell (creation/redemption & hedging), not single-name accumulation.

## 3. Swing Setups (1–6 weeks)
**Invalidation discipline (C34):** anchored to real dark-pool shelves where available.

### 3a. Long swings (regime-aligned)
| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **MU** | 3 (LOW) | Memory super-cycle validated in real time — Jun-24 blowout +15.7% (1048→1213), $50B next-Q guide, $100B contracts; sector-leader (+$1.12B 30d) + long-gamma vol. **But market-excess −9.3pp = beta, not alpha; extended at 52w high (RSI 64.5).** | Small starter long on a pullback, NOT chasing the top tick | Loses the **$1,200 / $1,206 DP shelf** (then $1,150) | **starter** (half → debate −1; beta-flagged; out-of-regime cap) |

No other long cleared. **SNDK / SMH "bullish" net-premium labels are FALSE-BULLISH** — the actual 5-day OI builds are **put-led** (SNDK 1500P/1420P/1750P; SMH 560P/590P), i.e. semis hedging/distribution, not accumulation. **AMAT** is a closest-miss (real mega-tier 0.754 buy + 5d OI BUILDING) but the conviction-matrix confidence is 12.8 (<50) and it's +53% in 30d (late chase) — watch-only.

### 3b. Short / fade swings (defined risk only — all WATCH-ONLY today)
| Ticker | Thesis | Why watch-only | Invalidation |
|---|---|---|---|
| **META** | Cleanest short: DP **distribution** (mega-tier 0.0 buy ratio = pure selling $1.01B/20 trades) + 4/5 bearish put sweeps + Tier-1 FLOOR_PUT 600P; bearish_flow **+17.0pp market-excess**; DEX −$4.56B. 4 straight down days (562→543). | Fundamentals CAUTION (4/4 beats, +26% rev, strong margins — a strong company being *hedged*; RSI 34 oversold; sell-side recom 1.26, +51% target). Debate tie 0.55/0.55. **Both gates fire → watch-only.** | Reclaims the **$544–546 DP shelf** / back above 557.67 |
| **NVDA** | bearish_flow +17pp class edge; mega-selling 0.113 buy ratio; 30d −$484M. | **Hedge-diluted** (top bearish print is a Dec-2027 LEAP = portfolio insurance, not directional). Best fundamentals in book; MU read-through is a *bullish* catalyst. Debate anti 0.65 > pro 0.55. Weakest short. | DEX flips positive / reclaims 200d-relative strength |
| **IWM** | Multileg bearish put structure (Jul-17 287P/283P, repeat ×2 days) into NFP; small-caps most rate-sensitive into sticky-PCE/hawkish-Fed. | Single-agent flag; counter-trend at 52w high (+15.3% above 200d, RSI 62, AAII bull 44.9%); soft-NFP squeeze risk. Defined-risk only. | NFP prints soft/Goldilocks → cover |

**Sweeps (informational, 0 points):** the persistence book is overwhelmingly **bearish/hedge** and index/mega-cap dominated (SPXW/SPY/QQQ/IWM + MSFT/NVDA/TSLA/META/INTC puts, 5-of-5 persistence) — read as protection bought into NFP, not directional conviction. The one clean *bullish* opening build was an uncertain small-cap name surfaced by sweeps alone (single-agent, 0 points → watch).

## 4. LEAP Builds (6–24 months)
**No qualifying LEAP candidates.** DTE>180 share is 5.2% (thin) and today's long-dated tape is macro/rate-hedging (TLT C105 paired against sold C120 + HYG/KRE put complex = financing, not conviction) and **distribution dressed as call-OI builds**: BSX C60 270115 (+15k OI but DP buy_ratio 0.141, $89M sold on the bid, inst-accum DISTRIBUTION, −16.7% 30d), WFC C97.5 (DP 0.312 distribution). Every name fails the conviction-matrix >70 DIRECTIONAL_LONG gate and/or the 90d slow-accretion gate. No conviction-matrix +1 awarded.

## 5. Volatility Surface
- **Best vol trade: CNXC SELL-VOL into earnings** (6/29 AMC) — front-rich backwardation + **VRP +0.52** (vol genuinely rich vs realised) + ivr100 + 4-day binary. Watch-only (earnings-scout SKIP'd it on a no-clean-event-expiry / structure-hygiene basis; vol-surface flags it as the standout). Size to the 17.4% implied move, defined-risk.
- **NKE SELL-VOL (6/30 AMC, half-size) — see §6/§7.** Clean 07-02 IV kink (86% vs 63% back-month) but flat back-month skew + bearish flow + a 5-day binary → defined-risk only.
- **Event-free premium sells (positive VRP):** WDC +0.084, TXN +0.083, INTC +0.073, ICE +0.064 — genuinely-rich, no-catalyst names → 30–45 DTE iron condor inside the 1σ move.
- **Stand aside despite IV-rank 100:** SMH / AMAT / LRCX / TSM / STM / MCHP / AMD — VRP-FAIR (−0.02 to +0.04). High IV-rank ≠ rich; the SMH put-heavy PCR 3.05 is paid-for protection, not a premium-selling gift.
- **BUY-VOL (negative VRP):** **MU −0.31**, GLW −0.10 — vol cheap vs realised; own gamma / calendar, do **not** sell.
- *Substrate caveats:* all term-structure labels were degenerate (1-DTE front leg) and reclassified off hygiene-filtered curves; all IV percentiles are n=52 provisional (not 252-day).

## 6. Risk & Correlation
- **Macro headline:** sticky core PCE 3.41% YoY + hawkish-Fed/USD-strengthening backdrop into **Jul-2 NFP (Tier-1)**; NKE earnings 6/30 (T+3) is the one named in-horizon binary.
- **Correlation clusters (`uw risk portfolio-correlation`):** **`semis_cluster` {MU, SNDK, AMAT} corr 0.778–0.823** (≥0.70 → treat as one position) — MU is the only *sized* member, so no cluster penalty bites. Soft-watch (0.60–0.70): META/AMZN, IWM/AMAT, NKE/AMZN, NVDA/IWM, MU/IWM — the whole book is one big-cap-tech/semis/risk-beta complex, but only one sized name per direction.
- **Gates applied:** rubric_regime FIRES on all (out-of-regime → cap half). Debate gate FIRES 5/5. Fundamentals CAUTION on META/NVDA/NKE. VRP FAIR → no vol-sizing edge either way. Panic does **not** fire (front-end ratio elevated on QQQ only, not >1.10 market-wide).
- **Fundamentals verdicts (top-5):** META CAUTION (−1, strong co being hedged), NVDA CAUTION (−1, hedge-diluted short), **MU CONFIRM (0, blowout validated)**, NKE CAUTION (−1, earnings T+3 gap risk), IWM NA (0, ETF). **No VETOs.**
- **Adverse-flow exits (carried `conviction_2026-06-24`: BJ, SMH, IREN):** no hard exit — all three flow-on-thesis. **SMH soft-watch** (net flow still +$32.7M long but PCR 3.05 + IVR 93.8 put-build).
- **Breadth cross-check (advisory):** advancers 305 / decliners 198, pct_green 60.64 — green price tape, **no <50 divergence flag**, but green price vs 35.4% bullish options flow is a distribution-into-strength tell (worst mover AAPL −6.12%; top SNDK +21.97%).
- **Hedge sleeve:** book is near-flat (one beta-long MU starter; shorts all watch-only). Regime-appropriate sleeve: a small **defined-risk SPY July put vertical (~1–2% OTM, expiring just past 07-02)** as NFP insurance, ~10–15% of nominal. **No naked vol either direction** (FAIR VRP gives no cheap-vol tailwind).

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**None.** No name reached MEDIUM (≥7) or HIGH (≥9). Max raw_score today was **MU at 3 (LOW)**. The full scored/watch book:

**Expectancy lens (advisory — C31; `[advisory — expectancy is not yet a live sizing axis]`):** the most recent `/calibration-audit` (2026-06-20) recorded a **persistent tier inversion** (HIGH realized ~0.143, below MED/LOW), a long edge **real-but-decaying** (67%→38% across eras), and a **negative-edge short book** (−22.7pp vs same-window SPY short). Net: the book's realized edge is thin and not tier-monotone — display-only context, the live sizer remains the win-rate ladder (today, half-capped). This reinforces standing aside on a no-edge day.

| Ticker | Dir | raw | dominant class | win_rate (n, src) | mkt_excess | pre-risk | fundamentals | debate (pro/anti) | gates fired | final | invalidation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MU | long | 3 | sector_rotation | 0.5357 (140, clean) | −9.3pp (beta) | half | CONFIRM | 0.65 / 0.65 | rubric_regime, debate | **starter** | $1,200/$1,206 DP shelf |
| NKE | vol_short | 2 | earnings_vol | NA(substrate) | — | half | CAUTION | 0.55 / 0.55 | rubric_regime, fundamentals, event_risk, debate | watch-only | IV holds >70% pre-print / back-month skew flips +; defined-risk only |
| META | short | 1 | bearish_flow | 0.5037 (135, clean) | +17.0pp | half | CAUTION | 0.55 / 0.55 | rubric_regime, fundamentals, debate | watch-only | reclaims $544–546 DP shelf |
| NVDA | short | 1 | bearish_flow | 0.5037 (135, clean) | +17.0pp (hedge-diluted) | half | CAUTION | 0.55 / 0.65 | rubric_regime, fundamentals, debate | watch-only | reclaims 200d-rel strength / MU-demand follow-through |
| IWM | short | 2 | bearish_flow (index) | NA | — | half | NA | 0.55 / 0.65 | rubric_regime, event_risk, debate | watch-only | soft/Goldilocks NFP → cover |

*MU is the only sized name (a beta-flagged starter). The two cleanest directional shorts (META, NVDA) carry the only positive market-excess (+17pp) but are floored to watch-only by the fundamentals + debate gates — the edge is in the class excess, not the additive points.*

### Conviction-scoring rubric (Step 4, frozen `2026-06-12`) — embedded for audit
```
Daily conviction score = Σ:
  +1  dealer-positioning MECHANIZED DEX flip / vanna-squeeze in trade direction (verified sign change, not level)
  +3  3+ aligned accumulation signals (DP + OI + smart-positioning, block-stratified institutional) — CONJUNCTION: full +3 only when cum_flow_30d confirms (aligned AND |≥$50M| AND ≥5% of gross); else halved to +1
  +1  multi-day OI build (oi-trend BUILDING, ≥5 days)
  +1  conviction-matrix DIRECTIONAL_LONG >70 — CONDITIONAL: leap_directional only
  +1  cum_premium_flow net directional accretion (30d) — intent-screened (no distribution_flag; not ex-div sub-parity calls)
  +1  sector-rotation single-name leader — CONDITIONAL: persistence≥0.6 AND cum_flow aligned AND |≥$50M|
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg directional structure (term-structure-anchored)
  +1  vol-surface KINKED/BACKWARDATION with VRP-aligned bias
  +1  opex-pin-strategist top-5 (OPEX week only)
  -2  contrarian overcrowded long + rising pc-ratio-zscore (informed-flow continuation penalty)
  -3  flow_conflict (cum_flow_30d clearly opposite dominant class)  |  -1  flow_conflict_lite (MIXED/bottom-quartile)
  [TIER GATES, applied by risk-monitor, 0 points]: -1 tier correlation cluster; -1 tier regime conflict
Tiers: ≥9 HIGH (full) · 7-8 MEDIUM (half) · 3-6 LOW (starter/watch) · ≤2 drop.
Out-of-regime guard (P0.6): all conviction sizing capped at half until ≥30 resolved post-2026-06-12 calls re-validate tiers.
```

## 8. Watch-only — single signal, no confluence
For journaling, NOT trade entry today:
- **SNDK** (long) — sector-rotation leader (+$972M) but sweep + accumulation flag **put-led distribution** (conflicting flags → fails clean confluence).
- **MRVL** (long) — sector-rotation leader (+$194M) only; single agent.
- **AMAT** (long) — sector-rotation leader (+$80M) + real mega-tier 0.754 DP buy + 5d OI BUILDING, but conviction-matrix confidence 12.8 (<50), +53% 30d late chase; IVR 100 distribution-flavored.
- **MSFT** (short) — sweep 5/5 bearish + Tier-1 floor put 390P (advisory); #1 bearish net-premium (−$179M) but accumulation NOT confirmed (mega 0.458 balanced).
- **AMZN** (short) — Consumer-Cyclical rotation-out leader (−$352M 30d); sweep 5/5 but MIXED (disqualified).
- **CNXC** (vol) — vol-surface SELL-VOL standout (VRP +0.52, 6/29 earnings) but earnings-scout SKIP'd on expiry-grid structure.
- **TSLA / AAPL** — Tier-1 floor puts but internally conflicted (TSLA bullish aggregate flow vs the put; AAPL DP net-buying despite −6.12% / the 305P block).

---
*Single-leg whale (advisory C19, 0 points): 4 scored Tier-1 FLOOR_PUT_BLOCK (bearish, WR 61%, +23.5pp vs SPY) — AAPL 305P, MSFT 390P, META 600P, TSLA 415P (deep-ITM DTE-1 ask-side floor blocks). META's is the only one with confirmed DP distribution behind it.*
