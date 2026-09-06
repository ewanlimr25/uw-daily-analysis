# Weekly Market Intelligence — Week of 2026-07-06 (ISO 2026-W28)

## Executive Summary
- **Week regime + WoW Δ:** TRANSITIONAL/UPTREND, **held** — the regime label was unchanged Monday→Friday (SPY 754.95 > 20sma 743.81 > 50sma 741.24, +2.43% 30d, −0.72% from 90d high), but options-flow breadth *softened* (bullish tickers 37.4% → 33.4%). VRP is mixed-to-premium-buying: SPY FAIR (−0.028), QQQ PREMIUM_BUYING (−0.073, vol cheap vs realized). A broad, undifferentiated risk-on tape — every GICS sector took inflow — with the front end of vol *deflating* into a heavy event week.
- **Rubric regime status:** OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL/UPTREND) — sizing capped at half. Zero post-freeze HIGH/MED calls have resolved; the P0.6 guard stands.
- **Signal performance:** 0 of 1 resolved (hit rate 0/1 = 0%); 3 INCONCLUSIVE excluded; 4 total calls in universe (4 envelope-anchored, 0 reconstructed). The lone resolvable call — SPY short (07-08) — lost as the tape ground higher; the other three (NBIS long, NVDA long, EWZ long) had no ATR-clearing move within the week. A thin, near-uninformative scorecard: the week's dailies barely committed capital.
- **Top swing build for next week:** *None.* No name cleared to HIGH or MEDIUM tier. The highest raw score was SNDK at 5 (LOW), and it — like the entire board — sits on a single **saturated OI-trend line** (C47 artifact: `consecutive_build_days == --days` on every liquid name). Watch-only across the board.
- **Top LEAP build:** *None.* The LEAP radar returned an empty board — all 10 mega-caps failed the cumulative-premium-flow gate (MIXED / 30d–90d sign-flip) and conviction-matrix (MIXED, confidence <6%).
- **Biggest emerging risk:** A compressed **triple-binary event stack** in the coming week — CPI (07-14), PPI (07-15), and July OPEX (07-17) — with JPM and the bank cohort reporting into it. Secondary: a tight **semis/memory correlation cluster** (SNDK/MU/AMD/INTC pairwise 0.70–0.86) means any single-name semis long is really a beta bet on the group.

## 0. Week in Review — Intra-Week Signal Performance

Universe = the union of non-DROP `calls[]` across the week's five daily `decision.json` envelopes (all five days ran — 0 reconstructed). The week's dailies were overwhelmingly DROP-tier; only four calls carried a live tier.

| Ticker | Direction | Source | Move vs ATR(14) | Flow/OI | Grade | Note |
|---|---|---|---|---|---|---|
| SPY | short | envelope 2026-07-08 | +9.38 vs 0.5×ATR 2.31 (**against**) | Tape ground higher into Fri | **LOSS** | Called short on the 07-08 breadth-divergence panic (22% green); regime never broke, SPY closed the week at highs |
| NBIS | long | envelope 2026-07-09 | +3.55 vs 0.5×ATR 7.89 | Flow bullish 7/10 days, IV rank 94 | **INCONCLUSIVE** | Bounced but did not clear the (very wide) ATR threshold in one session |
| NVDA | long | envelope 2026-07-10 | 0 (called on WEEK_END) | oi BUILDING (sat) | **INCONCLUSIVE** | Zero forward window — called Friday |
| EWZ | long | envelope 2026-07-10 | 0 (called on WEEK_END) | net flow bearish Fri | **INCONCLUSIVE** | Zero forward window — called Friday |

**Read:** 0/1 resolved is a non-result, not a verdict — the desk simply didn't commit enough to grade. The one call with a real forward window (SPY short) faded against a regime that held. The discipline was correct: three of four calls were made too late in the week to resolve, and the board never manufactured conviction it didn't have.

## 1. Regime & WoW Delta

The week opened and closed in the same **TRANSITIONAL** regime ("mixed signals, reduce size, favor defined-risk"), with the underlying **UPTREND** intact — SPY held above its 20- and 50-day averages all week and finished −0.72% from its 90-day high. The tell is beneath the label: options-flow breadth deteriorated (bullish-flow tickers 37.4% Monday → 33.4% Friday) even as the cash tape stayed green (fz breadth 338 advancers / 163 decliners, 67.2% green — no cash divergence). This is a tape that keeps grinding higher on narrowing participation.

**Vol regime is mixed-to-premium-buying.** SPY VRP is FAIR (−0.028, IV ≈ realized); QQQ VRP is PREMIUM_BUYING (−0.073, vol *cheap* versus realized). That configuration favors owning vol / calendars over naked premium sales — reinforced by the tape-wide front-end IV **deflation** the vol-surface scan found (27 names reverted out of backwardation with front IV falling). **DTE share:** the weekly bucket roughly doubled across the week (0.13 → 0.27) while monthlies held (~0.14) and 0DTE registered flat — a modest retail-tape acceleration that argues for treating any rotation read as 2–3-week tactical, not multi-month.

**Macro backdrop.** Yield curve normal (+0.35 10s2s); core CPI 2.96% YoY but core PCE **3.41%** (sticky, elevated); unemployment 4.2% with soft payrolls (+57k); 10Y 4.54% flat; USD strengthening; fed funds 3.62%. A mildly stagflationary lean with a firming dollar — a headwind for mega-cap multinationals. **Forward event risk (next two weeks):** CPI (Tue 07-14), PPI (Wed 07-15), Fed Chair Warsh testimony (House 07-14 / Senate 07-15), jobless claims + retail sales (~07-16), and **July OPEX (Fri 07-17)** — with the bank-earnings cohort (JPM/GS/WFC/BAC/C/MS 07-14/15) and NFLX (07-16) landing inside the same window. Next week is front-loaded with binary risk.

**Implication:** favor defined-risk, keep sizing light into CPI, and treat every directional read as provisional until the 07-14/15 prints clear.

## 2. Sector Rotation

**Rotation regime call: `no_change` (low confidence).** Every one of the 11 GICS sectors registered INFLOW with persistence ≥0.8 (nine at a flat 1.0) — nothing is rotating *out* at the GICS level, which rules out any of the canonical defensive/cyclical/growth/value patterns by construction. This is a broad, undifferentiated risk-on tape, not a rotation. The signal this week is *leadership differentiation within* the inflow, and that is where the ETF-instrument layer earns its keep.

Above-median standouts (5-day summed net flow): Technology (~$16.3B), Communication Services (~$4.4B), Consumer Cyclical (~$2.9B), Financial Services (~$1.35B), Healthcare (~$1.23B). But the ETF layer disconfirms the two biggest:

- **Financial Services (XLF agrees) — the cleanest live rotation leg.** Best-confirmed of the group; single-name leaders SOFI, COF, PYPL, JPM.
- **Communication Services (XLC agrees but thin)** — direction confirms, but ETF size is trivial; read as a single-name (META) story with an ETF tailwind, not independent confirmation.
- **Consumer Cyclical (XLY weak-agree)** — confirms but the week-end sweep tape flipped put-heavy; softening. Leader: TSLA.
- **Technology (XLK / SMH both MIXED) → DISAGREE.** The largest GICS dollar flow in the market did *not* show up as broad ETF creation — this is single-name concentration (NVDA/AMD/SNDK), not a sector-wide rotation. Downgraded to watch-only.
- **Healthcare (XLV MIXED, XBI outright BEARISH) → DISAGREE.** GICS inflow is mega-cap pharma; the biotech sleeve (XBI) is being sold.

**ETF flow tape (advisory):**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| XLF | +$21.1M | BULLISH (5d) | 1M-sh block near-ask, clean | Modest, balanced | **agree** | SOFI, COF, PYPL, JPM |
| EWY | +$19.3M | BULLISH | 609k-sh block 0.34 below mid (distribution tell) | Put-heavy 2028 LEAP puts | n/a (geographic) | — |
| XLY | +$0.65M | BULLISH (weak) | Block sold below mid | Put-heavy week-end | **agree (weak)** | TSLA |
| XBI | −$10.4M | BEARISH | Mixed | LEAP puts bought, calls sold | **disagree** (Healthcare green) | biotech sleeve |
| GDX | −$5.7M | BEARISH | Small blocks near mid | Aug puts hit bid | **disagree** | — |
| XLRE | −$0.01M | BEARISH (de minimis) | Tiny | Zero sweeps | n/a | — |

**Swing implication:** the only ETF-confirmed longs are XLF financials (SOFI/COF/PYPL) plus META (Comm-Services) and TSLA (softening); the cleanest rotation-*out* signal is the XBI+GDX bearish pair sitting under nominally-green GICS umbrellas. Treat NVDA/AMD/SNDK as single-name flow plays, not sector-rotation trades. All of this is advisory and adds no rubric points; nothing here survived to a sized position (see §7).

## 3. Swing Book (1–6 weeks)

**Empty.** No ticker cleared to HIGH or MEDIUM tier this week. Every candidate that cleared the two-agent confluence gate scored LOW (raw 3–5) and resolved to **watch-only** after the risk stack. See §9 for the LOW-tier watchlist and §8 for why the top five were cut to zero capital. This is a "no-edge" week — a valid output, not a failure.

## 4. LEAP Book (6–24 months)

**Empty.** The LEAP radar disqualified all 10 mega-caps on the two structural gates: cumulative-premium-flow returned MIXED with a 30d/90d sign-flip on 8 of 10 (TSLA 30d −$272M vs 90d +$762M; AAPL −274/+313; NVDA +157/−161; the two same-sign names, MSTR/NFLX, are net *bearish*), and conviction-matrix read MIXED with confidence 0.2–5.2% across the board — an order of magnitude below the >70 bar. AAPL showed a genuine fresh 2028 450-strike call build (30:1 ask skew) but the flow gate kills it outright. No LEAP-grade slow-accretion signature exists in the union this week.

## 5. Volatility Surface — WoW Term Structure & Skew Evolution

The dominant WoW move was a **broad front-end vol deflation**: 27 names reverted from BACKWARDATION (07-06) to CONTANGO (07-10) with front IV falling — consistent with the negative-leaning VRP (vol richness draining, not building). Two substrate caveats apply and were enforced: raw `iv-term-structure` remains 0DTE-contaminated (58/84 names raw-classify BACKWARDATION with a null kink expiry — 27 reclassify after the ≥15-contract tenor floor), and `iv-percentile-zscore` ran on only 62 days market-wide (below the 120-day floor), so all percentile reads are provisional.

**Shifted INTO KINKED (event-driven, hand to earnings):** META (kink 07-31, front IV **rising** — earnings building, do not fade), GOOGL/GOOG, TSLA (07-31), IBM/NOW/PLTR, LLY and PANW (front IV rising — PANW's 142% IV flagged as a possible thin-strike artifact). **Calendar-spread candidates (backwardation, front falling, no catalyst):** the semis cluster — AMAT, ASML, IREN, DELL, MRVL, RKLB — plus FCX. **Do NOT fade** the rising-front names (TSM, NFLX, JNJ, MA, KR, GTLB, PGR — event still building).

**Important context for §2/§3:** SNDK's whole-week signal is **post-earnings IV-crush residue** — its earnings settled 07-10 ($444M same-day expiry) — not a fresh vol dislocation. That reframes SNDK's entire flow footprint (see §8). No single-contract IV outlier survived the hygiene filter this week.

## 6. Earnings — Recap & 2-Week Lookahead

**(a) Recap — 6 of 8 SELL VOL confirmed.** The week's clean IV-crush names: DAL (beat, sold the news), PEP, LEVI (textbook — IV rank 56→11, tiny net move), AZZ, PSMT, SMPL (cleanest — IV rank 98→43, price round-tripped a +16.6% beat). Two **disconfirmed** — the traps: HELE (violent multi-day −10% whipsaw off a near-zero est. base) and WDFC (+46.5% beat drove a +10.9% move that ran premium sellers over). Takeaway: extreme-magnitude surprises (noisy EPS base or outsized beat) are where the "sell the crush" prior breaks.

**(b) 2-week lookahead (ranked).** *Note: the screener's `implied_move_perc` field is broken (showed NFLX at 0.43% — off ~19x); the moves below are straddle-estimated from term-structure IV.*

| Rank | Ticker(s) | Date | Verdict | Note |
|---|---|---|---|---|
| 1 | JNJ, GS | 07-14/15 | **CALENDAR** | Most extreme front-end panic + real tail-hedging; **OPEX-overlap** |
| 2 | WFC, MS, BAC, C, JPM | 07-14/15 | **CALENDAR** | Bank kickoff; front-end ratio >1.10 on all → sell the front event tenor / own the back; MS best back-skew |
| 3 | NFLX | 07-16 | **BUY VOL (small)** | ~8% implied move likely *under*-prices historical realized; complacent tail = small size; **OPEX-overlap** |
| 4 | TXN, IBM | 07-22 | **CALENDAR** | Real kink, not extreme; clear of OPEX |
| — | ASML, TSM, NOW, GOOGL, BLK | 07-15/22 | **SKIP** | Complacent-tail / mixed / far-DTE artifact |
| — | ROL, TDY, EFOR | 07-22 | **SKIP** | Fail the contract-count liquidity floor |

The whole bank cohort reads **CALENDAR, not SELL VOL** — front-end-iv-ratio clears 1.10 on every name, so the correct structure captures the term-structure normalization without eating the binary front gap. **analyst-vs-flow remains unwired** on this build (returns options-flow only) — no genuine analyst-disagreement scores this week.

## 7. Risk & Correlation (week-candidate universe)

**Correlation.** One live cluster: **semis/memory** (pairwise ≥0.70) — AMD/INTC 0.86, SNDK/MU 0.86, MU/AMD 0.77, SNDK/AMD 0.75, SNDK/INTC 0.71. Kept member SNDK (highest raw); every other member is already skip/dropped, so the cluster penalty has no live target. NVDA sits *outside* the cluster this week (max pairwise 0.51 vs AMD) — the usual NVDA-semis lockstep did not print. Soft-watch (0.60–0.70): MU/INTC, INTC/TSLA.

**Panic gate — clean.** SPY front-end-iv-ratio 0.568 / QQQ 0.650, deep CONTANGO (5-DTE control 0.741). Notably, the tape is pricing event premium into the *belly*, not the front, going into a CPI+PPI+OPEX week — so front-end event insurance is unusually cheap.

**Macro & event risk.** Core PCE 3.41% sticky, soft payrolls, strengthening USD (megacap headwind). The **CPI print (07-14) sits at T+2** — a Tier-1 binary that fires the event-risk gate (−1 tier) on every undefined-risk swing long book-wide. **JPM's own earnings land the same session (07-14)**, stacking a second binary; PPI (07-15, not Tier-1) and OPEX (07-17, T+5) round out the stack.

**Fundamentals verdicts (top-5).** No VETOs. NVDA CONFIRM, META CONFIRM; SNDK CAUTION (stale post-print data + chronic insider selling + split news), JPM CAUTION (pure event-risk, 07-14), **SOFI CAUTION** — insider MSPR −39.5 selling *into* the dark-pool accumulation read, the textbook distribution-dressed-as-accumulation pattern the gate exists to catch.

**Debate cuts.** The bear side won or tied on **all five** top names (SNDK 0.55/0.85, NVDA 0.65/0.75, JPM 0.55/0.75, SOFI 0.55/0.75, META 0.65/0.65) — the debate gate fired book-wide. The recurring theme the bears exploited: the entire board's directional score rests on one **saturated** OI-trend line.

**Breadth cross-check (advisory).** 338 adv / 163 dec, pct_green 67.2% — green cash tape, no divergence from the UW regime label. The breadth softness is in *options-flow* breadth (33.4% bullish), not the cash market.

**Adverse-flow exits (vs conviction_week_2026-W27):** AAPL (bearish net −$67.7M into a long watch thesis — exit candidate) and HOOD (bearish −$21.1M despite a heavy-call P/C 0.30 — calls being faded, exit candidate). Both are flow-driven, not fundamentals-driven (the fundamentals tripwire found no adverse changes).

**Hedge sleeve: not required** — the book carries zero sized capital, so net delta is zero. Advisory only: for any discretionary longs held through CPI/PPI/OPEX, the 0.568 SPY front-end ratio makes a defined-risk SPY put vertical expiring just past 07-17 the efficient event hedge; skip the VIX ladder (front-end contango bleeds).

## 8. High-Conviction Cross-Ref (HIGH and MEDIUM tier)

**No HIGH or MEDIUM names this week — zero capital deployed.** This is the **eighth consecutive empty/near-empty board**, and it is the correct output: the entire top-5 stands on a single **saturated C47 OI-trend floor** (`consecutive_build_days == 5 == --days` on every liquid name — the +3 is earned by expiry mechanics, not accumulation), win-rate is `NA(substrate)` everywhere (no dominant class is backtest-supported), the debate gate cleared *zero* names, and a Tier-1 CPI print sits at T+2. For reference, the 2026-07-04 audit graded exactly this empty-book refusal as the system's best behavior (sized book realized 36.1% vs paper 45.2%).

*Expectancy lens (advisory, C31): not applicable — no sized book to compute payoff ratios over. The prior calibration windows show the desk's edge lives in the empty-board discipline itself this quarter, not in tier asymmetry.*

The top five by raw score, all cut to **watch-only**:

- **SNDK** (long, raw 5, LOW): +3 oi (SATURATED) / +1 cum_flow (+$1.04B 30d) / +1 mechanized DEX flip. `fundamentals CAUTION`; debate bear 0.85 ≥ bull 0.55. **The whole-week bullish footprint is post-earnings crush residue + a broad-semis (SK Hynix/Micron) relief bounce (+20% Tue→Fri), not name-specific conviction** — and escalating single-leg opening PUTs across 4/5 sessions point the other way. Gate stack: fundamentals −1, event_risk −1 (CPI T+2), debate −1, rubric_regime half → **skip**. Invalidation (if traded discretionarily): break of the dark-pool shelf; watch whether the DEX flip holds or reverts ≥3 sessions.
- **NVDA** (long, raw 4, LOW): +3 oi (SATURATED) / +1 cum_flow (+$157M 30d, but 90d −$161M sign-flip). `fundamentals CONFIRM` (cleanest of the five); debate bear 0.75 ≥ bull 0.65. Multileg's ≥2-day repeat was **withheld** — it's a long-vega Sep/Jul calendar (a vol structure), not a directional long, and the pin thesis broke on the 196→210 breakout. Gate: event_risk −1, debate −1, rubric_regime half → **skip**.
- **JPM** (long, raw 4, LOW): +3 oi (SATURATED, builds in 0-DTE/07-17 strikes = pre-earnings/OPEX mechanics) / +1 earnings-calendar. `fundamentals CAUTION` (clean fundamentals; the caution is pure event-risk). **Own earnings 07-14 stacked on CPI same session** — untouchable as a naked directional long; if the desk wants JPM it must be re-underwritten as an explicit earnings-vol calendar through earnings-scout. Gate: fundamentals −1, event_risk −1, debate −1, rubric_regime half → **skip**.
- **SOFI** (long, raw 3, LOW): +3 oi (SATURATED) / +1 accumulation (C11-halved — the union's *only* genuine accumulation read, buy/sell 1.78) / −1 flow_conflict_lite. `fundamentals CAUTION` — insider selling into the accumulation read; cum_flow dead flat (−$0.7M). The one genuine accumulation signal on the board is undercut by the exact distribution pattern the gate flags. fz MODERATE squeeze (14.9% short float) is a two-edged tailwind. Gate: fundamentals −1, event_risk −1, debate −1 → **skip**.
- **META** (long, raw 3, LOW): +3 oi (SATURATED) / +1 vol-surface (KINKED 07-31, IV rank 100) / −1 flow_conflict_lite. `fundamentals CONFIRM` (dated AI-infra catalyst) but the +1 is really a *vol* read — IV rank 100 into a PREMIUM_BUYING QQQ tape argues for the vol-surface desk, not a directional long, and price already ran +11.5% on the week (RSI 66). 90d cum-flow −$368M. Gate: event_risk −1, debate −1, rubric_regime half → **skip**.

Embedded rubric (for audit):

```
Weekly conviction score = Σ:
  # +3 swept ≥3/5 days REMOVED 2026-05-23 P0.3 (multi_day_sweep −22pp; informational only, 0 pts)
  +3  uw historical oi-trend BUILDING full week, --days ≥ 5 (WEEKLY-only +3; C47: state saturation — consecutive_build_days==--days is a floor, not a count)
  +3  3+ aligned accumulation signals + dark-pool block-stratified institutional-tier — C11 CONJUNCTION: full +3 only if cum_flow_30d sign-aligned AND |cum_flow_30d|≥$50M; else floored +3→+1
  +1  conviction-matrix DIRECTIONAL_LONG conf>70, stable WoW — CONDITIONAL: only when dominant_signal_class==leap_directional
  +2  oi position-rolls institutional roll forward into longer-dated LEAP
  +1  cumulative-premium-flow net directional accretion — INTENT-SCREENED (no C28 distribution_flag; not deep-ITM ex-div arb)
  +1  dealer-positioning MECHANIZED DEX flip or vanna squeeze — verified SIGN CHANGE only, flip-day |net_dex|≥0.25× trailing-10 median
  +1  sector-rotation single-name leader — CONDITIONAL: persistence≥0.6 AND cum_flow_30d aligned AND ≥$50M
  +1  earnings-scout BUY VOL / SELL VOL next 2wk (term-skew aligned)
  +2  multileg directional structure repeated ≥2 days (term-structure-anchored)
  +1  vol-surface KINKED/BACKWARDATION worsening WoW; iv-percentile-zscore extreme; VRP-aligned
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian crowded long, rising pc-z trajectory (VRP positive) — informed-flow-continuation penalty
  -3  flow_conflict — cum_flow 30d clearly opposite dominant class (mutually exclusive w/ lite)
  -1  flow_conflict_lite — cum_flow 30d MIXED / bottom-quartile magnitude
  [TIER GATE, 2d] −1 tier: correlation cluster (pairwise ≥0.70)
  [TIER GATE, 2d] −1 tier: WoW regime flip conflicts with trade direction
Tiers: ≥9 HIGH / 7–8 MED / 3–6 LOW / ≤2 drop. FROZEN 2026-06-12. OUT-OF-REGIME → all sizing capped at half (P0.6).
```

## 9. Setups for Next Week

**Next-session GEX advisory (SPY/QQQ only — dealer context, NOT a backtested edge).** The Step-0 rolling backtest verdict is **NO_GO_NO_EDGE**: next close landed closer to the nearest wall only 24.6% of the time vs a 50% baseline (n≈118) — walls *repel* more than they magnetize. Read the levels as where mechanical hedging leans, nothing more.
- **SPY** — spot 754.9, ZGL 754.15 (reliable, within 0.1% of spot), regime **POSITIVE** (+$3.18B total GEX), call wall 755 (dominant, +$2.03B, essentially at spot), put wall 740 (748 nearer soft support). Read: spot pinned to the ZGL with a massive long-gamma wall immediately overhead → mean-revert/pin bias 748–755 into the open. Structure: iron-fly / short-straddle framing on the 754–755 pin, not a wide condor.
- **QQQ** — spot 725.6, ZGL unreliable (recurring grid artifact — do not cite the level), regime effectively **NEGATIVE** with a −$147M pocket sitting at-the-money (726). Read: short-gamma at the money → trend-amplifying microstructure, not a clean pin; favor debit verticals / long-straddle framing over pin trades. Walls 730/705 are wide and one-sided.
- *Caveats (both): EOD book refreshes after the open; CPI/PPI gap risk through the walls; ETF-not-index book; D+1 expiry cannot be isolated.*

**Next-session 0DTE premium-selling setup (validated stack; advisory, 0 rubric points).** Backtest verdict **GO_PREMIUM_SELL_INTRADAY**. Delta-neutral, enter at the open, never carry overnight; VIX 15.03 (LOW tercile — weakest expectancy).
- **SPY**: sell premium, expected range ~0.79% (long-gamma), size ×0.5, iron condor wings ~±0.8%. Backtest mean PnL **+0.286% gross / +0.186% net** (of 0.10% assumed round-trip; % of underlying spot notional).
- **QQQ**: sell premium, expected range ~1.9% (short-gamma, wider/trendier), size ×0.5. Backtest **+0.386% gross / +0.286% net**.
- *Lead with the net line; the short-vol left tail is UNSAMPLED (no vol shock in the window) so the gross win-rate overstates a negatively-skewed edge. Stand aside on a VIX spike or front-end backwardation — and note CPI/PPI/OPEX all sit in the coming week. Permanent advisory until a vol-shock day enters the sample.*

**Swing setups (dealer-positioning).** Only **SNDK** cleared the mechanized DEX-flip gate (dex_flip_long) — but on a 5-session proxy median (not the required trailing-10), with gamma thinning, and it's a post-earnings name; treat as watch, not a setup. No vanna squeeze fired (VIX managed only 2 consecutive down days; **IWM, NFLX, MSTR carry put-heavy books that become live squeeze candidates if Monday prints a 3rd VIX down-day** — re-check first). MSFT's GEX regime flipped back POSITIVE (pinning) — cleanest single-name regime read, a stabilization tell, not a directional trigger.

**Pin vs trend:** SPY pins (long-gamma, ZGL at spot); QQQ trends (short-gamma ATM). Into a CPI/PPI week, expect the SPY pin to be fragile to the 07-14 print.

**OPEX ranked book (07-17 OPEX).** From opex-pin-strategist, ranked by gamma-enforcement:

| Rank | Ticker | Pin | Spot | Dist | Structure | CPI/PPI fragility |
|---|---|---|---|---|---|---|
| 1 | BAC | 60 | 59.63 | 0.63% | Iron fly (tight, strong +wall) | Low (tightest cushion) |
| 2 | XLF | 55 | 55.70 | 1.22% | Broken-wing butterfly, skew to 56 | High (rate-sensitive) |
| 3 | AMZN | 250 | 245.27 | 1.93% | BWB, skew to 245 | Moderate |
| 4 | MSFT | 390 | 384.85 | 1.34% | BWB, skew to 385 | Moderate |
| 5 | TSLA | 400 | 407.69 | 1.89% | BWB, skew to 407.5 (real wall at spot, not the 400 OI-pin) | Moderate |
| — | HYG | 81 | 79.70 | 1.63% | **Watch-only** — fully-negative gamma regime, marginal pin | Highest |

No name in the OPEX book qualifies for a short straddle (none clears the <0.5% distance bar); the book is iron-fly / butterfly only, and CPI (07-14) / PPI (07-15) sit *inside* the OPEX window as the dominant invalidation risk for every pin.

**Actionable HIGH-tier setups: none** (empty board). **LOW-tier names to track for daily-analysis confirmation:** SNDK, NVDA, JPM, SOFI, META (written to `conviction_week_2026-W28`) — plus the ETF-confirmed financials leaders (COF, PYPL) and the vol-surface calendar candidates (AMAT/ASML/MRVL) if the daily fleet re-confirms.

**Deep-dive hand-off:** skipped — no HIGH-tier name to hand off on a no-edge week.

## 10. Watch-only — single signal, no confluence

Surfaced by a single agent or direction-conflicted; listed for journaling, **not** for entry:
- **COF, PYPL** — sector-rotation financials leaders only (single agent).
- **XBI, GDX** — sector-rotation bearish ETF legs only (single agent); note GDX 30d flow is actually +$86M *bullish*, against its own short-leg tag — a flow_conflict on arrival if it re-enters.
- **BAC, XLF, AMZN, HYG** — OPEX-pin structures only; not directional entries.
- **MU, MSFT** — cleared confluence but **direction-conflicted** (MU: 5/5 sweeps but MIXED direction; MSFT: bearish single-leg PUT roll vs pinning GEX). Non-directional, watch-only.
- **INTC, TSLA, AMD** — scored to raw 0 via mechanical flow_conflict (30d cum-flow clearly opposite the long thesis: INTC −$706M BEARISH-labeled, TSLA −$272M, AMD −$96M) despite clearing confluence. The bullish sweeps/structure on each is contradicted by net premium leaving.
