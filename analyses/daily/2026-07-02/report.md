# Daily Market Analysis — 2026-07-02

> Next session: **Monday 2026-07-06** (Friday 07-03 closed, July-4 observed — 3-day weekend gap risk on everything below).

## Executive Summary

- **Regime + GEX state:** TRANSITIONAL — SPY 744.78 above both SMAs (20d 741.08 / 50d 737.43) on a green price day (S&P 357 adv / 145 dec), but flow breadth is decisively bearish (34.9% of tickers bullish, 2,182 vs 4,072). Both index books go into the long weekend **fully short gamma** (SPY −$821M, QQQ −$704M). VIX 16.15. VRP FAIR (−0.017, RV > IV — no vol edge either direction). Sector lean: money out of Tech/Consumer-Cyclical core, into Healthcare single names and Financials; semis/memory complex under heavy, opening-quality put pressure.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half` (P0.6 guard; 0/30 post-freeze HIGH/MED calls resolved).
- **Next-session GEX (SPY/QQQ):** SPY — FULLY_NEGATIVE (re-deepened 2 sessions, −$821M), ZGL null/unreliable (practical flip band 746–748), call wall 750 / put wall 740, −$527M magnet parked AT 745: trend-prone, moves away from 745 get chased. QQQ — FULLY_NEGATIVE (**fresh 1-day-old flip**, −$704M), no upside shelf until 730, put wall 700: the more dangerous book; fresh flips precede realized-vol expansion. Structure bias both: directional 0DTE / debit verticals with the first decisive break; premium selling only as wide defined-risk wings (SPY 740/750, QQQ 700/730) at the 0.5 scalar. Advisory, see §2.
- **Top swing build:** **NONE — second consecutive empty conviction book.** 27 candidates scored; only IBIT cleared the raw-3 drop floor (LOW, starter), and the bull/bear debate cut it to **skip / watch-only** (bear 0.75 ≥ bull 0.55). The debate layer swept the full top-5 board — the second consecutive 5/5 sweep (07-01 was the first).
- **Top LEAP candidate:** NONE — zero qualified. Today's long-dated tape is financing artifacts, macro hedges, and buy-writes (§4). Notably, nobody is paying IVR-100 vol at LEAP tenor in semis.
- **Biggest risk:** the **semis-capex correlation cluster** — KLAC/AMAT/INTC/SNDK/TSLA pairwise 0.72–0.93. Every short candidate on the board is substantially one trade. Defensive actions only today: IBIT → watchlist watch-only; **SNDK / BSX / JBL flagged as adverse-flow exit candidates** on standing conviction groups. No positions, no hedge sleeve (flat book).

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." SPY 744.78, above 20/50 SMA, −2.05% from 90d high, 30d change −1.95%. Trend label UPTREND but flow breadth bearish: only 34.9% of 6,254 optionable tickers carried bullish net flow. Guidance: half sizes, defined-risk, iron condors in range.

**Breadth cross-check (`fz`, advisory):** S&P constituents 357 advancers / 145 decliners, pct_green 71.0, median +1.38% — a broad green price day sitting on top of bearish options flow. No index-green/breadth-red divergence flag; the divergence today is price-vs-flow, not price-vs-breadth. Top mover GPC +12.9%, worst SNDK −14.1%.

**Per-index gamma (EOD 0–45d book):**

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 744.38 | null (unreliable; grid flip band 746–748) | −$821M | FULLY_NEGATIVE (2 sessions) | 750 (+$107M; 755/760 shelf behind) | 740 (−$87M; 735 behind) |
| QQQ | 712.56 | null (no positive territory until 729–730) | −$704M | FULLY_NEGATIVE (**fresh flip**, was +$141M 07-01) | 730 (weak, +$10M) | 700 (−$57M) |
| IWM | — | unreliable fit (322→null→155 whipsaw) | −$511M (label contradicts grid) | disqualified read | — | — |

**DTE volume share:** 0DTE 48.6% / weeklies 8.4% / monthlies 27.9% / LEAPs 4.0% → **RETAIL_DRIVEN** tape. Rotation and swing conviction uniformly downgraded one notch.

**VRP (`uw historical vrp`, SPY):** FAIR, −0.017 (IV30 13.6 vs RV30 15.3). Realized is outrunning implied — no premium-selling edge at the index; the contrarian fade lane aborted on this gate.

**Macro backdrop (FRED):** curve normal +0.35 (10Y 4.48 flat / 2Y 4.17 +12bp 30d); core CPI 2.96% / core PCE 3.41% YoY; unemployment 4.2%, June payrolls +57k (**printed today** — soft, read by the wraps as labor deceleration); USD strengthening 30d; fed funds 3.63.

**Forward event-risk calendar:** 07-03 market closed · jobless claims 07-09, 07-16 · **June CPI Tue 07-14 (Tier-1, T+7)** · PPI ~07-15/16 (Tier-1) · Q2 bank earnings kick off 07-14+ (GS 07-14; ASML/JNJ/MS/BLK 07-15; TSM/NFLX/ABT 07-16) · FOMC 07-28/29 (Tier-1) · PCE 07-30. Nothing Tier-1 inside T+5; the July-17 weekly expiry bundles CPI + PPI + bank kickoff + OPEX.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book (OI persists overnight) read as the *prior* for Monday 07-06's open. Prose-only, 0 rubric points, no backtested predictive claim (validation lives in `/weekly-analysis` §2). This map carries across **three nights** of overseas/headline risk plus weekend theta/charm decay.

**SPY — FULLY_NEGATIVE, re-deepened (−$189M 07-01 → −$821M 07-02), after only a 2-day positive reprieve (06-29/30).** ZGL null → `zgl_reliable=false`; the grid's sign-change band is 746–748 (+0.4% above spot). The book's dominant feature: **745 carries −$527M — 6× any other strike — sitting AT spot.** In short gamma that is an accelerant, not a pin: hedging pushes spot AWAY from 745 whichever way it breaks. Downside brakes at 740 then 735; upside, dealers flip progressively long through 746–748 and the 750/755/760 +GEX ladder becomes friction (~750 = realistic cap). Monday's 0DTE expected move (1.26%, ~735–754) prices *beyond* both walls — a wall-break is already in the straddle. Monday-expiry OI is real ($284M premium, balanced). Overhead put shelf: 12.5k 750P + 10k 755P at Jul-OPEX.
**Structure bias:** directional 0DTE / debit verticals with the first decisive break away from 745 (down-break targets 740→735; up-break through 748 targets 750). Any premium sold: defined-risk wings beyond 740/750 only.

**QQQ — FULLY_NEGATIVE, FRESH FLIP (positive 06-30 +$558M → +$141M 07-01 → −$704M today on a −1.8% spot decline).** No meaningful +GEX until 729–730 (+2.3%); overhead −GEX shelf at 713 (−$168M)/715/720 *accelerates* moves through it; soft cluster 710–712, then 700 (−$57M). Two regime flips inside 10 days = unstable dealer book, and fresh negative flips empirically precede realized-vol expansion. The 0DTE expected move (1.93%, ~699–726) reaches the 700 put wall and stops short of the weak 730 call wall — Monday likely realizes toward the wide end. Jul-17 OPEX bucket already heavily put-skewed ($185M P vs $72M C).
**Structure bias:** directional 0DTE / debit verticals with trend; the textbook long-straddle-on-the-flip setup if vol is bought anywhere. Premium selling only as wide ~700/730 condors at 0.5 scalar — never naked in a 1-day-old negative flip.

**Mandatory caveats:** EOD is a prior — fresh 0DTE OI re-computes ZGL/walls in the first 30–60 min, amplified here by 3 days of weekend theta/charm decay · 3-day-weekend gap risk (a gap through the walls in a fully-negative book gets amplified, not absorbed) · ETF book, not SPX/NDX (corroborated today by SPX −$1.35B put-heavy net flow) · 0–45 DTE proxy, not the isolated D+1 expiry · SPY's FULLY_NEGATIVE label vs its 747+ positive grid strikes = label-engine noise; read as "decisively short gamma AT spot."

### 2a. Next-session 0DTE premium-selling setup (validated stack — advisory, 0 points)

Rolling backtest (n=57): verdict **GO_PREMIUM_SELL_INTRADAY** both indices. **Net-of-cost first:** SPY mean +0.217%/day net (+0.317% gross, win 94.7%, worst −1.4%); QQQ +0.301%/day net (+0.401% gross, win 87.7%, worst −2.45%). PnL basis: % of underlying spot notional, GROSS minus 0.10% assumed round-trip cost — not premium-collected, not margin-relative; the gross win-rate overstates a negatively-skewed short-vol edge (Vilkov 2024).

| Index | Sell? | Vol state | Size scalar | Implied move | Expected range | Structure | Entry |
|---|---|---|---|---|---|---|---|
| SPY | yes | LOW (VIX 16.15) | **0.5** | 0.45% | 1.26% (short-gamma bracket) | wider iron condor, wings ≈ ±1.26% — or reduce/stand aside | at/after Monday's open once the gap resolves; hold to close; never overnight |
| QQQ | yes | LOW | **0.5** | 0.94% | 1.93% (short-gamma bracket) | wider condor, wings ≈ ±1.93%; QQQ = weaker proxy (no NDX book) | same |

VIX-LOW tercile is the thinnest edge bucket (SPY +0.127%/day gross vs +0.508% in HIGH) — the 0.5 scalar is doing real work. No stand-aside flag, but the left tail is UNSAMPLED (no vol-shock day in the validation window) and Monday opens across a 3-day gap in twin fresh-negative gamma books: respect the entry rule (gap must resolve first) strictly. Delta-neutral only — no directional tilt. Promotion bar: permanently advisory until a vol-shock enters the sample AND net expectancy clears a tail-aware bar.

## 2a. Swing Dealer Positioning (1–4 weeks)

**ZERO scored-eligible mechanized DEX flips today** — the +1 rubric line fires for nothing. All vanna-squeeze flags carry an UNVERIFIABLE VIX leg (no clean dated 2026 VIX series) and are not scored-eligible.

- **SPY:** public call-long book decaying fast — net DEX +26.2B (06-30) → +8.1B → +2.0B today (92% two-session decay). Stale verified flip 06-29 (neg→pos) already paid and decayed. **Watch item Monday: a negative print ≥ ~4.5B is a fresh mechanized flip** (prior positive run = 4 sessions). Vanna: call-heavy book → falling IV = dealer selling; anti-squeeze side. Swing bias NEUTRAL/short-lean, LOW-MODERATE.
- **QQQ:** the cleanest swing thesis on the board, honestly unscored — the book decisively flipped call-heavy→put-heavy across 07-01/07-02 (+36.2B → −0.4B → −20.5B; flip-day magnitude 1.08× trailing median) but missed the mechanized rule on a run-length technicality (the −0.36B zero-crossing broke the prior-sign run). Broad all-strike negative gamma 690–728, two GEX regime flips in 10 days. **Swing bias SHORT, MODERATE — unscored.** Charm note: put-heavy book gets a modest mechanical Monday-open bid from 3-day weekend decay — tactical timing only.
- **IWM:** DEX whipsaw at trivial magnitude + unreliable ZGL series → disqualified, NEUTRAL.
- **MU:** near-miss flip — first put-heavy print after 10 straight call-long sessions, but flip-day |−3.17B| = 0.209× median, below the 0.25× floor. −20% already realized; IVR 100 = vol-crush bounce risk. Short-lean LOW, unscored; the flip window is mechanically closed.
- **AMD:** call-long book bleeding (+9.6B → +1.7B, −82%) but not flipped. **Watch item Monday: any negative print ≥ ~0.25× median = flip candidate.**
- **AAPL:** monotonically IMPROVING call-long book (+1.4B → +14.2B, 10× in 4 sessions) with spot +9.3%. LONG lean, LOW-MODERATE, unscored; extreme one-sidedness (call DEX +14.9B vs put −0.7B) is itself an air-pocket risk.

## 2b. Sector Rotation

**Rotation regime call: `no_change`** — with an early, unconfirmed growth→value tilt. Confidence LOW-MEDIUM, uniformly downgraded on the 48.6%-0DTE retail tape. The GICS persistence tool is saturated (11/11 sectors INFLOW, 10 at 1.0) — differentiation is market-relative: Tech decelerating off its 06-30 peak ($5.98B → $3.08B) and regime-calc −$590M out; Consumer-Cyclical fading ($1.20B → $488M, −$154M out); Healthcare the only non-decelerating major; Financials accelerating (+$368M today). Growth is *splitting internally* (semis → software; IGV is the single biggest ETF inflow at +$86M), not exiting — hence no canonical regime call.

**ETF flow tape (advisory):**

| ETF | Net prem dir (5d) | Persistence | DP positioning | Options urgency | GICS agree | Leaders |
|---|---|---|---|---|---|---|
| IGV +$86.1M | inflow | BULLISH 5d | heavy repositioning (close-cross, wide-NBBO) | hedged upside (Sep/Nov calls + Jul/Aug put hedges) | agree (software leg) | MSFT, PLTR, SNOW, NET, FROG |
| KRE +$25.0M | inflow | BULLISH 5d | buy-tilted ($17.3M at/above ask) | **HIGH bullish institutional** — Aug 70C $35.2M bought vs 78/80C sold = ~$22M net-debit spread | **agree → best cross-confirmed lane on the board** | JPM, C, AXP |
| XLE +$14.3M | inflow | BULLISH 5d | at-mid neutral | matched long-dated collars, not directional | agree-weak | — |
| XBI −$12.1M | outflow | BEARISH 5d | buy-tilted DP vs bearish options = churn | Aug 155P stack + 168C sold = collar | **disagree → Healthcare downgraded watch-only** | — |
| EWT −$4.2M | outflow | BEARISH 5d | thin neutral | mixed (possible roll-up) | n/a | TSM link — Taiwan/semi de-risk coherent |
| XLI −$2.3M | outflow | BEARISH 5d | at-mid | **decisive capped-risk bearish: Sep 165/155 put spread, 50k×, bought at ask** | **disagree → see below** | — |

**XLI investigation — both sides are right; it's an intra-sector split.** The GICS Industrials +$248M inflow is concentrated in defense/space (SPCX +$41.4M alone ≈ 1/6 of the sector's day, plus EOSE/BA/RTX/NOC); the cap-weighted cyclical core (GE/CAT/UNP/HON) is being explicitly hedged with the 50k Sep 165/155 put spread. Do NOT read Industrials inflow as risk-on cyclical rotation.

**Swing-book implication:** long regional-bank leaders (KRE vehicle; JPM/C/AXP) + starter Healthcare singles (DVA/NVO/UTHR, watch-only until XLV/XBI confirm); avoid/short the semis-Taiwan complex and XLI cyclical core — all half-conviction pending Monday. *(None of this survived the quant floor today — see §7.)*

---

## 3. Swing Setups (1–6 weeks)

> **The conviction book is EMPTY — second consecutive session.** 27 candidates scored against the frozen rubric; one name (IBIT, raw 3, LOW) cleared the drop floor and the debate gate cut it to watch-only. Everything below is journaling, not trade entry. The single biggest driver: **30-day cumulative premium flow contradicted nearly every Phase 1 thesis** — the mechanical flow_conflict (−3) fired nine times (SPCX −$217M, AAPL −$137M, MSFT −$573M, NVDA −$512M vs LONG theses; SNDK +$909M vs SHORT).

### 3a. Long swings (regime-aligned) — none sized

| Ticker | Score | Thesis (journal) | Structure ref | Invalidation (C34) | Sizing |
|---|---|---|---|---|---|
| IBIT | 3 (LOW) | The only full flow-structure coherence on the board: Nov-20 40/46 bull vertical (~$8M debit, 2.7:1, breakeven +19%) + 30d flow +$306M aligned + 06-25 capitulation print (P/C 2.57→0.50) + two-week 33.3–36.5 base. Debate killed sizing: options stack <7% of ONE month's record $4.5B ETF outflow; unvalidated signal class; long edge is uptrend-only. | Nov-20 40/46 call vertical (defined risk) | Loses the 33.29 base low; ETF outflows re-accelerate with P/C re-inflating | **skip — watch-only, on watchlist** |
| KRE | 1 (DROP) | $21.9M Aug 70/78/80 call ratio ladder at IV pctile 5.3 into dated catalysts (bank earnings 07-14+, Bowman dereg, +0.35 curve) — but the confluence collapses to ONE whale print counted by three agents, 30d flow dead-flat (+$4.8M), and the ladder's author pre-sold the upside above 78. | Aug-21 70/78/80 ratio ladder (whale's own) | Aug call OI unwinds; or one bad regional print (CRE/deposit costs) 07-14+ | skip |
| WMT | 1 (DROP) | Accumulation-hunter's #1: mega-tier DP 0.925/$558M defending **111.84** ($590M shelf), put protection *lifted* ($5M closed), BUILDING 5/5 — but the options tape never confirmed (30d −$2.7M) and the conviction matrix failed its floor (37.6 < 50). | — | Close below 108.80 (secondary DP block) | skip (watch-only) |
| SPCX | −1 (DROP) | Loudest accumulation story, worst flow contradiction: +833k OI 5/5 and DP shelf 158–162 vs 30d flow **−$217M** (3.6× union median → full −3). The bullish paper is penny deep-OTM lotto (Jul10 330C, +104% OTM); the institutional size is in Sep 150P/Oct 100P ($38.6M+). | — | — (contradicted) | skip |
| AAPL / MSFT / NFLX / NVDA / MSTR | −1…−3 | All flow_conflict longs: DP/OI accumulation stacks (AAPL mega 0.95, closing-cross contaminated) against outright negative 30d premium books (AAPL −$137M, MSFT −$573M, NFLX −$81M + collar, NVDA −$512M, MSTR −$583M). The NVDA row is the 2026-05-08 lesson firing as designed. | — | — | skip |

### 3b. Short / fade swings (defined risk only) — none sized

| Ticker | Score | Thesis (journal) | Structure ref | Invalidation | Sizing |
|---|---|---|---|---|---|
| INTC | 2 (DROP) | Cleanest short residue on the board: multi-day multi-expiry opening put build (Sep18 90P +3,011 at 95% ask; Nov20 80P) that **front-ran** the −9% break, 30d flow −$402M aligned. Killed on: peak-vol expression (IVR 100 through the 07-23 earnings crush), 4/4 beat streak + HSBC $200 PT, insurance-scale flow (~7bps of cap), "no short alpha-sizing" audit rule. **Overhang flag stands** — revisit only as a defined-risk earnings structure if it re-scores. | Sep 90P (reference; peak-vol warning) | Closes above 130; sweep tape flips call-dominant | skip |
| SNDK | −2 (DROP) | Biggest persistence story of the week (5/5 sessions, $1.87B sweeps, put-side ΔOI +224k/5d from 1750 down to 935) — but sweep persistence is 0-point, and the mechanical flow switch reads the 30d book +$909M AGAINST the short (Phase 1 calls it attribution artifact; the rule doesn't narrate). Put buyers paying IVR-100 with VRP −0.11 = crush risk even if right. **Adverse-flow EXIT candidate on the 06-30 conviction group.** | — | Net premium flips ≥ +$30M Monday; Jul10 put OI unwinds | skip |
| KLAC | −1 (DROP) | **The actionable C19 advisory short:** Tier-1 OPENING_PUT_PRIME (Jul17 315P, $1.58M, size/OI 5.0, delta −0.95 = synthetic short) ∧ mega DP buy-ratio 0.00 ($20.8M all sell) — the strongest bearish co-confirmation configuration. z −0.33 (whale early, not chasing). C19 = 0 rubric points pending cross-regime validation. | Jul17 315P (whale's own) | P/C z > +1 with flow flipping bullish | skip (C19 advisory) |
| TSLA | 1 (DROP) | 5/5 bearish sweeps ($5.86B) + insider MSPR −45 + PE 414 — but record Q2 deliveries printed today (480k vs 397k), the tails are conceded weekend hedges that decay Monday, and the 90d book is +$624M opposite. Bear's own path: revisit as a defined-risk earnings-window structure week of 07-15 (the margin question). | — | Reclaims pre-print level within ~3 sessions | skip |
| WULF | 2 (DROP) | Institutional 2-day roll-down (24P → Jul17 20/18 vertical, 65k×) with rotten fundamentals (miss streak, −611% margin, negative book) — but entry chases −21.5%/6 sessions at doubled IV, roll-day aggregate flow was net *bullish*, 16/16 unanimous-buy book + Citi $36, HPC PR gap risk, dark squeeze gauge. Deep-dive wrinkle: today's top OI changes are CALL-heavy (Jul10/17 25C +30k) — the tape is two-sided. | Jul-17 20/18 put vertical (whale's own) | Reclaims 24; HPC hosting PR | skip |
| XLI | 1 (DROP) | Real 50k Sep 165/155 put spread on the cyclical core, but hedge-shaped (exact equal size, no single-leg whale) and the 30d book reads bullish. Index-ETF short = the audit's 0-for-4 stratum. | Sep 165/155 vertical (mirror) | Sep 165P block unwinds | skip |
| QQQ | −3 (DROP) | The unscored dealer thesis (§2a): put-heavy DEX flip at 1.08× median + fresh FULLY_NEGATIVE gamma + two regime flips in 10d. Flow switch fired against it (+$86M 30d) and index shorts are the audit's worst stratum. Belongs in the 0DTE advisory, not the swing book. | — | net DEX positive ≥3 sessions | skip |
| GS / GLW / AMAT | −1…−3 | GS: C19 Tier-1 put vs call-crowded tape, but DP is 0.833 BUY — contradicted. GLW: cheap-put-skew observation (VRP −0.16), 30d book +$77M against. AMAT: contrarian **continuation-down warning** (z +3.29 RISING, 0.79→1.72 in 3 sessions while price 723→603) — informed flow pressing; stands as a BLOCK on semicap dip-buys, not a scored short. | — | AMAT: CONTANGO restored + z < +1 + flow bullish | skip |

**Near-term sweep ledger (informational, 0 points):** persistence-confirmed — SNDK 5/5 (put-side, $1.87B), SPCX 5/5 (bullish barbell, $1.21B), TSLA 5/5 (bearish tails), SMH 4/5 (monolithic Jul10/17 put build +431k), INTC 4/5, MSTR 3/5 (window bearish, **flipped bullish today**: Jul10 101–107C ΔOI 15–40×). Index sweeps (SPY/QQQ/IWM/SPX) demoted as hedge flow — cum-flow misaligned or churn. Single-day: KRE Aug 70C spread ($35M), XLI Sep put spread, IBIT Nov 40/46, VIX Jul22 35C tail buy (44k, weekend hedge), PEP Sep call overwriting ($31M bid-side). Mixed/disqualified: MU ($6.9B — biggest premium, window-mixed), NVDA (0DTE churn), AMD, META, AAPL.

## 4. LEAP Builds (6–24 months)

**Zero qualified.** LEAP share of tape 4.0%. Every DTE>180 survivor failed the required cumulative-accretion gate (G4) or the scenario gate (G8):

- **NFLX** (5-6/9 gates) — Mar-27 100C +10.8k genuinely ask-side (11,774 ask vs 297 bid) and recurring across 5 sessions, but the LEAP book is two-sided (Jan-27 P65 +54.1k, Nov-26 P60 +25.7k) and premium accretion is wrong-direction on both windows (30d −$81M / 90d −$183M). Dip-buying + collar structuring, not conviction. Re-test: 30d flow flips positive while the Jan-27 C90/C100 build continues. Merger-arb check clean.
- **TLT** (4/9) — most active long-dated book on the tape, but it's a structure: Jan-28 calls +121k built WHILE Jan-28 P55–P83 +120k built. Two-sided rate risk-reversal + covered-call overlay (G8 COVERED_CALL reject).
- **XLF** (4/9) — buy-write program: heavy DP buying (3.62 ratio) + Jan-27 C55 crossed mid + COVERED_CALL matrix. Yield harvvesting, not upside conviction.
- **NKE** (3/9) — Mar-27 C55 ask-side build recurring (the closest thing to a fresh LEAP thesis) but 90d flow −$52M BEARISH and near-dated put walls building concurrently. First name to re-test post-earnings.
- **EOSE** — P1.5 financing-artifact disqualifier: Jan-28 P10 +30k deep-ITM at the bid = borrow synthetic (Muravyev-Pearson-Pollet class).
- **Semis: no DTE>180 name surfaced at all** — nobody pays IVR-100 vol at LEAP tenor; the smart long-dated money is standing aside from the complex.

## 5. Volatility Surface

**Substrate caveats:** every raw term-structure label printed BACKWARDATION with null kink (0DTE contamination — audit P1.3); all reads below are hygiene-filtered (0DTE dropped, <15-contract tenors dropped). IV-percentile substrate is n=57 — all percentile-100 quotes PROVISIONAL. A fake 07-17 "kink" (unweighted-wing artifact) appears simultaneously on AMAT/ARM/ASML — do not trade it.

- **KINKED (event-aligned, → earnings-scout):** T 07-31 (earnings + FOMC; front panic resolved 1.43→1.08, what remains is pure event premium), GEV 07-24/31 (VRP +0.11 but institutions buying protection at complacent skew), TXN 07-24, INTC 07-24, FTNT step 07-24→07-31 (**richest VRP +0.28**), TSM — no kink at its own earnings expiry (front lifted by the flow wave, f/b 1.29 still >1.10: NOT a fade; three dated events pending).
- **The one clean calendar: VZ** — f/b 1.20 steepest in set, front ratio FALLING 1.17→1.03 (panic resolving = window open). **Sell Jul-17 42P (~0.34 IV) / buy Sep-18 (~0.29)**; 180d put skew 1.50 + Jan-27 put accumulation supports the long leg. Invalidation: ratio re-inflates >1.10 or VZ earnings confirmed before 07-17. (KLAC f/b 1.11 headline is an FDX-defect analog — no valid tenor 15–50d; DO NOT trade.)
- **Skew dislocations:** **KRE** top actionable (IV pctile 5.3, contango, $48.9M call premium in Aug-21 alone vs 3.8k puts — whale-sized upside in cheap vol ahead of three dated catalysts); GLW complacent-inverted skew against VRP −0.16 and bearish tape (put side is the cheap side; DO-NOT-SELL premium despite IVR 100); TSM complacent at 30d AND 180d into earnings (upside tail free; express via Sep 440/480 call spreads, never outright OTM calls — Boyer-Vorkink lottery advisory); INTC puts underpriced relative to calls vs −$82.5M net flow.
- **VRP dispersion (the story, given index FAIR):** sells that clear — FTNT +0.28, BE +0.27, STX +0.18, MRNA +0.17, GEV +0.11, NBIS +0.11 (all earnings-embedded; condors must expire pre-event or price it). **Do NOT sell:** ARM −0.17, GLW −0.16, SNDK −0.11, KLAC −0.06, AMAT −0.04, AMD −0.04 — the semicap/memory IVR-100 complex is IV *chasing* realized (SNDK the extreme: pctile 100 with RV 1.35 > IV 1.24). Screener-driven premium sales there are the classic trap.
- **Telecom IVR-100 answer:** two opposite whales — T = long-dated CALL accumulation (Jan-27 $3.0M), VZ = long-dated PUT accumulation (skew 1.50). Not one sector trade.

**Earnings verdict board (earnings-scout; all SELL VOL capped half-size, defined-risk, VRP FAIR regime):** JNJ 07-15 **SELL VOL top pick** (kink ON 07-17: 37.9% vs 28/30; TAIL_HEDGING back skew 1.106; iron condor 255P/272.5C, enter week of 07-13) · ABT 07-16 SELL VOL (most stretched back skew 1.177) · PEP 07-09 SELL VOL half (kink ON 07-10 at 40.4%; **warning: PCR 0.077 vs premium-weighted flow −$30.9M** — sized money short calls into the print; wider put wing) · NFLX 07-16 SELL VOL half (largest kink: 61.3% vs 35.2%; back skew complacent → half) · ASML 07-15 SELL VOL half weakest (07-17/07-24 calendar; semicap complex may keep the base bid) · SKIPs: TSM (no event kink — vol is flow-driven), GS (CPI + earnings share the expiry, unisolatable), AEHR (classic short-vol blowup profile), PENG, MS/BLK/CTAS (CPI-week bundling). Calendar is thin until 07-14; JNJ+ABT = one healthcare-vol position for correlation purposes.

## 6. Risk & Correlation

**Macro headline:** curve normal +0.35, payrolls +57k (soft, printed today), USD firming, VIX 16.15. Forward: CPI 07-14 (T+7), PPI 07-15/16, bank earnings 07-14+, FOMC 07-28/29. Nothing Tier-1 ≤T+5. Breadth: 357/145 advancers, pct_green 71.0 — green day, no distribution divergence.

**Correlation clusters (30d, mechanical):**
- **`semis_capex_cluster` FIRES (≥0.70):** KLAC/AMAT/INTC/SNDK/TSLA — pairwise 0.72–0.93 (KLAC/AMAT 0.929). Kept member: INTC (highest raw score). TSLA takes the −1 cluster tier. **Every short candidate on today's board is substantially one trade.**
- Soft watch 0.60–0.70: INTC/SNDK 0.681, TSLA/AMAT 0.646, INTC/TSLA 0.632.
- BTC-beta prior NOT confirmed at 30d: IBIT shows no pair ≥0.55; no discretionary upgrade (mechanical rule).

**Gate outcomes (top-5):** regime/VRP/panic/sector — no-op board-wide (front-end ratios SPY 0.526 / QQQ 0.694, deep contango — no panic; all sectors net-inflow — no adverse rotation). Fundamentals: INTC/WULF/TSLA CAUTION −1; IBIT/KRE NA (ETFs, never penalized). Event-risk: no-op (nothing Tier-1 ≤T+5; all references defined-risk). **Debate: fired on ALL FIVE names — bear residual ≥ bull residual across the board (second consecutive 5/5 sweep; 07-01 was the first).** rubric_regime: capped-half ACTIVE (moot — nothing sized above starter pre-gate).

**Fundamentals verdicts:** INTC CAUTION (4/4 beat streak, HSBC $200 same-day, earnings 07-23 inside horizon) · WULF CAUTION (legs confirm the short but 16/16 unanimous-buy book, Citi $36, HPC PR gap, dark squeeze gauge) · TSLA CAUTION (record Q2 deliveries 480,126 printed today; insider MSPR −45.35 and EPS −39% still confirm) · IBIT NA (record $4.5B June ETF outflows carried as key_risk) · KRE NA (corroborating dated catalyst stack). Zero VETOs.

**Adverse-flow exit candidates (standing conviction groups):** **SNDK** (06-30 group: −$152.7M day flow, IVR 100, 2.1× volume — hard flow exit; clean on the fz fundamentals tripwire) · **BSX** (06-22 group: P/C 3.79, IVR 98.3, $45M DP print — accumulation-hunter confirms *hedged distribution*, mega tier 0.362 sell-dominant) · **JBL** (W24 group: P/C 5.11). Decay watch: DELL (IVR 93, mild bearish). Favorable: NFLX (call-heavy OI build). PEP: 3.3× volume, direction unclear — watch into the 07-09 print.

**Hedge sleeve: NONE.** The book is flat — a flat book is its own hedge. Advisory: weekend front-end is optically cheap but VRP is FAIR, so a standalone long-put punt is not positive-expectancy, and index-ETF put buying is the audit's 0-for-4 pattern. If the desk carries discretionary long exposure outside this book: 2–3 week SPY 3–5% OTM put vertical bought Monday post-gap, sized to that external delta only.

**Risk summary:** Second consecutive empty conviction book: 27 candidates, one above the drop floor, and the debate gate cut it from starter to skip — the second consecutive full debate sweep. Every structural gate corroborates standing down: TRANSITIONAL regime with thin bullish flow breadth, FAIR VRP offering no vol edge in either direction, and a five-name semis-capex correlation cluster that reduces the entire short side of the board to one already-skipped bet. The only mechanical actions today are defensive: IBIT written to the watchlist as watch-only for adverse-flow tracking, and SNDK/BSX/JBL tagged as exit candidates on hard adverse-flow reversals against carried theses. No positions, no hedge; re-engage when either the regime resolves or a candidate survives the debate.

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**None.** No ticker reached MEDIUM (≥7) or HIGH (≥9). Highest raw score on the board: IBIT at 3 (LOW). The Step 3a load-bearing gate was never reached.

**Expectancy lens `[advisory — expectancy is not yet a live sizing axis]`:** most recent `/calibration-audit` (2026-06-27): tier calibration remains INVERTED — HIGH realized 0.143 (3rd consecutive audit; the HIGH book was 4 index-ETF shorts 0-for-4 + 2 faded longs), long edge is UPTREND-ONLY (matched-basis +18.7pp in uptrend / −21.7pp outside), short book carries negative selection alpha, and the out-of-regime half-cap measured PROTECTIVE (−16.7pp avoided, n=10). No per-tier expectancy/payoff table is computable for the current freeze era (0/30 post-freeze HIGH/MED calls resolved) — which is precisely why the P0.6 cap stays on.

**Top-5 calibration rows (per the empty-book protocol — documented, not traded):**

| Ticker | Dir | Raw | Class | WR (n, source) | mkt-excess | Fund. | Debate (bull/bear) | Final |
|---|---|---|---|---|---|---|---|---|
| IBIT | long | 3 | multileg_directional | — (NA substrate) | — | NA | 0.55 / **0.75** | skip → **watchlist watch-only** |
| INTC | short | 2 | bearish_flow | 0.529 (138, clean) | +13.8pp | CAUTION | 0.55 / **0.85** | skip (overhang flag) |
| WULF | short | 2 | multileg_directional | — (NA substrate) | — | CAUTION | 0.65 / **0.75** | skip |
| TSLA | short | 1 | bearish_flow | 0.529 (138, clean) | +13.8pp | CAUTION | 0.55 / **0.85** | skip (revisit 07-15 wk) |
| KRE | long | 1 | multileg_directional | — (NA substrate) | — | NA | 0.65 / **0.85** | skip |

Class notes: bullish_flow failed its emission floor outright (WR 0.478 < 0.50, excess −8.0pp — beta-negative); dark_pool_accumulation returned an empty backtest class (NA substrate) — all five accumulation names sized on tier-default; high_iv_rank quoted at the 0.80 ceiling (raw 0.9207, n=164) as **calibration-only** — it is a BH-surviving *negative-edge* class and never drives size.

**Deep-dive hand-off:** skipped — no-edge day (no HIGH-tier names).

<details><summary><b>Conviction scoring rubric (frozen 2026-06-12) — embedded verbatim for audit</b></summary>

```
Daily conviction score = Σ:
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna-squeeze setup in trade direction — the trigger must be a verified SIGN CHANGE, not a level: sign(net_dex) on the latest session opposite to ≥3 consecutive prior sessions, read from dated `uw options-structure dex --date` calls (≥4 to verify the prior-session sign run; ~11 for the trailing-median floor), with |net_dex| on the flip day ≥ 0.25× the trailing-10-session median |net_dex|; the evidence string must cite both dated values. Vanna disjunct additionally requires a dated VIX source (Yahoo chart API ^VIX) for the falling-VIX leg — no out-of-band VIX fills.   # DEMOTED +3→+1 and MECHANIZED 2026-06-12 audit P0.4
  +3  3+ aligned signals in accumulation-hunter (DP + OI + uw oi smart-positioning, uw dark-pool block-stratified institutional-tier confirmed) — CONJUNCTION (2026-05-25 register C11): full +3 only when cum_premium_flow_30d confirms (sign aligned with thesis AND |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1. A sub-$50M flow that halves this line does not separately qualify for the +1 cum_flow line.   # was +2; promoted 2026-05-15 audit P1.2 (LOAD-BEARING)
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)                       # was +2; reduced 2026-05-09
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL ONLY (2026-05-23 audit P1.1): award +1 only when dominant_signal_class == leap_directional; in all non-LEAP contexts contribution is 0.
  +1  uw historical cumulative-premium-flow shows net directional accretion in trade direction (30d window) — INTENT-SCREENED (2026-06-06 audit P1.4): (a) no C28 distribution_flag on the name, AND (b) on dividend payers inside an ex-div window, the accreting prints are NOT deep-ITM sub-parity calls. Screen failed or unevaluated on a flagged name → 0.   # DEMOTED +3→+1 2026-06-06 audit P1.4
  # +2 line for uw insights signal-confluence ≥4 REMOVED 2026-06-12 audit P0.2
  # +1 line for uw hot-chains sweep-persistence top-5 REMOVED 2026-05-23 audit P0.3
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector — CONDITIONAL (2026-05-23 audit P1.5): (a) sector persistence_score ≥ 0.6 AND (b) cum_premium_flow_30d direction aligned AND (c) |cum_flow_30d| ≥ $50M. Default 0.
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)   # was +1; promoted 2026-05-09
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising uw historical pc-ratio-zscore (VRP positive)   # MECHANISM (2026-06-12 P1.5): informed-flow CONTINUATION penalty (Pan-Poteshman 2006; Ge-Lin-Pearson 2016), routed through the C13 router
  -3  flow_conflict — mechanical when uw historical cumulative-premium-flow 30d direction is *clearly opposite* dominant_signal_class (signed-sum sign flip + magnitude > today's union-median |cum_flow_30d|, or explicit OPPOSITE label)   # 2026-05-15 audit P0; mutually exclusive with flow_conflict_lite
  -1  flow_conflict_lite — when the 30d cum_premium_flow read is MIXED (signed sum near zero, or aligned but bottom-quartile magnitude in today's union)   # mutually exclusive with flow_conflict
  # The two lines below are risk-monitor TIER gates applied in Step 2d, NOT score_components (0 points, never in Σ):
  -1  [TIER GATE, 2d] risk-monitor flags in correlation cluster (pairwise corr ≥ 0.70) — −1 TIER
  -3  [TIER GATE, 2d] uw risk market-regime conflicts with trade direction — −1 TIER (regime gate)
Tiers: ≥9 HIGH (full, subject to Step 3a 3-of-4 load-bearing gate + Step 5 win-rate gate) / 7–8 MEDIUM (half) / 3–6 LOW (starter/watch) / ≤2 drop.
Rubric version: 2026-06-12 (FROZEN). Out-of-regime guard (P0.6): all sizes capped at half until a /calibration-audit records ≥30 resolved post-2026-06-12 calls and re-validates the tiers.
```

</details>

## 8. Watch-only — single signal, no confluence

Journaling only, NOT trade entry:

- **WMT** (accumulation-hunter only) — best sub-gate accumulation read; DP defense at 111.84; watch for options-tape confirmation.
- **MCD / MA** (accumulation near-misses) — conviction-matrix 46.9 / 42.7 vs the 50 floor; MCD closest in the fleet, re-test next session.
- **JPM / C / AXP** (sector-rotation leaders) — JPM +$14.4M, P/C 0.33; the sector +1 failed only the $50M magnitude gate.
- **MSTR** (sweep-tracker flip-watch) — 3/5 bearish window flipped bullish today (Jul10 101–107C, ΔOI 15–40×); crypto complex confirms (IBIT/BTDR/MARA); but 30d book −$583M bearish and bullish_flow class below its WR floor.
- **NVDA** (multileg only) — $17M Jul-10 200/205 bull vertical explicitly carving NVDA out of the semis short basket; single-day, flow-conflicted.
- **WULF / TSLA / GS / GLW** — single-agent shorts, see §3b.
- **JNJ / ABT / PEP / ASML / NFLX-vol** (earnings-scout only) and **VZ / FTNT / MRNA / BE / STX** (vol-surface only) — the §5 vol lane; earnings_vol and high_iv_rank are 0-point/negative-edge classes.
- **BSX** — watchlist alert resolved: NOT accumulation; hedged institutional distribution (mega tier 0.362 sell-dominant, put ask 40.4k vs call 7.7k). Exit candidate, §6.
- **fz advisory lanes:** squeeze candidates (floored): ASTS (SF 24.1%), APLD (28.8%), AAP (20.8%, DTC 6.7), ACHC, BEAM (30.2%, DTC 13.0), AI (33.3%), ASAN (35.0%). RS/new-high: MRNA (+10%), VRTX, ILMN, CB, ALL, FROG, OSCR, DVA, NAVN, VOYA, PTGX, AXS. None earned rubric points (C15–C18 advisory).
- **Single-leg whale (C19 advisory, 0 points):** Tier-1 OPENING_PUT_PRIME — **KLAC** Jul17 315P ($1.58M, size/OI 5.0; co-flag FIRED with DP all-sell) and **GS** Jul24 1060P ($501k; co-flag did NOT fire, DP is buy-side). Tier-2 context: SNDK Aug21 1850P $6.74M floor print. MU's largest put print was a Tier-4 CLOSING_ANTISIGNAL (size/OI 0.40) — softens the MU bear read. Call side reported as CALL_UNVALIDATED (non-bull regime).

---

*Generated by /daily-analysis · rubric 2026-06-12 (frozen) · envelope: `analyses/daily/2026-07-02/decision.json` · watchlist group `conviction_2026-07-02` = [IBIT] (watch-only)*
