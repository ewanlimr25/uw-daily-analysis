# Daily Market Analysis — 2026-06-16

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL (trend UPTREND) — SPY 750.33 (>20/50 SMA, +1.5% 30d, −1.3% from 90d high), VIX **16.41 (LOW)**, bullish flow only **34.7%**. Both SPY & QQQ flipped to **SHORT-GAMMA** at the EOD print (total_gex −431M / −307M) with **put walls sitting at spot** (SPY 750 / QQQ 730). Tape lean: **semiconductor / tech distribution**, defensives bid, desks buying downside protection into the Fed.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half` (P0.6 guard active). Moot today — zero names sized.
- **Next-session GEX (SPY/QQQ):** SPY short-gamma · ZGL unreliable · call wall 755 (+0.56%) / put wall 750 (at spot) · *defined-risk directional, not premium-sell.* QQQ short-gamma · ZGL unreliable · call wall 740 (+1.17%) / put wall 730 (−0.20%) · *directional debit verticals on a 730 break.* — advisory, see §2.
- **Top swing build:** **NONE.** Zero names cleared the quant floor (raw_score ≥ 3). The entire candidate union's net premium flow either *opposes* or *fails to confirm* its own thesis; the dominant `bearish_flow` class clean win-rate is **0.4203 (sub-coin-flip)**. This is a **"no edge" day** — a valid output, not a failure.
- **Top LEAP candidate:** **NONE.** leap-positioning-radar cleared zero DIRECTIONAL_LONG names (XLF closest, fails the cum-flow accretion gate at conf 28.3). Long-dated tape is defensive/bearish (put accumulation in semis).
- **Biggest risk:** The would-be semis short (MU/NVDA/SMH/TSM/KLAC/AVGO/SOXX) is **one 0.99-correlated position**, not a basket — and **FOMC decision + SEP lands this week (Jun 17–18)**, inside every swing horizon. The actionable note is a single existing-position exit (**trim HPE** — off-thesis flow reversal) and a **cheap defined-risk Fed-week hedge sleeve** (below). No new directional risk.

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend label UPTREND (SPY > 20-SMA 746.44 > 50-SMA 726.61). Breadth is **flow-bearish**: 2,174 bullish vs 4,083 bearish flow tickers (**34.7% bullish**). Guidance: half position sizes, defined-risk, iron condors in range.
- **Per-index gamma (current-state EOD book):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 750.78 | 285 (unreliable, extrapolated) | **−431M** | SHORT-GAMMA | 755 | **750 (at spot)** |
| QQQ | 731.45 | 291 (unreliable) | **−307M** | SHORT-GAMMA | 740 | 730 (−0.2%) |
| IWM | 292.13 | null (FULLY_NEGATIVE) | negative | SHORT-GAMMA | — | ~290 |

  Both index ETFs flipped **negative same-day** from a clean long-gamma book on 6/15 — a **fresh, unstable** short-gamma regime, gap-voidable into FOMC. §2 carries the forward read.
- **`uw options-flow dte-volume-share`:** 0DTE 31.4% / weeklies 32.4% / monthlies 21.8% / LEAP 5.1% — **BALANCED** (not retail-dominated; 0DTE < 50%).
- **`uw historical vrp` (SPY):** **FAIR**, slightly negative (−0.0076; IV30 13.77% vs RV30 14.53%) — realized just *above* implied. **Not** a clean premium-selling edge broadly.
- **Macro backdrop (`fred_macro`):** yield curve **normal** (+0.38); **core CPI 2.96%** YoY, **core PCE 3.29%** (sticky); unemployment 4.3%, payrolls +172k; **10Y 4.47% (falling −0.12 30d)**; USD **strengthening**; fed funds 3.63%. Disinflating headline, sticky core, easing long end.
- **Forward event_risk (next ~10 trading days):** **PPI (May) — Jun 17 [HIGH]** · **FOMC decision + SEP — Jun 17–18 [HIGH, DOMINANT — Warsh's first meeting, rate held 3.50–3.75%]** · **Initial Jobless Claims — Jun 18 [MED]** · **Monthly OPEX — Jun 19 [MED]** · **Core PCE / Personal Income — Jun 28 [HIGH]**. A double event-risk week (Fed Wed/Thu, OPEX Fri).

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book read forward as the prior for the next open. Prose-only, **0 rubric points**, no backtested predictive claim. Scope: **SPY and QQQ only.**

**Data-integrity note:** the GEX endpoint labeled both books `regime: POSITIVE` but returned **negative `total_gex`** (−431M / −307M) with a deeply-extrapolated ZGL (~62% below spot, fails the 5% rule). Per the ZGL-reliability fallback, the governing read is the **`total_gex` sign + spot-vs-wall = SHORT GAMMA**, `zgl_reliable=false`. The 6/15 book was cleanly long-gamma (+1.19B / +0.66B) → today is a **same-day flip negative = fresh / unstable.**

| Index | Regime | ZGL | Call wall | Put wall | Next-session 0DTE structure bias |
|---|---|---|---|---|---|
| **SPY** | SHORT-GAMMA (−431M) | unreliable | 755 (+0.56%) | **750 (at spot)** | Short-gamma + tight 4-pt call wall → **defined-risk directional**, not premium-sell. Down-break of 750 → put debit vertical 750/745 (dealers amplify); hold → fade the 755 poke (755-capped). Avoid naked short straddles — at-money −GEX wall = vol can expand fast if 750 fails. |
| **QQQ** | SHORT-GAMMA (−307M) | unreliable | 740 (+1.17%) | 730 (−0.20%) | Short-gamma + wider call wall → **directional debit verticals / long-premium on the flip.** Break of 730–731 → put debit vertical toward the 715 shelf; strength toward 740 can be faded with room. Long straddle more justifiable than SPY if 730 cracks into the print. |

**Mandatory caveats:** EOD is a *prior*, not a target (fresh 0DTE OI re-computes ZGL/walls in the first 30–60 min). **Gap risk voids the prior** — FOMC (Jun 17–18) + PPI (Jun 17) can gap spot through the walls before hedging engages. ZGL unreliable today (use total_gex sign + walls). ETF book, not the cleaner SPX/NDX index book. uw-pp cannot isolate the D+1 expiry (0–45 DTE proxy).

### 2a. Next-session 0DTE premium-selling setup (`zerodte_setup.py` — the validated stack)
> Advisory, **delta-neutral, 0 rubric points.** NOT a guaranteed edge — the validation sample has **no vol shock**, so the short-vol left tail is **unsampled**. The GEX walls above are a *map*, not a pin (wall-as-magnet backtested NO_GO).

| Index | Sell premium? | Verdict | Win (open) | Mean PnL gross / **net** | Vol state · VIX | Exp. range | Size scalar | Structure / caution |
|---|---|---|---|---|---|---|---|---|
| **SPY** (≈SPX) | yes | GO_PREMIUM_SELL_INTRADAY | 95.7% | +0.31% / **+0.21% net** | LOW · 16.41 | ±1.22% | **0.50** | Wider iron condor, wings ≈ ±1.22% (short-gamma / trendier) — or reduce. |
| **QQQ** (weaker) | yes | GO_PREMIUM_SELL_INTRADAY | 89.1% | +0.389% / **+0.289% net** | LOW · 16.41 | ±1.88% | **0.25** | Wider IC, wings ≈ ±1.88%. **⚠ CAUTION: front-end backwardation (0DTE IV 1.93× VIX) — event/gap risk, half size.** |

- **PnL basis:** `mean_pnl_open_*_pct` is **% of underlying spot notional, GROSS** (net = gross − 0.10% assumed round-trip cost). Lead with **net** — at LOW VIX the edge is thin and a negatively-skewed seller overstates on the gross win-rate.
- **When:** enter at/after the open once the gap resolves; hold the 0DTE to the close; **never carry overnight** (overnight backtested negative). If it gaps beyond the wings, stand aside.
- **Direction:** none — delta-neutral. **Given the FOMC gap risk + LOW VIX (thin edge) + short-gamma, this lane is best stood-aside through Wednesday** and reconsidered post-decision.

## 2a. Swing Dealer Positioning (1–4 weeks)
- **`dealer-positioning-strategist`: NO mechanized DEX sign-change qualifies on the latest session for any index or theme name. Dealer-positioning +1 rubric line NOT awarded.** The whole complex flipped positive on 6/11–6/12 (5 sessions stale, already expressed: SPY 737→750, QQQ 716→743) — no *new* flip today; books continued positive runs into FOMC. Positive DEX in an up-tape is **beta**, not a pre-directional signal.
- SPY DEX +46.4B (NEUTRAL swing) · QQQ +45.3B (NEUTRAL) · IWM −1.06B (latest negative but |flip| 0.12× the 10-session median = **rejected as a low-magnitude whipsaw**).
- **IWM is the only put-heavy book** (net_vanna +31,282) — a latent vanna-squeeze setup — but the falling-VIX leg is **unverifiable** (Yahoo `^VIX` returns 2025-anchored candles; out-of-band VIX forbidden for the squeeze leg). Flagged "latent, do not score"; re-check post-FOMC if a citable VIX series appears. IWM ZGL freshly flipped FULLY_NEGATIVE on 6/15 (fragility into the Fed).
- Theme names (NVDA/AMD/MU/SMH/AVGO) all uniformly **POSITIVE DEX (beta)** — confirming the distribution thesis lives in put-OI / dark pool, not dealer-delta sign.

## 2b. Sector Rotation
- **`sector-rotation-strategist`: rotation_regime = `no_change`** (low confidence). No clean canonical pattern — money-OUT = Tech (distributing) but money-IN spans Comm Services (growth-adjacent) + Financials (value) + Industrials (cyclical) simultaneously. Name-selection tape, not a rotation tape.
- **CONFLICT RESOLVED:** `sector-flow` shows Tech +$5.1B "inflow" — but that is a **gross-premium artifact** (Tech is the largest sector by gross premium, so its call−put spread is mechanically largest every day). The instrument tape contradicts it decisively: **SMH −$125M is the single largest ETF outflow in the universe** (wall-to-wall puts $600/560/665 Jul–Sep), with MU −$192M, MSFT −$84M, SNDK −$52M, INTC −$48M. **Technology is DISTRIBUTING**, exactly as the synthesis flagged.
- Persistence non-discriminating today (10/11 sectors = 1.0 INFLOW on net call-put premium); the market-relative magnitude bar carries the call. Inflow leaders (advisory): Comm Services (META), Financials (JPM/BRKB — **OPEX-call-inflated, wait post-6/18**), Industrials (GWW/AAL). None promoted — all single-agent, fail the confluence gate.

**ETF flow tape (advisory, 0 points)** — ranked by 5d net-premium × persistence:

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| **SMH** (→Tech) | **outflow −$125M** (largest) | strong | bid-side hedge prints | **PUT-dominated** ($600/560/665 Jul-Sep) | **agree** (Tech distributing) | MU/MSFT/SNDK/INTC |
| GDX (→Materials) | inflow +$36M | moderate | large bid-side accum | MIXED (Sep puts vs 2028 LEAP calls) | partial | SCCO/AG/Vizsla |
| EWY (Korea) | inflow +$8.5M | mixed | strong accum ($144M+$69M) | calls $220 Jul ask-side | n/a (no GICS) | instrument-only |
| IGV (→Software) | inflow +$6.7M | moderate | accum prints | mixed | **disagree** (Tech net OUT) → watch-only | — |
| XLE / XOP (→Energy) | inflow +$7.1M / +$5.7M | moderate | rank-only | rank-only | agree | — |

  ETF DP is a positioning/creation-redemption tell, **not** single-name accumulation; ETF options flow weighted above ETF DP. **Highest-conviction read: short the semis on strength** — but see §6/§7, the short does not clear the quant floor (flow contradicts it).

## 3. Swing Setups (1–6 weeks)

**EMPTY — no swing setup cleared the conviction floor today.**

Zero names scored raw_score ≥ 3 at the quant layer. The dominant semis-distribution thesis is real at the *positioning* level (put-OI building, dark-pool distribution) but is **contradicted by net premium flow on every name**:
- **MU** (short) raw **−1**: +1 earnings SELL VOL, +1 OI build, **−3 flow_conflict** (30d net premium **+$153.3M LONG** opposes the short). `bearish_flow` clean WR 0.4203. → skip.
- **NVDA** (short) raw **−1**: +1 OPEX BWB pin, +1 OI build, **−3 flow_conflict** (30d **+$132.7M LONG**). → skip.
- **SMH** (short) raw **1**: +1 OI build, +1 cum-flow accretion (−$67M short-aligned), −1 flow_conflict_lite. Sector +1 withheld (Tech persistence is INFLOW/long, opposing the short). → skip.
- **MSFT** (short) raw **1**: +1 OI build, +1 cum-flow accretion (−$53.9M), −1 flow_conflict_lite. (accumulation-hunter: COVERED_CALL/upside-capped, not a clean short.) → skip.
- **XLB** (short) raw **1**: +2 multileg bear put spreads (cleanest directional structure on the board), −1 flow_conflict_lite (30d +$10.4M bullish). win_rate NA(substrate). → starter, but below floor → drop.

- **3a. Long swings:** none. accumulation-hunter cleared **zero** real institutional longs (MSFT = covered-call cap; AAPL = DIRECTIONAL_LONG but conf 23.4 retail-0DTE-diluted; LRCX = distribution, block-tier 0.264 selling). Long-side confluence names were all sub-floor micro-caps (OCUL/NMRA/DOMO/QMCO/TGTX) failing the C12 liquidity floor.
- **3b. Short / fade swings:** none cleared. contrarian-scanner found **zero fades** — the semis "crowded short" is a **structural insurance bid into FOMC** (uniform BACKWARDATION + catalyst), not crowding to fade; no index fear extreme (SPY z +0.93, QQQ z −0.69, all NORMAL). The multileg bearish structures are in **defensives** (VFC bear put spread 15/10, XLB bear put spreads) — single/double-agent, dropped to watch-only.

**Sweeps (informational, 0 points):** no clean directional sweep. The entire persistence book is index/mega-cap **hedge flow** (SPY/QQQ/NVDA/MSFT/META bearish sweeps, all cum_flow MIXED). MRVL bullish per the tool but corroboration kills it (two-sided OI into OPEX) → watch-only. Net tape: bearish-tilted **hedging**, not directional shorting.

## 4. LEAP Builds (6–24 months)

**EMPTY — zero DIRECTIONAL_LONG LEAP candidates clear the 6-of-9 gate.**

- **XLF** (closest): DIRECTIONAL_LONG but **conf 28.3 (<70)**; OI BUILDING 10 days, but **cum-flow accretion FAILS** (90d +7.8M / 30d −1.3M, flat) and DTE>180 strikes are **bid-side** (sell-side, not conviction). Disqualified.
- Near-misses disqualified: CORZ (cum-flow bearish), NKE (DIRECTIONAL_SHORT), FCX (bid-side LEAP strike), BAC (insufficient persistence).
- Long-dated tape is **defensive/bearish**: fresh put builds VSH (P45 dte584, +4.5×, $24.1M ask-side), NVDA (P180/190 dte185), MU (P550 dte185), MRVL (K280)/SYF (K75) dte584. Noted, not LONG flags.

## 5. Volatility Surface
`vol-surface-scout` — the backwardation across the high-IV cluster is **FOMC/OPEX-driven** (concentrated in the 06-18 front bucket, decaying off the 10-DTE leg), **not idiosyncratic**. All percentiles PROVISIONAL (n=46, below the 120-day floor) — leaning on z-scores. VRP FAIR/slightly-negative ⇒ **not** endorsing broad premium-selling; calendars/diagonals (long the back leg) preferred over naked short premium, and **any short-vol must be defined-risk and closed before the Jun 17–18 FOMC.**

| Ticker | Term structure | z-score | Skew | Read | Bias |
|---|---|---|---|---|---|
| **STX** ($1031) | BACKWARDATION (decayed from 2.10→1.115 7/45) | +1.87 | COMPLACENT | Highest genuine z in the liquid set; steepest front-bucket panic decay | **SELL VOL small / calendar-diagonal** — sell 06-26, own 07-17 (harvest crush without naked FOMC) |
| **SMH** ($616) | BACKWARDATION | +1.31 | **TAIL_HEDGING (put bid)** | Real index hedging demand in the back month — do not sell that tail | **Calendar, NOT short** — sell 06-26 / own 07-17 |
| **TSM** ($426) | BACKWARDATION | +2.12 | COMPLACENT | 7/45 ratio FLAT off the 0DTE noise leg — no front richness to short | Context only — no clean trade |
| **COHR** ($383) | BACKWARDATION | **−0.10 (NORMAL)** | COMPLACENT | IV is *median*, not rich (Goyal-Saretto correction of a single-day spike) | **NO TRADE / demote** |
| **KLAC** ($237) | BACKWARDATION | +1.72 | COMPLACENT | Real high-z but sparse tenor (no clean 10-DTE) | Watch — not actionable |

- **ENSG disqualified** (z +2.51 headline but thin tape: 41 call contracts, ~$13K premium). IV outliers (`iv-outliers`) all penny-stock OPEX lottery noise — zero C12-eligible.
- **Earnings vol (thin mid-June window):** **JBL** (Jun-17 pre, SELL VOL **half-size**, cleanest crush — 161% front → ~70% back) · **ACN** (Jun-18 pre, SELL VOL **half-size**, front-ratio 2.458 panic — wait for it to tick down) · **MU** (Jun-24, SELL VOL quarter / lean SKIP) · **NKE** (Jun-30, SKIP). No full-size SELL VOL anywhere — back-month skew complacent on all (tail not priced). No BUY VOL, no calendar. These are single-agent (earnings-scout) → watch-only, defined-risk, **closed before the print / FOMC**.

## 6. Risk & Correlation
- **Macro headline:** sticky core (CPI 2.96% / PCE 3.29%), 10Y 4.47% falling, USD strengthening. **Forward event_risk: FOMC + SEP Jun 17–18 (DOMINANT, inside every horizon), PPI Jun 17, Jobless Jun 18, OPEX Jun 19, PCE Jun 28.** The Fed alone would −1-tier any swing structure this week.
- **Breadth cross-check (`fz`, advisory):** S&P 500 advancers 273 / decliners 230 / **pct_green 54.27%** / avg change −0.11% / median +0.14%. **No strong divergence** (green-ish but a flat tape; pct_green > 50). Top TTWO +6.35%, worst CBOE −9.45%.
- **Would-be correlation cluster (`semis_distribution_cluster`):** had a semis short cleared, it would have been **one position, not seven** — SMH/SOXX 0.991, SMH/KLAC 0.891, MU/SOXX 0.850, NVDA/TSM 0.811; 9/10 pairs ≥ 0.70. 100% single-sector concentration = 7× the same FOMC-event risk.
- **Gate stack (moot — zero names sized):** a hypothetical semis short into FOMC would have carried **regime (−1) + cluster (−1) + event_risk (−1) + rubric_regime (cap-half) simultaneously** — floored to skip/starter even before the quant's sub-coin-flip win-rate (0.4203) and full −3 flow_conflict zeroed it.
- **Fundamentals gate / debate:** correctly **SKIPPED** — no top-5 surfaced to vet (both stages can only confirm/cut a sized name; there were none).
- **Adverse-flow exits** (vs prior `conviction_2026-06-15` = SMH, GOOGL, MU, INTC, HPE):
  - **⚠ HPE — EXIT CANDIDATE.** Bearish net flow −$6.0M + **net OI decreasing −15.2k** (positions closing) vs prior long-lean. **Trim/close** any HPE long.
  - MU / SMH / INTC — flow **confirms** the distribution read (not exits), but **MU IVR 96.9** = distribution is maximally priced; do not initiate fresh short-vol there.
  - GOOGL — flow still **bullish/constructive** (the lone clean name); hold.
- **Hedge sleeve (standalone Fed-week tail insurance — there is no directional book to hedge, only the tape's vol-expansion risk; VIX 16.41 makes optionality cheap):**
  1. **SPY 745/725 put spread** (06-19 / 06-26) — 745 just below the 750 put wall; below it short-gamma dealer selling accelerates the move.
  2. **QQQ 725/705 put spread** (06-19 / 06-26) — semis/tech tilt without single-name FOMC risk in the 0.99-correlated cluster.
  3. **VIX 20/30 call spread (July)** — follows the institutional $15.8M VIX 45/65 bid; convex pop on a hawkish-SEP surprise.
  - **Do NOT sell premium** into this (FAIR/negative VRP + short-gamma + binary event = wrong side of the vol gamma). Size to 1–2 fixed risk units, defined-risk, all legs ≤ ~5 weeks.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**NONE.** No HIGH or MEDIUM tier names today. The book is empty by design — the quant floor and the risk stack agree on **no trade**.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: not computed today (empty book). Note: the most recent `/calibration-audit` (2026-06-12) found the ≥9 HIGH cut **failed its scheduled re-confirmation** (HIGH realized 0.222 vs claimed 0.774 on the first post-UPTREND window) — the P0.6 out-of-regime guard caps all sizing at half in the interim. The frozen rubric carries no validated ranking claim until ≥30 resolved post-2026-06-12 calls re-validate the tiers.

**Audit trail — scored-then-dropped names (raw < 3 floor; documented for calibration, NOT for entry):**

| Ticker | Dir | raw | Σ components | dominant_class | win_rate (clean, n) | market_excess | Why dropped |
|---|---|---|---|---|---|---|---|
| MU | short | −1 | +1 earn, +1 OI, **−3 flow_conflict** | bearish_flow | 0.4203 (n=138) | +0.130 | 30d net +$153.3M LONG opposes short; WR sub-coin-flip |
| NVDA | short | −1 | +1 OPEX pin, +1 OI, **−3 flow_conflict** | bearish_flow | 0.4203 (n=138) | +0.130 | 30d net +$132.7M LONG opposes short |
| SMH | short | 1 | +1 OI, +1 cum-flow, −1 lite | bearish_flow | 0.4203 (n=138) | +0.130 | sub-floor; sector +1 withheld (Tech INFLOW) |
| MSFT | short | 1 | +1 OI, +1 cum-flow, −1 lite | bearish_flow | 0.4203 (n=138) | +0.130 | covered-call (not a clean short); sub-floor |
| XLB | short | 1 | +2 multileg, −1 lite | multileg_directional | NA(substrate) | — | cleanest structure but 30d flow bullish; sub-floor |

*win_rate via the P0.3 clean-query protocol (bearish_flow, market-wide per class, complete-window n=138, 11 clamped rows dropped — the raw headline 40.3% is quarantined). market_excess vs SPY-short over the same windows is positive but downgrade-only and cannot lift a sub-0.50 class.*

<details><summary><strong>Conviction-scoring rubric (frozen v2026-06-12) — embedded for audit</strong></summary>

```
Daily conviction score = Σ:
  +1  dealer-positioning MECHANIZED DEX flip / vanna-squeeze in trade dir (verified SIGN CHANGE, not level)
  +3  3+ aligned accumulation (DP+OI+smart-positioning, block institutional-tier) — CONJUNCTION: full +3 only if
        cum_flow_30d sign-aligned AND |cum_flow_30d| ≥ $50M; else halved → +1
  +1  multi-day OI build (oi-trend BUILDING, --days ≥ 5)
  +1  conviction-matrix DIRECTIONAL_LONG conf > 70 — CONDITIONAL: only when dominant_signal_class == leap_directional
  +1  cum-flow net directional accretion (30d) — INTENT-SCREENED (no C28 distribution_flag; no deep-ITM ex-div arb)
  +1  sector-rotation single-name leader — CONDITIONAL: sector persistence ≥ 0.6 AND cum_flow_30d aligned AND ≥ $50M
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg directional structure (term-structure-anchored play type)
  +1  vol-surface KINKED / BACKWARDATION with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian overcrowded long + rising pc-ratio-zscore (informed-flow continuation penalty)
  -3  flow_conflict — cum-flow 30d clearly opposite dominant_signal_class (mechanical)
  -1  flow_conflict_lite — cum-flow 30d MIXED (mutually exclusive with flow_conflict)
  [TIER GATES, applied by risk-monitor in 2d, NOT score_components]:
  -1 tier  correlation cluster (pairwise corr ≥ 0.70)
  -1 tier  market-regime conflicts with trade direction
REMOVED: signal-confluence ≥4 line (P0.2); sweep-persistence line (0 points).
Tiers: ≥9 HIGH (full) · 7–8 MEDIUM (half) · 3–6 LOW (watch) · ≤2 drop.
OUT-OF-REGIME guard (P0.6): all conviction sizing capped at half until ≥30 resolved post-2026-06-12 calls re-validate.
```
</details>

**Deep-dive hand-off:** none (no HIGH-tier names). Step 6 / 6.5 / 8.5 (deep dives, batch-scan, `/stock-deep-dive` hand-off) skipped — empty book.

## 8. Watch-only — single signal, no confluence
Surfaced by one agent (or with internal conflict) — for journaling, **NOT** for trade entry today:
- **Bearish single-names:** TSM (sector-out; contrarian aborted), KLAC (distribution), VFC (multileg bear put spread 15/10 — cleanest single-name directional, single-agent), CRM (single-leg floor put K230 $30M **but** bullish net-prem +$89M — conflicted), INTC / SNDK / AVGO / COHR (distribution flags).
- **Single-leg Tier-1 floor PUTS (C19 advisory, 0 points, informed-continuation):** CRM, INTU (K440 $11.7M), MSFT (K450 $10M), ZS (K250), COIN (K270), SMCI (K55), NBIS (K255, OPENING_PUT_PRIME size/OI 3.26 — strongest). Routed to the short lane as context, not fades.
- **Bullish single-names:** META (Comm Svcs leader, IVR 36 cheap vol), GWW / AAL (Industrials), JPM / BRKB (Financials — OPEX-call-inflated, wait post-6/18), AAPL (bullish confluence 5 but accumulation DIRECTIONAL_LONG rejected at conf 23.4).
- **Vol / non-directional (defined-risk, close before FOMC):** JBL & ACN (earnings SELL VOL), STX (calendar). OPEX pins (neutral-vol, **post-FOMC only**): XLF iron-fly 55 (strongest enforcement, +278M wall), AAPL iron-fly 300, NVDA BWB 210, AMZN BWB 250 — index pins (SPY/QQQ/IWM) **do not qualify** (short-gamma at the OPEX strike or >2% distance).

---
*Two-phase fleet: 11 Phase-1 alpha-finders (OPEX week) → signal-confluence-quant → risk-monitor. Fundamentals-gate + bull/bear debate skipped (no top-5). Rubric frozen v2026-06-12. Watchlist write-back: SKIPPED (zero conviction names — avoids polluting tomorrow's correlation universe).*
