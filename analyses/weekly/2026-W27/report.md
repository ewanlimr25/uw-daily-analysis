# Weekly Market Intelligence — Week of 2026-06-29 (ISO 2026-W27)

*4-day week: Friday 2026-07-03 closed (July-4th observed). Data week-end = 2026-07-02. Next session Monday 2026-07-06 after a 3-day weekend.*

## Executive Summary

- **Week regime + WoW Δ:** TRANSITIONAL held Monday→Thursday; trend UPTREND intact (SPY 744.78 > 20SMA 741.08 > 50SMA 737.43) but breadth deteriorated 37.9%→34.9% bullish — a narrowing tape grinding higher. VRP FAIR / mildly negative (SPY −0.017): no premium-selling edge, slight premium-buyer tilt.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half` (P0.6 guard; non-binding this week — nothing survived above starter).
- **Signal performance:** 0 of 1 resolved won (hit rate 0/1 = 0%); 2 INCONCLUSIVE excluded; 3 total calls in universe (3 envelope-anchored, 0 reconstructed). The one resolved call — SNDK long, 06-30 envelope, LOW/watch-only — was a −23.3% LOSS; no capital was ever recommended on it, and the daily fleet itself flipped SNDK long→neutral→short before the crash completed.
- **Top swing build for next week:** none sized. Best surviving long is **HOOD (raw 4, LOW → watch-only)** — week-long OI build + Tech-leader confirmation, killed at the debate (OI build decomposes into direction-mixed gamma churn; bear tie 0.55/0.55). Trigger to promote: `uw oi smart-positioning` showing a clean bullish OTM-call skew plus insights-accumulation ≥3 consecutive ACCUMULATION days.
- **Top LEAP build:** none — zero candidates cleared 6-of-9 gates (third consecutive empty LEAP book). NKE was the near-miss (clean 2027 C55 build + $152M DP shelf at $44.09) but chain-wide 30d/90d cum-flow is net **bearish** — hard Gate-4 kill.
- **The only sized line:** **SPY Jul-17 defined-risk put hedge, starter, HEDGE BUDGET ONLY** (~740/720 vertical, ≤0.5% NAV premium). It is insurance for the CPI 7/14 + banks 7/14-15 + OPEX 7/17 cluster sitting on FULLY_NEGATIVE dealer books — not an alpha short (desk record on index alpha-shorts: 0-for-4).
- **Biggest emerging risk:** the memory/semicap crack (SNDK −14%, WDC/MU/AMAT/STX/LRCX at IV rank ~100) spreading into core Tech while the index event cluster lands 7/14–17 on freshly-flipped FULLY_NEGATIVE gamma. Watch item from last week's book: **AMAT vol-long has realised (IV rank 100) — harvest zone, not add zone.**

---

## 0. Week in Review — Intra-Week Signal Performance

Universe = union of `calls[]` across this week's daily `decision.json` envelopes (hindsight-free, survivorship-free; the one deliberate override of the fresh-CLI principle). All four covered dates had envelopes. Of ~70 rows, only **3 were non-DROP** (all LOW/watch-only) — the empty-conviction-book protocol in action all week.

| Ticker | Direction | Source | Move vs ATR | Flow/OI | Grade | Note |
|---|---|---|---|---|---|---|
| SNDK | long | envelope 2026-06-30 (LOW/watch-only) | −528.7 pts (−23.3%) vs 0.5×ATR(14) = 89.5 | Flow reversed hard against (glut-fear unwind; bearish net flow, IV rank 100) | **LOSS** | No capital recommended; daily fleet flipped to neutral (07-01) then short (07-02) before the low |
| BABA | long | envelope 2026-06-29 (LOW/watch-only) | +0.63 vs 0.5×ATR = 0.83 | Bullish net flow 07-01/07-02, mild support | INCONCLUSIVE | Sub-threshold move; September straddle flow noted by multileg (vol, not direction) |
| IBIT | long | envelope 2026-07-02 (LOW/watch-only) | zero forward window (called at week-end) | n/a | INCONCLUSIVE | Resolves next week; this week's Phase 2 independently killed it (collar decomposition, bear 0.85) |

**Headline: 0 of 1 resolved (0%); 2 INCONCLUSIVE excluded; 3 total (3 envelope-anchored, 0 reconstructed).** A 0-for-1 on a watch-only universe is a calibration datapoint, not a P&L event — the system's refusal to size anything this week was itself the correct call.

---

## 1. Regime & WoW Delta

- **Regime:** TRANSITIONAL on 06-29 and still TRANSITIONAL at week-end (held). Trend UPTREND: SPY 744.78, above both rising SMAs, −2.05% from 90d high. Trading guidance unchanged all week: half sizes, defined risk.
- **Breadth:** bullish-flow tickers 37.9% → 34.9% WoW (deteriorating under a green tape). fz cross-check (advisory): 70.97% of S&P 500 green on 07-02 (357 adv / 145 dec) — **no divergence** with the regime label; the softness is in options flow breadth, not cash-market breadth.
- **VRP:** FAIR (SPY VRP −0.0166; IV30 13.6% vs RV30 15.3%). No premium-selling edge; contrarian fade engine disabled by rule this week.
- **DTE volume share (MARKET, 07-02):** 0DTE 0.0 (holiday-adjacent artifact), weeklies 0.20, monthlies 0.162, LEAPs 0.04 — regime hint BALANCED; no retail-tape downgrade.
- **Front-end IV:** SPY 0.526 / QQQ 0.694 — deep CONTANGO. The long weekend crushed near-dated IV; there is zero panic premium anywhere in the index complex. Protection is cheap; that fact is load-bearing for §9.
- **Macro backdrop (FRED):** curve normal (+0.35 10s2s), core CPI 2.96% / core PCE 3.41% YoY, unemployment 4.2% with payrolls +57k (soft), 10Y 4.48% flat, USD strengthening, fed funds 3.63%. June jobs printed Thursday 07-02 (holiday schedule) — soft enough to read rate-cut-friendly; Fed tone into the week was dovish (Warsh at Sintra). Net macro read: dovish-drift tape with a hot event cluster ahead.
- **Event risk (next two weeks):** FOMC minutes 7/8 · jobless claims 7/9 · **CPI (June) 7/14 — Tier-1, confirmed** · PPI ~7/15 · retail sales + claims ~7/16 · **monthly OPEX 7/17** · **Q2 bank earnings kickoff 7/14–15 (JPM/GS/WFC/C/BAC)** · FOMC decision 7/28–29 (outside window). The 7/14–17 span is one fused elevated-vol window, not four independent events.
- **Implication for next week's bias:** dovish macro + intact uptrend argue for continuation; deteriorating flow breadth + semicap crack + FULLY_NEGATIVE dealer gamma argue the continuation is fragile. The desk expression is not a direction call — it is cheap defined-risk protection into 7/17 and patience on the long book until the tape confirms.

## 2. Sector Rotation

**Rotation regime call: `no_change` (low confidence).** Every GICS sector printed INFLOW with persistence 1.0 (5-of-5 sign-consistent) — a broad trending tape gives the rotation engine nothing two-sided to work with. Applying the market-relative bar, only **Technology** (~$3.1–6.0B/day, wk-end +$3.07B) and **Consumer Cyclical** (+$488M wk-end) clear both magnitude and ETF cross-confirm.

- **Healthcare: downgraded to watch-only.** GICS shows +$435M call-heavy inflow, but both representative ETFs disagree (XLV −$0.7M MIXED; XBI −$12.1M BEARISH). The "inflow" is small/mid-cap bullish flow (DVA, MRNA, VRTX) fighting mega-cap distribution (UNH, LLY, INCY). Single-name RS, not sector rotation.
- **Industrials: bearish at the ETF level.** XLI −$2.3M with a $7.4M ask-side Sep 165P sweep — fade the regime tool's single-day "INTO Industrials" read. Short/de-risk candidates: CAT, GE, HON, VRT, UAL, AAL. The defense/aerospace pocket (RTX, NOC, BA, AXON, RKLB) is bullish and must not be grouped into that short list.
- **Financials: narrow, not sector-wide.** XLF flat; **KRE genuinely bullish** (+$25M, aggressive $35.2M ITM Aug C70 ask-side sweep) — a regional-bank pocket into the 7/14–15 bank prints. VOYA is a standout idiosyncratic insurance long (fz new-high cross-confirmed).
- **Defensive undertow forming, not yet tradeable:** insurance (AXS, VOYA, ALL, CB, CINF), select pharma (ABBV, VRTX, ILMN, INCY), aerospace/defense — needs 2–3 more sessions of persistence before it is a rotation call.

**ETF flow tape (advisory — 0 rubric points):**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| IGV | inflow +$86.1M | BULLISH | Large below-mid creation-flavored blocks | Puts bid into strength (hedged longs) | agree (Tech) w/ caution | n/a (thematic) |
| KRE | inflow +$25.0M | BULLISH | Normal near-mid | **$35.2M ITM Aug C70 ask-side buy** | disagree (XLF flat — pocket only) | JPM, C, AXP, MA, CBOE, VOYA |
| XLE | inflow +$14.3M | BULLISH | Normal | LEAP-dated, low urgency | tentative agree | — |
| XLK | inflow +$5.7M | BULLISH | not deep-pulled | — | agree | AAPL, MSFT, PLTR, TSM, NET, HOOD, MSTR, SNOW |
| XLY | inflow +$1.9M | BULLISH | not deep-pulled | — | agree | HD, ABNB, MELI, BABA, MCD |
| **XBI** | **outflow −$12.1M** | BEARISH | Above-mid buy blocks (DP ≠ options; ambiguous) | Puts dominant, bid/mid side | **disagree (Healthcare)** | JNJ/MRNA/VRTX bullish pocket vs UNH/LLY/INCY bearish |
| **EWT** | **outflow −$4.2M** | BEARISH | Wide NBBO | Mixed | n/a (Taiwan) | Corroborates semicap crack |
| **XLI** | **outflow −$2.3M** | BEARISH | Normal | $7.4M ask-side Sep 165P | **disagree (Industrials)** | CAT, GE, HON, VRT (de-risk); NOT RTX/NOC/BA/AXON |
| SMH | +$63.3M but MIXED | MIXED | — | — | flag | Semicap crack watch — non-persistent |

GICS-vs-ETF agreement: Tech and ConsCyc agree → high-conviction continuation; Healthcare and Industrials disagree → watch-only / bearish-lean respectively. The tape strengthens the conditional sector-leader +1 only for Tech names (HOOD was the beneficiary this week); it adds no rubric points itself.

## 3. Swing Book (1–6 weeks) — ranked by weekly conviction score

**No HIGH, no MEDIUM — third consecutive near-empty week.** The frozen bands (HIGH ≥9 / MED 7–8) are structurally empty; the deductions doing the work are mechanical `flow_conflict` lines — the 30d options tape refuses to confirm the flashy microstructure signals.

### 3a. Long swings (regime-aligned)

| Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure | Invalidation (C34-anchored) |
|---|---|---|---|---|---|---|---|
| HOOD | LOW | 4 | NA(substrate) | **watch_only** (debate −1) | Full-week OI build (+26.7k→+54.7k/day) + Tech-leader confirm (cum_flow_30d +$100.7M aligned); fundamentals CONFIRM (rev +41.5%, Chain mainnet catalyst stack) | None until promoted; expression when promoted = defined-risk calls | DP shelf **$108.65** (secondary $98.69, $584M/83 trades); thesis dead if insights-accumulation prints DISTRIBUTION 2+ sessions or OI build breaks |
| AAPL | LOW | 3 | NA(substrate) | **watch_only** (fundamentals −1, debate −1; hard-no for sizing) | Persistent block-tier DP buying (0.50–0.70 all week, $500M non-CC 6/29) + OI build — but insider MSPR −50.5 and 30d flow −$136.5M flipped bearish in the same window at the highs | None | Deep DP shelf **$283.78** ($18.05B); active week shelf $308.63; watch for block-tier <0.50 for 2+ sessions |
| ~~MRNA~~ | LOW | 3 | NA(substrate) | **VETO → watch-only** | Strongest DP footprint of the week ($400M non-CC mega buys) — but the gate caught distribution dressed as accumulation: COVERED_CALL scenario on the print day, squeeze-labeled +66%/30d run, rev −30% YoY, no forward catalyst | — | — (not persisted) |

⚠ **Distribution cautions (C28, advisory):** HOOD — Jan-27 C140 LEAP call closed $1.14M (6/30). AAPL — ~$11M call-side OI closings 6/30 incl. LEAP C310 −1,309 contracts. MRNA — LEAP call close $539K (minor vs the $183M same-day buy, but the VETO rests on bigger things).

### 3b. Short / fade swings (defined risk only)

| Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure | Invalidation |
|---|---|---|---|---|---|---|---|
| SPY (hedge) | LOW | 3 | NA(substrate); advisory bearish_flow class 0.529 n=138, +13.8pp vs SPY-short bench | **starter — HEDGE BUDGET ONLY** | Cross-asset institutional protection cluster (SPY 2-day put roll + IWM 3-day ladder ~$105M + HYG credit ladder) all expiring **7/17**, bought against contango-crushed cheap fronts, into the CPI/banks/OPEX window on FULLY_NEGATIVE dealer books | **Jul-17 put vertical ~740/720**, ≤0.5% NAV premium, defined risk; expires at the event window by design | Structure is self-invalidating (premium cap). Thesis falsifiers: IWM/HYG ladders stop repeating; GEX flips back positive pre-CPI; breadth re-expands >37.9% |
| IBIT | DROP | 1 | 0.478 (n=138, excess −0.080 = beta) | **skip** (debate −1; WR floor) | The "+$306M bullish accretion" decomposed as the call leg of a collar (put walls 25–35 dollar-matched vs call walls 40–60); record June BTC-ETF outflows against it | None | — |

Unscored-but-real structures (conf=1, cannot enter the book — §7/§10): **IWM** 3-day Jul-17 put ladder (~$105M — the strongest single structure of the week), **HYG** 2-day credit put ladder, **WULF** 2-day put spread (front-backwardated, move already priced). The dropped mechanized DEX flips — **PLTR long** (clean flip, GEX +37M→+214M) and **MU short** (flip + same-day GEX regime break) — were each killed by −3 `flow_conflict` (30d cum-flow opposes both). They are flip-context watch items, not trades; see §9.

## 4. LEAP Book (6–24 months)

**Empty — zero candidates cleared the 6-of-9 gate stack.** Near-misses, documented:

| Ticker | Killed by | Detail |
|---|---|---|
| NKE | Gate 4 (cum-flow) | Clean 2027 C55 build (+9,001 OI, ask-dominant) + $152.4M DP shelf at $44.09 — but 30d −$34.7M / 90d −$51.6M net BEARISH (larger OTM put builds outweigh the call); conviction-matrix confidence 31.3 |
| IBIT | Gate 2 (structure) + Gate 8 | Jun-27 C55 +20k calls arrive WITH +39k OTM puts (35/22/30) = collar/overlay; recurring roll is put-side; confidence 17.8. Same watch-only outcome as every prior IBIT build |
| TLT | Gate 4 + Gate 8 | Ask-dominant 2028 C95/C100 duration bets, but 30d −$127.5M and scenario COVERED_CALL |
| PSKY | Gate 8 explicit reject | Scenario COVERED_CALL; per-day strike churn = MM hedging on a thin book |
| MSFT / WMT / RKT | Gates 4/8; Gate 1 | Thin LEAP presence vs near-dated noise; WMT is put-protective; RKT was small-book coincidence |

Data-quality note for `/calibration-audit`: `historical oi-trend --days 10` returned `consecutive_build_days = 10` (the ceiling) for every liquid name checked — Gate 1 was non-discriminating this week; Gates 4/8 did all the work.

## 5. Volatility Surface — WoW Term Structure & Skew Evolution

The complex was already dislocated on 06-29 and mostly stayed there — 10 of 12 elevated-IV names were BACKWARDATION/KINKED at both endpoints. What changed:

- **WDC — the one clean WoW flip:** FLAT→BACKWARDATION (7d/28d ratio 0.987→1.121, still rising), iv-pctile z=3.06. Panic still building, no catalyst for 27 days — **no fade, no calendar; hold off.**
- **SNDK / AMAT — sharpest escalation:** SNDK front IV +12.7pts to 139.6%; AMAT ratio +16pts to 1.19 and pc-z crossed **+2.59σ** on 07-02. Both fail the ">1.10 and rising" disqualifier — event-driven, do not fade.
- **OPEX-kink artifact (new methodology flag):** MU/AMAT/ARM/TXN "kinks" land exactly on monthly-OPEX expiries (Jul17/Aug21/Sep18/Dec18) — unweighted avg_iv wing contamination, not event premium. Only **ASML (kink 7/17, 2 days after its 7/15 print)** and **TSM (backwardation into 7/16)** carry genuine catalyst alignment → §6.
- **Raw-rank vs robust-z divergence:** MU reads IV rank 100 but iv-pctile z = **0.878 (70th pct, NORMAL)** — the headline rank materially overstates MU's vol extremity. ARM/AMD similar (z≈1.4). All percentile reads this week are PROVISIONAL (`dates_used=57` < 120-day bar).
- **Calendar candidates:** only **LRCX** (marginal, small size — sell ~7/17 straddle / buy ~9/18; the "backwardation" is a cheap far tail, not a rich front). MU was mechanically the best setup but is **VRP-disqualified** (name VRP −0.246, most negative in set — if anything, buy Sept optionality small).
- **Notable whale print:** KLAC Sep C118/C100 buying ($1.85M at ~130% IV) ahead of its 7/30 print — institutional pre-earnings convexity, consistent with the name's negative VRP. (C19 cross-flag: a Tier-1 opening put hit KLAC 7/02 — two-sided institutional interest; no clean directional read.)
- **Rate vol:** TLH percentile 0 / z −1.52 (confirmed by the robust metric — rare this week); ZROZ/EDV by extension. Cheap convexity for rate-shock hedges. ASHR (China A) percentile 100 with a genuinely strong z=3.24.

## 6. Earnings — Recap & 2-Week Lookahead

**(a) Recap — the flow crowd went 1-for-4 on direction this week:**

| Ticker | Print | Pre-event flow thesis | Outcome | Grade |
|---|---|---|---|---|
| NKE | 06-30 post | Bearish tilt; front-ratio 1.417 (extreme panic) | Beat, **+7.4%** (≈ implied move); IV crushed 89→33 | Direction DISCONFIRMING / vol-magnitude CONFIRMING |
| FDS | 07-01 pre | Bearish tilt | Beat, **+6.7%** | DISCONFIRMING |
| GIS | 07-01 pre | Mixed-bearish | Beat, **+8.5%** | DISCONFIRMING (bearish leg) |
| STZ | 06-30 pre | Bearish; front-ratio 1.327 | −2% net drift; IV crush paid | **CONFIRMING** |

Pattern worth keeping: the >1.4 front-end panic reading (NKE) marked the zone where the crowd was most wrong; ~1.3 (STZ) was calibrated. Also: all three beats saw post-print flow stay bearish while price rallied — no PEAD candidates (explicit disqualifier). SNDK/MU/WDC and MRNA were *not* earnings events (glut-fear unwind and Science-Day squeeze respectively).

**(b) Lookahead (2026-07-06 → 07-17) — vol-seller's calendar, all sizes pre-capped at half at emission (earnings_vol has no clean backtest substrate; 2026-06-27 audit: earnings_vol/high_iv_rank are the two BH-surviving miscalibrations):**

| Rank | Ticker | Date | Kink (hygiene-corrected) | Skew | Flow | Play | Size cap |
|---|---|---|---|---|---|---|---|
| 1 | ABT | 7/16 pre | KINKED 14d (+10.1pp), covers print | TAIL_HEDGING both tenors | Bullish | **SELL VOL** — condor/strangle at 7/17 expiry | half |
| 2 | JPM + banks bloc | 7/14–15 | KINKED 14d (+10.1pp) | TAIL_HEDGING both tenors | Bullish | **SELL VOL — size the 6 banks as ONE correlated position** | half (bloc) |
| 3 | CTAS | 7/15 pre | KINKED 14d (+10.4pp) | Back stretched, front normal | Thin bullish | SELL VOL, modest | half |
| 4 | ASML | 7/15 pre | KINKED 14d (+26.3pp — largest) | Back-month FLAT/complacent → disqualifier for full | Bearish | SELL VOL half or calendar | half |
| 5 | NFLX | 7/16 post | KINKED 14d (+26.1pp) | COMPLACENT both tenors + call-crowded | Bullish | Defined-risk only (iron condor; no naked) | half |
| 6 | TSM | 7/16 pre | NO kink — monotonic backwardation; ratio 1.132 >1.10 bar | Complacent | Bullish premium / put-heavy volume divergence | **Calendar / wait-for-unwind** — sector panic bleed, not event pricing | no position |
| — | PENG 7/7, MAN 7/16, AZZ 7/8, SMPL 7/9 | | | | | **SKIP** — PENG binary (22% implied, no tail hedge anywhere, dte 5 event-risk flag); MAN/AZZ/SMPL fail the ≥15-contract liquidity floor (the FDX-precedent class) | — |

Data flags: `implied_move_perc` is mis-scaled (0.4–0.6%) on large liquid names this cycle — do not quote it; `analyst-vs-flow` returned flow-side only (no analyst leg) — disagreement scores unavailable this week.

## 7. Risk & Correlation (week-candidate universe)

- **Correlation clusters (30d):** HOOD/PLTR 0.737 (`retail_momentum_cluster` — HOOD is the kept member, PLTR already dropped); MU/WDC 0.721 (`semicap_storage_cluster` — both dropped; hedge-sleeve relevance only). Expected HOOD↔IBIT and AAPL↔SPY clusters did **not** confirm (<0.60). Cluster gate fired on zero book members.
- **Macro & event risk:** CPI 7/14 (T+7) + Q2 banks 7/14–15 + OPEX 7/17 (T+10) = one fused window. Own-earnings inside the swing horizon: HOOD 7/28, AAPL 7/30, MRNA 7/30 — defined-risk-only exemption applies; any undefined-risk expression would take the event-risk tier cut.
- **Fundamentals verdicts (top-5):** HOOD **CONFIRM** · AAPL **CAUTION** (insider MSPR −50.5 — live and material; corroborates the 30d flow flip) · MRNA **VETO** (distribution-dressed-as-accumulation: COVERED_CALL scenario on the $183M print day, buy-ratio collapse to 0.469 on the +10% pop, absent from the 7/02 top-100 DP tape, rev −30%, no forward catalyst) · SPY NA (macro note: dovish backdrop cuts against fresh shorts) · IBIT NA (record $4.5B June BTC-ETF outflows contradict the long).
- **Debate-disconfirmation cuts (bear ≥ bull):** HOOD (0.55/0.55 tie — gamma-churn decomposition), AAPL (0.55/0.65 — two independent lanes bearish at the highs; fresh short-dated put opening), MRNA (0.55/0.85 — concurrence with VETO), IBIT (0.55-binned/0.85 — collar decomposition). SPY hedge cleared (0.65/0.55-binned; true bear 0.35).
- **Breadth cross-check (advisory):** 70.97% S&P green on 07-02 — no divergence; no size impact.
- **Adverse-flow exits (prior group `conviction_week_2026-W26`):** **AMAT vol-long: thesis realised** (IV rank 100, P/C 1.72) — harvest zone, flag take-profit. **NOW long: soft exit** (bearish flow, 0.72× volume, IV rank 90 makes adds expensive). **TSLA short: adverse drift** (+$51.6B cap against the short; flow still bearish — monitor, don't add). QQQ short and SMH short on-thesis (SMH crowding rising; adds expensive at IV rank 94).
- **Concentration:** none in the sized book (the sized book is one hedge). The real concentration risk is thematic — everything bearish this week (semicap crowding, index put clusters, C19 Tier-1 puts on ADI/AMAT/KLAC) is one correlated "July event window" trade. Treat all of it as a single hedge budget.
- **Hedge sleeve:** the SPY Jul-17 ~740/720 put vertical **is** the sleeve (≤0.5% NAV premium). Do not add single-name/SMH shorts for alpha (MU/WDC 0.721 = one bet; protection already re-rated at IV rank 91–100; shorts are hedges, not alpha — 2026-06-27). No VIX ladder (weekend decay + contango make the vertical better carry).

**Tool/data caveats logged for the next `/calibration-audit`:** (1) SPY's +1 "cum-flow aligned" is a window-selection artifact — 180d pull shows a 1.3% net skew on $159B two-way flow that the tool itself labels MIXED (rubric frozen; record only). (2) `historical pc-ratio-zscore` has no `--date` path — trajectories must be reconstructed from `historical trend` PCR series (document as canonical method). (3) `oi decrease-with-volume` needs a DTE>3 filter to avoid expiry-mechanics false capitulation reads. (4) `historical oi-trend` `consecutive_build_days` ceilings at `--days` for liquid names (Gate-1 saturation). (5) iv-percentile-zscore ran on `dates_used=57` (<120) — all percentile quotes provisional. (6) KINKED classifications landing on monthly-OPEX expiries are wing-contamination artifacts (extends P1.3). (7) `insights institutional-accumulation` 10-day window unreachable (parquet retention). (8) fz enrichment returned market_cap/index only this session (selector miss on SI/analyst fields).

## 8. High-Conviction Cross-Ref

**No HIGH or MEDIUM tier names this week.** Per the empty-book protocol, the top-5 by raw score are documented at full audit depth (all were run through 2b/2c/2d):

**HOOD (LONG, raw 4, LOW → watch_only).** Components: +3 oi-trend BUILDING full week (accumulation-hunter, `uw historical oi-trend`) · +1 sector-leader conditional fully satisfied (sector-rotation, persistence 1.0 + cum_flow_30d +$100.7M aligned). Win-rate NA(substrate). Fundamentals CONFIRM. Debate {bull 0.55, bear 0.55} → gate fired on the tie; bear's decomposition (direction-mixed OI straddling spot; Jan-28 P70 block) beats the bull's "mechanically independent OI" framing. Gates: 8 no-op, debate −1, rubric_regime capped-half (non-binding). Watchlisted. Promotion trigger: clean bullish OTM-call OI skew + ≥3 consecutive ACCUMULATION days.

**AAPL (LONG, raw 3, LOW → watch_only, hard-no for sizing).** Components: +3 oi-trend · +1 conjunction halved (C11: 30d flow sign-opposes) · −1 flow_conflict_lite. Fundamentals CAUTION (−1). Debate {0.55, 0.65} (−1): the two genuinely independent lanes — insider Form-4s (−50.5 MSPR) and 30d premium (−$136.5M) — flipped bearish in the same window at all-time highs; the 90d +$337M "confirmation" mechanically contains the pre-flip regime. Fresh 7/02 unusual-volume was short-dated put-side opening. Watchlisted for the shelf ($283.78) — not for entry.

**MRNA (LONG, raw 3, VETO).** The week's marquee catch. $400M of genuine non-closing-cross mega DP buys (buy_ratio 1.000, institutional tier confirmed) — and the conviction-matrix classified the print day itself COVERED_CALL ("capping upside"); the +10% breakout day showed buy-ratio 0.469/MIXED with MRNA absent from the top-100 DP tape; 5-day net premium −$2.9M across the exact print window. Squeeze-labeled +66%/30d run, rev −30% YoY, no forward catalyst, earnings 7/30. Debate {0.55 nominal (bull self-flagged ~0.35–0.40), 0.85}. Not persisted.

**SPY (SHORT hedge, raw 3, LOW → starter, hedge budget only).** Components: +2 multileg repeat (P708→P707/710/714 rolls, Jul-17) · +1 cum-flow aligned (with the 180d MIXED-label audit caveat above). Debate cleared it {0.65, 0.55-binned (true 0.35)} — the bear conceded the cross-asset 7/17 cluster. Advisory class read: bearish_flow 0.529 (n=138) vs SPY-short bench 0.391 = +13.8pp — a rare positive-excess short class, quoted advisory-only against the 0-for-4 index-short desk record.

**IBIT (LONG, raw 1, DROP → skip).** +1 cum-flow only; the debate's strike-level decomposition (put walls 25–35 ≈ dollar-matched vs call walls 40–60; Jun-27 premium $607.8K C / $619.4K P) resolved the "accretion" as a collar. Class WR 0.478 / excess −0.080 = beta. Debate {0.55-binned (true 0.38), 0.85}.

**Expectancy lens (advisory, C31):** no HIGH/MED calls exist post-2026-06-12 freeze to compute a live per-tier expectancy line; the latest `/calibration-audit` (2026-06-27) tier table stands — HIGH realized 0.143 (inverted, 3rd consecutive), long edge UPTREND-only, short book negative-edge. That table *is* the reason this week's board refuses to size: the system is behaving as calibrated.

Embedded rubric (for audit):

```
Weekly conviction score (rubric_version 2026-06-12, FROZEN) = Σ:
  +3  uw historical oi-trend BUILDING full week (--days ≥ 5)
  +3  accumulation conjunction (3+ aligned + block-stratified institutional) — full only if cum_flow_30d
      sign-aligned AND |cum_flow_30d| ≥ $50M; else halved to +1
  +1  conviction-matrix DIRECTIONAL_LONG conf>70 — only when dominant class == leap_directional
  +2  position-rolls institutional LEAP roll (per-covered-date)
  +1  cum-premium-flow net directional accretion — intent-screened (no C28 flag; no dividend-capture)
  +1  MECHANIZED DEX flip or vanna squeeze (verified sign change; flip-day |net_dex| ≥ 0.25× 10-session median)
  +1  sector-leader conditional (persistence ≥ 0.6 AND cum_flow_30d aligned AND ≥ $50M)
  +1  earnings-scout BUY/SELL VOL next 2wk (term-skew aligned for full size)
  +2  multileg directional structure repeated ≥2 days
  +1  vol-surface KINKED/BACKWARDATION worsening WoW + iv-percentile extreme + VRP-aligned
  +1  opex-pin-strategist top-5 (OPEX week only — N/A this week)
  -2  crowded long w/ rising pc-z trajectory (VRP positive only — could not fire this week, VRP negative)
  -3  flow_conflict (30d cum-flow clearly opposite dominant class; > union-median magnitude)
  -1  flow_conflict_lite (MIXED 30d read) — mutually exclusive with flow_conflict
  [TIER GATES, 2d — not score components]: correlation cluster −1 tier; regime conflict −1 tier
  Tiers: ≥9 HIGH (full) / 7–8 MEDIUM (half) / 3–6 LOW (starter/watch) / ≤2 drop
  Win-rate ladder: ≥0.70 ×1.0 · 0.50–0.70 ×0.5 · <0.50 watch-only · null → starter · NA(substrate) → cap half
  Guards: n<10 → 0.69 cap · market-excess ≤0 → half, ≤−0.10 → starter · C4 non-opening flow → half
  P0.6: OUT-OF-REGIME — all conviction sizes capped at half until ≥30 post-2026-06-12 resolved calls re-validate
```

`flow_conflict` applied: PLTR (−3), MU (−3), MSTR (−3). `flow_conflict_lite`: AAPL, MRNA, KRE (−1 each). Union-median |cum_flow_30d| = $174.25M.

## 9. Setups for Next Week

- **Next-session GEX advisory (SPY/QQQ only — NO_GO_NO_EDGE backtest: pooled walls-as-magnet 24.6% vs 50%, n=114 — walls repel; dealer context only).** SPY: FULLY_NEGATIVE (−$821M), ZGL null/unreliable, call wall 750, put wall 740, and the largest single print −$527M sitting AT the money at 745 — the ATM zone is the amplification epicenter. Regime is only 2 sessions old. QQQ: FULLY_NEGATIVE (−$704M), thin call wall 730, put wall 700, −$168M ATM at 713 — flipped regime twice in-week, the least stable prior. Both books carry 3-day-weekend charm/vanna decay and gap risk; EOD book refreshes after Monday's open; ETF-not-index. Structure bias both: favor debit/defined-risk over premium selling into Monday's open.
- **Next-session 0DTE premium-selling setup (validated stack; advisory, 0 points):** verdict **GO_PREMIUM_SELL_INTRADAY** both indices, but VIX 16.15 = **LOW state → size 0.5×, weakest tercile**. SPY: iron condor wings ≈ ±1.26%, enter at/after open once the gap resolves, never carry overnight — backtest mean PnL **+0.32% gross / +0.22% net** of underlying-spot notional per day (n=57, win 94.7% gross — win-rate is NOT the promotion metric). QQQ: wings ≈ ±1.93%, **+0.40% gross / +0.30% net** (n=57). LOW-VIX tercile expectancy is the thinnest (SPY 0.127 gross vs 0.10 assumed cost — marginal). **Unsampled-tail caveat: no vol shock in the validation sample; the short-vol left tail is unpriced. Monday follows a 3-day weekend — stand aside if the open gaps beyond the wings.**
- **Dealer swing setups (flip-context, not trades):** PLTR long flip (mechanized, clean, GEX accelerating +214M) and MU short flip (mechanized, marginal, GEX regime break) both scored −2 after flow_conflict — the tape must confirm before either is actionable. Re-verify Monday: PLTR needs 30d cum-flow to turn/neutralize; MU short needs the +$474M bullish 30d flow to roll off. AMAT/INTC positive DEX decaying fast toward flips (semicap cluster) — watch for confirmed sign changes. IBIT DEX decaying toward a positive flip — the one crypto watch item.
- **Pin vs trend:** not OPEX week (7/17 is T+10). Fused event window 7/14–17 argues *trend/vol expansion risk* over pinning; re-run the pin map next week when opex-pin-strategist spawns.
- **Actionable (in order):** (1) **SPY Jul-17 ~740/720 put vertical, starter, hedge budget ≤0.5% NAV** — the week's only sized line. (2) **Harvest AMAT vol-long** from last week's book (IV rank 100 — thesis realised). (3) Earnings SELL VOL lane, all half-size caps: ABT 7/16 (best), banks bloc 7/14–15 (one position), CTAS; ASML half/calendar; NFLX defined-risk only. (4) KRE Aug call ladder is the one bullish structure worth stalking into bank earnings — needs a second day of institutional confirmation.
- **LOW-tier names to track for daily confirmation:** HOOD (promotion trigger above), AAPL (shelf watch $283.78/$308.63), WMT (late-week $305M non-CC flip — needs 2+ more ACCUMULATION days), VOYA (insurance RS), KLAC (two-sided whale interest into 7/30).
- **C19 single-leg persistence (advisory):** 11 Tier-1 opening/floor puts this week, zero name-level repeats; sector-level cluster in semicap (ADI+AMAT 6/29, KLAC 7/02) corroborates the crack. Notables: MSFT 470P $4.1M (7/17), GS 1060P (7/24), FSLR 230P. Several deep-ITM (|Δ|>0.9) — treat those as possible synthetic/arb prints. 06-30 printed zero scored signals. OOS scoreboard continues accruing toward the C19 graduation gate.
- **Deep-dive hand-off:** skipped — no-edge week (no post-gate HIGH-tier names; protocol says skip).

## 10. Watch-only — single signal, no confluence

Journaling only, NOT for entry: **INTC** short (sweep 4/4 clean $855M; multileg tape is financing-flagged) · **DRAM** short (sweep 3/4, memory-basket proxy) · **WULF** short (multileg 2-day, front-backwardated) · **IWM** short (multileg 3-day ladder — strongest structure of the week; hedge-cluster member, absorbed into the SPY sleeve thesis) · **HYG** short (credit ladder, same cluster) · **VOYA** long (sector + fz RS) · **CAT** short (XLI-confirmed de-risk candidate) · **WMT** long (late-week accumulation flip, 2/4 days were distribution) · **AMAT** short (contrarian +2.6σ informed-flow continuation; C19 put) · **KLAC** watch (Sept whale calls vs C19 put — two-sided) · **STX** divergence (−23% price vs bullish flow — the semicap outlier) · **TSM** conflicted (sweep bearish vs funnel bullish; earnings lane says calendar/wait) · **SNDK** conflicted (sweep dip-buying vs everything else; post-move, no forward signal) · **MSTR** long (sweep-inversion bullish but −3 flow_conflict — tape opposes) · **KRE** long (one-day $48M call ladder — stalk for a repeat) · **NKE** (LEAP near-miss; bearish chain flow).

---

*Generated 2026-07-03 by /weekly-analysis (11-agent fleet: 10 Phase-1 + quant/fundamentals/debate×5/risk Phase-2). Rubric 2026-06-12 (frozen). Envelope: `analyses/weekly/2026-W27/decision.json`. Watchlist group `conviction_week_2026-W27` = HOOD, AAPL, SPY.*
