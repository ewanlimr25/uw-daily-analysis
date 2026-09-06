# Daily Market Analysis — 2026-09-01

## Executive Summary

- **Regime + GEX state:** TRANSITIONAL / PULLBACK_IN_UPTREND. SPY 761.78, below the 20sma (769.21), above the 50sma (754.71), −2.26% from the 90d high. VIX +9.52% → 16.34. Breadth 31.1% bullish — independently corroborated by `fz` at 31.41% green (158 adv / 342 dec). **Both index books are short-gamma with their heaviest negative-gamma strike essentially at-the-money** (SPY 760, +0.20% from spot; QQQ 708, +0.06%). Sector lean: only XLE is green on both 1d and 5d (+1.27 / +4.37); defensives green on the day; XLY/XLI worst.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL/PULLBACK_IN_UPTREND) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** SPY — short-gamma, ZGL null (unreliable), call wall 780 (+2.43%), put wall 760 (+0.20%); regime **held** (negative 7 of 8 sessions). QQQ — short-gamma (total_gex −$1.06B **while the tool's own label reads POSITIVE**), ZGL 235.03 is extrapolated garbage, call wall 730 (+3.16%), put wall 700 (−1.07%); regime **fresh-flip, lower confidence**. Neither index offers a credible pin. Advisory — see §2.
- **Top swing build:** **None.** One name (IWM) cleared the `raw_score ≥ 3` drop floor in a 25-name union, and it is a directional short, which routes terminally to `watch_only`.
- **Top LEAP candidate:** **None.** Zero of six screened names cleared even Gate 4 of nine.
- **Biggest risk:** Not a position — it is the **calendar against a short-gamma book**. Jobless claims 9/3, **NFP 9/4 pre-open (T+3)**, Labor Day 9/7 closed, **CPI 9/11 (T+7)**, **FOMC + dot plot 9/15–16 (T+10)**. Dealers are hedged short gamma exactly where price sits, so a gap through those shelves gets amplified rather than dampened. The correct expression of that view today is **no exposure**, which is what the gate stack produced.

**This is the 40th consecutive empty daily conviction board** (verified by globbing `analyses/daily/*/decision.json` only; last sized daily board **2026-07-07**). It is the frozen rubric behaving as calibrated, not a failure to find ideas.

---

## 1. Regime & Gamma State

`uw risk market-regime` returns **TRANSITIONAL — "Half position sizes. Favor defined-risk strategies. Iron condors in range."**, trend **PULLBACK_IN_UPTREND**. Market breadth 1,957 bullish vs 4,330 bearish tickers = **31.1% bullish**.

The tape is a **broad** decline, not a cap-weighted artifact — this distinction was checked before it was written into any agent prompt:

| | SPY | QQQ | IWM | RSP (equal-wt) | VIX |
|---|---|---|---|---|---|
| 1d | −0.69% | −1.27% | −1.14% | −0.82% | **+9.52% → 16.34** |
| 5d | −0.54% | −0.43% | **−2.89%** | −1.96% | +3.09% |
| rv20 / rv60 | 7.0 / 11.3 | 12.8 / 20.6 | 11.7 / 13.8 | 10.2 / 10.1 | — |

Equal-weight (−0.82%) is *worse* than cap-weight (−0.69%), and `fz`'s independent advance-decline lineage agrees with the UW regime label almost exactly. **IWM's −2.89% 5d underperforms even RSP by >90bp** — a size/credit-sensitivity risk-off leg, not a mega-cap divergence story.

**Per-index gamma (current-state EOD book; §2 carries the forward read):**

| | spot | zero-gamma | total GEX | regime (derived from sign) | call wall | put wall |
|---|---|---|---|---|---|---|
| SPY | 761.49 | `null` (unreliable) | **−$1.597B** | SHORT GAMMA (label FULLY_NEGATIVE, consistent) | 780 (+2.43%) | 760 (**+0.20%**) |
| QQQ | 707.58 | 235.03 (extrapolated, unreliable) | **−$1.064B** | SHORT GAMMA (**label says POSITIVE — contradicts its own sign**) | 730 (+3.16%) | 700 (−1.07%) |
| IWM | 290.41 | noisy/unreliable | negative 8 of 10 sessions | SHORT GAMMA | — | 280 strike at **−$172.2M** |

**`uw options-flow dte-volume-share`:** 0DTE 29.6% / weeklies 28.3% / monthlies 27.2% / LEAPs 4.4% — `regime_hint: BALANCED`. Neither a retail 0DTE tape nor an institutional-positioning tape; no directional benefit-of-the-doubt available from this axis. The thin 4.4% LEAP share is itself context for §4's empty result.

**`uw historical vrp`:** SPY **FAIR +0.0106** (IV30 13.01% vs RV30 11.95%) · QQQ **NEGATIVE −0.0254** (IV30 18.20% vs RV30 20.75%). **Index vol is cheap-to-realised on the Nasdaq complex** — a long-vol-favourable, short-vol-hostile backdrop. This is a live gate, not colour: it fired on every short-vega structure below.

**Macro backdrop** (`scripts/fred_macro.py`): yield curve **normal +0.40** (10Y 4.75% flat 30d, 2Y 4.34%); core CPI **2.79%** YoY; core PCE **3.34%** YoY; unemployment 4.1%; **payrolls −23k MoM (negative)**; USD weakening (−2.04 on the broad index over 30d); fed funds 3.63%.

> **A negative payrolls print with core PCE still at 3.34% is a stagflationary tilt** — weak growth *and* limited room to cut. This matters more than it looks: it is the single fact that killed the strongest bull argument on the board (the "weak jobs → dovish Fed → small-cap relief rally" case for IWM), and it cuts against small-caps on both legs, since IWM constituents are disproportionately floating-rate and credit-sensitive.

**Forward `event_risk` — a wall-to-wall Tier-1 calendar.** Trading-day arithmetic from T+0 = 2026-09-01, with 9/7 Labor Day excluded:

| Date | T+ | Event | Tier |
|---|---|---|---|
| 2026-09-03 Thu | T+2 | Weekly jobless claims | MED |
| **2026-09-04 Fri** | **T+3** | **NFP / Employment Situation, 8:30am ET** | **HIGH** |
| 2026-09-07 Mon | — | Labor Day — market closed | — |
| **2026-09-11 Fri** | **T+7** | **CPI (August)** | **HIGH** |
| **2026-09-15/16** | **T+10** | **FOMC + SEP dot plot, decision Wed 2:00pm ET** | **HIGH** |

Essentially every horizon on today's board contains a Tier-1 event. NFP at T+3 fired the event-risk gate on nearly every call.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — open interest that persists overnight — read forward as the *prior* for the next session's open. **Prose-only, 0 rubric points, no backtested predictive claim.** Predictive validation of these levels lives in `/weekly-analysis`'s rolling §2 backtest. Scope is SPY and QQQ only.

**SPY — short gamma, held, no pin.** `total_gex` −$1.597B, the most negative print of an 8-session window (negative in 7 of 8; a single positive blip on 08-27 reverted immediately). The negative concentration is not a distant floor: strikes **757–765 bracket spot and each carries −$25M to −$289M**, with **760 — essentially at spot — the single most negative strike on the entire grid**. The nominal "put wall" at 760 is 0.20% away and **will not act as classical support**; in short gamma a break below it accelerates as dealers sell into the drop to stay hedged. 780 is the only meaningful positive-gamma pocket. `zero_gamma_level` is `null` (FULLY_NEGATIVE day) ⇒ `zgl_reliable: false`; the read rests entirely on the `total_gex` sign plus spot-vs-wall geometry.

**QQQ — short gamma, fresh flip, lower confidence.** `total_gex` −$1.064B. ⚠️ **The tool's `regime` label prints POSITIVE and contradicts its own `total_gex` sign** — the documented 3-of-4-session defect, caught and overridden here. More important than the nominal walls: **strike 708, +0.06% from spot, carries −$367M — the largest-magnitude strike on the grid, ~3× the nominal 700 put wall.** The 700–711 band is uniformly and deeply negative. The trailing week alternates sign day to day, so today's decisive flip — coincident with QQQ −1.27% and VIX +9.5% — reads as **event-driven and fresh**, not a held regime. ZGL 235.03 sits ~470 points below spot: extrapolation artifact, ignore entirely.

**Structure bias, both indices:** short-gamma with peak negative gamma at-the-money ⇒ **no credible pin to sell around**. Favour debit verticals / directional 0DTE in the break direction; a long straddle is defensible given walls are wide relative to the negative trough. QQQ's negative VRP (IV30 18.20% < RV30 20.75%) reinforces a long-gamma tilt over premium selling.

**Mandatory caveats:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and re-computes the walls. SPY has no ZGL at all today, so there is no flip level to anchor to — only the sign.
- **ZGL unreliable on both names** (`zgl_reliable: false`): SPY null, QQQ extrapolated deep-OTM.
- **Gap risk voids the prior, and it is acute this week.** Jobless claims land 9/3 and **NFP 9/4 pre-open**, both inside the window this prior is meant to inform. A gap through the 757–765 (SPY) or 700–711 (QQQ) negative shelves would be **compounded by dealer hedging**, not faded. QQQ's higher beta (rv20 12.8 vs SPY 7.0) means it compounds faster.
- **Tooling limit:** `uw` cannot isolate the D+1 expiry (`gex --dte-max 1` errors). This is the standing 0–45 DTE book — the best available proxy, not the isolated next-session expiry.
- **ETF book**, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py`)

Advisory, delta-neutral, **0 rubric points**, and explicitly **not a guaranteed edge** — the validation sample contains no vol shock, so the short-vol left tail is **unsampled**.

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` / VIX | **MID** / 16.34 | **MID** / 16.34 |
| implied move | 0.80% | 1.11% |
| `expected_range_pct` (wing width) | **±1.08%** | **±1.81%** |
| `size_scalar` | 1.0 | 1.0 |
| backtest verdict | `GO_PREMIUM_SELL_INTRADAY` | `GO_PREMIUM_SELL_INTRADAY` |
| MID-tercile mean PnL, **gross** | +0.202% | +0.326% |
| **net of the 0.1% assumed round-trip cost** | **+0.102%** | **+0.226%** |
| `stand_aside_reason` / `caution` | none | none |

`pnl_basis` is **percent-of-underlying-spot notional, GROSS** — not premium-collected, not margin-relative. Leading with net, as required: **+0.102% / +0.226%** are small absolute numbers, and the gross 88.3% / 86.7% win rates overstate a negatively-skewed seller's edge. **Vol state is MID, which matters** — this lane is net-negative-to-zero at LOW VIX, and today's tercile bounds (15.8 / 17.3) put VIX 16.34 in the middle bucket where the edge actually lives.

**⚠️ Standing tension between §2 and §2a, stated rather than buried.** The script says sell premium; the gamma map says both books are short-gamma with no pin. The script itself partly registers this — its `suggested_structure` reads *"wider iron condor … (short-gamma: wider range / trendier) — **or reduce / stand aside**."* The honest synthesis: **if this lane is traded at all, use the wider wings (±1.08% / ±1.81%), not the tighter implied move, and stand aside on any gap** — the 9/3 claims and 9/4 NFP prints are exactly the gap risk the entry rule exists to avoid. Entry rule unchanged: enter at/after the open once the gap resolves, hold to the close, **never carry overnight**. SPY ≈ SPX (validated identical); **QQQ is the weaker instrument** (Nasdaq index book unavailable) — flag its lower confidence.

**Promotion bar (unchanged):** this lane stays advisory / 0 rubric points **permanently** until both a vol-shock day enters the sample and net expectancy clears a tail-aware bar. Win-rate is explicitly *not* the promotion metric for a negatively-skewed short-vol strategy.

## 2b. Swing Dealer Positioning (1–4 weeks)

All DEX verdicts computed by `scripts/dex_flip.py` off 13 dated `uw options-structure dex --date` snapshots per symbol (2026-08-14 → 2026-09-01) — not by hand.

| symbol | net_dex (09-01) | mechanized flip? | evidence | whipsaw |
|---|---|---|---|---|
| **SPY** | **−$15.37B** | **QUALIFIES, SHORT** | +$13.54B (08-31) → −$15.37B; prior 5 sessions all positive; \|flip\| vs floor $3.54B ⇒ ratio **4.35** | ⚠️ **TRUE** — 5 sign changes in 13 sessions |
| **QQQ** | **−$11.59B** | **QUALIFIES, SHORT** | +$16.63B (08-31) → −$11.59B; prior 5 positive; ratio **3.70** | FALSE — 3 sign changes (cleaner) |
| IWM | −$16.81B | **NO** — "a DEX level is not a flip" | negative 7 of 8 sessions; **deepening −0.56B → −6.76B → −9.02B → −16.81B** | — |
| MU | +$4.78B | **NO** — 0 sign changes, positive all window | a stale positive level | — |
| TSLA | −$187M | **NO** — 9 sign changes / 13 | pure noise at this magnitude | ⚠️ TRUE |

**No vanna squeeze fires anywhere.** Every index book is put-heavy (SPY net_vanna +78,443; QQQ +65,968; IWM +232,940 — the largest) but **VIX is rising, not falling** (dated ^VIX: 08-27 14.51 → 08-31 14.92 → 09-01 16.34). The falling-VIX leg is unsatisfied, so the classic dealer-buy-to-cover mechanism is explicitly not in play. Classified "vanna pressure, not squeeze." If VIX rolls over and prints three consecutive lower closes, re-check immediately — the put-heavy books are loaded and waiting.

Front-end IV ratios at `--near-dte 7`: SPY 0.835, QQQ 0.753, IWM 0.712 — **all CONTANGO, no front-end panic** despite today's VIX pop.

> **The caveat that governs both qualifying flips:** SPY and QQQ flipped **on the same session as the selloff and the VIX spike**. Dealers re-hedging a move that already happened is at least as plausible as dealers leading one. Combined with a negative-gamma book into a loaded calendar, the honest framing is a **volatility-expansion / momentum-confirmation signal, not a standalone directional entry** — wait for post-NFP confirmation rather than pre-positioning into Thursday/Friday data. IWM tells the same directional story with better trajectory evidence but **structurally cannot earn the +1**, which is the rubric line working exactly as designed.

## 2c. Sector Rotation

**Rotation regime call: `no_change`, confidence LOW.**

Direction is taken from the **netted** `uw risk market-regime.sector_rotation` only (C55). `sector-flow` and `sector-flow-persistence` are **one gross-turnover source**, sign-agnostic, and cannot express direction — they are a durability filter.

⚠️ **Persistence had zero discrimination today: it printed INFLOW or ROTATING on 11 of 11 sectors, 6 of them at exactly 1.0.** Population firing rate 100%. Used only as a durability check on sectors already confirmed by the netted source; never to rank or select.

| Sector | Netted (directional) | Gross (turnover) | Persist | Verdict |
|---|---|---|---|---|
| **Technology** | **−$160.4M OUT** (largest) | **+$2.14B IN** | 1.0 | ⚠️ **DISAGREE → watch_only** |
| Communication Services | +$46.1M IN | +$350.6M IN | 0.8 | **AGREE, above-median → confirmed IN** |
| Healthcare | +$26.6M IN | +$193.1M IN | 1.0 | **AGREE, 5/5 days positive → confirmed IN** |
| Utilities | +$9.1M IN | −$47.9M OUT | 0.6 | DISAGREE → watch_only |
| Consumer Cyclical | −$46.1M OUT | +$135.6M IN | 0.8 | DISAGREE → watch_only |
| Industrials | −$24.8M OUT | −$18.6M OUT | 0.6 | agree but sub-median magnitude → context only |
| Energy | *not in top-3/bottom-3 (unknown)* | +$543.3M (**6× day-jump**) | 1.0 | **watch_only** — see below |

**Adjudication — the Technology contradiction.** Netted −$160.4M against gross +$2.14B is explained by the screener split: **11 of the top-25 bearish-flow names are mega-cap tech** (DELL, MSFT, MU, MSTR, NVDA, AVGO, PLTR, CRWD, MDB, PANW, AMD, ORCL) against a thinner bullish set (AAPL, SNDK, STX, ARM, MRVL, TEAM, AAOI) — **real distribution in breadth offset by concentrated call buying**, netting to a large gross positive but a negative netted read. The ETF tape corroborates: XLK's own dark-pool prints are mixed-sign near mid with no clean tilt, and its sweep tape is split bid/ask on near-dated calls. That is two-way churn, not accumulation. **Technology is watch_only, confidently.**

**Adjudication — the Energy spike.** The daily series is 55.4 → 58.2 → 59.0 → 90.3 → **543.3** ($M): four stable days then one outlier session. `persistence_score` 1.0 captures **sign** consistency only, never magnitude consistency, so it does not validate the jump. Energy also has **no netted read at all** (unlisted in the top-3/bottom-3 truncation — *unknown, not zero*). Critically the ETF tape does **not** confirm it: XLE 5d net premium is a trivial **+$2.21M/MIXED**, XOP −$0.28M/MIXED. The price strength (XLE +1.27%/+4.37%, USO +5.46%/+11.77%, PBR +5.06%/+9.30%) plus a `fz` new-high list dominated by energy (HP, DK, UGP, EQNR, OKE, MPC) looks driven by **spot/cash oil and a weakening USD, not durable options positioning**. **Fails the ≥3-day persistence bar → appendix/watch-only, not a rotation call.**

**Single-name leaders — only META clears the conditional +1.** (a) CommSvcs persistence 0.8 ≥ 0.6 ✓ (b) cum_flow_30d +$62.4M aligned ✓ (c) ≥ $50M ✓. ⚠️ **Double-count declared:** conditions (b)/(c) test the *identical field at the identical threshold* as the standalone cum-flow line, and (a) fires on everything — two rubric lines carrying one bit. **GOOGL fails (b)** — cum_flow_30d **−$126.4M misaligned** against a +$8.5M one-day pop. **MRNA fails (c)** (+$27.3M) and **BSX fails (c)** (+$4.2M).

**ETF flow tape (advisory — 0 rubric points).** 21 ranked, top-3/top-3 deep-pulled, 37 calls total (under the 40 cap).

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| XLK | inflow +$13.37M | bullish | mixed-sign near mid, no tilt | mixed 9/4 calls both sides | **disagree** (netted OUT) | — (skip) |
| IGV | inflow +$11.40M | bullish | one quote glitch | small, mixed | **disagree** | — (skip) |
| XLI | inflow +$4.83M (thin) | bullish | blocks **below mid** (sell-tilt) | **~$64M Nov-20 put buying** | **disagree** | — (contradictory) |
| GDX | outflow **−$20.68M** | bearish | large above-mid blocks | **all-put sweep tape** | n/a | instrument-only, price-confirmed (−3.9%/−10.3%) |
| EWY | outflow −$11.23M | mixed | one $148.5M ambiguous block | mostly `no_side` | n/a | inconclusive |
| KRE | outflow −$3.99M | bearish | modest | put-skewed (Oct 72P) | **disagree** vs FinSvcs gross | instrument-specific weakness |

**Not one deep-pulled ETF produced `gics_agreement: agree`.** Nothing here strengthens a rotation call; XLK/IGV/XLI actively argue for downgrading conviction. **Swing-book implication: no high-conviction sector trade today.**

---

## 3. Swing Setups (1–6 weeks)

**Empty. One name (IWM) cleared the `raw_score ≥ 3` drop floor out of a 25-name union, and it is a directional short, which routes terminally to `watch_only`.** The full scored board is in §7.

### 3a. Long swings (regime-aligned)

**None sized.** The three long-side candidates all failed on their own evidence:

- **META** (raw 2, `sector_rotation`) — **both its points are one bit of information**, declared as a double-count by two agents. The bear then landed the decisive blow arithmetically: **5d flow (+$132.4M) exceeds the entire 30d (+$62.4M), which means the prior 25 days netted ≈ −$70M.** The "acceleration" is a single recent burst sitting on a month of net distribution. Against it: insider **MSPR −55.84** with net selling in 18 of 20 months, a last print that **missed by −16.0%** breaking a three-quarter beat streak, and a name-specific Tier-1 `FLOOR_PUT_BLOCK`. *In fairness to the long side:* the 10-day tape is **8 bullish / 2 bearish** flow-days and today's largest OI add is a **Jan-2027 830C, +30,737 contracts (~$18.8M, 43% OTM)** — a genuine long-dated bullish convexity build the LEAP screen missed because it filters at `--min-dte 180` and this sits at dte 136. The bear's "month of distribution" therefore has to live in days 11–30. Debate **bull 0.35 / bear 0.75**.
- **BSX** (raw 1, `multileg_directional`) — the day's cleanest piece of detective work, and it went against the trade. The multileg agent flagged that the rich front end (dte-3 IV **64.3%** vs a 43.2% back month) implied *a near-term catalyst it could not identify*; the fundamentals gate found it — **2026-08-28: "Boston Scientific says cyberattack has disrupted product manufacturing."** The front-end richness is **disruption premium, not bullish anticipation**. Then a third, entirely independent instrument converged: the panic gate read **1.219 BACKWARDATION at `--near-dte 7` on a name with no scheduled catalyst for 57 days** — front-end richness with nothing on the calendar to explain it. The bull's load-bearing argument (insiders bought *through* the incident window, MSPR +91.7 Jul → +100 Aug) was dismantled cleanly: **MSPR is a monthly aggregate**, and the 08-28 disclosure leaves only two trading days of August, so the within-month sequence cannot be established from this data. Also noted: insiders buying stock at $48 is not the same bet as a **25%-OTM Dec-18 call spread needing +25% in 108 days**, and there is a **competing Dec-18 45P build (+749)** at the same expiry. Debate **bull 0.35 / bear 0.65**.
- **SNDK** (raw 1, `vol_long`) — **the cleanest near-miss on the board**: the only fundamentals **CONFIRM**, the only **bull debate win** (0.70 vs 0.35), sitting in the fleet's one validated lane — and killed by score alone. See §5.

**No `distribution_flag` was raised on any long name today** — accumulation-hunter returned a clean board, so the C28 counter-signal had nothing to attach to.

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only` (2026-08-01 P0 #1) — routing, not suppression.** Theses are generated, scored, fully gate-verdicted and serialized so the counterfactual keeps resolving.

- **IWM — SHORT, `watch_only`. raw_score 3, the only name above the drop floor.** Laddered put verticals **285P/275P expiring 2026-09-11 — CPI day itself** — exact size match 166,080/166,080, ~$19.6M net debit, dte 10. The term structure anchors it: hygiene shape **KINKED** (the raw label said CONTANGO and flipped), with the 09-11 tenor a qualifying kink at 6.8% prominence on a thick 5,366-contract tenor. `multi_day_repeat = 5` — the same thesis **re-struck progressively lower for five sessions** as IWM bled 305 → 290. The 280 strike sits in a **−$172.2M net-GEX trench**. cum_flow_30d **−$250.4M**, aligned, 9.2× the union median, parity screen clean both directions.
  **New corroboration from the §6 deep-dive that neither debate side had:** IWM's four largest OI adds today are **all puts across three separate tenors** — 282P (dte 17, +36,744), 280P (dte 3, +21,091), 279P (dte 45, +20,452), 280P (dte 45, +15,752). Put building at dte 3, 17 *and* 45 materially weakens the bull's "this is a single CPI-day event hedge" reading; a one-off event hedge does not build across a 45-day curve.
  **Honest counterweights:** `cum_flow_5d` is **−$5.52M, effectively flat** (0.58% of 5d gross) — the 30d accretion is *not* freshly reinforced at the premium layer; the structure's expiry **is** the CPI print, making it an event bet rather than a trend bet; and **hedge-vs-directional intent is genuinely unresolvable** from available data — both debate sides conceded this. Debate **bull 0.25 / bear 0.65**.
- **QQQ — SHORT, `watch_only`. raw_score 0.** Buy 690P / Sell 665P expiring 2026-09-25 (dte 24), matched **twice** (33,216 + 22,142 on both legs), ~$20.25M net debit, spanning NFP + CPI + FOMC. The buyer placed the expiry **past** the CPI kink in a local vol trough — buying the event window at cheaper vol than the kink itself commands. Earned +2 multileg and +1 DEX flip, then **lost 3 to `flow_conflict`** — see the defect note in §7.
- **SPY — SHORT, `watch_only`. raw_score −2**, the only negative on the board, entirely from the same `flow_conflict` mechanism.
- **Contrarian lane: EMPTY.** A 27-name scan found **zero BULLISH_EXTREME** anywhere — the −2 line mechanically requires one to trigger. The five BEARISH_EXTREME prints (IWM z=4.496 — the day's most extreme; SLV 3.777; TEAM 2.722; NVDA 2.346; MSTR 2.126) are all disqualified: IWM out-of-scope for a fade, TEAM shows flow *aligned* not divergent, NVDA's IV rank is 5.16 (basement-cheap, nothing to sell), MSTR/SLV are crowd-and-flow-**agree** continuation setups rather than crowd-is-wrong setups. Separately, **`pc-ratio-zscore` has no `--date` flag**, so a "rising" multi-date z trajectory was **unearnable for every name** — the −2 line could not have been awarded today even had a bullish extreme existed.

### Sweeps (informational — 0 rubric points)

The sweep-persistence rubric line was removed 2026-05-23 (P0.3) after two audits measured −22pp marginal contribution. Ranked persistence-first; **firing rate 20 of 26 (76.9%) cleared ≥3-of-5**, which is wide enough to confirm the weak discrimination that got the line removed.

| Ticker | Tool's 5d tag | Persist | 5d premium | Read |
|---|---|---|---|---|
| MU | bearish | 5/5 | $2.59B | **Contradicts** — today's tape is near-balanced call ask/bid at adjacent strikes; 0DTE-adjacent MM churn |
| PLTR | bearish | 5/5 | $477.8M | Mixed — LEAP call *and* put buying; the one near-term print is `no_side` |
| MSTR | bearish | 4/5 | $749.5M | **Contradicts** — actual prints skew call-side; one $40C expires **on NFP day** |
| AMD | bearish | 4/5 | $454.0M | **Contradicts** — mixed LEAP legs; the dated print is bullish call-ask |
| **MRVL** | bearish | 3/5 | $507.5M | **Most internally consistent** — put-skewed, tool-aligned (09-25 $270P ask, $3.1M) |
| GLD | bearish | 3/5 | $411.5M | Real but reads as **distribution/unwind** — LEAP calls repeatedly hit on the *bid* |

**No clean first-class directional name today.** Every mega-cap/index persistence name (SPXW, SPY, NVDA, QQQ, TSLA, META, AAPL, MSFT, AMZN, AVGO, IWM) is demoted as unverified hedge flow. **Event exposure:** MSTR's $40C expires *on* NFP; PLTR $140C, AMD $300C and MRVL $270P all span NFP + CPI + FOMC in a single structure.

**The tape-wide fact that frames all of it:** today's raw single-leg whale scan is **135 of 207 `CLOSING_ANTISIGNAL` (65%)**. Two-thirds of large single-leg prints are position *closing*, not opening — and per Pan-Poteshman, only opening flow predicts.

---

## 4. LEAP Builds (6–24 months)

**Empty. Zero of six screened names cleared even Gate 4 of nine** — a clean refusal, not a failure to look.

`uw oi biggest-increases --min-dte 180` returned mostly **puts** (SPY 700P, PCG 10P, LUV 47.5P, XEL 70P, EEM 52P/65P, IWM 250P) — excluded by construction as non-DIRECTIONAL_LONG. C12 eliminated LCID ($4.55 < $5) and GRRR ($16.6M ADV). The four surviving call-side builds all failed:

| Ticker | Gates | Why it died |
|---|---|---|
| **BMNR** | 1/9 | $20C dte199, OI +9,719 ask-dominant — but cum_flow_90d **−$19.66M**, `institutional-accumulation` says **DISTRIBUTION** (buy/sell 0.54), conviction-matrix flips to **DIRECTIONAL_SHORT** (23.4%). A local pocket of buying inside a broader distribution tape — exactly the false positive the aggregate gates exist to catch. |
| **NFLX** | 2/9 | $120C dte289 ask-dominant, and `institutional-accumulation` is the one clean lane (buy/sell 2.3) — but cum_flow_90d **−$318.05M** and conviction-matrix confidence **20%** vs a >70 requirement. Price already +17.9%/30d: chasing, not accumulating. |
| **QXO** | 0/9 | The "build" is **bid-dominant on both strikes** (16,038 bid vs 1,086 ask on the $22C) — call *selling*, never a long candidate at source. cum_flow explicitly BEARISH. |
| **GAP** | 0/9 | Bid-dominant again (484 bid / 159 ask); cum_flow +$2.27M/90d is immaterial and flat — no accretion shape. |

**`oi-trend` BUILDING population: 2 of 2 checked hit the 10-day ceiling** — the known zero-discrimination defect reproduced verbatim. Treated as a non-differentiator.

**Macro context for the refusal:** the LEAP tape is thin at **4.4% of DTE volume share**, and a thin tape produces exactly the low-quality prints seen here (two of four "builds" were premium-selling). Layered on a **stagflationary tilt** — negative payrolls against 3.34% core PCE — underwriting a fresh 6–24 month directional-long options thesis today would mean adding duration risk precisely when multiple expansion compresses and real financing costs rise.

---

## 5. Volatility Surface

**Macro-beta reference, computed first (every single-name kink is checked against it):**

- **SPY kink_dte = 3 → 2026-09-04 = NFP day.** front_end_ratio(7) 0.836.
- **QQQ kink_dte = 10 → 2026-09-11 = CPI day.** front_end_ratio(7) 0.752.
- Full macro dte set across both index curves: **{3, 10, 17, 29}** → NFP, CPI, OPEX/FOMC-adjacent, month-end.

`expiry_heatmap` confirms this structurally: **2026-09-18 (OPEX) is the #1 premium-concentration expiry ($3.64B) and 2026-09-04 (NFP) is #2 ($3.12B)** market-wide. The front-tenor IV spikes below are a real, broad phenomenon.

**⚠️ Substrate hygiene — mandatory, and it mattered enormously.** Classifying from the raw `iv-term-structure` label would have been wrong on the majority of names: **raw → hygiene `shape` flipped on 10 of 16 (62.5%)**, and the raw label returned **zero CONTANGO in 16 names**. `min_contracts` = 15 (a named, tunable, **not audit-frozen** parameter). Panic firing rate at `--near-dte 7`: **7/16 (43.75%) above 1.05, 4/16 (25%) above 1.10** — healthy discrimination, unlike the CLI default of 1 which fires on nearly everything.

**⚠️ `iv-percentile-zscore` short-delivered fleet-wide — `dates_used` = 99 of 252. Every IV-percentile figure below is PROVISIONAL.**

### BUY VOL — the unconstrained lane

| Ticker | shape (raw → hygiene) | kink dte | macro-beta check | VRP | IV-pctile | implied move | Verdict |
|---|---|---|---|---|---|---|---|
| **SNDK** | BACKWARDATION → BACKWARDATION (**unflipped, no kink**) | — | **CLEAN** | **−0.6151** (book's strongest) | 1.01 | **7.91%** | **BUY VOL — cleanest read on the board** |
| PLTR | **CONTANGO → BACKWARDATION** (flipped both) | — | clean | −0.5538 | 10.1 | 5.14% | BUY VOL |
| MRVL | BACKWARDATION (kink fails prominence 3.0%) | — | clean | −0.3413 | 11.1 | 7.04% | BUY VOL, lower conviction |
| IREN | BACKWARDATION → **KINKED** | **17** | ⚠️ **IN macro set**; prominence 5.1% barely clears | −0.5334 | 0 | 18.16% | BUY VOL, discounted |
| ARM | KINKED, **92.2% prominence** | **17** | ⚠️ **IN macro set**; prominence almost certainly OPEX contract-concentration | −0.24 (weak) | — | 29.62% | **Both confirming legs compromised** — mechanically +1, substantively noise |
| DOCU | — | earnings 9/3 | — | **−0.056** PREMIUM_BUYING | — | **13.97%** | BUY VOL — RV20 58.0 / RV60 56.3 consistent, **not** a stale-gap artifact |
| CIEN | — | earnings 9/3 | — | **−0.051** | — | **14.72%** | BUY VOL — RV20 74.3 / RV60 77.4 persistently high, genuine |

**SNDK is the standout and deserves its own paragraph.** It is the only name in the book whose term structure is **unflipped, macro-uncontaminated and kink-free**, carrying the **strongest VRP in the entire book (−0.6151** — IV30 69.7% vs RV20 87.5% / RV60 127.1%), the **only fundamentals CONFIRM**, and the **only bull debate win (0.70 vs 0.35)**. It sits in `vol_long` — the fleet's one genuinely validated lane (+9.5pp vs unselected same-date peers, n=43, paired McNemar p=0.0034, 5-for-5 on every sized row in the corpus). It is nonetheless **unsizeable**, because `vol_term_dislocation` maxes at **1 rubric point** and therefore cannot clear the DROP floor by construction. That is a **registered coverage gap in a frozen rubric**, and SNDK is today's clean instance of it — recorded, not worked around.
*The bear's live objections, which stand:* RV60 (127.1%) ≫ RV20 (87.5%) is a **decelerating** vol regime, so part of the "cheap" gap may be the market correctly pricing further decay; the 3-day tenor **spans NFP**, so some of the 87.28% front IV is legitimate event premium rather than dislocation; and accumulation-hunter independently found a **$184.8M pre-market cluster = 23.7% of SNDK's 30d net flow**, raising the possibility the setup is flow-manufactured and could compress abruptly.

### SELL VOL — all route to `watch_only`

Generated in full, scored and serialized; **routed, not deleted**. `vol_short` books **−25.1pp** against unselected same-date single-name peers (n=111, paired McNemar p<0.0001), negative in **4 of 4 regime buckets**, and represents **20 of the 48 sized rows in the entire corpus history**.

| Ticker | Earnings | implied move | VRP | Back-month skew | Note |
|---|---|---|---|---|---|
| **AMBA** | **9/3 AMC (T+2)** | **16.80%** | +0.114 | **TAIL_HEDGING +0.165 — the only stretched back-month in the batch** | Earnings lane's highest-conviction call |
| SNOW | 9/2 AMC (tomorrow) | 15.15% | **+0.300** (largest) | flat/COMPLACENT | one confirming leg only |
| PATH | 9/3 | **19.49%** (largest) | +0.124 | flat | raw kink is a **mislocation** off a 362-contract hump — disregarded |
| ZS | 9/3 | 16.12% | +0.162 | NORMAL, not stretched | |
| LULU | 9/3 | 12.15% | +0.172 | flat | ⚠️ its −$488M "bearish" cum-flow is the **deep-ITM parity artifact** — not a directional read |
| CHWY | 9/9 BMO | 15.69% | +0.164 | NORMAL | |
| ORCL | 9/8 | 15.15% | +0.087 (weak) | flat | ⚠️ kink at **dte 10 = CPI day**, 11.1% prominence vs the index's own 6.7–7.2% at the identical dte — only ~4pp of name-specific excess, **heavily discounted** |
| MDB | — | 34.63% | +0.1961 | — | `vol_term_dislocation`; front ratio 1.466 |

**AMBA deserves the scrutiny it got.** It was the earnings lane's best call — the only name where three legs aligned. The debate reframed it convincingly: **the three legs are plausibly one signal wearing three costumes.** A stretched back-month tail skew (TAIL_HEDGING +0.165) is the market **pricing expansion risk**, and selling into that is the *exact documented mechanism* behind `vol_short`'s −25.1pp deficit (selected names realise a 1.132 vol ratio vs a 0.962 peer median). On the specific question of whether AMBA respects its implied move, the record is unfavourable: trailing surprises **+173.7%, +28.0%, +24.3%, +3.6%** — **two of four would have blown straight through a 16.8% move**, not one of four. Add insider **MSPR −99.21** into a T+2 print and **9.72% short float at 2.44 days-to-cover** (a beat stacks a short-cover pop on top of the base move, landing on the vertical's short strike first). Debate **bull 0.28 / bear 0.65**.

### No edge / killed

- **Killed on the stale-earnings-RV falsifier:** **MRNA** (VRP −4.4261 looks spectacular, but RV30 523.9% is dominated by **today's own +9.93% move** — a binary-event artifact that cannot recur inside the structure's tenor), **CRWD** (RV20/60 85.7/73.1 still carries the −6.90%/+16.02% earnings gap), **TEAM** (RV30 120.9% carries the −3.68%/+12.34% gap).
- **GDX** — BACKWARDATION with front ratio 1.135 and **no identified catalyst**: the stated "don't fade it" disqualifier.
- **GLD** — kink at dte 2, one day off SPY's NFP kink at dte 3 ⇒ **macro-adjacent, not idiosyncratic**.
- **MSTR** (kink 24.9% prominence but likely OPEX concentration), **TSLA** (kink dte 38, unconfirmed), **PANW** (front ratio **1.756**, the most extreme in the book, but VRP +0.0457 is essentially FAIR — **the two confirmation legs disagree**, and the dte-24 kink has no identified catalyst; the +1 was **withheld**, not reduced).

**Calendar-spread candidates:** premium is bimodal at **09-18 (OPEX, $3.64B)** and **09-04 (NFP, $3.12B)**, with 12-18 ($2.94B, quarterly LEAP roll) and 10-16 ($2.4B) secondary. Any calendar should anchor its short leg to 09-04 or 09-11 and its long leg to 09-18 or 10-16, never past the 12-18 shelf without explicit reason.

---

## 6. Risk & Correlation

**Macro headline:** stagflationary tilt — **payrolls −23k MoM against core PCE 3.34% YoY**, curve normal +0.40, 10Y 4.75% flat, USD weakening. Forward calendar: **claims 9/3 (T+2), NFP 9/4 (T+3), CPI 9/11 (T+7), FOMC + dots 9/15–16 (T+10).**

**Breadth cross-check (advisory, `fz`):** 158 advancers / 342 decliners, **pct_green 31.41%**, avg change −0.83%, median −0.77%. This **agrees** with the `uw` regime label's 31.1% bullish-flow reading — `divergence_flag: false`. Two independent data lineages concur it is a weak tape; there is no distribution tell hiding behind a green index today, because the index is not green.

### Correlation clusters

⚠️ **New instrumentation defect found, and it materially affected the analysis.** `uw risk portfolio-correlation` **truncates `high_correlations` to 10 rows**. On the full 15-name call the listing bottomed out at **0.717** — meaning **the entire 0.60–0.70 soft-watch band was invisible**, which is precisely the band the mechanical cluster rule adjudicates. It was recovered only by re-running on subsets. A single full-breadth call would have silently hidden it. *(The `sector_breakdown: {"Unknown": 15}` 100%-concentration warning is the separate known-spurious defect — ignored; pairwise matrix used.)*

- **`index_beta_cluster`** — SPY/QQQ **0.923**, IWM/SPY 0.852, IWM/QQQ 0.833. Keeper by raw_score: **IWM (3)**; SPY (−2) and QQQ (0) each take **−1 tier**.
- **`AI_semis_cluster`** — connected component {SNDK, IREN, CIEN, MRVL, ARM}, bridged into QQQ: IREN/CIEN 0.773 · MRVL/ARM 0.747 · SNDK/IREN 0.743 · SNDK/CIEN 0.729 · QQQ/IREN 0.749 · QQQ/ARM 0.746 · QQQ/CIEN 0.717 · MRVL/IREN 0.711 · MRVL/CIEN 0.710 · **SNDK/MRVL 0.700 (exactly at threshold ⇒ cluster, not soft-watch)**. **Tie-break indeterminate** — all five carry raw_score 1 and the specified tie-breaker (`cum_premium_flow_30d` in trade direction) is unavailable for `vol_term_dislocation` rows. **No keeper designated; −1 applied uniformly to all five**, recorded so the gap is auditable rather than resolved by discretion. Non-binding on outcome (all already floored at `skip`).
- **Soft watch (0.60–0.70, surfaced, no penalty):** PLTR/ARM 0.672 · ARM/CIEN 0.624 · QQQ/PLTR 0.602. PLTR is **not** a semis-cluster member (max 0.672).
- **Correlation-clean:** META, BSX, AMBA, EWZ — no pair ≥ 0.543 with each other, the indices, or the semis complex. Their kills are idiosyncratic, not portfolio-structural.

### Gates applied

**Panic gate — it discriminated properly and produced the day's sharpest inference.** Read at `--near-dte 7` (never the CLI default of 1), it fired on **3 of 8**:

| | SPY | QQQ | IWM | META | SNDK | **BSX** | **AMBA** | **MDB** |
|---|---|---|---|---|---|---|---|---|
| ratio | 0.835 | 0.753 | 0.712 | 0.889 | 0.979 | **1.219** | **1.413** | **1.466** |
| | CONTANGO | CONTANGO | CONTANGO | CONTANGO | FLAT | **BACKWARD** | **BACKWARD** | **BACKWARD** |

AMBA (1.413) and MDB (1.466) are backwardated because they report inside 10 days — that is **event premium, and calling it "panic" is a category error** even though the gate mechanically fires. **BSX is the real signal: 1.219 backwardation with no scheduled catalyst for 57 days.** Front-end richness with nothing on the calendar to explain it — and the fundamentals gate independently identified the cause (the 08-28 cyberattack). **Two instruments of entirely separate lineage — a news scan and an IV term structure — converged on the same conclusion.** That is a kill signal, not a setup.

**Fundamentals verdicts (top-5). No VETOs.**

| Ticker | Verdict | Adj | Reason | Next earnings |
|---|---|---|---|---|
| IWM | **NA** | 0 | ETF — no company layer; NA never penalises | — |
| META | **CAUTION** | −1 | `insider_selling_cluster` — MSPR −55.84, selling 18 of 20 months, last print −16.0% | 2026-10-27 (56d) |
| BSX | **CAUTION** | −1 | `news_catalyst_contradicts_thesis` — 08-28 cyberattack, scope/duration unquantified | 2026-10-28 (57d) |
| AMBA | **CAUTION** | −1 | `insider_selling_cluster` — MSPR −99.21 into a T+2 print | **2026-09-03 (2d)** |
| SNDK | **CONFIRM** | 0 | Only CONFIRM on the board; 4-of-4 beats, +175.3% YoY revenue | 2026-11-04 (64d) |

**Event-risk gate.** NFP at **T+3** fired on every structure with a horizon ≥3 sessions. Jobless claims 9/3 is MED tier and correctly **did not** fire. **BSX was exempted** despite NFP at T+3 — its defined-risk Dec-18 debit spread runs *through* all three prints, and stamping −1 on it would be the "tax everything equally" failure the gate's re-scope corrected. AMBA's own 9/3 print is **exempt as the event play itself**, but its post-print unwind lands on NFP morning, which is not.

**Debate gate.** Bears won **4 of 5**; only SNDK passed. Four of five bulls could not clear a coin flip (0.25 / 0.35 / 0.35 / 0.28). No pair was BOTH_SIDES_LOW — every bear cleared 0.55 — but **a board where the advocates *for* the trades average 0.39 residual is a board-level negative signal in its own right**, independent of any individual gate.

**Adverse-flow exit candidates: none — and the reason matters.** `uw watchlist alerts` and `uw watchlist scan` both returned *watchlist is empty*. Direct state-file inspection confirms **`conviction_2026-08-31` does not exist, nor do 08-22 through 08-31**. The last dated daily write-back was **`conviction_2026-08-21 ['IWM']`** — seven consecutive sessions produced no LOW-or-better name. There is no carried book, so no flow reversals to surface, and the fundamentals-drift tripwire is a cold start with no prior snapshot.

**Hedge sleeve: none.** The sized book is empty, so net delta is zero and directional skew is undefined. A hedge on a zero-delta book is not a hedge — it is a naked long-vol position, i.e. a *trade*, and it would have to clear the same gate stack that just rejected everything. The tape genuinely warrants defensive posture (short-gamma at-the-money on both indices, no pin, VIX 16.34 after a +9.5% day, stagflationary macro, wall-to-wall Tier-1 calendar) — but that is an argument for **having no exposure**, which is the position the gate stack already produced. *Conditional, for externally-held long equity only:* a defined-risk SPY put vertical expiring **after 2026-09-04** — not a VIX call ladder, since VIX at 16.34 after a +9.5% day is no longer cheap tail insurance and the negative NDX VRP means index vol is already bid relative to realised.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Empty. No name reached MEDIUM (raw_score ≥ 7); the highest score on the board was 3.** The full scored board follows for auditability.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`, from the 2026-08-30 `/calibration-audit` `phase_3_calibration`:

| Tier | n | Expectancy | Payoff ratio | half-Kelly |
|---|---|---|---|---|
| HIGH | 7 | −2.441% | 0.720 | 0.0 |
| MEDIUM | 19 | +0.104% | 0.948 | 0.0132 |
| LOW | 125 | −2.141% | 0.906 | 0.0 |
| DROP | 542 | **−5.964%** | **0.601** | 0.0 |

**Kelly gate: `ADVISORY_ONLY`** (n=27 closed sized calls vs a required 30; tier × expectancy non-monotone). The win-rate ladder stays live. Note the second-cycle payoff-ratio finding: **DROP's payoff ratio (0.601) is far worse than LOW/MEDIUM (0.906/0.948)** and its expectancy is worst by 3.8pp — the long-running "the trades we refuse beat the trades we take" reading rests on **hit rate alone and does not survive a payoff-aware metric**.

### Full scored board

| Ticker | Dir / class | raw | Tier | Σ components | win_rate | Gates fired | **FINAL** |
|---|---|---|---|---|---|---|---|
| **IWM** | short / `multileg_directional` | **3** | **LOW** | +2 multileg, +1 cum-flow | `null` NA(substrate) | event −1, debate −1 | **`watch_only`** (short routing) |
| META | long / `sector_rotation` | 2 | drop | +1 sector-leader, +1 cum-flow | `null` | fund −1, debate −1, event −1 | `skip` |
| BSX | long / `multileg_directional` | 1 | drop | +2 multileg, −1 flow_conflict_lite | `null` | fund −1, debate −1, **panic −1** | `skip` |
| SNDK | vol_long / `vol_term_dislocation` | 1 | drop | +1 vol-surface | `null` | cluster −1, sector −1, event −1 | `skip` |
| AMBA | **vol_short** / `earnings_vol` | 1 | drop | +1 earnings SELL VOL | `null` | fund −1, debate −1, panic −1, vrp −1, sector −1, event −1 (**six**) | **`watch_only`** (vol_short routing) |
| MDB | **vol_short** / `vol_term_dislocation` | 1 | drop | +1 vol-surface | `null` | panic −1, vrp −1, sector −1, event −1 | **`watch_only`** |
| SPY | short / `dealer_positioning` | **−2** | drop | +1 DEX flip, **−3 flow_conflict** | `null` | cluster −1, event −1 | **`watch_only`** (short routing) |
| QQQ | short / `multileg_directional` | 0 | drop | +2 multileg, +1 DEX flip, **−3 flow_conflict** | `null` | cluster −1, sector −1, event −1 | **`watch_only`** (short routing) |
| EWZ | **unresolved** / `multileg_directional` | 0 | drop | +2 **withheld → 0** | `null` | event −1 | `skip` |
| IREN / PLTR / MRVL / ARM | vol_long / `vol_term_dislocation` | 1 ea | drop | +1 vol-surface | `null` | cluster −1 (exc. PLTR), sector −1, event −1 | `skip` |
| DOCU / CIEN | vol_long / `earnings_vol` | 1 ea | drop | +1 earnings BUY VOL | `null` | sector −1, event −1 | `skip` |
| SNOW / LULU / ZS / PATH / CHWY / ORCL | **vol_short** / `earnings_vol` | 1 ea | drop | +1 earnings SELL VOL | `null` | vrp −1, sector −1, event −1 | **`watch_only`** |
| PANW | vol_long / `vol_term_dislocation` | 0 | drop | +1 **withheld → 0** | `null` | sector −1, event −1 | `skip` |
| GOOGL, MRNA, NVDA, AAPL, TSLA, MSTR, GDX, GLD + 9 no-tenor earnings names | — | 0 | drop | none earned | `null` | — | `skip` |

**`win_rate` is `null` / `NA(substrate)` on all 25 rows — correctly, and this is the honest label rather than a failure.** `uw historical signal-backtest` supports exactly five `--signal-type` values (`bullish_flow`, `bearish_flow`, `high_iv_rank`, `volume_spike`, `dark_pool_accumulation`). **Today's dominant classes are none of them** (`multileg_directional`, `sector_rotation`, `vol_term_dislocation`, `earnings_vol`, `dealer_positioning`), so the quant made **zero backtest calls** rather than quoting an unsupported number. Consequently **`market_excess` is `null` on every row too** — with no signal WR, a benchmark leg alone would be a fabricated "excess". **The Step-5 win-rate ladder and the C2 market-excess gate both could not bind today**; sizing fell to tier default → half-cap → routing → floor.

### Registered findings for the next `/calibration-audit` — routed, not acted on

1. **Cum-flow award/deduction scale asymmetry (the day's most consequential defect).** The **award** side carries two floors ($50M absolute + 5%-of-gross scale-relative); the **deduction** side carries **neither a scale floor nor a freshness floor**. Today that cost **QQQ −3 on a 0.71%-of-gross imbalance** (+$347.5M net on $48.66B gross) and **SPY −3 on 0.087%-of-gross** — while **META was *awarded* on 0.394%-of-gross**, a *smaller* imbalance than the one that penalised QQQ. QQQ went from raw 3 to raw 0 on it. Compounding: **8 of the 10 largest QQQ call prints today carry `side: no_side`**, so the directional attribution building that net is itself substantially unresolved. This is directionally material because it **manufactures short-side score suppression**. It is a rubric change under a freeze and requires pre-registration with cross-regime ∧ n≥30-per-arm ∧ BH-surviving evidence — **not fixable in-flight, and no score was adjusted for it.**
2. **`portfolio-correlation` truncates `high_correlations` to 10 rows**, hiding the entire 0.60–0.70 soft-watch band on a wide call. New; recovered by subset re-runs.
3. **`--near-dte 7` tie-break trap (new, same family as the recorded snap defect but a different mechanism).** With weeklies listed, the flag selects **dte=10 (09-11 CPI) over dte=3 (09-04)** purely on `|10−7| < |3−7|`. For the 8 names reporting by 09-02/09-04, dte=10 is **already past their event**, making the automated pre-event panic read **invalid on 8 of 15 measurable names**. Population firing rate at near-dte 7 was **14/15 (93.3%)** — inflated by this CPI-week confound.
4. **`iv-percentile-zscore` short-delivered fleet-wide** — `dates_used` 99 of 252. Every IV-percentile read today is provisional.
5. **`uw insights analyst-vs-flow` re-confirmed dead** — no analyst leg at all (SNOW and AMBA checked directly; payload carries only `options_flow`).
6. **`yahoo_fundamentals` returned HTTP 401** on all three deep-dive names — that MCP path is down. No impact (Finnhub covered fundamentals), but it is a graceful-skip that should be recorded.
7. **Coverage gap, unchanged:** `vol_term_dislocation` maxes at **1 point**, so a sound long-gamma call cannot clear the DROP floor by construction. **SNDK is today's instance** — the cleanest vol read in the book, the only CONFIRM, the only bull debate win, structurally incapable of scoring above 1.
8. **Vol-lane generation balance worth a glance.** In a tape with **negative NDX VRP** — the condition that most favours long vol — the scouts produced **7 `vol_long` vs 8 `vol_short` candidates**, near parity. `vol_long` is the one vol result that measures positive (+9.5pp, 5-for-5 sized). Not a violation; worth checking the Phase-1 vol screens.
9. **Short-generation drift does *not* apply to this board.** Today is **11 of 25 short-side (44%)** — 3 directional + 8 vol_short — well above the 17.6% drift level that triggered the generation floor. Phase 1 is still producing the counterfactual rows the routing rules depend on.

> **Reconciliation note for the auditor:** debate residuals are quoted in this report as the **raw values the agents returned** (0.25 / 0.28 / 0.35 / 0.65 / 0.70 / 0.75). `decision.json` stores them **discretized to the schema's bin-midpoint enum**, so SNDK's bull residual appears as `0.75` (the `[0.70, 0.80)` bin) and AMBA's as `0.25` (the `[0.20, 0.30)` bin). The bins are the schema contract; the raw values are here for provenance. No other figure differs between the two files.

### Conviction scoring rubric — `rubric_version 2026-06-12` (FROZEN), embedded verbatim

```
Daily conviction score = Σ:
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna-squeeze setup in trade direction
      — must be a verified SIGN CHANGE, not a level: sign(net_dex) on the latest session opposite to ≥3
      consecutive prior sessions, |net_dex| on the flip day ≥ 0.25× the trailing-10-session median.
      Computed by scripts/dex_flip.py, never by hand. Vanna disjunct requires a dated falling-VIX source.
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified
      institutional-tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms
      (sign aligned AND |cum_flow_30d| ≥ $50M); else halved to +1.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: award only when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +1  cumulative-premium-flow net directional accretion (30d) — INTENT-SCREENED: (a) no C28
      distribution_flag, AND (b) on dividend payers in an ex-div window, not deep-ITM sub-parity calls.
  +1  sector-rotation-strategist names ticker single-name leader — CONDITIONAL: (a) persistence ≥ 0.6
      AND (b) cum_flow_30d aligned AND (c) |cum_flow_30d| ≥ $50M. Default 0.
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored play type)
  +1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags overcrowded long with rising pc-ratio-zscore (VRP positive) — an
      INFORMED-FLOW CONTINUATION penalty, not a "fade the crowd" signal.
  -3  flow_conflict — cum_premium_flow 30d clearly opposite dominant_signal_class
  -1  flow_conflict_lite — 30d read MIXED (near zero, or aligned but bottom-quartile)
      (the -3 and -1 are MUTUALLY EXCLUSIVE — apply ONE, never both)
  # TIER GATES applied by risk-monitor in 2d — contribute 0 to raw_score, never in score_components:
  -1  [TIER GATE] correlation cluster (pairwise corr ≥ 0.70) — −1 TIER
  -3  [TIER GATE] market-regime conflicts with trade direction — −1 TIER
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | HIGH | full (subject to the 3-of-4 load-bearing-tool gate + win-rate gate) |
| 7 – 8 | MEDIUM | half (subject to win-rate gate) |
| 3 – 6 | LOW | starter / watch-only |
| ≤ 2 | drop | filtered by the quant's drop floor |

**Tier-cut status:** the ≥9 HIGH cut was set in-sample on UPTREND data and **failed its scheduled re-confirmation on 2026-06-12**. The cuts are retained under the freeze but carry **no validated ranking claim**; the out-of-regime guard caps all sizing at half in the interim. That guard's lift is **unrunnable for a 9th consecutive cycle** — the HIGH/MEDIUM bands are structurally empty, so there is nothing to re-validate against.

---

## 8. Watch-only — single signal, no confluence

Only **three names cleared the ≥2-agent confluence gate**: IWM, QQQ (multileg + dealer-positioning) and BSX (multileg + sector-rotation). Everything below was flagged by a single agent — listed for journaling, **not for trade entry today**.

- **AAPL** — the day's most interesting contradiction, and it was **adjudicated and rejected by two agents independently**. It topped the bullish net-premium board (**+$70.7M**), closed **+2.61%**, *and* carried a Tier-1 `OPENING_PUT_PRIME` (size/OI **13.47**, dte 10). Resolution: accumulation-hunter found its bullish dark-pool headline is **~90% closing-cross artifact** (top bucket $325.13 = the close; ~90% of the mega tape inside the 20:00–21:05Z window) with call OI *closing* (330C/300C/360C, 17DTE); contrarian-scanner found P/C z-score **NORMAL (−0.094)**, so there is no crowding extreme and the −2 line cannot even trigger. Net read: **one idiosyncratic institutional put sitting on top of unremarkable bullish flow** — not a candidate in either direction. Carried as a caution against any AAPL long thesis generated elsewhere.
- **PBR** — accumulation-hunter's closest near-miss: `conviction-matrix` **DIRECTIONAL_LONG at 38.5%**, below the 50% floor, on the one sector with genuine price strength. Worth a same-week re-check if confidence crosses 50% while the mega-tier sample grows beyond n=1.
- **MRVL** — the only internally consistent bearish sweep read (put-skewed, tool-aligned), but sweeps earn 0 points; separately a `vol_long` candidate. The two are different axes, not a contradiction.
- **Single-leg Tier-1 bearish (advisory, permanently 0 points — C19 closed as REFUTED):** `OPENING_PUT_PRIME` AAPL, CRCL (9.13), LITE (4.50); `FLOOR_PUT_BLOCK` MU, META, AMD, TSLA, VST. Regime is neutral so the call side is `CALL_UNVALIDATED` — **not faded by default**, since the "calls are beta" result was measured in a bull window and is bull-regime-conditional.
- **Energy complex** (HP, DK, UGP, EQNR, OKE, MPC via the `fz` new-high lane; USO, PBR, XLE on the tape) — genuine, broad price strength and the day's only green sector on both 1d and 5d, but **no durable options-flow confirmation** (XLE 5d net +$2.21M/MIXED). Watch for the flow to catch up to the tape.
- **Squeeze lane (`fz`, advisory):** ABEO, ABSI, ACHC, ACHV, AESI, AI, ALMU, AMCX, APLD, ARCT — all >20% short float. None earned a scored co-flag. ⚠️ Tickers decoded from the **known `fz` doubled-first-letter bug**, which corrupted **every row** of both bulk screens again today (AABEO→ABEO, MMMED→MMED, HHP→HP). Per-ticker `fz_enrich` is healthy.
- **Also single-signal:** GOOGL (sector-leader fails (b) — cum_flow_30d −$126.4M against a +$8.5M pop), MRNA, NVDA (multileg rejected by its own false-positive control — 1.5:1 size mismatch, ambiguous side tags), TSLA, MSTR, GDX, GLD, IOT, GME, RH, SIG, ADBE, KR, and the nine earnings names with **no tradeable near-event tenor** (NTAP, AGX, OLLI, PVH, GWRE, CPRT, CASY, HUBG, VSXY) whose event premium is **unmeasurable, not absent**.

---

*Generated by `/daily-analysis` · 11 Phase 1 agents (no OPEX agent — third Friday is 2026-09-18) → quant → fundamentals gate → 5-name bull/bear debate → risk-monitor. Rubric frozen at `2026-06-12`. Watchlist write-back: `conviction_2026-09-01 → ["IWM"]`.*
