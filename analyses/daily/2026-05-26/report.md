# Daily Market Analysis — 2026-05-26

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / UPTREND. SPY 750.59 (>20sma 733, >50sma 698, −0.2% from 90d high), VIX 16.94 (LOW). Breadth **WEAK at 40.1% bullish** — a narrow, mega-cap-semis-led tape. SPY & QQQ both sit in **long-gamma** EOD books (pin/vol-suppression). Sector lean: Tech dominant (+$8.7B net premium) but it is **concentration, not rotation**.
- **Next-session GEX (SPY/QQQ):** SPY — long-gamma, ZGL 749.65 (reliable), call wall 751 / put wall 730 → pin-to-750, fade pokes to 755. QQQ — long-gamma (ZGL unreliable, fallback positive), call wall 740 / support shelf 725 → pin-to-730. Advisory, see §2.
- **Top swing build:** **None survives.** All five top-conviction names (AMD, SNDK, NVDA, INTC, QQQ) were gated to **SKIP** — every long is the same crowded AI/semis position, the bears won all five disconfirmation debates, and PCE (T+2) sits inside every horizon. Max raw_score was 6 (no HIGH, no MEDIUM).
- **Top LEAP candidate:** **None.** `leap-positioning-radar` returned zero — the day's long-dated OI is income-structured (TLT/AAPL covered calls) or wrong-direction. Closest near-miss VALE fails the 90d accretion gate (conf 46).
- **Biggest risk:** `AI_semis_megacap_cluster` = {AMD, QQQ, SOXX} (pairwise corr 0.79–0.85) = **one position wearing five tickers**, and the entire complex is **call-heavy into low VIX → latent downside vanna drift, no squeeze fuel**. A hot PCE print Thursday into a thin gamma shelf is the asymmetric risk. **Hedge: QQQ/SPY put-debit spread past PCE + small VIX call ladder.**

> **Net desk read:** No directional adds today. This is a distribution-flavored, narrow-breadth, premium-selling tape. The edge is **vol, not direction** — premium-sell the indices (FAIR/positive VRP supports it), harvest the earnings-vol cluster selectively, and hedge net long-semis delta into PCE.

---

## 1. Regime & Gamma State
- **`risk_market_regime`:** TRANSITIONAL — "mixed signals, reduce size, favor defined-risk." Trend UPTREND. SPY 750.59, +5.13% / 30d, −0.2% from the 90d high. Breadth **WEAK: 40.1% bullish (2,475 bullish vs 3,697 bearish of 6,172 optionable names)** — the advance is narrow and mega-cap-led.
- **Per-index gamma (current-state EOD book):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 750.24 | 749.65 (reliable) | +$1.066B | POSITIVE (long-γ) | 751 | 730 |
| QQQ | 730.00 | n/a (unreliable→253) | +$536M | POSITIVE (long-γ) | 740 | 705 (soft; real support 725) |
| IWM | 290.16 | ~281–283 | +$262M | POSITIVE (fragile) | — | 271/272 (−45/−49M) |

- **`options_flow_dte_volume_share`:** BALANCED — 0DTE 27.9% / weeklies 27.5% / monthlies 24.8% / LEAPs 6.3%. Not a retail-dominated tape; institutional and retail share roughly balanced.
- **`historical_vrp` (SPY):** FAIR — IV30 14.32% vs RV30 10.44%, VRP +3.88pp. Mild premium-selling lean; no strong vol edge either direction.
- **Macro backdrop (`scripts/fred_macro.py`):** Yield curve **normal** (+0.49 10y−2y). Core CPI **2.99%** YoY, core PCE **3.2%** YoY (sticky, above target). Unemployment 4.3%, payrolls +115k. 10Y **4.56% and RISING** (+26bp/30d), USD **STRENGTHENING**, fed funds 3.62%. Read: **disinflation stalling, real yields firm, USD bid = a mild risk-asset headwind / valuation cap.**
- **Forward `event_risk` (next ~10 trading days):** **PCE core Thu 2026-05-28 (T+2, Tier-1, HIGH — inside every horizon below)** · jobless claims 05-28 · ISM Mfg 06-01 · **NFP May 2026-06-05 (Tier-1, T+7)** · **CPI May ~06-10/11 (Tier-1)** · **FOMC + SEP 06-16/17 (Tier-1, T+14 — flag for any 2-4wk swing held past mid-June).**

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book (open interest persists overnight), read forward as the *prior* for the 2026-05-27 open. Prose-only, **0 rubric points, no backtested predictive claim** (predictive validation lives in `/weekly-analysis`). Scope: **SPY and QQQ only.**

Both indices print **POSITIVE (long-gamma)** with spot pinned essentially on the dominant gamma node — a textbook mean-revert / vol-suppression prior that aligns with §2a's premium-sell read. Both regimes flipped POSITIVE on 2026-05-22 and have held 3 sessions (moderately stable, not fresh).

**SPY — spot 750.24 · ZGL 749.65 (reliable, 0.08% below spot) · POSITIVE · total_gex +$1.066B.** Call wall **751** (+172M; secondary 755 +147M). Put wall **730** (−2.7%, −90M; soft support 735). The 750 strike is a +557M monolith — the gravity center, with spot/ZGL/node stacked within a point. **Read:** tight long-gamma pin; dealers sell 751–755 strength, buy 740 weakness → range ~749–755 absent a gap; the 0DTE straddle is rich. **Structure bias:** iron fly / short straddle / butterfly @ 750; downside is a gap-only risk (put wall far).

**QQQ — spot 730.00 · ZGL unreliable (raw 253.67 = deep-OTM extrapolation, discarded) → fall back to total_gex sign +$536M POSITIVE + spot-on-node.** Call wall **740** (+1.37%, +50M; 735 +41M). Put wall nominal 705 (weak); **real support is the 725 +GEX shelf (+52M).** The 730 strike is a +224M monolith — 80%+ of the positive book sits on this one strike, with a **negative-gamma air pocket directly below** (715 −16M, 705 −25M). **Read:** long-gamma pin to 730; range ~725–740 (±1.0–1.4%); no short-gamma downside trap *in the 0–45d book* — but a break below 730 has thin support before the neg-gamma shelf. **Structure bias:** iron fly @ 730 or condor short 725/740.

**Mandatory caveats:** (1) EOD = prior, not the live book — first 30–60 min of 0DTE OI re-computes the walls; re-pull after the open. (2) **Gap risk is live into PCE core Thu 05-28** — long gamma suppresses intraday chop, not gaps; the put walls are gap-tail levels. (3) ETF book, not the cleaner SPX/NDX index book. (4) uw-pp cannot isolate the D+1 expiry (0–45d proxy). (5) SPY's 30d regime oscillates NEG↔POS frequently — **ZGL 749.65 is the short-gamma trip-wire**; QQQ's pin is one strike deep.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — the validated stack)
> The GEX walls above are a **map (where), not a pin to trade directionally** — wall-as-magnet and every directional 0DTE signal backtested NO_GO. What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, NOT a guaranteed edge (validation sample has no vol shock → short-vol tail unsampled).

Both indices: **`GO_PREMIUM_SELL_INTRADAY`** (SPY 96.8% open-win, QQQ 93.5%, n=31). VIX 16.94 → **LOW vol state → size 0.5×.** Long-gamma → quieter next-day range → tighter wings. No stand-aside flag.

| Index | sell_premium | vol_state | implied move | exp. range | size | structure | entry |
|---|---|---|---|---|---|---|---|
| SPY | ✓ | LOW | 0.76% | 0.74% | 0.5× | iron fly / short straddle @ 750.4, wings ±0.74% | enter at/after open once gap resolves; hold to close; **never overnight** |
| QQQ | ✓ | LOW | 1.21% | 1.20% | 0.5× | iron fly @ 730.03, wings ±1.2% | same — gaps beyond wings → stand aside |

SPY ≈ SPX (validated identical). **QQQ weaker** (Nasdaq index book unavailable) — flag lower confidence. Delta-neutral; no directional tilt.

## 2a. Swing Dealer Positioning (1–4 weeks)
`dealer-positioning-strategist` read:
- **QQQ — mild-LONG:** clean NEGATIVE→POSITIVE GEX regime flip 05-22, held 3 sessions, rebuilding gamma; dips dealer-supported. The cleanest constructive index read (carried to §3, then gated).
- **SPY — NEUTRAL-mild-long:** positive-gamma orderly grind, ZGL rising 739→749.65; no pre-directional DEX flip, trend-follow only.
- **IWM — NEUTRAL (fragile):** recovered to positive gamma 05-22 but sat FULLY_NEGATIVE 05-15→05-21; weak gamma base + rates headwind (10Y rising, USD strong) = small-cap drag. Not a swing long.
- **NVDA — SHORT/capped:** 153M +GEX wall pinned at 215 overhead, decaying gamma, −9% off the 05-14 high (235→215). Carried to §3b.
- **MARKET-WIDE FLAG:** **No vanna squeeze anywhere** — every name (SPY/QQQ/IWM/NVDA/META/MSFT/MU/AMD/GOOGL) prints net-vanna NEGATIVE = **call-heavy book**. With VIX low, vanna pressure is latent **downside drift**, not a squeeze tailwind. If vol shocks around PCE/FOMC, dealer un-hedging *amplifies* downside. This is the portfolio-level asymmetry of the day.

## 2b. Sector Rotation
`sector-rotation-strategist`: **`rotation_regime = no_change` (low confidence).** All 11 GICS sectors printed net-positive premium with 5-day persistence ≥0.8 (10 of 11 at 1.0). **There is no de-risking leg** — money is flowing into everything (concentrated in Tech), so this is **concentration, not rotation.** Tech 5d inflow is accelerating (3.30→8.72 $B). No swing-book rotation trade; no short leg (Energy is *stalling*, not reversing).

**ETF flow tape (advisory — strengthens the conditional sector-leader +1, adds no rubric points):**

| ETF | Net prem dir | Persistence | DP positioning | Options urgency | GICS agreement | Leaders |
|---|---|---|---|---|---|---|
| EWY | inflow +$36.0M | strong | $82M/$50M blocks (hedging) | Aug 220C swept $13.4M | n/a (Korea) | instrument-only |
| XLK | inflow +$31.2M | strong | $18.5M ask print | **2027 150C swept ask $34.5M** | agree (Tech 1.0) | MU/AMD/ALAB/MRVL |
| XLI | inflow +$16.0M | strong (cleanest) | accumulation-leaning | PUT sweeps (hedging into strength) | agree (Industrials 1.0) | RKLB/RDW/GE |
| XLY | inflow +$12.6M | strong | — | — | agree (Disc 1.0) | TSLA/CVNA/MELI |
| XLE | outflow −$1.8M | weak (MIXED) | no edge | mild bullish (disagrees) | disagree → watch-only | — |
| XLC | outflow −$0.11M | weak (BEARISH) | mild distribution | no sweeps | disagree → watch-only | — |

Standout: **XLK 2027 150C swept $34.5M and EWY Aug 220C $13.4M** — long-dated, ask-side, institutional upside on Tech/Korea-semis. Reinforces the concentration read, not a rotation.

---

## 3. Swing Setups (1–6 weeks)
**Ranked by conviction score — but note: nothing cleared the gate stack. All five directional candidates were floored to SKIP.** Listed with the full audit so the journal records *why* each was cut, not just that it was.

### 3a. Long swings (regime-aligned) — ALL GATED TO SKIP

| Ticker | Score | Thesis | Pre-risk | Gate cuts | Final |
|---|---|---|---|---|---|
| **AMD** | 6 (LOW) | Clean 5/5 persistent bullish opening sweep (call-side, OI building 7d), +$390.8M 30d cum-flow, Aug 380C + LEAP call ladder; CONFIRM fundamentals (3/4 beats, +35% rev). | half | event_risk −1 (PCE T+2), debate −1 (bear 0.65 ≥ bull 0.65) | **SKIP** |
| **SNDK** | 4 (LOW) | Strongest cum-flow in the union (+$877.5M 30d), OI building 7d; CONFIRM fundamentals (4/4 beats, memory supercycle). | half | event_risk −1, debate −1 | **SKIP** |
| **INTC** | 4 (LOW) | +$248.1M recent cum-flow, OI building; but structured 150C overwrite (muddy), MU-sympathy beta. | half | fundamentals CAUTION −1, event_risk −1, debate −1 (bear 0.75 ≥ bull 0.55) | **SKIP** |
| **QQQ** | 3 (LOW) | Dealer GEX flip 05-22 + accelerating Tech tape (+$616.7M 30d). | half | cluster −1 (dup of AMD), event_risk −1, debate −1 | **SKIP** |

The shared kill-shot: **win-rate 0.85 (bullish_flow) is beta, not edge** — SPY-long benchmarked 1.000 over the same windows (market-excess −0.062, capped to half pre-risk). On top, every long faces PCE T+2 inside its horizon and lost its disconfirmation debate. **No adds.**

**Sweeps (informational, `sweep-tracker`, 0 rubric points):** Only **AMD** is a clean first-class persistent bullish *opening* sweep (5/5, call-side, $2.13B 5d, OI building). **INTC** bullish-lean but structured. **MU and SNDK carry stale bullish tags but TODAY are put-heavy** (5/29 + LEAP put ladders — downside hedging into PCE), flagged as divergences, not longs. **NVDA** bearish but 0DTE call-churn (opening unconfirmed). Mega-caps demoted to hedge-flow watch.

### 3b. Short / fade swings (defined risk only)

| Ticker | Score | Thesis | Pre-risk | Gate cuts | Final |
|---|---|---|---|---|---|
| **NVDA** | 4 (LOW) | CONTESTED, adjudicated SHORT: cum-flow 30d −$300.8M & 90d −$251.6M, **5d −$390M accelerating bearish**; mega-DP DISTRIBUTION (buy_ratio 0.03, sold $215.33 = −$2.66 below mid pre-market); dealer 215 gamma cap. Price −9% off the 05-14 high. **Counter:** multileg sees Jun-2028 215C/225C LEAP-call build (~$48M) — but those fills are **bid-side / sold**, i.e. part of the distribution, not accumulation. | starter | fundamentals CAUTION −1 (3/3 beats fight the short; earnings date UNRESOLVED), event_risk −1, debate −1 (bear 0.65 ≥ bull 0.55) | **SKIP** |

NVDA bearish_flow backtests 0.286 (n=14) — below the 0.50 floor; shorting a 3/3-beat +70%-growth megacap into a positive-gamma pin is low-hit-rate. **Watch, don't trade.** Contrarian-scanner separately found NVDA fails the fade gate (1 of 3 signals, PC z-score 0.00 NORMAL, IV only 34).

**`contrarian-scanner`: zero qualifying fades.** Every Step-0 "crowded long" (MU/AMD/QCOM/PANW…) is NORMAL on pc z-score, not a statistical extreme. CRWD's only real extreme (+2.84σ put) is a BACKWARDATION earnings hedge, not euphoria. No naked shorts of an uptrend; FAIR VRP = thin fade edge. Stand down.

---

## 4. LEAP Builds (6–24 months)
**`leap-positioning-radar`: ZERO candidates clear the 6-of-9 gate stack with DIRECTIONAL_LONG conf >70.** Today's long-dated OI is income-structured or wrong-direction:
- **VALE** (closest near-miss, conf 46.2) — genuine institutional accumulation (buy/sell 2.75, $27.4M DP clustered $16.38–16.50, Jan'27 $22C +25.3k) but **fails the REQUIRED 90d accretion gate** (net +$1.11M MIXED — fresh 30d thesis only) and conviction <70. Routed to accumulation-hunter for a shorter-horizon look, not LEAP-sizeable.
- **EWZ** (conf 41) — 90d flow −$28.3M BEARISH (wrong-direction DQ).
- **TLT** — 265k LEAP-call OI but **calls sold on bid** (covered-call income overwrite), compounded by the rising-rate duration headwind. DQ.
- **AAPL** COVERED_CALL (conf 14, LEAP builds were puts); **META** DISTRIBUTION (conf 19, DP buy 0.31). DQ.

No LEAP-grade directional conviction on the tape.

---

## 5. Volatility Surface
`vol-surface-scout` + `earnings-scout`. Entire scanned universe is **BACKWARDATION** (earnings-season + PCE front-bid cluster); every IV100 name validated genuinely elevated (Goyal-Saretto z 2.1–2.5), not single-day spikes. **VRP only FAIR → premium-selling is NOT sized up; calendars (long back / short front) are the safer expression.**

**Earnings-vol verdicts (next ~14 days):**

| Ticker | ER date | Implied move | Term structure | Verdict | Note |
|---|---|---|---|---|---|
| **MRVL** | 05-27 | ~11% | front 194% backwardation | **SELL VOL (half)** | back-month complacent → half only |
| **CRM** | 05-27 | ~7% | front 119% backwardation | **SELL VOL (half)** | clean front kink, flat tail |
| **PANW** | 06-02 | ~3-4% | **KINK at 06-05** (104%) | **SELL VOL (half)** | cleanest event-expiry kink; small move caps size |
| **CIEN** | 06-04 | ~6% | backwardation, tail priced | **SELL VOL (fuller)** | only name with back-month put-bid → safest short |
| **CRDO** | 06-01 | ~8% | near-flat front, whole curve bid | **BUY VOL** | event under-priced vs structural vol |
| **AVGO** | 06-03 | ~3% | CONTANGO, kink building 06-05 | **CALENDAR / BUY VOL** | sell post-print 06-05 vs long 06-12/18 |
| DELL/OKTA/SNOW | 05-28 | 8-11% | front 163-202% (too hot) | **SKIP** | front-panic >1.10, coin-flip |

**Calendar candidates (no single-name catalyst — pure PCE front-bid, cleanest setups):**
- **SOXX** — front 97.4% vs 58.6% (06-05), PC ~8.4 by volume = macro hedge. Long calendar: sell 5/29 @ 570, buy 6/05/6/18. **(scored — see §7.)**
- **QCOM** — front 137.7% (no near-term earnings, PCE + crowded calls). Sell 5/29, buy 6/18. Small size.

Both calendars: enter **only after** 05-28 PCE confirms the front is crushing, or scale small pre-print — do not put on full size into an un-printed PCE.

---

## 6. Risk & Correlation
`risk-monitor` consuming the Phase-1 union + quant score + fundamentals + debate.

**Macro headline:** disinflation stalling (core PCE 3.2%), 10Y 4.56% rising, USD bid = mild risk-asset headwind. **PCE core Thu 05-28 (T+2) is the dominant event** — inside every swing horizon here.

**Correlation cluster (`risk_portfolio_correlation`, 30d):** `AI_semis_megacap_cluster = {AMD, QQQ, SOXX}` — pairwise 0.79 (AMD/QQQ), 0.81 (AMD/SOXX), 0.85 (QQQ/SOXX). **One position wearing five tickers.** Highest raw_score member AMD is kept; QQQ and SOXX take −1 cluster duplication. INTC/SNDK correlate only in the soft-watch band (≤0.66) — no penalty (mechanical threshold, not discretionarily upgraded).

**Fundamentals verdicts (top 5):** AMD CONFIRM · SNDK CONFIRM · **NVDA CAUTION −1** (3/3 beats + bullish catalyst flood fight the short; earnings date UNRESOLVED — resolve before any hold-through) · **INTC CAUTION −1** (unprofitable, cosmetic beats off floored estimates, mega-DP 100% sell-side into a +93.6% rally) · QQQ NA. **No VETOs.**

**Event-risk gate:** PCE T+2 inside the horizon of all five → −1 each.
**Debate gate:** bear residual ≥ bull on **all five** → −1 each. The disconfirmation step did its job on a crowded, distribution-flavored tape.

**Adverse-flow exit list** (prior group `conviction_2026-05-22` = {F, AMD, RKLB, INTC, TTWO}):
- **AMD — EXIT-CANDIDATE:** $227.9M DP + IV99.5 + OI +86.7k = distribution-into-IV-extreme, off-thesis at size.
- **INTC — EXIT-CANDIDATE:** $99.4M DP + IV82.7, fundamentals flagged 100% sell-side mega-DP.
- **F** — IV100, monitor (richly priced, no hard reversal). **RKLB / TTWO** — bullish flow intact, no exit (TTWO cleanest: PCR 0.39, IV43).

**Hedge sleeve:** book skews >0.6 long in one correlated AI/semis cluster *and* the complex carries latent downside vanna drift into a Tier-1 PCE print with no squeeze fuel.
- **Primary:** QQQ or SPY **put-debit spread** expiring just past PCE (~1–2wk, ~5% wide), sized to neutralize net long-semis delta. Buy the spread / sell the lower leg to fund (vol is rich).
- **Tail:** small **VIX call ladder** (16.94 base) as cheap convexity for the dealer-unhedging-amplifies-downside scenario.
- The NVDA short and SOXX calendar already lean short — size the index hedge to *residual* net long delta.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**None.** No call reached MEDIUM (≥7) or HIGH (≥10) this session. Max raw_score was AMD at 6 (LOW). The HIGH-tier load-bearing-tool gate (Step 3a) is therefore a no-op for all names.

For completeness, the **LOW-tier scored book** (raw 3–6) with full audit trail — all gated to SKIP except SOXX (STARTER):

| Ticker | Raw | Class | Dir | Win-rate (n) | Pre-risk | Fund. | Bull resid. | Gates applied | Final |
|---|---|---|---|---|---|---|---|---|---|
| AMD | 6 | multi_day_sweep | long | 0.85 (16)¹ | half | CONFIRM | 0.65 | event_risk, debate | **skip** |
| SNDK | 4 | bullish_flow | long | 0.85 (16)¹ | half | CONFIRM | 0.65 | event_risk, debate | **skip** |
| NVDA | 4 | bearish_flow | short | 0.286 (14) | starter | CAUTION | 0.55 | fundamentals, event_risk, debate | **skip** |
| INTC | 4 | bullish_flow | long | 0.85 (16)¹ | half | CAUTION | 0.55 | fundamentals, event_risk, debate | **skip** |
| QQQ | 3 | dealer_flip | long | 0.85 (16)¹ | half | NA | 0.65 | cluster, event_risk, debate | **skip** |
| SOXX | 3 | high_iv_rank (calendar) | vol_long | 0.842 (19) | full | NA | — | vrp −1, cluster −1 | **starter** |

¹ bullish_flow raw WR 0.938 (n=16) → N-capped 0.85 → **market-excess gate caps to half** (SPY-long benched 1.000, excess −0.062 → beta in an UPTREND, not edge).

**Invalidation levels:** AMD — close back below 475 (heaviest fresh call OI) or the 380C block proving a roll. SNDK — 5/29 put OI build accelerating + close below 1480. NVDA short (if ever taken) — reclaim/hold >220 (into the 220/230 +GEX shelf) flips dealers supportive; or earnings lands inside the window (binary, invalidate). INTC — 5/29 125C ask-flow drying / 150C overwrite unwinding. QQQ — close below 725 (breaks the pin into the neg-gamma air pocket) or loss of the 05-22 POSITIVE regime ≥3 sessions. SOXX calendar — front fails to crush post-PCE.

**Dropped below floor (raw < 3), journaled:** MU (**−2**, hard −3 flow_conflict — 30d −$381M put-side distribution opposing the stale TOP-bullish tag; thin gamma blow-off). SMH/IWM (1 — multileg put-spread downside hedges, flow_conflict_lite). PANW/MRVL/CIEN (2 — valid SELL-VOL ideas, below conviction floor, surfaced in §5). AVGO/CRDO/QCOM (1 — vol calendars/BUY VOL, §5).

### Conviction-scoring rubric (Step 4) — embedded for audit
```
Daily conviction score = Σ:
 +3 dealer DEX flip / vanna-squeeze in trade direction
 +3 3+ aligned accumulation signals (DP+OI+oi_smart_positioning, block-stratified institutional) — CONJUNCTION: full +3 only when cum_flow_30d confirms (sign-aligned AND |cum_flow_30d|≥$50M); else +3→+1
 +1 multi-day OI build (historical_oi_trend BUILDING, lookback≥5d)
 +1 conviction_matrix DIRECTIONAL_LONG conf>70 — CONDITIONAL: only when dominant_signal_class==leap_directional; else 0
 +3 historical_cumulative_premium_flow net directional accretion in trade direction (30d)
 +2 insights_signal_confluence ≥4 (second-agent confirmation)
 +1 sector single-name leader — CONDITIONAL: persistence≥0.6 AND cum_flow_30d aligned AND |cum_flow_30d|≥$50M
 +1 earnings-scout BUY VOL or SELL VOL
 +2 multileg directional structure (term-structure-anchored)
 +1 vol-surface KINKED/BACKWARDATION watch w/ VRP-aligned bias
 -2 contrarian overcrowded long w/ rising pc_zscore (VRP positive)
 -3 flow_conflict (cum_flow_30d clearly OPPOSITE class) | -1 flow_conflict_lite (MIXED) — mutually exclusive
 -1 correlation cluster (risk 2d) | -3 regime conflict (risk 2d)
Tiers: ≥10 HIGH (full) · 7-9 MED (half) · 3-6 LOW (starter/watch) · ≤2 drop.
Step 5 sizing on win_rate: ≥0.70 full · 0.50-0.70 half · <0.50 starter/skip. Guards (downgrade-only): n<10 cap 0.69; market-excess ≤0 cap half / ≤−0.10 starter; bullish/bearish_flow not-OI-confirmed-opening cap half.
```

## 8. Watch-only — single signal, no confluence
For journaling, NOT trade entry:
- **CRDO** — earnings-scout BUY VOL (06-01, event under-priced) — single agent, no confluence.
- **AVGO** — earnings-scout CALENDAR (06-03) — single agent.
- **CRM** — earnings-scout SELL VOL (05-27) — single agent.
- **QCOM** — vol-surface calendar (no near-term earnings) — surfaced in §5, below conviction floor.
- **VALE** — leap near-miss (fresh 30d accretion, conf 46) — re-check if 90d flow flips BULLISH + conviction >70 while holding the $16.38–16.50 DP shelf.
- **MU** — DROPPED on −3 flow_conflict (put-side distribution vs stale bullish tag); late-stage blow-off on thinning gamma. Not a long.

---

*Generated by the two-phase agent fleet. Phase 1: 10 alpha-finding agents (non-OPEX week). Phase 2: signal-confluence-quant → fundamentals-gate → bull/bear debate → risk-monitor. Decision envelope: `analyses/2026-05-26.decision.json`.*
