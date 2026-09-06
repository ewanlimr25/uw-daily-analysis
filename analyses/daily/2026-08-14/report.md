# Daily Market Analysis — 2026-08-14

## Executive Summary

- **Regime + GEX state:** TRANSITIONAL (trend UPTREND) — SPY 776.34 above both 20/50 SMAs but −0.20% on the day; VIX 14.25 and falling (−2.6% 1d, −4.36% 5d); SPY and QQQ both in **POSITIVE gamma** sitting essentially *on* their zero-gamma levels; `fz` breadth 49.7% green with a median change of **exactly 0.00%**. Sector lean: Energy (XLE +1.39% 1d, **+7.67% 5d**) and Utilities bid, Consumer Cyclical and Healthcare sold. A directionless, low-energy, pre-OPEX drift.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** **SPY** POSITIVE / ZGL 774.67 (0.18% from spot) / call wall 780 · put wall 765 — pin bias, walls tight. **QQQ** POSITIVE / ZGL 729.92 (0.07%) / call wall 735 · put wall 720 — same pin setup, thinner book. Both regimes are only 2–3 sessions old. Advisory, see §2.
- **Top swing build:** **none.** No name cleared the gate stack. The highest raw score on the board was 5 (LOW tier) and it was VETO'd on fundamentals.
- **Top LEAP candidate:** **none.** `leap-positioning-radar` returned an empty pass-list; its only real candidate (PLTR) failed two *required* gates.
- **Biggest risk:** not a position — it is the **substrate**. Three separate rubric/tool lines fired on ~100% of their population today (`oi-trend BUILDING` **14 of 14**, sector persistence **11 of 11**, raw BACKWARDATION labels **11 of 15 flipped** under hygiene). Every raw score below carries one point of pure noise. The only correlation cluster on the board is **MU/AMD at 0.855**.

**Post-gate book: EMPTY. Zero sized positions.** This is the 20th consecutive empty board, and it is the correct output — the audit record shows the DROP pile has repeatedly outperformed the sized book (DROP 43.3% vs sized 38.6%).

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend UPTREND. SPY 776.34, SMA20 756.20, SMA50 748.93, +3.41% 30d, −0.39% from the 90d high. Guidance: *half position sizes, favour defined-risk, iron condors in range.*

The breadth reading is the session's most informative single number, and it needs both sources to see it. UW **flow** breadth is **35.1% bullish** (2,214 bullish-flow tickers vs 4,098 bearish, of 6,312 with options). `fz` **price** breadth is **49.7% green** (250 advancers / 245 decliners / 8 unchanged, median change 0.00%, average +0.06%). Price and breadth agree with each other; **flow is materially more bearish than price**. Bearish flow into a flat tape is the real signal of the day, and it is what the empty book is ultimately expressing.

### Per-index gamma (current-state EOD book)

| Index | Spot | Zero-gamma | ZGL reliable | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|---|
| SPY | 776.06 | 774.67 (−0.18%) | yes | +$2.02B | POSITIVE | 780 (+$443.5M) | 765 (−$128.4M) |
| QQQ | 730.41 | 729.92 (−0.07%) | yes | +$652.3M | POSITIVE | 735 (+$156.3M) | 720 (−$20.6M) |
| IWM | 305.09 | *degenerate (150–215 vs spot ~305)* | **no** | — | — | — | — |

IWM's ZGL is the documented **ZGL-grid artifact** (the SPY/QQQ/IWM/MU class) and is reported as unusable rather than laundered into a level.

**`uw options-flow dte-volume-share`:** 0DTE **45.8%**, weeklies 25.3%, monthlies 16.0%, LEAPs 3.3% → `RETAIL_DRIVEN`. Institutional monthly+ share is only 19.3%. Per the market-level overlay rule this uniformly **downgrades every rotation and swing conviction** — the tape has no institutional benefit-of-the-doubt today.

**`uw historical vrp`:** SPY −0.0073 **FAIR** (IV30 11.76% vs realised 12.49%); QQQ −0.0506 **PREMIUM_BUYING** (IV30 18.17% vs realised **23.24%**). Both negative — this is a premium-**buying** tape. That single fact closed the contrarian fade lane and set the burden of proof against every short-vol structure on the board.

**Macro backdrop (`scripts/fred_macro.py`):** curve **normal** (10Y−2Y +51bp); core CPI 2.79% YoY, **core PCE 3.29% YoY** (sticky, well above target); unemployment 4.1% with **payrolls −23k MoM — an outright contraction**; 10Y 4.63% flat over 30d; USD weakening; fed funds 3.63%, leaving only ~34bp of *real* policy rate. Soft labour + sticky core + weak dollar is a **stagflationary tilt**, and it is a coherent explanation for what the tape is actually doing: bidding Energy and Utilities, selling Consumer Cyclical.

### Forward event risk (next ~10 sessions)

| Date | Event | Impact |
|---|---|---|
| 2026-08-19 (T+3) | FOMC minutes (Jul 28–29 meeting) | medium-high |
| 2026-08-20 (T+4) | Weekly jobless claims | low-medium (elevated salience after −23k payrolls) |
| 2026-08-21 (T+5) | **Jackson Hole opens (Powell)** | **high** |
| 2026-08-21 (T+5) | **Monthly OPEX** (third Friday) | **high — structural** |
| 2026-08-21 (T+5) | Flash S&P PMIs / Philly Fed / Existing Home Sales | medium |
| 2026-08-22 | Jackson Hole day 2 | medium-high |
| 2026-08-25 (T+7) | Consumer Confidence / New Home Sales | low-medium |
| 2026-08-26 (T+8) | **Core PCE (July) + Q2 GDP 2nd est.** | **high** |
| 2026-08-27 (T+9) | Weekly jobless claims | low-medium |
| 2026-09-04 | NFP (August) | high (just outside the window) |

**There is no clean window.** Any 1–6 week swing sized today eats four Tier-1 events. Every thesis below had to state how it survives Jackson Hole; most could not.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** Prose-only, **0 conviction-rubric points**, no backtested predictive claim. The predictive validation of these levels lives in `/weekly-analysis`'s rolling §2 backtest, not here. Scope is SPY and QQQ only.

**SPY — POSITIVE gamma, spot on the flip.** Spot 776.06 sits 0.18% above a reliable ZGL of 774.67; `total_gex` +$2.02B. Structural prior is mean-revert / pin / vol-suppression into Monday's open. Two wrinkles matter more than the walls: the largest gamma concentration in the whole book is not the wall at all — **strikes 775/776 together carry ~$1.61B**, sitting essentially *at* spot, and that is the real magnet. There is a local negative pocket immediately above at **777 (−$106.4M)** before gamma turns positive again into the 780 wall, so expect chop in that 30–40¢ band rather than a clean glide.

**QQQ — POSITIVE gamma, spot on the flip.** Spot 730.41, ZGL 729.92 (0.07% away, reliable), `total_gex` +$652.3M. Strike **730 alone carries +$198.8M — the largest single-strike print in the QQQ book** and the true magnet. A negative pocket sits at 731/732/732.5 (~−$116M combined) before gamma turns positive into the 735 wall (secondary at 740).

**Regime freshness — read this before trusting the pin.** Both books have been genuinely choppy: SPY flipped POSITIVE/NEGATIVE/FULLY_NEGATIVE **6 times in 30 sessions**, QQQ **6 times**, with FULLY_NEGATIVE stretches in mid-to-late July where ZGL was null. The current POSITIVE regime is **only 2 sessions old for SPY** (flipped 08-13) and **3 for QQQ** (08-12). Recent, not battle-tested.

**Structure bias.** Both indices show tight walls (SPY call wall +0.51% / put wall −1.43%; QQQ +0.63% / −1.43%) — textbook iron-fly / butterfly geometry centred near 775–776 and 730. **But do not size off the structural read alone**, because §2a says the economics are negative. QQQ deserves the most caution: its −0.0506 PREMIUM_BUYING VRP means a short-premium structure there fights the vol surface directly, not merely a VIX-tercile note.

**Mandatory caveats:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes Monday and re-computes both ZGL and walls.
- **ZGL reliability.** Both indices pass the ~5%-of-spot test tonight (`zgl_reliable=true`). This book has historically produced garbage extrapolations on NEGATIVE-regime days (SPY 08-06: 814.6; 08-11: 789.87) — not the case here, but the failure mode is live.
- **Gap risk voids the prior.** No Tier-1 print falls on 08-17 itself, but FOMC minutes (08-19), Jackson Hole (08-21/22) and the OPEX unwind sit immediately downstream. This is a **one-session** read.
- **Tooling limit.** `gex --dte-max 1` errors, so this is the standing **0–45 DTE** book used as the D+1 proxy. That matters more than usual today: per `expiry-heatmap`, **monthly OPEX 08-21 is the 3rd-largest expiry in the book at $4.16B** while the actual D+1 target 08-17 carries only **$1.19B**. The aggregate walls above are materially **OPEX-weighted three sessions out**, not Monday-dated.
- **ETF book.** This is the SPY/QQQ ETF gamma book, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup — **STAND ASIDE**

The `zerodte_setup` headline says `GO_PREMIUM_SELL_INTRADAY` with `sell_premium: true` for both indices. **Both fields are unconditional and both are misleading tonight.**

`vol_state` is **LOW** (VIX 14.25, below the 16.1 low-tercile bound). Reading `mean_pnl_by_vix_state[LOW]` net of the assumed 0.1% round-trip cost:

| Index | LOW-tercile gross | **LOW-tercile NET** | Unconditional net (the headline) |
|---|---|---|---|
| SPY | +0.022% | **−0.078%** | +0.119% |
| QQQ | +0.091% | **−0.009%** | +0.241% |

**Both are negative-expectancy in the current VIX tercile.** The attractive unconditional figure borrows its entire edge from the MID (+0.331 / +0.469) and HIGH (+0.305 / +0.462) terciles. Two independent reads reinforce standing aside: SPY's VRP is FAIR (not premium-selling), and QQQ's is outright PREMIUM_BUYING.

For the record, the setup block: SPY `implied_move` 0.35%, `expected_range` 0.78%, `size_scalar` 0.5, suggested iron fly at 775.9 ±0.78%; QQQ 0.56% / 1.37% / 0.5, iron fly at 730.84 ±1.37%. Entry rule if it were taken: enter at/after the open once the gap resolves, hold to the close, **never carry overnight**. Worst observed day: SPY −1.40%, QQQ −2.45%. **`pnl_basis` is percent-of-underlying-spot-notional, GROSS** — not premium-collected and not margin-relative.

**Promotion bar unchanged:** this lane stays advisory / 0 rubric points permanently until *both* a vol-shock day enters the sample (the short-vol left tail is **UNSAMPLED**) *and* net expectancy clears a tail-aware bar. Win-rate is explicitly not the promotion metric for a negatively-skewed strategy.

---

## 2b. Swing Dealer Positioning (1–4 weeks)

Every DEX-flip verdict below was computed by `scripts/dex_flip.py` from 13 dated `uw options-structure dex` calls per symbol (2026-07-29 → 2026-08-14), never by hand.

**Exactly one name earns the mechanized +1: AVGO, direction SHORT.**

- `qualifies: true`. Evidence: `net_dex` 2026-08-13 **+2,752,637,767** → 2026-08-14 **−938,468,521**; the prior **11 sessions were all positive** ($0.6B–$5.5B). Flip magnitude 938,468,521 vs a floor of 805,217,827 (0.25× the trailing-10 median of 3,220,871,308) → `magnitude_ratio` **1.17**.
- `sign_changes_in_window: 2`, **`whipsaw_warning: false`** — a clean flip, unlike the 4–5× churn that caveated both July passers.
- GEX confirms it is not a single-strike artifact: regime **FULLY_NEGATIVE**, with **every strike from 330 to 455 carrying negative net GEX**. The regime went NEGATIVE on 08-10 and **held** (only 2 flips in 10 sessions, in contrast to the whipsawing indices).
- **Vanna is *not* a squeeze here.** The book is nominally put-heavy (`net_vanna` +1,016) but AVGO fell **−5.94%** today — a stock cratering has *rising* IV, which inverts the squeeze precondition. The same put-heavy book then makes dealers sell more, reinforcing downside. Flagged as bearish vanna pressure, not a squeeze.
- Tension worth stating: `front-end-iv-ratio` (at `--near-dte 7`) reads **0.823 CONTANGO** — no panic priced despite the −5.94% move.

**No name earns a vanna-squeeze flag, and the naive "falling VIX = bullish squeeze" read is wrong-signed today.** The VIX path 08-10 15.46 → 08-11 15.28 → 08-12 14.55 → **08-13 14.63 (UP)** → 08-14 14.25 breaks the ≥3-consecutive-decline requirement at the mechanized granularity. Independently, **SPY/QQQ/IWM books are all call-heavy** (`net_vanna` −235,949 / −181,567 / −108,577) — in a call-heavy book, falling IV makes dealers *cut* long-underlying hedges, i.e. mild **selling** pressure. The Karsan framing only works on a put-heavy book, and index books are not.

Other names: **SPY/QQQ/IWM** no flip, DEX positive throughout and *improving-then-decelerating* (SPY 44.7B→55.9B→83.1B→66.5B) — dealer long-delta built hard mid-week then eased Friday. Swing bias NEUTRAL on all three. **MU** (+264M→14.9B, steeply rising) and **AMD** (4.3B→11.75B) show building DEX but `qualifies: false` — low-conviction long tilt, no rubric points. **TSLA** carries `whipsaw_warning: true` (5 sign changes in 13 sessions) — the whipsaw *is* the finding; avoid building a dealer thesis there. **SNDK** disqualified at the dealer level too: its 5d DEX swing (−1.2B → +12.2B) tracks the deep-ITM roll, not conviction.

---

## 2c. Sector Rotation

**Rotation regime call: `no_change`. Confidence: LOW.**

Direction is read off the netted `uw risk market-regime.sector_rotation` across four sessions (08-11→08-14), not a single snapshot. `sector-flow` / `sector-flow-persistence` are one **gross-turnover** source and cannot express direction — and this session they carry **zero information**: 11 of 11 sectors return `trend=INFLOW` and 10 of 11 return `persistence_score=1.0`. A 1.0 is not evidence today, and it is not treated as such anywhere below.

| Sector | 08-11 | 08-12 | 08-13 | 08-14 | Read |
|---|---|---|---|---|---|
| **Consumer Cyclical** | OUT | OUT | OUT | OUT | **4/4 OUT — the only sector clearing the ≥3-day bar cleanly** |
| Financial Services | IN | IN | absent | IN | 3/4 IN |
| Industrials | absent | IN | IN | **OUT (flipped today)** | 3-day IN broken today — 1 session, not yet a reversal |
| Technology | OUT | OUT | IN | IN | flip-flopped mid-week — no persistent direction despite $3.11B gross |
| Healthcare | absent | IN | OUT | OUT | 2/4 OUT, short of bar |
| Utilities | absent | absent | IN | IN | 2/4 IN — one session from confirmation |
| Energy | IN (once) | absent | absent | absent | **never reappears — see below** |

**Rotating into:** *Financial Services* (netted 3/4, leaders **SYF**, **IVZ**; **CIFR** flagged — GICS-tagged Financials but functionally a bitcoin miner). *Energy* — resolved at the instrument layer: XLE's 5d cumulative options flow is persistently BULLISH (+$7.81M, all-call ask-side sweeps at $57–62 strikes) with dark-pool prints buy-leaning ($18.6M above mid). Leader **BTU**; note mega-cap **XOM is in today's bearish screener** (−$10.8M), so the bid is in the smaller/coal-adjacent complex, not the majors.

**The Energy resolution, stated plainly:** Energy never cracks the netted top-3 in either direction across four sessions despite being the best price tape (XLE +7.67% 5d) and the 2nd-largest gross flow (+$1.31B). This is **not** a C55 netted-vs-gross disagreement — it is netted **silence**: Energy's net call-minus-put dollar imbalance never gets large enough to rank in an 11-sector top/bottom-3 in a market where Tech options notional dwarfs it. Gross + ETF + price all agree IN; the authoritative netted tool is simply mute. Flagged as **sourced non-authoritatively**, not laundered into a "netted agree."

**Rotating out of:** *Consumer Cyclical* — the session's highest-conviction rotation call (netted 4/4, XLY 5d persistently BEARISH with a thin sweep tape and no buy-side block, price weakest on both 1d and 5d). Named leaders **LULU** and **AMZN** — both **`watch_only`** under the short-routing rule regardless of signal quality.

**Watch-only:** Industrials (netted flipped IN→OUT *today* after three clean IN sessions while ETF XLI is still 5d bullish — 2 of 3 sources still say IN); Healthcare (2/4 OUT, a C55 DISAGREE sector, price confirms with XLV worst on 1d); Technology (no persistent direction).

**Why `no_change` and not Growth→Value:** the Value-in leg is real (Financials + Energy) but the **Growth-out leg fails** — Technology reversed from OUT to IN over the last two sessions rather than persisting out. The Cyclical-out leg does not pair with a confirmed Defensive-in leg either (Healthcare is itself trending out; only Utilities is building). Best framing: a **stagflation-consistent tilt that has not yet organised into a callable regime.**

### ETF flow tape (advisory — 0 rubric points)

| ETF | Net premium dir (5d) | Persistence | DP positioning | Options urgency | GICS agreement | Leaders |
|---|---|---|---|---|---|---|
| **XLE** | inflow +$7.8M | BULLISH | buy-leaning, $18.6M block above mid | clean near-dated call sweeps, ask-side | agree (gross+ETF; **netted silent**) | BTU |
| **XLY** | outflow −$6.4M | BEARISH | thin, no buy block | thin (3 prints, no urgency) | **agree** (netted 4/4 OUT) | LULU, AMZN |
| **XLI** | inflow +$3.5M | BULLISH | neutral-to-buy (1 stale-NBBO print discarded) | small notional, call-leaning | **disagree** (netted flipped today) | held — watch_only |
| **IGV** | outflow −$13.9M | BEARISH | no dominant block | **distribution signature** — calls sold at bid + puts bought at ask, repeated | **disagree** (Tech netted flip-flops) | skip — flags semis-vs-software divergence |
| **GDX** | outflow −$15.9M | BEARISH | buy-leaning $28.2M block above mid — **contradicts the options direction; dominated by a 2028 tail-hedge put, not accumulation** | mixed, hedge-heavy | **disagree** | skip — idiosyncratic gold-miner story |
| EWY | inflow +$22.6M | BULLISH | mixed blocks | call-buying > 2 large longer-dated put blocks | n/a (geographic) | skip |
| SMH | inflow +$28.1M | MIXED | — | — | n/a (rank-only) | — |
| XOP / EWT / XLU / XLRE | small inflow | BULLISH | rank-only | rank-only | XLU building | — |
| XLP / XLC / XLF / XLB | near-flat | MIXED | rank-only | rank-only | n/a | — |
| KRE / XBI / ITB / TAN | small outflow | BEARISH | rank-only | rank-only | n/a | — |

The tape is advisory: ETF DP is a positioning/persistence tell (creation-redemption and hedging), **not** single-name accumulation, and ETF options flow is weighted above ETF DP. It strengthens the conditional sector-leader +1 via `gics_agreement`; it adds no rubric points.

---

## 3. Swing Setups (1–6 weeks)

**Post-gate: empty. Nothing is sized.** Seven names cleared the ≥2-agent confluence gate; all seven finished at `skip` or `watch_only`.

| Ticker | Score | Tier | Thesis | Structure | Invalidation | Final size |
|---|---|---|---|---|---|---|
| LULU | 5 | LOW | Laddered ITM-put synthetic short | Dec-18-26 300/350P ladder | Fundamentals VETO already fired | **watch_only** |
| ROST | 3 | LOW | Short vol into 08-20 print | Defined-risk iron fly, 08-21 | front-end ratio 1.857 ≫ 1.10 | **skip** |
| MU | 2 | DROP | Long gamma on cheapest vol by rank | Long straddle | 7-DTE tenor is the *richest* point on its own curve | **skip** |
| CRWD | 2 | DROP | Put-weighted long vol into 08-26 | 08-28 strangle, 2×200P/1×240C | Name VRP FAIR — no edge either way | **skip** |
| HPQ | 2 | DROP | Long vol into 08-26 | 08-28 strangle ~32C/28P | Name VRP contradicts the thesis | **skip** |
| AMZN | 1 | DROP | Bearish sweep persistence + sector | — | Short-routed | **watch_only** |
| AMD | 1 | DROP | Bullish flow (contested) | — | MU/AMD corr 0.855 | **skip** |

### 3a. Long swings (regime-aligned)

**Empty.** The accumulation book returned **zero** full-conviction candidates. Its two survivors both died on the C11 conjunction:

- **GOOGL** — the cleanest name screened. Three near-identical 500,000-share **mid-day** prints (16:09/16:29/16:39Z, not closing-cross) at $345.05/$345.50/$345.60, all positive vs mid, $518.1M total; mega-tier buy_ratio **0.986**; `institutional-accumulation` = ACCUMULATION with buy/sell 3.22; `oi-trend` BUILDING 5/5 (+471,575). **Failed:** `cum_premium_flow_30d` **−$26.9M MIXED** — wrong sign for a bullish thesis and an order of magnitude below the $50M gate, so the +3 halves to +1. DP shelf for invalidation (C34): **$345.00–$346.10**. `distribution_flag` present (350C 35-DTE, OI −729 on 3,829 volume, ~$4.29M). Only 14% of its mega tier was closing-cross — the best on the board.
- **AAPL** — same shape, worse. Mega buy_ratio 0.876 but **60% closing-cross contaminated**; `cum_flow_30d` **−$114.6M MIXED**. Its `distribution_flag` is larger and more diversified than GOOGL's, including a **399-DTE 400C LEAP unwind** (−1,595, $2.25M). DP level $305.26.

Both failed the ≥2-agent confluence gate as well (accumulation-hunter was their only positive flag).

**Closing-cross contamination was severe today** and had to be segregated before any `buy_ratio` could be read: NVDA **100%**, LITE 100%, MSFT 87.5%, WDC 70%, AAPL 60%, plus SPY/QQQ/SNDK. Raw mega-tier buy ratios on those names are meaningless.

**Sweep ledger (informational — 0 rubric points; the sweep-persistence line was removed 2026-05-23 P0.3).** Ranked by `sweep-persistence`, not single-day size:

| Ticker | Side | Persistence | 5d cum sweep premium | Today's confirmation |
|---|---|---|---|---|
| **PLTR** | Bullish | 4/5 | $717.7M | **Strongest same-day confirm on the board** — 162.5C ask-dominant ~89:1 (ask 9,146 / bid 103) $11.35M + 170C $4.88M |
| AMZN | Bearish | 4/5 | $470.2M | Small but direction-consistent (265C bid-dominant, $2.1M) |
| MU | Bearish | 5/5 | **$3.58B — largest on the tape** | **Near-nil** — only ~85%-OTM Aug-21 lottery puts at $8–10.5K notional, IV 350%+; MU absent from the top-100 premium list |
| AMD | Bullish | 5/5 | $1.0B | **Contradicts** — the single AMD print today is a *bought put* (Aug-21 300P, ask-dominant, $53.7K) |

Mega-cap/index names were filtered on the hedge-flow test and mostly failed it: **NVDA** bearish 5/5 but `cum_flow_30d` skew 0.1% (statistically flat), **QQQ** bearish 5/5 but flow slightly *bullish*, **AAPL** bearish 5/5 but flow bullish-leaning. Only AMZN passed. **SMCI** was disqualified on a genuinely mixed same-day tape (simultaneous large ask-side call buying *and* bid-side call selling) consistent with 0DTE churn.

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only` (2026-08-01 P0 #1).** Routing, not suppression — theses below are fully carried and serialized so the counterfactual keeps resolving.

**LULU — `watch_only` (fundamentals VETO + short routing).** The best-evidenced name on the board, and it still does not trade.
- *Structure:* a laddered ITM-put **synthetic short stock**, Dec-18-2026 (126 DTE). Ask-side puts at 220/230/280/300/350: two $22.06M/$22.18M **350P** clips (delta −0.83/−0.85, size 956, 25 minutes apart), $26.79M **300P** (delta −0.85), plus $13.14M/$11.51M 300P. `expiry-heatmap` confirms Dec-18 premium of $100.58M is **99.96% PUT** ($100.54M put vs $42K call) — explicitly checked for a collar; it is not one. Max loss ≈ $100M gross premium if LULU rallies through 300–350.
- *Flow:* `cum_premium_flow_30d` **−$216.66M at 38.4% of gross** — the **only** name on today's board whose net is not noise-level (every other name sits at 0.2–2%).
- *Sector:* the cleanest netted call of the session (Consumer Cyclical 4/4 OUT, XLY worst on both windows).
- **Why it dies:** `fundamentals-gate` **VETO**. Beat streak 3-of-4; insider MSPR **+78.42** across four separate quarters; **Michael Burry initiated a position on 2026-08-10 — the same week the bearish flow was building**. PE 9.83x, PS 1.29x, margins 55.7% / 18.3% / 13.0%. No tender or M&A found (checked explicitly). This is the gate doing exactly what it exists for: flow that contradicts the underlying on multiple axes.
- *Invalidation:* the short's own risk is earnings **2026-09-02/03** (19 days out, inside the option's life) — a beat on a beat-streak name forces urgent unwinds on −0.85-delta puts.
- *Debate:* bull 0.35 / bear 0.45. **Polarity is inverted on this name** — the bull argued the *short is wrong*, the bear that it is right. Neither advocate cleared a coin flip.

**AMZN — `watch_only` (short routing).** Bearish sweep persistence 4/5 ($470.2M 5d) with the mega-cap hedge-flow filter genuinely passed, plus the Consumer Cyclical netted-out leadership. `win_rate` 0.5188 (n=133, `backtest_clean`) with **`market_excess` +0.0902 — the only positive-excess call on the entire board.** Regime gate −1 (UPTREND vs short). Not debated (outside top-5).

> **Correction carried from the quant:** sweep-tracker justified passing AMZN through its hedge-flow filter using a "1.65% net-bearish skew" ($18.16B vs $17.86B). Those are the **90-day** figures. The true **30-day** window is $7.889B vs $7.826B = **0.40%**, four times weaker — barely above the NVDA reading (0.1%) that the same filter *rejected*. Outcome unchanged (short-routed regardless), but it is a live agent defect.

**AVGO — did not reach the book, and this is the day's most interesting near-miss.** It carried the session's **only** mechanized DEX flip (clean, `whipsaw_warning: false`, FULLY_NEGATIVE GEX holding since 08-10), was the **worst S&P mover (−5.94%)** and the **largest bearish net_flow (−$86.5M)**. It failed the ≥2-agent confluence gate on agent count: `dealer-positioning-strategist` flagged it, but `contrarian-scanner` examined and **explicitly disqualified** it (P/C z −0.439 NORMAL — no crowding leg; the term-structure kink lands on the 08-21 macro stack, i.e. event risk being priced rather than a crowd mispricing), and `vol-surface-scout` found clean CONTANGO with no dislocation. An examine-and-decline is not a positive flag. Even had it passed, it is a short → `watch_only`. **The session's cleanest mechanical signal was disposed of twice over.** Correct under the rules; worth recording.

---

## 4. LEAP Builds (6–24 months)

**Empty pass-list.** `uw oi biggest-increases --min-dte 180` was dominated by index/ETF hedging flow (XLF, HYG, QQQ, GLD, EEM, FXI, TLT, XLE, XLY, XLK, KWEB, IBIT — all out of single-name scope) and a long tail of sub-$8M deep-OTM/ITM noise.

**PLTR — the only candidate with real size, DISQUALIFIED on two *required* gates.**
- Passed: a genuine fresh build — 271217C00180000 (490 DTE, strike 180 vs spot ~174), `oi_diff` **+3,018 (+162%)**, **87% ask-side** (3,690 vs 533), $21.7M premium. `oi-trend` BUILDING 10/10. And `position-rolls` detected **0**, so it is a genuine new open, not a roll.
- **Failed (required):** `cum_premium_flow_90d` **−$68.2M MIXED** — no slow-accretion signature; the single idiosyncratic build is swamped by day-to-day churn. A positive 30d (+$162.7M) atop a negative 90d is reversal noise, not the flat-then-accrete shape the gate requires.
- **Failed (required, hard reject):** `conviction-matrix` returns **HEDGED_LONG at 13.9% confidence** — explicitly "dark pool buying + put protection," one of the two scenarios the spec rejects outright regardless of everything else.
- Gate tally **2 of 9**.

**Disqualified on artifact screen:** **SNDK** — its DTE-854 OI increases sit at strikes 2000–3500 against a spot of 1641, the deep-ITM box/financing signature (same family as its 900C roll). **SPCX** — long-dated legs are small, bid-dominant and mixed put/call. Note the **SPX** box would also surface in a naive DTE>180 screen and is financing, not conviction.

---

## 5. Volatility Surface

**Today is an expiry Friday, so 0DTE contamination is at maximum — and it showed.** `scripts/term_structure_hygiene.py` (min_contracts=15, a **tunable, non-audit-frozen** parameter) **flipped 11 of 15 raw BACKWARDATION labels.** The `dte_approx: 0` bucket carries 250–480% average IV on any expiry-day snapshot and inverts every front-vs-back comparison.

| Ticker | raw_shape | hygiene `shape` | `base_shape` | Verdict |
|---|---|---|---|---|
| **AAP** | BACKWARDATION | **BACKWARDATION** | BACKWARDATION | **SURVIVED — real** |
| **OKTA** | BACKWARDATION | **BACKWARDATION** | BACKWARDATION | **SURVIVED — real** |
| **ROST** | BACKWARDATION | **BACKWARDATION** | BACKWARDATION | **SURVIVED — real** (thin back tenors, 11 dropped) |
| **ARGX** | BACKWARDATION | **BACKWARDATION** | BACKWARDATION | SURVIVED but thin (2 kept / 4 dropped) |
| CRWD · AMD · ADSK · MU · HPQ · AMAT · KR | BACKWARDATION | **KINKED** | CONTANGO | FLIPPED |
| NVDA · AVGO · TSM | BACKWARDATION | **CONTANGO** | CONTANGO | FLIPPED — fully clean |
| LRCX | BACKWARDATION | **FLAT** | FLAT | FLIPPED |

**The session's cleanest vol observation: semis vol is structurally cheap against what semis actually realise.** The index-level negative VRP traces straight into single names — **MU −0.335**, **AMAT −0.253**, **AMD −0.248**, **LRCX −0.233**, TSM −0.0795 — with 30d realised running 78–96% against IV30 of 53–63%. SMH `rv20` is **45.2** while VIX prices **14.25**.

| Ticker | Shape | iv_percentile* | VRP | implied_move | Read |
|---|---|---|---|---|---|
| **LRCX** | FLAT | 2.3 LOW_IV | −0.233 | 10.02% | **Cleanest long-vol substrate — no event kink to fight.** 1 agent only → §8 |
| **MU** | KINKED 7dte/08-21 (prom 38.8%) | 1.15 LOW_IV | −0.335 | 12.15% | Cheapest by rank, but the kink is **OPEX-mechanical, not an event** |
| AMAT | KINKED 14dte (prom 11.8%) | 2.3 LOW_IV | −0.253 | 8.80% | Same family, no earnings in window |
| AMD | KINKED 7dte/08-21 (prom 16.2%) | 13.8 LOW_IV | −0.248 | 9.02% | OPEX kink, not earnings |
| TSM | CONTANGO (real) | 0 LOW_IV | −0.0795 | 5.45% | Cheapest absolute rank; steep clean contango, no dislocation to trade |
| NVDA | CONTANGO (real) | 27.6 NORMAL | −0.013 FAIR | 5.02% | No edge either side |
| AVGO | CONTANGO (real) | 41.4 NORMAL | +0.042 FAIR | 5.85% | No vol panic despite −5.94% |

\* **All percentile reads are PROVISIONAL** — `uw historical iv-percentile-zscore` returned `dates_used: 87` against a 252-day request on **every** ticker, below the ≥120-day bar.

**Genuine event backwardation (not calendar candidates — front-end ratios above 1.10 and rising into real events):** ROST 1.762–1.857 (ER 08-20, VRP +0.167), AAP 1.607 (ER 08-20, implied move 14.3–17.8% — the largest on the board), OKTA 1.415 (ER 08-26). ARGX is the outlier — a BACKWARDATION base label but a near-neutral 1.043 front-end ratio on thin tenors; low confidence, not tradable.

**Skew:** KR and ADSK read TAIL_HEDGING (1.177 / 1.187), HPQ TAIL_HEDGING (1.103); AMD/MU/AVGO/CRWD/AMAT/LRCX/TSM all COMPLACENT (~0.96–1.01); NVDA NORMAL (1.055); OKTA COMPLACENT (0.998).

**IV-rank screens were largely unusable today.** The `--mode high` screen is entirely sub-floor micro-caps and leveraged/inverse ETFs (SOXS at 100, plus sub-$5 names) — no tradeable single-name signal. The `--mode low` screen holds real liquid names pinned at ivr=0 (IBIT, BAC, RKLB, NVO, JPM, WFC, XYZ, U, ECHO, ETHA) — cheap optionality in a premium-buying tape, but none carry earnings inside 14 days.

### Earnings vol calls

| Ticker | Verdict | ER date | DTE | implied_move | Shape (raw→hygiene) | Kink@ER | FE ratio (7d) | Back-skew |
|---|---|---|---|---|---|---|---|---|
| ROST | SELL VOL (half, defined-risk) | 2026-08-20 pm | 6 | ~7.5% | BACKW→BACKW | front *is* the event | **1.857** | 0.0038 COMPLACENT |
| HPQ | BUY VOL | 2026-08-26 pm | 12 | ~11.9% | BACKW→**KINKED** | **yes, 11.4%** | 0.771 | 0.0021 COMPLACENT |
| CRWD | BUY VOL | 2026-08-26 pm | 12 | ~11.2% | BACKW→**KINKED** | yes, 7.7%, whale-confirmed | 0.883 | −0.0256 COMPLACENT |
| ADSK | SKIP | 2026-08-27 pm | 13 | ~10.2% (low conf) | BACKW→KINKED **off-event** | no — 4.2%, sub-threshold | 0.744 | 0.0251 NORMAL |
| OKTA | SKIP | 2026-08-26 pm | 12 | — | BACKW→BACKW | no kink | 1.415 | −0.01 COMPLACENT |
| AAP | SKIP | 2026-08-20 am | 6 | ~14.3% | BACKW→BACKW | front *is* the event | 1.607 | 0.0268 NORMAL |

ADSK is the interesting miss: its earnings tenor scores only 4.2% prominence (sub-threshold) while a real **22.7%-prominence kink sits at 42 DTE / 2026-09-25 with no confirmed catalyst.** Worth a look, not a trade.

**Front-end-ratio population check:** the gate fired BACKWARDATION in exactly the 3 names whose 7-DTE tenor contains the earnings date and CONTANGO in the 3 whose earnings falls in the second tenor — a clean 50/50 split tracking event timing correctly. That is a **real** discriminating read, unlike the near-100% firing rate documented for the `--near-dte 1` degenerate case.

---

## 6. Risk & Correlation

**Macro headline:** stagflationary tilt — core PCE 3.29% sticky against payrolls −23k MoM, ~34bp real policy rate, weakening USD. **Forward calendar:** FOMC minutes T+3, Jackson Hole + monthly OPEX T+5, Core PCE T+8. No clean window.

**Correlation clusters (`uw risk portfolio-correlation`, run against today's candidates, not the static watchlist):**

| Pair | corr | Action |
|---|---|---|
| **MU / AMD** | **0.855** | **CLUSTER** — one semis bet, not two. MU kept (raw 2), **AMD −1 tier** (raw 1) |
| LULU / ROST | 0.522 | below the 0.60 floor — no penalty |
| CRWD / HPQ | below tool floor | **not** upgraded to a cluster despite the same-day-report intuition — that discretion was removed by the 2026-05-15 audit. Surfaced instead as an **event concentration**: both report 08-26, the same session as Core PCE |

> `sector_breakdown` returned `Unknown` for all seven names — the tool's sector tagging is dead this run, so its "100% in Unknown" concentration warning is an artifact, not a signal.

**VRP gate — bound at the name level, not the index.** The two levels disagree today and it is load-bearing: a single-name vol structure's P&L is driven by *that name's* IV-vs-RV spread, while index VRP is backdrop. Binding at the index would have handed HPQ a free pass and penalised ROST for something it does not own.
- ROST short-vol, name VRP **+0.167 PREMIUM_SELLING** → supports → no-op
- **HPQ long-vol, name VRP +0.089 PREMIUM_SELLING → CONTRADICTS → −1 tier**
- CRWD long-vol, name VRP +0.028 FAIR → neutral (and this removes the cheapness support the negative index backdrop would otherwise imply)
- MU long-vol, name VRP −0.335 → supports → no-op

**Panic gate — genuinely discriminating today, 2 of 7 (29%).** Read at `--near-dte 7`, never the default 1: ROST **1.857** (fires), **MU 1.184 (fires)**, AMD 1.06, AMZN 0.937, CRWD 0.883, HPQ 0.771, LULU 0.731.

> **MU's panic reading is a new finding — no Phase 1 agent recorded it**, and it materially changes the name. MU's thesis is *long* the 7-DTE straddle on a kink `vol-surface-scout` itself labelled **mechanical (OPEX), not an event** — and at 1.184 backwardation, that 7-DTE tenor is the **richest point on MU's own curve**. "Cheapest vol by rank" (iv_percentile 1.15) is a *28-day* statement; the tenor actually being bought is not cheap.

**Fundamentals verdicts:** **LULU VETO** (beat streak + insider MSPR +78.42 over four quarters + Burry initiating 08-10 — see §3b). **ROST/MU/CRWD/HPQ all CONFIRM.** ROST carried a **date conflict** — Finnhub returned 08-19, the company's own 2026-08-06 press release says **08-20 postmarket**; `uw insights deep-dive` independently returns **2026-08-20**, so 08-20 is used. A one-day error moves the event from T+3 to T+4 and changes gate severity.

**Event-risk flags:** ROST −0.5 (Jackson Hole *and* monthly OPEX both land on 08-21 = T+5, held through to its 08-21 expiry; its own 08-20 earnings is exempt — that *is* the event play). AMD and AMZN −0.5 each (JH + OPEX at T+5, directional and undefined-risk). CRWD/HPQ no-op (own earnings *is* the play, Core PCE same session, and the long strangle is defined-risk — both exemptions apply). MU no-op (earnings outside; for a long-gamma structure in-window macro is the thesis, not the risk). LULU no-op (126-DTE defined-risk structure; routine macro is ambient).

**Debate-disconfirmation cuts — the gate fired on all five names, which is itself the headline.**

| Ticker | Bull | Bear | Gate |
|---|---|---|---|
| LULU | 0.35 | 0.45 | FIRES *(polarity inverted — see §3b)* |
| ROST | 0.35 | **0.65** | FIRES |
| MU | 0.45 | **0.65** | FIRES |
| CRWD | 0.35 | **0.65** | FIRES |
| HPQ | 0.45 | 0.55 | FIRES |

**Four of five bull residuals came in at or below 0.45 — sub-coin-flip while arguing their own side.** No pair qualified for a second round. All residuals serialize verbatim on the 0.15-floor ladder; nothing was clamped to 0.55.

**Breadth cross-check (advisory):** `fz` 250 advancers / 245 decliners / 8 unchanged, **49.7% green**, average +0.06%, **median exactly 0.00%**; top mover CPRT +7.55%, worst **AVGO −5.94%**. **No classic divergence** — the index is flat-to-red and breadth is ~50%, so price and breadth agree. The tell is the gap between UW **flow** breadth (35.1% bullish) and `fz` **price** breadth (49.7% green). Advisory, 0 points, does not change sizing.

**Adverse-flow / exit candidates:** `conviction_2026-08-13` = {CRWV}. `uw watchlist alerts` fired three times on it (volume spike 1.5×, a $10.5M dark-pool print, OI shift +30,579) — all **thesis-confirming, not adverse**. `uw watchlist scan` shows flow still bullish (+$4.96M, PCR 0.686). **No exit candidates.** One soft observation: CRWV failed to reappear in any Phase 1 agent's output today — decay-by-non-reappearance rather than reversal. It was not re-carried, and that is recorded as a decision rather than an accident.

**Hedge sleeve: none, and that is the answer.** The post-gate book is empty, so net delta is zero and directional skew is undefined — nowhere near the ±0.6 trigger. A hedge sleeve on an empty book is a naked directional bet with a defensive name on it. The 0DTE premium-sell lane is also negative-expectancy in the current VIX tercile (§2a), so stand aside there too.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Empty. No name reached MEDIUM (7), let alone HIGH (9).** The Step-3a 3-of-4 load-bearing-tool gate therefore **no-ops — recorded, not skipped.**

**Expectancy lens** *(advisory — expectancy is not yet a live sizing axis)*: not computed this session. No tier reached MEDIUM or above, and the rolling `conviction_<date>` closed-call set has no resolved rows in the relevant bands. The most recent `/calibration-audit` (2026-08-08) tier expectancies stand unchanged.

### Full scored book (all seven confluence-gate passers)

Nothing here was sized. Reproduced in full so the counterfactual resolves.

**1. LULU — raw 5, LOW, `multileg_directional`, final `watch_only`**
```
+2  multileg directional structure   | multileg-strategist | uw hot-chains multileg
+1  cum-flow net accretion (30d)     | signal-confluence-quant | uw historical cumulative-premium-flow
+1  sector-rotation single-name lead | sector-rotation-strategist | uw risk market-regime
+1  multi-day OI build (BUILDING 5d) | signal-confluence-quant | uw historical oi-trend   [SESSION CONSTANT]
 0  flow_conflict — aligned bearish at 4.6× union median, no deduction
Σ = 5 ✓
```
`cum_flow_30d` −$216,659,349 / `90d` −$79,286,229 · `win_rate` NA(substrate) · `market_excess` null · fundamentals **VETO** · debate 0.35/0.45.
**Double-count disclosed:** the sector-leader +1 and the cum-flow +1 test the *identical field at the identical $50M threshold*, with a non-discriminating persistence gate (a). De-duplicated LULU is raw 4; also de-constanted for the OI line, raw 3. Neither correction changes the tier band or the routing.

**2. ROST — raw 3, LOW, `earnings_vol`, final `skip`**
```
+1  earnings-scout SELL VOL          | earnings-scout | uw screener earnings-catalyst
+1  vol-surface BACKWARDATION, VRP-aligned | vol-surface-scout | uw options-structure term-skew
+1  multi-day OI build               | signal-confluence-quant | uw historical oi-trend   [SESSION CONSTANT]
Σ = 3 ✓
```
`implied_move` 7.5 · `win_rate` NA(substrate) · fundamentals CONFIRM · debate 0.35/0.65 · gates: **panic (1.857)**, debate, event −0.5, rubric_regime.
The `earnings_vol` 0.55 class ceiling never binds because there is no number to cap — the class is genuinely unsupported by `signal-backtest`. Both of earnings-scout's *own* disqualifiers were active (front-end ratio 1.857 vs its 1.10 bar; flat back-skew = zero tail cover).

**3. MU — raw 2, DROP, `event_vol`, final `skip`** — `+1` vol-surface KINKED VRP-aligned, `+1` OI constant. `cum_flow_30d` +$684,943,179 (but only **1.03% of $66.8B gross** — noise at MU's scale). `implied_move` 12.15. debate 0.45/0.65. Killed by the panic gate at 1.184 plus the debate gate.
> **Class mapping disclosed:** the quant's working label was `vol_long`, which is **not** in the schema's canonical class list. It serializes as the nearest canonical bucket, `event_vol`. **A future audit must not read this as an earnings trade** — MU has no earnings inside the structure's life (next print 2026-09-21/22, 38 days out); the "event" anchoring it is the 08-21 OPEX kink, which `vol-surface-scout` itself called mechanical. `high_iv_rank` would have been actively wrong (MU is LOW IV: percentile 1.15, iv_rank 32.4) and would have wrongly attracted that class's 0.60 ceiling. Recorded so the collapse is auditable rather than silent.

**4. CRWD — raw 2, DROP, `earnings_vol`, final `skip`** — `+1` earnings-scout BUY VOL, `+1` OI constant. The vol-surface line was **not** awarded: name VRP +0.028 FAIR is not a VRP-aligned bias. `cum_flow_30d` −$20,206,010 / `90d` +$61,540,857 — **signs disagree**. `implied_move` 11.2. debate 0.35/0.65.

**5. HPQ — raw 2, DROP, `earnings_vol`, final `skip`** — `+1` earnings-scout BUY VOL, `+1` OI constant. Vol-surface line **not** awarded: name VRP +0.089 PREMIUM_SELLING points opposite to the BUY VOL thesis. `implied_move` 11.9. debate 0.45/0.55. Best *structural* kink on the board (11.4% prominence), killed by having only one scoring line that is not the session constant.

**6. AMZN — raw 1, DROP, `bearish_flow`, final `watch_only`** — `+1` sector-leader, `+1` OI constant, **−1 flow_conflict_lite**. `win_rate` **0.5188** (n=133, `backtest_clean`), **`market_excess` +0.0902**. The quant declined the +1 cum-flow accretion line here on the record: a flow cannot be both "net directional accretion" and "MIXED" on the same field in the same window. Residual incoherence noted — the sector-leader line pays +1 on the same MIXED flow that costs −1 as `flow_conflict_lite`, a self-cancelling wash scored twice in opposite directions.

**7. AMD — raw 1, DROP, `bullish_flow`, final `skip`** — `+1` vol-surface, `+1` OI constant, **−1 flow_conflict_lite**. `win_rate` **0.4848** (n=132), **`market_excess` −0.0909 → `beta`, not edge.** `|cum_flow_30d|` $47.185M *is itself* today's union median, so the −3 test fails on strict inequality; cross-checked against the $50M phrasing, which also gives −1. Both phrasings agree, so the self-referential median is not load-bearing.

### Conviction-scoring rubric (Step 4) — verbatim, version `2026-06-12` (FROZEN)

```
Daily conviction score = Σ:
  +1  MECHANIZED DEX flip or vanna-squeeze in trade direction — verified SIGN CHANGE, never a level.
      sign(net_dex) latest session opposite to ≥3 consecutive prior sessions; |net_dex| on the flip day
      ≥ 0.25× the trailing-10-session median |net_dex|; computed by scripts/dex_flip.py, never by hand.
      Vanna disjunct additionally requires a dated VIX source for the falling-VIX leg.
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified
      institutional tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms
      (sign aligned AND |cum_flow_30d| ≥ $50M); else halved (floored) +3 → +1.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: award only when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +1  uw historical cumulative-premium-flow net directional accretion in trade direction (30d) —
      INTENT-SCREENED: only when (a) no C28 distribution_flag on the name, AND (b) on dividend payers in
      an ex-div window the accreting prints are NOT deep-ITM sub-parity calls.
  +1  sector-rotation-strategist names ticker as single-name leader in a rotating sector — CONDITIONAL:
      (a) sector persistence_score ≥ 0.6 AND (b) cum_premium_flow_30d direction aligned AND
      (c) |cum_flow_30d| ≥ $50M. Default 0.
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored play type)
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags overcrowded long with rising pc-ratio-zscore (VRP positive) — an INFORMED-
      FLOW CONTINUATION penalty, not a "crowd is wrong, fade it" signal.
  -3  flow_conflict — applied mechanically when cum_premium_flow 30d direction is clearly opposite
      dominant_signal_class (signed-sum sign flip + magnitude > today's union-median |cum_flow_30d|,
      or explicit OPPOSITE label).
  -1  flow_conflict_lite — when the 30d read is MIXED (signed sum near zero, or aligned but
      bottom-quartile magnitude in today's union).
      # -3 and -1 are MUTUALLY EXCLUSIVE — apply ONE, never both.
  # The two lines below are risk-monitor TIER gates applied in Step 2d. They contribute 0 to raw_score
  # and never appear in score_components:
  -1  [TIER GATE] correlation cluster (pairwise corr ≥ 0.70) — −1 TIER
  -3  [TIER GATE] market-regime conflicts with trade direction — −1 TIER
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | HIGH | full (subject to the Step-3a load-bearing gate + win-rate gate) |
| 7–8 | MEDIUM | half (subject to win-rate gate) |
| 3–6 | LOW | starter / watch-only |
| ≤ 2 | drop | filtered by the quant's drop floor |

**Deep-dive hand-off:** skipped — no HIGH-tier names. **Batched strategy synthesis (`uw playbook batch-scan`):** skipped — no name at raw_score ≥ 7.

---

## 8. Watch-only — single signal, no confluence

Journaling only, **not for trade entry today.** Every name below was flagged by exactly one Phase 1 agent, or was examined and declined.

| Ticker | Flagging agent | Why it stopped here |
|---|---|---|
| **AVGO** | dealer-positioning-strategist | The session's **only mechanized DEX flip** (clean, no whipsaw, FULLY_NEGATIVE GEX held since 08-10), worst S&P mover −5.94%, largest bearish net_flow −$86.5M. contrarian-scanner and vol-surface-scout both examined and declined. Short → `watch_only` regardless. |
| **GOOGL** | accumulation-hunter | Cleanest DP/OI stack of the day (mega buy_ratio 0.986, only 14% closing-cross, ACCUMULATION 3.22, BUILDING 5/5) but C11 conjunction fails on −$26.9M MIXED cum-flow. DP shelf $345.00–$346.10. |
| **AAPL** | accumulation-hunter | Same shape, 60% closing-cross contaminated, cum-flow −$114.6M. Distribution flag includes a 399-DTE LEAP call unwind. |
| **NVDA** | multileg-strategist | Real term-structure-anchored structure: four Aug-21 calls (227.5C $21.16M, 230C, 235C, 237.5C) with confirmed **bid-side selling** at 227.5C = call spread/condor sold for range income, deliberately built in the vol **trough before** the Aug-28 earnings kink. `repeat_count` 2 — the strongest multi-day structural evidence of the session. The two other agents that looked at NVDA both declined. |
| **PLTR** | sweep-tracker | Strongest same-day sweep confirmation on the board; leap-radar hard-rejected the long-dated leg on two required gates. |
| **LRCX** | vol-surface-scout | The cleanest long-vol substrate on the board (FLAT post-hygiene — **no event kink to fight**, VRP −0.233, iv_pct 2.3). One flag only. |
| **AMAT / TSM** | vol-surface-scout | Same semis-cheap-vol family. |
| **APP** | multileg-strategist | Synthetic-short-via-ITM-puts family (1110P Jan-2027 ×2 + 500P Sep + 440/400P Aug), but ambiguous `side` tagging means a SNDK-style roll cannot be ruled out. Gross put buying (~$40M+) exceeds the −$17.4M net figure. |
| **SYF / IVZ / CIFR / BTU** | sector-rotation-strategist | Sector leaders on one flag. CIFR is GICS-tagged Financials but functionally a bitcoin miner. |
| **OKTA / AAP** | vol-surface-scout | Real post-hygiene BACKWARDATION, but earnings-scout returned explicit **SKIP** on both. |
| **ARGX** | vol-surface-scout | BACKWARDATION on 2 kept / 4 dropped tenors; front-end ratio only 1.043. Low confidence. |
| **ADSK** | *(none)* | Examined by both vol agents, flagged positively by neither. Qualifying kink is at 42 DTE with no catalyst; the earnings tenor is sub-threshold at 4.2%. |
| **SPCX** | multileg-strategist | **Not directional.** multileg corrected the framing: a **zero-cost collar** invisible to every net-premium screen (10,000-lot 125P $32.2M + 10,000-lot 185C $31.2M, same Jan-2028 expiry, identical timestamp). Its −$31.7M net_flow should not be read directionally. |
| **SMCI / ORCL** | *(none)* | SMCI disqualified on a mixed same-day tape (simultaneous ask-side call buying and bid-side call selling); ORCL 3/5 persistence but thin confirmation ($522K). |
| **SNDK** | *(none)* | **Disqualified by four agents independently** — see below. |

### Tape artifacts — the funnel's top two bullish lines were both financing

**SNDK (+$166.4M, the #1 single-name bullish net_flow) is a CONFIRMED DEEP-ITM ROLL.** SELL 1,500× Aug-14 0DTE 900C @ bid $107.63M (delta 0.989) against BUY 1,500× Aug-28 900C @ ask $107.95M (delta 0.985) — same size, same strike, same underlying tick (1615.7), **identical timestamp 15:26:08Z**. Net premium delta **+$322K on $215M gross notional**. A deep-ITM stock-equivalent position extended two weeks out of an expiring bucket — not a fresh bullish bet. Independently corroborated: accumulation-hunter found mega-tier buy_ratio **0.017** (98.3% SELL); dealer-positioning found the 5d DEX swing tracks the roll; leap-radar found 854-DTE OI at strikes 2000–3500 against spot 1641. **Nets to flat.**

**SPX (+$408.6M) is a BOX SPREAD / SYNTHETIC FINANCING.** ~15 clips of 200 contracts each, Feb/Mar-2027 4700C and 4750C — strikes **40% below** a 7,782 spot, delta 0.97–1.00 — printed across ask, bid *and* mid within a 20-minute window (19:13–19:33Z). Deep-ITM near-delta-1 options have negligible vega, so the quoted 27–38% "IV" is noise off intrinsic value, not a vol signal; boxes price off rate differentials. **Index call premium must not be read as bullish today.**

Both are the same lesson: **net before believing.** Check the `side` field and look for offsetting legs before treating a net-premium figure as conviction.

---

## Substrate defects observed this session

Logged for `/calibration-audit`. Several are new.

1. **`oi-trend BUILDING` fired 14 of 14 names** — a pure session constant. Every raw score in §7 carries one point of noise; de-constanted the board is LULU 4 / ROST 2 / everything ≤1. Fourth documented instance of the C47 zero-discrimination family.
2. **`sector-flow-persistence`: 11 of 11 sectors INFLOW, 10 of 11 at 1.0** — ~100% population firing, zero discrimination. Third documented instance.
3. **Raw BACKWARDATION labels: 11 of 15 flipped under hygiene** on this expiry-day snapshot. Only AAP/OKTA/ARGX/ROST survived.
4. **NEW — `screener earnings-catalyst.implied_move_perc` is broken for this cohort.** It reads 5–15× too small (ROST 0.047%, HPQ 0.58%, AAP 2.0%) versus IV-derived straddle approximations (ROST ~7.5%, AAP ~14.3%). Flagged **independently by both earnings-scout and vol-surface-scout**, and reconfirmed by `uw insights deep-dive` (LULU 0.0037%, ROST 0.0047%, MU 0.0050%). Looks like a units/expiry-selection bug. Worth a substrate ticket.
5. **NEW — `uw insights analyst-vs-flow` returned no analyst-rating data for any of the 6 earnings names** — only a duplicate `options_flow` block. Read as *unmeasured*, not "no divergence."
6. **`iv-percentile-zscore` returned `dates_used: 87` against a 252-day request on every ticker** — below the ≥120-day bar. All percentile reads are provisional. (Known defect, reconfirmed.)
7. **The sector-leader +1 duplicates the cum-flow +1 by construction** — same field, same $50M threshold, with a non-discriminating gate (a). Fired on both LULU and AMZN; on AMZN it pays +1 on the exact flow that costs −1 as `flow_conflict_lite`.
8. **`fz` doubled-first-letter ticker bug is LIVE again on the `screen` surface** (AABCL=ABCL, AAEHR=AEHR, CCLYM=CLYM, QQMCO=QMCO, SSGMT=SGMT, HHTFL=HTFL). The `fz_enrich` path was clean for all five top-5 names. Advisory lanes only.
9. **Closing-cross leak (20:00–20:26Z at exact closing price) dominated the mega DP tier** — NVDA 100%, LITE 100%, MSFT 87.5%, WDC 70%, AAPL 60%. Must be segregated before reading any `buy_ratio`.
10. **ZGL-grid artifact reconfirmed** on IWM (ZGL 150–215 vs spot ~305) and on SPY/QQQ NEGATIVE-regime days.
11. **`pc-ratio-zscore` still has no `--date` flag**, so the −2 overcrowded-long line's "rising" clause remains structurally unsatisfiable.
12. **`portfolio-correlation.sector_breakdown` returned `Unknown` for all 7 names** — its concentration warning is an artifact.
13. **NEW — sweep-tracker window error:** it justified AMZN's hedge-flow pass with a "1.65% skew" that is the **90-day** figure; the 30-day window is 0.40%, four times weaker.
14. **`volume-vs-average` was unusable** — almost entirely sub-floor micro-names (WHG at a 3,673× ratio on 1,347 contracts).
15. **NEW — the canonical `dominant_signal_class` list has no bucket for a delta-neutral long-vol trade with no event.** MU's honest label is `vol_long`; the schema's 17 canonical values offer only `earnings_vol` (no earnings), `high_iv_rank` (MU is LOW IV — and that label would wrongly attach a 0.60 ceiling) or `event_vol` (the "event" being a mechanical OPEX kink). It was serialized as `event_vol` with the mapping disclosed in `key_risks`. Three of today's seven names also returned `NA(substrate)` because `earnings_vol`, `multileg_directional` and `vol_long` are **not among the five classes `signal-backtest` supports** — the vol lane is structurally unmeasurable, not merely unmeasured.

---

## Watchlist write-back

`uw watchlist manage --action add --group conviction_2026-08-14 --tickers ROST` — **CONFIRMED**, verified via `--action list`.

LOW-tier-or-better was {LULU, ROST}; **LULU excluded as VETO'd**, leaving **{ROST}** alone. The write-back rule is tier-based, not size-based (its purpose is tomorrow's correlation and adverse-flow loop), and with ROST reporting at T+4 that measurement is genuinely useful. DROP names were **not** written — they poison the correlation loop. LULU's counterfactual is preserved through `decision.json`, not the watchlist. CRWV was not re-carried (see §6).
