# Daily Market Analysis — 2026-07-31

## Executive Summary

- **Regime + GEX state:** `TRANSITIONAL — mixed signals` on an `UPTREND` trend label. SPY 747.03, clinging to its 20-SMA (745.69) and 50-SMA (744.99), flat over 30 days (+0.17%). **SPY gamma flipped POSITIVE today after seven straight FULLY_NEGATIVE sessions — fresh and unstable.** QQQ sits on the zero-gamma line (total_gex −$2.19M, ZGL null). VIX 15.99, −6.44% on the day and −13.94% over five. Flow breadth 34.1% bullish; `fz` breadth 43.94% green (221 adv / 281 dec) with **divergence_flag TRUE**. Sector lean: no durable rotation — `no_change`.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** **SPY** — POSITIVE / ZGL 746.93 (0.02% from spot, reliable) · call wall **748**, put wall **730** · long-gamma pin, but the call wall is 1 point away, so the iron fly must be tight, not wide. **QQQ** — FULLY_NEGATIVE label on a total_gex of just −$2.19M with a mixed-sign strike grid · ZGL null / unreliable · call wall 688 (at spot), put wall 680 · coin-flip regime, size down. Advisory, see §2.
- **Top swing build:** **NONE.** The post-gate book is flat.
- **Top LEAP candidate:** **NONE.** `leap-positioning-radar` returned an empty book (LEAP share is 2.6% of market volume).
- **Biggest risk:** not a correlation cluster in our book — we have no book. It is what the tape is telling us and we cannot trade: **four independent, defined-risk, institutional bearish structures all expiring 2026-08-07 (NFP)** — IWM Aug-07 285P/275P (4-session repeat, strikes ratcheting down, size 48k→119k), QQQ Aug-07 660P/645P, plus Tier-1 opening puts in MRVL (P215, 7 DTE) and AMD (P440, 10 DTE) — while `vol-surface-scout` independently found a genuine interior IV kink at **exactly 7 DTE = 2026-08-07** on QQQ, SMH, TSLA, MU *and* GOOGL. Flow geometry and the vol surface point at the same date without being derived from each other. Both index structures failed the confluence gate, so neither is a scored call. **Hedge sleeve: if the desk carries discretionary long exposure into 8/07, mirror the institutional structure (QQQ Aug-07 660/645 put debit vertical or IWM 285/275) sized strictly to external book delta.**

**Today's real story is the tape framing, not the book.** SPY +0.72% and QQQ +0.65% are cap-weighted illusions: **equal-weight RSP closed −0.17% and small-cap IWM −0.48%.** AMZN (+15.32%), GOOGL (+6.73%), MSFT (+3.02%) and NVDA (+2.93%) carried the index while AAPL (−7.35%), MU (−5.90%), SNDK (−5.09%), COIN (−10.59%) and RDDT (−20.99%) were taken apart. This is dispersion, not a rally — and reading the green index without the OHLC would have produced the opposite framing.

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Guidance: half position sizes, defined-risk structures, iron condors in range. Trend label UPTREND. SPY 747.03, above both SMAs but by only 0.18% / 0.27%; −1.76% from the 90-day high; +0.17% over 30 days. Flow breadth: 2,142 bullish vs **4,138 bearish** tickers = 34.1% bullish.

### Per-index gamma (EOD current-state; §2 carries the forward read)

| Index | Spot | Zero-gamma | ZGL reliable | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|---|
| SPY | 747.06 | 746.93 | ✅ (0.02% from spot) | +$1.19B | POSITIVE | **748** (+$280.2M) | 730 (−$104.7M) |
| QQQ | 687.99 | `null` | ❌ | **−$2.19M** (≈ zero) | FULLY_NEGATIVE (label suspect) | 688 (+$94.1M) | 680 (−$69.7M) |
| IWM | — | — | — | — | swing read only (§2a) | — | — |

SPY's regime is **one day old**: FULLY_NEGATIVE for seven consecutive sessions (07-22 → 07-30, total_gex −$370M to −$2.8B) before today's flip. QQQ has had three regime flips in 30 sessions and its "FULLY_NEGATIVE" label rests on a total_gex of −$2.19M against a grid holding 29 positive and 21 negative strikes — a marginal-sign artifact, not a conviction short-gamma book.

### DTE volume share (`uw options-flow dte-volume-share`, MARKET-level)

| 0DTE | Weeklies | Monthlies | LEAPs |
|---|---|---|---|
| **48.2%** | 21.4% | 14.8% | 2.6% |

`regime_hint: RETAIL_DRIVEN`. Monthly+LEAP share is only 17.4% — institutional positioning share is thin, which uniformly downgrades swing and rotation conviction today.

### VRP (`uw historical vrp`)

| Symbol | IV30 | Realised σ30 | VRP | Regime |
|---|---|---|---|---|
| SPY | 13.08% | 12.80% | **+0.29pp** | FAIR — no edge from vol alone |
| QQQ | 22.65% | 25.88% | **−3.23pp** | **NEGATIVE** — realised exceeds implied |

The Nasdaq complex is realising more than it implies. That makes short-premium structures in large-cap tech a fight and long-premium/debit structures the correct side — a point that independently corroborates the institutional QQQ put *debit* spread in §2a.

### Macro backdrop (`scripts/fred_macro.py`)

Yield curve **normal** (10Y−2Y +0.47) · core CPI **2.81%** YoY · **core PCE 3.29%** YoY (still well above target) · unemployment 4.2% · payrolls **+57k** (soft) · 10Y **4.68% and rising** (+24bp/30d) · USD weakening · fed funds 3.63%.

A soft-payrolls / sticky-core-PCE / rising-10Y combination is the least comfortable backdrop for long-duration equity risk, and it is the standing argument against any 12–24 month bullish LEAP — moot today, since the LEAP book is empty.

### Forward event risk (Tier-1 in the next ~10 trading days)

| Event | Date | Trading days out | Impact |
|---|---|---|---|
| ISM Manufacturing PMI | 2026-08-03 | T+1 | medium |
| JOLTS | 2026-08-04 | T+2 | medium |
| ISM Services PMI | 2026-08-05 | T+3 | medium |
| **Nonfarm Payrolls** | **2026-08-07** | **T+5** | **TIER-1** |
| **CPI** | **2026-08-12** | **T+8** | **TIER-1** |
| **PPI** | **2026-08-13** | **T+9** | **TIER-1** |

FOMC met 2026-07-28/29 — just passed; none inside the window.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — built from open interest that persists overnight — read forward as the prior for the next session's open. Prose-only, **0 rubric points**, no backtested predictive claim. Predictive validation lives in `/weekly-analysis`'s rolling §2 backtest. Scope: **SPY and QQQ only.**

### SPY — long-gamma pin, but freshly flipped

Spot **747.06** · ZGL **746.93** (`zgl_reliable: true` — 0.13 points, 0.02% from spot) · regime **POSITIVE** · total_gex **+$1.19B** · call wall **748** (+$280.2M) · put wall **730** (−$104.7M).

Spot is essentially pinned *at* the zero-gamma level with a large positive-gamma cluster stacked immediately overhead (746: +$182M · 747: +$505M · 748: +$280M). Textbook long-gamma pin — dealers buy dips and sell rips inside 746–750, suppressing realised range.

**Structure bias:** long-gamma with walls *tight* → **iron fly / short straddle centred ~747, narrow wings (748/746 short strikes)**, or a butterfly body at 747–748. **Do not size a wide condor** — the call wall is one point away and there is no meaningful edge past it.

**Regime freshness: FRESH AND UNSTABLE.** SPY printed FULLY_NEGATIVE for seven straight sessions (07-22 → 07-30) before flipping POSITIVE today. One session of positive gamma after a full week of trend-regime negative gamma is fragile; a single soft print flips it back and unpins the tape.

### QQQ — sitting on the flip line, low confidence

Spot **687.99** · ZGL **`null`** (`zgl_reliable: false`) · regime label **FULLY_NEGATIVE** but total_gex is only **−$2.19M** · call wall **688** (at spot) · put wall **680** (−1.2%).

Treat the FULLY_NEGATIVE label as a marginal-sign artifact, not a regime read: the per-strike grid holds 29 positive vs 21 negative strikes with large magnitudes on both sides (688: +$94.1M, 680: −$69.7M). With total_gex effectively zero and no resolvable ZGL, spot-vs-wall is the only usable signal — spot sits directly on the call wall with the put wall 8 points below.

**Structure bias:** ambiguous / near-flip → **smaller size**; favour a long straddle or a genuinely wide iron condor with shorts outside 680/688, rather than committing to a pin or a directional debit vertical. If early flow confirms a clean positive flip, tighten toward the wider condor; if it confirms negative, treat **680 as the downside acceleration level**.

**Regime freshness: whippy.** Three flips in 30 sessions; NEGATIVE/FULLY_NEGATIVE almost continuously since 07-22. Consistent with this week's mega-cap earnings dispersion — a book that cannot hold a stable regime.

### Mandatory caveats

- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and recomputes both ZGL and walls. This matters most for QQQ, whose total_gex is thin enough to flip sign on light opening flow alone.
- **ZGL reliability.** SPY's is trustworthy (0.02% from spot). QQQ's is `null` and the regime label itself is suspect.
- **Gap risk voids the prior.** Monday 08-03 carries only a medium-impact ISM Manufacturing print and no Tier-1 catalyst until NFP on 08-07, so gap risk into the open is comparatively low — but SPY's 1-point spot-to-call-wall distance and QQQ's flip-line ambiguity mean even a modest gap invalidates the walls.
- **Tooling limit.** `uw options-structure gex --dte-max 1` errors — this is the standing 0–45 DTE book, the best available proxy for the next-session prior, not the isolated D+1 expiry.
- **ETF book**, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py`)

The GEX walls above are a **map, not a pin** — wall-as-magnet backtested NO_GO, as did every directional 0DTE signal. What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, and explicitly not a guaranteed edge: the validation sample contains no vol shock, so the short-vol left tail is **UNSAMPLED**.

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` / VIX | LOW / 15.99 | LOW / 15.99 |
| `implied_move_pct` | 0.49% | 0.97% |
| `expected_range_pct` | 0.79% | 2.01% |
| `size_scalar` | **0.5** | **0.5** |
| Suggested structure | iron fly / short straddle centred 747.07, wings ≈ ±0.79% (long-gamma: quieter, mean-reverting) | wider iron condor, wings ≈ ±2.01% (short-gamma: wider range / trendier) — or reduce / stand aside |
| `stand_aside_reason` / `caution` | none | none |
| Rolling backtest verdict | `GO_PREMIUM_SELL_INTRADAY` (n=60, win 90.0%) | `GO_PREMIUM_SELL_INTRADAY` (n=60, win 86.7%) |
| **mean PnL open — GROSS** | +0.248% | +0.382% |
| **mean PnL open — NET of cost** | **+0.148%** | **+0.282%** |

`pnl_basis`: **percent-of-underlying-spot-notional, GROSS** — not premium-collected, not margin-relative. Round-trip cost assumed 0.10%. **Lead with net.** Vilkov (2024) found an unconditional 0DTE condor flips to negative net Sharpe once costs are charged, so the gross win-rate overstates a negatively-skewed seller's edge.

- **When:** enter at/after the open once the overnight gap resolves; **hold the 0DTE to the close; never carry overnight** (overnight entry backtested at +0.04% SPY / **−0.086% QQQ** — the gap erases the edge). If it gaps beyond the wings, stand aside.
- **Size:** `size_scalar` 0.5 on both — VIX in the LOW tercile (bounds 16.7 / 18.1) is the thin-edge state (mean PnL LOW 0.073% vs MID 0.336% on SPY).
- **Direction:** none. Delta-neutral. Do not add a tilt.
- **SPY ≈ SPX** (validated identical — trade either). **QQQ is weaker** (Nasdaq index book unavailable) — flag its lower confidence, and note QQQ's own worst day in sample was −2.453%.

**Promotion bar:** this lane stays advisory / 0 rubric points **permanently** until *both* a vol-shock day enters the sample and net expectancy clears a tail-aware bar. Win-rate is explicitly not the promotion metric.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

`dealer-positioning-strategist` ran the mechanized `scripts/dex_flip.py` test across 11 symbols. **Five qualified** — but read the whipsaw column before trusting any of them.

| Symbol | Direction | Magnitude ratio | Sign changes | Whipsaw | Swing bias |
|---|---|---|---|---|---|
| SPY | long | 2.28× | 1 | No | **NEUTRAL/CONFLICTED** (vanna disagrees) |
| AAPL | short | 2.32× | 1 | No | SHORT (med-high) |
| RDDT | short | **15.43×** | 3 | No | SHORT (med-high) |
| COIN | short | 6.14× | 4 | **YES** | SHORT (LOW confidence) |
| MRVL | long | 1.59× (thin) | 3 | No (at threshold) | LONG (LOW confidence) |

**Non-qualifiers, with the script's own reasons:** QQQ (no sign change — still negative every session, but trajectory collapsing fast toward a flip: −65.0B → −7.8B → −6.3B), IWM (flat/oscillating), **AMZN** (0-session prior run — today's +$15.8B is a *level* continuing from 07-30, not a flip; whipsaw TRUE), **MU** (prior opposite-sign run is 1 session, needs ≥3; whipsaw TRUE, 4 sign changes), GOOGL (0-session prior run), SNDK (0-session prior run).

The AMZN and MU exclusions are the point of mechanizing this line: both would have been hand-scored as flips on a level read, which is precisely the 2026-06-11 failure the P0.4 demotion was written to stop.

**Vanna-squeeze flags (put-heavy book + falling VIX):** QQQ (net_vanna +35,050, put/call ≈1.4×) and **IWM (net_vanna +82,036 — the strongest put-heavy skew in the set, put/call ≈2.9×)**. Both read LONG. Note the VIX leg carries an asterisk: the strict "≥3 consecutive down closes" test fails — 07-29 spiked to 20.66, breaking the streak; only 07-30→07-31 are consecutive declines. The 5-session net (−13.94%) is unambiguously down, but it is a net decline through a spike, not a clean grind.

**Front-end IV panic (`--near-dte 7`, hygiene-corrected):** SNDK **1.299** (highest on the board) · MU 1.198 · AMZN 1.195 · AAPL 1.181 · RDDT 1.116 · QQQ 1.073 · GOOGL 1.055 · MRVL 1.053 · COIN 1.025 (flat) · IWM 0.943 · SPY 0.900.

**Substrate warning worth registering:** raw `front-end-iv-ratio` at its default `--near-dte 1` returned **1.611 (SPY) / 1.696 (QQQ) / 2.047 (CRWV)** — all nominally past the 1.10 panic threshold — because `near_dte_actual` snapped to 0 on an expiry-day snapshot. Hygiene-corrected, the same three read **0.90 / 1.073 / 0.98**. Firing a panic gate off the raw number on a day VIX fell 6.4% would have been a substrate error, not a risk read.

---

## 2b. Sector Rotation

**Rotation regime call: `no_change` (low confidence).**

### The turnover trap, caught twice

`uw options-flow sector-flow` and `sector-flow-persistence` report **turnover, not direction** — their `net_flow` is gross call premium minus gross put premium, which is sign-agnostic about the aggressor. Today they disagree violently with the aggressor-classified tape on the same session:

| Sector | Turnover metric (gross call$−put$) | Aggressor-CLASSIFIED | ETF options flow (5d) | Verdict |
|---|---|---|---|---|
| **Technology** | persistence 1.0, **+$2.78B** | **−$187.7M OUTFLOW** | XLK +$2.9M (≈flat); SMH mixed, top sweep a **$51.7M 2027 LEAP put** | **Turnover trap** — not rotation-in |
| **Financial Services** | persistence 1.0, **+$499.6M** | **−$17.9M OUTFLOW** | XLF −$0.7M mixed; KRE −$3.3M bearish | **Turnover trap** — not rotation-in |
| Consumer Cyclical | 0.8 OUTFLOW trend, +$1.84B today | +$86.4M INFLOW | XLY +3.29%/+6.11% | **100%+ = AMZN alone** (+$89.6M, more than the whole sector) |
| Communication Services | 0.8 INFLOW, +$656.3M | +$38.0M INFLOW | XLC +1.56% price but **options net BEARISH −$1.45M** | **>100% = GOOG+GOOGL** ($69.1M combined); GICS/ETF disagree |
| **Industrials** | **0.8 OUTFLOW (4/5d)**, −$171.0M | **−$20.9M OUTFLOW** | XLI **−$4.7M bearish**; $162.1M block @ 20:01Z | **Only 3-way corroborated call** |

Both mechanical "standouts" are false positives. The one sector where three differently-biased sources agree is **Industrials, rotating out** — and even that had **no qualifying single-name leader**: only SPCX (−$8.56M) and POWL (+$4.24M) surfaced, and neither is remotely near the $50M / 30-day cum-flow gate. **The conditional sector-leader +1 was awarded to no ticker today.**

`persistence_score` is a **0–1 sign-consistency scale** (≥0.6 ≈ 3-of-5 days), not a 0–5 count. Six sectors tied at 1.0 — saturated and non-discriminating.

### ETF flow tape (advisory — 0 rubric points)

Top-3 inflow / top-3 outflow from the 21-ETF universe (33 `uw` calls, within the ≤40 cap):

| ETF | Net premium dir | Net flow (5d) | DP positioning | Options urgency | GICS agreement | Leaders |
|---|---|---|---|---|---|---|
| SMH | **mixed** | +$52.6M (largest gross, sign-inconsistent) | Mixed blocks $12.5–41M — creation/redemption noise, not accumulation | **$51.7M 2027 LEAP put** dominates — defensive | **disagree** | — |
| XOP | inflow | +$5.4M | thin ($1.8–4M) | thin, LEAP calls, low urgency | n/a | — |
| IGV | inflow | +$5.3M | modest buy-tilt | small, balanced | n/a | — |
| **XLI** | **outflow** | **−$4.7M** | **$162.1M single block @ 20:01Z** — positioning tell | thin ($360K call sweep) | **agree** | none clear the gate |
| **XLE** | outflow | **−$8.5M** | balanced, one sell-aggressive print | thin | disagree | — |
| **GDX** | **outflow** | **−$17.6M (largest)** | $45.9M / $22.2M near-mid, aggressor inconclusive | call selling on bid at $75/$79 — hedge/overwrite tilt | n/a | — |

ETF DP is a positioning/persistence tell (creation-redemption and hedging), **not** single-name accumulation; ETF options flow is weighted above ETF DP. The tape strengthens the existing conditional sector-leader +1 and adds **no rubric points**.

**Retail-tape downgrade:** 48.2% 0DTE share uniformly downgrades all rotation conviction to **tactical-only**, including the Industrials call.

---

## 3. Swing Setups (1–6 weeks)

### **The post-gate book is FLAT. There are no swing setups today. This is the 20th consecutive empty conviction board.**

Five names cleared the Step-3 confluence gate (≥2 distinct Phase 1 agents flagging positively). Four are shorts; one is a direction-neutral vol structure. Under the frozen 2026-06-12 rubric none reached tradeable size.

| Ticker | Dir | raw | Tier | Killed by |
|---|---|---|---|---|
| CRWV | vol long | 3 | LOW | VRP gate (−1) + debate gate (−1) → starter floored to skip |
| AAPL | short | 1 | DROP | quant drop floor (≤2) |
| RDDT | short | 1 | DROP | quant drop floor **+ fundamentals VETO** |
| COIN | short | 1 | DROP | quant drop floor |
| MU | short | **−1** | DROP | **−3 flow_conflict** + fundamentals VETO |

### 3a. Long swings (regime-aligned) — **EMPTY**

No name produced a scored long thesis. The two structurally strongest long-side reads both failed the confluence gate on a single flag:

- **AMZN (+15.32%)** — `multileg-strategist` inferred a genuine long call diagonal roll: sell Aug-21 250C (OI 71,889, closing a pre-earnings long that just paid) → buy **Nov-20 240C** (OI 2,429, *opening*, $99.9M, delta 0.749) plus Nov-20 305C. The anchor is real and worth recording: they paid up into the **112-day Nov hump at 37.3% IV** rather than the **42-day belly minimum at 32.8%** — deliberately buying *through* the next earnings event at full premium is a conviction statement about the stock, not a vol trade. But `repeat_count` is 1, `dealer-positioning` flags post-earnings vanna-unwind risk (net_vanna −51,565, the largest call-heavy magnitude in the set), and `sweep-tracker` read today's AMZN flow as **profit-taking / covered-call writing into the rally** ($52.6M bid-side 250C cluster, 714 trades), not a chase. One positive flag → watch-only.
- **NVDA** — `accumulation-hunter`'s only surviving long candidate, and self-described as "not a clean flag": 4 aligned signals, mega-tier DP buy_ratio 0.774, OI BUILDING 5 days (+2,110,641 net — genuinely large, not the C47 degenerate case), institutional-accumulation ACCUMULATION at 1.66 buy/sell. **But `cum_flow_30d` is −$64.8M — sign MISMATCH against the bullish thesis, so the C11 conjunction halves +3 → +1**, and ~20% of mega buy volume is a confirmed closing-cross print ($230M @ 20:08:03Z). One flag → watch-only. **C34 invalidation anchor if ever revisited: the $200.75 DP shelf ($1.36B, 6.79M shares, 191 trades).**

### 3b. Short / fade swings (defined risk only) — **EMPTY**

Four short theses cleared confluence; none survived. The structural finding is that **the frozen rubric has almost no way to score a short**:

> The entire bearish evidence stack today — three mechanized DEX flips (AAPL 2.32×, RDDT 15.43×, COIN 6.14×), institutional-tier dark-pool **distribution** (AAPL 77.2% sell, MU 64.7% sell), Tier-1 floor/opening put blocks, and capitulation put sweeps — maps to **exactly one scored line**, the +1 DEX flip. There is no distribution mirror of the +3 accumulation conjunction; sweep-persistence was removed 2026-05-23; single-leg puts earn 0 permanently (C19 CLOSED as REFUTED 2026-07-25).

Per name:

- **AAPL — SHORT, raw 1, DROP.** The cleanest mechanized flip on the board (`+6,317,233,146 → −4,905,966,157`, ten prior sessions all positive, whipsaw False) plus 77.2% mega-tier DP selling, a $7.00M floor put block at strike 340 (21 DTE), and front-end 1.181. Fundamentals **CONFIRM**: a real −6.88% EPS miss with a September-quarter guide-down on AI-driven component/memory shortages, and **UBS extending the constraint into fiscal 2027**. What kills it: `cum_flow_30d` is **−$90.4M but MIXED** — $6.919B bearish vs $6.828B bullish, a 50.3/49.7 split where the net is **0.66% of gross**. That is mega-cap churn, not directional accretion, and it earned **−1 flow_conflict_lite**. The bull's unrefuted point stands: every piece of bearish evidence — DEX flip, DP sell-tier, floor put, sweeps — *postdates* the print by construction. The evidence describes a −7.35% move that already happened. **Invalidation if ever traded:** no clean non-cross DP level (AAPL was in today's 20:00Z closing-cross print set) — fall back to a reclaim of the pre-earnings gap. **10-day trend:** 6 bearish / 4 bullish days; IV rank collapsed 75.22 → 52.75.
- **RDDT — SHORT, raw 1, DROP + fundamentals VETO.** Strongest DEX flip magnitude in the fleet (15.43×) on an unusually clean prior run — four consecutive sessions pinned within ±1% of +$168M, then a violent reversal to −$419.9M — with GEX flipping FULLY_NEGATIVE the same session (negative gamma is pro-cyclical and *amplifies*). `vol-surface-scout`: base_shape **BACKWARDATION, unflipped even post-hygiene**, front-end 1.116 — "**NOT a clean crush — still a LIVE event. Do not build a calendar here.**" **The fundamentals gate VETOED it**: 4-of-4 EPS beats, revenue **+70.64% YoY**, EPS +460.37%, gross margin 91.4%, **debt/equity 0**, current ratio 11.56, insider MSPR **+6.23 (not selling)**. The −21% came from a single qualitative comment — the CEO calling Google referral traffic "choppy" — on an otherwise clean beat-and-raise, and post-cut sell-side targets sit almost entirely *above* spot (B.Riley $270, Truist $275 raised, Wedbush $221, Piper $195, Oppenheimer $200; only Wells Fargo's $142 is near, **none below**). Both debaters converged honestly: the microstructure says live-and-amplifying, the fundamentals say overshoot, and the bear conceded its case is a tactical entry read, not a 2–3 quarter thesis. **10-day trend:** IV rank collapsed 70.83 → **28.30** — the vol has already been sold.
- **COIN — SHORT, raw 1, DROP.** The strongest *fundamental* short on the board and the weakest *microstructure*: fundamentals **CONFIRM** 3-of-3 (three consecutive deepening misses at −519.8% / −559.7% / −574.4% surprise, revenue −5.76% and EPS −50.57% YoY, insider MSPR −41.73 with two months at −100). But the DEX flip carries **`whipsaw_warning: TRUE`** (4 sign changes in 11 sessions, 5 GEX regime flips in 10) and its own analyst rated it LOW confidence; `cum_flow_30d` is **+$22.4M and 90d +$122.9M — both POSITIVE, opposing the short**; front-end is **1.025 (FLAT)**, measurably calmer than RDDT or MU on a comparable-size crash. "Record 10.3% of global crypto trading, still a third straight loss" is a share-of-a-shrinking-pie value trap, but a 3.36-beta proxy after −10.6% into an 89-day catalyst vacuum is a bad entry on a real thesis.
- **MU — SHORT, raw −1, DROP + fundamentals VETO.** The only negative score on the board. Distribution evidence is genuine (64.7% mega-tier DP selling, a $7.25M opening put at strike 820 with size/OI 5.097, the largest sweep premium on the tape at $5.77B including ask-side LEAP puts out to Dec-2027, Michael Burry newly disclosed short, and a pc-z that unwound from BULLISH_EXTREME −2.726 on 07-29 to −0.85 while price kept falling). **The mechanized DEX flip FAILED** (prior opposite-sign run of 1 session, needs ≥3; whipsaw TRUE). And **`cum_flow_30d` is +$466.9M net BULLISH — 7.2× the union median — triggering the full −3 flow_conflict.** Fundamentals **VETO**: 4-of-4 beats, revenue +166.98% / EPS +700.71% YoY, margins expanding across gross/operating/net, debt/equity 0.27 — with **same-day third-party corroboration** that Apple attributed its own guide-down to memory shortages and hyperscaler capex beats confirm the shortage. **This is the third consecutive session an MU short has died on this same gate** (+$725M on 07-24, +$467M today). The bear's own honest conclusion: *"this is a 'don't be long' signal, not a short — a short here is a cycle-timing bet dressed as a flow read."* **C34 invalidation anchor: $823.03 — $493.4M of dark-pool volume across 140 prints today, an order of magnitude above every other level.** That is the institutional battleground: a hold above says the −5.90% day was absorbed; a break below with follow-through is the first evidence the flow side is winning.

### Near-term sweeps (informational — 0 rubric points)

`sweep-persistence` scoring was removed 2026-05-23 (P0.3, −22pp marginal contribution over two audits). Ranking is prose-only. **Persistent (≥3 of 5 sessions), non-mega-cap:**

| Rank | Ticker | Dir | Persist. | 5d sweep premium | Read |
|---|---|---|---|---|---|
| 1 | MU | mixed | 5/5 | $5.77B | Post-earnings unwind + fresh protective LEAP puts — not directional |
| 2 | SNDK | bearish | 5/5 | $2.66B | **Divergence**: window bearish (2028 LEAP puts) but today's largest print is an ask-side bullish call sweep |
| 3 | AMD | bearish | 5/5 | $1.81B | Top two prints (strikes 20/30 on a $476 underlying) are an **un-split-adjusted strike-grid artifact** — discount |
| 4 | SPCX | bullish | 5/5 | $953M | Cleanest bullish read; ΔOI +231,604, buy-the-dip continuation |
| 5 | INTC | mixed | 5/5 | $884M | Near-identical call/put trade counts at the same 110 strike = **straddle, not directional** |
| 6 | SMH | bearish | 4/5 | $1.08B | $51.7M 2027 LEAP put — sector hedging, not fresh conviction |
| 7 | NBIS | bullish | 4/5 | $786M | Clean repeated call buying across 150/170/185/200 |
| 8 | BE | bullish | 4/5 | $655M | Dip-buy into a +11.3% 5-day run |
| 9 | SOXL | bullish (stale) | 3/5 | $314M | Tag is stale — today's flow is put-dominated; SOXL −16.2% over 5d |

**Mega-cap hedge-flow filter applied:** SPXW, QQQ, SPY, NVDA, TSLA, MSFT, AMZN, SPX, AAPL, META, IWM, GOOGL all failed the alignment screen — every one returned `trend_direction: MIXED` on 30-day cum-flow with bull/bear premium within a few percent (SPY $28.46B vs $29.16B; NVDA $13.33B vs $13.39B). Not directional; footnote only.

**Chase vs capitulation:** GOOGL is the only clean momentum-chase among the winners (genuine ask-side 320C/325C/327.5C buying). **AMZN is profit-taking, not a chase** (bid-side 250C cluster, $52.6M, 714 trades). MSFT is mixed with the larger premium on the sell side. NVDA is 0DTE market-maker churn. AAPL, RDDT and COIN are all clear capitulation.

---

## 4. LEAP Builds (6–24 months)

### **EMPTY BOOK.** No candidate cleared the 6-of-9 gate.

With `share_leaps` at **2.6%** of market volume on the last trading day of July — peak roll season — this is the expected outcome, not a miss. Disqualifications, which are the substantive output:

- **CORZ** (`CORZ280121C00035000`, 539 DTE, strike $35 vs spot $20.72, oi_diff +11,046) — **FAIL on the required 90-day cum-flow accretion gate**: net **−$54.7M BEARISH** ($462.9M bullish vs $517.6M bearish). Conviction-matrix reads `HEDGED_LONG` at 57.3 confidence — an explicit reject ("dark pool buying + put protection — institution buying stock and hedging"), which independently confirms the flow read. ~2 of 9 gates.
- **WBD** (`WBD270617P00023000`, 321 DTE) — **FAIL gate 1**: `consecutive_build_days: 1` (flat, not a persistent build). 90d cum-flow −$24.8M. Conviction-matrix labels DIRECTIONAL_LONG but at **28.1 confidence** (floor is 70) and contradicts itself — the text cites "aggressive call purchases" while the actual flow shows put_bid_volume 47,485 dominating. ~1 of 9.
- **CMCSA** (`CMCSA270617C00030000`, 321 DTE) — **FAIL gates 1 and 4**: single-day build, 90d cum-flow −$22.1M. ~2 of 9.
- **DRAM** — excluded as a **data-quality flag**, not scored: it is the Roundhill Memory ETF (IPO 2026-04-02), a thematic ETF outside this radar's single-name mandate, and `market_data.py` returned an implausible **$4.5B 20-day ADV** for a four-month-old thematic fund — almost certainly a ticker collision. Flagged and discarded rather than theorised from.

Month-end roll season did not confound the scan — none of the three showed roll-back or elevated `rolls_detected`; the failures are genuine accretion-direction and build-persistence failures.

---

## 5. Volatility Surface

### Substrate hygiene — the headline finding

Raw `uw options-structure iv-term-structure` returned **BACKWARDATION on 19 of 19 names** examined. After `scripts/term_structure_hygiene.py` dropped the 0DTE/expired bucket and sub-15-contract tenors, **14 of 19 flipped**: the corrected distribution is **13 KINKED, 5 BACKWARDATION, 1 pure CONTANGO**. The `dte_approx: 0` bucket carries 250–480% average IV on any expiry-day snapshot and inverts every front-vs-back comparison. `min_contracts=15` is a **tunable, not audit-frozen** parameter.

### The NFP cluster — the day's most important vol finding

The front-end kink cluster is **not** idiosyncratic earnings noise. **QQQ, SMH, TSLA, MU and GOOGL all show a genuine interior local-max at DTE = 7 = 2026-08-07 (Nonfarm Payrolls)**, verified against each name's own tenor curve (TSLA: 3d 38.5% → 5d 47.5% → **7d 55.0%** → 10d 45.8% — a real hump, not a monotonic ramp). SPY's NFP candidate at 5.0% prominence narrowly misses the 5% bar on a 69,958-contract tenor, while the module's mechanical pick landed on a thin 3,145-contract Tuesday weekly — read SPY as KINKED at 08-07 on an otherwise CONTANGO curve. **The market is pricing NFP week, not five unrelated companies.**

| Ticker | raw | base_shape | kink-aware | flipped | FER (7d) | kink DTE / expiry | prom. |
|---|---|---|---|---|---|---|---|
| QQQ | BACKW. | CONTANGO | **KINKED** | ✅ | 1.073 | 7 / **2026-08-07** | 6.8% |
| MU | BACKW. | CONTANGO | **KINKED** | ✅ | 1.198 | 7 / **2026-08-07** | 26.9% |
| SMH | BACKW. | CONTANGO | **KINKED** | ✅ | 1.169 | 7 / **2026-08-07** | 10.4% |
| TSLA | BACKW. | CONTANGO | **KINKED** | ✅ | 1.113 | 7 / **2026-08-07** | 15.8% |
| GOOGL | BACKW. | CONTANGO | **KINKED** | ✅ | 1.055 | 7 / **2026-08-07** | 6.5% |
| SPY | BACKW. | CONTANGO | KINKED | ✅ | 0.900 | 11 (thin) / 08-07 read | 21.3% / 5.0% |
| AAPL | BACKW. | CONTANGO | CONTANGO | ✅ | 1.181 | — | — |
| AMZN | BACKW. | CONTANGO | KINKED | ✅ | 1.195 | 5 / 08-05 (CPI cand. 30.3%) | 11.3% |
| MSFT | BACKW. | CONTANGO | KINKED | ✅ | 1.134 | 21 / 08-21 | 6.5% |
| CRWV | BACKW. | CONTANGO | **KINKED** | ✅ | 0.980 | 14 / **08-14 (earnings)** | 7.5% |
| AMD | BACKW. | CONTANGO | KINKED | ✅ | 1.032 | 28 / 08-28 (no catalyst) | 20.3% |
| COIN | BACKW. | CONTANGO | KINKED | ✅ | 1.025 | 49 / 09-18 (Sep print) | 53.8% |
| MSTR | BACKW. | CONTANGO | KINKED | ✅ | 0.957 | 14 / 08-14 (no catalyst) | 9.3% |
| ARM | BACKW. | BACKW. | KINKED | shape only | 1.164 | 21 / 08-21 (thin, 5,517 ct) | 79.7% |
| APP | BACKW. | BACKW. | BACKW. | ❌ | **1.405** | — | — |
| RDDT | BACKW. | BACKW. | BACKW. | ❌ | 1.116 | — | — |
| IREN | BACKW. | BACKW. | BACKW. | ❌ | 1.090 | — | — |
| HOOD | BACKW. | BACKW. | BACKW. | ❌ | 1.060 | — | — |
| MRVL | BACKW. | BACKW. | BACKW. | ❌ | 1.053 | — | — |

### Post-earnings IV-crush calendars — the cleanest structure on the board

| Ticker | base_shape | FER | Structure | Note |
|---|---|---|---|---|
| **AAPL** | CONTANGO | 1.181 | short 2026-08-07 / long 2026-08-28 (34.1% vs 28.8%) | Cleanest; base-shape read undersells it, FER is the honest number |
| **MSFT** | CONTANGO | 1.134 | short 08-07 / long 08-28 (37.1% vs 32.7%) | Clean crush |
| AMZN | CONTANGO | 1.195 | short 08-07 / long 08-28 (42.1% vs 35.2%) | **Less clean** — a secondary CPI-week bump (12 DTE, 30.3% prominence) sits *inside* the front leg and a naive 7/28 calendar does not hedge it |
| GOOGL | CONTANGO | 1.055 | marginal | Ratio close to the FLAT band |
| **RDDT** | **BACKWARDATION (unflipped)** | 1.116 | **DO NOT BUILD** | Curve stayed front-loaded post-print — continued-turmoil pricing, still a live event |

> **Every short leg above expires 2026-08-07 — you are short NFP-week vol on the front leg.** With VIX at 15.99 and −13.94% over five sessions, that is selling cheap front vol into a three-print macro stack (NFP 8/07, CPI 8/12, PPI 8/13). Acceptable for AAPL/MSFT where the long back leg absorbs a blowout; least clean for AMZN.

### BACKWARDATION calendars (front rich, no catalyst) — **NONE clear the bar**

APP (1.405 — earnings 8/05, straightforward pre-earnings richness, abort), RDDT (1.116, >1.10, live event), and HOOD/MRVL/IREN (all below 1.10 but **with no prior-session snapshot to confirm the ratio is *falling***). The "panic resolving" precondition could not be evidenced for any of them. This bucket is a genuine "nothing here," not a coverage gap.

### Realized-vs-implied dislocations (IV30 vs RV20)

| Ticker | IV30 | RV20 | Gap | Read |
|---|---|---|---|---|
| **TSLA** | 45.3% | 67.0% | **−21.7** | **Genuine** — no earnings in window; buy-vol candidate |
| **MU** | 92.1% | 106.5% | **−14.4** | **Genuine** — next print ~09-21; reinforced by the real 7-DTE NFP kink |
| IREN | 126.7% | 152.7% | −26.0 | Genuine but bitcoin-beta-noisy RV; context only |
| RDDT / AMZN / MSFT / GOOGL / AAPL | — | — | −28.5 … −10.3 | **Artifact** — RV20 mechanically inflated by yesterday's earnings gap sitting inside the 20-day window. Disregard for ~3 sessions |
| **MSTR** | 76.1% | 58.1% | **+18.0** | Closest thing to a genuine sell-vol candidate — but bitcoin-correlated and QQQ-adjacent, so defined-risk only (iron condor, never naked) |
| APP | 89.3% | 59.2% | +30.1 | Rich because the 8/05 earnings is priced — not tradeable as a sell |

### IV outliers

`iv_outliers.json` is dominated by micro-cap/illiquid names (FRMI, PCT, SPCX, EOSE, KORU, REPL, XNDU — all sub-$50M ADV, dropped on C12). Only two liquid names carry real premium: **INTC** (0DTE put, strike 105, $83.5K) and **RBLX** (0DTE put, strike 49.5, $199K) — both same-day tail bets, not structural mispricings.

> ⚠ **`uw historical iv-percentile-zscore` returned `dates_used: 77` for every single symbol today — below the 120-day first-class floor. Every percentile and z-score in this section is PROVISIONAL.**

---

## 6. Risk & Correlation

**Macro headline:** yield curve normal (+0.47), core CPI 2.81% / **core PCE 3.29%**, unemployment 4.2%, payrolls **+57k** (cooling), 10Y **4.68% and rising** (+24bp/30d), USD weakening, fed funds 3.63%. Forward Tier-1 stack: **NFP 08-07 (T+5) · CPI 08-12 (T+8) · PPI 08-13 (T+9).** FOMC just passed.

**Breadth:** `fz` reports **221 advancers / 281 decliners, 43.94% green**, avg change −0.13%, median −0.24% — against a **green** cap-weighted index. **`divergence_flag: TRUE`.** This is the distribution tell the single regime label hides, and it agrees with the flow-breadth read (34.1% bullish) and with equal-weight RSP closing −0.17%. Advisory — it does not change sizing.

### Correlation clusters (`uw risk portfolio-correlation`, 30d, run against today's candidates)

- **CLUSTER (≥0.70): RDDT / COIN = 0.755** — `post_earnings_selloff_cluster`. Same bet: high-beta post-earnings capitulation short. RDDT is VETO'd, so COIN is the kept member by elimination. Both are DROPs, so this changes nothing sized — recorded so the loop sees it.
- **Soft watch (0.60–0.70): CRWV / MU = 0.685** — both AI-infrastructure beta. No deduction under the mechanical band, but if both ever pass gates simultaneously expect this pair to breach 0.70.
- No flag: AAPL / COIN 0.51 and below.
- **Tool caveat:** sector metadata returned `Unknown` on all five names — the concentration warning is unusable today.

### Fundamentals verdicts (top 5)

| Ticker | Verdict | Next earnings | Days | Read |
|---|---|---|---|---|
| CRWV | **CONFIRM** | 2026-08-11 | 11 | Genuinely binary print (surprise dispersion −25.7% → +78.7%); event correctly priced at 14 DTE; fresh Leidos DoD/IC cloud catalyst dated today. Risks: d/e **6.48**, current ratio **0.46**, $2.6B term loan repriced wider (S+550 vs S+425–450 talk, OID to 97) |
| AAPL | CONFIRM | 2026-10-28 | 89 | Real miss + forward guide-down; UBS sees the constraint persisting into FY27; insider MSPR −50.5. Trailing growth still healthy (+14.24% rev, +32.61% EPS) — it is a forward guide-down, not a trailing deterioration |
| RDDT | **VETO** | 2026-10-28 | 89 | 4/4 beats, rev +70.64% YoY, d/e 0, insider MSPR +6.23, analyst PTs mostly above spot — capitulation overshoot, not a fundamentals short |
| COIN | CONFIRM | 2026-10-28 | 89 | 3 straight deepening misses, rev −5.76% / EPS −50.57% YoY, insider MSPR −41.73 |
| MU | **VETO** | 2026-09-21 | 52 | 4/4 beats, rev +167% / EPS +701% YoY, margins expanding, same-day memory-shortage corroboration from Apple and hyperscaler capex — the fundamentals back the **bull** side of the 3-session-running flow_conflict |

`fz_context` was **unavailable on all five** — every derived field returned null with `screen_fallback_used: []`, the known upstream Finviz quote-grid gap (C17). Advisory, 0 tier impact. Separately, `fz`'s screener output today exhibited the **synthetic-ticker artifact** (every ticker's first letter doubled: `CCDNA`→CDNA, `SSNOW`→SNOW, `NNWL`→NWL), and the squeeze screen returned an alphabetical page-1 head (all A/B names) rather than a ranked top-N — so the squeeze lane carried no usable signal today.

### Distribution flag (C28, advisory — 0 points, 0 tier impact)

**MSFT** carries `distribution_flag: present = true` despite a pristine-looking 0.981 mega-tier DP buy ratio. Two of thirty trades — **$559.8M, 31.6% of mega buy volume — executed at 20:00:12Z and 20:08:03Z**, the closing-cross window, and the dominant DP level ($464.72) is the *exact closing price* with 200 trades. Underneath, `uw oi decrease-with-volume` shows four Aug-21 **call** OI closures on high volume: `C00480000` −47,108 (vol 81,349), `C00500000` −22,724, `C00390000` −18,217, `C00450000` −14,523 — **≈$160M notional of institutional call OI unwound same-day**, `closing_side: "call"`. Net OI still rose because other strikes opened, so this reads as a *roll* rather than pure distribution — but it directly undercuts a conviction-accumulation reading, and `contrarian-scanner` independently flagged MSFT for long-fragility (price +22.5% over 30 days against net options flow of −$12.4M).

**Systemic artifact:** nearly every top-20 dark-pool print today (SPY, QQQ, IVV, AAPL, APP, MSFT, V, HD, SPCX, IXUS, SNOW) executed in the 20:00–20:25Z closing-cross window at or near the closing price. On the last trading day of July this is month-end rebalancing leakage, not stealth accumulation. Any single-day DP size read today should be discounted accordingly.

### Event-risk flags

NFP (08-07) sits **T+5** — inside the horizon of every short considered, all of which are undefined-risk directional expressions. Moot at skip. CRWV's 8/14 expiry contains earnings 8/11, CPI 8/12 *and* PPI 8/13.

### Debate-disconfirmation cuts

**CRWV was cut by the debate gate** (anti-trade bear 0.45 ≥ pro-trade bull 0.40) with a **BOTH_SIDES_LOW** flag — neither advocate cleared a coin flip. The bear dismantled the bull's load-bearing statistic: the 0.8537 figure is a **|move| > 2% realisation rate**, not "realized beat implied" — a bar a 109%-RV name clears on a quiet Tuesday, and it says nothing about clearing **19.4%**. Working the pricing apples-to-apples (same folded-normal 0.7979 factor that reproduces the quoted 19.39% from 124% IV), RV20 of 109.4% implies a **~17.1–17.4%** expected 14-day move against **19.39% priced** — the straddle is **~12–13% rich to trailing realized**. Earnings lands on **day 11 of 14**, leaving a 3-day conversion window. The bear conceded the −25.7%/+78.7% surprise dispersion is a genuine fat-tail argument it could not refute.

> ⚠ **Spec gap to register for the next `/calibration-audit`.** The `debate` gate is written as "bear residual ≥ bull residual ⇒ −1 tier," which assumes a LONG thesis where the bear is the disconfirmer. **Four of today's five names are SHORT theses, where the bear-researcher argues FOR the trade and the bull is the disconfirmer.** Applied literally, the gate would have fired on all four shorts for the wrong reason. It was applied direction-aware (cut when the side arguing *against* the trade has residual ≥ the side arguing *for* it), and today is the first session where the literal and intent readings produce **opposite verdicts** on four names. The gate text needs a direction-aware rewrite. A second item: `debate_residuals` bins at 0.10 spacing from 0.15, so CRWV's bull residual of **0.40** is unrepresentable — it was binned **down to 0.35** (conservative for a pro-trade residual; the gate fires either way).

### Hedge sleeve

**No hedge required from this book — the sized book is flat, zero positions, zero net delta.** The ≥0.6 directional-skew trigger cannot fire on an empty book.

The standing note is the **NFP convergence** described in the Executive Summary. If the desk carries discretionary long exposure into 08-07, **mirror the institutional structure rather than inventing one**: a QQQ Aug-07 660/645 put debit vertical (~$122/contract debit, ~12:1) or IWM Aug-07 285/275 (~$75.4/contract debit, ~13:1), sized strictly to external book delta. This is a hedge use, not an alpha expression — the no-short-alpha-sizing rule stands, and both structures failed the Step-3 confluence gate as trades.

### Adverse-flow exit list

**None.** `uw watchlist alerts` and `uw watchlist scan` against `conviction_2026-07-30` both returned an empty watchlist — yesterday was also an empty board, so there is no carried position to exit. The `fz` quote-drift tripwire had nothing to run against.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

### **No name reached MEDIUM or HIGH. This section is empty by result, not by omission.**

**Expectancy lens `[advisory — expectancy is not yet a live sizing axis]`** — per-tier realised win rates from the most recent `/calibration-audit` (2026-07-25, `phase_3_calibration`):

| Tier | n | Realised WR | Payoff ratio |
|---|---|---|---|
| HIGH | 7 | **0.143** | not emitted by the audit's calibration table |
| MEDIUM | 19 | 0.526 | — |
| LOW | 87 | 0.402 | — |
| **DROP** | **327** | **0.431** | — |

`HIGH > MEDIUM > LOW` **fails for the 4th consecutive audit**, and **DROP (0.431) beats LOW (0.402)** — the names the system refused have outperformed the names it graded tradeable. All 7 HIGH calls are pre-freeze; the frozen 2026-06-12 rubric has produced **none** (LOW 0.308 on n=26, DROP 0.419 on n=267). This is the direct, measured justification for today's flat book: refusing to trade has been the better-calibrated action. The payoff-ratio column is genuinely absent from the audit's output — not withheld — so the C31 lens is half-populated today.

### Full per-ticker audit trail (all five gated names)

| Ticker | Dir | raw | Tier | Σ check | Class | win_rate (src, n) | excess | pre-risk | Fund. | Debate (bull/bear) | Gates fired | **final** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **CRWV** | vol long | **3** | **LOW** | 1+1+1=3 ✅ | earnings_vol | 0.80 (backtest_clean, 164; uncapped 0.8537) | n/a | starter | CONFIRM | 0.40 / 0.45 | vrp −1, debate −1 | **watch-only** |
| AAPL | short | 1 | DROP | 1+1−1=1 ✅ | bearish_flow | 0.5809 (backtest_clean, 136) | +0.0588 | skip | CONFIRM | 0.35 / 0.65 | event_risk −0.5 (nominal) | **skip** |
| RDDT | short | 1 | DROP | 1+1−1=1 ✅ | bearish_flow | 0.5809 (backtest_clean, 136) | +0.0588 | skip | **VETO** | 0.35 / 0.35 | cluster, debate (both moot) | **veto** |
| COIN | short | 1 | DROP | 1+1−1=1 ✅ | bearish_flow | 0.5809 (backtest_clean, 136) | +0.0588 | skip | CONFIRM | 0.25 / 0.45 | event_risk −0.5 (nominal) | **skip** |
| MU | short | **−1** | DROP | 1+1−3=−1 ✅ | bearish_flow | 0.5809 (backtest_clean, 136) | +0.0588 | skip | **VETO** | 0.45 / 0.35 | debate (moot) | **veto** |

**Score components — CRWV (raw 3):** `+1` earnings-scout BUY VOL (kink @14 DTE = 08-14 matching the 08-11 print, prominence 7.5%) · `+1` vol-surface-scout independent KINKED-with-catalyst confirmation on a separate tool path · `+1` `oi-trend` BUILDING (+64,238 net, in real Sep/Jan-27/Dec-28 positioning tenors, not 0DTE).

**Score components — AAPL / RDDT / COIN (raw 1 each):** `+1` mechanized DEX flip · `+1` oi-trend BUILDING · `−1` flow_conflict_lite.
**Score components — MU (raw −1):** `+1` vol-surface KINKED @ NFP · `+1` oi-trend BUILDING · **`−3` flow_conflict** (+$466.9M net bullish, 7.2× union median).

### Sizing-guard audit

Four downgrade-only guards applied, all stacking, none upgrading: (1) the n<10 cap of 0.69 was a no-op (n=136 and n=164); (2) the **C2 market-excess gate** passed — `bearish_flow` cleared same-direction SPY by **+5.9pp over the same 136 kept windows** (SPY short base 0.5221); (3) the **C4 OI-opening gate** was a no-op — all four shorts showed BUILDING with positive net ΔOI (AAPL +213,455 / RDDT +37,732 / COIN +44,995 / MU +139,378); (4) the **[0.55, 0.65) anti-predictive band floor fired** on all four shorts — 0.5809 sits squarely in the band that realised **0.179 overall / 0.133 post-freeze**, flooring them to starter before the drop floor superseded to skip. **The quote itself was left unchanged** so the reliability diagram still bins the true statement.

**CRWV's 0.80 was deliberately not the sizing input.** `high_iv_rank` and `earnings_vol` are the two standing BH-surviving over-claim classes, so the vol quote never drives `pre_risk_size` — CRWV sized on the tier-default path. The debate independently confirmed this was right: the 0.8537 measures |move| > 2%, not "realized beat implied."

### Substrate degeneracies observed today (for the audit register)

1. **`oi-trend` returned `consecutive_build_days: 78` on all five names** and the +1 BUILDING line fired **5-of-5** — zero discrimination, matching the 16-of-16 on 2026-07-24 (register **C47**). AAPL's and COIN's top "builds" were same-day-expiry 0DTE strikes — expiry artifacts.
2. **`cumulative-premium-flow` returned `trend_direction: MIXED` on all 10 pulls** — the label carries zero discrimination; the magnitude arms of the flow_conflict branch did all the work.
3. **Raw `front-end-iv-ratio` fired nominal panic reads >1.6 on a day VIX fell 6.4%** because `near_dte_actual` snapped to 0. The hygiene path must be mandatory *before* the panic gate, not optional after it.
4. **`uw historical pc-ratio-zscore` has no `--date` flag** (re-confirmed) — the "rising z" precondition for the −2 crowding line is structurally unevidenceable with the current tool. Zero names hit ±2σ anywhere today (max |z| = AMD +1.83; SPY +0.83, QQQ −0.30).
5. **`iv-percentile-zscore` returned `dates_used: 77` for every symbol** — below the 120-day first-class floor.
6. **MU's −3 vs AAPL's −1 flow_conflict branch is scale-sensitive**, as the MU bear fairly noted: MU's +$466.9M is **0.53% of $88.6B gross** while AAPL's −$90.4M is **0.66% of $13.7B gross** — a *smaller* share of book tripped the *heavier* branch, because the magnitude test is absolute and MU has the largest options book in the funnel ($41.8B ADV). Worth registering; the rubric is frozen, so this is a note, not a change.

### Conviction-scoring rubric (verbatim, frozen version `2026-06-12`)

```
Daily conviction score = Σ:
  +1  MECHANIZED DEX sign-flip or vanna-squeeze in trade direction (scripts/dex_flip.py; sign CHANGE not level;
      ≥3 consecutive prior sessions opposite; |net_dex| ≥ 0.25× trailing-10 median)   # DEMOTED +3→+1 & mechanized 2026-06-12 P0.4
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified institutional-tier
      confirmed) — CONJUNCTION (C11): full +3 only when cum_flow_30d sign-aligned AND |cum_flow_30d| ≥ $50M;
      else halved to +1
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix DIRECTIONAL_LONG conf > 70 — CONDITIONAL: only when
      dominant_signal_class == leap_directional; 0 otherwise
  +1  cumulative-premium-flow net directional accretion in trade direction (30d) — INTENT-SCREENED:
      no C28 distribution_flag, and not deep-ITM sub-parity ex-div calls
  +1  sector-rotation single-name leader — CONDITIONAL: persistence_score ≥ 0.6 AND cum_flow_30d aligned
      AND |cum_flow_30d| ≥ $50M
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored play type)
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist top-5 (OPEX week only)
  -2  contrarian-scanner overcrowded long with rising pc-ratio-zscore (informed-flow CONTINUATION penalty,
      not a reversal signal — Pan-Poteshman 2006, Ge-Lin-Pearson 2016)
  -3  flow_conflict — cum_flow_30d clearly opposite dominant_signal_class (sign flip + magnitude > union-median)
  -1  flow_conflict_lite — 30d read MIXED (signed sum near zero, or aligned but bottom-quartile magnitude)
      # -3 and -1 are MUTUALLY EXCLUSIVE — apply ONE
  # TIER GATES (risk-monitor, Step 2d) — contribute 0 to raw_score, never appear in score_components:
  -1  [TIER] correlation cluster (pairwise corr ≥ 0.70)
  -3  [TIER] market-regime conflicts with trade direction  → −1 TIER
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | HIGH | full (subject to Step-3a load-bearing gate + win-rate gate) |
| 7–8 | MEDIUM | half (subject to win-rate gate) |
| 3–6 | LOW | starter / watch-only |
| ≤ 2 | drop | filtered by the quant's drop floor |

**Tier-cut status:** the ≥9 HIGH cut failed its scheduled re-confirmation on 2026-06-12 and has inverted for four consecutive audits. Cuts are retained under the P0.1 freeze but **carry no validated ranking claim**; the P0.6 out-of-regime guard caps all sizing at half in the interim.

### Deep-dive hand-off

**Skipped** — no HIGH-tier names. Step 6.5's batch strategy synthesis (`uw playbook batch-scan`) likewise had no qualifying names at raw_score ≥ 7.

---

## 8. Watch-only — single signal, no confluence

Listed for journaling, **not for trade entry today**. Each surfaced from one Phase 1 agent and failed the ≥2-agent confluence gate.

**The two most substantive findings on the board are in this section — read them before dismissing it.**

| Ticker | Dir | Flagged by | Why it failed the gate |
|---|---|---|---|
| **IWM** | SHORT | `multileg-strategist` (**HIGH** conviction, qualifies +2) | **`dealer-positioning-strategist` flags the OPPOSITE direction** (vanna_squeeze, net_vanna +82,036 — the strongest put-heavy skew in the set — swing_bias LONG). Conflicting single flags; neither direction reaches 2 agents. |
| **QQQ** | SHORT | `multileg-strategist` (MEDIUM-HIGH, qualifies +2) | Same inversion — `dealer-positioning` reads QQQ vanna-squeeze LONG. Also live partial-unwind risk: multileg_ratio fell 0.981 (07-28) → 0.474 (07-31). |
| **AMZN** | LONG | `multileg-strategist` (MEDIUM, +2 discounted, repeat_count 1) | `dealer-positioning` DEX flip failed (level, not flip; whipsaw TRUE) and flags vanna-unwind risk; `sweep-tracker` reads profit-taking, not a chase. |
| **NVDA** | LONG | `accumulation-hunter` (self-described "not a clean flag") | cum_flow_30d −$64.8M sign-mismatched → C11 halves +3 to +1; ~20% of mega buy volume is closing-cross. |
| **MSFT** | LONG | `accumulation-hunter` (**rejected on evidence**) | 31.6% of mega buy volume is confirmed closing-cross; carries `distribution_flag: present` (~$160M of Aug-21 call OI unwound). See §6. |
| GOOGL | LONG | `sweep-tracker` (self-demoted) | Mega-cap hedge-flow filter — cum_flow MIXED; `accumulation-hunter` excluded it as GOOG-vs-GOOGL dual-share-class arb (mega buy_ratio 0.729 vs 0.103 on the same day). |
| SPCX | LONG | `sweep-tracker` (5/5, cleanest bullish read) | Carries a Tier-1 *bearish* opening put; `sector-rotation` lists it as an Industrials bearish name. Conflicting. |
| NBIS | LONG | `sweep-tracker` (4/5) | Single agent; `earnings-scout` SKIP. |
| BE | LONG | `sweep-tracker` (4/5) | Single agent. |
| TSLA | VOL LONG | `vol-surface-scout` (genuine −21.7pp RV>IV gap, no earnings in window) | Single agent; `sweep-tracker` demoted it under the hedge-flow filter. |
| PLTR | VOL LONG | `earnings-scout` (BUY VOL, MEDIUM-HIGH; earnings 08-03, implied move 11.75%, IV rank 77.98) | Single agent. Note: the **highest-conviction earnings call of the day** and it earned no second flag. |
| SMCI | VOL LONG | `earnings-scout` (BUY VOL, MEDIUM; 08-11, implied move 18.04%) | Single agent. |
| CSCO | VOL SHORT | `earnings-scout` (SELL VOL half-size; 08-12, implied move 9.75%, cleanest kink-at-event in its scan) | Single agent. |
| UBER, DDOG | VOL LONG | `earnings-scout` (low conviction) | Single agent. |
| SNDK | — | conflicting across three agents | `accumulation-hunter` CONFLICT (DP 94% buy vs bearish options tape — "don't score either way"); `contrarian-scanner` disqualified (genuine BACKWARDATION + earnings 08-05); `earnings-scout` SKIP. Highest front-end panic on the board (1.299). |
| SMH | SHORT | `sweep-tracker` (4/5, sector hedging) | Single directional flag; the $51.7M 2027 LEAP put reads as protection, not conviction. |
| INTC | — | `sweep-tracker` routed to multileg | `multileg-strategist` did not confirm; flow is straddle-shaped at the 110 strike. |

**Also noted and not traded:** a **SPY deep put butterfly** ladder — exact 1×2×1 twice (Sep-30 635/535/435 at 150,137/300,058/150,013 and Oct-16 625/525/425 at 150,094/300,138/150,001), repeating a 07-27 print of the identical Sep-18 625/525/425 triplet with size stepping 100k→150k. It is a systematic portfolio tail overlay 28–30% below spot — no swing-horizon directional thesis is expressible there — and its side attribution self-contradicts across two structurally identical prints, so direction is unresolvable from the substrate. Recorded as market structure, not as a call.

---

*Generated by `/daily-analysis` — 11 Phase 1 agents (no OPEX agent; 2026-07-31 is outside the third-Friday window), then quant → fundamentals → debate → risk. Rubric version `2026-06-12` (frozen). Envelope: `analyses/daily/2026-07-31/decision.json`.*
