# Daily Market Analysis — 2026-06-03

## Executive Summary
- **Regime + GEX state:** **TRANSITIONAL / UPTREND** — SPY 754.24 (+5.05% 30d, above 20/50 SMA, −0.81% from 90d high) but **breadth is weak** (33.8% bullish flow, Finviz 39.8% green, avg −0.48%) — a narrow-breadth / distribution-leaning tape under an uptrend label. VIX 16.06. Index dealer book **short-gamma / defensive into NFP**: SPY FULLY_NEGATIVE GEX (−797M, call wall 760 / put wall 740), QQQ thinly long-gamma (+89M, walls 742–750) with a **panicked front-end (1.136 backwardation)**. VRP **FAIR** (0.04) — no vol edge. Half-size, defined-risk guidance.
- **Next-session GEX (SPY/QQQ):** **SPY** — short-gamma (FULLY_NEGATIVE), ZGL unreliable(null), call wall **760** / put wall **740** → dealers amplify; range-with-downside-tail, debit verticals over premium sales. **QQQ** — modest long-gamma, ZGL unreliable, call wall **750** / put wall **742** (spot perched on the flip) → pin 742–750 while it holds, one tick from flipping short. *Advisory, see §2. NFP gap (Fri 6/5) voids the prior.*
- **Top swing build:** **SNDK — LONG, raw 8 (MEDIUM), STARTER / defined-risk only.** The only debate-cleared, fundamentals-CONFIRM, flow-confirmed name. +$1.29B 30d cum-premium accretion, 5/5 OI build, institutional DP mega-buy, memory/storage is the one BID theme. Structure: **bull put spread below the 1788–1800 DP shelf**, small, post-NFP. Win-rate 0.64 is a fallback proxy (n=14) — conviction real, edge unconfirmed. Invalidation: loses the **1788 DP shelf**.
- **Top LEAP candidate:** **NONE.** The long-dated OI tape is a hedging/yield-enhancement book (ETF puts, covered-call writing); every single-name LEAP build resolved COVERED_CALL / DISTRIBUTION / MIXED. Compute mega-caps show LEAP *put* accumulation, not bullish builds. LEAP book empty.
- **Biggest risk:** **Semis/memory concentration into a macro gauntlet.** 4 of 5 top names + every watch name are semis/memory — structurally one correlated bet, and the surviving long (SNDK) sits inside a complex flagged **CONFIRMED DISTRIBUTION** (SMH +143k OI all puts). **NFP Fri 6/5 (2 sessions out)**, CPI 6/10, FOMC 6/17. If the book grows beyond SNDK, hedge with a **QQQ put spread through NFP** (panic is QQQ-localized).

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** **TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity."** Underlying trend **UPTREND**. SPY 754.24, +5.05% 30d, above 20SMA (744.83) and 50SMA (709.82), −0.81% from the 90-day high. Market breadth: **2,100 bullish / 4,109 bearish flow tickers (33.8% bullish)** across 6,209 names. Guidance: half position sizes, defined-risk, iron condors in range.

**Breadth narrative:** This is the key tension of the day. Price is near 90-day highs in a defined uptrend, but **both** breadth lineages agree the tape underneath is weak — UW flow breadth 33.8% bullish, Finviz advance/decline **200 up / 300 down (39.8% green), avg −0.48% / median −0.43%**. A market near highs being carried by a shrinking cohort is the classic late-cycle / narrow-breadth signature. Not a clean "green index, weak breadth" divergence (today's tape was itself modestly red), but the **price-vs-breadth divergence is real** and argues for defense.

**Per-index gamma (current-state EOD book; §2 carries the forward read):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 754.65 | null (unreliable) | **−796.7M** | **FULLY_NEGATIVE (short-γ)** | 760 | 740 |
| QQQ | 744.22 | 207 (unreliable) | **+88.9M** | POSITIVE (long-γ, thin) | 750 | 742 |
| IWM | — | whipsaw | −590M (6/03) | choppy / flip-prone | — | — |

**`uw options-flow dte-volume-share`:** 0DTE 29.2% / weeklies 25.5% / monthlies **30.6%** / LEAPs 6.5% — **BALANCED**, monthlies highest (some institutional positioning present, not a retail-dominated tape).

**`uw historical vrp` (SPY):** **FAIR**, VRP +0.04 (IV30 13.6% vs realized 9.6%). IV modestly rich but no clear premium-sell or premium-buy edge.

**Macro backdrop (`scripts/fred_macro.py`):** Yield curve **NORMAL** (+0.41 10y2y); **core CPI 2.99% / core PCE 3.29% YoY (sticky ~3%)**; unemployment 4.3%, payrolls +115k (soft); **10Y 4.46% RISING** (+0.07/30d); USD weakening; fed funds 3.62%. A sticky-inflation, cooling-labor, rates-drifting-up backdrop. **Forward event risk (next ~10 td):** jobless claims 6/4 (LOW) · **NFP 6/5 (HIGH — 2 sessions out)** · **CPI 6/10 (HIGH)** · PPI 6/11 (MED) · **FOMC + SEP 6/17 (HIGH)**. A macro gauntlet — every swing sized today eats NFP in two sessions.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book (OI persists overnight) read forward as the *prior* for the next open. Prose-only, **0 rubric points**, no backtested predictive claim (validation lives in `/weekly-analysis` §2). SPY/QQQ only.

The two indices are **split-regime** into the open, and **both ZGLs are unreliable**. SPY's EOD book is **FULLY_NEGATIVE** (short-gamma, every strike 733–757 net-negative, ZGL null) — dealers amplify direction; a move that extends gets chased, not faded. QQQ is the mirror: a **modestly POSITIVE** book (+89M, mild long-gamma / mean-revert bias) but spot 744.22 sits directly on top of a 742 negative pocket, one bad tick from flipping short. Critically, **SPY's regime is freshly flipped and historically unstable** (crossed zero-gamma almost every session: P 5/28 → N 6/01 → P 6/02 → FULLY_NEGATIVE 6/03) — do not treat today's short-gamma read as durable. QQQ's POSITIVE regime has held since the 5/22 flip and is the more trustworthy prior.

| Index | Regime | Spot · ZGL | Call wall | Put wall | One-line structure bias (next-session 0DTE) |
|---|---|---|---|---|---|
| **SPY** | SHORT-γ (FULLY_NEGATIVE, −797M) | 754.65 · null (`zgl_reliable=false`) | **760** (+116M; cap/magnet, +0.71%) | **740** (−122M; air-pocket, −1.94%) | Dealers amplify below 760. Debit verticals / directional 0DTE on a break; long straddle to own expansion. **Do not sell the straddle naked.** Half-size. |
| **QQQ** | LONG-γ (POSITIVE, +89M, thin) | 750 (+71M, +0.78%) | **742** (−58M; spot sits on the flip, −0.30%) | Pin 742–750 while it holds → iron fly / butterfly ~744. Flip to directional if 742 breaks (joins SPY short-γ). FAIR VRP = no premium tailwind, keep small. |

**Net desk read:** range-with-downside-tail. QQQ pins while it holds 742; a 742 break + SPY toward 740 is the scenario where both go short-gamma and trend together.

**Mandatory caveats:** (1) EOD is a *prior*, not a target — fresh 0DTE OI re-prices the ZGL/walls in the first 30–60 min. (2) **ZGL unreliable on both** (SPY null on FULLY_NEGATIVE; QQQ 207 = deep-OTM extrapolation) — fall back to total_gex sign + spot-vs-wall. (3) **Gap risk voids the prior** — NFP Fri 6/5 (2 sessions out) can gap spot through the walls before any hedging engages. (4) Tooling: uw cannot isolate the D+1 expiry — this is the standing 0–45 DTE book. (5) ETF book, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — the validated stack)

Backtest verdict **GO_PREMIUM_SELL_INTRADAY** (SPY open-win 97.3% / QQQ 94.6%, n=37 each) — advisory, **0 rubric points**, delta-neutral, NOT a guaranteed edge (validation sample has no vol shock; short-vol tail unsampled).

| Index | Sell premium? | Vol state | Implied / Exp range | Size scalar | Structure | Caution |
|---|---|---|---|---|---|---|
| **SPY** | yes | LOW (VIX 16.06) | 0.82% / 1.05% | **0.5** | Wider iron condor, wings ≈ ±1.05% (short-γ: wider/trendier) | — |
| **QQQ** | yes | LOW | 1.37% / 1.17% | **0.25** | Iron fly / short straddle centred 743.62, wings ≈ ±1.17% (long-γ) | **Front-end backwardation 1.36× VIX → event/gap risk, half size** |

**Entry rule:** enter at/after the open once the overnight gap resolves; if it gaps beyond the wings, stand aside. Hold the 0DTE to the close — **never carry overnight**. **SPY ≈ SPX** (validated identical); **QQQ weaker** (Nasdaq index book unavailable) — lower confidence. Direction: none (delta-neutral). The GEX walls above are a *map*, not a pin.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

`dealer-positioning-strategist`: the dealer book flipped **defensive into NFP**. **No vanna-squeeze long exists anywhere in the universe** — the book is call-heavy into low VIX (a vanna *headwind*, not a squeeze), and the lone put-heavy name (GOOGL) is falling, so its squeeze isn't armed.

| Ticker | swing_bias | Driver |
|---|---|---|
| **QQQ** | SHORT-LEAN | GEX cushion 87% gone in 2d (+691M→+89M) + front-end ratio **1.136 PANICKED**, NFP T+2 |
| **SPY** | SHORT-LEAN | Confirmed broad FULLY_NEGATIVE gamma flip 6/03 (spot below flip, dealers amplify); front-end still flat 1.036 |
| **NVDA** | SHORT-LEAN | Falling 224→215 under a positive-DEX shell = distribution; call-heavy = no squeeze fuel (cleanest single-name) |
| **MSFT** | SHORT-LEAN | GEX halving (+268→+111M) while spot −34pts — same compute-sell signature |
| **GOOGL** | NEUTRAL / squeeze-WATCH | Lone put-heavy book; latent vanna-buy *if* price stabilizes + own-IV falls — NOT armed today |

**Flat / no dealer thesis:** IWM (chop), AVGO / MRVL / MU / SNDK (parabolic momentum, negligible gamma — these are flow/momentum names, not dealer-mechanics names). The index complex is **short-gamma and vol-expansion-prone for the next 1–2 weeks**, NFP-gated.

## 2b. Sector Rotation

`sector-rotation-strategist`: **rotation_regime `growth→value` (medium confidence).** Value/commodity bid (Energy, Materials, regional Financials) while growth-cyclical de-risks (Discretionary, Industrials, and the **mega-cap AI-compute** sub-sector of Tech). Caveat: every GICS sector reads persistence_score 1.0 (sign-consistent INFLOW on a rising tape) — non-discriminating; the **discriminating signal is the ETF instrument tape + Δ-flow**, below.

- **Rotating IN:** Technology **software** (IGV institutional, monthlies 62.6% / 0DTE 0%) — leaders SNDK, MU, LRCX, WDC, GLW, APP; **Energy** (OXY, XOM, VLO, MPC, COP); **Basic Materials** (MOS, DOW, NUE); **regional Financials** (KRE).
- **Rotating OUT:** **Consumer Cyclical** (AMZN, TSLA, F, CMG — XLY put-confirmed BEARISH); **Industrials** (BA, RTX, GWW, CMI — XLI put-confirmed BEARISH); **mega-cap compute** (NVDA, AVGO, ASML, MSFT, GOOGL); **Utilities** (XLU bearish).

**ETF flow tape (advisory — strengthens the conditional sector-leader +1, no new points):**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| IGV | inflow | BULLISH 5d | accumulation $66.9M ask-side | moderate-bullish (Jun-100C, Jan LEAP build) | **agree** (Tech sw) | SNDK, MU, LRCX, WDC |
| XLE | inflow | BULLISH 5d | $270.6M ask-side block | moderate-bullish | **agree** (Energy) | OXY, XOM, VLO, MPC |
| GDX | inflow | BULLISH 5d | **hedging/redemption** $82M below-mid | **mixed — puts bid** | agree (downgraded) | (miners; broad-Mat separate) |
| KRE / EWT / TAN | inflow | BULLISH 5d | rank-only | rank-only | agree / n/a | — |
| XLY | outflow | **BEARISH 5d** | light | bearish (Sep 112.5P ask-bought) | **agree** (Discretionary) | AMZN, TSLA, F, CMG |
| XLI | outflow | **BEARISH 5d** | light | bearish (Jul/Jun/Sep puts ask) | **agree** (Industrials) | BA, RTX, GWW, CMI |
| XLU | outflow | **BEARISH 5d** | light | weak-bearish | **agree** (Utilities) | — |

**Key cross-check:** GICS persistence reads INFLOW (=1) for Discretionary/Industrials/Utilities, but the **ETF options tape reads persistent BEARISH** for XLY/XLI/XLU — the higher-resolution read, and exactly the divergence the ETF layer was built to catch. **GDX downgraded** (cum-flow bullish but options dominated by bought puts = hedging, not miner accumulation).

---

## 3. Swing Setups (1–6 weeks)

Ranked by conviction score. **This is a half-size, defined-risk regime two sessions before NFP** — the combined QQQ front-end panic (−1 to all) + NFP-at-T+2 event gate (−1 to all swings) imposed a −2-tier book-wide brake before any name-specific gate. **Only one name survived to a live (defined-risk) size.**

| Ticker | Score | Dir | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|---|
| **SNDK** | 8 (MED) | LONG | Cleanest flow-confirmed accumulation; memory/storage is the one BID theme; +$1.29B 30d, 5/5 OI build, fundamentals CONFIRM | **Bull put spread** below 1788–1800 DP shelf (sell rich IV, defined-risk); post-NFP entry | Loses the **1788 DP shelf** | **STARTER / defined-risk only** |
| NVDA | 6 (LOW) | SHORT | Dealer distribution under positive-DEX; −$210M/−$322M flow; but fundamentals fight it (strong-buy, +44% to target) | (watch) defined-risk put spread only | Reclaims 224 w/ GEX expanding | **SKIP / watch** |
| MRVL | 4 (LOW) | LONG | Momentum/semicap leader; +$140M flow — but C2 **beta** (no alpha), RSI 87, +22% past target, parabolic +61%/10d | (watch) | Loses the breakout / 30-min tape flips | **SKIP / watch** |
| INTC | 3 (LOW) | LONG | Single-agent 150C 6/18 +49k OI build; +$155M flow — but unprofitable, HOLD-rated, on the SOLD side of the theme | (watch) | 150C OI stalls/bleeds | **SKIP / watch** |
| CMG | 3 (LOW) | SHORT | Confluence-5 + NFP-dated put diagonal; fresh MS downgrade ($49→$37); −12%/3d — but RSI 27 oversold, 2.56 d-to-cover | (watch) defined-risk put diagonal | Reclaims SMA20 / risk-on NFP squeeze | **SKIP** |

### 3a. Long swings (regime-aligned)
- **SNDK (the one live name).** Accumulation-hunter's #1: institutional DP mega-buy (1.00), institutional-accumulation 1.27, **5/5 BUILDING OI**, distribution_flag FALSE, **+$1.29B 30d / +$1.54B 90d** cum-premium accretion (84% landed in the last 30d — accelerating). Fundamentals **CONFIRM** (4/4 beats, rev +82.8%, fresh Morgan Stanley PT→$1,750 on 6/03). Deep-dive: long-dated **2400C/2700C Dec-2028** accumulation alongside near-dated 1600P/1550P protection on the rip. The honest caveat the bear landed: **price ~$1,831 is ~3% PAST the $1,775 consensus target, RSI 74, +31.5%/10d** — extended, no squeeze floor (short float 6.25%), and the win-rate is an unvalidated proxy (0.64, n=14). **Structure:** bull put spread below the **1788–1800 DP shelf** monetizes the rich IV (IVR 76, IV30 ~100%) with defined risk; keep it small and prefer post-NFP entry. *MU and WDC accumulation is real (inst-accum 1.78 / 1.27) but the quant's C11 conjunction correctly stripped both — cum-flow does not confirm (WDC −$18.5M opposing & sub-$50M; MU +$30.1M sub-$50M + **distribution_flag TRUE**: $283.5M call-OI closing). SNDK is the only flow-confirmed storage long.*
- **MRVL / INTC** — long theses present but gated to watch: MRVL is C2 **beta** (−0.077 excess, no alpha vs SPY-long), parabolic into RSI 87 with today's tape turning bearish (huge 6/5 167.5P build); INTC is single-agent, unprofitable, HOLD-rated, and on the *sold* side of the theme.

**Distribution caution (C28):** MU carries a `distribution_flag` — ⚠ $283.5M call-OI being closed (advisory, 0 points, does not change sizing); dwarfed by the build but a fray on a crowded long.

### 3b. Short / fade swings (defined risk only)
- **NVDA (cleanest single-name short, but gated SKIP).** Dealer-positioning's top short — falling under a positive-DEX shell (distribution), call-heavy (no squeeze fuel), −$210M/−$322M multi-horizon flow, #1 bearish on the tape (−$179M today), rotation OUT of mega-cap compute. It is the **only top-5 name with positive market-excess (+0.052 alpha)**. But it lost its debate (bear 0.75 ≥ bull 0.55), fundamentals are pristine (CAUTION −1: strong-buy, +44% to target, +71% rev, +110% EPS), C4 shows the OI build is call-dominant (short *not* opening-confirmed), and IV is *falling* (61→41, slow distribution, no panic). A pure positioning short into a fundamentally bid mega-cap, two sessions before NFP — **watch, not a live short.**
- **CMG (best short *structure*, gated SKIP).** The only confluence-confirmed name (signal-confluence 5), C4 opening-short CONFIRMED (P25 6/17 +31.9k opening), NFP-dated bearish put diagonal, fresh MS downgrade ($49→$37), below all SMAs, Consumer-Cyclical rotating out. But it lost its debate (tie → bear≥bull), and the entry is hostile: **RSI 27 oversold, highest days-to-cover in the book (2.56), +49% analyst upside** = squeeze fuel into a risk-on NFP. Direction right, timing wrong — defer.

### Near-term sweeps (`sweep-tracker` — informational, 0 rubric points)
Only **4 names** carry a clean persistent (≥3/5) + opening-confirmed + direction-agreeing read: **MRVL (long, 5/5, $1.95B), INTC (long, 5/5, 150C +49k OI), NOW (long, 3/5), DELL (short, 3/5, put-build).** The highest-information signal is the **conflict cohort**: **MU and SNDK** — the crowded memory longs — saw **fresh put-opening today** against their 5/5 bull streaks (hedging/fade into NFP; "do not chase the breakout long here"). No mega-cap earned a directional slot (all hedge-flow / synthetic-contaminated). A VIX 6/17 call ladder confirms desks are buying tail protection into FOMC.

---

## 4. LEAP Builds (6–24 months)

**`leap-positioning-radar`: ZERO qualifying candidates.** No ticker passes the 6-of-9 gate stack; the binding filter is conviction-matrix (every single-name LEAP-DTE build resolved **COVERED_CALL / DISTRIBUTION / MIXED**, none DIRECTIONAL_LONG >70). The long-dated tape is a hedging/yield book (EEM/QQQ/HYG/XLU/FXI/LQD puts; UVXY/VIX; covered-call writing on SOFI/AUR/BNO).

**Compute mega-caps (mandated call-vs-put check):** none show a bullish LEAP call build — their long-dated positioning is the Tier-2 **PUT** accumulation flagged in Step 0, correctly NOT labeled bullish. 90d cum-flow confirms no accretion: NVDA −$322M, AVGO +$79M MIXED (dte597 puts), MRVL +$134M MIXED (dte170 puts), LRCX +$55M MIXED (dte597 puts), CRM −$1M flat. **Near-misses:** AUR (COVERED_CALL 55.8 + C12 fail), SOFI (COVERED_CALL + −$45M flow), VALE (DISTRIBUTION), NU (MIXED 2.5), LYV (DISTRIBUTION + −$7.6M). **No LEAP positions to size today.**

---

## 5. Volatility Surface

**`vol-surface-scout`: NO clean calendar candidates; stand aside.** The entire scanned universe is BACKWARDATION — but that is the *expected* macro-week shape (NFP 6/5, CPI 6/10, FOMC 6/17), front-end index IV elevated for scheduled macro, not dislocated. VRP FAIR (+0.04) gives no sell-vol tailwind.

- **IV-outlier bucket EMPTY** — all 0DTE noise + sub-$5 lottery calls; no liquid single-name whale-hedge mispricing.
- **Semis IV bid across the complex (IVR 100):** MRVL, SOXX/SOXL, AI, HON, VSH, AOSL, ICE. **MRVL and SOXL are momentum melt-ups, NOT vol sales** — front-end ratios *rising* (MRVL 1.71, SOXL 1.81) into parabolic moves; selling that gamma is selling in front of a chasing tape.
- **ICE** is the only falling-ratio name (1.39→1.30) but fails the structural test (premium massed in the 9/18 back-month, front 6/5 a put-skewed afterthought) — not a clean calendar.
- **Advisory — COMPLACENT skew composite (0 points):** APTV/MRVL/AI/HON/ICE print negative back-month skew (calls bid, downside unpriced) — lottery-profile crowded-call buying. No scored −2 fade (regime is UPTREND). Routed to the quant's C13 router so it does not stack with the contrarian line.

---

## 6. Risk & Correlation

`risk-monitor` consuming today's candidate union + the quant's audited score (not the static watchlist).

**Macro headline:** sticky ~3% core inflation (core PCE 3.29%), cooling labor (+115k payrolls), 10Y 4.46% rising, USD weakening. **Forward event risk:** **NFP 6/5 (HIGH, T+2)** · CPI 6/10 (HIGH) · PPI 6/11 (MED) · **FOMC+SEP 6/17 (HIGH)**. NFP is inside every swing horizon today.

**Breadth cross-check (advisory):** Finviz 200 advancers / 300 decliners, **pct_green 39.8%**, avg −0.48%. Confirms the weak-breadth read (agrees with UW 33.8% bullish). `divergence_flag=false` (the tape itself was modestly red, not a green-index/weak-breadth split) — but the **price-vs-breadth divergence** (near 90d highs, weak internals) is the structural distribution tell. Advisory; does not change sizing.

**Gates applied (the −2 book-wide brake):**
- **Front-end-IV panic:** QQQ ratio **1.136 (BACKWARDATION >1.10) → −1 tier to the entire book** (panic is tech/QQQ-localized; SPY 1.036 is calm, so the broad hedge is cheaper than the QQQ-specific one). The semis-heavy book references the panicked QQQ.
- **Event-risk gate:** NFP at **T+2 → −1 tier on every directional swing** unless explicitly defined-risk through the print.
- **VRP gate:** no-op for all 5 (no name is a vol structure; FAIR VRP). Stated per gate-discipline.
- **Regime gate:** no-op — longs align with UPTREND, shorts align with the compute-SOLD / Discretionary-OUT sub-regimes (not −3).
- **Fundamentals:** **−1 each on NVDA, MRVL, INTC (CAUTION)**; SNDK/CMG CONFIRM (0). No VETOs.
- **Debate:** **−1 each on NVDA, MRVL, INTC, CMG** (bear residual ≥ bull). SNDK clears (bull 0.75 > bear 0.65).

**Correlation clusters (`uw risk portfolio-correlation`, mechanical):** The only pair ≥0.70 is **SNDK/MU 0.719** — but MU is watch-only, so no active-book deduction. Among the active top-5 the max pairwise corr is SNDK/INTC 0.525. Soft-watch (0.60–0.70): INTC/SMH 0.663, MU/SMH 0.662, MU/WDC 0.655, WDC/SMH 0.612. **Cluster gate does not fire** (per 2026-05-15 P1.4 discipline — no discretionary upgrade of the "all semis" intuition). **But the concentration risk is the dominant book risk, flagged separately:** 4 of 5 top names + every watch name are **semis/memory (100% one sector)**, and SNDK sits inside a CONFIRMED-DISTRIBUTION complex (SMH +143k puts). Do not treat SNDK + any semis revival as independent risk.

**Fundamentals verdicts (top-5):** SNDK **CONFIRM**; NVDA **CAUTION** (strong-buy +44% to target fights the short); MRVL **CAUTION** (RSI 87, +22% past target); INTC **CAUTION** (HOLD-rated, unprofitable, +14% past target); CMG **CONFIRM** (fresh MS downgrade, broken technicals — but RSI 27 / 2.56 d-to-cover bounce risk).

**Adverse-flow exit list (yesterday's `conviction_2026-06-02` = TSLA/AMD/MRVL/SNDK/AVGO):**
- **AVGO → EXIT** (flow flipped bearish −$20.4M, IVR 88.6, $256M DP block).
- **AMD → EXIT** (bearish −$14.9M, IVR 92.3, $256M DP block).
- **MRVL → off-thesis** (today's flow bearish −$4.3M vs the long it was scored on — also gated SKIP).
- **TSLA → monitor** (mixed). **SNDK → confirms carry** (flow bullish +$92.5M — the only carried name whose flow confirms its thesis).

**Hedge sleeve:** directional-skew hedge **NOT triggered** (one defined-risk starter = small net delta). The real book risk is the tech/QQQ tail + concentration: **if the book grows beyond SNDK, pair it with a QQQ 1–2-week put spread through NFP** (panic is QQQ-localized; QQQ near-IV rich at 27% so prefer a spread over outright puts). VIX 16.06 is cheap left-tail insurance into the gauntlet if the book scales.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: per the most recent `/calibration-audit` (2026-05-30), the realised per-tier read was **HIGH (≥9) ~0.77 / MED (7–8) ~0.54 / LOW ~0.50** (in-sample, single UPTREND regime), and benchmark-excess showed **longs ≈ −22pp (beta) vs shorts ≈ +20pp (alpha)**. Today's book reproduces that signature exactly: the bullish_flow longs (MRVL/INTC) scored as **beta** (market-excess −0.077), while the lone short with measured edge (NVDA) carried **+0.052 excess** — yet its *expression* still died on the gate stack. The live sizer remains the win-rate ladder (Step 5); this is display-only context to keep the desk honest about where the book's edge actually lives.

Only **SNDK** clears raw_score ≥ 7.

### SNDK — LONG — raw_score 8 — MEDIUM — final size STARTER (defined-risk only)
- **score_components:** `+3` accumulation 3+ aligned [C11 conjunction FULL] (accumulation-hunter / `institutional-accumulation`) · `+3` cum_premium_flow 30d net accretion +$1.29B (quant / `cumulative-premium-flow`) · `+1` multi-day OI build 5/5 (accumulation-hunter / `oi-trend`) · `+1` sector single-name leader (sector-rotation / `sector-flow-persistence`). **Σ = 8.** ✓
- **dominant_signal_class:** dark_pool_accumulation · **confluence_score:** not-listed (flow tools confirm; second-agent confluence does not)
- **cum_premium_flow:** 30d **+$1,293.5M** / 90d **+$1,542.5M** · **win_rate 0.6429 (n=14, FALLBACK_PROXY — backtest returned 0 signals, capped 0.65)**
- **pre_risk_size:** half → **final_size: STARTER / defined-risk only**
- **gate_verdicts:** regime no-op · vrp no-op · **panic −1** (QQQ 1.136) · cluster no-op (SNDK/MU 0.719 but MU watch-only) · sector no-op (Tech INFLOW 1.0) · **fundamentals CONFIRM (0)** · **event_risk −1** (NFP T+2; waived iff defined-risk through NFP) · **debate no-op** (bull 0.75 > bear 0.65, CLEARS)
- **fundamentals_verdict:** CONFIRM · **debate_residual (bull):** 0.75
- **fz_context:** short float 6.25%, days-to-cover 0.57, float 146.1M, recom 1.61 (buy), RSI 74.2, **−3.1% to target (price past target)**, squeeze LOW — advisory, 0 points
- **structure:** Bull put spread below the 1788–1800 DP shelf (sell rich IV, defined-risk) · **entry/trigger:** small, prefer post-NFP open · **invalidation:** loses the **1788 DP shelf**
- **key_risks:** parabolic extension (RSI 74, +31.5%/10d, price past target, AI-bubble framing); semis/memory concentration (correlated to MU/MRVL/SMH); SMH-complex CONFIRMED DISTRIBUTION overhead; unvalidated proxy win-rate
- **thesis:** The cleanest flow-confirmed accumulation on the tape, in the one BID theme (memory/storage), fundamentals and a fresh sell-side catalyst both aligned — but it has already run, so size it as a small defined-risk starter that monetizes the rich IV rather than chasing spot.

**Below-threshold names (LOW, raw 3–6) carried at watch** for tomorrow's correlation/adverse-flow loop: NVDA (6, short), MRVL (4, long), INTC (3, long), CMG (3, short) — all gated **SKIP/watch** (see §3, §6).

### Conviction-scoring rubric (Step 4, verbatim for audit)
```
Daily conviction score = Σ:
 +3 dealer-positioning DEX flip / vanna-squeeze in trade direction
 +3 accumulation 3+ aligned (DP+OI+smart-positioning, block-stratified inst-tier) — C11: full +3 only when cum_flow_30d sign-aligned AND |cum_flow_30d|≥$50M; else +1
 +1 multi-day OI build (oi-trend BUILDING, --days ≥5)
 +1 conviction-matrix DIRECTIONAL_LONG conf>70 — CONDITIONAL: only when dominant_signal_class==leap_directional; else 0
 +3 cum_premium_flow net directional accretion (30d)
 +2 signal-confluence ≥4 (second-agent confirmation)
 +1 sector single-name leader — CONDITIONAL: persistence≥0.6 AND cum_flow_30d aligned AND ≥$50M
 +1 earnings-scout BUY VOL / SELL VOL
 +2 multileg directional structure (term-structure-anchored)
 +1 vol-surface KINKED/BACKWARDATION with VRP-aligned bias
 +1 opex-pin top-5 (OPEX week only)
 -2 contrarian overcrowded long + rising pc-ratio-zscore (VRP positive)
 -3 flow_conflict (30d cum-flow clearly opposite dominant_signal_class) | -1 flow_conflict_lite (MIXED) — mutually exclusive
 -1 correlation cluster (corr>0.7) [risk 2d] · -3 regime conflict [risk 2d]
 # sweep-persistence = 0 points (removed P0.3); §2 GEX = 0 points (advisory)
Tiers: ≥9 HIGH (full) · 7–8 MED (half) · 3–6 LOW (starter/watch) · ≤2 drop
Sizing ladder (win_rate): ≥0.70 full · 0.50–0.70 half · <0.50 starter/skip. Guards (downgrade-only): C2 market-excess + n<10 cap 0.69; C4 OI-opening; C12 liquidity floor.
```

---

## 8. Watch-only — single signal / dropped / no confluence

For journaling, **not** for trade entry today.

- **WDC** (long, raw 1) — accumulation real (inst-accum 1.78, cleanest no-distribution) but C11-halved: cum-flow −$18.5M opposes & sub-$50M. The storage long the flow does *not* confirm.
- **MU** (long, raw 1) — C11-halved (+$30.1M sub-$50M) + **distribution_flag TRUE** ($283.5M call-OI closing) + put-build today. Two-sided.
- **MSFT** (short, raw 0) — canonical **flow_conflict −3**: dealer GEX-halving says short, but +$454.2M 30d bullish flow (3.1× union-median) opposes. Do not size.
- **GOOGL** (short, raw 1) — dealer NEUTRAL/squeeze-WATCH contradicts the short (latent long); −$262.8M flow but sector +1 withheld.
- **CPB** (short, raw 2) — earnings SELL VOL (6/8), only positive back-tail skew, but 2.2% move; sub-threshold.
- **ORCL** (SELL VOL, raw 1) — earnings vol play (6/10, 9-DTE IV hump 119.8%, back-tail COMPLACENT, bearish flow −$32.9M divergence). Highest-EV *vol* name but non-directional, confluence 3.
- **SMH** (ETF) — **CONFIRMED DISTRIBUTION** (+143k OI all puts, inst-accum 0.73 sell) — the semis-complex hedging tell, not a long.
- **NBIS** (conflicting) — accum #4 spec vs sweep put-build vs −$27M bearish; net ambiguous.
- **Energy/Materials leaders** (OXY/XOM/VLO/MPC/MOS/DOW/NUE) — sector-rotation single-agent only; no confluence backing → watch.
- **DELL / NOW** (sweep-only) — DELL short put-build (3/5), NOW long call-build (3/5) but net premium −$17M bearish (flow conflict); single-agent.

---

*Generated by `/daily-analysis` — 10 Phase 1 agents (parallel) → quant → fundamentals → bull/bear debate → risk-monitor. opex-pin-strategist omitted (June OPEX 6/19, outside 5-day window). Watchlist `conviction_2026-06-03` = SNDK, NVDA, MRVL, INTC, CMG. No HIGH-tier names → no `/stock-deep-dive` hand-off.*
