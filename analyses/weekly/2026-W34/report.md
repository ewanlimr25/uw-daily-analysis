# Weekly Market Intelligence — Week of 2026-08-17 (ISO 2026-W34)

## Executive Summary

- **Week regime + WoW Δ:** TRANSITIONAL / UPTREND **held** both ends — SPY 765.72, above its 20SMA (762.33) and 50SMA (751.75), −1.75% off the 90-day high — but options-flow breadth stayed **below 50% bullish every single session** (33.6% Mon → 39.2% Fri). VRP is **FAIR-to-negative**: SPY +0.0016 (a rounding error), QQQ **−0.0307** (IV below realised — a premium-**buying** regime on the Nasdaq complex). The netted sector book flipped hard mid-week: Technology +$222.6M IN Monday → **−$328.6M OUT Friday**, Healthcare −$41.2M → **+$38.0M IN**.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`.
- **Signal performance:** **0 of 4 resolved (hit rate 0/4 = 0%); 1 INCONCLUSIVE excluded; 5 total calls in universe (5 envelope-anchored, 0 reconstructed).** Every resolvable call lost — and **zero capital was at risk**, because all five were LOW tier at `skip` or `watch_only`. The gate stack refused the entire week.
- **Top swing build for next week:** **None sized.** IWM (short) is the only name above the drop floor at raw 5 / LOW, and it routes to `watch_only` under the short-direction rule. It carries the best-built structure of the week and is still not investable — see §3b.
- **Top LEAP build:** **None.** The LEAP book is empty; the sole candidate (IBIT) hard-failed its accretion gate.
- **Biggest emerging risk:** **Jackson Hole, 08-27→08-29 — Kevin Warsh's first appearance as Fed Chair — with July core PCE landing 08-28 (T+4 to T+5).** Core PCE is running 3.29% YoY against payrolls of −23k and a 10Y bear-steepening to 4.69%. Secondary: a genuine `semis_memory_cluster` (INTC/AMD/SNDK/AVGO, pairwise to 0.856) and the fact that IWM at **0.833 correlation to SPY** is index beta wearing a Russell ticker.

---

## 0. Week in Review — Intra-Week Signal Performance

Universe = the union of non-DROP `calls[]` across this week's five daily `decision.json` envelopes, keyed by `(ticker, direction)`. All five weekdays produced an envelope, so there is **no reconstruction and no survivorship gap**. 50 calls were emitted in total; 6 were non-DROP; 5 unique after IWM/short appears on both 08-20 and 08-21.

| Ticker | Direction | Source | Move vs 0.5×ATR(14) | Flow/OI | Grade | Note |
|---|---|---|---|---|---|---|
| CRWV | long | envelope 2026-08-17 | **−3.86×** ($106.00 → $87.85, −17.1%) | cum-flow MIXED; oi-trend saturated | **LOSS** | Decisive. AI/datacenter complex unwound. |
| MU | long | envelope 2026-08-17 | **−1.25×** ($1,011.75 → $966.78, −4.4%) | cum-flow MIXED; oi-trend saturated | **LOSS** | Lost into the Technology netted-outflow flip. |
| ULTA | vol_short | envelope 2026-08-18 | +0.55× (below the 1.0 threshold) | cum-flow MIXED | **INCONCLUSIVE** | The event has not happened — ULTA prints 2026-08-27. Correctly unresolved. |
| GDX | short | envelope 2026-08-19 | **+2.92× against** ($97.33 → $102.83, +5.7%) | cum-flow BEARISH — flow leg held, price refuted it | **LOSS** | Gold ripped; the bearish flow read was right and irrelevant. |
| IWM | short | envelope 2026-08-20 | **+1.35× against** ($297.67 → $299.96, +0.8%) | cum-flow BEARISH — flow leg held | **LOSS** | Same call re-made 08-21 and again this week. |

**Capital impact: zero.** CRWV, MU and ULTA were `skip`; GDX and IWM were `watch_only` via the 2026-08-01 short-routing rule. A 0/4 hit rate on four LOW-tier paper calls costs nothing, and the short-routing rule paid for itself twice in five sessions.

Two honest qualifications. First, **n=4 is not evidence of a broken rubric** — it is one thin week, and the meaningful fact is that the book was correctly empty rather than that the paper calls lost. Second, both losing shorts had their **flow leg confirmed and their price leg refuted**, which is the signature the 2026-08-01 audit identified as mis-selection rather than mistiming.

---

## 1. Regime & WoW Delta

The regime label did not move: TRANSITIONAL with `trend: UPTREND` on both the Monday and Friday reads, SPY above both moving averages, guidance unchanged at *"Half position sizes. Favor defined-risk strategies."* What moved underneath it was breadth and rotation. Options-flow breadth improved from 33.6% to 39.2% bullish but **never crossed 50% on any covered day** — 3,837 bearish-flow tickers against 2,479 bullish on Friday. Against that, the `fz` price-breadth cross-check reads **66% green** (332 advancers / 169 decliners). Those two measures come from different lineages and are not directly comparable, but the gap is the tell: broad price participation on OPEX Friday while options flow stays put-skewed is a hedged tape, not a conviction bid. Flagged as `divergence_flag: true`, advisory, no size impact.

`dte-volume-share` crossed into `RETAIL_DRIVEN` at Friday's close with 0DTE at 45.9%. Pulled across all five days it reads 20.5 / 20.4 / 22.5 / 31.1 / 45.9% — but the **institutional (monthly + LEAP) share held flat at ~20–23% the whole week**. The 0DTE ramp is mechanical compression out of weeklies into a monthly expiry, not a regime shift. Reading Friday's number alone would have badly misled.

**Macro backdrop** (`scripts/fred_macro.py`): the curve is normal at +0.50 (10Y−2Y) but **bear-steepening** — the 10Y rose to 4.69% while the 2Y fell to 4.19% and the USD weakened over 30 days. Core PCE is **3.29% YoY**, *above* core CPI at 2.79% and well above target; payrolls printed **−23k**; unemployment 4.1%; fed funds 3.63%. That is a stagflation-lite configuration: sticky inflation, softening labour, rising term premium. It is specifically hostile to profitless small-caps and specifically supportive of gold — the two names that dominated this week's candidate set.

**Forward event risk (trading days from T+0 = 2026-08-21):**

| Event | Date | T+N | Tier |
|---|---|---|---|
| Conference Board consumer confidence | 08-25 | T+2 | 2 |
| Durable goods | 08-26 | T+3 | 2 |
| Q2 GDP 2nd est. + jobless claims | 08-27 | T+4 | 2 |
| **Jackson Hole — Warsh's first as Chair** | 08-27→08-29 | **T+4→T+6** | **1 by impact** |
| **July core PCE** | 08-28 | **T+5** | **1** |
| August CPI | 09-11 | T+14 | 1 |
| FOMC + SEP | 09-15→09-16 | T+16/17 | 1 |

Implication for next week: the tape has a new Fed Chair's debut policy speech and a hot core-PCE print inside five sessions. Nothing in this book is worth carrying uncompensated gamma into that.

---

## 2. Sector Rotation

**Rotation regime call: `no_change`. Confidence: LOW.**

Direction reads off the netted `market-regime.sector_rotation` only. Two structural limits shaped this section. First, that source is a **top-3/bottom-3 truncation**, and the fleet pins it on Monday and Friday only — so it yields exactly **two data points**, and a ≥3-day persistence claim on the only directional source is **unmeetable by construction**. Five of eleven sectors (Industrials, Communication Services, Energy, Real Estate, Utilities) had no netted reading at all on Friday. Second, `sector-flow-persistence` fired **INFLOW on 10 of 11 sectors** (the 11th, Utilities, ROTATING at 0.6) — zero discrimination, as expected from a sign-agnostic gross-turnover measure. It is a durability filter and nothing more.

The week's headline — Technology flipping from largest netted inflow to largest netted outflow — **does not survive independent confirmation**. The same Friday session shows gross Technology flow at **+$4,037.1M**, and XLK's own 5-day instrument tape reads **BULLISH (+$7.41M)**. Technology routes to `watch_only`.

The ETF instrument layer did the most valuable work of this section: **it overruled two of the three sectors that looked confirmed at the GICS level.**

| Sector | Netted (Fri) | Gross (Fri) | Representative ETF (5d) | Verdict |
|---|---|---|---|---|
| Healthcare | +$38.0M IN | +$568.7M | **XLV +$4.95M BULLISH**, call-dominant ask-side sweeps | **Survives all four layers** |
| Basic Materials | +$16.6M IN | +$302.2M | **XLB −$4.89M**, GDX **−$26.40M (worst in universe)** | Overruled → `watch_only` |
| Financial Services | +$15.7M IN | +$444.4M | **XLF −$13.91M (2nd worst)** | Overruled → `watch_only` |

**ETF flow tape (advisory, 0 rubric points)** — ranked, top-3 each side deep-pulled:

| ETF | Net premium dir (5d) | Net flow | GICS agreement | DP positioning | Options urgency | Named leaders |
|---|---|---|---|---|---|---|
| XLK | inflow BULLISH | +$7.41M | **disagree** (Tech netted OUT) | $115.8M top-5, 4-of-5 above mid | put-skewed Friday (OPEX hedging) | see bifurcation below |
| XLV | inflow BULLISH | +$4.95M | **agree** | $359.4M top-5, 3-of-5 above mid | call-dominant, $604.8K aggressive ask | MRNA, JNJ |
| XLY | inflow BULLISH (thin) | +$2.34M | disagree | $140.6M top-5, mixed | thin, call-only, noise-level | TSLA |
| KRE | inflow BULLISH | +$1.75M | agree (subsector only) | not deep-pulled | not deep-pulled | SOFI |
| XLB | outflow BEARISH | −$4.89M | **disagree** | not deep-pulled | not deep-pulled | none in funnel |
| XOP | outflow BEARISH | −$8.40M | no netted read | $11.9M, 1-of-5 above mid | put-heavy, incl. $4.52M 2027 put buy | — |
| XLF | outflow BEARISH | −$13.91M | **disagree** | $298.2M, 1-of-5 above mid (distribution-skewed) | $21.9M call premium, only $1.9M at ask | CG bearish |
| GDX | **outflow BEARISH (largest)** | **−$26.40M** | **disagree** | $116.2M, mixed | $44.4M call premium but mostly **bid-side (writing)** | — |

Only **Healthcare** clears netted → gross → market-relative → ETF cross-confirm simultaneously, with **MRNA and JNJ** as the named leaders. Even that is qualified: the netted series *flipped mid-week* (OUT Monday, IN Friday), so its durability rests on the 5-day XLV instrument read and Friday's call-skewed sweep tape, not on the netted series itself. Treat it as a reversal that completed by Friday, not a rotation that held all week.

A genuine subsector bifurcation is worth recording: **regional/challenger banks bid (KRE +$1.75M, SOFI +$8.0M) while broad financials and private equity sold (XLF −$13.91M, CG −$11.0M)**. That is instrument-only — no netted GICS line supports it — and it is the one thread in the value/cyclical story that survived scrutiny.

---

## 3. Swing Book (1–6 weeks)

### 3a — Long swings (regime-aligned)

**Empty. No long-side name cleared the drop floor.**

The two names that cleared the confluence gate on the long side both died on measured evidence rather than on a gate:

- **GLD — raw_score 2, DROP.** Structure alone scored +5 and was clean: a 2-day rolling call vertical (410C/430C exp 09-04 rolled to 430C/445C exp 09-11, matched ~55,292-contract legs, 430C confirmed ask-side bought, ~$92.2M) plus direction-verified call OI at **7.98:1** with +77,917 net ask-side bought. A **−3 `flow_conflict`** (cum_flow_30d −$275.16M, 8.72× the union median) is the entire difference between LOW and DROP. See §7 — both debate sides independently concluded that deduction rests on **stale** flow.
- **MSTR — raw_score 0, DROP.** The cleanest illustration of why direction-verification matters. The raw `oi-trend` label reads BUILDING with a perfect 5-of-5 streak and +540,606 net OI, which under a literal reading would have made MSTR a 3-point name. Side-resolved, the build is **institutions writing calls into a +28.17% week** — week call `net_ask_bid` **−42,898 (bid-side sold)**, corroborated by `conviction-matrix` MIXED at 5.8% confidence with net-bid call flow, and by sweep-tracker's net-bearish tag. Its $594.8M deep-ITM Dec-2028 stock-replacement vertical is real and well-executed, but it printed on **one day only** and fails the ≥2-day repeat requirement.

### 3b — Short / fade swings (defined risk only)

**All route to `watch_only` and are never sized** (2026-08-01 P0 #1). Routing, not suppression — theses, structures and invalidations print, and every call serializes so the counterfactual keeps resolving.

| Ticker | Tier | Score | Win-rate | Final size | Thesis | Structure | Invalidation |
|---|---|---|---|---|---|---|---|
| **IWM** | LOW | **5** | null `NA(substrate)` | `watch_only` | The best-built structure of the week. A persistent OTM put program exp **09-18** walking strikes down 289→288→287→286→285→283 across **4 sessions**, each strike repeating on two consecutive days (~$128.2M), plus a debit put vertical exp 09-11 (sell 285P / buy 295P, exact size match 55,273 both legs, $27.7M). Aggregate **$155.9M**. Side confirmed ask-side via `greek-screener` on both 08-20 and 08-21; OI direction-verified at **5.64:1** puts with +338,283 ask-side bought and only 9,156 of 1.03M adds at 0DTE — not expiry churn. Term structure is clean monotonic CONTANGO with no kink at Jackson Hole or PCE, so this is directional, not an event-vol play. | Long 09-18 OTM puts / 09-11 295P-285P debit vertical | Flow reverses to bid-side unwind of the 283–286 strikes, or breadth crosses back above 50% bullish |
| INTC | DROP | 1 | 0.5448 (n=134) | `watch_only` | Bearish sweeps 4-of-5 and the **only name in the week's sweep book with two independent legs agreeing** (`INTC260828P00065000` at a 165× ask/bid ratio). But the OI build runs the wrong way — calls 302,198 vs puts 175,608, **both legs bid-sold**, including a Dec-2028 70C covered-call write on $33.5M premium. | — | Netted Technology reverts to inflow; a direction-verified put-dominant OI build fails to appear |
| AMD | DROP | 1 | 0.5448 (n=134) | `watch_only` **(VETO'd)** | Sweep persistence 5-of-5 ($1.15B) but smart-money direction UNCONFIRMED; put-crowding building (pc z +1.478) under a bullish headline. Fundamentals **VETO** the short outright. | — | — |
| SNDK | DROP | −3 | 0.5448 (n=134) | `watch_only` | Largest bearish sweep book of the week ($2.45B, 5-of-5) running against **+$1,185.8M of 30-day bullish premium accretion** — a −3 flow conflict at 37.6× the union median. | — | — |
| SPCX | DROP | −3 | 0.5448 (n=134) | `watch_only` | Bearish sweeps 5-of-5, $1.30B, unconfirmed. −3 flow conflict, though at +$50.3M on $13.46B gross this is a boundary case (0.37% of gross). | — | — |

⚠ **Distribution caution (C28):** no long name in this book carries a `distribution_flag`, because no long name survived. The flag that *was* raised — **AAPL**, cross-validated three ways — is not in the trade book at all; see §7.

---

## 4. LEAP Book (6–24 months)

**Empty.** `IBIT` was the only funnel name with LEAP-scale fresh OI (45C/45P Jun-2027 +29,717/+24,100; 96C Jan-2028 +9,944 ask-heavy; 70C Dec-2027 +8,343 ask-heavy) and it **hard-failed the required accretion gate**: 90-day net flow is **+$233.85M on $6.97B gross — 3.35% — nowhere near a slow-accretion signature**, with the 30-day actually wrong-signed at −$15.16M. `position-rolls` returned **0 on all five covered dates**, `conviction-matrix` reads MIXED at **1.1% confidence**, and its apparent "LEAP ladder" resolves to an ATM 45-strike straddle — a volatility book, not a directional thesis. Its `oi-trend` build was driven by 0DTE/1DTE/7DTE strikes, i.e. OPEX-week short-dated churn contaminating the aggregate.

Explicit disqualifications: **INTC** 70C Dec-2028 (+6,660) is `prev_bid_volume` 6,104 vs `prev_ask_volume` 459 — calls **sold** at the bid, covered-call writing, not conviction. **AVGO** Sep-2027 legs are sub-2,500 contracts. **AMD** 300P Sep/Jun-2027 has two legs pulling opposite ways. **WMT**, **COIN**, **MRNA** are below materiality or wrong-signed.

Market-wide, `share_leaps` was **3.6%** of Friday volume. The absence of a LEAP signal is consistent with the tape, not a search failure.

---

## 5. Volatility Surface — WoW Term Structure & Skew Evolution

**The headline finding of this section is a measurement result, and it is the most important methodological output of the week.**

Raw `iv-term-structure` labels show BACKWARDATION firing on **9 of 15 names Monday (60%) rising to 13 of 15 Friday (87%)** — which would read as a dramatic week-over-week vol-regime deterioration. Run both snapshots through `scripts/term_structure_hygiene.py` and the hygiene-corrected `base_shape` reads **3 of 15 (20%) Monday → 4 of 15 (27%) Friday**. Essentially the entire apparent shift is **0DTE-bucket contamination on expiry day**. Confirmed directly: at the CLI default `--near-dte 1`, `near_dte_actual` snapped to 0 and returned BACKWARDATION on **5 of 5** spot-checks (SPY 1.078, QQQ 1.139, NVDA 1.584, AMD 2.087, MU 1.482) — all artifacts. **Never difference two raw snapshots across an expiry boundary.**

**Genuine WoW dislocations (hygiene-corrected), 2 of 15:**

- **MSTR** — CONTANGO → **BACKWARDATION**. Kink moved 14dte/09-04 → 28dte/09-18 (past September OPEX). `front_end_ratio@7` 0.931→0.962, rising but still below 1.05 — richening early, not panicking. Kink tenor sits *after* Jackson Hole/PCE, so `event_span_flag: NO`. Watch, don't trade.
- **IWM** — CONTANGO → **FLAT**, with term-skew **TAIL_HEDGING on both days and the ratio rising 1.333 → 1.380**. Small-cap put-hedging demand building independently of the shape change. Kink tenors (09-04, 09-30) sit outside the event window.

**The event-span table is the load-bearing result.** Six names carry their kink at exactly the **2026-08-28** tenor — Jackson Hole day-2 plus core PCE:

| Ticker | Kink (Fri) | dte | Event span | `front_ratio@7` Mon→Fri |
|---|---|---|---|---|
| NVDA | 2026-08-28 | 7 | **YES** | 1.177 → **1.392** (rising) |
| MU | 2026-08-28 | 7 | **YES** (moved IN from 42dte) | 1.058 → **1.190** |
| TSLA | 2026-08-28 | 7 | **YES** (moved IN from 42dte) | 1.010 → 1.038 |
| INTC | 2026-08-28 | 7 | **YES** (stable all week) | 1.016 → 1.004 |
| AMD | 2026-08-28 | 7 | **YES** | 1.026 → 1.044 |
| QQQ | 2026-08-28 | 7 | **YES** (fresh Friday, low prominence) | 0.903 → 0.914 |

This is **correct event pricing, not a dislocation to fade**. NVDA and MU show the front ratio *intensifying* through the week rather than resolving — the market is pricing a known binary, and selling that premium is selling insurance against a Fed-chair debut.

**Skew** richened only at the index/ETF level: SPY TAIL_HEDGING 1.368 → **1.454**, IWM 1.333 → 1.380, QQQ 1.250 → 1.270. Every single-name skew ratio *fell* — MSTR, AVGO, MRVL, PLTR all flattened further into complacency. All the tail-hedging demand this week is in the index complex.

**Calendar-spread candidates: none.** The gate requires a falling `front_end_ratio` with no pending catalyst. CRWD is the only falling-backwardation name (1.153 → 1.096) and it has earnings five days out — disqualified. HOOD (1.026→1.129), MRVL, NVDA and MU are all rising.

**`iv-percentile-zscore` is unusable this week.** Every ticker returned `dates_used: 92` against a requested 252-day lookback — a silent ~2.7× short-delivery, below the 120-day floor. **All percentile reads are PROVISIONAL** regardless of how extreme they look (NTAP 98.91/z 1.972; MU 0/z −1.849; INTC 1.09/z −1.884). No "extreme IV percentile" claim was scoreable anywhere in the book.

**NTAP** is flagged and handed off rather than classified: `base_shape` `NO_NEAR_TENOR` both weeks — the front end is genuinely unmeasurable under the hygiene floor (raw Friday printed a nonsense 5.767 at `near_dte_actual: 0`). Real elevated IV (rank 100), earnings 09-02, but the term-structure lane cannot classify it.

---

## 6. Earnings — Recap & 2-Week Lookahead

### (a) Recap

Five names printed during the covered week. Note that ULTA, INTU, CRWD, CRM, MRVL, HPQ, SNOW, DELL and AVGO — all flagged intra-week by the daily fleet — **had not yet printed**; their dates run 08-25 → 09-02.

| Ticker | Print | Pre-event thesis | Realized | Grade |
|---|---|---|---|---|
| **TJX** | 08-19 pre | Genuine BACKWARDATION (fer7 1.341); disqualified as a calendar — "hold, not fade" | Gap **−4.4%**, −2.6% more next session; **−6.8% over two sessions** | **CONFIRMING** |
| **WMT** | 08-20 pre | Grouped CALENDAR, scored 0 — "front panic persisting = event real" | Gap **−6.9%** on 83.6M shares (~4–5× normal) | **STRONGLY CONFIRMING** |
| **DE** | 08-20 pre | Genuine BACKWARDATION (fer7 1.274); hold-not-fade | **+5.3%**, then +5.1% more — **+11.5% total** | **CONFIRMING** |
| **ROST** | 08-20 post | Explicitly killed for SELL VOL — "front ratio 1.688, event still pending, don't fade it" | Gap **+6.5%**, settled +4.4% | **CONFIRMING** |
| **BABA** | ~08-20 | Grouped CALENDAR, scored 0 | +1.3% then **−8.6%** — but 08-21 was a broad tech de-rate day | **INCONCLUSIVE** |

**Four of four resolvable earnings calls confirmed, and every one of them was a decision to stand aside.** The lane's value this week was entirely in refusals: each name it declined to fade went on to move 4–11%. A short-vol structure on any of them would have been destroyed.

No PEAD candidates: DE and ROST show the strongest positive continuation but **both fail the C12 liquidity floor** and are excluded fail-closed; WMT and TJX were negative surprises; BABA's reaction is ambiguous.

### (b) Two-week lookahead

**The decisive population result: 0 of 15 names register `TAIL_HEDGING` on back-month skew (`--dte-target 60`); 11 of 15 are COMPLACENT.** No name in this book qualifies for full-size SELL VOL anywhere — a tool-verified corroboration of the negative-VRP premium-buying regime.

Second result: raw `KINKED` fires on 9 of 15 (60%), but only **4 of 15 (26.7%)** have the kink land at the earnings-adjacent tenor with the tenor clearing 15 contracts — **SNOW, LULU, DELL, AVGO**. The other five kink at 09-18 (Sept OPEX / near-FOMC) or 09-11 (CPI): **macro bleed misread as event pricing**.

A methodology limitation worth recording: for earnings 4–6 days out, the nearest surviving tenor (7 DTE) **is** the earnings expiry, so a kink-finder scanning interior points structurally cannot register it even when it is genuinely the curve's peak. Ten of fifteen names show this "front-collapsed-into-earnings" shape. For those, `front_end_ratio@7` is the operative gauge, not `kink_expiry`.

| Ticker | Earnings | Days | Shape | fer7 | Back-skew (60d) | Implied move | Play | JH collision |
|---|---|---|---|---|---|---|---|---|
| INTU | 08-25 | 4 | front-collapsed | 1.206 | +0.024 NORMAL | 9.40% | SELL VOL (half) | No |
| CRWD | 08-26 | 5 | front-collapsed | 1.096 | −0.001 COMPLACENT | 9.28% | **SKIP** | Borderline |
| CRM | 08-26 | 5 | front-collapsed | 1.347 | +0.004 COMPLACENT | 8.67% | SELL VOL (half) | Borderline |
| HPQ | 08-26 | 5 | BACKWARDATION | 1.547 | +0.0235 NORMAL | 10.03% | SELL VOL (half) | Borderline |
| **ULTA** | 08-27 | 6 | BACKWARDATION | 1.683 | +0.0306 NORMAL | 9.37% | **SKIP/AVOID** — last 5 prints averaged ~11.9% vs 2.86% implied | **Yes** |
| MRVL | 08-27 | 6 | BACKWARDATION | 1.274 | −0.0389 COMPLACENT | 11.95% | **SKIP** — front/back mismatch | **Yes** |
| ADSK | 08-27 | 6 | BACKWARDATION | 1.455 | +0.0076 COMPLACENT | 8.95% | **SKIP** | **Yes** |
| **DG** | 08-27 | 6 | BACKWARDATION | 1.633 | **+0.0362 NORMAL (most stretched)** | 9.00% | SELL VOL (best-of-book, still half) | **Yes** |
| OKTA | 08-26 | 5 | front-collapsed | **1.694 (highest)** | −0.0029 COMPLACENT | 14.15% | **SKIP** — coin flip | Borderline |
| DELL | 09-01 | 11 | KINKED but weak (6.7% prom) | 0.820 | −0.0146 COMPLACENT | 15.02% | **SKIP** | No |
| PANW | 09-01 | 11 | kink is **CPI**, not earnings | 1.123 | −0.0059 COMPLACENT | 19.71% | **SKIP** | No |
| MDB | 09-01 | 11 | peak at 7dte, unrelated to print | 1.442 | +0.0096 COMPLACENT | — | **SKIP** | No |
| **SNOW** | 09-02 | 12 | **clean KINKED at earnings** (23.0% prom) | 0.506 | +0.010 COMPLACENT | 14.96% | SELL VOL (half) | No |
| **LULU** | 09-03 | 13 | **clean KINKED at earnings** (14.1% prom) | 0.698 | −0.0094 COMPLACENT | 11.14% | **CONTESTED** — see §7 | No |
| **AVGO** | **CONTESTED** 09-02 vs 08-26 | 12 or 6 | KINKED at earnings *if* 09-02 | 0.818 | −0.0064 COMPLACENT | 9.88% | **Unsizeable — resolve the date first** | Depends |

**Four of the six nearest-dated names — ULTA, MRVL, ADSK, DG — print on 2026-08-27, the day Jackson Hole opens.** CRWD, CRM, HPQ and OKTA print 08-26, one day before. Every post-print IV-crush thesis in this book is carrying macro event risk stacked on top of single-name event risk.

**`analyst-vs-flow` is confirmed DEAD.** Run on SNOW/DELL/LULU/AVGO, every payload carries only `{options_flow, symbol}` — **zero analyst leg**. The "analyst-vs-flow disagreement is the highest-EV setup" framing depends on a leg that does not exist in this tool. No analyst-divergence score was assigned to any name.

---

## 7. Risk & Correlation (week-candidate universe)

**Correlation clusters** (`portfolio-correlation`, 30d, 16 symbols). One real cluster and one software pair:

- **`semis_memory_cluster` — INTC, AMD, SNDK, AVGO.** AMD/SNDK **0.856**, INTC/SNDK 0.828, INTC/AMD 0.788, INTC/AVGO 0.739. INTC kept (tie broken on |cum_flow_30d| in the trade direction: −$440.2M); **−1 tier to AMD, AVGO, SNDK**.
- **`enterprise_software_cluster` — INTU/CRM at 0.863.** Both at raw 1 with no `cum_premium_flow_30d` reported, so the specified tie-break field is unavailable; −1 tier applied to both rather than inventing a winner. Zero economic consequence — both are already `skip`.
- Soft watch (0.60–0.70, no penalty): INTC/SPY 0.642, DG/CRM 0.661, IWM/INTC 0.621, GLD/MSTR 0.620, LULU/DG 0.610, HPQ/CRM 0.602. AMD/INTU at **−0.622** is a genuine negative pair.
- **The most important number here is IWM/SPY at 0.833.** SPY is not a W34 candidate so no tier deduction is owed, but an IWM short is 83.3% the same trade as an SPY short — index beta wearing a Russell ticker, which is precisely the expression the short-routing rule exists to stop sizing.

**Substrate defect, reported not propagated:** `sector_breakdown` returned `{"Unknown": 16}` with a spurious `CONCENTRATION: 100% of tickers in Unknown` warning. That is a null sector-mapping artifact, not a finding. Discarded; the `high_correlations` array itself is sound.

**Macro & event risk** — see §1. Jackson Hole is Tier-1 by impact but is **not** in the enumerated `{CPI, FOMC, NFP, PCE}` set, so it fires no gate. That is the rule as written and it was not stretched; it is carried in narrative, where it is the single best reason not to open uncompensated directional exposure. Core PCE at T+5 does fire, on the five undefined-risk short-vol structures.

**Fundamentals verdicts (top-5):**

| Ticker | Verdict | Contradicting facts |
|---|---|---|
| IWM | **NA** | Russell 2000 basket — no issuer. NA never penalizes. |
| GLD | **NA** | Gold trust — no issuer. News stack *corroborates*: gold >$4,600/oz, +14% in August, biggest monthly gain since 1999. |
| **LULU** | **CAUTION** (−1) | The **08-20 VETO was overturned**. The formal triad actually favours the long — beat streak 3-of-4, **MSPR +78.42, the strongest insider reading in the top-5**. Held at CAUTION on two dated 08-14 governance events (Soros Fund Management fully dissolved its stake; AI Chief exited pre-CEO-transition), `fz inst_trans` −0.50%, and insider data **stale since June**. |
| **INTC** | **CAUTION** (−1) | Beat streak 4-of-4 fights the short — but it is **low-information**, measured against near-zero estimates ($0.014, $0.01). Still unprofitable at **−19.79% net margin**, revenue +7.47%. Insider genuinely neutral (MSPR −1.48). 1-of-3 axes ⇒ below the 2-of-3 VETO bar. |
| **AMD** | **VETO** | Textbook "fundamentals fight the short": beat streak **4-of-4 and accelerating**, revenue **+39.54%** YoY, EPS **+124.33%** YoY, margins clean (GM 53.2% / OM 15.71% / NM 15.58%). The sole bearish leg (MSPR −47.86) is **chronic — negative in 14 of 20 months** = routine 10b5-1 with ~0 abnormal information. Three bullish analyst actions in-window incl. BMO Outperform, $550 PT. |

**Debate-disconfirmation cuts.** Three of five debated names are shorts, which inverts the roles: the bull was briefed to argue *against* the call. The gate was applied on **"did the disconfirming side win"**, and both readings are recorded because they diverge on three rows.

| Ticker | Dir | `{bull, bear}` | Defender | Disconfirmer | Applied | Literal frozen rule |
|---|---|---|---|---|---|---|
| IWM | short | {0.55, 0.45} | bear 0.45 | **bull 0.55** | **−1 tier** | no-op (diverges) |
| GLD | long | {0.35, 0.45} | bull 0.35 | **bear 0.45** | **−1 tier** | −1 (agrees) |
| LULU | vol | {0.35, 0.65} | bull 0.35 | **bear 0.65** | **−1 tier** | −1 (agrees) |
| INTC | short | {0.45, 0.65} | **bear 0.65** | bull 0.45 | no-op | −1 (diverges) |
| AMD | short | {0.65, 0.25} | bear 0.25 | **bull 0.65** | **−1 tier** | no-op (diverges) |

**This is a rule-specification gap, flagged for `/calibration-audit` and deliberately not retuned.** It costs zero dollars this week because every affected name is already `watch_only` or `skip`.

**Two debate findings matter more than the residual arithmetic:**

1. **GLD — a genuine scoring defect, found by the bull and independently verified and conceded by the bear.** Decomposing `cum_premium_flow` by window gives 5d **+$28.4M** / 10d −$73.2M / 15d −$99.3M / 20d −$302.3M / 30d −$275.2M. The bearish mass is ~−$203M in 07-27→07-31 and ~−$101.6M in 08-10→08-14 — **both pre-date the structure being scored**, and the five sessions that actually contain the multileg rolls and the +5.45% move are net **bullish**. The bear's own words: *"the −3 flow_conflict deduction that turns this from LOW into DROP is stapling two stale liquidation events from three-plus weeks ago onto a structure that started forming after them. That's a real methodological flaw in the score."* Both sides also verified GLD's 08-21 dark-pool tiers as **buy**-leaning (block 0.563 on 79 trades/$175.5M; large 0.64 on 2,869 trades/$635.9M) on the very day cited as distribution. The bear's surviving counter: the **mega tier (≥$10M) was 100% SELL in both GLD (2 trades/$31.8M) and GDX (2 trades/$96.45M)** that session — a minority-of-trades argument against a majority-of-trades one. **The score was not overridden.** This goes to the audit.

2. **LULU — the largest bearish number in the book is mis-attributed.** The −$452.0M / 43.13%-of-gross reading is a **2026-12-18** book ($106.1M, 99.8% puts) at strikes **$300 and $350 against a $115–121 underlying**, deltas −0.83 to −0.91, recurring daily in the same 90-minute after-close window. That is 2.5–3× notional-ITM — pure intrinsic, near-zero vega — **expiring 3.5 months after the earnings print**: a rolling collar against an existing equity long, not directional conviction. The actual earnings tenor (09-04) carries **$1.035M and is call-leaning** ($577K call / $458K put). The bear verified this, conceded it, then correctly noted that defeating a bearish number does not manufacture a bullish one — and raised an unresolved question: the collar's observed window (08-14 onward) is **exactly coincident with the Soros exit**, so it may be that unwind expressed structurally. Unresolved either way; not sizeable.

**Breadth cross-check (advisory):** 332 advancers / 169 decliners, **66% green**, top mover HOOD +13.7%, worst MRVL −5.57%. `divergence_flag: true` against 39.2% bullish options-flow breadth. No size impact.

**Adverse-flow exits from the carried `conviction_week_2026-W33` group (IWM, SNDK, AVGO, SPY, NBIS):**

`watchlist alerts` carried **no information today** — it fired `LARGE_DARK_POOL` on ~85 of ~90 names (~94%) at closing-cross-scale notionals on an OPEX Friday (SPY $575.8M, SNDK $498.6M, IWM $450.0M). Discarded; `watchlist scan` used instead.

- **SNDK — EXIT.** Bullish net flow **+$25.9M against a short thesis**, and its score collapsed to −3.
- **NBIS — EXIT.** Silent thesis decay; net flow effectively zero at $214k, with no hard alert fired.
- **IWM — carry.** Flow still thesis-consistent a week later (bearish, −$28.2M, P/C 1.842).
- **AVGO** — thesis intact but **earnings date CONTESTED (08-26 vs 09-02)**; unsizeable on horizon indeterminacy alone.

**Hedge sleeve: none — and proposing one would increase risk.** The book has zero sized positions and net delta of zero. A SPY put vertical or VIX call ladder bought against a flat book is not a hedge; it is a naked directional bet on Jackson Hole wearing a hedge's clothing. The correct hedge for an empty book into a new Fed Chair's debut is **cash**.

---

## 8. High-Conviction Cross-Ref (HIGH and MEDIUM tier)

**Empty — no name reached HIGH or MEDIUM.** The highest score in the book is IWM at raw 5 (LOW), and it routes to `watch_only`.

Because nothing reached ≥9, the **Step 3a load-bearing-tool gate never triggered**. That is worth stating explicitly, because it means the `block-stratified` instability documented this week (mega `buy_ratio` swinging 0 → 1.0 day-to-day on every name — MU printed 0.474 / 0.946 / 0 / 0.868 / 1.0) is **not load-bearing on any call this week**. It would have been, had anything scored HIGH.

**Expectancy lens (advisory, C31):** not computable this cycle. With zero sized calls this week and no HIGH/MEDIUM band population post-freeze, there is no tier × expectancy table to display. The standing observation from prior audits holds: the **DROP pile has repeatedly outperformed the traded book** (0.440 vs 0.435 at 2026-08-01; 43.3% vs 41.1% at 07-18; 0.477 vs 0.406 at 07-11).

**Embedded rubric (for audit) — FROZEN, version `2026-06-12`:**

```
Weekly conviction score = Σ:
  +3  uw historical oi-trend BUILDING for the full week, --days >= 5   [WEEKLY-ONLY +3 vs DAILY +1; register C47]
  +3  3+ aligned signals in accumulation-hunter sustained across week, uw dark-pool block-stratified
      institutional-tier confirmed — CONJUNCTION (C11): full +3 only when cum_premium_flow_30d confirms
      (sign aligned AND |cum_flow_30d| >= $50M); else halved (floored) +3 -> +1
  +1  uw insights conviction-matrix = DIRECTIONAL_LONG, confidence > 70, stable WoW — CONDITIONAL:
      award only when dominant_signal_class == leap_directional; 0 in all non-LEAP contexts
  +2  uw oi position-rolls shows institutional roll forward into longer-dated LEAP (per covered date)
  +1  uw historical cumulative-premium-flow net directional accretion across the week — INTENT-SCREENED:
      (a) no C28 distribution_flag on the name, AND (b) on dividend payers in an ex-div window the
      accreting prints are NOT deep-ITM sub-parity calls. Screen failed or unevaluated -> 0
  +1  dealer-positioning-strategist MECHANIZED DEX flip or vanna squeeze in trade direction — verified
      SIGN CHANGE only, via scripts/dex_flip.py; whipsaw_warning mandatory to report
  +1  sector-rotation-strategist names ticker as single-name leader within rotating sector — CONDITIONAL:
      (a) sector persistence_score >= 0.6 AND (b) cum_flow_30d aligned AND (c) |cum_flow_30d| >= $50M
  +1  earnings-scout BUY VOL or SELL VOL for next 2 weeks (term-skew aligned for full size)
  +2  multileg-strategist directional structure repeated on >= 2 days (term-structure-anchored play type)
  +1  vol-surface-scout flags KINKED or BACKWARDATION, worsening WoW; iv-percentile-zscore extreme; VRP-aligned
  +1  opex-pin-strategist ranks ticker top-5 (OPEX week only)
  -2  contrarian-scanner crowded long with rising pc-ratio-zscore trajectory (VRP positive)
      [MECHANISM: informed-flow CONTINUATION penalty, not "fade the crowd"]
  -3  flow_conflict — cum_premium_flow 30d direction clearly opposite dominant_signal_class
  -1  flow_conflict_lite — 30d cum_premium_flow read is MIXED   [mutually exclusive with flow_conflict]
  # TIER GATES applied by risk-monitor in 2d; contribute 0 to raw_score, never in score_components:
  #  -1 TIER  correlation cluster (pairwise corr >= 0.70)
  #  -1 TIER  WoW market-regime flip conflicts with trade direction
Tiers: >=9 HIGH (full) | 7-8 MEDIUM (half) | 3-6 LOW (starter/watch) | <=2 drop
```

**Rubric lines that earned zero across the entire book, and why:**

| Line | Why it paid nothing |
|---|---|
| +3 accumulation conjunction (C11) | accumulation-hunter returned **zero** qualifying names — 18 candidates decontaminated, all disqualified. The conjunction gate was never reached. |
| +2 `position-rolls` into LEAP | Only 4 single-date rolls exist in the whole book, and **not one far leg is LEAP-dated** (the tool's near/far boundary is 21 DTE; every far leg sits at dte 22–56). |
| +1 mechanized DEX flip | **Zero of 15 names** produced a verified sign change across 14 ISO dates. AVGO near-missed at `magnitude_ratio` 0.93 vs a 1.0 floor; COIN/MSTR/TSLA were whipsaw-disqualified (5–6 sign changes in 14 sessions). |
| +1 opex-pin top-5 | Empty book — August OPEX expired 08-21, next monthly is 28 days out. |
| +1 conviction-matrix | Conditional on `leap_directional`, which only MSTR satisfied — and MSTR reads MIXED at 5.8%. |
| +1 sector leader | Only MRNA nominated; fails gates (b) and (c). Gate (a) is non-discriminating (10-of-11 sectors INFLOW). |
| −2 contrarian crowded long | **Zero BULLISH_EXTREME out of 91 names.** Also, the "(VRP positive)" precondition fails on the Nasdaq complex. |
| +1 vol-surface KINKED/worsening | Paid once (MSTR). The "iv-percentile extreme" sub-condition was **unavailable on all 15 names** (`dates_used` 92 < 120 floor). |

---

## 9. Setups for Next Week

### Next-session GEX advisory — SPY and QQQ only (prose-only, 0 rubric points)

**Framed by its track record first: the Step-0 rolling backtest verdict is `NO_GO_NO_EDGE`.** Over n=118 pooled sessions the next close landed closer to the nearest EOD wall only **19.5% of the time against a 50% baseline** (p=1.0 in the magnet direction) — the walls are **anti-magnets**. Pin direction was a coin flip at exactly 50.0%. H1 (short-gamma → higher realised vol) now runs the right way (0.838 vs 0.775 mean abs return) but the effect is small. What follows is dealer context, not an edge.

- **SPY** — spot 765.69. Regime `FULLY_NEGATIVE`, `total_gex` **−894.8M** (label and sign agree today). **ZGL null ⇒ `zgl_reliable: false`.** Call wall **780** (+73.8M, a real local peak). The raw put wall at 765 (−678.3M) **is the expiring OPEX ATM spike, not a Monday level** — stripping the 763–767 band, the durable shelves are **760** (−192.2M) and **755** (−49.5M). Read: dealers net short gamma across the surviving book ⇒ trend-amplifying hedging, not a pin. Structure bias: defined-risk directional over premium-selling; do not build an iron fly around 765.
- **QQQ** — spot 713.23. Regime label reads `POSITIVE` but `total_gex` is **−18.8M (negative)** — **the label contradicts its own sign**, and this happened on 4 of 6 sessions this week. ZGL prints **207.89 — over 70% below spot**, so `zgl_reliable: false`. This is not a one-off: the week's ZGL series ran 734.54 → 261.7 → 208.83 → 207.89, i.e. once the regime destabilizes the extrapolation collapses to a recurring garbage floor. Call wall **730** (+56.5M); stripping the expiry spike at 713, there is negative GEX on **both** sides of spot (700 at −71.3M, 718 at −65.4M) — a genuinely unstable book. Combined with QQQ's negative VRP, this favours long-vol over any short-premium structure.

**Mandatory caveats:** this is the standing 0–45d book pulled tonight and Monday's fresh 0DTE OI will reset the near-strike map; it is the **ETF** book, not the cleaner SPX/NDX index book; the CLI **cannot isolate the D+1 expiry** (`--dte-max 1` errors); and **post-OPEX depletion is the dominant caveat this week** — the 08-21 expiry ($6.56B premium, the second-largest bucket on the whole forward curve) is now gone, and the 08-28 ($2.58B) and 09-18 ($7.21B) buckets have not backfilled it yet. Expect the map to be unusually unstable into Monday.

### Next-session 0DTE premium-selling setup (advisory, 0 rubric points)

Rolling backtest verdict: `GO_PREMIUM_SELL_INTRADAY` (n=60 per index). **But read the VIX conditioning before acting on it, because the `sell_premium: true` flag is unconditional and this is a LOW-vol tape.**

| | SPY | QQQ |
|---|---|---|
| `vol_state` / VIX | **LOW** / 15.13 (tercile bounds 16.0 / 17.3) | **LOW** / 15.13 |
| implied move | 0.38% | 0.66% |
| expected range | 1.18% | 1.98% |
| `size_scalar` | 0.5 | 0.5 |
| mean PnL open, gross | 0.202% | 0.336% |
| **mean PnL open, NET** | **0.102%** | **0.236%** |
| **mean PnL at LOW VIX (gross)** | **0.060%** | **0.151%** |
| **LOW VIX minus 0.1% cost** | **−0.04% — NET NEGATIVE** | **+0.05% — marginal** |
| worst day | −1.4% | −2.453% |

**The SPY lane is net-negative at the current VIX tercile and should be stood aside.** QQQ is marginally positive and not worth the tail. The edge in this stack lives in the MID and HIGH VIX terciles (SPY 0.215 / 0.331; QQQ 0.365 / 0.493), not here. Structure if traded: wider iron condor, wings ≈ ±1.18% (SPY) / ±1.98% (QQQ), entered at/after the open once the overnight gap resolves, **never carried overnight**; stand aside on a VIX spike or front-end backwardation. PnL is quoted as **% of underlying spot notional, gross** — not premium-collected, not margin-relative. **The tail is unsampled** — there is no vol shock in the 60-day window, and short vol is negatively skewed. This stays advisory and 0 points permanently until a vol-shock day enters the sample and net expectancy clears a tail-aware bar.

### Swing setups, pin regime, and the actionable list

**dealer-positioning:** nothing scored. The one carry-forward is a **substrate-confirmed SPY short-gamma regime flip** (`total_gex` flipped positive→negative on 08-17 and held all five sessions; 30-day context shows 11 consecutive positive sessions before that, so the flip is real, not a one-day artifact). QQQ's version flipped 08-18 but is essentially flat by week-end (−18.7M). IWM's GEX sign is choppy in both 10d and 30d windows — no clean regime. **AVGO is the near-miss worth re-testing**: DEX flipped negative on 08-14 and held six sessions, failing the magnitude floor by a hair (`magnitude_ratio` 0.93, `sign_changes_in_window` 1 — no whipsaw). Re-run `dex_flip.py` on 08-24→08-28; if the run persists above the floor it becomes a scored `dex_flip_short` next week.

**Vanna:** no squeeze fires anywhere. Two books are put-heavy (IWM `net_vanna` +22,611, AVGO +5,234) but the VIX path was **choppy, not falling** — 15.19 / 15.84 / 14.89 / 16.01 / 15.13 — and a squeeze requires a clean ≥3-session decline. "Vanna pressure" at most.

**Pin vs trend regime call: TREND, weakly.** Both indices are short-gamma on the surviving book, which is amplifying rather than dampening, and the walls-as-magnets hypothesis is measured at 19.5% against a 50% baseline. Do not trade pins.

**OPEX book: none.** August OPEX expired on 08-21 and the next monthly is **2026-09-18, 28 days out** — too far for OI to have concentrated into a real pin structure. `pin-risk` was confirmed to have **no expiry-selection flag**: even with `--dte-max 30`, all 30 returned rows carry `dte_to_opex: 0`. Using `opex-concentration` instead, SPY/QQQ/IWM produce **zero matches** (OI too distributed for any single expiry to clear a 1% concentration threshold), and the sole forward funnel candidate — DCI, 09-18, 100% concentration — dies on `pin_distance_pct` 3.44% > 2% with a thin 1,976 total OI.

**Two to three highest-conviction actionable setups: there are none.** No HIGH-tier name exists. The honest actionable list for the coming week is:

1. **Stand aside into Jackson Hole.** A new Fed Chair's first policy speech plus a hot core PCE print at T+4/T+5, against a book with no sized positions, is a week to hold cash rather than manufacture exposure.
2. **Watch IWM's put program for a tell.** If the 283–286 strikes start printing bid-side (unwind) rather than ask-side, the structure was insurance and the read is dead. If it keeps opening through another down-leg, it was scaling.
3. **Re-test AVGO's DEX flip** on 08-24→08-28 against the magnitude floor, and **resolve AVGO's contested earnings date** (08-26 vs 09-02) before considering any vol structure.

**LOW-tier names to track for daily confirmation:** IWM (the only LOW name in the book).

**Deep-dive hand-off:** skipped — no HIGH-tier, non-VETO names exist. This is a no-edge week.

---

## 10. Watch-only — single signal, no confluence

Surfaced by exactly one Phase 1 agent and excluded from the trade book. Listed for journaling only, **not** for entry.

- **SNDK** (sweep-tracker, bearish 5-of-5, $2.45B, direction unconfirmed) — also carries +$1,185.8M of 30d bullish premium running against the sweep read, and is on this week's exit list.
- **SPCX** (sweep-tracker, bearish 5-of-5, $1.30B, unconfirmed).
- **AMD** (sweep-tracker, bearish 5-of-5, $1.15B, unconfirmed) — fundamentals VETO'd the short.
- **MRNA** (sector-rotation Healthcare leader +$14.3M vs sweep-tracker bearish 3-of-5 vs a clean opening Tier-1 put — genuinely three-way conflicted, and **+129.2% on the week with rv20 at 371%**).
- **JNJ** (sector-rotation Healthcare leader, +$7.3M — one agent only).
- **SOFI** (sector-rotation, KRE regional-bank subsector, instrument-only, no GICS confirmation).
- **HOOD** — the clearest crowding-penalty case in the book: call-crowded (pc z −1.437), **+13.7% in a single day** (the week's top mover), bullish net flow $36.1M, and `front_end_ratio@7` crossing into panic at 1.026→1.129. A HOOD long sizes **down** for crowding, not up.
- **NTAP** (vol-surface handoff — iv_rank 100, earnings 09-02, but `NO_NEAR_TENOR` both weeks; term-structure lane cannot classify it).
- **CG** — a collar (short 52.5C bid + long 40P ask, exact size match 100,000, exp 09-18). Protective hedge on an existing holder's book into Jackson Hole, explicitly **not** alpha.
- **AAPL** — not a candidate in either direction, but carrying the week's only cross-validated **C28 distribution flag**: a Wednesday clean-buy of +$1.26B almost exactly unwound by Friday's clean-sell, `institutional-accumulation` flipping NEUTRAL (1.36) → **DISTRIBUTION (0.49)**, and non-0DTE 28-DTE call OI closing −3,275 contracts. Counts against any AAPL long thesis. Secondary cautions: **NEE** (three clean non-closing-cross sells on 08-20 totalling $408.2M with zero offsetting buys) and **NVDA** (net-sell isolated flow on 4 of 5 days, ~−$131M on the week).

**Refuted this week — do not carry forward as live hypotheses.** The daily fleet flagged QQQ-short and GDX during the week; multileg-strategist refuted both. QQQ showed P705 **ask-side bought** on 08-19 against P685 and P660 **both bid-side sold** (exact size match 37,000) on 08-20 — opposite aggressor signatures 24 hours apart on the same expiry pool. GDX resolves to two unrelated books at different horizons: a Nov-20 75P/85P tail-hedge vertical and a near-ATM Aug-28 104C.
