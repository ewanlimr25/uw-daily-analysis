# Daily Market Analysis — 2026-08-24

## Executive Summary

- **Regime + GEX state:** TRANSITIONAL / PULLBACK_IN_UPTREND. SPY 763.47 (−0.29% 1d, −1.19% 5d), just below its 20SMA (763.55), above its 50SMA (752.26). VIX 15.85 (+4.76%). **Both index books are net dealer SHORT gamma** — SPY `total_gex` −$1.28B for 7 straight sessions, QQQ −$548M for 6. Options-flow breadth 34.6% bullish. Sector lean: Technology netted **−$346.2M**, the largest outflow on the tape by an order of magnitude.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`.
- **Next-session GEX (SPY/QQQ):** SPY — short-gamma, ZGL unreliable (336.67, >55% below spot), put wall 760 (−0.48%) inside a deep negative-GEX trench, call wall 780; **amplification, not a pin**. QQQ — `FULLY_NEGATIVE`, ZGL null, put wall 705 sitting **0.24% below spot**; highest-amplification setup of the two. Advisory, see §2.
- **Top swing build:** **None.** No name cleared the drop floor.
- **Top LEAP candidate:** **None.** Zero candidates cleared 6-of-9 gates.
- **Biggest risk:** A nine-name AI/semis correlation cluster (centroid SMH: 0.939 to INTC, 0.882 to MU, 0.865 to AMD) and a three-name crypto cluster (0.857/0.821/0.772). Twelve of sixteen candidates were the same two bets wearing different tickers. Hedge sleeve: **QQQ Sep-18 put debit vertical below the 705 wall — not SPY.**

> **EMPTY CONVICTION BOOK.** Max `raw_score` = 1 against a HIGH band of ≥9. All 16 confluence-passing names land at DROP. The rubric awarded **11 positive points across all 16 names** and deducted **−17**, net **−6**. Re-derived from `analyses/daily/*/decision.json` only: this is the **34th consecutive empty daily board**; last sized daily board was **2026-07-07** (PEP full + 8 starters).

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** TRANSITIONAL — "Half position sizes. Favor defined-risk strategies. Iron condors in range." Trend PULLBACK_IN_UPTREND. Breadth: 2,183 bullish vs 4,118 bearish tickers of 6,301 (34.6% bullish).

**The tape is a rotation, not a broad decline** — and this framing is load-bearing for everything below. Confirmed on two independent lineages:

| | 1d | 5d | | 1d | 5d |
|---|---|---|---|---|---|
| SPY | −0.29% | −1.19% | XLK | −1.78% | **−5.40%** |
| QQQ | −1.00% | **−3.23%** | SMH | −2.43% | **−7.96%** |
| IWM | −0.66% | −2.00% | SOXL | −7.83% | **−26.64%** |
| **RSP (equal-wt)** | **+0.12%** | **+0.52%** | XLP | +1.70% | +3.27% |
| ^VIX | +4.76% | +4.34% | XLV | +0.05% | +4.58% |

Cap-weighted indices are red while equal-weight is **green**, and the independent `fz` breadth cross-check prints **60.44% advancers (304 / 196 / 3 unchanged of 503)**. The damage is concentrated: SOXL −26.6%, NBIS −21.6%, WDC −18.8%, CRWV −18.6%, SNDK −16.4%, INTC −15.7%, LITE −14.3%, VRT −12.8%, MU −10.0%, AMD −9.7% over five sessions. The bid is in gold (+5.2%), silver (+4.4%), crypto (IBIT +22.6%, MSTR +25.5%, COIN +19.2%), healthcare (+4.6%) and staples (+3.3%). The `fz` RS/new-high screen — a different data lineage entirely — returns leaders in financials (V, SCHW, SEIC), consumer (EXPE, ABNB, TGT, FIVE), healthcare and materials, and **zero semis/AI names**.

**Per-index gamma (current-state EOD book):**

| | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 763.70 | 336.67 *(unreliable)* | **−$1,284,006,949** | NEGATIVE *(label said POSITIVE)* | 780 (+2.14%) | 760 (−0.48%) |
| QQQ | 706.72 | null | **−$548,110,530** | FULLY_NEGATIVE | 720 (+1.87%) | 705 (−0.24%) |
| IWM | 297.97 | — | negative | — | — | — |

⚠️ **The GEX `regime` label contradicted its own `total_gex` sign on SPY** — the field returned `POSITIVE` against −$1.28B. This is the known substrate defect; the sign is trusted and the envelope serializes `NEGATIVE`. IWM shows three `total_gex` sign flips in ten sessions — whipsaw, treat as noise.

**`uw options-flow dte-volume-share`:** 0DTE 36.8% / weeklies 23.8% / monthlies 20.4% / LEAPs 4.4% — `BALANCED`. No retail-0DTE domination and no institutional monthly tilt, so no weighting adjustment either way.

**`uw historical vrp`:** SPY **+0.007 FAIR**; QQQ **−0.0197 NEGATIVE** (IV30 19.88% *below* realised 21.85%). The Nasdaq complex is a premium-**buying** environment.

**Macro backdrop** (`scripts/fred_macro.py`): yield curve normal (+0.46), core CPI 2.79% YoY, core PCE **3.29%** YoY, unemployment 4.1% with payrolls **−23k MoM**, 10Y 4.74% and **rising**, USD **weakening**, fed funds 3.63%. Stagflation-lite tension — and the rising-10Y / weakening-USD combination is the macro engine underneath today's rotation, funding the metals-and-crypto bid while taxing long-duration tech multiples.

**Forward event risk** (T+N in *trading* days from 2026-08-24): **PCE T+2→T+4** (Aug 26–28, sources conflict; earliest edge governs), GDP 2nd est T+3, ISM Mfg T+6, ISM Svcs T+8, **NFP T+9** (Sep 4), **CPI T+13** (Sep 11), **FOMC + SEP T+15/T+16** (Sep 15–16), monthly OPEX T+18 (Sep 18). Four Tier-1 binaries inside a single swing window.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** Prose-only, **0 rubric points**, no backtested predictive claim. Built from open interest that persists overnight and read forward as the prior for tomorrow's open.

**SPY — persistent short gamma, amplification zone at 760.** `total_gex` has been negative **every session since 2026-08-17** (−368M, −1224M, −303M, −1872M, −895M, −1284M) even as the regime *label* flip-flopped POSITIVE/NEGATIVE/FULLY_NEGATIVE almost daily with garbage ZGLs on the "POSITIVE" days. This is a durable book, not a fresh flip. Spot sits inside the single largest negative-GEX cluster on the grid (760–765, −$106M to −$315M per strike) with the put wall only 0.48% below. **Dealers amplify here, they do not pin.** The +GEX call wall at 780 is thin by comparison and unlikely to cap a real trend day.
→ *Structure bias:* debit verticals / directional 0DTE. **Do not** put on an iron fly or condor around 763–765 — the grid there is deeply negative, the opposite of a pin.

**QQQ — short gamma with the put wall on top of spot.** Negative for six straight sessions, and today the label and sign agree (`FULLY_NEGATIVE`, ZGL genuinely null). The put wall at 705 sits **0.24% below spot** — essentially at it — so dealers are positioned to sell aggressively on any further downtick with almost no cushion. Highest-amplification setup of the two.
→ *Structure bias:* directional debit verticals, or a long straddle on a flip through 705. Negative VRP independently argues against being short QQQ vol — both signals point the same way.

**Mandatory caveats.** EOD is a **prior, not a target** — fresh 0DTE OI floods in during the first 30–60 minutes and re-computes the ZGL and walls, which matters most on QQQ where the wall is 0.24% from spot. **ZGL is unreliable on both** (SPY's 336.67 is >55% below spot; QQQ's is null), so both reads rest on the `total_gex` sign plus wall geometry. **Gap risk voids the prior** — the PCE window opens Aug 26 and CRM/HPQ/CRWD report the same day. **Tooling limit:** `uw` cannot isolate the D+1 expiry, so this is the standing 0–45 DTE book. **ETF book**, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup — **STAND ASIDE ON SPY**

`scripts/zerodte_setup.py` returns `GO_PREMIUM_SELL_INTRADAY` for both indices with `sell_premium: true`. **That flag is unconditional and it does not survive two independent checks today.**

| | SPY | QQQ |
|---|---|---|
| `vol_state` / VIX | LOW / 15.85 (terciles 15.9 / 17.3) | LOW / 15.85 |
| implied move / expected range | 0.61% / 1.15% | 1.03% / 1.94% |
| `mean_pnl_open_pct` (**gross**) | +0.205% | +0.335% |
| `mean_pnl_open_net_pct` | +0.105% | +0.235% |
| **`mean_pnl_by_vix_state[LOW]` − 0.1% cost** | **+0.013%** | **+0.107%** |
| worst observed open-entry day | −1.4% | −2.453% |

`pnl_basis` is **percent-of-underlying-spot-notional, gross** — not premium-collected, not margin-relative.

1. **VIX 15.85 sits in the LOW tercile**, where SPY's net expectancy is **+0.013%** — effectively zero. QQQ's +0.107% is thin but real.
2. **Both dealer books are short gamma** — the opposite of the long-gamma pin regime premium-selling wants.

On QQQ there is a third strike: VRP is **negative**, so selling premium on a name whose implied already sits below its realised is the wrong side of the sign. **SPY: stand aside. QQQ: reduce or stand aside.** Entry rule if traded at all — enter at/after the open once the gap resolves, hold to the close, never carry overnight (QQQ overnight backtests at −0.10%). The short-vol left tail is **unsampled**; the validation window contains no vol shock. **SPY ≈ SPX** (validated identical); **QQQ is the weaker read** — the Nasdaq index book is unavailable, so this is the ETF proxy. Advisory, **0 rubric points**, and this lane stays advisory permanently until a vol-shock day enters the sample *and* net expectancy clears a tail-aware bar.

## 2a. Swing Dealer Positioning (1–4 weeks)

**26 names tested through `scripts/dex_flip.py`. One qualifier — and it failed the confluence gate.**

**WMT** is the only name market-wide clearing the mechanized +1 line: `net_dex` −$1,706,978,987 (08-21) → **+$99,581,502** (08-24), prior three sessions all negative, |flip| against a floor of $58,825,439 (0.25× the trailing-10 median of $235,301,755) = **ratio 1.69**. Corroborated from two other lineages — a same-day `total_gex` sign flip NEG→POS (not a single-strike artifact; the top strike is 26% of gross) and the Step 0 watchlist alert (2.5× volume, P/C **0.21**, a $117.1M single DP print, +102,333 net OI). But the script also returns **`whipsaw_warning: true` — 5 sign changes in 13 sessions** — and the flip-day magnitude is small against prior negative swings up to −$2.05B. **`accumulation-hunter` then rejected the name outright** (`institutional-accumulation` = NEUTRAL, failing its primary gate), leaving WMT with a single positive agent flag. See §8.

**The vanna disjunct is dead market-wide.** The dated ^VIX series shows no three-consecutive-session down-run ending near today (08-20 16.01 → 08-21 15.13 → 08-24 15.85, closing +4.76%), so `vanna_squeeze_flag = false` on all 26 names. Put-heavy books get "vanna pressure," not squeeze.

Near-misses, watched not scored: **QQQ** broke a genuine 12-session positive DEX run today but at **ratio 0.62** of the floor; TSM 0.80; SNDK 0.54.

**The most consequential unscored finding: the semis options book has not confirmed the spot carnage.** NVDA, MU, AMD, MRVL, MCHP and DELL all still print **net-positive DEX** after 5-day drops of 7–10%. That is a level, not a sign change, so it earns nothing — but it means the derivatives market has not ratified the liquidation happening in the underlying.

## 2b. Sector Rotation

**Rotation regime call: `no_change`. Zero sectors clear the full gate stack.**

Direction is read **only** off the netted `uw risk market-regime.sector_rotation` block (C55). `sector-flow` and `sector-flow-persistence` are one gross-turnover source and cannot express direction — and today the persistence limb **fired ≥0.6 on 11 of 11 sectors** (six at exactly 1.0), reproducing the zero-discrimination pattern recorded on 2026-08-14. It did no work.

| Netted OUT | | Netted IN | |
|---|---|---|---|
| **Technology** | **−$346,246,398** | Communication Services | +$17,452,199 |
| Industrials | −$25,018,410 | Consumer Defensive | +$11,424,977 |
| Consumer Cyclical | −$21,157,164 | Financial Services | +$10,431,987 |

**Technology OUT is the cleanest read of the day** and a textbook C55 case: the *gross* source printed **positive** (+$524M) while netted is −$346.2M, and price confirms the netted read hard (XLK −5.40% 5d). Three names cleared all three sector-leader conditions on the short side — **MCHP** (30d −$158.8M), **INTC** (−$398.0M), **ORCL** (−$85.0M). **NVDA and MU failed condition (b)**: despite printing today's largest bearish flows (−$115.9M, −$96.9M), their 30d cum-flow is net *positive* (+$128.0M, +$126.6M).

Financial Services was the only long-side sector to clear netted + persistence + magnitude + gross agreement — but **XLF's own ETF options tape shows a −$14.7M 5d outflow**, so the instrument layer contradicts the GICS layer and the call drops to watch-only. MA (+$14.8M) and DB (+$3.4M) both fail the ≥$50M condition.

**Two methodological holes recorded rather than papered over.** First, **Healthcare** clears persistence, magnitude and price (XLV +4.58% 5d, the best SPDR on the board) but has **no netted direction at all** because it falls outside the top-3/bottom-3 truncation — the netted block may be dropping the largest true rotation of the day. Second, the sector-leader conditions (b)/(c) test the **identical field and threshold** as the standalone cum-flow rubric line; the quant suppressed the duplicate on INTC and MCHP and awarded one bit once.

**ETF flow tape (advisory).** Magnitudes here are one to two orders smaller than the GICS aggregates — a tie-breaker, never the primary read.

| ETF | Net premium dir | 5d net flow | DP positioning | Options urgency | GICS agreement | Leaders |
|---|---|---|---|---|---|---|
| XLK | inflow (weak) | +$5.0M | mixed, no tilt | thin, mixed | **disagree** (netted OUT) | SNDK, AMD, WDC *(context only)* |
| IGV | inflow | +$3.8M | large blocks **below mid** — distribution-flavoured | thin bullish, low notional | **disagree** | — |
| XLY | inflow (weak) | +$2.5M | one near-mid block | **zero sweeps** | **disagree** (netted OUT) | AMZN *(context)* |
| XLF | **outflow** | **−$14.7M** | consistently below-mid prints | thin, single-block, mixed | **disagree** (netted IN, price IN) | — |
| EWY | outflow | −$19.4M | very large blocks ($60M+), no sign | modest bullish calls | n/a (geographic) | — |
| GDX | **outflow** | −$32.3M | mixed sign | real bullish call buying Sep/Dec/Jan27 — conflicts with the outflow | n/a | — |

---

## 3. Swing Setups (1–6 weeks)

**Empty. No name cleared the drop floor.** Sixteen names passed the ≥2-agent confluence gate; the highest score among them was **1**, against a LOW band that starts at 3 and a HIGH band at 9.

### 3a. Long swings (regime-aligned) — none sized

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **GLD** | **1** | Institutional gold long into the PCE→FOMC corridor. A **decontaminated $847.3M above-ask block** at 13:53:54Z (9:53am ET) — nowhere near the closing window, executed +$1.26 vs mid, mega-tier trades clustered at 429 *above* the 426.7 close. Direction-verified 5d OI build (39,817 call adds vs 5,513 put). Plus the day's only rubric-eligible multileg structure. | Sep-18 420C/430C bull vertical, 115,876/leg, $57.94M debit | **Loses the $427.73 second-tier DP shelf** (C34 — the top bucket is the closing-cross artifact) | **skip** |
| AMD | −3 | Best-evidenced semis-exhaustion candidate: price −16.7% (30d) against **+$21.4M bullish net flow**, and a Jan-27 $300P shedding **4,324 OI on 4,673 volume** — a large downside hedge actively closing. | Bull call debit spread ~25–30 DTE (**not** premium-selling — negative VRP) | Flow flips bearish; OR new 30d low with *fresh* put OI adds | **skip** |
| IBIT | −1 | Crypto-proxy long lean, +22.6% 5d. Zero positive lines fired. | — | — | **skip** |

⚠ **GLD distribution caution:** $21.8M of institutional-size **call OI closing** across ~15 strikes even as the dark pool shows fresh buying — advisory, 0 points, does not change sizing, but unresolved.

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only` (2026-08-01 P0 #1).** Routing, not suppression — every thesis below was generated, scored, gate-verdicted and serialized so the counterfactual keeps resolving.

| Ticker | Score | Thesis | Invalidation | Sizing |
|---|---|---|---|---|
| SLV | 1 | Only clean aligned 30d bearish accretion on the board (−$186.4M, non-MIXED BEARISH label, 5d agreeing) | Silver reclaims the high with the macro tailwind intact | **watch_only** |
| INTC | 1 | Cleanest sector leader: −$398.0M 30d inside the −$346.2M netted tech outflow, price −15.7% 5d | C4 gate turns put-dominant (currently **call**-dominant: +174,140 net OI, adds at C80/C100/C130) | **watch_only** |
| **MCHP** | 1 | Largest bearish net flow in the market (−$152.8M) | n/a — **VETO'd** | **veto** |
| MSTR | 0 | 4/5 aligned bearish persistence against an underlying **up 25.5%** — hedge/fade signature; Dec-28 100C/110C shed 31,466 and 29,124 OI | Flow flips bullish; call OI re-adds at higher strikes | **watch_only** |
| AVGO | 0 | Genuine 361–362 shelf fade into the close + DISTRIBUTION verdict | Reclaims $361 for 2 sessions | **watch_only** |
| NBIS | −2 | Best-corroborated bearish continuation (5/5 aligned), −21.6% 5d | — | **watch_only** |
| COIN | −1 | Persistence flip + contrarian long-fade | — | **watch_only** |
| SMH | −1 | Bearish flow (pcr 1.51, 7-DTE 400P) inside the tech outflow | — | **watch_only** |
| MU | −3 | Largest bearish net flow ex-index (−$96.9M) | — | **watch_only** |

**Sweep ledger** (informational, **0 rubric points** — the persistence line was removed 2026-05-23 P0.3). **5 bullish / 9 bearish**, matching the 34.6% bullish flow breadth. Cleanest aligned bearish continuations: **NBIS** (5/5, −$8.7M), **INTC** (5/5, −$13.2M), **MSTR** (4/5, −$21.5M). Six contradiction flags worth carrying: **SNDK, AMD, MRNA** all hold 4–5/5 *bearish* persistence books that flipped **bullish** today into the carnage (dip-buying or short-covering, not fresh conviction); **COIN and SLV** did the reverse after big up-weeks; **MCHP**'s thin 1/5 "bullish" tag is contradicted by the largest bearish net flow in the market. The persistence top-10 is **7/10 index/mega-cap hedge flow** with unverified alignment and carries no scoring value.

---

## 4. LEAP Builds (6–24 months)

**Empty. Zero candidates cleared 6-of-9 gates.** `uw oi biggest-increases --min-dte 180` returned only 20 rows for the entire session; five unique tickers survived the C12 floor, and **all five failed the required cum-flow accretion gate** — every one returns `MIXED` at both 90d and 30d with net flow inside ±3.6% of gross, which is noise at that notional.

| Ticker | Gates | Disqualification |
|---|---|---|
| TSLA | 2-of-9 | Required cum-flow gate fails (MIXED both windows, and the **30d is more negative than the 90d** — flow trending bearish into a bullish 990C build). DP evidence is **closing-cross contaminated**: the $149.5M ticket fired at 20:00:18Z at the exact close and is **51.7%** of its top price-level cluster. conviction-matrix MIXED at 8.8%. |
| IBIT | 2-of-9 | Required gate fails. The $38.8M block is **64.6%** of its top cluster — past the >20% single-ticket invalidation. Its LEAP strike (80c DTE207) is **94.5% bid-side**. Genuine `ACCUMULATION` on the 10d signal and confidence only 13.4% against a 70 bar. **The one name worth a re-check.** |
| INTC | 1-of-9 | +460% OI jump on the 2028 $80C looked like a textbook dip-LEAP — but **67.7% bid-side**. conviction-matrix 2.6%. |
| ORCL | 1-of-9 | +244% OI jump with **`prev_ask_volume: 0`** against a 6,496-contract move — the build happened entirely off the visible tape, so **no direction can be attributed at all**. |
| XLF | ~0-of-9 | Put-side build with a 90d→30d **sign divergence** (+$5.7M MIXED → −$19.7M BEARISH). The 47P is 88.8% bid-side (put *selling* — a bullish stance), the 48P 55% ask-side. Unresolvable put-sale-netting ambiguity. |

The framing answer is **(c)**: long-dated money is doing nothing directional. The rotation visible in the 5-day tape has not propagated into the DTE>180 book — consistent with LEAP share at just 4.4% of today's volume.

---

## 5. Volatility Surface

**The headline dislocation is the dispersion — and the honest version is less tradeable than it first looks.**

| | IV30 | Realised 30d | VRP | Regime |
|---|---|---|---|---|
| SPY | 13.04% | 12.35% | **+0.007** | FAIR |
| QQQ | 19.88% | 21.85% | −0.0197 | premium-BUYING |
| XLK | 25.76% | 30.39% | −0.0463 | premium-BUYING |
| SMH | 36.73% | 43.71% | −0.0698 | premium-BUYING |
| SOXL | 121.89% | 154.74% | **−0.3285** | premium-BUYING (extreme) |

VRP widens **monotonically** as you move down the rotation. But **index vol is fair, not rich** — so there is no confirmed short leg to fund a dispersion trade. The clean expression is outright long premium in the semis names, *not* a paired short-index spread.

**Substrate hygiene mattered enormously.** Of 29 names, **20 flipped `shape` (69%)** and **10 flipped `base_shape` (34%)** after dropping the 0DTE bucket and sub-15-contract tenors. Nine carry a **CONTANGO base with a genuine event kink riding on top** (SPY, SMH, SOXL, MU, AMD, INTC, GLD, DELL) — a pattern a bare BACKWARDATION label would have collapsed and mis-traded.

**Ranked candidates.** BUY VOL: **NBIS** (VRP −0.8817, the largest cheap-vol gap in the scan, on a **28.6%-prominence kink at the Sep-18 monthly OPEX** — a real structural node), SNDK (−0.6746), CRWV (−0.5353), LITE (−0.3451), MU (−0.3256), WDC (−0.3058), **MRVL** (−0.1479, earnings T+3, realised running 93.4% against a priced 8.97%), INTC (−0.1593, iv percentile 2.15 — an extreme floor), **DELL** (−0.0625, kink correctly tagging the post-earnings 9/4 tenor). SELL VOL: **NTAP** (+0.1948 — the one name where `iv_rank = 100` is *not* spurious, with an independently elevated z of 2.101), **SNPS** (+0.1499), SLV (+0.0804), IBIT (+0.0734), AVGO (+0.0683), MSTR (+0.0576).

**Measurement defects recorded:**
- **`front-end-iv-ratio > 1.05` fired 17/26 (65.4%)** at `--near-dte 7`. Elevated for a real reason (dense earnings + the PCE window inside every near tenor), so VRP sign did the discriminating instead.
- **HYG disqualified as an artifact** — a front-end ratio of **7.127** off a 4-DTE tenor quoting 36.9% IV against its own `iv30d` of 3.6%, a >10× internal contradiction with no catalyst.
- **NTAP and MANE are `NO_NEAR_TENOR`** — the front end is *unmeasurable*, not calm. NTAP's real 9-DTE event (earnings 09-02, 11.32% implied move) is invisible to `iv-term-structure` but visible to `earnings-catalyst` — a genuine coverage gap between two tools.
- **Every `iv_percentile_z` returned `dates_used: 93`**, below the 120-day first-class floor. All percentile readings are **provisional**.
- The cached `iv_rank_high.json` is **saturated — 25 of 25 rows print 100**, and only NTAP and MANE clear C12. Treat as a screening artifact, not 25 signals.

**Earnings slate** (36 of 40 pass C12; QFIN/EH/CAN/AI fail). **6 BUY VOL** — SNOW, ZS, IOT, CIEN, DOCU, DELL, all with genuine at-event kinks on CONTANGO bases at the Sep-04 tenor. **3 SELL VOL half-size** — WDAY, BBY, GAP (plain front-loaded backwardation with TAIL_HEDGING back-month skew). **13 CALENDAR** — MRVL, CRM, HPQ, CRWD, OKTA, SNPS, KSS, BBWI, ULTA, DLTR, DG, INTU, ZM. **14 SKIP.**

⚠️ **Two tooling findings from the earnings lane that should outlive this report:**
1. **`--near-dte 7` silently breaks for anything reporting more than 4 days out.** It snaps to the nearest listed tenor — here always the 4-DTE Aug 28 bucket. Valid for the 22 names reporting Aug 25–28 (fires 17/22 = 77.3%); **invalid for the 14 reporting Sep 1–3, because that tenor expires before their earnings date.** MDB, AEO, MDT and CPB additionally showed an **inverted** pattern where the invalid pre-event tenor printed *higher* IV than the true event-covering tenor — which killed those four theses. Recommendation: `scripts/term_structure_hygiene.py` should flag `near_dte_actual < days_to_earnings` as INVALID rather than returning a ratio.
2. **The kink-finder mislocates the event** when a larger unrelated far-dated hump sits on thin contracts. CRM, CRWD, SNPS, ZM, MDB, PANW and PATH all reported a `kink_expiry` weeks past the true earnings tenor; the genuine near-event candidate was present in `kink_candidates[]` but marked `qualifies: false`. ZM's 66.9%-prominence kink is noise.

**`analyst-vs-flow` returned 0/36 populated analyst legs** — the defect is total. No divergence claim was made anywhere in this report.

---

## 6. Risk & Correlation

**Macro headline:** stagflation-lite — core PCE 3.29% and core CPI 2.79% above target against a **negative payrolls print (−23k)** and a rising 10Y (4.74%), with the USD weakening and the curve normal at +0.46. Four Tier-1 binaries sit inside a single swing window: **PCE T+2→T+4, NFP T+9, CPI T+13, FOMC T+15/T+16**, with monthly OPEX at T+18.

**Breadth cross-check (advisory):** 304 advancers / 196 decliners, **60.44% green**. This is *not* the index-green/breadth-red distribution tell — it is the opposite shape, and it is the signature of a rotation. Advisory, does not change sizing.

**Correlation clusters** (measured against today's 16 candidates, not the static watchlist; pairwise ≥0.70):

| Cluster | Members | Kept | Tightest edges |
|---|---|---|---|
| **AI/semis** | SMH, INTC, MU, SNDK, AMD, MRVL, AVGO, NBIS, DELL | **INTC** | SMH/INTC **0.939**, MU/SNDK 0.910, INTC/MU 0.882, SMH/AMD 0.865 |
| **Crypto beta** | MSTR, IBIT, COIN | **MSTR** | IBIT/MSTR 0.857, COIN/MSTR 0.821, IBIT/COIN 0.772 |
| **Precious metals** | GLD, SLV | **SLV** | GLD/SLV 0.891 |

Two findings the assumed membership got wrong: **MCHP clears 0.70 with nothing on the board** (best edge SMH 0.697 — soft-watch, no penalty), and **DELL — which was not assumed to be in the cluster — does join** at a single 0.708 edge to SMH. **SNPS returns no pair above the tool's reporting floor** against any of the other fifteen: the only genuinely uncorrelated name on the board. **SMH is the correlation centroid** — sizing SMH alongside any single semis name is sizing the same bet twice.

*The `portfolio-correlation.sector_breakdown` returned `{"Unknown": 16}` with a spurious 100%-concentration warning. That is the standing tool artifact and is not reported as a finding.*

**Fundamentals verdicts (top-5):**

- **MCHP — VETO.** The sharpest catch of the run. A sector-rotation short carrying today's largest bearish net flow, sitting on a clean **4-of-4 beat streak**, **+20.93% YoY revenue growth**, 60.2% gross margin — and a **same-day BMO initiation at Outperform, $95 PT against $74.21 spot (~28% implied upside)**. Two of three fundamental legs oppose the flow. Only insider selling (MSPR −57.85) supports the bear case. **Independently corroborated by the quant's own flow-side anomaly** — `put_call_ratio` 0.0155 (call-dominant volume) inside a nominally bearish funnel row, plus a call-dominant OI build. Two unrelated methods agreeing the short is fooled.
- **INTC — CAUTION.** Same pattern, weaker: 4/4 beats and +7.47% revenue growth fight the short; net margin −19.79% is the one leg supporting it. Its OI build is **call-dominant** (+174,140 net; adds at C80 Dec-28 +7,407, C100 Aug-28 +6,981, C130 Oct-16 +6,584).
- **SLV — CAUTION.** The catalyst stack directly contradicts the short: four same-day bullish silver/gold headlines, zero bearish, and the same weak-USD macro that supports the gold long.
- **GLD — NA** (bullion trust; NA never penalizes). Macro-substitute check is net tailwind. `fz` flags **RSI 72.49, overbought**.
- **DELL — CONFIRM.** Surprise dispersion (3/4 beats, one −1.2% miss) actively supports long vol against a 5.35% implied move. **Date correction: earnings is 2026-09-03 (T+8), not the 2026-09-01 in the UW catalyst cache** — Finnhub is authoritative and the gate, the T+N arithmetic and the envelope all use 09-03.

**Gate stack, 144/144 verdicts recorded, zero silent skips:** regime **1/16** (AMD only — a long into the pullback leg in the epicentre of the damage), vrp **0/16**, panic **9/16**, cluster **11/16**, sector **2/16** (AMD and COIN — the gate discriminated properly rather than stamping every tech name, because seven tech shorts are *aligned* with the outflow), fundamentals **3/5 evaluated**, event_risk **12/16**, debate **0/16 (not run)**, rubric_regime **16/16 armed, 0 binding**.

Two firing rates were flagged honestly by the risk officer rather than left to look clean. **`panic` at 9/16 is tenor-sensitive** — 8 of the 9 firings sat on a tenor the CLI snapped to 4 DTE rather than the requested 7; at an 11-DTE cross-check MCHP, SNDK, NBIS and COIN all flip off, and only DELL, MSTR, MRVL, SNPS and IBIT persist. **`event_risk` at 12/16 (75%)** is uncomfortably close to the zero-discrimination pattern the P1.2 re-scope was written to stop — but its four exemptions did real work (GLD on defined risk; DELL/MRVL/SNPS as event plays), and the firing is driven by a named, dated Tier-1 print two sessions out, not ambient atmosphere.

**Adverse-flow exits: none.** The carried `conviction_2026-08-21` group holds **IWM** (short, watch_only). Every alert today is thesis-*confirming*, not adverse: flow direction bearish, P/C 1.486 with put volume exceeding call volume, net flow −$965,119, IWM −0.66% 1d / −2.00% 5d, IV rank 8.83 (the ladder is still cheap to hold).

**Hedge sleeve** — advice for *carried* exposure; the conviction book is empty so today's fleet creates no new delta.

1. **Hedge the concentration, not the index. Do not buy SPY protection** — SPY VRP is FAIR so there is no vol edge in the premium, and the tape is a rotation: an SPY hedge pays for a broad decline that is not happening.
2. **Primary: QQQ Sep-18 put debit vertical**, long just below the 705 put wall (~700), short ~670. Negative VRP means you buy premium cheap against realised; Sep-18 covers PCE, NFP, CPI and the FOMC and is itself monthly OPEX; and a debit vertical is defined risk, so the hedge is exempt from the event-risk gate by construction.
3. **If the book is semis-concentrated, use SMH puts instead** — VRP −0.0698 is cheaper than QQQ's, and SMH is the measured correlation centroid of the damage.
4. **Size to 25–40% of net long tech/semis delta**, not the whole book. The rotation has a destination; hedging the full book would short its winners by accident.
5. **VIX calls optional, ≤25% of the hedge budget**, dated to the Sep-16 FOMC. Index term structure is in CONTANGO on all three (SPY 0.856, QQQ 0.904, IWM 0.848) — there is no panic bid to ride.

**Do not** sell index premium to finance the hedge. Short gamma on both indices plus negative QQQ VRP is exactly the regime where a premium-selling financing leg blows up.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Empty. No name reached MEDIUM (7) or HIGH (9).** The board's maximum was 1.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no per-tier expectancy is printable this session. No name reached a conviction tier, and the last daily board with a sized call was 2026-07-07 — so there is no current-cycle tier×expectancy table to display, and the C3 fractional-Kelly sizer remains advisory pending a monotone tier×expectancy relationship on n≥30.

### Why the board is empty — the null result is the finding

**Four of eleven rubric lines were structurally dead before scoring began:**

| Line | Fired | Why |
|---|---|---|
| +1 DEX flip / vanna-squeeze | **0/16** | Sole market-wide qualifier (WMT) failed the confluence gate; `vanna_squeeze_flag` false on all 26 names (VIX rising, no 3-session down-run). The semis complex shows net-positive DEX **levels** with no sign change — beta, not a flip. |
| +1 conviction-matrix DIRECTIONAL_LONG >70 | **0/16** | Conditional on `dominant_signal_class == leap_directional`; zero LEAP candidates cleared 6-of-9. |
| +1 opex-pin top-5 | **0/16** | Agent not spawned — 2026-08-21 monthly OPEX has passed; next is 2026-09-18. |
| −2 contrarian overcrowded long | **0/16** | No bid-side leader printed BULLISH_EXTREME (IBIT −0.265, MSTR +0.322, COIN +0.299, GLD −1.305, MRNA +0.664, ASST −0.897 — all NORMAL). WPM's **9.759** is BEARISH_EXTREME — a protective put/collar bid after a +47.65% parabola, the wrong direction for this penalty, and correctly disqualified. `pc-ratio-zscore` has **no `--date` flag**, so "rising" is structurally unestablishable. |

A fifth line was killed by **direction-verification**: `+1 multi-day OI build` fired **1 of 16**. The bare `BUILDING` label fired **12/12** in accumulation-hunter and **5/5** in leap-radar — 100%, zero discrimination, reconfirmed twice today. Requiring a direction-verified build left only GLD. Both shorts measured directly (INTC, MCHP) turned out to be building **calls against their own theses**.

**Positive-line yield: 11 points from 7 awards.** +3 accumulation conjunction → GLD and AVGO, **both halved**. +1 direction-verified OI build → GLD. +2 multileg directional → GLD. +1 cum-flow accretion → SLV. +1 sector leader → INTC, MCHP. +1 earnings BUY/SELL VOL → DELL. +1 vol-surface kinked/backwardation → NBIS, MSTR.
**Deductions: −17 across 9 of 16 names** — four −3s (GLD, AMD, MU, NBIS) and five −1 lites (IBIT, MSTR, COIN, AVGO, SMH). Mutual exclusivity held; no ticker carries both.

### ⚠️ All four −3 flow_conflict deductions fired on a stale window — 4 of 4

| | 30d (what −3 reads) | 5d | 90d | Without −3 |
|---|---|---|---|---|
| **GLD** | −$311.4M | **+$10.1M** | −$331.4M | raw **4 = LOW** |
| **MU** | **+$126.6M** | **−$494.2M** | −$52.8M | raw 0 |
| **NBIS** | +$235.6M | −$20.9M | +$312.6M | raw +1 |
| **AMD** | −$143.3M | +$2.1M (today +$21.4M) | +$115.4M | raw 0 |

In every case the 5-day flow **disagrees in sign** with the 30-day scalar, and in **three of four the 5d is aligned with the thesis the −3 is punishing**. **12 of the 17 deducted points come from a mechanism with a documented window-staleness defect.** GLD is the sharpest case — an $847.3M above-ask block and a $57.94M bull vertical both printed *today*, scored against a 30-day scalar whose net is only −3.72% of a $4.3B gross. **MU is the most extreme**: a **$620.8M sign-flipped disagreement**, with the 90d *also* negative, so the stale-bullish 30d sits sandwiched between two bearish windows. The quant applied all four as the frozen rubric requires and flagged the pattern rather than overriding it — the correct behaviour under freeze, and the single most consequential rubric-mechanics finding of the session.

### Two further structural gaps recorded for the next audit

1. **The rubric has no line for an earnings-scout CALENDAR verdict.** MRVL and SNPS both scored **0 with empty `score_components`** — the line enumerates only "BUY VOL or SELL VOL," while C13 simultaneously routes the earnings-tenor kink away from vol-surface. MRVL carries 112,493 contracts of volume and an 8.97% implied move; SNPS a +71.7pt IV-RV gap, IVR 73.8 and a 4:1 bearish flow tilt. Neither scored a point. No third verdict was invented — that would be a rubric edit under freeze. Counterfactual: reading CALENDAR as SELL VOL gives each raw 1, still DROP, so no tier changed today. It will on a fatter board.
2. **There is no positive contrarian award in the frozen rubric.** The only contrarian line is the −2 penalty, so AMD — the best-evidenced mean-reversion setup on the board — could not score above zero by construction.

**Both directional lanes are negative-excess.** `bullish_flow` 0.4615 vs SPY-long 0.4923 (n=130); `bearish_flow` 0.5333 vs SPY-down 0.5704 (n=135), measured on complete, liquidity-floored windows against a dedicated same-window SPY series. Neither long nor short single-name selection beat simply taking the index side of the same bet. Headline `win_rate` values (0.447 / 0.542) are **never quoted** — the tool silently includes `truncated_signals` (13 and 11 rows). `dark_pool_accumulation` returns **0 rows market-wide**, reconfirming that lane is unmeasurable even though nominally supported.

### Conviction-scoring rubric (Step 4, verbatim — version `2026-06-12`, FROZEN)

```
Daily conviction score = Σ:
  +1  MECHANIZED DEX flip or vanna-squeeze in trade direction — verified SIGN CHANGE, not a level:
      sign(net_dex) on the latest session opposite to ≥3 consecutive prior sessions, |net_dex| on the
      flip day ≥ 0.25× the trailing-10-session median |net_dex|. Computed by scripts/dex_flip.py, never
      by hand. Vanna disjunct additionally requires a dated falling-VIX leg.
  +3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified
      institutional tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms
      (sign aligned AND |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: award only when
      dominant_signal_class == leap_directional; 0 in all non-LEAP contexts.
  +1  uw historical cumulative-premium-flow net directional accretion (30d) — INTENT-SCREENED:
      (a) no C28 distribution_flag on the name, AND (b) on dividend payers in an ex-div window the
      accreting prints are not deep-ITM sub-parity calls. Screen failed or unevaluated ⇒ 0.
  +1  sector-rotation-strategist names ticker as single-name leader — CONDITIONAL, all three of:
      (a) sector persistence_score ≥ 0.6, (b) cum_flow_30d direction aligned, (c) |cum_flow_30d| ≥ $50M.
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising uw historical pc-ratio-zscore (VRP positive)
      — an INFORMED-FLOW CONTINUATION penalty, not a "fade the crowd" signal.
  -3  flow_conflict — applied mechanically when cum_premium_flow 30d direction is clearly OPPOSITE
      dominant_signal_class (signed-sum sign flip + magnitude > today's union-median |cum_flow_30d|,
      or explicit OPPOSITE label)
  -1  flow_conflict_lite — when the 30d read is MIXED (signed sum near zero, or aligned but
      bottom-quartile magnitude in today's union). Mutually exclusive with flow_conflict.
  # TIER GATES (0 points, applied by risk-monitor in 2d, listed for documentation only):
  -1  [TIER GATE] correlation cluster (pairwise corr ≥ 0.70) — −1 TIER, not −1 point
  -3  [TIER GATE] uw risk market-regime conflicts with trade direction — −1 TIER, not −3 points
```

| Score | Tier | Sizing default |
|---|---|---|
| ≥ 9 | HIGH | full (subject to the Step 3a load-bearing gate + win-rate gate) |
| 7 – 8 | MEDIUM | half |
| 3 – 6 | LOW | starter / watch-only |
| ≤ 2 | DROP | filtered by the quant's drop floor |

*Tier-cut status: the ≥9 HIGH cut failed its scheduled re-confirmation on 2026-06-12 and is retained under freeze with no validated ranking claim. The P0.6 out-of-regime guard caps all sizing at half in the interim.*

---

## 8. Watch-only — single signal, no confluence

Listed for journaling, **not for trade entry today**.

- **WMT** — **the only mechanized DEX-flip qualifier market-wide** (ratio 1.69, corroborated by a same-day GEX sign flip and a $117.1M DP print with P/C 0.21). Failed the gate because `accumulation-hunter` examined it and **rejected it**: `institutional-accumulation` returns **NEUTRAL**, failing its primary gate. `dex_flip.py` also returns `whipsaw_warning: true` — 5 sign changes in 13 sessions. **This is why the +1 DEX line awarded zero to every scored name.**
- **HYG** — **the strongest single distribution signal on the tape**, and it failed on one agent. DISTRIBUTION verdict, mega-tier buy_ratio **0.094**, and the cleanest direction-verified OI build of the whole scan: a genuine multi-expiry **put ladder** (8 of the top-10 building contracts are puts), corroborated by a $68.6M DP print and +224,038 net OI. `vol-surface-scout` disqualified it as a data artifact (front-end ratio 7.127 against an `iv30d` of 3.6%). **Unresolved put-sale-netting risk:** `oi smart-positioning` reads the flagship 75P as **bid-side (sold)**, which would invert it into a bullish income trade.
- **ORCL** — sector-rotation short leader clearing all three gates (−$85.0M 30d), but the only agent to flag it. Its 2028 240C build has `prev_ask_volume: 0` against a 6,496-contract move — entirely off-tape, no attributable direction.
- **NVDA** — largest mega-cap bearish net flow (−$115.9M) with a $77.4M Jan-27 $180P ticket, but no agent surfaced it as first-class: demoted to the sweep hedge-flow footnote, its multileg is a hedge with one leg *inferred*, and vol-surface gives it zero confirming legs. Its 30d cum-flow is net **positive** (+$128.0M).
- **NTAP** — the only SELL VOL name where `iv_rank = 100` is genuinely elevated (z = 2.101, VRP +0.1948, earnings 09-02). Single agent.
- **WPM** — 9.759σ P/C extreme, correctly **disqualified**: a protective put/collar bid after a +47.65% 30d parabola, not fade fuel.
- **MA / DB** — Financial Services long-side leaders; both fail the ≥$50M cum-flow condition (+$14.8M, +$3.4M).
- **SNDK** — the **largest 30d flow in the union by 4× ($1.30B)**, left entirely unscored because no direction is inferable (5/5 bearish persistence flipped bullish today; 5d −$98.1M opposite the 30d). An unresolvable direction on the biggest flow on the board is a reason not to trade it, not a reason to guess.
- Vol-surface single-signal names: SOXL, XLK, WDC, VRT, CRWV, LITE. Earnings-only names: SNOW, ZS, IOT, CIEN, DOCU, HPQ, CRWD, OKTA, KSS, BBWI, ULTA, DLTR, DG, INTU, ZM, WDAY, BBY, GAP, CRM.

**Sub-C12 names dropped from the funnel entirely** (price < $5 or 20d dollar ADV < $50M): DNN, DQ, TXO, BLCO, MGEE, CCS, OMCL, BUG, CMP, CRI, NGVC, DBA, plus every micro-ETF in `volume_vs_average` (EAGG, SIZE, RSPR, GGR, SPCK, FTGC, FBND, FV, PFFV, NERV, PPSI, SPMB, STXF, BBCA, RSPC, BLCK, CZNC, EWQ). Also excluded despite otherwise-clean evidence: **ACN** (the cleanest genuine sub-close distribution block of the whole scan), **AMAT** ($363M genuine block above close), ADI, AAPL — none in the C12-passed set.

---

## Watchlist write-back

**Zero tickers written. No group created. `uw watchlist manage` was not invoked.**

Rule cited (corrected 2026-07-23): *write only names at LOW tier or better — never the raw top-5.* Every one of the 16 union names is tier DROP; the LOW band starts at 3 and the board's maximum was 1. MCHP is additionally excluded by the VETO rule. Writing today's top-5 by score would persist GLD/SLV/INTC/MCHP/DELL as "conviction" names the system explicitly refused, corrupting tomorrow's correlation and adverse-flow baselines.

Consequence: tomorrow's run will find no `conviction_2026-08-24` group and must fall back to `conviction_2026-08-21` (IWM), exactly as today fell back over the weekend. That is the intended behaviour of an empty board, not a failure.

---

## Decontamination casualties — six names killed before scoring

Recorded because the mechanisms are live and will recur:

| Ticker | What looked real | What decontamination found |
|---|---|---|
| **PLTR** | DISTRIBUTION verdict, mega buy_ratio 0.039 | **93.5% of mega premium is two prints at 20:00:06Z at the exact close.** After stripping, residual flow is buy-leaning **~61% — the signal reverses sign.** |
| **MSFT** | DISTRIBUTION verdict, ratio 0.4 | **≥34.7% of mega premium is part of the cross-name ~$500M basket print at 20:53–20:55Z**, which hit NVDA/MSFT/MU/AAPL simultaneously at near-identical notionals. 30d cum-flow is net *bullish* (+4.5%), contradicting. |
| **AMD** | ACCUMULATION, mega buy_ratio **1.00** | The $1.07B "100% buy" mega tier sits almost entirely inside the exact-closing-price bucket (456.75, 72 trades, $1.06B). |
| **WMT** | $117.1M print, watchlist alert, DEX flip | `institutional-accumulation` = **NEUTRAL** — fails the primary gate outright. |
| **GOOGL / GOOG** | ACCUMULATION (1.71–2.35) | Price faded from a genuine intraday shelf into the close, and C28 found **$1.69M of institutional call OI closing** — contradicting. |
| **AVGO** | mega buy_ratio 0.044 | Same closing-cross signature as AMD/PLTR/MSFT; C28 finds put OI closing ($960,593) **exceeding** the confirming call closes ($273,589). Survived as a low-confidence watch-only. |

Both stacked contamination mechanisms fired today — the closing-cross artifact *and* the basket/program print.

---

*Fleet: 10 Phase-1 agents (`opex-pin-strategist` omitted — 2026-08-21 monthly OPEX has passed, next is 2026-09-18; same precedent as 2026-07-20). Phase 2: quant → fundamentals-gate → risk-monitor. **Bull/bear debate (2c) skipped** — no name reached LOW tier, so the debate had nothing to gate. Steps 6, 6.5 and 8.5 (deep dive, batch-scan, deep-dive hand-off) skipped per the empty-board protocol. `fz` available; all `fz` lanes advisory, 0 rubric points. Envelope: `decision.json`, schema 1.3, rubric 2026-06-12, 22 calls, validated.*
