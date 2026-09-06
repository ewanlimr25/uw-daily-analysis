# Daily Market Analysis — 2026-07-06

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL (bullish flow on only 37.4% of tickers) with SPY still in UPTREND at 751.28, above the 20-SMA (740.79) and 50-SMA (738.23), −1.2% from the 90d high. SPY flipped back to POSITIVE gamma but on a knife-edge (spot 751.52 vs ZGL 751.06 — 4th regime flip in 15 sessions); QQQ sits in NEGATIVE gamma on a thin book. VIX 15.57. Breadth negative-divergent (220 adv / 280 dec on a flat-green tape). Sector lean: Tech/Cyclicals/Financials in, defensives (Healthcare/Staples/Utilities) unwinding on the DP layer.
- **Rubric regime status:** OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half.
- **Next-session GEX (SPY/QQQ):** SPY: long-gamma (fresh flip) · ZGL 751.06 · call wall 752 / put wall 740 · knife-edge pin — defined-risk fly over naked straddle. QQQ: short-gamma · ZGL 749.53 (3.7% above spot, near tolerance edge) · call wall 730 / put wall 710 · debit verticals / long premium over selling. Advisory, see §2.
- **Top swing build:** **NONE.** All 18 Phase-1 union names scored ≤1 against a drop floor of 3 — the fourth and deepest empty-book day (top raw on 2026-07-01 was 4; today it is 1). Zero names cleared the two-agent confluence gate. Top-raw SNDK long was killed by fundamentals CAUTION (insider MSPR −100, "smart money cashing out") + debate (bear 0.65 > bull 0.40) + a $23.8M Tier-1 opening put against it.
- **Top LEAP candidate:** TEVA Jan-2027 33/36C — the only name to pass the LEAP gate stack (8-of-9), with 6.3x fresh ask-side OI build and 3.6:1 DP buy skew. Scored **0** under the frozen rubric (conviction-matrix 45.8 < 70 leap gate; flow_conflict_lite on absolute magnitude). Watch-only, not sized.
- **Biggest risk:** memory-semis cluster (SNDK/MU pairwise corr **0.832** — treat as one position) showing distribution signatures under bullish headlines; both are tagged **exit candidates on the carried book**. CPI lands 2026-07-14 (T+6) with an institutional index-put hedge complex (SPXW/SPY/QQQ/IWM, 5-of-5-day OI-confirmed put persistence) already built around it. Sanctioned expression: token long convexity only (≤0.5% NAV — SPY Aug-21 745/720 put vertical or VIX Aug 17/20/25 call ladder).

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — mixed signals, reduce position size, wait for clarity.** SPY trend is still UPTREND (above both SMAs), but market breadth is bearish-flow-dominated: 3,917 tickers net-bearish vs 2,339 net-bullish (37.4% bullish). Guidance from the tool: half sizes, defined-risk structures. The `fz` breadth cross-check (advisory) corroborates: 220 advancers / 280 decliners (`pct_green` 43.7) with a +0.02% average change — **a green-index/negative-breadth divergence, a mild distribution tell** (median S&P name −0.25% on the day).

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 751.52 | 751.06 (reliable, 0.06% from spot) | +$1.41B | POSITIVE (fresh flip, 4th in 15 sessions) | 752 | 740 |
| QQQ | 723.02 | 749.53 (3.67% above spot — near tolerance edge) | +$82.8M (thin) | NEGATIVE | 730 | 710 |
| IWM | — | unreliable (ZGL estimates swung 140→322 across the window; thin per-strike OI) | noise-scale | unstable | — | — |

- `uw options-flow dte-volume-share`: **BALANCED** — 0DTE 39.2%, weeklies 25.2%, monthlies 19.0%, LEAPs 4.3%. Neither retail-dominated nor institutionally skewed; no regime reweight.
- `uw historical vrp` (SPY): **FAIR / negative** — IV30 13.3% vs realized 15.2% (vrp −0.019). Realized is running *above* implied: no premium-selling edge at the index level; short-vol structures carry a −1 VRP gate today.
- **Macro backdrop** (FRED): curve normal (+0.35 10s2s), core CPI 2.96% / core PCE 3.41% (sticky), unemployment 4.2% with +57k payrolls (soft), 10Y 4.49% flat over 30d, USD strengthening, Fed funds 3.63%.
- **Forward event risk:** FOMC **minutes** 7/8 (medium) · jobless claims 7/9 · **CPI 7/14 (high, T+6)** · PPI 7/15 · retail sales 7/16 · monthly OPEX 7/17 · Q2 bank-earnings kickoff ~7/14–17 (GS 7/14, MS/BLK/ASML/JNJ 7/15, ABT/NFLX/TSM 7/16) · **FOMC decision 7/29 (high, no SEP)**.

**Desk read:** a flat tape hiding a heavily two-sided session — record IV-rank-100 breadth across mega-cap tech (MSFT, AMD, LRCX, AMAT, ASML, ARM, WDC, SNDK, STX — mostly earnings-season vol bid, see §5), 276 closing-anti-signal prints on the single-leg tape (de-risking), and a persistent institutional index-put book into CPI. Institutions are hedging and rotating, not initiating.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book (OI persists overnight) read forward as the *prior* for 2026-07-07's open. Prose-only, contributes 0 points to the conviction rubric, no backtested predictive claim (validation lives in `/weekly-analysis` §2).

**SPY — POSITIVE (long-gamma), knife-edge.** Spot 751.52 sits 0.46 above the ZGL at 751.06 with the call wall at 752 just 0.06% overhead and the put wall at 740 (−1.53%). Dealers are nominally long gamma (mean-revert/pin bias) but the margin is razor-thin and this book has whipsawed regimes 4 times in 15 sessions (FULLY_NEGATIVE as recently as 07-02). A decisive push through ~751 flips the prior back negative intraday. **Structure bias:** iron fly / butterfly centered 751–752, *defined-risk* (butterfly over naked short straddle), small size — this is not a settled long-gamma regime.

**QQQ — NEGATIVE (short-gamma), thin book.** Spot 723.02 sits well below the 749.53 ZGL (3.67% away — treat with reduced confidence near the 5% tolerance edge); total GEX +$83M is an order of magnitude thinner than SPY's, so pinning power is weak. Call wall 730 (+0.97%) is a soft cap; put wall 710 (−1.80%) the nearer downside pivot. **Structure bias:** debit verticals / long premium / directional 0DTE over selling; fade pokes above 730 only lightly.

**Mandatory caveats:** EOD is a prior, not a target — fresh 0DTE OI re-computes ZGL/walls in the first 30–60 min. Both books are fresh one-session flips inside a 3-week whipsaw — do not lean hard on either the SPY pin or the QQQ trend read. Gap risk: FOMC minutes 7/8 (one session out), CPI 7/14. This is the 0–45 DTE ETF book (uw-pp cannot isolate the D+1 expiry; ETF ≠ SPX/NDX index book). Cross-current: today's heavy index put premium (SPX −$163M, SPXW −$80M, QQQ −$79M) is an independent directional-hedge flow worth respecting alongside this map.

### 2a. Next-session 0DTE premium-selling setup (validated stack — advisory, 0 points)

`scripts/zerodte_setup.py` verdict: **GO_PREMIUM_SELL_INTRADAY** both indices (n=58 rolling).

| | SPY | QQQ |
|---|---|---|
| sell_premium | yes | yes |
| vol_state / VIX | LOW / 15.57 | LOW / 15.57 |
| implied move | 0.59% | 1.28% |
| expected range (GEX-conditioned) | 0.78% | 1.32% |
| size_scalar | 0.5 | **0.25** |
| structure | iron fly / short straddle centered 751.74, wings ≈ ±0.78% | iron fly centered 723.01, wings ≈ ±1.32% |
| entry rule | at/after open once gap resolves; hold to close; never overnight | same |
| caution | none | **front-end backwardation (0DTE IV 1.31× VIX) — event/gap risk, half size** |

PnL basis (P1.8): backtest `mean_pnl_open_net_pct` **SPY +0.211%/day, QQQ +0.300%/day** net of an assumed 0.10% round-trip cost (gross 0.311%/0.400%) — **percent of underlying spot notional, GROSS basis, not premium-collected and not margin-relative**; win rates (94.8%/87.9%) overstate a negatively-skewed short-vol edge. Overnight variant is negative. Vol-shock tail is UNSAMPLED — this lane is permanently advisory pending a tail-aware net-expectancy bar. Note the tension: LOW vol_state means the thinnest conditional edge tercile (mean_pnl LOW 0.125% vs HIGH 0.490%), and index VRP is negative today — respect the 0.5/0.25 size scalars.

---

## 2a. Swing Dealer Positioning (1–4 weeks)

**No mechanized DEX flip fired anywhere — the +1 dealer rubric line is 0 fleet-wide today.**

- **SPY:** net DEX positive 5 consecutive sessions (06-29 → 07-06), today's +$30.3B the largest of the run (1.67× the trailing-10-session median). No sign change = no scored flip, but the advisory lean is **LONG** — real, strengthening dealer buy-flow supporting the uptrend. Vanna book is call-heavy (net_vanna −95.2k): a *latent* selling headwind if VIX declines 3 straight sessions (unmet — VIX 16.45→16.59→16.15→15.57, broken by the 07-01 uptick). Charm mildly negative. Front-end IV ratio 0.75 CONTANGO — no panic.
- **QQQ:** pure whipsaw — 3 sign changes in 5 sessions, today's +$4.0B below even the 0.25× median floor. **NEUTRAL.** The interesting latent setup: QQQ is in a negative-gamma pocket with a put-heavy vanna book — the textbook vanna-squeeze precondition. It fires only on a clean 3-session VIX decline; watch trigger, not current state.
- **IWM:** flat/noise on all three axes (DEX sub-$3.5B, vanna balanced, ZGL erratic). Disqualified — small-cap dealer book too thin to read at this horizon.

---

## 2b. Sector Rotation

**Rotation regime call: defensive→cyclical (MEDIUM confidence)** — more precisely, *risk-on with a defensive unwind*: the OUT side is a clean canonical-defensive exit (Healthcare −$33M, Staples, Utilities on the DP layer), while the IN side is co-opted by an outsized AI/mega-cap-growth surge (Tech +$4.79B = 66% of all cross-sector inflow) plus genuine Consumer Cyclical (+$1.03B) and Financials (+$463M) strength. The sector-flow-persistence tool shows every sector at 1.0 this week (call-premium-based metric, zero differentiation) — differentiation came from magnitude ranks and the ETF tape.

**ETF flow tape (advisory — instrument-level, 0 rubric points):**

| ETF | Net premium dir | Persistence | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| KRE | inflow +$25.1M (largest of 21) | BULLISH 5/5d | large near-mid blocks (ambiguous) | call sweeps Aug/Sep/Jan'27 $75–80, ask-side | **agree** → high conviction | JPM, BAC |
| XLE | inflow +$15.7M | BULLISH 5/5d | near-mid prints, neutral | mixed (2027 put + $55/56 call buying) | **disagree** (Energy weakest GICS sector, 0.8 persistence) → watch-only | Energy internally split (SHEL/EXE + vs XOM/COP/DVN −) |
| IGV | inflow +$9.9M | BULLISH 5/5d | dominated by one $180.7M closing-cross artifact — discounted | Jul $99 / Jan'27 $100 call buys | **agree** → high conviction w/ internal dispersion | PLTR, CRWV + / CRWD, ORCL − |
| EWT | outflow −$4.97M | BEARISH 5/5d | mixed | net bearish tilt | n/a (Taiwan thematic) | — |
| XBI | outflow −$4.91M | BEARISH 5/5d | mixed | two large put blocks (Jul $174, Jun'27 $150) | disagree w/ GICS aggregate, but corroborated by equity-DP Healthcare outflow + LLY/UNH bearish → bearish-subset read | LLY −, UNH − vs BIIB/VERA/RVMD + |
| XLI | outflow −$1.46M (thin) | BEARISH 5/5d (near-balanced) | neutral | today call-heavy (conflicts w/ 5d label) | disagree, weakly | — |

SMH: −$4.94M (2nd-largest magnitude) but MIXED direction — fails the ≥3-day persistence rule, appendix-only. Healthcare is genuinely **bifurcated**: LLY/UNH dragging vs biotech bid — a pairs-shaped idea, not a clean rotation call.

**Swing-book implication:** the two cross-confirmed rotation lanes are KRE/Financials (JPM, BAC) and IGV/AI-software (PLTR, CRWV — avoid the diverging CRWD/ORCL legacy names). Both lanes' single-name leaders nevertheless **failed the rubric** today (JPM/BAC/CRWV on the $50M cum-flow magnitude floor; PLTR on a −$188.7M 30d flow conflict). Rotation context, not sized trades.

---

## 3. Swing Setups (1–6 weeks)

**§3a Long swings: EMPTY. §3b Short/fade swings: EMPTY.**

No ticker cleared the two-agent confluence gate (Step 3), and the quant's top raw score was 1 against a drop floor of 3. The mechanical killer was the 30-day cumulative-premium-flow tape: every marquee bullish name was carrying above-median net *selling* against its thesis — AMD −$275M, INTC −$519M, MSTR −$637M, PLTR −$189M, GOOGL −$500M — each drawing the −3 flow_conflict. The contrarian-scanner independently returned zero fades (the four true bearish P/C extremes — CAT z=2.87, BSX z=3.05, ALL z=2.39, ALNY z=2.50 — all read as real hedge bids or informed continuation, and negative VRP aborts premium-selling fades anyway).

**Near-term sweep tape (informational, 0 points):** the only clean 5/5-day persistence is the **index put hedge complex** — SPXW/QQQ/SPY (5/5) and IWM (3/5), all OI-confirmed opening (IWM 283P +47.4k the largest single build in the scan), aligned with 30d cum-flow — broad institutional hedging into FOMC minutes 7/8 and CPI 7/14, not single-name conviction. Three persistence-break reversal watches: **MSTR** (bullish 4-DTE call build +45k OI, genuinely opening-confirmed — but −$637M/30d against it and the −$55M net premium day resolves to deep-ITM Sep 100C overwrite/financing), **INTC** (>$500M call sweeps at 88/89 7/10 — *not* OI-confirmed; churn on existing strikes while the real OI adds were 75P +26.9k; single-session bull call spread fighting −$519M/30d), **TSLA** (ambiguous mixed OI). Whale tickets of note: AMD $391M Aug 380C → $321M Oct 450C deep-ITM **diagonal roll** (multi-session bullish continuation footprint — the one genuinely constructive single-name structure today, but drowned by the name's own −$275M 30d tape, mega-tier DP 59% sell-side, and a Tier-1 opening 555P 7/10); SNDK Dec 80C/120C $336M = financing box (no directional info).

**C19 single-leg whale tier scan (advisory, 0 points):** three Tier-1 OPENING_PUT_PRIME prints — **SNDK 1750P 7/17 $23.8M (size/OI 2.09)**, SPCX 300P 7/17 $3.5M, **AMD 555P 7/10 $3.4M (size/OI 5.98)** — the validated bearish class (WR 61–64% next-session, bull-regime-measured; regime today neutral). Tier-2 context puts: AAPL, KLAC, WDC, INTC, INTU, NKE, UPS, LOGI. 276 CLOSING_ANTISIGNAL prints = heavy de-risking tape. Call side reported as CALL_UNVALIDATED (neutral regime — no fade-by-default).

---

## 4. LEAP Builds (6–24 months)

**TEVA — the sole candidate (watch-only; scored 0 under the frozen rubric).** Jan-2027 $33C/$36C fresh builds at 6.33x OI change, 100% ask-side; oi-trend BUILDING 6 consecutive days; 90d cum premium +$7.98M with 82% of it in the trailing 30d (fresh-thesis signature, ~13% of the name's gross — large for a $50M-gross tape); DP buy/sell 3.62 defending the $34.65–35.42 shelf; forward roll balance 0.949 (thesis-intact, single-date). 8-of-9 gates passed — but conviction-matrix confidence 45.8% fails the >70 leap line, and the frozen union-median flow test docks a −1 lite (the $6.6M flow is bottom-of-union in *absolute* terms). Earnings 7/29 sits inside FOMC week; the Jan-27 tenor extends well past it. No tender/M&A headline found (merger-arb blindspot checked; noisy feed — re-verify before any future sizing).

**Disqualified:** META (90d flow −$60M against the $17.3M Sep-27 600C floor block), ORCL (90d −$325M), NFLX (30d −$92.5M), GEO (context print uncorroborated — no long-dated OI presence), TER (flow is 4–11 DTE event-driven, not LEAP), BAC (Jun-27 65C size/OI 0.65 = partial close/roll-down), CXW/CSCO/KO/CMCSA/GIS/USO (Gate-4 accretion failures). Rolls of note: POET/INFQ far-leg growth trivial vs near-term OI collapse = net de-risking; XLF "roll" is a data-quality outlier (far build 24x the near reduction — legs not mechanically linked).

---

## 5. Volatility Surface

**The headline vol story: the IVR-100 wall is earnings-season bid, not dislocation.** 21 of 26 IVR-100 names report between 7/15 and 8/4. Once the 0DTE-contamination bug is corrected, MSFT's "BACKWARDATION" flips to CONTANGO 0.949 — the real signal is a set of clean earnings kinks. All `iv-percentile-zscore` reads are PROVISIONAL (dates_used=58 << 120-day floor).

**Catalyst-aligned kinks (hand-off to the earnings book):**

| Ticker | Kink expiry | Print | Implied move | VRP bias | Play shape |
|---|---|---|---|---|---|
| MSFT | 7/31 (46.6% vs 38.8/44.7) | 7/29 | 2.71% | FAIR (+0.023) | earnings calendar/straddle only — small edge |
| T | 7/24 (51.6% vs 41.4/46.7) | 7/22 | 3.12% | SELL (+0.051) | condor, respect rich put skew (tail-hedged 1.336) |
| **BE** | 7/31 hump 151.7% | 7/30 | **10.86%** | **SELL (+0.351, richest)** | condor/strangle into print — but see distribution caution §8 |
| FTNT | 7/31 (78.4% vs 56.9) | 7/29 | 4.02% | SELL (+0.285) | condor, complacent skew |
| TSCO | 7/24 (62.9% vs 46.3) | 7/23 | 3.10% | SELL (+0.168) | thin contracts — small |
| ASML | 7/17 contains the **7/15 print** | 7/15 | 5.08% | FAIR | genuinely earnings-driven (not an OPEX artifact); earnings-scout dissents: monotonic decay, no hump — SKIP on disagreement |
| GEV | 7/24 mild hump + unexplained 7/10 front spike | 7/22 | 5.14% | SELL (+0.113) | two separate stories; don't conflate |

**Substrate-artifact suspects — do NOT size:** WDC (242.8% at 7/17 OPEX tenor, earnings 7/29 — symmetric skew, FAIR VRP, no catalyst at that date) and AMAT (221.5% at 7/17, earnings mid-Aug) — both look like unweighted deep-OTM wing contamination at the strike-heavy monthly expiry. WDC's real catalyst read: 8.72% implied at 7/29.

**Backwardation calendars (catalyst-free):** MRNA is the best-positioned (front/back ratio 1.095, the only one under the 1.10 disqualifier; VRP +0.283) but needs a falling-ratio confirmation print tomorrow before acting. NBIS (1.168), SNDK (1.185), COHR (1.204) all fail the ratio gate today.

**Earnings-scout verdicts (14-day window):** MS **SELL VOL full** (event hump + tail-hedged back month — the cleanest short in the scan), ABT SELL VOL (tiny 2.46% implied = thin dollar edge), PEP SELL VOL half (32% crush priced but complacent back month), STT SELL VOL half (thin options), NFLX **BUY VOL** — *overturned in debate*: the quoted 2.66% implied move is a basis break (real straddle-implied ≈12.5% at 71.8% IV × √(11/365)); the cheap-vol thesis collapsed. SKIPs: BLK, ASML, TSM, JNJ, GS (CPI-day print + mismatched front leg), GE (anomalous curve), PENG (23% implied move, no tail confirmation), AEHR. All five scored plays entered Phase 2 and were gated to SKIP (§6/§7) — the negative index VRP and the earnings_vol lane's negative-edge audit history kept every short-vol structure unsized.

---

## 6. Risk & Correlation

**Macro headline:** normal curve (+0.35), sticky core inflation (CPI 2.96 / PCE 3.41), soft payrolls (+57k), 10Y flat at 4.49, USD strengthening, FF 3.63. **Event calendar:** FOMC minutes 7/8 (T+2, ambient), CPI **7/14 (T+6, the binding gate)**, PPI 7/15, retail sales 7/16, OPEX 7/17, FOMC decision 7/29. **Breadth cross-check:** 220 adv / 280 dec, pct_green 43.7 on a green index — **divergence flag ON** (distribution tell; advisory, no sizing change).

- **Correlation clusters:** SNDK/MU pairwise **0.832** → memory-semis cluster, treat as one position. SNDK kept (direction-aligned +$1.66B 90d flow), MU −1 cluster tier (90d flow −$134M against; tie-break used the tool's 90d window — known artifact, disclosed). No other pair ≥0.60. `portfolio-correlation` returned sector=Unknown for all five (tool gap, noted for audit).
- **Gate stack on the top-5-by-raw (all pre-risk skip; gates recorded for the envelope):** SNDK — fundamentals −1 (CAUTION), debate −1, event −0.5, OOR half-cap. MU — cluster −1, debate −1, event −0.5, half-cap. MS — **VRP −1 (short vol into negative VRP)**, debate −1, event −0.5 (CPI eve-of-print), half-cap. NFLX — debate −1 (implied-move basis break; VRP favorable but cannot upgrade), half-cap. ABT — VRP −1, debate −1 (0.65/0.65 tie fires), event −0.5, half-cap. **Final: SKIP × 5.**
- **Fundamentals verdicts:** SNDK **CAUTION** (insider MSPR −100 near-uniform 18mo + same-day "smart money cashing out" press; 4/4 beats acknowledged — 1-of-3 legs contradicts). MU CONFIRM (June insider flip to buying; Tepper/Appaloosa citation). MS CONFIRM (qualified — no move-size data exists in the enrichment). NFLX CONFIRM (for the vol thesis; 4/4 miss streak with variable magnitudes). ABT CONFIRM (strongest: ±1.1% surprise band ×4, insider +85, DOJ probe closed 7/1).
- **Debate disconfirmation: the bear won all five** — SNDK 0.40/0.65, MU 0.55/0.65, MS 0.40/0.65, NFLX 0.60/0.75, ABT 0.65/0.65 (tie fires). Standout: the NFLX bear's straddle arithmetic invalidated the entry premise; the MS bear reframed back-month tail-hedging as smart money *on the other side* of the strangle.
- **Adverse-flow exits (carried book):** **SNDK — EXIT CANDIDATE** (Tier-1 put + insider −100 + IVR 100 into 8/12 earnings; flow and fundamentals both reversed vs the carried long). **MU — EXIT CANDIDATE** (90d flow −$134M, mega-tier 59% sell, 8/7 term kink). Advisory adverse: SMH (P/C 6.27, IVR 96), BSX (P/C 4.10, IVR 100). **IBIT — on-thesis HOLD** (bullish flow +$5.9M, OI +391k, IVR 10.5). No adverse fz fundamentals drift on the rest of the carried book.
- **Hedge sleeve:** formal skew gate not triggered (nothing added today; net new delta 0). Maintenance convexity only: **SPY Aug-21 745/720 put debit vertical** (spans CPI 7/14, OPEX 7/17, FOMC 7/29) or **VIX Aug 17/20/25 call ladder**, 0.25–0.50% NAV. Do not sell premium against it — the negative-VRP regime gates short-vol overlays. Rationale: the institutional tape has already built this hedge (5/5-day index put persistence); we align in token size rather than fade it.
- **Watchlist write-back:** **skipped** — all-DROP board; DROP names are never written and no LOW names exist today. `conviction_2026-07-06` group not created.

**Risk officer summary:** fourth and deepest empty-book day; every gate agrees with the quant. The bear residual beat or tied the bull on all five names, both short-vol earnings plays were selling cheap vol into a negative-VRP tape, and the one hot cluster (memory semis) is being distributed into under bullish headlines. Refusing to size is the correct output — the sized-vs-paper history (36.1% vs 45.2%) says the gates earn their keep on exactly this kind of day. The real work today was the carried book: SNDK and MU tagged for exit, IBIT held, and token convexity into CPI.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**EMPTY.** No HIGH or MEDIUM tier names today — the top raw score across the 18-name union was 1 (drop floor 3). No name reached Step 3a's load-bearing gate, Step 5 sizing, Step 6 deep-dives, or the Step 6.5 batch strategy scan (all skipped by protocol on an all-DROP board). Step 8.5 deep-dive hand-off: skipped (no-edge day).

**Expectancy lens [advisory — expectancy is not yet a live sizing axis]:** per the 2026-07-04 calibration audit, the tier ladder remains inverted (HIGH realized 0.143 across three consecutive audits) and the post-freeze book ran −8.8pp vs benchmark; the out-of-regime half-cap has been protective (out-of-regime calls −16.7pp, n=10). A day that produces zero sized calls should be read against that base rate: the frozen rubric currently has no demonstrated positive expectancy at any tier, and abstention is cheap.

**Top-5-by-raw audit trail (all DROP/skip — recorded for the calibration loop):**

| Ticker | Dir | Raw | Class | WR (n, src) | Fund. | Debate (bull/bear) | Final |
|---|---|---|---|---|---|---|---|
| SNDK | long | 1 | bullish_flow | 0.4599 (137, clean; excess −9.5pp) | CAUTION | 0.40 / 0.65 | SKIP + carried-book EXIT |
| MU | long | 1 | sector_rotation | NA(substrate) | CONFIRM | 0.55 / 0.65 | SKIP + carried-book EXIT |
| MS | vol_short | 1 | earnings_vol | NA(substrate) | CONFIRM | 0.40 / 0.65 | SKIP |
| NFLX | vol_long | 1 | earnings_vol | NA(substrate) | CONFIRM | 0.60 / 0.75 | SKIP |
| ABT | vol_short | 1 | earnings_vol | NA(substrate) | CONFIRM | 0.65 / 0.65 | SKIP |

### Conviction-scoring rubric (Step 4, verbatim — RUBRIC FROZEN version 2026-06-12)

```
Daily conviction score = Σ:
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna-squeeze setup in trade direction — the trigger must be a verified SIGN CHANGE, not a level: sign(net_dex) on the latest session opposite to ≥3 consecutive prior sessions, read from dated `uw options-structure dex --date` calls (≥4 to verify the prior-session sign run; ~11 for the trailing-median floor), with |net_dex| on the flip day ≥ 0.25× the trailing-10-session median |net_dex|; the evidence string must cite both dated values. Vanna disjunct additionally requires a dated VIX source (Yahoo chart API ^VIX) for the falling-VIX leg — no out-of-band VIX fills.
  +3  3+ aligned signals in accumulation-hunter (DP + OI + uw oi smart-positioning, uw dark-pool block-stratified institutional-tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms (sign aligned AND |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: only when dominant_signal_class == leap_directional; else 0.
  +1  uw historical cumulative-premium-flow net directional accretion in trade direction (30d) — INTENT-SCREENED (no C28 distribution_flag; no ex-div deep-ITM sub-parity arb). Screen failed/unevaluated on a flagged name → 0.
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector — CONDITIONAL: (a) sector persistence ≥ 0.6 AND (b) cum_premium_flow_30d aligned AND (c) |cum_flow_30d| ≥ $50M. Default 0.
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising uw historical pc-ratio-zscore (VRP positive) — informed-flow continuation penalty, routed via C13, never double-counts with a flow read
  -3  flow_conflict — mechanical when 30d cum-premium-flow direction is clearly opposite dominant_signal_class (sign flip + magnitude > union-median |cum_flow_30d|, or explicit OPPOSITE label)
  -1  flow_conflict_lite — when the 30d read is MIXED (signed sum near zero, or aligned but bottom-quartile magnitude). Mutually exclusive with flow_conflict.
  # TIER GATES (2d, not score_components): correlation cluster (corr ≥ 0.70) = −1 TIER; regime conflict = −1 TIER.
```

**Tiers:** ≥9 HIGH (full, subject to 3-of-4 load-bearing gate + win-rate gate) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 drop. Tier cuts retained under the P0.1 freeze; carry no validated ranking claim (2026-06-12 re-confirmation failed); P0.6 caps all sizing at half while OUT-OF-REGIME.

---

## 8. Watch-only — single signal, no confluence

Every name below surfaced from a single agent (or died on internal contradiction) and failed the two-agent confluence gate. Journaling only — NOT trade entry.

| Ticker | Source agent | Raw | One-line reason it isn't a trade |
|---|---|---|---|
| SNDK | quant top-raw (cum-flow +1) | 1 | $874M/30d bullish flow vs Tier-1 $23.8M opening put, insider −100, "cashing out" press; genuinely mixed → CAUTION + exit candidate |
| MU | sector-rotation | 1 | Tech-leader +1 passes, but mega-tier DP 59% sell + 90d flow negative + 8/7 term kink; cluster-linked to SNDK (0.832) |
| MS | earnings-scout | 1 | cleanest sell-vol structure in the scan, killed by negative VRP + CPI-eve print + vol-lane audit history |
| NFLX | earnings-scout | 1 | BUY VOL premise died in debate: quoted 2.66% implied move is a basis artifact (real ≈12.5%) |
| ABT | earnings-scout | 1 | strongest fundamentals of the five; surprise tightness ≠ move tightness; CPI + retail sales stack on the expiry |
| PEP | earnings-scout | 1 | 32% crush priced (7/9 print) but complacent back month; $43M DP print was 2-day-only persistence |
| STT | earnings-scout | 1 | tail priced but options too thin to execute at size (cc 35–52) |
| BE | vol-surface / sweep-tracker | 1 | richest VRP in cohort (+0.351, 10.86% implied 7/30) but 30d flow −$292M, put OI builds, **distribution_flag: 300C 7/17 closed ~$695K (⚠ accumulation-as-distribution caution)**; accumulation matrix 43.6 just under the 50 floor — closest miss of the day |
| TEVA | leap-radar | 0 | 8-of-9 LEAP gates, killed by the frozen matrix >70 line + absolute-magnitude lite dock; the one name worth journaling as a future LEAP re-scan |
| JPM | sector-rotation | 0 | KRE leader but +$24.4M < $50M floor; conviction-matrix reads DISTRIBUTION 32.7% |
| BAC | sector-rotation | 0 | same $50M floor fail; Jun-27 65C size/OI 0.65 reads as partial close |
| CRWV | sector-rotation | 0 | $22.5M flow exactly at the q1 boundary; 90d +$73M supportive; single-agent |
| AMD | multileg | −1 | genuine $712M bullish diagonal roll (+2, multi-session) vs −$275M/30d flow conflict, mega-tier 59% sell, Tier-1 555P — the day's most instructive contradiction |
| INTC | multileg | −1 | single-session 88/89 bull spread vs uniformly bearish 30d/90d tape; call sweeps not OI-confirmed |
| LLY | sector-rotation (short leg) | −1 | XBI/DP/single-name bearish trifecta vs the name's own +$70M/30d bullish options flow; also under the standing no-short-alpha ruling |
| MSTR | sweep-tracker | −3 | OI-confirmed one-day call reversal vs −$637M/30d (largest conflict in union) + Sep 100C overwrite read |
| PLTR | sector-rotation | −3 | IGV-lane leadership vs −$189M/30d + −$202M/90d persistent net selling |
| GOOGL | contrarian (informational) | −3 | one day of dip-buying (+$18.6M) vs a quarter of net selling (−$500M/30d) |

---

*Generated by /daily-analysis (11-agent Phase 1 fleet + quant/fundamentals/debate/risk Phase 2; opex-pin-strategist not spawned — outside OPEX window). Envelope: `analyses/daily/2026-07-06/decision.json` (schema 1.3, rubric 2026-06-12). Event dates: BLS CPI/PPI schedules, Fed FOMC calendar, Census retail. Empty-book protocol (4th occurrence) applied: 2b/2c/2d ran on top-5-by-raw; no watchlist write-back.*
