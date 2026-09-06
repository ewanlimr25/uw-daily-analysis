# Daily Market Analysis — 2026-08-13

## Executive Summary

- **Regime + GEX state:** TRANSITIONAL (trend UPTREND) — SPY 777.88, above both 20SMA (754.54) and 50SMA (748.48), −0.19% from the 90d high. SPY long-gamma (+$3.08B, ZGL 774.76, spot 0.38% above it) with a dominant call wall at 780 carrying ~40% of the book; QQQ long-gamma (+$1.30B) with an unusable ZGL. VIX **14.63**. `fz` breadth 63.4% green (319A/183D) and RSP +0.75% ≈ SPY +0.70% — a genuinely **broad** advance, not a cap-weighted illusion. But UW **flow** breadth is only **35% bullish** (2,209 vs 4,101 tickers): price is broad, positioning is not. Sector lean: Technology netted **+$322.3M** IN, Industrials +$96.0M IN.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** SPY — POSITIVE / ZGL 774.76 (reliable) / call wall 780 · put wall 765 → tight-cap iron fly, skew the short call in. QQQ — POSITIVE / ZGL **unusable (211.28 artifact, discarded)** / call wall 735 · put wall 715 → butterfly near 733–735, lower confidence. Advisory, see §2.
- **Top swing build:** **None.** The post-gate book is **flat**. The highest-scoring name in a 9-name field was CRWV at `raw_score 3` (LOW) and it took three full-tier cuts plus a half from a `starter` base.
- **Top LEAP candidate:** **None.** Zero of the universe cleared 6-of-9 gates; all plausible candidates (TLT, DRAM, GOOG) failed the required 90d/30d accretion gate with net premium <3.2% of gross and `trend_direction: MIXED`.
- **Biggest risk:** `AI_infra_semis_cluster` = {CRWV, SNDK, MU, QQQ, ORCL} — five of nine candidates were **one bet** (SNDK/MU corr **0.901**). No hedge sleeve recommended: there is no book to hedge.

**Today is a no-edge day.** That is the output, not a failure.

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — mixed signals, reduce position size, wait for clarity**; trend **UPTREND**; guidance *"Half position sizes. Favor defined-risk strategies. Iron condors in range."* SPY +3.06% over 30d, sitting 0.19% off its 90d high.

**The breadth split is the day's most important regime fact.** Two independent lineages disagree about what "broad" means:

| Source | Measure | Reading |
|---|---|---|
| `fz breadth` (Finviz, price) | advancers/decliners | 319 / 183, **63.4% green**, avg +0.76% |
| `market_data.py` (Yahoo OHLC) | equal- vs cap-weight | RSP **+0.75%** vs SPY **+0.70%** — equal-weight *led* |
| `uw risk market-regime` (options flow) | bullish vs bearish flow tickers | 2,209 / 4,101 — **35% bullish** |

Price participation was genuinely broad; **options positioning was net bearish across 65% of tickers.** A green, broad tape that the options market is leaning against is the definition of TRANSITIONAL, and it is why the regime label overrides the cheerful breadth print. `breadth_cross_check.divergence_flag = false` (the narrow test — green index with `pct_green < 50` — does not fire), but the flow-vs-price split is the real divergence and is recorded here rather than in that boolean.

**Per-index gamma (current-state EOD book; §2 carries the forward read):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 777.74 | 774.76 (reliable, −0.38%) | +$3.084B | POSITIVE | 780 (+0.29%) | 765 (−1.64%) |
| QQQ | 732.33 | **211.28 — DISCARDED** | +$1.301B | POSITIVE (fallback basis) | 735 (+0.36%) | 715 (−2.37%) |
| IWM | — | ZGL implausible 9-of-10 sessions — **artifact, not used** | — | — | — | — |

**`uw options-flow dte-volume-share`:** 0DTE 24.7% · weeklies 29.5% · monthlies 30.5% · LEAPs **4.2%** → `regime_hint: BALANCED`. Neither a retail-dominated nor an institution-dominated tape; no uniform conviction adjustment applied either way. The 4.2% LEAP share is why §4 is empty and that is expected, not a miss.

**`uw historical vrp`:** SPY **FAIR** (−0.003; IV30 12.18% vs realised 12.48%). QQQ **PREMIUM_BUYING** (−0.0501; IV30 18.82% vs realised **23.83%**). Vol is *cheap* relative to what the tape is actually delivering, most acutely in tech. **Long premium is the VRP-aligned side today** — this governs §2a, §5, and the (absent) hedge sleeve. Risk-monitor found every single candidate name PREMIUM_BUYING except ORCL (+0.0996).

**Macro backdrop** (`scripts/fred_macro.py`): yield curve **normal** (10y2y +0.48) · core CPI **2.79%** YoY vs core PCE **3.29%** YoY — *the gap is the problem; PCE is not converging* · unemployment 4.1% with payrolls **−23k MoM** · 10Y **4.68% and rising** (+0.06 over 30d) · USD **weakening** (−2.07 over 30d) · fed funds 3.63%. A rising long end plus a negative payroll print against a 3.63% funds rate is a stagflation-lite configuration — consistent with TRANSITIONAL, and materially adverse for the leveraged growth names this fleet surfaced.

**Forward `event_risk` (T+0 = 2026-08-13):**

| Event | Date | T+N | In swing horizon |
|---|---|---|---|
| CPI (Jul) | 2026-08-12 | T−1 | behind us |
| PPI (Jul) | 2026-08-13 | **T+0** | behind us (today) |
| Monthly OPEX | 2026-08-21 | T+6 | yes — held through |
| PCE (Jul) + GDP Q2 2nd est | 2026-08-26 | T+9 | yes |
| Jackson Hole symposium | 2026-08-27…29 | T+10…12 | ambient, not a named Tier-1 binary |

**Nothing sits at ≤T+5.** Both big binaries just cleared, so the event gate correctly fired the lighter deeper-in-swing deduction rather than a full tier on most names — with one exception (RTX, whose own ex-div is T+1 and whose structure *terminates* on OPEX).

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** Prose-only, **0 conviction-rubric points**, no backtested predictive claim. Predictive validation of these levels lives in `/weekly-analysis`'s rolling §2 backtest, not here. Scope is SPY and QQQ only.

### SPY — POSITIVE / long gamma

`spot 777.74 · ZGL 774.76 (zgl_reliable: true) · total_gex +$3.084B · call wall 780 · put wall 765`

Spot sits **0.38% above** a trustworthy ZGL in a positive-GEX book — dealers are long gamma into the close, so the next-session prior is mean-reversion / pin / vol-suppression rather than trend. The structure is **asymmetric**: the 780 call wall carries roughly 40% of the entire book's GEX and sits only 29bp away, while the 765 put wall is an order of magnitude smaller and 1.64% below. Upside is capped much harder than downside is supported.

**Structure bias:** iron fly / butterfly centred 778–780 with the short strikes hugging the 780 wall — **skew the short call leg tighter than the short put leg** to reflect the wall imbalance. A symmetric condor mis-prices this book.

**Regime freshness:** this POSITIVE read is **fresh and unstable** — SPY flipped regime four times in the trailing 10 sessions (POS→NEG 08-05, NEG→POS 08-07, POS→NEG 08-10, NEG→POS today). Spot is straddling the ZGL by less than 0.4%, so this is genuine thin-gamma knife-edge, not an artifact. Reduce confidence in the pin accordingly.

### QQQ — POSITIVE / long gamma, lower confidence

`spot 732.33 · ZGL 211.28 → DISCARDED (zgl_reliable: false) · total_gex +$1.301B · call wall 735 · put wall 715`

The reported ZGL of 211.28 sits **71% below spot** — far outside the ~5% trust band and a textbook instance of the known ZGL-grid extrapolation artifact. Discarded per protocol; the regime read falls back to the `total_gex` sign plus spot-vs-wall geometry. Spot is 0.36% under a real +GEX wall at 735, with a thinner, more distant put wall at 715.

**Structure bias:** butterfly / iron fly with short strikes near 733–735. **Confidence is materially below SPY's** for two reasons: the ZGL is unusable, and QQQ's VRP regime is PREMIUM_BUYING (IV 18.82% vs realised 23.83%) — a positive-GEX label does not guarantee vol suppression when realised vol is already running 5 points hot. The book is also roughly half SPY's notional.

**Regime freshness:** 5 flips in the trailing 20 sessions (07-22, 08-06, 08-07, 08-11, 08-12) — a noisier book than SPY's.

### Mandatory caveats

- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and recomputes both ZGL and walls before the prior can bind.
- **ZGL reliability.** SPY's is trusted (0.38% from spot). QQQ's is a discarded artifact. IWM's was implausible in 9 of 10 recent sessions and is not reported at all.
- **Gap risk voids the prior.** No scheduled overnight catalyst between this snapshot and tomorrow's open (PPI already cleared today), but this is a static read.
- **Tooling limit.** `gex --dte-max 1` errors — the D+1 expiry cannot be isolated. This is the standing **0–45 DTE** book as proxy. Cross-check: the 2026-08-14 expiry alone carries $5.12B premium vs $2.64B for today's and $6.01B for the 08-21 monthly, so near-dated tenors do dominate and the proxy is reasonable.
- **ETF book, not index book.** SPY/QQQ ETF gamma, not the cleaner SPX/NDX books. Treat walls as directional signal, not precise strike targets.

### 2a. Next-session 0DTE premium-selling setup — ⚠ **STAND ASIDE**

`scripts/zerodte_setup.py` returns `sell_premium: true` and `verdict: GO_PREMIUM_SELL_INTRADAY` for both indices. **Do not take that at face value today.** Those fields are **unconditional**; the conditional expectancy is negative.

VIX closed **14.63**, below the sample's lower tercile bound of 16.2 ⇒ `vol_state: LOW`. Reading `mean_pnl_by_vix_state[LOW]` net of the assumed 0.1% round-trip cost:

| Index | Unconditional gross | Unconditional **net** | **LOW-VIX gross** | **LOW-VIX net** |
|---|---|---|---|---|
| SPY | +0.226% | +0.126% | **+0.011%** | **−0.089%** |
| QQQ | +0.347% | +0.247% | **+0.086%** | **−0.014%** |

**Both indices are negative net expectancy in the current vol state.** The edge in this lane lives entirely in the MID (SPY +0.333 / QQQ +0.436) and HIGH (+0.334 / +0.520) terciles. The headline `GO` verdict is computed off the unconditional mean and does not condition on `vol_state`; the reported 88.3% / 85.0% gross win-rates further overstate a negatively-skewed short-vol strategy — Vilkov (2024) finds an unconditional 0DTE condor flips to negative net Sharpe once costs are charged.

A second, independent reason to stand aside: **QQQ's VRP is −0.0501 (PREMIUM_BUYING)** — realised vol is running 5 points *above* implied. Selling premium into that is selling something already cheap.

`pnl_basis`: percent-of-underlying-spot-notional, **gross**, from a `0.8×1σ` premium capture minus realised |open−close| — not premium-collected and not margin-relative, so even the positive figures are small in absolute terms.

**Recommendation: no 0DTE premium sale tomorrow in either index.** If the setup were taken anyway, the script's parameters are SPY: iron fly centred 777.7, wings ≈ ±0.8%, `size_scalar 0.5`; QQQ: centred 732.41, wings ≈ ±1.39%, `size_scalar 0.5`; enter at/after the open once the gap resolves, hold to the close, never carry overnight. **SPY ≈ SPX** (validated identical); **QQQ is the weaker of the two** (Nasdaq index book unavailable).

This lane is **advisory, delta-neutral, 0 rubric points, permanently** until both a vol-shock day enters the sample (the short-vol left tail is currently **UNSAMPLED**) and net expectancy clears a tail-aware bar. Win-rate is explicitly not the promotion metric.

> **Envelope traceability:** `decision.json` records `next_session_0dte_setup.backtest_verdict: "NO_GO_NO_EDGE"` and `sell_premium: false` on both indices — the **conditional** verdict adopted here. The script's own raw field returned the unconditional `GO_PREMIUM_SELL_INTRADAY`; the override and its arithmetic are carried in each index's `stand_aside_reason`.

---

## 2b. Swing Dealer Positioning (1–4 weeks)

All three indices printed the **identical shape** — positive DEX, a mid-week trough, and a hard rally into today: SPY $83.06B (+87% off the 08-11 trough), QQQ $62.22B, IWM $11.39B. That is **one macro dealer-flow event, not three independent theses**, and it should be read as such. Front-end IV ratios at `--near-dte 7` are calm across the board: SPY 0.798, QQQ 0.784, IWM 0.811 — all CONTANGO, no panic.

**Mechanized DEX-flip line (+1): exactly one name in the entire fleet qualified — TSLA.** Computed by `scripts/dex_flip.py`, not by hand:

```
TSLA net_dex 2026-08-12 −2,152,650,160 → 2026-08-13 +3,678,957,472; prior 3 sessions
(08-10 −235,433,700, 08-11 −59,167,640, 08-12 −2,152,650,160) all negative;
|flip| 3,678,957,472 vs floor 295,380,213 (0.25× trailing-10 median 1,181,520,851)
```

Magnitude ratio **12.45×** the floor — a clean clear. But `whipsaw_warning = True`: **5 sign changes across the 15-session window**, so this is "public delta positioning just crossed back to net-long inside a genuinely choppy book," not a one-way regime change. Per-strike GEX confirms it is not a single-strike artifact (top strike 335 carries only 17.4% of total). Front-end ratio 0.953 FLAT — no panic confirmation, so treat as early-stage.

**TSLA nonetheless failed the Step 3 confluence gate** (dealer-positioning was its only positive flag) and is therefore **not scored** — it appears in §8. The single best mechanized signal of the day earns nothing, which is the confluence gate working as designed rather than a defect.

**No vanna-squeeze fires anywhere.** The only put-heavy book in the fleet was GOOG, and its VIX leg is broken: VIX fell three straight sessions (08-10 15.46 → 08-11 15.28 → 08-12 14.55) then **rose** on 08-13 to 14.63. A squeeze precondition that is not currently intact is vanna *pressure*, not a squeeze — GOOG is skipped, not scored. Worth a re-check if VIX resumes a clean ≥3-session decline.

**Near-panic without a flip:** META (front-end 1.095) and SNDK (1.101) both breach the 1.05 threshold but are call-heavy, not put-heavy, and neither clears the flip test — SNDK's sign change landed on **08-12, not today**. Both are *watch*, not thesis.

**Data-quality flag carried through this whole section:** `gex-time-series`'s `zero_gamma_level` / `regime_flip_dates` are corrupted for most single names — MU spot $957 against a printed ZGL of $25.86; TSLA spot $339 against $89. This is the known ZGL-grid artifact, now confirmed on NVDA, MSFT, TSLA, PLTR, META, INTC, AAPL and GOOG in addition to the previously-tagged SPY/QQQ/IWM/MU. SPY and ORCL are the only clean exceptions. Everywhere else only `total_gex` sign and trend are reported, and ZGL-derived "regime flips" are marked UNRELIABLE.

---

## 2c. Sector Rotation

**Rotation regime call: `no_change`** (confidence: **low**).

Two sectors clear a full rotating-in call (Technology, Industrials — both cyclical, same direction), but **zero sectors clear a confirmed rotating-out call**. A rotation regime needs two coherent sides; with no confirmed OUT side this is broad risk-on concentrated in two sectors, not a rotation.

**⚠ The direction rule that governs this section (C55).** `sector-flow` and `sector-flow-persistence` are **one gross-turnover source**, not two — their `net_flow` is gross call$ minus put$ and is sign-agnostic with respect to buying versus selling. They cannot express direction. **Direction reads only off the netted `market-regime.sector_rotation`.**

Today `sector-flow` returned a **positive** gross figure for **all 11 sectors** (the floor is Real Estate at +$9.67M). Structurally, therefore, *any* sector the netted source calls OUT will always appear to "disagree" with gross — the disagreement is the mechanism, not a coincidence.

| Sector | Netted (authoritative) | Gross turnover | Persistence | Netted vs gross | Verdict |
|---|---|---|---|---|---|
| Technology | **+$322.3M IN** | +$3,015.1M | 1.0 | agree | **rotating_in** |
| Industrials | **+$96.0M IN** | +$505.5M | 1.0 | agree | **rotating_in** |
| Utilities | +$16.0M IN | +$35.5M | 1.0 | agree | watch_only — broad tape, not standout (rank 10/11) |
| Healthcare | **−$34.7M OUT** | +$402.2M | 1.0 | **disagree** | **watch_only** |
| Consumer Cyclical | **−$54.4M OUT** | +$277.8M | 1.0 | **disagree** | **watch_only** |
| Communication Services | **−$40.6M OUT** | +$210.5M | 1.0 | **disagree** | **watch_only** |
| Financial Services | no netted call | +$488.4M | 1.0 | n/a | no call |
| Energy / Basic Materials / Cons. Defensive / Real Estate | no netted call | +$223.7M / +$199.0M / +$52.0M / +$9.7M | 1.0 | n/a | no call |

**Persistence returned `1.0` and `trend: INFLOW` for all 11 sectors — zero discrimination.** It fired 11-of-11 and is treated as non-informative today. It cannot on its own satisfy the conditional sector-leader gate, and this is the first of **three** signals that fired on ~100% of their population today (see §6).

**ETF flow tape (advisory — 0 rubric points).** Ranked from `cumulative-premium-flow --days 5` across the canonical universe, then deep-pulled on the top/bottom 3:

| ETF | 5d net premium | Persistence | DP positioning | Options urgency | GICS agreement |
|---|---|---|---|---|---|
| SMH | +$23.55M (1) | **MIXED — not persistent** | large prints below mid → creation/redemption-flavoured | split ask/bid, no urgency | agrees in sign w/ Tech IN, but non-persistent ⇒ **weak confirmation only** |
| EWY | +$16.60M (2) | bullish, persistent | near mid, balanced | muted | **n/a** (Korea, geographic) |
| XLI | +$3.47M (3) | bullish, persistent | tight to mid | **entirely PUT, bid-side, Nov-dated** ($4.15M 180p, $2.22M 170p) | **AGREE** (Industrials IN) — but the put-heavy tape is a hedge/skew flag |
| XLV | −$4.53M | bearish, persistent | balanced churn | small call-only | corroborates Healthcare OUT — sector still watch_only per C55 |
| XLY | −$5.93M | bearish, persistent | one $28.3M print near mid | LEAP calls + small near-dated puts, mixed | corroborates Cons. Cyclical OUT — still watch_only |
| GDX | **−$47.02M** (largest move on the tape) | bearish, persistent | very large two-way prints ($188M/$163M/$137M straddling mid) — creation/redemption + hedging, **not** a clean read | calls dominate but split bid/ask | **n/a** — no netted Basic Materials call |

The most interesting line is **XLI**: the sector is netted-IN, the ETF's cumulative flow is persistently bullish, and yet **every one of its sweeps is a bid-side November put.** The sector desk is buying the constituents while buying downside protection on the wrapper. That is a hedge structure, not a directional bet — and it is the single most useful piece of context for RTX in §3.

**Named leaders** (Technology): SNDK +$126.4M, MU +$82.2M, CRWV +$42.7M, SMCI +$34.0M, MSFT +$33.0M, ORCL +$28.4M, APP +$23.4M, PLTR +$13.9M, HOOD +$12.2M. (Industrials): RTX +$115.9M, CAR +$12.2M. Sector inflow is **not uniform** — NVDA, AAPL, DELL, INTC, CSCO, AMAT, COHR, ARM, MSTR and LITE all show single-name net *selling* inside a net-inflow sector.

**Conditional sector-leader +1 — known defect, stated per name in §7.** Conditions (b) and (c) test the *identical field and identical threshold* as the standalone cum-flow rubric line, and condition (a) is non-discriminating today (1.0 for all 11). The quant found the defect is worse than a double-count: the gate carries **no intent screen and no scale-relative test**, so on RTX it paid +1 off flow the intent-screened line had *already rejected as arb*, and on SNDK it paid +1 off a net that is 2.33% of gross. **The line awarded 5 points across the union and not one was independent evidence.**

---

## 3. Swing Setups (1–6 weeks)

### 3a. Long swings (regime-aligned)

**EMPTY.** No long call survived the gate stack.

The nearest miss was **CRWV**, and it is worth recording exactly how it died, because the arithmetic is the day's lesson:

| Stage | Result |
|---|---|
| `raw_score` | **3** (LOW) — highest of 9 survivors |
| Components | +1 sector-leader · +1 oi-trend BUILDING · +1 cum-flow accretion |
| Genuinely independent evidence | **one line** (two of three are the same cum-flow field re-counted) |
| `win_rate` | 0.4507 (n=142, `backtest_clean`, market-wide) — **below the 0.50 floor** |
| `market_excess` | **−0.0845** — the class *loses to simply being long SPY* |
| pre-risk size | `starter` (one step above zero) |
| Gates fired | panic −1 (FER 1.631) · fundamentals CAUTION −1 · debate −1 (bear 0.45 ≥ bull 0.35) · event −0.5 |
| **final_size** | **`watch_only`** |

CRWV's cum-flow line was genuinely the cleanest in the union — **+$234.4M/30d and +$299.8M/90d at 6.77% of gross with `trend_direction: BULLISH`**, intent screen passed, and 10 consecutive bullish flow days on `uw historical trend`. Both debaters agreed it was real. It still could not survive, because one clean line against `D/E 6.4849` with a `current_ratio` of **0.4555**, persistent insider selling (MSPR −58.28 since mid-2025), two of the last four quarters missed by double digits, and a +24.56% five-day extension on **rv20 134.9** is not a trade.

**A finding the deep-dive added that the scoring did not see:** three of CRWV's top-five OI changes are **1-DTE (2026-08-14 expiry)** — `P00100000` +7,983, `C00120000` +7,241, `C00115000` +5,509. The "C95/P100 institutional cluster" both debaters anchored to is substantially **next-day gamma flow**, not a multi-day institutional build. Only the C95 leg (dte 8, +8,051) is a genuine swing-tenor build. This further hollows out an already-thin +1.

Invalidation had CRWV been taken, anchored to the real dark-pool level rather than a round number: **loses the $110.90 DP average-price shelf** (`total_premium` $852.3M across 3,627 trades), or the C95 strike on a daily close.

### 3b. Short / fade swings (defined risk only)

**MU — `watch_only`, not sized. Directional short routing (2026-08-01 audit P0 #1).**

This is **routing, not suppression**: the thesis is generated, scored, gate-verdicted and serialized in full so the counterfactual keeps resolving.

- **Thesis:** the largest non-index persistent bearish book in the market — sweep-persistence **5/5 sessions, $3.741B** — building into a **+4.23% 1d / +7.76% 5d rally**. Corroborated by accumulation-hunter: MU's mega-tier dark-pool `buy_ratio` is **0.102**, i.e. heavy institutional *selling*. Vol-surface has it KINKED at 8DTE (prominence 20.0%, implied move 8.9%).
- **`raw_score` −2** (DROP): `+1 oi-trend BUILDING` (5/5, **put-dominant** — P550 +11,301 / P600 +5,589, so the build is in the short direction and C4 opening is confirmed) minus **`−3 flow_conflict`** (cum_flow_30d **+$548.5M bullish against the short**, magnitude above the union median of $234.4M).
- **The flow_conflict is substantive, not merely mechanical.** Three independent sources contradict the short: sector-rotation names MU a *bullish* Technology leader (+$82.2M); cum-flow is net bullish on both windows; price is up on the day and the week.
- **Counterfactual recorded for the audit:** the sizing ladder would have said `half` (WR 0.5493, excess **+0.0775**, C4 confirmed, outside the anti-predictive band); the tier would independently have said DROP at raw −2. Both are preserved so the next audit can separate the routing effect from the scoring effect.
- **The uncomfortable observation:** MU is the **only name in today's book with positive market excess** (+7.75pp on n=142) and the best win-rate — and it is the one the routing rule refuses to size. That is the rule doing what the paired McNemar evidence (`ALL/short` p=0.0038, near-identical deficit in rising and falling tape) says it should. `bearish_flow` outperformance accrues to **nothing**: criterion C19 was **CLOSED as REFUTED** on 2026-07-25. Recorded as observation, not as an edge claim.

**Contrarian book: EMPTY, and the abort was principled.** `contrarian-scanner` returned zero fades. Reasons, stacked: (1) **VRP is negative on both indices**, and the −2 overcrowded-long rubric line *requires VRP positive* — so that line **did not fire today, full stop**; (2) **no name in the universe reached ±2σ** on `pc-ratio-zscore` (extremes were SNDK −1.63 and LULU +1.23, both well inside NORMAL); (3) the tape is broad, which is a *worse* fade setup than a narrow one; (4) the trend is UPTREND with SPY above both SMAs, so no naked shorts regardless. The one genuine price/flow divergence — **DELL**, price +25.4% over the flow window against net options flow of −$16.75M — is flagged as *watch for confirmation*, not a fade: single-name divergences of this kind bias toward informed **continuation**, not reversal (Pan-Poteshman 2006; Ge-Lin-Pearson 2016).

**Near-term sweeps (informational — 0 rubric points; the sweep-persistence line was removed 2026-05-23 P0.3 for −22pp marginal contribution across two audits).** Persistence-ranked, non-index:

| Ticker | Side | 5d cum premium | Persistence | Read |
|---|---|---|---|---|
| MU | bearish | $3.741B | **5/5** | largest persistent bearish book; flow/price tension — see above |
| SNDK | bearish | $1.816B | **5/5** | **data-quality flagged** — see §6 artifacts |
| PLTR | bullish | $1.205B | 4/5 | loudest bullish book of the day; scored **1** |
| ORCL | bullish | $291.5M | 3/5 | clears the bar, materially smaller |

Index/mega-cap persistence (SPXW, SPY, QQQ, NVDA, AAPL all 5/5 bearish) is demoted to a hedge-flow footnote — cum-flow alignment was not verified for those names, so they are not surfaced directionally.

---

## 4. LEAP Builds (6–24 months)

**EMPTY — zero qualifiers.** On a day when LEAPs were **4.2% of total volume**, this is the expected outcome, not a search failure.

Three names had genuine fresh DTE>180 builds and were run through the full 9-gate funnel. **All three failed the required accretion gate (Gate 4)** — the dispositive test — with the identical signature:

| Ticker | Build evidence | 90d cum-flow | net-as-%-of-gross | Gates | Verdict |
|---|---|---|---|---|---|
| **TLT** | two fresh ask-side call builds, dte 308 & 526, strike 80 (`prev_ask_volume` 10,008/48 and 10,020/72 — strong ask dominance); oi-trend BUILDING 10/10 | **−$147.5M**, MIXED | **3.2%** | ≤2-of-9 | **DISQUALIFIED** |
| **DRAM** | put, dte 855, `oi_diff_plain` 6,885 | **−$74.7M**, MIXED | **1.0%** | ≤1-of-9 | **DISQUALIFIED** — also `consecutive_build_days: 1`, a one-day spike, not persistence |
| **GOOG** | oi-trend BUILDING 10/10, net_oi_change +40,150 | **+$34.9M**, MIXED | **0.22%** | 1-of-9 | **DISQUALIFIED** — roll `balance_ratio` 0.648 below the 0.7 bar; 30d sign-flips vs 90d |

Every candidate showed **balanced two-way flow netting to a small residual** — the same put-sale-netting signature that contaminates SNDK. TLT's is the most instructive: real ask-side call conviction at dte 308/526 sitting inside a book where bullish and bearish premium are essentially balanced ($4.66B combined gross), which reads as two-way rate-view positioning — calls for a dovish pivot against puts hedging sticky inflation, consistent with the 10Y at 4.68% and rising — not directional accumulation.

Also excluded: **IBIT and FXI** long-dated puts from `oi biggest-increases`, where `oi_diff_plain` of 9,000–24,000 sits against `prev_ask_volume + prev_bid_volume` of **~20 total** — an OI/volume mismatch consistent with an off-tape block, not a coherent lit build.

The `+1 conviction-matrix DIRECTIONAL_LONG` rubric line is **LEAP-conditional**; with zero LEAP qualifiers it awards **0 on every name in the book**.

**Monitoring note only (not a call):** TLT's ask-side call build at dte 308/526, strike 80, is worth watching for a break toward directional net flow if rate-cut conviction firms.

---

## 5. Volatility Surface

**Net read: no genuine event-driven vol dislocation today.** The backwardation visible almost everywhere is dominated by the PPI-day front tenor and Aug-21 OPEX gamma mechanics, not mispriced tail risk.

**Raw-vs-hygiene disagreement (14 names scanned) — the substrate hygiene pass is itself the finding:**

| Metric | Count |
|---|---|
| Kink-aware `shape` flipped from `raw_shape` | **7 of 14** — SOXL, LCID, DOCS, PLTR, MU, IWM, SPY |
| Monotonic `base_shape` flipped from `raw_shape` | 4 of 14 — DOCS, QQQ, PLTR, SPY |
| `base_shape` distribution after hygiene | **BACKWARDATION 14/14** |

The 14/14 BACKWARDATION `base_shape` is itself a mechanical artifact, not a signal: `base_shape` is a first-two-tenor slope, mostly DTE1 vs DTE8, and **DTE1 is tomorrow's PPI-adjacent expiry**. Half the raw labels flipped once the 0DTE/expired bucket and sub-15-contract tenors were dropped. Classifying from the raw label today would have been wrong in 7 of 14 cases.

**KINKED names — all OPEX mechanics, none with an earnings catalyst.** Every kink lands on or near the Aug 21 monthly OPEX tenor. Checked against `earnings_catalyst.json`: **none of the six has an earnings date in the window.** These are gamma/pin mechanics, not event-vol mispricings, so no hand-off to earnings-scout and no event-vol claim.

| Ticker | raw → hygiene shape | kink DTE | prominence | FER @7DTE | IV %ile (z) | implied move | Note |
|---|---|---|---|---|---|---|---|
| SPY | CONTANGO → KINKED | 8d (08-21) | 11.0% | 0.797 | 1.16 (−1.14) | 1.6% | OPEX pin |
| QQQ | KINKED → KINKED | 8d | 14.1% | 0.784 | 1.16 (−1.79) | 2.3% | OPEX pin; VRP-aligned side is **long** vol |
| IWM | BACKWARD. → KINKED | 8d | 31.1% | 0.811 | 0 (−1.73) | 1.95% | OPEX pin |
| MU | BACKWARD. → KINKED | 8d | 20.0% | 0.864 | 5.81 (−1.84) | 8.9% | OPEX pin |
| SOXL | BACKWARD. → KINKED | 22d | 5.1% | 1.12 | 15.12 (−1.25) | 23.9% | 3× leveraged — scale accordingly |
| LCID | BACKWARD. → KINKED | 29d | 49.5% | 0.543 | 18.6 (−0.83) | 13.5% | **44-contract tenor — do NOT size off this kink** |

**BACKWARDATION calendar candidates — all `watch_only`.** Clean reads where raw, hygiene and base labels agree:

| Ticker | FER @7-8d vs 29d | IV %ile (z) | implied move | Status |
|---|---|---|---|---|
| COHR | 1.096 | 0 (−2.29) | 13.2% | calendar candidate, cleared <1.10 |
| CRWV | 1.079 | 1.16 (−1.65) | 12.7% | calendar candidate |
| SMCI | 1.076 | 22.09 (−0.82) | 13.4% | calendar candidate |
| SNDK | 1.101 | 2.33 (−1.31) | 14.9% | **borderline — do not fade yet** |
| LITE | 1.119 | 0 (−2.39) | 13.7% | **borderline — above 1.10 disqualifier** |
| RBLX | 1.023 | 2.33 (−1.46) | 8.8% | edge marginal, advisory only |

**None of these is sized**, for two reasons. First, the calendar-entry disqualifier requires the front-end ratio to be **falling** (panic resolving), and only a single-session snapshot exists — a second session is needed to confirm decay rather than build. Second, a textbook calendar is net-short-vega at initiation, which runs **against** today's negative VRP; if taken at all these should be structured as ratio/1×2 calendars that stay net-long back-month vega rather than flat short-vol.

**Earnings vol (thin week).** Only 3 of 114 catalyst names intersect the C12 universe:

| Ticker | Verdict | Earnings | Days | Implied move | Shape | Reasoning |
|---|---|---|---|---|---|---|
| **ULTA** | **SELL VOL, half** | 2026-08-27 | 14 | **9.5%** | KINKED @15d, prominence 12.6%, **615 contracts** | Real kink on strong liquidity; back-month skew +0.0086 = COMPLACENT, tail unpriced ⇒ capped at half; negative index VRP is a headwind |
| **BABA** | **CALENDAR** | 2026-08-20 | 7 | **7.3%** | BACKWARDATION, no kink; **FER 1.312** on 7,092 contracts | Genuine front panic persisting into the event; sell rich front / buy cheaper back |
| **BURL** | **SKIP** | 2026-08-27 | 14 | 9.7% | KINKED @15d, prominence **26.7%** — strongest of the three | **39-contract tenor, <$2M total flow** — mechanically passing but practically unpriceable. Same trap class as the FDX 11-contract lesson |

All three failed the confluence gate (earnings-scout was the sole flagging agent on each) and appear in §8. `earnings_vol` is **not** among the 5 classes `signal-backtest` supports ⇒ its win-rate can only ever be `NA(substrate)`; the class also caps at 0.55, landing it in the anti-predictive band ⇒ starter at most.

**IV outliers:** only two universe hits, both QQQ, both today's 0DTE expiry ($91.7K and $728.8K premium). Deep-wing 0DTE prints on PPI day — classic wing noise, **not actionable**.

---

## 6. Risk & Correlation

**Macro headline:** yield curve normal (+0.48), 10Y **4.68% and rising**, USD weakening, core PCE **3.29%** against core CPI 2.79% — the gap is not converging — unemployment 4.1% with payrolls **−23k**. Rising long end plus negative payrolls at a 3.63% funds rate is stagflation-lite. Forward calendar per §1: nothing at ≤T+5; OPEX T+6, PCE+GDP T+9, Jackson Hole T+10…12.

**Breadth cross-check (advisory):** `fz` 319 advancers / 183 decliners, **63.4% green**, avg +0.76%. `divergence_flag: false` on the narrow test. But UW flow breadth is **35% bullish** — price participation broad, options positioning net bearish. Recorded as the real divergence; it does not change sizing.

### Correlation clusters

`uw risk portfolio-correlation` against today's 9 candidates (not the static watchlist), 30d lookback. Sector metadata returned `Unknown` for all nine — a tool limitation that makes the built-in concentration warning uninformative, though the pairwise coefficients are sound.

**`AI_infra_semis_cluster` — transitively linked, treat as ONE position: {CRWV, SNDK, MU, QQQ, ORCL}**

| Pair | Corr |
|---|---|
| SNDK / MU | **0.901** |
| SNDK / QQQ | 0.787 |
| QQQ / MU | 0.743 |
| CRWV / ORCL | 0.721 |
| CRWV / SNDK | 0.708 |
| CRWV / MU | 0.708 |

Kept member: **CRWV** (raw 3, highest — no tiebreak needed). SNDK, MU, QQQ and ORCL each took `−1 tier`. Soft-watch band 0.60–0.70 (CRWV/QQQ 0.693, ORCL/QQQ 0.683, CRWV/SMCI 0.679) carries **no penalty**. MSFT, PLTR and RTX have no pair ≥0.70.

**The practical read: five of nine candidates were one bet.** A nine-name candidate list was never as diversified as it looked.

### Fundamentals verdicts (top 5)

No VETOs — none of the five met the mechanical ≥2-of-3 contradiction bar. But **four of five CAUTION**, and the contradicting leg is the same one almost every time.

| Ticker | Verdict | Adj | Contradicting facts |
|---|---|---|---|
| CRWV | CAUTION | −1 | Insider MSPR **−58.28** persistent since mid-2025 · **D/E 6.4849, current_ratio 0.4555** (the enrichment script mislabels this "low"; raw metrics and independent coverage disagree) · fresh $2.6B delayed-draw term loan · **2 of last 4 quarters missed** (−22.3%, −11.2%) |
| RTX | CAUTION | −1 | Caution is on the **flow thesis, not the business** (business is CONFIRM-quality: 4/4 beats, insider **BUYING** +41.12, D/E 0.58, $289B backlog, live Pentagon contract flow). `fz` puts ex-div at **Aug 14**; the headline print expires **on Aug 21 OPEX** |
| SNDK | **CONFIRM** | 0 | Real dated Investor Day catalyst (FY2030 50% FCF margins) · 4/4 beats · **squeeze hypothesis explicitly REFUTED** (short_float 4.67%, days-to-cover 0.51) |
| MSFT | CAUTION | −1 | Insider MSPR **−83.89**, heaviest in the group · put-dominant OI build against a long thesis · `catalyst_support: none` · ex-div 2026-08-20 unconfirmed |
| PLTR | CAUTION | −1 | Insider MSPR −38.74 **corroborating the −$62.1M 90d flow flip** · PE 143.2x / PS 96.5x · `catalyst_support: contradictory` (Burry named PLTR while loading QQQ puts) |

The CRWV and PLTR cautions are the informative ones: insider selling and the flow record point the **same** direction, which is exactly the configuration this gate exists to catch. Note also that `fz`'s analyst axis (`recom`, `upside_to_target_pct`) came back `null` on all five — the known upstream gap, unrecoverable, not absent-by-choice.

### Debate-disconfirmation cuts — **the gate fired on all five**

| Ticker | bull | bear | Gate | Bear's strongest surviving point |
|---|---|---|---|---|
| CRWV | 0.35 | **0.45** | CUT | The 3 points collapse to one signal wearing three hats; one clean flow line against 6.5× leverage and a sub-1 current ratio |
| SNDK | 0.35 | **0.65** | CUT | Call-lean OI admits a **call-overwriting** reading (selling upside into strength) that OI alone cannot distinguish from accumulation |
| PLTR | 0.25 | **0.65** | CUT | 90d flow **−$62.1M** while price makes highs, corroborated by insider selling and fundamentals CAUTION — three independent channels converging |
| MSFT | 0.35 | **0.75** | CUT | "Zero DEX sign changes" is the **absence** of the thing the rubric scores — the null hypothesis wearing a signal's clothing |
| RTX | 0.25 | **0.85** | CUT | Both surviving components trace to the same arb structure; the bull's own proposed structure ("wait for Aug 15+, require a close back above 220.48") **is a no-trade structure in bull clothing** |

No round-2 escalation qualified (requires both residuals within one bin *and* ≥0.75). **Not one bull cleared 0.35** — no advocate could make their case even at half-conviction. CRWV was BOTH_SIDES_LOW (0.35/0.45): neither side cleared a coin flip, which is the strongest kill signal the debate produces.

### ⚠ Three signals fired on ~100% of their population today

This is the day's most significant instrumentation finding and all three should be graded together:

1. **`sector_flow_persistence` = 1.0 for all 11 sectors** — `trend: INFLOW` on every one.
2. **`oi-trend BUILDING` fired 9-of-9** across the scored union with `consecutive_build_days: 5` on **every single name** — criterion C47 replicating exactly. It contributed +1 to all nine and discriminated nothing.
3. **NEW — single-name `front_end_iv_ratio` breached 1.10 on 8 of 9 names** (SMCI 1.788, COHR 1.657, CRWV 1.631, SNDK 1.531, MSFT 1.439, PLTR 1.300, ORCL 1.278, RTX 1.224; only MU at 1.080 cleared) **while both indices printed CONTANGO/FLAT** (SPY 0.91, QQQ 0.978). A gate that fires on 8-of-9 names against calm indices is not detecting eight independent panics — it is measuring a thin 1DTE single-name near-leg, the same class as the known no-near-dated-tenor artifact. **Recommend the next `/calibration-audit` grade single-name `front_end_iv_ratio` for population-wide firing the way C47 was graded.** It did not change today's sizing (the fires were redundant, not load-bearing).

### Adverse-flow exit candidates (rolling `conviction_*` groups)

| Ticker | From | Status |
|---|---|---|
| **EWY** | 2026-08-12 | **EXIT — hard.** `flow_direction: bearish`, net_flow −$1.07M, P/C 0.708 against yesterday's long thesis. Two HIGH-severity alerts: `LARGE_DARK_POOL` ($41.3M single print, $192.6M total DP premium) and `OI_SHIFT` (+56,746). A $41M single DP print alongside a flow-direction flip **one day after entry** is distribution |
| **AVGO** | 2026-08-04 | **EXIT — soft.** Bearish flow, net −$884.5K, P/C 0.972 (near parity). Decayed off-thesis with no hard alert — precisely what `scan` exists to catch |
| NBIS | 08-04, 08-11 | On-thesis. Bullish +$6.67M, P/C 0.84, OI +121,861 (largest build in the carried set). Cap drift $48.6B→$65.2B is price appreciation, not adverse |
| MSFT | 2026-08-10 | Flow on-thesis (+$32.99M) — but today's fundamentals gate independently returned **CAUTION on insider MSPR −83.89**, which the flow-only alert channel cannot see. **Advisory adverse-fundamentals watch** |
| ZTS, LRCX | 08-05, 08-04 | On-thesis, no action |

### Hedge sleeve

**None required — the post-gate book is flat.** Net delta is zero and directional skew is undefined; proposing a hedge against an empty book would be manufacturing exposure, not managing it.

For the record, **if** a book existed, the VRP-aligned hedge today is **long vol, not short**: VIX 14.63, QQQ IV 18.82% vs realised 23.83%, negative VRP on 8 of 9 names, and PCE+GDP (T+9) plus Jackson Hole (T+10…12) clustered just past the OPEX unpin. That is a cheap-convexity configuration. Flagged as context for tomorrow; **it carries none of the 9-gate approval.**

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**EMPTY — no name reached raw_score ≥ 7.** The Step 3a load-bearing-tool gate (3-of-4) never engaged because no call approached raw ≥ 9. Step 6.5's batched `uw playbook batch-scan` was **skipped** — it operates on the raw ≥ 7 list, which is empty. Step 8.5's `/stock-deep-dive` hand-off is **skipped** per the command's no-edge-day rule (no HIGH-tier names).

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: not computed this session. There are no HIGH/MEDIUM rows to display it against, and the rolling `conviction_<date>` closed-call set has not accumulated resolutions since the last audit. The C3 fractional-Kelly sizer remains ADVISORY until tier×expectancy is monotone on n≥30.

### Full scored book (for audit; all below the §7 threshold)

| Ticker | Dir | raw | Tier | Class | cum_flow_30d (net-%-gross, trend) | win_rate (n, source) | excess | pre-risk | Fund. | Debate (b/br) | Gates fired | **final** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CRWV | long | 3 | LOW | `bullish_flow` | +$234.4M (6.77%, BULLISH) | 0.4507 (142, clean) | −0.0845 | starter | CAUTION | 0.35/0.45 | panic, fund, debate, event | **watch_only** |
| RTX | long | 2 | DROP | `sector_rotation` | +$114.2M (20.23%, BULLISH) — **intent screen FAILED** | null (NA(substrate)) | null | skip | CAUTION | 0.25/0.85 | panic, fund, event(−1), debate | **skip** |
| SNDK | neutral | 1 | DROP | `bullish_flow` | +$1,258.3M (**2.33%**, MIXED) | 0.4507 (142, clean) | −0.0845 | skip | CONFIRM | 0.35/0.65 | panic, cluster, debate | **skip** |
| MSFT | long | 1 | DROP | `sector_rotation` | +$681.8M (4.17%, MIXED) | null (NA(substrate)) | null | skip | CAUTION | 0.35/0.75 | panic, fund, debate | **skip** |
| PLTR | long | 1 | DROP | `bullish_flow` | +$195.0M (2.59%, MIXED); **90d −$62.1M** | 0.4507 (142, clean) | −0.0845 | skip | CAUTION | 0.25/0.65 | panic, fund, debate | **skip** |
| ORCL | long | 0 | DROP | `sector_rotation` | −$75.2M (−1.17%, MIXED, OPPOSES) | null (NA(substrate)) | null | skip | NA | — | panic, **vrp**, cluster | **skip** |
| SMCI | long | 0 | DROP | `sector_rotation` | +$32.7M (2.74%, MIXED) | null (NA(substrate)) | null | skip | NA | — | panic | **skip** |
| QQQ | long | 0 | DROP | `multileg_directional` | −$294.8M (−0.52%, MIXED, OPPOSES ⇒ −3) | null (NA(substrate)) | null | skip | NA | — | cluster | **skip** |
| MU | **short** | −2 | DROP | `bearish_flow` | +$548.5M **bullish vs short** ⇒ −3 | 0.5493 (142, clean) | **+0.0775** | watch_only | NA | — | regime, cluster | **watch_only** (routing) |

`Σ score_components[].points == raw_score` verified on all 9. Every quote ≤0.80; every `win_rate_source ∈ {backtest_clean, NA(substrate)}` (zero retired values); the sub-0.50 floor held on all three 0.4507 rows.

**Instrumentation gap (3rd+ consecutive cycle):** `dp_block_to_float_ratio` and `insider_cluster_flag` are `null` on all nine — emitted as explicit `null`, not absent. Today's cause is **legitimate upstream disqualification** (every accumulation candidate was disqualified before the float/insider lane ran), not the emitter bug that blocked C16/C18 previously. **C16 and C18 remain ungradeable.**

### Conviction-scoring rubric — version `2026-06-12` (FROZEN), embedded verbatim

```
Daily conviction score = Σ:
  +1  MECHANIZED DEX flip / vanna-squeeze in trade direction — verified SIGN CHANGE, never a level:
      sign(net_dex) on the latest session opposite to ≥3 consecutive prior sessions, from dated
      `uw options-structure dex --date` calls, with |net_dex| on the flip day ≥ 0.25× the trailing-10
      median |net_dex|. Computed by scripts/dex_flip.py, never by hand. Vanna disjunct needs a dated
      VIX source for the falling-VIX leg.        # DEMOTED +3→+1 and MECHANIZED 2026-06-12 P0.4
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified
      institutional-tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d
      confirms (sign aligned AND |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1. A sub-$50M
      flow that halves this line does NOT separately qualify for the +1 cum-flow line.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  conviction-matrix DIRECTIONAL_LONG confidence>70 — CONDITIONAL: awards only when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +1  cumulative-premium-flow net directional accretion (30d) — INTENT-SCREENED: award only when
      (a) no C28 distribution_flag, AND (b) on dividend payers in an ex-div window the accreting
      prints are NOT deep-ITM sub-parity calls. Screen failed/unevaluated on a flagged name → 0.
  +1  sector-rotation names ticker as single-name leader in a rotating sector — CONDITIONAL:
      (a) sector persistence_score ≥ 0.6 AND (b) cum_flow_30d direction aligned AND (c) ≥$50M.
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored play type)
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist top-5 (OPEX week only)
  -2  contrarian-scanner overcrowded long with RISING pc-ratio-zscore (requires VRP POSITIVE)
  -3  flow_conflict — cum_premium_flow 30d direction clearly opposite dominant_signal_class
      (sign flip + magnitude > union-median |cum_flow_30d|, or explicit OPPOSITE label)
  -1  flow_conflict_lite — 30d read MIXED (signed sum near zero, or aligned but bottom-quartile)
      ** -3 and -1 are MUTUALLY EXCLUSIVE — apply ONE, never both. **
# REMOVED: signal-confluence ≥4 (+2) removed 2026-06-12 P0.2 — server-side re-count of already-scored
#          quantities; tool keeps exactly one role, the Step 0 funnel seed.
# REMOVED: sweep-persistence top-5 (+1) removed 2026-05-23 P0.3 — −22pp marginal, two audits.
# REMOVED: gamma-flip 0DTE breakout (+2) removed 2026-05-09 — §2 is advisory, 0 points.
# TIER GATES (risk-monitor, Step 2d — NOT score_components, contribute 0 to raw_score):
#   -1 TIER  correlation cluster (pairwise corr ≥ 0.70)
#   -1 TIER  market-regime conflicts with trade direction
```

**Tiers:** `≥9` HIGH (full) · `7–8` MEDIUM (half) · `3–6` LOW (starter/watch) · `≤2` DROP.
**Tier-cut status:** the ≥9 HIGH cut failed its scheduled re-confirmation on 2026-06-12 (bands inverted: HIGH 0.222 / MED 0.214 / LOW 0.444). Cuts are retained under the P0.1 freeze but carry **no validated ranking claim**; the P0.6 out-of-regime guard caps all sizing at half in the interim.

---

## 8. Watch-only — single signal, no confluence

Failed the Step 3 confluence gate (fewer than two distinct Phase 1 agents flagging in the same direction). **Listed for journaling, NOT for trade entry today.** Two of these are the best-evidenced findings of the entire session, which is worth sitting with.

| Ticker | Flagging agent | Finding |
|---|---|---|
| **CSCO** | accumulation-hunter (only) | **The single cleanest accumulation read fleet-wide — and it scores nothing.** All three DP tiers simultaneously bullish and mutually consistent (mega 0.679/6/$107.3M · block 0.629/107/$228.6M · large 0.603/4,538/$862.4M); buying genuinely distributed across the session (dominant price level only **4.05%** of DP premium, vs MSFT's 40.9%); institutional-accumulation ACCUMULATION with buy/sell 1.60; oi-trend BUILDING 5/5 with today's build (+138,650) an order of magnitude above the prior four sessions; 30d price flat +0.69% — the textbook quiet-before-a-move signature. Independently flagged by `daily-synthesis` on three HIGH-severity alerts. **Caution:** options premium is modestly net *bearish* (−$13.17M, P/C 0.58) — a real divergence. **Invalidation if ever taken: loses the $112.30–112.53 DP shelf** where institutions bought the intraday dip |
| **TSLA** | dealer-positioning (only) | **The only mechanized DEX flip in the entire fleet** (+12.45× the magnitude floor, evidence string in §2b) — but `whipsaw_warning = True`, 5 sign changes in 15 sessions, and front-end 0.953 FLAT gives no panic confirmation. Also carries a Tier-1 single-leg CONTRARIAN_SHORT put co-flag (DTE 8, size/OI 1.31), i.e. the two signals point opposite ways |
| **VALE** | multileg (only) | Two directional structures, cleanest `multileg_ratio` in the book (0.986–1.0): a bear put spread (Aug-21 P21/P16, $10.5M/$2.5M, 8DTE tactical) **and** a bullish Dec-18 three-way risk reversal (short P13 financing long C14/C16). Genuinely opposite at different horizons |
| **NVDA** | multileg (only) | Family of vertical call spreads across three tenors sharing a common 270C wing (09-04 240C/270C $11.6M; 09-18 225C/270C $25.6M; 09-25 260C/270C $3.4M). Side data unavailable — the long/short leg assignment is **inference, not fact**. Post-event positioning, not an earnings play. Counterweight: NVDA's mega-tier DP `buy_ratio` is **0.032** — heavy institutional selling |
| **ULTA** | earnings-scout (only) | SELL VOL half — kink @15d on 615 contracts, implied move 9.5%, earnings 2026-08-27 |
| **BABA** | earnings-scout (only) | CALENDAR — FER 1.312 on 7,092 contracts, implied move 7.3%, earnings 2026-08-20 |
| **BURL** | earnings-scout (only) | SKIP — strongest kink (26.7%) on the thinnest tenor (39 contracts) |
| COHR, LITE, RBLX, SOXL, LCID | vol-surface (only) | Calendar/kink candidates, all `watch_only` pending second-session FER-decay confirmation |
| **DELL** | contrarian (only) | Price +25.4% over the flow window vs net options flow **−$16.75M**, IV rank 76.5 — genuine divergence, flagged as **watch for continuation**, not a fade |
| XLF | multileg (only) | 57P Sep-18/Oct-16 calendar, ratios 0.985/0.992 — **non-directional**, earns no +2. Raw label BACKWARDATION is a dte-1 artifact; cleaned curve is CONTANGO ⇒ vol-mispricing play |
| TLT, DRAM, GOOG | leap-radar (only) | LEAP builds disqualified on the accretion gate — see §4 |
| **GOOG** | dealer-positioning (only) | Only put-heavy book in the fleet ("classic vanna-squeeze setup if VIX collapses") but the VIX leg broke on 08-13 and current DEX is NEGATIVE — vanna pressure, not a squeeze. **Re-check if VIX resumes a ≥3-session decline** |

**Dropped by the C12 liquidity floor** (price ≥ $5 AND 20d dollar-ADV ≥ $50M), never scored: TRIN ($20.4M ADV), QMCO ($35.8M), TXO ($2.1M), KURA ($13.1M), REAL ($40.9M), CLBT ($37.4M). 71 of 77 names passed.

---

## Appendix — substrate defects and artifacts recorded this session

Logged for `/calibration-audit`. Every one was caught before it entered a scored line.

1. **`fz` doubled-first-letter ticker bug is LIVE again on the `screen` surface** — today returned `QQMCO` (=QMCO), `AANRO` (=ANRO), `IIMC` (=IMC), `AABCL`, `AABEO`. The `breadth` surface is clean. This bug previously blocked C16 for 4 audits and corrupted the C18 insider store 100% for 5. **Never match an `fz` ticker with `==`.**
2. **`top_premium_trades` returned `ticker: null` on all 20 rows.** The largest tickets (strike-7000 calls, strike-8000 puts, expiries 08-21/09-18/10-16) are unattributed **SPX** index prints. No single-name attribution was made from them.
3. **Un-split-adjusted strike grid, SNDK:** a strike-3480 put at `avg_price` 2283.06, exp 2028-12-15, on a stock at $1528. Rejected. It is folded into the sweep-persistence tool's $1.816B SNDK aggregate, so that whole line carries reduced confidence.
4. **Put-sale netting confirmed live on SNDK** (the standing blind spot): 30d net $1.258B on $27.57B gross bullish / $26.31B gross bearish = **2.33% of gross**, `trend_direction: MIXED`. The union's largest headline flow number and its emptiest.
5. **Dividend-capture arb caught on RTX** — `fz` ex-div **2026-08-14** (tomorrow); the $40.2M ask-side deep-ITM strike-200 call (spot 220.48, 295.8× ask/bid, exp on OPEX day) is **35% of net 30d flow**. The NEE 2026-06-04 signature. The intent screen zeroed the +1. *Caveat:* Finnhub has no ex-div field, so the date is `fz`-sourced and unconfirmed — and `fz` is exhibiting the bug in item 1, so this warrants verification rather than blind trust.
6. **Three signals fired on ~100% of population** — sector persistence 11/11, `oi-trend BUILDING` 9/9 (C47 replicating), and single-name `front_end_iv_ratio` 8/9 against calm indices (NEW — recommend grading).
7. **`iv-percentile-zscore` returned `dates_used: 86` against a 252-day request** on all 14 names — every percentile and z-score in §5 is **PROVISIONAL**, below the 120-day first-class floor.
8. **QQQ `zero_gamma_level` = 211.28 against spot 732.33** (71% below) — extrapolation artifact, discarded. ZGL corruption now confirmed on NVDA, MSFT, TSLA, PLTR, META, INTC, AAPL, GOOG in addition to SPY/QQQ/IWM/MU.
9. **`front-end-iv-ratio` CLI default `--near-dte 1` snapped to the PPI-contaminated 1DTE bucket on 12 of 14 names**, reading false "panic" at 1.08–1.79. Re-derived at `--near-dte 7` the picture is calm and differentiated. Always read at 7.
10. **`earnings_catalyst.implied_move_perc` is a uniform ~1.45% across BABA/ULTA/BURL** despite very different underlyings, IVs and DTEs — inconsistent with an earnings-specific ATM straddle calculation. Substituted kink-tenor straddle approximations. Worth a substrate audit.
11. **`uw insights analyst-vs-flow` returned no analyst-side field** on any ticker — only `options_flow`. The analyst-vs-flow divergence signal, described as the highest-EV earnings setup, is currently **unmeasurable**.
12. **`portfolio-correlation` returned `sector: Unknown`** for all nine candidates, making its built-in concentration warning uninformative (pairwise coefficients are sound).
13. **CRWV's OI "build" is substantially 1-DTE** — 3 of its top 5 OI changes are the 2026-08-14 expiry. Only the C95 leg (dte 8) is a genuine swing-tenor build. Found in Step 6, after scoring.
14. **`signal-backtest` supports only 5 classes** (`bullish_flow`, `bearish_flow`, `high_iv_rank`, `volume_spike`, `dark_pool_accumulation`). `sector_rotation`, `multileg_directional` and `earnings_vol` can only ever be `NA(substrate)` — that covered **5 of today's 9** scored names.
