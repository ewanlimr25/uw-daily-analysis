# Phase 1 Candidate Union — 2026-07-30

## Confluence gate result (Step 3): 5 names cleared ≥2 distinct positive agent flags

| Ticker | Flagging agents (positive) | Direction agreement |
|---|---|---|
| **MU** | dealer-positioning-strategist, sector-rotation-strategist | agree (long) |
| **MSFT** | multileg-strategist, vol-surface-scout | agree (own back-end / bullish continuation) |
| **AMD** | earnings-scout, vol-surface-scout | agree (BUY VOL) |
| **PLTR** | earnings-scout, vol-surface-scout | **CONFLICT — SELL VOL vs BUY VOL** |
| **SPY** | multileg-strategist, vol-surface-scout | agree (own downside / own vol) — index hedge, not alpha |

---

## Per-name detail for scoring

### MU — close $874.66, +18.36% 1d / −11.67% 5d, ADV $42.5B, IV rank 77.7
- **dealer-positioning-strategist [POSITIVE]:** the ONLY qualifying mechanized DEX flip in the fleet today. `scripts/dex_flip.py` → `qualifies=TRUE, direction=long`. Evidence: `MU net_dex 2026-07-29 −16,580,609,504 → 2026-07-30 +1,443,844,185; prior 4 sessions (07-24 −4,056,285,870; 07-27 −5,412,686,232; 07-28 −9,116,138,017; 07-29 −16,580,609,504) all negative; |flip| 1,443,844,185 vs floor 1,296,381,556 (0.25× trailing-10 median 5,185,526,224)`. **magnitude_ratio 1.11× — barely clears.** `sign_changes_in_window=4`, **`whipsaw_warning=TRUE`**. Vanna LONG but net_vanna +928 = noise-level. front-end-iv-ratio **1.362 BACKWARDATION (extreme panic, still building)**. swing_bias LONG, **LOW CONVICTION**.
- **sector-rotation-strategist [POSITIVE]:** Technology single-name leader clearing **ALL THREE** gates — persistence_score 1.0 (≥0.6 ✓), `cum_premium_flow_30d` **+$673.4M** bullish-aligned ✓, |cum_flow| ≥ $50M ✓. One of only two Tech names to pass (with SNDK). Note: the genuine multi-week Tech accumulation is a narrow **memory/storage sub-theme**, not broad tech.
- **accumulation-hunter [EXPLICIT REJECT]:** mega-tier DP buy_ratio 0.784 looks bullish BUT `institutional-accumulation` = **NEUTRAL**, price −16.16% 30d. Called "textbook short-cover-into-a-squeeze."
- **sweep-tracker [NEUTRAL]:** 5/5 session persistence, $5.28B cumulative premium (largest single-name book on the tape) but `dominant_direction: mixed` → no directional thesis.
- **contrarian-scanner [ABORTED]:** negative-QQQ-VRP abort rule. z-score −1.166 NORMAL (no extreme). Price-vs-flow divergence exists (price −16.2% 30d, flow +$145M) but is explanatory/lagging, not forward.
- **vol-surface-scout [CONTEXT]:** **largest kink in the set (25.6% prominence at 8/7 dte8)**. Key divergence: raw IV rank 77.7 ("elevated") vs robust percentile **39.5th** (z=0.13, median) — MU's BASE vol is NOT stretched, so a 25.6%-prominent kink on a normal baseline is "the cleanest true dislocation in the batch." BUT no confirmed forward catalyst → treat as NFP/macro, not idiosyncratic. Implied move ~20% overstates a discrete event on a continuously-high-vol name. skew NORMAL 1.022.
- No C28 distribution_flag evaluated. No earnings in the 14d window.

### MSFT — close $451.10, +15.51% 1d / +18.22% 5d, ADV $14.1B, IV rank 53.8. **Reported 7/29 (BEAT).**
- **multileg-strategist [POSITIVE, HIGHEST CONVICTION of the whole fleet]:** diagonal call roll up-and-out. SELL Aug-21 C390 (19,500 @ $62.60 = **$122.07M**, Δ0.939, IV 0.407) / BUY Nov-20 C420 (19,500 @ $54.35 = **$105.98M**, Δ0.707, IV 0.340). Identical size AND identical timestamp `14:47:25Z`, `no_side` both legs = one negotiated two-leg cross. **Net credit $16.09M.** Delta −25%, vega +0.73/contract (≈ +$1.42M per vol point). `uw oi oi-by-strike` confirms standing base: strike 390 call_oi 63,302; strike 420 call_oi 84,678, both call_heavy. **Aligned fresh single-leg ask-side demand across 5 tenors:** Aug07 C470 5.0:1 · Aug21 C450 1.9:1 · Aug21 C500 2.5:1 · Sep04 C465 11.1:1 · Sep18 C470 8.8:1. Term-structure anchor: BACKWARDATION / base BACKWARDATION, **not flipped**, front_end_ratio **1.243**, **NO kink at any tenor** → play_type = **directional bullish continuation with favourable vol carry** (sells rich front 0.407, buys cheap back 0.340). Explicitly NOT an event play. OPENING+UNWIND: Aug leg unwinds, Nov leg opens; net posture still long, less delta, more vega/duration, $16M off the table. Risk cap: long Nov20 C420 fully funded by the Aug leg. **Direction is INFERRED, not observed (`no_side` both legs)** — sell-Aug/buy-Nov is the only economically coherent read.
- **vol-surface-scout [POSITIVE]:** "cleanest calendar-candidate rationale in the batch." BACKWARDATION, no kink, front_end_ratio **1.243**, skew TAIL_HEDGING 1.11, robust pctile 61.8 (z −0.12; raw rank 53.8). Elevated 6dte IV 43.5% vs back-month 33–35% one day after the print = **post-earnings vol-decay lag, NOT forward risk**. Short front / long back. Implied 6-day range ~5.6% (to 2026-08-05). Caveat: needs T+1 confirmation the ratio is decaying, not re-inflating.
- **sector-rotation-strategist [EXPLICIT FAIL]:** `cum_premium_flow_30d` = **−$34.0M, MIXED** → fails leader gate (a) direction and (c) magnitude. "Today's print is an earnings pop, not multi-week accumulation, despite driving the entire headline number."
- **dealer-positioning-strategist [DISQUALIFIED]:** DEX POSITIVE and building hard (+1.03B→+2.84B→+3.60B→+2.94B→**+20.5B**), `sign_changes=0`, **no flip → 0 rubric points (level, not flip)**. vanna_state SHORT (net_vanna −50,766, largest call-heavy read in the set) — if IV keeps falling, dealers short calls must CUT long-stock hedges = selling pressure, arguing against self-reinforcing follow-through. ZGL whipsaws 4 flips in 10 sessions. **Disqualified on DEX/vanna disagreement.** front-end-iv-ratio 1.217 BACKWARDATION (vol-crush candidate, not directional edge).
- **sweep-tracker [DEMOTED]:** mega-cap gate — `cum_flow_30d` MIXED, not directional.
- **contrarian-scanner:** z 0.151 NORMAL, price/flow aligned, nothing to fade.

### AMD — close $485.39, +13.00% 1d / −10.06% 5d, ADV $14.3B, IV rank 78.1. **Earnings 2026-08-04 postmarket (5 days).**
- **earnings-scout [POSITIVE — BUY VOL, modest conviction]:** kink at dte6 (2026-08-05, first tenor after the 8/4 print) is a **NEAR-MISS at 4.0% prominence vs the 5.0% threshold** — genuine but sub-threshold; the market has NOT strongly conceded a hump. Back-month skew −0.0052 COMPLACENT/flat, no tail hedging. **Implied move 3.48%** — modest vs AMD's historical earnings range. front_end_ratio 1.255 (panicked). Key point: AMD's +13% today is index/beta-driven (semis melt-up), so **the idiosyncratic earnings catalyst has NOT been used up by today's move**. Flow +$62.15M bullish but likely contaminated by the squeeze. Structure: long straddle/strangle dte6 (8/5) ~$485.
- **vol-surface-scout [POSITIVE — override the label]:** module reports plain BACKWARDATION (no kink), but that is an artifact of the prominence test — AMD's 4dte (8/3, 80.1% IV) expires BEFORE the 8/4 print, while 6dte (8/5, 110.3%) and 8dte (8/7, 106.1%) both straddle it = a genuine **two-tenor elevated plateau, not a single spike**, which the local-max-vs-both-neighbours test under-detects. "**A real, event-anchored dislocation the algorithm missed.**" Robust pctile 76.3 / z0.73. Skew COMPLACENT 1.015 → argues AGAINST a directional risk-reversal. Caveat: implied move 3.48% is small relative to >100% front IV → **the straddle is already efficiently priced; buying here is expensive vol, not cheap vol.**
- **sweep-tracker [CONTRADICTION FLAG]:** 5/5 persistence, $1.72B cumulative sweep premium, tool tags **bearish** (matches −10.06% 5d) — but today's actual tape is a balanced $560-strike Jan-2027 straddle-like block plus **call-dominated fresh OI** (495C/437.5C/485C) and a 1DTE 500C chase-buy ($6.5M). "The bearish persistence describes the drawdown, not today's tape — today looks like short-cover/hedge-unwind, not a fresh short press." OI-confirmed opening (BUILDING 5/5, +565K net OI 5d).
- **sector-rotation-strategist [FAIL]:** `cum_premium_flow_30d` = **−$163.7M** → FAILS leader gate direction.
- **contrarian-scanner [ABORTED]:** QQQ-complex negative-VRP abort.

### PLTR — close $122.26, −0.60% 1d / −0.90% 5d, ADV $4.6B, IV rank 79.1. **Earnings 2026-08-03 postmarket (4 days).**
- **earnings-scout [POSITIVE — SELL VOL, half size]:** genuine kink at dte8 (2026-08-07), the correct post-earnings tenor (Mon 8/3 PM print realizes before the Fri 8/7 expiry), **18.7% prominence on 9,688 contracts** — well above the floor. **BUT back-month skew (45dte) = 0.0134 NORMAL/flat** → front-only kink = explicit half-size case. Flow **bearish −$10.86M** (matches step0 top_bearish). front_end_ratio 1.34 (panicked). Implied move 2.25%. Structure: iron fly at 8/7, ~$122 strike, half size.
- **vol-surface-scout [POSITIVE — BUY VOL]:** same kink, same 18.7% prominence, same 8/7 tenor. Robust pctile **97.4 / z1.82** (raw 79.1) — genuinely extreme. skew NORMAL 1.023. Implied move 2.25%, ATM IV ~102%. "BUY VOL — earnings straddle/strangle into 8/7, size to the 2.25% move; kink is genuine."
- **>>> DIRECTIONAL CONFLICT: the two vol lanes agree exactly on the substrate (kink date, prominence, implied move) and disagree on the SIGN of the trade. Do NOT award both vol lines as if they were independent confirmation. <<<**
- Note: vol-surface flags that PLTR has **no listed weekly between now and 8/7**, so the 8/7 expiry simultaneously spans PLTR's own earnings AND **NFP (2026-08-07, HIGH impact)** — the "kink" is a compound earnings+macro read, not a clean single-event premium.

### SPY — close $741.69, +1.68% 1d / +0.48% 5d. Index hedge, NOT a single-name alpha call.
- **multileg-strategist [POSITIVE, bearish]:** Aug-21 P706/P695 bear put spread. BUY Aug21 P706 (ask 25,788 / bid 289 = **89.2:1**, $7.02M) / SELL Aug21 P695 (bid 18,458 / ask 612, $4.04M). Net debit ~$3.0M, $11 wide. `repeat_count`: P706=3, P702=3, P695=2; ticker 5/5 days. Term-structure: raw BACKWARDATION → **hygiene FLIPPED to KINKED at 2026-08-07 dte8, prominence 8.8%**, front_end_ratio 0.945 → **event play anchored to NFP**. OI-confirmed opening (Aug07 P700 3.18×, P720 1.81×, P730 1.68×). Risk cap clean: max loss = debit.
- **vol-surface-scout [POSITIVE, own-vol]:** SPY IV30d 14.4% at the **34th percentile (z −0.49)** while constituents that moved 8–27% today carry IV30d 45–216% at the 55th–100th percentile. SPY skew_ratio **1.482 TAIL_HEDGING** — HIGHER than QQQ's 1.285 despite much lower absolute vol. "Hedgers are buying cheap SPY tail protection while chasing the QQQ/semis melt-up." → **textbook long-dispersion setup (short index vol / own single-name vol or correlation)**. Front ratio 0.945, kink 8/7 8.8% prominence = the NFP read.
- **dealer-positioning-strategist:** DEX NEGATIVE, trajectory −38.4B→−34.5B→−26.1B→−75.2B(7/29 FOMC trough)→−1.8B(7/30), magnitude collapsed ~97% but **sign never changed → qualifies=false**. vanna LONG (+70,251, put-heavy) but **vanna_squeeze_flag=FALSE — VIX gate fails**. swing_bias NEUTRAL/FLAT.
- **sweep-tracker [DEMOTED]:** hedge-flow signature, cum_flow_30d MIXED (net −$1.34B on $60B gross).
- **contrarian-scanner:** z 0.383 NORMAL, no extreme.

---

## FAILED CONFLUENCE GATE — single-signal, §8 watch-only (NOT for entry)

| Ticker | Sole flagging agent | Note |
|---|---|---|
| SNDK | sector-rotation (Tech leader, cum_flow_30d **+$993.0M**, passes all 3 gates) | earnings 8/5; earnings-scout SKIP (no kink, COMPLACENT back skew −0.0442, implied move 7.83% on an already-extreme realized-vol regime); vol-surface disqualified from calendar (event-pending) |
| NBIS | sweep-tracker (4/5 bullish persistence, OI-confirmed opening, put-SELLING + call-buying into the drawdown — "best risk/reward name on this list") | dealer-positioning NEUTRAL + whipsaw TRUE; earnings-scout SKIP (FLAT front ratio 1.049, earnings 8/12 collides with CPI); contrarian ABORTED |
| BE | sweep-tracker (4/5 bullish persistence, clean ask-side call buying Sep–Jan, +369K net OI) | 5d only −4.68% vs peers −15/−27% → today's +26.5% looks like payoff of pre-existing positioning |
| DRAM | multileg (2028-01-21 LEAP call-spread ladder, ~$11.6M debit vs ~$55.8M max payoff; **today's 4 legs = 127,163 contracts vs prior standing call OI of 89,949 at that expiry** — decisively OPENING; traded at IV 0.863–0.877, cheapest vol on the surface) | **COVERAGE GAP: leap-positioning-radar never saw DRAM** — `uw oi biggest-increases --min-dte 180` returned only 20 rows market-wide and DRAM was not among them |
| IWM | multileg (Aug-21 put-spread collar, **repeat_count=4, the strongest campaign in the book**, 5/5 days; BUY P278 at 22.5:1, SELL C298 at 0.034 = collar; kink at 8/7 = NFP; "a bet against the median stock, not against the index headline") | bearish/hedge |
| AVGO | accumulation-hunter (3 signals, institutional-tier CONFIRMED mega 0.604 / block 0.598, ACCUMULATION ratio 1.51, oi-trend 5/5, mid-session 19:24:53Z print NOT closing-cross, DP support **$387.84 / $387.61 / $370.32**) | **conjunction FAILS**: cum_flow_30d +$21.8M **MIXED** (<$50M) → +3 halves to +1. **distribution_flag present=true** (call-side OI closing). insider_cluster false; dp_block_to_float_ratio null |
| MA | accumulation-hunter (3 signals, block-tier 0.812 = strongest bullish block ratio in scan, ACCUMULATION 1.71, oi-trend 5/5, clean tape, DP support **$577.35 / $563.32**, distribution_flag FALSE) | **conjunction FAILS**: cum_flow_30d +$14.0M bullish-aligned but **<$50M** → +1. Already +17.11% 30d = not "quiet". sector-rotation explicitly declined to claim it as a leader |
| XOM | earnings-scout (SELL VOL **full size** — one of only two names clearing the full-size bar; back-month skew +0.056 TAIL_HEDGING, skew_ratio 1.199) | earnings 7/31 premarket (1 day). Implied move 1.94%, low absolute premium ceiling |
| UBER | earnings-scout (SELL VOL half; kink 19.7% prominence at 8/7) | back-month skew **−0.1107 COMPLACENT** = actively complacent, the "riskier short" case |
| NET | earnings-scout (SELL VOL half; kink 11.7% at 8/7) | back skew unmeasurable; PCR 2.36 put-skewed vs net-bullish premium = divergence caution |
| DDOG | earnings-scout (CALENDAR: sell 8/7 / buy 8/28 ~$268) | FEIR **1.512 — most extreme in the set**, IV rank 95.5, no confirmed kink, back skew unmeasurable |
| NVDA | multileg (bear call spread — **explicitly DISAGREES with the bullish funnel**: SELL Aug07 C200/C205, BUY C207.5/C210 + SELL Aug21 C200 $27.02M + BUY Sep18 P180 $13.82M; the +$21.19M bullish net premium is inflated by 0/1DTE gross turnover, Jul31 C195/197.5/200 all bid-side heavy = selling/closing) | NVDA +2.65% vs SMH +6.88%, −6.57% 5d. vol-surface calls it weak (front ratio 0.918 undercuts the KINKED label) |
| AMZN | vol-surface (robust pctile **100 / z=2.279 — most extreme in the batch**; front ratio **1.715 — highest in the set**; 1dte IV 171.4%) | **REPORTS AFTER TODAY'S CLOSE — confirmed. Not actionable in a post-market report; the event is resolving now.** multileg SKIPPED it (net-bearish flow vs all-call multileg = hedge) |
| AAPL | vol-surface (robust pctile **97.4 / z1.57 HIGH_IV**, front ratio 1.427; kink at 9/18 is mechanical quad-witch, not earnings) | **ALSO REPORTS AFTER TODAY'S CLOSE — confirmed.** multileg: Jul31 C332.5/C335 straddle at spot 333.43 |
| SNOW | vol-surface (best "panic resolving" candidate — front ratio **0.917, already sub-1**) | accumulation-hunter **REJECTED** (mega tier 100% sell — the $20.1M alert print IS a sell) |
| SHOP | vol-surface (BUY VOL, low conviction — prominence 5.9% barely clears) | accumulation-hunter **REJECTED**: `institutional-accumulation` returns explicit **DISTRIBUTION** |
| SKHY | multileg (Aug07 P125 → Aug28 P110 diagonal put roll; protection maintained, reset lower+longer after +17.5%) | **NOT defined-risk** — the Aug07 P100 leg sits ~1:2 vs P125; if the 2× P100 is short, downside re-opens below ~$75 |
| IGV | multileg (Aug21/Nov20 P90 put calendar, 97.6% size match, ~$7.2M debit) — **DEMOTED to hedge, not alpha** | IGV Jan-27 P/C 6.423 with 257,954 puts = 25.24% of total OI → standing systematic software-hedge book; this is program maintenance. Still notable: software downside being extended in duration while XLK ripped +5.50% and IGV managed only +1.02% |
| RH / CVNA / LCID | sector-rotation (Consumer Cyclical persistent 5/5-day OUTFLOW, above-median magnitude) | RH bearish/bullish premium ~10:1, −5.64% today; CVNA PCR 1.53, −7.36%; LCID PCR 1.25 |
| CORT | funnel-only dual-lane (uw signal-confluence bullish score 5 + fz RS new-high, +27.29% 1d / +22.41% 5d) | **no Phase 1 agent flagged it** |
| TRMB | contrarian (BEARISH_EXTREME z=**2.995**, PCR 12.1) but explicitly "**not a fade setup — crowd and smart money agree**"; reads as informed-flow short-continuation caution | vol-surface **DISQUALIFIED**: `NO_NEAR_TENOR` (nearest 22dte, 29 contracts) despite earnings in 6 days — chain has no weekly spanning its own event. Extreme PCR very likely a thin-book artifact |
| SOXX / SOXL / SMH | vol-surface BACKWARDATION context; sweep-tracker SOXL 3/5 borderline w/ contradiction flag | sector-rotation: **SMH DP blocks crossed BELOW mid (selling pressure)** + $26.8M Jan-28 500P → "corroborates that the semis pop is a short-cover bounce, not fresh accumulation" |

## EXPLICIT DROPS (rejected by ≥1 agent, no positive flags)
- **META** — rejected independently by **five** agents: accumulation-hunter (cum_flow −$21.8M MIXED, NEUTRAL detector, "bullish premium on a −7.95% miss day = put-selling/hedge-unwind"), dealer-positioning (DISQUALIFIED, DEX −$5.97B today vs put-heavy vanna = active disagreement), vol-surface (**skew COMPLACENT 0.963 after an 8% single-day drop — nobody is hedging; "don't buy this dip's vol"**), multileg (**deep-ITM put parity artifact CONFIRMED: 2028-01-21 P1020 @ $485.00 vs intrinsic $486.80 — trading BELOW parity**; this is the mechanical explanation for META's anomalous bullish net premium), sweep-tracker (hedge-flow, Aug-21 dated post-miss hedges).
- **LRCX** — accumulation-hunter REJECT: mega-tier buy_ratio **0.0** (4 trades, 100% SELL, $162M), price −20.43% 30d. The $100.7M watchlist "alert" print is a SELL. dealer-positioning: worst whipsaw in the set (7 sign changes/16 sessions).
- **INTC** — sweep-tracker contradiction flag (bearish 5/5 tag vs call-dominated fresh OI); leap-radar DISQUALIFIED (cum_flow_90d −$753M).
- **SPCX** — sweep-tracker ARTIFACT FLAG: $330 strike vs $112.25 spot (~194% OTM) at 1–8 DTE priced at nickels; spot flat (−0.31% 1d) despite $837M "bullish" sweep premium.
- **CSCO** — accumulation-hunter artifact exclusion: 76% of daily DP volume in one 20:05:06Z closing-cross print; cum_flow_30d −$0.76M contradicts the single-day ACCUMULATION read.
- **COHU** — vol-surface DISQUALIFIED `NO_NEAR_TENOR` (no listed expiry inside 22 DTE at all); raw IV rank 99.7 / robust z=2.845 is computed off a monthly-only thin book.
- **WOLF / TLT / PDD / INTC / VFC** — leap-radar, all disqualified. PDD is the instructive near-miss: 5/9 gates pass but `conviction-matrix` = **COVERED_CALL, confidence 17.5** ("dark pool buying + call selling — yield enhancement, capping upside") = absolute veto.

---

## CROSS-CUTTING FINDINGS FOR THE QUANT

1. **`uw historical oi-trend` BUILDING has ZERO discrimination again.** accumulation-hunter: BUILDING with 5/5 consecutive build days on **6 of 6** tickers checked. leap-radar: BUILDING with 9–10 consecutive build days on **5 of 5** checked. This reproduces the 2026-07-24 16-of-16 finding. **Do not treat the +1 oi-trend line as independent evidence today** — flag it in the audit trail wherever it fires.

2. **68% of single-leg whale prints (417/610) carry the CLOSING signature** (size/OI < 0.5). On a +3.3% QQQ melt-up, the dominant footprint is position CLOSING, not fresh opening conviction.

3. **Month-end closing-cross contamination is broad.** SPY mega-tier DP buy_ratio 0.036, QQQ 0.019 — both ~100% SELL in mega tier, driven by 4–5 prints all timestamped 20:00–20:25Z. Stale-NBBO crosses confirmed on AAPL (21:45:14Z, price $333.43 vs NBBO ask $309.73) and AMZN (21:07:00Z, $235.50 vs ask $252.80).

4. **The SPX/SPXW "signal" is a box/jelly-roll.** $1.20B = 55% of ALL multileg premium today: four legs, identical size 5,000, identical timestamp 18:40:45Z, deep-ITM, **positive theta (+0.12)** on the Sep P8000. Zero directional content. Anyone ranking multileg by raw premium gets this as their #1.

5. **`uw historical iv-percentile-zscore` returned `dates_used=76` on 0/23 tickers clearing the 120-day bar** — every percentile/z-score this run is PROVISIONAL.

6. **No vanna squeeze qualifies anywhere.** The dated VIX series (07-23 18.70 → 07-24 18.58 → 07-27 18.67 → 07-28 18.21 → 07-29 **20.66 FOMC spike** → 07-30 **17.09**) shows only ONE down session after a one-day spike. Fails the ≥3-session-falling gate for every ticker.

7. **`uw options-flow unusual-volume` is degenerate today** — entire top-20 is MSFT strikes with OI = 1 or 2, producing vol/OI of 1,711–3,893.

8. **`multileg_ratio > 1.0` is mathematically impossible but present**: NN Sep18 C30 = 2.892, C18 1.975; SKHY Dec18 C210 1.997; TLT Aug21 P82 1.600. None scored.

9. **`uw hot-chains multileg` default `--top-n 20` is unusable** — the top 20 is entirely VIX/SPXW/IWM/SPY/index. Every single-name structure found today sits below rank 20.

10. **SPY, QQQ and IWM all kink at exactly 2026-08-07 = NFP.** Index and breadth-sensitive vehicles are being hedged into the NFP→CPI window while two single names see genuine long-dated bullish structure (MSFT, DRAM). These are not the same trade.

11. **`uw historical pc-ratio-zscore` has NO `--date` flag** — current-day only, no historical path. **Every z-score this run is a LEVEL, not a trajectory.** The −2 "rising pc-ratio-zscore" rubric line is therefore UNSCOREABLE today for every ticker.

12. **`uw screener earnings-catalyst` coverage gap**: AMZN and AAPL both report after today's close (confirmed) yet neither appears in its 14-day earnings window, and `earnings_date` is `null` on every row it does return.
