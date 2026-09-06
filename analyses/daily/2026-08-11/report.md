# Daily Market Analysis — 2026-08-11

## Executive Summary

- **Regime + GEX state:** TRANSITIONAL (trend UPTREND) — SPY 770.56 above both SMAs but **both indices flipped into NEGATIVE gamma with the largest negative-GEX strike sitting AT the money**. VIX 15.28 (−7.39% 5d). UW options breadth 36.1% bullish against fz cash breadth 54.67% green. Netted sector lean: Technology **−$140.8M OUT**, Financials/Energy/Industrials IN.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** SPY short-gamma · ZGL 789.87 (reliable) · call wall 780 / put wall **770 = spot** · favour long gamma. QQQ short-gamma · ZGL 769.03 **unreliable** · call wall 730 / put wall **718 = spot** · same bias, lower confidence. Advisory — see §2.
- **Top swing build:** **None.** The board is empty. NBIS was the only name above the drop floor (raw 3, LOW) and took five independent −1 tiers off a `starter`.
- **Top LEAP candidate:** **None.** `leap-positioning-radar` returned an empty book — every DTE>180 candidate was a covered-call write, a sub-floor illiquid name, or had 10-day OI building against flat-to-bearish 90-day premium accretion.
- **Biggest risk:** **July CPI prints tomorrow (2026-08-12), inside the horizon of every structure considered today** — and NBIS reports the same morning. No correlation cluster matters because there is no book: the only pair ≥0.70 was NBIS/MU at 0.792, and they point in opposite directions.

---

## 1. Regime & Gamma State

`uw risk market-regime` reads **TRANSITIONAL — mixed signals, reduce position size, wait for clarity**, with the trend label still **UPTREND**: SPY 770.56, above the 20d (752.30) and 50d (747.84), +2.86% over 30 days, only −0.81% from the 90-day high. Guidance verbatim: *"Half position sizes. Favor defined-risk strategies."*

**The tape is rotation, not decline, and the distinction is outcome-relevant.** Cap-weighted indices closed red while equal-weight and small-cap closed green:

| | 1d | 5d | rv20 |
|---|---|---|---|
| SPY | −0.32% | −0.10% | 13.7% |
| QQQ | −0.34% | −0.75% | 24.2% |
| IWM | **+0.34%** | −0.24% | 15.0% |
| RSP (equal-weight) | **+0.21%** | +0.21% | 10.4% |
| VIX | −1.16% | −7.39% | — |

Sector leadership confirms it: **XLE +1.25% (+4.12% 5d), XLU +1.16%, XLI +0.60%, XLB +2.38% 5d, XLV +3.65% 5d** against XLRE −0.72%, XLC −0.50%, XLY −0.36%, XLK −0.12%. The single-name drag is **GOOGL −3.84% (−8.96% 5d)**. UW's own options breadth reads 36.1% bullish — that is a *flow* measure of a tape whose *cash* breadth is 54.67% green. Read the red index as mega-cap-specific weakness inside a broadening market, not risk-off.

**Per-index gamma (current-state EOD book; §2 carries the forward read):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 770.60 | 789.87 (reliable) | +$209.4M | **NEGATIVE** | 780 (+1.22%) | **770 (at spot, −$255.1M)** |
| QQQ | 718.26 | 769.03 (**unreliable**, 7.07% away) | +$55.8M | **NEGATIVE** | 730 (+1.63%) | **718 (at spot, −$43.7M)** |
| IWM | 300.99 | artifact-affected (see note) | — | positive DEX throughout | — | — |

> **Tool defect, surfaced for the audit:** `uw historical gex-time-series` returns intermittently implausible `zero_gamma_level` values — QQQ 249.5 against a $718 spot, NVDA 7.56 against ~$180, IWM 100–191 against $301. This is the known ZGL-grid artifact. Both `gamma-flip-tracker` and `dealer-positioning-strategist` read the `regime` and `total_gex` *sign* instead of the absolute level, and flagged rather than suppressed the affected rows.

`uw options-flow dte-volume-share`: 0DTE **29.2%** / weeklies 29.0% / monthlies 27.2% / LEAPs **4.0%** — hint **BALANCED**. Neither retail-dominated nor institutionally-positioned. The 4.0% LEAP share is consistent with the empty LEAP book in §4.

`uw historical vrp`: **SPY +0.0037 FAIR** (IV30 12.91% vs realised 12.54%); **QQQ −0.0479 NEGATIVE** (IV30 19.65% *below* realised 24.44%). **No positive VRP was measured anywhere on the tape today**, and `vol-surface-scout` emitted no SELL VOL bias across ten screened names. That single fact independently killed both the TGT short-vol lane and the 0DTE premium-sell lane.

**Macro backdrop** (`scripts/fred_macro.py`): yield curve **normal** (10Y−2Y +0.48), core CPI **2.81%** YoY, core PCE **3.29%** YoY, unemployment **4.1%**, payrolls **−23k MoM**, 10Y **4.72% and rising** (+0.16 over 30d), USD **weakening**, fed funds 3.63%. This is a **stagflationary tilt** — inflation is not yet beaten while the labour market is contracting. It is also the direct macro rationale for the growth→value rotation in §2b.

**Forward event risk:**

| Date | Event | Tier |
|---|---|---|
| **2026-08-12 (T+1)** | **July CPI** | **1** |
| 2026-08-13 | July PPI | 1 |
| 2026-08-14 | Retail Sales + Consumer Sentiment | 2 |
| 2026-08-20 | FOMC Minutes | 1 |
| 2026-08-21 | Monthly OPEX | structural |
| 2026-08-27/29 | Jackson Hole | 1 |
| 2026-09-16 | FOMC rate decision (no August meeting) | 1 |

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** Prose-only, **0 conviction-rubric points**, no backtested predictive claim. Predictive validation of these levels lives in `/weekly-analysis`'s rolling §2 backtest, not here.

**SPY** — spot 770.60 sits below ZGL 789.87 (2.5% away, inside the trust band) = **short-gamma**. The wrinkle that matters: the single largest negative-GEX strike on the entire book, **−$255.1M, sits at 770 — on top of spot**. That is a gamma cliff at the money, which *amplifies whipsaw* rather than pinning. Call wall 780 (+1.22%) is the nearest real magnet; 765 (−$94.3M) and 755 (−$69.1M) are the nearest support shelves. The regime flipped POSITIVE→NEGATIVE on **2026-08-10, one session ago**, with five flips in 30 days — fresh and unstable.
**Structure bias:** favour **long gamma** — debit verticals, directional 0DTE, or a long straddle given spot sits on the cliff. A short-gamma book plus a Tier-1 macro print is the setup for a genuine breakout, not a pin.

**QQQ** — spot 718.26, ZGL 769.03 flagged **`zgl_reliable=false`** (7.07% away, and the flip produced a `zgl_delta` of +548.58, a classic extrapolation artifact). Falling back to the `total_gex` sign (+$55.8M) plus spot-vs-strike structure: the three largest negative-GEX strikes (718, 715, 719, ~−$120M together) all sit within $3 of spot — the same ATM short-gamma clustering. Call wall 730 (+1.63%, 735 close behind); support 715 then 700. Regime flipped **today**, five flips in 30 days.
**Structure bias:** same as SPY, sized smaller — the ZGL is unreliable and the flip is same-day fresh.

**Mandatory caveats:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and recomputes both walls and the ZGL.
- **ZGL reliability.** SPY's is inside the 5% band and used directly; QQQ's is outside it and explicitly marked unreliable.
- **Gap risk voids the prior.** July CPI prints tomorrow morning and can gap spot through either wall before hedging engages. Both indices are already in a fresh, unstable, short-gamma-at-the-money posture. Do not treat 780/730 as hard caps or 765/715 as hard floors into that print.
- **Tooling limit.** `uw` cannot isolate the D+1 expiry (`gex --dte-max 1` errors) — this is the standing 0–45 DTE book as proxy.
- **ETF book**, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup — **STAND ASIDE**

`scripts/zerodte_setup.py` returns `verdict: GO_PREMIUM_SELL_INTRADAY` and `sell_premium: true` for both indices. **That verdict is unconditional, and today it is wrong.**

Today's `vol_state` is **LOW** (VIX 15.28). Reading `mean_pnl_by_vix_state[LOW]` net of the assumed 0.1% round-trip cost:

| | Unconditional gross | Unconditional net | **LOW-tercile gross** | **LOW-tercile NET** |
|---|---|---|---|---|
| SPY | +0.227% | +0.127% | **−0.018%** | **−0.118%** |
| QQQ | +0.356% | +0.256% | **+0.040%** | **−0.060%** |

The lane's edge lives entirely in the **MID (+0.356%) and HIGH (+0.343%)** VIX terciles (bounds 16.4 / 17.8). The attractive headline is the unconditional average, and it is carried by terciles we are not in.

Three independent reasons to stand aside compound on top of that: both indices are in **negative gamma with the put wall at the money** (whipsaw favours long gamma, not short), **CPI prints tomorrow** (gap risk against a delta-neutral seller), and QQQ carries **front-end backwardation** (0DTE IV 1.35× VIX). PnL basis note: `mean_pnl_open_pct` is **percent-of-underlying-spot-notional, gross** — not premium-collected, not margin-relative.

**Recommendation: no 0DTE premium sale tomorrow.** Worst day in the 60-session sample was −1.4% (SPY) / −2.453% (QQQ), and the short-vol left tail is **UNSAMPLED** — the validation window contains no vol shock, so the 88.3%/85.0% gross win rates overstate a negatively-skewed seller's edge.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

**Zero qualifying DEX flips across eleven names.** The mechanized +1 rubric line awards nothing to anyone today. `scripts/dex_flip.py` was run over the 14-session window 2026-07-23→2026-08-11 for SPY, QQQ, IWM, AMD, NVDA, MSFT, GOOGL, MSTR, META, MU and NBIS; every one returned `qualifies: false`.

Two genuine near-misses, both correctly rejected on the magnitude floor:

- **GOOGL** — `net_dex 2026-08-10 +$3,028,259,205 → 2026-08-11 −$7,042,193`; prior 10 sessions all positive; **|flip| is 0.2% of the $797.8M floor**. The whole positive book evaporated in one session, and `total_gex` collapsed +$142M → −$7.6M in lockstep.
- **NBIS** — three straight negative sessions (−$276.3M, −$373.2M, −$267.8M) → +$25.3M; **|flip| is 13% of the $196.8M floor**. `whipsaw_warning: true`, 4 sign changes in 14 sessions.

**No vanna squeeze qualifies anywhere.** The setup requires a put-heavy book *and* a falling-VIX leg of ≥3 consecutive sessions. The VIX series (dated, from the raw Yahoo chart API) reads `08-05 15.81 → 08-06 15.15 → 08-07 14.90 → 08-10 15.46 → 08-11 15.28` — the three-session decline **broke on 08-10**. GOOGL and NBIS are the only put-heavy books and are downgraded to **"vanna pressure, not squeeze."**

Front-end IV panic (>1.05) is live on **GOOGL 1.254, NBIS 1.279, MSFT 1.085, META 1.079** — all read as CPI event pricing, not standalone directional signal. SPY/QQQ/NVDA/MSTR/MU all show DEX magnitude deteriorating 40–95% off this week's peak while remaining nominally positive; **NVDA is the most likely near-term flip candidate** if the decline continues. IWM is the one name where dealer positioning (steady positive DEX) agrees with the rotation tape — unscored context only.

## 2b. Sector Rotation

**Rotation regime call: `growth→value`, HIGH confidence.**

Both canonical legs match on the **netted** source: Technology (growth) **−$140.8M OUT**; Financial Services **+$13.78M** and Energy **+$12.45M** (value) **IN**. The macro corroborates directly — 10Y rising to 4.72%, USD weakening, core PCE sticky at 3.29% is a rising-discount-rate tape that structurally favours cheap cyclicals over long-duration growth.

> **Direction discipline (C55).** `sector-flow` and `sector-flow-persistence` are **one gross-turnover source** and cannot express direction. Today they disagree violently with the netted read — Technology is **gross +$2.13B vs netted −$140.8M**, the most extreme split in the book. Every direction below is read off the netted `market-regime.sector_rotation`.

> **Persistence is degenerate today.** All eleven sectors returned `persistence_score = 1.0` and `trend = INFLOW`. The field separates nothing — the ≥0.6 threshold is satisfied *everywhere*, so the durability leg contributed zero information (C47-class). Conviction differentiation came from netted magnitude + ETF cross-confirm + price tape instead.

> **Coverage gap:** `market_regime.sector_rotation` surfaces only **6 of 11 sectors** (top-3 in / top-3 out). **Healthcare, Real Estate, Basic Materials and Communication Services have no netted direction today** — no rotation call is possible for them regardless of how their tape looks (XLV +3.65% 5d, XLB +2.38%, XLRE −2.41%). Direction was not manufactured from the gross figure.

**Rotating IN** (netted-confirmed, gross agrees, ETF confirms):

| Sector | Netted | Tape | ETF confirm | Named leaders |
|---|---|---|---|---|
| Energy | +$12.45M | XLE +1.25% / +4.12% 5d | XOP +$1.58M BULLISH-persistent (but XLE itself MIXED −$2.02M — flow lags price) | **EQT, XOM, OXY, DINO, VLO** |
| Industrials | +$6.73M | XLI +0.60% | **XLI #1 ETF inflow of the universe** (+$16.6M BULLISH-persistent, $155M top-5 DP mostly ≥mid, call-leaning sweeps to Nov $195) | **AXON, VRT, RKLB, UNP** |
| Financial Services | +$13.78M | XLF flat | **KRE +$8.35M BULLISH-persistent** — the leg is **regional banks specifically**; broad XLF actually contradicts at −$1.96M MIXED | **SOFI, BX, V, IREN, GS** |

**Rotating OUT — all three land in `watch_only`** (gross-vs-netted disagreement per C55, and independently blocked by the short-routing rule):

- **Technology** (netted −$140.8M vs gross +$2.13B) — the ETF split is the informative part: **IGV (software) −$14.46M BEARISH-persistent agrees** with the netted OUT, **SMH (semis) +$3.83M disagrees**. The OUT is real but **concentrated in software/mega-cap, not semis**.
- **Consumer Cyclical** (−$53.9M) — weakest evidence; XLY and ITB ETF flows both disagree. Largely noise.
- **Consumer Defensive** (−$35.7M) — **strongest of the three**: XLP price *and* XLP ETF flow (−$9.29M BEARISH-persistent) independently confirm. The +$835.6M gross spike is a one-day artifact (the sector jumped from ~$60M to $835M in a single session), likely CLX-driven.

**ETF flow tape (advisory — strengthens the conditional sector-leader +1, adds no rubric points):**

| ETF | Net premium dir | Persistence | GICS agreement | Notes |
|---|---|---|---|---|
| XLI | **+$16.6M** | BULLISH | **agree** | heaviest DP tape, call-leaning sweeps |
| EWY | +$12.6M | BULLISH | n/a (Korea) | DP mixed, weak urgency |
| KRE | +$8.35M | BULLISH | **agree** | the real Financials driver |
| SMH | +$3.83M | MIXED | disagree | semis diverge from the Tech OUT |
| XOP | +$1.58M | BULLISH | **agree** | |
| XLP | −$9.29M | BEARISH | **agree** | independently confirms Cons. Defensive OUT |
| IGV | −$14.46M | BEARISH | **agree** | strong bearish urgency — $13.2M put-ask Dec18 $90 |
| **GDX** | **−$52.7M** | BEARISH | n/a | largest outflow of the 21-ETF universe; reads idiosyncratic gold/rate flow, **not** a sourced sector call (XLB price was actually up) |

**Swing-book implication:** long the netted-confirmed IN book, sized per the conditional +1 gate — which on today's board produced exactly one scored name (AXON, and it scored 0 on the line because its cum-flow was $9.56M against a $50M requirement). Tactical only into CPI: a hot print extends growth→value, a cool print risks snapping mega-cap tech back.

---

## 3. Swing Setups (1–6 weeks)

**The board is empty. Zero sized positions.** Five names cleared the ≥2-agent confluence gate; two more are carried as confluence-gate failures so the counterfactual stays gradeable. Every one ended at `skip` or `watch_only`.

| Ticker | Score | Tier | Dir | Thesis (one line) | Invalidation | Final |
|---|---|---|---|---|---|---|
| NBIS | 3 | LOW | long | Cleanest pre-cross institutional DP print of the day, on a name reporting earnings tomorrow | Loses the **$191.00–192.06 DP shelf** | **skip** |
| GOOGL | 1 | DROP | short | Only mega-cap where sweep + cum_flow + price + screener all agree — and insiders are buying | Reclaims/holds $357.52 | **watch_only** |
| SE | 1 | DROP | long | Perfect 1.00 buy_ratio print sitting opposite the strongest distribution signal in the scan | Loses the **$130.02–131.29 DP shelf** | **watch_only** |
| TGT | 1 | DROP | vol_short | Best-instrumented vol setup of the day, in a structurally losing class with no positive VRP anywhere | 45d skew flattens to COMPLACENT | **skip** |
| AXON | 0 | DROP | long | Only favourable sector read on the board; margin collapsed to 0.42% underneath it | Loses $629 (secondary clean DP level) | **skip** |
| NVDA | 0 | DROP | short | Textbook institutional put vertical, erased by +$255M of opposing bullish flow | 220P leg stops building / >$225 | **watch_only** |
| MU | −1 | DROP | short | Tier-1 "bearish signal" is a delta −0.965 financing put | 30d flow turns decisively negative | **watch_only** |

> **Invalidation discipline (C34):** NBIS, SE and AXON are anchored to real institutional dark-pool levels rather than guessed percentages. AXON's primary level ($636.31) is explicitly **not** used as the anchor because it is ~72% closing-cross contaminated — the secondary clean level at $629 is.

### 3a. Long swings (regime-aligned)

**NBIS — raw 3, LOW, `starter` → `skip` after five −1 tiers.** The evidence is genuinely good and genuinely insufficient. Mega-tier DP buy_ratio **0.881** ($151.7M, n=4), with all four prints executed **19:38–19:48Z — before the 20:00Z closing-cross window** that contaminated 67–93% of every other mega-cap's tape today. Largest ticket 471,400sh / **$90.5M @ $192.05** on a defended $191.00–192.06 shelf; `institutional-accumulation` ACCUMULATION at buy/sell 1.98; OI BUILDING 5/5 (+188,006); vol KINKED with **VRP −0.4915** so optionality is cheap.

Against it: the OI build is **59.9% put-dominated** (against the thesis), the DEX flip failed its floor at 13% of requirement, there is no vanna squeeze, sweep-tracker shows a **conflicting 3-of-5-day bearish** tape, and ⚠ **a C28 distribution flag is present — $2.48M of 220-strike calls (10 DTE) being closed**, plus a smaller close at 260. Underneath: operating margin **−70.55%**, insider MSPR **−73.42 across five straight negative months**, and **Michael Burry short at $211.77** (above the close, currently profitable). And it **reports earnings tomorrow morning alongside CPI**, with a 23.16% implied move on a 161.8%-rv name.

The C11 conjunction halved to +1 because the +$225.8M net flow is only **2.71% of NBIS's own $8.35B trailing-30d gross** — churn, not confirmation. *Good flow is not a reason to be long into a double binary you cannot handicap.*

**SE — VETO'd.** Mega buy_ratio **exactly 1.00** ($52.7M, n=3, 15:43–17:17Z, **zero contamination**) — the cleanest execution profile in the book, on a $130.02–131.29 shelf, and the only name clearing the scale-relative 5% floor (8.41% of gross) with a clean BULLISH label. Directly opposite: ⚠ **three ITM/near-money call strikes closing on heavy volume — $7.09M + $6.5M + $6.1M ≈ $19.7M, roughly 37% the size of the entire buy print**. Insider MSPR **−100 for five consecutive months** with zero offsetting buys, corroborated independently by fz `insider_trans −30.67%`. RSI 76.77 after +37% in 30 days. TD Cowen Hold, PT **$100 (−24%)**. And it **reported this morning** — SE closed 131.51 against 114.80 yesterday, a **+14.6% earnings gap**, with IV rank crushing 78.7 → 20.4. The "accumulation" print landed *after* the binary resolved, which is exactly when index-rebalancing and dealer-unwind flow spikes. It also failed the confluence gate — one agent of ten flagged it.

**AXON — CAUTION, scored 0.** Block buy_ratio 0.856 ($79.7M, n=48) with `institutional-accumulation` at 2.56 (highest of the three), plus an independent sector-leader nomination in netted-IN Industrials. But the two "independent" families are plausibly the same beta wave measured twice — when XLI is the largest ETF inflow in the universe, every large-cap Industrials name shows buy-leaning DP prints almost mechanically, and `dp_block_to_float_ratio 0.0000738` is what beta looks like up close. Fundamentals invert the story: **operating margin 0.42%** against +34.6% revenue growth, **EPS −40.22% YoY**, **PE 243×**, three of four quarters missed, and an explicit *"Take Some Chips Off The Table"* downgrade. The OI build is decelerating to nothing (+4,787 → +2,916 → +663 → **+588**). Both debate advocates finished at **0.25 — a both-sides-low tie**.

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only` (2026-08-01 P0 #1).** Theses, structures and invalidations are carried in full; none is sized. This is routing, not suppression.

**GOOGL — VETO'd, and the VETO is the gate working.** On flow alone this was the most attractive short on the board: sweep-tracker's own words, *"the one mega-cap where sweep + cum_flow + price + screener all agree"* (bearish 3/5, cum_flow −$39.8M aligned, −3.84% day / −8.96% week with rv20 51.3% expanding against rv60 42.9%). The dealer book de-risked violently — net_dex +$3.028B → −$7.04M after ten straight positive sessions, total_gex +$142M → −$7.6M in lockstep, front-end IV panic **1.254**, the strongest in the mega-cap group. Then fundamentals: insiders are **BUYING** (MSPR +30.83), revenue +20.05% YoY, operating margin 33.11%, net margin 54.77%, **no negative GOOGL-specific catalyst**, and BNP Paribas reiterated Outperform/$420 the same session. The honest read is that GOOGL is the designated drag of a growth→value rotation — a macro-flow mechanism, not a company thesis. The debate agreed: the bull (arguing *against* the short) finished at 0.55 vs the bear's 0.45.

**NVDA — the day's best-constructed structure, routed anyway.** `multileg-strategist` found a clean **2026-10-16 P220/P180 debit put vertical**, `multileg_ratio` 0.971 on both legs, volumes matched within 2.6%, genuinely **opening** (the 220P built +30,028 on 08-10), **repeat count 2**, and correctly term-structure-anchored: at the traded 66-DTE tenor the curve is **flat** (the front-week backwardation is the macro stack), so it is a directional bet, not disguised vol timing. Today's −$51.5M net-premium flip actually *resolves* the flow_conflict that flagged this same structure on 08-10. Every structural check passes — and the quant still docked it **−3** on a 30d cum_flow of **+$255M bullish**. Routing rule and flow conflict agree from different directions.

**MU — dissolves on inspection.** Sweep-tracker had 5-of-5 bearish sessions and the single-leg scan graded it `OPENING_PUT_PRIME`, the top tier of the validated hierarchy. But the driving print is a **strike-1100 put against an 855.4 spot, delta −0.965, ~zero extrinsic, $2.46M** — stock-replacement financing, not directional conviction. Accumulation-hunter disqualified its DP tape (52%+ of mega premium at 20:00:15–20:12:44Z at the identical price $868.52; surviving blocks ~$12 below mid). The one genuinely supportive leg is the OI build at 58.9% put-dominated, which **passes the C4 opening gate — the only name today to do so**. Not enough against +$164M of opposing flow.

### Sweep ledger (informational — 0 rubric points)

Persistence-ranked, 5-day window. The sweep-persistence rubric line was removed 2026-05-23 (P0.3).

| Ticker | Dir | Persist. | 30d cum_flow | Alignment | Read |
|---|---|---|---|---|---|
| INTC | bearish | 5/5 | −$823M | **aligned** | Cleanest first-class name on the board |
| SPCX | bearish | 5/5 | −$52.9M | aligned | Thin name, no contract detail surfaced |
| MU | bearish | 5/5 | **+$164M** | **divergent** | Financing-structure driven → watch-only |
| SNDK | bearish | 5/5 | **+$1.17B** | **divergent** | Known put-sale netting contamination class |
| GOOGL | bearish | 3/5 | −$39.8M | aligned | Strongest mega-cap co-signal |
| NVDA / AAPL / SPX | — | 5/5 | opposing | **hedge-flow** | Demoted by the mega-cap filter |
| SPY / QQQ / SPXW | bearish | 5/5 | aligned | **CPI event-hedge** | Aligned but flagged as tail-hedging, not conviction |

TSLA, MSFT, AMD, PLTR, META and AMZN all returned `dominant_direction: mixed` at 5/5 — no directional thesis by disqualifier rule.

---

## 4. LEAP Builds (6–24 months)

**Empty book.** No ticker cleared 6-of-9 gates. LEAP share of total DTE volume is only **4.0%** today — a thin lane, and it was not forced.

The `--min-dte 180` screen was dominated by disqualifying patterns rather than conviction:
- **Covered-call WRITES dressed as OI growth** — SPHR Feb-2027 $180C (`prev_ask_volume` 0 vs `prev_bid_volume` 9,151 = 100% bid-side, i.e. call *selling*); CXW $35C, same pattern.
- **Sub-C12 names** — MPT $4.02, KOS $2.555, GRAB $3.73 fail the $5 price floor. **VNET** was the one genuinely ask-dominant bullish print (8,436 ask vs 3,045 bid) and fails liquidity at **$27.5M ADV < $50M**.
- **OTM put hedges** — HL, AG (silver miners), DRAM; plus SLV/RUT/VIX lottery strikes.

Three candidates cleared C12 and reached verification. **All three failed Gate 4 (90-day cumulative premium accretion):**

| Ticker | 10d oi-trend | 90d cum-flow | Verdict |
|---|---|---|---|
| TTD | BUILDING 10/10, +307,005 | **MIXED −$38.2M** on ~$772M gross | Fresh DTE-528 $15C print is bid-side dominant = call *selling* |
| VRT | BUILDING 10/10, +159,815 | **MIXED −$6.07M** on $3.44B gross (0.18%) | Long-dated prints appear intermittently, not as a persistent build |
| DIS | BUILDING 10/10, +126,007 | **BEARISH −$49.2M** | Roll reads as position management inside bearish flow |

The pattern is consistent: **open interest is turning over without net directional accretion.** No cross-horizon confirmation either — none of NBIS, SE or AXON appears anywhere in the DTE>180 list.

---

## 5. Volatility Surface

**The standout read of the day is a dispersion mispricing, not a directional vol call.** Index IV sits near the bottom of its own distribution (SPY percentile **5.95**, QQQ **2.38**) while single-name realised vol in the AI/semis complex runs 4–12× index rv20 — **SOXL 167%, NBIS 162%, SNDK 149%, CRWV 125%, MU 105%, AMD 81%, TSLA 63%, MSTR 55%, GOOGL 51%** against SPY 13.7% and RSP 10.4%. Critically, single-name *implied* has not caught up either: **every AI/semis name screened carries strongly negative VRP**. Index vol cheap + single-name IV cheap relative to RV + single-name RV extreme is a **correlation mispricing** — buy single-name vol, stay flat index vol. Sizing that view belongs to a dedicated dispersion book, not this report's rubric.

| Ticker | raw / shape / base_shape | kink (expiry) | prom% | IV %ile (n=84) | VRP | front-end | implied move |
|---|---|---|---|---|---|---|---|
| SPY | CONTANGO / KINKED / **BACKWARDATION** | 10d (08-21) | 11.6 | 5.95 | +0.0037 FAIR | 0.77 | 1.65% |
| QQQ | CONTANGO / KINKED / FLAT | 3d (08-14) | 7.0 | 2.38 | −0.0479 NEG | 0.835 | 2.52% |
| NBIS | BACKWARD / KINKED / BACKWARD | 38d (09-18) | 21.0 | 34.52 | **−0.4915** | **1.279** | 23.16% |
| SNDK | BACKWARD / BACKWARD / BACKWARD | — | — | 0 | **−0.6354** | 1.176 | 17.40% |
| CRWV | BACKWARD / BACKWARD / BACKWARD | — | — | 61.90 | −0.2912 | **1.260** | 19.95% |
| MU | BACKWARD / KINKED / BACKWARD | 10d (08-21) | 23.9 | 5.95 | −0.3429 | 0.944 | 10.87% |
| AMD | BACKWARD / **CONTANGO** / CONTANGO | — | — | 13.10 | −0.2747 | 1.021 | 9.37% |
| GOOGL | BACKWARD / KINKED / **CONTANGO** | 3d (08-14) | 6.7 | 4.76 | −0.1457 | **1.254** | 6.13% |
| TSLA | BACKWARD / KINKED / BACKWARD | 13d (08-24) | **76.0** | 0 | −0.2285 | 1.015 | 6.34% |
| MSTR | KINKED / KINKED / BACKWARD | 17d (08-28) | 11.3 | 17.86 | +0.0454 FAIR | 0.898 | 12.87% |

> **Substrate hygiene applied, and it mattered.** **7 of 10 raw term-structure labels flipped** under `scripts/term_structure_hygiene.py` (min_contracts 15 — a tunable, *not* audit-frozen); 5 of 10 flipped at the monotonic `base_shape` level. Separately, `uw historical iv-percentile-zscore --lookback-days 252` returned **`dates_used: 84` on every single name** — below the 120-day floor, so **every percentile above is provisional**, not first-class.

**Every KINKED name with a catalyst is macro, not idiosyncratic.** QQQ and GOOGL kink at 08-14 (**Retail Sales**); SPY and MU kink at 08-21 (**the session after FOMC Minutes**). None appears in the earnings-catalyst screen. Do not trade these as name-specific dislocations.

**No BACKWARDATION calendar candidate qualifies.** CRWV (1.26), SNDK (1.176) and NBIS (1.279) are all structurally backwardated at every filter level — genuinely, not as a 0DTE artifact — but all three carry front-end ratio **>1.10 with no resolution**, which is "event still pending, don't fade," not a calendar opportunity. Buy the straddle; don't sell the calendar.

**Idiosyncratic outliers, watch-only:** **TSLA's 08-24 tenor** spikes to 78.9% against 44.8%/40.7%/42.98% on immediate neighbours — 76% prominence, the largest of the batch, on 3,695 contracts, with **no identifiable catalyst**. Do not size. **MSTR 08-28** (11.3% prominence, thinnest kink relative to neighbours) — flag, don't size.

**Earnings vol lane** (`earnings-scout`): every screened name shows an elevated 3-DTE (08-14) bucket spanning CPI + PPI + Retail Sales *at once*. For the six retailers printing 08-18→08-20, the hygiene module cleanly separates it — the genuine earnings kink sits one tenor later at 08-21. **TGT** was the standout (SELL VOL full size, kink at 08-21 prominence 17.6%, 17 tenors kept / 0 dropped, 1,785 contracts, front-end 1.575, skew TAIL_HEDGING) — see §7 for why it still doesn't trade. HD (moderate-full), WMT (moderate), LOW / TJX / ROST (half each, on flat or unmeasurable back-month skew) all failed the confluence gate at one agent. **CSCO** (earnings 08-12, *the same day as CPI*) and **AMAT** (earnings 08-13, PPI day; its detected kink is at 09-18, which does **not** match the earnings date and therefore fails the "kink AT the earnings expiry" gate) are both explicitly **macro-contaminated** — CALENDAR rather than SELL VOL. ADI and BABA: SKIP, `implied_move: null`.

---

## 6. Risk & Correlation

**Macro headline:** stagflationary tilt — core PCE 3.29% and core CPI 2.81% against payrolls **−23k** and unemployment 4.1%, with the 10Y at **4.72% and rising** and the USD weakening. Forward calendar: **CPI T+1**, PPI T+2, Retail Sales T+3, FOMC Minutes T+7, OPEX T+8, Jackson Hole T+16.

**Correlation clusters** (`uw risk portfolio-correlation` against today's candidates, not the static watchlist):

| Pair | corr | Action |
|---|---|---|
| **NBIS / MU** | **0.792** | Cluster `AI_compute_memory_cluster`; NBIS kept (raw 3 > raw −1), **MU −1 tier** |
| SE / AXON | 0.516 | Below the 0.60 soft-watch floor — not surfaced |

> **Audit annotation:** NBIS is **long** and MU is **short**. At 0.792 with opposite signs these are *offsetting*, not duplicative — economically a partial hedge, not a doubled bet. The 2026-05-15 P1.4 threshold is direction-agnostic and forbids discretionary reclassification, so it was applied as written and the mismatch recorded. Immaterial today (MU routes to `watch_only` regardless), but a candidate for sign-conditioning at a future audit.
>
> **Tool defect:** `sector_breakdown` returned `{"Unknown": 7}` with a *"CONCENTRATION: 100% of tickers in Unknown"* warning. The sector-classification leg is dead for all seven names; the warning carries zero information and was ignored. Only the price-correlation matrix was used.

**Gates applied.** Every call carries all nine `gate_verdicts` keys in `decision.json`. Summary of what actually fired: **regime** on the three shorts; **panic** on GOOGL (1.254), NBIS (1.279) and TGT (1.575); **VRP contradiction** on TGT (short-vol into negative/fair VRP with no positive VRP measured anywhere); **cluster** on MU; **sector** on NBIS, SE; **fundamentals** VETO on GOOGL and SE, CAUTION on NBIS and AXON; **event_risk** on all but NVDA (exempt — defined-risk debit vertical through the print); **debate** on NBIS, SE, TGT, AXON; **rubric_regime** half-cap on everything (non-binding — nothing reached half).

**Fundamentals verdicts (top-5):**

| Ticker | Verdict | The contradicting facts |
|---|---|---|
| NBIS | **CAUTION** | Insider MSPR −73.42 (5 straight negative months); op margin −70.55%; Burry short at $211.77; earnings T+1 |
| GOOGL | **VETO** | Insiders **buying** (+30.83); revenue +20.05%; margins 33.11%/54.77%; **no negative catalyst** — fundamentals fight the short |
| SE | **VETO** | Insider MSPR **−100 five straight months**; earnings resolved today; RSI 76.77; TD Cowen PT $100 (−24%) |
| TGT | CONFIRM | — (3/3 beat streak, insiders buying) |
| AXON | **CAUTION** | Op margin 0.42%; EPS −40.22% YoY; PE 243×; miss_streak 3-of-4; explicit downgrade |

**Breadth cross-check (advisory):** 275 advancers / 226 decliners, **`pct_green` 54.67%**, avg change +0.19%. `divergence_flag: false` — and note this is the *inverse* of the usual distribution tell: the index is red while most names are green. Top mover KKR +6.88%, worst APP −5.99%.

**Adverse-flow exit — MSFT.** The carried `conviction_2026-08-10` group holds one name. Yesterday's thesis was a LOW-tier long (raw 6) on ACCUMULATION + OI BUILDING 5/5 + an Oct16 510C/550C bullish vertical, leaning on a +$727.8M bullish 30d cum flow. Today: **`flow_direction: bearish`, net flow −$46.75M** (#3 on the market-wide bearish screener) — on `volume_ratio` **0.54**, i.e. barely half normal participation. `LARGE_DARK_POOL` ($345.9M) and `OI_SHIFT` (+134,481) alerts fired at high severity, but **accumulation-hunter disqualified MSFT today at 93.4% closing-cross contamination** — that $345.9M print is almost certainly the same artifact, so the alerts are *not* confirmatory. **Recommendation: exit MSFT.** The `fz quote-drift` tripwire showed no fundamental deterioration; the exit case rests entirely on flow.

**Hedge sleeve: none. There is nothing to hedge.** The conviction book is empty, net delta is zero, and directional skew is undefined — nowhere near the ≥0.6 threshold that triggers a sleeve. Buying protection against a flat book is a naked long-vol punt wearing a hedge's clothing. The only carried exposure is MSFT, and closing it is strictly cheaper than insuring it.

On the **VIX call ladder** (`multileg-strategist` flagged it as the most persistent multi-day theme in the book — strikes 18.5/20/22/23/24/35 across Aug19/Sep16/Oct21/Nov18, ≥3 sessions): a prior session ranked it worst of three hedge options, and that ranking survives re-examination, though the case *for* it has genuinely strengthened. In its favour: index vol is at the bottom of its own distribution, QQQ VRP is negative, and both indices are in negative gamma with ATM put walls — index optionality is measurably cheap. Against it: every one of those facts argues for owning **index optionality**, not **VIX convexity**. VIX at 15.28 and −7.39% over five sessions means the ladder has been bleeding carry for at least three; strikes at 22/24/35 only pay on a genuine shock, while a merely-bad CPI moves SPY 1–2% and the ladder decays through it. And today's panic is **name-specific, not index-wide** (GOOGL 1.254, NBIS 1.279 against index IV in the bottom decile) — buying index-vol convexity to hedge single-name event pricing is a basis mismatch. Ranking: (1) do nothing / flatten MSFT; (2) if unseen exposure exists, long near-dated QQQ gamma — negative VRP makes it the cheapest correct expression and it participates in an ordinary bad print; (3) VIX call ladder, last.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Empty — no name reached MEDIUM (7).** Top score was NBIS at 3. The full audited breakdown for all seven scored calls is serialized in `analyses/daily/2026-08-11/decision.json`; the summary table in §3 carries the tier, direction, gates and final size for each.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: not printable this cycle. The HIGH and MEDIUM bands are **structurally empty** — this is the 8th consecutive cycle in which the out-of-regime freeze-lift cannot run for exactly that reason, and per-tier expectancy over an empty band is undefined. The LOW band holds one un-sized name. The live sizer remains the win-rate ladder in any case.

### Why nothing traded — the seven failure modes were all different

This matters more than the empty result: an empty board produced by seven *different* kill mechanisms is credible, where seven instances of the same mechanism would suggest a stuck gate.

- **NBIS** — genuinely clean institutional buying, killed by its own balance sheet, its own earnings at T+1, and a CPI print landing the same morning.
- **GOOGL** — the only mega-cap where every flow read agreed, VETO'd because insiders are *buying* a name growing revenue 20% with no negative catalyst.
- **SE** — a perfect 1.00 mega buy_ratio sitting directly opposite the strongest call-book distribution signal in the scan, on a name that reported this morning.
- **TGT** — the best-instrumented vol setup of the day, unsellable because **no positive VRP was measured anywhere on the tape**.
- **AXON** — the only favourable sector read, and the debate produced a **0.25/0.25 tie**: neither advocate cleared a coin flip.
- **NVDA** — a structurally flawless institutional put vertical, routed by the short rule and independently docked −3 on +$255M of opposing flow.
- **MU** — the Tier-1 "bearish signal" was a delta −0.965 financing put.

### Three structural facts underneath today's book

1. **Today's mega-cap dark-pool tape is 67–93% closing-cross artifact.** Across MU, AMAT, MSFT, AVGO, APO, OKLO, IBM and the mega-cap complex, the bulk of mega-tier premium executed 20:00:06–20:12:44Z at a single repeated price, frequently re-reported at 21:19:36Z at the *exact same price*. Only three names had a genuinely intraday institutional footprint. Any accumulation read that does not timestamp-filter is reading the closing auction.
2. **The sector-persistence field is fully degenerate** — 1.0 across all eleven sectors. The conditional sector-leader gate's durability clause passes trivially for everyone and discriminated nothing.
3. **`dark_pool_accumulation` has zero backtest substrate** (`total_signals: 0`), and `earnings_vol`, `multileg_directional` and `oi_build` are not supported classes. **Five of seven calls carry `win_rate: NA(substrate)`** — not a low win rate, an *unmeasured* one. Only the two `bearish_flow` names received a real quote (0.5816, n=141 complete windows, market_excess +0.0567 — a class-level figure that per C49/C53 is not tradeable edge).

### Rubric (frozen, version `2026-06-12`)

```
Daily conviction score = Σ:
  +1  MECHANIZED DEX flip / vanna-squeeze in trade direction (verified SIGN CHANGE via scripts/dex_flip.py, not a level)
  +3  3+ aligned signals in accumulation-hunter — CONJUNCTION (C11): full +3 only when cum_flow_30d confirms
      (sign aligned AND |cum_flow_30d| >= $50M); else halved to +1
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days >= 5)
  +1  uw insights conviction-matrix DIRECTIONAL_LONG conf > 70 — CONDITIONAL: only when class == leap_directional
  +1  cumulative-premium-flow net directional accretion (30d) — INTENT-SCREENED (no C28 distribution_flag;
      no deep-ITM sub-parity ex-div calls)
  +1  sector-rotation-strategist names ticker as single-name leader — CONDITIONAL: (a) persistence >= 0.6
      AND (b) cum_flow_30d aligned AND (c) |cum_flow_30d| >= $50M
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (play type ANCHORED TO TERM STRUCTURE)
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist top-5 (OPEX week only)
  -2  contrarian-scanner overcrowded long with rising pc-ratio-zscore (informed-flow CONTINUATION penalty,
      not a "fade the crowd" signal)
  -3  flow_conflict — cum_flow 30d clearly OPPOSITE dominant_signal_class
  -1  flow_conflict_lite — 30d read MIXED / bottom-quartile magnitude
      (flow_conflict and flow_conflict_lite are MUTUALLY EXCLUSIVE — apply ONE)
  # TIER GATES (risk-monitor, 2d) — contribute 0 to raw_score:
  -1 TIER  correlation cluster (pairwise corr >= 0.70)
  -1 TIER  regime conflict with trade direction
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | HIGH | full (subject to the 3-of-4 load-bearing-tool gate + win-rate gate) |
| 7–8 | MEDIUM | half |
| 3–6 | LOW | starter / watch-only |
| ≤ 2 | drop | filtered |

**Rubric-line flags raised by the quant for the next `/calibration-audit`:**

1. **The `+1 multi-day OI build` line fired 6-of-6 and is direction-agnostic — and today it paid three names for evidence pointing the wrong way.** Every scored name returned `consecutive_build_days: 5`. Splitting by option type: the build runs *against* the thesis for **NBIS (59.9% put on a long), NVDA (63.4% call on a short) and GOOGL (67.6% call on a short)**, and is pure noise for SE (49.9/50.1). Only AXON and MU agree with their theses. A line that fires universally *and* whose underlying quantity anti-correlates with the thesis half the time is adding a constant plus noise. A **direction-conditioned variant** (award only when the build's call/put skew agrees with the trade direction) would be tightening-only and therefore freeze-safe; on today's board it would move NBIS 3→2 (below the LOW floor), GOOGL 1→0, NVDA 0→−1.
2. **The C11 absolute-vs-scale floors are asymmetric and caught opposite names.** NBIS clears $50M ($225.8M) but fails 5%-of-gross (2.71%); SE clears 8.41%-of-gross but fails $50M ($16.1M). Both halved. Worth checking whether the conjunction has *ever* paid a full +3 post-freeze.
3. **Sub-1%-of-gross nets drove full −3 deductions on two names.** NVDA's +$255M conflict is 0.92% of a $27.8B gross book; MU's +$164M is **0.24% of $69.5B** — statistically near-indistinguishable from balanced, yet mechanically read as a full −3. Applied as written under the freeze; flagged.
4. **The clamping artifact is live and large.** `bullish_flow` clamped rows realised 0.6667 against 0.4126 on complete windows — a **+25pp recency inflation** sitting inside the tool's own headline. The P0.3 clean-query protocol is earning its keep; the headline was never quoted.

---

## 8. Watch-only — single signal, no confluence

Surfaced by one agent, failed the ≥2-agent gate. Journaling only — not for entry.

- **Sector-rotation leaders (1 agent):** EQT, XOM, OXY, DINO, VLO (Energy) · VRT, RKLB, UNP (Industrials) · SOFI, BX, V, IREN, GS (Financials — note the leg is regional-banks-specific via KRE, not broad XLF)
- **Earnings vol (1 agent):** HD (SELL VOL moderate-full), WMT (moderate), LOW (half — back-month skew COMPLACENT), TJX (half — back-month unmeasurable), ROST (half + execution-risk flag: only 77 contracts at the kink tenor), CSCO (CALENDAR, macro-contaminated — earnings *on* CPI day), AMAT (CALENDAR, macro-contaminated + false-lead kink at 09-18 ≠ the 08-13 earnings date)
- **Sweep persistence (1 agent):** INTC (cleanest aligned bearish, 5/5), SPCX (5/5 bearish, thin)
- **Multileg (1 agent):** TLT Sept-18 82-strike straddle — a clean event play with a genuine local kink at Sept 18 (20.0% IV vs 12.0%/13.0% neighbours, n=2,781) against the **Sept 16 FOMC**; EWZ Oct16/Nov20 C37 calendar (weak 0.4pt contango anchor, no aligned whale ticket); MSTR Aug21/Oct16 C95 calendar (**unanchorable** — the raw KINKED label points at Dec-18, four expiries beyond the back leg)
- **Vol surface (1 agent):** CRWV, SNDK, TSLA (TSLA's 76%-prominence 08-24 kink has no identifiable catalyst)
- **Accumulation (1 agent):** SE — carried into §3a and `decision.json` as a confluence-gate failure because it reached the top-5 by score

**Screened out entirely, with cause:**
- **Financing / stock-replacement structures, not theses:** TLT C75/C76 (deep-ITM, ~$0.35 extrinsic — the same rolling family flagged 08-06 with strikes rolled 76/77→75/76), RTX C125 diagonal (delta 0.989, ~$99 ITM), TGT C80/C85 diagonal (delta 0.988+), the SPX/SPXW 7000C/8000P box family (size-matched pairs, confirmed recurring 08-03 through today), and the MU strike-1100 put (delta −0.965).
- **Explicit event hedges, not conviction:** SPY Aug21 C785/P760 strangle (spans CPI + PPI + Retail Sales + FOMC Minutes), SPXW Sept25 P6300/P6400 (standing crash hedge, 45 DTE past the CPI window), the VIX multi-expiry call ladder.
- **Data artifacts:** DRAM P30 pricing at $0.001/share on 56,900 contracts (degenerate/stale contract).
- **Contaminated accumulation reads:** SNDK (institutional-accumulation NEUTRAL at buy/sell 0.82, mega buy_ratio **0.0** = 100% sell-classified, largest print **$23.42 below NBBO mid**), AMAT (mega buy_ratio 0.012 = 98.8% sell — distribution, not accumulation), APO/OKLO/IBM/MSFT/AVGO (68–93% closing-cross contaminated).
- **`fz` lanes degraded:** the squeeze screen returned an unranked alphabetical page-1 (every row `A*`) and **every row across both `fz` screens carries the known upstream doubled-first-letter corruption** (`AARMK`→ARMK, `CCODI`→CODI, `QQMCO`→QMCO, `AABCL`→ABCL). The squeeze lane was treated as unavailable rather than trusted; the RS lane de-doubled to ARMK, CAH, CODI, QMCO. Advisory, 0 rubric points, no effect on the report.

---

*Fleet: 10 Phase 1 agents (opex-pin-strategist correctly not spawned — third Friday is 2026-08-21, outside the 5-day window; `leap-positioning-radar` re-spawned once after an API error). Step-0 cache: 22/22 payloads, 0 failures. C12 liquidity floor: 66 pass, 4 fail (^VIX index — expected, HP $43.2M ADV, LB $23.6M ADV, HTZ $2.45 price). Envelope validated against `schemas/decision_envelope.schema.json` — 7 calls, Σ score_components == raw_score on every one.*
