# Phase 1 digest — 2026-W34 (Mon 2026-08-17 → Fri 2026-08-21, FULL 5-day week, WEEK_END = monthly OPEX Friday)
All 12 agents returned. This is the union handed to Phase 2.

## Agents returning an EMPTY book (not a failure — the correct output)
- **accumulation-hunter**: ZERO tickers clear. Tested 18 candidates (from 33 funnel names with DP prominence on ≥2 of 5 days) through full trade-level decontamination. All disqualified.
- **leap-positioning-radar**: ZERO. IBIT was the only funnel name with LEAP-scale OI adds; hard-failed the required accretion gate (90d net flow = 3.35% of gross; `rolls_detected: 0` on all 5 dates; conviction-matrix MIXED at 1.1% confidence).
- **opex-pin-strategist**: ZERO. Aug OPEX expired today; next monthly 2026-09-18 (28d out). One forward candidate (DCI) killed on pin_distance 3.44% > 2% with thin 1,976 OI.
- **dealer-positioning-strategist**: ZERO scored DEX flips out of 15 names tested via `scripts/dex_flip.py` on 14 ISO dates.
- **contrarian-scanner**: ZERO BULLISH_EXTREME out of 91 names. 3 BEARISH_EXTREME, all disqualified.
- **vol-surface-scout**: ZERO calendar-spread candidates qualify.
- **gamma-flip-tracker**: advisory only, 0 rubric points by construction.
- **single-leg whale**: advisory only, 0 rubric points permanently (C19 CLOSED as REFUTED).

## LONG-side candidates

### GLD — 2 agents, aligned  [CLEARS CONFLUENCE]
- multileg-strategist: near-term call vertical, **2-day rolling structure**. 08-18: 410C/430C exp 2026-09-04, exact size match 55,292 both legs, 430C confirmed **ask-side/bought**. 08-19: rolled to 430C/445C exp 2026-09-11 (430 anchor retained, upper strike rolled up). ~$92.2M. Separate single-day LEAP call vertical 525C/530C exp 2027-06-17, ~$115.2M.
- sweep-tracker: bullish persistence 3-of-5 sessions, $686M premium — but smart-money-flow direction **unconfirmed** (did not surface in the market-wide top-100 either side).
- Term-structure anchor: front CONTANGO (21.6%→~30% dte3→dte10-14) flattening to ~27% at dte56. No JH/PCE kink. play_type directional.
- Opening/closing: OPENING/rolling forward. Not an expiry-driven close. Does NOT use the dying 08-21 expiry.
- Event exposure: near legs (09-04/09-11) span JH + PCE — positioned FOR a dovish/weak-dollar reaction.
- Macro tailwind: USD weakening 30d, 10Y rising, core PCE 3.29% sticky.
- Note: GDX (gold miners) is the **worst-outflow ETF in the entire 21-name universe** (-$26.4M/5d) and its $44.4M of Friday "call premium" is mostly **call-selling at the bid**. Gold-metal flow and gold-miner flow disagree this week.

### MSTR — 2 agents, one conflicting  [CLEARS CONFLUENCE, with conflict noted]
- multileg-strategist: deep-ITM **LEAP call vertical exp 2028-12-15**, long 100C / short 110C, both strikes below spot 119.26 (deltas 0.81/0.79) = stock-replacement structure. Repeated 2,000-lot clips, 9+ per strike = sliced worked-order signature. ~$594.8M notional. **Single day only (08-21)**.
- vol-surface-scout: genuine hygiene-corrected WoW dislocation — `base_shape` CONTANGO(Mon) → **BACKWARDATION(Fri)**. Kink moved 14dte/09-04 → 28dte/09-18. front_end_ratio@7 0.931→0.962 (rising, still <1.05, not panic). term-skew COMPLACENT both days.
- CONFLICT: sweep-tracker tags MSTR net **bearish** 3-of-5 — but contract-level detail is genuinely split (08-21 0DTE 100C aggressive buying at ask/bid 7.5 vs next-week 122C **selling/closing** at ask/bid 0.13, net_flow −12,987).
- dealer-positioning: **whipsaw disqualified** — 6 DEX sign changes in 14 sessions.
- Price: +28.17% on the week. iv-percentile PROVISIONAL (dates_used 92).

## SHORT-side candidates (ALL route to `watch_only`, never sized — 2026-08-01 P0 #1)

### IWM — 2 agents, aligned  [CLEARS CONFLUENCE]
- multileg-strategist: **the strongest structure of the week**. (a) persistent OTM put-buying program exp 2026-09-18, strikes walking DOWN 289→288→287→286→285→283 across **4 days** (08-18,19,20,21), each strike repeating on 2 consecutive days forming an overlapping chain; ~$128.2M. (b) debit put vertical exp 2026-09-11, sell 285P (bid, δ−0.169) / buy 295P (ask, δ−0.368), exact size match 55,273 both legs, $27.7M. Aggregate **$155.9M**.
- Side CONFIRMED via greek-screener: net ask-side (bought) on 283/285/286 on both 08-20 and 08-21, partially financed by bid-side (sold) 288 puts. OPENING, not a roll of the dying August contract.
- vol-surface-scout: `base_shape` CONTANGO(Mon) → FLAT(Fri); term-skew **TAIL_HEDGING both days, ratio RISING 1.333→1.380** = small-cap put-hedging demand building independently of the shape change.
- Term-structure anchor: clean monotonic CONTANGO (12.8%→18.6%→20.9%), no kink at JH (dte6) or PCE (dte7) ⇒ directional play, not an event-vol play.
- Sits below zero-gamma (299.43) in the OTM wing of a POSITIVE total-GEX regime — insurance-shaped, not amplification-shaped.
- Event exposure: both expiries span JH + PCE. Positioned FOR a hawkish-surprise selloff.
- Continuity: IWM/short was the daily call on BOTH 08-20 and 08-21 (LOW, watch_only) and W33's top watchlist name. It has now lost as a call twice while the structure kept building.

### INTC — sweep + advisory single-leg
- sweep-tracker: bearish 4-of-5, $675M, and the **only name in the sweep book with two independent legs agreeing** — INTC260828P00065000 shows ask-side put buying at a 165x ask/bid ratio.
- vol-surface: kink pinned at the 2026-08-28 tenor and STABLE all week (front ratio 1.016→1.004) = event-aligned, correctly priced.
- Price −12.13% on the week. LEAP 70C Dec-2028 OI build is **calls sold at the bid** (prev_bid 6,104 vs prev_ask 459) = covered-call writing, not conviction.

### Others (single-agent or advisory-only — fail the confluence gate)
SNDK (sweep bear 5/5, $2.45B, unconfirmed), SPCX (sweep bear 5/5, $1.30B, unconfirmed), AMD (sweep bear 5/5 unconfirmed + contrarian put-crowding building under bullish headline flow), MRNA (sector-rotation says Healthcare **bull leader** +$14.3M vs sweep-tracker **bear** 3/5 vs a clean opening Tier-1 **put** — genuinely conflicted, and +129% on the week), AVGO (dealer-positioning near-miss dex_flip_short, magnitude_ratio 0.93 vs 1.0 floor + contrarian call-crowded + earnings-scout BUY VOL with a CONTESTED earnings date).

## VOL / EARNINGS lane (earnings-scout is the only agent flagging these — single-signal)
Hard population result: **0 of 15 names register `TAIL_HEDGING` on back-month skew (`term-skew --dte-target 60`)**. 11 of 15 are COMPLACENT. ⇒ **no name qualifies for full-size SELL VOL anywhere in this book.** Tool-verified corroboration of the QQQ-negative-VRP premium-buying regime.
- **SNOW** (2026-09-02, 12d): clean KINKED at the earnings tenor, 23.0% prominence, 743 contracts. fer7 0.506. Back-skew +0.010 COMPLACENT. → SELL VOL, half.
- **DG** (2026-08-27, 6d): best front+back alignment in the book, back-skew **+0.0362 NORMAL (most stretched in sample)**, fer7 1.633. → SELL VOL, half. **Prints the same day Jackson Hole opens.**
- **INTU** (08-25, 4d) fer7 1.206, back +0.024 NORMAL → SELL VOL half. **CRM** (08-26) fer7 1.347 → SELL VOL half. **HPQ** (08-26) fer7 1.547, back +0.0235 NORMAL → SELL VOL half.
- **LULU** (09-03, 13d): clean kink at earnings, 14.1% prom. earnings-scout says BUY VOL (contested) but **fundamentals VETO'd it on 08-20** (Soros exit + AI-chief departure, both 08-14), vol-surface independently reads SELL VOL on the same object, and flow is one-sided bearish −$54.6M. Genuinely contested — do not size without re-confirmation.
- **AVGO**: earnings date **CONTESTED** — 09-02 (today's kink-tenor evidence, fer7 0.818 cheap) vs 08-26 (a report 2 days ago). Resolve before sizing.
- SKIP: CRWD, MRVL, DELL, PANW, MDB, OKTA, ADSK, **ULTA** (base-rate disqualifier: last 5 prints averaged ~11.9% move vs 2.86% implied).
- **4 of the 6 nearest-dated names (ULTA, MRVL, ADSK, DG) print 2026-08-27 — the day Jackson Hole opens.** CRWD/CRM/HPQ/OKTA print 08-26, one day before.

## Negative / caution flags to carry into Phase 2
- **AAPL — C28 distribution_flag, cross-validated 3 ways.** Wed clean-buy +$1.26B almost exactly unwound by Friday clean-sell; `institutional-accumulation` flipped NEUTRAL(1.36) → **DISTRIBUTION(0.49)**; non-0DTE 28-DTE call OI closed −3,275 contracts (~$4.97M). Counts AGAINST any AAPL long.
- **NEE** — three clean non-closing-cross sells on 08-20 ($190.6M + $186.8M + $30.8M) with zero offsetting buys.
- **NVDA** — net-sell isolated flow on 4 of 5 days (~−$131M on the week); institutional-accumulation degrading 1.18 → 0.86.
- **HOOD** — clearest crowding-penalty case in the book: call-crowded (pc z −1.437) + **+13.7% in one day** (week's #1 mover) + bullish net flow $36.1M + front_end_ratio@7 crossed into panic 1.026→1.129. A HOOD long sizes DOWN for crowding, not up.
- **QQQ short and GDX (either direction) are REFUTED/INCONCLUSIVE this week**, correcting the daily fleet's hypotheses. QQQ: P705 ask-side BOUGHT 08-19 vs P685+P660 both bid-side SOLD (exact size match 37,000) 08-20 — opposite aggressor signature 24h apart. GDX: a Nov-20 75P/85P tail-hedge vertical (08-19) and a near-ATM Aug-28 104C (08-21) are two separate books at different horizons.
- **CG** — collar (short 52.5C bid + long 40P ask, exact size match 100,000, exp 09-18). Protective hedge on an existing holder's position, NOT alpha.

## Regime / gate context for Phase 2
- Regime HELD TRANSITIONAL/UPTREND. Flow breadth improved 33.6%→39.2% bullish but stayed <50% all week.
- **Rubric is OUT-OF-REGIME** (fitted UPTREND, current TRANSITIONAL) ⇒ P0.6 guard caps every size at half.
- VRP: SPY +0.0016 FAIR (zero edge), QQQ −0.0307 NEGATIVE (premium-BUYING on the Nasdaq complex).
- Sector rotation regime call: **no_change, LOW confidence**. Only Healthcare survives netted→gross→ETF confirmation. The ETF layer OVERRULED Basic Materials (XLB −$4.89M, GDX −$26.4M) and Financial Services (XLF −$13.91M) despite both reading netted-IN. Technology's netted −$328.6M OUT is contradicted by its own same-day gross +$4,037.1M and by XLK +$7.41M BULLISH.
- Event risk inside every horizon: **Jackson Hole 08-27→08-29 (Kevin Warsh's FIRST as Fed Chair)** and **July core PCE 08-28** (running hot at 3.29% YoY).
- `dte-volume-share` crossed to RETAIL_DRIVEN at Friday's close (0DTE 45.9%) but institutional monthly+LEAP share held FLAT ~20-23% all week — the ramp is mechanical OPEX compression.
