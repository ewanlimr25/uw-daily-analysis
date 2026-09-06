# Daily Market Analysis — 2026-06-04

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / UPTREND — SPY 757.09 (+4.6% 30d, −0.44% from 90d high), VIX 15.4, half-size + defined-risk mandate. Dealers **net-short gamma** across SPY/QQQ/IWM into NFP. Breadth split: price 72% green vs **options-flow breadth only 39.2% bullish** (flow more cautious than price). Sector lean: **cyclical→defensive (risk-off), HIGH confidence**.
- **Next-session GEX (SPY/QQQ):** **SPY** — NEGATIVE/transition, ZGL 763.25, pins to **757 call wall** / 745 put wall → iron fly on a quiet NFP. **QQQ** — short-gamma, sitting on a **−493M trigger at 740** with front-end backwardation → primed to *trend* off NFP, don't sell it. *Advisory, see §2. NFP gap voids the prior.*
- **Top swing build:** **None at conviction.** The day's headline name **NEE** (raw 7) was disconfirmed — its +$506M "accumulation" is a **dividend-capture arbitrage** (deep-ITM 40C printed *below intrinsic*, 23 resting OI, ex-div week), not directional buying. Held to **starter, defined-risk only**, not naked through the event wall. The rule-based scan independently returns *"No Clear Edge — Stay Flat."*
- **Top LEAP candidate:** **None.** No name passes the 6-of-9 LEAP gate; thin LEAP tape (5.6% of volume) into a defensive regime. META/NEE handed to the cash/swing desk; both fail LEAP-location.
- **Biggest risk:** **Event wall + beta book.** NFP **tomorrow (Jun 5)**, CPI Jun 10, FOMC Jun 16-17 — three Tier-1 prints inside the swing horizon. Every long class scored **beta, not edge** (C2 market-excess −0.18 to −0.27 vs SPY). **Verdict: defensive stand-down day** — the day's real edge is the delta-neutral §2 0DTE premium-sell, not the directional sleeve.

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend **UPTREND**. SPY 757.09, above 20-SMA (745.99) and 50-SMA (711.90), +4.6% over 30d, but only −0.44% from the 90-day high (extended, little room). Trading guidance: **half position sizes, defined-risk, iron condors in range.**

**Breadth — the key tell:** `uw` options-flow breadth is **39.2% bullish** (2,437 bullish vs 3,778 bearish flow tickers of 6,215). The `fz` price-breadth cross-check (large-cap, independent lineage) is **72% green** (362 adv / 140 dec, avg +0.96%). Large-cap *price* is strong while broad *flow* is defensive — a distribution undertone the single regime label hides (no formal divergence flag since `pct_green` > 50, but the gap is the signal).

**Per-index gamma (current-state EOD book; §2 carries the forward read):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 756.96 | 763.25 (reliable) | +$472.6M | NEGATIVE (transition) | 757 (+309M) | 745 (−79M) |
| QQQ | 740.56 | 190.07 (**unreliable**) | **−$844M** | short-gamma (label stale) | 745 (+45M) | **740 (−493M, at spot)** |
| IWM | 288.19 | null | −$37M | FULLY_NEGATIVE | — | — |

All three are short-gamma or on the flip — dealers amplify rather than dampen moves into the print.

**DTE volume share:** 0DTE 23.4% / weeklies 31.3% / monthlies 32.4% / LEAP 5.6% — `regime_hint` BALANCED (monthly+ ~38% = moderate institutional, not a retail-0DTE tape).

**VRP:** **FAIR** — IV30 0.129 vs realized σ30 0.093 (vrp +0.036). No meaningful premium edge either direction; vol is neither cheap nor rich.

**Macro backdrop** (`scripts/fred_macro.py`): yield curve **normal** (+0.42 10y2y), **Core CPI 2.99% / Core PCE 3.29% YoY — sticky, above target**, unemployment 4.3% (+115k payrolls), 10Y **4.49%** flat 30d, 2Y 4.08%, USD **weakening**, Fed funds 3.62%. Late-cycle, sticky-inflation backdrop that limits Fed dovishness and keeps rate-proxies (utilities) pressured.

**Forward event-risk calendar (next ~10 sessions):**

| Event | Date | Distance | Impact |
|---|---|---|---|
| **Nonfarm Payrolls (May)** | **Fri Jun 5** | **T+1 (next session)** | **HIGH** |
| **CPI (May)** | Wed Jun 10 | T+4 | HIGH |
| PPI (May) / jobless claims | ~Thu Jun 11 | T+5 | medium |
| **FOMC decision + SEP/dot-plot** | Tue-Wed Jun 16-17 | T+8/9 | HIGH |

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book (OI persists overnight) read forward as the *prior* for the Jun-5 open. Prose-only, **0 rubric points**, no backtested predictive claim. **Overriding caveat: NFP (May) prints Fri Jun 5 pre-open (HIGH) — a gap through any level below voids the entire prior in the first print.**

### SPY — pins to 757, range-bound *if* NFP is benign
- **spot 756.96 · ZGL 763.25 (reliable, +0.83%) · total_gex +$472.6M · regime NEGATIVE/transition.** Spot sits *on* the 757 call wall and *below* the 763.25 flip → locally short-gamma (trend-amplifying) until it reclaims ~763; the dense +GEX shelf from 755 up caps pushes above 757.
- **call wall 757 (+$309M, dominant) → 760 (+207M) · put wall 745 (−$79M), stacked 750/753.** Realistic pre-NFP band **750–760**.
- **Structure bias:** quiet NFP → iron fly / short straddle centered **757**, wings 745 / 763 (VRP FAIR — keep tight, half-size). Hot NFP gap below 745 inverts to trend-accelerant → debit put vertical 745/740. **Do not sell the straddle naked into the print.**

### QQQ — sitting on a −493M short-gamma trigger at 740
- **spot 740.56 · ZGL 190.07 UNRELIABLE (zgl_reliable=false) · total_gex −$844M (collapsed from +$691M on 06-01) · effectively SHORT-GAMMA** (the "POSITIVE" label is a broken-ZGL artifact — trust the −844M total and the −493M strike at spot).
- **put wall 740 (−$493M, AT spot) → 741 (−203M) · call wall 745 (+45M) → 750 (+64M).** A break of 740 accelerates; 745 is the first re-stabilizing shelf.
- **Structure bias:** short-gamma + front-end backwardation (0DTE IV 1.26× VIX) → directional 0DTE / debit verticals in the NFP direction, or a long straddle to own the expansion. **Do not sell the 740 straddle** — short gamma + backwardation + NFP is how you get run over.

**Mandatory caveats:** EOD = prior, not target (first-hour 0DTE OI re-forms the walls); **NFP gap voids it** (short-gamma books gap further); ZGL on QQQ unreliable (fall back to total_gex sign); SPY/QQQ **ETF** book, not the cleaner SPX/NDX index book; `uw` cannot isolate the D+1 expiry (0–45d proxy, but Jun-5 expiry holds healthy share).

### 2a. Next-session 0DTE premium-selling setup (validated stack)
Both indices **GO_PREMIUM_SELL_INTRADAY** (delta-neutral, advisory, **0 rubric points** — NOT a guaranteed edge; validation sample has no vol shock, tail unsampled):

| Index | sell? | vol_state | VIX | implied move | exp. range | size | structure | entry |
|---|---|---|---|---|---|---|---|---|
| **SPY** | yes | LOW | 15.4 | 0.73% | 0.69% | **0.5** | iron fly @756.53 ±0.69% (long-gamma, quieter) | at/after open, hold to close, never overnight |
| **QQQ** | yes | LOW | 15.4 | 1.22% | 1.38% | **0.25** | wider condor ±1.38% (short-gamma) — or reduce/stand aside | same |

- **Whether (VRP):** front-expiry implied move systematically exceeds realized next-day open-to-close (SPY backtest WR 97.4% open, n=38; QQQ 94.7%).
- **Size (VIX):** LOW vol → small (thin edge); SPY 0.5, QQQ 0.25.
- **⚠ Stand-aside override:** QQQ flagged **front-end backwardation (0DTE IV 1.26× VIX) — event/gap risk, half size.** And **NFP tomorrow is the gap risk** — if either gaps beyond the wings at the open, stand aside. SPY ≈ SPX (trade either); QQQ weaker (Nasdaq index book unavailable) + the short-gamma/backwardation makes it the riskier of the two.

## 2a. Swing Dealer Positioning (1–4 weeks)
`dealer-positioning-strategist`: **all three indices show DETERIORATING DEX + a fresh negative-gamma regime flip** — a synchronized structural deterioration, not a single-name story.

| Index | DEX (5d trajectory) | Vanna squeeze | Regime flip | Swing bias |
|---|---|---|---|---|
| **QQQ** | +$53B, **−26%** (fresh leg down) | FALSE (call-heavy) | total_gex → −$844M (first sustained sub-zero in 30d) | **SHORT / defensive, LOW-MED** |
| **SPY** | +$51B, **−32%** | FALSE | flipped NEGATIVE 06-03 (on the knife) | **SHORT / defensive, LOW** |
| **IWM** | +$10B, −29% (noisy) | FALSE | FULLY_NEGATIVE today | **NEUTRAL-SHORT, LOW** |

QQQ is the best-aligned bearish read (deteriorating DEX + neg-gamma flip + front-end panic + the bearish semis cluster underneath). **No clean single-name DEX setups** — NEE/MU/NVDA all show static-sign-vs-flow disagreement. **Conviction caveat:** all three flips sit 1 day ahead of NFP — a fresh pre-NFP flip is structurally low-conviction (the print can snap dealers back to positive gamma overnight). Treat as a **defensive tilt / hedge justification, not a fresh short entry.**

## 2b. Sector Rotation
`sector-rotation-strategist`: **`rotation_regime = cyclical→defensive` (risk-off), HIGH confidence.**

| Rotating INTO | Persistence | 5d trajectory | Single-name leaders |
|---|---|---|---|
| **Utilities** | 1.0 | 10× spike today (+$554M) | **NEE +$506M** (#1 net premium in the market), GEV, VST |
| **Consumer Defensive** | 1.0 | clean monotonic 5.5× accel | PG, KO, HSY, STZ |
| **Healthcare** | 1.0 | steady, DP-confirmed | LLY, UNH, REGN, ISRG |

| Rotating OUT | Persistence | 5d trajectory | De-risking names |
|---|---|---|---|
| **Consumer Cyclical** | 1.0 | **collapsed 95%** today (2.0B→0.05B) | TSLA, NKE, HD, PDD |
| **Industrials** | 0.8 | monotonic bleed to **negative** (only neg sector) | HTZ, BE, HON |

**Tech resolution — the +$5.44B "inflow" is mega-cap call-chasing, NOT rotation:** (1) decelerating (11.6B→5.4B, today 41% of the 5d-ago print); (2) DP/equity **OUT −$231M** (institutions distributing shares under the call print); (3) **XLK instrument options are −$0.73M with call sweeps on the bid** (selling/closing) — the ETF that *is* Tech does not confirm the aggregate; (4) the biggest bearish single-names on the tape are **semis** (MU −226M, SNDK −86M, AAPL −45M, AMD −34M, TSM −16M, WDC −15M); (5) **SMH's own sweeps are protective puts.** Do not put Tech in the swing book as a long.

**ETF flow tape (advisory — 0 rubric points):**

| ETF | Net premium | Persistence | Options urgency | GICS agreement | Read |
|---|---|---|---|---|---|
| **XLY** | **−$7.90M (outflow)** | BEARISH (strongest) | **puts on ask** (110P/117P) | agree (cyclical out) | cleanest cyclical de-risk |
| **EWT** (Taiwan) | +$4.82M | BULLISH | **calls on ask** + $201M above-mid print | n/a (country) | semi-supply-chain bid, instrument-only |
| **SMH** | +$26.3M | MIXED | **PUT-heavy / protective** | **disagree** (semis sold) | hedged, not accumulated |
| **XLK** | −$0.73M | MIXED | calls on **bid** (selling) | **disagree** | call-chasing tell |
| XLV / XLF / XLP / XLU | small inflow | bullish | — | agree | confirmatory defensive bid |

---

## 3. Swing Setups (1–6 weeks)
Ranked by conviction. **Invalidation anchored to real institutional DP levels where available (C34).**

### 3a. Long swings (regime-aligned)

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **NEE** | 7 → **starter** | Defensive-rotation leader, **but the +$506M "conviction" is dividend-capture arb, not directional buying** (see §7). Genuine residual: Utilities #1, oversold (RSI 38), persistent multi-month premium skew. **Rule-based scan: "No Clear Edge — Stay Flat."** | **Defined-risk only** — call debit spread (cap the debit; NEE has no gamma floor). NOT naked through NFP. | loses the **$83.66** relative low / DP shelf ~$85.68 turns to distribution | **starter** (debate + event gate) |
| TPR | 1 → watch | Cleanest accumulation (block DP buyR 0.78, OI BUILDING 5/5, DP support $138.4) but flow too thin (<$50M halved the score); fundamentals **CAUTION** (EPS −17.8% YoY, insider −17.5%) | watch-only | loses **$138.4** DP support | **skip / watch** |
| BTU | 1 → watch | Block DP buying (buyR 0.93) but momentum-stage (+14% extended, flat 10d flow) | watch-only | loses **$30.0** DP support | **skip / watch** |

**Sweep ledger (informational, 0 rubric points):** the *only* clean directional bullish print of the day was **NEE** (ask-side opening, 5/5 persistence) — and the debate showed it's arbitrage. Every other mega-cap "bullish" persistence label (NVDA/MSFT/MSTR/NOW/ARM/MU) was **two-sided hedge/gamma flow contradicted by today's tape**. There is **no broad fresh bullish call urgency** in this 39%-bullish-breadth tape.

### 3b. Short / fade swings (defined risk only)

| Ticker | Note | Verdict |
|---|---|---|
| **SNDK / AMD** | Clean bearish opening puts (SNDK Jan-27 1700P) confirm the semis-bearish theme — **but the quant blocks the short**: SNDK 30d cum-flow is **+$1,204M** (7.8× median) and AMD **+$421M**, both *opposing* the short → mechanical `flow_conflict −3`. **Do not short against +$1.2B of 30d flow.** | watch-only |
| **HTZ** | Deep-ITM event puts ($78M, restructuring binary) — **disqualified on liquidity** (20d $ADV $39.8M < $50M floor). | dropped |
| Single-leg whale PUTs (advisory C19, 0 pts) | 8 Tier-1 institutional opening/floor put blocks on **quality names**: ISRG (K520, soi 2.84, $6.4M — highest-edge), UBER (K92.5), ABT (K115), TMUS (K220), TSLA (K465 1DTE), LOW (K260), MSFT (K430), IREN. Institutions buying downside on quality = a risk-off tell. Context, not auto-scored. | context |

**Contrarian:** `contrarian-scanner` returns **NO QUALIFYING FADES** — every statistical extreme (NEE −2.25σ, CPNG +4.88σ, LOW, REGN) is event-contaminated by NFP (BACKWARDATION near a catalyst = hard disqualifier). Stand down; re-scan post-NFP.

## 4. LEAP Builds (6–24 months)
`leap-positioning-radar`: **NO QUALIFYING LEAP.** No name passes the 6-of-9 gate floor with DIRECTIONAL_LONG confidence >70. The >180-DTE tape is dominated by macro ETF hedging (EWZ, HYG, EEM, TLT, AAPL 315 straddle), not single-name conviction.
- **META** (3/9) — DP accumulation real (buy/sell 3.69, $695M whale at $627.57) but options desk **net-hedged**, cum-flow **−$457M wrong-direction**, conviction 29%. → cash-equity story, hand to accumulation desk.
- **NEE** (2–3/9) — best cum-flow signature (+$500M/90d) but **NOT LEAP-located** (biggest >180DTE build is 225-DTE C100 at +682 contracts, *bid-side*); 0 rolls; conviction MIXED 50%. → swing desk, not LEAP.
- GOOGL / AAPL / NU — fail cumulative-flow gate (wrong-direction or flat).

## 5. Volatility Surface
`vol-surface-scout`: surface-wide, **the entire front end is NFP-contaminated** — every IV-rank-100 semi name (MRVL, WDC, AMD, TSM) tags BACKWARDATION purely from the Jun-5 expiry capturing tomorrow's print. Those are **disqualified** (event pending, not a tradeable calendar). SPY is CONTANGO / IV %ile 2.6 (too cheap to sell).

**The one real vol play — MU:**
- **KINKED** with an isolated **Jul-2 earnings kink** (Jun-26 127.6% → **Jul-2 160.1%** → Jul-10 134.3%), front-ratio **0.885 CONTANGO** (NOT panic — a discrete future event, earnings **Jun-24**). IV %ile 86.8 (z +1.36). MU fell **−7.7% today** (1079→996) on the AVGO-driven semis selloff; the 160% IV is *earned*, not a giveaway.
- **Read:** SELL the rich event vol, defined-risk, **lean short** (today's −226M flow + RSI 70 + −21.6% above analyst target + the live "memory prices approaching a ceiling" narrative). Rule-based scan agrees: **Bear Call Spread** (HIGH_IV + bearish flow). **Entry timing:** vol-surface says leg in ~Jun-20+ (let the kink ripen, avoid 2-week theta bleed) — or put on a bear call spread now to express the directional-vol lean while the AVGO narrative is fresh.

**Earnings vol (half-size at most — back-month skew COMPLACENT on all but CPB):** ORCL (Jun-10, kink 121.7%, beat-streak **3/4 not 4/4**), ACN (Jun-18, cleanest kink 96%, clean 4/4 + insider buying), CPB (Jun-8, small — priced tail but −10.9% last-Q miss risk). KR/SJM/CASY/CHWY/LEN = SKIP (NFP artifact). **No BUY VOL this cycle** (VIX 15.4, no cheap front IV vs a real catalyst). **No full-size SELL VOL** (event premium + macro double-event).

## 6. Risk & Correlation
**`macro_snapshot` headline:** sticky inflation (Core PCE 3.29%), normal curve, 10Y 4.49% flat, USD weakening — late-cycle. **Forward wall: NFP T+1, CPI T+4, PPI T+5, FOMC T+8/9.** A directional swing sized to hold more than a session eats all three sequentially.

**`risk-monitor` verdict: DEFENSIVE STAND-DOWN.**
- **Correlation:** only cluster is **MU / SNDK 0.727** (`semis_storage_cluster`); MU is the kept member (raw 3 > SNDK 0), no penalty to the sized book. NEE/ACN −0.54 (no flag). Net correlation impact on the book: **zero**.
- **Fundamentals verdicts (top-5):** NEE **CONFIRM** (beat 4/4, −11% is rate-derating not deterioration, no imminent earnings), MU **CONFIRM** (160% IV earned), ORCL **CONFIRM** (beat-streak corrected to 3/4), ACN **CONFIRM** (4/4 + insider **buying** MSPR +44.71), TPR **CAUTION −1** (EPS −17.8% YoY + insider −17.5% cluster). **No VETO.**
- **Event-risk gate:** NEE **−1 tier** (NFP T+1, rate-proxy; CPI/FOMC stack). MU **no-op** (it *is* the event — Jun-24 binary).
- **Debate-disconfirmation cut (NEE):** bull residual 0.65 vs **bear 0.75 → gate fires**. Bear's mechanical finding: the "$389M LEAP whale" 40C sweep printed **$45.46, below the $45.68 intrinsic** (negative extrinsic), 23 contracts resting OI (round-tripped), on NEE's **ex-dividend week** → **dividend-capture arbitrage**, not conviction — it inflated the +3 cum_flow and the +$506M headline. Live institutional-accumulation = **NEUTRAL** (buy/sell 0.98); conviction-matrix "Balanced" (0.495). NEE has **no dealer gamma floor** (FULLY_NEGATIVE GEX 06-01, 5 flips in 15 sessions). → NEE held to **starter, defined-risk, not naked through the wall.**
- **Adverse-flow exits (vs `conviction_2026-06-03` = SNDK/NVDA/MRVL/INTC/CMG):** **CMG** (hard adverse — P/C 7.55, 4.5× volume, heavy put accumulation) and **SNDK** (off-thesis — flow flipped bearish, resolving the prior bull-DP conflict). NVDA/INTC/MRVL theses intact (MRVL "don't chase" — IV rank 100).
- **Breadth cross-check (advisory):** 362 adv / 140 dec, 72% green — no formal divergence flag, but flow-breadth (39%) << price-breadth (72%) reinforces the cautious read.
- **Hedge sleeve:** net book delta negligible (NEE starter + MU delta-neutral) → **no index hedge required.** The §2 delta-neutral 0DTE premium-sell is the appropriate vehicle to harvest the FAIR-VRP, low-VIX, range-bound tape into NFP — keep powder dry through the print.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Expectancy lens (advisory — C31, `[advisory — expectancy is not yet a live sizing axis]`):** the most recent calibration (2026-05-30) found **longs running ~−22pp beta in an up-tape** — and today's C2 market-excess gate independently reproduced it (the accumulation class scored **−27pp excess vs SPY**, capping the entire long book at *starter*). A high hit-rate with sub-1 payoff loses money; a coin-flip with a 1.5 payoff makes it. Per-tier realized expectancy is not yet monotone on n≥30, so it remains **display-only** — the live sizer is the win-rate ladder (Step 5). The takeaway today: **the book's long edge is beta, so the sizer correctly refuses to full-size it.**

| Ticker | raw | tier | dominant class | win_rate (n, src) | pre-risk | fund. | bull resid. | gates applied | final | invalidation |
|---|---|---|---|---|---|---|---|---|---|---|
| **NEE** | 7 | MEDIUM | dark_pool_accumulation | 0.619 (42, fallback_proxy) | starter | CONFIRM | 0.65 | event_risk −1, **debate −1**, C2 beta cap | **starter** (defined-risk) | $83.66 low / $85.68 DP |
| **MU** | 3 | LOW | high_iv_rank (earnings vol) | 0.837 (49, backtest) | half | CONFIRM | — | cluster no-op (kept), event no-op (is the event) | **half** (short-vol, defined-risk) | Jul-2 kink flattens / IV30 expands through entry |

**NEE `score_components`** (Σ = 7): `+3` accumulation conjunction (accumulation-hunter / `institutional-accumulation`, flow-confirmed ≥$50M) · `+3` cum_flow 30d +$499.6M (quant / `cumulative-premium-flow`) · `+1` sector-leader (sector-rotation / `sector-flow-persistence`, all 3 gates). LB-gate **3 of 5** cited (block-stratified ✓, cum-flow ✓, institutional-accum ✓; dex ✗, signal-confluence ✗). ⚠ **The debate showed the +3 cum_flow and +3 accumulation are substantially the same dividend-capture print** — strip the arb and the genuine score is closer to the +1 sector-leader. `fz`: short float 2.38% (no squeeze), Recom 2.00 Buy (+15.6%), RSI 38.5.

**MU `score_components`** (Σ = 3): `+2` KINKED isolated earnings structure (vol-surface / `term-skew`, CONTANGO front-ratio = real event) · `+1` high IV-rank (earnings-scout / `iv-rank`). Non-directional → no flow_conflict applied. `fz`: RSI 69.7, −21.6% above analyst target (extended).

**Conviction-scoring rubric (Step 4) — embedded for audit:**
```
+3 accumulation 3+ aligned (DP+OI+smart-pos, block institutional) — CONJUNCTION: full +3 only if cum_flow_30d aligned AND |cum_flow_30d|≥$50M, else +3→+1
+1 multi-day OI build (oi-trend BUILDING ≥5d)
+1 conviction-matrix DIRECTIONAL_LONG >70 — CONDITIONAL: only when dominant_class==leap_directional (else 0)
+3 cumulative-premium-flow net directional accretion (30d)
+2 signal-confluence ≥4 (second-agent confirmation)
+1 sector-leader — CONDITIONAL: persistence≥0.6 AND cum_flow_30d aligned AND |cum_flow_30d|≥$50M
+1 earnings-scout BUY/SELL VOL    +2 multileg directional (term-anchored)    +1 vol-surface KINKED/BACKWARDATION VRP-aligned
-2 contrarian overcrowded long (rising pc-zscore, VRP+)
-3 flow_conflict (30d clearly opposite) / -1 flow_conflict_lite (MIXED) — apply exactly ONE
-1 correlation cluster (corr>0.7, in 2d)    -3 regime conflict (in 2d)
[sweep-persistence line REMOVED 2026-05-23 P0.3 — 0 points]
Tiers: ≥9 HIGH (full) · 7-8 MEDIUM (half) · 3-6 LOW (starter/watch) · ≤2 drop
```

## 8. Watch-only — single signal, no confluence / below floor
Journaling only, **not for entry today**:
- **ORCL** (raw 2) — earnings-vol SELL VOL Jun-10 (6d); needs defined-risk; on watchlist.
- **ACN** (raw 2) — earnings-vol SELL VOL Jun-18; clean 4/4 + insider buying; on watchlist.
- **TPR** (raw 1) — accumulation but flow-thin + fundamentals CAUTION; on watchlist.
- **BTU** (raw 1) — block DP buying but momentum-stage / flat 10d flow.
- **NVDA** (raw 1) — multileg bull spread vs two-sided sweep tape (CONFLICTED).
- **SNDK** (raw 0) / **AMD** (raw −2) — bearish semis sweeps blocked by `flow_conflict` (+$1.2B / +$421M 30d flow opposes the short).
- **MRVL** (raw 1) — two-sided event straddle, IV rank 100 (don't chase).
- **HTZ** — disqualified on the C12 liquidity floor.

---
*Watchlist `conviction_2026-06-04` = [NEE, MU, ORCL, ACN, TPR] written back. No `/stock-deep-dive` hand-off — no HIGH-tier names (no-edge day). §2 next-session GEX + 0DTE setup are advisory (0 points); §2/§2a do not enter the conviction rubric.*
