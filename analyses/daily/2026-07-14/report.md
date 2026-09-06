# Daily Market Analysis — 2026-07-14

## Executive Summary

- **Regime + GEX state:** TRANSITIONAL (trend UPTREND) — SPY 751.83, above 20SMA (744.89) and 50SMA (742.65), +1.91% 30d, −1.13% from the 90d high. VIX 16.5. **Breadth is negative and the divergence is the day's headline**: only 35.6% of optionable tickers show bullish flow (2,234 bull vs 4,035 bear), and just **40.4% of the S&P is green with a median change of −0.42%**. Next-session gamma: SPY **short-gamma** below a 759.96 flip; QQQ **long-gamma** pinned on a 719.75 flip with a dominant 720 call wall. Sector lean: Financials the only clean inflow; Technology **bifurcated** (semis bought, software distributed).
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`. Moot in practice today — the entire board is `skip`.
- **Next-session GEX (SPY/QQQ):** **SPY** — NEGATIVE/short-gamma · ZGL 759.96 (reliable, 1.06% above spot) · call wall 760 / put wall 740 · *trend-amplifying into 755–760, do not default to a wide condor with the flip this close.* **QQQ** — POSITIVE/long-gamma · ZGL 719.75 (spot sits **on** it) · call wall 720 (+$568.5M, the dominant strike in the chain) / put wall 700 · *pin setup at 720.* Advisory, 0 rubric points — see §2.
- **Top swing build:** **None.** No name reached even LOW tier. The best-corroborated thesis on the board (TSM short, 5 agents, the fleet's only verified mechanized DEX flip) scored **raw 2** and dropped.
- **Top LEAP candidate:** **None.** Zero names cleared the 6-of-9 gate; all three liquidity-clean candidates (WULF, SLS, RIG) failed the required cumulative-premium-flow accretion gate.
- **Biggest risk:** Not a position — it's the **data**. Today's tape is pervasively artifact-contaminated: the mega-cap dark-pool tape is closing-cross crossed market-wide (20:00Z–21:56Z), ~85% of the multileg tape is financing/rolls/crosses, and the 07-17 OPEX expiry makes the term-structure KINKED gate unreachable on 0-of-13 and 18-of-19 names respectively. The desk's real exposure today is to **mistaking mechanics for conviction**.

> **This is the 10th consecutive empty conviction book, and only the second-ever all-DROP board** (nothing reached even LOW). Per the 2026-07-04 audit, the DROP pile has outperformed the traded book (0.477 vs 0.406) — empty-board discipline is the system's best-graded behaviour, not a failure. Stages 2b (fundamentals-gate) and 2c (bull/bear debate) were **skipped**: they can only cut size, and there is no size to cut (2026-07-13 precedent).

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** `TRANSITIONAL — Mixed signals, reduce position size, wait for clarity`. Trend **UPTREND**. Guidance: *"Half position sizes. Favor defined-risk strategies. Iron condors in range."*

The regime label and the tape disagree in an informative way. SPY sits above both moving averages and mega-cap tech was strong (NVDA +4.06%, CRWD +12.14%, SK Hynix ADR +27.29%), but underneath, **297 S&P names declined against 203 advancers** and the median name lost 0.42%. This is a narrow, top-heavy tape — a green index carried by a handful of names while the majority bleeds. That is the classic distribution backdrop, and it is why today's accumulation and confluence screens produced so little that survived scrutiny.

**Dispersion was extreme.** IBM fell **−25.21%** (the worst S&P mover) on a non-earnings day — its next print is 07-22, eight days out. SK Hynix rose +27.29%. When single-name realised vol runs this hot, "high IV rank" stops meaning "rich vol" (see §5).

**Per-index gamma (current-state EOD book; §2 carries the forward read):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 752.00 | 759.96 (reliable) | +$446.4M | NEGATIVE (spot below flip) | 760 (+$187.1M) | 740 (−$133.2M) |
| QQQ | 719.91 | 719.75 (reliable) | +$586.0M | POSITIVE (spot on flip) | 720 (+$568.5M) | 700 (−$96.4M) |
| IWM | ~294.5 | **unusable** (130.52/150.27/155.38/194.16/199.14 vs spot ~294–300) | — | — | — | — |

IWM's zero-gamma series is a data-quality failure, not a level — flagged, not traded.

**`uw options-flow dte-volume-share`:** 0DTE 28.8% · weeklies 36.3% · monthlies 21.6% · LEAPs 4.8% → `regime_hint: BALANCED`. Below the 50% 0DTE retail-dominance threshold, so no forced conviction downgrade; equally, no institutional-tape benefit of the doubt. **The 4.8% LEAP share is the thinnest bucket by a wide margin** — the market's attention is entirely in the front, which lowered the prior on any genuine long-dated build (§4).

**`uw historical vrp`:**
- **SPY: −0.0172, `FAIR`** — IV30 13.77 vs realised 15.49. *"IV close to realised — no clear edge from VRP alone."*
- **QQQ: −0.0655, `PREMIUM_BUYING`** — IV30 23.72 vs realised 30.27. **Vol is cheap versus realised on the Nasdaq book by ~6.5 vol points.** This single reading did more work today than any other: it aborted the contrarian fade book, disqualified short-premium structures on tech/semis, and is the reason a hedge should be bought rather than financed by selling.

**Macro backdrop (`scripts/fred_macro.py`):** Curve **normal** (10Y−2Y +0.40) · core CPI **2.81%** YoY · core PCE **3.41%** YoY · unemployment **4.2%** · payrolls **+57k** · 10Y **4.62%, rising** (+0.14 over 30d) · USD **strengthening** (+0.59 over 30d) · fed funds **3.62%**. A rising-10Y, strengthening-USD, core-PCE-at-3.4% backdrop is a headwind for long-duration equity risk and a hawkish frame for the banks' NII commentary.

**Forward event risk (Tier-1, next ~10 sessions):**

| Event | Date | Impact |
|---|---|---|
| **PPI (June)** | **2026-07-15, 08:30 ET** | **HIGH — tomorrow, before the open this GEX map is meant to inform** |
| Initial jobless claims | 2026-07-16 | MEDIUM |
| **Monthly OPEX (July)** | **2026-07-17** | **HIGH — mechanical pin/gamma unwind, T+3** |
| Initial jobless claims | 2026-07-23 | MEDIUM |
| **FOMC + press conference** | **2026-07-28/29** | **HIGH — ~T+11, inside any 1–4wk swing** |
| **PCE (June)** | **2026-07-31** | **HIGH — ~T+13** |
| CPI (July) | 2026-08-12 | HIGH (outside the window) |

Every Tier-1 print through PCE sits inside a swing horizon opened today. The empty book incidentally sidesteps the heaviest event corridor of the month.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — built from open interest that persists overnight — read forward as the *prior* for the next session's open. It is **prose-only, contributes 0 points** to the conviction rubric, and makes **no backtested predictive claim**. Predictive validation lives in `/weekly-analysis`'s rolling §2 backtest. Scope is **SPY and QQQ only**.

### SPY — short-gamma, but the flip is close
`spot 752.00 · ZGL 759.96 (zgl_reliable: true, 1.06% above spot) · regime NEGATIVE · total_gex +$446.4M · call wall 760 · put wall 740`

Spot sits **below** the 759.96 flip, so dealers are short gamma on the way up to 760 — expect trend amplification if spot pushes toward/through 755–760 (dealers buy into strength), with a looser downside cushion toward the 740 put wall. Note the tension: `total_gex` is *positive* while spot is *below* the flip. This is a narrow 752–760 band (~1.1%) rather than a wide pin — the book is not deeply short-gamma, just on the wrong side of a nearby flip.

**Structure bias:** debit call spread to the wall (752/760) if momentum confirms at the open; a tight iron fly centred 753–755 if the open stalls under the flip. **Do not default to a wide condor — the flip is too close for a confident vol-suppression trade.**

### QQQ — long-gamma, pinned on the flip
`spot 719.91 · ZGL 719.75 (zgl_reliable: true, 0.02% from spot) · regime POSITIVE · total_gex +$586.0M · call wall 720 · put wall 700`

Spot is razor-thin on top of the flip, and the **720 strike carries +$568.5M — by far the largest single-strike GEX in the book, ~1.3× the next five strikes combined** — a powerful magnet directly at spot. Reads as a pin: dealers long gamma right at 720, mean-reversion/vol suppression clustered tightly around 719–720 unless flow breaks the wall outright.

**Structure bias:** iron fly / short straddle centred at 720, with the 700 put wall 2.8% away giving reasonable downside runway for wing placement.

**Regime freshness — both indices: FRESH and UNSTABLE.** SPY flip-flopped NEGATIVE → POSITIVE → FULLY_NEGATIVE → NEGATIVE across 07-09/10/13/14; QQQ was FULLY_NEGATIVE on 07-13 and POSITIVE today. Both have flipped on 4+ of the last 10 sessions. **Treat today's regime read as low-persistence.**

**Mandatory caveats:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and re-computes ZGL/walls — especially acute for QQQ, where spot sits almost exactly on the flip and a small overnight OI shift could flip the regime sign entirely.
- **ZGL reliability.** Both of today's ZGLs pass the ±5% sanity check. **But QQQ's series is artifact-prone**: 3 of the last 10 sessions returned a sub-320 ZGL against a ~710–725 spot (07-01: 314.06; 07-08: 300.24; 07-09: 300.29) — the known GEX-grid bug. Today's 719.75 is **the exception, not the rule**; treat with elevated caution despite passing. IWM's series (130–199 vs ~294–300 spot) is outright unusable.
- **Gap risk voids the prior.** **PPI (June) prints 2026-07-15 at 08:30 ET — before the open this map informs.** A surprise can gap spot through either wall before dealers re-hedge.
- **OPEX week.** Monthly expiry 07-17 is 3 calendar days out. `expiry-heatmap` confirms the book is unusually front-loaded: SPY's 07-15 expiry is the #2 premium bucket ($172M) behind today's 0DTE ($545M), with 07-17 #3 ($122M); for QQQ the 07-17 monthly is #2 ($213M), ahead of 07-15 ($182M). **This book will decay and reprice fast into Friday.**
- **Tooling limit.** `gex --dte-max 1` errors — uw-pp cannot isolate the D+1 expiry. This is the standing 0–45 DTE book, the best available proxy, not the isolated next-session expiry.
- **ETF book**, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup (the validated stack)

The GEX walls above are a **map (advisory "where"), not a pin** — wall-as-magnet backtested NO_GO, as did every directional 0DTE signal. What validated is a **delta-neutral premium-selling** edge. **Advisory, 0 rubric points, and NOT a guaranteed edge.**

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `backtest_verdict` | GO_PREMIUM_SELL_INTRADAY | GO_PREMIUM_SELL_INTRADAY |
| win-rate (open-entry, gross) | 93.3% (n=60) | 86.7% (n=60) |
| **`mean_pnl_open_pct` (GROSS)** | **+0.282%** | **+0.393%** |
| **`mean_pnl_open_net_pct` (NET — lead with this)** | **+0.182%** | **+0.293%** |
| assumed round-trip cost | 0.10% | 0.10% |
| overnight-entry PnL | **−0.166%** | **−0.392%** |
| worst day (open-entry) | −1.40% | −2.453% |
| `vol_state` / VIX | LOW / 16.5 | LOW / 16.5 |
| `implied_move_pct` | 0.74% | 1.39% |
| `expected_range_pct` | 0.79% | 1.34% |
| **`size_scalar`** | **0.5** | **0.25** |
| `suggested_structure` | iron fly / short straddle centred **751.91**, wings ≈ ±0.79% | iron fly / short straddle centred **719.72**, wings ≈ ±1.34% |
| `caution` | none | **Front-end backwardation (0DTE IV 1.34× VIX) — event/gap risk; half size** |

**`pnl_basis`:** percent-of-underlying-**spot notional, GROSS** of transaction costs (0.8×1σ premium captured minus realised |open−close|). **It is NOT premium-collected and NOT margin-relative** — so +0.182% net on SPY is tiny in absolute terms. Vilkov (2024) found an unconditional 0DTE condor flips to negative net Sharpe once costs are charged; **the gross win-rate overstates a negatively-skewed seller's edge.**

- **When:** enter at/after the open once the overnight gap resolves; **hold to the close; never carry overnight** (overnight entry is negative on both indices — the gap erases the edge). **If it gaps beyond the wings, stand aside.** With PPI at 08:30 ET tomorrow, a gap is live.
- **How much:** `vol_state` is **LOW** on both (VIX 16.5, below the 16.9 tercile bound) — the thin-edge regime. Mean PnL by VIX state: SPY LOW +0.075% / MID +0.317% / HIGH +0.454%. **The LOW bucket is where this edge is weakest.** QQQ carries an explicit front-end-backwardation caution and its `size_scalar` is only **0.25**.
- **Direction:** none. Delta-neutral. Do not add a tilt.
- **SPY ≈ SPX** (validated identical). **QQQ is the weaker vehicle** (Nasdaq index book unavailable) — lower confidence.
- **Promotion bar:** stays advisory / 0 points **permanently** until both a vol-shock day enters the sample (**the short-vol left tail is currently UNSAMPLED**) and net expectancy clears a tail-aware bar. Win-rate is explicitly **not** the promotion metric.

## 2a. Swing Dealer Positioning (1–4 weeks)

**The dominant finding is negative: the DEX series whipsaws sign almost daily across every index and most single names** — exactly the low-magnitude whipsaw pattern the 2026-06-12 audit (P0.4) demoted this line for (+3 → +1, mechanized). Only **one name** in the entire fleet cleared the mechanized sign-change bar.

| Symbol | DEX (07-14) | 5d trajectory | Mechanized flip? | Vanna | Swing bias |
|---|---|---|---|---|---|
| SPY | +$16.36B | sign flips on 4 of last 5 transitions | **NO** — no ≥3-session prior run exists | LONG (call-heavy) — not squeeze-eligible | FLAT |
| QQQ | +$3.27B | volatile, no trend | **NO** | SHORT (put-heavy) — **VIX leg unverifiable → no squeeze** | FLAT |
| IWM | −$2.98B | persistently negative 5 of 6 | **NO** — a sustained *level*, no run to flip against | SHORT (put-heavy) — VIX leg unverifiable | FLAT (unscored bearish lean) |
| **TSM** | **−$451.6M** | **+$733.3M (7/10) → −$248.7M (7/13) → −$451.6M (7/14)** | **YES** | put-heavy (+1,877), consistent | **SHORT** |
| IBM | −$1,244.2M | 7 straight positive → flip | **technically yes — DISQUALIFIED** | — | none |
| NVDA, MU, TSLA, INTC, GEV | sustained levels | no flip | **NO** | mostly call-heavy | FLAT |

**TSM is the fleet's only verified mechanized flip.** Evidence: `net_dex` 7/10 **+733.3M** → 7/13 **−248.7M**, with the prior three sessions (7/8, 7/9, 7/10) all positive; |flip| 248.7M = **1.29× the trailing-10-session median floor** (192.7M = 0.25 × 770.75M median); **confirmed persisting 7/14 at −451.6M** — a second consecutive negative session, not a one-day whipsaw. Per-strike GEX confirms the flip is broad-book (largest single strike ~−$10.8M at 420), not a single-strike artifact. The ZGL regime went FULLY_NEGATIVE on 07-01 and deepened from −19.2M to −32.7M through 07-14.

**But the agent's own caveat is decisive and honest: this is coincident, not anticipatory.** TSM already fell ~11% (475.38 → 421.58) over the window, *before* the 7/13 flip; GEX went negative on 07-01, also before. **The flip is confirming an in-progress decline, not leading it** — which undercuts the "flip precedes price" framing the line rests on. Combined with OPEX resetting the 0–45d book in 3 days and earnings on 07-16, TSM's flip earned its +1 and nothing more.

**IBM's flip was disqualified, correctly.** It technically cleared the mechanics (7 straight positive sessions → −$1,244.2M, vs a ~$300.1M median floor), but **07-14 is the exact day IBM fell −25.21%**. A same-day options-delta repricing following a quarter-of-value crash is a **mechanical consequence of the move, not a forward-looking signal** — the move is already fully in the tape. IBM's ZGL series is also wildly unstable (115/279/125/133/279/115.55/146.98/156.79/119.26), the known grid-artifact class.

**The vanna-squeeze disjunct cannot fire on any name.** QQQ and IWM both show the qualifying put-heavy book, but the falling-VIX leg requires a **dated VIX series, and ^VIX has no clean 2026 source** in this environment (the Yahoo chart API returns prior-year candles for 2026 dates — a documented, verified bug). Step 0's VIX 16.5 is a single scalar, not a trajectory. The agents correctly declined to fill VIX out-of-band rather than manufacture a squeeze.

**Two tool disagreements worth flagging:** INTC sits on the bearish net-premium leaderboard (−$36.8M) with **zero DEX corroboration** — and §7's artifact finding shows that net premium is substantially *manufactured* by a financing ladder. GEV topped the bearish confluence screen (score 6→5) with **zero DEX corroboration** either.

## 2b. Sector Rotation

**Rotation regime call: `no_change` (confidence LOW).**

**Persistence is non-discriminating today and must not be read as conviction.** `sector-flow-persistence` returned `persistence_score = 1.0` (max) with `trend: INFLOW` for **9 of 11 sectors** across 07-08…07-14 — every sector net-positive every day. A gate that everything passes separates nothing. The real signal is in magnitude and trajectory.

| Sector | Persistence | Today net flow | 5d trajectory | Read |
|---|---|---|---|---|
| Technology | 1.0 | $2,780.9M | 2.84B→3.21B→**4.07B peak**→1.21B→2.78B | Magnitude-huge but **bifurcated, not a rotation** |
| Communication Services | 1.0 | $393.8M | 343M→822M→**1,807M spike**→409M→394M | One-day outlier, reverted to baseline |
| **Financial Services** | 1.0 | **$381.0M** | 129M→314M→235M→244M→**381M (5d high)** | **Cleanest signal in the set** |
| Consumer Cyclical | 1.0 | $307.7M | 160M→595M→**831M peak**→383M→308M | Decelerating 2 straight days |
| Healthcare | 1.0 | $278.5M | 249M→209M→194M→222M→279M | Stable; biotech soft underneath |
| Basic Materials | **0.6** | $77.1M | +5.9M→**−9.2M**→+9.8M→**−2.5M**→+77.1M | **Watch-only** — textbook single-day spike after two negative days |
| Energy | 1.0 | $70.6M | 95M→26M→49M→100M→71M | Below median, no trend |

**The Technology contradiction — resolved as compositional, not measurement error.** `uw risk market-regime` reports Technology **−$58.4M outflow** while `uw options-flow sector-flow` reports **+$2,780.9M inflow** on the same date. The ETF layer decomposes it:
- **SMH (semis):** +$14.35M 5d flow, sweep tape strongly bullish (**+$59.3M net call premium**, ask-side dominant).
- **IGV (software):** −$2.08M 5d flow, sweeps **−$4.94M**, DP heavily sell-tilted ($162.7M below-mid vs $21.0M above-mid).
- **XLK (broad):** −$1.16M, MIXED — **not confirming the GICS headline.**

**Technology is bifurcated: semis are being bought via options; software and mega-cap services are showing dark-pool distribution.** The GICS inflow is a semis phenomenon; the regime tool's outflow is picking up the software side. Neither is wrong — they are different netting bases on different sub-currents of one bucket. **Do not score a blanket Technology rotation call on this.** Step 0 corroborates: the day's top bullish net-premium names are almost entirely semis (NVDA, MU, SNDK, TSM, INTC, UMC).

**Single-name leaders vs the conditional +1 gate** — (a) persistence ≥0.6, (b) cum_flow_30d aligned, (c) |cum_flow_30d| ≥$50M:

| Ticker | Thesis | (a) | cum_flow_30d | (b) | (c) | +1? |
|---|---|---|---|---|---|---|
| **MU** | semis, bullish | ✓ | **+$282.0M** | ✓ | ✓ | **YES** |
| **SNDK** | semis, bullish | ✓ | **+$988.2M** | ✓ | ✓ | **YES** |
| NVDA | semis, bullish | ✓ | **−$2.1M (MIXED)** | ✗ | — | NO |
| GS | financials, bullish | ✓ | +$12.2M | ✓ | ✗ | NO — informational |
| JPM | financials, bullish | ✓ | +$41.8M | ✓ | ✗ (close) | NO — informational |
| ABBV | biotech, bearish | ✓ | −$39.7M | ✓ | ✗ | NO — informational |
| ISRG | biotech, bearish | ✓ | −$8.5M | ✓ | ✗ | NO — informational |

Financial Services is the strongest *sector-level* signal (persistence, trajectory, and ETF cross-confirm all agree), but neither GS nor JPM has accumulated $50M over 30 days — consistent with a **fresh, accelerating rotation rather than an established build**. Worth re-checking in 2–3 sessions. Note §8: the financials signal is very likely **bank-earnings-reaction flow** (JPM/GS/BAC/WFC/C all reported this morning), not slow accumulation.

**ETF flow tape (advisory — strengthens the conditional +1, adds no points):**

| Rank | ETF | 5d net flow | Trend | GICS agreement | Read |
|---|---|---|---|---|---|
| 1 in | **EWY** (Korea) | +$38.50M | BULLISH | n/a (geographic) | **Distribution into strength** — DP heavily sell-tilted ($385.7M below-mid vs $87.7M above-mid), sweeps flat/slightly bearish (−$3.5M) despite topping the inflow rank. SK Hynix +27.3% today. **Not a fresh long.** |
| 2 in | **XLF** | +$21.62M | BULLISH | **AGREE** | DP buy-tilt ($36.1M vs $28.1M), sweeps strongly bullish call-dominant (+$17.8M) — confirms rotation-in |
| 3 in | **SMH** | +$14.35M | MIXED | agrees w/ semis leg only | DP sell-tilt ($240.3M below-mid — discounted as creation/redemption noise), but sweeps strongly bullish (+$59.3M ask-side) — options flow weighted higher |
| 3 out | **IGV** | −$2.08M | MIXED | **DISAGREE w/ GICS Tech; agrees w/ regime tool** | Cleanest outflow confirmation — DP $162.7M below-mid, sweeps −$4.9M put-dominant. **This is the piece that explains the Tech discrepancy.** |
| 2 out | **GDX** | −$13.20M | BEARISH | consistent w/ Materials instability | DP balanced, sweeps mixed — **no clean signal, not a rotation-out call** |
| 1 out | **XBI** | −$14.03M | BEARISH | partial | Within-sector rotation out of biotech/device (ABBV, ISRG) while Healthcare aggregate is mildly positive |

**Swing-book implication:** long Financials leaders (GS/JPM — sector conviction high, but neither clears the $50M gate; size light, await confirmation) and semis leaders (MU/SNDK — gate-cleared); avoid a broad Tech or software long off the GICS headline; treat EWY as distribution-into-strength. **None of this survived the full rubric — see §7.**

---

## 3. Swing Setups (1–6 weeks)

### **EMPTY — no name reached even LOW tier.**

Six names cleared the ≥2-agent confluence gate. All six scored **≤2** and hit the drop floor. This is only the second all-DROP board on record. The scoring detail is in §7; the short version is that **every marginal line was declined either by the flagging agent itself or by a documented artifact screen.**

### 3a. Long swings (regime-aligned)
**None.** SNDK (raw 1) and NBIS (raw −1) were the only long candidates; both failed. NBIS is the more instructive: three agents read the **same 07-24 expiry** three different ways — sweep-tracker saw a bullish 350C build (91.5% opening-dominant), vol-surface's own expiry-heatmap showed **heavily put-skewed premium ($82M @ 07-24)**, and multileg independently identified the 170P Jul-17→Jul-24 leg as an **OPEX calendar roll** (Jul-17 leg vol/OI 0.60 = closing; Jul-24 leg vol/OI 1.50 = opening). The stock fell −7.80% on the day. When three agents read one expiry three ways, the honest answer is no position.

### 3b. Short / fade swings (defined risk only)
**None.** The contrarian fade book was **aborted wholesale on the VRP gate** — see §5. TSM (raw 2) and MSFT (raw 2) were the strongest shorts and both dropped.

### Sweep ledger (informational — 0 rubric points)

The sweep-persistence line was removed on 2026-05-23 (P0.3) after a −22pp marginal contribution across two audits. **Today's tape is dominated by OPEX mechanics and index financing, not conviction.**

**(a) Genuine multi-day persistence, direction clean, liquidity-cleared:**

| Ticker | Dir | Persist. | Premium (5d) | Opening confirm | Read |
|---|---|---|---|---|---|
| **MSFT** | Bearish | 4/5 | $680.1M | ΔOI 2301/vol 4255 = **54%** | The only mega-cap clearing the hedge-flow filter (cum_flow_30d **BEARISH −$859.8M, aligned**). ⚠ **But the largest building OI is *calls* (397.5C/400C/395C)** — likely covered-call supply into OPEX, not a put-bid bearish bet. |
| **NBIS** | Bullish | 4/5 | $490.7M | ΔOI 15063/vol 16457 = **91.5%**, largest build IS the 350C | ⚠ Stock **−7.80% today** despite persistent bullish premium; contradicted by put-skewed premium on the same expiry. |
| **ORCL** | Bearish | 4/5 | $534.2M | ΔOI 11773/vol 13642 = **86%**, but top contract is a *call* | ⚠ **Parity-arb caveat** — the Step-0 Tier-1 200P floor block is an unresolved deep-ITM mechanical print; `sweep-ratio` shows an ORCL 250C at **$0.01** ($2,922 premium) = lotto noise. |
| **SPCX** | Bullish | 4/5 | $610.3M | ΔOI 6344/vol 19736 = 32% | ⚠ **DISQUALIFIED — intraday conflict**: live put sweep today ($671,810) and the **largest OI build today is a PUT (130P)**; stock −2.20%. |

**(b) Mega-cap / index hedge-flow (filtered — `cum_flow_30d` fails to confirm):** SPXW bearish 5/5 ($9.54B) and **SPX bullish 5/5 ($2.27B) — same underlying, opposite direction, same day**, which by itself proves these are vol-structuring trades, not a market call. Also SPY (bearish 5/5, MIXED −$1.39B), QQQ (bearish 5/5, MIXED −$237.8M), TSLA (bearish 5/5, MIXED −$445.7M — top build a 330P at 78% ΔOI/vol, the closest to genuine alignment), AAPL (bearish 5/5, MIXED −$262.7M — but top build is a 332.5C, undercutting the tag).

**(c) Persistent but mixed-direction (no thesis):** NVDA, MU, META, SNDK, AMD, IWM, INTC (all 5/5), AMZN (4/5).

**(d) Short persistence (<3/5), watch-only:** AVGO, TSM, SMH (2/5); IBM, ARM, PLTR, HOOD, SKHY, SOXL, MRVL (1/5).

---

## 4. LEAP Builds (6–24 months)

### **EMPTY — zero candidates cleared the 6-of-9 gate.**

The LEAP share of today's tape was **4.8%** — the thinnest bucket by a wide margin, which lowered the prior before the screen even ran. `uw oi biggest-increases --min-dte 180` returned mostly index/ETF products (QQQ, HYG, XLE, GLD, IEI, IEF, EWZ, EWY, EEM, ARKK, TLT — out of scope). Single-name survivors: WULF, SLS, RIG, GRAB, KEEL, ERII. The **C12 liquidity floor** dropped GRAB ($3.80, sub-$5), KEEL ($4.49, sub-$5), and ERII ($9.79M ADV). Three advanced to the full gate; **all three failed the required `cumulative-premium-flow` accretion gate:**

- **WULF** — 5 consecutive build days and a fresh +40,888-contract build in the 270115C00025000 (185 DTE), single print ask_vol 41,003 vs bid_vol 696. **But 90d net flow −$65.9M and 30d −$48.9M (both MIXED/negative)** — textbook wrong-direction disqualifier, no accretion signature. Conviction-matrix **MIXED at confidence 10** (vs the >70 DIRECTIONAL_LONG requirement). Aggregate call flow is actually **bid-heavy** (127,641 bid vs 124,104 ask), contradicting the single print. Stock **−24.36% over 30d** while this OI built, and **short float 30.54%** → consistent with the Muravyev-Pearson-Pollet financing pattern (buying calls as a stock substitute to dodge borrow costs), not conviction. **2-of-9 at best.**
- **SLS** — 8 consecutive build days, but 90d **−$21.4M** / 30d **+$6.6M** (sign flips between windows, no accretion). Internally contradictory: the $30-strike 185-DTE call build (+30,356) is **bid-dominant** (301 ask vs 25,304 bid — *selling* into the bid) while the $15-strike build (+11,584) is ask-dominant. Two adjacent strikes on one expiry with opposite trade-side character = offsetting/hedged positioning, not a directional thesis. Short float 34.45%.
- **RIG** — only **3** consecutive build days (<5 required). 90d **+$2.8M** (flat) / 30d **−$1.8M, BEARISH** — wrong direction. The build is at the $5.50 strike vs $5.30 spot (essentially ATM, not conviction strike selection). Short float 21.99%.

All three carry short float ≥22%, which raises the prior that long-dated options activity reflects **borrow-cost financing mechanics** rather than conviction. The macro backdrop (10Y 4.62% rising, USD strengthening) is a standing headwind for long-duration equity risk, but was not needed to reject any of these — they failed on flow mechanics alone.

---

## 5. Volatility Surface

### The OPEX-kink artifact is total — the KINKED gate is unreachable today

This is the most important vol finding of the run, and two agents found it independently:
- **earnings-scout: 0 of 13 tickers** ever return `structure=KINKED`. Every name (banks, TSM, NFLX, IBM, ISRG, SCHW, NXPI, CTAS) reads `BACKWARDATION, kink_expiry: null`, and the front leg in **every** curve is the **2026-07-17 monthly OPEX expiry** (dte≈3), carrying **17K–78K contracts vs 500–7K one tenor out**.
- **vol-surface-scout: 18 of 19** non-mega-index names classify raw BACKWARDATION with `kink_expiry: null`; for **every single name** the 07-17 leg carries the highest or near-highest avg_iv on the whole curve.

**This reconfirms the 2026-06-12 audit finding and extends it: the artifact generalizes beyond pre-FOMC windows to ANY OPEX-proximate week.**

**The mitigation both agents built independently is worth institutionalizing.** earnings-scout established a **pure-OPEX control band** from the five money-center banks (confirmed already-reported this morning → no forward event, so their front-end elevation is *purely* mechanical): **front/far ratio 1.38–1.75, mean ≈1.60.** Any name inside that band **cannot be distinguished from mechanical OPEX noise**. Applied: TSM 1.589, IBM 1.397, SCHW 1.463, MS 1.721, NXPI 1.235 all sit **inside** → no event excess. Only NFLX (2.393), ISRG (2.256), GEV (2.093), CTAS (1.973) exceed it.

**The naive `front-end-iv-ratio` is actively misleading in *both* directions** — it manufactures fake panic on OPEX-front names, *and* it **masks real kinks**: it reads **1.035 FLAT on MSFT** and **0.885 CONTANGO on FTNT** while both curves clearly hump at the earnings-adjacent expiry. **The full thick-tenor curve must be read; the single ratio cannot be trusted alone.**

### IV rank ≠ rich vol — the trap the funnel set today

Step 0's IV-rank-100 list (MSFT, CTSH, NBIS, SNDK, BSX, ISRG, CPNG, UMC, DDOG, FTNT) looks like a premium-selling shopping list. It is not. **IV rank is a percentile of IV against its own history — it says nothing about IV vs realised.** QQQ makes the point cleanly: its `iv-percentile` is **50.0** (dead centre of its own range) while realised vol runs **~6.5 points above implied**. A name can carry an unremarkable percentile and still be cheap. The corollary holds in reverse: **every** IV-rank-100 name above has a confirmed or plausible near-term catalyst that legitimately justifies elevated IV, and earnings-scout confirmed **none is inside a 14-day actionable window** (MSFT/BSX/UMC/FTNT/CTSH 07-29; CPNG 08-04; SNDK 08-05; NBIS/DDOG 08-06).

**⚠ Substrate caveat on every percentile below:** `iv-percentile-zscore` returned `dates_used: 64` against `lookback_days: 252` — **25% of the requested window**, well under the agent's 120-day first-class floor. **All percentiles/z-scores today are PROVISIONAL.**

### Genuine, earnings-anchored kinks (survived the artifact screen)

| Ticker | Earnings | Real kink evidence | Front-end ratio | iv-pctile/z (prov., n=64) | VRP-aligned? |
|---|---|---|---|---|---|
| **MSFT** | 07-29 pm (15d) | dte=17 (07-31) **53.0% vs 35.8%** at dte=13 | 1.035 — **FLAT, masks the hump** | 100 / 2.26 | **YES** — BUY VOL, implied move **2.44%** |
| **FTNT** | 07-29 pm (15d) | dte=17 **92.9% vs 57.0%/81.5%** neighbours | 0.885 — **CONTANGO, masks the hump** | 95.3 / 2.23 | YES — BUY VOL, 3.41% |
| **INTC** | 07-23 pm (9d) | dte=10 **119.9%**, right after earnings | 1.165 | 90.6 / 1.24 | YES — BUY VOL, 6.04% |
| **BSX** | 07-29 am (15d) | dte=17/24 **60.6%/58.0% vs 50.1%** at dte=10 | 1.0 — **FLAT, misleading** | 100 / 2.15 | **NO** — healthcare, no VRP anchor |
| **CPNG** | 08-04 (21d) | genuine build dte=17→24 (57.6%→69.9%) | 1.347 | 100 / 3.16 | YES — BUY VOL, 4.07% |
| **BMY** | 07-30 am (16d) | modest bump dte=17 (36.7% vs 30.8%) | 1.249 | 100 / 4.66 | **NO** — healthcare |
| **FTAI** | 07-29 pm (15d) | dte=17 **102.5%** (thin, n=43) | 1.054 borderline | 85.9 / 1.60 | **NO** — industrials |
| **TSM** | **07-16 am (2d)** | earnings falls **inside** the 07-17 OPEX contract — front IS the earnings leg | 1.589 — **inside the OPEX band** | 79.7 / 1.14 | ratio shows **no event excess** |

### OPEX artifacts — do not trade
- **ISRG** — front dte=3 spike (**107.8%**) declines monotonically after (66.3%→56.2%→51.5%) with **no secondary hump**. Mostly OPEX artifact despite a real 07-28 earnings date 14 days out.
- **GEV** — front dte=3 (**139.5%**) largely OPEX, though real put-heavy premium ($3.8M/$4.1M) at dte=24/17 straddles the 07-22 earnings.
- The mechanical front-leg elevation present on **literally every name** at dte=3.

### Structurally elevated, not event-anchored
- **NBIS** — curve broadly elevated **142–160% across nearly every tenor**, no discrete kink, no confirmed earnings date. **Open question flagged:** `expiry-heatmap` shows heavily **put-skewed** premium ($82M @ 07-24, $35M @ 07-31) dwarfing pure-OPEX noise — a possible unconfirmed catalyst (ADR/foreign-filer lag), and it **directly contradicts** sweep-tracker's bullish read.
- **SNDK** — same flat-high profile, no discrete kink, no unusual premium concentration.

### Post-move catch-up, not a forward kink
- **SKHY** (+27.29%) — front IV 154.9% is **realised-vol catch-up from an already-completed move**. `iv-percentile` **unavailable** (only 1 IV30d reading, <5 required) — no data to grade richness.
- **IBM** — genuinely mixed: today's −25.21% crash + a pending 07-22 print. Vol is **broadly elevated (crash shock), not kinked at the earnings tenor**; front-end 1.397 is inside the OPEX band. **earnings-scout confirms the crash is NOT earnings-related** — the print is 8 days away. Re-check 3–4 days before 07-22 once crash-vol decays.

### Calendars / BACKWARDATION with no catalyst: **EMPTY**
Every single-name BACKWARDATION either has a pending earnings catalyst inside the window (disqualified — do not fade an unresolved event) or is NBIS/SNDK, which lack a confirmed catalyst but show front-end ratios still above 1.05 with **no historical time series to confirm the ratio is actually *falling***. A single snapshot cannot certify "panic resolving."

### IV outliers: non-productive
`iv-outliers --min-iv 1.5 --top-n 30` returned exclusively sub-$10 penny-biotech/microcap lottery contracts (EOSE, RGNX, SPCE, SPRO, IMNM, BIOX, DSGN, LCDL, SBET — several with avg_iv **1000%+**) plus routine SPY/QQQ 0DTE wing noise. **All fail the liquidity floor.**

### Contrarian fade book — ABORTED on the VRP gate

The contrarian-scanner **aborted its entire book**, correctly and on its own charter. Its disqualifier reads *"Negative VRP (rich vol is justified)"* with **no structure-type qualifier**, and its flag condition is *"VRP is positive."* Both indices are negative (SPY −0.0172, QQQ −0.0655). The agent **explicitly considered and rejected** a debit-structure carve-out as an unauthorised self-reinterpretation of its own gate. That is exactly right.

Two independent readings reinforce the abort:
1. **No index-level fear extreme exists** — SPY pc-z **−1.20 (NORMAL)**, QQQ pc-z **−0.40 (NORMAL)**, nowhere near ±2σ. The only venue the charter permits fades on presents no candidate.
2. **No bullish crowding exists anywhere** — NVDA z **−0.71**, MU **+0.51**, AMZN **−0.57**, SNDK **−1.15**; all NORMAL, several *below* zero (more put-skewed than their own norm).

**Therefore the −2 informed-flow-continuation line cannot fire on any name today**: its own "VRP positive" precondition is unmet; there is no overcrowded long to attach it to; and `pc-ratio-zscore` has **no `--date` flag**, so "rising" is unverifiable from a single snapshot regardless.

The only extremes found are all **BEARISH_EXTREME** and all correctly declined as fades: **IBM z=2.50** (post-crash protective put bid vs a 20d mean of 0.34 — the canonical "real hedge bid, don't fade it"), **FTAI z=9.01** (aligned institutional flow on a 6-factor bearish name — per Pan-Poteshman / Ge-Lin-Pearson, single-name put crowding predicts **continuation**; the crowd is more likely right), **GLD z=4.56** (structural macro insurance amid rising yields and a strengthening USD).

---

## 6. Risk & Correlation

**Macro headline:** Curve normal (+0.40) · core CPI 2.81% / core PCE **3.41%** YoY · unemployment 4.2% · payrolls +57k · **10Y 4.62%, rising** · **USD strengthening** · fed funds 3.62%. A hawkish-tilt backdrop for long-duration risk.

**Forward event risk:** **PPI 07-15 08:30 ET (HIGH, tomorrow)** · claims 07-16 · **OPEX 07-17 (HIGH, mechanical)** · claims 07-23 · **FOMC 07-28/29 (HIGH)** · **PCE 07-31 (HIGH)** · CPI 08-12. Every Tier-1 print through PCE sits inside a 1–4wk swing horizon opened today. Had anything sized, **PPI at T+1 and OPEX at T+3 would each have fired a −1 tier** on any non-event-play swing.

**Breadth cross-check (`fz breadth`, advisory — does not change sizing):** advancers **203** / decliners **297** / unchanged 3 · **`pct_green` 40.36** · avg change −0.38% · median **−0.42%** · top mover CRWD +12.14% · worst mover IBM −25.21%. **`divergence_flag: true`** — the index and mega-cap tech are green while the majority of the S&P declines. **This is a distribution tell**, from a data lineage independent of `uw risk market-regime`, and it is consistent with the day's other findings: software/mega-cap DP distribution (IGV), a Technology sector-tool outflow, and an accumulation screen that produced nothing.

**Correlation — today's 6 candidates were really ~2 bets:**

| Cluster | Members | Pairwise corr (30d) |
|---|---|---|
| **semis/memory (hard, ≥0.70)** | SNDK, TSM (+ watch: MU, INTC) | SNDK/MU **0.858** · TSM/INTC **0.778** · MU/INTC **0.777** · SNDK/INTC **0.759** · TSM/MU 0.672 |
| soft watch pairs (0.60–0.70, no penalty) | TSM hub | TSM/NVDA 0.692 · TSM/NBIS 0.680 · TSM/TSLA 0.678 · MSFT/AMZN 0.677 · TSLA/INTC 0.624 |

**4 of 6 candidates were semis/tech-adjacent** (TSM, SNDK, NBIS, MSFT). Had anything sized, SNDK-long and MU-long would have been one bet, and TSM-short would have been partially self-hedged against the SNDK long. **TSM is the correlation hub**, soft-linked to NVDA, NBIS, TSLA and MU. Recorded for the desk; no tier action — everything is `skip`.
> *Tool caveat:* `portfolio-correlation` returned `sector: "Unknown"` for all 11 symbols — the sector-metadata lane is broken. The pairwise matrix itself is intact. (Also: the flag is `--symbols`, not `--tickers`.)

**Fundamentals verdicts:** **none — stage 2b was skipped.** With every name at `skip`, the fundamentals gate can only cut size that does not exist. Same for the 2c bull/bear debate. This follows the 2026-07-13 precedent for an all-DROP board.

**Watchlist — the feedback loop is fully cold.** `uw watchlist alerts` and `uw watchlist scan` both return **empty**: there is no `conviction_2026-07-13` group, and **no older non-empty `conviction_<date>` group exists at all**. The state file has fully drained — the direct consequence of a 10-run empty-book streak. **There are no carried positions to monitor and therefore zero adverse-flow exit candidates.** That absence *is* the finding. The first non-empty book will restart the loop from scratch, and its Day-1 alerts read will be baseline-free.

**Hedge sleeve.** No new exposure — the book is empty, there is no fresh delta to hedge. For **legacy** long tech/semis beta: **QQQ VRP is PREMIUM_BUYING (IV 23.7 vs realised 30.3), which makes long protection unusually well-priced — do not sell premium to finance the hedge.** Preferred expression is a QQQ put vertical or put ladder, opened **before PPI at 08:30 ET tomorrow** and sized to survive the OPEX 07-17 unwind and FOMC 07-28/29. The distribution tell (green index / 40.4% breadth, Technology sector-tool outflow, 10Y rising, USD strengthening) argues for holding the hedge through PCE 07-31 rather than day-trading it. **Do not hedge via short single-name semis** — the short book has shown no selection alpha in any decided regime (−22.9pp blended, 2026-07-04 audit).

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

### **EMPTY — zero names at HIGH or MEDIUM. Zero at LOW. All six DROP.**

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no per-tier expectancy row is computable this run — there are no calls in any tier, and the rolling `conviction_<date>` watchlist is empty across all 10 runs of the current streak, so `scripts/kelly_sizing.py` has no closed calls to draw on. The most recent audit reference point (2026-07-04) stands: **DROP pile 0.477 vs traded book 0.406** — the board the system declines to trade has been outperforming the board it trades, which is the empirical case for today's output.

### Full scored board (all DROP — shown because the *reasoning* is the product today)

| Ticker | Dir | Raw | Σ components | Class | cum_flow_30d | WR (clean, market-wide) | Excess | Size |
|---|---|---|---|---|---|---|---|---|
| **MSFT** | short | **2** | +1 cum-flow accretion · +1 vol-surface genuine kink | bearish_flow | −$859.8M (**BEARISH label**) | 0.5299 (n=134) | **+0.1866** | skip |
| **TSM** | short | **2** | +1 mechanized DEX flip · +1 multi-day OI build | bearish_flow | −$301.7M (MIXED) | 0.5299 (n=134) | +0.1866 | skip |
| **SNDK** | long | **1** | +1 sector-rotation semis leader | sector_rotation | +$988.2M (MIXED) | null / NA(substrate) | null | skip |
| **TSLA** | short | **1** | **+2 multileg directional** · **−1 flow_conflict_lite** | multileg_directional | −$445.7M (MIXED) | null / NA(substrate) | null | skip |
| **NBIS** | long | **−1** | −1 flow_conflict_lite | bullish_flow | +$47.1M (MIXED) | 0.4929 (n=140) | **−0.1357** | skip |
| **FTAI** | short | **−1** | −1 flow_conflict_lite | bearish_flow | +$1.2M (MIXED) | 0.5299 (n=134) | +0.1866 | skip |

**Union-median |cum_flow_30d| = $373.70M** (the magnitude threshold for the mechanical flow_conflict test). 25%-of-median = $93.42M.

**Signal-backtest, clean protocol (P0.3) — the headline was never quoted:**

| Class | Kept n | Clamped rows dropped | Clean WR | SPY same-direction bench | Excess |
|---|---|---|---|---|---|
| `bearish_flow` | 134 | 10 (07-08/09/10) | **0.5299** | 0.3433 | **+0.1866** |
| `bullish_flow` | 140 | 14 (+1 price-floor) | **0.4929** | 0.6286 | **−0.1357** |

The tool's raw headlines were **53.5%** (bearish) and **49.0%** (bullish) with 10 and 14 truncated rows **silently included** — the reason the headline field is quarantined. Both figures are **market-wide class rates, not ticker-specific** (the tool has no `--symbol`). `multileg_directional` and `sector_rotation` are **not supported signal types** → `NA(substrate)` for TSLA/SNDK. Per-row ADV could not be verified for the market-wide kept rows (rows carry price only); the price ≥ $5 floor was applied and the ADV limitation is recorded here per C12 fail-closed honesty.

> **Do not read the `bearish_flow` +18.66pp class excess as short alpha.** It is a market-wide class statistic measured over falling June windows. The book-level finding is unchanged: **short selection alpha −22.9pp** (2026-07-04 audit). None of these shorts is sized anyway.

### Why the board is empty — the four adjudications that decided it

**1. TSM (raw 2) — the closest call on the board, and worth the desk's attention.**
The most-corroborated thesis of the run: five agents, the fleet's **only** verified mechanized DEX flip (fully dated: 7/10 +733.3M → 7/13 −248.7M, prior 3 sessions positive, |flip| 1.29× the 0.25×median floor, confirmed 7/14 at −451.6M), today's **#1 bearish net-premium name (−$88.8M)**, DP distribution, and a 4-leg bear call spread. It scored 2 because every other line was declined:
- **multileg's +2 was declined by multileg itself** — four reasons: it's a **ROLL** not a fresh build (Aug legs vol/OI < 1 = closing), `repeat_count=1`, **net short vega into PREMIUM_BUYING VRP**, and the play type does not follow *from* the term structure (the structure deliberately sits **past** the only real feature — the 07-16 earnings kink — in the flat region; direction comes from DEX/flow). The agent reads it as a **covered-call overwrite rolled down-and-out**, not a standalone bet.
- **vol-surface's +1 was declined by the artifact screen** — front-end 1.589 sits **inside the pure-OPEX control band (1.38–1.75)**, and earnings-scout's verdict is *"zero vol mispricing."* The BACKWARDATION label is mechanical OPEX elevation, not a dislocation.
- **earnings-scout returned SKIP → 0.**
- **The cum-flow +1 was declined — and this single call decided the tier.** 30d net is −$301.7M: sign-aligned, ≥$50M, 0.81× union median. **But the tool's own `trend_direction` is MIXED** (bearish 52.4% / bullish 47.6% of a $6.29B gross — a 4.8% imbalance, below the tool's directional threshold). "Net directional accretion" requires a directional read. No deduction either — the mechanical lite branch is clean (aligned sign, mid-quartile, above 25%-median, no OPPOSITE label).
- **Counterfactual, stated plainly: had that +1 been awarded on a strict sign+magnitude reading, TSM = raw 3 → LOW / starter.** The quant flagged this as a **rubric ambiguity worth registering** — *"net directional accretion" has no frozen operationalization of near-zero-vs-gross, and today it decided a tier.*

**2. TSLA (raw 1) — the fleet's only qualifying +2, starved by the absence of corroboration.**
The multileg evidence is genuinely strong and fully audited: Sep-18 **400P/300P debit put spread**, 13,010 × 100-wide, fresh build (vol/OI **1.77** and 1.10, ask% 82.3, 87% classified BOUGHT), ~85% of Sep-18 put volume, ≈**−481k delta (~$190M short-equivalent)**, **long vega** (regime-correct vs PREMIUM_BUYING). Term-structure-anchored: placed in the thick-tenor **trough** (09-18, 50.1%) deliberately **past** the real 07-31 event kink (71.6%, n=5,906), after the agent correctly **overrode** the tool's thin-LEAP `KINKED@2027-12-17` artifact (n=298 at 521 DTE). Debit $28.03 → **$36.5M outlay**, breakeven **371.97 (−6.1%)**, max profit ~$93.6M, risk capped at the debit.
It still scored 1, because **nothing corroborates it**: dealer-positioning FLAT (the 7/13 dip is a bracketed 1-day whipsaw), opex-pin **disqualified** (bottom-tercile pin score, diffuse wall), sweeps 0 by rubric and MIXED-filtered anyway, OI-build 0 (mixed composition: 330P vs 3× 420C). Then **−1 flow_conflict_lite**: cum_flow_30d −$445.7M is **MIXED — a 49.5%/50.5% split, a 1.04% imbalance on $42.98B gross**, the textbook near-zero case. `repeat_count=1`, and the legs straddle **FOMC 07-28/29 + PCE 07-31**. The agent's own words: *"do NOT treat the multileg line alone as HIGH-conviction."* **This is precisely the single-signal thesis the additive rubric is designed to starve.**

**3. MSFT (raw 2) — direction conflict, resolved SHORT.**
Sweep-tracker's thesis is directionally short (bearish 4/5, the only mega-cap clearing the hedge-flow filter) but **sweeps earn 0 points**; vol-surface's is long-vol / direction-neutral. Resolved **SHORT / `bearish_flow`**: the −$859.8M 30d flow is the **union's only tool-labeled directional read (BEARISH)**, and the vol lane is the documented negative-edge lane with earnings (07-29) outside the 14-day window. Under SHORT the −$859.8M earns **+1 accretion** (it would have been a **−3 flow_conflict** under a LONG resolution). The **OI-build +1 was declined**: 10 consecutive build days, but the composition is **all calls — against the trade direction**. ⚠ The award's weakness is on the record: the largest builds are calls (397.5C/400C/395C) = **covered-call supply into OPEX**, which prints as bearish premium without any put-bid conviction. The C4 opening gate would have capped it at half regardless (put-side opening not OI-confirmed).

**4. FTAI (raw −1) — why the top-scoring screen name scores below zero.**
FTAI was Step 0's **highest bearish confluence score (6)** — bearish_flow, high_pcr, volume_spike, dp_distribution, oi_building_puts, high_iv_sell_premium. On the real rubric it scores **−1**, and the reason is the single most useful lesson of the run: **six correlated single-day screen factors are not six signals.** Both flagging agents explicitly declined to score it (vol-surface: no valid VRP anchor — Industrials, SPY's FAIR VRP too diluted to license a claim on an unrelated-sector idiosyncratic name; contrarian: the pc-z 9.01 is *aligned* informed flow predicting continuation, not a fade, and the −2 line is LONG-only with an unmet precondition). The `oi_building_puts` factor **does not survive the 10-day OI trend** — adds are trivial (533–2,364 contracts/day) and **call-dominant** (the 08-21 220C is the largest add). Its entire 30d options tape is **$67.1M gross — roughly 0.1% of MSFT's** — and the 30d net leans marginally **bullish against the short**, firing `flow_conflict_lite`. **The funnel score is a seed, not a conviction score.**

**Σ-invariant verification:** MSFT 1+1=2 ✓ · TSM 1+1=2 ✓ · SNDK 1=1 ✓ · TSLA 2−1=1 ✓ · NBIS −1=−1 ✓ · FTAI −1=−1 ✓. Load-bearing-tool gate: no-op (no raw ≥ 9). Every quoted win_rate passed the pre-emit assertions (≤0.80 ceiling, sizing-eligible source, no degenerate 0.0, sub-0.50 ⇒ starter/skip).

**Quant departures from Phase 1 agents' own recommendations (logged):**
1. **TSM / SNDK / NBIS vol-surface +1 all declined** despite sitting in the scout's "scored-eligible BUY VOL" cluster — for SNDK/NBIS the scout's **own §5 disclaims a genuine dislocation** ("structurally elevated, not event-anchored"); for TSM the earnings-scout control-band test overrides. **Only MSFT's kink survived.**
2. **TSM cum-flow +1 declined on the MIXED label** despite aligned sign and $301.7M ≥ $50M — the tier-deciding call, flagged for `/calibration-audit`.
3. **SNDK sector +1 awarded on sign-agreement per the gate's own text**, even though the same flow fails the accretion-line standard — the two gates are worded differently (sign agreement vs directional accretion) and each was applied as written rather than collapsed. Tension noted.
4. **MSFT resolved SHORT / `bearish_flow`** over vol-surface's direction-neutral framing.
5. **TSM dominant class assigned `bearish_flow`** on a 1/1 component tie (no rubric class exists for a dealer-positioning flip) — noted rather than silently mapped.

### Deep-dive hand-off
**Skipped** — no HIGH-tier names. Per Step 8.5, deep dives are skipped entirely on a no-edge day.

---

### Conviction-scoring rubric (verbatim, version `2026-06-12` — FROZEN)

```
Daily conviction score = Σ:
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna-squeeze setup in trade direction — the trigger must be a
      verified SIGN CHANGE, not a level: sign(net_dex) on the latest session opposite to ≥3 consecutive prior sessions, read from
      dated `uw options-structure dex --date` calls (≥4 to verify the prior-session sign run; ~11 for the trailing-median floor),
      with |net_dex| on the flip day ≥ 0.25× the trailing-10-session median |net_dex|; the evidence string must cite both dated
      values. Vanna disjunct additionally requires a dated VIX source for the falling-VIX leg — no out-of-band VIX fills.
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified institutional-tier confirmed)
      — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms (sign aligned AND |cum_flow_30d| ≥ $50M);
        else halved (floored) +3→+1. A sub-$50M flow that halves this line does not separately qualify as "net directional
        accretion" for the +1 cum_flow line.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL ONLY: award only when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +1  uw historical cumulative-premium-flow shows net directional accretion in trade direction (30d) — INTENT-SCREENED: award only
      when (a) no C28 distribution_flag on the name, AND (b) on dividend payers inside an ex-div window, the accreting prints are
      NOT deep-ITM sub-parity calls. Screen failed or unevaluated on a flagged name → 0.
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector — CONDITIONAL: award only when
      (a) sector persistence_score ≥ 0.6 AND (b) cum_premium_flow_30d direction aligned with thesis AND (c) |cum_flow_30d| ≥ $50M.
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising uw historical pc-ratio-zscore (VRP positive) — an INFORMED-FLOW
      CONTINUATION penalty, not a "crowd is wrong, fade it" signal. Single-name P/C extremes predict continuation, not reversal
      (Pan-Poteshman 2006; Ge-Lin-Pearson 2016).
  -3  flow_conflict — cum_premium_flow 30d direction clearly OPPOSITE dominant_signal_class (signed-sum sign flip + magnitude >
      today's union-median |cum_flow_30d|, or explicit OPPOSITE label). Mutually exclusive with flow_conflict_lite.
  -1  flow_conflict_lite — the 30d cum_premium_flow read is MIXED (signed sum near zero, or aligned but bottom-quartile magnitude
      in today's union). Mutually exclusive with flow_conflict.
  # NOT score_components — risk-monitor TIER gates applied in Step 2d (contribute 0 to raw_score):
  -1  [TIER GATE] risk-monitor flags in correlation cluster (pairwise corr ≥ 0.70) — −1 TIER
  -3  [TIER GATE] uw risk market-regime conflicts with trade direction — −1 TIER
  # REMOVED: uw insights signal-confluence ≥4 (+2, removed 2026-06-12 P0.2); uw hot-chains sweep-persistence top-5 (+1, removed
  #   2026-05-23 P0.3, −22pp marginal contribution); gamma-flip-tracker 0DTE breakout (+2, removed 2026-05-09).
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | **HIGH** | full size (subject to the 3-of-4 load-bearing-tool gate + win-rate gate) |
| 7–8 | **MEDIUM** | half size (subject to win-rate gate) |
| 3–6 | **LOW** | starter / watch-only |
| ≤ 2 | **drop** | filtered by the quant's drop floor |

**Tier-cut status:** the ≥9 HIGH cut **failed its scheduled re-confirmation on 2026-06-12** (bands inverted on the first post-UPTREND window: HIGH 0.222 / MED 0.214 / LOW 0.444). The cuts are retained under the P0.1 freeze but **carry no validated ranking claim**; the P0.6 out-of-regime guard caps all sizing at half in the interim.

---

## 8. Watch-only — single signal, no confluence

Flagged by exactly **one** Phase 1 agent → failed the ≥2-agent confluence gate, excluded from the rubric. **For journaling, not entry.**

| Ticker | Sole flag | Why it did not clear |
|---|---|---|
| **MU** | sector-rotation +1 (cum_flow_30d **+$282.0M** aligned, persistence 1.0) | sweep 5/5 but **MIXED direction** → no thesis. Accumulation: mega buy_ratio **0.043**, NEUTRAL. No DEX flip. **The strongest single-agent name on the board** — re-check if a second agent confirms. |
| **NVDA** | opex-pin +1 (pin 215, dist 1.51%, `gex_at_pin` **+$96.19M** discrete peak, OI 96,507, expiry 07-17 **verified**) | **sector-rotation explicitly disqualifies it: cum_flow_30d −$2.1M (MIXED)** — not aligned, despite topping today's bullish net-premium board (+$56.3M). **multileg excluded it as a hedge/collar**: the structure flips direction day-to-day (~60k **call** line 07-13 → ~60k **put** spread 07-14 at matched size) = a collar program around a long book. Sweep 5/5 MIXED. |
| **AMZN** | opex-pin +1 (pin 250, dist 1.00%, `gex_at_pin` **+$51.06M**, OI 43,723, expiry 07-17 verified) | **accumulation-hunter caught a concrete false positive**: `institutional-accumulation AMZN` returns ACCUMULATION (buy_sell_ratio 2.76) driven **100%** by the $247.49 / 88-trade / **$568.5M** level — **every trade inside the 20:00–21:25Z closing-cross window.** |
| **BAC** | accumulation-hunter +3 **halved to +1** | Conjunction fails: cum_flow_30d **+$32.0M — right sign, below the $50M gate.** Block-tier buy_ratio only **0.546**; smart_positioning MIXED; largest OI adds are in the **07-17 series = OPEX roll mechanics**. Weak `distribution_flag` present (270115C65 LEAP call OI −480 ≈ $114K closing). Block/float ratio **0.0000253** = negligible. **earnings-scout: BAC already reported 07-14 premarket** → the bullish flag is **post-print PEAD-reaction flow, not accumulation**. |
| **INTC** | vol-surface +1 (real 07-23 earnings kink at dte=10, 119.9%) | **multileg proved INTC's bearish net premium is manufactured by an artifact** — see the artifact register below. No DEX corroboration. Sweep 5/5 MIXED. |
| FTNT | vol-surface +1 (real 07-29 kink, dte=17 92.9%) | Earnings 15d out, outside the actionable window. |
| CTSH, UMC | vol-surface | **Chain too sparse to certify a kink** — CTSH has 8 expiries with a gap from dte=3 → dte=38; UMC's dte=3 127.3% is plausibly OPEX + TSM-sympathy + own earnings, indistinguishable. |
| CPNG, DDOG | vol-surface | CPNG earnings 21d out. DDOG: `implied_move` null, **earnings date unconfirmed**. |
| BSX, ISRG, BMY, GEV | vol-surface (real kinks) | **Not scored-eligible — no valid VRP anchor** (healthcare/industrials/utilities). **ISRG's front spike is mostly OPEX artifact.** GEV: no DEX corroboration despite its bearish screen score. |
| **IBM** | (dealer-positioning **disqualified** it; contrarian declined to fade) | **Artifact-dominated — do not trade.** DEX flip technically met but **disqualified as a same-day mechanical consequence of the −25.21% crash**. ZGL series unstable (115/279/125/133/279/…). contrarian z=2.50 = post-crash **protective put bid** (20d mean 0.34) — "real hedge bid, don't fade." **earnings-scout confirms the crash is NOT earnings-related — next print 07-22.** Front-end 1.397 **inside the OPEX band** → no event excess. The Step-0 Tier-1 **290P floor block remains an unresolved artifact.** |
| ORCL | sweep (bearish 4/5) | **Parity-arb caveat** — the Tier-1 **200P floor block** (delta −0.955, 3 DTE) is an unresolved deep-ITM mechanical print; `sweep-ratio` shows an ORCL 250C at **$0.01** = lotto noise. Persistence likely contaminated by mechanics. |
| SPCX | sweep (bullish 4/5) | **Disqualified — intraday direction conflict** (live put sweep + largest OI build is a **put**; stock −2.20%). |
| DAL | accumulation-hunter | **Disqualified on sign misalignment** — cum_flow_30d **−$3.2M MIXED** vs a DP-buy thesis; OI build dominated by far-OTM weekly **put selling** (strike 75 vs spot 85.53). |
| WULF, SLS, RIG | leap-radar | All rejected — see §4. |
| SKHY | vol-surface (declined) | +27.29% today; front IV is **realised-vol catch-up from a completed move**. `iv-percentile` **unavailable** (1 reading, <5 required). |

---

## Appendix — Artifact register (for `/calibration-audit`)

Today's defining feature is that **the tape's headline signals are substantially mechanical.** Recording the evidence.

### A. The dark-pool tape is pervasively closing-cross contaminated — worse than the documented 07-02 lesson
Every name at/near the top of `block-stratified` — **MU, NVDA, META, AAPL, AVGO, SNDK, AMZN, TSLA, MSFT, IBM, CSCO, LRCX, JPM, AXP, CVS, WFC, GOOGL, TSM, C, XOM** — shows mega/large-tier prints as dozens of trades at **one identical repeated reference price**, clustered **20:00Z through 21:56Z** (a wider window than the 20:00–20:25Z previously documented). Examples: AMZN 10 prints all at 247.49 (20:00:00–21:24:48); TSLA all at 396.18. **This is a market-wide MOC/benchmark-cross artifact, not stealth accumulation.** Concrete false positive: `institutional-accumulation AMZN` = ACCUMULATION driven **100%** by trades inside the cross window. **Appears persistent, not one-off — escalating.**

### B. ~85% of the multileg tape is financing / rolls / crosses
- **SPX/SPXW box + collar financing** (confirmed independently by sweep-tracker **and** multileg): `SPX 7000C bid 5400` + `8000P bid 5400` **both at 17:54:38Z**; 7000C ask 3000 Sep + 8000C bid 3000 Dec-27 same timestamp; 1200/1000 clusters at 19:49:14Z / 19:52:06Z / 19:54:43-44Z across 2029-12-21 and 2030-12-20. Deep-ITM/OTM 4-leg at 7000/8000 strikes on a **7548** index with matched sizes = **synthetic lending, zero directional read**. **This is why SPX prints bullish (+$320.5M) and SPXW prints bearish on the same underlying simultaneously.** SPX alone = **$4,514M** of the multileg premium.
- **INTC 07-17 80C/81C financing ladder — the best catch of the day.** A $1-wide deep-ITM call spread (spot 107.76) at 3 DTE priced **28.35 − 27.17 = $1.18 on a spread that can be worth at most $1.00** — arithmetically impossible, confirming crossed/stale marks. IVs of **205.8% / 179.2%** on deep-ITM 3-DTE calls confirm it. **Recurs every session** (07-09, 07-10, 07-13, 07-14): `repeat_count = 4` **on an artifact** — a naive repeat-counter would score this as top-conviction. It **manufactures much of INTC's −$36.8M "bearish" net premium.**
- **WULF Dec-18 30C/38C/16P seagull UNWIND** — repeat_count 2 with identical ~15,00x sizes, but **all three legs vol/OI ≤ 1** (0.51/0.91/0.99) and the 38C is ask%=100 **buying to close** a short. The 07-09 structure is being **closed, not rebuilt** — a second naive-repeat trap.
- **NBIS 170P Jul-17 → Jul-24 OPEX calendar roll** (Jul-17 vol/OI 0.60 closing → Jul-24 vol/OI 1.50 opening).
- **DRAM** — side classification **0–2%** (`280121P43` 0% classified, OI 58 vs vol 8,204); strikes/expiries differ every day = churn. **CC 260807 17C/21.5C** — vol 25,061 against **OI = 0 on both legs**. **EQPT 270115 15C/45C** — vol 18,983 vs OI 179, ~99% unclassified. **INFY 260821 13C/13P** — same strike + expiry, call **and** put, matched 15,014/15,026, ~0.2% classified = **synthetic long / conversion = financing, non-directional by construction.**
- **Step-0 Tier-1 "FLOOR_PUT_BLOCK" singles (IBM 290P $13.86M, ORCL 200P $7.70M)** — both **deep-ITM** (delta −0.98 / −0.955, strikes far above spot), 3 DTE. Stock-substitute / parity mechanics, **not directional conviction** — the documented ORCL parity-arb class. IBM's is further compromised: a 3-DTE deep-ITM put block on a name that **already crashed −25.21%** is hedging/assignment mechanics. **Unresolved; C19 advisory, 0 points regardless.**

### C. Tool caveats logged this run
1. **`uw hot-chains multileg --top-n` defaults to 20 and returned ZERO single names today** — the entire single-name multileg tape sits below the default cutoff; `--top-n 200` was required. **A default-20 run would have produced a false "nothing here."**
2. **`uw oi pin-risk` `dte_to_opex` is unreliable** — reports **0** for SPY/QQQ/IWM and **1** for NVDA/AMZN/TSLA on 07-14 when monthly OPEX is **07-17**; it keys on the nearest daily/weekly expiry. opex-pin **independently verified** true attribution via `uw oi term-structure`: NVDA 1.77M OI @ 07-17 vs 184K @ 07-15 (**9.6×**); AMZN 655K vs 42K (**15.8×**); TSLA 791K vs 121K (**6.5×**) — the pins ARE genuinely 07-17-anchored despite the mislabel. Also: SPY's nominal "pin" (720) sits **4.23% below** spot — a distant put shelf, not a pin.
3. **`uw oi opex-concentration` is non-productive** — top rows are 100%-concentration artifacts on illiquid micro-names with total OI 1–6k (RMAX, RBBN, HUBG, EMPD, SOPH, ANGI, CVU, OSUR, STTK, CALC), several with `pin_distance_pct: null` and even `spot: null`. Ranking by `concentration_pct` is meaningless.
4. **`uw screener volume-vs-average --min-volume-ratio 3` non-productive again (recurring)** — returned almost entirely illiquid micro-ETFs (XOMO 1447× on avg vol **2.5**; SPAB 407× on avg vol **1.97**; BABO, SCHE, AVLV). **All sub-floor, all dropped by C12.**
5. **`uw options-flow iv-outliers` non-productive** — all penny-biotech/microcap lottery contracts + 0DTE wing noise; all sub-floor.
6. **`uw insights analyst-vs-flow` returns only the options_flow half — no analyst-rating field** on every ticker tested (NFLX/TSM/IBM/MS). **Reconfirms the "analyst-vs-flow unwired" caveat logged 2026-07-13** — the tool cannot deliver its headline use case.
7. **`uw screener earnings-catalyst` omits major names** — NVDA, TSLA, MU, SNDK, NBIS, WULF absent, **and all five money-center banks** (JPM/GS/BAC/WFC/C) even at a 120-day / min-iv-rank-0 net. It is nonetheless the **working** earnings source (yahoo `get_earning_dates` fails: `Import lxml failed`).
8. **QQQ ZGL sub-320 grid artifact recurs** — 3 of the last 10 sessions (07-01: 314.06; 07-08: 300.24; 07-09: 300.29) against a ~710–725 spot. `gex-time-series` reported a QQQ "regime flip" on 07-10 with `zgl_delta 451.71` against spot ~725. **IWM is worse: 130.52/150.27/155.38/194.16/199.14 vs spot ~294–300 = unusable.**
9. **`iv-percentile-zscore` returns 64 of 252 requested dates** — 25% coverage, under the 120-day first-class floor. **All percentiles this run are PROVISIONAL.**
10. **Index/ETF DEX + ZGL whipsaw** — SPY/QQQ flip regime on **4+ of the last 10 sessions**; SPY DEX sign-flips on 4 of the last 5 transitions. Exactly the pattern the 2026-06-12 P0.4 demotion targeted.
11. **`uw risk portfolio-correlation` sector metadata broken** — returned `sector: "Unknown"` for all 11 large-cap symbols; the pairwise matrix is intact. Flag is `--symbols`, not `--tickers`.
12. **`uw historical pc-ratio-zscore` has no `--date` flag** — "rising z" is unverifiable from a single snapshot, which structurally blocks the −2 line's "rising" condition.
13. **`uw historical vrp` requires `--symbol`** — no market-wide mode.
14. **`uw screener iv-rank` uses `--mode high|low`**, not `--direction`.

### D. Rubric ambiguity worth registering
**"Net directional accretion" has no frozen operationalization of near-zero-vs-gross, and today it decided a tier** (TSM: aligned sign + $301.7M ≥ $50M but a MIXED tool label at a 4.8% imbalance → +1 declined → raw 2 DROP instead of raw 3 LOW). Relatedly, the **sector-leader gate** (worded "direction aligned") and the **accretion line** (worded "net directional accretion") were applied as written and reached **opposite conclusions on the same SNDK flow** — sign-agreement passed, accretion failed. The two gates need a common, frozen definition or an explicit statement that they are deliberately different tests.
