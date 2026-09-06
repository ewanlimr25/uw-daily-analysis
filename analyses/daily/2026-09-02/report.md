# Daily Market Analysis — 2026-09-02

## Executive Summary

- **Regime + GEX state:** `TRANSITIONAL — Mixed signals, reduce position size, wait for clarity` / trend `PULLBACK_IN_UPTREND`. SPY 765.16 (+0.44%) below its 20dma 768.98, above its 50dma 755.34. VIX 15.20 (−6.98%). **Both indices short-gamma by `total_gex` sign** (SPY −233.7M, QQQ −304.9M). Netted sector lean IN: Comm Svcs / Healthcare / Technology; OUT: Industrials / Cons Cyclical / Cons Defensive.
- **Rubric regime status:** `OUT-OF-REGIME (fitted UPTREND; current TRANSITIONAL) — sizing capped at half`
- **Next-session GEX (SPY/QQQ):** SPY short-gamma, ZGL `null` (unreliable), call wall 780 (+1.92%) / **put wall 760 (−$210.7M, the largest-magnitude strike on the grid) just 0.69% below spot** — favour defined-risk directional over premium-selling. QQQ short-gamma **by sign** (its `regime` label prints POSITIVE and contradicts itself), ZGL 256.43 unusable, call wall 730 (+2.97%) / put wall 700 (−1.26%) — wider walls, choppier book, lower conviction. Advisory, §2.
- **Top swing build:** **None sized.** Highest-scored name is **IWM (raw 4, LOW, SHORT)** — a verified multi-session institutional put-spread campaign into the CPI expiry — routed `watch_only` under the short-direction rule. `win_rate NA(substrate)`.
- **Top LEAP candidate:** **None.** Every DTE>180 candidate failed the required 90d accretion gate or was a hedge rather than a directional build. LEAP share of tape 3.8%.
- **Biggest risk:** **`macro_beta_cluster`** — IWM, SPY, QQQ, INTC, MU, MRVL, ORCL, QBTS are **one connected position**, bridged by QQQ/INTC 0.875 and QQQ/MU 0.754. The index-short book and the semis book are not two positions. **No hedge sleeve: the sized book is empty, so net delta is zero and there is nothing to hedge.**

**Board: empty. 41st consecutive empty daily board** (re-derived by globbing `analyses/daily/*/decision.json` only; last sized daily 2026-07-07).

---

## 1. Regime & Gamma State

`uw risk market-regime`: **TRANSITIONAL**, trend `PULLBACK_IN_UPTREND`, guidance *"Half position sizes. Favor defined-risk strategies. Iron condors in range."* Options-flow breadth is **34.9% bullish** (2,197 bullish vs 4,094 bearish of 6,291 optionable).

**Breadth divergence — new today.** `fz` price breadth reads 301 advancers / 201 decliners, **pct_green 59.84%**, while `uw` options-flow breadth reads 34.9% bullish. **Yesterday the two lineages agreed (31.4% / 31.1%); today they split.** Price up, positioning defensive. `divergence_flag` is FALSE by the formal rule (green tape *and* pct_green > 50), but the flow-vs-price split is the more informative reading and is surfaced in §6.

| Index | Spot | Zero-gamma | `total_gex` | Regime (by sign) | Call wall | Put wall |
|---|---|---|---|---|---|---|
| SPY | 765.27 | `null` (`zgl_reliable=false`) | **−233,735,588** | short-gamma (label FULLY_NEGATIVE — agrees) | 780 (+1.92%) | **760 (+0.69%)**, −$210.7M |
| QQQ | 708.96 | 256.43 → ~64% off spot, **unusable** | **−304,947,405** | short-gamma **by sign** — **label prints POSITIVE and contradicts itself** | 730 (+2.97%) | 700 (−1.26%) |
| IWM | 294.01 | — | negative 9 of last 10 sessions | short-gamma | — | — |

**Tape framing.** Today was a **broad** bounce, not a cap-weighted narrow one: RSP +0.46% ≈ SPY +0.44%, and IWM **led at +1.18%**. But it sits inside a losing week — 5-day: SPY −0.12%, QQQ −0.30%, IWM −1.74%, XLI **−4.19%**, XLY −2.62%. **XLE +4.28% is the only sector positive on the week.**

`uw options-flow dte-volume-share`: 0DTE 39.3% / weeklies 23.1% / monthlies 25.1% / LEAPs 3.8% → **BALANCED**. No uniform conviction adjustment applied.

`uw historical vrp`: **SPY +0.0046 FAIR** (iv30 12.44% vs rv30 11.98%); **QQQ −0.0264** (iv30 18.06% *below* rv30 20.70%). Neither a premium-selling nor a premium-buying tape at the index. Notably, **every single-name candidate examined today also carried negative VRP** — vol is broadly cheap versus realised, which forecloses premium-selling fades market-wide.

**Macro backdrop** (`scripts/fred_macro.py`): yield curve **normal +0.40** (10Y 4.79 flat 30d, 2Y 4.39); core CPI **2.79%** YoY; **core PCE 3.34%** YoY (sticky, above target); unemployment 4.1%; **payrolls −23k MoM (negative)**; fed funds 3.63%; **USD weakening −2.04 over 30d**. A stagflationary tilt: sticky core inflation against contracting payrolls. Weak USD supports commodities/energy/gold.

**Forward event risk — trading-day counts, corrected for the Labor Day holiday.** `2026-09-07` is Labor Day (NYSE closed); the Step 0 calendar initially counted it as a session.

| Event | Date | Trading-day count |
|---|---|---|
| Employment Situation / NFP | 2026-09-04 | **T+2** |
| PPI | 2026-09-10 | **T+5** (Step 0 said T+6) |
| CPI (August) | 2026-09-11 | **T+6** (Step 0 said T+7) |
| FOMC + SEP | 2026-09-16 | **T+9** |

No verdict changed on the correction, but the structures below carry a **three-day holiday weekend** of gap risk into NFP.

---

## 2. Next-Session GEX Map — SPY & QQQ (advisory)

> **Advisory, not a scored signal.** EOD dealer-gamma book read forward as the prior for the next open. **Prose-only, 0 rubric points, no backtested predictive claim.** Scope is SPY and QQQ only.

**SPY** — spot 765.27, `total_gex` **−233,735,588**, label FULLY_NEGATIVE (label and sign **agree** today). ZGL `null` → `zgl_reliable=false`; fall back to the sign plus spot-vs-wall. Call wall **780** (+1.92%), put wall **760** (−$210.73M, **the single largest-magnitude strike on the entire grid**), with spot only **+0.69%** above it. Short-gamma has held **7 of the last 8 sessions** — this is a persistent regime, not a fresh flip. *Structure bias:* dealers amplify rather than dampen; a break of 760 is mechanically accelerated. Favour defined-risk directional over a tight iron fly.

**QQQ** — spot 708.96, `total_gex` **−304,947,405** while the tool's own `regime` field prints **POSITIVE**. **The sign is authoritative; the label contradicted itself on both 09-01 and 09-02.** ZGL 256.43 against a 708.96 spot is a ~64% deviation — garbage extrapolation, `zgl_reliable=false`. Call wall 730 (+2.97%), put wall 700 (−1.26%). The regime has been **flip-flopping every 1–2 sessions** (sign sequence over 8 sessions: −,+,+,+,−,+,−,−). *Structure bias:* short-gamma tilt argues against premium-selling, but the instability argues against high-conviction direction either. Lower conviction than SPY.

**Mandatory caveats.** EOD is a **prior, not a target** — fresh 0DTE OI re-computes both books in the first 30–60 minutes. **Gap risk voids the prior**, and a three-day weekend plus NFP at T+2 is exactly that risk. `uw` **cannot isolate the D+1 expiry** (`gex --dte-max 1` errors), so this is the standing 0–45 DTE proxy book. This is the **SPY/QQQ ETF book**, not the cleaner SPX/NDX index book.

### 2a. Next-session 0DTE premium-selling setup (`scripts/zerodte_setup.py`)

The GEX walls above are a **map, not a pin** — wall-as-magnet backtested NO_GO. What validated is a **delta-neutral premium-selling** edge. Advisory, **0 rubric points**, not a guaranteed edge.

| | SPY | QQQ |
|---|---|---|
| `sell_premium` | true | true |
| `vol_state` / VIX | LOW / 15.20 | LOW / 15.20 |
| implied move | 0.77% | 1.11% |
| `expected_range_pct` | 1.07% | 1.79% |
| `size_scalar` | 0.5 | 0.5 |
| structure | wider iron condor, wings ≈ ±1.07% | wider iron condor, wings ≈ ±1.79% |
| **LOW-VIX tercile, NET of the 0.10% round trip** | **+0.139%/day** | **+0.268%/day** |

`backtest.verdict` = `GO_PREMIUM_SELL_INTRADAY` both. **PnL basis: percent-of-underlying-spot notional, GROSS** — the net figures above are the ones that matter. `entry_rule`: enter at/after the open once the gap resolves; hold to the close; **never carry overnight**. No `stand_aside_reason` set.

**State the tension plainly:** the systematic lane says sell premium while **SPY sits 0.69% above the largest put wall on its grid in a book short-gamma 7 of 8 sessions** — not the setup premium-selling wants. Reconcile at the desk, not mechanically. **Tail caveat: the 60-day validation sample contains no vol shock, so the short-vol left tail is UNSAMPLED.** Promotion bar remains permanent-advisory until a vol-shock day enters the sample and net expectancy clears a tail-aware test.

---

## 2b. Swing Dealer Positioning (1–4 weeks)

**QQQ is the only qualifying mechanized DEX flip in a 10-name sweep.** `scripts/dex_flip.py`: `qualifies=TRUE`, net_dex **08-31 +16,634,321,146 → 09-02 −5,434,177,585**, prior 5 sessions all positive, |flip| 5.43B against a floor of 3.13B (0.25× the trailing-10 median 12.54B), **magnitude_ratio 1.73×**, `whipsaw_warning FALSE`. Swing bias SHORT, MEDIUM conviction.

**Explicit no-flip roster — negative results matter here.** SPY (`qualifies=FALSE`, **whipsaw_warning TRUE**, 4 sign changes, net_dex still +8.67B but deteriorating from +32.16B), IWM (persistent negative *level*, not a flip), **MU (net_dex +8.90B rising — a bullish LEVEL with `sign_changes_in_window: 0`; this is precisely the pattern that mis-scored MU on 2026-06-11 and the mechanization exists to catch)**, NVDA, META (whipsaw, 6 sign changes), PANW (net_dex +$0.01B, economically meaningless), AMD, AVGO, MRVL.

**MRVL is a genuine near-miss worth recording:** its DEX flip is dated **2026-08-28** — three sessions stale, so the rule (which fires only on the latest session) returns FALSE — but `uw historical gex-time-series` shows **`regime_flip_detected TRUE` on the same date**, POSITIVE→NEGATIVE after a 19-session positive run, sustained four sessions. DEX and GEX flipped together. Real confluence, just outside the mechanized window; scored 0, reported here.

**Vanna squeeze fired ZERO times across all 10 names.** The gate requires a falling-VIX leg, and the dated ^VIX series reads **08-27 14.51 → 08-31 14.92 → 09-01 16.34 → 09-02 15.20**: VIX *rose* two sessions before today's −6.98%. Today's drop is the setup, not a confirmed squeeze. IWM carries the largest dormant put-heavy book (net_vanna +125,249) — one more down day arms it, which is a live risk *against* the IWM short.

---

## 2c. Sector Rotation

**Rotation regime call: `no_change`, confidence LOW.**

Direction reads off the **netted** `uw risk market-regime.sector_rotation` only — the sole directional source, and a **top-3/bottom-3 truncation** (the other five sectors are *unknown*, not zero):

- **IN:** Comm Svcs +$60.4M · Healthcare +$12.5M · Technology +$8.2M
- **OUT:** Industrials −$27.6M · Consumer Cyclical −$20.6M · Consumer Defensive −$9.2M

`sector-flow` and `sector-flow-persistence` are **one gross-turnover source, sign-agnostic**, and today fired **INFLOW on 9 of 11 sectors** (five tied at persistence 1.0) — **near-zero discrimination**. Used as a durability filter only.

**Only Technology clears the standout bar** (top-third persistence ∩ above-median gross), and its netted magnitude **+$8.2M is the weakest of the three inflow sectors** — that tension is flagged, not hidden. Comm Svcs (largest netted number) and Healthcare fail the persistence/magnitude bar.

**All three netted-OUT sectors are gross-disagree → `watch_only`:** Industrials (netted −$27.6M vs gross +$134.9M), Consumer Cyclical (−$20.6M vs +$443.1M), Consumer Defensive (−$9.2M vs +$38.9M). No sized de-risking call anywhere.

**Energy reconciliation, stated honestly.** XLE is the only sector positive on the week (+4.28%) and dominates the `fz` new-high lane (HP, UGP, DINO, TDW, PSX, HOS), **yet Energy sits outside the netted top-3 entirely and its options flow is unimpressive** — XOP outright bearish (−$2.36M), XLE `trend_direction` MIXED. This is **price momentum not yet confirmed by options positioning**. Appendix only, not a rotation call.

**ETF flow tape (advisory, 0 rubric points; magnitudes are 2–3 orders below the GICS aggregates — colour only):**

| ETF | Net premium (5d) | Persistence | GICS agreement | DP positioning | Options urgency |
|---|---|---|---|---|---|
| IGV | +$7.68M | BULLISH | agree (Tech) | below-mid heavy, mild sell-tilt | bearish-leaning |
| XLK | +$5.65M | BULLISH | agree (Tech) | strong buy-tilt ($97.4M vs $23.9M) | balanced |
| XLV | +$2.20M | BULLISH | agree (Healthcare) | sell-tilt | thin sample (n=7) |
| EWY | −$18.59M | BEARISH | n/a (no GICS) | balanced | contradicts 5d label |
| GDX | −$12.66M | BEARISH | **disagree** | strong buy-tilt | contradicts 5d label |
| KRE | −$4.23M | BEARISH | **disagree** | buy-tilt | contradicts 5d label |

Single-name Technology leaders named: MU, NVDA, TSM, DELL, CRM. **Note that MU and TSM both fail the sector-leader +1 condition on cum-flow direction** (MU −$303.4M, TSM −$105.2M — both opposite a long thesis) and DELL fails the $50M magnitude floor.

---

## 3. Swing Setups (1–6 weeks)

**Nothing is sized.** Every row below is `watch_only` or `skip`. Theses, structures and invalidations are stated in full because the routing is **terminal sizing, not screening** — these serialize into `decision.json` so the counterfactual keeps resolving.

### 3a. Long swings (regime-aligned)

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **NBIS** | 3 (LOW) | Genuine *intraday* institutional DP blocks at a defended shelf while price fell −7.64%; C11 conjunction satisfied on sign + $50M | none proposed | **Loses the $200–201 DP shelf** (C34-valid, second-tier: $200.05 $70.9M/5 trades + $201.00 $40.7M/6 trades ≈ $111.6M) | **watch_only** |
| INTC | 0 (DROP) | DP block buying into a −10.16% decline with a call-side OI build | none | **No valid DP shelf exists** — see below | **skip** |

**NBIS — ⚠ distribution caution.** `distribution_flag` present (09-04 $190C, $2.34M closing, OI −1,314). More importantly the **OI build runs against the thesis 2.5:1 by contract count**, largest add the 2026-10-16 **$125 PUT (+9,325, 39% OTM at 44 DTE)**. **But state the dollars alongside the count:** that put is **$1.31M of premium**, while NBIS's tape is **call-dominated by dollars — $80.33M call premium vs $36.61M put premium, PCR 0.62**. The "put-dominant build" is a *contract-count* artifact of cheap far-OTM puts; three separate agents weighted it as a major bearish tell. It does not rescue the long — the insider cluster and the scale failure below are untouched — but the count should never stand without the dollars.
**The +3 rests on noise-level accretion:** +$123.9M is **1.59% of $7.816B gross**. It clears the $50M absolute floor and **fails the 5%-of-gross scale floor**. `conviction-matrix` reads DIRECTIONAL_LONG at only **18.5%** confidence. Confluence gate **FAILED** — 1 of 10 agents.

**INTC — the "bullish OI build" is covered-call overwriting, not accumulation.** `uw insights conviction-matrix` returns scenario **`COVERED_CALL`** (conf 31.8%): *"Dark pool buying + call selling — yield enhancement, capping upside."* Raw legs confirm it: **call_bid_volume 191,632 > call_ask_volume 156,422 — calls net SOLD.** The build is real but sell-side; upside is capped by construction. C11 **fails on sign mismatch** (cum_flow_30d −$237.3M). **And there is no valid C34 anchor:** the top price-level bucket is $90.05 = $631.8M (48% — the close), while the second tier $89.78 holds only $10.4M, **60× smaller**. That is the day's range floor, not a defended institutional level.

### 3b. Short / fade swings (defined risk only)

**All directional shorts print as `watch_only` (2026-08-01 P0 #1). Routing, not suppression** — full theses below.

| Ticker | Score | Thesis | Structure | Invalidation | Sizing |
|---|---|---|---|---|---|
| **IWM** | 4 (LOW) | Verified multi-session institutional put-spread campaign into the CPI expiry, struck into the deepest negative-gamma trenches on the grid | **Long 285P / short 275P, exp 2026-09-11**, ~$1.178 net debit per spread | IWM reclaims 297, or the campaign stops re-striking lower | **watch_only** |
| SPY | 2 (DROP) | 755/760 put vertical expiring on CPI day, bought at a relative IV *trough*; spot 0.69% above the largest put wall in a short-gamma book | Long 760P / short 755P, exp 09-11 | SPY reclaims the 20dma 768.98 | **watch_only** |
| QQQ | 1 (DROP) | Only qualifying mechanized DEX flip of the session + a CPI-day put vertical landing *on* the dte9 IV bump | Long 705P / short 695P, exp 09-11 | DEX reverts positive; close above the 730 call wall | **watch_only** |
| PANW | 1 (DROP) | −$51.7M/30d bearish flow aligned short (−2.47% of gross — scale-meaningful); five-month insider selling cluster | none proposed | 90d flow stays positive; drop recovers | **watch_only** |
| MRVL | −1 (DROP) | DEX **and** GEX regime both flipped negative on 2026-08-28 and have held four sessions | none proposed | DEX and GEX both revert positive ≥2 sessions | **watch_only** |
| GLD | −2 (DROP) | *Bullish* structures against persistently bearish flow — conflicted, not a short | 2× call verticals (9/18 415/435, 9/11 430/445) | — | **skip** |
| MU | −4 (DROP) | Most disconfirmed name on the board | — | — | **skip** |

**IWM — the decisive decomposition.** The two largest OI adds are **one structure, not two signals**: 285P bought **98.3% ask-side** (+163,038) and 275P sold **99.99% bid-side** (+166,122), OI diffs matching within 1.9%, both expiring 09-11. Net debit **$1.6182 − $0.4400 = $1.178/spread ≈ $19.2M** — against **$19.6M and "~$1.18 per spread" yesterday**. The campaign is continuing essentially unchanged, one DTE closer. **Consequence: IWM's `flow_direction: bullish` label is the sold wing of a bearish spread being counted as bullish premium — it must not be read as bullish positioning.** The quant's "52:1 put build" is more honestly a large defined-risk **put-spread** campaign than naked put buying. Still net bearish, still direction-verified.

**SPY — a staleness nuance that cuts against the bull.** The bull leaned on "+$63.2M/30d cum-flow is bullish," but the **two most recent sessions are both bearish** (−$27.0M today, −$13.8M yesterday) with PCR rising to 1.24/1.18 from 1.03. The 30d bullish aggregate is **stale relative to a freshly bearish two-day tape** — the mirror of the falsifier applied to GLD below.

**GLD — the freshness falsifier was checked and it HELD.** A −3 `flow_conflict` against the bullish call-spread structures is well-founded and **scale-robust**: GLD is bearish at *every* window — 5d −$67.6M (−6.40% of gross), 10d −$156.6M (−5.51%), 20d −$268.8M (−4.73%), **30d −$565.6M (−6.93%)**, 90d −$523.4M. This is **not** the 2026-08-21 stale-flow artifact (which had fresh *bullish* 5d against stale bearish blocks). Clears both the $50M and 5%-of-gross floors. The structures themselves are also **not term-structure anchored** — after 0DTE hygiene the curve is **FLAT** (dte9 28.1% / dte16 27.8%), so there is no vol edge, only direction.

**MU — the most disconfirmed name in the book (raw −4).** P/C z = **−2.233 BULLISH_EXTREME** (0.53 vs 20d mean 0.71), widening monotonically 5d −1.123 → 10d −1.631 → 20d −2.233; price **−3.45%** while flow ran **+$83.1M bullish** — the crowd buying calls into weakness. That earns the **−2 informed-flow *continuation* penalty** (single-name P/C extremes predict continuation, not reversal — this is a dock on a long, not a fade signal). Plus a **−3 flow_conflict** (cum_flow_30d −$303.4M). Sector-leader +1 **fails** condition (b). 5/5 bearish sweep persistence on the highest cumulative premium in the non-index book. **Even with the −3 removed, MU is raw −1 and still drops.** Its KINKED term structure has `kink_dte = 9 = 2026-09-11 = CPI` — macro beta, not name-specific edge.

**Sweep ledger (informational, 0 rubric points — the sweep-persistence line was removed 2026-05-23 P0.3).** Persistence-first: MU 5/5 bearish ($2.69B cum premium, the largest non-index book), PLTR 5/5 bearish, SNDK and SPCX 5/5 *mixed* (no thesis), MSTR/MRVL/AMD 3/5 bearish, MSFT 4/5 bullish (cum-flow aligned +$798.8M — **but see the decay note in §8**). **TSLA and IWM were demoted on a hedge-flow signature**: TSLA's 4/5-bullish sweep sits against −$539.3M 30d cum-flow with its largest print a 0DTE $355C; IWM's 4/5-bullish is contradicted by three ask-side put strikes on the live tape and, as shown above, is the sold wing of a bearish spread.

---

## 4. LEAP Builds (6–24 months)

**Empty. No candidate cleared 6-of-9 gates.** LEAP share of today's tape is **3.8%** — an empty book is the correct output here, not a search failure.

Disqualifications worth recording: **GDX** failed the required 90d accretion gate outright (90d −$107.8M **decaying into** 30d −$141.9M — accretion running the wrong way as the window narrows). **EWZ** failed on scale (90d +$11.1M on $1.06B gross ≈ **1.0% of gross** — flat, MIXED at both windows), despite a genuine fresh far-dated call build. **AAPL** failed three ways — the 380-DTE $350C build is **bid-side dominated** (11,080 vs 232 = call *selling*), 90d cum-flow −$9.4M on $17.9B gross (≈0.05%, pure noise), and `conviction-matrix` MIXED at 3.9%. SPY/QQQ DTE>180 candidates were deep-OTM **puts** — tail hedges, not directional longs, excluded by construction.

---

## 5. Volatility Surface

**Mandatory hygiene was run** (`scripts/term_structure_hygiene.py`, `min_contracts=15` — a named, tunable, **not audit-frozen** parameter). Population: raw label BACKWARDATION on 6/8; after hygiene BACKWARDATION 5/8, KINKED 3/8, **3 of 8 flipped** purely from dropping the 0DTE bucket.

**Population firing rates — grade the instrument, not just the name.** `front-end-iv-ratio` at `--near-dte 7` fired BACKWARDATION on **7 of 7** names in the earnings population (ratios 1.32–1.57, all snapping to dte=9) — **100% firing rate, zero discrimination today**. In the vol-scout population it fired 2 of 6. Treat as context, never as a standalone signal.

**Macro-beta falsifier fired once and killed a name.** SPY `kink_dte=16`, QQQ `kink_dte=16`, **OKLO `kink_dte=16`** — all 2026-09-18, i.e. **monthly OPEX, not a company event**. OKLO's KINKED label is shared index beta, scored **0**.

| Ticker | Honest expression | VRP | Evidence | implied_move | Verdict |
|---|---|---|---|---|---|
| **NTAP** | **SELL VOL via calendar** | **+0.4087** | IV 76.0% vs RV30 35.1% **and RV10 25.3%** — gap holds on both windows, not a stale artifact. iv_rank 100 (only liquid name in that slice). | **16.2%** | **skip** — VRP gate |
| **QBTS** | **BUY VOL** | **−0.4618** | IV 65.0% vs RV30 111.2%; rv10 84.9% still hot — robust across windows | 20.1% | **skip** — cluster |
| **OKLO** | BUY VOL | −0.2853 | IV 68.6% vs RV30 97.2%; robust — **but the KINK is OPEX macro beta** | 21.3% | **skip** |
| **ORCL** | **SELL VOL via calendar** | +0.0786 | The one genuine kink-at-event: `kink_dte 9` = 2026-09-11, prominence **13.5%** on 7,057 contracts, base CONTANGO | **`null` — deliberate** | **skip** — VRP gate |
| CPB | SELL VOL | +0.1083 | Back-month skew TAIL_HEDGING at both tenors (1.134 / 1.225) — the only such name | **4.56%** (valid, T+1) | **watch_only** |
| RKLB / CLS / NVTS | — | negative | **DISQUALIFIED on the RV10 stale-artifact check** — rv10 has collapsed *below* current IV (RKLB 37.8% vs IV 64.2%) | — | **skip** |

**ORCL's `implied_move` is `null` on purpose.** Its `earnings-catalyst` figure of 2.93% is computed off the **dte=1 tenor, which expires five days before the 09-08 print** — the known pre-event-tenor defect that understates the true move 4.5–5.8×. Emitting it would poison the exact field the last three audits are trying to build. Re-derived off the 09-11 tenor the move is ~11.9%. **Additional risk the macro check did not catch: the 09-11 expiry is CPI day, so that front leg bundles *both* ORCL earnings and CPI — selling it sells two event premia, not one.**

**`NO_NEAR_TENOR` is not `FLAT`.** NTAP's hygiene `front_end_ratio` is `null` — its tenor ladder jumps 16 → 44 DTE with nothing near the 30-day target, and the raw call snapped `near_dte_actual` to 16, returning a meaningless 1.000. That means **unmeasurable**, never "calm."

**`uw historical iv-percentile-zscore` silently short-delivered again:** `dates_used: 100` against a 252-day request. Percentile reads are provisional.

**No KINKED name with genuine catalyst alignment survived**, and the cached `iv_outliers` list is 100% leveraged-ETF 0DTE noise (SOXL/TQQQ/TLT/SMH) with no C12-liquid overlap.

---

## 6. Risk & Correlation

**Macro headline:** stagflationary tilt — **core PCE 3.34% sticky against payrolls −23k**; curve normal +0.40; USD weakening −2.04/30d. **NFP T+2, PPI T+5, CPI T+6, FOMC T+9** (trading days, Labor-Day-corrected).

**Correlation — one connected component, not three.** `uw risk portfolio-correlation` run against **today's candidates**, not the static watchlist:

`macro_beta_cluster` = **IWM · SPY · QQQ · INTC · MU · MRVL · ORCL · QBTS**

| Pair | corr | Role |
|---|---|---|
| SPY/QQQ | 0.911–0.915 | index core |
| IWM/SPY | 0.846–0.856 | index core |
| **QQQ/INTC** | **0.875** | **bridge: index ↔ semis** |
| MU/INTC | 0.845–0.852 | semis |
| **QQQ/MU** | **0.754–0.762** | **bridge** |
| SPY/ORCL | 0.740 | bridge: index ↔ vol |
| MRVL/INTC | 0.729 | semis |
| **QBTS/IWM** | **0.706** | bridge: index ↔ vol_long |

**The index-short book and the semis book are ONE position.** Kept member: IWM (highest raw_score). All others take −1 tier.

> **Two instrumentation notes carried forward, flagged not acted on.** (1) `sector_breakdown` returned `{"Unknown": 15}` with a spurious *"100% in top sector"* warning — **there is no real 100% concentration**; known defect, ignored. (2) The tool showed **~0.010 pull-to-pull jitter** on identical pairs across different symbol universes (SPY/QQQ printed both 0.911 and 0.915; IWM/SPY both 0.846 and 0.856). Today's final kill — QBTS at **0.706** — rests on a coefficient **0.006 above the mechanical line**, i.e. inside the instrument's own noise band. The rule removes discretion in *both* directions so it was fired as written, and QBTS had an independent second reason to drop; but the 0.70 threshold deserves an instrumentation note in the next audit.

**Gates fired.** VRP contradiction killed **NTAP** and **ORCL** (both net **long** vega buying into strongly positive name-level VRP; index VRP would have let them through). Cluster killed **QBTS** and **ORCL**. Sector fired once — **CPB**, Consumer Defensive netted outflow with persistence 0.8. Panic gate **no-op everywhere** (SPY 0.86 / QQQ 0.83, both CONTANGO at the corrected `near_dte 7`).

**Fundamentals verdicts.** **NBIS → CAUTION (−1), `insider_selling_cluster`** — MSPR **−100 in 4 of 5 months** (3mo avg −73.42) against a claimed accumulation long; a −100 print means every share transacted that month was a sale. **PANW → CAUTION (−1), `news_catalyst_contradicts_thesis`** — PANW **beat FQ4 and guided FY2027 above Street, then fell −9.28%** (worst of 503); a fresh short chases an already-fired event. **IWM/SPY/QQQ → NA (0)** — ETFs, no company layer; **NA never penalizes.** **No VETO anywhere.**

**Event-risk gate.** NFP at T+2 is a dated Tier-1 binary inside every swing horizon opened today. **Exemptions applied honestly:** IWM/SPY/QQQ (defined-risk long-premium put structures — max loss is the debit), and QBTS/NTAP/ORCL/CPB (long-premium, and the trade *is* the event play). **Fired on NBIS, PANW and MRVL** — directional and undefined-risk through the print.

**Debate cuts.** The two names cut are the **two highest-scoring on the board** — the disconfirmation step cutting the crowded top rather than the tail, which is what it was added to do. IWM (bear 0.65 ≥ bull 0.35) and NBIS (bear 0.75 ≥ bull 0.25) each take −1. SPY, PANW and QQQ no-op.

**Adverse-flow exits: none.** Yesterday's `conviction_2026-09-01` held IWM only. Its scan row **contradicts itself** — `flow_direction: "bullish"` and `net_flow +$12.76M` (≈1% of the row's own $1.27B DP premium, i.e. noise) against **PCR 1.72**, put volume 1,028,207 vs call 596,893. As decomposed in §3b, that "bullish" premium is **the sold wing of a bearish put spread**. The label is an artifact; IWM is **not** an adverse-flow exit candidate.

**Breadth cross-check (advisory).** 301 advancers / 201 decliners, pct_green 59.84%, `divergence_flag FALSE`. The informative reading is the **lineage split**: price breadth 59.84% green against options-flow breadth 34.9% bullish, where **yesterday the two agreed at 31.4% / 31.1%**. Price up, positioning defensive.

**Hedge sleeve: none, and recommending one would be an error.** The sized book is empty, so net delta is zero. A hedge against a zero position is an unhedged directional bet wearing a risk-management label.

---

## 7. High-Conviction Cross-Ref (HIGH and MEDIUM tier — raw_score ≥ 7)

**Empty. No name reached MEDIUM (7) or HIGH (9).** Highest score on the board is IWM at 4. The Step 3a load-bearing gate no-ops (nothing reached ≥9), and the out-of-regime half-cap never binds because nothing reached a conviction tier.

**Expectancy lens** `[advisory — expectancy is not yet a live sizing axis]`, from the 2026-08-30 audit `phase_3_calibration`:

| Tier | n | Expectancy | Payoff ratio |
|---|---|---|---|
| HIGH | 7 | −2.441% | 0.720 |
| MEDIUM | 19 | **+0.104%** | 0.948 |
| LOW | 125 | −2.141% | 0.906 |
| DROP | 542 | −5.964% | 0.601 |

Kelly gate: **`ADVISORY_ONLY`** (n=27 closed sized calls vs a required 30; tier × expectancy non-monotone). The win-rate ladder stays live. Note DROP's payoff ratio (0.601) is far worse than LOW/MEDIUM — the long-running "the trades we refuse beat the trades we take" reading rests on **hit rate alone and does not survive a payoff-aware metric**.

**Win-rate substrate.** `uw historical signal-backtest` supports only five classes (`bullish_flow`, `bearish_flow`, `high_iv_rank`, `volume_spike`, `dark_pool_accumulation`). Today's book is dominated by `multileg_directional` and `vol_term_dislocation`, **neither of which is supported** — so **19 of 20 rows carry `win_rate: null` / `NA(substrate)`**. Both classes that *were* queryable came back degraded: `dark_pool_accumulation` returned **`total_signals: 0` market-wide** (NBIS and INTC unmeasurable), and `bearish_flow` produced the book's only measured quote — **0.5214 on n=140** under the clean protocol (150 kept after dropping 12 clamped rows, then C12 dropping CAR and NDX) — with **`market_excess` exactly −0.1000**: same-direction SPY-short won **0.6214** over the identical windows. **The class does not beat simply shorting the index.**

**Rubric (Step 4), embedded verbatim for audit — `rubric_version: 2026-06-12`, FROZEN:**

```
+1  MECHANIZED DEX flip / vanna-squeeze in trade direction (verified SIGN CHANGE via scripts/dex_flip.py, not a level)
+3  3+ aligned accumulation-hunter signals (DP + OI + smart-positioning, block-stratified institutional-tier)
    — C11 CONJUNCTION: full +3 only when cum_flow_30d sign aligns AND |cum_flow_30d| >= $50M; else halved to +1
+1  multi-day OI build (oi-trend BUILDING, --days >= 5) — direction-verified only
+1  conviction-matrix DIRECTIONAL_LONG conf > 70 — ONLY when dominant_signal_class == leap_directional, else 0
+1  cumulative-premium-flow net directional accretion 30d in trade direction — INTENT-SCREENED
+1  sector-rotation single-name leader — CONDITIONAL: (a) persistence >= 0.6 AND (b) cum_flow direction aligned AND (c) |cum_flow_30d| >= $50M
+1  earnings-scout BUY VOL or SELL VOL
+2  multileg-strategist directional structure (play type ANCHORED TO TERM STRUCTURE)
+1  vol-surface-scout KINKED or BACKWARDATION watch with VRP-aligned bias
+1  opex-pin-strategist top-5 (OPEX week only — NOT APPLICABLE, 09-18 OPEX is 16 days out)
-2  contrarian-scanner overcrowded long with rising pc-ratio-zscore   [informed-flow CONTINUATION penalty, not a fade]
-3  flow_conflict — cum_flow_30d clearly OPPOSITE dominant_signal_class (sign flip + magnitude > union median)
-1  flow_conflict_lite — 30d read MIXED / bottom-quartile magnitude      [-3 and -1 MUTUALLY EXCLUSIVE]
Tiers: >=9 HIGH (full) | 7-8 MEDIUM (half) | 3-6 LOW (starter/watch) | <=2 drop
INVARIANT: Sum(score_components[].points) == raw_score
```

**Union-median |cum_flow_30d| used for the −3 magnitude test: $263.3M** (median of the six gated names: QQQ 317.9 / SPY 63.2 / IWM 223.2 / GLD 565.6 / MU 303.4 / MRVL 13.0). The full 20-name union median of $28.5M was **rejected** — pooling a $48B-gross index book with a $15M-gross single name is the C49 bigger-wronger-denominator error. Sensitivity disclosed: on the wide denominator SPY → −3 (raw 2→0) and INTC → −3 (raw 0→−2); no tier changes.

**Deep-dive hand-off: skipped.** No HIGH-tier names — the step is explicitly skipped on a no-edge day.

---

## 8. Watch-only — single signal, no confluence

Failed the ≥2-agent gate. **Journaling only, not for entry.**

- **NBIS** (accumulation-hunter) — richest single-agent evidence set on the board; detailed in §3a.
- **INTC** (accumulation-hunter) — covered-call overwriting; §3a.
- **NTAP, QBTS, OKLO** (vol-surface-scout) — §5.
- **ORCL, CPB** (earnings-scout) — §5. ORCL is the only genuine kink-at-event of the session.
- **PANW** (contrarian-scanner; dealer-positioning called it NEUTRAL/event-contaminated) — §3b.
- **EWZ** (multileg only; **leap-positioning-radar evaluated and disqualified it**) — call diagonal 10/16 C40 / 11/20 C45 on a genuine Oct–Nov IV shelf (dte30 32.3% → dte44 40.9% → dte79 43.8%), likely a Brazil-specific catalyst, unconfirmed. Note its 12/18 $35 calls are simultaneously being **closed** (OI −69,586 on 70,026 volume) — maturity rotation, not clean fresh conviction.
- **PCG, ET** (multileg only, LOW confidence, small notional). PCG's front-end IV of 292.5% at dte2 is name-specific distress (−26.8% over 5d), not NFP.
- **RKLB, CLS, NVTS** (vol-surface, disqualified on the RV10 stale check) — §5.
- **MSFT** — the only non-ETF name with clean bullish 30d cum-flow (+$798.8M, labelled BULLISH), **rejected on the decay falsifier**: 90d is only **+$57.2M**, implying the prior 60 days were net *bearish* and the "accumulation" is a recent non-persistent spike. `institutional-accumulation` also read NEUTRAL.
- **CRWD** — advisory `CLOSING_ANTISIGNAL` (Tier-4) on a $3.00M call, dte 135 → **AVOID**; weakens any bullish CRWD thesis. There were **no Tier-1 single-leg signals at all today**.

---

## Appendix — substrate findings recorded this session

Nine defects re-confirmed with live numbers, plus one new:

1. **NEW — `oi-trend.consecutive_build_days` is CENSORED BY `--days`.** Verified: returns exactly **5 at `--days 5`, 10 at `--days 10`, 30 at `--days 30`**; only the default (101 sessions) reveals the true run. Across 7 names at `--days 5`, **all 7 returned exactly 5**. This *explains* the long-standing "BUILDING fires 14-of-14" defect — it was never merely non-discriminating, it is **mechanically equal to the window**. At the default the field does discriminate (SPY 6, GLD 35, PANW 49) while **QQQ, MU, MRVL and NBIS all saturate at 101/101**. The frozen rubric's `--days >= 5` condition is therefore **tautological** for any continuously-building name. **Today's +1 OI awards are unaffected** — the quant scored on its own ≥2:1 call-vs-put direction-verification bar, never on the BUILDING label. **Freeze-bound: register, do not patch.**
2. **Dark-pool contamination, BOTH mechanisms, live.** Basket/program prints: **SPY $500.00M, GOOGL $500.00M and META $426.13M in the same second (20:59:14Z)**; NVDA $500.00M at 20:59:25Z; **VOO and IVV at an identical $574.95M** (20:08:17Z); IVV **$1,000.00M twice** at the same timestamp and size. Plus every top-20 print landed **20:00–20:59Z, the closing auction**. Any DP-derived distribution/accumulation claim on SPY/NVDA/GOOGL/META today is contaminated.
3. **The $2.10B top-20 whale tape is SPX financing machinery, not direction.** Deep-ITM $7000C paired with $8000P across five matched expiries. **Two legs outright sub-parity** — SPXW 8000P 09-30 (TV −12.18, $93.9M) and SPX 8000P 09-18 (TV −7.91, $72.4M) = **$166.3M of "bearish put premium" that is financing**. Near-parity stock-replacement calls (SPXW 7000C 09-30, TV +27.23, delta 0.962). **The only genuinely convex ticket in the entire top-20 is SPX 8000C Jan-2027, TV +146.20, delta 0.375, $46.1M.** QQQ 700P 12-18 ($41.3M) carries `side: no_side`.
4. **`analyst-vs-flow` has no analyst leg — 0 of 7 rows** (prior audit: 0/21). Confirmed broken.
5. **`front-end-iv-ratio` fired 7 of 7** at `--near-dte 7` in the earnings population — zero discrimination today.
6. **GEX `regime` label contradicts its own `total_gex` sign** on QQQ, on both 09-01 and 09-02 (label POSITIVE, sign −304.9M).
7. **`iv-percentile-zscore` silently short-delivered** — `dates_used: 100` against a 252-day request.
8. **`portfolio-correlation.sector_breakdown`** returned `{"Unknown": 15}` with a spurious 100%-concentration warning; **plus ~0.010 pull-to-pull jitter** on identical pairs.
9. **`sector-flow-persistence` fired INFLOW on 9 of 11 sectors** (five tied at 1.0) — near-zero discrimination.
10. **`dark_pool_accumulation` signal-backtest returns `total_signals: 0` market-wide** — the class is unmeasurable, so NBIS and INTC have no backtested support at all.

**Scale-asymmetry defect fired three times today, in both directions.** QQQ took a **−3 on 0.66%-of-gross** (second consecutive session; 09-01 was 0.71%), MU a **−3 on 0.54%-of-gross**, while **ET was denied a +1 despite carrying the book's strongest scale-relative reading (+18.96% of gross)** because it failed an absolute-dollar floor. GLD is the control case — its −3 clears both floors and is scale-robust. The award side of that field requires **$50M *and* ≥5% of gross**; the deduction side has **neither**. Applied as frozen. **Register, do not patch.**

**Model routing:** fleet models/effort are pinned in `.claude/agents/*.md` frontmatter (quant + risk-monitor opus/high; synthesis fleet sonnet/high; mechanized agents sonnet/medium). 10 Phase 1 agents spawned — `opex-pin-strategist` correctly omitted (2026-09-18 OPEX is 16 days out).
