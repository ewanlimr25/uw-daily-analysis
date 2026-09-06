# Daily Market Analysis — 2026-08-07

## Executive Summary

- **Regime + GEX state:** **TRANSITIONAL** (trend UPTREND). SPY 773.26 (+0.61%, above both 20/50 SMA), QQQ 723.03 (+1.17%), IWM 301.56 (+1.11%), RSP 220.09 (+0.69%) — a genuinely **broad** advance, equal-weight participating, not a cap-weighted trap. SOXX +2.02% leads; XLE (−1.13%) is the only sector down. Both SPY and QQQ sit in **POSITIVE (long) gamma with spot pinned essentially on the ZGL** (SPY 772.84 vs 772.36; QQQ 722.39 vs 721.08), but both flipped regime *today* after 2–3 sessions of whipsaw. **VIX 14.9.** Sector lean: netted flow into Technology (+$110.4M) and Industrials (+$79.5M), out of Consumer Cyclical (−$30.8M) and Communication Services (−$18.9M).
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** SPY — long-gamma · ZGL 772.36 (reliable) · call wall **775** (2.4pts up) / put wall **755** (17.8pts down) · *asymmetric pin: tight cap, wide floor — skew the structure to the call side.* QQQ — long-gamma · ZGL 721.08 (reliable) · call wall **730** / put wall **715** · *symmetric ~1% box, standard iron fly.* Advisory, see §2.
- **Top swing build:** **NONE.** The conviction book is empty — all six confluence-gate passers scored below the LOW cut (raw range −1 to 2, drop floor is ≤2). Top raw_score is 2 (MU, AMD).
- **Top LEAP candidate:** **NONE.** `leap-positioning-radar` returned an empty book — every DTE>180 candidate failed Gate 4 (cumulative-premium-flow), a hard disqualifier. LEAP share of volume was only 3.0%.
- **Biggest risk:** The one cluster that would have mattered — **`AI_semis_optics` (MU / AMD / LITE, pairwise corr 0.82–0.86)** — is three of the six candidates, i.e. half the board was one position. With nothing sized, the live risk is **CPI on 2026-08-12 (T+3)** against a stagflationary print stack (core PCE 3.29% sticky, payrolls −23k, 10Y 4.69% rising). No hedge sleeve is mandatory (net delta zero); optional starter-size QQQ long-vol convexity is cheap here (VIX 14.9, QQQ VRP PREMIUM_BUYING).

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** `TRANSITIONAL — Mixed signals, reduce position size, wait for clarity`, trend **UPTREND**. SPY 773.26, above 20SMA (750.17) and 50SMA (747.19), +2.87% over 30d, −0.46% from the 90-day high. Guidance: *"Half position sizes. Favor defined-risk strategies. Iron condors in range."*

**The breadth story is the day's most important tell, and it is two-sided.** Price breadth is unambiguously healthy — `fz` reports 321 advancers / 180 decliners, **63.8% green**, avg +0.70%, and the OHLC confirms it (RSP +0.69% ≈ SPY +0.61%, IWM +1.11% leading). There is **no distribution divergence** in price. But UW's own *options-flow* breadth is only **37.7% bullish** (2,368 bullish vs 3,913 bearish tickers), and the index tape is net-bearish on premium (SPY −$135.6M, QQQ −$26.0M). Those two series measure different things — price breadth vs options-flow breadth — and the gap between them is the read: **price is rising on put-heavy options positioning three sessions before CPI.** That is consistent with hedged participation, not conviction buying.

### Per-index gamma table (current-state EOD book)

| Index | Spot | Zero-gamma | ZGL reliable | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|---|
| SPY | 772.84 | 772.36 | **yes** (0.06% from spot) | +$1.852B | POSITIVE | 775 (+0.3%) | 755 (−2.3%) |
| QQQ | 722.39 | 721.08 | **yes** (0.18% from spot) | +$853.5M | POSITIVE | 730 (+1.05%) | 715 (−1.02%) |
| IWM | — | — | — | — | — | — | — |

IWM is deliberately out of scope for the §2 read (SPY/QQQ only). `dealer-positioning-strategist` covers IWM on the swing horizon in §2a: DEX +$8.3B POSITIVE, one ZGL regime flip in-window (08-04), and a raw trajectory that whipsaws almost daily — low-confidence ZGL, no swing thesis.

**`uw options-flow dte-volume-share`:** 0DTE **46.4%** · weeklies 21.1% · monthlies 20.9% · LEAPs **3.0%**. `regime_hint: RETAIL_DRIVEN`. This is MARKET-level only (`symbol: MARKET`) — not a per-sector split. Effect: a uniform conviction haircut on every rotation and directional call, and a warning that a large share of today's "sweeps" are retail 0DTE churn rather than institutional urgency.

**`uw historical vrp`:** SPY **−0.0073 / FAIR** (iv30d 12.72% vs realised 13.45%) — no VRP edge either way. QQQ **−0.0536 / PREMIUM_BUYING** (iv30d 20.44% vs realised 25.79%) — vol is cheap versus realised. The tape favours **buying** premium, not selling it, which is why the contrarian book is empty (see §3b) and the vol lane leans long-vega (§5).

**Macro backdrop** (`scripts/fred_macro.py`): yield curve **normal** at +46bp (10Y 4.69% / 2Y 4.25%), core CPI **2.81%** YoY but core PCE **3.29%** YoY — inflation not beaten. Unemployment 4.1% with payrolls **−23k MoM (contracting)**. 10Y **rising** (+14bp over 30d), USD **weakening**, fed funds 3.63%. This is a stagflationary tilt: sticky prices, cracking labour, rising long rates. The weakening dollar is the cleanest explanation for the gold-miner bid (GDX +7.11% today, +21.31% over 5d).

**Forward `event_risk` (next ~10 trading days):**

| Event | Date | Impact | Note |
|---|---|---|---|
| **CPI (July)** | **2026-08-12** | **HIGH** | **T+3.** Inside any swing horizon opened today. Confirmed BLS 8:30 ET. |
| PPI (July) | 2026-08-13 | MEDIUM | Expected on the standard day-after-CPI cadence; date not independently confirmed. |
| Initial jobless claims | 2026-08-13 | MEDIUM | Elevated importance with payrolls at −23k. |
| Retail sales (July) | 2026-08-14 | MEDIUM | Approximate — mid-month Census cadence. |
| Initial jobless claims | 2026-08-20 | MEDIUM | Weekly. |
| Core PCE (July) | 2026-08-28 | HIGH | Outside the 10-day window; relevant to 3wk+ horizons. **Two vol-surface kinks land here.** |
| FOMC + SEP | 2026-09-15 | HIGH | Outside the window; LEAP/multi-week only. |

Per-name earnings inside the window: **LITE 2026-08-11 postmarket (T+2, confirmed)**, COHR 2026-08-12, NBIS 2026-08-12. All others (MU 09-21, TSLA 10-20, MSTR 10-28, PLTR 11-02, AMD 11-02) are outside.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — open interest that persists overnight — read forward as the *prior* for the next session's open. It is **prose-only, contributes 0 points** to the conviction rubric, and makes **no backtested predictive claim**. Predictive validation lives in `/weekly-analysis`'s rolling §2 backtest.

### SPY — long gamma, asymmetric walls

Spot 772.84 · **ZGL 772.36 (reliable, 0.06% away)** · **POSITIVE**, total GEX +$1.852B · call wall **775** (+$478.4M) · put wall **755** (−$33.1M).

Spot is sitting almost exactly on the ZGL inside a positive-but-thin regime — dealers are long gamma by a hair. Structurally that is a mean-revert / pin bias, but **the wall geometry is lopsided**: the call wall is 2.4pts (0.3%) away while the put wall is 17.8pts (2.3%) away. Strike 773 carries the single largest print (+$626.9M) but sits at-the-money, so it reads as the pin centre rather than the wall. Expect pokes above ~775 to be faded hard while downside has real room before dealer support engages at 755.

**Structure bias:** an asymmetric pin, not a symmetric box — **skew to the call side**. Short call spread or a call-side-tight iron fly with the put wing wide or skipped, rather than a symmetric condor.

### QQQ — long gamma, symmetric box

Spot 722.39 · **ZGL 721.08 (reliable, 0.18% away)** · **POSITIVE**, total GEX +$853.5M · call wall **730** (+$111.2M) · put wall **715** (−$18.1M).

Spot just above ZGL in a comparably thin positive regime, but the geometry is far more symmetric — walls roughly equidistant at ~1% each side, with the 723–725 cluster ($59–81M each) reinforcing the pin zone. Classic long-gamma box, mean-revert / range-bound between 715–730.

**Structure bias:** standard iron fly or condor centred 722–723, shorts toward the 715/730 wings.

**Regime freshness — read this before trusting either map.** Both indices flipped regime **today**. SPY ran POSITIVE (08-04) → NEGATIVE (08-05) → NEGATIVE (08-06, with a garbage extrapolated ZGL of 814.6) → POSITIVE (08-07). QQQ ran POSITIVE (08-03/04/05, with 08-05's ZGL of 249.5 a clear extrapolation artifact) → NEGATIVE (08-06, ZGL 749.31, >3.5% from spot, unreliable) → POSITIVE (08-07). Three regime labels in four sessions on QQQ, two of them carrying unreliable ZGLs. Today's read is the cleanest point in the series but it is **a fresh flip sitting on the line, not a settled multi-day regime.** Confidence should be materially lower than for a regime held 3+ clean sessions.

**Mandatory caveats:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes of Monday's session and re-computes the ZGL and walls.
- **ZGL reliability.** Both are reliable today (within 0.2% of spot). Note that three of the last four sessions produced extrapolated/garbage ZGLs on one index or the other — this field fails silently and often.
- **Gap risk voids the prior.** No Tier-1 event sits between the close and Monday's open, but **CPI on 08-12 is three sessions out** and can gap spot through these walls before any hedging mechanic engages.
- **Tooling limit.** `uw options-structure gex --dte-max 1` errors — this is the standing **0–45 DTE** book used as the best available proxy, not the isolated D+1 expiry.
- **ETF book**, not the cleaner SPX/NDX index book.

*Context check (from the cached expiry heatmap, not re-fetched):* near-dated concentration is genuine, not a thin-book artifact — SPY 2026-08-14 carries $3.05B total premium, 08-10 $1.40B, and CPI-day 08-12 $387M.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py`)

The walls above are a **map**, not a pin — wall-as-magnet backtested NO_GO, as did every directional 0DTE signal. What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, and **not a guaranteed edge** — the validation sample contains no vol shock, so the short-vol left tail is unsampled.

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` / VIX | **LOW** / 14.9 | **LOW** / 14.9 |
| `implied_move_pct` | 0.45% | 0.77% |
| `expected_range_pct` | 0.83% | 1.45% |
| `size_scalar` | **0.5** | **0.5** |
| Structure | iron fly / short straddle @ **772.89**, wings ±0.83% | iron fly / short straddle @ **722.68**, wings ±1.45% |
| `backtest.verdict` | GO_PREMIUM_SELL_INTRADAY | GO_PREMIUM_SELL_INTRADAY |
| Win rate (open entry) | 88.3% | 85.0% |
| `mean_pnl_open_pct` (**gross**) | +0.223% | +0.360% |
| **`mean_pnl_open_net_pct`** | **+0.123%** | **+0.260%** |
| Worst day (open entry) | −1.40% | −2.45% |
| `stand_aside_reason` | null | null |

**Lead with net, and read the basis correctly.** `pnl_basis` is *percent-of-underlying-spot-notional, GROSS* — it is **not** premium-collected and **not** margin-relative. SPY's net +0.123%/day is tiny in absolute terms, and Vilkov (2024) found an unconditional 0DTE condor flips to negative net Sharpe once costs are charged. The 88.3% gross win rate overstates a negatively-skewed seller's edge.

**The binding caveat today: `vol_state` is LOW, and LOW is exactly where this edge is thinnest.** `mean_pnl_by_vix_state` shows SPY **LOW = −0.059%** (negative), MID +0.414%, HIGH +0.315%; QQQ LOW +0.016% (≈flat), MID +0.574%, HIGH +0.489%. VIX at 14.9 sits below the lower tercile bound (16.4). The `size_scalar` of 0.5 already reflects that — but honestly read, **this is a near-stand-aside day for the premium-selling lane**, not a green light. GEX supports it (both indices long-gamma, quieter expected range) and VRP argues against it (both negative — you would be selling cheap vol). Those conflict; the VIX-tercile evidence breaks the tie toward standing aside.

**Entry rule:** enter at/after the open once the overnight gap resolves; if it gaps beyond the wings, stand aside. Hold to the close — **never carry overnight** (overnight entry backtested negative: SPY +0.017%, QQQ **−0.092%**). **Direction: none.** SPY ≈ SPX (validated identical); **QQQ is the weaker of the two** (Nasdaq index book unavailable) — flag its lower confidence.

**Promotion bar:** this lane stays advisory / 0 rubric points **permanently** until BOTH a vol-shock day enters the sample AND net expectancy clears a tail-aware bar. Win-rate is explicitly not the promotion metric.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

**One name in the entire fleet cleared the mechanized DEX-flip bar: TSLA.** Everything else is a DEX *level* — mostly positive, mostly call-heavy, all consistent with the broad up-tape — which is precisely the beta artifact the 2026-06-12 P0.4 mechanization exists to reject.

**Tested (14):** SPY, QQQ, IWM, TSLA, NVDA, MU, MRVL, TSM, AMD, META, UBER, MSTR, LITE, PLTR — 12 dated `dex` pulls each (07-23 → 08-07) run through `scripts/dex_flip.py`. **Skipped:** MSFT (small net-premium footprint), SNDK (standing put-sale-netting flag makes the DEX read unreliable).

**Dated VIX series** (Yahoo chart API ^VIX, the only source permitted for the falling-VIX leg): 08-03 15.86 → 08-04 16.50 → 08-05 15.81 → 08-06 15.15 → 08-07 14.90 — **three consecutive falling sessions.**

### TSLA — the only mechanized +1

`scripts/dex_flip.py` verdict `qualifies=true, direction=long`. Verbatim evidence: *"TSLA net_dex 2026-08-06 −2,823,223,741 → 2026-08-07 +1,037,118,716; prior 3 sessions (2026-08-04 −18,316,592, 2026-08-05 −1,973,053,980, 2026-08-06 −2,823,223,741) all negative; |flip| 1,037,118,716 vs floor 652,716,891 (0.25× trailing-10 median 2,610,867,564)"*. `magnitude_ratio` 1.59.

**Vanna-squeeze flag TRUE** — net_vanna +9,526 (put-heavy: put +29,678 vs call −20,152) plus the dated three-session VIX decline. Charm +422,189 (positive). GEX regime stable POSITIVE for six straight sessions, with total_gex on the flip day $195.2M vs $67.8M on 08-06 — roughly 3× reaccelerating. Per-strike GEX confirms it is not a single-strike artifact (largest strike $330 is 44% of total, with real distribution 320–350 against spot 328.19). `front-end-iv-ratio(7)` 1.006 FLAT — no panic, meaning the squeeze reads as *building*, not maturing.

**Honest caveats, both material.** (1) `sign_changes_in_window=3` — `whipsaw_warning` is FALSE only because it fires at >3. The full 12-day series ran negative for seven straight sessions (07-23→07-31), flipped positive 08-03, went negative again 08-04–08-06, then positive a **second** time on 08-07. Real, but noisy — not textbook. (2) The +1 line is a *demoted* line (was +3) with no peer-reviewed support for DEX/vanna flips as 1–4wk directional signals; hedging pressure is intraday-mean-reverting (Baltussen et al. 2021). Hypothesis, not edge. **And it did not survive scoring anyway** — see §3a.

### Indices and the rest — FLAT

SPY/QQQ/IWM all show no DEX sign change anywhere in the 12-session window (all-positive, call-heavy throughout) and all three carry **negative net_vanna** (call-heavy: SPY −359,715, QQQ −180,943, IWM −93,556). On a call-heavy book, falling VIX is a **selling-pressure headwind**, the mirror image of a squeeze. IWM's charm is −621,601 — the only negative charm in the scan.

All ten remaining single names (NVDA, MU, MRVL, TSM, AMD, META, UBER, MSTR, LITE, PLTR) show `qualifies=false` and call-heavy vanna. **MU (4 sign changes), META (4) and MSTR (5) carry explicit `whipsaw_warning=TRUE`** — their books are genuinely unstable in sign, so even a future flip on those names should be read sceptically.

---

## 2b. Sector Rotation

**Rotation regime call: `no_change`, confidence LOW.**

None of the four canonical patterns fits. Technology IN rules out growth→value; defensive→cyclical would require Industrials OUT, which is false; Consumer Cyclical OUT rules out cyclical→defensive since Industrials is IN. This is **not a macro rotation** — it is Tech flow-dominance plus one genuinely persistent single-sector distribution signal.

**Direction is read only off the NETTED `uw risk market-regime.sector_rotation` (C55).** The gross source (`sector-flow` and `sector-flow-persistence`, which are **one source**, values identical to the dollar) returned `persistence_score = 1` and `trend = INFLOW` for **all 11 sectors** today — **zero discrimination.** The ≥0.6 persistence gate is therefore **unsatisfied-by-degeneracy**, not confirmed. It is used below as a durability cross-reference only, never as direction.

### Per-sector persistence (netted source, 5-session reconstruction)

| Sector | 08-03 | 08-04 | 08-05 | 08-06 | 08-07 | Read |
|---|---|---|---|---|---|---|
| **Technology** | IN $217M | IN $839M | OUT −$65M | IN $620M | IN $110M | 4-of-5 IN, dollar-dominant every session |
| **Consumer Cyclical** | IN $77M | OUT −$63M | OUT −$61M | OUT −$45M | OUT −$31M | **4 consecutive sessions OUT — cleanest unbroken streak in the book** |
| Industrials | absent | IN $41M | OUT −$89M | IN $21M | IN $80M | 2-day streak, 1 reversal — moderate only |
| Healthcare | OUT −$36M | OUT −$28M | ~flat | absent | OUT −$7.5M | Weak, small-dollar persistent negative tilt |
| Communication Services | IN $138M | OUT −$103M | absent | IN $9M | OUT −$19M | Flips every session — noise |
| Consumer Defensive | OUT −$4M | absent | IN $3M | OUT −$9M | IN $9M | Flips 3× in 5 sessions, trivial dollars — noise despite today's "IN" |

**The XLY contradiction, resolved rather than papered over.** XLY was the day's best sector ETF (+1.49%, ABNB +17.4%) while the netted options book shows Consumer Cyclical bleeding for a fourth straight session. That is not a data error — it is **narrow-breadth price strength masking sector-level options distribution.** Price is carried by idiosyncratic winners (ABNB +17.4%, UBER +6.5%, TSLA +2.8%) while the aggregate sector book nets negative four sessions running. TSLA itself shows positive own net_flow (+$16.5M) inside a sector being sold — a genuine within-sector divergence.

### ETF flow tape (advisory — 0 rubric points)

| ETF | Net premium dir (5d) | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|
| **XLI** | **inflow +$17.24M** | Two blocks flagged with stale/crossed NBBO (ask $200.92 vs trade $185.18 — discounted); one clean $14.6M at mid | Mostly Sept put buying (ask side, 180 strike) + mixed Nov calls — no strong tell | **agree** (netted Industrials IN) | SPCX — **fails** the +1 gate |
| **EWY** | inflow +$15.05M | Aggressive above-mid buying ($18M, $8.5M, $8.4M, all buy-side) | Oct $190C ($4.2M) + Nov $165C ($4.2M) vs one Jan'27 $150P hedge ($8.95M) — net call-skewed | n/a (country basket) | — |
| **KRE** | inflow +$9.4M | Largest block shows crossed/stale NBBO — discounted | Small mixed put activity, no urgency | n/a | — |
| **GDX** | **outflow −$57.5M (largest in universe)** | Large blocks near mid (500k sh) — creation/redemption, not accumulation | **Contradicts its own 5d tape**: ~$72M of aggressive 0DTE bullish call buying (75/77.5 strikes) on GDX +7.1%/+21.3% | n/a | *excluded — appendix only* |
| **XLP** | outflow −$8.05M | 396k-share block near mid — hedging-flavoured | Small mixed tickets | **disagree** (netted Cons Defensive "IN" but is itself noise) | — |
| **XLE** | outflow −$6.53M | Mixed-side blocks near mid | Mixed puts/calls, no urgency | n/a — agrees with the tape (XLE −1.13%/−3.44%, weakest sector) | — |
| SMH | +$22.4M (largest raw inflow) but `trend_direction = MIXED` | not deep-pulled | not deep-pulled | n/a | **excluded from top-3 on persistence-over-magnitude** |
| XLK | +$4.2M (small but directionally clean) | rank-only | rank-only | **agree** (netted Tech IN) | see below |

GDX is excluded from every rotation and leader output: its 5-day tape is the universe's largest outflow while a single-day 0DTE call spike points the other way — textbook appendix-only. The tape is advisory and adds **no rubric points**; it strengthens the existing conditional sector-leader +1 only via `gics_agreement` and cum-flow alignment.

### Single-name leaders — the conditional +1, checked leg by leg

**Technology** (4-of-5 netted inflow, XLK agrees) — from `screener_bullish` ∩ C12 pass:

| Ticker | (a) persistence ≥0.6 | (b) 30d cum-flow aligned | (c) \|30d\| ≥ $50M | Qualifies? |
|---|---|---|---|---|
| NVDA | 1.0 *(degenerate — caveated)* | +$381.9M ✓ | ✓ | **Yes** |
| SNDK | 1.0 *(degenerate)* | +$1.247B ✓ | ✓ | **Yes** |
| MSFT | 1.0 *(degenerate)* | +$686.9M ✓ | ✓ | **Yes** |
| MRVL | 1.0 *(degenerate)* | +$90.9M ✓ | ✓ | **Yes** |
| **TSM** | 1.0 *(degenerate)* | **−$92.7M ✗ NOT aligned** | $92.7M | **No — excluded** |

TSM is flagged as a within-sector caution: today's +$14.6M print runs against a bearish 30-day book. **None of the four qualifiers reached the rubric anyway** — all four failed the Step 3 confluence gate at n=1 (see §8).

**Industrials** — the only net-flow-tagged name is **SPCX** (+$93.5M, dominating the sector aggregate). Gate: (b) −$20.2M **not aligned**, (c) **$20.2M < $50M** — **fails**. Strip SPCX and the sector is close to noise; CAR (−$29.0M) is a bearish outlier in the same sector the same day. Industrials is not a clean broad rotation.

**Consumer Cyclical** (persistent OUT) — LULU (−$25.7M) and AMZN (−$10.4M) carry the distribution. **Watch-only / short-vol context list, never a sized short** (2026-08-01 P0 #1).

**Swing-book implication:** the Technology inflow is the only durable netted call, but every one of its qualifying leaders died at the confluence gate — so the correct expression today is *no position*, not a Tech long. Consumer Cyclical's four-session distribution is watch-only. Industrials/SPCX is a single-day flash; do not swing-size it. Apply a uniform haircut for the 46.4% 0DTE retail overlay.

**Invalidation:** Technology breaks if the netted figure prints negative two consecutive sessions (08-07 is session 2 of the current re-confirmation, so one more negative flips it). Consumer Cyclical distribution breaks on two consecutive positive prints. Watch for `dte_share` pushing through 50% (deepen the haircut) and for the gross persistence tool regaining any discrimination at all.

---

## 3. Swing Setups (1–6 weeks)

**The book is empty.** Six names cleared the Step 3 confluence gate (≥2 distinct Phase 1 agents). All six scored **below the LOW cut of 3** under the frozen `2026-06-12` rubric and were filtered by the quant's drop floor.

| Ticker | Score | Tier | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|---|
| MU | 2 | DROP | Long vega into the 08-14 macro cluster: iv30d 72.3% vs realised 101.2% | *(would have been)* calendar around the 7dte kink | loses the $871.81 DP volume-weighted level | **skip** |
| AMD | 2 | DROP | Long vega into the 08-28 Core PCE kink | *(would have been)* 21dte calendar | loses the $483.41 DP level | **skip** |
| PLTR | 1 | DROP | Long on 30d flow accretion +$268.0M | — | loses the $169.18 DP level | **skip** |
| MSTR | 1 | DROP | Long on a Dec-2028 100/110 call vertical | defined-risk vertical, $15.3M capped | breaks $85 / Dec-2028 C100 OI fails to build past ~5k | **watch_only (VETO)** |
| LITE | 0 | DROP | Contested — neutral calendar vs bearish distribution | — | — | **skip** |
| TSLA | −1 | DROP | Long on the fleet's only mechanized DEX flip | — | DEX reverses negative ≥3 sessions | **skip** |

### 3a. Long swings (regime-aligned) — none sized

**TSLA is the day's most instructive kill.** It earned the only script-verified mechanized DEX flip in the entire fleet (+1) and a VRP-aligned kink watch (+1) — then took **−3 flow_conflict** against **−$616.8M** of 30-day cumulative premium, 2.39× the union median of $258.3M and the largest absolute net in the book. Net raw score: **−1**. This is the 2026-07-24 MU/NBIS pattern repeating exactly: the mechanized flip fires and dies on the flow gate. The gate is doing precisely what it was installed for after the 2026-05-08 NVDA raw-10 loss. TSLA additionally sits in Consumer Cyclical, the sector in netted outflow four straight sessions.

**PLTR is the only name with a graded substrate, and the substrate says no.** Its `bullish_flow` class realised **0.4255 on n=141** under the clean-query protocol, against a same-window SPY-long benchmark of **0.5106** — **market excess −8.5pp**. The class is losing to the index in an up-tape. The bull's own closing argument conceded the point: *"'the class is beta-negative but my specific ticker will be different' is precisely the kind of unfalsifiable special pleading the bear should throw back at me, and they'd be right to."* The quant also awarded **zero** on two lines a bull would expect: the multileg +2 (the Sep18 155C→Dec18 175C diagonal is a **de-risking duration roll** — delta cut 0.735→0.548, strike raised $20, buying the 61.3% Dec tenor while selling the 53.4% Sep tenor, the *wrong* side of contango) and the vol-surface +1 (term structure is **FLAT at both levels, no kink** — the predicate simply is not met). PLTR is +39.78% over five sessions with rv20 105.3% against rv60 84.2%, RSI 72.83, and no short-covering fuel (3.54% short float).

**MSTR is VETO'd.** It produced the cleanest opening structure of the day — ~49.8k Dec-2028 100/110 call verticals, $527M gross, **size/OI ≈ 10×** against 4,888 resting OI, ml_ratio 0.998/1.000, $3.07 on a $10-wide (risk capped $15.3M, max profit ~$34.5M). The term-structure logic is coherent: at 86% back-end IV an outright LEAP call is prohibitive, so the spread cancels vega and buys pure duration. But the fundamentals gate returned an effective 3-of-3 contradiction — miss streak (3 of 4, surprises to −1517.9%), insider MSPR negative **every month April–July 2026**, and a CEO publicly defending a pivot *away* from BTC accumulation toward cash reserves and buybacks, which repudiates the very premise of a +10%-by-2028 call vertical. Flow opposes on **all three horizons**: 30d −$257.6M, 90d −$590.5M, today −$128.1M (the day's #2 most bearish name).

> **A knife-edge worth registering.** MSTR's flow deduction printed **−1 (lite)** rather than **−3 (full)** because |−$257.6M| missed the union median of $258.3M **by $0.7M** — and that median was itself inflated by TSLA's −$617M outlier. Had −3 fired, MSTR would be raw −1 instead of 1, so the artifact was *conservative* and the empty book is robust to it. But the general point stands and should reach the next audit: **a flow_conflict threshold defined relative to the union median is composition-sensitive** — one extreme name reshapes the cut for everyone else. Harmless today; not harmless on a knife-edge LOW name.

**MU and AMD** both scored 2 on identical components (+1 vol-surface KINKED with VRP-aligned bias, +1 oi-trend BUILDING at 83 consecutive days). Both are direction-neutral vol theses, chosen over the contested bearish sweep read. Neither is backtestable — `vol_long` is not among the five classes `uw historical signal-backtest` supports, so `win_rate` is `NA(substrate)` by construction.

> **New artifact class found in Step 6, and it matters.** The "opening-confirmed bearish put build" that anchored sweep-tracker's MU and AMD reads dissolves on inspection of the premium. **MU260814P00550000**: 25,845 contracts at an average price of **$0.14**, strike 550 against spot 877.57 — that is ~**$362K** of total premium on a 37%-out-of-the-money put. **AMD260814P00297500**: 9,993 contracts at **$0.105**, strike 297.5 against spot 483.36 — ~**$105K**, 38% OTM. These are penny-priced deep-OTM tail hedges, **not** conviction bearish positioning, and they are far too small to have bid up the 08-14 tenor as the bear case claimed. The lesson generalises: **OI-confirmed-opening (ΔOI ÷ volume ≈ 1.0) is blind to premium and to moneyness.** A 99%-opening print on a 14-cent lottery ticket carries the same "opening confirmed" stamp as a $20M at-the-money block. Worth registering as a C4-adjacent screen.

### 3b. Short / fade swings (defined risk only) — empty

`contrarian-scanner` returned an **empty book** and the reasoning is sound. No name on the prime fade surface (PLTR, LITE, ABNB, GDX, UBER, NVDA, TTD, NFLX) clears ±2σ on `uw historical pc-ratio-zscore`:

| Ticker | Current P/C | 20d mean | z-score | Flag |
|---|---|---|---|---|
| SPY | 0.958 | 1.170 | **−1.417** | NORMAL (closest to extreme) |
| ABNB | 0.460 | 0.698 | −0.929 | NORMAL |
| PLTR | 0.427 | 0.540 | −0.870 | NORMAL |
| QQQ | 0.983 | 1.100 | −0.794 | NORMAL |
| GDX | 0.412 | 0.749 | −0.692 | NORMAL |
| LITE | 0.999 | 1.136 | −0.547 | NORMAL |
| NFLX | 0.390 | 0.481 | −0.530 | NORMAL |
| UBER | 0.531 | 0.606 | −0.417 | NORMAL |
| NVDA | 0.506 | 0.531 | −0.342 | NORMAL |
| TTD | 0.600 | 0.489 | +0.624 | NORMAL |

Two structural notes. First, **`pc-ratio-zscore` has no `--date` flag**, so the "rising z" clause of the −2 overcrowded-long line is unsatisfiable from a single call — only *levels* are claimable today, and none are close. Second, the two index carve-outs (SPY/QQQ) are on the **wrong side** even setting magnitude aside: current P/C is *below* trailing mean (complacent/call-skewed), so even a −2σ print would read as bullish-extreme informed-continuation caution, not the fear-extreme the fade literature supports.

**Both indices print negative VRP** (SPY FAIR −0.0073, QQQ PREMIUM_BUYING −0.0536), so selling premium into cheap vol is the wrong side regardless — any fade would have had to be defined-risk directional, not naked short premium or condors.

Price-vs-flow divergences do exist as context: **LITE** price +9.0% against net flow −$7.82M (IV rank 78.4); **GDX** price +16.7% against −$34.8M. Neither reaches the ≥3-aligned-signal bar. **All directional shorts print as `watch_only` regardless (2026-08-01 P0 #1)** — routing, not suppression: the theses are generated, scored, gate-verdicted and serialized so the counterfactual keeps resolving.

### Sweeps (informational — 0 rubric points)

The sweep-persistence rubric line was **removed 2026-05-23 (P0.3)** after −22pp marginal contribution across two audits. Ranked for narrative only:

| Rank | Ticker | Net dir (5d) | Persistence | Cum. premium | Opening confirmed |
|---|---|---|---|---|---|
| 1 | MU | bearish | 5/5 | $4.18B | yes — but see the penny-put artifact above |
| 2 | AMD | bearish | 5/5 | $1.93B | yes — same artifact |
| 3 | SPCX | bearish *(label)* | 5/5 | $3.10B | yes (DTE42, 81% opening) |

**A data-quality finding on the tool itself:** `consistency_score` is confirmed live to be exactly `sessions_in_top ÷ 5` — so a `1.0` means **participation, not same-direction confirmation**. For all three names, today's own tape is mixed. SPCX is the sharpest case: the 5-day label says bearish, but today's largest single print is a **bullish** LEAP call ask-buy ($16.3M Dec26 $110) and SPCX is the one name in today's top-20 smart-money-flow — **call-ask dominant, ratio 2.09×**. A stale netted label diverging from live tape.

Demoted on the mega-cap hedge-flow filter (sweep direction not confirmed by 30d cum-flow, all **MIXED**): SPY ($9.1B, cum-flow −$449M on $28.84B/$29.29B gross), QQQ ($8.1B, +$46.7M), IWM ($0.60B, −$252M), GOOGL ($1.01B, +$1.7M on ~$4.47B/$4.47B). SPX and SPXW disagree in sign with each other — itself evidence of 0DTE hedge flow rather than direction. NVDA/MSFT/TSLA/AMZN/META all MIXED and mega-cap-filtered; NVDA's 0DTE tape carries IV readings of 49–582%, textbook retail churn at a 46.4% 0DTE share.

---

## 4. LEAP Builds (6–24 months)

**Empty book.** No ticker reaches 6-of-9 gates. Every C12-pass name with DTE>180 open interest fails **Gate 4 (`historical cumulative-premium-flow`)**, a hard disqualifier — all return `trend_direction: MIXED` with net flow at 0–10% of gross. Consistent with the 3.0% LEAP volume share, but the disqualification is not merely thinness: it is a clean *absence of directional accretion* on every candidate.

| Ticker | Contract | Why disqualified |
|---|---|---|
| **IBIT** | 861DTE $15 PUT (61% OTM), oi_diff +64,771 (+4,937%), ask 58,222 ≫ bid 4,345 | Gate 4 flat (90d +$296.5M on $6.1B gross = 4.9%, MIXED). Also a **PUT** on a spot-BTC ETF — tail insurance, not a bullish thesis |
| **HYG** | 196DTE $76 PUT, oi_diff +11,778 (+39%) | Gate 4 flat (90d −$29.8M / $627M = 4.7%). Roll `balance_ratio` 0.685 below the 0.7 bar. Structurally a bond-ETF credit hedge |
| **SPCX** | 314/532DTE, CALL (220/185) **and** PUT (90/75) building simultaneously | Collar/hedge overlay, not directional. Gate 4 near-total noise (90d −$328.2M on $18.9B = 1.7%; 30d 0.17%). Roll balance 0.476 |
| **NVDA** | 314DTE $260 CALL, oi_diff +3,991 (+13.3%), ask 372 ≫ bid 89 | Gate 4 **hard fail**: 90d net $34.5M on **$93.5B** gross = **0.037%**. Conviction-matrix DIRECTIONAL_LONG but confidence **17%**, far below the >70 bar |
| **QQQ** | 861DTE $1100 CALL, oi_diff +4,346 (+1,076%) | **bid-dominant** (ask 9 / bid 2,029) = calls *sold*; paired with an ask-dominant 861DTE $600 PUT — a classic index collar |
| **META** | 497DTE $1450 CALL (145% OTM), oi_diff +2,201 (+2,717%) | **bid-dominant** (bid 1,711 ≫ ask 744) = far-OTM call *overwriting*, not accumulation |
| **IWM** | 314DTE $250 PUT, oi_diff +4,992 (+12.1%) | Gate 1 fails outright — trivial volume (ask 0, bid 5) |

Everything else in the top-60 `biggest-increases --min-dte 180` scan (CELH, EEM, ASX, B, UWMC, NOK, WBD, SLV, CLF, STM, NFLX $90C at 10 contracts, XLU $50C at 4 contracts, SKHY) fails the C12 liquidity floor or is trivial size.

**Blind-spot checks, both clean:** no merger-arb signature (no candidate shows the "100% mega-DP buy + clean LEAP OI build" fingerprint — all flow is MIXED or two-sided); the one put-sale-netting candidate (NVDA's 314DTE $130 put, bid 4,465 ≫ ask 134) is moot since NVDA dies on Gate 4 first.

---

## 5. Volatility Surface

**Mandatory substrate hygiene was run and it mattered enormously.** `scripts/term_structure_hygiene.py` (min_contracts=15, a **tunable, NOT audit-frozen** parameter) on 12 names: raw `iv-term-structure` returned **BACKWARDATION on 12 of 12**. After dropping the 0DTE bucket and sub-threshold tenors, **11 of 12 flipped** and **10 of 12 base_shape flipped to CONTANGO**. Only **LITE and GDX** kept genuine backwardation at the base level. This reproduces the 2026-07-24 defect at full scale — no raw label is trustworthy without this filter.

**Two further substrate defects to note.** `iv-percentile-zscore --lookback-days 252` returned **`dates_used: 82` for every name** — below the 120-day floor, so **every percentile below is PROVISIONAL**. And the cached single-contract `iv-outliers` set, filtered to C12-pass names, yields exactly 4 rows (MSTR, MRVL ×2, TTD) — **all four on the 2026-08-07 (0DTE) expiry**, i.e. mechanical wing blowups on expiring contracts. **Zero qualifying single-contract IV outliers today.**

### Kinked names with catalyst alignment

| Ticker | Shape (hygiene) | Kink | Prominence | IV pctl (prov.) | VRP | front-end(7) | Implied move @ kink | Catalyst | Bias |
|---|---|---|---|---|---|---|---|---|---|
| **TSM** | KINKED (base CONTANGO) | 21dte/**08-28**, 42dte/**09-18** | **35.4%** (n=3290), **105.9%** (n=5435) | **0.0**, z **−2.062** | **−0.1165** PREMIUM_BUYING | 0.797 (cheap) | 17.77% | **Core PCE**; post-FOMC | **BUY VOL / CALENDAR — highest conviction** |
| MU | KINKED (base CONTANGO) | 7dte/08-14 | 11.4% | 13.41, z −1.457 | **−0.2891** | 0.964 | 11.8% | CPI/PPI/claims/retail cluster | BUY VOL / CALENDAR |
| AMD | KINKED (base CONTANGO) | 21dte/08-28 | **7.6% — thinnest of the day** | 13.41, z −0.96 | −0.2288 | 1.021 | 17.74% | Core PCE | BUY VOL — low conviction |
| AMZN | KINKED (base CONTANGO) | 5dte/**08-12** | 19.5% | 24.39, z −0.851 | −0.2378 | 1.028 | 4.73% | **CPI day** | **Correctly priced — not an edge** |
| MSTR | KINKED (base CONTANGO) | 21dte/08-28 | 10.1% | 32.93, z −0.646 | **−0.0282 FAIR** | 0.94 | 22.09% | Core PCE | Weak calendar, low conviction |
| TSLA | KINKED (base CONTANGO) | 12dte/08-19 | 11.4% | **8.54**, z −1.536 | −0.2539 | 1.006 | 10.92% | **no catalyst match** | BUY VOL on cheapness; kink itself low-conviction |
| NVDA | KINKED (base CONTANGO) | 7dte/08-14 | 9.4% | 52.44, z −0.165 | **+0.0104 FAIR** | 0.861 | — | macro cluster | **NEUTRAL — skip, fairly priced** |
| PLTR | **FLAT both levels** | none (best 3.1%, sub-threshold) | — | 46.34, z −0.525 | **−0.5044 — most negative in batch** | 1.038 | 7.76% (front) | — | BUY VOL, straight long-vega, no calendar leg |
| SOXX | clean **CONTANGO** | none (best 5.0%, sub-threshold) | — | 42.68, z −0.301 | −0.128 | 0.907 | — | — | mild BUY VOL, basket context |

### Genuine backwardation — both disqualified

**GDX** — base_shape did **not** flip under hygiene; this is real backwardation. front-end-iv-ratio **1.124 = genuine panic**, driven by the +7.1%/+21.3% gold-miner rip on a weakening dollar. VRP −0.0411 FAIR — no vol edge despite the dislocation. The standing rule fires: **BACKWARDATION with front-end ratio > 1.10 — do not fade.** `WATCH_ONLY`, no new premium.

**LITE** — base_shape did not flip. front-end-iv-ratio **1.288 = severe panic**, consistent with a pre-earnings bid (08-11 postmarket, T+2). IV percentile 71.95, z +0.562, VRP −0.0228 FAIR. Same disqualifier; earnings-scout's lane (see below).

**Net: the "BACKWARDATION with no catalyst → calendar" bucket is EMPTY today.** Both real-backwardation names have *rising, unresolving* front-end ratios and fail the falling-ratio gate.

### Earnings vol lane

Only **3 names** survive `earnings_catalyst` (289 rows) ∩ the C12 floor: **LITE, COHR, NBIS**. The other 286 are sub-floor micro/small-caps (the ALMS-at-iv_rank-100 pattern).

**A structural finding: none of the three has an expiry landing on its earnings date.** LITE reports 08-11, COHR and NBIS on 08-12; no Tuesday or Wednesday weekly exists for any of them. The nearest surviving tenor is the 08-14 Friday weekly. **The "kink at earnings expiry" gate therefore cannot fire for any of them by construction** — there is no candidate tenor to kink on.

| | LITE | COHR | NBIS |
|---|---|---|---|
| Earnings | **2026-08-11 pm (confirmed)** | 2026-08-12 pm | 2026-08-12, time unknown |
| Close | $890.17 | $379.13 | $187.97 |
| Shape (hygiene) | BACKWARDATION, **no kink** | BACKWARDATION, **no kink** | raw BACKWARDATION → **KINKED at 09-18 (DTE 42) — NOT the earnings date** |
| front-end(7) | **1.288** | **1.305** | **1.246** |
| Back skew (42dte) | −0.0084 COMPLACENT | −0.0161 COMPLACENT | +0.0067 ≈flat |
| Front ATM IV | 138.1% | 140.8% | 156.8% |
| **IV-derived implied move** | **≈19.1%** | **≈19.5%** | **≈21.7%** |
| Flow | bearish, −$7.8M | bullish, +$6.0M | bearish, −$15.1M |
| **Verdict** | **CALENDAR** | **CALENDAR** | **CALENDAR (with caution)** |

**No BUY VOL and no SELL VOL calls this session.** All three route to CALENDAR, gated by extreme front-end panic (all >1.10), flat/complacent back skew (which affirmatively disqualifies SELL VOL sizing), no genuine at-event kink, and CPI event-stacking. **Since the rubric's +1 line requires BUY VOL *or* SELL VOL, CALENDAR earns zero** — which is why LITE scored raw 0 with an empty component set.

NBIS carries an extra caution: **do not use the 09-18 tenor as the back leg** — it *is* the anomalous rich tenor (133.0% IV against ~122% expected from the surrounding decay). Use 09-11 (35dte, 122.1%) or 10-16 (70dte, 118.7%).

> **Data-quality defect, corroborated twice.** The cached `earnings_catalyst.implied_move_perc` reads **0.53–0.85%** for these three names against IV-derived values of ~19–22% — roughly an order of magnitude low, consistent with a ~15–16% annualised IV baseline being used instead of the actual 138–157% front-tenor IV. Step 6's `uw insights deep-dive` independently reproduces it: MU `implied_move_perc` 0.00238 (0.238%) against iv30d 72.3%; AMD 0.00377; PLTR 0.00269. **This is not confined to the earnings screener — the field is broken across the CLI.** Same class as the C43 emission bug. Every `implied_move` in this report's envelope is IV-derived, not taken from the field.

---

## 6. Risk & Correlation

**Macro headline:** stagflationary tilt — core PCE **3.29%** sticky above target, payrolls **−23k** contracting, 10Y **4.69%** rising, curve normal +46bp, USD weakening, fed funds 3.63%. **CPI 2026-08-12 is T+3.**

**Breadth cross-check (advisory):** 321 advancers / 180 decliners, **63.8% green**, `divergence_flag: false`. Green tape *with* majority-green breadth — **no distribution divergence** in price. The divergence that does exist is between price breadth (63.8% green) and UW's options-flow breadth (**37.7% bullish**), which supports the empty book rather than arguing against it. Advisory; does not change sizing.

**Correlation clusters** (`uw risk portfolio-correlation` against today's candidates, not the static watchlist):

| Cluster | Members | Pairwise | Kept |
|---|---|---|---|
| **`AI_semis_optics`** | MU / AMD / LITE | MU–LITE **0.858**, MU–AMD **0.841**, AMD–LITE **0.823** | **MU** (raw-2 tie with AMD broken on \|30d flow\|: $258.9M vs $48.0M) |

Three of six candidates were **one position**. AMD and LITE take the mechanical −1 cluster tier. No soft-watch pairs — the next-highest is AMD/TSLA at 0.517, below the 0.60 band. PLTR and MSTR are uncorrelated with the cluster at the 30-day lookback.

**Gate stack applied — 9 keys per call.** Live (non-no-op) gates today:

| Gate | Fired on | Detail |
|---|---|---|
| `fundamentals` | MSTR (**VETO**), LITE (−1), TSLA (−1) | MSTR routes to watch-only outright |
| `debate` | **all five debated names** | bear residual ≥ bull in every case |
| `cluster` | AMD, LITE | `AI_semis_optics`, MU kept |
| `event_risk` | PLTR, MSTR, TSLA | CPI T+3 through undefined-risk directional exposure. MU/AMD exempt (defined-risk long-vol *through* the print); LITE exempt (it **is** the event play) |
| `panic` | LITE only | front-end-iv-ratio **1.288**, sole breach of 1.10 |
| `sector` | TSLA | Consumer Cyclical netted outflow 4 consecutive sessions (persistence 0.8) |
| `rubric_regime` | **all six** | OUT-OF-REGIME, capped half — freeze holds a 7th cycle |
| `regime`, `vrp` | none | recorded as no-ops |

**Debate residuals** — the gate fired 5-of-5:

| Ticker | Bull | Bear | Verdict |
|---|---|---|---|
| MSTR | 0.15 | **0.85** | widest spread; debate agrees with the VETO |
| LITE | 0.25 | **0.75** | |
| MU | 0.35 | **0.75** | |
| PLTR | 0.35 | **0.65** | |
| AMD | 0.25 | 0.25 | **BOTH_SIDES_LOW** — neither advocate cleared a coin flip |
| TSLA | null | null | not debated (6th, below top-5) — a *reasoned* null |

No escalation to a second round: the rule requires both residuals ≥0.75 *and* within one bin. AMD's 0.25/0.25 is within a bin but far below 0.75. **AMD's both-sides-low pair is the strongest kill signal the debate produces** and is recorded verbatim — the schema's residual floor was lowered from 0.55 to 0.15 by the 2026-07-25 audit precisely so pairs like this survive serialization (the fix that erased TSLA's 0.42/0.40 on 07-23 is confirmed working).

**Adverse-flow exit lane:** `uw watchlist alerts --group conviction_2026-08-06` returns **empty — the group does not exist**, because yesterday's board was also all-DROP and correctly wrote nothing. **Zero carried positions ⇒ zero exit candidates.** The advisory 87-name static scan shows MU −$28.9M, AMD −$20.2M, TSLA +$16.5M (a one-day counter-tick against −$616.8M over 30d), SPY −$135.6M, QQQ −$26.0M, SMH pcr 4.39 — the index tape agrees with the put-heavy breadth tell.

**Hedge sleeve:** the mechanical trigger (directional skew ≥0.6 of net book delta) **does not fire — net delta is zero.** No hedge is mandatory. On the discretionary question, the setup for cheap convexity is genuinely present: VIX 14.9, QQQ VRP PREMIUM_BUYING (implied below realised — you are paid to own vol), a stagflationary print stack at T+3, and a tape rising on 37.7% bullish options breadth. If the desk wants insurance: **starter-size, defined-risk long-vol on QQQ** — a put debit spread or put calendar through 08-12, or a Sept VIX call ladder — capped at starter under the `rubric_regime` discipline. This is portfolio insurance (a hedge *use*, explicitly out of scope of the short-routing rule), not an alpha call. **With no book to protect, carrying nothing is equally acceptable.**

### Empty-book sanity assessment

**Correctly gated, not accidentally empty.** The board is empty at *every* layer independently — raw scores (max 2 vs a LOW cut of 3), fundamentals (1 VETO, 2 CAUTION), debate (bear ≥ bull 5-of-5), cluster (3 of 6 names are one position), and event risk (CPI T+3). No single gate carries the whole kill.

Three near-misses were specifically re-examined:

- **MSTR's flow knife-edge** — confirmed conservative. Correcting it could only push MSTR deeper into DROP. Escalated to the next audit as a composition-sensitivity issue, not a live fix.
- **TSM** — correct kill under the frozen funnel, and the strongest watch-item in the report. It failed confluence at n=1 despite being vol-surface-scout's highest-conviction name. Three reasons it is not a suppressed real call: (1) the n=1 kill is the *designed* behaviour — the 2026-06-12 audit collapsed confluence to funnel-only precisely because composite re-counting manufactured conviction; (2) its headline stats ride the `dates_used: 82` defect, so "percentile 0.0, z −2.062" is computed on a third of the advertised window and is less extreme than it reads; (3) `sector-rotation-strategist` actively excluded it (30d cum-flow −$92.7M, not aligned) — that is a negative verdict, not a missing second opinion. **Disposition: if a second Phase 1 agent independently surfaces TSM on Monday, it earns a real funnel pass. Do not back-door it today.**
- **INSM** — correct kill, and empirically endorsed rather than merely mechanical. It was the only name to pass a full accumulation gate stack (see §8), but the audit record actively supports killing pure-accumulation singles: the accumulation +3 conjunction was BH-significant **negative**-excess (C48, −29.2pp, p=0.003; beta thesis reconfirmed 2026-07-18).

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**No names qualify.** Zero HIGH-tier and zero MEDIUM-tier calls. Highest raw_score is 2 against a MEDIUM cut of 7.

Consequently: **Step 6.5 batched strategy synthesis was skipped** (`uw playbook batch-scan` operates on raw_score ≥ 7 — the list is empty), and **Step 8.5 deep-dive hand-off was skipped** per the standing "no edge day" rule (no HIGH-tier names). Step 6 deep-dives ran anyway on the top 3 by score (MU, AMD, PLTR) and surfaced the penny-put artifact documented in §3a.

### Expectancy lens `[advisory — expectancy is not yet a live sizing axis]`

From the most recent `/calibration-audit` (2026-08-01, `phase_3_calibration`):

| Tier | n | Realised WR | Mean PnL | Payoff ratio (avg win / \|avg loss\|) |
|---|---|---|---|---|
| HIGH | 7 | 0.143 | −2.441% | 0.72 |
| MEDIUM | 19 | 0.526 | +0.104% | 0.948 |
| LOW | 91 | 0.418 | −0.583% | **1.197** |
| **DROP** | **384** | **0.440** | −2.270% | 0.824 |

**Tier ranking remains inverted and the DROP pile still out-hits LOW (0.440 vs 0.418).** The Kelly gate is `ADVISORY_ONLY` — n=27 closed is below the 30 required and tier × expectancy is non-monotone (LOW −1.784 > HIGH −1.965 > MEDIUM −2.239). Do not flip the sizer; the win-rate ladder stays live. Display-only context: note that **LOW is the only tier with a payoff ratio above 1.0** — the book's edge, such as it is, lives in payoff not hit-rate.

### Per-ticker audit trail (all DROP — recorded for the calibration loop)

| Ticker | Dir | Raw | Components | Class | win_rate (src, n) | Excess | Pre-risk | Fund. | Bull/Bear | Gates fired | Final |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MU | vol_long | **2** | +1 vol-surface KINKED/VRP · +1 oi-trend BUILDING | `event_vol` | null, NA(substrate) | — | skip | CONFIRM | 0.35 / 0.75 | debate, rubric_regime | **skip** |
| AMD | vol_long | **2** | +1 vol-surface KINKED/VRP · +1 oi-trend BUILDING | `event_vol` | null, NA(substrate) | — | skip | CONFIRM | 0.25 / 0.25 | cluster, debate, rubric_regime | **skip** |
| PLTR | long | **1** | +1 cum-flow 30d accretion | bullish_flow | **0.4255**, backtest_clean, n=141 | **−0.0851** | skip | CONFIRM | 0.35 / 0.65 | event_risk, debate, rubric_regime | **skip** |
| MSTR | long | **1** | +2 multileg directional · −1 flow_conflict_lite | multileg_directional | null, NA(substrate) | — | skip | **VETO** | 0.15 / 0.85 | fundamentals, event_risk, debate, rubric_regime | **watch_only** |
| LITE | neutral | **0** | *(empty)* | earnings_vol | null, NA(substrate) | — | skip | CAUTION | 0.25 / 0.75 | panic, cluster, fundamentals, debate, rubric_regime | **skip** |
| TSLA | long | **−1** | +1 mechanized DEX flip · +1 vol-surface KINKED · **−3 flow_conflict** | vanna_squeeze | null, NA(substrate) | — | skip | CAUTION | not debated | sector, fundamentals, event_risk, rubric_regime | **skip** |

**Only one name in the book had a quotable win-rate at all.** Five of six are `NA(substrate)` because `uw historical signal-backtest` supports exactly five classes (`bullish_flow`, `bearish_flow`, `high_iv_rank`, `volume_spike`, `dark_pool_accumulation`) and today's dominant classes were `event_vol` ×2, `multileg_directional`, `earnings_vol` and `vanna_squeeze` — none of them covered.

*Class-naming note:* the quant labelled MU and AMD `vol_long`, which is **not** on the schema's canonical class list, so the envelope maps both to **`event_vol`** — the correct canonical fit, since each is a direction-neutral vol thesis anchored to a scheduled macro-event kink (MU on the 08-14 CPI/PPI/claims/retail cluster, AMD on 08-28 Core PCE) and neither has earnings inside the window. The mapping does not change the `NA(substrate)` verdict — `event_vol` is likewise not among the five backtestable classes. The one graded class (PLTR / `bullish_flow`) came back **0.4255 on n=141 with −8.5pp excess.** Clean-protocol detail: `--top-n 200` pinned, 156 rows returned, headline 45.5% **never quoted**, 14 clamped rows dropped (signal_date > 2026-07-31, incomplete 5-td forward window), 1 row dropped at the C12 floor (HTZ at $2.27). Union-median |cum_flow_30d| = **$258.3M**.

**Data-quality note carried from the quant:** `cumulative-premium-flow` returned `trend_direction: MIXED` on **6 of 6** names — the label is degenerate today, the same failure mode as the all-sectors `persistence_score=1`. The quantitative branches (signed sum, union-median magnitude, quartiles) were used instead and the label treated as non-informative.

### Conviction-scoring rubric (verbatim, frozen `2026-06-12`)

```
Daily conviction score = Σ:
  +1  MECHANIZED DEX flip or vanna-squeeze in trade direction — script-verified SIGN CHANGE only
      (sign(net_dex) latest session opposite to ≥3 consecutive priors; |net_dex| ≥ 0.25× trailing-10
      median; computed by scripts/dex_flip.py, never by hand). A positive DEX LEVEL in an up-tape is beta.
  +3  3+ aligned accumulation signals (DP + OI + smart-positioning, block-stratified institutional-tier)
      — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms (sign aligned AND
      |cum_flow_30d| ≥ $50M); else HALVED (floored) +3→+1.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix DIRECTIONAL_LONG conf > 70 — CONDITIONAL: only when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +1  cum-premium-flow net directional accretion in trade direction (30d) — INTENT-SCREENED:
      0 if a C28 distribution_flag is present, or if deep-ITM sub-parity ex-div calls drive it.
  +1  sector-rotation single-name leader — CONDITIONAL: (a) sector persistence_score ≥ 0.6,
      (b) cum_flow_30d aligned, (c) |cum_flow_30d| ≥ $50M. Default 0.
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored play type)
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist top-5 (OPEX week only)
  -2  contrarian-scanner overcrowded long with RISING pc-ratio-zscore (VRP positive)
      — an INFORMED-FLOW CONTINUATION penalty, not "the crowd is wrong, fade it".
  -3  flow_conflict — cum_premium_flow 30d CLEARLY OPPOSITE dominant_signal_class
      (signed-sum sign flip + magnitude > today's union-median |cum_flow_30d|, or explicit OPPOSITE)
  -1  flow_conflict_lite — 30d read MIXED (signed sum near zero, or aligned but bottom-quartile)
      [flow_conflict and flow_conflict_lite are MUTUALLY EXCLUSIVE — apply ONE, never both]

  # sweep-persistence top-5 REMOVED 2026-05-23 P0.3 (−22pp, two consecutive audits) — earns 0.
  # signal-confluence ≥4 (+2) REMOVED 2026-06-12 P0.2 — the tool is a server-side RE-COUNT of
  #   already-scored quantities; it now has exactly ONE role, the Step 0 funnel seed.
  # gamma-flip-tracker 0DTE breakout REMOVED 2026-05-09 (NO-INFO on swing); §2 is advisory, 0 points.
  # The two lines below are risk-monitor TIER gates in 2d, NOT score_components (0 to raw_score):
  -1  [TIER GATE] correlation cluster (pairwise corr ≥ 0.70) — −1 TIER, not −1 point
  -3  [TIER GATE] uw risk market-regime conflicts with trade direction — −1 TIER, not −3 points

Tiers: ≥9 HIGH (full) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 DROP.
Tier-cut status: the ≥9 HIGH cut FAILED its scheduled re-confirmation 2026-06-12 (bands inverted).
Cuts retained under the P0.1 freeze but carry NO validated ranking claim; P0.6 caps all sizing at half.
```

---

## 8. Watch-only — single signal, no confluence

Candidates surfaced by exactly one Phase 1 agent. Listed for journaling, **not for trade entry**. Note that Step-0 funnel appearance does **not** count as an agent flag — the `uw insights signal-confluence` entry path was removed 2026-06-12 (P0.2).

**The two most interesting names in the entire report are in this section**, which is itself the finding:

- **TSM** *(vol-surface-scout only)* — the fleet's highest-conviction vol read. IV percentile **0.0**, z **−2.062** (most extreme in the batch, though PROVISIONAL on `dates_used: 82`), VRP **−0.1165 PREMIUM_BUYING**, front-end-iv-ratio **0.797** (front genuinely cheap), and **two thick, catalyst-aligned kinks**: 21dte/**08-28 Core PCE** (prominence 35.4%, n=3,290) and 42dte/**09-18 post-FOMC** (prominence 105.9%, n=5,435). Killed because `sector-rotation-strategist` explicitly *excluded* it — 30d cum-flow **−$92.7M, not aligned** with a long thesis — which is a negative verdict, not a second positive flag. **The single name to watch Monday.**
- **INSM** *(accumulation-hunter only)* — the only name in the fleet to pass a full accumulation gate stack, with **5 aligned signals**: block-stratified `highest_tier=block` buy_ratio **0.908** and — critically — **clean of the closing-cross artifact** (largest block $7.99M / 62,000sh printed at **14:30:22Z**, with only ~13% of block premium in the 20:00–20:25Z window); institutional-accumulation ACCUMULATION at buy/sell **2.0** on $74.4M; oi-trend **BUILDING 5/5 days**, +17,657 contracts; cum-flow BULLISH +$6.31M on $46.9M gross (**13.5% net-of-gross** — no put-sale-netting red flag); conviction-matrix **DIRECTIONAL_LONG at 60.2%**. DP support **$128.84**. `dp_block_to_float_ratio` 0.000289; `insider_cluster_present` **false** (checked, not skipped). ⚠ **distribution caution:** ~$15.6M of **call OI being closed** across 5 strikes (140C/105dte −1,533; 100C/161dte −417 deep-ITM; 130C/14dte −361; 110C/14dte −384; 120C/105dte −273) — someone unwinding bullish call exposure the same day the DP tape buys stock. Also RSI 73.7, +26.8% over 30d.
- **NVDA** *(sector-rotation only)* — Tech leader passing all three +1 legs (30d +$381.9M). But accumulation-hunter near-missed it (conviction-matrix confidence **17%**; mega tier $1.32B entirely 20:00–20:13Z closing-cross), vol-surface called it **NEUTRAL/skip** (VRP +0.0104 FAIR, fairly priced), sweep-tracker disqualified it (MIXED + mega-cap filter), and leap-radar killed it on Gate 4 (0.037% net-of-gross).
- **SNDK** *(sector-rotation only)* — passes all three +1 legs (30d +$1.247B), but carries the standing **2026-08-06 put-sale-netting flag**; conviction-matrix MIXED; sweeps read as a collar/hedge.
- **MSFT** *(sector-rotation only)* — all three legs hold (30d +$686.9M); conviction-matrix MIXED.
- **MRVL** *(sector-rotation only)* — all three legs hold (30d +$90.9M); sweep persistence only 1/5.
- **COHR** *(earnings-scout only)* — front-end-iv-ratio **1.305**, the most extreme of the day. CPI lands **same-day** as its 08-12 print — a double catalyst that genuinely justifies the elevated front IV rather than mispricing it.
- **NBIS** *(earnings-scout only)* — kink is at 09-18, not the earnings date; excluded from the earnings read.
- **MCHP** *(multileg only)* — the only exact-contract multi-day repeat (08-04 and 08-07, identical strikes and expiries). But the Sep18 75C / Dec18 65C diagonal is **capped at $75 and MCHP closed +13.89% at $84.69** — $9.69 through the cap. A poor-man's-covered-call whose upside was surrendered; deltas 0.805/0.778 near delta-neutral. Open-vs-close unresolved (size/OI 0.80 and 0.94 is a classic closing signature, but OI files lag a session); unwind is the more coherent read.
- **GLD** *(multileg only)* — Nov20 335P/470C risk-reversal, repeat_count **3** (highest persistence in the multileg book). Direction **corrected** by smart-positioning: the 08-06 Sep leg was **SELL 410C / BUY 430C** (bid 56,354 vs ask 1,834) — a *sold* call spread / overwrite, not a bullish initiation; Nov 345P also sold. ⚠ the short 335P/345P legs mean this structure is **not downside-capped**.
- **SPCX** *(sweep-tracker only, with caution)* — 5/5 bearish label contradicted by today's bullish call-ask dominance; sector-rotation explicitly fails it for the +1; leap-radar reads it as a collar.
- **GDX** — **zero** positive nominations despite +7.11%/+21.31%. vol-surface `WATCH_ONLY` ("do not size"), sector-rotation excluded it entirely, multileg screened its 0DTE 75C/77.5C as an exact-parity artifact, contrarian had 1 signal but failed the crowding gate.
- **IBM** — **zero** nominations, but arguably the cleanest raw DP tape of the day: block buy_ratio 0.788 across 25 trades spread all session (9:37am–4:56pm ET, **zero mega-tier print**, so structurally immune to the closing-cross artifact), oi-trend BUILDING 5d, ACCUMULATION 2.13, cum-flow +$36.5M. **Killed solely by conviction-matrix confidence 22.1%.** 4 of 5 signals aligned.
- **UBER / RTX** — accumulation near-misses. UBER: 3 aligned but mega-tier DP is 100% closing-cross ($94.8M @ 20:13:01Z) and conviction-matrix 29.5%. RTX: buy/sell ratio 19.46 but mega tier n=2, conviction-matrix 46.8%, cum-flow MIXED.
- **LULU / AMZN** — Consumer Cyclical distribution names. Watch-only / short-vol context, never sized shorts.

---

## Appendix — run-quality findings for the next `/calibration-audit`

1. **`fz` screen emitter is doubling the first letter of every ticker again** — `AABNB`=ABNB, `HHALO`=HALO, `QQNST`=QNST, `CCRSR`=CRSR, `PPUBM`=PUBM, `FFIVN`=FIVN, `NNTRA`=NTRA, `TTILE`=TILE, plus the entire A-prefixed squeeze slice (AABEO, AABR, AACHC, AAESI, AAI, AAIRS). This is the documented **MMSFT-class defect** that blocked C16 for four audits. **`fz breadth` returned `ABNB` correctly, so the defect is in the SCREEN emitter specifically.** `fz_enrich.py --ticker` is unaffected (verified — every payload echoed the correct ticker). The squeeze lane was additionally alphabetically head-truncated to an A-only slice and was marked `usable: false`; the RS lane was de-doubled manually and used.
2. **The closing-cross mega-DP artifact contaminated every mega-cap in the top-30 DP premium list** — MSFT $975M, MU $706M, NVDA $549M, META $325M, AMD $290M, PLTR $275M, AMZN $253M, ORCL $105M+$176M, TSLA $122M+$102M, UBER $94.8M — all at the exact closing price with duplicate/echoed premiums in the 20:00–20:25Z window. It invalidated the institutional-tier read on all of them and left INSM as the only survivor.
3. **`implied_move_perc` is broken CLI-wide, not just in the earnings screener** (new this run). Reproduced in `uw insights deep-dive` for MU (0.238% against iv30d 72.3%), AMD (0.377%) and PLTR (0.269%), and in `earnings_catalyst` for LITE/COHR/NBIS (0.53–0.85% against IV-derived 19–22%). C43-class emission defect. All envelope `implied_move` values are IV-derived.
4. **New artifact class — "opening-confirmed" is blind to premium and moneyness.** MU260814P00550000 is 25,845 contracts at **$0.14** (≈$362K, 37% OTM) and AMD260814P00297500 is 9,993 at **$0.105** (≈$105K, 38% OTM), yet both carry a ~99–100% ΔOI/volume opening stamp and anchored a "$4.18B bearish build" narrative. Recommend a premium/moneyness screen alongside the C4 OI-opening gate.
5. **`sweep-persistence.consistency_score` is exactly `sessions_in_top ÷ 5`** — participation, not same-direction confirmation. A `1.0` does not mean the direction held.
6. **Funnel gap (structural).** `multileg-strategist` independently verified that **MCHP (adv $932M)** and **GLD (adv $2,827M)** both pass the C12 floor but were **absent from the Step-0 pass list** — because the Step-0 universe is seeded from *flow leaders*, not a liquidity universe. Liquid names that did not light up the options screens are never floored and never reach the agents. Neither changes today's book (both n=1), but the defect is real.
7. **Two known substrate defects reconfirmed:** `iv-percentile-zscore` returned `dates_used: 82` against a 252-day request for **every** name (all percentiles PROVISIONAL); `pc-ratio-zscore` still has no `--date` flag (the "rising z" clause of the −2 line remains unsatisfiable).
8. **Two degeneracies on the same day:** gross `sector-flow-persistence` returned `persistence_score=1 / INFLOW` for **all 11 sectors**, and `cumulative-premium-flow` returned `trend_direction: MIXED` for **6 of 6** scored names. Both labels carried zero information; both were bypassed in favour of quantitative branches.
9. **Flow_conflict threshold is composition-sensitive** — MSTR missed the −3 branch by $0.7M against a union median inflated by a single outlier (TSLA −$617M). Conservative today; not structurally safe.
10. **Schema fix confirmed working:** the 2026-07-25 P1 #5 lowering of the debate-residual floor from 0.55 to 0.15 allowed today's 0.15/0.25/0.35 bull residuals — including AMD's BOTH_SIDES_LOW 0.25/0.25 pair — to serialize. Under the old floor all five would have been clamped or erased.
11. **`vol_long` is not a canonical `dominant_signal_class`** and the validator caught it (warning, not an error). The quant emits it for direction-neutral vol theses; the schema's `x-canonical-classes` list has no such member. Mapped to `event_vol` here, but the quant should emit a canonical value directly — otherwise every audit has to re-implement the collapse. Worth a one-line fix in `signal-confluence-quant.md`.
