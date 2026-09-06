# Weekly Market Intelligence — Week of 2026-07-13 (ISO 2026-W29)

## Executive Summary
- **Week regime + WoW Δ:** TRANSITIONAL/CHOPPY, **held** Mon→Fri — no regime flip. SPY closed 743.29, below both the 20-SMA (745.02) and 50-SMA (744.38), −0.94% on 30 days and −2.25% off the 90-day high. Options-flow breadth stayed bearish-skewed (bullish tickers 33.8%→38.4%). VIX ran up to 18.77 (HIGH tercile). VRP is FAIR/neutral (SPY −0.003, QQQ −0.042) — no vol-selling edge. This was a **short-gamma, elevated-vol, distribution tape**, not a dip to buy.
- **Rubric regime status:** OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL/CHOPPY) — sizing capped at half. Moot this week: the board is empty.
- **Signal performance:** 0 of 0 resolved (hit rate n/a); 0 INCONCLUSIVE; **0 non-DROP calls in the universe** — all five daily boards this week were all-DROP (E: envelopes exist for all 5 covered days but committed zero actionable calls; R: 0 reconstructed). The desk made no live calls to grade — and that was the correct outcome (see §0).
- **Top swing build for next week:** **None.** Zero names cleared even LOW tier — the 13th consecutive empty conviction board. §3 is empty by design, not omission.
- **Top LEAP build:** **None.** Zero of eight DTE>180 screen names cleared the 6-of-9 gate.
- **Biggest emerging risk:** A single **semis-complex correlation cluster** (INTC/AMD/MU/SMH/SNDK/NVDA, pairwise corr to 0.94) that just fell 8–29% in a week — any semi exposure is one bet, and the coming fortnight stacks FOMC (07-29), Q2 GDP and Core PCE (both 07-30) onto a short-gamma tape.

---

## 0. Week in Review — Intra-Week Signal Performance

The scorecard universe is the union of non-DROP `calls[]` across this week's five daily `decision.json` envelopes. **That universe is empty: every call on all five days was DROP.** There is nothing to grade — the hit rate is undefined because the desk committed zero live positions.

That is the headline, not a footnote. **The empty-board discipline paid off enormously this week.** The recurring names the flow tape kept surfacing — and which a less disciplined book would have been tempted to buy on their *bullish* net-premium — were precisely the names that collapsed:

| Ticker | Net-premium tape this week | Week move (base 07-10 → 07-17) | Move in ATR(14) |
|---|---|---|---|
| SNDK | bullish (8/10 bull days, +$509M 30d) | **−29.3%** | −4.0 |
| NBIS | bullish (8/10 bull days, +$144M 30d) | **−19.1%** | −2.9 |
| MU | mixed | −13.2% | −3.3 |
| INTC | mixed/bullish snaps | −13.5% | −2.8 |
| AMD | mixed | −11.2% | −2.7 |
| SMH | bearish ETF tape | −9.0% | −3.0 |
| TSM | mixed | −8.3% | −3.0 |
| QQQ | bearish (8/10 bear days) | −4.1% | −3.0 |
| NVDA | net +$82M bullish | −3.8% | −2.0 |
| SPY | bearish | −1.5% | −2.5 |

The lesson is the one the desk has now logged repeatedly: **in this regime, "bullish" net-premium on a mega-cap semi is hedging/distribution, not conviction.** Any long the flow tempted would have been a −2 to −4 ATR drawdown. The short-leaning DROP calls (INTC/MU/TSM/SMH/NBIS) would have won — but short alpha-sizing carries no validated edge in this book (2026-06-27 audit), so staying flat was the right call on both sides.

---

## 1. Regime & WoW Delta

The regime label was identical at both ends of the week — TRANSITIONAL, trend CHOPPY, "reduce position size, favor defined-risk." SPY sat below its 20- and 50-day averages all week and never reclaimed them. Options-flow breadth improved marginally (bullish-flow tickers 33.8%→38.4%) but stayed decisively bearish-skewed, and the independent Finviz cash-tape breadth was outright red: **147 advancers vs 356 decliners, pct_green 29.2%** — a distribution divergence against the neutral "transitional" label (worst mover ISRG −14.2%; top mover TRV +9.2% on an insurance-earnings beat). VIX pushing to 18.77 (HIGH tercile) with VRP FAIR means volatility is fairly priced, not cheap — there is no premium-selling edge to harvest and no dislocation to fade.

The market-wide DTE-volume mix read BALANCED (weeklies 20.5%, monthlies 17.3%, LEAPs 4.1%); the `share_0dte=0` print is an OPEX-Friday parquet artifact, not a real read, and cannot be used as a retail/institutional discriminator this week.

**Macro backdrop.** Sticky core inflation (core CPI 2.81% YoY, core PCE 3.41%), a normal but modestly re-steepening curve (10Y−2Y +0.37), the 10Y **rising** to 4.57%, a **strengthening** USD, and a soft payroll print (+57k). June CPI landed mid-week (07-14) and was part of the chop. The mix is a mild headwind: no disinflation gift, real rates drifting up, dollar firm. **Forward event risk (next two weeks):** initial jobless claims 07-23 (Tier-2); **FOMC 07-29** (no SEP, Tier-1); **Q2 GDP advance + Core PCE both 07-30** (Tier-1). Both Tier-1 macro events land in the *second* week of the horizon, so next week (W30) is macro-light but earnings-heavy — the Q2 mega-cap season begins.

**Implication for next week's bias:** defensive. Short-gamma dealer books (§9) plus an event-heavy fortnight plus fair-priced vol argue for defined-risk, low-gross posture and against both premium-selling and dip-buying until the regime resolves.

---

## 2. Sector Rotation

**Rotation regime call: `no_change` (low confidence).** No cross-sector inflow/outflow split matches a canonical macro rotation — every clean pattern fails a leg (defensive→cyclical fails because Healthcare is a top-5 inflow and Industrials the worst outflow; growth→value fails because Tech/Comm lead inflows; value→growth fails because Financials are the 4th-strongest inflow). What the tape actually shows is **mega-cap-growth / AI-infrastructure concentration, not rotation**: Technology + Communication Services together drew ~$7.26B of 5-day net-call premium, outweighing the other nine sectors combined (~$3.9B).

The critical caveat: this is **net-call premium (a skew/level metric), and its named "leaders" — NVDA, CDNS, SNDK, NBIS, META — are exactly the names that got crushed this week.** Net-call premium is not directional conviction. The concentrated, institutional-size dollar bets ran the other way (put-heavy in the mega-caps; BRK.B/AXP puts under a net-call-positive Financial Services; near-parity TSLA under a net-call-positive Consumer Cyclical). Treat Financial Services and Consumer Cyclical "inflows" as broad small-ticket skew, not conviction — watch-only.

**ETF flow tape (advisory).** The instrument layer sharpens the picture — and it is defensive/hedging where it is clean:

| ETF | Net premium dir (5d) | GICS map | GICS agreement | Read |
|---|---|---|---|---|
| SMH | **−$159.6M BEARISH** | Technology | **disagree** | $130M of 7/31 put-buying — semis-specific hedging *inside* the "bullish" Tech sector; do not lump SMH into a Tech rotation |
| KRE | −$10.1M BEARISH | Financial Services | disagree | Regional-bank weakness under a net-call-positive Financials — explains the AXP/BRK.B bearish dispersion |
| GDX | −$24.6M BEARISH | Materials | disagree (weak) | Long-dated put buying on gold miners |
| EWY / EWT | +$32M / +$1.5M BULLISH | Korea / Taiwan | n/a | Bullish aggregate but hedge-heavy (EWY's top sweep is a $10M put); Taiwan (TSM-heavy) firm vs US-semis hedged |
| XLI | +$4.3M BULLISH | Industrials | **disagree** | One $165M DP buy block, but GICS Industrials is the worst outflow sector — watch-only |

Note that **XLK itself reads MIXED** at the ETF level despite Technology being the #1 GICS inflow sector — an internal caution flag on the whole "AI-infra long" thread. Industrials is genuinely bifurcated (BE/FIX/RKLB bullish vs SPCX/VRT/CAT bearish) — not a clean short book.

**Swing-book implication:** there is no durable rotation to trade. The one coherent cross-sector correlation is a *theme* (AI-infra) that spent the week de-rating, and the cleanest ETF signals are hedges (SMH/KRE/GDX puts). No sector-leader +1 was awarded to any name (0-for-4 on the conditional gate).

---

## 3. Swing Book (1–6 weeks)

**Empty.** Zero names cleared the confluence gate into a scored LONG, and zero cleared even LOW tier after scoring. No swing long (§3a) and no swing short (§3b) is carried.

The near-misses and why they died:
- **NBIS** — sweep-tracker's only first-class bearish name (5/5 sessions, $779M, aggressive 07/24 210P buying), and it fell −19%. But the persistence line was removed from the rubric (2026-05-23 P0.3), the opposing bullish net-premium (+$144M) is below the deduction magnitude bar, and short selection-alpha has no validated sizing edge. Scored −1, DROP.
- **NVDA** — the week's only repeat multileg structure (Sep 210P/170P put vertical, 2 days), but hedge-ambiguous on flat 30d flow (+$51M) and **VETO'd by fundamentals** (elite growth/margins fight the short; the Sep vertical unexpectedly spans the 08-25 earnings). Watch-only.
- **SMH** — the cleanest 3-agent bearish confluence of the week (fresh opening 522.5P/517.5P $131M + −$160M ETF tape + tail-hedging skew), and right (−9%) — but the rubric structurally cannot score a hedging-basket short, and it netted a lite deduction on flat aggregate flow. Scored −1, DROP.

Dealer-positioning found **no mechanized DEX flip and no vanna squeeze** anywhere (VIX fell 07-13→07-15, briefly arming a put-heavy squeeze, then reversed into OPEX and invalidated it). The one item to carry: QQQ's DEX and total-GEX deteriorated monotonically over the last three sessions — a lean-short watch pending post-OPEX confirmation, not a scored setup.

---

## 4. LEAP Book (6–24 months)

**Empty.** The DTE>180 OI-growth screen surfaced eight single names (AAPL, FHN, RKT, DRAM, CMCSA, NOK, IREN, BE); **none cleared the 6-of-9 gate.** AAPL had the cleanest ask-side build (Sep-2027 $400C) but fails the required cumulative-premium-flow accretion gate (30d −$62M / MIXED, 90d flat) — a single fresh position, not slow accretion. FHN is a single-day, bid-filled covered-call write with mixed institutional-accumulation across the week. The other six show net premium flow running *opposite* their fresh OI build — a direct disqualifier. Nothing should be carried forward as a "building" thesis.

---

## 5. Volatility Surface — WoW Term Structure & Skew Evolution

**Substrate hygiene first:** on OPEX Friday, the expired 0DTE bucket (avg IV 90–430%) swamps the front leg and forces a mechanical `BACKWARDATION/null` label on *every* name. After dropping the expired bucket and applying a 15-contract floor, the real surface is far more differentiated. (PLTR is the clean proof: the raw classifier correctly caught `KINKED @2026-08-07` on 07-13, then flipped to a contaminated `BACKWARDATION/null` on 07-17 even though the underlying kink never moved.)

The real shapes are **earnings kinks, not surface dislocations:**
- **INTC** — sharp earnings kink at 07-24 (137.3% vs ~92%/119% flanks), growing WoW. Event-driven → §6.
- **AMD** — mirror of INTC, kink at 07-24 growing WoW. **But see §6/§7: the 07-24 date is AMD's AI Day, not its earnings print (08-04)** — the kink is a product-event, not an earnings-vol setup.
- **PLTR** — the highest-confidence, WoW-persistent kink in the set (08-07, clears the contract floor both dates). Flagship earnings hand-off.
- **SNDK / AVGO / MU** — plausible but unconfirmed forward kinks (Aug 7 / Sept 18 / multi-peak); need an earnings-date match before trading.

**No calendar-spread candidate this week.** Every backwardation-flagged name either has a live catalyst, has a front-end ratio that is *rising* (TSM 1.245, DRAM 1.073 — both explicitly disqualified as panic-still-building), or has a ratio that materially understates the real belly/back kink (the tool is endpoint-only). SMH carries persistent tail-hedging skew; NVDA is the quiet control (no dislocation). Note: `iv-percentile-zscore` returned only 56–67 usable days (below the 120-day floor) — every IV-percentile read this week is provisional.

---

## 6. Earnings — Recap & 2-Week Lookahead

**(a) Recap — this week's bank/tech prints.** The vol-sale book worked on the clean prints and half-sizing saved the whipsaws:

| Ticker | Pre-event thesis | Grade | Note |
|---|---|---|---|
| JPM | SELL VOL half | **CONFIRMING** | Cleanest print — orderly +2.5% gap, gradual IV bleed |
| BAC | SELL VOL full | **CONFIRMING** | Textbook crush (IV30d 25%→21%) |
| WFC | SELL VOL full | **CONFIRMING** | −2.7% gap fully round-tripped by 07-15 |
| JNJ | CALENDAR (from W28) | **CONFIRMING** | Front-end panic persisted past the print — calendar signature |
| MS | SELL VOL half | CONFIRMING (whipsaw) | +3.4%→−6.3%; half-size discipline warranted |
| C | SELL VOL moderate | **DISCONFIRMING** | −8.1% directional trend ran over the sold vol |
| GS | SELL VOL half | **DISCONFIRMING** | +9% pop then −7.4%; IV never cleanly crushed — half-size prevented a full loss |
| NFLX | conflicting (SELL vs BUY vol across reports) | MIXED | Realized ~6% ≈ implied; the thesis conflict is itself the finding |
| ASML | SELL VOL half | INCONCLUSIVE | IV round-tripped rather than staying crushed |
| TSM | SELL VOL half | UNGRADABLE | Finnhub surprise is a TWD/USD unit artifact — do not carry forward |
| GE, BLK | SKIP | **SKIP validated** | Both had single-day moves (−4.1%, +6.6%) that would have run over a sold-vol position |

Net: ~5 confirming / 2 disconfirming, and the half-size discipline on GS/MS was directly validated.

**(b) Lookahead — next 2 weeks (all SELL VOL half at most — no back-month reached TAIL_HEDGING, so nothing clears full size):**

| Rank | Ticker | Earnings | DTE | Term structure | Fundamentals verdict | Read |
|---|---|---|---|---|---|---|
| 1 | INTC | 07-23 PM | 6 | KINKED @07-24 | **CONFIRM** | Genuine kink, huge liquidity; 4/4 beat streak; event already priced. Sell-vol-half framing, but SOX bear-market correlation is the tail risk |
| 2 | FTNT | 07-29 PM | 12 | KINKED @07-31 | not run | Repeat of last cycle's flagged vol edge; re-check for a directional whale before sizing |
| 3 | CDNS | 07-27 PM | 10 | KINKED @07-31 | **CAUTION** | **"Kimi K3 designs a chip in 48h with no proprietary EDA" is a real moat-disruption catalyst into the print** — raises realized-move odds against short vega |
| 4 | GOOGL | 07-22 PM | 5 | KINKED @07-24 | not run | Front-ratio 1.586 is the most extreme of the cohort (past the "wait for unwind" threshold); no confirming flow |
| 5 | TSLA | 07-22 PM | 5 | KINKED @07-24 | **CONFIRM** (short) | Complacent skew + neutral flow argue against short-vol; but fundamentals (EPS −39%, 3.95% margin, PE 370x) support a directional short into the print |
| — | AMD | **08-04** (not 07-24) | 18 | kink is AI Day 07-24 | **CAUTION** | Date mismatch: the 07-24 kink is the Advancing-AI event, not earnings — a vol trade calibrated to the wrong date |
| — | LRCX / DPZ / VC | 07-29 / 07-20 / 07-23 | — | not-kinked / substrate gap | — | SKIP — no isolatable earnings tenor or no name-specific richness |

Caveat: `analyst-vs-flow` remains unwired (no analyst-recommendation field returned on any name), so no disagreement metric could be computed. The screener's `implied_move` field is broken again this cycle and was not used.

---

## 7. Risk & Correlation (week-candidate universe)

**Correlation — one semis bet, not six names.** `uw risk portfolio-correlation` on the union returns a single dominant cluster:

> **`semis_complex_cluster`** = {INTC, AMD, MU, SMH, SNDK, NVDA} — AMD/SMH 0.941, INTC/SMH 0.914, MU/SMH 0.894, INTC/AMD 0.892, MU/SNDK 0.874, SMH/SNDK 0.855, AMD/MU 0.814, INTC/MU 0.804, NVDA/SMH 0.779. The tool's own warning: "pairs move nearly in lockstep — not truly diversified." Kept member for any hypothetical sizing: INTC (highest raw). (Sector metadata came back 100% "Unknown" this run — logged for the audit.)

**Macro & event risk:** sticky core inflation, 10Y rising to 4.57%, USD firm. From Friday's close: jobless claims 07-23 (T+4, Tier-2, no fire), **FOMC 07-29 (T+8)**, **Q2 GDP + Core PCE 07-30 (T+9)** — both Tier-1, outside any 1-week structure's firing band but inside any 2–4 week swing horizon. Name-level: TSLA earnings 07-22 (T+3) fires the event-risk gate.

**Fundamentals verdicts (top-5):** INTC CONFIRM · AMD CAUTION (07-24 = AI Day not earnings; insider MSPR −84.7) · CDNS CAUTION (Kimi K3 disruption catalyst; insider −68.8) · **NVDA VETO** (elite fundamentals fight the short; Sep vertical spans 08-25 earnings; insider −98.6 is routine at NVDA's scale) · TSLA CONFIRM (short-supportive: EPS −39%, PE 370x). None change sizing — the board is empty — but the NVDA VETO and the AMD date-mismatch are the two items worth flagging.

**Debate-disconfirmation cuts:** the bull/bear debate (2c) was **skipped** — zero names reached LOW tier, so there was no conviction call to stress-test (consistent with the 07-13 all-DROP precedent). No residuals to report.

**Breadth cross-check:** advancers 147 / decliners 356, pct_green 29.2% — **divergence flagged** (red cash tape vs the neutral "transitional" label = distribution tell). Advisory, no size impact.

**Adverse-flow scan — prior-week group `conviction_week_2026-W28` = [SNDK, NVDA, JPM, SOFI, META]:**
- **SNDK — hard EXIT.** −29% on the week, IV rank 100 (vol blown out), OI +42.5k into the collapse. Any carried thesis is broken; the "bullish" flow tag at these levels is knife-catching/covering.
- **META — soft exit / monitor.** This week's fleet reads it net-bearish (flow_conflict); divergence from a carried long = off-thesis decay.
- **NVDA — monitor** (hedge-ambiguous/flat this week). **JPM, SOFI — no adverse alerts.**

**Watchlist write-back: EMPTY** — zero conviction-tier names, so no `conviction_week_2026-W29` group was created and no DROP names were written. 13th consecutive empty write-back — and the discipline was directly validated (the bullish-net-premium semis it refused all fell 11–29%).

**Hedge sleeve.** No book hedge is required (empty conviction book, net delta zero). For *standing* portfolio exposure into the event-heavy fortnight on a short-gamma, VIX-18.77 tape: prefer a **defined-risk SPY put debit vertical spanning both prints** (~740/710, Aug expiry) over VIX calls — VIX is already HIGH-tercile and VRP is FAIR, so convexity is fairly priced, not cheap, and a vertical caps the vol bill. Size at half-tier max. Do **not** sell wings or premium through FOMC in this gamma regime, and avoid SMH puts (semi IV is already stressed post the −29% SNDK week — you'd be buying the top of the vol move).

---

## 8. High-Conviction Cross-Ref (HIGH and MEDIUM tier)

**Empty — no HIGH or MEDIUM tier names.** All ten union candidates scored DROP (top raw_score +1).

**Expectancy lens (advisory, C31):** not computable — zero closed conviction calls this week and an empty book, so there is no per-tier expectancy or payoff ratio to display. The Kelly/expectancy sizer remains advisory regardless (Step 5 uses the win-rate ladder).

The single most important quantitative note for the desk: the only real win-rate in the entire book — **`bearish_flow`, clean-protocol WR 0.553 on n=132, +15.2pp over same-window SPY-short (the 3rd straight positive read)** — attaches to SMH/NBIS/SNDK, names the rubric scored at or below −1. The rubric structurally cannot score a bearish/hedging flow even when it is right (SMH −9%, NBIS −19%, SNDK −29%). This is the standing **C19 / bearish_flow accrual gap**, logged again for `/calibration-audit`.

Embedded rubric (for audit): the frozen weekly conviction rubric, version `2026-06-12`, is embedded verbatim in the skill definition and stamped on the envelope (`rubric_version: "2026-06-12"`). No line was re-weighted this run; the freeze holds.

---

## 9. Setups for Next Week

- **Next-session GEX advisory (SPY/QQQ only — advisory, 0 rubric points, backtest `NO_GO_NO_EDGE`).** The Step-0 backtest is explicit: GEX walls are **not** magnets (next close closer-to-nearest-wall 22%, p=1.0) — this is dealer context, never a predictive claim.
  - **SPY** (spot 742.95): **FULLY_NEGATIVE**, total GEX −$2.27B, ZGL unreliable. The largest negative-gamma mass (−$498.7M) sits at **742 — essentially on Friday's close**; the only +GEX pocket is a thin, isolated 760. Dealers are maximally short gamma at spot into the open, so a directional push either way is amplified. Regime is *unstable* (flip-flops almost daily). **Bias:** short-gamma playbook — long premium / debit verticals, avoid iron flies pinned at 742–743; a break of the 740/745 shelf accelerates.
  - **QQQ** (spot 695.66): **FULLY_NEGATIVE**, total GEX −$1.96B, **no credible call wall**. −$977M of negative gamma concentrated at 695 (at spot). Held FULLY_NEGATIVE two straight sessions while spot fell 719→695 and GEX worsened −1.15B→−1.96B — a *trending* short-gamma regime, the more dangerous of the two books. **Bias:** trend/breakout — long straddle or directional debit verticals with the trend; explicitly avoid range-bound premium-selling.
- **Next-session 0DTE premium-selling setup (validated stack — advisory, 0 rubric points):** rolling backtest verdict `GO_PREMIUM_SELL_INTRADAY` (SPY n=60 mean +0.279% gross / **+0.179% net**; QQQ +0.389% gross / **+0.289% net**; % of underlying-spot notional). **But the current setup says STAND ASIDE for both** — VIX spiking +2.0 into 18.77 (HIGH tercile), `sell_premium: false`, size scalar 0. Delta-neutral only, never carry overnight; the short-vol left tail is unsampled (no vol shock in the window), so the gross win-rate overstates a negatively-skewed edge. Permanent advisory / 0 rubric points.
- **Swing dealer setups (dealer-positioning):** none scored — no mechanized DEX flip, no vanna squeeze. Carry QQQ's monotonically deteriorating DEX/GEX as a lean-short watch, pending post-OPEX confirmation.
- **Pin vs trend:** trend, not pin — both index books are short-gamma with no functioning magnet.
- **OPEX book:** N/A. The monthly OPEX resolved on 07-17; next week (W30) is post-OPEX (next monthly is 08-21, 34 days out), so `opex-pin-strategist` was not spawned and there is no next-week pin book.
- **Highest-conviction actionable setups for the coming week:** **none** — this is a no-edge week. The only forward-looking, defensible expressions are (a) the standing defined-risk SPY put-vertical hedge into FOMC/PCE/GDP (§7) and (b) the earnings-vol watch names (INTC 07-23, CDNS 07-27 — both half-size at most, both carrying caution), which are §6 event plays, not conviction swings.
- **LOW-tier names to track for daily confirmation:** none reached LOW.
- **Deep-dive hand-off:** skipped — no HIGH-tier names on a no-edge week.

---

## 10. Watch-only — single signal, no confluence

Listed for journaling, **not** for trade entry:
- **MU** — single-agent flag only (vol-surface's messy multi-peak surface); failed the ≥2-agent confluence gate. Fell −13.2% on dead-flat net premium — the tape repriced without a scored signal.
- **PLTR** — vol-surface's highest-confidence earnings kink (08-07), but a single-lane read; carry to the earnings lookahead, not the trade book.
- **TRV** — Finviz RS new-high (+9.2%) on an insurance-earnings beat; orthogonal to the flow engine, advisory only.
- Index/hedge context (not names): SPXW/SPY/QQQ bearish sweep tape (market hedge), the single-leg repeat-put cluster MSFT/ORCL/IBM/MSTR (bearish protection into the 07-17 expiry, now expired), and the SMH/KRE/GDX ETF put hedging from §2.
