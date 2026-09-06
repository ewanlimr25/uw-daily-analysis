# Daily Market Analysis — 2026-06-12

## Executive Summary
- **Regime + GEX state:** **TRANSITIONAL / PULLBACK_IN_UPTREND.** SPY 741.75 (below 20sma 745.07, above 50sma 722.80; −2.45% from 90d high). SPY & QQQ both **freshly flipped to fragile long-gamma on 06-12** out of a week of deep negative gamma (SPY total GEX +39.6M, QQQ +424.9M — razor-thin). VIX 17.68. Options-flow breadth **BEARISH (38.6% bullish)** against a strongly green price tape (78.9% advancers) — a **hedged, skeptical rally**. Sector lean: Tech-led inflow, but the instrument tape (SMH put-wall) is de-risking.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`. The ≥9 HIGH cut failed its 2026-06-12 re-confirmation; P0.6 guard active, 0/30 post-freeze calls resolved.
- **Next-session GEX (SPY/QQQ):** *Advisory, see §2.* **SPY** — long-gamma (fragile), ZGL unreliable, call wall **743** (≈at spot), put wall **730** → pin/mean-revert bias, fade pokes past 743 toward 742, line breaks below 735/730. **QQQ** — cleaner long-gamma, call wall **723** (cluster 720–723 straddling spot), put wall **715** → pin ~722, loosens below 715.
- **Top swing build:** **None at conviction.** This is a **no-edge day** — zero names reach HIGH or MEDIUM. The single scored survivor is **SMH SHORT (LOW, raw 3, starter)** — a semis de-risk / FOMC tail-hedge read (deep-OTM put build), not a momentum short; carry defined-risk only, flat before the 06-17 FOMC, win_rate 0.447 (n=114), +13.7pp market excess.
- **Top LEAP candidate:** **None at conviction.** USAR (DIRECTIONAL_LONG, 6/8 gates, marginal) is single-signal → watch-only (§8).
- **Biggest risk:** **FOMC + SEP/dot-plot Wed 2026-06-17 (T+3)** — a binary inside every swing horizon, with both indices on a freshly-flipped, fragile long-gamma line that a gap can re-arm to short-gamma trend. Secondary: the **semis correlation cluster** (SMH/IWM/MU/MRVL/SNDK/USAR all ≥0.70) — one bet, not six.

> **Bottom line:** Defensive tape into a stacked-binary week (Retail Sales 6/16, FOMC 6/17, ACN/triple-witch 6/18). The options book is hedging a green rally; no clean directional edge cleared the confluence gate. Stand mostly aside; the only validated playbook is the delta-neutral 0DTE premium-sell (§2a), and that, too, is advisory and should stand aside if VIX spikes into the Fed.

## 1. Regime & Gamma State
- **`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend PULLBACK_IN_UPTREND. SPY 741.75, change_30d −0.08%, −2.45% from 90d high. Guidance: half sizes, defined-risk, iron condors in range.
- **Breadth:** options-flow breadth BEARISH — 2,412 bullish / 3,830 bearish flow tickers (38.6% bullish). **`fz` price breadth (advisory):** 397 advancers / 106 decliners, **78.93% green**, avg +0.78%. → **flow-vs-price divergence**: a broad up-day the options tape is fading/hedging.

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 741.77 | 334.92 *(unreliable)* | +39.6M | long-gamma (fresh, fragile) | 743 | 730 |
| QQQ | 721.93 | 211.16 *(unreliable)* | +424.9M | long-gamma (fresh) | 723 | 715 |
| IWM | 292.95 | — | +3.39M (flipped +ve 6/12) | long-gamma (fresh) | 300 / 295 | 282 / 275 |

- **`uw options-flow dte-volume-share`:** BALANCED — weeklies 29.4%, monthlies 13.9%, LEAPs 4% (0DTE field empty in the parquet this date). Monthly+ ~18% = mixed/retail-leaning tape.
- **`uw historical vrp` (SPY):** **FAIR** — IV30 14.87% vs RV30 13.62% (+1.25pp). No clean VRP edge; premium-selling only mildly favored.
- **Macro backdrop (`fred_macro`):** Yield curve **NORMAL** (10y−2y +0.39). Core CPI **2.96%** / core PCE **3.29%** YoY — **sticky, above target**. Unemployment 4.3%, payrolls +172k. 10Y 4.45% (flat 30d), 2Y 4.05%. **USD strengthening** (+1.98 30d). Fed funds 3.62%. **Forward event risk:** Retail Sales ~6/16 (MED) · **FOMC + SEP/dot-plot 6/17 (HIGH, ≈98% no-change priced)** · jobless claims 6/18 (LOW) · Core PCE ~6/26 (HIGH).

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book (OI persists overnight) read as the *prior* for the next session's open (2026-06-15, Mon). Prose-only, 0 rubric points, no backtested predictive claim. SPY/QQQ only.

**Lead caveat: both regimes flipped POSITIVE only on 06-12** out of a week-long FULLY_NEGATIVE stretch (SPY 06-05→06-11; QQQ 06-05→06-10), with near-zero (SPY) to modest (QQQ) total GEX. This is a **brand-new, low-magnitude, one-session long-gamma regime sitting on the flip line** — the mean-reversion/pin prior is shallow and a gap (esp. into FOMC 6/17) can re-arm short-gamma trend behavior fast. Discount accordingly.

### SPY — long-gamma (fragile)
- spot 741.77 · ZGL 334.92 **unreliable** (deep-OTM extrapolation; read off total_gex sign + spot-vs-wall) · total_gex **+39.6M** (razor-thin).
- **call wall 743** (+173.2M, with 742 +172.9M — a twin wall essentially **at spot**; secondary magnet 750). **put wall 730** (−106.1M; support 735, 720).
- **Read / structure bias:** Spot pinned against the 742–743 wall; dealer long-gamma hedging caps and reverts toward it. Realistic next-session range ≈ 735–750. **0DTE: iron fly / short straddle centred 742–743** (matches §2a); fade pokes above 743 back toward 742; the pin breaks below 735/730 (re-arms trend).

### QQQ — long-gamma (cleaner)
- spot 721.93 · ZGL 211.16 **unreliable** · total_gex **+424.9M**.
- **call wall 723** (+146.8M, with 720 +142.8M — twin cluster straddling spot; magnets 725/735/740). **put wall 715** (−22.7M, diffuse — support is the 720 cluster, not a true wall).
- **Read / structure bias:** Stronger long-gamma pin than SPY. **0DTE: iron fly / short straddle / butterfly ~722**, condor wings 715/735; fade extensions toward 720–723; loosens below 715.

**Mandatory caveats:** EOD = prior, not a target (re-read at the open after fresh 0DTE OI floods in); **gap/event risk voids the prior** (FOMC 6/17, Retail Sales 6/16 inside horizon); ZGL unreliable on both (deep-OTM extrapolation); **D+1 expiry cannot be isolated** (`gex --dte-max 1` errors; this is the 0–45d proxy); **ETF book, not the cleaner SPX/NDX index book**.

### 2a. Next-session 0DTE premium-selling setup (`zerodte_setup` — the validated stack)
> Advisory, delta-neutral, **0 rubric points**, NOT a guaranteed edge (validation sample has **no vol shock** — the short-vol left tail is UNSAMPLED). The GEX walls above are a map, not a pin (wall-as-magnet backtested NO_GO). What validated is a delta-neutral VRP premium-sell.

| Index | sell_premium | vol_state / VIX | implied / expected range | mean PnL (gross / **net**) | size | structure / entry |
|---|---|---|---|---|---|---|
| **SPY** | YES — `GO_PREMIUM_SELL_INTRADAY` (n=44, win 95.5%) | MID / 17.68 | 0.75% / 0.77% | +0.319% / **+0.219%** | 1.0× | iron fly @742.49 ±0.77%; enter after open once gap resolves, **hold to close, never overnight**; stand aside if it gaps beyond wings |
| **QQQ** | YES — `GO_PREMIUM_SELL_INTRADAY` (n=44, win 90.9%) | MID / 17.68 | 1.19% / 1.21% | +0.417% / **+0.317%** | 1.0× | iron fly ~722 ±1.21%; same entry/exit rule; **weaker** (NDX index book unavailable) |

`pnl_basis`: **% of underlying spot notional, GROSS of costs** (0.1% round-trip assumed) — lead with the **net** figure; it is tiny in absolute terms and a negatively-skewed short-vol edge. **Override: stand aside if VIX spikes or front-end backwardation appears into FOMC 6/17.** Promotion bar (P1.8): stays advisory permanently until a vol-shock enters the sample AND net expectancy clears a tail-aware bar.

## 2a. Swing Dealer Positioning (1–4 weeks)
`dealer-positioning-strategist`: under the **mechanized** DEX-flip definition (verified sign change + magnitude floor), **only IWM** produces a clean, scoreable flip:
- **IWM — swing_bias LONG (scoreable +1):** net_dex 6/10 −12.84B → 6/11 +7.60B (≥4 prior NEG sessions), flip-day |Δ| 0.87× trailing-10 median (≥0.25× floor), confirmed +14.77B 6/12; multi-strike GEX corroborates (not a single-strike artifact). *Tension:* call-heavy book → vanna is a mild headwind, not a squeeze. **Single-agent → §8 watch-only** (failed the ≥2-agent confluence gate).
- **SPY** flip **fails** the magnitude floor (flip-day 0.19× median); **QQQ** flip **fails** the ≥3-consecutive-prior-session run; **MU/AMD** = positive DEX *levels* in an up-tape (NOT flips, 0 points).
- **META — 6 consecutive negative-DEX sessions** (dealer put-heavy) **vs +269M bullish net-premium tape** — a flagged conflict; vanna-squeeze "MATURING" only (VIX has just 2 clean down-sessions, needs 3). Watch.
- **No vanna-squeeze flag fires** anywhere (VIX 6/10→6/12 down-run is only 2 sessions).

## 2b. Sector Rotation
`sector-rotation-strategist`: **`rotation_regime = no_change` (low confidence).** GICS layer is non-discriminating — all sectors net-inflow, near-uniform persistence 1.0 (whole-tape inflow day); Healthcare's +3.85B is a single-day 06-12 anomaly (discounted). **Zero single-name leaders clear the conditional +1** (all fail the $50M cum_flow floor or contradict on 30d direction: BAC/COF/TROW/HD aligned but <$50M; PDD −55M / BABA −25M contradict).

The actionable instrument-level tell is **bearish, not a rotation**: the ETF options tape disagrees with the bullish GICS aggregate and tilts net-defensive — consistent with the Step-0 flow-vs-price breadth divergence.

**ETF flow tape (advisory, 0 points):**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| **SMH** | **−$121M (outflow, dominant)** | BEARISH 5d | block @ −mid | **heavy PUT buying** (Aug 475P, Dec 600/450P) | **disagree** (GICS Tech +5.57B) | ADBE, INTU, AAPL, FSLR |
| XBI | −$8.5M outflow | BEARISH | call bid + put hedges | modest | agree (Healthcare OUT) | UNH, MRK |
| KRE | −$21M outflow | BEARISH | creation/redemption (non-directional) | small calls | disagree (XLF inflow) | — |
| EWY | +$15.4M | mixed | block sell-lean | put-heavy sweeps | n/a (country) | — |
| XLP | +$7.25M | BULLISH 5d | quiet buying near ask | none | agree (Staples defensive) | — |
| XLF | +$2.19M | BULLISH | — | — | agree (Financials) | BAC, COF, TROW |
| XLY | +$1.66M | BULLISH | — | — | agree (Cyclical) | HD, BKNG |

Lead: **SMH the dominant outflow** (semis hedging/de-risk) vs a quiet **XLP defensive bid**. The one swing-book implication is *caution*, not a rotation trade: stay light/defined-risk on semicap longs into FOMC 6/17; the ROKU/SNDK/KLAC semicap RS is a price move the options tape is fading.

## 3. Swing Setups (1–6 weeks)
**No HIGH/MEDIUM-conviction swing setups today.** One LOW-tier scored short.

### 3a. Long swings (regime-aligned)
**None cleared confluence.** The candidates were all single-signal (see §8): IWM (DEX flip, LONG), MRVL/SNDK (bullish sweeps — but MRVL's flow turned net-bearish on the carried watchlist, see §6), USAR (LEAP). AMZN had a genuine bull call vertical (multileg) **but carries a distribution counter-signal** (accumulation-hunter: cum_flow −188.7M, COVERED_CALL, Aug-240C −7,350 OI unwind) → conflicted, watch-only.

### 3b. Short / fade swings (defined risk only)

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **SMH** | 3 (LOW) | Semis **de-risk / FOMC tail-hedge** — opening ask-side PUT build (420/450/525/545 P, Jul/Aug), cum_flow_30d −77.9M / 90d −211.4M, ETF outflow leader (−$121M put-wall). **But the puts are deep-OTM (12–32% below spot 619.96) = crash protection, not a momentum short**; SMH actually closed **+2% over 10d and green on 06-12** (net_flow +14M). | **Defined-risk put spread only** (e.g. Jul 580/540), NOT naked short; or skip | Loses the bearish read if SMH reclaims the 06-12 high on call buying **or** the SEMICAP RS cluster (KLAC/VECO/SNDK new-highs) extends; **flat before FOMC 6/17** | **starter** (P0.6 half-cap; WR 0.447/n=114, +13.7pp excess; FOMC tail) |

Near-term **sweeps** (informational, 0 points unless co-flagged): GOOGL bearish (cum_flow −495M aligned, opening call-selling), NVDA bearish-lean (cum_flow −51.6M, noisy), MRVL/SNDK bullish (qualified). Single-leg whale Tier-1 PUT blocks (DTE6, 6/19 expiry, advisory C19): **GS** (OPENING_PUT_PRIME), and FLOOR_PUT blocks on AMZN/COIN/CRM/MSFT/MSTR/NFLX/PLTR/PYPL/TMUS/ZS/ZTS/LOW — a defensive single-leg tape consistent with the bearish flow breadth.

## 4. LEAP Builds (6–24 months)
**No qualified LEAP at conviction.** `leap-positioning-radar` surfaced **USAR** (DIRECTIONAL_LONG, leap_directional, 6/8 gates — *marginal*: Gate 8 cleared only via the alt LEAP-tenor path, same-day matrix 16.3%; Gate 4 cum-flow positive but small/MIXED). DTE-189 $30C ask-side 20:1, DP defense shelf $21.90–$22.35, IVR 12 (cheap vol), strong-buy rated (+79.6% target), institutions adding (+35.9%). **Single-agent → §8 watch-only**; if traded, defined-risk LEAP call debit spread (Jan-27 $25/$35), half-size.

Disqualified: **PYPL** (distribution dressed as deep OI — cum_flow negative both windows, LEAP calls bid-side, DISTRIBUTION matrix); XYZ (4/8, 30d accretion stalled); GLD/FXI/EFA/M/ARCC (fail the fresh-LEAP-build gate).

## 5. Volatility Surface
`vol-surface-scout` / `earnings-scout` — the cleanest single-name vol is in two earnings names (both SELL VOL, half-size, defined-risk):

| Ticker | State | Setup | Verdict | Note |
|---|---|---|---|---|
| **ACN** | **KINKED @ 6/18** | +44.3pp front kink, 1.65× ratio; front-end-iv-ratio **1.891 (PANIC)**; implied move ~10%; z+1.60 | **SELL VOL — half** | Earnings 6/18 BMO (confirmed). Back-month flat (not stretched) + extreme front ratio → half only. **Below conviction floor (raw 2, DROP) — earnings-desk only.** FOMC 6/17 stacks a 2nd binary one day prior. |
| **KR** | **KINKED @ 6/18** | +21.3pp kink, 1.54×; implied move ~5%; defensive (cleanest from FOMC) | **SELL VOL — half** | Single-agent → §8 watch-only. Near-back skew the one positive tail read. |
| MU | front-loaded BACKWARDATION | FOMC + earnings 6/24; z+1.49 (pct PROVISIONAL n=44); IVR 99.6 | SELL VOL into earnings | Single-agent → §8 watch-only; vol is macro/sector-driven, revisit post-FOMC. |

**Substrate note:** the `iv-term-structure` classifier is degenerate on this date (expired `dte=-1` bucket inverts the label, `kink_expiry` null on every name) — all KINKED reads above are hand-reconstructed after dropping the contaminated front bucket. IV percentiles are PROVISIONAL (n=44 < 120 floor); z-scores lead. No clean no-catalyst calendar exists (every backwardation is FOMC- or earnings-driven). No qualifying IV outlier (all were 0DTE expiry-day gamma noise on leveraged ETFs).

## 6. Risk & Correlation
**Macro headline:** sticky core inflation (core CPI 2.96% / core PCE 3.29%, both above target), normal curve, strengthening USD, Fed funds 3.62% — into a **stacked-binary week**: Retail Sales 6/16 (T+1, MED), **FOMC + SEP/dot-plot 6/17 (T+3, HIGH)**, jobless claims + ACN earnings + triple-witch 6/18 (T+4), Core PCE 6/26 (HIGH).

- **Correlation clusters (`uw risk portfolio-correlation`, 30d):** a **semis_megacap_cluster** fires hard — SMH/IWM **0.831**, SMH/MU **0.809**, IWM/USAR 0.789, SNDK/MU 0.777, SMH/USAR 0.744, SMH/MRVL 0.728. **SMH is the only *sized* member** → kept member, no cluster penalty; but IWM/MU/MRVL/SNDK/USAR are the **same semis bet** — never let two pass at size on a future day.
- **Regime/VRP/panic gates:** regime TRANSITIONAL (SMH short aligns with the bearish flow breadth); VRP FAIR (no clean vol edge); SPY front-end not in market-wide panic (ACN's 1.89 ratio is its *own* earnings kink being sold, not an override).
- **Fundamentals verdicts (top-2):** **ACN CONFIRM** (earnings 6/18 BMO confirmed, beat-streak 4/4, insider buying MSPR +44.7, low leverage — a stable name to sit short-vol on; key risk = two stacked binaries 6/17 + 6/18). **SMH NA** (ETF — gate never penalizes). No VETO, no CAUTION.
- **Event-risk flags:** **SMH** — FOMC 6/17 (T+3) is a beta-wide binary that dominates a 1.73-beta semis ETF over the swing horizon → carry defined-risk, **flat before the Fed** (or skip). **ACN** — event-exempt (the SELL-VOL trade *is* the 6/18 earnings event).
- **Debate-disconfirmation:** **N/A** — no MEDIUM+ conviction name existed to stress-test; the bull/bear step had no qualifying input (a genuine outcome on a no-edge day, not a skipped step).
- **Adverse-flow exit list** (vs `conviction_2026-06-11` = AAPL/MU/MRVL/ASML): **MRVL — exit-candidate** (watchlist scan shows net-bearish flow today, conflicting with the carried bullish thesis); **AAPL — soft exit** (flow turned bearish, −20.8M); MU (+100M) / ASML (+8.4M) on-thesis, hold.
- **Breadth cross-check (advisory):** 397 adv / 106 dec, **78.9% green**, avg +0.78% — but UW options-flow breadth is **bearish (38.6%)**. Price-vs-flow divergence = a hedged/skeptical rally (the day's dominant structural read). `divergence_flag=false` (the schema flag only fires on green + pct_green<50). Advisory, does not change sizing.
- **Hedge sleeve:** **none required** — one starter short (SMH) + one non-directional sell-vol (ACN, skip-floor) = negligible net book delta. If SMH is carried through 6/17, express it as a defined-risk put spread (self-hedges the FOMC tail) rather than a naked short.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)
**EMPTY — no HIGH or MEDIUM names today.** The conviction book did not clear a single name to `raw_score ≥ 7`. This is a valid "no-edge" output, consistent with the OUT-OF-REGIME / TRANSITIONAL tape and the hedged-rally breadth divergence.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no resolved post-2026-06-12 conviction calls exist yet (0/30 toward the P0.6 re-validation), so no per-tier realised expectancy/payoff is available this run. The most recent `/calibration-audit` (2026-06-12) found the tier bands **inverted** on the first post-UPTREND window (HIGH 0.222 / MED 0.214 / LOW 0.444) — the explicit reason every size is capped at half until ≥30 post-freeze calls resolve.

For completeness, the two scored (sub-HIGH/MEDIUM) names and their audit trail:

| Ticker | raw | tier | class | win_rate (n, source) | mkt_excess | pre→final size | fund. | debate | gates applied |
|---|---|---|---|---|---|---|---|---|---|
| SMH | 3 | LOW | bearish_flow | 0.447 (114, backtest_clean) | +0.137 | starter→**starter** | NA | n/a | rubric_regime=half-cap, event_risk=FOMC T+3, cluster=kept-member |
| ACN | 2 | DROP | earnings_vol | null (NA substrate) | n/a | skip→**skip** | CONFIRM | n/a | event_risk=EXEMPT (trade is the event), rubric_regime=moot |

**Recommended deep dive:** none — no HIGH-tier name to hand to `/stock-deep-dive`. (Step 8.5 correctly skipped on a no-edge day.)

### Conviction-scoring rubric (v2026-06-12, FROZEN) — embedded for audit
```
Daily conviction score = Σ:
  +1  dealer-positioning MECHANIZED DEX flip / vanna-squeeze in trade direction (verified sign change + |net_dex|≥0.25× trailing-10 median; vanna needs dated falling-VIX)
  +3  3+ aligned accumulation signals (DP+OI+smart-positioning, block-stratified institutional) — CONJUNCTION: full +3 only if cum_flow_30d sign-aligned AND |cum_flow_30d|≥$50M; else halved → +1
  +1  multi-day OI build (oi-trend BUILDING, --days≥5)
  +1  conviction-matrix DIRECTIONAL_LONG conf>70 — CONDITIONAL: only when dominant_signal_class==leap_directional; else 0
  +1  cum-premium-flow net directional accretion in trade direction (30d) — INTENT-SCREENED (no C28 distribution_flag; no ex-div deep-ITM sub-parity calls)
  +1  sector-rotation single-name leader — CONDITIONAL: persistence≥0.6 AND cum_flow_30d aligned AND |cum_flow_30d|≥$50M; else 0
  +1  earnings-scout BUY VOL or SELL VOL
  +2  multileg-strategist directional structure (term-structure-anchored play type)
  +1  vol-surface-scout KINKED/BACKWARDATION with VRP-aligned bias
  +1  opex-pin-strategist top-5 (OPEX week only)
  -2  contrarian overcrowded long w/ rising pc-ratio-zscore (informed-flow continuation penalty; multi-date z required)
  -3  flow_conflict (cum_flow 30d clearly opposite dominant class) | -1 flow_conflict_lite (MIXED) — mutually exclusive
  [TIER GATES, risk-monitor 2d, NOT score_components]: -1 tier corr-cluster ≥0.70 ; -1 tier regime conflict
Tiers: ≥9 HIGH (full) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 drop.
OUT-OF-REGIME guard (P0.6): ALL sizing capped at half until ≥30 post-2026-06-12 calls re-validate the tiers.
```

## 8. Watch-only — single signal, no confluence
Surfaced by one agent only (or conflicted) — **journaling, NOT trade entry today.**

| Ticker | Dir | Flagging agent | Note |
|---|---|---|---|
| IWM | LONG | dealer-positioning | Mechanized DEX flip 6/10→6/11 (scoreable +1, 1 agent). Fragile fresh long-gamma. |
| GOOGL | BEARISH | sweep-tracker | cum_flow −495M aligned, opening call-selling, 3/5 persistence. Cleanest scorable bearish mega-cap. |
| MRVL | BULLISH→⚠ | sweep-tracker | cum_flow +141M, 5/5 build — BUT carried-watchlist flow turned net-bearish today (exit-candidate, §6). |
| SNDK | BULLISH | sweep-tracker (+fz RS) | cum_flow +1.19B, RS new-high leader (+5.2%). Two-sided intraday tape. |
| NVDA | BEARISH-lean | sweep-tracker | cum_flow −51.6M aligned, noisy near-term call tape. |
| KR | SELL VOL | earnings-scout | KINKED @6/18, defensive grocer (cleanest from FOMC). |
| MU | SELL VOL | vol-surface-scout | front-loaded BACKWARDATION into 6/24 earnings; IVR 99.6 (macro/sector-driven vol). |
| AMZN | conflicted | multileg (LONG) vs accumulation (DISTRIBUTION) | Bull call vertical Aug 270/295 (repeat=1) **vs** ⚠ distribution_flag (240C −7,350 OI unwind, cum_flow −188.7M, COVERED_CALL). Do not promote. |
| USAR | LONG (LEAP) | leap-radar | DIRECTIONAL_LONG, 6/8 gates marginal, +1 conviction-matrix eligible. DP shelf $21.90. |
| EFA | LONG | accumulation near-miss | Real mega+block DP + BUILDING + cum_flow +56M, but conviction-matrix conf 42 (<50 gate). |
| XOM | LONG | accumulation near-miss | DP $395M defense @147.01, BUILDING, but conf 45 (<50). |

---
*Generated 2026-06-13 for the 2026-06-12 session. Phase 1: 10 alpha-finding agents (no OPEX agent — 6/19 OPEX is 7d out). Phase 2: quant → fundamentals → (debate N/A) → risk. Watchlist `conviction_2026-06-12` = [SMH, ACN].*
