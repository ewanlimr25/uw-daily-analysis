# Weekly Market Intelligence — Week of 2026-08-03 (ISO 2026-W32)

## Executive Summary

- **Week regime + WoW Δ:** TRANSITIONAL **held** at both ends with `trend` UPTREND throughout, and this time the price tape was genuinely strong — SPY **+3.51%** (747.03 → 773.26), QQQ **+5.09%**, IWM +3.56%, SMH **+7.80%**, XLK +7.20%, VIX **−6.82% to 14.90**. But the internals did not follow: `uw` options-flow breadth **deteriorated 40.0% → 37.7% bullish** (2,368 bullish vs 3,913 bearish tickers), and SPY (+3.51%) beat equal-weight RSP (+2.36%) by **1.15pp** — mega-cap carried the index. VRP is **NEGATIVE on both indices** (SPY −0.0073 FAIR, QQQ **−0.0536 PREMIUM_BUYING**), so this is a premium-**buying** week: contrarian-scanner aborted its entire fade book for the third consecutive week, and every `vol_short` proposal contradicts the vol regime.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`.
- **Signal performance:** **3 of 5 resolved (hit rate 3/5 = 60%); 1 INCONCLUSIVE excluded; 6 total non-DROP calls in universe (6 envelope-anchored, 0 reconstructed)** — out of **39 total calls** across the week's five daily envelopes, of which 33 were DROP. Unusually, the non-DROP book **beat** the DROP pile this week (60% vs 44.4%), reversing the recent pattern. See §0.
- **Top swing build for next week:** **None.** The post-gate book is **empty**. The only scored name — NVDA, raw 3, LOW — gated `starter → skip` on three independent axes.
- **Top LEAP build:** **None.** Zero of the floored funnel cleared 6-of-9 gates. The near-miss (BULL) failed on zero roll evidence across all five sessions, conviction-matrix 51.9 vs a >70 bar, and a "long-dated" OI build that is actually short-dated churn.
- **Biggest emerging risk:** **Systematic institutional de-risking that the price tape completely conceals.** Three mega-caps (MSFT, GOOGL, and probably PLTR) rolled calls **up and out for net credits** — taking ~$85M off the table, not adding risk — while SPY crash-flies, an IWM put ladder, HYG credit puts and a $20M GDX put build all opened **ask-side**. Long-dated ETF positioning ran **23 put rows ($119.5M) vs 10 call rows ($33.4M)**, with QQQ 600P/750P **bought at the ask** and QQQ 1100C/900C **sold at the bid** — an index-level collar. Runner-up: **the dark-pool accumulation signal is structurally contaminated this week** (below).

> **The 21st consecutive effectively-empty conviction board, and this one was gate-earned rather than gate-shy.** NVDA lost on insiders selling into it (MSPR −98.61, near −100 in 14 of 17 months), CPI at T+3 with its own print at T+13, and a debate its bull lost 0.35 to 0.65. The week's only *full-size* proposal — HD SELL VOL — is a short-vol structure in a premium-buying week on a name with a 3-of-4 earnings **miss** streak. Sized exposure: **zero**.

---

## 0. Week in Review — Intra-Week Signal Performance

**Universe:** the union of `calls[]` across this week's five daily `decision.json` envelopes — the only hindsight-free record of what was actually committed. **All five envelopes exist, so nothing was reconstructed.** **39 total calls; 6 non-DROP.** Resolution runs from each call's own envelope date forward to 2026-08-07, graded on the C20 path-aware **0.5 × ATR(14)** threshold measured as-of the call date.

### Primary scorecard — non-DROP calls

| Ticker | Direction | Source | Move vs ATR | Flow/OI | Grade | Note |
|---|---|---|---|---|---|---|
| SNDK | long | envelope 08-03 | close **−0.39×ATR**; MFE **+0.82×ATR** on 08-04 | cum-flow +$1.25B but only **2.34% of gross**, MIXED | **WIN** (path-aware) | Reached +0.5×ATR favourable on the very next session *before* any adverse 0.5×ATR excursion. Then earnings (08-05 PM) gapped it −13% on 08-06. The pre-earnings positioning thesis was right for two sessions; the binary went the other way. **Sized `skip` precisely because of the 13.88% implied move** — the gate was vindicated. |
| AVGO | long | envelope 08-04 | **+0.55×ATR** (+2.30%) | — | **WIN** | The cleanest win: MAE only −0.42×ATR, never seriously offside. Sized `watch_only`. |
| ZTS | vol_short | envelope 08-05 | realised round-trip well inside the 10.56% implied | iv30d **−52.2%** on the print — the largest crush of the week | **WIN** | Vol thesis correct: move contained, crush realised. Risk-monitor killed it anyway on non-vol grounds (broken beat streak, debate) — the right call for the right reasons, and it cost nothing. |
| LRCX | long | envelope 08-04 | close −0.25×ATR; **MAE −0.96×ATR** on 08-06 | — | **LOSS** | Breached 0.5×ATR against on 08-06; MFE never exceeded +0.24×ATR. |
| NBIS | long | envelope 08-04 | **−1.40×ATR** (−16.73%) | flow turned bearish, −$15.1M | **LOSS** | The week's worst miss. MAE −1.67×ATR, MFE +0.08×ATR — offside essentially from entry. |
| CRWV | vol_long | envelope 08-06 | +0.68×ATR after 1 session | — | INCONCLUSIVE | **Catalyst outside the window** — the thesis is the 2026-08-11 earnings print, which has not occurred. Not a dumping ground: the reason is verifiable and dated. |

**Headline: 3 of 5 resolved (hit rate 3/5 = 60%); 1 INCONCLUSIVE excluded; 6 total non-DROP in universe (6 envelope-anchored, 0 reconstructed); 39 total calls, 33 DROP.** A denominator of five carries little information — but **every one of these was `skip` or `watch_only`, so realised book P&L is exactly zero.**

### Supplementary — DROP-pile discipline check (n=17 directional DROP calls, 9 resolved)

Not part of the formal scorecard; grades what the desk *declined* to trade.

| Metric | Result |
|---|---|
| DROP hit rate | **4W / 5L = 44.4%** |
| Non-DROP hit rate | **3W / 2L = 60.0%** |

**This reverses the recent pattern.** In the 07-18 and 07-31 audits the DROP pile outperformed the traded book, which was the empirical backbone of empty-board discipline. This week the calls that survived to non-DROP status did better than the ones killed. One week at n=5 vs n=9 proves nothing either way, but it is worth recording, because three consecutive audits have leaned on the opposite result. Worst DROP misses: GDX short **−2.04×ATR** (shorting a +21.3% week), GOOGL long −1.68×ATR, SMH short −1.39×ATR.

---

## 1. Regime & WoW Delta

The regime label held TRANSITIONAL Monday to Friday with `trend` UPTREND at both ends, and unlike recent weeks the price action genuinely earned it: SPY closed at 773.26, above both its 20SMA (750.17) and 50SMA (747.19) and only −0.46% from its 90-day high, having gained 3.51% on the week. QQQ added 5.09%, semis (SMH +7.80%) led, and VIX fell 6.82% to **14.90** — the low tercile of its own 60-day distribution.

The internals tell a different story. `uw` options-flow breadth **deteriorated from 40.0% to 37.7% bullish** across the week, meaning that of 6,281 optionable names, 3,913 carried net-bearish flow while the index made highs. SPY's 3.51% beat equal-weight RSP's 2.36% by 1.15pp, so the advance was cap-weighted rather than broad.

> **A methodological warning that affects any WoW price read:** the `spy` sub-block of `uw risk market-regime` returned **byte-identical values** for `--date 2026-08-03` and `--date 2026-08-07` (current 773.26, change_30d 2.87%, sma_20 750.17, sma_50 747.19). It is a **live snapshot, not date-pinned**. Every price delta in this note comes from the raw Yahoo chart API via `scripts/market_data.py`, never from that block.

**VRP** — SPY vrp −0.0073 (iv30d 12.72% vs realised 13.45%) = FAIR; QQQ vrp **−0.0536** (iv30d 20.44% vs realised 25.79%) = **PREMIUM_BUYING**. Both negative. Note the tension worth flagging: index IV is *cheap* against realised, yet VIX sits in its low tercile — and QQQ realised 25.8% against SPY's 13.5% is a very wide dispersion gap. Vol-surface-scout found the same tilt pervasive at the single-name level: **11 of 18 measurable names are PREMIUM_BUYING against only 3 PREMIUM_SELLING.**

**DTE share** — the tape got structurally shorter-dated all week: 0DTE share **15.5% → 17.3% → 17.6% → 26.4% → 46.4%**, with Friday flipping to `RETAIL_DRIVEN`. Monthlies fell 22.7% → 20.9% and LEAPs 3.6% → 3.0%. Friday is a weekly-expiry day so part of that spike is mechanics, but **Thursday's 26.4% is genuinely elevated** against the 15–18% Monday–Wednesday baseline. Consequence applied fleet-wide: rotation conviction downgraded uniformly, and week-end-only directional prints discounted.

**Macro backdrop** (`scripts/fred_macro.py`) — a **stagflationary tilt**. Core PCE **3.29% YoY** sits above core CPI (2.81%) and well above target; payrolls went **negative (−23k MoM)** with unemployment 4.1%; the 10Y rose to **4.69%** (+14bp/30d) while the USD **weakened** — an unusual pairing that points to term-premium/fiscal pressure rather than growth. Fed funds at 3.63% against core PCE 3.29% leaves almost no real-rate buffer. Negative payrolls with sticky core PCE is the worst cell for long-duration risk.

**Forward event risk (next two weeks):** **CPI (July) 2026-08-12 — HIGH**, T+3 trading days and inside every swing horizon in this book. PPI 08-13, jobless claims 08-13 and 08-20, retail sales 08-14, **monthly OPEX 08-21**. No FOMC inside two weeks.

**Implication for next week:** the index is making highs on narrowing participation with cheap-vs-realised index vol and a CPI print three sessions away. That combination argues for owning convexity rather than selling it — which is precisely what the institutional tape did (§2, §9).

---

## 2. Sector Rotation

**Rotation regime call: `no_change`, confidence LOW.** No canonical pattern forms. The inflow leg simultaneously contains growth (Technology), cyclical (Industrials) and defensive (Consumer Defensive), which is not one of the four canonical rotations, and **all three netted-outflow sectors fail the C55 gross-vs-netted agreement test**, so there is no confirmed outflow leg to pair against anything.

**Direction is read exclusively off the netted `uw risk market-regime.sector_rotation` (C55).** This week produced an unusually clean demonstration of why:

| Sector | Netted (C55, authoritative) | Gross turnover | Verdict |
|---|---|---|---|
| Technology | **+$110.4M** (in) | +$5.350B | agree — but **halved WoW** from +$217.4M |
| Industrials | **+$79.5M** (in) | +$447.5M | agree — new this week, single netted reading |
| Consumer Defensive | **+$8.6M** (in) | +$43.2M | agrees on GICS, but **XLP options flow disagrees** (−$8.05M outflow) |
| Consumer Cyclical | **−$30.8M** (out) | +$677.9M | **DISAGREE → watch_only** |
| Communication Services | **−$18.9M** (out) | +$590.5M | **DISAGREE → watch_only** |
| Healthcare | **−$7.5M** (out) | +$194.7M | **DISAGREE → watch_only** (found this run, not pre-flagged) |

**Two degenerate-substrate findings that materially weaken this section:**

1. `uw options-flow sector-flow-persistence --days 5` returned **all 11 sectors as `trend: INFLOW` with `persistence_score: 1.0`**. Every sector inflowing at once is arithmetically impossible for netted flow — it is the gross-turnover artifact, and an identical score across all 11 means **zero cross-sectional discrimination**. The conditional sector-leader +1 requires `persistence_score ≥ 0.6`; every sector nominally clears that on a degenerate all-equal reading, so **the gate is uninformative and was awarded on the flow leg alone**.
2. Netted-vs-gross **disagree in sign on three sectors**, not the two flagged in preflight.

**WoW netted shift:** Communication Services flipped +$138.0M → −$18.9M; Consumer Cyclical flipped +$76.9M → −$30.8M; Technology stayed in but halved; Consumer Defensive flipped −$4.1M → **+$8.6M** (a defensive bid appearing); Industrials new at +$79.5M; Healthcare's outflow shrank.

**Single-name leaders (C12-floored universe only).** Only **NVDA, BULL and MRVL** clear the full conditional bar (sign-aligned 30d flow, ≥$50M, floored-funnel member). **SNDK was excluded** — its net is 1.4% of gross (MIXED), the known put-sale-netting artifact. **WOLF and TSM fail on sign conflict** (30d flow opposes the daily print). **SPCX fails**: it single-handedly *is* the Industrials story (+$93.5M daily net, 96× the next name) yet its own 30d trend is net bearish −$20.2M — a one-day idiosyncratic catalyst, not durable accumulation. **No Industrials name earns the +1.** Consumer Defensive has **zero** floored-funnel names, so its inflow is unactionable regardless.

### ETF flow tape (advisory — 0 rubric points)

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| **SMH** | inflow +$22.35M | MIXED | 20:00Z closing-cross-style $33.3M print then near-mid buys — mixed | **LEAP-dated bullish tilt**: 2027-06 750/700 call sweeps ($16.2M + $7.1M) vs LEAP puts ($8.6M + $6.4M) | agree (Technology) | NVDA, MRVL |
| **XLI** | inflow +$17.24M | **BULLISH** | clean $14.6M near-mid block; two later prints show crossed/stale NBBO | thin — small LEAP put hedge, no urgency | agree (Industrials) | — (SPCX fails its own +1) |
| **EWY** | inflow +$15.05M | **BULLISH** | clean, no artifact | genuine buy-side: 2027-06 $160c bid-side aggression ($3.73M, 75 trades) alongside a $8.95M downside LEAP put hedge | n/a (geographic) | SK Hynix (SKHY) overlap reinforces the semis story |
| **GDX** | outflow **−$57.52M** (largest of all 21) | **BEARISH** | mixed 20:00Z-adjacent blocks | 0DTE deep-ITM 75/77.5 call sweeps (~$40M + $33M) look like rolls/closes, not fresh bets | n/a | — |
| **XLP** | outflow −$8.05M | BEARISH | one $33.7M near-mid basket-rebalance block | thin ask-side OTM put buying | **disagrees with the GICS Consumer Defensive inflow** | — |
| **XLE** | outflow −$6.53M | BEARISH | ordinary | thin, mixed | n/a | — |

Rank-only: XLK +$4.20M, KRE +$9.40M, XOP +$7.07M, IGV +$1.78M, XLU +$0.81M, XLY +$0.74M, XLV +$0.62M, EWT +$0.30M, XLC +$0.20M, ITB +$0.05M, XBI −$1.52M, XLB −$0.42M, XLF −$0.19M, XLRE −$0.02M, TAN −$0.13M. No graceful-skips; all 21 returned usable flow.

> **The GDX anomaly is the tape's sharpest single fact this week.** GDX rose **+21.31%** — its best week since 2008 — while carrying the **largest options-premium outflow of all 21 ETFs** (5d −$57.5M, 30d −$100.5M, both labelled BEARISH). This is the cleanest live demonstration of the netting blind spot in the book: a name up a fifth in five sessions reading decisively bearish on net premium. It is *also* genuinely ambiguous — see §3b, where the debate turns on exactly whether that premium is a directional bet or miner-equity longs hedging a parabolic move.

**Swing-book implication:** no sector-wide rotation trade is supported. Technology is the only GICS+gross+ETF-consistent inflow and it is *decelerating* (halved WoW, SMH persistence MIXED). Conviction on every sector call is downgraded one notch for the RETAIL_DRIVEN Friday tape.

---

## 3. Swing Book (1–6 weeks)

### 3a. Long swings (regime-aligned)

| Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure | Invalidation |
|---|---|---|---|---|---|---|---|
| **NVDA** | LOW | 3 | `NA(substrate)` | **watch_only** | Technology sector-leader long on a saturated OI build + sector conditional, less a flow-conflict-lite deduction. DEX accelerated monotonically +$8.18B → +$30.55B with GEX stable-positive and zero flips across both 10d and 30d — the cleanest dealer read in the fleet. | Not entered. Would have been a starter-size defined-risk call spread. | **No dark-pool shelf available** — accumulation-hunter returned an empty board, so the C34 institutional anchor could not be used. Fallback: DEX trajectory turning negative for ≥3 sessions, or a close below the 20SMA. |

**NVDA is the only name in the book, and it does not survive.** Three independent gates fire: fundamentals **CAUTION** (insider MSPR −98.61 3-month average, near −100 in **14 of the last 17 months**, against a 4/4 beat streak and +70.7% revenue growth — a 1-of-3 contradiction, below the ≥2-of-3 VETO bar); **event risk** (CPI at T+3, and NVDA's own earnings 2026-08-26 at T+13, both inside a 1–4 week horizon); and the **debate gate** (bear 0.65 ≥ bull 0.35). Starter → three tiers down → floored at **skip/watch_only**. It never reaches the out-of-regime half-cap.

Two of NVDA's three positive points come from lines this run independently documented as non-discriminating — the +3 `oi-trend` is **C47-saturated** (`consecutive_build_days` 5 == `--days` 5, a floor rather than a count, saturated on *every* mega-cap checked) and the +1 sector line rests on a degenerate all-sectors-equal persistence read plus a flow figure that is **+1.37% of gross**. Its own bull conceded both and argued the case off-rubric on dealer positioning; the bear countered that DEX acceleration during an +11.56% week is plausibly **reverse causality** — dealers accumulate positive delta *because* spot rallied — and that this week's own `gex_advisory_backtest` graded the GEX signal class `NO_GO_NO_EDGE`. That exchange is why the residuals came in 0.35/0.65.

### 3b. Short / fade swings (defined risk only)

**Both names route to `watch_only` and are never sized**, per the 2026-08-01 P0 #1 short-routing rule. This is **routing, not suppression** — theses, structures, invalidations and full gate verdicts are recorded below so the counterfactual keeps resolving.

| Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure | Invalidation |
|---|---|---|---|---|---|---|---|
| **GDX** | DROP | 2 | **0.5915** (n=142, `backtest_clean`, market_excess **+0.0915**) | **watch_only** (routed) | The week's cleanest price-vs-flow divergence: +21.31% price against 30d net premium −$100.5M (−8.42% of gross, BEARISH — one of only two genuinely directional labels in the entire book). Largest ETF outflow of all 21. | ~$20M of Nov-20 **and** Dec-18 P75/P67 put verticals opened in **parallel**, 99.8% ask-side both. Vol-aware: the front is rich (BACKWARDATION, 0.5107 at 7d) and they deliberately bought the **cheap back tenors** (0.4499/0.4564). | Netted flow flipping positive, or the November OI unwinding bid-side. |
| **IWM** | DROP | 1 | `NA(substrate)` | **watch_only** (routed) | Pre-CPI small-cap downside hedge. | Aug-21 ask-side put ladder repeated on **three** days with strikes marching **up** (277/279/282 → 283–295 → 288) — paying more for closer-to-money protection, i.e. rising conviction. Base CONTANGO with no qualifying kink (4.9% vs a 5.0 threshold) ⇒ directional, not event. | **Already partially invalidated:** sweep-tracker found the same puts **sold aggressively at the bid on Friday** — the builder took the hedge off into the weekend. |

**On GDX, the debate is genuinely unresolved and worth reading.** The bull's strongest surviving point is that the ETF creation/redemption outflow is a *structurally independent* flow surface from options positioning, so two separate mechanisms agree on direction. The bear's rebuttal is sharper: the identical "buy the cheap back tenors" structuring was graded a **hedge, not a bet**, on SPY *this same week* (§9), C46 groups SPY/IWM/HYG as one macro trade, and IWM's sibling ladder already unwound Friday. Layered on: gold rose ~8% on the week — **one of only seven such weeks since 1986** — on negative payrolls and dovish repricing, a real macro force against the short. Residuals 0.35/0.65.

⚠ **Distribution caution (C28):** no `distribution_flag` fired on any long-thesis name — accumulation-hunter's board was empty, so there was nothing to flag.

---

## 4. LEAP Book (6–24 months)

**Empty. Zero candidates cleared 6-of-9 gates.**

The mega-caps that would normally seed this book — NVDA, GOOGL, META, UBER, SPCX — were all killed at the **required** cumulative-premium-flow accretion gate, and for an instructive reason: their long-dated OI "growth" is short-dated churn wearing LEAP clothing. NVDA's 90d net is **+$34.5M on $93.5B gross = +0.04%**; GOOGL's 90d is **−$617.1M**, the wrong sign entirely.

The one contender, **BULL** (Webull), reached a full 9-gate workup and failed on three: `uw oi position-rolls` returned **`rolls_detected: 0` on every one of the five covered dates**; conviction-matrix confidence **51.9** against a >70 bar (the alternative ask≫bid path also failed — the LEAP strike was *bid*-heavy, 1,087 ask vs 1,193 bid); and its 7-day OI build is driven by 0–25 DTE churn rather than the long-dated book. Its earnings also land 2026-08-19, twelve days out — informed traders express views around a known near-dated catalyst short-dated, not through 532-DTE LEAPs.

**The genuinely important finding here is what the long-dated tape *was* doing.** LEAP volume share **fell 3.6% → 3.0%** while 0DTE tripled, and the only clean long-dated signal in the funnel is **defensive**:

| Instrument | Structure | Aggressor | Premium |
|---|---|---|---|
| IBIT 861d **P15** (spot 36.80, −59% OTM) | put | **ASK** (58,222 vs 4,345 bid) | $11.9M |
| QQQ 861d **P600** | put | **ASK** (2,037 vs 29) | $22.0M |
| QQQ 406d **P750** | put | ask | $23.6M |
| QQQ 861d **C1100** | call | **BID** (9 ask vs 2,029) | $11.6M |
| QQQ 497d **C900** | call | **BID** (2 vs 504) | $8.0M |
| TLT 532d C90 / C120 | call | **BID** | $1.0M |
| GDX 861d P60 | put | ASK (1,279 vs 293) | $1.0M |

Across the ETF/index complex: **23 put rows ($119.5M) versus 10 call rows ($33.4M)**. Institutions were **buying long-dated downside at the ask while selling long-dated upside at the bid** — an index-level collar/risk-reversal. Read against the macro block (10Y rising while USD weakens, core PCE 3.29%, payrolls negative), this is duration insurance, not multi-quarter conviction. The TLT upside-call selling is consistent with the same rate view.

---

## 5. Volatility Surface — WoW Term Structure & Skew Evolution

**Lead finding: 63% of Friday's raw term-structure labels were artifacts.** Running both snapshots through `scripts/term_structure_hygiene.py` across 43 names:

| | Mon 08-03 | Fri 08-07 (expiry day) |
|---|---|---|
| raw label = BACKWARDATION | 41/43 (95%) | 38/43 (88%) |
| kink-aware `shape` **disagrees** with raw | 11/43 (26%) | **27/43 (63%)** |
| monotonic `base_shape` **disagrees** with raw | 10/43 (23%) | 19/43 (44%) |

2026-08-07 is a weekly-expiry Friday, so the 0DTE bucket dominates the raw curve and the artifact rate is **2.4× Monday's**. Any WoW "shape change" read off raw labels would mostly measure *which day you sampled*. This is exactly the failure the hygiene step exists to prevent, and it is the single strongest argument for keeping it mandatory.

**Newly KINKED across the week (9):** DE, EQT, NLY, SKHY, TTD, U, WOLF, ASTS, IOVA. **Kink resolved (1):** IWM (KINKED → CONTANGO).

Catalyst alignment: **DE** (kink 08-21 vs earnings 08-20), **ROST** (08-21 vs 08-20) and **HD** (08-21 vs 08-18) are genuinely earnings-aligned. **ASTS is misaligned** — its 42dte hump is a September-OPEX cluster, not its 08-10 print. A cluster of the 14dte kinks (U, WOLF, HD, DE, ROST) sit on the **same 2026-08-21 monthly OPEX date**, which means a chunk of the "kink" population is generic monthly-OI liquidity structure rather than idiosyncratic event risk — worth knowing before treating a kink as a catalyst signal.

**IOVA is the standout dislocation:** a **70.6% prominence** kink at 21dte (2026-08-28) with **no matching earnings**, on the week's #1 mover (+55.8%). That reads as a real non-earnings catalyst (FDA/data-readout class) the standard screener cannot see. ROKU's 95.9%-prominence kink at 49dte sits on only 37 contracts against 263/94 on its neighbours — clears the floor but is thin; treat as marginal.

**Skew:** index tail-hedging is **easing, not building** — SPY skew_ratio 1.365 → 1.244, QQQ 1.254 → 1.205, IWM 1.271 → 1.189, all still TAIL_HEDGING but with the put bid unwinding even as VIX sits at a 3-month low and QQQ realised stays at 25.8%. **TTD is the clean skew story**: COMPLACENT (1.013) → **TAIL_HEDGING** (1.176), tracking its −21.9% single-day crash — fresh put-buying showing up *after* the event.

**Calendar-spread candidates: none survive.** Every BACKWARDATION-without-catalyst name (STX, RAM, NOWL) carries **negative VRP** (−0.157, −0.586, −0.327), so fading their front tenor directly contradicts the VRP gate. SNDK is disqualified twice over (VRP −0.606 and the put-sale-netting distortion). An empty bucket is the correct output in a pervasively premium-buying week.

> ⚠ **`uw historical iv-percentile-zscore` substrate defect — universal this week.** Every ticker queried returned `dates_used` between **17 and 82** against a `--lookback-days 252` request. The maximum window achieved anywhere was 82. **No first-class percentile read exists this week**; every percentile in this note is provisional. Worst cases: JMKE n=4 (unusable), SKHX n=17, SKHY n=18.

**Structural bias for next week:** long-vol / premium-buying almost everywhere, with one coherent exception — **DE, HD and ROST are the only positive-VRP names** (+0.060, +0.071, +0.157) and are exactly the three with clean earnings-aligned kinks. That is a small sell-vol island inside a buy-vol week, and it supports an **advisory dispersion idea**: long index vol (SPY/QQQ, both negative VRP) financed against short vol on the DE/HD/ROST earnings island. It is the one structure this week's data supports on *both* legs simultaneously — but note §3/§8, where all three names were gated out on fundamentals and debate.

---

## 6. Earnings — Recap & 2-Week Lookahead

### (a) Recap — prints 2026-08-03 → 08-07

| Ticker | Event | Pre-event thesis | IV crush | Realised move | Grade |
|---|---|---|---|---|---|
| MCD | 08-04 AM | CALENDAR (08-03 report) | −10.4% | +1.17%, orderly | **CONFIRMING** |
| SNDK | 08-05 | CALENDAR | −9.0%, kept bleeding | −5.4% then −6.8%/−3.7% | **CONFIRMING** (mostly) |
| LLY | 08-05 | CALENDAR | −20.6% | +4.86% | **CONFIRMING** — clean crush, contained move |
| ZTS | 08-06 AM | CALENDAR, routed `watch_only` pre-print | **−52.2%**, largest of the week | +3.87% then −5.97% | **CONFIRMING (thesis)**; the kill was vindicated separately on non-vol grounds |
| INSM | 08-06 AM | **SKIP** (dimensions conflicting) | −53.7% | **+33.86%** | SKIP vindicated — a move ~3× any reasonable implied estimate; anyone short vol was destroyed |
| TTD | 08-07 AM | none | −32.7% | **−21.9%** (worst S&P mover) | n/a — post-crash flow flipped **bullish** (+$737K), the exact artifact that mislabelled TTD "bullish" in the confluence screener |
| ABNB | 08-07 AM | none | −21.8% | **+17.4%** | n/a — flow confirmed (+$1.27M) |
| APP | ~08-06 | none | −19.9% | **−19.7%** | n/a — flow confirmed the miss (−$14.5M) |
| SEZL | 08-07 AM | none | −11.9% | **−33.9%** | n/a — flow read **bullish** (+$942K) into a −34% crash; crash-day call buying, not signal |
| DOCS | 08-07 AM | none | −26.6% | **+32.6%** | n/a — **PEAD-disqualifying**: flow read bearish (−$10.9M) into a +32.6% pop |
| TWLO / FIVN / HALO / NTRA / U / IOVA | 08-06–08-07 | none | −34.0% / −30.5% / −13.9% / −18.3% / −28.3% / −17.6% | +24.9 / +19.8 / +20.2 / +21.4 / +15.1 / +43.1 | n/a — all flow-confirmed beats; **U** is the cleanest 2-day continuation |

**Correction to an earlier framing in this run: COHR and LITE have NOT printed.** Their +44.2% and +24.7% weekly moves are **pre-earnings run-ups** (optics/photonics sympathy, plausibly AI-datacenter capex read-through), with earnings still ahead on 08-12 and 08-11. Front IV of 140.8%/138.1% confirms no crush has occurred. They carry forward as lookahead candidates, not recap grades.

**PEAD advisory (0 rubric points, NO_GO register):** ranked by flow-confirmation strength — **U** (2-day bullish continuation) > ABNB / TWLO / HALO / NTRA (single-day confirm) > FIVN / IOVA (thin or fading). **DOCS explicitly disqualified** despite its beat.

### (b) Lookahead — through 2026-08-21 (C12-floored funnel only)

> ⚠ **CPI-day cluster: TRMB, COHR, CSCO and NBIS all report on 2026-08-12 — the CPI print itself.** Any structure on those four eats stacked event risk on the same day, not merely inside the holding period.

| Rank | Ticker | Earnings | DTE | IV rank | Implied move (IV-derived) | Hygiene shape @ fer(7) | Back skew | **Verdict** | CPI overlap |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **HD** | 08-18 AM | 11 | 84.5 | **7.46%** | CONTANGO → **KINKED** @14dte, 8.7% prom, **636 contracts** | **+0.0403 TAIL_HEDGING** | **SELL VOL, full size** | No |
| 2 | **DE** | 08-20 AM | 13 | 84.1 | 9.01% | CONTANGO → **KINKED** @14dte, 12.2% prom, 201 contracts | +0.0326 NORMAL | **SELL VOL, half size** | No |
| 3 | **ROST** | 08-20 PM | 13 | 92.4 | 9.03% | KINKED @14dte, **14.4% prom** (largest), only 73 contracts | +0.0193 NORMAL | **SELL VOL, half size** | No |
| 4 | **HRB** | 08-11 PM | 4 | 56.2 | 11.65% | BACKWARDATION @1.345 | **+0.0981 TAIL_HEDGING** (strongest in batch) | **CALENDAR** — best-priced in the small-cap batch | No |
| 5 | **NBIS** | 08-12 | 5 | 53.7 | 21.72% | raw KINKED @42dte is a **false positive**; true signal smooth BACKWARDATION @1.246 | −0.0299 COMPLACENT | **CALENDAR, caution** — do **not** use the 09-18 tenor as the back leg, it is the anomalous rich one | **Yes** |
| 6 | **COHR** | 08-12 PM | 5 | 87.4 | 19.5% | BACKWARDATION @1.305 | −0.0074 COMPLACENT | **CALENDAR** | **Yes** |
| 7 | **CSCO** | 08-12 PM | 5 | 84.0 | 10.44% | BACKWARDATION @**1.493** (most extreme front ratio in the scan) | +0.0079 flat | **CALENDAR** | **Yes** |
| 8 | **LITE** | 08-11 PM | 4 | 78.4 | 19.1% | BACKWARDATION @1.288 | −0.0045 COMPLACENT | **CALENDAR** | No |
| 9 | **ASTS** | 08-10 PM | 3 | 50.7 | 18.49% | raw KINKED @42dte also a **false positive**; true BACKWARDATION @1.261 | −0.0812 COMPLACENT | **CALENDAR** | No |
| 10 | **TRMB** | 08-12 AM | 5 | 91.4 | 12.75% | BACKWARDATION @1.286 | +0.0199 NORMAL | **CALENDAR** | **Yes** |
| — | MRCY / KEYS | 08-18 PM | 11 | 85.9 / 83.3 | 22.3% / 14.6% | BACKWARDATION | **UNMEASURABLE** | **SKIP** — the mandatory second dimension is unmeasurable, not absent | No |
| — | CECO | 08-10 AM | 3 | 88.7 | ~20.8% | `front_end_ratio` itself unmeasurable (2nd kept tenor is 105dte) | COMPLACENT | **SKIP** — `NO_NEAR_TENOR` class | No |
| — | AAON / ACM / DPC / MWH | 08-10→13 | 3–6 | 74.6–91.5 | null | **INSUFFICIENT_DATA** (0–1 tenors clear the 15-contract floor) | — | **SKIP** — premium unmeasurable, not absent | mixed |

**Two tool defects surfaced here, both verified:**

1. **`uw insights analyst-vs-flow` returns no analyst data at all.** Tested across HD, DE, ROST, NVDA, TSLA, AAPL and COHR — every response contains only `options_flow` and `symbol`. The tool cannot deliver the comparison its name promises, so the **analyst-vs-flow disagreement ranking the earnings rubric calls for is unavailable this week**; the ranking above uses term-structure conviction as its primary axis instead.
2. **`implied_move_perc` is unreliable per-row, not merely mis-scaled.** HD reports `implied_move = $0.63` on a $355.62 close into an 11-day print — 0.18%, roughly 40× too small against an IV-derived 7.46%. But TRMB reads 4.55/59.51 = 7.6%, which is correct and matches its own field. **Some rows are right and most are wrong**, so no single unit conversion repairs it. Every implied move in this note is IV-derived.

---

## 7. Risk & Correlation (week-candidate universe)

**Correlation clusters (30d, 13-name set):**

| Cluster | Members (pairwise) | Kept member |
|---|---|---|
| `macro_hedge_complex` (C46) | SPY/IWM **0.78**; HYG the structural third leg (SPY corr 0.649) | **SPY** (raw 2 > IWM 1 > HYG unscored) |
| `AI_semis_cluster` | MU/AMD **0.841**, COHR/MU **0.778**, COHR/AMD **0.719** | **COHR** (only scored member) |
| SPY/TSLA pair | **0.767** | SPY |

Soft watch (0.60–0.70, no penalty): SPY/AMD 0.677, IWM/COHR 0.667, SPY/HYG 0.649, SPY/COHR 0.644. **NVDA and GDX appear in no pair ≥0.60** — GDX is the only genuine diversifier in the set, and it is short-routed anyway.

**Panic gate: CLEAN — and this is a hygiene save worth recording.** The raw `front-end-iv-ratio` printed **1.376 (SPY) / 1.382 (QQQ) = BACKWARDATION**, which would have fired the >1.10 panic override on the whole book. Both carried `near_dte_actual: 0` — the expiry-Friday 0DTE bucket. Re-read at `--near-dte 5` they are **0.751 and 0.82, CONTANGO**. The panic gate correctly does **not** fire.

**VRP gate:** negative VRP on both indices means **every `vol_short` call contradicts the vol regime** — this fires on HD, DE and ROST.

**Fundamentals verdicts (top-5):** NVDA **CAUTION** (insider MSPR −98.61); DE **CAUTION** (2 of last 4 surprises would have breached the implied envelope; AGCO peer cut guidance −11%; live UAW dispute); HD **CAUTION** (3-of-4 miss streak, leadership overhaul, TSCO guidance cut — partly offset by insider *buying* MSPR +29.98); GDX and SPY **NA — because they are ETFs, structurally inapplicable, not a data gap.** **No VETOs** — no name reached the ≥2-of-3 contradiction signature.

**Debate-disconfirmation cuts — the bear won all four debated names:** NVDA {bull 0.35, bear 0.65}, HD {0.45, 0.65}, DE {0.45, 0.65}, GDX {0.35, 0.65}. SPY recorded as **`n/a_nondirectional`** — no debate was run, because multileg established the barbell carries no directional information and a bull/bear framing would have manufactured a disagreement that does not exist. That is an explicit n/a, not a missing value.

**Breadth cross-check (advisory, `fz`):** 321 advancers / 180 decliners, **63.82% green**, avg +0.70%, median +0.48% — against `uw` options-flow breadth of **37.7% bullish**. **Divergence flagged, and note the polarity is the opposite of the usual tell**: price breadth is strong while options positioning is net-bearish across 6,281 names. Read as a hedging/distribution tell rather than confirmation. Top mover ABNB +17.43%, worst TTD −21.90%.

### ⚠ Systemic finding: the dark-pool accumulation signal is contaminated this week

Share of top-20 dark-pool premium executing in the **20:00–20:25Z closing-cross window** on 2026-08-07:

| NVDA | MU | MSFT | AMD | PLTR | AMZN | MRVL | TSM |
|---|---|---|---|---|---|---|---|
| **80.8%** | **74.9%** | **71.5%** | 61.8% | 57.4% | 27.4% | 12.5% | 5.2% |

MSFT is the extreme case: **10 of its top 12 prints executed at exactly $499.99 — the closing price — totalling ~$2.05B of $2.18B (94%)**, including a $438M print at 21:44 after-hours still pegged to the close, plus **three identical $32.2M prints stamped 20:00:06 to the same second** (the twin-print artifact appearing as a triplet inside one name). MSFT's headline "$4.24B DP premium, 3.42× buy/sell ratio" is benchmark/MOC flow, not stealth accumulation.

Accumulation-hunter found 11–87% contamination **every day, 08-03 → 08-07, across every liquid name checked**. This is not a Friday effect. **Recommendation: escalate to a standing weekly caveat** — any `dark_pool_accumulation` component on a mega-cap needs the closing-cross share reported alongside it.

**Adverse-flow exits (prior group `conviction_week_2026-W31` = MRVL, SNDK, IWM, SPY):**
- **IWM — EXIT CANDIDATE.** The Aug-21 put ladder was sold aggressively at the bid Friday after four straight ask-side build days; the hedge thesis was unwound into the weekend. IV rank 1.7 means re-entry is cheap if wanted.
- **SPY — DECAYING, hold as complex.** Friday net flow −$135.6M with OI +491.8k; the barbell is still in place but the complex is *shrinking* (contrast HYG, which rolled out).
- **SNDK — NO SIGNAL (contaminated), not an exit.** VOLUME_SPIKE + $230.6M DP reads bullish, but this is the active put-sale-netting blind spot: net is 1.4% of gross, MIXED.
- **MRVL — CLEAN.** Bullish flow, OI building, IV rank 72.3. No action.

**Hedge sleeve:** no mechanical hedge fires — the post-gate book is **empty**, net delta zero, so the skew trigger is undefined. Advisory for any legacy long beta carried into CPI: **mirror what the tape itself printed.** Smart money put on an index-level collar this week (23 ETF put rows/$119.5M vs 10 call rows/$33.4M; QQQ 600P and 750P bought at the ask, QQQ 1100C and 900C sold at the bid). A QQQ September put spread financed by upside call sales is the regime-consistent expression: QQQ's −0.054 VRP means the bought leg is cheap versus realised, CPI at T+3 is the named catalyst, and negative payrolls with core PCE 3.29% is precisely the macro cell that punishes unhedged duration. Defined risk only; **no naked short vol into the print.**

---

## 8. High-Conviction Cross-Ref (HIGH and MEDIUM tier)

**Empty — no name reached MEDIUM or HIGH.** The highest raw score on the board was **3 (NVDA, LOW)**, against a MEDIUM cut of 7 and a HIGH cut of 9.

**Expectancy lens (advisory — C31):** not computable this week. There are no closed `conviction_week_*` positions to compute per-tier expectancy or payoff ratios over — the book has been effectively empty for 21 consecutive sessions, so no tier has accumulated a resolved sample. C3 Kelly remains ADVISORY.

**Rubric lines that awarded to NOBODY this week** — a useful read on where the frozen rubric currently has no purchase:

1. **+3 accumulation C11 conjunction** — accumulation-hunter's board was empty; every mega-cap DP read was closing-cross contaminated.
2. **+1 conviction-matrix DIRECTIONAL_LONG >70** — no `leap_directional` class exists in the scored set; the best reading anywhere was 51.9.
3. **+2 position-rolls into LEAP** — the only qualifying evidence (HYG, #1 in the entire market) sits on a name that failed the confluence gate.
4. **+1 mechanized DEX flip / vanna squeeze** — **TSLA was the sole qualifier in the entire market and it failed the confluence gate** (one supporting agent). SPY/QQQ/IWM/NVDA/COHR are stale *levels*; MU/PLTR/TTD/NBIS carry `whipsaw_warning`.
5. **−2 contrarian crowded-long** — **unsatisfiable as written**: `uw historical pc-ratio-zscore` has no `--date` flag, so the "rising z" clause cannot be evidenced. Not awarded on a guess.
6. **−3 full flow_conflict** — no scored name had sign-opposing flow above the median.

Lines that did award: **+3 oi-trend** (NVDA only, and C47-saturated ⇒ zero discrimination); **+2 multileg** (SPY and IWM only — **C46 deflation confirmed: zero single-name equities earned it**); **+1 vol-surface** (DE only, the single verifiable WoW worsening in the funnel); **+1 sector leader** (NVDA, GDX).

**Embedded rubric (for audit):**

```
Weekly conviction score = Σ:
  +3  uw historical oi-trend BUILDING for the full week, --days ≥ 5   # WEEKLY-ONLY +3 vs DAILY +1. FROZEN at +3 (P0.1);
      over-weight PRE-REGISTERED for a future cross-regime audit. SHARPENED → register C47 (2026-07-04 P2 #3, weight
      UNCHANGED under the freeze): backing tool measured −9.2pp class-controlled marginal (n=69, negative in 3 of 4
      regime strata; choppy −36.4pp) AND carries a measurement artifact — consecutive_build_days ceilings at --days on
      liquid names, so the +3 can be earned by expiry mechanics. When quoting this line, state whether
      consecutive_build_days == --days (saturated: the read is a floor, not a count).
  +3  3+ aligned signals in accumulation-hunter sustained across week, uw dark-pool block-stratified institutional-tier
      confirmed — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms (sign aligned AND |cum_flow_30d| ≥
      $50M); else halved (floored) +3→+1.
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70, stable WoW — CONDITIONAL ONLY: award only when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +2  uw oi position-rolls shows institutional roll forward into longer-dated LEAP (per-covered-date)
  +1  uw historical cumulative-premium-flow shows net directional accretion across the week — INTENT-SCREENED: award only
      when (a) no C28 distribution_flag on the name, AND (b) on dividend payers inside an ex-div window, the accreting
      prints are NOT deep-ITM sub-parity calls. Screen failed or unevaluated on a flagged name → 0.
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna squeeze in trade direction — verified SIGN
      CHANGE only, not a level: sign(net_dex) on the latest session opposite to ≥3 consecutive prior sessions, flip-day
      |net_dex| ≥ 0.25× trailing-10-session median |net_dex|, both dated values cited. Compute with scripts/dex_flip.py —
      do NOT do the arithmetic by hand; report sign_changes_in_window / whipsaw_warning.
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector — CONDITIONAL: (a) sector
      persistence_score ≥ 0.6 AND (b) cum_premium_flow_30d direction aligned AND (c) |cum_flow_30d| ≥ $50M. Default 0.
  +1  in earnings-scout BUY VOL or SELL VOL for next 2 weeks (uw options-structure term-skew aligned for full size)
  +2  multileg-strategist directional structure repeated on ≥2 days (term-structure-anchored play type)
  +1  vol-surface-scout flags KINKED or BACKWARDATION, worsening WoW; uw historical iv-percentile-zscore extreme;
      VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner crowded long with rising uw historical pc-ratio-zscore trajectory (VRP positive)
      # MECHANISM: an INFORMED-FLOW CONTINUATION penalty, not "crowd is wrong, fade it".
  -3  flow_conflict — cum_premium_flow 30d direction *clearly opposite* dominant_signal_class (signed-sum sign flip +
      magnitude > union-median |cum_flow_30d|, or explicit OPPOSITE label)
  -1  flow_conflict_lite — 30d cum_premium_flow read is MIXED (signed sum near zero, or aligned but bottom-quartile)
      # -3 and -1 are mutually exclusive: apply ONE, never both.
  # TIER GATES applied by risk-monitor in Step 2d (0 points, never in score_components):
  -2  [TIER GATE] correlation cluster (pairwise corr ≥ 0.70) — −1 TIER
  -3  [TIER GATE] WoW regime flip conflicts with trade direction — −1 TIER

Tiers: ≥9 HIGH (full) | 7–8 MEDIUM (half) | 3–6 LOW (starter/watch) | ≤2 drop
Rubric version: 2026-06-12 (FROZEN). Out-of-regime guard P0.6: all sizing capped at HALF.
```

---

## 9. Setups for Next Week

### Next-session GEX advisory (SPY/QQQ only — prose-only, 0 rubric points)

**Lead with the track record: the Step 0 rolling backtest returns `NO_GO_NO_EDGE` (pooled n=118).** The next close landed closer to the nearest GEX wall only **21.2%** of the time against a 50% baseline (p=1.0) — walls behave as **anti-magnets**; price systematically moved *away*. H1 also runs backwards: short-gamma mean absolute return 0.747 versus long-gamma 0.953, the opposite of dealer-hedging theory. Everything below is dealer *context*, never a forecast.

- **SPY** — spot 772.84, ZGL **772.36** (`zgl_reliable: true`, 0.06% from spot), regime **POSITIVE**, total_gex $1.85B. Call wall **773** (essentially at spot), put wall **755** (−2.31%). Nominally a long-gamma pin setup — but the regime flipped POSITIVE only *today* after two flips this week (POSITIVE→NEGATIVE 08-05, NEGATIVE→POSITIVE 08-07) and four in 30 days. Fresh and unstable, not a held read.
- **QQQ** — spot 722.39, ZGL **721.08** (reliable, 0.18%), regime **POSITIVE**, total_gex $853M. Call wall **730** (+1.05%), put wall **715** (−1.02%) — a wider, more symmetric range. Regime is *less* stable than SPY's: NEGATIVE (07-30) → FULLY_NEGATIVE (07-31) → POSITIVE (08-03–08-05, including a garbage extrapolated ZGL of 249.5 on 08-05, correctly discarded) → NEGATIVE (08-06) → POSITIVE (08-07). **Three regime changes in five sessions.**

Mandatory caveats: the EOD book is a prior that gets refreshed by fresh 0DTE OI in the first 30–60 minutes of the open; gap risk; this is the ETF book, not the cleaner index book; `uw` cannot isolate the D+1 expiry, so this is a 0–45d proxy. With 0DTE share at 46.4% and both indices flipping regime repeatedly, the standing book going into Monday should be read as a noisy, fast-refreshing prior.

### Next-session 0DTE premium-selling setup (validated stack — advisory, 0 rubric points)

Rolling backtest `verdict: GO_PREMIUM_SELL_INTRADAY` (n=60 each).

| | SPY | QQQ |
|---|---|---|
| Win rate (open entry) | 88.3% | 85.0% |
| **mean_pnl_open_pct (GROSS)** | **+0.223%** | **+0.360%** |
| **mean_pnl_open_net_pct (NET of 0.1% round trip)** | **+0.123%** | **+0.260%** |
| Worst day | −1.40% | −2.453% |
| Structure | iron fly / short straddle centred **772.89**, wings ≈ **±0.83%** | centred **722.68**, wings ≈ **±1.45%** |
| vol_state / VIX / size scalar | LOW / 14.9 / **0.5** | LOW / 14.9 / **0.5** |

`pnl_basis`: **percent of underlying spot notional, GROSS** — not premium-collected, not margin-relative. Lead with the **net** line. Entry rule: enter at/after the open once the overnight gap resolves; stand aside if it gaps beyond the wings; **hold to the close, never carry overnight** (SPY overnight mean +0.017%, QQQ **−0.092%**).

> ⚠ **Two caveats that matter more than usual this week.** First, the unsampled tail: the validation window contains **no vol shock**, so the short-vol left tail is unsampled and win-rate is explicitly *not* the promotion metric for a negatively-skewed payoff. Second, and specific to now — **VIX at 14.9 sits in the LOW tercile (bounds 16.4/18.0), and the backtest's mean PnL in the LOW-VIX state is NEGATIVE for SPY (−0.059%) and roughly flat for QQQ (+0.016%).** The edge lives in the MID and HIGH VIX cells; the current state is the one cell where it does not pay. The 0.5 size scalar already reflects this. Advisory, 0 rubric points, permanently until a shock enters the sample.

### Dealer-positioning swing setups (1–4 weeks)

**TSLA is the single most interesting name on the tape and it is not in the book.** It is the **only mechanized DEX sign-flip in the entire market this week** — `dex_flip.py` returns `qualifies: True`, `whipsaw_warning: False`, net_dex −$2,823,212,218 (08-06) → **+$1,037,105,324** (08-07) against three consecutive negative prior sessions, with |flip| 1.59× the magnitude floor — *and* the only put-heavy vanna book (net_vanna +9,526) with VIX down three straight sessions, so the flip and the squeeze conditions align independently. Its front-end ratio of 0.923 CONTANGO means the squeeze is still *building*, not maturing.

It fails the confluence gate on one supporting agent, and the counterfactual is instructive: had it entered, the frozen rubric would have scored **+1 (flip) − 3 (flow_conflict: cum_flow_30d −$616.8M against the long, 6.1× the union median) = raw −2 → drop anyway.** The gate and the rubric agree. Its 30-day GEX book also carries **7 regime flips** — the most unstable in the set.

Other swing reads: **NVDA** cleanest structural level (stable positive GEX, zero flips) but gated out; **PLTR** strong level with GEX total nearly tripled, though 4 sign changes in 16 sessions flag whipsaw; **COHR** long but **maturing/extended** (+44.2% with a panicked 1.305 front ratio); **NBIS short building** (DEX, GEX and front-end panic all agree bearish, flip one session too old to qualify); **AMD** flat/caution on a live disagreement (DEX positive level while GEX flipped negative the same session); **MU, STX, TTD** no clean thesis.

### Pin vs trend

**Trend, weakly — but with low conviction in the GEX read.** Both indices sit essentially on their zero-gamma levels with positive total GEX, which nominally favours pinning; but both flipped regime two to three times this week, the walls are backtested anti-magnets, and 0DTE share at 46.4% means the book refreshes fast. Treat neither as a reliable prior.

### Actionable setups

**None at HIGH tier — there are no HIGH-tier names.** The honest recommendation for the coming week is to hold no new directional risk into CPI (08-12) and, if legacy beta is carried, express the hedge as the defined-risk QQQ collar in §7.

**LOW-tier names to track for daily confirmation:** NVDA (watch for the insider pattern breaking or a post-earnings re-rate after 08-26), TSLA (whether the DEX flip survives a second session and picks up a second agent), GDX (whether the −$100.5M premium outflow converts to price weakness or was simply a hedge), DE/HD/ROST (whether the positive-VRP island survives their prints).

**Deep-dive hand-off:** skipped — no HIGH-tier, post-gate, non-VETO name exists. This is a no-edge week.

---

## 10. Watch-only — single signal, no confluence

Names surfaced by one agent but failing the ≥2-agent confluence gate. **For journaling, not trade entry.**

| Ticker | Sole flagging agent | Why it failed |
|---|---|---|
| **TSLA** | dealer-positioning | The market's only mechanized DEX flip + vanna squeeze. sweep-tracker graded it mixed. Counterfactual raw −2 (drop) after flow_conflict. |
| **HYG** | multileg | **#1 position-roll in the entire market** (near_oi −54,207 / far_oi +79,090, puts — the hedge is being *extended*). Jan-2027 P65 at 99.3% ask for $1.13M = extreme cheap convexity. Term anchor LOW confidence (8 of 17 tenors below the contract floor). Third leg of the C46 complex. |
| **MSTR** | multileg | Dec-2028 C100/C110 LEAP vertical, ~$15.4M risk vs $50M max, buys the expensive end of the curve. Single-day; OI-unverifiable until 08-10. |
| **NBIS** | earnings-scout (vs dealer bearish) | Directional conflict; −17% in 3 sessions; earnings on CPI day; whipsaw TRUE. |
| **PLTR** | dealer-positioning | Level not flip (whipsaw TRUE); multileg OI-unverifiable; the calendar earns nothing from a FLAT term structure. |
| **GOOGL** | — | Multileg direction **inverted by the T+1 OI correction**: sold the 375, bought the 410 ⇒ **net credit ~$72M taken off the table**, not fresh bullish risk. |
| **MSFT** | — | Same roll-up-and-out template, ~$12.78/sh net credit. DP tape 94% closing-cross. accumulation-hunter disqualified it on conviction-matrix COVERED_CALL. |
| **MU / AMD** | sweep-tracker (thin) | Both `short`; MU whipsaw TRUE and decelerating, AMD carries a live DEX-vs-GEX disagreement. |
| **SPCX** | sweep / sector (conflicted) | Tool says bearish, day-count says bullish on 4 of 5 days; 30d flow −$20.2M contradicts the daily print. |
| **ACHC** | contrarian (flagged, not surfaced) | The week's one genuine price-vs-flow divergence (+15% price, bearish flow) — but single-name P/C extremes predict **continuation, not reversal**, so it is an informed-continuation watch, not a fade. |
| **IOVA** | vol-surface + earnings (advisory) | 70.6%-prominence kink with no earnings match; 30d flow −38% of gross **bearish against** the week's #1 mover. |
| **IBKR / AVB** | contrarian (stood down) | BEARISH_EXTREME P/C z (5.997 / 3.542) but `divergence: false` — price and flow **aligned**, i.e. real hedge bids, the case the mandate explicitly warns against fading. |

---

## Appendix — Single-Leg Whale Persistence (advisory, permanently 0 points; C19 CLOSED as REFUTED 2026-07-25)

Tier-1 opening/floor PUT signals across the five covered sessions: **12 distinct names, zero repeats.** No name threw a repeat Tier-1 print, so **there is no persistence signal this week** — the primary thing this scan looks for did not occur.

**A defect worth registering: the Tier-1 classifier has no moneyness screen.** The two largest "Tier-1 opening put" prints of the week are both **1 DTE and deep in the money**:

| Date | Ticker | Label | DTE | Premium | Strike vs spot |
|---|---|---|---|---|---|
| 08-06 | **SNDK** | OPENING_PUT_PRIME | **1** | **$12,150,000** | **+46.9% ITM** (K 1900 vs spot 1293.53) |
| 08-06 | **APP** | OPENING_PUT_PRIME | **1** | $2,293,500 | **+61.5% ITM** (K 550 vs spot 340.47) |
| 08-07 | NFLX | FLOOR_PUT_BLOCK | 14 | $1,737,200 | +29.0% ITM |
| 08-06 | META | FLOOR_PUT_BLOCK | 15 | $832,425 | +25.6% ITM |

A put struck 47% above spot with one day to expiry is **parity/exercise mechanics** — a delta-1 or conversion leg — not "an institution shorting a specific name against the tape," which is what the tool's own `note` field claims. Multileg independently caught the same SNDK structure and found the near leg printed **below parity on the bid (a sale)**, confirming it carries no directional information. The clean, near-the-money Tier-1 signals this week were **DDOG, U, FLR, RL, NVDA, TENX, AAPL and LITE**.

Reported as descriptive colour only. C19 was closed as REFUTED (register C53); there is no rolling-WR gate left to clear and no promotion path to report against. This does **not** refute the 2026-05-29 Tier-1 PUT backtest, which was a different measurement on a different substrate.

---

*Rubric version `2026-06-12` (FROZEN). Generated 2026-08-07. Phase 1: 10 agents (OPEX guard not triggered — third Friday 2026-08-21 is 14 days out). Post-gate conviction book: **empty**. Watchlist write-back: **deliberately empty** — `conviction_week_2026-W32` was not created.*
