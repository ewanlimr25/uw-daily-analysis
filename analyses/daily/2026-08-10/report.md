# Daily Market Analysis — 2026-08-10

## Executive Summary

- **Regime + GEX state:** `uw risk market-regime` = **TRANSITIONAL** ("Mixed signals, reduce position size, wait for clarity") on an **UPTREND** trend — SPY **773.03**, above 20SMA (751.37) and 50SMA (747.56), +2.39% 30d, −0.49% from the 90d high. **VIX 15.46.** SPY sits in a genuine **NEAR_FLIP** (spot 772.87 vs ZGL 773.02 — fifteen cents), QQQ long-gamma, IWM's label and aggregate contradict. UW breadth **34.9% bullish-flow tickers**; `fz` breadth 45.73% green. Netted sector rotation **IN** Financial Services / Healthcare / Energy, **OUT Technology −$279.9M**.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** **SPY** — long-gamma by aggregate (`total_gex` **+$1.843B**) despite a NEGATIVE label · ZGL **773.02** (reliable, 0.02% from spot) · call wall 773 / put wall 765 · **pin-lean 773–775 with wider wings — the regime has flipped 3× in 4 sessions on a `total_gex` that barely moved.** **QQQ** — POSITIVE, `total_gex` +$368.1M · **ZGL 220.46 is an artifact, `zgl_reliable=false`** · call wall 730 (+1.22%) / put wall 715 (−0.86%), **both inside the 1.42% expected range** · condor, not a fly. Advisory, 0 rubric points — see §2.
- **Top swing build:** **none.** The board is **empty — zero sized positions.** The only name that cleared both the confluence gate and the drop floor is **MSFT (raw 6, LOW)**, and it took **three independent cuts** — fundamentals CAUTION, event-risk CPI at T+2, and the debate gate — landing at **`watch_only`**. Both debate advocates, arguing opposite sides, independently recommended `watch_only` over `starter`.
- **Top LEAP candidate:** **none.** LEAP share of DTE volume is **3.9%** (the thinnest bucket); zero names reached 6-of-9 gates. The only two funnel hits in `oi biggest-increases --min-dte 180` were **AG and HL, both puts**.
- **Biggest risk:** **CPI Wednesday 2026-08-12, two sessions out**, with PPI Thursday behind it. Every structure considered today sits inside the ≤T+3 event band. Correlation clusters collapse the candidate list further: **{INTC, MRVL, SNDK}** at 0.85–0.94 is one semis position and **{HD, LOW}** at 0.930 is one short-vol retail position. **No hedge sleeve is recommended** — directional skew is 0.00 and hedging a book with no positions would be initiating a naked CPI bet under a risk-management label.

---

## 1. Regime & Gamma State

**`uw risk market-regime`: TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity."** Trend UPTREND. Guidance: *"Half position sizes. Favor defined-risk strategies. Iron condors in range."* Market breadth 2,190 bullish / 4,091 bearish of 6,281 optionable = **34.9% bullish**.

**This was a rotation day, not a distribution day** — the distinction is outcome-relevant and the single regime label hides it. Cap-weighted vs equal-weight (raw Yahoo OHLC, `--as-of 2026-08-10`):

| | 1d% | 5d% | rv20% |
|---|---|---|---|
| SPY | −0.03 | +2.03 | 13.6 |
| QQQ | −0.30 | +2.97 | 24.5 |
| IWM | −0.52 | +1.27 | 15.0 |
| **RSP (equal-weight)** | **+0.06** | +1.43 | 10.6 |

**RSP ≥ SPY > QQQ.** Equal-weight beat cap-weight, so the red was concentrated, not broad. Sector ETFs 1d%: **XLE +4.66**, **XLV +1.67**, XLB +0.61, XLC +0.52, XLF +0.36 | XLY −0.16, XLP −0.20, XLI −0.31, **XLK −0.88**, **XLU −1.10**, **XLRE −1.29**.

What was sold: the AI/semis/optics complex — **COHR −14.24** (the S&P's worst mover), LITE −8.61, SOXL −7.31, IREN −6.04, RIOT −5.46, WULF −5.15, MRVL −4.65, FSLR −4.29, INTC −4.06, RKLB −3.37, NVDA −2.86, AMD −2.86, CRWV −2.74, **SMH −2.28**, MU −1.89, AVGO −1.25. **But nearly every one is up on the 5d** (NVDA +5.28, MRVL +7.63, INTC +7.16, COHR +12.84, SOXL +11.39, AVGO +7.69). Today was a one-session reversal off a strong week, not an established downtrend.

What was bought: energy (USO +6.73, RIG +8.75, BOIL +8.32, CRK +7.08, NE +6.82), precious metals (AGQ +6.53 / 5d **+27.56**, SLV +3.32, HL +4.15 / 5d +21.62, GFI 5d +21.02, AG 5d +20.06, GLD 5d +8.29), healthcare (LLY +3.90 / 5d +9.86, RDNT +6.76), and software/security (PANW +5.82, CRWD +5.01, ORCL +2.74, NOW +2.05, MSFT +1.21, UBER +4.01, CHYM +6.01, BSP +15.70).

**The intra-tech split is the day's real story:** MSFT printed **+$51.5M** net premium with price +1.21% while NVDA (−$49.0M), MU (−$38.7M), TSM, AVGO, MRVL, ASML, INTC and SNDK were all net-bearish. Software bid, semis sold.

### Per-index gamma (current-state EOD book, 0–45 DTE)

| | spot | zero-gamma | total GEX | regime (label) | call wall | put wall |
|---|---|---|---|---|---|---|
| **SPY** | 772.87 | **773.02** (reliable, 0.02% away) | **+$1,843,417,646** | NEGATIVE | 773 ($493.0M) | 765 (−$33.6M) |
| **QQQ** | 721.20 | **220.46 — ARTIFACT, unreliable** | **+$368,101,679** | POSITIVE | 730 ($95.8M) | 715 (−$25.8M) |
| **IWM** | 299.90 | **159.84 — ARTIFACT, unreliable** | **−$309,056,450** | POSITIVE | 305 ($73.5M) | 295 (−$103.2M) |

⚠ **Two label-vs-aggregate contradictions, in opposite directions.** SPY's discrete label reads NEGATIVE while `total_gex` is strongly **positive**; **IWM's label reads POSITIVE while `total_gex` is −$309M**. In both cases trust the aggregate sign over the label. And the ZGL field is only usable on SPY — QQQ printed 220.46 against a 721 spot and IWM 159.84 against a 300 spot. This is the known ZGL-grid defect, and `dealer-positioning-strategist` found it recurring across QQQ, IWM, MRVL, TSM and AVGO with garbage values (314.06, 300.24, 352.82, 220.46) interleaved with plausible ones. **Registered as a substrate finding.**

**`uw options-flow dte-volume-share`: 0DTE 34.9% · weeklies 25.0% · monthlies 24.9% · LEAPs 3.9% → `regime_hint: BALANCED`.** Institutional (monthly+) share 28.8% — neither retail-dominated nor institution-dominated, so no benefit of the doubt in either direction for rotation or positioning conviction.

**`uw historical vrp`:** **SPY FAIR −0.0016** (IV30 13.04% vs realised30 13.20%) — no VRP edge. **QQQ PREMIUM_BUYING −0.0503** (IV30 **20.43%** vs realised30 **25.46%**) — Nasdaq is moving materially more than options imply, corroborated independently by QQQ rv20 24.5% against SPY's 13.6%. Long premium on the Nasdaq complex is comparatively cheap; selling it fights the vol regime.

**Macro backdrop** (`scripts/fred_macro.py`, `available: true`): yield curve **normal** (10Y−2Y +0.47) but the composition is stagflationary — **core CPI 2.81% / core PCE 3.29% YoY** (sticky above target), unemployment 4.1%, **payrolls −23k MoM** (outright contraction), **10Y 4.65% and rising** (+9bp/30d) against a 2Y at 4.19% (−2bp), **USD weakening** (−2.07/30d), fed funds 3.63%. That combination is the coherent reason rate-sensitives (XLU −1.10, XLRE −1.29) are the worst sectors and gold/silver/energy the best — it is a tape that punishes duration and rewards real assets.

**Forward event risk — a Tier-1 stack inside 48 hours:**

| Event | Date | Trading days out | Impact |
|---|---|---|---|
| **CPI (July)** | **Wed 2026-08-12** 08:30 ET | **T+2** | **HIGH** |
| **PPI (July)** | **Thu 2026-08-13** | T+3 | **HIGH** |
| Retail Sales (July) | Fri 2026-08-14 | T+4 | MED-HIGH |
| Initial claims | Thu 08-13, Thu 08-20 | T+3 / T+8 | LOW |
| FOMC minutes (Jul 28–29) | ~Wed 2026-08-19 | T+7 | MEDIUM |
| **Monthly OPEX** | **Fri 2026-08-21** | T+9 | MEDIUM |
| Jackson Hole | Aug 27–29 | T+13 | MEDIUM |
| Core PCE | ~Fri 2026-08-28 | T+14 | HIGH |
| FOMC decision | Sep 15–16 | T+25 | HIGH |

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — built from open interest that **persists overnight** — read forward as the *prior* for the next session's open. It is **prose-only, contributes 0 points** to the conviction rubric, and makes **no backtested predictive claim**. Predictive validation of these levels lives in `/weekly-analysis`'s rolling §2 backtest, not here. Scope is **SPY and QQQ only**.

### SPY — long-gamma by aggregate, but a genuine NEAR_FLIP

`spot 772.87 · ZGL 773.02 · zgl_reliable TRUE · total_gex +$1,843,417,646 · label NEGATIVE`

Call wall **773** ($493.0M) is essentially co-located with spot rather than sitting further out; the next heavy long-gamma strikes are **775 (+$450.1M, +0.28%)** and **780 (+$491.3M, +0.92%, a round-number magnet)**. The put wall at **765 (−$33.6M, −1.02%)** is the deepest point of a **diffuse negative-gamma trough spanning 748–767**, not one dominant strike — 755 (−$32.6M), 760 (−$32.3M) and 767 (−$30.7M) are all comparable.

**Regime freshness: FRESH and UNSTABLE, not held.** The label has flipped **three times in the last four sessions** — POSITIVE→NEGATIVE 08-05, NEGATIVE→POSITIVE 08-07, POSITIVE→NEGATIVE again today. But `total_gex` barely moved between 08-07 ($1.852B) and today ($1.843B): the flip is a razor-edge artifact of spot ticking **fifteen cents** below ZGL, not a real change in dealer positioning. **Read the aggregate sign, not the discrete label.**

**Read:** spot sits on top of a very large long-gamma concentration (773/775/780), which argues **mean-revert / pin bias into the open near 772–775**. But the daily label whipsaw is itself evidence of fragility. If spot slips below ~770 it enters the diffuse 748–767 negative-gamma trough, which would **accelerate** a move rather than cushion it.

**Structure bias:** iron fly / short straddle / butterfly centred **773–775** — which matches the independently-derived `zerodte_setup` centre of 772.82 — but keep wings **wider than the raw 0.82% expected range suggests**, or add a downside put-wing buffer, because of the flip instability and the air pocket below 768. Not a high-conviction pin; a pin-lean with real whipsaw risk.

### QQQ — long-gamma, held, but walls inside the expected move

`spot 721.20 · ZGL 220.46 · zgl_reliable FALSE · total_gex +$368,101,679 · label POSITIVE`

The ZGL is **69% away from spot** — a textbook instance of the ZGL-grid artifact — so the read falls back to the `total_gex` sign plus spot-vs-wall position. Call wall **730** ($95.8M, **+1.22%**), next tier 735 (+1.92%) and 740 (+2.61%). Put wall **715** ($25.8M, **−0.86%**), next 700 (−2.94%).

**Regime HELD** — POSITIVE on 4 of the last 5 sessions with a single NEGATIVE dip on 08-06. Materially more stable than SPY's whipsaw.

**Read:** long-gamma → mean-revert / vol-suppression lean. But **both walls sit inside the 1.42% expected range**, so a normal 0DTE session could test or pierce either — treat 715/730 as soft speed bumps, not boundaries.

**Structure bias:** **condor rather than a tight fly** — shorts just inside 715/730, long wings out toward 700/735–740 to survive a wall-piercing move within the expected range. Size QQQ smaller than SPY.

**Mandatory caveats — stated, not buried:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and re-computes the ZGL and walls. Given SPY's label has flipped 3× in 4 sessions, tomorrow's opening print could easily flip it a fourth time.
- **ZGL reliability:** trustworthy on SPY only (0.02% from spot). **QQQ's is an artifact and must not be used.**
- **Gap risk voids the prior.** **CPI lands Wednesday 08-12 and PPI Thursday 08-13**; overnight Asia/Europe macro applies too. This map orients an open, it does not survive a print.
- **Tooling limit:** `uw` cannot isolate the D+1 expiry (`gex --dte-max 1` errors). This is the standing **0–45 DTE** book — the best available proxy, not the isolated next-session expiry.
- **ETF book,** not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — the validated stack)

The GEX walls above are a **map (advisory "where"), not a pin** — wall-as-magnet backtested NO_GO, as did every directional 0DTE signal (charm, vanna, intraday momentum). What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, and **not a guaranteed edge**.

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` / VIX | **LOW** / 15.46 | **LOW** / 15.46 |
| `implied_move_pct` | 0.63% | 1.04% |
| `expected_range_pct` | **0.82%** | **1.42%** |
| `size_scalar` | **0.5** | **0.5** |
| `suggested_structure` | iron fly / short straddle centred **772.82**, wings ≈ ±0.82% | iron fly / short straddle centred **720.95**, wings ≈ ±1.42% |
| `stand_aside_reason` / `caution` | none | none |
| `mean_pnl_open_pct` (GROSS) | +0.227% | +0.360% |
| **`mean_pnl_open_net_pct`** | **+0.127%** | **+0.260%** |
| `premium_sell_win_open_pct` | 88.3% | 85.0% |
| `worst_day_open_pct` | −1.4% | **−2.453%** |

`backtest.verdict` = **GO_PREMIUM_SELL_INTRADAY** on n=60 for both. **`pnl_basis`: percent-of-underlying-spot-notional, GROSS of transaction costs — NOT premium-collected and NOT margin-relative.** So "+0.227%" is tiny in absolute terms; the net figure (gross minus the assumed 0.1% round-trip half-spread + fees) is the one to lead with.

⚠ **The material finding, which the unconditional verdict hides: conditioned on the VIX state we are actually in, this lane has no net edge today.**

| `mean_pnl_by_vix_state` | LOW ← **we are here** | MID | HIGH |
|---|---|---|---|
| SPY | **−0.019%** | +0.388% | +0.312% |
| QQQ | **+0.043%** | +0.547% | +0.491% |

VIX 15.46 puts both indices in the **LOW** bucket, where gross expectancy is **−0.019% (SPY)** and **+0.043% (QQQ)**. Net of the 0.1% cost assumption both are **negative** (SPY ≈ −0.119%, QQQ ≈ −0.057%). The edge in this strategy lives in the **MID and HIGH** VIX terciles (bounds 16.4 / 17.9), not the low one — which is exactly why `size_scalar` is 0.5 and why the skill's own guidance says *"skip when VIX low (thin edge)."* **On today's conditional numbers it is worse than thin: it is negative after costs. Stand aside rather than size it.**

Other mechanics for completeness: **GEX vol-suppression is confirmed** (`gex_to_range_corr` −0.38 SPY / −0.37 QQQ; long-gamma mean range 0.82% vs short-gamma 1.24% on SPY, 1.42% vs 2.03% on QQQ) — long-gamma → tighter wings, short-gamma → wings out or stand aside. **Entry: at/after the open once the overnight gap resolves; hold to the close; never carry overnight** — overnight entry is +0.024% on SPY and **−0.083% on QQQ**, i.e. the gap erases the edge. **SPY ≈ SPX** (validated identical); **QQQ is the weaker read** (Nasdaq index book unavailable). **Direction: none — delta-neutral. Do not add a tilt.**

**Tension to state explicitly:** this front-expiry lane says "sell premium" while the **30d QQQ VRP says PREMIUM_BUYING** (IV 20.43% vs realised 25.46%). Different horizons — do not let the 0DTE lane imply a 30-day short-vol view on Nasdaq.

**Promotion bar (P1.8):** this lane stays advisory / 0 rubric points **permanently** until BOTH a vol-shock day enters the sample (the short-vol left tail is currently **UNSAMPLED**) AND **net** expectancy clears a tail-aware bar. Win-rate is explicitly **not** the promotion metric for a negatively-skewed short-vol strategy — an 88.3% win rate alongside a −1.4% worst day is precisely the shape that misleads. **CPI is Wednesday.**

---

## 2b. Swing Dealer Positioning (1–4 weeks)

**The scored +1 dealer-positioning line fires nowhere today.** `dealer-positioning-strategist` screened 23 symbols and fully verified 11 with `scripts/dex_flip.py` (11 dated `dex` calls each, 2026-08-10 back to 07-27).

**Zero symbols qualify for the mechanized DEX flip.** Two near-misses, both **magnitude-floor failures — a level, not a flip:**

- **SMH**, `magnitude_ratio` **0.50**: `net_dex 2026-08-07 +2,933,350,692 → 2026-08-10 −502,649,817; prior 4 sessions all positive; |flip| 502,649,817 vs floor 1,013,788,285 (0.25× trailing-10 median 4,055,153,142)`.
- **LITE**, `magnitude_ratio` **0.29**: `net_dex 2026-08-07 +1,611,460,418 → 2026-08-10 −62,841,732; prior 6 sessions all positive; |flip| 62,841,732 vs floor 215,265,950`. **LITE reports tomorrow** — this is event-driven, not a dealer story.

Both are **watch items for 08-11**, not signals today.

**Zero valid vanna squeezes — the dated VIX leg fails outright.** `^VIX` (raw Yahoo chart API): 08-04 16.50 → 08-05 15.81 → 08-06 15.15 → 08-07 14.90 → **08-10 15.46 (+3.76%)**. VIX fell three straight sessions into Friday but **rose today**, breaking the falling-VIX requirement as of the most recent session. This invalidates every put-heavy book regardless of composition — and only MU (net_vanna +332) and SNDK (+838) screen put-heavy at all, both negligible.

**GLD** carries `whipsaw_warning = TRUE` (4 sign changes in the window); it flipped bullish on 08-05 and sustained, so it is not a today-flip. **USO** likewise flipped 08-06 and held.

**Front-end IV ratios (`--near-dte 7`, never the default 1):** **COHR 1.727** · **LITE 1.575** · **SNDK 1.289** · USO 1.219 · CRWD 1.168 · GLD 1.163 · NOW 1.131 · PANW 1.126 · MRVL 1.088 · MSFT 0.995 FLAT. **Indices are all CONTANGO — SPY 0.743 / QQQ 0.905 / IWM 0.828 — so there is no index-level panic.**

**Every symbol screened came back `swing_bias: NEUTRAL, confidence: LOW.`** `regime_flip_detected` is technically true for most names, but nearly all are 2–5 flips in 8–10 sessions — noise, not positioning, and not elevated to a thesis.

---

## 2c. Sector Rotation

**Rotation regime call: `no_change`, confidence LOW.** Today's tidy cross-confirmation does **not** clear the ≥3-day persistence bar.

**The direction rule (C55):** `sector_flow_persistence` and `sector_flow` are **one gross-turnover source**, sign-agnostic — today they returned `trend: INFLOW` with `persistence_score: 1.0` for **all 11 sectors**, i.e. literally zero discrimination. Direction reads off the **netted** `market_regime.sector_rotation` only.

| Sector | Netted | Gross | Agreement | Price 1d / 5d | Verdict |
|---|---|---|---|---|---|
| Financial Services | **+$37.4M IN** | +$288.3M IN | agree | +0.36 / — | watch_only — 1st netted appearance in 5 sessions |
| Healthcare | **+$26.3M IN** | +$178.4M IN | agree | +1.67 / +3.82 | watch_only — flipped from OUT (08-07) today |
| Energy | **+$20.4M IN** | +$109.3M IN | agree | **+4.66** / +2.36 | watch_only — 1st appearance, strongest supporting thread |
| **Technology** | **−$279.9M OUT** | **+$3.68B IN** | **disagree** | −0.88 / +4.65 | watch_only — contradictory **and** non-persistent |
| Comm Services | −$26.7M OUT | +$646.1M IN | disagree | +0.52 / — | watch_only |
| Utilities | −$24.7M OUT | +$57.7M IN | disagree | −1.10 / −2.77 | watch_only (netted + price agree bearish; gross blocks) |
| Industrials / Cons Cyc / Materials / Cons Def / Real Estate | no netted read | all IN | n/a | — | no call |

**Two substrate findings worth registering.** First, **`market_regime.sector_rotation` is a top-3/bottom-3 truncation, not full-11 netted data** — every day returns exactly 3 IN and 3 OUT of 11, so **"not listed" ≠ "flat"**, only "not extreme enough that day." Second, back-filling the netted source across 08-04→08-10 shows **Technology whipsaws IN / OUT / IN / IN / OUT** (+839.2M, −65.3M, +620.3M, +110.4M, −279.9M) — **three sign changes in four sessions**, a persistence of 2-of-5 = **0.40**. ⇒ **Do not let today's single netted-OUT print drive a short or fade thesis on megacap tech.** Healthcare's IN is a 1-day flip out of a mildly-OUT stretch; Financial Services and Energy have no prior read at all.

**Single-name leader +1 conditional — exactly one name clears all three conditions:** **COIN** (persistence 1.0 ≥0.6 ✓ trivially · `cum_flow_30d` **+$62.2M** aligned ✓ · ≥$50M ✓). Everything else fails **purely on the $50M size condition** — XOM +$30.9M, LLY +$32.6M, CVX +$2.16M, NE +$1.55M, RIG +$0.62M, WHD +$0.24M, RDNT +$0.09M — or on sign (BRK-B −$3.7M, ALLY −$0.24M). Condition (a) is doing no work, since all 11 sectors read 1.0.

**ETF flow tape (advisory — strengthens the conditional +1, adds no rubric points).** 21/21 ranked clean, top-3 each side deep-pulled.

| ETF | Net premium dir (5d) | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| **XOP** | inflow +$19.46M | BULLISH-consistent | $59.9M, 12/20 below-mid | mild bull-tilt, but $9.66M no-side long-dated puts dominate | **agree** (Energy IN) | XOM, CVX, VLO, RIG, NE, WHD |
| **EWY** | inflow +$16.84M | BULLISH-consistent | $135.2M, 14/20 below-mid | bull-tilt, $41.9M no-side block dominates | n/a (Korea) | — |
| **XLI** | inflow +$15.86M | BULLISH label, MIXED strength | $22.7M, 12/20 below-mid | **bear-tilt today** | **disagree** (price red, sweeps bearish) | SPCX, LMT, POWL, VRT, AXON |
| KRE | inflow +$8.87M | BULLISH-consistent | — | — | **agree** (FinServ IN) | — |
| **GDX** | **outflow −$55.18M** (largest) | BEARISH-consistent | $107.2M, balanced 9/9 | flips bull today — inconsistent | n/a | — |
| XLP | outflow −$8.53M | BEARISH-consistent | $27.0M | negligible (n=2) | n/a | — |
| XLE | outflow −$2.48M | **treat as flat** | $96.8M, **12/20 above-mid** | **bull-tilt**, +2.8% intraday | agree | XOM, CVX, RIG, NE |

Three findings worth calling out. **XLE's "outflow" is noise, not signal** — −$2.48M is under 4% of $67M gross turnover; sweeps, DP and price all lean bullish. **XOP is the cleaner Energy read.** **GDX is the tape's single largest 5d outflow (−$55M) while gold/silver miners are up 20%+ on the week** — that matches the hedging/overwrite reading on GFI/AG/HL rather than distribution; **do not short miners off that number.** And **Financial Services strength is concentrated in regionals (KRE) plus fintech, not megacap financials** — broad XLF is flat-to-negative over 5d.

**Confirmation trigger:** Financial Services and/or Energy printing netted-IN again on **both 08-11 and 08-12** with Technology holding OUT graduates this to a live growth→value call. CPI Wednesday is the wildcard — a hot core print plausibly extends the value/defensive/energy bid; a soft one could flip Tech straight back to IN, as it already has twice this week.

---

## 3. Swing Setups (1–6 weeks)

**Empty. Zero sized positions.** No name survived the gate stack. This is the correct output, not a failure — see §6.

### 3a. Long swings (regime-aligned)

**None sized.** One name reached the section and was gated out of it:

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **MSFT** | **6 (LOW)** | Genuine dispersed institutional accumulation in the cleanest single-name expression of the software-bid / semis-sold split, with call OI building across 11–39 DTE and a defined-risk Oct16 vertical on top. Fundamentals confirm the hard legs (4/4 beats, rev +17.79% / EPS +31.56% YoY, ROE 33.22%, D/E 0.24). | Oct16 510C/550C debit vertical (**preferred over** `batch-scan`'s "Aggressive Long Calls" — multileg saw the actual coordinated flow and the vertical is defined-risk) | **Close below the 505.14 DP shelf** (institutional band 505.14–510.23, heaviest genuine clip **508.38**). The $506.06 level is excluded — it is closing-cross convergence, $1.2B across 100 trades. | **`watch_only`** — −3 tiers |

**Why MSFT is not sized.** Three independent cuts, any one of which floors `starter`: **fundamentals CAUTION** (insider MSPR −83.89 across **six consecutive negative months**, against a dark-pool *accumulation* long thesis); **event risk** (CPI at T+2, inside the band, with OPEX T+9 and core PCE T+14 inside the 67-DTE Oct16 horizon — its own earnings at 2026-10-27 fall *after* that expiry, so the event risk here is purely macro); and the **debate gate** (bear 0.65 ≥ bull 0.35). On top of that its +3 conjunction fails the quant's own pre-registered **C11(c) 5%-of-gross floor** — the +$727.8M net is only **4.41%** of MSFT's own $16.5B 30d gross premium (90d worse at 2.8%), a small residual on enormous two-way churn.

⚠ **Distribution caution (C28, advisory, 0 points, no sizing effect):** deep-ITM 480C (25DTE, $480 vs $506 spot) OI fell **2179→852 on volume 1761** (~$3.83M closed), plus an ATM 510C close (−525 OI). Read as profit-taking on a name up big — but it mechanically zeroed the separate +1 cum-flow line, and it corroborates the insider-selling backdrop.

The bear's unrefuted point deserves recording because it is the sharpest evidence critique of the day: the "$523.5M dispersed buying" is **49% one print** (500,000sh / $254.2M), the surviving footprint is only **~6.5% of MSFT's own $4.168B dark-pool tape**, the call-OI build is **0.18% of total OI** at $0.44–$5.60 average prices — indistinguishable from overwrite supply being lifted, per the same per-leg-NBBO-tag argument `multileg-strategist` proved on GLD today — and **`oi_smart_positioning` never measured MSFT at all**, so one of the three conjunction legs behind the +3 is not a weak measurement but an *absent* one.

**Other longs considered and killed** (§7 has the full score audit): **GLD −3** (passed the confluence gate on 2 agents but took the full flow_conflict deduction — see below) · **COIN 2, VETO'd** · **NOW 1** (the only fundamentals CONFIRM and the only clean BULLISH 30d flow label of the day, but the accumulation evidence is 5-of-6 closing-cross prints leaving ONE genuine $17.9M trade, and its largest OI build is a **67dte protective PUT at $9.39** against 4dte calls at $1.90–$3.75) · **PLTR 1** (the load-bearing Dec 175C build was retracted by two independent tools; 90d flow −$48.0M; `market_excess` −0.1000) · **SPCX −1** (self-conflicted).

**GLD deserves a sentence beyond its score,** since it was one of only two names to clear the ≥2-agent confluence gate. `cum_flow_30d` is **−$290.2M against a long thesis — 3.06× the union median $94.85M**, with 90d agreeing at −$291.7M, so the −3 fires mechanically and was not narrated away (2026-05-15 P0 exists precisely because it was, once). Independently: the structure the desk would be buying is a **2:1 front-ratio spread whose risk cap is unconfirmed** (no visible capping wing), the vol surface is **correctly priced** (VRP +0.0192 FAIR), and the only leg that repeats *verbatim* across sessions is the **hedge** — the Nov20 470C collar at $18.4M on 08-07 and $21.0M today. When the hedge is what repeats, the program is managing an existing position, not expressing conviction. The deep-dive OI confirms it: the dominant build is a **Nov20 four-legged fence with puts (335/345, +86,883 contracts) building slightly more than calls (460/470, +81,888)**. Uncapped short gamma into CPI at T+2 is the wrong trade at any score.

Also resolved: the apparent "aggressive GLD call buying vs −$63.2M net premium" contradiction is **not** a contradiction. The 445C's "110,654 ask vs 112 bid" is a **per-leg NBBO tag**, not a package-level signal — in a multi-leg execution both legs can print as ask-side crosses — and the negative aggregate is exactly what a **2× short leg collecting more premium than the 1× long leg costs** produces.

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only` (2026-08-01 P0 #1).** The section still carries the theses; nothing is sized. This is **routing, not suppression** — the calls are scored and serialized so the counterfactual keeps resolving.

| Ticker | Score | Thesis | Invalidation | Sizing |
|---|---|---|---|---|
| **INTC** | 1 (DROP) | `bearish_flow` on the cleanest large aligned directional flow of the day: `cum_flow_30d` **−$858.7M, label BEARISH** (−6.98% of gross); **96.1% ask-side on the 67.5P**, sweep ratio 44.2, size/OI **13.5**; the driver is a **$15B dilutive equity offering**. Clean-protocol WR **0.5714 on n=133** with `market_excess` **+0.0752** — **the only positive-excess class in the run.** | n/a — not sized | **`watch_only`** (short routing) |

Counterweights on the record: INTC is **4-of-4 EPS beats** with **rev +7.47% YoY**, insider is **neutral** (−1.48), it is **+7.16% on the 5d** so today was one red session in an up week, DEX is **+$1.4B positive with no qualifying flip**, and a large part of −4.06% is sector beta. `fundamentals-gate` returned **CAUTION** — a short here is short a *financing print*, which is the weakest kind of short. The 67.5P is ~31% OTM at 39 DTE, i.e. tail convexity rather than a base case. Note also that a positive-excess *class* is not a positive-excess *call*.

`contrarian-scanner` returned an **empty board by design.** Only three names cleared ±2σ crowding — **AG (z=8.695)**, **HL (z=19.167)**, **NVDA (z=2.049)** — and all three were rejected: AG/HL on **BACKWARDATION plus `is_this_actually_a_hedge_not_a_short = TRUE`** (heavy put buying while spot is +12–20% on the week is protective; AG's 270115P00010000 OI fell **−31,009**, i.e. puts being *closed*), and NVDA on the **QQQ-complex VRP abort** (PREMIUM_BUYING −0.0503 means shorting Nasdaq premium fights the regime) plus backwardation. DAVE (5d −22.63%), HONA (−21.69%) and TTD (−26.83%) were rejected as **late/chasing, not crowded**. ⚠ **Substrate limit:** `pc-ratio-zscore` has **no `--date` flag**, so the −2 rubric line's "rising z" clause is **unsatisfiable** — reported as such rather than fabricated.

### Sweeps (informational — 0 rubric points)

Persistence-ranked, and the ranking is doing real work today because several persistence labels **contradict** the live tape.

| Ticker | Side | Read | Persistence | Price 1d | Note |
|---|---|---|---|---|---|
| **MSFT** | call | **bullish — cleanest on the board** | 5/5 bullish | +1.21% | 89.2% ask-side on 261016C550 (ratio 9.24); 39dte 545C OI +7,476; cum-flow aligned +8.5% skew |
| MU | put | bearish, price-confirmed | 5/5 bearish | −1.89% | ⚠ **underlying OI evidence ruled an artifact** — see below |
| AMD | put | bearish, price-confirmed | 5/5 bearish | −2.86% | ⚠ same artifact ruling |
| **GLD** | call | **bullish — contradicts its own 3/5 "bearish" label** | 3/5 bearish | +1.02% | Resolved as the long leg of a ratio spread, not naked buying |
| **SPCX** | mixed | **reject the bearish framing** | 5/5 bearish | — | +$14.8M net premium today and a 4dte call OI build +76,283. Net-window direction ≠ per-day confirmation |
| INTC | put | bearish lean today | 5/5 mixed | −4.06% | 96.1% ask-side 67.5P, ratio 44.2 |
| NVDA | mixed | **genuinely conflicted, watch-only** | 5/5 mixed | −2.86% | Mixed sweeps, cum-flow net **bullish**, but a 67dte 220P build **+30,028** |
| SPY / QQQ / GOOGL / AAPL / AMZN / META / TSLA | mixed | **hedge flow, demoted** | 3–5/5 | — | Margins are noise: QQQ **0.2%**, GOOGL **0.05%**, AAPL 0.4%, AMZN 0.7%, SPY 1.5% |

**Artifacts rejected.** **SPX/SPXW synchronized multi-strike bursts** at identical timestamps (19:57:05Z, 18:33:39Z) across 6000C/7000C/8000C, 2026–2031 expiries, deltas 0.74–0.99 = **stock-replacement / convexity ladders**, not momentum — confirmed independently in both `top_premium_trades` and `greek_screener`. **MU's 4dte 105P (+23,158) and AMD's 4dte 70P (+9,500) are un-split-adjusted strike-grid artifacts** — 85–88% OTM against $861 and $469.56 spots, far too deep to function as a 4-day CPI hedge (which would sit 3–7% OTM), and absent from `hot-chains multileg` across four checked sessions. **The bearish sweep read on MU/AMD therefore rests on OI evidence that is not real**, even though the price weakness is. **SNDK's $289M 2027-01-15 1660P is `side: no_side`** — unclassifiable; a possible pairing with a $132M bid-side 1020C executes **4.5 hours apart**, arguing two independent tickets rather than one package. **Do not size off it.**

---

## 4. LEAP Builds (6–24 months)

**Empty. Zero names reached 6-of-9 gates.** LEAP share of DTE volume is **3.9%** — the thinnest bucket — so an empty book is the expected outcome, and it is reported rather than filled.

`oi biggest-increases --min-dte 180` top-20 is dominated by non-funnel names (MSTR, TLT, WBD, CSGP, MARA, CPRT, GRAB, WOLF, SPX, DRAM, EWZ, GDX), all disqualified on funnel non-membership. **Only two funnel hits — AG and HL — and both are PUTS.**

| Ticker | Detail | Gates | Disqualification |
|---|---|---|---|
| **AG** | AG280121P00010000, 529dte, **put, sold-to-bid** (bid 7,863 ≫ ask 4,066), OI +11,748 | **0/9** | `cum_flow_90d` **+$3.29M on ~$477M gross = 0.7%** (noise); institutional-accumulation **DISTRIBUTION** (0.55); conviction-matrix **DIRECTIONAL_SHORT**. Put-sale-netting blind spot triggered |
| **HL** | HL280121P00010000, 529dte, put bought-at-ask, OI +5,295 | **1/9** | conviction-matrix **HEDGED_LONG → auto-reject**; `cum_flow_90d` **−$6.75M** on ~$277M gross |
| **TTD** | TTD281215P00030000, 858dte, put bought-at-ask, OI +528 | 0–1/9 | `cum_flow_90d` **BEARISH −$38.5M**; conviction-matrix **COVERED_CALL → auto-reject**. Independently confirms the falling-knife ruling |
| **MSFT** | Checked specifically given its board-leading flow | **1/9** | **Every top daily OI-build contract is 4–70 DTE**; zero >180 DTE contracts in the build leaders on 08-10 or 08-07; absent entirely from `--min-dte 180` top-20 ⇒ **no fresh LEAP position exists.** `cum_flow_90d` +$771.8M is only **2.8% of gross** (two-way churn). Matrix DIRECTIONAL_LONG at **confidence 12.3%**, far below >70. **MSFT's conviction is structurally swing-horizon (11–70 DTE), not LEAP** |
| **PLTR** | Checked given the 130dte 175C +49,736 build | **0/9** | The real build sits at **130 DTE, outside this lane**; the full >180DTE chain's max single-contract oi_diff is just **648**. Matrix MIXED |
| **CRWD** | — | ≤1/9 | Largest >180DTE build only 299 contracts; matrix MIXED |

Blind-spot checks run and documented: put-sale netting / net-as-%-of-gross (AG, HL, MSFT, TTD), long-dated-put-is-not-a-bullish-build (AG, HL, TTD, cross-referenced against the Step-0 single-leg put list — MSFT 680P 858dte, NVDA 450P 858dte, ADBE 450P 529dte, NET 440P 529dte, LITE 1110P 676dte, META 600P 403dte, MSTR 300P 858dte), merger-arb/tender (none found), dividend-capture (not triggered), and strike-vs-spot plausibility (AG $10P vs $18.88 and HL $10P vs $17.55 are plausible deep-OTM, not stale grid).

---

## 5. Volatility Surface

**Substrate hygiene applied throughout** via `scripts/term_structure_hygiene.py` (`min_contracts=15`, `near_dte=7`) — the raw `iv-term-structure` label is not trusted. ⚠ **`iv-percentile-zscore` returned `dates_used: 83` on every ticker against a 252-day request, so every percentile below is PROVISIONAL.**

**The buried lede of the day, and the discrimination that matters:** a dense earnings cluster lands **08-11 → 08-13, concentrated in exactly the complex that sold off.** `earnings_catalyst`'s `next_earnings_date` field is populated **230/230** (an earlier draft of my own Step 0 context wrongly reported it null — an extraction error on my part, caught by `earnings-scout` and corrected mid-run before the last three agents spawned; it materially changed the read on LITE/COHR/CRWV/SMCI from "distribution" to "pre-earnings de-risking").

| Ticker | Print | Time | IV rank | Implied move | Today 1d% |
|---|---|---|---|---|---|
| SE | 08-11 | premarket | 78.7 | 11% | +1.21 |
| CAH | 08-11 | premarket | 81.3 | 6% | — |
| CAVA | 08-11 | postmarket | 85.9 | 11% | — |
| SMCI | 08-11 | postmarket | 72.1 | 12% | — |
| **LITE** | **08-11** | postmarket | 64.8 | **10%** | **−8.61** |
| **CRWV** | **08-11** | postmarket | 52.8 | **11%** | **−2.74** |
| CSCO | 08-12 (CPI day) | postmarket | 90.6 | 7% | — |
| **COHR** | **08-12** (CPI day) | postmarket | 73.6 | **10%** | **−14.24** |
| BIRK / GDS | 08-13 | premarket | 100 / 83.1 | 10% / 12% | +3.30 / — |
| HD / KEYS / BHP | 08-18 | — | 86.7 / 81.6 / 75.5 | 2.3% / 9% / 5% | — |
| TJX / LOW | 08-19 | premarket | 90.4 / 86.4 | 2.4% / 2.6% | — |
| ROST / DE / AAP | 08-20 | — | 94.9 / 82.3 / 80.5 | 2.2% / 2.4% / 4% | — |

⇒ **A large part of today's semis/optics selloff is pre-earnings de-risking ahead of that cluster, stacked on CPI Wednesday** — a materially better explanation than "the AI trade is breaking," and consistent with the 5d column being green across the complex. **NVDA, MU, AMD, MRVL, AVGO, TSM, INTC, ASML, FSLR, SNDK, MSFT, ORCL, NOW, PANW, CRWD are all absent from the ≤14-day screen**, so their weakness is *not* earnings-driven and any backwardation there is not event-explained.

### Genuine dislocations (NOT event-explained)

**SNDK — the highest-conviction dislocation on the board, BUY VOL.** `raw_shape` = `shape` = `base_shape` = **BACKWARDATION** (no flip, no kink; smooth monotone decay 121%@4dte → 94–98% back months). `front_end_ratio` **1.289**. **VRP −0.5966 — iv30d 91.5% vs realised 151.2%, the widest gap screened.** term-skew COMPLACENT (0.988), `iv_percentile` 2.41 LOW_IV (provisional, n=83). **No earnings inside 14 days.** `implied_move` 12.7%. Structure: **long calendar / long back-month straddle** — buy Sep (32dte, 93.8% IV) against trailing realised 151%; **do not sell the front, it is still cheap versus realised even at 121%.** Deliberately based on the **vol** read, not the flow read — SNDK is the live put-sale-netting name (on 2026-08-06 one bid-side deep-ITM put sale was 74% of its net), and VRP/term-skew are clean of that contamination. **Scored 1 → DROP; final `skip`** (panic gate 1.289 > 1.10, drop floor binds).

**USO — real but modest, macro-diluted.** raw BACKWARDATION → **KINKED** → `base_shape` **CONTANGO** (both flipped — a contango base *with* a front kink; neither label alone describes it). Genuine qualifying kink at 4dte (08-14), **prominence 19.8% on 5,992 contracts** (liquid). `front_end_ratio` 1.219. **VRP −0.1066.** ⚠ **`macro_floor_adjusted: YES`** — the 4dte kink coincides with the shared CPI/EIA Wednesday cluster, so the name-specific claim is diluted. Structure: calendar, sell the 08-14/08-21 front against a 09-11/09-18 long leg. **Scored 1 → `skip`** — and note the risk officer's ruling that this calendar is **short an undefined amount of premium into a named binary**, which is not "playing the event."

**MRVL — watch only, no trade.** KINKED with a genuine backwardation base, but kink 18dte prominence **6.1%** (barely clears the 5% floor) and `front_end_ratio` **1.088** — the thinnest screened, and the closest near-miss to the 1.10 panic bar. **No VRP figure was measured**, so the +1 line's mandatory "VRP-aligned bias" clause is **unverified rather than merely weak** — the quant withheld the point on that basis, which is the right call. Scored **0**.

**GLD — not a dislocation.** KINKED (kink 39dte, only 6.7%), `base_shape` **FLAT**, `front_end_ratio` 1.163, `iv_percentile` 84.34 HIGH_IV — **but VRP +0.0192 FAIR** (realised 23.4% vs implied 25.3%). The elevated percentile is a real gold-vol regime, **correctly priced**. No surface edge.

### Event-explained backwardation — correctly priced, do NOT fade these levels

| Ticker | shape / base | `front_end_ratio` | kink | term-skew | VRP | Catalyst |
|---|---|---|---|---|---|---|
| LITE | BACKW / BACKW | 1.575 | none | COMPLACENT 1.004 | −0.1648 PREMIUM_BUYING | 08-11 post |
| COHR | BACKW / BACKW | **1.727** | none | COMPLACENT 0.943 | −0.2169 PREMIUM_BUYING | 08-12 post, CPI day |
| CRWV | BACKW / BACKW | **1.797** | none | COMPLACENT 0.98 | −0.2817 PREMIUM_BUYING | 08-11 post |
| SE | BACKW / BACKW | **2.238** | none | ~flat 1.007 | **+0.2516 PREMIUM_SELLING** | 08-11 pre |
| BIRK | BACKW / BACKW | 1.354 | none | **TAIL_HEDGING 1.147** | **+0.3139 PREMIUM_SELLING** | 08-13 pre |

None is a level mispricing — the front is elevated because a real binary sits 1–3 days out, and hygiene did not flip any of them (`flipped=false` throughout). The VRP pattern is the expected pre-earnings shape (LITE/COHR/CRWV cheap versus already-elevated realised; SE/BIRK rich versus realised, with BIRK carrying genuine put-side tail hedging). **The exploitable structure here is the post-event crush, not the level** — sell the 08-14 weekly the morning after each print against a September long leg. That is a **next-session** decision, not today's, and it is flagged for tomorrow rather than sized now.

### Earnings vol plays

**HD — SELL VOL, the only clean company-specific vol signal in the entire scan.** Earnings **08-18 premarket** (8 DTE). raw BACKWARDATION → **shape KINKED**, `base_shape` **CONTANGO**, `flipped=true`. **`kink_dte` 11 (08-21 expiry — the tenor containing the print), `kink_prominence_pct` 27.4 on a 1,306-contract tenor** — the only genuine kink at an own-earnings tenor anywhere in the scan (neighbours: 08-14 IV 40.7%, 08-28 IV 37.1%, versus the kink tenor's **51.9%**). Back-month 102dte = **TAIL_HEDGING 1.125**, so the tail is priced alongside the kink. `implied_move` **2.33%**.
**Macro-vs-company attribution done explicitly:** the 08-14 tenor (IV 40.7%) is the shared CPI/PPI/Retail-Sales macro floor; the 08-21 kink sits **above** it, so the marginal excess is HD-specific. The `front_end_ratio` of 1.259 is dominated by the **macro** leg — do not gate on that number alone.
**Do not enter today.** CPI Wednesday and PPI Thursday both sit inside the tenor before HD even reports; better entry is **Thu 08-13 / Fri 08-14** once the macro leg resolves. Structure: short strangle / iron condor on the **08-21** expiry, shorts around ±2.3%. **Scored 1 → `skip`** (panic gate 1.259 > 1.10 fired without exception; drop floor binds).

**LOW — SELL VOL, secondary only.** 08-19 premarket. KINKED, kink 11dte but prominence only **9.9% on 250 contracts**; `front_end_ratio` 1.070; back-month **NORMAL 1.058 — tail NOT confirmed**. `implied_move` 2.60%. Better run as a calendar (long 08-14 / short 08-21) than a naked short. **Scored 1 → `skip`**; also −1 tier as the non-kept member of the {HD, LOW} correlation cluster.

**The entire 08-11 → 08-13 cluster is a SKIP as a vol trade.** SE (2.238), CAH (2.138), CSCO (2.057), CAVA (2.029), BIRK (1.354) all show **`kink_dte: None`**, because each print falls inside the *same* nearest tenor (08-14) that must also price CPI + PPI + Retail Sales. **There is no lower-DTE macro-only tenor to net against, so macro and company premium are inseparable.** Loud front-end ratios there are the expected signature of an imminent binary in a macro week, not a mispricing. Note CAH/CAVA/SMCI/CSCO/GDS are additionally **sub-C12** (under $50M ADV) and cannot be sized regardless.

**TJX** shows a front (4dte) IV of **107%** against 11dte 38% — a 2.8× gap on a 318-contract tenor, far beyond anything else screened; it reads as a strike-average artifact (thin far-OTM strikes skewing the bucket mean), and there is no kink at its own earnings tenor, so nothing is tradeable. **ROST**'s 1.578 front elevation with no kink is pure macro hedging (Retail Sales is a direct read-through). **BIRK** is disqualified on liquidity — only two tenors clear the 15-contract floor.

**IV outliers: the lane is EMPTY.** 19 of 20 cached rows sit on the **08-10 (today, 0DTE)** expiry — pure decay noise (INTC calls showing `avg_iv` 12–15% against `max_iv` 210–292% on under 600 contracts). Exactly the contamination the hygiene rule exists to drop.

**Calendar candidates from the expiry heatmap** (market-wide, not per-name): premium concentrates at **09-18 monthly $5.79B** and **08-14 weekly $2.97B** — consistent with the earnings cluster settling at 08-14 plus CPI hedging, with September the first clean monthly past both. This corroborates USO's front-vs-September calendar rather than adding a new name.

⚠ **`analyst-vs-flow` returned no analyst-comparison field on any name today** — the divergence lane, normally the highest-EV earnings setup, was unassessable. Substrate gap.

---

## 6. Risk & Correlation

**Macro headline:** stagflationary composition — core PCE **3.29%** sticky, payrolls **−23k**, 10Y **4.65% rising**, USD weakening — punishing duration, rewarding real assets. **Forward event risk is dominated by CPI at T+2 (Wed 08-12)**, with PPI T+3, Retail Sales T+4, OPEX T+9, core PCE T+14 and FOMC T+25. **Every structure considered today sits inside the ≤T+3 band.** Counting convention for the audit: T+0 = 2026-08-10, **trading days**.

**Breadth cross-check (`fz`, advisory, 0 points):** advancers **230** / decliners **270**, `pct_green` **45.73%**, avg change +0.01%, median **−0.17%**. Top mover DDOG +11.48%, worst COHR −14.24%. `pct_green < 50` on a roughly flat SPY would normally read as a distribution tell — **but it is not one here**, and the reason is in §1: RSP was **green** and the decliners are concentrated in semis/AI-power plus rate-sensitives (XLU/XLRE, consistent with 10Y +9bp). **This is churn inside a rotation, not distribution.** Advisory; it does not change sizing.

### Correlation clusters (`uw risk portfolio-correlation` on today's candidates, not the static watchlist)

**`semis_memory_cluster` = {INTC, MRVL, SNDK}** — INTC/MRVL **0.936**, SNDK/MRVL **0.870**, INTC/SNDK **0.848**. Kept member **SNDK** (tiebreak on |cum_flow| in direction: −$130.6M vs INTC's −$31.6M); **INTC and MRVL take −1 tier**.
**`bigbox_retail_cluster` = {HD, LOW}** — HD/LOW **0.930**. Kept member **HD** (kink 27.4% on 1,306 contracts vs LOW's 9.9% on 250); **LOW takes −1 tier**. **This pair is ONE short-vol retail position, not two**, and Retail Sales Fri 08-14 is a direct read-through landing before both prints.

**The cluster that does NOT exist, stated because it is counterintuitive:** **MSFT / NOW / PLTR return `high_correlations: null`** even on an isolated 3-symbol probe — all three pairwise coefficients sit below the tool's ~0.53 reporting floor. On 30-day realised data these mega/large-cap software names are **not** the same bet, which is precisely what today's tape would predict (software bid, semis sold). **No cluster penalty on MSFT, NOW or PLTR.** **GLD/USO is likewise unreported** — gold and oil are not one commodity bet this window. The only sub-0.70 pairs returned are **negative** (USO/HD −0.699, USO/LOW −0.658, NOW/SNDK −0.531), and negative correlation is the opposite bet, not the same one — recorded, not deducted, and not upgraded.
⚠ **Substrate caveat:** `sector_breakdown` returned `{"Unknown": 12}` and the accompanying "100% concentration" warning is a **null-sector artifact**, not a real concentration read. Ignore it; the pairwise coefficients are the usable output.

### Gates applied

**Regime:** TRANSITIONAL on an UPTREND trend — no directional conflict for longs; **−1 tier on INTC** (UPTREND vs a SHORT direction).
**VRP:** no contradiction fired. QQQ PREMIUM_BUYING **favours** MSFT's long-premium vertical and SNDK/USO/MRVL's long-vol structures (no size-up granted — gates only cut). HD/LOW were evaluated rather than skipped: SPY VRP is negative in sign (−0.0016) which would contradict a short-vol structure, but at 0.16 vol-bp and classified **FAIR** no contradiction is established, and QQQ's read does not govern consumer-discretionary names.
**Panic (`front-end-iv-ratio` > 1.10), no exceptions:** fired **−1 tier** on **NOW (1.131)**, **SNDK (1.289)**, **USO (1.219)**, **GLD (1.163)** and **HD (1.259)** — the last despite `earnings-scout`'s correct observation that HD's ratio is macro-dominated; the override has no exceptions. **MRVL at 1.088 is the closest near-miss.** **MSFT at 0.995 is FLAT** — no panic. Indices all contango.
**Sector:** **fires nowhere**, and the arithmetic is on the record rather than discretionary. Technology is netted-OUT (−$279.9M) and MSFT/NOW/PLTR/MRVL all sit in it — but Technology's netted persistence is **2-of-5 = 0.40 < 0.60**. The *gross* `persistence_score` of 1.0 was **rejected as an input**: it reads 1.0 for all 11 sectors, so using it as the persistence of a *netted* direction is a category error (C55) that would fire this gate on every candidate every day — the "gate that taxes everything equally is a haircut, not a filter" failure. The adverse fact is surfaced as narrative headwind instead.
**Fundamentals:** **−1 tier** on MSFT, INTC, PLTR (CAUTION); **VETO → watch-only** on COIN; **no-op** on NOW (CONFIRM).
**Event risk:** **−1 tier on every candidate** — CPI at T+2 is inside every horizon. HD and LOW's *own* earnings (08-18 / 08-19) are exempt as the event being played, but CPI and PPI are **not** the event those trades play and sit inside the short tenor undefined-risk. MSFT's own earnings (2026-10-27) fall **after** its Oct16 expiry, so its event risk is purely macro.
**Debate:** **fired on all 5 debated names** (see below).
**`rubric_regime`:** **OUT-OF-REGIME** — rubric frozen `2026-06-12`, fitted in the UPTREND that ended then, current regime TRANSITIONAL ⇒ **all conviction-tier sizing capped at half.** The HIGH/MEDIUM bands are structurally empty again, so the freeze-lift remains unrunnable.

### Fundamentals verdicts (top-5, with the contradicting facts)

| Ticker | Verdict | The contradicting fact |
|---|---|---|
| **MSFT** | **CAUTION −1** | **Insider MSPR −83.89 across six consecutive negative months** (Mar −98.6, Apr −100, May −100, Jun −51.7, Jul −100, Aug −100) against a dark-pool *accumulation* long thesis. Beat_streak 4/4 and rev +17.79% / EPS +31.56% are genuinely strong — the contradiction is **positioning, not business quality**. Could not be classified opportunistic vs routine (C10 classifier unavailable). RSI **79.14** |
| **COIN** | **VETO** | **3-of-3:** miss_streak 3/4 · insider selling −66.16 · **rev −10.35% YoY with net margin −15.72%.** Independently corroborated by `batch-scan` (`has_edge: false`, **`DP_DISTRIBUTION`**), a 7-of-10 bearish flow tape, and −3.20% today. beta **3.35** into CPI |
| **INTC** | **CAUTION −1** | Mixed, and the mix matters: the **$15B dilutive equity offering** is today's actual driver — bearish and flow-corroborating, not a rescue — but beat_streak 4/4 and rev +7.47% YoY argue against a *structural* short |
| **NOW** | **CONFIRM** | No contradiction. **Insider BUYING, MSPR +59.86** — the only insider-buying name on the board — beat_streak 3/4, rev +22.19% YoY. Fundamentals do not contradict the long, but they also **do not explain why the flow signature is defensive** |
| **PLTR** | **CAUTION −1** | Insider selling −38.74; **PE 139.6 / PS 94.1 / PB 57.3**; a contradictory same-day catalyst stack — **Burry adding fresh OTM puts, a bearish valuation piece, and PLTR's own CEO warning on AI-spending excess** |

⚠ **Earnings-date disagreement recorded:** Finnhub gives MSFT **2026-10-27** and NOW **2026-10-27**; the UW screen said **2026-11-04** for both — an 8-day gap. Finnhub is treated as primary (ticker-specific source). Both are ~78 days out, so neither carries own-earnings event risk inside a swing horizon.

### Debate-disconfirmation cuts — the gate fired on 5 of 5

| Ticker | bull | bear | Verdict |
|---|---|---|---|
| **MSFT** | **0.35** | **0.65** | **−1 tier.** Both advocates independently recommended `watch_only` over `starter` |
| COIN | 0.15 | 0.95 | −1 tier — widest spread on the board; the bull agreed the VETO is correct |
| INTC | 0.25 | 0.65 | −1 tier; the bull could not sustain the "dilution is a clearing event" argument |
| **NOW** | **0.45** | **0.55** | **−1 tier** — narrowest, one bin. The bull could not clear a coin flip on a name whose fundamentals CONFIRM |
| PLTR | 0.15 | 0.85 | −1 tier |

No pair qualified for a second round (escalation requires residuals within one bin **and** ≥0.75). **All residuals serialized verbatim, none clamped** — three of five bull residuals sit below 0.55, and the schema's former lack of a sub-0.55 bin is exactly what erased this signal on a prior run.

**MSFT is the rare case where both advocates converged on the risk decision itself.** The assigned bull volunteered the downgrade: *"if risk-monitor is choosing between starter and watch_only, I'd rather it land on watch_only than size a name whose core flow signal fails its own significance floor."* When the bull argues for less size, the debate has cleared the trade in the negative direction.

**A rubric-structure finding both debate sides confirmed, worth registering:** the sector-leader conditional +1's conditions (b) and (c) test the **identical field and threshold** (`cum_flow_30d` sign-aligned, ≥$50M) as the standalone cum-flow +1 line, while condition (a) is non-discriminating (persistence 1.0 for all 11 sectors). **Any name clearing the sector-conditional gate will by construction also clear the standalone line off the same number** — they are not independent confirmations. **COIN's raw 2 is one independent fact counted twice.** Recommended fix: cap the combined contribution at +1, or replace condition (a) with a field the standalone line does not already score. **This is a rubric-freeze matter — flagged for `/calibration-audit`, not changed here.**

### Adverse-flow exit candidates (`uw watchlist alerts` / `scan`)

There are **no `conviction_2026-08-06` or `_08-07` groups** — both runs produced empty post-gate books, consistent with today.

**`conviction_2026-08-05` = ['ZTS']** (long): flow still **bullish**, net +$0.41M, close 74.83, vol ratio 1.8×, IV rank 42.6, OI +1,151, DP $85.9M/257 trades. Two benign alerts (a 1.8× volume spike; a $5.7M single DP print — small-institutional, not mega tier). **Not an adverse reversal, but `decayed_off_thesis`** — +$0.41M is noise-level. **Drop from active tracking; no exit action.**

**`conviction_week_2026-W31` = ['MRVL','SNDK','IWM','SPY']:**

| Ticker | Flow | Net | Read |
|---|---|---|---|
| **MRVL** | bearish | **−$15.78M** | **EXIT CANDIDATE** — adverse reversal; price (−4.65%) and flow both against it |
| **SNDK** | bearish | **−$130.63M** | **EXIT CANDIDATE, with a caveat** — largest single-name bearish net on the tape, but flow and price **disagree** (+2.12%), and the put-sale-netting blind spot has a documented 08-06 precedent on **this exact ticker** (a "+$388M top bullish" that was ONE bid-side deep-ITM put sale, 74% of net). **Check the `side` field and net-as-%-of-gross before acting either way** |
| IWM | bullish | **+$0.03M** | `decayed_off_thesis`, not adverse — +$30k is noise; P/C 1.496 put-heavy on volume; IV rank 5.7 |
| SPY | bearish | −$70.85M | Adverse vs a long thesis, but read it as **hedging, not distribution** — a $773M single DP print and +1.07M OI alongside the Aug14 780C/788C `event_vol` structure (volumes *declining* 147.8K→99.4K) and the standing VIX 35C tail program = pre-CPI protection |

`fz quote-drift ZTS` returned *"need at least 2 snapshots (have 1)"* — **cold-start, skipped silently** per the advisory rule.

### Hedge sleeve

**Directional skew 0.00. Net delta zero. Positions none. The hedge rule (≥0.6 skew) does not fire, and no hedge is proposed.** Buying SPY/QQQ puts or a VIX call ladder against a book with no positions is not risk management — it is **initiating a naked directional CPI bet under a hedging label**, and it would be the only sized risk on the sheet.

Two notes if the desk carries long exposure from **outside** this fleet. **Substrate preference: QQQ over SPY over VIX** — QQQ VRP is PREMIUM_BUYING (−0.0503), so a **QQQ Aug-21 put vertical** is the cheapest defined-risk protection available; SPY VRP is FAIR, no edge; a **VIX call ladder is the worst of the three** (VIX 15.46 with index front-end IV in contango means paying up for the leg that only pays on a shock, and the 0DTE validation sample contains **no vol shock at all** — do not size a tail structure off an untested tail). And **anchor the wings, not the direction**: SPY spot 772.87 versus ZGL 773.02 is a genuine NEAR_FLIP that has flipped 3× in 4 sessions on a `total_gex` that barely moved; below **768** lies a diffuse negative-gamma trough spanning **748–767** with no dominant strike, so protection belongs below 768 — and the GEX prior is void on a CPI gap regardless.

### Is the book empty, and is that correct?

**Yes, and yes.** The failure is over-determined rather than marginal: no HIGH, no MEDIUM, one LOW name in twelve scored. MSFT took **three independent, unrelated cuts**, any one of which floors `starter`. Its +3 conjunction fails the quant's own pre-registered C11(c) 5%-of-gross floor (4.41% at 30d, 2.8% at 90d), and the bear's unrefuted point is that **`oi_smart_positioning` never measured MSFT at all** — one of the three conjunction legs is *absent*, not merely weak. **Both debate advocates, arguing opposite sides, independently recommended `watch_only`.** The debate gate fired on 5 of 5 names. CPI is two sessions out and the regime tool itself says *"wait for clarity"* — the strongest available expression of which is to wait.

The audit record supports this rather than merely tolerating it: the **DROP pile has outperformed the sized book in every window that measured it** (43.3% vs 38.6% on 2026-07-18; 0.440 DROP vs 0.418 LOW vs 0.143 HIGH on 2026-08-01), the out-of-regime half-cap has been **protective in all five audits that measured it**, and the empty-board refusal has now been graded correct six-plus consecutive times. Manufacturing a trade to avoid a flat sheet is the behaviour this system's own history grades as wrong.

**What to watch tomorrow, in order:** whether MSFT's OI build extends a 6th session and holds the **505.14** shelf; whether the **LITE (08-11 post)**, **CRWV** and **SMCI** prints resolve the semis backwardation — **SMH's failed DEX flip at `magnitude_ratio` 0.50 and LITE's at 0.29 are levels, not flips**, and become real signals only if they extend; and whether Financial Services and Energy print netted-IN again on **both 08-11 and 08-12** with Technology holding OUT, the only path by which the rotation call graduates from `no_change`.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**No name reached HIGH or MEDIUM. This section is empty by construction.** `raw_score` ceiling today was **6** (MSFT, LOW).

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no per-tier expectancy is reportable this run — there are **zero HIGH and zero MEDIUM calls to compute over**, and the most recent `/calibration-audit` (2026-08-08) found the same structural emptiness, which is why the freeze-lift has now been unrunnable for **eight consecutive cycles** (one `full`-sized call in 626 rows). The standing per-tier reads it carries are **HIGH 0.143 / LOW 0.418 / DROP 0.440** — an inversion that has persisted across multiple audits and is the reason the ≥9 HIGH cut carries no validated ranking claim. The live sizer remains the win-rate ladder; the C3 fractional-Kelly sizer stays ADVISORY until tier × expectancy is monotone on n≥30.

### Full score audit — all 12 scored calls (the below-threshold book, for the record)

| Ticker | raw | tier | dir | class | `win_rate` (n, source) | `market_excess` | pre-risk | fund. | debate (bull/bear) | final |
|---|---|---|---|---|---|---|---|---|---|---|
| **MSFT** | **6** | **LOW** | long | `dark_pool_accumulation` | `null` — **NA(substrate)** | `null` | starter | CAUTION −1 | 0.35 / 0.65 | **`watch_only`** |
| COIN | 2 | DROP | long | `sector_rotation` | `null` — NA(substrate) | `null` | skip | **VETO** | 0.15 / 0.95 | `watch_only` (VETO) |
| INTC | 1 | DROP | **short** | `bearish_flow` | **0.5714** (n=133, backtest_clean) | **+0.0752** | watch_only | CAUTION −1 | 0.25 / 0.65 | **`watch_only`** (short routing) |
| NOW | 1 | DROP | long | `dark_pool_accumulation` | `null` — NA(substrate) | `null` | skip | **CONFIRM** | 0.45 / 0.55 | skip |
| PLTR | 1 | DROP | long | `bullish_flow` | 0.4308 (n=130) | **−0.1000** | skip | CAUTION −1 | 0.15 / 0.85 | skip |
| SNDK | 1 | DROP | vol_long | `high_iv_rank` | **0.60** (ceiling; uncapped 0.8205, n=156) | +0.5256 (artifact) | skip | NA | — | skip |
| USO | 1 | DROP | vol_long | `high_iv_rank` | 0.60 (ceiling) | +0.5256 (artifact) | skip | NA | — | skip |
| HD | 1 | DROP | vol_short | `earnings_vol` | `null` — **NA(substrate)** | `null` | skip | NA | — | skip |
| LOW | 1 | DROP | vol_short | `earnings_vol` | `null` — NA(substrate) | `null` | skip | NA | — | skip |
| MRVL | 0 | DROP | vol_long | `high_iv_rank` | 0.60 (ceiling) | +0.5256 (artifact) | skip | NA | — | skip |
| SPCX | −1 | DROP | long | `bullish_flow` | 0.4308 | −0.1000 | skip | NA | — | skip |
| **GLD** | **−3** | DROP | long | `bullish_flow` | 0.4308 | −0.1000 | skip | NA | — | skip |

**MSFT `score_components` (Σ = 3+1+2 = 6 ✓):**

| Line | pts | Source agent | Source tool | Evidence |
|---|---|---|---|---|
| 3+ aligned signals in accumulation-hunter (conjunction) | **+3** | accumulation-hunter | `uw insights institutional-accumulation` + `uw dark-pool block-stratified` | ACCUMULATION 1.51 + `oi_trend` BUILDING 5/5 (+579,082) + mega buy_ratio 0.69 institutional tier. C11 as frozen: `cum_flow_30d` +$727.8M sign-aligned ✓, ≥$50M ✓ ⇒ **full +3**. Two $506.06 prints 7s apart ($1.33B) excluded as closing-cross; **$523.5M genuine dispersed regular-hours buying at 4 price levels survives** |
| multi-day OI build | **+1** | accumulation-hunter | `uw historical oi-trend` | BUILDING 5/5, +579,082. ⚠ **C47: fired 16-of-16 on a prior run — awarded because frozen, treated as zero evidence** |
| multileg directional structure (term-structure-anchored) | **+2** | multileg-strategist | `uw hot-chains multileg` | Oct16 510C/550C vertical, `multileg_ratio` 0.97–0.99 both legs, $221.3M, defined risk (max loss = net debit, 40-wide). ⚠ Booked at less than full confidence: the agent lacked `iv-term-structure`, so the term anchor is the **absence of a near-dated event**, not a measured kink; `repeats_over_n_sessions = 1` |
| cum-premium-flow 30d accretion — INTENT-SCREENED | **0** | signal-confluence-quant | `uw historical cumulative-premium-flow` | **ZEROED** — a C28 `distribution_flag` is present (deep-ITM 480C OI 2179→852 on vol 1761, ~$3.83M closed), so screen condition (a) fails |
| MECHANIZED DEX flip / vanna-squeeze | 0 | dealer-positioning-strategist | `scripts/dex_flip.py` | Fires nowhere today |
| conviction-matrix DIRECTIONAL_LONG >70 | 0 | leap-positioning-radar | `uw insights conviction-matrix` | LEAP-only conditional, class ≠ `leap_directional`; would fail anyway at **confidence 12.3%** |
| flow_conflict / lite | 0 | signal-confluence-quant | `uw historical cumulative-premium-flow` | Aligned, magnitude **7.67× the union median** — neither branch fires |

**`gate_verdicts` (MSFT, all 9 keys):** `regime:` no-op · `vrp:` no-op (favourable) · `panic:` no-op (0.995 FLAT) · `cluster:` no-op (below reporting floor vs NOW/PLTR) · `sector:` no-op (Tech netted OUT but persistence 0.40 < 0.60) · `fundamentals:` **−1 tier (CAUTION)** · `event_risk:` **−1 tier (CPI T+2)** · `debate:` **−1 tier (bear 0.65 ≥ bull 0.35)** · `rubric_regime:` capped half (OUT-OF-REGIME). **Net −3 tiers ⇒ `watch_only`.**

**Step 3a load-bearing-tool gate: does not fire** (no candidate reached raw ≥9). Reported anyway, because a silent skip reads as a missed gate: **MSFT cites 3 of 4** — `dark-pool block-stratified` ✓, `historical cumulative-premium-flow` ✓, `insights institutional-accumulation` ✓, `options-structure dex` ✗. At 3-of-4 MSFT would have **preserved** HIGH on citation breadth had it scored ≥9; **the gate is not what holds it at LOW — the score is.**

**Union median `|cum_flow_30d|` = $94.85M** (over the 12 scored names; near-zero bar $23.71M, Q1 bar $15.62M). Deductions applied: **GLD −3** (−$290.2M opposing, 3.06× median), **SPCX −1**, **TTD −1**, **UBER −1** (all near-zero AND bottom-quartile). Exactly one deduction per ticker, never both. **MSFT: none** — its label is MIXED, but the frozen rubric operationalizes lite as "near zero **or** bottom-quartile," and at 7.67× the median it is the opposite of both.

**Clean-query protocol record (P0.3).** Complete-window cutoff `signal_date ≤ 2026-08-03`; `--top-n 200` pinned; headline `win_rate` never quoted; graded against the **class** direction.

| Class | Headline (not quoted) | Clamped | Price floor | ADV floor | **Kept n** | **Recomputed** | SPY same-window | Excess |
|---|---|---|---|---|---|---|---|---|
| `dark_pool_accumulation` | — | — | — | — | **0** | **NA(substrate)** | — | — |
| `bullish_flow` | 42.9% | 13 | 1 | 12 | 130 | **0.4308** | 0.5308 | **−0.1000** |
| `bearish_flow` | 57.9% | 11 | 0 | 8 | 133 | **0.5714** | 0.4962 | **+0.0752** |
| `high_iv_rank` | 78.7% | 15 | 10 | 7 | 156 | 0.8205 → **capped 0.60** | 0.2949 | +0.5256 (artifact) |

⚠ **Three substrate findings from this run, for `/calibration-audit`:**
1. **`dark_pool_accumulation` returns `total_signals: 0` market-wide at every `--top-n`** — the desk's most heavily-weighted rubric line (+3) currently has **no measurable base rate at all**. Bears directly on the pre-registered DP-conjunction backtest.
2. **`scripts/excess_winrate.py` does not implement the 2026-08-01 P1 #3 vol class ceilings** — there is no `class_ceiling` function and no `earnings_vol`/`high_iv_rank` constants; `size_decision(0.8205, 156, 0.2949)` returns **`full`**. The 0.60 ceiling was applied **by hand**. This is the same shape as the historical leak that P1 #2 mechanized the absolute ceiling to prevent: the prose ceiling is live, the code path is not. Harmless today (the drop floor binds everything) ⇒ **latent, register item, not a P0.**
3. **The C11(c) 5%-of-gross adjudication should be settled before it matters.** Today it changed nothing (LOW/starter either way), but on a name scoring 8 or 9 it is the difference between MEDIUM and HIGH. The frozen rubric's C11 text is only "sign-aligned AND ≥$50M"; the 5% floor comes from the quant's own definition and its level is **pre-registered and undecided**. The frozen-literal number was taken as authoritative here (raw 6), with the churn finding carried as advisory (raw 4) — the freeze exists so audits grade the rubric rather than retune it mid-run.

The `+0.5256` excess on `high_iv_rank` is **not edge** — the benchmark is SPY clearing a 2% 5-day move (0.2949) in a 13.6-rv tape against single names (0.8205); that gap is single-name-versus-index dispersion, structurally positive and uninformative.

### Conviction scoring rubric (Step 4) — embedded verbatim for audit

> **RUBRIC FROZEN — version `2026-06-12`.** Weights, tier cuts and gate membership are frozen. No line may be promoted, demoted, added or re-binned until a change clears a pre-registered, cross-regime, Benjamini-Hochberg-surviving bar. Audits **grade** this rubric; they do not retune it.

```
Daily conviction score = Σ:
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna-squeeze in trade direction — must be a verified
      SIGN CHANGE, not a level: sign(net_dex) on the latest session opposite to ≥3 consecutive prior sessions, read from
      dated `uw options-structure dex --date` calls, with |net_dex| on the flip day ≥ 0.25× the trailing-10-session median
      |net_dex|; evidence must cite both dated values. Compute with `scripts/dex_flip.py` — never by hand. Vanna disjunct
      additionally requires a dated VIX source (Yahoo chart API ^VIX).   # DEMOTED +3→+1 and MECHANIZED 2026-06-12 P0.4
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified institutional tier confirmed)
      — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms (sign aligned AND |cum_flow_30d| ≥ $50M);
      else halved to +1.   # was +2; promoted 2026-05-15 P1.2 (LOAD-BEARING)
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)   # was +2; reduced 2026-05-09
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: award only when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.   # 2026-05-23 P1.1 (−23pp on swing, n=8)
  +1  uw historical cumulative-premium-flow net directional accretion (30d) — INTENT-SCREENED: 0 if a C28
      distribution_flag is present, or (dividend payer in an ex-div window) the accreting prints are deep-ITM sub-parity
      calls. A sub-$50M flow that halved the +3 does NOT separately qualify here.   # DEMOTED +3→+1 2026-06-06 P1.4
  +1  sector-rotation-strategist names ticker as single-name leader — CONDITIONAL: (a) sector persistence_score ≥ 0.6
      AND (b) cum_premium_flow_30d aligned AND (c) |cum_flow_30d| ≥ $50M. Default 0.   # 2026-05-23 P1.5
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored play type)   # promoted 2026-05-09
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags overcrowded long with rising uw historical pc-ratio-zscore (VRP positive)
      # MECHANISM (2026-06-12 P1.5): an INFORMED-FLOW CONTINUATION penalty, not "the crowd is wrong, fade it."
  -3  flow_conflict — cum_premium_flow 30d direction clearly opposite dominant_signal_class (signed-sum sign flip +
      magnitude > today's union-median |cum_flow_30d|, or explicit OPPOSITE label)   # 2026-05-15 P0
  -1  flow_conflict_lite — 30d cum_premium_flow read is MIXED (signed sum near zero, or aligned but bottom-quartile
      magnitude in today's union)   # mutually exclusive with flow_conflict — apply ONE, never both
  # REMOVED: signal-confluence ≥4 (+2, removed 2026-06-12 P0.2 — a server-side RE-COUNT of quantities already scored;
  #   funnel-seed ONLY, earns 0, gates no entry, sits in no HIGH-tier gate)
  # REMOVED: sweep-persistence top-5 (+1, removed 2026-05-23 P0.3 — −22pp over two consecutive audits)
  # REMOVED: gamma-flip-tracker 0DTE setup (removed 2026-05-09 — NO-INFO on swing; §2 is advisory, 0 points, kept OUT of calls[])
  # TIER GATES applied by risk-monitor in 2d — 0 points, never score_components:
  -1  [TIER] correlation cluster (pairwise corr ≥ 0.70) — −1 TIER
  -3  [TIER] uw risk market-regime conflicts with trade direction — −1 TIER
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | HIGH | full (subject to Step 3a LB gate + win-rate gate) |
| 7–8 | MEDIUM | half (subject to win-rate gate) |
| 3–6 | LOW | starter / watch-only |
| ≤ 2 | drop | filtered by the quant's drop floor |

**Tier-cut status:** the ≥9 HIGH cut was set in-sample on UPTREND data and **failed its scheduled re-confirmation on 2026-06-12** (bands inverted on the first post-UPTREND window). The cuts are retained under the freeze but **carry no validated ranking claim**; the P0.6 out-of-regime guard caps all sizing at half in the interim.

---

## 8. Watch-only — single signal, no confluence

Surfaced by one agent but failed the ≥2-agent confluence gate. **For journaling, not trade entry.**

| Ticker | Flagging agent | The single signal |
|---|---|---|
| **NOW** | accumulation-hunter | +$113.2M `cum_flow_30d`, the **only clean non-MIXED BULLISH label of the day** (5.85% of gross — clearing even the advisory 5% floor MSFT failed), plus the run's only fundamentals CONFIRM with **insider buying**. Undercut by 5-of-6 closing-cross DP prints and a 67dte protective PUT as its largest OI build |
| **COIN** | sector-rotation-strategist | The **only** single-name leader clearing all three conditions of the conditional +1. VETO'd on fundamentals; the +1/+1 is arguably one fact counted twice |
| **SNDK** | vol-surface-scout | The board's **highest-conviction vol dislocation** (VRP −0.5966, iv30d 91.5% vs realised 151.2%, no earnings in 14 days) — scores 1 because the frozen rubric pays for flow and structure, not surface mispricing |
| **USO** | vol-surface-scout | Genuine 4dte kink, 19.8% prominence on 5,992 contracts — but `macro_floor_adjusted: YES` (the kink *is* the CPI/EIA Wednesday cluster) |
| **HD** | earnings-scout | The only genuine kink at an own-earnings tenor in the whole scan (27.4% prominence, 1,306 contracts, 08-21 expiry, tail confirmed). **Better entry Thu 08-13 / Fri 08-14** |
| **LOW** | earnings-scout | Weak mirror of HD — 9.9% prominence on 250 contracts, tail not confirmed |
| **INTC** | sweep-tracker | −$858.7M BEARISH cum-flow, 96.1% ask-side 67.5P at 13.5× size/OI, and the **only positive-excess class in the run** (+0.0752). Routed `watch_only` as a directional short |
| **PLTR** | sweep-tracker | 130dte 175C OI build +49,736 — but retracted by `multileg` (not an active structure) and `leap-radar` (0/9) |
| **SPCX** | sweep-tracker | Self-conflicted: 5/5 bearish persistence label against +$14.8M net bullish premium and a 4dte call build +76,283 |
| **MRVL** | vol-surface-scout | Marginal KINKED (6.1% prominence, `front_end_ratio` 1.088) with **VRP never measured** — the +1's mandatory clause is unverified |
| XOM / CVX / RIG / NE / WHD | sector-rotation-strategist | Energy leaders; **all fail the +1 on the $50M size condition** ($30.9M / $2.16M / $0.62M / $1.55M / $0.24M) |
| SMH / LITE | dealer-positioning-strategist | **Not even positive flags** — both DEX sign flips **failed the magnitude floor** (0.50 / 0.29). Watch items for 08-11 |

**Explicitly rejected by the agent that looked hardest** (not watch-only — negative evidence): **TTD** (100% of buy-side DP tape closing-cross-pegged at $13.39 across 20:04–21:29Z while real intraday trades printed mixed-direction at *declining* prices; 30d −$4.9M, 90d **−$38.5M BEARISH**; matrix COVERED_CALL — confirmed **distribution-into-weakness disguised as accumulation**) · **SMH** (mega DP buy_ratio **0** — 100% sell — resolving the +$14.2M screener divergence as distribution) · **CRWD** (institutional-accumulation **NEUTRAL**, no mega tier, +$42.1M MIXED below $50M ⇒ the +5.01% new-high move is **not** accumulation-confirmed) · **UBER** (mega 100% closing-pegged, cum-flow **−$5.9M**) · **RDNT** (no mega tier, block buy_ratio **0.164** despite +6.76%) · **AG / HL / GFI** (block tier **100% sell**; hedging against a +20% week, not shorts) · **WULF / CRWV** (mega single print, 100% sell) · **ORCL** (mega 0.502 coin-flip, block 0.428) · **PANW** (3 of 4 mega prints closing-pegged, cum-flow MIXED) · **MU / AMD** (bearish OI evidence ruled an un-split-adjusted strike-grid artifact).

---

### Run metadata

Fleet: **10 Phase 1 agents** (11-agent roster minus `opex-pin-strategist` — the third Friday is **2026-08-21**, 11 days out, so the OPEX guard did not fire), then Phase 2 sequentially: quant → fundamentals-gate → 5 bull/bear debates → risk-monitor. All Step-0 cache payloads fetched clean (`failed[] == []`, 22/22).
`fz_available: true`, but ⚠ **the upstream doubled-first-letter bug is live on every `fz` surface today** (`AABEO`→ABEO, `CCRWD`→CRWD, `BBSP`→BSP — de-doubling verified by exact price cross-match against `iv_rank_high` and `screener_bearish`). The squeeze lane additionally returned only 20 alphabetically-first A-tickers — a truncated page-1, **not a ranked market-wide screen** — so it cannot claim to surface the top squeeze names. All `fz` lanes are advisory, 0 rubric points.
Single-leg whale scan (`--regime neutral`, since TRANSITIONAL is not bull): **25 signals, ZERO Tier-1** — 11 `OPENING_PUT_STRONG` (Tier-2, DTE>30), 8 `CALL_UNVALIDATED` (correctly labelled rather than faded, per the regime tag), 6 `PUT_CONTEXT`, every row `action: CONTEXT_ONLY`. **No edge from this lane today.** Advisory, **0 rubric points permanently** — C19 was CLOSED as REFUTED on 2026-07-25 and no rolling WR is reported as accrual.
`volume_vs_average` was **unusable**: it returned micro-ETFs on 14–200 contracts of volume (HRZN1 ratio 1501 on 50 contracts; WDIV 14; IUSV 18; MUNI 23), essentially all failing C12. No candidates were seeded from it.
C12 liquidity floor (price ≥ $5 AND 20d dollar-ADV ≥ $50M, fail-closed, `--as-of 2026-08-10`) dropped **22 names**: COLM $42.2M, BLBD $40.3M, CWEN $39.1M, AGIO $42.3M, GRBK $15.4M, BL $32.0M, ODD $11.3M, EVC $16.0M, JANX $11.5M, GO $21.9M, CRK $31.8M, NEO $46.7M, AIRJ $9.3M, GEO $47.1M, HZO $30.2M, SBET $49.4M, TDOC $47.1M, ALMS $27.3M, AHCO $25.0M, EYPT $20.7M, MFP $42.6M (all sub-ADV) and MPT (price $4.15).
`schema_version: 1.3` · `rubric_version: 2026-06-12` · envelope at `analyses/daily/2026-08-10/decision.json`.
