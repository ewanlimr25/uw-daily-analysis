# Daily Market Analysis — 2026-07-09

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / trend UPTREND. SPY 751.71 (>20SMA 742.34, >50SMA 740.37, +1.69% 30d, −1.14% from 90d high), VIX 15.84 (LOW). Options-flow breadth soft (36.8% bullish tickers, 3,956 bearish vs 2,304 bullish) — up-tape carried by a thin set of names. SPY next-session gamma pinned right ON the flip (751.32 vs ZGL 751.74); QQQ long-gamma in a wide channel. Sector lean: Technology (+$3.2B net) + Comm Svcs (+$822M) lead; Basic Materials the only net-negative sector.
- **Rubric regime status:** **OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half.** (P0.6 guard active — freeze-lift still cannot run: 0/30 post-freeze HIGH/MED resolved.)
- **Next-session GEX (SPY/QQQ):** SPY — NEGATIVE-at-the-flip, ZGL 751.74 (reliable), call wall **752** (razor-tight), put wall **740** (wide); fresh/unstable, prefer defined-risk directional over a pin. QQQ — POSITIVE (ZGL unreliable, fell back to total_gex sign), wide 705–730 channel → condor/wide-wing fly. Advisory, see §2.
- **Top swing build:** **NONE.** Zero names cleared to HIGH or MEDIUM. Only survivor is **NBIS (raw 3, LOW → WATCH-ONLY)** — a negative-excess beta long with insiders selling into it, bear residual 30pts above bull, CPI at T+3. Not sized.
- **Top LEAP candidate:** **NONE.** leap-positioning-radar returned zero of nine gate-passers; GLD the lone near-miss (killed by flat 90d cum-flow).
- **Biggest risk:** **CPI 2026-07-14 (T+3, HIGH)** lands inside every swing horizon before its own catalysts. No correlation cluster on the (empty) book; hedge sleeve not required. Watch **TSM** for exit — carried long-watch flow flipped bearish today.

> **Seventh consecutive near-empty sized book — and correctly so.** Nothing on today's tape beats holding cash into Tuesday's CPI. The one non-drop name is beta that underperforms SPY, with three independent gates cutting it before the out-of-regime half-cap even binds.

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend **UPTREND** (SPY above 20/50 SMA). Trading guidance: half position sizes, defined-risk, iron condors in range. Breadth (options-flow): 36.8% bullish tickers — a weak-participation up-tape.
- **Per-index gamma (current-state EOD 0–45d book; §2 carries the forward read):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 751.32 | 751.74 (reliable) | +$1.243B | NEGATIVE (at-flip) | 752 | 740 |
| QQQ | 723.19 | 300.29 (unreliable) | +$275.6M | POSITIVE | 730 | 705 |
| IWM | ~298 | 140.21 (artifact) | — | choppy/FULLY_NEG toggling | — | — |

- **`uw options-flow dte-volume-share`:** 0DTE 29.2% / weeklies 30.6% / monthlies 27.9% / LEAP 4.8% — **BALANCED** (not retail-dominated; monthlies+ ≈ 33% institutional).
- **`uw historical vrp` (SPY):** **FAIR** (IV30 0.1323 vs realised 0.1535, vrp −0.021) — realized slightly above implied, no clean premium-selling edge; a mild premium-buying tilt at the index.
- **Macro backdrop (`fred_macro`):** yield curve **normal** (+0.38 10Y−2Y), core CPI **2.96%** / core PCE **3.41%** (sticky), unemployment **4.2%**, payrolls **+57k** (soft), 10Y **4.56%** (flat 30d), USD **strengthening**, fed funds **3.62%**. Forward `event_risk`: **CPI (June) 2026-07-14 (HIGH)**, **PPI 07-15 (MED)**, OPEX 07-17, FOMC + SEP 07-29 (outside 10-day window).

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book (OI persists overnight), read forward as the prior for the 2026-07-10 open. Prose-only, 0 rubric points, no backtested predictive claim. Scope: SPY & QQQ only.

**SPY** — spot **751.32**, ZGL **751.74** (`zgl_reliable=true`, 0.06% from spot — as close to the flip as the book gets), regime **NEGATIVE**, total_gex **+$1.243B**. Call wall **752** (+0.68 pts — razor-tight), put wall **740** (−11.3 pts — wide). **Read:** spot sitting essentially ON the zero-gamma line — a coin-flip prior, not a clean regime call. The 10-day series has whipsawed POSITIVE/NEGATIVE/FULLY_NEGATIVE every 1–3 sessions (fresh, unstable flip). Wall asymmetry: tight cap at 752, well-cushioned floor into 740. **Structure bias:** prefer defined-risk directional (call debit capped near 752, or put credit down to ~745) over a pin trade — an iron fly here fights a regime that flipped twice in the prior four sessions. A hold above 752 reads as a short-gamma-above breakout, not a fade. **Caveats:** EOD prior only (fresh 0DTE OI re-computes ZGL/walls in the first 30–60 min); CPI 07-14 is not a same-session 07-10 risk but gap risk builds into it; SPY ETF book, not SPX; cannot isolate the D+1 expiry (0–45d proxy).

**QQQ** — spot **723.19**, ZGL **300.29** (`zgl_reliable=false` — deep-OTM extrapolation artifact, garbage nearly every session this window), regime **POSITIVE**, total_gex **+$275.6M**. Call wall **730** (+6.8 pts), put wall **705** (−18.2 pts). **Read:** falling back to total_gex sign (ZGL unusable), dealers net-long gamma with spot well inside a wide 705–730 channel → mean-revert / pin behavior for the open, not trend acceleration. Regime flipped POSITIVE only 07-08 after two FULLY_NEGATIVE sessions — recently re-established, not deeply held. **Structure bias:** long-gamma, wide channel → condor or wide-wing iron fly; fade pokes beyond 730 rather than chase. Put wall 705 too far to lean on as a same-session floor. **Caveats:** ZGL unusable for QQQ this cycle (do not quote it); same EOD-staleness / gap-risk / ETF-not-NDX / 0–45d-proxy caveats.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — the validated stack)
The GEX walls above are a **map, not a pin** (wall-as-magnet backtested NO_GO). What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, NOT a guaranteed edge (validation sample has no vol shock — short-vol left tail UNSAMPLED). Rolling backtest verdict: **GO_PREMIUM_SELL_INTRADAY** (n=60).

| Index | sell? | vol_state | VIX | implied move | exp. range | size | Structure | PnL (open, gross → **net**) | Win% |
|---|---|---|---|---|---|---|---|---|---|
| SPY | yes | LOW | 15.84 | 0.69% | 0.78% | 0.5× | iron fly / short straddle @ 751.63, wings ±0.78% | +0.296% → **+0.196%** | 95.0% |
| QQQ | yes | LOW | 15.84 | 1.43% | 1.32% | 0.25× | iron fly / short straddle @ 723.62, wings ±1.32% | +0.394% → **+0.294%** | 88.3% |

- **PnL basis:** % of underlying spot notional, **GROSS**; net = minus assumed 0.1% round-trip cost. Lead with net — tiny in absolute terms. Gross win-rate overstates a negatively-skewed short-vol seller's edge (Vilkov 2024).
- **When:** enter at/after the open once the gap resolves; **hold 0DTE to the close, never overnight** (overnight backtested negative). Gap beyond wings → stand aside.
- **QQQ caution:** front-end backwardation (0DTE IV 1.43× VIX) = event/gap risk; quarter-size. **SPY ≈ SPX** (trade either); **QQQ weaker** (NDX book unavailable), lower confidence.
- **Direction:** none — delta-neutral. No directional tilt.

## 2a. Swing Dealer Positioning (1–4 weeks)
**Empty board at the index level.** `dealer-positioning-strategist`: no mechanized DEX flip clears the sign+magnitude bar on SPY, QQQ, or IWM; no valid vanna-squeeze (all three books call-heavy, VIX not in a clean 3-session decline); ZGL/GEX regime whipsawing near-daily with no stable grind.
- **SPY:** DEX +$28.29B (07-09) but a whipsaw week (+$2.0B→+$30.3B→+$3.7B→−$6.6B→+$28.3B); prior-3 run NEG/POS/POS (mixed) → level, not flip. Swing bias **FLAT/NEUTRAL**.
- **QQQ:** DEX +$14.16B; prior-3 NEG/NEG/POS (mixed) → no flip. **FLAT/NEUTRAL.**
- **IWM:** the one to re-check tomorrow — 3-session negative sign-run then a razor-thin +$0.161B flip, but magnitude = 0.15× the trailing-10 median ($1.095B), below the 0.25× floor → **killed as whipsaw artifact.** A second positive session ≥$0.27B on 07-10 would make it a live mechanized flip. Watch-only.
- CPI 07-14 sits inside the 1–4wk window for all three; the pre-CPI whipsaw in both DEX and GEX regime reads as the market pricing uncertainty into the print, not dealers building a directional book.
- **Data-quality flags for `/calibration-audit`:** (1) `gex-time-series regime_flip_dates` under-captures FULLY_NEGATIVE transitions across all three names; IWM's 06-26 flip prints ZGL 140.21 vs ~298 spot (artifact). (2) **The Yahoo ^VIX chart-API path worked cleanly for 2026 dates this run** (07-09 close 15.84 = Step-0 VIX) — contradicts the standing `yahoo_chart_api_2025_anchored` memo; worth re-verifying before that note is trusted further.

## 2b. Sector Rotation
`sector-rotation-strategist`: **`rotation_regime: no_change` (low confidence).** GICS persistence layer is degenerate — all 11 sectors read persistence_score 1.0, all INFLOW (broad tape, non-discriminating). No clean two-sided rotation pattern; nothing clears a genuine GICS-level outflow.
- **Cleared magnitude + ETF cross-confirm (into):** Financials (SOFI/PYPL/MA/BRKB), Consumer Cyclical (TSLA/LULU/CVNA), Communication Services (META/NBIS/RDDT). **But the +1 sector-leader gate FAILS on the 30d cum-flow leg for the sampled leaders** — TSLA −$256.5M, META −$58.3M, SOFI −$4.6M all net-bearish 30d → early-stage reversal, not established accumulation.
- **GICS-vs-ETF divergence — do NOT trade Tech as rotation-in:** Technology posted the day's largest headline print (+$3.21B) but **XLK's own 5-day options flow is bearish** (−$4.75M, call-selling/unwind) — mega-cap-concentrated, the broad basket distributing.
- **Short-side watch (not scored):** Materials/miners complex — GDX (−$7.07M 5d, put-heavy, bid-aggressive) + broad single-name bearish concentration (RIO/AA/DOW/VALE/NUE/ALB/MP/EQX) that the −$9M GICS aggregate badly understates.

**ETF flow tape (advisory)** — top ranked (21 scanned, 6 deep-pulled):

| ETF | Net premium dir (5d) | Persistence | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|
| SMH | inflow (+$39.2M, largest) | MIXED | — | n/a (thematic) | — |
| KRE | inflow (+$23.8M) | BULLISH | put-heavy / hedge-leaning | agree (Financials) | — |
| XLF | inflow (+$20.8M) | BULLISH | call-tilted, ask>bid | agree (Financials) | SOFI, PYPL, MA |
| XLY | inflow (+$1.30M) | BULLISH | — | agree (Cons Cyclical) | TSLA, LULU, CVNA |
| XLC | inflow (+$0.50M) | BULLISH | — | agree (Comm Svcs) | META, NBIS, RDDT |
| **XLK** | **outflow (−$4.75M)** | **BEARISH** | call-heavy but bid-dominant (selling) | **disagree (Technology)** | — |
| GDX | outflow (−$7.07M) | BEARISH | put-heavy, bid-aggressive | agree-ish (Materials) | RIO, AA, DOW, VALE |

## 3. Swing Setups (1–6 weeks)
**Empty — no name cleared to a sized swing tier.** The confluence-cleared candidates (SNDK, NBIS, META) scored raw 3/2/0; none survived the gate stack. See §7 for the full audit trail and §8 for single-agent watch-only names.

- **3a. Long swings (regime-aligned):** none sized. **NBIS** (raw 3, LOW) is watch-only — see §7.
- **3b. Short / fade swings (defined risk only):** none. `contrarian-scanner` returned zero qualifying fades (VRP FAIR kills premium fades; the only ±2σ extremes — SAP/ARE/TAN — are flow-aligned continuation in backwardation, not fades).

**Urgency-ranked sweeps (informational, 0 rubric points):**

| Ticker | Side | 5d premium | Persistence | Note |
|---|---|---|---|---|
| SNDK | Bullish | $2.47B | 5/5 | Cleanest liquid single-direction name; scored raw 2 (drop) — loud tape earns 0 points (deprecated line), no scored co-flag. |
| INTC | Bearish | $874M | 5/5 | Aggressive 1-DTE (07-10 expiry) call-selling, vol>>OI (opening) — urgent but single-agent. §8 watch. |
| NBIS | Bullish | $521M | 4/5 | Second-cleanest; the LOW watch-only name. |
| SOXL | Bearish | $504M | 3/5 | 3× leveraged semis — directional confirm only, path-decay risk. |

> The absolute-premium sweep leaderboard was **100% SPX index overlay/collar legs** (7000/8000 strikes, 2026-09→2027-12) — hedge flow, not single-name direction; stripped by the hedge-flow filter. **Data-quality note:** MU (`most-active` puts at $1,880–$2,390 strikes, DTE ~800, OI 9–243 vs volume 559–691) shows an implausible strike/spot ratio — likely the stale-contract / twin-print artifact class flagged 2026-07-07; desk should sanity-check MU's raw feed before trusting any MU aggregate.

## 4. LEAP Builds (6–24 months)
**Empty.** `leap-positioning-radar`: zero of nine gate-passers. All five Step-0 heavy names DROP — META (2/9, established base not fresh build), AMD (MIXED 6% conf), TSLA (long-dated flow is a downside put hedge, not bullish), OKLO + FXI (hard-reject: conviction-matrix DISTRIBUTION). **GLD** the lone documented near-miss: genuine fresh long-dated ask-side call build (GLD Dec-28 445C +2,399 OI, aggressive ask), but killed by Gate 4 — 90d cum-flow flat/MIXED (−$36.7M net on $16.2B gross) and NEUTRAL/sell-tilted institutional-accumulation. Re-test in 2–3 weeks if the 30d bullish tilt (+$185M) starts pulling 90d positive.

## 5. Volatility Surface
`vol-surface-scout` — substrate caveats stated up front: `iv-percentile-zscore` capped at n=61 repo-wide (percentiles PROVISIONAL); `front-end-iv-ratio` 0DTE-contaminated (rebuilt from the term-structure table for every name).

**KINKED, catalyst-aligned (event-driven — hand to earnings-scout):**
- **META** — kink 2026-07-31, earnings 07-29, IV-rank 100, z=3.58, VRP FAIR (+0.020, purely event-priced, no independent sell edge), implied move ~14%.
- **FTAI** — kink 2026-07-31, earnings 07-29 PM, VRP strongly PREMIUM_SELLING (+0.271, best-aligned — rich AND event), implied move ~18%.
- **BAND** — soft kink at the 08-21 monthly (only expiry spanning earnings), VRP FAIR.

**Cleanest structural SELL VOL (no acute term dislocation):** **STX** — VRP PREMIUM_SELLING (+0.240), rich vs realized, flat curve, earnings 08-04 (26d, not the driver). Weaker: SNDK (marginal backwardation 1.054, VRP FAIR — confirm next session).

**Calendar candidates:** none qualify cleanly — AMAT (negative VRP −0.038 + ratio 1.309 >1.10 = don't fade, don't sell) and XENE (real backwardation, no identified catalyst — likely FDA/data readout; hand to fundamentals-gate before sizing) both disqualified.

**Flags:** **TLRY** — Step-0 tagged it a cheap-vol BUY seed; robust percentile (NORMAL 67.2, not low) + strong PREMIUM_SELLING VRP (+0.425) argue the **opposite** (sell the pre-earnings runup, don't buy). **MVO disqualified** — data-integrity failure (iv30d mismatch 0.06 vs 6.05 across tools).

**Earnings-scout term-structure book (next 14d):** JPM **SELL VOL** (KINKED self-confirmed, kink 07-17, TAIL_HEDGING back-skew — full size on its own merits, but prints **07-14 same day as CPI**); TXN **SELL VOL** (half); GS/WFC/NOW **CALENDAR** (front richly bid, tail not confirmed); NFLX/ASML/TSM/INTC/GOOGL **SKIP** (flat back-month). All single-agent → §8, not scored.

## 6. Risk & Correlation
- **Macro headline:** sticky core inflation (core PCE 3.41%), soft labor (+57k payrolls, 4.2% U-rate), normal curve. **Forward event_risk: CPI 2026-07-14 (T+3, HIGH), PPI 07-15 (T+4), OPEX 07-17, FOMC+SEP 07-29.** CPI fires the −1 event-risk tier on any undefined-risk swing inside the horizon.
- **Correlation:** `uw risk portfolio-correlation` on the candidate union (NBIS/SNDK/META) — max pair NBIS/SNDK **0.51** (< 0.60). **No clusters, no soft-watch pairs.** (Tool returned sector=Unknown for all three — metadata gap, not a real concentration read.)
- **VRP / panic:** VRP FAIR (sign-neutral, no vol-structure tilt); SPY front-end IV ratio **1.003 = FLAT**, panic override does not fire.
- **Fundamentals verdicts (top-3):** NBIS **CAUTION** (insider MSPR −78 selling into the rally; earnings 07-29); SNDK **CAUTION** (insider MSPR −100, reads routine/10b5-1; earnings 08-12); META **CONFIRM** (vol/event, clean fundamentals, bearish 30d/90d flow reads as pre-earnings hedging). **No VETOs.**
- **Debate cuts:** NBIS bull 0.55 / bear **0.85** (bear ≥ bull → −1 tier, did not clear); SNDK bull 0.55 / bear **0.85** (−1 tier).
- **Adverse-flow exit list (carried `conviction_2026-07-08`: SNDK/TSM/SPY/PLTR/AMZN):** **TSM — EXIT CANDIDATE** (flow flipped bearish −$15.6M, P/C 1.32, IVR 94.5, $61.2M DP print against the carried long-watch). **PLTR — soft exit** (bearish flow, off-thesis decay). **SNDK — hold-watch with vol warning** (still bullish +$92.3M but HIGH_IV_RANK 100 — long-premium pays top-of-range vol). SPY/AMZN no adverse signal. fz fundamentals-drift tripwire CLEAN.
- **Breadth cross-check (fz, advisory):** 301 advancers / 202 decliners, **pct_green 59.84%**, avg +0.63% (top LITE +11.1%, worst APA −5.1%). **No divergence** (green tape + pct_green > 50) — unlike yesterday's 22%-green distribution tell, today's breadth confirms the up-tape. Advisory, 0 points.
- **Hedge sleeve:** **none required** — the sized book is empty (net delta ≈ 0). Per the 07-04 audit, the empty-book refusal to size is the system's best-graded behavior; no hedge is manufactured for a book with no exposure.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**No HIGH or MEDIUM names today.** Below is the full audit trail for the three confluence-cleared candidates (all LOW/drop), sourced from the `signal-confluence-quant` output.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no sized book → no per-tier expectancy to display this run. The live sizer remains the win-rate ladder; C3 fractional-Kelly stays advisory.

| Ticker | Raw | Tier | Dominant class | win_rate (n, source) | market_excess | Pre-risk | Fund. | Debate (bull/bear) | Gates fired | Final |
|---|---|---|---|---|---|---|---|---|---|---|
| **NBIS** | 3 | LOW | bullish_flow | 0.457 (140, clean) | **−0.107 (beta)** | starter | CAUTION −1 | 0.55 / **0.85** | fund −1, debate −1, event −1, half-cap | **WATCH-ONLY** |
| SNDK | 2 | drop | bullish_flow | 0.457 (140, clean) | −0.107 | skip | CAUTION −1 | 0.55 / 0.85 | (moot on drop) | DROP |
| META | 0 | drop | earnings_vol | NA | — | skip | CONFIRM 0 | — | (moot on drop) | DROP |

- **NBIS** — score_components: +1 sector Comm Svcs leader (persistence 1.0, +$67.2M 30d aligned ≥$50M — all three gates verified live), +1 multi-day OI build (BUILDING +587k/10d), +1 cum-flow accretion (+$67.2M, intent-screened clean). **Honest texture:** the +$67.2M is 0.8% of $8.2B gross (exactly the union median) and the class it rides (`bullish_flow`) is **negative-edge beta** — clean WR 0.457 vs SPY-long 0.564 over the identical 140 windows (−10.7pp, C2 starter-cap binding on its own). Three independent gates cut a name already flagged beta. **Invalidation (informational):** sector persistence < 0.6 for ≥2 sessions, or sweep persistence flips. Only 1 of 4 load-bearing tools cited — would not clear the Step-3a HIGH gate regardless.
- **SNDK** — drops at raw 2 despite the **loudest tape on the board** ($2.47B, 5/5 sweep persistence earns 0 points; deprecated line, no co-flag to carry it). +1 OI build, +1 cum-flow (+$831.5M 30d, 12.4× median). Class-backtest warning is the real caution: SNDK appears 12× in the kept `bullish_flow` rows with 5d forward moves +28% to −25% — no selection edge; a persistent-flow long here is an unpaid-for vol bet. IVR 100 → any re-emergence must be defined-risk, never long-premium.
- **META** — raw 0. Every candidate line fails its gate: KINKED is pure event-pricing into 07-29 at VRP FAIR (no aligned bias); sector +1 fails on 30d cum-flow −$58.3M / 90d −$501M (bearish base, opposing the bullish framing); conviction-matrix confidence 16.1% < 70. Not a conviction call; any event-vol expression is an earnings-scout conversation, not a scored line.

### Conviction-scoring rubric (Step 4, verbatim — frozen `2026-06-12`)
```
Daily conviction score = Σ:
  +1  dealer-positioning MECHANIZED DEX flip / vanna-squeeze in trade direction (verified SIGN CHANGE, not level)
  +3  3+ aligned accumulation signals (DP + OI + smart-positioning, block-stratified institutional-tier) — CONJUNCTION: full +3 only when cum_flow_30d confirms (aligned AND |cum_flow_30d| ≥ $50M); else halved +3→+1
  +1  multi-day OI build (oi-trend BUILDING, --days ≥ 5)
  +1  conviction-matrix DIRECTIONAL_LONG confidence > 70 — CONDITIONAL: leap_directional class only
  +1  cumulative-premium-flow net directional accretion in trade direction (30d) — INTENT-SCREENED (no distribution_flag; no deep-ITM ex-div arb)
  +1  sector-rotation single-name leader — CONDITIONAL: persistence ≥ 0.6 AND cum_flow_30d aligned AND |cum_flow_30d| ≥ $50M
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored)
  +1  vol-surface-scout KINKED / BACKWARDATION with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner overcrowded long + rising pc-ratio-zscore (informed-flow CONTINUATION penalty)
  -3  flow_conflict (30d cum-flow clearly opposite dominant_signal_class)
  -1  flow_conflict_lite (30d cum-flow MIXED / bottom-quartile aligned) — mutually exclusive with flow_conflict
  [TIER GATES, 2d — 0 points, applied by risk-monitor]:
  -1 tier  correlation cluster (pairwise corr ≥ 0.70)
  -1 tier  regime conflict with trade direction
```
Tiers: **≥9 HIGH** (full) · **7–8 MEDIUM** (half) · **3–6 LOW** (starter/watch) · **≤2 drop**. Sizing ladder (clean-protocol win_rate): ≥0.70 full · 0.50–0.70 half · <0.50 starter/skip · null starter · NA(substrate) tier-default capped half. **OUT-OF-REGIME guard active → all sizing capped at half.**

## 8. Watch-only — single signal, no confluence
Surfaced by one agent, failed the 2-agent confluence gate. Journaling only, **not for trade entry today.**
- **INTC** (bearish) — sweep-tracker 5/5 bearish, $874M, aggressive 1-DTE (07-10) call-selling, vol>>OI. Single-agent; earnings-scout SKIP'd it (elevated IV persists past print, wrong side of a short-vol). Urgent but unconfirmed.
- **OKLO** (conflict) — multileg-strategist read a bullish LEAP diagonal call ladder (Dec-26 90C + Jan-28 200C, $67.7M debit), BUT leap-radar (conviction-matrix **DISTRIBUTION**) and accumulation-hunter (block-tier buy_ratio **0.0** = 100% sell) both flag distribution. Directional-structure vs distribution conflict — do not act.
- **TLT** (bullish rates) — multileg-strategist 1×1.5 ratio bull-call spread (Jan-28 95C/110C); leap-radar reads it as a rates-hedging book (MIXED). Single positive agent.
- **JPM / TXN** (SELL VOL) — earnings-scout only; JPM full-merit but prints 07-14 = CPI day. §5 vol items, not scored.
- **FTAI / STX** (SELL VOL) — vol-surface-scout only. §5.
- **SAP / ARE / TAN** (bearish extremes) — contrarian-scanner flagged real ±2σ pc-z but all three are flow-aligned continuation in backwardation, not fades. Not entered.

---
*Structural note for `/calibration-audit`: systemic closing-cross contamination across ~20 mega-caps (NVDA/MSFT/AAPL/GOOGL/AVGO/MU/META/AMD/JPM/… clustered at 20:00:00–20:00:46Z at identical prices) wiped the accumulation-hunter board — broader than the 2026-07-02 precedent. Likely batch/delayed-ATS reporting rather than true closing-auction flow; effect on signal is the same (exclude). Worth an audit note.*
