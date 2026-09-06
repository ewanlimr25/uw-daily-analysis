# Daily Market Analysis — 2026-07-24

## Executive Summary

- **Regime + GEX state:** TRANSITIONAL / CHOPPY. SPY 738.93 (+0.10%) sits below both the 20-SMA (746.15) and 50-SMA (745.07), −2.82% off the 90-day high. VIX 18.58. Both index gamma books are **FULLY_NEGATIVE** (SPY −$1.556B, QQQ −$1.753B) with `zero_gamma_level` null — dealers amplify moves in *both* directions. Options-flow breadth is 33% bullish (2,074 bullish vs 4,215 bearish tickers). **Today was an AI/semis unwind with a broad rotation, not a bounce**: cap-weighted QQQ −1.12% and IWM −0.31% while equal-weight RSP +0.78% and 72% of S&P names rose (XLRE +2.22%, XLB +1.93%, XLP +1.11%) — the casualties were NBIS −15.02%, BE −14.91%, SOXL −13.14%, SNDK −10.79%, IREN −8.65%, MU −6.99%, WDC −6.90%.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL/CHOPPY) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** SPY — short gamma, ZGL null/unreliable, a −$396.3M net-GEX trapdoor at 740 one point above spot, unbroken put trench 735→720; bias: no pin, size down, tight wings. QQQ — short gamma, ZGL null/unreliable, **no positive-gamma resistance anywhere near spot**, a single −$734.5M spike at 685; bias: no structural level to anchor short strikes against. Advisory, see §2.
- **Top swing build:** **None.** Zero names cleared to a sized long or short.
- **Top LEAP candidate:** **None.** Zero of nine candidates cleared 6-of-9 gates.
- **Biggest risk:** the semis / AI-infrastructure complex (MU · NBIS · SMH · BE · IREN · SOXL · SOXX · SNDK · AMD) is functionally **one unwinding position** — MU/SMH correlate at 0.854. No hedge sleeve is triggered because the sized book is empty; **FOMC lands in 3 trading days (07-29 presser)** and Monday 07-27 is the only clean session before it.

> **The post-gate book is flat — the 19th consecutive empty conviction board.** Three names walked in at LOW/starter (TSLA, AKAM, FSLR); all three left as watch-only. This is the graded-correct behaviour, not manufactured caution: the 2026-07-18 calibration audit measured DROP 43.3% > traded 41.1% > sized 38.6%.

---

## 1. Regime & Gamma State

`uw risk market-regime` returns **TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity"**, trend **CHOPPY**, guidance *"half position sizes, favor defined-risk strategies, iron condors in range."* SPY has now lost both moving averages. The breadth picture is the day's central fact and it is **two-sided**: the options tape is deeply bearish (33% bullish flow breadth) while the *price* tape is broadly green (363 advancers vs 140 decliners). Those are not contradictory — they are measuring different things. The selling is concentrated in the cap-weighted AI/semis complex; the buying is spread across the other 400 names.

**Per-index gamma (EOD current-state book, 0–45 DTE):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 738.52 | `null` (unreliable) | −$1.556B | FULLY_NEGATIVE | 739 (+$64.3M, ATM noise); real cluster 748 / 760 | 735 (−$155.0M), trench to 720 |
| QQQ | 684.16 | `null` (unreliable) | −$1.753B | FULLY_NEGATIVE | 701 (+$646K — noise-level, no real wall) | 685 (−$734.5M) |
| IWM | 291.26 | 194.01 — **grid artifact** | −$1.335B | label says POSITIVE; **`total_gex` is negative** | — | — |

⚠ **IWM row is unreliable.** The tool labels the regime POSITIVE while `total_gex` is −$1.335B, and returns a ZGL 33% below spot. This is the known ZGL-grid artifact (recurring on SPY/QQQ/IWM/MU); `zgl_reliable=false`. Read the `total_gex` *sign*, not the label.

**DTE volume share (market-wide):** 0DTE **50.1%** · weeklies 24.1% · monthlies 13.8% · LEAPs 2.1% → `RETAIL_DRIVEN`. Half of today's tape expires tonight; only 15.9% is monthly-or-longer, which is why the genuine institutional multi-leg slice is thin (§3) and the LEAP board is empty (§4).

**VRP:** SPY **FAIR +0.0177** (IV30 0.1534 vs RV30 0.1357) · QQQ **FAIR-but-NEGATIVE −0.0138** (IV30 0.2619 vs RV30 0.2757). The sign split is itself the headline vol observation — Nasdaq-complex vol is *cheap* versus realised, so premium-selling in that complex is unsupported (see §5).

**Macro backdrop** (`scripts/fred_macro.py`): yield curve **normal** (10Y−2Y +0.36) · core CPI **2.81% YoY** · core PCE **3.41% YoY** · unemployment 4.2% · payrolls +57k MoM · **10Y 4.71%, RISING (+21bp/30d)** · **USD STRENGTHENING** · fed funds 3.63%. Rising long-end yields plus a firming dollar is a direct headwind to long-duration growth and to the capital-intensive AI-infrastructure buildout names that led today's decline.

**Forward event risk — a macro-stacked fortnight, and today's dominant gate:**

| Event | Date | Trading days out | Impact |
|---|---|---|---|
| **FOMC decision + presser** | 2026-07-29 14:00 ET (mtg 07-28/29) | **T+3** | **HIGH** |
| JOLTS (June) | 2026-07-29 | T+3 | low |
| Jobless claims | 2026-07-30 | T+4 | low |
| **Core PCE (June)** | ~2026-07-31 | **T+5** | **HIGH** |
| Jobless claims | 2026-08-06 | T+9 | low |
| **NFP / Employment Situation (July)** | 2026-08-07 | **T+10** | **HIGH** |
| **CPI (July)** | 2026-08-12 | T+13 | **HIGH** |

Monday **2026-07-27 is the only clean pre-FOMC session.**

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — built from open interest that persists overnight — read forward as the *prior* for the next session's open. Prose-only, **0 rubric points**, no backtested predictive claim. Scope is SPY and QQQ only.

Both books came back `regime: FULLY_NEGATIVE` with `zero_gamma_level: null`, so the per-strike `net_gex` array was pulled directly (50-strike grid, populated, spanning spot) and the read falls back to the `total_gex` sign plus spot-vs-wall position.

**SPY — spot 738.52 · ZGL null (`zgl_reliable=false`) · total GEX −$1.556B · FULLY_NEGATIVE**
The nominal call wall at 739 (+$64.3M) is one point above spot and is essentially ATM 0DTE noise. One strike further up, **740 carries −$396.3M net GEX — the single largest strike in the entire book.** That is not a wall, it is a short-gamma trapdoor directly overhead. Below spot there is an unbroken negative trench: 735 (−$155.0M), 730 (−$147.8M), 725 (−$117.8M), 720 (−$140.9M), continuing to the bottom of the visible grid at 714. There is no positive-gamma buffer anywhere nearby. `total_gex` has deepened across the week (−$443M on 07-22 → −$2.47B on 07-23 → −$1.56B today).
**Structure bias:** short gamma reads *vol expansion / trend*, while the VRP backtest (§2a) says *sell premium*. Resolve the tension through **wing width and size, not direction** — if selling premium, keep strikes tight inside the 735–748 zone and cut the 1.5× scalar rather than running a wide condor into an unbounded trench on either side.

**QQQ — spot 684.16 · ZGL null (`zgl_reliable=false`) · total GEX −$1.753B · FULLY_NEGATIVE**
The more extreme of the two. The nominal call wall at 701 is +$646K — noise; the next positive strikes (709 at +$321K, 697 at +$82K) are negligible. **There is effectively no positive-gamma resistance anywhere in the visible 45-DTE book above spot.** Below, 685 carries −$734.5M and dominates the grid, with 680 (−$128.3M) and 695 (−$77.7M) behind it; the book is negative from 660 through 709. `total_gex` deepened from −$477M (07-22, still POSITIVE that day) to −$1.18B (07-23) to −$1.75B today as QQQ fell 706.70 → 684.16 — textbook self-reinforcing short-gamma dynamics.
**Structure bias:** with no call-side wall there is **no structural level to anchor short strikes against**. Favour a long straddle/strangle or a debit vertical sized to the 1.10% implied move, or stand aside into FOMC — QQQ's rate sensitivity (10Y +21bp/30d, USD firming) compounds the gap risk.

**Regime freshness:** neither regime is fresh in a useful sense. Both indices have whipsawed POSITIVE/NEGATIVE/FULLY_NEGATIVE nearly every session for three weeks (SPY flips 07-10, 07-16, 07-17, a NEGATIVE blip 07-21/22, FULLY_NEGATIVE 07-23→today; QQQ similar). The current stretch is **2 clean sessions old inside a chronically unstable regime — treat the prior as low-confidence.**

**Mandatory caveats:**
- **EOD is a prior, not a target.** Today's 0DTE expiry carried $6.71B of premium (vs $1.99B for Monday 07-27 and $4.20B for 07-31) and rolls off tonight. A large share of the negative-gamma concentration at SPY 740 / QQQ 685 is 0DTE-driven and **will not carry forward** — Monday's opening book could look materially different once fresh OI populates in the first 30–60 minutes.
- **ZGL unreliable.** `null` on FULLY_NEGATIVE days; the read falls back to the `total_gex` sign and spot-vs-wall position.
- **Gap risk voids the prior.** FOMC is Tuesday/Wednesday; Monday 07-27 is the last clean session. This prior is good for one session.
- **Tooling limit.** `gex --dte-max 1` errors — uw-pp cannot isolate the D+1 expiry. This is the standing **0–45 DTE** book, the best available proxy.
- **ETF book, not index book.** SPY/QQQ ETF gamma includes creation/redemption noise that SPX/NDX does not.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py`)

The GEX walls above are a **map, not a pin** — wall-as-magnet backtested NO_GO, as did every directional 0DTE signal. What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, and **not a guaranteed edge**.

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` / VIX | HIGH / 18.58 | HIGH / 18.58 |
| implied move | 0.62% | 1.10% |
| `expected_range_pct` | 1.18% | 1.95% |
| `size_scalar` | 1.5 | 1.5 |
| suggested structure | wider iron condor, wings ≈ ±1.18% | wider iron condor, wings ≈ ±1.95% |
| `stand_aside_reason` / `caution` | null | null |
| rolling backtest | **net +0.175%/day** (gross 0.275%, cost 0.10%), win 93.3%, worst −1.40% | **net +0.304%/day** (gross 0.404%, cost 0.10%), win 88.3%, worst −2.453% |
| verdict | `GO_PREMIUM_SELL_INTRADAY` | `GO_PREMIUM_SELL_INTRADAY` |

**Read the PnL on its real basis.** `pnl_basis` = *percent-of-underlying-spot-notional, GROSS* — not premium-collected, not margin-relative. Lead with the **net** figure: +0.175%/day (SPY), +0.304%/day (QQQ). The gross win-rate materially overstates a negatively-skewed short-vol edge.

**Entry rule:** enter at/after the open once the overnight gap resolves; if it gaps beyond the wings, stand aside. Hold the 0DTE to the close — **never carry overnight** (overnight entry backtested negative: SPY +0.051%, QQQ **−0.075%**). No directional tilt — this is delta-neutral.

**SPY ≈ SPX** (validated identical). **QQQ is weaker** (Nasdaq index book unavailable) — lower confidence.
**Promotion bar (P1.8):** stays advisory / 0 rubric points **permanently** until BOTH a vol-shock day enters the sample (the short-vol left tail is **UNSAMPLED**) AND net expectancy clears a tail-aware bar. Win-rate is explicitly **not** the promotion metric.

### 2b. Swing Dealer Positioning (1–4 weeks)

The mechanized DEX-flip test (sign change on the latest session opposite ≥3 consecutive priors, flip-day |net_dex| ≥ 0.25× the trailing-10-session median) **fired on two names today — the first clean pass in some time.**

| Symbol | net_dex (07-24) | Prior run | Flip? | Vanna squeeze | Swing bias |
|---|---|---|---|---|---|
| **MU** | −$4.06B | +$4.96B / +$3.60B / +$4.77B | **YES** — 3.3× the $1.216B floor (median $4.865B) | false | SHORT |
| **NBIS** | −$0.587B | +$1.344B / +$1.335B / +$1.207B | **YES** — 2.6× the $0.226B floor (median $0.903B) | false | SHORT |
| SPY | −$38.43B | −$50.52B / −$8.71B / −$4.24B | no — level only, deepening | false | SHORT (tilt, unscored) |
| QQQ | −$48.27B | −$37.00B / −$14.74B / −$6.02B | no — monotonic deepening | false | SHORT (tilt, unscored) |
| IWM | −$10.16B | −$8.71B / −$5.76B / −$2.53B | no | false | NEUTRAL→SHORT (low conf.) |
| TSLA | −$7.40B | −$9.65B / −$1.64B / −$0.43B | no | false | SHORT (tilt) |
| SMH | −$8.98B | −$4.68B / −$4.27B / −$4.97B | no — roughly doubled today | false | SHORT (tilt) |
| ORCL | −$1.64B | −$1.32B / −$0.48B / −$0.51B | no | false | SHORT (tilt) |
| AMD | +$3.37B | +$5.39B / +$7.66B / +$6.18B | no — positive but fading | false | NEUTRAL |
| AAPL | +$11.43B | +$4.55B / +$6.35B / +$7.55B | no — positive, improving | false | LONG (tilt) |
| MSTR, GOOGL | — | — | **no — stale flip** (sign changed 1–2 sessions ago, fails the "latest session" test) | false | reported honestly, not stretched |

**Both flips carry an honest caveat:** MU has changed DEX sign 5 times in the trailing 14 sessions and NBIS 4 times — both clear the magnitude floor because their absolute DEX runs large, not because this flip is structurally different from the prior three. NBIS's flip-day magnitude is *smaller* than the run it reverses. Corroboration is nonetheless real: both saw same-day GEX total-sign flips, both carry Tier-1 opening put whales, and NBIS's $170 whale strike is the #2 GEX concentration in its book (13.6% of |gex|).

**No name earns the vanna-squeeze line.** VIX fell 18.65 (07-20) → 17.05 → 16.64 (07-22) but **reversed** to 18.70 / 18.58 over the last two sessions, so the ≥3-session falling-VIX gate fails market-wide — consistent with FOMC bidding front-end vol back up.

Front-end IV ratios are elevated across the complex (SPY 1.429, QQQ 1.421, IWM 1.506) but **this is contaminated by Friday same-day 0DTE expiry** inflating every name's near tenor. Directionally suggestive of an event-risk bid; not a clean panic signal.

### 2c. Sector Rotation

**Rotation regime call: `no_change` — confidence LOW.** No canonical two-camp pattern fits. Four sectors stand out on inflow simultaneously (Technology, Financial Services, Healthcare, Energy — one growth, one crypto-proxy, one defensive, one cyclical) against a single clean outflow leg (Industrials). That maps to no canonical rotation, so only individual sector calls are surfaced.

⚠ **The persistence scale is degenerate today.** Eight of eleven sectors printed `persistence_score = 1.0`, so the ≥0.6 gate is non-binding and persistence is **non-discriminating** this session. Ties were resolved by ranking the 1.0 cohort on signed net-flow magnitude against the cross-sector median ($35.8M).

⚠ **Retail-tape downgrade (uniform).** 0DTE share is 50.1%, at/over the retail-dominated threshold → **every rotation call below is tactical-only, not swing-book conviction.**

| Sector | Persistence | Trend | Net flow by day, 07-20 → 07-24 ($M) |
|---|---|---|---|
| Technology | 1.0 | INFLOW | 1,423.5 / 2,462.5 / 3,234.9 / 767.2 / **966.7** |
| Financial Services | 1.0 | INFLOW | 236.3 / 251.1 / 184.5 / 136.2 / **145.1** |
| Healthcare | 1.0 | INFLOW | 101.2 / 144.7 / 456.7 / 30.7 / **132.5** |
| Energy | 1.0 | INFLOW | 66.3 / 84.3 / 108.1 / 104.3 / **78.0** |
| Communication Services | 0.8 | INFLOW | 618.4 / 591.9 / 501.2 / −784.0 / **75.4** |
| Consumer Defensive | 1.0 | INFLOW | 45.0 / 49.1 / 36.1 / 133.6 / **35.8** |
| Real Estate | 1.0 | INFLOW | 14.2 / 10.2 / 5.5 / 9.2 / **23.5** |
| Basic Materials | 1.0 | INFLOW | 10.6 / 29.0 / 35.7 / 15.5 / **18.3** |
| Utilities | 1.0 | INFLOW | 22.1 / 20.3 / 38.3 / 9.8 / **3.6** |
| **Industrials** | 0.8 | **OUTFLOW** | −5.3 / +33.5 / **−68.7 / −125.4 / −194.0** |
| Consumer Cyclical | 0.6 | ROTATING | +311.1 / +307.7 / +154.7 / **−3,043.2 / −672.7** |

**Industrials is the cleanest signal on the board** — three consecutive accelerating outflow days — but no C12-passing single-name short surfaced; it reads as breadth-driven. **Consumer Cyclical is the opposite case**: the tool's own label is ROTATING and the 0.6 score is propped up by three stale positive days while the last two sessions flipped hard negative. That is a **2-day reversal that fails the ≥3-day hard rule** — watch-only, and this matters because TSLA's scored sector component rests on it (§7).

⚠ **Unreconciled tool conflict, flagged not resolved.** `uw options-flow sector-flow` reports Technology **+$966.7M inflow** today; `uw risk market-regime`'s own `sector_rotation` block reports Technology **−$392.5M outflow** on the same session. Two different definitions. The `sector-flow` + `sector-flow-persistence` pair is weighted primary (corroborated across five consecutive same-sign days and consistent with the single-name screener); the `market-regime` figure is a single opaque number with no visible methodology.

**Technology is bifurcated, and that is the day's real story:** the bullish leg is mega-cap software/platform (AAPL +$31M, MSFT +$13M, PLTR +$7M, IBM +$6M, CBRS +$7M) while **semis sell off inside the same "Technology inflow" headline** (AMD −$41M, TSM −$33M, INTC −$23M, NBIS −$29M, AVGO −$13M, NVDA −$11M). Financial Services' "inflow" is crypto-proxy driven (MSTR +$40M, WULF +$19M) with no conventional bank in the top-25 — treat that label with caution.

**ETF flow tape (advisory — instrument layer the GICS aggregates cannot see):**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| **SMH** | inflow +$106.2M (#1) | BULLISH (5d) | top print $50.4M below-mid (sell-leaning) | **fresh large PUT sweeps: $55.5M / $43.2M / $37.3M at 527.5–535, 07-31** | agree on 5d, **same-day reversal — caution** | n/a (thematic) |
| **IGV** | inflow +$17.2M (#2) | BULLISH | — | **confirming**: $19.3M ask-side call sweep, $88 strike, 1,138 trades, 07-31 | **agree — high conviction** | n/a |
| **XLY** | inflow +$15.1M (#3) | BULLISH | $30.6M near mid, neutral | thin, no urgency | **DISAGREE** (GICS Cons. Cyc. −$672.7M) | watch-only |
| **XLE** | outflow −$16.1M (#21) | BEARISH | $23.8M above mid (mild buy-lean) | modest small put buying | **DISAGREE** (GICS Energy clean inflow) | downgrade Energy to caution |
| **EWY** | outflow −$8.0M (#20) | MIXED | $89.2M below mid near close | scattered small puts | n/a (geographic) | appendix-only |
| **XBI** | outflow −$5.7M (#19) | BEARISH | mixed-sign | small, mixed | **DISAGREE** (GICS Healthcare inflow) | Healthcare inflow is large-cap pharma, **not** biotech |

Rank-only: XLK +1.9M · GDX +1.5M · XOP +1.4M · XLU +0.30M · XLV +0.29M · XLRE +0.24M · XLP +0.18M · EWT +0.15M · KRE +0.10M · ITB −5.7K · XLB −0.29M · XLF −2.2M · XLC −1.1M · XLI −3.1M · TAN −0.54M.

**Three of the four standout-inflow sectors have their representative ETF disagreeing on direction.** Only Technology gets genuine two-instrument confirmation (IGV agrees cleanly; SMH agrees on the 5-day window but flips bearish intraday). This materially weakens Energy and the biotech leg of Healthcare. The tape is **advisory** — it strengthens the conditional sector-leader +1 via `gics_agreement` and cum-flow alignment; it adds **no rubric points**.

**Conditional sector-leader +1 — only two names clear all three gates:**

| Name | Sector | (a) persistence ≥0.6 | cum_flow_30d | (b) aligned | (c) ≥$50M | Result |
|---|---|---|---|---|---|---|
| **IBM** (long) | Technology | 1.0 ✓ | +$61.8M | ✓ | ✓ | **PASS** |
| **TSLA** (short) | Cons. Cyclical | 0.6 ✓ | −$562.4M | ✓ | ✓ | **PASS** |
| AAPL | Technology | 1.0 ✓ | +$37.0M | ✓ | ✗ | FAIL (c) |
| MSFT | Technology | 1.0 ✓ | −$619.6M | ✗ | — | FAIL (b) |
| PLTR | Technology | 1.0 ✓ | −$232.9M | ✗ | — | FAIL (b) |
| MSTR | Fin. Services | 1.0 ✓ | −$416.3M | ✗ | — | FAIL (b) |
| WULF | Fin. Services | 1.0 ✓ | −$49.7M | ✗ | — | FAIL (b) |
| HUT | Fin. Services | 1.0 ✓ | −$12.8M | ✗ | — | FAIL (b) |
| SMMT | Healthcare | 1.0 ✓ | +$8.4M | ✓ | ✗ | FAIL (c) |
| LLY | Healthcare | 1.0 ✓ | +$25.5M | ✓ | ✗ | FAIL (c) |
| XOM | Energy | 1.0 ✓ | +$19.3M | ✓ | ✗ | FAIL (c) |
| LULU (short) | Cons. Cyclical | 0.6 ✓ | +$42.9M | ✗ | — | FAIL (b) |

All three Financial Services "leaders" fail on 30-day alignment despite today's positive print — that sector's inflow is a short-horizon reversal, not sustained accumulation.

---

## 3. Swing Setups (1–6 weeks)

### 3a. Long swings (regime-aligned)

**EMPTY.** No long cleared the confluence gate with a positive post-gate size.

`accumulation-hunter` returned a **null board** — no ticker reached three aligned signals with institutional-tier DP confirmation, uncontaminated timestamps, and a coherent OI direction. The kill mechanism today was specific and worth recording:

> **Market-wide closing-cross contamination.** The `uw dark-pool largest` tape is dominated by prints clustered **20:00:11Z–20:11:30Z** at or near closing-cross prices with wide/stale NBBO (JNJ's cross prints show bid 259.40 vs ask 263.91 — a $4.50 spread on a $263 stock). This hit SPY, QQQ, MU, SNDK, VOO, GOOGL, MSFT, NVDA, IVV, LRCX and JNJ simultaneously. **GOOGL ($288.5M), MSFT ($286.0M), LRCX ($231.5M) and NVDA ($207.0M) share the identical timestamp `20:09:02Z`** — a synchronized basket/index execution, not four independent institutions. **QQQ shows a literal twin-print artifact:** two 250,000-share, $171,059,700 trades at the identical timestamp `20:10:58Z`.

**JNJ** came closest and still failed: `institutional-accumulation` flagged ACCUMULATION (buy/sell 2.54, $273.9M DP premium) and mega-tier buy_ratio was 1.00 — but **two of the three mega prints ($41.8M of $51.85M, ~81%) are closing-cross prints**, leaving one genuine $10.06M print. `smart-positioning` reads majority *bearish*, cum_flow_30d is +$7.68M (MIXED, far below the $50M conjunction threshold), and a **C28 `distribution_flag` fired**: `JNJ260918C00270000` shed **−5,526 contracts of OI on 6,646 volume** (~$3.75M prior-session premium). A call being closed while the desk reads "accumulation" is a direct contradiction.

Also dropped: **SMMT** (confluence 6, but highest DP tier is "block" not mega, $5.0M total — sub-scale), **UBER** (institutional-accumulation NEUTRAL, mega tier 100% *sell*, cum_flow_30d −$28.1M — this is distribution), **AAPL/GOOGL/MSFT** (all NEUTRAL on accumulation; their biggest prints sit inside the 20:09:02Z basket window; cum_flow_30d +$37.0M / −$29.7M / −$619.6M).

### 3b. Short / fade swings (defined risk only)

**EMPTY — one name reached the table and gated to watch-only.**

**TSLA — SHORT — raw_score 3 (LOW) → WATCH-ONLY**
Spot 313.03 (−2.08% today, **−17.81% over 5 sessions**). The move is concentrated: 374.01 (07-22) → 319.69 (07-23) → 313.03 (07-24), i.e. **−16.3% in two sessions**, tied to the broad AI-capex unwind.
- *Score:* +1 conditional sector-leader · +1 cum-flow accretion (−$562.4M, 8.6× union median) · +1 oi-trend BUILDING.
- *Fundamentals:* **CONFIRM.** Last print (2026-06-30) **missed by −35.3%** ($0.33 vs $0.5103 est). EPS −37.66% YoY against revenue +11.75% YoY = genuine margin compression (net margin 3.67%, op 4.22%). PE 308.9. Insider MSPR 3mo −45.35, net selling. **Next earnings 2026-10-20 — 88 days out, no catalyst inside any swing horizon.**
- *Debate:* bull 0.42 / bear 0.40 — **the disconfirming side wins, gate fires.** The bear conceded five of eight counter-points outright (move already realised, no catalyst for 88 days, beta 1.84 into a rotation not a risk-off, FOMC at T+3, and the fleet's own audits: 2026-06-27 "no short alpha-sizing anywhere" with HIGH tier realised 0.143; 2026-07-18 broad short direction −7.2pp pooled / −26.7pp uptrend / −22.7pp pullback over 394 decided calls).
- *Scoring-integrity flag:* one of the three score components rests on a 2-day Consumer Cyclical reversal that **fails sector-rotation's own ≥3-day persistence rule**. If Monday's sector flow prints positive, raw drops to 2 — below the LOW floor.
- **Invalidation (C34, real DP level):** institutional supply sits **overhead** at 378.93 ($851.8M / 101 trades), 374.01 and 369.57. Below spot there is only a thin shelf at **308–310** ($14–27M per level) — 10–20× lighter — and **no institutional footprint at all between 313 and 369**. Invalidation: **daily close back above ~$326**, reclaiming the 319.69–325.86 DP node.
- *Final:* **watch-only.** Panic gate −1 (SPY front-end 1.429 > 1.10), event-risk gate −1 (FOMC T+3), debate gate −1.

**Near-term sweep ledger (informational — `sweep-persistence` earns 0 rubric points):**

| Ticker | Side | 5d sweep premium | Persistence | OI-confirmed opening | Note |
|---|---|---|---|---|---|
| **SMH** | bearish | $515.9M | 3 of 5 | **yes** — ΔOI +101,377, 5 straight build days, top adds both PUTS (K532.5 +15,751, K527.5 +15,735, 7DTE) | the only name surviving every filter |
| **SNDK** | tool says *bullish* (5/5) — **tape says bearish** | $1.78B | 5 of 5 | yes — ΔOI +25,508, top adds PUTS | label broke today: −$98.1M net, −10.79% (worst S&P mover) |
| **NBIS** | tool says *bullish* (4/5) — **tape says bearish** | $915.5M | 4 of 5 | yes — ΔOI +34,781, top adds PUTS (K170 +5,055) | matches the $32.65M K170 whale almost exactly |
| MU | mixed direction over window | — | 5/5 sessions, **no clean direction** | yes — ΔOI +113,254, put-led (largest of cohort) | today's cleanest OI-confirmed bearish flow; not a persistence story |
| BE | bearish | — | 2 of 5 (below bar) | yes — ΔOI +38,585, **one strike carries +21,366** (K105 7DTE) | watch for a third bearish day |

**The most important sweep finding is not the ranking — it is that three names (SNDK, NBIS, GOOGL) show multi-day sweep persistence in one direction being overrun by same-session reversals with OI and whale confirmation on the other side.** That is persistence *breaking in real time*.

Mega-cap/index names (SPXW, QQQ, SPY, NVDA, META, MSFT, GOOGL, AMZN) were demoted to footnote by the hedge-flow filter: `cum_premium_flow --days 30` returned `trend_direction: MIXED` for **every one**, and MIXED can never satisfy the alignment check. The SPX/QQQ/SPY 5-of-5 "bearish persistence" is a standing institutional hedge book (2027–2028-dated collar/skew structures), not momentum.

---

## 4. LEAP Builds (6–24 months)

**EMPTY — zero of nine candidates cleared 6-of-9 gates.** With LEAPs at **2.1% of the tape** and a rising-10Y backdrop, this is the expected answer.

**Disqualified on the accretion gate (90d cum-flow flat or wrong-direction):** NFLX (−$283.8M / 30d −$156.4M — the Dec-2028 75C/75P pair looked like a risk-reversal but the put leg was *sold*), AAL (−$58.6M; the Dec-2028 $10C add showed prev_bid 7,203 ≫ prev_ask 5 = a call *seller*, i.e. covered-call financing), WBD (−$23.6M, plus merger/spinoff overhang), SOFI (−$57.2M). **NOK** ($32 strike, 250% OTM, bid 8,911 ≫ ask 862 = seller) and **JBLU** ($4 put, 100% bid-side) disqualified on flow direction. **EOSE** failed C12 outright (spot $3.47). **TLT**'s large far-dated $80P build (693 DTE, +11,092 OI) is a genuine rates hedge consistent with the rising-10Y macro line, but conviction-matrix returns MIXED at 3.4% — directionally bearish-on-TLT, not a long thesis this lane scores.

All five Step-0 watchlist OI shifts (SMH, AMD, NBIS, UBER, JNJ) were checked directly: **every one is 0–35 DTE**, zero long-dated content.

**Near-miss — CVNA, 5 of 9 → DISQUALIFY.** A Mar-2027 $60C (238 DTE) went from **36 to 7,520 OI (+20,789%)**, ask-dominant ~2.5×, with $25.8M DP premium clustered tightly $60.04–$60.64 (buy/sell 1.8×) and cum_flow +$69.1M/30d. But: (1) **oi-trend fails** — walking all ten days, that contract *never appears before today*; the aggregate `consecutive_build_days=10` is driven by 0–7 DTE churn, and the other long-dated contracts on prior days are different strikes, mixed calls and puts, all <900 contracts. This is a single-session spike, not a ladder. (2) **conviction-matrix fails** — BULLISH_ACCUMULATION at **14.3%**, not DIRECTIONAL_LONG >70. (3) **Decisive: CVNA reports earnings 2026-07-29, five days out.** A same-day 20,789% OI spike in a 238-DTE ATM call five days before a print is an earnings/gamma play wrapped in LEAP tenor, not a 6–24 month conviction build.

---

## 5. Volatility Surface

**Substrate hygiene first — and it changed the answer.** Raw `iv-term-structure` returned **BACKWARDATION on 39 of 41 scanned names**, mechanically. Re-deriving per name (dropping the 0DTE/expired bucket and any tenor with <15 contracts) **flipped 14 of 41 to CONTANGO** — the raw label was pure 0DTE-wing noise. `front-end-iv-ratio` at its default `near-dte=1` is unusable (ratios 2.3–8.7 driven by `near_dte_actual: 0`); all figures below use a hygiene-adjusted `near-dte=7`.

⚠ **All `iv-percentile-zscore` readings are PROVISIONAL.** Every candidate returned `dates_used: 72` against a requested 252-day lookback — below the ≥120-day threshold for a first-class claim.

⚠ **No win-rate or edge claim is attached to anything in this section.** `earnings_vol` and `high_iv_rank` are Benjamini-Hochberg-confirmed **false positives** across five consecutive audits (claimed ~0.88 → realised 0.35–0.38). These are structural observations only.

**KINKED (genuine local-max hump surviving the hygiene filter):**

| Ticker | Kink expiry | Magnitude | Likely cause | iv_pctl / z (n=72) | VRP ref | Bias | Scored |
|---|---|---|---|---|---|---|---|
| **AKAM** | 2026-08-07 | 63.4% → 105.1% (+65.9% rel), then decays | **Name-specific** — earnings 08-06 matches the kink tenor | 98.61 / 1.89 | QQQ (cheap) | BUY VOL front | **+1** |
| **SOXL** | 2026-08-21 | 28d 226.4% vs 21d 202.6% / 35d 195.8% (31k+ contracts) | **Sector** — semis earnings cluster at Aug OPEX | 90.28 / 1.21 | QQQ | BUY VOL | **+1** |
| **SOXX** | 2026-08-21 | 28d 70.5% vs 68.3% / 66.3% | Same sector cluster | 95.83 / 1.25 | QQQ | BUY VOL | **+1** (internal tension: a secondary front-rich leg argues sell-vol on the very front) |
| **IREN** | 2026-08-21 | 28d 132.4% vs 127.3% / 130.0% — marginal | Same cluster; the cross-name corroboration is the real signal | 93.06 / 1.73 | QQQ | BUY VOL | **+1** |
| DELL | 2026-09-18 | 56d 100.3% vs 35d 83.9% / 84d 88.4% | **Ambiguous** — no confirmed catalyst; Sep-18 is monthly OPEX | 79.17 / 0.82 | QQQ | — | **0 — withheld** |

**BACKWARDATION (monotonic front-rich decay, hygiene-clean):**

| Ticker | Cause | iv_pctl / z | front-end(7,30) | VRP ref | Bias | Scored |
|---|---|---|---|---|---|---|
| **BE** | earnings 07-28 PM (4d) | 93.06 / 2.08 | 1.434 | SPY (rich) | SELL VOL | **+1** — largest front dislocation on the board (246.97% at 7d) |
| **VLO** | earnings 07-30 AM (6d) | 88.89 / 1.41 | 1.230 | SPY (rich) | SELL VOL | **+1** |
| **BSX** | earnings 07-29 AM — **on FOMC decision day** | 98.61 / 1.70 | 1.496 | SPY (rich) | SELL VOL | **+1**, compounded-event caveat |
| **FSLR** | earnings 07-30 PM (6d) | 100 / 1.56 | 1.169 | SPY (rich) | SELL VOL | **+1** |
| FTNT | earnings 07-29 PM — **on FOMC presser day** | 97.22 / 1.74 | 1.551 | QQQ (**cheap**) | structure says sell, regime says buy | **0 — VRP conflict** |

**"No near-dated tenor" — the RMBS class, NOT calm:** **WHR, DIOD, LDOS, COHU** all return `front_end_iv_ratio = 1.000 FLAT`, but only because no tenor under 28 DTE cleared the 15-contract floor (WHR's own earnings is three days out and there is *still* no liquid near-dated bucket). Post-filter these are smooth monotonic decay with no tradable front-end concavity. Not surfaced.

**IV outliers:** all 20 rows from `options-flow iv-outliers` are same-day 0DTE. Two are size-worthy — **SOXL 160P** ($1.68M premium, 904 vol) and **SOXL 180P** ($752K, 199 vol) — and read as same-day tactical hedging layered on the Aug-21 sector kink. The rest (ODD, PYPL, RR, XLF, GRAB, MPT, KWEB, ALT, HTZ, PURR, BBAI) are sub-$330K on deep-OTM penny-strike contracts with `max_iv` >400–2000% pulling the average — mechanical wide-spread artifacts.

**Vol-regime read.** SPY and QQQ **disagree in VRP sign** (+0.0177 vs −0.0138) while *both* books are fully short gamma. A short-gamma book paired with a positive SPY VRP is the genuine tension: dealers should be adding fuel to realised vol, yet SPY implied isn't pricing much premium over that risk. The desk read: **size SPY-side short-gamma exposure down** (vol fair-to-rich against a book that can accelerate), and **leave room to own convexity on the Nasdaq/semis side** (negative QQQ VRP into a short-gamma book is a cleaner "vol is cheap and the plumbing wants to move" setup — consistent with the SOXL/SOXX/IREN Aug-21 cluster). Note that the earnings cluster lands *inside* FOMC week (BE 07-28, FTNT+BSX 07-29, FSLR/VLO/COHU 07-30), so front-end IV across nearly the whole surviving universe is real name-specific event premium — **and the clean "macro-only calendar-spread candidate" bucket came back empty.**

**Rejected as efficiently priced or unclassifiable:** AAPL, MSFT, AMZN (earnings 5–6 days out but flipped CONTANGO post-filter — catalyst present, no structural mispricing); VRTX, SNDK, AMD, NBIS, WULF (same); MU, TSLA, SMH, MSTR, GOOGL (flipped CONTANGO, no earnings match at all — raw BACKWARDATION was pure 0DTE artifact); ENS, ADNT, EEFT, EQR, SNEX, WK, BAND, KGS (0–1 surviving thick tenors, cannot classify).

---

## 6. Risk & Correlation

**Macro headline:** curve normal (+0.36); core CPI 2.81% / core PCE 3.41% both still above target; 10Y 4.71% rising +21bp/30d; USD strengthening; payrolls +57k. **Forward stack: FOMC T+3 · Core PCE T+5 · NFP T+10 · CPI T+13.** Monday 07-27 is the only clean pre-FOMC session.

**Panic gate is LIVE and book-wide.** SPY front-end IV ratio **1.429**, QQQ **1.421** — both above the 1.10 threshold → **−1 tier on every call, no exceptions.**

**Correlation clusters** (`uw risk portfolio-correlation` on today's nine candidates):

| Pair | Corr | Classification |
|---|---|---|
| **MU / SMH** | **0.854** | **Cluster** (`AI_semis_cluster`) — one position. Moot: both already DROP |
| BE / SMH | 0.699 | soft watch (0.001 below the mechanical line — no discretionary upgrade) |
| FSLR / SMH | 0.654 | soft watch |
| NBIS / SMH | 0.651 | soft watch |
| IWM / SMH | 0.649 | soft watch |
| BE / NBIS | 0.620 | soft watch |

The semis / AI-infra complex (MU · NBIS · SMH · BE · IREN, with SOXL · SOXX · SNDK · AMD alongside) is functionally **one unwinding position**. No ≥0.70 pair touches the three LOW names, so no cluster deduction applied to TSLA/AKAM/FSLR.

**Fundamentals verdicts (top-5):** TSLA **CONFIRM** · AKAM **CONFIRM** · FSLR **CONFIRM** · **BE CAUTION (−1 tier)** · IREN **CONFIRM**. Zero VETOs.
The one flag — **BE** — is the inverse of the usual pattern this gate catches. Bearish flow (a $5.53M Tier-1 opening floor put, −$59.6M net premium) is riding into a name whose fundamentals and sell-side just turned *more* supportive: a 4-of-4 EPS beat streak, revenue +56.5% YoY, and **JPMorgan raising its PT to $346 from $267 (Overweight) on 07-21, three days before the −14.9% drop**. The decline reads as broad AI-infra sympathy (same session: NBIS −15.0%, SOXL −13.1%, MU −7.0%, WDC −6.9%) rather than a BE-specific break. With earnings landing 07-28 postmarket — the night before FOMC day 1 — a beat consistent with that streak is a violent squeeze setup against any short-vol structure. Balance-sheet counterweight: **D/E 3.73**, net margin 0.25%, ROE 0.82%.

**Event-risk flags:** BE earnings T+2 (night before FOMC) · FSLR earnings T+4 (day after the presser, day before PCE) · BSX and FTNT earnings **on FOMC day itself** · CVNA earnings T+3 · AKAM earnings T+9 (its short leg expires 08-07, **the NFP date**).

**Debate-disconfirmation cuts — the gate fired on all three LOW names:**

| Ticker | Proponent | Disconfirmer | Gate |
|---|---|---|---|
| TSLA | bear 0.40 | bull **0.42** | **FIRES** |
| AKAM | bear 0.45 | bull **0.60** | **FIRES** |
| FSLR | bear 0.40 | bull **0.70** | **FIRES** (widest margin on the board) |
| BE | bear 0.65 | bull 0.58 | does not fire on residuals — **but both sides concluded SKIP** |

No pair was within one bin *and* ≥0.75, so no round-2 escalation. Both vol debates converged on the same objection, which the for-the-trade side conceded it could not rebut: `earnings_vol` is a BH-confirmed false positive across five consecutive audits. Additionally AKAM's short leg carries **only 72 contracts** of OI (flanks hold 337 and 411) — a fill-and-exit trap independent of whether the vol call is right — and FSLR's 9.6% implied move sits *below* its own most recent +17.5% surprise.

**Breadth cross-check (`fz`, advisory, 0 points):** 363 advancers / 140 decliners, **`pct_green` 72.17%**, avg change +0.77%, median +0.97%, top mover IP +11.21%, worst SNDK −10.79%. **This is a genuine divergence but the inverse of the usual distribution tell**: the *price* tape is broadly green while options-flow breadth is 33% bullish and SPY sits below both SMAs. Cross-referenced against cap-weighted index performance (QQQ −1.12%, RSP +0.78%), the correct read is a **rotation out of the AI/semis complex into the broad market**, not a low-quality bounce. Advisory — does not change sizing.

**Adverse-flow exits** (`uw watchlist alerts` + `scan` on `conviction_2026-07-23` = [MU]): three alerts — HIGH_IV_RANK 82.5, LARGE_DARK_POOL $452.0M single print (28,603 trades — **the known 20:00Z closing-cross mega-DP artifact class; do not trade it**), OI_SHIFT +113,254. Day flow bearish, net −$139.2M, P/C 1.23, price −6.99%. **No position to exit** (MU was watch-only). Verdict: keep MU watch-only; do not resurrect the short on one bearish day. A second consecutive bearish flow day post-FOMC reopens the conversation.

**Hedge sleeve:** mechanical trigger **not met** — the sized book is empty, net delta zero. Advisory for residual AI/semis exposure held outside this book: **do not buy front-week protection or VIX calls here** — front vol is precisely what is expensive (SPY 1.43× / QQQ 1.42× backwardation, VIX 18.58 already spiking). Prefer **Aug-21 QQQ or SMH put debit verticals** (the lower short strike sells back part of the inflated IV), half-size per regime guidance, entered Monday 07-27. Short-gamma dealers on both index books mean any FOMC surprise gets amplified — defined-risk is the only acceptable format this week.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**EMPTY. Zero names reached raw_score ≥ 7.** Board: **0 HIGH / 0 MEDIUM / 3 LOW** (all starter pre-risk, all watch-only post-gate). Step 3a load-bearing-tool gate: N/A — nothing reached ≥9. Step 6.5 `uw playbook batch-scan` was **skipped** — it operates on the raw_score ≥ 7 list, which is empty. Step 8.5 deep-dive hand-off **skipped** — no HIGH-tier names.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no calls were sized today, so no per-tier expectancy is generated. Standing context from the most recent audit (2026-07-18): **DROP 43.3% > traded book 41.1% > sized 38.6%** — the DROP pile continues to outperform the traded book, and HIGH-tier realised 0.143 across the prior three audits (tier inversion, regime-invariant).

**Full LOW-tier detail (the three names that reached the table):**

| | TSLA | AKAM | FSLR |
|---|---|---|---|
| Direction | short | vol (calendar) | vol (calendar) |
| raw_score | 3 | 3 | 3 |
| Components | +1 sector-leader · +1 cum-flow · +1 oi BUILDING | +1 earnings SELL VOL · +1 vol-surface KINKED · +1 oi BUILDING | +1 earnings CALENDAR · +1 vol-surface BACKWARDATION · +1 oi BUILDING |
| dominant_signal_class | `sector_rotation` | `earnings_vol` | `earnings_vol` |
| cum_flow 30d / 90d | −$562.4M / n.p. | −$10.1M / −$9.6M | +$4.8M / +$25.1M |
| win_rate (n, source) | null — **NA(substrate)** | null — **NA(substrate)** | null — **NA(substrate)** |
| market_excess | n/a | n/a | n/a |
| pre-risk size | starter | starter | starter |
| fundamentals | CONFIRM | CONFIRM | CONFIRM |
| debate (proponent/disconfirmer) | 0.40 / **0.42** | 0.45 / **0.60** | 0.40 / **0.70** |
| Gates applied | panic −1 · event_risk −1 · debate −1 | panic −1 · debate −1 | panic −1 · debate −1 |
| **final size** | **watch-only** | **watch-only** | **watch-only** |
| Invalidation | close > ~$326 (reclaims the 319.69–325.86 DP node) | 08-07 tenor premium fails to compress by 08-01; or the 72-contract leg cannot be exited | front-end ratio compresses under ~1.08 pre-07-30; or a >5% pre-print move on FOMC/PCE |

**Substrate coverage gap, stated plainly.** `uw historical signal-backtest` supports only five classes (`bullish_flow`, `bearish_flow`, `high_iv_rank`, `volume_spike`, `dark_pool_accumulation`). None of today's dominant classes except `bearish_flow` are backtestable, so **17 of 20 scored rows carry an honest `NA(substrate)`**. The single clean number: class **`bearish_flow` WR 0.6087, n=138 kept** (12 clamped rows dropped under the P0.3 clean-query protocol; headline 62.7% deliberately *not* quoted), against a same-window SPY-short benchmark of 0.5652 → **market-excess +4.35pp**. That is the **seventh consecutive positive `bearish_flow` read that earns 0 rubric points** (C19 accrual item — the down-tape edge remains unscoreable by the long-biased frozen rubric).

**Two audit flags carried forward from this run:**
1. **`+1 oi-trend BUILDING` fired on 16 of 16 names pulled — zero discrimination.** Applied verbatim under the freeze, but it corroborates registered criterion C47. Recommend the next audit pre-register an activity-normalised variant (net ΔOI / total OI).
2. **New artifact candidate — un-split-adjusted strike grid.** Multiple long-dated single-leg "puts" carry strikes 2–4× spot: TSLA K760 vs spot 310.10 (875 DTE), NOW K208 vs 98.35, INTU K740 vs 295.13, ISRG K560 vs 338.70, LULU K280 vs 114.83, MSTR K390 vs 92.29, NFLX K120 vs 70.22. `multileg-strategist` confirmed the mechanism on **LULU 261218 P300**, which prices at **$185.64 against intrinsic $185.72 — exactly parity**, i.e. a deep-ITM synthetic against a stale pre-split grid, not a directional put build. Do not read these as bearish conviction.

<details>
<summary><strong>Conviction-scoring rubric — version <code>2026-06-12</code> (FROZEN), embedded verbatim for audit</strong></summary>

```
Daily conviction score = Σ:
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna-squeeze setup in trade direction — the trigger must be a verified SIGN CHANGE, not a level: sign(net_dex) on the latest session opposite to ≥3 consecutive prior sessions, read from dated `uw options-structure dex --date` calls (≥4 to verify the prior-session sign run; ~11 for the trailing-median floor), with |net_dex| on the flip day ≥ 0.25× the trailing-10-session median |net_dex|; the evidence string must cite both dated values. Vanna disjunct additionally requires a dated VIX source (Yahoo chart API ^VIX) for the falling-VIX leg — no out-of-band VIX fills.
  +3  3+ aligned signals in accumulation-hunter (DP + OI + uw oi smart-positioning, uw dark-pool block-stratified institutional-tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms (sign aligned with thesis AND |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1. A sub-$50M flow that halves this line does not separately qualify as "net directional accretion" for the +1 cum_flow line.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL ONLY: award +1 only when dominant_signal_class == leap_directional; in all non-LEAP contexts contribution is 0.
  +1  uw historical cumulative-premium-flow shows net directional accretion in trade direction (30d window) — INTENT-SCREENED: award only when (a) no C28 distribution_flag present on the name, AND (b) on dividend payers inside an ex-div window, the accreting prints are NOT deep-ITM sub-parity calls. Screen failed or unevaluated on a flagged name → 0.
  # +2 line for uw insights signal-confluence ≥4 REMOVED 2026-06-12 audit P0.2
  # +1 line for uw hot-chains sweep-persistence top-5 REMOVED 2026-05-23 audit P0.3
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector — CONDITIONAL: award +1 only when (a) sector persistence_score ≥ 0.6 AND (b) cum_premium_flow_30d direction aligned with thesis direction AND (c) |cum_flow_30d| ≥ $50M. Default 0.
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising uw historical pc-ratio-zscore (VRP positive) — an INFORMED-FLOW CONTINUATION penalty, not a "crowd is wrong, fade it" signal.
  -3  flow_conflict — applied mechanically when cum_premium_flow 30d direction is clearly opposite dominant_signal_class (signed-sum sign flip + magnitude > today's union-median |cum_flow_30d|, or explicit OPPOSITE label)
  -1  flow_conflict_lite — the 30d cum_premium_flow read is MIXED (signed sum near zero, or aligned but bottom-quartile magnitude in today's union)
      (flow_conflict and flow_conflict_lite are MUTUALLY EXCLUSIVE — apply ONE, never both)
  # The two lines below are TIER GATES applied by risk-monitor in Step 2d. They contribute 0 to raw_score
  # and never appear in score_components.
  -1  [TIER GATE] risk-monitor flags in correlation cluster (pairwise corr ≥ 0.70) — −1 TIER
  -3  [TIER GATE] uw risk market-regime conflicts with trade direction — −1 TIER (regime gate)
  # gamma-flip-tracker 0DTE breakout setup removed from swing/LEAP scoring 2026-05-09 (§2 is advisory, 0 points)
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | HIGH | full size (subject to Step 3a load-bearing gate + Step 5 win-rate gate) |
| 7 – 8 | MEDIUM | half size (subject to Step 5 win-rate gate) |
| 3 – 6 | LOW | starter / watch-only |
| ≤ 2 | drop | filtered by the quant's drop floor |

**Tier-cut status (2026-06-12):** the ≥9 HIGH cut **failed its scheduled re-confirmation** — bands inverted on the first post-UPTREND window (HIGH 0.222 / MED 0.214 / LOW 0.444). The cuts are retained under the P0.1 freeze but carry **no validated ranking claim**; the P0.6 out-of-regime guard caps all sizing at half in the interim.

</details>

---

## 8. Watch-only — single signal, no confluence

Candidates surfaced by exactly one Phase 1 agent (failing the ≥2-agent confluence gate), or caught by a false-positive control. **For journaling, not for entry.**

| Ticker | Raw | Components | Class | cum_flow 30d / 90d | Note |
|---|---|---|---|---|---|
| **IBM** | 3 | +1 sector-leader (Tech 1.0, +$61.8M, ≥$50M) · +1 cum-flow · +1 oi BUILDING | `sector_rotation` | +$61.8M / n.p. | The only single-agent name at 3 — would be LOW if a second agent confirmed |
| SOXL | 2 | +1 vol KINKED 08-21 · +1 oi BUILDING | `earnings_vol` (cluster) | −$405.9M / −$678.0M | Aug-21 semis-kink cluster leg |
| SOXX | 2 | +1 vol KINKED · +1 oi BUILDING | `earnings_vol` (cluster) | +$30.6M / +$89.2M | Internal front-rich tension noted |
| VLO | 2 | +1 vol BACKWARDATION · +1 oi BUILDING | `earnings_vol` | +$4.1M / −$36.9M | Earnings 07-30 AM; +18% today = post-reaction IV |
| BSX | 2 | +1 vol BACKWARDATION · +1 oi BUILDING | `earnings_vol` | +$13.3M / +$14.5M | earnings-scout **SKIPPED** — 07-29 is FOMC decision day, premium unattributable |
| CVNA | 2 | +1 cum-flow · +1 oi BUILDING | `leap_directional` | +$69.1M / +$47.7M | LEAP gate 5-of-9 DISQUALIFY; earnings 07-29 |
| ORCL | 2 | +1 cum-flow (−$243.5M, 3.7× median) · +1 oi BUILDING | `bearish_flow` | −$243.5M / −$492.6M | C4 opening gate unverified → would cap half if ever scored |
| SNDK | 1 | +1 oi BUILDING only | `multi_day_sweep` (broken) | +$785.4M / +$2,192.5M | Worst S&P mover; cum-flow +1 **not** awarded — the flagging thesis broke, no direction to align to |
| AAPL | 1 | +1 oi BUILDING only | `oi_build` | +$37.0M / n.p. | Sector conditional fails (c); dealer LONG tilt unscored |
| **MSTR** | 0 | none — **false-positive control CATCH** | — | −$416.3M / n.p. | Headline +$40.3M bullish, but 07-23 smart-positioning **inverts** it: C97.5 *sold* (bid 14,750 vs ask 3,642, +18,188 OI), C103 *bought* (ask 12,082 vs bid 3,084, +17,804 OI) = a bear call spread / covered-call overwrite, not a bullish build |
| **WULF** | 0 | none — control #3 | — | −$49.7M / n.p. | Legs from different data vintages, not cleanly inferable into one package |

**Structures explicitly rejected by `multileg-strategist` (recorded so they are not re-surfaced tomorrow):**
- **INTC 260727 C79/C80, $141.1M** — the single largest multileg premium on the board. Deep-ITM $1-wide spread, legs $17.29/$16.30 = **net $0.99 on a $1.00 width** (~1% over 3 days), **OI 0 and 35** against 41,824/42,212 volume, sitting in the vol trough. **Financing flow, zero directional information.**
- **SPX conversions / boxes / jelly rolls** — 260821 C7000 + P8000, 260918 C7450 + P7450, plus 261016/261120/281215 quartets. **SPX 261218 C400 and 270115 C400 print $217,910,355 and $217,900,933 on identical volume (311)** — a deep-ITM jelly roll *and* a twin-print flag.
- **Confirmed twin-print NBBO artifact:** SPX 281215 C7000, 18:05:20, size 500, $76,024,500 — appears **twice, byte-identical**. Deduplicated; would otherwise have doubled apparent size.
- **LQD / HYG / TLT** ladders — IV 1.8–9.9%, ~$0.28/contract on 40–50k volume, ml ratio ~1.0: dealer-hedge-shaped.
- **Event hedges** (expiry brackets 07-29): SPY 260731 P740/P715 + 260918 P660 tail; QQQ 260731 P695 ($49.8M); IWM 260727 P290 / 260731 P283/P285; the whole SMH 07-31 complex.
- **Split-grid artifacts:** LULU 261218 P300/P350 ($70.5M/$62.7M, priced at parity); BE 260807 P192.5 (OI **1** vs volume 20,292, $30.94/share against $7.61 intrinsic); SNDK 260731/260724 C1000 deep-ITM calendar roll.
- **WEN 260814 P7.5/P6.5** — C12 *passes* ($6.99, ADV $169.2M) and the vertical is coherent, but repeat_count 1 with no aligned whale, term structure too thin to anchor (08-14 n=99), and its 0DTE companion P8 prints **below intrinsic** ($0.92 vs $1.01) — the sub-parity arb artifact class.

**The one structure that did earn the +2 — and still dropped:** **IWM 260821 P279/P277** debit put vertical ($12.10M + $12.85M, ~$0.31–0.80 debit on a $2.00 width, 28 DTE). A genuine 3-session programme (07-20 P278 28,046 → 07-22 P287 40,801 → 07-24 P277/P279, **strikes re-struck lower as the tape fell**), OI-confirmed opening (+24,765 ask-skewed on 07-23), and term-structure-anchored: the 08-21 tenor sits at 21.1% (n=5,883) on the flat 20.5–21.7% plateau while the event bump is at **07-31, not 08-21** — so no event premium at the tenor traded. It still scored only **raw 2** after a −1 `flow_conflict_lite` and dropped at the floor. `multileg-strategist`'s own caveat is worth keeping: the 08-21 tranche sits at the *back* of a protection ladder (P/C **20.1** at 07-28, 503,478 puts at 07-31), and index-ETF shorts are this fleet's documented bleed (0-for-4 at HIGH conviction; the 2026-06-27 audit explicitly refuted "express bearish index-relative").

**Cross-cutting institutional read:** the most persistent structure this week is not on any single name — **VIX call ladders have printed four consecutive sessions** (07-21 C35 across Aug/Sep/Oct, ~330k contracts; 07-23 a Sep 45/65 **1×2 ratio call spread**, 100,738 × 200,166, C65 OI +199,001; 07-24 C20/C30/C35). Same week as the IWM and SMH put ladders. Non-directional in equity terms and ineligible for any rubric line, but it is the strongest evidence on the tape that today's multi-leg complex is a coordinated **protection bid into the 07-29 FOMC / 07-31 PCE stack**.

---

### Data-quality notes for the next `/calibration-audit`

1. **`fz screen` endpoint is returning synthetic tickers** (AABEO, AABSI, AACHC, AAAPL, AABBV — doubled-prefix artifacts). Both Step-0 `fz` lanes (squeeze, RS) graceful-skipped, and `fz_enrich` returned `upstream_gaps: [earnings, recom, short_interest, target_price]` on **all five** top-5 names — a total upstream-gap day, not partial. `fz breadth` was verified **sound** (real tickers, IP / SNDK match the `uw` tape). 0 rubric impact.
2. **`uw insights deep-dive`'s `yahoo_fundamentals` leg returned HTTP 401.** Finnhub enrichment was unaffected.
3. **Raw Yahoo chart API is healthy and 2026-anchored** — closes reconcile exactly against the `uw` screener (SMMT 13.66, BE 184.89, NBIS 187.77). Used for C12 dollar-ADV verification and all price context in this report.
4. **`uw screener volume-vs-average` produced zero usable names** — the entire top-25 was sub-$50M-ADV micro tickers (SAFT, CLIP, LVWR, HEEM, SMU2, FCBC, JPEM, SPEQW…), all purged by the C12 floor. **C12 exclusions today:** CBRG, VZLA (sub-$5); LXU ($8.6M ADV), UTI ($43.9M), NVCR ($33.9M), TRLV ($8.5M), DRV ($2.7M), REGL ($6.6M), TOPT ($10.4M), AIPO ($39.4M), KMPR ($35.9M), NGS ($5.5M), AGRO ($6.7M).
5. **`uw screener iv-rank` uses `--mode`, not `--direction`** — the documented flag in the command file is wrong.
6. **ZGL-grid artifact recurred** on IWM (regime label POSITIVE against negative `total_gex`, ZGL 33% from spot) and intermittently on SPY/QQQ (1-day POSITIVE blips 07-14/07-16/07-22 with ZGL snapping ~50% away from spot).
7. **Schema limitation — `debate_residuals` binning loses the gate signal at low confidence.** The envelope enum is `[0.55, 0.65, 0.75, 0.85, 0.95]`, with no bin below 0.55. Today's honest residuals were TSLA bull 0.42 / bear 0.40, AKAM bull 0.60 / bear 0.45, FSLR bull 0.70 / bear 0.40, BE bull 0.58 / bear 0.65. **TSLA's pair both floor to 0.55, erasing the 0.42 > 0.40 ordering that actually fired its debate gate** — an audit reading the envelope alone could not reproduce that cut. AKAM, FSLR and BE retain their ordering. Recommend the next audit pre-register a lower bin (0.35 and/or 0.45), or store the raw residual alongside the binned one.
8. **`uw historical vrp` requires `--symbol`** — it has no market-wide mode, so the Step-0 "VRP classification" is per-index (SPY and QQQ pulled separately), and those two disagreed in sign today.
