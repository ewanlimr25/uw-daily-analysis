# Weekly Market Intelligence — Week of 2026-08-24 (ISO 2026-W35)

## Executive Summary

- **Week regime + WoW Δ:** TRANSITIONAL / UPTREND **held** at both ends — SPY 769.35, above its 20SMA (769.22) and 50SMA (753.96), −1.29% off the 90-day high — but the internals eroded underneath a static label. Options-flow breadth fell **34.6% → 30.5% bullish** (4,366 bearish-flow tickers vs 1,920 bullish on Friday), the `fz` price-breadth cross-check printed **45.53% green**, and **SPY +0.47% on the week against equal-weight RSP −0.44%** — a 91bp cap-weight divergence. VRP is negative on both indices (SPY −0.0027 FAIR; QQQ **−0.0418**, IV30 16.87% below realised 21.05%) — a premium-**buying** tape. VIX 14.43, −4.63% on the week, near cycle lows.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`.
- **Signal performance:** **4 of 14 resolved (hit rate 4/14 = 28.6%); 15 INCONCLUSIVE excluded; 44 total calls in universe (44 envelope-anchored, 0 reconstructed)** — of which 29 were directional and 15 were vol/neutral calls not gradeable under the 0.5×ATR price rule. **Capital impact: zero.** Every one of the 44 calls scored DROP tier at `skip`, `watch_only` or `veto` across all five daily envelopes.
- **Top swing build for next week:** **None sized.** The highest score on the board was raw 4 (LOW) and the best pre-risk size the quant could justify anywhere was `starter`. NOW and MSFT both gate to `skip`; MRVL and GLD route to `watch_only` under the short rule.
- **Top LEAP build:** **None.** `leap-positioning-radar` returned zero candidates — the `conviction-matrix` DIRECTIONAL_LONG confidence ceiling observed market-wide was **36.3%** against a >70 gate, making the gate effectively unsatisfiable in this tape.
- **Biggest emerging risk:** **Three Tier-1 macro binaries inside twelve trading days — NFP 2026-09-04 (T+5), CPI 2026-09-11 (T+9), FOMC/SEP 2026-09-15/16 (T+11/12)** — landing on a stagflationary print: payrolls **contracted −23k** while core PCE runs **3.34%**, 10Y at 4.67% and rising, USD weakening. Secondary: a genuine `crypto_beta_cluster` (MSTR/COIN pairwise **0.834**) and the fact that the week's advance was carried by a handful of mega-cap software names while the average stock fell.

---

## 0. Week in Review — Intra-Week Signal Performance

Universe = the union of `calls[]` across this week's five daily `decision.json` envelopes, keyed by `(ticker, direction)`. All five weekdays produced an envelope, so there is **no reconstruction and no survivorship gap**. 44 calls were emitted in total; **all 44 scored DROP tier**, so none carried capital. 29 were directional (long/short) and gradeable on price; 15 were `vol_long`/`vol_short`/`neutral` and are not resolvable under the 0.5×ATR(14) directional rule.

Resolution window runs from each call's envelope date to 2026-08-28. WIN = moved ≥0.5×ATR(14) in the call's direction; LOSS = moved ≥0.5×ATR(14) against it; INCONCLUSIVE = |move| < 0.5×ATR(14).

| Ticker | Direction | Source | Move vs ATR | Flow/OI | Grade | Note |
|---|---|---|---|---|---|---|
| SLV | short | envelope 2026-08-24 | **+1.21×** ($62.20 → $60.02, −3.5%) | cum-flow bearish, aligned | **WIN** | Precious-metals complex rolled over with GLD. |
| NVDA | long | envelope 2026-08-25 | **+0.80×** ($213.05 → $217.55, +2.1%) | flow mixed | **WIN** | The 08-25 call corrected the 08-24 short on the same name. |
| DIS | short | envelope 2026-08-26 | **+0.70×** ($109.63 → $108.10, −1.4%) | flow bearish | **WIN** | Small but clean. |
| HYG | short | envelope 2026-08-27 | **+0.78×** ($79.87 → $79.74, −0.16%) | credit hedge campaign | **WIN** | Tiny ATR (0.166) makes this a low-information win. |
| NVDA | short | envelope 2026-08-24 | **−1.54×** ($208.48 → $217.55, +4.4%) | flow mixed | **LOSS** | Direct contradiction of the 08-25 long on the same name. |
| ORCL | short | envelope 2026-08-24 | **−1.33×** ($142.45 → $150.85, +5.9%) | — | **LOSS** | Enterprise-software beat wave ran it over. |
| BBWI | short | envelope 2026-08-25 | **−1.72×** ($17.58 → $19.22, +9.3%) | — | **LOSS** | Post-earnings squeeze. |
| GLD | long | envelope 2026-08-24 | **−2.22×** ($426.69 → $408.89, −4.2%) | — | **LOSS** | Called long Monday; the desk called it short by Thursday. |
| WMT | long | envelope 2026-08-24 | **−1.19×** ($106.49 → $103.09, −3.2%) | — | **LOSS** | |
| GOOG | short | envelope 2026-08-27 | **−0.87×** ($337.71 → $342.88, +1.5%) | — | **LOSS** | |
| AVGO | short | envelope 2026-08-24 | **−0.74×** ($358.76 → $368.79, +2.8%) | — | **LOSS** | |
| MSTR | short | envelope 2026-08-24 | **−0.73×** ($122.63 → $127.31, +3.8%) | — | **LOSS** | Won on Friday alone (−7.3%) but lost the week. |
| IBIT | long | envelope 2026-08-24 | **−0.64×** ($44.64 → $43.90, −1.7%) | — | **LOSS** | |
| ISRG | short | envelope 2026-08-27 | **−0.50×** ($367.07 → $372.60, +1.5%) | — | **LOSS** | Exactly at the loss threshold. |
| INTC · MCHP · COIN · SMH · NBIS · AMD · MU(×2) · HYG(08-24) · TSLA · EWZ · META · SNDK · MRNA · MRVL | mixed | envelopes 08-24 → 08-28 | all \|move\| < 0.5×ATR | — | **INCONCLUSIVE** (15) | MRNA and MRVL were called on 08-28 itself and have a zero-session window — unresolvable by construction. |

**Hit rate 4/14 = 28.6% on resolved directional calls.** Split by side: **shorts 3 WIN / 7 LOSS (30%)**, **longs 1 WIN / 3 LOSS (25%)**. Both sides poor; n is far too small to conclude anything beyond "this week's paper book was not predictive."

Three observations that matter more than the hit rate:

**The book contradicted itself on NVDA within one session.** A short on 08-24 (LOSS, −1.54×) and a long on 08-25 (WIN, +0.80×). Both resolved consistently with the actual tape — NVDA rallied — so the 08-25 call corrected the 08-24 one. That is the system updating, not incoherence, but a weekly reader should see it stated rather than netted away. The same pattern hit GLD: long on 08-24 (LOSS, −2.22×, the week's worst), short by 08-27 (this week's scored call).

**Short generation is healthy.** 20 of 29 directional calls (69%) were shorts. Against the 2026-08-22 audit's measured finding that short-thesis *generation* had halved post-P0 (32.0% → 17.6%), this week's board runs well above even the pre-P0 baseline. The generation floor is being honored; the routing rule is not starving its own falsifier.

**Capital impact was zero, and that is the actual result.** A 28.6% hit rate on 14 unsized paper calls costs nothing. The meaningful fact is that the gate stack refused the entire week — for the 39th consecutive daily board — not that the paper calls lost.

---

## 1. Regime & WoW Delta

The label did not move. `market-regime` read TRANSITIONAL with `trend: UPTREND` on both 08-24 and 08-28, SPY above both moving averages, guidance unchanged at *"Half position sizes. Favor defined-risk strategies. Iron condors in range."* What moved was everything underneath it.

Options-flow breadth deteriorated from **34.6% to 30.5% bullish** and never came close to 50% on any covered session. The `fz` price-breadth cross-check reads **45.53% green** (229 advancers / 273 decliners, avg change −0.34%, median −0.13%) — a different data lineage reaching the same conclusion, and flagged `divergence_flag: true` against the UPTREND label. The cleanest expression is the index-versus-average-stock spread: **SPY +0.47% on the week while equal-weight RSP fell −0.44%**. The index went up because its largest constituents went up. The median stock did not.

> **Substrate caveat:** the `spy` sub-block inside `market-regime` returned byte-identical values (spot 769.35, sma_20 769.22, change_30d_pct 3.73) for both the 08-24 and 08-28 queries. It is a live snapshot, not a date-pinned field — the WoW delta above is computed from `market_breadth` and `sector_rotation`, which do vary by date, not from that block.

`dte-volume-share` (MARKET level) shows the horizon **shortening**: weeklies' share ran **0.059 → 0.213** across the week while monthlies held flat (0.158 → 0.157) and LEAPs fell (0.044 → 0.031). That is a more tactical, less committed tape, and it argues for uniformly downgrading multi-week conviction rather than any single name. `share_0dte: 0` is an EOD-parquet artifact, not a real zero.

**Macro backdrop** (`scripts/fred_macro.py`): the curve is normal at **+0.39** (10Y−2Y) with the 10Y at **4.67% and rising** (+0.06 over 30d) while the 2Y fell to 4.20% — bear-steepening. Core CPI is 2.79% but **core PCE is 3.34%**, well above target and above core CPI. Payrolls **contracted −23k**; unemployment 4.1%; fed funds 3.63%; the broad USD index **weakened** 120.57 → 118.06. That is a stagflationary configuration — softening labour into sticky inflation with a rising term premium — and it is specifically hostile to long-duration equity and specifically supportive of gold, which is worth noting given this week's scored gold call is a short.

**Forward event risk (trading days from T+0 = 2026-08-28, Labor Day 09-07 excluded):**

| Event | Date | Trading days | Tier |
|---|---|---|---|
| JOLTS | 2026-09-02 | T+3 | medium |
| Jobless claims | 2026-09-03 | T+4 | medium |
| **Nonfarm payrolls** | **2026-09-04** | **T+5** | **Tier-1** |
| PPI | 2026-09-10 | T+8 | medium-high |
| **CPI** | **2026-09-11** | **T+9** | **Tier-1** |
| **FOMC + SEP** | **2026-09-15/16** | **T+11/12** | **Tier-1** |
| Monthly OPEX | 2026-09-18 | T+14 | mechanical |

Three Tier-1 binaries inside twelve trading days is the defining feature of next week's risk. A second negative payroll print on 09-04 would reprice growth outright.

---

## 2. Sector Rotation

**Rotation regime call: `no_change` at the GICS cross-sector level — with high confidence, and for a mechanical reason worth stating.**

No sector cleared both the persistence and the magnitude bar. On the IN side, Communication Services (+$42.9M netted) clears magnitude but its persistence of 0.8 sits in the *bottom* tercile this week; Real Estate clears persistence (1.0) but its +$4.1M is far below the $37.15M median; Consumer Cyclical fails both. On the OUT side, all three outflow sectors route to **`watch_only`** — and here is the mechanical finding: **gross `sector-flow` printed a positive value on all 11 sectors this week** (call premium exceeded put premium everywhere), so gross is structurally incapable of corroborating *any* netted outflow this week. The Technology conflict is the largest instance — netted **−$387.4M OUT** against gross **+$3,750.7M IN** — but it is not unique to Technology.

| Sector | Netted (market-regime) | Gross (sector-flow) | Agreement | Persistence |
|---|---|---|---|---|
| Communication Services | **IN** +$42.9M | +$351.6M | agree | 0.8 |
| Real Estate | **IN** +$4.1M | +$4.65M | agree | 1.0 |
| Consumer Cyclical | **IN** +$1.15M | +$437.4M | agree (sign only) | 0.8 |
| Technology | **OUT** −$387.4M | +$3,750.7M | **disagree → watch_only** | 1.0 |
| Financial Services | **OUT** −$49.9M | +$251.8M | **disagree → watch_only** | 1.0 |
| Industrials | **OUT** −$31.4M | +$228.7M | **disagree → watch_only** | 0.8 |

> `sector-flow-persistence` fired **INFLOW on 11 of 11 sectors** (7 at score 1.0). This is the documented gross-turnover defect — the metric is sign-agnostic and cannot express direction. It is used here strictly as a durability filter; all direction comes from the netted `market-regime.sector_rotation`.

**The real rotation this week was intra-Technology, and GICS cannot see it.** IGV (software) rose **+5.93%** while SMH (semis) fell **−1.30%** — a 7.2pp weekly spread inside a single GICS bucket. That is why netted Technology reads negative while software rallies: MSFT/AAPL weight drags XLK's aggregate mildly positive, but the semis/AI-hardware/crypto-adjacent names inside the same bucket bled harder in dollar terms.

- **Software side (bullish Technology leaders):** MSFT +$145.0M, AAPL +$27.0M, NOW +$22.3M, PANW +$6.3M, STX +$5.6M, ESTC +$5.6M.
- **Semis / AI-hardware / crypto-beta side (bearish leaders):** NVDA −$178.4M, SNDK −$171.8M, GLW −$75.1M, MSTR −$26.3M, COIN −$21.8M, AVGO −$21.1M, INTC −$12.6M.

**ETF flow tape (advisory)** — instrument-level, 5-day `cumulative-premium-flow`, 37 of a 40-call budget used:

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| **XLK** | +$7.43M BULLISH | persistent | mid-clustered, creation/redemption churn | $5.19M Sep-27 185P (LEAP hedge, no_side) | **disagree** vs netted Tech | MSFT, AAPL |
| **IGV** | +$5.64M BULLISH | persistent | $174M print above ask; a garbled $131M print discarded | $6.34M Nov-20 103P + $2.58M 97P bought | disagree vs netted Tech | NOW, PANW, ESTC |
| XLV | +$1.45M BULLISH | persistent | unremarkable | modest Sep call sweeps | n/a | MRNA, BNTX |
| KRE | +$1.22M BULLISH | persistent | — | — | disagree vs netted Financials | — |
| XLC | +$0.74M BULLISH | persistent | — | — | **agrees** (small) | META, GOOGL |
| **SMH** | −$3.96M **MIXED** | **not persistent** | — | — | — | NVDA, AVGO |
| XBI | −$7.90M BEARISH | persistent | mixed, tilts bearish | near-term put buying | diverges from XLV | — |
| XOP | −$12.43M BEARISH | persistent | prints consistently below mid | thin | — | — |
| GDX | −$16.51M BEARISH | persistent | mixed | $4.0M Nov-20 90P ask-side | — | AU |

**The most important line in that table is SMH.** Despite falling 1.30% on price and being the semis benchmark, its 5-day options net flow is only **−$3.96M on ~$730M of gross turnover, and the sign is MIXED / non-persistent**. The semis weakness this week is a **price and beta story, not a sustained options-positioning outflow**. IGV, by contrast, is smaller in absolute dollars but **persistent and sign-consistent**. That asymmetry is the single best argument that the software-over-semis split is real rather than a one-week artifact — and simultaneously the best argument against pressing a semis short, since the positioning outflow that would justify one does not exist.

**Swing-book implication:** the actionable idea is an intra-Technology pair — long software (NOW/PANW/STX/ESTC) against short/avoid semis-AI-hardware (NVDA/SNDK/AVGO/MRVL/MSTR/COIN) — but it is **not yet a rotation call**. It needs 3+ more sessions of the same IGV-persistent / SMH-non-persistent split before it clears the bar. Communication Services is the only GICS-level watch note worth carrying.

**Invalidation:** IGV's 5-day trend flipping from BULLISH to MIXED/BEARISH, or SMH flipping to a persistent sign, collapses the split. Weeklies' share pushing past 0.25–0.30 would suspend rotation framing entirely.

---

## 3. Swing Book (1–6 weeks)

**The book is empty. Zero sized positions.**

The gate stack did not kill this board so much as confirm it arrived dead: the highest raw score anywhere was **4 (LOW)**, and the best pre-risk size the quant could justify was **`starter`** — one step off the `skip` floor. Any single gate fire kills a starter. Every sizeable name took three or four.

### 3a — Long swings (regime-aligned)

| Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure | Invalidation |
|---|---|---|---|---|---|---|---|
| **NOW** | LOW | 4 | `null` NA(substrate) | **skip** | Direction-verified OI build: non-0DTE bullish OI share **0.872** (the strongest verification in the population), with real forward legs — Jan-27 115P sold at dte140, Nov-20 160C bought at dte84, Oct-16 150C bought at dte49. Cum-flow +$181.9M/30d at **9.09% of gross**, the highest net-as-%-of-gross on the board, aligned across 5d/30d/90d with no decay. | Would have been a starter-size Oct/Nov call structure. Not taken. | Loss of the $138–139 shelf; IGV persistence flipping; a fourth NEUTRAL/DISTRIBUTION day in `institutional-accumulation`. |
| **MSFT** | LOW | 4 | `null` NA(substrate) | **skip** | Flattest, least event-driven OI build on the board (net_oi positive and stable all 5 sessions). Non-0DTE bullish OI 0.694 / premium-weighted 0.825. Cum-flow **+$809.7M/30d and accelerating** (90d +$565.4M is *smaller* than 30d). Parity screen passed on the headline $92.8M Nov-20 480C — $20.44 time value on $54.29 premium, genuine ask-side buying. | Not taken. | Break of $505; insider MSPR turning further negative; resolution of the ex-div question against the flow read. |

Both names failed on the same pattern: a real derivatives-side signal that the *dark-pool* side would not corroborate. `accumulation-hunter` graded NOW's DP tape "isolated bookends, not a persistent build" (ACCUM 08-24, three NEUTRAL, ACCUM 08-28) and found the **08-27 $43.0M print was sell-side**; it affirmatively **rejected** MSFT's DP tape as closing-cross-contaminated (mega-tier buy-ratio whipsawing 0.11 → 0.90 → 0.82 → 0.81 → 0.18). `playbook batch-scan` independently returned **`has_edge: false` — "No Clear Edge — Stay Flat"** on MSFT.

### 3b — Short / fade swings (defined risk only)

All three shorts route to **`watch_only`** under the 2026-08-01 short-direction rule. Routing, not suppression: each keeps its full score, components, gate verdicts and serialization so the counterfactual keeps resolving.

| Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure | Invalidation |
|---|---|---|---|---|---|---|---|
| **MRVL** | LOW | 4 | `null` NA(substrate) | **watch_only** | The week's **only qualifying DEX sign flip**: net_dex +1,918,988,168 (08-27) → **−497,529,185** (08-28) after 14 consecutive positive sessions; magnitude_ratio **1.01**; `sign_changes_in_window: 1`; `whipsaw_warning: false`; not earnings-dated. `total_gex` flipped negative the same session (9 of prior 10 positive), spread across ~50 strikes. Non-0DTE bearish OI 0.737. | Would require a defined-risk put spread; not taken. | ⚠ DEX trajectory positive ≥3 sessions, or `total_gex` persistently positive. **Institutional DP shelf: none clean — use the Oct-02 275C strike zone as the structural reference.** |
| **GLD** | LOW | 3 | `null` NA(substrate) | **watch_only** | 408P/413P put debit vertical repeated 08-27 **and** 08-28, independently verified in the OI book (413P bought ask-dominant +20,310; 408P sold bid-dominant −32,879). Cum-flow **−$481.7M/30d bearish on all three windows**, with 94% of the 90d accretion inside the last 30d — the staleness failure mode explicitly checked and rebutted. | **The scored structure EXPIRED 2026-08-28.** No surviving exposure. | Reclaim and hold of $413. Note USD weakening (120.57 → 118.06) is a standing headwind to any re-expression. |
| **SNDK** | DROP | −3 | **0.5405** (n=148, `backtest_clean`) | **skip** | Sweep-persistence bearish 5/5 sessions; 2nd-largest netted outflow on the tape (−$171.8M). **But the thesis is refuted by its own OI book** — see below. | Not taken. | n/a — dropped. |

**Three corrections that materially changed this section, all found by cross-checking agents against each other:**

**MRVL's headline evidence was misread by three agents.** The `MRVL 261016P00165000` ticket — cited by sweep-tracker, dealer-positioning-strategist and contrarian-scanner as an aggressive bearish put sweep — is **`side: bid`**: 23,666 contracts at an average $2.19 ($5.32M). The customer **sold** those puts. A put *write* 24% out of the money is a mildly bullish/range-bound stance, the mirror image of how it was read. `multileg-strategist` caught this independently; direct verification confirmed it. MRVL's book is genuinely two-sided — ask-side bearish (230P 0DTE $5.94M, Sep-18 215P $4.15M) alongside ask-side bullish (Jan-28 300C $7.74M, Dec-18 150C $4.66M, Oct-16 250C $3.97M) — and the Sep-18 320P cluster is sub-parity financing. The DEX flip stands on its own merits; it has lost its corroboration. `playbook batch-scan` separately reads MRVL's flow as **BULLISH**.

**SNDK's bearish OI build is a 0DTE artifact.** Its apparent 70.3% bearish OI tilt collapses once same-day expiries are stripped: forward-dated OI is **82.6% bullish premium-weighted**, and the actual forward structure is a **short strangle** (calls sold at 1530/1600, puts sold at 1440/1265 around a $1,484.74 spot) — a range-bound premium sale, not a directional short. The −3 `flow_conflict` was correctly applied on a 30d basis, though it carries two caveats the quant flagged honestly: SNDK's 5d flow (−$190.7M) actually *agrees* with the short, and the +$944.7M that triggered the deduction is only 1.93% of a $48.9B gross — noise-level by the scale standard the *award* side of the rubric applies. Tier-invariant this week, but a real asymmetry in the rubric.

**GLD's scored structure has already expired.** Two of its three points came from a 0–1DTE vertical that settled Friday. Both debate sides conceded it; the bear called it "the strongest point in this debate."

---

## 4. LEAP Book (6–24 months)

**Empty.** `leap-positioning-radar` screened 28 tickers across three funnels and returned **zero candidates** — a clean rejection, not a coverage gap.

The gate that killed everything was Gate 8: `conviction-matrix` DIRECTIONAL_LONG at confidence > 70. **The highest DIRECTIONAL_LONG confidence found anywhere in the tape was 36.3% (ISRG)** — the gate was effectively unsatisfiable this week. The two names with genuinely persistent multi-week DTE≥180 OI building were both structurally disqualified:

- **INTC** — the only ticker with real Dec-2028 (DTE 840–850) OI accumulation stacking daily across 8 sessions. Killed on cum-flow (30d −$264M and 90d −$896M, both MIXED, bullish/bearish premium near dead-even) and on scenario (MIXED, 1.2% confidence). Decisively: its largest LEAP line (`INTC281215C00210000`) was **bid-heavy — i.e. sold — on 3 of the 4 sessions it appeared**, reading as call overwriting against existing long stock rather than fresh conviction.
- **TLT** — second-most-persistent DTE≥180 builder. Killed outright on a **COVERED_CALL** scenario label ("dark pool buying + call selling — yield enhancement, capping upside"), a hard reject.

Also rejected: **OKLO** (HEDGED_LONG scenario), **IREN** (COVERED_CALL), **CORZ** (30d +$14.0M bullish but 90d −$48.2M — the textbook recent-burst-not-accretion signature the mandate disqualifies), **VFC** (DISTRIBUTION scenario; the flagged Jan-2027 $10C is deep-ITM with unresolved parity), **CELH** (DIRECTIONAL_SHORT — wrong direction).

The macro overlay is consistent with the emptiness: LEAP volume share **fell 0.044 → 0.031** across the week while weeklies more than tripled. With three Tier-1 binaries inside twelve trading days, informed positioning is being expressed short-dated. That argues against long-tenor expression right now rather than for it.

---

## 5. Volatility Surface — WoW Term Structure & Skew Evolution

This was the week's strongest analytical lane, and it produced one genuinely clean find plus one real dislocation.

**The SPY kink tracks NFP precisely.** On 08-24, SPY's `base_shape` flipped BACKWARDATION → **KINKED at dte=5 → 2026-09-03**, prominence 5.4%. By 08-28 the base shape had normalized to CONTANGO while the kink moved to **dte=6 → 2026-09-04** — the exact nonfarm-payrolls date — with prominence **growing to 8.3%**. A kink that migrates with the calendar and *strengthens* as the event approaches is the signature of genuine event-vol pricing, not a substrate artifact. QQQ's earlier backwardation cleared to clean CONTANGO with no kink, so this is specific to SPY/NFP rather than general index panic.

**Hygiene changed the answer, as it was supposed to.** Raw `base_shape` returned BACKWARDATION on 13 of 14 names (08-24) and 12 of 14 (08-28) — the near-universal mechanical pre-event backwardation that makes the bare label useless. Seven of fourteen names flipped raw → kink-aware `shape` after cleanup. A separate FOMC-week kink concentrated cleanly at **2026-09-18** across IREN, ASTS, OKLO, APLD, BE, MSTR and COIN (prominence 5.9–14.1%) — and `expiry-heatmap` confirms 2026-09-18 is the **#2 premium-concentration expiry market-wide at $3.77B**, second only to the 0DTE bucket. That is a real, broad institutional lean into the FOMC monthly.

**`front-end-iv-ratio` firing rate collapsed across the week — and that is informative.** Re-read at `--near-dte 7` (never the CLI default of 1, which fires on nearly everything): **11 of 14 names fired >1.05 on 08-24 (78.6%)** versus **4–5 of 14 on 08-28 (28.6–35.7%)**. Front-end panic *fell* even as the high-beta complex cratered on Friday. Risk-monitor's independent read at the same tenor found only **2 of 10 names above 1.10** — a properly discriminating population rate, with SPY at 0.853 and QQQ at 0.858 in deep contango.

**The core finding: a genuine long-vol dislocation, not a broken IV-rank denominator.** Confirmed three independent ways — absolute IV below trailing realized (not merely low against a noisy percentile), a real and broadening event kink, and skew that stayed **COMPLACENT** (call IV > put IV) straight through the drawdown on every high-beta name, both dates. The market never rotated to put-side hedging while these names fell 6–15%.

| Ticker | IV30 | RV20 | Gap | Read |
|---|---|---|---|---|
| MRVL | 57.6% | 87.9% | **−30.3pp** | cheapest in population |
| OKLO | 72.1% | 93.4% | **−21.3pp** | cheap |
| IONQ | 71.2% | 87.5% | −16.3pp | cheap |
| ASTS | 63.7% | 78.6% | −14.9pp | cheap |
| IREN | 77.6% | 90.5% | −12.9pp | cheap |
| MSTR | 67.3% | 79.6% | −12.3pp | cheap |
| COIN | 60.1% | 69.0% | −9.0pp | cheap |
| APLD | 69.7% | 73.9% | −4.2pp | roughly fair |
| RKLB / AFRM | 64.5% / 49.6% | 63.2% / 48.5% | ≈ +1pp | fair |
| **BE** | 78.7% | 72.2% | **+6.5pp** | **RICH — the lone opposite sign** |

**Caveats carried:** every `iv-percentile-zscore` read is **PROVISIONAL** — the tool short-delivered `dates_used: 97` against a requested 252-day lookback on all 14 names, so the IV-vs-RV absolute comparison above is the load-bearing evidence, not the percentile. **APLD and QS** sit in the same cheap-vol bucket but their kink tenors carry only 12 and 11 contracts, below the 15-contract floor — watch-only, do not size off those tenors. And risk-monitor's per-name panic read surfaced a real tension with the MSTR thesis: its **5-day front is backwardated at 1.112**, so the near tenor is already bid and the cheap-vol claim survives at the 30d tenor but not at the front where a three-catalyst gamma trade would actually be expressed.

Calendar-spread candidates: **AFRM and MRVL** show persistent backwardation with falling front-end ratios (1.355 → 1.196 and 1.268 → 1.126), the structural precondition — but MRVL's −30.3pp IV-RV gap means there is nothing rich to sell at the front, which argues against a classic short-front calendar. Both watch-only.

---

## 6. Earnings — Recap & 2-Week Lookahead

### (a) Recap — the week's prints

| Ticker | Report | Pre-event fleet thesis | Reaction | Grade |
|---|---|---|---|---|
| NVDA | 08-26 amc | `skip` — the 230C/240C bull spread was killed same-day on inverted per-leg data | +8.7% (08-27), then **−4.6%** Friday — a round trip to 217.55 | **CONFIRMING** — correctly killed; a held spread would have round-tripped through both strikes |
| MRVL | 08-27 amc | BUY VOL / CONFIRM, ~9.1% implied — scored 0, routed `skip` | **−10.3%** (08-28) | **CONFIRMING the vol read, not a booked trade** — realised slightly exceeded the priced move |
| **CRM** | 08-26 amc | CALENDAR | **+22.6%** | **DISCONFIRMING** — a calendar wants a pin; +22.6% blows through both legs |
| **CRWD** | 08-26 amc | CALENDAR | **+20.5%** | **DISCONFIRMING** — same failure |
| **OKTA** | 08-26 amc | `skip`; 08-25 scan quoted 15.9% implied, skew COMPLACENT | **+28.6%** | **DISCONFIRMING the COMPLACENT-skew read** — realised ~1.8× the priced move |
| **SNPS** | 08-26 amc | CALENDAR | **+13.4%** | Marginal DISCONFIRM |
| WDAY | 08-27 amc | SELL VOL half-size | +5.8% | **CONFIRMING** — contained |
| BBY | 08-27 bmo | SELL VOL half-size, 11.1% implied | −4.4% | **CONFIRMING** |
| KSS | 08-26 bmo | 18.6% implied, TAIL_HEDGING | EPS **missed** badly (0.31 vs 0.58) but stock **+1.5%** | **CONFIRMING** — even a real miss stayed inside a rich priced range |
| BBWI | 08-26 bmo | 15.8% implied | +7.5% | **CONFIRMING** |
| BURL | 08-27 bmo | 11.1% implied | −7.6%, then −5.9% Friday | **Mixed** — the second leg looks like broad liquidation bleed, not a second surprise |

**The headline finding is a structure-selection failure, not a direction failure.** The enterprise-software cohort ran hot enough to break the CALENDAR structure the fleet defaulted to — CRM, CRWD, OKTA and SNPS all beat wide and moved 13–29%. The fleet's own regime read (negative VRP ⇒ favor long gamma) was **directionally correct but was not applied to the CALENDAR bucket**. That is the single most actionable lesson of the week, and it is why the lookahead below skews BUY VOL and contains zero calendars.

**ESTC was a ranking miss, not a data miss.** ESTC reported 08-27 amc, beat EPS 0.70 vs 0.596 (+17.5%) on in-line revenue, and closed **+19.3%**. It sat in the `earnings-catalyst` cache all week with a *valid* implied move (13.9% → 14.7%, days-to-earnings ≤3 throughout, so not subject to the pre-event-tenor defect) — but **no daily report surfaced it**, because its IV rank of 52–59 was crowded out of the top-N by higher-IV-rank names. A real, underpriced move — **14.7% priced against 19.3% realised** — went unscored because the scan sorts by IV rank rather than by richness or edge.

**Correction carried from Phase 1:** NOW's +12.6% week was **not** an earnings reaction — NOW has no print this week. It was a sympathy rally on the CRM/CRWD/WDAY beat wave. That correction propagated into the NOW thesis in §3a and into the fundamentals gate.

### (b) Lookahead — 2026-08-31 → 2026-09-11

Sixteen candidates, minus DSGX (fails C12 at $35.2M ADV), run through `term_structure_hygiene.py --near-dte 7`. **Eight of fifteen flipped shape after cleanup.**

| Ticker | Report | True event tenor | `--near-dte 7` valid? | Back-month skew | Confirmation leg | Re-derived move | Verdict |
|---|---|---|---|---|---|---|---|
| **MDB** | 09-01 amc | dte6 (09-04), IV 148.2% | Yes | flat 1.03 | **Strong** — $3.17M/$1.79M/$1.15M OTM calls at 490/505/530 vs spot 446.62 | **19.0%** | **BUY VOL** |
| **SNOW** | 09-02 amc | dte6 (09-04), IV 111.8% | Yes | flat 1.02 | **Strong** — $1.77M/$1.35M/$1.13M OTM calls 340/352.5/355 vs 328 | **14.3%** | **BUY VOL** |
| **PATH** | 09-03 amc | dte6 (09-04), IV 132.7% | Yes | flat 0.98 | Moderate-strong — balanced straddle-like build | **17.0%** | **BUY VOL** |
| **ZS** | 09-03 amc | dte6 (09-04), IV 123.3% | Yes | flat 0.96 | Moderate — call-dominant | **15.8%** | **BUY VOL** |
| **DOCU** | 09-03 amc | dte6 (09-04), IV 101.6% | Yes | flat 1.02 | Moderate — $302.6k @ $70C vs spot 64 | **13.0%** | **BUY VOL** (smaller — historically muted) |
| MDT | 09-01 amo | dte6, IV 47.8% | Yes | flat 0.98 | Weak | 6.1% | SKIP — move too small to size |
| ADBE | 09-10 amc | dte13 = **CPI day** | **No** | flat 0.98 | Moderate but macro-contaminated | ~11.7% (not attributable) | **SKIP** |
| KR | 09-11 amo | dte13 = **CPI day** | **No** | ~zero | Thin ($19k/$12k) | ~8.0% | **SKIP** |
| CHWY | 09-09 amo | dte13 = **CPI day** | **No** | 1.04 | Weak, put-tilted | ~14.0% | **SKIP** |
| PANW | 09-01 amc | non-monotonic curve | partial | flat 0.98 | **None** — 4 outlier rows, all sub-$1.2k | not quotable | **SKIP** |
| NTAP · SAIC · OLLI · CASY | various | **`NO_NEAR_TENOR`** | — | — | — | **null** | **SKIP** |
| SIG | 09-11 | event tenor dropped (8 contracts < 15 floor) | — | — | — | null | **SKIP** |
| DSGX | 09-10 | — | — | — | — | — | **SKIP (C12 fail)** |

**Zero SELL VOL calls.** Back-month skew at the 09-18 tenor read COMPLACENT or NORMAL on **all 10 measurable names** (skew_ratio 0.96–1.04) with **no TAIL_HEDGING anywhere** — which disqualifies full-size premium selling across the board and is exactly regime-consistent with negative index VRP.

**Three substrate defects were handled rather than absorbed.** (1) Raw `implied_move_perc` was **not quoted for any name** — it is computed off a pre-event tenor and printed absurd values this week (ADBE 0.38%, PANW 0.34%, SNOW 0.34%, MDB 0.60%); every move above is re-derived as ATM_IV(true event tenor) × √(DTE/365). (2) The `--near-dte 7` snap silently lands on a weekly expiring *before* the report for any name >4 days out — four names are marked INVALID on exactly that basis. (3) The auto-kink-finder mislocated the event on **MDB, SNOW, PATH, KR, PANW, CHWY and SIG**, placing the "kink" at a monthly tenor sitting between PPI/CPI/FOMC rather than at the name's own earnings; each was re-read directly at the true tenor. `analyst-vs-flow` returned **no analyst leg on any of the 10 names**, confirming the known 0/21 defect — it was not used as a confirmation leg.

**Stacked macro risk, stated plainly:** all five BUY VOL names price off the **2026-09-04 weekly expiry, which is also NFP day**. That is a tailwind for long gamma (more binary risk, more optionality value) but it means the realised move on those names will not be a clean read of earnings-only vol.

---

## 7. Risk & Correlation

**Correlation refuted two of three expected clusters.** `portfolio-correlation` over the eight-name candidate set, 30-day primary window (`sector_breakdown` returned `{"Unknown": 8}` with the spurious 100%-concentration warning — the known defect, disregarded; the pairwise matrix is the input):

| Pair | 30d | 60d | Classification | Action |
|---|---|---|---|---|
| **MSTR / COIN** | **0.834** | 0.791 | **CLUSTER** (≥0.70) | −1 tier to COIN; MSTR kept on cum-flow tiebreak |
| MRVL / SNDK | 0.673 | 0.732 | SOFT WATCH (0.60–0.70) | **No penalty** |
| GLD / MSTR | 0.610 | 0.554 | SOFT WATCH | **No penalty** |
| **NOW / MSFT** | **< 0.50** | — | **no cluster** | **No penalty** |
| NOW / SNDK | −0.506 | — | negative | not surfaced |

**There is no software cluster.** NOW/MSFT did not surface at all — a dedicated two-name call returned `high_correlations: null`, i.e. below 0.50. The 7.2pp IGV-vs-SMH rotation **dispersed** the software megacaps rather than fusing them (NOW's +12.63% sympathy beta against MSFT's +6.27% on genuine cum-flow). Had the cluster been assumed rather than measured, one of the two would have been wrongly docked a tier. The semis pair reaches 0.732 at 60d but sits at 0.673 on the primary 30d window and was **not** upgraded — window-shopping is precisely what the 2026-05-15 P1.4 fix removed. PLTR is uncorrelated with everything on the board (no pair ≥0.50); its risk is idiosyncratic.

**Macro & event risk.** Stagflationary tilt — payrolls −23k against core PCE 3.34%, 10Y 4.67% rising, USD weakening, curve +0.39. Three Tier-1 prints inside twelve trading days (NFP T+5, CPI T+9, FOMC T+11/12). Because every remaining candidate was an undefined-risk directional swing, the event gate fired **−1 tier** on NOW, MSFT, MRVL and GLD. **MSTR and COIN were exempted** — both are long-gamma structures kinked to the 09-18 FOMC monthly, and docking a trade for the events it exists to harvest would be backwards.

**Fundamentals verdicts.** NOW **CONFIRM** (0) — but with no idiosyncratic catalyst; the +12.63% was sympathy beta, RSI 72.72. MSFT **CAUTION** (−1) — insider MSPR −83.89 3mo with **July and August both pinned at the −100 floor**, a same-day "Rerating Is Probably Over For Now" downgrade, and an unresolved ex-dividend date possibly inside the 30d cum-flow window. MRVL **CAUTION** (−1) — and notably the fundamentals cut *against the short*: rev +34.07% YoY, op margin 36.61%, Craig-Hallum raising PT to $300 and B. Riley maintaining Buy at $315 against a $216.62 close, plus a Google AI chip deal framed at $120B long-term revenue. GLD **NA** (0, no penalty) with a split macro read. MSTR **CONFIRM** (0) — balance-sheet fragility corroborates the long-gamma thesis.

**Debate-disconfirmation cuts — the gate fired on all five names.** NOW 0.65 ≥ 0.45; MSFT 0.65 ≥ 0.35; MRVL 0.35 = 0.35; GLD 0.35 = 0.35; MSTR 0.75 ≥ 0.45. **Not one bull residual on the board cleared a coin flip**, and four of five sat below 0.55. Two pairs were BOTH_SIDES_LOW (MRVL, GLD) — recorded, not mechanized; n=3 observed lifetime, far short of the pre-registration bar. The concessions did real work: NOW's bull conceded the sell-side DP print, MSFT's bull conceded the insider floor outright, **MRVL's bear abandoned the causal story behind its own DEX flip**, and GLD's bear conceded its structure had expired.

**Breadth cross-check (advisory).** `fz` 229 advancers / 273 decliners, **45.53% green**, `divergence_flag: true` against the UPTREND label. Different lineage, same conclusion as the `uw` 30.5% bullish-flow read and the SPY-vs-RSP spread. No size impact.

**Adverse-flow exits.** **IWM → EXIT CANDIDATE.** W34 carried it long on `vanna_squeeze_flag: true`; it now prints `flow_direction: bearish`, `net_flow −$7,285,407`, put/call **2.54**, and −1.40% on the week against SPY +0.47%. The `OI_SHIFT` (+238,826) and `LARGE_DARK_POOL` ($49.6M) alerts read as engagement but at P/C 2.54 the OI build is put-heavy — it confirms the reversal. The charm headwind (−1,477,356) and persistent negative gamma won; the coiled spring resolved down. IWM also failed to re-qualify this week (single-agent, `passes_gate: false`) — a double exit signal.

**Hedge sleeve: none. Do not buy protection.** The book has zero sized positions and therefore zero net delta; a hedge against a flat book is a certain premium expense with nothing to offset. The directional skew trigger (≥0.6) is not remotely approached even across the paper board (2 long / 3 short / 2 vol_long / 1 contested). Concentration: N/A — no positions. If the desk wants standing tail protection for reasons outside this book, the setup is genuinely favourable — VIX 14.43, negative VRP on both indices, SPY/QQQ front-end in deep contango (0.853/0.858) — but that is a portfolio-level decision against exposure this note has not been shown.

---

## 8. High-Conviction Cross-Ref (HIGH and MEDIUM tier)

**Empty. No name reached MEDIUM or HIGH.** The board's maximum was raw 4 against a MEDIUM cut of 7 and a HIGH cut of 9.

The Step 3a load-bearing-tool gate was therefore a **no-op this week** — recorded explicitly rather than skipped silently, since no candidate reached the ≥9 threshold where the 3-of-4 citation requirement binds.

**Expectancy lens (advisory — C31):** not computable this cycle. With no sized positions this week and no closed conviction calls in the rolling `conviction_week_*` groups, there is no tier×expectancy series to display. The relevant standing observation from prior audits — that the DROP pile has out-realised the traded book in every audit that has measured it (0.477 vs 0.406 on 2026-07-11; 43.3% vs 38.6% on 2026-07-18) — remains the honest frame for a week that produced only DROP and `watch_only`.

**A structural finding worth registering.** The quant established that a `vol_term_dislocation` call can earn **at most 1 point** under the frozen weekly rubric: ten of the eleven lines are either explicitly directional (+3 oi-trend requires a direction-verified build; +3 accumulation is a long-side conjunction; +1 cum-flow requires accretion *in the trade direction*; +1 DEX requires a flip *in trade direction*; the sector-leader gate requires cum-flow direction alignment; both flow_conflict deductions are switched off for non-directional classes) or structurally unavailable (conviction-matrix is LEAP-only; position-rolls returned zero market-wide; earnings and OPEX lines don't apply). **A structurally sound long-gamma setup cannot clear the DROP floor by construction.** MSTR and COIN are not weak calls that scored badly — they are calls the frozen rubric has no surface to score. That is a coverage gap, and this is exactly the week to notice it, because the vol lane was the strongest analytical output on the board. It is flagged for a future `/calibration-audit`, **not acted on** — inventing a vol lane inside a frozen rubric is the unregistered change the freeze exists to prevent.

**Embedded rubric (for audit):**

```
Weekly conviction score = Σ:
  +3  uw historical oi-trend BUILDING for the full week, --days >= 5   [C47: saturation check mandatory]
  +3  3+ aligned signals in accumulation-hunter sustained across week, dark-pool block-stratified
      institutional-tier confirmed — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms
      (sign aligned AND |cum_flow_30d| >= $50M); else halved (floored) +3 -> +1
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70, stable WoW
      — CONDITIONAL: award only when dominant_signal_class == leap_directional; else 0
  +2  uw oi position-rolls shows institutional roll forward into longer-dated LEAP
  +1  uw historical cumulative-premium-flow net directional accretion across the week
      — INTENT-SCREENED: (a) no C28 distribution_flag, AND (b) not deep-ITM sub-parity calls in an ex-div window
  +1  dealer-positioning-strategist MECHANIZED DEX flip or vanna squeeze in trade direction
      — VERIFIED SIGN CHANGE only, via scripts/dex_flip.py; whipsaw_warning mandatory to report
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector
      — CONDITIONAL: (a) persistence_score >= 0.6 AND (b) cum_flow_30d aligned AND (c) |cum_flow_30d| >= $50M
  +1  earnings-scout BUY VOL or SELL VOL for next 2 weeks (term-skew aligned for full size)
  +2  multileg-strategist directional structure repeated on >=2 days (term-structure-anchored play type)
  +1  vol-surface-scout KINKED or BACKWARDATION worsening WoW; iv-percentile-zscore extreme; VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner crowded long with rising pc-ratio-zscore trajectory (VRP positive)
  -3  flow_conflict — cum_premium_flow 30d direction clearly opposite dominant_signal_class
  -1  flow_conflict_lite — 30d cum_premium_flow read is MIXED
      [-3 and -1 mutually exclusive — apply ONE, never both]
  # Tier gates applied by risk-monitor in Step 2d, contributing 0 to raw_score:
  -2  [TIER GATE] correlation cluster (pairwise corr >= 0.70) — -1 TIER
  -3  [TIER GATE] WoW regime flip conflicts with trade direction — -1 TIER

Tiers: >=9 HIGH (full) · 7-8 MEDIUM (half) · 3-6 LOW (starter/watch) · <=2 DROP
rubric_version: 2026-06-12 (FROZEN)
```

---

## 9. Setups for Next Week

**Next-session GEX advisory (SPY/QQQ only) — prose-only, 0 rubric points, and framed by its own track record.**

> **Backtest verdict first: `NO_GO_NO_EDGE`.** Over a pooled n=118, the next close landed closer to the nearest EOD wall only **17.8% of the time against a 50% baseline** (p=1.0) — walls are **anti-magnets**, not magnets. H1 also ran backwards pooled (long-gamma mean abs return 0.838 vs short-gamma 0.822). Everything below is dealer context with **no predictive claim**.

- **SPY** — spot 769.30. `total_gex` **negative (−$139.8M)**; the FULLY_NEGATIVE label and the sign agree on this read. `zero_gamma_level` null ⇒ **`zgl_reliable: false`**. Call wall **772** (+0.35%), put wall **765** (−0.56%) — a tight ~1-point box, but the negative total argues against reading it as a stable pin. Structure bias: a break of either wall is what dealers would chase, not fade.
- **QQQ** — spot 716.31. `total_gex` **negative (−$90.1M)**, label and sign agree. `zgl_reliable: false`. Call wall **730** (+1.91%), put wall **716** — **essentially at spot**. The heaviest dealer short-gamma concentration sitting directly under Friday's close with no resistance until +1.9% is the most notable feature in either book. Not a premium-selling setup.

> **Substrate defect re-confirmed, and it is severe.** The GEX `regime` label contradicted its own `total_gex` sign on **4 of 7 sessions for both SPY and QQQ** this week. Every regime read in this note uses the raw `total_gex` sign, never the label. A new observation for the defect log: **SPY, QQQ and SMH all show an identical single-session `total_gex` sign flip on 2026-08-27 that reverts the next day** — three unrelated names flipping on one date and reverting looks like a settlement/data artifact rather than three independent regime shifts.

**Next-session 0DTE premium-selling setup (advisory, 0 rubric points, delta-neutral).** Rolling backtest verdict `GO_PREMIUM_SELL_INTRADAY`, but **the `sell_premium: true` flag is unconditional and must not be read as a green light.** Current `vol_state` is **LOW** (VIX 14.43), and the edge lives in the MID/HIGH terciles (bounds 15.8 / 17.3).

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true (unconditional) | true (unconditional) |
| `vol_state` | LOW | LOW |
| implied move | 0.39% | 0.59% |
| expected range | ±1.1% | ±1.91% |
| `size_scalar` | 0.5 | 0.5 |
| mean PnL open, **gross** | 0.222% | 0.345% |
| mean PnL open, **net** (after 0.1% round-trip) | **0.122%** | **0.245%** |
| **at LOW vol state, gross → net** | 0.15% → **+0.05%** | 0.22% → **+0.12%** |
| worst day | −1.4% | −2.453% |

**Read the LOW-vol row, not the headline.** Net of cost at the current vol state this is **+0.05%/day on SPY and +0.12%/day on QQQ** — thin, positive, and nothing like the headline. `pnl_basis` is **% of underlying spot notional, gross** — not premium-collected, not margin-relative. Entry at/after the open once the overnight gap resolves; stand aside if it gaps beyond the wings; **never carry overnight**. The validation sample contains **no vol shock — the short-vol left tail is unsampled**, and win-rate is explicitly not the promotion metric for a negatively-skewed payoff.

**Swing setups from dealer positioning.** MRVL is the only qualifying DEX flip (`dex_flip_short`) and routes to `watch_only`. **IWM's vanna squeeze is live but fragile** — `vanna_squeeze_flag: true` on net_vanna +101,358 with VIX falling four consecutive dated sessions (15.85 → 15.45 → 15.21 → 14.51 → 14.43) — but charm is a −1,477,356 headwind and IWM sits in persistent negative gamma, so it is a coiled spring in *both* directions. It failed the confluence gate on a single agent and is simultaneously this week's adverse-flow exit candidate. **Not a setup — a contradiction to watch resolve.**

**Pin vs trend:** neither. Not OPEX week (next monthly third-Friday is 2026-09-18, T+14), both indices short-gamma, and the walls are backtested anti-magnets. Trade the events, not the structure.

**Highest-conviction actionable setups for the coming week:** **none from the conviction book** — it is empty. The three genuinely interesting non-scored ideas, in order:

1. **The BUY VOL earnings lane (§6b)** — MDB (19.0% re-derived move), SNOW (14.3%), PATH (17.0%), ZS (15.8%), DOCU (13.0%). All five confirmed by real OTM call flow at the true event tenor, all consistent with the negative-VRP long-gamma tilt, all validated in direction by this week's realised software moves. Caveat: all five price off the 09-04 NFP expiry.
2. **The long-vol dislocation (§5)** — IV 9–30pp below realized on OKLO, MRVL, IONQ, ASTS, IREN, MSTR, COIN with skew still COMPLACENT. Unscoreable under the frozen rubric, which is itself the finding.
3. **A multi-day VIX convexity build** — `multileg-strategist` found the Sep-16 20C printing on three separate sessions with the ratio *rising* each day (0.827 → 0.94 → 0.956), surrounded by a 21/22/25/28/35/40/45C ladder and near-ATM 16P/17P protection added Thursday, against a genuine contango curve. Someone is accumulating tail convexity into the September event stack. Single-agent, watch-only, but it is the most coherent institutional story of the week.

**LOW-tier names to track for daily confirmation:** NOW, MSFT (long); MRVL, GLD (short, `watch_only`).

**Deep-dive hand-off:** skipped — no HIGH-tier names post-gate. Correct output for a no-edge week.

---

## 10. Watch-only — single signal, no confluence

Surfaced by one agent only; listed for journaling, **not** for entry.

- **IWM** — `vanna_squeeze` (dealer-positioning only). Simultaneously this week's adverse-flow **exit** candidate from the W34 group. Failed the gate and reversed.
- **VIX** — multileg convexity ladder, `repeat_count=3` on the Sep-16 20C with rising ratios, plus a 21–45C tail ladder against contango. The most coherent single-agent story of the week.
- **NVDA** — multileg Jan-27 180P / Jun-27 140P put diagonal, ~$22M net debit on 100–120k contracts, both legs OTM with clean time value. But **dealer-positioning explicitly withheld a call**: DEX stayed positive with **0 sign changes** through a −4.6% Friday, so the drop was beta-driven, not dealer-driven. Sweep direction MIXED.
- **SPX** — a Dec-18 7000C/8000P combo built Thursday (~$187.6M net debit), fully closed Friday for a large credit, then re-opened in Oct-16 at ~43% of size. Desk-level de-risking timed to Friday's liquidation. Note the short-put leg is uncapped to the downside.
- **HYG** — put-buying campaign across three sessions (Nov-20 75P/79P, Oct-16 77P, Sep-18 77P/79P/80P). Credit-spread-widening hedge consistent with the macro read.
- **PBR** — Nov-20 C21/C24 repeated identically on 08-25 and 08-27, genuine KINK at Sep-18, all OTM with full time value.
- **EWZ** — Nov-20 C40–46 ladder, large Tuesday add then **nothing Wed–Fri**. The fade is the signal; treat as a decaying thesis.
- **TLT** — rate-hedge theme present, but `leap-radar` rejected it outright on a COVERED_CALL scenario.
- **MU** (sweep bearish 5/5), **AMD** (bearish 4/5) — single-agent persistence, no co-flag.
- **MRNA** — accumulation marginal; two isolated ACCUM days bookending three NEUTRAL, and the spike-then-fade path (138.89 → 158.83 → 137.99) reads catalyst-driven, not quiet accumulation.
- **AVGO** — sweep bullish tag **demoted to hedge-flow** (cum_flow_30d MIXED); dealer DEX negative but magnitude fading −2.4B → −0.15B. Watch for a flip next week.
- **PLTR** — genuinely contested direction (accumulation-hunter long vs sweep-tracker bearish 4/5), `oi smart-positioning` bullish share ~48% (a coin flip), ceiling-saturated `oi-trend`, and a live C28 `distribution_flag`: two 203-DTE LEAP calls closed for **$33.2M combined on the same session** as its third straight accumulation day. Scored 0 either direction — the DROP is robust to which side you pick.

**Single-leg whale advisory (permanently 0 points; C19 closed as REFUTED 2026-07-25):** the tier scan returned 20–25 signals per session but **zero Tier-1 opening/floor PUT signals across all five covered dates**. Nothing to report, and nothing accrues.
