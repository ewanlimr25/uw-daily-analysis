# Weekly Market Intelligence — Week of 2026-08-10 (ISO 2026-W33)

## Executive Summary

- **Week regime + WoW Δ:** TRANSITIONAL **held** Monday to Friday, `trend` UPTREND at both ends, SPY above both SMAs all week, flow breadth frozen at 34.9% → 35.1% bullish. The index barely moved — SPY **+0.40%** (773.03 → 776.34), QQQ +1.11%, IWM +1.17%, VIX 15.46 → 14.25. That calm is the least interesting fact about the week. The **netted sector rotation flipped hard** (Technology −$279.9M largest-outflow Monday → +$40.5M largest-inflow Friday; Healthcare and Utilities also sign-flipped), and underneath it ran a violent **intra-Technology dispersion**: NBIS +47.7%, SNDK +35.4%, STX +19.8%, MU +10.7% against AVGO −8.1%, APP −9.0%, AMAT −5.9%. VRP is **negative** (QQQ −0.0506 PREMIUM_BUYING, SPY −0.0073 FAIR) — a premium-**buying** tape, with realised vol 12.5% on SPY against 23.2% on QQQ.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`.
- **Signal performance:** **2 of 6 resolved (hit rate 1/2 = 50%); 4 INCONCLUSIVE excluded; 6 total non-DROP calls in universe (6 envelope-anchored, 0 reconstructed); 41 total calls, 35 DROP.** A denominator of two carries almost no information. The one WIN — **NBIS long, called 08-11 at $193.23, closing the week at $277.68 (+43.70%, +6.10×ATR)** — was sized `skip`.
- **Top swing build for next week:** **None.** Nothing reached MEDIUM or HIGH for a **ninth consecutive cycle**. Five names scored LOW; the two carrying a `starter` (SNDK, NBIS) were cut by fundamentals CAUTION *and* the debate gate; the two shorts (IWM, AVGO) route to `watch_only` by policy; SPY has no direction to size.
- **Top LEAP build:** **None.** Zero candidates cleared Gate 4 (cum-flow accretion), let alone 6-of-9. `biggest-increases --min-dte 180` returned 20 rows, **all ETF/index** — no single-stock LEAP build exists in the screen at all, against a market-wide LEAP share decaying 3.9% → 3.3%.
- **Biggest emerging risk:** **the scoring substrate, not a position.** The **+3 OI line was the sole source of points on 8 of 8 names**, saturated at a **100% population firing rate** across both the 5d and 10d windows, with put-heavy ≤7DTE composition on names whose thesis is long (MU 60.9% put, STX 54.0% put; SNDK and MU 78% inside 7DTE). Strip that one line and the entire week's book scores between −1 and +3. Compounding it, **`win_rate` is `NA(substrate)` on all eight** — `oi_build` and `multileg_directional` are not backtestable classes and `dark_pool_accumulation` returned **zero rows market-wide** — so the sizing ladder was bypassed by the tier-default path on 100% of rows. Runner-up: the **long lane had no measured edge over the index** (`bullish_flow` 0.4848 vs a 0.5758 SPY-long benchmark, −9.1pp), while the only lane with positive excess (`bearish_flow`, +9.0pp) is the one routed to `watch_only` by policy.

> **The 21st consecutive empty conviction board.** Two things make this week different from the last twenty. First, the empty board was **not** obviously correct: the fleet found NBIS at $193.23 on 08-11, scored it, and declined to size it — and it closed the week +43.7%. Second, for the first time the *reason* the board is empty is legible and mechanical rather than atmospheric: one saturated rubric line is carrying every score in the book, and the backtest substrate cannot price a single one of this week's dominant signal classes.

---

## 0. Week in Review — Intra-Week Signal Performance

**Universe:** the union of `calls[]` across the week's five daily `decision.json` envelopes — the only hindsight-free record of what was actually committed. All five envelopes exist, so **nothing was reconstructed**. **41 total calls; 6 non-DROP.** Resolution runs from each call's own envelope date forward to 2026-08-14, graded at 0.5 × ATR(14) measured as-of the call date.

### Primary scorecard — non-DROP calls

| Ticker | Direction | Source | Move vs ATR | Flow/OI | Grade | Note |
|---|---|---|---|---|---|---|
| **NBIS** | long | envelope 08-11 | **+43.70%, +6.10×ATR** | 5d cum-flow +$95.3M; OI BUILDING (saturated) | **WIN** | Sized `skip` at raw-3 LOW. The largest miss-by-not-sizing in the book's history. |
| **MSFT** | long | envelope 08-10 | −2.11%, **−1.18×ATR** | 5d cum-flow +$33.4M — *bullish against a losing long* | **LOSS** | Sized `watch_only`. Thesis was DP accumulation; §7 shows that read was closing-cross contamination. |
| EWY | long | envelope 08-12 | +2.20%, +0.82×ATR | 5d cum-flow +$22.6M | INCONCLUSIVE | Below the 0.5×ATR threshold. |
| CRWV | long | envelope 08-13 | −0.97%, −0.23×ATR | 5d cum-flow +$112.6M | INCONCLUSIVE | Below threshold. |
| LULU | short | envelope 08-14 | 0.00%, 0.00×ATR | — | INCONCLUSIVE | Zero forward sessions (called on week-end). |
| ROST | vol_short | envelope 08-14 | 0.00%, 0.00×ATR | — | INCONCLUSIVE | Zero forward sessions. |

**Headline: 2 of 6 resolved (hit rate 1/2 = 50%); 4 INCONCLUSIVE excluded; 6 total non-DROP in universe (6 envelope-anchored, 0 reconstructed); 41 total calls, 35 DROP.** Every call was `skip` or `watch_only`, so **realised book P&L is exactly zero** for the 21st consecutive week.

**The NBIS miss deserves to be stated plainly rather than buried in a denominator.** It was surfaced, scored, debated in miniature and dropped — and it then delivered a 6.10×ATR move, the largest single resolved move the scorecard has recorded. It is one name and the honest statistical read is that n=2 tells us nothing. But it is also the exact failure mode the empty-board discipline is supposed to be *paying* for: the discipline is defensible only if the DROP pile keeps under-performing, and this week it did not by much (below).

### Supplementary — DROP-pile discipline check (30 directional calls, 14 resolved)

Not part of the formal scorecard; it grades what the desk *declined* to trade, the way `/calibration-audit` does.

| Metric | Result |
|---|---|
| All directional | 5W / 9L = **35.7%** (n=14 resolved) |
| DROP-only | 4W / 8L = **33.3%** (n=12 resolved) |
| Non-DROP | 1W / 1L = 50.0% (n=2 resolved) |

**This week inverts the usual pattern** — for six straight audits the DROP pile out-performed the traded book; here the (unsized) non-DROP book edged it, 50% vs 33.3%. On n=2 against n=12 that is noise, not a regime change, and it should not be read as the rubric starting to work.

The DROP pile's worst calls were **shorts into the memory melt-up**: MU short (08-11) **−2.63×ATR**, NVDA short (08-11) −1.98×ATR, SE long −3.96×ATR, INTC short −1.34×ATR, META short −1.01×ATR. The short-routing policy kept every one of them at `watch_only` — which is the policy working exactly as designed, and is worth setting against the NBIS miss on the other side of the ledger.

---

## 1. Regime & WoW Delta

The regime **label held**: TRANSITIONAL with `trend` UPTREND at both ends, SPY above its 20SMA (756.20) and 50SMA (748.93) all week, and flow breadth essentially frozen at 34.9% → 35.1% bullish. Underneath, the index barely moved — SPY 773.03 → 776.34 (**+0.40%**), QQQ +1.11%, IWM +1.17%, VIX 15.46 → 14.25.

**What actually moved was the netted sector rotation, and it flipped hard.** Monday's netted `market-regime.sector_rotation` had Technology as the single largest *outflow* at **−$279.9M**; Friday's had it as the single largest *inflow* at **+$40.5M**. Healthcare flipped +$26.3M → −$18.9M, Utilities −$24.7M → +$4.1M, and Consumer Cyclical became the dominant outflow at −$118.8M. Two data points do not make a rotation — and §2 shows the instrument-level tape refuses to confirm it.

**Two Step-0 measurement caveats, both material:**
- The `spy` sub-block of `uw risk market-regime` returned **776.34 for both the 08-10 and 08-14 dated calls** — it is a live snapshot, not date-pinned. SPY's actual 08-10 close was **773.03**. No WoW SPY delta can be read off that tool.
- The netted `sector_rotation` field is a **top-3/bottom-3 truncation of 11 sectors**, available here for only two of five sessions. "Not listed" ≠ "flat". The ≥3-day persistence bar a rotation call requires is structurally unmeetable from this source.

**VRP: negative, and asymmetrically so.** QQQ −0.0506 (IV30 18.17% vs realised 23.24%) is a decisive **PREMIUM_BUYING** read; SPY −0.0073 (11.76% vs 12.49%) is FAIR. The SPY-vs-QQQ realised gap — **12.5% against 23.2%** — is the whole story: dispersion is concentrated in the Nasdaq complex, not the index. Every short-premium structure in this note is fighting the vol regime, and that is stated wherever one appears. It also aborts contrarian-scanner's fade lane outright for the third consecutive week.

**DTE mix deteriorated into the weekend.** 0DTE share ran 16.1% (Mon) → 18.3% (Wed) → **45.8%** (Fri), flipping the regime hint to RETAIL_DRIVEN, while LEAP share decayed 3.9% → 3.3%. Friday is a weekly-expiry day so part of the spike is mechanical, but the direction is unambiguous: the marginal participant got shorter-dated all week. Every Friday-dated signal in this note is weighted down accordingly.

**Macro backdrop — stagflationary tilt.** Core PCE **3.29% YoY** sits above target *and* above core CPI (2.79%) — the stickiness is services-led. Against that, payrolls printed **−23k MoM**, outright contraction, with unemployment at 4.1%. Fed funds 3.63%, 10Y 4.63% and flat, curve normal at +0.51, USD weakening. Growth cracking while inflation is unfinished is the least accommodating backdrop for a Fed-pivot trade, and it raises the bar on every long-duration, high-multiple thesis in the book — §4 is empty partly for this reason.

**Breadth cross-check (advisory, `fz`):** 250 advancers / 245 decliners, **49.7% green, median member change 0.00%**, while SPY sits −0.39% from its 90-day high. Divergence flagged. The index is being carried by a narrow cap-weighted cohort; read this week's green tape as **rotation, not participation**.

**Implication for next week:** an unchanged regime label, a genuinely negative VRP, a retail-skewing DTE mix and the §7 event wall together argue for long-optionality, defined-risk expressions — and against anything that sells premium or requires a durable trend.

---

## 2. Sector Rotation

**Rotation regime call: `no_change`, confidence LOW.** No canonical macro pattern (defensive→cyclical, cyclical→defensive, growth→value, value→growth) is satisfied. The week's one real, price-and-flow-confirmed persistent move is **not a GICS rotation at all** — it is a violent **intra-Technology dispersion** that the netted sector aggregate actively conceals.

**The direction source is thin and the durability source is broken.** `options-flow sector-flow-persistence` returned `trend: INFLOW` with `persistence_score: 1.0` for **11 of 11 sectors** — zero discrimination. It and `sector-flow` are **one gross-turnover source** (identical values; `net_flow` = gross call$ − put$, sign-agnostic), so they cannot express direction and cannot corroborate each other. Direction therefore comes only from the netted `market-regime.sector_rotation`, which exists for two of five sessions and is top-3/bottom-3 truncated. Because gross printed positive for all 11 sectors, it **mechanically agrees with every netted "IN" and disagrees with every netted "OUT"** — which forces all four `rotating_out_of` sectors to `watch_only` by rule, independent of judgment.

| Sector | Netted Mon | Netted Fri | Gross (Fri) | Agreement | Verdict |
|---|---|---|---|---|---|
| Technology | −$279.9M OUT | **+$40.5M IN** | +$3,114.6M | agree | Sign-flipped mid-week; two points only — **not a durable sector call** |
| Financial Services | +$37.4M IN | +$24.5M IN | +$344.8M | agree | Only same-sign sector at both endpoints — but its ETF disagrees |
| Utilities | −$24.7M OUT | +$4.1M IN | +$36.1M | agree | Sign-flipped; magnitude trivial |
| Consumer Cyclical | — | −$118.8M OUT | +$652.4M | **disagree** | watch_only |
| Industrials | — | −$48.8M OUT | +$338.6M | **disagree** | watch_only |
| Healthcare | +$26.3M IN | −$18.9M OUT | +$251.8M | **disagree** | Flipped *and* disagrees — weakest read of the week |

### The real story: memory/storage vs AI-infra, inside Technology

Persistent across five sessions and confirmed from four independent angles:

- **Price (5d):** NBIS **+47.7%**, SNDK **+35.4%**, STX **+19.8%**, MU +10.7%, LRCX +6.8%, AMD +6.4% — against APP **−9.0%**, AVGO **−8.1%** (−5.94% Friday alone, worst S&P member), AMAT −5.9%, MSTR −7.0%.
- **Friday sector-filtered screener:** bullish Technology = SNDK, AMD, MU, STX, LRCX; bearish Technology = AVGO, APP, AMAT. Clean overlap with the price split.
- **ETF instrument tape:** **IGV (software) is a clean, persistent BEARISH outflow (−$13.9M)** whose top sweeps are **bid-side call *selling*** — a distribution signature, not a crash hedge. **XLK itself is net-negative and MIXED.**
- **Geographic confirmation:** **EWY (Korea — Samsung/SK Hynix)** is a clean multi-day **BULLISH** inflow (+$22.6M), corroborating the memory thesis from outside the US options tape.

**The single most important finding of the week: every GICS "IN" read fails its own instrument-level cross-check.** Technology says IN while XLK is negative/MIXED; Financial Services says IN while KRE is −$1.3M BEARISH. The netted Technology inflow is an artifact of netting a strong memory/hardware bid against a real software/AI-infra sell. **Any "Technology" call must name which side of the split it sits on**; a sector-level read is worse than useless here.

**ETF flow tape (advisory — 0 rubric points)**

| ETF | Net flow (5d) | Trend | GICS | Agreement | Deep-pull |
|---|---|---|---|---|---|
| SMH | +$28.1M | MIXED | Technology | weak agree | DP aggressive buy late; sweeps mixed, no clean skew |
| **EWY** | **+$22.6M** | **BULLISH** | n/a (Korea) | n/a | $52M DP print below mid; one clean Sept call-buy $3.9M |
| XLE | +$7.8M | BULLISH | Energy | n/a (no Fri read) | DP top print aggressive buy; sweeps 3/3 calls, 2 ask-side, near-dated — genuine urgency |
| XLI | +$3.5M | BULLISH | Industrials | **disagree** | — |
| XOP | +$3.2M | BULLISH | Energy | n/a | — |
| KRE | −$1.3M | BEARISH | Financials | **disagree** | — |
| XLK | −$3.3M | **MIXED** | Technology | **disagree** | — |
| XLY | −$6.4M | BEARISH | Cons. Cyclical | agree | Sweeps thin (3 prints, `no_side`) |
| **IGV** | **−$13.9M** | **BEARISH** | Technology | agrees w/ split thesis | **Top-2 sweeps are bid-side call SELLING — distribution** |
| GDX | −$15.9M | BEARISH | Basic Materials | n/a | Contradicted by one $28.2M aggressive DP *buy* — inconclusive |

**Energy is the week's blind spot.** XLE **+7.67%** and USO **+7.31%** made Energy far and away the best-performing sector, with Friday gross flow spiking to **$1,311.9M** — second only to Technology and 6–17× its Mon–Thu run-rate of $77–224M — plus genuinely urgent ask-side near-dated call sweeps. Yet Energy appears in **neither** netted top-3 list on Friday, a direct consequence of the top-3 truncation. The only C12-passing Energy single name, XOM, is on Friday's *bearish* list. Flagged as a leader/ETF conflict, not a call.

**Conviction overlay:** Friday's 0DTE share at 45.8% (RETAIL_DRIVEN) downgrades rotation conviction uniformly — and specifically taints the Friday netted snapshot that is one of only two direction reads available.

---

## 3. Swing Book (1–6 weeks) — ranked by weekly conviction score

**Five names cleared the confluence gate and scored ≥3; three dropped below the floor. Nothing reached MEDIUM (≥7) or HIGH (≥9) — the ninth consecutive cycle in which the post-freeze bands are structurally empty. After the gate stack, the book is FLAT: zero sized positions.**

**The finding that should govern how this table is read.** The **+3 OI line was the sole source of points on 8 of 8 names**, and it is saturated — `consecutive_build_days == --days` at *both* the 5-day and 10-day windows on every name, a 100% population firing rate extending C47's 6-of-6 to 8-of-8. Worse, its *composition* contradicts the theses it pays for: MU's build is **60.9% put-side** and STX's **54.0% put-side** on nominally LONG theses, and SNDK and MU are **78% inside 7DTE**. **Strip that one line and this entire week's book scores between −1 and +3.** It is the only thing holding five names above the drop floor.

**Second, equally uncomfortable:** the long lane had **no measured edge over simply being long the index**. Under the clean-query protocol `bullish_flow` realised **0.4848 (n=132)** against a same-window SPY-long benchmark of **0.5758** — **−9.1pp**, a tenth of a point from the C2 starter trigger. Six of eight names are long. The short lane realised **+9.0pp excess** — and both shorts route to `watch_only` by policy.

**Win rate is `NA(substrate)` on all eight, for a structural reason.** `signal-backtest` supports five classes; `oi_build` and `multileg_directional` — the dominant classes of every name here — are not among them, and `dark_pool_accumulation` returned **zero rows market-wide**, independently corroborating accumulation-hunter's empty board from a second substrate. The sizing ladder was bypassed by the tier-default path on 100% of rows.

### 3a. Long swings

| Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure | Invalidation |
|---|---|---|---|---|---|---|---|
| **SNDK** | LOW | 3 | `NA(substrate)` | **skip** (4 gates fired) | Mechanized DEX flip long fired 08-12 (ratio 2.52, whipsaw FALSE) and **held and grew ~9×** to +$12.20B; price 1212→1641 with net flow inflecting on exactly the flip date; 4/4 EPS beats, +175.3% YoY revenue, JPMorgan $2,250 PT. IV *fell* as price ripped (0.925→0.829). | Would have been a defined-risk debit call spread; **not taken** | Below the **$1,630** DP shelf — *not* the $1,641.11 top print, which is the closing cross ($633.3M in 42 trades at the exact close). Or DEX reverses ≥3 sessions. |
| **NBIS** | LOW | 3 | `NA(substrate)` | **skip** (5 gates fired) | The only name genuinely earning the vol line — front-end ratio **deepened 1.178 → 1.215** at the clean 7DTE read, the deepest and only *worsening* backwardation in the set, VRP-aligned. Growth is extraordinary (+488% YoY, 4/4 beats with narrowing losses, $40B backlog, Citi PT $324); GEX flipped NEGATIVE→POSITIVE 08-12. | Would have been long vol / defined-risk; **not taken** | Below the **$272** DP shelf (not the $277 closing-cross-adjacent print); or institutional-accumulation stays NEUTRAL/DISTRIBUTION another week; or the 250C/190C closures fail to reverse into fresh opening size. |

⚠ **NBIS carries a live C28 `distribution_flag`** — verified directly: the two largest OI decreases are **08-21 (7DTE) CALLS being closed, 190C −2,161 and 250C −775**, both deep ITM against a $277.68 spot, distinct from the 0DTE rows which are mechanical expiry. Institutional profit-taking into a +47.7% melt-up. Advisory, 0 points, no size change — but it is the clearest chase-not-accumulation tell in the book.

⚠ **SNDK's premium tape is triply contaminated** (verified independently): its top two tickets are a **same-strike $900 calendar roll** — $108.0M ask (Aug-28) against $107.6M bid (Aug-14), both delta ~0.99, i.e. **$215.6M of gross premium representing ~$0.4M of directional intent**; it carries **bid-side deep-ITM put sales** (2028 1500P $28.1M, 2027 2750P $14.2M) that the netting convention books as *bullish*; and its flow shows **two incompatible strike grids at the same 2026-12-18 expiry** (120/330 alongside 900–3520 on a $1,641 stock) — an un-split-adjusted grid artifact.

### 3b. Short / fade swings — routed, not suppressed

Both shorts route to **`watch_only`** under the 2026-08-01 P0 #1 policy, applied before the win-rate ladder and instrument-agnostic. This is **routing, not suppression**: theses, structures and invalidations are printed, the full 9-key `gate_verdicts` is recorded, and both serialize into `decision.json` so the counterfactual keeps resolving.

| Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure | Invalidation |
|---|---|---|---|---|---|---|---|
| **IWM** | LOW | **6** | `NA(substrate)` | **watch_only** (SHORT-ROUTING) | Top of the book and the only name whose evidence is internally consistent across three independent tools: a 295P calendar (08-12) rolling into a 289/290P Sep18 vertical, **visible directly in the OI tape** (289P +38,016 on 08-14, 288P +36,467 and Sep04 295P +67,185 on 08-13), sitting on a standalone **−$105.4M negative-gamma wall at 295**, backed by the **only non-MIXED cum-flow read in the union** (−$271.3M, −5.16% of gross, sign-consistent at 90d) and 8 bearish flow days of 10. | Sep18 289/290P debit vertical (defined risk, VRP-aligned) | Reclaims and holds above ~295 through OPEX week; or the 289/290P cluster is not rolled forward; or the dealer book's long-gamma build at 305 persists while put OI stops growing. |
| **AVGO** | LOW | 3 | `NA(substrate)` | **watch_only** (SHORT-ROUTING) | The cleanest mechanized flip in the book: **eleven consecutive positive DEX sessions** then a decisive −$938.5M print clearing the magnitude floor (ratio 1.17, whipsaw FALSE), corroborated by a GEX regime flip **three sessions earlier on 08-10** — dealer positioning turned *before* the headline. Worst S&P performer of the week inside a cohort that sold together. fundamentals **CONFIRM**. | Defined-risk put spread | DEX reverses positive ≥3 sessions; or cum-flow breaks bullish above the $37.9M noise floor; or the 09-02 earnings print re-rates it on still-excellent operating metrics. |

**The unresolved conflict on IWM is the most interesting thing in the book.** `dealer-positioning-strategist` reads the dealer book building **LONG** all week — DEX +$8.34B → **+$11.26B**, `total_gex` to **+$1.17B** (the highest print of the window), regime POSITIVE throughout, with a **+$921.3M long-gamma wall at 305**, essentially at spot. **Both debate advocates independently concluded the put ladder most plausibly reads as insurance on a long book rather than fresh net-short conviction** — including the bear, whose job was to defend the short. A 289/290P vertical 4–5% OTM into monthly OPEX with Jackson Hole the same day, bought at the cheapest IV rank of the three indices (1.1), is the shape a long book buys, not a fresh directional bet.

### 3c. Not carried — SPY

**SPY scored 3 but is not a trade.** Its `repeat_count 2` counts **two different, opposite-signed structures**, not one directional structure repeated: a 1:2:1 put-fly tail-hedge ladder 26–38% OTM, and a tactical 780/78x call vertical rolled into the 08-21 tenor. The quant explicitly declined the +2 multileg line on those grounds — netting them would fabricate a direction no book in the tape holds. Carried as §9 structural context.

**The ladder is verifiable in the OI tape, and it is the single largest OI event in the index this week:**

| Date | Expiry | Wing | **Body** | Wing | Width |
|---|---|---|---|---|---|
| 08-13 | Oct 30 | 470P +75,000 | **570P +149,941** | 670P +75,000 | 100 |
| 08-13 | Nov 20 | 400P +74,998 | **520P +150,008** | (640P) | 120 |
| 08-14 | Dec 18 | 350P +150,046 | **480P +300,046** | 610P +150,051 | 130 |

Exact 1:2:1 ratios across three expiries, rolled on consecutive sessions, with **body strikes descending (570 → 520 → 480)** and **wings widening (100 → 120 → 130)** — a systematic programme buying progressively deeper and wider downside convexity while the index grinds to within 0.39% of its 90-day high.

### 3d. Dropped below the floor

| Ticker | Score | Why |
|---|---|---|
| **MU** | 2 | The saturated OI line actively argues *against* the long: **60.9% put-side, 78% inside 7DTE**. Net-30 +$684.9M is **1.03% of gross — thinnest in the set**, thinning to 0.19% at 90d. DEX correctly **failed as a level, not a flip** (the exact P0.4 error the mechanization exists to catch). Sharpest conflict in the union: sweep-tracker reads **bearish persistence 5-of-5 against a +10.7% week**, while sector-rotation and vol-surface read long — and the week's dailies called MU short twice into +11.88% and +2.30%. |
| **STX** | 2 | +$17.9M is the **smallest \|net30\| in the union** (0.51% of gross), below both the bottom-quartile cut ($37.9M) and 25%-of-median ($52.1M). The sector-leader line fails on two independent gates — the $50M floor is missed by nearly 3× on its own merits. Otherwise the *healthiest* of the melt-up cohort (price-vs-flow aligned, fragility z −1.117), but "least fragile in an extended cohort" is not a thesis. |
| **AMD** | 2 | The cleanest illustration of why the removed lines matter: its best evidence is sweep-tracker's **bullish 5-of-5 single-direction persistence**, and that line was deleted on 2026-05-23 after two consecutive audits measured it negative. Flow is bearish-signed at 30d (−$47.2M) *against* the long, and **sign-flips to +$39.9M at 90d**. Least extended of the cohort (+6.4% 5d) — a real point on entry risk, but not a scored one. |



## 4. LEAP Book (6–24 months)

**Empty. Zero candidates cleared Gate 4 (cum-flow accretion), let alone the required 6-of-9.**

`uw oi biggest-increases --min-dte 180` returned only **20 rows, every one an ETF/index product** — no genuine single-stock LEAP build appears in the primary screen at all this week. After intersecting with the liquidity floor the entire candidate set is QQQ, GLD, FXI, MSTR (plus XLU/KWEB surfacing marginally in `position-rolls`).

| Ticker | 30d net flow | 90d net | Verdict |
|---|---|---|---|
| MSTR | −$136.9M MIXED | **−$504.9M** MIXED | FAIL — wrong-direction over 90d |
| QQQ | −$223.3M MIXED | +$51.2M on $177B gross (**0.03%**) | FAIL — dead flat, no accretion signature |
| GLD | −$251.1M MIXED | **−$330.2M** MIXED | FAIL — wrong-direction over 90d |
| FXI | +$32.7M BULLISH | −$15.3M MIXED | FAIL — 30d blip unbacked by 90d; neither fresh-thesis nor thesis-extension shape |

**No name shows rolls recurring on ≥2 of the five covered dates** — there is no multi-week roll-forward persistence anywhere in the week's data, independently corroborating the Gate-4 verdict. MSTR's single 08-12 roll had `balance_ratio` 0.135 with far-OI change (+50,634) dwarfing roll size (6,837) — fresh OI, not a roll-forward. XLU (08-13) and KWEB (08-14) were single-date spikes, and KWEB's was put-side, the wrong side for a directional-long LEAP.

**Two contextual reasons this is the expected result, not a scan failure:** market-wide LEAP share **decayed all week** (3.9% → 3.3%) while 0DTE share tripled — the marginal long-dated participant is not present in single names; and the **stagflationary macro** (core PCE 3.29% above core CPI 2.79%, payrolls −23k) is the least accommodating backdrop for the longest-duration expression in the book. Gate 1 (`oi-trend --days 10`) returned `consecutive_build_days == 10` on **4 of 4** names — saturated at the ceiling, non-discriminating, unusable for ranking (C47).

---

## 5. Volatility Surface — WoW Term Structure & Skew Evolution

**Method note first, because it changes the answer.** Both snapshots (08-10 and 08-14) were run through `scripts/term_structure_hygiene.py` before differencing. This is not optional here: **08-14 is a weekly-expiry Friday with 45.8% 0DTE share**, so an unfiltered WoW comparison measures which day you sampled, not the surface. Raw labels flipped under hygiene on **7/12 names at 08-10 and 8/12 at 08-14** (raw-vs-`shape`); on the stricter raw-vs-`base_shape` test, 4/12 and 6/12.

**Correction to the standing expectation:** nothing in the basket went NORMAL/CONTANGO → BACKWARDATION this week. On cleaned `base_shape` the movement ran the **other way** — names came *out* of genuine backwardation: **QQQ**, **AMAT** and **AVGO** all BACKWARDATION→CONTANGO, **LRCX** BACKWARDATION→FLAT, **MU** FLAT→CONTANGO. Held genuinely backwardated at both ends: **NBIS, SNDK, STX, APP** — and NBIS is the only one *deepening* (front_end_ratio 1.178 → **1.215**).

| Ticker | base 08-10→08-14 | kink expiry | front_end_ratio (7DTE) | skew @~98DTE |
|---|---|---|---|---|
| SPY | CONTANGO → CONTANGO | 08-18 → **08-21** | 1.002 → 0.782 | 1.415 → 1.426 **TAIL_HEDGING** |
| QQQ | **BACKWARDATION → CONTANGO** | none → **08-19** | 0.944 → 0.979 | 1.234 → 1.250 **TAIL_HEDGING** |
| NBIS | BACKWARDATION (deepening) | 09-18 → none | 1.178 → **1.215** | 0.973 → 0.978 COMPLACENT |
| SNDK | BACKWARDATION (flat) | none | 1.154 → 1.150 | 0.994 → 0.991 COMPLACENT |
| STX | BACKWARDATION (cooling) | none | 1.090 → 1.080 | 1.006 → 0.985 COMPLACENT |
| MU | FLAT → CONTANGO | 08-21 → **08-21** | 1.297 → 1.184 | 0.989 → 0.950 COMPLACENT |
| AMD | CONTANGO → CONTANGO | 08-28 → **08-21** | 1.057 → 1.060 | 0.974 → 0.971 COMPLACENT |
| AVGO | **BACKWARDATION → CONTANGO** | 08-21 → **08-21** | 0.863 → 0.823 | 1.013 → 1.012 COMPLACENT |
| APP | BACKWARDATION (cooling) | none | 1.104 → **1.060** | 1.003 → 0.979 COMPLACENT |
| LRCX | **BACKWARDATION → FLAT** | — | 1.170 → 1.174 | 1.004 → 0.984 COMPLACENT |
| AMAT | **BACKWARDATION → CONTANGO** | 09-18 → 08-28 | 1.300 → 1.107 | 0.997 → 0.964 COMPLACENT |
| MSTR | CONTANGO → CONTANGO | 08-28 → 09-04 | 1.009 → 0.920 | 1.004 → 0.989 COMPLACENT |

**The load-bearing finding: by 08-14 the kink converges on 2026-08-21 across SPY, QQQ, MU, AMD and AVGO** — five independent names' term structures pointing at the same date, precisely the FOMC-minutes / monthly-OPEX / Jackson-Hole-opening stack. Cross-checked against the earnings screen: **none** of these names report in that window, so the kink is unambiguously macro-event-driven. That convergence is corroborated from a completely different tool by the multileg tape — SPY's 780C vertical was *rolled into* the 08-21 tenor and IWM's 295P calendar has its front leg *at* 08-21.

**Skew:** only SPY and QQQ show real **TAIL_HEDGING** (1.426 / 1.250, stable-to-rising) — genuine index-level hedging demand. **Every single name reads COMPLACENT** (call side richer than put side) at both ends. NBIS carries the most negative skew of all — call-rich complacency stacked on a +47.7% five-day melt-up is a lottery-composite signature (advisory colour only).

**IV percentile — all PROVISIONAL.** Every ticker returned **`dates_used: 87`** against a 252-day request, below the ≥120-day first-class bar. With that caveat: the memory/HBM complex reads **LOW_IV / bottom-15th-percentile on a relative basis** despite enormous absolute IV — NBIS 97.5% IV at the 13.8th percentile (z −0.853), SNDK 82.9% at the 0th (z −1.583), MU 62.7% at the 1.2th (z −1.977), STX 71.9% at the 4.6th. Raw IV rank would scream "sell vol"; the outlier-robust percentile says the surface is cheap against its own recent history. AVGO (41.4th percentile) is the only name near the middle of its own distribution — the least dislocated, consistent with its base_shape resolving to plain CONTANGO.

**Front-end-iv population firing rate:** at the mandated `--near-dte 7`, **8/12 (66.7%)** fire above 1.05, and they split correctly — index/AVGO/MSTR calm (SPY 0.782, QQQ 0.979, AVGO 0.823, MSTR 0.920) against the memory/capex complex elevated. Materially better-behaved than the CLI default `--near-dte 1`, which fired 8-of-9 on 2026-08-13 while SPY/QQQ printed CONTANGO. **Read at 7, always.**

**Calendar candidates** (persistent backwardation + falling front ratio, no catalyst): **APP** is cleanest (1.104 → 1.060, panic resolving, no earnings in 14 days); **STX** secondary and thinner; **SNDK** borderline. **NBIS is explicitly disqualified** — its front ratio is *rising*, so the backwardation is still event-driven and not resolving. Do not fade it.

**VRP-aligned structural recommendation: long vol / dispersion.** Negative VRP, bottom-decile relative IV percentiles, and violent realised vol (rv20: NBIS 183.5, SNDK 149.8, MU 101.5, STX 80.2) against an 11.8% SPY IV30 all point the same way. The structurally indicated expression is **long single-name vol in the memory/HBM complex against short index vol**, sized around the 08-21 event wall — with the explicit caveat that the short-index leg is the *relative* leg of a dispersion trade, not a standalone short-vol conviction call.

---

## 6. Earnings — Recap & 2-Week Lookahead

**Substrate defect, reported before the content because it removes this section's primary ranking axis:** `uw insights analyst-vs-flow` returned **no analyst block on 0 of 21 tickers tested** — the payload is exactly `{options_flow, symbol}`, verified independently on HPQ/AAPL/NVDA. The tool is half-implemented relative to its own name, which makes the command's "analyst-vs-flow disagreement is the highest-EV setup" instruction **structurally unexecutable**. The lookahead below is ranked by confirmed-kink + back-month-skew alignment instead. A null payload is *unmeasured*, never "no divergence."

Two further hygiene notes: `implied_move` figures below are **IV-derived** (front IV × √(DTE/365)), not the CLI's native field, which is pinned to a sub-1-day horizon and runs ~8–16× too small. And `earnings_vol` is **not a supported `signal-backtest` class**, so every verdict here is a structural read with `win_rate: NA(substrate)`, capped at 0.55 by the 2026-08-01 ceiling regardless.

### (a) Recap — what printed this week

| Ticker | Pre-event flow | Implied | Realised | IV crush | Grade |
|---|---|---|---|---|---|
| **NBIS** (08-12) | near-neutral, P/C 0.89 | 11.0% | **+34.1% day-of, +47.7% 5d** (~4× implied) | **None** — IV held 0.97–1.10 as realised outran it | **Massively CONFIRMING for BUY VOL; catastrophic for SELL VOL.** Any short-vol seller was destroyed. |
| **AMAT** (08-13 pm) | put-heavy, P/C 1.43 | 7.3% | −5.1% day-of / −5.9% 5d, **despite an EPS beat** (guidance/margin sell-the-news) | Clean: iv_rank 62.9 → 36.7 | **CONFIRMING** — move inside the implied range, IV crushed, bearish-tilted flow called direction. Clean SELL VOL win. |
| **LITE** (08-11) | put-heavy, P/C 1.87, bearish-tilted | 9.9% | **+13.9%** | Partial only (iv_rank 64.8 → 47.5) | **DISCONFIRMING on direction** (bearish flow, stock ripped); **CONFIRMING for BUY VOL** — realised blew through implied. |

**Correction worth recording: AVGO's −5.94% Friday / −8.1% week was NOT an earnings reaction.** Its next print is 2026-09-02 (19 days out). The move was a BofA note flagging AI-chip-financing risk plus Third Point dissolving its stake. It must not be coded as an earnings-vol event downstream.

### (b) Lookahead — 2026-08-17 → 2026-08-28

**Population firing rate on `front_end_ratio` at 7DTE: 10/18 (55.6%) — and it splits purely on days-to-earnings, not richness.** All nine names reporting in 4–6 days fire (their 7DTE tenor *is* the earnings tenor, so nothing else is arithmetically possible); all nine reporting in 11–13 days do not. Read the ratio as "event inside 7 days," not "market panicked."

**Week-2 cohort — the genuine kink test, and where the signal is:**

| Ticker | Earnings | Kink @ 08-28 | Back-month skew | Implied | Verdict |
|---|---|---|---|---|---|
| **HPQ** | 08-26 pm | **11.4%** ✓ | **TAIL_HEDGING** 1.103 | 13.8% | **SELL VOL — FULL SIZE.** Front kink at the correct tenor *and* back-month stretched alongside it. Cleanest name in the scan. |
| ZM | 08-25 pm | **16.9%** ✓ (strongest) | COMPLACENT 0.961 | 12.7% | SELL VOL — half. Textbook front-only disqualifier: best kink shape, zero back-month confirmation. |
| INTU | 08-25 pm | 11.2% ✓ | COMPLACENT ~flat | 12.8% | SELL VOL — half. Front-only. |
| SNPS | 08-26 pm | 9.6% ✓ | NORMAL 1.068 (leaning) | 11.6% | SELL VOL — moderate. |
| CRWD | 08-26 pm | 7.7% ✓ (weakest) | COMPLACENT | 12.9% | SELL VOL — half, weak conviction. |
| MRVL | 08-27 pm | 6.5% ✓ (barely) | COMPLACENT | 17.8% | SELL VOL — half, weakest confirmed kink. |
| **ADSK** | 08-27 pm | **4.2% — sub-threshold** at the earnings tenor (its 22.7% kink sits at an unrelated 09-25) | TAIL_HEDGING 0.09 but at the *wrong* tenor | 12.2% | **BUY VOL.** The market does not specially price ADSK's earnings; event vol looks cheap. ⚠ Core PCE (est.) lands 08-28, one day after. |
| **CRM** | 08-26 pm | **4.4% — sub-threshold** (its 20.8% kink sits at 09-18) | NORMAL ~flat | 11.1% | **BUY VOL.** Same pattern — the real dislocation is elsewhere and unrelated. |
| OKTA | 08-26 pm | none — curve decays smoothly | COMPLACENT, dead flat | **22.2%** (richest) | **SKIP.** Maximum richness, zero signal. |

**Week-1 cohort — mechanically backwardated** (the front tenor *is* the event tenor, so no kink shape is possible by construction; context, not a discriminating signal): HD (08-18), LOW/TJX/ADI (08-19), WMT/DE/AAP/ROST/BABA (08-20).

Only **HD, LOW, TJX** carry genuine TAIL_HEDGING back-month confirmation → SELL VOL at half size (the VRP-negative week trims full). **WMT → CALENDAR** (defined risk; it reports *on* FOMC-minutes day). **DE, AAP, ROST, BABA, ADI → SKIP** — ROST has the highest front ratio in the entire scan (1.857) with dead-flat back-month skew, the front-only coin-flip at its most extreme, plus a direct macro collision.

**Every 08-20 print collides directly with FOMC minutes** — the most severe collision tier (SKIP or CALENDAR only, never naked short vol). The 08-18/08-19 names get a 1–2 day buffer, but Jackson Hole (08-21/22) still sits inside any multi-day post-print hold.

**VRP alignment:** every SELL VOL call runs *against* this week's premium-buying regime and is sized down accordingly; the two BUY VOL calls (ADSK, CRM) and the recap's NBIS/LITE outcomes align with it.

---

## 7. Risk & Correlation (week-candidate universe)

**The post-gate book is EMPTY. Zero sized positions — not "light", not "starter-only", flat.** Both `starter` candidates (SNDK, NBIS) gate to `skip`; the other three were already `watch_only` on entry (two by SHORT-routing, one for having no direction to size).

### Correlation clusters — `uw risk portfolio-correlation`, 30d

**`memory_complex_long_cluster` — FIRES.** **SNDK / NBIS = 0.709.** Wider complex, context only (all DROP-tier): SNDK/MU **0.900**, SNDK/AMD 0.876, SNDK/STX 0.821, MU/AMD 0.855, NBIS/MU 0.706. **Kept SNDK** — raw scores tie at 3, tiebroken on in-direction `cum_premium_flow_30d` (+$1,577.4M vs +$305.5M); **NBIS takes −1 tier.** Read plainly: this was never two ideas. It is **one violently-extended memory-complex bet held twice** — +35.4% and +47.7% on the week, rv20 149.8 and 183.5, ATR14 ~9.8% and ~10.0% of spot. Two starters here would have been a single ~2×-sized position in the most extended cohort on the tape.

**`index_etf_cluster` — FIRES.** **IWM / SPY = 0.817.** Kept IWM (raw 6 > 3); **SPY takes −1 tier.** Moot for sizing (both already `watch_only`) but recorded for portfolio visibility.

**AVGO appears in no pair ≥ 0.60 with any book member** — the only genuinely uncorrelated name here, and the one policy forbids sizing. `sector_breakdown` returned `Unknown: 8`; the CLI's sector tagging is null for this set, so the "100% in top sector" warning is an artifact and is not treated as a signal.

### Panic gate — read at `--near-dte 7`, and it worked

| Ticker | front-end IV ratio @7DTE | Regime | Gate |
|---|---|---|---|
| **NBIS** | **1.215** (deepening from 1.178) | BACKWARDATION | **FIRES** |
| MU | 1.184 | BACKWARDATION | fires (DROP) |
| **SNDK** | **1.150** | BACKWARDATION | **FIRES** |
| STX | 1.080 | — | no-op (DROP) |
| AMD | 1.060 | — | no-op (DROP) |
| IWM | 0.904 | CONTANGO | no-op |
| AVGO | 0.823 | CONTANGO | no-op |
| SPY | 0.782 | CONTANGO | no-op |

**Population firing rate 3 of 8 (37.5%), and it discriminates correctly** — firing on exactly the memory-complex melt-up names while staying quiet on both indices and the AI-infra bleed name. This is the direct opposite of the 2026-08-13 failure at the CLI default `--near-dte 1`, where it fired 8-of-9 while SPY/QQQ printed CONTANGO. Note AVGO specifically: the default read was **1.731 "BACKWARDATION"** — a pure 1DTE-bucket artifact — against **0.823 CONTANGO** at 7. **Read at 7, always.**

### Macro & event risk

Stagflationary tilt: core PCE **3.29%** YoY above core CPI 2.79%, payrolls **−23k**, unemployment 4.1%, 10Y 4.63% flat, USD weakening. The worst backdrop for a Fed-pivot trade, and it raises the bar sharply on long-duration/high-multiple names — NBIS carries PE 1,513, PS 121, operating margin −50.48%.

**The event wall, counted from T+0 = 2026-08-14:**

| Event | Date | Trading days |
|---|---|---|
| Building Permits + Housing Starts | 08-19 | T+3 (medium) |
| **FOMC MINUTES** | **08-20** | **T+4** |
| **MONTHLY OPEX** | **08-21** | **T+5** |
| Jackson Hole opens + claims / Philly Fed / flash PMI stack | 08-21 → 08-22 | T+5 / T+6 |

Two named, dated Tier-1 binaries land in the T+4–T+5 band, stacking to **−1 tier** on every undefined-risk swing call. Jackson Hole is treated as corroborating context, not a separate deduction — spending another −0.5 on it would be ambient-macro stamping. Independent corroboration that the book is pricing 08-21: the term-structure kink converges there across **five separate names**, and both multileg roll targets point at it. No name-specific earnings fall inside the window.

### Fundamentals verdicts — zero VETOs

| Ticker | Verdict | Adj | The contradicting fact |
|---|---|---|---|
| **SNDK** | **CAUTION** | −1 | Insider MSPR −100 or near it in **13 of the last 18 months, every month since 2026-01 without exception**, against a long-accumulation call. Earnings/growth do *not* contradict (4/4 beats, +175.3% YoY) — textbook CAUTION, not VETO. |
| **NBIS** | **CAUTION** | −1 | Insider MSPR −73.42 3mo average, two of the last three months at −100 / −86.1. VETO test explicitly does not clear (1-of-3 legs). |
| **AVGO** | CONFIRM | 0 | Fundamentals do not fight the short (rev +32.29%, GM 68.35%, OM 43.43%). Confirmed the −5.94% Friday was **not** an earnings reaction (next print 09-02). |
| IWM / SPY | NA | 0 | Index ETFs, no issuer. NA never penalizes. |

**A discrimination worth crediting:** the gate declined to treat AVGO's 19-month MSPR ≈ −100 cadence as fresh bearish conviction, reading it instead as scheduled 10b5-1 decumulation, and rested the CONFIRM on the BofA financing note and Third Point's exit — while noting Soros *raised* +6.5% the same window. That is the gate distinguishing a signal from a constant, which is exactly what it exists to do.

### Debate-disconfirmation cuts

**The gate fired on 4 of 4 debated names** (`bear_residual ≥ bull_residual` in every case). The debate can only cut, never add.

| Ticker | Bull | Bear | Spread | Gate |
|---|---|---|---|---|
| IWM | 0.35 | 0.35 | 0.00 | **FIRES** (tie) |
| SNDK | 0.35 | 0.65 | 0.30 | **FIRES** |
| AVGO | 0.35 | 0.45 | 0.10 | **FIRES** |
| NBIS | **0.25** | **0.75** | **0.50** | **FIRES** |
| SPY | — | — | — | not run |

**SPY's debate was deliberately not run and serializes as `null`, not as a low pair** — it was scored non-directional, and a bull/bear debate needs a directional proposition; running one would have manufactured a direction the quant explicitly declined to assign.

**IWM produced a both-sides-low 0.35/0.35 pair** — "neither advocate can make their case," precisely the signal the 2026-07-25 P1 #5 bin-ladder extension (floor 0.55 → 0.15) exists to preserve; under the old schema it would have been unrepresentable. What makes it notable is that the **bear — arguing *for* the top-scored short — conceded the dealer-book conflict outright.**

**NBIS produced the widest spread in the book (0.50).** The bull's own opening conceded that "smart money is trimming into retail-driven momentum, with squeeze mechanics as the most charitable alternative explanation." The bear then inverted the squeeze pillar: 29.79% short float against only **2.89 days to cover** means covering fuel is closer to *exhausted* than fresh. And it drew the distinction that decides the name — **the deepening backwardation NBIS earned its +1 for is a vol-structure / event-fear signal, not a directional-conviction one.** The bull was borrowing a long-vol argument to fund a directional long.

**SNDK's bear offered the sharpest reframing of the week:** it granted the DEX flip is real, durable and non-saturated, then argued it is *reactive* — dealers short gamma on short-dated calls (78% of the OI build sits inside 7DTE) getting run over by a +35% tape and buying to stay hedged. On that reading the flip is the *mechanism* of the move, not evidence for it. It conceded it cannot prove that over the bull's reading, which is why the residual landed at 0.65 rather than higher.

**What the round is actually telling us:** every residual landed at or below 0.45 on the side the rubric scored. Not one advocate could defend the call the score produced. That is not four coincidences — it is the additive score and the disconfirmation layer disagreeing systematically, which is the failure mode the debate stage was added to catch.

### Breadth cross-check (advisory)

250 advancers / 245 decliners, **49.7% green with a 0.00% median member change**, while SPY sits −0.39% from its 90-day high. Divergence flagged. Green tape here is **rotation, not participation** — a narrow cap-weighted cohort carrying the index. No size impact.

### Prior-group adverse flow — `conviction_week_2026-W31` (`MRVL, SNDK, IWM, SPY`; W32 not run)

| Ticker | Flow | net_flow | Vol ratio | Read |
|---|---|---|---|---|
| **SNDK** | bullish | +$166.4M | **2.33** | **CONFIRMING on direction, DECAYING on quality.** 2.3× volume, a $537M single DP print, OI +64,465 — but the confirmation *is* the contaminated evidence: net-30 is 2.9% of a $54.29B gross, and the top tickets are the $215.6M-gross calendar roll netting ~$0.4M of intent. The thesis is not reversing; it is thinning. |
| **IWM** | bearish | −$25.0M | 0.72 | **CONFIRMING but thin.** P/C 1.757, put volume 763k vs call 434k, OI +159,186 — direction holds W31→W33. But volume ratio 0.72 is **below-average participation**, against a dealer book that built long all week. |
| **SPY** | bullish | +$53.9M | 0.77 | No adverse reversal; carried as structural. |
| **MRVL** | bearish | −$106k | 0.84 | **EXIT CANDIDATE — off-thesis decay without a hard alert.** Zero Phase 1 agents flagged it this week; it dropped out of the candidate union entirely, with nil net flow and below-average participation. Exactly the silent decay the scan exists to surface. **Dropped from the W33 write.** |

**`fz` fundamentals-drift tripwire (advisory):** SNDK moved 7 fields, **all accretive, none adverse** — Book/sh 93.09→107.78, Cash/sh 25.22→32.16, Income 4.51B→11.43B, Sales 13.18B→20.25B, Market Cap 189.55B→243.03B. No short-float jump, no target cut. A +28% market-cap re-rate in two weeks with fundamentals catching up — descriptive colour, not a flag. No adverse-fundamentals exit candidate this week.

### Hedge sleeve

**None required — there is no book to hedge.** Post-gate net delta is zero; directional skew is undefined by construction, nowhere near the ±0.6 trigger.

*Conditional guidance if the desk carries residual long beta from elsewhere:* in a **VRP-negative, premium-buying** tape the hedge must be **long premium** — SPY/QQQ Sep18 put verticals or a VIX call ladder spanning 08-20/08-21 — and **never** a short-premium/iron-fly expression, which contradicts the vol regime outright. The optionality is genuinely cheap (SPY IV rank 6.1, IV percentile 0, z −1.271). Note **the tape is already doing this trade**: SPY's 1:2:1 put-fly ladder and a 76.3%-put OI build with a 300,046-contract Dec18 480P as its largest print. Related: the 0DTE premium-selling lane is **net-negative at this VIX** — stand aside there too (§9).

### Final sizing table

Lane-level `market_excess` proxy (per-call `win_rate` is `NA(substrate)` on all 8): longs carry `bullish_flow` **−9.1pp** ⇒ `beta`; shorts carry `bearish_flow` **+9.0pp**.

| Ticker | Class | Dir | Win-rate | Market excess | Pre-risk | Gates fired | **Final** |
|---|---|---|---|---|---|---|---|
| **IWM** | multileg_directional | short | NA(substrate) | +9.0pp (lane) | watch_only | regime, event_risk, debate | **watch_only** |
| **SNDK** | oi_build | long | NA(substrate) | **−9.1pp `beta`** | starter | panic, fundamentals, event_risk, debate (**4×**) | **skip** |
| **AVGO** | oi_build | short | NA(substrate) | +9.0pp (lane) | watch_only | regime, event_risk, debate | **watch_only** |
| **SPY** | structural_hedge | none | NA(substrate) | n/a | watch_only | cluster | **watch_only** |
| **NBIS** | oi_build | long | NA(substrate) | **−9.1pp `beta`** | starter | panic, cluster, fundamentals, event_risk, debate (**5×**) | **skip** |

**`watchlist_write_back_confirmation`:** `uw watchlist manage --action add --group conviction_week_2026-W33 --tickers IWM,SNDK,AVGO,SPY,NBIS` — **CONFIRMED**, verified via `--action list`. All five are LOW-or-better per the corrected 2026-07-23 rule; **MU, STX and AMD (raw 2, DROP) were excluded** so they do not poison next week's correlation loop. Zero VETOs. **MRVL was not carried forward.**

### Risk officer's plain statement

**The board is empty and it should be.** Four independent facts make that the right answer rather than an unlucky one:

1. **The scoring substrate is the week's real risk.** The +3 OI line was the sole source of points on **8 of 8 names**, saturated at a 100% population firing rate at both windows, with put-heavy composition on names whose thesis is long. Strip it and the book scores −1 to +3. **Sizing off it would be sizing off nothing.**
2. **`win_rate` is `NA(substrate)` on all eight, structurally** — the rubric's highest-weight lines attach to classes the substrate cannot measure, and `dark_pool_accumulation` returns zero rows market-wide. No call here has a measured hit rate behind it.
3. **The long lane had no measured edge over the index** (−9.1pp), six of eight names were long, and both survivors sit in one 0.709-correlated melt-up cluster at rv20 150 and 184, with a live distribution flag on one and insider selling on both.
4. **The event wall is inside the first five sessions of anything opened now.** Opening undefined-risk 4.5-beta longs into FOMC minutes at T+4 and OPEX/Jackson Hole at T+5, in a stagflationary macro with payrolls contracting, is the trade the gate stack exists to refuse.

**One item on the record for the next audit, as an observation and not an override:** the only lane with positive measured excess this week is the short lane (**+9.0pp, n=133**), and both short candidates route to `watch_only` by policy. The rule is correctly applied — it is routing, not suppression, and IWM and AVGO remain fully scored, gate-verdicted and serialized so the counterfactual keeps resolving. But this is now a recurring pattern the audit should watch: **the policy is costing the desk the one lane with positive measured excess in the week's own data.** Its revisit trigger (short-side McNemar non-significant across two consecutive cross-regime windows) is **unmet and moving further away** (p 0.0115 → 0.0038), so nothing changes today.



## 8. High-Conviction Cross-Ref (HIGH and MEDIUM tier)

**Empty. No name reached MEDIUM (≥7) or HIGH (≥9)** — the ninth consecutive cycle in which the post-freeze bands are structurally unpopulated. What follows is the expectancy lens and the audit-facing per-name record for the five LOW-tier calls, since there is no higher tier to cross-reference.

### Expectancy lens (advisory — C31)

From the 2026-08-08 `/calibration-audit` `phase_3_calibration`, era-stratified and never pooled:

| Tier | n (all eras) | Realised WR | Frozen era (`2026-06-12`) |
|---|---|---|---|
| HIGH | 7 | **0.143** | **0 decided calls** |
| MEDIUM | 19 | 0.526 | **0 decided calls** |
| LOW | 104 | 0.375 | 0.279 (n=43) |
| DROP | 412 | 0.415 | **0.403 (n=352)** |

**Tier monotonicity failed for the 6th consecutive audit**, and in the frozen era **DROP (0.403, n=352) still beats LOW (0.279, n=43)** — the declined pile continues to out-perform the tier the book actually surfaces. HIGH has been frozen at n=7 / 0.143 for four audits because the rubric has emitted no HIGH since the freeze; the re-validation is not merely unsatisfied but **structurally unrunnable for the 8th cycle**. `BRIER 0.2863`, `LOG-LOSS 0.795` against a 0.693 coin-flip reference — the damage sits in confident-and-wrong quotes, not diffuse noise.

**None of the reliability bands bind this week**, because every call carries `win_rate: null / NA(substrate)` — no quote was emitted into any band at all. Worth stating plainly rather than treating as a clean bill of health: the anti-predictive `[0.55,0.65)` floor and the 0.80-band overconfidence are **unexercised, not disproven**, and the reason is that the substrate cannot price this week's dominant signal classes. This week adds nothing to HIGH or MEDIUM and five more rows to LOW.

### Per-name audit record (all LOW, all gated to no capital)

| Ticker | Score components (Σ = raw) | Win-rate | Fundamentals | Debate (bull/bear) | Final | Invalidation |
|---|---|---|---|---|---|---|
| **IWM** | +3 oi (saturated) +2 multileg +1 accretion = **6** | NA(substrate) | NA | 0.35 / 0.35 | watch_only | Reclaims ~295 through OPEX week |
| **SNDK** | +3 oi (saturated) +1 dex_flip −1 flow_lite = **3** | NA(substrate) | **CAUTION** | 0.35 / 0.65 | **skip** | Below the $1,630 DP shelf |
| **AVGO** | +3 oi (saturated) +1 dex_flip −1 flow_lite = **3** | NA(substrate) | CONFIRM | 0.35 / 0.45 | watch_only | DEX reverses ≥3 sessions |
| **SPY** | +3 oi (saturated) = **3** | NA(substrate) | NA | not run | watch_only | n/a — non-directional |
| **NBIS** | +3 oi (saturated) +1 vol_surface −1 flow_lite = **3** | NA(substrate) | **CAUTION** ⚠`distribution_flag` | 0.25 / 0.75 | **skip** | Below the $272 DP shelf |

**The single most important line in this table is the one every row shares.** Remove the saturated `+3 oi` component and the scores become IWM 3, SNDK 0, AVGO 0, SPY 0, NBIS 0 — i.e. **four of the five names would not have cleared the DROP floor at all**, and the fifth would have fallen from top-of-book to the bottom of the LOW band. The book's entire apparent structure this week rests on a measurement with a 100% population firing rate.

**Instrumentation trio (advisory, 0 rubric points):** `implied_move` is `null` on the one vol row (NBIS) — an instrumentation gap, deliberately *not* filled with the CLI's native field, which is pinned to a sub-1-day horizon and runs ~16× too small; emitting it would satisfy the schema while poisoning the IV-vs-RV resolution the field exists to enable. `dp_block_to_float_ratio` is `null` on four of five (correctly — no name has `dark_pool_accumulation` as dominant class, so C16 has no row to grade) with SNDK at 0.00224. `insider_cluster_flag` is `null` throughout — lane skipped, **not `false`**; C18 has shown zero variance across all 15 populations to date.

### Embedded rubric (for audit) — FROZEN version `2026-06-12`

```
Weekly conviction score = Σ:
  # +3 line for swept on ≥3 of 5 days REMOVED 2026-05-23 audit P0.3
  # (sweep-persistence marginal contribution −22pp two consecutive audits; multi_day_sweep realised
  #  0.43 vs a claimed 0.70. Tool remains informational; contributes 0 points.)
  +3  uw historical oi-trend BUILDING for the full week, --days ≥ 5   # WEEKLY-ONLY +3 vs DAILY +1.
      # SHARPENED → register C47: backing tool measured −9.2pp class-controlled marginal (n=69);
      # `consecutive_build_days` ceilings at `--days` on liquid names, so the award can be earned by
      # expiry mechanics. When quoting this line, state whether consecutive_build_days == --days.
  +3  3+ aligned signals in accumulation-hunter sustained across week, uw dark-pool block-stratified
      institutional-tier confirmed — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms
      (sign aligned AND |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1.
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70, stable WoW — CONDITIONAL ONLY:
      award only when dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +2  uw oi position-rolls shows institutional roll forward into longer-dated LEAP (per-covered-date)
  +1  uw historical cumulative-premium-flow shows net directional accretion across the week —
      INTENT-SCREENED: award only when (a) no C28 distribution_flag on the name, AND (b) on dividend
      payers inside an ex-div window, the accreting prints are NOT deep-ITM sub-parity calls. Else 0.
  # +2 line for uw insights signal-confluence ≥4 REMOVED 2026-06-12 audit P0.2 (server-side re-count
  #    of already-scored quantities; no per-ticker mode; funnel-seed role only).
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna squeeze in trade direction —
      verified SIGN CHANGE only, not a level: sign(net_dex) on the latest session opposite to ≥3
      consecutive prior sessions; flip-day |net_dex| ≥ 0.25× trailing-10-session median |net_dex|;
      computed with scripts/dex_flip.py; sign_changes_in_window / whipsaw_warning mandatory to report.
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector —
      CONDITIONAL: (a) sector persistence_score ≥ 0.6 AND (b) cum_premium_flow_30d direction aligned
      AND (c) |cum_flow_30d| ≥ $50M. Default 0.
  +1  in earnings-scout BUY VOL or SELL VOL for next 2 weeks (term-skew aligned for full size)
  +2  multileg-strategist directional structure repeated on ≥2 days (term-structure-anchored play type)
  +1  vol-surface-scout flags KINKED or BACKWARDATION, worsening WoW; iv-percentile-zscore extreme;
      VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner crowded long with rising pc-ratio-zscore trajectory (VRP positive)
      # An INFORMED-FLOW CONTINUATION penalty, not a "fade the crowd" signal.
  -3  flow_conflict — cum_premium_flow 30d direction clearly OPPOSITE dominant_signal_class
      (signed-sum sign flip + magnitude > union-median |cum_flow_30d|, or explicit OPPOSITE label)
  -1  flow_conflict_lite — 30d cum_premium_flow read is MIXED (signed sum near zero, or aligned but
      bottom-quartile magnitude)          # -3 and -1 are MUTUALLY EXCLUSIVE — apply ONE, never both
  # The two lines below are TIER GATES applied in Step 2d, not score_components (0 to raw_score):
  -2  [TIER GATE] risk-monitor flags correlation cluster (pairwise corr ≥ 0.70) — −1 TIER
  -3  [TIER GATE] WoW market-regime flip conflicts with trade direction — −1 TIER
```

**Tiers:** ≥9 HIGH (full size) · 7–8 MEDIUM (half) · 3–6 LOW (starter / watch-only) · ≤2 drop.

**Lines that scored ZERO across all eight names this week, and why** — recorded rather than silently skipped:
- **+3 accumulation conjunction:** accumulation-hunter returned an empty board and rejected all six mega-tier candidates, so the base award was never earned and the halving-to-+1 path never opened. `dark_pool_accumulation` returning zero backtest rows market-wide is independent corroboration.
- **−2 contrarian crowded long:** fails on *both* qualifiers — the "rising pc-ratio-zscore" clause is structurally unsatisfiable (`pc-ratio-zscore` has no `--date` flag) **and** the line requires VRP *positive* while this week is decisively VRP-negative.
- **+1 opex-pin:** `is_opex_week: false`. The 7-day guard spawned the agent, but the pin book is forward-looking into W34.
- **+1 sector-leader:** condition (a) is non-discriminating (persistence 1.0 on 11-of-11 sectors), (b) fails on MIXED flow everywhere, and (c) fails on magnitude for STX ($17.9M) and AVGO ($34.8M). Because it scored zero everywhere, the known `sector ↔ cum-flow` double-count did not fire this week.
- **+1 conviction-matrix, +2 position-rolls:** no LEAP-class name existed to award them to.

**The central adjudication that shaped the week**, recorded for audit: *a MIXED cum-flow read supplies no direction, and it must supply no direction consistently to every line that queries it.* Seven of eight names printed MIXED at 0.5–3.3% net-of-gross. That single read is queried by three separate rubric lines (the +3 conjunction's confirm-clause, the standalone +1 accretion, and condition (b) of the sector-leader line). It cannot be "no direction" for one and "direction aligned" for another — so on every MIXED name all three resolved to zero, and the name additionally took the −1 `flow_conflict_lite` the label itself triggers. No name double-dipped.



## 9. Setups for Next Week

### Next-session GEX advisory — SPY/QQQ only (prose-only, 0 rubric points)

**Lead with the track record, not the levels.** The Step-0 rolling backtest returned **`NO_GO_NO_EDGE`**: walls-as-magnet ran at **22.0% pooled (n=118, p vs 50% = 1.0)** — the next close moved *away* from the nearest wall 78% of the time — `contained_within_walls` 55.1% and `moved_in_pin_direction` 54.2% are both near coin-flip, and H1 ran backwards (long-gamma sessions realised **more** absolute movement, 0.829% vs 0.700%). These are **dealer-context levels, not magnets or targets.**

| | SPY | QQQ |
|---|---|---|
| Spot | 776.06 | 730.41 |
| Zero-gamma level | 774.67 (**reliable**, −0.18%) | 729.92 (**reliable**, −0.07%) |
| Regime | POSITIVE (long gamma) | POSITIVE (long gamma) |
| Total GEX | $2.02B | $652.3M |
| Call wall | **780** (+$443.5M) | **735** (+$156.3M) |
| Put wall | **765** (−$128.4M) | **720** (−$20.6M, shallow) |

**The book is about to change shape.** The largest strikes in both books (SPY 775/776, QQQ 730) are **today's 08-14 expiry**, settling tonight — **$5.49B of premium, the single largest expiry bucket, rolls off.** After that, **09-18 ($4.20B) and 08-21 ($4.16B) become the twin dominant tenors**, and much of the GEX currently supporting the walls above sits in the 08-21 bucket that will be extinguished on OPEX Friday. Treat Monday's book as materially reshaped from Friday's, and next week's structure as unstable into 08-21.

**Regime freshness:** SPY's POSITIVE regime is only **two sessions old** — it flipped NEGATIVE on 08-10, held NEGATIVE through 08-12, flipped back on 08-13 (flip dates 08-05, 08-07, 08-10, 08-13). QQQ's ZGL was **unreliable/extrapolated on 08-10 and 08-13** despite a POSITIVE label; only Monday's and Friday's reads are clean. Trust the aggregate `total_gex` sign over the discrete label.

*Mandatory caveats:* EOD prior refreshed by fresh 0DTE OI in Monday's first 30–60 minutes; gap risk; this is the SPY/QQQ **ETF** book, not the cleaner SPX/NDX index book; the CLI cannot isolate the D+1 expiry, so this is a 0–45d proxy diluted by the 08-21 concentration.

### Next-session 0DTE premium-selling setup — **STAND ASIDE**

The script returns `sell_premium: true` and `GO_PREMIUM_SELL_INTRADAY` for both indices. **Both are overridden here, and the override is the point of this subsection.** Those verdicts are unconditional; the edge is not.

Current `vol_state` is **LOW (VIX 14.25)**. Reading `mean_pnl_by_vix_state[LOW]` net of the assumed 0.1% round-trip cost:

| | Headline net (unconditional) | **LOW-VIX gross** | **LOW-VIX NET** |
|---|---|---|---|
| SPY | +0.119% | +0.022% | **−0.078%** |
| QQQ | +0.241% | +0.091% | **−0.009%** |

**Both are net-negative-to-zero at today's VIX.** The lane's entire edge lives in the MID/HIGH terciles (SPY +0.231%/+0.205% net, QQQ +0.369%/+0.362% net). Selling 0DTE premium here means trading a −0.078% expectancy while quoting a +0.119% headline. Add that the sample contains **no vol shock** — the short-vol left tail is unsampled, `worst_day_open_pct` is −1.4% (SPY) / −2.453% (QQQ) — and that next week carries FOMC minutes plus Jackson Hole.

*If traded anyway* (advisory, 0 rubric points): SPY iron fly centred 775.9, wings ±0.78%; QQQ centred 730.84, wings ±1.37%; size scalar 0.5; enter at the open once the overnight gap resolves; **never carry overnight**; stand aside on a VIX spike or front-end backwardation. PnL basis is % of underlying spot notional, gross — lead with the net line. Win-rate (88.3%/85.0%) is **not** the promotion metric for a negatively-skewed short-vol book.

### OPEX pin book — forward-looking into 2026-08-21

Today is 7 calendar days before the monthly third Friday, so **next week (W34) is OPEX week**; this book is a prior on where dealer gravity is *building*, with five full sessions to evolve. Of 19 raw `pin-risk` rows only 9 are in the liquidity-floor set, and only **two clear a 2% pin-distance gate**:

| Ticker | Pin strike | Spot | Distance | OI at pin | GEX at pin | Structure |
|---|---|---|---|---|---|---|
| **SPY** | 780 | 776.31 | **0.48%** | 94,621 | +$389.6M | **Iron fly** (defined risk — see override) |
| **MSFT** | 500 | 495.17 | 0.98% | 47,634 | +$54.0M | **Iron fly** |

Dropped on distance: QQQ 700 (4.26%), NVDA 220 (2.31%), IWM 290 (4.94%, *and* short-gamma −$10.4M), AMZN 275 (4.71%), NFLX 80 (2.33%), FXI 36 (3.06%), GLD 420 (4.63%). Note `pin-risk` returned `dte_to_opex: 0` on every row — it keys to the nearest weekly, not the 08-21 monthly; the strikes above are the current gamma skeleton carried forward, cross-checked at `--dte-max 10`. There is **no `probability` field** and none is quoted.

**Event-collision verdict — the dominant read.** Friday 08-21 is simultaneously monthly OPEX, the **Jackson Hole opening**, and a claims/Philly-Fed/flash-PMI stack, with **FOMC minutes two sessions earlier on 08-20**. Pin mechanics assume a quiet dealer-dominated drift into expiry; that assumption is at maximum stress. **SPY's technical short-straddle qualification is overridden down to iron fly** on this basis — no naked short vol in this book at any distance. Compounding it, VRP is negative, so every structure here is short premium into a tape that says optionality is *cheap*.

**Lane verdict: marginally tradeable, defined-risk only, small size** — iron flies only, SPY 780 / MSFT 500 only, and re-run the pin scan Mon–Thu to confirm the walls haven't shifted ≥30% before committing. Given the `NO_GO_NO_EDGE` backtest sitting underneath the whole mechanism, **"no structure this cycle" is the better-calibrated default and is the recommendation of record.**

### Swing dealer setups (1–4 weeks)

Only two names produced a mechanized DEX sign-change: **SNDK** (`dex_flip_long`, fired 08-12, magnitude_ratio 2.52, whipsaw FALSE, and the flip held and grew ~9× to +$12.20B) and **AVGO** (`dex_flip_short`, 08-14, |flip| $938.5M vs an $805.2M floor, ratio 1.17, whipsaw FALSE, corroborated by a GEX regime flip three sessions earlier on 08-10). Both are gated to `watch_only` — see §7.

Explicit negatives worth recording: **MU and IWM built DEX *levels*, not flips** (the exact level-as-flip error the 2026-06-12 mechanization exists to prevent); **NBIS failed the magnitude floor** (flip value $25.3M vs a $196.8M floor, ratio 0.13 — whipsaw around zero, correctly rejected); **MSTR was disqualified on whipsaw** (7 sign changes in 14 sessions). **No name produced a valid `vanna_squeeze` flag** — the VIX gate requires ≥3 consecutive falling sessions and the 08-13 uptick (14.55 → 14.63) breaks the run at two. Note the ^VIX series was successfully dated this week via the Yahoo chart API (15.46 → 15.28 → 14.55 → 14.63 → 14.25), resolving for this window the "no clean 2026 VIX source" gap.

### Pin vs trend regime call

**Neither, and that is the call.** The pin mechanism is `NO_GO_NO_EDGE` on its own out-of-sample record, and the trend read is contradicted by breadth (49.7% green, 0.00% median member) and by a netted sector rotation that reversed inside five sessions. The one thing the book agrees on is the **08-21 date** — five term-structure kinks and both multileg roll targets converge there. Position around the *event*, not around a direction.

### LOW-tier names to track for daily-analysis confirmation

**IWM, SNDK, AVGO, SPY, NBIS** — all LOW, all gated to no capital this week. The two worth watching hardest for a thesis change are **SNDK** (does institutional-accumulation ever confirm the move, or does the DEX flip decay?) and **IWM** (does the dealer book stay long-gamma, which would confirm the put ladder is a hedge rather than a directional build?).

### Deep-dive hand-off

**Skipped — no-edge week.** No name reached HIGH tier, so there is no post-gate, non-VETO HIGH-tier name to hand off. Recommended if the desk wants one anyway: `Recommended deep dive: /stock-deep-dive NBIS` — not because it is a trade, but because it is the week's largest resolved move, the widest debate spread (0.50), and carries the only live C28 distribution flag in the book.

### Single-leg whale scan — empty

`uw options-flow single-leg --regime bull` returned **25 graded signals per session and zero Tier-1 prints on all five sessions.** No repeat Tier-1 opening/floor PUT names, so there is no persistence colour to report. Advisory and **permanently 0 rubric points** — C19 was CLOSED as REFUTED on 2026-07-25 (register C53); there is no promotion path and no rolling-WR gate to report progress against.

---

## 10. Watch-only — single signal, no confluence

Surfaced by exactly one Phase 1 agent; **listed for journaling, not for entry.**

| Ticker | Source agent | Read | Why it stops here |
|---|---|---|---|
| **GLD** | multileg-strategist | Bullish OTM Sep18 call ladder (400/420/425/445C), repeat-2, rolled and tightened 08-12; separate 330P financing leg | Genuinely clean structure, and the stagflation/weak-USD macro independently supports it — which is exactly why the gate exists. One agent is one agent. GLD's 90d LEAP flow is also −$330.2M, and it was a DROP call on 08-10 that graded INCONCLUSIVE. |
| **EWY** | sector-rotation-strategist | Clean multi-day BULLISH ETF inflow +$22.6M; Korea/Samsung/SK Hynix = geographic proxy for the memory thesis | Best single-signal name of the week. Was the 08-12 LOW call; graded INCONCLUSIVE at +2.20% (0.82×ATR) — just under threshold. |
| **APP** | vol-surface-scout | Best calendar candidate — front ratio 1.104→1.060 (panic resolving), backwardation held, no earnings in 14d | Vol-lane only; sector-rotation independently flags it as AI-infra-bleed avoid (−9.0% 5d). Direction conflict. |
| **AMAT** | accumulation-hunter | DISTRIBUTION three straight days; bearish-inferred put OI building; −5.9% 5d | Bearish ⇒ `watch_only` by routing regardless. Clean earnings SELL-VOL win this week (§6). |
| **LRCX** | sector-rotation-strategist | Memory-cohort leader, +6.8% 5d | Marginal second flag only; base_shape resolved BACKWARDATION→FLAT. |
| **MSFT** | opex-pin-strategist | Pin candidate 500 strike, 0.98%, +$54.0M GEX | Its accumulation thesis was **rejected as closing-cross contamination** (§7); the multileg print was single-day. Lost 2.11% as an 08-10 LOW call. |
| **MSTR** | multileg-strategist | Single-day 95C calendar, CONTANGO-anchored | dealer-positioning **disqualified** it on whipsaw (7 sign changes in 14 sessions). Screener-vs-tape divergence (bullish screener, −7.0% 5d). |
| **CIFR** | sector-rotation-strategist | Only C12-passing bullish Financial-Services name | Thin, single agent; its sector's GICS "IN" read fails the ETF cross-check (KRE −$1.3M bearish). |
| **XLU** | sector-rotation-strategist | Only tradeable Utilities vehicle; scored 6/6 in the Step-0 confluence funnel | Sector sign-flipped mid-week on trivial magnitude (+$4.1M netted). |
| **IGV** | sector-rotation-strategist | Clean persistent BEARISH −$13.9M with bid-side call *selling* — distribution signature | ETF, advisory, bearish ⇒ no entry. The cleanest confirmation of the software/AI-infra side of the split. |
