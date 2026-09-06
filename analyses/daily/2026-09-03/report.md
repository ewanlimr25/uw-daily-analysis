# Daily Market Analysis — 2026-09-03

## Executive Summary

- **Regime + GEX state:** Price tape is an **UPTREND day-one reclaim** — SPY 773.17 (+1.05%) back above its true 20dma (769.21) and 50dma (756.14) after two sessions below; QQQ 717.41 (+1.15%), IWM +1.18%, RSP +0.46% (broad, not cap-weighted-only), VIX 14.32 (−5.79%). Both index gamma books flipped positive today but are **one session old and unstable**. Sector lean: Technology is the only rotation where netted and gross agree, and it is **bifurcated** — mega-cap accumulating while the semis basket is actively put-hedged. **⚠️ The `market-regime` tool's own `trend: DOWNTREND` is a broken artifact and is used nowhere in this report** (§1).
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current UPTREND-reclaim/TRANSITIONAL) — sizing capped at half`. Non-binding today: nothing reached half.
- **Next-session GEX (SPY/QQQ):** SPY — long-gamma, ZGL 774.24 (reliable, 0.18% from spot), call wall **773 essentially on top of spot**, put wall 760 → tight-pin read. QQQ — long-gamma by `total_gex` sign only (ZGL 276.37 is a 61%-off artifact, disregarded), call wall 720 just 0.36% above spot vs put wall 700 → **asymmetric, upside-capped**. Advisory, 0 rubric points, see §2. **NFP at 08:30 ET tomorrow voids both maps on any gap beyond ~2%.**
- **Top swing build:** **None sized.** The highest-scoring name in the book reached raw_score 3 (LOW). The best-evidenced structure — IWM's three-expiry bear put ladder, the only genuine multi-day build on the tape — routes to `watch_only` as a directional short.
- **Top LEAP candidate:** **None.** `leap-positioning-radar` returned a clean empty board: every DTE>180 build failed the cum-flow accretion gate (§4).
- **Biggest risk:** **Nonfarm payrolls, 08:30 ET tomorrow (T+1)** — the binding event-risk severity on every call with a horizon past tomorrow, and the reason two structures in this book expire directly into an unhedged Tier-1 print. No hedge sleeve is recommended, because there is no sized exposure to hedge (§6).

**Sized positions: zero. This is the 42nd consecutive empty-sized daily board** (re-derived by globbing `analyses/daily/*/decision.json` only; last sized daily 2026-07-07). The two names carrying a non-`watch_only` pre-risk size — MSFT and MSTR — were gated to `skip` by **three and four independent tier deductions respectively, before any routing rule was reached**. The routing rules did not empty this board; the gate stack did.

---

## 1. Regime & Gamma State

### ⚠️ Substrate correction that governs this whole section

`uw risk market-regime` reported `trend: DOWNTREND`, `above_20sma: false`, `above_50sma: false`, `change_30d_pct: −100`, `pct_from_90d_high: −100`. **All of it is false, and the mechanism is now proven to the cent: the tool ingested SPY's close as 0.00.** Forcing today's bar to zero in the real 60-bar close series reproduces the tool's output exactly — SMA20 → 730.55 (tool printed 730.55) and SMA50 → 740.67 (tool printed 740.68). Each reported SMA is dragged down by `true_close / window`.

| field | tool | truth (`uw historical trend --days 60`) |
|---|---|---|
| SPY close | **0.00** | **773.17** (+1.05% from 765.16) |
| SMA20 | 730.55 | **769.21** → SPY **+0.52%** above |
| SMA50 | 740.68 | **756.14** → SPY **+2.25%** above |
| trend | DOWNTREND | **UPTREND — but a day-one reclaim** |

Recent closes: 08-27 771.10 · 08-28 769.35 · 08-31 767.05 · **09-01 761.78** · **09-02 765.16** · 09-03 773.17. SPY spent 09-01 and 09-02 *below* the 20dma and reclaimed it today. The prior session's envelope already carried `PULLBACK_IN_UPTREND`; today is the reclaim, not a comfortable trend, and it is sized accordingly.

The **same zeroed-price failure** hit `uw insights price-vs-flow` (`price_end: 0`, `price_change_pct: −100` on 13 of 13 symbols) and **leaked into the `signal-backtest` substrate** (3 result rows carried `price_after_5d: 0` / `pct_change: −100` — missing bars, not −100% moves; the quant dropped them before recomputing).

### The day's central tension: price breadth vs flow breadth

| lineage | reading |
|---|---|
| **fz price breadth** (independent source) | **67.59% green** — 340 advancers / 161 decliners of 503, avg +0.70%, median +0.64% |
| **uw options-flow breadth** | **35.9% bullish** — 2,260 bullish vs 4,032 bearish flow tickers of 6,292 |

Price participation is broad while flow positioning is defensive. This is not the classic distribution tell (green index with sub-50% advancers); it is the cross-lineage version — participation is real, but the options market is not paying for upside.

### Per-index gamma (current-state EOD book; §2 carries the forward read)

| index | spot | zero-gamma | total GEX | regime (by sign) | call wall | put wall |
|---|---|---|---|---|---|---|
| SPY | 772.88 | 774.24 (reliable) | **+$1.070B** | POSITIVE | 773 | 760 |
| QQQ | 717.41 | 276.37 (**unreliable — 61% off, disregarded**) | +$359.8M | POSITIVE | 720 | 700 |
| IWM | 295.08 | 170.06 (**unreliable — 42% off, disregarded**) | **−$870.1M** | **NEGATIVE** | — | — |

IWM matters for §3: `total_gex` is **−$870.1M** and **every strike from 274 to 296 carries negative net_gex** (285: −$205.2M, 290: −$196.4M). Dealers are short gamma in the exact band spot occupies, so a break through 290 makes hedging flow *sell into* the decline.

> **A second, independent GEX defect was isolated today.** `uw historical gex-time-series` computes its `regime` label as **`sign(spot − zero_gamma_level)`**, not from the gamma sign — and the ZGL itself runs 36–71% below spot on **16 of 30 rows** sampled across SPY/QQQ/IWM. Consequence: the label disagreed with its own `total_gex` sign on **27 of 30 rows**, printing `POSITIVE` on a −$1.284B book. `regime_flip_dates` is unusable for the same reason (its own `zgl_delta` values include single-day moves of +410, +499, +548). **Only the `total_gex` sign was trusted anywhere in this report.**

### DTE mix and VRP

`dte-volume-share` (MARKET-level only): 0DTE 25.2% · weeklies 31.4% · monthlies 30.7% · LEAPs 3.7% → `regime_hint: BALANCED`. Monthlies+LEAPs at 34.4% means institutional positioning is present but **not dominant** — swing and rotation calls got no automatic benefit of the doubt today.

**VRP: POSITIVE / premium-selling — the tool's label is inverted.** `uw historical vrp` reports `PREMIUM_BUYING` (−2.79 SPY / −2.73 QQQ), but `iv30d` is a decimal (0.1172) while `realised_vol` sits on another scale (2.9041) — and SPY's realised (2.9041) is near-identical to QQQ's (2.9078) although QQQ's RV structurally runs 1.3–1.5× SPY's. `earnings-scout` independently confirmed the same ~2.9 constant on ASO, ORCL and TCOM, proving the field is not a per-symbol realized vol. Like-for-like:

| symbol | IV30 | RV20 | true VRP |
|---|---|---|---|
| SPY | 11.72% | 7.2% | **+4.5pp** |
| QQQ | 17.29% | 12.6% | **+4.7pp** |
| ASO | 55.2% | 36.5% | **+18.7pp** |
| ORCL | 66.6% | 44.9% | **+21.7pp** |
| TCOM | 35.6% | 23.5% | **+12.1pp** |

### Macro backdrop

Yield curve **normal** (10y2y +0.43) · core CPI **2.79%** YoY but core PCE **3.34%** against a **3.63%** funds rate · unemployment 4.1% with payrolls already **−23k MoM** · 10Y **4.79% and RISING** (+0.09/30d) · broad USD **weakening** (−2.04/30d) · SOFR 3.65%. A stagflation-lean setup: the Fed cannot cut easily into sticky core inflation, and the bond market is pricing that even as the labour market softens.

**Forward event risk (T+N in trading days, Labor Day 09-07 excluded):**

| event | date | T+N | impact |
|---|---|---|---|
| **Nonfarm payrolls (Aug), 08:30 ET** | **2026-09-04** | **T+1** | **HIGH** |
| ASO earnings (premarket) | 2026-09-09 | T+3 | medium |
| PPI *(date unconfirmed by search)* | ~2026-09-10 | T+4 | medium |
| **CPI (Aug), 08:30 ET** | **2026-09-11** | **T+5** | **HIGH** |
| **FOMC + SEP dot plot** | **2026-09-15/16** | T+7/T+8 | **HIGH** |
| Monthly OPEX | 2026-09-18 | T+10 | medium |

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** Prose-only, **0 rubric points**, no backtested predictive claim. Scope is SPY and QQQ only.

**SPY — long-gamma, knife-edge, tight pin.** Spot 772.88 sits just *under* ZGL 774.24 (0.18% away, comfortably inside the ~5% trust band, so `zgl_reliable: true`). `total_gex` flipped from strongly negative (09-01 −$1.60B, 09-02 −$233.7M) to **+$1.070B** today — a one-session-old, unconfirmed flip. The call wall at **773 is essentially co-located with spot**, signalling an unusually tight pin, with 760 the next magnet ~13 points below. *Structure bias:* long-gamma with walls tight → iron fly / short straddle centred 773, **if the open confirms the prior**.

**QQQ — long-gamma but asymmetric.** ZGL 276.37 is 61% below spot, a deep-OTM extrapolation artifact (QQQ's ZGL has been unusable on ~8 of the last 10 sessions) — **disregarded**; the read rests on the `total_gex` sign (+$359.8M) and wall geometry. The call wall at 720 is only **0.36% above spot** while the put wall at 700 sits 2.4% below: dealers resist upside almost immediately, downside has a wide low-friction runway. *Structure bias:* condor skewed with the short call near 720 and a wider put wing toward 700 — **not** a symmetric fly.

**Mandatory caveats.** (1) **EOD is a prior, not a target** — fresh 0DTE OI floods in during the first 30–60 minutes and re-computes both ZGL and walls. (2) **ZGL reliability** — SPY's is trustworthy, QQQ's is not; QQQ's regime rests on sign plus geometry, which is inherently less precise. (3) **Gap risk is acute.** NFP prints 08:30 ET before the open. SPY's call wall is 0.1–0.3 pts from spot, so even a 0.3–0.5% gap vaults through it; the map holds to roughly ±1% and is **void beyond ~2%**. QQQ's 720 wall is trivially gapped through on any upside surprise. Both regimes are one day old inside a whipsawing series, so an NFP gap is more likely to trigger a fresh flip than a range extension. (4) **Tooling limit** — `gex --dte-max 1` errors, so this is the standing 0–45 DTE proxy book, not the isolated D+1 expiry. (5) **ETF book**, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup (the validated stack)

The GEX walls above are a **map, not a pin** — wall-as-magnet backtested NO_GO, as did every directional 0DTE signal. What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, not a guaranteed edge.

| | SPY | QQQ |
|---|---|---|
| `sell_premium` / verdict | true / `GO_PREMIUM_SELL_INTRADAY` | true / `GO_PREMIUM_SELL_INTRADAY` |
| `vol_state` / VIX | **LOW** / 14.32 | **LOW** / 14.32 |
| implied move / expected range | 0.74% / 0.77% | 1.02% / 1.36% |
| `size_scalar` | 0.5 | 0.5 |
| structure | iron fly / short straddle @ 772.82, wings ±0.77% | iron fly / short straddle @ 717.41, wings ±1.36% |
| gross mean PnL | 0.256% | 0.398% |
| **net mean PnL** (after 0.10% cost) | **0.156%** | **0.298%** |
| worst day | −0.892% | −1.068% |
| **LOW-tercile mean (the live state)** | 0.224% gross → **~+0.124% net** | 0.347% gross → **~+0.247% net** |

**Read the basis honestly:** `mean_pnl_open_pct` is **percent-of-underlying-spot-notional, gross** — not premium-collected, not margin-relative. Net of cost the edge at the current LOW vol tercile is roughly **+0.12% (SPY) / +0.25% (QQQ)** of notional — real but thin, and LOW is the weakest of the three terciles.

**Two caveats that dominate the numbers.** The short-vol **left tail is UNSAMPLED** (no vol shock in the 60-day window), so the 88.3% gross win-rate overstates a negatively-skewed seller's edge. And **NFP prints 08:30 ET tomorrow, before the open** — the `entry_rule`'s "enter once the overnight gap resolves" is doing all the work on a jobs-report morning, because the gap *is* the risk. **SPY ≈ SPX** (validated identical); **QQQ is the weaker proxy** (Nasdaq index book unavailable) and its overnight PnL is outright negative (−0.039%), reinforcing the never-carry-overnight rule.

*Promotion bar:* this lane stays advisory / 0 points **permanently** until both a vol-shock day enters the sample and net expectancy clears a tail-aware bar. Win-rate is explicitly not the promotion metric.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

**The scored +1 DEX-flip line is 0 for every name today.** `scripts/dex_flip.py` was run over the full 14-session window (08-17 → 09-03) on 17 names: **0 of 17 qualify.** Closest miss was QQQ — a prior run of only 2 sessions where the rule requires ≥3, and its window already carries `whipsaw_warning: true` with 4 sign changes.

**No vanna-squeeze flag may fire either — and this corrected the orchestrator's own Step 0 context.** I had written that the falling-VIX leg was satisfied; `dealer-positioning-strategist` falsified it with the dated series: `08-27 14.51 → 08-28 14.43 → 08-31 14.92 → 09-01 16.34 → 09-02 15.20 → 09-03 14.32`. VIX **spiked** on 09-01 and has fallen only **2** consecutive sessions; the mechanized rule needs ≥3.

| index | DEX | 5d trajectory | flip? | vanna book | swing bias |
|---|---|---|---|---|---|
| SPY | +39.56B | whipsaw 24.4→13.5→**−15.4**→8.7→39.6 | no (6 sign changes, **whipsaw**) | call-heavy | **NEUTRAL** |
| QQQ | +17.81B | flat/whipsaw | no (prior run 2, needs 3; **whipsaw**) | call-heavy | **NEUTRAL** |
| IWM | −5.75B | improving −6.8→−9.0→−16.8→−8.6→−5.7 | no (3 changes) | **put-heavy (+82,462)** | **LONG-lean, unconfirmed** |

**IWM and SMH both carry a genuine vanna-pressure setup one session short of its gate** — put-heavy DEX agreeing with a put-heavy vanna book, needing one more down-VIX session. Worth a watch note next session; note it points **against** the IWM short in §3.

Strongest non-scored directional builds (persistent, non-flipping): **NVDA** (8.2→24.4B, `sign_changes=0`, front-end IV 1.073 panic-adjacent), **SNOW** (6× jump today, front-end IV **1.113** — highest panic reading in the set), **HOOD** (strongest acceleration, but same-day as a +16.6% spot move, so causality is unclear), **DELL**, **META**. Useful context; explicitly **not rubric-qualifying**. **AMD excluded** for internal disagreement (DEX call-heavy vs vanna put-heavy); **TSLA excluded** for pure whipsaw (**10 sign changes in 14 sessions**, the worst in the set).

---

## 2b. Sector Rotation

**Rotation regime call: `no_change`.** No sector clears both the netted-direction gate and a multi-day durability check on *both* an in- and an out-leg, so no canonical two-sided pattern can be called.

**Direction reads off the netted source only** (`market-regime.sector_rotation`; a top-3/bottom-3 truncation, so absent sectors have no netted read):

| sector | netted | gross | agreement | verdict |
|---|---|---|---|---|
| **Technology** | **+$246.8M IN** | +$2.27B | **AGREE** | tradeable — but see bifurcation |
| **Financial Services** | **+$65.2M IN** | +$531.5M | **AGREE** | **downgraded to watch_only** — XLF −$0.82M MIXED and KRE −$5.15M BEARISH over 5d; neither ETF confirms |
| Consumer Cyclical | +$101.1M IN | −$210.7M OUT | DISAGREE | watch_only |
| Basic Materials | −$12.6M OUT | +$449.2M IN | DISAGREE | watch_only |
| Healthcare | −$9.8M OUT | +$96.5M IN | DISAGREE | watch_only |
| Utilities | −$3.9M OUT | +$16.2M IN | DISAGREE | watch_only |

> ⚠️ **`sector-flow-persistence` fired INFLOW at persistence 1.0 on 7 of 11 sectors today** — the known zero-discrimination defect. Treated as **non-informative** this session. The only discriminating persistence readings are Industrials and Utilities at 0.6 ROTATING; XLI is the 5-day laggard (−4.19%), which runs *with* the IWM short.

**The headline finding is a bifurcated Technology tape.** XLK confirms the netted inflow (+$7.63M/5d BULLISH), but **SMH is −$71.98M BEARISH** with over **$140M of Sept-18 downside puts** (630P/650P/650P/665P/675P, all ask/mid-side) and IGV is −$8.67M BEARISH. Mega-cap and software are being accumulated while the **semis basket is actively put-hedged**. This is why AVGO and SMH take no adverse-sector deduction in §6 despite Technology being netted-IN: the truncated GICS line is the wrong sector for those names.

**Energy — investigated explicitly, no call.** XLE is the 5-day price leader (+4.28%) yet absent from the truncated netted table, and the ETF tape does *not* rescue it: XLE −$0.80M MIXED, XOP −$2.85M BEARISH. Price strength without options-flow accumulation. Watch-only.

**ETF flow tape (advisory, 0 rubric points)** — top 3 each side:

| ETF | net premium (5d) | persistence | GICS agreement | note |
|---|---|---|---|---|
| XLK | **+$7.63M** | BULLISH | agree (Tech) | ask-side aggressive, 2 large prints above ask |
| XLV | +$1.21M | BULLISH | disagree (Healthcare netted-out) | ambiguous DP, thin far-dated options |
| XLC | +$0.36M | BULLISH | n/a (absent from netted table) | thin, near-mid, no sweeps |
| GDX | −$9.96M | MIXED | agree-direction, gross disagrees | **contradicts itself** — call-heavy sweep buying |
| IGV | −$8.67M | BEARISH | **disagree (Tech netted-IN)** | sell-leaning DP |
| **SMH** | **−$71.98M** | **BEARISH** | **disagree (Tech netted-IN)** | **decisive: >$140M Sept-18 downside puts** |

Independent non-flow corroboration (advisory): **6 of the 11 `fz` new-high breakouts are financials** (PFG, UNM, MUFG, DB, GNW, SLDE) — supporting the netted Financial Services inflow even as the ETF options tape declined to confirm it.

---

## 3. Swing Setups (1–6 weeks)

**Nothing is sized.** Full theses, structures and invalidations are carried below because routing is **not suppression** — every row is scored, gate-verdicted and serialized so the counterfactual keeps resolving.

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| GLD | 3 | Bear vertical into NFP on −$522.3M/30d bearish accretion | 09-04 long 395P / short 392P | loses the 410.18/410.50 second-tier DP shelf | **watch_only** |
| IWM | 3 | 3-expiry bear put ladder, only genuine multi-day build | 09-11 275P/285P · 09-18 282P/284P · 10-16 279P/281P/288P | reclaims 288 into 09-11; or a 3rd down-VIX session | **watch_only** |
| MSFT | 3 | Sole surviving accumulation candidate; $236.5M clean block | delta-long starter | loses the **$514.15** second-tier DP shelf | **skip** |
| MSTR | 3 | Bullish call diagonal, Tech leader | short 09-04 136C / long 09-11 145C | BTC loses $80K | **skip** |
| AVGO | 2 | Post-earnings drift short | ask-side put buying (not entered) | reclaims 367–370 | **watch_only** |
| SMH | −1 | #1 bearish name on the tape, scores negative | >$140M Sept-18 puts (not entered) | Sept-18 put book closed/rolled | **watch_only** |
| HOOD | 1 | Sector-leader tag only | — | 30d cum-flow flips | **skip** |
| NVDA | 1 | Sector-leader tag only | — | 30d cum-flow flips | **skip** |

### 3a. Long swings

**MSFT — raw 3, `skip`.** The only name in the book whose institutional-tier evidence survives stripping **both** of today's dark-pool contamination windows: two prints at 16:11:30Z totalling **$236.5M** (345,000 + 115,000 sh @ $514.1457) at `trade_vs_mid` **+1.036** — above the ask — corroborated across two independent tools. Every other bullish-leaderboard name failed that test (TSLA mega buy_ratio 0.293, NVDA 0.129, PEP 0.103, MCD 0.000). Fundamentals are excellent (rev +17.79% YoY, EPS +31.56%, 4-of-4 beat streak) with no earnings until 11-04. **C34 invalidation anchors to the $514.15 second-tier shelf**, not the $510.12 top bucket (the closing cross).

⚠️ **Distribution caution.** A live C28 `distribution_flag`: institutional call closing across three strikes and tenors ($500C/15d OI −890 ≈$817K; $530C/43d −294; $550C/78d −254). Advisory, 0 points, no sizing impact — but it sits on the same name as the buy block. **Its bull could only reach 0.35 residual confidence** and conceded it cannot reconcile insiders being net sellers in **12 of the last 20 months** (MSPR −83.89) with an accumulation thesis. The bear then found the decisive fact the bull omitted: **the same dark-pool pull contains a $94.4M SELL at 12:50:49Z at `trade_vs_mid` −4.135 — −0.825% below mid, roughly 4× more aggressive in relative terms than the buy block's +0.202% above mid.** Add a flow base implying **−$739.8M over the 60 days preceding the window**, and the accumulation reading does not hold.

**MSTR — raw 3, `skip`.** Bullish call diagonal (short 09-04 136C / long 09-11 145C) in the one sector where netted and gross agree, on a +14.1% session. **The quant flagged the front-leg parity as potentially fatal; the bull resolved it** by matching each execution to the underlying at its own timestamp — every sampled print carries positive time value (+$1.22, +$0.52, +$0.46, and the 145C fully extrinsic at $5.07). The apparent sub-parity was a stale-mark artifact of MSTR running $123.19 → $144.82 intraday. **The +2 stands.** But the bear reframed what it proves: a one-day-old single ticket with capped upside whose front leg expires into NFP is a **vol harvest that happens to be call-shaped**, not directional conviction — dwarfed same-session by near-dated call OI closing (−13,113 vs +6,286 added further out; `balance_ratio` 0.479 = de-grossing) and by **deep-ITM 2027/2028 LEAP puts** (strikes 480–700 on a $144 stock, deltas −0.91 to −0.97) several times the diagonal's $22.65M. Cum-flow **+$232.0M/30d inverts to −$362.3M/90d and is worsening**. The Technology tag is a classification artifact — a BTC-treasury vehicle's +14.1% is BTC +5% levered ~2.8×, not an AI/cloud rotation.

**HOOD (raw 1) and NVDA (raw 1) — `skip`.** Both score on a single sector-leader tag. The gap between narrative prominence and score is the point: NVDA has the cleanest DEX build on the tape (`sign_changes=0`) and a 1.073 front-end IV reading, and **both earn zero by design** — a persistent one-sided *level* is explicitly not the mechanized flip trigger. Its institutional dark-pool read is not merely absent but **actively negative at a 0.129 mega-tier buy ratio**, and it took a $500.00M round-notional print inside the basket window. HOOD's flagship evidence — the strongest single-session DEX acceleration in the set — arrived the *same day* as a +16.6% spot move, so it is plausibly reactive hedging rather than a leading signal.

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only`.** Theses, structures and invalidations still run.

**IWM — raw 3, `watch_only`. The best-evidenced structure in the book.** A three-expiry bear put ladder with **`repeat_count=3` on the 282P** — the only genuine multi-day build today — whose strikes match the OI tape almost contract-for-contract (282P +30,587, 285P +24,364, 279P +17,253, 270P +17,061), with **no parity contamination** (the bull ran the test itself: all four driving strikes are genuinely OTM against a 295.17 spot) and a 30-day bearish flow that **deepens** to −$449.0M at 90 days rather than decaying. The bull's strongest objection — that a put-heavy IWM book is the *structural baseline*, with PCR > 1.3 on all ten of the last ten sessions — was answered by the bear with the **increment** the bull never checked: **282P open interest jumped 48,190 → 78,777 in one session (+63.5%) on ~14:1 ask-side dominance, and the 285P +59.4% on ~120:1.** Routine hedge churn does not print 120:1. The collar reframe fails on notional (the 300C leg is ~$198K against ~$4.25M in the 282P alone). Dealers are short gamma across 274–296. **Against it:** the vanna-squeeze setup is one down-VIX session from flipping the same book into a mechanical buy force, IWM led the tape today (+1.18%, beating SPY), and IV at a **3.87 rank** says the options market prices no distress.

**GLD — raw 3, `watch_only`, and it should not be read as the book's strongest call despite ranking first.** A one-day bear vertical (09-04 395P/392P) resting on −$522.3M/30d bearish accretion that is genuinely fresh — the 90-day figure is −$522.9M, so essentially all of it accrued inside 30 days — plus a 395P bought aggressively on the ask today (175,441 contracts) that is **fully extrinsic** (spot 411.26 vs strike 395), so unlike AVGO there is no parity contamination. The bear also established that today's classifiable **call** flow is net **sold** ($4.77M bid vs $3.28M ask), i.e. overwrite supply into the bounce. **But the anti-short case carried the higher residual (0.65 vs 0.45)** and the reasons are structural: the Step 6 deep-dive found **~268,600 contracts of upside call OI built at the 15-DTE 415/430/435 strikes** against only ~12,450 of put OI; GLD is **bouncing, not breaking** (396.75 on 09-01 → 402.78 → 410.22, +3.4% off the low); today's put/call ratio spiked **0.16 → 1.59 in a single session** while every other session in the window printed sub-1.0; **$627.68M of same-day ETF inflows** ran against it; and the NFP asymmetry points the wrong way — payrolls are already −23k, so a weak print is dovish, real yields fall, and gold rises. **GLD was scored LONG at raw −2 / skip yesterday and SHORT at raw 3 today — a full sign flip in one session, on a session GLD rallied +1.85%.**

**AVGO — raw 2, `watch_only`.** Fundamentals-gate returned **CONFIRM**: AVGO **reported earnings today** and fell 5.6% despite an 86% revenue surge, on ~18 consecutive months of negative insider sentiment (MSPR −94.62). But **the flow confirmation largely dissolves under a parity screen.** Testing `time_value = premium − intrinsic`: the single-leg scan's Tier-1 `OPENING_PUT_PRIME` (445P, dte 1) is itself **sub-parity at −$0.15** with an implied vol of 265% on a deep-ITM contract, and the Sept-18 complex (P490 $50.26M, P500 $7.50M, P480 $5.79M — all `no_side`, 2–3 prints each) carries time value between −$0.69 and −$0.01. **Genuine contamination: $63.55M of $276.58M = 23.0%.** So sweep-tracker's "triple confluence" is closer to **one contaminated source counted three times** than three independent confirmations. Neither researcher could establish *why* the stock fell on a large beat, and both said so.

> **A correction to this desk's own work.** My first pass reported 28.2% contamination. The bear-researcher identified a **look-ahead artifact**: `uw options-flow sweeps` returns a **day-blended `avg_price`**, and the C350 rows aggregate **3,607** and **3,497** executions while AVGO ranged **343.21–357.225** intraday — so comparing a blended average to the *closing* intrinsic manufactures false sub-parity for any strike the stock crossed during the day. Verified and accepted; the C350 finding is withdrawn and the figure corrected to **23.0%**. The Tier-1 445P finding stands (single print, own execution-time `signal_price` 356.45). **Method rule going forward: check `trade_count` before trusting any parity verdict.**

**SMH — raw −1, `watch_only`.** The **#1 bearish name on the entire tape** — −$76.3M on `screener_bearish`, −$71.98M of 5-day ETF options flow, over $140M of Sept-18 downside puts on the ask — **scores minus one**. Two rubric artifacts produce that, neither of them evidence: every one of SMH's bearish signals is sweep/urgency-tape evidence, which earns **0 points** since the 2026-05-23 deprecation; and its own mildly bullish trailing cum-flow (+$24.5M) converts into an **active −1 deduction** on a figure that is **0.41% of its own $5.92B 30-day gross**. Note also that `dealer-positioning` contradicts the short outright, reading SMH LONG-lean.

### Sweep tape (informational — 0 rubric points)

Persistence-ranked (≥3-of-5 sessions, C12-passing, directionally consistent): **AVGO** bearish 5/5 ($999.3M/5d) · **MSFT** bullish 4/5 ($818.6M) · **AMD** bearish 4/5 ($486.8M) · **DELL** bearish 3/5 ($1.10B) · **MSTR** bearish 3/5 ($626.7M) · **GLD** bearish 3/5 ($382.8M, today's 395P ask/bid ratio **231×**).

**QQQ, TSLA and IWM sweep-persistence directions are hedge-flow artifacts, not signals** — all three fail the cum-flow alignment screen (QQQ sweeps bearish 5/5 against net-bullish 30d flow; TSLA and IWM the mirror). The QQQ print behind it was a **2027-06-17 740P**, a LEAP-dated hedge, not a momentum trade.

---

## 4. LEAP Builds (6–24 months)

**Empty. No candidates.** `uw oi biggest-increases --min-dte 180` returned only 20 rows, 8 inside the C12 floor, and **every one failed the required cum-flow accretion gate**:

| ticker | fresh DTE>180 build | 30d net | 90d net | disqualification |
|---|---|---|---|---|
| **NVDA** | 270319C00320 (197d), OI **+14,329**, ask:bid **39.8:1** | +$236.6M | +$70.1M | **decay** — collapses as the window widens; 90d net is 0.07% of gross |
| **TTD** | 280121C00020 (505d), ask 5,550 vs bid 70 | −$82.1M | −$98.8M | **wrong sign, both windows** — a fresh call build inside a bearish book |
| **TLT** | 280121C00100/C00090 (505d), OI +21,716/+14,613 | −$5.3M | −$138.9M | **decay and wrong-direction widening**; macro also argues against a Fed-cuts-duration-rallies thesis |
| **XLF** | 270319C00059 (197d), OI +12,781 | −$15.4M | −$0.9M | **bid-dominant** (73 ask vs 192 bid) = call writing, not a long build |
| **MSTR** | *(context)* balance_ratio 0.479 | +$232.0M | **−$362.3M** | **outright sign reversal, growing** — the cleanest falsifier on the tape |

No candidate reached the dark-pool, institutional-accumulation or conviction-matrix gates — correctly, since there is no point padding a thesis already rejected on a required gate. `dte-volume-share` puts LEAPs at just **3.7%** of market volume: a thin tape where "fresh conviction" mostly is not there. **The +1 conviction-matrix rubric line is therefore unavailable to every name in this report**, since it is conditional on `dominant_signal_class == leap_directional`.

---

## 5. Volatility Surface

**Substrate hygiene was mandatory and load-bearing.** Across 13 names, `scripts/term_structure_hygiene.py` flipped the kink-aware shape on **9 of 13 (69%)** and the monotonic base shape on 4 of 13 — raw labels were unusable, as expected. `front-end-iv-ratio --near-dte 7` fired non-FLAT on **9 of 13 (69%)**, a high population rate, so individual readings are directional colour rather than a clean binary. **`iv-percentile-zscore` returned `dates_used: 101` on 13 of 13 names — 0% cleared the 120-day floor, so every IV-percentile figure in this report is PROVISIONAL.**

**Macro kink anchor, computed first:** SPY kink at **dte 8** (prominence 22.9%) and QQQ at **dte 8** (5.3%) — both **2026-09-11 = CPI day**. Any single-name kink at dte≈8 is presumptively shared CPI beta and was discounted; this hit **AMD, SMH, ORCL and AVGO**. A second cluster at dte 15 (2026-09-18 monthly OPEX) hit XPEV and NKE.

**ASO — SELL VOL (`watch_only`).** The cleanest name-specific surface read of the session: monotonic BACKWARDATION with **`kink_dte` null**, so no collision with the CPI hump; front-end ratio **1.486 at dte-8, and VALID** because that expiry falls after the 09-09 print (the documented snap trap was checked and cleared); IV at its **92nd percentile**; own-name VRP **+18.7pp**. **Corrected implied move ≈9.1%** re-derived from the dte-8 tenor against a raw dte-1 figure of 2.25% — a **4.0× understatement avoided**. Fragilities: 5 of 11 tenors dropped for the sub-15-contract floor, and the back-month TAIL_HEDGING 1.23 read rests on 16 contracts while the adjacent dte-43 tenor reads NORMAL 1.053.

**Cross-agent disagreement, left unresolved rather than smoothed over — TCOM.** `vol-surface-scout` ranked it the session's **best `vol_long`**: IV30 at its **13.86th percentile** while term structure still shows genuine backwardation (1.29 front ratio, so the market prices *some* event premium) into a hard dated catalyst 12 days out, implied move ~9.6%. `earnings-scout` returned **SKIP**: earnings land on 09-15 *during* FOMC, and the only post-event tenor (09-18) simultaneously prices earnings, the FOMC/SEP dot plot **and** monthly OPEX — so the event premium is **not isolable**, closer to "unmeasurable" than to edge. Both percentile reads are provisional. **TCOM failed the two-agent confluence gate on exactly this disagreement and is not in the book.** It is the one name worth re-checking after tomorrow's print.

**ORCL — SKIP.** A genuine kink (dte 8, prominence 9.7%, all 19 tenors clearing the contract floor) with earnings 09-10, but two independent disqualifiers: back-month skew is **flat across every tenor tested** (0.969 / 0.981 / 0.984 / 0.976 / 1.006 on well-populated tenors — the tail is not priced alongside the front), and the front ratio of 1.436 trips the >1.10 extreme-panic rule. Its kink also collides exactly with the SPY/QQQ CPI dte.

**AVGO — SELL VOL (`watch_only`).** BACKWARDATION driven by a dte-1 IV of 70.77% decaying to high-30s, implied move ≈3.7%. The event has now resolved (iv30d crushed **0.4902 → 0.3599**), and the dte-1 spike is substantially NFP-shaped macro beta rather than name-specific skew.

**Buckets 2 and 3 are empty.** No BACKWARDATION calendar could be certified as "front-ratio falling" from a single EOD snapshot (LULU carried the richest ratio at 1.506 but direction is unconfirmed, so it stays out per the don't-fade-a-rising-ratio rule). All 20 `iv-outliers` rows were sub-C12 microcaps except one SPY row in the expired 0DTE bucket, which hygiene requires dropping.

> **Why the vol lane is so heavily constrained.** `vol_short` is adversely selected: **−25.1pp against unselected same-date peers on n=111** (paired McNemar p<0.0001), negative in **4 of 4** regime buckets, while `vol_long` runs **+9.5pp** and is 5-for-5 on every sized row in the corpus. The diagnosed mechanism is a **sign error, not a dead lane** — the scouts identify vol-*expansion* candidates correctly and that identification has been used to *sell* into the expansion. Hence: every net-short-vega expression routes to `watch_only`; `vol_long` is explicitly unconstrained. **These figures price SELECTION, not P&L** — vol rows resolve on an RV-direction proxy.

---

## 6. Risk & Correlation

**Macro headline:** stagflation-lean — core PCE 3.34% against a 3.63% funds rate, payrolls already −23k, 10Y 4.79% and rising, USD weakening. **The forward calendar is the dominant risk in this book: NFP at T+1 tomorrow, CPI at T+5, FOMC+SEP at T+7/T+8.**

**Breadth (advisory, 0 points):** 340 advancers / 161 decliners, **67.59% green**, avg +0.70%. `divergence_flag` is **false** on its own terms — the index is green *and* participation is broad. The material divergence is the **cross-lineage** one: price breadth 67.59% green against uw options-flow breadth of only **35.9% bullish**.

### ⚠️ The correlation tool failed verification and was not used for sizing

`uw risk portfolio-correlation` returned **0.971–0.996 on every pair**, including **GLD/NVDA 0.988** and **GLD/ASO 0.987**. Gold correlating 0.99 with a semis name is not plausible, and the figures are not reproducible as return *or* level correlation at any window (40/30/20/10 bars). Taken at face value it classes **all 36 pairs as clusters** — the same zero-discrimination signature as `oi-trend` BUILDING firing 14-of-14. The gate was instead computed from **reproducible 40-day log-return correlations** off `uw historical trend` closes:

| pair | tool | true return corr | true level corr |
|---|---|---|---|
| GLD/IWM | 0.996 | **0.423** | 0.563 |
| GLD/NVDA | 0.988 | **0.393** | 0.643 |
| IWM/ASO | 0.991 | **0.235** | 0.083 |
| AVGO/SMH | 0.995 | **0.726** | 0.495 |
| NVDA/SMH | 0.994 | **0.743** | 0.491 |

**Clusters that genuinely fire (≥0.70):** `semis_complex` **AVGO/SMH 0.726** (both short the same basket = one position; AVGO kept on raw 2, **SMH takes −1**) and **NVDA/SMH 0.743**. **Soft watch (0.60–0.70, no penalty):** IWM/SMH 0.667 · MSTR/HOOD 0.648 · GLD/MSTR 0.628.

SPY return-correlation: IWM 0.819 · SMH 0.705 · NVDA 0.603 · AVGO 0.558 · MSFT 0.550 · HOOD 0.526 · MSTR 0.424 · **GLD 0.325** · **ASO 0.203**. GLD and ASO are the genuine diversifiers; MSFT is third.

> **A gate-design flaw worth registering: the cluster gate is direction-blind.** It fired on NVDA/SMH at 0.743 and charged SMH −1 — but **NVDA is long and SMH is short**. A correlated *opposite-direction* pair is an **offset, not a concentration**. Applied per the letter because it is non-binding today, and flagged rather than overridden.

### Fundamentals verdicts (top 5)

| ticker | verdict | reason | tier |
|---|---|---|---|
| GLD | **NA** | ETF — no issuer fundamentals | 0 |
| IWM | **NA** | ETF — no issuer fundamentals | 0 |
| **MSFT** | **CAUTION** | `insider_selling_cluster` — MSPR **−83.89** (3mo), 12 of 20 months net-negative | **−1** |
| **MSTR** | **CAUTION** | `insider_selling_cluster` — MSPR −28.22; BTC-collateralized convertible leverage **not captured** by a reported D/E of 0.16 | **−1** |
| **AVGO** | **CONFIRM** | earnings resolved today, −5.6% on an 86% revenue beat; MSPR −94.62 over ~18 months | 0 |

**No VETOs this cycle.** The gate also delivered the session's single most consequential fact: **AVGO had already reported**, converting what vol-surface-scout treated as unresolved forward event risk into resolved, corroborating post-print drift.

### Panic gate — my Step 0 briefing was wrong and risk-monitor caught it

I told risk-monitor the panic gate would no-op on the board, quoting AVGO at 1.045 and omitting ASO entirely. Re-reading independently, **two names exceed 1.10: ASO at 1.486 (the highest on the board) and AVGO at 1.161.** Both fire.

> **New substrate defect: the `--near-dte 7` snap is NON-DETERMINISTIC.** Four identical consecutive invocations, same session: `AVGO → dte8/1.161/BACKWARDATION, dte6/1.045/FLAT, dte8/1.161, dte6/1.045`. The snap resolves to the dte-6 *or* dte-8 neighbour at random, which on AVGO **straddles the 1.10 panic threshold** and on NVDA flips the regime label (1.073 BACKWARDATION vs 0.843 CONTANGO). ASO and MSTR were stable 4-of-4, so stability is per-name. The conservative (higher) reading was taken throughout, since every gate it feeds is downgrade-only. This is a **third distinct defect** on this one tool.

### Adverse-flow exits and hedge

Carried group `conviction_2026-09-02` = IWM, NBIS. **No exit candidates.** IWM's alerts (`LOW_IV_RANK` 3.9, `LARGE_DARK_POOL` $18.46M, `OI_SHIFT` +297,756) **confirm** rather than contradict — the OI shift *is* the 282P/285P/279P build the ladder is made of. NBIS shows soft decay (volume_ratio 0.57, thesis not contradicted) but did not re-qualify and is not carried forward. Fundamentals-drift tripwire: one cosmetic IWM dividend-yield denominator change from its own +1.18% move; nothing adverse.

**Hedge sleeve: NOT WARRANTED.** Every row lands at `watch_only` or `skip`, so net delta is zero — buying protection against an empty book is a pure premium expense, and an expensive one in a positive-VRP tape. Even the paper book has no skew to hedge (4 directional shorts vs 4 longs plus 1 short-vol = 0.50 short skew, below the 0.6 proposal threshold). The correct hedge for an empty book against an unhedged Tier-1 print is the empty book itself.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**This section is empty. No name reached MEDIUM (7), let alone HIGH (9).** The top of the book is four names tied at raw_score 3 (LOW).

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: not computable this session. There are no HIGH/MEDIUM rows to report per-tier expectancy or payoff ratio for, and the rolling `conviction_<date>` closed-call set has produced no sized daily position since 2026-07-07. Display-only context in any case — the live sizer remains the win-rate ladder.

**Because §7 is empty, the full audit trail for all nine scored calls is carried in §3, §5 and the `decision.json` sidecar**, which holds `score_components[]` with a named source agent and a single canonical tool per component, the 9-key `gate_verdicts`, `debate_residuals`, `market_excess` and the instrumentation trio for every row.

### Gates: what actually fired

Only **two** score-level guards bound today, both on the `bearish_flow` pair (AVGO, SMH): **C2 market-excess −0.0811** (the class has historically *underperformed simply shorting SPY* over the same 148 windows) and **C4 opening-gate fail-closed**. The load-bearing-tool gate, the N-cap, the 0.80 ceiling, the anti-predictive [0.55, 0.65) band and the vol-lane class ceilings **never bound — no quote got high enough to test them**. The out-of-regime guard is recorded on all nine rows and is non-binding because nothing reached half.

**Win-rate substrate:** seven of nine rows are `NA(substrate)`, not measured-and-passed. `dark_pool_accumulation` returned **0 rows market-wide** (known defect), and `multileg_directional` / `sector_rotation` / `earnings_vol` are **not among the five backtest-supported classes**. Only `bearish_flow` produced a number, under the P0.3 clean-query protocol: headline **56.7%** (never quoted) versus a clean **0.5203 on n=148** after dropping 13 clamped rows — **a 4.7pp recency artifact**, the quarantine earning its keep. The tool's own `truncated_signals` field reported 14 against the authoritative filter's 13; the two disagree.

### Conviction rubric (frozen, version `2026-06-12`) — embedded verbatim for audit

```
Daily conviction score = Σ:
  +1  MECHANIZED DEX flip or vanna-squeeze in trade direction (verified SIGN CHANGE, not a level;
      computed by scripts/dex_flip.py, never by hand)
  +3  3+ aligned accumulation signals (DP + OI + smart-positioning + block-stratified institutional tier)
      — C11 CONJUNCTION: full +3 only when cum_flow_30d sign-aligned AND |cum_flow_30d| ≥ $50M; else halved to +1
  +1  multi-day OI build (oi-trend BUILDING, --days ≥ 5)
  +1  conviction-matrix DIRECTIONAL_LONG conf>70 — CONDITIONAL: only when dominant_signal_class == leap_directional
  +1  cumulative-premium-flow net directional accretion 30d — INTENT-SCREENED (0 if a C28 distribution_flag
      is present, or on deep-ITM sub-parity dividend-capture prints)
  +1  sector-rotation single-name leader — CONDITIONAL, ALL THREE: (a) sector persistence ≥ 0.6 AND
      (b) cum_flow_30d direction aligned AND (c) |cum_flow_30d| ≥ $50M. Default 0.
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (play type anchored to term structure)
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist top-5 (OPEX week only)
  -2  contrarian-scanner overcrowded long with RISING pc-ratio-zscore (VRP positive)
      — an INFORMED-FLOW CONTINUATION penalty, not "fade the crowd"
  -3  flow_conflict — cum_flow_30d clearly opposite dominant_signal_class
  -1  flow_conflict_lite — 30d cum-flow read is MIXED
      (-3 and -1 are MUTUALLY EXCLUSIVE — apply ONE, never both)
  # sweep-persistence earns 0 points (removed 2026-05-23 P0.3)
  # signal-confluence earns 0 points and gates nothing (removed 2026-06-12 P0.2)
  # gamma-flip-tracker / §2 GEX earns 0 points by design
  # regime and correlation deductions are TIER GATES applied by risk-monitor in 2d — NOT score_components

Tiers: ≥9 HIGH (full) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 drop
```

### Deep-dive hand-off

**Skipped — correctly.** Step 8.5 applies to the top 2 **HIGH-tier** names post-gate. There are none. No `/stock-deep-dive` is recommended today.

---

## 8. Watch-only — single signal, no confluence

Failed the two-agent confluence gate. Listed for journaling, **not for entry**.

- **QQQ** — the highest-quality *structure* found today and it cannot enter the rubric on one agent. `multileg-strategist` HIGH conviction: a long strangle built from two debit verticals (09-11 long 695P / short 680P + long 740C / short 750C), **repeat_count 2–3**, anchored exactly at the dte-8 CPI kink, long-vega and defined-risk both sides.
- **TCOM** — the genuine cross-agent disagreement (§5). Best `vol_long` per vol-surface-scout; SKIP per earnings-scout because the 09-18 tenor prices earnings + FOMC + OPEX simultaneously.
- **SNDK** — sector-rotation leader with the largest cum-flow of the group (+$779.2M/30d), but the only positive flag. Its contrarian read is BULLISH_EXTREME (z −2.267) and its Tier-1 1800P **expires 09-04 = NFP day**, so it plausibly prices a macro hedge rather than a name view.
- **SNOW** — dealer-positioning LONG (6× DEX jump, front-end IV **1.113**, the highest panic reading in the set) plus an fz new-high breakout (+16.55% on $7.78B), but sweep-tracker shows SNOW **bearish 2/5** — a live price-vs-flow tension.
- **DELL** — dealer-positioning LONG, but **sector-rotation explicitly disqualified it** (cum_flow_30d −$2.9M MIXED fails condition (b)) and sweeps read bearish 3/5.
- **META** — dealer-positioning LONG; everything else negative. Genuine non-contaminated DP prints are thin and roughly flat ($15.4M sell vs $14.2M buy), the contrarian z is 0.269 NORMAL (no crowd extreme to fade), and a Tier-1 opening 790P sits underneath a +$47.3M bullish headline.
- **MCD** — zero positive flags. Mega tier is **1 trade at buy_ratio 0.000 (a sell)**; block tier 0.144. Its pc-ratio z of **19.78** looks extreme but the 20-day std is 0.102, so a single large put block can manufacture it — **the z-score and the Tier-1 310P are very likely the same print counted twice**, not two confirmations. Reclassified as a genuine hedge bid, not a fade.
- **TSLA** — top of the bullish leaderboard at +$156.0M yet **mega-tier buy_ratio 0.293**; dealer-positioning excluded it for **10 sign changes in 14 sessions**.
- **PLTR** — a real $151.87M block at 19:55:26Z, but cum_flow **−$49.3M/30d** (wrong sign *and* under the floor) worsening to −$358.2M/90d. Note the DP price-level pattern **inverts** here: the *top* bucket ($182.97) is the genuine print and the *second* ($182.53) is the closing cross.
- **MU** — the best timestamp-clean DP evidence of anyone reviewed (~$163M buy-side, all above mid, none in contaminated windows) and the cleanest OI call-dominance (2.96:1), but institutional-accumulation reads NEUTRAL and cum_flow **−$388.6M/30d vs +$530.1M/90d — a sign flip**.
- **INTC** — mechanically clears 3 signals (genuine $84.6M buy, best OI ratio in the group at 5.83:1) but cum_flow −$203.7M/30d worsening to −$884.1M/90d, plus a live distribution_flag.
- **NKE** — multileg bearish risk reversal (09-18 long 40P / short 45C); **routing ambiguous** because the short 45C is uncapped and a synthetic short cannot be distinguished from a collar on stock.
- **AMD** — sweeps bearish 4/5, but dealer-positioning **disqualified it for internal disagreement** (DEX call-heavy vs vanna put-heavy, both near flat).
- **IBIT, LULU, KLAC** — single-agent or single-ticket only.

### Screened out — financing structures, not conviction

- **KWEB** — the day's highest-value disagreement. It sits on the **bullish** leaderboard at +$14.4M, and its only multileg structure is a **parity-priced put box**: the 09-18 36P at $10.30 against $10.45 intrinsic = **time value −$0.15, sub-parity**; the 33P at $7.535 vs $7.45 ≈ parity. **The +$14.4M is not bullish conviction — it is box noise.**
- **XPEV** — 09-18 17P/14P on an $11.13 stock, both deep ITM; a $2.957 debit on a $3-wide spread means **max profit ≈$0.043, 1.4% of width** — economically a conversion. Its −$21.1M bearish headline is very likely this structure.
- **SPX/SPXW** — the largest premium on the tape (+$1.099B) but a deep-ITM 7000C / 8000P book across 09-18/12-18/2030/2031 with sizes repeating in 4600/4000/2500/1000 blocks: a box-spread/financing overlay layered with 0DTE noise. Structure not cleanly inferable.

### Dropped — C12 liquidity floor (price ≥ $5 AND 20d $ADV ≥ $50M)

ACHC ($46.3M) · AI ($47.9M) · ASAN ($41.3M) · **CAR ($43.7M — despite +$41.9M of bullish net premium)** · CLDX ($31.6M) · GNW ($26.3M) · LXU ($7.8M) · PTON ($45.9M) · SLDE ($19.3M) · STOK ($27.5M) · **YELP ($26.2M — the top bearish-confluence name at score 5)**. PCG and EWZ were surfaced by multileg but are not on the C12-verified list and were dropped unverified.

---

## Appendix — substrate defects found this session

Five, three of them new. All are recorded to project memory; none were patched mid-run.

1. **`market-regime` zeroed-price defect (new, systemic).** SPY's close ingested as 0.00 → both SMAs dragged by `close/window`, `trend` inverted to DOWNTREND on a +1.05% up-day. Reproduced to the cent. Same failure hit `insights price-vs-flow` (13/13 symbols) and leaked into the `signal-backtest` substrate.
2. **`gex-time-series` ZGL corruption (new).** `regime` is computed as `sign(spot − ZGL)`, and the ZGL runs 36–71% below spot on **16 of 30 rows** — so the label disagreed with its own `total_gex` sign on **27 of 30 rows**. `regime_flip_dates` unusable.
3. **`front-end-iv-ratio --near-dte 7` non-determinism (new).** Identical consecutive calls alternate between the dte-6 and dte-8 tenor, straddling the 1.10 panic threshold on AVGO. Third distinct defect on this tool.
4. **`portfolio-correlation` not reproducible.** 0.971–0.996 on every pair; classes the whole board as one cluster.
5. **`vrp` units bug.** `realised_vol` returns the same ~2.9 constant across five symbols — not a per-symbol RV; inverts the classification.

Plus a **second dark-pool contamination window**, distinct from the known closing cross: a program/basket wave at **~21:06:55–21:08:00Z** hitting ~10 large caps with round notionals inside 90 seconds (NVDA $500.00M, GOOGL $499.9998M, SPY $499.9998M). Several headline mega-tier buy ratios (MSTR 0.879, DELL 0.896, INTC 0.931) collapse once it is stripped.

**Register items (flagged, not patched):** the frozen rubric cannot score a pure sweep-tape thesis (AVGO scores 2, SMH −1); the cum-flow deduction side still has no scale or freshness floor while the award side has two (SMH's −1 rests on 0.41% of gross); the cluster gate is direction-blind; and the debate gate's role polarity is unresolved for short calls — the two readings **invert** on IWM and AVGO. The recommended fix for the last is upstream: have researchers emit `pro_trade_residual` / `anti_trade_residual` rather than role-named scalars.
