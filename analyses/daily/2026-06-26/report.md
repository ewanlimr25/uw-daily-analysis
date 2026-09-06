# Daily Market Analysis — 2026-06-26

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / CHOPPY — SPY 728.99 below its 20- (743.6) and 50-SMA (734.35), −2.86% 30d, −4.13% off the 90d high; VIX 18.41; flow breadth 38.2% bullish (sub-40 = defensive); 0DTE share 48.1% (retail-dominated). **SPY and QQQ are both FULLY_NEGATIVE / short-gamma** (vol-amplifying). Sector lean: no durable rotation (every GICS sector low-persistence); semis sold off, software rotated in intraday. **Today is Q2 quarter-end (Russell reconstitution) — dark-pool prints are rebalance-distorted; discount single-name DP "accumulation."**
- **Rubric regime status:** OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half. *(Moot today — no book to size.)*
- **Next-session GEX (SPY/QQQ):** **SPY** short-gamma, ZGL null (FULLY_NEGATIVE), call wall 734 / put wall 730 — coiled 730–735 hinge, play the break, not the pin. **QQQ** short-gamma, ZGL null, no meaningful call wall / dominant put wall 705 (−206M) — asymmetric, lean-down-with-acceleration if 707/705 fails. Advisory, see §2.
- **Top swing build:** **NONE.** Zero names cleared the raw-score ≥3 floor. The book is flow-conflict-heavy — every directional multileg (NVDA long, SMH/IGV short) fights its own 30-day net premium; the one qualitatively strong short (MSFT, DP distribution + Tier-1 floor put) earns only +1 because the additive rubric has no symmetric short line. **No high-conviction directional trade today.**
- **Top LEAP candidate:** **NONE.** Thin LEAP tape (4.7% share); zero names passed the 6-of-9 gate stack. NOW is the lone watch (positive 30/90d accretion) but conviction-matrix is retail-diluted to 19.8.
- **Biggest risk:** **June NFP at T+4 (Thu 2026-07-02, pulled forward ahead of the July 3 market close)** into a short-gamma, FAIR-VRP, no-premium-cushion tape. One real correlation cluster: software-megacap {MSFT, IGV} at 0.884. Hedge sleeve: stay long convexity into NFP, do **not** sell naked premium.

---

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend CHOPPY. SPY 728.99, above_20sma **false**, above_50sma **false**, −2.86% 30d, −4.13% from 90d high. Market breadth: 2,385 bullish-flow vs 3,854 bearish-flow tickers (38.2% bullish) — a defensive, bearish-leaning tape. Trading guidance: half sizes, defined-risk, iron condors in range.
- **Per-index gamma (current-state EOD book):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | ~732 (book) / 728.99 (close) | null (unreliable) | −1.36B | **FULLY_NEGATIVE** | 734 | 730 / 731 |
| QQQ | ~708 (book) / 706.52 (close) | null (unreliable) | −0.87B | **FULLY_NEGATIVE** | none meaningful | 705 (−206M) |
| IWM | ~298 | 140 (nonsensical, ignore) | ~−61M (low-mag) | whipsaw/flat | — | — |

  Both index majors are deeply short-gamma — the dealer book **amplifies** moves rather than dampening them. (§2 carries the forward, next-session advisory read of these same SPY/QQQ levels with concrete 0DTE structure.)
- **`uw options-flow dte-volume-share`:** 0DTE **48.1%** (RETAIL_DRIVEN), weeklies 20.6%, monthlies 16.8%, LEAPs 4.7%. A retail-dominated, short-dated tape — single-day signals are noise; weight multi-day persistence.
- **`uw historical vrp`:** **FAIR** — SPY IV30 16.1% vs realized 15.1% (VRP +0.0107); QQQ IV30 28.0% vs realized 27.7% (+0.0029). IV ≈ realized: **no premium-selling cushion** at the index.
- **Macro backdrop (`fred_macro.py`):** yield curve **normal** (+0.31, 10Y−2Y); core CPI **2.96%** YoY, core PCE **3.41%** YoY (still sticky above target); unemployment 4.3%, payrolls +172k; 10Y **4.4%** (falling −0.1 over 30d); USD strengthening; fed funds 3.63%. **Forward event_risk (next ~10 trading days):** **June NFP — Thu 2026-07-02 (HIGH; pulled forward ahead of the July 3 Independence Day market close)**; jobless claims 07-02 & 07-09 (med); **June CPI — ~2026-07-14 (HIGH, just outside the 10-day window)**; FOMC 07-28/29 (outside window).

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book (open interest persists overnight), read forward as the *prior* for the Mon 2026-06-29 open. Prose-only, 0 rubric points, no backtested predictive claim. Scope: SPY & QQQ only.

### SPY — FULLY_NEGATIVE / short-gamma
- spot ~732.14 (book) · ZGL **null** (`zgl_reliable=false`; the time-series ZGL prints of ~300–327 are extrapolation garbage) · total_gex **−1.36B**
- **call wall 734** (+69.98M, the only meaningful long-gamma shelf above spot) · **put wall 730/731** (−138M / −124M); deeper accelerant cluster 725 (−129M) / 720 (−124M). The single most-negative strike, **735 (−147.8M)**, sits just *above* spot — a short-gamma accelerant cap, not support.
- **Read:** short-gamma / trend / vol-expansion. The 730–735 zone is a thin, all-negative coiled hinge ~4 pts wide. A break below 730/731 mechanically begets selling toward 725→720; a poke above 734 runs into the 735 negative-gamma cap. Realistic next-session band absent a gap ≈ 725–740.
- **Structure bias:** debit verticals / directional 0DTE / long-straddle-on-the-flip — **not** a pin/short-vol structure. Fade-the-poke condors are inappropriate in this short-gamma regime. (5th consecutive FULLY_NEGATIVE session since 06-22 — durable, not a one-day artifact.)

### QQQ — FULLY_NEGATIVE / short-gamma
- spot ~708.02 (book) · ZGL **null** (`zgl_reliable=false`) · total_gex **−0.87B**
- **call wall: none meaningful** (724/730 only trivially positive) — upside is unanchored. **put wall 705 (−205.98M)** — by far the dominant strike in the book, ~3 pts below spot; flanked by 707 (−75.9M) under spot and 710 (−66.4M) above; accelerant at 700/695.
- **Read:** short-gamma / trend, heavily asymmetric. A break of 707→705 hands dealers a forced-sell cascade toward 700→695; with no symmetric call wall, a relief rally faces little resistance and can extend. Band absent a gap ≈ 700–716.
- **Structure bias:** directional / debit structures; defined-risk put-debit / breakdown if 707 fails, defined-risk call-debit on a reclaim of 710. The 705/707 shelf is the clean trade tell.

**Mandatory caveats:** EOD is a *prior, not a target* (fresh 0DTE OI re-computes ZGL/walls in the first 30–60 min — and 0DTE is 48% of volume, so it re-weights fast); **gap risk voids the prior** — NFP-shortened week, cross-check the open against this map; this is the SPY/QQQ **ETF** book, not the cleaner SPX/NDX index book; `uw` cannot isolate the D+1 expiry, so this is the standing 0–45 DTE aggregate as the next-session proxy.

### 2a. Next-session 0DTE premium-selling setup (`zerodte_setup.py` — the validated stack)
Delta-neutral premium-selling edge (the GEX walls are a *map*, not a pin — wall-as-magnet and every directional 0DTE signal backtested NO_GO). Advisory, **0 rubric points**, NOT a guaranteed edge (validation sample has no vol shock — short-vol left tail unsampled). Rolling backtest **verdict: GO_PREMIUM_SELL_INTRADAY** (SPY n=53, QQQ n=53).

| Index | sell_premium | vol_state | VIX | implied move | exp. range | size | structure | PnL/day (gross → **net**) |
|---|---|---|---|---|---|---|---|---|
| SPY | true | MID | 18.41 | 0.74% | 1.25% | 1.0× | wider iron condor, wings ≈ ±1.25% | +0.323% → **+0.223%** |
| QQQ | true | MID | 18.41 | 1.31% | 1.90% | 1.0× | wider iron condor, wings ≈ ±1.9% | +0.440% → **+0.340%** |

- **Whether (VRP):** front-expiry implied move systematically exceeds realized open-to-close. **PnL basis: % of underlying spot notional, GROSS** — net is after the assumed 0.1% round-trip cost. Lead with **net** (SPY +0.22%, QQQ +0.34%) — tiny in absolute terms, and a negatively-skewed seller's edge that gross win-rate overstates.
- **How much:** short-gamma → wider next-day range → wings out (or reduce). **When:** enter at/after the open once the gap resolves; hold to the close; **never carry overnight** (overnight PnL is negative). **Size (VIX):** MID vol, 1.0× scalar. **Stand-aside:** none flagged today — *but* this is the wrong regime to be over-eager: FAIR VRP + short-gamma + NFP at T+4 means a miss gets amplified. **Direction: none — delta-neutral.**
- **SPY ≈ SPX** (validated identical); **QQQ weaker** (Nasdaq index book unavailable) — lower confidence. This lane stays advisory / 0 points permanently until a vol-shock day enters the sample AND net expectancy clears a tail-aware bar.

## 2a. Swing Dealer Positioning (1–4 weeks)
`dealer-positioning-strategist`: **SPY and QQQ both swing_bias SHORT / defensive.** Negative DEX **and** negative GEX, sustained 3–5 sessions (verified, magnitude-passing flips: SPY 6/22, QQQ 6/23 — but both **stale**, matured into a sustained de-risked regime, not a fresh today-signal). Front-end IV ratio **1.66–1.76 BACKWARDATION** (forward stress). **No vanna squeeze fires anywhere** — every book is put-heavy (qualifies on book side) but VIX is chopping 18–19, not falling ≥3 sessions → classify as **vanna pressure, not squeeze**. A VIX break below ~16 with the put-heavy book intact is the single catalyst that would flip the index bias LONG.
- **IWM:** NEUTRAL (DEX oscillates around zero; no clean run).
- **MSFT:** NEUTRAL — 10-session negative-DEX run snapped to ~zero today on a +5.6% bounce, but the flip **FAILS the magnitude gate** (|flip| 0.071B = 0.015× the trailing-10 median) → whipsaw artifact, not a verified flip. If MSFT prints positive DEX for 2–3 sessions it *becomes* a bullish flip — re-check, but it is not one today.
- **AAPL:** NEUTRAL (DEX noisy, single negative session inside positives).
- **NFP 07-02 lands into a negative-gamma book that amplifies the reaction** — the key near-term vol event for this swing window.

## 2b. Sector Rotation
`sector-rotation-strategist`: **rotation_regime = `no_change` (low confidence).** Every GICS sector reads INFLOW with persistence_score = 1 (the choppy/low end) — no sector clears the market-relative standout bar; the field is uniform. Market 0DTE share 48.1% (retail) → all rotation conviction downgraded uniformly. **No rotation trade.**
- **Healthcare** — the single cleanest *accelerating* GICS inflow (5d 197M→510M), but **WATCH-ONLY**: its ETFs disagree (XLV −3.4M, XBI −11.4M both bearish 5d) — the inflow is concentrated in large-cap pharma (LLY +37.5M, UNH, JNJ), not the broad/biotech baskets.
- **Technology** — largest absolute flow but **ambiguous**: call premium +3.21B while the regime's directional/DP measure shows −637M OUT, and decelerating from Monday. ETF tape contaminated — SMH/IGV top the 5d inflow rank but the sweeps are dominated by **bid-side put buying** (SMH $57M+$47M puts; IGV $52M+$22M Jan-27 puts) = **hedging, not accumulation**.
- **Fading:** Industrials (257M→157M, XLI −3.0M), Financials (276M→121M, XLF −2.2M). **Largest single ETF outflow: XBI −11.4M** (biotech de-risk).

**ETF flow tape (advisory)** — strengthens nothing into a scored line today; the tape is hedging, not accumulation.

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| SMH | inflow (+128.7M)* | 5d bullish *contaminated* | $48M/$31M DP creations | **bid-side PUTS** ($57M+$47M) = hedging | agree-but-ambiguous (Tech) | NOW, MSFT, NVDA |
| IGV | inflow (+76.9M)* | 5d bullish | $108M DP print | **bid-side Jan-27 PUTS** ($52M+$22M) = hedging | agree-but-ambiguous (Tech) | MSFT, NOW |
| GDX | inflow (+30.8M) | 5d bullish | $82M at-mid DP | thin, mixed | n/a → Materials partial | — |
| XLV | outflow (−3.4M) | bearish | $48M+$38M DP (redemption) | thin | **disagree** w/ accelerating GICS HC | NTRA, CNC, TMO (out) |
| XBI | **outflow (−11.4M)** | bearish (largest) | $26M below-mid DP | thin | **disagree** w/ GICS HC | biotech de-risk |

  *SMH/IGV "inflow" is call-side premium; the directional sweeps are put-heavy → read as hedging, GICS agreement downgraded to ambiguous.

## 3. Swing Setups (1–6 weeks)
**No qualifying swing setups.** No name cleared the 2-agent confluence gate AND the raw-score ≥3 floor. The directional candidates that surfaced are all flow-conflicted or sub-floor; they appear below for journaling only.

### 3a. Long swings (regime-aligned)
**NONE sized.** Candidates examined (all DROPPED):
- **UBER** (raw +1, DROP) — accumulation-hunter DIRECTIONAL_LONG 54.1, DP $1.4B @ 76.20, OI BUILDING 5/5 — but the print is the **Q2 Russell-reconstitution closing cross** (rebalance, not conviction), options smart-positioning leans bearish (call-writing), cum_flow 30d −$38.5M (fails the +3 accumulation conjunction → halved to +1; flow_conflict_lite −1 → net +1). Fundamentals **CAUTION −1** (3/4 EPS misses). **Invalidation:** loses the $76.20 DP shelf.
- **NVDA** (raw −1, DROP) — multileg 220C 10-16 $56M bullish Q3 (+2) but cum_flow 30d **−$545M** / 90d −$337M deteriorating → **flow_conflict −3**. Best fundamentals on the board (CONFIRM: +70% rev, 64% op margin, Recom 1.25, RSI 37.5) — the single-day call whale is fighting a quarter of net-bearish premium. **Invalidation:** loses the 200-handle / 220C OI bleeds.

### 3b. Short / fade swings (defined risk only)
**NONE sized.** Candidates examined (all DROPPED / watch-only):
- **MSFT** (raw +1, DROP — the strongest *qualitative* short) — accumulation-hunter **DP DISTRIBUTION** (mega buy_ratio 0.096, sell-side $21.6B; conviction-matrix DISTRIBUTION) + Step-0 single-leg whale **Tier-1 FLOOR_PUT_BLOCK 425P** $2.37M (C19 advisory, 0 pts) + a 10-session negative-DEX history. Earns only the cum-flow +1 (−$521M bearish-aligned) because the additive rubric has **no symmetric short-distribution line**. Fundamentals **CAUTION −1**: 4/4 beats, 47% op margin, Recom 1.23 / +50% target all fight the short; only insider-selling backs it — shorting an oversold (RSI 40) compounder into a software rotation-in. *Note the DP sell-side is plausibly quarter-end rebalance crossing, not conviction distribution.* **Invalidation:** reclaims and holds above the distribution level / DEX prints positive ≥3 sessions.
- **SMH** (raw −1, DROP) — multileg $113M bearish put diagonal (600P 07-02 / 540P 07-17) into NFP (+2), but cum_flow 30d **+$161M** opposes the short → **flow_conflict −3**. Semis sold off today (sector-corroborating). **Invalidation:** SMH rallies through 600 and holds.
- **IGV** (raw −1, DROP) — multileg $74M clean 80/70 put debit spread (2027-01-15 LEAP) bearish software (+2), but cum_flow 30d **+$87.5M** opposes → **flow_conflict −3**; software rotated IN today (MSFT +5%, NOW +9.9%) cuts against it; cluster −1 (corr 0.884 with MSFT). **Invalidation:** software rotation-in holds / paired OI unwinds.

**Near-term sweeps (informational, 0 rubric points):** No first-class directional sweep today. Every persistent name (MU, SNDK, SPCX, AMD, INTC, MRVL, MSTR — all 5/5 or 3–4/5 sessions) is either hedge-flow-filtered (mega-cap, cum_flow MIXED — SPXW/SPY/QQQ/TSLA/NVDA/META), catalyst-clustered (**MU** imminent earnings), or directionally conflicting (SNDK/SPCX/MSTR window-vs-opening). Best LOW-tier narrative: **INTC short** (130P 07-17 +11.4k OI opening build, non-mega-cap) — but no co-flag, so watch-only (§8).

## 4. LEAP Builds (6–24 months)
**No LEAP candidates pass.** Thin LEAP tape (DTE>180 = 4.7% of volume) in a TRANSITIONAL regime with SPY below its SMAs. The binding disqualifier across the universe is **cum-premium-flow (Gate 4) + conviction-matrix (Gate 8)** — not one name combines a bullish 90d slow-accretion signature with DIRECTIONAL_LONG matrix >70.

Near-misses (failed filter):
- **NVDA** — best ask-side LEAP build (C205 dte356 / C300 dte721, ~$38M), but cum_flow 90d −$337M / 30d −$545M deteriorating + matrix 28.7. Drawdown bounce-fish, not slow accumulation.
- **NOW** — highest LEAP-tenor presence (9/10 days) and the **only** name with positive accretion on both 30d (+$79M) and 90d (+$77M) windows, but matrix **19.8** (retail-diluted) and thin magnitude → **watch-only** (§8), not a buy.
- **NBIS / META / UBER / LLY / TSLA** — all fail Gate 4 (wrong-direction or reversing 90d flow) and/or Gate 8 (matrix not DIRECTIONAL_LONG >70). Disqualified on sight: FXI/KWEB/BABA (bid-side or roll-back), SBET/HTZ/SNAP (sub-$5 liquidity floor), TLT (rate hedge).

## 5. Volatility Surface
`vol-surface-scout`: index VRP FAIR → relative-value vol (calendars / event-isolation) over outright index premium selling. The semis cluster (AMAT/ADI/TXN/TER, all iv_rank 100) turned out **NOT** to be the dislocation — their front bulge is the **July 2 NFP macro premium** (AMAT ratio 2.04 isolates entirely to the NFP-week expiry); do not sell the dte-6 NFP straddle, the event is still pending.

**Two genuine event-vol calendars (both PREMIUM_SELLING VRP + confirmed earnings kink) — handed to earnings-scout, watch-only here:**

| Ticker | Structure | Kink tenor | VRP | Catalyst | Bias |
|---|---|---|---|---|---|
| **TSCO** | KINKED at earnings tenor (dte-28 Jul-24 55.8% vs dte-56 47%, ratio 1.187) | Jul-24 | **+0.172 PREMIUM_SELLING** (richest in scan) | **Earnings 2026-07-23** | short the Jul-24/31 tenor vs long Aug-21 (short calendar) |
| **ABT** | KINKED at earnings tenor (dte-21 Jul-17 35.3% vs dte-56 31.4%, ratio 1.122) | Jul-17 | **+0.0875 PREMIUM_SELLING**, TAIL_HEDGING skew | **Earnings 2026-07-16** | short Jul-17 vs long Aug-21 put calendar (harvest skew + event premium) |

**Percentile caveat:** every `iv-percentile-zscore` returned `dates_used: 53` (< 120-day floor) → all percentile labels are PROVISIONAL n=53; lead with the z-score (TSCO 2.41, ABT 2.49). **IV outliers:** all 0DTE penny-strike garbage (GRAB/BULL/UNG max_iv 4000%+) — no clean whale-hedge mispricing. **NXPI** is the only PREMIUM_BUYING name (VRP −0.069) but flat term / no catalyst → pass.

## 6. Risk & Correlation
**Macro headline:** TRANSITIONAL / CHOPPY, VIX 18.41, **VRP FAIR (no premium cushion)**, breadth 38%, both index majors short-gamma. Core PCE 3.41% YoY still sticky; 10Y falling to 4.4%; USD strengthening. **Forward event_risk: June NFP Thu 2026-07-02 (T+4, HIGH binary); June CPI ~2026-07-14 (T+11, just outside the window).**

- **Correlation clusters** (`uw risk portfolio-correlation`, 30d): **`software_megacap_cluster` = {MSFT, IGV} at corr 0.884** — same short-software bet; keep MSFT (higher raw), IGV takes the −1 cluster tier. **NVDA / SMH at 0.698 = soft-watch only, no penalty** (mechanical threshold — no discretionary upgrade despite the natural semis pairing). 100% top-sector (tech/semis/software) across all 5 candidates, but nothing is sized → book concentration moot.
- **Regime / VRP / panic gates:** all no-op (nothing sized). Front-end backwardation 1.66–1.76 is *forward* stress, not a >1.10 spot-panic override on any structure.
- **Fundamentals verdicts (top-5):** **UBER CAUTION** (3/4 EPS misses vs strong rev / insider-buying / Recom 1.35); **MSFT CAUTION** (4/4 beats + Recom 1.23 fight the short; only insider-selling −83.89 backs it); **NVDA CONFIRM** (cleanest fundamentals; flow weakness = high-beta dip); **SMH / IGV NA** (ETFs — SMH sector-corroborated by semis sell-off; IGV cut against by software rotation-in). **No VETO.** `fz` analyst axis is loud and consistent: Recom ≈1.2–1.35 across all three single names with +38–61% upside — corroborates the longs, fights the shorts. Squeeze pressure LOW on all (SI 1.3–2.8%).
- **Event-risk flags:** all single-name earnings are 32–60d out (MSFT 07-28, UBER 08-04, NVDA 08-25) — outside any near-term horizon. NFP at T+4 is the binding macro event for anything held through next week.
- **Debate:** SKIPPED this run (no MEDIUM/HIGH name to stress-test) — debate gate no-op / NA residuals.
- **Adverse-flow exit list:** scanned `conviction_2026-06-25` {META, NVDA, MU, NKE, IWM} — all fired LARGE_DARK_POOL / OI_SHIFT alerts but these are **positioning, not reversals** (NVDA/META/MU flow still bullish today); `fz` drift tripwire clean (NVDA drift is purely price-mechanical). **No exit candidates.**
- **Breadth cross-check (`fz`, advisory):** advancers 324 / decliners 178, **pct_green 64.4%**, avg +0.55% (top MRNA +12.6%, worst ON −23.7%). Index green AND pct_green > 50 → **no divergence flag**. Note the price/flow tension: a green *price* tape (64% green) against a bearish *flow* breadth (38.2% bullish) — price up broadly while options positioning stays defensive.
- **Hedge sleeve / defensive posture (standalone — no book to overlay):** (1) **Long convexity into NFP**, not premium-selling — a modest VIX call ladder (Jul 20/25) or a small SPY/QQQ put-spread held through 07-02; defensive/starter size (VIX only 18–19, no squeeze, don't overpay for tail). (2) **No naked short premium into the print** — FAIR VRP + short-gamma + binary event is exactly where sell-vol gets run over (explicitly avoid the §8 STZ/TSCO/ABT/NKE ideas as held-through-NFP structures). (3) **Mean-reversion watch:** if front-end backwardation flattens below ~1.0 next week (panic resolving), that favors contrarian longs — monitor, don't pre-position. (4) **Quarter-end caveat:** today's DP prints are Russell-distorted — don't read single-name DP accumulation as conviction until 06-29+ confirms.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**EMPTY. No name reached MEDIUM (≥7) or HIGH (≥9) tier — in fact none cleared the LOW floor (≥3).** This is a valid no-edge output, not a failure.

**Expectancy lens (advisory — C31):** `[advisory — expectancy is not yet a live sizing axis]` — no resolved per-tier expectancy to display today (no sized book; the most recent `/calibration-audit` found the tiers inverted on the first post-UPTREND window, which is why the P0.6 half-cap is active). Per-tier payoff-ratio context is not actionable on a zero-position day.

The five confluence-gate-passing names and their full audit, for journaling (all DROPPED below the raw≥3 floor, dominated by `flow_conflict` deductions):

| Ticker | raw | Components | Class | cum_flow 30d | win_rate (n, source) | excess | Fund. | Final |
|---|---|---|---|---|---|---|---|---|
| UBER | +1 | +1 accum-conjunction (halved, cum_flow fails $50M) · +1 OI-build · −1 flow_conflict_lite | dark_pool_accumulation | −$38.5M | null `NA(substrate)` (empty class) | n/a | CAUTION | no size — DROP |
| MSFT | +1 | +1 cum-flow intent-screened (−$521M bearish-aligned) | bearish_flow | −$521M | 0.5185 (n=135, backtest_clean) | **+0.156** | CAUTION | no size — DROP |
| NVDA | −1 | +2 multileg directional · −3 flow_conflict | bullish_flow / multileg | −$545M | 0.5141 (n=142, backtest_clean) | −0.085 | CONFIRM | no size — DROP |
| SMH | −1 | +2 multileg directional · −3 flow_conflict | bearish_flow / multileg | +$161M | 0.5185 (class ref) | +0.156 | NA (ETF) | no size — DROP |
| IGV | −1 | +2 multileg directional · −3 flow_conflict | bearish_flow / multileg | +$87.5M | 0.5185 (class ref) | +0.156 | NA (ETF) | no size — DROP |

**Backtest substrate (P0.3 clean protocol, --top-n 200 pinned, complete-forward-window WR):** `bearish_flow` 0.5185 (n=135, headline 54.4% discarded, +0.156 excess vs SPY-down = edge); `bullish_flow` 0.5141 (n=142, −0.085 excess = beta → C2 caps half); `dark_pool_accumulation` **null / NA(substrate)** (empty class today). MSFT's +0.156 market-excess is genuine alpha (not beta) — irrelevant today since the name dropped below floor.

**Rubric-asymmetry note (for the auditor):** the rubric's strongest scored lines are all *long-accumulation* lines; there is no symmetric *short-distribution* +3. So MSFT — DP distribution + Tier-1 floor put + a multi-session negative-DEX history, the cleanest qualitative short on the tape — scores only +1. This is a known structural asymmetry, flagged, not improvised around.

### Conviction-scoring rubric (Step 4, FROZEN version 2026-06-12) — embedded for audit
```
Daily conviction score = Σ:
  +1  dealer-positioning MECHANIZED DEX flip / vanna-squeeze in trade direction (verified sign change, not a level)
  +3  3+ aligned accumulation signals (DP+OI+smart-positioning, block-stratified institutional) — CONJUNCTION: full +3 only when cum_flow_30d sign-aligned AND |cum_flow_30d| ≥ $50M; else halved to +1
  +1  multi-day OI build (oi-trend BUILDING, --days ≥5)
  +1  conviction-matrix DIRECTIONAL_LONG conf >70 — CONDITIONAL: only when dominant_signal_class == leap_directional; else 0
  +1  cum-premium-flow net directional accretion (30d) — INTENT-SCREENED (no distribution_flag; not deep-ITM ex-div arb)
  +1  sector-rotation single-name leader — CONDITIONAL: persistence ≥0.6 AND cum_flow aligned AND |cum_flow_30d| ≥ $50M
  +1  earnings-scout BUY VOL / SELL VOL
  +2  multileg directional (term-structure-anchored play type)
  +1  vol-surface KINKED / BACKWARDATION with VRP-aligned bias
  +1  opex-pin-strategist top-5 (OPEX week only)
  -2  contrarian overcrowded long + rising pc-ratio-zscore (informed-flow-continuation penalty)
  -3  flow_conflict (cum_flow 30d clearly opposite dominant class) / -1 flow_conflict_lite (MIXED)
  [TIER GATES, risk 2d, not score_components]: -1 tier corr-cluster ≥0.70; -1 tier regime conflict
Tiers: ≥9 HIGH (full) · 7-8 MEDIUM (half) · 3-6 LOW (starter/watch) · ≤2 drop
P0.6 out-of-regime guard: all conviction sizing capped at HALF (rubric fitted UPTREND, current TRANSITIONAL).
```

## 8. Watch-only — single signal, no confluence
Surfaced by one agent (or sub-floor); **for journaling, NOT trade entry today.**
- **STZ** (sell-vol) — earnings-scout SELL VOL near-full, earnings 6/30, front kink + back-month TAIL_HEDGING. *Do not hold through NFP as naked short-vol.*
- **TSCO** (sell-vol) — vol-surface calendar, VRP +0.172 (richest), earnings 2026-07-23.
- **ABT** (sell-vol) — vol-surface put calendar, VRP +0.0875, TAIL_HEDGING, earnings 2026-07-16.
- **NKE** (sell-vol, half/lean-skip) — earnings-scout, front-only kink + complacent tail (coin-flip), earnings 6/30.
- **IWM** (short) — multileg $56M 290/285 put vertical + 285P 07-17/07-31 calendar; dealer-positioning NEUTRAL (single clean agent).
- **INTC** (short) — sweep-tracker 130P 07-17 +11.4k OI opening build, cleanest single-name bearish opening build, no co-flag.
- **FLEX** (short/continuation) — contrarian BEARISH_EXTREME pc-z 4.82 but flow AGREES (informed-continuation caution, NOT a fade) + BACKWARDATION near catalyst, iv_rank 99. *Continuation-watch, do not buy the dip.*
- **NOW** (long) — sector-rotation Tech leader watch + LEAP near-miss (positive 30/90d accretion) but conviction-matrix 19.8.

---
*No HIGH-tier names → no deep-dive hand-off (Step 8.5 skipped). No raw≥7 names → no batch-scan (Step 6.5 skipped). Watchlist persisted to `conviction_2026-06-26` {UBER, MSFT, NVDA, SMH, IGV} to seed tomorrow's correlation + adverse-flow universe.*
