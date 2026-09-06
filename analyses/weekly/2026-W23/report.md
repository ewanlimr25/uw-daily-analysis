# Weekly Market Intelligence — Week of 2026-06-01 (ISO 2026-W23)

## Executive Summary

- **Week regime + WoW Δ:** TRANSITIONAL (PULLBACK_IN_UPTREND) held all five sessions but deteriorated internally — bullish flow breadth collapsed 40.1% → 29.4%, VIX spiked +6.1 to 21.51 into Friday's close, and both SPY and QQQ ended the week in FULLY_NEGATIVE dealer-gamma regimes. VRP is FAIR (+0.043) — no vol edge either way, and the front end is in outright backwardation (SPY 1.99 / QQQ 1.85).
- **Signal performance:** 7 of 10 resolved early-week signals confirmed (70%). The split is the story: every WIN was bearish, vol-up, or defensive (single-leg Tier-1 puts on MU/SNDK, the IWM bear diagonal, the VIX call ladder, healthcare accumulation); every LOSS was a cyclical long (MU pre-print bullish flow, Tech inflow persistence, FCX accumulation).
- **Top swing build for next week:** **None sized.** The week's highest-conviction structure — SHORT IWM (raw 11, the only MEDIUM-tier call) — gates to **watch-only**: the LB gate demoted it (2/5 load-bearing tools), its signal-class backtest is 0-for-2 with −73pp market excess, and the bear matched the bull in debate (0.65/0.65) after showing Friday's "roll-down" prints were a mechanical hedge roll. Entry trigger, not a position: IWM failing to reclaim 292 post-CPI with GEX still negative.
- **Top LEAP build:** **None qualified** — zero names passed the 6-of-9 LEAP gate (UTHR and FCX both stalled at 5/9). The week's LEAP tape is dominated by *bearish hedging*: the $340M IWM P290 Jan-2027 put flood is the largest long-dated move on the book.
- **Biggest emerging risk:** The index correlation cluster (IWM/SPY 0.897, SPY/FCX 0.755, IWM/FCX 0.726) sitting directly in front of a three-print macro stack — CPI 6/10, PPI 6/11, FOMC+SEP 6/16-17 — with dealers short gamma on both major index books. Institutions spent all five sessions building one coordinated macro hedge (IWM puts + VIX calls expiring FOMC day + SPY CPI condor + HYG credit spreads). Adverse-flow exits fired on four prior-week conviction names (SMH, AVGO, ORCL, MSFT).

**Desk posture: this is a no-edge week by mechanical gating, not by judgment override.** All six scored names land watch-only. The only actionable structure is the hedge sleeve (defined-risk VIX call ladder into FOMC, mirroring the institutional template observed all week). Re-entry levels are journaled per name below; the CPI print on Wednesday is the gate-reopening event.

---

## 0. Week in Review — Intra-Week Signal Performance

Hit rate: **7 WIN / 3 LOSS** (70%), 3 INCONCLUSIVE excluded. Sourced from `uw hot-chains sweep-persistence`, `uw historical oi-trend`, `uw historical cumulative-premium-flow`, `uw historical trend` (no daily files read).

| Ticker | Signal type | Early-week direction | Week-end outcome | Grade | Note |
|---|---|---|---|---|---|
| MU | Pre-print bullish flow (3 of 4 days into print) | Bullish | −13.25% Friday post-earnings | **LOSS** | Bullish positioning into the print was trapped |
| MU | Single-leg Tier-1 opening puts (C19, 06-01/02/03) | Bearish | Print −13.25% | **WIN** | 4-session put persistence = top C19 signal of week |
| SNDK | Single-leg Tier-1 puts (06-01, escalating) | Bearish | ~−15% Wed→Fri | **WIN** | 3-session persistence; collateral to MU |
| LULU | FE-ratio 2.08 backwardation (BUY VOL read, Mon) | Vol-up / big move | −13.5% realized post-print | **WIN** | FE>1.10 disqualifier fired correctly |
| MRVL | Pre-print bullish flow → post-print | Bullish | Week +20% but −17% off post-print high; Fri flow −$62.5M | INCONCLUSIVE | Price up on week, flow flipped hard bearish |
| IWM | Multileg bear put diagonal (initiated Thu) | Bearish | Fri −3.5%, broke 282 | **WIN** | $524M structure, rolled down same week |
| VIX | Multileg call ladder (5/5 sessions from Mon) | Vol-up | VIX 15.4 → 21.51 (+6.1) | **WIN** | Jun-17 expiry = FOMC settlement day |
| Tech sector | Mon +$13.1B net inflow persistence | Bullish | Inflow −71% by Fri; semis de-risked | **LOSS** | Persistence sign held but magnitude collapsed |
| Healthcare | Sector accumulation from Mon (+$216M) | Bullish | Only accelerating sector (+$305M Fri); JNJ +4.1% | **WIN** | Defensive rotation confirmed |
| TSLA | Bearish net flow 5 of 7 sessions | Bearish | ~−6% on week; DEX flipped short Fri | **WIN** | Dealer flip confirmed the flow |
| FCX | DP block accumulation Mon–Thu | Bullish | −9% Friday to $63.37 (on the DP shelf) | **LOSS** | Price contradicted the DP story; shelf tested once |
| XLE | Multileg bear put spread (Mon) | Bearish | Flat (57.3 → 57.67) | INCONCLUSIVE | Inside spread range, no resolution |
| HYG | Multileg credit-hedge put spreads (Mon/Tue) | Bearish | −0.5% (79.84 → 79.43) | INCONCLUSIVE | Insufficient movement |

The week's defining lesson: **dark-pool accumulation on defensives beat sweep/flow momentum on cyclicals by every measure**, and the C19 single-leg put scan (advisory) had its best week on record — Tier-1 put prints surged 3–5/day Mon–Wed → 13 Thu → 16 Fri, front-running Friday's de-risk.

---

## 1. Regime & WoW Delta

`uw risk market-regime` printed **TRANSITIONAL — PULLBACK_IN_UPTREND** on both Monday and Friday, but the label hides the deterioration: bullish-flow breadth fell 40.1% → 29.4%, the regime tool's Friday day-flow showed Technology −$808M / CommSvcs −$130M / ConsCyclical −$125M against Consumer Defensive +$13M / Healthcare +$12M, and SPY closed below its 20-SMA (737.55 vs 746.29) while holding the 50-SMA (713.51). Guidance unchanged all week: *half position sizes, defined-risk structures*.

**Vol regime (`uw historical vrp`):** SPY VRP +0.043 (IV30 16.5% vs RV30 12.2%) = **FAIR** — a mild premium-selling tilt on paper, but the Friday VIX spike (+6.1 to 21.51) and front-end backwardation (SPY 1.99 / QQQ 1.85, with the expiring-0DTE near-leg caveat) mean the panic gate fires market-wide. Premium-selling structures are disqualified until the front end normalizes.

**Institutional vs retail share (`uw options-flow dte-volume-share`):** Monday BALANCED (0DTE 19.4%) → Friday RETAIL_DRIVEN (0DTE 44.4%). Retail chased the Friday move; institutional positioning had been laid earlier in the week (see §3 multileg).

**Macro backdrop (FRED):** Yield curve normal (+0.38), core CPI 2.99% / core PCE 3.29% (sticky above target), payrolls +172k (hot — the NFP print catalyzed Friday's rate-repricing), unemployment 4.3%, 10Y 4.47 flat, USD weakening, Fed funds 3.62.

**Event risk (next two weeks):** CPI **Wed 6/10**, PPI **Thu 6/11**, jobless claims 6/11 & 6/18, **FOMC + SEP Tue/Wed 6/16-17**, OPEX Fri 6/19. Every swing horizon on the book contains all three Tier-1 prints — the event-risk gate fires on every name this week.

**Implication for next week's bias:** The tape enters CPI week with dealers short gamma on both index books, a hot-payrolls hawkish prior, and institutions already hedged. A benign CPI unwinds the hedge complex violently (short-cover rally, vol crush); a hot CPI activates the dealer sell-amplifier. Binary — which is precisely why the book carries no directional size into Wednesday.

---

## 2. Sector Rotation

**Rotation regime call: cyclical → defensive, HIGH confidence** (sector-rotation-strategist).

- **Rotating INTO:** Healthcare (persistence 1.0, the only sector whose Friday flow exceeds Monday's: +$216M → +$305M) and Consumer Defensive (persistence 1.0, flow nearly doubled Mon→Fri). Leaders: **LLY, JNJ, UTHR** (healthcare).
- **Rotating OUT OF:** Technology (persistence 1.0 on sign but magnitude collapsed −71%, $13.1B → $3.8B daily; ETF read XLK net-bearish), Consumer Cyclical (−97.5% magnitude; XLY −$8.5M BEARISH, GICS+ETF agree), Communications (fading; XLC disagrees → watch-only), Industrials (0.8 persistence, XLI bearish; transport leaders JBHT/SNDR/ODFL exempt).
- **Intra-sector dispersion:** Tech is bifurcating, not uniformly bearish — STM/AMD/ON/TSM/KLAC/TER survived the Friday screen as relative-strength names while NVDA/MU/MRVL/SNDK/INTC/AVGO led outflows. Do not short the survivors on the rotation thesis alone.

**ETF flow tape (advisory — instrument layer, no rubric points):**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| **XLV** | inflow +$3.6M | bullish 5/5 | Institutionally active; above-mid intraday buys | **$52.4M Jan-2027 LEAP call block (3 prints, no_side) — strategic initiation** | **agree** | LLY, JNJ, UTHR |
| **EWT** | inflow +$4.5M | bullish 5/5 | Creation-dominated + secondary above-mid buys | Jun $100 calls ask-side, multi-fill | n/a (Taiwan) | — |
| **XLE** | inflow +$4.3M | bullish 5/5 | Bid-below-mid (hedging pattern) | Mixed; $1.98M Sep 55 put sweep = bearish tell | agree (downgraded to HOLD) | — |
| **IGV** | outflow −$22.8M | bearish 5/5 | Close prints mechanical (wide spread) | **Jul 103 puts $5.25M combined — bearish** | agree (Tech out) | — |
| **XLY** | outflow −$8.5M | bearish 5/5 | Early-week RS buying, late-week neutral | Put-dominant sweeps | agree | short: TSLA; hold: LULU, TJX |
| **XLI** | outflow −$2.9M | bearish 5/5 | Index rebalancing, neutral | Light put hedging | agree (medium) | avoid shorting CTAS/JBHT/SNDR/ODFL |

The **XLV Jan-2027 LEAP call block ($52.4M)** is the single clearest institutional accumulation print of the week — LEAP-tenor, no_side block initiation at the sector level, agreeing with GICS persistence. It strengthens the healthcare-leader read but adds no rubric points. Watch-only conflicts: XLC (GICS fading vs ETF bullish), XLU/XLB (GICS positive vs ETF bearish), SMH (mixed — $23.7M net on $1.8B gross is noise).

**Rotation invalidation:** Healthcare persistence < 0.6 for 2+ sessions, XLV flow flipping put-dominant, VIX < 19, or breadth recovering > 45%.

---

## 3. Swing Book (1–6 weeks) — ranked by weekly conviction score

**Every name gates to watch-only.** The stack: panic gate (front-end > 1.10, market-wide) + event-risk gate (CPI/PPI/FOMC inside every horizon) + debate gate (bear residual ≥ bull on all five) fires before any name-specific consideration. The table records the book as scored, with re-entry triggers — these are journal entries, not positions.

### 3a. Long swings (regime-aligned: defensive rotation)

| Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure (if triggered) | Invalidation (C34 DP shelf) |
|---|---|---|---|---|---|---|---|
| DXCM | LOW | 6 | 0.50 (fallback, n=0) | **watch-only** | Institutional DP blocks 3/5 + OI build 5/5 + dual analyst upgrades (Stifel $90, Citi $84) + ADA catalyst; fundamentals CONFIRM | Conditional: long / call spread only after ADA read-through AND hold above shelf | **$72.86**; bear note: IV is 77th pctile (not cheap), Jan-2028 $60 put ladder building underneath |
| JNJ | LOW | 5 | 0.50 (fallback, n=0) | **watch-only** | Mega DP blocks 5/5 ($164M Fri at 100% buy) + healthcare rotation leader — BUT 30d net premium −$7.4M contradicts; bear's covered-call-overwrite read explains all signals; fundamentals CAUTION | None until net premium flow turns positive over a 5-session window | **$232.77** |
| FCX | LOW | 5 | 0.50 (fallback, n=0) | **watch-only** | Block DP 5/5 + largest OI build (+99k) + copper macro + 4/4 beats — BUT cyclical long against defensive rotation, below ZGL (dealer amplification), revenue −24% YoY, fundamentals CAUTION | Bull put spread 60/55 only if shelf holds through CPI | **$63.02–63.42** (tested once, Friday close $63.37) |
| UTHR | LOW | 4 | 0.50 (fallback, n=0) | **watch-only** | DP buy/sell 3.56 + conviction-matrix DIRECTIONAL_LONG 77.9% + 10d OI build; flow sub-$50M (C11 halved); fewest gate-fires of the book (3) | Jan-2027 500/600 call debit spread pending LEAP-gate qualification | **$547.60–550.38** |

⚠ **Distribution caution (C28):** No name carries a mechanical `distribution_flag` (no bullish-side OI closure detected on the longs — `uw oi decrease-with-volume` clean). The JNJ caution is an *inference* (premium-flow divergence + insider trend), not a C28 flow flag.

### 3b. Short / fade swings (defined risk only)

| Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure (if triggered) | Invalidation |
|---|---|---|---|---|---|---|---|
| IWM | **MEDIUM** (demoted from HIGH, LB 2/5) | **11** | 0.000 (n=2, excess −0.733) | **watch-only** | The week's strongest structure: $524M bear put diagonal + DEX flip +$7.6B→−$15B + FULLY_NEGATIVE GEX + $340M Jan-27 LEAP put flood + 90d −$1.07B smooth bearish. BUT: backtest 0-for-2, bear showed the Friday prints were hedge ROLLS and the LEAP blocks were no_side cross-trades; PCR 1.89 = hedge already crowded | Bear put spread (e.g. Jul 280/265) only on a post-CPI failure to reclaim 292 with GEX still negative | Close above week high (292) on volume, or CPI < 2.8% core |
| SPY | LOW | 6 | 0.69 (capped, n=6, excess +0.10) | **watch-only** | $116M Jun-10 CPI put condor + DEX flip + FULLY_NEGATIVE GEX — but the condor reads as hedge-book insurance; PULLBACK_IN_UPTREND base rate against a 2–4% flush; theta bleeds into the print | None — the institutional condor is the observed hedge template, not an alpha trade | Close above 750 pre-CPI |

Sweep-tracker context (informational, 0 points): bearish sweep persistence on NVDA/MSFT/ORCL through the week; SNDK bullish sweeps failed (LOSS); MRVL/STM 30d correlation 0.876.

---

## 4. LEAP Book (6–24 months)

**Zero qualified candidates** — no name passed the 6-of-9 gate. The long-dated tape is hedging, not accumulation: IWM P290 Jan-27 +113k contracts ($340M, bid-side) and P265 Mar-27 +46k are the largest LEAP moves of the week; HYG/VIX/XLE rolls are risk-management structures.

| Ticker | Gates | Why disqualified | Watch trigger (re-run 2026-06-12) |
|---|---|---|---|
| UTHR | 5/9 | No LEAP OI initiations >500/day; no rolls; cum_flow +$8.1M sub-$50M (conviction-matrix 77.9% DIRECTIONAL_LONG is real) | Fresh LEAP OI in biggest-increases 3 of 5 sessions + 30d flow crossing $50M; earnings 7/28 |
| FCX | 5/9 | **Hard fail:** 90d flow MIXED (+$5.3M on $653M gross = noise); conviction 20.1%; LEAP book bilateral (collar = hedged ownership) | 90d flow turning BULLISH-labeled + conviction > 70 |
| LLY | 3/9 | 90d MIXED at scale ($37.9M net on $3.3B gross); conviction-matrix MIXED 8% | — |
| COF | 2/9 | **Hard disqualifier: conviction-matrix DISTRIBUTION** (DP buy/sell 0.39 against +$153M bullish flow — the canonical distribution-dressed-as-accumulation trap) | none — do not revisit on flow alone |
| A | 2/9 | COVERED_CALL scenario (explicit disqualifier) | — |
| DXCM | 3/9 | 90d flow −$750k wrong direction | — |

---

## 5. Volatility Surface — WoW Term Structure & Skew Evolution

The week ran a full semis earnings-IV cycle: MU/MRVL/FSLR entered in acute backwardation (100–140% front IV), crushed to contango by Friday — but back months retained 70–130% IV with residual Jun-12 kinks. Index surfaces moved the other way: SPY contango → backwardation (0DTE-mechanical but VIX-corroborated), QQQ back months now visibly pricing the Jun-10 CPI and Jun-18 FOMC kinks (Jun-18 IV 28.5% vs next-week 22.7%).

| Name | Mon → Fri shape | IV pctile (252d z) | VRP | Read |
|---|---|---|---|---|
| SMH | BACKWARDATION → BACKWARDATION, FE ratio 1.68 → 2.84 **rising** | 100th (z +2.16) | +0.030 | **Disqualified** — panic worsening, do not sell premium |
| STM | BACKWARDATION worsening, FE 1.22 → 2.06 | 100th (z +2.27) | +0.039 | **Disqualified** — rising ratio |
| TXN | FE 2.08 → 6.60 (severe) | 100th (z +2.14) | +0.069 | **Disqualified** — possible data artifact, monitor |
| CMCSA | Kink resolved (77% → 39%) | 100th (z +2.71, highest in set) | −0.005 | Watch-only — VRP neutral blocks the sell |
| FSLR | BACKWARDATION → CONTANGO (resolved) | 97th (z +2.26) | **+0.088** | Cleanest premium-sell candidate: Jul-17 iron condor, half size (policy-headline risk) |
| MU | Post-print crush; Jun-12 kink 123% vs Jun-18 133% | 100th (z +1.58) | −0.019 | Calendar: long Jun-18 / short Jun-12 into ~6/25 earnings shadow |
| MRVL | Jun-12 residual kink 150% | 100th (z +1.56) | **−0.126** | Long-vol calendar only — premium-selling contraindicated |
| AMD | BACKWARDATION → CONTANGO | 97th (z +0.99) | **−0.262** | Long-vol calendar (RV outrunning IV badly) |
| QQQ | KINKED → BACKWARDATION; back months 24% → 27-28% | 90th (z +1.65) | +0.048 | The CPI/FOMC kinks are the real WoW signal |

Top calendar candidates: **1) FSLR Jul-17 iron condor** (VRP +0.088, no catalyst, panic resolved), **2) MU Jun-18/Jun-12 calendar** (earnings-shadow), **3) AMD Jun-18/Jun-12 calendar** (negative-VRP long-vol). All half-size at most — the market-wide panic gate applies.

---

## 6. Earnings — Recap & 2-Week Lookahead

**(a) Recap — the FE-ratio gate had a perfect week.** All four prints (MU −13.25%, MRVL −17% off the print, LULU −13.5%, FIVE −13.5%) entered with front-end ratios above the 1.10 disqualifier and resolved through violent moves, not IV decay. Every SELL VOL expression was DISCONFIRMING; BUY VOL / directional puts were correct in all four. Lesson codified: *FE > 1.10 into backwardation + calls dominating pre-print flow = hedging of a known negative event, not bullish conviction* (MRVL was the textbook case). SNDK (−15%) confirmed sector-hedge propagation.

**(b) Lookahead (ranked, floor-passing):**

| Rank | Ticker | Date | Setup | Play | Conv. | FOMC contam. |
|---|---|---|---|---|---|---|
| 1 | **KR** | 6/18 pre | IV rank 100, PCR 0.21, COMPLACENT back-month, FE 0.48 | **SELL VOL full** (post-FOMC print — Fed known before entry) | 4/5 | nominal only |
| 2 | **MTN** | 6/8 post | TAIL_HEDGING back-month (+0.130), PCR 4.14 (extreme), BACKWARDATION FE 1.24 | **BUY VOL — long puts / put spread** (130/120) | 4/5 | NO (pre-CPI) |
| 3 | ORCL | 6/10 post | Jun-12 kink 126% vs back ~70%; COMPLACENT back-month; 253k call vol | SELL VOL half (iron condor) — close before FOMC | 3/5 | YES |
| 4 | LEN | 6/11 post | IV 100, clean Jun-12 kink, flat back-month | SELL VOL half — CPI lands the day before (rate-sensitive) | 3/5 | CPI direct |
| 5 | CHWY | 6/10 pre | Kink at Jun-12 (111%), flat back-month | SELL VOL half (iron condor) | 3/5 | NO |
| 6 | UNFI | 6/9 pre | Breakout +4.8%, bullish flow 5/5, PCR 0.28; FE 1.48 blocks vol-selling | Directional bull call spread (PEAD-watch if beat) | 3/5 | NO |
| 7 | ADBE | 6/11 post | Kink at Jun-12 (93%) but bearish pre-print flow 4/5 days | SELL VOL half or SKIP — informed put-buying tell | 2/5 | YES |
| 8 | KMX | 6/17 pre | FE 1.53 — disqualified from vol-selling | Calendar only (sell Jun-18 103% / buy Jul-17 68%) | 2/5 | YES |
| — | SAIL | 6/9 pre | FE 1.33, backwardation to Dec — structural uncertainty | **SKIP** | 1/5 | NO |
| — | ACN | 6/18 pre | IV 99 clean kink BUT prints the morning after FOMC | SKIP for non-institutional desks | 3/5 | **EXTREME** |

PEAD watch (advisory, 0 pts): LULU (post-print bullish flow 3/5 days, stabilizing above $114) and UNFI (if 6/9 beat confirms).

---

## 7. Risk & Correlation (week-candidate universe)

**Correlation clusters (`uw risk portfolio-correlation`, 30d):** one cluster fires — `broad_market_index_cluster` {IWM, SPY, FCX}: IWM/SPY **0.897**, SPY/FCX 0.755, IWM/FCX 0.726. IWM kept (highest raw score 11); SPY and FCX take the −1 cluster cut. Healthcare longs (JNJ/DXCM/UTHR) show no pairwise corr ≥ 0.70 — soft watch only.

**Macro & event risk:** curve normal +0.38; core CPI 2.99% / PCE 3.29% sticky; payrolls +172k hot; USD weakening. **CPI 6/10 + PPI 6/11 + FOMC/SEP 6/16-17 + OPEX 6/19 all sit inside every name's horizon — the event gate fires on the entire book** (stacked Tier-1 prints → −1 tier universally).

**Fundamentals verdicts (top-5):**
- **DXCM — CONFIRM**: 3/4 beat streak, +16% rev / +77% EPS, dual PT raises, ADA window, D/E 0.47. Risks: FDA Class II app recall, Q4-25 guidance crater (−32%).
- **JNJ — CAUTION (−1)**: 30d net premium −$7.4M against the $164M DP block; EPS −3.9% YoY (Stelara erosion, China MedTech); thin beats (3 of 4 sub-1%); Finviz insider_trans −9.8% (advisory). The covered-call-overwrite / pension-rebalance reading explains every observed signal.
- **FCX — CAUTION (−1)**: revenue −24.2% YoY (hard flag, partially base-effects); rising Q2 production costs; insider_trans −7.3% (advisory); Street target $70.04 sits well below the GS/Citi copper euphoria.
- IWM / SPY — NA (ETFs).

**Debate-disconfirmation cuts — all five names** (bear residual ≥ bull): IWM 0.65/0.65 (tie — hedge-roll reading of the diagonal), DXCM 0.75>0.55 (bull's "cheap options" premise factually wrong — IV at 77th pctile; Jan-28 put ladder underneath), SPY 0.75>0.55 (condor = insurance, negative-EV decay), JNJ 0.75>0.65 (overwrite interpretation dominant), FCX 0.75>0.65 (shelf untested below ZGL). The debate layer did this week exactly what it exists to do: it stopped an additive-scoring book from carrying longs into a binary macro window on unproven (n=0) signal classes.

**Breadth cross-check (advisory, Finviz):** SPX advancers 237 / decliners 266, pct_green 47.1% on a red Friday — consistent with the `uw` regime read, no divergence flag.

**Adverse-flow exits (prior conviction groups):** **SMH** (PCR 3.78 + IV rank 100 + $80M DP + OI +61k — full panic stack; double-confirmed across groups), **AVGO** (−$48.8M net bearish vs W22 long), **ORCL** (event passed, flow now bearish), **MSFT** ($139M DP + net −$24.2M vs long thesis), **IWM-short carryover** (Friday DP flow bullish + PCR 1.89 — the short is crowded).

**Concentration risk + hedge sleeve:** Book is delta-flat (all watch-only). Recommended posture: **defined-risk VIX call spread ladder into FOMC** (buy Jun-17 VIX 22–24 calls / sell 28–30, 0.5–1.0% notional — mirrors the institutional 5/5-day ladder observed expiring FOMC settlement day) plus optionally a small defined-risk SPY put spread near the 720–735 put-wall zone through OPEX. **Do not short vol into FOMC week.**

---

## 8. High-Conviction Cross-Ref

**Expectancy lens (advisory — C31):** Latest calibration (2026-05-30 audit, path-aware): HIGH-tier (raw ≥9) realised 0.774 (n=31) vs MEDIUM ~0.54 — but C21 benchmark-excess shows long calls in the trailing sample were −22pp *beta* while shorts carried +20pp alpha; payoff-ratio data insufficient for a fresh per-tier expectancy line this week (no closed weekly cohort since). Display-only; the live sizer remains the Step-5 win-rate ladder. This week's asymmetry note: the only positive-expectancy expressions all week were *short/vol-up* — consistent with the C21 finding.

**No HIGH-tier names survive.** One MEDIUM:

### IWM — SHORT — MEDIUM (raw 11, demoted from HIGH) — final: watch-only
**Components:** +3 OI building 5d (puts, accumulation-hunter) | +2 multileg repeat ≥2d ($524M diagonal, conf 5/5) | +2 LEAP roll (P290 Jan-27 $340M) | +3 cum-flow 90d −$1.07B smooth bearish | +2 DEX flip short (dealer) | −1 flow_conflict_lite (30d MIXED label). Σ = 11.
**Win-rate:** 0.000 (n=2, backtest, bearish_flow proxy) — excess −0.733 vs short-SPY 73.3% ⇒ the class has been pure (expensive) beta. **Fundamentals:** NA (ETF). **Residuals:** bull 0.65 / bear 0.65 — tie, gate fires. Bear's tape work: the Friday "roll-down" was BID-near/ASK-far (mechanical hedge roll); the $340M Thursday prints were `no_side` cross-trades; Friday net put premium was −$60M (puts *sold*); PCR 1.89 = the hedge is already crowded and the pain trade is up.
**Gates:** regime PASS · VRP PASS · panic FIRE · cluster PASS (kept) · sector PASS · fundamentals NA · event FIRE · debate FIRE → −3 tiers → **watch-only**.
**Re-entry:** post-CPI failure to reclaim 292 with GEX still FULLY_NEGATIVE → bear put spread, starter, hard stop above week high. LB-gate reminder: any future HIGH-tier promotion needs ≥3 of 5 load-bearing tools — this call cites only cum-flow + DEX.

### LOW tier (all watch-only)
- **DXCM (6):** +3 OI build, +1 C11-halved accumulation, +2 confluence(5). CONFIRM fundamentals; bull 0.55 / bear 0.75. The bear's two factual contributions — IV at the 77th percentile (not "cheap"), and a building Jan-2028 $60 put ladder — must be resolved before entry. Trigger: post-ADA hold above $72.86 with the put-ladder OI flattening.
- **SPY short (6):** +3 OI build, +2 multileg condor, +2 DEX flip, −1 lite. WR 0.69 (capped, n=6, excess +0.10 — the only positive-excess class on the book). Bull 0.55 / bear 0.75; −5 tiers (VRP, panic, cluster, event, debate). The condor is the market's hedge, not our trade.
- **JNJ (5):** +3 OI build, +1 C11-halved, +2 confluence(5), −1 lite. CAUTION; bull 0.65 / bear 0.75. Flip condition: 5 consecutive sessions of positive net premium flow confirming the DP blocks are directional, not overwritten.
- **FCX (5):** +3 OI build, +1 C11-halved, +2 confluence(5), −1 lite. CAUTION; bull 0.65 / bear 0.75; **7 gates fire** (most-gated name on the book). The $63.02 shelf into a hot CPI is the specific gap risk.
- **UTHR (4):** +3 OI build (10d), +1 C11-halved. Fewest gate-fires (3); cleanest *qualitative* long (conviction-matrix 77.9%, DP 3.56) but sub-$50M flow keeps the score honest. LEAP watch 5/9, re-run 6/12.

**Dropped (≤2):** LLY (2), PGR (2), FIVE (2), KR (2), MTN (2), ORCL (2), XLE (1), MU (0), TSLA (0), NVDA (−1), QQQ (−1), AVGO (−1), TSM (−3). Mechanical flow_conflict (−3) erased every megacap short — TSLA (+$132M 30d flow against the short), AVGO (+$77M), TSM (+$35M), QQQ (+$28M): the dip-buying premium flow in megacaps is real and disqualifies fresh shorts at these levels under the rubric.

<details><summary><b>Embedded rubric (for audit)</b></summary>

```
Weekly conviction score = Σ:
  # +3 sweep-persistence line REMOVED 2026-05-23 audit P0.3 (informational only)
  +3  uw historical oi-trend BUILDING full week, --days ≥ 5
  +3  accumulation 3+ aligned signals + block-stratified institutional — C11 CONJUNCTION:
      full +3 only when cum_premium_flow_30d sign-aligned AND |cum_flow_30d| ≥ $50M; else +1.
      Sub-$50M flow that halves this line does NOT separately earn the +3 cum_flow line.
  +1  conviction-matrix DIRECTIONAL_LONG conf>70 — ONLY when dominant class == leap_directional
  +2  oi position-rolls institutional roll forward into longer-dated LEAP
  +3  cum-premium-flow net directional accretion (sharp 30d fresh / smooth 90d extension)
  +2  signal-confluence ≥4 at WEEK_END
  +2  dealer DEX flip or vanna squeeze in trade direction
  +1  sector leader CONDITIONAL (persistence ≥0.6 AND cum_flow aligned AND ≥$50M)
  +1  earnings-scout BUY/SELL VOL next 2 wks (term-skew aligned for full size)
  +2  multileg directional structure repeated ≥2 days
  +1  vol-surface KINKED/BACKWARDATION worsening WoW, iv-pctile extreme, VRP-aligned
  +1  opex-pin top-5 (OPEX week only — N/A this week)
  −2  contrarian crowded long w/ RISING pc-ratio-zscore (VRP positive)
  −3  flow_conflict (30d clearly opposite, magnitude > union median $18.0M) — XOR with −1
  −1  flow_conflict_lite (MIXED / bottom-quartile) — XOR with −3
  −2  corr cluster >0.7 (risk-monitor, 2d)
  −3  WoW regime flip conflicts with direction (risk-monitor, 2d)
Tiers: ≥9 HIGH / 7–8 MEDIUM / 3–6 LOW / ≤2 drop.
Step 3a LB gate: HIGH requires ≥3 of 5 of {block-stratified, cum-flow-30d, institutional-accumulation, DEX, signal-confluence}.
Step 5 sizing: WR ≥0.70 ×1.0 · 0.50–0.70 ×0.5 · <0.50 ×0; n<10 cap 0.69; market-excess ≤0 cap half / ≤−0.10 starter; C4 opening gate.
```
</details>

---

## 9. Setups for Next Week

**GEX advisory (SPY/QQQ only — 0 points, prose-only).** Backtest verdict first: **NO_GO_NO_EDGE** (n=78 pooled, walls-as-magnet 25.6% vs 50% — significantly *anti*-magnetic; H1 pooled runs backwards). Read what follows as dealer-structure orientation, never as edge.
- **SPY:** FULLY_NEGATIVE, total GEX −$1.81B, ZGL null (unreliable). Put wall **735** (−$283M) 0.2% below Friday's close; only positive-GEX strike 755 (+$15M, token). Dealer book amplifies both directions; a gap below 735 puts spot inside the heaviest negative cluster.
- **QQQ:** FULLY_NEGATIVE, −$934M, **no positive-GEX strike anywhere in the 0–45d grid** (no call wall). Put wall **700** (−$267M) 0.9% below spot; below it, air until ~683–685.
- Caveats: EOD book is the overnight prior (Monday's 06-08 expiry carries $420M/$503M and refreshes the map in the first 30–60 min); gap risk dominates; ETF-not-index book; D+1 expiry cannot be isolated.

**Next-session 0DTE setup (validated stack — advisory, 0 points):** backtest **GO_PREMIUM_SELL_INTRADAY** (SPY 94.9% / QQQ 92.3% open-entry win, n=39) **but the live setup says STAND ASIDE** — VIX 21.51 spiking (+6.1), size_scalar 0.0 on both indices. Rule honored: never sell the open after a VIX spike / front-end backwardation. Unsampled-tail caveat stands.

**Dealer swing setups (1–4 weeks):** Confirmed `dex_flip_short`: SPY, QQQ, IWM, AVGO, TSLA (TSLA with 3-session front-end backwardation 1.76). Imminent: MU (−$17B DEX in 5d), EEM. GEX-confirmed: TSM. Sole long: **LLY `dex_flip_long`** (+110% DEX build, stable positive GEX) — score-gated to drop (2) this week on missing OI/accumulation support; watch for those to fill in. The vanna books on all three indices are put-heavy with *rising* VIX — pressure, not squeeze; the squeeze trigger is a VIX reversal below ~18.

**Pin vs trend call:** **Trend.** Both index books are fully negative with no reliable ZGL — there is no pin to trade until OPEX week (6/19) rebuilds positive gamma somewhere. Re-assess after CPI.

**Actionable (in order of desk preference):**
1. **Hedge sleeve only:** VIX Jun-17 22–24/28–30 call spread ladder (FOMC settlement day — the institutional template), 0.5–1.0% notional.
2. **MTN long puts into Monday's print** (§6, 4/5, pre-CPI window, defined risk).
3. **KR sell-vol on 6/18** — enter *after* FOMC resolves; full-size eligible by setup quality but respect the regime.

**LOW-tier names to track for daily confirmation:** DXCM (post-ADA, $72.86), UTHR (LEAP gates, 6/12 re-run), JNJ (premium-flow flip), FCX ($63.02 shelf through CPI), IWM (292 reclaim-failure trigger).

**Deep-dive hand-off:** Skipped — no-edge week (no post-gate HIGH-tier names). If forced to queue research for next week: `/stock-deep-dive UTHR` and `/stock-deep-dive DXCM` are the two names whose theses survive the most scrutiny at the smallest gate count.

## 10. Watch-only — single signal, no confluence (journal, not trade entry)

| Name | Single source | Note |
|---|---|---|
| ISRG / TMUS / ABT | single-leg C19 (advisory) | Consecutive-day deep-ITM floor-put cluster (~$18.8M, Jun-18) — defensive-name hedging not yet in consensus; watch into OPEX |
| MSTR | single-leg C19 | $4.88M opening put 28x size/OI (6/2) — front-ran the crypto-proxy weakness |
| EWT | sector-rotation ETF tape | Taiwan calls + LEAP bids; instrument-only, no GICS gate |
| HYG | multileg | Credit-hedge diagonals (macro package leg) |
| CMG | multileg | Deep-OTM bear diagonal, Jun-18 kink, no confluence — speculative tail |
| XLE | multileg vs ETF-tape conflict | 3-day bear put spread against net ETF inflow — collar on a long book most likely |
| CTAS | contrarian | Crowded-long fade (PCR 0.895→0.12, VRP +0.085) — conflicts with sector-rotation leader status; regime-borderline |
| FSLR | vol-surface | Cleanest premium-sell surface (97th pctile, VRP +0.088) — vehicle without a directional sponsor |
| GLD | multileg (1-day) | Sep 500/550 bull call spread contradicted by −$323M 30d flow — hedge on a short gold book, not a long thesis |
| EMN, BBAR, A, PRGO, CPRI, LMND | screener confluence only | Confluence ≥5 but no Phase-1 agent sponsorship — journal only |
| MSFT | sweeps (informational) | Bearish sweep persistence + $139M DP + 1 Tier-1 put; adverse-flow exit fired on prior-week long |

---
*Generated 2026-06-05 EOD by /weekly-analysis (11-agent Phase 1 fleet + 4-stage Phase 2). Data: `uw` CLI (EOD parquet through 2026-06-05), FRED, Finnhub, Finviz (`fz`, advisory lanes). All sizes post-gate. The decision envelope sits beside this file as `decision.json`.*
