# Daily Market Analysis — 2026-08-26

> Backdated run, executed 2026-08-27. All `uw` calls pinned `--date 2026-08-26`; `market_data.py` pinned `--as-of 2026-08-26`. "Next session" = 2026-08-27.

## Executive Summary

- **Regime + GEX state:** TRANSITIONAL / PULLBACK_IN_UPTREND. SPY 766.08 (+0.02%), just below its 20SMA (766.63), above the 50SMA (752.97). VIX 15.21. A flat, narrow tape — every index inside ±0.15%. **SPY is short-gamma** (`total_gex` −451.6M), **QQQ long-gamma** (+283.3M). Sector lean: Technology is the only sector where netted and gross flow agree.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`. Not the binding constraint today — every call floors at `skip` before the cap is reached.
- **Next-session GEX (SPY/QQQ):** SPY — short-gamma · ZGL unreliable (364.22, 52% below spot) · call wall 780 (+1.73%) / put wall 765 (−0.22%, effectively ATM) · trend/breakout-amplification prior, a push through 765 accelerates rather than cushions. QQQ — long-gamma · ZGL 729.30 (+2.44%, reliable) · call wall 715 (+0.44%, very tight) / put wall 700 (−1.67%) · mean-revert/pin 700–715, but spot sits *below* the ZGL, i.e. the fragile edge of the well. Advisory — see §2.
- **Top swing build:** **None.** Zero positions sized.
- **Top LEAP candidate:** **None.** `leap-positioning-radar` cleared zero names on 6-of-9 gates.
- **Biggest risk:** Not a correlation cluster — there is no book to correlate. The real risk on this board is **methodological**: per-name VRP, the confirmation leg under all four SELL VOL theses, is biased rich into every earnings print by construction (§6).

**Zero positions sized — the 36th consecutive zero-sized daily board** (last sized: 2026-07-07). The board did not die on the risk stack; no cluster, panic, or regime conflict fired. It died at the quant stage, because the three heaviest rubric lines were structurally unavailable: `accumulation-hunter` returned zero flags, `multileg-strategist` found one structure market-wide and self-scored it 0, and `scripts/dex_flip.py` returned `qualifies: false` on all 15 symbols.

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — mixed signals, reduce position size, wait for clarity**; trend **PULLBACK_IN_UPTREND**. Guidance: *"Half position sizes. Favor defined-risk strategies. Iron condors in range."*

The headline tension on this tape is **breadth**. Only **34.7%** of optionable tickers carry bullish flow — 2,183 bullish against 4,105 bearish — while price closed flat-to-green. Flow breadth is materially weaker than price breadth.

| Index | Spot | Zero-gamma | `total_gex` | Regime (by sign) | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 766.71 | 364.22 (**unreliable**) | **−451,624,376** | **SHORT-gamma** | 780 (+1.73%) | 765 (−0.22%) |
| QQQ | 711.90 | 729.30 (reliable) | **+283,316,372** | **LONG-gamma** | 715 (+0.44%) | 700 (−1.67%) |
| IWM | — | — | — | whipsaws (5 sign changes/10d) | — | — |

> ⚠️ **The GEX `regime` label contradicted its own `total_gex` sign on *both* indices this session** — SPY labeled POSITIVE against a negative sign, QQQ labeled NEGATIVE against a positive one. This is the known substrate defect, now observed in 4 of 5 audited sessions. Every read above trusts the **sign**. `dealer-positioning-strategist` independently reproduced the same contradiction on other dates this week.

**Tape framing (C12-verified, `--as-of` pinned):** SPY +0.02%, QQQ +0.09%, IWM −0.10%, RSP +0.15%. Over 5 days the cap-weighted indices bled (SPY −0.39%, QQQ −0.66%, IWM −0.92%) while equal-weight RSP was flat (+0.02%) — a **mild rotation out of mega-cap**, not a broad decline. Sector ETFs 1d: XLI +1.09, XLK +0.61, XLE +0.60, XLU +0.46, XLB +0.17, XLF −0.09, XLP −0.29, XLC −0.50, XLRE −0.60, XLY −0.67, XLV −1.00.

**DTE share:** 0DTE **4.2%**, weeklies 21.8%, monthlies 20.4%, LEAPs 4.1% — `regime_hint` BALANCED. Not a retail-dominated tape; institutional positioning is present.

**VRP:** SPY +0.0038 **FAIR** (IV30 12.68 vs RV 12.30). QQQ **−0.0279 FAIR-but-NEGATIVE** (IV30 18.88 vs RV **21.66**) — implied is *below* realized on the Nasdaq complex, so premium selling on QQQ-complex single names is not favoured. `contrarian-scanner` applied its negative-VRP abort across 22 QQQ-complex names.

**Macro backdrop** (`scripts/fred_macro.py`): curve normal **+47bp** (10Y 4.64, 2Y 4.17); core CPI **2.79% YoY**; core PCE **3.34% YoY**; unemployment 4.1%; payrolls **−23k MoM**; 10Y flat over 30d; USD weakening; fed funds 3.63. **Core PCE above core CPI and above target, with contracting payrolls — the stagflationary quadrant.** This is the single most important macro fact on the board and it is hostile to undefined-risk short vol carried through a print.

**Forward event risk** (T+N on the trading calendar, T+0 = 2026-08-26): claims + Q2 GDP 2nd est 08-27 (T+1, medium) · JOLTS 09-02 (T+5) · ISM Services 09-03 (T+6) · **NFP 09-04 (T+7, Tier-1)** · **PPI 09-10 (T+11, Tier-1)** · **CPI 09-11 (T+12, Tier-1)** · **FOMC 09-16 (T+15, Tier-1)** · monthly OPEX 09-18 (T+17). No Tier-1 print falls at ≤T+3.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book read forward as the prior for the 2026-08-27 open. Prose-only, **0 rubric points**, no backtested predictive claim.

**SPY — short-gamma.** `total_gex` −451.6M. The put-wall cluster sits immediately below spot (765 at −0.22%, 760 behind at −0.87%), so a push through 765 at the open is likely to see dealer hedging **accelerate** the move lower rather than cushion it. Upside is comparatively open to 780. Structure bias: favour debit verticals or a directional lean over premium selling; if selling at all, skew it and keep wings wide.

**QQQ — long-gamma.** `total_gex` +283.3M, ZGL 729.30 reliable. The call wall at 715 is unusually tight (+0.44%) and should act as firm near-term resistance; 700 supports 1.67% below. Mean-revert/pin bias between 700–715 — but spot (711.90) sits *below* the ZGL (729.30), i.e. QQQ is on the fragile edge of its long-gamma well, not deep inside it. A clean break above 715 could migrate the book toward the flip near 729 and loosen the pin.

**Mandatory caveats.** EOD is a **prior, not a target** — fresh 0DTE OI re-computes the walls in the first 30–60 minutes. SPY's ZGL is extrapolated garbage (52% below spot) so its read rests entirely on the `total_gex` sign and spot-vs-wall position. Gap risk: claims + Q2 GDP 2nd est print 08-27 pre-open and can gap spot through the walls before hedging engages. `uw` **cannot isolate the D+1 expiry** (`--dte-max 1` errors) — this is the standing 0–45 DTE proxy book. This is the **ETF** book, not the cleaner SPX/NDX index book. Per `/weekly-analysis`, EOD-GEX-wall-as-magnet currently backtests **NO_GO** (walls behave as anti-magnets) — treat the above as hedging-mechanics narrative, not a trade signal.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py`)

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` / VIX | LOW / 15.21 | LOW / 15.21 |
| implied move | 0.94% | 1.42% |
| `expected_range_pct` | 1.12% | 1.37% |
| `size_scalar` | 0.5 | 0.25 |
| structure | wider iron condor, wings ≈ ±1.12% (short-gamma) | iron fly / short straddle centred 712.9, wings ≈ ±1.37% (long-gamma) |
| caution | — | front-end backwardation (0DTE IV 1.48× VIX) — event/gap risk, half size |
| PnL (gross / **net**) | +0.212% / **+0.112%** | +0.344% / **+0.244%** |

`backtest.verdict` is `GO_PREMIUM_SELL_INTRADAY` on both, `pnl_basis` = **percent-of-underlying-spot notional, GROSS**, net of an assumed 0.1% round-trip.

> ⚠️ **Read the VIX-conditioned cell, not the headline.** `sell_premium` and the verdict are **unconditional**. `vol_state` is **LOW**, and at LOW VIX the conditioned means are SPY **+0.132% gross → +0.032% net** and QQQ **+0.233% → +0.133% net**. SPY's LOW-VIX net expectancy is statistically indistinguishable from zero. The edge lives in the MID/HIGH terciles (bounds 15.9 / 17.3) and **VIX at 15.21 sits below the low-tercile bound**. Entry rule: enter at/after the open once the gap resolves, hold to the close, never carry overnight. Delta-neutral — no directional tilt. Advisory, **0 rubric points**; the short-vol left tail is **UNSAMPLED** (no vol shock in the validation window), so the gross win-rate overstates a negatively-skewed seller's edge.

## 2a. Swing Dealer Positioning (1–4 weeks)

**Zero names qualify for the +1 DEX-flip line.** `scripts/dex_flip.py` returned `qualifies: false` on all 15 symbols — mostly *"no sign change"*, which is precisely the level-scored-as-flip failure the 2026-06-12 mechanization was built to prevent. **No vanna squeeze validates anywhere:** the dated `^VIX` series falls only two consecutive sessions (08-24 15.85 → 08-25 15.45 → 08-26 15.21) against a ≥3-session gate, so that leg fails fleet-wide.

Non-scored GEX regime findings, computed off the **true `total_gex` sign** rather than the contradictory label:

- **SPY** — flipped negative **2026-08-17**, sustained **8 straight sessions**. A real, durable short-gamma regime.
- **AVGO** — flipped negative 2026-08-18, **7 straight sessions**, paired with a put-heavy vanna book. The closest thing on the board to a maturing vanna-squeeze precursor — blocked solely by the VIX leg.
- **QQQ** — flipped back positive 2026-08-25, only 2 sessions. Too fresh to trust.
- **INTC** — same-day marginal GEX flip to positive plus DEX decay toward flat. Narrative watch only.

Whipsaw warnings: TSLA (6 sign changes in 11 sessions), MSTR (5), SPY (4). Treat any level-based framing on these with elevated scepticism.

## 2b. Sector Rotation

**Rotation regime call: `no_change` (confidence low).** No canonical pattern is satisfied — growth→value needs Tech out (it's in); defensive→cyclical needs Discretionary in (Consumer Cyclical is out); cyclical→defensive needs Industrials out (it's in). This is genuinely mixed, not a rotation.

| Sector | Netted (directional) | Gross (turnover) | Agreement |
|---|---|---|---|
| **Technology** | **+$118.3M IN** | +$1,751.8M (#1, 2.5× runner-up) | **AGREE — the only clean call** |
| Industrials | +$8.2M IN | +$150.3M | Netted magnitude at the truncation noise floor |
| Financial Services | +$6.8M IN | +$119.5M | Nominal agree, but XLF's own tape is 5d **bearish −$14.7M** → watch_only |
| Consumer Cyclical | **−$56.9M OUT** | +$356.4M (#3 IN) | **DISAGREE → watch_only** |
| Communication Services | **−$26.8M OUT** | +$702.6M (#2 IN) | **DISAGREE → watch_only** (sharpest conflict) |
| Healthcare | −$13.6M OUT | +$95.4M | **DISAGREE → watch_only** |
| Materials, Energy, Utilities, Cons. Defensive, Real Estate | *absent from truncation* | positive | **UNKNOWN, not neutral** |

> ⚠️ **`sector-flow-persistence` fired INFLOW on 11-of-11 sectors at scores 0.8–1.0 — zero discrimination today.** It is sign-agnostic *gross turnover* and cannot express direction; direction comes only from the netted `market-regime.sector_rotation`, which is itself a **top-3/bottom-3 truncation** (five sectors simply absent — unknown, not neutral). The conditional sector-leader +1's condition (a) is therefore satisfied in a meaningless sense; the real gate is (b) ∧ (c).

**Single-name leaders (C12-floored, Technology only):**

| Ticker | Today net_flow | 30d cum_flow | (a) | (b) | (c) | Result |
|---|---|---|---|---|---|---|
| **MSFT** | +$7.7M | **+$657.2M** | ✓ | ✓ | ✓ | **+1 awarded — the only name clearing all three** |
| INTC | +$43.0M (day's top) | **−$291.3M** | ✓ | ✗ | ✓ | 0 |
| AMD | +$22.8M | −$27.6M | ✓ | ✗ | ✗ | 0 |
| PLTR | +$16.5M | −$144.2M | ✓ | ✗ | ✓ | 0 |
| MSTR | +$19.1M | +$33.5M | ✓ | ✓ | ✗ | 0 |

**The two largest bullish single-day prints on the tape — INTC and PLTR — both carry negative 30-day cumulative flow.** Today's print does not represent sustained accumulation in either.

**ETF flow tape (advisory, 0 rubric points):**

| ETF | Net premium dir | DP positioning | Options urgency | GICS agreement | Read |
|---|---|---|---|---|---|
| XLK | inflow +$13.9M | Large EOD blocks near mid — creation/redemption | **2027-12-17 LEAP calls, $8.6M @ 170** | agree (Tech) | High-conviction confirm of the Tech thesis |
| SMH | inflow +$46.3M | mixed-mid | 9/18 bearish put sweep $4.25M alongside call unwind | agree (Tech) | Moderate; sweep tape doesn't cleanly confirm |
| EWY | inflow (weak) | mixed | $50M+ in 2-day expiry calls | n/a | Single-session — fails multi-day persistence |
| GDX | outflow −$26.9M | large mixed blocks | 2027 LEAP put buy $14.45M | n/a (Materials truncated) | Watch-only |
| XOP | outflow −$19.6M | single $32.3M close-timed block | thin | n/a (Energy truncated) | Low conviction |
| XLF | outflow −$14.7M | **$93.2M single block at 20:25** (creation/redemption) | thin | **disagree** | Confirms watch_only |

---

## 3. Swing Setups (1–6 weeks)

### 3a. Long swings (regime-aligned)

**Empty.** No long swing thesis cleared the confluence gate with a score above the DROP floor.

The one name that came closest was **MSFT**, and it is instructive. `accumulation-hunter` found a genuine, timestamp-verified institutional buy block — **32 trades in 95 seconds (12:00:14–12:01:49Z, pre-market), 2,973,290 shares, $1,462.0M, executed above the then-prevailing NBBO ask of $488.18**. `sector-rotation-strategist` independently awarded MSFT the only sector-leader +1 on the board (+$657.2M 30d cum-flow). But `accumulation-hunter` **rejected it** on the C11 conjunction: OI build is mixed calls *and* puts (not direction-verified), `oi_smart_positioning` has no MSFT row at all, and the 30d cum-flow is tool-labeled **MIXED at just 4.3% of gross**. Two of five legs is not a conjunction. Because it was filed as a rejected near-miss rather than a flag, MSFT carries only **one** positive agent and fails the ≥2-agent confluence gate — it appears in §8, not here.

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only` (2026-08-01 P0 #1).** Routing, not suppression — theses are generated, scored and serialized in full so the counterfactual keeps resolving.

**DIS — `watch_only`, raw_score −1, `bearish_flow`.** Best-corroborated idea on the board and the lowest-scoring; see §6.

- *Thesis:* distribution into strength. `uw insights price-vs-flow` shows **DIVERGENCE true** — price +9.95% over the lookback against net options flow of **−$924K**. `uw oi decrease-with-volume` confirms Sep-18 110C (−4,541 OI) and 120C (−2,648 OI) being **closed on volume** — call-side profit-taking as price extends. Step 0's single-leg scan flags a Tier-1 `OPENING_PUT_PRIME`, $580K, 23 DTE, K108 against spot 109.93 (essentially ATM, OI ~25 vs size 4,434 — genuinely opening).
- *Independent second flag:* `sweep-tracker` found today's **largest actual DIS print is that same contract** — a $108P 9/18 bought at the **ask**, $640K, 4,434 contracts — while the 5-day sweep-persistence label reads "bullish 5/5". The aggregate label is stale and wrong against the tape.
- *Structure:* Sep-18 108/100 put debit spread (IV rank only 14.85 favours a debit, not a credit). *Not sized.*
- *Invalidation:* net premium flow flips positive, or the Sep-18 call-OI unwind reverses into fresh call buying.
- *Key risks:* 30d cum-flow is **−$1.85M, only −0.6% of $284.8M gross** — arithmetically churn; the bearish tilt lives in the **stale 60–90d window** (90d −$45.84M) while 5d is **+$1.72M, mildly bullish**. Four Tier-1 macro binaries sit inside the 23-DTE horizon.
- *Backtest:* `win_rate` **0.5294** (n=136, `backtest_clean`) against a same-window same-direction SPY short of **0.6029** → **market_excess −0.0735**. A short that underperforms a naive index short is exactly the population the routing rule exists for.

**HPQ — `watch_only`, failed confluence (1 agent).** `price-vs-flow` divergence true (price +26.4% vs flow −$1.13M), IV rank 74.4. But P/C 3.0 absolute is z = +0.771 **NORMAL** — HPQ's baseline P/C is chronically high, so 3.0 is no fresh anomaly — and `oi decrease-with-volume` shows *puts* closing, which is ambiguous. Two internal signals, one agent. See §8.

**BURL / URBN** — screened and explicitly **not actionable**. BURL is already −11.86% with flow aligned (priced in); URBN's notional is trivial ($1.42M bearish vs $1.35M bullish). Listed to show the screen ran.

**Sweeps (informational, 0 rubric points).** Only two names are genuinely clean on persistence **and** direction-verified ΔOI: **DLTR** (put 4/5; ΔOI lands exactly on the $140P +416 and $124P +1,399, matching the Tier-1 `FLOOR_PUT_BLOCK`) and **MSTR** (put 5/5; ΔOI 100% puts across six strikes).

> ⚠️ **Four names carry "bearish" persistence labels that today's ΔOI contradicts** — INTC, AMD, PLTR, MRNA all show **call-dominant** actual OI builds. INTC's bearish label is driven by a **$32.8M 2028 $140P sold at the bid**; MSTR's largest single ticket was a **$25.8M $335P 2028 sold at bid**. Both are *writes*, not directional buys, booked as bearish premium. This is the put-sale netting mechanism, live on four names at once. PLTR's largest sweep was a 2-DTE $175C printing on **both bid and ask** — gamma scalping, not a directional bet.

Mega-cap hedge-flow filter: AAPL aligned but with no urgency in the actual prints (also Tier-4 AVOID), NVDA misaligned (sweep bearish, cum_flow bullish), GOOGL misaligned. All demoted to footnote.

---

## 4. LEAP Builds (6–24 months)

**Empty.** Zero candidates cleared 6-of-9 gates. LEAP share of volume was **4.1%** — a thin day. The two REQUIRED gates (90d slow-accretion cum-flow, `conviction-matrix` DIRECTIONAL_LONG >70) bound on every name.

Disqualifications worth recording, because several looked bullish until the bid/ask split was checked:

| Name | Why it failed |
|---|---|
| **ASTS** | The $1.29M "call print" was **99.75% at the BID** (prev_ask_volume 1 vs prev_bid_volume 400) — the whale tape and the OI build are the **same contract read from opposite sides**. Net positioning is short calls. |
| **NVO** | `conviction-matrix` returns **COVERED_CALL** — *"dark pool buying + call selling — yield enhancement, capping upside."* Deep-ITM long-dated call on a dividend payer = financing/yield overlay, not conviction. |
| **GOOGL** | `conviction-matrix` **DIRECTIONAL_SHORT** at 29.9%; dark pool shows distribution (buy_sell_ratio 0.28, $2.07B volume, two blocks of $472M and $368M both below mid); 90d −$558M. |
| **CRCL** | Best of the pool at ~3–4/9. 90d −$57.3M MIXED decomposes to first-60d ≈ **−$110.1M** then a +30d swing — a **sign reversal**, not slow accretion. |
| DKS | 90d −$15.5M, 30d −$10.9M — wrong direction. Dominant flow is a 23-DTE cluster, not LEAP-horizon. |
| INTC | 90d **−$889.7M**; the K210/842-DTE call print was **bid-heavy** (2,892 ask vs 3,587 bid) — a covered-call overlay. |
| IBIT | `consecutive_build_days` = **1**. Single session, not accumulation. |
| SOXX | Textbook risk-reversal shape, but cum-flow MIXED both windows on ~$3.3B gross each side; matrix confidence 0.3%. |

---

## 5. Volatility Surface

**No fillable vol dislocation outside routine pre-earnings pricing.**

> ⚠️ **Three substrate defects fired simultaneously today.** (1) The raw `iv-term-structure` label **flipped on 6 of 11 names** after `scripts/term_structure_hygiene.py`; base shape flipped on 3 more (MDB/DELL/LULU are **contango bases with an earnings kink on top** — neither label alone describes them). (2) `uw historical iv-percentile-zscore --lookback-days 252` returned **`dates_used: 95` on every single ticker** — *all* percentiles below are PROVISIONAL. (3) The cached `iv_rank_high` funnel has **zero overlap** with the C12-floored universe: all 25 rows are `iv_rank=100` micro-caps/ETNs (DVIN, SNBRQ, VSXY, INV, MANE, SPWH, JEDI…). A dislocation the desk cannot fill at size is not a trade.

**Event bucket** — `front_end_ratio ≥ 1.10` on 6 of 7, meaning *"event still pending, don't fade"*. These are **not** calendar candidates; they route to §7 as earnings-vol rows.

| Ticker | shape / base_shape | front_end_ratio | IV pct (provisional) | back-month skew | implied move |
|---|---|---|---|---|---|
| BURL | BACKW / BACKW | **1.572** (highest) | 97.89 HIGH_IV | +0.0042 flat | 7.9% |
| DLTR | BACKW / BACKW | 1.556 | 67.37 | +0.0213 mild | 7.9% |
| MDB | **KINKED** / CONTANGO | 1.551 | 80.0 HIGH_IV | +0.0205 mild | **20.0%** |
| LULU | KINKED / CONTANGO | 1.472 | 73.68 | −0.0108 flat | 12.5% |
| DELL | KINKED (thin, 6.2%) / CONTANGO | 1.454 | 45.26 (vs raw 67.4) | −0.0088 flat | 17.1% |
| PANW | KINKED **MISLOCATED** / BACKW | 1.358 | 82.11 HIGH_IV | −0.0006 dead flat | 16.2% |
| MRVL | BACKW / BACKW | 1.309 (weakest) | **17.89 LOW_IV** (vs raw 55.0) | −0.0352 complacent | 9.1% |
| ORCL | BACKW / BACKW | 0.862 **INVALID** | 71.58 | +0.0007 flat | 16.4% |

**PANW's kink is mislocated onto CPI.** The hygiene script reports `kink_expiry` 2026-09-11 (dte15) — that is the **CPI print**, ten days after PANW's own 09-04 event tenor. Caught independently by both `vol-surface-scout` and `earnings-scout`. Its SELL VOL read had to be recovered from the fallback `base_shape` instead; the primary read failed.

**ORCL's front-end ratio is invalid, not calm.** Its dte=8 tenor (09-04) sits *before* the 09-08 print, so 0.862 CONTANGO measures pre-event quiet, not post-event decay. The true event tenor is dte=15.

**No-catalyst bucket — all held `watch_only` for want of a confirmation leg:** **ASTS** (percentile **0**, z **−2.463** — cheapest vol in the set, kink 09-18 two days after FOMC; the best *structural* buy-vol setup on the board but zero confirmation legs), **SOXL** (pct 8.42, kink NFP-aligned), **MU** (pct 6.32, kink NFP-aligned; its flagged $910P outlier is a `dte=-1` print artifact already dropped by hygiene).

Single-contract IV outliers: every cached row is a 0DTE/expiry-day print. Nothing survives the liquidity floor plus the 0DTE filter.

---

## 6. Risk & Correlation

**Macro headline:** stagflationary quadrant — core PCE **3.34% YoY** *above* core CPI 2.79% and above target, payrolls **−23k**, unemployment 4.1%, curve +47bp, USD weakening. Forward Tier-1: **NFP T+7 · PPI T+11 · CPI T+12 · FOMC T+15.** No Tier-1 at ≤T+3.

**Correlation.** `uw risk portfolio-correlation` over today's seven candidates. **No cluster fires.**

| Pair | corr | Classification |
|---|---|---|
| DLTR / LULU | **0.697** | **Soft watch (0.60–0.70)** — no penalty |
| BURL / LULU | 0.561 | not flagged |
| DLTR / BURL | 0.553 | not flagged |
| MDB / PANW | 0.545 | not flagged |

DLTR/LULU at 0.697 sits **0.003 below** the ≥0.70 threshold. Risk-monitor deliberately did **not** upgrade it — this is exactly the discretionary judgement the mechanical gate exists to remove (a prior audit found 0.631 firing while 0.703 did not). It is two consumer names, both short-vol into a print, in the same 30-day beta; if either were sizeable they would be one position.

> ⚠️ **Tool artifact, discarded not propagated:** `sector_breakdown` returned `{"Unknown": 7}` with a spurious *"CONCENTRATION: 100% of tickers in Unknown"* warning. The sector resolver returns `Unknown` for every symbol then computes a concentration alarm off its own null. True sectors: DLTR Consumer **Defensive**; BURL, LULU Consumer Cyclical; MDB, PANW, MRVL Technology; DIS Communication Services. Actual concentration is 3-way.

**Panic gate — the CLI default would have fired a false alarm.** `front-end-iv-ratio` at the default `--near-dte 1` reads SPY **1.164** / QQQ **1.147**, both above the 1.10 panic threshold. Re-read at the discriminating `--near-dte 7`: SPY **0.915 CONTANGO**, QQQ **0.981 FLAT** — *below* 1.0, i.e. panic resolving. VIX 15.21 corroborates. **No panic.**

**Fundamentals verdicts (top-5):**

| Ticker | Verdict | Tier adj | Driver |
|---|---|---|---|
| DLTR | **CAUTION** | −1 | 3/4 beat streak + Truist→$138 / Guggenheim→$145 PT raises (08-25) fight the bearish put tilt; +51.33% YoY revenue is a **Family Dollar divestiture comp distortion**, not organic |
| MDB | **CAUTION** | −1 | Largest implied move on the board (20.0%); insider MSPR **−84.05** persistent over 3 months; stacked PT raises lift the bar a beat must clear |
| BURL | **CAUTION** | −1 | Insider MSPR **−100 two consecutive months**; beat margin thinned to +1.02% from 7–18% |
| LULU | **CONFIRM** | 0 | Insider MSPR **+78.42** — the only clean net insider *buying* in the top-5, consistent 3 months; beat streak intact |
| MRVL | **CONFIRM** | 0 | Mixed near-zero surprise trend, insider reversal to −100, "$20.8B swing" narrative — all corroborate **large move size**, which supports BUY VOL |

> **Correction.** The fundamentals gate cited "Consumer Cyclical, largest netted outflow (−$56.9M)" as one of four reasons for DLTR's CAUTION. **DLTR is Consumer Defensive**, which is absent from the netted truncation entirely — that reason is **void** and originated in the orchestrator's prompt, not the agent's analysis. DLTR's CAUTION stands on its other three legs. BURL and LULU *are* Consumer Cyclical and the −$56.9M does apply to them. Verified against `earnings_catalyst.json`.

**Debate — five debates, five bear wins, zero bull wins.** The gate fires on all five.

| Ticker | bull | bear | Bear's strongest unrefuted point |
|---|---|---|---|
| MDB | 0.25 | **0.75** | **6 of the last 8 quarterly prints exceeded 20%** (median ~22%, mean ~23.5%, range 16.9–38.0%) — the 20.0% implied move being sold is *below* MDB's own typical realized print |
| DLTR | 0.35 | **0.65** | The +0.1996 VRP is near-definitional into a print; a single 7.25% move alone pushes trailing RV to the low-40s once it lands |
| BURL | 0.25 | **0.55** | Surface calm is real (1-DTE skew flat, ratio 1.003) but positioning is **~10:1 put-skewed in premium** ($29.6M vs $2.97M) with fresh 310/320/330 strangle OI into a 2-day expiry |
| LULU | 0.45 | **0.55** | **25-delta skew is inverted** (call 0.8242 > put 0.8142) — with insider buying and 10.43% short float / 3.16 DTC, three reads point at a fat **upside** tail, which loses for a short strangle just as hard |
| MRVL | 0.45 | 0.45 | 174.4% front IV × √(1/365) = **9.13%** — the "9.1% implied move" **is** front-tenor IV restated; IV30 (79.65%) interpolates to the 29-DTE point (80.77%), i.e. *after* the print. **BOTH_SIDES_LOW** — neither advocate cleared a coin flip |

> ### The finding of the day: per-name VRP is a contaminated confirmation leg
>
> Per-name `uw historical vrp` printed PREMIUM_SELLING on **all five** short-vol names — DLTR +0.1996, MDB +0.2361, BURL +0.1813, LULU +0.2041, PANW +0.2200 — and that reading was the **confirmation leg under every SELL VOL thesis on the board**.
>
> Two bears, in separate debates and by different arithmetic, established that this is **near-definitional into any earnings print**: IV30 is a forward measure that already contains the upcoming event hump, while trailing RV30 is a backward measure that structurally *excludes* the prior one. MDB last reported ~60 sessions before this measurement, so its 30-session realized window contains **zero** earnings jumps. The metric will read "rich" every quarter regardless of whether the priced move is adequate — and MDB's own history says it usually is not.
>
> The VRP *sign* gate still mechanically no-ops (the structures are correctly aligned to the sign), but it is recorded as **aligned-but-uninformative** on all five. A no-op here is not evidence of support.
>
> The one uncontaminated VRP read on the board is **MRVL −0.1168 PREMIUM_BUYING** (IV30 79.65 < RV30 91.33), which genuinely supports a long-vol structure — though the MRVL bear then showed the comparison is at the wrong *tenor* anyway.
>
> Note the shape: five bear wins is not five independent verdicts. Four rest on the **same** structural objection — the board tried to sell earnings vol on names whose own realized-move history says the implied is under-priced, confirmed by a metric biased rich into every print. **One finding replicated five times.**

**Adverse-flow / exits.** `conviction_2026-08-25` **does not exist** — 08-24 and 08-25 were empty boards, so the corrected write-back rule correctly wrote nothing. The actual rolling carry is **`conviction_2026-08-21 = [IWM]`**, and the gate ran against it. **IWM's thesis is INTACT, not an exit candidate**: today reads `flow_direction: bearish`, net flow −$6.57M, put/call 1.313, OI **+148,501 increasing**, price −0.92% over 5d (weakest of the four index proxies). Its three alerts (LARGE_DARK_POOL $22.1M, OI_SHIFT +148,501, LOW_IV_RANK 5.0) are confirmations, not reversals — `LOW_IV_RANK 5.0` in fact *supports* the long-put expression. IWM remains `watch_only` (directional short).

**Breadth cross-check:** **unavailable this run.** `fz` cannot be date-pinned and was verified serving 2026-08-27 pre-market data — it reported HPQ as the day's worst mover at **−10.36%** and DG as top mover at **+10.65%**, when on 2026-08-26 HPQ actually closed **+3.39%** and DG **+0.16%** (OKTA likewise +17.68% vs an actual +2.92%). On a backdated run those lanes would inject look-ahead into the report and corrupt the audit truth-set, so `fz_available` was set **false** for the breadth cross-check and the squeeze/RS candidate surface. Lagged structural fields (short float — exchange semi-monthly settlement, ~2-week lag — and float) remained available to the fundamentals gate, which is why `fz_context` is populated on the top-5. Advisory lane, graceful skip, zero sizing impact.

**Hedge sleeve: none, and buying one would be pure cost.** The book's directional skew is **0.00** — six non-directional vol structures at `skip`, one directional short at `watch_only`. Net delta zero. The ≥0.6 skew trigger cannot be met by an empty book. *For desk awareness only, not a recommendation from this book:* the live macro tail is the 09-04 → 09-11 → 09-16 sequence against a stagflationary backdrop; the cheapest defined-risk expression, if directional exposure exists **outside** this book, is a SPY put spread or VIX call ladder dated past 09-16, funded by a cheap front end (VIX 15.21, SPY 7d/30d ratio 0.915 CONTANGO). That is a PM-owned macro overlay, not a hedge to today's conviction book — which has nothing to hedge.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Empty. Zero names reached MEDIUM (7) or HIGH (9).** The highest score on the board was **1**.

*Expectancy lens (advisory — C31):* not printable this cycle. Every tier band is empty, so there is no per-tier realised expectancy or payoff ratio to display. `[advisory — expectancy is not yet a live sizing axis]`

Full audit trail for all seven scored names, since none reached the §7 threshold:

| Ticker | raw | Components | Class | win_rate (n, source) | market_excess | pre-risk | Fund. | Debate (bull/bear) | Gates fired | **Final** |
|---|---|---|---|---|---|---|---|---|---|---|
| **DLTR** | **1** | +1 earnings SELL VOL · +1 direction-verified put OI build · −1 flow_conflict_lite | `oi_build` | null — NA(substrate) | null | skip | CAUTION | 0.35 / **0.65** | fundamentals −1, debate −1, rubric cap | **skip** |
| **MDB** | **1** | +1 earnings SELL VOL | `earnings_vol` | null — NA(substrate) | null | skip | CAUTION | 0.25 / **0.75** | fundamentals −1, event −0.5, debate −1, rubric cap | **skip** |
| **BURL** | **1** | +1 earnings SELL VOL | `earnings_vol` | null — NA(substrate) | null | skip | CAUTION | 0.25 / **0.55** | fundamentals −1, sector tag, debate −1, rubric cap | **skip** |
| **LULU** | **1** | +1 earnings SELL VOL | `earnings_vol` | null — NA(substrate) | null | skip | CONFIRM | 0.45 / **0.55** | sector tag, event −0.5, debate −1, rubric cap | **skip** |
| **MRVL** | **1** | +1 earnings BUY VOL | `earnings_vol` | null — NA(substrate) | null | skip | CONFIRM | 0.45 / 0.45 | debate −1, rubric cap | **skip** |
| **PANW** | **1** | +1 earnings SELL VOL | `earnings_vol` | null — NA(substrate) | null | skip | NA | n/a | rubric cap only | **skip** |
| **DIS** | **−1** | −1 flow_conflict_lite | `bearish_flow` | **0.5294** (n=136, `backtest_clean`) | **−0.0735 → beta** | watch_only | NA | n/a | **short routing (terminal)**, event −1, rubric cap | **watch_only** |

**Invalidation levels.** DLTR: put OI build fails to persist past the print / persistence drops out of top-N. MDB, BURL, LULU, PANW, MRVL: IV fails to crush at the post-print tenor, or the term-structure kink resolves flat. DIS: net premium flow flips positive, or the Sep-18 call-OI unwind reverses.

**Why `market_excess` is null on six of seven:** `uw historical signal-backtest` supports only five classes, and **`oi_build` and `earnings_vol` are not among them**. This is a **substrate limitation, not a measurement of zero**. The quant explicitly declined to substitute a neighbouring class to manufacture a measurable rate. DIS is the only name with a clean read, and it flags **beta**.

**The rubric-coverage gap this board exposes.** DIS is the most-corroborated idea produced today — three agents independently read distribution-into-strength — and it scored **−1**, the lowest on the board. The rubric has **no line that pays a contrarian thesis**; its only contrarian line is a **−2 deduction**, which was itself unawardable because `pc-ratio-zscore` has no `--date` flag and so cannot establish the "rising" trajectory the line requires. Flagged for the next audit, not patched here.

A second gap: the `flow_conflict` **deduction** side has no scale-relative floor while the **award** side does. Five of seven names today have net flow at 0.4–5.0% of gross — arithmetically churn — yet are still judged on it.

### Conviction rubric (version `2026-06-12`, frozen) — reproduced for audit

```
Daily conviction score = Σ:
  +1  dealer-positioning MECHANIZED DEX flip / vanna-squeeze in trade direction (scripts/dex_flip.py; verified SIGN CHANGE, not level)
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified institutional-tier confirmed)
      — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms (sign aligned AND |cum_flow_30d| >= $50M); else halved to +1
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days >= 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: only when dominant_signal_class == leap_directional
  +1  uw historical cumulative-premium-flow net directional accretion, 30d — INTENT-SCREENED (no C28 distribution_flag; no ex-div deep-ITM sub-parity calls)
  +1  sector-rotation-strategist names ticker single-name leader — CONDITIONAL: (a) persistence >= 0.6 AND (b) cum_flow_30d aligned AND (c) |cum_flow_30d| >= $50M
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored play type)
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner overcrowded long with RISING pc-ratio-zscore (VRP positive) — informed-flow CONTINUATION penalty, not a fade signal
  -3  flow_conflict — cum_premium_flow 30d clearly opposite dominant_signal_class
  -1  flow_conflict_lite — 30d read MIXED (signed sum near zero, or aligned but bottom-quartile magnitude)
      (-3 and -1 are mutually exclusive — apply ONE, never both)
  # TIER GATES applied by risk-monitor in 2d, contributing 0 to raw_score:
  -1 TIER  correlation cluster (pairwise corr >= 0.70)
  -1 TIER  market-regime conflicts with trade direction
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | HIGH | full (subject to Step 3a load-bearing gate + win-rate gate) |
| 7–8 | MEDIUM | half (subject to win-rate gate) |
| 3–6 | LOW | starter / watch-only |
| ≤ 2 | DROP | filtered by the quant's drop floor |

**Tier-cut status:** the ≥9 HIGH cut was set in-sample on UPTREND data and **failed its scheduled re-confirmation on 2026-06-12** (bands inverted: HIGH 0.222 / MED 0.214 / LOW 0.444). Cuts are retained under the P0.1 freeze but carry no validated ranking claim; the P0.6 out-of-regime guard caps all sizing at half in the interim.

**Deep-dive hand-off:** skipped — no HIGH-tier names (Step 8.5 explicitly skips on a no-edge day). `uw playbook batch-scan` (Step 6.5) likewise a no-op: zero names at raw_score ≥ 7.

---

## 8. Watch-only — single signal, no confluence

Surfaced by exactly one Phase 1 agent; failed the ≥2-agent confluence gate. **Journaling only, not for entry.**

| Ticker | Sole flagging agent | Note |
|---|---|---|
| **MSFT** | sector-rotation-strategist (+1 leader, all 3 gates, 30d cum-flow **+$657.2M**) | `accumulation-hunter` found a genuine $1.462B pre-market above-ask block but filed it a **rejected** near-miss (C11 conjunction not met), so it is not a second positive flag. **The single most interesting name on the board that cannot be traded today.** |
| **HPQ** | contrarian-scanner (2 internal signals) | price-vs-flow divergence (+26.4% price vs −$1.13M flow), IV rank 74.4; but P/C z +0.771 NORMAL and the OI check is ambiguous |
| **MSTR** | sweep-tracker (put 5/5, ΔOI 100% puts) | Largest single ticket was a **$25.8M $335P 2028 sold at bid** — a write, not a directional buy |
| **NVDA** | multileg-strategist | The board's only decomposable structure (230C/240C 08-28 vertical, near-mirror ask/bid magnitudes) — **self-scored 0**: single-day print, and it contradicts NVDA's aggregate flow (−$28.16M, 2nd most bearish name). Hedge-suspect |
| **ASTS** | vol-surface-scout | Cheapest vol in the scan (percentile 0, z −2.463), kink 09-18. Best structural buy-vol setup with **zero** confirmation legs |
| **SOXL**, **MU** | vol-surface-scout | LOW_IV with NFP-aligned kinks — macro, not idiosyncratic; no confirmation leg |
| **AVGO** | dealer-positioning-strategist | 7-session sustained negative GEX + put-heavy vanna = maturing squeeze precursor, blocked solely by the VIX leg |
| **DELL**, **ORCL** | earnings-scout verdict **SKIP** | DELL: thin 6.2% kink + flat skew + neutral VRP (three weak signals stacked). ORCL: event 13d out, front-end read structurally invalid |
| **SNDK** | sweep-tracker (Tier C) | $13.5M 2-DTE $1,500P ask-buy is real urgency, but ΔOI is balanced calls/puts |
| **INTC**, **AMD**, **PLTR**, **MRNA** | sweep-tracker — **downgraded** | "Bearish" persistence labels contradicted by call-dominant ΔOI; put-sale netting artifacts |
| **IBIT** | sweep-tracker (3/5 threshold) | Long-dated call buying reads as a BTC-macro LEAP bet, not urgent sweep flow |

**Dropped by the C12 liquidity floor (16):** GRRR ($15.6M ADV), MSOS ($4.85), EWN ($8.3M), CABA ($3.25), METC ($25.0M), ZURA ($8.0M), JMIA ($12.3M), SHOE ($8.0M), MEC ($16.0M), BCAX ($17.2M), FHTX ($2.1M), VYX ($18.7M), WHF ($0.4M), AVD ($2.21), PSTL ($7.3M), BEAM ($46.5M).

> **Note on the bullish funnel.** **Seven of the ten** names in the `uw` bullish signal-confluence funnel failed the liquidity floor (GRRR, MSOS, EWN, CABA, METC, ZURA, JMIA). Only MTCH, CI and GEO survived. The bullish top-of-funnel today was dominated by illiquid micro-caps — a structural reason the long book was thin before any agent formed a view.

---

## Appendix — run integrity

- **10 Phase 1 agents** spawned (not 11/12). `opex-pin-strategist` **correctly omitted**: August monthly OPEX was **2026-08-21**, five days *before* the data date, so that book has expired; next monthly is 2026-09-18 (23 days out). The ±5-calendar-day guard is symmetric and would have fired on the post-expiry side, but `uw oi pin-risk` has no expiry-selection flag and would have returned the Aug-28 weekly mislabeled as an OPEX pin. *(The command header says "11 Phase 1 agents"; its own Step 1 enumeration lists 10 unconditional agents plus the conditional OPEX one. The enumeration was followed.)*
- **Step 0 cache:** 22/22 market-wide payloads written, zero failures. No agent re-fetched a cached payload.
- **`fz` lanes:** breadth cross-check and squeeze/RS candidate surface **skipped** (look-ahead, see §6). Per-ticker `fz_enrich` lagged structural fields used. `fz screen` also re-confirmed the **doubled-first-letter ticker bug** on 20/20 rows (AABEO, OOKTA, BBBY→BBY) — de-doubled before any use.
- **`yahoo_fundamentals` inside `uw insights deep-dive` returned HTTP 401** on all three top names — that enrichment leg is down; Finnhub carried fundamentals instead.
- **Helper test suite:** 423 tests pass.
- **Watchlist write-back:** `no-op — zero LOW+ names`. All seven candidates are DROP tier (below the LOW floor of 3), and the corrected 2026-07-23 rule writes only LOW-or-better. `conviction_2026-08-26` was **not created**; no `uw watchlist manage` mutation issued.
- **Short-lane generation note.** DIS was the **only** short thesis produced — 1 of 7 candidates, **14.3%** of the board — against a tape with 34.7% bullish flow breadth, 4,105 bearish vs 2,183 bullish tickers, SPY below its 20SMA, and a stagflationary macro print. The 2026-08-22 audit measured short-thesis *generation* halving (32.0% → 17.6%, p=0.00035; regime-controlled 31.3% → 17.4%, p=0.0045) while routing compliance stayed perfect. **Today sits below even that drifted rate.** A tape this bearish producing one short candidate is a Phase-1 screening signal, not a clean board. Flagged for the next audit: this is the population the counterfactual needs to stay falsifiable, and it is not accruing. *(Trailing 15-session short share is 22.3%, so the lane is not dead — but today is an outlier low.)*
