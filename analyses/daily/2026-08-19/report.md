# Daily Market Analysis — 2026-08-19

## Executive Summary

- **Regime + GEX state:** `TRANSITIONAL — mixed signals, reduce position size` on an intact `UPTREND` structure (SPY 769.06, above 20SMA 759.77 and 50SMA 749.84, −1.32% off the 90d high). The tape's real story is **breadth, not direction**: **RSP +1.04% > SPY +0.21% > QQQ −0.20%** — equal-weight beat cap-weight by 124bp, so this was a **broadening rotation, explicitly not a tech-led rally**. XLV **+3.51%** (5d +4.30%) led; XLK **−1.07%** (5d −2.76%) lagged. Flow breadth is the contrarian tell at **36.5% bullish** (2,303 of 6,314 tickers) while the independent `fz` price tape prints **56.66% green** (285 adv / 217 dec) — options flow is markedly more bearish than price. VIX 14.89 (−6.0% 1d, but **+2.34% 5d**). Netted sector flow **OUT of Communication Services (−$73.6M), Technology (−$59.1M), Industrials (−$36.5M)**; **INTO Consumer Cyclical (+$111.1M), Healthcare (+$103.3M), Consumer Defensive (+$17.7M)**.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** **SPY** — regime label POSITIVE but `total_gex` **−$303.2M** (a direct contradiction, graded on the total_gex sign), ZGL 356.12 is a garbage extrapolation vs spot 769.20 → `zgl_reliable: false`; call wall 775 (+0.75%), put wall 765 (−0.55%) — an unusually **tight bracket** around spot. **QQQ** — clean `FULLY_NEGATIVE`, `total_gex` −$560.6M, no ZGL, and the single most negative strike in the grid (**−$276.3M**) sits at **717, essentially at spot** — dealers are shortest gamma exactly where price is, with no cushion. Advisory, 0 rubric points — see §2.
- **Top swing build:** **None.** Nothing reached MEDIUM or HIGH. The highest score on the entire board was **3, against a HIGH cut of 9**.
- **Top LEAP candidate:** **None.** The LEAP book is empty — no candidate reached even **4 of 9** gates, and the 90d accretion gate bound on every single name.
- **Biggest risk:** not a position — it is the **event wall of 2026-08-26 to 08-28**, when **Core PCE**, **NVDA's Q2 FY27 print (AMC)**, and **Jackson Hole with Chair Warsh's first keynote** land inside 72 hours of each other. Any structure carried past Friday's OPEX inherits all three. The correlation book is unusually *benign* by comparison: **the AI-semis cluster that dominated the last two sessions did not persist** — today's tightest AI-adjacent pair is NVDA/QQQ at **0.676**, below the 0.70 line.

> **No edge today. Nothing is sized.** This is the **31st consecutive empty conviction board** — a figure **verified mechanically**, by globbing every `analyses/daily/*/decision.json` for a non-`skip`/`watch_only` `final_size`, not carried forward from prior prose. The last session that sized anything was **2026-07-07** (PEP full; BE/JNJ/MS/SCHW/GM/IBKR/STT/ELV starter). Note that the 08-17 and 08-18 reports claimed "22nd" and "23rd" respectively and **both were wrong** — sub-agent streak counts confabulate, and this run's own Phase 2 agents also reported "23rd". Always re-derive from the envelopes.
>
> The empty board is the designed output, not a failure — the DROP pile has out-realised the traded book across recent audit cycles. But a **31-session** drought is a materially different fact from a 24-session one, and it deserves scrutiny in its own right: either the market has offered no edge for six straight weeks, or the gate stack is mis-calibrated toward refusal. `/calibration-audit` should treat the true streak length as a first-class question.

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** `TRANSITIONAL — Mixed signals, reduce position size, wait for clarity`; trend `UPTREND`; guidance *"Half position sizes. Favor defined-risk strategies. Iron condors in range."* SPY 769.06, +2.78% 30d, above both SMAs.

The breadth picture is genuinely two-sided and worth separating carefully, because the two sources measure different things and **disagree in a way that matters**:

| Source | Measures | Reading |
|---|---|---|
| `uw risk market-regime.market_breadth` | **options-flow** breadth | **36.5% bullish** (2,303 bullish / 4,011 bearish tickers) |
| `fz breadth --group sector` (advisory) | **price** breadth | **56.66% green** (285 adv / 217 dec), avg +0.90%, median +0.38% |

Price breadth is healthy and confirms the broadening; **flow breadth is not**. There is no `divergence_flag` under the standing rule (that fires on green-index-with-`pct_green`<50, which did not happen), but a 20-point gap between price breadth and flow breadth is the honest headline of the day: **more stocks went up than down, while more tickers saw bearish premium than bullish.**

**Per-index gamma (current-state EOD book):**

| Index | Spot | Zero-gamma | `total_gex` | Regime label | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 769.20 | 356.12 ⚠ *rejected, >55% from spot* | **−$303.2M** | POSITIVE ⚠ *conflicts with total_gex* | 775 (+0.75%) | 765 (−0.55%) |
| QQQ | 716.30 | `null` (FULLY_NEGATIVE) | **−$560.6M** | FULLY_NEGATIVE | 735 (+2.6%) | 715 (−0.18%) |
| IWM | 301.72 | — | — | oscillating POS/FULLY_NEG | — | — |

`uw options-flow dte-volume-share`: 0DTE **32.3%**, weeklies **28.0%**, monthlies **23.5%**, LEAPs **3.7%** — `regime_hint: BALANCED`. The 3.7% LEAP share is why the LEAP lane came back structurally thin, not merely selective.

**`uw historical vrp`:** SPY **FAIR** (iv30 0.1256 vs realised30 0.1246, VRP **+0.0011** — effectively zero). QQQ **FAIR** but **negative** (iv30 0.1948 vs realised30 **0.2279**, VRP **−0.0331**) — *the Nasdaq index is realising more than it implies*. There is no systematic premium-selling edge anywhere in the index complex today; if anything QQQ vol is cheap.

**Macro backdrop** (`scripts/fred_macro.py`): yield curve **normal** at +0.46 (10Y 4.71 / 2Y 4.19); core CPI **2.79% YoY**; core PCE **3.29% YoY**; unemployment **4.1%**; **payrolls −23k MoM (contracting)**; 10Y **4.71% and rising** (+16bp/30d); USD **weakening** (broad index −1.41 /30d); fed funds 3.63%.

That combination — long rates rising, dollar falling, payrolls contracting, core PCE re-accelerating above target — is a **stagflationary tilt**, and it is the honest backdrop to a "broadening rotation" that on inspection is defensives (XLV, XLP) and gold beating growth (XLK). Read the rotation as **risk-repricing, not risk-seeking**.

**Forward `event_risk` (Tier-1 unless noted), T+0 = 2026-08-19:**

| Event | Date | Trading days | Note |
|---|---|---|---|
| Jobless claims | Aug 20 (Thu) | T+1 | Tier-2 |
| **Monthly OPEX** | **Aug 21 (Fri)** | **T+2** | Aug-21 expiry alone holds **~$7.7B** premium, >2× the next bucket |
| **Core PCE** | **Aug 26 (Wed)** | **T+5** | Fed's preferred gauge, currently 3.29% |
| **NVDA Q2 FY27 (AMC)** | **Aug 26 (Wed)** | **T+5** | consensus ~$28.7B rev, >50% YoY |
| **Jackson Hole** | **Aug 27–29** | T+6/T+7 | **Warsh's first keynote as Chair, Aug 28** — unknown reaction function |
| Aug payrolls | Sep 4 | T+11 | outside live horizons |
| Aug CPI | Sep 11 | T+16 | outside live horizons |

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** Prose-only, **0 rubric points**, no backtested predictive claim. Scope is **SPY and QQQ only**. Predictive validation of these levels lives in `/weekly-analysis`'s rolling §2 backtest, not here.

**⚠ OPEX-week caveat, and it is unusually binding tonight.** The next session (2026-08-20) is **D−1 into monthly OPEX**. The Aug-21 expiry carries **~$7.7B of premium — more than double the next-largest bucket (Sep-18, ~$4.4B)** — so a disproportionate share of the standing 0–45 DTE gamma book described below **expires within 48 hours**. Every level here is a one-session prior that partially unwinds Friday; Monday's book will be structurally different.

### SPY — signal conflict, graded on `total_gex`
Spot 769.20 · ZGL 356.12 **rejected** (>55% from spot — a garbage extrapolation, `zgl_reliable: false`) · regime label **POSITIVE** but `total_gex` **−$303,228,583** · call wall **775** (+165.6M net GEX) · put wall **765** (−330.8M).

The CLI's classifier and its own aggregate disagree. Falling back to the documented rule (total_gex sign + spot-vs-wall position), this is closer to a **short-gamma / amplifying** book than a mean-reverting one. What *is* unambiguous is the geometry: dealers have built a **tight bracket around spot** — put wall only 55bp below, call wall only 75bp above. Regime freshness is poor: **6 flips in the trailing 30 sessions**, FULLY_NEGATIVE on 08-17 and 08-18, nominally POSITIVE today. Not a held regime.

**Structure bias:** not a clean pin. A narrow-width iron condor (shorts near 767/771, wings just past 765/775) harvests the tight bracket while capping the tail if a wall breaks — but given the label/aggregate conflict, **reducing or standing aside until the first 30–60 minutes re-price is the more defensible call.**

### QQQ — clean short-gamma, no cushion
Spot 716.30 · ZGL `null` (no zero-crossing in the grid) · regime **FULLY_NEGATIVE** · `total_gex` **−$560,644,368** (label and aggregate agree — no conflict) · call wall **735** (+2.6%) · put wall **715** (−0.18%).

The detail that matters: **strike 717 — 0.7pt above spot — prints −$276.3M, the single most negative strike in the entire grid.** Dealers are short gamma immediately around current price with essentially no nearby support shelf. Regime freshness is also poor (5 flips in 8 sessions). This is a **trend/breakout, vol-expansion** setup: a directional push at the open is more likely to be amplified than faded, with 735 the first real brake 2.6% away.

**Structure bias:** **do not sell premium into this book.** Debit verticals or a directional lean in the break direction; long straddle/strangle around 716 if directionless. QQQ's IV already trades **below** realised (VRP −0.0331), so buying vol here is not overpaying — which reinforces the long-gamma lean.

**Mandatory caveats (both names):** EOD is a **prior, not a target** — fresh 0DTE OI re-anchors both walls in the first 30–60 min. **Gap risk voids the prior** (Aug 20 claims pre-market). `uw options-structure gex --dte-max 1` errors, so this is the **0–45 DTE** proxy, not the isolated D+1 expiry — and per the OPEX caveat it is abnormally front-loaded. This is the **SPY/QQQ ETF book**, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup — **STAND ASIDE**

`scripts/zerodte_setup.py` returns `sell_premium: true` and `verdict: GO_PREMIUM_SELL_INTRADAY` for both indices. **That verdict is unconditional and I am overriding it.** It does not survive the VIX-tercile read:

| Index | vol_state | VIX | gross `mean_pnl` at this state | assumed round-trip cost | **NET** |
|---|---|---|---|---|---|
| SPY | **LOW** | 14.89 | +0.020% | 0.10% | **−0.080%** |
| QQQ | **LOW** | 14.89 | +0.067% | 0.10% | **−0.033%** |

VIX 14.89 sits below the sample's tercile bounds **[16.1, 17.3]** → bottom tercile, LOW confirmed. **Both indices are net-negative after costs at today's vol state.** The edge in this lane lives entirely in the MID (+0.166% / +0.300% net) and HIGH (+0.231% / +0.393% net) terciles. The headline 86.7% / 85.0% *gross* win-rates are exactly the kind of figure that overstates a negatively-skewed short-vol strategy once costs are charged.

Per-index detail as returned: SPY `expected_range_pct` 1.21%, implied move 0.66%, `size_scalar` 0.5; QQQ `expected_range_pct` 2.05%, implied move 1.14%, `size_scalar` 0.5; `stand_aside_reason: null` and `caution: null` on both. **PnL basis: percent-of-underlying-spot-notional, GROSS** — not premium-collected, not margin-relative.

Two further reasons to stand aside beyond the arithmetic: QQQ's **negative VRP** means you would be *selling* vol that is already cheap to realised, and QQQ's **short-gamma book with no cushion at spot** (§2 above) is the regime where short-vol structures break. **Advisory, 0 rubric points, permanently — promotion requires a vol-shock day in the sample (the left tail is still UNSAMPLED) and a tail-aware net-expectancy bar.**

---

## 2b. Swing Dealer Positioning (1–4 weeks)

**Zero names score the +1 mechanized dealer line.** Both disjuncts fail, and they fail for clean, checkable reasons:

**Vanna is structurally dead this cycle.** Dated VIX closes (Yahoo raw chart API — no out-of-band fills): `08-13: 14.63 → 08-14: 14.25 → 08-17: 15.19 → 08-18: 15.84 → 08-19: 14.89`. VIX **rose two consecutive sessions then fell only one**. The precondition needs a ≥3-session falling run, so `vanna_squeeze_flag = FALSE` **market-wide**, regardless of book shape. Put-heavy books (AMD, AVGO, AMAT, SMH) are correctly tagged **"vanna pressure, not squeeze."**

**No DEX flip qualifies.** `scripts/dex_flip.py` run over 10 names × 13-date windows (08-03 → 08-19) returned `qualifies: false` on every one:

| Ticker | sign changes | whipsaw | Note |
|---|---|---|---|
| SPY, QQQ, IWM, NVDA, AMD, MRVL | 0 | false | monotone, no flip |
| MU | 1 | false | flip earlier in window, not latest session |
| **AVGO** | 1 | false | flipped ~08-13→08-14, **already negative 4 straight and deepening** — real, but predates the latest session so it fails the mechanized test |
| AMAT | 3 | false | near-miss: 2-session prior run (needs ≥3); alternates almost daily = noise |
| **SMH** | 4 | **true** | building 2-session negative run; one more would qualify — **but the window whipsawed 4×, do not pre-empt** |

The one coherent cross-asset pattern is **systematic positive-DEX decay into Friday's expiry**: SPY $83.06B → $26.47B, QQQ $62.22B → $13.67B, IWM $11.39B → $3.02B, NVDA $23.33B → $11.99B (roughly halved), MU $17.25B → $2.86B. Call-long books thinning into OPEX. **This is informational — quiet de-risking, not reversal — and it scores nothing.**

**Watch into next session:** **AVGO** and **SMH** both carry sustained/building put-heavy dealer books consistent with today's semis distribution (broad-based across strikes, not a single-strike artifact). If either prints a 3rd consecutive negative-`net_dex` session tomorrow with |net_dex| ≥ 0.25× trailing median, re-run `dex_flip.py` — that would be the window's first qualifying flip. **SMH's front-end IV ratio is 1.049 at `--near-dte 7`, just under the 1.10 panic threshold.**

Healthcare front-end backwardation (LLY 1.448, MRK 1.235, AMGN 1.292) is **event-driven IV repricing off the MRNA spillover**, not a dealer-hedging dynamic — routed to §5, not scored here.

*Standing caveat: every level above partly reflects OI expiring in 2 sessions and will reset next week.*

---

## 2c. Sector Rotation

**Rotation regime call: `no_change` (low confidence).**

The finding that matters is one a single-day snapshot cannot produce: **no sector clears the 3-day netted-persistence bar.** Reconstructing the netted series back to 08-03 from prior cached `market_regime.json` snapshots (values in $M; `.` = outside the reported top-3/bottom-3 truncation):

| Sector | 08-04 | 08-05 | 08-06 | 08-07 | 08-10 | 08-11 | 08-12 | 08-13 | 08-14 | 08-17 | 08-18 | **08-19** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Technology | +839 | −65 | +620 | +110 | −279 | −140 | −34 | +322 | +40 | +222 | −409 | **−59** |
| Comm Svcs | −102 | . | +9 | −18 | −26 | . | −37 | −40 | . | −121 | −141 | **−73** |
| Consumer Cyclical | −63 | −61 | −44 | −30 | . | −53 | −79 | −54 | −118 | −124 | −53 | **+111** |
| Healthcare | −27 | +0 | . | −7 | +26 | . | +28 | −34 | −18 | −41 | . | **+103** |
| Industrials | +41 | −89 | +20 | +79 | . | +6 | +86 | +95 | −48 | +41 | . | **−36** |

- **Consumer Cyclical** flipped IN today after **eight straight OUT sessions** (08-04 → 08-18). A one-day reversal against an established outflow, not a rotation — and corroborated by TSLA's **−$721.0M** and AMZN's −$43.8M 30d cum-flow.
- **Healthcare** flipped IN after 3 straight OUT sessions, on a hard exogenous catalyst. Highest-quality "day 1" candidate, but mechanically fails the 3-day bar.
- **Communication Services** is the only durable signal — netted OUT in **6 of 6** sessions it appears, including the last 3 straight. Routes to `watch_only` regardless (short-routing rule), not a sized short.
- **Technology** is 2 sessions OUT, but the series above is **whipsawing violently** (+839 → −65 → +620 → −279 → +322 → −409 → −59). A "2-day Tech outflow" read has no statistical footing in that sequence.

**⚠ The persistence tool is degenerate today and was not used for direction.** `sector-flow-persistence` returned `INFLOW / persistence_score 1.0` on **10 of 11 sectors** (Utilities 0.8 the lone exception) — **including Technology, which the netted source has as the second-largest outflow.** A filter that fires on ~everything discriminates nothing. This is the documented gross-turnover defect: `sector-flow` and `sector-flow-persistence` are **one sign-agnostic source**, and only `market-regime.sector_rotation` carries direction (C55). Graded as noise, used only as the durability filter the spec assigns it.

Note the flat contradiction this produces: **Technology is simultaneously the largest gross number (+$3.891B) and a netted OUTFLOW (−$59.1M)** — the gross/netted distinction in a single line.

**ETF flow tape (advisory, 0 points)** — instrument-level layer the GICS aggregates cannot see:

| ETF | Net premium dir | 5d net | DP positioning | Options urgency | GICS agreement |
|---|---|---|---|---|---|
| **XLV** | inflow | +$8.49M | large EOD blocks, one aggressive above-mid (+$17.3M @ +0.30 vs mid) | calls dominant (170c/157c/167c) | **agree** (Healthcare IN) |
| **XLI** | inflow | +$5.61M | blocks near/above mid (closing-cross risk) | thin: **puts only** (180p) | **disagree** (netted OUT) |
| **XLE** | inflow | +$3.50M | modest, near-mid | calls + one LEAP put hedge | n/a |
| **XLP** | outflow | −$2.93M | small, mixed sign | **puts dominant** | **disagree** (netted IN) |
| **EWY** | outflow | −$8.86M | one block sold below mid ($20.1M) | **>$45M long-dated put sweeps** vs minimal calls | n/a (Korea semis/AI proxy) |
| **GDX** | outflow | −$16.63M | large blocks, ambiguous sign | put-skewed ($15.3M + $5.85M puts) | n/a |

Two disagreements worth the desk's attention: **XLP is bearish on its own options tape while GICS netted shows Consumer Defensive as an inflow** — independently confirming that Consumer Defensive's +$17.7M fails the magnitude bar and should not be read as rotating in. And **XLI's put-only options tape contradicts its own bullish DP print** *and* the netted Industrials outflow — no coherent read.

**Single-name leaders — the conditional +1 gate, tested explicitly:**

| Ticker | (a) persistence ≥0.6 | (b) 30d flow aligned | (c) \|flow\| ≥$50M | Result |
|---|---|---|---|---|
| **LLY** | PASS *(degenerate)* | PASS (+$114.17M) | PASS | **PASS — only name clearing all three** |
| MRNA | PASS *(degenerate)* | PASS (+$25.17M) | **FAIL** | FAIL |
| TSLA | PASS *(degenerate)* | **FAIL (−$721.02M)** | (magnitude, wrong sign) | FAIL |
| AMZN | PASS *(degenerate)* | **FAIL (−$43.75M)** | FAIL | FAIL |
| UNH | PASS *(degenerate)* | **FAIL (−$0.11M)** | FAIL | FAIL |
| WMT | PASS *(degenerate)* | PASS (+$16.55M) | **FAIL** | FAIL |

⚠ **Known defect, confirmed live on a real candidate today:** conditions (b)/(c) test the **identical field at the identical threshold** as the standalone cum-flow rubric line, and (a) is non-discriminating. LLY's two rubric points therefore rest on **one bit of evidence counted twice**. Applied as written (the freeze forbids netting them), but LLY's honest score is **1, not 2**. Logged for `/calibration-audit`.

---

## 3. Swing Setups (1–6 weeks)

**The section is empty of sized trades.** Nothing reached MEDIUM or HIGH; the entire book sizes to `skip` or `watch_only`. Full theses are retained below so the counterfactual keeps resolving.

### 3a. Long swings (regime-aligned) — none sized

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **MSFT** | 2 (DROP) | Beyond-OPEX call OI building (Sep-18/Oct-2), 30d cum-flow +$648.6M, DP mega-tier buy_ratio 0.884 | — | Loses the **$479.65** second-tier DP shelf; or `oi-trend` flips UNWINDING 2+ sessions | **skip** |
| **LLY** | 2 (DROP) | Only name clearing the sector-leader gate; +$114.17M 30d / +$185.3M 90d; sole fundamentals **CONFIRM** | — | 30d cum-flow turns negative; healthcare netted flow reverts OUT | **skip** |
| **AAPL** | 1 (DROP) | One genuine pre-market sliced parent order (~161k sh × 5 blocks at 12:10Z) bought ahead of a +2.19% day | — | Loses the **$310.03** second-tier DP shelf | **skip** |
| **NFLX** | 1 (DROP) | OPEX pin 80, distance **0.26%** — tightest on the board, `gex_at_pin` +43.4M | Iron fly 80, wings 75/85 | Clears ~78 or ~82 **and** net_gex at 80 flips negative | **skip** |
| **NVDA** | 1 (DROP) | OPEX pin 220, OI 86,566 (largest surviving mass), `gex_at_pin` +58.7M | Broken-wing fly 215/220/232.5 | Breaks 215 or 222.5 with a gex sign flip at 220 | **skip** |
| **GLD** | 0 (DROP) | Multileg bullish call vertical 430C/445C Sep-11 (56,203/56,111 matched) | — | — | **skip** |

**Distribution cautions (C28, advisory, 0 points, no sizing impact):**
- ⚠ **MSFT** — Sep-18 480C OI **−1,179** on 851 volume (~$1.89M closing call premium), in the *same beyond-OPEX expiries* cited as evidence of forward positioning.
- ⚠ **AAPL** — Sep-18 320C OI **−3,041** on 8,284 volume — at the **exact strike** the pin thesis relies on for dealer long gamma.

**§6 deep-dive addendum — the single most useful thing this section produced.** `uw historical trend --days 10` reveals that **MSFT printed bearish flow *today*** (`flow_direction: bearish`, net_flow **−$11.46M**) despite carrying the day's largest accumulation score — 4 bearish days of 10. **LLY** was bullish today (+$61.09M, **7 of 10 bullish days**), consistent with its thesis. This is why the deep-dive step exists: MSFT's same-day flow contradicts its own label.

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only` (2026-08-01 P0 #1) — routing, not suppression.**

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **GDX** | **3 (LOW)** | Institutions built a **$21.16M put debit vertical** (long 85P / short 75P, Nov-20, 93 DTE), legs matched 45,006/45,079 at `multileg_ratio` **0.9999**, build NEW. Post-hygiene curve is flat-to-mild CONTANGO with **no back-month kink** ⇒ resolves DIRECTIONAL, not event-vol. 30d cum-flow **−$125.8M** (2.92× union median) confirms. **§6 addendum: 8 of 10 bearish flow days, and flow was bearish TODAY while price rose +9.42%** — a genuine price-vs-flow divergence that strengthens the directional read. | Nov-20 85P/75P put vertical, max loss ~$9.45M | net_dex/cum-flow reverts positive ≥3 sessions; or gold breaks decisively above the $4,500 area | **`watch_only`** |

**The honest tension on GDX, stated rather than resolved:** fundamentals-gate returned **CAUTION** because the gold news stack is *unanimously bullish* (record $4,500 gold, sinking dollar, "best month since April 2020") and reads the structure as a **hedge against a long spot-gold book**, not a directional short. The bear's rebuttal is that this defence is **unfalsifiable** — no position-level data exists to distinguish a hedge from a short, and a hedge and a short have identical payoff. The debate landed bull 0.55 / bear 0.45 — the only name all day where either advocate cleared a coin flip, and only barely. **Two independent gates (short-routing and fundamentals CAUTION) point the same way, so the practical answer is the same regardless of which framing is right.**

**Sweeps (informational, 0 rubric points — line removed 2026-05-23 P0.3 after −22pp over two audits).** **No ticker clears all three bars** (≥3-of-5 persistence, non-mega-cap/non-index, single non-mixed direction). MU, SNDK, AMD and NBIS all show 5/5 persistence but `direction: mixed` — no directional thesis. The mega-cap/index book (SPXW, QQQ, SPY, SPX, TSLA, NVDA, META, AAPL, AMZN) is demoted under the hedge-flow filter. **The genuinely useful separation today is the OPEX-mechanical bucket:** >$600M of MSFT Aug-21 call clusters with `side: no_side` are gamma-roll mechanics, and the SPX/SPXW 7000-strike ladder transacting on both sides across Aug-21 *and* Oct/Dec/Jan tenors is a **roll**, not fresh conviction. One contradiction worth logging: IWM's persistence window is tagged *bullish* while today's actual tape shows a 09-18 288P at 44× ask-ratio — **bearish** — a textbook hedge-flow mismatch.

---

## 4. LEAP Builds (6–24 months)

**Empty book.** No candidate reached even **4 of 9** gates, let alone the required 6. Consistent with LEAPs being only **3.7%** of today's volume share — a structurally thin day for this lane, not merely a selective one.

The binding constraint was **Gate 4 (90d cumulative-premium-flow accretion)** on *every* name checked — MIXED or BEARISH across the board, with no clean multi-week bullish accretion anywhere.

**Near-misses, with the specific failing gate:**
- **WOLF** (DTE 394, C50/C55, ~10,000 contracts each, `oi_change` 161–833%) — the most eye-catching fresh build on the tape, and it **disqualifies on inspection**: both strikes show `prev_bid_volume` ≫ `prev_ask_volume` (10,003 vs 0; 10,002 vs 7) — **contracts SOLD at the bid**. This is call *writing*, a bearish/covered-call signature masquerading as an OI build. 90d cum-flow **BEARISH −$99.7M**; conviction-matrix confidence 24.2% (needs >70). **0–1 of 9.**
- **GLD** (DTE 302) — the 525C shows 67,500 bid volume vs 207 ask (sold), the 530C shows 67,526 ask (bought): same expiry, opposite sides ⇒ a **call spread, not a directional long**. Conviction-matrix MIXED at 5% confidence. **1 of 9 at best.**
- **MRNA** — despite the +176.97% platform-validating readout, **no DTE>180 concentration exists at all**; top contracts are DTE 9/30. 90d cum-flow MIXED at +$29.9M on ~$950M/$920M gross. **Verdict: too early** — a genuine LEAP response would need several more sessions to register.
- **MRK** — top contracts DTE 2 and 93, nothing >180; 90d cum-flow **BEARISH −$51.7M**.
- **XBI** — `consecutive_build_days` 2 (needs ≥5); 90d flow MIXED −$8.1M. **0 of 9.**

`position-rolls` was populated but is dominated by the mechanical Aug→Sep roll two sessions before expiry, and the tool exposes **no destination-DTE field** to confirm any land at DTE>180 with *added* notional. PLTR and TMDX are worth a look in tomorrow's cache if they persist; neither is actionable today.

*Substrate note: `signal-backtest` does not support the `oi_build` class, so this lane is structurally unmeasurable there — any win-rate would be `NA(substrate)`.*

---

## 5. Volatility Surface

**Population framing first, per the grading discipline: 14 names tested; 9 (64%) were reclassified off the raw label after hygiene.** Raw `iv-term-structure` printed BACKWARDATION on 10 of 14 before cleaning; `scripts/term_structure_hygiene.py` (`min_contracts=15`, a **tunable, not audit-frozen** parameter) flipped 9. Post-hygiene: BACKWARDATION 5, KINKED 7, CONTANGO 1, FLAT 1. Grade every firing below by that base rate, not by anecdote.

**⚠ Every IV-percentile figure this run is PROVISIONAL.** `iv-percentile-zscore` returned `dates_used: 90` against a requested 252 on **every single call** — the documented silent short-delivery. Reported as n=90 claims, not 252-day reads.

### The marquee dislocation — QQQ front-month vol is underpriced
QQQ's **dte7 tenor lands exactly on NVDA earnings + Core PCE (Aug 26)** yet prices IV at **17.7%** — *below* both the dte30 tenor (20.86%, ratio 0.849) and trailing realised (rv20 23.2%). VRP **−0.0331**. SPY shows a weaker mirror (front 12.2% vs far 15.2%, ratio 0.805) with **two live kinks in its own curve** (dte2/Aug-21 OPEX at 11.1% prominence; dte8/Aug-27 at 8.4%) — so the market is pricing *some* near-term structure, just not enough to close the QQQ IV/RV gap.

**This reads as a genuine BUY VOL setup on QQQ into the event stack** — calendar or long front straddle, not a sell.

> **⚠ And it scores exactly zero.** The frozen rubric's vol line requires `shape ∈ {KINKED, BACKWARDATION}`; QQQ's hygiene-corrected shape is **FLAT**. The rubric has **no vehicle for a VRP-negative front-end BUY VOL read on a flat curve**. This is the strongest single observation on the board and the scoring machinery cannot express it. Flagged for `/calibration-audit` as a rubric-design gap — not retuned here, since the freeze forbids it.

### MRNA — the two agents disagreed, and neither is wrong
This is worth stating plainly rather than papering over. **contrarian-scanner** called MRNA a `vol_fade` (iv_rank **100**, front-end ratio **1.484**, BACKWARDATION surviving hygiene with **0 tenors dropped**). **vol-surface-scout** called it **watch-only — not a clean crush trade**, because VRP is deeply *negative*: iv30 **126.6%** vs rv20 **355.7%**, i.e. realised is ~3× implied.

Both flagged the same root problem: **rv20 is corrupted by today's own +176.97% gap**, so trailing realised vol is not a usable comparator and forward realised is unknowable. Selling 200% IV on a name that just moved 177% is not obviously rich; buying it is not obviously cheap. **Neither "rich" nor "cheap" is establishable ⇒ watch-only.** Additional caution: the readout genuinely re-rates the platform and multiple further trials remain, so this is not pure binary-event crush. Term skew reads **1.139 TAIL_HEDGING** at dte302.

### Other names

| Ticker | shape | base_shape | front ratio @dte7 | kink (dte @ prom.) | iv pctile / z *(n=90)* | Note |
|---|---|---|---|---|---|---|
| MRK | KINKED | BACKWARDATION | 1.235 | 37 @ 7.5% | 93.33 / +1.52 | Real front richness off the +12.6% move; skew 1.192 TAIL_HEDGING |
| MRVL | **CONTANGO** *(flipped)* | CONTANGO | 1.269 | 9 @ 3.8% **sub-threshold** | 17.78 / −0.56 | Near-miss kink aligns with Aug-27 earnings |
| MU | KINKED | BACKWARDATION | 0.944 | 16 @ 17.9% | 4.44 / −1.75 | Kink at 16d, not front; no near-term event |
| NBIS | KINKED | BACKWARDATION | 0.924 | 30 @ 15.4% | 12.22 / −1.10 | Curve otherwise cheap vs realised (91.7% vs rv20 182.6%) |
| AVGO | KINKED | BACKWARDATION | 0.841 | 16 @ 10.3% | 45.56 / −0.25 | Front genuinely cheap (contango into the kink) |
| AMAT | KINKED | BACKWARDATION | 0.905 | 30 @ 8.9% | 12.22 / −1.09 | Modest kink at monthly |
| SNDK | BACKWARDATION | BACKWARDATION | 1.091 | none | 1.11 / −1.43 | Broad, no single kink — genuine post-move decay |
| STX | BACKWARDATION | BACKWARDATION | 1.054 | none | 5.56 / −1.21 | ⚠ **15 tenors kept — exactly at the floor**, treat cautiously |
| SMR | KINKED | BACKWARDATION | 1.092 | 37 @ **26.4%** | 1.11 / −2.78 | ⚠ only **11 tenors** — thin, size down |
| QBTS | BACKWARDATION | BACKWARDATION | 1.001 | none | 0 / −2.36 | ⚠ **12 tenors**; effectively FLAT — label is noise on a thin curve |

**No calendar candidate clears on trend.** Every BACKWARDATION name would need a *falling* front-end-ratio to qualify, and **no prior-session snapshot exists** to establish direction of travel. Recorded as a data gap, not a clearance.

**Single-contract IV outliers are all noise today.** Every flagged row (AVGO Aug-19 390P max_iv 182%, NVDA 110/115/120C, SOXL 135/145/130P, MSFT 345/350C, SPY 500C) is a **same-day 0DTE expiry**; AVGO's avg_iv 6.1% vs max_iv 182% spread is single-print expiry-day microstructure, not whale mispricing. **None graduate as tradeable dislocations.**

---

## 6. Risk & Correlation

**Macro headline:** yield curve normal (+0.46); core CPI 2.79% / **core PCE 3.29% and above target**; unemployment 4.1% with **payrolls −23k MoM**; 10Y **4.71% rising**; USD **weakening**; fed funds 3.63%. **Forward event wall: OPEX (T+2) → Core PCE + NVDA AMC (T+5) → Jackson Hole/Warsh (T+6/T+7).**

**Breadth (advisory):** 285 advancers / 217 decliners, **`pct_green` 56.66%** — index green **and** `pct_green` > 50, so **no divergence flag** fires. But see §1: price breadth (56.7% green) and *flow* breadth (36.5% bullish) disagree by ~20 points, which is the softer distribution tell worth carrying forward.

### Correlation clusters (`uw risk portfolio-correlation`, 30d, today's 13 candidates)

| Cluster | Members | Corr | Kept | Penalised |
|---|---|---|---|---|
| `precious_metals` | GDX / GLD | **0.928** | GDX (raw 3) | GLD −1 tier |
| `enterprise_software_earnings` | CRM / INTU | **0.880** | CRM | INTU −1 tier |
| `biotech_catalyst` | MRNA / MRK | **0.868** | MRNA | MRK −1 tier |

**Soft watch (0.60–0.70, no penalty):** NVDA/QQQ **0.676** · QQQ/HYG 0.622 · NFLX/INTU 0.608.

**The AI-semis cluster did NOT persist.** Prior sessions measured NBIS/CRWV 0.904, AMAT/SMH 0.902, MU/MRVL 0.848. On today's candidate set the tightest AI-adjacent pair is **NVDA/QQQ at 0.676 — below the line.** Semis **decorrelated from the index** this month rather than moving as one bet, which is consistent with the broadening tape. Also notable: **LLY/QQQ −0.509** — the healthcare leg is a genuine anti-correlate to the tech leg right now.

*Tool caveat: `sector_breakdown` returned `100% Unknown` for all 13 tickers, so its sector-concentration warning is a null artifact and was ignored. The correlation coefficients themselves are sound.*

### Gates applied

**Panic gate — re-read at `--near-dte 7`** (at the CLI default of 1 this line fires on ~everything and carries no information). **Population firing rate 7/14 (50%) — properly discriminating.**

| Fires (>1.10) | Does not fire |
|---|---|
| MRNA 1.484 · LLY 1.448 · CRM 1.297 · INTU 1.284 · NVDA 1.258 · MRK 1.235 · NFLX 1.132 | MSFT 1.082 · GDX 1.057 · GLD 1.056 · AAPL 1.011 · QQQ 0.848 · SPY 0.804 · HYG 0.560 |

**The split is the most interesting datum on the page:** both indices sit in **deep contango** (SPY 0.804, QQQ 0.848) while **seven single names are backwardated**. Vol is priced **idiosyncratically, not systemically** — seven names each carrying their own binary, against a calm tape. That structure argues for name-level dispersion rather than index directional exposure; nothing on this board scored well enough to express it.

**Fundamentals verdicts (top-5):** **No VETO today.** LLY **CONFIRM**; GDX, MSFT, AAPL, NVDA all **CAUTION (−1 tier)**. The common thread is stark — **four of five carry insider selling**: NVDA MSPR **−98.61** (near-total), MSFT **−83.89**, AAPL **−76.74**, LLY −25.38 (mildest). Insiders are selling the mega-cap complex into a rotation out of it.

**Event-risk flags:** OPEX (T+2) hits every non-pin structure carried through Friday; Core PCE + NVDA AMC (T+5) stack on top. Pin plays (NFLX, NVDA) and earnings-vol plays (CRM, INTU) are **exempt** — the event *is* the trade.

**Debate-disconfirmation cuts:** 3 of 5 debated names failed. **MSFT** (bear 0.65 ≥ bull 0.35), **LLY** (0.65 ≥ 0.35), **AAPL** (0.25 = 0.25, tie ⇒ cut). GDX and NVDA passed only weakly. **AAPL at 0.25/0.25 and NVDA at 0.45/0.35 are `BOTH_SIDES_LOW`** — neither advocate cleared a coin flip. Recorded, not mechanized into a deduction (n far below the cross-regime ∧ n≥30/arm ∧ BH bar).

**Adverse-flow exit list:** carried group `conviction_2026-08-18` = **[ULTA]**. `watchlist alerts` shows `LARGE_DARK_POOL` (**high severity**, $5,899,252 single print) and `VOLUME_SPIKE` (1.7×). `watchlist scan` shows **`flow_direction: bearish`**, net_flow **−$413,641**, P/C 1.008, `iv_rank` 74.0. **→ ULTA tagged EXIT CANDIDATE.** The `fz` drift tripwire shows only price drift (mcap 21.21B → 22.21B) — **no short-float jump, no target cut, no recom deterioration** — so the exit rests on flow alone; the underlying did not re-rate. The tell is that **price rose while options flow turned bearish**.

**Hedge sleeve: none. There is no book to hedge.** Net delta is exactly zero, so a hedge would be a naked directional position wearing a hedge's name. For the record, had there been a book: QQQ's **negative VRP** means a long put leg is bought **below** realised vol (genuinely cheap protection), and a concentrated semis book should be hedged with **SMH/SOXX, not SPY** — an index hedge structurally under-hedges concentrated damage.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**This section is empty. Zero names reached raw_score ≥ 7.** The highest score on the board was **3**. Full audit rows for the top of the book are preserved below so the counterfactual stays gradeable.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: per the most recent `/calibration-audit` (2026-08-08), the **DROP pile continues to out-realise the sized book** (DROP ≈0.415 vs decided HIGH ≈0.143). Per-tier expectancy and payoff ratio cannot be computed for this run because **no tier above LOW was populated** — a high hit-rate with a sub-1 payoff still loses money, and a coin-flip with a 1.5 payoff makes it, but neither can be measured on an empty book. Display-only; the live sizer remains the Step 5 win-rate ladder.

| Ticker | raw | tier | class | win_rate (n, source) | pre-risk | fundamentals | bull/bear | gates applied | **final** |
|---|---|---|---|---|---|---|---|---|---|
| **GDX** | 3 | LOW | multileg_directional | `null` `NA(substrate)` | watch_only | CAUTION | 0.55 / 0.45 | regime −1, fundamentals −1, event −1, rubric_regime cap | **`watch_only`** |
| MSFT | 2 | DROP | dark_pool_accumulation | `null` `NA(substrate)` | skip | CAUTION | 0.35 / **0.65** | fundamentals −1, sector −1, debate −1, event −1, cap | **skip** |
| LLY | 2 | DROP | sector_rotation | `null` `NA(substrate)` | skip | **CONFIRM** | 0.35 / **0.65** | panic −1, debate −1, event −1, cap | **skip** |
| AAPL | 1 | DROP | dark_pool_accumulation | `null` `NA(substrate)` | skip | CAUTION | 0.25 / 0.25 | fundamentals −1, sector −1, debate −1, event −1, cap | **skip** |
| NFLX | 1 | DROP | opex_pin | `null` `NA(substrate)` | skip | NA | — | panic −1, sector −1, cap | **skip** |
| NVDA | 1 | DROP | opex_pin | `null` `NA(substrate)` | skip | CAUTION | 0.45 / 0.35 | panic −1, fundamentals −1, sector −1, cap | **skip** |
| CRM | 1 | DROP | earnings_vol | `null` `NA(substrate)` | skip | NA | — | vrp −1, panic −1, sector −1, cap | **skip** |
| INTU | 1 | DROP | earnings_vol | `null` `NA(substrate)` | skip | NA | — | vrp −1, panic −1, cluster −1, sector −1, cap | **skip** |
| GLD | 0 | DROP | multileg_directional | `null` `NA(substrate)` | skip | NA | — | cluster −1, event −1, cap | **skip** |
| MRNA | 0 | DROP | high_iv_rank | **0.60** (n=152, `backtest_clean`) | skip | NA | — | vrp −1, panic −1, cap | **skip** |
| MRK | 0 | DROP | high_iv_rank | `null` `NA(substrate)` | skip | NA | — | panic −1, cluster −1, event −1, cap | **skip** |

### Substrate and integrity notes for `/calibration-audit`

1. **`dark_pool_accumulation` returned 0 rows market-wide again** — the desk's most-cited accumulation class remains permanently unmeasurable via `signal-backtest`. **`multileg_directional`, `opex_pin`, `sector_rotation` and `earnings_vol` are not supported classes at all**, so those tools were correctly **not called** and no numeric quote was invented.
2. **The forward-window clamping artifact reproduced in the documented direction.** The one completed clean-protocol measurement (`high_iv_rank`): 189 rows → 15 clamped rows dropped (clamped realised **0.867** vs clean **0.805**) → 22 further dropped on the C12 liquidity floor → **kept n=152, raw 0.7895**. The `high_iv_rank` class ceiling of **0.60 binds**, landing it in the `[0.55, 0.65)` anti-predictive band → `starter` floor. **The tool's own headline (`vol_realisation_rate 81.0%`) was never quoted.**
3. **C56 counter, stated carefully:** today emits **one** in-band `[0.55, 0.65)` quoted row (MRNA at 0.60, disclosure-only, not cited for any upgrade or tie-break). Post-starter-floor in-band count → **20**; post-disclosure-rule → **9**. Both below the n≥30 bar. *Compute the post-fix in-band count first and write it down before looking at any realised rate — the pooled corpus figure is a description of history, never the trigger.*
4. **⚠ Rubric-integrity item — a gate was applied that is not in the frozen rubric text.** The quant halved MSFT's C11 accumulation award 3→1 using a **"scale-relative ≥5% of gross" floor** (MSFT's net is 3.98% of $16.28B gross). That floor lives in the agent's own definition but does **not** appear in the frozen rubric carried by `daily-analysis.md`, which specifies only *sign-aligned* ∧ *|cum_flow_30d| ≥ $50M*. With the full +3, MSFT would score **4 (LOW)** rather than 2 (DROP). **Immaterial today** — MSFT failed the Step 3 confluence gate anyway — but the two documents disagree and one of them should be corrected.
5. **The QQQ BUY VOL read scores zero on a shape-label technicality** (§5). Rubric-design gap, logged not patched.
6. **The LLY sector-leader/cum-flow double-count is now confirmed live on a real candidate** (§2c). Two rubric lines, one bit.
7. **Verified empty-board streak is 31, not 23/24.** Re-derived mechanically from every `analyses/daily/*/decision.json` by testing for a non-`skip`/`watch_only` `final_size`. Last sized session: **2026-07-07**. The 08-17 report claimed 22nd, 08-18 claimed 23rd, and this run's own quant and risk-monitor both reported 23rd — **all wrong**. Streak counts must be re-derived from envelopes every run, never inherited from prose. A 31-session drought is a different phenomenon from a 24-session one and warrants direct examination: no-edge market vs over-refusing gate stack.
8. **Freeze-lift remains structurally unrunnable — for a 9th consecutive cycle.** Today contributes **zero HIGH and zero MEDIUM**. The binding constraint is **band emptiness, not sample size**: post-freeze resolved calls now vastly exceed the stated ≥30 threshold while decided HIGH and MEDIUM remain at zero. Do not read the next "≥30 resolved" milestone as progress toward lifting the half-cap.
9. **Watch the OOR-cap margin.** It has compressed monotonically across five measurements (−16.7 / −14.3 / −11.9 / −12.0 / −8.9pp). Still protective, still keeps — but if the next two cycles continue toward zero, the cap needs a formal re-grade rather than being left on autopilot.
10. **`fz` doubled-first-letter bug re-confirmed, 20/20 rows** on every `fz screen` surface (`MMRNA`, `MMRK`, `TTWST`, `AABSI`). Bulk screen lanes were de-doubled before use; per-ticker `fz_enrich` is healthy and was used for all fundamentals context.
11. **Yahoo `quoteSummary` returned HTTP 401 on all three deep-dives** — the yfinance path is unavailable; Finnhub carried fundamentals and the lane graceful-skipped as designed. Separately, **`uw` and Finnhub disagree on MSFT's next earnings date** (2026-11-04 vs 2026-10-27); the Finnhub value was used.

### Conviction rubric (frozen, version `2026-06-12`) — embedded verbatim for audit

```
Daily conviction score = Σ:
  +1  dealer-positioning MECHANIZED DEX flip or vanna-squeeze in trade direction (verified SIGN CHANGE via scripts/dex_flip.py, never by hand)
  +3  accumulation-hunter 3+ aligned signals (DP + OI + smart-positioning, block-stratified institutional confirmed)
      — C11 CONJUNCTION: full +3 only when cum_flow_30d sign-aligned AND |cum_flow_30d| >= $50M; else halved to +1
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days >= 5)
  +1  uw insights conviction-matrix DIRECTIONAL_LONG conf>70 — CONDITIONAL: only when dominant_signal_class == leap_directional
  +1  cumulative-premium-flow net directional accretion 30d — INTENT-SCREENED (0 if C28 distribution_flag, or ex-div deep-ITM sub-parity calls)
  +1  sector-rotation single-name leader — CONDITIONAL on (a) persistence>=0.6 AND (b) cum_flow_30d aligned AND (c) |cum_flow_30d|>=$50M
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (play type anchored to term structure)
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner overcrowded long with RISING pc-ratio-zscore (VRP positive) — informed-flow CONTINUATION penalty
  -3  flow_conflict — cum_flow_30d clearly opposite dominant_signal_class
  -1  flow_conflict_lite — 30d cum-flow MIXED
      (flow_conflict and flow_conflict_lite are MUTUALLY EXCLUSIVE — apply exactly ONE)
  # TIER GATES (risk-monitor, 0 points, never in score_components):
  -1 tier  correlation cluster (pairwise corr >= 0.70)
  -1 tier  market-regime conflicts with trade direction
Tiers: >=9 HIGH (full) · 7-8 MEDIUM (half) · 3-6 LOW (starter/watch) · <=2 DROP
```

---

## 8. Watch-only — single signal, no confluence

Only **three** names cleared the Step 3 confluence gate (≥2 distinct Phase 1 agents flagging positively): **GDX** (multileg + sector-rotation ETF tape), **GLD** (multileg + opex-pin), **AAPL** (accumulation + opex-pin). Everything below was flagged by exactly **one** agent — listed for journaling, **not for trade entry today**.

| Ticker | Sole flagging agent | Signal |
|---|---|---|
| MSFT | accumulation-hunter | C11 award 3 (halved to 1 by the quant's scale-relative floor) |
| LLY | sector-rotation-strategist | only name clearing all three sector-leader gates |
| NFLX, NVDA | opex-pin-strategist | pin 80 (0.26%) / pin 220 (1.09%) |
| CRM, INTU | earnings-scout | SELL VOL half-size, kink at dte9 (10.6% / 18.5% prominence) |
| CRWD, WMT, DE, BABA | earnings-scout | CALENDAR — **scored 0**: the rubric line reads literally "BUY VOL or SELL VOL" and CALENDAR is neither. WMT and DE report **tomorrow pre-market** |
| QQQ | vol-surface-scout | **BUY VOL** — front-month underpriced into the event stack; scores 0 on shape label (see §5) |
| SPY | vol-surface-scout | KINKED, two live kinks (OPEX + event-cluster); VRP FAIR so no aligned bias |
| MRNA | contrarian-scanner / vol-surface-scout | **agents disagreed** — vol_fade vs watch-only (see §5) |
| MRK, MU, NBIS, AVGO, AMAT, SMR, SNDK, STX, QBTS | vol-surface-scout | KINKED/BACKWARDATION but **no name-level VRP read exists** ⇒ fail closed, 0 points |
| HYG, PSKY | multileg-strategist | calendars — vol-mispricing, not directional ⇒ 0 points |
| MU, SNDK, AMD, NBIS | sweep-tracker | 5/5 persistence but `direction: mixed` — no thesis. **0 rubric points regardless** |
| AVGO, SMH | dealer-positioning-strategist | building put-heavy books; **neither clears the mechanized flip bar** (SMH whipsaw-flagged) |
| TWLO, IMAX, QCOM, TSLA, ORCL, PFE | single-leg whale scan | Tier-1 rows — **advisory, permanently 0 points (C19 CLOSED as REFUTED)** |
| NBIS, GOOGL, META | *rejected upstream* | `institutional-accumulation` NEUTRAL (1.39 / 1.20 / 0.88) — never scored |

**C12 liquidity floor** dropped 24 names from the funnel before scoring (fail-closed): PUMP, NTLA, DPST, OPEN, SVV, SPCE, OPRA, TDOC, METC, FDMT, CADL, IMMX, XNCR, CGEM, IMNM, OMER, BLFS, PBLS, CGAU, ATRC, ACHV, AI, BEAM, ASAN.

---

*Fleet: 12 Phase 1 agents (OPEX week) → signal-confluence-quant → fundamentals-gate → bull/bear debate (5 names × 2 sides) → risk-monitor. Rubric frozen at `2026-06-12`. Envelope: `analyses/daily/2026-08-19/decision.json`.*
