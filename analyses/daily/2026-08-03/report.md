# Daily Market Analysis — 2026-08-03

## Executive Summary

- **Regime + GEX state:** `uw` label **TRANSITIONAL** (trend UPTREND). SPY 757.67 **+1.42%**, above 20SMA (746.01) and 50SMA (745.32), −0.36% from the 90d high. QQQ +1.76%, IWM +1.72%, RSP +0.98% — a genuinely **broad** rally, 67.6% of the S&P green (340 adv / 163 dec). **VIX 15.86, −15.05% over five sessions.** Both SPY and QQQ flipped into **long gamma** (SPY +$1.286B, QQQ +$774.4M) — but SPY's flip is 2 sessions old and QQQ's is **1 session old**, after a month of FULLY_NEGATIVE whipsaw. Sector lean: netted Technology +$217.4M / Comm Svcs +$138.0M / Consumer Cyclical +$76.9M in; Healthcare −$36.5M out. **Two divergences carry the day: (i) price breadth 67.6% green against `uw` options-FLOW breadth of only 40% bullish, and (ii) semis LAGGED the tech tape (SMH +0.91% / SOXX +0.55% vs XLK +1.53%, both NEGATIVE on 5d).**
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`. Freeze-lift structurally unrunnable for a 7th consecutive cycle (354 post-freeze resolved calls, **zero HIGH or MEDIUM ever emitted**).
- **Next-session GEX (SPY/QQQ):** **SPY** — long-gamma, ZGL **756.06** (reliable, 0.25% below spot), call wall **758** (effectively *at* spot), put wall **735**; iron fly / tight-body condor ~758. **QQQ** — long-gamma, ZGL **699.22** (reliable), call wall **701**, put wall **680**, with **+$434.7M of gamma piled on the 700 strike** — the biggest single print on the grid. Both flips are provisional; size QQQ smaller. Advisory, see §2.
- **Top swing build:** **NONE.** The board is empty for the **20th consecutive session**. The only name to clear the confluence gate at LOW tier — **SNDK (raw 4)** — was gated to `skip` by four independent fires (front-end panic 1.548 · fundamentals CAUTION on insider MSPR −100 · own earnings **T+2** with a **13.88% implied move** · debate lost 0.45 vs 0.65).
- **Top LEAP candidate:** **NONE.** `leap-positioning-radar` passed exactly one name at a marginal 6-of-9 (**CRWV**), self-demoted it to "LOW-tier input", and it then scored raw 2 → DROP. NVDA had the cleanest fresh ask-dominant LEAP build on the tape and was **disqualified on 90d cum-flow of −$188.7M**.
- **Biggest risk:** **`AI_semis_cluster` = {SNDK, CRWV, NBIS, SMH}** — four of six candidates are one 0.71–0.89-correlated AI-infrastructure bet. Nothing is sized, so no hedge is mechanically required; the standing advisory is cheap index wings into NFP (T+4) / CPI (T+7). The regime tell: `multileg-strategist` found a systematic desk building an **escalating SPY crash-convexity put-fly ladder** (~$66M debit, 4 expiries, scaled 100k→150k over 3 sessions, bodies 30–34% OTM) plus two sessions of IWM downside buying into NFP.

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** `TRANSITIONAL — Mixed signals, reduce position size, wait for clarity`. Trend **UPTREND**. SPY 757.67, above both the 20SMA (746.01) and 50SMA (745.32), +1.73% over 30d, −0.36% from the 90d high. Guidance: *"Half position sizes. Favor defined-risk strategies. Iron condors in range."*

**The breadth story is inverted from the usual, and it is the most important read of the day.** Two independent breadth measures disagree in direction:

| Source | Measure | Reading |
|---|---|---|
| `uw risk market-regime` | **options-flow** breadth | **40% bullish** — 2,514 bullish-flow vs **3,770 bearish-flow** tickers (of 6,284) |
| `fz breadth --group sector` (advisory) | **price** breadth | **67.59% green** — 340 advancers / 163 decliners, avg +1.04%, median +0.81% |

Price is broadly green; the options tape is not confirming it. Top mover FSLR +10.28%, worst MAR −6.97%. This is the opposite of the usual "green index, narrow breadth" distribution tell — here participation is *wide* and the derivatives market is the sceptic. Advisory, 0 rubric points, and it does not override the `uw` regime label — but it is the frame for everything below.

**Tape framing** (raw Yahoo chart API, `--as-of 2026-08-03`):

| Symbol | Close | 1d | 5d | rv20 | 20d $ADV |
|---|---|---|---|---|---|
| SPY | 757.67 | +1.42% | +2.51% | 13.0 | $35.8B |
| QQQ | 700.07 | +1.76% | +2.63% | 23.5 | $28.4B |
| IWM | 296.22 | +1.72% | +1.13% | 14.5 | $6.4B |
| RSP (equal-weight) | 217.11 | +0.98% | +0.90% | 10.2 | $1.9B |
| XLC | 111.34 | **+2.86%** | **+3.42%** | 24.7 | $709M |
| XLI | 183.16 | +1.85% | −0.02% | 17.7 | $1.2B |
| XLY | 118.21 | +1.83% | **+6.65%** | 25.7 | $979M |
| XLK | 178.04 | +1.53% | +2.15% | 31.9 | $1.6B |
| **SMH** | 545.46 | **+0.91%** | **−0.56%** | 48.2 | $7.3B |
| **SOXX** | 507.68 | **+0.55%** | **−1.66%** | 58.1 | $5.7B |
| XLV | 162.24 | −0.19% | −0.71% | 18.4 | $1.5B |
| XLP | 84.86 | −0.22% | −0.59% | 19.5 | $963M |
| XLE | 58.79 | **−1.28%** | +0.74% | 21.1 | $1.7B |
| ^VIX | 15.86 | −0.81% | **−15.05%** | — | n/a |

IWM (+1.72%) ≈ QQQ (+1.76%) and RSP is green — this is not a narrow mega-cap tape. But **semis materially lagged**: SMH and SOXX both underperformed XLK and are **negative on the week** while carrying enormous realised vol (rv20 48.2 / 58.1). A tech rally that semis do not lead is a different animal from the AI-complex tapes of July, and it is the single most consequential distinction in today's data.

**Per-index gamma (current-state EOD book):**

| Index | Spot | Zero-gamma | ZGL reliable | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|---|
| SPY | 757.93 | 756.06 | ✅ (0.25% below spot) | **+$1.286B** | long-gamma / POSITIVE | **758** (+$240.8M) · 760 (+$228.2M) | **735** (−$56.1M) · 740 |
| QQQ | 700.19 | 699.22 | ✅ (0.14% below spot) | **+$774.4M** | long-gamma / POSITIVE | **701** (+$61.9M) · 710 | **680** (−$52.5M) · 685 |
| IWM | 296.22 | — | ❌ | — | **unstable** | — | — |

IWM's ZGL alternates POSITIVE/FULLY_NEGATIVE nearly every session across the 10-day window (07-21 POS, 07-22 FULLY_NEG, 07-23 POS, 07-24 POS, 07-27 FULLY_NEG, 07-28 FULLY_NEG, 07-29 FULLY_NEG, 07-30 POS, 07-31 FULLY_NEG, 08-03 POS). This is the known **ZGL-grid instability artifact**, not a tradeable trajectory — reported as unusable rather than quoted.

**`uw options-flow dte-volume-share` (MARKET-level only):** 0DTE **35.6%** · weeklies 24.7% · monthlies 19.5% · LEAPs **3.6%** → `regime_hint: BALANCED`. Neither a retail-0DTE-dominated tape nor a heavy institutional-positioning tape, so no uniform benefit-of-the-doubt and no uniform downgrade applies. The 3.6% LEAP share is context for §4's near-empty output.

**`uw historical vrp`:** SPY IV30 0.127 vs realised30 0.1325 → **vrp −0.0055, FAIR**. QQQ IV30 0.2168 vs realised30 0.253 → **vrp −0.0361, FAIR**. *"IV close to realised — no clear edge from VRP alone."* Both marginally negative: this is **not** a premium-selling tape and not clearly a premium-buying one. Do not lean on VRP in either direction today.

**Macro backdrop** (`scripts/fred_macro.py`, `available: true`): yield curve **normal, 10Y−2Y +0.45** · core CPI **2.81% YoY** (headline 3.73%) · core PCE **3.29% YoY** (headline 3.67%) · unemployment **4.2%** · payrolls **+57k** MoM · 10Y **4.75%, RISING** (+27bp over 30d, from 4.48) · 2Y 4.28% (+11bp) · broad USD **weakening** (−1.44 index pts/30d) · fed funds **3.63%** · SOFR 3.66%.

**Read:** core PCE at 3.29% sits well above target while the 10Y backs up 27bp in a month against a 3.63% policy rate. That is a rising-real-rate, sticky-core backdrop under a weakening dollar — a direct cost-of-capital drag on long-duration, high-multiple equity that today's flow tape does not price. It bears specifically on CRWV (beta 7.41) and NBIS (operative beta 4.44).

**Forward event risk (Tier-1, next ~10 trading days):**

| Date | Event | Impact | Trading days out |
|---|---|---|---|
| 2026-08-06 Thu | Weekly jobless claims | LOW | 3 |
| **2026-08-07 Fri** | **Employment Situation / NFP (July), 8:30 ET** | **HIGH** | **4** |
| **2026-08-12 Wed** | **CPI (July)** | **HIGH** | **7** |
| 2026-08-13 Thu | PPI (July) | MEDIUM | 8 |
| 2026-08-14 Fri | Retail sales (July) | MEDIUM | 9 |
| 2026-08-19 Wed | FOMC minutes (Jul 28–29) | MEDIUM | 12 |

**No FOMC meeting in August** — next is September. Every 1–6 week swing thesis carries NFP *and* CPI inside its horizon. Name-specific prints stack on top: **MCD 08-04 (T+1)**, **SNDK 08-05 (T+2)**, CRWV 08-11 (T+6), **NBIS 08-12 (T+7, on CPI day)**.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — built from open interest that persists overnight — read forward as the *prior* for the 2026-08-04 open. It is **prose-only, contributes 0 points** to the conviction rubric, and makes **no backtested predictive claim**. Predictive validation lives in `/weekly-analysis`'s rolling §2 backtest, not here. Scope is **SPY and QQQ only**.

### SPY
`spot 757.93 · ZGL 756.06 (reliable) · POSITIVE / long-gamma · total_gex +$1.286B · call wall 758 (+$240.8M), secondary 760 (+$228.2M) · put wall 735 (−$56.1M), secondary 740 · distance to call wall +0.01%, to put wall −3.02%`

**Read:** Dealers are net long gamma with the ZGL sitting almost exactly at spot and a wall of positive gamma piled at 758–760 — the classic mean-reversion / pin configuration into the open. But the regime **flipped only on 2026-07-31** (from FULLY_NEGATIVE, which had held since 07-17), following a whipsaw month with flips on 07-10, 07-21 and 07-31. Treat the pin as **provisional, not entrenched**. The put wall at 735 (−3.0%) is the nearest real support shelf if the pin breaks.

**Structure bias:** walls tight around spot with real air to 760/765 — iron fly or tight-body iron condor centred ~758, shorts near 755/761. Avoid naked strikes beyond 760 given the freshness of the flip.

### QQQ
`spot 700.19 · ZGL 699.22 (reliable) · POSITIVE / long-gamma · total_gex +$774.4M · call wall 701 (+$61.9M), secondary 710 · put wall 680 (−$52.5M), secondary 685 · distance to call wall +0.12%, to put wall −2.88%`

**Read:** QQQ flipped from FULLY_NEGATIVE into POSITIVE gamma **today**, on the +1.76% rally — a **one-session-old, unconfirmed** regime after weeks of negative gamma. The 700 strike carries **+$434.7M, the single biggest print on the entire grid**, a strong magnet just below spot. This is the freshest and least-tested of the two flips; a 1-day-old regime after a month of whipsaw is exactly what gets round-tripped by the first bad print. Read with more scepticism than SPY.

**Structure bias:** butterfly / iron fly body straddling 700–701 rather than a wide condor. **Size smaller than the SPY structure**, keep wings tighter — the put side's real support at 680 is 2.9% away, a big gap to lean on for a same-day structure.

**Mandatory caveats:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes of 08-04 and re-computes the ZGL and walls.
- **ZGL reliability.** Both sit within ~0.3% of spot — reliable by the 5% rule — but SPY's regime is 2 sessions old and QQQ's is 1, both after a month of whipsaw. Neither is "held" in the multi-session sense.
- **Gap risk voids the prior.** No Tier-1 event before tomorrow's open (NFP is T+4), but a gap through either wall invalidates the pin read entirely.
- **Tooling limit.** `uw-pp` cannot isolate the D+1 expiry (`gex --dte-max 1` errors). This is the standing **0–45 DTE** book — the best available proxy, not the isolated next-session expiry.
- **ETF book**, not the cleaner SPX/NDX index book — ETF OI is fragmented across more strikes and expiries and is structurally noisier.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — the validated stack)

The GEX walls above are a **map, not a pin** — wall-as-magnet backtested NO_GO, as did every directional 0DTE signal. What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, and **not a guaranteed edge**: the validation sample contains no vol shock, so the short-vol left tail is **unsampled**.

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` / VIX | **LOW** / 15.86 | **LOW** / 15.86 |
| `implied_move_pct` | 0.63% | 1.39% |
| `expected_range_pct` | 0.80% | 1.41% |
| `size_scalar` | 0.5 | 0.5 |
| `suggested_structure` | iron fly / short straddle centred **758.0**, wings ≈ ±0.8% | body straddling 700–701, wings ≈ ±1.41% |
| `stand_aside_reason` / `caution` | none | none |
| Backtest (n=60) win rate | 90.0% | 85.0% |
| **mean PnL gross** | **+0.239%** of spot notional | **+0.369%** |
| **mean PnL NET** (after 0.1% round-trip) | **+0.139%** | **+0.269%** |
| worst day (open entry) | −1.40% | −2.453% |
| overnight entry | +0.036% | **−0.085%** |
| `verdict` | GO_PREMIUM_SELL_INTRADAY | GO_PREMIUM_SELL_INTRADAY |

**Lead with the net number, on its real basis.** `pnl_basis` is **percent-of-underlying-spot-notional, GROSS** — not premium-collected and not margin-relative. Net of an assumed 0.1% round-trip, SPY's edge is **+0.139%** of spot notional per day. That is tiny in absolute terms, and Vilkov (2024) found an unconditional 0DTE condor flips to negative net Sharpe once costs are charged — the 90% gross win rate materially overstates a negatively-skewed seller's edge.

**Critically, both indices are in the `LOW` vol state — the thin-edge bucket.** SPY's mean PnL by VIX state is LOW **0.014** / MID 0.368 / HIGH 0.335; QQQ LOW **0.018** / MID 0.574 / HIGH 0.516. At VIX 15.86 after a −15% five-session crush, this setup is sitting in the one tercile where the historical edge is ~nil. **Size at the 0.5 scalar or stand aside**; the `sell_premium: true` flag is not an instruction to press.

**Entry rule:** enter at/after the open once the overnight gap resolves; if it gaps beyond the wings, stand aside. Hold the 0DTE to the close — **never carry overnight** (QQQ's overnight expectancy is negative). Direction: **none** — delta-neutral, do not add a tilt. **SPY ≈ SPX** (validated identical); **QQQ is the weaker of the two** — flag its lower confidence.

**Promotion bar:** this lane stays advisory / 0 rubric points **permanently** until both a vol-shock day enters the sample and **net** expectancy clears a tail-aware bar. Win rate is explicitly not the promotion metric.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

> Framing (2026-06-12 P0.4): the "DEX flips precede price moves" thesis (Karsan / SqueezeMetrics) is **practitioner hypothesis, not validated evidence** — hedging pressure is intraday-mean-reverting (Baltussen et al. 2021), and a positive DEX *level* in an up-tape is beta, not edge (`dealer_positioning` ran −7pp excess in the 2026-05-30 audit; +3.7pp, p=1.000, n=27 in the 2026-08-01 audit — indistinguishable from beta). **Only the mechanized sign-change trigger computed by `scripts/dex_flip.py` feeds the scored line.**

**Qualifying mechanized DEX flips — the only names eligible for the +1 line:**

| Symbol | Direction | Ratio | Whipsaw | Evidence |
|---|---|---|---|---|
| **QQQ** | LONG | **1.89×** | none (1 sign change / 12d) | `net_dex 07-31 −6,258,341,456 → 08-03 +16,010,796,835`; prior 11 sessions all negative; \|flip\| 16.0B vs floor 8.48B (0.25× trailing-10 median 33.9B). Independently corroborated by GEX flipping FULLY_NEGATIVE → POSITIVE the same session. |
| **TSLA** | LONG | **1.43×** | none | `net_dex 07-31 −400,174,029 → 08-03 +1,325,962,943`; prior 11 sessions all negative; \|flip\| 1.33B vs floor 0.93B (median 3.71B). ⚠ front-end IV@7dte **1.466 BACKWARDATION** (near 71.8% vs far 49.0%) — unresolved event risk a pure dealer read cannot see. Vanna leg marginal (net_vanna +33, essentially balanced) — do not lean on it. |
| **FSLR** | LONG | **6.01×** (largest) | none | `net_dex 07-31 −56,310,922 → 08-03 +162,983,744`; prior 11 sessions all negative; \|flip\| 163M vs floor 27.1M (median 108.5M). Same-day GEX regime-flip confirmation (`{date: 2026-08-03, NEGATIVE→POSITIVE, ZGL 135.02}`). ⚠ **options book thin** — every per-strike value under $250M. |

**Did NOT qualify:** SPY (flipped 07-31, two sessions ago — already in the tape, beta not edge) · **IWM** (sign change present but magnitude **1.08B < 1.76B floor** — precisely the whipsaw-around-zero case the floor exists to kill) · **COHR** (0.92× — closest near-miss, re-check 08-04) · INTC (flipped 07-30, holding 3 sessions) · **MU** (`whipsaw_warning TRUE`, **4 sign changes**) · ACLS (whipsaw TRUE, noise-level book).

**Vanna-squeeze flags TRUE** (put-heavy book + dated falling VIX — 07-30 17.09 → 07-31 15.99 → 08-03 15.86, three consecutive falling closes): **SNDK, ASML, INTC, MU** (with caution — its DEX whipsaws against it), **TSLA** (marginal).

**None of the three qualifying flips cleared the Step-3 confluence gate** — each was flagged by `dealer-positioning-strategist` alone. They live in §8, not the conviction book. That is the gate working as designed, but it is worth stating plainly: the day's cleanest mechanized signal earned no position.

Triaged snapshot-only (no flip candidacy, all showing continuation of an existing call-heavy posture): NVDA (+8.18B), AMZN (+12.73B), GOOGL (+6.54B), AMD (+3.35B), META (+3.25B), ORCL (+1.50B), AVGO (+0.81B), NOW, RDDT, DELL, OKTA, INTU, MPWR, LITE.

---

## 2b. Sector Rotation

**Rotation regime call: `no_change`** (`regime_confidence: low`).

Only **Technology** survives every gate. The raw netted labels (Discretionary in; Staples / Healthcare / Utilities out) superficially resemble **defensive→cyclical**, but scrutiny kills every leg except Technology — flagged explicitly so the risk layer is not blindsided if the pattern re-emerges with real persistence.

> **Direction reads off the NETTED source only.** `uw risk market-regime.sector_rotation` is the sole netted source and the only thing that can express direction. `sector-flow` and `sector-flow-persistence` are **one gross-turnover source** (call$ − put$, sign-agnostic, values identical to the dollar) — a durability filter, not a direction. **Netted-vs-gross disagreement ⇒ `watch_only` (C55).**

| Sector | Netted $ | Gross $ | Persistence | Trend | Price (1d/5d) | Verdict |
|---|---|---|---|---|---|---|
| Technology | **+$217.4M IN** | +$4.80B | **1.00** | INFLOW | XLK +1.53% / +2.15% | **rotating_in** (high conviction) |
| Communication Services | +$138.0M IN | +$1.23B | 0.80 | INFLOW | XLC +2.86% / +3.42% | watch_only — agrees, but outside top-third persistence tier |
| Consumer Cyclical | +$76.9M IN | +$1.49B | 0.60 | **ROTATING** | XLY +1.83% / +6.65% | watch_only — 3 negative days then a 2-day reversal, fails the ≥3-day-current-direction rule |
| Financial Services | — | +$224.6M | 1.00 | INFLOW | XLF +0.77% / +0.88% | no_call (no netted direction) |
| Industrials | — | +$200.5M | 0.60 | ROTATING | XLI +1.85% / −0.02% | no_call |
| **Healthcare** | **−$36.5M OUT** | **+$173.0M** | 1.00 | INFLOW | XLV −0.19% / −0.71% | **watch_only — DISAGREE** |
| **Consumer Defensive** | **−$4.1M OUT** | **+$54.6M** | 1.00 | INFLOW | XLP −0.22% / −0.59% | **watch_only — DISAGREE** |
| Energy | — | +$34.0M | 1.00 | INFLOW | XLE −1.28% / +0.74% | no_call |
| Basic Materials | — | +$14.1M | 1.00 | INFLOW | XLB +1.15% / −0.74% | no_call |
| Real Estate | — | +$7.3M | 0.60 | ROTATING | XLRE +0.24% / −1.27% | no_call |
| Utilities | −$0.8M OUT | −$15.9M | 0.80 | OUTFLOW | XLU +0.02% / −2.89% | watch_only — agrees but noise-level |

**Two netted-vs-gross disagreements, not one.** Healthcare was flagged in preflight; **Consumer Defensive was found independently by the agent** and is new — both show gross INFLOW with persistence 1.00 against a netted OUTFLOW, and both are forced to `watch_only` under C55.

**The load-bearing catch.** Technology is the one clean rotation-in, but three of the five biggest single-day Technology bullish prints sit on **negative 30-day cumulative flow**:

| Ticker | Sector persistence | cum_flow_30d | 30d direction | ≥$50M | Conditional +1? |
|---|---|---|---|---|---|
| **SNDK** | 1.00 | **+$928.3M** | aligned | ✅ | **YES — the only name passing all three gates** |
| NVDA | 1.00 | +$35.3M | aligned | ❌ ($35.3M < $50M) | No — magnitude bar fails |
| AMD | 1.00 | **−$117.2M** | **misaligned** | ✅ | **No — flow_conflict** |
| ORCL | 1.00 | **−$173.9M** | **misaligned** | ✅ | **No — flow_conflict** |
| MU | 1.00 | −$41.9M | misaligned | ❌ | No |

Today's Technology print on AMD, ORCL and MU is a **counter-trend bounce inside a month-long distributive pattern** — the same flow_conflict pattern that has killed prior fleet calls. Only SNDK is the exception.

**ETF flow tape (advisory — instrument-level layer the GICS aggregates cannot see; 0 new rubric points):**

| ETF | Net premium (5d) | Persistence | DP positioning | Options urgency | GICS agreement | Leaders |
|---|---|---|---|---|---|---|
| **SMH** | **+$101.3M** | BULLISH | $217.4M DP, **70% below-mid** (two-way/hedging-heavy) | call-skewed $66.8M vs $53.8M put; **ask-side call $25.3M > ask-side put $11.5M** | **agree** → Technology | see §3 |
| XLY | +$5.4M | BULLISH | $79.8M DP, 85% below-mid | 3 sweeps, all call ($6.2M), thin | agree (sector itself watch_only) | AMZN, TSLA |
| **IGV** | +$5.4M | BULLISH | $87.5M DP, **60% above-mid** (aggressive buy-side) | call-skewed $4.9M vs $1.6M; ask-side call $3.3M dominant | **agree** → Technology | — |
| XBI | +$3.9M | BULLISH | rank-only | rank-only | n/a (no netted Healthcare call) | — |
| XLE / XLK | +$2.4M / +$2.2M | MIXED | rank-only | rank-only | weak | — |
| KRE | −$2.0M | BEARISH | rank-only | rank-only | n/a | — |
| XLI | −$2.2M | BEARISH | rank-only | rank-only | n/a | — |
| EWY | −$3.4M | MIXED | $158.7M DP, 58% above-mid | put-heavy total ($30.0M vs $22.1M) but **ask-side call-dominant** ($7.0M vs $2.9M) | n/a (Korea) | — |
| **XOP** | **−$6.3M** | BEARISH | $20.4M DP, **96% below-mid** (heavy sell pressure) | **overwhelmingly put: $19.6M vs $0.56M call; ask-side put $15.1M** | n/a | — |
| **GDX** | **−$14.9M** | BEARISH | $20.8M DP, 90% above-mid (**contradicts** its own bearish 5d label) | still call-skewed today | n/a — thin/noisy, not tradeable | — |

**SMH and IGV are the two most net-bullish ETFs in the entire 21-ETF universe on options flow — while SMH/SOXX price LAGGED and are negative on 5d.** That flow/price divergence is genuine and is carried forward, not used to downgrade the Technology call. Note also the **intra-Energy split**: XLE (mega-cap) is flat/mixed while **XOP (E&P) is aggressively bearish** with 96% below-mid DP and $15.1M of ask-side put buying — a sub-sector story, not a sector-wide call.

**Swing-book implication:** the only sector-derived long candidate is **SNDK**; treat AMD/ORCL/MU bullish prints as counter-trend bounces inside 30d distribution and do not size off today's flow alone. No sized short candidates from the sector layer.

---

## 3. Swing Setups (1–6 weeks)

**Post-gate book: EMPTY. Zero sized positions — the 20th consecutive empty board.**

### 3a. Long swings (regime-aligned)

| Ticker | Score | Tier | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|---|
| **SNDK** | **4** | LOW | Only name clearing all three sector-leader gates: Technology netted+gross agree with persistence 1.00, `cum_flow_30d` **+$928.3M** (7.4× union median, 1.75% of $53.16B gross), 90d **+$2.62B** — a quarter of sustained accretion, not a recency artifact. Vanna-squeeze TRUE on a put-heavy book into three falling VIX closes. Vol BACKWARDATION, front-end 1.548, vrp_proxy −20.6 (BUY-cheap). Fundamentals genuinely strong: 4/4 beat streak, rev +82.76% YoY, gross margin 56.0%, D/E 0.20. | *(would have been)* starter long equity / call spread | Close below **$1,214.83** (07-31 swing low, −5.7%) or post-print DEX sign-flip negative. No DP level available — price-swing fallback. | **skip** |
| GOOGL | 2 | DROP | 5-aligned dark-pool accumulation that **survived the closing-cross filter** where AAPL/MSFT/META/AVGO/SOFI/PCG did not; institutional-accumulation ACCUMULATION (1.76 b/s), OI BUILDING 5/5. Fundamentals CONFIRM with insider **buying** (MSPR +30.83). | — | Close below the **$368.42 DP shelf** (C34; defended level $373.51, resistance $375.28) | **skip** |
| NBIS | 1 | DROP | `sweep-tracker`'s #1 conviction name — 5/5 persistence, $970M cumulative sweep premium, call-ask > put-ask. 30% short float on a tight 202M float. Institutions net-adding +15.49%. | — | No DP level — fallback: net-DEX sign-flip negative on 2 consecutive sessions, or 30d cum-flow turning net-bearish | **skip** |

**Why SNDK died** — four gates fired independently on the day's best score:
1. **panic** — `front-end-iv-ratio` **1.548** at near-dte 4 (>1.10). Earnings-hump elevation rather than systemic panic, but the gate is mechanical.
2. **fundamentals CAUTION** — insider **MSPR −100.0, every single month since 2025-07**, into the print.
3. **event_risk** — **own earnings 2026-08-05 = T+2**, with a **13.88% implied move** (178.92 points on a $1,288.03 stock — the largest liquid implied move in the whole batch). A directional long is not the event play and is undefined-risk through the gap. NFP at T+4 stacks on top.
4. **debate** — bear 0.65 ≥ bull 0.45. The unrefuted point: *"every flow/vanna/vol-surface signal in this stack describes pre-earnings dealer **positioning**, not the print's **outcome** — a binary gap can overwrite the entire thesis in one session."* The bear additionally argued the vanna leg and the vol leg are **the same elevated-near-dated-IV fact counted twice**, which `dealer-positioning-strategist` itself supports: *"the 210% near-dated IV is well outside normal dealer-hedging territory — likely event risk dominates this name's book; the vanna-squeeze mechanics are SECONDARY to that catalyst."*

**Revisit SNDK after the 08-05 print.** If the accretion thesis is real, post-print flow will re-confirm it at far better information and without the binary.

**Distribution cautions (C28, advisory — 0 points, no sizing impact):**
- **GOOGL** ⚠ `GOOGL260821C00350000` (Aug21 $350C) OI **−2,410 on $7.6M closing premium** — the largest single OI decrease in the entire GOOGL chain today, well above the institutional floor; also 270617C320 −647/$7.7M, 270115C300 −468/$7.7M, 260821C365 −643/$1.89M. Accumulation-hunter: *"Puts are NOT the driver here — this is a genuine call-side distribution tell."* Sitting on top of a **+11.9% three-session run** ($333.66 → $356.13 → $373.51), this reads as distribution into strength.
- **NBIS** ⚠ `NBIS260807C150` OI **−1,095 / $13.5M**, a deep-ITM winner close (strike $150 vs spot $212.77); call-side decreases **$19.0M vs $2.8M put**.

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only` (2026-08-01 audit P0 #1).** This is **routing, not suppression** — the thesis is generated, scored, gated and serialized so the counterfactual keeps resolving for `/calibration-audit`. Short legs inside defined-risk spreads and short-vol structures are unaffected.

| Ticker | Score | Direction | Thesis | Invalidation | Sizing |
|---|---|---|---|---|---|
| **SMH** | **−3** | short | The tape agrees with the bear read — semis did not lead a tech rally (SMH −0.56% / SOXX −1.66% on 5d vs XLK +2.15%) and `sweep-tracker` flagged it bearish at 3/5 persistence on $671M. Term-skew **TAIL_HEDGING** (+0.061) clusters with UCTT and SOXX, and a **SMH put-510 IV outlier** (avg 3.9% / max 59.3%) reads as tail-hedge accumulation. **But the premium tape disagrees violently**: `cum_flow_30d` **+$184.4M bullish at 1.47× union median** ⇒ mechanical **−3 flow_conflict**, and SMH is the #1 most net-bullish ETF in the 21-ETF universe. | 30d cum-flow staying net-bullish plus two consecutive closes above the 08-03 high; confirms if 5d semis underperformance extends while netted Tech flow flips negative | **watch_only** |

**Note the uncomfortable fact:** SMH carries the **only positive market_excess in today's entire book** (`bearish_flow` clean WR **0.5804, n=143, excess +8.4pp`) and it sits on the side the system is barred from sizing. That is exactly the counterfactual the routing rule exists to preserve — the 2026-08-01 paired McNemar found the short book runs **−13.0pp in up-tape and −14.1pp in down-tape** against a naive index short, near-identical in both, which is mis-selection rather than mistiming. The class quote also lands in the **[0.55, 0.65) anti-predictive band** (realised ~0.29 on decided rows), so it is disclosure only, not upgrade-eligible.

**Contrarian lane: EMPTY, and the reason is instructive.** `contrarian-scanner` tested 32 C12-funnel names. Four hit ±2σ — HD (BEARISH_EXTREME z=3.08), XOP (BEARISH_EXTREME z=18.1, likely a thin-liquidity artifact), ASML (BULLISH_EXTREME z=−2.09), ABT (BULLISH_EXTREME z=−2.14). **The −2 "overcrowded long, VRP positive" line was applied to no name**: the two right-polarity (BULLISH_EXTREME) names both carry **negative** per-name VRP (ASML −0.0088, ABT −0.0728), while the two with positive VRP are the wrong polarity. **Tool limitation confirmed empirically: `uw historical pc-ratio-zscore` has no `--date` flag**, so "rising" cannot be asserted for any name — `pc_z_trajectory: UNAVAILABLE` throughout. ABT was the best-evidenced divergence (price +22% vs net flow −$13.97M, P/C 0.0501 vs mean 0.655) and was killed by three independent switches: negative VRP, genuine BACKWARDATION surviving hygiene (front-end 1.72), and the Healthcare netted-vs-gross disagreement.

**Sweep tape (informational — the sweep-persistence line earns 0 rubric points, removed 2026-05-23 P0.3 on −22pp marginal contribution across two audits):**

Clean ≥3-of-5 persistence reads: **NBIS** (5/5, $970M, bullish, best non-mega-cap read), **AMZN** (5/5, $2.98B, bullish, cleanest mega-cap — passes the cum-flow alignment screen), **GOOGL** (3/5, $674M, bullish but paired-strike/possible spread), **SMH** (3/5, $671M, bearish, coherent with the weak semis tape).

**Artifact / do-not-trade list:**
- **SPX / SPXW** — symmetric matched-strike call+put sweeps across four expiries (7000/8000, 4200/4250, Sep'26–Dec'27) = an institutional collar / hedge-roll, zero directional information.
- **SPY / QQQ / IWM** — balanced 0DTE call ladders (ask ≈ bid at every adjacent strike) plus deep-OTM tail-hedge puts (SPY 620P/500P Nov'26; IWM 282P/175P/120P Dec'18). SPY/QQQ technically pass the cum-flow alignment check but the margin is <0.2% of gross — inside noise.
- **NVDA** — tagged bearish 5/5 ($3.5B) but `cum_flow_30d` is net **bullish** (+$35.3M); today's largest line is a near-balanced 0DTE ATM call (ask 287,203 vs bid 250,519) = market-maker churn.
- **AAPL** — tagged bearish 5/5 but today's tape shows **more call-buying dollars than put-buying dollars**; tag and tape disagree.
- **MU** — largest single-name cumulative premium ($5.6B) but the granular tape is balanced two-sided 0DTE churn at every strike and 30d cum-flow is dead flat (−0.10%). Very likely 0DTE MM noise wearing a "bearish 5/5" label.
- **MSFT, META** — `dominant_direction: mixed` per the tool itself; disqualified regardless of premium size.
- **BE, SPCX, SOXL** — surfaced by the raw scans but **not in the C12-floored funnel**; dropped fail-closed. SPCX additionally shows a tag/tape conflict (tagged bullish 5/5, granular tape actually put-heavy ~$27M).

**Institutional multi-leg structures — three found, all defined-risk, none a directional short.** These are the most informative flow on the tape today and **none cleared the confluence gate** (each was surfaced by `multileg-strategist` alone), so none earned the +2 line:

1. **SPY deep-OTM put butterfly LADDER (rank 1, highest conviction on the board).** 1:2:1 replicated across four expiries and **escalating over three sessions**: 07-28 Sep18 P625/525/425 (100k/200k/100k) → 07-31 Sep30 P635/535/435 (150k/300k/150k, $0.99) → 07-31 Oct16 P625/525/425 ($1.13) → **08-03 Nov20 P620/500/380 (150k/300k/150k, $1.69)**. Net debit today ≈**$25.4M**, program ≈**$66M**; max payoff 120 wide × 150,000 × 100 = **$1.8B** (~71:1). **100% opening** (`oi_diff_plain` ≈ `volume` on every leg — Oct16 P525: 300,092 vs 300,138). Ask-side confirmed: `SPY261120P00380000` **ask 150,054 / bid 33, ratio 4,547**. Hand-negotiated: 42 trades on 300,233 volume (7,148 contracts/trade) into a pre-trade OI of 397. The cleaned curve is **CONTANGO and strengthening** (11.5%@d2 → 17.7%@d46 / 18.0%@d58 / 17.3%@d74 / 19.1%@d109) — a butterfly nets to ≈zero vega, so it buys deep crash convexity **without paying the contango**, which a long put or put calendar could not. Bodies at 500–535 are **−30% to −34% from spot**, so NFP and CPI are irrelevant to the payoff, and the whole structure sits outside the dealer gamma grid (733+). **Zero artifact flags.** Read: a systematic desk paying up for tail insurance into a VIX-15.86 tape that just crushed −15% in five sessions — **a regime signal, not a trade to copy, and explicitly NOT a directional short.**
2. **MSFT call diagonal, roll UP-and-OUT (rank 2) — this one overturns the raw net premium.** SOLD Aug21 C460 (bid 33,725 / ask 8,306, OI 59,187, **+$171.6M**) + Aug21 C500 (+$38.3M) + Sep18 C480 (+$24.9M); **BOUGHT Oct16 C510** (ask 37,494 / bid 3,947, OI **253 — virgin**, −$100.9M). **Net credit ≈$109M**, delta cut ~60%. The cleaned curve is **genuine BACKWARDATION** (50.7%@d2 → 35.2%@d7 → **d74 Oct16 = 32.0%, the lowest point on the whole curve**; Aug21 d18 = 35.1%) — they are **selling the backwardated front and buying the curve trough**, exactly what the shape calls for, and buying 32% implied against **rv20 56.4**. Repeated: 07-31 built a matched Oct16 C500/C570 vertical. **MSFT prints −$11.4M net premium and sits in the Step-0 bearish top-25 — that number is 100% an artifact of selling $210M of calls to close winners. There is no bearish MSFT positioning today.**
3. **IWM NFP event program (rank 3, MEDIUM).** Clean 07-31 leg: BUY Aug7 P285 @$0.945 / SELL Aug7 P275 @$0.191, matched size, OI 42,262→92,222 and 28,728→77,931. Net debit $0.755 ≈ **$3.74M**, max $10 wide = $49.5M, **13.3:1**. The raw `KINKED @2026-08-03` label is **contaminated** (that bucket is today's expiry, n=108,119, IV 24.09% vs 18.46% the next day) and was discarded; the cleaned curve is **CONTANGO with one genuine event kink at dte 4 = 2026-08-07 = 19.36%** vs 18.47%(d3)/16.60%(d7). A debit put spread buys and sells at the same kinked vol ⇒ near-vol-neutral, expressing NFP **direction** without paying the **event premium**. Today's Aug21 legs are directionally unambiguous (P282 ask 46,381 / bid 2,724, ratio 17.0) but their prices are **non-monotone in strike** (277 $0.903 / 279 $0.994 / 282 $1.021 — VWAP contamination from the +1.72% intraday drift), so the agent **could not derive a coherent net debit and declined to name that structure**.

**Multileg artifact rejections:** (a) **SPX 7000/8000 conversion-reversal / box complex** — the *entire* `top_premium_trades` payload including the day's largest print at **$888.4M**; paired legs at identical size and timestamp (2027-12-17 C7000 size 7,000 bid + P8000 size 7,000 ask, both 19:47:56Z), the same contract printing on both bid and ask at identical prices, C−P ≈ 0 vs a theoretical −17. Synthetic financing — **anyone reading `top-premium-trades` naively today gets a completely false picture of institutional intent.** (b) SPXW 260803 C7580–7610 — 0DTE expiry-day artifact, IV 1.94–6.80. (c) **FISV Sep18 C55/P50 — an option-vs-STOCK collar** (`stock_multi_leg_volume` 99,001 and 150,000 vs option-only 127 and 87 = ~99.9% against stock); **this explains FISV's −$66.3M net premium, #2 bearish in Step 0, as a collar artifact rather than bearish conviction.** (d) DRAM Aug21 C60 (50,002 stock vs 50 option). (e) NKE Sep18 P40/C45 — a genuine ~$20M option-option structure, but sizes unequal (88,060 P vs 72,077 C) and only 158 of 88,191 contracts classified bid/ask, so long strangle vs short strangle vs ratio risk-reversal could not be distinguished — **consciously declined as not scoreable.**

---

## 4. LEAP Builds (6–24 months)

**EMPTY.** LEAPs are only **3.6% of today's DTE volume share**, and the radar did not manufacture conviction where the flow does not support it.

**One marginal candidate, gated out: CRWV at exactly 6 of 9 gates**, self-demoted by the agent to "LOW-tier input, not MEDIUM/HIGH", then scored raw 2 → DROP.
- **Passed:** `oi_trend` BUILDING **10/10** consecutive days; fresh OTM LEAP builds — `CRWV270319C00110000` (strike $110, DTE 228, OI +1,945, **96% ask-side**) and `CRWV270617C00200000` (strike $200, DTE 318, OI +1,364, **90% ask-side**), both genuine directional convexity, not deep-ITM stock replacement; `cum_premium_flow_90d` **+$140.4M** (30d +$45.8M ⇒ implied prior-60d +$94.6M, smooth accretion); dark-pool largest; DP price levels.
- **Failed:** `position_rolls` — **ZERO rolls across 08-03/07-31/07-30/07-29/07-28**, i.e. a fresh open, not a thesis extension; `institutional_accumulation_10d` — **4 of 5 sessions NEUTRAL**.
- ⚠ **`conviction-matrix` reads MIXED at confidence 4.3**, failing the >70 DIRECTIONAL_LONG bar outright — the agent cleared it only via an "alternative LEAP-tenor path", so **the +1 conviction-matrix rubric line was correctly not awarded**.
- ⚠ **The 90d net skew is only ~1.6% of gross turnover** — near the noise floor for a beta-7.41 name.
- ⚠ CRWV closed **$85.76, +19.5% on the day** (07-30 $73.90 → 07-31 $71.77 → 08-03 $85.76), against being −22.9% over 30 days. A violent bounce, not a quiet build.
- fz: short_float 18.96%, DTC 2.22, **beta 7.41**, insider_own 37.8% with **insider_trans −15.3% (net selling)**. **C34 invalidation anchor: the $81.56 dark-pool support cluster.**
- Fundamentals **CAUTION**: miss_streak 3-of-4 (−22.3%, −11.2%, beat, −25.7%), unprofitable (net −25.57%), **D/E 6.4849** with the script's "low" leverage tag flagged as miscalibrated. Gate's verdict on this leg verbatim: *"distribution dressed as accumulation — YES."*

**Disqualifications worth recording:**

| Ticker | Reason |
|---|---|
| **NVDA** | The **cleanest-looking fresh ask-dominant LEAP call build of the day** (270319C250, 271217C225, 270319C195, 271217C220; ask/bid up to 20:1; `oi-trend` BUILDING 10/10) — **fails Gate 4 outright on `cum-premium-flow` 90d net = −$188.7M.** 30d is +$35.3M, so days 31–90 run **−$224.0M**: a late partial reversal inside a net-bearish 90d regime, not thesis-extension. |
| **MSFT** | Zero rows in the `--min-dte 180` fresh-build list; its only long-dated footprint is a roll whose far leg is DTE≈74 (not LEAP-length). **`conviction-matrix` = COVERED_CALL, confidence 14** ("dark pool buying + call selling — yield enhancement, capping upside") = hard disqualifier. |
| TSLA | 281215P250 (+9,384) and 281215P175 (+7,925) are **puts** — tail hedging, wrong sign for this lane. |
| FSLR | 90d +$23.1M ≈ 1% skew (noise); institutional-accumulation NEUTRAL (0.91, slightly sell-tilted); matrix MIXED 2.5. |
| SOFI / AMD | Deep-OTM $5 lottery put / strike $1,120 vs spot $484.58 — artifacts, not conviction. |
| EA, INTC, GOOGL, ORCL, AXTI, LLY | All **bid-dominant** (selling calls/puts) or near-balanced — none clears Gate 2. |
| IWM, QQQ, SPY, XLU, XLF, SMH, XLE, XLB, XLK | Index/sector-ETF long-dated OI growth is overwhelmingly **put-side** (IWM270617P275, QQQ271217P390, SPY280616P435, XLU270617P37, SMH270617P625…) — portfolio/rate hedging consistent with the rising-10Y backdrop, and out of scope for a single-name radar. |

---

## 5. Volatility Surface

**Hygiene summary (mandatory — the raw label is not trustworthy).** Of 22 names scanned, **10 (45%) had their raw shape label flip** after dropping the 0DTE/expired bucket and sub-15-contract tenors: MU, COHR, ACLS, SMH, DELL, HD, OKTA, INTU, KGS, EA. Base-shape also flipped for MU, COHR, SMH, DELL and EA — meaning those five carry a **contango base with a kink riding on top**, a shape neither label alone describes. Cleaned counts: BACKWARDATION 13 · KINKED 6 · FLAT 1 · **NO_NEAR_TENOR 2**. `earnings-scout` independently ran the same module and **7 of its 15 labels flipped** (CRWV, ACLS, COHR, NBIS, AMD, KGS, LLY).

> `min_contracts` (default 15) is a **named, tunable parameter and NOT audit-frozen** — it was introduced ad hoc and has not cleared a pre-registered bar. FIS, IRM, ACLS, KGS, FERG and EAT all live or die on it.

**KINKED names:**

| Ticker | kink DTE | kink expiry | Prominence | Contracts | Event at the kink |
|---|---|---|---|---|---|
| **OKTA** | 18 | 2026-08-21 | **101.9%** | 1,508 | **Largest kink in the scan** — IV 175.0% vs 76–87% neighbours. No catalyst-cache match; likely FQ2 just outside the 14-day screener window. |
| **HD** | 18 | 2026-08-21 | 25.5% | 819 | Consistent with HD's historical mid-August earnings window. |
| **SMH** | 11 | 2026-08-14 | 11.6% | 1,658 | ETF — broad semis earnings cluster, sitting between NFP and CPI. |
| DELL | 11 | 2026-08-14 | 7.9% (2nd at 46d, 11.7%) | 3,352 | Ambiguous — Aug 14 is retail-sales day; could be macro or a missed earnings date. |
| **MU** | 4 | **2026-08-07 = NFP day** | 6.8% | **44,450** | **A pure macro kink, not earnings.** Front tenor already at 130% IV into NFP on top of rv20 106.4%. |
| INTU | 25 | 2026-08-28 | 6.7% | 174 | Likely FQ4, outside the screener window. |
| ACLS | 18 | 2026-08-21 | 29% raw jump | **10 (floor near-miss)** | **Manual override** — earnings 2026-08-06 (T+3), `implied_move` 16.48% from the independent earnings-catalyst cache corroborates a real kink the 15-contract floor is suppressing. |

**BACKWARDATION calendars: ZERO surfaced.** Every elevated-ratio name has an identifiable pending catalyst inside the front tenor, so none clears the "panic resolving, no catalyst" bar — and with only today's snapshot, no ratio can be certified as *falling*:

| Ticker | front_end_ratio | Catalyst inside the front tenor |
|---|---|---|
| **MCD** | **1.802** | Earnings **tomorrow** (08-04 premarket) — the most extreme ratio in the scan, purely event |
| SNDK | 1.548 | Earnings 08-05 (T+2) |
| AXTI | 1.396 | No earnings match, but rv20 193% and +43% over 5d — idiosyncratic event still resolving |
| SOXX | 1.364 | NFP + CPI inside the front tenor |
| LITE | 1.262 | Earnings 08-11 |
| FSLR | 1.242 | No earnings match; IV-rank 100, NFP/CPI inside front |
| WOLF | 1.231 | Structurally chaotic post-Ch.11 name; NFP inside front |

Two are too data-thin to trade at all: **UCTT** (only 2 tenors survive the floor) and **MPWR** (5 tenors, nearest 18 DTE, no listed kink, −5.73% today on no identified catalyst).

**`NO_NEAR_TENOR` is NOT `FLAT` — ACLS and KGS both hit it.** Their nearest surviving tenor is 46+ DTE, so the front end is **unmeasurable**; a raw `front-end-iv-ratio` of 1.00 there means "no data", never "calm". Both have earnings inside three days.

**IV outliers** (all 20 cached rows are today's expiry, so most `max_iv` vs `avg_iv` gaps are single-print noise). Two corroborate the semis thesis independently: **MU put 850** (avg 2.1% / max 53.9%, vol 456, $1.66M) and **MU put 742.5** (avg 2.0% / max 53.3%, vol 587) — same signature on the name already kinking on NFP with rv20 106%; plus **SMH put 510** (avg 3.9% / max 59.3%). Reads as tail-hedge accumulation, not noise.

**Skew (`term-skew --dte-target 365`):** TAIL_HEDGING clusters exactly where you would expect — the semis complex (**UCTT 0.143**, SMH 0.061, SOXX 0.058) and two hard-catalyst names (**HD 0.068**, MCD 0.053). **No lottery-composite candidates** (COMPLACENT + high IV-rank + negative skew) — the only negative-skew name (LNTH, −0.0128) has IV-rank 0 and fails the high-IV-rank leg. C6 stays correctly withheld; nothing to route through C13.

**Best clean single vol candidate: AXTI** — `vrp_proxy −42.1 BUY-cheap`, the largest realised/implied gap in the scan (rv20 **193.1%** vs IV ~151%), VRP-aligned, on a +43% five-day move. An outright long-vol / straddle idea, not a calendar. **Flagged by one agent only ⇒ §8, not scored.**

**Earnings vol verdicts** (`earnings-scout`, 15 candidates from the intersection of the earnings-catalyst cache and the C12 funnel):

| Ticker | Verdict | Earnings | Implied move | front_end_ratio | Note |
|---|---|---|---|---|---|
| **CRWV** | **SELL VOL** (rank 1) | 08-11 | **9.02%** | **1.177** | The **only** name in the batch clearing the >1.10 panic DQ. Hygiene flipped raw BACKWARDATION → **CONTANGO**. Sub-threshold kink at 11dte (4.99–5.0% vs the 5.0% bar) sitting exactly on the earnings-adjacent tenor. |
| SNDK | CALENDAR | 08-05 | **13.88%** | 1.548 | Largest liquid move in the batch; **naked short DQ'd**. Strongest back-skew in the batch (TAIL_HEDGING +0.0948). |
| MCD | CALENDAR | **08-04 AM** | 3.37% | **1.802** | Naked short DQ'd. Covering expiry **is NFP day**. |
| LLY | CALENDAR | 08-05 | 5.83% | 1.895 | ⚠ Hygiene KINKED, but the **kink at 25 DTE (08-28) is NOT at the earnings tenor** — almost certainly a separate LLY-specific catalyst. Short leg restricted to 08-07; do not extend past 08-28. |

**Structural finding worth carrying forward:** the 08-04/08-05 earnings cluster (MCD / AMD / FIS / IRM / LLY / SNDK / IONQ) **all share one covering expiry — 2026-08-07, which is NFP day.** Every front-end ratio in that cluster is inflated by NFP macro premium *on top of* earnings premium, which is why so many read "extreme panic" rather than clean event pricing. The 08-12 cluster (COHR / NBIS / EAT) has the identical problem with **CPI**. **Cross-agent agreement on one of these ratios is corroboration of a shared artifact, not independent confirmation.**

**11 SKIPs, with reasons:** AMD (kink not at its own earnings tenor; back skew flat −0.003) · FIS (ratio 2.421, 9 of 13 tenors dropped, skew payload empty) · IRM (ratio 1.536, 3 tenors, skew empty) · IONQ (ratio 1.579, weak back confirmation) · **ACLS + KGS (NO_NEAR_TENOR — unmeasurable)** · **FERG + EAT (degenerate front/back pairing — the raw CLI misreports `ratio=1.000 FLAT`, the exact artifact the hygiene module exists to catch; RMBS class)** · LITE (front elevation is NFP day, not its own 08-11 earnings — macro misread as an earnings signal) · COHR (hygiene flips to FLAT, no event premium at all; earnings 08-12 = CPI day) · NBIS (2.9% kink, CPI same-day).

**Two data-quality flags found (not assumed):**
1. ⚠ **EA is a merger-arb pinned name — DO NOT TRADE.** `iv_rank 0` and 2–9% IV across every tenor including 2028 LEAPs initially reads as cheap vol, but **rv20 = rv60 = 3.8%** confirms it trades near-parity to a pending take-private. The flat curve is **arb pinning, not complacency** — the same failure class as the registered merger-arb blind spot.
2. ⚠ **`screener iv-rank --mode low` field `iv30d` looks corrupted.** LNTH's screener `iv30d = 6.7%` (which drives its `iv_rank 0` tag) disagrees with its own `iv-term-structure` read of **13.6–19.0% across 14 cleanly-liquid tenors**, and its `iv30d_1m`/`iv30d_1w` (0.52/0.60) do not reconcile with `iv30d` either. **Do not trust the IV-rank-0 bucket at face value.** Not independently verified for ITGR/ATKR, but the same field is the suspect.

⚠ **Every `iv-percentile-zscore` in this section used `dates_used = 78`, below the ≥120-day bar — all percentiles and z-scores are PROVISIONAL.**

**Class ceilings apply** (2026-08-01 P1 #3): FSLR, DELL, HD, MCD, OKTA, INTU and KGS sit in the `high_iv_rank`-capped lane (0.60), and `earnings_vol` caps at 0.55 — both then land in the anti-predictive [0.55, 0.65) band and floor at `starter`.

---

## 6. Risk & Correlation

**Macro headline:** curve normal (+0.45), **core PCE 3.29% sticky above target**, **10Y 4.75% and rising +27bp/30d** against a 3.63% fed funds rate, USD weakening. A rising-real-rate backdrop the flow tape does not price. Forward calendar: claims 08-06 (T+3) · **NFP 08-07 (T+4, HIGH)** · **CPI 08-12 (T+7, HIGH)** · PPI 08-13 · retail sales 08-14 · FOMC minutes 08-19 · **no August FOMC**.

**Breadth cross-check (`fz`, advisory):** 340 advancers / 163 decliners, **`pct_green` 67.59%**, avg +1.04%. `divergence_flag: false` on the classic test (the index is green *and* `pct_green` > 50). **But the meaningful divergence today runs the other way** — `uw` options-flow breadth is only **40% bullish** (2,514 vs 3,770) against that 67.6% green price tape. Two independent lineages disagreeing in direction. Advisory, does not change sizing.

**Correlation clusters (`uw risk portfolio-correlation` against today's candidates, not the static watchlist):**

**`AI_semis_cluster` = {SNDK, CRWV, NBIS, SMH}** — a single connected component at the ≥0.70 threshold:

| Pair | Corr |
|---|---|
| SNDK / SMH | **0.893** |
| CRWV / NBIS | **0.877** |
| NBIS / SMH | 0.759 |
| SNDK / NBIS | 0.719 |
| CRWV / SMH | 0.710 |

**Kept member: SNDK** (highest raw_score, 4). CRWV and NBIS take a mechanical −1 tier; SMH is recorded but moot under short routing. **Four of six candidates are one AI-infrastructure bet.** Soft cluster (monitor, no penalty): SNDK/CRWV 0.698. Not flagged: **SNDK/MCD −0.609** — negative-signed, a diversifier rather than a duplication; GOOGL pairs all below 0.60.

**Front-end IV panic reads (`--near-dte 7`, never the default 1):** SNDK **1.548** · MCD **1.802** · NBIS **1.208** · CRWV **1.177** · GOOGL **1.109** (marginal, 0.009 over) — all five fire the mechanical >1.10 override. SNDK/MCD/CRWV are earnings-hump elevation rather than systemic panic; the gate is mechanical and fires anyway. **SMH 1.094 is the only candidate below threshold** — index-level tape shows no systemic panic.

**Regime conflicts:** SMH short vs UPTREND trend (SPY above both SMAs) — recorded, moot under short routing. No long conflicts. TRANSITIONAL's "reduce size, wait for clarity" is honoured by the empty book itself.

**Sector warnings:** Healthcare **and** Consumer Defensive both force `watch_only` on netted-vs-gross disagreement (C55) — no candidates affected. Technology is the one clean netted+gross+persistence inflow, **but semis are not participating** (SMH −0.56% / SOXX −1.66% on 5d vs XLK +2.15%) — a Tech-in read does not transfer to SOX names this week.

**Fundamentals verdicts (Phase 2b — no VETOs):**

| Ticker | Verdict | Δtier | Next earnings | Driver |
|---|---|---|---|---|
| SNDK | **CAUTION** | −1 | **2026-08-05 (T+2)** | Insider **MSPR −100.0 every month since 2025-07** into a 13.88% implied-move print. Offset by a 4/4 beat streak and +82.76% revenue growth. |
| CRWV | **CAUTION** | −1 | 2026-08-11 (T+6) | miss_streak 3-of-4, MSPR −60.9, unprofitable, **D/E 6.48** (script's "low" tag miscalibrated), beta 7.41 |
| GOOGL | **CONFIRM** | 0 | 2026-10-27 (T+85) | **Insider MSPR +30.83 (BUYING)**, rev +20.05%, margins 60.9/33.1/54.8%, D/E 0.12 |
| NBIS | **CAUTION** | −1 | **2026-08-12 (T+7, CPI day)** | MSPR −73.42, **operating margin −70.55%** (the +93.09% net margin is likely non-operating), operative **beta 4.44** (fz) not 1.03 (Finnhub) |
| MCD | **CONFIRM** | 0 | **2026-08-04 (T+1, premarket)** | beat_streak 3/4 low-dispersion; MSPR −55.47 but insider_own only 0.06% ⇒ de minimis |

This was a **real-insider-data run** — all five MSPR reads are genuine signals, so no verdict relies on the NA-never-penalizes carve-out. The recurring pattern across three CAUTIONs is identical: **persistent insider selling stacked against an imminent or event-basis earnings print.**

⚠ **Data discrepancy flagged:** GOOGL's next-earnings date reads **2026-10-27 from Finnhub** but **2026-11-04 from the `uw` chain**. Both are far outside any horizon here, so it changes nothing today — recorded so it can be resolved before it matters.

**Event-risk flags:** MCD T+1 · SNDK T+2 · CRWV T+6 · NBIS T+7 (on CPI day) — plus NFP at T+4 and CPI at T+7 inside every swing horizon.

**Debate-disconfirmation cuts — the gate fired on all five names:**

| Ticker | Bull residual | Bear residual | Gate |
|---|---|---|---|
| SNDK | 0.45 | **0.65** | **cut** |
| CRWV | 0.30 | **0.75** | **cut** |
| GOOGL | 0.35 | **0.75** | **cut** |
| NBIS | 0.25 | **0.75** | **cut** |
| MCD | 0.35 | **0.75** | **cut** |

No name escalated to a second round (escalation requires both residuals within one bin **and** ≥0.75; no bull reached 0.75). Notably, **GOOGL's bull conceded register C48 outright** — the exact +3 accumulation conjunction it was arguing for is BH-significant negative-excess at **−29.2pp, p=0.003**.

**Adverse flow / exit candidates** (carried group `conviction_2026-07-31` = [CRWV], carried thesis **vol_long**):
- **CRWV — EXIT CANDIDATE (monetize, not adverse).** The carried long-vol thesis **paid**: +19.5% single-session realised move, volume 2.0×, OI +61,863, a $9.8M single DP print, and iv_rank now 80.7. Vol is now rich into the 08-11 print and today's own fleet flipped to the *opposite* structure (a vol_short fly). **Monetize or roll to defined risk** — holding long premium at iv_rank 80.7 after the spike is a decaying asset.
- **Fundamentals-drift tripwire (`fz`, advisory):** CRWV drift since 07-31 shows only market cap / EV +$7.63B — i.e. the price move itself. **No adverse fundamental field moved** (no short-float jump, no target cut, no recom deterioration). No adverse-fundamentals exit.

**Hedge sleeve:** **Book net delta = 0 (no sized positions) — no mechanical hedge required.** Advisory for residual portfolio longs: with VIX 15.86 after a −15% five-session crush, VRP fair-to-negative, and NFP T+4 / CPI T+7 both live, downside convexity is near its cheapest configuration of the summer. Preferred expressions: a **SPY Sep 745/720 put debit spread** (defined-risk, ~1.6% OTM entry) or a small **VIX Sep 18/22/26 call ladder**. Both are hedge *uses* and out of scope for the short-routing rule. The corroborating regime signal — not a directional call — is `multileg-strategist`'s **SPY crash-convexity put-fly ladder** (~$66M debit, 4 expiries, bodies 30–34% OTM, scaled 100k→150k over three sessions, Sept→Nov) plus **two sessions of IWM downside buying into NFP**. A well-capitalized desk is paying up for tail insurance into the autumn while spot grinds higher. That is the tape in which owning cheap wings beats selling them.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**EMPTY. No name reached MEDIUM (7) or HIGH (9). Highest raw_score today was 4.**

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`, from the 2026-08-01 `/calibration-audit` `phase_3_calibration`:

| Tier | Mean realised P&L | Payoff ratio | Half-Kelly | n |
|---|---|---|---|---|
| HIGH | **−2.441** | 0.72 | 0.0 | 7 |
| MEDIUM | +0.104 | 0.948 | 0.0132 | 19 |
| LOW | −0.583 | **1.197** | 0.0 | 91 |
| DROP | −2.270 | 0.824 | 0.0 | 384 |

**Kelly gate: `ADVISORY_ONLY`** — n=27 closed is below the 30 required, and tier × expectancy is non-monotone. The win-rate ladder stays the live sizer. Note what the table says about *where the edge lives*: **LOW carries the only payoff ratio above 1.0** while HIGH is the worst mean P&L in the book — a high hit-rate with a sub-1 payoff loses money, and this book's hit-rate ordering is inverted anyway (HIGH 0.143 realised vs DROP 0.440, **5th consecutive audit**).

Since §7 is empty, the audited breakdown for the five debated names is recorded here instead:

| | **SNDK** | **CRWV** | **GOOGL** | **NBIS** | **MCD** | **SMH** |
|---|---|---|---|---|---|---|
| `raw_score` | **4** | 2 | 2 | 1 | 0 | **−3** |
| Tier | LOW | DROP | DROP | DROP | DROP | DROP |
| Direction | long | vol_short | long | long | vol | **short** |
| `dominant_signal_class` | `sector_rotation` | `earnings_vol` | `dark_pool_accumulation` | `bullish_flow` | `earnings_vol` | `bearish_flow` |
| `confluence_score` | null | null | null | null | 5 (bearish funnel) | null |
| `cum_flow_30d` | **+$928.3M** | +$45.8M | +$66.7M | +$285.2M | +$0.38M | +$184.4M |
| `cum_flow_90d` | **+$2.62B** | +$140.4M | **−$487.1M** | +$305.8M | −$23.3M | +$97.6M |
| `win_rate` (n, source) | null — NA(substrate) | null — NA(substrate) | null — NA(substrate) | **0.4161** (137, backtest_clean) | null — NA(substrate) | **0.5804** (143, backtest_clean) |
| `market_excess` | null | null | null | **−8.03pp** | null | **+8.39pp** |
| `pre_risk_size` | starter | skip | skip | skip | skip | watch_only |
| `fundamentals_verdict` | CAUTION | CAUTION | **CONFIRM** | CAUTION | **CONFIRM** | n/a (ETF) |
| Debate (bull / bear) | 0.45 / **0.65** | 0.30 / **0.75** | 0.35 / **0.75** | 0.25 / **0.75** | 0.35 / **0.75** | n/a |
| Gates fired | panic, fundamentals, event_risk, debate (−4) | panic, cluster, fundamentals, debate (−4) | panic, event_risk, debate (−3) | panic, cluster, fundamentals, event_risk, debate (−5) | panic, debate (−2) | short-routing, regime, cluster, sector, event_risk |
| **Final size** | **skip** | **skip** | **skip** | **skip** | **skip** | **watch_only** |
| Invalidation | Close < $1,214.83 or post-print DEX sign-flip | DP cluster **$81.56**–$85.76 breach | **DP shelf $368.42** (C34) | DEX sign-flip 2 sessions, or 30d cum-flow net-bearish | Self-expires at tomorrow's open | 30d cum-flow stays bullish + 2 closes above the 08-03 high |

**`sector_rotation` — SNDK's own class — was newly flagged as miscalibrated in the 2026-08-01 audit at +28.6pp divergence with a realised 0.25**, joining `earnings_vol` (+43.4pp, n=97) and `high_iv_rank` (+32.1pp, n=24) as classes where the rubric lies to itself. That is an independent argument against the day's top score that no agent raised, and it strengthens the skip.

**Score component detail (SNDK, Σ = 4 = raw_score):**

| Line | Pts | Source agent | Source tool | Evidence |
|---|---|---|---|---|
| sector-rotation single-name leader (conditional) | +1 | sector-rotation-strategist | `sector-flow-persistence` + `market-regime` (netted) + `cumulative-premium-flow` | Technology persistence 1.00 ≥ 0.6; netted +$217.4M agrees with gross (C55-clean); cum_flow_30d +$928.3M aligned, ≥$50M. Only name passing all three. |
| mechanized DEX flip / vanna-squeeze | +1 | dealer-positioning-strategist | `options-structure vanna` + dated VIX | vanna_squeeze TRUE: net_vanna +209 (put 1,135 vs call −926) + 3 falling VIX closes 17.09→15.99→15.86; DEX de-risking −8.29B→−0.23B agrees. **Caveat carried: the agent itself calls the mechanics secondary to the 08-05 event.** |
| vol-surface BACKWARDATION with VRP-aligned bias | +1 | vol-surface-scout | `front-end-iv-ratio` + `iv-term-structure` | BACKWARDATION survives hygiene 19/19 tenors, ratio 1.548, vrp_proxy −20.6 BUY-cheap (RV20 156.2 ahead of front IV). Proxy is self-built IV−RV, not the audited tool. |
| cum-flow net directional accretion (30d), intent-screened | +1 | signal-confluence-quant | `historical cumulative-premium-flow` | +$928,294,801 aligned, 1.75% of $53.16B gross, 7.4× union median. C28 intent screen **passes** — top OI decreases are two-sided dte-4 event de-risking (C1100 −178/$15.7M vs P1200 −197/$14.7M) = churn, not one-sided distribution. No dividend ⇒ ex-div arb screen n/a. |

**Two quant rulings worth recording, both freeze-safe and tightening-only:**
1. **CALENDAR ∉ {BUY VOL, SELL VOL}.** The frozen line names two verdicts; CALENDAR is a third (short-front / long-back relative value, net-vega ambiguous). Widening a frozen line's coverage is a **loosening**, which the freeze forbids. **SNDK and MCD scored 0 on that line; CRWV's unambiguous SELL VOL earned the +1.**
2. **"Mild align" ≠ "VRP-aligned bias."** MCD (`vrp_proxy +6.9 neutral`) and SMH (+6.2 neutral) got 0; only SNDK (−20.6 BUY-cheap) carries explicit alignment.
3. **C11 gate (c) — the scale-relative floor — bound on GOOGL**: +$66.67M is **0.80% of $8.336B trailing-30d gross**, below the 5% bar ⇒ **+3 halved to +1**. This is the same failure mode as the 2026-06-11 AAPL read that cleared a full +3 on a 0.6% net imbalance. GOOGL's separate +1 cum-flow line then scored 0 on the C28 intent screen (distribution_flag present) — the same weak flow cannot both halve the accumulation line and pay on its own line.

**Instrumentation carried (advisory, 0 rubric points — these exist so the *next* audit can grade C16/C18, which have been untestable for three cycles):** `implied_move` — SNDK 13.88% · CRWV 9.02% · MCD 3.37% · GOOGL 2.83%. `dp_block_to_float_ratio` — GOOGL **4.37e-5** (255,805 sh / 5.85B float). `insider_cluster_flag` — GOOGL **false** (checked-and-absent, not null).

**Deep-dive hand-off:** skipped — no HIGH-tier names. `uw playbook batch-scan` also skipped: the raw_score ≥ 7 list is empty, so there was nothing to batch.

### Conviction rubric (Step 4), embedded verbatim for audit — **RUBRIC FROZEN, version `2026-06-12`**

```
Daily conviction score = Σ:
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna-squeeze setup in trade direction
      (verified SIGN CHANGE, not a level; |net_dex| on flip day ≥ 0.25× trailing-10-session median;
       computed by scripts/dex_flip.py, never by hand; vanna disjunct needs a dated VIX source)
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified
      institutional-tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms
      (sign aligned AND |cum_flow_30d| ≥ $50M AND ≥5% of the name's trailing-30d gross); else halved +3→+1
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL:
      award only when dominant_signal_class == leap_directional; 0 in all non-LEAP contexts
  +1  uw historical cumulative-premium-flow net directional accretion (30d) — INTENT-SCREENED:
      award only when (a) no C28 distribution_flag on the name, AND (b) on dividend payers in an
      ex-div window, the accreting prints are NOT deep-ITM sub-parity calls
  +1  sector-rotation-strategist names ticker as single-name leader — CONDITIONAL: sector
      persistence_score ≥ 0.6 AND cum_flow_30d aligned AND |cum_flow_30d| ≥ $50M. Default 0.
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising pc-ratio-zscore (VRP positive)
      — an INFORMED-FLOW CONTINUATION penalty, not a "crowd is wrong, fade it" signal
  -3  flow_conflict — cum_premium_flow 30d direction clearly opposite dominant_signal_class
  -1  flow_conflict_lite — 30d cum_flow read is MIXED (mutually exclusive with flow_conflict)

  # TIER GATES applied by risk-monitor in 2d — 0 points, never in score_components:
  -1  [TIER GATE] correlation cluster (pairwise corr ≥ 0.70)
  -3  [TIER GATE] uw risk market-regime conflicts with trade direction

  # REMOVED: uw insights signal-confluence ≥4 (+2) — 2026-06-12 P0.2, a server-side re-count of
  #          already-scored quantities. Funnel seed only: 0 points, gates no entry, in no HIGH gate.
  # REMOVED: uw hot-chains sweep-persistence top-5 (+1) — 2026-05-23 P0.3, −22pp over two audits.
  # REMOVED: gamma-flip-tracker 0DTE breakout (+2) — 2026-05-09, NO-INFO on swing horizon.
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | **HIGH** | full (subject to the Step-3a 3-of-4 load-bearing gate + win-rate gate) |
| 7 – 8 | **MEDIUM** | half (subject to win-rate gate) |
| 3 – 6 | **LOW** | starter / watch-only |
| ≤ 2 | drop | filtered by the quant's drop floor |

**Tier-cut status:** the ≥9 HIGH cut **failed its scheduled re-confirmation on 2026-06-12** (HIGH realised 0.222 / MED 0.214 / LOW 0.444) and the inversion has now persisted for **five consecutive audits** (HIGH 0.143 vs DROP 0.440 at 2026-08-01). The cuts are retained under the P0.1 freeze — re-binning on another thin window repeats the documented failure mode — but they **carry no validated ranking claim**, and the P0.6 out-of-regime guard caps all sizing at half in the interim.

---

## 8. Watch-only — single signal, no confluence

Surfaced by exactly one Phase 1 agent, so excluded from the conviction rubric. **Journaling only, not trade entry.**

| Ticker | Flagging agent | Finding |
|---|---|---|
| **QQQ** | dealer-positioning | **Qualifying mechanized DEX flip, LONG, 1.89×**, zero whipsaw, corroborated by a same-session GEX regime flip. The cleanest mechanized signal of the day — and it earned no position because no second agent saw it. |
| **TSLA** | dealer-positioning | Qualifying mechanized DEX flip LONG 1.43×, zero whipsaw. ⚠ front-end IV 1.466 BACKWARDATION = unresolved event risk. |
| **FSLR** | dealer-positioning | Qualifying mechanized DEX flip LONG **6.01× (largest ratio)** + same-day GEX regime confirmation. ⚠ Thin options book (<$250M per strike). Also today's top S&P mover, +10.28%. |
| **INTC** | dealer-positioning | Vanna-squeeze TRUE + DEX flipped 07-30 and holding 3 sessions. Cleanest multi-signal confluence of the vanna group, but the flip is not on the latest session so it does not qualify. |
| **ASML / SNDK / MU** | dealer-positioning | Vanna-squeeze TRUE. MU carries `whipsaw_warning` (4 sign changes) and its DEX trajectory disagrees with the vanna sign. |
| **MSFT** | multileg | **$109M net-credit call diagonal roll up-and-out** — moderately bullish and materially de-risked. Its −$11.4M net premium and bearish top-25 ranking are a **pure artifact** of selling $210M of calls to close winners. |
| **SPY / IWM** | multileg | The crash-convexity put-fly ladder and the NFP put debit spread. **Defined-risk long structures, NOT directional index shorts** — explicitly out of scope for the short-routing rule. |
| **NVDA** | accumulation-hunter | MEDIUM, 5 aligned signals, but cum_flow_30d +$35.3M **fails the $50M conjunction bar** (would halve to +1) and ~60% of mega-tier dollar volume is closing-cross. Separately disqualified from the LEAP book on 90d −$188.7M. |
| **AXTI** | vol-surface | **Best clean vol candidate in the scan** — vrp_proxy −42.1 BUY-cheap, rv20 193.1% vs IV ~151%, VRP-aligned, +43% over 5d. Outright long-vol / straddle. |
| **OKTA** | vol-surface | **Largest kink in the scan** — 18 DTE / 08-21, prominence **101.9%**, IV 175.0% vs 76–87% neighbours. VRP conflicts, so no rubric point. |
| **HD** | vol-surface / contrarian | KINKED 18d/25.5%; BEARISH_EXTREME z=3.08 but wrong polarity for the −2 line, and price/flow are *aligned* (no divergence to fade). |
| **DELL / INTU** | vol-surface | KINKED 11d/7.9% and 25d/6.7%. VRP conflicts ⇒ 0 points. Both in the `high_iv_rank` 0.60-capped lane. |
| **LLY** | earnings-scout | CALENDAR, but the qualifying kink at 25 DTE is **not** at its earnings tenor — a separate catalyst. |
| **ACLS / KGS** | vol-surface / earnings-scout | **NO_NEAR_TENOR** — front end unmeasurable, not calm. Both have earnings within 3 days. |
| **ASML / ABT / XOP** | contrarian | Tested at ±2σ and rejected — see §3b for the three independent kill switches on ABT. |
| **COHR** | dealer-positioning / vol-surface | DEX flip near-miss at **0.92× the floor** — re-check 08-04. Hygiene flips its shape to FLAT (no event premium); earnings 08-12 = CPI day. |
| **MPWR / UCTT** | vol-surface | Too data-thin to size (2 and 5 surviving tenors). UCTT carries the highest TAIL_HEDGING skew in the scan (0.143). |
| **MRCY** | volume-vs-average | Volume ratio 50.7× average with iv_rank 98.9 and no identified catalyst — a flow-side look, not a vol-side one. |
| **EA** | vol-surface | ⚠ **DO NOT TRADE** — merger-arb pinned (rv20 = rv60 = 3.8%, near-parity to a pending take-private). |

**Also dropped before scoring:** 15 names failed the C12 liquidity floor — DIOD ($40.2M ADV), **ELVN ($48.2M)**, **CDNA ($50.0M)**, GRAB (price $3.67), ADNT, NEOG, PGEN, FOSL, LIND, ARXS, **AI ($47.1M)**, ABR, ABSI, AESI, PAGS. Note that **both `fz` orthogonal lanes contributed almost nothing tradeable today**: after de-doubling the emitter bug, nearly every squeeze and RS candidate fell below the floor; only EAT, IMAX, ACHC and ATKR survived into the funnel, and none was flagged by any agent.

---

## Data-quality notes for the next calibration audit

1. **`fz screen` doubles the first letter of every ticker** (AABEO→ABEO, EEAT→EAT, PPGEN→PGEN, NNEOG→NEOG). Present on both the squeeze and RS lanes. De-doubled manually this run. `fz breadth` and `fz_enrich` are unaffected. This is the same emitter-class bug that blocked C16 for four audits — **check the emitter, not the consumer.**
2. **`uw historical pc-ratio-zscore` has no `--date` flag** (confirmed empirically: `error: unknown flag: --date`). It is a single-snapshot tool, so the "rising z-score" clause in the −2 contrarian rubric line **cannot be evaluated by any agent** as currently written. This is a live unsatisfiable-precondition bug in a frozen rubric line.
3. **`uw insights analyst-vs-flow` returned only the `options_flow` block for all 15 earnings candidates** — no analyst-recommendation field in the payload. The analyst-vs-flow divergence check (described as the highest-EV setup in `earnings-scout`'s lane) could not be applied to a single name.
4. **`screener iv-rank --mode low` field `iv30d` is internally inconsistent** — LNTH reads 6.7% against its own term structure's 13.6–19.0%, and `iv30d_1m`/`iv30d_1w` do not reconcile with it. The entire IV-rank-0 bucket should be treated as suspect until verified.
5. **`fz` `recom` and `upside_to_target_pct` are null for all five enriched names** — confirmed upstream gap (the known C17 freeze), not absence-by-choice.
6. **`uw insights deep-dive`'s `yahoo_fundamentals` leg returned HTTP 401 for all three top names** — graceful-skipped, no impact on the report.
7. **GOOGL next-earnings disagrees across sources**: Finnhub 2026-10-27 vs `uw` chain 2026-11-04.
8. **Every `iv-percentile-zscore` in this run used `dates_used = 78`, below the ≥120-day bar** — all percentiles and z-scores in §5 are provisional.
9. **`min_contracts = 15`** in `term_structure_hygiene.py` is tunable and **not audit-frozen**; six names in this run (FIS, IRM, ACLS, KGS, FERG, EAT) live or die on it.
10. **Two envelope-emission adjustments, recorded so the audit reads the right numbers.** (a) CRWV's bull residual came back as **0.30**, which falls exactly between the schema's 0.25 and 0.35 bins — binned **down to 0.25** (the conservative direction for a confidence that only ever cuts size). The debate gate fires either way. (b) SMH's pre-risk recommendation was emitted by the quant as `watch_only`, which the schema does not permit in `pre_risk_size` — recorded as `pre_risk_size: "skip"` (what the ladder-then-band-then-floor actually produces on a raw −3) with `final_size: "watch_only"` carrying the short-routing result. The routing rule belongs at final size, not pre-risk.
