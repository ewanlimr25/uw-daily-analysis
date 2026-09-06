# Daily Market Analysis — 2026-08-06

## Executive Summary

- **Regime + GEX state:** **TRANSITIONAL** (trend UPTREND) — SPY 768.56 −0.16%, above 20SMA 749.26 and 50SMA 746.73, +3.11% 30d, −1.07% from the 90d high. VIX 15.15 (−4.17% 1d, −11.35% 5d). **UW options-flow breadth 34.1% bullish** (2,141 of 6,281) against a 40.16%-green cash tape. **RSP −0.52% underperformed SPY −0.16%** — narrow, cap-weighted-carried. SPY gamma is thin (`total_gex` +$33M, drained from +$1.29B in four sessions) with the **put wall 768 sitting 0.11% from spot**; QQQ's gamma regime **flipped POSITIVE→NEGATIVE today**. Netted sector rotation: **IN** Technology +$620.3M / Industrials / Comm Services; **OUT** Consumer Cyclical / Defensive / Basic Materials.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** SPY — NEGATIVE, ZGL 814.60 **unreliable** (5.95% away), call wall 775 / put wall 768 (at spot), thin book, no clean pin. QQQ — NEGATIVE, ZGL 749.31 (borderline-reliable, 4.73%), call wall 730 / put wall 700, **regime flipped today = maximally fresh and unstable**. Advisory, see §2.
- **Top swing build:** **NONE.** No name cleared the Step-3 confluence gate with a survivable score. **20th consecutive empty conviction board.**
- **Top LEAP candidate:** **NONE.** LEAP DTE share is 3.5% of market volume; zero of four funnel-eligible names cleared 6-of-9 gates.
- **Biggest risk:** **July NFP prints tomorrow 2026-08-07 08:30 ET, pre-open, into a near-zero dealer long-gamma cushion.** Secondary: the AI-infra/semis correlation complex (SNDK/MU 0.896, CRWV/NBIS 0.876, 10 pairs ≥0.70) is one bet, not eleven.

---

## 1. Regime & Gamma State

`uw risk market-regime` returns **TRANSITIONAL — "Half position sizes. Favor defined-risk strategies. Iron condors in range."** with `trend: UPTREND`. The label and the tape disagree in an informative way: SPY sits above both moving averages after a +3.62% five-day run, but only **34.1% of 6,281 optionable tickers show bullish flow**. The options tape is materially more bearish than the price tape.

The cash tape confirms narrowness rather than strength. Equal-weight **RSP fell 0.52%** against SPY's **0.16%** — the cap-weighted top carried an otherwise soft session. Only four sectors closed green: **XLE +1.48%**, SMH +0.31%, XLC +0.28%, XLV +0.18%. The weakest were XLB −0.89%, XLRE −0.86%, XLI −0.85%.

Five-day context matters for reading today as a pullback rather than a turn: XLK +5.46%, SMH +6.05%, XLY +5.08%, QQQ +4.55%, SPY +3.62%.

### Per-index gamma (current-state EOD book)

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 768.85 | 814.60 (**unreliable**, 5.95% away) | **+$33.3M** | NEGATIVE | 775 (+$357.4M) | **768** (−$132.4M, **0.11% from spot**) |
| QQQ | 715.47 | 749.31 (borderline, 4.73%) | +$127.2M | NEGATIVE (**flipped today**) | 730 (+$78.5M) | 700 (−$19.7M) |
| IWM | 298.25 | ZGL grid artifact (100.02 / 309.44 — physically implausible) | choppy, no trend | flips near-daily | — | — |

**The load-bearing observation is the drain, not the level.** SPY `total_gex` fell +$1.29B → +$1.10B → +$636M → **+$33M** across 08-03→08-06; QQQ fell +$774M → +$624M → +$285M → **+$127M**. Both trajectories are smooth and mutually corroborating, unlike the point-estimate ZGL, which carries the known SPY/QQQ/IWM grid artifact (QQQ printed 249.5 mid-window; IWM printed 100.02 against a $298 spot). Dealer long-gamma cushion has quietly evaporated into a Tier-1 macro binary. That raises realised-vol fragility — it is **not** a directional signal.

**DTE volume share:** BALANCED — 0DTE 28.4%, weeklies 29.9%, monthlies 28.5%, LEAPs 3.5%. Neither a retail-dominated nor an institutional-positioning tape, so rotation and swing conviction get neither bonus nor uniform downgrade.

**VRP:** SPY IV30 0.1298 vs realised 0.1339 ⇒ **−0.0041, FAIR**. QQQ IV30 0.2143 vs realised 0.2568 ⇒ **−0.0424, FAIR**. Both slightly **negative — realised exceeds implied.** This is a premium-**buying** tilt and it contradicts the naive "VIX 15, sell vol" instinct. It aborted the contrarian short-premium lane fleet-wide and it is why no calendar or credit structure appears anywhere below.

### Macro backdrop

Yield curve **normal** at +0.44 (10Y 4.63%, 2Y 4.18%). Core CPI **2.81%** YoY, core PCE **3.29%** YoY — PCE still running well above target. Unemployment 4.2%, payrolls **+57k** (decelerating). 10Y **rising** (+0.15 over 30d), broad USD **weakening** (−1.44 over 30d). Fed funds effective 3.63%.

**Forward Tier-1 calendar:**

| Date | Event | Impact |
|---|---|---|
| **2026-08-07** | **July Employment Situation / NFP, 08:30 ET** | **HIGH — tomorrow, pre-open** |
| 2026-08-12 | CPI (July) | HIGH |
| 2026-08-13 | PPI (July) + initial jobless claims | MEDIUM / LOW |
| 2026-08-19 | FOMC minutes (July meeting) | MEDIUM |
| 2026-08-21 | Monthly OPEX | MEDIUM |
| 2026-08-28 | Core PCE (July) | HIGH |
| 2026-09-16 | FOMC decision + SEP | HIGH |

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — built from open interest that persists overnight — read forward as the *prior* for the next session's open. Prose-only, **0 rubric points**, no backtested predictive claim. Predictive validation of these levels lives in `/weekly-analysis`'s rolling §2 backtest, not here. Scope is SPY and QQQ only.

### SPY — thin book, put wall on top of spot

`regime` NEGATIVE, `total_gex` **+$33.3M** (marginally positive, effectively neutral), ZGL 814.60 with **`zgl_reliable: false`** (5.95% above spot, outside the ~5% trust band — falling back to the `total_gex` sign plus spot-vs-wall position). Call wall **775** (+$357.4M, the dominant strike in the whole book, 0.80% above spot). Put wall **768** (−$132.4M) — **0.11% from spot, effectively underneath the close.**

**Read:** the put wall sitting on the print is the standout feature. Dealers are already short gamma at the current level, so a move either way in the first 30–60 minutes plausibly flips the local sign fast. Do not treat 814 as a magnet — it is an extrapolation. The tradeable structure is the tight 768→775 band. Below 768 the book is thin and offers little dealer-driven cushion; a downside gap could accelerate rather than get absorbed.

**Structure bias:** this is **not** clean long-gamma pin material. A narrow iron fly / butterfly centred 768–770 only works if NFP resolves calm. If NFP surprises, this reverts to a short-gamma trend read and a debit vertical (toward 775 on a beat, toward sub-768 on a miss) is the more honest expression. Do not lean on 775 as a hard cap.

### QQQ — freshly flipped, wider walls

`regime` NEGATIVE, `total_gex` +$127.2M, ZGL 749.31 with `zgl_reliable: true` **but borderline** (4.73%, just inside the band — a small overnight move pushes it outside). Call wall **730** (+$78.5M, 2.03% above). Put wall **700** (−$19.7M, 2.16% below).

**Read:** `gex-time-series` shows the regime **flipped POSITIVE→NEGATIVE today, 2026-08-06** (`zgl_delta` +499.81, the largest jump in the 30-day trajectory). This is a maximally fresh, unstable flip — the dealer book went from stabilising to potentially trend-amplifying on today's close. Combined with a wider, more symmetric 700–730 spread, tomorrow's realistic range is wider than SPY's and a break of either wall has less gamma cushioning it.

**Structure bias:** freshly-flipped short gamma plus a real catalyst inside the window favours **debit verticals or a long straddle/strangle toward the wall edges** over premium-selling. This is not a pin setup. A condor is the lower-probability branch, viable only if NFP prints in line and QQQ re-stabilises intraday.

### Mandatory caveats

- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and recomputes the ZGL and walls. This is especially live for QQQ, whose flip happened *today*.
- **ZGL reliability.** SPY's is explicitly unreliable (5.95%); QQQ's is borderline (4.73%). IWM's is a recurring grid artifact and is not reported.
- **Gap risk voids the prior.** **NFP at 08:30 ET tomorrow is pre-open.** A fresh short-gamma flip plus a Tier-1 macro print is the highest-instability combination this book produces. The 08-07 expiry alone already carries $5.8B notional — the largest single expiry in the book.
- **Tooling limit.** `uw` cannot isolate the D+1 expiry (`gex --dte-max 1` errors). This is the standing **0–45 DTE** book as proxy.
- **ETF book.** SPY/QQQ ETF gamma, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup — **STAND ASIDE**

`scripts/zerodte_setup.py` returns `sell_premium: true` for both indices with `backtest.verdict: GO_PREMIUM_SELL_INTRADAY` (SPY n=60, 88.3% open-entry win rate, **mean_pnl_open_pct +0.224% gross / +0.124% net** of an assumed 0.10% round-trip; QQQ 85.0%, **+0.362% gross / +0.262% net**). `pnl_basis` is **percent-of-underlying-spot-notional, GROSS** — not premium-collected, not margin-relative.

**Two independent reasons override the `sell_premium: true` flag today:**

1. **VIX 15.15 is the LOW tercile** (bounds 16.5 / 18.1), where the backtest's own conditioning shows **mean PnL −0.052% for SPY and +0.007% for QQQ** — i.e. **no edge at this vol state**. The positive headline expectancy lives entirely in the MID (+0.39 / +0.563) and HIGH (+0.335 / +0.515) terciles.
2. **NFP prints 08:30 ET pre-open**, and the entry rule requires waiting for the gap to resolve. A macro binary is precisely the tail this validation sample does not contain.

| Index | sell_premium | vol_state | VIX | Implied move | Expected range | Size scalar | Suggested structure | Caution |
|---|---|---|---|---|---|---|---|---|
| SPY | true (**overridden**) | LOW | 15.15 | 0.88% | 0.85% | 0.50 | iron fly / short straddle @ 768.85, wings ±0.85% | — |
| QQQ | true (**overridden**) | LOW | 15.15 | 1.47% | 1.48% | 0.25 | iron fly / short straddle @ 715.6, wings ±1.48% | Front-end backwardation (0DTE IV 1.54× VIX) — event/gap risk, half size |

**Verdict: stand aside on the 0DTE premium-selling lane tomorrow.** SPY ≈ SPX (validated identical); QQQ is the weaker of the two (Nasdaq index book unavailable) and additionally carries a backwardation caution. Advisory, **0 rubric points**, and explicitly **not** a guaranteed edge — the validation sample contains no vol shock, so the short-vol left tail is **UNSAMPLED**. Promotion bar unchanged: this lane stays advisory permanently until a vol-shock day enters the sample **and** net expectancy clears a tail-aware bar. Win rate is explicitly not the promotion metric for a negatively-skewed short-vol strategy.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

**Zero names qualify for the +1 mechanized DEX-flip line. Zero vanna squeezes confirmed.** This is a reportable empty result, not a data gap.

`scripts/dex_flip.py` was run against dated `uw options-structure dex` pulls — a full 11-session series (07-23→08-06) for SPY, QQQ, IWM, SNDK, NBIS, APP, MU, MSTR, AAPL, META, and a lighter 5-session screen for eleven more.

| Symbol | Latest net_dex | Qualifies | Reason |
|---|---|---|---|
| **NBIS** | −$276.3M | **false — near miss** | Genuine sign change (4 prior positive sessions), but \|flip\| $276.3M < floor $318.2M. **`magnitude_ratio` 0.87** — 13% short |
| SNDK | −$3.40B | false | Only 2 consecutive opposite-sign prior sessions (need ≥3) |
| APP | −$1.04B | false | Only 2 consecutive opposite-sign prior sessions |
| MU | +$2.38B | false | 0-session opposite run; **`whipsaw_warning: true`** (4 sign changes / 11 sessions) |
| MSTR | +$518M | false | 0-session opposite run; **`whipsaw_warning: true`** (5 changes) |
| META | +$2.06B | false | 0-session opposite run; **`whipsaw_warning: true`** (4 changes) |
| AAPL | +$8.11B | false | Flip occurred 07-31→08-04 but is now 3 sessions stale |
| SPY / QQQ / IWM | +$53.9B / +$29.9B / +$4.05B | false | 0-session opposite runs — **level, not flip** |

NBIS evidence string, verbatim: `NBIS net_dex 2026-08-05 +1,624,922,035 -> 2026-08-06 -276,281,309; prior 4 sessions all positive; |flip| 276,281,309 vs floor 318,198,343 (0.25x trailing-10 median 1,272,793,372)`.

**Vanna:** only SNDK, NBIS and APP carry put-heavy books (positive `net_vanna`); every index and mega-cap tested is call-heavy, making a vanna squeeze structurally inapplicable there. The VIX leg then fails: dated closes run 07-30 17.09 → 07-31 15.99 → 08-03 15.86 → **08-04 16.50 (+4.04%)** → 08-05 15.81 → 08-06 15.15. That is only **two** consecutive down sessions, not the required three. **The −11.35% five-day headline masks a mid-week spike-and-recovery.** All three are classified "vanna pressure, not a confirmed squeeze."

NBIS carries an additional disqualifier: earnings **2026-08-12** (six sessions out) and the strongest front-end backwardation of the group (1.242). Any put-heavy / DEX-negative read on NBIS is **earnings-confounded**, not dealer-hedging convexity.

**Front-end IV ratio (`--near-dte 7`):** SPY 0.838, QQQ 0.917, IWM 0.902 — all CONTANGO, **no front panic**, consistent with a falling VIX. Single names in backwardation: NBIS 1.242, SNDK 1.140, APP 1.129, MSFT 1.108.

---

## 2b. Sector Rotation

**Rotation regime call: `no_change`, confidence LOW.**

### The direction-sourcing problem, stated plainly

All 11 GICS sectors read **INFLOW** on `sector-flow-persistence` with scores 0.6–1.0. That is **zero discrimination**, not universal accumulation — `sector-flow` and `sector-flow-persistence` are one **gross-turnover** source (`net_flow` = gross call$ − put$, sign-agnostic) and cannot express direction. Direction below is read exclusively off the **netted** `market-regime.sector_rotation`.

Cross-checking netted sign against gross sign produces a clean split: **all three netted-IN sectors agree with gross; all three netted-OUT sectors disagree** (gross was positive on all three). Per C55, the three "out" sectors are **watch_only** at the GICS layer.

| Sector | Netted (authoritative) | Gross today | Agreement | Persistence | Call |
|---|---|---|---|---|---|
| Technology | **+$620.3M IN** | +$1,263.5M | agree | 1.0 | **Confirmed rotation-IN, high conviction** |
| Industrials | +$20.8M IN | +$26.9M | agree | 0.8 | Confirmed, marginal netted magnitude |
| Comm Services | +$9.4M IN | +$320.4M | agree (razor-thin) | 1.0 | Weak / borderline |
| Consumer Cyclical | **−$44.6M OUT** | +$171.2M | **disagree** | 1.0 | **watch_only** |
| Consumer Defensive | −$9.1M OUT | +$70.3M | **disagree** | 1.0 | **watch_only** |
| Basic Materials | −$7.7M OUT | +$77.0M | **disagree** | 1.0 | **watch_only** |

Note that Comm Services is netted-IN by only **$9.4M against $320.4M gross — a 2.9% net-of-gross ratio.** That number resurfaces materially in §6.

### The XLE tension, resolved

XLE was today's best sector (+1.48%) but is −1.36% over five days with $310M of gross turnover. The instrument layer settles it: **XLE five-day cumulative options net flow is −$4.30M with `trend_direction: BEARISH`** — persistent multi-day negative positioning underneath today's price pop. **Today's move is a one-day bounce, not a rotation.** The picture bifurcates within Energy, though: **XOP (E&P) is +$7.01M BULLISH** while majors-heavy XLE is persistently bearish. Any real Energy rotation forming is narrower than the sector price action implies.

### Single-name leaders passing all three +1 gates

Only two names market-wide passed persistence ≥0.6 **and** aligned `cum_flow_30d` **and** |cum_flow_30d| ≥ $50M:

- **SNDK** — persistence 1.0, cum_flow_30d +$1.317B — **subsequently REVOKED** by the quant as a put-sale-netting artifact (§7).
- **META** — persistence 1.0, cum_flow_30d +$477.0M — clean on the letter of the rule, but single-flag and heavily contested (§6).

Explicit gate-(b) failures: **AMD** (cum_flow_30d −$50.3M), **NFLX** (−$124.4M), **SPCX** (−$116.8M) — all three had strong single-day prints and net-bearish 30-day flow.

**Industrials rotation-in is real at the ETF level only** (XLI +$17.98M, clean BULLISH) with **zero qualifying single-name leader** — SPCX fails gate (b), and AXON/CAT/POWL all printed bearish today. Trade the index, not a stock.

### ETF flow tape (advisory — 0 rubric points)

| ETF | 5d net premium | Persistence | DP positioning | Options urgency | GICS agreement | Leaders |
|---|---|---|---|---|---|---|
| **SMH** | +$31.9M | MIXED | Mixed near/through-mid, creation/redemption | Largest sweep Dec-18 $700c ($12.65M), bullish tilt | agree (Tech IN) | see above |
| **XLI** | +$18.0M | **BULLISH** | Near-mid, neutral | Small, mild bullish call tilt | agree (Industrials IN) | none qualifying |
| **KRE** | +$8.08M | **BULLISH** | Near-mid, neutral | Small/mixed | n/a — regional-bank-specific, plausible NIM trade on rising 10Y | none in C12 |
| XOP | +$7.01M | BULLISH | — | — | n/a — resolves the XLE tension | — |
| XLK | +$2.18M | MIXED | — | — | agree (Tech IN) | — |
| **XLE** | **−$4.30M** | **BEARISH** | — | — | n/a — **today's +1.48% is a bounce** | — |
| EWY | −$4.95M | MIXED | Near-mid, mild sell tilt | LEAP protective put + 2 written calls | n/a (Korea) | thin |
| **XLP** | **−$7.49M** | **BEARISH** | Near-mid, neutral | Largest sweep is an ask-side put | disagree at GICS, **ETF confirms OUT** | — |
| **GDX** | **−$31.3M** (largest outflow in the universe) | **BEARISH** | Large prints, mostly near-mid | Two largest sweeps are protective LEAP/long-dated puts | disagree at GICS, **ETF confirms OUT** | — |

XLY (+$0.08M), XLB (−$0.18M), XLU (−$0.36M), XLF (−$1.17M), XLRE (−$0.04M), XLV (+$0.52M), IGV, ITB, XLC, EWT and TAN are all flat/noise-level. Note **XLV is flat despite Healthcare's $194.1M gross number** — another instance of gross turnover overstating a sector.

ETF dark-pool prints are a **positioning/persistence tell** (creation/redemption and hedging mechanics), **not** single-name accumulation; ETF options flow is weighted above ETF DP throughout.

**Swing-book implication:** the honest read is not a two-sided macro rotation but a **concentrated single-sector story** — mega-cap Technology and semis absorbing flow against narrow breadth. Forcing a canonical defensive→cyclical label would be overreach: Consumer Defensive OUT and Industrials IN fit that pattern, but Basic Materials is also OUT (should be IN) and Consumer Cyclical shows no signal at all.

---

## 3. Swing Setups (1–6 weeks)

### 3a. Long swings (regime-aligned)

**EMPTY.** No long-side name cleared the Step-3 confluence gate with a survivable score.

The two names that came closest, and why they died:

| Ticker | Evidence for | What killed it |
|---|---|---|
| **MSFT** | multileg's cleanest structure of the day: two call verticals sharing short strike 570 (Sep-18 C525/C570, Oct-16 C500/C570), legs matched within 2%, **$62.4M net debit**, **repeat build** (`repeat_count` 2 — same program laddered up from 08-03), anchored to a hygiene-verified KINKED 2026-09-18 tenor (n=8,347), risk capped at the debit, `cum_flow_30d` **+$501.5M** | **Single positive Phase 1 flag** ⇒ fails the confluence gate. accumulation-hunter named it and *excluded* it: DP mega buy_ratio 0.708 rests on a **$647.8M print at 20:00:06Z (closing cross)** at the exact closing price $499.86; ex that print mega buy ≈ mega sell. **Block tier ($1M–$10M) buy_ratio 0.446 — sell-leaning.** `conviction-matrix` confidence **14.5%**. `distribution_flag` 500C `oi_diff` **−3,431 on the exact ATM anchor strike.** Fundamentals CAUTION (insider MSPR **−83.89**, 4 of last 6 months at −100). Debate **0.35 / 0.75** |
| **TSM** | multileg 1×2 call ratio, exact 2:1 (Dec-18 C500 16,095 / C560 32,246), single timestamp, ~zero-cost net credit, kink-avoidant (steps past a 79%-prominence Sep-18 kink rather than pay it) | **−3 flow_conflict**: `cum_flow_30d` **−$136.7M** opposes the bullish structure at **1.17× the union median** ($116.8M). Net **−1 ⇒ drop.** Single ticket (`repeat_count` 1) and **no built-in risk cap** — the short 1× is naked above ~620. Also excluded by accumulation-hunter: the dominant DP level $422.50 is **only 3 trades / $430M** ≈ one block cross reported in pieces |

**Invalidation discipline note (C34):** where a name carries a dark-pool price-levels read, the invalidation is anchored to the institutional level rather than a guessed percentage. Today's anchors, for the record: AMZN $272.26 (108 trades, $748.9M — the dominant shelf), TSM $422.50 (**low confidence**, 3-trade concentration), MSFT $499.86 (**low confidence** — this is the closing print, not a defended shelf).

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only` (2026-08-01 P0 #1).** The section runs and carries full theses; nothing is sized. This is routing, not suppression — the theses are scored and serialized so the counterfactual keeps resolving.

**No short was sized today, and none needed routing** — the entire bearish complex arrived single-agent, 0-point, or below the drop floor and was already watch-only on its own merits.

- **TXRH** — `pc-ratio-zscore` **z = +2.485 BEARISH_EXTREME**, P/C 1.968, iv_rank 82.06, volume 6.52×. `price-vs-flow` independently flags **DIVERGENCE**: price +9.2% over 30d against bearish net flow. Term structure BACKWARDATION **survives the hygiene re-derivation** (front-end ratio 1.636, 8 DTE @ 52.2% vs 43 DTE @ 31.9% — real, not 0DTE noise). **Per the mechanism correction this is a short-*continuation* setup, not a fade** — single-name P/C extremes predict continuation, not reversal (Pan-Poteshman 2006; Ge-Lin-Pearson 2016), so the informed read is that the put buyers are more likely right. Only 4 of 5 candidate signals align (no OI capitulation confirmation), which keeps it below the sized bar independently. Structure would be a defined-risk debit put spread; a credit variant is killed by negative VRP. Invalidation: a new lookback high on *rising* net premium, or term structure flipping to CONTANGO.
- **FLR** — z = **+3.142 BEARISH_EXTREME**, P/C 2.70, iv_rank 100, BACKWARDATION surviving hygiene (front ratio 1.457). **Dropped, not traded: earnings tomorrow premarket, the same morning as NFP.** Pure event risk. Fundamentals-gate CONFIRMED the bearish positioning is justified (3-of-4 miss streak, revenue −8.32%, **negative gross margin −1.63%**) — but insiders are net *buying* (MSPR +21.76), which is a genuine counter-signal.
- **MU / AMD / PLTR** — the day's cleanest dispersion tell, and it earns zero points. All three carry bearish sweep persistence (**MU 5/5 at $4.58B, AMD 5/5 at $1.96B, PLTR 4/5 at $1.44B**) *inside* Technology, the only sector with a real netted inflow. Sector-level netting is masking single-name distribution in three of the largest-premium sweep books on the tape.

### Sweep ledger (informational — 0 rubric points)

The `sweep-persistence` rubric line was **removed 2026-05-23 P0.3** (marginal contribution −22pp across two consecutive audits, n=15). Persistence is the honest way to rank urgency; it does not score.

| Rank | Ticker | Side | Persistence | 5d cum. premium | Read |
|---|---|---|---|---|---|
| 1 | **MU** | bearish | **5/5** | $4.58B | Heaviest bearish premium in the book, every session this week — actively faded inside a bought sector |
| 2 | **AMD** | bearish | **5/5** | $1.96B | Same pattern despite SMH +6.05% 5d |
| 3 | **PLTR** | bearish | 4/5 | $1.44B | Third straight session inside "bought" Technology |
| 4 | **INTC** | bullish | 4/5 | $609M | Only persistent bullish near-term flow |
| 5 | **NBIS** | bullish | 3/5 (at the floor) | $425M | Thinner than the label implies |

**The bullish sweep flow is concentrated, not broad:** INTC + NBIS ≈ $1.0B against ~$8.0B of bearish persistent premium in MU + AMD + PLTR alone — before counting the index/mega-cap bearish complex (SPXW + SPY + QQQ ≈ $31.4B, filtered as probable hedge flow). This corroborates rather than contradicts the 34.1% bullish flow breadth.

Mega-cap names filtered under the 2026-05-15 P1.1 rule: MSFT, AMZN, AAPL, GOOGL, NVDA, TSLA, IWM all **mixed 5/5** ⇒ disqualified regardless.

**One clarification worth carrying forward:** SNDK's tape was 100% put, but `side=bid` on the $286.79M print means the customer **sold** to the bid — this was aggressive put-**selling**, not a bearish buy-to-open. Read as bearish conviction it would have been exactly backwards. See §7.

---

## 4. LEAP Builds (6–24 months)

**EMPTY — zero qualifying candidates.** LEAP DTE share is **3.5%** of market volume and only 20 names market-wide showed DTE>180 OI growth, of which four passed C12.

| Ticker | Looked like | Gates passed | Failing gate(s) |
|---|---|---|---|
| **TLT** | LEAP call build, DTE 533, $90C, +24,597 OI | **2 of 9** | **Gate 4 (required): `cum_premium_flow_90d` −$170.9M, MIXED.** **Gate 8: `conviction-matrix` = COVERED_CALL, 22.7%** — explicit reject. Gate 1: strike/expiry rotates almost every session (90C→88C→99C→…) = a **rolling call-writing overlay**, not a coherent build. `call_bid_volume` 224,441 > `call_ask_volume` 146,257 — calls sold into strength. Also fights a rising-10Y backdrop |
| **NVDA** | LEAP call build, DTE 315, $260C, +11,909 OI | **1 of 9** | **Gate 4: `cum_premium_flow_90d` −$84.5M against ~$46.1B/$46.2B gross = statistically flat, MIXED.** **Gate 8: `conviction-matrix` MIXED, 7.8%.** The 260C print was **bid-dominant** (15,554 bid vs 5,217 ask) = writing, not buying. Zero DTE>180 contracts in the daily top-10 on any of 10 sessions |
| SLV | LEAP put, DTE 225, +8K OI | — | Put, fails DIRECTIONAL_LONG by construction |
| GLD | LEAP put, DTE 315, +6.7K OI | — | Same |
| CPNG | 27× OI increase, DTE 315 — the biggest raw mover | — | **Fails the C12 liquidity floor**, excluded before gate testing |

Both TLT and NVDA fail on **hard disqualifiers, not close calls.** TLT in particular is the yield-enhancement/financing artifact class the rubric warns about.

---

## 5. Volatility Surface

### The framing that governs everything below

**VRP is negative on both indices** (SPY −0.0041, QQQ −0.0424 — realised exceeds implied). This is a premium-**buying** tape. It is the single most important read today and it contradicts the naive "VIX 15, sell vol" instinct.

### Mandatory substrate hygiene

`scripts/term_structure_hygiene.py` was run over 20 C12-passing liquid names (`min_contracts` 15 — a **named, tunable parameter, not audit-frozen**). **20 of 20 raw labels were BACKWARDATION.** Post-hygiene: 11 BACKWARDATION, 8 KINKED, 1 NO_NEAR_TENOR.

**Critically, `base_shape` is BACKWARDATION on all 19 measurable names with zero base-level flips.** This is *not* 0DTE-bucket noise being scrubbed away — it is a genuine market-wide ~6–8 DTE premium over the 29–30 DTE tenor, consistent with NFP tomorrow plus CPI on 08-12 sitting inside that window for every name simultaneously.

### Two substrate defects worth recording

1. **`iv-percentile-zscore` returned `dates_used: 81` for all 20 names uniformly** — well under the ≥120-day bar. **Every percentile below is PROVISIONAL**, directional colour only, not a calibrated read.
2. **The IV-rank screens are near-useless today.** `iv_rank_high.json` is dominated by sub-$5 and illiquid names (HTZ $2.02, AWRE $1.23, TDUP $3.11, SPWH $1.18, RCON $0.04, ATNM $0.79) plus **null-close synthetic tickers** (`RIOX1`, `ATRO1`, `LCDL`, `HOOX1`, `NVDX1`, `AZUL1`, `AVO1`, `AIV1`, `ABVEF`). `iv_rank_low.json` carries the same synthetics (`BDX1`, `SKHX`, `SKUU`, `SKHU`, `FIRY`). All fail C12 and were dropped rather than ranked around.

### Raw IV rank vs robust percentile diverge hard on semis

| Ticker | Raw iv_rank | Robust ivpz (n=81, provisional) | Regime |
|---|---|---|---|
| MU | 56.6 | **20.99** | NORMAL (near LOW) |
| AMD | 54.1 | **23.46** | NORMAL (near LOW) |
| INTC | 61.4 | **19.75** | **LOW_IV** |
| SOXX / SOXL | 71.3 / 70.6 | 44.44 | NORMAL |
| **AVGO** | 66.0 | **88.89** | **HIGH_IV — opposite direction** |

Raw rank says "moderately elevated" across MU/AMD/INTC/SOXX/SOXL; the outlier-robust read puts most of them in the **bottom half of their own IV history**. With **SMH realised vol at 49.4%**, the semis complex is the sharpest **negative-VRP pocket** in the book: realised hot, implied cheap-to-normal. **AVGO is the exception — already caught up at the 89th percentile; do not buy vol there.**

### Earnings-proximate dislocations

| Ticker | Shape | Base shape | Front ratio (tenors) | ivpz | Term skew | Implied move | Catalyst |
|---|---|---|---|---|---|---|---|
| **FLR** | BACKWARDATION | BACKWARDATION | **1.457** (15/43 DTE, 401 & 366 contracts) | 81.5 | insufficient coverage | **11.59%** | Earnings **08-07 premarket** |
| **SMCI** | BACKWARDATION | BACKWARDATION | 1.291 (8/29, **0 dropped, 17 tenors**) | 80.3 | COMPLACENT 0.997 | **2.97%** | Earnings 08-11 |
| **CRWV** | BACKWARDATION | BACKWARDATION | 1.284 (8/29, **0 dropped, 20 tenors**) | 80.3 | NORMAL 1.039 | **3.70%** | Earnings 08-11 |
| **NBIS** | KINKED (**false positive**) | BACKWARDATION | 1.242 (8/29, 0 dropped) | 71.6 | COMPLACENT 0.998 | **5.10%** | Earnings 08-12 |
| BIRK | BACKWARDATION | BACKWARDATION | **null** — no clean pair (2 tenors kept, 3 dropped <15 contracts) | 60.5 | TAIL_HEDGING 1.393 (533 DTE only) | 11.25% | Earnings 08-13 |
| ENS | **NO_NEAR_TENOR** | unmeasurable | **null** | 69.1 | insufficient | 8.74% (unverifiable) | Earnings 08-12 |

**Three findings that matter:**

- **None of these register as KINKED-at-earnings.** Earnings vol at the true front tenor shows up as smooth BACKWARDATION, not a hump, because the earnings expiry *is* the front tenor.
- **NBIS's KINKED label is a false positive.** `kink_expiry` is **2026-09-18 — five weeks past its 08-12 earnings.** It is a mid-curve hump from a different catalyst, and treating it as the earnings signal is exactly the mistake the hygiene protocol exists to prevent.
- **BIRK and ENS are data-insufficient, not signals.** ENS's earnings-spanning 08-21 tenor has **10 contracts** — below the floor. Per the protocol that is `NO_NEAR_TENOR` = **unmeasurable**, never "flat". A 1.000 ratio there means "no data."

### No calendars fire today

TEAM (1.476), NET (1.451), WDC (1.374) and AMD (1.062) all clear >1.05 with no earnings catalyst and clean multi-tenor data — but front-end backwardation right now is **event-PENDING, not panic-RESOLVING**. There is no same-methodology prior-day ratio to confirm a falling front end, and NFP prints before any of these could resolve. Per the disqualifier rule these are **watch-only**. Re-read `front-end-iv-ratio --near-dte 7 --far-dte 30` post-NFP; a genuine collapse then is the calendar entry.

### Artifacts flagged, not traded

1. **OKTA's "kink"** at 15 DTE (2026-08-21): `avg_iv` **216%** against neighbours at 77% and 87%, prominence **149.4%**. It clears the contract floor (1,254 contracts) but the magnitude is implausible with no imminent earnings — near-certain unweighted-wing contamination.
2. **Recurring monthly-cluster humps:** DELL/AVGO/NBIS all kink at 2026-09-18 (Sept monthly OPEX), CRM/AMD at 08-28, PANW at 09-04, MU at 08-14. None align with an identified earnings date; all sit at standard monthly/OPEX-adjacent expiries where OI depth is structurally higher. Treat as a **monthly-expiry wing-depth artifact class**, not individually scored kinks.
3. **`iv_outliers` has zero overlap with the liquid book** — it returns SPY 751/750/756C and 787P, QQQ 495C, IWM 301P (all 0DTE-adjacent index noise) plus micro-caps that mostly fail C12. No genuine whale-hedge single-contract signal in the liquid names today.

---

## 6. Risk & Correlation

**Macro headline:** curve normal at +0.44, core PCE 3.29% still running hot against core CPI 2.81%, payrolls decelerating to +57k, 10Y 4.63% and **rising**, USD weakening. The tape enters **NFP tomorrow pre-open** with essentially no dealer long-gamma cushion (SPY `total_gex` +$33M; QQQ gamma flipped negative today; SPY put wall 0.11% from spot). Gap risk is live in both directions.

**Breadth cross-check (advisory, `fz`):** 202 advancers / 299 decliners, **`pct_green` 40.16%**, avg −0.50%, median −0.33%, 503 names. Top mover MSI +8.2%, worst HONA −23.16%. **`divergence_flag` FALSE** — the index closed *red* (SPY −0.16%), so sub-50% green is consistent with the tape and is **not** the green-index distribution tell (that flag fires only on green index + sub-50% breadth). The informative cross-read is against UW options-flow breadth at **34.1% bullish**: the options tape is materially more bearish than the cash tape. Advisory, 0 rubric points.

### Correlation clusters (`uw risk portfolio-correlation`, 11 candidates, 30d)

One giant AI-infra/semis complex — **10 pairs ≥ 0.70**:

- **Semis/memory:** SNDK/MU **0.896**, SNDK/AMD 0.890, MU/INTC 0.884, AMD/INTC 0.867, TSM/INTC 0.866, SNDK/INTC 0.863, TSM/AMD 0.859, MU/AMD 0.839. **SNDK, MU, AMD, TSM and INTC are one bet.**
- **AI neocloud:** **CRWV/NBIS 0.876.**
- Oddity worth noting: **FLR/MU 0.816** — AI-datacenter capex beta bleeding into an E&C name.

No cluster deduction fired mechanically, because CRWV was the only sized candidate and is the highest-scored member of its cluster; every other member was already DROP or watch-only. Had a second semis name passed the floor it would have taken an automatic −1. Sector metadata returned "Unknown" ×11 (upstream gap), so the concentration read was done off the netted rotation instead.

### The panic gate fired mechanically

`uw options-structure front-end-iv-ratio`: **SPY 1.121 > 1.10** (near IV 17.08 vs 29d 15.24), QQQ **1.233**, both BACKWARDATION. The rule admits no exceptions, so **everything reduces one tier.**

Colour that does *not* soften the gate: `near_dte_actual = 1`, and the near tenor **is the NFP expiry** — so this is event premium, not fear, and VIX fell 4.2% today. The 2026-05-15 audit specifically killed this kind of discretionary non-fire, so the cut stands as written.

### Fundamentals verdicts (top-5)

| Ticker | Verdict | Tier adj | Driver | Next earnings | Days |
|---|---|---|---|---|---|
| **CRWV** | **CONFIRM** | 0 | 08-11 date confirmed. Miss streak (3/4: −22.31%, −11.20%, +78.72%, −25.70%) and insider MSPR −60.9 **corroborate** a vol thesis rather than contradict it. Carried risks: net margin −25.57%, ROE −40.33%, **D/E ~648% scale-corrected**, `current_ratio` **0.4555** | **2026-08-11** | **5** |
| **MSFT** | CAUTION | −1 | Insider **MSPR −83.89**, **4 of last 6 months at −100** — the heaviest in the group. `distribution_flag` on the exact ATM anchor strike. DP accumulation closing-cross-inflated. RSI **78.11** after +24.6% in a month. Fundamentals alone would CONFIRM (rev +17.79%, EPS +31.56%, net margin 40.31%, D/E 0.24) | 2026-10-27 | 82 |
| **FLR** | CONFIRM | 0 | 08-07 premarket confirmed. Genuine 3/4 miss streak, revenue −8.32%, **negative gross margin −1.63%** — the z=+3.14 put positioning is fundamentally justified. Counter-signal: insider **buying** +21.76 | **2026-08-07** | **1** |
| **META** | CAUTION | −1 | The `beat_streak` label masks a **−16.03% EPS miss last quarter — the largest surprise either direction in four quarters.** **EPS growth −3.69% YoY against revenue +27.65%** (AI capex margin compression). Insider MSPR −22.63. Same-day AI-safety incident headline; stock already in a down move | 2026-10-27 | 82 |
| **NBIS** | CAUTION | −1 | **Earnings 08-12 = CPI day.** Insider MSPR −73.42. **Burry disclosed a new short today**; "data center plans pushback" headline. Operating margin −70.55% masked by a likely one-off net margin of 93.09%; PS 104×. Counterweight: 4/4 beats and **30.22% short float / 3.1 DTC** = real squeeze risk against any short | **2026-08-12** | **6** |

**No VETOs** — no name cleared the ≥2-of-3 Finnhub contradiction bar. All three CAUTIONs are driven primarily by the insider leg, which returned **live, non-NA data** this run. `recom` and `upside_to_target_pct` are **null for all five** — a confirmed `fz` upstream gap, so the **analyst axis is NA**, not absent-by-choice.

### Debate-disconfirmation cuts

| Ticker | bull | bear | Verdict |
|---|---|---|---|
| **CRWV** | **0.35** | **0.75** | **−1 tier** |
| MSFT | 0.35 | 0.75 | −1 tier (moot — already DROP) |
| META | 0.25 | 0.75 | −1 tier (moot — already DROP) |

**All three bull residuals landed far below the 0.69–0.75 historical baseline**, and each conceded its own case substantially. Single round; no escalation (residuals nowhere near within one bin at ≥0.75).

The three bear findings worth carrying forward:

- **CRWV** — `uw historical vrp --symbol CRWV` returns realised 30d **122.38%** against IV30 **104.55%**: **VRP −0.1784, PREMIUM_BUYING**. CRWV has been gapping **+21.5%, +19.5%, −11.4%, −9.6%, −5.1%** on ordinary flow with no catalyst. The flat `term_skew` is therefore explained by an **already-elevated whole curve**, not a binary-event blind spot — which means the +1 front-end and +1 term-skew components are partly **the same fact counted twice**.
- **MSFT** — the bull's "four independent sources" collapse to **one set of option prints described four times**. The $62.4M-modelled-vs-$58.1M-reported "7% match" is near-tautological: the model derives its debit from the same legs that generate the reported net premium. And if a desk were opening 17,130 fresh Oct C500s, OI on that strike should **build**, not contract by 3,431.
- **META** — Comm Services is netted-IN by **2.9% of gross**, materially the same ratio (**2.4%**) that got SNDK's +1 revoked *in this same run*. The +$477M has **never been intent-screened** for put-selling or overwriting — the exact failure mode that produced the SNDK artifact.

### Adverse-flow exit list

Rolling group `conviction_2026-08-05` = **ZTS**.

- **ZTS — exit-watch (adverse flow, moderate).** Today: flow direction **bearish** (net −$0.19M), P/C **1.30**, **2.7× volume spike**, a $9.5M single DP print (484 DP trades, $161M notional), OI +11,787. Day-flow direction opposes the carried thesis, but dollar magnitude is small ⇒ **monitor/tighten, not a hard exit.** `fz` drift tripwire is cold-start (1 snapshot) and was skipped per protocol; drift coverage begins tomorrow.
- Wider stale-conviction sweep: **NVDA bearish (−$15.9M)** and **TSM bearish (−$15.4M)** — consistent with today's TSM flow_conflict kill. Older conviction groups holding these names should not be refreshed.

### Hedge sleeve

Book directional skew is **undefined — zero sized positions** — so no mechanical net-delta hedge triggers. Advisory overlay for any external long beta carried into NFP:

- **Follow the tape's most persistent institutional theme.** The **VIX Oct-21 C20/C30 call spread** (59,392 × 58,167 lots, ~$9.2M debit) sits on top of an Aug-19 and Sep-16 call-spread complex that **also ran on 08-05**. Institutions keep buying Sep/Oct VIX upside while VIX sits at 15.15 and the front end stays complacent — this is the single most persistent multi-day multileg theme in the tape and it flatly contradicts the calm surface. Long convexity at ~15 VIX, with negative index VRP, a drained SPY gamma cushion and QQQ gamma freshly negative, is the aligned structure: defined risk, cheap carry.
- **Shorter-dated alternative:** a SPY Aug-21 put vertical struck around the **768 put wall** (0.11% from spot) — defined-risk, monetises a break of the wall into the macro gauntlet.
- The §2a override stands: **stand aside** on tomorrow's 0DTE premium-selling lane.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**EMPTY. No name reached MEDIUM (raw_score ≥ 7).** The highest raw score on the board was **3**.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no per-tier expectancy row is printed today because no tier has a sized position, and the most recent `/calibration-audit` (2026-08-01) recorded **zero post-freeze HIGH/MEDIUM** calls for the sixth consecutive cycle. The standing per-tier read from that audit remains: **DROP 0.431 > LOW 0.402 > sized 0.386** — the empty-board discipline continues to be graded correct rather than merely defensible.

### The one name that reached Phase 2d

**CRWV — raw_score 3, LOW, `vol_long`, `earnings_vol` → final size `watch_only`.**

| Component | Points | Source | Evidence |
|---|---|---|---|
| earnings-scout BUY VOL | +1 | `uw options-structure front-end-iv-ratio` | Earnings 08-11 (5 sessions). `front_end_ratio` **1.284** (8 vs 29 DTE, **20-tenor chain, 0 dropped** post-hygiene), `base_shape` BACKWARDATION, `term_skew` NORMAL 1.039 (tail not priced), `implied_move_pct` **3.70**. Flow bullish and the day's dollar leader (+$10.8M net: $37.35M bull vs $26.56M bear) |
| vol-surface BACKWARDATION, VRP-aligned | +1 | `uw options-structure term-skew` | Post-hygiene BACKWARDATION; index VRP negative both sides aligns with a long-vol bias. `ivpz` 80.3 **PROVISIONAL** (`dates_used: 81`). **C13 tension surfaced, not silently resolved:** this and the earnings-scout line are correlated reads of the same front-end richness |
| oi-trend BUILDING | +1 | `uw historical oi-trend` | 82 consecutive build days; net OI +14,004 today. **C47 caveat: this line fired 16-of-16 on 2026-07-24 — zero discrimination** |

`win_rate` **null**, `win_rate_source` **`NA(substrate)`**, `market_excess` null, `cum_premium_flow_30d` +$92.1M (only **3.1% of $2.96B gross**, tool label MIXED), `implied_move` 3.70, `dp_block_to_float_ratio` null (not a DP row), `insider_cluster_flag` null (never evaluated), `debate_residuals` {bull 0.35, bear 0.75}, `fundamentals_verdict` CONFIRM.

**`gate_verdicts` (all 9 keys):** `regime` no-op · `vrp` no-op, supportive · **`panic` −1 tier** (SPY 1.121 > 1.10) · `cluster` no-op (kept member, CRWV/NBIS 0.876) · `sector` no-op (Technology netted-IN) · `fundamentals` CONFIRM, no-op · `event_risk` no-op via exemption (the trade *is* the earnings-vol event play, though NFP T+1 and CPI T+4 are named in-horizon binaries) · **`debate` −1 tier** (bear 0.75 ≥ bull 0.35) · `rubric_regime` capped half (OUT-OF-REGIME; moot at starter).

**Disposition, stated explicitly rather than left unchanged:** pre-risk `starter` → panic −1 → `skip` → debate −1 → floored at `skip` → **routed to `watch_only`**.

**Why this is the right kill.** A raw-3 LOW with no win-rate substrate at all (`uw historical signal-backtest` has **no `earnings_vol` class** — the enum is only `bullish_flow`, `bearish_flow`, `high_iv_rank`, `volume_spike`, `dark_pool_accumulation`), one component that fired 16-of-16 with zero discrimination, a second component the bear showed is partially double-counted with the first, and a 0.35 bull residual. The class itself realises **0.449 on n=78** and has been a BH-surviving over-claimer for 4–5 consecutive audits — which is why the 2026-08-01 audit imposed the 0.55 ceiling. Even setting the mechanical panic fire aside, the debate gate alone kills it from the starter floor. Long CRWV vol is *directionally sympathetic* with the negative-VRP regime; anyone wanting that exposure gets it cleaner through the index/VIX hedge sleeve than through a single name that must survive **NFP (T+1) → its own print (T+3) → CPI (T+4)** back-to-back at 104% IV.

### The day's most important correction: SNDK

**The +$388M "top bullish net premium" headline is one ticket, and it is a put SALE.**

`SNDK 2027-01-15 P1660`, 5,000 lots at $573, **bid side**, $286.50M — **74% of the entire net**, executed 15:17:35Z. SNDK appears **nowhere** in the multileg top-120, and there is no second SNDK leg anywhere in top-premium or the greek screener.

- **Not** the un-split parity artifact: spot 1258.58, intrinsic ~$347–401 against a $573 price — $172–226 of real extrinsic.
- **Not** the 20:00Z closing-cross artifact: it printed at 11:17 ET.
- It is a **bid-side deep-ITM put sale** — short vol / synthetic long. **UW's netting convention books put sales as bullish premium**, which is the entire source of the headline.

Term structure is BACKWARDATION with no kink, the whole curve sits above 100% IV, **rv20 is 156.3%**, and the stock fell **6.81% today** and is down **46.1%** over the lookback. Somebody monetised panic vol at 103% IV.

The contamination reaches the 30-day figure too. `cum_premium_flow_30d` decomposes to `cumulative_bullish` **$27.680B** vs `cumulative_bearish` **$26.363B** — a net **+$1.317B on $54.0B gross, a 2.4% imbalance**, with the tool's own label reading **MIXED**. Today's single put sale is **21.8% of the entire 30-day net**. A name down 46% with 156% realised vol is exactly where systematic put-selling and overwriting concentrate, and every such sale books as "bullish premium."

**Ruling: sector-rotation's +1 on SNDK is revoked, not merely discounted.** Proposed for the audit register as a **new artifact class — put-sale netting inflation of `cumulative-premium-flow` in collapsed high-IV names** — the third member of the "premium counted without intent classification" family, alongside the dividend-capture and merger-arb blind spots.

### Other structures screened and rejected

| Ticker | Shape | Why it is not a trade |
|---|---|---|
| **TLT** | Aug-14 C76/C77 33,600×2 and Aug-17 C76/C77 32,400×2 — large, repeating, C12-passing, perfectly equal size | Leg prices differ by **exactly the $1.00 strike width** ($0.997 / $0.994). Spot 82.52 leaves $0.36 and **$0.08** of extrinsic on a 1-point deep-ITM spread. A spread at 100% of max value has zero optionality; no rational buyer exists. **Financing / early-exercise-arb family** — and repeating a financing trade is still a financing trade |
| **EWZ** | Dec-18 C34/C35/C45/C46 at 51,575 lots each (one 4-leg order), repeating from 08-04 | Geometry certain, **sign unresolvable**. A long condor books +$2.4M; a short-body version books −$33.0M against a reported −$29.4M — the arithmetic favours the **bearish/overwrite** reading, opposite to `confluence_bullish EWZ(5)`. The 71–134 DTE hump is genuine (Brazilian October election), but direction is not recoverable |
| **GLD** | Sep-18 C410 (57,773) / C430 (60,454) | The 410 leg printed **bid side** (55,292 @ 6.54) — it was **sold**. This is a **short** call spread, a rolling overwrite ladder repeating from 08-05, skipping the 08-12 CPI kink. Carry/vol-harvest against long bullion, not a directional bet |
| **ET** | Aug-21 C20 at $0.694 vs $0.67 intrinsic; Jan-2028 C15 at $6.138 vs $5.67 intrinsic | **2.4 cents of extrinsic at 15 DTE**; $0.47 on a 533-day option. Both implausible. Shaped like a diagonal, priced like an assignment/distribution arb in ET's early-August ex-date window |
| **SPCX** | Aug-07 P115 / P120, 1 DTE into NFP | Internally inconsistent — spot 114.88 puts the spread at $5.00 intrinsic while the legs imply $3.31; `ml` ratio only 0.63/0.83; the put shape contradicts SPCX's own +$40M bullish net premium |
| **SPX / SPXW** | Four legs at one timestamp, all size 1,300, deep-ITM European | **Box-family financing.** Gamma ~0.0001, all near parity. SPXW additionally printed the identical $1737.27 four times across different lot sizes — a stale-price fragment |

### Structures outside the C12 funnel, noted for context

- **IGV Aug-21 C100 / Nov-20 C100**, 20,040 / 20,003, dead ATM (spot 99.42), ~$9.37M debit — the cleanest calendar of the day. But front IV 0.3385 vs back 0.3487 = **CONTANGO at the calendar's own tenors** with no qualifying kink ⇒ vol-mispricing/theta harvest, **not** an event play.
- **XLE Oct-16 P55 (20,114) / C60 (20,002)** — equal-size risk reversal, short put / long call, bullish energy on the day XLE led the tape. Sits at 71 DTE, past the Sep-18 kink.

### Conviction scoring rubric (Step 4, verbatim — rubric_version `2026-06-12`, FROZEN)

```
Daily conviction score = Σ:
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna-squeeze setup in trade direction —
      the trigger must be a verified SIGN CHANGE, not a level: sign(net_dex) on the latest session opposite to
      ≥3 consecutive prior sessions, read from dated `uw options-structure dex --date` calls, with |net_dex| on
      the flip day ≥ 0.25× the trailing-10-session median |net_dex|; evidence must cite both dated values.
      Compute with `python3 scripts/dex_flip.py` — do NOT do the arithmetic by hand. Vanna disjunct additionally
      requires a dated VIX source for the falling-VIX leg.   # DEMOTED +3→+1 and MECHANIZED 2026-06-12 P0.4
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified institutional-tier
      confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms (sign aligned AND
      |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: award only when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts (marginal contribution −23pp on swing).
  +1  uw historical cumulative-premium-flow shows net directional accretion in trade direction (30d) —
      INTENT-SCREENED (P1.4): award only when (a) no C28 distribution_flag on the name, AND (b) on dividend payers
      inside an ex-div window, the accreting prints are NOT deep-ITM sub-parity calls. Screen failed → 0.
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector — CONDITIONAL:
      (a) sector persistence_score ≥ 0.6 AND (b) cum_flow_30d direction aligned AND (c) |cum_flow_30d| ≥ $50M.
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising pc-ratio-zscore (VRP positive) — an INFORMED-FLOW
      CONTINUATION penalty, not "the crowd is wrong, fade it". Single-name P/C extremes predict continuation
      (Pan-Poteshman 2006; Ge-Lin-Pearson 2016). "Rising" needs a multi-date z trajectory.
  -3  flow_conflict — cum_premium_flow 30d direction clearly opposite dominant_signal_class (sign flip +
      magnitude > today's union-median |cum_flow_30d|, or explicit OPPOSITE label)
  -1  flow_conflict_lite — 30d cum flow read is MIXED. Mutually exclusive with flow_conflict — apply ONE.
  # TIER GATES (2d) — contribute 0 to raw_score, never appear in score_components:
  -1  [TIER GATE] risk-monitor correlation cluster (pairwise corr ≥ 0.70) — −1 TIER
  -3  [TIER GATE] uw risk market-regime conflicts with trade direction — −1 TIER
  # REMOVED: signal-confluence ≥4 (+2, removed 2026-06-12 P0.2 — server-side re-count of already-scored
  #   quantities); sweep-persistence top-5 (+1, removed 2026-05-23 P0.3 — MC −22pp two consecutive audits);
  #   gamma-flip 0DTE breakout (+2, removed 2026-05-09 — NO-INFO on swing horizon).
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | HIGH | full (subject to the 3-of-4 load-bearing-tool gate + win-rate gate) |
| 7 – 8 | MEDIUM | half (subject to win-rate gate) |
| 3 – 6 | LOW | starter / watch-only |
| ≤ 2 | drop | filtered by the quant's drop floor |

**Tier-cut status:** the ≥9 HIGH cut failed its scheduled re-confirmation on 2026-06-12 (bands inverted on the first post-UPTREND window: HIGH 0.222 / MED 0.214 / LOW 0.444). The cuts are retained under the P0.1 freeze but carry **no validated ranking claim**; the P0.6 out-of-regime guard caps all sizing at half in the interim.

---

## 8. Watch-only — single signal, no confluence

Listed for journaling. **Not for trade entry today.** Per the corrected 2026-07-23 write-back rule, **none of these were written to the watchlist** — DROP names poison the correlation loop.

| Ticker | Single flag | Why it stayed here |
|---|---|---|
| **MSFT** | multileg +2 (the day's cleanest structure) | Strongest name on this list. Accumulation-hunter named-and-excluded it; the exclusion is evidentially *negative*, not neutral. Re-check tomorrow: if accumulation cleans up ex-closing-cross or the block tier flips buy-side, it clears the gate with the +2 already banked |
| **TSM** | multileg +2 (reduced) | −3 flow_conflict at 1.17× union median. Structure reads as overwrite/yield, not length — flow read and structure read agree against the bullish label |
| **SNDK** | sector +1 — **REVOKED** | Put-sale netting artifact. Direction genuinely unresolved: the put tape is put-*selling* (a vol-short / synthetic-long expression) on a stock down 46% with 156% realised vol |
| **META** | sector +1 (clean on the letter of the rule) | Single flag, contested by bearish 4/5 sweep persistence ($972M) and a same-day Tier-1 `FLOOR_PUT_BLOCK`. Its 2.9% net-of-gross is close to the 2.4% that revoked SNDK. Re-check tomorrow |
| **NBIS** | conflicting across four agents | Bullish sweeps at the 3/5 floor vs bearish premium-weighted flow vs a DEX near-miss at 0.87× vs an artifact-caveated vol read. Scores 1 |
| **FLR** | gate-passed (2 flags) but raw 2 | Below the drop floor. `oi-trend` NOT building (net OI −1,717) was the mechanical discriminator against CRWV — **the first time in weeks that line has discriminated anything** |
| **MU / AMD / PLTR** | sweep persistence (0 points) | The day's best dispersion tell, but single-agent and unscoreable. Any directional short routes `watch_only` regardless |
| **TXRH** | contrarian watch_only | Short-continuation, not a fade. Short routing applies |
| **SMCI** | vol-surface buy-vol | earnings-scout SKIPped it — premium-weighted flow is net **bearish** ($16.6M vs $10.4M) despite call-heavy ticket count, so the "flow aligns" leg fails |
| **INTC** | sweep bullish 4/5 | Single flag. Robust ivpz **19.75 = LOW_IV** against a raw iv_rank of 61.4 |
| **AMZN** | accumulation named-and-excluded | `conviction-matrix` COVERED_CALL 16.1%; `cum_flow_30d` −$16.8M (wrong sign **and** sub-$50M); `distribution_flag` present |
| **AAPL** | contrarian pre-crossing watch | z −1.702, bullish-aligned price+flow while absorbing a same-day Tier-1 `OPENING_PUT_PRIME` (DTE 4, size/OI 8.55×). Pair with META for tomorrow's re-check |

**AAPL and META are the two names to re-check tomorrow for a crossing into BULLISH_EXTREME** — both run bullish-aligned price and flow while absorbing same-day Tier-1 institutional puts, which is the pre-crossing pattern. Note a real tooling gap: **this build of `pc-ratio-zscore` has no `--date` flag**, so no multi-day trajectory was obtainable. Levels are reported as NORMAL, explicitly **not** as "rising."

---

## Appendix — substrate notes for the next `/calibration-audit`

Four items surfaced today that the audit should pick up:

1. **`uw historical signal-backtest` supports only 5 classes** — `bullish_flow`, `bearish_flow`, `high_iv_rank`, `volume_spike`, `dark_pool_accumulation`. **`earnings_vol` is not backtestable at all**, so the clean protocol structurally cannot complete for it. This retroactively raises the question of where prior `earnings_vol` win-rate quotes originated.
2. **`uw historical iv-percentile-zscore` returned `dates_used: 81` uniformly** across all 20 names against a `--lookback-days 252` request — under the ≥120-day bar. Every percentile in today's fleet output is PROVISIONAL.
3. **New artifact class proposed: put-sale netting inflation of `cumulative-premium-flow`** in collapsed high-IV names (the SNDK case above). Sibling of the dividend-capture and merger-arb blind spots.
4. **The `fz` doubled-first-letter emitter bug is live** on the `screen` lanes (`AABEO`→ABEO, `PPAYS`→PAYS, `IIOVA`→IOVA, `AAMLX`→AMLX). The deterministic inverse was verified against the `Company` field and repaired names were carried as advisory only. **`fz breadth`, `fz insider-clusters` and single-ticker `fz_enrich` lookups were unaffected this run** — the defect is in the screen emitter specifically. Separately, `recom` / `upside_to_target_pct` returned null for all five fundamentals-gate names (confirmed upstream quote-grid gap, blocking C17).
