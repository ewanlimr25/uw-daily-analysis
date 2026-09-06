# Daily Market Analysis — 2026-06-15

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL (trend UPTREND, mixed signals — half size, defined-risk). SPY 754.8 (>20/50sma), QQQ 743.5, both **long-gamma (POSITIVE)** into the event. VIX **16.2 (LOW)**. Breadth near-even (pct_green 50.9%). Tech is the #1 net-inflow sector (+$7.78B) on a chip-led risk-on rally — but the semis **ETF** tape diverges bearish (SMH −$102.6M July puts).
- **Rubric regime status:** **OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half.** The ≥9 HIGH cut failed its 2026-06-12 re-confirmation; the P0.6 guard is active and risk-monitor enforces the half-cap (0/30 post-freeze calls resolved).
- **Next-session GEX (SPY/QQQ):** **SPY** long-gamma, ZGL 754.2 ≈ spot (knife-edge), call wall **755**, put wall **735** → pin/mean-revert prior, but lose 754 and it trap-doors short-gamma into 735. **QQQ** long-gamma, ZGL 739, call wall **750**, support **740** → 740–750 box, cushioned downside. *Advisory, see §2.*
- **Top swing build:** **None at conviction.** This is a no-edge, event-gated day. The single name clearing the quant floor (short **SMH**, raw 5/LOW) floors to **SKIP** after regime + FOMC-T+2 + tied-debate gates. win_rate 0.436 (market-excess +0.136), but it fights a risk-on tape at a 52-week high.
- **Top LEAP candidate:** **None.** leap-positioning-radar surfaced zero — every BUILDING name failed the cum-flow + conviction-matrix gates (bid-side deep-ITM financing, MIXED 90d flow).
- **Biggest risk:** **FOMC decision + SEP, Wed June 17 (T+2)** dominates every horizon, then OPEX Fri June 19. One correlation cluster — `SEMI_MEGACAP` {SMH/QQQ 0.95, SMH/MU 0.83, SMH/INTC 0.77}. Net book flat → no hedge sleeve required.

> **Desk read:** Stand aside. The disciplined output of a TRANSITIONAL, out-of-regime tape two days before a Fed decision and four days before OPEX is **no new directional risk**. The actionable content is structural (the OPEX pin book + the §2/§2a 0DTE advisory) and a single VOL watch (MU into its 6/24 print). Nothing earns more than starter pre-risk, and the one starter floors to skip.

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend **UPTREND** (SPY 754.83 > 20sma 745.86 > 50sma 724.78; +0.89% 30d; −0.73% from 90d high). Market breadth narrow: **bullish_pct 37.1%** (2,320 bullish vs 3,927 bearish flow tickers) — the tape is led by a handful of mega-caps, not broad participation. Guidance: half sizes, defined-risk, iron condors in range.

- **Per-index gamma (current-state EOD book):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 754.55 | 754.23 | +1.19B | long-gamma (POSITIVE) | 755 | 735 |
| QQQ | 743.54 | 738.97 | +0.66B | long-gamma (POSITIVE) | 750 | 740 (support, no −GEX shelf) |
| IWM | 294.66 | — | −72M | FULLY_NEGATIVE (flipped today) | 295 (real wall) | 290 (short-gamma pocket) |

  Both index regimes are **FRESH** — SPY/QQQ flipped back POSITIVE only on 06-11/06-12 after week-long FULLY_NEGATIVE runs (06-05→06-10). Do not treat the long-gamma pin as durable through Wednesday.

- **DTE volume share:** 0DTE **33.1%** / weeklies 32.1% / monthlies 20.6% / LEAP 5.1% — `regime_hint: BALANCED` (not retail-dominated; rotation/swing-eligible tape, LEAP share thin).
- **VRP (`uw historical vrp` SPY):** **FAIR** — IV30 0.1335 vs realised σ30 0.1444, vrp −0.0109. IV ≈ realised: no clear premium-selling or -buying edge at the index.
- **Macro backdrop (`scripts/fred_macro.py`):** yield curve **normal** (10y2y +0.40); **core CPI 2.96% / core PCE 3.29% YoY (sticky, above target)**; unemployment 4.3%, payrolls +172k; 10Y 4.48% (flat 30d); **USD strengthening**; fed funds 3.62%.
  **Forward `event_risk` (next ~10 trading days):**
  - **FOMC decision + SEP — Wed June 17 [Tier-1, HIGH]** — sticky core PCE + strengthening USD = live two-sided dot-plot risk.
  - Jobless claims + retail sales — Thu June 18 [MED].
  - **Monthly OPEX — Fri June 19 [MED].**

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book (OI persists overnight), read forward as the *prior* for tomorrow's open. Prose-only, **0 rubric points**, no backtested predictive claim. SPY/QQQ only.

| Index | Regime | ZGL (reliable?) | Call wall | Put wall | Structure bias (next-session 0DTE) |
|---|---|---|---|---|---|
| **SPY** | long-gamma POSITIVE (+1.19B) | 754.23 ✓ (on spot) | **755** (+415M, dominant strike in book) | **735** (−58M, true −GEX shelf) | Walls TIGHT, ZGL on spot → iron fly / butterfly centered **755** for the pin. Knife-edge: **lose 754 and it flips short-gamma into the 740→735 trap-door.** Tight range 753–757. |
| **QQQ** | long-gamma POSITIVE (+0.66B) | 738.97 ✓ (−0.6%) | **750** (heaviest +GEX above; 744–745 near-spot cluster) | **740** (+137M super-strike = structural support, NOT a −GEX shelf) | Walls moderately WIDE (~10pt box 740–750) → iron condor 740/750, or butterfly 744–745. Cushioned downside (no −GEX shelf — decelerates at 740, doesn't trap-door). |

**Cross-read:** Both long-gamma into FOMC, but SPY is on a knife-edge (ZGL = spot, 754 is the line) while QQQ has ~4.6pts of cushion. A bearish FOMC surprise flips SPY short-gamma faster (into 740→735) than QQQ (cushioned at 740).

**Mandatory caveats:** (1) EOD is a **prior, not a target** — fresh 0DTE OI re-computes the ZGL/walls in the first 30–60 min. (2) **Gap risk is elevated all week** — FOMC Wed, data Thu, OPEX Fri; a gap through the walls voids the prior before hedging engages. (3) ETF book, not the cleaner SPX/NDX index book. (4) uw cannot isolate the D+1 expiry — this is the 0–45d proxy. (5) Both regimes are FRESH (flipped 06-11/06-12), so the long-gamma pin is real for the open but not durable through Wednesday's decision.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — the validated stack)
The walls above are a **map, not a pin** (wall-as-magnet backtested NO_GO). What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points, NOT a guaranteed edge** (no vol shock in sample → short-vol left tail unsampled). Verdict: **GO_PREMIUM_SELL_INTRADAY** (both).

| Index | sell_premium | vol_state / VIX | implied move | exp. range | size | structure | net PnL/day (gross) | stand-aside / caution |
|---|---|---|---|---|---|---|---|---|
| **SPY** | yes | LOW / 16.2 | 0.75% | 0.77% | **0.5×** | iron fly / short straddle @ 754.5, wings ±0.77% | **+0.22%** (gross +0.32%) | — |
| **QQQ** | yes | LOW / 16.2 | 1.38% | 1.20% | **0.25×** | iron fly / short straddle @ 743.7, wings ±1.2% | **+0.31%** (gross +0.41%) | ⚠ Front-end backwardation (0DTE IV 1.35× VIX) — event/gap risk; half size |

- **PnL basis (P1.8):** figures are **% of underlying spot notional, lead with net-of-cost**; tiny in absolute terms. SPY ≈ SPX (trade either); **QQQ weaker** (Nasdaq index book unavailable) — lower confidence.
- **When:** enter at/after the open once the gap resolves; **hold to the close, never carry overnight** (overnight entry backtests negative). If it gaps beyond the wings, stand aside.
- **FOMC overlay:** Wednesday is the day NOT to be short bare front-end vol blind — the validated entry is intraday-only and delta-neutral; respect the QQQ backwardation caution all week. **Direction: none.**

## 2b. Swing Dealer Positioning (1–4 weeks)
- **No mechanized DEX flips** on the latest session. The market-wide flip to positive dealer-delta happened **06-11** (2 sessions stale — does not feed a scored line). Every "positive DEX" index/large-cap reading today (SPY +74B, QQQ +85B, NVDA +20B, MU +45B) is **beta in the up-tape, not a flip** — the exact level-vs-flip trap the P0.4 audit demoted the line for. Index swing bias: **NEUTRAL** across SPY/QQQ/IWM.
- **Two vanna-squeeze flags (hypothesis-grade, low conviction)** — the only candidates that could feed the +1 dealer-positioning line:
  - **CRM** — put-heavy book (net_vanna +4,647) + 4-session falling VIX (22.2→16.2, dated ^VIX), front-end IV ratio 1.35 (maturing). **Counter-caveat:** the single-leg-whale flagged a BEARISH floor put block on CRM ($20.4M 230P) — those puts ARE the put-heavy book; if they're informed bearish, the squeeze fails to ignite.
  - **MSFT** — put-heavy book (net_vanna +3,720) + same falling VIX, front ratio 1.24. Same bearish-put-block counter ($6.7M 460P) + accumulation-hunter read it as mega-SELL distribution.
  - Both carry an explicit bearish counter and resolve to low-conviction LONG hypotheses, not trade tickets. IWM flipped FULLY_NEGATIVE GEX today; QQQ front-end ratio 1.093 (front panicked into FOMC).

## 2c. Sector Rotation
- **Rotation regime: `no_change` (low confidence).** The GICS field is non-discriminating — 9 of 11 sectors read INFLOW at persistence 1.0 (a broad-tape artifact). Above-median magnitude + 1.0 persistence: Technology (+$7.78B), Comm Svcs (+$975M), Financials (+$476M), Industrials (+$320M). Consumer Cyclical is the only ROTATING read (0.6).
- **The decisive signal — the ETF tape contradicts the GICS Tech read.** GICS Tech prints +$7.78B at 1.0 persistence, but **every Tech ETF instrument is net-bearish on the 5d options tape**: XLK −$9.75M, **SMH −$102.6M (largest outflow in the 21-ETF universe)**, IGV mixed. SMH's deep-pull is wall-to-wall July put buying ($35M/$32M/$16M on the 525–600 strikes). The headline +$7.78B is retail-skewed single-name **call** premium (NVDA/MU/AMD) masking institutional **de-risking of the semis complex**. → Technology downgrades to watch-only.

**ETF flow tape (advisory — 0 rubric points):**

| ETF | Net premium dir | Persistence | DP / options read | GICS agreement | Note |
|---|---|---|---|---|---|
| **SMH** | **outflow −$102.6M** | strong | heavy July put buying (525p/545p/600p) | **DISAGREE** vs Tech +$7.78B | The standout contradiction — semis de-risking |
| KRE | outflow −$21.8M | consistent | DP = creation/redemption (not directional) | DISAGREE vs Financials | regional banks, watch-only |
| XBI | outflow −$8.56M | consistent | put-skewed | DISAGREE vs Healthcare | biotech de-risk |
| GDX | inflow +$26.4M | strong | **put-dominated** (Sep80p/70p) | n/a (Materials-proxy) | hedged-long, not clean bull |
| EWY | inflow +$10.0M | MIXED | rank-only | n/a (Korea) | instrument-only |
| XLE/XOP | inflow +$3.8M/+$3.1M | bullish | **put-dominated** | agree (Energy, tiny) | hedged-long |

- **Single-name leaders:** the only name passing the +1 sector-leader gate is **HPE** (Technology, +$75.6M clean bullish 30d, persistence 1.0, ≥$50M) — but it's **idiosyncratic** (HPE/Juniper, not the semis complex), not a sector vote. Every other "leader" (MU, NVDA, AMD, META, GOOG, TSLA, AMZN) fails the gate on mixed/opposed 30d cum-flow.
- **Implication:** trending broad-inflow tape with idiosyncratic leadership, **not** a sector rotation. Do not chase semis longs into July OPEX — the ETF tape says institutions are hedging the complex.

## 3. Swing Setups (1–6 weeks)
**No conviction swing setups today.** The quant scored exactly one name above the raw≥3 drop floor — a short **SMH** — and risk-monitor floored it to SKIP.

### 3a. Long swings (regime-aligned) — *none*
No long cleared confluence + scoring. The bullish single-agent names all carry disqualifiers: **HPE** (cleanest leader, +$75.6M, fundamentals CONFIRM) and **INTC** (+$77M, 95d calls) both scored raw 2 (single-agent confluence) and INTC drew a fundamentals **CAUTION** (unprofitable, 22% above sell-side target). **WULF** (multileg call vertical Jul-17 27/33, bullish, $33M) — single agent, high-IV miner, dropped. All are watch-only (§8).

### 3b. Short / fade swings (defined risk only) — *one, floored to skip*

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **SMH** | 5 (LOW) | Institutional semis de-risking — largest ETF outflow in the universe (−$102.6M July puts), 5-day opening put accumulation (525P ask 357:1), multileg 525/545 put vertical. Distribution-into-strength. | Defined-risk put debit spread expiring **after FOMC** (≥06-18), ≤ starter — only if expressed at all | Closes above 6/15 52w-high / reclaims with chip-led tape; bullish flow + OI-increasing persists into 06-16; dovish SEP. **Already half-invalidated by today's +$18.1M bullish flow reversal.** | **SKIP** (starter pre-risk → regime −1, FOMC-T+2 −1, tied-debate −1 floor it out) |

- **Why it floors:** win_rate 0.436 (market-excess +0.136 is genuine short alpha, but absolute WR < 0.50 floors to starter), the bull/bear debate **tied at 0.55** (did not clear the short), and it's a fight-the-tape short at a 52-week high two days before a Fed decision. Discretionary defined-risk only.
- **Contrarian-scanner:** 0 fades surfaced. VRP not positive blocks premium fades; **KLAC** (+3.8σ BEARISH_EXTREME) is **event-pending BACKWARDATION (ABORT)**, not crowded euphoria — a structural hedge bid, not a fade.

**Near-term sweeps (informational, 0 rubric points):** persistence-backed reads — **SMH** PUT/bearish (4/5, opening-confirmed), **INTC** CALL/bullish (4/5, opening-confirmed, 95d Sep calls), **GOOGL** PUT/bearish (3/5, cum_flow −$520M 30d). Direction-unconfirmed (persistent but mixed): MRVL, AMZN, MU, TSLA. Mega-cap hedge-flow (sweep ≠ cum_flow, not directional): QQQ, NVDA, MSFT, META.

**OPEX pin book (structural, into Fri 06-19)** — non-directional pin mechanics, scored +1 each (LOW/DROP), surfaced as the desk's expiry-week structure sleeve, **enter post-FOMC Wed**:

| Ticker | Pin | Spot | Distance | GEX-at-pin | Structure | FOMC gap risk |
|---|---|---|---|---|---|---|
| **NVDA** | 210 / 212.5 | 212.47 | 1.16% | +138M / +226M (on spot) | iron fly @ 212.5, wings ±5 | **HIGH** — highest-beta into SEP |
| **QQQ** | 740 | 743.82 | 0.51% | +126.5M (dominant) | short straddle / strangle 740 | **HIGH** — direct FOMC vehicle |
| **AAPL** | 300 / 295 | 296.44 | 1.20% | +50M twin walls | broken-wing fly, body 300 → 295 | MODERATE (most resilient) |

(IWM disqualified — short-gamma at the 290 pin; MSFT distance >2%; AMZN/GLD bottom-tercile pin_score; SOFI no OI-mass field.)

## 4. LEAP Builds (6–24 months)
**None.** leap-positioning-radar passed **zero** names against the 6-of-9 gate. The long-dated tape is macro/credit hedges (HYG/EEM/TLT/XLF puts), index put-hedging (QQQ), and bid-side deep-ITM financing structures — not fresh ask-side conviction. Disqualified near-misses (cum-flow + conviction-matrix failures): **ADBE** (3/9; MIXED −$10.3M 90d, conviction-matrix conf 12.8, bid-side deep-ITM C130), **CRWV** (2/9; MIXED conviction, balanced flow), **WULF** (2/9; −$63.6M 90d), **QQQ** (index, retail-diluted put-hedge tape). Re-scan next session; **CRWV** is first to re-examine if its '28 calls flip to ask-side with a turning 90d cum-flow.

## 5. Volatility Surface
**One tradeable dislocation: MU.** Everything else this week is FOMC/OPEX front-week contamination (every name's raw BACKWARDATION label is the 06-18 expiry carrying FOMC+OPEX, not a name-specific event).

- **MU** — idiosyncratic earnings kink: curve peaks at the **2026-07-02 expiry (152.7% IV, 7,931 contracts)**, the first tenor fully capturing the **June 24 PM earnings** (after FOMC/OPEX, so the hump is purely Micron's print). Single-name **VRP negative** (IV30 106.7% vs realised ~114.8% → vol cheap vs delivered → **buy-vol bias**); **skew COMPLACENT** (−0.044 to −0.049 — downside tail NOT priced). The surface says long-vol/long-the-event, NOT a premium-selling calendar. Routed to earnings-scout (§ below). *Caveat: all IV-percentile reads ran on n≈45 dates — provisional, not 252-day percentiles.*
- **KLAC** — DISQUALIFIED: ratio 1.579 is FOMC-contaminated front (1.21 IV) over a July monthly at 0.765; no near catalyst. Event-driven, not a calendar.
- **SUNB** — DISQUALIFIED on liquidity: back tenors 2–9 contracts (sub-floor); not constructible.
- **iv-outliers** returned only 0DTE QQQ/TSLA/AVGO mechanical noise — no whale-hedge mispricing.

**Earnings vol (earnings-scout):** No full-size trade. **MU** = SELL VOL **half-size** (earnings 6/24 PM, back-month skew complacent — front-only richness, no full-conviction sell; **note the vol-surface read disagrees and leans buy-vol** — the two agree VOL is the play, disagree direction, so it is a vol-structure decision, not a directional score). **ACN** SELL VOL half (6/18, but FOMC/OPEX-contaminated front). **JBL** SKIP (earnings on FOMC morning 6/17 — front maximally contaminated). No BUY VOL, no clean calendars.

## 6. Risk & Correlation
- **Macro headline:** sticky core PCE 3.29% + strengthening USD into a live **FOMC decision Wed June 17 (T+2)** — the gate that dominates every horizon this week. Then jobless/retail Thu, OPEX Fri. A swing book sized today carries un-priced Fed risk Wednesday; that is why every gate stack subtracts an event_risk tier.
- **Correlation cluster (`uw risk portfolio-correlation`, 30d):** one dominant cluster — **`SEMI_MEGACAP`**: SMH/QQQ 0.948, SMH/MU 0.832, MU/QQQ 0.803, SMH/INTC 0.771, INTC/QQQ 0.701. Treat as **one position** — SMH is the kept (highest-score) member; the rest are duplicative semis exposure. GOOGL (Comm Svcs) and HPE (0.551) are independent. NVDA is soft-watch only (0.61–0.68).
- **Fundamentals verdicts (top-5, no VETOs):** **SMH** NA (ETF; semis backdrop *contradicts* the short — chips led the 6/15 rebound). **GOOGL** CAUTION (−1) — insider buying +30.83 + beat streak fight the bearish flow → likely hedging. **MU** CONFIRM — real 6/24 binary (rich IV justified; date vol to the 6/26 cycle, NOT 6/19 OPEX). **INTC** CAUTION (−1) — unprofitable, 22% above target. **HPE** CONFIRM — beat streak, +40% rev, Juniper/Discover.
- **Event-risk flags:** FOMC Wed inside every swing horizon (−1 each). MU's own earnings 6/24 is 5 days *after* OPEX — any MU vol structure must be dated to the 6/26 cycle.
- **Debate-disconfirmation:** SMH bull 0.55 / bear 0.55 — **tied, did not clear the short** (−1 tier). Both sides conceded SMH is a fight-the-tape short at a 52w-high with a sub-coin base rate.
- **Adverse-flow exits (from `conviction_2026-06-12` = [SMH, ACN]):** **SMH — EXIT-CANDIDATE** (carried short): today's flow flipped **bullish (+$18.1M, OI +148.8k)** against yesterday's bearish thesis. **ACN — monitor** (no hard reversal). `fz` quote-drift clean on both (no SI/target/recom deterioration).
- **Breadth cross-check (`fz`, advisory):** advancers 256 / decliners 246, **pct_green 50.89%** — near-even, **no divergence** from the UPTREND-trend label (green tape, pct_green > 50). Top mover WDC +16.1%, worst FOXA −16.84%.
- **Hedge sleeve:** **none required** — net book is flat (the only directional name floored to skip). No SPY/QQQ vertical or VIX ladder warranted on a stand-aside book into a known FOMC binary.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**Empty — zero HIGH/MEDIUM names today.** No name scored ≥7; the Step-3a load-bearing-tool gate never engages (no HIGH candidates). The full scored book lives in `decision.json`. For completeness, the top of the (sub-threshold) book:

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no HIGH/MEDIUM calls to size, and no recent `/calibration-audit` per-tier expectancy table is being quoted; the live sizer remains the win-rate ladder (Step 5), itself capped at half by the out-of-regime guard.

| Ticker | raw | tier | class | win_rate (n, src) | mkt_excess | pre-risk | fund. | debate | final | note |
|---|---|---|---|---|---|---|---|---|---|---|
| SMH | 5 | LOW | bearish_flow | 0.436 (117, clean) | +0.136 | starter | NA | 0.55/0.55 tie | **SKIP** | semis de-risk short; floored by regime+FOMC+debate |
| GOOGL | 2 | DROP | bearish_flow | 0.436 (117, clean) | +0.136 | skip | CAUTION | — | watch | flow likely hedging (insider buying + beat streak) |
| MU | 2 | DROP | high_iv_rank | 0.80c (149, clean) | n/a | skip | CONFIRM | — | watch | real 6/24 binary; VOL watch (sell-vs-buy contested) |
| INTC | 2 | DROP | bullish_flow | 0.551 (118, clean) | −0.149 | skip | CAUTION | — | watch | unprofitable turnaround, beta |
| HPE | 2 | DROP | bullish_flow | 0.551 (118, clean) | −0.149 | skip | CONFIRM | — | watch | cleanest leader but single-agent + beta |
| NVDA/QQQ/AAPL | 1 | DROP | opex_pin | n/a | n/a | — | CONFIRM/NA | — | watch | OPEX pin book (structural, §3) |

**Backtest substrate note (P0.3):** both directional classes ran the clean-query protocol (complete forward windows, pinned `--top-n`, 29–39 clamped rows dropped); the raw tool headline is quarantined and never quoted. `bearish_flow` 0.436 carries genuine short-side excess (+0.136 vs SPY-down) but absolute WR < 0.50 governs the floor; `bullish_flow` 0.551 is negative-excess beta (−0.149) → C2 caps starter.

### Conviction-scoring rubric (frozen v2026-06-12) — embedded for audit
```
Daily conviction score = Σ:
  +1  dealer-positioning MECHANIZED DEX flip or vanna-squeeze (verified sign change; vanna needs dated falling-VIX)
  +3  accumulation 3+ aligned signals (DP+OI+smart-positioning, block-stratified institutional) — CONJUNCTION: full +3 only if cum_flow_30d confirms (sign aligned ∧ |flow|≥$50M); else halved +1
  +1  multi-day OI build (oi-trend BUILDING, days≥5)
  +1  conviction-matrix DIRECTIONAL_LONG conf>70 — CONDITIONAL: only when class==leap_directional
  +1  cum-premium-flow net directional accretion (30d) — INTENT-SCREENED (no C28 distribution_flag; no ex-div sub-parity arb)
  +1  sector-rotation single-name leader — CONDITIONAL: persistence≥0.6 ∧ cum_flow aligned ∧ |flow|≥$50M
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg directional structure (term-structure-anchored)
  +1  vol-surface KINKED/BACKWARDATION with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week)
  -2  contrarian overcrowded long with rising pc-ratio-zscore (VRP positive)
  -3  flow_conflict (cum_flow 30d clearly opposite class)  / -1 flow_conflict_lite (MIXED) — mutually exclusive
  [TIER GATES, risk-monitor 2d, not score_components]: -1 tier corr-cluster ≥0.70; -3→-1 tier regime conflict
Tiers: ≥9 HIGH (full*) · 7-8 MEDIUM (half) · 3-6 LOW (starter/watch) · ≤2 drop.
  *OUT-OF-REGIME guard (P0.6): all sizing capped at half until ≥30 resolved post-2026-06-12 calls re-validate the tiers.
```

## 8. Watch-only — single signal, no confluence
Surfaced by one agent, failed the ≥2-agent confluence gate. Journaling only, **not** for entry today.
- **HPE** — sector-rotation single-name leader (+$75.6M, fundamentals CONFIRM). Cleanest leader in the union; single-agent. Watch for a 2nd confirming flag.
- **INTC** — sweep-tracker Tier-1 bullish (95d Sep calls, opening-confirmed); fundamentals CAUTION (unprofitable, above target).
- **GOOGL** — sweep-tracker Tier-1 bearish (−$520M 30d); fundamentals CAUTION on the short (hedging signature).
- **CRM / MSFT** — dealer-positioning vanna-squeeze LONG (low conviction), each **contradicted** by a single-leg-whale bearish floor put block (CRM 230P $20.4M, MSFT 460P $6.7M). Conflicted; watch.
- **WULF** — multileg call vertical (bullish, $33M, high-IV miner); single agent.
- **INTU** — single-leg-whale bearish floor put block (440P $14.3M, advisory C19, 0 points); no scored flag.

---
*Single-leg whale scan (advisory C19, 0 rubric points): Tier-1 FLOOR_PUT_BLOCK bearish — CRM 230P $20.4M, INTU 440P $14.3M, MSFT 460P $6.7M (institutional puts on mega-cap tech into FOMC week). Promotion to a scored line still gated on the pre-registered ≥58% WR / ≥60-day / ≥2-regime bar.*
