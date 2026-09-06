# Daily Market Analysis — 2026-08-25

## Executive Summary

- **Regime + GEX state:** `TRANSITIONAL` (trend UPTREND) — SPY 765.91 (+0.32%), above 20d/50d SMA, −1.73% from the 90d high. **SPY sits almost exactly on its own gamma flip** (spot 765.69 vs call wall 766, +0.04%); QQQ 710.60 is long-gamma with its call wall at 711 (+0.06%). VIX 15.45 (−2.52%), LOW tercile. VRP **FAIR** (+0.0038) — no vol edge either way. **Breadth is the story: SPY/QQQ/IWM all green while equal-weight RSP is −0.07% and only 41.15% of S&P names closed higher (207 adv / 294 dec).** Flow breadth 35.7% bullish. Netted sector lean: Technology +$122.4M / Financials +$31.5M / Comm Services +$27.6M IN, Consumer Cyclical −$21.1M OUT.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** **SPY** — short-gamma by sign (total_gex −$132.6M, the smallest-magnitude negative in 6 sessions), ZGL 332.87 **unreliable**, call wall 766 / put wall 760; sitting *on* the flip, bimodal. **QQQ** — long-gamma (total_gex +$338.9M, a **fresh 1-day flip**), ZGL 719.65 reliable, call wall 711 / put wall 700; compression bias. **The tool's own `regime` label contradicted its `total_gex` sign on both names and was overridden.** Advisory, see §2.
- **Top swing build:** **NONE.** Zero names cleared the `raw_score ≥ 3` drop floor. Top score was EWZ at **2**.
- **Top LEAP candidate:** **NONE.** Empty book — no name reached even 3-of-9 gates.
- **Biggest risk:** **Four Tier-1 binaries detonate in one overnight gap.** Core PCE 2026-08-26 08:30 ET *plus* **NVDA, OKTA and BBWI earnings all in the same session.** Correlation cluster `semis_vol_cluster` = {MU, AMD} at corr 0.834. No book to hedge — **cash is the position.**

> **This is the 35th consecutive empty daily board.** Last sized daily was 2026-07-07. Re-derived by globbing `analyses/daily/*/decision.json` only.

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity."** Trend **UPTREND**. SPY 765.91, above both the 20d (764.80) and 50d (752.75), +3.63% over 30d, −1.73% off the 90d high. Guidance: *"Half position sizes. Favor defined-risk strategies. Iron condors in range."*

**The breadth divergence is the session's defining fact and it is corroborated twice over.** The index tape is green (SPY +0.32%, QQQ +0.62%, IWM +0.42%) while **equal-weight RSP closed −0.07%** and Finviz breadth shows **207 advancers against 294 decliners, 41.15% green, median change −0.24%**. Two instruments from unrelated data lineages say the same thing: this was a **cap-weighted advance on distribution**, not a broad bid. Options flow breadth agrees — 2,239 bullish-flow tickers vs **4,041 bearish** (35.7%).

### Per-index gamma (current-state EOD book, 0–45 DTE)

| Index | Spot | Zero-gamma | ZGL reliable | Total GEX | Regime (derived) | Tool label | Call wall | Put wall |
|---|---|---|---|---|---|---|---|---|
| SPY | 765.69 | 332.87 | **false** (57% off spot) | **−$132.6M** | **NEGATIVE** | POSITIVE ❌ | 766 (+0.04%) | 760 (−0.74%) |
| QQQ | 710.60 | 719.65 | true (1.27%) | **+$338.9M** | **POSITIVE** | NEGATIVE ❌ | 711 (+0.06%) | 700 (−1.49%) |
| IWM | 299.23 | — | — | — | DEX negative, whipsawing | — | — | — |

**Substrate defect confirmed live:** the GEX `regime` label contradicted its own `total_gex` sign on **both** indices, and on **3 of the last 4 SPY sessions**. Every regime read above is derived from the `total_gex` sign plus per-strike structure; the label was discarded.

**DTE volume share:** 0DTE 28.6% · weeklies 29.0% · monthlies 20.6% · LEAPs 3.9%. Regime hint **BALANCED** — no retail-0DTE dominance, no institutional-monthly tilt. LEAP share of 3.9% is thin, consistent with the empty LEAP book.

**VRP (`uw historical vrp`):** SPY **FAIR**, +0.0038 (IV30d 12.72% vs realised 12.34%). Index vol is fairly priced — there is no premium-selling *or* premium-buying tailwind to lean on. Realised 20d: SPY 12.9 · QQQ 21.7 · **SMH 42.4** · GLD 23.4.

### Macro backdrop (`scripts/fred_macro.py`)

Yield curve **normal** (10Y−2Y +47bp) · core CPI **2.79%** YoY · core PCE **3.29%** YoY · unemployment **4.1%** · **July payrolls −23k (contraction)** · 10Y 4.70%, flat over 30d · broad USD **weakening** (−2.51 over 30d) · fed funds 3.63.

**This is genuine stagflationary tension.** Core PCE at 3.29% sits well above target while payrolls are *shrinking*, leaving a **~34bp real policy rate** — thin. There is no comfortable side to tomorrow's print: hot kills the cut, cold confirms the labour contraction.

### Forward event risk (T+0 = 2026-08-25, trading days; Labor Day 09-07 excluded)

| Event | Date | T+N | Impact |
|---|---|---|---|
| **Core PCE (July)** | **2026-08-26 08:30 ET** | **T+1** | **TIER-1 — before the next open** |
| Initial jobless claims | 2026-08-27 | T+2 | Tier-2 |
| Employment Situation / NFP (Aug) | 2026-09-04 | T+8 | TIER-1 (elevated: July printed −23k) |
| CPI (Aug) | 2026-09-11 | T+12 | TIER-1 |
| FOMC + SEP dot plot | 2026-09-15/16 | T+14/15 | TIER-1 |
| Monthly OPEX | 2026-09-18 | T+17 | — |

**A 4-week swing horizon opened today contains every one of them.**

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — built from open interest that persists overnight — read forward as the *prior* for the next session's open. It is **prose-only, contributes 0 points** to the conviction rubric, and makes **no backtested predictive claim**. Scope is SPY and QQQ only.

**SPY — sitting on the flip line, bimodal, low conviction.** Total GEX −$132.6M is genuinely negative but is the *smallest-magnitude* negative reading in six sessions (it was −$1.28B on 08-24) — the book is drifting toward true zero-gamma, not entrenched short. The per-strike grid is violently split: deeply negative gamma packed from **741–765**, then an abrupt, massive positive pocket starting exactly at **766**. Hold above 766 and dealers are locally long gamma (compression, fade pokes above the wall); slip under 765 and price drops into the −$88M to −$251M shelf at 755/760, where the wall turns from magnet into accelerant. **Structure bias:** this is neither a clean pin nor a clean trend setup — a tight-wing iron fly / straddle centred 765–766 captures direction off the print with defined risk, or stand aside (see §2a). ZGL 332.87 is a deep-OTM extrapolation artifact — `zgl_reliable: false`, ignore it and read the sign and the walls.

**QQQ — fresh long-gamma flip, cleaner of the two.** Total GEX +$338.9M is the first clean positive reading since 08-14, reversing a five-session negative stretch (08-18 through 08-24). Note the internal tension: the *reliable* ZGL at 719.65 sits 1.27% **above** spot, which by the naive spot-vs-ZGL heuristic would read short-gamma — but both the `total_gex` sign and the per-strike grid override it. Strikes **707–712** form a dense dominant positive-gamma pocket sitting directly under and at spot, with **711 alone at +$176.9M**, dwarfing everything else in range. Locally, dealers are long gamma exactly where price is. **Structure bias:** compression / mean-reversion into the open, with room to extend toward ZGL ~720 on a push through 711/712; a break down through the 700 shelf flips the thesis.

**Cross-check.** `expiry-heatmap`: the 2026-08-26 expiry carries **$1.47B** total premium (5th largest listed) and the 08-28 weekly **$2.70B** (2nd largest) — near-dated expiries hold real volume share, so this book is not resting on stale OI.

**Mandatory caveats — stated, not buried:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and recomputes both the ZGL and the walls.
- **ZGL reliability.** SPY's is unusable (57% off spot); QQQ's is within tolerance. When unreliable, fall back to the `total_gex` sign plus spot-vs-wall.
- **The gap risk is not hypothetical — it is scheduled.** Core PCE prints 08:30 ET tomorrow, *before* cash open, and can reset both walls before either prior is ever tested live.
- **Tooling limit.** `gex --dte-max 1` errors; the D+1 expiry cannot be isolated. This is the standing 0–45 DTE book as proxy.
- **ETF book**, not the cleaner SPX/NDX index book.
- **The tool's own `regime` label is wrong on both names today** and was overridden by the `total_gex` sign.

### 2a. Next-session 0DTE premium-selling setup — **STAND ASIDE**

The GEX walls above are a map, not a pin (wall-as-magnet backtested NO_GO, as did every directional 0DTE signal). What validated is a delta-neutral **premium-selling** edge. `scripts/zerodte_setup.py` returns `GO_PREMIUM_SELL_INTRADAY` on both indices — **and that verdict should not be acted on tomorrow.**

| | SPY | QQQ |
|---|---|---|
| `sell_premium` / `vol_state` | true / **LOW** | true / **LOW** |
| VIX | 15.45 | 15.45 |
| implied move / expected range | 0.76% / **1.13%** | 1.17% / **1.39%** |
| `size_scalar` | 0.5 | 0.5 |
| suggested structure | wider iron condor, wings ≈ ±1.13% | iron fly / short straddle centred 711.04, wings ≈ ±1.39% |
| rolling backtest (n=60) | win 86.7%, **gross +0.204%**, **net +0.104%** | win 85.0%, **gross +0.333%**, **net +0.233%** |
| worst day (open entry) | −1.40% | −2.453% |
| `mean_pnl_by_vix_state` | LOW **0.11** · MID 0.172 · HIGH 0.331 | LOW **0.201** · MID 0.305 · HIGH 0.493 |

**PnL basis: percent-of-underlying-spot-notional, GROSS.** Not premium-collected, not margin-relative — a "+0.2%/day" figure is tiny in absolute terms. Lead with net.

**Two reasons to stand aside, and the tool flags neither:**
1. **`vol_state` is LOW (VIX 15.45, below the 15.9 tercile bound), and `GO_PREMIUM_SELL_INTRADAY` / `sell_premium: true` are UNCONDITIONAL flags that do not condition on VIX state.** Read the tercile row instead: at LOW VIX, SPY's gross **+0.11%** becomes **≈ +0.01% net** of the 0.1% cost assumption — statistically zero. QQQ's is ≈ +0.10%. The edge lives in the MID/HIGH terciles; it is not present tonight.
2. **The stack's own entry rule says stand aside if it gaps beyond the wings — and the gap is scheduled.** Core PCE at 08:30 ET is a known Tier-1 binary. Selling near-zero-expectancy premium into a scheduled macro print is how a quarter's edge is lost in one morning.

**Promotion bar unchanged:** this lane stays advisory / 0 rubric points permanently until BOTH a vol-shock day enters the sample (the short-vol left tail is currently **UNSAMPLED**) AND net expectancy clears a tail-aware bar. Win-rate is explicitly NOT the promotion metric for a negatively-skewed short-vol strategy. **SPY ≈ SPX** (validated identical); **QQQ is weaker** — the Nasdaq index book is unavailable.

## 2a. Swing Dealer Positioning (1–4 weeks)

**One mechanized DEX sign-flip in the entire universe, and it is marginal.**

| Symbol | DEX flip | Direction | magnitude_ratio | Whipsaw (sign changes/12d) | Vanna squeeze | Swing bias |
|---|---|---|---|---|---|---|
| **META** | **TRUE** | long | **1.01** | **true (4)** | false | **LONG, low-mod** |
| SPY | false | — | — | true (4) | false | NEUTRAL |
| QQQ | false | — | — | false (2) | false | NEUTRAL |
| IWM | false | — | — | false (3) | false (*pressure*, not squeeze) | NEUTRAL |
| MSTR | false | — | — | **true (6)** | false | DISQUALIFIED |
| TSLA | false | — | — | true (5) | false (*pressure*) | DISQUALIFIED |
| SMH | false | — | — | false (2) | false (*pressure*) | DISQUALIFIED |

**META's flip, in full:** six consecutive negative sessions (08-17 −3.179B, 08-18 −6.244B, 08-19 −5.238B, 08-20 −4.729B, 08-21 −2.911B, 08-24 −0.914B) then **08-25 +666,183,761**, against a magnitude floor of 658,203,824 (0.25× the trailing-10 median of 2,632,815,294). It clears by **~1%** — a single re-print erases it. Independently corroborated by `total_gex` flipping on the same days and by a **distributed 50-strike tilt** (negative 507.5–557.5, positive 560+, spot 568.63), so it is not a single-strike artifact.

**Every vanna-squeeze flag is FALSE, and for a mechanical reason.** The dated ^VIX series (08-17 15.19 → 08-18 15.84 → 08-19 14.89 → 08-20 16.01 → 08-21 15.13 → 08-24 15.85 → 08-25 15.45) shows **no ≥3-consecutive-session decline anywhere in the window**. IWM, TSLA and SMH have put-heavy books — the *setup* ingredient — but the falling-VIX leg fails, so they are reclassified **"vanna pressure, not squeeze."** IWM is worth re-checking if VIX starts a clean multi-session decline.

**Worth carrying as context:** SMH's dealer book stayed net-short-hedge (negative DEX) straight through today's +1.65% semis bounce — **the rally got no dealer tailwind.** Context only, 0 points.

The "DEX flips precede price moves" framing (Karsan / SqueezeMetrics) is **practitioner hypothesis, not validated evidence** at this horizon — hedging pressure is intraday-mean-reverting (Baltussen et al. 2021), and a positive DEX *level* in an up-tape ran −7pp excess. This line was demoted +3 → +1 in the 2026-06-12 freeze for exactly that reason.

## 2b. Sector Rotation

**Regime call: `value→growth`, confidence LOW-MEDIUM — a contested, single-sided lean, not a regime shift.**

Only the growth side confirms cleanly. Financials, Consumer Cyclical, Consumer Defensive and Energy all hit netted-vs-gross (or netted-vs-ETF) disagreement and route to **watch_only**.

| Sector | Netted (directional) | Gross today | Persistence | ETF cross-confirm | Verdict |
|---|---|---|---|---|---|
| **Technology** | **+$122.4M** | +$1,770.3M | 0.8 (4/5) | **agree** — SMH +$69.0M/5d, sweep urgency +$21.5M; XLK +$6.2M | **rotating IN** |
| **Comm Services** | **+$27.6M** | +$379.7M | 0.8 (4/5) | **agree** — XLC +$0.7M (small) | **rotating IN** |
| Financial Services | +$31.5M | +$280.8M | **1.0 (5/5)** | **disagree** — XLF **−$14.7M/5d** | watch_only |
| Consumer Cyclical | **−$21.1M** | **+$390.9M** | 0.8 | XLY ~flat, uninformative | watch_only (sign conflict) |
| Consumer Defensive | −$9.9M | +$19.3M | 1.0 | XLP −$0.8M (agrees with netted) | watch_only |
| Energy | −$0.4M | +$49.2M | 1.0 | XOP **−$20.2M/5d**, sweeps −$11.5M | watch_only |

**Two measurement facts you must hold onto:**
1. **`sector-flow-persistence` fired INFLOW on 10 of 11 sectors** at scores 0.8–1.0, with **6 tied at the 1.0 ceiling**. That is near-zero discrimination — it is a *durability filter*, sign-agnostic gross turnover, and it **cannot express direction**. Only the netted `market-regime.sector_rotation` can, and that field is itself a **top-3/bottom-3 truncation** — the middle of the distribution is unobserved.
2. **A direct contradiction:** gross `sector-flow` shows Consumer Cyclical **+$390.9M** while the netted source shows **−$21.1M**. Same sector, same session, opposite signs. The netted source wins; the sector routes to watch_only.

**Named leaders (C12-passing):** Technology — NVDA (+$33.1M), AMD (+$32.4M), MSTR (+$19.9M), MU (+$17.3M), APP (+$17.1M). Comm Services — GOOG (+$8.0M), META (+$5.9M).

**The flow read and the price tape disagree, and the price tape has more sessions behind it.** Today's netted Technology inflow is **one session** against a five-day rotation running the other way: **XLB +3.48, XLV +3.28, XLC +2.44, XLRE +1.64, GLD +7.41** versus **XLI −2.82, XLE −2.54, SMH −2.45, XLK −2.09, XLU −1.61.** Today's SMH +1.65 / XLK +0.94 is a one-day reversal of a week-long *defensive* rotation, on 41% breadth. Read the Technology inflow as **flow into weakness / early accumulation**, not confirmed momentum — and note it is exactly what a stagflationary macro (core PCE 3.29% vs payrolls −23k) argues against.

### ETF flow tape (advisory — 0 rubric points; 33 `uw` calls, cap 40)

| ETF | Net premium dir (5d) | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|
| SMH | **+$69.0M BULLISH** | — | **+$21.5M bullish** | agree (Tech) | NVDA, AMD, MU |
| XLK | +$6.2M BULLISH | — | +$0.2M ~flat | agree (Tech) | NVDA, AMD, MSTR, APP |
| XLC | +$0.7M BULLISH | — | rank-only | agree (Comm Svc) | GOOG, META |
| XLF | **−$14.7M BEARISH** | — | −$0.2M | **disagree** | — |
| XOP | **−$20.2M BEARISH** | prints sold below mid | **−$11.5M bearish** | disagree (Energy) | — |
| GDX | **−$27.3M BEARISH** | mixed-sign | −$6.75M bearish | n/a (netted silent) | — |

Cleanest independent bearish instrument reads are **XOP** and **GDX** — both route to context only, never a sized short. **Appendix note:** Healthcare shows gross persistence 1.0 and the **2nd-best 5d price tape (+3.28%)**, with an orthogonal `fz` RS/new-high cluster (13 of 16 names healthcare/biotech) — but XLV (−$1.9M) and XBI (−$12.8M) do **not** confirm options-flow accumulation. That is a price/breadth story, not a flow rotation.

---

## 3. Swing Setups (1–6 weeks)

**Nothing is sized. All eight names that cleared the confluence gate scored below the `raw_score ≥ 3` drop floor.** The theses below are carried in full — they are generated, scored, gate-verdicted and serialized so the counterfactual keeps resolving.

| Ticker | Score | Tier | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|---|
| EWZ | **2** | DROP | Nov-20 institutional call ladder into a genuine term-structure hump | financed bull call spread + ATM put | loses the Nov-20 hump / OI unwinds | **skip** |
| NVDA | 1 | DROP | 08-28 230C/240C bull spread into earnings-week backwardation | 3-DTE vertical | **fails 208.48 (08-24 low)** | **skip** |
| META | 1 | DROP | Only mechanized DEX sign-flip in the universe | swing long | **loses the $563–565 DP shelf** | **skip** |
| MU | 1 | DROP | Underpriced semis vol, IV 64.7% vs RV 97.7% | long strangle / calendar | VRP flips positive | **skip** |
| ZS | 1 | DROP | Sell vol into the 09-03 print | iron condor ±17.6% | VRP compresses pre-print | **skip** |
| AMD | 0 | DROP | Cheap vol into NFP | long straddle | base curve steepens | **skip** |
| OKTA | 0 | DROP | Front-panic calendar, earnings T+1 | 8/28–9/04 calendar | panic resolves pre-print | **skip** |
| BBWI | **−1** | DROP | Bearish continuation, pc-z +6.728 | *see §3b* | reclaims $19 | **watch_only** |

### 3a. Long swings (regime-aligned)

**EWZ — the board's top score, and the one whose evidence changed most under scrutiny.** `multileg-strategist` found the session's strongest term-structure-anchored structure: a 2026-11-20 (87 DTE) call ladder across 41C/43C/45C/46C at multileg_ratio 0.99–1.00, repeating from 08-24 (43C printed $2.16M then, escalating today), with the cleaned IV curve running 52d 36.4% → **87d 39.3% at the target expiry** → 115d 37.4% — a genuine local hump centred exactly on the expiry being bought. The 43C leg converted **37,288 of 37,439 volume into open interest (99.6%)** — the cleanest opening flow anywhere in a tape where 126 of 163 single-leg signals are *closing*. The 10-day tape is the strongest of any name reviewed: **+5.97%, 7 of 10 bullish flow days**, with the two largest net-flow days being the two most recent.

**Then the quant re-read the book, and the headline inverted.** Phase 1 described a *"500,000-contract $31.5M ask-side block."* `uw oi biggest-increases` shows that strike at **volume 37,439, prev_ask 8,788 vs prev_bid 22,193 — bid-dominant 2.5:1**, avg $0.58, ≈$2.16M premium. The two tools disagree **~14× on volume and ~15× on premium at the same strike, and neither has been adjudicated.** The full Nov-20 book reads: 38C/41C/42C **bought**, 43C/44C **sold**, and **35P +16,759 bought at $7.04M — the largest single premium line in the name, at the money against a $35.88 spot.** That is a financed bull spread needing **+19.8%** to reach max value, with a large protective put alongside — not unhedged conviction. The bull conceded this outright.

**META — the only mechanized dealer flip, on a name that is genuinely bottoming.** DEX flipped after six negative sessions, corroborated by `total_gex` and a distributed 50-strike tilt. The OI build is direction-verified bullish: **94.3% call share** (+21,567 call vs +1,309 put) at 68–95% OI conversion. And the tape supports the *timing*: META fell 594.97 → 543.67 (−8.6%) into 08-18 on a −$124.4M capitulation day, then printed **four consecutive higher closes** (549.90 → 559.02 → 570.05, +4.85% off the low). This flip lands on a recovering name, not a falling knife. **Against it:** magnitude_ratio 1.01, whipsaw true (4 sign changes in 12 sessions), and **FER@7 = 1.186 — already past the 1.10 invalidation threshold before initiation, with no catalyst to explain it** (earnings 63–71 days out). `accumulation-hunter` did *not* clear it (conviction-matrix 19.9%), and its DP evidence is contaminated — the top bucket ($570.05) is **34.8% of the day's $1.261B DP premium and was excluded as the closing cross**; the "second-tier shelf" at $559.02 is a lone $22.7M block, so the credible defended zone is **$563–565**. Fundamentals: the most recent print **missed by −16.03%**, EPS growth is **−3.69% YoY** despite +27.65% revenue, and there is no name-specific catalyst.

**NVDA — the fundamentals are strong and the trade is still wrong.** Revenue +70.68% YoY, EPS +110.34%, gross margin 74.15%, debt/equity 0.05, 4-of-4 beat streak. `multileg-strategist` inferred an 08-28 230C/240C bull call spread anchored to clean earnings-week backwardation (84.3% at 3DTE → ~41% at 52d, confirmed genuine by the hygiene module). Technology is the largest netted sector inflow and NVDA is its top single name at +$33.1M.

**Everything else points the other way, from four independent directions:**
- **Per-leg side data inverts the thesis.** The named strike itself — 08-28 230C — printed +13,071 OI on volume 53,799 with **ask 22,717 vs bid 28,646: sold, not bought.** Same bid-side pattern on 08-28 215C, 09-04 220C (3.3:1) and 08-31 215C (3.3:1). Against that: 08-28 170P ask 9.1:1 bought, and **2027-01-15 180P +98,465 OI on volume 101,992, ask 100,728 vs bid 1,221 — an 82:1 ask-skew, $77.4M deep-OTM put purchase, the single largest directional commitment in the name.** The two largest OI changes in NVDA today are *both puts*.
- **The "event hedge" reading does not survive the tenor.** The fundamentals gate judged the protective positioning to be event-risk hedging into a known binary. But nobody hedges a *tomorrow* binary with **143-day** options — theta and vega on a 2027-01 put barely move on an earnings gap. That is a structural position, not an event hedge.
- **Three independent tools return one word.** `leap-positioning-radar`: 90d cum-flow MIXED at −$139.5M; `institutional-accumulation` = **DISTRIBUTION** (DP buy_ratio 0.316, $28.7M sold vs $13.3M bought); `conviction-matrix` = **DISTRIBUTION, 18.4%**.
- **The tape.** NVDA is in a clean **10-day downtrend: 224.09 → 213.05 (−4.93%)** with an unbroken lower-high sequence (225.30, 225.16, 225.01, 219.74, 217.56, 216.85, 214.72, 208.48). Today's +4.57 is the first up day in five, and 08-24 printed **−$115.9M**, the largest single-day outflow in the window — one session before the print. *No Phase 1 agent surfaced this; it came out of the Step 6 deep dive.*

**And the timing is the worst on the board: NVDA earnings 2026-08-26 — confirmed independently by `uw` and Finnhub — in the same session as Core PCE at 08:30 ET.** A 3-DTE spread must clear both in one gap.

**Sweeps (informational — 0 rubric points).** Persistence-ranked, the 5-day board is dominated by index/mega-cap **hedge flow**: SPXW, QQQ, SPY, TSLA, NVDA, SPX all at 5/5 sessions but with `cum_flow_30d` MIXED or contradicting, so all are demoted to footnotes. Only two names cleared persistent + opening + near-term: **SPCX** and **TSLA** floor put blocks. **A caution on SPCX** — the $11.35M FLOOR_PUT_BLOCK is strike 180 against a spot of 138.49, delta −0.935, 3 DTE. **Intrinsic value is $11.21M of an $11.35M premium: extrinsic is $0.15M, 1.28%.** That is a deep-ITM synthetic-short / financing structure, very likely one leg of a conversion — not a directional conviction ticket. **EWZ** is the standout single-day print: `smart-money-flow`'s #1 and #2 lines are both EWZ calls at ask/bid ratios of **39.9 and 37.7**, among the most lopsided on the board.

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only` (2026-08-01 P0 #1). The section still runs and carries full theses — this is routing, not suppression.**

**BBWI — the best-evidenced idea of the session, and it scored −1.** `contrarian-scanner` was explicit that this is a **bearish continuation, NOT a fade**: pc-ratio-zscore **BEARISH_EXTREME z = +6.728** (P/C 2.913 vs 20d mean 0.638), `price-vs-flow` divergence **false** — price and flow are *aligned* (price −14.9%, flow −$1.82M) — iv_rank **95.3**, volume_ratio **19.67**, `oi decrease-with-volume` **EMPTY** (nothing unwinding; positioning is fresh), backwardation surviving hygiene, and genuine **TAIL_HEDGING skew at 1.383** — one of only 4 names in 22 with a real tail bid. Confluence funnel score 5. 5-day flow at **−38.58% of gross**, the strongest scale-relative directional confirmation on the entire board. It carries the board's **only measured win-rate: 0.5486 on n=144 under the clean protocol**, with market_excess **−0.0486** (date-clustered −0.0262, same sign).

**It scored −1 because the frozen rubric has no line capable of paying a directional short.** Every line that could score a bearish name is a deduction, was removed, is permanently 0-point, is long-only by construction, or requires a structure BBWI lacks. Worse, the `−1 flow_conflict_lite` fired *because BBWI is small*: the bottom-quartile test is union-relative and therefore scale-blind, so a perfectly-aligned 13.7%-of-gross flow on a $10.4M gross book is penalised while NVDA's 0.38%-of-gross churn on $27.6B is not. **The C11 award side has a 5%-of-gross scale floor; the deduction side has none.** Both defects are registered below.

**BBWI also reports tomorrow (2026-08-26), in the same session as Core PCE.**

**Other short-side theses carried, unsized:** **ARGX** — genuine price-vs-flow divergence (price +18.1% vs flow −$2.41M, pc-z +6.717), CONTANGO term structure, but routed outside the contrarian lane as short-continuation material; single agent, failed the confluence gate. **XOP / GDX** — the cleanest independent bearish ETF-instrument reads (XOP −$20.2M/5d with sweeps −$11.5M; GDX −$27.3M/5d), context only.

**A note on the short lane, because the drift is measured.** The 2026-08-22 audit found short-thesis *generation* halved (32.0% → 17.6%, regime-controlled p = 0.0045) while routing compliance stayed perfect. Today's board generated **1 directional short of 8 names (12.5%)** — and the mechanism is now visible: the rubric cannot score a short positively, so shorts fall below the drop floor before the routing rule is ever reached. Over the last 15 sessions the short share is **30 of 146 = 20.5%**, recovering from the trough (08-24 ran 54.5%), but today is below trend on a tape with 41% breadth. **A distribution tape yielding one short candidate is a screen to re-check, not a clean board.**

---

## 4. LEAP Builds (6–24 months)

**Empty book. Zero names reached even 3-of-9 gates, let alone the required 6.**

LEAP share of DTE volume is **3.9%** — thin. `uw oi biggest-increases --min-dte 180` returned 20 rows, of which only **4 touch the C12 universe**, all on NVDA and USO, all **put-side and bid-dominant** (i.e. puts being *sold*). **There is not one ask-side, long-dated call build in the liquid universe today.**

**Disqualifications, with the gate that killed each:**

- **NVDA** — the largest fresh long-dated print (`NVDA270617P00140000`, 296 DTE, +119,850 contracts, $55.0M) is a **deep-OTM put SALE**: `prev_bid_volume` 120,133 vs `prev_ask_volume` **283**. This is the **put-sale netting trap** in its purest form — cum_premium_flow books it as bullish premium. Fails three gates simultaneously: cum-flow 90d **MIXED at −$139.5M**; `institutional-accumulation` = **DISTRIBUTION** (buy_ratio 0.316); `conviction-matrix` = **DISTRIBUTION, 18.4%**.
- **USO** — `oi-trend --days 10` shows `consecutive_build_days: 0` and `net_oi_change −657,179` (OI actually *falling*). Explicit disqualifier. conviction-matrix MIXED, 7.0%.
- **SMCI** — surfaced only via `position-rolls`, never via `biggest-increases`; no fresh DTE>180 entry exists, and balance_ratio 0.316 is well under the 0.7 thesis-intact threshold — closer to a partial unwind than a thesis extension.
- **WOLF, IBIT, TLT, PCT, NKE, AG, HL, MPT, EEM, BEKE** — all fail the C12 liquidity floor and were not re-verified (fail-closed). For the record, WOLF's 388-DTE $35C print is *also* bid-dominant (10,012 vs 12) — calls being **sold**, covered-call flavour.

**Substrate note:** `oi-trend BUILDING` fired **10/10 consecutive days on both NVDA and SMCI**, reconfirming that the raw label carries no discriminating power. Nothing was awarded on it.

---

## 5. Volatility Surface

**Lead with the population statistics — they matter more than any single name.** 31 C12-passing names run through `iv-term-structure` → `scripts/term_structure_hygiene.py` at `min_contracts = 15` (a **named, tunable, NOT audit-frozen** parameter):

| | Raw label | Post-hygiene |
|---|---|---|
| BACKWARDATION | **24 / 31 (77%)** | 14 |
| KINKED | 3 | **12** |
| CONTANGO | 4 | 2 |
| NO_NEAR_TENOR | 0 | **3** (DKS, VICI, DINO — front end **unmeasurable**, not "flat") |

**16 of 31 (52%) flipped** on the kink-aware shape; 8 of 31 flipped on the monotonic base shape. This replicates the audit's degenerate-raw-label finding almost exactly. **`front_end_iv_ratio` at `--near-dte 7` fired >1.05 on 19 of 22 measurable names (86%)** — near-zero standalone discrimination; the >1.10 disqualifier fired on 18 of 22 (82%). Every `iv-percentile-zscore` read returned **`dates_used: 94` against a 252-day request** — below the 120-day floor, so all are **PROVISIONAL**.

**The single most important finding in this section is that the kinks are macro, not idiosyncratic.** Nearly every KINKED name's `kink_expiry` lands on one of four dates: **2026-08-28** (SPY, MU, META — pre-empting Core PCE), **2026-09-04** (AMD, TSLA, ZS — NFP), **2026-09-11** (ORCL, DG, PANW, PATH — **CPI**), **2026-09-18** (MSTR, QCOM — post-FOMC). This is the market pricing the macro calendar into front tenors across unrelated names. **Only 7 of 12 KINKED names locate the kink at their own earnings expiry; 5 of 12 mislocate** — a worse rate than the historical ~19%.

**Back-month skew is the gate almost nothing clears.** Measurable on 22 of 25 names: **TAIL_HEDGING (stretched) on only 4 of 22 (18%)** — AEO, **BBWI, BBY, KSS**. **COMPLACENT/flat on 11 of 22 (50%).** Almost none of the KINKED-at-event names also show a stretched tail, which is why so much of this book routes to calendars rather than naked short vol.

### BUY VOL

| Ticker | Basis | Implied move (derived) | Structure |
|---|---|---|---|
| **MU** | base_shape **CONTANGO** post-hygiene (raw BACKWARDATION flipped), FER@7 0.914 no panic. **VRP −0.330 — IV 64.7% vs RV 97.7%, a 33pp gap, widest in the scan.** iv_pctile 7.5 (provisional). No idiosyncratic catalyst — systematically underpriced semis vol (SMH rv20 42.4%). | **10.7%** | long strangle / calendar, **starter** |
| **AMD** | base_shape **FLAT**, kink prominence **5.9% = near-miss below threshold**. FER@7 0.915. VRP −0.218 (22pp gap), iv_pctile 13.8 (provisional). Kink at NFP 09-04 — cheap vol into a *macro* catalyst. | **8.5%** | NFP-week straddle, small |
| **DELL** | KINKED, kink_expiry **2026-09-04 matches** earnings 09-01. **VRP −0.068 (PREMIUM_BUYING)** — vol cheap vs realised, contradicting the naive "high IV = crowded" read. Skew flat/NORMAL. | **19.6%** | 09-04 ATM straddle, starter |
| **MRVL** | Plain BACKWARDATION, FER 1.245. **VRP −0.149, most negative in scan** (IV 79.2% vs RV 94.1%). Earnings 08-27. | **13.1%** | straddle into 8/28, starter |

### SELL VOL (half size at most — every one carries a disqualifier)

| Ticker | Basis | Implied move | Disqualifier |
|---|---|---|---|
| **SNOW** | kink 09-04 matches earnings 09-02. **VRP +0.360, strongest premium-sell read in the set.** | 17.4% | skew 1.087 — just under the TAIL_HEDGING cut |
| **MDB** | kink 09-04 matches earnings 09-01. VRP +0.209. Richest vol in the scan (IV 124.7%). | **20.6%** | skew **UNMEASURABLE** |
| **ZS** | kink 09-04 matches earnings 09-03. VRP +0.251, FER@7 1.462. | 17.6% | **skew COMPLACENT/FLAT 0.0042, ratio 1.007** |
| **LULU** | kink 09-04 matches earnings 09-03. VRP +0.196. | 13.5% | skew flat 0.0087 |

### CALENDARS (front panic >1.10 disqualifies naked size)

**BBWI** (front 3DTE IV 173.7% vs 10DTE 104.7%, FER 1.456, **TAIL_HEDGING 1.383**, VRP +0.206, move 15.8%) · **KSS** (204.9% vs 117.8%, FER 1.487, TAIL_HEDGING 1.19, VRP +0.2785, move 18.6%) · **BBY** (122.1% vs 71.4%, FER 1.433, TAIL_HEDGING 1.33, move 11.1%) · **OKTA** (175.8% vs 116.6%, **FER 1.595 — the most extreme in the scan**, skew COMPLACENT, VRP +0.3155, move 15.9%) · **CRWD** (FER 1.312, skew flat, move 10.6%) · **BURL** (FER 1.443, move 11.1%) · **ADSK** (191.9% vs 72.4%, FER 1.301, move 17.4%) · **DLTR** (FER 1.461, skew unmeasurable, move 11.5%).

### SKIP, with reasons

- **A, DCI, DY** — **`NO_NEAR_TENOR`.** The three highest raw IV ranks in the entire scan (85.8 / 83.4 / **96.1**) with earnings *tomorrow*, and **no listed tenor both covers the event and clears the 15-contract floor** (nearest jumps to 24 DTE). **Unmeasurable, not calm.** Do not read the IV rank as tradeable.
- **CRM** — kink at 52 DTE / Oct-16, unrelated; earnings is tomorrow. VRP **FAIR (+0.02)** — no confirming leg despite a textbook earnings-backwardation shape.
- **DG, PANW, PATH, ORCL** — kinks land on/near **2026-09-11 = the CPI print**, not their own earnings (PANW's 44.4% prominence, the largest in the set, is a market-wide macro hump). ORCL's FER read is additionally `INVALID_TENOR_PRE_EVENT`.
- **DOCU** — kink correctly located with 15.2% prominence, but **VRP FAIR (+0.008)**: failing to contradict is not confirmation.
- **AEO** — kink mislocated to 09-25, 23 days post-earnings; genuine TAIL_HEDGING and an unusual FER 0.683 make it an anomaly worth a follow-up, not a verdict.

**IV outliers:** the largest-premium rows are **0DTE-adjacent noise** — SPY 500C exp 08-25 (avg_iv **673%**), QQQ 495C exp 08-25 (avg_iv **1092%**) — same-day expiry gamma artifacts, the known contamination. The next tier is $1-strike penny names at 20–60× IV. **No credible single-contract whale mispricing surfaced today.** Skew across the seven names checked at 30 DTE is **COMPLACENT on all seven** (0.95–1.01) — no tail-hedging demand and no call-side lottery skew anywhere in that set.

**Class ceilings apply and are binding:** `earnings_vol` caps at **0.55** (post-freeze realises **0.449 on n=78** — a losing class), `high_iv_rank` at **0.60** (realises 0.562, n=16). Both then land in the **[0.55, 0.65) anti-predictive band** → starter. That stacking is intended.

---

## 6. Risk & Correlation

**Macro headline:** core PCE **3.29%** YoY against **July payrolls −23k**, fed funds 3.63 → a **~34bp real policy rate**. Curve normal +47bp, 10Y 4.70% flat, broad USD **weakening −2.51 over 30d**, gold **+7.41% over 5 days**. **Forward:** Core PCE **T+1**, NFP T+8, CPI T+12, FOMC T+14/15.

**Breadth (advisory, 0 points, `fz`):** 207 advancers / 294 decliners, **`pct_green` 41.15%**, median change −0.24%. **`divergence_flag: true`** — the index is green with fewer than half its constituents participating. Independently corroborated by equal-weight **RSP −0.07%** vs SPY +0.32%. Two unrelated data lineages, one conclusion: **narrow-leadership distribution.** This does not change sizing; it changes how much you trust "green tape."

### Correlation clusters

`uw risk portfolio-correlation` on today's eight candidates (not the static watchlist), 30d:

| Pair | corr | Band | Action |
|---|---|---|---|
| **MU / AMD** | **0.834** | ≥ 0.70 → **CLUSTER** | `semis_vol_cluster` — keep MU (score 1 > 0); **AMD −1 tier** |
| ZS / OKTA | 0.692 | 0.60–0.70 → soft watch | **No penalty** (mechanical threshold) |
| NVDA / AMD | 0.510 | < 0.60 | not flagged |
| NVDA / MU | 0.501 | < 0.60 | not flagged |

**ZS/OKTA is the textbook case for why the discretion was removed.** Qualitatively these are the same trade — two security/identity SaaS names, both `short_vol`, both `earnings_vol`, both with earnings-driven FER blowouts (1.462 / 1.595), both flagged for flat COMPLACENT skew. Every instinct says cluster them. The 2026-05-15 audit removed exactly that discretion (0.631 fired once, 0.703 did not); **0.692 < 0.70 → soft watch, no deduction.** Recorded, not overridden.

**NVDA is the third semi and the tool puts it below even the soft band** (0.51 / 0.50). On a 30d lookback that is real idiosyncratic divergence — NVDA is trading its own earnings — but it means **the matrix would not have protected a three-semi book.** Treat NVDA/MU/AMD as concentrated regardless.

**KNOWN DEFECT, not a finding:** `sector_breakdown` returned `{"Unknown": 8}` with `sector_concentration: "100% in top sector"` and a `CONCENTRATION` warning. The tool failed to map sectors and reported its own failure as an alarm. **Discarded.**

### Gate stack — 26 firings across 8 names, zero silent skips

**Event risk is the loudest gate and it fires 8 of 8.** Four Tier-1 binaries detonate in **one overnight gap**: Core PCE 08:30 ET, plus **NVDA, OKTA and BBWI earnings all on 2026-08-26.** Three of today's eight candidates report into the same macro print.

**The panic gate fires 5 of 8 — and the desk should know what it is measuring.** At `--near-dte 7`: OKTA 1.595, ZS 1.462, BBWI 1.456, NVDA 1.444, META 1.186 fire; MU 0.914, AMD 0.915, EWZ 1.010 do not — while **both indices print CONTANGO** (SPY 0.887, QQQ 0.925). This is **single-name earnings backwardation, not systemic panic**: four of the five firings have a dated binary inside nine sessions. It is applied mechanically at −1 with no exceptions. **META at 1.186 is the one firing with no catalyst to explain it** — which is why its own bull volunteered it as the killing argument.

**The debate gate fires 5 of 5.** No thesis survived disconfirmation.

**The sector gate fires on nobody**, and one non-firing deserves explanation: **BBWI sits in Consumer Cyclical, the largest netted OUTFLOW (−$21.1M) — and BBWI is a short. Outflow supports the short.** Firing the gate there would be a sign error.

### Fundamentals verdicts (top-5)

| Name | Verdict | Adj | The contradicting fact |
|---|---|---|---|
| **NVDA** | **CAUTION** | −1 | Earnings **T+1**, held through by the scored 08-28 structure; insider MSPR −98.61. *But* 2 of 3 legs support the long, so no VETO — and the MSPR is chronically ~−100 back through 2025, i.e. routine 10b5-1 with low incremental information (C10). |
| **META** | **CAUTION** | −1 | The "beat_streak" is a majority-of-4 count — **the most recent and largest-magnitude surprise was a −16.03% MISS**. EPS growth **−3.69% YoY** on +27.65% revenue. MSPR −55.84 and here *genuinely informative* (month-to-month sign flips, unlike NVDA). No catalyst. |
| **MU** | CONFIRM | 0 | Fundamentals corroborate the *vol* thesis: revenue +166.98% YoY, EPS +700.71%, beats 17–27%. Earnings 27d out, so current RV is cycle repricing, not anticipation. |
| **ZS** | CONFIRM | 0 | Four tightly-clustered positive surprises (3.96–9.33%) = the safer-to-sell-vol signature; full PT-reiteration stack ($192–214) in the trailing week. |
| **EWZ** | **NA** | 0 | Country ETF — the gate's machinery is structurally inapplicable. **NA never penalizes.** |

**Zero VETOs.** AMD / OKTA / BBWI sit outside the top-5 and were not gated.

### Debate residuals — 5 of 5 CUT

| Name | bull | bear | Spread | Gate |
|---|---|---|---|---|
| EWZ | 0.35 | **0.75** | −0.40 | CUT |
| NVDA | 0.25 | **0.85** | −0.60 | CUT |
| META | 0.25 | 0.25 | 0.00 | CUT (tie) |
| MU | 0.35 | **0.65** | −0.30 | CUT |
| ZS | 0.25 | 0.45 | −0.20 | CUT |

**Every bull residual is ≤ 0.35 — BOTH_SIDES_LOW on all five.** In three cases (EWZ, META, MU) **the bull volunteered the argument that killed its own thesis**, and in a fourth (NVDA) it conceded the bear's lead point outright. The additive rubric scored EWZ at 2 and would have kept walking; the disconfirmation step is what turned "weak long" into "no trade." A both-sides-low deduction remains a pre-registration candidate, **not** a live gate — the cut applied is the standard `bear ≥ bull → −1 tier`.

### Adverse-flow exits

**`conviction_2026-08-24` does not exist.** The most recent daily group is **`conviction_2026-08-21` = [IWM]** — yesterday also produced an empty board and correctly wrote nothing. Scanned the rolling 7-session universe instead:

| Carried name | Today's flow | Read |
|---|---|---|
| **IWM** (08-20, 08-21) | bullish, +$18.6M, OI +139,707, a $418.39M DP print | **Thesis intact, no reversal.** But volume_ratio 0.60 = engagement decaying. **MONITOR** |
| **GDX** (08-19) | bullish, +$159k (trivial), volume_ratio 0.94 | Working on the underlying (GLD +7.41%/5d) but options engagement is flat. **MONITOR** |
| **ULTA** (08-18) | bullish, +$505k, **volume_ratio 2.46**, P/C 1.357 | **SOFT EXIT.** Not a flow reversal, but ULTA sits in Consumer Cyclical — the largest netted **OUTFLOW** — with XLY −0.30% and elevated volume arriving put-tilted. Off-thesis drift. |

**Hard exits: none.** `fz quote-drift` since 08-24 is **clean** — no short-float spike, no PT cut, no `Recom` deterioration on any carried name.

**One un-grouped alert worth surfacing: EWZ** flagged `VOLUME_SPIKE 11.9×`, `LOW_PUT_CALL P/C 0.04`, `LARGE_DARK_POOL $106.38M single trade`, `OI_SHIFT +257,546`. That corroborates the *scale* of the Nov-20 build — **but it contradicts the per-leg read**: a P/C of 0.04 is an extreme call-count skew, while the largest *premium* line in the name is a $7.04M ATM put buy and the flagship 43C is bid-side. **Contract-count and premium-weight point opposite ways in the same name on the same day.** Neither adjudicated.

### Hedge sleeve

**None recommended. Directional skew is 0.0 — there is no book to hedge, and a hedge against an empty book is a naked position with a defensive label on it.**

**What the desk should actually do overnight:** carry no directional or vol exposure. **Cash is the position.** If legacy risk exists, the only defensible action is trimming gross into the print — an SPY/QQQ vertical or VIX ladder bought at VIX 15.45 the session before a Tier-1 print is *paying* the event premium, not avoiding it. **Do not run the 0DTE stack tomorrow morning** (§2a). Reassess after 08:30 ET with three earnings reports landing in the same gap.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**EMPTY. No name reached MEDIUM (7), let alone HIGH (9). The top score was 2.**

**Expectancy lens** *(advisory — expectancy is not yet a live sizing axis)*, from the 2026-08-22 `phase_3_calibration`:

| Tier | Mean realised P&L | Payoff ratio | n |
|---|---|---|---|
| HIGH | **−2.441%** | 0.72 | 7 |
| MEDIUM | +0.104% | 0.948 | 19 |
| LOW | −2.249% | 0.929 | 123 |
| **DROP** | **−5.004%** | **0.647** | 488 |

C3 fractional-Kelly remains **`ADVISORY_ONLY`** — n=27 closed calls (bar ≥30) *and* tier × expectancy is non-monotone. The win-rate ladder stays the live sizer. The one encouraging line: **DROP's expectancy is by far the worst even though its hit rate is the best** (payoff 0.647 vs 0.929/0.948) — the DROP pile wins small and loses big. That is the first metric in eight cycles suggesting the tier ordering does *something*, and it is a P&L metric, not a hit-rate one.

### Full audit trail — all 8 scored calls

| Ticker | Dir | raw | Tier | Class | win_rate (n, source) | excess | pre-risk | Fund. | bull/bear | Gates fired | Final |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EWZ | long | **2** | DROP | multileg_directional | null · NA(substrate) | null | skip | NA | 0.35 / 0.75 | event_risk, debate, rubric_regime | **skip** |
| NVDA | long | 1 | DROP | multileg_directional | null · NA(substrate) | null | skip | CAUTION | 0.25 / 0.85 | panic, fundamentals, event_risk, debate, rubric_regime | **skip** |
| META | long | 1 | DROP | dealer_positioning | null · NA(substrate) | null | skip | CAUTION | 0.25 / 0.25 | panic, fundamentals, event_risk, debate, rubric_regime | **skip** |
| MU | vol_long | 1 | DROP | vol_term_dislocation | null · NA(substrate) | null | skip | CONFIRM | 0.35 / 0.65 | event_risk, debate, rubric_regime | **skip** |
| ZS | vol_short | 1 | DROP | earnings_vol | null · NA(substrate) | null | skip | CONFIRM | 0.25 / 0.45 | panic, event_risk, debate, rubric_regime | **skip** |
| AMD | vol_long | 0 | DROP | vol_term_dislocation | null · NA(substrate) | null | skip | — | — | cluster, event_risk, rubric_regime | **skip** |
| OKTA | vol_short | 0 | DROP | earnings_vol | null · NA(substrate) | null | skip | — | — | panic, event_risk, rubric_regime | **skip** |
| **BBWI** | **short** | **−1** | DROP | bearish_flow | **0.5486 · n=144 · backtest_clean** | **−0.0486** | watch_only | — | — | regime, panic, event_risk, rubric_regime, **SHORT-ROUTING** | **watch_only** |

**Scoring components that fired at all:** `+2` multileg (NVDA, EWZ) · `+1` DEX flip (META) · `+1` direction-verified OI build (META, EWZ) · `+1` vol-surface VRP-aligned (MU) · `+1` earnings-scout vol side (ZS) · `−1` flow_conflict_lite (**4 of 4 directional-class names**). **The single most-firing line on the board is a deduction.**

**Rubric lines that earned ZERO across all 8 names — and why:**

| Line | Why zero |
|---|---|
| `+3` accumulation conjunction | accumulation-hunter cleared **zero** tickers. AAPL disqualified (conviction-matrix **COVERED_CALL**, 27.4%), AMZN 31.0% and META 19.9% below the 50% floor; **GOOGL/GOOG/SNPS rejected for confirmed basket/closing-cross contamination**; MRVL on a mega-vs-block tier contradiction (0.123 vs 0.604); TSLA NEUTRAL on n=1. The C11 gate was never reached — there was nothing to gate. |
| `+1` conviction-matrix >70 | Conditional on `leap_directional`; the LEAP book is empty ⇒ **unsatisfiable by construction**. |
| `+1` OPEX pin top-5 | Monthly OPEX passed 2026-08-21; today is OPEX+2. Scored book empty. |
| `+1` cum-flow accretion | 7 of 8 names return `trend_direction: MIXED` @30d. **The intent screen was never reached on any name.** |
| `+1` sector leader | All four candidates fail condition (b) — 30d direction MIXED. AMD additionally fails on outright **sign** (−$97.85M against the thesis). Condition (a) was non-discriminating as predicted (10 of 11 sectors INFLOW at 0.8–1.0). |
| `−3` flow_conflict | META was the only literal trigger; **downgraded to −1** on three grounds (tool label is MIXED not OPPOSITE; −0.128% of gross is degenerate; the 5d flow **agrees** with the thesis and the 30d window entirely predates the signal). |
| `−2` overcrowded long | NVDA was the only candidate. VRP +0.0465 satisfies the parenthetical, but **the "rising" trajectory condition measurably FAILS** — see below. |
| ~~`+2` signal-confluence ≥4~~ | Removed 2026-06-12 P0.2 — structurally zero. |
| ~~`+1` sweep-persistence~~ | Removed 2026-05-23 P0.3 — structurally zero. **Directly consequential today: it is why OKTA scores 0 despite a 2-agent gate pass.** |

**HIGH-tier load-bearing-tool gate: NO-OP** (no name ≥ 9), recorded rather than silently skipped. It could not have passed anyway: **two of the four LB tools produced nothing at all today** (`uw dark-pool block-stratified` and `uw insights institutional-accumulation` — accumulation-hunter flagged zero names), and `uw options-structure dex` is cited on META only. **Maximum LB-tool citation on any name today is 2 of 4.** Even a score-9 name would have been demoted to MEDIUM.

### Substrate findings surfaced this session

- **S1 — NVDA per-leg side data inverts the multileg thesis.** Detailed in §3a. The data the agent said was unavailable exists, and it points short.
- **S2 — EWZ's flagship block is bid-side and the two tools disagree ~15× on premium.** Detailed in §3a. Unadjudicated.
- **S3 — NVDA's "rising pc-z" is now VERIFIED as FAILING, not merely unverified.** `pc-ratio-zscore` has no `--date` flag, but **`uw historical trend` supplies the underlying P/C series directly**: 08-25 0.385 · 08-24 0.652 · 08-21 0.602 · 08-20 0.583 · 08-19 0.595 · 08-18 0.572 · 08-17 0.548 · 08-14 0.538 · 08-13 0.517 · 08-12 0.519 · 08-11 0.685. Prior-15d mean **0.544** → last-5d mean **0.563**: the ratio is **rising**, i.e. call-crowding is *unwinding*. Today's 0.385 is a lone outlier against eight sessions in the 0.506–0.685 band. The rubric's `"Rising" needs a multi-date z trajectory` guard did its job. **Recommend recording `uw historical trend` as the standard substitute substrate for pc-z trajectories — it closes a gap the fleet has been logging as unverifiable for cycles.**
- **S4 — BBWI's Tier-1 `OPENING_PUT_PRIME` does not reconcile.** The single-leg scan reports $500K premium at size/OI 23.8×; `uw oi biggest-increases` shows OI +125 on volume 163, **bid-side**, ~$0.00M, against a whole top-10 OI book of $0.20M. A $500K ticket would need ~$30/contract on a $17 stock. **0 points either way** (C19 refuted), but a Tier-1 "opening" label the OI tool shows as bid-side and non-opening belongs in the defect log.
- **S5 — `oi-trend` non-discrimination quantified.** `overall_trend = BUILDING` on **8 of 8** (zero variance); `consecutive_build_days` at the cap of 5 on **7 of 8**. EWZ's `3` is the only informative value the field produced all session. **Direction-verification cuts the award from 8/8 to 2/8** — the verification carries all the discriminating power; the label carries none.

### Registered rubric-structure defects (not fixed — the 2026-06-12 freeze holds)

- **D1 — no rubric line can pay a directional short.** Every line that could score a bearish name is a deduction, was removed, is permanently 0-point, is long-only by construction, or requires a structure a short thesis lacks. **This compounds with the 2026-08-01 routing rule** and is the plausible generative mechanism for the 2026-08-22 finding that short generation halved (32.0% → 17.6%, regime-controlled p = 0.0045) while routing compliance stayed perfect. **It is a scoring-side problem, not a routing-side one.**
- **D2 — the flow_conflict deduction side is scale-blind.** The C11 award side has a 5%-of-gross scale-relative floor; the deduction side has none. The bottom-quartile test is union-relative, so **BBWI's perfectly-aligned 13.7%-of-gross flow on a $10.4M gross book is penalised while NVDA's 0.38%-of-gross churn on $27.6B is not.** It systematically over-penalises small caps and under-penalises mega-caps.

### Instrumentation trio

`implied_move`: **MU 10.7% · AMD 8.5% · ZS 17.6% · OKTA 15.9% · BBWI 15.8%**; explicit `null` on NVDA/META/EWZ (not vol rows, no agent derived one). `dp_block_to_float_ratio`: **`null` on all 8 — N/A by construction**, since there are zero `dark_pool_accumulation` rows on the board; **C16 is ungradeable today for want of a subject, not for want of instrumentation.** `insider_cluster_flag`: **`false` on all 8 — checked-and-absent, not `null`** (`fz insider-clusters` returned empty market-wide against a *populated* store). Note this is a **16th consecutive all-`false` population** for C18, which the 2026-08-08 audit already found has zero variance across 15.

### Conviction scoring rubric (version `2026-06-12`, FROZEN) — embedded verbatim

```
Daily conviction score = Σ:
  +1  dealer-positioning MECHANIZED DEX flip or vanna-squeeze in trade direction — verified SIGN CHANGE,
      not a level; computed by scripts/dex_flip.py; evidence must cite both dated values
  +3  3+ aligned signals in accumulation-hunter (DP + OI + oi smart-positioning, dark-pool block-stratified
      institutional-tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms
      (sign aligned AND |cum_flow_30d| >= $50M); else halved (floored) +3 -> +1
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days >= 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: award only when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts
  +1  uw historical cumulative-premium-flow net directional accretion in trade direction (30d) —
      INTENT-SCREENED: (a) no C28 distribution_flag on the name, AND (b) on dividend payers inside an
      ex-div window the accreting prints are NOT deep-ITM sub-parity calls
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector — CONDITIONAL:
      (a) sector persistence_score >= 0.6 AND (b) cum_flow_30d direction aligned AND (c) |cum_flow_30d| >= $50M
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising pc-ratio-zscore (VRP positive) — an
      INFORMED-FLOW CONTINUATION penalty, not "fade the crowd". "Rising" needs a multi-date z trajectory.
  -3  flow_conflict — cum_premium_flow 30d direction CLEARLY opposite dominant_signal_class
  -1  flow_conflict_lite — 30d cum_premium_flow read is MIXED
      (-3 and -1 are MUTUALLY EXCLUSIVE — apply ONE, never both)
  # REMOVED: +2 signal-confluence >=4 (2026-06-12 P0.2); +1 sweep-persistence (2026-05-23 P0.3)
  # TIER GATES (2d, not score_components, contribute 0 to raw_score):
  -1  [TIER GATE] risk-monitor correlation cluster (pairwise corr >= 0.70) — -1 TIER
  -3  [TIER GATE] uw risk market-regime conflicts with trade direction — -1 TIER
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | HIGH | full (subject to the 3-of-4 load-bearing gate + win-rate gate) |
| 7 – 8 | MEDIUM | half (subject to win-rate gate) |
| 3 – 6 | LOW | starter / watch-only |
| ≤ 2 | drop | filtered by the quant's drop floor |

**Tier-cut status:** the ≥9 HIGH cut **failed its scheduled re-confirmation on 2026-06-12** (bands inverted on the first post-UPTREND window). Cuts are retained under the freeze but carry **no validated ranking claim**; the P0.6 out-of-regime guard caps all sizing at half in the interim.

---

## 8. Watch-only — single signal, no confluence

Surfaced by one agent, failed the ≥2-agent confluence gate. **For journaling, not entry.**

| Ticker | Sole flag | Note |
|---|---|---|
| **DELL** | earnings-scout BUY VOL | Strongest single-agent vol idea on the board — kink 09-04 matches earnings 09-01, **VRP −0.068 PREMIUM_BUYING**, implied move 19.6% |
| **MRVL** | earnings-scout BUY VOL | VRP −0.149 (most negative in scan); but accumulation-hunter **rejected** it on a mega-vs-block tier contradiction (mega buy_ratio 0.123 sell-dominated on $407.7M) |
| **SNOW** | earnings-scout SELL VOL | VRP +0.360, strongest premium-sell read; skew 1.087 just under the tail cut |
| **MDB** | earnings-scout SELL VOL | Richest vol in the scan (implied move 20.6%); skew unmeasurable |
| **KSS** | earnings-scout CALENDAR | Genuine TAIL_HEDGING 1.19, VRP +0.2785 — but contrarian called it **ambiguous**: a stale bearish pc-z 4.493 against today's *bullish* price+flow alignment = short-covering risk |
| **GLD** | sweep-tracker (bullish) — **CONTRADICTED** | multileg found the dominant 425C print ($27.9M, 86% of strike volume) traded **BID-side**, consistent with a bear call spread / covered-call overwrite, and **declined the directional +2**. GLD +7.41%/5d with screener net_flow −$101.8M |
| **TSLA** | sweep-tracker Tier-1 floor put | accumulation-hunter rejected (NEUTRAL, n=1 mega trade); dealer-positioning disqualified (5 sign changes) |
| **SPCX** | sweep-tracker Tier-1 floor put | **Deep-ITM financing structure, not conviction** — extrinsic is 1.28% of a $11.35M premium (see §3a) |
| **MSTR** | sector-rotation Tech leader | dealer-positioning **disqualified** it — 6 DEX sign changes in 12 sessions, worst whipsaw in the batch |
| **GOOG** | sector-rotation Comm Svc leader | accumulation-hunter **rejected** GOOG/GOOGL outright for confirmed basket/closing-cross contamination |
| **APP** | sector-rotation Tech leader | single agent |
| **ARGX** | contrarian price-vs-flow divergence | Price +18.1% vs flow −$2.41M, pc-z +6.717, CONTANGO — routed outside the contrarian lane as short-continuation material |
| **SMH** | dealer-positioning note | Dealer book stayed net-short-hedge through today's +1.65% bounce — **the rally got no dealer tailwind** |
| **CRWD, BBY, BURL, ADSK, DLTR, LULU** | earnings-scout | Calendar / sell-vol candidates, single agent each |
| **AAPL, AMZN** | accumulation near-miss | AAPL killed by **COVERED_CALL** (27.4%); AMZN 31.0% with a $15.9M deep-ITM call closure and a sector netted outflow |
| **A, DCI, DY** | earnings-scout SKIP | Highest IV ranks in the scan with earnings tomorrow — **`NO_NEAR_TENOR`, unmeasurable not calm** |
| **NVS, IWM, GDX, ULTA** | funnel / carried watchlist | See §6 for the carried-name flow scan |

---

### Fleet-integrity notes

- **`fz` bulk-screen ticker corruption confirmed again — 20/20 rows on both lanes** (AABEO→ABEO, KKURA→KURA). Decoded by stripping the doubled leading character. Per-ticker `fz_enrich` is healthy; only the bulk funnels are affected. All `fz` lanes are advisory / 0 points.
- **Yahoo `quoteSummary` returned HTTP 401 on all three deep-dive names** — the MCP fundamentals path is down this session. Graceful-skipped; Finnhub carried Phase 2b. The **raw** Yahoo chart API (used by `market_data.py` for C12 and the ^VIX series) worked normally.
- **`opex-pin-strategist` was spawned on the mechanical 5-calendar-day rule and correctly returned an empty scored book** — monthly OPEX passed 2026-08-21, `pin-risk` has no expiry flag (returns only the 08-28 weekly), and `opex-concentration`'s forward-monthly names have **zero overlap** with the C12 universe. It surfaced one advisory NVDA 210-strike observation with a verified positive net-GEX sign, explicitly gated by tomorrow's PCE.
- **`uw playbook batch-scan` (Step 6.5) was deliberately skipped** — it operates on the HIGH+MEDIUM list (raw_score ≥ 7) and there are zero such names. Recorded as a reasoned skip, not an omission.
- **Watchlist write-back: NOTHING WRITTEN, deliberately.** All eight names are DROP tier; the rule (corrected 2026-07-23) is to write only LOW-or-better names, never the raw top-5. Writing EWZ/NVDA/META/MU/ZS would seed tomorrow's correlation and adverse-flow checks with names this desk explicitly refused to size. Zero state mutations this session.
