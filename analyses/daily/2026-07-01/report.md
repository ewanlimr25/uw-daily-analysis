# Daily Market Analysis — 2026-07-01

## Executive Summary
- **Regime + GEX state:** TRANSITIONAL (trend UPTREND — SPY 745.76 above 20/50 SMA, but flow breadth just 37.1% bullish; 3,934 bearish vs 2,319 bullish flow tickers). SPY EOD gamma book net short (−188.9M, spot parked exactly on the 745/746 flip); QQQ long-gamma (+141.2M) but fresh and fading; IWM FULLY_NEGATIVE (−163M). VIX 16.59. Price breadth green (59.4% advancers) against a bearish flow tape — flow-vs-price tension, not classic distribution. Sector lean: no rotation; the dispersion is intra-Tech (semis → software).
- **Rubric regime status:** OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half.
- **Conviction book: EMPTY.** Zero names cleared the raw ≥3 floor (highest: MSTR/TSM/TLT at raw 2). The frozen 2026-06-12 rubric, the fundamentals gate, and all five bull/bear debates agree: this is a no-trade tape — TRANSITIONAL regime, June NFP printing 8:30 ET pre-open tomorrow, markets closed Friday, and 20 of 28 scored names carrying MIXED 30-day flow. A "no edge" day is a valid output.
- **Next-session GEX (SPY/QQQ):** SPY — net short gamma, spot dead on the 745/746 sign flip, walls 750/740; conditional-directional book, no clean pin. QQQ — long-gamma with a single +316.8M pole at 725 (pin magnet), put wall 724; below 723 the book flips short-gamma. Both priors are unusually fragile: NFP gaps them before the open. Advisory, see §2.
- **Top swing build:** none scored. Best-documented watch: MSTR short (raw 2, fundamentals CONFIRM, but debate cut it — the smart money expresses this thesis in Sep-dated far-OTM puts, not a 1–4wk swing).
- **Top LEAP candidate:** none promoted. STLA cleared 7-of-8 radar gates (Jan-27 7C +7.7k at 99.5% ask-side, 8-day OI build) but is floor-fragile at $5.81 and conviction-matrix reads COVERED_CALL — advisory watch only (§4).
- **Biggest risk:** the NFP gap. Every EOD level in this report is a prior that dies at 8:30 ET tomorrow; QQQ carries a crowded-long extreme (P/C z −2.11) into the print with front-end backwardation (0DTE IV 1.59× VIX), into a 3-day weekend. See §6 for the hedge sleeve.

---

## 1. Regime & Gamma State

**`uw risk market-regime`:** TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity." Trend UPTREND: SPY 745.76 > SMA20 741.55 > SMA50 736.61, −1.93% from the 90-day high, −1.68% over 30 days. Guidance: half position sizes, defined-risk structures. Flow breadth is the bearish half of the mix: only 37.1% of the 6,253 optionable tickers printed bullish flow.

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 745.94 | null (grid flip ~745.5; `zgl_reliable=false`) | −188.9M | FULLY_NEGATIVE¹ | 746 (real shelf 750) | 745 (real shelf 740) |
| QQQ | 725.86 | 314.06 = artifact (`zgl_reliable=false`) | +141.2M | POSITIVE (fresh, fading) | 740 | 724 |
| IWM | 299.32 | — | −163M | FULLY_NEGATIVE (whipsaw regime) | — | — |

¹ Tool label contradicts its own grid (27/50 strikes positive; ~−303M of the total sits below the 724 grid floor) — read as net short gamma concentrated at/below spot, not all-strikes-negative.

**DTE share (`uw options-flow dte-volume-share`):** BALANCED — 0DTE 34.1%, weeklies 24.1%, monthlies 23.8%, LEAPs 5.0%. Neither retail-dominated nor institutionally skewed; no uniform conviction adjustment.

**VRP (`uw historical vrp`):** FAIR on both indices and slightly negative — SPY IV30 13.9% vs realised 15.4% (VRP −0.015), QQQ 24.6% vs 28.9% (−0.043). Realised running above implied means premium-selling has no carry edge; every short-vol expression today had to justify itself name-specifically, and none did.

**Macro backdrop (`scripts/fred_macro.py`):** curve normal (+0.31), core CPI 2.96% / core PCE 3.41% YoY, unemployment 4.3% with payrolls +172k, 10Y 4.44 flat over 30 days, USD strengthening, fed funds 3.63. Benign but not dovish — the sticky core-PCE print keeps the July FOMC live.

**Forward event risk:** **June NFP 2026-07-02 8:30 ET (pre-open, next session)** · US markets closed 2026-07-03 (July 4 observed) · June CPI 2026-07-14 · June PPI ~2026-07-15 · FOMC 2026-07-28/29 (outside the 10-day window but inside every August-expiry structure). The 07-17 OPEX expiry bundles CPI + PPI + the first wave of bank/semi earnings.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)
> **Advisory, not a scored signal.** EOD dealer-gamma book (OI persists overnight) read forward as the *prior* for the 2026-07-02 open. Prose-only, contributes 0 points to the conviction rubric, no backtested predictive claim (validation lives in `/weekly-analysis` §2). **This prior is unusually fragile tomorrow: NFP prints pre-open and Friday is a holiday — a >1% gap voids every level below until fresh 0DTE OI rebuilds the map in the first 30–60 minutes.**

### SPY — spot parked ON the flip line, short gamma underneath
Spot 745.94, total GEX −188.9M, ZGL null (`zgl_reliable=false`; the per-strike grid flips sign at 745/746). Put wall 745 (−213.6M) is the ATM battleground with support shelves 740 (−75.6M) / 735 (−81.9M); call wall 746 (+127.9M) is ATM-adjacent with the real caps at 750 (+115.5M) / 755 (+111.4M). The short-gamma regime is persistent (FULLY_NEGATIVE 06-22→06-26, a shallow two-day repair, back to FULLY_NEGATIVE today) — not fresh. Operative rails: 750 (+0.54%) and 740 (−0.80%) vs a 0.92% 0DTE implied move — the straddle roughly prices the wall band.

**Structure bias (conditional-directional, no clean pin):** NFP gap opens and holds below 745 → dealers amplify; debit put verticals toward 740/735, do not sell premium into short gamma. Opens/stabilizes 746+ → dealers dampen; fade pokes into 750–755 via call credit spreads at the 750 wall. Enter only after the gap resolves.

### QQQ — concentrated long-gamma pin, fresh and fading
Spot 725.86, total GEX +141.2M POSITIVE — but the regime flipped NEG→POS only on 06-30 and faded +558M → +141M in one session. One dominant pole: **725 (+316.8M, 2.2× the entire net book)** flanked by negative wings 724/726 — a genuine pin magnet while QQQ trades ~723–730. Below ~723 the grid turns uniformly negative: a gap through the 724 put wall flips the book short-gamma and the move runs (720, 715, 710 shelves). Call wall 740. The 1.66% 0DTE implied move dwarfs the ±5-pt pin width — the straddle is rich *only if* the pin holds, and the 0DTE IV at 1.59× VIX is NFP event premium, not free money.

**Structure bias:** iron fly / short straddle centred 725 at quarter size, entered **only after the NFP gap resolves inside 723–730**; an open below 723 invalidates the pin → debit put verticals toward 720.

**Near-dated confirmation:** the 07-02 expiry is the second-largest premium bucket on both books (SPY $251M, QQQ $273M — `uw options-flow expiry-heatmap`).

**Mandatory caveats:** EOD book = prior refreshed after the open; HIGH gap risk (NFP pre-open + holiday weekend); ETF book, not the SPX/NDX index book; 0–45 DTE proxy (D+1 expiry cannot be isolated); SPY tool-label/grid contradiction and unreliable ZGLs on both indices documented above.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py` — the validated stack)
Backtest verdict **GO_PREMIUM_SELL_INTRADAY** on both indices (n=56) — but tomorrow is an NFP session; the entry rule carries the day.

| | SPY | QQQ |
|---|---|---|
| sell_premium | true | true |
| vol_state / VIX | LOW / 16.59 | LOW / 16.59 |
| implied move | 0.92% | 1.66% |
| expected range | 1.25% | 1.25% |
| size_scalar | 0.5 | **0.25** |
| structure | wider iron condor, wings ≈ ±1.25% | iron fly / short straddle centred ~724.74 |
| net PnL (gross) | **+0.215%/day net** (+0.315 gross) | **+0.315%/day net** (+0.415 gross) |
| caution | — | **front-end backwardation: 0DTE IV 1.59× VIX — event/gap risk, half size** |

PnL basis: % of underlying spot notional, gross minus 0.10% assumed round-trip cost — *not* premium-collected, not margin-relative; lead with net per P1.8. Win rates (94.6% SPY / 89.3% QQQ open-entry) overstate a negatively-skewed short-vol edge — the validation sample contains **no vol shock; the left tail is unsampled**. VIX 16.59 sits in the LOW tercile — the thinnest-edge state (SPY mean +0.112%/day). **Entry:** at/after the open once the NFP gap resolves; hold to the close; never carry overnight (overnight entry backtested −0.156%/day SPY). If it gaps beyond the wings, stand aside. Delta-neutral only — no directional tilt. SPY ≈ SPX (validated identical); QQQ weaker (Nasdaq index book unavailable). Advisory, 0 rubric points; promotion permanently gated on a tail-aware net-expectancy bar.

## 2a′. Swing Dealer Positioning (1–4 weeks)
**Zero mechanized DEX flips today — the +1 dealer line earned nothing.** SPY's sign flip happened 06-29 (mid-window, now trajectory context); QQQ's 07-01 tick to −0.36B fails both the ≥3-prior-session bar and the 0.25× magnitude floor (0.03× the ~12B trailing median — textbook whipsaw the floor exists to kill).

- **QQQ — the one live dealer setup: vanna squeeze, event-gated.** Put-heavy book (net_vanna +10,350; put_vanna 84,970 > |call_vanna| 74,619) + dated 3-session VIX decline (18.41 → 17.65 → 16.45; 07-01 +0.14 marginal) + tool-flagged GEX regime flip 06-30 NEG→POS that held today. Front-end ratio 1.155 sits above the 1.10 line — the squeeze is **armed, not maturing**: it matures only if NFP resolves benignly and the front end crushes (that crush is itself the vanna fuel). Swing bias LONG (1–2wk), strictly post-event. Invalidation: hot NFP / VIX up 2+ sessions / net_vanna flips negative / GEX back below zero.
- **SPY — FLAT (disqualified):** DEX trajectory strongly improving (−31.8B → +8.1B over four sessions) but vanna is call-heavy short-side and GEX flipped back FULLY_NEGATIVE — DEX and vanna disagree, which is an explicit skip.
- **IWM — FLAT:** near-zero DEX, whipsawing GEX regime, no thesis.
- **MU — dealer book NOT confirming the bearish tape:** net_dex +3.43B (public still net call-long) against −$283M day premium. The semis short thesis lacks dealer confirmation.
- **META/TSM — positive DEX levels (+8.17B/+1.28B), levels only, no flip claims.** TSM's positive DEX sits oddly against iv_rank 100 and bearish premium — no clean read.

## 2b. Sector Rotation
**Rotation regime: `no_change` (confidence low).** The GICS persistence layer is non-discriminating — 9 of 11 sectors at 1.0, everything INFLOW; there is no persistent outflow side (Energy's −$17.3M today is a single-day flip inside a 0.8 score). Market-relative bar clears only Technology (+$4.07B), Comms (+$1.51B), Financials (+$302M), Healthcare (+$266M). This is a broad trending tape, not rotation. **The tradeable dispersion is INTRA-Tech: semis → software.**

**ETF flow tape (advisory — instrument layer the GICS aggregates can't see):**

| ETF | Net premium dir | Persistence (5d) | DP positioning | Options urgency | GICS agreement | Named leaders |
|---|---|---|---|---|---|---|
| SMH | inflow +$105.4M | BULLISH but 07-01 day-flip | **below-mid late prints $243M (distribution/hedging tell)** | put-dominated sweeps (600P $17.7M, 602.5P $13.3M) | agree, with tension | — |
| IGV | inflow +$85.6M | BULLISH — cleanest tape in the book | moderate, near-mid | call-side sweeps across tenors | agree | MSFT, NOW, PLTR |
| XLE | inflow +$15.0M | BULLISH | large near-mid | long-dated collars | **disagree** → watch-only | — |
| XBI | outflow −$9.4M | BEARISH | near/above mid | put-tilted | **disagree** (GICS HC inflow) → watch-only | — |
| EWT | outflow −$5.4M | BEARISH | thin | Sep calls sold on bid (overwrite/exit) | n/a — TSM echo | — |
| XLV | outflow −$1.6M | BEARISH | large near-mid | small/mixed | **disagree** → watch-only | — |

Three cross-basis divergences worth the desk's attention: (1) **Tech options +$4.07B vs Tech DP −$484M**, co-confirmed at instrument level by SMH's below-mid late prints — a confirmed inflow with a distribution tell; (2) **the semis/software split inside the Tech 1.0 aggregate** — SMH day-flipped bearish (PCR 3.76) with the whole semicap complex at iv_rank 100 while IGV runs +$85.6M call-side (EWT −$5.4M is the geographic echo); (3) **both HC ETFs outflow while GICS HC prints +$266M inflow** — the healthcare bid is single-name (ABVX, RARE, ACHC, GH), not basket; do not express HC via ETF.

Long-side leaders (all failed scoring on 30d flow conflicts — see §7): META +$126.5M (but 30d −$102M), MSFT +$53.3M (30d −$597M + Tier-1 put + DP distribution), LITE +$48.9M (30d +$94M MIXED), PLTR +$25.6M (30d −$241M), NOW +$8.2M (30d +$35M < $50M gate). Short-side: the semis stress complex (MU/INTC/AMD/SNDK/TSM) — per the 2026-06-27 audit, shorts are hedge/relative-value legs, never sized alpha. Swing implication: the pair expression (long software vs semis hedge) is the only durable read, half-size into NFP; it earned no rubric points today.

---

## 3. Swing Setups (1–6 weeks)

> **The scored book is EMPTY.** No name cleared the raw ≥3 conviction floor (28 scored; top raw = 2). Everything below is watch-only documentation — journaling, invalidations, and re-entry triggers. Nothing here is a trade entry today.

### 3a. Long swings (regime-aligned) — none scored
- **QQQ (raw 1, the only confluence-pass name):** Mar-2027 795/815 call vertical (~$237M gross — but volume ≈ existing OI at both strikes: likely a roll) + $19.6M unambiguously fresh 805C ask blocks + the vanna-squeeze setup (§2a′). Failed the mechanized dealer bar; flow_conflict_lite on MIXED index churn; crowded-long P/C z −2.11 into NFP. Debate: bull 0.65 / bear 0.75 — cut. **Re-entry trigger: benign NFP → front-end crush → vanna fuel; look again 07-02 after the gap.**
- **IGV (raw 1):** cleanest ETF call tape (+$118M 30d), Jan-27 80P −128.9k hedge unwind — but its own top holdings ran −$838M combined 30d single-name outflow (MSFT/PLTR), the bullish_flow class WR is 0.4855 (< 0.50 floor) with −7.3pp market excess (beta, not edge). Debate cut (0.55/0.65).
- **JPM (raw 1):** the strongest single-name DP stack on the tape — mega buy_ratio **1.00** ($2.02B, 7 prints, zero sold), detector 24.4×, 3-day OI build, DP shelf 334.07 — but conviction-matrix 47.6 < 50 floor, options tape near-balanced, and the prints carry a Q3-day-1 benchmark-cross signature. C11 halved the accumulation award (cum-flow +$2.8M ≪ $50M). **Re-test 07-02: if conviction clears 50 with the DP stack intact, this promotes.** Invalidation anchor (C34): the 334.07 single-price shelf / 327.33 secondary.
- **DLO (raw 1):** Dec-2026 13/17 call vertical 60k×60k (~$10.7M debit) + Aug 16/20s — the cleanest fresh institutional structure on the small-cap board, and a funnel confluence-6 name. Single-agent, 30d history uninformative ($10M-gross book). Watch for a second session of follow-through.
- **WULF (raw 1):** Jul-17 bullish put-credit ladder (sold 27P/26P vs bought 24/23/22P) + Sep 22C buys — note the headline "$27.3M put premium" is premium *sold*; the naive read gets the sign wrong.
- **ACHC (raw 0):** confluence-6 funnel + 23.6% short float + 5/5-day Jul 35C OI build — but the DP/OI stack is retail-scale ($11.8M total DP) and institutional-tier unconfirmed. Squeeze-watch material, not accumulation.

### 3b. Short / fade swings (defined risk only) — none scored
- **MSTR (raw 2 — the board's top score):** 30d cum flow −$601M outright BEARISH (6.1× union median), Sep 35P/60P opening builds, 8/10 bearish days, fundamentals **CONFIRM** (insider selling, PT cuts, BTC < 200-wk MA, the $1.25B sell-framework doctrine break). **Debate cut it (bull 0.65 / bear 0.75)** on tenor and path: the institutional money expresses this exclusively in Sep far-OTM puts — it refuses the 1–4wk swing-short tenor — while beta 3.58, PB 0.855, a $2B buyback, and yesterday's +7.4% flow-unsponsored bounce make the swing short a squeeze magnet. If expressed at all: Sep-dated defined-risk puts, not a swing short. Invalidation: 30d cum flow flips positive / a second consecutive bullish-net session.
- **TSM (raw 2): fundamentals VETO.** 4/4 beat streak, fortress margins, PTs raised, earnings **07-15 confirmed** (14 days — a binary from a serial beater); 90d flow +$276M bullish; dealer DEX positive; 25Δ skew NORMAL, not tail-hedging. The −$291M 30d bearish paper reads as hedging/collaring of a winning long base into the print. The short is dead; the surface trade (§5 calendar) is the live idea, post-NFP.
- **INTC (raw 0):** sweep-persistence #1 short (4/5 sessions, $773M window, −$310M 30d, opening-confirmed put builds Aug 14P / Nov 8P) — but the trend label is MIXED (the ~$600M of deep-ITM next-day call *arb* prints pollute every premium aggregate; multileg correctly excluded them). Watch: next session's sweep direction.
- **SMH (raw −1, confluence-pass):** 4/5 bearish sweeps but aggregate ΔOI −7.6k (churn, opening-unconfirmed), 30d flow +$85M opposes, and both flagging agents called it a hedge leg. The semis put tape is statistically ordinary (z −0.44 vs its own 20d norm) — **not crowded, and not a fade either** (§5 for the vol expression).
- **BSX (raw −1):** P/C z +6.84 BEARISH_EXTREME + Tier-1 whale put (55P Jul-17, $1.04M, floor print) — but this is informed continuation on a live catalyst stack (Edwards FDA clearance 06-29, valve recall, PT cuts; −52% YTD), front IV 137% on the 1-DTE line, and the 30d book is net *bullish* +$41.6M. No fade, no chase; contrarian's defined-risk continuation-short plan stays prose-only.
- **CAR (raw 1):** P/C z +4.75 with 133% 1-DTE IV = an unidentified imminent catalyst priced. Do not touch either side; if the front end collapses benign, the trapped put crowd becomes next run's squeeze-long candidate.
- **TLT (raw 2):** Aug 83/79 put vertical 51k×50k (~$0.24 debit, ~17:1) spanning NFP + CPI + FOMC; 10/10 bearish days. Debate cut (0.55/0.75): the 82.76 breakeven sits below the entire 57-day low while the 10Y is flat over 30 days — cheap convexity, poor base rate. Documented as the institutions' rates-tail expression, not a call.

**Sweep ledger (informational — 0 rubric points):** INTC #1 (4/5 bearish, opening-confirmed), MSTR #2 (3/5, cum-flow co-flag), SMH #3 (churn), TSLA #4 (5/5 bearish $5.19B but mega-cap hedge character, half-weight). Contested: SNDK (5/5 window-bullish $1.68B vs today −$49.9M put-heavy builds — a long book under attack, direction flip in progress; largest |cum_flow| in the union at +$1.05B). Index put books (SPXW/SPY/QQQ 5/5 bearish, $8.7–12.2B) are pre-NFP hedge demand, not directional. Single-day watch: WMT 110P $7.45M ask 40:1, EOSE Jan-28 10P $18.2M, KWEB Sep 27C $3.3M.

---

## 4. LEAP Builds (6–24 months)

**None promoted.** Today's DTE>180 tape is dominated by ETF/macro hedging into the event corridor (XLE Dec-27/Jan-27 50–52.5P +40k / ~$17.1M — producer-hedge-ambiguous, context only; TLT Jan-27 85P +13k, Jun-28 80P +10k; IWM Jan-27 210P +14k; FXI collars; SPY Jun-27 672P written at bid).

- **STLA — 7-of-8 radar gates, advisory watch (NOT scored: raw 0, floor-fragile).** Jan-2027 $7C +7,739 (OI 6.1×, 99.5% ask-side, ~$0.55) + Jan-2028 12C builds recurring across 8 consecutive sessions; DP accumulation 2.32 buy/sell into a −24% monthly slide, cluster 5.76–5.87; 90d flow +$3.9M bullish (thesis-extension). Kill-side: conviction-matrix reads COVERED_CALL 25.2 (strict Gate-8 fail — cleared only via the P1.5 alt LEAP-tenor path: ask 6,709 vs bid 31), 30d flow flat, price $5.81 sits $0.81 above the C12 floor. If taken despite the flags: Jan-27 $7C or $5/$8 call spread, half-size. Invalidation: close < 5.76 DP floor; < $5.00 breaches C12 outright; 90d flow negative ≥10 sessions.
- **Disqualified (kill gates, for the record):** NFLX — Mar-27 100C +10.8k at 97.5% ask-side *but* 90d flow −$185.5M (hard Gate-4 fail; re-qualifies fast if 30d flips positive). RIVN — Jan-28 12P bid-heavy = put *selling*, not a LEAP buy. CL/NTR — flat/wrong-direction flow. **META Dec-2028 1130P ($2.34M deep-ITM) resolved as collar/conversion financing, not a structural short** — call-dominant 10-day build, absent from rolls, +$126.5M same-day bullish premium.

---

## 5. Volatility Surface

**The day's surface story is the semicap complex:** TSM / LRCX / KLAC / ASML / TER all at iv_rank 100 with z-scores 2.3–3.3 (percentile reads are n=56 provisional — below the 120-day floor; the z is the defensible statistic). And the surprising read: **all five are COMPLACENT at the 51-DTE tenor** (skew ratios 0.99–1.018; TSM's 25Δ calls bid *over* puts) — a rank-100 vol bid with zero put-skew premium means the surface is repricing *symmetric* uncertainty, not tail-hedging. Desk implication: **put spreads / put calendars are the efficient bearish semis expression; outright long puts fight the 100th-percentile level.**

- **ASML — KINKED at 07-17** (77.2% vs 62.0/67.3 neighbors, 1,413 contracts; ER 07-15 premarket confirmed, implied move 2.52%): the only name where kink, catalyst, and screener triangulate — but back-month skew is flat (front-only kink = coin flip), FE ratio 1.20 > 1.10, and 2.5% implied is arguably *cheap* vs ASML's typical 4–6% print move. SKIP; revisit ≥07-10 (FE toward 1.05–1.10 with kink intact opens the 07-17/08-21 calendar; back-month skew > +0.05 upgrades to SELL VOL).
- **TER — kink 07-31** (103.4%) at late-Jul ER, z 3.27 (highest in complex). **LRCX** — plateau, whole curve bid, weak standalone.
- **TSM — the cleanest structural calendar (WATCH):** 07-10 77.3% vs 08-21 55.5% / 09-18 54.8% — a 22-pt drop over 6 weeks. Short 07-10 / long 07-24-or-08-21 call calendar, **but the short leg is NFP + June-sales vol and the ER sits between legs. Trigger: enter only post-NFP with the front-end ratio falling; abort if the ratio is still >1.10 and rising past 07-06.** Expiry heatmap supports the legs: 07-10 is put-heavy hedging; Jun-2027 LEAPs are $15.4M calls vs $2.0M puts.
- **NBIS — persistent steep backwardation** (9d 139.6% vs 79d 123.9%) with no catalyst in the screen window — same post-NFP trigger, watch only.
- **MU — surface unusable:** the filtered curve is an unweighted-strike-mix sawtooth (104%→142% adjacent tenors); back months ~90% vs front 104–134% says the DRAM vol bid persists post-print, but no term trade.
- **Earnings calendars (from earnings-scout, all half-size, all watch-only at raw 1):** **GS** — cleanest kink on the board (07-17 56.2% vs 38.4/39.2 neighbors, 3,599 contracts; FE 1.55 disqualifies naked shorts) → sell 07-17 ~1020 straddle / buy 08-21, enter after the 07-10 weekly rolls off; but the 07-17 bucket is triple-loaded (CPI + ER + OPEX). **PEP** — the most extreme front panic scanned (FE 1.689; 07-10 45.4% vs 30d 28.7% on a 1.1% implied-move staples name; −42k pre-event OI de-risking) → sell 07-10 141 straddle / buy 08-21, enter 07-06 post-NFP only. Both carry the earnings_vol class caveat: the two BH-surviving miscalibrated vol classes (claimed 0.88 → realised 0.38) — never sized off a backtest quote. **PENG** (07-07 post, 23.3% implied, iv_rank 98): uninvestable both ways — complacent back-month skew kills the short, a 4-quarter beat streak at 170% IV kills the long; first PEAD screen of the month if it beats and holds. JNJ/AEHR/CAG — SKIP/watch.
- **IV outliers:** clean nothing-found (scan dominated by same-day-expired deep-ITM exercise mechanics; forward-dated residue fails the liquidity floor).
- **Notable unwinds (`uw oi decrease-with-volume`):** IGV Jan-27 80P −128.9k ($35.9M software hedge OFF — mildly constructive); SMH 07-02 600P −56.8k + 07-17 540P −49.4k (semis event-hedge cleanup); VIX Aug 55C −48.9k (tail-hedge unwind into NFP — a mild complacency tell).

---

## §6 Risk & Sizing (Phase 2d) — 2026-07-01

**Top line:** EMPTY CONVICTION BOOK — zero of 28 scored names clear raw ≥ 3 (top: MSTR/TSM/TLT at raw 2, all DROP → skip). Regime TRANSITIONAL (trend leg UPTREND: SPY 745.76 > SMA20 741.55 > SMA50 736.61, but flow breadth 37.1% bullish); VRP FAIR/negative (SPY −0.015 / QQQ −0.043 — vol cheap vs realised: long-vol favored; all four vol_sell watch structures GS/PEP/IWM/SPX are VRP-contradicted); front-end IV SPY 0.986 FLAT (no systemic panic) but QQQ 1.155 BACKWARDATION > 1.10 — panic gate fires on QQQ (dated NFP event premium, not systemic panic); DTE share BALANCED (0DTE 34.1%) — no horizon reweight. The no-trade read is coherent: TRANSITIONAL tape, NFP pre-open next session, holiday-closed Friday, 20/28 names on MIXED 30d flow labels. Nothing is sized tonight; the gate stack below is documentation for the calibration loop.

**Macro headline & forward calendar:** curve normal (+0.31); core CPI 2.96% vs core PCE 3.41%; unemployment 4.3% / payrolls +172k; 10Y 4.44% flat; USD strengthening; FF 3.63%. Tier-1 in-horizon binaries (T+0 = 2026-07-01 report date, TRADING-day counts, 2026-07-03 closed): **NFP 2026-07-02 pre-open = T+1**; CPI 2026-07-14 = T+8; PPI 2026-07-15 (not Tier-1); **TSM earnings CONFIRMED 2026-07-15 = T+9**; FOMC 2026-07-28 = T+18; MSTR earnings 2026-07-29 = T+19. Breadth (fz advisory): 299 adv / 204 dec, 59.4% green, divergence_flag false.

**Correlation clusters (mechanical thresholds, 30d lookback):** one cluster — `semis_tech_beta_cluster` {QQQ, SMH, TSM, INTC, MU}: QQQ/SMH 0.938, SMH/INTC 0.847, SMH/MU 0.846, TSM/SMH 0.836, TSM/QQQ 0.825, QQQ/MU 0.781, QQQ/INTC 0.749 — all ≥ 0.70, one position. Kept by quant raw_score: **TSM (raw 2)** — itself VETO'd to watch-only, so the entire cluster is watch-only in practice; −1 tier documented on QQQ (raw 1), SMH (−1), INTC (0), MU (0). Direction-mixed cluster (QQQ long vs TSM/SMH/INTC short, MU two-way vol): same factor, partially offsetting signs — still one bet for book construction. Soft-watch pairs (0.60–0.70, NO penalty, monitor): TSM/INTC 0.696, TSM/MU 0.642, INTC/MU 0.634. No pair ≥ 0.60 surfaced for MSTR, TLT, CAR, BSX, IGV — IGV's absence is a data caveat (tool returned sector Unknown for all 10 symbols); do not read IGV as uncorrelated with QQQ.

**Sector rotation:** no rotation regime; intra-Tech semis→software split only. Tech GICS bullish persistence 1.0 is ADVERSE to the TSM short (mechanical −1 documented, moot under VETO). IGV long carries the wrapper-vs-holdings divergence (+$118M ETF inflow vs −$838M single-name software outflow; MSFT/NOW/PLTR 30d flow all bearish) — prose caution, no mechanical deduction (no bearish-direction persistence ≥ 0.6 against the wrapper). MSFT/META mega-DP distribution flags (buy_ratio 0.104/0.136) vs bullish day premium remain the day's clearest cross-basis warning.

**Fundamentals verdicts (2b):** MSTR **CONFIRM** (insider selling MSPR −23.8 into the decline, PT cuts, BTC < 200wk MA, $1.25B sell-framework doctrine break; carried key_risks: PB 0.855 + $2B board-approved buyback = mechanical bid, beta 3.58 crowded-short squeeze, CEO STRC preferred buy counter-tell, earnings 07-29 at horizon tail). TSM **VETO → watch-only** (mechanical 2-of-3 contradiction: 4/4 beat streak + fortress growth/margins — rev +30.7%, net margin 47%, ROE 36.9%; the bearish paper reads as hedging/collaring a winning long base into the confirmed 07-15 print 14d out; insider MSPR −93.2 is the lone dissenting leg). TLT / IGV / QQQ **NA** (ETFs — NA never penalizes).

**Sizing table** (quant pre-risk → gate stack → final; all 9 gate verdicts per call serialized to `gate_verdicts`, residual pairs to `debate_residuals`):

| Ticker | Dir | Class | WR (n) | Excess | Pre-risk | Gates that fire (documented — all moot at skip) | Final |
|---|---|---|---|---|---|---|---|
| MSTR | short | bearish_flow | 0.540 (137) | +0.146 | skip | event_risk −1 (NFP 2026-07-02 = T+1 from 07-01; own earnings 07-29 = T+19 stacks at horizon tail); debate −1 (bear 0.75 ≥ bull 0.65); rubric_regime cap half; 06-27 register: no short selection-alpha sizing | **skip (watch)** |
| TSM | short | bearish_flow | 0.540 (137) | +0.146 | skip | **fundamentals VETO → watch-only**; sector −1 (Tech bullish persistence 1.0 adverse to short); event_risk −1 (own earnings 2026-07-15 = T+9 + NFP = T+1, stacked); debate −1 (bear 0.85 ≥ bull 0.55); cluster kept-member no-op; rubric cap half — all sizing-moot under VETO | **watch-only (VETO)** |
| TLT | short | multileg_directional | NA(substrate) | n/a | skip | debate −1 (bear 0.75 ≥ bull 0.55); event_risk EXEMPT (defined-risk Aug-21 83/79 put vertical spanning NFP/CPI/FOMC IS the event play); rubric cap half | **skip (watch)** |
| IGV | long | bullish_flow | 0.486 (138) | **−0.073 `beta`** | skip | event_risk −1 (NFP = T+1, undefined-risk ETF delta); debate −1 (bear 0.65 ≥ bull 0.55); sub-0.50 WR floor (starter/skip); rubric cap half | **skip (watch)** |
| QQQ | long | multileg_directional | NA(substrate) | n/a | skip | panic −1 (QQQ front_end_iv_ratio 1.155 > 1.10); cluster −1 (semis_tech_beta member, TSM raw 2 kept); event_risk −1 (NFP = T+1; exempt only if expressed via the defined-risk Mar-27 795/815 vertical); debate −1 (bear 0.75 ≥ bull 0.65); rubric cap half | **skip (watch)** |

Floor holds at skip; no gate resurrects a DROP. **The debate cut all five** (bear ≥ bull on every top-5 name — a clean sweep). IGV is the only `beta`-flagged row (−7.3pp vs same-window SPY-long: the wrapper long merely rides the tape). MSTR/TSM's +14.6pp is class-level short excess for bearish_flow this window — NOT selection alpha; the 2026-06-27 register stands (no short selection-alpha sizing; C2 binds at half for any future promotion off this class).

**Debate residuals (C43 serialization — mandatory pair):** MSTR {bull 0.65, bear 0.75}; TSM {bull 0.55, bear 0.85}; TLT {bull 0.55, bear 0.75}; IGV {bull 0.55, bear 0.65}; QQQ {bull 0.65, bear 0.75}. Strongest unrefuted bear points: MSTR — the −$601M stack is expressed only in Sep far-OTM puts (tenor refuses the 1–4wk window); TSM — 25Δ skew NORMAL, not TAIL_HEDGING (iv-100 bid ≠ Taiwan-tail print); TLT — 82.76 breakeven sits below the 57-day low with 10Y flat; IGV — single-name software outflow dwarfs the wrapper inflow; QQQ — the $237M Mar-27 vertical is volume≈OI (likely roll), zero top-20 OI footprint.

**Adverse-flow exits — `conviction_2026-06-30` carry (SNDK, BMY, DELL, EWZ, XLB; all were watch_only, so exits are watch-hygiene, not P&L actions):**
- **SNDK (carried long, LOW) — EXIT CANDIDATE (strongest):** flow flipped bearish (day net −$49.9M, P/C 1.065, +33.5k OI put-heavy builds), IV rank 85.9, $81.3M single DP block on 22,997 DP trades; today's quant confirms "direction flip in progress."
- **DELL (carried long) — EXIT CANDIDATE:** bearish net flow −$11.6M, IV rank 92.2 (re-entry expensive), $85.1M single DP print, OI +42.6k.
- **EWZ (carried long) — EXIT CANDIDATE (moderate):** bearish flow −$8.3M, OI shift +68,011 (high-severity), $24.0M DP block.
- **BMY (carried vol_long) — ON-THESIS:** bullish tape, P/C 0.21, OI +10.0k, IV rank 53 stable. Hold on watch.
- **XLB (carried short) — STALE (scan catch, no hard alert):** flow still bearish-aligned but the options tape decayed to volume_ratio 0.18; off-thesis by decay — drop from carry.
- fz drift tripwire (8b): cold-start — single snapshots only on all 5 carried names; nothing surfaced (advisory, silent-skip honored).

**Hedge sleeve:** none required — the conviction book is empty (net delta 0.00; the ≥0.6 skew rule is n/a). Desk carry note into NFP T+1 pre-open + closed Friday: do NOT buy front-end index vol (QQQ FE 1.155 shows the NFP premium already priced — institutions are selling that front event premium) and do NOT sell it either (negative VRP contradicts short-vol — the same gate pinning GS/PEP/IWM/SPX to watch). If the desk carries legacy long-beta from outside this book, the tape-consistent expression is Q3-tenor defined-risk downside echoing the institutional prints (IWM Jul-31 290P, HYG Feb-27 76/70 put verticals, TLT tails), sized starter — never front-week into the print.

**Watchlist write-back:** none — empty conviction book (no name ≥ raw 3). Writing DROP-tier names into `conviction_2026-07-01` would poison tomorrow's correlation/adverse-flow loop with non-positions; the honest record is the empty write. `conviction_2026-06-30` remains the live carry until it ages out of the 7-day window.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Empty. No name reached LOW (≥3), let alone MEDIUM (≥7).** The top of the raw board with full audit context (all DROP/skip, documented for the calibration loop):

**Expectancy lens (advisory — C31, from /calibration-audit 2026-06-27, n=23 closed):** HIGH mean P&L −2.44% / payoff 0.72 · MEDIUM +0.10% / 0.95 · LOW −0.73% / 1.00 · DROP −3.70% / 0.57. The tier inversion (HIGH < MEDIUM on both hit-rate and expectancy) is why the freeze + half-cap stands. `[advisory — expectancy is not yet a live sizing axis]`

| Ticker | Dir | Raw | Components (agent · tool) | Class | WR (n, source) | Excess | Fund. | Debate (bull/bear) | Final |
|---|---|---|---|---|---|---|---|---|---|
| MSTR | short | 2 | +1 cum-flow −$601M (quant · cumulative-premium-flow), +1 OI build 5d (sweep-tracker · oi-trend) | bearish_flow | 0.540 (137, clean) | +0.146 | CONFIRM | 0.65 / 0.75 **cut** | skip |
| TSM | short | 2 | +1 cum-flow −$291M (quant), +1 backwardation VRP-aligned (vol-surface · iv-term-structure) | bearish_flow | 0.540 (137, clean) | +0.146 | **VETO** | 0.55 / 0.85 **cut** | skip (veto) |
| TLT | short | 2 | +2 multileg 83/79 put vertical (multileg · hot-chains multileg) | multileg_directional | NA(substrate) | — | NA | 0.55 / 0.75 **cut** | skip |
| IGV | long | 1 | +1 cum-flow +$118M (sector-rotation · cumulative-premium-flow) | bullish_flow | 0.486 (138, clean) — **< 0.50 floor** | −0.073 | NA | 0.55 / 0.65 **cut** | skip |
| QQQ | long | 1 | +2 multileg Mar-27 vertical, +0 vanna (mechanized bar failed), −1 flow_conflict_lite | multileg_directional | NA(substrate) | — | NA | 0.65 / 0.75 **cut** | skip |

Full gate stacks per name in §6. Notable deductions on the rest of the board: MSFT −3 flow_conflict (30d −$597M vs the sector-long flag, 6.1× median — mechanically agrees with the mega-DP distribution read, buy_ratio 0.104 on $1.94B, and the Tier-1 470P); PLTR −3 (30d −$241M AND 90d −$257M against the leader thesis); META −3 (30d −$102M, 90d −$592M; DP buy_ratio 0.136). The sector-long lane was the refuted side of the day.

**Deep-dive hand-off:** skipped — no HIGH-tier names (Step 8.5 no-edge rule).

### Conviction scoring rubric (frozen version 2026-06-12, embedded verbatim)

```
Daily conviction score = Σ:
  +1  dealer-positioning-strategist flags a MECHANIZED DEX flip or vanna-squeeze setup in trade direction — the trigger must be a verified SIGN CHANGE, not a level: sign(net_dex) on the latest session opposite to ≥3 consecutive prior sessions, read from dated `uw options-structure dex --date` calls (≥4 to verify the prior-session sign run; ~11 for the trailing-median floor), with |net_dex| on the flip day ≥ 0.25× the trailing-10-session median |net_dex|; the evidence string must cite both dated values. Vanna disjunct additionally requires a dated VIX source (Yahoo chart API ^VIX) for the falling-VIX leg — no out-of-band VIX fills.
  +3  3+ aligned signals in accumulation-hunter (DP + OI + uw oi smart-positioning, uw dark-pool block-stratified institutional-tier confirmed) — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms (sign aligned AND |cum_flow_30d| ≥ $50M); else halved (floored) +3→+1.
  +1  multi-day OI build (uw historical oi-trend BUILDING, --days ≥ 5)
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70 — CONDITIONAL: only when dominant_signal_class == leap_directional; else 0.
  +1  uw historical cumulative-premium-flow net directional accretion in trade direction (30d) — INTENT-SCREENED (C28 distribution_flag; ex-div deep-ITM dividend-capture check). Screen failed or unevaluated on a flagged name → 0.
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector — CONDITIONAL: (a) persistence ≥ 0.6 AND (b) cum_flow_30d aligned AND (c) |cum_flow_30d| ≥ $50M. Default 0.
  +1  in earnings-scout BUY VOL or SELL VOL
  +2  in multileg-strategist with directional structure (term-structure-anchored play type)
  +1  in vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner flags as overcrowded long with rising pc-ratio-zscore (VRP positive) — informed-flow continuation penalty; requires multi-date z trajectory; routed via C13, never double-counts with a flow read.
  -3  flow_conflict — mechanical: 30d cum-flow clearly opposite dominant_signal_class (sign flip + magnitude > union-median |cum_flow_30d|, or explicit OPPOSITE label)
  -1  flow_conflict_lite — MIXED 30d read (signed sum near zero, or aligned but bottom-quartile magnitude). Mutually exclusive with flow_conflict.
  # TIER GATES (2d, not score components): correlation cluster ≥0.70 → −1 TIER; regime conflict → −1 TIER.
Tiers: ≥9 HIGH (full, subject to 3-of-4 LB gate + win-rate gate) · 7–8 MEDIUM (half) · 3–6 LOW (starter/watch) · ≤2 drop.
Out-of-regime guard (P0.6): all sizes capped at half until a /calibration-audit records ≥30 resolved post-2026-06-12 calls and re-validates the tiers.
```

---

## 8. Watch-only — single signal, no confluence

Journaling only, NOT trade entries. Sourced from one agent each (or direction-conflicted), failed the ≥2-agent confluence gate:

| Ticker | Dir | Source agent | One-line signal | Raw |
|---|---|---|---|---|
| JPM | long | accumulation-hunter | mega DP buy_ratio 1.00 / $2.02B, conviction 47.6 < 50 — re-test 07-02 | 1 |
| DLO | long | multileg | Dec 13/17 call vertical $10.7M + funnel confluence-6 | 1 |
| WULF | long | multileg | Jul-17 put-credit ladder + Sep 22C buys | 1 |
| ACHC | long | accumulation-hunter | 5/5 OI build + SF 23.6% squeeze context; retail-scale DP | 0 |
| STLA | long LEAP | leap-radar | 7-of-8 gates, Jan-27 7C 6.1× build; floor-fragile $5.81 | 0 |
| CAR | short | contrarian | P/C z +4.75, 133% 1-DTE IV — event structure, no touch | 1 |
| BSX | short | contrarian | P/C z +6.84 + Tier-1 whale put; informed continuation, 30d flow opposes | −1 |
| INTC | short | sweep-tracker | 4/5 sweep persistence, −$310M 30d, arb-polluted aggregates | 0 |
| MSTR | short | sweep-tracker | top raw score; fundamentals CONFIRM; debate cut on tenor/squeeze path | 2 |
| TSM | short | sector-rotation | fundamentals VETO — hedging of a winning long base | 2 |
| TLT | short | multileg | Aug 83/79 vertical, 3 catalysts inside expiry; breakeven below 57d low | 2 |
| IGV | long | sector-rotation | +$118M wrapper inflow vs −$838M constituent outflow | 1 |
| QQQ | long | dealer+multileg | confluence-pass but raw 1; vanna squeeze armed, post-NFP re-look | 1 |
| GS / PEP | vol_sell | earnings-scout | event calendars (§5), enter post-NFP / post-07-10 | 1 |
| SNDK | — | sweep-tracker | 5/5 bullish window under attack, direction flip in progress | 0 |
| MU | vol context | sweep-tracker | $8.25B 5-session two-way battle, MIXED — epicenter, no direction | 0 |
| TSLA | short | sweep-tracker | 5/5 bearish $5.19B but hedge character, 90d +$790M opposes | −1 |
| HYG | short LEAP | multileg | Feb-27 76/70 put vertical — credit hedge tell, not alpha | 1 |
| XLE | short LEAP | leap-radar | +40k long-dated puts ~$17.1M — producer-hedge ambiguous | — |
| NBIS / TER / LRCX / KLAC | vol watch | vol-surface | rank-100 complex; triggers in §5 | 0 |
| ASML | vol watch | earnings+vol-surface | kink real, both agents SKIP; revisit ≥07-10 | 0 |
| SPX | vol context | multileg | −$988M headline is sold Sep straddle + packages, NOT directional panic | 0 |
| IWM | vol context | multileg | Jul-17 put spreads SOLD into CPI kink + Jul-31 290P hedge bought | 0 |

Floor exclusions: HTZ (price $2.17 + jelly roll), EWT (thin, fail-closed), AEHR (uncertain, fail-closed), FCEL (< $5), micro-cap funnel names (BEX/KSTR/RAM/MULL/KORU/CIA).
