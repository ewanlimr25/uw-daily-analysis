# Daily Market Analysis — 2026-08-18

## Executive Summary

- **Regime + GEX state:** `TRANSITIONAL — mixed signals, reduce position size` on an intact `UPTREND` structure (SPY 767.45, above 20SMA 758.68 and 50SMA 749.84, −1.53% off the 90d high). Breadth is the tell: **31.5% bullish flow** (1,990 of 6,316 tickers) and **44.6% green** on the independent `fz` tape. Today was a **semis/AI-led risk-off, not broad selling** — SOXX −4.96%, SMH −4.09%, SOXL −14.8%, EWY −8.13%, XLK −2.47%, while XLE +1.76%, XLV +1.60%, XLP +1.06%, XLF +0.45% — and **RSP (−0.45%) beat SPY (−0.68%)**, confirming concentrated rather than broad damage. Both indices enter tomorrow **short-gamma**: SPY `FULLY_NEGATIVE` (total_gex −$1.22B, second straight session, deepening), QQQ negative with the put wall **0.08% below spot**. VIX 15.84 (+4.28%, rising two sessions). Sector lean: netted flow **OUT of Technology (−$410.0M)**, Comm Svcs (−$141.6M), Consumer Cyclical (−$53.4M); **INTO Energy** and Consumer Defensive.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** **SPY** — short-gamma (`FULLY_NEGATIVE`), ZGL null/unreliable, call wall 780 (+1.60%), put wall 765 (−0.35%) · bias: debit verticals, **no pin or premium-selling structures**. **QQQ** — short-gamma (label/total_gex contradiction, graded by total_gex sign), ZGL 261.7 is a garbage extrapolation, call wall 735 (+2.43%), put wall 717 (−0.08%) · bias: directional 0DTE only, essentially **no downside cushion**. Advisory, 0 rubric points — see §2.
- **Top swing build:** **None.** No name reached MEDIUM or HIGH. The entire book sizes to `skip`.
- **Top LEAP candidate:** **None.** The LEAP board is empty — only 2 C12-passing names appeared in `oi biggest-increases --min-dte 180`, and both were disqualified (CRWV on a `COVERED_CALL` conviction-matrix read at confidence 20.5 and a 3.0% net/gross accretion ratio; IWM on −$1.337B 90d flow and a deep-OTM index-put hedge signature).
- **Biggest risk:** the **`AI_semis_complex` correlation cluster** — NBIS/CRWV 0.904, AMAT/SMH 0.902, LITE/SMH 0.859, SNDK/SMH 0.851, LITE/CRWV 0.801 (10 pairs ≥0.70, 6 members: **LITE, NBIS, AMAT, CRWV, SNDK, SMH**). Treat as **one position**. Hedge sleeve: **QQQ put vertical expiring ~08-28** — that single expiry spans FOMC Minutes (T+1), OPEX (T+3), PCE (T+6) and Warsh's keynote (T+8), and negative QQQ VRP means the long leg is bought **below** realized. Hedge **SMH/SOXX rather than SPY** for any semis book — an index hedge structurally under-hedges concentrated damage.

> **No edge today. Nothing is sized.** This is the 23rd consecutive empty board and it is the designed output, not a failure — the DROP pile has out-realised the traded book in six consecutive audits.

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** TRANSITIONAL — *"Half position sizes. Favor defined-risk strategies. Iron condors in range."* Trend UPTREND. SPY 767.45, +3.42% over 30d, above both SMAs.

**Breadth narrative.** The regime label and the breadth data disagree in tone, not in fact. `uw` flow breadth is **31.5% bullish**; the independent `fz` advance-decline tape reads **224 advancers / 275 decliners / 3 unchanged of 502, pct_green 44.62%**, avg change −0.45%, median −0.19% (top TRGP +7.14%, worst COHR −12.75%). The index is red **and** pct_green < 50 — those are *consistent*, so **no divergence flag** fires. This is not the hidden-distribution case; it is an ordinary down day whose damage is unevenly distributed.

| Index | Spot | Zero-gamma | Reliable | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|---|
| SPY | 767.70 | `null` | ✗ | **−$1,223.7M** | `FULLY_NEGATIVE` | 780 (+1.60%) | **765 (−0.35%)** |
| QQQ | 717.58 | 261.70 ⚠ | ✗ | **−$523.8M** | `NEGATIVE` (via total_gex sign) | 735 (+2.43%) | **717 (−0.08%)** |
| IWM | 300.23 | 170.92 ⚠ | ✗ | **−$575.3M** | label `POSITIVE`, total_gex **negative** | 305 (+1.59%) | n/a (no clean wall below spot) |

⚠ **Three of three ZGLs are unusable today** — SPY returns `null` (FULLY_NEGATIVE), QQQ returns 261.70 (~64% below spot) and IWM returns 170.92 (~43% below spot). Both are deep-OTM extrapolation artifacts. QQQ and IWM additionally show the **raw `regime` label contradicting the `total_gex` sign**; both are graded here by the total_gex-sign fallback and flagged `zgl_reliable=false`. This is §2's stated fallback rule doing its job, not a judgment call.

**`uw options-flow dte-volume-share`:** 0DTE **25.6%** · weeklies **34.3%** · monthlies **24.2%** · LEAPs **4.5%** → `BALANCED`. Neither a clean institutional-positioning tape (which would argue for giving multi-week calls the benefit of the doubt) nor a retail-dominated one. Market-level only — the tool returns `{symbol: MARKET}` and has no per-sector split.

**`uw historical vrp`:** SPY **FAIR, +0.0079** (IV30 13.30% vs realised 12.51%) — essentially zero premium cushion. QQQ **FAIR label but NEGATIVE value, −0.0292** (IV30 **19.87%** vs realised **22.79%**) — **Nasdaq IV is below realized**, i.e. a premium-**buying** environment. This single fact does more work in today's report than any other: it is the reason three of the five debated structures are on the wrong side of the vol regime.

**Macro backdrop** (`scripts/fred_macro.py`): yield curve **normal** (10Y−2Y +0.52) · core CPI **2.79%** YoY · **core PCE 3.29% YoY (hot, well above target)** · unemployment 4.1% · **payrolls −23k MoM (contracting)** · 10Y **4.72%, rising** (+0.17 in 30d) · USD **weakening** (−1.41 in 30d) · fed funds 3.63%. **Stagflationary tint** — inflation above target while employment contracts and the long end rises.

**Forward event risk — T+0 = 2026-08-18, counted in trading days.**

| Event | Date | Offset | Impact |
|---|---|---|---|
| **FOMC Minutes** (Jul 28–29 mtg), 2:00pm ET | 2026-08-19 | **T+1** | HIGH |
| Initial jobless claims | 2026-08-20 | T+2 | MEDIUM |
| **Monthly OPEX expiry** | 2026-08-21 | **T+3** | HIGH (mechanical) |
| INTU earnings | 2026-08-25 | T+5 | — |
| **PCE / Personal Income & Outlays (July)**, 8:30am · NVDA earnings | 2026-08-26 | **T+6** | HIGH |
| ULTA earnings · **Jackson Hole opens** · Q2 GDP 2nd est | 2026-08-27 | **T+7** | HIGH |
| **Jackson Hole keynote — Kevin Warsh's FIRST speech as Fed Chair** | 2026-08-28 | **T+8** | HIGH |
| NFP (August employment situation) | 2026-09-04 | T+13 | HIGH |
| CPI (August) | 2026-09-11 | T+18 | HIGH |

**There is no clean window in this book.** Every structure that reached Phase 2 spans at least two named, dated Tier-1 binaries. A brand-new Fed Chair's first framework speech is the specific problem: it has **no historical reaction function to price against**, so no implied move can be correctly calibrated to it.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — built from open interest that persists overnight — read forward as the *prior* for the next session's open. It is **prose-only, contributes 0 points** to the conviction rubric, and makes **no backtested predictive claim**. Predictive validation of these levels lives in `/weekly-analysis`'s rolling §2 backtest. Scope is **SPY and QQQ only**.

**SPY — short-gamma, second session, deepening.** Spot 767.70, `total_gex` **−$1,223.7M** (08-17: −$368M → 08-18: −$1.22B). ZGL is `null` — the FULLY_NEGATIVE case — so the read falls back to the total_gex sign plus spot-vs-wall geometry, and `zgl_reliable=false`. **The put wall at 765 sits only 0.35% below spot** and carries −$317.2M net GEX; the call wall is 780 (+1.60%, +$105.1M). Dealers are short gamma essentially *at* spot, so they sell into weakness and buy into strength — **amplifying** the tape rather than dampening it. Because this regime held and deepened across two sessions rather than flipping once, it is the more reliable of the two index reads.
**Structure bias:** debit verticals / directional 0DTE only. Put debit spread pressing toward 765 on continuation; call debit spread toward 780 on a reflex bounce. **Avoid iron flies and short straddles entirely** — the book is set up to amplify, not pin.

**QQQ — short-gamma, but the tool contradicts itself.** Spot 717.58, `total_gex` **−$523.8M**, yet the raw `regime` label reads `POSITIVE` and the ZGL returns **261.70** (~64% below spot — a deep-OTM extrapolation, not a level). Graded `NEGATIVE` by the total_gex-sign fallback, with **the label itself flagged unreliable today, not merely the ZGL**. **The put wall at 717 is 0.08% below spot** — effectively no downside cushion; a break below 717 removes the nearest hedging support. Call wall 735 (+2.43%).
**Structure bias:** debit verticals / directional 0DTE. Put debit spread toward 700–710 on continuation, call debit spread toward 730–735 on a bounce off the flip. **No short-vol or pin structures** — walls are too close and the regime is actively amplifying.

**Mandatory caveats — stated, not buried:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and re-computes the ZGL and walls. This orients the open; it is not a level to trade blindly.
- **ZGL reliability: both indices fail today.** SPY is `null`, QQQ is an extrapolated 261.70. Both fall back to total_gex sign + spot-vs-wall position, `zgl_reliable=false`.
- **Gap risk voids the prior.** **FOMC Minutes land tomorrow at 2:00pm ET** — an intraday catalyst that can void this morning prior mid-session regardless of how the open behaves.
- **OPEX front-loading.** Monthly expiry is 2026-08-21 (T+3), so the 0–45d book is unusually concentrated: the 08-21 expiry alone carries **$6.41B** of premium versus $4.19B for the entire 09-18 expiry. These walls are OPEX-week walls, not evenly-distributed ones.
- **Tooling limit.** `uw` cannot isolate the D+1 expiry (`gex --dte-max 1` errors). This is the standing **0–45 DTE** book — the best available proxy, not the isolated next-session expiry.
- **ETF book.** SPY/QQQ ETF gamma, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup — **STAND ASIDE**

The GEX walls above are a **map, not a pin** — wall-as-magnet backtested `NO_GO` on this desk's own data. What validated is a delta-neutral premium-selling edge, and **today it is not present.**

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` / VIX | **LOW** / 15.84 | **LOW** / 15.84 |
| implied move | 0.70% | 1.17% |
| expected range | 1.23% | 2.08% |
| `size_scalar` | 0.5 | 0.5 |
| rolling `mean_pnl_open_pct` (**gross**) | +0.212% | +0.331% |
| **`mean_pnl_open_net_pct`** | **+0.112%** | **+0.231%** |
| **`mean_pnl_by_vix_state.LOW` (gross)** | **+0.01%** | **+0.07%** |

⚠ **`sell_premium: true` is UNCONDITIONAL and must not be read as a green light.** The conditional table is what matters. At **today's LOW VIX tercile** (bounds 16.1 / 17.3 — VIX 15.84 sits below both), the rolling edge is **+0.01% SPY / +0.07% QQQ gross**, and the assumed round-trip cost is **0.1%**. Net of cost both are **zero-to-negative**. The edge in this lane lives only in the **MID and HIGH** VIX terciles (SPY +0.293%/+0.331%, QQQ +0.431%/+0.493%). **Recommendation: stand aside.** This is compounded by the short-gamma book above (short-gamma sessions realise a 1.23%/2.08% range vs 0.77%/1.33% in long-gamma) and by FOMC Minutes at 2:00pm.

`pnl_basis` is **% of underlying spot notional, GROSS** — not premium-collected and not margin-relative. **SPY ≈ SPX** (validated identical); **QQQ is weaker** (Nasdaq index book unavailable) — lower confidence. This lane is **advisory, 0 rubric points, permanently**, until both a vol-shock day enters the sample (the short-vol left tail is currently **UNSAMPLED**) and net expectancy clears a tail-aware bar. Win-rate is explicitly **not** the promotion metric for a negatively-skewed short-vol strategy.

---

## 2b. Swing Dealer Positioning (1–4 weeks)

**No name earns the +1 mechanized DEX-flip rubric line. All nine fully-tested names return `qualifies: false`.**

The rubric requires a verified **sign change** — `sign(net_dex)` on the latest session opposite to ≥3 consecutive prior sessions, with |net_dex| ≥ 0.25× the trailing-10-session median. Computed by `scripts/dex_flip.py` across 11 dated sessions (08-04 → 08-18) per name; not one qualified. Every reading below is a **level**, and a positive DEX level in a tape is beta, which the 2026-05-30 audit measured at **−7pp excess**.

**No vanna squeeze qualifies anywhere, market-wide.** The dated VIX series (raw Yahoo chart API, `^VIX`) reads 08-14 **14.25** → 08-17 **15.19** → 08-18 **15.84**. **VIX has risen two consecutive sessions**, which fails the falling-VIX leg outright. Worse, it inverts the mechanism: for the put-heavy books below (META, AVGO, TSLA, LITE, KLAC, COIN, INTC), rising IV means |put delta| grows and dealers short those puts must **sell** more underlying to stay hedged — **vanna-driven sell pressure, not squeeze support.**

| Ticker | DEX (08-18) | Trajectory | Flip? | Vanna | FEIR@7d | Swing bias |
|---|---|---|---|---|---|---|
| SPY | +11.35B | **−89% from 99.87B (08-04)**, monotonic | ✗ | call-heavy | 0.776 CONTANGO | NEUTRAL, caution-negative |
| QQQ | +10.51B | 68.17B → 10.51B | ✗ | call-heavy | 0.796 CONTANGO | NEUTRAL / SHORT-lean, unconfirmed |
| IWM | +3.49B | 10.68B → 3.49B | ✗ | call-heavy | 0.729 CONTANGO | NEUTRAL |
| MU | +3.49B | built to 17.25B (08-17), **−80% today** | ✗ | call-heavy | 0.932 | NEUTRAL |
| SNDK | +3.06B | whipsaw, 2 sign changes in window | ✗ ⚠whipsaw | call-heavy | **1.075 BACKWARDATION — panic** | NEUTRAL / SHORT-lean |
| META | **−6.24B** | deepened 2 sessions | ✗ ⚠whipsaw (3 changes) | **put-heavy** | 0.817 | SHORT-lean *(advisory)* |
| AVGO | **−1.90B** | negative 3 sessions; **flip is 4 sessions stale** | ✗ (closest miss) | **put-heavy** | 0.707 | SHORT-lean *(advisory)* |
| TSM | +0.84B | 4.54B → 0.84B, −79% in a day | ✗ | call-heavy | 0.734 | NEUTRAL |
| CRWV | +0.50B | 3.37B → 0.50B | ✗ | call-heavy | **1.054 BACKWARDATION — panic** | NEUTRAL |

**The one genuinely tradable dealer-flow observation is SPY's GEX regime flip** — POSITIVE (+$2.02B, 08-14) → FULLY_NEGATIVE (08-17, 08-18, deepening to −$1.22B) — a real, two-session-confirmed regime change landing directly before FOMC Minutes and OPEX. It is a **volatility-amplification** signal, not a directional call.

**Divergences worth carrying:** **NBIS** and **STX** both show call-long DEX books despite −7.6% / −9.2% crashes — either stale positioning or a genuine dip-buy signature. **INTC** shows internal DEX/vanna disagreement (DEX +0.66B call-long, vanna put-heavy) ⇒ no clean thesis. Level-only leans (explicitly **not scored**): LONG — NVDA, MSFT, AAPL, AMZN, LLY, INTU; SHORT — TSLA, LITE, KLAC, COIN.

---

## 2c. Sector Rotation

**Rotation regime call: `growth→value`, confidence LOW — and explicitly not a sized call.** Two mechanical gates block anything stronger.

1. **≥3-day persistence of the netted source cannot be certified.** `market-regime.sector_rotation` is a point-in-time snapshot with no historical netted series available; only the 5-day price tape and 5-day ETF options flow corroborate, and those are a different substrate.
2. **The netted-vs-gross disagreement kills the entire "out" leg.** Every sector's *gross* flow is positive today (a uniformly call-heavy tape), so **any sector netted negative automatically disagrees with gross** — which is Technology, Comm Svcs and Consumer Cyclical, i.e. the whole growth-out side. All three route to **`watch_only`**.

**⚠ Today's persistence column is non-discriminating and carries zero evidentiary weight.** `sector-flow-persistence` fired **INFLOW / persistence_score 1.0 on 10 of 11 sectors** (Real Estate 0.8). It is sign-agnostic **gross turnover**, and `sector-flow` + `sector-flow-persistence` are **one source, not two**. The ≥0.6 leg is technically satisfied everywhere and means nothing. Every directional claim below rests on the **netted** read.

| Sector | Netted | Netted flow | Gross flow | Agreement | Persistence |
|---|---|---|---|---|---|
| Energy | **IN** | +$1.44M | +$993.59M | **agree** | 1.0 *(non-disc.)* |
| Consumer Defensive | **IN** | +$1.32M | +$54.66M | **agree** | 1.0 *(non-disc.)* |
| Technology | **OUT** | **−$409.99M** | +$1,806.79M | **disagree ⇒ watch_only** | 1.0 *(non-disc.)* |
| Communication Services | **OUT** | −$141.57M | +$273.03M | **disagree ⇒ watch_only** | 1.0 *(non-disc.)* |
| Consumer Cyclical | **OUT** | −$53.44M | +$181.72M | **disagree ⇒ watch_only** | 1.0 *(non-disc.)* |
| Real Estate | listed IN, value negative (truncation artifact) | −$1.85M | +$71.87M | disagree | 0.8 |
| HC / Fin / Ind / Materials / Utilities | **truncated** — direction unknown | n/a | positive | n/a | 1.0 *(non-disc.)* |

**Energy is the only fully-agreeing leg** — netted IN, gross positive, price tape (XLE +1.76% / +4.51% 5d) and 5-day ETF options flow (XLE +$7.24M, BULLISH) all align. **No single-name leader clears the conditional +1** anywhere today: **ET** cum_flow_30d +$8.62M BULLISH but **< $50M ⇒ fails gate (c)**; **HAL** +$3.18M ⇒ fails (c); **COST** fails both (b) MIXED and (c). **TRGP** (+7.13%, RS leader) has no options-flow signature ⇒ watch only.

**ETF flow tape (advisory — 0 rubric points).** Instrument-level layer the GICS aggregates cannot see.

| ETF | Net premium dir (5d) | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| **XLE** | **inflow +$7.24M** | BULLISH | large EOD block near mid, inconclusive | mild bullish call tilt ($4.1M Nov 65c) | **agree** | ET, HAL *(neither clears +1)* |
| **XLV** | inflow +$5.02M | BULLISH | largest print 200k sh **−0.30 vs mid — mild distribution tell** | muted | n/a (truncated) | — |
| **XLI** | inflow +$2.92M | BULLISH | modest, at mid | tiny, mixed | n/a (truncated) | — |
| EWZ | inflow +$4.58M | BULLISH | rank-only | rank-only | n/a (geographic) | — |
| **SMH** | **outflow −$26.15M** (largest) | MIXED | huge EOD prints **above mid (+1.22, +0.94) — dip-buy/creation tell** | **clearly bearish** — $24.5M + $9.4M aggressive ask-side puts | agree (weak) | skipped |
| **SOXX** | mixed −$9.67M | MIXED | one print +1.82 vs mid — dip-buy tell | net bearish (2 ask-side puts vs 1 bid-side call) | agree (weak) | skipped |
| **EWY** | mixed −$9.19M | MIXED | mixed, no clean tell | **notably BULLISH** — $8.3M + $7.5M + $6.3M call sweeps **into a −8.13% collapse** | n/a (geographic) | skipped |
| XLY | outflow −$4.19M | BEARISH | rank-only | rank-only | **agree** (netted −$53.44M) | — |
| XLP | outflow −$2.74M | BEARISH | rank-only | rank-only | **disagree** (netted +$1.32M) | — |
| GLD | mixed −$18.47M | MIXED | rank-only | rank-only | n/a (commodity) | — |

**Divergence worth flagging:** **EWY's options tape bought calls aggressively into an 8% single-day collapse** — genuine bottom-fishing in the Korea/semis complex that contradicts both the price action and SMH's own bearish put urgency. Single session, so not actionable under the ≥3-day rule.

**Swing-book implication:** no sized rotation trade. Energy is the only corroborated leg and its magnitudes ($1.44M netted; leaders at $3–9M 30d) are far too small to clear any sizing gate. **Do not short the Tech/semis breakdown** into FOMC Minutes and OPEX on today's data — the netted-vs-gross disagreement makes it `watch_only` by rule despite the price carnage. Revisit if the netted source confirms Technology outflow for two more sessions.

---

## 3. Swing Setups (1–6 weeks)

**Empty. No name is sized.** Five names cleared the Step-3 confluence gate; all five were scored, fundamentals-checked, debated, and gated to `skip`. They are documented here in full because the theses are still being tracked and graded — routing, not suppression.

| Ticker | Score | Tier | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|---|
| **ULTA** | **3** | **LOW** | Short-vol into an earnings kink: KINKED @10DTE (prominence 25.0%, strongest in sample), IV pct 80.9, iv_rank 74.0 | Iron condor short 495P / 538C, wings 475P / 560C, exp 08-28 | **Kills itself on base rate — see below** | **skip** |
| NVDA | 2 | DROP | Institutional call diagonal, event-anchored | Long 232.5C Aug-28 / short 240C Sep-04, 23,249/leg | Loses ~220 into the 08-26 print | **skip** |
| GLD | 2 | DROP | Capped-upside vol mispricing at two local humps | Sell 410C/buy 430C Sep-04; sell 525C/buy 530C Jun-27 | GLD closes above 410 on volume before Sep-04 | **skip** |
| LITE | 2 | DROP | Long vol — IV30 81.6% vs RV20 117.8% | *(calendar abandoned mid-debate)* | Realized vol decays to the 84–88% shelf | **skip** |
| INTU | 2 | DROP | Short-vol into an earnings kink (prominence 13.6%, weakest) | Iron condor short 335P / 366C, wings 320P / 385C, exp 08-28 | **Kills itself on base rate — see below** | **skip** |

**Invalidation discipline (C34) note:** no name carries a usable dark-pool shelf for anchoring, because `accumulation-hunter` returned an empty board and today's DP tape was a **closing-cross contamination event** (below). The invalidations above are therefore structural/level-based, and that limitation is stated rather than papered over with a round-number stop.

### The two findings that killed the book

Both are **earnings-gap base rates**, and both were produced by the debate rather than by the score:

- **ULTA — last 5 prints: −14.24% (2026-03-13), +12.65% (2025-12-05), −7.14% then +8.08% the next session (2025-08-29), +11.78% (2025-05-30), +13.68% (2025-03-14). Mean absolute move ≈ 11.9%, against a 2.86% implied.** The proposed condor's shorts sit 4.1%/4.2% out and its **wings at 8.08%/8.37%** — so **4 of the last 5 prints would have blown clean through the WINGS to maximum loss**, not merely through the shorts. That is not a mispriced condor; it is a structurally inverted one.
- **INTU — last 4 prints (verified independently, twice): −20.02% (2026-05-21), −5.52%, −5.03%, +4.03%. Mean absolute move 8.65% = 2.6× the 3.38% implied.** Shorts at −4.40%/+4.45% ⇒ **3-of-4 clean breach, the miss by 0.4pp**. INTU/QQQ correlation is **−0.33 (20d) / −0.18 (60d) / −0.14 (120d)** — it genuinely decouples from the index, which **concentrates** the idiosyncratic gap risk rather than dampening it.

Two further debate results are worth recording because they show the process working in both directions:
- **NVDA:** the bear verified that the bull's marquee OI number was **the wrong contract** — the +27,817 build is `NVDA260828C00240000` (Aug-28), which is **neither leg** of the long-232.5C-Aug-28 / short-240C-Sep-04 diagonal. The genuine 08-14 Sep-04 build (+22,651 / +24,222) is real; today's headline number is someone else's trade.
- **LITE:** the bear **ran its own attack and it failed.** Decomposing rv20 to test whether 117.8% was a one-day gap artifact, stripping the three largest daily moves still leaves realized vol at **96.3%** — above the entire 83.8–88% belly/shelf. It conceded there is **no clean short leg anywhere on LITE's surface**, and the bull correspondingly **abandoned the calendar structure mid-debate**. The residual then rested on process (an unscored substituted strangle), invalid confluence, and 76 catalyst-free days of theta.

### 3a. Long swings (regime-aligned)
**Empty.** NVDA is the only long-direction name that cleared confluence and it sizes to `skip` on six gates. No `distribution_flag` cautions apply to a sized long because there are none.

### 3b. Short / fade swings (defined risk only)
**Empty — and note there is nothing for the short-routing rule to route today.** None of the five are directional shorts: ULTA and INTU are **delta-neutral short-*vol*** condors and GLD is a **defined-risk credit spread**, all of which fall inside the SHORT-routing rule's own explicit carve-out for vol structures and defined-risk spreads. `contrarian-scanner` produced **zero fades**: SPY z +1.70 and QQQ z +0.585 are not ±2σ extremes; the retail/consumer cluster's real extremes are earnings-imminent (TJX 08-19, ROST/DE 08-20) or statistically thin (DG z +8.109 is a small-denominator artifact on mean PCR 0.63 / σ 0.33); and **DELL** (z +2.281, a genuine $8.4M flow-vs-price divergence) was **stood down on negative QQQ-complex VRP**.

**Sweeps (informational — 0 rubric points; the sweep-persistence line was removed 2026-05-23).** Nothing clears the bar. The five highest-persistence single names — **MU, SNDK, NBIS, AMD, INTC, all 5-of-5 sessions** — are every one tagged `dominant_direction: mixed`, a hard disqualifier. **ORCL** (2/5 bullish) is the cleanest single direction but below the ≥3/5 threshold. Most-likely-fake, all textbook `CALL_BETA_FADE_CHASE`: **SOXL** bullish sweeps into a **−14.8%** day, **CRWV** into **−12.1%**, **SMH** into **−4.1%**. Mega-cap/index sweep volume (QQQ, SPY, AAPL, META bearish 5/5) reads as **index collar/hedge structuring and event-straddling into FOMC Minutes and OPEX** — concurrent SPX 7000c/8000p prints across the 08-21/09-11/10-16/12-18/2027-06-17 tenors — not fresh directional conviction.

---

## 4. LEAP Builds (6–24 months)

**Empty. Zero candidates clear the 6-of-9 gate.** This is a legitimate empty board, not a coverage gap.

The funnel itself was nearly bare: `oi biggest-increases --min-dte 180` returned 20 rows of which only **2 are C12-passing** (CRWV, IWM); `position-rolls` returned 34 rows of which only 3 are C12-passing (EWY, ORCL, AS), all with `balance_ratio` 0.12–0.45 against the 0.7 thesis-intact threshold. With `near_dte_max=21` and OPEX three days out, **essentially 100% of the surviving roll tape is ordinary monthly-expiry mechanics, not near→LEAP extension.**

**Disqualifications (the notes are the deliverable):**
- **CRWV — 2/9, disqualified twice over.** Gate 4 (cum-flow accretion, REQUIRED) **fails**: 90d net +$301.97M against cumulative bullish $5.20B / bearish $4.90B ⇒ **net/gross ≈ 3.0%**, a rounding error on two-sided churn, and ~$240M of the $302M landed in the last 30 days — the "fresh thesis" pattern, not thesis-extension. Gate 8 **hard-fails**: `conviction-matrix` returns **`COVERED_CALL`, confidence 20.5** ("dark pool buying + call selling — yield enhancement, capping upside") — an explicit disqualifier. Gate 1 fails on coherence: the `dte>180` top contracts land on a different strike and expiry almost every session (Jan-28 $35P, Dec-28 $35P, Jun-27 $50/$130P, Jun-28 $65P, Sep-27 $180C) — dispersion, not accretion.
- **IWM — disqualified outright.** 90d net flow **−$1.337B**, `MIXED`, net/gross −4.75% — wrong direction and non-discriminating magnitude. The fresh OI is a 395-DTE $220 put against a $300.23 spot: a portfolio hedge signature, not a single-name directional thesis.
- **The semis/AI complex was probed directly and produced nothing.** `oi-trend --days 10` on MU, NBIS, SNDK, STX, LITE, AVGO, KLAC, AMAT, TSM, AMD, DELL: **none shows a persistent single-strike, single-tenor long-dated build** (AVGO alone lands on four different strikes across four sessions, none recurring; KLAC shows `consecutive_build_days: 0`). This directly answers the adversarial question — **today's 5–12% AI/semis drawdown has NOT produced a coherent long-dated institutional accumulation signature.** What is visible is dispersed daily noise, which is neither the "genuine buying" nor the "forced de-risking" pattern.

Macro context for any 6–24 month thesis: core PCE 3.29% hot with payrolls contracting −23k and the 10Y rising to 4.72% is a stagflationary tint genuinely hostile to long-duration equity risk, and Warsh's debut framework speech on 08-28 is a real regime-uncertainty event for long-duration positioning.

---

## 5. Volatility Surface

**Substrate hygiene is the headline.** Raw `iv-term-structure` would have labelled **15 of 17** names BACKWARDATION; after dropping the 0DTE/expired bucket and sub-15-contract tenors, **10 of 17 flipped (59%)**. This is OPEX week, so the front bucket is maximally polluted and the raw label is maximally untrustworthy.

| Ticker | raw_shape | shape (kink-aware) | base_shape | flipped | FEIR@7d | kept/dropped |
|---|---|---|---|---|---|---|
| DDOG | BACKWARDATION | **KINKED** | BACKWARDATION | ✓ | 0.93 | 16/0 |
| NBIS | BACKWARDATION | **KINKED** | BACKWARDATION | ✓ | 1.038 | 18/0 |
| AMAT | BACKWARDATION | **KINKED** | BACKWARDATION | ✓ | 0.765 | 17/0 |
| DELL | BACKWARDATION | **KINKED** | BACKWARDATION | ✓ | 0.754 | 18/0 |
| STX | BACKWARDATION | **KINKED** | BACKWARDATION | ✓ | 1.055 | 14/0 |
| MU | BACKWARDATION | **KINKED** | **CONTANGO** | ✓ | ✓ | 0.932 | 24/0 |
| ULTA | BACKWARDATION | **KINKED** | **CONTANGO** | ✓ | ✓ | 1.496 | 10/3 |
| QQQ | CONTANGO | **KINKED** | CONTANGO | ✓ | 0.796 | 32/1 |
| SPY | CONTANGO | **KINKED** | **BACKWARDATION** | ✓ | ✓ | 0.776 | 33/1 |
| INTC | BACKWARDATION | **FLAT** | FLAT | ✓ | 0.916 | 22/0 |
| TJX | BACKWARDATION | BACKWARDATION | BACKWARDATION | – | 1.341 | 13/0 |
| LITE | BACKWARDATION | BACKWARDATION | BACKWARDATION | – | 1.048 | 19/0 |
| DE | BACKWARDATION | BACKWARDATION | BACKWARDATION | – | 1.274 | 12/2 |
| VIRT | BACKWARDATION | BACKWARDATION | BACKWARDATION | – | 1.997 | **2/3 (thin)** |
| CRWV | BACKWARDATION | BACKWARDATION | BACKWARDATION | – | 1.054 | 19/0 |
| SNDK | BACKWARDATION | BACKWARDATION | BACKWARDATION | – | 1.075 | 19/0 |
| ROST | BACKWARDATION | BACKWARDATION | BACKWARDATION | – | 1.467 | 7/5 |

`min_contracts = 15` — a **named, tunable parameter, NOT audit-frozen**; reported rather than treated as settled. **front-end-iv-ratio population firing rate: 8 of 17 = 47%** at `--near-dte 7` — a genuine discriminator, versus the ~8-of-9 the `--near-dte 1` default produces. Within `earnings-scout`'s earnings-selected sample it fired **10 of 11 = 91%**, which is near-zero discrimination *there* — the informative fact in that sample is the one name that **didn't** fire (CRWD).

**VRP-vs-realized cross-check — the core value-add today.** The entire semis complex is in deep negative VRP; IV is far below the vol these names are actually delivering:

| Ticker | IV30 | RV20 | Read |
|---|---|---|---|
| NBIS | 93.4% | **178.6%** | strongly NEGATIVE |
| SNDK | 85.5% | **149.6%** | strongly NEGATIVE |
| CRWV | 78.0% | **141.9%** | strongly NEGATIVE |
| LITE | 81.6% | **117.8%** | NEGATIVE |
| MU | 64.8% | 97.9% | strongly NEGATIVE |
| DDOG | 53.8% | 95.2% | strongly NEGATIVE |
| AMAT | 57.5% | 81.7% | NEGATIVE |
| STX | 75.7% | 80.5% | NEGATIVE |
| INTC | 63.4% | 76.1% | NEGATIVE |
| DELL | 81.6% | 82.0% | ~FAIR (the lone exception) |

⇒ **VRP-aligned bias per complex: SPY FAIR (no edge either way); Nasdaq/semis NEGATIVE ⇒ BUY vol, never sell.** A name whose IV rank "looks high" against an rv20 of 150 is not rich premium — that check is what separates a real dislocation from a headline.

**KINKED names, catalyst-aligned:** only **ULTA** — kink at 10 DTE / 2026-08-28, prominence **25.0%**, sitting one day after its 08-27 print; base_shape flips to CONTANGO. Every other kink (NBIS, AMAT, DELL, STX, MU, DDOG at 17–31 DTE) clusters on **2026-09-18 — September monthly OPEX** — i.e. **structural dealer-hedging term inflation, not an event kink**; none appears in the 14-day earnings catalyst. SPY (kink DTE 3 = OPEX, prominence 5.6%) and QQQ (kink DTE 2, prominence 5.9%) are thin mechanical artifacts, not trades.

**BACKWARDATION calendar candidates (no catalyst, post-hygiene):** **LITE** is the best of them (19/19 tenors kept, FEIR 1.048 below panic, no earnings for 76 days) — but see §3, where the calendar structure was abandoned because **no expiry on LITE's entire curve, front through 850 DTE, is priced at or above the 117.8% realizing.** **CRWV** and **SNDK** share the shape at smaller size. **TJX / DE / ROST** are real backwardation but **disqualified as calendars** — earnings 1–2 days out means this is a hold, not a fade. **VIRT** is excluded despite IV percentile 100 (z +2.711): only **2 of 5 tenors survive** the contract floor, so its 1.997 ratio is not a tradable read.

**⚠ Every IV percentile in this section is PROVISIONAL** — `iv-percentile-zscore` returned `dates_used = 89` on **all 17** names, well below the 120-day floor. **No IV outlier survived** from `iv_outliers.json`: every large gap belonged to sub-$5 or 0DTE/OPEX-day contracts. **Skew:** STX/MU/INTC/SNDK/LITE/DELL all print **COMPLACENT** (call IV ≥ put IV, 0.93–1.00) despite the sector risk-off — puts are *not* bid over calls. SPY/QQQ/VIRT show normal **TAIL_HEDGING**, the expected defensive posture into FOMC Minutes and OPEX.

**Any calendar straddling 08-26 / 08-28 is a macro-event structure, not a term-structure trade.** Stated on every candidate above.

---

## 6. Risk & Correlation

**Macro headline:** stagflationary tint — core PCE **3.29%** YoY above target while payrolls contract **−23k** and the 10Y rises to **4.72%**; curve normal (+0.52), USD weakening, fed funds 3.63%. **Forward calendar: FOMC Minutes T+1 · OPEX T+3 · PCE T+6 · Jackson Hole opens T+7 · Warsh's first keynote as Fed Chair T+8 · NFP T+13 · CPI T+18.**

**Breadth:** 224 advancers / 275 decliners, **pct_green 44.62%** (`fz`, independent lineage), against `uw` flow breadth of 31.5% bullish. Index red **and** pct_green < 50 ⇒ **consistent, no divergence flag**. Advisory, 0 rubric points, does not change sizing.

**Correlation clusters (`uw risk portfolio-correlation`, 19-name candidate union — not the static watchlist):**

- **`AI_semis_complex` — CONFIRMED, 6 members, 10 pairs ≥0.70.** NBIS/CRWV **0.904** · AMAT/SMH **0.902** · LITE/SMH **0.859** · SNDK/SMH **0.851** · LITE/CRWV **0.801** · LITE/AMAT 0.791 · CRWV/SMH 0.787 · AMAT/SNDK 0.780 · AMAT/CRWV 0.778 · LITE/SNDK 0.724. **Treat as one position.** LITE is inside it and is not the kept member (5-way score tie broken on |cum_flow_30d| → SNDK) ⇒ −1 tier.
- **`retail_consumer` — PARTIALLY REFUTED.** Only **ROST/BURL 0.789** (30d) / 0.754 (60d) is a real pair. **ULTA appears in no pair at any threshold — its max |corr| to every other candidate is <0.52 at both 30d and 60d.** The Phase-1 claim that ULTA belongs to a retail cluster is **refuted**, and it carries no cluster penalty.
- **Inverse pair surfaced, not penalized: LITE/INTU −0.71.** Magnitude ≥0.70 but negative — the opposite bet, not the same bet; the gate reads corr ≥ **+**0.70 so it does not fire. Recorded because two vol structures on anti-correlated underlyings do not diversify a vol book.

> ⚠ **Instrumentation defect found: `uw risk portfolio-correlation` returns a TOP-10 TRUNCATED pair list, not a threshold filter.** The 19-name run returned exactly 10 pairs, all ≥0.724, hiding the entire 0.60–0.70 soft-watch band until subset re-runs exposed it. Today this was harmless because all 10 returned pairs were genuine cluster members — but on a wider union with more moderate correlations it would **silently drop cluster members**. Flagged for the register. Separately, `sector_breakdown` returned `{Unknown: 19}`, so the tool's "100% in top sector" concentration warning is an **artifact**, not a read; the Step-0 netted sector layer was used instead.

**Gates applied.** **Panic gate no-ops book-wide** — SPY 0.776 / QQQ 0.796 at `--near-dte 7`, both CONTANGO, nowhere near the 1.10 threshold. ULTA (1.496) and INTU (1.252) read above it, but at `near_dte 10` those are **earnings term-premium dated to their own prints** — the short-vol *setup*, already taxed by the event-risk gate; firing panic on it would double-tax one quantity. **VRP is the decisive gate:** SPY FAIR (+0.0079, zero cushion), QQQ NEGATIVE (−0.0292) — **three of the five names are short-vol structures into a FAIR-to-negative vol regime**, and at the name level it is worse than the index read.

**Fundamentals verdicts (top-5).** **No VETOs. Four CAUTIONs, one NA.**

| Ticker | Verdict | Adj | Next earnings | Days | Contradicting facts |
|---|---|---|---|---|---|
| **ULTA** | CAUTION | −1 | 2026-08-27 | 9 | Underlying is actively **bullish** — beat 3/4, **insider NET BUYING (MSPR +26.02, +145,580 shares in March)**, rev +42.98%, D/E 0.022. CAUTION is **event stacking, not deterioration**. Crucially: **no fundamental basis found for the term-spanning put bid** (490/500/510/540 across Aug-28→Sep-18 plus Dec-18 485P, Jun-27 480P) — it reads as **hedging, not informed distribution**, which removes the "smart money knows something" leg from the bear case but does nothing for the vol math. |
| **NVDA** | CAUTION | −1 | 2026-08-26 | 8 | Beat 4/4, rev +70.68%, ROE 111.7% — no deterioration. But **insider MSPR −98.61**, near-maximal −100 in 3 of 4 active months, **−2.74M shares in June**, and routine-vs-opportunistic was **unclassifiable**. Earnings sits *inside* the diagonal. |
| **GLD** | **NA** | 0 | n/a | n/a | ETF/commodity trust — no earnings, insider or leverage surface. **NA never penalizes.** Risk read is macro-only. |
| **LITE** | CAUTION | −1 | 2026-11-02 | 76 | Beat 4/4, rev +83.22%, and the only company headline is *bullish* ("optical shortage getting bigger") against a −9.87% day ⇒ sector contagion, not an idiosyncratic break. But **GAAP net margin −230.1%**, **D/E 2.2677 (highest in set)**, PS 23.55, insider selling 2 of 3 months. **Three independent lenses converge bearish**: DP distribution 0.321, DEX −0.49B put-heavy, insider selling. |
| **INTU** | CAUTION | −1 | 2026-08-25 | 7 | Beat 3/4, D/E 0.303, Mizuho Outperform $430 PT; insider selling **de-escalating** (Jun −100 → Jul −15.8 → Aug +10.9). CAUTION is event stacking. |

**Event-risk flags:** every one of the five spans ≥2 named, dated Tier-1 binaries. ULTA and INTU's own earnings are **exempt** as the event play; the stacking that fires the gate is OPEX (T+3), PCE (T+6) and Warsh (T+8) being held *through*. GLD's near leg expires **2026-09-04 = NFP day**, after Minutes, OPEX, PCE and Jackson Hole.

**Debate-disconfirmation cuts: the bear won 5 of 5 — a clean sweep, with every bull residual below 0.55 and three at ≤0.35.** ULTA 0.35/**0.85** · NVDA 0.35/**0.75** · GLD 0.35/**0.45** · LITE 0.25/**0.45** · INTU 0.15/**0.85**. Four of five pairs are also **BOTH_SIDES_LOW** — neither advocate could clear a coin flip. No round-2 escalation triggered (that requires residuals within one bin **and** ≥0.75). This is not five close calls; it is an entire board on which no advocate could make the case.

**Adverse-flow exit list.** ⚠ `conviction_2026-08-17` **does not exist** — yesterday's run wrote no group, consistent with the empty-board streak. Most recent existing group used: **`conviction_2026-08-14` = [ROST]**.
**ROST — EXIT CANDIDATE.** close 236.38, `flow_direction: bearish`, P/C 1.227, net_flow −166,259, **iv_rank 95.27**, volume_ratio 2.23. Three alerts fired: VOLUME_SPIKE 2.2× (med), HIGH_IV_RANK 95.3 (med), LARGE_DARK_POOL $129.2M single print (high). **⚠ Discount the dark-pool alert** — $129.2M of $181.3M total DP premium is **71.3% of the day's DP in one trade**, the textbook closing-cross signature, i.e. mechanical, not informed distribution. The exit tag rests on the flow legs plus iv_rank 95.3 making anything long-premium unaffordable, plus earnings 08-20. **Do not re-enter.**

**Hedge sleeve.** Today's book has zero net delta because it has zero positions; this is for a desk carrying **pre-existing** risk into the 08-19 → 09-04 stack. **Protection is unusually cheap right now and that is the actionable observation** — QQQ VRP is −0.0292 (IV below realized) and SPY/QQQ front-ends are in contango at 0.776/0.796.
- **Primary: QQQ put vertical, ~08-28 expiry** — one expiry spanning FOMC Minutes (T+1), OPEX (T+3), PCE (T+6) and Warsh (T+8), with the long leg bought below realized. Size to net delta.
- **Hedge SMH/SOXX, not SPY, for a semis book.** RSP beat SPY today; an index hedge structurally under-hedges concentrated damage. SOXL −14.8% and EWY −8.13% show where the convexity actually is.
- **Prefer this to a VIX call ladder** — VIX 15.84 is low in absolute terms but already rising two sessions, and roll carry is punitive versus the QQQ route.
- **Do not sell index premium into this window** (see §2a).

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**This section is empty. Zero names reached MEDIUM (7) or HIGH (9).** The maximum achievable score today was **6** — multileg +2 ∧ earnings +1 ∧ vol-surface +1 ∧ oi-build +1 ∧ cum-flow +1 — and **no name carried more than two of those five lines.** The board capped out below MEDIUM before any gate fired. Reaching 7 today would have required inventing a line.

**Expectancy lens `[advisory — expectancy is not yet a live sizing axis]`** (from `/calibration-audit` 2026-08-15, `phase_3_calibration`):

| Tier | n | Mean P&L | Payoff ratio | Capped ½-Kelly |
|---|---|---|---|---|
| HIGH | 7 | **−2.441%** | 0.72 | 0.0 |
| MEDIUM | 19 | **+0.104%** | 0.948 | 0.0132 |
| LOW | 108 | −1.963% | **1.008** | 0.0 |
| DROP | 438 | −2.870% | 0.787 | 0.0 |

C3 gate status **`ADVISORY_ONLY`** — n=27 closed sized calls (<30 floor) **and** tier×expectancy is non-monotone. The live sizer remains the win-rate ladder. Read plainly: **MEDIUM is the only tier with positive expectancy, and HIGH is the worst-performing sized tier.** That is the standing tier inversion, and it is why nothing here is force-fitted upward.

**Full audited breakdown of the five confluence-gate passers** (all `skip`; the rubric they were scored against is embedded below):

| | ULTA | NVDA | GLD | LITE | INTU |
|---|---|---|---|---|---|
| `raw_score` | **3** | 2 | 2 | 2 | 2 |
| tier | **LOW** | DROP | DROP | DROP | DROP |
| `score_components` | +1 earnings SELL VOL · +1 vol-surface KINKED · +1 oi-build | **+2 multileg** · +1 oi-build · **−1 flow_conflict_lite** | **+2 multileg** · +1 oi-build · **−1 flow_conflict_lite** | +1 vol-surface · +1 oi-build | +1 earnings SELL VOL · +1 oi-build |
| `dominant_signal_class` | `earnings_vol` | `multileg_directional` | `multileg_directional` | `vol_long` | `earnings_vol` |
| `confluence_score` | 6 (Step-0 **bearish** funnel) | null | null | null | null |
| `win_rate` (n, source) | **null — `NA(substrate)`** | null — `NA(substrate)` | null — `NA(substrate)` | null — `NA(substrate)` | null — `NA(substrate)` |
| `market_excess` | unknown (substrate) | unknown | unknown | unknown | unknown |
| `implied_move` | **2.86%** (straddle) | n/a | n/a | ≈25.2% *(proxy)* | **3.38%** (straddle) |
| pre-risk size | **starter** | skip | skip | skip | skip |
| `fundamentals_verdict` | CAUTION | CAUTION | **NA** | CAUTION | CAUTION |
| debate residuals (bull/bear) | 0.35 / **0.85** | 0.35 / **0.75** | 0.35 / **0.45** | 0.25 / **0.45** | 0.15 / **0.85** |
| gates fired | vrp, sector, fundamentals, event_risk, debate **(5)** | regime, vrp, sector, fundamentals, event_risk, debate **(6)** | regime, vrp, event_risk, debate **(4)** | **cluster**, sector, fundamentals, debate **(4)** | vrp, sector, fundamentals, event_risk, debate **(5)** |
| **final size** | **skip** | **skip** | **skip** | **skip** | **skip** |
| invalidation | 4-of-5 prints breach the **wings** | loses ~220 into the 08-26 print | closes >410 on volume pre-Sep-04 | RV decays to the 84–88% shelf | 3-of-4 prints breach the shorts |

**`win_rate` is `NA(substrate)` on every scored passer** — `earnings_vol`, `multileg_directional` and `vol_long` are **not among the 5 classes `signal-backtest` supports** (`bullish_flow` | `bearish_flow` | `high_iv_rank` | `volume_spike` | `dark_pool_accumulation`), so neither a win rate nor a same-window SPY excess is computable. A call with unmeasurable excess **cannot be beta-flagged either way**, so `unknown(substrate)` is recorded rather than a number invented. The two measurable classes today, under the P0.3 clean-query protocol (`--top-n 200`, rows post-filtered to complete forward windows, WR recomputed on the kept n — the tool's headline is never quoted):

| Class | Headline (never quoted) | Clamped dropped | Sub-C12 dropped | Kept n | **Clean rate** | SPY benchmark | **Excess** |
|---|---|---|---|---|---|---|---|
| `bullish_flow` | 48.0% (`truncated_signals`=9) | 9 | 10 | **131** | **0.5038** | 0.5802 | **−0.0763** |
| `high_iv_rank` | 81.0% (`truncated_signals`=15) | 15 | 20 | **154** | 0.7987 | 0.2273 | +0.5714 |

> The `high_iv_rank` **+0.5714 excess is not edge and must not be quoted as a discovery.** For a non-directional class the benchmark is structurally mis-specified — it compares *single names* realising >2% in 5 days against *SPY* doing so, and single names are far more volatile by construction. That is **volatility beta**. The 2026-08-01 class ceiling caps `high_iv_rank` at 0.60 regardless, landing it in the anti-predictive [0.55, 0.65) band ⇒ `starter`.

### Three substrate findings that matter more than today's calls

1. **The board was manufactured by a constant.** `uw historical oi-trend` returned **BUILDING with `consecutive_build_days: 5` on 19 of 19 scored names — a 100% firing rate.** It adds +1 to every row and contributes **zero ranking information**. Strip it and the board is **ULTA 2, everything else ≤1, and there is no LOW tier at all.** Corroborating the churn concern, the ≤3DTE share of the OI change (OPEX is T+3) is majority-churn on four names: **LITE 53.3%, DE 51.5%, SNDK 47.8%, AMAT 45.1%**; cleanest builds are ET 2.1%, GLD 3.5%, HAL 10.9%. This is the same zero-discrimination pattern already logged for `front_end_iv_ratio` (8-of-9 at the default) and `sector-flow-persistence` (11-of-11). **Recommend registering it as a criterion.**
2. **`cum_premium_flow` is churn on 15 of 19 names.** `trend_direction: MIXED` on 15/19, and **net-as-%-of-gross is below 5% on 15 of 19**. NVDA's headline +$361.96M is **1.26% of $28.7B gross**. **Zero names earned the +1 accretion line.** The four with a real relative signature — **ET 15.38%, HAL 8.08%, CRWV 6.79%, ROST 6.06%** — each fail on absolute scale (<$50M) or on the C28 intent screen. Worth stating plainly: **the rubric's absolute dollar floors are scale-blind and discarded ET, the one name today whose premium tape is genuinely one-sided.** That is the mirror image of the mega-cap degeneracy the C11 scale-relative floor was written to fix, and it is a candidate for pre-registration — **not something to act on inside a frozen rubric.**
3. **ULTA's two vol points are one bit counted twice.** `earnings-scout` and `vol-surface-scout` read the **identical term-structure kink through the same hygiene module**. On genuinely independent evidence ULTA scores **2 — DROP**. The one name above the floor is arguably a scoring artifact. **GLD's confluence pass has the same defect in a different form**: its "second agent" (sweep-tracker) flagged the *identical* 525/530C Jun-27 ticket and then routed it to multileg itself — a one-agent name wearing a two-agent badge.

4. **Schema gap: `vol_long` is not a canonical `dominant_signal_class`.** The envelope validates (exit 0) but emits 5 warnings — LITE, NBIS, AMAT, CRWV, SNDK all carry `vol_long`, which is off the schema's `x-canonical-classes` list. It was **kept deliberately rather than mapped**: the only canonical vol buckets are `earnings_vol` (no earnings on these names), `event_vol` (vol-surface-scout explicitly found the kinks are structural September-OPEX term inflation, *not* event kinks) and `high_iv_rank` — and `high_iv_rank` is a **sell-rich-premium class carrying a live 0.60 audit ceiling**, whereas these rows are the exact opposite trade (buying vol because IV sits *below* realized). Forcing that label would pollute a calibrated class with opposite-direction rows to silence a warning. `vol_long` already has **5 prior uses in the corpus**, so this is an existing gap, not a new invention. **Recommend registering `vol_long` as canonical** — it is a real, recurring, non-directional class the schema does not yet name.

### Conviction rubric (Step 4) — version `2026-06-12`, FROZEN

```
Daily conviction score = Σ:
  +1  MECHANIZED DEX flip / vanna-squeeze in trade direction — verified SIGN CHANGE, never a level.
      sign(net_dex) latest session opposite ≥3 consecutive priors; |net_dex| ≥ 0.25× trailing-10-session
      median |net_dex|. Computed by scripts/dex_flip.py, never by hand. Vanna disjunct needs a dated VIX.
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified
      institutional-tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms
      (sign aligned AND |cum_flow_30d| ≥ $50M); else halved to +1.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  conviction-matrix DIRECTIONAL_LONG conf > 70 — ONLY when dominant_signal_class == leap_directional
  +1  cumulative-premium-flow net directional accretion (30d) — INTENT-SCREENED: (a) no C28
      distribution_flag on the name, AND (b) on dividend payers in an ex-div window, accreting prints are
      NOT deep-ITM sub-parity calls. Failed or unevaluated on a flagged name ⇒ 0.
  +1  sector-rotation single-name leader — CONDITIONAL on ALL of: (a) sector persistence_score ≥ 0.6,
      (b) cum_flow_30d direction aligned, (c) |cum_flow_30d| ≥ $50M. Default 0.
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored play type)
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner overcrowded long with RISING pc-ratio-zscore (VRP positive) — an INFORMED-FLOW
      CONTINUATION penalty, NOT a "crowd is wrong, fade it" signal (Pan-Poteshman 2006; Ge-Lin-Pearson 2016).
  -3  flow_conflict — cum_premium_flow 30d CLEARLY OPPOSITE dominant_signal_class (sign flip + magnitude >
      today's union-median |cum_flow_30d|, or explicit OPPOSITE label)
  -1  flow_conflict_lite — 30d read is MIXED (signed sum near zero, or aligned but bottom-quartile magnitude)
      [flow_conflict and flow_conflict_lite are MUTUALLY EXCLUSIVE — apply exactly ONE]
  # TIER GATES (risk-monitor, Step 2d) — 0 points, never in score_components:
  -1 tier  correlation cluster (pairwise corr ≥ 0.70)
  -1 tier  market-regime conflicts with trade direction
```
**Tiers:** ≥9 HIGH (full) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 DROP.
**Today's union-median |cum_flow_30d| = $32.97M** (n=19); 25%-of-median $8.24M; bottom quartile $3.18M.
**Σ `score_components` == `raw_score` verified on all 19 rows.** No tier-gate line was emitted into `score_components`.
**Tier-cut status:** the ≥9 HIGH cut failed its scheduled re-confirmation on 2026-06-12 and is retained under the P0.1 freeze with **no validated ranking claim**; the P0.6 out-of-regime guard caps all sizing at half in the interim.

**Deep-dive hand-off:** skipped — no HIGH-tier names. (`/stock-deep-dive` is reserved for the top-2 HIGH-tier post-gate names; there are none.)

---

## 8. Watch-only — single signal, no confluence

Flagged by exactly one Phase 1 agent, so excluded from the rubric. Listed for journaling, **not for trade entry**.

| Ticker | Sole flagging agent | Read |
|---|---|---|
| **CRWD** | earnings-scout | **BUY VOL, its top pick.** The only name in the earnings sample **not** panicking into its own print — FEIR 0.916 CONTANGO, and the 10DTE earnings-adjacent tenor is *lower* than the front. Its real kink sits at 31 DTE / 09-18 (September OPEX), not its earnings. Largest premium imbalance in the sample at **−$11.7M bearish**, unmatched by any vol bid. Earnings 08-26, implied move 3.48%. |
| **BABA** | earnings-scout | BUY VOL — back skew **COMPLACENT** (0.919, no downside insurance priced), iv_rank only 62.9, on a China ADR with a history of realized > implied on regulatory headlines. Earnings 08-20, implied move 5.61%. |
| **NBIS** | vol-surface-scout | BUY VOL / calendar into the 09-18 hump. IV 93.4% vs **RV20 178.6%** — the most extreme negative VRP in the book. |
| **AMAT** | vol-surface-scout | KINKED @31DTE (09-18), prominence 25.8%, FEIR 0.765. Net premium flow is **0.01% of gross** — the purest churn reading in the entire set. |
| **CRWV** | vol-surface-scout | BUY VOL, but carries a **C28 `distribution_flag`** (Jan-27 145C OI −1,877, $2.49M) and fell −12.10%. The one name whose cum-flow would otherwise have earned the +1 accretion line (BULLISH, +$239.7M, 6.79% of gross) — **denied by the intent screen, which did exactly its job.** |
| **SNDK** | vol-surface-scout | BUY VOL shape, but its +$1.47B 30d net is heavily contaminated: a **$455M closing-cross print = 64% of the mega tier** at the identical closing price; net only 2.67% of gross. |
| **TJX / ROST / DE** | earnings-scout | SELL VOL half-size (mechanical front-panic, not a clean mispricing). All three report within 2 days — **event-driven, so `contrarian-scanner` disqualified them as fades** and `vol-surface-scout` disqualified them as calendars. |
| **BURL / DG** | earnings-scout | BURL minimal size (skew unmeasurable at the intended tenor, 6 of 10 tenors dropped). DG small BUY VOL (complacent skew + smallest implied move in the sample, 2.74%, on a name with a fat-tail gap history). |
| **DELL** | contrarian-scanner | z **+2.281 BEARISH_EXTREME** with a genuine $8.36M flow-vs-price divergence — **stood down on negative QQQ-complex VRP**. Its `high_iv_rank` clean rate 0.7987 (n=154) caps to 0.60 and floors to starter; moot at DROP. |
| **ULTA** *(also §7)* | contrarian-scanner | Carried as an **informed-continuation caution**, explicitly **not a fade** — the put crowd is plausibly the informed side. |
| **ET / HAL / TRGP** | sector-rotation-strategist | Energy leaders; ET and HAL both fail the +1 gate on |cum_flow_30d| < $50M. **ET has the cleanest directional flow signature in the entire scored set by relative measure (15.38% net-of-gross, 2.1% OPEX churn) and scores 1.** TRGP is a price/RS leader with no options-flow signature. |
| **ORCL** | sweep-tracker | Cleanest single sweep direction (2/5 bullish) but below the ≥3/5 bar — **and it took the day's only −3 `flow_conflict`** (−$69.54M, 2.11× the union median, directly opposing a LONG thesis) for a final `raw_score` of **−2**, the lowest on the board. |
| **SMH** | multileg-strategist (context only) | Coordinated 515P/545P Sep-04 put buying, $23.8M + $9.4M, both ask-side. Directionally aligned with the tape but **structurally ambiguous** (both legs bought — the offsetting leg is off the top-20 cutoff), so no +2 was granted. |
| **MU / INTC / AMD** | sweep-tracker | 5-of-5 persistence but `dominant_direction: mixed` — **a hard disqualifier, not a positive flag.** Two-way churn on already-crushed names. |
| **META / AVGO / TSLA / KLAC / COIN** | dealer-positioning-strategist | Level-only SHORT leans with put-heavy vanna taking **sell pressure** from rising VIX. **Not scored** — no DEX flip qualified. AVGO is the closest miss (a real 3-session-run flip, but 4 sessions stale). |
| **NKE** | opex-pin-strategist | The only name to clear the OPEX distance gate (**0.10%**, strike 40 vs spot 40.24) — then **disqualified as an anti-pin**: `FULLY_NEGATIVE` GEX with strike-40 net_gex **−$61.2M, the single most negative strike on its chain**. Massive OI mass sitting on short gamma amplifies moves through the strike instead of pinning to it. |

**Also formally empty:** `accumulation-hunter` (no ticker cleared ≥3 aligned signals — today was a **closing-cross contamination event**: MSFT $1.02B @20:00:06Z, MU 2×$711M = 71% of its mega tier @20:05Z, SNDK $455M = 64% @20:22Z, all at the identical closing price; `institutional-accumulation` returned **NEUTRAL** for MU/SNDK/INTC despite mega buy_ratios of 0.93–0.95; LITE/STX/NBIS/KLAC are net **DISTRIBUTION** at block buy_ratios 0.32/0.27/0.32/0.19); `opex-pin-strategist` (empty book — **stand-aside OPEX week**); `leap-positioning-radar` (empty); `contrarian-scanner` (no fades).

**Single-leg whale scan (advisory, 0 rubric points — permanently; C19 CLOSED as REFUTED 2026-07-25).** Eight **Tier-1 `FLOOR_PUT_BLOCK`** signals fired, all 3-DTE expiring at Friday's monthly OPEX, deltas −0.90 to −0.96: **TSLA, META, MU, ORCL, AAPL**, GOOGL, APP, QCOM (the last three not C12-confirmed). Executed same-session as the semis risk-off, into FOMC Minutes and OPEX — these read as **structural hedges into a stacked catalyst week, not discretionary crowding to fade.** Routing context only.

---

### Watchlist write-back

```
group:    conviction_2026-08-18
written:  ["ULTA"]
verified: conviction_2026-08-18 = ['ULTA']   (post-write read-back confirmed)
excluded: NVDA, GLD, LITE, INTU + all 14 remaining union names — ALL DROP tier (raw ≤ 2).
          Group deliberately NOT padded to five names, per the corrected 2026-07-23 rule:
          write LOW-tier-or-better only, never the raw top-5.
vetoes:   none issued today.
note:     ULTA is written at LOW tier for tomorrow's correlation and adverse-flow measurement
          even though it sizes to `skip`. Write-back is keyed on TIER, not on final size —
          this is what keeps the counterfactual gradeable.
```
