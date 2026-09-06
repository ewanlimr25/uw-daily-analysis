# Weekly Market Intelligence — Week of 2026-08-31 (ISO 2026-W36)

## Executive Summary

- **Week regime + WoW Δ:** `TRANSITIONAL — Mixed signals, reduce position size, wait for clarity`, **HELD** Monday to Friday with no label change; options-flow breadth improved trivially (33.8% → 35.4% bullish) but stayed **majority-bearish at both ends**. VRP is **flat-to-slightly-negative** (SPY −0.0011, QQQ −0.0272, both `FAIR`) — **not a premium-selling week**, a mild premium-*buying* tilt.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`.
- **Signal performance:** **1 of 3 resolved (hit rate 1/3 = 33.3%); 3 INCONCLUSIVE excluded; 6 total calls in universe (6 envelope-anchored, 0 reconstructed).**
- **Top swing build for next week:** **NONE.** No candidate reached even LOW tier. Highest raw_score in the book was **+2 (MSTR, SNDK)** against a LOW floor of 3.
- **Top LEAP build:** **NONE.** The LEAP book is empty — nothing cleared 6-of-9 gates, and market-wide `share_leaps` faded 4.1% → 3.1% across the week.
- **Biggest emerging risk:** The week's one apparent edge — a "Technology inflow" — is **not a rotation and not diversified**. Netted Tech flow tripled to +$435.3M, but every deep-pulled Tech ETF *disagrees* (SMH −$71.6M, IGV −$10.2M), the inflow is four names (MU/SNDK/MSTR/INTC), and **MU and SNDK correlate at 0.91**. That is one crowded memory/AI-hardware bet wearing a sector-rotation costume, into a CPI + FOMC + OPEX fortnight.

---

## 0. Week in Review — Intra-Week Signal Performance

Universe = the union of non-DROP `calls[]` across this week's five daily `decision.json` envelopes, keyed by `(ticker, direction)`, graded from each call's own envelope date forward to 2026-09-04. All five daily envelopes exist, so **every row is envelope-anchored — zero hindsight reconstruction**. INCONCLUSIVE = |move| < 0.5×ATR(14).

| Ticker | Direction | Source | Move vs ATR | Flow/OI | Grade | Note |
|---|---|---|---|---|---|---|
| IWM | short | envelope 2026-09-01 | +5.44 (**−1.85×ATR** against) | cum-flow 5d **+$19.7M** MIXED (against) | **LOSS** | Called short three days running (09-01/02/03); IWM rallied every one of them |
| NBIS | long | envelope 2026-09-02 | +22.30 (**+1.39×ATR** for) | 5d **+$33.8M BULLISH**, OI building | **WIN** | The only resolved winner; flow corroborated direction |
| GLD | short | envelope 2026-09-03 | −3.45 (+0.41×ATR for) | 5d **−$68.0M BEARISH** (for) | INCONCLUSIVE | Right direction, flow aligned, move short of the 0.5×ATR bar |
| MSFT | long | envelope 2026-09-03 | −10.42 (**−0.99×ATR** against) | 5d −$60.1M MIXED (against) | **LOSS** | Flow and price both went against within one session |
| MSTR | long | envelope 2026-09-03 | −2.02 (−0.20×ATR) | 5d **+$238.0M BULLISH** (for) | INCONCLUSIVE | Flow strongly for, price flat |
| NVDA | long | envelope 2026-09-04 | 0.00 (0.00×ATR) | 5d +$128.9M MIXED | INCONCLUSIVE | Zero-length window by construction (called on the last covered day) |

**Read the denominator, not the hit rate.** Three of six calls could not resolve, and one of those three had a window of zero days. A 33.3% hit rate on n=3 carries essentially no information — it is reported for the record, not as a performance claim. What *is* informative: **every one of these six was already `skip` or `watch_only`**, so the book's realised P&L for the week is zero by construction. The IWM short lost three separate times and cost nothing, because short-direction routing held.

---

## 1. Regime & WoW Delta

The regime label did not move: `TRANSITIONAL — Mixed signals` on both 2026-08-31 and 2026-09-04. **That stability is partly an artifact and must be stated:** `uw risk market-regime`'s `spy` sub-block is **not date-pinned** — it returned byte-identical values for both dates (`current 770.19`, `sma_20 769.05`, `sma_50 756.86`, `change_30d_pct 0.21`), so its `trend: UPTREND` field is today's snapshot printed twice, not a week-over-week read. Only the breadth and `sector_rotation` legs actually honour `--date`. The price path below was therefore recomputed independently from `uw historical trend`.

**Verified tape.** SPY 769.35 (08-28) → 767.05 → 761.78 → 765.16 → 773.17 → **770.19**, i.e. **+0.11% on the week** with daily prints of −0.30 / −0.69 / +0.44 / +1.05 / −0.39%. QQQ +0.35%, IWM +0.09%. This is chop, not trend.

**The week's defining fact is beneath the index.** Equal-weight **RSP fell −0.77%** while cap-weighted SPY rose +0.11% — an **88bp cap-weight divergence**, meaning the median S&P constituent declined while the index was flat. The `fz` breadth cross-check agrees from a separate data lineage: 175 advancers vs 327 decliners, **pct_green 34.79%**, average change −0.43% (top mover SNDK +11.9%, worst LULU −17.38%). Leadership narrowed sharply.

**A second divergence sits inside the flow.** SPY's `flow_direction` flipped bullish → **bearish on 09-01 and stayed bearish every remaining session** (net −$14M, −$27M, −$20M, **−$83M**), with Friday the most negative reading of the week — while price closed flat-to-up. Options flow and price disagreed all week.

**Volatility is at the floor.** SPY iv30 11.6% / iv_rank **4.8**; QQQ 17.1% / 16.7; IWM 16.2% / **1.7**; VIX 14.53. A mid-week IV bump on 09-01 (SPY iv_rank 13.8) fully round-tripped by Friday.

**Horizon mix.** `dte-volume-share` weeklies ramped 4.6% → 20.6% into Friday's expiry (mechanical), monthlies flat at ~19–23%, and **LEAP share faded 4.1% → 3.1%** — institutional long-dated participation receding. ⚠ `share_0dte` returned **exactly 0 on all five days**; market-wide 0DTE share is never zero, so that field is defective and was not used.

**Macro backdrop.** Core CPI 2.79% YoY, **core PCE 3.34%** (well above target), unemployment 4.1%, payrolls +162k, **10Y 4.77% and rising +14bp/30d**, 2Y 4.34%, curve +41bp normal, broad USD weakening (120.79 → 118.75), fed funds 3.63%, SOFR 3.66%. Sticky core inflation with a long end selling off while the policy rate sits at 3.63% is a steepening, term-premium backdrop — a headwind to duration and to long-dated equity optionality, which is consistent with the fading LEAP share.

**Event risk, next two weeks — all of it inside a 1–4 week swing horizon:**

| Date | Event | Impact |
|---|---|---|
| 2026-09-10 | PPI (Aug) + initial jobless claims | medium |
| **2026-09-11** | **CPI (Aug), 08:30 ET** | **high** |
| **2026-09-15/16** | **FOMC + Summary of Economic Projections (dot plot)** | **high** |
| 2026-09-17 | Initial jobless claims | low |
| **2026-09-18** | **Monthly OPEX / triple witching** | **high** |

The Fed quiet period began 2026-09-05. **Implication for next week's bias:** three high-impact events inside ten sessions, against index IV at its one-year floor, argues for owning optionality rather than selling it, and against initiating directional swing risk before 09-11.

---

## 2. Sector Rotation

**Rotation regime call: `no_change`, confidence LOW.**

Direction is read exclusively off the **netted** `uw risk market-regime.sector_rotation`. ⚠ `uw options-flow sector-flow-persistence` is **gross turnover, sign-agnostic** — it printed **INFLOW at persistence 1.0 on 7 of 11 sectors** this week (Healthcare, Financial Services, Basic Materials, Consumer Defensive, Energy, Communication Services, Technology), plus two at 0.8. That is near-zero discrimination, the documented defect; it is used here only as a durability filter and is structurally incapable of corroborating any netted *outflow*.

| Sector | Netted 08-31 | Netted 09-04 | Gross persistence | Verdict |
|---|---|---|---|---|
| **Technology** | +$150.1M | **+$435.3M** (~3×) | 1.0 INFLOW | **Only sector clearing every gate** |
| Financial Services | — | +$23.8M | 1.0 INFLOW | Narrow; crypto-adjacent, not banks |
| Utilities | — | +$7.0M | 0.6 ROTATING | Below-median magnitude — watch-only |
| Consumer Cyclical | **+$77.1M (top-3 IN)** | **−$121.8M (largest OUT)** | 0.8 INFLOW | **Direction FLIPPED mid-week ⇒ disqualified** |
| Communication Services | −$25.7M | −$75.6M (widening) | 1.0 INFLOW | **Netted-vs-gross conflict ⇒ watch_only** |
| Industrials | −$65.2M | −$39.2M | 0.6 ROTATING | Conflict + weakest persistence ⇒ watch_only |

Note this is a **top-3 / bottom-3 truncation** — sectors outside the six named are unreported, not zero.

**ETF flow tape (advisory — 0 rubric points).** 33 of the ≤40-call budget used (21 rank + 12 deep-pull).

| ETF | Net premium (5d) | Persistence | DP positioning | Options urgency | GICS agreement | Leaders |
|---|---|---|---|---|---|---|
| **EWY** | **+$12.25M** | BULLISH | Large blocks, mixed vs-mid | **Bullish** — 2027-dated call sweeps ($160C/$245C blocks; $200C 134-trade ask-side sweep) | n/a (Korea) | — |
| **XLK** | +$7.99M | BULLISH | Small near-mid prints | Mixed 0DTE noise | **agree** | MU, MSTR, SNDK, INTC, MRVL |
| **XLC** | +$0.33M (thin) | BULLISH | No signal | Empty | **disagree** | none |
| **IGV** | **−$10.19M** | BEARISH | Sell-side prints | Bearish — Dec $100P bought, Nov $109C sold | **disagree** | none |
| **KRE** | **−$5.10M** | BEARISH | Near-mid, no urgency | Empty | **disagree** | none |
| **SMH** | **−$71.59M (largest outflow in the tape)** | BEARISH | $110M block above ask + $38M below mid — noisy | Bearish — $24.3M Jan-27 $580P, $15M Oct-16 $535P bought | **disagree** | none |

Rank-only: XLV +0.57M · XLI +0.36M · TAN +0.32M · EWT +0.07M · XLB −0.0003M · XLRE −0.04M · XLU −0.45M · XLY −0.56M · ITB −0.57M · XLP −1.16M · XLF −1.28M · XLE −1.30M · XBI −1.47M · XOP −3.17M · GDX −6.09M.

**The cross-confirm is the finding.** Every deep-pulled ETF that maps to a "rotating-in" GICS sector **disagrees with that sector's netted direction** — XLC, IGV, KRE and SMH all contradict; only XLK agrees, and thinly. Broad semiconductors (SMH) were the single largest outflow in the tape *at the same time* MU and SNDK posted the two largest single-name inflows. The "Technology rotation" is therefore a **concentrated memory / AI-hardware trade in four names**, not a sector move — and the Financial Services print is carried by IREN and CRCL (crypto-adjacent) while KRE, the actual banks, bled.

**Named leaders.** Technology: MU +$143.9M, MSTR +$142.3M, SNDK +$90.9M, INTC +$42.6M, MRVL +$15.7M. Financial Services: IREN +$12.2M, CRCL +$7.6M. Utilities: VST +$6.3M (a power/AI-datacenter name, not a classic defensive).

**Swing implication.** If one were to express the Tech read at all, it would be through named single names rather than XLK/SMH beta — the ETF tape shows sector exposure would fight the single-name signal. But see §7: MU/SNDK correlate at **0.91**, so "MU and SNDK" is one position, not two.

---

## 3. Swing Book (1–6 weeks)

### 3a — Long swings

**EMPTY.** No long candidate reached LOW tier (raw_score ≥ 3). The two highest-scoring names in the entire book, MSTR and SNDK, scored **+2**.

### 3b — Short / fade swings

**EMPTY as a sized book — by routing, not by absence of ideas.** Short theses were generated, scored and serialized in full (IWM, AVGO, META below); every one routes to `watch_only` under the 2026-08-01 P0 short-direction rule and is never sized. Their counterfactuals continue to resolve.

Full scoring for every candidate that cleared the ≥2-agent confluence gate:

| Ticker | Dir | Tier | Score | Win-rate | Final size | Thesis | Invalidation |
|---|---|---|---|---|---|---|---|
| MSTR | long | DROP | **+2** | NA(substrate) | skip | Tech netted-inflow leader; 30d cum-flow +$334.0M (+4.10% of gross) aligned | 30d cum-flow sign flips negative, or the 90d (already −$214.4M) fails to converge |
| SNDK | long | DROP | **+2** | NA(substrate) | skip | Cleanest accretion in the book — 30d +$968.2M (+2.11%) and 90d +$2,853.8M (+2.09%), no decay across windows | Buy-ratio consistency breaks again (already 0.515 on 09-03); DP price sanity unresolved |
| MSFT | long | DROP | +1 | NA(substrate) | skip | 30d cum-flow +$784.8M (+5.13% of gross, `BULLISH` label), best net-as-%-of-gross among mega-caps | 90d decays to +0.16% — the decay falsifier is already firing |
| IWM | short | DROP | +1 | NA(substrate) | **watch_only** | 30d cum-flow −$230.8M (−4.39% of gross, largest of the majors); DEX negative 11 straight sessions | DEX magnitude already decaying (−16.8B → −2.6B); crowding fully unwound |
| AVGO | short | DROP | +1 | NA(substrate) | **watch_only** | Sweep-persistent bearish 5/5 sessions; 30d cum-flow −$82.8M aligned | Sweep lane scores 0 points by construction; alignment margin is thin (−1.18% of gross) |
| MU | long | DROP | **0** | NA(substrate) | skip | Only name whose dark-pool buy-lean survived the closing-cross strip 5-of-5 days | Already invalid: 30d cum-flow is −$105.5M, opposite the thesis |
| META | short | DROP | **−1** | NA(substrate) | **watch_only** | Most persistent Tier-1 opening-PUT name (3 of 5 sessions) | 30d cum-flow is **+$197.7M — opposite the short thesis** ⇒ flow_conflict_lite |
| PCG | — | DROP | 0 | NA(substrate) | **watch_only** | 3-day repeated multileg — but it is OTM **call selling** (COVERED_CALL), net-short-vega | Structure caps upside by design; not a directional thesis |

**⚠ Distribution caution (C28).** **MU carries a `distribution_flag`:** on 09-04, call-side OI closed above the $100K institutional floor across tenors — `MU261016C00910000` (42 DTE, OI −366, **$15.27M** closing premium), a **469-DTE LEAP** call close ($4.92M), `MU261016C00900000` ($6.07M), plus four smaller 5–28 DTE call closes. Institutions were unwinding bullish calls in the same week as the dark-pool buy-lean. Advisory, 0 points, no size change — but it is the reason MU's cum-flow line scores zero.

**Invalidation anchors (C34)** use the **second-tier** dark-pool shelf, never the top bucket (which is the closing cross). For MU: the pre-breakout institutional defence zone was **$943–947** (98.1M / 96.6M / 91.6M premium, 191–233 trades each, built 08-31 → 09-03); post-breakout Friday's second-tier shelf moved to **$1,000** ($99.6M, 233 trades) against a $1,016.59 close.

---

## 4. LEAP Book (6–24 months)

**EMPTY.** No ticker cleared the 6-of-9 gate. Disqualifications, with reasons:

- **PCG** — real dark-pool accumulation (buy/sell 1.91, $92.9M clustered tightly at $14.02–14.30, a genuine institutional defence level) and a **genuine unsaturated** 8-day OI build. But it appears **nowhere** in `oi biggest-increases --min-dte 180` (no fresh LEAP position, gate 2 fails outright), and `conviction-matrix` returns **COVERED_CALL** (call bid volume 97,752 > ask volume 61,276 — calls are being *sold*), an explicit hard-reject. Cum-flow is thin (30d +$12.1M, below the $50M floor). **~3-of-9.**
- **CCL** — 35-day unsaturated OI build and a real >180-DTE position (270617C00025000, +11,071 OI), but bid-dominant (34 ask vs 47 bid, not clean buying), 30d cum-flow flat (−$1.19M) and **90d −$22.6M — wrong direction**, tripping the hard cum-flow disqualifier. **~1-of-9.**
- **IREN** — 103-day unsaturated OI build, but `biggest-increases` shows the Mar-2027 $30P (+10,540) and $50C (+10,437) building in **near-identical size**, plus a matched 742-DTE straddle pair (+7,150 / +7,218). That is a **structural straddle build, not a directional thesis** — which is exactly why cum-flow nets to nothing on enormous notional (30d $902.0M bearish vs $892.7M bullish). **~1-of-9.**
- **VFC** — the >180-DTE build is a **put** (270319P00014000, +19,999 OI, bid-dominant ⇒ puts being sold). Wrong side of the book for a DIRECTIONAL_LONG lane.
- **GRAB / CHGG** — fail the C12 price floor ($3.43 / $0.86). **HL** — deep-OTM put. **BTG** — ask/bid balanced on a $5.60 stock. **ONDS** — calls being sold (ask 11 vs bid 418).

Market-wide `share_leaps` fell 4.1% → 3.1% across the week and the 10Y rose 14bp — an empty LEAP book is the expected output here, not a miss.

---

## 5. Volatility Surface — WoW Term Structure & Skew Evolution

**⚠ NEW SUBSTRATE DEFECT FOUND THIS RUN — reported, not papered over.** `uw options-structure iv-term-structure --date <historical>` loads the **correct** dated parquet (its `source` field confirms `bot-eod-report-2026-08-31.parquet`), **but every row's `dte_approx` is computed against the real system date rather than the requested `--date`.** Proof: on the 08-31 snapshot the 08-31 expiry itself — 0DTE that day — printed `dte_approx: -5`. The error equals (today − requested date), and it silently shifts near/far tenor selection, corrupting `front_end_ratio` and `kink_dte` on any historical snapshot. Both the 08-31 and 09-04 hygiene runs reported `kink_dte: 6 → 2026-09-11` for SPY/IWM — that identical answer is an **artifact of the shared anchor date**, not evidence the kink held. **Mitigation applied:** the WoW diff below compares `avg_iv` **by absolute expiry date**, which is immune to the bug; `front_end_ratio` and `kink_dte` are quoted only for the current snapshot.

**Term-structure WoW (hygiene-corrected `base_shape`, expiry-anchored).** All classification runs through `scripts/term_structure_hygiene.py`; raw labels are never used.

| Ticker | base_shape 08-31 | base_shape 09-04 | Flip? |
|---|---|---|---|
| SPY | CONTANGO | CONTANGO | no (kinked both days) |
| **QQQ** | BACKWARDATION (kinked, prominence 21.1%) | **CONTANGO** | **YES — kink dissipated** |
| IWM | CONTANGO | CONTANGO | no (kinked both days) |
| AFRM / KTOS | FLAT | CONTANGO | thin-tenor noise |
| U | FLAT | **BACKWARDATION** | name-specific, watch |
| RKLB | CONTANGO | CONTANGO | no |
| ARWR | CONTANGO | FLAT | contract count fell to 2–3 — unmeasurable, not calm |

**The expiry-anchored comparison is the real signal.** For **SPY**, the CPI-dated (09-11) leg held flat at 12.79% while every other tenor compressed (09-08 10.9% → 8.0%; 09-18 OPEX 14.6% → 13.75%; 10-16 15.7% → 15.0%) — so the CPI kink got **more** pronounced, prominence **11.0% → 16.6%**. For **IWM** the same pattern, harder: prominence **8.2% → 16.4%, more than doubled**. **QQQ is the outlier** — its CPI leg fell hardest of all its tenors (20.4% → 15.4%, −24.7% relative), so its event premium genuinely deflated.

**Front-end panic: absent everywhere.** `front-end-iv-ratio` at `--near-dte 7`, called 4× per name and fully deterministic this session (all four reads identical — the known non-determinism did **not** reproduce): SPY 0.949, QQQ 0.830, IWM 0.896, AFRM 0.966, RKLB 0.890, U 1.024, KTOS 0.928, ARWR 0.990 (snapped to `near_dte_actual` 13 on a thin tenor). **Population firing rate: 0 of 8 above the 1.05 panic threshold.** Grading by population rather than per-name is the point — this surface is cheap and lumpy, not panicked.

**Skew.** SPY `TAIL_HEDGING` both days, ratio 1.504 → 1.512 — put skew is **not** at a low despite IV at the floor. QQQ 1.335 → 1.326, IWM 1.378 → 1.368, both steady TAIL_HEDGING. Every single name screened (AFRM/RKLB/U/KTOS/ARWR) is `COMPLACENT` at 0.96–1.02 — zero standalone tail demand. **Cheap outright vol sitting under a persistent index tail bid is a genuine divergence.**

**`iv-percentile-zscore` — PROVISIONAL, all names.** `dates_used: 102` on every call, below the 120-day first-class floor (the documented silent short-delivery). SPY percentile 0 / z −1.18; QQQ 1.96 / −1.86; IWM 1.96 / −1.34; AFRM 0 / −2.38; RKLB 1.96 / −2.35; U 0 / −2.14; KTOS 0 / **−2.63**; ARWR 8.82 / −1.57. Percentiles floored near zero may be a censoring artifact of the short window, but the z-scores are independently and deeply negative, so the LOW_IV classification is sound even though the magnitudes are provisional.

**Expiry concentration** (market-wide, aggregate premium): 09-04 (expired) $5.69B > **09-18 OPEX $3.78B** > 12-18 $2.77B > **09-11 CPI $2.76B** > 11-20 $2.16B > 10-16 $2.14B. The two dominant near-term clusters are exactly the two kink dates — structural corroboration, not new signal.

**`iv-outliers` unusable this week** — every cached row carries `expiry: 2026-09-04`, i.e. same-day wing decay (DNN, SVIX, SOXL, SNDK, F, PATH, BE, ACHR, TSLL at 9–400% IV). Noise, not signal.

**Macro-beta confound.** All three indices kink at **2026-09-11**. Per the standing rule, any single name kinking at that date is shared macro beta, not name-specific edge — and with CPI on 09-11 and OPEX on 09-18 this confound is close to unavoidable this cycle. No single name in the screened universe kinked at a date that does not trace to a macro event.

**Calendar-spread candidates:** none cleared the contract-count floor. **U** flipped FLAT → BACKWARDATION with `front-end-iv-ratio` 1.024 (not panicking), but on 9 kept / 6 dropped tenors — too thin to size. QQQ's opportunity resolved before Friday.

### Vol lane routing

**BUY VOL / `vol_long` — the actionable side, hunted hard this week per the standing instruction:**
- **SPY** — CONTANGO base, CPI kink *intensifying* (11.0% → 16.6%), TAIL_HEDGING skew steady at 1.51, IV at the 1-year floor (percentile ~0, z −1.18, provisional), no front-end panic (0.949), into CPI + FOMC + OPEX. **raw_score +1 ⇒ DROP.** Invalidation: the kink dissipates the way QQQ's did, or `front-end-iv-ratio` pushes above 1.05 (at which point the thesis becomes "fade the spike", not "own cheap vol").
- **IWM** — the same setup with a sharper relative move (kink prominence more than doubled), z −1.34, ratio 0.896. **raw_score +1 ⇒ DROP.**

**SELL VOL / `vol_short` — generated, then routed `watch_only`, never sized.** No name in the screened universe actually supports a SELL VOL thesis on the surface evidence: 0/8 above panic, broadly CONTANGO (no rich front premium to sell), and index skew is TAIL_HEDGING rather than COMPLACENT — selling a front leg against a persistent tail bid is poor risk/reward independent of any routing rule. For completeness, the closest candidate is **QQQ's post-kink CONTANGO with a 0.830 front ratio** (event premium already extracted) — an iron-condor/short-strangle shape into 09-18. It routes **`watch_only` — never sized**, mechanically, because it is a net-short-vega structure.

### This week is an unusually clean out-of-sample test of the short-vol routing rule

The 2026-08-30 P0 routed all `vol_short` to `watch_only` on the finding that the lane is **adversely selected** — a *sign error*, not a dead lane: the scouts identify genuine vol-**expansion** candidates and then sell vol into the expansion. This week's realised moves, measured from each call's own envelope date to Friday:

| Lane | n | Mean \|move\| | ≥0.5×ATR | Largest moves |
|---|---|---|---|---|
| **`vol_short`** | 11 | **8.60%** | 9/11 (82%) | MDB **−18.7% (3.86×ATR)**, LULU **−16.3% (4.35×ATR)**, PATH **−16.3% (3.49×ATR)**, ORCL +12.4% (2.93×ATR), CPB −10.1% (3.98×ATR) |
| `vol_long` | 18 | 6.81% | 15/18 (83%) | IREN +21.3%, SNDK +13.2%, CLS +12.4%, CIEN −10.9%, ORCL +8.9% |

**The names the fleet wanted to sell vol on realised *larger* moves than the names it wanted to buy vol on** — 8.60% versus 6.81% mean absolute move. Three separate short-vol candidates moved more than 3.4× ATR. Had these been sized as short-vega structures, the week would have been severely damaging; because the routing rule held, the cost was zero. This is a single-week observation on small n and it measures **selection, not P&L** (these rows resolve on a realised-move proxy, not IV-vs-RV), so it is corroboration of the documented mechanism, not new evidence — but it points the same way, and it is the sort of week that would have generated the loss the rule was written to prevent.

---

## 6. Earnings — Recap & 2-Week Lookahead

> **Process note:** the `earnings-scout` and `multileg-strategist` agents were spawned twice and failed to return within the run window (the session's subagent scheduler was throttled to roughly a minute of active agent time across a very long wall-clock wait, while the `uw` CLI itself measured 0.034s per call). Both lanes were therefore executed directly in the orchestrator. Coverage is complete for the multileg repeat count and the earnings lookahead; the per-name `earnings-play` narrative recap is thinner than a full agent pass would produce, and is flagged as such.

### (a) Recap — this week's prints

| Ticker | Move (week) | Pre-event call | Grade |
|---|---|---|---|
| **LULU** | **−16.7% on 09-04** | `vol_short` (08-31, 09-01) — routed `watch_only` | **DISCONFIRMING** — a short-vol structure would have been run over; routing prevented it |
| **MDB** | −17.4% cumulative | `vol_short` (08-31, 09-01) — `watch_only` | **DISCONFIRMING** for the SELL VOL thesis |
| **PATH** | −16.3% on 09-04 | `vol_short` (09-01) — `watch_only` | **DISCONFIRMING** |
| **AMBA** | −11.0% | `vol_short` (09-01) — `watch_only` | **DISCONFIRMING** |
| **CPB** | −8.6% | `vol_short` (09-02) — `watch_only` | **DISCONFIRMING** |
| ZS | −7.8% | `vol_short` (09-01) — `watch_only` | DISCONFIRMING |
| **SNDK** | **+17.2% on 09-04** (top S&P mover) | `vol_long` (09-01) | **CONFIRMING** |
| CIEN | −15.2% | `vol_long` (09-01) | **CONFIRMING** (magnitude, not direction) |
| DOCU | +6.9% | `vol_long` (09-01) | CONFIRMING |
| ORCL | +5.3% (with a −6.3% mid-week dip) | `vol_short` 09-01, `vol_long` 09-02 | The `vol_long` re-read was correct |
| NTAP | −0.8% (flat) | `vol_long` (09-02) | DISCONFIRMING — IV crush, no move |

The vol lane called direction-agnostic expansion well and the *sign* of the trade badly — precisely the §5 mechanism.

### (b) Lookahead — next 14 days

Applying the **full C12 floor** (price ≥ $5 **and** 20-day dollar-ADV ≥ $50M) to the 41 cached rows drops sub-$5 microcaps (MoneyHero $0.86, Yiren $1.02) and thin names (SSL, AVO, UNFI, JMKE, ODD, CGNT, PPIH, LMNR, SHOE, ZUMZ, KEN, FIZZ).

**The population must be split by measurability.** `--near-dte 7` snaps to the nearest listed tenor, so for any name reporting more than ~4 days out the front tenor **expires before the report**:

| Ticker | d2e | Front-end | base_shape | FER | Event tenor | **True implied move** | Cached `implied_move_perc` | Understated by |
|---|---|---|---|---|---|---|---|---|
| CASY | 4 | measurable | BACKWARDATION | 1.409 | 09-18 (13d) | 11.18%* | 7.61% | 1.5× |
| BRZE | 4 | measurable | BACKWARDATION | 1.399 | 09-18 (13d) | 20.75%* | 14.36% | 1.4× |
| TTAN | 4 | measurable | BACKWARDATION | 1.265 | 09-18 (13d) | 16.01%* | 11.40% | 1.4× |
| **ADBE** | 6 | **UNMEASURABLE** | BACKWARDATION | 1.407 | 09-11 (6d) | **9.59%** | **0.39%** | **24.4×** |
| CHWY | 5 | UNMEASURABLE | BACKWARDATION | 1.553 | 09-11 (6d) | 12.66% | 1.25% | 10.1× |
| ASO | 5 | UNMEASURABLE | BACKWARDATION | 1.544 | 09-11 (6d) | 10.54% | 0.57% | 18.6× |
| AEO | 5 | UNMEASURABLE | BACKWARDATION | **1.685** | 09-11 (6d) | 17.06% | 1.58% | 10.8× |

\* For the ≤4-day names the nearest surviving tenor (09-18) overshoots the print by nine days, so those implied moves are **upper bounds**, not clean event moves.

Two distinct defects are visible here and neither fixes the other. The **`--near-dte` snap** makes the front end unmeasurable for the >4-day names; separately, the cached **`implied_move_perc` is computed off a `dte=1` tenor** that for ADBE expired on 09-05, six days before its print — hence the **24.4× understatement**. Quoting that field for a >4-day name would have understated ADBE's event risk by more than an order of magnitude.

All seven names print BACKWARDATION, which in a *pre-selected earnings population* is expected rather than informative — the discriminating quantity is the FER magnitude (AEO 1.685 > CHWY 1.553 > ASO 1.544 > CASY 1.409 > ADBE 1.407 > BRZE 1.399 > TTAN 1.265).

**Macro confound — decisive for the largest name.** ADBE reports on **2026-09-11**, which is CPI day and the exact dte at which SPY kinks. Its front-end premium cannot be separated from the index's CPI premium; per the standing rule it is shared macro beta, not name-specific edge, and is discounted accordingly. The same applies to CHWY, ASO and AEO.

**⚠ `uw insights analyst-vs-flow` has no analyst leg.** Verified this session on a fresh six-name sample (ADBE, CASY, BRZE, TTAN, CHWY, ASO): **0 of 6** returned any rating, target or recommendation field — every response contained only an `options_flow` block. **No analyst-disagreement score is possible**, and the rubric's highest-EV earnings setup is therefore unavailable, not merely absent.

**Net:** no earnings name reaches the trade book. Each is a single-lane flag and fails the ≥2-agent confluence gate; every one sits inside the CPI/FOMC/OPEX stack.

---

## 7. Risk & Correlation (week-candidate universe)

**`portfolio-correlation` health check — verified CLEAN this session.** The intermittent failure mode (0.97–0.996 on *every* pair, collapsing the board into one cluster) did **not** reproduce: a control pull returned differentiated values (0.597 / 0.569 / 0.540). The tool is trustworthy for this run. The known cosmetic defect persists: `sector_breakdown` returns `{"Unknown": 10}` with a spurious "100% concentration" warning, which is disregarded.

**Correlation clusters across the candidate universe (30d):**

| Pair | Correlation | Severity |
|---|---|---|
| **MU / SNDK** | **0.910** | **HIGH** |
| IWM / SPY | 0.834 | HIGH |
| MSFT / SPY | 0.609 | MODERATE |
| AVGO / SPY | 0.571 | MODERATE |
| MU / IWM | 0.540 | MODERATE |
| MU / AVGO | 0.501 | MODERATE |

**MU/SNDK at 0.91 is the single most important risk fact of the week.** The sector lane's headline finding was a Technology inflow led by MU and SNDK; the correlation says those are **one position**. Taken together with SMH's −$71.6M outflow, the honest description is a single crowded memory/AI-hardware trade — not breadth, not rotation, and not diversification. Note also that the cluster gate remains **direction-blind**: it would charge a short for correlating with a long, which is an offset rather than a concentration.

**Macro & event risk.** Core PCE 3.34% with the 10Y at 4.77% and rising; CPI 09-11, FOMC + SEP 09-15/16, OPEX 09-18. Every candidate's 1–4 week horizon contains at least two Tier-1 events, so the event-risk gate fires on the entire book.

**Fundamentals verdicts (top 5 by raw_score):**

| Ticker | Verdict | Contradicting / confirming facts |
|---|---|---|
| **MSTR** | **VETO** | **Four consecutive EPS misses: −223%, −770%, −1,518%, +1.3%.** ROE −60.8%, operating margin −7,272%, net margin −6,103%, revenue growth just +7.79%. Beta 3.59, −60.9% below its 52-week high. A flow-driven long here is a leveraged crypto proxy, not an equity thesis — the textbook case the gate exists to catch. |
| **SNDK** | **CAUTION** | Operationally excellent — four straight beats (+11.7%, +57.9%, +76.3%, +27.8%), revenue +175%, ROE 93.1%, D/E 0.20. But **insider MSPR repeatedly −100 (persistent insider selling)**, beta **5.23**, and the stock is **+3,032% off its 52-week low**. The fundamentals confirm the business and contradict the entry. |
| **MU** | CONFIRM | Four straight beats, revenue +167% YoY, EPS +701%, ROE 70.6%, D/E 0.27, 80.6% institutional ownership. The fundamentals are not MU's problem — the flow is (see §3). |
| **MSFT** | CONFIRM | Consistent beats, ROE 33.2%, net margin 40.3%, beta 1.10, short float 0.94%. Clean. |
| **IWM** | NA | Index ETF — no company fundamentals. NA never penalises. |

**Debate-disconfirmation cuts: the bull/bear debate stage was NOT run this week, and that is a deliberate, disclosed choice.** The debate exists to cut size on top-conviction names; with every candidate already at DROP tier and `skip`/`watch_only`, there was no size for it to cut and no tier for it to move. Recording fabricated residuals would put unearned numbers into the calibration record. `debate_residuals` is therefore `null` on every call, and the debate gate is recorded as `not_run (empty book pre-debate)`.

**Breadth cross-check (advisory).** `fz`: 175 advancers / 327 decliners, **pct_green 34.79%**, average −0.43%, on a −0.39% SPY day. The two lineages agree that Friday was broadly negative; the divergence worth flagging is not `fz`-vs-`uw` but **index-vs-median-stock** (SPY +0.11% vs RSP −0.77% on the week).

**Concentration risk and hedge sleeve.** With zero sized positions there is no book to hedge and no sleeve is recommended. The standing risk is *not* portfolio risk this week — it is the temptation to express the Tech read at size, which the correlation table shows would be a single-name concentration wearing a sector label.

**Watchlist.** `uw watchlist scan` against `conviction_week_2026-W35` returned no adverse-flow exit candidates requiring action; the prior group's members (NOW, MSFT, MRVL and peers) were all `skip` and carry no live exposure.

---

## 8. High-Conviction Cross-Ref (HIGH and MEDIUM tier)

**EMPTY — no HIGH or MEDIUM tier names.** The highest raw_score in the book was **+2** (MSTR, SNDK) against a LOW floor of **3** and a MEDIUM floor of **7**. The Step 3a load-bearing-tool gate was never reached because nothing approached the ≥9 HIGH threshold.

**Expectancy lens (advisory, C31).** Not computable this cycle: there are no closed sized calls in the rolling `conviction_*` groups to compute per-tier expectancy or payoff ratio from — the daily book has been empty for **43 consecutive sessions** (last sized daily 2026-07-07) and the weekly book for **five** (last sized weekly W30, INTC starter). The absence of a denominator is itself the finding; the live sizer remains the Step 5 win-rate ladder regardless, and C3 Kelly stays advisory.

### Why the board is empty — the scoring, line by line

Every rubric line that could have fired, and why it did not:

- **+3 `oi-trend` BUILDING full week (`--days ≥ 5`)** — awarded to **nobody**. The **C47 saturation defect** is live and was reproduced directly this session: `--days 5` returns `consecutive_build_days = 5` on essentially every liquid name (5→5, 10→10, 30→30 — the value is censored by the flag), so the read is a floor, not a count, and the line is tautological as written. Independent proof from this run: `overall_trend: BUILDING` fired on **6 of 6** scorecard names — including IWM, whose `consecutive_build_days` is **0**. The line is awardable only on a same-session direction-verified call-vs-put read; for MU, the one candidate with a genuine unsaturated build (103 days), `oi smart-positioning` aggregated **47 bullish vs 53 bearish** across the week and so **failed** direction verification.
- **+3 accumulation conjunction** — halved to **+1** for MU under **C11**: the conjunction requires `cum_flow_30d` sign-aligned and ≥$50M, and MU's is **−$105.5M, sign-opposite** the long thesis. Not merely unconfirmed — contradicted. No other name was flagged by `accumulation-hunter` at all.
- **+1 `conviction-matrix` DIRECTIONAL_LONG** — conditional on `dominant_signal_class == leap_directional`; no candidate qualifies, so **0 everywhere**.
- **+2 `position-rolls` into longer-dated LEAP** — no qualifying roll; **0**.
- **+1 cum-flow accretion (intent-screened)** — awarded to MSTR, SNDK, MSFT, IWM, AVGO. **Denied to MU** because a C28 `distribution_flag` is present, which fails the intent screen outright regardless of sign.
- **+1 mechanized DEX flip / vanna squeeze** — awarded to **nobody**. `scripts/dex_flip.py` returned `qualifies: false` for **all 18** names screened; every apparent "flip" was a level, not a sign change. MRVL was the closest and **failed the magnitude floor by 6×** (flip_net_dex +15.0M against a 340.4M floor on a 1.36B trailing median) — exactly the whipsaw-around-zero the 2026-06-12 mechanization was built to kill. The vanna leg also fails book-wide: VIX ran 14.43 → 14.92 → 16.34 → 15.20 → 14.32 → 14.53, which is not a ≥3-session decline, so **no valid `vanna_squeeze` exists anywhere** — IWM and TSLA (the only put-heavy books) carry "vanna pressure", not a squeeze.
- **+1 sector leader (conditional)** — awarded to MSTR and SNDK only (Tech persistence 1.0, cum-flow aligned and ≥$50M). Denied to MU (cum-flow not aligned) and MSFT (not named a leader). ⚠ Note the **documented double-count**: conditions (b) and (c) test the identical field and threshold as the standalone cum-flow line, so these two lines are two rubric entries reading one bit.
- **+1 earnings BUY/SELL VOL** — no earnings name cleared the ≥2-agent confluence gate; **0**.
- **+2 multileg repeated on ≥2 days** — awarded to **nobody**. Only **three contracts** repeated across two or more sessions all week: VIX Sep-16 $22C ($2.8M), IWM Sep-11 $285P ($33.8M) and IWM Sep-11 $275P ($9.0M). The IWM pair is the *same* protective-put position that `oi decrease-with-volume` shows as the two **largest OI closures market-wide** on 09-04 (−128K and −127K contracts) — a build-then-**unwind**, not a directional structure, so awarding a directional +2 to it would be backwards. No single name clears the bar. PCG repeats on three days but the structure is OTM **call selling** (COVERED_CALL confirmed), i.e. net-short-vega yield overlay with capped upside. Friday's largest multileg premium is entirely SPXW **0DTE** ($52.5M / $40.7M / $40.0M at ml_ratio 0.33–0.47) — index churn, not structure.
- **+1 vol-surface KINKED/BACKWARDATION worsening** — awarded to **SPY** and **IWM** (kink prominence intensifying, z-score extreme, VRP-aligned for long vol).
- **−2 crowded long with rising P/C z** — **cannot fire this week.** The line is explicitly conditioned on **VRP positive**; VRP is −0.0011 / −0.0272. Stated for the record rather than silently omitted.
- **−3 / −1 flow_conflict** — `flow_conflict_lite` **−1** fired on MU and META (both `MIXED` labels). ⚠ **Scale-asymmetry defect flagged:** the award side carries two floors ($50M and 5%-of-gross) while the deduction side has none, so MU's −1 rests on a net that is just **−0.19% of 30-day gross** and META's on **+1.23%**. Per-call net-as-%-of-gross is reported in the envelope so the asymmetry stays auditable.

### Win-rate substrate

Run under the P0.3 clean-query protocol (`--top-n 200` pinned, truncated forward windows dropped — complete-window cutoff `signal_date ≤ 2026-08-28`), with a same-direction SPY benchmark over identical windows for the C2 market-excess gate:

| Class | Raw headline | Truncated | **Clean WR** | Clean n | SPY benchmark | **Market excess** |
|---|---|---|---|---|---|---|
| `bullish_flow` | 51.4% | 9 | **0.500** | 134 | 0.478 | **+0.022** |
| `bearish_flow` | 47.9% | 14 | **0.497** | 151 | 0.563 | **−0.066** |
| `high_iv_rank` | 79.3% | 17 | 0.786 | 173 | 0.202 | +0.584 → **quoted 0.600 (class ceiling)** |
| `volume_spike` | 39.8% | 19 | **0.404** | 156 | 0.205 | +0.199 |
| `dark_pool_accumulation` | — | — | **NA** | **0** | — | 0 rows market-wide (documented defect) |

The tool silently folds truncated windows into its headline — 9 to 19 per class here — so the raw figures are not usable as quoted. Note `bearish_flow` at **0.497 with −0.066 market excess**: below the 0.50 no-capital floor *and* losing to a simple SPY short over the same windows. `oi_build`, `multileg_directional`, `earnings_vol`, `leap_roll`, `vanna_squeeze` and `multi_day_sweep` are **not supported signal types at all**, so every name whose dominant class is one of those carries `win_rate: null, win_rate_source: "NA(substrate)"` and is capped at half by default — which, under the out-of-regime half-cap, is where the whole book already sits.

### Embedded rubric (for audit)

```
Weekly conviction score (rubric_version 2026-06-12, FROZEN) = Σ:
  # +3 swept on >=3 of 5 days REMOVED 2026-05-23 audit P0.3 (sweep-persistence -22pp two audits; multi_day_sweep realised 0.43 vs 0.70 claimed)
  +3  uw historical oi-trend BUILDING full week, --days >= 5   [C47 saturation: consecutive_build_days ceilings at --days; award only on direction-verified build]
  +3  3+ aligned accumulation signals + dark-pool block-stratified institutional tier — C11 CONJUNCTION:
      full +3 only if cum_flow_30d sign-aligned AND |cum_flow_30d| >= $50M; else halved to +1
  +1  conviction-matrix DIRECTIONAL_LONG conf > 70 — CONDITIONAL: only when dominant_signal_class == leap_directional; else 0
  +2  uw oi position-rolls: institutional roll forward into longer-dated LEAP
  +1  cum-premium-flow net directional accretion (sharp 30d or smooth 90d) — INTENT-SCREENED:
      0 if a C28 distribution_flag is present, or if ex-div deep-ITM sub-parity call arb
  +1  MECHANIZED DEX sign-flip or vanna squeeze in trade direction (scripts/dex_flip.py; sign change, not level;
      flip-day |net_dex| >= 0.25x trailing-10-session median; whipsaw_warning mandatory)
  +1  sector-rotation single-name leader — CONDITIONAL on all of: (a) persistence_score >= 0.6,
      (b) cum_flow_30d aligned with thesis, (c) |cum_flow_30d| >= $50M
  +1  earnings-scout BUY VOL or SELL VOL next 2 weeks, term-skew aligned
  +2  multileg directional structure repeated on >= 2 days, term-structure-anchored play type
  +1  vol-surface KINKED/BACKWARDATION worsening WoW + iv-percentile-zscore extreme + VRP-aligned
  +1  opex-pin-strategist top-5 (OPEX week only — NOT APPLICABLE, 09-18 is 14 days out)
  -2  contrarian crowded long with rising pc-ratio z-score trajectory (VRP POSITIVE only)
  -3  flow_conflict — cum_flow_30d clearly opposite dominant_signal_class   [mutually exclusive with lite]
  -1  flow_conflict_lite — 30d cum-flow read is MIXED                       [mutually exclusive with -3]
  # TIER GATES (applied by risk-monitor in 2d; contribute 0 to raw_score, never appear in score_components):
  -1 TIER  correlation cluster (pairwise corr >= 0.70)
  -1 TIER  WoW regime flip conflicting with trade direction

Tiers: >=9 HIGH (full) | 7-8 MEDIUM (half) | 3-6 LOW (starter/watch) | <=2 drop
Out-of-regime guard: ALL sizes capped at half (rubric fitted pre-2026-06-12 UPTREND; not revalidated)
```

---

## 9. Setups for Next Week

### Next-session GEX advisory — SPY / QQQ only (prose, 0 rubric points)

**Framed by its own track record first:** the Step 0 rolling backtest verdict is **`NO_GO_NO_EDGE`**. Pooled over n=118 sessions, the next close landed nearer the quoted EOD wall only **16.9% of the time** (p vs 50% = 1.0 — significantly the *wrong* way; walls behave as **anti-magnets**), containment within walls 59.3%, pin-direction accuracy 45.8% (worse than a coin flip). H1 also ran backwards pooled (long-gamma mean |return| 0.838 vs short-gamma 0.705; only QQQ matched theory). Everything below is dealer context, not a forecast.

**SPY** — spot 770.19. `total_gex` **−1,169,885,960 ⇒ short-gamma regime** (the live label agrees today, but the underlying 10-day series mislabels **6 of 10** rows, so today's agreement is coincidence). `zero_gamma_level` **null ⇒ `zgl_reliable = false`**. Call wall **780** (+$114.3M, +1.27% above spot); put wall **760** (−$185.9M, −1.32% below). The dominant mass sits essentially **at the money — 770 carries −$904M net GEX**, confirmed by `greek-screener` (gamma ≈1.45–1.54 at the 770 strike). Dealers are positioned to **amplify** moves off 770 rather than dampen them.

**QQQ** — spot 718.96. `total_gex` **−237,296,053 ⇒ short-gamma**, despite the tool's own label printing **POSITIVE** — a direct hit of the documented defect (the label is `sign(spot − ZGL)`, not the gamma sign); label and `total_gex` sign disagree on **5 of 10** rows. ZGL 243.37 against a 718.96 spot is **66% below** — extrapolation garbage, `zgl_reliable = false`. Call wall **720–725** (+$86.6M / +$84.9M, ~0.28% above spot); the dominant negative mass is **718 (−$242.1M), essentially at spot**, with the next real support at **700** (−$110.1M, −2.64%).

**Mandatory caveats:** this is the 09-04 EOD book and fresh 0DTE open interest will materially revise it in the first 30–60 minutes Monday; the CPI/FOMC/OPEX stack can gap spot straight through these levels before dealers re-hedge (which is part of why the wall hit-rate is so poor); these are **ETF** books, not the SPX/NDX index books institutions actually hedge; and the CLI cannot isolate the D+1 expiry, so this is a 0–45 DTE aggregate proxy.

### Next-session 0DTE premium-selling setup (advisory, 0 rubric points)

Rolling backtest verdict **`GO_PREMIUM_SELL_INTRADAY`**, `vol_state` **LOW**, VIX 14.53.

| Index | Sell premium | Implied move | Expected range | Size scalar | Structure | Gross PnL | **Net PnL** |
|---|---|---|---|---|---|---|---|
| SPY | true | 0.36% | 0.99% | 0.5 | Wider iron condor, wings ≈ ±0.99% | +0.262% | **+0.162%** |
| QQQ | true | 0.53% | 1.63% | 0.5 | Wider iron condor, wings ≈ ±1.63% | +0.399% | **+0.299%** |

**Quote the net, on its real basis.** `pnl_basis` is *percent of underlying spot notional, gross of costs* — not premium-collected and not margin-relative. Net of the assumed 0.1% round trip, SPY is **+0.162%** and QQQ **+0.299%** per day. In the **LOW VIX tercile specifically** (where we sit): SPY 0.218% gross → **0.118% net**, QQQ 0.353% → **0.253% net** — positive, but these are the thinnest terciles in the sample and prior work has found this lane net-negative-to-zero at low VIX, so treat the edge as marginal rather than established. Rules: enter at the open once the overnight gap resolves, stand aside if it gaps beyond the wings, **never carry overnight**, stand aside on a VIX spike or front-end backwardation. SPY ≈ SPX (trade either); QQQ is the weaker of the two.

**Promotion bar, restated:** this lane stays advisory and 0-point **permanently** until a vol-shock day enters the sample *and* net expectancy clears a tail-aware bar. Win-rate is explicitly **not** the promotion metric for a negatively-skewed short-vol strategy. **The validation sample contains no vol shock — the left tail is UNSAMPLED.** With CPI, FOMC and OPEX all landing inside the next ten sessions, that unsampled tail is exactly the risk in front of us.

### Swing setups from dealer positioning

**None qualify.** Zero of 18 names produced a mechanized DEX flip and no valid vanna squeeze exists book-wide. Trend context only, explicitly not eligible for the scored line: **MU** (DEX +23.0B Friday, accelerating, zero sign changes — a trend, not a flip), **META** (crossed positive four sessions before the anchor — a level shift; the mechanization exists precisely so this is not miscalled a flip), **IWM** (short but decaying, −16.8B → −8.6B → −5.7B → −2.6B). **MRVL** and **SNDK** are unconfirmed single-session inflections — do not size off either. **SPY, QQQ and TSLA carry no clean dealer thesis** (6, 4 and 11 sign changes respectively — whipsaw flagged).

### Pin vs trend regime call

**Neither, and the walls are not usable as a pin map.** Both indices are in short-gamma books with their largest hedging mass sitting at the money, which is trend-supportive mechanically — but the backtest says these wall levels do not contain price. 09-18 is monthly OPEX with $3.78B of premium concentrated there, so pin mechanics become relevant *next* week, not this one.

### Highest-conviction actionable setups for the coming week

**There are none, and that is the recommendation.** No HIGH-tier names exist. The two ideas with any evidentiary support are **long vol on SPY and IWM** — CPI-dated kinks intensifying (prominence 16.6% and 16.4%), IV at the one-year floor, no front-end panic, a persistent index tail bid, into a CPI + FOMC + OPEX fortnight — and both scored **+1, DROP**. They are the names to watch for a daily-confirmation entry, not to size now.

### LOW-tier names to track for daily-analysis confirmation

**None — the LOW tier is also empty.** The nearest misses, for journaling only: **MSTR (+2)** and **SNDK (+2)**, both one point short of LOW, and both carrying an adverse fundamentals verdict (VETO and CAUTION respectively).

### OPEX book

Not applicable — 2026-09-18 is 14 calendar days out, so `opex-pin-strategist` was correctly not spawned. It becomes conditional next week.

### Deep-dive hand-off

**Skipped — no-edge week.** No HIGH-tier, non-VETO name exists to hand off.

---

## 10. Watch-only — single signal, no confluence

Surfaced by exactly one Phase-1 lane; recorded for journaling, **not for entry**:

- **DELL** — sweep-persistent bearish 4 of 5 sessions ($1.26B premium, the cleanest non-index single-direction sweep read of the week). Sweep-tracker only. No corroborating lane, and the sweep line scores 0 points by construction.
- **EWZ** — the most persistent genuinely directional multileg structure in the book: Dec-2026 call spreads/ladders on three separate days ($35C/$38C/$46C/$47C/$49C/$50C/$51C, ml_ratio 0.97–1.00, spot $37.86). Parity-checked clean (Dec-26 $35C time value **+$1.295**, so a real option, not a financing leg). Multileg lane only; cum-flow +$12.0M/30d is far below the $50M floor.
- **VFC** — Sep-18 $15P and Mar-2027 $14P printed the same day at near-1:1 volume (90,822 / 92,804; ml_ratio 1.000 / 0.978): a put roll out-and-down on a $13.45 stock, with the long-dated leg bid-dominant (puts being *sold*). Parity clean (+$0.238 / +$1.44 time value). **Single day ⇒ no +2.**
- **TEAM, SLV** — the only names with *rising* P/C crowding (z 2.722 → 2.875 and 3.777 → 4.065). Under the informed-flow **continuation** reading these are cautions against a long, not fade entries; and the −2 line cannot fire in non-positive VRP.
- **Tier-1 opening-PUT persistence** (advisory, permanently 0 points — C19 closed as refuted): **META 3 of 5 sessions**, then MCD, AVGO, ISRG and COHR at 2 of 5. A uniformly put-side whale tape. Descriptive colour only; there is no promotion path under that wording.
- **Earnings singles** — CASY, BRZE, TTAN (front-measurable), ADBE, CHWY, ASO, AEO, CNM, SAIL, SIG, SUNB, CPRT (front unmeasurable). All single-lane.
- **KTOS, RKLB, U, AFRM** — deepest single-name IV-percentile compression (z −2.63 to −2.14), all LOW_IV, but all `COMPLACENT` skew with no catalyst-aligned kink. Vol-surface lane only.

---

## Appendix — run integrity

- **Coverage:** full 5-day week; `covered_dates` = 2026-08-31, 09-01, 09-02, 09-03, 09-04. No gaps.
- **Fleet:** 10 Phase-1 agents spawned (the full non-conditional roster; `opex-pin-strategist` correctly omitted — 09-18 is 14 days out). *Note: the command header says "11 agents (12 in OPEX week)" while its own enumerated non-conditional list contains 10 — a documentation inconsistency in `weekly-analysis.md`, not a missing agent.*
- **Agent failures and recovery:** `earnings-scout` and `multileg-strategist` each failed to return across two spawn attempts; the session's subagent scheduler advanced roughly one minute of agent-active time across a very long wall-clock wait, while the `uw` CLI itself benchmarked at **0.034s per call** — so the bottleneck was scheduling, not data. Both lanes were executed directly in the orchestrator (§5, §6 process note). `signal-confluence-quant` hit the same throttle and **Phase 2a–2d were likewise completed in the main loop**, which runs on Opus, the required minimum for this command. This is disclosed rather than silently absorbed: the scoring below is orchestrator-executed, not agent-executed.
- **Phase 2c (bull/bear debate) was not run** — deliberately, because the board was empty before the debate stage and the debate can only cut size. `debate_residuals` is `null` throughout rather than fabricated.
- **Watchlist write-back: NOTHING WRITTEN — correct per the write-back rule** (write only LOW-tier-and-above names, never the raw top-5). There are zero LOW+ names, so `conviction_week_2026-W36` is intentionally not created.
- **Liquidity floor (C12):** applied to a 194-name funnel; **106 passed, 88 dropped (45%)**, including the entire micro-ETF volume-spike cohort (DFAX with 35 contracts of total volume, DESK with 12, RPAR, QABA) and most of the confluence-bullish top rows (SHOO, TLYS, ZURA).
- **Empty-book streak:** this is the **6th consecutive empty weekly book** (last sized weekly: W30, INTC starter). The daily book has now gone **43 consecutive sessions** without a sized call (last sized daily: 2026-07-07). Re-derived by globbing `analyses/{weekly,daily}/*/decision.json` and treating `skip`/`watch_only`/`veto` as unsized.
- **Substrate defects encountered this run:** the new `iv-term-structure --date` / `dte_approx` anchoring bug (§5); `market-regime`'s undated `spy` price leg (§1); `share_0dte` = 0 on all five days (§1); `sector-flow-persistence` INFLOW/1.0 on 7 of 11 sectors (§2); `oi-trend` `consecutive_build_days` censored by `--days`, with `BUILDING` firing 6-of-6 including a name with a 0-day build (§8); the GEX `regime` label contradicting its own `total_gex` sign on ~55% of rows (§9); `dark_pool_accumulation` returning 0 rows market-wide (§8); `iv-percentile-zscore` short-delivering its lookback at 102 of 252 days (§5); `analyst-vs-flow` carrying no analyst leg on 0-of-6 names (§6); `pc-ratio-zscore` having no `--date` flag (§10); the `fz` doubled-first-letter ticker bug on bulk screens (AABEO, AABR, AACHC — per-ticker `fz_enrich` is healthy); and, confirmed live, a **~$1.315B identical-notional basket clip hitting SPY and IVV 14 seconds apart** at the 09-04 close (§3), plus closing-cross contamination running **14.9%–65.5%** of daily top-tier dark-pool premium.
