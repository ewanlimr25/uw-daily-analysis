# Daily Market Analysis — 2026-06-22

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL — PULLBACK_IN_UPTREND. SPY 744.39 (below 20SMA 747.16, above 50SMA 730.95, −2.11% from 90d high); bullish flow only 35.2%. **Both SPY & QQQ flipped FULLY_NEGATIVE (short-gamma) today** — fresh same-day flip from POSITIVE. VIX 17.28, VRP FAIR. Breadth (fz) pct_green 52.88% — no divergence. Defensive rotation (Utilities/RE/Healthcare in; Comm Services/Cyclicals out). Half-size desk guidance.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL/PULLBACK) — sizing capped at half`. The 2026-06-12 freeze + P0.6 half-cap is active (no calibration-audit has cleared ≥30 resolved post-06-12 calls; 2026-06-20 audit recommended KEEP freeze).
- **Next-session GEX (SPY/QQQ):** SPY — FULLY_NEGATIVE, total_gex −1.38B, ZGL null/unreliable, call wall 755 / put wall 745 (spot on the wall) → short-gamma, trend/breakout, vol-expansion prior. QQQ — FULLY_NEGATIVE, total_gex −291M, call wall 750 / put wall 738 → same, shallower book. **Advisory, see §2.** Gappy and fragile into PCE.
- **Top swing build:** *None at conviction.* This is a no-edge directional day. The single scored name is **MU (raw 3, LOW)** — a defined-risk **vol/event play into 06-24 AMC earnings** (implied ±11.2%), sized **starter** only after a fundamentals CAUTION and a debate cut. Not a directional long.
- **Top LEAP candidate:** None. No name cleared the 6-of-9 LEAP gate; NVDA was the cleanest near-miss (ATM C205 $34.8M build) but 90d/30d cum-flow is net **negative** → fails the slow-accretion gate.
- **Biggest risk:** A **memory/semis cluster** (MU·WDC·SNDK·AMAT·INTC·NVDA, pairwise corr ≥0.72) sitting on **IV-rank 100** into a wall of late-June earnings, all inside a short-gamma tape **3 trading days before Core PCE (Thu 06-25)**. One catalyst moves the whole complex. No hedge sleeve required (book is one starter vol play; net delta ~flat).

## 1. Regime & Gamma State
`uw risk market-regime`: **TRANSITIONAL — PULLBACK_IN_UPTREND.** SPY 744.39, below the 20SMA (747.16) but holding the 50SMA (730.95); +0.42% / 30d, −2.11% from the 90d high. Flow breadth is **bearish**: 35.2% bullish (2,203 bullish vs 4,053 bearish tickers of 6,256). Desk guidance: half size, defined-risk, iron condors in range.

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 744.69 | null (unreliable) | −1.38B | **FULLY_NEGATIVE** | 755 | 745 |
| QQQ | 737.61 | null (unreliable) | −291M | **FULLY_NEGATIVE** | 750 | 738 |
| IWM | 298.25 | 322.26 (above spot) | ~0 (flip) | flipped NEGATIVE | — | — |

Both SPY and QQQ flipped to a **net-negative (short-gamma) book today** — dealers now hedge *with* direction (amplify moves), the opposite of the long-gamma pin that held on 06-18. IWM also logged a GEX regime flip (ZGL 322 sits ~24 pts above spot → small-cap downside mechanically amplified).

- **DTE volume share:** 0DTE 36.1% / weeklies 25.1% / monthlies 21.6% / LEAPs 5.0% — `regime_hint BALANCED`. Not retail-0DTE-dominated; no auto-downgrade of swing conviction.
- **VRP:** SPY **FAIR** (IV30 14.78% vs realized 14.58%, +0.21%); QQQ **FAIR** (IV 24.7% vs realized 26.48%, −1.78% — a mild premium-*buy* tilt). No clean vol edge either direction.
- **Macro backdrop** (`fred_macro`): yield curve **normal** (10Y−2Y +0.27); core CPI **2.96%** / core PCE **3.29%** YoY (still sticky-above-target); unemployment 4.3%, payrolls +172k; 10Y **4.46% and falling** (−0.21/30d); USD **strengthening**; fed funds 3.63%. **Forward event risk:** **Core PCE (May) — Thu 2026-06-25 (HIGH, T+3)**, with Initial Jobless Claims and the Q1 GDP third estimate the same morning. June FOMC already passed (06-17, hawkish-hold). Next CPI ~mid-July, next FOMC ~late-July (both outside current horizons).

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, prose-only, 0 rubric points, no backtested predictive claim.** EOD dealer-gamma book read forward as the *prior* for the next open; predictive validation lives in `/weekly-analysis`. SPY/QQQ only.

| Index | Regime · ZGL | Call wall / put wall | One-line structure bias (next-session 0DTE) |
|---|---|---|---|
| **SPY** | FULLY_NEGATIVE · ZGL null (unreliable) | 755 / 745 (spot on the put wall) | **Short-gamma → trend/breakout.** Below 743 accelerates toward the 740/735 shelves; above 748 dealers flip to buying toward 755. Range ~−740 to +755 (~1.4%). Debit verticals / directional 0DTE, NOT a naked short-straddle into a fresh negative book. |
| **QQQ** | FULLY_NEGATIVE · ZGL null (unreliable) | 750 / 738 (spot on the put wall) | **Short-gamma**, shallower (−291M, ~⅕ of SPY). Below 737 accelerates to 732/730; above ~744 turns up toward 750. Range ~−732 to +750 (~1.7%). Directional 0DTE / debit verticals; higher-beta gap vehicle into PCE. |

**Mandatory caveats:** (1) EOD is a **prior, not a target** — first-hour 0DTE OI re-draws the walls; re-read after the open. (2) Both regimes flipped **today** (fresh, unstable). (3) **Gap risk voids the prior** — Core PCE Thu 06-25 can gap spot through the walls; this map is most fragile around the print. (4) ZGL is **null/unreliable** on a FULLY_NEGATIVE book — read derived from `total_gex` sign + spot-vs-wall, `zgl_reliable=false`. (5) ETF book, not the cleaner SPX/NDX index book; D+1 expiry cannot be isolated (0–45d proxy).

### 2a. Next-session 0DTE premium-selling setup (validated stack)
`zerodte_setup` returns **GO_PREMIUM_SELL_INTRADAY** for both indices, but read it against today's short-gamma flip:

| Index | sell_premium | vol_state · VIX | implied move | expected range | size | structure | net edge |
|---|---|---|---|---|---|---|---|
| SPY | yes | MID · 17.28 | 0.87% | 1.21% | 1.0× | **wider iron condor, wings ≈ ±1.21%** (short-gamma → wider/trendier) — or reduce/stand aside | +0.30% gross / **+0.20% net** (win 93.9%, n=49) |
| QQQ | yes | MID · 17.28 | — | ~1.86% (short-gamma) | 1.0× | wider condor / reduce | +0.393% gross / **+0.293% net** (win 89.8%, n=49) |

**Lead with net, not the win-rate** (`pnl_basis`: % of spot notional, GROSS; a negatively-skewed seller's gross win-rate overstates the edge once costs are charged). **Caution this session:** the book is **short-gamma** (wider realized range, trendier) *and* a HIGH macro print lands at T+3 — the validated edge weakens precisely in this regime, and the vol-shock left tail is **unsampled**. Treat as *wings-wide or stand-aside*, delta-neutral only, **0 rubric points**. SPY ≈ SPX (trade either); QQQ weaker (NDX book unavailable).

### 2b. Swing Dealer Positioning (1–4 weeks)
- **SPY — MECHANIZED DEX FLIP SHORT (the one scored dealer trigger today).** Verified sign change: 06-18 +5.2B → 06-22 −10.1B against a clean 5-session positive run, flip-day |net_dex| 0.41× the trailing-10 median; co-fires the GEX FULLY_NEGATIVE flip and is broad (28/50 strikes negative, not a single-strike OPEX artifact). Dealers have flipped from dip-buying to selling-the-weakness. **Swing bias SHORT/cautious into PCE.** (As a standalone additive-rubric call it is sub-floor — see §7 — but the mechanics are real and feed the index-hedge bias.)
- **No vanna-squeeze** anywhere: SPY's book is genuinely put-heavy (net_vanna +35k) but the dated ^VIX series is **rising** (06-18 16.40 → 06-22 17.28, zero consecutive falls) → vanna *pressure*, not a squeeze; flag correctly suppressed. A VIX collapse from here would invert the SPY thesis to LONG (named invalidation).
- **QQQ** DEX positive but rapidly deteriorating (+77.5B → +12.0B), call-heavy vanna — no scored flip. **IWM** GEX-regime flip with ZGL overhead — structural small-cap downside caution, no scored DEX trigger.

### 2c. Sector Rotation
**Rotation regime: `no_change` (low confidence).** The persistent-inflow set straddles defensives (Utilities, Real Estate, Healthcare) *and* cyclicals/value (Financials, Industrials, Basic Materials) at once — no clean axis. Idiosyncratic positioning in a pullback tape, not rotation.

**ETF flow tape (advisory, 0 points)** — three conflicts the GICS aggregates hide:

| ETF | Net premium dir | Persistence | DP / options | GICS agreement | Note |
|---|---|---|---|---|---|
| SMH | inflow | +$106M 5d (largest) | call sweeps Jul/Aug | **disagree** | Semis diverge sharply bullish from broad XLK (MIXED) — instrument-level semi strength, not a Tech rotation |
| GDX | inflow | +$40.9M 5d | 2027 LEAP put buys | agree | Gold-miner inflow but options urgency is **protective** (hedged, not adding) |
| KRE | outflow | −$3.6M 5d | 2027 LEAP put buys | disagree | Regional banks **de-risking** even as GICS Financials shows inflow — large-cap banks in, regionals out |

Only **BSX** (Boston Scientific, Healthcare) passes the conditional sector-leader gate (persistence 0.8, 30d cum-flow +$51.3M aligned ≥$50M, DP-supported) — but it is single-agent, so it sits as watch-only (§8), not a scored call.

## 3. Swing Setups (1–6 weeks)
**No conviction-tier swing call cleared the rubric today.** The book is event-gated and defensive. Surfacing the disciplined output:

### 3a. Long swings (regime-aligned)
- *Empty at conviction.* **BSX** is the only qualified single-name long signal (Healthcare leader, +$51.3M 30d, DP-supported) but failed the ≥2-agent confluence gate → watch-only (§8).
- The accumulation lane returned **zero** flags: the cleanest dark-pool buy-side names — LRCX, AMAT, INTC, BE — *all* failed `conviction-matrix` (COVERED_CALL / HEDGED_LONG / sub-50 DIRECTIONAL_LONG), and the semis are +32–47% over 30 days (late-stage chase, not quiet accumulation). LRCX additionally carries a **C28 distribution_flag** (400C OI closed on volume, $2.3M). This is distribution dressed as accumulation — the structural warning of the day.

### 3b. Short / fade swings (defined risk only)
- **SPY — dealer DEX-flip short (index hedge bias, sub-floor outright).** Mechanics are real (§2b) but the `bearish_flow` class backtests **WR 0.42 < 0.50**, and risk-monitor docks the outright to **skip** before PCE (T+3 event gate on an undefined-risk directional short). *Do not initiate outright before 06-25; if expressed, a defined-risk-through-print put vertical only.*
- **Single-leg whale Tier-1 CONTRARIAN_SHORT puts (advisory C19, 0 points):** **TSLA** 415P floor-block $6.7M (25 DTE), **CRWV** 110P opening-prime $2.2M (size/OI 12.2), **INTC** 135P opening-prime $1.06M (size/OI 11.4). Genuine institutional single-name shorts against the tape — but every one is in **BACKWARDATION into a catalyst** and none reached a statistical crowding extreme, so they are **caution/continuation watch-items, not promoted fades** (and TRANSITIONAL ≠ the bull regime the call-beta read was measured in).
- **Bearish opening PUT builds (sweep-only, 0 points):** **NBIS** (P170, 4/5 persistence, +28.8× OI), **SNDK** (P1000/P1200 ladder, 5/5, memory IV-100 cohort), **SOXL** (3× semis put ladder) — the persistence screen *labeled these bullish*; the OI-tenor read corrects all three to **downside/hedge** positioning. Watch, no scored entry.
- **CDNS** — Step-0's standout bearish (signal-confluence score 6: bearish flow + high PCR + volume spike + DP distribution + OI building puts, net −$110M). Single-agent / informational; large single-day P370 put sweep (~$94M).

## 4. LEAP Builds (6–24 months)
**No LEAP-grade candidates** cleared the 6-of-9 gate. The long-dated tape is dominated by put-side / index-credit hedges (PBR, HYG, IWM, TLT, KRE, the two-sided SPCX complex) — dropped under borrow/financing discipline.
- **NVDA (near-miss):** the single cleanest signature — ATM C205 (DTE 360) +6,610 OI, ask 5,354 ≫ bid 2,647, $34.8M — but 90d **and** 30d cum-premium-flow are net **negative** (−268M / −98M) and conviction-matrix is MIXED @ 4.5%. The lone LEAP strike is swamped by the bearish weekly tech tape (Gate-4 fail). Re-check after PCE if cum-flow flips positive on an intact build.
- **SOFI** = COVERED_CALL (yield-enhancement overwrite, rejected). **EOSE** = $7 micro-cap lottery pair (3 of 9).

## 5. Volatility Surface
The day's real action. The memory/semis complex is at **IV-rank 100** across the board (MU, WDC, STX, DRAM, INTC, TSM, KLAC, ADI, TXN, TSEM, SIMO, ALGM; AMAT 97, SMH 98, GLW 99) into a wall of late-June earnings.

| Ticker | Structure | Catalyst | VRP | Verdict | Note |
|---|---|---|---|---|---|
| **WDC** | BACKWARDATION + **isolated 2026-07-17 kink** (IV 216%, z=3.30) | earnings ~07-17/24 (implied by surface; date unconfirmed) | **+0.145 PREMIUM_SELLING** | **SELL VOL / CALENDAR** | The one clean, VRP-confirmed dislocation — event vol *rich* vs realized → calendar-short the d25 kink vs an adjacent tenor |
| **MU** | KINKED + 06-26 front hump | **ER 2026-06-24 AMC**, implied ±11.2% | **−0.093 PREMIUM_BUYING** | **BUY VOL** (long straddle into print) | Mirror of WDC — event vol *cheap*; do NOT sell premium. Earnings-scout's SELL-VOL read conflicts (front-IV rich) — net: long-vol/own-the-move only if the realized gap beats ±11.2% |
| **FDX** | KINKED, steepest kink (FEIR 2.13) | ER 2026-06-23 AMC, implied ±6.5% | rich | SELL VOL (full) / calendar | Cleanest pure earnings vol-sell; back-skew stretched (tail also priced) → enter as the front-ratio unwinds |
| **CBRS** | KINKED (FEIR 1.586) | ER 2026-06-23, implied ±13% | — | SELL VOL (half) | Flow net-bearish −$221k; don't lean the short put too tight (negative back-skew) |
| **KLAC** | flat-front backwardation | none (late-July) | +0.058 | advisory sell only | Least event-contaminated premium-sell in the cluster, but no kink/catalyst → thin edge |

**Disqualified noise:** AIG (z=7.9 is a 4-DTE-wing artifact, not a dislocation); GLW (negative VRP → not a sell); all single-contract `iv-outliers` were 0DTE quad-witch pin prints (TSLA 420P, NVDA 0DTE chase). The broad semis cluster (TSM/INTC/KLAC/AMAT/ADI/TXN) is **PCE-macro + MU-sympathy backwardation**, not name-specific event vol — no own-earnings trade in them today.

## 6. Risk & Correlation
**Macro headline:** sticky core PCE (3.29% YoY) with the **May PCE print landing Thu 06-25 (T+3)** — the binding event for every swing-horizon decision today. Curve normal, 10Y falling, USD strengthening.

- **Correlation clusters** (`portfolio-correlation`, 30d): **MU/WDC 0.716 = cluster** (kept member MU, raw 3 > WDC); **MU/SPY 0.662 = soft-watch** (no penalty). The full **memory/semis complex (MU·WDC·SNDK·AMAT·INTC·NVDA, pairwise 0.75–0.77) is one correlated bet** — only MU is sized within it, so no portfolio over-concentration, but treat any add as adding to the same position.
- **Gates applied:** regime FAIR/no-op; VRP FAIR/no-op; panic no-op (front-IV not >1.10); **MU fundamentals CAUTION −1**, **debate −1** (bear 0.65 ≥ bull 0.55), **event-risk** exempt (the trade *is* the earnings play), **rubric_regime** half-cap. **SPY** event-risk −1 (PCE T+3 on an undefined-risk short), rubric_regime half-cap, debate tie/no-op.
- **Fundamentals verdicts (top-5):** **MU — CAUTION** (4/4 beat streak, +85% rev, Anthropic supply-deal catalyst, recom 1.35 — but price 8.4% *above* consensus target, RSI 69.8; a SELL-VOL structure into an asymmetrically-bullish binary carries upside gap risk). **SPY — NA** (index).
- **Event-risk flags:** MU own ER 06-24 (T+2) + PCE 06-25 (T+3); SPY PCE T+3.
- **Adverse-flow exits** (vs carried `conviction_2026-06-18`): **NKE** (flow reversed bearish, net −$2.3M, $24M DP, IV-rank 88.6) and **MRVL** (net −$14.2M, $207M DP block) → **exit candidates**. SNDK/MU still bullish-aligned; EWZ benign.
- **Breadth cross-check (advisory):** advancers 266 / decliners 236, pct_green 52.88% — green tape, **no divergence** (pct_green > 50). Does not change sizing.
- **Hedge sleeve:** **not required** — book is one starter delta-neutral vol play; net delta ~flat. A SPY short, if taken defined-risk, would itself be the beta hedge.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**No HIGH or MEDIUM tier names today.** Max raw_score = 3 (MU). This is a correctly defensive, vol-dominated, no-clean-accumulation session into a macro print.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: the most recent `/calibration-audit` (2026-06-20) found the conviction tiers **inverted and out-of-regime** (HIGH realized ≈0.14–0.22 vs the claimed ~0.77, bands inverted on the first post-UPTREND window) — which is *why* the P0.6 half-cap is active and nothing is sized above starter regardless of the additive score. The book's edge is not currently demonstrable at the tier level; size defensively. (Display-only; the live sizer remains the win-rate ladder.)

**Scored-call audit trail (the one above-floor name + the docked dealer short):**

| Ticker | Horizon | raw | tier | class | win_rate (n, src) | mkt_excess | pre-risk | fund | debate (B/b) | gates | final | invalidation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **MU** | vol | 3 | LOW | high_iv_rank | 0.80 (n=174, backtest_clean) | null | half | CAUTION | 0.55 / 0.65 | fund −1, debate −1, rubric half; event exempt | **starter** (defined-risk vol) | ER 06-24 disappoints / VRP flips positive / breaks momentum gap |
| **SPY** | swing | 0 | DROP | bearish_flow | 0.42 (n=137, backtest_clean) | +0.18 | starter | NA | 0.65 / 0.65 | event −1 (PCE T+3), rubric half | **skip** (no-add pre-PCE) | DEX prints positive ≥3 sessions / VIX collapses (→ long) |

> **Note on scoring (arithmetic correction):** the quant's narrative stated MU=5 / SPY=4, but the signed components sum to **MU=3** (+1 earnings-vol, +1 vol-surface, +1 halved-accumulation) and **SPY=0** (+1 dealer DEX-flip, −1 flow_conflict_lite). The envelope carries the corrected, Σ-consistent scores. Neither changes the tier outcome materially (MU stays LOW, SPY is sub-floor DROP) nor the final sizing (MU starter, SPY skip).

**Conviction-scoring rubric (frozen `2026-06-12`):** `+1` mechanized DEX-flip / vanna-squeeze · `+3` 3+ aligned accumulation (DP+OI+smart-positioning, block-stratified; halved to +1 if cum_flow_30d not sign-aligned ≥$50M) · `+1` multi-day OI build · `+1` conviction-matrix DIRECTIONAL_LONG>70 (leap_directional only) · `+1` cum_premium_flow 30d accretion (intent-screened) · `+1` sector-leader (persistence≥0.6 + aligned cum_flow ≥$50M) · `+1` earnings-scout BUY/SELL VOL · `+2` multileg directional · `+1` vol-surface KINKED/BACKWARDATION VRP-aligned · `−2` contrarian crowded-long w/ rising PC-z · `−3` flow_conflict / `−1` flow_conflict_lite (mutually exclusive). Tiers: ≥9 HIGH / 7–8 MEDIUM / 3–6 LOW / ≤2 drop. **Tier cuts carry no validated ranking claim post-2026-06-12; all sizing capped at half (P0.6).**

## 8. Watch-only — single signal, no confluence
Surfaced from one agent (or advisory-only); journaling, NOT trade entry today.
- **WDC** — vol-surface SELL-VOL/calendar (isolated 07-17 kink, +VRP) — the cleanest surface dislocation, but earnings date unconfirmed and second agent soft → watch.
- **FDX** — earnings SELL VOL (full), ER 06-23, steepest kink. Single-agent.
- **CBRS** — earnings SELL VOL (half), ER 06-23. Single-agent.
- **ACN** — multileg long strangle/combo (08-21, $32M, near-delta-neutral), but repeat_count 1 and 90d cum-flow −$121M conflicts a long-vol read. Single-agent.
- **BSX** — sector-leader long (Healthcare, +$51.3M 30d, DP-supported). Single-agent (the conditional +1 *passes*, but confluence fails).
- **NBIS / SNDK / SOXL** — bearish opening PUT builds (sweep-only, 0 pts).
- **TSLA / CRWV / INTC** — single-leg whale Tier-1 puts (advisory C19, 0 pts).
- **CDNS** — standout bearish funnel name (score 6), informational.
- **NVDA** — LEAP near-miss (cum-flow negative). **LRCX** — accumulation near-miss + C28 distribution_flag.

---
*Generated by /daily-analysis · 11 Phase-1 agents (post-OPEX; opex-pin-strategist omitted — June monthly expired Thu 06-18 on the Juneteenth-shifted calendar, next monthly 07-17 is 25d out) → quant → fundamentals-gate → bull/bear debate → risk-monitor. Rubric frozen 2026-06-12; P0.6 out-of-regime half-cap active.*
