# Daily Market Analysis — 2026-08-28

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL (trend UPTREND) — SPY 769.35 pinned on its 20SMA (769.22), VIX 14.43 (−4.63% 5d), breadth weak (30.5% of optionable names bullish-flow; fz 45.53% of S&P green). **Both index gamma books are freshly SHORT-GAMMA** (SPY `total_gex` −$139.8M, QQQ −$90.1M, ZGL null on both) — the dealer complex amplifies rather than dampens. Tape is a **semis-led flush** (SMH −3.47%, SOXX −3.20%, MRVL −10.28%) with rotation into Comm-Svcs (+1.42%) / Discretionary (+1.15%) / Financials (+0.38%).
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** SPY short-gamma · ZGL null (unreliable) · call wall 772 (+0.35%) / put wall 765 (−0.56%) — tight cage but amplifying sign. QQQ short-gamma · ZGL null · call wall 730 (+1.91%) / put wall **716 (−0.04%, spot sitting on it)** — coiled and fragile. Advisory, see §2.
- **Top swing build:** **NONE.** The conviction book is empty. Two names cleared the confluence gate; both scored `raw_score 1` against a drop floor of 3.
- **Top LEAP candidate:** **NONE.** Zero of four candidates cleared 6-of-9 gates; all hard-failed the 90d cum-flow accretion gate.
- **Biggest risk:** No book, therefore no correlation cluster and nothing to hedge. The live risk is the **carried IWM long from `conviction_2026-08-21`**, now facing a 2.54 put/call ratio, −$7.3M net flow and a put-side OI build — tagged **exit candidate**.

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — "Half position sizes. Favor defined-risk strategies. Iron condors in range."** Trend **UPTREND**. SPY 769.35, above both the 20SMA (769.22, by 0.02%) and 50SMA (753.96); +3.73% over 30d; −1.29% from the 90d high.

Breadth is the tell the index print hides. Only **1,920 of 6,286** optionable names carry bullish flow (**30.5%**), and the independent `fz` lineage agrees — **229 advancers vs 273 decliners** (45.53% green), average constituent −0.34%. Two different data lineages, same conclusion: the tape is weaker than SPY's −0.23% suggests. Unlike yesterday there is **no green-index/red-breadth divergence** to flag — index and breadth are both mildly negative, so they agree.

| Index | Spot | Zero-gamma | Total GEX | Regime (label) | Label vs sign | Call wall | Put wall |
|---|---|---|---|---|---|---|---|
| SPY | 769.30 | `null` | −$139.77M | FULLY_NEGATIVE | **agree** | 772 | 765 |
| QQQ | 716.31 | `null` | −$90.14M | FULLY_NEGATIVE | **agree** | 730 | 716 |
| IWM | — | — | — | negative 9-of-10 sessions | — | — | — |

Worth noting: the documented GEX defect — the `regime` label contradicting its own `total_gex` sign — ran on 4 of 4 sessions this week but **did not fire today**. Label and sign agree on both indices, which makes today's read more trustworthy than the week's.

**DTE mix (`uw options-flow dte-volume-share`):** 0DTE **47.9%**, weeklies 21.3%, monthlies 15.7%, LEAPs **3.1%** → `RETAIL_DRIVEN`. Institutional positioning is not what moved this tape, and every swing/LEAP thesis today gets a uniform conviction downgrade as a result.

**VRP (`uw historical vrp`):** SPY IV30 11.63% vs realised 11.90% ⇒ **−0.0027 FAIR**. QQQ IV30 16.87% vs realised 21.05% ⇒ **−0.0418 FAIR**. IV sits at or **below** realised, most sharply on QQQ. This is a **premium-buying** tilt, and it is the reason no naked premium-selling fade appears anywhere in this report.

**Macro backdrop (`scripts/fred_macro.py`):** curve normal and bull-steepening (10y2y +0.39; 2Y −0.06 while 10Y +0.06 over 30d), core CPI 2.79% YoY, **core PCE 3.34% YoY** (sticky, above target), unemployment 4.1%, **payrolls −23k MoM (contraction)**, 10Y **4.67 and rising**, USD **weakening** (−2.51 over 30d), fed funds 3.63%. Sticky core inflation plus a negative payroll print plus a rising long end is a **stagflationary tilt** — the worst backdrop for undefined-risk directional swing exposure, and independently the best argument for today's empty book.

**Forward event risk** (T+n counted on the trading calendar from 2026-08-28; Labor Day Mon 09-07 closed):

| Event | Date | Trading days out | Impact |
|---|---|---|---|
| JOLTS (July) | 2026-09-02 | T+3 | medium |
| **Nonfarm Payrolls (Aug)** | 2026-09-04 | **T+5** | high |
| **PPI (Aug)** | 2026-09-10 | **T+8** | high |
| **CPI (Aug)** | 2026-09-11 | **T+9** | high |
| **FOMC + SEP** | 2026-09-16 | **T+12** | high |

Any 1–4 week swing opened today holds through four named, dated Tier-1 prints.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — open interest that persists overnight — read forward as the *prior* for Monday's open. **Prose-only, 0 rubric points, no backtested predictive claim.** Predictive validation lives in `/weekly-analysis`'s rolling §2 backtest, not here. Scope is SPY and QQQ only.

**SPY** — spot 769.30 · ZGL **null, `zgl_reliable: false`** · `total_gex` **−$139.77M** (short gamma) · call wall **772** (+0.35%) · put wall **765** (−0.56%).
Regime freshness: **fresh and unstable** — 5 flips in 30 sessions (08-05, 08-07, 08-10, 08-13, 08-27), and 08-27's +$690M flipped to −$139.8M in a single session. Spot sits inside a tight ~1.3%-wide cage, but the *sign* argues breakout/trend rather than mean-reversion if either wall gives.
**Structure bias:** short-gamma ⇒ debit verticals / directional 0DTE, or a long straddle on a breach of 765 or 772. **Not** a premium-selling setup. If premium is sold anyway, keep wings inside 765/772 and size down.

**QQQ** — spot 716.31 · ZGL **null, `zgl_reliable: false`** · `total_gex` **−$90.14M** (short gamma) · call wall **730** (+1.91%) · put wall **716 (−0.04% — spot is sitting on it)**.
Regime freshness: **fresher and more unstable than SPY** — 8 flips in 30 sessions; 08-27 printed +$1.15B and today −$90.1M, a violent one-day swing.
Spot resting directly on the largest-magnitude negative-GEX strike is the least stable place a short-gamma book can open. A push below 716 has **no meaningful dealer support until 700** (−$77.5M shelf, −2.3% away), while 730 is the nearest upside magnet.
**Structure bias:** debit verticals or a long straddle, skewed to respect the downside air pocket to 700. Avoid short premium centred at spot.

**Mandatory caveats:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and re-computes ZGL and walls.
- **ZGL is `null` on both indices** — extrapolation failed. The read rests on the `total_gex` sign plus spot-vs-wall position only. There is no anchor level to trade directly.
- **Gap risk.** No Tier-1 print before Monday's open (NFP is T+5), but Friday's semis flush is a fresh, overnight-holdable shock.
- **Tooling limit.** `gex --dte-max 1` errors; this is the standing **0–45 DTE** book, the best available proxy for the next-session prior, not the isolated D+1 expiry.
- **ETF book**, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` / VIX | **LOW** / 14.43 | **LOW** / 14.43 |
| implied move | 0.39% | 0.59% |
| `expected_range_pct` | 1.10% | 1.91% |
| `size_scalar` | 0.5 | 0.5 |
| suggested structure | wider iron condor, wings ≈ ±1.1% | wider iron condor, wings ≈ ±1.91% |
| `stand_aside_reason` | none | none |
| backtest win (open entry) | 86.7% (n=60) | 85.0% (n=60) |
| mean PnL open, **gross** | +0.222% | +0.345% |
| mean PnL open, **net** | **+0.122%** | **+0.245%** |
| worst day | −1.40% | −2.453% |

`pnl_basis`: **percent-of-underlying-spot-notional, GROSS** of transaction costs — not premium-collected, not margin-relative. A "+0.2%/day" figure is tiny in absolute terms.

**⚠️ Do not read the `GO_PREMIUM_SELL_INTRADAY` verdict as a green light today.** The verdict and the `sell_premium: true` flag are **unconditional** — they do not consult the live vol state. At VIX 14.43 the vol state is **LOW**, and the conditional expectancy is `mean_pnl_by_vix_state[LOW]` minus the 0.1% round-trip cost:
- SPY: 0.15 − 0.10 = **+0.05%** — effectively zero.
- QQQ: 0.22 − 0.10 = **+0.12%** — thin.

The edge lives in the **MID/HIGH** terciles (bounds 15.8 / 17.3), not here. Compounding this, **both index gamma books are short gamma**, so the dealer complex amplifies moves — the wrong backdrop for short premium into an NFP at T+5. Treat this lane as **thin-to-nil today**, not actionable.

Advisory, delta-neutral, **0 rubric points**, and explicitly not a guaranteed edge: the validation sample contains **no vol shock**, so the short-vol left tail is **unsampled**. **SPY ≈ SPX** (validated identical); **QQQ is weaker** (Nasdaq index book unavailable) — lower confidence. Promotion bar: this lane stays advisory permanently until both a vol-shock day enters the sample **and** net expectancy clears a tail-aware bar. Win-rate is explicitly not the promotion metric for a negatively-skewed short-vol strategy.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

**One mechanically-qualifying DEX sign flip in the entire fleet: MRVL.**

| Symbol | net_dex latest | DEX flip qualifies? | Vanna squeeze | GEX regime | Swing bias |
|---|---|---|---|---|---|
| **MRVL** | −$497.5M | **YES** — `magnitude_ratio 1.01`, `whipsaw_warning FALSE` | no (net_vanna +1,147, negligible) | flipped NEG same session, broad | **SHORT** (hypothesis) |
| **IWM** | −$6.76B | no — flip predates today; neighbour already same-sign | **YES** — put-heavy book + 5-session falling VIX | negative 9-of-10 | **LONG** (hypothesis) |
| **AMAT** | — | no — 3 sign changes, whipsaw | no | **NEGATIVE 8 straight sessions since 08-18** (well-confirmed) | NEUTRAL-to-SHORT |
| LRCX | −$66.8M | no — **fails magnitude floor** (66.8M < 66.9M) | no | fresh single-day, unconfirmed | NEUTRAL |
| SPY / QQQ | +$24.4B / +$17.7B | no — 0 adjacent sign changes | no (call-heavy ⇒ *selling* pressure) | see §2 | NEUTRAL |
| META | — | no — 4 sign changes, whipsaw | no | **confirmed flip NEG→POS 08-24, held 5 sessions** | NEUTRAL |
| MSFT/GOOGL/AAPL/PLTR/AMZN/NOW | all strongly positive | **no — zero sign changes anywhere** | no | positive all 10 sessions | NEUTRAL |

The distinction that matters: **a level is not a flip and earns nothing.** MSFT (+$15.6B), AAPL (+$9.5B), PLTR (+$4.7B) and GOOGL (+$2.1B) all carry large positive DEX with **zero** sign changes in the window — stable books riding a rally, not pre-move setups. All six mega-caps are call-heavy on vanna, which with a falling VIX is a quiet mechanical **headwind** to further upside, not a tailwind. That is worth flagging explicitly for anyone chasing today's AMZN +3.97% or NOW +4.54% pop on a multi-week view.

**IWM carries the cleanest vanna setup in the scan** — put-heavy book confirmed two independent ways (negative DEX level for 5 straight sessions *and* positive net_vanna +101,358), a live falling-VIX leg (dated Yahoo closes: 08-24 15.85 → 08-25 15.45 → 08-26 15.21 → 08-27 14.51 → 08-28 14.43), and a persistently negative-gamma amplifying regime. Front-end ratio 0.912 is calm, so the squeeze is **still building, not maturing**. It also disagrees with the tape (IWM −1.35% today, worst of the majors) — which is the point of the read, but keeps it hypothesis-grade. **It earns no rubric points: the flip is not mechanically qualifying.**

**AMAT's GEX regime flip is better-confirmed than MRVL's** (8 sessions vs 1), but its own `front_end_iv_ratio@7` of **1.285** — the most panicked in the scan — is already past the 1.10 invalidation bar, so any long-squeeze read there is self-invalidated. Also noted for the vol desk: **AVGO's front-end ratio is 1.506** against only −0.74% price action, a genuine dislocation that looks event-driven.

---

## 2b. Sector Rotation

**Rotation regime call: `no_change`, confidence LOW.** No canonical pattern fits. Technology is netted OUT while Communication Services is the top inflow (kills growth→value); Financials are OUT (kills value→growth); Industrials OUT while Consumer Cyclical IN is internally contradictory for either cyclical pattern.

What is actually happening is an **intra-Technology bifurcation** — a semis flush alongside a software/mega-cap bid — plus a thin, well-confirmed bid into Comm-Svcs and Discretionary. That is not a GICS-level macro rotation.

| Sector | Netted (directional) | Gross turnover | Persistence | Tape 1d | Verdict |
|---|---|---|---|---|---|
| Technology | **OUT −$387.4M** | +$3,750.7M | 1.0 | XLK −1.55%, SMH **−3.47%** | **watch_only** — netted-vs-gross conflict |
| Financial Services | OUT −$49.9M | +$251.8M | 1.0 | XLF +0.38% | watch_only |
| Industrials | OUT −$31.4M | +$228.7M | 0.8 | XLI −0.93% | watch_only (but see below) |
| Communication Services | **IN +$42.9M** | +$351.6M | 0.8 | **XLC +1.42%** | rotating_in, med-high |
| Consumer Cyclical | IN +$1.1M | +$437.4M | 0.8 | **XLY +1.15%** | rotating_in, medium |
| Real Estate | IN +$4.1M | +$4.65M | 1.0 | XLRE −0.40% | watch_only — fails magnitude bar; own ETF contradicts |
| Healthcare / Utilities / Materials / Energy / Cons. Defensive | no netted signal (top-3/bottom-3 truncation) | positive | 0.8–1.0 | mixed | no_signal |

**The methodological point of the day.** `sector-flow` and `sector-flow-persistence` are **one gross-turnover source**, sign-agnostic, and today they fired `INFLOW / persistence 1.0` on **7 of 11 sectors** — the documented zero-discrimination pattern. Because gross cannot be negative today, *every* netted-OUT sector mechanically "disagrees" with its own gross line and routes to `watch_only`. **Technology is the sharpest case: netted −$387.4M vs gross +$3,750.7M.** The tape (SMH −3.47%, SOXX −3.20%, XLK −1.55%) sides decisively with the **netted** read. No persistence-based deduction was taken off the gross source anywhere in this report.

Note also that the persistence *score* is non-discriminating in the opposite direction: 7 sectors tie at 1.0, so the two genuinely rotating sectors (0.8, i.e. 4-of-5 same-sign days) sit in the *bottom* tier by that score despite clearing the ≥3-day substantive bar.

**Single-name leaders — every one FAILS the conditional +1 gate:**

| Sector | Leader | Today's flow | cum_flow_30d | Aligned? | ≥$50M? | Gate |
|---|---|---|---|---|---|---|
| Comm Svcs | META | +$21.3M | **−$36.8M** | no | no | FAIL |
| Comm Svcs | GOOGL | +$8.7M | **−$96.7M** | no | yes | FAIL |
| Comm Svcs | ASTS | +$12.3M | +$34.6M | yes | no | FAIL |
| Comm Svcs | CHTR | — | +$14.3M | yes | no | FAIL |
| Cons Cyc | AMZN | +$59.8M | **−$106.0M** | no | yes | FAIL |
| Cons Cyc | NKE | +$6.2M | +$9.8M | yes | no | FAIL |

The mega-caps' 30-day options positioning has been net **bearish/mixed** even as today's single-day print and price action are bullish. Read today's pop as a **rotation/short-covering day, not confirmed accumulation**.

**ETF flow tape (advisory, 0 points)** — 21 ETFs ranked by 5d options net flow, top-3 each side deep-pulled:

| ETF | Net premium dir | 5d net flow | GICS agreement | Deep-pull read |
|---|---|---|---|---|
| XLK | inflow | +$7.43M | **disagree** (netted OUT) | DP routine; sweep book is one 2027 $185 **PUT**, $5.19M — long-dated hedge, not accumulation |
| IGV | inflow | +$5.64M | disagree | $131M block at −5.05 vs mid (basket cross, not directional); sweeps skew **Nov puts** — contradicts its own bullish label |
| XLV | inflow | +$1.45M | n/a | sweeps skew call/ask-side, mild bullish tilt |
| XLC | inflow | +$0.74M | **agree** | — |
| XLY | inflow | +$0.18M | **agree** | — |
| XLRE | outflow | −$0.03M | **disagree** (netted IN) | — |
| XLI | outflow | −$2.93M | **agree** | — |
| SMH | mixed | −$3.96M | **agree** | the one Tech-family ETF siding with netted OUT |
| XBI | outflow | −$7.90M | n/a | near-term sweeps skew puts |
| XOP | outflow | −$12.43M | n/a | DP prints all **below** mid — selling into bids |
| GDX | outflow | −$16.51M | n/a | mixed; no conviction either way |

The Technology ETF family is **split** — XLK and IGV disagree with the netted OUT call while SMH agrees — which is itself the confirmation that this is a **semis-specific flush, not a broad Tech outflow**. XLK's own headline "inflow" dissolves on inspection into a long-dated put hedge. EWY (−$7.66M, Korea, heavy semis weight) corroborates the same story from a geographic angle.

**Swing-book implication:** a thin long lean toward Comm-Svcs/Discretionary mega-caps is undercut by all six named leaders failing the cum-flow gate; treat today's pop as short-covering. Nothing here is sized.

---

## 3. Swing Setups (1–6 weeks)

**Empty. No swing position is recommended today.**

Two names cleared the two-agent confluence gate. Both scored `raw_score 1` against a drop floor of 3, and both failed for instructive and opposite reasons.

### 3a. Long swings (regime-aligned)

**None sized.**

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| MRNA | **1** (DROP) | Institutional DP accumulation — 3 aligned signals, mega-tier buy_ratio 0.67 ($307.0M), block tier 0.649 ($592.2M); **prices ranged genuinely $135.80–$142.77, surviving the closing-cross screen on a day AMZN/META/TSLA/AVGO/PLTR/GOOGL all failed it** | — | **Loses the $137.50 second-tier DP shelf** (C34-anchored, $108.8M / 21 trades — *not* the $137.99 closing-adjacent bucket) | **skip** |

MRNA is the only genuinely clean dark-pool tape on the board, and it still isn't enough. The +3 accumulation conjunction **halved to +1** on its own flow test: `cum_flow_30d` is **+$2.84M on $2,597.8M gross = +0.109%**, failing the $50M absolute bar by 18× and the 5% scale-relative bar by 46×. Worse, the footprint **decays as the window widens** — 10d +1.5% of gross → 30d +0.109% → 90d +1.108%. A real accumulation program does the opposite.

The `oi-trend` BUILDING label was **withheld, not awarded**: the build is **put-led** (Sep-04 125P +9,526 and 120P +9,432, ~19,000 contracts of fresh protection, against ~10.5K calls scattered). The documented defect is that BUILDING fires on essentially everything; awarding it on a put-led build in support of a long would have been backwards.

Both of MRNA's positive components trace to the **same one-day event** — a dilutive **private debt offering announced 08-28**. That offering plausibly generates the convertible-arb/dealer-hedging blocks that look like accumulation in a buy-ratio screen, *and* it plausibly inflates `rv20` to 375.2, which would make the −301.7pp IV-vs-RV gap behind the vol +1 an artifact. One load-bearing signal wearing two scorecard lines. The bull conceded it could not separate conviction from debt-offering plumbing.

> ⚠ Also unresolved: the vol surface shows a real **14DTE kink (2026-09-11, 37.1% prominence)** and **neither the fleet nor the fundamentals gate could find any dated catalyst to explain it** — no PDUFA, no confirmed Phase 3 readout, no ACIP vote. Either there is an unidentified pipeline binary the DP flow is front-running, or the kink is an artifact. It is flagged as an open question, not traded.

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only` (2026-08-01 P0 #1) — routing, not suppression.** The section runs, theses are fully argued, and every short is scored and serialized so the counterfactual keeps resolving.

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| MRVL | **1** (DROP) | **Mechanized DEX sign flip** — net_dex 08-27 +$1.919B → 08-28 −$497.5M after 13 straight positive sessions; `magnitude_ratio 1.01`, `whipsaw_warning FALSE`; corroborated by a same-session **broad** GEX flip (top strike only ~30% of −$21.7M across 50 strikes) ⇒ dealers now short gamma below spot; `front_end_iv_ratio@7` 1.126, past the panic bar | — | DEX flips back positive ≥3 sessions, or front-end ratio cools under 1.05 | **watch_only** (VETO + short-routing) |

**MRVL is a textbook short trap and the fundamentals gate correctly VETO'd it.** Today's −10.28% followed a Q2 **beat AND raise** — record revenue $2.74B (+37% YoY), Data Center +46% YoY at 79% of mix, Q3 guided $3.15B ±5%, FY27 raised to ~$11.5B and FY28 to ~$16.5B. Revenue +34.07% YoY, margins 51.5/36.6/29.0%. **Four analysts raised price targets on the day of the drop** (Craig-Hallum $217→$300, Rosenblatt $300, Needham $300, B. Riley $315; TD Cowen's $245 trim still 13% above spot). Flow actively **faded** the move: `cum_flow_30d` +$52.6M bullish and **+$7.6M bullish net premium on a −10.28% day**.

The short **lost its own debate**: the bear conceded the DEX flip is most likely a **mechanical post-earnings unwind** — 13 positive DEX sessions into a binary print, flip on earnings day, clearing its floor by **1%** on the single most IV-crushing session of the quarter — carrying no information content. What survives is a **beta/mechanical** short (short-gamma complex, Technology the largest netted outflow, semis de-rating), not a fundamental or flow-confirmed distribution thesis.

### Sweep ledger (informational — 0 rubric points)

Ranked persistence-first; the sweep-persistence rubric line was removed 2026-05-23 (marginal contribution −22pp over two audits).

| Ticker | Persistence | Side | 5d premium | Read | vs today's tape |
|---|---|---|---|---|---|
| **MSFT** | **3/5** | call, bought (ask-side, Nov-20 420/480) | $802.1M | Mega-cap filter **passes** — `cum_flow_30d` +$809.7M BULLISH, genuinely aligned. Best-quality sweep on the board | **agrees** (+1.68%) |
| SNDK | 5/5 | call, **sold** (bid-side, deep-ITM 900 vs $1,493) | $1.36B | Call-writing/unwind, not a fresh short. **Multileg resolved it as a position roll** (matched 1,700 size, same second) | — |
| MSTR | 5/5 | ambiguous (mid/no_side, deep-ITM 0DTE) | $907.0M | Side unclear — stock-substitute/hedge noise | n/a |
| GLD | 4/5 | put-leaning | $1.37B | 4th straight bearish session; macro/rates-driven | independent |
| PLTR | 4/5 | put-leaning | $424.4M | **Conflicts** with the bullish funnel seed — unresolved | n/a |
| INTC | 4/5 | mixed | $422.6M | Mixed direction — disqualified regardless of count | watch |
| AVGO | 3/5 | call-leaning | $299.6M | Mega-cap filter **fails** — `cum_flow_30d` MIXED (+$36.4M, flat) | n/a |

NVDA, AAPL, AMZN, META and TSLA all print 5/5 persistence but with **mixed** direction *and* mixed 30d cum-flow — genuine two-sided hedge flow, no directional read. NVDA specifically shows both aggressive put buying (Sep-04 190P, +59.1k) and call buying (Sep-09 240C, +31.1k) on the same tape.

Below-threshold and instructive: **SOXL** carried a stale 1/5 *bullish* tag while closing **−9.52%** with −$31.5M bearish premium, and **FXI**'s stale 1/5 bullish tag was contradicted intraday by fresh far-dated put buying (Mar-27 35P +46.5k). Textbook illustrations of why single-day sweep tags are not trusted directionally.

---

## 4. LEAP Builds (6–24 months)

**Empty. Zero candidates cleared 6-of-9 gates.** Expected: LEAP share is only **3.1%** of today's tape.

`uw oi biggest-increases --min-dte 180` returned 100 raw contracts market-wide; cross-referenced against the 73-name C12 funnel, only **16 contract-level hits across 4 underlyings** survived. AMZN and META entries carried 1–9 total contracts of prior volume (statistically meaningless) and were dropped.

| Candidate | Gates | Killed by |
|---|---|---|
| **FXI** (203 DTE $35 put) | ≤2/9 | 90d cum-flow **−$4.66M MIXED** on ~$370M gross each side; `conviction-matrix` **HEDGED_LONG** conf 33.8% — an explicit disqualifier (DP buy + put protection = hedge, not conviction) |
| **TLT** (203 DTE $87 call, genuinely ask-dominant) | ~1/9 | 90d **−$123.5M MIXED**; `conviction-matrix` **COVERED_CALL** conf 13.8% — an outright-rejected scenario that directly contradicts the single ask-dominant print |
| **NVDA** (840 DTE $230 call) | ≤1/9 | 90d net **+$430,802 on $51.46B gross — a 0.0008% tilt**; `conviction-matrix` MIXED conf 2.1%; and the long-dated strike is **bid-dominant** (988 ask vs 2,336 bid), i.e. call-writing not LEAP buying |
| **INTC** (203/293/840 DTE calls) | ≤1/9 | 90d **−$895.8M MIXED**; long-dated prints scatter across four strikes on different days — dispersion, not one accumulating thesis |

The failure pattern is uniform and worth recording: `oi-trend` fired **BUILDING on 4 of 4** (consistent with the documented 14-of-14 zero-discrimination finding) while `cumulative-premium-flow` was **flat/MIXED on every single name** — the flow gate did all the discriminating work, exactly as designed.

---

## 5. Volatility Surface

**Book-level VRP bias: premium-BUYING.** SPY −0.0027 / QQQ −0.0418, both FAIR — IV at or below realised. Every confirmed IV-vs-RV gap found today was **negative** (vol cheap), reinforcing the index read. No SELL VOL idea in this report clears that headwind at full size.

**Dispersion read:** SPY `rv20` **10.1** vs QQQ **17.8** is a wide index spread, and the semis complex sits at 35–115 (SMH 35.0, SOXX 39.4, NVDA 45.1, MRVL 87.9, SOXL 114.8) — yet TSM, ASML, NVDA, AMAT and LRCX all print `iv_percentile` **0** (LOW_IV). Single-name and sector vol has **not** caught up to realised turbulence. That is a genuine dispersion setup (buy single-name/sector vol vs index) — flagged as context only; no structure is sized here.

**Substrate hygiene, and why it matters.** Raw `iv-term-structure` returned **BACKWARDATION on 16 of 16** names sampled — mechanically, zero discriminating power. After `scripts/term_structure_hygiene.py` (min_contracts 15, a **named tunable, not audit-frozen**), **14 of 16 flipped**. Post-hygiene: KINKED 11/16, BACKWARDATION 3/16, CONTANGO 1/16, FLAT 1/16; and the monotonic `base_shape` splits a far more informative BACKWARDATION 8 / CONTANGO 7 / FLAT 1.

**Population firing rates** (the discipline that separates signal from mechanism):
- raw BACKWARDATION: **16/16 (100%)** — useless
- `front_end_iv_ratio@7` > 1.05: **8/15 measurable (53%)** — discriminating properly
- `term-skew` COMPLACENT: 10/16 (62.5%) — high firing rate, low standalone power; only SOXL showed genuine TAIL_HEDGING (skew_ratio 1.124), consistent with real semis stress
- `iv-percentile-zscore`: **every name returned `dates_used: 97`** against a 252-day request — all percentiles below are **PROVISIONAL**, not true 252d percentiles.

**Two names clear a genuine confirmation leg:**

| Ticker | raw → hygiene → base | flipped | FE@7 | kink | IV-vs-RV | rv20 | Read |
|---|---|---|---|---|---|---|---|
| **MRNA** | BACKW → **KINKED** → CONTANGO | yes | 1.198 | **14DTE (09-11), 37.1%** | **−301.7pp** | 375.2 | **BUY VOL** confirmed; long straddle at the 09-11 tenor; implied move ~22.6% |
| **MRVL** | BACKW → **BACKWARDATION** → BACKW | **no** | 1.126 | — | **−30.3pp** | 87.9 | **BUY VOL** confirmed despite the backwardation label; **not** a calendar (ratio not falling); implied move ~7.7% |

**Everything else is `watch_only`** — hygiene-corrected labels with no independent confirmation leg: AMAT (FE@7 **1.285**, most panicked in the scan), LRCX (1.119), MDB (1.64), LULU, PANW, MSTR, NOW (calm, nothing to trade), TSM (fully flipped to FLAT), ASML (flipped to CONTANGO).

**A macro artifact worth naming:** NVDA, AMZN, META and SOXL all kink at **exactly 7DTE = 2026-09-04 = NFP**, prominence 5–14%. That is a market-wide event bump priced uniformly across unrelated names — context, not stock-specific mispricing.

**`ESTC` is `NO_NEAR_TENOR`, which is not `FLAT`** — no listed tenor at or under 7DTE exists, so its front end is **unmeasurable**. A 1.000 ratio there means "no data", never "calm".

**The `iv_rank` lanes were unusable today and were not mined.** All 25 `iv_rank_high` rows sit at exactly 100 and are near-all illiquid or suffixed artifacts (CLBK2, SNEX2, NVDX1, DFDV1, AVO1, ATRO1, IREZ1, AZUL1, REZI1, SMU2, NXH, INV, SPWH, BRLT, MERC, AWRE, CINT); `iv_rank_low` is all-zeros (IREN, QS, ONDS, RKLB, ASTS, BE, AFRM…). Zero discrimination, nearly all C12-fail. Similarly `iv_outliers` was dominated by 0DTE noise (WEN, SOXS, SOFI, RXT, IONQ, TOST, NIO), yielding no actionable non-0DTE outlier.

**Earnings vol lane** — 4 of 78 catalyst rows intersect the C12 funnel:

| Ticker | Earnings | Days out | Tenor spans event? | FE@7 | Re-derived move | Verdict |
|---|---|---|---|---|---|---|
| MDB | 09-01 PM | 4 | ✓ (09-04) | 1.64 | **16.4%** | SELL VOL, half |
| LULU | 09-03 PM | 6 | ✓ (09-04) | 1.542 | **9.7%** | SELL VOL, half |
| PANW | 09-01 PM | 4 | ✓ (09-04) | 0.706 | 12.4% | **SKIP** — kink at 09-11 is CPI, not earnings |
| CIEN | 09-03 PM | 6 | ✓ (09-04) | 1.403 | 12.6% | **SKIP** — VRP −0.0333, realised running *ahead* of implied |

**The INVALID list is empty** — all four tenors genuinely span their events. But note the **structural finding**: for any name reporting inside the first surviving tenor, the kink-finder **cannot** place a kink at the event by construction (a kink needs an interior local max with two lower neighbours, and the front tenor has no left neighbour once 0DTE is dropped). MDB/PANW/LULU were all tagged KINKED with the kink one-to-two tenors **past** the earnings tenor. **None of the three "kink at earnings" reads is valid**, and this will recur on nearly every ≤7-day earnings name.

Both SELL VOL calls are **half-size** because back-month skew is flat/COMPLACENT on all four names — the tail is never priced alongside the front event. And both are single-agent, so neither entered the rubric.

---

## 6. Risk & Correlation

**Macro headline:** stagflationary tilt — core PCE **3.34%** sticky above target, payrolls **−23k**, 10Y **4.67 rising**, USD weakening, curve normal and bull-steepening (+0.39). Forward Tier-1: **NFP T+5, PPI T+8, CPI T+9, FOMC T+12.**

**Breadth:** 229 advancers / 273 decliners, **45.53% green**, median constituent −0.13%. SPY closed red (−0.23%) and breadth is also below 50% — the two **agree**, so there is no hidden-distribution divergence today (unlike 08-27). Advisory, 0 rubric points, no sizing effect.

**Correlation clusters: none.** No pair reached the 0.70 threshold on today's candidate set.

| Pair | corr | Band | Action |
|---|---|---|---|
| MRVL / SNDK | **0.673** | soft watch (0.60–0.70) | **No penalty.** Both are semis de-rating expressions — the pair to watch if a future session scores both |
| MRVL / IWM | 0.595 | below | not surfaced |
| NOW / MDB | 0.548 | below | not surfaced |
| MRNA / TLT | 0.545 | below | not surfaced |

**MRNA and MRVL do not pair above the 0.506 reporting floor** — the two scored names are genuinely independent bets. The soft-watch pair was **not** discretionarily upgraded to a cluster.

> **Substrate defect confirmed and NOT propagated:** `portfolio-correlation.sector_breakdown` returned `{"Unknown": 10}` with a spurious `"CONCENTRATION: 100% of tickers in Unknown"` warning. All 10 rows carry `sector: "Unknown"` — the figure is an artifact of missing metadata, not real concentration. **The false warning was discarded and played no part in sizing.** Real sector concentration was assessed off the netted `market-regime.sector_rotation` instead.

**Fundamentals verdicts:**
- **MRNA → CAUTION (−1 tier).** 4-of-4 EPS beat streak and low leverage (D/E 0.073) support the long, but revenue **−27.62% YoY**, net margin **−141.4%**, a **dilutive private debt offering announced 08-28**, and an insider sale of **−499,246 shares** (MSPR −24.93) into the same tape contradict it. No dated catalyst found for the 09-11 vol kink. Next earnings 2026-11-04 (T+68, outside).
- **MRVL → VETO.** 2-of-3 fundamental legs contradict the short (Q2 beat-and-raise; +34% YoY revenue with 29% net margin); only insider selling (MSPR −30.71) supports it. `next_earnings_date` returned `null` — a post-print cache gap, explicitly **not** treated as absence of event risk (next print ~late Nov 2026).

**Event-risk gate fires on both** — three-to-four named, dated Tier-1 prints inside a 1–4 week horizon, with undefined-risk directional expressions rather than event plays.

**Debate-disconfirmation:** MRNA **fires** (bear 0.65 ≥ bull 0.25, the widest gap on the board). MRVL's literal formula no-ops (bear 0.25 < bull 0.65) — but the call is a **short**, so the trade-*advocating* side is the bear at 0.25 and the trade-*opposing* side is the bull at 0.65: the disconfirmation step decisively did **not** clear this trade. Recorded as firing on the direction-adjusted reading, with both scalars stated so the arithmetic is auditable.

> **Flagged for the next `/calibration-audit` (instrumentation, not a live rule change):** the `bear ≥ bull → −1 tier` formula is written in long-oriented framing and **inverts its meaning on SHORT calls** — applied literally, a short thesis both advocates agree is weak scores as *clearing* the gate. The live rule was not rewritten; the outcome is moot here (MRVL is VETO'd and short-routed regardless). This should be registered and mechanized rather than left to per-session judgment.

**Adverse-flow exit list.** `conviction_2026-08-27` **does not exist** — the most recent daily group is `conviction_2026-08-21 = ['IWM']`, with no groups for 08-24 through 08-27, consistent with four further empty boards that correctly wrote nothing.

- **IWM — EXIT CANDIDATE.** The carried thesis was a long vanna-squeeze. Today: `flow_direction: bearish`, net flow **−$7,285,407**, put/call ratio **2.544**, close 295.75 (−1.35% today, −1.40% 5d, worst major). Alerts: `LARGE_DARK_POOL` (high, $49.6M on 3,091 trades), `OI_SHIFT` (high, net OI +238,826), `LOW_IV_RANK` (medium, iv_rank **1.10**). The OI build is arriving alongside a 2.54 P/C ratio and negative net flow — **the build is put-side, adverse to the long thesis, not confirming.** Today's dealer-positioning read still sees a squeeze building, but that read explicitly disagrees with both tape and flow.
- `fz quote-drift IWM --since 2026-08-21`: no field changes; no short-float spike, no target cut. No adverse-fundamentals exit candidate. (Store's latest IWM snapshot is 08-22 — staleness noted, advisory only.)

**Hedge sleeve: nothing to hedge.** Net book delta is zero — one call floors at `skip`, one routes to `watch_only`. Directional skew is undefined on an empty book, so proposing an SPY/QQQ vertical or a VIX ladder would be manufacturing exposure, not managing it. Two context notes: (1) if residual IWM exposure is carried, protection is unusually cheap at `iv_rank` 1.10 — that argues for **closing or collaring** the tagged exit candidate, not a new sleeve; (2) the 0DTE premium-sell lane is not a green light (see §2a).

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Empty. No name reached MEDIUM (7) or HIGH (9).** Highest score on the board was **1**.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: not computable this session. There are no HIGH/MEDIUM rows to tier, and the rolling `conviction_<date>` closed-call population contains no decided HIGH/MEDIUM rows post-freeze (the freeze-lift has been structurally unrunnable for eight consecutive cycles). Per-tier realised expectancy and payoff ratio are therefore **unavailable**, not zero.

Both scored names are recorded below for audit continuity even though both dropped.

| Field | MRNA | MRVL |
|---|---|---|
| `raw_score` / tier | 1 / DROP | 1 / DROP |
| direction / horizon | long / swing | **short** / swing |
| `dominant_signal_class` | `dark_pool_accumulation` | `dealer_positioning` |
| `win_rate` (n, source) | `null` (0, **`NA(substrate)`** — class returned **0 rows market-wide**) | `null` (0, **`NA(substrate)`** — class **not backtest-supported**) |
| `market_excess` | `null` — no kept windows to benchmark | `null` |
| `cum_flow_30d / 90d` | +$2.84M / +$38.69M (both MIXED) | +$52.61M / +$283.62M (both MIXED) |
| `implied_move` | 22.6% (09-11 tenor) | 7.7% (09-04 tenor) |
| `dp_block_to_float_ratio` | **0.001123** (410,300 sh / 365.28M float) | `null` |
| `insider_cluster_flag` | `null` | `null` |
| pre-risk size | `skip` | `watch_only` |
| `fundamentals_verdict` | **CAUTION** (−1) | **VETO** |
| bull / bear residuals | 0.25 / **0.65** | 0.65 / 0.25 |
| gates fired | panic −1, fundamentals −1, event_risk −1, debate −1, rubric_regime cap-half | fundamentals VETO, short-routing, regime −1, panic −1, event_risk −1, debate (direction-adj) |
| **final size** | **`skip`** | **`watch_only`** |
| invalidation | loses the **$137.50** second-tier DP shelf | DEX flips positive ≥3 sessions, or FE@7 < 1.05 |

**`market_excess` is `NA(substrate)` on both names — not zero, and not null-by-omission.** Neither class has a usable backtest leg, so no `beta` flag can be assigned in either direction. The entire scored board today is **unmeasurable against SPY**. That is a measurement gap worth surfacing rather than burying.

**Score component detail:**

*MRNA* (Σ = 1 ✓): **+1** accumulation conjunction C11 [accumulation-hunter / `uw insights institutional-accumulation`] — *a +3 line halved because cum_flow_30d +$2.84M = +0.109% of gross fails both the $50M absolute and 5% scale-relative bars*; **+1** vol-surface KINKED with VRP-aligned bias [vol-surface-scout / `uw options-structure iv-term-structure`]; **−1** `flow_conflict_lite`.

*MRVL* (Σ = 1 ✓): **+1** mechanized DEX sign flip [dealer-positioning-strategist / `scripts/dex_flip.py`]; **+1** vol-surface unflipped BACKWARDATION, VRP-aligned [vol-surface-scout / `uw options-structure iv-term-structure`]; **−1** `flow_conflict_lite`.

**On the MRVL `flow_conflict` judgment call.** The literal mechanical read gives **−3** under both phrasings (|+$52.6M| exceeds both the $27.73M union median and the $50M bar, with the sign opposing a short). **−1** was applied instead, for four stated reasons: the tool's own `trend_direction` returns **MIXED**, declining to assign the sign that branch 1 presupposes; net is **1.094% of the name's own $4.81B gross** (the award side of this rubric has a 5% scale-relative floor for exactly this reason — the deduction side's lack of one is a documented defect, not a licence); **29 of the 30 sessions in the flow window pre-date the DEX flip being scored**, the same staleness pattern both debate sides conceded on GLD 2026-08-21; and the "union median" is degenerate at n=2. **This choice is not load-bearing** — under −3 MRVL scores −1, under −1 it scores 1, under a non-directional vol class it scores 2; all three are below the floor and all three produce DROP.

**Two substrate defects re-confirmed live today**, both worth carrying into the next audit: `dark_pool_accumulation` returned **0 rows market-wide** (`total_signals: 0`), meaning the accumulation lane is structurally unmeasurable; and MRVL's `oi-trend` returned **`consecutive_build_days: 98`** with 9 of the top-10 builds at 0DTE — the strongest single datum yet for the BUILDING zero-discrimination finding.

<details>
<summary><strong>Conviction scoring rubric (Step 4), verbatim — rubric_version 2026-06-12 (FROZEN)</strong></summary>

```
Daily conviction score = Σ:
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna-squeeze setup in trade direction —
      the trigger must be a verified SIGN CHANGE, not a level: sign(net_dex) on the latest session opposite to
      ≥3 consecutive prior sessions, read from dated `uw options-structure dex --date` calls, with |net_dex| on
      the flip day ≥ 0.25× the trailing-10-session median |net_dex|; evidence must cite both dated values.
      Compute with `python3 scripts/dex_flip.py` — do NOT do the arithmetic by hand. Vanna disjunct additionally
      requires a dated VIX source. [DEMOTED +3→+1 and MECHANIZED 2026-06-12 audit P0.4]
  +3  3+ aligned signals in accumulation-hunter (DP + OI + uw oi smart-positioning, uw dark-pool block-stratified
      institutional-tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms (sign
      aligned AND |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: award only when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +1  uw historical cumulative-premium-flow shows net directional accretion in trade direction (30d) —
      INTENT-SCREENED: no C28 distribution_flag, and not deep-ITM sub-parity dividend-capture. [DEMOTED +3→+1]
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector — CONDITIONAL:
      (a) sector persistence_score ≥ 0.6 AND (b) cum_flow_30d direction aligned AND (c) |cum_flow_30d| ≥ $50M.
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising uw historical pc-ratio-zscore (VRP positive)
      # MECHANISM: an INFORMED-FLOW CONTINUATION penalty, not "crowd is wrong, fade it".
  -3  flow_conflict — cum-premium-flow 30d direction clearly OPPOSITE dominant_signal_class
  -1  flow_conflict_lite — 30d cum_premium_flow read is MIXED (near zero, or bottom-quartile magnitude)
      # -3 and -1 are MUTUALLY EXCLUSIVE — apply ONE, never both.
  # TIER GATES (0 points, applied by risk-monitor in 2d, never in score_components):
  -1  [TIER GATE] correlation cluster (pairwise corr ≥ 0.70) — −1 TIER
  -3  [TIER GATE] market-regime conflicts with trade direction — −1 TIER
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | HIGH | full (subject to load-bearing-tool gate + win-rate gate) |
| 7–8 | MEDIUM | half (subject to win-rate gate) |
| 3–6 | LOW | starter / watch-only |
| ≤ 2 | drop | filtered by the quant's drop floor |

**Tier-cut status (2026-06-12):** the ≥9 HIGH cut was set in-sample on UPTREND data and **failed its scheduled re-confirmation** — bands inverted on the first post-UPTREND window (HIGH 0.222 / MED 0.214 / LOW 0.444). The cuts are retained under the P0.1 freeze but carry **no validated ranking claim**; the P0.6 out-of-regime guard caps all sizing at half in the interim.

</details>

---

## 8. Watch-only — single signal, no confluence

Surfaced by exactly one Phase 1 agent (or resolved as void). Listed for journaling, **not for trade entry today.**

| Ticker | Flagging agent | Read | Why it failed the gate |
|---|---|---|---|
| **NOW** | accumulation-hunter | 4 aligned signals, `cum_flow_10d` **+$86.17M BULLISH** (25.8% of gross); C34 shelf $143.60, origin block $138.43 ($23.8M @12:39:58Z) | Single agent. **⚠ `distribution_flag: true`** — two institutional-size Sep-18 CALL OI closures (−1,404 @150C ~$408.7K; −604 @135C deep-ITM ~$472.2K) on a **+4.5% day**: someone unwinding bullish exposure into strength. Mega-tier buy_ratio 1.0 but **n=3, too thin** |
| **MSFT** | sweep-tracker | 3/5 persistence, ask-side Nov-20 420/480 call buys, `cum_flow_30d` +$809.7M BULLISH, +$145.0M net premium today | Single agent. Dealer-positioning is NEUTRAL (DEX level, **zero** sign changes); multileg explicitly **not** scored (no shared timestamp / matched size — separate blocks) |
| **MDB** | earnings-scout | SELL VOL half; VRP +0.2402 PREMIUM_SELLING confirms; move **16.4%** at 09-04 | Single agent. Vol-surface `watch_only` — the 21DTE kink is a strike-weighting artifact |
| **LULU** | earnings-scout | SELL VOL half; VRP +0.1747; move **9.7%** | Single agent. **Multileg VOIDED it as a PARITY ARTIFACT** (below). Price/flow divergence: +5.05% on −$12.9M bearish flow |
| **FXI** | multileg-strategist | Atomic 4-leg collar/overwrite, all legs @17:39:40Z; net credit ~$15.4M; CONTANGO-anchored; net short-delta ~−39K | Single agent. **Risk cap UNCONFIRMED** — two short calls are uncapped if uncovered. Single-day, no repeat. LEAP radar disqualified it (HEDGED_LONG) |
| **TLT** | multileg-strategist | 3-leg put diagonal @13:33:44Z, 65,000 each leg; net debit ~$2.9M; **4-session recurring campaign**; spans CPI + FOMC; net long vol into events priced FLAT | Single agent. Offsetting large ask-side call buying (Sep-30 C84 ~35K, Oct-16 C83 ~9.9K). LEAP radar disqualified it (COVERED_CALL) |
| **IWM** | dealer-positioning | Cleanest vanna-squeeze in the scan; put-heavy book confirmed two ways; live falling-VIX leg | Single agent, and an index. **DEX flip does not qualify mechanically** (flip predates today). Now also an **exit candidate** — see §6 |
| **AMAT** | dealer-positioning | Multi-day-confirmed GEX regime flip (NEG 8 straight sessions since 08-18) | No clean positive. **`FE@7 1.285` already past the 1.10 invalidation bar** — self-invalidating |
| **SNDK** | sweep-tracker | 5/5 bearish persistence, $1.36B; −$171.8M net premium | Single agent, and **multileg resolved the structure as a position ROLL**, not a fresh short (matched 1,700 size, same second, near-zero time value) |
| **CIEN** | — | BEARISH_EXTREME z=2.949; signal-confluence bearish 5/5 | **Zero positive flags.** Earnings-scout SKIP (VRP −0.0333, realised *ahead* of implied); contrarian DISQUALIFIED it — **earnings 09-03 + backwardation = event pending, not crowding**; the put skew is a real hedge bid |
| **META** | — | Tier-1 FLOOR_PUT_BLOCK (21DTE, $18.1M, size/OI 1.49) **conflicting** with a Tier-3 bullish call print same day | **Zero clean positives.** Accumulation-hunter **screened it out** as closing-cross contamination; sector-leader gate failed (cum_flow −$36.8M, wrong sign); dealer-positioning NEUTRAL |
| **NVDA** | — | −$178.4M net premium (largest single-name bearish on the board); 140-DTE call unwind, OI −80,731 ($815M prior premium) — real distribution into a 30-day rally | **Zero positives.** Sweeps mixed both sides, cum-flow MIXED; accumulation-hunter excluded it (mega tier sell-dominated, 0.364) |
| **GLW** | — | Flagged −$75.1M bearish anomaly | **VOID — parity artifact.** Mar-27 C60 / Jan-27 C55 / Dec-18 C70 all deep-ITM (delta 0.97–0.99), time value ~$0.5–2 on a $151 spot, `side: no_side`. Deep-ITM **call sales** booking as bearish premium — the call-side mirror of the LULU pattern. **Not genuine bearish conviction; score nothing** |

**Contamination screen — excluded from the accumulation board, not silently omitted.** AMZN, META, TSLA, AVGO and PLTR all showed mega-tier "buy" dominance driven by **1–7 prints pinned to the exact closing price** in the 20:00–21:20Z window (AMZN: $179.05M + $167.84M both at 20:55:01Z @ $266.43, with the top price bucket carrying 21.4% of the name's total DP premium across 124 trades). **GOOGL's mega tier is sell-dominated** (buy_ratio 0.091, a $708.0M print at 20:00:06Z). This is the same closing-cross/basket signature logged on 2026-08-20. MRNA is the notable name that **passed** this screen.

**`fz` advisory lanes.** The upstream **doubled-first-letter bug** was present again on every bulk `fz screen` surface (AABEO→ABEO, EESTC→ESTC, TTEAM→TEAM) and was corrected before use; per-ticker `fz_enrich` is healthy. The squeeze screen returned only an **alphabetically truncated A–B page** (20 rows) — partial coverage, not a ranked top-20. **ESTC** (+19.31%, new high) and **BOX** each appeared in both a `uw` funnel and the `fz` RS lane; neither drew a second scoring agent. Notable squeeze context: **ASTS** 31.76% short float / 3.20 days-to-cover.

**C12 liquidity floor:** 73 of 91 funnel names passed; **18 dropped** — PD, BBW, QFIN, PDS, GHM, CLDX, MBX, XSD, WD, FNKO, AMPL, NIQ, KFY, AI, ASAN, BEAM, ARQQ, ABR (all sub-$50M 20d dollar-ADV). The `volume_vs_average` lane was near-worthless today: 25 of 25 rows were micro-ETFs (BFOR, FFTY, USAI, GLAM, TWM, HYLB, DYNF, PFFV…), essentially all C12-fail.

---

## Watchlist write-back

**Nothing written.** `watchlist_write_back_confirmation: {written: false, group: "conviction_2026-08-28", tickers: []}`

The corrected rule (2026-07-23) permits only **LOW-tier-or-better** names, never the raw top-5. Both scored names carry `raw_score 1` — two full points below the LOW band floor of 3 — and both are tier DROP; MRVL additionally carries a fundamentals VETO. **No candidate qualifies.** Writing a DROP name in to produce a non-empty group is exactly the failure mode the corrected rule exists to prevent: it would seed tomorrow's correlation and adverse-flow checks with a thesis the desk explicitly declined to take. `uw watchlist manage` was not called; no other group was touched.

Prior group read for alerts/scan: `conviction_2026-08-21 = ['IWM']`. `conviction_2026-08-27` does not exist — 08-24 through 08-27 were also empty boards.

---

## Deep-dive hand-off

**Skipped** — no HIGH-tier names. Per Step 8.5 the hand-off is skipped entirely on a no-edge day.

One optional follow-up, flagged rather than actioned: **MRNA's vol leg is the most interesting standalone read on the board** — a −301.7pp IV-vs-RV gap and a 37.1%-prominence 14DTE kink with no identifiable catalyst. If anyone wants it resolved, that is a `uw insights deep-dive` question, and `rv20 375.2` should be checked for single-jump inflation from the 08-28 debt-offering news first. It cannot be scored (single agent) and is not proposed as a trade.
