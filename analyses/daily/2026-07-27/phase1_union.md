# Phase 1 candidate union — 2026-07-27

10 Phase 1 agents ran (opex-pin-strategist not spawned — third Friday was 2026-07-17, 10 days past).

## ⚠ READ FIRST: `analyses/daily/2026-07-27/DATA_CORRECTION.md`
`scripts/market_data.py` returned non-deterministic pct-change columns. The Step 0 context handed to agents carried **MU −9.09% (actually −2.25%)**, **INTC −8.54% (actually −0.70%)**, **XLK −2.33% (actually −0.90%)**. Authoritative moves below are from `uw historical trend` close-to-close. Where an agent's *rationale* leaned on a bad number it is marked ⚠ and downgraded.

## Corrected tape (authoritative, `uw historical trend`)
SPY +0.02% · QQQ −0.31% · IWM +0.60% · RSP +0.75% · VIX 18.67 · breadth 65.2% green (328/175)
Down: SNDK −11.02%, LITE −6.69%, AMKR −6.54%, ASML −5.80%, AMD −5.17%, NVDA −4.99%, LRCX −4.46%, STX −4.07%, COHR −3.92%, DELL −2.42%, SMH −2.25%, MU −2.25%, SOXX −2.05%, XLE −2.11%, XLU −1.32%, XLK −0.90%, INTC −0.70%, TSLA −1.22% (−16.33% 5d), AMZN −0.31%
Up: MSTR +7.61%, LW +7.12%, PLTR +7.00%, NOW +6.86%, COIN +5.81%, GM +5.32%, DBX +4.62%, GLOB +4.28%, ORCL +4.27%, BSX +2.85%, TCOM +2.59%, GOOGL +2.13%, MSFT +1.94%, COST +1.77%, XLP +1.46%, XLY +1.31%, XLC +1.28%, AAPL +1.17%, XLF +1.01%, JPM +0.85%

---

## AGENTS RETURNING EMPTY BOARDS (3 of 10)

**`accumulation-hunter` — ZERO names cleared.** Headline: **the 20:00:00Z–20:15:27Z closing-cross artifact ate the entire mega-tier signal** on an ordinary non-quarter-end session. MU, PLTR, NOW, GM, JPM, ASML all showed mega `buy_ratio` that collapsed or reversed once those prints were stripped. Specific rejections:
- MU: mega buy_ratio 0.602 → ~0.23 (sell-dominated) after stripping 2 trades at 20:07:47Z that were 81% of mega buy volume. Real-session premarket crosses at `trade_vs_mid` −21.45 / −13.95 / −19.13 = aggressive sells into a stale NBBO. `institutional-accumulation` NEUTRAL (1.02). oi-trend BUILDING but top contracts are DTE-4 **puts**.
- SNDK: `institutional-accumulation` 0.87 (sell-leaning); mega buy_ratio 0.153.
- ASML: labelled ACCUMULATION (1.63) but **100% of the mega tier is one trade at 20:07:03Z** ($171.3M). Only other mega print is a real-session sell.
- PLTR: mega buy_ratio 0.93 but all 4 trades 20:00:06–20:00:34Z. `institutional-accumulation` NEUTRAL 1.49.
- NOW, GM: same closing-cross pattern; GM flips to 0.81 sell-leaning when stripped.
- **GOOGL: `institutional-accumulation` = DISTRIBUTION (0.59) on 4,348 trades**, mega buy_ratio 0.163 — NOT closing-cross dependent. Genuine bearish caution.
- **AAPL: DISTRIBUTION (0.60) on 9,440 trades**, mega buy_ratio 0.094. Genuine bearish caution.
- JPM: surfaced as watch-only, explicitly NOT flagged — 47% of buy volume is closing-cross, `distribution_flag` present (call OI closing 320/350/360), reads as FOMC-week positioning in a rate-sensitive name.
- `insider_cluster_present`: **null** for all — the `fz` insider store is empty market-wide ("No insider data in the local store yet"), lane unavailable.

**`contrarian-scanner` — ZERO names cleared.** No ticker anywhere reached a ±2σ P/C z-score. Highest reading on the tape was TSLA +1.578 (still NORMAL). Also: **`uw historical pc-ratio-zscore` has no `--date` flag** in the installed build, so no "rising z" trajectory claim is possible today — the −2 rubric line requires a multi-date path and cannot be evidenced. MSTR/ORCL "bullish flow" is a 30-day dip-buy pattern (−20.4% / −34.9% over 30d), not blow-off euphoria. INTC's heaviest OI-closing is **long calls capitulating** (bearish confirmation, not a bottom).

**`leap-positioning-radar` — ZERO names cleared 6-of-9.** No fresh, ask-side, meaningfully-sized DTE>180 call open anywhere in the 61-name funnel. Only long-dated OI that moved was **puts**: INTC 2027-06-17 P85 (+13,503, DTE 325), ORCL 2027-12-17 P100 (+3,999, ask-side). Every semis name and mega-cap leader reads `cumulative-premium-flow` **MIXED** with net ~0.1–0.6% of gross — the opposite of slow accretion. Conviction-matrix: INTC = **COVERED_CALL 14.5%**, ORCL = **DISTRIBUTION 13.5%**, AMKR = **DIRECTIONAL_SHORT 27.1%**. Confirms C47: `consecutive_build_days` returned 10/10 for nearly every name = zero discrimination.

---

## POSITIVE FLAGS BY AGENT

### `dealer-positioning-strategist` — 2 mechanized DEX flips qualify
VIX dated series (Yahoo ^VIX): 07-21 17.05 → 07-22 16.64 → 07-23 18.70 → 07-24 18.58 → 07-27 18.67. **VIX is choppy-to-rising, not falling → every vanna-squeeze candidate is killed; zero vanna flags today.**
- **NVDA — SHORT, QUALIFIES.** `dex_flip.py` verbatim: *"NVDA net_dex 2026-07-24 +3,162,134,515 -> 2026-07-27 -3,635,988,005; prior 10 sessions all positive; |flip| 3,635,988,005 vs floor 1,363,060,481 (0.25x trailing-10 median 5,452,241,924)"*. `magnitude_ratio` 2.67, `sign_changes_in_window` **1**, `whipsaw_warning` **false**. GEX regime flipped POSITIVE→NEGATIVE the same day. Cleanest flip on the board.
- **PLTR — LONG, QUALIFIES.** *"PLTR net_dex 2026-07-24 -480,058,776 -> 2026-07-27 +947,286,825; prior 3 sessions (07-22 −178,327,379, 07-23 −328,543,917, 07-24 −480,058,776) all negative; |flip| 947,286,825 vs floor 265,499,262.5"*. `magnitude_ratio` 3.57, `sign_changes_in_window` **2**, `whipsaw_warning` false. GEX flipped positive same day.
- **Do NOT re-count:** MU, SNDK, INTC each flipped on **2026-07-24**; 07-27 is a continuation (`prior_run_length=0`), not a new flip. ASML tested and **fails on whipsaw** (4 sign changes / 11 sessions).
- TSLA: SHORT bias on a persistent negative DEX **level** (never flipped sign all week) + currently-negative GEX. Explicitly **not** a mechanized flip.
- ⚠ Known artifact re-confirmed: ZGL-grid corruption on SPY (ZGL 360.62 vs spot 750.13), QQQ (352.82 vs 706.7), IWM (~150–196 vs ~293–296), INTC (24.3 vs 91.67) — roughly half spot. Discard those regime labels.

### `multileg-strategist` — 3 structures qualify for the +2 (term-structure-anchored)
- **SMH — BEARISH, `qualifies_for_plus2: TRUE`.** 7/31 532.5/527.5 put vertical, 76,400 lots each leg, same second (19:13:09Z), $11.3M net debit on $141M gross, max gain $26.9M (2.38:1). **`multi_day_repeat_count` = 2** (7/24 identical strikes converted ~98% into OI: 61,199 vol → 60,286 OI). Term anchor: hygiene-verified KINKED @ 2026-08-07; the structure's own 7/31 tenor is 90.2% IV on 12,661 contracts vs 65.0% at 7 DTE — the trader picked the first expiry after FOMC+PCE and used a vertical to strip the event vol while keeping direction. SMH GEX FULLY_NEGATIVE (total_gex −$318M). **Honest weakness: both legs `no_side`; aggressor unobservable, sign inferred from the surrounding one-directional bearish book.** Confidence MEDIUM.
- **WOLF — BEARISH, `qualifies_for_plus2: TRUE`.** **The cleanest aggressor evidence on the tape** — every leg has an explicit side across multiple trades. 9/18 broken-wing put ladder: BUY 30P 42,509 @ask, BUY 25P 22,501 @ask, BUY 22.5P 40,005 @ask, BUY 20P 18,003 @ask, SELL 17.5P 50,112 @bid, plus SELL 2027 65C 21,251 @bid. ~$58M net debit, net long ~72,900 puts ≈ −5.8M shares (−$131M notional vs $138M ADV). Term anchor: hygiene KINKED @ 8/28 (149.6%) — they bought the **post-kink** 9/18 tenor at 131.7%, spanning the catalyst without paying for it. WOLF is the #1 bearish net-premium name (−$69.9M), +3.07% today but **−18.99% over 5d**. `repeat_count` **1**. Risk cap NOT fully defined (short 2027 65C sleeve uncapped). Competing read that could not be ruled out: conv-arb / hard-to-borrow synthetic short — argued against by the 65C sale monetising the recovery tail. Confidence MEDIUM-HIGH direction / MEDIUM overall.
- **INTC — BULLISH, `qualifies_for_plus2: TRUE`.** **Solves the $193M mystery ticket:** the $193.0M and $65.5M `no_side` prints are two legs of one package, both at **19:24:01Z**. BUY 70C 2026-11-20 65,200 @$29.60 (δ0.798) / SELL 97.5C 2026-09-18 70,000 @$9.35 (δ0.496) = **$127.5M net debit diagonal, +1.73M shares delta, vega ≈ −255/pt (flat)**. Legs verified analytically: at S=92.125 the 70C reprices to $29.54 vs $29.60 printed and δ 0.7976 vs 0.7976; the 97.5C to $9.42 vs $9.35, δ 0.4958 vs 0.4958 — **not** the un-split-adjusted strike artifact. Term anchor: **the only name whose BACKWARDATION label survived hygiene unflipped**, no kink → not an event play; sells richer front (86.3%) buys cheaper back (83.5%), but 2.8 vol points against $159M delta means the thesis is **delta, not vol**. ⚠ **Narrative correction: the agent framed this as "a bid for the semis washout" — INTC fell only 0.70% today. The structure stands; the knife-catching characterisation does not.** Contradictions named by the agent: both legs `no_side`; INTC's only single-leg whale signal is **bearish** (1/15/27 170P at ask, deep-ITM synthetic short); INTC net premium −$13.7M; a **live financing desk in the name** (7/31 deep-ITM 1-wide call pairs at near-identical sizes = boxes/conversions) raising the prior this is balance-sheet — but a box nets ~zero delta and this carries +1.73M shares, so it is a genuine risk position. Confidence MEDIUM.
- **Rejected:** IWM (rolling hedge overlay — highest repeat count 4, but strikes roll each session, two-way sides on the same contract, only 13% OI conversion); SPY 9/18 425/525/625 put fly (immaculate 1:2:1 but `side=mid` on 9 trades, no corroborating OI, body at SPY −29% where a fly is a terrible hedge → dealer/skew inventory); NVDA 7/31 215C/222.5C ($4.3M, 4DTE, 9.4% OTM, 7/24 OI shows bid-side = overwriting).
- **NEW ARTIFACT CLASS (4th):** **>$700M of SPX "premium" today is synthetic financing, not conviction** — 7000/8000 call-ask + put-bid pairs at identical size and the same second (10/16 2,500×2 @17:34:21; 12/18 1,750×2 @16:33:39; 10/16 1,000×2 @18:04:05; 11/20 1,000×2 @14:00:23). Jelly rolls / boxes, ~zero directional content. Any lane reading `top_premium_trades` naively books this as institutional conviction.
- Also: SMH 7/31 deep-OTM put builds (425P/385P/390P/325P, 23–41% OTM at 4 DTE) are financing/wing mechanics, not signal; and the SMH 530P prints $8.15 vs the 527.5P's $8.48 — a **put-monotonicity violation**; don't build on the 530 leg (the 527.5/532.5 pair is internally consistent).

### `sector-rotation-strategist` — rotation call `growth→value`, medium confidence
Trap 1 confirmed firing: **8 of 11 sectors read `persistence_score` 1.0 INFLOW simultaneously** = near-zero discrimination, and **Technology reads 1.0 INFLOW with +$367M net_flow on a day XLK fell**. Rejected as a sector call; decomposed into software(+) vs semis(−).
Conditional **+1 gate (persistence ≥0.6 ∧ cum_flow_30d aligned ∧ |cum_flow_30d| ≥$50M)** — names that FIRE:
- **TSLA** (bearish): persistence 0.6 PASS, cum_flow_30d **−$629,546,735** PASS, magnitude PASS → **FIRES**
- **AMZN** (bearish): −$186,199,912 → **FIRES**
- **AMD** (bearish): −$225,844,347 → **FIRES**
- **INTC** (bearish): −$836,153,067 → **FIRES**
Names that FAIL: JPM (+$47,989,672 — **misses leg C by $2M**), BAC, RF, WAL, LLY (+$22.9M), BSX (+$16.8M), QGEN (+$8.0M), NOW (+$26.3M), and PLTR/MSFT/ORCL/GOOGL all **fail leg B** (30d cum-flow net *negative*: PLTR −$203,873,113, MSFT −$540,713,062, ORCL −$251,802,739, GOOGL −$3,743,256) — today's software pop runs against a negative 30-day book. NVDA fails leg B (+$22,171,520 positive, misaligned with a short thesis). LRCX fails leg B (+$159,220,917).
ETF tape (advisory): **SMH — `gics_agreement: DISAGREE`**, sweeps dominated by near-dated 7/31 puts (~$192M combined at 532.5/527.5/530), blocks show creation/redemption pattern, price-confirmed bearish. **XLE — largest outflow (−$29.6M), clean 5/5 bearish**, GICS Energy nominally INFLOW → second Trap-1 casualty. IGV #1 inflow but its biggest single sweep is a **Dec-2026 $95 put ($9.3M) > $95 call ($6.7M)** = downside hedge.

### `sweep-tracker` — NO positively-flagged names
Resolves the price-vs-flow divergences as **unwind, not dip-buying**:
- **SNDK**: the "+$58.1M bullish" headline is a mirage — the three largest tickets ($49.0M, $33.8M, $19.3M) are deep-ITM long-dated **puts sold at the bid** (closing protection at a profit, books as bullish premium, conveys nothing). The one genuinely fresh ticket is **$38.6M buying an OTM put at the ask** — bearish.
- **MU**: 5 of 7 top tickets bid-side (closing); only 30% of sampled premium ask-side. ⚠ strikes 2110/1710/1810/1300 against a $900 stock = the known un-split-adjusted grid artifact; side composition still unambiguous.
- **ASML**: 28% ask-side, mostly call/put overwrite (income), one real $7.5M ask-side call buy.
- **DELL**: the only genuine buying — ask-side call buys + put sale (bullish risk-reversal) — but $2–4M tickets, **0/5 persistence**, single-day.
- **PLTR**: only **1 of 5** sessions in the persistence top list and **that single day reads bearish**; today's sample 76% bid/sell-side. **Directly contradicts a sweep-backed rip** — the +7.00% is retail/0DTE-driven.
- **MSTR**: 91% ask-side but the ask-side flow is mostly **puts** — buying protection into the +7.61%, not chasing.
- **ORCL**: same-expiry 7/31 put+call pairing = **FOMC-week strangle / event hedge**, not directional.
- **TSLA**: genuine repeated ask-side put buying across expiries (12/18 560P $20.3M, 12/18 570P $17.2M, 7/31 400P $17.0M), 83% ask-side ex-0DTE, **5/5 persistence**, opening not closing — but 90d cum_flow is **MIXED** (bullish $59.97B vs bearish $59.94B, net +$33.6M) so the mega-cap hedge-flow filter will not certify clean directional persistence. Bearish **watch**.
- INTC: $193M/$65.5M `no_side` prints referred to multileg (resolved — see above).

### `earnings-scout` — 1 positive flag
- **PLTR — BUY VOL** (the only positive). Earnings **2026-08-03 PM (7 DTE)**. Hygiene: `raw_shape` BACKWARDATION → **`shape` KINKED, `base_shape` CONTANGO, flipped=true**. `front_end_ratio` **0.946** (flat — no front panic to fade). Kink **DTE 11 / 2026-08-07 / 9.1% prominence** = the correct first expiry after the print, and **by 8/3 both FOMC and PCE/GDP are resolved history** → `kink_attribution: EARNINGS`, the only macro-decontaminated kink in the scan. Back-month skew 1.01 COMPLACENT (event tail NOT priced) → favours buying vol. **`implied_move_pct` 4.52%.** dte4 tenor 66.6% IV vs dte11 89.2%; RV20 48.6 / RV60 59.1. Structure: long 8/07 straddle (130) or 122.5/140 strangle. Agent rates **moderate, not high** — forward event premium looks appropriately priced, not obviously cheap.
- **ALL OTHERS SKIP.** STX (7/28), BSX (7/29), LRCX (7/29), MSFT (7/29) → **explicit MACRO_FOMC_PCE contamination**, front_end_ratio 1.5–1.94 is the Fed, not the print. AAPL/AMZN (7/30) → cleanest-*looking* kinks (contango base + spike at the correct post-print expiry) but the print lands the **same day as Core PCE + Q2 GDP** → un-splittable, AMBIGUOUS. ARM/COIN/ABBV → kink not at the earnings tenor. AMD → real elevation but prominence test fails, tool's kink is 10 days past the print. SNDK → hygiene shape **FLAT**, the 11.53% implied move is a sector-wide re-rating not an event premium. NBIS → smooth backwardation, no kink. **ENTG → `NO_NEAR_TENOR`** (nearest surviving tenor 25 DTE > 21 ceiling) — front end unmeasurable, NOT calm.
- **DATA GAP:** `uw insights analyst-vs-flow` returned **zero `analyst_recommendation` fields across all 13 tickers** — only the `options_flow` half populated. Analyst-vs-flow disagreement is **UNASSESSABLE**, not "none". Worth escalating upstream.

### `vol-surface-scout` — 2 positive flags (both ⚠ downgraded, see below)
Hygiene: **23 pulled, 14 flipped raw→hygiene** (MU, SNDK, AMD, STX, COHR, ENTG, SOXL, SMH, AMKR, DELL, ARM, PLTR, MSTR, WOLF). Raw label was BACKWARDATION on **21 of 23** — reconfirms the near-mechanical-default finding. `base_shape` flipped on 6; MU/AMD/PLTR are **CONTANGO base with a kink on top**, which the single-label tool cannot express. `min_contracts=15` (NOT audit-frozen). **`NO_NEAR_TENOR`: ENTG, AMKR** — front unmeasurable, not FLAT.
- ⚠⚠ **SYSTEMIC SUBSTRATE FINDING: every `iv-percentile-zscore` read this run carries `dates_used: 73`** — well under the ≥120-day first-class threshold, identical n across all 23 tickers. **All percentile/z reads are PROVISIONAL.** Escalate to the data-layer owner.
- **MU raw `iv_rank` 79.9 vs Goyal-Saretto percentile 42.47 (NORMAL)** — a 37-point divergence. Raw rank was being driven by a single-day spike. ⚠ **And that spike was smaller than the agent believed (−2.25%, not −9.09%).** Both facts point the same way: **MU's "elevated IV" is false.** ARM shows the same in miniature (86.7 raw vs 68.49 GS).
- **MU — BUY VOL flag ⚠ DOWNGRADED.** Rationale was "realised has already outrun implied after today's −9% print." The print was −2.25%. VRP −0.126 is a tool output that survives, but the agent's own GS read (42nd percentile) contradicts the premium thesis. **Fails the 2-agent gate regardless.**
- **SNDK — BUY VOL flag STANDS** (−11.02% is correct). VRP −0.081, GS percentile 90.41 HIGH_IV, hygiene shape **FLAT** despite 8/5 earnings 9 days out → event premium underpriced. `implied_move_pct` 11.53%.
- **ARM — WATCH/investigate, not a trade rec.** Aug-21 tenor kink at **54.2% prominence** (5,472 contracts vs 262/474 neighbours) sits well past its own 7/29 earnings → looks like a discrete positioning print. Referred to multileg / iv-outliers.
- **NO calendar-spread candidate qualifies.** The bucket requires evidence the front-end panic is *resolving*; a single EOD snapshot three sessions before FOMC cannot show that. Every BACKWARDATION name >1.10 has a catalyst inside its horizon → **HOLD, not a calendar bucket, until post-PCE 7/30 EOD.**
- IV outliers are all 0DTE 2026-07-27 expiry = mechanical tail of today's action, not whale mispricings.

### `gamma-flip-tracker` — §2 advisory only (0 rubric points)
Both **SPY and QQQ FULLY_NEGATIVE**, `zero_gamma_level` **null / `zgl_reliable: false`** on both, regime **HELD 3 straight sessions** (7/23, 7/24, 7/27) — not a fresh flip.
- SPY: spot 738.91, `total_gex` **−$1,589,298,789**. No reliable call wall; first positive strike 748 (+$44.9M), largest positive cluster 760 (+$56.7M, 2.9% above). Put wall 735 (−$153.4M). Largest negative strike is **ATM at 739/740 (−$381.7M combined) — a gravity trough, not support**. Top strikes: 740 (−$266.3M), 735 (−$153.4M), 730 (−$149.2M).
- QQQ: spot 681.85, `total_gex` **−$904,798,396**. Positive prints negligible everywhere (<$5.1M). Put wall 680 (−$151.6M, ~ATM); troughs 690 (−$71.9M), 700 (−$55.6M) = round-number OI, not support.
- **Structure bias: short-gamma ⇒ debit verticals / long straddles. Do NOT run iron flies or condors — there is no gamma cushion to sell against.** QQQ's negative VRP independently reinforces this.

---

## CONFLUENCE GATE (≥2 distinct Phase 1 agents flagging positively)

### PASS — 4 names
| Ticker | Agent 1 | Agent 2 | Direction |
|---|---|---|---|
| **PLTR** | dealer-positioning (mechanized DEX flip LONG, mag 3.57) | earnings-scout (BUY VOL, clean earnings kink, IM 4.52%) | LONG / long-vol |
| **SMH** | multileg (+2 bearish 7/31 put vertical, repeat 2, OI-confirmed) | sector-rotation (ETF tape, `gics_agreement: DISAGREE`, ~$192M bearish 7/31 put urgency, price-confirmed) | SHORT |
| **INTC** | multileg (+2 **BULLISH** diagonal, $127.5M debit, +1.73M shares δ) | sector-rotation (+1 conditional, **BEARISH**, cum_flow_30d −$836.2M) | ⚠ **DIRECTIONAL CONFLICT** |
| **TSLA** | sector-rotation (+1 conditional bearish, cum_flow_30d −$629.5M) | dealer-positioning (SHORT bias — persistent negative DEX **level**, explicitly NOT a mechanized flip) | SHORT |

### FAIL — single signal only (→ §8 watch-only)
- **NVDA** — dealer-positioning only. *The cleanest mechanized DEX flip on the board (mag 2.67, 1 sign change, whipsaw false, GEX confirmed same day) and it still fails the gate.* vol-surface explicitly did NOT flag it; sector-rotation fails leg B (+$22.2M, misaligned); multileg rejected its 7/31 calls as overwriting.
- **WOLF** — multileg only. *The cleanest aggressor evidence on the tape and it fails the gate.* vol-surface: CAUTION/no-trade (distressed, possible restructuring). Step-0 `confluence_bearish` score 5 is **funnel-seed only, 0 points, not a second opinion** (2026-06-12 P0.2).
- **MU** — vol-surface only, and ⚠ downgraded by the data correction.
- **SNDK** — vol-surface only.
- **AMZN, AMD** — sector-rotation only.
- **GOOGL, AAPL** — accumulation-hunter DISTRIBUTION caution only.
- **ARM** — vol-surface watch only.
- **JPM** — accumulation-hunter explicitly declined to flag; sector-rotation missed leg C by $2M.
- **DELL** — sweep-tracker mild positive, single-day, 0/5 persistence.
- CNC, TCOM, GLOB, RF, DBX, FAF — leap-radar noted consistent small bullish 90d/30d flow but all fail Gate 1 or are noise-scale (<$1.5M net).

---

## Cross-cutting artifacts registered this run
1. **Closing-cross 20:00:00Z–20:15:27Z** — contaminated mega-tier DP on MU/PLTR/NOW/GM/JPM/ASML. Recurring (2026-07-02 lesson) and now confirmed on a non-quarter-end day.
2. **Un-split-adjusted / mangled strike grid** — MU (2110/1710/1810/1300 vs $900 spot), ASML (1670–1850).
3. **Event-hedge shapes** — ORCL 7/31 put+call same-expiry pairing.
4. **NEW: SPX box / jelly-roll financing** — >$700M of `top_premium_trades` "premium" is boxes with ~zero directional content.
5. **ZGL-grid corruption** — SPY/QQQ/IWM/INTC ZGL ≈ half spot.
6. **`iv-percentile-zscore` n=73 everywhere** — all percentile reads provisional.
7. **`analyst-vs-flow` returns no `analyst_recommendation`** — disagreement unassessable across 13 tickers.
8. **`pc-ratio-zscore` has no `--date` flag** — the −2 rubric line's "rising z" requirement is unevidenceable in the current build.
9. **`market_data.py` non-deterministic pct columns** — see DATA_CORRECTION.md.
10. **`fz screen` ticker corruption** — leading char doubled (RRTX→RTX). Breadth endpoint unaffected.
11. **`fz` insider store empty** — `insider_cluster_present` is null fleet-wide, not false.
12. **SMH put-monotonicity violation** — 530P $8.15 < 527.5P $8.48.
