# Daily Market Analysis — 2026-08-27

## Executive Summary

- **Regime + GEX state:** TRANSITIONAL (trend UPTREND). SPY 771.10 **+0.66%**, QQQ +1.37%, VIX 14.51 (−4.6%). But **RSP equal-weight −0.30%** and **10 of 11 sector ETFs red** — `fz` breadth **30.2% green (152 adv / 349 dec)**, median S&P constituent −0.65%. SPY next-session book is contradictory (label NEGATIVE vs `total_gex` **+$690M**); QQQ is coherently long-gamma, spot pinned on its ZGL. Sector lean: Technology netted IN +$500.3M, and that is the entire tape.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** SPY — regime **contradictory**, ZGL 774.33, call wall 771 (0.06% away), put wall 760 → defined-risk only, no naked straddle sale. QQQ — **long-gamma**, ZGL 719.16 (spot 720.00), call wall 730, put wall 700 → pin/mean-revert lean. Advisory, see §2.
- **Top swing build:** **None.** No name reaches the `raw_score ≥ 3` LOW cut. Highest score on the board is GOOG at **2**.
- **Top LEAP candidate:** **None.** Zero names cleared the 6-of-9 LEAP gate; the DTE>180 book is protective puts and covered-call *selling* on AAPL/NVDA.
- **Biggest risk:** the one the fleet did **not** take — a narrow, single-sector melt-up on 30.2% breadth reads as a rally on the index print and as distribution underneath it. The tightest correlation on the board (**MU/SNDK 0.905**) would have been one position expressed twice, shorting the exact complex NVDA named as the binding AI bottleneck. No hedge sleeve: the sized book is empty, so book delta is zero.

> **37th consecutive empty daily board.** Last sized daily was **2026-07-07**. Re-derived by globbing `analyses/daily/*/decision.json` only, counting `full`/`half`/`starter` as sized (`veto` rows are not positions).

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — "Half position sizes. Favor defined-risk strategies."** Trend UPTREND; SPY 771.10, above both the 20d (768.10) and 50d (753.39) SMA, +5.71% on 30d, −1.06% from the 90d high. `uw` market breadth: **36.1% bullish** (2,271 bullish vs 4,013 bearish flow tickers of 6,284).

**The tape framing is the story, and it is outcome-relevant.** The index is green; the market is not.

| Instrument | 1d | 5d | Read |
|---|---|---|---|
| SPY | +0.66% | +1.11% | cap-weighted green |
| QQQ | +1.37% | +1.43% | cap-weighted green |
| **RSP (equal-weight)** | **−0.30%** | +0.53% | **the median stock fell** |
| IWM | +0.29% | +0.72% | flat |
| XLK | **+3.16%** | +3.01% | the only green sector |
| XLP / XLV / XLY / XLC | −1.38 / −1.13 / −1.09 / −1.07 | — | **10 of 11 sectors red** |

The entire index gain is a software/semis **earnings reaction**: OKTA +28.63%, CRM +22.58%, CRWD +20.50%, PANW +12.83%, NOW +10.04%, S +10.73%, IGV +7.74%, plus NVDA +8.74%, SOXL +5.53%, AVGO +4.49%, SMH +3.10%. Strip those and the session is broadly distributive.

**Per-index gamma (current-state EOD book):**

| Index | Spot | Zero-gamma | Total GEX | Regime label | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 770.55 | 774.33 | **+$690.0M** | NEGATIVE ⚠ *contradicts its own sign* | 771 (+0.06%) | 760 (−1.37%) |
| QQQ | 720.00 | 719.16 | +$1,152.9M | POSITIVE ✓ agrees | 730 (+1.39%) | 700 (−2.78%) |
| IWM | — | — | −$0.56B DEX | choppy, 7-of-10 sessions negative | — | — |

**`uw options-flow dte-volume-share`:** 0DTE 24.0% · weeklies 32.7% · monthlies 25.0% · LEAPs 3.6% → **BALANCED**. No retail-dominance tell, no institutional-positioning tell. It neither upgrades nor downgrades today's calls.

**`uw historical vrp`:** SPY IV30 11.84% vs realised 12.29% → **−0.0044, FAIR**. QQQ IV30 17.71% vs realised **21.46%** → **−0.0375, NEGATIVE**. Realised exceeds implied on QQQ: **premium selling has no VRP tailwind today; buying is marginally favoured.**

**Macro backdrop** (`scripts/fred_macro.py`): curve **normal** (10Y−2Y +0.47); core CPI **2.79%** YoY, core PCE **3.34%** YoY — sticky, above target; unemployment 4.1% with payrolls **−23k MoM (contracting)**; 10Y 4.66%, flat on 30d; USD weakening; fed funds 3.63%. **Mildly stagflationary — sticky inflation against a contracting labour print.** That is the macro least friendly to the narrow, high-multiple growth melt-up that carried the index today.

**Forward event risk** (trading days from 2026-08-27):

| Event | Date | Offset | Tier |
|---|---|---|---|
| JOLTS (Jul) | 2026-09-02 | T+4 | medium |
| Jobless claims | 2026-09-03 | T+5 | low |
| **Nonfarm Payrolls (Aug)** | 2026-09-04 | **T+6** | **TIER-1** |
| Labor Day — closed | 2026-09-07 | — | — |
| **PPI (Aug)** | 2026-09-10 | **T+9** | **TIER-1** |
| **CPI (Aug)** | 2026-09-11 | **T+10** | **TIER-1** |
| **FOMC + SEP** | 2026-09-16 | **T+13** | **TIER-1** |
| Monthly OPEX | 2026-09-18 | T+15 | — |
| Core PCE (Aug) | 2026-09-30 | T+23 | TIER-1 |

Nothing Tier-1 sits inside T+3. What matters is the **stack**: four dated Tier-1 binaries inside any 2–4 week swing horizon.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book (OI persists overnight) read forward as the *prior* for the next open. **Prose-only, 0 rubric points, no backtested predictive claim.** Predictive validation lives in `/weekly-analysis`'s rolling §2 backtest, which has previously returned **NO_GO on walls-as-magnets** — treat walls as a range/vol-regime indicator, not a magnet trade.

**SPY — MIXED / UNSTABLE. Do not lean.**
Spot 770.55, ZGL 774.33 (`zgl_reliable: true`), `total_gex` **+$690.0M**. The regime label reads **NEGATIVE while the aggregate sign is POSITIVE** — the documented label/sign defect, and today it ran on **4 of 4 sessions this week** (08-24→08-27 each showed the same contradiction). Trust the sign, not the label. The regime also flipped today with a large, noisy `zgl_delta` of +410 — a *fresh* flip is unstable by construction. Spot-vs-ZGL says short-gamma/trend-prone; the `total_gex` sign says long-gamma/dampened. The **771 call wall sits 0.06% from spot** — essentially at-the-money — so a push through it on fresh 0DTE call buying could see rapid follow-through. 760 is the more credible downside shelf.
→ **Structure bias:** defined-risk verticals. A tight straddle/iron-fly sale is *not* supported with the call wall on top of spot.

**QQQ — LONG-GAMMA / pin-prone. The coherent one.**
Spot 720.00, ZGL 719.16 (0.12% away), `total_gex` **+$1,152.9M**, label POSITIVE — **label and sign agree**. The largest single-strike concentration sits right at 720 (~$601M). Today's flip into POSITIVE was small and orderly (`zgl_delta` −10.14), unlike SPY's snap. Walls 700/730.
→ **Structure bias:** iron condor / short strangle inside 700–730, or an iron fly centred 719–720 to harvest the pin. Fade pokes beyond 730.

**Mandatory caveats.** EOD is a **prior, not a target** — fresh 0DTE OI floods in during the first 30–60 minutes and re-computes ZGL and walls. **Gap risk voids the prior**; today's melt-up was narrow and concentrated, so a mean-reversion gap is plausible and would invalidate the map before hedging engages. Tooling **cannot isolate the D+1 expiry** (`gex --dte-max 1` errors) — this is the standing 0–45 DTE book. This is the **SPY/QQQ ETF book**, not the cleaner SPX/NDX index book. QQQ's pin in particular sits on top of very concentrated single-name earnings flow that could overwhelm it.

### 2a. Next-session 0DTE premium-selling setup — **read the conditional, not the headline**

`scripts/zerodte_setup.py` returns `verdict: GO_PREMIUM_SELL_INTRADAY` and `sell_premium: true` for both indices. **That verdict is unconditional and it overstates the edge today.**

`vol_state` is **LOW** (VIX 14.51). Reading `mean_pnl_by_vix_state[LOW]` net of the assumed 0.1% round-trip cost:

| Index | Uncond. gross | Uncond. net | **LOW-VIX gross** | **LOW-VIX net** | Verdict as read |
|---|---|---|---|---|---|
| SPY | +0.216% | +0.116% | +0.131% | **+0.031%** | ~zero edge — stand aside |
| QQQ | +0.346% | +0.246% | +0.223% | **+0.123%** | thin, size down hard |

The edge lives in the **MID/HIGH VIX terciles** (bounds 15.8 / 17.3), not here. `pnl_basis` is **percent-of-underlying-spot-notional, GROSS** — not premium-collected, not margin-relative, so even the unconditional figure is small in absolute terms. Gross win-rates (SPY 86.7%, QQQ 85.0% on n=60) **overstate a negatively-skewed short-vol strategy**, and the validation sample contains **no vol shock — the left tail is UNSAMPLED**.

Structures if taken anyway: SPY iron fly / short straddle centred 770.4, wings ±0.83%; QQQ centred 719.95, wings ±1.37%; `size_scalar` 0.5 on both. **Enter at/after the open once the gap resolves; hold to the close; never carry overnight** (overnight entry backtested negative: QQQ `mean_pnl_overnight_pct` −0.10%). Delta-neutral — add no directional tilt. **Advisory, 0 rubric points, permanently** until a vol-shock day enters the sample AND net expectancy clears a tail-aware bar.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

**One qualifying mechanized DEX flip in the entire fleet: GOOG.**

`scripts/dex_flip.py` — `qualifies: true`, direction **short**, flip 2026-08-26: net_dex **−347,698,975** after three consecutive positive sessions (08-21 +803.8M, 08-24 +652.2M, 08-25 +503.4M). Trailing-10 median |net_dex| 450,732,072 → floor 112,683,018; **magnitude_ratio 3.09**; `sign_changes_in_window: 2`; **`whipsaw_warning: FALSE`**. Still live — 08-27 net_dex −371,930,604, a second consecutive negative session. Not a single-strike artifact: negative net_gex is spread across strikes 245–330. `total_gex` corroborates independently (positive 08-21→08-26, negative today).

**The generating agent declined to assert direction.** `net_vanna +3,618` (marginally put-heavy) with VIX falling fires `vanna_squeeze_flag = TRUE` — a **bullish** mechanism opposing the bearish flip — so `swing_bias` was set **NEUTRAL/CONFLICTED**. The +1 rubric line stands on the mechanized test; the directional read does not.

**No qualifying flips on SPY, QQQ, IWM, NVDA, MU, MRVL, AVGO.** SPY/QQQ show DEX *level* improvement (both turned strongly positive) but **not** a mechanized flip — not scored. IWM is mechanically the cleanest vanna-squeeze (put-heavy book, VIX falling, tool's own language calls it "classic") but is **disqualified**: its DEX trajectory is negative/deteriorating, contradicting the bullish squeeze mechanism. **NVDA and AVGO DEX/GEX moves today are earnings-repricing artifacts**, explicitly excluded. AVGO carries a *stale* qualifying flip from 08-14 — nine sessions old, already played out.

> **New substrate defect recorded.** `gex-time-series.zero_gamma_level` is **scale-corrupted on every single-name symbol** pulled (NVDA ZGL ≈25–95 against a ~$228 spot; MU ≈8–135 against ~$935; GOOG/MRVL/AVGO the same ⅓-to-1/10 mismatch). MRVL's reported `regime_flip_dates` (08-24/08-25) are **false** — pure ZGL scale artifacts with `total_gex` never changing sign. Regime was re-derived from the raw `total_gex` sign throughout.

## 2b. Sector Rotation

**Rotation regime call: `no_change`. Confidence: low.**

**Direction discipline.** `sector-flow` and `sector-flow-persistence` are **one gross-turnover source, sign-agnostic**, and today they fired **INFLOW on 11 of 11 sectors** (7 at persistence 1.0) — zero discrimination. Direction reads only off the netted `market-regime.sector_rotation`.

| Sector | Netted | Gross | Agreement | Persist. | Verdict |
|---|---|---|---|---|---|
| **Technology** | **IN +$500.3M** | +$5,763.7M | agree | 1.0 | **CONFIRMED IN** |
| Energy | IN +$4.3M | +$58.2M | agree | 1.0 | watch_only — fails magnitude bar (below $80.4M cross-sector median) |
| Consumer Cyclical | IN +$25.0M | **−$46.5M** | **DISAGREE** | 0.8 | watch_only — explicit conflict |
| **Healthcare** | **OUT −$15.6M** | **+$55.3M** | **DISAGREE** | 1.0 | watch_only — opposite signs, same session |
| Comm Services | OUT −$169.9M | −$446.8M | agree today only | 0.8 | watch_only — **1-day flip off a 4-day inflow trend** |
| Industrials | OUT −$51.2M | −$306.7M | agree today only | 0.8 | watch_only — same 1-day flip |

Technology is the only netted-confirmed, magnitude-clearing leg — and it is best read as an **earnings-continuation basket, not a rotation**. Critically, there is **dispersion inside it**: MU (−$103.2M) and SNDK (−$63.6M) are the two largest Technology *bearish*-screener names. Memory/storage is being sold while software and AI-compute semis rip.

**ETF flow tape (advisory — 0 rubric points).** 33 of the 40-call cap used.

| ETF | Net flow (5d) | GICS map | Agreement | DP positioning | Options urgency |
|---|---|---|---|---|---|
| IGV | +$10.25M | Tech (software) | agree | mixed/hedge-heavy | **~$20.7M of Dec-18 put buying vs ~$4.9M calls — real downside hedging under the rally** |
| XLK | +$9.95M | Tech (1:1) | **agree — high conviction** | mixed, no tell | small/retail-scale |
| KRE | +$3.15M | Financials | n/a | muted | tiny — and **zero** Financials names in the top bullish screener |
| GDX | −$19.79M | Basic Materials | **DISAGREE** | $33M/$26M blocks **above mid** | conflicting: Jan-27 $110C block vs near-term put hedges |
| XOP | −$17.15M | Energy | **DISAGREE** | thin | put-heavy — corroborates that "Energy IN" is not real |
| XLF | −$15.16M | Financials | **DISAGREE** w/ gross | blocks **below mid** (seller-aggressive) | thin |

Financials and Basic Materials show high-persistence *gross* inflow with **no netted confirmation**, and their representative ETFs (XLF, GDX) both show 5-day options **outflow**. That disagreement is good reason to disbelieve the gross read on both.

---

## 3. Swing Setups (1–6 weeks)

**Empty. No name reaches the `raw_score ≥ 3` LOW cut.** The three names below cleared the ≥2-agent confluence gate and are carried at full detail so the counterfactual stays gradeable — none is sized.

### 3a. Long swings (regime-aligned)

**Empty.** Zero long candidates cleared the confluence gate.

The nearest misses were the sector-rotation Technology leaders (NVDA, MSFT, NOW, CRM, AVGO — each `raw_score 1`), and every one failed independent confirmation: **accumulation-hunter rejected all of them** (COVERED_CALL / MIXED / sub-threshold DIRECTIONAL_LONG confidence), and dealer-positioning flagged the NVDA and AVGO moves as earnings-repricing artifacts. **TSLA scored −3** — the worst on the board — on a −$591.2M flow conflict at 7.0× the union median.

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only` (2026-08-01 P0 #1). Routing, not suppression** — theses are generated, scored, gate-verdicted and serialized in full.

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **GOOG** | **2** | Mechanized DEX sign-flip short (3.09× floor, no whipsaw, 2nd consecutive negative session, GEX-corroborated) + KINKED term structure with the kink landing **exactly on the 09-11 CPI date**, negative VRP. Comm Services netted OUT confirms. | Defined-risk put spread through 09-11 | DEX trajectory positive ≥3 sessions (undoes the 08-26 flip), or the vanna squeeze strengthens on falling VIX | **`watch_only`** |
| **MU** | **1** | Persistent bearish sweeps 5/5 sessions ($2.35B) + price-vs-flow divergence (price +10.2%, flow bearish) + BULLISH_EXTREME P/C z=−3.501; insider MSPR −33.33; **5d −4.00% while its own complex ripped** | — | Flow flips aligned; z reverts while price rises; MU reclaims ~$950 | **`watch_only`** — fundamentals **VETO** |
| **SNDK** | **−1** | Persistent bearish sweeps 5/5 ($1.31B) + 2nd-largest Tech bearish-screener name; insider MSPR **−99.42** (near-maximal); 5d **−7.23%** into maximally good news | — | 8d flow flips bullish; insider selling stops | **`watch_only`** — fundamentals **VETO** |

**Single-signal shorts (failed the confluence gate, §8):** ISRG — BEARISH_EXTREME z=10.021, price-vs-flow divergence (price +6.3%, flow −$15.9M), Tier-1 `OPENING_PUT_PRIME` $3.15M size/OI 2.787 on a deep-ITM $460P at 22 DTE. Healthcare netted OUT confirms. HYG — bearish credit-hedge ladder, structurally unresolved.

**Near-term sweeps (`sweep-tracker` — informational, 0 rubric points; the persistence line was removed 2026-05-23 P0.3 after −22pp over two audits).**

Ranked by 5-session persistence, **segregated by whether the name gapped on earnings today** — call sweeps on a name that just gapped 10–28% are chasing/hedging flow, not fresh positioning:

- **Non-gap, 5/5 persistence:** MU bearish $2.35B · TSLA bullish $3.69B · SNDK bearish $1.31B · META mixed $1.17B · MSTR bearish $998.5M · AAPL bearish $760.2M (mega-cap hedge-flow filter applies) · AMZN mixed $576.4M
- **Non-gap, 4/5:** GLD bearish $1.42B · **AMD bearish $543.0M — bearish sweeps while NVDA/AVGO/software rip on earnings, a notable intra-complex divergence** · PLTR bearish $537.9M · INTC mixed
- **Gapped today:** NVDA $5.47B but direction **mixed** (bid *and* ask heavy simultaneously — post-print dealer hedging, not a thesis)
- **Index/hedge flow (not directional):** SPX/SPXW deep-ITM collar structures, VIX calls, SPY/IWM puts, HYG/TLT, IGV puts — consistent with hedging under a narrow rally

**Caveat carried from the agent:** none of MU/TSLA/SNDK appeared in *today's* top-20 raw sweep or smart-money-flow tables. The 5/5 figure is a window aggregate, not same-day reconfirmation.

---

## 4. LEAP Builds (6–24 months)

**Empty. Zero candidates cleared the 6-of-9 gate.** LEAP share of volume was **3.6%** — a thin lane; no candidates were manufactured from it.

The DTE>180 book is a **hedging and overlay book, not an accumulation book**:
- **Covered-call selling** on the day's winners: NVDA $460C dte-841 **bid-heavy** (selling), AAPL $340C dte-841 bid-heavy — `conviction-matrix` returns **COVERED_CALL** on AAPL explicitly ("dark pool buying + call selling — yield enhancement, capping upside").
- **Protective/tail puts** on megacaps and commodity/EM: NFLX, NVAX, AMZN, ORCL, GOOG, MSFT (dte-512 deep-OTM puts), SLV/EWZ/EEM/GDX/AG/PBR — bid-heavy, dealer-side.
- **Only genuine ask-side LEAP call build: CORZ** ($35C, dte 512, oi_diff +8,347) — **disqualified 0–1 of 9**: today's OI build is dominated by **9-DTE** contracts, not the LEAP tenor (direction-verification fails); 90d cum-flow is **net bearish** ($542.2M bearish vs $493.8M bullish — wrong direction, a hard disqualifier); `conviction-matrix` = **DISTRIBUTION at 12.8% confidence** with DP sell volume exceeding buy (ratio 0.372).
- **MPT** sub-$5 (C12 fail) and a bearish put buy. **ASHR** brand-new OI 0→10,000 with no ask/bid split to direction-verify.

Institutions are **hedging into** the melt-up, not building multi-quarter longs — consistent with the stagflationary macro (sticky core PCE 3.34%, payrolls −23k).

---

## 5. Volatility Surface

**Substrate hygiene ran first; the raw labels are unusable.** `scripts/term_structure_hygiene.py` at `min_contracts=15` (a **named, tunable, NOT audit-frozen** parameter) over 21 liquid names:

- Raw `iv-term-structure`: **BACKWARDATION 17/21 (81%)** → after dropping the 0DTE bucket and sub-15-contract tenors: **11/21 (52%)**. **7 of 21 (33%) flipped shape** (SPY, RBLX, MSTR, TTD, SNOW, PANW, MU); the monotonic `base_shape` flipped on a different 6.
- `front_end_iv_ratio` at `--near-dte 7` fired on **12/21 (57%)** — graded by population, not per-name.
- ⚠ **Every `iv_percentile_zscore` is PROVISIONAL**: requested `--lookback-days 252`, the tool returned **`dates_used: 96`** — below the 120-day first-class floor. Directional colour only, never a sizing input.

**The structural read: the kinks sit on the macro calendar, not on earnings.** SPY/QQQ/AMD/MU kink at NFP week; **GOOG kinks exactly on CPI (09-11)**; MSTR/RBLX/TTD all kink at the 09-18 OPEX. These are macro-event kinks, not idiosyncratic dislocations — the one exception is SNOW.

| Ticker | raw | hygiene | base | FE@7 | kink (DTE/date) | prom. | VRP | Impl. move | Bias |
|---|---|---|---|---|---|---|---|---|---|
| **SNOW** | BACKW | **KINKED** | CONTANGO | 1.517 | 8 / 09-04 | **27.3%** | **+0.328** | 16.5% | **SELL VOL / calendar** (earnings 09-02) |
| **RBLX** | BACKW | KINKED | BACKW | 1.008 | 22 / 09-18 | 23.0% | −0.327 | 17.7% | **BUY VOL / calendar** |
| **TTD** | BACKW | KINKED | BACKW | **1.137** | 22 / 09-18 | 15.4% | −0.300 | 16.1% | BUY VOL — **short-front calendar DISQUALIFIED** (ratio >1.10, event-pending, not confirmed falling) |
| **MU** | BACKW | KINKED | BACKW | 1.027 | 8 / 09-04 | 11.0% | −0.344 | 10.7% | BUY VOL — cleanest calm-front calendar |
| **GOOG** | KINKED | KINKED | BACKW | 0.968 | 15 / **09-11 CPI** | 7.3% | −0.121 | 6.5% | BUY VOL, small size |
| MSTR | BACKW | KINKED | BACKW | 1.113 | 22 / 09-18 | 15.9% | −0.022 FAIR | 23.0% | **watch_only** — no confirming leg |
| PANW | BACKW | **CONTANGO** | CONTANGO | 1.394 | none | +0.068 | 18.7% | context — **shape/ratio conflict unresolved** |
| SPY / QQQ | CONTANGO / KINKED | KINKED | BACKW | 0.814 / 0.884 | 6 / 5 | low | FAIR / −0.038 | 1.5% / 2.5% | no dislocation |

**Every SELL-VOL call must clear the VRP headwind** — realised is running above implied on QQQ, so index vol is if anything cheap. Only SNOW carries positive VRP.

**IV outliers:** dominated by illiquid 0DTE penny-strike calls (SPCH, KORU, QS, DNUT, MSTX, NMAX at $0.5–$1.5 strikes) plus single-contract dispersion artifacts (QQQ 0DTE $710C at 6.5% avg IV; SMH 0DTE $572.5C at 3.0% vs 36.5% max). **Noise, not findings.** The `iv_rank` screener itself is dominated by sub-C12 microcaps (INV, BRLT, SPWH, DRAM, SSPC) and was unusable for this scan.

**Post-earnings distortion warning:** OKTA, CRM, CRWD, PANW, NOW, S and SNOW all have front-end IV **crushing right now**, which makes their term structure look artificially steep. Separate that from a genuine dislocation. Meanwhile realised vol is elevated across the board (RBLX rv20 116.2%, SOXL 109.1%, MEI 100.5%, PLTR 99.2%, TTD 98.8%, OKTA 98.1%, SPCX 97.5%, LITE 97.3%, SNDK 96.2%).

**Earnings vol lane** — population firing rate: raw BACKWARDATION **9/9 (100%)**, zero discriminating power. Back-month skew **6/6 COMPLACENT** (|skew| ≤0.018) — no tail hedging priced past any event in this batch. Verdict: **6 SKIP, 3 CALENDAR, 0 naked SELL VOL, 0 BUY VOL.**

| Ticker | Earnings | d2e | Validity | Impl. move used | Raw catalyst field | Understatement | Verdict |
|---|---|---|---|---|---|---|---|
| **MDB** | 09-01 | 5 | VALID | **21.0%** (dte-8) | 2.45% (dte-1) | **8.6×** | **CALENDAR** — kink prom. 31.5%, FE 1.63, VRP +0.2056 |
| **LULU** | 09-03 | 7 | VALID | **12.4%** | 1.64% | **7.5×** | **CALENDAR** — prom. 22.7%, FE 1.441, VRP +0.1909 |
| **ZS** | 09-03 | 7 | VALID | **17.8%** | 2.14% | **8.3×** | **CALENDAR, half size** — shape is FLAT, *no discrete kink*; leans on VRP alone |
| DELL | 09-01 | 5 | VALID | 16.8% | 2.51% | 6.7× | **SKIP** — kink **mislocated at 09-18, two days after FOMC**; never qualifies at dte-8; VRP FAIR |
| ADBE | 09-10 | 14 | **INVALID-SNAP** | 12.9% (corrected dte-15) | 1.78% | 7.3× | **SKIP** — prom. 7.7% (barely over floor); reports one day before CPI, event-stacked |
| ORCL | 09-08 | 12 | **INVALID-SNAP** | 16.65% (corrected) | 2.12% | 7.8× | **SKIP** — no kink at all; raw FE 0.821 misreads real panic as *calm* |
| MNSO | 08-28 | 1 | **NO_NEAR_TENOR** | **null** | — | — | **SKIP** — FE 1.000 means *no data*, not calm |
| NTAP | 09-02 | 6 | **NO_NEAR_TENOR** | **null** | — | — | **SKIP** — iv_rank 98.1 is a 30d artifact at the wrong tenor |
| SAIC | 08-31 | 4 | INSUFFICIENT_DATA | **null** | — | — | **SKIP** — every tenor below the contract floor |

> ⚠ **All three CALENDAR short legs expire 2026-09-04 — NFP day.** That is **one stacked event risk, not three independent trades.**

---

## 6. Risk & Correlation

**Macro headline:** mildly stagflationary — core PCE **3.34%** YoY sticky above target while payrolls **contracted −23k MoM**. Forward stack: NFP T+6, PPI T+9, CPI T+10, FOMC+SEP T+13, OPEX T+15.

**Breadth cross-check (advisory, 0 points).** `fz breadth`: **152 advancers / 349 decliners / 2 unchanged, `pct_green` 30.22%**, avg change −0.30%, median −0.65%. Top mover CRM +22.58%, worst HRL −10.25%. **`divergence_flag: TRUE`** — SPY closed **green** with under a third of S&P constituents green. From a different data lineage than `uw` (which independently reports 36.1% bullish), so two sources agree the tape is far weaker than the index print. **Advisory — it does not change sizing.**

**Correlation clusters** (`uw risk portfolio-correlation`, today's 16 candidates, 30d):
- **`memory_storage_cluster` — MU / SNDK, corr 0.905.** The tightest pair on the board: one AI-memory bet expressed twice. MU keeps (raw 1 > −1); **SNDK takes −1 tier**. Both VETO'd anyway, so the deduction is confirmatory — but had either survived, sizing both would have been a **double-weight short into the complex NVDA named as the binding AI bottleneck**.
- **`enterprise_software_cluster` — NOW / CRM / ZS / MDB**, chained (NOW–CRM 0.823, CRM–ZS 0.751, MDB–ZS 0.741). Four-way `raw_score 1` tie; all DROP-tier, so no keep/drop resolution was required. Recorded for the audit trail.
- **Soft watch (0.60–0.70, no penalty):** SNOW/MDB 0.68, NOW/ZS 0.639.
- **Measured and recorded as-is:** NVDA/AVGO came in at **0.584** — below even soft-watch on a 30d window. Surprising; not smoothed toward intuition.
- ⚠ `sector_breakdown` returned `{"Unknown": 16}` with a "100% in top sector" warning — **the documented CLI defect, excluded, not a real finding.**

**Gates applied.** Only two of nine did real work: **fundamentals** and the LOW cut itself. Every name failed on score before the risk stack was reached.

| Gate | Result |
|---|---|
| regime | −1 tier on all shorts (UPTREND vs SHORT) — but the UPTREND label is **one-sector-carried**; weakest version of this gate in weeks |
| vrp | no-op on all carried names (directional shorts, not naked short-vol) |
| **panic** | **`NA` — `front-end-iv-ratio` was never fetched and is absent from the Step-0 cache. A real gap, not a no-op.** VIX 14.51 is ambient evidence, not the ratio; no value was substituted |
| cluster | −1 tier SNDK (MU/SNDK 0.905) |
| sector | −1 tier MU/SNDK (Technology netted INFLOW is adverse to a short) — fired mechanically, evidentiary weight thin |
| fundamentals | **VETO MU · VETO SNDK · CAUTION GOOG** |
| event_risk | −1 tier on all three (stacked Tier-1 clause). **JOLTS T+4 explicitly does NOT fire** — medium impact, not Tier-1 |
| debate | **no-op on all three** — bear residual never exceeded bull |
| rubric_regime | **capped half on everything** (OUT-OF-REGIME) |

**Fundamentals verdicts (the load-bearing gate today):**
- **MU — VETO.** Short into a **4/4 EPS beat streak** (+17.3/+27.3/+17.4/+2.8%), revenue **+166.98% YoY**, EPS +700.71%, gross margin 72.57%, ROE 70.55%. Catalyst stack directly contradicts: **NVDA's 08-26 call named memory the binding AI-infrastructure bottleneck** ("customers want 50% more than it can supply"); TrendForce projects 68% of 2027 hyperscaler capex into memory. **Earnings 2026-09-21, T+16 — inside the horizon.** Insider MSPR −33.33 is the lone confirming leg.
- **SNDK — VETO.** 4/4 beat streak with the two largest beats most recent (+57.9%, +76.3%), revenue **+175.3% YoY**, ROE 93.13%. **$31B Kioxia NAND expansion announced 2026-08-27 — today.** Strong Buy upgrade 08-25. Institutions **net buyers** (+1.67%). Insider MSPR **−99.42** — near-maximal selling, the single cleanest bearish datum in the book, and it does not carry 2-of-3.
- **GOOG — CAUTION (−1).** Short into revenue +20.05% YoY, EPS +115.31%, D/E 0.12. Earnings trend *mixed*, not a miss streak. Insider data NA (never penalises).

**Debate disconfirmation:** GOOG bull 0.65 / bear 0.30 · MU bull 0.65 / bear 0.25 · SNDK bull 0.45 / bear 0.35. No round-2 escalation. **SNDK is a BOTH_SIDES_LOW case — neither advocate cleared a coin flip**; residuals carried verbatim on the 0.15–0.95 ladder, not clamped.

> **Registered for the auditor, not acted on:** all three debated names are **shorts**, and on a short thesis the *bull* is the disconfirming advocate — so the mechanical `bear ≥ bull` test runs with **inverted polarity** relative to its design intent. Direction-adjusted, GOOG's 0.65-vs-0.30 means the counter-case *dominates*. The mechanical no-op was applied as written; no direction-aware variant was invented. **As specified, the debate gate is structurally incapable of cutting a short** — on a book that routes every short to `watch_only`, it has no bite on the short lane at all.

**Adverse-flow exits.** `conviction_2026-08-26` **does not exist** (08-24/25/26 all produced empty boards and correctly wrote nothing). The last populated group is **`conviction_2026-08-21` = [IWM]**, carried 6 sessions. Alerts: LOW_IV_RANK (IV rank **1.66**), LARGE_DARK_POOL ($18.8M single print), OI_SHIFT (+124,193 contracts, **direction-unverified → awarded nothing**). Scan: close 299.81, flow **bearish**, net −$9.93M, P/C 1.327, volume ratio 0.82. **IWM tagged THESIS LAPSED — remove from carry** (scores 0/skip today). `fz` drift tripwire on IWM and GOOG: **no field changes**, no adverse-fundamentals exits.

**Hedge sleeve: NONE. Do not put one on.** The sized book holds zero positions, so net book delta is exactly zero — a SPY/QQQ vertical or VIX ladder against a zero-delta book is not a hedge, it is a naked directional position opened with house money. *Conditionally*, for legacy exposure generated outside this fleet: a **QQQ defined-risk put spread or VIX call ladder** is the cheapest expression given negative VRP (QQQ realised 21.5% vs implied 17.7%) into the NFP/CPI/FOMC stack. But that hedges delta this fleet did not create.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Empty. No name reached HIGH or MEDIUM.** The full carried book is below for auditability.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]` — from `analyses/audit/2026-08-22/phase_3_calibration.md`. The C3 fractional-Kelly gate remains **`ADVISORY_ONLY`** (n=27 vs a ≥30 bar, and tier×expectancy is **non-monotone**: LOW −1.784 · MEDIUM −2.239 · HIGH −1.965). The win-rate ladder stays the live sizer.

| Tier | Mean realised P&L | Payoff ratio | Capped half-Kelly | n |
|---|---|---|---|---|
| HIGH | **−2.441%** | 0.72 | 0.0 | 7 |
| MEDIUM | +0.104% | 0.948 | 0.0132 | 19 |
| LOW | −2.249% | 0.929 | 0.0 | 123 |
| DROP | **−5.004%** | **0.647** | 0.0 | 488 |

The one encouraging line: DROP's expectancy is by far the worst even though its *hit rate* is the best (payoff 0.647 vs 0.929/0.948). **The DROP pile wins small and loses big** — the first metric in eight cycles suggesting tier ordering does something, and it is a P&L metric, not a hit-rate one.

### Carried calls (all `watch_only` — full audit trail)

**GOOG — SHORT — swing — `raw_score 2` — `dealer_positioning`**
`score_components`: **+1** mechanized DEX flip (dealer-positioning-strategist / `scripts/dex_flip.py`) — *"flip 08-26 −347,698,975 after 3 consecutive positive sessions; magnitude_ratio 3.09 vs floor 112,683,018; whipsaw FALSE; 08-27 −371,930,604 = 2nd consecutive negative"*. **+1** vol-surface KINKED, VRP-aligned (vol-surface-scout / `scripts/term_structure_hygiene.py`) — *"hygiene KINKED, kink dte-15 = 09-11 CPI; VRP −0.1212, IV30 26.6% vs realised 38.7%"*. Σ = 2 ✓
`win_rate: null` · `win_rate_source: NA(substrate)` (`dealer_positioning` is not one of the five backtest-supported classes) · `market_excess: null` · cum_flow 30d −$136.8M / 90d −$130.5M · **parity FAIL — 64.1% deep-ITM at/sub-parity** · fundamentals **CAUTION** · debate 0.65/0.30 · **final `watch_only`**

**MU — SHORT — swing — `raw_score 1` — `vol_term_dislocation`**
`score_components`: **+1** vol-surface KINKED, VRP-aligned — *"raw BACKWARDATION → hygiene KINKED, 23 tenors, 0 dropped; VRP −0.3439, IV30 58.6% vs realised 93.0%; kink dte-8 = NFP date, NOT an MU catalyst"*. Σ = 1 ✓
`win_rate: null` · `NA(substrate)` · cum_flow 30d −$159.4M (**only −0.26% of $60.4B gross — the weakest scale-relative bearish read in the union**; 90d flips **positive** +$5.9M) · **parity FAIL — 65.0% financing; today's −$103.2M is ~91% `no_side` deep-ITM puts** · fundamentals **VETO** · debate 0.65/0.25 · **final `watch_only`**

**SNDK — SHORT — swing — `raw_score −1` — `bearish_flow`**
`score_components`: **−1** flow_conflict_lite — *"`trend_direction: MIXED`; sign-unstable across windows (30d +$1,159.2M / 10d +$118.4M / 8d −$159.0M / 5d +$6.9M); only +2.29% of gross"*. Σ = −1 ✓
`win_rate` **0.5274** · `win_rate_n` 146 kept (13 clamped rows dropped) · `backtest_clean` — **market-wide per class, NOT SNDK-specific** · **`market_excess` −0.0685** · fundamentals **VETO** · debate 0.45/0.35 · **final `watch_only`**

> The **−3 `flow_conflict` was disqualified** on SNDK despite a literal 13.7×-median trigger, because it failed all three pre-deduction screens: **(1) staleness** — the entire +$1,318.2M bullish net lands 07-17→08-17, *before* the sweep window the thesis rests on, while the clean recent 8d window is **−$159.0M**; **(2) single-ticket** — one 08-06 print (5,000× Jan-2027 $1660P sold on the bid, $286.5M, TV +226) is **24.7% of the 30d net** and is a short-vol premium sale, not a directional bet; **(3) parity** — the 08-14 session's matched $900-call calendar roll is **$215.6M, larger than that day's entire +$166.4M net**. `−1 lite` applied instead; mutual exclusivity respected.

**ISRG — SHORT — `raw_score 0`** · **HYG — SHORT — `raw_score 0`** — both `watch_only`, not debated (outside top-3), fundamentals NA.

### Rubric lines that scored zero today, and why

| Line | Why 0 |
|---|---|
| **+3 accumulation (3+ aligned)** | **Zero survivors union-wide.** All 24 institutional-tier DP names failed the `conviction-matrix` gate. The **C11 conjunction was never even reached** |
| +1 conviction-matrix DIRECTIONAL_LONG >70 | Zero LEAP candidates; the line is LEAP-only (2026-05-23 P1.1), so structurally 0 |
| **+1 multi-day OI build** | **0 on every name.** `oi-trend` returns BUILDING/5-consecutive-days universally (the 14-of-14 zero-discrimination defect). Direction-verified on all three gate-passers: **call-dominant — building the wrong way** (MU 56/58/60%, SNDK 66/46/61%, GOOG 59/57/**91**% calls) |
| **+1 cum-premium-flow accretion** | 0 on both eligible names — **intent screen failed**: 65.0% (MU) and 64.1% (GOOG) of top-of-book premium is deep-ITM at/sub-parity financing |
| +1 sector-rotation leader | 0 on the shorts. **Awarded on 5 Tech longs — and flagged:** gate (a) fired on 11-of-11 sectors at persistence 1.0, so it discriminates nothing; those +1s rest entirely on gates (b)+(c), which test the **identical field and threshold** as the standalone cum-flow line. **That is the documented double-count** — two rubric lines, one bit. Changed no decision (all land at raw 1) |
| **−2 contrarian overcrowded long** | **Explicitly withheld on MU and ISRG.** `pc-ratio-zscore` has **no `--date` flag**; today's z-values are single snapshots and "RISING" cannot be established. Stated rather than silently skipped |
| +1 opex-pin top-5 | Not OPEX week (third Friday was 08-21; next 09-18). Agent not spawned |
| +2 multileg directional | 0 on PCG (play type fits **neither canonical bucket** — the agent said so rather than forcing a label) and HYG (structurally unresolved). Awarded only on PBR and EWZ |

### Multileg structures accepted and rejected (informational)

**Accepted:** **PBR** (HIGH) — Nov-20 21C/24C credit spread, matched 27,500/25,950 clips, clean bid/ask tags, anchored **past** the Sep-18 earnings kink, TV positive both legs, **repeat=2**. **EWZ** (HIGH) — Nov-20 45C/46C debit spread, 21,000 matched both legs, **repeat=2**. **PCG** (MEDIUM) — Sep-18/Oct-16 20C calendar, 245,000 matched both legs (99% of each leg's day volume). **HYG** (MEDIUM, context only) — bearish credit ladder, repeat=2, risk cap not cleanly stateable.
**Rejected:** **HNI** — deep-ITM 22.5C/40C with **`time_value < 0` on both legs** (−$0.18, −$0.19), `side: no_side`, 600-lot prints repeated 15× — **textbook conversion/box, financing not conviction**. **GOOGL** — second leg's side unconfirmable. **WULF** — 1:2 mismatched sizing, `no_side`, ambiguous. **GLD** — running call program, no confirmable defined 2-leg pair. **NVDA** — all high-ratio contracts mechanically explained by post-earnings IV-crush unwind and delta-hedging. **IGV** — clean 103P/95P Dec-18 credit vertical but **excluded from +2**: IGV gapped +7.74% purely as a constituent pass-through of CRM/OKTA/CRWD/PANW/NOW earnings.

### Conviction rubric (Step 4, verbatim — rubric_version `2026-06-12`, FROZEN)

```
Daily conviction score = Σ:
  +1  MECHANIZED DEX flip / vanna-squeeze in trade direction (verified SIGN CHANGE, not a level;
      computed by scripts/dex_flip.py — never by hand)   # DEMOTED +3→+1 2026-06-12 P0.4
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified
      institutional-tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d
      confirms (sign aligned AND |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: award only
      when dominant_signal_class == leap_directional; 0 in all non-LEAP contexts
  +1  uw historical cumulative-premium-flow net directional accretion (30d) — INTENT-SCREENED:
      award only when (a) no C28 distribution_flag, AND (b) on dividend payers in an ex-div window
      the accreting prints are NOT deep-ITM sub-parity calls. Screen failed/unevaluated → 0
  +1  sector-rotation-strategist names ticker single-name leader — CONDITIONAL: (a) sector
      persistence_score ≥ 0.6 AND (b) cum_flow_30d aligned AND (c) |cum_flow_30d| ≥ $50M
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored play type)
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner overcrowded long with RISING pc-ratio-zscore (VRP positive)
      # INFORMED-FLOW CONTINUATION penalty, NOT "fade the crowd" (Pan-Poteshman 2006;
      # Ge-Lin-Pearson 2016). "Rising" needs a multi-date z trajectory.
  -3  flow_conflict — cum_premium_flow 30d CLEARLY opposite dominant_signal_class
  -1  flow_conflict_lite — 30d read MIXED   # -3 and -1 MUTUALLY EXCLUSIVE, apply ONE
  # Removed: sweep-persistence +1 (2026-05-23 P0.3, −22pp over two audits);
  #          signal-confluence ≥4 +2 (2026-06-12 P0.2, selection-confounded re-count)
  # TIER GATES (risk-monitor 2d, 0 points, NOT score_components):
  -1 tier  correlation cluster (pairwise corr ≥ 0.70)
  -1 tier  market-regime conflicts with trade direction
```
Tiers: **≥9 HIGH** (full) · **7–8 MEDIUM** (half) · **3–6 LOW** (starter/watch) · **≤2 drop**.

---

## 8. Watch-only — single signal, no confluence

Surfaced by exactly one Phase 1 agent; failed the ≥2-agent confluence gate. **Journaling only, not trade entry.**

| Ticker | Flagged by | Signal | Note |
|---|---|---|---|
| ISRG | contrarian-scanner | BEARISH_EXTREME z=10.021; price-vs-flow divergence (+6.3% price, −$15.9M flow); Tier-1 `OPENING_PUT_PRIME` $3.15M, size/OI 2.787 | Healthcare netted OUT confirms; `oi-decrease-with-volume` returns **zero rows** — no unwind evidence |
| SNOW | vol-surface-scout | KINKED, prom. **27.3%** (highest in set), VRP **+0.328**, FE@7 1.517 | Earnings 09-02. Would have taken a **`vrp: −1 tier`** — short-vol into negative index VRP is exactly what the sign gate catches |
| MDB / LULU / ZS | earnings-scout | CALENDAR × 3 | **All three short legs expire 09-04 = NFP** — one stacked risk. LULU was **explicitly disqualified by contrarian-scanner** (earnings in 7d = event-driven hedge bid, not crowding) |
| RBLX / TTD | vol-surface-scout | BUY VOL, negative VRP | RBLX **disqualified by contrarian** (continuation already played out, −26.2% over window). TTD's short-front calendar variant disqualified (FE 1.137 >1.10, unconfirmed falling) |
| PBR / EWZ | multileg-strategist | HIGH-conviction verticals, repeat=2 | Genuinely clean structures on non-gap names — the best unconfirmed ideas on the board |
| PCG / HYG | multileg-strategist | MEDIUM | PCG play type fits neither canonical bucket; HYG structurally unresolved |
| NVDA / MSFT / NOW / CRM / AVGO | sector-rotation-strategist | Tech single-name leaders | **accumulation-hunter rejected all** (COVERED_CALL / MIXED / low-confidence) |
| TSLA | sweep-tracker | Bullish 5/5, $3.69B | **raw −3** — flow conflict −$591.2M at 7.0× union median. ⚠ parity screen **not run** on TSLA; flagged for honesty, does not change the drop |
| AMD / PLTR / MSTR / GLD / AAPL / META / AMZN / INTC | sweep-tracker | Persistence only | Removed rubric line → 0 points |
| IWM | dealer-positioning-strategist | Cleanest vanna-squeeze mechanically | **Disqualified** — DEX trajectory contradicts the bullish squeeze mechanism |

**C12 liquidity floor drops** (price ≥ $5 AND 20d dollar ADV ≥ $50M, fail-closed): **PENN** ($48.7M), **PLAB** ($41.2M), **MEI** ($9.4M), **XRP** ($23.9M), **NEO** ($31.9M), **VYX** ($19.6M), **OMER** ($40.1M). `^VIX` fails by construction (index, no share volume) — expected, it is tape context not a candidate.

**`fz` advisory lanes — BOTH BULK FUNNELS CORRUPT.** The doubled-first-letter ticker bug is live on **20/20 rows** of both the squeeze lane (AABEO, AABR, AABSI, AACHC, AACHV, AAESI…) and the RS lane (PPURR, NNEO, **OOKTA**, FFROG, AAMPL, CCDNA, AAYA). Decodable but **never matched with `==`**. Per-ticker `fz_enrich` is healthy and was used for the fundamentals gate. Both lanes are advisory, 0 rubric points.

---

## Process notes

- **Step 6 (deep-dive top 3)** was skipped: no name reaches the LOW cut, and the top 3 already received a **fundamentals gate plus a two-sided adversarial debate** — strictly more scrutiny than `deep-dive` provides.
- **Step 6.5 (batch-scan)** and **Step 8.5 (deep-dive hand-off)** skipped — both are gated on HIGH/MEDIUM tier, of which there are none.
- **Watchlist write-back: NOTHING WRITTEN**, correctly. The rule (corrected 2026-07-23) is to write **only LOW-tier or better, never the raw top-5**; zero names reach LOW, and MU/SNDK are VETO-excluded regardless. No write was manufactured to fill the quota. Consequence: no `conviction_2026-08-27` group exists, so tomorrow has no daily carry group to measure adverse flow against — **expected and correct for an empty board, not an instrumentation failure.**

## ⚠ Short-generation floor — flagged for the next audit

Today produced **5 short theses out of ~30 candidates (~17%)** — squarely inside the suppressed band the 2026-08-22 audit measured (32.0% → 17.6%, Fisher p=0.00035; regime-controlled 31.3% → 17.4%, p=0.0045). **Three of the five were the same AI-memory / mega-cap-tech bet.**

A tape with **30.2% breadth green, 349 decliners, and 10 of 11 sectors red** should generate short candidates abundantly. It generated five. Compliance with the routing rule is clean — every short carries a full score, all nine gate verdicts, and serializes for the counterfactual — but this is what drift from *routing* into *suppression* looks like, and the rule becomes unfalsifiable if the lane starves. **Phase 1's short screens are worth a look before the next session. A session that yields few shorts in a distributive tape is a screen to re-check, not a clean board.**
