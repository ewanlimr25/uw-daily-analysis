# Daily Market Analysis — 2026-06-05

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / PULLBACK_IN_UPTREND — SPY 737.55 below its 20SMA (746.29), VIX **21.51 spiking +6.1**, breadth 29.4% bullish (4,390 bearish vs 1,831 bullish flow tickers), tape RETAIL_DRIVEN (0DTE 44.4%). **All three index gamma books flipped FULLY_NEGATIVE today**; semis/memory complex broke (MU −13.25%, entire SMH complex at IV rank 100); sector lean = **cyclical→defensive rotation, high confidence**.
- **Next-session GEX (SPY/QQQ):** SPY — FULLY_NEGATIVE (total GEX −$1.81B) · ZGL null/unreliable · no real call wall (token +GEX at 755) / put wall **735** (spot sits 1pt above it) → short-gamma trend/breakout prior, do not sell premium. QQQ — FULLY_NEGATIVE (−$0.93B) · ZGL null · **NO call wall exists anywhere on the book** / put wall **700** → purest vol-expansion setup; loss of 705→700 opens air below. Both flips are 1-session fresh = maximally unstable. — advisory, see §2.
- **Top swing build:** **SHORT IWM** (raw 10, true HIGH) — $430M institutional put ladder (290/282/275/274/265P, Jun18→2027, repeated 6/4+6/5) + synchronized DEX flip + −$132M/30d flow. Debate + event gates cut it **half → starter, defined-risk only** (286/278 put debit spread); invalidation = daily close > 286.08. WR 0.567 proxy (n=67) — tagged beta, not alpha.
- **Top LEAP candidate:** **None qualified** — the entire DTE>180 tape is protective (IWM/XLF/FXI/QQQ/TLT puts, VIX calls, penny lotto). Zero 6-of-9 passes; consistent with a defensive tape.
- **Biggest risk:** **index_de_risk_short_cluster** — IWM/QQQ/SMH shorts are one trade worn three ways (QQQ/SMH corr 0.945; IWM/QQQ 0.796). Express once via IWM defined-risk; QQQ/SMH gated to watch-only. Residual book risk is a **gap-UP squeeze into CPI (Jun 10)** against fresh 1-day-old short-gamma flips; hedge = defined-risk verticals, no VIX calls (vol already paid +6.1).

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — mixed signals, reduce position size, wait for clarity.** Trend PULLBACK_IN_UPTREND: SPY 737.55, below 20SMA 746.29, above 50SMA 713.51, −3.0% off the 90d high. Guidance: half sizes, defined-risk structures. Breadth is decisively risk-off — only 29.4% of optionable tickers carried bullish flow; the fz cross-check (different lineage) agrees: SPX 237 adv / 266 dec, `pct_green` 47.1, avg −0.92% — red index, red breadth, **no divergence**.

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 736.30 | null (unreliable) | **−$1.81B** | FULLY_NEGATIVE (flipped today) | ~755 (token +15M, not a real wall) | **735** (−283M; spot 1pt above) |
| QQQ | 706.14 | null (unreliable) | **−$0.93B** | FULLY_NEGATIVE (first neg day after 10 straight POSITIVE) | **none** — zero +GEX strikes on book | **700** (−267M) |
| IWM | 281.65 | n/a | ~−$1.22B (deepening) | FULLY_NEGATIVE (led the break — flipped 6/4) | n/a | 275/265 ladder strikes |

- `uw options-flow dte-volume-share`: 0DTE 44.4% / weekly 20.2% / monthly 23.4% / LEAP 4.8% → **RETAIL_DRIVEN**. Institutional share (monthly+) only 28.2% — size the swing book at the low end.
- `uw historical vrp`: SPY **FAIR** (IV30 16.5% vs RV30 12.2%, VRP +0.043); QQQ **FAIR** (26.2% vs 21.3%, +0.048). No clean premium-selling or premium-buying edge at the index level; the edge today is in single-name VRP dislocations (§5).
- **Macro backdrop** (FRED): curve normal +0.38 · core CPI 2.99% / core PCE 3.29% YoY (sticky) · unemployment 4.3%, payrolls **+172k printed today (hot)** · 10Y 4.47 flat · USD weakening · FF 3.62. **Event-risk calendar:** **CPI Wed Jun 10 · PPI + claims Thu Jun 11 · FOMC + SEP Wed Jun 17 · claims Jun 18 · OPEX Fri Jun 19** — every Tier-1 print of the month sits inside the 1–4wk swing horizon. Today's hot NFP already forced a hawkish repricing (VIX +6.1, Nasdaq-led selloff).

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book (OI persists overnight) read forward as the *prior* for Monday 2026-06-08's open. Prose-only, **0 points** to the conviction rubric, no backtested predictive claim (validation lives in `/weekly-analysis`'s rolling §2 backtest). SPY and QQQ only.

**SPY — spot 736.30, FULLY_NEGATIVE, total GEX −$1.81B, ZGL null (`zgl_reliable=false`).** Per-strike grid (714–758) is negative at essentially every strike; the only +GEX above spot is a trivial +15.2M at 755 — a soft vacuum ceiling, not a wall. The dominant structure is the **put wall at 735 (−283M), one point below spot**, with secondary acceleration pockets at 740 (−193M) and 730 (−166M). Regime freshness: flipped POSITIVE→FULLY_NEGATIVE **today**, 5 regime crossings in 8 sessions — whippy and unstable. **Read:** dealers are short gamma everywhere and hedge *with* direction — Monday favors trend/breakout and vol expansion, not pin. Hold 735 and the upside is a slow vacuum toward 755; lose 735 and 730 unlocks the steepest amplification pocket. **Structure bias:** debit verticals / directional 0DTE / long straddle on a 735 break. **No short premium, no iron flies.**

**QQQ — spot 706.14, FULLY_NEGATIVE, total GEX −$0.93B, ZGL null (`zgl_reliable=false`).** The grid (683–729) holds **zero positive-GEX strikes — no call wall exists at all**; upside is pure gamma vacuum. Put wall **700 (−267M)** with a nearer cluster at 705. Regime freshness: QQQ held POSITIVE for ~10 straight sessions (5/22→6/4) and ruptured to FULLY_NEGATIVE **in one day** on the semis break — the sharpest, least-distributed flip of the pair. **Read:** purest trend/vol-expansion setup; 705→700 loss triggers the largest amplification node with thin air below. **Structure bias:** short-gamma directional (debit put verticals / long straddle); premium-selling explicitly off.

**Mandatory caveats:** (1) **EOD is a prior, not a target** — Monday's first 30–60min of fresh 0DTE OI re-computes these walls; (2) **ZGL unreliable** on both (null on FULLY_NEGATIVE days) — regime read off total_gex sign + spot-vs-wall; (3) **gap risk voids the prior** — no Tier-1 print Monday, but VIX +6.1 into a weekend on 1-day-old flips means a gap can blow through the walls before any hedging engages; (4) **0–45 DTE proxy** — the CLI cannot isolate the D+1 expiry (near-dated share confirmed dominant: SPY 06-08 $420M, QQQ 06-08 $503M on the expiry heatmap); (5) **ETF book**, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup (validated stack — `scripts/zerodte_setup.py`)
**STAND ASIDE — both indices.** The walls above are a map, not a pin (wall-as-magnet backtested NO_GO).

| Index | sell_premium | vol_state | VIX | implied move | expected range | size_scalar | structure | stand_aside_reason |
|---|---|---|---|---|---|---|---|---|
| SPY | **false** | HIGH | 21.51 | 1.00% | 1.05% | **0.0** | (wider IC ±1.05% if forced) | **VIX spiking +6.1 — short-vol left-tail regime; stand aside** |
| QQQ | **false** | HIGH | 21.51 | 1.67% | 1.53% | **0.0** | (wider IC ±1.53% if forced) | **VIX spiking +6.1 — stand aside** |

Rolling backtest context: GO_PREMIUM_SELL_INTRADAY verdict stands historically (SPY 94.9% / QQQ 92.3% open-entry WR, n=39) **but the validation sample has no vol shock — the short-vol left tail is unsampled, and today is exactly the spike-day the stand-aside rule exists for.** Entry rule (when live): enter at/after the open once the gap resolves; hold to the close; never carry overnight. Delta-neutral only — no directional tilt. Advisory, 0 rubric points.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

**The single dominant signal of the day: a synchronized positive→negative DEX flip across all three indices in one session, confirmed same-day by GEX regime flips into FULLY_NEGATIVE.** Dealers went from long-gamma stabilizers to short-gamma amplifiers with a sell-into-weakness hedge bias.

| Symbol | DEX state | 5d trajectory | Vanna | Charm | Swing bias | Confidence |
|---|---|---|---|---|---|---|
| SPY | **−46.6B** | +75.6B → +51.0B → **−46.6B** (97.6B one-day flip; put_dex −98.7B) | pressure, NOT squeeze (put-heavy + *rising* VIX) | −3.14M (downside drift into OPEX) | SHORT-to-NEUTRAL | med-high |
| QQQ | **−24.3B** | +72.3B → +53.0B → **−24.3B** (~77B flip) | pressure, not squeeze | −1.67M | **SHORT** | **high** — first FULLY_NEG day in window, freshest de-risk |
| IWM | **−15.1B** | +10.5B → +10.2B → **−15.1B** (full sign flip; put_dex −27.6B) | pressure | −2.89M (heaviest vs book size) | SHORT-to-NEUTRAL | med — led the break 6/4, most already-in-tape |
| MU | +14.0B (halved in one day) | +31.2B → +32.1B → +14.0B | call-heavy + falling IV = **selling** pressure | −58k | SHORT (sell rips; bounce risk) | med |
| SMH | −4.5B (put_dex −11.4B) | flipped today | **SQUEEZE-WATCH** — put-heavy + rank-100 IV; 3-session semis-IV lower-high = swing-LONG reversal trigger | **−586k** (heaviest decay-drift) | SHORT but squeeze-watch | med |
| AMD | +10.7B (halved) | +13.8B → +18.7B → +10.7B | call-heavy, falling-IV selling | **+120k (only positive)** | NEUTRAL — signals disagree, disqualified | low |
| LLY | **+3.4B** call-heavy (put_dex only −0.31B) | stable | n/a (defensive) | +28k supportive | **LONG (defensive)** | med |

**Critical vanna caveat:** every index book is put-heavy, which arms a vanna *squeeze* only if VIX rolls over — but VIX is **rising**, so all three are vanna *pressure* (dealers sell as |put delta| grows). No index BUY setup until VIX prints ≥3 sessions of lower highs. **SMH is the name to watch for that flip.** The clean pair on the swing book: **LONG LLY / SHORT IWM-or-QQQ** — carried into §3. Invalidations: index DEX re-flips positive ≥3 sessions, or a VIX peak + put-heavy books flipping to genuine squeeze.

## 2b. Sector Rotation

**Rotation regime call: `cyclical→defensive` — high confidence** (with growth-out as corroborating second axis). The persistence tool is non-discriminating this week (every sector 1.0), so the call rests on **magnitude trajectory + ETF cross-confirm**: Tech net flow collapsed 13.1B→8.3B→9.5B→5.4B→**3.8B** across the week (−71%) while Healthcare firmed 216→128→258→226→**305M** and Staples 50→62→65→100→**96M**. Daily-synthesis delta-based rotation agrees: OUT of Tech/CommSvcs/ConsCyclical, INTO ConsDefensive/Healthcare.

**ETF flow tape (advisory — instrument layer):**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| XLV | inflow | BULLISH | **$38.5M 250k-share block @154** | $30M Jan-2027 152C sweeps (long-dated upside) | **agree** → high-conviction | UTHR, LLY, JNJ |
| EWT | inflow | BULLISH | $60M block at ask (+0.52 vs mid) | Jun 100C ask-side sweeps | n/a (geo) | — |
| XLE | inflow | BULLISH (XOP confirms) | near-mid neutral | mixed Sep 55P / Jun 60C | **disagree** (GICS decaying) → watch-only | — |
| IGV | **outflow −22.8M (largest in universe)** | BEARISH | prints above mid but swamped | Jul 103P ask-side sweeps ×200 | **agree** → high-conviction outflow | — |
| XLY | outflow −8.5M | BEARISH | near-mid | put-lean (Jul 118P) | agree | — |
| XLI | outflow −2.9M | BEARISH | wide-NBBO low signal | Jul 165P/Jun 170P ask-side | **disagree** (GICS +$250M, FIX/CMI bullish) → watch-only | FIX, CMI (watch) |

Leaders feeding §3 with the `sector_rotation` tag: **UTHR** (+$18.8M, IV rank 13.9 cheap), **LLY** (+$17.0M, RS new-high), **JNJ** (+$6.7M, P/C 0.20), WMT/PG/COST (Staples, sub-$50M each). **Industrials and Energy are watch-only** until the ETF/GICS disagreement resolves. Caveat: 0DTE share 44.4% = not a strongly institutional tape; size defensive longs at the lower end. Binary regime-decider: hot CPI accelerates the rotation, cool CPI snaps growth back and invalidates it.

---

## 3. Swing Setups (1–6 weeks)

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **IWM (short)** | **10 — HIGH** | $430M put ladder + DEX flip + −$132M/30d flow; small-cap = highest-beta loser of hawkish repricing | **286/278 put debit spread** (defined-risk; no naked short into CPI) | Daily close > **286.08** (DP shelf/gap mid); hard stop > 287.67 | **Starter** (gated from half: event −1, debate −1) |
| **LLY (long)** | **9 — HIGH** (MEDIUM in envelope per validator band) | Only supportive dealer book on the board + +$62.6M/30d flow + defensive-rotation leader + CONFIRM fundamentals | Stock or call vertical (e.g. Aug 1140/1200 call spread); defined-risk through CPI/FOMC | Close < **1105** breakout shelf; or DP blocks migrating below spot | **Starter** (gated from half: macro-event beta) |
| QQQ (short) | 4 — LOW | Freshest DEX flip (10 sessions POSITIVE → FULLY_NEG) but 30d flow opposes, entry late −5.3% | — | Reclaim ~700-705 w/ GEX re-flip | **Watch-only** (corr −1, event −1, debate −1) |
| SMH (short) | 3 — LOW | Complex-wide put_dex/charm pressure, but P/C *below* its own mean + IV pctl 100 = squeeze fuel loaded | — | 2nd lower IV-high + 50DMA hold = vanna-reversal trigger (would flip bias LONG) | **Watch-only** |
| JNJ (long) | 3 — LOW | $164M mega-tier DP @BR 1.00 — but debate showed the Jul 220C "build" is **bid-side written** (buy-write leg) inside the May-26 ex-div window; confluence **neutralized** | — | Close < **232.77** DP shelf; thesis revives only on 30/90d flow follow-through | **Watch-only** |
| PGR (long) | 3 — LOW | Block-tier BR 1.00 pure-buy + screen-confluence 5; insurance defensive leadership; flow near-zero | Starter stock/short put | Close < **204.02** DP shelf | Starter |
| FCX (long) | 3 — LOW | Largest 5d OI build on board (+99k) + screen 5; but flow bottom-quartile and ⚠ distribution caution below | Starter only | Close < **63.37** DP shelf | Starter |

**Invalidation discipline (C34):** every level above is a real institutional dark-pool level (IWM 286.08 shelf/281.65 battle line, LLY 1105 breakout shelf, JNJ 232.77, PGR 204.02, FCX 63.37), not a guessed percentage.

### 3a. Long swings (regime-aligned: defensive rotation)
- **LLY** — the clean long. Dealer book call-heavy with almost no put hedging (+3.4B DEX, put_dex −0.31B), +charm; 4/4 beats, rev +47% YoY, GLP-1 catalyst stack; earnings 8/5 (outside horizon). Bear's surviving point (sizing, not direction): DEX *decayed* 3.47B→3.36B while spot rose +1.4% — call-trimming into strength — and accumulation-hunter saw DP sell-lean 0.72. Debate cleared (bull 0.65 > bear 0.55); IV rank 32.5 says the vol surface prices orderly continuation, not exhaustion. Note: `uw playbook batch-scan` returned "No Clear Edge — Stay Flat" on LLY — the rule-based scan does not see the dealer-positioning axis; the dealer read governs (noted disagreement).
- **JNJ** — ⚠ **neutralized, watch-only.** The bear landed hard: `uw oi smart-positioning` shows the marquee Jul 220C build at net_ask_bid **−739** (bid-side, inferred bearish) = the written call leg of a **buy-write** against the $164M DP stock print, sitting inside the **2026-05-26 ex-div ($1.34) dividend-capture window** — the exact blind spot in project memory. buy_ratio of exactly 1.00 is a mechanical-wrap signature. C28 distribution_flag is clean and fundamentals CONFIRM, so this is dead-money/mislabeled rather than short-able — watch for 30/90d flow follow-through before touching.
- **PGR / FCX** — starters. FCX carries a **distribution caution (C28):** ⚠ 2028 70C LEAP closed −2,084 OI on 3,241 vol (~$6.5M) and fresh 80C adds are bid-side (call supply) — a two-sided build, advisory only, sizing unchanged.
- Watch-list longs that failed gates: **UTHR** (1-agent, cheap IV — the best of the unscored), WMT, PG, COST, **STM** (+$53M single-day whale, no persistence), **SNDK** (3-of-5 sweep persistence + $377M/5d flow but zero co-flag confirmation and −$114M today against a broken complex), **GLD** (single-day Sep 500/550 call spread, no repeat).

### 3b. Short / fade swings (defined risk only)
- **IWM** — the desk's one live directional short; see §7 for the full audit. Express **once** for the whole index cluster.
- **MCD** — bearish watch (raw 1, below floor): mega-tier DP **BR 0.00 ($84M sold)** + block BR 0.19 sell-dominant **+ Tier-1 single-leg 310P** (C19) — the strongest DP-distribution × put-print co-confirmation of the day; needs a second scored agent to act.
- **BSX** — logged, not traded: DP distribution real (mega BR 0.00) but 30d flow +$30.5M *opposes* the short — the disagreement is itself the signal. NKE/PYPL/ISRG carry Tier-1 puts but DP shows *accumulation* (divergence, no co-confirm); HD/ABT/TMUS puts sit on neutral DP.
- **MU fade (contrarian)** — dropped on a 3-way conflict: contrarian says fade the put crowd (z +3.24, capitulation in the 765P), dealer-positioning says sell rips, vol-surface says no VRP edge with earnings ~Jun 25 propping the front. Tactical defined-risk put-credit-spread only if you must; not on the book.

**Sweep tape (informational, 0 points):** the persistence book is ~all index/mega-cap hedge flow — every mega-cap returns MIXED 30d cum-flow and demotes (NVDA, TSLA, AVGO, MSFT, META, AMD, AAPL, AMZN, GOOGL). The big SPX prints are a textbook collar (Dec 7000C bought / Dec+Jun 8000P) = protection demand into CPI/FOMC. Genuinely directional residue: **SNDK bullish** (only name passing every sweep gate; relative-strength divergence against its own broken sector) and **MRVL = trap** (5-of-5 bullish persistence label is stale — today −$63M with a $1.58M ask-side 165P; do not buy the label). 634 closing-antisignal prints on the day. All 14 Tier-1 single-leg whale prints were **puts** (PYPL, REGN, ISRG, TMUS, BSX, NKE, AMD, ABT, HD, AAOI, NOC, MCD, MP, IRDM) — a uniformly bearish institutional single-leg tape (C19 advisory).

---

## 4. LEAP Builds (6–24 months)

**Zero qualified candidates** — and that is itself the read: the DTE>180 tape is structurally defensive. Every material long-dated build is (1) index/ETF downside protection (IWM 270115P-290 ×113k / XLF / FXI / EWY / QQQ / TLT puts), (2) vol hedging (VIX Dec-26 70C), or (3) deep-OTM penny lotto (LAES, NOK).

Disqualified near-misses:
- **XLF** (3/9 gates): oi-trend BUILDING + DP accumulation 1.69, but the DTE>180 builds are protective puts + 43%-OTM call overwrites; conviction-matrix **HEDGED_LONG** (rejected scenario); cum-flow flat (+$0.6M/30d on $190M two-sided).
- **IWM** (1/9): largest build on the tape but it is the bearish ladder — conviction-matrix **COVERED_CALL** (rejected); feeds the §3 short, not a LEAP long.
- **NOK** (1-2/9): +37%/30d momentum with 50–110% OTM penny LEAPs = retail signature; cum-flow negative both windows.

---

## 5. Volatility Surface

**Structural finding — the 0DTE classification trap:** five names flagged BACKWARDATION (SNDK, WDC, TSM, MAR + MU-adjacent) are **false positives** — the expiring 06-05 chain prints absurd IV (WDC 392%, SNDK 224%, TSM 176%) and drags the classifier; `front-end-iv-ratio` was **unreadable across the board today** (panic gate stood down as NOT_EVALUABLE). Drop the 0DTE node and every one is clean CONTANGO from 7DTE out. The only genuine backwardation is **KLAC** (13d 70% → 42d 64%) — a marginal FAIR-VRP calendar, watch-only.

| Ticker | TS class (artifact-corrected) | IV30 | IV pctl (z) | VRP | Dislocation | Structure |
|---|---|---|---|---|---|---|
| **AMD** | CONTANGO clean | 71% | 97 (+0.99) | **−0.262 (deepest neg on board)** | IV 71% vs realized 97% — most underpriced vol in semis | **BUY VOL** — long Jun26/Jul17 ATM straddle (half) |
| **MRVL** | CONTANGO (front 150% = borrowed macro/MU fear, no own earnings until Aug) | 110% | 100 (+1.56) | **−0.126** | Cheap vs realized at pctl 100 (Goyal-Saretto) | **BUY VOL** — long straddle (starter) |
| **WDC** | CONTANGO from 7d | 85% | 79.5 (+0.97) | **+0.179 (richest on board)** | Clean front-to-back decay 101→87, NORMAL regime | **SELL VOL** — Jun26/Jul17 IC (half) |
| SNDK | CONTANGO from 7d | 107% | 84.6 | +0.066 thin | Only genuine sell-VRP in memory complex | SELL VOL small |
| MU | CONTANGO + Jun18 hump 133% | 104% | 100 (+1.58) | −0.019 FAIR | **Event-driven (earnings ~Jun 25) — hold, no crush edge** | PASS → earnings-scout |
| KLAC | **real mild BACKWARDATION** | 64% | 92.3 (+1.77) | +0.039 FAIR | CPI/FOMC hump, no VRP cushion | Calendar watch-only |
| ON / TSM | CONTANGO | 73%/46% | 95/82 | ~0 | Rank is noise (VRP-corrected) | Pass |

Earnings-vol book (earnings-scout — every liquid candidate is an IV-crush *sell*, no liquid BUY VOL setups):
- **ORCL** — SELL VOL half: IC 06-12 ±7.5% (short ~230C/197.5P). Front 126% vs 86% next tenor. ⚠ **prints Jun 10 post-mkt = CPI day (double event)**; back-month COMPLACENT → half only.
- **CHWY** — SELL VOL half: 06-12 strangle ±13.5%. Hump 111%→76%. Prints Jun 10 pre-mkt (CPI day).
- **ADBE** — SELL VOL half: IC 06-12 ±6.5%. Hump 93%→68%. ⚠ prints Jun 11 = PPI day.
- **LEN** — SKIP (the only TAIL_HEDGING back-month — gate satisfied — but hump too shallow at 5.9% and rate-levered straight into FOMC). **ACN/KR** — SKIP (flat/unreadable back-month skew, 13d early). **SAIL** — genuine backwardation, macro-free window (Jun 9), but untradeable at desk size.
- Lottery-skew advisory (C6, 0 points): MU/MRVL/AMD all print COMPLACENT 1y skew (0.86–0.89, calls bid over puts) — Boyer-Vorkink overpriced-OTM-call color only.

---

## 6. Risk & Correlation

**Macro headline:** curve normal +0.38, core CPI 2.99%/PCE 3.29% sticky, payrolls +172k hot (today), 10Y 4.47, USD weakening. **Forward calendar: CPI Jun 10 → PPI/claims Jun 11 → FOMC+SEP Jun 17 → OPEX Jun 19 — the entire swing horizon is event-dense; every directional call took an event-risk downgrade.** Breadth line: 237 adv / 266 dec (`pct_green` 47.1) — red tape, consistent with the red index, **no breadth divergence flag**.

**Correlation clusters (`uw risk portfolio-correlation` vs today's candidates):**
- **index_de_risk_short_cluster** — QQQ/SMH **0.945**, IWM/QQQ 0.796, IWM/SMH 0.786. One trade worn three ways (debate independently confirmed the triple-count). **Kept IWM (raw 10); QQQ and SMH −1 corr each → watch-only.**
- semis_beta_complex — SMH/AMD 0.848, SMH/WDC 0.79: AMD/WDC are non-directional vol structures, no same-direction penalty; book-beta awareness only.
- SMH/FCX 0.809 but **opposite directions** — partial internal hedge, no penalty.

**Gate stack outcomes (full verdicts in §7):** regime — no conflicts (shorts align with PULLBACK; LLY/JNJ are rotation-aligned defensives); VRP — no-op (FAIR); **panic — NOT_EVALUABLE** (front-end-iv-ratio is a 0DTE-Friday artifact; stood down explicitly, not skipped); fundamentals — LLY CONFIRM, JNJ CONFIRM (yellow flags: insider_trans −9.8%, flow non-confirm), ETFs NA; event-risk — −1 on both index shorts (CPI+FOMC stacked), −½ step on the defensives; **debate — fired on 4 of 5** (IWM 0.65/0.65, QQQ 0.55/0.55, SMH 0.55/**0.75**, JNJ 0.65/0.65; only LLY cleared).

**Adverse-flow exits (vs `conviction_2026-06-04`):** **MU — EXIT** (bearish −$75.8M, −13.25%, complex broke; thesis dead). **NEE — EXIT** (bearish flow; the prior bullish read was the known dividend-capture artifact). ORCL — monitor (flow bearish but it's now a vol play into the print). ACN, TPR — hold, no adverse reversal.

**Hedge sleeve:** post-gate the cluster collapse leaves net tilt *below* the 0.6 trigger — no mechanical sleeve required. The residual risk is a **gap-UP squeeze into CPI** against 1-day-old short-gamma flips: express the IWM short as the 286/278 put debit spread (caps squeeze damage), and a small ~2wk SPY 730/715 put vertical hedges hawkish-CPI beta on the LLY long. **No VIX call ladder — vol already spiked +6.1; you'd be paying the top.**

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Expectancy lens (advisory — C31)** `[advisory — expectancy is not yet a live sizing axis]` — realised per-tier terminal expectancy from the 2026-05-30 calibration audit: HIGH n=44, WR 59.1%, **expectancy −1.24%/trade, payoff R 0.71**; MEDIUM n=107, WR 53.3%, **+3.18%, R 1.47**; LOW n=65, WR 50.8%, −0.97%, R 0.80. Tier expectancy is **non-monotone** — the book's realised asymmetry lives in MEDIUM, and HIGH-tier conviction has historically carried *negative* terminal expectancy (Kelly sizer stays ADVISORY_ONLY). Today's aggressive gating of two true-HIGH calls down to starters is consistent with that finding.

### IWM — SHORT — raw 10 (true HIGH; LB gate 3/5: dex ✓ cum-flow ✓ confluence ✓)
| Field | Value |
|---|---|
| score_components | +3 DEX flip short (dealer-positioning, `uw options-structure dex`: +10.2B→−15.1B) · +2 multileg directional ladder (multileg, `uw hot-chains multileg`: $430M 290/282/275/274/265P, repeats 6/4+6/5) · +3 cum-flow aligned (quant, `uw historical cumulative-premium-flow`: −$132.3M/30d, −$1.07B/90d) · +2 confluence (quant: dealer+multileg+leap-radar context) = **10** |
| dominant class / win_rate | dealer_positioning_flip · 0.567 (n=67, **bearish_flow proxy** — no backtest class for DEX flips) · market-excess **−0.13 → beta tag** |
| pre-risk → final | half → **starter** (event −1: CPI+FOMC in horizon + Russell reconstitution distortion; debate −1: bear tied 0.65 — post-gap chase, pc-z +0.265 NORMAL, 0 fresh rolls, today's tape printed net-bullish +$55.2M) |
| fundamentals / debate | NA (ETF) · bull 0.65 / bear 0.65 — gate fired |
| gate_verdicts | regime no-op · vrp no-op · panic NOT_EVALUABLE · cluster KEPT-member · sector no-op · fundamentals NA · event_risk −1 · debate −1 |
| structure / invalidation | 286/278 put debit spread · **daily close > 286.08** (hard stop 287.67) |
| disagreement notes | `uw playbook batch-scan` reads IWM single-day flow as *bullish* ("Aggressive Long Calls") — same polarity ambiguity the bear flagged on the ladder prints; the multileg read (actual coordinated structure) governs per the standing rule, but the disagreement is real and is why this is a starter, not a half. |

### LLY — LONG — raw 9 (true HIGH; recorded MEDIUM in envelope per validator band; LB gate 3/5)
| Field | Value |
|---|---|
| score_components | +3 dealer swing LONG (dealer-positioning, `uw options-structure dex`: +3.4B call-heavy, put_dex −0.31B) · +3 cum-flow aligned (quant: +$62.6M/30d) · +2 confluence (dealer+sector) · +1 sector leader conditional met (sector-rotation, `uw options-flow sector-flow-persistence`) = **9** |
| dominant class / win_rate | dealer_positioning · 0.392 (n=74 bullish_flow proxy — pullback-window beta-long; C2 capped) |
| pre-risk → final | half → **starter** (event −½: macro-beta through CPI/FOMC unhedged) |
| fundamentals / debate | **CONFIRM** (4/4 beats, rev +47%, earnings 8/5 outside horizon; RSI 68.4 flag) · bull 0.65 / bear 0.55 — **cleared** (only name to clear) |
| gate_verdicts | regime no-op (defensive-aligned) · vrp no-op · panic NOT_EVALUABLE · cluster no-op · sector favorable · fundamentals CONFIRM · event_risk −½ · debate clear |
| structure / invalidation | stock or Aug call vertical, defined-risk · **close < 1105 shelf** or DP blocks migrating below spot |
| bear color (monitor) | DEX decaying into the rip (3.47→3.36B as spot +1.4%); accum-hunter DP 0.72 sell-lean; batch-scan "no edge". The vol surface (IV rank 32.5) sides with absorption over distribution. |

**Deep-dive hand-off:** `stock-deep-dive` skill not available in this session — *Recommended deep dive: `/stock-deep-dive IWM` and `/stock-deep-dive LLY`*.

<details><summary>Conviction-scoring rubric (verbatim, for audit)</summary>

```
Daily conviction score = Σ:
  +3  dealer-positioning-strategist flags DEX flip or vanna-squeeze setup in trade direction
  +3  3+ aligned signals in accumulation-hunter (DP + OI + uw oi smart-positioning, uw dark-pool block-stratified institutional-tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms (sign aligned AND |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1. A sub-$50M flow that halves this line does not separately qualify for the +3 cum_flow line.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — ONLY when dominant_signal_class == leap_directional; else 0
  +3  uw historical cumulative-premium-flow net directional accretion in trade direction (30d window)
  +2  uw insights signal-confluence ≥4 (second-agent confirmation)
  +1  sector-rotation single-name leader — CONDITIONAL: persistence ≥0.6 AND cum_flow_30d aligned AND |cum_flow_30d| ≥ $50M
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising pc-ratio-zscore (VRP positive)
  -3  flow_conflict — 30d cum-flow clearly opposite dominant_signal_class (mechanical)
  -1  flow_conflict_lite — 30d cum-flow MIXED (mutually exclusive with flow_conflict)
  -1  risk-monitor correlation cluster (corr > 0.7) — applied in 2d
  -3  uw risk market-regime conflicts with trade direction — applied in 2d
Tiers: ≥9 HIGH (full, subject to 3-of-5 LB gate + win-rate ladder) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 drop.
Win-rate ladder: ≥0.70 full · 0.50–0.70 half · <0.50 starter/skip. Guards: n<10 caps at 0.69; market-excess ≤0 caps half (≤−0.10 starter); non-OI-confirmed flow caps half.
```
</details>

---

## 8. Watch-only — single signal, no confluence

| Ticker | Source agent | Signal | Why excluded |
|---|---|---|---|
| MCD (short) | accumulation-hunter | Mega-tier DP BR 0.00 ($84M sold) + Tier-1 310P co-flag | 1 scored agent; C11 halved (flow −$39.9M < $50M); raw 1 |
| BSX (short) | accumulation-hunter | DP distribution (mega BR 0.00) | 30d flow +$30.5M opposes — disagreement nets to 0 |
| TJX (long) | accumulation-hunter | Mega $105M BR 1.00, conviction 61.2% | Single-mega-print dependent; flow +2.9M bottom-quartile; raw 1 |
| SNDK (long) | sweep-tracker | 3-of-5 sweep persistence, +$377M/5d, OI building | No co-flag (accum/multileg silent); −$114M today; broken complex |
| UTHR (long) | sector-rotation | +$18.8M, IV rank 13.9 | 1 agent; flow < $50M conditional |
| STM (long) | sweep-tracker | $53M single-day net, Oct 100C whale | No persistence history |
| GLD (long) | multileg | Sep 500/550 call spread $29M | Single-day, no repeat; Step-0 flow −$21.9M opposes |
| WMT/PG/COST (long) | sector-rotation | Staples leaders | 1 agent each, sub-$50M flows |
| MU (fade) | contrarian | pc-z +3.24 BEARISH_EXTREME + capitulation | 3-way agent conflict (dealer says short, vol says no edge) |
| KLAC (vol) | vol-surface | Only genuine backwardation on the board | FAIR VRP — no edge to pay for |
| SMH-reversal (long) | dealer-positioning | Vanna-squeeze BUY trigger | Conditional: arms only on 3-session semis-IV lower-high |

---

*Generated by /daily-analysis · 11-agent Phase-1 fleet (opex-pin omitted, June OPEX 14d out) · Phase-2 quant → fundamentals → debate → risk · decision envelope: `decision.json` (schema 1.2) · sources: `uw` CLI EOD parquet 2026-06-05, FRED, Finviz (`fz`), Finnhub.*
