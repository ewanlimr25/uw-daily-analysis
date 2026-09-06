# Daily Market Analysis — 2026-08-05

## Executive Summary
- **Regime + GEX state:** **TRANSITIONAL** (trend UPTREND) — SPY 769.79 (−0.20%) above 20SMA 748.41 and 50SMA 746.37, but UW options-flow breadth only **35.6% bullish** (2,234 of 6,280 tickers). VIX **15.81**, −4.18% today and **−23.48% over five sessions**. SPY's gamma book **flipped NEGATIVE today** (day 1, unconfirmed) with ZGL 775.97 above spot; QQQ POSITIVE but decaying. Sector lean is defensive on netted flow (Utilities/Staples in; Industrials/Tech/Cons-Cyclical out) while price says the exact opposite.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** **SPY** — NEGATIVE (short gamma), ZGL **775.97** (reliable, 0.6% above spot), call wall 775 / put wall 770 → walls tight, coiled two-way tape, size small. **QQQ** — POSITIVE but total GEX decayed >60% in two sessions, ZGL **unusable artifact (249.5 vs spot 719.73)**, call wall 735 / put wall 715 → skewed condor or stand aside. Advisory, see §2.
- **Top swing build:** **NONE.** Nothing cleared the gate stack. The sized book is empty.
- **Top LEAP candidate:** **NONE.** LEAP radar returned an empty board — zero names reached 6-of-9 gates.
- **Biggest risk:** **Event stack, not correlation.** Jobless claims + ZTS earnings T+1 (08-06), **NFP T+2 (08-07)**, **CPI T+5 (08-12)**. The 08-07 expiry carries **$4.85B** — the third-largest live expiry — precisely because it is payrolls day. With an empty book there is no cluster to hedge; `portfolio-correlation` returned no pair ≥0.70.

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — Mixed signals, reduce position size, wait for clarity.** Trend **UPTREND**. SPY 769.79, +2.95% over 30d, −0.91% from its 90-day high, above both the 20- and 50-day SMA. Tool guidance verbatim: *"Half position sizes. Favor defined-risk strategies. Iron condors in range."*

The breadth picture is the tension. UW flow breadth reads **35.6% bullish**, while `fz`'s independent cash-tape breadth reads **48.71% green** (245 advancers / 257 decliners, avg −0.22%, median −0.04%). Both are sub-50 and the index closed red, so `divergence_flag = false` — this is **not** the green-tape distribution tell. It is a mild, broad pullback where the options tape is materially more bearish than the cash tape.

**Tape framing (the thing that must not be misread).** SPY −0.20% versus equal-weight RSP −0.23% — cap-weighted and equal-weight moved together, so there is **no cap-weight divergence today**. The week is the story:

| Symbol | 1d | 5d |
|---|---|---|
| SPY | −0.20% | **+5.53%** |
| QQQ | −0.90% | **+8.40%** |
| IWM | −0.64% | +3.88% |
| RSP | −0.23% | +1.85% |
| ^VIX | 15.81 (−4.18%) | **−23.48%** |

Sector ETFs, 1d / 5d: XLV +1.27 / −1.25 · XLB +1.23 / +1.74 · XLY +0.30 / +6.30 · XLRE +0.07 / −1.65 · XLI −0.03 / +5.49 · XLP −0.05 / −2.32 · **XLK −0.53 / +11.61** · XLU −1.02 / −2.78 · XLC −1.04 / +1.24 · **XLE −2.07 / −2.28**.

The correct read is *extended after a vertical week into a payrolls print*, not *dip to buy*.

### Per-index gamma (current-state EOD book)

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 771.34 | **775.97** (reliable) | +$636.5M | **NEGATIVE** (spot below ZGL) | 775 | 770 |
| QQQ | 719.73 | 249.5 — **artifact, discard** | +$285.3M | POSITIVE (decaying) | 735 | 715 |
| IWM | — | — | — | **FULLY_NEGATIVE**, whipsawing 6+ times in 10 sessions — disqualified as noise | — | — |

**DTE volume share:** 0DTE 37.1% · weeklies 23.4% · monthlies 27.2% · LEAPs 3.3% → `regime_hint` **BALANCED**. Monthly+ at 30.5% is middling — neither a clean institutional-positioning tape nor a retail 0DTE tape.

**VRP:** SPY **FAIR** (+0.0009; IV30 13.46% vs realised 13.37%) — no edge either way. QQQ **FAIR label but −0.0367** (IV30 22.01% vs realised **25.68%**) — realised is running *above* implied on the Nasdaq complex, making it a **premium-buying** tape. Short-vol structures on QQQ/semis are VRP-contradicted; this gated several candidates below.

**Macro backdrop** (`scripts/fred_macro.py`): yield curve **normal** (10Y−2Y +0.45) · core CPI **2.81%** YoY · core PCE **3.29%** YoY · unemployment 4.2% · payrolls +57k MoM · 10Y **4.63% and RISING** (+0.14 over 30d) · USD **weakening** (−1.44 over 30d) · fed funds 3.63%. Core PCE well above target with a rising long end is a hawkish-drift backdrop underneath an equity melt-up.

**Forward `event_risk`:** claims Thu 08-06 (medium) · **NFP Fri 08-07 (high)** · **CPI Wed 08-12 (high)** · PPI Thu 08-13 (medium-high) · FOMC minutes Wed 08-19 (medium).

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — built from open interest that persists overnight — read forward as the *prior* for next session's open. It is prose-only, contributes **0 points** to the conviction rubric, and makes **no backtested predictive claim**. Predictive validation of these levels lives in `/weekly-analysis`'s rolling §2 backtest. Scope is **SPY and QQQ only**.

**SPY — short gamma, walls tight, flip is one day old.**
Spot 771.34, ZGL **775.97** (`zgl_reliable = true`, 0.6% above spot — comfortably inside the 5% band), total GEX +$636.5M, call wall **775**, put wall **770**. The call wall and the flip line are effectively the same level.

`regime_flip_dates` shows POSITIVE→NEGATIVE **exactly on 2026-08-05 — day 1, unconfirmed.** The mechanism is legible in the ZGL trajectory: 746.93 (07-31) → 756.06 → 767.91 → **775.97 today**, i.e. +8.06 in one session while spot fell only 0.20%. Fresh 0DTE call-side OI built at the top of the five-day melt-up pushed the flip line *up* faster than price fell, and today's mild dip let ZGL cross above spot.

*Structure bias:* this is **not** the classic "cheap straddle, ride the trend" short-gamma setup, because the put wall sits essentially on top of spot (1.34 points, 0.17% below). Read it as a coiled two-way tape — debit verticals or a small long straddle rather than a full directional 0DTE push. A break of 770 can air-pocket; a reclaim of 775–776 flips dealers back long gamma and caps upside hard.

**QQQ — nominally long gamma, but thin and decaying.**
Spot 719.73, `zero_gamma_level` **249.5 — a 65%-below-spot extrapolation artifact, discarded entirely** (`zgl_reliable = false`; this is the standing SPY/QQQ/IWM/MU grid-artifact class, and for QQQ it recurs on *every* day of the 30-day window: 249.5, 711.88, 699.22, 352.82…). Regime POSITIVE by `total_gex` sign, held three sessions — but magnitude decayed from +$774M (08-03) to +$624M (08-04) to **+$285M today**, a >60% two-day fall while price is up 8.40% over five sessions. The options book is not confirming the equity rally with fresh long-gamma conviction. Call wall **735** (2.1% above), put wall **715** (0.66% below) — asymmetric.

*Structure bias:* skewed iron condor with the short strike inside 715 tighter than the one inside 735, or stand aside per §2a's own QQQ cautions.

**Mandatory caveats — stated, not buried:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and recomputes ZGL and walls. This is especially live for SPY, whose flip happened *today*: if early OI reprices the 775 strike or spot reclaims 775–776, the book flips straight back to POSITIVE.
- **ZGL reliability.** SPY's trusted (0.6% from spot); QQQ's discarded (65% away, known artifact). QQQ's regime read leans entirely on the `total_gex` sign, which has independently softened.
- **Gap risk voids the prior.** **NFP lands Friday 2026-08-07, two sessions out, and is itself an expiry — the 08-07 tenor carries $4.85B, third-largest of all live expiries.** Tomorrow is jobless claims. A payrolls surprise blows through either wall regardless of tonight's dealer positioning.
- **Tooling limit.** `uw` cannot isolate the D+1 expiry (`gex --dte-max 1` errors). This is the standing **0–45 DTE** book as the best available proxy.
- **ETF book.** SPY/QQQ ETF gamma, not the cleaner SPX/NDX index book. Corroborated today: the market-wide top-20 greek screener contains **zero** SPY/QQQ prints (all SPX/NVDA), so no independent index-book cross-check was available.

### 2a. Next-session 0DTE premium-selling setup (validated stack)

The GEX walls above are a **map, not a pin** — wall-as-magnet backtested NO_GO, as did every directional 0DTE signal. What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, and explicitly **not a guaranteed edge**.

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` / VIX | **LOW** / 15.81 | **LOW** / 15.81 |
| implied move | 0.85% | 1.50% |
| `expected_range_pct` | 0.85% | 1.45% |
| `size_scalar` | **0.50** | **0.25** |
| structure | iron fly / short straddle centred **770.93**, wings ±0.85% | iron fly centred **717.19**, wings ±1.45% |
| `stand_aside_reason` | none | none |
| `caution` | none | **front-end backwardation** |
| backtest (n=60) | win 88.3%, gross **+0.217%** → **net +0.117%** | win 85.0%, gross **+0.356%** → **net +0.256%** |
| worst day | −1.40% | −2.453% |

`backtest_verdict` for both: **GO_PREMIUM_SELL_INTRADAY**.

**The binding caveat is the VIX conditioner, and it argues against taking this.** PnL by VIX state is LOW **−0.08** / MID +0.373 / HIGH +0.335, with tercile bounds [16.5, 18.1]. At **VIX 15.81 we are in the LOW tercile — the only negative-expectancy state in the sample.** The stack says "sell" while its own conditioner says this is the thin-edge regime; that is why `size_scalar` is 0.50 and 0.25 rather than 1.0.

`pnl_basis` (quote it on its real footing): **percent-of-underlying-spot-notional, GROSS**, computed as 0.8×1σ premium captured minus realised |open−close|. It is **not** premium-collected and **not** margin-relative, so "+0.117% net" is tiny in absolute terms. Lead with net — Vilkov (2024) found an unconditional 0DTE condor flips to negative net Sharpe once costs are charged, so the gross win-rate overstates a negatively-skewed seller's edge.

**Entry rule:** enter at/after the open once the overnight gap resolves; if it gaps beyond the wings, stand aside. Hold the 0DTE to the close — **never carry overnight** (SPY overnight mean +0.02%, QQQ **−0.097%**; the gap erases the edge). **Direction: none — this is delta-neutral. Do not add a directional tilt.**

**SPY ≈ SPX** (validated identical). **QQQ is the weaker book** (no Nasdaq index substitute), carries a backwardation caution, and sits in the negative LOW-VIX tercile — treat as stand-aside-leaning.

**Tail caveat (mandatory):** the validation sample contains **no vol shock**; the short-vol left tail is **UNSAMPLED**. Promotion bar: this lane stays advisory / 0 rubric points **permanently** until both a vol-shock day enters the sample and **net** expectancy clears a tail-aware bar. Win-rate is explicitly **not** the promotion metric.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

**Headline: zero names qualify for the mechanized +1 DEX-flip line.** The full dated test (13 `uw options-structure dex --date` calls each through `scripts/dex_flip.py`, 2026-07-20→08-05) ran on **8 names** — SPY, QQQ, IWM, NVDA, AMD, MSFT, TSM, TSLA. Ten more got a light-touch read only (AVGO, MU, PLTR, NBIS, SMH, MSTR, NFLX, GOOGL, AMZN, APP), flagged `dex_trajectory_5d: UNAVAILABLE` rather than invented.

| Symbol | sign changes | Why it fails |
|---|---|---|
| SPY | 1 | Real flip on 07-31 (9-session negative run → positive), but stale — 08-04 already carries today's sign, `prior_run_length = 0` |
| QQQ | 1 | Flip 08-03 (10-session negative run), today continues positive |
| IWM | 1 | Flip 08-03, today continues positive |
| NVDA | 2 | Flip 07-31, today continues positive and accelerating |
| AMD | 2 | Negative dip lasted only 2 sessions (07-28/29) — never cleared the 3-session floor either way |
| MSFT | **0** | Always positive — a pure **level** jump ($0.7–6.3B → $20.5–29.1B on 07-30), no sign change |
| TSM | 3 | Flip 07-30, today continues positive, 6 sessions in |
| TSLA | 2 | Failed 1-day flip 08-03, reverted 08-04/05 |

SPY/QQQ/IWM/TSM all had *genuine* flips that cleared the ≥3-session prior-run rule when they happened — they are 2–6 sessions stale by today. **Real trend information, zero rubric points.** MSFT is the instructive case: a large DEX *level* jump with no sign change, exactly the class of miscall (MU/MRVL/ASML, 2026-06-11) this mechanized line was built to prevent.

**Vanna-squeeze candidates (hypothesis-only — Karsan/SqueezeMetrics framing, no validated edge, no pre-registered backtest).** Dated VIX leg from the Yahoo chart API `^VIX`: 07-29 20.66 → 07-30 17.09 → 07-31 15.99 → 08-03 15.86 → 08-04 16.50 (a +4.0% bounce) → 08-05 **15.81**. Net −23.5% with one interrupting up-day — the caveat is attached, not hidden.
- **TSLA** — `vanna_state` **SHORT/put-heavy** (net_vanna +14,886; the tool's own text: *"Classic vanna-squeeze setup if VIX collapses"*), charm +1,207,673, GEX confirmed POSITIVE five sessions. DEX itself has **not** flipped — which is the point of the setup, not a flaw.
- **NFLX** — put-heavy (+1,104), **freshest GEX confirmation in the book** (regime flipped NEGATIVE→POSITIVE *today*), front-end IV 1.113.

**Constructive dealer flow:** QQQ (index) and NVDA (single name) — DEX and GEX both stable-positive with no conflicts. **SPY: caution** — DEX trend is long but GEX flipped negative today at the ZGL, with a vanna *selling* headwind (call-heavy book, net_vanna −351,954: falling VIX shrinks call delta and dealers cut long-stock hedges). **AMD is the name to watch** — dealer positioning is stable but its front-end IV ratio **1.142** is the most panicked in the book against −$131.5M bearish premium; that tension is what precedes a genuine flip.

Front-end IV ratios (`--near-dte 7`): AMD **1.142** · MSFT 1.135 · NFLX 1.113 · TSM 1.056 · TSLA 0.995 FLAT · QQQ 0.935 · SPY 0.922.

---

## 2b. Sector Rotation

**Rotation regime call: `no_change`, confidence LOW. Every sector is `watch_only`. Zero single-name leaders extracted.**

### The netted-vs-gross conflict (C55) is the finding

Direction reads off the **netted** `uw risk market-regime.sector_rotation`. `sector-flow` and `sector-flow-persistence` are **one gross-turnover source** (net_flow = gross call$ − put$, sign-agnostic) and are a **durability filter only** — they cannot express direction. Today they disagree violently:

| Sector | NETTED (authoritative) | GROSS turnover (durability only) | Status |
|---|---|---|---|
| **Technology** | **−$65.30M OUT** | **+$5,164.97M**, persistence 1.0 | **DISAGREE → watch_only** (flagship conflict) |
| Industrials | **−$89.45M OUT** | +$93.0M, 0.6 ROTATING | DISAGREE → watch_only |
| Consumer Cyclical | **−$61.21M OUT** | +$717.3M, 0.8 | DISAGREE → watch_only |
| Consumer Defensive | **+$2.60M IN** | +$44.6M, 1.0 | Agree, but below median magnitude → "broad tape, no rotation" |
| Utilities | **+$11.90M IN** | +$43.1M, 0.6 ROTATING | Agree, but sub-standout → "broad tape, no rotation" |
| Healthcare | −$0.58M (≈flat) | +$253.2M, 1.0 | Netted ≈ noise → watch_only |
| Financial Services | *no netted read* | +$198.7M, 1.0 | Insufficient evidence → watch_only |
| Comm Services | *no netted read* | +$814.0M, 0.8 | watch_only |

Two mechanical notes. First, the **absolute ≥0.6 persistence gate is saturated** — 6 of 11 sectors tie at 1.0, so it discriminates nothing; the market-relative test (top-third persistence **and** above-median signed magnitude, median $115.8M) is what actually separates, and only Technology, Financial Services and Healthcare clear it. None converts to a call. Second, `market-regime.sector_rotation` only ever lists 3-in / 3-out, so **5 of 11 sectors have no netted read at all** — those default to `watch_only` on evidence-insufficiency, not on disagreement.

Single-name flow corroborates the Technology verdict directly: NVDA/MSFT/TSM/MU/PLTR/SHOP lead the bullish screener **and** AMD/INTC/NOW/SNDK lead the bearish one. Same-sector two-way churn, name by name — precisely the signature the gross metric cannot disambiguate. Do not read Tech screener strength as sector confirmation.

**Flow contradicts price.** Netted flow favours Utilities/Staples, whose 5-day tape is the *worst* on the board (XLU −2.78%, XLP −2.32%) while XLK ran +11.61%. The ETF layer resolves part of it: **XLP's own options tape is net bearish** (5d net −$7.0M, clean put buying — Dec-18 78P ask $8.84M, Sep-18 78P $1.87M). The XLP *instrument* is not being accumulated even though the GICS aggregate reads mildly positive, so that aggregate inflow is likely concentrated in individual staples names (WMT +$10.7M screener premium) rather than the sector ETF. **Read the Utilities/Staples "inflow" as noise/hedging-adjacent, not early accumulation.**

### ETF flow tape (advisory — 0 rubric points)

| ETF | Net flow (5d) | Dir / persistence | DP positioning | Options urgency | GICS agreement | Leaders |
|---|---|---|---|---|---|---|
| **SMH** | +$85.8M | BULLISH | 2 large below-mid blocks ($35.5M, $15.0M — sold below mid, distribution tell) + 1 at-mid | Mixed: Sep-18 590C bought, Jan-27 550P bought (hedge), Sep-18 600C **sold at bid** ($7.5M) | agrees gross Tech, **disagrees netted Tech** → reinforces watch_only | n/a |
| EWY | +$17.2M | MIXED | not deep-pulled | — | n/a (geographic) | — |
| **XLI** | +$14.3M | BULLISH | 1 aggressive above-mid buy ($11.0M, +2.17 vs mid) | Nov-20 170P **sold at bid** $14.3M vs 170P bought at ask $2.9M — net ambiguous | **disagrees netted Industrials (−$89.45M)** → watch_only | n/a |
| XOP | +$10.3M | BULLISH | not deep-pulled | — | Energy no netted read; diverges from XLE | — |
| KRE | +$8.1M | BULLISH | not deep-pulled | — | Fin Svcs gross standout, no netted read | — |
| XLK | +$4.1M | BULLISH | not deep-pulled | — | same Tech conflict as SMH | — |
| **XLE** | **−$3.3M** | BEARISH | Seller-initiated blocks (below/at-mid), $34.4M/$10.6M/$10.6M | Put buying (Dec-18 60P $4.7M) + calls sold at bid — clean bearish tilt | contradicts XOP → within-Energy split | — |
| **XLP** | **−$7.0M** | BEARISH | Near-mid, no strong tell | Clean put buying (Dec-18 78P $8.84M) | **disagrees GICS Cons Defensive** → watch_only | — |
| **GDX** | **−$28.6M** | **BEARISH** (largest outflow in universe, multi-day sign-consistent) | Large above-mid blocks ($96.7M/$58.6M/$45.9M) — but ETF DP is a creation/redemption & hedging tell, **not** accumulation | Dominant put buying at ask: Dec-18 75P $19.8M + Nov-20 75P $16.2M (~$36M) vs Sep-18 79C ask $11.5M | Basic Materials gross INFLOW but **miners sold via puts** — sub-industry divergence | — |

**Swing-book implication:** no rotation trade to put on. Treat Technology as a **two-way churn / no-net-bet** sector. **GDX is the one clean, multi-day-persistent, options-flow-confirmed bearish read** — carried to §3b. Do not buy the Utilities/Staples inflow headline.

---

## 3. Swing Setups (1–6 weeks)

**Nothing is sized. One name reached LOW tier and was gated to watch-only; one reached DROP and was routed to watch-only.**

### 3a. Long swings (regime-aligned)

**Empty.** No long candidate cleared the confluence gate.

The **accumulation board is empty**, and the reason is itself the finding: today's mega-tier dark-pool tape is dominated by **closing-cross artifact**. For AAPL, MSFT, AMD, AMZN, GOOGL, GOOG, LLY and AVGO, ~100% of mega-tier trade count executes 20:00:00–20:10Z at **one identical price per name** (AAPL $311.00, MSFT $487.46, AMD $482.05, AMZN $272.65, GOOGL $362.43, GOOG $360.13, LLY $1169.86, AVGO $418.28), confirmed by `dark-pool extended-hours` tagging. That is quarter-flow / benchmark-rebalance / MOC allocation, **not stealth buying** — their high mega buy_ratios are an artifact, not conviction.

Two names carried a genuine non-closing-cross component and both were rejected:
- **TSM** — ~$570M of real intraday institutional block buying (13:41–16:53Z, aggressor-side, DP shelves $417 / $420 / $422, invalidation anchor **$414**). Killed by every downstream gate: `institutional-accumulation` reads **NEUTRAL** (buy_sell_ratio 1.05), `cum_flow_30d` **−$141.2M** (clears $50M in the *wrong* direction for a long), and a **C28 `distribution_flag`** — ~$18.6M of closing call premium on the 260918C00400000 strike (OI −5,078 on 5,198 volume), plus two more call strikes closing on high volume with no put-side offset. Bullish-position unwind, not accumulation.
- **MU** — genuine tail (~$147M) dwarfed by a $1.095B / 1.226M-share / 103-trade closing-cross print at $893.19. `institutional-accumulation` **NEUTRAL** (1.09); `cum_flow_30d` **−$0.39M**, failing the $50M conjunction by three orders of magnitude. `distribution_flag` present.

**NVDA is the day's sharpest unresolved contradiction and is flagged, not traded.** It is the #1 net-premium bullish name (**+$110.0M**), yet its mega-tier dark-pool `buy_ratio` is **0.039** — **96% of mega-size institutional prints were sells** ($1.24B sold vs $50M bought across 28 mega-tier trades). `contrarian-scanner` adjudicated and could not corroborate from its own lane: `price-vs-flow` `divergence: false`, flow bullish, price +10.16%/30d, P/C z **−1.113 NORMAL** — the distribution tell lives in the block-print channel its tools cannot see. **NVDA therefore does not qualify for the −2 continuation penalty.** `leap-positioning-radar` independently confirms DP buy_ratio 0.434 (net selling) and 90d cum-flow +$68.6M on $91.4B gross = **0.07% skew** (noise). Meanwhile `dealer-positioning` has NVDA's DEX/GEX as the cleanest picture in the book. Genuinely two-sided; carried to §8. Same pattern, smaller: **SPY mega buy_ratio 0.154, PLTR 0.34**.

### 3b. Short / fade swings (defined risk only)

> **All directional shorts print as `watch_only` (2026-08-01 P0 #1).** This section still carries full theses, structures and invalidations — the routing is not suppression, and every short is scored and serialized so `/calibration-audit` keeps resolving the counterfactual. Short-vol structures and defined-risk short legs are unaffected.

**GDX — raw_score 2, DROP tier, `watch_only`.** Direction SHORT, `multileg_directional`.

| Field | Value |
|---|---|
| Structure | Two matched long put debit verticals: buy 2026-12-18 P75 / sell P67 (~46,500×) **and** buy 2026-11-20 P75 / sell P67 (~45,050×) |
| Evidence | 99.8% ask on both long legs, 99.9% bid on both short legs; net debit ≈ **$19.8M**, ~$8.00 wide, max value ~$36M; **v/OI 4.4 (Dec) and 10.6 (Nov) = opening**; brand-new strikes (261120 P75 OI was 4,243) |
| Term anchor | Post-hygiene curve **flat 44–48%** with a ~3-vol bump at Dec-18 (47.6%). Deliberately **not** anchored to the kink — equal size in the un-kinked Nov and the kinked Dec proves they are not trading it. The flat mid-curve is *why* a two-month ladder is the coherent expression. Vol entry fair: Dec 47.6% vs rv20 45.8% |
| Context | GDX closed **$83.68, +7.39% today, +13.74% over 5 sessions**; gold broke $4,200. GEX POSITIVE, zero-gamma 54.01, strike-70 node **−$10.8M** net gex — deep in the negative-gamma put wing, where a move down is accelerative |
| `cum_flow_30d` | **−$24.19M** = −2.1% of $1.14B gross, label MIXED → **−1 `flow_conflict_lite`**, not −3 |
| `repeat_count` | **1** — verified against the 08-04, 08-03, 07-31 and 07-30 multileg boards. Single session, not a programme |
| **Invalidation** | GDX holds above **$80** through Sep-18 expiry with term structure flat; **or** the P75 legs begin printing bid-side (unwind); **or** 30d cum-flow turns clearly positive |

**Honest residual, conceded by the finding agent itself:** *"protection on a large long-miner book after +13.7% is close to as likely as a new bearish thesis — a hedge is not alpha."* The fundamentals gate returned **CAUTION**: mechanical legs are structurally NA (it is an ETF, and NA never penalizes), but a dated macro stack contradicts the structure — gold >$4,200 on its biggest day since February, USD weakening, China + Tether accumulating, LBMA Q2 demand **+37% YoY**, and sell-side "calling the bottom" pieces dated **07-28/07-29 that predate the rally**. GDX is also still **−4.28% below its 200-day SMA** with RSI 63.06 — not a blow-off top. Debate: bull 0.55 / bear 0.45, gate does not fire.

### Sweeps (informational — 0 rubric points)

Ranked persistence-first. A method caveat: `sweep-persistence` returns a window-level `dominant_direction`, not a per-day directional series, so "≥3 of 5 days same direction" cannot be certified from that call alone — claims below are corroborated against today's actual ask/bid prints.

| Ticker | Side | 5d premium | Persistence | Key print | Read |
|---|---|---|---|---|---|
| **AMD** | Bearish | $2.06B | **5/5, consistency 1.0** | Call selling + LEAP put buying, ~$45M bearish tilt | Strongest bearish name on the desk; also the day's #1 net-bearish premium (−$131.5M). Two independent sources agree |
| **TSLA** | Bearish | $3.03B | **5/5, consistency 1.0** | **330P, Aug-7 expiry, ask-side $8.75M, 2 DTE** | 2 DTE = **NFP day**. Event hedge, not a multi-week thesis. Could unwind fast post-print |
| **NBIS** | Bullish | $752.4M | **5/5, consistency 1.0** | 170C/190C/200C, Aug 14–21, 9–16 DTE; ask $33.1M vs bid $21.5M (~1.5:1) | Cleanest bullish momentum, no event confound |
| AVGO | Bullish | — | 3/5 | Dec-18 / Jan-2028 LEAP-dominated, $5.3M call-ask at 135 DTE | Not urgent momentum — a LEAP lean |
| BE | Bullish | — | 4/5 | Thin (~$12M), mostly LEAP | Real persistence, today does not confirm urgency |

**Exclusions that matter:** **MU** shows 5/5 "mixed" but today's largest single line is **$18.6M of call *selling*** (900 strike, 2 DTE) — distribution / covered-call writing against the AI rally, not fresh conviction. **QQQ** is an explicit flow_conflict seed: sweeps bearish 5/5 but `cum_flow_30d` **+$53.4M bullish**. **SPXW** ($13.2B, the largest book) is junk: 19 of the top-20 premium trades are one $7000-strike ladder rolled across Sep/Oct/Dec/2027/2028, and the greek screener shows deep-ITM call/put pairs at **identical size and identical timestamp** (C7000 2,000 + P8000 2,000 @14:48:44) — box/jelly-roll financing, zero directional content. **META** would have ranked Tier-1 (bearish 5/5, $1.63B) but **fails the C12 floor** and cannot be proposed.

---

## 4. LEAP Builds (6–24 months)

**Empty board. Zero candidates cleared 6-of-9 gates.** Consistent with LEAPs being only **3.3%** of today's DTE volume share.

The `uw oi biggest-increases --min-dte 180` list is dominated by index/ETF hedging structures (SPX puts/calls at 316–499 DTE, VIX, LQD/HYG/EEM/XLF credit- and rate-hedges) — not single-name directional builds. Disqualifications with reasons:

| Ticker | Gate 2 (fresh DTE>180) | Gate 4 (90d accretion, REQUIRED) | Gate 8 (conviction-matrix) | Verdict |
|---|---|---|---|---|
| **PLTR** | Present, but the DTE=226 build is a **bull call spread** (270319C165 bought on ask / C200 **sold to open**) — two-sided, capped | **−$48.7M** over 90d, MIXED | **MIXED, confidence 4.2%** | DISQUALIFY. Also: 35% of its DP premium is the $158.43 **closing-cross** print |
| **AVGO** | Absent from top-20 | +$90M on ~$22.2B gross = **0.4% skew**, noise | **COVERED_CALL, 18.7%** — *"dark pool buying + call selling, yield enhancement, capping upside"* | DISQUALIFY — COVERED_CALL is a hard reject. 38% of DP premium is the $418.28 closing-cross print |
| BE | Absent | **−$467M** (wrong sign) | MIXED, 2.8% | DISQUALIFY |
| GOOG | Absent (closest 163 DTE, under floor) | +$106.5M / $15B = 0.7%, and 30d **−$48.1M** | MIXED, 6.2% | DISQUALIFY |
| GOOGL | Absent | **−$608M** (wrong sign) | MIXED, 4.0% | DISQUALIFY |
| NVDA | Absent — all top OI growth is 0–9 DTE | +$68.6M / $91.4B = **0.07%** | MIXED, 6.6% | DISQUALIFY |

The macro overlay argues the same way: **10Y at 4.63% and rising** is a genuine headwind to long-duration equity exposure, and netted sector flow is **OUT of Technology**, the sector all six candidates sit in.

---

## 5. Volatility Surface

**Headline hygiene finding: the raw `iv-term-structure` label read BACKWARDATION on 19 of 19 names (100%)** — driven by the **2026-08-07 NFP tenor** sitting inside nearly every front bucket. Running `scripts/term_structure_hygiene.py` (drops `dte<1` and `contracts<15`) **flipped 6 of 19 to KINKED** (AMD, MSFT, TSM, TSLA, MU, AVGO). Note this run's failure mode is *"hides a kink"* — **none flipped to CONTANGO**, unlike 2026-07-24 where 14 of 39 did. `min_contracts=15` (a named, tunable parameter, **not audit-frozen**) killed 2 of 10 earnings names outright and reshaped 4 more.

**NFP contamination is in the front bucket of everything.** The 08-07 tenor prints 92.0% IV on GDX, 56.1% KRE, 46.0% XLI, 44.3% WMT, 201% COHR, 187% NBIS. Any raw label read today without dropping that bucket gives the wrong answer on every name.

### The one genuine, catalyst-aligned dislocation: ZTS

`shape` = `base_shape` = BACKWARDATION, monotonic 16d→534d, **8 tenors kept / 0 dropped**, front tenor 2,068 contracts — the cleanest data quality in its cohort. 16d IV **70.6%** vs 44d **49.6%** = **+42.3% front premium**; front-end ratio **1.424**, well above AMD's 1.142 (the highest *non-earnings* panic in the book), so this is genuine event pricing rather than NFP bleed. `iv-percentile-zscore` **100th pctile, z=+3.79, HIGH_IV** — but **PROVISIONAL** (`dates_used` 80 < the 120 threshold). VRP **+0.44 PREMIUM_SELLING** (IV30 74.07% vs realised 30.07%) — strongly VRP-aligned. `term-skew` at 16 DTE **COMPLACENT 0.927** (calls 74.7% richer than puts 69.2%): the market is **not** crash-hedging this. `implied_move` **10.56%**. Carried to §7 — and killed there.

A reported blind spot: `find_kink`'s interior-local-max test structurally cannot flag ZTS, because its nearest tenor (16 DTE) *is* the earnings-loaded front and sits at the curve boundary. The +42.3% front load is a manual base-slope read, not a module kink detection.

### NEW substrate defect — quarterly-expiry wing contamination

**AMD, TSM, MU and AVGO all show a KINKED read landing on exactly 2026-09-18** — which `expiry_heatmap` confirms is the **single largest premium concentration in the entire book at $6.12B**, larger than today's 0DTE ($5.50B) and NFP's ($4.85B). Because `avg_iv` is unweighted across strikes, the expiry with the most listed strikes mechanically pulls in more far-OTM wing IV regardless of real event risk. The evidence it is an artifact: `term-skew` reads **COMPLACENT/NORMAL and flat** for all four (AMD 0.984, MU 0.979, AVGO 1.032) — inconsistent with genuine event pricing. Contract counts at 44 DTE are healthy (2.4k–12.8k), so the sub-15 floor does not catch it. **Recommendation: treat any KINKED read at the largest-OI quarterly expiry as suspect until skew corroborates it.**

**TSLA's 12-DTE kink** (2026-08-17, prominence 53.9%) is a separate thin-liquidity artifact — an off-cycle Monday expiry carrying only 2,494 contracts against 11–13k on the surrounding Friday weeklies, corroborated flat by front-end ratio 0.995 and skew_ratio 0.997.

### NEW CLI defect — degenerate `front-end-iv-ratio` tenor collapse

The tool returns `near_dte_actual == far_dte_actual`, ratio exactly **1.000**, regime **FLAT** for INSM, MNST, RXO, MRCY, CECO, HAE (and ZTS at near-dte 16) — a tie-break artifact when a name's only two liquid tenors (16 / 44 DTE) sit symmetrically around the tool's `back_dte≈30` default. This is **distinct from the documented `NO_NEAR_TENOR` case and lives inside the raw CLI**, not the term-structure label. Cross-validated: where the raw tool did return a sane number (ZTS, ITT) it matched the hygiene module's `slope_front_next_pct` **exactly**, so the hygiene slope is the trustworthy fallback. **`NO_NEAR_TENOR` is not `FLAT`, and neither is this** — a 1.000 here means "no data", never "calm".

### Disqualified vol candidates

| Name | Reason |
|---|---|
| **MSFT** | Genuine macro kink at **2026-08-12 = CPI**, not a company catalyst. VRP **−0.26 PREMIUM_BUYING** → selling the CPI-elevated front is VRP-contradicted. Context only |
| AMD / TSM / MU | 44-DTE wing-contamination artifact **and** all VRP-negative (−0.12 / −0.069 / −0.25). IV percentiles 33.8 / 22.5 / 28.8 — low percentile alongside a "kinked" read is itself inconsistent |
| TSLA | Thin-tenor artifact + negative VRP |
| AVGO | 9-DTE kink is real but small (prominence 8.2%, just above threshold) with no confirming catalyst; VRP +0.142 mild. 44-DTE leg withheld as artifact-cluster |
| NFLX / NVDA / QQQ | Clean, no kink. **QQQ front-end ratio 0.935 (<1)** — the index book is **not** pricing NFP as a dislocation; the front-end IV crush is real, not a mispricing waiting to be sold |
| KRE, BITX, AR, PAG, ATKR | Low-IV-rank screener names — all no-kink or INSUFFICIENT_DATA (PAG: 0 tenors survived). Screener "low IV rank" ≠ actionable |

**`iv_outliers` cache: every row is today's 0DTE bucket** (108–460% avg IV, the AKAM class). Per the hygiene mandate that is pure wing noise — **zero genuine single-contract whale-hedge signal today.**

### Earnings cohort

Ten C12-floor names with `days_to_earnings ≤ 13`. A structural finding overrides the cohort: **six of ten (ZTS, CECO, ITT, RXO, INSM, MNST — all reporting 08-06) have no listed weekly option.** Their nearest liquid expiry is the 08-21 monthly, **15 days after the print**, so a clean "kink AT the earnings expiry" is structurally unobservable. What you get is the 16-DTE tenor (contains the event) priced above the 44-DTE tenor (does not) — real event-richness, but a diluted read.

**No BUY VOL candidates today** — every genuine near-term earnings name clearing C12 already shows IV rank ≥56 (most ≥75, several at 100) with backwardation priced in. Nothing reads as under-priced vol.

| Name | Verdict | Earnings | Implied move | Why |
|---|---|---|---|---|
| **ZTS** | CALENDAR | 08-06 AM (T+1) | **10.56%** | See §7 — the only name to reach the rubric, and it was gated out |
| **MNST** | CALENDAR | 08-06 PM | 6.54% | Front-end 1.335. 1y skew TAIL_HEDGING 0.1058 is *structural*, unrelated to the print; 60DTE flat. Single-agent, failed confluence |
| **COHR** | CALENDAR | **08-12 = CPI day** | 6.15% | 13 tenors kept / 0 dropped (real weeklies, best data in cohort). Front-end 1.266 at the 9-DTE tenor, correctly skipping the NFP-contaminated 2-DTE tenor which reads **201% IV**. But its 30-DTE back leg also has CPI-adjacent life, compressing the calendar's edge |
| NBIS | SKIP | 08-12 | 7.39% | Raw KINKED is a **false positive** — `kink_expiry` 09-18 is 44 DTE, nowhere near the print. `playbook suggest-strategy` independently returns *"No Clear Edge — Stay Flat"*; flow/DP are bullish, contradicting a short-vol thesis |
| INSM | SKIP | 08-06 | 12.65% | Skew COMPLACENT/negative (−0.0092) into a binary biotech readout while P/C is 3.73 — dimensions point opposite ways |
| RXO | SKIP | 08-06 | 13.05% | 60DTE skew **−0.1375** (calls richer — unusual) against P/C 5.16; only 2 usable tenors, "far" tenor at 163 DTE |
| ITT | SKIP | 08-06 | 7.35% | Weakest front-end in cohort (1.145), only 2 tenors, flow net bullish contradicting |
| **CECO** | SKIP | 08-06 | 15.80% | **1 tenor survives** (30 contracts) → INSUFFICIENT_DATA. The headline 15.80% is built off a thin book — do not trust at size |
| **HAE** | SKIP | 08-06 | — | **0 tenors survive** the contract floor (6 and 2). Not FLAT, not calm — **no tradable options market** |
| MRCY | SKIP | 08-18 | — | Term-skew unmeasurable at both 60DTE and 1y; re-read closer to the event |

---

## 6. Risk & Correlation

**Macro headline:** core PCE **3.29%** YoY well above target with the 10Y **rising** to 4.63% (+14bp/30d) and the USD weakening — a hawkish-drift backdrop beneath a vertical equity week. **Forward event stack: claims + ZTS earnings T+1 (08-06) · NFP T+2 (08-07) · CPI T+5 (08-12) · PPI T+6 · FOMC minutes T+10.** Any swing sized today eats two Tier-1 prints inside a week.

**Correlation:** `uw risk portfolio-correlation --symbols ZTS,GDX` returned `high_correlations: null`. **No cluster ≥0.70, no soft-watch in 0.60–0.70.** A pet-health pharma and a gold-miner ETF are economically orthogonal and the tool confirms it. No candidate duplicates another.

**Panic gate — FIRES.** SPY front-end IV ratio **1.165** (near-DTE-1 IV 18.47% vs 30d 15.86%, BACKWARDATION), above the 1.10 threshold → **−1 tier on everything, no exceptions.** Desk note, not a gate modifier: the DTE-1 bucket *is* the claims/NFP expiry carrying $4.85B, so this is event premium being priced correctly rather than disorderly panic. The threshold is mechanical precisely because discretionary overrides were mis-applied before (2026-05-15 audit).

**VRP gates:** SPY FAIR (+0.0009), QQQ **NEGATIVE** (−0.0367) — premium-buying tape in tech. ZTS's own name-level VRP is **+0.44 PREMIUM_SELLING**, aligned with its short-front-vol structure, so its `vrp` gate no-ops.

**Fundamentals verdicts (top-2):**
- **ZTS — CAUTION (−1).** Earnings tomorrow premarket; beat streak **broken** (Q1'26 missed −6.19% after +7.75%, +3.79%, +4.53%); sell-side **cut PT −14.15% to $108.07 on 08-04**, one day before the print; Yahoo (08-03) flags **US competition and Librela safety concerns**; Diamond Hill Q2 letter cites softening pet-care demand; dark-pool distribution 521.8K sell vs 278.2K buy. Offsetting but not clearing: insider MSPR **+23.83** 3mo average (July +100) — genuine insider *buying*, not the selling-into-weakness pattern this gate hunts — plus Michael Burry adding, and +2.4% YoY revenue growth. `fz_context`: short float 4.51%, days-to-cover 2.47, squeeze LOW, RSI 42.02, inst_own 97.68% with inst_trans **−1.65%** (trimming).
- **GDX — CAUTION (−1, moot).** Detailed in §3b.

**Event-risk flags:** ZTS's own earnings at T+1 is **exempt — the trade *is* the event play**; NFP T+2 and CPI T+5 sit inside the front-leg horizon but are **exempt as defined-risk** (long calendar, max loss capped at the net debit). Verdict no-op, with both exemptions named rather than assumed.

**Debate-disconfirmation cuts:** **ZTS bear 0.65 ≥ bull 0.55 → gate FIRES, −1 tier.** The bear's unrefuted point is structural: with no weekly listed, both legs straddle the print, so the overnight-crush mechanic is unavailable, and the bull's variance decomposition may be circular — its "no-event baseline" (the 09-18 leg's 49.6% IV) is plausibly contaminated by the same event it is trying to isolate, which would pull the derived event-move estimate toward the quoted 10.56% almost by construction. The bull's convergence check (~10.8% vs 10.56%) and the capped-debit argument survive, but they establish *bounded loss*, not *edge*. GDX bull 0.55 / bear 0.45 → no-op. Neither pair reached the ≥0.75 threshold, so no second round.

**Adverse-flow exits from `conviction_2026-08-04` (AVGO, LRCX, NBIS):**
- **LRCX — soft exit candidate.** Flow flipped bearish against yesterday's thesis: net −$5.32M, P/C 1.04, a $128.5M single DP print, IV rank 69.9. Magnitude is modest (volume_ratio 0.92, no spike) — off-thesis decay rather than a hard reversal.
- **AVGO — on-thesis.** Bullish net +$6.8M, OI +57,180, $64.3M DP print on the buy side.
- **NBIS — on-thesis, watch the put tape.** Bullish net +$13.3M, OI +43,182, but P/C 1.256 on volume_ratio 0.58 — quiet with put-heavy volume.
- `fz` drift tripwire: no adverse fundamentals changes (NBIS market cap +$3.3B is price-driven and benign).

**Breadth cross-check (advisory, 0 points):** 245 advancers / 257 decliners, **pct_green 48.71%**, avg −0.22%, median −0.04%. `divergence_flag` **false** — the index closed red, so sub-50% green is *consistent*, not the distribution tell (that flag fires on green-index + sub-50% breadth). Cross-read against UW's 35.6% bullish-flow: **the options tape is materially more bearish than the cash tape.**

**Hedge sleeve: none required.** The sized book is empty; net delta ≈ 0. Do not manufacture a hedge for a book that holds nothing.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**No HIGH or MEDIUM tier calls today.** Both names that cleared the confluence gate are recorded below for the audit trail.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: not computable this session — zero HIGH/MEDIUM calls exist to bin, and the rolling `conviction_<date>` closed-call set has not produced per-tier expectancy since the 2026-08-01 audit. Carried forward from that audit: the freeze-lift criterion remains structurally unrunnable, with **0 post-freeze HIGH/MEDIUM calls** across six cycles.

### ZTS — raw 3, LOW → **watch_only** (triple-gated)

| Field | Value |
|---|---|
| `direction` / `horizon` | vol_short (delta-neutral calendar) / vol |
| `dominant_signal_class` | `earnings_vol` |
| `score_components` | **+1** earnings-scout SELL VOL→CALENDAR (`front-end-iv-ratio` 1.424 BACKWARDATION; 16d 70.6% vs 44d 49.6% = +42.3% front premium; back-month skew flat → front-only richness disqualifies full-size SELL VOL) · **+1** vol-surface BACKWARDATION with VRP-aligned bias (`vrp` +0.44 PREMIUM_SELLING, IV30 74.07% vs realised 30.07%; iv-percentile 100th, z=+3.79, PROVISIONAL) · **+1** `oi-trend` BUILDING 5/5 (+13,116, concentrated in the 08-21 event tenor both sides) |
| Σ check | 1 + 1 + 1 = **3** ✓ |
| `win_rate` | **null**, `win_rate_source` **NA(substrate)** |
| `market_excess` | null |
| `confluence_score` | 5 (bearish funnel — informational only, 0 scoring use) |
| `cum_flow_30d / 90d` | −$8.50M / +$11.58M |
| `implied_move` | **10.56%** |
| `pre_risk_size` | starter |
| `fundamentals_verdict` | **CAUTION** (−1) |
| `debate_residuals` | bull **0.55** / bear **0.65** → gate fires (−1) |
| `gate_verdicts` | regime no-op · vrp no-op · **panic −1** · cluster no-op · sector no-op · **fundamentals −1** · event_risk no-op (both exemptions named) · **debate −1** · rubric_regime capped-half |
| **`final_size`** | **`watch_only`** |
| Structure | Sell 2026-08-21 74-strike straddle (IV 70.6%) / buy 2026-09-18 74-strike straddle (IV 49.6%). Spot $74.39 |
| **Invalidation** | Realised move blows through both legs (gap >> 10.56%). DP distribution + bearish flow mean directional tail risk is real, not purely a vol-crush trade — **close the short leg immediately post-print regardless of thesis** |

Arithmetic: starter −1 (panic) = skip; the further −1s floor at skip. **Even absent the panic gate, fundamentals + debate alone reach the same floor — this is a triple-gated kill, not a marginal one.**

### GDX — raw 2, DROP → **watch_only** (short-routed)

| Field | Value |
|---|---|
| `direction` / `horizon` | short / swing |
| `dominant_signal_class` | `multileg_directional` |
| `score_components` | **+2** multileg term-structure-anchored put-vertical ladder · **+1** `oi-trend` BUILDING 5/5 (+287,584 — but **two-sided**: 08-03's largest adds were **calls**, 77.5C/79C) · **−1** `flow_conflict_lite` (−$24.19M = −2.1% of gross, MIXED) |
| Σ check | 2 + 1 − 1 = **2** ✓ |
| `win_rate` | **null**, `win_rate_source` **NA(substrate)** |
| `gate_verdicts` | regime −1 · vrp no-op · panic −1 · cluster no-op · sector no-op · fundamentals −1 · event_risk no-op · debate no-op · rubric_regime capped-half — **all n/a for sizing; routing governs** |
| **`final_size`** | **`watch_only`** (2026-08-01 P0 #1, directional short, instrument-agnostic) |

### Instrumentation note (register C43 / C16 / C18)

`dp_block_to_float_ratio` and `insider_cluster_flag` are **explicit `null`** on both calls, and the reason is recorded rather than silently dropped: neither name is a `dark_pool_accumulation` row (the accumulation board was empty), and the `fz` insider-cluster lane returned exactly one row market-wide — **`XXAIR`**, a corrupted symbol (recovered: `XAIR`) that fails the C12 floor. `implied_move` **is** populated on the vol row (ZTS, 10.56%) as required.

**⚠ The `fz` doubled-first-letter emitter bug is live again this run** — `fz screen` returned `AANET`=ANET, `CCRL`=CRL, `ZZETA`=ZETA, `QQLYS`=QLYS, `BBLMN`=BLMN, `AABEO`=ABEO, and `fz insider-clusters` returned `XXAIR`=XAIR. `fz breadth` and single-ticker `fz_enrich` lookups are **unaffected** (both keyed back correctly to ZTS/GDX). This is the same class as the `MMSFT` bug that blocked criterion C16 for four consecutive audits: **the defect is in the emitter, and present-and-wrong is worse than absent.** Symbols were recovered from the `Company` field where one exists; the ownership/squeeze view has no Company column and had to be re-pulled with `--view overview` to recover at all.

### Conviction-scoring rubric (verbatim, `rubric_version: 2026-06-12` — FROZEN)

```
Daily conviction score = Σ:
  +1  MECHANIZED DEX flip or vanna-squeeze in trade direction — verified SIGN CHANGE, not a level:
      sign(net_dex) on the latest session opposite to ≥3 consecutive prior sessions, |net_dex| on the flip
      day ≥ 0.25× the trailing-10-session median |net_dex|. Computed by scripts/dex_flip.py, never by hand.
  +3  3+ aligned accumulation signals (DP + OI + smart-positioning, block-stratified institutional-tier
      confirmed) — CONJUNCTION (C11): full +3 ONLY when cum_flow_30d sign-aligned AND |cum_flow_30d| ≥ $50M;
      else halved to +1.
  +1  multi-day OI build (historical oi-trend BUILDING, --days ≥ 5)
  +1  conviction-matrix DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: only when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +1  cum-premium-flow net directional accretion (30d) — INTENT-SCREENED: 0 if a C28 distribution_flag is
      present, or if accreting prints are deep-ITM sub-parity calls on a dividend payer in an ex-div window.
  +1  sector-rotation single-name leader — CONDITIONAL, needs ALL of: persistence_score ≥ 0.6 AND
      cum_flow_30d direction aligned AND |cum_flow_30d| ≥ $50M. Default 0.
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored play type)
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner overcrowded long with rising pc-ratio-zscore — an INFORMED-FLOW CONTINUATION
      penalty, not "fade the crowd" (Pan-Poteshman 2006; Ge-Lin-Pearson 2016).
  -3  flow_conflict — cum_flow_30d clearly OPPOSITE dominant_signal_class
  -1  flow_conflict_lite — 30d cum-flow read is MIXED (signed sum near zero, or aligned but bottom-quartile)
      (-3 and -1 are MUTUALLY EXCLUSIVE — apply exactly one)
  # The two lines below are TIER GATES applied by risk-monitor in 2d. They contribute 0 to raw_score and
  # never appear in score_components.
  -1  [TIER GATE] correlation cluster (pairwise corr ≥ 0.70) — −1 TIER
  -3  [TIER GATE] market-regime conflicts with trade direction — −1 TIER
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | HIGH | full (subject to the 3-of-4 load-bearing-tool gate + win-rate gate) |
| 7–8 | MEDIUM | half (subject to win-rate gate) |
| 3–6 | LOW | starter / watch-only |
| ≤ 2 | DROP | filtered by the quant's drop floor |

**Tier-cut status:** the ≥9 HIGH cut was set in-sample on UPTREND data and **failed its scheduled re-confirmation on 2026-06-12** (bands inverted: HIGH 0.222 / MED 0.214 / LOW 0.444). The cuts are retained under the P0.1 freeze but **carry no validated ranking claim**; the P0.6 out-of-regime guard caps all sizing at half in the interim.

---

## 8. Watch-only — single signal, no confluence

Surfaced by one agent (or by two in *opposite* directions) and excluded from trade entry today. Journaling only.

| Ticker | Flag | Why it failed |
|---|---|---|
| **AMD** | sweep-tracker bearish 5/5, −$131.5M (day's largest bearish print) | Single positive flag. `contrarian-scanner` disqualified the fade framing (P/C z **+0.584 NORMAL** — puts are *not* overcrowded, so there is no crowded short to fade; `divergence: false`). `vol-surface-scout` disqualified its KINKED read as the 44-DTE artifact; VRP −0.12. **Highest front-end panic in the book (1.142) — the name most likely to produce a genuine DEX flip next** |
| **TSLA** | 2 flags, **opposite directions** | `sweep-tracker` bearish 5/5, but the headline print is a **2-DTE 330P into NFP = event hedge**. `dealer-positioning` `vanna_squeeze_flag: true` → LONG (hypothesis-only). `contrarian-scanner`: P/C 0.7217 is *below* its 20d mean (z −0.309) — by contract count TSLA is **less** put-heavy than its own norm. **Unresolved conflict, not confluence** |
| **NVDA** | 0 positive flags | The day's sharpest contradiction: +$110.0M bullish premium vs **96% mega-tier institutional selling**. Unresolvable from within any single lane — see §3a. **Does not qualify for the −2 penalty** (P/C z −1.113, nowhere near ±2σ) |
| **MSFT** | 0 positive flags | P/C z **+4.789 BEARISH_EXTREME** looks like a screaming fade — it is a **structural insurance bid**: flow still net bullish +$35.75M, price +33.38%/30d, and the term-structure elevation sits **precisely on the 08-07 NFP expiry**. `vol-surface` independently disqualified it (kink lands on CPI; VRP −0.26). Raw P/C extremity is a false positive for crowding |
| **NFLX** | 1 flag | Vanna-squeeze (put-heavy, freshest GEX confirmation in the book — regime flipped today). No kink, VRP ≈ FAIR. Hypothesis-only, single lane |
| **NBIS** | 1 flag | Cleanest bullish momentum (5/5, calls-only, ask-heavy 1.5:1) but earnings-scout **SKIP** (false-positive kink), `playbook` "No Clear Edge — Stay Flat", dealer NEGATIVE/amplification-risk all 10 sessions |
| **MNST, COHR** | 1 flag each | Calendar candidates with structural (MNST: 1y tail-hedge skew is unrelated to the print) or CPI-overlap (COHR: earnings *on* CPI day) confounds |
| **AVGO** | Contradicted | `conviction-matrix` **COVERED_CALL 18.7%** (hard reject); 38% of DP premium is the closing-cross print; sweep tier-2 only |
| **TSM, MU** | Rejected | `institutional-accumulation` **NEUTRAL** on both; TSM `cum_flow_30d` **−$141.2M** (wrong sign), MU −$0.39M (trivial); **C28 `distribution_flag` present on both** |
| **SOXL, INSM, RXO** | Disqualified | P/C z extremes (2.028 / 2.384 / 3.536) — SOXL is a 3x leveraged single instrument (continuation, no index-fade exception); INSM/RXO are thin-liquidity artifacts (RXO tenor counts 221→9→14→2→15) |
| **KRE, XLP, XLI, WMT** | Identified, deliberately unscored | KRE buys premium ~8 vol above rv20 under **contango** (vol-disadvantaged). XLP is a **put calendar roll** Sep→Dec at $78 — maintains existing protection, and is long the expensive back / short the cheap front, the inverse of the vol-mispricing trade. XLI has **both legs bid-side** (premium sale/unwind, direction not inferrable). WMT's near-parity ITM leg is the flagged artifact class with two readings; its real content is a **+9.4-vol earnings bulge at 08-21** |
| **PLTR, BE, GOOG, GOOGL** | LEAP-disqualified | Capped call spread / wrong-sign 90d flows (BE −$467M, GOOGL −$608M) / closing-cross artifacts |
| **CECO, HAE, ITT, MRCY** | Unmeasurable | HAE: **0 tenors survive** the contract floor. CECO: 1 tenor → INSUFFICIENT_DATA |
| **DDOG, U, RL** | Off-floor | The three Tier-1 single-leg CONTRARIAN_SHORT puts (size/OI 15.52 / 5.22 / 1.65). **All three fail the C12 floor** → cannot be proposed. Advisory only, **0 points, C19 CLOSED** |
| **SPX / SPXW** | Junk | Box/jelly-roll financing — identical size and timestamp on deep-ITM call/put pairs. Zero directional content |
| **QQQ** | Flow conflict | Sweeps bearish 5/5 vs `cum_flow_30d` **+$53.4M bullish**; P/C z NORMAL after Monday's extreme already unwound; negative VRP |
| **META** | Off-floor | Would have ranked Tier-1 bearish (5/5, $1.63B) but fails C12 |

---

## Appendix — cross-cutting findings for `/calibration-audit`

1. **`uw historical signal-backtest` has no `earnings_vol` and no `multileg_directional` class.** Its enum is exactly `{bullish_flow, bearish_flow, high_iv_rank, volume_spike, dark_pool_accumulation}`. Both of today's names therefore carry honest `win_rate: null / NA(substrate)` — no proxy class was borrowed (C13 forbids it). **Implication worth registering: every historical `earnings_vol` numeric quote in the corpus must have been proxy-sourced**, which bears directly on the 2026-08-01 P1 #3 ceiling (`earnings_vol` capped at 0.55 on a claimed post-freeze realised 0.449, n=78).
2. **C47 reconfirmed hard.** `oi-trend BUILDING` fired on **every single name tested by three independent agents** — `consecutive_build_days: 7` identically across sweep-tracker's 5 candidates, 5/5 on TSM/MU/ZTS/GDX, 10 on PLTR/AVGO/NVDA. Zero discrimination; likely a market-wide pre-NFP OI accretion. It still contributed +1 to both scored names because the rubric is frozen and audits grade rather than retune.
3. **NEW: quarterly-expiry wing contamination** in `iv-term-structure` — see §5.
4. **NEW: degenerate `front-end-iv-ratio` tenor collapse** inside the raw CLI — see §5.
5. **`fz` doubled-first-letter emitter bug live on two endpoints** (`screen`, `insider-clusters`); `breadth` and single-ticker enrichment unaffected — see §7.
6. **Zero mechanized DEX flips** across 8 fully-tested names; every apparent flip is 2–6 sessions stale.
7. **Closing-cross contamination dominates the mega-tier DP tape** — 8 mega-caps at one identical price per name in the 20:00–20:10Z window.
