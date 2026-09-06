# Weekly Market Intelligence — Week of 2026-07-27 (ISO 2026-W31)

## Executive Summary

- **Week regime + WoW Δ:** TRANSITIONAL **held** Monday to Friday with `trend` UPTREND at both ends, but the label conceals a V. SPY sold off 747.03 → 740.86 → **729.46** (07-29, FOMC decision day, below both SMAs, VIX 20.66) and then ripped ~+2.4% over two sessions to close **747.03**, back above its 20SMA (745.69) and 50SMA (744.99). The internals did not follow the price: `uw` flow breadth **deteriorated 35.2% → 34.1% bullish**, and Friday's +0.72% index print came with only **43.94%** of S&P members green and a **−0.24% median member**. This was a cap-weighted mega-cap earnings event, not a broadening. VRP is **FAIR/NEUTRAL** — SPY +0.0029, QQQ **−0.0323** — so there is no premium-selling edge at the index level, and the negative QQQ side forced contrarian-scanner to abort its entire fade book for the second consecutive week.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`.
- **Signal performance:** **4 of 6 resolved (hit rate 1/4 = 25%); 2 INCONCLUSIVE excluded; 6 total non-DROP calls in universe (6 envelope-anchored, 0 reconstructed)** — out of **44 total calls** across the week's five daily envelopes, of which 38 were DROP. See §0; the supplementary DROP-pile check is again the more informative read.
- **Top swing build for next week:** **None.** All four LOW-tier candidates floor to watch-only. The least-bad is **IWM short** — a genuine five-day institutional put-debit-spread program — but it carries no price confirmation, a single-tool thesis, and the standing index-ETF short penalty.
- **Top LEAP build:** **None.** Zero of 15 candidates cleared 6-of-9 gates. MU and SNDK cap at 5-of-9, both failing on the same pair (institutional-accumulation reads NEUTRAL; conviction-matrix confidence 0.6% / 2.7% against a >70 bar).
- **Biggest emerging risk:** **The scoring substrate, not a correlation cluster.** Three of the week's rubric inputs returned degenerate or contaminated values simultaneously — the +3 OI line saturated at its ceiling on *every* name checked, the panic gate lost its input entirely, and all six mechanized DEX flips fired on the same 0DTE-dominated Friday. The board's top two scores rest on a measurement with zero discrimination this week. Runner-up: **INTC**, last week's only sized call in 20 weeks, has flipped to adverse flow.

> **The 20th consecutive empty conviction board — and this week the empty board was, again, demonstrably the alpha.** The fleet's own daily calls were systematically wrong-way short into the V-reversal: AMZN short graded **−6.00×ATR**, BE −1.65, WDC −1.64, SMH −1.44. Nothing was sized. Nothing was lost.

---

## 0. Week in Review — Intra-Week Signal Performance

**Universe:** the union of `calls[]` across this week's five daily `decision.json` envelopes — the only hindsight-free record of what was actually committed. All five envelopes exist, so **nothing was reconstructed**. **44 total calls; 6 non-DROP.** Resolution runs from each call's own envelope date forward to 2026-07-31. Grade threshold is 0.5 × ATR(14) measured as-of the call date.

### Primary scorecard — non-DROP calls

| Ticker | Direction | Source | Move vs ATR | Flow/OI | Grade | Note |
|---|---|---|---|---|---|---|
| SNDK | long | envelope 07-28 | +10.83%, **+0.61×ATR** | cum-flow +$1.01B bullish, sustained | **WIN** | Sized `skip`. The one winner. |
| BE | short | envelope 07-28 | **+23.36%, −1.55×ATR** | flow flipped hard bullish | **LOSS** | Sized `watch_only`. The week's worst miss by a wide margin. |
| MU | long | envelope 07-30 | −5.90%, **−0.60×ATR** | 30d cum-flow +$466.9M bullish *against* a long that still lost | **LOSS** | Sized `skip`. |
| SPY | short | envelope 07-30 | +0.72%, **−0.66×ATR** | — | **LOSS** | Sized `watch_only`. |
| TSLA | short | envelope 07-28 | −1.23%, −0.23×ATR | — | INCONCLUSIVE | Below threshold. |
| CRWV | vol_long | envelope 07-31 | 0.00%, 0.00×ATR | — | INCONCLUSIVE | 0 forward sessions (called on week-end). |

**Headline: 4 of 6 resolved (hit rate 1/4 = 25%); 2 INCONCLUSIVE excluded; 6 total non-DROP in universe (6 envelope-anchored, 0 reconstructed); 44 total calls, 38 DROP.** A denominator of four carries little information — but **every one of these was `skip` or `watch_only`, so the realised book P&L is exactly zero.**

### Supplementary — DROP-pile discipline check (n=33 directional DROP calls, 13 resolved)

This is not part of the formal scorecard; it grades what the desk *declined* to trade, the way `/calibration-audit` does.

| Metric | Result |
|---|---|
| DROP hit rate | **3W / 10L = 23.1%** |
| Non-DROP hit rate | 1W / 3L = 25% |

The two piles are statistically indistinguishable at these sample sizes — but the *shape* of the DROP losses is the finding. **The fleet was persistently short into a V-bottom reversal**, and the four worst-graded calls of the week were all shorts that got run over:

| Ticker | Dir | Date | Move | ATR multiple |
|---|---|---|---|---|
| AMZN | short | 07-27 | **+17.37%** | **−6.00×ATR** |
| BE | short | 07-29 | **+25.69%** | −1.65×ATR |
| WDC | short | 07-28 | +17.55% | −1.64×ATR |
| SMH | short | 07-29 | +7.20% | −1.44×ATR |

An AMZN short at −6.00×ATR is the single most dangerous call the fleet has produced in months. It was scored raw-2 and dropped. **That is the system working.**

### Carried W30 positions

| Ticker | W30 call | Move to 07-31 | ATR | Grade |
|---|---|---|---|---|
| **INTC** | short, **starter — the only sized call in 20 weeks** | −2.30% | +0.28×ATR | INCONCLUSIVE (running slightly in-the-money) |
| TSLA | short, watch_only | −0.58% | +0.11×ATR | INCONCLUSIVE |
| **BE** | short, raw-7, **VETO'd** | **+11.31%** | −0.79×ATR | **LOSS — the veto was correct** |
| TSM | short, VETO'd | +0.21% | −0.05×ATR | INCONCLUSIVE |
| IBM | long, DROP | +4.42% | +0.62×ATR | WIN (declined) |

**BE deserves emphasis.** It scored **raw 7** last week — the highest score of that run — and was VETO'd. It then rose +11.31%, and rose a further +25.69% against a fresh 07-29 short. The veto stack saved the desk twice on the same name in eight days.

---

## 1. Regime & WoW Delta

`uw risk market-regime` returned **TRANSITIONAL — Mixed signals, reduce position size, wait for clarity** with `trend: UPTREND` on both Monday and Friday. The WoW label therefore *held*, but that is the least informative fact about the week.

> **⚠ Tool artifact, recorded for the audit.** `uw risk market-regime` returns an **identical `spy` sub-block for `--date 2026-07-27` and `--date 2026-07-31`** (747.03 / SMA20 745.69 / SMA50 744.99). The `spy` block does **not** respect `--date`. A WoW price delta must not be read off this tool. The true intra-week path was reconstructed from this week's own daily envelopes.

The real path: 747.03 (Mon) → 740.86 (Tue) → **729.46 (Wed, FOMC decision day, below both 20/50 SMA, VIX 20.66 +13.45% 1d, breadth 32.5%)** → 741.69 (Thu) → **747.03 (Fri, reclaimed both)**. VIX collapsed 20.66 → **15.99** across the final two sessions.

**Vol regime:** `uw historical vrp` — SPY **+0.0029** (IV30 13.08% vs realised 12.80%, FAIR); QQQ **−0.0323** (IV30 22.65% vs realised **25.88%**, i.e. index vol on the tech complex is *cheap* relative to what it actually delivered). Per the operating rule this tilts the week toward **premium-buying** and away from premium-selling fades — and it is why contrarian-scanner's abort clause fired.

**DTE volume share** (`{symbol: MARKET}`, market-wide overlay):

| Date | 0DTE | Weeklies | Monthlies | LEAPs | Hint |
|---|---|---|---|---|---|
| 07-27 | 16.8% | 5.3% | 12.0% | 2.8% | BALANCED |
| 07-29 | 19.5% | 8.5% | 14.8% | 3.0% | BALANCED |
| **07-31** | **48.2%** | 21.4% | 14.8% | **2.6%** | **RETAIL_DRIVEN** |

0DTE share nearly **tripled** Mon→Fri while LEAP share *fell*. Part of that is the Friday weekly-expiry mechanic, but 48.2% is extreme, it lands on the same session as the mega-cap earnings rip, and it is the single most consequential number in this report — it contaminates the DEX lane (§3), the term-structure lane (§5), and the panic gate (§7) simultaneously.

**Macro backdrop** (`scripts/fred_macro.py`): yield curve **normal** (10Y−2Y +47bp). Core CPI **2.81%** YoY, core PCE **3.29%** — the stickier gauge is the worse one, running ~130bp above target. Unemployment 4.2%, payrolls **+57k** (soft). 10Y **4.68%, +24bp over 30d** against fed funds 3.63% — the long end is repricing term premium, not growth. USD weakening. Net: a mildly stagflationary mix — soft labour, sticky core, rising long yields — a direct headwind to long-duration equity multiples.

**Forward event risk (next two weeks):** NFP **2026-08-07** (high) · CPI **2026-08-12** (high) · PPI **2026-08-13** (medium) · jobless claims 08-06 and 08-13 (low). **No August FOMC** — the July 28–29 meeting was Wednesday's trough, and the next is September 15–16 with an SEP. The window is data-driven, not Fed-driven.

**Implication for next week:** a tape that needs three stocks to make a new high, with breadth deteriorating underneath it, into a soft-labour/sticky-core data stack. That is a configuration for reduced size and defined risk, which is what the gate stack independently produced.

---

## 2. Sector Rotation

**Rotation regime call: `cyclical→defensive`, MEDIUM confidence** (downgraded from a technically-clean read).

> **⚠ Major tool finding — the Technology contradiction is resolved, and it corrects a standing project assumption.** `uw options-flow sector-flow-persistence`'s `by_day` values are **literally identical, to the dollar**, to `uw options-flow sector-flow`'s classified split for the same dates (Technology 07-27 = `$366,844,565` in both). They are **not two independent sources** — both compute `gross call$ − gross put$`, and `persistence` is merely the multi-day wrapper. The only properly **netted** source is `uw risk market-regime`'s `sector_rotation` block. On 07-31 Technology read **+$2.78B** from the gross pair and **−$187.7M** from market-regime. The $2.78B is two-way earnings turnover (MSFT/semis trading heavily in both directions around the prints); the −$187.7M is real net de-risking. **Never quote a sector direction without naming which source produced it.**

Because 07-30 and 07-31 are earnings-turnover artifacts (Technology +$2.47B/+$2.78B; Consumer Cyclical printing **+$1.84B on 07-31 alone** — that is AMZN, +15.32% that day — despite being labelled OUTFLOW on persistence), the durable read leans on 07-27→07-29.

| Sector | 07-27 | 07-28 | 07-29 | Durable shape | Persist. | ETF cross-confirm |
|---|---|---|---|---|---|---|
| Financial Services | +149.8M | +167.0M | +188.1M | Monotonic ↑, strongest | 1.0 | **DISAGREE** — XLF −$0.69M (MIXED), KRE −$3.3M (BEARISH); **zero bullish leaders** |
| Energy | +38.9M | +48.1M | +61.0M | Monotonic ↑ | 1.0 | **PARTIAL** — XOP +$5.4M agrees, XLE −$8.5M disagrees; signal is **E&P-specific** |
| Healthcare | +85.4M | +206.0M | +88.1M | Positive all 3 | 1.0 | **AGREE** — XLV +$1.6M, XBI +$3.2M. Cleanest defensive confirm |
| Consumer Defensive | +53.4M | +112.5M | +100.1M | Positive all 3 | 1.0 | **AGREE** — XLP +$1.2M |
| Comm. Services | +348.3M | +184.1M | +364.8M | Strongly positive | 0.8 | DISAGREE — XLC −$1.4M |
| Technology | +366.8M | +34.2M | +223.1M | Positive, modest vs spike | 1.0 | AGREE (mild) — XLK +$2.9M, IGV +$5.3M |
| **Consumer Cyclical** | −386.1M | −250.0M | −313.3M | **Persistently, deeply negative** | 0.8 | DISAGREE — XLY +$4.0M, but **AMZN-weight contaminated**; ex-AMZN the outflow is real |
| **Industrials** | −47.0M | +69.1M | −151.0M | Choppy, ending sharply negative | 0.8 | **AGREE** — XLI −$4.7M, best outflow confirm |
| Utilities | +15.0M | −12.0M | −23.6M | Flips negative | 0.6 | Agrees by trend-end — XLU −$1.3M |

**Why only MEDIUM confidence:** (a) Utilities, the third defensive leg, is trending *negative*, not confirming; (b) the strongest GICS number in the table — Financial Services — is flatly disconfirmed by both its ETFs and has **zero** bullish single-name leaders; (c) 0DTE share tripling to 48.2% forces a uniform downgrade on all rotation calls; (d) flow breadth *worsened* while price ripped.

**Named single-name leaders (all three legs: persistence ≥ 0.6 ∧ cum-flow aligned ∧ |cum-flow| ≥ $50M):**

| Ticker | Sector | Dir | cum_flow_30d | 3 legs | Note |
|---|---|---|---|---|---|
| **TSLA** | Consumer Cyclical | short | **−$634.9M** | ✅ | Cleanest, largest-magnitude claim in the set |
| **AMD** | Technology | short | −$125.4M | ✅ | |
| **AAPL** | Technology | short | −$90.4M | ✅ | |
| **MRVL** | Technology | long | +$115.0M | ✅ | Only Technology long clearing the bar |
| NVDA | Technology | long | −$64.8M | ❌ leg b | Flow contradicts the price strength |
| PLTR | Technology | long | −$160.0M | ❌ leg b | Same — do not chase |
| MU | Technology | short | **+$466.9M** | ❌ leg b | Flow is net *bullish* despite −10.6% wk = dip-accumulation, not a clean short |

**The real story is not GICS-level.** The dominant flow of the week — semis/AI-capex funding mega-cap platform earnings winners — is *intra*-Technology (and intra-Consumer-Cyclical for AMZN). It shows up as a bifurcation in the leader table, not as a sector rotation.

**ETF flow tape (advisory — 0 rubric points)**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| **XOP** | +$5.37M | BULLISH | $1–4M blocks, evenly split vs mid | thin 2027/28 LEAP call buying | **agree** (Energy, E&P-specific) | none |
| **IGV** | +$5.33M | BULLISH | one $10M print flagged NBBO artifact (bid=0), rest near-mid | 0DTE/near call buying 89/92 + LEAP put at 85 — mixed | **agree** (Tech/software) | none |
| **XLY** | +$4.01M | BULLISH | one $28.3M near-mid block (creation/redemption) | **LEAP PUT buy** $941K Dec-26 K115 — a hedge | **disagree** (AMZN-weight contamination) | TSLA/LCID, but *short* side |
| **GDX** | −$17.58M | BEARISH | $45.9M + $22.2M near-mid crosses | call buy *and* sell at same K79 = collar | **disagree** (concentrated thematic) | none |
| **XLE** | −$8.50M | BEARISH | $2–10M near mid, no dominant print | LEAP put $908K offset by Aug calls | **disagree** (majors vs E&P split) | none |
| **XLI** | −$4.71M | BEARISH | one **$162.1M** block *above* mid (+0.44) — creation/redemption, **not** accumulation | thin, $360K | **agree** (best outflow confirm) | SPCX; POWL is a bullish outlier risk |

Rank-only: XLK +$2.9M, XLV +$1.6M, ITB +$1.5M, XLP +$1.2M, TAN +$0.14M, XLB −$0.09M, XLRE −$0.05M, EWT −$0.32M, XLF −$0.69M, XLU −$1.27M, XLC −$1.45M, KRE −$3.32M. **SMH +$52.59M is the largest raw number in the universe but is labelled MIXED (non-persistent day-to-day) → appendix-only, disqualified from the rotation call.**

**Swing-book implication:** tactical and half-sized at best. Financial Services and broad Energy are **watch-only** (GICS says one thing, ETFs and screener say another). Healthcare/Consumer Defensive is real but has **no tradeable single-name leader** from this week's funnel — express via XLV/XLP or not at all.

---

## 3. Swing Book (1–6 weeks) — ranked by weekly conviction score

**The swing book is empty.** All four LOW-tier candidates floor to watch-only under the gate stack. They are documented here in full because the *evidence* is unusually good on two of them and the reasons for killing them are the useful output.

### 3a. Long swings (regime-aligned)

| Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure | Invalidation |
|---|---|---|---|---|---|---|---|
| **MRVL** | LOW | 5 | `null` NA(substrate) | **watch_only** | Only Tech long clearing all 3 sector-leader legs (+$115.0M 30d). Contrarian dip-buy in the complex that funded the rally. | — | **DP shelf $183.30** (62 trades, $235.0M, ~2.3% below close $187.56) |
| **SNDK** | LOW | 4 | `null` NA(substrate) | **watch_only** | Long vol into the 08-05 print. BACKWARDATION smooth 181/156/146/140%, front-end 1.30. **Delta-neutral.** | — | Not a level — fails if realised move by 08-05 < ~20% breakeven |

⚠ **MRVL carries a `distribution_flag`** — three institutional-size call closes on 07-31 ($1.53M 0DTE, $622K 0DTE, $281K LEAP) after the mega-tier DP buy ratio collapsed from 1.0/1.0/1.0 (Mon–Wed) to **0.0/0.0** (Thu/Fri). Advisory, 0 points, no size change — but it is why the +1 cum-flow line was withheld.

### 3b. Short / fade swings (defined risk only)

| Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure | Invalidation |
|---|---|---|---|---|---|---|---|
| **IWM** | LOW | 3 | `null` NA(substrate) | **watch_only** | The week's only true five-day institutional program. Aug-21 put debit spread ladder re-struck downward all week and **held through the +2.4% rip**. | Aug-21 put debit spread, ~4.6:1 | **DP shelf $292.68–293.98** (~0.5–1.0% above spot $291.20) |
| **SPY** | LOW | 3 | `null` NA(substrate) | **watch_only** | Aug-21 P750/P715 — the cleanest single print of the week (opposite-side legs, sizes matched to 0.2%). | Put debit spread, 3.3:1, $27.5M risk / $89.9M max | Holding above ~$747–748 invalidates; needs a close back below 50SMA $744.99 |

**Both are defined-risk debit spreads, not naked shorts.** Any future sizing must size the *structure*, not the delta.

**Dropped by the rubric (raw ≤ 2):** TSLA short (2) · AMD short (2) · AAPL short (1) · COIN short (0). Detail in §8.

---

## 4. LEAP Book (6–24 months)

**Empty.** Zero of 15 screened candidates cleared 6-of-9 gates.

| Ticker | Gates | Why it failed |
|---|---|---|
| **MU** | **5-of-9** | Passed: oi-trend (saturated), biggest-increases, cum-flow (+$466.9M/30d, +$257.4M/90d — **sharp fresh-thesis**, days 31–90 netted −$209.5M), DP largest, DP price-levels ($493.4M at $823.03, 140 trades). **Failed:** zero position-rolls; institutional-accumulation **NEUTRAL** (0.98–1.05); conviction-matrix MIXED at **0.6%**. |
| **SNDK** | **5-of-9** | Same failure pair. cum-flow +$1.01B/30d, +$2.60B/90d = **smooth thesis-extension**. But zero rolls, fresh LEAP OI **put-dominated**, conviction-matrix MIXED 2.7%, and **earnings 08-05 inside the window** — leap-radar explicitly recommends excluding until past the print (Augustin et al.: informed traders with a known near-dated catalyst express *short*-dated). |
| CRWV | ~3-of-9 | cum-flow thin vs book size; DP print essentially *at* mid (+0.09, not aggressive); matrix MIXED 3.7%. |
| INTC | Gate 4 hard-fail | cum-flow **−$914.7M/30d, −$753.2M/90d**, both bearish — despite a strong alt-path signal (100C DTE233/323, ask:bid 8:1) and 7/5-day persistence. |
| NVDA | Gate 4 hard-fail | −$64.8M/30d, −$258.1M/90d; matrix DIRECTIONAL_LONG but only **13.2%** confidence. |
| **WBD** | Gate 1 + 4; **merger-arb flagged** | Equity ACCUMULATION (DP buy/sell 2.44) + **bearish** options premium + `consecutive_build_days=1` + matrix DIRECTIONAL_LONG at 28.1% = the classic own-stock-plus-protective-puts deal hedge. Same class as the NUVL 2026-06-24 precedent. |
| BE, SPCX, CORZ, GME, CMCSA, NOK, AMD, ARM | Gate 4 | All bearish or reversing on 30d/90d cum-flow. **SPCX additionally IPO'd 2026-06-12** — only ~33 trading days of history, so its 30d/90d reads are structurally unreliable. |
| LBTYA | **C12 fail** | ADV $25.3M < $50M floor — dropped before any gate check. |

---

## 5. Volatility Surface — WoW Term Structure & Skew Evolution

> **⚠ Hygiene is load-bearing this week.** The raw `iv-term-structure` label flipped **7 of 22 names on 07-27 and 14 of 22 on 07-31** once `term_structure_hygiene.py` dropped the `dte_approx: 0` bucket and sub-15-contract tenors. 07-31 was an expiry Friday with 48.2% 0DTE share — exactly the condition that manufactures a fake backwardation flip. Every shape below is the **hygiene-corrected `base_shape`**, compared like-for-like.

### Genuine hygiene-confirmed builds

**ARM — the headline finding, and the cleanest vol structure of the week.** A genuine **KINKED** curve at the **2026-08-21** tenor on a BACKWARDATION base: **IV 173.7% on 5,517 contracts**, against neighbours 08-14 (96.7%) and 08-28 (88.8%) — that clears the liquidity floor by ~300×, so it is *not* a thin-tenor artifact. Kink prominence **grew 54.2% → 79.7%** across the week. **No earnings catalyst** (verified absent from the ≤14-day universe). Critically, the front-end ratio is **falling** (1.238 → 1.164) *while* the mid-curve hump grows — front-end panic is not building. Term skew 1.016 NORMAL → 0.998 COMPLACENT. **The raw label said BACKWARDATION on both days and completely hid this; hygiene is the only reason it surfaced.** Calendar candidate: sell 08-21 / buy 08-14 or 09-18 (both liquid at 796 and 1,513 contracts). Reads as OPEX positioning / gamma absorption, not event risk. *Single-agent finding — failed the confluence gate, so it is watch-only.*

**LCID** — KINKED at 28 DTE (08-28), prominence 22.0% on 118 contracts, kink IV 203.2%. Front-end ratio crushed **1.258 → 0.851** (CONTANGO) even as the hump grew. Skew TAIL_HEDGING both days (1.232 → 1.205). But the entire curve sits >100% IV (rv20 158.4%), so this is a spike inside an already-chaotic surface — much less clean than ARM. Secondary.

**Post-earnings unwinds, not fresh dislocations:** AMZN, MSFT, GOOGL all flipped base BACKWARDATION → CONTANGO — the genuine unwind of pre-earnings vol. Each picked up a *new* mild kink at the 08-21 monthly (prominence 6.5%), which is the market-wide OPEX concentration bucket, not idiosyncratic. **CRWV**'s new 14-DTE kink (08-14, 7.5%) *is* legitimate — its earnings are 2026-08-11 and 08-14 is the first weekly expiry closing after that print.

### Raw-label claims that hygiene overturned — this list is itself the finding

| Ticker | Raw said | Hygiene says | What actually happened |
|---|---|---|---|
| **AAPL** | BACKWARDATION both days (looks calm) | **base flipped BACKWARDATION → CONTANGO** | Real de-escalation the raw label completely missed. Front-end eased 1.215 → 1.181. |
| ALNY | FLAT → BACKWARDATION ("fresh backwardation!") | **BACKWARDATION unchanged** | 07-27's FLAT was an artifact of only 2 tenors surviving (129 and 32 contracts). Nothing changed. |
| PGY | FLAT → CONTANGO | **BACKWARDATION unchanged** | Same pattern — thin tenors (5, 6, 8 contracts). |
| CAKE | CONTANGO → FLAT | **INSUFFICIENT_DATA → BACKWARDATION** | 07-27 had **1** surviving tenor (70 contracts) — should never have been classified at all. |
| MU | BACKWARDATION unchanged | KINK at 08-07 **strengthened 19.2% → 26.9%** | The 08-07 kink is **NFP day** — a market-wide macro event, not a company catalyst. **Do not fade or calendar this**; it is correctly-priced macro risk. |

### Calendar-spread candidates

| Ticker | Front-end ratio WoW | base_shape | Catalyst | Verdict |
|---|---|---|---|---|
| **ARM** | 1.238 → 1.164 (falling) | BACKWARDATION, kink building 08-21 | **none found** | **Candidate** — sell 08-21 / buy 08-14+09-18 |
| BTDR | 2.982 → 1.097 (huge crush) | BACKWARDATION, no kink | none | Candidate, but thin book — verify liquidity before sizing |
| RDDT | 1.292 → 1.116 (falling) | BACKWARDATION unchanged | already reported | IV crushed *despite* a real realised-vol event — favours **owning** vol cheap, not a calendar |
| MU | flat (not falling) | KINKED, strengthening | **NFP 08-07** | **Disqualified** — persisting into a pending macro print |

### Disqualified

**EA — merger-arb pin, not a vol trade.** rv20 **3.8%** with term-structure IVs of 3.6–12.7% at every liquid tenor are *real*, not a data artifact: EA at $209.86 is pinned near a cash-deal price. `iv_percentile_zscore` = 0 (z −2.048), the lowest in the scan. **Do not surface as a BUY/SELL VOL candidate** — capped upside at the bid, same class as the NUVL precedent.

### Substrate defects recorded this week

- **`uw options-flow iv-outliers` was 100% contaminated** — 20 of 20 results on 07-31 sat in the `2026-07-31` 0DTE bucket. Zero usable single-contract outliers; not cited anywhere in this report.
- **`uw historical iv-percentile-zscore` returned `dates_used: 77` on every call**, below the 120-day floor. **Every percentile in this section is PROVISIONAL.**
- **`uw screener earnings-catalyst`'s `implied_move_perc` is broken** on at least PLTR (0.14% vs 14.7% term-structure-derived), SNDK (0.83% vs 25.1%), CRWV (0.68% vs 24.3%). Found independently by two agents. **The envelope's `implied_move` uses the derived value, not the raw field.**

---

## 6. Earnings — Recap & 2-Week Lookahead

### (a) Recap — this week's prints

> **Triage correction:** AMD, PLTR, SNDK, UCTT and POWL had **not** reported as of 07-31 (all report 08-03/04/05). Their double-digit weekly drops are **pre-earnings positioning and semis sympathy**, not post-print drift. MU printed the *prior* week. HOOD and ARM show no single-day earnings gap — sector drift, excluded.

| Ticker | Print → reaction | Pre-event thesis | IV rank before → after | Realised | Grade | Lesson |
|---|---|---|---|---|---|---|
| **AAPL** | 07-30 → **07-31 −7.35%** | 07-27 fleet: DROP, but **institutional DISTRIBUTION flag** (buy/sell 0.60, 91% sell at top DP tier, 9,440-trade sample, *not* closing-cross) 3 sessions ahead | 75.2 → 52.7 | −7.35% | **CONFIRMING** | Pre-print distribution-into-strength correctly anticipated the miss |
| **GOOGL** | 07-30 → **07-31 +6.73%** | 07-27 fleet: DROP, **same DISTRIBUTION signal, same tool, same day** (buy/sell 0.59, mega-tier 0.163) | 30.3 → 38.1 (*rose*) | +11.38% wk | **DISCONFIRMING** | **The week's sharpest calibration lesson — see below** |
| **AMZN** | 07-30 → **07-31 +15.32%** | 07-27 SHORT lean, never sized (fundamentals CAUTION + event gate) | 72.3 → 31.4 | +15.32% | DISCONFIRMING (unsized) | A thin 30d cum-flow short signal (1.5% of gross turnover) is not an earnings-direction read; the gates spared real capital |
| **MSFT** | **07-29** → **07-30 +15.51%** | 07-30 LONG lean via a **$228M negotiated diagonal call roll** (sell Aug-21 C390 / buy Nov-20 C420) | 88.5 → 43.3 | +21.75% wk | **CONFIRMING** | Institutional diagonal call-roll ahead of a beat is a repeatable structural tell — it never scored |
| **RDDT** | 07-30 → **07-31 −20.99%** | none | 69.0 → 28.3 | −16.63% wk | N/A | **STILL LIVE, not resolved** — term structure remains backwardated post-hygiene (1.116) with GEX FULLY_NEGATIVE |
| **ALNY** | 07-29 → **07-30 −28.31%** | none | 89.1 → 83.7 → 69.1 (**slow bleed**) | −24.38% wk | N/A | Biotech binaries crush IV far more slowly than mega-cap tech — distinct risk class |
| **COIN** | 07-30 → **07-31 −10.59%** | none | 72.7 → 48.9 (clean) | −7.60% wk | N/A | 3 consecutive misses, deepening; revenue *and* EPS negative YoY. Event **resolved** |
| **DXCM** | 07-30 → **07-31 +11.95%** | none | 44.7 → 19.5 | +16.65% wk | N/A | Textbook clean beat + full crush — good calibration reference |
| **BABA** | 07-30 → **07-31 +5.10%** | none | 56.3 → 67.8 → **59.4 (no crush)** | +9.02% wk | N/A | China ADRs don't crush cleanly even on a benign beat |
| **LCID** | 07-27 → **07-28 +21.54%**, then **07-31 −9.11%** | none | 50.2 → 61.3 → 50.0 | +17.14% wk | N/A | **Put premium spiked to $53.9M on 07-30** (vs ~$4M/day) — foreshadowed Friday's fade two days after the print |
| CAKE / AVTR | 07-28 → 07-29 +13.63% / +15.78% | none | both crushed cleanly | +19.71% / +20.45% wk | N/A | Clean small-cap beat+crush |
| PGY | 07-29 → +8.96%, +9.24% | none | 58.7 → 18.3 | +21.27% wk | N/A | Momentum continued 2 sessions post-beat despite the crush |

> **The AAPL/GOOGL pair is the most important calibration result of the week.** The *identical* advisory signal — institutional distribution into strength, same tool, same session (07-27) — preceded AAPL's −7.35% miss and GOOGL's +6.73% beat. **This line is not a standalone edge**, and it should be registered as such at the next `/calibration-audit`.

### (b) Lookahead — through ~2026-08-14

> **Structural finding: 9 of 15 candidates in the 08-03 cluster cannot be priced for the event.** They have **no listed options expiry between 0 and ~21 DTE** — the earnings premium is blended inside the first-listed monthly and cannot be isolated. Per the hygiene rule these return **SKIP, reason "unmeasurable"** — *not* a calm/FLAT read. Affected: **POWL** (ivr 88.5), **STRL** (97.2), **UCTT** (93.0), **AEIS** (87.0), **ICHR** (77.0), **FANG** (79.4), **CLX** (76.1), **TSN** (69.6), **TWST** (69.0). This is the RMBS class recurring across the majority of a single cluster.

| Ticker | Date | d | IVR | Term shape (hygiene) | front@7 | Skew | Play | Spans macro? | Disqualifiers |
|---|---|---|---|---|---|---|---|---|---|
| **AMD** | 08-04 | 4 | 78.9 | CONTANGO base; real liquid step dte3 72.6% → dte5 109.3% spanning the print (the "KINKED" label at 28dte is a 51–159-contract artifact) | 1.03 | **COMPLACENT** (0.011) | **BUY VOL** | **No** — dte5 (08-05) clears NFP | Flat back-month → don't oversize |
| **SNDK** | 08-05 | 5 | 75.7 | BACKWARDATION, smooth 181/156/146/140% | **1.30** | NORMAL (0.060, borderline) | **BUY VOL** (cautious) | **Yes** — dte7 = NFP day | Extreme front **and** flat back = double SELL-VOL disqualifier |
| **WMB** | 08-03 | 3 | 78.7 (pcr 9.02) | BACKWARDATION, smooth 40.3→32.0% | **1.26** | **TAIL_HEDGING** (1.123, stretched) | **CALENDAR** | **Yes** — dte7 = NFP; back leg spans CPI+PPI | Front too extreme to short outright |
| **ON** | 08-03 | 3 | 79.0 | BACKWARDATION, smooth 125→87% | **1.45** | NORMAL (0.048) | CALENDAR (low conviction) | **Yes** | Extreme front + only-NORMAL back = front-only-panic coin-flip |
| **VRTX** | 08-03 | 3 | 83.5 | Mechanical KINKED at 28dte is a **51-contract artifact** | 0.90 (contaminated) | NORMAL | **SKIP** | Yes | Both legs contaminated; biotech binary risk (cf. ALNY this week) |
| **PLTR** | 08-03 | 3 | 78.0 | BACKWARDATION, smooth | **1.46 — most extreme in the set** | **COMPLACENT 0.995 — most complacent in the set** | **NO PLAY / HEDGE FLAG** | **Yes** | **See below** |

> **⚠ PLTR is a live conflict.** It reports **Monday 08-03** carrying the **most extreme front-end panic (1.46) *and* the most complacent back-month (0.995)** in the entire lookahead — the textbook double SELL-VOL disqualifier — while simultaneously sitting in this week's bullish swing funnel. **Any PLTR long carries an uncompensated, un-hedged binary event in three days with essentially zero tail pricing.** It failed the confluence gate (1 positive agent vs 2 negative) and is not in the book, but the conflict is worth stating explicitly.

**Zero full-size SELL VOL calls were generated this week** — no name cleared both SELL-VOL conditions (extreme front *and* stretched back) simultaneously. That is consistent with the FAIR/negative VRP regime.

---

## 7. Risk & Correlation (week-candidate universe)

**Correlation clusters** (`uw risk portfolio-correlation` across the 8 scored names):

| Pair | Corr | Class | Action |
|---|---|---|---|
| **MRVL / SNDK** | **0.858** | Cluster | **−1 tier to SNDK** (lower raw: 4 < 5). MRVL kept. |
| MRVL / AMD | 0.909 | Cluster | AMD is DROP — noted only |
| SNDK / AMD | 0.868 | Cluster | AMD is DROP — noted only |
| SPY / TSLA | 0.748 | Cluster | TSLA is a carried W30 position — flagged for portfolio visibility |
| SPY / AMD | 0.676 | Soft watch | no penalty |
| MRVL / SPY | 0.639 | Soft watch | no penalty |
| IWM / SPY | 0.630 | Soft watch | no penalty |
| IWM / AMD | 0.621 | Soft watch | no penalty |

*Caveat carried from risk-monitor:* MRVL/SNDK is a **price** correlation, and SNDK is a delta-neutral long-vol structure rather than an outright long — true portfolio beta-overlap is smaller than 0.858 implies. The mechanical gate was applied anyway, with no discretionary exception.

**Macro & event risk:** core PCE **3.29%** above core CPI 2.81%; payrolls **+57k**; 10Y **4.68%, +24bp/30d** vs fed funds 3.63%; curve normal +47bp; USD weakening. Forward: **NFP 08-07 (T+5), CPI 08-12 (T+8), PPI 08-13; no August FOMC.**

**Fundamentals verdicts:**
- **MRVL — CAUTION (−1 tier).** Two consecutive earnings misses (−0.94%, −0.41%) after two beats; insider 3mo MSPR −5.32 (neutral, **not buying**); beta 2.24. Offsetting: revenue **+34.07% YoY**, D/E 0.31, earnings 20 days out.
- **SNDK — CONFIRM (0).** Beat streak 4/4 but decelerating (+597% → +27.8% → +76.3% → +57.9%). **Insider 3mo MSPR −100.0 — four straight months of maximal selling, not noisy.** Beta 4.26. Live China memory-glut catalyst. The gate reads this as *corroborating for long vol* (sustained selling + dated catalyst + bifurcated news = wide-distribution setup) **with the explicit caveat that the structure must stay delta-neutral.**
- **IWM / SPY — NA.** Index ETFs, no issuer fundamentals. NA never penalises.
- `fz_context`: `available: true` but **all fields null** for MRVL/SNDK (**C17 upstream quote-grid gap**); `available: false` for the ETFs.

**Debate-disconfirmation cuts — the gate fired on all four:**

| Ticker | bull | bear | Bear's decisive point |
|---|---|---|---|
| MRVL | 0.25 | **0.75** | accumulation-hunter's own intraweek reversal (2.24 → 0.90) + the **$281K LEAP close** — a long-duration holder exiting the same week |
| SNDK | 0.35 | **0.65** | 181% IV ⇒ **25.1% expected move** vs rv20-implied 21.3%; straddle breakeven ≈ **±20%**; this week's own recap shows ~50% IV crush within one session of reporting |
| IWM | 0.35 | **0.65** | Conceded negative-alpha class base rate + **zero price confirmation in five sessions (+0.01%)** + single-tool thesis |
| SPY | 0.25 | **0.75** | The DEX flip is **+19.68B at 2.28× trailing median** after an 11-session negative run, `whipsaw FALSE`, with GEX co-flipping POSITIVE on a **reliable** ZGL 0.02% from spot — too large and too cross-confirmed to be passive drift |

Notably, **both bulls arguing for index shorts conceded the 2026-06-27 audit finding** unprompted: 6 of 7 sized shorts that week were index ETFs at −2.10% mean while the lone single-name short won — *"no short alpha-sizing anywhere."*

> **⚠ The panic gate has no valid input this week.** `uw options-structure front-end-iv-ratio` returned `near_dte_actual = 0` on **every** name pulled (SPY 1.611, QQQ 1.696, AAPL 3.373, COIN 2.348, MRVL 2.183, NVDA 1.715, PLTR 1.422). All are Friday-0DTE contamination — the same artifact as 2026-07-24. Recorded as **`NA(substrate)`, not PASS**, on every call.

**Breadth cross-check (advisory):** finviz 221 advancers / 281 decliners, **`pct_green` 43.94%**, mean −0.13%, median **−0.24%**; top mover AMZN +15.32%, worst GDDY −16.70%. **`divergence_flag: true`** — SPY rose 0.72% on a day the median S&P member fell. Read every breadth signal this week against cap-weighted prints.

**Adverse-flow exits — carried `conviction_week_2026-W30` group:**

| Ticker | W30 position | Alerts | Flow now | Read |
|---|---|---|---|---|
| **INTC** | short, **starter — the only sized call in 20 weeks** | LARGE_DARK_POOL ($300.0M single trade), OI_SHIFT (+149,910) | **bullish** (+11,887) | **ADVERSE REVERSAL — EXIT CANDIDATE.** Flow has flipped against the short. Currently −2.30% in thesis direction (+0.28×ATR, INCONCLUSIVE), but the reversal argues for tightening or covering. |
| TSLA | short, watch_only | LARGE_DARK_POOL ($38.9M), OI_SHIFT (+177,206) | bearish (−$20.4M) | Still aligned. Hold as-is. |

**Hedge sleeve:** the live carried book is **100% short** (INTC + TSLA, both starter) — directional skew above the 0.6 threshold — and INTC has just flipped adverse. Given (a) eight consecutive audits finding negative selection in the short book, (b) SPY's own DEX+GEX flip favouring continuation, and (c) a melt-up that is cap-weighted but real in price, the recommendation is a modest **defined-risk SPY or QQQ near-the-money call vertical spanning the 08-07 NFP print**, sized at ~30–50% of the two carried shorts' combined notional delta. This is insurance against a continued mega-cap-led melt-up, not a new directional bet. **Given the explicit adverse reversal on INTC, tightening or covering that leg outright is the more direct action;** the hedge sleeve is the fallback if it is carried into next week.

---

## 8. High-Conviction Cross-Ref (HIGH and MEDIUM tier)

**Empty — zero HIGH, zero MEDIUM.** This is the **20th consecutive empty conviction board**.

**Expectancy lens (advisory — C31):** not computable this cycle. There are no post-freeze HIGH/MEDIUM resolved calls to build a per-tier expectancy from — the freeze-lift criterion has now failed for a seventh consecutive cycle for exactly this reason. The most recent `/calibration-audit` (2026-07-25) recorded DROP **0.431** vs sized **0.361**, the sixth straight cycle where the declined book outperformed the traded one.

### Why each LOW name died — the useful output

**MRVL long (raw 5, the week's top score) → watch_only.** Gates: sector −1 (semis were the funding source), fundamentals −1 (CAUTION), debate −1 (0.25 vs 0.75). The score itself is the problem: **+3 of its 5 points come from the saturated OI line.** Strip that and MRVL is a raw 2 — a DROP. Both agents that produced its mechanical passes **disowned them**: dealer-positioning disqualified its own DEX flip (GEX flipped the opposite way the day *before*; 72% of per-strike gamma at a single strike below spot), and accumulation-hunter rejected the name outright on C28 distribution. `load_bearing_tools_cited` is 4-of-4 — but **two of those four citations are rejections**, so the gate is measuring breadth of inquiry, not breadth of support.

**SNDK vol_long (raw 4) → watch_only.** Gates: cluster −1 (0.858 with MRVL, lower score), sector −1, event_risk −0.5 (NFP at T+5 on the same 08-07 expiry as the earnings play), debate −1. Also +3-of-4 from the saturated line. The bear's hurdle math is the decisive argument: 181% IV at 7 DTE prices a **25.1% expected move** against ~21.3% implied by trailing rv20, with a straddle breakeven near **±20%** — and every clean print in this week's own recap crushed IV ~50% within a session.

**IWM short (raw 3) → watch_only.** Gates: regime −1 (short vs UPTREND), event_risk −0.5, debate −1. **Structurally the best evidence in the entire union** — a real five-day program with verified opening prints (v/OI 52.3 and 142), genuine two-sided verticals, held and rolled *down* through a +2.4% rip. But: zero price confirmation (+0.01% on the week), **1-of-4** load-bearing tools, no backtest class exists, and it is an index short.

**SPY short (raw 3) → watch_only.** Gates: regime −1, event_risk −0.5, debate −1. Carries a contradiction the score cannot express: **dealer-positioning has SPY as a qualifying DEX flip LONG** with moderate conviction, while the multileg book is short. And sweep-tracker itself declines to treat SPY as tradeable — *"pure index hedge flow, context only"* — so the $10.5B of bearish premium is hedging, not conviction.

### Dropped by the rubric (raw ≤ 2)

| Ticker | Dir | raw | Why it died |
|---|---|---|---|
| **TSLA** | short | 2 | Largest bearish book of the week ($3.34B, bearish 5/5) and the cleanest sector-leader claim (−$634.9M) — and it earns **zero** for the sweeps, because that line was **removed 2026-05-23** after two audits measured it at −22/−24pp marginal. Price was **flat, −0.58%**, against $3.34B of bearish premium: hedge/overlay flow. **Third failed instance of this thesis.** |
| **AMD** | short | 2 | Sector and cum-flow legs clean, but flow-side corroboration **absent by sweep-tracker's own admission** (never cleared smart-money top-50 on any day). 90d flow is **+$64.2M, opposite** the 30d. DEX turned **positive** on 07-31. Reports **08-04**. The +1 earnings-vol line was withheld under the C13 router — earnings-scout's AMD read is `vol_long`, **a different trade**; paying it would manufacture confluence from two agents that disagree. |
| **AAPL** | short | 1 | The **cleanest mechanical evidence set of the week** — longest DEX run (14 sessions, whipsaw FALSE), same-day GEX confirmation, all three sector legs, a −7.35% Friday, and a DP distribution flag three sessions before the print — killed by `flow_conflict_lite` on bottom-quartile magnitude ($90.4M = 0.50× union median). Also: 90d flow **+$315.3M** opposes, and the earnings event has **already passed**. |
| **COIN** | short | 0 | **Verification killed it: 30d cum-flow is +$22.4M BULLISH against the short** — the one figure the union file lacked, and it pointed the wrong way. Only evidence was the **most-whipsawed DEX flip in the set** (6 sign changes in 14 sessions) on the 0DTE Friday. dealer-positioning explicitly refused to call it actionable; vanna contradicts. |

> **⚠ Registerable finding — `flow_conflict` is phrasing-sensitive, and the two authorised branches are not equivalent.** AAPL scores **raw 1 (DROP)** under the primary union-median branch and **raw 3 (LOW)** under the authorised `$50M` mechanical alternative. The quant applied the primary branch correctly (the fallback's precondition — "union-median unavailable" — is not met at n=8), but the rule text asserts the two are "equivalent on recent data" and **on this week's data they are not.** Compounding it: AAPL's −$90.4M is **~1.3% of its own $6.9B gross 30d premium, essentially identical to SPY's 1.2%** — the mega-cap scale degeneracy the C11 P1.4 scale-relative floor was written to fix. Practical stake is small (both readings land at starter-or-below), but the divergence should be registered.

### Embedded rubric (for audit)

```
Weekly conviction score = Σ:
  # +3 line for swept on ≥3 of 5 days REMOVED 2026-05-23 audit P0.3
  +3  uw historical oi-trend BUILDING for the full week, --days ≥ 5   # WEEKLY-ONLY +3 vs DAILY +1; C47 sharpening pre-registered
  +3  3+ aligned signals in accumulation-hunter sustained across week, uw dark-pool block-stratified institutional-tier confirmed
      — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms (sign aligned AND |cum_flow_30d| ≥ $50M); else halved → +1
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70, stable WoW — CONDITIONAL: only when dominant_signal_class == leap_directional
  +2  uw oi position-rolls shows institutional roll forward into longer-dated LEAP (per-covered-date)
  +1  uw historical cumulative-premium-flow net directional accretion across the week — INTENT-SCREENED (no C28 distribution_flag; no dividend-capture parity issue)
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna squeeze in trade direction — verified SIGN CHANGE only, via scripts/dex_flip.py
  +1  sector-rotation-strategist names ticker as single-name leader — CONDITIONAL: persistence_score ≥ 0.6 AND cum_flow_30d aligned AND |cum_flow_30d| ≥ $50M
  +1  earnings-scout BUY VOL or SELL VOL for next 2 weeks (term-skew aligned for full size)
  +2  multileg-strategist directional structure repeated on ≥2 days (term-structure-anchored play type)
  +1  vol-surface-scout KINKED/BACKWARDATION worsening WoW; iv-percentile-zscore extreme; VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner crowded long with rising pc-ratio-zscore trajectory (VRP positive)   # INFORMED-FLOW CONTINUATION penalty
  -3  flow_conflict — cum_premium_flow 30d clearly opposite dominant_signal_class
  -1  flow_conflict_lite — 30d cum_premium_flow read is MIXED   # mutually exclusive with flow_conflict
  # TIER GATES (risk-monitor, Step 2d — 0 points, never in score_components):
  -2  [TIER GATE] correlation cluster (pairwise corr ≥ 0.70) → −1 TIER
  -3  [TIER GATE] WoW regime flip conflicts with trade direction → −1 TIER
```
**Tiers:** ≥9 HIGH (full) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 drop. `rubric_version: 2026-06-12` (FROZEN). Tier cuts carry **no validated ranking claim** — they failed re-confirmation on 2026-06-12 (HIGH 0.222 / MED 0.214 / LOW 0.444) and are retained only under the freeze.

---

## 9. Setups for Next Week

### Next-session GEX advisory (SPY/QQQ only — prose, 0 rubric points)

> **Lead with the track record: the Step 0 rolling backtest returned `NO_GO_NO_EDGE`.** Pooled over 118 sessions, the next close landed closer to the nearest EOD wall in only **24 of 118 = 20.3%** (p vs 50% = 1.0) — walls behaved as **anti-magnets**, markedly *worse* than a coin flip (SPY 18.6%, QQQ 22.0%). Containment-within-walls and pin-direction were both coin flips (52.5%). H1 (short-gamma → higher next-session vol) **ran backwards pooled**: long-gamma mean |ret| 0.776 vs short-gamma 0.731 (n=40). **Nothing below is a predictive claim.**

**SPY** — spot 747.06 · ZGL **746.93** (`zgl_reliable: true`, 0.02% from spot) · regime **POSITIVE** (long gamma) · total_gex **+1.19B** · call wall **748** (+0.13%) · put wall **730** (−2.28%). **The flip is one session old.** SPY was FULLY_NEGATIVE every session 07-27→07-30 with a null ZGL throughout; it turned POSITIVE with a clean ZGL only at Friday's close, coincident with reclaiming both SMAs. Spot sits almost exactly on both the ZGL and the call wall — dealers are near flat-gamma at the money, and small moves either way could re-flip the sign. The downside gap to 730 is the only real space in the book.

**QQQ** — spot 687.99 · ZGL **null** (`zgl_reliable: false`) · regime **FULLY_NEGATIVE**, but total_gex is only **−2.19M**, essentially flat · call wall **688** (= spot) · put wall **680** (−1.16%). QQQ never resolved a clean zero-gamma level all week (a 07-30 reading of 729.4 against a 683.77 spot was 6.7% away — an extrapolation artifact, correctly discarded). A FULLY_NEGATIVE label on a near-zero total_gex is a coin-flip regime with very little structural conviction.

*Mandatory caveats:* the EOD book is refreshed by 0DTE OI in the first 30–60 minutes; overnight gap risk into an NFP week; this is the **ETF** book, not SPX/NDX; and `uw` cannot isolate the D+1 expiry from the 0–45d aggregate. Friday's 0DTE tranche has already rolled off — nearest surviving expiries are 08-03 ($2.06B), 08-07 ($3.47B), 08-21 ($3.92B), 09-18 ($5.57B).

### Next-session 0DTE premium-selling setup (validated stack — advisory, 0 rubric points)

Rolling backtest verdict **`GO_PREMIUM_SELL_INTRADAY`**. Both indices `sell_premium: true`, `vol_state: LOW` (VIX **15.99**), `size_scalar: 0.5`.

| | SPY | QQQ |
|---|---|---|
| implied_move | 0.49% | 0.97% |
| expected_range | 0.79% | 2.01% |
| structure | iron fly / short straddle centred **747.07**, wings ≈ ±0.79% (long-gamma: quieter, mean-reverting) | wider iron condor, wings ≈ ±2.01% (short-gamma: trendier) — or reduce / stand aside |
| **mean PnL (net)** | **+0.148%** | **+0.282%** |
| mean PnL (gross) | +0.248% | +0.382% |
| worst day | −1.40% | −2.453% |

**Quote PnL on its real basis:** these are **% of underlying spot notional, GROSS** of costs (`round_trip_cost_pct_assumed` 0.1); the **net** line leads. Not premium-collected, not margin-relative. Entry rule: enter at/after the open once the overnight gap resolves; if it gaps beyond the wings, stand aside; **hold to the close — never carry overnight.** SPY ≈ SPX (trade either); QQQ is weaker. **Tail caveat, mandatory: there is no vol shock in the 60-day sample — the short-vol left tail is UNSAMPLED, and gross win-rate overstates a negatively-skewed short-vol edge.** Advisory and 0 points **permanently**; win-rate is explicitly not the promotion metric.

### Swing setups from dealer positioning (1–4 weeks)

> **⚠ Read this before acting on any DEX flip.** **All six mechanized flips fired on the same session — Friday 07-31, the 48.2%-0DTE RETAIL_DRIVEN day.** Six independent names flipping sign simultaneously on the highest-0DTE-share day of the week is a signature of expiry contamination, not six independent dealer repositionings. **A Monday 08-03 second-session confirmation is the cheapest, highest-value check available before anything here is acted on.**

| Ticker | Flip | Quality | Verdict |
|---|---|---|---|
| **AAPL** | SHORT | prior_run **14** (longest), mag 2.32×, `whipsaw FALSE`, GEX confirms same day (176M→−199.7M), top strike only 30% of total | Cleanest of the six — but scored raw 1, DROP |
| **SPY** | LONG | prior_run **11**, mag 2.28×, `whipsaw FALSE`; GEX co-flipped POSITIVE with a reliable ZGL | Contradicts the SPY multileg short outright |
| **NVDA** | LONG | prior_run 4, mag 6.2×, `whipsaw FALSE`; GEX already POSITIVE since 07-22 (DEX catching up to gamma, a cleaner setup) | Failed confluence (1 agent) |
| **PLTR** | LONG | prior_run 3 (bare minimum), mag 2.08×, **`whipsaw TRUE`** (4 changes); but DEX+GEX+vanna all agree | Failed confluence; **reports 08-03** |
| **MRVL** | LONG | prior_run 5, mag **1.59× (thin)**, **`whipsaw TRUE`**; **GEX regime disagrees** | Disowned by its own agent |
| **COIN** | SHORT | prior_run 4, mag 6.14×, **`whipsaw TRUE` — 6 sign changes, worst in set**; vanna conflicts | Disowned by its own agent |

**No vanna squeeze qualifies.** VIX fell for only **two** consecutive sessions (07-30, 07-31) off the FOMC spike — one short of the ≥3-session requirement. Put-heavy books that would become candidates if VIX prints a third down day Monday: **QQQ** (deeply negative DEX collapsing toward zero, closest non-qualifier to both a flip and a squeeze), AAPL, COIN, PLTR, MU, ARM, SMH, SNDK, TSLA.

### Pin vs trend

**Trend, weakly — and with low confidence.** SPY's long-gamma flip is one session old and sits on top of its own ZGL and call wall; QQQ's total_gex is essentially zero. Neither book offers the wide, well-defined range a textbook pin regime would. With the GEX advisory at `NO_GO_NO_EDGE`, the honest read is that the dealer book gives **no usable pin/trend signal this week**.

### Actionable setups for the coming week

**None at HIGH tier — there are no HIGH-tier names.** What to watch instead, in priority order:

1. **Monday 08-03 DEX re-read** on SPY, AAPL, NVDA, PLTR, MRVL, COIN. If the flips hold on a normal-0DTE session, they become real; if they evaporate, F1 is confirmed as an artifact class and should be registered at the next audit.
2. **INTC — act on the adverse flow.** Tighten or cover the carried W30 short; flow has flipped bullish (+$300.0M single DP trade, OI +149,910).
3. **ARM calendar** (sell 08-21 173.7% / buy 08-14 or 09-18) — the cleanest vol structure of the week, watch-only on a single-agent finding. Re-check whether a second agent picks it up.
4. **PLTR earnings Monday** — not a trade, a hazard. Most extreme front-panic + most complacent back-month in the lookahead.
5. **The 08-03 earnings cluster is largely unpriceable** — 9 of 15 names have no measurable event tenor. Do not read their calm-looking front ends as calm.

### LOW-tier names to track for daily-analysis confirmation

**MRVL, SNDK, IWM, SPY** — all written to `conviction_week_2026-W31`. Each needs a specific trigger before it becomes tradeable: MRVL needs Monday DP prints re-confirming accumulation (mega-tier buy ratio back above 0.7) and a non-0DTE DEX confirmation; SNDK needs to be re-examined *after* the 08-05 print; IWM and SPY need **price confirmation** — the ladders have been rolled down all week against a flat-to-rising tape, and until price moves, both are theses describing their own drawdown.

### Deep-dive hand-off

**Skipped — no-edge week.** No HIGH-tier, post-gate, non-VETO name exists to hand off.

---

## 10. Watch-only — single signal, no confluence

Surfaced by exactly one Phase 1 agent, or contradicted by others. **Journaling only — not for entry.**

| Ticker | Signal | Why it failed the gate |
|---|---|---|
| **ARM** | vol-surface: genuine liquid KINKED at 08-21, prominence 54.2%→79.7%, no catalyst, front-end falling | 1 agent; a vol trade, not directional. **The best single finding of the week.** |
| **SPCX** | sweep-tracker bullish 5/5, 66.8% OI-opening confirmed, $952.9M premium | sector-rotation has it **bearish** (−$181.9M 30d); leap-radar dropped it. Verified real (Space Exploration Technologies, ADV $9.3B) but **IPO'd 2026-06-12** — only ~33 sessions of history, so 30d/90d flow is unreliable. |
| **INTC** | sweep-tracker bullish lean 5/5, OI-opening 75.9% | leap-radar hard-dropped it (30d −$914.7M, 90d −$753.2M). **A long here contradicts a live carried short.** |
| **NVDA** | dealer-positioning DEX flip LONG (clean, whipsaw FALSE) | sector leg (b) fails (−$64.8M); leap dropped it; matrix confidence 13.2%. |
| **PLTR** | dealer-positioning DEX flip LONG, best internal alignment | sector leg (b) fails (−$160.0M); earnings-scout NO PLAY + hedge flag; **reports 08-03**. |
| **SMH** | sweep-tracker bearish 4/5, PUT-dominant every sampled day, $51.7M 2027 LEAP put | sector-rotation labels it MIXED/appendix-only; multileg says the put spreads were a **roll** of an existing 76k-OI book whose expiry has passed. Graded **LOSS (−1.44×ATR)** on 07-29. |
| **MU** | five agents touched it | **They contradict each other.** leap 5-of-9 long; accumulation **rejected** (closing-cross leak — 84.5%/86.4% of Mon/Tue top-30 premium inside 20:00–20:25Z, and ex-cross the Monday read flips to **91% SELL**); sector caution (30d +$466.9M bullish vs −10.6% price); vol-surface **disqualified** (08-07 kink is NFP-priced); sweeps "mixed". No clean direction. |
| **RDDT** | earnings-scout: **still-live**, not resolved | Post-crash term structure remains backwardated (1.116) with GEX FULLY_NEGATIVE. Was VETO'd in the 07-31 daily envelope. |
| **QGEN** | multileg: Aug-21 1×2 call backspread 40/45, ratio exactly 1:2 on two consecutive days, C45 bought at 96–97% ask, OPENING (v/OI 3.23) | 1 agent. Net ~$0.52 **credit**; profits <$40 or >$50.52; max loss $4.48 at $45. Term-structure anchor is thin (n=62). |
| **WOLF** | multileg: Sep-18 put debit spread 22.5/17.5 (v/OI 874 opening) + Jan-27/Jun-27 call diagonal | 1 agent. Bimodal/distressed, ~130% IV flat, defined risk both ways. |
| **LITE** | accumulation sub-threshold; DP shelf **$693.24** (37 trades, $252.5M) is a genuine C34 anchor | conviction-matrix never reaches DIRECTIONAL_LONG (1.6% → 17.9%). Net cum-flow is only 3.4% of $3.04B gross — a thin skew. |
| **STX** | accumulation sub-threshold; DP shelf $856.13 exactly at Friday's close | Mega tier **net sell** (0.225) while block tier net buy (0.613) — tiers disagree. cum-flow −$17.24M **fails** the $50M test. Matrix = **COVERED_CALL**, an explicit disqualifier. |
| **EA** | vol-surface: rv20 3.8%, lowest IV percentile in the scan | **Merger-arb pin.** Real, not an artifact — pinned near a cash-deal price. Same class as the NUVL VETO. |
| **WBD** | leap-radar | **Merger-arb signature** — equity accumulation + bearish options premium + inconsistent OI. |
| **UCTT / EQIX** | contrarian: the week's only ±2σ extremes (z 6.14 / 6.40) | UCTT is an insurance bid into a known 08-03 catalyst (a real hedge, not a fade); EQIX has price and flow **aligned** — continuation, nothing to fade. |
| **AMZN / GOOGL** | contrarian soft crowded-long flags | Neither crossed ±2σ (z −0.42 / −0.24) so **no hard −2 is statistically justified**. **MSFT was explicitly cleared** — z **+1.06**, i.e. *more* put-hedged than its own 20-day norm despite +21.8%; do not penalise it. |

---

### Appendix — substrate and tooling defects recorded this week

| # | Defect | Impact |
|---|---|---|
| F1 | **All six mechanized DEX flips fired on the same 48.2%-0DTE Friday** | Every +1 DEX award is provisional; needs a Monday 08-03 re-read |
| F2 | **`front-end-iv-ratio` returned `near_dte_actual=0` on every name** | The panic gate has no valid input; recorded `NA(substrate)` |
| F3 | **C47 saturation universal** — `consecutive_build_days == --days` at *both* 5 and 10 on every ticker checked by two independent agents | The +3 weekly OI line has zero discrimination; it carries 3 of MRVL's 5 and 3 of SNDK's 4 points |
| F4 | **`sector-flow` ≡ `sector-flow-persistence`** (identical to the dollar); only `market-regime.sector_rotation` is netted | Corrects a standing project assumption |
| F5 | **`earnings-catalyst.implied_move_perc` broken** (PLTR 0.14% vs 14.7%; SNDK 0.83% vs 25.1%; CRWV 0.68% vs 24.3%) | Envelope `implied_move` uses derived values |
| F6 | **`iv-percentile-zscore` returned `dates_used: 77`** (< 120-day floor) on every call | All percentiles provisional |
| F7 | **`iv-outliers` 100% contaminated** — 20/20 in the 0DTE bucket | Not cited anywhere |
| — | **`pc-ratio-zscore` has no `--date` flag** | The command's "z-score trajectory across covered_dates" is **not producible**; contrarian-scanner substituted per-session `historical trend` P/C ratios and said so |
| — | **`market-regime`'s `spy` sub-block ignores `--date`** | WoW price deltas must not be read from it |
| — | **`fz screen` ticker field corrupted** (AABEO, NNWL for Newell, CCDNA for CaredX) | Squeeze/RS funnel lanes graceful-skipped; `fz breadth` unaffected |
| — | **`fz` quote-grid gap (C17)** — all analyst/short-interest fields null | `fz_context` present but empty on both single names |
| — | **`flow_conflict` phrasing-sensitive** — union-median vs $50M branches disagree (AAPL raw 1 vs raw 3) | Registerable; rule text claims equivalence that does not hold here |
