# Daily Market Analysis — 2026-09-04

## Executive Summary
- **Regime + GEX state:** `TRANSITIONAL — Mixed signals, reduce position size, wait for clarity` (trend sub-field UPTREND). SPY 770.19 (−0.39%) above its 20d/50d SMA, but **equal-weight RSP −0.48%** and only **34.79% of S&P names green** (median name −0.56%). SPY's dealer book is **FULLY_NEGATIVE**: `total_gex` −$1.17B with **−$904.1M in the single 770 ATM strike**. ^VIX 14.53 (+1.47%). Sector lean is a **narrow semis/memory melt-up on a red tape** — SOXX +3.52%, SMH +2.61% against IGV (software) −2.23% (−4.50% 5d).
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** **SPY** short-gamma · ZGL null (unreliable) · call wall 780 / put wall 760 → hedging *amplifies* moves off 769.88 rather than pinning; avoid selling ATM premium. **QQQ** short-gamma by `total_gex` sign (−$237.3M) · ZGL 243.37 is a corrupt extrapolation · walls 718/720, a ~0.3% band → live flip zone, wait for the first 30–60 min. Advisory, see §2.
- **Top swing build:** **NONE.** No name clears MEDIUM. The board's top score is NVDA at raw 3 (LOW), and it floors at `skip` after the event-risk and debate gates. **Empty conviction book — the 43rd consecutive empty daily board** (last sized 2026-07-07; re-derived by globbing `analyses/daily/*/decision.json` only).
- **Top LEAP candidate:** **NONE.** Only IREN and VFC surfaced above 180 DTE market-wide; both disqualified (2/9 and 1/9 gates). LEAP share of DTE volume is 3.1%, the thinnest bucket on the board.
- **Biggest risk:** There is no book, so there is no correlation cluster to hedge. The live risk is **structural, not positional**: CPI at T+4 (2026-09-11) and FOMC+SEP at T+7 (2026-09-15/16) land against a short-gamma index book with three-quarters of its negative gamma in one ATM strike. Anything carried in from outside this book should be expressed as **long convexity**, not short premium.

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** TRANSITIONAL. SPY 770.19, above 20SMA (769.05) and 50SMA (756.86), +0.21% over 30d, −1.18% from the 90d high. Guidance: *"Half position sizes. Favor defined-risk strategies. Iron condors in range."* Flow-ticker breadth: 2,229 bullish vs 4,064 bearish of 6,293 (**35.4% bullish**).

**The tape framing matters more than the label today.** QQQ's green close (+0.18%) is *entirely* semis. Equal-weight SPY is red, 8 of 11 sectors are red, and software is being sold hard:

| Instrument | 1d | 5d | rv20 |
|---|---|---|---|
| SPY 770.19 | −0.39% | +0.11% | 7.9 |
| QQQ 718.96 | +0.18% | +0.35% | 12.5 |
| IWM 296.01 | +0.28% | +0.09% | 11.9 |
| **RSP (equal-wt) 219.00** | **−0.48%** | −0.77% | 8.6 |
| **SOXX 519.86** | **+3.52%** | +2.21% | 33.1 |
| **SMH 567.01** | **+2.61%** | +2.51% | 30.6 |
| **IGV (software) 104.57** | **−2.23%** | **−4.50%** | 39.1 |
| XLY / XLC / XLV | −1.33% / −1.19% / −1.04% | | |
| GLD 406.77 | −0.84% | −0.52% | 26.4 |

Top mover SNDK **+11.9%**; worst LULU **−17.38%**.

**Per-index gamma (current-state EOD book; §2 carries the forward read):**

| Index | Spot | Zero-gamma | `total_gex` | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 769.88 | `null` (unreliable) | **−$1,169,916,780** | FULLY_NEGATIVE | 780 (+$114.3M) | 760 (−$185.9M) |
| QQQ | 718.32 | 243.37 (**corrupt, >65% from spot**) | **−$237,297,106** | NEGATIVE by `total_gex` sign | 720 (+$86.6M) | 718 (−$242.1M) |
| IWM | — | — | negative on **23 of 30** sessions | persistently short-gamma | — | — |

**`uw options-flow dte-volume-share`:** 0DTE **48.9%**, weeklies 20.6%, monthlies 19.1%, LEAPs 3.1% → `regime_hint: RETAIL_DRIVEN`. Institutional positioning share is thin; every rotation and swing call is downgraded uniformly for this.

**`uw historical vrp`:** SPY IV30 0.1162 vs realised 0.1173 → **−0.0011, FAIR**. QQQ 0.1706 vs 0.1978 → **−0.0272, FAIR**. *"IV close to realised — no clear edge from VRP alone."* Neither a premium-selling nor a premium-buying environment. No VRP claim is made anywhere in this report at the index level.

**Macro backdrop** (`scripts/fred_macro.py`): yield curve **normal** (10y2y +0.41); core CPI 2.79% YoY; **core PCE 3.34%** — sticky and above target; unemployment 4.1%; payrolls +162k (Aug, released today); **10Y 4.77% and RISING** (+0.14 over 30d); USD **weakening** (−2.04 over 30d); fed funds 3.63%; SOFR 3.66%. Sticky core PCE against a rising long end into a FOMC with a fresh dot plot is the least forgiving backdrop for the duration-sensitive AI-infra complex that makes up the entire top-5.

**Forward event risk** (T+N in *trading* days from 2026-09-04; Labor Day Mon 2026-09-07 excluded):

| Event | Date | T+N | Impact |
|---|---|---|---|
| NFP (Aug) | 2026-09-04 | T+0 (released) | high — already in the tape |
| PPI (Aug) | 2026-09-10 | T+3 | medium |
| **CPI (Aug)** | **2026-09-11** | **T+4** | **high** |
| **FOMC + SEP** | **2026-09-15/16** | **T+6/T+7** | **high** |
| Monthly OPEX | 2026-09-18 | T+9 | medium |
| Core PCE (Aug) | ~2026-09-25 | ~T+14 | high |

Robust to the holiday assumption: if 09-07 were open, CPI is T+5 and FOMC T+8 — CPI stays inside the T+4/T+5 band either way.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book — open interest persists overnight — read forward as the *prior* for the next session's open (2026-09-08, Tuesday, after Labor Day). **Prose-only, 0 rubric points, no backtested predictive claim.** Predictive validation lives in `/weekly-analysis`'s rolling §2 backtest. Scope is SPY and QQQ only.

**SPY — short-gamma, and the concentration is the story.** Spot 769.88, `zero_gamma_level` **null** (`zgl_reliable: false`), `total_gex` **−$1,169,916,780**, call wall **780** (+1.31%), put wall **760** (−1.28%). The dominant feature is not the wall spread — it is the strike *at* spot: **770 alone carries −$904.1M net GEX, over 75% of the entire negative book in one ATM strike.** Dealers are short gamma exactly where price sits, so hedging flow amplifies moves toward either wall rather than pinning. Not fresh: `total_gex` has been negative on 13 of the last 18 sessions since 08-17, with brief positive interludes (08-13, 08-14, 08-27, 09-03) that reverted within a day or two. **Structure bias:** debit verticals / directional 0DTE in the break direction once the opening range resolves; **avoid selling ATM premium** — a short straddle or iron fly fights the amplifying flow here. If the open pins 769–770, a long straddle toward the 760/780 walls is the cleaner structural read with VIX at 14.53.

**QQQ — a live flip zone, and the tool's own label is wrong.** Spot 718.32, `zero_gamma_level` 243.37 (**>65% away from spot — a corrupt extrapolation**, `zgl_reliable: false`), and the tool prints `regime: POSITIVE` while `total_gex` is **−$237,297,106**. This is the documented regime-label defect firing live: the label is `sign(spot − ZGL)`, not the gamma sign. **Trusting `total_gex` sign only, this is short-gamma.** Call wall 720 (+$86.6M, +0.23%), put wall 718 (−$242.1M, −0.04%) — a ~2-point / 0.3% band essentially co-located with spot. `total_gex` has flipped sign four times in the trailing nine sessions (08-27 +$1.15B, 08-28 −$90M, 08-31 +$197M, 09-01 −$1.06B, 09-02 −$305M, 09-03 +$360M, 09-04 −$237M) — a genuine flip zone, not a settled regime. **Structure bias:** wait for the first 30–60 min of fresh 0DTE OI before committing; do **not** put on an iron fly or short straddle against a negative `total_gex`.

**Mandatory caveats:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in over the first 30–60 min and re-computes the map — acute for SPY, where −$904M sits in one near-dated ATM strike.
- **ZGL reliability.** Both indices are `zgl_reliable: false` today — SPY's is `null` on a FULLY_NEGATIVE day, QQQ's is an extrapolation >65% from spot. Fall back to the `total_gex` sign plus spot-vs-wall position.
- **Gap risk voids the prior.** PPI 09-10, CPI 09-11, FOMC+SEP 09-15/16 can gap spot through the walls before any hedging mechanic engages.
- **Tooling limit.** `uw` cannot isolate the D+1 expiry (`gex --dte-max 1` errors). This is the standing **0–45 DTE** book, the best available proxy.
- **ETF book**, not the cleaner SPX/NDX index book.
- **`regime_flip_dates` from `gex-time-series` was NOT trusted** — the known ZGL corruption makes it unusable (`zgl_delta` swings of hundreds of points in a day).

Context checks (no re-fetch): `expiry_heatmap` shows 09-04 (0DTE, now expired) $5.69B, **09-18 monthly OPEX $3.78B**, **09-11 CPI day $2.76B**, 09-09 $1.11B — near-dated expiries hold meaningful share. `greek_screener` top-gamma prints are SPX/SPXW index book.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — the validated stack)

The GEX walls above are a **map, not a pin** — wall-as-magnet backtested NO_GO, as did every directional signal. What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, not a guaranteed edge.

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` / VIX | **LOW** / 14.53 | **LOW** / 14.53 |
| `implied_move_pct` | 0.36% | 0.53% |
| `expected_range_pct` | 0.99% | 1.63% |
| `size_scalar` | 0.5 | 0.5 |
| `suggested_structure` | wider iron condor, wings ≈ ±0.99% | wider iron condor, wings ≈ ±1.63% |
| gross `mean_pnl_open_pct` | 0.262% | 0.399% |
| **net `mean_pnl_open_net_pct`** | **0.162%** | **0.299%** |
| `stand_aside_reason` / `caution` | null | null |

`backtest.verdict` = `GO_PREMIUM_SELL_INTRADAY` (n=60, win 88.3%). **Quote the PnL on its real basis:** `pnl_basis` is *percent-of-underlying-spot-notional, GROSS* — not premium-collected, not margin-relative. **Lead with net.** In the **LOW-VIX tercile that actually applies today**, the means are SPY 0.218% / QQQ 0.353% gross → **net +0.118% / +0.253%** after the assumed 0.1% round-trip. That is a thin edge.

- **Entry:** at/after the open once the overnight gap resolves; if it gaps beyond the wings, stand aside. **Hold to the close — never carry overnight** (overnight entry backtested negative; SPY `mean_pnl_overnight_pct` +0.047%, QQQ **−0.027%**).
- **Direction:** none. Delta-neutral. Do not add a directional tilt.
- **SPY ≈ SPX** (validated identical). **QQQ is weaker** — the Nasdaq index book is unavailable; flag its lower confidence.
- **Tail UNSAMPLED** — the validation sample contains no vol shock, so the short-vol left tail is unmeasured. `worst_day_open_pct` is −0.892% (SPY) / −1.068% (QQQ) *within the sampled window only*.

**⚠ Direct tension worth stating rather than burying:** the 0DTE model says *sell premium*, while SPY's own dealer book is decisively **short-gamma with −$904M at the ATM strike**, which argues moves get amplified, not dampened. These two advisory reads disagree. The short-gamma read argues for the **wider** end of the wing guidance or standing aside — and with a thin LOW-VIX net edge and an unsampled tail, standing aside into the CPI/FOMC fortnight is the defensible choice.

**Promotion bar:** this lane stays advisory / 0 rubric points **permanently** until BOTH a vol-shock day enters the sample AND **net** expectancy clears a tail-aware bar. Win-rate is explicitly NOT the promotion metric for a negatively-skewed short-vol strategy.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

Every DEX-flip verdict was computed by `python3 scripts/dex_flip.py` over 11 dated sessions (2026-08-21 → 09-04). Hand arithmetic was not used anywhere.

**The dated VIX leg fails, so no vanna-squeeze flag can validly fire today.** ^VIX closes: 08-28 14.43 → 08-31 14.92 → 09-01 16.34 → 09-02 15.20 → 09-03 14.32 → **09-04 14.53**. VIX is *not* falling for ≥3 sessions — it rose today. IWM, AMAT and TSLA carry put-heavy (long-vanna) books and would be squeeze candidates only on a resumed VIX decline; they are reported as **"vanna pressure, not squeeze."**

**Index level — no flips, all NEUTRAL:**

| | SPY | QQQ | IWM |
|---|---|---|---|
| DEX state | mixed/whipsaw | mixed/whipsaw | NEGATIVE (persistent) |
| `dex_flip_detected` | **false** (4 sign changes, whipsaw) | **false** (4 sign changes, whipsaw) | **false** (1 sign change, no run) |
| vanna | SHORT (call-heavy) | SHORT (call-heavy) | **LONG (put-heavy, +51,873)** |
| `total_gex` 30d | 13/30 pos — choppy | 17/30 pos — choppy | **23/30 negative** |
| front-end IV ratio (dte7, 4× read) | 0.949 | 0.830 | 0.896 |
| swing bias | NEUTRAL | NEUTRAL | NEUTRAL-to-cautious |

IWM's persistently negative 30d gamma book is carried forward as **regime context** (amplification risk), not as a scored line.

**Only two names earn the mechanized +1 — and both come with the same caveat:**

- **CRWV — QUALIFIES, LONG.** `net_dex` 2026-09-03 −$192,504,843 → 2026-09-04 **+$462,502,925**; the prior six sessions (08-27 → 09-03) all negative; |flip| **10.42× the floor** ($44.4M = 0.25× the trailing-10 median $177.5M); **`whipsaw_warning: false`** — a clean series. GEX-confirmed not a single-strike artifact (top strike 18.4% of gross |gex|). Corroborated same-day by `total_gex` flipping from five negative sessions to +$22.9M.
- **NBIS — QUALIFIES, LONG, but discount it.** |flip| **14.41× the floor** (the largest ratio on the board) — but **`whipsaw_warning: true`, 6 sign changes in 11 sessions.** The sign change *is* this series' baseline behaviour, not a regime flip.

**⚠ The caveat that travels with both:** each flip is dated to the *same session* as a large realised rally — CRWV +5.7% (81.61 → 89.28), NBIS +6.7% (210.51 → 224.53). This is dealer flow **confirming a move already in the tape, not leading it** — a materially weaker form of the "flow precedes price" hypothesis the line rests on, and the reason the rubric demoted it +3 → +1 and mechanized it. The desk's standing falsifier treats a flip dated to a large same-session move as presumptively mechanical.

**Screened, no flip (context only):** MU, SNDK, INTC, NVDA, DRAM all show DEX **levels** deepening with 0 sign changes — the textbook case the mechanized rule exists to reject. **PATH** produced a real sign change with a clean 10-session prior run and `whipsaw_warning: false`, but **failed the magnitude floor** (|−$7.18M| < $27.02M, ratio 0.27) → explicit watch item, not a call. MRVL and META flipped 2–4 sessions ago (not the latest session). ALAB, APP and **TSLA (9 sign changes in 11 sessions)** are too noisy to read.

---

## 2b. Sector Rotation

**Direction reads off the NETTED `uw risk market-regime.sector_rotation` only.** `sector-flow` and `sector-flow-persistence` are one *gross-turnover* source and cannot express direction — today persistence fired **INFLOW at 1.0 on 7 of 11 sectors and 0.8 on 2 more**, its documented zero-discrimination signature. It is a durability filter, nothing else.

| Sector | Persistence | Netted | Gross | Verdict |
|---|---|---|---|---|
| Technology | 1.0 | **+$435.3M IN** | +$4.50B | **AGREE — rotation call** |
| Financial Services | 1.0 | **+$23.8M IN** | +$359.7M | AGREE, but smallest netted-IN leg |
| Utilities | 0.6 ROTATING | +$7.0M IN | +$56.3M | agree on sign, marginal magnitude |
| Communication Services | 1.0 | **−$75.6M OUT** | **+$394M** | **DISAGREE → watch_only** |
| Consumer Cyclical | 0.8 | **−$121.8M OUT** | **+$217.7M** | **DISAGREE → watch_only** |
| Industrials | 0.6 ROTATING | **−$39.2M OUT** | **+$252.2M** | **DISAGREE → watch_only** |
| Cons Defensive / Energy / Healthcare / Basic Mat / Real Estate | 1.0 / 1.0 / 1.0 / 1.0 / 0.8 | **n/a — truncated** | small | **no netted read → watch_only** |

`market-regime.sector_rotation` is a **top-3/bottom-3 truncation**, so five sectors have no netted direction at all. Persistence firing 1.0 on four of those five is the saturated-metric artifact, not evidence.

**Rotation regime call: `no_change`, confidence LOW.** The IN leg spans growth, value and defensive simultaneously — not a coherent macro pattern — and the entire OUT leg is netted-vs-gross disagreement, i.e. unconfirmed two-way churn rather than de-risking.

**The real story is an intra-sector split inside Technology, not a GICS rotation.** Technology's +$435.3M netted inflow is concentrated in **memory/semis** while **software inside the same GICS bucket is being sold**:
- **IN:** MU +$143.9M, SNDK +$90.9M, INTC +$42.6M, MRVL +$15.7M, CRWV +$14.4M, AMAT +$6.2M, NVDA (30d +$255.2M)
- **OUT:** MSFT −$24.5M, AAPL −$20.2M, HOOD −$12.3M, SNOW −$10.3M, PATH −$8.8M, PLTR −$8.0M, NTNX −$7.5M, COIN −$7.0M

This matches the tape exactly (SOXX +3.52% / SMH +2.61% vs IGV −2.23%). **"Technology IN" is a semis/memory call, not a blanket tech long.**

**ETF flow tape (advisory — 0 rubric points; 33 of the 40-call cap used):**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| **EWY** | inflow +$12.25M | BULLISH | large ask-side blocks ($94M, $37M) | **long-dated 2027 calls** ($27.7M Jun-27 $160C, $10.5M Jun-27 $245C) | n/a (country basket) | — (Samsung/SK Hynix proxy — cross-asset memory corroboration) |
| **XLK** | inflow +$7.99M | BULLISH | mixed small blocks | thin, mostly 0DTE | **agree** (Tech IN) | see Tech leaders |
| XLC | inflow +$0.33M | BULLISH but negligible | small, near mid | none | reinforces Comm Svcs watch_only | — |
| **SMH** | **outflow −$71.6M** | BEARISH | mixed ($110M/$49M buy-side vs $38M sell) | **protective puts dominate** — $24.3M Jan-27 $580P, $15.0M Oct-16 $535P vs only $11.7M Oct-16 $615C | **disagree** with Tech IN | — |
| **IGV** | outflow −$10.2M | BEARISH | mixed small-to-mid | $6.18M Dec-18 $100P (`no_side`) | **confirms the software-sold leg** | — |
| KRE | outflow −$5.1M | BEARISH | thin, no tell | none | **disagree** with Fin Svcs IN | — |

**Two disagreements worth stating plainly.** (1) **SMH — the sector's own vehicle — is being hedged into the rally**, not chased: −$71.6M over 5d dominated by protective puts on a +2.61% day. (2) **KRE disagrees with the Financial-Services IN call**, which means that call is **CRCL/fintech-driven, not regional-bank breadth** — and CRCL is itself the name the sector leg then qualifies, which is close to circular.

**Single-name leaders — conditional +1 check** (a) persistence ≥0.6, (b) cum_flow_30d aligned, (c) |cum_flow_30d| ≥ $50M:

| Ticker | Today net | cum_flow_30d | Aligned | ≥$50M | +1? |
|---|---|---|---|---|---|
| **SNDK** | +$90.9M | +$968.2M | yes | yes | **PASS** |
| **NVDA** | +$7.6M | +$255.2M | yes | yes | **PASS** |
| **CRCL** | +$7.6M | +$65.6M | yes | yes | **PASS** |
| MU | +$143.9M | **−$105.5M** | **no** | — | FAIL — *largest single-day bullish print on the tape against a net-bearish 30d: distribution into strength, not accumulation* |
| INTC | +$42.6M | −$138.3M | no | — | FAIL |
| MRVL / AMAT / IREN | small | −$2.6M / −$5.7M / −$9.3M | no | no | FAIL |
| VST | +$6.3M | +$6.2M | yes | **no** | FAIL (c) |

**Energy / tanker cluster:** the `fz` RS lane surfaced a clean new-high cluster (FRO, INSW, DHT, NAT — LPG and CMBT **failed C12** and cannot be proposed). But Energy is not in the netted top-3/bottom-3 → **no netted direction**, XLE 5d options flow is flat/MIXED and XOP is BEARISH −$3.2M despite XLE price +2.20% over 5d. Flow does not confirm the price move. **Appendix / watch-only, not a rotation call.**

**Swing-book implication:** the only defensible rotation expression is the memory/semis leg, and even there the vehicle matters — **avoid SMH and IGV** (both show options-flow disagreement), treat **MU and INTC as momentum-only, not accumulation**, and downgrade everything one notch for the 48.9%-0DTE retail tape.

---

## 3. Swing Setups (1–6 weeks)

**Nothing is sized. The entire section is `skip` or `watch_only`.** Presented in full because the counterfactual must keep resolving.

Ranked by conviction score:

| Ticker | Score | Tier | Dir | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|---|---|
| NVDA | 3 | LOW | long | Tech netted-IN leader; vol kink + 30d accretion | defined-risk debit spread | **loses the $231 DP shelf** (2nd-tier, 162 trades — *not* the $230.36 closing bucket) | **skip** |
| CRCL | 2 | DROP | long | Fin-Svcs netted-IN leader, cleanest cum-flow by scale (5.74% of gross) | — | loses $87.72 (10d base) | **skip** |
| CRWV | 2 | DROP | long | Cleanest mechanized DEX flip on the board | — | DEX reverses negative ≥3 sessions | **skip** |
| NBIS | 2 | DROP | long | DEX flip 14.41× floor, but whipsawing | — | any single session flipping net_dex negative | **skip** |
| SNDK | 2 | DROP | long | Largest absolute 30d cum-flow (+$968.2M) | — | **loses the $1720 DP shelf** (2nd-tier, 72 trades — *not* the $1740 closing bucket) | **skip** |
| VFC | 1 | DROP | **short** | Coordinated put diagonal roll | Mar-2027 $14P vs closed Sep-18 $15P | reclaims and holds **$15.00** | **watch_only** |
| SNOW | 1 | DROP | **vol_long** | Largest kink prominence in an 18-name sample | Sep-18 straddle / Sep18-Oct16 calendar | kink dissipates, or RV10/20 fall under IV30 | **skip** |
| TSLA | 1 | DROP | **short** | Only clean 5-of-5 bearish sweep persistence | — | flow flips bullish ≥2 sessions | **watch_only** |
| MSFT | 1 | DROP | long | 30d cum-flow +$784.8M | — | — | **skip** (+ **EXIT CANDIDATE**) |
| ECHO / LMT | 1 | DROP | **short** | Tier-1 FLOOR_PUT_BLOCK whales | — | — | **watch_only** |
| INTC | 0 | DROP | **short** | DP distribution; C28 flag present | — | — | **watch_only** |
| GE / PATH / LULU / ADBE / ORCL | 0 | DROP | unresolved | see §8 | — | — | **skip** |
| AI / BE | −1 | DROP | long / **short** | see §8 | — | — | skip / **watch_only** |
| **MU** | **−3** | DROP | long | **flow_conflict fires** | — | — | **skip** |

### 3a. Long swings (regime-aligned)

**None sized.** The four semis/memory longs (NVDA, CRWV, NBIS, SNDK) plus CRCL all die on the same stack: the event-risk gate (CPI T+4, FOMC T+7) and a lost debate, with three of five additionally carrying a fundamentals CAUTION.

The evidence problem underneath them is worth stating once, clearly, because it recurs across the whole board: **the semis melt-up's dark-pool signature is overwhelmingly closing-cross and basket-program contamination, not accumulation.** Contamination share of visible mega-tier premium — **SNDK ~98%, INTC ~96%, NVDA ~94%, MU ~65%**. A **$500.0M identical-notional clip at 21:17:20Z hit NVDA, GOOGL, SPY and SNDK simultaneously**, and `dark-pool extended-hours` independently confirms SNDK's two largest prints ($448.0M @20:28:24Z, $318.8M @21:17:06Z) are tagged `extended_hours_trade` **at exactly the closing price**. That is post-close benchmark flow. **Peer-complex "corroboration" across the semis is one program print smeared across correlated names — not four independent signals.**

**Distribution cautions (C28, advisory, 0 points, no sizing impact):**
- **INTC** ⚠ 2028 LEAP call OI −3,646 on $13.6M premium — institutional-size call *closing* in the same session `institutional-accumulation` mislabelled the name ACCUMULATION.
- **SNDK** ⚠ Sep-18 $1800C OI −96 on 708 volume, avg $16.74 (positive time value — a genuine OTM close) sitting alongside the $968M cum-flow.
- **MU** ⚠ Oct-16 $910C OI −366 on 1,597 volume — but avg price 95.63 vs intrinsic ~106, i.e. **negative time value**, so parity/exercise-linked rather than conviction distribution. Low confidence.

**Sweep ledger (informational — 0 rubric points; the sweep-persistence line was removed 2026-05-23 P0.3 at −22pp marginal).** Only **TSLA** clears ≥3-of-5 same-direction persistence cleanly (bearish, 5/5, $4.99B 5d, consistency 1.0 — confirming today's −$109.5M net premium). **MSTR** is bullish 3/5 but both dated legs are 0DTE/7DTE on a 48.9%-0DTE tape — discount toward noise. **MSFT** is bullish-persistent 3/5 but **contradicted** by today's −$24.5M bearish print → watch-only. MU, NVDA, SNDK, AAPL, META, AMZN, SPCX and PLTR all carry high persistence with **MIXED direction** → disqualified as directional reads. SPX/SPXW dominate 13 of 20 sweep rows and 17 of 20 top-premium tickets — index hedge book, filtered out. *Coverage gap flagged: per-ticker expiry/DTE for TSLA, MSFT, MU, SNDK, META could not be resolved from the assigned tool set (the market-wide tools are top-20-only and were crowded out by index names).*

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only` and none are sized (2026-08-01 P0 #1). This is routing, not suppression** — six shorts were generated, fully scored, gate-verdicted and serialized so the counterfactual keeps resolving.

**VFC — the best-evidenced structure on the entire board, and it scores 1.** A coordinated **put diagonal roll**: closing `VFC260918P00015000` ($15P, 14 DTE) against opening `VFC270319P00014000` ($14P, 196 DTE), **lot-for-lot matched** (1750/1750, 1682/1682, 1645/1645, 1575/1575, 1000/1000) at matching timestamps, **repeat_count 3** across 08-31 → 09-04. Term-structure anchor: rolling *out of* the front-month IV kink (14dte 50.8%, 1,947 contracts) *into* the flat back-month plateau (196dte 46.3%, 834 contracts) — a duration extension that deliberately steps outside the CPI/FOMC event window. **GEX-confirmed:** $14 and $15 are the two largest negative-GEX strikes on the whole chain (−$10.3M / −$20.9M; next largest anywhere −$979K). **Parity PASS on both legs** (Sep $15P time value +$0.06–0.14; Mar $14P +$1.33–1.42) — real conviction, not a box/conversion financing leg. Net **long** vega, so the short-vol routing rule does not apply. Corroborated by two independent agents reading DISTRIBUTION (`dark_pool buy_ratio` 0.294; put_bid 88,134 ≫ put_ask 54,864). Invalidation: VFC reclaims and holds above **$15.00**, or the Mar-2027 $14P OI starts declining.

**TSLA** — the only clean 5-of-5 bearish persistence name, corroborated by an aligned 30d (−$142.1M) *and* 90d (−$744.5M) cum-flow, and a zero-defect-verified price-vs-flow divergence (price +14.5% vs bearish flow). Its win-rate is measured — **0.4894 on n=141 clean rows** — with **market_excess −0.0851**, i.e. the class does not beat simply shorting the index. Flagged `beta`.

**ECHO / LMT** — Tier-1 `FLOOR_PUT_BLOCK` whales ($2.4M, delta −0.857; $3.6M, delta −0.943). ECHO's 30d net is **31.8% of its own gross** with 30d ≈ 90d (−$142.6M vs −$141.0M) — durable, scale-clean signed conviction, better than any long on the board on every quality axis except absolute size. Advisory, permanently 0 points (C19 closed as REFUTED). The whale-plus-crowding co-flag **fails on all three** (pc-ratio z NORMAL).

**INTC** — `institutional-accumulation` returns ACCUMULATION (buy_sell_ratio 2.23); this is a **confirmed false positive**, ~96% of it three closing-cross clips at $95.80. cum_flow_30d −$138.3M, 90d −$869.4M, C28 flag present.

**No fade candidates from the crowding lane.** All 18 names tested printed `extreme: NORMAL` on `pc-ratio-zscore` — none cleared ±2σ, and the tool has no `--date` so no "rising" trajectory is establishable. **Consequently the −2 informed-flow-continuation penalty fires on nobody today**, including the melt-up names: SNDK's z is **+0.086**, essentially its 20-day mean, on a +11.9% day. The euphoria is real in flow dollars but is *not* corroborated by the crowding statistic.

---

## 4. LEAP Builds (6–24 months)

**Empty — and correctly so.** `uw oi biggest-increases --min-dte 180` returned only 20 rows market-wide, dominated by bond/ETF names (IEF, LQD, EWZ, HYG) and non-C12 names. Only two C12 names appeared:

- **IREN — DISQUALIFIED, 2 of 9 gates.** Fatal: 90d cum-flow **−$71.4M, MIXED** (the explicit disqualifier — no accretion signature) and `conviction-matrix` **MIXED at 4.3%** confidence (hard reject, not even a directional label). Its 742-DTE (2028-09-15) $120 put/call pair added ~7,200 OI on **both** legs the same session against prior ask/bid volumes of only 1–67 contracts — the signature of a **synthetic-stock / conversion-reversal block**, not a directional LEAP bet.
- **VFC — DISQUALIFIED, 1 of 9 gates.** `consecutive_build_days` = 1 at both the default and `--days 10` (a genuine single-day spike, not the censoring artifact); 30d cum-flow −$658K MIXED; `conviction-matrix` **DISTRIBUTION** at 20.6% — a mandatory reject scenario.

Structural context: LEAP share of total DTE volume is **3.1%**, the thinnest bucket on the board, against 48.9% 0DTE. A rising 10Y (4.77%) is a direct duration headwind. A clean empty LEAP board is the expected output on this tape, not a coverage gap.

---

## 5. Volatility Surface

**Substrate hygiene was run on all 18 names — `scripts/term_structure_hygiene.py --near-dte 7 --min-contracts 15`. 13 of 18 flipped** (raw label ≠ hygiene shape), consistent with the documented defect. Every `dte_approx: 0` bucket (250–2000%+ max_iv) was dropped. `min_contracts` = 15 is a **tunable, not audit-frozen** — reported, not treated as settled.

**Macro null computed FIRST, as required:**
- **SPY:** raw CONTANGO → hygiene **KINKED**, `kink_dte` **7 (2026-09-11, CPI)**, prominence 16.6%; `base_shape` still CONTANGO.
- **QQQ:** CONTANGO throughout, with a *sub-threshold* near-miss at dte 7 (prominence 4.5%, under the 5% floor) — same CPI date.
- **⇒ dte 7 / 2026-09-11 is shared index-level attention. Any single name kinking at that exact dte is presumptively macro beta, not edge.**

**Names sharing the CPI null — context only, NOT tradeable edge:** **NVDA** (kink dte 7, prominence 15.4%, implied move 5.12%), **MU** (18.9%, 8.24%), **DRAM** (9.6%, 7.76%). All three flipped from raw BACKWARDATION to KINKED on a CONTANGO base.

**Two confirmed BUY VOL candidates — neither is constrained by the short-vol routing rule (both net long vega):**

**SNOW — the session's best idea, and the rubric cannot score it.** Hygiene **KINKED** (flipped from raw BACKWARDATION), base CONTANGO, `kink_dte` **14 / 2026-09-18 (OPEX)**, prominence **44.1% — the largest in the 18-name sample, and matching neither index null.** `implied_move` **12.72%** at the kink expiry against **6.14% / 10.82%** on the neighbouring tenors — a real hump in *dollar-move* terms, not annualized-IV smoothing. VRP −0.2194 PREMIUM_BUYING, **confirmed and reinforcing**: RV is *freshly expanding* (122.5 / 91.2 / 67.1 / 60.8 vs IV30 42.54%) — the opposite of the stale-RV failure mode. No earnings catalyst in the 14-day screen. Term-skew 1.012, flat → a pure vol-level play with no directional tilt. Structure: long Sep-18 straddle, or a Sep18/Oct16 calendar. Invalidation: kink dissipates at next read, or RV10/20 fall back under IV30. `iv-percentile` z −2.28 is **PROVISIONAL** (`dates_used` n=102 < 120).

**NVDA — BUY VOL, but self-disqualified as idiosyncratic edge.** VRP −0.1224 PREMIUM_BUYING robust across RV10/20/30 (24.4 / 55.3 / 43.7 / 44.3 vs IV30 33.2%); implied move 5.12% (dte7) / 9.52% (30d); term-skew 1.075 NORMAL. But its kink **matches the SPY CPI null** — shared macro beta. Note also that NVDA's `iv_rank` collapsed **42.7 → 9.4 over ten sessions** while price ran +10.5%: options are cheap, but the vol lane has little left to harvest.

**Confirmed real BACKWARDATION — all three fail the confirmation leg:**
- **LULU:** `front_end_ratio` **1.159 — above the 1.10 panic bar, on the day of a −17.38% crash.** RV5 124.2% vs RV30 66.2% confirms the trailing-RV distortion is today's gap. **Do not fade.**
- **PATH:** real backwardation but −16.63% today; RV5 122.1% → RV30 79.2%. The "cheap" −0.2095 VRP is a same-day event artifact.
- **U:** ratio 1.024 (flat), thin contracts. Its RV pattern **inverts** the usual staleness direction — RV30 58.2% ≫ RV5/10/20 (35.1 / 26.9 / 29.8), so the headline "cheap" VRP **flips to fair/rich on a de-staled read**.

**Stale-RV falsifier applied across the VRP scan — it killed three of eight headline "edges":**

| Ticker | IV30 | RV5/10/20/30 | Headline VRP | Confirmed? |
|---|---|---|---|---|
| **SNOW** | 42.54% | 122.5/91.2/67.1/60.8 | −0.2194 | **CONFIRMED, reinforcing** |
| **NVDA** | 33.2% | 24.4/55.3/43.7/44.3 | −0.1224 | **CONFIRMED** (3 of 4 windows) |
| MU | 66.02% | 45.3/49.1/52.9/82.4 | −0.1946 | **stale artifact** — only RV30 clears IV |
| DRAM | 63.71% | 50.6/53.1/62.5/80.9 | −0.2016 | **stale artifact** |
| **NBIS** | 81.77% | 58.4/62.9/127.5/145.8 | **−0.776** (largest headline on the board) | **STALE ARTIFACT — the biggest one.** RV5/10 sit *below* IV30; the whole reading is an old RV20/30 spike |
| PATH / LULU | 57.74% / 40.16% | crash-dominated | −0.2095 / −0.2331 | **event-contaminated — discard** |
| U | 44.5% | 35.1/26.9/29.8/58.2 | −0.1691 | **stale, inverse direction** |

**Term-skew:** SPY 1.512 and QQQ 1.326 are both **TAIL_HEDGING** despite index IV near a YTD-low percentile — hedging demand is present even though outright level is cheap, consistent with the CPI/FOMC stack. MU 0.975 / NBIS 0.988 COMPLACENT (call-rich), but both fail the high-IV-rank condition (percentile 5–24) so no lottery flag applies.

**Flipped to CONTANGO with no kink at all** (raw BACKWARDATION was pure 0DTE contamination — no dislocation): MRVL, CRWV, IREN, **SNDK**, AMAT, MSTR.

**IV outliers:** all sub-C12 or 0DTE noise (DNN, SVIX, SOXL binary strikes; BE/SNDK/PATH deep-OTM single contracts expiring today). Not tradeable. **The `iv-rank --mode high` screen is saturated** — all 25 rows print `iv_rank: 100` and are microcap/illiquid; C12 empties the lane entirely. Graded by population firing rate, 25-of-25 at the maximum is not a discriminator.

**Earnings vol — zero scoreable candidates.** ADBE and ORCL (both reporting 2026-09-10 postmarket, 6 days out) carry genuinely elevated front ends — `front_end_ratio` **1.407** and **1.525**, deterministic across 4 repeated calls with `near_dte_actual: 7` both times. But **that dte-7 tenor IS 2026-09-11 = CPI day, and SPY's own hygiene kink lands on the identical dte** — so the elevated front end is a *mix* of earnings premium and shared macro, not clean name-specific edge. Back-month term-skew is **−0.0186 COMPLACENT on both** — the textbook "coin-flip, do not size SELL VOL" profile. `analyst-vs-flow` returned **zero analyst rows** (the documented 0/21 defect). Re-derived implied moves ≈ **8.3%** (ADBE) and **11.5%** (ORCL) — note the cached `implied_move_perc` of **0.39%** is the dte=1 pre-event-tenor defect and is **not** quoted.

---

## 6. Risk & Correlation

**Macro headline:** yield curve normal (+0.41); core CPI 2.79%; **core PCE 3.34% sticky above target**; unemployment 4.1%; payrolls +162k; **10Y 4.77% RISING**; USD weakening; fed funds 3.63%. **Forward stack: PPI T+3, CPI T+4, FOMC+SEP T+6/T+7, OPEX T+9, PCE ~T+14.**

**Breadth cross-check (`fz`, advisory, 0 points):** 175 advancers / 327 decliners of 503; **`pct_green` 34.79%**; avg change −0.43%, median −0.56%. **`divergence_flag: true`** — `uw` labels the trend UPTREND and QQQ closed green, yet fewer than 35% of S&P names advanced and the median name fell. A narrowing-leadership / distribution tell that the single regime label hides. Advisory; it does not change sizing.

**Correlation — the tool was NOT degenerate today, and that is itself worth recording.** `portfolio-correlation` was cross-validated against 60-session log-return correlations computed from `uw historical trend` closes. **Max deviation 0.015.** The documented "0.97–0.996 on every pair" failure mode is **absent this session** — the tool is computing log returns correctly and is reproducible. (`sector_breakdown: {"Unknown": 10}` with its spurious 100%-concentration warning is the known artifact, ignored.)

| Pair | Tool | Self-computed | Δ |
|---|---|---|---|
| CRWV/NBIS | 0.844 | **0.841** | 0.003 |
| SNDK/INTC | 0.771 | **0.774** | 0.003 |
| NBIS/SNDK | 0.620 | **0.632** | 0.012 |
| NVDA/INTC | 0.534 | **0.536** | 0.002 |

*Illustrating why this matters:* on **price levels** rather than returns, NVDA/INTC computes **−0.394** versus **+0.536** on returns — anyone reading level correlations gets the sign wrong.

**Clusters applied DIRECTIONALLY** (only same-direction names concentrate risk; a long/short pair is an offset):
- **`AI_infra_cluster` FIRES (long):** CRWV/NBIS **0.841**. Kept member **CRWV** (raw tie 2/2, broken on cum_flow_30d +$229.3M > +$171.4M). **NBIS −1 tier.**
- **`short_industrial_cluster` FIRES (short):** INTC/BE **0.732**. Kept **INTC** (raw 0 > −1). **BE −1 tier.**
- **Soft watch, no penalty (0.60–0.70):** NBIS/SNDK 0.632, CRWV/SNDK 0.612.
- **Explicit offsets — NOT charged:** **SNDK/INTC 0.774** is long-vs-short, a *hedge*, not a concentration. Charging it would be exactly the direction-blind error the register documents. Also NBIS/BE 0.678, CRWV/BE 0.639, SNDK/BE 0.622.
- **NVDA carries no cluster flag** — its highest same-direction correlation is 0.459 (CRWV), below the soft band. Despite the "AI complex" narrative, NVDA is not statistically the same bet as CRWV/NBIS over 60 sessions. **SNOW** likewise clean (max 0.481).

**Gates applied.** VRP **FAIR** at the index → no VRP gate fires either way. **Panic gate:** all candidates re-read at `--near-dte 7`, 3–4× each per the non-determinism defect — **all deterministic today, zero variance across repeats.** Two fires, both on `watch_only` shorts: **BE 1.209** and **LMT 4.349** (LMT's is a thin-tenor substrate artifact rather than genuine panic, but the gate is mechanical and is recorded as fired). Index readings SPY 0.949 / QQQ 0.830 are well below the bar.

**Fundamentals verdicts (top-5):** NVDA **CONFIRM** (0), CRCL **CONFIRM** (0), CRWV **CAUTION** (−1, `insider_selling_cluster`), NBIS **CAUTION** (−1, `insider_selling_cluster`), SNDK **CAUTION** (−1, `insider_selling_cluster`). **No VETOs**, and **no top-5 name has earnings inside the horizon** (61–74 days out). The pattern the gate surfaced: **three of five are insider-selling clusters, and SNDK's is MSPR −99.78 — near-total liquidation — landing exactly on its +11.9% day.** That is distribution wearing an accumulation costume, and it independently corroborates the ~98% dark-pool contamination finding. CRWV's contradicting facts are the hardest: net margin −25.4%, ROE −45.37%, **current_ratio 0.4555 (sub-1)**, debt/equity 6.48, plus a dated same-day bearish catalyst.

**Debate disconfirmation — the bear won 5-for-5**, with four of five bulls unable to clear 0.35 residual and SNDK's bull finishing at **0.15**. Two bear findings are **methodological rather than name-specific** and invalidate confluence claims across the board:
1. **DEX and GEX are two partial derivatives of the same dealer option inventory** — "two structurally distinct measurements agreeing" is one fact counted twice. This undercuts the mechanized DEX-flip +1 on *both* CRWV and NBIS.
2. **The $500.0M identical-notional 21:17:20Z basket clip hit NVDA/GOOGL/SPY/SNDK simultaneously** — peer-complex corroboration across the semis is one program print, not four signals.

**Adverse-flow exits** (`conviction_2026-09-03` = GLD, IWM, MSFT, MSTR):
- **MSFT — EXIT CANDIDATE.** Carried long on a dark-pool accumulation thesis; flow flipped **bearish −$24.5M** the next session. It independently reappears on today's board at raw 1 DROP with its bullish sweep persistence contradicted by the same print. Two stages now disagree with yesterday's long.
- **IWM** — direction confirms (bearish −$9.05M, P/C 1.27) but **OI is unwinding (−88,088)**; soft decay tag, not a hard alert.
- **GLD** (−$8.17M, OI +438,369) and **MSTR** (+$142.3M, vol ratio 1.63) both confirm. No reversal.
- *`fz` fundamentals-drift tripwire returned "no field changes" on all four against a single snapshot — i.e. **no prior-day baseline exists (cold start)**. Read as `not measured`, not `clean`.*

**Hedge sleeve: NONE — and deliberately so.** The book is empty, so directional skew is undefined. A hedge against a zero book is not risk management; it is a naked directional bet wearing its clothes. For exposure carried in from outside this book, the structural read is hostile to premium selling: **−$904.1M of SPY's −$1.17B `total_gex` sits in the single 770 strike with spot at 769.88**, so hedging amplifies moves toward 760/780 rather than pinning them. With VIX at 14.53 the correct expression through 09-11 is **long convexity** — debit verticals or a 760/780 strangle — not short premium.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Empty. No ticker reached raw_score ≥ 7.** The highest score on the board is **NVDA at 3 (LOW)**.

**Expectancy lens `[advisory — expectancy is not yet a live sizing axis]`** — realised per-tier figures from the most recent `/calibration-audit` (2026-08-30, `phase_3_calibration`):

| Tier | n | Realised WR | Expectancy | Payoff ratio |
|---|---|---|---|---|
| HIGH | 7 | 14.3% | −2.441% | 0.720 |
| MEDIUM | 19 | 52.6% | +0.104% | 0.948 |
| LOW | 125 | 40.0% | −2.141% | 0.906 |
| DROP | 542 | 38.0% | −5.964% | 0.601 |

Display-only context, not a sizing input; the live sizer remains the win-rate ladder. It is worth reading today because it says the thing the desk keeps re-learning: **HIGH has realised 14.3% against DROP's 38.0%** — a 23.7pp inversion at the top — so a board that produces no HIGH-tier names is not obviously a board that produces no edge. The one honest bright spot is MEDIUM (payoff 0.948, the only positive expectancy), and nothing reached it today.

**Why the board is empty — the mechanical account.** The rubric's high-value lines were all *structurally unavailable* today, not merely unearned:
- **+3 accumulation conjunction: cannot fire.** `accumulation-hunter` returned **ZERO** qualifying names — no ticker satisfies block-stratified institutional-tier *and* a timestamp-clean mega read *and* `conviction-matrix` ≥ 50.
- **+1 conviction-matrix: cannot fire.** LEAP-gated, and the LEAP lane is empty.
- **+1 opex-pin: unavailable.** 2026-09-18 is 14 days out — not OPEX week.
- **−2 contrarian: cannot fire.** 18 of 18 tested names printed `pc-ratio extreme: NORMAL`.
- **+1 multi-day OI build: awarded to nobody**, because its owning agent (accumulation-hunter) advanced no name. *(Self-sourcing it across 20 names would have lifted five of them on a measurement with demonstrated zero variance — see the substrate note below.)*

What remained was a set of +1 lines. **A board built only of +1s cannot reach 7.**

### Full audited call list

| # | Ticker | Raw | Tier | Dir | Class | Pre-risk | Final | WR (source, n) | Excess | Fund. | Debate (bull/bear) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NVDA | 3 | LOW | long | sector_rotation | starter | **skip** | null NA(substrate) | null | CONFIRM | 0.35 / 0.65 |
| 2 | CRCL | 2 | DROP | long | sector_rotation | skip | **skip** | null NA(substrate) | null | CONFIRM | 0.25 / 0.85 |
| 3 | CRWV | 2 | DROP | long | dealer_positioning | skip | **skip** | null NA(substrate) | null | CAUTION | 0.25 / 0.75 |
| 4 | NBIS | 2 | DROP | long | dealer_positioning | skip | **skip** | null NA(substrate) | null | CAUTION | 0.25 / 0.85 |
| 5 | SNDK | 2 | DROP | long | sector_rotation | skip | **skip** | null NA(substrate) | null | CAUTION | 0.15 / 0.85 |
| 6 | VFC | 1 | DROP | short | multileg_directional | skip | **watch_only** | null NA(substrate) | null | NA | — |
| 7 | SNOW | 1 | DROP | vol_long | vol_term_dislocation | skip | **skip** | null NA(substrate) | null | NA | — |
| 8 | TSLA | 1 | DROP | short | bearish_flow | skip | **watch_only** | **0.4894 (backtest_clean, 141)** | **−0.0851** | NA | — |
| 9 | MSFT | 1 | DROP | long | bullish_flow | skip | **skip** | **0.5122 (backtest_clean, 123)** | **+0.0244** | NA | — |
| 10 | ECHO | 1 | DROP | short | single_leg_whale | skip | **watch_only** | null NA(substrate) | null | NA | — |
| 11 | LMT | 1 | DROP | short | single_leg_whale | skip | **watch_only** | null NA(substrate) | null | NA | — |
| 12 | INTC | 0 | DROP | short | dark_pool_distribution | skip | **watch_only** | null NA(substrate) | null | NA | — |
| 13 | GE | 0 | DROP | neutral | multileg_directional | skip | **skip** | null NA(substrate) | null | NA | — |
| 14 | PATH | 0 | DROP | neutral | vol_term_dislocation | skip | **skip** | null NA(substrate) | null | NA | — |
| 15 | LULU | 0 | DROP | neutral | vol_term_dislocation | skip | **skip** | null NA(substrate) | null | NA | — |
| 16 | ADBE | 0 | DROP | neutral | earnings_vol | skip | **skip** | null NA(substrate) | null | NA | — |
| 17 | ORCL | 0 | DROP | neutral | earnings_vol | skip | **skip** | null NA(substrate) | null | NA | — |
| 18 | AI | −1 | DROP | long | bullish_flow | skip | **skip** | 0.5122 (backtest_clean, 123) | +0.0244 | NA | — |
| 19 | BE | −1 | DROP | short | single_leg_whale | skip | **watch_only** | null NA(substrate) | null | NA | — |
| 20 | MU | **−3** | DROP | long | bullish_flow | skip | **skip** | 0.5122 (backtest_clean, 123) | +0.0244 | NA | — |

**NVDA — full audit trail (the only name that reached a conviction tier).**
`score_components`: **+1** vol-surface-scout / `uw options-structure term-skew` — hygiene KINKED, kink_dte 7, VRP −0.1224 robust across RV10/20/30. **+1** sector-rotation-strategist / `uw risk market-regime` — Technology persistence 1.0, netted +$435.3M IN, netted-vs-gross agree, cum_flow aligned ≥ $50M. **+1** signal-confluence-quant / `uw historical cumulative-premium-flow` — 30d +$255.2M, intent screen passed (no C28 flag, no ex-div sub-parity signature). **Σ = 3 ✓**
`gate_verdicts` (all 9): regime **no-op** · vrp **no-op** (index FAIR; the name's favourable −0.1224 cannot add size — the stack is downgrade-only) · panic **no-op** (1.016 @dte6, deterministic 4/4) · cluster **no-op** (max same-direction 0.459) · sector **no-op** (Tech IN, tailwind) · fundamentals **CONFIRM, no-op** · event_risk **−1 tier** (CPI T+4, FOMC T+7 — two named Tier-1 binaries, stacked) · debate **−1 tier** (bear 0.65 ≥ bull 0.35) · rubric_regime **capped half (OUT-OF-REGIME)**.
`starter −1 −1 → **skip**`. Outcome-invariant: even as a defined-risk debit spread the event gate only softens to −0.5, and `starter −0.5 −1` still floors at skip.

**Three findings the quant flagged that the calibration loop should see:**

1. **The sector-leader +1 and the cum-flow +1 double-counted on 3 of 3 affected names.** The sector-leader line's conditions (b) and (c) test the *identical field and threshold* as the standalone cum-flow line, and condition (a) is non-discriminating today (persistence fired 1.0 on 9 of 11 sectors). Collapse the duplicate and **NVDA drops to 2, SNDK and CRCL to 1** — i.e. the board's top name and two runners-up exist only because one bit of evidence is counted twice. Awarded per the freeze; flagged, not patched.
2. **The cum-flow deduction asymmetry fired 4 times, 3 of them scale-degenerate.** The award side carries two floors ($50M and 5%-of-gross); the −3/−1 deduction side carries **neither**. **MU took a full −3 on a net worth 0.19% of its own gross book** — one-fifth of one percent — which under the award side's floors would not qualify as directional evidence in *either* direction. BE took −1 on 1.28%; AI took −1 on $1.4M absolute despite being 5.01% of gross. Three of the four penalised names are shorts or short-adjacent. **MU is honestly a 0, not a −3**, and its 90d is **+$691.5M**, sign-opposite to the scored 30d window.
3. **Scale degeneracy on the *award* side too.** The +1 cum-flow line paid on nets worth **0.50% (TSLA), 0.80% (NVDA), 2.11% (SNDK), 2.27% (NBIS)** of their own gross books. Only ECHO (31.8%), CRWV (6.88%), CRCL (5.74%), MSFT (5.13%) and LMT (15.2%) would survive a scale floor on this line.

**And one coverage gap that is now confirmed on the daily side, not just the weekly.** **SNOW cleared all nine risk gates without a single deduction** — the only name on the board where the risk stack and the score disagree — and still floors at `skip` on a quant raw of **1**. A pure long-vol term dislocation maxes out at one rubric point (the single vol-surface line), so it is **incapable of clearing DROP by construction**, however good it is. This one is good: the largest kink prominence in an 18-name sample, matching neither index null, a 12.72% implied move at the kink against 6.14%/10.82% neighbours, and a VRP that is confirmed *and reinforcing* on freshly expanding RV rather than the stale artifact that killed NBIS and MU. It also sits in the one lane with measured positive edge (`vol_long` +9.5pp vs unselected same-date peers, n=43, McNemar p=0.0034, 5-for-5 on every sized row in the corpus). The weekly rubric already has this gap registered; **today it reproduced on the daily.**

**Substrate note — `oi-trend` censoring re-confirmed 4-of-4.** Probing `--days 10` on MU/MSFT/AI/TSLA returned `overall_trend: BUILDING` with `consecutive_build_days` **exactly equal to `--days`** on every name. Independently, `leap-positioning-radar` found IREN returns **103** consecutive build days at the default versus exactly **10** at `--days 10` — the censoring made visible in a single name. The rubric's `--days >= 5` OI line is tautological as written.

### Conviction rubric (verbatim, `rubric_version: 2026-06-12`)

```
Daily conviction score = Σ:
  +1  MECHANIZED DEX flip / vanna-squeeze in trade direction (verified SIGN CHANGE, not a level;
      computed by scripts/dex_flip.py; |flip| >= 0.25x trailing-10 median |net_dex|)
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified
      institutional-tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d
      confirms (sign aligned AND |cum_flow_30d| >= $50M); else halved to +1
  +1  multi-day OI build (oi-trend BUILDING, --days >= 5)
  +1  conviction-matrix DIRECTIONAL_LONG conf > 70 — ONLY when dominant_signal_class == leap_directional
  +1  cumulative-premium-flow net directional accretion 30d — INTENT-SCREENED (no C28 flag; no
      ex-div deep-ITM sub-parity calls on dividend payers)
  +1  sector-rotation single-name leader — CONDITIONAL on ALL of: (a) persistence >= 0.6,
      (b) cum_flow_30d aligned, (c) |cum_flow_30d| >= $50M
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored play type)
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist top-5 (OPEX week only)
  -2  contrarian-scanner overcrowded long with RISING pc-ratio-zscore (VRP positive)
  -3  flow_conflict — cum_flow_30d clearly opposite dominant_signal_class
  -1  flow_conflict_lite — 30d cum-flow MIXED / bottom-quartile magnitude
      (-3 and -1 are MUTUALLY EXCLUSIVE)
  [TIER GATES, applied by risk-monitor in 2d — 0 points, never in score_components]
  -1 TIER  correlation cluster (pairwise corr >= 0.70, applied directionally)
  -1 TIER  regime conflict with trade direction

Tiers: >=9 HIGH (full) | 7-8 MEDIUM (half) | 3-6 LOW (starter/watch) | <=2 DROP
```

**Deep-dive hand-off:** skipped — no HIGH-tier names. This is a no-edge day.

---

## 8. Watch-only — single signal, no confluence

Failed the ≥2-agent confluence gate. Listed for journaling, **not for trade entry**.

- **CRWV** — cleanest mechanized DEX flip on the board (10.42× floor, `whipsaw_warning: false`, GEX-confirmed) and a scale-clean +$229.3M/30d (6.88% of gross, 90d > 30d = durable). But `conviction-matrix` DIRECTIONAL_LONG at only **22%** vs the ≥50 floor, and the flip is **coincident with a +5.7% same-session rally**. 1 agent.
- **NBIS** — DEX flip at 14.41× the floor, but **`whipsaw_warning: true`, 6 sign changes in 11 sessions**, coincident with a +6.7% same-day rally, and the board's **largest stale-VRP artifact**. 1 agent.
- **SNDK** — sector-leader PASS on all three conditions with the largest absolute 30d flow on the board (+$968.2M). Killed by **~98% closing-cross/basket contamination**, `conviction-matrix` MIXED 10%, `institutional-accumulation` NEUTRAL, a post-hygiene flip to CONTANGO with **no kink at all**, MIXED sweep direction, and price already +36.13% over 30d. 1 agent.
- **CRCL** — sector-leader PASS and the **cleanest cum-flow on the board by scale** (5.74% of gross, explicit BULLISH). But the Financial-Services-IN leg is CRCL-driven and KRE disagrees (−$5.1M), so condition (a) is near-circular; the bull's own verification found the **mega-tier dark pool completely EMPTY (0 trades)** with the large tier at a coin-flip 0.513 buy ratio, and 90d MIXED at ~1% of gross. 1 agent.
- **SNOW** — see §5 and §7. 1 strong agent; the second flag was a *directional bearish* read being used to support a *delta-neutral* structure, which the quant correctly declined to count (that relabeling would let a flag in either direction support long vol, making the second-agent requirement vacuous).
- **PATH** — real DEX sign change, clean 10-session prior run, `whipsaw_warning: false`, but **below the magnitude floor** (ratio 0.27). Watch for a deeper negative print next session. Vol read is event-contaminated (−16.63% today).
- **MU** — **0 positive agents and 4 explicit disqualifications.** Today's +$143.9M is the largest single-day bullish print on the tape; its 30d cum-flow is **−$105.5M**. DEX is a **level with 0 sign changes** — the case the mechanized rule exists to reject. `conviction-matrix` MIXED 5.9%. VRP a stale artifact. The name today's tape would most have pulled a desk into, and it scored lowest.
- **INTC** — the `institutional-accumulation` ACCUMULATION label is a **confirmed false positive** (~96% closing-cross). C28 distribution flag present.
- **AI** — the *only* name clearing `conviction-matrix` DIRECTIONAL_LONG ≥50 (50.4%), plus the `fz` squeeze cross-hit (short float 34.14%, days-to-cover 8.27) and the board's highest bullish confluence score (6). Killed outright: **largest single DP print all day is $740K** — fails the mega/block-tier check, no exceptions. Multileg separately rejected its structure as dealer-hedge-shaped (`no_side`/mid prints, $15–17/contract, 0DTE/7DTE only).
- **GE** — a real ~$42M put diagonal, but **direction unresolvable**: neither contract appears in any of the last 5 sessions' top-20 OI-change lists despite a 12,100-lot trade, so it likely printed against existing OI (a **close**, not an open). Does not earn the +2. Worth a next-session OI re-check.
- **LULU** — front-end ratio 1.159 above the panic bar, but entirely today's −17.38% crash gap. Do not fade. Its −$415.2M/30d (44.9% of gross) is **scored in neither direction**: it matches the documented deep-ITM sub-parity financing signature (put premium of $100M–$324M per session on a ~$120 stock is only reachable when flow is nearly all intrinsic), and 73% of the net is a stale 08-13→08-21 cluster during which the stock was flat. An unmeasurable input is not evidence either way.
- **ADBE / ORCL** — SKIP on the merits (see §5). **Recording an orchestrator-side funnel gap:** both were initially absent from the C12 pass list because that list was built from the *flow screeners* only, so liquid names reporting soon that did not light up today's options tape were excluded **by construction**. Verified directly: **ADBE $1.19B ADV, ORCL $3.38B ADV** — both clear C12 comfortably. The substantive verdict is unchanged, but the funnel should draw from `earnings_catalyst` as well as the flow screens.
- **MSFT** — bullish sweep persistence 3/5 contradicted by today's −$24.5M; **also an adverse-flow exit candidate** from yesterday's group. Its 30d (+$784.8M) sits inside a 90d of only +$71.1M, i.e. days 31–90 were net **−$713.7M** — a recent burst, not durable accretion. Its dividend-payer ex-div intent screen was **not evaluated by any agent**, so its +1 carries an unverified leg.
- **ECHO / LMT / BE** — Tier-1 `FLOOR_PUT_BLOCK` whales and BE's multi-strike IV-outlier put cluster. The whale-plus-crowding co-flag **fails on all three** (pc-ratio z NORMAL). Advisory, permanently 0 points.
- Also surfaced, sub-threshold: MRVL (**not present in `dark-pool block-stratified`'s top-30 at all**, so institutional tier is unconfirmable by the required tool), IREN, AMAT, MSTR, DRAM, EWY, ALAB, APP, AMZN, **PLTR** (HEDGED_LONG → excluded by the offsetting-hedge rule), U, DVN, CME, EFX, LYV, SIRI, DOW, FSLY.
- **`fz` RS tanker/midstream new-high cluster** (FRO, INSW, DHT, NAT — LPG and CMBT failed C12): no options-flow corroboration, no netted sector read. Appendix only.

---

### Run notes
- **Fleet:** 10 Phase 1 agents spawned. *The command header says "11 Phase 1 agents" but its own enumerated list contains 10 non-conditional agents plus the conditional `opex-pin-strategist`; 2026-09-18 is 14 days out, so OPEX was correctly not spawned. The header count is off by one against its own list.*
- **`fz` health:** available (v1.0.0). All `fz` lanes advisory, 0 rubric points. **The doubled-first-letter ticker defect re-confirmed on every bulk `fz screen` row** (TTARS=TARS, AAI=AI, AABEO=ABEO); per-ticker `fz_enrich` healthy.
- **C12 liquidity floor:** applied with `--as-of 2026-09-04`, fail-closed. 83 of 94 funnel names passed; 11 dropped (SHOO $39.0M, TLYS $4.40, ZURA $9.5M, AVNT $34.8M, CRK $38.1M, ACAD $43.3M, CLDX $29.9M, NN $46.9M, BRBR $31.4M, LPG $26.1M, CMBT $19.9M).
- **Step-0 cache:** 22 market-wide payloads fetched once; no agent re-fetched a cached payload.
- **Substrate defects that fired live today:** QQQ GEX regime-label inversion; `gex-time-series` ZGL corruption; `oi-trend` `consecutive_build_days` censoring (4-of-4, plus IREN 103-vs-10); `sector-flow-persistence` zero discrimination (9 of 11 sectors); `iv-rank --mode high` saturation (25 of 25 at 100); `analyst-vs-flow` zero analyst rows; `earnings-catalyst.implied_move_perc` pre-event tenor (0.39% vs a re-derived ~8.3%); raw IV term-structure mislabeling (13 of 18 flipped after hygiene); `fz` doubled-ticker.
- **Defect that did NOT fire:** `portfolio-correlation` was **reproducible today** (max deviation 0.015 vs self-computed log-return correlations). The documented degenerate mode is **intermittent, not permanent** — verify per session rather than assuming either state.
