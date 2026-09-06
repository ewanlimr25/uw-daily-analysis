# Daily Market Analysis — 2026-06-10

## Executive Summary
- **Regime + GEX state:** **TRANSITIONAL / PULLBACK_IN_UPTREND**, risk-off. SPY 725.43 (below 20sma 745.62, above 50sma 719.32, −1.88% 30d). **VIX 22.25 spiking +2.4** on a hot CPI print (headline ~4.2% YoY, 3-yr high) + US-Iran/Hormuz backdrop. Breadth bearish — 34% bullish flow; `fz` confirms (174 adv / 328 decl, 34.6% green, no divergence). SPY/QQQ/IWM **all deeply short-gamma** (FULLY_NEGATIVE; SPY total GEX −2.5B, the most negative print in 30 days). Defensive sector lean.
- **Next-session GEX (SPY/QQQ):** **SPY** — SHORT-GAMMA (FULLY_NEGATIVE), ZGL null/unreliable, total GEX −2.5B; accel strikes 725/720 down, 741 release up · bias: trend/breakout, debit-directional not naked premium-sell. **QQQ** — SHORT-GAMMA (FULLY_NEGATIVE), −794M; 700/690 down, 715 up · front-end 2.03×VIX (extreme). **Advisory — PPI 8:30am tomorrow voids the prior on a gap.** See §2.
- **Top swing build:** **SMH SHORT — HALF size** (raw 9, the only HIGH name). Bear call spread above spot (IV rank 100 → sell rich premium, defined risk). Dealer short-gamma + macro risk-off + validated bearish-flow edge (+57.7pp market-excess). Invalidation: close > 600. WR 0.80 (n=29).
- **Top LEAP candidate:** **None.** No DTE>180 build cleared the conviction-matrix / cum-flow gates; long-dated tape is defensive ETF put hedging (LEAP share only 5.0%).
- **Biggest risk:** The whole book is **one correlated bearish-beta cluster** (SMH/SPY/IWM/LRCX pairwise corr ≥0.75; SMH/LRCX 0.92). Sized as ONE position: SMH-short-half + a **SPY 730/745 call-spread hedge** for the dovish-FOMC / cool-PPI squeeze tail. Do not stack four naked correlated shorts into the densest event week of the month.

> **No-edge-on-the-long-side day.** Zero accumulation cleared (all DP bids were COVERED_CALL/HEDGED_LONG); zero fades cleared (trends in progress, not crowding); zero LEAPs. The single coherent edge is a **defensive/short** lean, gated hard by a three-event window (PPI 6/11, SpaceX IPO 6/12, FOMC 6/17).

---

## 1. Regime & Gamma State

- **`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend **PULLBACK_IN_UPTREND**. Breadth bearish: 2,121 bullish / 4,114 bearish tickers (34% bullish). Guidance: half position sizes, defined-risk, iron condors in range.
- **Breadth cross-check (`fz`, advisory):** 174 advancers / 328 decliners, **pct_green 34.6%**, avg −1.2%, median −1.13%, worst SMCI −27.98%. **No divergence** from the `uw` label — the red tape is genuine, no washed-out contrarian signal to fade.

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 726.71 | null (unreliable) | **−2.51B** (deepest 30d) | SHORT-GAMMA (FULLY_NEGATIVE, 6 sessions) | 741 (release shelf) | 725 / 720 cluster |
| QQQ | 695.48 | null (unreliable) | −794M | SHORT-GAMMA (FULLY_NEGATIVE, 4 sessions) | 715 (release shelf) | 700 / 690 |
| IWM | 282.70 | ~180 (1-day artifact) | −1.0B | SHORT-GAMMA (per-strike; 275/276 deep neg) | — | 279 / 275 well |

- **`uw options-flow dte-volume-share`:** 0DTE **40.9%**, weeklies 23.1%, monthlies 24.4%, LEAPs 5.0% → **RETAIL_DRIVEN** hint (the index Tech-premium "inflow" is heavily 0DTE/hedging, not institutional accumulation).
- **`uw historical vrp`:** SPY **PREMIUM_SELLING** (IV30 0.185 vs RV30 0.130, vrp +0.055); QQQ **PREMIUM_SELLING** (IV30 0.295 vs RV30 0.222, vrp +0.073). **But the front end is BACKWARDATED** (SPY 0DTE IV 1.26×VIX, QQQ 2.03×VIX) — the 30d curve favors selling while the front end is in event-panic. This split matters: it gates off the 0DTE premium-sell (§2a) and bites the LRCX sell-front-vol calendar.
- **Macro backdrop (`fred_macro`):** yield curve **normal +0.42**; core CPI 2.96% YoY (headline ~4.2–4.27%, 3-yr high, printed today); core PCE 3.29%; unemployment 4.3%; payrolls +172k; **10Y 4.53% RISING** (+0.15 30d); **USD STRENGTHENING** (+1.98 30d); fed funds 3.62%. Sticky inflation + rising rates + strong USD = a mild **risk-off** macro that aligns with the defensive tape.
- **Forward `event_risk` calendar:** **PPI May — 2026-06-11 (TOMORROW 8:30am, HIGH, front-end);** SpaceX IPO 6/12 (single-name, TSLA halo); **FOMC + SEP/dot-plot — 2026-06-17 (HIGH);** PCE May — 2026-06-25 (HIGH); + ambient US-Iran/Strait-of-Hormuz geopolitical risk. This is the densest event window of the month.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book (open interest persists overnight), read forward as the *prior* for the 6/11 open. Prose-only, **0 conviction points**, no backtested predictive claim. SPY/QQQ only.

| Index | Regime | ZGL | Call wall | Put wall | One-line next-session 0DTE bias |
|---|---|---|---|---|---|
| **SPY** | SHORT-GAMMA (FULLY_NEGATIVE, total GEX −2.51B, deepest in 30d) | null / `zgl_reliable=false` | 741 (least-negative release shelf; no true +GEX wall in range) | 725 / 720 (−359M / −329M cluster, *acceleration* strikes not absorbers) | Trend / breakout / vol-expansion. Debit verticals / directional / long straddle through the 725 flip. **Do NOT sell naked premium despite PREMIUM_SELLING VRP** — short gamma overrides for direction. |
| **QQQ** | SHORT-GAMMA (FULLY_NEGATIVE, −794M; shallower than SPY) | null / `zgl_reliable=false` | 715 (release shelf) | 700 / 690 | Trend / breakout. Front-end 2.03×VIX = very rich straddle; favor **debit verticals over outright straddles** to limit IV-crush bleed if PPI is a non-event. |

**Regime freshness:** SPY FULLY_NEGATIVE 6 straight sessions, deepening each day (−1.81B → −2.51B) — **entrenched and intensifying**, not fresh. QQQ FULLY_NEGATIVE 4 sessions (newer flip, was POSITIVE all May). The 6/11 (PPI-day) expiry carries ~$1.48B premium, put-skewed (905M put vs 572M call) — the book is hedged for downside into the print.

**Mandatory caveats:** EOD = a prior refreshed by fresh 0DTE OI in the first 30–60 min — re-pull after the open. **PPI 8:30am gap risk voids this prior** (front-end backwardated, VIX spiking). ETF book, not the cleaner SPX/NDX index book. `uw` cannot isolate the D+1 expiry — this is the standing 0–45 DTE book.

### 2a. Next-session 0DTE premium-selling setup (`zerodte_setup.py`) — **STAND ASIDE**

Both SPY and QQQ return **`sell_premium=false`, `size_scalar=0.0`** today. The rolling backtest verdict is GO_PREMIUM_SELL_INTRADAY (SPY 95.2% / QQQ 90.5% historical open-entry win rate), **but today's regime gates it off**: VIX spiking +2.4 (short-vol left-tail regime) and front-end backwardation (SPY 0DTE IV 1.26×VIX, QQQ 2.03×VIX) — the exact "stand aside" conditions. **Do not put on the delta-neutral 0DTE premium-sell tomorrow.** (Advisory, 0 points; validation sample has no vol shock → tail unsampled.)

### 2b. Swing Dealer Positioning (1–4 weeks)

`dealer-positioning-strategist` reads **SHORT across the complex** into the PPI→FOMC event wall:
- **QQQ — top-conviction swing short.** Cleanest one-way POSITIVE→FULLY_NEGATIVE flip (6/04–05), held 4 sessions; DEX −25.9B; front-end 2.03×VIX (extreme panic = tech is where the fear concentrates).
- **SPY — swing short.** Regime flip 6/01, FULLY_NEGATIVE since 6/03 (6 sessions); DEX −58B; GEX −2.5B deepest in 30d.
- **SMH — clean semis swing short.** DEX −4.6B put-heavy; persistent dealer-short gamma the entire lookback; front-end 1.70×VIX.
- **TSLA — swing short.** DEX −3.6B put-heavy + vanna AGREE; total GEX crossed negative today (clean directional agreement, unlike NVDA).
- **NVDA — SHORT-WATCH only** (DEX +4.0B call-heavy DISAGREES with vanna SHORT → disqualified clean; but GEX crossed negative today + calm CONTANGO front-end = asymmetric downside catch-up risk if it backwardates).
- **AMD — NEUTRAL** (DEX/vanna disagree, low-magnitude flip = artifact).
- **No actionable swing LONG exists** — every put-heavy book is **vanna PRESSURE, not squeeze** (rising VIX disqualifies the squeeze). The asymmetric long to watch: if VIX rolls over for ≥3 sessions post-FOMC and backwardation unwinds, SMH (put-heavy + IV-100) becomes the highest-beta relief-rally long. Not yet.

### 2c. Sector Rotation

`sector-rotation-strategist`: **`no_change` / no durable rotation.** All 9 GICS sectors posted persistence_score=1 with trend=INFLOW across 5 sessions — a *broad-tape bid fading*, not a rotation (9 of 11 sectors show negative window deltas). No sector rotating OUT to pair against an inflow leg → no canonical pattern. The Step-0 divergence (options-premium lens shows Tech +3.28B; DP/net-flow lens shows defensive-in) **resolves to the defensive/risk-off read** via the ETF tape, but magnitudes are sub-floor. **No single-name leaders extracted; no swing rotation trade.**

**ETF flow tape (advisory — 0 points):**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Note |
|---|---|---|---|---|---|---|
| **SMH** | **outflow −116.6M** | bearish | $204.8M crosses (hedge/CR) | **strong bear (18p/2c)** | disagree (Tech GICS premium = 0DTE/hedge noise) | cleanest directional ETF signal — bearish |
| EWY | outflow −33.7M | bearish | block crosses | bear (12p/8c) | n/a (Korea = semi proxy) | confirms semi de-risk |
| KRE | outflow −21.6M | bearish | institutional crosses | mixed/weak | disagree (Financials GICS +inflow) | regionals weaker than money-center |
| GDX | inflow +7.9M | mixed-bull | creation/redemption | thin | disagree | gold/defensive tilt, sub-floor |
| XLP | inflow +7.4M | bullish | single block hedge | flat | agree (Cons Defensive INFLOW) | defensive tilt, sub-floor |

Takeaway: **semis are the one place the multi-day options tape has conviction, and it is bearish** (SMH −116.6M, 18:2 puts; EWY confirms). The defensive inflow side (GDX/XLP) is trivial premium with creation/redemption DP — positioning tell only, no accumulation signal.

---

## 3. Swing Setups (1–6 weeks)

| Ticker | Score | Direction | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|---|
| **SMH** | **9 / HIGH** | **SHORT** | Dealer short-gamma (DEX −4.6B, FULLY_NEGATIVE GEX) amplifies downside into PPI/FOMC; semis led the rally, lead the de-risk; validated bearish-flow edge (+57.7pp market-excess). Distribution-trap *disproven* (DP mega/block buy_ratio 0.479/0.477 = net selling, cost basis 584 above spot). | **Bear call spread above spot** (IV rank 100 → sell rich premium, defined risk; *not* bought puts). `batch-scan` independently → Bear Call Spread. | **close > 600** (bear's own stop; SMH GEX flips +ve at 600/605/610 → dealer gamma inverts). | **HALF** (cluster-kept member; event-risk −1 for FOMC 6/17 + MU 6/24 squeeze risk above) |
| IWM | 6 / LOW | short | Multileg put debit spread (P279/P275-276 6/18, repeat 3) in deep neg-gamma well; macro corroborates (rates rising crush small-caps). | put debit spread 6/18 | close > 290 / 90d flow flips bullish | **SKIP** (cluster −1, event-risk −1; `batch-scan` says DP_ACCUMULATION → contested) |
| SPY | 5 / LOW | short | Deepest DEX/GEX, largest cum_flow in union (−1078M). | — | close > 735 | **SKIP** (weakest leg — DP accumulating +68M / $924M print *against* the short; cluster −1) |
| TSLA | 3 / LOW | short | Confirmed downtrend (−13.7%/10d), DEX −3.6B + vanna agree, GEX crossed neg; 386x PE most rate-vulnerable mega-cap multiple. | — | gap > pre-IPO high / close > 21d after 6/12 | **SKIP** until post-6/12 (fundamentals CAUTION −1; SpaceX IPO 6/12 = unhedgeable upside gap; `batch-scan` "No Edge — Stay Flat") |

**Near-term sweeps (`sweep-tracker`, informational — 0 points unless co-flagged):**
- **MRVL** — the one clean *bullish* name: 5/5 persistence, opening call build 3:1 (C300/C320), 2DTE straddles PPI. But single-agent, failed the ≥4 confluence gate → **watch-only** (§8). bullish_flow WR 0.294 / market-excess −0.386 (bullish flow lost in this risk-off tape).
- **MSTR** — bearish 3/5, opening put build (P101/P115/P100); BTC-proxy de-risk. Single-agent → watch.
- **MU** — 5/5 persistence but two-sided event straddle into 6/24 earnings (vol, not direction) → §5.
- **ORCL** — *already reported today* (+11.64% EPS beat, IaaS +93%); the Step-0 opening put was the hedge into the print, now resolving. → §5 PEAD advisory.
- Index/mega-cap sweeps (SPX/QQQ/SPY box-conversion + cum_flow MIXED) are **hedge-flow plumbing**, not directional.

> No 3b short/fade swings issued: `contrarian-scanner` found **zero** clean fades (NVDA/TSLA/AMZN bearish-extreme but flow ALIGNED with the slide = trend, not crowding; SMH PCR 4.09 debunked z −0.34 NORMAL = structural insurance).

---

## 4. LEAP Builds (6–24 months)

**None.** `leap-positioning-radar` returned **no qualifying DTE>180 build** — every single-name candidate failed a mandatory gate (conviction-matrix not DIRECTIONAL_LONG, and/or cum-premium-flow flat/negative):
- **PBR** C25 271217 (+30,417 OI, 5d build) — conviction-matrix MIXED 1.4%, DP balanced 0.486, cum-flow near-balanced. ~2 of 9 gates.
- **UNM** C105 261218 — COVERED_CALL 42.6% (net call selling + DP buying = yield enhancement). Reject.
- **SRAD** C17.5/C20 261218 — DIRECTIONAL_SHORT 54.8% (paired put build). Reject.
- **NOK** C30 270115 — chain-wide net call SELLING + cum-flow NET NEGATIVE −$26M. Reject.

The long-dated tape is defensive ETF/index put hedging (XLP/VIX/HYG put rolls, TLT 80P, IBIT 35P, FXI puts). LEAP DTE-volume share only 5.0%. Re-scan when LEAP share recovers >8–10% and breadth turns.

---

## 5. Volatility Surface

`vol-surface-scout` — the **only VRP-aligned tradeable vol dislocations** are the semis FOMC-front calendars; everything else is event-trap or 0DTE noise.

| Name | pct / z | front-ratio | Front driver | Verdict |
|---|---|---|---|---|
| **AMAT** | 100 / +3.24 | 1.82 | macro (FOMC 6/17), no Aug binary | **SELL-FRONT CALENDAR** (best): sell 6/18 (138%) / own 7/17 (75%). ~64 vol-pt decay capture. |
| **LRCX** | 97.6 / +2.81 | 1.66 | macro, late-Jul earnings far out | **SELL-FRONT CALENDAR** (back leg ≤7/17). ⚠ See §6 — gated by FOMC front-vol expansion risk. |
| **MU** | 100 / +1.56 | 1.26 | name earnings ~6/24 (kink at 7/17 = 164.6%) | **EVENT-TRAP** — calendar only, never naked. Hand to earnings (SKIP for now; bearish flow −$22.6M vs serial-beat divergence; revisit ~6/22, lean BUY VOL if kink under-prices the beat-gap). |
| SMH | 100 / +2.66 | 1.70 | basket of above; TAIL_HEDGING skew +0.056 | calendar-eligible but prefer single names; the directional short is the cleaner expression. |
| SOXL | 100 / +2.52 | 1.78 | 3x leverage of macro front (328% IV) | **AVOID** — leverage path-decay, not a sellable mispricing. |
| TER | 100 / +2.53 | 1.44 | macro | **C12 FAIL** — too thin (16–146 contracts/expiry). |

**Earnings vol (`earnings-scout`)** — no full-size SELL VOL exists (every back-month tail is COMPLACENT → all half-size, front-only kink):
- **KMX** (6/17) — **SELL VOL ¾** (best: the only name with positive back-month skew +0.033; 11.3% implied historically rich). Short 6/18 strangle/condor.
- **ADBE** (6/11 tomorrow) — **SELL VOL half** but front-end ratio 2.6 (extreme panic) → wait for the unwind to begin before shorting; ~7.8% implied, serial in-line beater.
- **ACN** (6/18), **JBL** (6/17), **KR** (6/18) — SELL VOL half (clean kinks, complacent tails).
- **MU** (6/24) — SKIP for now (too early, macro-contaminated front, beat-vs-flow divergence).
- **ORCL** — PEAD advisory (record +11.64% beat, IaaS +93%; withheld from scored lines, NO_GO per C7; verify post-gap flow before acting).

**Single-contract IV outliers:** EMPTY — every outlier is 0DTE (TSLA/SLV/UNG/QQQ) intraday gamma noise, no multi-day whale-hedge mispricing.

**Multi-leg structures (`multileg-strategist`)** confirm defined-risk downside into the two-event week: **IWM** put debit spread (repeat 3, HIGH), **HYG** credit puts (repeat 3, risk-off hedge), **EQT** put diagonal (event), **SOUN** put calendar (front-vol crush). The only bullish single-name structure (NVDA C215) is hedge-shaped, not genuine dissent.

---

## 6. Risk & Correlation

**Macro headline:** Hot CPI today (headline ~4.2% YoY, 3-yr high) into a risk-off tape; 10Y 4.53% rising, USD strengthening — every macro vector points the way the book leans (down). That alignment **is the trap**: it's one bet, not five. Breadth (`fz`) confirms — 34.6% green, no divergence.

**Forward event calendar:** PPI 6/11 (tomorrow, front-end) · SpaceX IPO 6/12 (TSLA gap) · **FOMC + dot-plot 6/17 (the named Tier-1 binary every swing structure holds through)** · MU earnings 6/24 (SMH proxy) · PCE 6/25.

**Correlation — THE dominant finding:** this is **one position wearing five tickers.** `beta_short_cluster` (30d): SMH/LRCX **0.92**, SPY/IWM 0.87, SMH/SPY 0.84, IWM/LRCX 0.82, SMH/IWM 0.79, SPY/LRCX 0.75, SMH/TSLA 0.75. SMH/SPY/IWM/LRCX form a hard cluster (all pairwise ≥0.75); TSLA cluster-linked to SMH. **Kept member = SMH** (highest raw 9); every other leg takes the mechanical **−1 tier**.

**Gates applied:**
- **Regime:** shorts are regime-ALIGNED in a risk-off TRANSITIONAL tape → no regime penalty.
- **VRP/panic:** 30d PREMIUM_SELLING doesn't help delta shorts (no-op on SMH/SPY/IWM/TSLA). **But the backwardated front bites LRCX** — a sell-front-vol calendar into a backwardated curve with PPI + FOMC inside the sold leg is the wrong vega sign → **−1**.
- **Fundamentals:** SMH/IWM/SPY **NA** (ETFs, never penalize); **TSLA CAUTION −1** (SpaceX IPO + JPM +227% target + oversold late entry); **LRCX CAUTION −1** (upgrade cascade + front-vol expansion). **No VETOs.**
- **Event-risk:** −1 on every directional short (FOMC 6/17 in-horizon; TSLA SpaceX 6/12).
- **Debate (short theses → disconfirmer=bull, trade-side=bear):** SMH bull 0.55 < bear 0.75 → **clears, no cut**. TSLA bull 0.55 < bear 0.65 → clears narrowly; both agree "mistimed not wrong" (captured by CAUTION + event gates).

**Adverse-flow exit list (vs `conviction_2026-06-09`):** **MSFT** flow bearish −30.7M (confirms yesterday's DISTRIBUTION flag — stays off-book); **SNDK** bearish −20M, decayed off-thesis; **SPY** DP *accumulating* +68M / $924M print + huge OI build = adverse to the SPY short → first leg to trim. IWM mixed (no exit tag).

**Hedge sleeve:** book is ~0.9 net short beta with **no long ballast against a squeeze**. Dominant tail = dovish-FOMC / cool-PPI relief rally. **Recommended: SPY 730/745 call vertical, expiry 6/19** (covers PPI + FOMC), sized ~25–30% of cluster net short delta. Buy upside convexity — do NOT add short-vol (VIX already 22 spiking); do NOT hedge with QQQ (inside the cluster).

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no fresh per-tier expectancy table from a cleared `/calibration-audit` this run (last audit 2026-06-06 flagged short-alpha compression +19.7→+6.0pp; re-audit ~06-12). The live sizer remains the win-rate ladder (Step 5).

Only one name clears raw ≥ 7:

### SMH — raw 9 — HIGH — SHORT — final size **HALF**
| Field | Value |
|---|---|
| **score_components** | +3 dealer-positioning DEX (`uw options-structure dex`, −4.6B put-heavy FULLY_NEGATIVE) · +2 signal-confluence=4 (`uw insights signal-confluence`, bearish) · +1 sector-rotation leader (`sector-flow-persistence`, semis ETF −116.6M, all 3 gates) · +1 cum-flow accretion (`cumulative-premium-flow`, −50.8M aligned, intent-screened) · +1 vol-surface (`term-skew`, IV-100 TAIL_HEDGING) · +1 OI build puts (`oi-trend`, P515/525 BUILDING) = **9** |
| **dominant_signal_class** | dealer_positioning (bearish) |
| **win_rate** | 0.80 (raw 0.897, N-capped) · n=29 · backtest (bearish_flow) · **market-excess +0.577** (genuine alpha, not beta) |
| **cum_premium_flow** | 30d −$50.8M / 90d −$192.3M |
| **fundamentals_verdict** | NA (ETF) — key risk: MU 6/24 beat-streak *fights* the short |
| **bull/bear residual** | bull (disconfirmer) 0.55 / bear (trade-side) 0.75 → short cleared |
| **gate_verdicts** | regime: no-op (aligned) · vrp: no-op (delta) · panic: no-op · cluster: KEPT member · sector: no-op · fundamentals: NA · **event_risk: −1 (FOMC 6/17 + MU 6/24)** · debate: no-op |
| **final_size** | **HALF** (HIGH/full pre-risk → halved by event-risk + the joint-cluster cap) |
| **structure** | Bear call spread above spot (IV-100 → sell rich premium, defined risk). Confirmed by `batch-scan`. |
| **invalidation** | close > 600 (SMH GEX flips +ve 600/605/610 → dealer gamma inverts) |

**LB-gate (Step 3a):** SMH cites 3 of 5 load-bearing tools (cumulative-premium-flow ✓, options-structure dex ✓, signal-confluence ✓) → **HIGH tier preserved.**

**LOW-tier supporting candidates (raw 3–6, all SKIP/watch via gate stack):** IWM (6), SPY (5), TSLA (3), LRCX (3 vol) — see §3/§5/§6. All gated to skip: same SMH short at worse entries, contested by DP accumulation (IWM/SPY), event-trapped (TSLA), or wrong vega sign (LRCX).

**Deep-dive hand-off:** `Recommended deep dive: /stock-deep-dive SMH` (stock-deep-dive skill not available in this session — run manually).

### Conviction scoring rubric (Step 4, verbatim for audit)
```
+3 dealer-positioning DEX flip or vanna-squeeze in trade direction
+3 3+ aligned accumulation signals — CONJUNCTION: full +3 only if cum_flow_30d confirms (sign aligned AND |cum_flow_30d|≥$50M); else halved to +1
+1 multi-day OI build (oi-trend BUILDING ≥5d)
+1 conviction-matrix DIRECTIONAL_LONG conf>70 — CONDITIONAL: only if dominant_signal_class==leap_directional, else 0
+1 cum-premium-flow net directional accretion (30d) — INTENT-SCREENED: no distribution_flag, no dividend-capture arb
+2 signal-confluence ≥4 (second-agent confirmation)
+1 sector-rotation single-name leader — CONDITIONAL: persistence≥0.6 AND cum_flow_30d aligned AND |cum_flow_30d|≥$50M
+1 earnings-scout BUY VOL or SELL VOL
+2 multileg-strategist directional structure (term-structure-anchored)
+1 vol-surface KINKED/BACKWARDATION with VRP-aligned bias
-2 contrarian overcrowded long w/ rising pc-ratio-zscore (VRP positive)
-3 flow_conflict (cum_flow_30d clearly opposite dominant_signal_class)
-1 flow_conflict_lite (MIXED 30d cum_flow) — mutually exclusive with flow_conflict
[gamma-flip 0DTE setup = 0 points by design — §2 advisory only]
Tiers: ≥9 HIGH (full) · 7-8 MEDIUM (half) · 3-6 LOW (starter/watch) · ≤2 drop
```

---

## 8. Watch-only — single signal, no confluence

Surfaced from one agent but failed the confluence gate (≥2 agents OR 1 agent + signal-confluence ≥4). Journaling only, **not for trade entry today.**

| Ticker | Source | Signal | Why watch-only |
|---|---|---|---|
| **MRVL** | sweep-tracker | bullish 5/5 persistence, opening call build 3:1 | Single-agent; failed ≥4 confluence gate; bullish_flow market-excess −0.386 (lost in risk-off tape). The one clean bull name — watch for confluence. |
| **MSTR** | sweep-tracker | bearish 3/5, opening put build | Single-agent; BTC-proxy de-risk. |
| **NVDA** | dealer-positioning / accumulation | SHORT-WATCH (DEX/vanna disagree); C28 230C closing $48.3M | Disqualified clean (conflicted signals); calm CONTANGO front = downside catch-up risk if it backwardates. |
| **QQQ** | dealer-positioning / gamma | swing short (DEX −25.9B) but −1 flow_conflict_lite (cum_flow bottom-quartile) | Raw 2 — dropped; carried as the §2b top-conviction swing-short read, but the scored line failed the floor. |
| **MSFT** | accumulation (C28) | **DISTRIBUTION flag** — call OI closing $51M @500C/575C + DP net-selling 0.375 | Distribution-dressed-as-accumulation. NOT a long; hand to fundamentals as CAUTION/VETO support. |
| AMAT / ADBE / KMX | vol-surface / earnings | calendar / sell-vol | Valid vol-structure ideas (§5), not directional-conviction scored. |
```
