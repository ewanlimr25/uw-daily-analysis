# Weekly Market Intelligence — Week of 2026-06-22 (ISO 2026-W26)

## Executive Summary
- **Week regime + WoW Δ:** TRANSITIONAL / CHOPPY — *held* all week (same label Monday→Friday). SPY closed 728.99, below both the 20-day (743.6) and 50-day (734.35) SMA, −2.86% over 30 days and −4.13% off the 90-day high. Breadth improved at the margin (options bullish_pct 35.2%→38.2%) but remains bearish-leaning. VRP is **PREMIUM_BUYING** (SPY −2.74, QQQ −2.63): realised vol is running above implied — vol is cheap, premium-selling is disfavoured.
- **Rubric regime status:** **OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half.** The 2026-06-12 freeze block is active; no tier carries a validated ranking claim until a `/calibration-audit` records ≥30 resolved post-2026-06-12 calls.
- **Signal performance:** **12 of 26 resolved (hit rate 12/26 = 46.2%); 14 INCONCLUSIVE excluded; 40 total calls in universe (40 envelope-anchored, 0 reconstructed).** A sub-coin-flip week — the daily book's tech/semis shorts landed but its vol-short book and late-week large-cap shorts lost. Nearly all calls were DROP-tier watch-only, correctly flagged low-conviction.
- **Top swing build for next week:** **QQQ SHORT — STARTER** (the *only* live call). Mechanized DEX flip (6/23) + 54-day PUT OI build in a FULLY_NEGATIVE GEX book; express as a defined-risk bear put spread through NFP. Invalidation: a close back above 724, or a VIX-collapse vanna squeeze off the 705 put wall. win_rate 0.519 (n=135), market_excess +14.8pp. Tier LOW.
- **Top LEAP build:** **NONE.** leap-positioning-radar returned zero qualifiers — every bullish-funnel name failed the 90d/30d cum-flow gate in the choppy tape; roll activity was protective puts, not fresh LEAP-call accumulation.
- **Biggest emerging risk:** a tight **tech/semis correlation cluster** (QQQ/SMH 0.94, AMAT/SMH 0.87, SMH/MU 0.87, QQQ/MU 0.82) — the entire candidate book is one bet — compounded by **NFP on Jul-2 (T+4)** inside the swing horizon and a holiday-shortened week (Jul-3 early close).

## 0. Week in Review — Intra-Week Signal Performance

Universe = the union of `calls[]` across this week's five daily `decision.json` envelopes (hindsight-free, survivorship-free; thesis direction read from the pre-committed envelope). INCONCLUSIVE = |move| < 0.5×ATR(14). All 40 calls were envelope-sourced (no reconstruction). Directional grades use `uw historical trend` close-to-close vs an ATR(14) proxy; volatility grades use realised-move magnitude.

| Ticker | Direction | Source (envelope) | Move vs ATR | Flow/OI | Grade | Note |
|---|---|---|---|---|---|---|
| MU | vol_long | 2026-06-22 | 1.07× | bearish 06-26; IVR 78 | **WIN** | large realised move (earnings gap) |
| SPY | short | 2026-06-22 | 2.56× | bearish all week | **WIN** | clean directional |
| WDC | vol_short | 2026-06-22 | 3.85× | bearish; IVR 97 | **LOSS** | huge realised move |
| FDX | vol_short | 2026-06-22 | 1.68× | earnings-adjacent | **LOSS** | sold the beat |
| CBRS | vol_short | 2026-06-22 | 3.03× | bearish | **LOSS** | biotech gap |
| BSX | long | 2026-06-22 | 0.16× | mixed | INCONCLUSIVE | no resolution |
| ACN | neutral | 2026-06-22 | 0.83× | bearish, post-gap | **LOSS** | range thesis failed |
| NBIS | short | 2026-06-22 | 4.28× | bearish, OI falling | **WIN** | strong breakdown |
| SNDK | short | 2026-06-22 | 1.25× | bearish premium | **WIN** | pulled back |
| TSLA | short | 2026-06-22 | 2.67× | bearish, net put | **WIN** | clean |
| NVDA | long | 2026-06-22 | 4.05× | bearish; semis weak | **LOSS** | 4× ATR wrong way |
| CDNS | short | 2026-06-22 | 2.02× | bearish; EDA weak | **WIN** | clean |
| MU | vol_short | 2026-06-23 | 1.09× | reversal 06-25 | **LOSS** | large move = vol_short loss |
| NFLX | short | 2026-06-23 | 0.70× | mixed; recovered | **LOSS** | moved up vs short |
| IWM | short | 2026-06-23 | 1.60× | small-caps rallied | **LOSS** | 1.6× ATR against |
| INTC | long | 2026-06-23 | 0.65× | bearish; underperf | **LOSS** | wrong way |
| NVDA | short | 2026-06-23 | 1.88× | bearish; semis lower | **WIN** | continuation |
| SMH | long | 2026-06-23 | 0.47× | choppy | INCONCLUSIVE | < 0.5× ATR |
| CART | long | 2026-06-23 | 1.44× | bullish; OI building | **WIN** | grind higher |
| QQQ | short | 2026-06-23 | 0.59× | bearish | **WIN** | ≥0.5× in direction |
| SPCX | long | 2026-06-24 | 0.18× | thin | INCONCLUSIVE | sparse |
| NUVL | long | 2026-06-24 | 0.02× | tender-pinned | INCONCLUSIVE | VETO'd at issue (GSK tender) |
| BJ | long | 2026-06-24 | 0.80× | mildly bullish | **WIN** | defensive consumer |
| SMH | short | 2026-06-24 | 0.33× | choppy | INCONCLUSIVE | contradicts 06-23 long |
| IREN | short | 2026-06-24 | 1.10× | bearish; miner down | **WIN** | in direction |
| NKE | vol_short | 2026-06-24 | 1.23× | bearish drift | **LOSS** | realised move too big |
| SNDK | long | 2026-06-24 | 1.21× | bullish bounce | **WIN** | reversed up |
| RCL | long | 2026-06-24 | 0.33× | mixed | INCONCLUSIVE | < 0.5× ATR |
| MU | long | 2026-06-25 | 1.10× | bearish 06-26 | **LOSS** | sold off; 1-day window |
| META | short | 2026-06-25 | 0.72× | recovered | **LOSS** | up vs short |
| AMZN | short | 2026-06-25 | 1.25× | bounced | **LOSS** | against thesis |
| MSFT | short | 2026-06-25 | 2.41× | surged | **LOSS** | large rally vs short |
| UBER | long | 2026-06-26 | — | — | INCONCLUSIVE | 0-day window |
| IGV | short | 2026-06-26 | — | — | INCONCLUSIVE | 0-day window |
| STZ | vol_short | 2026-06-26 | — | — | INCONCLUSIVE | 0-day window |
| TSCO | vol_short | 2026-06-26 | — | — | INCONCLUSIVE | 0-day window |
| ABT | vol_short | 2026-06-26 | — | — | INCONCLUSIVE | 0-day window |
| INTC | short | 2026-06-26 | — | — | INCONCLUSIVE | 0-day window |
| FLEX | short | 2026-06-26 | — | — | INCONCLUSIVE | 0-day window |
| NOW | long | 2026-06-26 | — | — | INCONCLUSIVE | 0-day window |

**Read:** Monday–Tuesday tech/semis shorts (SPY, NBIS, TSLA, CDNS, SNDK-short, NVDA-short from 06-23) were the week's clean wins. The drag came from (a) the **vol_short book** — WDC, FDX, CBRS, MU-vol_short and NKE all realised moves above the 1× ATR threshold in a week that was anything but quiet, exactly the wrong bet in a PREMIUM_BUYING tape; and (b) the **late-week large-cap shorts** (META, AMZN, MSFT, issued 06-25) that were immediately bid up on Friday's software rotation. The same name (NVDA) carried both a winning short and a losing long from adjacent issue dates — a structural tell that competing directional calls were emitted before resolution. The saving grace: nearly all of these were DROP-tier watch-only, never sized with capital.

## 1. Regime & WoW Delta

The week opened and closed in the same place: **TRANSITIONAL — "mixed signals, reduce size, wait for clarity," trend CHOPPY.** There was no regime improvement to trade into. SPY held below both the 20- and 50-day moving averages all week; the 30-day change sits at −2.86% and the index is −4.13% off its 90-day high. The only WoW delta worth noting is a marginal lift in options breadth (bullish_pct 35.2%→38.2%), which leaves flow still tilted bearish.

**VRP — PREMIUM_BUYING.** SPY VRP −2.74, QQQ −2.63: 30-day realised vol is running above 30-day implied. Vol is *cheap* relative to what the market is actually delivering. This is a premium-*buying* week — it favours long-gamma / calendar structures (vol-surface-scout, earnings-scout) and penalises premium-selling fades (contrarian-scanner's whole book was muted by this gate).

**DTE volume share (market-level): BALANCED.** 0DTE share ~0, weeklies 20.6%, monthlies 16.8%, LEAPs 4.7%. No retail-tape skew, no institutional LEAP surge — neither the swing nor LEAP book earns a structural tailwind from the tape.

**Macro backdrop.** Core CPI 2.96% / core PCE 3.41% YoY — sticky, still above target. Yield curve normal (10Y−2Y +0.31). 10Y at 4.4% and *falling* (the bond market pricing deceleration); USD strengthening; fed funds 3.63%; unemployment 4.3%, payrolls +172k. The mix is **stagflation-lite** — sticky inflation against softening growth tells — which structurally penalises directional conviction. **Forward event risk (next two weeks):** ISM Manufacturing ~Jul-1; **June NFP ~Jul-2 (HIGH**, advanced for the Jul-4 holiday); US market closed / early-close Jul-3; ISM Services ~Jul-6; **June CPI ~Jul-14 (HIGH)**. Any short-DTE directional trade is gated around the Jul-2 payrolls print.

**Implication for next week's bias:** lean defensive and small. The tape is choppy, vol is cheap (own gamma, don't sell it), and two Tier-1 macro prints land inside the first two weeks. This is a stand-aside-and-pick-spots regime, not a press-the-trend one.

## 2. Sector Rotation

**Rotation regime call: value→growth (medium confidence).** On the GICS persistence layer all 11 sectors printed sign-consistent inflow (persistence_score 1.0) except Consumer Cyclical (0.6, the lone net-outflow at −$210M on the week) — a "uniform-high-absolute-gate" artifact the audit flagged, so the market-relative bar was applied. Only **Technology** survives the full cross-confirm: GICS persistence 1.0 + week total ~$19.9B *and* the top-3 ETFs by net premium (XLK, SMH, IGV all bullish) agree. The clean direction is a growth/AI-capex premium bid.

**The important caveat — the rotation call fights the single-name flow.** sector-rotation reads Technology *in* on gross premium, but dealer-positioning fired mechanized `dex_flip_short` on QQQ/NVDA/TSLA, multileg flagged bearish structures across IGV/SMH/NFLX, and sweeps confirmed bearish semis (SMH/INTC/MRVL). The reconciliation: the bullish "Tech in" is *gross* premium concentrated in software/enterprise single names (NOW/IBM/PANW/CRM, cum_flow_30d ≥ $50M), while the bearish signals are concentrated in *semis and indices*. Even the software ETF (IGV) carries a $74M Jan-2027 bear put spread. Treat "Tech in" as a software-specific, single-agent read, not a green light on the sector.

**Watch-only (GICS inflow, ETF disagrees):** Healthcare (LLY dominant, +$93.8M 30d, but XLV/XBI bearish), Industrials (XLI bearish), Communication Services (META single-name driven, XLC bearish). None upgrade to a rotation call until the ETF wrapper confirms.

**ETF flow tape (advisory — strengthens the conditional sector-leader +1, no rubric points):**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| SMH | inflow (+$128.7M) | 5/5 bullish | premium-to-ask blocks (accumulation) | PUT sweeps dominate (long-with-hedge) | agree (Tech) | — (semis basket) |
| IGV | inflow (+$76.9M) | 5/5 bullish | $108M creation/redemption print | net PUT-dominant ($74M Jan-27 macro hedges) | agree (Tech) — conviction reduced | — |
| GDX | inflow (+$30.8M) | 5/5 bullish | mixed vs-mid | long-dated put structures | n/a (Materials) | — |
| XBI | outflow (−$11.4M) | bearish | ambiguous | thin/mixed | disagree (HC→watch) | — |
| XLV | outflow (−$3.4M) | bearish | offsetting blocks | modest Jan-27 call accumulation | disagree (HC→watch) | — |
| XLI | outflow (−$3.0M) | bearish | creation/redemption | negligible (<$250K) | disagree (Inds→watch) | — |

Lead read: the top inflow ETFs (SMH, IGV) show the *same* long-with-hedge / macro-hedge signature their constituent flow does — bullish gross premium with heavy protective puts. This reinforces the "Tech-in is hedged, not conviction" framing.

## 3. Swing Book (1–6 weeks) — ranked by weekly conviction score

A genuinely thin, conflicted, bearish-leaning week. Only two names cleared the score-3 floor, both LOW tier; both are capped at half by the OUT-OF-REGIME guard and further cut by the gate stack.

### 3a — Long swings (regime-aligned)
None cleared. The software longs (NOW/IBM/PANW/CRM) rest on a single agent (sector-rotation) and are contradicted by leap-radar's 30d cum-flow reversal flag. See §10.

### 3b — Short / fade swings (defined risk only)

| Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure | Invalidation |
|---|---|---|---|---|---|---|---|
| QQQ | LOW | 3 | 0.519 (n=135, clean) | **STARTER** | Mechanized DEX flip (6/23) + 54-day PUT OI build in FULLY_NEGATIVE GEX; 30d premium near-flat (−1 lite), Tech tape still inflowing → regime short, not flow-confirmed | **bear put spread** (defined-risk through NFP), anchor 705–715 | close back above 724; VIX-collapse vanna squeeze off the 705 wall; strong NFP rip |
| AMAT | LOW | 3 | 0.80 (capped; raw .921, n=164) | **watch-only** (debate-cut) | Long-vol on front backwardation (Jul-02 IV 169%, ratio 2.105) + per-name VRP −2.25; CONFIRM fundamentals — but bear won the debate on phantom-catalyst risk | small Jul-02 straddle *if taken*; else watch | front IV ratio < 1.5 (event passed / double-crush); VRP flips positive |

AMAT carried the strongest backtest support in the book (+35pp excess) and a CONFIRM fundamentals overlay, but two compounding −1 tier penalties (tech-semis cluster + debate gate) cut it to watch-only. The bear's case is structurally sound: Jul-02 IV (169%) sits far above Jul-10 (83%) with **no confirmed Jul-02 catalyst** — the Jun-26 Master Class already fired and next earnings is Aug-13. Buying peak IV-rank-100 vol into a possibly-phantom catalyst risks a double crush.

## 4. LEAP Book (6–24 months)

**Empty.** leap-positioning-radar ran the full gate battery on all contenders (NVDA, META, ORCL, UBER, MSFT, NBIS, AAPL, TSLA, LLY, NOW) and surfaced **zero** qualifiers. Gate 4 (90d/30d cum-flow accretion) was the binding discriminator — in a TRANSITIONAL/CHOPPY tape premium flow is suppressed and balanced, so the slow-accretion LEAP signature does not form. The biggest-increases DTE>180 list was thin (20 results); the only ask-dominated common-stock call builds (NVDA, NBIS) both failed on bearish/stalling cum-flow. Roll activity was dominated by **protective put rolls** (ORCL, NOW, NFLX, GLD), not fresh LEAP-call initiations.

## 5. Volatility Surface — WoW Term Structure & Skew Evolution

After substrate hygiene (expired 0DTE bucket excluded), the index surfaces are clean **CONTANGO** — the KINKED/BACKWARDATION labels on SPY/QQQ are classifier artifacts from the expired Jun-26 front bucket; no calendar edge. Single-name reads:

- **AMAT — BUY VOL (event-driven, not a calendar).** Genuine front-end backwardation: Jul-02 169% vs Jul-17 106% vs back-month ~80%; front-IV ratio **2.105 and rising WoW**. Per-name VRP −2.25 (realised ~4× implied). The ratio is too high and rising to run a calendar (event still pending). IV percentile 98th (provisional, 53 days). Skew flipped COMPLACENT→mild put-bid. *Disqualified for calendar; long straddle/strangle is the only clean expression — and the debate cut it to watch.*
- **ABT — SELL VOL (per-name override).** KINKED at Jul-17 (survives hygiene), per-name VRP **PREMIUM_SELLING +0.0875**, skew TAIL_HEDGING 1.178 and *widening* WoW (+5.2pp). Earnings-aligned (Jul-17 = typical ABT Q2 window). Market-wide VRP conflicts (index PREMIUM_BUYING) → defined-risk, half-size only.
- **TSCO — SELL VOL (per-name override).** Strongest per-name PREMIUM_SELLING in the watchlist (+0.172), but CONTANGO surface and skew *compressing* WoW (−5.8pp) → the richest window may have passed; a short put spread on Sep-18 is the cleanest expression. Half-size.
- **ADI / TXN / TER — NEUTRAL.** FAIR VRP, flat/contango live surfaces, no edge. (TER has a notable Jan-2028 LEAP call accumulation — a note for the LEAP radar, not a vol trade.)

All single-contract IV outliers this week were 0DTE OPEX mechanics on SPY/QQQ — no actionable single-name dislocations.

## 6. Earnings — Recap & 2-Week Lookahead

**(a) Recap.** The regime lesson was clean: TRANSITIONAL + PREMIUM_BUYING means **beats get sold.** FDX (+4.8% beat → −3.5%), CCL (+17% beat → −4.9%), SNX (+16% beat → −2.0%) all fell on beats. The only unambiguous BUY VOL confirmation was **MU** (+17.4% beat, IVR 100, +15.7% gap next session — realised dwarfed implied). AYI (+1.3% beat → +17.6% gap) rewarded a reset-to-the-floor name. SELL VOL was structurally the wrong posture all week.

**(b) 2-week lookahead (ranked).**

| Rank | Ticker | ER Date | Verdict | Key signal | Front IV ratio | Back-month skew | Event overlap |
|---|---|---|---|---|---|---|---|
| 1 | **PEP** | Jul 9 pre | **SELL VOL (half)** | Genuine kink at Jul-10 (33.2% vs 25.4%/29.8%); implied 6.3% vs 1.5–4% historical | 0.882 CONTANGO | NORMAL (+0.009) — half-size only | — |
| 2 | **GIS** | Jul 1 pre | **CALENDAR (half)** | Back-month TAIL_HEDGING (+0.059); bullish flow 4/5d | FLAT 1.0 | TAIL_HEDGING | NFP Jul-2 next day |
| 3 | **FDS** | Jul 1 pre | **BUY VOL (call spread)** | Bullish flow (PCR 0.226, +$317M, OI build); VRP supports | FLAT 1.0 | NORMAL | — |
| 4 | NKE | Jun 30 post | SKIP | front ratio 1.663 extreme; back COMPLACENT; bearish flow | 1.663 | COMPLACENT | — |
| 5 | STZ | Jun 30 post | SKIP | front ratio 1.577 extreme | 1.577 | TAIL_HEDGING | — |
| 6 | AVAV | Jun 29 post | SKIP | front ratio 1.563; back COMPLACENT | 1.563 | COMPLACENT | — |

PEP is the cleanest kink in the scan but the flat back-month skew + PREMIUM_BUYING headwind cap it at half-size. FDS is the strongest directional read (unambiguous bullish flow). GIS carries NFP-day overlap risk — exit before the Jul-2 print.

## 7. Risk & Correlation (week-candidate universe)

**Correlation clusters (≥0.70, 30d).** The entire book is one bet:

| Pair | Corr | Cluster |
|---|---|---|
| QQQ / SMH | 0.943 | tech_semis |
| NOW / IGV | 0.921 | software_etf |
| AMAT / SMH | 0.873 | tech_semis |
| SMH / MU | 0.865 | tech_semis |
| SMH / INTC | 0.829 | tech_semis |
| AMAT / MU | 0.826 | tech_semis |
| QQQ / MU | 0.820 | tech_semis |
| TSLA / IWM | 0.797 | risk_small_cap |
| QQQ / IWM | 0.794 | risk_small_cap |

QQQ is the kept member of the tech_semis cluster; **AMAT took a −1 cluster tier** as the lower-ranked member. There is no diversification in this candidate set — any sizing must treat QQQ-short and AMAT-vol as the same tech-semis exposure.

**Macro & event risk:** sticky inflation / falling-10Y stagflation-lite; **NFP Jul-2 (T+4)** is the primary near-term event for the QQQ short — it sits inside the swing horizon and took the size from half to starter. June CPI Jul-14 sits inside a 2–4 week horizon.

**Fundamentals verdicts (top-5):** QQQ/SMH NA (ETF); **AMAT CONFIRM** (beat streak, Master Class catalyst — vol thesis direction-neutral, insider selling orthogonal); **TSLA CAUTION** (mixed earnings after two beats, Jul-22 binary, analyst PT $401.75 above price tilts against the short); **NOW CONFIRM** (beat streak, insider buying, +43% PT upside); **LLY CONFIRM** — the accumulation-hunter distribution_flag (buy_ratio 0.379) resolved as profit-taking into a +6.3% all-time-high catalyst (EU Jaypirca approval), *not* systematic exit; dividend-capture arb risk low (0.61% yield, 49-day ex-date). **No VETOs this week.**

**Debate-disconfirmation cuts:** **AMAT** — disconfirmer (bear, sell-the-crush) residual 0.75 ≥ proponent (bull) 0.65 → debate gate fired, −1 tier (phantom Jul-02 catalyst / double-crush). QQQ — proponent (bear, pro-short) 0.65 > disconfirmer (bull, anti-short) 0.55 → debate cleared the short.

**Breadth cross-check (advisory):** fz price breadth 64.4% green (324 adv / 178 dec) vs uw options flow 38.2% bullish — a price-up / flow-down divergence. Not the classic <50 distribution flag; flow is lagging green price. 0 points.

**Adverse-flow exits:** the prior `conviction_week_2026-W25` watchlist group did not exist (cold start for the feedback loop) — no prior-week exit candidates. Live-watchlist alerts of note: INTC (bearish flow + expanding OI, consistent with the semis-short theme), MSFT (large bullish dark-pool accumulation — inconsistent with an aggressive broad-market short), PLTR (low-IV bullish accumulation).

**Hedge sleeve.** The live book is a single QQQ short starter — net short, minimal notional. Recommendation: express QQQ via a **bear put spread (defined-risk)** rather than outright, which itself neutralises the NFP Jul-2 tail. A separate VIX hedge is not warranted at starter size. With one position there is no long-side exposure to offset.

## 8. High-Conviction Cross-Ref (HIGH and MEDIUM tier)

**None.** No candidate reached MEDIUM (≥7) or HIGH (≥9). The week's two scored names are both LOW (raw 3): QQQ SHORT → STARTER, AMAT BUY VOL → watch-only. This section is empty by construction — an honest low-edge week.

**Expectancy lens (advisory — C31):** not applicable this cycle — no per-tier expectancy table with a populated HIGH/MEDIUM cohort, and the closed-call sample under `conviction_week_*` is too thin (cold-start watchlist) to compute a payoff ratio. The live sizer remains the win-rate ladder (Step 5); C3 Kelly stays advisory.

Embedded rubric (for audit) — **FROZEN, version 2026-06-12:**

```
Weekly conviction score = Σ:
  +3  oi-trend BUILDING full week (--days >= 5)                                  (accumulation/leap)
  +3  3+ aligned accumulation signals, block-stratified institutional confirmed  — CONJUNCTION: full +3 only when cum_premium_flow_30d sign-aligned AND |cum_flow_30d| >= $50M; else halved +3->+1
  +1  conviction-matrix DIRECTIONAL_LONG, conf > 70, stable WoW                   — CONDITIONAL: leap_directional context only
  +2  oi position-rolls institutional roll forward into longer-dated LEAP
  +1  cumulative-premium-flow net directional accretion (30d/90d)                 — INTENT-SCREENED: no distribution_flag; no div-capture deep-ITM sub-parity
  +1  MECHANIZED dex_flip / vanna squeeze in trade direction                      — verified SIGN CHANGE only (not a level)
  +1  sector-rotation single-name leader                                         — CONDITIONAL: persistence >= 0.6 AND cum_flow aligned AND |cum_flow_30d| >= $50M
  +1  earnings BUY VOL / SELL VOL, term-skew aligned (next 2 weeks)
  +2  multileg directional structure repeated on >= 2 days (term-structure-anchored)
  +1  vol-surface KINKED/BACKWARDATION worsening WoW + iv-percentile-zscore extreme + VRP-aligned
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian crowded long, rising pc-ratio-zscore (VRP positive ONLY)
  -3  flow_conflict — 30d cum_premium_flow clearly opposite dominant_signal_class
  -1  flow_conflict_lite — 30d cum_premium_flow MIXED (mutually exclusive with -3)
  [multi_day_sweep = 0 points — removed 2026-05-23 P0.3]
  [TIER GATES applied by risk-monitor in 2d, NOT score_components: -1 tier correlation cluster; -1 tier WoW regime flip]
Tiers: >=9 HIGH (full) | 7-8 MEDIUM (half) | 3-6 LOW (starter/watch) | <=2 drop.
Out-of-regime guard (2026-06-12 P0.6): all sizes capped at half until a /calibration-audit clears >=30 post-freeze calls.
```

## 9. Setups for Next Week

- **Next-session GEX advisory (SPY/QQQ only — prose, 0 points).** Backtest verdict **NO_GO_NO_EDGE** (SPY walls-as-magnet 26.4% vs 50%, p≈1.0 — walls are *not* magnets; dealer context only). Both indices are **FULLY_NEGATIVE** GEX (5 consecutive sessions, no computable ZGL). **SPY** spot 732.14, call wall 734 / put wall 730 — a very tight pocket, dealers short gamma across the book, range-expansion favoured over pinning. **QQQ** spot 708, put wall **705 (−$206M, the single largest node, ~3pts below spot)** vs call wall 724 (~16pts away) — sharply asymmetric downside-gap risk. Treat as a map of dealer hedging, not a tradable edge.
- **Next-session 0DTE premium-selling setup (validated stack, advisory, 0 points).** Backtest **GO_PREMIUM_SELL_INTRADAY**, VIX 18.41 (MID). SPY: sell premium, expected range ±1.25%, net **+0.223%** of spot notional (gross +0.323%, win 94.3% n=53). QQQ: range ±1.9%, net **+0.34%** (gross +0.44%, win 90.6%). Delta-neutral; **enter at the open, never carry overnight**; stand aside on a VIX spike or front-end backwardation. **Caveat:** PnL is % of spot notional, GROSS of costs — lead with the net line; the validation sample has **no vol shock** (left tail UNSAMPLED). **And note the tension:** this week's VRP is PREMIUM_BUYING (vol cheap vs realised), which argues *against* selling premium — if the open IV is light, size down or stand aside.
- **Dealer-positioning swing setups (1–4 weeks).** Active `dex_flip_short` on **QQQ, NVDA, TSLA** (all flipped 6/23 — note the single-date correlation reduces independence). TSLA carries an additional GEX regime flip (ZGL 399.31 now overhead). A **vanna-squeeze watch** sits on the put-heavy SPY/QQQ/NVDA/TSLA/META books: if VIX closes lower for ≥3 sessions (e.g. off a benign NFP), those put walls become contra-trend LONG fuel — the inflection to monitor.
- **Pin vs trend:** neither — FULLY_NEGATIVE GEX with no pin support; the structure favours range-expansion on a catalyst (NFP) over pinning.
- **2–3 highest-conviction actionable setups:** only one carries capital — **QQQ short via bear put spread, starter.** Everything else is watch-only.
- **LOW-tier / watch names to track for daily confirmation:** AMAT (re-evaluate after Jul-02 resolves the catalyst question), NOW/IBM/PANW/CRM (software longs — need a second confirming agent), SMH (if 30d cum-flow turns bearish, the −3 flow_conflict lifts).
- **OPEX:** not OPEX week (June monthly already expired Jun-19; next monthly Jul-17) — opex-pin-strategist not spawned.
- **Deep-dive hand-off:** skipped — no HIGH-tier names on a no-edge week.

## 10. Watch-only — single signal, no confluence

For journaling, **not** for trade entry next week:

- **NVDA (mixed)** — dealer dex_flip_short (bearish) vs a $56.2M Oct-16 220C ask-side print (bullish, 145×) + bearish 90d cum-flow. Directionally unresolved.
- **MU (mixed)** — 5/5 sweep persistence (near-term puts $650–675) vs +$706M 30d bullish cum-flow + an earnings beat. Short-term puts against a bullish long-term book.
- **IGV (mixed)** — $74M Jan-27 bear put spread vs bullish smart-money flow divergence and +$76.9M ETF cum-flow. Conflicted.
- **IWM (short, 1 agent)** — multileg's highest-conviction structure (4-day 280–290 bear put spread, deep-negative GEX) but dealer DEX was flat; needs a second agent.
- **INTC (short, 1 agent)** — sweep 4/5 sessions, Jul-02 P75 ask-bought, 30d cum-flow −$133M aligned; single agent.
- **MRVL (short, 1 agent)** — Jul-02 P155 53× ask put, but +$178M 30d bullish cum-flow (flow_conflict risk).
- **NFLX (short, 1 agent)** — bearish diagonal, but Comm Services is an *inflow* sector (sector conflict).
- **NOW / IBM / PANW / CRM (long, sector-rotation only)** — software leaders with cum_flow_30d ≥ $50M and CONFIRM-quality fundamentals (NOW especially: +43% analyst PT upside), but a single Phase-1 agent and a leap-radar 30d-reversal flag across the funnel. The most interesting longs to watch for a second confirming signal.
- **LLY (long)** — Healthcare leader, +$93.8M 30d, CONFIRM fundamentals (EU catalyst + ATH), but ETF (XLV/XBI) disagrees and an advisory distribution_flag is present; scored 0.
- **ABT / TSCO (sell vol, 1 agent)** — per-name PREMIUM_SELLING overrides; defined-risk half-size if taken.
- **PEP / FDS / GIS (earnings, 1 agent)** — see §6.
- **WMB (short, 1 agent)** — accumulation-hunter DIRECTIONAL_SHORT 55.9%, DP distribution; advisory.
