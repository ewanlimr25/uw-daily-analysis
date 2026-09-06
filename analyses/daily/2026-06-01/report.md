# Daily Market Analysis — 2026-06-01

## Executive Summary
- **Regime + GEX state:** **TRANSITIONAL / UPTREND** — half-size, defined-risk (iron condors in range). SPY 758.54 (+5.55% 30d, −0.23% from 90d high) sits on a **knife-edge gamma flip** (ZGL 759.72); QQQ 742.57 in clean long-gamma. VIX 16.05 (LOW). **Breadth is the tell: BEARISH despite the uptrend** — UW bullish_pct 40.1%, Finviz pct_green 41.55% (two independent lineages agree the tape is narrow/distributive). Tech is the only high-magnitude sector inflow; mega-cap platforms (TSLA/META/AAPL/GOOGL) are being sold.
- **Next-session GEX (SPY/QQQ):** *advisory, see §2.* **SPY** — short-gamma knife-edge at ZGL 759.72 (spot 758.54), call wall 760 / put wall 740; **fade-the-line, don't sell the straddle through it** (regime fresh/unstable). **QQQ** — long-gamma, ZGL 740.39, pin magnet 742, put wall 730; **short-straddle / iron-fly @742** (durable, held POSITIVE since 5/22).
- **Top swing build:** **MSFT (starter)** — the *single* directional survivor of the full gate stack. Cleanest dealer-DEX inflection (flip 5/27 preceded +12%), strongest cum-flow (+$776M/30d), fundamentals CONFIRM (4/4 beats, no earnings for 57d), bull won the debate (0.75 vs 0.65). **But it is still beta** (market-excess −10.6pp) and crowded — express as a defined-risk bull-put spread, not a naked long.
- **Top LEAP candidate:** **None.** leap-positioning-radar returned NO qualifying LEAP (all 6 single-name builds failed the conviction-matrix gate; MSFT was the strongest near-miss). The two long-dated put structures (SNDK $23.5M, IREN) are hedges, not directional shorts.
- **Biggest risk:** **Thematic concentration into an event wall.** 100% of the conviction longs are one AI-infra/mega-cap Tech bet (pairwise corr just under the 0.70 cluster line but thematically ~1.0 on a macro shock), held into NFP (6/5), CPI (6/10), PPI (~6/11), FOMC+SEP (6/17), with AVGO earnings 6/3 and ORCL earnings 6/10. **The one genuine-edge name (META short, +19.8pp alpha) is fundamentals-VETO'd.** Hedge: QQQ put vertical to 6/19 + VIX call ladder.

> **Desk call: this is a stand-aside / near-flat day.** The gates did their job by refusing to let a crowded, all-beta long book size up into an event wall while the only real edge was a fundamentals trap. The cleanest expressions today are the **delta-neutral 0DTE premium-sell (§2a)** and the **index vol calendar (§5)** — not any directional single name.

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend **UPTREND**. SPY 758.54, above 20-SMA (741.23) and 50-SMA (705.62), +5.55% 30d, −0.23% from the 90d high. Guidance: half position sizes, favor defined-risk, iron condors in range.

**Breadth (the divergence):** UW market breadth 2,483 bullish vs 3,715 bearish tickers (**bullish_pct 40.1%**) of 6,198. Finviz cross-check (advisory, independent lineage): **209 advancers / 294 decliners, pct_green 41.55%**, avg +0.05% but **median −0.58%**; top mover MGM +16.1%, worst FDX −17.8%. **Both sources independently flag a green index on negative breadth = distribution / narrow-leadership tell.**

**Per-index gamma (current-state EOD book — §2 carries the forward read):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 758.54 | 759.72 (reliable) | +686.5M | **NEGATIVE / short-gamma** (spot just *below* ZGL — knife-edge) | 760 (+249M) | 740 (−51M) |
| QQQ | 742.57 | 740.39 (reliable) | +691.8M | **POSITIVE / long-gamma** (spot *above* ZGL) | 760 (thin); 742 at-spot magnet (+263M) | 730 (−12M) |
| IWM | ~289 | 183.15 (**unreliable artifact**) | −363M | data-quality caveat — ZGL is a deep-ITM/sparse-OI artifact; spot sits on a short-gamma strike (−121M@289) | n/a | 289 (short-gamma pin) |

**`uw options-flow dte-volume-share`:** 0DTE 25.9% / weeklies 26.8% / monthlies 23.5% / LEAPs 7.3% — **BALANCED** (not retail-dominated; ~31% monthly+ = institutional-leaning).

**`uw historical vrp`:** SPY **FAIR** (IV30 13.1% vs realized 9.6%, VRP +0.035); QQQ **PREMIUM_SELLING** (IV30 20.6% vs realized 15.6%, VRP +0.050). Net: mildly premium-selling tape.

**Macro backdrop (`scripts/fred_macro.py`):** Yield curve **normal/positive** (10s2s +0.42, no inversion stress). Core CPI **2.99%** YoY (headline ~3.95% — sticky), unemployment **4.3%**, payrolls **+115k** (cooling labor), 10Y **4.45%** (flat 30d), FFR 3.62%, **USD weakening**. Benign-but-late-cycle; the narrow breadth is the warning, not the macro.

**Forward `event_risk` (Tier-1, next ~2 weeks):** **NFP 6/5 · CPI 6/10 · PPI ~6/11 · FOMC + SEP 6/17.** A stacked 4-event wall inside a standard swing horizon — plus single-name earnings AVGO 6/3 and ORCL 6/10 (= CPI day).

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book (OI persists overnight), read forward as the *prior* for the 6/02 open. Prose-only, **0 rubric points**, no backtested predictive claim (validation lives in `/weekly-analysis`). SPY & QQQ only.

| Index | Regime | ZGL (reliable?) | Call wall | Put wall | Next-session 0DTE structure bias |
|---|---|---|---|---|---|
| **SPY** | **NEGATIVE / short-gamma** (knife-edge, spot 758.54 just below ZGL) | 759.72 ✓ | 760 (+249M) | 740 (−51M) | **Fade-the-line, do NOT sell the straddle through it.** Below 757 → short-gamma air down to 740 (debit put vertical / directional). Reclaim >759.72 → long-gamma pin re-asserts (758/760 iron-fly). Binary-at-the-line. |
| **QQQ** | **POSITIVE / long-gamma** (spot above ZGL) | 740.39 ✓ | 760 (thin); 742 at-spot magnet | 730 (−12M) | **Short straddle / iron-fly centred 742**, or condor 730/735–748/753. Long-gamma vol suppression, mean-revert toward 742. Downside only accelerates if 740.39 fails. |

**Regime freshness:** SPY **FRESH & UNSTABLE** — flipped POSITIVE→NEGATIVE *today*, 9 ZGL crossings in 30 sessions, ZGL pinned within ~2–4pts of spot all week. QQQ **DURABLE** — held POSITIVE continuously since 5/22 (10 sessions). The QQQ pin carries more weight than SPY's.

**Mandatory caveats:** (1) EOD = prior, not target — fresh 0DTE OI re-computes the map in the first 30–60 min. (2) SPY's headline `total_gex` is positive but driven by far-OTM call gamma; **trust the NEGATIVE regime flag + near-spot per-strike sign**, not the headline total. (3) **Gap risk voids the prior** — 6/02 has no Tier-1 print but the event wall (NFP 6/5+) means any overnight gap through SPY 759.72 / QQQ 740.39 invalidates the map. (4) ETF book, not the cleaner SPX/NDX index book. (5) Tooling cannot isolate the D+1 expiry — this is the 0–45d proxy.

### 2a. Next-Session 0DTE Premium-Selling Setup (`scripts/zerodte_setup.py` — the validated stack)

> The GEX walls above are a *map* (advisory "where"), not a pin — wall-as-magnet and every directional 0DTE signal backtested NO_GO. What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, NOT a guaranteed edge (validation sample has no vol shock → short-vol tail unsampled).

Backtest verdict: **GO_PREMIUM_SELL_INTRADAY** (both indices).

| Index | sell_premium | vol_state | VIX | implied_move | exp. range | size_scalar | Structure | Entry |
|---|---|---|---|---|---|---|---|---|
| **SPY** (≈SPX) | YES | LOW | 16.05 | 0.63% | 0.70% | 0.5× | iron fly / short straddle @758.65, wings ≈ ±0.7% | Enter at/after the open once the gap resolves; hold 0DTE to the close; never carry overnight. Stand aside if it gaps beyond the wings. |
| **QQQ** (weaker — NDX book unavailable) | YES | LOW | 16.05 | 1.14% | 1.19% | 0.5× | iron fly @742.41, wings ≈ ±1.19% | Same entry rule. |

Backtest context: SPY premium-sell open win 97.1% (n=35), mean +0.39%/day; QQQ 94.3%, +0.49%/day. Overnight carry is negative both (SPY −0.22%, QQQ −0.42%) — **intraday only.** No stand-aside triggered (VIX not spiking, no front-end backwardation). Delta-neutral — no directional tilt.

---

## 2b. Swing Dealer Positioning (1–4 weeks)

`dealer-positioning-strategist`. **No vanna squeeze exists anywhere in the book** — every index and nearly every single name is call-heavy with VIX falling, which is a mild *de-grossing drift* (dealers trim longs as IV decays), a headwind into the event wall, not a squeeze tailwind. The lone put-heavy name is META (a short).

| Symbol | DEX state | 5d DEX trajectory | Regime flip | swing_bias |
|---|---|---|---|---|
| **QQQ** | POSITIVE +62.8B | constructive (puts unwound) | none; spot>ZGL long-gamma | **LONG** (cleanest index structure) |
| **SPY** | POSITIVE +56.4B | deteriorating off 5/29 peak | **FLIP 6/01 POS→NEG (knife-edge)** | **NEUTRAL** |
| **IWM** | POSITIVE +7.65B | deteriorating | ZGL artifact — unreliable | **NEUTRAL** (data-DQ) |
| **MSFT** | POSITIVE +16.75B | **sharp + inflection (14× off 5/27 trough)** | 5/27 flip preceded +12% | **LONG** |
| **MU** | POSITIVE +31.1B | strongly improving | none | **LONG** (but +36%/8d extended; see §3 flow-conflict) |
| **AVGO** | POSITIVE +7.31B | improving (monotonic) | whippy (5 flips/10d) | **LONG** (light) |
| **NVDA** | POSITIVE +31.7B | **deteriorating → 1-day repair** | none | **NEUTRAL** (dealer-vs-flow contradiction) |
| **TSLA** | POSITIVE +3.5B | **collapsing −77% off 5/27** | gamma cushion vanishing | **SHORT** |
| **META** | **NEGATIVE −0.70B** | **flipped POS→NEG** | **FLIP 6/01 POS→NEG gamma** | **SHORT** (strongest structural short) |
| **AAPL** | POSITIVE +9.96B | flat/supported | none, deep long-gamma floor | **NEUTRAL** (dealer-vs-flow contradiction) |

**Flagged contradictions:** NVDA (#1 flow long but DEX deteriorating → held NEUTRAL pending confirmation); AAPL (flow sold −58M but dealer structure supportive → NEUTRAL); META (flow + dealer agree short — structurally the strongest, but see the fundamentals VETO in §6).

## 2c. Sector Rotation

`sector-rotation-strategist`. **Rotation regime: `no_change` (low confidence) — this is concentration/narrowing within Growth, NOT a rotation.** Technology is the only high-magnitude inflow leg (synthesis +$982M; sector-flow +$13.1B; persistence 1.0). The "outflow" sectors form no coherent defensive/value destination, and defensives are flat (not receiving the money). BEARISH breadth corroborates: capital is narrowing into mega-cap AI-infra.

- **Rotating into:** Technology (NVDA/MU/SNDK/ADI/MSFT/ORCL/IBM) — *but this is the AI-infra/semis bid, not broad Tech; mega-cap consumer-platforms are sold.* Financials (GS/MS/C — money-center, not regionals: KRE bearish).
- **Rotating out of (de-risking):** Consumer Discretionary — **XLY clean OUT** (imbalance −0.281, 84% bearish put-sweep urgency) is the only sector-level short lens. Comm Services synthesis −119M is a 1-day artifact (5d persistence still inflow, XLC bullish) → watch-only.

**ETF flow tape (advisory — strengthens the conditional sector-leader +1, 0 new points):**

| ETF | Net prem dir | Persistence (5d imbal) | Options urgency | GICS agreement | Note |
|---|---|---|---|---|---|
| IGV (software) | inflow | +0.096 BULLISH | +33.7M call, imb +0.63 | **agree** (Tech IN) | confirms software leg |
| XLK | inflow | **+0.186 BULLISH** | +8.0M call, imb +0.48 | **agree** | NVDA/MSFT/ORCL weights |
| XLE | inflow | +0.142 BULLISH | +10.4M call | **agree (XLE side only)** | conflicts w/ XOP |
| **XLY** | **outflow** | **−0.281 BEARISH** | −4.5M put, imb −0.84 | **agree (Discretionary OUT)** | index-short lens; AMZN is intra-basket dispersion |
| **SMH** | **outflow** | **−0.039 MIXED** | −3.1M put | **DISAGREE (Tech IN, SMH OUT)** | **KEY TELL: semis-basket distribution under a bid Tech tape — late-cycle narrowing; downgrades "broad semis long" to single-name only** |
| XOP | outflow | −0.132 BEARISH | mixed | disagree (Energy IN, XOP OUT) | E&P de-risking vs broad-energy bid |

Two divergences worth the desk's attention: **SMH (distribution) vs Tech GICS (inflow)** = the semis basket rolling over before the generals; **XOP (bearish) vs XLE (bullish)** = quality-up within energy. Both downgrade basket-level conviction to single-name.

---

## 3. Swing Setups (1–6 weeks)

**The entire long book is beta in one AI-infra cluster, and four of five scored names eat an event-risk and/or debate cut. Net result: one starter (MSFT), the rest SKIP/watch.** Ranked by conviction score.

| Ticker | Score / Tier | Dir | Thesis | Structure | Invalidation | **Final size** |
|---|---|---|---|---|---|---|
| **ORCL** | 10 / HIGH | L | DP accumulation (mega buy-ratio 0.821) + cum-flow +$209M into 6/10 earnings | Bull put spread *(if at all)* — defined-risk only, expiry must not straddle the 6/10 binary | Loses the **248.15 DP shelf** (densest institutional level; secondary 246.75) | **SKIP** |
| **MSFT** | 8 / MED | L | Cleanest dealer DEX inflection (flip 5/27 → +12%) + strongest cum-flow (+$776M); CONFIRM, no earnings 57d | **Bull put spread below ~448** (DEX support); defined-risk | Daily close < ~448 / loss of the DEX-support bid | **STARTER** |
| **AVGO** | 8 / MED | L | Dealer DEX + 10d call-OI build + AI-capex — **but earnings 6/3 (2 days)** | **Watch until post-6/3** (or pre-3 0DTE gamma scalp only) | n/a — binary event, no swing entry pre-print | **SKIP** (watch post-6/3) |
| **IBM** | 7 / MED | L | Cleanest signed-bullish cum-flow (+$313M/90d) + Barclays PT→$350; CONFIRM | Bull put spread *(if at all)* — but see debate | Below the breakout shelf; cum-flow turning | **SKIP** |
| **SNOW** | 3 / LOW | L | Cleanest accumulation microstructure (mega buy-ratio **1.000**), but cum-flow +$48M sub-floor | Watch — flow below conviction floor | Loses **280** DP cluster | **SKIP** |

### 3a. Long swings (regime-aligned)
- **MSFT** is the only survivor. The bull won its debate (0.75 vs 0.65) on a **real, persistent dealer-DEX structural bid** (+$16.75B, dealers short calls → mechanically buy dips); the bear conceded that bid is genuine and recommended "cut," not "kill." Sized to **starter** because (a) market-excess −10.6pp = beta not alpha, (b) the gamma fuel is half-spent ($721M→$269M total_gex), (c) crowded mega-cap into bearish breadth. Defined-risk bull-put spread, not a naked long.
- **ORCL / AVGO / IBM** are gated to SKIP. ORCL: bear won the debate (0.75 vs 0.65) — a parabolic +22%-in-3-days blow-off (203.70→225.78→248.15), 90d flow net **−$157M**, into a CPI-day earnings binary at IV rank 100; the "accumulation" is a 5-day chase, and fz shows institutions net sellers last settlement. AVGO: both sides agree **kill the swing** (earnings in 2 days, mixed-surprise name at the richest multiple, −9.3% max-pain pin below spot). IBM: debate tie (bear ≥ bull) — fresh option flow is **net puts 2.24:1** with a $6.7M Mar-27 300P hedge printed at the top and the $350 call being sold; chasing a +9% one-day Barclays pop at RSI 83.85.

### 3b. Short / fade swings (defined risk only)
- **META — VETO'd to watch-only.** The microstructure short is genuinely the book's only alpha (DEX sign-flip + GEX flip + −$347M flow, market-excess +19.8pp), **but** it points at a strengthening business: 4/4 *accelerating* beats, 26% revenue growth, **22x PE (cheapest in the cohort)**, Recom 1.29 with +37% analyst upside. Short into that is distribution risk against you. Any residual bearish expression must be tactical, defined-risk, de-sized — not an outright swing short.
- **contrarian-scanner: NO qualifying fades.** Only SMCI & MSTR broke ±2σ and both are structural insurance bids into the event cluster (backwardation-into-catalyst), not crowded euphoria. A valid disciplined no-go.

**Near-term sweeps (informational, 0 rubric points) — the most important colour today:** sweep-tracker found the semis "bullish" persistence labels are premium-weighting artifacts; the **fresh OI build is put-dominant** on MU / INTC / MRVL / SNDK / AMD (5/5 consecutive build days) — a coordinated **semis downside-hedge / opening-put build into NFP**, mirrored by index put-protection (SPY/QQQ/SPXW) and credit/ETF hedges (HYG/IGV/XLE). The underlying tape bought these names; the options tape is hedging them. **AMD** is the cleanest standalone bear (bearish persistence + bearish OI build) but failed the confluence gate (1 agent) → watch.

---

## 4. LEAP Builds (6–24 months)

**No qualifying LEAP.** `leap-positioning-radar` ran the full DTE>180 set; all 6 single-name builds (MSFT, CPNG, BSX, SW, CODI, IREN) failed Gate 8 (conviction-matrix DIRECTIONAL_LONG conf >70 — all returned MIXED/PARTIAL). LEAP share of flow is a thin 7.3%.

- **MSFT** — strongest near-miss: OI BUILDING 10d, $20.3M C520 fresh LEAP (largest single-name LEAP on the tape), but cum-flow MIXED (+$955M on 51.7/48.3 split = churn) and conviction MIXED 3%. Real LEAP participation buried in two-sided mega-cap flow.
- **CODI** — cleanest cum-flow signature (+$36.4M, 89.6% bullish) but conviction PARTIAL_DATA, 0 DP trades, sub-$50M ADV (fails liquidity floor).
- **SNDK $23.5M LEAP put / IREN** — both two-sided **hedge/collar** structures (puts financed against fresh LEAP calls), NOT directional shorts. SNDK 90d flow is net +$1.11B bullish, corroborating its bullish day-flow; the put is protection.

---

## 5. Volatility Surface

`vol-surface-scout`. Net VRP bias: **mildly sell-vol** (QQQ PREMIUM_SELLING, SPY FAIR).

- **Single-name SELL-VOL (post-crush only):** PANW (6/2), CRWD (6/3), AI (6/3), GTLB (6/2), ORCL (6/10), ADBE (6/11) — all BACKWARDATION with rich front IV (front-ratio 1.13–1.99) **rising into an imminent earnings print**. Positive VRP, but the only trade is the *post-event* crush capture; **never sell into the rising build.** All disqualified as calendars (the 6/18 OPEX "second hump" is a trap — it retains post-earnings drift premium, both legs collapse together).
- **ARM — VRP CONFLICT flag:** iv_rank 100 / z +2.34 *look* rich, but VRP is **NEGATIVE** (IV30 107% < realized 119%, PREMIUM_BUYING). **Do NOT sell ARM premium** — it has realized more than it implies; the back-month is the long-gamma/buy-vol expression.
- **Index BUY-VOL (the one genuine calendar dislocation):** **SPY/QQQ.** The curve correctly humps each macro event (NFP 16.0%, CPI 15.3%, FOMC-week 18.0%) but the **inter-event troughs sit at the 252-day floor** (SPY iv-pctl 2.86th, z −1.09). Trade: **long the FOMC-week 6/18 expiry, short the quiet 6/15** (sell ~12.2% to own ~18.0%), or own the 6/18 ATM straddle financed by selling 6/15. **Small size** — VRP is only FAIR, so this is a vega-cheapness play, not a VRP play.
- **No actionable single-contract IV outliers** (all 0DTE index/penny-stock noise; fail the $5 / $50M floor).
- **multileg-strategist:** one clean directional structure — **AMZN long call butterfly 250/275/300 Jan-27** ($1.12B notional, net debit ~$3.27, target 275, CONTANGO-anchored, GEX reinforces the 275 pin). Score-eligible but the name dropped on opposing 30d flow (see §8). GEHC long strangle 57.5P/62.5C (6/18) is a vol play, not directional.

---

## 6. Risk & Correlation

`risk-monitor` consuming the candidate union + audited score + fundamentals + debate.

**Macro headline:** curve normal, sticky-but-cooling inflation/labor, USD weakening — benign-but-late-cycle. **The warning is breadth, not macro.** Forward event wall: **NFP 6/5 · CPI 6/10 · PPI ~6/11 · FOMC+SEP 6/17**, plus AVGO earnings 6/3 and ORCL earnings 6/10. **Breadth cross-check:** advancers 209 / decliners 294, pct_green 41.55% — **green index on negative breadth = distribution tell** (flagged, advisory, 0 size impact).

**Correlation:** `uw risk portfolio-correlation` on today's candidates — max pair **ORCL/MSFT 0.644**, below the 0.70 mechanical cluster threshold → **no cluster penalty fires** on any name (mechanical P1.4 discipline; no discretionary upgrade). **But the thematic concentration is total** — 100% mega-cap Tech/AI-infra, which will correlate toward 1.0 on a macro shock. Treat the longs as one position when sizing the book; the hedge sleeve (not the per-name gate) is the instrument for that tail.

**Gate stack applied (dominant gate today = event-risk):**

| Gate | Outcome |
|---|---|
| Regime | no-op (longs align with UPTREND; META short would conflict but is VETO'd) |
| VRP / Panic | no-op (no vol-structure candidates; front-end-iv-ratio not >1.10, VIX 16 LOW) |
| Cluster | no-op (max pair 0.644 < 0.70; ORCL/MSFT soft-watch, no penalty) |
| Sector | no-op (Tech persistence 1.0 INFLOW — no *adverse* rotation) |
| **Fundamentals** | **CAUTION −1** ORCL, AVGO; **VETO → watch-only** META; CONFIRM no-op MSFT, IBM |
| **Event-risk** | **−1 every swing name** (4-event wall in 12 sessions; ORCL/AVGO earnings ≤T+7) |
| **Debate** | **cut** ORCL, AVGO, IBM (bear ≥ bull); no-op MSFT (bull won) |

**Fundamentals verdicts (the contradicting facts):**
- **META — VETO:** short into 4/4 accelerating beats, 26% growth, 22x PE (cheapest in cohort), Recom 1.29 / +37% upside. Smart-money distribution risk *against* the short, not for it.
- **ORCL — CAUTION:** fundamentals corroborate the long, but earnings 6/10 AMC (= CPI day), IV rank 100, RSI 80.7, price 1.8% above target, D/E 4.67.
- **AVGO — CAUTION:** earnings 6/3 (2 days), mixed surprise history (2/4 misses), richest multiple, +5.2% to target.
- **MSFT / IBM — CONFIRM:** 4/4 beats, no near-term earnings; IBM advisory cautions (RSI 83.85, flow 10% past a weak 2.04 consensus).

**Adverse-flow exit (from `uw watchlist scan` on conviction_2026-05-29):** **SMH — EXIT** (semis-long proxy flipped hard bearish: P/C 2.87, net −$6.2M, IV rank 98, ETF AUM −$490M outflow) — corroborates the SMH-distribution divergence in §2c and the bearish breadth. MSFT flow still constructive (no exit). ORCL flow right but setup wrong (risk-gate exit, not flow). HPE momentum already realized — don't chase.

**Hedge sleeve (mandatory — book skew ~1.0 long Tech):** (1) **QQQ put vertical** ~2–3% / ~6–7% OTM, **expiry 6/19** — covers NFP→FOMC, defined-risk, cheap at VIX 16, and QQQ *is* the book (MSFT/AVGO/NVDA/META weights). (2) **VIX call ladder** (June 20/25 spread) — convexity is cheap near the VIX floor into a 4-event wall on bearish breadth.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no prior `/calibration-audit` per-tier expectancy table is being consumed this run; the live sizer remains the win-rate ladder (Step 5). The book-level read from the 2026-05-30 audit stands: **longs ran ~−22pp benchmark-excess (beta) and shorts ~+20pp (alpha)** — today's book is 100% beta longs with the one alpha short VETO'd, the structurally worst excess profile, which is *why* the honest sizing is near-zero.

| Ticker | raw_score | dominant_signal_class | win_rate (n, src) | market-excess | pre-risk | fund. | bull/bear | final | invalidation |
|---|---|---|---|---|---|---|---|---|---|
| **ORCL** | 10 (HIGH) | dark_pool_accumulation | 0.5676 (74, fallback) | **−0.149 beta** | starter | CAUTION | 0.65 / **0.75** | **SKIP** | loses 248.15 DP shelf |
| **MSFT** | 8 (MED) | gamma_breakout | 0.519 (133, proxy) | **−0.106 beta** | starter | CONFIRM | **0.75** / 0.65 | **STARTER** | close < ~448 |
| **AVGO** | 8 (MED) | gamma_breakout | 0.519 (133, proxy) | **−0.106 beta** | starter | CAUTION | 0.65 / **0.75** | **SKIP** (watch post-6/3) | binary 6/3 — no pre-print swing |
| **IBM** | 7 (MED) | bullish_flow | 0.519 (133, backtest) | **−0.106 beta** | starter | CONFIRM | 0.65 / 0.65 (tie) | **SKIP** | breakout shelf / cum-flow turn |

**Per-ticker audit detail:**
- **ORCL (10):** +3 accum conjunction (accumulation-hunter/institutional-accumulation; mega buy-ratio 0.821, cf30 +$209M confirms) · +3 cum-flow accretion (quant/cumulative-premium-flow) · +2 signal-confluence=5 · +1 OI build · +1 sector leader. LB-gate 4/5 → HIGH preserved. **Final SKIP** — fundamentals (−1, CPI-day earnings) + event-risk (−1) + debate (bear 0.75 > bull 0.65, distribution-at-the-top). Win-rate is beta (excess −0.149). `distribution_flag`: not present in `oi decrease-with-volume` (present:false).
- **MSFT (8):** +3 dealer DEX flip (dealer-positioning/dex) · +3 cum-flow accretion (+$776M, largest in union) · +1 OI build (call-dominant +87,754/0 puts) · +1 sector leader. **Final STARTER** — only event-stack cut; bull won the debate on a real DEX bid. Beta (−0.106), so defined-risk only.
- **AVGO (8):** +3 dealer DEX · +3 cum-flow accretion (+$179M) · +1 OI build · +1 sector leader. **Final SKIP** — CAUTION (earnings 6/3) + event-risk + debate (kill swing). Watch post-print.
- **IBM (7):** +3 cum-flow accretion (+$150M/30d, +$313M/90d — cleanest signed-bullish) · +2 signal-confluence=4 · +1 OI build · +1 sector leader. C4 opening confirmed (no cap). **Final SKIP** — event-stack + debate tie (fresh flow net puts 2.24:1).

**Deep-dive hand-off:** none. No HIGH-tier name survives the gate (ORCL is HIGH by score but SKIP'd). This is a no-edge day for the single-name deep-dive engine — `/stock-deep-dive` not triggered. If the desk wants one anyway, MSFT (the lone survivor) is the candidate: `Recommended deep dive: /stock-deep-dive MSFT`.

### Conviction-scoring rubric (Step 4, embedded for audit)
```
+3 dealer DEX flip / vanna-squeeze in trade direction
+3 accumulation 3+ aligned signals — CONJUNCTION C11: full +3 only if cum_flow_30d sign-aligned AND |cf30|≥$50M; else +1
+1 multi-day OI build (BUILDING --days≥5)
+1 conviction-matrix DIRECTIONAL_LONG conf>70 — CONDITIONAL (leap_directional only; else 0)
+3 cum-premium-flow net directional accretion (30d)
+2 signal-confluence ≥4 (second-agent confirmation)
+1 sector-rotation single-name leader — CONDITIONAL (persistence≥0.6 AND cf30 aligned AND |cf30|≥$50M)
+1 earnings BUY VOL / SELL VOL
+2 multileg directional structure (term-structure-anchored)
+1 vol-surface KINKED/BACKWARDATION with VRP-aligned bias
−2 contrarian overcrowded long + rising pc-ratio-zscore (VRP positive)
−3 flow_conflict (cf30 clearly opposite dominant class) | −1 flow_conflict_lite (cf30 MIXED) — mutually exclusive
−1 correlation cluster (corr>0.7, applied in 2d) | −3 regime conflict (applied in 2d)
TIERS: ≥9 HIGH (full) / 7–8 MEDIUM (half) / 3–6 LOW (starter/watch) / ≤2 drop. §2/§2a advisory = 0 points.
```

---

## 8. Watch-only — single signal / failed confluence gate / gated out

Listed for journaling, **NOT for trade entry today.**

- **META** (short) — **VETO** (short into strengthening fundamentals). The book's only genuine alpha, killed by the gate. Re-evaluate only if fundamentals re-rate.
- **TSLA** (short) — DROPPED, **flow_conflict −3**: dealer DEX collapse is real, but cf30 **+$460M BULLISH** opposes the short (the canonical un-penalized-flow-conflict trap). Suppressed correctly.
- **MU** (long) — DROPPED (raw 2): dealer DEX +3 but cf30 −$174M not long-aligned (sector +1 fails) and OI build **100% put-dominant** (+104,961 puts / 0 calls) — the long thesis is microstructure-contradicted. Extended +36%/8d.
- **AMZN** (long) — DROPPED (raw 2): real multileg long-fly structure (Jan-27 250/275/300) but cf30 −$41M opposes the long (flow_conflict_lite). Watch the fly; don't chase the name.
- **CRWV** (long) — **DISTRIBUTION TRAP:** Step-0 bullish-confluence score 5 is the illusion — DP buy/sell 0.55, mega buy-ratio **0.081 (mega tier overwhelmingly SELLING)**. Accumulation-as-distribution; flagged to risk. 0 positive agents.
- **SNDK** (short-ish) — put-dominated OI build + $23.5M LEAP put (hedge), MIXED conviction. Reject as long; not scorable as short.
- **AMD** (short) — strongest watch: clean bearish microstructure (bear persistence 5/5 + bear OI build 5/5), but 1 agent + confluence 3 → failed gate. One 2nd bearish agent from scorable (bearish_flow carries +19.8pp excess).
- **NVDA** (long) — #1 flow leader (+$182M) but dealer-positioning NEUTRAL (DEX deteriorating, single up-day repair) → 1 agent + confluence 3 → failed gate. cf90 −$110M MIXED.
- **MRVL** (short) — conflict: on the bullish leaderboard (+$44M) yet sweep OI build put-dominant + Tier-1 opening-put (advisory). Mixed → correctly excluded.
- **SHW (conf 6) / CME / DVN / DDOG** — signal-confluence-*screener* bearish but **0 Phase-1 agent flags** → fail the confluence gate. QCOM — sweep conflicted (bear persistence + call OI build) → watch.

**Single-leg whale (advisory C19, 0 points):** 3 Tier-1 OPENING_PUT_PRIME shorts — HUBS ($896K), SPCE ($754K, vs its +21.7% RS pop), MRVL ($672K). Context: SNDK $23.5M LEAP put (structural hedge). contrarian-scanner found no crowding behind any of them (NORMAL z-scores, net-bullish aligned flow) → corroborate nothing tradeable today; logged.
