# Daily Market Analysis — 2026-08-04

## Executive Summary

- **Regime + GEX state:** TRANSITIONAL (trend UPTREND). SPY 771.33 **+1.80%**, QQQ 723.85 **+3.40%**, IWM +1.85%, RSP +1.44%; SMH +5.55%, XLK +4.98%. VIX 16.50 **+4.04% — vol bid INTO the rally**. Equity breadth 71.4% green, but options-flow breadth only **41.1% bullish**. Both index gamma books are long-gamma but **freshly flipped** (SPY 3 sessions, QQQ 2). Sector lean: Technology is the only C55-clean rotating-in sector.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`.
- **Next-session GEX (SPY/QQQ):** SPY POSITIVE · ZGL 767.91 (reliable) · call wall 775 (+0.37%) / put wall 750 (−2.87%) → call-skewed condor, not a symmetric fly. QQQ POSITIVE · ZGL 711.88 (reliable) · call wall 730 (+0.82%) / **no put wall anywhere in the grid** → wider wings, smaller size. Advisory, see §2.
- **Top swing build:** **NONE.** The post-gate book is empty for the 20th consecutive session.
- **Top LEAP candidate:** **NONE.** Every candidate failed the 90d cumulative-premium-flow accretion gate.
- **Biggest risk:** the `AI_semis_cluster` — AVGO / LRCX / NBIS are one position (LRCX/NBIS **0.748**, AVGO/LRCX **0.702**), inside a wider complex running LRCX/AMAT 0.943, MU/AMAT 0.885, NBIS/CRWV 0.880. Hedge sleeve is advisory only because net delta is zero.

**The day in one line:** the tape melted up, and the institutions who own it spent the session buying insurance — ~$255M of multileg **debit** concentrated in downside convexity against ~$2.6M of credit, 76% of the whale tape **closing** rather than opening, and VIX up 4% on a +1.8% SPY day. Not one AI/semis melt-up name appears anywhere in the multileg screen.

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL — mixed signals, reduce position size, wait for clarity**; trend **UPTREND**. SPY 771.33, above the 20SMA (747.20) and 50SMA (745.89), +2.67% over 30d, −0.27% from the 90d high. Flow breadth: 2,585 bullish vs 3,701 bearish tickers = **41.1% bullish**. Guidance: *"Half position sizes. Favor defined-risk strategies. Iron condors in range."*

**The tape framing matters more than the label today.** 1-day breadth is genuinely broad (IWM +1.85%, RSP +1.44%, 71.4% of S&P names green, median +0.88%) — but the **week** is heavily cap-weighted: SPY +4.11% 5d vs RSP **+1.17%** 5d. Today was broad; the week was a mega-cap-tech event.

| Index | Spot | Zero-gamma | Total GEX | Regime | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 772.17 | 767.91 (reliable) | +$1.104B | POSITIVE | 775 (+0.37%) | 750 (−2.87%) |
| QQQ | 724.09 | 711.88 (reliable) | +$623.7M | POSITIVE | 730 (+0.82%) | **none in grid** (soft floor 710, −1.95%) |
| IWM | — | — | — | **artifact — excluded** | — | — |

IWM's GEX regime flipped POSITIVE→FULLY_NEGATIVE→POSITIVE→NEGATIVE across four sessions with a `zgl_delta` of 155.19. That is the known **ZGL-grid artifact class**, not a signal, and it is excluded from every read below.

**DTE volume share:** 0DTE 26.2% · weeklies 30.9% · monthlies 29.4% · LEAPs 3.6% → `BALANCED`. Neither retail- nor institution-dominated; no uniform conviction adjustment applies.

**VRP:** SPY `FAIR` (iv30 13.94% vs realised 14.14%, VRP −0.002). QQQ **NEGATIVE** (iv30 22.97% vs realised **27.32%**, VRP −0.0435) — IV sits materially *below* realised on the Nasdaq complex. Premium is cheap there; long-premium structures are correctly signed and naked short-vol is the wrong lean.

**Macro backdrop** (`scripts/fred_macro.py`): curve normal at **+43bp** (10Y 4.70% / 2Y 4.25%); core CPI **2.81%** YoY but core PCE still **3.29%**; unemployment 4.2% with payrolls decelerating to **+57k**; 10Y **rising +21bp/30d**; USD weakening; fed funds 3.63%. A rising long end underneath a long-duration tech melt-up is a fragile combination.

**Forward event risk:**

| Event | Date | Impact | Trading days out |
|---|---|---|---|
| Initial jobless claims | 2026-08-06 | MEDIUM | 2 |
| **Employment Situation / NFP (July)** | **2026-08-07** | **HIGH** | **3** |
| **CPI (July)** | **2026-08-12** | **HIGH** | **6** |
| PPI (July, est.) | 2026-08-13 | MEDIUM | 7 |
| Core PCE (July, est.) | 2026-08-28 | HIGH | 17 |
| FOMC + SEP | 2026-09-16 | HIGH | 30 |

NFP at T+3 sits inside every swing horizon on the board.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** This is the EOD dealer-gamma book — built from open interest that persists overnight — read forward as the *prior* for the next open. Prose-only, **0 rubric points**, no backtested predictive claim. Predictive validation lives in `/weekly-analysis`'s rolling §2 backtest. Scope is **SPY and QQQ only**.

**SPY** — spot 772.17, ZGL **767.91** (0.55% below spot, reliable), regime **POSITIVE**, total GEX **+$1.104B**, call wall **775**, put wall **750**. Regime is on its **3rd session holding positive** (flipped 07-31), and the ZGL has walked *up* with spot every session — 746.93 → 756.06 → 767.91, a +21pt climb in three days. That is a book chasing price, not a stabilised one. The call wall sits only **+0.37%** away after a +1.8%/+4.1%(5d) run — a shallow ceiling that fresh 0DTE call buying at the open could push through, flipping local hedging flow from suppressive to accelerant.
→ **Structure bias:** asymmetric book (tight call wall, far put wall) favours a **call-skewed iron condor / short call spread anchored 772–775** with the put wing further out near 750–755. A symmetric ATM fly risks pin-break on the call side.

**QQQ** — spot 724.09, ZGL **711.88** (1.69% below spot, reliable), regime **POSITIVE**, total GEX **+$623.7M**, call wall **730**. **There is no put wall: the entire visible per-strike grid (703–745) is net positive gamma.** Nearest floor is the largest positive-GEX strike below spot, 710 (−1.95%) — a soft support, not a hard wall. The regime is **very fresh** — flipped POSITIVE only on 08-03, having been FULLY_NEGATIVE as recently as 07-31, with the ZGL jumping 699.22 → 711.88 in one session.
→ **Structure bias:** wider-wing condor (710–730) over a tight fly. A 2-day-old long-gamma flip sitting on top of *negative* VRP is a fragile pin — treat any 0DTE short-vol here as smaller size and wider wings than SPY.

**Cross-index tension worth stating:** VIX rose **+4.04%** on a day SPY closed **+1.80%**, while both books read nominally long-gamma (vol-suppressive). Two consistent readings: the vol bid is event-driven (NFP at T+3) rather than a gamma-regime signal; and both regimes are freshly flipped and still chasing spot, so neither may yet be exerting real hedging suppression despite the POSITIVE tag.

**Mandatory caveats:**
- **EOD is a prior, not a target.** Fresh 0DTE OI floods in during the first 30–60 minutes and recomputes the ZGL and walls — especially after a fast melt-up. QQQ's next-day expiry already carries $3.36B of premium and the 08-07 (NFP) expiry $6.69B, so near-dated tenors are far from thin.
- **ZGL reliability.** Both ZGLs sit within 2% of spot and are trusted. QQQ's "no negative-GEX strike anywhere in grid" pattern is atypical for a book this fresh and is flagged for intraday sanity-check.
- **Gap risk voids the prior.** NFP is 3 sessions out; overnight macro can gap spot through the walls before any hedging mechanic engages.
- **Tooling limit.** `gex --dte-max 1` errors, so this is the standing **0–45 DTE** book — a proxy for the next-session prior, not the isolated D+1 expiry.
- **ETF book**, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup

> The GEX walls above are a **map, not a pin** — wall-as-magnet backtested NO_GO, as did every directional signal. What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, not a guaranteed edge.

**★ Lead with this, not the headline win-rate: `vol_state` is LOW on both indices, and the LOW-VIX tercile mean PnL is NEGATIVE before costs — SPY −0.049%, QQQ −0.014%.** Net of the assumed 0.10% round-trip, **this lane is a loser at today's VIX of 16.50.** The 88.3%/83.3% gross win rates are the wrong metric for a negatively-skewed short-vol strategy (Vilkov 2024: an unconditional 0DTE condor flips to negative net Sharpe once costs are charged).

| | SPY | QQQ |
|---|---|---|
| `sell_premium` / `vol_state` | true / **LOW** | true / **LOW** |
| VIX · implied move · expected range | 16.5 · 0.89% · 0.83% | 16.5 · 1.83% · 1.45% |
| `size_scalar` | 0.5 | **0.25** |
| Suggested structure | iron fly / short straddle @ 772.3, wings ±0.83% | iron fly / short straddle @ 722.25, wings ±1.45% |
| Backtest (n=60) | win 88.3%, gross **+0.223%**, **net +0.123%**, worst −1.40% | win 83.3%, gross +0.341%, **net +0.241%**, worst **−2.453%** |
| `caution` | none | **front-end backwardation (0DTE IV 1.76× VIX) — event/gap risk; half size** |

`pnl_basis`: percent-of-underlying-spot-notional, **GROSS** — not premium-collected, not margin-relative. Entry rule for both: enter at/after the open once the gap resolves, hold to the close, **never carry overnight**. If it gaps beyond the wings, stand aside. **SPY ≈ SPX** (validated identical); **QQQ is weaker** (Nasdaq index book unavailable) — lower confidence. Tail caveat: the validation sample contains **no vol shock**, so the short-vol left tail is UNSAMPLED. Promotion bar unchanged: this lane stays advisory permanently until a vol-shock day enters the sample AND net expectancy clears a tail-aware bar.

**Desk read: stand aside on both.** Negative expected value in the LOW-VIX tercile, NFP at T+3, and a QQQ front end in backwardation is not a premium-selling configuration.

## 2a-bis. Swing Dealer Positioning (1–4 weeks)

**Two script-verified mechanized DEX sign flips today — ARM and LRCX.** Both are the only names eligible for the +1 rubric line.

| | ARM | LRCX |
|---|---|---|
| Flip | 08-03 **−71,175,320** → 08-04 **+899,938,432** | 08-03 **−123,479,835** → 08-04 **+631,525,734** |
| Prior run | 7 sessions all negative | 7 sessions all negative |
| Magnitude vs floor | 899.9M vs 49.7M = **18.1×** | 631.5M vs 24.6M = **25.7×** |
| `whipsaw_warning` | **false** (3 sign changes) | **TRUE — 5 sign changes** |
| Per-strike check | top strike 25.8% of \|GEX\| — no artifact | max 11.1% — no artifact |
| GEX regime | NEGATIVE (short-gamma, amplifying) | POSITIVE (flipped 08-03) |

SPY, QQQ, AMD and NBIS all show a genuine multi-day DEX turn from negative to positive, but the flip occurred **2–4 sessions ago** — the mechanized latest-session rule correctly excludes them. Indices: SPY DEX +99.87B improving monotonically (−75.2B → +99.9B over 5 sessions), front-end ratio 0.79 CONTANGO, swing bias LONG; QQQ +68.16B, ratio 0.914, LONG; IWM +10.68B but GEX artifact-compromised, FLAT/weak-long at low confidence.

**No vanna squeeze exists anywhere.** All 11 books returned **negative `net_vanna` = call-heavy**, and the falling-VIX leg broke today (VIX +4.04% after three consecutive down sessions: 20.66 → 17.09 → 15.99 → 15.86 → 16.50). The setup is disqualified on book side alone, independent of the VIX reversal.

**Discordant note:** front-end IV is in backwardation above the 1.10 panic threshold on **6 of 8 single names** (AMAT 1.224, AMD 1.217, NBIS 1.212, ARM 1.163, PLTR 1.152, LRCX 1.150, MU 1.122) even as GEX/DEX turn supportive. The market is still pricing elevated near-term event risk — NFP sits inside every one of those windows. **AVGO at 0.902 CONTANGO is the sole no-panic front end in the complex.**

**GEX artifact caution:** AVGO, DELL, IWM and MU all show regime flipping nearly every session with implausible ZGL jumps (AVGO 400↔164). This extends the documented ZGL-grid artifact class — previously SPY/QQQ/IWM/MU — to **AVGO and DELL**. Those regime flags are not tradable and are excluded throughout.

## 2b. Sector Rotation

**Rotation regime call: `no_change`** — a tech-concentration melt-up, not a cross-sector rotation. `regime_confidence: low` (only one side populated).

Direction is read off the **NETTED** `uw risk market-regime.sector_rotation` per C55. `sector-flow` and `sector-flow-persistence` are one **gross-turnover** source and cannot express direction — and today proves it: **all 11 sectors are positive in gross.**

| Sector | Netted ($) | Gross ($) | Persistence | Agreement | Verdict |
|---|---|---|---|---|---|
| **Technology** | **+839.2M** | +7.58B | **1.0** | **agree** | **rotating_in — high conviction** |
| Communication Services | −102.8M | +1.38B | 0.8 | **disagree** | watch_only |
| Consumer Cyclical | −63.1M | +742M | 0.6 | **disagree** | watch_only |
| Healthcare | −27.6M | +168M | 1.0 | **disagree** | watch_only |
| Industrials | +41.0M | +441M | 0.6 | nominal agree, fails market-relative bar | **downgraded to watch_only** |
| Basic Materials | +2.6M | +54.1M | 1.0 | nominal agree | marginal — noise-level magnitude |

Industrials was downgraded despite nominal agreement: its persistence (0.6) falls outside the top-third tie group (six sectors tie at 1.0), its flow was negative on 3 of the last 5 sessions before flipping only on 08-03/08-04, and its representative ETF **XLI contradicts the netted print** — 5-day options net_flow −$1.43M bearish, largest sweep a $1.6M Sept 166 **put** buy.

**Technology single-name leaders** (persistence 1.00 for all): PLTR (+$191.0M 30d, aligned), MSFT (+$368.7M, aligned), AVGO (+$98.6M, aligned) pass all three conditional gates. **MU (−$165.5M) and INTC (−$1.01B) are strongly misaligned** — today's pop runs against a 30-day net-bearish backdrop; that is short-covering or late momentum, not accumulation.

**ETF flow tape (advisory — adds no rubric points):**

| ETF | Net premium (5d) | Persistence | DP positioning | Options urgency | GICS agreement |
|---|---|---|---|---|---|
| **SMH** | **+$130.1M** | BULLISH | large ask-side blocks (+7.46, +3.9 vs mid) | mixed: $10.3M Sep 600C **and** $10.4M 2027 550P hedge | agree (→Tech) |
| XOP | +$13.1M | BULLISH | near mid, no skew | **contradicts label** — $15.6M Oct 165P + $5.1M Oct 150P, bid-side | n/a |
| EWY | +$11.6M | MIXED | net positive tilt | call-dominant | n/a |
| IGV | +$11.3M | BULLISH | — | — | agree (→Tech) |
| XLK | +$4.7M | BULLISH | — | — | agree (→Tech) |
| **GDX** | **−$15.7M** | BEARISH | prints near/above ask | **heavy call buying — contradicts its own bearish label** | conflicted |
| **XLI** | **−$1.43M** | BEARISH | 250k block below mid; one print shows an **anomalous NBBO spread (bid 169.81 / ask 187.50)** — stale-quote artifact | put-dominant | **disagrees with netted Industrials-IN** |

SMH + XLK + IGV agreeing with GICS Technology reinforces the single high-conviction rotation call. GDX and XLI both carry internal conflicts between their own net-flow label and their own urgency tell — noise, not signal.

---

## 3. Swing Setups (1–6 weeks)

**Post-gate book: EMPTY.** Three names reached LOW tier at starter size pre-risk; all three gate to skip. Each dies on **three or more independent gates**, not on any single marginal call.

### 3a. Long swings (regime-aligned)

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **LRCX** | 4 (LOW) | Swing long off a script-verified mechanized DEX sign flip; cleanest earnings beat streak on the board (4/4, accelerating); earnings 77d out | *not entered* | **DEX-reversal rule** — the thesis *is* the flip, so any single-session net-DEX flip back negative kills it (whipsaw already TRUE, 5 sign changes). % fallback: close < 301.85 (−5%) | **SKIP → watch_only** |
| **AVGO** | 4 (LOW) | Technology sector-leader long — the only name clearing all three conditional gates on the netted C55 source; only no-panic front end in the complex | *not entered* | % rule: close < 397.25 (−5%) or 30d cum-flow flips negative. DEX unusable (ZGL-grid artifact) | **SKIP → watch_only** |
| **NBIS** | 3 (LOW) | Bullish-flow long; +$264.7M 30d accretion, 2nd-largest aligned in the union; 30.22% short float on a 202M float | *not entered* | Second consecutive session of bearish top-ticket skew, or close < 214.45 (−5%). **Hard rule: nothing held into 08-12** | **SKIP → watch_only** |

**Why the invalidations are percentage- and DEX-based rather than dark-pool levels:** the C34 discipline prefers a real institutional DP level, but `accumulation-hunter` returned **zero qualifying names** today, so no DP shelf exists to anchor to. That absence is itself the finding.

**Deep-dive corroboration (Step 6) — all three cut against the long thesis:**
- **LRCX:** **4 of the top 5 OI builds are PUTS** — 270617P200 (+2,203), 260807P265 (+1,036), 260918P330 (+1,004), 260821P290 (+937). Only one call build (260828C360). The +1 OI point the rubric awarded is being driven by put accumulation. Implied move 6.96%, iv30d 87.6%.
- **NBIS:** **today's `flow_direction` is BEARISH** — net_flow −$15.8M, P/C 1.556, bearish premium $114.3M > bullish $98.5M. Independent corroboration of sweep-tracker's reversal from a different tool. Implied move 10.13%, iv30d 139.3%.
- **AVGO:** largest single OI build is a **put** — 260911P295 (+6,574, 38 DTE). Flow bullish 9 of 10 days so the trend is intact, but the marginal build is downside. Implied move 4.05%.

**Sweeps (informational, 0 rubric points).** Persistence-first ledger: **INTC** is the one clean confirming signal — 4/5-session bullish persistence, $652.5M 5d premium, largest ticket $112.65M call/ask at the 70 strike, and **99% opening-dominant** (top contract ΔOI 21,654 on volume 21,832). ORCL is a weaker second (3/5, but only 34% opening-dominant). Against that: **SMH carries 3/5 bearish persistence strongly corroborated today — aggressive far-OTM put buying into a +5.55% day, `smart-money-flow` ask/bid ratio 5,003× on the 395P.** NBIS shows a live reversal. AMD has the highest raw persistence (5/5) but its own tape is a genuine coin flip and should not be read as directional.

**Artifact:** the SPX/SPXW "bearish" persistence is a **multi-leg collar complex mis-counted as directional single-leg sweep premium** — size- and timestamp-matched legs (9,200 @ 18:02:18 across a 7000C/8000P pair; 6,700 @ 18:31:20; 5,100+4,500 @ 20:01:52), tenors to Dec-2031, call deltas 0.72–0.94. **SPX/SPXW sweep-persistence is not usable this session.** Distinct from the known cross-name twin-print NBBO artifact.

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only` (2026-08-01 P0 #1).** This is **routing, not suppression** — theses are generated, scored and serialized so the counterfactual keeps resolving; none are sized.

- **IWM — the cleanest event-anchored structure of the day.** Aug-21 put debit vertical, +P295 (dte17) 53,643 @ $2.985 against the P282–279 zone, ~$10.3M debit, width $13, payoff **6.76:1**. **Highest repeat count in the book: 5 of 5 sessions**, rolled *up* daily as IWM rallied (277→278→279→282→295), with OI confirming every session — including an explicitly NFP-dated Aug-07 285/275 spread at +49,960/+49,203 on 08-03. The dte17 tenor spans **both NFP and CPI**. Term structure BACKWARDATION unflipped. This is the one name where the structural read and `uw playbook batch-scan` agree. → `watch_only`.
- **HYG — credit tail.** Dec-18 P75, 52,000 of 69,561 volume. Term structure: raw CONTANGO → hygiene **KINKED @ 09-18** (FOMC-adjacent, flipped). Back end ramps 0.0499@73d → **0.1114@136d against rv20 of 2.9%** — Dec IV is roughly **4× realised**. The market is explicitly pricing Q4 credit stress. Partner leg inferred, not observed. → `watch_only`.
- **GOOGL — informed-flow caution, not a fade.** Price +9.1%/20d against a Tier-2 opening put (375P, 09-04, size/OI 12.2). Per Pan-Poteshman / Ge-Lin-Pearson, single-name informed puts predict *continuation*, so this is a short thesis to respect rather than a crowd to fade. Disqualified as a standalone fade on BACKWARDATION-near-NFP and only 2 aligned signals.

**`contrarian-scanner` returned zero fade candidates and zero −2 deductions.** The rubric's −2 line requires **VRP positive** and VRP is FAIR/NEGATIVE everywhere. Separately, no AI-complex name shows P/C crowding beyond its own 20-day norm — the closest, MU (z −1.985) and ARM (z −1.714), are dip-recovery accumulation textures, the opposite of the euphoric chase the deduction is built to catch. At index level SPY (z −4.208) and QQQ (z −2.369) are BULLISH_EXTREME — the *wrong polarity* for the one citation-supported index contrarian edge (Simon-Wiggins 2001 fires at high-P/C fear extremes).

---

## 4. LEAP Builds (6–24 months)

**Empty board. No candidate qualified.**

Every name screened failed **Gate 4** — the `uw historical cumulative-premium-flow` 90d accretion gate — before gate-counting even began. LEAP share of DTE volume is 3.6%, a thin tape.

| Ticker | Gates | 90d cum-flow | Disqualifier |
|---|---|---|---|
| WOLF | 1/9 | **−$127.2M BEARISH** | DP signal DISTRIBUTION (buy/sell 0.59); conviction-matrix **DISTRIBUTION, conf 12.8%**; price −44.67%/30d. A single large call OI print against a dominant institutional-selling tape |
| GSAT | 1/9 | −$210k **MIXED** (flat) | conviction-matrix **DIRECTIONAL_SHORT**, conf 13%; DP DISTRIBUTION |
| VFC | 0/9 | −$6.49M BEARISH | wrong-direction both windows |

The AI/semis complex was checked directly for a slow-accretion signature underneath the noise: **all 11 names returned `trend_direction: MIXED` on 90d**, with net/gross ratios of 1–4% — statistically flat. **`oi-trend` BUILDING fired 11 of 11**, restating register C47's zero-discrimination problem (it fired 16-of-16 on 2026-07-24): on a broad melt-up day every liquid name's OI builds, so the label carries no weight alone. INTC is the cleanest disqualification — its DTE≥180 call OI build is **bid-dominant (selling)** with 30d cum-flow outright bearish.

`uw oi position-rolls` detected no far-dated roll-forward in any candidate (the day's rolls cluster in TLT, VIX, HYG, CCJ, ETHA, WBD) — no thesis-extension activity in the melt-up names.

**Rate-sensitivity note:** 10Y at 4.70% and rising, core PCE 3.29% — a rising long end is a structural headwind to long-duration-growth LEAP calls regardless of flow signature.

---

## 5. Volatility Surface

**Substrate hygiene is the headline.** Raw `iv-term-structure` labels were wrong on a large fraction of the book again. Running `scripts/term_structure_hygiene.py` (min_contracts=15 — a **named, tunable, NOT audit-frozen** parameter): **7 of 18 names flipped** — AMAT, ARM, AVGO, MU, NBIS, SMH (BACKWARDATION→KINKED) and **SOXX (BACKWARDATION→CONTANGO)**. SMH and SOXX also flipped *base* shape (→FLAT / →CONTANGO), the exact "contango base with an event kink" case where neither label alone describes the curve. In the earnings lane a further 3 flipped: SMCI, CSCO (both →KINKED with CONTANGO base) and AMAT. **None of today's tradable candidates would have been visible from the raw label.**

**What the surface is actually saying.** Every one of 18 names shows a real IV spike at the dte1–3 tenor (AMD 198%→102%, INTC 133%→96%, MU 147%→108%, SOXL 265%→209%). That bump is **uniform across the book** — per Dubinsky-Johannes-Kaeck-Seeger, exactly the signature that carries *zero* discriminating power. It is NFP hedging demand, and it is why the raw tool returns BACKWARDATION on nearly everything. VIX's +4% is the same macro-hedge bid showing up at index level.

The discriminating layer is one tenor further out: a **ticker-specific kink cluster at 08-14 (post-CPI) and 08-21 (OPEX)** whose prominence varies sharply across otherwise-similar semis — **ARM 29.0%** versus AVGO/MU/AMAT/SMH at 5.7–6.8%. Combined with **15 of 17 single names carrying negative VRP** (tercile: PLTR −0.453, IBM −0.427, MU −0.260, SOXL −0.157, NBIS −0.153, LRCX −0.142, AMAT −0.121, CRWV −0.087 vs positive DELL +0.163, AVGO +0.155, IRM +0.137 — the negative tercile is 3–4× wider), the surface reads **buy-vol / calendar**, not "vol is rich, fade the VIX pop."

**Calendar candidate — IBM is the best structural fit in the book.** Front-end ratio **1.017**, the flattest in the entire scan (panic absent, not merely low), no catalyst in the window, and **VRP −0.427**, the deepest negative reading — so being net long back-month vega is correctly signed. Trade: 08-14 / 09-18 ATM calendar near the 235 strike. It failed the confluence gate on a single flag, so it is watch-only, but it is the cleanest vol structure surfaced today.

**Earnings vol (both half-size, both front-only-kink disqualified):**

| Ticker | ER | Kink | Prominence | Implied move | iv_rank | Verdict |
|---|---|---|---|---|---|---|
| **CSCO** | 08-12 (**CPI day**) | dte10 = 08-14 | **19.5% — strongest of the scan** | 2.77% | 96.0 | SELL VOL, **half size** |
| **SMCI** | 08-11 | dte10 = 08-14 | 11.8% | 6.79% | 98.0 | SELL VOL, **half size** |

Both were downsized because back-month skew is **flat, not stretched** (CSCO NORMAL 1.055, SMCI **COMPLACENT 0.957**) — the front-only-kink disqualifier. SMCI carries two further headwinds: it sits in the negative-VRP AI complex where running short vol is the wrong lean, and CPI falls inside its dte10 tenor. For CSCO, CPI lands on its own earnings day, so part of the kink's richness is macro rather than earnings-specific.

**`GFS` — `NO_NEAR_TENOR`, not FLAT (mandatory skip).** The raw tool reported `regime: FLAT, ratio 1.0`, but `near_dte_actual == far_dte_actual == 17`: it compared a tenor to itself because **no listed expiry exists before dte17**, with earnings tomorrow premarket. The event premium is **unmeasurable**, never "calm."

**Calibration discipline:** `high_iv_rank` and `earnings_vol` are the only two classes surviving BH correction as miscalibrations for a 4th–5th consecutive audit (post-freeze `earnings_vol` realises 0.449 on n=78; `high_iv_rank` 0.562 on n=16). **DELL is the canonical case** — raw iv_rank 100, front-end 1.026 no panic, VRP +0.163 positive — and is explicitly *not* surfaced as a sell-vol candidate: its class ceiling (0.60) drops it into the anti-predictive band, capping it at starter. A high-IV-rank fade is not a high-probability trade.

**IV outliers:** the cached file is dominated by same-day-expiry noise (QQQ 495c max_iv 477.6%, IWM 287c 173.4%) — documented 0DTE contamination. **No AI/semis single-contract outlier survived filtering.**

**New QC artifact — SOXX base_shape regression gap.** `front_end_ratio` **1.404** (strongly backwardated front) contradicts its own `base_shape: CONTANGO`. Tenors: dte3 84.5% → dte10 **88.7% (rising)** → dte17 65.9% (sharp drop) → declining tail to dte864 50.8%. dte10 carries 1,515 contracts, so this is **not** a thin-tenor artifact — the monotonic fit nets CONTANGO despite a visibly backwardated front cluster that is up-then-down rather than cleanly declining. **Do not trade SOXX term structure off this read.**

**Data-quality flags:** all `iv-percentile-zscore` reads used `dates_used: 79` against a requested 252 (SKHY: 15) — every percentile in this section is **PROVISIONAL**, below the ≥120-day first-class bar. SKHY's `uw historical vrp` returned "insufficient price history" — abstained entirely.

---

## 6. Risk & Correlation

**Macro headline:** curve normal +43bp; core PCE 3.29% still hot against core CPI 2.81%; **10Y 4.70% and rising +21bp/30d under a tech melt-up**; payrolls decelerating to +57k; USD weakening. Forward: **NFP T+3 (08-07)**, CPI T+6 (08-12), PPI T+7, core PCE T+17, FOMC 09-16.

**Breadth cross-check (`fz`, advisory):** 359 advancers / 141 decliners, **71.37% green**, avg +1.46%, median +0.88%; top mover PLTR +29.46%, worst APTV −16.62%. `divergence_flag: false` — the equity tape *confirms* the green index. **But it contradicts `uw` options-flow breadth at 41.1% bullish.** Equity tape broad-green versus options flow bearish-skewed is the day's central divergence, and it resolves in favour of the options tape once you notice that 76% of whale prints were closing and ~$255M of multileg debit went into downside convexity.

**Correlation cluster — `AI_semis_cluster` FIRES.** All three sized candidates are one bet:

| Pair | Correlation |
|---|---|
| LRCX / NBIS | **0.748** |
| AVGO / LRCX | **0.702** |
| AVGO / NBIS | 0.694 (soft-watch, no penalty) |

Kept member: **LRCX** (raw 4 ties AVGO 4; tiebreak on cum_flow_30d, +$104.5M > +$98.6M). AVGO and NBIS each take −1 tier. Wider complex: LRCX/AMAT **0.943**, MU/AMAT 0.885, NBIS/CRWV 0.880, LRCX/MU 0.876, LRCX/INTC 0.875, MU/INTC 0.823, ARM/INTC 0.819. The entire candidate union is effectively a single AI-semis position.

**Fundamentals verdicts (top-5):**

| Ticker | Verdict | Adj | Contradicting facts |
|---|---|---|---|
| AVGO | **CAUTION** | −1 | insider MSPR **−94.62**, net-selling **14 of 16 months**; **Goldman removed it from the Conviction List the same day** (adding MSFT); earnings trend *mixed* — Q2'26 −0.24% and Q1'26 −0.87% were both misses |
| LRCX | **CAUTION** | −1 | insider MSPR −81.53; $1.05M Tier-2 opening 560P (Jun-2027) |
| NBIS | **CAUTION** | −1 | insider MSPR −73.42; op margin **−70.55%**; **earnings 08-12 land ON CPI day** |
| PLTR | CONFIRM | 0 | `post_catalyst_chase` TRUE; 90d cum-flow −$60.9M MIXED contradicts the 30d +$191M; $3.63M 155P (size/OI 25.6) laid on the melt-up day |
| MU | CONFIRM | 0 | the dte17 kink is **macro** (NFP/CPI/PPI), not MU's own earnings (09-21, outside the window) |

No VETOs. Every long name carries material insider net-selling — a quality-fundamentals, elevated-insider-selling tape.

**Debate-disconfirmation cuts — the gate fired 5-for-5, a first.**

| Ticker | Bull | Bear | Bear's strongest unrefuted point |
|---|---|---|---|
| AVGO | 0.35 | **0.75** | Insider MSPR −94.62 plus a same-day GS de-list — both flow-independent — on a rally the bull conceded is chip-sector beta |
| LRCX | 0.35 | **0.65** | `dealer_positioning` has `win_rate: null / NA(substrate)` — the primary signal has **never been measured to have any edge** — and `vol-surface-scout` independently returned "no trade" on the same name |
| NBIS | 0.25 | **0.65** | The `bullish_flow` class books 0.4203 / **−8.0pp excess** before any name evidence; and selling calls at the bid *and* buying puts at the ask is one short-delta expression twice, not offsetting de-risking |
| PLTR | 0.25 | **0.75** | 90d cum-flow −$60.9M MIXED contradicts the 30d +$191M the score rests on |
| MU | 0.25 | **0.75** | `front_end_iv_ratio` 1.122 breached the panic gate **before** any of the three calendared prints fired — the adverse case for a short-front calendar |

**Adverse-flow exit candidates: none available.** The rolling `conviction_2026-08-03` group is **empty** — no LOW+ names were written yesterday under the corrected 07-23 rule, consistent with the empty-board streak. Both `uw watchlist alerts` and `uw watchlist scan` returned empty. The `fz` quote-drift tripwire cold-starts silently.

**Hedge sleeve.** Sized book is empty → net delta ≈ 0 → the ≥0.6 skew trigger does not fire and **no hedge is mandatory**. Advisory for any residual long-tech exposure carried into NFP: the institutional tape is already building the right shape. Mirror the **IWM-style Aug-21 defined-risk put vertical** (dte17, spans both NFP and CPI, ~6.8:1) on SPY or QQQ — long premium is correctly signed against QQQ VRP of −0.0435. The SPY Nov fly ladder is deep-tail insurance only (peaks at −34%); the VIX Sep C35 ladder is the convex alternative. **Do not sell premium on QQQ-complex names to finance it** — wrong side of negative VRP.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**No HIGH or MEDIUM tier calls. 0 HIGH / 0 MEDIUM / 3 LOW — and all three LOW names gate to skip.**

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`: no per-tier expectancy can be computed this session — the sized book is empty and the rolling `conviction_2026-08-03` group holds no closed calls. The standing audit finding remains that the **DROP pile has out-graded the sized book in every audit since 2026-07-04** (DROP 43.3% vs sized 38.6% on the 07-18 window), which is the empirical basis for treating an empty board as a decision rather than a failure.

**Full audit trail for the three LOW names** (none sized; recorded so the counterfactual resolves):

| | AVGO | LRCX | NBIS |
|---|---|---|---|
| `raw_score` | 4 | 4 | 3 |
| Components | sector-leader +1 · OI build +1 · vol KINKED/VRP +1 · cum-flow +1 | DEX flip +1 · OI build +1 · sector-leader +1 · cum-flow +1 | vol KINKED/VRP +1 · OI build +1 · cum-flow +1 |
| `dominant_signal_class` | `sector_rotation` | `dealer_positioning` | `bullish_flow` |
| `win_rate` (n, source) | null — `NA(substrate)` | null — `NA(substrate)` | **0.4203** (n=138, `backtest_clean`) |
| `market_excess` | null | null | **−0.0797** |
| Pre-risk size | starter | starter | starter |
| `fundamentals_verdict` | CAUTION | CAUTION | CAUTION |
| Debate (bull/bear) | 0.35 / **0.75** | 0.35 / **0.65** | 0.25 / **0.65** |
| Gates fired | cluster, fundamentals, event_risk, debate | panic, fundamentals, event_risk, debate | panic, cluster, **sector**, fundamentals, event_risk (+ stacked own-earnings), debate |
| **Final size** | **watch_only** | **watch_only** | **watch_only** |

**Substrate note that shapes the whole board:** `uw historical signal-backtest` supports only 5 classes (`bullish_flow`, `bearish_flow`, `high_iv_rank`, `volume_spike`, `dark_pool_accumulation`). `dealer_positioning`, `sector_rotation`, `multileg_directional` and `earnings_vol` have **no substrate in this CLI build** — so the two highest-scoring names on the board rest on signal classes whose edge has never been measured at all. The one clean-protocol run (`bullish_flow`, 5d, `--top-n 200` pinned) dropped 14 clamped rows plus 1 C12 sub-floor row (HTZ at $2.20), kept **n=138**, and recomputed **WR 0.4203** against a same-window SPY-long benchmark of 0.5000 → **market_excess −8.0pp**. The headline 47.1%/153 was never quoted.

**Step 6.5 batched strategy synthesis was skipped** — `uw playbook batch-scan` operates on the raw_score ≥ 7 list, which is empty. It was run against the multileg structure names for the disagreement check instead; see §8.

**Deep-dive hand-off:** skipped. Step 8.5 applies to the top-2 **HIGH-tier post-gate** names and there are none. Step 6 deep dives were run on the top 3 by conviction and are reported in §3a.

### Conviction rubric (frozen, version `2026-06-12`) — embedded verbatim for audit

```
+1  MECHANIZED DEX flip or vanna-squeeze in trade direction (script-verified SIGN CHANGE via scripts/dex_flip.py, not a level)
+3  3+ aligned signals in accumulation-hunter (DP + OI + smart-positioning, block-stratified institutional-tier confirmed)
    — CONJUNCTION (C11): full +3 only when cum_flow_30d sign-aligned AND |cum_flow_30d| >= $50M; else halved (floored) to +1
+1  multi-day OI build (uw historical oi-trend BUILDING, --days >= 5)
+1  uw insights conviction-matrix DIRECTIONAL_LONG conf > 70 — CONDITIONAL: only when dominant_signal_class == leap_directional
+1  cum-premium-flow net directional accretion 30d — INTENT-SCREENED: only when (a) no C28 distribution_flag, AND
    (b) on dividend payers in an ex-div window the accreting prints are not deep-ITM sub-parity calls
+1  sector-rotation single-name leader — CONDITIONAL: persistence >= 0.6 AND cum_flow_30d aligned AND |cum_flow_30d| >= $50M
+1  earnings-scout BUY VOL or SELL VOL
+2  multileg-strategist directional structure (term-structure-anchored play type)
+1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
+1  opex-pin-strategist top-5 (OPEX week only)
-2  contrarian-scanner overcrowded long with rising pc-ratio-zscore (VRP positive) — INFORMED-FLOW CONTINUATION penalty
-3  flow_conflict — cum_flow_30d clearly opposite dominant_signal_class (sign flip AND magnitude > union-median |cum_flow_30d|)
-1  flow_conflict_lite — 30d read MIXED (signed sum near zero, or aligned but bottom-quartile magnitude)
    flow_conflict and flow_conflict_lite are MUTUALLY EXCLUSIVE
[TIER GATES, applied by risk-monitor in 2d — 0 points, never score_components]
-1 tier  correlation cluster (pairwise corr >= 0.70)
-1 tier  regime conflict with trade direction

Tiers: >=9 HIGH (full) | 7-8 MEDIUM (half) | 3-6 LOW (starter/watch) | <=2 DROP
```

**Lines that fired for nobody today:** +3 accumulation (zero qualifying names — closing-cross contamination), +1 conviction-matrix (no LEAP class), −2 contrarian (VRP not positive anywhere), +1 vanna (all books call-heavy, VIX rose), +1 opex (Aug OPEX 17 days out, agent not spawned).

---

## 8. Watch-only — single signal, no confluence

Failed the ≥2-distinct-agent confluence gate. Listed for journaling, **not for entry**.

| Ticker | Sole flag | Note |
|---|---|---|
| **IBM** | vol-surface-scout | The best *structural* vol fit on the board (front-end 1.017, VRP −0.427, no catalyst) — and it scores **0**, because the frozen rubric's vol line requires KINKED or BACKWARDATION and IBM is neither. Registered counterfactual |
| **INTC** | sweep-tracker | Cleanest confirming sweep in the book (99% opening-dominant) against the **largest flow conflict in the union**: 30d cum-flow **−$1,012.3M**, 6.7× the median threshold → −3. Net raw_score **−2** |
| SMCI / CSCO | earnings-scout | Both half-size SELL VOL; see §5 |
| **MCHP** | multileg + sweep (2 flags, but raw 1) | $64.0M Dec-65C/Sep-75C diagonal, delta +0.779 / **vega 0.15** = pure delta, leveraged stock replacement. Back end FLAT (68.6% vs 68.1%) so no term carry. NEW BUILD at 5× standing OI. Docked to raw 1 by a −1 lite on a −$12.2M/8%-of-median flow read — a registered counterfactual |
| **GOOGL** | multileg | $71.9M Oct-16 375/410 call debit vertical, the largest single-name structure of the day. **ADD-vs-OVERWRITE unresolved** — C375 already held ~54k OI from 07-29, so today's package may be that long being *capped* by selling 53k C410, a bullishness-reducing adjustment fitting the 76%-closing tape. Resolves on tomorrow's T+1 OI |
| CG / EWZ / HYG / VIX | multileg | CG has **undefined risk above $58.30** (40,504 naked calls). EWZ direction unresolvable, sitting on the Oct-2026 Brazilian election vol hump with VRP **+11.6pts**. VIX C12-disqualified (index, no share ADV) |
| CRWV / AMAT / DELL | vol-surface-scout | See §5 |
| ORCL / TSM / MSFT / PLTR / MU / SMH / ARM / SPY | various | Scored but DROP; see §3, §6 |

**`uw playbook batch-scan` disagreements (multileg read preferred, per Step 6.5):**

| Ticker | batch-scan | Structural read | Verdict |
|---|---|---|---|
| **GOOGL** | `flow_direction: bearish` → "follow the smart money" | **$71.9M LONG call debit vertical** | **Flat contradiction** — batch-scan is counting the sold C410 leg as bearish premium. The classic multi-leg mis-classification: *the short wing of a debit vertical reads as bearish single-leg flow.* Surface this loudest |
| HYG | `LOW_IV` → "long call / call debit spread" | 52,000-contract Dec **put** structure where Dec IV is ~4× rv20 | Contradiction — "LOW_IV" is an iv_rank on the wrong tenor. Do not buy HYG calls |
| EWZ | "aggressive long puts" | Dec combo on the election vol hump, VRP +11.6pts | Direction may be right; the structure buys the richest premium on the curve |
| MCHP | `HIGH_IV` → "bull put **spread (credit)**" | $64.0M **debit** diagonal, vega 0.15, flat back end | Both bullish, but credit vs debit is opposite. iv_rank 89 overstates it: IV 68% vs rv20 55.7% is only +12pts, and there is no term carry to sell |
| SPY | `LOW_IV`, bullish → "long call" | Bullish Aug-21 spread exists ($28.7M) but is **outweighed 2.5:1** by $73.2M of laddered put flies | Partial — batch-scan sees only the bullish side, missing the entire hedging programme |
| CG | "bull put spread" — defined risk | 1:1.405 ratio call spread — **undefined** risk | Risk profile does not match what is being built |
| **IWM** | "long put / put debit spread" | Aug-21 put debit vertical, 5-of-5 sessions | **Agreement** — the one convergence, which raises confidence in the IWM read |

---

## Appendix — tooling and substrate findings for the next calibration audit

1. **`fz` doubled-first-letter ticker corruption confirmed on a second endpoint.** `fz screen` (AABEO, AABR, BBLZE, ZZBRA, DDDOG, MMT, SSWK, AAME) and now **`fz insider-clusters` (XXAIR)**. Squeeze and RS lanes were graceful-skipped this run. `fz breadth` is unaffected, and `fz_enrich.py` returned **clean** tickers for all five top-5 names — so the bug is **intermittent and endpoint-specific**, not universal. It has blocked C16 for four audits.
2. **`hot-chains multileg`'s `multileg_ratio` is `multileg_volume / multileg_total`, NOT `/ volume`.** A row can post ratio 0.9999 on **45 contracts** of actual multileg volume (KRE260821P71: ratio 0.9999, mlvol 45, volume 85,552; FISV260918P50: ratio 0.9956, mlvol 87, volume 150,756). The agent's own documented `>0.3` screen therefore admits near-zero-multileg rows — **the screen rule is defective**; re-screen on `multileg_volume / volume`. Today's read is unaffected (all 18 non-SPXW rows clear both).
3. **`historical oi-trend` is T+1 relative to `hot-chains multileg`.** Six SPY legs with 150k–300k multileg volume on 07-31 had *zero* same-day OI corroboration but matched exactly on the next session's row (+300,033 / +300,092 / +149,973 / +149,991 / +150,011 / +150,001). Reading OI same-day mis-tags every multileg row as unconfirmed.
4. **Raw `front-end-iv-ratio` selects sub-floor far tenors (4–7 contracts) on 4 of 9 earnings names**, inflating the ratio: AKAM raw 1.599 vs clean 1.282; TWLO 1.513 vs 1.386; IRM 1.347 vs 1.157; DBX 1.238 vs 1.129. Contamination is **not confined to `iv-term-structure`**.
5. **`uw insights analyst-vs-flow` returned no analyst field on all 9 tickers tested** — the highest-EV setup in earnings-scout's kit was uncomputable. Tool gap, not "no divergence."
6. **SOXX `base_shape` regression gap** — see §5. New artifact.
7. **ZGL-grid artifact extended to AVGO and DELL** (previously SPY/QQQ/IWM/MU).
8. **New artifact class: SPX/SPXW multi-leg collar counted as directional single-leg sweep premium** — see §3a. Distinct from the cross-name twin-print NBBO artifact.
9. **Conversion/reversal parity artifact recurs:** on 07-31, HTZ260821P9 (100,000 @ $7.40) paired with HTZ260821C9 (100,000 @ $0.01) on a ~$1.60 underlying — a conversion at exact parity with zero directional content that would have ranked top-10 on that day's multileg screen. Nothing in the payload distinguishes it. A standing filter is warranted.
10. **`term_structure_hygiene.py` input-shape sharp edge:** it requires the `{ticker: payload}` wrapper. Passing the bare CLI payload iterates the dict's keys and dies on `TypeError: 'int' object is not iterable` (hitting `expiry_count: 24`). `contrarian-scanner` hit this and hand-derived instead, missing NVDA's KINKED classification (raw BACKWARDATION → hygiene KINKED, base BACKWARDATION — verified independently). Operator error, but the failure mode is non-obvious and worth a clearer error.
11. **Step-0 C12 universe gap:** MCHP, SMCI, CSCO, GFS, DBX, AKAM and COHR were absent from `c12_liquidity_floor.pass[]` because that list only covers names pre-surfaced by the `uw` screeners. All independently cleared C12 when agents ran the floor directly. The floor is correct; the *universe fed to it* is screener-bounded.
12. **Data corrections made during this run:** GOOGL's `cum_flow_30d` was transcribed into the union as −$106.6M, which is the **single-day** screener net; the tool-authoritative 30d is **+$17.4M MIXED** (0.2% imbalance), so GOOGL takes `flow_conflict_lite` (−1), not −3. ORCL's 30d tool label is **MIXED**, not BEARISH. The pinned union median ($150.8M) differs from the recomputed median of the printed values ($127.05M); the pinned value was applied as instructed and no name's deduction changes under either.
13. **AVGO's +1 cum-flow line rests on a quartile-boundary ruling** — +$98.6M is rank 4 of 14, *exactly* the Tukey Q1 value, so not strictly inside the bottom quartile. One quartile-method choice away it becomes a −1 lite instead of a +1: a **2-point swing** on a raw score of 4. Flagged as method-dependent.
