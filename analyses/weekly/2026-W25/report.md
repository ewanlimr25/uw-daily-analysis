# Weekly Market Intelligence — Week of 2026-06-15 (ISO 2026-W25)

*Coverage: Mon 06-15 → Thu 06-18 (4 sessions). Fri 06-19 = Juneteenth, market closed — no data. Report compiled post-close 06-19/20. Rubric version `2026-06-12` (frozen).*

## Executive Summary
- **Week regime + WoW Δ:** Regime **HELD TRANSITIONAL / PULLBACK_IN_UPTREND** all week — no improvement, no deterioration. SPY closed 746.74, above its 50-DMA (729.66) but below its 20-DMA (747.08); bullish-flow breadth limped from 37.1% (Mon) to 38.6% (Thu). **VRP FAIR** (SPY −0.005, QQQ −0.027 — IV ≈ realized, a faint premium-buying lean). VIX 16.4 (LOW). The defining event was the **06-17 FOMC hawkish hold**: rates held at 3.50–3.75%, but the 2026 median dot jumped 3.4%→3.8% with 9 of 19 members now seeing a hike (first meeting under Chair Warsh). That repricing — not a sell-off — is what kept the tape "transitional."
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL/PULLBACK_IN_UPTREND) — sizing capped at half`. The P0.6 guard is active; no conviction call can be sized above half regardless of score.
- **Signal performance (intra-week scorecard):** **0 of 2 resolved (hit rate 0/2 = 0%); 0 INCONCLUSIVE excluded; 2 total in universe (2 envelope-anchored, 0 reconstructed).** Both daily calls were directional **shorts** sized `skip` (no capital) — SMH and SPY — and both were run over by the 06-18 semiconductor/market rally. Zero capital impact; the dailies correctly refused to deploy.
- **Top swing build for next week:** **None.** No name cleared MEDIUM tier. The single name above the ≥3 score floor (INTC) was cut to watch-only by the debate gate.
- **Top LEAP build:** **None.** Zero candidates passed the LEAP 6-of-9 gate filter (every semi/AI-hardware name failed the cumulative-premium-flow accretion gate — the build was contested, not clean).
- **Biggest emerging risk:** **The entire semiconductor complex is one correlated bet** (SMH the hub: MU/SMH 0.85, INTC/SMH 0.82, MRVL/SMH 0.78, AVGO/SMH 0.73) sitting on a **contradiction** — surface-bullish flow (sweeps, positive DEX, SMH ETF inflow) layered over heavy downside hedging (broad backwardation, opening put verticals, a Tier-1 INTC put at 72× size/OI, and MRVL/AVGO distribution prints). This is a tape priced for a binary, not a trend.

---

## 0. Week in Review — Intra-Week Signal Performance

Universe = the union of `calls[]` across this week's daily `decision.json` envelopes (06-15…06-18), non-DROP, keyed by `(ticker, direction)` — the pre-committed, hindsight-free record. Thesis direction is read from the envelope as written; outcomes graded with fresh `uw historical trend` from the call date to week-end (06-18). INCONCLUSIVE = |move| < 0.5×ATR(14) (close-to-close ATR proxy per the broken-Yahoo-OHLC workaround).

| Ticker | Direction | Source | Move vs ATR | Flow/OI | Grade | Note |
|---|---|---|---|---|---|---|
| SMH | short | envelope 06-15 | +12.78 (+1.97%) vs 0.5×ATR 11.22 — **against** | Net flow flipped bullish into 06-18 (+$93.7M); semis ripped | **LOSS** | Worked intra-week (616 on 06-16) then SMH rallied to 659.88 by Thu. Sized `skip` — no capital. |
| SPY | short | envelope 06-17 | +5.78 (+0.78%) vs 0.5×ATR 3.40 — **against** | SPY net flow +$75M bullish on 06-18; post-FOMC relief bid | **LOSS** | Called into the FOMC-day weakness; reversed next session. Sized `skip` — no capital. |

**Read:** Both dailies refused to put capital behind their two shorts (`skip` size), and both shorts would have lost into the 06-18 rally (SNDK +11.5%, broad semi bid the day before the holiday). A 0/2 hit rate on two no-capital calls is the system working as designed in a no-edge tape — it surfaced the bearish microstructure, scored it below the deployment bar, and sat out. The denominator is tiny (2 calls, both skip) precisely because the week offered no edge.

---

## 1. Regime & WoW Delta

The market spent the entire week in **TRANSITIONAL / PULLBACK_IN_UPTREND** — the WoW delta is *held*, not improved or deteriorated. SPY sits in a tactically awkward spot: above the 50-DMA (constructive) but pinned at the 20-DMA (747.08), 30-day change +1.77%, 1.8% off the 90-day high. Bullish-flow breadth is weak (38.6% of optionable tickers bullish on Thu) — a green tape carried by a narrow semiconductor cohort, not broad participation.

**VRP** is **FAIR** (SPY −0.005, QQQ −0.027): 30-day implied ≈ realized with a slight premium-buying lean. This is the worst environment for conviction — neither premium-sellers (no rich vol to harvest) nor premium-buyers (no cheap vol) have a structural edge. It de-rates both the contrarian-fade and the earnings-vol books this week.

**Institutional vs retail tape:** market-level DTE share shifted toward duration across the week — weeklies 6.6%→19.4%, monthlies 15.5%→17.7%, 0DTE share 0%. That is a *constructive* institutional-tape signal (rising monthly+ share), but it was not enough to lift any single name to conviction.

**Macro backdrop** (`scripts/fred_macro.py`): yield curve normal (+0.27, 10Y−2Y); core CPI 2.96% YoY, core PCE 3.29% YoY (both sticky, above target); unemployment 4.3%, payrolls +172k (softening, not recessionary); 10Y 4.49% and *falling* (−12bp/30d); USD strengthening; fed funds 3.63%. The **06-17 FOMC hawkish hold** is the regime's pivot: holding 3.50–3.75% while moving the 2026 dot 3.4%→3.8% (9/19 see a hike) is a hawkish surprise that reprices growth multiples and pressures rate-sensitive and high-beta names. The 06-17 single-day Consumer Cyclical outflow (−$1.66B) is the tape registering exactly that.

**Forward event risk (next 2 weeks):** **May Core PCE — Thu 2026-06-26** (T+4 trading days from the report date; *inside* the 1-week swing horizon) and **June NFP — Thu 2026-07-02** (T+8; inside the 2-week horizon). Both are Tier-1. The event-risk gate fires on any undefined-risk structure carried through 06-26.

**Breadth cross-check (`fz`, advisory):** advancers 264 / decliners 238, pct_green 52.5%, top mover SNDK +11.5%, worst ACN −18.0% (earnings). No divergence from the `uw` regime label (mild green tape, mildly positive breadth). Advisory, no size impact.

**Implication for next week's bias:** defensive. A hawkish-hold week with sticky core inflation, a 2.2-beta-led semi tape, and PCE landing T+4 is not a week to chase. Favor defined-risk, half-size, and post-PCE re-entry.

---

## 2. Sector Rotation

**Rotation regime call: `growth→value` (medium confidence).** The persistence-gated read (≥3-day) surfaces **Financial Services** and **Industrials** as the only two sectors clearing the market-relative bar (persistence_score 1.0 *and* 06-18 net-flow above the cross-sector median of $219.6M):

| Sector | persistence_score | 06-18 net flow | Gate |
|---|---|---|---|
| Financial Services | 1.0 | $446M | **ROTATION CALL** |
| Industrials | 1.0 | $492M | **ROTATION CALL** |
| Utilities | 1.0 | $195M | below median — broad tape |
| Basic Materials | 1.0 | $49M | below median — broad tape |
| Real Estate | 1.0 | $40M | below median — broad tape |
| Technology | 0.8 | $9,357M | not top-third persistence (06-17 FOMC outflow day) |
| Healthcare / Cons. Cyclical | 0.8 | $220M / $587M | not top-third |

The hawkish FOMC is the driver: **Financials** lead on NIM repricing into higher-for-longer (the rate-cycle value play), with **Industrials** a concurrent cyclical-capex bid (power grid / data-center buildout). There is **no rotating-out sector** — all 11 are net-inflow — so this is a one-sided rotation *toward* value, not away from growth. Technology's enormous +$9.36B week-end skew is a single-day (06-18) semiconductor spike on 0.8 persistence; it does not clear the rotation bar.

**Named single-name leaders** (sector-rotation only — see §10, these failed the 2-agent confluence gate and are *watch*, not conviction):
- **Financials:** JPM ($794K net, iv_rank 48), MS ($1.2M, iv 53), BLK ($2.4M), C ($705K) — bank NIM + AUM.
- **Industrials:** CAT ($4.8M, iv 57), VRT ($1.1M, iv 60 — data-center cooling), ETN ($1.2M, iv 70 — grid), FIX ($2.0M — HVAC/data-center).

### ETF flow tape (advisory — instrument-level layer the GICS aggregates can't see)

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| SMH | inflow +$138.6M | multi-day bullish | $50–250K clustered prints @ 659.7 (creation/redemption tell) | CALL 640/655 Jul-17 **ask** sweeps (bullish urgency); PUT 650 Oct hedge | disagree (XLK −$14.2M, but SMH = semis sub-sleeve) | MU/MRVL/AMD/TSM |
| GDX | inflow +$44.8M | multi-day bullish | $641–796K blocks @ 82.5–82.9 | CALL 84 Mar / 85 Sep **ask** (6–12mo upside); PUT 70 hedge | partial-disagree (XLB MIXED) | gold miners thematic |
| IGV | inflow +$9.6M | bullish | $188–622K prints @ 89.1 | **PUT-dominated** sweeps (hedging longs, ambiguous) | partial-disagree | — (downgrade to watch) |
| XLK | **outflow −$14.2M** | bearish (instrument) | small $99–117K prints (redemption) | call-bid (closing longs) | disagree — **structural single-name bypass** | MU/SNDK/INTC direct |
| XLI | outflow −$1.6M (noise) | borderline | thin | long-dated Jan-28/Sep-26 **call** sweeps (bullish) | disagree (GICS Industrials 1.0; instrument is bypass noise) | CAT/VRT/ETN |
| XLV | outflow −$3.7M | bearish | thin | mixed | disagree (Healthcare double-weak) | — |

**Systematic finding:** every *broad* SPDR (XLK, XLI, XLF, XLV…) shows bearish/mixed instrument flow while its GICS sector shows 0.8–1.0 inflow. This is the **single-name-direct bypass** — institutions routing megacap orders directly (MU, JPM, CAT) rather than through ETF wrappers — not a directional contradiction. The genuine ETF-level inflows land in *sub-sector/thematic* ETFs (SMH semis, GDX gold, XBI biotech, XOP energy) where single-name substitution is harder. The tape **strengthens** the conditional sector-leader read via cum_flow alignment; it adds **no rubric points**.

**Swing-book implication:** the cleanest *directional* theme of the week is the growth→value rotation (long Financials/Industrials leaders), but every name is single-agent (sector-rotation only) and therefore watch-only. GDX (gold as a real-rate hedge into the hawkish hold) and SMH (semi sub-sleeve) are advisory instrument-level constructive reads.

---

## 3. Swing Book (1–6 weeks)

**No conviction swing calls this week.** No name cleared MEDIUM tier (≥7). The one name above the LOW floor (INTC, raw_score 3) was cut to watch-only by the debate gate — see §8.

**§3a Long swings (regime-aligned):** *empty.* The growth→value rotation leaders (JPM/MS/BLK/C, CAT/VRT/ETN/FIX) are single-agent watch-only candidates (§10), not conviction entries.

**§3b Short/fade swings (defined risk only):** *empty as scored calls.* The dealer-positioning fleet surfaced two clean directional **shorts** that failed the 2-agent confluence gate and remain watch-only:
- **MSFT — watch-only short.** The cleanest dealer read of the week: all-negative DEX across all 4 sessions (06-15 −0.48B → 06-18 −5.17B, deteriorating), put-heavy vanna book, GEX mass grinding to −$161M. The only bullish wildcard is a latent vanna tailwind *if* VIX falls ≥3 consecutive sessions (it did not — FOMC V-spike). Repeat Tier-1 single-leg puts (06-15/16/17) corroborate. Watch for a second agent next week.
- **PLTR — watch-only short.** Crossed DEX negative on 06-17 (thin book, ~−$0.5B). Cluster partner with MSFT (corr 0.83).

**Distribution caution (C28):** MRVL carries an explicit distribution signature — a $4.4B EOD sell-side block on 06-18, conviction-matrix DIRECTIONAL_SHORT 43.5%, DP buy_ratio 0.109 — despite surface-bullish call-ladder sweeps. Do not read MRVL's sweep tape as a long.

---

## 4. LEAP Book (6–24 months)

**No LEAP candidates passed the strict 6-of-9 gate filter.** The entire semiconductor/AI-hardware cohort (MU, MRVL, AVGO, AMD, TSM, CRDO, SNDK) was evaluated and disqualified. The universal discriminator was the **cumulative-premium-flow accretion gate (Gate 4)**: every name returned MIXED 90-day flow — contested, not the clean unidirectional slow-accretion a LEAP build requires.

- **AVGO** — nearest miss (gates 1, 2, 5, 6, 9, 10 pass). The Dec-2027 $430C ask-side print (38:1 ask/bid, +1,967 OI, DTE 547) is the single most compelling institutional LEAP touch of the week, but it is isolated to 06-18 and unsupported by multi-week accretion (90d flow flat +$12.7M) with DISTRIBUTION on 3 of 4 sessions. **Watchlist for W26**: if 30d flow turns net +$50M and accumulation holds near $411, the structure becomes viable.
- **MU / MRVL / SNDK** — disqualified on put-dominated long-dated OI (borrow/financing artifacts on high-short-interest names) and MIXED/SHORT conviction-matrix reads.
- **AMZN, TSM** — wrong-direction 90d flow (AMZN −$272M 30d; TSM reversed to −$174M 30d). **IBIT** — conviction-matrix COVERED_CALL (excluded). **CRDO** — sub-institutional OI volume.

The fleet's structural read: the semis' 10-day OI build is **sector/index rebalancing**, not single-name conviction accumulation. In a TRANSITIONAL post-FOMC tape, new LEAP initiations at elevated IV carry vega + financing drag and a half-size regime modifier — an unattractive entry.

---

## 5. Volatility Surface — WoW Term Structure & Skew Evolution

The defining surface feature of the week is **broad semiconductor backwardation** — the chip complex (SMH, AVGO, AMD, SOXL, SNDK, TSM) was simultaneously in backwardation, the market paying up for near-term protection across the sleeve. This is real event/macro hedging, **not** crowded bearishness to fade.

**Bucket 1 — KINKED with earnings catalyst (→ earnings-scout):**

| Ticker | Kink expiry | Kink IV (06-18) | WoW Δ | IV pctl (n=48, PROV) | front-end ratio | 90d skew | Bias |
|---|---|---|---|---|---|---|---|
| **MU** | 2026-07-17 | 162.8% | **+26.1pp** | 81 | 0.941 (no panic) | COMPLACENT (call-rich) | BUY VOL / calendar — neg VRP, do NOT sell |
| **NKE** | 2026-07-02 | 73.4% | +8.1pp | 98 | 0.618 (kink intermediate) | COMPLACENT→neutral | conditional SELL VOL if per-name VRP positive |
| **WDC** | 2026-07-17 | 120.9% | **−39.1pp** | 100 | 0.893 | COMPLACENT (zero skew) | KINKED but kink **compressing** — monitor |

- **MU** is the cleanest kink: +26pp WoW concentrated at the 07-17 monthly (25,888 contracts), earnings 06-24. But the whole curve is elevated (07-17 *above* the 06-26 earnings expiry) — not a clean isolated kink — and market VRP is negative, so the play is a **calendar (long 07-17 / short 06-26)**, never a naked short.
- **WDC** carries the highest z-score in the universe (+3.18) but its kink is *compressing* (−39pp WoW), which may mean event premium is bleeding early — watch before committing a calendar.

**Bucket 2 — Backwardation, no catalyst (calendar candidates):** *none qualify.* **TSM** is genuine backwardation but its front-end-iv-ratio (1.155) is *above* 1.10 and *steepening* — the hard disqualifier (Taiwan/geopolitical risk premium still active, not a resolving panic). Do not establish a TSM calendar until the ratio falls below 1.05.

**Bucket 3 — single-contract IV outliers:** *none.* The 06-18 `iv-outliers` scan is entirely contaminated by same-day OPEX-expiry artifacts (SOXL 1493%, AMD 758%) — discarded.

**Caveats:** all `iv-percentile-zscore` reads are **PROVISIONAL (n=48** vs the 252-day request) — relative rankings valid, absolute "percentile 100" claims are not full-lookback. Every backwardation call is computed *after* dropping the expired 06-18 bucket (the P1.3 substrate artifact). Calendar-spread concentration sits in the Jul-17 ($11.8B) vs Jun-26 ($4.3B) pair.

---

## 6. Earnings — Recap & 2-Week Lookahead

### (a) Recap — events that printed this week
- **ACN (Accenture) — DISCONFIRMING for short-vol.** Pre-print (06-16) showed iv_rank 84.8 with a genuine 06-18-expiry front-panic (131.5% avg_iv, ratio ~2.46) — the extreme-front-panic disqualifier was active, blocking SELL VOL. ACN then dropped **~−18% on 06-19** (the worst mover of the day), vastly exceeding the implied move. The correct read was BUY VOL / long put / SKIP. Any short-vol seller was trapped. **Calibration lesson:** IT/consulting names with guidance cuts can gap multiples of their implied move — relevant for FDX/NKE below.
- **KR (Kroger)** — printed 06-19 (holiday); no post-print data. PENDING.

### (b) Lookahead — ranked 2-week catalyst scan

| Ticker | Earnings | iv_rank | front-end ratio | Back-month skew | Flow | Verdict | Size |
|---|---|---|---|---|---|---|---|
| **NKE** | 06-30 PM | 93.8 | 1.559 BACKWARDATION | COMPLACENT | bearish net premium | **SELL VOL** (clean 07-02 kink) | half |
| **FDX** | 06-25 PM | 77.8 | 1.602 BACKWARDATION | COMPLACENT | bullish / heavy put vol | **CALENDAR** (front panic) | half |
| **MU** | 06-24 PM | 94.2 | 0.941 CONTANGO | COMPLACENT | **bullish +$522M** | SELL VOL (whole-curve, not clean kink) | half |
| GIS | 07-01 AM | 93.4 | 1.116 (proxy) | NORMAL | flat | SELL VOL — wait to confirm 07-02 bucket | half |
| PAYX / SNX / DRI / TCOM / WGO / FDS | 06-24…07-01 | — | no near-tenor | — | — | **SKIP** (no tradeable earnings-expiry liquidity) | — |

- **NKE** is the cleanest earnings-vol setup: a genuine 07-02 kink (73.4% vs 35.2% front), flat back-month (tail not priced), analyst-cautious + bearish flow. Defined-risk iron condor / short strangle on 07-02, strikes ±2× implied move, close immediately post-print. Half-size (regime).
- **FDX** front-end-ratio 1.602 → calendar (sell 06-26 / buy 07-17); partial ACN-contagion in logistics.
- **MU** is the headline print (06-24, +$522M bullish flow, iv 94) but the elevation is whole-curve, not an isolated kink, so the post-print IV crush may be incomplete — iron condor, defined risk, not naked.
- **analyst-vs-flow:** MU shows analyst/flow *agreement* (both bullish) — that reduces the divergence edge, not the highest-EV setup.

All earnings-vol plays are **half-size** (TRANSITIONAL + FAIR VRP, no naked shorts) and carry **null win_rate** (earnings_vol backtest = NA substrate). These are §5/§6 vol structures, not directional swing scores.

---

## 7. Risk & Correlation (week-candidate universe)

**Headline: NO-EDGE / CAPITAL-PRESERVATION WEEK.** The lowest-conviction weekly the rubric has produced. Zero new deployment is the correct posture.

**Correlation clusters (`uw risk portfolio-correlation`, 30d):**
- **SEMI_MEGACAP_CLUSTER (corr ≥ 0.70):** SMH is the hub — MU/SMH **0.85**, INTC/SMH **0.82**, MRVL/SMH **0.78**, AVGO/SMH **0.73**. The entire semi sleeve is *one* correlated bet. INTC, as the only scored member, is kept; the rest are below-floor/watch.
- **TECH_DIRECTIONAL_CLUSTER:** MSFT/PLTR **0.83** (both watch-only shorts — same negative-DEX thesis).
- Soft-watch (0.60–0.70, no penalty): INTC/MU 0.69, MU/AVGO 0.68, SMH/NVDA 0.65.

**Macro & event risk:** sticky core inflation (CPI 2.96%/PCE 3.29% YoY), hawkish FOMC dots (3.4→3.8%). **PCE 06-26 (T+4) is inside the swing horizon** — the event-risk gate fires (−0.5 step) on any undefined-risk structure carried through the print; **NFP 07-02 (T+8)** is the second Tier-1 event.

**Fundamentals verdict (top-5 = INTC only):** **INTC = CONFIRM** (4-of-4 EPS beat streak, LOW leverage D/E 0.41, next earnings 07-22 outside the immediate horizon) — but with severe carried risks: the stock **gapped +10–11% on 06-18** on an *unconfirmed Trump/Apple social-media catalyst* + a foundry leadership hire; it closed **$133.99 vs a $100.98 analyst target (−24.6% — the market is 25% over the Street)**; net margin −5.9% (unprofitable); beta 2.20; `fz` short-float 3.18% (LOW squeeze — no short-covering tailwind).

**Debate-disconfirmation cut:** **INTC bull 0.55 / bear 0.85 — the debate gate fires.** The bear's strongest unrefuted point is the **Tier-1 opening PUT (strike 150, size/OI 72×) printed on the spike day** — institutional put-buying *against* the accumulation thesis on the exact session price ripped. The bull's strongest unrefuted point is the genuine 90d cum-flow build (+$253.8M). The disconfirmation wins: this is an adverse-selection chase into a 25%-over-target spike, not a clean entry.

**Breadth cross-check:** advancers 264 / decliners 238, pct_green 52.5% — no divergence (advisory).

**Adverse-flow exit list (vs prior `conviction_week_2026-W24` group):**
- **HYG — EXIT CANDIDATE.** P/C 4.12 (near-distress put loading), bearish net flow, IV rank 5 (complacency being hedged). Any long-credit/risk-on carry from W24 is contradicted.
- **MU — MONITOR/harvest.** Flow continuation intact (+$522M, OI +97K) but iv_rank 94 — expensive vol; harvest premium / consider collar. Not adverse for the directional thesis.
- **ACN / KR — CAUTION** (bearish net flow + volume spikes; ACN already printed −18%). **JBL — watch.**

**Hedge sleeve:** the conviction book is effectively zero-deployed, so there is no net delta to hedge. *Conditional:* if the desk re-enters the INTC accumulation thesis post-PCE, hedge the cluster with a 30–45 DTE SMH put spread (front IV 0.10 is cheap in the CONTANGO front) sized ~50% of notional delta. Otherwise, **cash is the correct position.**

---

## 8. High-Conviction Cross-Ref (HIGH and MEDIUM tier)

**Empty — no HIGH or MEDIUM tier names this week.** For completeness, the single name above the LOW floor and its full gate trace:

### INTC — raw_score 3 (LOW) → **FINAL: SKIP / watch-only**
- **Score components (Σ = 3):** +3 OI BUILDING 10 consecutive sessions (accumulation-hunter / `uw oi`; mega-tier DP buy_ratio 0.95 on 06-18, DP defense $127–134) · +1 accumulation conjunction **halved** from +3 (accumulation-hunter / `uw dark-pool block-stratified`; 30d cum-flow +$37.1M is LONG-aligned but below the $50M floor) · −1 flow_conflict_lite (signal-confluence-quant / `uw historical cumulative-premium-flow`; bottom-quartile 30d magnitude).
- **win_rate:** `null` — NA(substrate) (dark_pool_accumulation backtest = 0 rows). **market_excess:** bullish_flow class −14.3pp vs SPY-long (beta, not alpha).
- **fundamentals_verdict:** CONFIRM (tier_adj 0). **debate_residuals:** {bull 0.55, bear 0.85}.
- **gate_verdicts:** regime no-op · vrp no-op · panic no-op (SPY front-end 0.635 contango) · cluster no-op (kept as top semi member) · sector no-op (Tech INFLOW) · fundamentals CONFIRM · **event_risk −0.5 (PCE T+4)** · **debate −1 tier (bear ≥ bull)** · **rubric_regime cap-half (OOR)**.
- **Sizing cascade:** quant pre-risk STARTER → debate −1 tier → **SKIP**. The OOR half-cap is moot (debate already hit the floor).
- **Desk read:** INTC's 90d accumulation (+$253.8M) is structurally real, but a +10% single-day spike on an unconfirmed social-media catalyst, landing 25% above the Street target on a 2.2-beta name, is a textbook chase. The Tier-1 72× put says smart money is *fading or hedging* the spike. Wait for the post-PCE (06-26) digest; re-enter from a lower base only if the spike holds and a second agent confirms.

**Expectancy lens (advisory — C31):** N/A this week — no closed conviction calls and no deployed tier to compute per-tier expectancy against. The honest statement: the week's edge lives in *not* trading, not in any asymmetry.

### Embedded rubric (for audit)
```
Weekly conviction score (FROZEN 2026-06-12) = Σ:
  +3  oi-trend BUILDING full week (--days≥5)
  +3  3+ aligned accumulation + DP block-stratified institutional-tier — CONJUNCTION
        (full only if cum_flow_30d sign-aligned AND |cum_flow_30d|≥$50M; else halved →+1)
  +1  conviction-matrix DIRECTIONAL_LONG conf>70 — CONDITIONAL (leap_directional only)
  +2  oi position-rolls institutional roll into longer-dated LEAP
  +1  cum-premium-flow net directional accretion — INTENT-SCREENED (no distribution_flag; no ex-div sub-parity calls)
  +1  dealer-positioning MECHANIZED DEX flip / vanna squeeze — verified sign change only  [0 for ALL names this week]
  +1  sector-rotation single-name leader — CONDITIONAL (persistence≥0.6 AND cum_flow aligned AND ≥$50M)
  +1  earnings-scout BUY/SELL VOL next 2wk, term-skew aligned (full size)
  +2  multileg directional structure repeated ≥2 days
  +1  vol-surface KINKED/BACKWARDATION worsening WoW + iv-pctl extreme + VRP-aligned
  +1  opex-pin-strategist top-5 (OPEX week)
  -2  contrarian crowded long, rising pc-z (informed-continuation; VRP-positive precondition)
  -3  flow_conflict (cum-flow 30d clearly opposite dominant class)  | -1 flow_conflict_lite (MIXED)  [mutually exclusive]
  [TIER GATES @ 2d, not score_components: -1 tier corr-cluster ≥0.70; -1 tier WoW regime flip]
Tiers: ≥9 HIGH · 7–8 MED · 3–6 LOW · ≤2 drop.  multi_day_sweep = 0 points (removed P0.3).
OUT-OF-REGIME (P0.6): all conviction sizing capped at HALF until ≥30 resolved post-2026-06-12 calls re-validate the tiers.
```

---

## 9. Setups for Next Week

**Next-session GEX advisory (SPY/QQQ only — prose, 0 rubric points).** Backtest verdict **`NO_GO_NO_EDGE`** (`scripts/gex_next_session_backtest.py`, n=96 pooled): walls-as-magnet hit just **26%** vs the 50% baseline — next close moved *away* from the nearest EOD wall more than chance. These walls are dealer context only, never a predictive target.
- **SPY** (EOD 06-18 spot ~747.3): ZGL unreliable (300.05 = extrapolation artifact, `zgl_reliable=false`); total_gex **net negative** 3 of the last 4 sessions → read as **net short-gamma post-OPEX** (the 06-18 monthly mass expired off the book). Call wall **755** (+$88M), put wall **748** (−$119M, essentially at spot). Short-gamma + a put wall at spot = the open has friction directly overhead; a break of 748 toward 735 can *accelerate* rather than absorb. Effective dealer band ~735–755.
- **QQQ** (settled exactly at the 740 OPEX pin): headline total_gex +$1.69B is *inflated by the now-expired +$1.34B 740-strike mass* — strip it and the Monday book is **weakly positive gamma 730–745, short below 728**. Surviving call wall **750** (+$47M), put wall **720** (−$24M). Range-trade above 728; long-gamma/short-vol bias holds while above 730.
- Caveats: EOD = a prior, not a live read; OPEX reset cleared the dominant mass in both books; ETF-not-index book; cannot isolate the D+1 (06-22) expiry; 3-day holiday gap risk into Monday.

**Next-session 0DTE premium-selling setup** (`scripts/zerodte_setup.py`, the *validated* stack — advisory, 0 rubric points). Verdict **`GO_PREMIUM_SELL_INTRADAY`**, but VIX 16.4 = **LOW vol state → size_scalar 0.5**:
- **SPY:** sell premium, expected range ±1.22%, **wider iron condor** (short-gamma: trendier) wings ≈ ±1.22%, or reduce/stand aside. Backtest n=48: win 93.8%, **mean PnL open +0.207% NET** / +0.307% gross (`pnl_basis` = % of underlying spot notional, gross of costs).
- **QQQ:** sell premium, expected range ±1.23%, **iron fly / short straddle centred ~740.1** (long-gamma: quieter/mean-reverting). Backtest n=48: win 89.6%, **mean PnL open +0.297% NET** / +0.397% gross.
- Rules: enter at/after the open once the overnight gap resolves; **never carry overnight** (overnight mean PnL is negative); stand aside on a VIX spike or front-end backwardation. **Promotion bar: permanently advisory/0 points** until a vol-shock day enters the sample AND net expectancy clears a tail-aware bar — win-rate is *not* the metric (negatively-skewed short vol). **The validation sample has no vol shock — the left tail is UNSAMPLED.** Lead with the net line; do not size off the 90% win-rate.

**OPEX book (06-18 settlement — June monthly settled off the 06-18 close, Fri 06-19 = holiday).** This is a *post-settlement* map, not a forward week-ahead structure — next monthly is Jul 17; the week of 06-22 trades the 06-26 weekly. Ranked pin book at settlement: **QQQ 740** (pin_distance 0.03%, +$1.33B GEX wall — settled at 739.76, a near-perfect pin), **TLT 88**, **AAPL 300** (FULLY_POSITIVE, iron-fly textbook), **NIO 5**, **IWM ~295** (gamma wall, not the 290 OI peak). **TSLA 400 disqualified** (negative GEX at pin — short-gamma, vol-event risk through the strike, not a pin).

**Swing setups (dealer-positioning):** zero mechanized DEX flips and zero vanna squeezes qualified this week (the FOMC VIX V-spike broke every ≥3-session run). MSFT (clean negative DEX) is the watch-condition short — a sustained VIX decline into W26 would instead arm its *put-heavy vanna tailwind* (a reversal, not the current setup).

**Pin vs trend:** post-OPEX reset + 3-day holiday gap = highest-uncertainty open of the month. No directional bias is warranted into Monday.

**Highest-conviction actionable setups for the coming week:** **none at conviction.** The actionable items are (1) the defined-risk **NKE 07-02 SELL VOL** and **FDX calendar** earnings-vol structures (half-size, §6), and (2) the advisory 0DTE premium-sell on SPY/QQQ at half-scalar.

**LOW-tier names to track for daily-analysis confirmation:** INTC (post-PCE re-entry watch), MSFT/PLTR (short thesis building a scoring case), the Financials (JPM/MS/BLK/C) and Industrials (CAT/VRT/ETN/FIX) rotation leaders, AVGO (LEAP re-eval if 30d flow turns +$50M).

**Deep-dive hand-off:** skipped — no HIGH-tier names on a no-edge week.

**Single-Leg Whale Persistence (advisory, C19):** the Tier-1 opening-PUT signal *exploded* into FOMC/OPEX — 06-17 threw 25 Tier-1 puts, 06-18 led by **INTC 150 (size/OI 72×)**, WDC 742.5 (16.7×), VRT 325 (5.8×). Repeat Tier-1 put names across the week cluster on **mega-cap software** (CRM, MSFT, INTU on 06-15/16/17; ZS, NOW, COIN) — a coherent bearish single-leg footprint that aligns with the dealer-positioning MSFT/PLTR shorts. Advisory only (0 rubric points); this is live out-of-sample accrual toward the C19 graduation gate (rolling WR ≥58%, ≥60 days, ≥2 regimes). Note: the validated put edge (WR 61–64%) is **bull-regime-conditional** — in this TRANSITIONAL tape it is regime-extrapolated and less reliable.

---

## 10. Watch-only — single signal, no confluence

Surfaced by one agent only; failed the 2-agent confluence gate. For journaling, **not** trade entry.

| Ticker | Single agent | Direction | Note |
|---|---|---|---|
| MSFT | dealer-positioning | SHORT | Cleanest negative-DEX read; repeat Tier-1 puts; top-bearish flow −$78M |
| PLTR | dealer-positioning | SHORT | Crossed DEX negative 06-17; MSFT cluster (0.83) |
| NVDA | dealer-positioning (flat) | — | DEX+ but bearish flow conflict; accumulation FAIL |
| JPM / MS / BLK / C | sector-rotation | LONG | Financials rate-cycle leaders (persistence 1.0) |
| CAT / VRT / ETN / FIX | sector-rotation | LONG | Industrials power-grid/capex leaders (persistence 1.0) |
| GDX | sector-rotation | LONG | Gold-miner thematic (real-rate hedge); instrument-only |
| MU | dealer-pos + sweep (net −1 score) | contested | Top bullish flow +$522M but crowded-long pc-z +1.74 + put-hedge dominant; earnings 06-24 → §6 |
| SMH | sector + dealer + multileg (net +1) | contested | Semi-sleeve bullish flow vs bearish put verticals; cluster hub |
| SNDK / MRVL / AVGO | various (net 0) | contested | Surface-bullish sweeps vs distribution/borrow-artifact signatures |

---

*Phase 1: 11 agents (OPEX week). Phase 2: quant → fundamentals-gate → bull/bear debate → risk-monitor. Watchlist `conviction_week_2026-W25` written {INTC, MSFT, PLTR} for next week's correlation/adverse-flow universe. Rubric `2026-06-12` frozen; OUT-OF-REGIME guard active. All data via the `uw` CLI; `fz` advisory lanes live; macro via FRED.*
