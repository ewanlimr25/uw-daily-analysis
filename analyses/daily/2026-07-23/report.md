# Daily Market Analysis — 2026-07-23

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / CHOPPY — SPY 738.18, **below both 20SMA (745.92) and 50SMA (745.05)**, −2.92% from the 90d high; breadth bearish (31.9% bullish flow, 4,279 bearish vs 2,000 bullish tickers). VIX **18.7, spiking +2.1**. SPY & QQQ next-session gamma **FULLY_NEGATIVE (short-gamma)**; IWM short-gamma too. Sector lean: Tech (semis) the only durable inflow; Consumer Cyclical (TSLA −14.5% earnings) and Comm Services bleeding.
- **Rubric regime status:** **OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL/CHOPPY) — sizing capped at half.** First genuine non-uptrend tape since the freeze; the P0.6 guard is binding.
- **Next-session GEX (SPY/QQQ):** SPY — short-gamma, ZGL null (unreliable), put wall 735 / call wall 760; trend-amplifying, don't sell premium. QQQ — short-gamma, ZGL null, put wall 690 / call wall 715; same bias. Advisory, see §2.
- **Top swing build:** **NONE.** No name reached MEDIUM (7–8) or HIGH (≥9). Top of book is MU (LONG, raw 3, LOW) → gated to **watch-only** by the front-end panic override + fundamentals CAUTION + stacked FOMC/PCE event risk.
- **Top LEAP candidate:** **NONE.** 0 of the DTE>180 fresh builds cleared the 6-of-9 gate (all failed the cum-premium-flow accretion test).
- **Biggest risk:** No book → no directional exposure to hedge. The live risk is exogenous: a **front-end vol panic** (SPY front-end-IV ratio 1.178, BACKWARDATION) four trading days ahead of a **no-SEP FOMC (07-29, Warsh presser)**, with Q2 GDP (~07-30), June PCE (~07-31) and NFP (08-07) stacked behind it. Buying index protection here pays panic prices.

**Board verdict: EMPTY — ~18th consecutive all-DROP daily, but the FIRST in a real TRANSITIONAL/CHOPPY down-tape.** The empty-board discipline held in exactly the regime the calibration loop was waiting for. Kill mechanism was the familiar one: 30d cum-flow flow_conflict / weak nets vs the Phase-1 theses, the removed sweep-persistence line paying nothing on sweep-only candidates, and the panic/fundamentals/event gate stack finishing off the sole survivor.

---

## 1. Regime & Gamma State
`uw risk market-regime`: **TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity"; trend CHOPPY.** SPY 738.18, below 20SMA (745.92) and 50SMA (745.05), −2.92% from the 90d high, +0.63% over 30d. Market breadth is decisively bearish: **31.9% bullish** (4,279 bearish-flow tickers vs 2,000 bullish of 6,279 with options). Trading guidance from the regime engine itself: *half position sizes, favor defined-risk, iron condors in range.*

**Breadth cross-check (`fz`, advisory):** 213 advancers / 290 decliners, **pct_green 42.35%**, avg change −0.40%, median −0.38%. Worst mover TSLA −14.52% (earnings), top mover LMT +10.54%. This is an independent A/D lineage and it **confirms** the `uw` regime — index down AND pct_green < 50, no divergence to flag (a genuine risk-off day, not a distribution-under-a-green-tape tell).

**Per-index gamma (current-state EOD 0–45d book):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 738.35 | null (unreliable) | −$2.47B | FULLY_NEGATIVE / short-gamma | 760 (+2.94%) | 735 (−0.45%) |
| QQQ | 692.22 | null (unreliable) | −$1.18B | FULLY_NEGATIVE / short-gamma | 715 (+3.29%) | 690 (−0.32%) |
| IWM | ~292 | 195.74 (unreliable, >30% from spot) | −$0.91B | short-gamma (label POSITIVE is the ZGL-grid artifact; total_gex sign governs) | — | — |

All three indices are short dealer gamma into the open — hedging flow amplifies moves in either direction, with no positive-gamma dampening shelf near spot. §2 carries the forward read for SPY/QQQ.

- **`uw options-flow dte-volume-share`:** 0DTE 27.1% / weeklies 31.7% / monthlies 25.7% / LEAPs 2.9% → **BALANCED** (not a retail-0DTE-dominated tape; institutional positioning share is normal).
- **`uw historical vrp` (SPY):** IV30 15.72% vs realised 14.38%, **VRP +0.0134 → FAIR** — IV ≈ realised, no clean premium-selling or premium-buying edge at the index level.
- **Macro backdrop (`fred_macro`):** yield curve **normal** (+0.34 10y–2y); core CPI 2.81% YoY cooling, **core PCE 3.41% YoY sticky**; unemployment 4.2%, payrolls decelerating (+57k); **10Y 4.67% rising** (+16bp/30d), **USD strengthening**, fed funds 3.63%. A mild hawkish-drift backdrop. **Forward event_risk (next ~10 td):** FOMC 07-29 (HIGH, no SEP, Warsh presser), Q2 GDP advance ~07-30 (HIGH), June PCE ~07-31 (HIGH), NFP 08-07 (HIGH). Extremely event-dense — any swing structure opened today holds through at least two named Tier-1 binaries.

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book (OI persists overnight) read forward as the prior for the 07-24 open. Prose-only, **0 rubric points**, no backtested predictive claim. Scope: SPY & QQQ only.

Both indices print the **identical structural signature: FULLY_NEGATIVE dealer gamma, ZGL unrecoverable (null), heaviest negative concentration sitting just above spot** — dealers short gamma across the entire near-strike grid, set up to *amplify* whatever direction the tape takes at the open. This is not a pin setup.

| Index | Regime | ZGL | Call wall | Put wall | One-line structure bias |
|---|---|---|---|---|---|
| **SPY** | short-gamma (total_gex −$2.47B) | null (`zgl_reliable=false`) | 760 (+2.94%, weak <$50M pocket — not a true cap; note −$632M at 740 just above spot) | 735 (−0.45%) | Debit verticals / directional 0DTE in the realized-move direction, or a long straddle if direction is unclear. **Do NOT sell premium / run an iron fly into this book.** |
| **QQQ** | short-gamma (total_gex −$1.18B) | null (`zgl_reliable=false`) | 715 (+3.29%, negligible) | 690 (−0.32%, ATM; −$214M at 695 the dominant node) | Same short-gamma playbook: directional debit verticals or long straddle on the flip zone; avoid premium-selling structures. |

**Mandatory caveats:** (1) EOD is a *prior*, not a target — fresh 07-24 0DTE OI (the 2nd-largest expiry slice) recomputes the ZGL/walls in the first 30–60 min. (2) **Gap risk is elevated and could void the prior intraday** — FOMC (07-29), GDP (~07-30) and PCE (~07-31) sit inside the 0–45d window and VIX is already spiking +2.1 to 18.7. (3) ZGL is null on both (FULLY_NEGATIVE) — fall back to the total_gex sign + spot-vs-wall position. (4) These are the SPY/QQQ **ETF** books, not the cleaner SPX/NDX index books. (5) `uw` cannot isolate the D+1 expiry (`--dte-max 1` errors) — this is the 0–45d proxy. (6) Regime has been flipping every few sessions (fresh/unstable, not a held regime).

### 2a. Next-session 0DTE premium-selling setup (`zerodte_setup` — the validated stack)
**STAND ASIDE both SPY and QQQ today.** Advisory, delta-neutral, **0 rubric points**, NOT a guaranteed edge (validation sample has no vol shock — the short-vol left tail is UNSAMPLED).

- **Whether / how much / size:** `vol_state = HIGH`, **`sell_premium = FALSE`**, `size_scalar = 0.0` for both indices. VIX 18.7 spiking (+2.1) → **short-vol left-tail regime; stand aside.** Two mechanical reads (the 0DTE engine's VIX-spike stand-aside AND the FULLY_NEGATIVE GEX book) converge on the same "don't sell premium" call.
- **Context (backtest, not today's action):** the rolling verdict is `GO_PREMIUM_SELL_INTRADAY` on a quiet tape — SPY net PnL **+0.171%/day** (gross +0.271%, % of spot notional), win 93.3%; QQQ net **+0.31%/day** (gross +0.41%), win 88.3%. Today does not qualify — the VIX spike + backwardation is precisely the regime the stand-aside rule exists for. Expected next-day range if forced: SPY ~1.19%, QQQ ~1.96% (short-gamma / wider).
- **Direction:** none — delta-neutral. No directional tilt.

## 2a. Swing Dealer Positioning (1–4 weeks)
`dealer-positioning-strategist` (11 dated DEX sessions 07-09→07-23; VIX from the Yahoo chart API `^VIX`, which read clean 2026 closes):

- **SPY / QQQ / IWM — all SHORT bias.** Persistently negative DEX (SPY −50.5B, QQQ −37.0B, IWM −8.7B on 07-23), deteriorating, with front-end-IV ratios in BACKWARDATION (SPY 1.178, QQQ **1.301** — most panicked, IWM 1.131). **No mechanized DEX flip** — these are continuations of an established negative regime (the level-vs-flip distinction), so **no rubric points**.
- **TSLA — SHORT** (extreme negative DEX −9.65B, ~6× prior day, post-earnings −14.5%). A magnitude blowout inside an already-negative regime, front-end ratio 1.619 (already blown out) — not a fresh flip, and the move is largely priced.
- **MU — LONG, the ONLY qualifying mechanized DEX flip in the fleet.** net_dex 07-16 −6.76B / 07-17 −3.09B / 07-20 −5.68B (3 consecutive negative) → **07-21 +4.77B flip**, held 07-22 +3.60B and 07-23 +4.96B; |flip| ≥ 0.25× the trailing-10 median. Clean bullish DEX/charm alignment (call-heavy book), front-end ratio 1.069 (mild, still building). Earns the +1 dealer-positioning line (see §7).
- **No vanna squeeze anywhere** — VIX reversed from a 3-session decline to a spike today, killing the falling-VIX leg on every put-heavy book (SPY/QQQ/IWM/TSLA all downgrade to "vanna pressure, not squeeze").

## 2b. Sector Rotation
`sector-rotation-strategist`: **rotation regime = `no_change`.** Only **Technology (semis-led)** survives both the market-relative persistence/magnitude bar AND GICS↔ETF cross-confirmation.

- **Rotating IN (confirmed): Technology** — persistence 1.0, +$767.2M net today (50× the cross-sector median), SMH cross-confirms (+$83.6M 5d, the largest ETF inflow in the universe). Leaders: MU (+$103.8M today, 30d +$841.8M — **qualifies the scored +1**), DELL (+$34M, 30d +$66M — qualifies), IBM (+$26M), SNDK (+$21M), MRVL, TSM (30d actually **−$43.4M** — does NOT qualify, flagged).
- **Rotating OUT (confirmed): Industrials** — persistence 0.8, 4/5 days negative, XLI confirms (−$3.6M). Leader SPCX qualifies bearish (30d −$383.8M).
- **Watch-only (GICS says inflow, ETF disagrees):** Financial Services (XLF/KRE bearish — GICS strength is crypto/fintech-adjacent names, not banks), Consumer Defensive (XLP bearish), Energy (XLE bearish). Do not action.
- **Idiosyncratic, not rotation:** Consumer Cyclical −$3.04B today is TSLA-earnings-driven (single name, −14.5%); Comm Services −$784M flip (GOOGL/GOOG −$110M combined) has insufficient persistence for a call yet.

**ETF flow tape (advisory — strengthens the sector-leader +1, adds no points):**

| ETF | Net premium dir (5d) | GICS agreement | Note |
|---|---|---|---|
| SMH | **+$83.6M BULLISH** (largest) | agree (Tech) | The real engine of the Tech inflow; semis |
| XLK | +$3.85M bullish | agree (weak) | Consistent |
| XLI | −$3.62M bearish | agree (Industrials) | Confirms rotation-OUT |
| XLE | −$14.1M bearish | **disagree** (GICS says in) | Watch-only |
| XLF / KRE | −$2.3M / −$6.7M bearish | **disagree** (GICS says +$136M in) | Banks diverge from the GICS bucket |
| XLP | −$1.0M bearish | **disagree** (GICS says +$134M in) | Watch-only |
| XLY | +$15.0M bullish (5d) | agree-on-trend | But large Dec put sweeps = hedging into TSLA break |

## 3. Swing Setups (1–6 weeks)
**No scored swing setups. §3 is empty by design — a valid "no-edge" output, not a failure.**

The one confluence-passing name, **MU (LONG)**, scored raw 3 (LOW) and was gated to **watch-only** (see §6/§7). Everything else was single-signal or flow-contradicted.

**Informational — near-term directional sweeps (`sweep-tracker`, 0 rubric points):** the persistence-ranked tape is one-sided **bearish** and consistent with the risk-off day, but every name is either event-hedge-contaminated or single-agent:
- **GOOGL** (bearish, 3/5 persistence, opening-confirmed 77%) — but a broad front-day IV spike across dozens of strikes = **imminent earnings hedge**, not clean directional conviction. Watch-only.
- **SMH** (bearish near-dated puts, 99% opening) — protective semis hedge into FOMC; **conflicts** with the +$83.6M 5d bullish ETF inflow. Contested.
- **ORCL** (bearish, 8-for-8 puts, opening-confirmed 95%, + single-leg Tier-1 OPENING_PUT_PRIME) — but fundamentals CONTRADICT the short ($6.99B Pentagon contract announced after-hours + Mizuho Outperform $320 PT). Watch-only, dangerous short.
- Contested / disqualified: AMD (net-flow conflict), NBIS (bearish tag flipped), AMZN (split-term: near-term protective puts vs Oct opening call build), MU/INTC (mixed tape).

**Single-leg whale scan (advisory, C19, 0 points):** Tier-1 OPENING_PUT_PRIME on **SNDK, BE, ORCL** (institutional shorts against the tape). Note the 2026-07-18 audit holds C19 advisory — the aggregate short-selection direction still runs negative benchmark-excess; do not treat as a scored bearish line. And SNDK's short is directly contradicted by +$863.5M bullish 30d cum-flow.

## 4. LEAP Builds (6–24 months)
**No LEAP candidates. §4 is empty.** `leap-positioning-radar` cleared 0 of the DTE>180 fresh-build universe through the 6-of-9 gate. Every ask-dominant fresh call build (CMCSA, RDDT, ORCL 510C, TLT) **failed the cumulative-premium-flow accretion test** — the OI growth is not backed by net directional premium (the exact flow-vs-OI divergence the radar exists to kill). The top-20 fresh builds skewed to macro/rate hedges (TLT, XLU, XLP, SPX) and speculative small-caps (MARA, SPCX), not durable single-name conviction.

## 5. Volatility Surface
`vol-surface-scout` + `earnings-scout` (VRP FAIR at index → hunt single-name dislocations). We are mid-Q2-earnings; most elevated IV is event-pending, not a tradable dislocation.

- **Genuine kinks with adequate population:** **MSFT** (07-31 expiry, 12,123 contracts, iv%ile 90 — earnings 07-29) and **NRG** (08-07 expiry, earnings 08-04) are the only two with a resolvable, populated kink. NRG is the one name where the back-month is also stretched (TAIL_HEDGING, skew +0.063) → the safest **SELL VOL** (moderate size, iron condor / short strangle at 08-07).
- **CALENDAR candidates (extreme front panic + flat back-month → don't sell naked):** **FSLR** (earnings 07-30 = GDP day, front-end ratio 1.275, back-month COMPLACENT), **GO** (earnings 08-04, ratio 1.72, implied move 17.8%). Sell the event expiry, own the back leg.
- **WHR SELL VOL half** (earnings 07-27, ratio 1.094 under the panic line, back-month flat). **SWKS / SIMO SKIP** (SIMO reports 07-29 = FOMC day → unhedgeable macro tail stacked on the straddle).
- **Systemic data-gap note (extends the RMBS/MXL/SIMO class):** SWKS, SIMO, WHR, GO, BIRK, TENX, FIX, EW have **no listed expiry inside 29 DTE** despite near-term earnings → `front-end-iv-ratio` reads a FLAT/1.0 **artifact** (coverage gap, not calm). Do not read FLAT as bullish here.
- **Semis protective hedging (context, not a trade):** SMH 07-31 expiry carries $51.9M premium, **put-heavy** ($44.9M put vs $6.9M call), TAIL_HEDGING skew — genuine FOMC/PCE protection consistent across SMH/SOXX/SOXL/INTC. Every one fails the ratio>1.10-and-pending disqualifier → revisit post-07-29/07-31 for the calendar-fade once the ratio turns down.
- **No single-contract IV outliers** among the watchlist names (today's blowups are small-cap/meme: CIFR, EOSE, RIG, BB, JBLU). **DELL's apparent 09-04/09-18 IV uptick is an unweighted-avg artifact** (call-skew wings dominating the per-tenor average), not a real kink — do not size off it.

## 6. Risk & Correlation
`risk-monitor` consuming the candidate union + quant score + fundamentals verdicts (debate 2c skipped — no HIGH/MEDIUM names).

**Macro headline:** hawkish-drift backdrop (sticky core PCE 3.41%, 10Y 4.67% rising, USD strengthening) into an **extremely event-dense window** — FOMC 07-29 (no-SEP, Warsh presser, T+4), Q2 GDP ~07-30, June PCE ~07-31, NFP 08-07. Any swing structure opened today holds through ≥2 named Tier-1 binaries.

**Panic gate — FIRES:** SPY front-end-IV ratio **1.178 (BACKWARDATION) > 1.10** → the panic override reduces everything on the board one tier, no exceptions. This alone gates the sole survivor.

**Correlation clusters:** `semis_cluster` MU/SMH (corr 0.864) — kept member MU (raw 3 > SMH 0); `megacap_platform_cluster` AMZN/GOOGL (0.772) — academic (both dropped). No sized names → no double-counting to resolve.

**Fundamentals verdicts (top-3 by score):**
- **MU — CAUTION (−1 tier).** Real bullish catalysts (Musk "significant memory allocation" thank-you, Nvidia RTX-50-Super-delay margin tailwind, Google-capex read-through) + a clean 4/4 beat streak (+166.98% YoY revenue). **But insiders net-sold in 14 of the last 17 months (MSPR −33.33)** — the distribution-into-strength tell this gate exists to catch. Next earnings 2026-09-21 (60d out, no event gate). D/E 0.269, balance sheet clean.
- **ORCL — CAUTION (short contradicted).** 3/4 beats, +17.35% rev growth, and a **$6.99B DoW/Pentagon IDIQ contract** announced after-hours (+2.3% AH) plus Mizuho Outperform $320 PT. Shorting into a fresh government tailwind + upgrade momentum is asymmetric-against.
- **TSLA — CONFIRM (short).** −35.33% EPS miss, EPS growth −39% YoY, thin margins (op 5% / net 3.95%), insider selling (−45.35), P/E 363×. But the thesis is already ~14.5% realized today — a late/crowded short.

**Breadth divergence:** none to flag — `fz` pct_green 42.35% with the index down is consistent risk-off, not a green-tape distribution tell.

**Hedge sleeve: not required.** The conviction book is empty; net delta is zero. With the front-end already in backwardation (1.178), buying index protection pays panic prices.

**Adverse-flow exit candidates:** none — the `conviction_2026-07-22` group is empty (prior boards were also all-DROP), so `uw watchlist alerts` / `scan` returned nothing to exit.

**Watchlist write-back:** `conviction_2026-07-23 ← [MU]` only. MU is the sole LOW-tier (raw 3) name and is written back as watch-only for adverse-flow tracking (07-02 precedent); the DROP-tier names (ORCL/TSLA/AMZN/DELL, raw ≤1) are deliberately **excluded** so they don't poison tomorrow's correlation/adverse-flow universe with non-positions.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**No HIGH or MEDIUM names today.** The section is empty. The single confluence-passing candidate is documented below for the audit trail.

**Expectancy lens (advisory — C31) `[advisory — expectancy is not yet a live sizing axis]`:** no closed conviction calls to compute per-tier expectancy from — the `conviction_<date>` groups have been empty across the recent all-DROP boards, so there is no realised payoff-ratio to display this cycle. The live sizer remains the win-rate ladder (Step 5); the C3 fractional-Kelly sizer stays advisory.

**Watch-only survivor breakdown — MU (LONG, gated out):**

| Field | Value |
|---|---|
| raw_score | **3 (LOW)** |
| score_components | +1 dealer-positioning MECHANIZED DEX flip (`uw options-structure dex`); +1 sector-rotation single-name leader (`sector-flow-persistence`: Tech persistence 1.0, 30d cum-flow +$841.8M aligned, ≥$50M); +1 cum-flow accretion 30d (intent-screened clean, no distribution_flag) |
| dominant_signal_class | sector_rotation |
| win_rate | **NA(substrate)** — `sector_rotation` is not a backtest `--signal-type`; clean protocol cannot complete. (Routing-robustness: had it routed `bullish_flow`, clean WR 0.386 n=145 < 0.50 → starter/skip anyway.) |
| cum_premium_flow 30d / 90d | +$841.8M / +$413.4M |
| pre-risk size | starter |
| fundamentals_verdict | **CAUTION (−1)** — insider net selling 14/17 months underneath the accumulation thesis |
| bull/bear residuals | NA (debate skipped) |
| gate_verdicts | panic **−1** (front-end 1.178 > 1.10) · fundamentals **−1** (CAUTION) · event_risk **−1** (FOMC 07-29 T+4 + PCE 07-31 T+6, stacked) · rubric_regime capped-half (OUT-OF-REGIME) · regime/vrp/cluster/sector/debate no-op |
| final size | **WATCH-ONLY** (the panic override alone takes starter → skip before fundamentals/events are even counted) |
| invalidation | 30d cum-flow flips negative; DEX reverses negative ≥3 sessions; or the tape preference simply doesn't return until the 07-29/07-31 prints clear |

**Note the correct posture:** a LOW-tier long with persistent insider distribution underneath it, entering at IV rank 85.5 (rich long premium), in a below-both-SMA choppy tape, four trading days ahead of a no-SEP FOMC + PCE, inside a live front-end vol panic. Watch-only is the graded-correct call. Revisit MU after 07-29/07-31 if the panic ratio resolves back under 1.0.

**Conviction-scoring rubric (frozen `2026-06-12`), embedded for audit:**
```
Daily conviction score = Σ:
 +1 dealer-positioning MECHANIZED DEX flip (verified sign change, not level)
 +3 accumulation conjunction (DP+OI+smart-positioning+block-stratified inst-tier); halved→+1 if cum_flow_30d not aligned or <$50M
 +1 multi-day OI build (oi-trend BUILDING, --days≥5)
 +1 conviction-matrix DIRECTIONAL_LONG conf>70 — only if class==leap_directional, else 0
 +1 cum_premium_flow net accretion 30d — intent-screened (0 if distribution_flag / dividend-capture arb)
 +1 sector-rotation single-name leader — persistence≥0.6 AND cum_flow_30d aligned AND ≥$50M
 +1 earnings-scout BUY VOL / SELL VOL
 +2 multileg directional (term-structure-anchored play type)
 +1 vol-surface KINKED/BACKWARDATION with VRP-aligned bias
 -2 contrarian overcrowded long with rising pc-ratio-zscore
 -3 flow_conflict (30d cum-flow clearly opposite dominant class)   |  -1 flow_conflict_lite (MIXED) — mutually exclusive
 [TIER GATES, risk-monitor 2d, not score points]: -1 tier correlation cluster; -3→-1 tier regime conflict
Tiers: ≥9 HIGH (full) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 drop.
Out-of-regime guard (P0.6): all sizing capped at half until a /calibration-audit clears ≥30 post-2026-06-12 resolved calls.
```

## 8. Watch-only — single signal / contested / no confluence
For journaling, **not** for trade entry today:

| Ticker | Signal | Why watch-only |
|---|---|---|
| DELL | sector-rotation Tech leader (30d +$66M) | 1 agent only; bottom-quartile net → flow_conflict_lite; no near-term earnings |
| ORCL | sweep Tier-A bearish + single-leg Tier-1 | 1 Phase-1 agent + advisory; fundamentals CONTRADICT (Pentagon contract) |
| TSLA | dealer-positioning SHORT; fundamentals CONFIRM miss | Priced −14.5% already; 1 agent; late/crowded short |
| SMH | sweep bearish hedge vs +$83.6M bullish 5d inflow | Direct agent conflict (protective puts vs ETF inflow) |
| GOOGL | sweep Tier-A bearish; Comm Services leader | Earnings-imminent BACKWARDATION = event hedge; flow_conflict_lite |
| SNDK | single-leg Tier-1 OPENING_PUT_PRIME | Short **contradicted** by +$863.5M bullish 30d flow (−3 flow_conflict) |
| AMZN | multileg bullish call spread (event 07-31) | −1 flow_conflict_lite (flat/bearish 30d); split-term; event-driven lottery |
| AMD / NBIS / PLTR / INTC / LULU | various | Contested / disqualified (net-flow conflict, tag flip, not-extreme z, mixed tape) |
| MSFT / NRG / FSLR / GO / WHR / SIMO / SWKS | earnings-vol (§5) | Non-directional vol plays, not conviction-book entries |

---
*Fleet: 11 Phase-1 alpha-finders (no OPEX agent — 6 td past July third-Friday) → quant → fundamentals-gate → risk-monitor. Debate (2c) skipped per empty-board protocol (no HIGH/MEDIUM). `fz` squeeze/RS screens returned mangled synthetic tickers this run and were treated as advisory-skip; `fz` breadth + enrich lanes ran clean. `zerodte_setup` = stand-aside. Rubric frozen 2026-06-12, OUT-OF-REGIME.*
