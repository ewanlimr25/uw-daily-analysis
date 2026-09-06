# Daily Market Analysis — 2026-08-20

## Executive Summary

- **Regime + GEX state:** `TRANSITIONAL — Mixed signals, reduce position size, wait for clarity` (trend field still `UPTREND`; SPY 762.60 above both 20SMA 760.99 and 50SMA 750.94). Broad decline — SPY −0.84%, QQQ −0.72%, IWM −1.34%, and critically **RSP −0.81% ≈ SPY**, so equal-weight fell as hard as cap-weight. VIX **16.01, +7.52%**. Breadth 157 advancers / 342 decliners (**31.2% green**); `uw` flow breadth 34.6% bullish. Both SPY and QQQ are **short-gamma** into tomorrow's open. Sector lean: no rotation call — `no_change`.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** **SPY** — FULLY_NEGATIVE, total_gex −$1.87B, ZGL null (`zgl_reliable=false`), call wall 780 / put wall 760; negative pockets straddle spot (765 = −$396M at +0.25%) → favor debit verticals over premium selling. **QQQ** — total_gex −$777M with the board's largest negative strike (710, −$248M) sitting *on* spot; call wall 730 / put wall 710; ZGL printed 208.83 vs 710.77 spot (garbage). Advisory, 0 rubric points — see §2.
- **Top swing build:** **None sized.** The only scored call is **IWM short (raw 4, LOW)** and it routes to **`watch_only`** — directional short alpha is never sized (2026-08-01 P0 #1). Two further gates (regime −1, debate −1) would floor it at `skip` even without that rule.
- **Top LEAP candidate:** **None.** ET (Energy Transfer) was the only name clearing 7-of-8 LEAP gates and it **failed the confluence gate on breadth** (one flagging agent, needs two), then scored 0.
- **Biggest risk:** Not a position — it is the **calendar**. PCE at T+4 and **Kevin Warsh's first Jackson Hole keynote as Fed Chair at T+6** are un-priced, and the vol surface is already pricing them (see §5). With zero exposure there is no correlation cluster and **no hedge is warranted**.

> **This is a no-edge day — the 32nd consecutive session without a sized position** (last sized 2026-07-07). That is an output, not a failure.

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL**, trend `UPTREND`, `market_breadth.bullish_pct` **34.6%** (2,184 bullish vs 4,131 bearish flow tickers of 6,315). Tool guidance verbatim: *"Half position sizes. Favor defined-risk strategies. Iron condors in range."* SPY −2.15% from its 90-day high.

The breadth narrative is unambiguous and both independent sources agree. `fz` breadth: **157 / 342**, `pct_green` **31.21%**, avg change −0.70%, median −0.74%. **`divergence_flag = FALSE`** — the divergence tell is a *green* index with `pct_green < 50`; today the index is red and breadth is red, so the two data lineages corroborate rather than conflict.

**Per-index gamma (current-state EOD book):**

| Index | Spot | Zero-gamma | `zgl_reliable` | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|---|
| SPY | 763.09 | `null` | **false** | −$1.872B | FULLY_NEGATIVE | 780 | 760 |
| QQQ | 710.77 | 208.83 *(garbage)* | **false** | −$777.4M | NEGATIVE *(API said POSITIVE — overruled)* | 730 | 710 |
| IWM | 297.66 | not resolved | — | −$806.8M *(50 strikes; largest = 36%)* | negative | — | 285 (pin, 4.25% away) |

**Substrate defect, stated up front:** the CLI's `regime` field **contradicts its own `total_gex` sign on 3 of the last 4 sessions** for both SPY and QQQ, and `zero_gamma_level` is null-or-extrapolated on nearly every recent session. Today's QQQ label of `POSITIVE` alongside a −$777M total_gex and VIX +7.52% is internally incoherent; the per-strike concentration resolves it to short-gamma. Both indices are marked `zgl_reliable=false` and read off `total_gex` sign + spot-vs-wall position instead.

`uw options-flow dte-volume-share` (MARKET-level): 0DTE **23.4%**, weeklies **34.4%**, monthlies **25.4%**, LEAPs **4.6%** → `regime_hint` **BALANCED**. Monthlies+LEAPs = 30.0%. Neither retail- nor institutional-dominated, so rotation calls get **no** benefit-of-the-doubt adjustment in either direction.

`uw historical vrp`: **SPY FAIR +0.0075** (IV30 0.133 vs realised 0.1255) · **QQQ FAIR −0.0208** (IV30 0.2027 vs realised **0.2234** — implied *below* realised). There is **no index-level VRP edge in either direction today**; neither premium-selling nor premium-buying lanes get a tailwind. Realised vol: SPY rv20 12.8 / rv60 12.4; QQQ rv20 22.2 / rv60 23.7; IWM rv20 15.1 / rv60 13.3; SMH rv20 45.3 / rv60 49.4.

**Macro backdrop** (`scripts/fred_macro.py`): yield curve **normal** (10Y−2Y +0.50) · core CPI **2.79%** YoY · core PCE **3.29%** YoY · unemployment **4.1%** · payrolls **−23k MoM (contraction)** · 10Y **4.65%** (30d flat) · 2Y 4.19% · USD **weakening** (−1.41 over 30d) · fed funds 3.63%. **This is a stagflationary tilt: core PCE well above target while payrolls contract.** The fundamentals-gate enrichment added the long end, which FRED's 10Y read misses: the **30Y spiked to 5.28% this week — the worst bond selloff since 2007**, with Treasury's doubled long-bond buybacks failing to hold yields down.

**Forward `event_risk` (trading days from T+0 = 2026-08-20):**

| Event | Date | T+ | Impact |
|---|---|---|---|
| **Monthly OPEX (third Friday)** | 2026-08-21 | T+1 | HIGH (mechanical) |
| **PCE / Personal Income & Outlays** | 2026-08-26 | T+4 | HIGH |
| Weekly jobless claims | 2026-08-27 | T+5 | MEDIUM |
| **Jackson Hole Symposium** | 2026-08-27 → 29 | T+5..7 | HIGH |
| **Warsh — FIRST keynote as Fed Chair** | 2026-08-28 | T+6 | **HIGH — un-priced policy-tone risk** |
| Weekly jobless claims | 2026-09-03 | T+10 | MEDIUM |
| August NFP | 2026-09-04 | T+11 | HIGH |
| August CPI | 2026-09-11 | T+16 | HIGH |
| FOMC + SEP | 2026-09-15/16 | T+18/19 | HIGH |

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** Prose-only, **0 rubric points**, no backtested predictive claim. Scope is SPY and QQQ only.

**The dominant caveat today is OPEX eve.** `expiry_heatmap` shows the **2026-08-21 expiry carries $12.38B notional — more than 2× the next-largest bucket** (09-18 monthly, $5.32B), and `pin-risk` puts SPY/QQQ at `dte_to_opex: 0`. A large fraction of the OI generating tonight's book **evaporates tomorrow afternoon**. This map therefore **overstates tomorrow's effective gamma through the OPEX unwind and understates the cleaner post-expiry regime** that emerges Friday afternoon. Treat every level as valid for the AM session only.

**SPY** — genuinely short-gamma; the API label and `total_gex` sign agree today. The per-strike grid is a *gamma canyon straddling spot*: 760 at −$285.7M just below, and **765 at −$396M — the single most negative strike on the entire board — just 0.25% above spot**. There is no cushion where price actually sits; the first dampening pocket is 780, 2.2% away. This is fully consistent with VIX +7.52%, so there is no long-vs-short-gamma tension to resolve. **Regime freshness: NOT fresh or stable** — the book chopped POSITIVE → POSITIVE → FULLY_NEGATIVE → FULLY_NEGATIVE → POSITIVE → FULLY_NEGATIVE across 08-13…08-20. Today's print is one more oscillation, not a durable break.
**Structure bias:** short-gamma → favor debit verticals / directional 0DTE over premium selling. If selling income anyway, only a very wide iron condor with shorts **outside the 758–768 chop zone**, sized down.

**QQQ** — the `POSITIVE` label is **overruled**. `total_gex` is −$777M and the largest negative-GEX strike on the whole board (**710, −$248M**) sits directly on spot, flanked by negatives both sides (700 −$101M, 705 −$79M, 711 −$41M, 712 −$37M, 715 −$50M). No cushion until 730, 2.7% away. **Structure bias:** avoid short premium in the 700–715 pocket; favor debit verticals, and if selling premium at all push strikes well outside 700/730 at the 0.5× size Step 0 already imposes.

**Mandatory caveats:** EOD is a **prior, not a target** — fresh 0DTE OI floods in during the first 30–60 minutes and re-computes both walls. **ZGL is unreliable on both names** (`null` on SPY, a ~71% miss on QQQ) — fall back to `total_gex` sign + spot-vs-wall. **Gap risk voids the prior** — the OPEX unwind is its own gap event, and PCE (T+4) / Warsh (T+6) sit just past this window. **Tooling limit:** `gex --dte-max 1` errors, so this is the standing **0–45 DTE** book as a proxy, not the isolated D+1 expiry. **This is the SPY/QQQ ETF book, not the cleaner SPX/NDX index book.**

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — the validated stack)

Both indices return `sell_premium: true`, `vol_state` **MID**, verdict `GO_PREMIUM_SELL_INTRADAY`.

| | SPY | QQQ |
|---|---|---|
| implied move / expected range | 0.88% / **1.20%** | 1.36% / **2.01%** |
| `size_scalar` | 1.0 | **0.5** |
| structure | wide iron condor, wings ≈ ±1.2% | wide iron condor, wings ≈ ±2.01%, half size |
| n=60 win rate | 86.7% | 85.0% |
| mean PnL open **GROSS** | 0.200% | 0.331% |
| mean PnL open **NET** | **0.100%** | **0.231%** |
| worst day | −1.4% | −2.453% |

`pnl_basis` is **percent-of-underlying-spot-notional, GROSS** — not premium-collected, not margin-relative — so "+0.10%/day" is tiny in absolute terms. **Lead with net.** `round_trip_cost_pct_assumed` 0.1%.

**Two caveats that should govern whether this is traded at all:**
1. **KNIFE-EDGE VIX CLASSIFICATION.** VIX closed **16.01** against a LOW/MID tercile boundary of **16.00**. That is a **0.01-point** classification. One tick lower and SPY reads LOW, where net expectancy is 0.060 − 0.100 = **−0.040%, negative**. Treat SPY's MID label as unreliable.
2. **It contradicts §2.** The premium-selling stack says sell; the standing gamma book says both indices are short-gamma with negative pockets on spot. Those disagree. Resolve toward smaller size or standing aside.

QQQ additionally carries front-end backwardation (0DTE IV **1.35× VIX**). That is independently corroborated: vol-surface-scout's hygiene-corrected QQQ is genuinely **KINKED with the hump at dte8 = the 2026-08-28 Warsh-keynote expiry**, and its `base_shape` is also BACKWARDATION — so the front-end bid is **real and event-structured, not 0DTE optical noise**.

**Promotion bar unchanged:** advisory / 0 rubric points **permanently** until BOTH a vol-shock day enters the sample (the short-vol left tail is currently **UNSAMPLED**) AND net expectancy clears a tail-aware bar. Win-rate is explicitly **not** the promotion metric for a negatively-skewed short-vol strategy.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

**Exactly one name earns the mechanized +1 line: IWM, direction SHORT.**

`scripts/dex_flip.py`: `qualifies=True`. net_dex **2026-08-19 +$3,021,577,102 → 2026-08-20 −$1,668,122,548**; the prior **11 sessions (08-05…08-19) were all positive**. |flip| $1,668,122,548 vs floor $1,562,738,301 (0.25× trailing-10 median $6,250,953,206) ⇒ **`magnitude_ratio` 1.07 — clears by only 7%**. `sign_changes_in_window` 1, **`whipsaw_warning` False**. Confirmed not a single-strike artifact (−$806.8M total across 50 strikes; largest strike 295 is 36%). Corroborated by 4 consecutive negative-`total_gex` sessions.

**The vanna-squeeze disjunct is FALSE for all 12 names scanned.** Dated `^VIX` closes: 14.25 → 15.19 → 15.84 → 14.89 → **16.01**, +12.3% over 5 sessions. VIX is **rising**, so every put-heavy book reads as bearish vanna *pressure*, never a squeeze.

Others, and why none qualify: **SPY** missed on magnitude (0.35× floor) despite net_dex collapsing >90% intraweek and flipping today. **QQQ / GOOGL** are pre-flip decay with no sign change yet (QQQ is one session away at +$0.38B). **SMH / META** flipped 3–4 sessions ago — expired triggers, not fresh. **ORCL** has a tool-confirmed GEX regime flip (POSITIVE→NEGATIVE on 08-17, held 4 sessions) but no DEX sign change. **TSLA** (5 sign changes) and **AMAT** (6 GEX regime flips in 10 days) are explicit whipsaw disqualifications. **MU** is the only call-heavy book in the set and the only name above the panic bar (front-end 1.123 BACKWARDATION).

One distinction worth carrying: **META (−8.4% on the week), AVGO (−13.3%) and COHR (−19% in 3 sessions)** all have short dealer books, but their moves have *already happened*. Those books are **confirmatory, not anticipatory** — the opposite of what a swing thesis needs.

---

## 2b. Sector Rotation

**Rotation regime call: `no_change`, low confidence.** Today is a broad VIX-driven risk-off session, not a rotation. **Zero names pass the conditional sector-leader +1 gate.**

**Correction to my own Step 0 framing.** I initially wrote that netted and gross sector flow disagree on 5 of 6 named sectors. Recomputed from the two cache files, it is **3 agree / 3 disagree**:

| Sector | Netted (`market-regime`) | Gross (`sector-flow`) | Agreement |
|---|---|---|---|
| Communication Services | +$78.5M | −$1,322.2M | **DISAGREE** |
| Industrials | +$49.8M | −$840.6M | **DISAGREE** |
| Healthcare | −$92.2M | +$1,082.5M | **DISAGREE** |
| Financial Services | +$25.0M | +$182.1M | AGREE |
| Consumer Cyclical | −$164.8M | −$738.2M | AGREE |
| Technology | −$56.6M | −$1,096.2M | AGREE |

The bottom line is unchanged, but the stated fact was wrong.

**Structural limit that removes half the tape from consideration:** `market-regime.sector_rotation` is a **top-3/bottom-3 truncation** — only 6 of 11 GICS sectors have a netted entry at all. **Energy, Basic Materials, Consumer Defensive, Real Estate and Utilities have NO netted direction today** and are un-callable under C55 regardless of what persistence says.

**`sector-flow-persistence` has zero discrimination today**: `trend: INFLOW` on **10 of 11 sectors** (score 1.0 on six, 0.8 on four); only Utilities differs (ROTATING, 0.6). It is sign-agnostic gross turnover, and it and `sector-flow` are **one source, not two**. The 0.8 scores are simply the four sectors that flipped hard negative *today* after four positive days.

**The Healthcare print is an MRNA artifact, not a rotation.** Gross shows the largest positive premium on the tape (+$1.08B, monotone INFLOW all 5 days) while netted shows OUT (−$92.2M); XLV was the **worst** 1-day sector (−1.87%) yet the **second-best** 5-day (+2.38%). **MRNA −23.55% today after +109.5% over the prior five sessions** is distorting the whole sector. Internally the sector is split — XLV bullish (+$6.85M 5d) but **XBI bearish (−$2.93M)** — and a dense life-science-tools/diagnostics cluster (ILMN, RGEN, IQV, NTRA, LH, RVTY, TWST, TXG) was making new highs on the day XLV was worst. That is single-name noise plus an intra-sector divergence, not a sector call.

**ETF flow tape (advisory, 0 points)** — 21 ETFs ranked on 5d `cumulative-premium-flow`:

| ETF | Net 5d | Trend | GICS agreement | Deep-pull note |
|---|---|---|---|---|
| SMH | +$20.09M | MIXED | disagree | Sweeps show urgent **0DTE put buying** (635/655, ~$52M) hitting the bid — today's urgency is bearish despite positive 5d flow |
| XLV | +$6.85M | BULLISH | disagree (netted OUT) | Top DP print is a **closing-cross artifact** (−$53.4M at 4.65 below mid) |
| XLK | +$3.87M | BULLISH | disagree | Meaningful **2027-06 long-dated put buying** at 180/185 (~$1.7M) — downside protection being added |
| IGV | **−$11.17M** | BEARISH | **agree** (netted + gross both OUT) | Cleanest Tech-negative confirmation, but on artifact-contaminated DP size |
| GDX | **−$21.37M** | BEARISH | n/a | Largest outflow in the universe, yet sweeps are **call-dominant** (~$19M vs ~$4M) — genuine internal divergence |
| EWY | −$10.35M | MIXED | n/a | Heavily **put-weighted, long-dated** (Jan-2027/Oct-2026, ~$13M) — cleanest bearish read in the deep-pull set |

Financial Services is the only sector with gross+netted agreement *and* a clean 5-day history — but its only floor-passing single-name leaders are **IREN and WULF, both Bitcoin miners**, not banks or insurers. That is a GICS-classification artifact, and it guts the "value rotation" reading. **Everything routes to `watch_only`.**

---

## 3. Swing Setups (1–6 weeks)

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **IWM** | **4** (LOW) | Small-cap dealer positioning flipped short for the first time in 12 sessions alongside an institutional September bear put vertical, into a stagflationary macro backdrop that hits Russell constituents' floating-rate/refi exposure harder than mega-caps | Bear put debit vertical, long 295P / short 285P, exp **2026-09-11**, ~$2.01 debit, 10pt wide, breakeven ≈$292.99 | net_dex reclaims positive ≥3 sessions post-OPEX, OR total_gex flips positive, OR IWM reclaims **$302** (the 08-19 close), invalidating the lower-high sequence 305.09 → 304.06 → 300.23 → 301.72 → 297.67 | **`watch_only` — NOT SIZED** |

### 3a. Long swings (regime-aligned)

**Empty.** No long cleared the confluence gate. `accumulation-hunter` returned **zero** names — the rubric's largest line (+3) is unearned by any ticker on the board today.

The near-misses are instructive and all failed the same way. **IREN, META, AMAT, SPCX, GOOG, GEV** each cleared institutional-tier block confirmation and then failed `conviction-matrix`, four of them with the identical explanation: **"Dark pool buying + call selling — yield enhancement, capping upside."** With OPEX tomorrow, that is a dateable **buy-write overlay** signature — institutions buying stock in the dark pool while writing calls against it to harvest elevated IV — not stealth accumulation. **GMAB, KBH, SSRM** passed conviction-matrix and failed elsewhere: GMAB on OI **UNWINDING** plus a trivial $390K cum-flow; KBH on **zero mega/block trades all session**; SSRM on n=2 institutional-tier depth.

### 3b. Short / fade swings (defined risk only)

**IWM** is the only entry, carried in full above. **All directional shorts print as `watch_only` (2026-08-01 P0 #1)** — the thesis is generated, scored and serialized so the counterfactual keeps resolving, but nothing is sized.

Ten-day flow corroborates the direction: `uw historical trend --days 10` returns **8 bearish days / 2 bullish**, with `net_flow` negative on every recent session (−$20.7M, −$7.9M, −$28.2M, −$24.0M, −$25.0M) and total OI building **10.01M → 10.48M**. P/C 2.43 today; IV rank 9.9.

`contrarian-scanner` returned **zero** fade candidates and the null is structural, not marginal: across ~30 names scanned, **not one hit a BULLISH_EXTREME** — every statistical extreme found was BEARISH_EXTREME, the opposite shape from what the −2 line targets. All three legs fail (no crowded long; "rising" is unverifiable because `pc-ratio-zscore` has no `--date`; VRP is not positive). Thin-book artifacts were correctly discarded rather than traded: **MTRN z=27.8** (2 usable expiries), **ADC z=9.46** (P/C 200.25 on $210 of bullish premium), **HXL z=13.9**.

**Sweeps (informational — 0 rubric points).** Persistence-ranked, non-mega: **MRVL** bullish 3/5 (+5.79% today, +12.98% on the week — the cleanest actionable non-mega name), **INTC** bearish 5/5, **SNDK/AMD** bearish 5/5, **NBIS** bearish 4/5. The two largest headline prints are **probable OPEX mechanics, not conviction**: **TSLA** −$114M at **DTE 1**, and **MU** −$91M at DTE 1 hit on *both* ask ($303M) and bid ($167M) at the same strike/expiry — a roll signature. **SPCX** is internally conflicted: it tops the bullish net-premium leaderboard (+$110M) while its single largest identifiable sweep is a **$122M put** (DTE 29) — a straddle/hedge, not a clean long.

---

## 4. LEAP Builds (6–24 months)

**Empty — no LEAP sized.**

**ET (Energy Transfer)** was the sole name clearing the gate stack (**7 of 8 scored gates**; gate 9 unavailable, `yahoo_fundamentals: HTTP 401`, which does not count against it under the graceful-skip rule) and it **failed the Step 3 confluence gate on breadth** — `leap-positioning-radar` flagged it, `accumulation-hunter` did not. It then scored **0**.

The evidence was genuinely good: a **Dec-2028 (848 DTE) call chain present in `top_contracts` on all 10 covered sessions**, strikes laddering **$22 → $32 → $37** as spot rose (incremental conviction, not a lottery ticket), `consecutive_build_days` 9, `rolls_detected` 0 on both dates, ask:bid ≈ **18:1** (3,628 vs 201) on the DTE-848 line, a $10.57M single DP print at $21.14 with levels clustered $21.14–$21.32 (**not** closing-cross-shaped). C12 verified independently: **$21.21 close, $206.0M 20d dollar-ADV**.

The honest weaknesses, which is why it stays out: `net_as_pct_of_gross` is only **5.6%** over 90d; `institutional-accumulation` **failed on 2 of 3 days**; `conviction-matrix` reads **34.4%**, clearing the >70 bar only via an alternative LEAP-tenor path; and the 90d/30d split (+$9.28M vs +$10.23M ⇒ days 31–90 ≈ **−$0.95M**) makes this a **fresh thesis, not smooth accretion**.

**Disqualifications elsewhere were principled, not arbitrary:** **RKT** hard-failed the required 90d flow gate (−$21.89M BEARISH). **SHEL** and **NVO** were killed by the dividend/financing-arb rule — deep-ITM long-dated calls on high-dividend names, and NVO's build was **bid-dominant (13,669 vs 4,357)**, i.e. covered-call writing, not buying. **MSTR** entries were puts (out of scope). **OPEN** failed C12 at $3.465.

**Notably, none of the Step-0 bullish premium leaders registered a DTE>180 build large enough to enter the top-20 discovery scan at all.**

---

## 5. Volatility Surface

**The hygiene layer is the story.** Raw `iv-term-structure` labelled **BACKWARDATION on 17 of 21 names (81%)**. After dropping the 0DTE/expired bucket and sub-15-contract tenors, **11 of 21 (52%) flipped**. An 81% population firing rate is not a signal. Corrected book: 9 BACKWARDATION / **8 KINKED** / 1 CONTANGO / 2 `NO_NEAR_TENOR` / 1 `INSUFFICIENT_DATA`. `min_contracts` = **15** (script default — a tunable, *not* audit-frozen). `NO_NEAR_TENOR`: **FTEC, CHD** — front end **unmeasurable**, which is never the same as calm. `INSUFFICIENT_DATA`: **HXL** (1 surviving tenor — do not trade).

**The KINKED book maps almost perfectly onto the event calendar**, which is itself the finding — the surface is pricing exactly the two named Tier-1 catalysts and nothing more:

| Ticker | kink_dte | kink_expiry | Prominence | Catalyst at that expiry |
|---|---|---|---|---|
| **AVGO** | 6 | 2026-08-26 | **42.8%** (largest in book) | **PCE** — no earnings confound |
| SNOW | 15 | 2026-09-04 | 18.7% | Earnings 09-02 |
| LRCX | 29 | 2026-09-18 | 14.8% | OPEX cycle / FOMC-adjacent |
| SOXL | 8 | 2026-08-28 | 11.7% | **Jackson Hole / Warsh** |
| **LULU** | 15 | 2026-09-04 | 10.0% | Earnings **09-02** |
| SPY | 6 | 2026-08-26 | 9.9% | **PCE** |
| QQQ | 8 | 2026-08-28 | 6.4% | **Jackson Hole / Warsh** |
| SMH | 6 | 2026-08-26 | 6.4% | **PCE** |
| IWM | 41 | 2026-09-30 | 5.1% *(at the floor — marginal)* | quarter-end |

**Single-name VRP inverts the naive high-IV-rank read, and this is the section's most actionable finding.**

- **MRNA's IV rank of 100 is stale.** VRP is **−4.15** (IV30 1.10 vs realised **5.25** — blown out by the −23.55% print on top of a +109.5% run). Options there are **cheap relative to what just happened**, not rich. That is a hard **SELL VOL disqualifier** on the name the funnel ranked as a top vol candidate. `iv-percentile-zscore` 98.9 but **`dates_used` = 91**, below the 120-day floor ⇒ provisional.
- **The entire GLW / WDC / LITE / COHR / LRCX / SOXL / MTRN / SMH cluster is uniformly PREMIUM_BUYING.** Their high IV rank is pre-drawdown and stale against the semis tape; realised vol has outrun the options market's repricing. **Sell-vol is disqualified across the whole cluster.**
- Only **ROST, OKTA, LULU, AVGO** have VRP aligned for premium selling — and **ROST is then killed anyway** by a front-end ratio of **1.688** with no confirmed-falling trend (the classic "event still pending, don't fade it" case).

**Net: no clean BACKWARDATION calendar clears both the ratio-trend and VRP-alignment bars today.** XOP is nearest (ratio ≈1.05, FAIR VRP) and is watch-only pending a falling-ratio confirmation. **AVGO** is the cleanest KINKED + VRP-aligned name on the board (implied move ≈8.4% into PCE) but it had **only one flagging agent** and never entered the rubric.

**Earnings vol book** (all capped at **starter** by the `earnings_vol` 0.55 class ceiling regardless of conviction; every implied move below is **derived**, because `earnings-catalyst.implied_move_perc` remains ~16× too small — it reported PANW at 2.0% and CRM at 1.5%):

| Ticker | Earnings | Verdict | Implied move | Note |
|---|---|---|---|---|
| **LULU** | **2026-09-02** | **BUY VOL, put-biased** | **11.01%** | $71.9M one-sided bearish book; 11% is low vs a 15–20% realised history — **but see the VETO in §6** |
| PDD | 2026-08-24 | BUY VOL | 7.75% | Kink prominence 23.9%, flow confirms |
| PANW | 2026-09-01 | SELL VOL (half) | 11.94% | Back-month flat = disqualifier |
| SNOW | 2026-09-02 | SELL VOL (half) | 14.73% | Second kink at 09-18 is FOMC-adjacent — possible macro contamination |
| DG | 2026-08-27 | SELL VOL (starter) | 9.22% | **Only genuinely stretched back tail in the scan** (skew +0.065 / ratio 1.16 TAIL_HEDGING) |
| BJ | **2026-08-21** | SELL VOL (starter) | 6.50% | Earnings **and** OPEX settlement on the same day — dual mechanism |

**DELL and CRM were rejected for exactly the right reason:** their kinks sit at dte29 adjacent to **FOMC 09-15/16**, not at their own earnings tenors — macro bleed misread as company event pricing.

---

## 6. Risk & Correlation

**Macro headline:** stagflationary tilt — core PCE **3.29%** YoY *while* payrolls print **−23k**; curve normal-but-flat (+0.50); 10Y 4.65% flat, **30Y at 5.28% after the worst bond selloff since 2007**; USD weakening. Forward calendar as tabulated in §1 — **PCE T+4 and the Warsh keynote T+6 both land inside any 1–4 week swing horizon.**

**Correlation clusters: none, and none was manufactured.** The book is one name; `uw risk portfolio-correlation --symbols IWM,LULU` returns `high_correlations: null`.

> **Latent cluster flagged for tomorrow.** `IWM/SPY` correlation is **0.839, warning HIGH** — well past the ≥0.70 threshold. `multileg-strategist` independently found a **SPY Sept-4 bear put vertical** that failed the confluence gate on *breadth, not quality*. IWM-short and SPY-short are **the same trade**. No deduction is owed today because SPY is not in the book — but if SPY ever clears the gate while IWM is carried, that is an automatic −1 tier, and the kept member would be **SPY** (`multi_day_repeat_verified` TRUE vs IWM's FALSE).

**Gate stack applied to IWM** — all 9 keys, including the no-ops:

| Gate | Verdict |
|---|---|
| `regime` | **−1 tier** — trend field reads UPTREND; IWM is +10.4% above SMA200 and −2.46% off its 52w high ⇒ countertrend short. Fired despite today's bearish tape, which cuts the other way. |
| `vrp` | no-op — FAIR/FAIR; the trade is directional and a same-expiry vertical largely nets its vega |
| `panic` | no-op — `front-end-iv-ratio --near-dte 7` = **0.821 CONTANGO**, far below 1.10 (reproduces dealer-positioning exactly) |
| `cluster` | no-op — 1-name book; latent IWM/SPY 0.839 recorded |
| `sector` | no-op — `no_change`, zero qualifying names |
| `fundamentals` | no-op — **NA**, `tier_adjustment 0`. **NA never penalizes.** |
| `event_risk` | no-op via the defined-risk exemption, **but 3 named in-horizon binaries recorded** (OPEX T+1, PCE T+4, Warsh T+6). Non-binding — short routing already floors the size. |
| `debate` | **−1 tier** — the side arguing *for* the trade returned **0.35** vs 0.65 against |
| `rubric_regime` | **capped half** — OUT-OF-REGIME |

**On the debate gate's orientation, because it inverts on a short and is easy to get backwards:** the call is SHORT, so the **bear argued FOR** the trade and the **bull argued AGAINST**. Residuals are `bull 0.65 / bear 0.35`. Read literally, "bear ≥ bull" is `0.35 ≥ 0.65` = false — but that string is written for a *long* call where bull = pro-trade. Applied literally to a short it would fire only when the *anti*-trade side is weak, i.e. exactly backwards. The semantically correct test (`pro_trade ≤ anti_trade`) **fires**. The advocate for this trade could not clear a coin flip.

The bear's own concession is the most useful line in the debate: the `ALL/short` McNemar result (**p=0.0115→0.0038, BH-surviving; UP −13.0pp / DOWN −14.1pp**) indicts the short **generation process**, not short timing — and IWM was produced by exactly that process. A near-identical deficit in both tapes is **mis-selection, not mistiming**, which a defined-risk wrapper does nothing to fix.

**Fundamentals verdicts:**
- **IWM → NA** (`tier_adjustment 0`). An ETF: `earnings_surprises=[]` and `insider_mspr=[]` are **structurally empty, not a data failure**. The macro backdrop corroborates the short in prose; the counter-fact is that IWM is **+10.40% above its SMA200 and only −2.46% off its 52-week high**, RSI 49.
- **LULU → VETO** (`tier_adjustment: veto`) — **on real data, not absence**: beat streak **3 of 4** (+2.76%, +12.63%, +5.62%; latest a −1.49% miss), insider MSPR 3-month average **+78.42**, positive in **6 of 7 months** (+96.4 in June), P/E 9.83, debt/equity **0**, margins 55.7 / 18.3 / 13.0. That is the opposite of the distribution signature this gate exists to catch. Countervailing and genuinely dated: EPS growth −16.12% YoY, **Soros dissolved its stake (08-14)**, and the AI chief exited ahead of the CEO transition (**08-14**) — which is precisely when the 30-day bearish book began.

**Breadth cross-check (advisory):** 157 advancers / 342 decliners, **31.21% green**. **No divergence** — the index is red and breadth is red, so `uw` and `fz` agree. The distribution tell (green index with `pct_green < 50`) is not present today.

**Adverse-flow scan** against `conviction_2026-08-19` (one name, **GDX**): 3 alerts — 1.7× volume, a **$30.2M single DP print**, **+92,864 net OI**. Scan shows close 99.85, `flow_direction` bearish, net −$10.2M. Yesterday's GDX thesis was also a `watch_only` short, so today's flow **confirms rather than reverses** it. Graded **monitor, direction-ambiguous** — the bearish label is a net-premium read while the raw mix is call-heavy (P/C 0.705). **Not an exit candidate; there was never a position to exit.**

**Hedge sleeve: none warranted.** Zero sized positions ⇒ zero net delta ⇒ nothing to hedge. The directional-skew trigger is not merely unmet, it is **undefined (0/0)**. Buying index verticals or a VIX ladder against an empty book is not risk management — it is a naked directional bet wearing a hedge's clothes.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Empty. No name reached MEDIUM (≥7), let alone HIGH (≥9).** The highest score on the board was **4**.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`, from the most recent `/calibration-audit` (**2026-08-15**, `phase_3_calibration`):

| Tier | n | realised WR | mean P&L | payoff ratio | capped ½-Kelly |
|---|---|---|---|---|---|
| HIGH | 7 | **0.143** | −2.441% | 0.72 | 0.0 |
| MEDIUM | 19 | **0.526** | **+0.104%** | 0.948 | 0.0132 |
| LOW | 108 | 0.389 | −1.963% | **1.008** | 0.0 |
| DROP | 438 | 0.420 | −2.870% | 0.787 | 0.0 |

Realised order is **MEDIUM > DROP > LOW > HIGH** — tier inversion for a **7th consecutive cycle**, present in every era stratum. C3 gate status **`ADVISORY_ONLY`** (n=27 < 30 *and* tier×expectancy non-monotone); the win-rate ladder stays the live sizer.

One precision note, because the claim is easy to overstate: **DROP beats LOW on win-rate (0.420 vs 0.389) but not on mean P&L (−2.870% vs −1.963%)** in this audit. "The DROP pile outperforms the traded book" holds on hit-rate, not on expectancy. MEDIUM is the only tier with positive expectancy and the only payoff ratio near 1.0.

### Scored book (the full audit trail for the one call that exists)

**IWM** · `short` · swing · **raw_score 4** · tier **LOW** · `dominant_signal_class` `multileg_directional` · `confluence_score` `null`

| # | Rubric line | Pts | Source agent | Source tool |
|---|---|---|---|---|
| 1 | +1 mechanized DEX flip / vanna-squeeze in trade direction | **+1** | dealer-positioning-strategist | `scripts/dex_flip.py` |
| 2 | +2 multileg directional structure (term-structure-anchored) | **+2** | multileg-strategist | `uw hot-chains multileg` |
| 3 | +1 multi-day OI build (`oi-trend` BUILDING, ≥5d) | **+1** | signal-confluence-quant | `uw historical oi-trend` |
| | **Σ = 4 = raw_score ✓** | | | |

`cum_premium_flow_30d` **−$320,125,137** · `90d` **−$518,404,201** (days 31–90 ≈ −$198.3M — both halves agree) · `win_rate` **null**, `win_rate_source` **`NA(substrate)`** · `market_excess` **null** · `pre_risk_size` **starter** → gates → `final_size` **`watch_only`** · `fundamentals_verdict` **NA** · `debate_residuals` **{bull 0.65, bear 0.35}** · LB-gate **2 of 4** (no-op at LOW).

> **`market_excess: null` is a substantive statement, not a missing field.** `multileg_directional` is not among the 5 backtestable classes ⇒ no win-rate ⇒ no signal windows ⇒ no same-direction SPY benchmark. IWM is **not** flagged as beta; it is **unmeasured**. A future audit must not read `null` as `0`.

**The +1 OI-trend line was awarded on a direction-verified build, not the raw label.** `oi-trend` returned `BUILDING` on **14 of 14 names sampled today**, spanning both flow directions and both tapes — zero discrimination, the same failure class as `sector-flow-persistence` at 10-of-11. What earns the point is that IWM's build is overwhelmingly **put-side** and concentrated in the Sept-18 tenor (P-share **0.67 / 0.88 / 1.00** across the last three sessions). This is a tightening-only reading of a frozen line; the counterfactual is identical (+1, raw 4).

**Two independent gates kill this trade even without the short-routing rule.** Strip the routing entirely and the ladder starts at `starter`; `regime −1` and `debate −1` stack to floor it at `skip`. The routing rule and the gate stack agree, and that convergence is worth more than either alone.

**On the short-routing judgement (upheld by both the quant and risk-monitor):** IWM's expression is a defined-risk bear put vertical, and the rule carves out "a short leg inside a defined-risk spread." The carve-out **does not apply**. It targets legs that are structurally short *inside* a construct whose thesis is not directional-short — the short put in a bull put credit spread, a calendar leg, a beta-hedge sleeve. Here the structure's **entire net delta is short**, its P&L is monotone decreasing in IWM, and the short 285P is a **financing** leg, not a hedging one. This is directional short alpha wearing a spread. Reading the carve-out any wider would let every short re-enter through its expression.

### Dropped rows (serialized so the DROP pile stays measurable)

- **LULU** raw **2** — dropped twice over. The **C13 ruling** stripped the vol-surface +1 (*"earnings-scout owns `earnings_vol` for the KINKED-at-earnings case; vol-surface does not separately score it"* — both agents reported the **same** kink object, 09-04 at 10.0% prominence), and fundamentals **VETO**'d it independently. Its flow was the cleanest on the board (**−$397.5M 30d at 40.25% of gross**, vs IWM's 6.02%) — but 90d −$201.5M implies days 31–90 ≈ **+$196.0M BULLISH**, so the bearish book is *entirely* a last-30-days phenomenon, not durable accretion. **Unresolved direction conflict recorded:** earnings-scout says BUY VOL; vol-surface computes VRP +0.235 PREMIUM_SELLING and would SELL the 09-04 straddle. The sign of the vega flips between them — that is the trade, not a detail. vol-surface reads a backward-looking rv30 of 0.339 that *cannot contain* the 09-02 event, so its "+0.235 premium" is substantially the event risk premium itself.
- **SPY** raw **2** — **failed the confluence gate on breadth, not quality.** This is the single strongest structure on the board: a Sept-4 NFP-day bear put vertical (long 752P / short 720P, ~$4.1M), **OPENING confirmed** by near-identical same-day OI builds on 08-19 (720P +12,372 / 752P +12,351), and the **only `multi_day_repeat_verified: TRUE`** spread today. The frozen rubric scores it 2. Registered as an observation, **not** a proposed fix — the additive rubric has had no line rewarding structural quality or multi-day repeat confirmation since sweep-persistence was removed (2026-05-23 P0.3), and one observation is exactly the evidence base the freeze exists to reject.
- **ET** raw **0** — the LEAP case in §4. Register tension worth logging: ET's **17.6%** net-as-%-of-gross is *healthier* than IWM's 6.02% — its flow is small in dollars because ET's options market is small, not because it is churny. The absolute $50M floor penalises a $21 mid-cap MLP for its market cap rather than its signal quality, where a scale-relative floor (as C11 already uses) would discriminate better. **Floor applied as frozen, not adjusted.**

### Conviction rubric (frozen, version `2026-06-12`) — embedded verbatim for audit

```
Daily conviction score = Σ:
  +1  MECHANIZED DEX flip / vanna-squeeze in trade direction (verified SIGN CHANGE via scripts/dex_flip.py)
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified institutional
      tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms (sign aligned AND
      |cum_flow_30d| >= $50M); else halved to +1
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days >= 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: only when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts
  +1  uw historical cumulative-premium-flow net directional accretion in trade direction (30d) —
      INTENT-SCREENED: (a) no C28 distribution_flag, AND (b) on dividend payers in an ex-div window the
      accreting prints are NOT deep-ITM sub-parity calls
  +1  sector-rotation-strategist names ticker as single-name leader in a rotating sector — CONDITIONAL:
      (a) persistence_score >= 0.6 AND (b) cum_flow_30d direction aligned AND (c) |cum_flow_30d| >= $50M
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising pc-ratio-zscore (VRP positive)
      # INFORMED-FLOW CONTINUATION penalty, NOT "crowd is wrong, fade it"
  -3  flow_conflict — cum_premium_flow 30d direction clearly OPPOSITE dominant_signal_class
  -1  flow_conflict_lite — 30d read is MIXED (signed sum near zero, or aligned but bottom-quartile magnitude)
      # -3 and -1 are MUTUALLY EXCLUSIVE — apply one, never both
  # NOT score_components — risk-monitor TIER gates applied in 2d, contributing 0 to raw_score:
  -1  [TIER GATE] correlation cluster (pairwise corr >= 0.70)
  -3  [TIER GATE] uw risk market-regime conflicts with trade direction
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | HIGH | full (subject to Step 3a load-bearing gate + win-rate gate) |
| 7–8 | MEDIUM | half |
| 3–6 | LOW | starter / watch-only |
| ≤ 2 | drop | filtered by the quant's drop floor |

---

## 8. Watch-only — single signal, no confluence

Surfaced by one agent, failed the ≥2-agent confluence gate. **Journaling only — not for entry.**

| Ticker | Flagging agent | Read | Why it failed |
|---|---|---|---|
| **SPY** | multileg-strategist | Sept-4 NFP-day bear put vertical, `multi_day_repeat_verified` **TRUE** — the best structure on the board | 1 agent. vol-surface said "no action beyond context"; dealer-positioning `qualifies=False` (0.35× floor); gamma-flip is the §2 advisory (0 points **by design**) |
| **ET** | leap-positioning-radar | 7-of-8 LEAP gates, Dec-2028 laddered call chain, 10/10 sessions | 1 agent — accumulation-hunter did not independently flag it |
| **AVGO** | vol-surface-scout | Cleanest KINKED + VRP-aligned name; kink at **PCE**, prominence **42.8%** (largest in book) | 1 agent. accumulation-hunter rejected it; dealer-positioning NEUTRAL |
| **QQQ** | multileg-strategist (**secondary** only) | Sept-18 bull put credit spread, ~$14.2M credit — resolves the apparent bullish/bearish contradiction in the screener | Agent explicitly withheld the full +2 (both-bid side-tag inference is plausible, not confirmed); contrarian rejected the fade |
| **PDD / PANW / SNOW / DG / BJ** | earnings-scout | Vol book, §5 | 1 agent each |
| **NFLX / NVDA / GLD / FXI** | opex-pin-strategist | Top-4 pin book, §3 note below | 1 agent each; the +1 OPEX line alone = raw 1, below the drop floor regardless |
| **MRVL** | sweep-tracker | Bullish 3/5 persistence, +5.79% / +12.98% 5d | Sweep lane earns **0 points**; earnings-scout returned `shape: FLAT`, no kink |
| **GOOGL** | — | **Negative flag** — fresh Tier-1 `FLOOR_PUT_BLOCK` ($8.9M, DTE 1, size/OI 1.97) + BEARISH_EXTREME z=2.60 *while* netting +$42.6M bullish premium | Carry as a **caution on GOOGL longs**, not a candidate. accumulation-hunter rejected GOOG (cum-flow −$137.6M, wrong sign) |
| **ROST** | — | Top bearish funnel seed (score 6, IV rank 100, 17.9× volume, P/C 2.59) | **Fails its own z-test: z=0.761, NORMAL.** Raw P/C does not clear its own 20-day distribution; IV is likely WMT-reaction bleed |
| **MRNA** | — | IV rank 100 | **VRP −4.15** ⇒ options are cheap, not rich. Hard sell-vol disqualifier |
| **GLD** | opex-pin-strategist | Pin at 420 (1.17%), confirmed +$110.7M gamma wall | **`distribution_flag: present`** — ~$63M of institutional call OI *closed* (Sept-18 430C −49,741 ≈$31.3M; 415C −27,487 ≈$32.0M, dte 29, **not** OPEX-roll mechanics) against +$39.3M bullish screener premium. **CAUTION, never CONFIRM** |

**OPEX pin book (OPEX-week only).** `opex-pin-strategist` returned an honest **4 names, not 5**: **NFLX** (pin 80, 0.19% away, gamma +$52.1M), **NVDA** (220, 1.37%, +$104.1M), **GLD** (420, 1.17%, +$110.7M), **FXI** (36, 0.93%, +$21.0M — thinnest wall, smallest size). The important finding is a substrate defect: **`pin-risk.nearest_high_oi_strike` is frequently NOT the dealer wall.** The four largest `pin_score` values on the board — **HYG (−$1.38B), TLT (−$218M), QQQ (−$100.6M), LQD (−$224.7M)** — all have **negative** net GEX at the nominal pin strike; the OI pile sits one strike *below* the real wall. And SPY's top-of-board 2.14M `pin_score` is a **4.90%-OTM pile with 0–1 DTE** — untradeable. Mass without proximity is not a pin. All four survivors are short-gamma structures sold into a **rising-vol** tape, which is how pin trades get run over; half normal OPEX-week size at most.

---

## Appendix — measurement defects confirmed live today

Carried for `/calibration-audit`. These are population-level findings, not per-name caveats.

1. **NEW — basket-print contamination, distinct from the known closing-cross.** A **~$500M-notional program print hit dozens of unrelated names inside a 90-second window (21:10:36–21:12Z)**: AAPL, SNDK, MSFT, CRM, NVDA all at *exactly* $500.0M, SPY at $493.5M, plus PG, AVGO, SMH, META, IREN, TPR, GOOG, LITE, SPCX. One rebalance sweeping the tape, not per-name conviction. Stacked on the closing-cross, top-bucket concentration reached **94.4% (AMAT), 91.5% (IREN), 87.6% (GEV), 71.4% (META)**. Any premium-ranked DP read today is contaminated twice over.
2. **NEW — `uw historical oi-trend` has zero discrimination.** `overall_trend: BUILDING` fired on **14 of 14** names sampled, across both flow directions and both up- and down-tape names. `contracts_with_increases > contracts_with_decreases` is structurally near-guaranteed on any liquid chain. Same failure class as `sector-flow-persistence` (10-of-11) and `front_end_iv_ratio` at the default `--near-dte`.
3. **Term-structure hygiene fired hard.** Raw BACKWARDATION on **17 of 21 (81%)**; **11 of 21 (52%) flipped** after dropping the 0DTE bucket and thin tenors.
4. **`uw insights analyst-vs-flow` has no analyst leg** — confirmed live on **0 of 19** earnings tickers. No divergence claim is possible on any name.
5. **`earnings-catalyst.implied_move_perc` remains ~16× too small** (PANW 2.0%, CRM 1.5%). Every implied move in this report is derived.
6. **GEX `regime` label contradicts its own `total_gex` sign** on 3 of the last 4 sessions for both SPY and QQQ; `zero_gamma_level` null or garbage (QQQ: **208.83** vs 710.77 spot).
7. **`iv-percentile-zscore` short-delivered** — `dates_used` = **91**, below the 120-day floor (MRNA, ROST). Percentiles provisional.
8. **`oi opex-concentration` degenerate** — top rows are 100%-concentration micro names with 1–9k total OI. No usable pin mass; the book had to be built from `pin-risk` + a GEX cross-check.
9. **`pin-risk.nearest_high_oi_strike` ≠ the dealer wall** on the four largest `pin_score` names (see §8).
10. **`fz screen` doubled-first-letter ticker bug re-confirmed, 20/20 rows on both surfaces** (AABEO/AABR/AAI…, IIOVA/MMRVI/TTALO…). De-corrupted by stripping the leading duplicate. Per-ticker `fz_enrich` is healthy and unaffected.
11. **Fleet bug (operational):** `vol-surface-scout` and `earnings-scout` collided on a shared `hygiene_out.json` scratchpad path and one clobbered the other mid-run. Needs agent-scoped output filenames.
12. **Orchestrator error, self-corrected:** Step 0 initially stated netted-vs-gross sector disagreement on 5 of 6 sectors; the correct count is **3 of 6** (§2b). Also, LULU's earnings date is **2026-09-02**, not 09-03 as first framed.
