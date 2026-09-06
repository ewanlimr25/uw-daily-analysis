# Daily Market Analysis — 2026-06-24

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL / PULLBACK_IN_UPTREND. SPY 733.24 (below 20sma 745.69, above 50sma 732.97; −3.57% from 90d high). SPY **and** QQQ dealer books are **FULLY_NEGATIVE / short-gamma** (amplification, not pinning) with null ZGL. VIX 18.63. Flow breadth **bearish (35.6% bullish)** even as price breadth is 64% green — a distribution-into-strength divergence. Sector tape: broad inflow, no clean rotation.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL/PULLBACK_IN_UPTREND) — sizing capped at half`.
- **Next-session GEX (SPY/QQQ):** SPY short-gamma, soft upside lid 736–737, downside −GEX shelf 735/730 → 720 support stack. QQQ short-gamma, upside magnet 720–723, heavy −GEX shelf 715 right under spot → 705–700. Both **freshly flipped & unstable**; PCE can void the prior on a gap. Advisory, see §2.
- **Top swing build:** **NONE.** Zero names cleared the conviction rubric. The single confluence-gate name (SPCX) dropped at raw −3 (flow_conflict). Stand aside.
- **Top LEAP candidate:** **NONE.** Zero DTE>180 directional-long builds cleared the 6-of-9 gate (thin LEAP tape, 5.5% DTE share).
- **Biggest risk:** ⚠ **Core PCE (May) releases TOMORROW, Thu 2026-06-25** (Fed's preferred gauge, sticky at 3.29% YoY) into a FULLY_NEGATIVE short-gamma book with front-end IV panic (SPY 1.31 / QQQ 1.57 backwardation). Semis cluster NVDA/SMH corr 0.917. **Desk posture: FLAT into the print.**

> **NO-EDGE / STAND-ASIDE DAY.** Three independent hard gates fire before sizing even begins — front-end panic (>1.10 both indices), a Tier-1 PCE print at T+1, and a fundamentals VETO on the one "clean" accumulation name. This is the mechanically correct call, not a discretionary one. §3/§4/§7 are intentionally empty; §1/§2/§5/§6/§8 carry the actionable context.

---

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend **PULLBACK_IN_UPTREND**. SPY 733.24, below 20sma (745.69), above 50sma (732.97); 30d −1.66%; −3.57% from 90d high. Breadth (flow): **35.6% bullish** (2,221 bullish vs 4,021 bearish of 6,242 optionable). Guidance: half size, defined-risk, iron condors in range.
- **Per-index gamma (EOD current-state book):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 733.24 | null (FULLY_NEGATIVE) | −0.78B | short-gamma | 736–737 (soft) | 720 (−GEX shelf) |
| QQQ | 713.43 | null (FULLY_NEGATIVE) | −0.24B | short-gamma | 720–723 (soft) | 715 → 705–700 |
| IWM | — | NEGATIVE (whipsaw) | — | short-gamma | — | — |

  Both index books **flipped POSITIVE→FULLY_NEGATIVE on 06-22/06-23** and are only 2–3 sessions old (unstable). §2 carries the forward next-session read.
- **`uw options-flow dte-volume-share`:** 0DTE 36.7%, weeklies 24.1%, monthlies 20.9%, LEAPs 5.5% — **BALANCED** with a mild retail tilt.
- **`uw historical vrp`:** SPY **FAIR** (IV30 16.7% vs realised 15.0%, VRP +1.71%); QQQ **FAIR** (IV30 28.7% vs realised 27.6%, VRP +1.09%). No clean index-level premium edge.
- **Macro backdrop** (`fred_macro` `macro_snapshot`): yield curve **normal** (10Y−2Y +0.30, no inversion); core CPI **2.96%** / core PCE **3.29%** YoY (sticky, above target); unemployment 4.3%, payrolls +172k; 10Y **4.50% (falling)**; USD **strengthening**; fed funds 3.63%. **Forward `event_risk`:** ⚠ **Core PCE (May) — Thu 2026-06-25 (T+1, high)**; NFP + jobless claims — Thu 2026-07-02 (T+6, high). The 06-25 print is the single most important catalyst on the board.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal — prose-only, 0 rubric points, no backtested predictive claim.** EOD dealer-gamma book read forward as the *prior* for tomorrow's open. SPY/QQQ only.

Both indices enter tomorrow **short-gamma, FULLY_NEGATIVE, ZGL null (`zgl_reliable=false`)** — dealers are positioned to **amplify** moves, not dampen them. The regime is **freshly flipped (06-22/06-23) and unstable**, so conviction in the trend read is lower than a held negative book.

| Index | Regime · ZGL | Call wall | Put wall | One-line next-session bias |
|---|---|---|---|---|
| **SPY** | short-gamma · ZGL null (total_gex −0.78B) | 736–737 (thin local magnet, soft lid ~0.5% up) | 735/730 −GEX shelf → **720 support stack** (−1.8%) | Defined-risk **directional/debit over premium-selling the pin**. A break below 730 gets sold toward 720; a poke above 736–737 can extend. |
| **QQQ** | short-gamma · ZGL null (total_gex −0.24B) | 720–723 (soft cap ~1% up) | **715 shelf right under spot** → 705–700 (−1.9%) | Same: a break of 715 amplifies toward 705–700. 0DTE put-premium tilt + front-end backwardation argue **defined-risk directional, not pinning**. |

**Mandatory caveats:** EOD is a **prior, not a target** (re-computed by fresh 0DTE OI in the first 30–60 min). **ZGL null on both** (FULLY_NEGATIVE) → read off the total_gex sign + spot-vs-wall, not a crossover level. ⚠ **PCE (May) tomorrow can gap spot through the walls and void the prior entirely** — the 06-25 expiry already carries meaningful OI, so post-print repricing is likely. These are the **SPY/QQQ ETF** books (noisier, more retail-tilted than SPX/NDX). uw-pp cannot isolate the D+1 expiry — this is the 0–45d aggregate proxy.

### 2a. Next-session 0DTE premium-selling setup (`zerodte_setup` — the validated stack)
> Advisory, delta-neutral, **0 rubric points**. NOT a guaranteed edge — the validation sample has no vol shock, so the short-vol left tail is **UNSAMPLED**.

Rolling backtest **verdict: GO_PREMIUM_SELL_INTRADAY** (SPY win 94.1%, QQQ 90.2% on the open-entry, hold-to-close, never-overnight rule). **PnL basis = % of underlying spot notional, GROSS** — lead with net:

| Index | Sell premium? | VIX / vol-state | Implied move | Expected range | Size | Net PnL/day | Structure |
|---|---|---|---|---|---|---|---|
| **SPY** | yes (script) | 18.63 / MID | 1.16% | 1.2% | 1.0× | **+0.216%** (gross +0.316%) | Wider iron condor, wings ≈ ±1.2% |
| **QQQ** | yes (script) | 18.63 / MID | 2.25% | 1.86% | 0.5× | **+0.32%** (gross +0.42%) | Wider iron condor, wings ≈ ±1.86% |

**Desk overlay — stand aside or size down into PCE:** the script's GO verdict is the rolling-history read; the *live* setup sits one session before a Tier-1 print into a FULLY_NEGATIVE short-gamma book. **Hold dry powder through the 06-25 open; if traded, half-size and enter only after the gap resolves.** QQQ additionally carries **front-end backwardation** (0DTE IV ≈ 1.92× VIX) — event/gap risk, half size. **SPY ≈ SPX** (trade either); **QQQ weaker** (lower confidence). Direction: **none** — delta-neutral; do not tilt.

### 2b. Swing Dealer Positioning (1–4 weeks)
`dealer-positioning-strategist`: the dealer complex **de-risked into negative gamma + negative DEX on 06-22/06-23** across SPY/QQQ/SMH — a clean, multi-day, mechanically-valid sign change confirmed by three lenses (per-symbol DEX sign, total-GEX regime, per-strike dispersion). **But no scored +1 DEX-flip line fires today:** the flips are valid yet **stale** (occurred 06-22/06-23, not on the latest 06-24 session — the rubric requires the flip ON the latest session). Every put-heavy book is **"vanna pressure, not squeeze"** because VIX is *rising* (16.40→17.28→19.49→18.63), disqualifying the falling-VIX leg. Front-end-iv-ratio: SPY 1.31 / QQQ 1.57 / SMH 1.63 — deep backwardation, front panicked.
- **SPY/QQQ/SMH swing_bias: SHORT/neutral-bearish** — dealers now sell into weakness.
- **MU:** euphoric call book unwinding fast (DEX +51.5B→+10.6B in 4 sessions post a +14% run); a positive *level* in a fading tape, explicitly **not** a flip → neutral/short-leaning.
- **IWM/META/ORCL:** whipsaw, no clean thesis → neutral.
- **Re-arm the LONG vanna-squeeze only if** VIX prints a 3-session lower run post-PCE while the books stay put-heavy.

### 2c. Sector Rotation
`sector-rotation-strategist`: **rotation_regime = no_change (low confidence).** All 11 sectors cleared the absolute ≥0.6 persistence gate (5 at 1.0, 4 at 0.8) — in a broad-inflow tape the absolute gate discriminates nothing, and the market-relative bar (top-third persistence AND above-median 1d magnitude) admits **only Industrials** (+$284M, persistence 1.0). **But XLI ETF shows 5d OUTFLOW** — a GICS-vs-ETF disagreement that downgrades even that one call to watch-grade. **Tech is decelerating hard** (+9.36B→+6.76B→+3.85B→+2.38B across the week, −75%): still 5d-net-inflow but late-stage, with INTC/MSFT/AMD/SNDK already de-risking inside it — **fade Tech bounces, don't chase.**

**ETF flow tape (advisory):**

| ETF | Net prem dir (5d) | Persistence | DP positioning | Options urgency | GICS agreement | Leaders |
|---|---|---|---|---|---|---|
| SMH | inflow +128.3M | BULLISH | $266M print = creation/redemption tell, **not** accumulation | **put-heavy sweeps (hedging)** | disagree (XLK MIXED) → **watch** | MU, LRCX, AMAT |
| GDX | inflow +42.3M | BULLISH | heavy creation prints | put-heavy (hedged) | n/a (gold thematic) | AEM, NTR |
| IGV | inflow +6.5M | MIXED | large prints | **call-heavy sweeps (genuine urgency)** | disagree (XLK MIXED) → watch | ORCL, software |
| XLV | outflow −5.1M | BEARISH | small prints | thin hedge unwind | agree (HC fading) | — |
| XBI | outflow −4.4M | MIXED | small prints | call-heavy (contrarian bid) | disagree → watch | — |

**Critical cross-check:** the two largest inflow ETFs (SMH, GDX) show **put-heavy sweeps against bullish 5d premium** = creation/redemption + protective hedging, **not** directional accumulation — not elevated to conviction. The tape **strengthens** the conditional sector-leader +1 only; it adds **no rubric points**.

---

## 3. Swing Setups (1–6 weeks)
**EMPTY — zero names cleared the conviction rubric.**

Only one name cleared the ≥2-distinct-agent confluence gate (**SPCX**, flagged by sector-rotation + sweep-tracker), and the quant **dropped it at raw_score −3**:
- −3 **flow_conflict**: 30d cum-premium-flow **−$304.9M** opposes the long thesis (12× the union-median magnitude; 90d net identical, so the contradiction is current, not a stale artifact).
- Sector-leader +1 **zeroed**: gate (b) fails (cum-flow opposes) and the XLI ETF 5d-outflow disagrees with the GICS single-name inflow.
- The OI "build" is verified **deep-OTM 2-DTE lottery calls** (300C/275C at ~$0.10 on a $154 stock, price −16% on the week) — lottery flow, not institutional conviction. Fundamentals (NA) + news corroborate a **crowded post-IPO unwind** (>$600B erased in a week, P/S ~109x).

Class-level `bullish_flow` win-rate (clean protocol): **0.558** (n=138), market_excess **−0.094** vs same-window SPY-long — i.e. **beta with no selection edge**, half-size at best even before the drop. No sweeps, accumulation, multileg, or LEAP build produced a second confirming agent on any sized-able name.

### 3a. Long swings — none.
### 3b. Short / fade swings — none sized. **IREN** is carried as a bearish *watch* only (§8): a Tier-1 OPENING_PUT_PRIME single-leg whale (advisory C19, 0 points) + contrarian continuation flag, borrow-constrained (17% short float) — but single-agent and not a defined-risk fade into PCE.

**Near-term sweeps (informational, 0 points):** the entire persistent-sweep board is index/mega-cap **hedge-flow** (SPXW/QQQ/SPY/TSLA/NVDA/MSFT/IWM/META all 5-of-5 persistence but cum_flow_30d MIXED — not directional). Only SPCX (lottery, dropped) and SNDK (52-day build but today put-leaning, conflicted) carried single-name persistence.

---

## 4. LEAP Builds (6–24 months)
**EMPTY — zero qualifying builds.** A thin-LEAP-tape day (5.5% DTE share) produced no DTE>180 directional-long clearing the 6-of-9 gate. The long-dated tape is dominated by rate/bond-ETF put hedges (TLT/LQD/FXI/KWEB), index protection, and penny/meme names below the quality floor.
- **NVDA** (2/9) — isolated 358-DTE 205C ask-side line, BUT 90d cum-flow **−$374M (distribution)**, conviction-matrix MIXED 9.1%, DP sell-side. Reject.
- **ORCL** (1/9) — lone 576-DTE put, 90d −$255M MIXED. Reject.
- **AAPL** (0/9) — conviction-matrix **DIRECTIONAL_SHORT** 28.6%; LEAP line was a neutral straddle. Reject.
- Rolls cross-check: only IGV (software-ETF put roll) and SPXU (inverse-S&P call roll) cleared balance — both **hedge/defensive**, not directional longs.

---

## 5. Volatility Surface
The IVR=100 semis cluster (INTC, TSM, STX, KLAC, COHR, ADI, TXN, AEHR, NBIS, …) is **mechanically BACKWARDATION** with the front bulge landing on the **2026-06-26 expiry = PCE day** — this is **macro front-end premium, not idiosyncratic event premium** (none appear in the earnings screen). Per the substrate-hygiene rule, bare backwardation before a macro print is ~zero-signal.

- **No live vol trade to initiate today.** Every dislocation has FEIR *rising* into PCE (STX 1.105, NBIS 1.132, TSM 1.103) — the disqualifier stack (BACKWARDATION + FEIR>1.10 rising + pending event) fires across the board. **Do not initiate short premium into the print.**
- **Single-name semis carry positive VRP → structural SELL-VOL bias** (STX +0.25, AEHR +0.23 richest) — but **gated to post-PCE**. **SMH is the exception (VRP −0.016) — do NOT sell premium on the index hedge.**
- **The one actionable single-name event vol play — NKE (earnings 2026-06-30, T+6): SELL VOL, HALF size** (`earnings-scout`). Only name with a real isolated kink AT the print (07-02 weekly 84.2% IV vs ~58% adjacent, clears the contract floor) over-pricing a ~12.5% move. **Half, not full:** the back-month 25Δ skew is flat/complacent (the tail isn't priced alongside the event) and the 07-02 print skew is negative (calls bid) against bearish net flow — a real flow-vs-positioning divergence. Structure: short 07-02 ATM straddle capped as a short iron condor (e.g. −39P/−45C, +36P/+48C). **Single-agent → watch-grade, not a sized book line.** Invalidation: FEIR climbs >1.10 pre-print, or the 84.2% kink dissipates, or the skew flips to put-bid.
- **Post-PCE re-check (2026-06-25):** if FEIR on STX/COHR collapses while back-month IV holds, the **06-26→07-17 calendar (COHR cleanest, FEIR already 1.02)** opens up.

---

## 6. Risk & Correlation
**`macro_snapshot` headline:** sticky core PCE 3.29% / core CPI 2.96% YoY, normal curve (+0.30), 10Y 4.50% falling, USD strengthening, fed funds 3.63%. **Forward `event_risk`: ⚠ Core PCE (May) Thu 2026-06-25 (T+1, high); NFP + claims Thu 2026-07-02 (T+6, high).**

**`breadth_cross_check` (fz, advisory):** price breadth **64% green** (321 adv / 179 dec, avg +0.71%) vs flow breadth **35.6% bullish** — a **distribution-into-strength divergence** (price up, options flow bearish/hedging). No hard divergence flag (pct_green > 50), but the split is a hedging tell that reinforces the stand-aside.

**Correlation clusters (`uw risk portfolio-correlation`, 30d, advisory — nothing sized):**

| Pair | Corr | Note |
|---|---|---|
| **NVDA / SMH** | **0.917** | semis are one bet — and they point opposite ways (NVDA multileg-bull vs SMH dealer-short) → a near-fully-offsetting non-position |
| NUVL / RCL | 0.881 | cluster (NUVL VETO'd anyway) |
| NVDA / RCL | 0.728 | cluster |
| NVDA / IREN | 0.663 | soft watch |
| BJ | neg-corr to SMH (−0.64) / IREN (−0.51) | the only genuine diversifier |

**Gate stack — all 9 keys (book-level, justifying stand-aside):**
- `regime`: −1 tier (TRANSITIONAL/PULLBACK, below-20sma, 35.6% bullish — half-size guidance, no long conviction clears)
- `vrp`: no-op (positive-VRP favors short-vol, but no sized vol structure survived)
- `panic`: **−1 FIRES** (front-end-iv-ratio SPY 1.31 / QQQ 1.57 backwardation, both >1.10)
- `cluster`: semis {NVDA 0.917 SMH} + {NUVL 0.881 RCL} flagged; advisory (nothing sized)
- `sector`: no-op (semis unwinding noted; no candidate cleared a rotation tag)
- `fundamentals`: **NUVL VETO** (GSK tender arb-cap) → watch-only; BJ CAUTION −1 (insider −20.77 + single-print); SPCX NA
- `event_risk`: **−1 FIRES** (PCE May = T+1, Tier-1, inside any horizon; trade is not the event play)
- `debate`: n/a (no rubric-eligible name to debate)
- `rubric_regime`: capped half (OUT-OF-REGIME — rubric 2026-06-12 fitted UPTREND, current TRANSITIONAL, <30 post-freeze calls)

Three independent hard gates (panic, event_risk, fundamentals-VETO) converge on **skip**.

**Adverse-flow scan** on carried `conviction_2026-06-23 = [MU, SPY, IWM, INTC, NFLX]`: **zero exit candidates.** Bearish names (INTC −$59.5M, NFLX, IWM) had flow *confirm* their thesis; bullish names (MU +$26.1M, SPY) held direction (MU IVR 93 = watch for vol unwind). `fz` fundamentals-drift tripwire **clean** (MU target *raised*, no short-float spikes / target cuts).

**Hedge sleeve / posture:** the book carries **no net delta** → no mechanical hedge required. **Primary: stay flat / hold dry powder through PCE.** If residual index exposure must be carried overnight, a small defined-risk **SPY put vertical** (~733/720, post-Thu expiry, ≤0.25% NAV) expresses the short-gamma gap risk. **Do NOT buy outright VIX calls / front straddles** — front-end IV is already rich (you'd pay the panic premium); favor premium-selling only *after* the front-end-iv-ratio falls back below 1.0 post-print.

**Watchlist write-back:** `conviction_2026-06-24 = [BJ, SMH, IREN]` (read-back verified). Excluded: NUVL (VETO — arb-capped), SPCX (distribution drop). Rationale: no conviction names today; persisted the strongest *diversified* forward-watch set (BJ neg-correlated to SMH/IREN) so tomorrow's RM has a meaningful adverse-flow scan target.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**EMPTY — no HIGH or MEDIUM tier names today.** Zero sized calls.

**Expectancy lens (advisory — C31):** not applicable — no resolved per-tier book to display this session (stand-aside). `[advisory — expectancy is not yet a live sizing axis]`

> **Conviction-scoring rubric (frozen, version `2026-06-12`) — embedded for audit:** Daily score = Σ: +1 mechanized DEX flip/vanna-squeeze in trade direction; +3 (→+1 if cum_flow_30d non-confirming) 3+ aligned accumulation signals (DP+OI+smart-positioning, block-stratified institutional); +1 multi-day OI build (BUILDING, ≥5d); +1 conviction-matrix DIRECTIONAL_LONG >70 (LEAP-context only); +1 cum-premium-flow net directional accretion 30d (intent-screened); +1 sector single-name leader (persistence≥0.6 ∧ cum_flow aligned ∧ ≥$50M); +1 earnings BUY/SELL VOL; +2 multileg directional (term-structure-anchored); +1 vol-surface KINKED/BACKWARDATION VRP-aligned; +1 OPEX top-5 pin (OPEX week only); −2 contrarian overcrowded-long w/ rising pc-ratio-zscore (informed-flow continuation); −3 flow_conflict (cum_flow_30d clearly opposite class) / −1 flow_conflict_lite (MIXED). Tiers: ≥9 HIGH (full), 7–8 MEDIUM (half), 3–6 LOW (watch), ≤2 drop. Gates (risk-monitor, tier-level): regime/cluster/panic/VRP/fundamentals/event-risk/debate/rubric_regime. **OUT-OF-REGIME guard active → all sizing capped at half.**

---

## 8. Watch-only — single signal, no confluence (NOT for trade entry)
Surfaced by one Phase-1 agent (or contested across agents); listed for journaling. Fundamentals verdicts attached where run.

| Ticker | Dir | Flagged by | Fundamentals | Watch note |
|---|---|---|---|---|
| **NUVL** | long | accumulation-hunter (mega 100% DP buy, LEAP OI build, conf 73.4) | **VETO** | **Not accumulation — closed GSK tender at $124** (stock $123.58). The DP buy + OI build is **merger-arb, upside structurally capped, zero directional alpha**. Earnings 4/4 miss + insider MSPR −26.84 corroborate. If it ever re-surfaces as a "directional long," kill it. |
| **BJ** | long | accumulation-hunter (single $23.3M mega block, conf 82.8) | **CAUTION** | Genuine quality (3/3 beats, ROE 26.6%, +17.7% to target, analyst-aligned, low beta 0.22) **but** insider selling (MSPR −20.77) + **single-print dependency**. Cleanest of the watch set; no imminent earnings (08-20, +57d). DP support $86.50. |
| **NVDA** | long (contested) | multileg-strategist (bullish Sept/Oct diagonal ~$49M, +2-eligible) | NA | **CONTESTED**: the bullish diagonal is contradicted by accumulation/leap/sweep all reading **distribution** (mega DP sell-side, 90d cum-flow −$374M, two-sided hedge). Confluence gate correctly held it out. Watch. |
| **SMH** | short | dealer-positioning (swing_bias SHORT, semis IVR 100 unwinding) | — | Bearish-lean dealer read; put-heavy hedging book. If sized tomorrow, express vs SOXX/sector (semis' negative-selection short history). Carried to watchlist. |
| **IREN** | short | single-leg whale Tier-1 OPENING_PUT_PRIME (C19 adv) + contrarian RISK | — | Informed opening put ($57P Jul, size/OI 16.9, +26pp backtest), **borrow-constrained** (17% short float, 1.25 days-to-cover) → respect the short, **not** a fade. Carried to watchlist. Advisory C19, 0 points. |
| **NKE** | vol-short | earnings-scout (SELL VOL half, isolated kink) | — | §5 event-vol play (earnings 06-30). Single-agent → watch-grade, not a sized line. |
| **SNDK** | long (conflicted) | sweep-tracker (52-day OI build) vs sector-rotation (Tech de-risk −$31.2M) | — | Internally conflicted (5d bullish-net but today put-leaning; sector tags bearish). Watch. |
| **RCL** | long | multileg-strategist (bullish diagonal, side-ambiguous put leg) | — | Low conviction (put leg flipped ask→bid between sessions). Watch. |
| **SPCX** | long (dropped) | sector-rotation + sweep-tracker (confluence ✓ but quant-dropped) | NA | Raw −3 (flow_conflict). Crowded post-IPO unwind (−35% in a week, P/S ~109x); lottery-call build, not accumulation. Quant correctly dropped. |

---

*Generated by /daily-analysis — 2026-06-24. NO-EDGE / stand-aside day: 0 sized calls. Phase 1 = 10 alpha-finders (no OPEX agent); Phase 2 = quant → fundamentals-gate → risk-monitor (debate N/A). Rubric frozen `2026-06-12`, OUT-OF-REGIME half-cap active.*
