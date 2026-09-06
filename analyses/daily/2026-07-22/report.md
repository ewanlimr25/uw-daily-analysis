# Daily Market Analysis — 2026-07-22

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / UPTREND (SPY 747.41, +0.41% 30d, −1.71% off the 90d high, above 20/50-SMA). Breadth **bearish** — only 33.8% of optionable names carry bullish flow; independent Finviz breadth 246 adv / 253 dec, `pct_green` 48.9% (**divergence flag** — index flat-to-green while more names fall). VIX 16.64 (LOW). Both index gamma books are **short-gamma near spot** (SPY FULLY_NEGATIVE, total_gex −$443M; QQQ negative near-spot despite a mislabeled "POSITIVE"). VRP FAIR (IV30 13.94 ≈ RV 13.92 — no vol edge either way). Tech is the lone heavy inflow (+$3.23B single-day, 5d persistence 0.8, ramping); Comm Services flowing out on the multi-day read.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`. Freeze-lift blocked a 5th consecutive audit cycle.
- **Next-session GEX (SPY/QQQ):** **SPY** short-gamma (FULLY_NEGATIVE, ZGL n/a, call wall 755 / put wall 740) → break of 740 accelerates, air-pocket to 735/730; **QQQ** short-gamma near spot (total_gex −$477M, call wall 730 / put wall 700; 0DTE IV backwardated 1.58× VIX) → trend/gap-risk prior, not a pin. Advisory, see §2.
- **Top swing build:** **NONE.** Zero names cleared the conviction rubric — top raw_score is 2 (JPM, NVDA), both single-agent, below the LOW floor (raw ≥3). ~17th consecutive all-DROP daily.
- **Top LEAP candidate:** **NONE.** Every long-dated near-miss (TLT, WULF, WEN, PBR, TSLA, INTC) failed the cum-premium-flow accretion gate; no mega-cap semi has a fresh ask-side LEAP call build.
- **Biggest risk:** the **semis/memory correlation cluster** {MU, DRAM, SMH, AMD, AVGO} (MU/DRAM 0.95, SMH/AMD 0.93) is one position, not five — and it sits directly under a stacked event calendar: **FOMC 07-29 (T+5, no-SEP) + MSFT & META earnings same day, GDP 07-30, core PCE 07-31**. The empty book is the hedge. No sleeve required.

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL / UPTREND. SPY 747.41, above 20-SMA (745.67) and 50-SMA (745.08), +0.41% 30d, −1.71% from the 90d high. Breadth is the tension: 2,119 bullish- vs 4,149 bearish-flow tickers (33.8% bullish). Guidance: half size, defined-risk, iron condors in range.
- **Breadth cross-check (Finviz, advisory):** 246 advancers / 253 decliners, `pct_green` 48.9%, avg change −0.01%, median −0.01%. Index green-ish but more names red → **breadth-divergence / distribution tell**, corroborating the bearish flow skew and the same-day insider-selling verdicts on NVDA/MU.

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 748.10 | n/a (FULLY_NEGATIVE) | −$443.1M | **FULLY_NEGATIVE** (short-gamma across grid) | 755 (+0.92%) | 740 (−1.08%) |
| QQQ | 706.70 | 352.82 (artifact) | −$477.0M | label POSITIVE but **negative near-spot** (trust the sign) | 730 (+3.30%) | 700 (−0.95%) |
| IWM | 293.91 | 130–199 (broken grid) | −$0.34B to −$1.16B (10d all neg) | short-gamma, no flip | — | — |

- **DTE volume share:** 0DTE 36.4% / weekly 27.0% / monthly 22.2% / LEAP 2.4% — **BALANCED** (no retail-dominance downweight, no institutional benefit-of-doubt).
- **VRP:** SPY IV30 13.94% ≈ realized σ30 13.92% → **FAIR** (vrp ≈ 0.0001). Neither a premium-selling nor a premium-buying regime at the index level.
- **Macro backdrop (`scripts/fred_macro.py`):** yield curve normal (10Y-2Y +0.36); core CPI 2.81% / **core PCE 3.41% YoY (sticky, above target)**; unemployment 4.2%, payrolls +57k; 10Y 4.63% **rising** (+17bp/30d); USD strengthening; fed funds 3.63%. Forward `event_risk` (Tier-1, next ~10 trading days): **jobless claims 07-23 · FOMC 07-29 (no-SEP, ~89% hold priced) · Q2 GDP advance 07-30 · core PCE (June) 07-31 · NFP 08-07.** A swing book sized today eats the FOMC/GDP/PCE stack next week.

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> Advisory, prose-only, **0 rubric points**, no backtested predictive claim. EOD 0–45d dealer-gamma book read forward as the prior for the next open. Scope: SPY & QQQ only. Predictive validation lives in `/weekly-analysis` §2.

**SPY — spot 748.10 · FULLY_NEGATIVE · total_gex −$443.1M · ZGL n/a (`zgl_reliable=false`)**
Every strike 724→748 carries negative net GEX — dealers are short gamma across the entire near-spot grid, not just below one flip line. This is a **trend/breakout prior**: hedging amplifies moves in either direction. Call wall 755 (+0.92%) is a soft cap; put wall 740 (−1.08%) is real support but reads as an **air-pocket** level — a break below 748 that reaches 740 likely accelerates into 735/730 as dealers sell weakness. **Structure bias:** prefer debit verticals / long premium over pin-mechanics 0DTE; if selling premium at all, keep wings very close and size down (FULLY_NEGATIVE is the worst regime for naked short-gamma).

**QQQ — spot 706.70 · label POSITIVE but total_gex −$477.0M (internally inconsistent) · ZGL 352.82 (artifact, `zgl_reliable=false`)**
The per-strike grid is negative at every strike 684→708 and only turns positive from 709 up. Trust the negative `total_gex` sign over the "POSITIVE" label (the same ZGL-grid artifact now confirmed recurring across SPY/IWM/MU). Spot sits on a negative-GEX shelf → trend risk on any move toward 700. Book turns supportive only above ~709–712 and stays thin to the 730 call wall — a rally has room before dealers cap it. Put wall 700 (−0.95%). **Structure bias:** directional 0DTE / debit verticals unless spot holds above ~710; 0DTE IV already flagged BACKWARDATION at 1.58× VIX (elevated-gap-risk session, not a pin).

**Mandatory caveats:** EOD is a *prior*, not a target (fresh 0DTE OI recomputes ZGL/walls in the first 30–60 min); gap risk voids the prior — **jobless claims 07-23 is same-day, FOMC/GDP/PCE land next week inside the 0–45d window**; ZGL unreliable on both (SPY null, QQQ extrapolated); ETF book, not the cleaner SPX/NDX index book; `uw` cannot isolate the D+1 expiry (0–45d proxy).

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py`, advisory)
> The GEX walls are a map, not a pin — wall-as-magnet and every directional 0DTE signal backtested NO_GO. What validated is **delta-neutral premium-selling**. Advisory, **0 rubric points**, NOT a guaranteed edge (no vol shock in the validation sample → short-vol left tail UNSAMPLED). Backtest verdict: **GO_PREMIUM_SELL_INTRADAY**.

| Index | Sell prem | Vol state | VIX | Implied move | Exp. range | Size | Net PnL (gross) | Structure |
|---|---|---|---|---|---|---|---|---|
| **SPY** | yes | LOW | 16.64 | 0.79% | 1.17% | ×0.5 | +0.178% (+0.278%) | wider IC ~±1.17% (short-gamma / trendier) |
| **QQQ** | yes | LOW | 16.64 | 1.66% | 1.93% | ×0.25 | +0.313% (+0.413%) | wider IC ~±1.93% — **caution: front-end backwardation (0DTE IV 1.58× VIX)** |

- **VIX LOW (16.64) = thin edge** (LOW-VIX-state mean PnL is the weakest tercile). SPY≈SPX (validated identical); QQQ weaker (NDX index book unavailable) — lower confidence + explicit backwardation caution → half the SPY size at most.
- **Entry:** at/after the open once the gap resolves; hold the 0DTE to the close; **never carry overnight** (overnight entry backtested negative). Stand aside if it gaps beyond the wings, or if VIX spikes / front-end steepens further into 07-23 claims.
- **Direction: none** — delta-neutral. Do not add a tilt.

## 2a. Swing Dealer Positioning (1–4 weeks)
VIX fell **3 consecutive sessions** (18.77 → 18.65 → 17.05 → 16.64, dated via Yahoo `^VIX` — the "no clean 2026 VIX source" memo is now stale). That falling-VIX leg validates the vanna reads below.

- **SPY / QQQ — vanna-squeeze TRUE (put-heavy book + falling VIX), swing_bias LONG (hypothesis-tier only).** Both DEX states are negative *levels*, not mechanized flips (the real sign change was 6 sessions ago, now entrenched). Karsan/SqueezeMetrics framing, not validated edge.
- **IWM — NEUTRAL.** DEX deteriorated on the latest session while vanna asserts dealer-buy pressure → the two disagree, no clean thesis.
- **MU — MECHANIZED DEX flip (LONG), the only clean scored flip today.** net_dex 07/20 −5.68B → 07/21 +4.77B, prior 3 sessions negative, |flip| ≈ 4.8B (≥ 0.25× median), held 2 sessions. Magnitude verified on a 7-session proxy median (not the full 11 — partial verification). Scores the +1 DEX line.
- **AVGO — real mechanized DEX flip (07/21) but vanna DISAGREES (call-heavy) → NEUTRAL/mixed, not a directional call** (earns 0).
- **NVDA / TSLA / SNDK / DELL — no qualifying flip** (SNDK's sign-change fails the magnitude floor — textbook whipsaw the rule exists to kill).
- **Audit note:** the broken-ZGL-grid artifact (`zero_gamma_level` ≈ half-of-spot with a spurious POSITIVE label contradicting negative `total_gex`) now confirmed recurring on SPY/QQQ/IWM/MU — escalate from a QQQ-specific note to a general `gex-time-series` defect.

## 2b. Sector Rotation
Rotation regime: **no_change** (low confidence). Structural non-discrimination — 7 of 11 sectors tied at persistence 1.0; magnitude did the work.
- **Rotating in (cross-confirmed):** Consumer Cyclical (persistence 1.0, +$155M, XLY agrees) — but its flow-dominant name **TSLA fails the leader gate** (30d cum-flow −$451M distribution). Healthcare (+$457M, XLV flat). **Financials (+$185M) but XLF/KRE ETFs DISAGREE → downgraded to watch-only.**
- **Tech — near-miss, flag for tomorrow:** persistence 0.8 (misses the 1.0 tier by one down-day 07-16), but by far the largest flow ($3.23B, 14× the next sector, ramping). ETF tape split: IGV weakly agrees, **SMH actively disagrees (−$55.3M 5d, worst reading in the universe)**. NVDA (30d +$37.9M) and AVGO (−$22.3M) both fail the leader gate.
- **Rotating out:** Industrials (persistence 0.8 OUTFLOW, −$69M, XLI agrees). BA the cleanest short but fails the $50M magnitude floor.
- **Only full-gate leader on the board: JPM** (Financials persistence 1.0, 30d cum +$53.0M ≥ $50M) — but sits under a watch-only sector, so it's a standalone idea, not a rotation trade.

**ETF flow tape (advisory — strengthens the conditional leader +1, no new points):**

| ETF | Net premium (5d) | Trend | GICS agreement | Note |
|---|---|---|---|---|
| XLY | +$10.6M | BULLISH | agree (Cons Cyclical) | leader TSLA gate-failed |
| IGV | +$4.65M | BULLISH | Tech watch-only | no call to gate |
| XOP | +$3.33M | BULLISH | Energy near-miss | — |
| XLI | −$3.86M | BEARISH | agree (Industrials out) | BA gate-failed |
| KRE | −$11.78M | BEARISH | disagree (Financials) | downgrades JPM's sector |
| SMH | **−$55.3M** | MIXED | **disagree (Tech)** | largest outflow in universe; overrides the +$6.3M single-day bullish sweep |

## 3. Swing Setups (1–6 weeks)
**EMPTY — no name cleared the conviction rubric.** Every long candidate was single-agent (confluence-gate fail) and/or killed by opposing 30d premium flow:

- **MU** (raw 1) — mechanized DEX flip LONG, but single-agent, insider selling into the +12% post-earnings gap (fundamentals CAUTION), and the flip is partly reactive to that gap. Keeper of the semis cluster; watch-only.
- **NVDA** (raw 2) — bullish deep-ITM call **diagonal** (Oct 180C / Sep 190C, Δ0.8 stock-replacement), but **roll-caveated** (same signature as a duration-extension roll) and single clean agent; insider MSPR −98.6 (near-total selling) into the long = fundamentals CAUTION. Watch-only.
- **AMD** (raw −3) — the recurring mega-cap pattern: bullish 5/5 sweep-persistence ($1.51B) but 30d cum-flow **−$161M** → mechanical −3 flow_conflict; the sweep-persistence line earns 0 points (removed 2026-05-23). Watch-only.
- **JPM** (raw 2) — sole full-gate sector leader + intent-screened accretion, CONFIRM fundamentals, but single-agent and its own sector downgraded to watch-only by the ETF tape. Cleanest *long* on the board and still a DROP.
- **DRAM** (raw −1) — bull call vertical (multileg) fully consumed by a −3 flow_conflict (30d −$64M against the long); prior wash-print history argues extra skepticism.

**Sweeps (informational, 0 points):** persistence-first — SPXW/SPY/QQQ bearish 5/5 (hedge/collar-flavored — today's SPX prints are a textbook collar: sell 7000C / buy 8000P); AMD bullish 5/5 (opening partial); SPCX bullish 5/5 opening-confirmed but a deep-OTM lotto strike. NVDA/META/AMZN bearish sweeps **demoted** (misaligned with bullish 30d cum-flow = hedge-flow signature).

## 4. LEAP Builds (6–24 months)
**EMPTY.** 0 qualifying candidates. Disqualified near-misses, all on the Gate-4 cum-premium-flow accretion test:
- **TLT** (2028 100C/120C, +212k contracts, 99.9% ask-side) — 30d flow −$108.5M bearish; call-OI build contradicted by aggregate premium flow.
- **WULF** (2028 22C/25C) — 30d −$86.8M bearish, same pattern.
- **WEN** — conviction-matrix confidence 21.4% (< 70); flow MIXED.
- **PBR** — covered-call writing + protective-put buying (hedged/covered, not directional).
- **TSLA** (2027 720C) — 30d −$451M bearish, conviction-matrix confidence 4.6%.
- **INTC** (2028 155C) — 30d −$792M bearish; build too small vs its near-dated hedging tape.
- **Audit note:** `oi-trend --days 10` returned `consecutive_build_days: 10` identically for all 14 names tested → BUILDING is non-discriminating (fires universally); the real discrimination came from Gate 2 + Gate 4.

## 5. Volatility Surface
Earnings-week vol dominates; **all IV-percentile reads PROVISIONAL** (dates_used 59–70 < 120 floor); raw `iv_rank`=100 is a screener-wide ceiling artifact. `kink_expiry` came back `null` on 12/12 names (the mechanical BACKWARDATION artifact) — kinks were re-derived by hand ex-0DTE.

| Name | Report | Real kink | VRP | Vol-surface bias | Earnings-scout | Net |
|---|---|---|---|---|---|---|
| **ON** | 08-03 | 08-07, +7.7pt (small) | −0.058 buying | BUY VOL | SKIP (shallow, 12d out) | conflicting → 0 |
| **DDOG** | 08-06 | 08-07, +24% (moderate), FLAT front | +0.438 selling | SELL VOL (cleanest) | SKIP (15d, FOMC/PCE between) | conflicting → 0 |
| **OUST** | 08-06 | 08-07, real | −0.086 buying | BUY VOL | (silent) | single agent |
| **LITE** | 08-11 | 08-14, mild bump | +0.295 selling | SELL VOL (weak) | (silent) | single agent |
| **SAP** | **07-23** | steep, front 135.8% | +0.164 (stale) | route-to-earnings | CALENDAR | pure event |
| **DRAM** | — (basket) | none (smooth decay) | ≈0 FAIR | NEUTRAL — no edge | — | contradicts multileg |
| **MXL/SIMO** | 07-23/29 | **no near-dated tenor** | stale | SKIP (artifact FLAT) | SKIP | data-gap |
| **TENX** | 08-12 | — | +3.15 extreme | DISQUALIFIED (TAIL_HEDGING skew, 74.5% implied move = real gap risk) | binary biotech | skip |

Single-contract IV outliers (whale flags, ex-0DTE): TENX $20C (09-18, IV 410%), MXL $95C (08-21), SIMO $300C (08-21). Calendar candidates (BACKWARDATION + falling front-ratio + no catalyst): **empty** — no name had a confirmed-falling front-end-iv-ratio this pass.

## 6. Risk & Correlation
- **Macro headline:** sticky core PCE (3.41%) + rising 10Y (4.63%) + strengthening USD into a **no-SEP FOMC (07-29, ~89% hold priced)**; the GDP advance (07-30) and core PCE (07-31) follow immediately. FOMC is **T+5** from today → the −0.5 one-size-step band for any undefined-risk swing.
- **Panic gate: NO-OP.** SPY front-end-iv-ratio **0.853 CONTANGO** (read at `--near-dte 7` to dodge the 0DTE-snap; near-IV 13.65 < far-IV 16.00) — the market is pricing the event stack into the *back* end, not front-panicking. VIX 16.64 LOW.
- **Correlation clusters (30d, ≥0.70 = one position):**
  - **`semis_memory` {MU, DRAM, SMH, AMD, AVGO}** — MU/DRAM 0.95, SMH/AMD 0.93, SMH/DRAM 0.92, MU/SMH 0.88. Keeper **MU** (highest raw). This is the day's dominant concentration risk.
  - **`enterprise_software` {MSFT, SAP, WDAY}** — SAP/WDAY 0.87, MSFT/SAP 0.81. Keeper **MSFT**.
  - NVDA surfaced in no ≥0.70 pair (tool top-10 truncation caveat; `sector_breakdown` returned `Unknown` for all 18 — non-functional this run).
- **Sector gate: NO-OP board-wide** — every candidate sits in an inflow sector (JPM/Financials, semis/software in Tech, GOOG/META in Comm Services); nothing adverse to persist.
- **Fundamentals verdicts (2b):** JPM CONFIRM · NVDA CAUTION (insider MSPR −98.6) · MU CAUTION (insider selling into the gap) · **GOOG VETO (reports today 07-22; beat-streak + healthy growth fight the short — bearish flow into a binary on a beating name reads as hedging, not alpha)** · META CONFIRM (earnings 07-29 = FOMC day). `fz` short-interest/analyst context unavailable on all 5 (recurring total upstream miss).
- **Debate (2c): SKIPPED** — no LOW+ name to disconfirm (empty board). Legitimate skip, not the instrumentation bug.
- **Watchlist hygiene:** yesterday's `conviction_2026-07-21` group **does not exist** (empty write-back, 16th straight) → no daily carried names, no exit candidates from the mandated group. Advisory scan of the in-window weekly group `conviction_week_2026-W28` {SNDK, NVDA, JPM, SOFI, META}: **META adverse** (bearish flow, −$39.8M, IVR 89.3, deteriorating into the 07-29 binary — exit candidate if held long); SOFI soft exit (thesis faded); SNDK watch (P/C 1.54, don't trust the "bullish" tag); NVDA supportive (+$67M, $260M DP); JPM benign.
- **Hedge sleeve: not required.** Empty book → net delta 0. Sizing anything today would skew long-tech into the T+5 FOMC / T+7 PCE stack; the empty book *is* the hedge.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**NONE.** Zero names reached MEDIUM (raw ≥ 7) or even LOW (raw ≥ 3). Top raw_score is **2** (JPM, NVDA). This is the ~17th consecutive all-DROP daily — the frozen rubric behaving as calibrated in a pre-FOMC, bearish-breadth, hedging tape, not a pipeline failure.

**Expectancy lens (advisory — C31):** `[advisory — expectancy is not yet a live sizing axis]` — no per-tier expectancy to display; nothing sized. Latest `/calibration-audit` (2026-07-18): DROP pile realized 43.3% > traded book 41.1% > sized 38.6% — the empty-board discipline continues to out-perform the sized book, so leaving the book empty is the evidence-backed action.

**Board scores (all DROP, for journaling):**

| Ticker | Raw | Dir | Class | Components | Confluence | Fund | Final |
|---|---|---|---|---|---|---|---|
| JPM | 2 | long | sector_rotation | +1 sector leader, +1 30d accretion (+$53M) | 1 agent (fail) | CONFIRM | skip |
| NVDA | 2 | long | multileg_directional | +2 diagonal (roll-caveated) | 1 agent (fail) | CAUTION | skip |
| MU | 1 | long | dealer_positioning | +1 mechanized DEX flip | 1 agent (fail) | CAUTION | skip |
| GOOG | 1 | short | bearish_flow | +1 OI build | **2 agents (PASS)** | **VETO** | **watch-only** |
| META | 1 | vol_short | earnings_vol | +1 SELL VOL (07-29) | 1 agent (fail) | CONFIRM | skip |
| MSFT | 1 | vol_short | earnings_vol | +1 SELL VOL (07-29) | 1 agent (fail) | CONFIRM* | skip |
| LITE | 1 | vol_short | earnings_vol | +1 KINKED VRP-aligned | 1 agent (fail) | NA | skip |
| OUST | 1 | vol_long | earnings_vol | +1 KINKED | 1 agent (fail) | NA | skip |
| DRAM | −1 | long | multileg_directional | +2 vertical, −3 flow_conflict | 1 agent (fail) | NA | skip |
| AMD | −3 | long | multi_day_sweep | −3 flow_conflict (sweep line 0 pts) | 1 agent (fail) | CAUTION | skip |

- **GOOG is the only ≥2-agent confluence passer** (contrarian BEARISH_EXTREME + accumulation bearish co-flag), yet scores raw 1 — its DP leg is the proven closing-cross artifact and the frozen rubric prices contrarian/single-leg bearish evidence at ~0. Fundamentals then VETO it (reports today). If the desk wants bearish expression, the honest citation is the **C19 advisory** Tier-1 FLOOR_PUT_BLOCK 330P: class `bearish_flow` clean WR **0.583 (n=132), +9.1pp vs SPY-short — 4th straight positive excess, still 0 rubric points** pending the ≥58%/≥60-day/≥2-regime graduation gate.
- **Audit fodder logged:** (a) net-vs-gross ambiguity decided points in opposite directions again — MU +$616M/0.68%-of-gross withheld vs AMD −$161M/0.78% fired −3 (escalated P1 stands); (b) SAP CALENDAR is un-scoreable under the literal "BUY VOL or SELL VOL" line; (c) `implied_move` was null fleet-wide from the quant because no scout piped a move into scoring (C43 supply-chain miss upstream — values recovered into the envelope from vol-surface/earnings prose); (d) MU DEX-flip median floor verified on a 7-session proxy.

### Conviction-scoring rubric (frozen `2026-06-12`) — embedded for audit
```
Daily conviction score = Σ:
 +1 dealer MECHANIZED DEX flip / vanna-squeeze in trade direction (verified sign change, magnitude ≥0.25× trailing-10 median)
 +3 3+ aligned accumulation signals (DP+OI+smart-positioning, block-stratified institutional) — halved to +1 unless cum_flow_30d confirms (aligned AND |≥$50M|)
 +1 multi-day OI build (oi-trend BUILDING, --days ≥5)
 +1 conviction-matrix DIRECTIONAL_LONG >70 — LEAP context only
 +1 cum-premium-flow net directional accretion 30d (intent-screened: no C28 distribution_flag; no div-capture arb)
 +1 sector-rotation single-name leader (persistence ≥0.6 AND cum_flow_30d aligned AND |≥$50M|)
 +1 earnings-scout BUY VOL or SELL VOL
 +2 multileg-strategist directional structure (term-structure-anchored)
 +1 vol-surface KINKED/BACKWARDATION with VRP-aligned bias
 +1 opex-pin-strategist top-5 (OPEX week only)
 -2 contrarian overcrowded long with rising pc-z (VRP positive)
 -3 flow_conflict (30d cum-flow clearly opposite dominant class) | -1 flow_conflict_lite (MIXED / bottom-quartile) — mutually exclusive
 [TIER GATES, risk 2d, not points] -1 correlation cluster | -1 regime conflict | fundamentals VETO→watch-only | event-risk | debate | rubric_regime half-cap
Tiers: ≥9 HIGH (full) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 DROP.  OUT-OF-REGIME → all sizes half-capped.
```

## 8. Watch-only — single signal, no confluence
For journaling, not entry. Every long candidate today is single-agent:
- **MU** (dealer DEX flip), **NVDA** (multileg diagonal), **AMD** (bullish sweeps), **JPM** (sector leader), **AVGO** (DEX flip, NEUTRAL), **SMH** (dealer LONG lean), **DRAM** (multileg vertical), **SPCX** (opening sweep, lotto strike).
- Vol (single agent): **OUST/LITE** (vol-surface), **META/MSFT** (earnings SELL VOL, 07-29 = FOMC day), **ON/DDOG** (vol-surface vs earnings-scout SKIP conflict), **SAP** (calendar, reports 07-23).
- Bearish (single agent): **WDAY** (pc-z 2.11, dp_distribution, +1 OI build −1 flow_conflict_lite = raw 0), **LLY** (price-vs-flow divergence), **SN** (Tier-1 opening 140P, C19 advisory).
- **GOOG** — the lone ≥2-agent name — moved to §7 (VETO, watch-only).

---
*Rubric frozen `2026-06-12`. Sizing OUT-OF-REGIME (half-capped). ~17th consecutive all-DROP daily; watchlist write-back empty (17th straight). No sized positions. Deep-dive hand-off skipped (no HIGH-tier names).*
