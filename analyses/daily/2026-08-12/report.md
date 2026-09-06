# Daily Market Analysis — 2026-08-12

## Executive Summary

- **Regime + GEX state:** `TRANSITIONAL` on a `UPTREND` tape — SPY 772.49 (+0.25%), above both the 20SMA (753.19) and 50SMA (748.12), −0.56% from its 90d high. VIX **14.55 (LOW tercile)**. **SPY short-gamma** (spot 0.84% below ZGL 779.01, walls coiled at ±0.33%), **QQQ long-gamma but one day old with spot sitting ON the ZGL** (723.70 vs 723.64). Price breadth 51.9% green but **flow breadth 33.9% bullish (2:1 bearish)**. Sector lean off the **netted** authority: IN Industrials / Financial Services; OUT Consumer Cyclical / Communication Services / Technology.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`. Non-binding today: every row is already `starter` or `skip`.
- **Next-session GEX (SPY/QQQ):** **SPY** — short-gamma · ZGL 779.01 · call wall 775 / put wall 770 · *no stable pin, regime flipped 3× in 8 sessions; debit vertical or stand aside.* **QQQ** — long-gamma · ZGL 723.64 · call wall 730 / put wall 715 · *born today, spot on the flip line; wide condor or stand aside, not a tight fly.* Advisory, see §2.
- **Top swing build:** **None.** The post-gate book is **flat**. The highest-scoring name (EWY, raw 3, LOW) routes to `watch_only`; the other four are below the raw<3 drop floor.
- **Top LEAP candidate:** **None.** `leap-positioning-radar` returned an empty book — zero of eleven Gate-1 survivors reached `conviction-matrix DIRECTIONAL_LONG >70`, and every one failed the 90d accretion gate.
- **Biggest risk:** the **`AI_infra_memory_cluster`** — NBIS/CRWV 0.888, EWY/CRWV 0.778, EWY/NBIS 0.729, NBIS/SMCI 0.713 — and on the extended run **EWY/MU 0.905** and **EWY/SNDK 0.882**. EWY is the highest-correlated node to the memory complex in the whole universe: it is not a diversifier, it *is* the memory bet with a Korean ticker. Any book across these names runs **one factor at 7× notional**. No hedge recommended — net delta is zero.

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — mixed signals, reduce position size, wait for clarity.** Trend `UPTREND`. Guidance: *half position sizes, favor defined-risk, iron condors in range.* SPY 772.49, +2.75% over 30d.

**The tape breadth is the story, and the two breadth measures disagree because they measure different things.** UW **flow** breadth is 33.9% bullish (2,135 bullish vs 4,164 bearish tickers of 6,299). `fz` **price** breadth is 51.89% green (261 advancers / 241 decliners / 1 unchanged of 503), avg change +0.20%, median +0.09%. Both are true: slightly more names rose than fell, while far more names saw net-bearish options premium. Neither is a distribution tell on its own — but the top mover was **SMCI +19.02%** against a +0.09% median, which says the gains were **concentrated, not broad**.

**What actually happened today was a violent intra-tech rotation on a flat index.** This framing was outcome-relevant and is easy to miss:

| Bucket | Names |
|---|---|
| Index — **flat** | SPY +0.25% · QQQ +0.73% · RSP +0.18% · IWM +0.57% |
| **AI-infra / memory / neocloud — ripping** | NBIS **+34.14%** · CRWV +19.28% · SMCI +19.02% · CBRS +11.63% · DELL +9.87% · IREN +9.86% · SPCX +9.65% · SKHY +9.01% · CRDO +8.26% · COHR +8.24% · DRAM +7.68% · STX +7.03% · SOXL +6.89% · SNDK +5.76% · ORCL +5.36% · MU +4.92% · APLD +4.92% · AMAT +4.29% · INTC +3.32% · NVDA +3.03% |
| **Mega-cap software / platforms — bleeding** | META −3.38% · DDOG −2.38% · MSFT −2.26% · PLTR −2.23% · AMZN −1.83% · TSLA −1.59% · AAPL −0.87% · NFLX −0.78% · AVGO −0.01% · APP −4.68% (5d **−27.30%**) · MELI −5.76% · UBER −4.05% |
| Sector ETFs | XLK +1.49% · XLRE +0.93% · XLU +0.48% · XLP +0.46% · XLV +0.26% · XLF +0.21% · XLE +0.16% · XLI +0.10% · **XLC −0.90% · XLY −1.13% · XLB −1.24%** |

Per-index gamma (current-state EOD book; §2 carries the forward read for SPY/QQQ):

| Index | Spot | Zero-gamma | ZGL reliable | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|---|
| SPY | 772.49 | 779.01 (−0.84%) | yes | +$1,125.8M | **NEGATIVE** (short-gamma) | 775 (+$551.3M, +0.33%) | 770 (−$151.7M, −0.32%) |
| QQQ | 723.70 | 723.64 (−0.008%) | yes | +$889.8M | **POSITIVE** (long-gamma, 1 day old) | 730 (+$141.0M, +0.87%) | 715 (−$35.8M, −1.20%) |
| IWM | 302.71 | *not pulled* | — | positive, deep | POSITIVE | *not pulled* | *not pulled* |

IWM's ZGL and walls are blank by design, not by omission: `gamma-flip-tracker`'s scope is SPY/QQQ only. `dealer-positioning-strategist` covered IWM on the swing horizon — DEX +$10.4B accelerating from $4.1B, GEX POSITIVE and deeply positive today, front-end ratio 0.824 CONTANGO, charm **negative** (−164,069, the only negative charm in its set).

**DTE volume share** (`MARKET`-level only): 0DTE 30.6% · weeklies 24.1% · monthlies 29.6% · LEAPs **4.1%** ⇒ `BALANCED`. Monthlies+LEAPs 33.7% vs 0DTE 30.6% — no strong retail/institutional skew, so rotation and swing calls get neither a boost nor a haircut from the DTE mix. LEAPs at 4.1% is thin, which is context for §4's empty book.

**VRP — the central dislocation of the day.**

| | IV30 | Realised σ30 | VRP | Regime |
|---|---|---|---|---|
| SPY | 12.11% | 12.39% | −0.0028 | `FAIR` — no edge from VRP alone |
| QQQ | **18.65%** | **24.01%** | **−0.0536** | **`PREMIUM_BUYING`** — vol cheap vs realised |

QQQ implied sits ~5.4 vol points *below* its own realised tape, and rv20 is **24.4% on QQQ vs 13.7% on SPY** (RSP 10.4%, IWM 15.0%). That is an extreme index-dispersion signature, and the single-name tape explains it: rv20 **NBIS 191.1%**, REPL 321.4%, SOXL 168.4%, AEHR 164.0%, IREN 150.4%, SNDK 149.2%, CRWV 137.0%, MTRN 127.4%, CBRS 124.0%, SMCI 116.3%, APLD 112.1%, PLTR 105.9%, MU 102.8%. **Index vol is cheap-to-fair while single-name realised vol is enormous.** Any "high IV rank ⇒ sell the premium" conclusion had to be reconciled against realised vol on the same name — and today it does not survive that check anywhere.

**Macro backdrop** (`scripts/fred_macro.py`): yield curve **normal** (10Y−2Y +0.48) · core CPI **2.79%** YoY · core PCE **3.29%** YoY · unemployment **4.1%** · payrolls **−23k MoM (negative)** · 10Y **4.70%, rising** (+14bp/30d) · broad USD **weakening** (119.06, −2.07/30d) · fed funds **3.63%**. Read: **mildly stagflationary.** Core PCE is sticky-high while payrolls printed negative. A rising 10Y *with* a weakening dollar is term-premium/inflation-risk repricing, not growth optimism — and fed funds 3.63% against core PCE 3.29% leaves almost no real policy room.

**Forward event risk (next ~10 trading days):**

| Event | Date | T+N | Impact |
|---|---|---|---|
| CPI (Jul) | 2026-08-12 | T+0 | **released today — already in this tape** |
| PPI (Jul) + initial jobless claims | 2026-08-13 | T+1 | medium-high |
| Retail Sales (Jul) + Consumer Sentiment (prelim) | 2026-08-14 | T+2 | high |
| FOMC **minutes** | 2026-08-19 | T+5 | medium |
| Initial jobless claims | 2026-08-20 | T+6 | low-medium |
| **Monthly OPEX** | 2026-08-21 | T+7 | medium |
| Consumer Confidence + new home sales | 2026-08-25 | T+9 | medium |
| Initial jobless claims | 2026-08-28 | T+12 | low-medium |
| **Core PCE (Jul)** | 2026-08-29 | T+12 (eff. 08-28) | **high** |
| FOMC decision + SEP | 2026-09-16 | ~T+23 | high |

`risk-monitor` deliberately did **not** spend deductions on PPI, Retail Sales or FOMC minutes. The firing bar is named, dated, Tier-1 binary only — {CPI, FOMC *decision*, NFP, PCE}, own earnings, or a held-through monthly OPEX. Three high/medium prints inside T+5 is the "busy week" atmosphere the 2026-06-06 re-scope was written to stop taxing: the widened gate fired on 47/52 calls and its downgrades realised **exactly the ungated win-rate (43% vs 43%)**. A gate that taxes everything equally is a haircut, not a filter.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — open interest that persists overnight — read forward as the *prior* for the next session's open. It is prose-only, contributes **0 points** to the conviction rubric, and makes **no backtested predictive claim**. Predictive validation of these levels lives in `/weekly-analysis`'s rolling §2 backtest, not here. Scope is **SPY and QQQ only**.

**SPY — short-gamma with no pin to sell into.** Spot 772.49 sits 0.84% *below* ZGL 779.01, and `total_gex` is positive at $1,125.8M. Nominally short-gamma ⇒ trend/breakout. But the walls sit unusually **tight** — call wall 775 (+0.33%), put wall 770 (−0.32%), roughly 2.5 points each side, i.e. **tighter than the 0.66% implied move**. That is the 0–45d book coiling dealer hedges right around spot rather than confirming a runway. And `gex-time-series` shows the regime **flipped three times in eight sessions** (POS→NEG 08-05, NEG→POS 08-07, POS→NEG 08-10, holding NEG through 08-12). *Structure bias: not a premium-sell pin — there isn't a stable one. Small defined-risk debit vertical, or stand aside; a clean break of 770 or 775 on fresh 0DTE OI could accelerate given short gamma.*

**QQQ — long-gamma, but born today and sitting on the flip line.** QQQ flipped NEGATIVE→POSITIVE **today**, and spot (723.70) sits essentially **on** the ZGL (723.64, 0.008% away) — the least stable possible read; a fractional dip reverts the book to short gamma. QQQ's own rv20 is 24.4% versus SPY's 13.7% even though the ETF closed flat, because the tape underneath is an AI-infra-vs-software rotation that **nets to near zero at the index level**. The "POSITIVE/pin" label masks a book on a knife's edge. *Structure bias: nominally pin-favouring, but the same-day flip plus extreme realised vol argue against sizing an iron fly at the pin. Wider condor with room, or stand aside — a break of either wall likely flips the regime label outright.*

**Mandatory caveats — stated, not buried:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and re-computes the ZGL and walls. Treat both books as a starting hypothesis, QQQ especially.
- **ZGL reliability.** Both pass the ~5%-of-spot trust threshold (`zgl_reliable=true`), but *reliable* ≠ *stable*. SPY's ZGL spiked to 789.87 on 08-11 with `total_gex` collapsing to $209M — a one-day extrapolation glitch consistent with the documented failure mode.
- **Gap risk voids the prior.** PPI and initial jobless claims print **08-13, inside the very session this prior describes**, and Retail Sales + Consumer Sentiment print 08-14. Either can gap spot through a wall before the book re-hedges.
- **Tooling limit.** `uw` cannot isolate the D+1 expiry (`gex --dte-max 1` errors). This is the standing **0–45 DTE** book — the best available proxy, not the isolated next-session expiry.
- **ETF book, not index book.** SPY/QQQ carry more retail noise and creation/redemption mechanics than the cleaner SPX/NDX gamma book.
- **Cross-confirmation was unavailable this run.** The cached `greek_screener` returned SPX deep-ITM 7000-strike *financing* prints rather than SPY/QQQ contracts, so the highest-gamma near-dated strikes could not be independently confirmed; the per-strike GEX grid is the only load-bearing source here. `expiry_heatmap` is market-wide (SPX-scale premium): 08-13 $544.6M vs 08-14 $3.45B vs 08-21 OPEX $4.25B — directional context only.

### 2a. Next-session 0DTE premium-selling setup — **STAND ASIDE BOTH INDICES**

The GEX walls above are a **map**, not a pin — wall-as-magnet backtested NO_GO, as did every directional 0DTE signal. What validated is a **delta-neutral premium-selling** edge. It does not apply tonight.

`scripts/zerodte_setup.py` returned `verdict: GO_PREMIUM_SELL_INTRADAY` and `sell_premium: true` for both indices — **and both are UNCONDITIONAL and must be overridden.** `vol_state` is **LOW** (VIX 14.55; tercile bounds 16.3 / 17.8). Read `mean_pnl_by_vix_state[vol_state]`, not the unconditional mean:

| | LOW gross | − 0.10% assumed round-trip cost | **LOW net** | MID | HIGH |
|---|---|---|---|---|---|
| SPY | +0.005% | −0.100% | **−0.095%** | +0.342% | +0.343% |
| QQQ | +0.063% | −0.100% | **−0.037%** | +0.473% | +0.513% |

**Both lanes are net-negative in this VIX tercile.** The edge lives only in MID/HIGH. The figures that look tradeable — `mean_pnl_open_net_pct` +0.13% SPY / +0.249% QQQ — are the **unconditional** ones, and they are the misleading numbers. `pnl_basis` is percent-of-underlying-spot-notional **gross**, not premium-collected and not margin-relative.

Three independent corroborations, each sufficient alone:
1. **No pin to sell into.** SPY's regime flipped 3× in 8 sessions with walls *tighter* than the implied move; QQQ's long-gamma label is one day old with spot 0.008% from the ZGL.
2. **QQQ VRP is PREMIUM_BUYING.** Selling QQQ premium means selling vol already 5.4 points cheap to its own realised tape — the wrong side of the cleanest vol read on the board.
3. **The left tail is unsampled.** The validation set contains **no vol shock**, and win-rate (88.3% SPY / 85.0% QQQ) is explicitly *not* the promotion metric for a negatively-skewed short-vol strategy. An 85%-win, unsampled-tail strategy at negative net expectancy is the worst available combination.

Selling premium tomorrow means paying 0.1% in frictions to collect a modelled 0.005–0.063%, with no pin, on cheap vol, into an unmeasured tail. **Stand aside.** Reference figures if the regime changes: SPY implied move 0.66% / expected range 0.80% / size_scalar 0.5 / worst day −1.4%; QQQ implied move 1.04% / expected range 1.39% / size_scalar 0.5 / worst day −2.453%.

**Promotion bar unchanged:** this lane stays advisory / 0 rubric points **permanently** until *both* a vol-shock day enters the sample and net expectancy clears a tail-aware bar.

---

## 2b. Swing Dealer Positioning (1–4 weeks)

`dealer-positioning-strategist` ran all ten names through the mechanized `scripts/dex_flip.py` against an 11-session dated window (2026-07-29 → 08-12, ISO dates, 0 fetch errors).

**Exactly one name qualifies for the +1 mechanized line: META, short.**

| Ticker | dex_flip (mechanized) | vanna squeeze | GEX regime flip | front-end IV (dte 7/9) | Swing bias | Conf. |
|---|---|---|---|---|---|---|
| **META** | **TRUE — short**, ratio 4.42, `whipsaw_warning=FALSE` | FALSE (put-heavy but VIX fails strict 3d test) | TRUE 08-11, deepened FULLY_NEGATIVE 08-12, multi-strike | 0.732 CONTANGO | **SHORT** | med-high |
| SPY | FALSE (positive since 07-31) | FALSE (call-heavy) | choppy, 3 flips/10d | 0.783 CONTANGO | NEUTRAL | low |
| QQQ | FALSE (positive since 08-03) | FALSE | choppy, 4 flips/10d | 0.823 CONTANGO | NEUTRAL | low |
| IWM | FALSE (positive since 08-03) | FALSE | 1 flip + oscillation | 0.824 CONTANGO | NEUTRAL / mild-long | low |
| MU | FALSE — "prior run of opposite sign is 0 sessions" | FALSE | none (stable POSITIVE) | 1.016 FLAT | NEUTRAL | low |
| NBIS | FALSE — **near-miss rejected as whipsaw** | FALSE | TRUE 08-12, **1 day old** | 1.126 BACKWARDATION | LONG-leaning | low |
| SMCI | FALSE — **ZERO sign changes in the window** | FALSE | none (POSITIVE full 15d) | 1.106 BACKWARDATION | LONG-leaning | med |
| DELL | FALSE (stale July flip) | FALSE | settled POSITIVE since 08-04 | **1.461** BACKWARDATION | LONG-leaning | med |
| PLTR | FALSE | FALSE | none, but DEX+GEX decaying 4–5d | 1.138 BACKWARDATION | NEUTRAL / watch | low |
| MSFT | FALSE — `sign_changes_in_window=0` | FALSE | settled POSITIVE, decelerating | 0.965 FLAT | NEUTRAL-cautious | low |

**META's flip, verbatim from the script:** *"META net_dex 2026-08-11 +2,354,830,886 → 2026-08-12 −2,205,674,149; prior 7 sessions (2026-08-03 … 2026-08-11, all positive); |flip| 2,205,674,149 vs floor 499,222,470 (0.25× trailing-10 median 1,996,889,880)."* `sign_changes_in_window=2`, no whipsaw. It is corroborated by GEX flipping POSITIVE→NEGATIVE on 08-11 and deepening to **FULLY_NEGATIVE** on 08-12 (`total_gex` −$14.0M, the only negative print in the 15-day window), confirmed **not** a single-strike artifact — negative gamma spread broadly across strikes $520–590, below spot.

**The counter-signal on META matters and is named:** it carries the **only put-heavy vanna book in the set** (`net_vanna +4,898`; `put_vanna +17,095` > `|call_vanna| 12,197`), and the tool's own note reads *"Classic vanna-squeeze setup if VIX collapses."* The flag is FALSE only on a technicality — VIX's down-run broke at two sessions on the 08-10 uptick (08-07 14.90 → 08-10 **15.46 up** → 08-11 15.28 → 08-12 14.55). One more clean down-day sequence activates a squeeze directly against the short.

**Everything else in the set is a DEX/GEX *level*, not a flip.** SMCI and DELL are legitimate multi-week persistence stories, but a positive monotonic DEX in an up-tape is what the rubric explicitly treats as **beta** — which is precisely why that line was demoted +3→+1 and mechanized. None of them feeds the scored line.

**Substrate defect, escalated: the ZGL-grid artifact has spread beyond SPY/QQQ/IWM/MU.** Implausible single-day `zero_gamma_level` price values appear in `uw historical gex-time-series` across nearly every name pulled — MU prints $10–70 against a ~$860–920 spot for the whole window; QQQ prints a stray 249.5 among ~700–770 values; DELL swings $69–528 against a $380–480 spot with 7 flagged regime flips 07-24→08-04; META shows wild single-day swings. The agent correctly read only the `regime` **label** and `total_gex` sign/magnitude, which move smoothly and are internally consistent. Do not trust the raw ZGL *price* from this endpoint.

---

## 2c. Sector Rotation

**Rotation regime call: `growth→value`, confidence MEDIUM.**

Direction is read off the **netted** authority only (`uw risk market-regime .sector_rotation`), pulled dated for all five sessions in the persistence window since the cache holds only today's snapshot:

| Sector | 08-06 | 08-07 | 08-10 | 08-11 | 08-12 | Netted persistence | Gross | Verdict |
|---|---|---|---|---|---|---|---|---|
| **Financial Services** | absent | absent | +37.4M IN | +13.8M IN | **+24.2M IN** | 3 consecutive IN | +$478.0M | **AGREE → call stands** |
| **Industrials** | +20.8M IN | +79.5M IN | absent | +6.7M IN | **+86.2M IN** | 4-of-5 IN | +$529.0M | **AGREE → call stands** |
| Technology | +620.3M IN | +110.4M IN | −279.9M OUT | −140.8M OUT | **−34.0M OUT** | 3 consecutive OUT | +$3.92B | **DISAGREE → watch_only** |
| Communication Svcs | +9.4M IN | −18.9M OUT | −26.7M OUT | absent | **−37.1M OUT** | 3-of-4 OUT | +$923.9M | **DISAGREE → watch_only** |
| Consumer Cyclical | −44.6M OUT | −30.8M OUT | absent | −53.9M OUT | **−79.9M OUT** | 4-of-5 OUT, accelerating | +$402.7M | **DISAGREE → watch_only** |

Healthcare, Energy, Materials, Utilities and Consumer Defensive fail persistence (mixed sign or single-day) and are appendix-only.

**Two structural notes that decide how much of this is usable:**
- **`sector-flow` and `sector-flow-persistence` are ONE gross-turnover source** (call\$ − put\$, sign-agnostic) and cannot express direction. Netted-vs-gross disagreement on **3 of the top-5 gross sectors** is the churn signature that routes those calls to `watch_only`. Technology's netted OUT is also **decelerating** (−280M → −141M → −34M), so the growth leg could resolve either way within days.
- **`persistence_score == 1` and `trend == INFLOW` for ALL 11 sectors.** The ≥0.6 gate is satisfied by every sector including the three that are netted-OUT ⇒ **zero discriminating information** (recurring C47-family defect). Where the sector gate fired below, durability came from the netted source's own dated 3-consecutive-session run, not from this field.

**ETF flow tape (advisory — instrument-level, what the GICS aggregates cannot see).** All 21 canonical ETFs ranked on 5d `cumulative-premium-flow`; no skips.

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| **EWY** | +$16.1M BULLISH | inflow #1 of 21 | $87.9M block @20:00:01Z at mid (closing-cross ⇒ creation/redemption tell, **not** accumulation) | **ask-side call sweeps dominant** — 135C $6.5M ask, 180C $6.4M ask | n/a (Korea) | SK Hynix / Samsung read-through |
| **SMH** | +$12.6M MIXED | inflow #2 | two ~$100–135M blocks 20:00–20:47Z, modest vs mid | thin/mixed | **disagree** vs netted Tech OUT | NVDA, CRWV, SMCI, SNDK |
| **XOP** | +$3.2M BULLISH | inflow #3 | $76.9M mid-day block, +0.25 vs mid | thin (<$500K top sweep) | agree, but Energy broke persistence | — |
| **IGV** | **−$11.1M BEARISH** | outflow | **$177.4M single print @20:47Z, +3.09 vs mid** | **$4.25M ASK-SIDE PUT BUY, K97 Nov** | **agree** with netted Tech OUT | META, MSFT, DDOG, PLTR, APP |
| **XLY** | −$5.7M BEARISH | outflow | $20.9M block near mid | **$17.9M ASK-SIDE PUT BUY, K112.5 Dec** | **agree** with netted Cyclical OUT | AMZN, TSLA |
| **GDX** | **−$46.5M BEARISH** | outflow, last of 21 | blocks near mid, no distribution signature | calls **sold at bid** (86C −$3.05M, 90C −$1.30M) | disagree vs gross Materials +$180M | — |

Mid-ranked and near-flat: XLE +2.1M, KRE +0.8M, XLU +0.6M, XLC +0.08M, XLRE +0.01M, ITB −0.04M, **XLK −0.35M MIXED**, XLP −0.42M, XLB −0.74M, XLF −0.98M, XLI −1.53M, TAN −0.11M, EWT +0.23M, XBI −3.6M, XLV −5.3M.

**The finding: the tradeable structure today is the INTRA-Tech split, which GICS structurally cannot see.** SMH (semis/AI-infra) absorbs inflow while IGV (software) shows confirmed distribution — the largest single DP print in the batch plus an aggressive ask-side put buy. That is the mechanism behind the Technology netted/gross conflict: software is genuinely being sold, and the gross Tech number is inflated by call-buying concentrated in the NBIS/CRWV/SMCI/SNDK/DELL complex. **XLK itself is flat/MIXED at −$0.35M** — the broad Tech SPDR shows no signal at all; the real split lives one level down.

**Single-name leaders and the conditional +1: zero names clear all three gates.** Stated explicitly rather than forced:

| Sector (confirmed IN) | Candidate | (a) persistence ≥0.6 | (b) 30d cum-flow aligned | (c) \|cum_flow_30d\| ≥ $50M | Verdict |
|---|---|---|---|---|---|
| Industrials | SPCX | ✓ 1.0 | ✗ −$7.26M MIXED | — | **fails** |
| Industrials | GXO | ✓ | ~ +$50.6K (noise) | ✗ ≪ $50M | **fails** |
| Industrials | UNP | ✓ | ✓ +$4.66M | ✗ ≪ $50M | **fails** |
| Financial Svcs | IREN | ✓ | ✗ −$70.9M MIXED | — | **fails** (GICS tag also miscoded — IREN is an AI-infra/datacentre operator) |
| Financial Svcs | KKR | ✓ | ✓ +$5.76M | ✗ ≪ $50M | **fails** |

The ETF tape is **advisory** — it strengthens the existing conditional sector-leader +1 via `gics_agreement` and cum-flow alignment, and adds **no new rubric points**. NVDA (+$303.3M 30d), CRWV (+$168.5M) and SMCI (+$363K) are reported as **instrument-level context only** because GICS Technology is itself `watch_only`. SNDK's +$1.08B is flagged as **contaminated** (see §6).

*Swing-book implication:* two confirmed sector rotations (Industrials, Financial Services IN) and **no single name inside either clears the accretion bar** — sector context passes to the quant without the rotation bonus. Software names (META/MSFT/DDOG/PLTR/APP) are `watch_only` short candidates, not sized shorts.

---

## 3. Swing Setups (1–6 weeks)

### 3a. Long swings (regime-aligned)

**Empty. No long swing is sized today.**

Four longs entered the rubric and all four are `skip`. The table records them because the reasoning is the deliverable:

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **EWY** | 3 (LOW) | Institutional Oct16 165C/130P risk reversal + Sep18 add-ons = leveraged bullish bet on Korean semiconductor exposure (SK Hynix / Samsung are top holdings) | Oct16 165C/130P risk reversal; Sep18 170/190 1:2 ratio + 195/215 vertical | Loses the **$161.21** shelf (07-30 snapback low); full crash replay ≈ $146 | **`watch_only`** |
| **NBIS** | 2 (DROP) | Cheapest vol in the book (VRP −83.2pp) + fresh DEX/GEX positive flip, carried as directional long | — | — | **`skip`** (below floor) |
| **CRWV** | 2 (DROP) | Cheap vol (VRP −59.8pp) + 30d cum flow +$168.5M | — | — | **`skip`** (below floor) |
| **SMCI** | 1 (DROP) | Cheap vol (VRP −32.8pp) + persistent positive DEX level + $60B order backlog | — | — | **`skip`** (below floor) |

**Why the whole long side died — one signature, found independently three ways.**

*(1) Every long shows call-side OI CLOSING dominance on the day of its own rip.* This is the most consistent read on the board:

| Ticker | Calls closed | Puts closed | Ratio | Largest single print |
|---|---|---|---|---|
| CRWV | −9,879 ct / $10.8M | −1,651 ct / $259K | 6:1 count, **42:1 premium** | `CRWV260821C00100000` dte9 −7,158 ct / $6.40M on vol 20,655 |
| EWY | −5,804 ct / $20.54M | — | — | `EWY261016C00165000` −5,244 ct / $19.99M — **the scored structure's own leg** |
| NBIS | −3,861 ct / $14.07M | −1,051 ct / $5.07M | 3.7:1 count | `NBIS260821C00240000` dte9 −2,098 ct; LEAP `NBIS270115C00110000` −393 ct / $4.79M |
| SMCI | −5,148 ct / $6.41M | −346 ct / $786K | 15:1 count | — |

For reference, the GDX print that earned a `distribution_flag TRUE` was −1,794 contracts on $2.99M. CRWV's top print is **4× that contract count and 2.1× the premium**. That is the signature of holders and overwriters monetising into strength, not fresh opening conviction. It zeroed the intent-screened cum-flow +1 on **all four**.

*(2) The class base rate is negative.* Market-wide `bullish_flow` under the clean-query protocol: **WR 0.4406 on n=143 (11 truncated rows dropped) against a same-window SPY benchmark of 0.5105 — market excess −0.0699.** Long-flow signals lost to simply being long SPY. Four of five scored names are longs.

*(3) Entry quality.* NBIS **+34.14% in one session on rv20 191.1%**; CRWV +19.28% on rv20 137.0%; SMCI +19.02% (5d +24.04%) on rv20 116.3%. Only EWY (+5.16%, rv20 70.7%) is not at a same-session price *and* vol extreme.

**The evidence class does not match the trade expression.** NBIS, CRWV and SMCI each have exactly one non-degenerate scored point, and in all three cases it is a **vol** signal (negative VRP) being carried as a *directional long*. Buying cheap vol on a name realising 137–191% is a defensible vol trade; it is not a reason to be long the stock after a 19–34% day. Both the NBIS and CRWV bulls conceded this and **abandoned the directional expression** for delta-neutral long vol; the SMCI bull declined to defend a long at all and chose "wait for a pullback."

**And the bears killed the vol reframe too, on term structure.** NBIS's curve is a **two-tenor earnings spike**, not a structural dislocation: dte2 155.6% → dte9 117.4% → dte16 108.8% → dte30 104.3%, and the entire curve out to 2028 sits in a tight **103–119% band** including the Jan-2027 LEAP (118.5%). IV30 101.75% *is* the resting level. The −83.2pp VRP is an ordinary IV read against an RV30 of 184.98% **mechanically inflated by one +34.14% day** (a 29.3% log move) inside the trailing window — and earnings were **today**, so the vol-inflating event has already fired. The 309-DTE term-skew reads `COMPLACENT` (0.0123, ratio 1.012): if smart money believed in a structural re-rating either way, the risk-reversal would have moved. CRWV is the same shape (dte2 128.3% → dte30 81.4% → dte44 80.8%, so a 30–45 DTE straddle buys 81–83% IV, not cheap in absolute terms) with one honest partial counter — `iv_rank` is only **15.09**, so IV *is* cheap relative to CRWV's own 52-week range.

**Sweeps** (`sweep-tracker`, informational — 0 rubric points; the sweep-persistence rubric line was removed 2026-05-23 P0.3). **Nothing was affirmatively handed up, and the reason is a substrate failure:** raw `uw options-flow sweeps --date 2026-08-12` returned **100% SPX index structuring** (top 20 rows all SPX/SPXW deep-ITM/OTM at 7000/8000/9000 strikes, $96M–$1.25B per leg) — **zero single-name rows.** `sweep-ratio` and `smart-money-flow` were saturated with SPY/QQQ 0DTE noise, GLD, sector-ETF puts and penny-premium micro-caps.

Persistence-confirmed (≥3 of 5 sessions), 5-day cumulative premium:

| Ticker | Dir | Sessions | 5d premium | Chasing? | Read |
|---|---|---|---|---|---|
| MU | bearish | 5/5 | $3.61B | **yes, +4.92%** | Do NOT surface as a short — call-selling / protective-put buying into strength |
| NVDA | bearish | 5/5 | $3.42B | yes, +3.03% | Mega-cap filter; demoted to hedge-flow footnote, cum-flow alignment unverified by this lane |
| SNDK | bearish | 5/5 | $1.48B | **yes, +5.76%, rv 149%** | Same divergence class as MU |
| AAPL | bearish | 5/5 | $976M | no (−0.87%) | Mega-cap filter; direction at least not contradicted by price |
| **NBIS** | bearish | 4/5 | $759M | **EXTREME, +34.14%, rv 191%** | *"The single largest price/flow divergence on the board… un-tradeable on this evidence alone"* |
| PLTR | bullish | 4/5 | $1.12B | price −2.23% (5d +7.96%) | The one persistent bullish name, diverging the *opposite* way — dip accumulation or stale decaying OI, unresolved |
| GOOGL | bearish | 3/5 | $337M | no (−0.08%) | At the persistence floor; weakest premium of the group |
| GLD | bullish | 3/5 | $793M | n/a | Only non-equity persistence, independent of the rotation story |

Disqualified as `MIXED` despite high session counts: TSLA 5/5, MSFT 5/5, SPX 5/5, AMD 5/5, META 5/5, INTC 5/5, AMZN 4/5, IWM 2/5.

**Correction the contrarian lane surfaced, and it matters.** The Step 0 single-day framing — "MU −$68M net flow but +4.92%", "AMD −$41.9M but +1.82%" — does **not** survive `uw insights price-vs-flow`, which measures a multi-**week** window. Over that window MU is **−11.7%** and AMD **−10.7%** with **aligned bearish flow**. Today's pop is a bounce inside a continuing downtrend: **continuation, not divergence**, and therefore not a fade.

### 3b. Short / fade swings (defined risk only)

**Every directional short prints as `watch_only` (2026-08-01 audit P0 #1).** The section still runs and carries full theses; no directional short is sized. Short-vol structures and defined-risk short legs are unaffected — the rule governs directional short *alpha* only.

**META — SHORT, raw_score −1, `watch_only`. The highest-information row on the board.**

*Thesis:* the fleet's only qualifying mechanized DEX sign flip (short, 4.42× the magnitude floor, no whipsaw, 1 of ~11 names tested), corroborated by GEX flipping POSITIVE→NEGATIVE 08-11 and deepening to FULLY_NEGATIVE 08-12 across a broad $520–590 strike zone, plus instrument-level software distribution (IGV −$11.1M 5d, a $177.4M single DP print, a $4.25M ask-side put buy) and a call-side-closing intent screen that is thesis-*consistent* (−8,475 ct / $36.5M calls vs −832 / $3.26M puts). Fundamentals **CONFIRM the short**: insider MSPR −55.84 with 18 of 20 months net-selling, last quarter **missed −16.03%** breaking a 3-quarter beat streak, EPS growth **−3.69%** against revenue **+27.65%** = live margin compression as 2026 capex steps to **$130–145B**.

*Invalidation / resolution test:* a reclaim of **$590+** with GEX flipping positive again is the flip being noise; a clean break below **$520** with GEX still negative is the thesis playing out.

*Why it is not traded, stated honestly:* the routing rule rests on a paired McNemar result that **strengthened** at the last audit (`ALL/short` p=0.0115 → **0.0038**, BH-surviving), with UP −13.0pp and DOWN −14.1pp near-identical ⇒ **mis-selection, not mistiming** — which retires the "shorts regain edge in a downtrend" clause. On top of that, the score itself is negative because 30d cum-flow is **+$434,995,751 BULLISH against the short** (5.0× the union median, 2nd largest of 14), the front end is **0.732 CONTANGO** so the vol market prices zero near-term stress, and the only put-heavy vanna book in the set is a squeeze waiting on three clean VIX down-days. **Do not trade it. Do resolve it.**

Other `watch_only` short candidates, none sized: **MSFT** (DEX decelerating −21% DoD to $20.83B, never flipped), **PLTR** (DEX decaying 4 sessions off an 08-07 peak while price cracks — but `sweep-tracker` reads it *bullish* 4/5, genuinely contradictory), **DDOG** (5d −14.92%), **APP** (5d **−27.30%**), **MRVL** and **AVGO** (see §6), **COHR**.

---

## 4. LEAP Builds (6–24 months)

**Empty book. Zero candidates clear 6-of-9 gates.** This is the correct output for this tape, not a search failure.

**Gate 1 passed** (`oi-trend` BUILDING ≥5 consecutive days with long-dated contracts present) — 11 names: LLY, UNP, ALB, GXO, KMI, MPC, TLT, GDX, SLV, ABCL, ASTS. Failed: KKR (2 days), WEC (0 long-dated), MTCH (2), ARMK (0 long-dated), ETN (2), THC (0), ACHC (4).

**Gate 8 (`conviction-matrix` DIRECTIONAL_LONG > 70) killed every survivor:**

| LLY | UNP | ALB | GXO | KMI | MPC | TLT | GDX | SLV | ABCL |
|---|---|---|---|---|---|---|---|---|---|
| MIXED / 8.9 | MIXED / 9.8 | **COVERED_CALL** / 29.3 | DIR_LONG / **61.7** | DIR_LONG / 39.7 | DIR_LONG / 44.1 | MIXED / 9.8 | **COVERED_CALL** / 24.1 | MIXED / 6.5 | MIXED / 6.3 |

GXO at 61.7 is the best of the batch and still under the bar. **Gate 4 (90d cum-flow accretion as % of gross) failed across the board too** — all flat-to-noise or wrong-direction: LLY +1.82% MIXED, UNP +1.47% MIXED, ALB −7.36% BEARISH, GXO −20.07% BEARISH, KMI −0.78%, MPC +2.06%, TLT −3.72%, GDX −2.20%, SLV −0.94%, ABCL +8.97% BULLISH.

29 position-rolls were detected market-wide, **none** touching the candidate list. Market-wide fresh DTE>180 OI growth is dominated by protective puts (AG/HL silver miners), macro-hedge ETF structure (VIX/XOP/XLU/EEM) and speculative single-name calls (HTZ/T).

**Closest near-miss — ASTS, disqualified on structure, not on a thin margin.** It cleared Gates 1, 2, 3, 5, 6 and 7 with the strongest fresh-LEAP print of the whole scan: `ASTS281215C00105000`, DTE 856, OI **300 → 4,307** (+4,007, 13.4×), $13.2M prior premium, zero rolls (consistent with a genuinely fresh position). Dark pool was clean: `institutional-accumulation` ACCUMULATION at buy/sell **2.27**, `block-stratified` `highest_tier = mega` with mega buy_ratio **1.00** ($16.1M) and block buy_ratio 0.915 (15 trades, $28.8M), DP shelf **$74.31** (338,658 sh / $25.17M / 17 trades), and it **passed the closing-cross screen cleanly** (largest print 20:47:12Z, outside the 20:00–20:25Z window, only 14.6% of DP volume, spread across $73.21–74.60).

**It died on Gate 8: `conviction-matrix` returns `COVERED_CALL` at confidence 26.7** — *"Dark pool buying + call selling — yield enhancement, capping upside"* — with call **bid** volume 50,632 exceeding call **ask** volume 37,646, i.e. net call **selling**. A holder is building the underlying via dark pool while writing calls against it. **Upside is capped, so directional alpha is ~zero** — the same structural blind spot as the documented merger-arb case, caught here by a second agent looking at the same name from a different angle. Gate 4 also fails: 90d net is only **0.44% of gross** ($36.8M on ~$8.4B, MIXED) even though the 30d is +$100.2M / 5.9% (BULLISH) — the two windows disagree.

**Macro overlay applied throughout:** every name that moved >4% today was rejected as a structurally poor LEAP entry (excluded IREN, CRWV, DDOG, SNDK, ORCL, MU — long-dated premium bought at a local price *and* vol extreme). And with the **10Y at 4.70% and rising** (+14bp/30d) against a weakening USD — term-premium repricing, not growth optimism — paying up for long-duration convexity is a direct headwind. TLT's own 90d flow (−3.72%, MIXED) offers no confirmation of a "buy duration" thesis either. LEAPs were only **4.1% of market volume** today.

*Callback:* ASTS next session if `conviction-matrix` flips off COVERED_CALL (call **ask** volume overtaking bid) while the 856-DTE 105C build persists — that would convert a yield overlay into a genuine directional signal.

---

## 5. Volatility Surface

**Substrate hygiene first, because today is an expiry day and the raw labels are near-worthless.** SPY/QQQ `260812` contracts dominate `most_active`, so the `dte_approx: 0` bucket (250–480% avg IV) inverts every front-vs-back comparison. All names were classified through `scripts/term_structure_hygiene.py --min-contracts 15`. **5 of 10 raw labels flipped** for `vol-surface-scout` and **4 of 6** for `earnings-scout`; 3 of 10 and 3 of 6 respectively flipped at the monotonic base-curve level too. `min_contracts` is a named tunable, **not audit-frozen**.

**The headline: cheap single-name vol against its own realised tape — a buy-vol dispersion setup, not a sell-premium one.** Every AI-infra/memory/neocloud mover carries deeply negative VRP:

| Ticker | IV30 | RV30 | VRP | Regime | Hygiene shape / base | front-end (9v30) | Implied move* |
|---|---|---|---|---|---|---|---|
| **NBIS** | 101.75% | 184.98% | **−83.2pp** | PREMIUM_BUYING | BACKWARDATION / held | 1.126 | ~18.5% |
| SNDK | 87.00% | 148.78% | −61.8pp | PREMIUM_BUYING | BACKWARDATION / held | 1.101 | ~15.3% |
| CRWV | 75.62% | 135.44% | −59.8pp | PREMIUM_BUYING | BACKWARDATION / held | **1.141** (highest) | ~14.6% |
| IREN | 92.29% | 149.00% | −56.7pp | PREMIUM_BUYING | BACKWARDATION / held | 0.994 FLAT | ~15.7% |
| PLTR | 45.23% | 100.80% | −55.6pp | PREMIUM_BUYING | KINKED / BACKWARDATION (**both flipped**) | 1.138 | — |
| MU | 65.49% | 100.94% | −35.5pp | PREMIUM_BUYING | KINKED / BACKWARDATION held | 1.016 FLAT | — |
| SMCI | 75.11% | 107.86% | −32.8pp | PREMIUM_BUYING | BACKWARDATION / held | 1.106 | ~13.8% |
| CRDO | 100.68% | 102.15% | −1.5pp | **FAIR** (outlier) | KINKED / BACKWARDATION held | 0.954 FLAT | — |
| QQQ | 18.65% | 24.01% | −5.4pp | PREMIUM_BUYING | KINKED / **CONTANGO** (base flipped) | 0.823 | ~2.38% |
| SPY | 12.11% | 12.39% | −0.28pp | **FAIR** | KINKED / FLAT (**both flipped**) | 0.783 | — |

\* **All implied moves in this table are parametric proxies** (IV·√(DTE/365) off the nearest surviving hygiene tenor), **not quoted ATM straddle mids** — no straddle-price tool exists in this toolset. This is the C42(b) blocker and it persists.

**Kinks and their anchors:**
- **KINKED with a genuine catalyst: none.** All ten tickers were cross-checked against the cached 149-name `earnings_catalyst` list — **zero matches**. QQQ's kink at 2026-08-14 (dte 2, prominence 9.4%) is the PPI/Retail-Sales cluster; SPY's at 2026-08-20 (dte 8, 17.7%) is the day before OPEX; MU's at 2026-08-21 (dte 9, prominence **26.3%** — largest of the batch, plus a secondary at dte44/09-25 at 42.6%) is OPEX/macro, **not** MU earnings. These are macro-event kinks, so no earnings-scout hand-off is warranted from this scan.
- **BACKWARDATION with no catalyst (nominal calendar candidates): NBIS, CRWV, SMCI, SNDK, IREN — all FAIL the entry gate** and are **reclassified as buy-vol candidates.** Two reasons: the elevated `front_end_iv_ratio` readings (1.10–1.14) cannot be confirmed *falling* (no prior-session snapshot available, so the panic-resolving bar is untestable), and **deeply negative VRP directly disqualifies any sell-front-month calendar** — selling premium into −60 to −83pp VRP is the exact error the 2026-06-06 P0.1 quote-cap leak punished (those leaked ≥0.80 quotes went 0-for-3). On these five, no `kink_candidate` cleared the 5% prominence threshold at all (all sub-threshold near-misses at the 2026-09-18 tenor, 0.0–11.4%), meaning the whole curve is **uniformly inverted** rather than event-humped — consistent with vol still catching up to a persistent high-RV regime rather than a single dated catalyst.
- **Single-contract IV outliers: none survive.** The cached `iv-outliers` set is **100% expiry-day 0DTE noise** — every row is the 2026-08-12 bucket on SLV/SPY/NVDA with `avg_iv` 2–38% but `max_iv` 97–777% (a handful of far-wing prints, not a mispricing). Unusable. Likewise the `iv-rank --mode high` top-25 is all `iv_rank == 100` and dominated by sub-$5 / illiquid / synthetic tickers (LCDL, TENX, ATRO1, SMU2, HOOX1, RIOX1, ABVEF, AZUL1, AVO1) — **none of the liquid AI-infra/semis names appear**, so it offers zero support for any "premium ripe to fade" read.

**The dispersion trade, and why it is not formally expressible.** Index vol is cheap-to-fair while single-name realised vol is enormous — but the *index leg is not rich enough to fund* a clean short-index-vol / long-single-name-vol variance structure (QQQ is itself PREMIUM_BUYING at −5.4pp; SPY is FAIR). So the defensible expression is **straight long premium on the extreme names**, not the formal dispersion structure. `multileg-strategist` screened specifically for institutions expressing this and found **no** dispersion-shaped ratio/diagonal pairing in today's single-name data — recorded as a negative result, not asserted.

**`iv-percentile-zscore` caveat:** requesting `--lookback-days 252` returned **`dates_used: 85` on every ticker** — below the 120-day first-class floor, so all percentiles and z-scores are **provisional**. With that caveat: all ten read `LOW_IV` regime at percentile 0–20, i.e. today's already-elevated absolute IV levels are still low relative to each name's *own* last-85-day range. Same story as VRP from a different angle.

**Earnings vol** (`earnings-scout`, 149 names in the next 14 days; six worked up in depth). None reached the confluence gate, so none is scored — all four live calls are in §6/§8:

| Ticker | Earnings | DTE | Raw → hygiene shape | Kink | front-end | Implied move | Term-skew 365d | Verdict |
|---|---|---|---|---|---|---|---|---|
| **TPR** | 08-13 pre | 1 | BACKWARDATION → BACKWARDATION (genuine monotonic panic, correctly not KINKED) | — | **1.575** (most extreme) | **8.44%** (trustworthy, 1-DTE) | COMPLACENT 1.016 (flat) | **CALENDAR** |
| **AMAT** | 08-13 post | 1 | BACKWARDATION → **KINKED** | dte37 (09-18), 21.9% — **does NOT match earnings, false positive** | 1.248 | 6.13% (trustworthy) | COMPLACENT 0.993 | **CALENDAR, reduced** |
| **LOW** | 08-19 pre | 7 | BACKWARDATION → **KINKED**, base → **CONTANGO** | **dte9 (08-21), 17.4%, 304 ct — 2d after earnings** | 1.368 | raw 1.68% **UNRELIABLE** → **~5.85%** recomputed | **TAIL_HEDGING 1.141 — the only back-month-confirmed stretch in the set** | **SELL VOL, best-confirmed** |
| **ROST** | 08-20 post | 8 | BACKWARDATION → **KINKED**, base → **CONTANGO** | **dte9 (08-21), 26.3%, 70 ct — day after earnings, and 08-21 is OPEX** | **1.803** | raw 1.22% **UNRELIABLE** → **~8.1%** | NORMAL 1.079 (partial only ⇒ size capped) | **SELL VOL, half** |
| OKTA | 08-26 post | 14 | BACKWARDATION → KINKED, base → CONTANGO | dte9 (08-21) — **this is OPEX, 5 days BEFORE earnings ⇒ false positive** | 1.396 (contaminated); clean earnings-tenor ~1.20 | raw 2.95% unreliable → ~19.6% | COMPLACENT 1.002 (flat) | **SKIP** |
| CRWD | 08-26 post | 14 | BACKWARDATION → BACKWARDATION (no flip, **no kink at all**) | none | **1.145** (lowest) | raw 2.92% unreliable → ~12.0% | COMPLACENT 1.002 | **SKIP** |

**New substrate defect worth registering:** `earnings-catalyst` / `earnings-play`'s `implied_move_perc` appears to price the **nearest calendar expiry, not the earnings-adjacent one**, for any name more than 2 days from its print. For 1-DTE names it matches a parametric ATM-straddle estimate within ~1–3pp (TPR 8.44%, AMAT 6.13%). For 7–14 DTE names it is **4–7× too low**: ROST raw 1.22% vs ~8.1% recomputed, LOW 1.68% vs ~5.85%, OKTA 2.95% vs ~19.6%, CRWD 2.92% vs ~12.0%.

**Vol-lane calibration reminder, applied:** `earnings_vol` caps at **0.55** and `high_iv_rank` at **0.60**; both then land in the anti-predictive [0.55, 0.65) band, so sizing floors at `starter`. Post-freeze `earnings_vol` realises **0.449 on n=78** — the most persistently over-claimed class in the book, surviving BH correction as a miscalibration for a 4th–5th consecutive audit. `earnings_vol` is also **not** among the 5 classes `signal-backtest` supports, so its win-rate can only ever be `NA(substrate)`. Nothing here is offered as high conviction.

**Data gap, not a finding:** `uw insights analyst-vs-flow` returned only an `options_flow` block for all six earnings names — no analyst-ratings data came back. That is a gap, **not** "no divergence." `term-skew` also failed the 365d target for TPR (*"insufficient call/put coverage"* — no liquid ~1y tenor), falling back to dte100/128.

---

## 6. Risk & Correlation

**Macro headline first:** mildly stagflationary — core PCE **3.29%** sticky-high, core CPI 2.79%, payrolls **−23k MoM**, unemployment 4.1%, 10Y **4.70% and rising** (+14bp/30d) with a **weakening USD** (term-premium repricing, not growth optimism), fed funds 3.63% leaving almost no real policy room, curve normal +0.48. Forward Tier-1 calendar in §1. CPI landed **today** and is already in this tape; the next binaries that fire the gate are **monthly OPEX 08-21 (T+7)** and **Core PCE 08-28/29 (T+12)**.

### Correlation — the single most important risk finding today

`uw risk portfolio-correlation` on today's candidates (not the static watchlist), 30d lookback. **Cluster `AI_infra_memory_cluster`**, mechanical threshold ≥0.70:

| Pair | corr | Class |
|---|---|---|
| NBIS / CRWV | **0.888** | cluster |
| EWY / CRWV | **0.778** | cluster |
| EWY / NBIS | **0.729** | cluster |
| NBIS / SMCI | **0.713** | cluster |
| CRWV / SMCI | 0.689 | soft watch — **no penalty** |
| EWY / SMCI | 0.569 | no flag |

All four longs form one connected component at ≥0.70. **META surfaced in zero pairs** — the one genuinely uncorrelated name on the board. Kept member is **EWY** on raw_score (3 > 2 = 2 > 1); NBIS, CRWV and SMCI each take −1 tier. The tool labels 0.713–0.778 "MODERATE" — **the tool's adjectives are not the gate**; the 2026-05-15 audit mechanized ≥0.70 precisely because discretionary reading fired at 0.631 in one case and not at 0.703 in another. No discretionary upgrades either: CRWV/SMCI at 0.689 stays soft-watch with **no** deduction, however obviously it is the same trade.

**Extending the run to the watch-only names changes how EWY must be read:**

| Pair | corr | | Pair | corr |
|---|---|---|---|---|
| MU / SNDK | 0.907 | | CRWV / IREN | 0.785 |
| **EWY / MU** | **0.905** | | EWY / CRWV | 0.778 |
| NBIS / CRWV | 0.888 | | SMCI / DELL | 0.760 |
| **EWY / SNDK** | **0.882** | | CRWV / SNDK | 0.758 |
| | | | **EWY / IREN** | **0.751** |

**EWY is the highest-correlated node to the memory complex in the entire universe** — 0.905 to MU and 0.882 to SNDK, *higher than its correlation to any of the three names it was supposedly diversifying against.* The "geographic read-through, one step removed from the underlying flow" framing is wrong in risk terms: **EWY is not a wrapper around a different bet, it is the memory bet with a Korean ticker.** Any book holding EWY alongside MU, SNDK, IREN, NBIS, CRWV, SMCI or DELL runs **one factor at 7× notional**, not seven positions. `sector_concentration: 100% in top sector` and the tool's own *"HIGH CORRELATION: some pairs move nearly in lockstep — not truly diversified"* both fire. EWY won the cluster on rank, **not** on being a different bet.

### Gates applied

**Panic gate** (`front-end-iv-ratio > 1.10`) fires on **3 of 5**: SMCI 1.106, NBIS 1.126, CRWV 1.141. META 0.732 CONTANGO does not fire. **DELL at 1.461** is the most extreme in the fleet and sits in watch-only. Two reads had to be fetched during the risk step because Phase 1 never produced them: **EWY `--near-dte 7` → ratio 1.056** (near_dte_actual 9, BACKWARDATION) — **below 1.10, so the panic gate does NOT fire on EWY**; the default `--near-dte 2` returns **4.45** on a 250.4% near-IV, which is exactly the expiry-day contamination the hygiene module drops. And **EWY VRP: IV30 51.78% vs realised 74.71% = −0.2292 PREMIUM_BUYING** — EWY had no VRP figure anywhere in the fleet, so that gate would otherwise have been *silently unevaluated on the only actionable name.*

**VRP gate** no-ops everywhere, with one flagged inconsistency: EWY's structure is net long premium ($17.46M debit vs $2.62M collected), aligned with negative VRP — but **the short 130P sub-leg is short vol in a negative-VRP regime**, internally inconsistent. Flagged, not deducted.

**Sector gate** fires −1 on NBIS/CRWV/SMCI (Technology netted OUT 3 consecutive sessions, DISAGREE-caveated, magnitude decelerating). It **no-ops on META** — outflow from a short's own sector is *favourable*, and the gate penalises adverse rotation only and can never upgrade. It was **declined on EWY**: attributing a software-distribution signal to a Korean memory ETF would contradict the fleet's own intra-Tech finding, since EWY's exposure is on the **inflow** (SMH) side.

**An asymmetry declared rather than hidden.** The Technology netted read is DISAGREE-flagged, which is enough to deny a sector-leader **+1** yet it is still applied as a **−1**. Gates are downgrade-only and the conservative direction is the permitted one, but this is the same rubric asymmetry the quant registered on META's net-vs-gross — and it is load-bearing on three rows. Both belong in the next audit's queue.

### Fundamentals verdicts

| Ticker | Verdict | tier_adj | Driver |
|---|---|---|---|
| EWY | CONFIRM | 0 | Korea/memory catalyst — **but see the correction below** |
| **NBIS** | **CAUTION** | **−1** | Insider MSPR **−73.42**, **all 5 reported months net-selling** while the stock ran $62.01 → $259.20; operating margin **−70.55%** behind a headline +93.09% net margin (non-operating one-off) |
| **CRWV** | **CAUTION** | **−1** | Insider MSPR **−58.28**, net-negative **17 of 20 months** (most persistent of the five); raw **D/E 6.4849** and **current ratio 0.4555** (current liabilities exceed current assets) on a GPU-datacentre capex book into a rising 10Y |
| SMCI | CONFIRM | 0 | $60B+ Q4 orders, book-to-bill >5×, FY2027 guidance $65–72B, D/E 0.755, current ratio 5.25 — **but see the ruling below** |
| META | CONFIRM (for the short) | 0 | Insider MSPR −55.84 / 18-of-20 months, −16.03% EPS miss, EPS growth −3.69% vs revenue +27.65% |

No VETOs today, so the `veto_fp_rate` monitor does not accrue.

**Two verdicts were materially undercut by the debate, and both corrections came from the bear pulling primary sources:**

**EWY's catalyst is a RUMOUR, not a filing.** The fundamentals gate recorded *"Temasek reported adding direct stakes in SK Hynix and Samsung."* The bear checked the sourcing: this is a same-day, **single-sourced** report (Asia Business Daily) that Temasek *"has recently decided to invest"* and is *"in contact with the Korean government to discuss the **timing** of the investment execution"* — and explicitly that **"Temasek has not announced an investment agreement with either chipmaker."** No agreed size, price or timeline. SK Hynix and Samsung ran 8%+ and EWY 5.16% **on an unconfirmed report of a potential future transaction.**

**SMCI's CONFIRM has an instrumentation blind spot, and the finding is serious.** The bear pulled the actual 2026-08-11 8-K. The $60B+ order figure is real and SEC-disclosed — but **Q4 FY26 preliminary revenue landed near the LOW END of the $11.0–12.5B guide**, so the +74.1% EPS surprise was a **margin-mix beat, not a volume beat**, in the same release that **doubled FY2027 gross-margin guidance from "8%+" to 15–17%**. Working capital is straining: cash conversion cycle **54 → 106 days** QoQ, days-inventory-outstanding **63 → 106**, and roughly **$6.6B of operating cash burned in a single quarter** versus $24M the prior quarter, against **$11.1B of inventory**. Current ratio 5.25 is a photograph; the cash-flow statement is the video. And there is a **live, unresolved March-2026 DOJ indictment alleging a $2.5B scheme to illegally divert AI servers to China** — two employees plus a contractor indicted, stock −33% on the news, independent board investigation ongoing, active securities-fraud class action — sitting directly under a growth story whose entire content is *"we are shipping tens of billions of dollars of AI servers,"* the exact product category of the indictment. Layered on the 2024 EY resignation (*"unwilling to be associated"* with management representations) and near-delisting.

`risk-monitor`'s ruling, stated plainly: **the fundamentals verdict stays CONFIRM with `tier_adjustment: 0`, and it is not rewritten.** Grading the underlying is the fundamentals gate's authority; silently substituting a different verdict would make the next audit's gate-effectiveness measurement score a verdict that gate never issued. **Separately, under the risk officer's own authority to refuse to size, SMCI is watch-only on the risk overlay regardless.** The real finding is instrumentation, not judgment: **a Finnhub-aggregate CONFIRM has no field for a live export-control indictment.** CONFIRM here means "nothing in the measured fields contradicts," not "clean." Wholly moot on sizing today (raw 1 / DROP / skip) — which is the right time to record a gap, before it costs anything.

### Debate disconfirmation — fires on 5 of 5

| Ticker | bull | bear | Verdict |
|---|---|---|---|
| EWY | 0.35 | 0.65 | −1 tier |
| NBIS | 0.25 | 0.85 | −1 tier |
| CRWV | **0.15** | 0.85 | −1 tier |
| SMCI | 0.25 | 0.75 | −1 tier |
| META | 0.35 | 0.65 | −1 tier (bull residual = confidence that *not* shorting is right) |

Round-2 escalation correctly not triggered (requires both ≥0.75 within one bin; every bull is ≤0.35). CRWV's bull at **0.15** sits exactly on the schema's new floor and is carried **verbatim, not clamped** — which is the entire reason the floor was lowered from 0.55. `BOTH_SIDES_LOW` applies nowhere: every bear cleared 0.55, so this is a clean unanimous bear sweep rather than the "neither advocate could make their case" signature.

**The material observation: the bulls did the disconfirming work themselves.** EWY's bull ran `uw oi position-rolls` (**0 detected**) and `biggest-increases`, and reported the reload was **partial and mixed** — only ~38% of closed call size and ~19% of closed put size came back on, with the put replacement tagged **BEARISH** (ask-side put *buying*) at a **more defensive strike, 130 → 150**; its verbatim conclusion was *"whatever this is, it is not accretion, and the +2 line's premise — that this structure was actively growing — does not survive contact with the OI data."* CRWV's bull ran the exculpatory mechanical-roll test it was asked to run and reported that it **failed**, finding put demand on the increase side: *"I went looking for exculpatory evidence and found the opposite."* SMCI's bull declined to defend a directional long at all. NBIS's and CRWV's bulls both abandoned the directional expression. **A 5-of-5 gate firing where the advocates self-refuted is a far stronger signal than five bears out-arguing five bulls.**

One place the bear **corrected the bull's own framing honestly** and it is worth recording: CRWV's "five-strike put wall" does **not** survive verification. `uw oi smart-positioning` shows the 56P dte23 (+12,906 ct) at `net_ask_bid −13,379` (bid 13,392 vs ask **13**) — a put **sold**, tagged bullish — as are 80P dte9, 70P dte2, 75P dte2, 88P dte2 and 87.5P dte128. Genuinely **bought**: 80P dte2 ($2.23M), 90P dte9 ($6.08M), 85P dte2 ($1.99M) ≈ **$10.3M bought against ~$11.2M sold — balanced, not a wall.** What survives is narrower and still real: the *bought* puts cluster at 80/85/90, **16–26% below spot**, at 2–9 DTE — real money paying for near-dated tail protection immediately into the euphoria — plus a **$6.75M ask-side put buy at K120 for 08-21** (a strike *above* spot, an ITM put bought outright, most plausibly a synthetic short or hedge overlay) against the $24.9M call-ask sweep at K100, roughly 3.7:1 rather than lopsided.

### Adverse flow / exit candidates

`conviction_2026-08-11` **exists** and contains **`["NBIS"]`**. `uw watchlist alerts` returns three: `VOLUME_SPIKE` medium (2.6× average options volume), `LARGE_DARK_POOL` **high** ($146,712,128 single trade, 9,444 total trades), `OI_SHIFT` medium (net OI +49,950 contracts). `uw watchlist scan`: `flow_direction: bullish`, `net_flow +$58,926,323`, close 259.20, PC 0.783, iv_rank 35.75, volume_ratio 2.58.

**No adverse flow reversal. NBIS is NOT an exit candidate on flow** — every alert is same-direction confirmation on a +34.14% day. **But the alert set is low-information and disagrees with the intent screen.** `OI_SHIFT: net OI increasing by 49,950` is *gross* OI growth, whereas `oi decrease-with-volume` on the same name and same session found **call-side closing dominance** (−3,861 ct / $14.07M calls vs −1,051 / $5.07M puts) plus a single-leg ticket at **size/OI 0.522**, the documented sub-0.5 closing anti-signal. Both are true: aggregate OI grew while the largest individual moves were call-side closes. **"No adverse alert" therefore does not mean "no adverse positioning"** — a flow-side analogue of the blindness the fz tripwire covers on the fundamentals side, worth registering.

`fz quote-drift NBIS --since 2026-08-11` returned **two moved fields, both mechanical and both non-adverse** — Enterprise Value 48.83B → 65.43B and Market Cap 48.63B → 65.23B, arithmetic on the +34.14% move. No short-float jump, no target-price cut, no recommendation deterioration. **Exit list: EMPTY.** `conviction_2026-08-11` left untouched.

### Breadth cross-check (advisory)

`fz breadth --group sector`: **261 advancers / 241 decliners / 1 unchanged of 503, `pct_green` 51.89%**, avg +0.20%, median +0.09%, top mover SMCI +19.02%, worst TPL −6.08%. **`divergence_flag: false`** — a green tape with `pct_green` > 50 is not the classic distribution signature. Advisory, 0 rubric points, and it does not change sizing. Two things it does say: the gains were **concentrated** (a +19% top mover against a +0.09% median), and price breadth **disagrees with flow breadth** (51.9% green vs 33.9% bullish flow) — different quantities, not conflated.

### Hedge sleeve — none, and the reason matters

**Net delta is zero. Buying protection against no exposure is not risk management, it is a naked long-vol punt financed by the hedge budget.** Declined rather than reflexively proposed.

Two notes for anyone carrying legacy AI-infra length from prior sessions (out of scope for this book; hedge legs, defined-risk spreads and short-vol structures all sit **outside** the short-routing rule — those are structure *uses*, not directional short expression):
1. **The instrument would be QQQ, not SPY and not VIX.** QQQ VRP is PREMIUM_BUYING (−0.0536) with rv20 24.4% — QQQ options are cheap relative to their own realised tape. SPY VRP is FAIR (−0.0028) with rv20 only 13.7%, so SPY puts are fairly priced *and* track the wrong thing. A defined-risk QQQ put vertical in a September expiry (past 08-21 OPEX) is the coherent expression.
2. **A VIX or SPY hedge would have paid nothing today, and that is the whole point of the tape.** The index was flat while NBIS ran +34%, CRWV +19%, SMCI +19% and META fell −3.38%. The rotation **nets to ~zero at the index level** — QQQ rv20 24.4% vs SPY 13.7% is exactly that dispersion signature. VIX at 14.55 makes a call ladder cheap in absolute terms, but a rotation-driven single-name drawdown that cancels at the index is the one risk a VIX or SPY hedge does not cover.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Empty. No name reached MEDIUM (raw ≥ 7).** The highest score on the board is 3.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`. From the most recent `/calibration-audit` (2026-08-08, `phase_3_calibration`):

| Tier | n | Realised WR | Mean realised P&L | Payoff ratio (avg win / \|avg loss\|) | Capped half-Kelly |
|---|---|---|---|---|---|
| HIGH | 7 | **0.143** | −2.441 | 0.72 | 0.0 |
| MEDIUM | 19 | 0.526 | **+0.104** | **0.948** | 0.0132 |
| LOW | 104 | 0.375 | −3.523 | 0.808 | 0.0 |
| DROP | 412 | **0.415** | −3.020 | 0.775 | 0.0 |

Tier monotonicity failed for a **6th consecutive cycle** — HIGH remains the worst tier in the corpus and DROP again beats LOW. **MEDIUM is the only tier with positive expectancy and the only one with a payoff ratio near 1.0.** The Kelly gate does not pass (n=27 < 30, and tier×expectancy is non-monotone), so the **win-rate ladder stays the live sizer** and the C3 fractional-Kelly sizer stays ADVISORY. Display-only context — but the point it makes is directly relevant today: a high hit-rate with a sub-1 payoff loses money, and every tier except MEDIUM has a payoff ratio below 0.81.

### The five scored calls (all below MEDIUM; recorded for the audit trail)

| Ticker | Dir | raw / tier | Σ components | Class | win_rate | market_excess | pre-risk | Fundamentals | bull / bear | Gates fired | **Final** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **EWY** | long | 3 / LOW | +2 multileg, +1 oi-trend | `multileg_directional` | `null` / `NA(substrate)` | `null` | starter | CONFIRM | 0.35 / 0.65 | event_risk −1, debate −1 | **`watch_only`** |
| **NBIS** | long | 2 / DROP | +1 vol-surface, +1 oi-trend | `event_vol` | `null` / `NA(substrate)` | `null` | skip | **CAUTION** | 0.25 / 0.85 | panic −1, cluster −1, sector −1, fundamentals −1, event −0.5, debate −1 | **`skip`** |
| **CRWV** | long | 2 / DROP | +1 vol-surface, +1 oi-trend | `event_vol` | `null` / `NA(substrate)` | `null` | skip | **CAUTION** | **0.15** / 0.85 | panic −1, cluster −1, sector −1, fundamentals −1, event −0.5, debate −1 | **`skip`** |
| **SMCI** | long | 1 / DROP | +1 vol-surface, +1 oi-trend, **−1 flow_conflict_lite** | `event_vol` | `null` / `NA(substrate)` | `null` | skip | CONFIRM | 0.25 / 0.75 | panic −1, cluster −1, sector −1, event −0.5, debate −1 | **`skip`** |
| **META** | **short** | −1 / DROP | +1 DEX flip, +1 oi-trend, **−3 flow_conflict** | `gamma_breakout` | `null` / `NA(substrate)` | `null` | skip | CONFIRM (short) | 0.35 / 0.65 | regime −1, debate −1, event −0.5, **SHORT ROUTING** | **`skip` → `watch_only`** |

**`market_excess` is `null` on all five — and the reason matters.** None of the five has a dominant class the backtest substrate supports (`multileg_directional`, `event_vol` and `gamma_breakout` are all outside the 5 supported classes), so every `win_rate` is `NA(substrate)` and no per-call excess can be computed. **No row gets a `beta` flag — not because none is beta, but because the substrate cannot say.** The relevant backdrop is class-level and unflattering: `bullish_flow` clean WR **0.4406** against a **0.5105** SPY benchmark (**−0.0699** excess, n=143). Four of five are longs.

**Class label note.** The three AI-infra rows are recorded in the envelope under the canonical **`event_vol`**, not the off-list `vol_long` the quant emitted (schema `x-canonical-classes`). `event_vol` is the accurate mapping: all three reported earnings on 2026-08-12, so both the BACKWARDATION shape and the inflated trailing RV30 that produce the negative VRP trace to an event that has **already fired**. Deliberately not `earnings_vol` (a pre-print setup) and not `high_iv_rank` (a persistent IV-percentile dislocation). Neither label is among the 5 backtest-supported classes, so `win_rate` stays `NA(substrate)` and no class ceiling binds — the relabel changes nothing mechanical, only groupability at the next audit.

**Union `|cum_flow_30d|` distribution used for the mechanical flow_conflict computation** (n=14, $M): `0.051, 0.363, 4.66, 5.76, 7.26, 70.93, 73.92, 100.17, 107.7, 168.54, 277.70, 303.35, 435.00, 1082.00` → **Q1 $6.13M · median $87.04M · Q3 $250.41M · 25%-of-median $21.76M.** Robustness without contaminated SNDK (n=13): Q1 $5.76M / median $73.92M / Q3 $168.54M — **every verdict identical under both.** The `trend_direction` label returned `MIXED` on 10 of 10 scored queries (13 of 14 overall), so the deduction was driven off the **numeric** branch; a label-driven `flow_conflict_lite` would have fired −1 on all five.

**Invalidation levels.** Only EWY has an actionable one: the **$161.21 shelf** (the 07-30 snapback low). Its own recent path is the reason — 07-24 close 162.96 → 07-28 151.45 → **07-29 144.21 (−11.5% in three sessions)** → **07-30 161.21 (+11.8% in one)** → 08-12 175.87, now **7.9% above its own pre-crash level**. A repeat of that 11.5% three-session drawdown from here lands in the mid-$150s; a full replay of the four-day round trip lands near **$146** — and the Oct16 structure is **short an uncapped put at 130** into a name that has just demonstrated that drawdown capacity. The other four are `skip`, so no level is defended.

### Full `gate_verdicts` — all 9 keys, EWY and META (the two `watch_only` rows)

**EWY**
```
regime:        no-op (TRANSITIONAL / trend UPTREND, SPY above both SMAs — no direction
               conflict for a long; the "half size" guidance is implemented by
               rubric_regime, not double-counted here)
vrp:           no-op (EWY VRP -0.2292 PREMIUM_BUYING, IV30 51.78% vs realised 74.71%;
               structure is net-LONG-premium $17.46M debit vs $2.62M collected = aligned.
               CAVEAT: the short 130P sub-leg is short vol in a negative-VRP regime —
               internally inconsistent, flagged not deducted)
panic:         no-op (front_iv_ratio 1.056 at --near-dte 7 / actual 9, below 1.10; the
               default --near-dte 2 reads 4.45 on a 250.4% 0DTE bucket = expiry-day
               contamination, rejected)
cluster:       no-op — KEPT MEMBER of AI_infra_memory_cluster on raw_score 3. Edges
               EWY/CRWV 0.778, EWY/NBIS 0.729. NB extended run: EWY/MU 0.905,
               EWY/SNDK 0.882, EWY/IREN 0.751 — kept on RANK, not on being a different bet
sector:        n/a (ETF, no GICS, gics_agreement n/a; economic exposure is Korean
               memory/semis = the INFLOW side of the intra-Tech split)
fundamentals:  no-op (CONFIRM, tier_adjustment 0). Catalyst materially corrected: the
               Temasek report is a same-day single-sourced RUMOUR of a POTENTIAL future
               transaction — "has NOT announced an investment agreement with either
               chipmaker" — no agreed size, price or timeline
event_risk:    -1 tier, stacked: -0.5 (monthly OPEX 2026-08-21 = T+7, held through)
               + -0.5 (Core PCE 2026-08-28/29 = T+12, inside the Oct16 65-DTE horizon).
               Undefined-risk qualifier MET: naked short 130P below 130, naked short call
               above ~210 on the Sep18 1:2 ratio. FOMC 2026-09-16 also in-horizon.
               PPI T+1 / Retail Sales T+2 / FOMC minutes T+5 = ambient, NOT fired.
               If re-expressed as defined risk, the exemption applies and this returns to
               no-op — the one gate here that is a function of STRUCTURE, not evidence
debate:        -1 tier (bear 0.65 >= bull 0.35)
rubric_regime: capped half (OUT-OF-REGIME; rubric 2026-06-12 fitted UPTREND, current
               TRANSITIONAL). NON-BINDING today — already at starter/skip
```

**META** — all 9 recorded, none omitted, despite the size override
```
regime:        -1 tier (trend UPTREND + SPY above both SMAs + 30d +2.75% vs SHORT.
               NB flow breadth is 2:1 BEARISH and META is today's sector laggard —
               the gate reads price/trend, mechanically)
vrp:           no-op (META VRP -0.2188 PREMIUM_BUYING, iv30 33.37% vs realised 55.25%;
               a directional short is not a short-vol structure, so no contradiction —
               puts are cheap, which favours a long-premium expression)
panic:         no-op (0.732 CONTANGO at --near-dte 7; 0.948 at near-dte 2 — CONTANGO on
               both. This is the bull's strongest unrefuted point: the vol market prices
               ZERO near-term stress against a supposedly fresh regime shift)
cluster:       no-op (zero pairs with any of EWY/NBIS/CRWV/SMCI — the one genuinely
               uncorrelated name on the board)
sector:        no-op (Comm Svcs netted OUT -$37.1M, 3-of-4 = FAVOURABLE to a short, not
               adverse; the gate penalises adverse rotation only and can never upgrade)
fundamentals:  no-op (CONFIRM-for-short, tier_adjustment 0; veto_for_short NOT met —
               insider signal is SELLING, MSPR -55.84, 18 of 20 months net-negative)
event_risk:    -0.5 (monthly OPEX 2026-08-21 = T+7, held through, undefined-risk short;
               the 9-DTE/08-21 bucket is the largest liquid bucket in the name at
               17,491 contracts / 54.69% IV). Own earnings 2026-10-27 = 76d, outside.
               MOOT — sizing already overridden by short routing
debate:        -1 tier (bear 0.65 >= bull 0.35)
rubric_regime: n/a (SHORT-ROUTED, sizing overridden); would have been "capped half
               (OUT-OF-REGIME)". Recorded, not omitted, for portfolio-risk visibility
```

NBIS, CRWV and SMCI carry the same 9 keys; their fired gates are in the table above and the DROP-floor verdict makes them moot.

### Instrumentation trio — status

`implied_move` is emitted on all three `event_vol` rows (NBIS 18.5%, CRWV 14.6%, SMCI 13.8%) but **all three are parametric proxies** (IV·√(DTE/365)), not quoted straddle mids — **the C42(b) IV-vs-RV blocker persists**; no scout quoted a real expected move. `dp_block_to_float_ratio` is `null` on all five (none is a `dark_pool_accumulation` row; the one name that was — ASTS at **0.00084** — failed the confluence gate). `insider_cluster_flag` is **`null`, not `false`**, on all five: the fz/accumulation lane never ran on these names, so **today adds nothing to C18's zero-variance problem.** ASTS's `false` is the only populated value and it sits in watch-only.

### Deep-dive hand-off

**Skipped — no HIGH-tier name.** Nothing to hand to `/stock-deep-dive`. Step 6.5 (`uw playbook batch-scan` on the raw ≥7 list) was also skipped for the same reason: the list is empty.

### Conviction-scoring rubric (frozen version `2026-06-12`), embedded verbatim

```
Daily conviction score = Σ:
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna-squeeze setup in trade
      direction — the trigger must be a verified SIGN CHANGE, not a level: sign(net_dex) on the
      latest session opposite to ≥3 consecutive prior sessions, read from dated `uw options-structure
      dex --date` calls, with |net_dex| on the flip day ≥ 0.25× the trailing-10-session median
      |net_dex|; the evidence string must cite both dated values. Compute with scripts/dex_flip.py —
      do NOT do the arithmetic by hand. Vanna disjunct additionally requires a dated VIX source.
      # DEMOTED +3→+1 and MECHANIZED 2026-06-12 audit P0.4
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified
      institutional-tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d
      confirms (sign aligned AND |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL ONLY:
      award only when dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +1  uw historical cumulative-premium-flow shows net directional accretion in trade direction
      (30d) — INTENT-SCREENED: award only when (a) no C28 distribution_flag on the name AND
      (b) on dividend payers inside an ex-div window, the accreting prints are NOT deep-ITM
      sub-parity calls. Screen failed or unevaluated on a flagged name → 0.
  # +2 line for uw insights signal-confluence ≥4 REMOVED 2026-06-12 audit P0.2
  # +1 line for uw hot-chains sweep-persistence top-5 REMOVED 2026-05-23 audit P0.3
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector —
      CONDITIONAL: award only when (a) sector persistence_score ≥ 0.6 AND (b) cum_premium_flow_30d
      direction aligned with thesis AND (c) |cum_flow_30d| ≥ $50M. Default 0.
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising uw historical pc-ratio-zscore
      (VRP positive)  # an INFORMED-FLOW CONTINUATION penalty, not "the crowd is wrong, fade it"
  -3  flow_conflict — applied mechanically when cum_premium_flow 30d direction is CLEARLY opposite
      dominant_signal_class (signed-sum sign flip + magnitude > today's union-median |cum_flow_30d|,
      or explicit OPPOSITE label)
  -1  flow_conflict_lite — when the 30d read is MIXED (signed sum near zero, or aligned but
      bottom-quartile magnitude in today's union). Mutually exclusive with -3: apply ONE, never both.
  # The two below are NOT score_components — they are risk-monitor TIER gates applied in Step 2d,
  # contribute 0 to raw_score, and never appear in score_components.
  -1  [TIER GATE, 2d] risk-monitor flags in correlation cluster (pairwise corr ≥ 0.70) — −1 TIER
  -3  [TIER GATE, 2d] uw risk market-regime conflicts with trade direction — −1 TIER (regime gate)
# Removed from swing/LEAP scoring 2026-05-09: gamma-flip-tracker 0DTE breakout setup (formerly +2).
# §2 is advisory / prose-only and contributes 0 points; next_session_gex is kept OUT of calls[].
```

**Tiers:** ≥9 HIGH (full size) · 7–8 MEDIUM (half) · 3–6 LOW (starter / watch-only) · ≤2 drop. **The cuts carry no validated ranking claim** — the ≥9 HIGH cut failed its scheduled re-confirmation on 2026-06-12 (HIGH realised 0.222 vs a claimed 0.774) and is retained only under the P0.1 freeze; the P0.6 out-of-regime guard caps all sizing at half in the interim.

---

## 8. Watch-only — single signal, no confluence

Surfaced by one Phase 1 agent but failed the ≥2-distinct-agent confluence gate. **Journaling only, not for entry today.**

| Ticker | Flagging agent | Dir | Note |
|---|---|---|---|
| **ASTS** | accumulation-hunter | long | The day's only accumulation flag, and **actively contradicted by leap-positioning-radar** (`COVERED_CALL` conf 26.7, call bid vol 50,632 > ask 37,646 = net call *selling*, capped upside). Accumulation evidence was genuinely clean: buy/sell 2.27, mega buy_ratio 1.00, `distribution_flag FALSE`, `dp_block_to_float_ratio` **0.00084**, `insider_cluster_flag` **false**, 30d +$100.17M (5.8% of gross), DP shelf **$74.31**, passed the closing-cross screen. fz: short_float 21.92%, days-to-cover 2.67, squeeze MODERATE, insider_trans −5.99%. Killed on structure, not on thinness. Full detail in §4. |
| **LOW** | earnings-scout | vol_short | SELL VOL, best-confirmed of the earnings set — the **only** back-month-confirmed stretch (`TAIL_HEDGING` 1.141). Kink at dte9 (08-21), prominence 17.4%, 304 contracts. front-end 1.368. Flow bullish +$469K, largest OI build (+5,386/−404). Reports 08-19, *after* Retail Sales resolves. |
| **ROST** | earnings-scout | vol_short | SELL VOL half. Kink at dte9 (08-21), prominence 26.3% — and 08-21 is **also monthly OPEX**, so gamma-pin mechanics layer on the event. front-end **1.803**. Back-skew only NORMAL (1.079) ⇒ size capped. |
| **TPR** | earnings-scout | vol_calendar | CALENDAR. Earnings 08-13 pre, same day as PPI + claims ⇒ macro beta stacks on the event. front-end **1.575** (most extreme). Implied move **8.44%** (trustworthy, 1-DTE). Entry ATM IV dte2 = 165.6%. Back-skew COMPLACENT ⇒ argues against SELL VOL sizing. −4.24% today. |
| **AMAT** | earnings-scout | vol_calendar | CALENDAR reduced. Earnings 08-13 post. Kink at dte37 (09-18) does **not** match the earnings date and has no identifiable catalyst ⇒ **false-positive kink**. front-end 1.248 (weakest of the two next-day reporters). Ripped +4.29% today against bearish flow ⇒ reads as protective-put buying into strength. |
| **SNDK** | vol-surface-scout | vol_long | BUY VOL, VRP −61.8pp. **CONTAMINATED:** 30d cum-flow +$1.08B is **2.08% of $52.11B gross** — a 2% imbalance is churn, and it is the exact field the 2026-08-06 put-sale-netting artifact corrupts. Cum-flow line correctly withheld. Excluded by leap-radar on two independent grounds. |
| **IREN** | vol-surface-scout | vol_long | BUY VOL, VRP −56.7pp. front-end **0.994 FLAT** — the one cluster name where near/far are level despite base BACKWARDATION (inversion sits beyond 9 DTE). GICS tag **miscoded** as Financial Services (it is an AI-infra/datacentre operator); 30d −$70.9M MIXED ⇒ fails the sector-leader gate. |
| **MU** | vol-surface-scout | vol_long | BUY VOL back-month past the OPEX bump. VRP −35.5pp. Kink at dte9 (08-21 OPEX, prominence 26.3% — largest of the batch) + secondary at dte44. **No MU earnings in the 149-name catalyst list** ⇒ pure OPEX/macro kink. **Four agents touched MU and none will carry a directional thesis.** |
| **DELL** | dealer-positioning | long | LONG-leaning medium. DEX fresh high +$3.60B on a +9.87% day; `dex_flip qualifies=FALSE` (stale 07-29/30 flip). front-end **1.461 — by far the most extreme front-panic print in the fleet.** GEX series 07-24→08-04 is the ZGL-grid artifact at its worst (ZGL $69–528 vs a $380–480 spot, 7 flagged flips); settled POSITIVE since 08-04 is the trustworthy tail. |
| **NVDA** | sector-rotation | long | Instrument context only. 30d +$303.3M — aligned and clears $50M, but GICS Tech is `watch_only` so it cannot carry the sector-leader +1. `sweep-tracker` bearish 5/5 on $3.42B, demoted to a hedge-flow footnote; closed +3.03%. accumulation-hunter did not flag it. |
| **MRVL** | single-leg advisory + contrarian (aborted) | short | The day's **only** Tier-1 `OPENING_PUT_PRIME`: put K215, exp 2026-09-11, DTE 30, **size/OI 5.989**, ask side, $1,028,752, `CONTRARIAN_SHORT`. **Advisory, 0 rubric points permanently** (C19 CLOSED as REFUTED 2026-07-25, register C53). contrarian-scanner found a real price-vs-flow divergence (price −20.2% over the window with net **bullish** flow +$5.2M) but **aborted** on BACKWARDATION with a kink at 16DTE/Aug-28 (97.1% vs 81.6% at 9DTE, 92.1% at 23DTE) = **event risk, not crowding**. pc_z −0.09 NORMAL. |
| **AVGO** | single-leg advisory + contrarian (aborted) | short | Tier-2 `OPENING_PUT_STRONG`: put K345, DTE 44, size/OI **9.942**, $1,292,000. Real divergence (price +12.6% with net **bearish** flow −$5.5M) but **aborted** on BACKWARDATION with a Sep-18 kink (37DTE, 66.9% vs 51.8% at 30DTE) consistent with an earnings-bearing expiry. pc_z +0.42 NORMAL. |
| **COHR** | contrarian (aborted) | short | Aborted. 2DTE avg_iv **175.9%** decaying to 91% by 30DTE; +8.24% today reads post-catalyst, not fresh crowding. pc_z −0.81 NORMAL. Also on the confluence-bearish screen at score 4. |
| **MSFT / PLTR / DDOG / APP** | sector-rotation | short | Software-distribution `watch_only`. PLTR is genuinely contradictory — DEX decaying 4 sessions while `sweep-tracker` reads it **bullish** 4/5 on $1.12B, and its raw CONTANGO flipped hard to hygiene KINKED / base BACKWARDATION (the largest raw-to-hygiene divergence in the set). APP 5d **−27.30%**. |
| **GLD** | sweep-tracker | long | Bullish 3/5, $793M — the only non-equity persistence and the only one outside the rotation story. Note the cross-current: **GDX** was disqualified by accumulation-hunter on 30d cum-flow **−$107.7M** plus `distribution_flag TRUE` (`GDX260918C00090000`, −1,794 ct on $2.99M), and ranked **last of 21 ETFs** at −$46.5M with calls sold at the bid. **Bullion bid vs miner distribution.** |

### Disqualified by their own flagging agent (recorded so the reasoning is not lost)

- **GDX** — genuine **two-signal contradiction**. Intraday DP was clean (ACCUMULATION 1.74×, mega 86.2% buy across 6 trades spread $90.96–91.76 through the regular session, passes the closing-cross screen) but 30d cum-flow is **BEARISH −$107.7M** and `distribution_flag` is **TRUE**.
- **WEC** — **closing-cross artifact.** Loudest accumulation ratio of the day (8.36× buy/sell) but **~64% of total DP volume ($102M of $154M) executed at the identical price $109.11**, clustered 20:00:13Z–21:05:12Z, with an anomalously wide NBBO (bid 106.93 / ask 111.27) = stale-quote reporting, the textbook benchmark/rebalance signature.
- **MPC** — mega tier is **one trade** ($155.1M, 445,393 sh) at 22:15:53Z after hours = **59% of the day's entire DP premium from a single ticket**, on a name already +31.48% over 30d with RSI 72.97.
- **ALB** — "mega tier" is literally **one parent order split into two identical prints** (129.36, 85,300 sh, one second apart at 17:17:17Z/17:17:18Z) = $22M from one parent.
- **ARMK** — `highest_tier = block` (no mega print at all), top trades clustered 20:47Z–21:26Z at the identical price 60.35 — the same late-clustering signature as WEC.
- **KKR / ETN / UNP / TLT** — `institutional-accumulation` returned **NEUTRAL** for all four despite decent block-tier premium ($35.4M / $26.0M / $19.7M / $57.9M). ETN and UNP sit in **Industrials, the #1 netted sector inflow** — worth a next-session look, but today's DP read does not clear the bar.
- **THC / GXO / MTCH / ACHC / ABCL / APLD / LLY** — weak, negative or absent institutional tier. **LLY** mega buy_ratio 0.327 (sell-dominated); **APLD** block buy_ratio 0.191 (sell-dominated — actually reads as *distribution*); GXO/ACHC zero mega+block; THC/MTCH/ABCL too thin (≤7 trades, block-tier only, sub-$20M).
- **SPX financing ladder** — excluded as structure, not conviction, and this is the day's most important artifact call. `multileg-strategist` identified a **multi-tenor risk-reversal / synthetic-long-forward financing ladder**: same-timestamp pairs across six expiries (Aug21/Sep18/Oct16/Nov20/Dec18/Jan27), long the 7000 call (delta 0.84–0.99) against short the 8000/9000 put (delta −0.56 to −0.95), identical sizes per tenor (Dec18: 10,700 × 7000C ask / 10,700 × 8000P bid). **Net per-unit delta ≈ 1.42 — both legs add long delta, so it is NOT a collar**; most consistent with a structured-note/dealer financing book or an index-arb overlay. Confirmed present on **08-10, 08-11 AND 08-12** = a three-day-old **standing programme**, which *reduces* rather than raises its value as new information. A naive scanner reading the raw **$977M / $392M (printed twice) / $368M** premiums as "massively bullish institutional flow" would be wrong on **both** magnitude (delta-heavy, not fresh directional) and novelty.
- **SPY put ladder** — six strikes (400/470/520/570/640/670P) × Oct30/Nov20, `multileg_ratio` 0.90–1.00, round lots (150,003 / 150,000 / 75,000×4), **no match on 08-10/08-11** ⇒ single-day systematic portfolio-insurance overlay.
- **ORCL** — `multileg_ratio` 0.346, i.e. **65% of the volume at that strike/expiry is single-leg**; no paired strike; BACKWARDATION but smooth with no kink ⇒ structure not cleanly inferable.
- **MSTR** — the 105C print is small and unpaired; the **real** story is a single-leg OI build at `MSTR261016C00095000` (**OI diff 44,254**, `net_ask_bid` 44,183 ≈ 100% ask-side opening, near-ATM, 65 DTE), an order of magnitude larger. Also KINKED at Dec18 (106.5% vs 78.4%/93.1%) on a thin 718 contracts.
- **MU 550P "calendar"** — dealer-hedge-shaped: premium per contract ~$2.63 and ~$7.86 (≈$0.03–0.08/share) at a strike ~40% below a $920+ spot with 2–9 DTE. High volume, trivial premium = cheap tail-hedge lottery tickets, not conviction.

---

## Appendix — substrate defects found this run

Recorded for `/calibration-audit`. Two are candidates for **P0**.

1. **`uw historical oi-trend` is provably broken, not merely uninformative — and it is currently load-bearing.** `consecutive_build_days == days_analyzed == 86` for SMCI, NBIS, META **and** CRWV, i.e. the tool claims OI built on every one of 86 consecutive trading days, which is mechanically impossible across two monthly expiries. `overall_trend: BUILDING` fired **5-of-5**. It is also **direction-blind** (`total_net_oi_change` is gross OI growth), so it awarded the same +1 to one short and four longs. Strictly worse than the registered 6-of-6 and 16-of-16 C47 cases because those were short windows. **Counterfactual: strip this line and EWY 3→2, NBIS 2→1, CRWV 2→1, SMCI 1→0, META −1→−2 — the board goes from one LOW name to completely empty.** The single actionable row on this board rests on a line that is demonstrably not measuring what it claims.
2. **Rubric asymmetry, mega-cap net-vs-gross — now load-bearing on four rows.** C11 imposes a 5%-of-gross scale-relative floor so a mega-cap's small net imbalance cannot *confirm* a +3. There is **no mirror on `flow_conflict`**: META's +$435M is **2.19% of $19.863B gross** — by C11's own logic, noise — yet it is penalised **−3**, which is what sets its tier. The 90d (−$283.7M) is **0.51% of $55.245B gross** and both windows carry the tool's own `MIXED` label. **The bear independently confirmed and accepted this rather than fighting it**, noting that stripping the line puts META at raw **+2** (or +1 without the degenerate oi-trend line). Neither the quant nor risk-monitor acted, because importing the floor would *loosen* a penalty — not downgrade-only, not freeze-safe. The same asymmetry recurs as the −1 sector cut on three Tech names off a DISAGREE-flagged read. **Registering, not acting** — but a rubric that treats a 2% mega-cap imbalance as noise when it would help and as conviction when it hurts is a real defect.
3. **`earnings-catalyst` / `earnings-play` `implied_move_perc` prices the wrong expiry** for any name >2 days from its print — the nearest *calendar* expiry, not the earnings-adjacent one. Accurate at 1 DTE (TPR 8.44%, AMAT 6.13%, both within ~1–3pp of a parametric check); **4–7× too low** at 7–14 DTE (ROST 1.22% vs ~8.1%, LOW 1.68% vs ~5.85%, OKTA 2.95% vs ~19.6%, CRWD 2.92% vs ~12.0%).
4. **Degenerate market-excess benchmark for non-directional classes.** The benchmark is "did SPY move >2% in 5 days" (0.2704 / 0.2890), which is ~never true, while a high-IV single name obviously moves >2%. So `volume_spike` books +0.2516 and `high_iv_rank` +0.5202 "excess" **mechanically**. Same denominator family as C49. Non-directional excess should be benchmarked against SPY **realised vol**, not move-frequency.
5. **`dark_pool_accumulation` returns an EMPTY backtest class** (`total_signals: 0`). The rubric's headline **+3 conjunction line has no backtest substrate at all** — directly relevant to the pre-registered DP-conjunction backtest (2026-06-12 P1.4). It cannot be graded from this tool.
6. **The ZGL-grid artifact has spread well beyond SPY/QQQ/IWM/MU** — implausible single-day `zero_gamma_level` prices across nearly every name in `gex-time-series` (MU $10–70 vs a ~$860–920 spot; QQQ a stray 249.5 among ~700–770; DELL $69–528 vs a $380–480 spot with 7 flagged flips 07-24→08-04; META wild single-day swings). SPY separately spiked to 789.87 on 08-11 with `total_gex` collapsing to $209M. The `regime` label and `total_gex` sign/magnitude remain trustworthy; the raw ZGL **price** does not.
7. **`iv-percentile-zscore --lookback-days 252` returned `dates_used: 85` on every ticker** — worse than the ~81 previously recorded, and below the 120-day first-class floor. All percentiles/z-scores are **provisional**.
8. **`cumulative-premium-flow` `trend_direction` returned `MIXED` on 10 of 10 scored queries** (13 of 14 overall; ASTS the lone `BULLISH`). The label carries no information today; a label-driven `flow_conflict_lite` would have fired on all five names.
9. **Zero-discrimination, recurring (C47 family):** sector `persistence_score == 1` and `trend == INFLOW` for **all 11 sectors** — including the three that are netted-OUT. Separately `consecutive_build_days: 5` fired 6-of-6 on the accumulation lane's checked tickers.
10. **`uw historical pc-ratio-zscore` still has no `--date` flag** ⇒ the "rising z" clause of the −2 overcrowded-long line remains **literally unsatisfiable**. Confirmed again.
11. **`uw insights institutional-accumulation` has no `--days` flag** (confirmed via `--help`) — single-day only. The command text's "5-day window" / "10-day window" phrasing is a fiction parameter.
12. **Raw `uw options-flow sweeps --date 2026-08-12` returned 100% SPX index structuring — zero single-name rows.** The day's directional single-name sweep tape is effectively unavailable from that endpoint. `sweep-ratio` and `smart-money-flow` were likewise saturated with 0DTE/ETF/micro-cap noise.
13. **`uw options-flow iv-outliers` is 100% expiry-day noise**, and **`uw screener iv-rank --mode high`** top-25 is all `iv_rank == 100` on sub-$5 / illiquid / synthetic tickers. Both unusable today.
14. **`uw insights analyst-vs-flow` returned only an `options_flow` block** for all six earnings names — a **data gap**, not a "no divergence" finding.
15. **The watchlist alert surface is blind to closing-side positioning.** `OI_SHIFT: net OI increasing by 49,950` on NBIS is gross OI growth, while `oi decrease-with-volume` on the same name and session shows call-side closing dominance. **"No adverse alert" ≠ "no adverse positioning"** — a flow-side analogue of the fz fundamentals tripwire.
16. **`fz` doubled-first-letter bug present on every surface** (`AAPLD`→APLD, `EETN`→ETN, `PP`→P, `CCAKE`→CAKE, `AAI`→AI, `MMETA`→META). De-doubled before use. The squeeze screen additionally returned an **alphabetical A-only slice of 20 rows** (throughput-limited, not a ranked squeeze list). All fz lanes advisory, 0 rubric points.
17. **`term-skew` failed the 365d target for TPR** (*"insufficient call/put coverage"* — no liquid ~1y tenor), falling back to dte100/128.
18. **Expiry-day term-structure contamination is at maximum today** — 5 of 10 raw labels flipped for `vol-surface-scout`, 4 of 6 for `earnings-scout`, with 3 of 10 and 3 of 6 also flipping at the monotonic base-curve level. The hygiene module is doing real work; raw labels are near-worthless on an expiry day.
