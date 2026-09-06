# Step 0 shared context — 2026-08-10 (Monday)

**Every Phase 1 agent receives this verbatim. Read the cached files; do NOT re-issue cached commands.**

## Hard rules
- `uw <group> <sub> [--flags] --json --quiet` — `--json` mandatory, `--quiet` for pure JSON. Pin point-in-time tools with `--date 2026-08-10`.
- **NO re-fetching** `uw risk market-regime`, `uw playbook daily-synthesis`, `uw historical vrp`, `uw options-structure front-end-iv-ratio`, or **any** payload in the cache table below. Read the file.
- Prefer **multi-day persistence** over single-day: `historical oi-trend` > `oi biggest-increases`; `hot-chains sweep-persistence` > `options-flow sweeps` for ranking; `options-flow sector-flow-persistence` > `sector-flow`; `historical pc-ratio-zscore` (never `screener put-call-extremes`).
- `uw historical signal-backtest` is **QUARANTINED** — Phase 1 agents must NOT call it (quant only, under the clean-query protocol).
- `uw insights signal-confluence` is **funnel-seed only** — do not consult it at entry/scoring.
- **NO file writes. NO watchlist mutation.** Return your findings as your final message only. (risk-monitor is the sole exception, later.)
- Sort tie-prone lists by an explicit key — Go map order is non-deterministic.
- `screener iv-rank` takes **`--mode high|low`, NOT `--direction`**.

## Step-0 cache — read these paths
Base: `analyses/daily/2026-08-10/step0_cache/`

| logical name | file |
|---|---|
| daily_synthesis | `daily_synthesis.json` |
| market_regime | `market_regime.json` |
| dte_volume_share | `dte_volume_share.json` |
| sector_flow | `sector_flow.json` |
| sector_flow_persistence | `sector_flow_persistence.json` |
| screener_bullish / screener_bearish | `screener_bullish.json` / `screener_bearish.json` |
| signal_confluence_bullish / _bearish | `signal_confluence_bullish.json` / `signal_confluence_bearish.json` |
| iv_rank_high / iv_rank_low | `iv_rank_high.json` / `iv_rank_low.json` |
| volume_vs_average | `volume_vs_average.json` |
| earnings_catalyst | `earnings_catalyst.json` |
| expiry_heatmap | `expiry_heatmap.json` |
| iv_outliers | `iv_outliers.json` |
| greek_screener | `greek_screener.json` |
| top_premium_trades | `top_premium_trades.json` |
| most_active | `most_active.json` |
| oi_smart_positioning | `oi_smart_positioning.json` |
| single_leg | `single_leg.json` |
| vrp_spy / vrp_qqq | `vrp_spy.json` / `vrp_qqq.json` |

All 22 payloads fetched OK; `failed[] == []`.

---

## Regime
- **`uw risk market-regime`: TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity"**; `trend: UPTREND`.
- SPY **773.03**, above 20SMA (751.37) and 50SMA (747.56), +2.39% 30d, −0.49% from 90d high.
- Market breadth (UW): **34.9% bullish-flow tickers** (2,190 bullish / 4,091 bearish of 6,281 optionable).
- Guidance: "Half position sizes. Favor defined-risk strategies. Iron condors in range."
- **VIX 15.46** (LOW vol state).

## Tape framing — THIS IS A ROTATION DAY, NOT A DISTRIBUTION DAY
Read this before writing any directional call. Cap-weighted vs equal-weight (raw Yahoo OHLC, `--as-of 2026-08-10`):

| | 1d% | 5d% | rv20% |
|---|---|---|---|
| SPY | **−0.03** | +2.03 | 13.6 |
| QQQ | **−0.30** | +2.97 | 24.5 |
| IWM | −0.52 | +1.27 | 15.0 |
| RSP (equal-wt) | **+0.06** | +1.43 | 10.6 |

**RSP ≥ SPY > QQQ** — equal-weight beat cap-weight. The red is concentrated, not broad.

Sector ETFs 1d%: **XLE +4.66**, **XLV +1.67**, XLB +0.61, XLC +0.52, XLF +0.36 | XLY −0.16, XLP −0.20, XLI −0.31, **XLK −0.88**, **XLU −1.10**, **XLRE −1.29**.

**What was sold — the AI/semis/optics complex (one-day reversal off a strong week):**
COHR **−14.24%** (5d +12.84), LITE −8.61 (5d +4.31), SOXL −7.31 (5d +11.39), IREN −6.04, WULF −5.15, RIOT −5.46, MRVL −4.65 (5d +7.63), FSLR −4.29, INTC −4.06 (5d +7.16), RKLB −3.37, NVDA −2.86 (5d **+5.28**), AMD −2.86, CRWV −2.74, **SMH −2.28** (5d +4.39), MU −1.89 (5d +3.80), AVGO −1.25, EWY −1.79.
→ Note the 5d column: almost every semi is **up** on the week. Today is a reversal, not an established downtrend. Do not extrapolate a trend from one session.

**What was bought:**
Energy — USO +6.73, RIG +8.75, BOIL +8.32, CRK +7.08, NE +6.82, WHD +4.67, BTU +3.53.
Precious metals — AGQ +6.53 (5d +27.56), SLV +3.32 (5d +13.25), SIVR +3.27, HL +4.15 (5d +21.62), GLD +1.02 (5d +8.29), GFI (5d +21.02), AG +2.45 (5d +20.06).
Healthcare — LLY +3.90 (5d +9.86), RDNT +6.76 (5d +15.69).
Software/security (NOT semis) — PANW +5.82 (5d +10.92), CRWD +5.01 (5d +11.17), ORCL +2.74, NOW +2.05, MSFT +1.21, UBER +4.01, BABA +3.04, CHYM +6.01 (5d +27.16), BSP +15.70 (5d +41.99).

**The intra-tech split is the day's real story:** MSFT +$51.5M net premium and +1.21% price, while NVDA −$49.0M / MU −$38.7M / TSM / AVGO / MRVL / ASML / INTC / SNDK are all net-bearish. Software bid, semis sold.

## Vol / VRP
- **SPY VRP: FAIR** (−0.0016) — IV30 13.04% vs realised30 13.20%. No VRP edge from SPY alone.
- **QQQ VRP: PREMIUM_BUYING** (−0.0503) — IV30 **20.43%** vs realised30 **25.46%**. Nasdaq is moving MORE than options imply. Confirmed independently by QQQ rv20 24.5%.
  → In a premium-BUYING tape, weight `gamma-flip-tracker` / `earnings-scout` (long premium) above premium-selling theses on QQQ names. Long vol on Nasdaq single names is comparatively cheap.
- **DTE volume share: 0DTE 34.9% · weeklies 25.0% · monthlies 24.9% · LEAPs 3.9% → `regime_hint: BALANCED`.** Monthly+ = 28.8% institutional. Neither retail-dominated nor institution-dominated — no benefit-of-the-doubt in either direction.

## Sector layer — READ DIRECTION OFF THE NETTED SOURCE ONLY
**`sector_flow_persistence` is GROSS TURNOVER, sign-agnostic. It returned `trend: INFLOW`, `persistence_score: 1` for ALL 11 sectors — zero discrimination. It is a DURABILITY filter only. It and `sector-flow` are ONE gross source and cannot express direction (2026-07-31/08-01 C55).**

**Netted directions — `market_regime.sector_rotation` (the ONLY netted source):**
- IN: **Financial Services +$37.4M**, **Healthcare +$26.3M**, **Energy +$20.4M**
- OUT: **Technology −$279.9M**, Communication Services −$26.7M, Utilities −$24.7M

**Gross-vs-netted DISAGREEMENTS (⇒ `watch_only`, per C55):**
- **Technology**: gross +$3.68B INFLOW (largest) vs netted **−$279.9M OUTFLOW**. Directly contradictory. Netted wins; conviction is watch_only.
- **Communication Services**: gross +$646M IN vs netted −$26.7M OUT → watch_only.
- **Utilities**: gross +$57.7M IN vs netted −$24.7M OUT → watch_only. (Corroborated by price: XLU −1.10%, 5d −2.77%.)
- **AGREE (both IN)**: Financial Services, Healthcare, Energy. These are the only three sectors where gross and netted point the same way — and all three are confirmed by price (XLF +0.36, XLV +1.67, XLE +4.66).

## Macro snapshot (`scripts/fred_macro.py`, available=true)
- Yield curve **normal**, 10Y−2Y **+0.47**
- Core CPI **2.81% YoY**; Core PCE **3.29% YoY** (headline CPI 3.73%, PCE 3.67%) — core PCE still well above target
- Unemployment **4.1%**; payrolls **−23k MoM** (July) — outright contraction
- 10Y **4.65%**, **rising** (+9bp/30d); 2Y 4.19% (−2bp); USD **weakening** (−2.07/30d); Fed funds **3.63%**, SOFR 3.62%
- Read: sticky-core + negative payrolls + rising long end + weak dollar = stagflationary tilt. That is the macro reason XLU/XLRE are the worst sectors and gold/silver are the best.

## Forward event risk — TIER-1 STACK INSIDE 48 HOURS
| Event | Date | Impact |
|---|---|---|
| **CPI (July)** | **Wed 2026-08-12** 08:30 ET | **HIGH** |
| **PPI (July)** | **Thu 2026-08-13** 08:30 ET | **HIGH** |
| Retail Sales (July) | Fri 2026-08-14 08:30 ET | MEDIUM-HIGH |
| Initial jobless claims | Thu 08-13, Thu 08-20 | LOW |
| FOMC minutes (Jul 28–29 mtg) | ~Wed 2026-08-19 | MEDIUM |
| **Monthly OPEX** | **Fri 2026-08-21** | MEDIUM |
| Jackson Hole symposium | Aug 27–29 | MEDIUM |
| Core PCE | ~Fri 2026-08-28 | HIGH |
| FOMC decision | Sep 15–16 | HIGH |

**Any swing thesis carries a CPI print in 2 sessions.** Gate directional conviction accordingly; the GEX/0DTE prior is void on a CPI gap.

## `fz` lanes — ADVISORY, 0 rubric points (`fz_available = true`)
**⚠ THE UPSTREAM DOUBLED-FIRST-LETTER BUG IS LIVE ON EVERY `fz` SURFACE TODAY.** `AABEO`→ABEO, `CCRWD`→CRWD, `BBSP`→BSP. De-doubling verified by exact price cross-match (`BBSP` $51.43 = BSP $51.43 in `iv_rank_high`; `CCRWD` $225.16 = CRWD $225.16 in `screener_bearish`). **Never match an `fz` ticker with `==`.** Rule: if `t[0] == t[1]`, strip the first character.

- **Breadth cross-check:** advancers **230** / decliners **270**, `pct_green` **45.73%**, avg_change +0.01%, median **−0.17%**. Top mover DDOG +11.48%; worst COHR −14.24%.
  → `pct_green < 50` on a ~flat SPY. **Do NOT call this a distribution tell** — RSP is green and the decliners are concentrated in semis/AI-power + rate-sensitives (XLU/XLRE, consistent with 10Y +9bp). This is churn inside a rotation.
- **Squeeze lane (`sh_short_o20,sh_price_o5,sh_avgvol_o500`, de-doubled):** ABEO, ABR, ABSI, ACHC, AESI, AI, ALMU, AMCX, AMPG, AMPX, ANNX, APLD, ARDT, ARQQ, ARRY, ASAN, ASST, ASTS, AVBP, AVTX.
  **COVERAGE LIMIT:** all 20 rows are alphabetically-first A-tickers — this is a truncated page-1, not a ranked market-wide screen. Treat as a partial sample; it cannot claim to surface the top squeeze names. Most relevant given today's tape: **APLD** ($29.06, 26.6% short float — AI datacenter, into the selloff), **ASTS** ($68.76, 22.9%), **AI** ($10.40, 32.5%), **ASAN** ($9.23, 39.5%).
- **RS / new-high lane (de-doubled):** NESR, BSP, ABCL, TXG, TWST, LFST, ORKA, ADPT, QNST, BMRN, S, ABNB, AXGN, BFLY, CRWD, CAKE, and 4 unresolved (PCLA/BLSM/ADIG/NEWP).
  **Heavily Healthcare/biotech-tilted** — independent corroboration of the netted rotation INTO Healthcare. Also picks up **CRWD** (+5.01%) — the software-not-semis split again.

## Single-leg whale scan (`single_leg.json`) — advisory, **0 rubric points, permanently** (C19 CLOSED as REFUTED 2026-07-25)
Run at `--regime neutral` (TRANSITIONAL is not bull, so calls correctly label `CALL_UNVALIDATED` rather than being faded).
**25 signals — ZERO Tier-1.** No `OPENING_PUT_PRIME`, no `FLOOR_PUT_BLOCK`. Breakdown: 11 `OPENING_PUT_STRONG` (Tier-2, DTE>30, edge decays), 8 `CALL_UNVALIDATED`, 6 `PUT_CONTEXT`. Every row is `action: CONTEXT_ONLY`.
→ **The single-leg lane offers no edge today.** The long-dated put tickets (MSFT 680P 858dte, NVDA 450P 858dte, ADBE 450P 529dte, NET 440P 529dte, LITE 1110P 676dte, META 600P 403dte) are Tier-2 context at best. Do not build a thesis on them. Notable short-DTE rows: INTC 67.5P 39dte size/OI 13.5; TEAM 155P 39dte size/OI 56.
Do NOT report any rolling-WR figure as C19 accrual progress — the criterion is retired.

## Funnel — C12 liquidity floor APPLIED (price ≥ $5 AND 20d dollar-ADV ≥ $50M, fail-closed)
This floored set is the funnel. Every downstream step consumes it.

**PASS (candidate universe):**
`MSFT LLY COST LULU ORCL COIN SLV USO SE PANW EWY AMD DOCU NOW CRWV BABA UBER WULF SPCX SKHY SMH BRK-B SNDK NVDA MU LITE FSLR INTC TSM MRVL IBIT VST AMZN GOOGL ASML COHR CRWD SOXL IREN SPHR AVGO RKLB GLD DAVE HONA EXPE ARGX GFI RIOT AG HL ICLN VSNT BTU TTD RIG COGT AGQ SHAK RDNT CHYM ASH SONY NE ALLY SIVR WHD NVO PYPL UPST CMCSA ROKU GBTC ECHO BOIL UNG BIRK SOXS BSP` + ETFs `SPY QQQ IWM RSP XLK XLF XLV XLE XLU XLY XLP XLI XLB XLRE XLC`

**C12 FAIL — DROPPED from the funnel, do not analyse:**
COLM ($42.2M), BLBD ($40.3M), CWEN ($39.1M), AGIO ($42.3M), GRBK ($15.4M), BL ($32.0M), ODD ($11.3M), EVC ($16.0M), JANX ($11.5M), GO ($21.9M), CRK ($31.8M), NEO ($46.7M), AIRJ ($9.3M), GEO ($47.1M), HZO ($30.2M), SBET ($49.4M), TDOC ($47.1M), ALMS ($27.3M), AHCO ($25.0M), EYPT ($20.7M), MFP ($42.6M) — all sub-$50M ADV. MPT (price $4.15 < $5). `^VIX` ADV $0 — index, tape context only, never a candidate. Index symbols SPX/NDX/RUT/VIX/SPXW are option underlyings, not funnel candidates — use SPY/QQQ/IWM proxies.
**Also note:** `volume_vs_average` is unusable today — it returned micro-ETFs on 14–200 contracts of volume (HRZN1 ratio 1501 on 50 contracts; WDIV 14; IUSV 18; MUNI 23). Essentially the whole screen fails C12. Do not seed candidates from it.

## Funnel detail
**`screener_bullish` top net premium:** SPX +$215.9M, **MSFT +$51.5M**, RUT +$41.2M, LLY +$20.1M, WULF +$18.5M, COST +$17.8M, LULU +$16.7M, ORCL +$16.2M, SPCX +$14.8M, COIN +$14.3M, SMH +$14.2M, SLV +$14.0M, USO +$13.8M, BRK-B +$13.7M, SE +$13.7M, PANW +$10.4M, VIX +$9.9M, EWY +$9.6M, AMD +$9.4M, DOCU +$7.7M, NOW +$7.6M, CRWV +$7.2M, BABA +$6.9M, UBER +$6.2M, SKHY +$5.8M.

**`screener_bearish` top net premium:** NDX −$131.6M, **SNDK −$130.6M**, QQQ −$80.2M, SPY −$70.8M, GLD −$63.2M, **NVDA −$49.0M**, **MU −$38.7M**, LITE −$32.8M, FSLR −$32.2M, INTC −$31.6M, TSM −$28.7M, MRVL −$15.8M, IBIT −$13.8M, VST −$13.3M, AMZN −$13.1M, GOOGL −$10.6M, ASML −$9.4M, COHR −$8.3M, CRWD −$8.2M, SOXL −$7.4M, IREN −$7.1M, SPHR −$7.1M, AVGO −$7.0M, RKLB −$6.8M.

**Divergences worth checking (flow vs price):**
- **SNDK**: −$130.6M net premium (largest single-name bearish) yet price **+2.12%**. ⚠ **Known blind spot — check the `side` field and net-as-%-of-gross before trusting this.** On 2026-08-06 SNDK's "+$388M top bullish" was ONE bid-side deep-ITM put SALE (74% of net). The netting engine books put sales as directional premium. Verify before either direction.
- **CRWD**: −$8.2M net premium yet **+5.01%** and 5d +11.17%, and it appears in the fz RS new-high lane. Flow and price disagree.
- **GLD**: −$63.2M net premium yet +1.02% and 5d +8.29% with silver ripping. Likely upside call-spread financing / covered-call overwrite, not directional selling — verify structure.
- **AMD / SMH / WULF / CRWV**: net-bullish premium but red price today. Dip-buying vs failed rally — check whether the flow is opening (`oi-trend` BUILDING) or churn.

**`signal_confluence_bullish` (funnel seed only, 0 points)** — post-C12 survivors: BTU 6, TTD 6, RIG 6, COGT 6, AGQ 5, SHAK 5, RDNT 5, CHYM 5, ASH 5, UBER 5, SONY 5, NE 5, ALLY 5, SIVR 5, WHD 5. (ABAT/CIG/SIDU/PEPG/MRLN/JANX/GO/CRK/NEO/AIRJ dropped — sub-floor.)
⚠ **TTD** carries `dp_accumulation` at score 6 but is **−2.97% today and −26.83% over 5d** — accumulation into a collapse is the merger-arb/falling-knife blind spot class. Treat with suspicion; require the `block-stratified` institutional tier and check for a distribution signature.

**`signal_confluence_bearish`** — post-C12 survivors: DAVE 5, HONA 5, ICLN 5, GFI 5, EXPE 5, VSNT 4, ARGX 4, HL 4, RIOT 4, AG 4. Note DAVE 5d **−22.63%** and HONA 5d **−21.69%** are already broken (late), while GFI/AG/HL are precious-metals names showing "bearish flow" while price is up 20%+ on the week — that is very likely **hedging/overwrite against a big spot gain, not directional shorting.** Verify structure before calling them shorts.

**`earnings_catalyst`** (n=230) — **CORRECTED (an earlier draft of this file wrongly said dates were null; that was an extraction error on my part, caught by `earnings-scout`).** The field is **`next_earnings_date`** (not `earnings_date`) and it is **populated 230/230**, alongside `days_to_earnings`, `er_time`, `implied_move` (in POINTS) and `implied_move_perc` (a **FRACTION** — 0.11 = 11%; convert before emitting, the envelope wants percent).

### ⚠ THIS IS THE DAY'S BURIED LEDE — A DENSE EARNINGS CLUSTER LANDS TOMORROW, IN THE EXACT COMPLEX THAT SOLD OFF

| Ticker | Print | Time | DTE | IV rank | Implied move | Today 1d% |
|---|---|---|---|---|---|---|
| **SE** | **2026-08-11** | premarket | 1 | 78.7 | **11%** | +1.21 |
| **CAH** | **2026-08-11** | premarket | 1 | 81.3 | 6% | — |
| **CAVA** | **2026-08-11** | postmarket | 1 | 85.9 | **11%** | — |
| **SMCI** | **2026-08-11** | postmarket | 1 | 72.1 | **12%** | — |
| **LITE** | **2026-08-11** | postmarket | 1 | 64.8 | **10%** | **−8.61** |
| **CRWV** | **2026-08-11** | postmarket | 1 | 52.8 | **11%** | **−2.74** |
| **CSCO** | 2026-08-12 (CPI day) | postmarket | 2 | 90.6 | 7% | — |
| **COHR** | 2026-08-12 (CPI day) | postmarket | 2 | 73.6 | **10%** | **−14.24** |
| BIRK | 2026-08-13 | premarket | 3 | 100 | 10% | +3.30 |
| GDS | 2026-08-13 | premarket | 3 | 83.1 | 12% | — |
| HD | 2026-08-18 | premarket | 8 | 86.7 | 2.3% | — |
| KEYS | 2026-08-18 | postmarket | 8 | 81.6 | 9% | — |
| BHP | 2026-08-18 | unknown | 8 | 75.5 | 5% | — |
| TJX | 2026-08-19 | premarket | 9 | 90.4 | 2.4% | — |
| LOW | 2026-08-19 | premarket | 9 | 86.4 | 2.6% | — |
| ROST | 2026-08-20 | postmarket | 10 | 94.9 | 2.2% | — |
| DE | 2026-08-20 | premarket | 10 | 82.3 | 2.4% | — |
| AAP | 2026-08-20 | premarket | 10 | 80.5 | 4% | — |

**THIS RE-EXPLAINS TODAY'S TAPE. Read it before writing any thesis on the AI/optics complex.**
- **LITE −8.61% reports TOMORROW post-close** (10% implied move). Its −$32.8M bearish net premium and its **1.575 extreme front-end backwardation** are **earnings-event pricing, not a dealer-positioning or distribution story.** Its DEX sign-flip-below-floor is event-driven.
- **COHR −14.24% (the S&P's worst mover) reports 08-12 post-close** (10% implied move, front-end ratio **1.727** — the most extreme screened). COHR fell 14% **into its own print**, in sympathy with LITE. That is pre-earnings de-risking, **not** institutional distribution.
- **CRWV −2.74% and SMCI both report tomorrow post-close** (11–12% implied moves).
- ⇒ **A large part of today's semis/optics selloff is pre-earnings de-risking ahead of a dense 08-11→08-13 print cluster, stacked on top of CPI Wednesday.** That is a materially better explanation than "the AI trade is breaking," and it is consistent with the 5d column being green across the complex. **Do not write a distribution thesis on LITE / COHR / CRWV / SMCI.**
- **NOT reporting inside 14 days** (absent from the screen): NVDA, MU, AMD, MRVL, AVGO, TSM, INTC, ASML, FSLR, SNDK, MSFT, ORCL, NOW, PANW, CRWD, COIN, UBER, LLY, TTD, WULF, IREN, RIOT, SPCX, VST. So the mega-cap semis have **no** near-dated event — their weakness is not earnings-driven, and any backwardation there is NOT event-explained.
- The mid-August **retail cohort** (HD/LOW/TJX/ROST/AAP) is the second block, and its implied moves are small (2.2–2.6%). **Retail Sales Fri 08-14 is a direct sector read-through that lands before all of their prints** — separate that macro leg from company premium.

**`iv_rank_low` (premium-buying candidates, post-C12):** SKHY, NVO, PYPL, BOIL, UPST, UNG, CMCSA, ROKU, GBTC, ECHO. `iv_rank_high` is almost entirely sub-floor microcaps (RCON $0.036, NVX $0.448, SKYE $0.53, TENX $1.375) — only SOXS, BSP, BIRK survive C12.

## Next-session 0DTE setup (`zerodte_setup`, advisory, 0 points)
`backtest.verdict: GO_PREMIUM_SELL_INTRADAY`. Delta-neutral premium selling only — no directional tilt.
- **SPY**: sell_premium=true, vol_state LOW, VIX 15.46, implied_move 0.63%, expected_range **0.82%**, size_scalar **0.5**, structure = iron fly / short straddle centred **772.82**, wings ≈ ±0.82%. No stand-aside, no caution.
- **QQQ**: sell_premium=true, vol_state LOW, implied_move 1.04%, expected_range **1.42%**, size_scalar **0.5**, structure = iron fly / short straddle centred **720.95**, wings ≈ ±1.42%. Lower confidence (Nasdaq index book unavailable).
- ⚠ **Tension to state:** the 0DTE front-expiry read says sell premium while the **30d QQQ VRP says PREMIUM_BUYING** (IV 20.4 vs realised 25.5). Different horizons. Do not let the 0DTE lane imply a 30d short-vol view on Nasdaq.
- Tail caveat: validation sample has **no vol shock** — short-vol left tail UNSAMPLED. CPI is Wednesday.

## Rubric status
**OUT-OF-REGIME** (rubric frozen `2026-06-12`, fitted UPTREND; current TRANSITIONAL) — **all sizing capped at half.**
**Directional SHORTs route to `watch_only` and are never sized** (2026-08-01 P0 #1) — routing, not suppression: generate, score and serialize short theses in full. Hedge legs / defined-risk spreads / short-vol structures are out of scope of that rule.
