# Weekly Market Intelligence — Week of 2026-05-25 (ISO 2026-W22)

*Holiday-shortened week — Memorial Day Monday 05-25 dark; 4 covered sessions 05-26→05-29. Fresh post-week analysis off the actual W22 tape (supersedes the 2026-05-25 week-ahead prep/A/B stub). Data: `uw` CLI (flow/greeks/DP/GEX), `fz` CLI (non-flow breadth/short-interest/analyst), FRED macro, Finnhub fundamentals.*

## Executive Summary
- **Week regime + WoW Δ:** Regime **HELD TRANSITIONAL** ("reduce size, wait for clarity") on a technical **UPTREND** (SPY 756.48, above 20/50SMA, +6.3% 30d) — but **breadth deteriorated** all week: bullish-flow tickers 40.1%→36.3%, and the `fz` cross-check reads **pct_green 38.77%** (advancers 195 / decliners 308). That is the defining tension of the week: a melt-up index masking a narrowing, distributing tape. **VRP FAIR** (SPY +0.027, QQQ +0.044) — no premium edge either way.
- **Signal performance:** **6 of 9 directional theses confirmed (66.7% hit rate).** The long/accumulation book ran clean (MSFT +7.6%, MU +29.3%, ORCL +17.5%, PLTR +14.4%, DELL +42.6% on earnings); the **short book got run over** (SMH +3.9%, IWM +1.9% both *rose*; PANW bearish-flagged +8.1%). The up-tape rewarded longs and punished shorts — vindicating the decision to gate every short to skip.
- **Top swing build for next week:** **MSFT — LONG, half size.** The only name to clear the full gate stack. Dark-pool accumulation C11 **FULL CLEAR** (mega-tier buy_ratio 0.94 ∧ +$770M 30d cum-flow ∧ ACCUMULATION), OI BUILDING 5/5 +446K, dealer DEX +$14.1B (#1 in fleet), fundamentals **CONFIRM** (4/4 beat streak, $37B AI run-rate, earnings out at Jul-29 = no binary in horizon). Invalidation: DP support break < $427. **Caveat: win_rate is a fallback proxy 0.50 (N=2) — confluence, not a validated edge.**
- **Top LEAP build:** **None cleared.** MSFT is the sole contender (fresh Dec-2027 build ~31.7K, 5 of 9 gates) but fails the conviction-matrix gate (35% < 70% — diluted by 40.8% 0DTE retail tape). Watch into post-FOMC.
- **Biggest emerging risk:** **AI/mega-cap concentration + a wall of June event risk.** Five of six scored names are Tech-adjacent; the SMH/IWM short pair correlates 0.762. Tier-1 catalysts stack into the swing window — AVGO earnings Jun-3, NFP Jun-5, **CPI Jun-10**, **FOMC + dot-plot Jun-16/17**. Sticky core PCE 3.29% + rising 10Y (4.45%) + strengthening USD leave little room for a dovish surprise; high-multiple names (AVGO 84x, ORCL D/E 4.67) are most exposed.

---

## 0. Week in Review — Intra-Week Signal Performance

Early-week direction (signal as of 05-26/27) graded against the 05-29 close (week move measured 05-22→05-29 via `uw historical trend`).

| Ticker | Signal type | Early-week direction | Week move | Week-end flow | Grade | Note |
|---|---|---|---|---|---|---|
| MSFT | dark_pool_accumulation | LONG | **+7.6%** | bullish (3/2) | **WIN** | C11 full-clear thesis confirmed by price + flow |
| MU | oi_build / sweep | LONG | **+29.3%** | bullish (4/1) | **WIN** | OI BUILDING 5/5 +961K; flow MIXED but price ran hard |
| ORCL | dex_flip_long | LONG | **+17.5%** | bullish (4/1) | **WIN** | Post-earnings dealer DEX flip paid; contrarian fade was *early/wrong* this week |
| PLTR | dex_flip_long | LONG | **+14.4%** | bullish (2/3) | **WIN** | DEX flip negative→+$6.3B confirmed |
| DELL | earnings BUY VOL | LONG/vol | **+42.6%** | bullish (4/1) | **WIN** | +62% EPS surprise; AI-server read-through; SELL VOL would have been catastrophic |
| MRVL | oi_build / sweep | LONG | **+4.4%** | bullish (4/1) | **WIN** | Beat-via-guidance; OI BUILDING 5/5 |
| AAPL | dark_pool_accumulation | LONG (conflicted) | +1.0% | bearish (3/2) | **INCONCLUSIVE** | Flat; flow contradicted accumulation (insider selling) |
| PANW | bearish_flow / fade | SHORT | **+8.1%** | bearish (3/2) | **LOSS** | Price rose against bearish flow — fade was wrong |
| SMH | bearish_flow | SHORT | **+3.9%** | bearish (1/4) | **LOSS** | Semis rose; short into Tech-inflow tape was wrong this week |
| IWM | dex_flip_short | SHORT | **+1.9%** | bearish (2/3) | **LOSS** | Small-caps rose; short into uptrend was wrong this week |

**Hit rate: 6 WINS / 3 LOSSES (AAPL inconclusive, excluded) = 66.7%.** The lesson is asymmetric: every *long* confirmed, every *short* failed. In a TRANSITIONAL-but-up tape, the bearish microstructure (put hedging, GEX flips, sweep persistence) read as conviction but resolved as *hedging noise* against a relentless index bid. This is precisely the regime where the short book must be sized as hedges, not directional alpha — which is what the gate stack enforced below.

---

## 1. Regime & WoW Delta

The week opened and closed in the same **TRANSITIONAL** regime label, but the internals deteriorated. Bullish-flow tickers fell from 40.1% (05-26) to 36.3% (05-29) even as SPY held its 30-day +6.3% and stayed above both moving averages. The `fz` breadth cross-check — a separate data lineage — corroborates the divergence: **38.77% green** with the index near highs is a textbook narrowing-leadership / distribution signature. Treat the up-tape as fragile and mega-cap-dependent, not broad.

**Vol regime — `uw historical vrp`:** SPY VRP +0.027 (IV 12.7% vs RV 10.0%), QQQ +0.044 (IV 20.2% vs RV 15.8%) — both **FAIR**. Mildly rich implied vol, no decisive premium-selling edge. This neither favors vol-sellers nor vol-buyers strongly; it does mean naked long-premium directional bets carry a small carry drag.

**Institutional vs retail — `uw options-flow dte-volume-share`:** 0DTE share climbed to **40.8%** by Friday (weeklies 21.2%, monthlies 18.2%, LEAPs 5.9%) → **RETAIL_DRIVEN** hint, up sharply from ~20% mid-week. Friday's expiry mechanically inflates 0DTE, but the magnitude flags a retail-crowded week-end — a reason to discount single-day momentum and lean on multi-day persistence.

**Macro backdrop (`fred_macro`):** Yield curve normal (+0.46). Core CPI 2.99% / **core PCE 3.29% YoY — sticky, above target.** Unemployment 4.3%, payrolls +115k (cooling). **10Y 4.45% and rising; USD strengthening; fed funds 3.62%.** The mix — sticky inflation, cooling-but-not-cracking labor, rising long end — is restrictive and argues against an aggressive cut. **Forward event risk (next 2 wks):** AVGO earnings Jun-3 · **NFP Jun-5** · **May CPI Jun-10** · PPI Jun-11/12 · **FOMC + SEP/dot-plot Jun-16/17** (highest-impact). Any swing held past Jun-16 wears binary repricing risk.

**Implication for next week:** Stay long-quality-and-narrow, hedged. The tape rewards mega-cap AI leadership but the breadth math and the June event wall argue for half-size, defined-risk, and a hedge sleeve rather than gross exposure.

---

## 2. Sector Rotation

**Rotation regime call: `no_change` (low confidence).** All 11 GICS sectors printed positive weekly net flow (persistence_score = 1.0 across the board) — a broad inflow tape, not a selective rotation. Differentiation is by **magnitude**, not persistence: Technology dominates at **+$11.6B** week-end net flow, an order of magnitude above Financial Services (+$1.40B), Comm Services (+$1.06B), and Consumer Cyclical (+$1.04B). The honest read is *growth-narrowing-within-growth* (software/AI leadership) rather than a canonical defensive↔cyclical or growth↔value rotation. The 05-29 intraday tape did show Comm Services (-$104M) and Consumer Cyclical (-$50M) rotating *out* — early profit-taking inside a strong weekly inflow.

The most actionable structural fact is the **software-over-semis split inside Technology**: software (IGV +$49.4M, XLK +$20.5M) being accumulated while semis (SMH **-$70.0M**, heavy multi-expiry put sweeps) are being hedged/de-risked into the June CPI/FOMC events. Within Energy, flow favors integrated majors (XLE inflow, Sep call sweeps) over E&P (XOP outflow).

**ETF flow tape (advisory — 0 rubric points):**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| IGV | **inflow** | BULLISH 5/5 | $113M/$49M/$26M blocks (creation, not single-name) | Dec-26 $90C $61.9M bullish | **agree** | MSFT, PLTR, NOW, DOCN |
| XLK | inflow | BULLISH 5/5 | $152M/$100M MOC blocks | Low directional | agree | (Tech leaders) |
| XLE | inflow | BULLISH 5/5 | $109M/$55M close blocks | Mar-27 risk-reversal + Sep $60C | agree (contra-XOP) | CVX, FANG, KMI |
| **SMH** | **outflow** | BEARISH 5/5 | $153M/$73M blocks | **HIGH bearish** — Jun/Jul/Aug put sweeps into CPI/FOMC | **disagree** (Tech bullish) | short: TSM, INTC, ASML |
| GDX | outflow | BEARISH 5/5 | mixed/ambiguous | mixed (Sep $100C vs puts) | disagree | skip — ambiguous |
| XOP | outflow | BEARISH 5/5 | thin | negligible | disagree | skip — thin |

**Read:** Institutions are buying software/AI (IGV/XLK + MSFT/PLTR/NOW) while *hedging* the semiconductor complex (SMH puts) into the June event wall — a pair-trade theme, not a sector rotation. The ETF tape strengthens (does not score) the Tech-leader conviction on MSFT.

---

## 3. Swing Book (1–6 weeks) — ranked by weekly conviction score

### 3a — Long swings (regime-aligned)

| Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure | Invalidation |
|---|---|---|---|---|---|---|---|
| **MSFT** | HIGH | 11 | 0.50* (fallback N=2) | **half** | DP accumulation C11 FULL CLEAR + DEX #1 + Tech leader; fundamentals CONFIRM | Long shares / Jul call debit spread; no binary until Jul-29 | DP support < $427; OI flips UNWINDING 2d |
| AVGO | MEDIUM | 9 | 0.50* (fallback N=0) | **skip** | DP accumulation + DEX; **but earnings Jun-3** | Event play only (defined-risk calendar) → else flat | miss/guide-down Jun-3; < $426 |
| AAPL | LOW | 6 | 0.50* (fallback N=2) | **skip** | DP accumulation **conflicted by insider selling**; debate lost | watch-only | insider MSPR persists; < $310 |
| ORCL | LOW | 6 | 0.79 → capped | **skip** | Dealer dex-flip-long **but** crowded-fade -1.639z, IVR 100, dual event | sell-vol/credit spread if traded | < $200; hot CPI Jun-10 |

\* dark_pool_accumulation backtest returned empty this run → fallback proxy 0.50. The 11 is *additive confluence*, not a validated win-rate — sized at half accordingly.

### 3b — Short / fade swings (defined risk only)

| Ticker | Tier | Score | Win-rate | Final size | Thesis | Note |
|---|---|---|---|---|---|---|
| SMH | MEDIUM | 8 | 0.419 | **skip** | Rolling put diagonal ×4 + ETF outflow into CPI/FOMC | Valid as a **hedge sleeve** vs semis longs, not a conviction short |
| IWM | MEDIUM | 7 | 0.419 | **skip** | dex_flip_short + GEX-negative + Jun-18 put vertical ×3 | 4 gate fires; squeeze risk if FOMC dovish; hedge only |

**Both shorts are structurally valid hedges but failed as standalone shorts:** WR 0.419 (< 0.50 floor) + shorting into a confirmed uptrend + the Step-0 scorecard already showing both *rose* this week. The bearish flow (-$1.09B 90d on IWM) is more credibly tail-hedging by longs than directional conviction.

---

## 4. LEAP Book (6–24 months)

**No LEAP cleared the strict 6-of-9 gate this week.** MSFT is the sole contender: a genuine fresh **Dec-2027 build (~31,700 contracts, $595–720 strikes)** across two sessions, with cum-flow +$770M/30d & +$874M/90d (fresh-thesis signature), DP whale prints ($832M @ $426.99), and ACCUMULATION confirmed — **5 clean gates.** It fails **Gate 8 (conviction-matrix 35% < 70%)**, because the matrix is overwhelmed by MSFT's heavy 0DTE/weekly volume (LEAP share only 5.9%) and cannot isolate the LEAP-specific flow. NVDA/PLTR/ORCL/AVGO/AMD all **disqualified** on Gate 4 (wrong-direction or put-dominated cum-flow) or Gate 8 (HEDGED_LONG/MIXED). Re-evaluate MSFT Dec-2027 calls post-FOMC if conviction-matrix crosses 50% and a third initiation episode appears.

---

## 5. Volatility Surface — WoW Term Structure & Skew Evolution

Every watched name expanded into the **mid-June earnings cluster** — universal 100th-percentile IV (Goyal-Saretto z-scores), amplified by the 4-day compressed week. The shape change is concentrated in the Jun-12/Jun-18 expiries (the $10.6B premium peak), where ORCL/ADBE/CRWD/PANW all migrated from LOW-CONTANGO to **KINKED-CONTANGO**.

- **Earnings kinks (SELL-VOL candidates, COMPLACENT back-skew):** ORCL (Jun-12 kink 93%, VRP +0.221), CRWD (Jun-18 kink 122%, VRP +0.208), PANW (Jun-5 kink 104%, VRP +0.213), ADBE (Jun-12 kink 71%, weakest VRP). All show calls richer than puts at 1y — market not hedging tail.
- **HPE** is the cleanest **calendar-spread** candidate: +4.22 IV z-score (highest non-leveraged), VRP +0.314, near/back ratio 1.72× — sell Jun-5 / buy Jun-26.
- **Disqualified backwardation (front-end-iv-ratio > 1.10, do not fade):** SPCE (2.83), SOXL (3.63), ULTA (4.03), MX (TAIL_HEDGING skew). Active event/panic — no calendar.
- **IV outliers** (SNDK 1600C 272%, SOXL 90C 367%, S 17.5P 292%) are all 0DTE expiry-day artifacts, not whale hedges.

---

## 6. Earnings — Recap & 2-Week Lookahead

**(a) Recap — W22 reporters (May 27–28):** The AI-infrastructure beat cluster dominated. **DELL** +62.2% EPS surprise → +42.6% week (**CONFIRMING** BUY VOL; SELL VOL would have been catastrophic). **SNOW** +20.2% → +48% (CONFIRMING). **NTAP** +5.1% → +25% (CONFIRMING). **OKTA** +4.7% → +33.7% (CONFIRMING — AI-security narrative). **CRM** beat EPS / missed rev → +6.2% (MIXED). **MRVL** -0.9% miss but guided well → +4.5% (DISCONFIRMING the numeric miss; SELL VOL partially worked). Vol-buyers won the week's prints cleanly; the AI read-through lifted the whole complex.

**(b) Lookahead — next 2 weeks (ranked):**

| Rank | Ticker | Date | Verdict | Back skew | Size | Anchor |
|---|---|---|---|---|---|---|
| 1 | HPE | Jun-1 amc | SELL VOL | COMPLACENT | full | DELL read-through pre-priced; Jun-5 kink 166% |
| 2 | PANW | Jun-2 amc | SELL VOL | COMPLACENT | half | Jun-5 kink 104%; equity-flow bearish vs options bullish |
| 3 | GTLB | Jun-2 amc | BUY VOL | n/a (small-cap) | half | 151% kink; call-biased; AI-security tail |
| 4 | AVGO | Jun-3 amc | CALENDAR | COMPLACENT | half | Jun-5 kink 90%; mega-cap tail; calendar captures crush |
| 5 | CRWD | Jun-3 amc | SELL VOL | COMPLACENT | half | Jun-5 kink 106%; neutral P/C; NFP same-week |
| 6 | CIEN | Jun-4 bmo | BUY VOL | n/a | half | Jun-5 kink 155%; balanced flow |
| 7 | ORCL | Jun-10 | SELL VOL | COMPLACENT | quarter | Jun-12 kink 93%; **CPI same-day** dual-event; crowded calls |
| — | ULTA | Jun-2 | SKIP | — | — | front-iv-ratio 4.03 (panic) |
| — | ADBE/LEN | Jun-11 | SKIP | — | — | back-month call skew / no kink |

Analyst-vs-flow divergence is the highest-EV tell; PANW (institutional equity bearish vs bullish options) is the cleanest. Mind the **NFP-Jun-5** straddle for all Jun-2/3 prints — size half, not full.

---

## 7. Risk & Correlation (week-candidate universe)

**Correlation clusters (`uw risk portfolio-correlation`, 30d):**
- **`broad_market_macro_cluster` — SMH / IWM corr 0.762** → cluster gate fires; SMH is the kept member (raw 8 > 7), **IWM takes -1 tier.** Both are short ETFs co-driven by the rising-rate/strong-USD macro.
- MSFT / ORCL 0.625 — soft watch (no penalty); both mega-cap Tech longs — review combined notional before sizing both.
- **Structural hedge note:** the AVGO long vs SMH short are opposing semis positions — SMH short partially *hedges* AVGO, it does not duplicate it.

**Concentration:** 5 of 6 scored names are Technology-adjacent — real single-sector concentration even though no adverse-rotation persistence gate fired (all sectors positive).

**Fundamentals verdicts (top-5):**
- **MSFT — CONFIRM.** 4/4 beat streak, $37B AI run-rate, D/E 0.26, analyst Recom 1.23 / +24% upside, earnings Jul-29. Risk: AI-capex FCF compression, RSI 69.6.
- **AVGO — CAUTION (-1).** **Earnings Jun-3 (5d)**, mixed beat/miss (2 of 4 misses), PE 84.7× near 52w high, only 7.5% analyst upside.
- **AAPL — CAUTION (-1).** **Insider MSPR -50.5 (May -100, pure sell)** into apparent accumulation = *distribution dressed as accumulation*; RSI 78.8 at 52w high; 1.3% analyst upside; flow internally contradicted (top_bearish net_flow vs +cum_flow).
- **ORCL — CAUTION (-1).** **Dual binary: CPI Jun-10 + earnings Jun-16.** D/E 4.67 (highest), current_ratio 0.75, IVR 100, crowded-long -1.639z.
- **SMH / IWM — NA** (ETFs). No VETOs issued.

**Debate-disconfirmation cuts:**
- **AAPL — bear 0.75 > bull 0.55 → cut.** Insider-selling-as-distribution unrefuted.
- **IWM — bull-of-short 0.65 = bear-of-short 0.65 → cut.** Both sides agree: trade as a defined-risk *hedge*, not a conviction short.
- **MSFT — bull 0.75 > bear 0.65 → no cut.** Both concede the win-rate is a fallback void; the multi-signal independence + clean fundamentals carry it.

**Event-risk gate:** AVGO (Jun-3 earnings), ORCL (CPI Jun-10 + earnings Jun-16), and all swing holds through FOMC Jun-16/17 are flagged. MSFT is the only name *outside* the FOMC blast radius (Jul-29 earnings).

**Breadth cross-check (advisory):** advancers 195 / decliners 308, **pct_green 38.77%** — divergence flag vs the green index tape; distribution tell, no size impact.

**Adverse-flow exits (vs prior `conviction_week_2026-W21` group {AAPL, OKTA, ADSK, MRVL, PANW}):**
- **AAPL — EXIT** (flow reversed bearish, $461M DP print + insider MSPR -100 corroborates).
- **PANW — EXIT / reduce** (flow bearish, IVR 100 — roll or close any long-vol).
- ADSK — MONITOR (P/C 2.78, 9.1× volume — ambiguous). OKTA — HOLD (bullish, RS breakout). MRVL — HOLD (DP $92.7M continues).

**Hedge sleeve:** Book is effectively 100% long (MSFT half only). Recommended: (1) **QQQ put debit spread** (ATM-2% / ATM-6%, Jun-16/20) to hedge the CPI+FOMC wall, ~0.25× MSFT notional; (2) **VIX Jun-18 20/25 call ladder** (VIX 15.3 cheap) ~0.1× as tail hedge; (3) **SMH put spread** as the explicit semis hedge ~0.15×.

---

## 8. High-Conviction Cross-Ref (HIGH and MEDIUM tier)

**MSFT — HIGH (raw 11) — LONG — final size half.**
Score components: +3 cum-flow (30d +$770M accretion), +3 accumulation C11 FULL CLEAR (DP block-stratified mega buy_ratio 0.94 ∧ cum-flow ≥$50M ∧ ACCUMULATION), +2 dealer dex_flip_long (DEX +$14.1B #1), +2 signal-confluence=5, +1 sector-rotation Tech leader. **win_rate 0.50** (fallback proxy N=2 — dark_pool_accumulation backtest empty; LB-gate 4/5 cited → HIGH preserved). `fundamentals_verdict` CONFIRM. Debate: bull 0.75 / bear 0.65 (no cut). gate_verdicts: all no-op (clean). The cleanest accumulation fingerprint in the tape, with the underlying fundamentals corroborating — but the absent backtest edge is why it sizes half, not full. **Invalidation: DP support break < $427; OI UNWINDING 2 sessions; conviction-matrix flips from DIRECTIONAL_LONG.**

**AVGO — MEDIUM (raw 9) — LONG — final size skip.**
+3 cum-flow, +3 accumulation, +2 dealer, +1 sector. CONFIRM-adjacent fundamentals but **CAUTION (-1)** on earnings Jun-3 + event-risk gate (-1) → skip as a hold. Tradable *only* as a defined-risk earnings-vol structure (calendar) through Jun-3. **Invalidation: miss/guide-down Jun-3; < $426.**

**SMH — MEDIUM (raw 8) — SHORT — final size skip.**
+3 cum-flow (-$78M/30d, -$114M/90d), +2 multileg (put diagonal ×4), +2 confluence, +1 sector. NA fundamentals. Regime gate (-1, short into uptrend) + event-risk gate (-1) → skip; **valid as a hedge sleeve** vs semis longs. **Invalidation: SMH > $560 on volume; semis inflow broadens.**

**IWM — MEDIUM (raw 7) — SHORT — final size skip.**
+3 cum-flow (-$273M/30d, -$1.09B/90d), +2 dealer (GEX flipped negative), +2 multileg (Jun-18 put vertical ×3). Four gate fires (regime -1, cluster -1, event-risk -1, debate -1) → skip. The strongest 90d short-flow in the union, but the debate and scorecard agree it's a hedge, not a directional short. **Invalidation: IWM > $220 on broad participation.**

*Embedded rubric (audit):*
```
+3 oi-trend BUILDING full week (--days≥5) | +3 accumulation 3+ aligned ∧ DP block-stratified institutional — C11 CONJUNCTION (full +3 only if cum_flow_30d sign-aligned ∧ |cum_flow_30d|≥$50M; else +1) | +1 conviction-matrix DIRECTIONAL_LONG conf>70 — leap_directional class ONLY | +2 oi position-rolls into LEAP | +3 cum-premium-flow net directional accretion | +2 signal-confluence≥4 week-end | +2 dealer DEX flip / vanna squeeze | +1 sector single-name leader (persistence≥0.6 ∧ cum_flow aligned ∧ ≥$50M) | +1 earnings BUY/SELL VOL term-skew aligned | +2 multileg directional repeat ≥2 days | +1 vol-surface KINKED/BACKWARDATION worsening | +1 opex top-5 | -2 contrarian crowded-long rising pcr | -3 flow_conflict / -1 flow_conflict_lite (mutually exclusive) | -2 corr cluster >0.7 | -3 WoW regime flip vs direction
Tiers: ≥10 HIGH / 7-9 MED / 3-6 LOW / ≤2 drop. multi_day_sweep = 0 pts (deprecated 2026-05-23).
```

---

## 9. Setups for Next Week

**Next-session GEX advisory (SPY/QQQ only — prose, 0 points).** Step-0 backtest verdict: **`NO_GO_NO_EDGE`** — over 60 sessions GEX walls were *not* magnets (next close landed closer to the nearest wall only 25% vs a 50% baseline, n=68; H1 ran backwards). Treat the levels as dealer context, not a forecast.
- **SPY:** spot 756.66, ZGL 755.93 (reliable, ~at-the-money), POSITIVE regime, total_gex +$1.22B. Call wall **757** (tight, $0.34 above), put wall **750**. Pinned within $1 of its own zero-gamma level — *no dealer buffer*; small moves flip hedging flows. Structure bias: tight iron fly / sell the 757 call against a 755–756 pin, but the regime is fragile.
- **QQQ:** spot 738.40, ZGL unreliable (extrapolated 308 — fall back to total_gex +$675.9M POSITIVE + walls). Call wall **750** (+1.6%), put wall **720** (-2.5%); thinner book than SPY. Band ~720–750, condor-friendly.
- Caveats: EOD book = prior session refreshed after the open; today's heavy 0DTE OI burns off tonight (will reshape the SPY grid); gap risk on the June event prints; ETF-not-index book.

**Next-session 0DTE premium-selling setup (validated — `GO_PREMIUM_SELL_INTRADAY`, 0 points).** VIX 15.32 (LOW), HIGH-VIX-tercile backtest WR 0.609. Delta-neutral, intraday-only:
- **SPY:** sell premium, iron fly / short straddle centred **756.72, wings ≈ ±0.7%**, size 0.5×. Enter at/after the open once the gap resolves; stand aside if it gaps beyond the wings; **never carry overnight.**
- **QQQ:** centred **738.49, wings ≈ ±1.19%**, size 0.5× (weaker than SPY).
- Stand aside on a VIX spike or front-end backwardation. **Tail caveat: no vol shock in sample — the short-vol left tail is UNSAMPLED.** Not a guaranteed edge.

**Dealer swing setups (1–4 wk):** universe-wide vanna headwind (every name call-heavy, falling VIX bleeds dealer long-hedges — a slow ceiling on the rally). Cleanest dealer longs: **MSFT** (DEX +$14.1B #1), PLTR, ORCL (post-earnings flip), AVGO. Cleanest dealer short: **IWM** (GEX flipped negative 05-29, put_ratio 0.484). **NVDA vanna-squeeze watch:** put_ratio 0.397 + largest positive charm — if VIX < 14 next week the put-side could force dealer buying.

**Pin vs trend:** SPY pinned at its ZGL (no buffer) → mild **pin** bias near 757 until a catalyst; QQQ wider band. The June event wall (CPI/FOMC) is the trend catalyst that breaks any pin.

**Actionable for the coming week:**
1. **MSFT long, half size** — the one cleared conviction call. Add the QQQ-put-spread hedge into CPI/FOMC.
2. **Earnings vol:** HPE (SELL VOL Jun-1), PANW (SELL VOL Jun-2, half), AVGO (calendar Jun-3) — defined-risk only, half into the NFP-Jun-5 straddle.
3. **Hedge sleeve:** QQQ put spread + VIX call ladder + SMH put spread.

**LOW-tier / watch for daily confirmation:** ORCL (sell-vol into Jun-10/16), AAPL (only if insider-selling reverses), MU/MRVL (long if cum-flow turns decisively positive), PLTR (dealer long, watch for confluence).

**Deep-dive hand-off:** *Recommended deep dive: `/stock-deep-dive MSFT`* (top cleared name).

---

## 10. Watch-only — single signal, no confluence

Surfaced by one agent, failed the confluence gate — journaling only, **not** for entry: **ARM** (dealer long, no co-flag), **NOW / DOCN** (sector leaders, single-agent), **NTAP** (earnings resolved), **DELL** (earnings resolved, +42.6% — momentum exhausted), **SNDK** (sweep #2, no co-flag), **QCOM** (sweep bearish 3/4, single-agent), **QQQ** (multileg hedge vs dealer-long conflict), **INTC** (sweep bearish; dealer disqualified), **CRWD** (earnings Jun-3, sell-vol framing).
