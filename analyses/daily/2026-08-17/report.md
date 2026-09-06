# Daily Market Analysis — 2026-08-17

## Executive Summary

- **Regime + GEX state:** TRANSITIONAL (trend UPTREND) — but the label describes about five stocks. SPY 772.67 (−0.47%) sits above both SMAs while equal-weight RSP fell −0.89% and only **26.2% of S&P names closed green** (median −0.95%). Both SPY and QQQ **flipped to fresh short-gamma today**: SPY FULLY_NEGATIVE (total_gex −$368M, ZGL unresolved), QQQ NEGATIVE (spot 730.13 vs ZGL 734.54, 0.6% from re-flipping). VIX 15.19, **+6.6% on a down-0.47% tape**. Sector lean: only XLE (+1.08%) and XLK (+0.16%) green; XLC −1.89%, XLP −1.64%, XLY −1.23%.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`. Non-binding today; nothing reached half.
- **Next-session GEX (SPY/QQQ):** SPY — short-gamma, ZGL unresolved, call wall 780 (+0.90%), put wall effectively at spot 773; trend-amplification prior, no clean pin. QQQ — short-gamma but contested, ZGL 734.54, call wall 735 (+0.67%), put wall 720 (−1.39%); a modest bounce re-flips it positive. Both regimes are **one session old**. Advisory, see §2.
- **Top swing build:** **None.** No name was sized. Highest conviction score on the board was CRWV at 5, in a rubric whose LOW band starts at 3 — no HIGH, no MEDIUM.
- **Top LEAP candidate:** **None.** Zero of the LEAP candidates cleared 6-of-9 gates; the accretion gate killed every one.
- **Biggest risk:** the AI-capex cluster. MU/MRVL correlate at **0.848**; CRWV sits at 0.694/0.689 — just under the mechanical line but economically the same bet. Three of five long candidates were one factor. Meanwhile the **largest single ticket in the entire book is a $129.3M SMH Nov-20 630 put** (20,100 lots) — a confirmed protective overlay on exactly that complex. No hedge sleeve is recommended because there is no book to hedge.

**The call: stand aside.** This is the 22nd consecutive empty conviction board.

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — mixed signals, reduce position size, wait for clarity.** Trend UPTREND. SPY 772.67, above SMA20 (757.73) and SMA50 (749.24), +3.95% over 30d, −0.86% from the 90d high. Market breadth by flow: **2,124 bullish vs 4,190 bearish tickers (33.6% bullish)** across 6,314 optionable names.

The label and the tape disagree violently, and two independent lineages agree with each other against the label:

| Source | Reading |
|---|---|
| `uw risk market-regime` breadth | 33.6% bullish flow |
| `fz breadth --group sector` (Finviz, independent lineage) | **132 advancers / 368 decliners, 26.24% green**, avg −0.90%, median −0.95% |
| Cap-weight vs equal-weight | SPY −0.47% vs **RSP −0.89%** — 42bp spread |

This is a **narrow semis/memory melt-up against broad distribution**, not a healthy advance. SNDK (+8.88%) was the top S&P mover; MU/MRVL/AMAT/SOXL/SOXX/SMH/LITE/DRAM/AXTI dominated bullish net premium. Everything else was sold.

**Per-index gamma (current-state EOD book):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 773.01 | `null` (unreliable) | −$367.98M | **FULLY_NEGATIVE** | 780 (+0.90%) | 773 (≈spot; next clean support 765) |
| QQQ | 730.13 | 734.54 (reliable) | +$582.19M | **NEGATIVE** | 735 (+0.67%) | 720 (−1.39%) |
| IWM | — | — | −$41M | **FULLY_NEGATIVE** (flipped today) | — | — |

All three indices broke to negative gamma on the same session. SPY held POSITIVE on 08-13/08-14 (ZGL ~774.7) before selling through it today. IWM held POSITIVE cleanly 08-06→08-14 then broke. QQQ's flip is dated and confirmed in `regime_flip_dates` (2026-08-17, zgl_delta +4.62) but is marginal.

**DTE volume share:** 0DTE 33.4% · weeklies 29.7% · monthlies 19.9% · LEAPs 4.8% → **BALANCED**. No institutional-vs-retail thumb on the scale.

**VRP (`uw historical vrp`):** SPY **+0.0045 FAIR** (IV30 12.87% vs realised 12.42%). QQQ **−0.0395** (IV30 **18.94% vs realised 22.90%**) — Nasdaq options are underpricing realised vol by ~4 points. **This is a premium-BUYING environment on the Nasdaq complex, not a selling one**, and it is the most actionable vol fact on the board.

**Macro backdrop** (`scripts/fred_macro.py`): **stagflationary tilt.** Payrolls **contracted −23k** m/m while core PCE runs **3.29% y/y** (core CPI 2.79%), unemployment 4.1%, 10Y **rising** to **4.68%** (+0.13 over 30d) against fed funds 3.63, USD **weakening** (broad index 120.31 → 118.90), curve normal at +0.53. Growth softening into sticky inflation — specifically hostile to high-multiple long-duration equity, which is the entire long side of today's board.

**Forward event risk (T+N in trading days from 2026-08-17):**

| Event | Date | T+N | Tier |
|---|---|---|---|
| FOMC minutes (July meeting) | 2026-08-19 | T+2 | Tier-2 |
| **Monthly OPEX** | 2026-08-21 | **T+4** | **Tier-1** — $5.18B, largest expiry in the book, call-heavy 2.13:1 |
| Jackson Hole opens | 2026-08-27 | T+8 | ambient |
| MRVL + ULTA earnings | 2026-08-27 | T+8 | Tier-1 (name-specific) |
| **Warsh's first Jackson Hole keynote as Fed chair** | 2026-08-28 | T+9 | ambient Fed-speaker |
| **July Core PCE** | 2026-08-28 | **T+9** | **Tier-1** |
| August NFP | 2026-09-04 | T+13 | outside horizon |
| FOMC decision + SEP | 2026-09-16 | T+22 | outside horizon |

**Every 2–4 week swing entered today holds through two named Tier-1 events.** Aug 28 is a genuine double catalyst — a brand-new Fed chair's first policy signal landing the same day as an inflation print.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book read forward as the prior for the next open. Prose-only, **0 conviction-rubric points**, no backtested predictive claim. Scope is SPY and QQQ only.

**SPY** — spot 773.01, ZGL `null` (**`zgl_reliable: false`**), regime **FULLY_NEGATIVE**, total_gex −$367.98M. Call wall 780 (+0.90%). The put wall computes to 773 — essentially the ATM strike, a massive negative-gamma cluster sitting *on* spot rather than support beneath it; next clean support is 765 (−1.04%, −$194.1M). **Structure bias:** short-gamma / trend-amplification. Dealers hedge pro-cyclically on both sides of the ATM cluster; there is no pin. Debit verticals or a long straddle/strangle bracketing 773 rather than premium-selling structures. **Regime is FRESH — day 1.** SPY held POSITIVE on 08-13/08-14 (ZGL 774.7–774.8) and sold through it today, with the ZGL calculation failing to resolve. That is a real regime break, not a rounding wobble.

**QQQ** — spot 730.13, ZGL **734.54** (`zgl_reliable: true`), regime **NEGATIVE**, total_gex +$582.19M. Call wall 735 (+0.67%), put wall 720 (−1.39%). Note the tension: total_gex sums *positive* despite the NEGATIVE label, because the aggregate is dominated by the 730/735/740 strike clusters — the spot-vs-ZGL geometry is the better read here since the ZGL is reliable. **Structure bias:** fragile short-gamma. Spot is only 0.6% below the flip, so a modest bounce re-flips it POSITIVE. Favour a defined-risk debit vertical toward 720 over an aggressive short-premium or full long-straddle commitment; 734.54/735 is the re-flip zone to watch, and the 730 strike itself is a large positive-GEX magnet that could act as a soft pin if the tape stalls. **Regime is FRESH — day 1**, dated flip confirmed, but contested rather than decisive.

**Mandatory caveats:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and re-computes the ZGL and walls. QQQ's 0.6% margin means a modest gap can flip the regime read entirely.
- **ZGL reliability.** SPY's is `null` and this read leans entirely on the total_gex sign plus spot-vs-wall geometry.
- **Gap risk voids the prior.** FOMC minutes 08-19 and monthly OPEX 08-21 both sit inside the near-dated book.
- **Tooling limit.** `uw` cannot isolate the D+1 expiry (`gex --dte-max 1` errors). This is the standing 0–45 DTE book as the best available proxy.
- **ETF book**, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup

`scripts/zerodte_setup.py` returns `sell_premium: true` and `GO_PREMIUM_SELL_INTRADAY` for both indices. **Read the conditioning before acting on that flag — it is unconditional and today it is misleading.**

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` | **LOW** | **LOW** |
| VIX | 15.19 | 15.19 |
| implied_move_pct | 0.56% | 0.94% |
| expected_range_pct | 1.26% | 1.35% |
| size_scalar | 0.5 | 0.5 |
| suggested_structure | wider iron condor, wings ≈ ±1.26% (short-gamma) | iron fly / short straddle centred 729.55, wings ≈ ±1.35% |
| mean_pnl_open (gross / **net**) | +0.213% / **+0.113%** | +0.336% / **+0.236%** |
| worst_day_open | −1.40% | −2.453% |

**The critical read: `vol_state` is LOW on both, and at LOW VIX this edge does not exist.** `mean_pnl_by_vix_state[LOW]` is **−0.003% gross for SPY** (⇒ **−0.103% net** of the 0.1% assumed round-trip cost) and **+0.072% gross for QQQ** (⇒ **−0.028% net**). Both are net-negative-to-zero at today's tercile. The edge lives entirely in the MID/HIGH terciles (SPY +0.327/+0.316, QQQ +0.456/+0.482 gross), and **VIX at 15.19 sits below the low tercile bound of 16.1**.

**Recommendation: stand aside on the 0DTE premium-sell lane tomorrow.** The headline verdict is a static flag, not a conditional one.

Entry rule if taken anyway: enter at/after the open once the overnight gap resolves; if it gaps beyond the wings, stand aside; hold to the close, never carry overnight. **Tail caveat:** the validation sample contains no vol shock — the short-vol left tail is UNSAMPLED. Advisory, **0 rubric points**, permanently until a vol-shock day enters the sample and net expectancy clears a tail-aware bar.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

**Zero of nine names earn the mechanized +1 DEX-flip line.** `scripts/dex_flip.py` returned `qualifies: false` on SPY, QQQ, IWM, MU, MRVL, SNDK, MSFT, META and TSLA — no verified sign change anywhere in the fleet.

**The entire vanna-squeeze lane is dead today for a mechanical reason:** VIX *rose* +6.6% (15.28 → 14.55 → 14.63 → 14.25 into 08-14, then broke up to 15.19). The falling-VIX leg fails fleet-wide. META and TSLA carry the put-heavy books that could squeeze — both are flagged "vanna pressure, not squeeze."

| Ticker | DEX state / 5d trajectory | Flip? | Vanna squeeze? | GEX regime flip | Swing bias (unscored) |
|---|---|---|---|---|---|
| SPY | POS +$37.7B, **deteriorating hard** (−43% d/d, −55% off 08-13 peak) | No | No (call-heavy) | **Yes — 08-17 → FULLY_NEGATIVE** | NEUTRAL, bearish lean |
| QQQ | POS +$45.7B, flat-to-mild deterioration | No | No | Noisy, tag inconsistent | NEUTRAL |
| IWM | POS +$7.8B, deteriorating (−31% today) | No | No | **Yes — 08-17 → FULLY_NEGATIVE** | SHORT lean — **diverges from price** |
| **MU** | POS +$17.2B, **improving monotonically 5/5 sessions** | No | No | No — clean POSITIVE throughout | **LONG** (strongest trajectory) |
| MRVL | POS +$2.78B, improving (+72% d/d) | No | No | 2 flips, now POSITIVE | LONG lean, sized down (panic 1.056) |
| SNDK | POS +$9.87B, flip already fired 08-11/12 | No | No | Yes, dated ~08-13 | NEUTRAL — extended, panic 1.23 |
| **MSFT** | POS +$15.4B, **deteriorating hard** (−30% today, GEX magnitude −59% off peak) | No | No | No, but magnitude fading | **SHORT lean** (cleanest bearish convergence) |
| META | NEG −$3.18B, **whipsawing** (3 sign changes) | No | No — VIX rising | Yes, twice | **DISQUALIFIED** |
| TSLA | ~flat +$421M, **whipsaw_warning: true** (4 sign changes) | No | No — VIX rising | No | **DISQUALIFIED** |

**IWM carries a genuine divergence worth naming:** its DEX and GEX both broke down on the same session, and it has the largest charm-decay drag of the three indices — yet its +1.36% 5-day return is the *best* of the three. Dealer positioning and price disagree.

---

## 2b. Sector Rotation

**Rotation regime call: `no_change`, confidence LOW.** No canonical pattern fits. Tech is IN (breaking growth→value and value→growth); Industrials IN + Healthcare OUT is half of defensive→cyclical, but Consumer Cyclical OUT directly contradicts that pattern. What is actually happening is **a narrow semis/memory melt-up funded by broad distribution across Discretionary, Communications and Healthcare** — not a rotation.

> ⚠ **Substrate warning.** `uw options-flow sector-flow-persistence` fired **INFLOW with persistence_score 1.0 on 10 of 11 sectors** (Real Estate 0.8) — zero discrimination. It is sign-agnostic **gross turnover**, and it plus `sector-flow` are **one source, not two**. It contradicts the netted source outright on Healthcare, Communication Services and Consumer Cyclical. Direction below reads off the **netted** `market-regime.sector_rotation` only, which is itself a **top-3/bottom-3 truncation** — the middle five sectors are undisclosed and are not inferred.

| Sector | Netted | Gross persistence | Agreement | Verdict |
|---|---|---|---|---|
| Technology | **IN #1 +$222.6M** | 1.0, $4.07B | AGREE | **IN** — but bifurcated |
| Industrials | IN #2 +$41.6M | 1.0, $372.4M | AGREE | **IN** — GE-led, not sector-wide |
| Basic Materials | IN #3 +$2.8M (trivial) | 1.0, below median | sign only | **No call** — fails magnitude bar |
| Consumer Cyclical | **OUT #1 −$124.6M** | 1.0 INFLOW | **DISAGREE** | `watch_only` — **highest-confidence on the board** |
| Communication Services | OUT −$121.7M | 1.0 INFLOW | **DISAGREE** | `watch_only` |
| Healthcare | OUT −$41.2M | 1.0 INFLOW | **DISAGREE** | `watch_only` — least resolved |
| Fin Svcs, Energy, Cons Defensive, Utilities, Real Estate | **undisclosed (truncated)** | — | n/a | **Cannot call** |

**Consumer Cyclical's contradiction was resolved by a third independent source:** XLY ETF options flow is −$6.58M BEARISH, persistent day-to-day, with near-zero call activity. Netted GICS and ETF options now agree *against* the gross-turnover measure. It stays mechanically `watch_only`, but it is a real distribution signal, not a coin flip. Single-name bearish leaders: LULU −$57.0M, TSLA −$33.2M.

**Technology is bifurcated and this matters.** XLK was barely green (+0.16%) and SMH's own instrument read is **MIXED, not persistent**. Semis/memory is bullish (SNDK, MU, MRVL, AMAT, AXTI, LITE, CRWV, CBRS) while megacap software is bearish — MSFT −$48.5M, ORCL −$17.3M, CRWD −$12.9M, QCOM −$11.5M, NOW −$7.2M — independently corroborated by **IGV −$20.99M BEARISH** with put buying.

**The XLE gap, explained:** Energy's gross flow ($369.6M) is the second-largest in the book, larger than Industrials' entire netted inflow. It does not appear in the netted top-3 because the tool discloses only 3 of 11 sectors per side — Energy sits in the undisclosed middle. The ETF layer fills the gap: XLE options are cleanly BULLISH and multi-day persistent (+$6.56M, ask-side call buying across OPEX-week, Aug-28 and Dec/2028 tenors), corroborating XLE's +1.08% day and +3.99% week.

**ETF flow tape (advisory — 0 rubric points), 33 of ≤40 calls used:**

| ETF | 5d net flow | Trend | GICS agreement | Note |
|---|---|---|---|---|
| **SMH** | +$22.21M | MIXED | agree (weak) | **$129.3M Nov-20 630P dominates**; real call buying alongside |
| **EWY** | +$18.69M | BULLISH | n/a (geographic) | clean multi-strike ask-side call buying |
| **XLE** | +$6.56M | BULLISH | n/a (netted undisclosed) | ask-side calls, OPEX + Dec + 2028 LEAP |
| XLI | +$4.75M | BULLISH | agree | — |
| XLV | +$3.80M | BULLISH | **disagree** vs netted OUT | — |
| XLK | +$1.88M | MIXED | agree (weak) | — |
| **XLY** | −$6.58M | BEARISH | **agree** — gross GICS was the outlier | thin options book, one $520K put sweep is most of it |
| **GDX** | −$18.30M | BEARISH | **disagree** vs trivial netted IN | two 2028-12 LEAP puts, $16.98M + $15.51M |
| **IGV** | −$20.99M | BEARISH | **disagree** vs netted IN | reinforces the Tech bifurcation |

---

## 3. Swing Setups (1–6 weeks)

**Empty. No swing position was sized today.**

Six names cleared the confluence gate and were scored. All six finished at `skip` or `watch_only`. The full audit is in §7; the summary:

| Ticker | Dir | Score | Tier | Pre-risk | Gates fired | Final |
|---|---|---|---|---|---|---|
| CRWV | long | 5 | LOW | starter | panic · fundamentals · event · debate | **skip** |
| MU | long | 3 | LOW | starter | fundamentals · event · debate | **skip** |
| MRVL | long | 2 | DROP | skip | cluster · fundamentals · event · debate | **skip** |
| ULTA | vol_short | 2 | DROP | skip | sector · event · debate | **skip** |
| GLD | long | 1 | DROP | skip | event · debate | **skip** |
| MSFT | **short** | −2 | DROP | starter | regime · event · **SHORT routing** | **watch_only** |

### 3a. Long swings (regime-aligned)

None sized. The three long candidates that reached LOW or near it — CRWV, MU, MRVL — are **one bet worn three ways**. MU/MRVL correlate at 0.848; CRWV at 0.694/0.689 sits six and eleven basis points under the mechanical cluster line and escapes the deduction on a rounding error, but is high-beta to the identical AI-capex factor.

**Invalidation levels are recorded even though nothing was entered** (C34 — anchored to real institutional dark-pool shelves from the *second-tier* bucket, not the contaminated top bucket):

- **CRWV** — loses the **$103.82** DP shelf (~2% below spot $105.91). Carries a **distribution caution**: ⚠ three call strikes closed same-day across near/mid/LEAP tenors (100C 4DTE −2,520ct/$2.01M; 150C 151DTE −780ct/$0.78M; 200C 851DTE −486ct/$1.54M, ~$4.32M) while the dark pool was buying. Advisory, 0 points, no sizing impact.
- **GLD** — loses the **$404.83** DP shelf (~0.2% below spot $405.47).
- **MU / MRVL** — no clean second-tier DP shelf; both would fall back to a DEX-reversal rule.

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only` and are never sized** (2026-08-01 P0 #1). This is routing, not suppression — theses are generated, scored and serialized so the counterfactual keeps resolving.

**MSFT — SHORT, watch_only.** The cleanest bearish convergence in the fleet, and the only call on the entire board with a measurable win rate. Three independent reads agree: the largest bearish net premium in the C12-passed book (**−$48.5M**); DEX deteriorating hard (08-10 $26.4B → 08-14 $22.1B → 08-17 $15.4B, −30% today alone); GEX magnitude quietly fading (−59% off its 08-07 peak) with no regime flip — quiet de-risking. Corroborated at instrument level by IGV −$20.99M. Price already −5% off its 08-10 high. **win_rate 0.4962 on n=133 clean rows, market_excess +6.77pp — alpha, not beta.**

Counter-evidence on the record: `multileg-strategist`'s false-positive control fired — a MSFT 2026-09-18 525/570 **bull** call vertical at 30,436/29,805 lots sits inside a net-bearish tape, the canonical "multileg contradicts underlying flow ⇒ likely hedge, not alpha" pattern. It self-assigned SKIP.

**The tension worth stating plainly:** the best-evidenced idea on the tape today was a short, and the book cannot express it. That is the pre-registered counterfactual doing its job — the 2026-08-08 audit needs ~30 decided watch-only shorts before it can be graded, and this is one of them.

**Sweep ledger (informational, 0 rubric points).** The sweep-persistence rubric line was removed 2026-05-23 (P0.3) after two audits measured its marginal contribution at −22pp.

Every mega-cap and index name with high persistence **failed the cum-flow alignment check and was demoted to hedge-flow**: SPXW, QQQ, SPY, NVDA, AAPL all swept 5/5 sessions bearish against `MIXED` 30d flow; IWM's sweeps were bullish against outright BEARISH cum-flow (inverted). MU ($4.05B, the largest single-name cumulative premium in the book), SNDK ($2.80B), NBIS, AMD, INTC and PLTR all carry 4–5 session persistence but **MIXED direction** — high premium, zero directional thesis. Only **SPCX** (5/5 clean bullish, $1.80B) and **SMCI** (3/5 clean bullish, $332M) cleared both bars, and neither found a corroborating agent (§8).

---

## 4. LEAP Builds (6–24 months)

**Empty board. Zero candidates clear 6-of-9 gates.**

The LEAP tape is thin to begin with — LEAPs are **4.8% of DTE volume share** today. The funnel (`uw oi biggest-increases --min-dte 180` ∩ C12 pass list) surfaced only RKT, CRWV, IWM and SPY; the indices are hedges, not theses.

**The universal kill was Gate 4, cumulative-premium-flow accretion.** Every candidate with a real long-dated OI build shows `MIXED` or wrong-sign net flow with **net-as-%-of-gross under ~7%** — that is balanced two-way flow, indistinguishable from noise, not a slow-accretion signature.

| Ticker | Gates | Disqualifier |
|---|---|---|
| RKT | ~2/9 | cum-flow **BEARISH** both windows (90d −7.2%, 30d −13.0%) while call OI builds — flow_conflict, not accumulation |
| CRWV | ~2/9 | the long-dated build is an **851-DTE $35 PUT** (+5,001), bid-heavier 548/775 — wrong side; 90d MIXED 3.1%; conviction-matrix confidence **16.9%** vs a 70 threshold |
| NVDA | 1/9 | 851-DTE 420C build is **bid-heavy 5,403/63 — covered-call WRITING, not buying**; 90d net −0.05% of gross, literally noise |
| SNDK | ~1/9 | the flagged $37.4M 2027-06-17 1050C is deep-ITM at 92.5% IV — **stock-replacement financing** (and see §7: it was *sold*) |
| IREN | ~2/9 | genuine ask-heavy 140C build, but net premium **negative** across both windows |
| MU | 1/9 | 90d MIXED 0.2% net/gross; conviction-matrix scenario MIXED, confidence **3.4%** |
| MRVL, SMH, SOXX, OKLO, MSTR | 0/9 | dropped at Gate 2 — long-dated OI changes de minimis (largest single change 25–1,066 contracts) |

`uw oi position-rolls` returned **0 detected on every symbol and date checked** — a structurally silent gate today, not a name-specific finding.

---

## 5. Volatility Surface

**The headline is a split, and it is the most actionable vol fact on the board.** SPY VRP is FAIR (+0.0045) — no edge. **QQQ VRP is −0.0395**, and the entire semis complex carries the same signature: **MU −0.319** (IV 64.9% vs RV 96.8%, the largest negative in the book), SOXX −0.127, SMH −0.084, MRVL −0.083. *The leadership everyone is chasing is exactly where options most underprice realised chop.* Combined with the fresh short-gamma flip on both indices and VIX +6.6%, that is a coherent long-vol setup into OPEX and Jackson Hole.

Only MDB (+0.205), LULU (+0.237) and ULTA (+0.159) sit in genuine premium-selling territory, and all three are earnings-proximate.

> **Substrate hygiene applied — and it was decisive.** `scripts/term_structure_hygiene.py` (`min_contracts=15`, a **tunable, not audit-frozen**, parameter) was run on 13 names. **10 of 13 raw labels flipped.** Raw BACKWARDATION on 8 names collapsed to KINKED on 6 once the 0DTE bucket was dropped. Today was an expiry day ($2.57B expired), so the contamination was live.

| Ticker | raw → shape (base) | Kink (prominence, contracts) | VRP | Bias |
|---|---|---|---|---|
| **MU** | BACKWARDATION → **KINKED** (CONTANGO) | dte4 = 8/21 OPEX (12.2%, **61,742c** — best-supported in the fleet) | **−0.319** | **BUY VOL** |
| QQQ | CONTANGO → KINKED (CONTANGO) | dte3 = 8/20 (29.7%, **only 9,798c** — thin) | −0.0395 | BUY VOL |
| SMH | BACKWARDATION → KINKED (CONTANGO) | dte4 = 8/21 (38.2%, 8,203c) | −0.084 | BUY VOL |
| MRVL | BACKWARDATION → **KINKED** (CONTANGO) | dte11 = 8/28 (9.3%, 7,101c) | −0.083 | KINKED + catalyst |
| ULTA | KINKED, unflipped (CONTANGO) | dte11 = 8/28 (**20.1%**, 579c) | **+0.159** | SELL VOL |
| SPY | CONTANGO → KINKED (FLAT) | dte4 = 8/21 (6.4%, 55,158c) | +0.0045 | NEUTRAL — mechanical OPEX bump |
| SOXX | BACKWARDATION, genuine | front dte4 is the driver | −0.127 | **DISQUALIFIED** — ratio 1.314 > 1.10 |
| FDX | BACKWARDATION, genuine | thin throughout | +0.023 | **DISQUALIFIED** — ratio 1.581, illiquid |
| MDB | BACKWARDATION → KINKED | dte11 (40.7%, only 536c; 7/20 tenors dropped) | +0.205 | **DISQUALIFIED** — ratio 1.137, thin |
| LULU | KINKED (**BACKWARDATION** base) | dte32 (20.2%, 1,048c) | +0.237 | likely out-of-window earnings — defer |

**Calendar candidates: none qualify.** SOXX and FDX have exactly the right shape — genuine front-loaded backwardation, no catalyst, negative VRP on SOXX — but both exceed the 1.10 disqualifier with no prior-session ratio available to confirm the panic is *falling* rather than building. Watch-only.

**Single-contract IV outliers: none.** The cached `iv_outliers` surface is 100% contaminated by today's 0DTE expiry, dominated by SLV far-OTM call noise reaching 451% IV on 20-lot prints.

**Instrument health notes:** `front-end-iv-ratio` read at `--near-dte 7` fired BACKWARDATION on **4 of 10 (40%)** — genuine discrimination, not the degenerate 8-of-9 seen at the default `--near-dte 1`. `iv-percentile-zscore` **short-delivered on every ticker** (`dates_used: 88`, FDX 87, against a 120-day floor) — **all percentile and z-score reads above are PROVISIONAL**. `iv_rank_high` is degenerate (25 names at exactly 100.0, mostly sub-$5 micro-caps plus malformed tickers REZI1/ATRO1/SGMOQ/SNEX2) and `iv_rank_low` returns all-null — both unusable today.

---

## 6. Risk & Correlation

**Macro headline:** stagflationary — payrolls −23k m/m into core PCE 3.29% y/y, 10Y rising to 4.68% against fed funds 3.63, USD weakening. **Forward Tier-1 calendar:** OPEX 08-21 (T+4), MRVL/ULTA earnings 08-27 (T+8), **July Core PCE 08-28 (T+9)**, NFP 09-04, FOMC 09-16.

**Breadth cross-check (advisory, 0 points):** `fz` reports **132 advancers / 368 decliners, 26.24% green**, median −0.95%. The `uw` regime label reads UPTREND with SPY above both SMAs. **`divergence_flag: true`** — a green-ish index with barely a quarter of names participating is a distribution tell the single label hides. Advisory; it does not override the `uw` regime or change sizing.

**Correlation clusters** (`uw risk portfolio-correlation`, 30d lookback, run against today's candidates rather than the static watchlist):

| Pair | corr | Class | Action |
|---|---|---|---|
| **MU / MRVL** | **0.848** | **CLUSTER (≥0.70)** | `semis_memory_cluster` — MU kept (score 3 > 2), **MRVL −1 tier** |
| CRWV / MU | 0.694 | soft watch (0.60–0.70) | surfaced, **no penalty** |
| CRWV / MRVL | 0.689 | soft watch | surfaced, **no penalty** |

CRWV was **not** upgraded into the cluster despite sitting six basis points under the line — the 2026-05-15 audit removed exactly that discretion after the gate fired at 0.631 in one case and not at 0.703 in another.

**How many real bets is this?** Mechanically five independent positions. **Economically three, arguably two:** (1) one AI-capex bet worn three ways — MU/MRVL at 0.848 outright, CRWV on the same factor escaping only on a rounding error; (2) one real-rates bet — GLD, driven directly by the 08-28 PCE and a new Fed chair's first keynote; (3) one idiosyncratic earnings-vol bet — ULTA. MSFT is a *short* on the same megacap-tech complex the first bet is long, so it partially offsets rather than diversifies. The tool returned `Unknown` sector for all six and "100% in top sector" — a null read, not a finding; the real concentration is the AI-capex factor at 3 of 5 sized-eligible names.

**Fundamentals verdicts (Phase 2b):**

| Name | Verdict | Contradicting evidence |
|---|---|---|
| **CRWV** | **CAUTION −1** | Insider MSPR net-negative **19 of 20 months**, worsening to **−84.9** in Aug (3mo avg −72.41); Viking Global **exited** (Tepper initiated); current_ratio **0.4555**, D/E **6.48** |
| **MU** | **CAUTION −1** | Insider MSPR −33.33 into a **+260% YTD** move; **Tepper cut Micron and exited SanDisk citing memory caution** |
| **MRVL** | **CAUTION −1** | Insider MSPR −30.71, **Aug 2026 at −100 — unanimous selling**; **UBS cut PT $340→$300** same day on a maintained Buy; surprise history a coin flip (−0.94/−0.41/+1.40/+0.27%) |
| **ULTA** | **CONFIRM 0** | none — 3-of-4 beats, insider MSPR **+26.02 net BUYING**, D/E 0.0222 |
| **GLD** | **NA 0** | commodity trust — **NA never penalizes** |

**No VETO was issued.** Three of four graded names are CAUTION on insider selling, and in each case the selling is *accelerating* into the flow the fleet scores as accumulation. That is one pattern, not three.

**Event-risk gate fired on 6 of 6 names.** That is a property of the entry date, not a discrimination between names — every 2–4 week swing entered today holds through OPEX (T+4) and Core PCE (T+9). The gate did no ranking work today and should not be credited with selectivity.

**Debate disconfirmation cuts — the bear met or exceeded the bull on 5 of 5:**

| Name | bull | bear | Note |
|---|---|---|---|
| CRWV | 0.25 | 0.45 | **BOTH_SIDES_LOW** — neither advocate cleared a coin flip |
| MU | 0.45 | 0.65 | |
| MRVL | 0.35 | **0.75** | widest spread on the board |
| ULTA | 0.35 | 0.65 | |
| GLD | 0.45 | 0.45 | tie — **≥ still trips the gate**; **BOTH_SIDES_LOW** |

Residuals carried verbatim per the 2026-07-25 bin-floor change (0.15 ladder) — CRWV's 0.25 is not clamped to 0.55.

**Adverse-flow exit candidates: none.** Prior group `conviction_2026-08-14` = **[ROST]**. `uw watchlist alerts` returned 3 alerts (4.9× volume spike, IV rank **91.1**, an $11.8M single DP trade); `uw watchlist scan` shows flow still **bullish**, net_flow +$1.26M, OI +1,789; `fz quote-drift` shows no field changes since 08-14. The thesis has not reversed — the volume and IV rank are ROST's own earnings (~08-20) approaching. **Flagged for awareness:** anyone still holding ROST is holding through a print at a 91 IV rank.

Off-group but corroborating: unfiltered alerts surfaced **HYG with a 4.82 put/call ratio** and a $63.7M DP print. HYG topped the raw OPEX pin board but carries **−$816M net GEX at the pin strike**, flanked by +$766M and +$735M just above — a knife's edge, not a wall. Credit is being hedged hard into OPEX.

**Hedge sleeve: none recommended.** Net book delta is zero because the book is empty; buying protection would be a naked long-vol punt dressed as risk management. For *legacy* exposure only, the tape inverts the usual reflex: front-end IV is the **cheap** leg (SPY ratio 0.727, QQQ 0.749 vs 30d) and QQQ realised is already outrunning implied. So do not sell the front to fund anything and do not put on a calendar. If hedging residual long delta, the structure is a **defined-risk QQQ or SPY put spread expiring 2026-08-28** — that expiry is where Core PCE and the Warsh keynote land, it spans the 08-21 OPEX roll-off and the warned 08-24 gamma air pocket, and it is where front-end IV is cheapest relative to 30d. Independent corroboration of the defensive read: **SQQQ** (−3× inverse QQQ) shows 5/5 bullish confluence — that is bearish Nasdaq positioning, not a long.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Empty. No name reached raw_score 7.** The highest score on the board was 5.

**Expectancy lens `[advisory — expectancy is not yet a live sizing axis]`:** per-tier realised expectancy and payoff ratio **cannot be displayed today**. No name reached HIGH or MEDIUM, and the 2026-08-08 audit found the HIGH/MEDIUM bands **structurally empty** across the post-freeze corpus — which is also why the out-of-regime freeze-lift has been unrunnable for eight consecutive cycles. The standing calibration finding remains that the **DROP pile has out-realised the traded book in every audit that has measured it** (2026-07-18: DROP 43.3% > book 41.1% > sized 38.6%). Today's board is entirely DROP/skip, which is the behaviour that finding rewards.

Full per-ticker audit follows, since the scored names are the deliverable even though none were sized.

### CRWV — raw 5, LOW, `dark_pool_accumulation` → **skip**

| Line | Pts | Source | Evidence |
|---|---|---|---|
| accumulation conjunction | **+3** | accumulation-hunter / `uw insights institutional-accumulation` | ACCUMULATION, buy/sell 1.53, price_30d +26.9%. **Only name in the union clearing C11 on all three gates**: cum_flow_30d +$240.26M sign-aligned, ≥$50M, **6.92% of $3.47B gross** (only name above the 5% scale-relative floor) ⇒ full +3, not halved |
| multi-day OI build | +1 | accumulation-hunter / `uw historical oi-trend` | BUILDING 5/5, net OI +324,837 |
| sector leader | +1 | sector-rotation-strategist / `uw risk market-regime` | Technology leader, +$8.8M; Tech is #1 netted inflow |
| cum-flow accretion | **0** | quant / `uw historical cumulative-premium-flow` | **Withheld by the C28 intent screen** despite a qualifying +$240.26M BULLISH read — condition (a) fails on a live distribution_flag |

`win_rate: null` / `NA(substrate)` — `dark_pool_accumulation` is a supported class but returns **0 rows market-wide** (verified live). `market_excess: null` — **ungradeable**. Fundamentals **CAUTION**. Debate 0.25/0.45. Dark pool: mega buy_ratio 0.659 with **3 of 4 megas clean intraday**; block 0.666 across 48 trades/$117.0M. `dp_block_to_float_ratio` 0.000578; `insider_cluster_flag` false.

**4 gates fired: panic (front_end_iv_ratio@7 = 1.159 > 1.10 — re-read at the risk stage because Phase 1 never emitted it, and it is the highest-scored name that carries panic), fundamentals, event_risk, debate.** Invalidation: loses the $103.82 second-tier DP shelf.

### MU — raw 3, LOW, `sector_rotation` → **skip**

| Line | Pts | Source | Evidence |
|---|---|---|---|
| multi-day OI build | +1 | quant / `uw historical oi-trend` | 5 consecutive build days, net +162,572 (2,836 increases vs 1,029 decreases) |
| sector leader | +1 | sector-rotation-strategist / `uw risk market-regime` | Technology leader, +$39.1M; gates (a)(b)(c) all pass |
| vol-surface KINKED, VRP-aligned | +1 | vol-surface-scout / `scripts/term_structure_hygiene.py` | raw BACKWARDATION → KINKED (base CONTANGO); best-supported kink in the fleet (dte4 OPEX, 12.2%, 61,742c); **VRP −0.319**, largest negative in the book |
| accumulation conjunction | **0** | accumulation-hunter / `uw insights institutional-accumulation` | **NEUTRAL, buy/sell 1.15 near parity — fails the gate outright.** Line does not apply at all, not even halved |
| cum-flow accretion | 0 | quant / `uw historical cumulative-premium-flow` | +$612.78M but **only 0.91% of $67.5B gross** — balanced two-way flow |

**A correction to the quant's audit trail, verified in the main loop.** The quant characterised MU's OI build as "put-heavy and DISCONFIRMING" and used that as its tie-break discriminator. That is overstated: the five largest put builds are **$0.01 penny options** — 155P/150P/160P/145P all at `avg_price $0.01` at 4 DTE against spot **$1,015.62**, i.e. **84–86% out of the money with zero delta**; the 650P is −36% OTM at $0.10. **Total premium across all five is $190,644**, of which the four penny strikes are **$39,704**, against $67.5B of 30-day gross flow. That is rounding error, not bearish positioning. The +1 line is direction-agnostic so the *score* is unchanged, and MRVL dropped anyway so the *ranking* is unaffected — but the interpretation should not stand. Both the MU bull and bear accepted the correction.

`win_rate: null` / `NA(substrate)` — `sector_rotation` is not among the 5 supported classes. `market_excess: null`. Fundamentals **CAUTION**. Debate 0.45/0.65.

**The largest gap on the board between how good a name looks and what it earns:** dealer-positioning called MU the cleanest coherent multi-day buildup in the fleet (DEX rising monotonically five straight sessions, GEX clean positive throughout, per-strike cluster 940–990 confirming it is not a ZGL artifact) and it **scored zero**, because the frozen rubric pays only for a verified DEX *sign change* and MU never flipped — `dex_flip.py` returns `qualifies: false` precisely *because* the buildup was sustained rather than a reversal. That is the rubric working as designed. The bear's unrefuted counter is that VRP −0.319 is a **long-VOLATILITY, delta-neutral** read being borrowed to support a long-**DELTA** thesis.

**3 gates fired: fundamentals, event_risk, debate.**

### MRVL — raw 2, DROP, `oi_build` → **skip**

+1 oi-trend (5 build days, net +38,760, **call-heavy and confirming**: 240C 11DTE +2,977/$2.46M, 227.5C +2,789/$1.52M, 235C +2,593/$0.88M) · +1 sector leader · +1 earnings-scout SELL VOL emitted (line is direction-agnostic) · **−1 flow_conflict_lite** (+$76.66M sign-aligned but bottom-quartile, below the union Q1 of $115.81M) · **0** vol-surface KINKED, killed by C13 routing (earnings-scout owns the `earnings_vol` object; both agents read the identical dte11 = 8/28 kink). **Σ = 2.**

**The quant refused to adjudicate a genuine two-agent contradiction** — earnings-scout said SELL VOL, vol-surface-scout said the negative VRP (−0.083) means the bump may be *underpriced* and leaned BUY. It ruled the vol leg NO CALL and let the directional long stand, noting that under SELL VOL the name scores 3/LOW/starter and would rank *above* MU. That refusal is the entire reason for the drop, and it is a reason for less confidence, not more.

Fundamentals **CAUTION** (insider MSPR Aug at −100, UBS PT cut). Debate 0.35/**0.75** — widest spread on the board. The bear's unrefuted point: **the 2026-12-18 200 PUT (+1,927 contracts at $27.60 = $5.32M) is larger than the entire 240C earnings build ($2.46M)** — the single largest premium commitment in the name is a December put, four months past the print.

**4 gates fired: cluster (semis_memory 0.848 with MU, MU kept), fundamentals, event_risk (three named in-horizon events — OPEX T+4, own earnings T+8, Core PCE T+9), debate.**

### ULTA — raw 2, DROP, `earnings_vol`, direction `vol_short` → **skip**

+1 oi-trend (5 build days, net **+1,431** — mechanically earned, materially trivial: top builds are 161/160/80/80/71 contracts) · +1 earnings-scout SELL VOL · **0** vol-surface SELL VOL, **C13 collision on the identical object** (both agents report dte11 = 8/28, prominence 20.1%, 579 contracts — the same numbers) · **0** flow_conflict (class is non-directional, the switch does not apply). **Σ = 2.**

Correctly **not** routed by the short-direction rule — `vol_short` structures are explicitly out of scope. `confluence_score: 6` (the only name in the union appearing in the Step 0 funnel; informational, zero scoring use). `implied_move: 9.5%` (earnings-scout's derivation 0.7979 × 0.6885 × √(11/365); the CLI's native 2.92% is the known sub-1-day defect).

Fundamentals **CONFIRM 0** — the only clean verdict on the board. Debate 0.35/0.65.

**Worth registering as a rubric-coverage gap, not a verdict on the trade:** ULTA is the cleanest setup on the board by agent agreement — two independent agents both say SELL VOL, VRP +0.159 positive, iv_rank 73.3, confluence 6/6, front_end_ratio 0.845 CONTANGO confirming the richness is isolated at the kink, and contrarian-scanner screened it and correctly declined to fade it — **and it scores 2**, because the frozen rubric has almost no line a pure short-vol earnings setup can earn once C13 removes the double-read.

**A substrate discrepancy the bear surfaced and nobody can currently resolve:** the CLI's `screener earnings-catalyst` reports `implied_move_perc: 0.0292` (**2.9%**) against earnings-scout's derived **9.5%** — a **>3× gap on the exact number the entire "premium is rich" claim rests on**. Until that reconciles, "68.9% ATM IV is rich enough to sell" cannot be asserted responsibly.

**3 gates fired: sector (Consumer Cyclical is the #1 netted OUTFLOW — a gap-risk objection to a short-vol book, not a directional one), event_risk (own earnings T+8 is EXEMPT as the event play; OPEX T+4 and Core PCE T+9 both sit inside the very expiry being sold), debate.**

### GLD — raw 1, DROP, `dark_pool_accumulation` → **skip**

+1 accumulation **halved from +3 by C11** · +1 oi-trend BUILDING 5/5 (net **+1,169,122** — the largest OI build of any name in the union by an order of magnitude) · **−1 flow_conflict_lite**. **Σ = 1.**

**The most consequential result of the day.** accumulation-hunter's HIGH-conviction call on the **cleanest tape in the entire fleet** does not survive its own flow check. All 7 mega prints were timestamp-verified *outside* the closing-cross window (08:00Z premarket through 22:12:51Z after-hours) on a day when AMAT's entire $756.6M mega tier was one pegged price and RDDT's $2.24B was 100% inside a 3-minute window. buy_ratio 2.13, the cleanest in the fleet.

And the 30-day cumulative premium flow is **−$233,263,332** — net **BEARISH** against a long thesis, on $7.86B gross (−2.97%), **holding at 90d (−$321,830,603)**. C11 fails on two independent gates: the sign is *opposed*, not merely unconfirming, and 2.97% is below the 5% scale floor.

**flow_conflict split, knife-edge:** sign flip ✓, but magnitude **|−$233.26M| vs the union median $236.76M — short by $3.50M, or 1.5%** ✗, and no explicit OPPOSITE label ✗. The −3 leg fails by a hair, so it falls to −1 `flow_conflict_lite`. Under the alternative $50M phrasing GLD takes −3 and scores **−1**. Either way it drops, so the knife-edge is immaterial to the outcome — but it is on the record.

Debate 0.45/0.45 — a tie, which still trips the gate, and **BOTH_SIDES_LOW**. The bear's decisive argument: the bull's "different desks, different horizons" defense makes a **falsifiable prediction that fails** — if today's buying were fresh signal overwriting stale positioning, the 90-day cumulative should be *less* negative than the 30-day. It is **more** negative. The selling is compounding, not stale. Reinforced by **~$440M of same-day GLD/IAU ETF outflows** and **GDX at −$18.3M with two 2028-12 LEAP puts ($16.98M + $15.51M)** — the miners hedged long-dated while the metal accumulates. Three independent lineages.

**2 gates fired: event_risk (GLD is maximally exposed to the OPEX/Core-PCE pair — a real-rates instrument into an inflation print stacked with a new Fed chair's first keynote), debate.** Invalidation: loses the $404.83 second-tier DP shelf.

### MSFT — raw −2, DROP, `bearish_flow`, direction `short` → **watch_only**

+1 oi-trend (5 build days, net +51,116, mixed composition) · **−3 flow_conflict** — mechanical and unambiguous: cum_flow_30d is **+$631,918,893 net BULLISH against a SHORT thesis** (sign flip ✓) at a magnitude **exceeding the union median $236.76M** ✓ · 0 sector · 0 cum-flow · 0 multileg. **Σ = −2.**

**The only call on the board with a real win rate.** P0.3 clean-query protocol executed in full: 157 rows pulled at `--top-n 200`; latest data date 2026-08-17 so a 5-day forward window requires `signal_date ≤ 2026-08-10`; **15 rows dropped as clamped** — note the tool's own `truncated_signals` field reads **16**, a mismatch against the authoritative filter and exactly the documented undercount. Clamping was verified directly: SPY rows dated 08-11 *and* 08-12 both report `price_after_5d = 772.67`, the 08-17 close. C12 floor dropped NDX (9 rows, an index with no share volume, fail-closed). **Kept n = 133. win_rate = 66/133 = 0.4962.** Headline `win_rate: 50.3%` and `total_signals: 157` **quarantined, not quoted**. C2 benchmark over the same kept windows = 0.4286 ⇒ **market_excess = +0.0677 — alpha, not beta.**

Gates: N-cap non-binding (n=133); the **sub-0.50 floor BINDS** ⇒ starter/skip; C4 opening gate caps half (OI building but two-way composition, so opening is not confirmed in the short direction). The ladder would have said **starter**; the SHORT-routing rule makes it **`watch_only`**, terminally.

**2 gates fired plus terminal routing: regime (UPTREND vs short — though note breadth at 26.2% green actually *agrees* with the short; the mechanical source is `market-regime.trend`), event_risk, SHORT routing.** `debate` gate is a genuine no-op — MSFT sits outside the debated top-5, so both residuals are null and the gate cannot evaluate.

---

### Conviction rubric (verbatim, frozen version `2026-06-12`)

```
Daily conviction score = Σ:
  +1  MECHANIZED DEX flip or vanna-squeeze in trade direction — verified SIGN CHANGE only, computed by
      scripts/dex_flip.py, never a level.                        [UNEARNED FLEET-WIDE TODAY — 0 of 9 qualify]
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified institutional
      tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms (sign aligned AND
      |cum_flow_30d| >= $50M); else halved (floored) +3 -> +1.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days >= 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: award only when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +1  uw historical cumulative-premium-flow net directional accretion in trade direction (30d) —
      INTENT-SCREENED: award only when (a) no C28 distribution_flag on the name, AND (b) on dividend payers
      in an ex-div window the accreting prints are not deep-ITM sub-parity calls.
  +1  sector-rotation-strategist names ticker as single-name leader within a rotating sector — CONDITIONAL:
      (a) sector persistence_score >= 0.6 AND (b) cum_premium_flow_30d aligned with thesis AND
      (c) |cum_flow_30d| >= $50M. Default 0.
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored play type)   [UNEARNED TODAY]
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)                          [UNEARNED TODAY]
  -2  contrarian-scanner flags as overcrowded long with RISING pc-ratio-zscore (VRP positive) — an
      INFORMED-FLOW CONTINUATION penalty, not a fade signal.                           [UNEARNED TODAY]
  -3  flow_conflict — applied mechanically when cum_premium_flow 30d direction is clearly OPPOSITE
      dominant_signal_class (sign flip + magnitude > today's union-median |cum_flow_30d|, or explicit
      OPPOSITE label).
  -1  flow_conflict_lite — 30d cum_premium_flow read is MIXED (signed sum near zero, or aligned but
      bottom-quartile magnitude in today's union).
      [flow_conflict and flow_conflict_lite are MUTUALLY EXCLUSIVE — apply ONE, never both.]
  # TIER GATES applied by risk-monitor in 2d — contribute 0 to raw_score, never appear in score_components:
  #  -1 [TIER GATE] correlation cluster (pairwise corr >= 0.70)
  #  -3 [TIER GATE] market-regime conflicts with trade direction
```

**Tiers:** ≥9 HIGH (full) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch-only) · ≤2 drop.

**Six of eleven positive rubric lines paid nothing to anyone today.** The scoreable surface reduced to four lines. Today's **union-median |cum_flow_30d| = $236,761,118**; union Q1 = $115,810,000.

---

## 8. Watch-only — single signal, no confluence

Surfaced by one agent, failed the ≥2-agent confluence gate. Journaling only, **not for trade entry**.

| Ticker | Flagged by | Why it failed |
|---|---|---|
| **SNDK** | sector-rotation only | **The day's top S&P mover (+8.88%) fails the gate.** Only sector-rotation flagged it (Tech leader, $111.1M — largest bullish net premium in the book). Against that: **multileg-strategist proved the $37.4M 2027-06-17 1050C was SOLD, not bought** — `ask_side_volume: 0, bid_side_volume: 400`, OI 382 vs 400 traded (opening size). A deep-ITM LEAP call sale at 92.5% IV reads as upside-capping / profit-taking — **distribution on the day's top mover**. accumulation-hunter returns NEUTRAL; sweep-tracker 5/5 but MIXED; dealer-positioning NEUTRAL (its real flip fired 08-11/12 and is priced, front-end ratio **1.23** is the most panicked in the fleet after a $1,229→$1,786 run); leap-radar DQ as stock-replacement |
| **DRAM** | opex-pin only | The **only** name on the entire OPEX board. Pin strike 60 vs spot 60.38 (0.6%), OI mass 104,754, **gex_at_pin +$25.63M on a genuine long-gamma wall** (total_gex +$94.4M, ZGL 57.17 below spot). Structure would be an iron fly at 60 into 08-21. **But** realized vol is **97.6% (rv20) / 104.4% (rv60)**, +5.36% today, +21.75% over 5d — a live melt-up with a ~$3.70 daily ATR against a $0.39-wide pin. No second agent |
| **SPCX** | sweep-tracker only | 5/5 sessions clean bullish, $1.80B cumulative — the only non-mega-cap with full persistence *and* clean direction. No corroborating agent, no resolvable single-print detail |
| **SMCI** | sweep-tracker only | 3/5 clean bullish, $332M. RV60 ~101%, so premium magnitude is not abnormal for the name |
| **GE** | sector-rotation only | Named Industrials leader (+$28.0M). **accumulation-hunter explicitly declined to flag it** — 77% of the mega tier ($269.8M of $350.5M) is closing-cross clustered at $369.43; genuine clean intraday megas total only ~$70M. "A watch, not a flag" |
| **ARKG** | multileg only | Double calendar (short 8/21 41-straddle / long 9/18 45-straddle), ~35,000 lots per leg, delta-neutral, front IV 68–106% vs back 40–44%. MEDIUM conviction but the **underlying catalyst is unidentified** |
| **QQQ** | vol-surface only | BUY VOL on VRP −0.0395. gamma-flip-tracker's short-gamma read is advisory/0-point by design and cannot count toward the gate. Belongs in §5, not as a scored call. The dte3 kink rests on only 9,798 contracts vs dte1's 111,520 — thin |
| **SMH** | vol-surface only | BUY VOL on VRP −0.084. sector-rotation read SMH as MIXED/not-persistent, which is not a positive flag. Carries the $129.3M protective overlay |
| **META** | sector-rotation only | Comm Services bearish leader (−$48.4M). dealer-positioning **explicitly disqualified** it — DEX whipsawing 3 sign changes, vanna put-heavy but squeeze invalid because VIX rose. Short would route watch_only regardless |
| **LULU** | sector-rotation only | Largest Consumer Cyclical bearish leader (−$57.0M). vol-surface found no actionable edge (apparent backwardation is probable out-of-window earnings contamination) |
| **IWM** | dealer-positioning only | SHORT lean — DEX and GEX both broke down on 08-17. But **price diverges**: IWM's +1.36% 5d is the best of the three indices |
| **XLE / EWY** | sector-rotation ETF tape only | Advisory instrument-level context (+$6.56M / +$18.69M BULLISH). Not funnel-eligible |
| **SOXX / FDX / MDB / CRWD** | vol-surface / earnings-scout | All explicitly **disqualified** rather than flagged — front-end ratios of 1.314 / 1.581 / 1.137 exceed the 1.10 threshold with no falling-trend confirmation; CRWD has no qualifying kink (2.5% prominence vs a 5% floor) |

**Also dropped, upstream of the gate:** the entire `signal_confluence_bullish` micro-cap cohort (HP, ENVX, RAM, ASST, ZIM, JMIA, NIQ, CCO, COHX, AVL, FRSH, EROC, STNE, SRPT, CCXI, IMVT) failed the **C12 liquidity floor** (price ≥ $5, 20d dollar-ADV ≥ $50M) and never entered the funnel. 76 of 84 screened names passed; 8 failed (7 on ADV, ENVX on price at $3.60).

---

## Process notes

- **Step 6.5 (batched strategy synthesis) skipped** — `uw playbook batch-scan` operates on the HIGH/MEDIUM list (raw_score ≥ 7) and that list is empty.
- **Step 8.5 (deep-dive hand-off) skipped** — no HIGH-tier names, which the command specifies as a skip condition.
- **Watchlist write-back: nothing written.** `conviction_2026-08-17` was **not created**. Only CRWV (5) and MU (3) reached LOW pre-gate and both were driven to `skip`; MRVL/ULTA/GLD/MSFT were never eligible below the 3-point floor. Per the corrected write-back rule (write only LOW+ names post-gate, never the raw top-5), zero names qualify. An empty group is a valid outcome and no empty group was created.
- **`yahoo_fundamentals` returned HTTP 401** on CRWV, MU and MRVL during the Step 6 deep dives — the yfinance path was down this run. Finnhub carried the fundamentals lane alone; `fz` was healthy for per-ticker enrichment.

### Substrate defects observed today (for the register)

1. **Closing-cross contamination — severe and pervasive.** AMAT's *entire* $756.6M mega tier is one pegged price ($535.31, 20:00:12–21:33:51Z; genuine intraday megas ~$25M). RDDT's $2.24B mega tier is 100% clustered in a **3-minute window** (20:04–20:06Z). GE 77% contaminated. MGM's mega tier is two prints at an identical $43.78 with a nonsense `buy_sell_ratio` of 656,462. AAPL dominated by repeated $305.59 closing prints. **Only GLD's mega tier was fully clean.**
2. **Term-structure raw labels — 10 of 13 flipped** after hygiene; raw BACKWARDATION on 8 names collapsed to KINKED on 6.
3. **`iv-percentile-zscore` short-delivered on every ticker** — `dates_used: 88` (FDX 87) against a 120-day floor.
4. **`sector-flow-persistence` fired INFLOW/1.0 on 10 of 11 sectors**, contradicting the netted source on three of them.
5. **`analyst-vs-flow` analyst leg populated 0 of 3** — reconfirms the known 0/21 defect.
6. **`iv_rank_high` degenerate** (25 names at exactly 100.0, sub-$5 micro-caps, malformed tickers REZI1/ATRO1/SGMOQ/SNEX2); **`iv_rank_low` returns all-null**.
7. **`fz` doubled-first-letter ticker bug on 20/20 rows of both screen lanes** (AABCL→ABCL, FFDMT→FDMT, IIOVA→IOVA — de-corrupted via Company-name verification). Per-ticker `fz_enrich` healthy.
8. **`signal-backtest` `truncated_signals` undercount** — field reads 16 against an authoritative 15 dropped rows.
9. **`implied_move` >3× discrepancy on ULTA** — CLI screener 2.92% vs derived 9.5%.
10. **`opex-concentration` unusable** — dominated by micro-caps at `concentration_pct: 100` on total OI of 1,000–4,600 contracts.
11. **`uw risk portfolio-correlation` returned `Unknown` sector for all six names** and "100% in top sector" — a null read presented as a finding.
12. **`validate_decision.py` C16 warning is a false positive on commodity ETFs.** It flagged GLD's `dp_block_to_float_ratio: null` as an instrumentation gap "despite `fz_context.available=true`". Verified upstream: `fz_enrich --ticker GLD` returns `float_shares: null` with `short_interest` in `upstream_gaps` — a commodity trust has no float concept in the Finviz model, so `null` is the **correct** value here, not a missing one. The check keys on `available=true` without accounting for instrument type. Envelope left as-is.

### Rubric-mechanics observations (applied as frozen, not acted on)

1. **The sector-leader +1 double-counts the cum-flow field, and the weaker test paid.** Gates (b)/(c) passed on MU/MRVL/CRWV and paid +1 while the standalone cum-flow line read **0** on the identical field — because the standalone line carries extra requirements (accretion label + intent screen) that (b)/(c) lack. Gate (a) was non-discriminating (persistence 1.0 on 10 of 11 sectors).
2. **The +3 accumulation conjunction requires an OI-build leg, and the separate +1 oi-trend line pays for that same observation again.** On CRWV, 4 of 5 points rest partly on one OI series. Not previously registered.
3. **`+1 multi-day OI build` fired 6-of-6 — a 100% population firing rate, zero discrimination** — including on ULTA at a 1,431-contract net build and on MU with a composition the quant misread.
