# Daily Market Analysis — 2026-06-29

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / **PULLBACK_IN_UPTREND** — SPY 741 (below 20-SMA 742.83, above 50-SMA 735.14, −1.8% 30d, −2.55% from 90d high); VIX 17.65 (MID); breadth bearish-leaning (37.9% bullish flow; `fz` 229 adv / 273 dec, 45.5% green). VRP FAIR (no index edge). SPY/QQQ next-session gamma **NEGATIVE** with a positive-gamma pin magnet sitting *at* spot. Sector lean: Tech-IN / Healthcare-OUT (value→growth, low confidence). **Front-end IV backwardation (SPY ratio 1.122 > 1.10) — the panic gate is live market-wide into NFP.**
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half` (P0.6 guard; freeze-lift cannot run — 0 post-freeze HIGH/MED resolved).
- **Next-session GEX (SPY/QQQ):** SPY — NEGATIVE-gamma · ZGL 764.2 (reliable) · call wall **741 (= spot, pin magnet)** / put wall 725 · downside acceleration shelf at **735 (= 50-SMA)** → pin-until-it-isn't, iron-fly bias with a hard tail below 735. QQQ — NEGATIVE-gamma · ZGL 749.94 · call wall **725 (= spot)** / put wall 715 · weaker pin (front-end backwardation), half-size. Advisory, see §2.
- **Top swing build:** **None at conviction.** Sole floor-clearer **BABA** (raw 3, LOW) → **WATCH-ONLY** after panic −1 + fundamentals CAUTION −1 + event-risk −1 + a failed debate (bear 0.75 ≥ bull 0.55). The +$330.8M/30d bid is unresolvably ambiguous (accumulation vs distribution-into-relief at a 52-wk low).
- **Top LEAP candidate:** **None.** Long-dated tape is hedge-dominated; lead near-miss ERAS is a parabolic, litigation-overhung, likely-HTB reject. §4 is an explicit no-edge section.
- **Biggest risk:** No new-book risk to hedge (post-gate book ≈ flat). The live risk is the **carried `conviction_2026-06-26` longs (SMH / MSFT / UBER) rolling over** into the pullback (SMH P/C 5.23, MSFT IV-rank 100, both net-bearish today) — trim the exit candidates rather than layer a new hedge. Keep powder dry into NFP (T+3).

> **Desk verdict: a genuine no-edge day.** Zero HIGH/MEDIUM conviction. The defensive tape (TRANSITIONAL pullback + bearish breadth), front-end backwardation into a 3-day-out NFP print, an out-of-regime rubric, and a thin candidate set that the gates correctly hollow out all point the same way: **stand aside, keep the book flat, wait for the print.** The only desk action with edge today is housekeeping the carried longs.

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend PULLBACK_IN_UPTREND. SPY 741, below the 20-SMA (742.83) but holding the 50-SMA (735.14). Breadth: 2,366 bullish vs 3,879 bearish flow tickers (37.9% bullish) — a bearish-leaning tape under a green-ish index.
- **Per-index gamma (current-state EOD book; forward read in §2):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 740.66 | 764.2 (reliable) | net short (−γ) | NEGATIVE | 741 (at spot) | 725 (shelf 735 = 50-SMA) |
| QQQ | 723.41 | 749.94 (reliable) | net short (−γ) | NEGATIVE | 725 (at spot) | 715 |
| IWM | ~298 | degenerate/noisy | ~flat | (whipsaw) | — | — |

- **`uw options-flow dte-volume-share`:** 0DTE 37.1% · weeklies 25% · monthlies 20.2% · LEAPs 5.1%. regime_hint BALANCED — mixed retail/institutional; not retail-dominated (0DTE < 50%), so swing-book eligible.
- **`uw historical vrp` (SPY):** FAIR — IV30 0.1526 ≈ realised 0.1566 (VRP −0.004). No premium-selling tailwind at the index; vol edge is single-name only.
- **Macro backdrop (`scripts/fred_macro.py`):** Yield curve normal (10Y-2Y +0.28); core CPI 2.96% YoY, core PCE 3.41% (sticky); unemployment 4.3%, payrolls +172k; 10Y 4.38% (falling −0.10/30d); USD strengthening; fed funds 3.63%. **Forward event risk:** June NFP **Thu Jul 2** (T+3, day before the Jul-3 market holiday → weekend gap risk), June CPI **Tue Jul 14** (T+10), PPI ~Jul 15, FOMC **Jul 28-29** (T+21).

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book read forward as the prior for tomorrow's open. Prose-only, **0 rubric points**, no backtested predictive claim (validation lives in `/weekly-analysis`). SPY & QQQ only.

Both indices climbed out of a 5-session FULLY_NEGATIVE stretch (06-22→06-26) into a **one-session-old NEGATIVE regime** — a *fresh, unstable* prior, not a held one.

| Index | Regime | ZGL | Call wall | Put wall | Next-session structure bias |
|---|---|---|---|---|---|
| **SPY** | NEGATIVE (−γ; spot 740.66 < ZGL 764.2) | 764.2 (reliable) | **741 (+0.05%, at spot)** | 725 (−2.1%); **shelf 735 (= 50-SMA)** | Pin-until-it-isn't: +γ magnet at 741 supports mean-reversion / iron-fly **while spot ≥ 735**; a break of 735 drops into the 735→725 air pocket = short-gamma acceleration. |
| **QQQ** | NEGATIVE (−γ; spot 723.41 < ZGL 749.94) | 749.94 (reliable) | **725 (+0.22%, at spot)** | 715 (−1.2%) | Same shape, weaker pin — front-end backwardation (0DTE IV 1.49× VIX) amplifies the short-gamma tail. Half-size; downside wing below 715. |

**Mandatory caveats:** (1) EOD is a prior, not a target — today's dominant 06-29 expiry ($794M SPY / $789M QQQ premium) rolls off tonight and partially resets the at-spot magnets on the open. (2) **Gap risk voids the read** — NFP Jul 2 (T+3) is a known event-gap window; near-dated books are already put-skew-hedged. (3) Fresh/unstable regime — one session out of 5 straight FULLY_NEGATIVE days; a down gap can snap it back (ZGL → null). (4) ETF book, not the cleaner SPX/NDX index book. (5) Cannot isolate the D+1 expiry — this is the 0–45d proxy.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — the validated stack)
The walls above are a *map*, not a pin (wall-as-magnet and every directional 0DTE signal backtested NO_GO). What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, NOT guaranteed (validation sample has no vol shock — the short-vol left tail is UNSAMPLED). Backtest verdict: **GO_PREMIUM_SELL_INTRADAY** (both).

| Index | Sell premium | Vol state / VIX | Implied move | Exp. range | Size | Structure | PnL basis |
|---|---|---|---|---|---|---|---|
| **SPY** | yes | MID / 17.65 | 0.94% | 0.76% | full (1.0×) | iron fly / short straddle @ 740.95, wings ±0.76% | gross +0.317% / **net +0.217%** of spot notional (n=54, open-win 94.4%) |
| **QQQ** | yes | MID / 17.65 | 1.65% | 1.24% | **half (0.5×)** | iron fly / short straddle @ 723.51, wings ±1.24% | gross +0.426% / **net +0.326%** (n=54, open-win 88.9%); **caution: front-end backwardation, event/gap risk** |

- **When:** enter at/after the open once the gap resolves; **hold to the close, never carry overnight** (overnight entry backtested negative). If it gaps beyond the wings, stand aside.
- **Lead with net, not gross:** the figures are % of underlying spot notional, GROSS; reported net of an assumed 0.10% round-trip cost. A negatively-skewed short-vol seller's gross win-rate overstates the edge. **Stand-aside trigger: NFP Jul 2 gap or front-end backwardation spiking further** — QQQ already carries the backwardation caution.

## 2a. Swing Dealer Positioning (1–4 weeks)
A **synchronized bullish mechanized DEX sign-flip fired 6/29** across SPY, QQQ, and TSLA (net dealer delta flipped from sustained-negative runs to positive on the same session):

| Name | DEX flip | Magnitude (× trailing-10 median) | Vanna squeeze | Swing bias |
|---|---|---|---|---|
| **TSLA** | TRUE (6/26 −1.09B → 6/29 +9.09B) | **2.0×** (strongest) | FALSE (call-heavy book — wrong side) | LONG (but +8.3% move concurrent; continuation only if positioning holds) |
| **QQQ** | TRUE (6/26 −25.4B → 6/29 +13.1B) | 0.52× | FALSE (call-heavy) | LONG (front-end backwardation 1.27 = acute fear) |
| **SPY** | TRUE (6/26 −31.8B → 6/29 +7.74B) | 0.27× (borderline) | FALSE (put-heavy, building not armed) | LONG (tentative; backwardation 1.12) |
| NVDA | **FALSE** — net_dex negative 5 straight sessions | — | — | NEUTRAL/SHORT-lean (the laggard that did NOT flip while QQQ ripped) |
| AMD | FALSE — persistent positive *level* (beta, not a flip) | — | — | no scoreable flip |
| IWM | FALSE — whipsaw, no clean run | — | — | NEUTRAL (skip) |

**Critical temper:** every flip lands in a still-**negative-gamma**, **backwardated** tape with VIX choppy (no ≥3-session decline → no vanna squeeze anywhere), NFP 3 sessions out, and FOMC inside the window. This is a **fragile bounce**, not clean trend-continuation, and the framing is practitioner hypothesis (Karsan/SqueezeMetrics), not validated edge at this horizon. None of these single-name flips earned a second confluence agent → they stay **watch-only** (see §8). NVDA's non-participation is the notable divergence.

## 2b. Sector Rotation
- **Rotation regime:** **value→growth, LOW confidence.** The one durable, cross-confirmed axis is **Tech-IN / Healthcare-OUT**. Not a clean macro-quadrant rotation — undertone is a late-cycle "quality barbell" (Tech megacaps + defensives bid; cyclicals + Healthcare bleed), consistent with PULLBACK + strengthening USD + falling 10Y.
- GICS persistence is 1.0/INFLOW for all 11 sectors (non-discriminating in a trending tape) → the call rests on the market-relative bar + the ETF instrument tape.

| Sector | Disposition | Cross-confirm |
|---|---|---|
| **Technology** | ROTATING IN (high conviction) | SMH +$146.6M / IGV +$79.5M / XLK +$7.0M all bullish — GICS + ETF AGREE |
| **Healthcare** | ROTATING OUT (high conviction) | XLV −$2.7M / XBI −$6.35M bearish — AGREE; the +$345M single-day inflow is noise (5d = −$16M) |
| Comm Services | watch-only (downgraded) | XLC −$0.47M bearish vs GICS +$744M — DISAGREE (mega-cap-concentrated) |
| Industrials | watch / lean-out | XLI −$1.85M bearish vs GICS +$338M — DISAGREE |
| Energy / Materials | watch-only | XLE +$18.4M / GDX +$33M inflow but 1-day / macro-hedge |

**ETF flow tape (advisory, 0 points)** — top inflow: **SMH** (+$146.6M, above-ask block accumulation), **IGV** (+$79.5M), **GDX** (+$33M, gold macro-hedge); top outflow: **XBI** (−$6.35M, deep-ITM put buys), **XLV** (−$2.71M, downside put accumulation), **ITB/XLI/XLF/XLC** (broad cyclical/financial bleed). Only **GLW** (Tech, 30d +$78M) and **BABA** (Discretionary, 30d +$330.8M) cleared the full 3-part single-name +1 gate; **TSLA (30d −$366.6M) and AMZN (30d −$279.5M) are counter-trend and were NOT featured.**

## 3. Swing Setups (1–6 weeks)
**No conviction-tier swing setups today.** No name survived the gate stack with a sized directional position. The candidate set and why each failed:

### 3a. Long swings (regime-aligned)
| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **BABA** | 3 (LOW) | Persistent two-horizon bullish premium (+$330.8M/30d, +$680.9M/90d) + Discretionary sector-leader, but the bid sits against falling price at a 52-wk low | Sep-18 100 bullish risk-reversal (call leg ambiguous — could be a short straddle) | Stay flat / short-bias on a daily close **< ~$93** (under 06-26 52-wk low); re-arm only > $100 on volume + insider selling stops + scandal de-escalates | **WATCH-ONLY** |
| AMZN | −1 (DROP) | Jan-27 bullish call ratio, but **killed by flow_conflict** (cum_flow_30d −$279.5M counter-trend) + DP mega-distribution (buy_ratio 0.256) + heavy insider selling | — | — | **DROP** |
| CG | 1 (DROP) | Single-occurrence bullish call diagonal, no flow confirmation; **fundamentals VETO** (4/4 miss streak, rev −28.9%/eps −50.6%) | — | — | **WATCH-ONLY (VETO)** |

### 3b. Short / fade swings (defined risk only)
**No tradeable shorts.** Contrarian-scanner found zero high-conviction fades — front-end backwardation into NFP + FAIR VRP gate every premium-fade. One scoring flag only: **AMD −2 contrarian penalty** (crowded long, pc-ratio z +2.227 BEARISH_EXTREME rising across 4 dated points) — but NOT a tradeable short (net premium still +$27M bullish; this is a put *hedge* bid layered on conviction, and single-name P/C extremes predict continuation). Sector-rotation flags **UNH / RVMD / PCVX** as Healthcare-OUT short-watch (UNH 30d −$49M narrowly misses the $50M floor) — watch-only.

**Near-term sweeps (informational, 0 rubric points):** the persistence book is dominated by index/mega **hedge** flow (SPXW/QQQ/SPY/TSLA/NVDA bearish 5/5 but cum_flow MIXED — demoted). Genuinely directional but co-flag-free (LOW-tier): SNDK (bullish, but protective put build on a parabolic), AMD/INTC (two-way hedge books, not clean shorts), MSTR (in flux). Best single-day bullish whale: **CG** (C50 Sep, 102× volume) — but VETO'd on fundamentals. The DTE3 urgency across the book is NFP-Jul-2 straddle/gap positioning, not directional momentum.

## 4. LEAP Builds (6–24 months)
**No qualifying LEAP-grade conviction builds.** The long-dated tape (5.1% DTE share, thin) is **hedge-dominated** — put-side ETF/single-name protection (IGV, TLT, XLV, IBIT, NOW/PATH/LYFT/NOK), fitting the pullback regime. Disqualified near-misses:
- **ERAS** — reaches 6-of-9 data gates but is a **textbook reject**: parabolic +79%/30d blow-off on top of a 700–800% run (not stealth accretion), likely-HTB borrow/financing artifact on deep-ITM C10 accretion, active Revolution-Medicines litigation overhang (binary), and smart money already distributing ($44.5M biotech-fund sale into the rally); the structure is a capped C10/C35 spread, not an outright LEAP.
- **GENI** (build_days 3 < 5 + conviction-matrix DISTRIBUTION), **BB** (bid-dominant = call-writing, not a directional long) — both drop at source.

## 5. Volatility Surface
The whole complex is in mechanical **NFP-Jul-2 front-week backwardation** (every name prints `BACKWARDATION, kink_expiry: null` — the documented pre-event classifier degeneracy). IV-rank "100" is **PROVISIONAL** (only 54 populated percentile days) — z-scores quoted instead.

- **AMAT — backwardation calendar candidate** (the only name with a *falling* front-end ratio, 2.037→1.440): sell the OPEX-rich 07-17 tenor (118.7%) vs long 08-21 (93.7%, owns earnings vega). VRP FAIR (+0.0158) caps it to term-shape edge only; size small. Part of a 4-name semicap vol cluster (GLW/AMAT/LRCX/WDC = one exposure).
- **MRNA — cleanest SELL VOL** (VRP +0.148 PREMIUM_SELLING, IV 92% vs realised 77%): iron condor expiring **07-31** (before the 08-07 earnings binary), harvesting the rich post-NFP/pre-earnings tenor. Size small (biotech gap risk).
- **PEP — SELL VOL (vol lane, see §7):** the lone clean earnings kink that isolates the 07-09 print from CPI Jul-14 — Jul-10 iron condor. CONFIRMED by fundamentals.
- **Do-NOT-trade warnings:** **CMCSA** (front-end ratio exploded 1.047→2.357 in one session = fresh news or wing-contamination artifact), **SLS** (VRP +0.82 is binary-clinical tail comp, not free premium), **GLW** (the −0.0747 VRP is a one-day +15.67%-spike artifact in the *realised* leg — IV is not actually cheap). The IV-100 cluster is a **macro/CPI masquerade**, not in-window earnings vol.

## 6. Risk & Correlation
**Macro headline:** sticky inflation (core PCE 3.41%, core CPI 2.96%) with a falling 10Y (4.38%) and strengthening USD; curve normal. **Forward event risk:** NFP **Jul 2 (T+3)**, CPI **Jul 14 (T+10)**, PPI ~Jul 15, FOMC **Jul 28-29**. The 3-day-out NFP (last session before the Jul-3 holiday) is the binding near-term binary.

- **Panic gate (live):** SPY front-end IV ratio **1.122 (BACKWARDATION, > 1.10)** — fires −1 tier market-wide despite a benign headline VIX (17.65) and FAIR VRP. Consistent with NFP 3 days out + the pullback.
- **Correlation:** `uw risk portfolio-correlation [BABA, AMZN, CG, PEP]` → `high_correlations: null`. No pairwise ≥ 0.70, none in the 0.60–0.70 soft-watch band. No cluster gate.
- **Fundamentals verdicts (top names):** **BABA CAUTION** (−1) — worsening 4/4 miss streak, 52-wk low 06-26, Anthropic IP-theft accusation escalated to Senators Warren/Scott, same-day CFO/C-suite selling ($2.13M) vs a stale +MSPR = distribution dressed as accumulation; **AMZN CAUTION** (−1) — heavy persistent insider selling corroborates the distribution kill (business healthy → profit-taking, not collapse); **CG VETO** — 4/4 miss streak + rev −28.9%/eps −50.6% contradict a bullish diagonal; **PEP CONFIRM** — SELL VOL condor corroborated.
- **Debate-disconfirmation cut:** **BABA bear 0.75 ≥ bull 0.55** — the +$330.8M bid is equally consistent with distribution-into-relief (CFO selling + 52-wk low + unpriceable Senate-level scandal); the ambiguous call leg may be a short straddle; multileg_directional has no backtest substrate. Debate did NOT clear the trade.
- **Breadth cross-check (`fz`, advisory):** 229 advancers / 273 decliners, **pct_green 45.5%** — more decliners than advancers despite Tech net-call-premium dominance. A mild **distribution / breadth-divergence tell** under a green-ish index; advisory, does not change sizing.
- **Adverse-flow exits (carried `conviction_2026-06-26`):** **SMH** (P/C 5.23, IV-rank 90, net-bearish), **MSFT** (net −$41.2M, IV-rank 100), **UBER** (net-bearish, mild) → **EXIT candidates** — the carried AI/semi long complex is rolling over into the pullback. NVDA (net +$16M, on-thesis) and IGV (balanced) → HOLD.
- **Hedge sleeve:** **none required.** Post-gate new book ≈ flat (BABA watch-only, AMZN/CG not sized, PEP delta-neutral). The real risk action is trimming the carried exit candidates, not layering a new hedge.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**None — zero HIGH/MEDIUM names today.** The full audited book (all four scored names, none surviving to a sized directional position):

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no resolved per-tier expectancy is quoted this run — the most recent `/calibration-audit` (2026-06-27) found the tiers inverted (HIGH 0.143, regime-invariant) and long edge UPTREND-ONLY (zero in pullback, p=0.79). In the current PULLBACK regime there is **no proven long alpha** — the book gets no benefit-of-the-doubt, reinforcing the flat posture.

| Ticker | raw | tier | dom. class | win_rate (n, src) | pre-risk | fund. | bull/bear | gates applied | final | invalidation |
|---|---|---|---|---|---|---|---|---|---|---|
| **BABA** | 3 | LOW | multileg_directional | NA (substrate) | starter | CAUTION | 0.55 / 0.75 | panic −1, fund −1, event_risk −1, debate −1, rubric half-cap | **WATCH-ONLY** | close < ~$93 (52-wk low) |
| **PEP** | 1 | DROP→vol | earnings_vol | NA | starter | CONFIRM | n/a | panic −1; rest no-op/exempt | **minimal-starter (vol)** | Jul-10 kink flattens; guide-down gap beyond wings |
| **AMZN** | −1 | DROP | multileg_directional | NA | skip | CAUTION | n/a | flow_conflict −3, fund −1, panic −1 (moot) | **DROP** | — |
| **CG** | 1 | DROP | multileg_directional | NA | skip | **VETO** | n/a | fundamentals VETO → watch | **WATCH-ONLY** | — |

**BABA score components:** +1 sector-leader (sector-rotation, `sector-flow-persistence`: Discretionary persistence 1.0 ∧ cum_flow_30d +$330.8M aligned ∧ ≥$50M) · +2 multileg-directional (multileg, `hot-chains multileg`: Sep-18 bullish risk-reversal, CONTANGO belly). Σ = 3. dominant `multileg_directional` has no backtest substrate → win_rate NA; the informational clean `bullish_flow` class WR is **0.489 (n=141)** — sub-0.50, no class edge.

**Deep-dive (top conviction name):** BABA `uw historical trend` (10d) shows price **102.60 → 95.51 (−6.9%)** — a downtrend to the 52-wk low, *not* a base; flow_direction labels 8/2 bullish but price fell (the accumulation-vs-distribution ambiguity made concrete). Genuine upside OTM call OI is building (Sep 120/145C, Dec 100/140C), so the bid is real — but it sits inside a falling tape with the disconfirmation stack above. Earnings ~Aug-27/Sep-04 (sources differ; both ~60d out, outside the swing horizon). Yahoo fundamentals 401 (known breakage).

**Deep-dive hand-off:** skipped — no HIGH-tier names. **Step 6.5 batch-scan skipped** — no HIGH/MEDIUM (raw ≥ 7) book to scan.

### Conviction rubric (frozen `2026-06-12`) — embedded for audit
Tiers: ≥9 HIGH (full) · 7–8 MED (half) · 3–6 LOW (starter/watch) · ≤2 drop. Key lines: +3 accumulation conjunction (halved to +1 if cum_flow doesn't confirm sign+≥$50M); +1 mechanized DEX flip (verified sign change, not level); +1 multi-day OI build; +1 conviction-matrix DIRECTIONAL_LONG>70 (LEAP-only); +1 cum_flow 30d accretion (intent-screened); +1 sector-leader (persistence≥0.6 ∧ cum_flow aligned ∧ ≥$50M); +1 earnings BUY/SELL VOL; +2 multileg directional (term-structure-anchored); +1 vol-surface KINKED/BACKWARDATION VRP-aligned; −2 contrarian crowded-long rising-z; −3 flow_conflict (30d clearly opposite) / −1 lite (MIXED). Tier gates (Step 2d, not score_components): −1 tier correlation cluster; −1 tier regime conflict. **OUT-OF-REGIME → all sizing capped at half (P0.6).**

## 8. Watch-only — single signal, no confluence
Surfaced by one agent (failed the ≥2-agent confluence gate) or carrying active disconfirmation — listed for journaling, **not for trade entry today**:
- **GLW** — sector-rotation +1 leader (Tech, 30d +$78M) + RS new-high (+15.67%), BUT accumulation-hunter flags **DP mega-distribution** (buy_ratio 0.262) and vol-surface warns the −VRP is a one-day-spike artifact + lottery-call flag; IV-100 is a macro masquerade, not earnings. Single positive agent + two warnings → watch-only.
- **TSLA** — dealer-positioning +1 (strongest DEX flip, 2.0× median) BUT sector-rotation counter-trend (30d −$366.6M), sweep hedge/MIXED, the +8.3% move is concurrent. Single positive agent.
- **CSCO** — accumulation-hunter sole gate-passer (DP mega buy-ratio 1.000 / $554M, 5d OI BUILD into 124/130/135C, conviction-matrix 51.8% barely clears) but cum_flow_30d mildly bearish (−$4.47M) and only one agent. Defended at $117.70.
- **MRNA** — vol-surface SELL VOL (07-31 condor) — single-agent vol read (see §5).
- **AMAT** — vol-surface backwardation calendar — single-agent (see §5); semicap cluster.
- **UNH / RVMD / PCVX** — sector-rotation Healthcare-OUT short-watch (UNH 30d −$49M misses the $50M floor).
- **SNDK / INTC / MSTR** — sweep-tracker persistent (Tier-A) but co-flag-free (sweep-only, LOW-tier).
- **AMD** — contrarian −2 penalty flag (crowded long, rising pc-ratio z); not a tradeable long or clean short.
