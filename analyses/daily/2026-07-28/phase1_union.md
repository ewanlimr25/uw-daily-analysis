# PHASE 1 CANDIDATE UNION — 2026-07-28 (all 10 agents returned)

Input to `signal-confluence-quant` (Step 2a). Rubric is FROZEN at `2026-06-12`.

## Headline: FOUR agents returned clean ZEROS

| Agent | Scored output |
|---|---|
| `accumulation-hunter` | **ZERO** accumulation flags. NBIS watch-only, `conjunction_met: false` |
| `contrarian-scanner` | **ZERO** qualifying fades. **No `BULLISH_EXTREME` anywhere** → the −2 line is unclaimable on every name |
| `leap-positioning-radar` | **ZERO** LEAP candidates (best = GEHC/IBM ≈3-of-9 gates; no conviction-matrix confidence >70, max 25) |
| `dealer-positioning-strategist` | **ZERO** mechanized DEX flips; **ZERO** vanna squeezes |

---

## SCORED-LINE ELIGIBILITY (adjudicate mechanically; do not re-derive)

- **+1 mechanized DEX flip** — **NONE.** The MU/NBIS/AMAT/WDC/INTC flip fired **2026-07-24**, 4 sessions stale; latest session shares sign with priors so `dex_flip.py` returns `qualifies=false`. Correct behaviour, not a bug.
- **+1 vanna squeeze** — **NONE.** VIX 07-24 18.58 → 07-27 18.67 → 07-28 18.21 = no clean ≥3-session decline. All put-heavy books are "vanna pressure, not squeeze."
- **+3 / +1 accumulation conjunction** — **NONE.** Zero names flagged.
- **+1 conviction-matrix (leap_directional ONLY)** — **NONE.** No name >70 confidence. In all non-LEAP contexts this line contributes **0** regardless.
- **+1 oi-trend BUILDING** — fired **13-of-13** and **16-of-16**. Zero discrimination (C47). Award per rubric where genuinely BUILDING, but flag the non-discrimination.
- **+1 sector-leader (needs ALL of: persistence ≥0.6 ∧ cum_flow_30d aligned ∧ |cum_flow_30d| ≥ $50M)** — **TSLA** (−$650.2M) and **BE** (−$214.7M) ONLY. Both **shorts**. Every long leader (GEHC, UHS, LW, KVUE, KNSA, INCY, THC, RCL) **fails the $50M bar**.
- **+1 earnings BUY/SELL VOL** — AAPL, AMZN, SHOP, DDOG (SELL VOL), **PLTR (BUY VOL)**.
- **+1 vol-surface KINKED/BACKWARDATION + VRP-aligned** — SNDK, GLW, BE(watch), NBIS, MU, WDC, CRWV, TSEM, QCOM, TSLA. **NOT eligible:** AMAT/KLAC/INTC/SMH/SOXL (VRP FAIR), GFS/NXPI (NO_NEAR_TENOR), **IBM (backward-window artifact — do not score)**.
- **+2 multileg directional (term-structure-anchored, risk-capped)** — **SMH, INTC, SNDK, HPQ** qualify. **TSM, KLAC, WDC, NBIS, PLTR, MU, AMAT, GFS, GEV, CRWV, BKNG, IP, ALL, GLOB do NOT.**
- **−2 overcrowded long (rising z)** — **NONE claimable.** No `BULLISH_EXTREME` in the candidate set.
- **−3 / −1 flow_conflict** — apply mechanically. **This is the decisive line today.**

> ⚠ **flow_conflict is the mechanic that decides this board.** Every AI/semis SHORT thesis sits on a tape
> showing **net-BULLISH 30d cumulative premium**: MU **+$464M**, NBIS **+$234.6M**, SNDK **+$146M (day)**,
> CRWV **+$50.4M**, AMAT **+$36M**. Conversely INTC's 30d cum-flow is **BEARISH** against multileg's LONG
> thesis, and SMH's ETF flow is **−$42.3M** against multileg's LONG thesis. Phase 1 proved that positive
> premium is put-selling / call-overwrite / hedge-unwind — **but the rubric is FROZEN and scores the tool
> output, not the interpretation.** Apply the deduction mechanically; let `risk-monitor` gate. Do not
> hand-wave it away, and do not "correct" the tool.

---

## CONFLUENCE GATE (Step 3) — ≥2 distinct agents flagging POSITIVELY, per direction

### PASSES (enter the rubric)
| Ticker | Direction | Agents flagging | Notes |
|---|---|---|---|
| **BE** | SHORT | sector-rotation (+1 gate CLEARS, −$214.7M), accumulation-hunter (DISTRIBUTION-leaning + Tier-1 `OPENING_PUT_PRIME` co-flag), vol-surface (SELL VOL, watch) | ⚠ sweep-tracker dissents — only genuine ask-side call sweep in the book (2,059 trades on 8/21 230C) |
| **AMAT** | SHORT | accumulation-hunter (explicit **DISTRIBUTION** label, buy/sell 0.59, block 0.382), dealer-positioning (SHORT lean, highest conviction of cohort, FEIVR 1.270) | vol lane scores 0 (VRP FAIR) |
| **KLAC** | SHORT | dealer-positioning (SHORT lean, GEX negative all 10 sessions, deepening 2× today), multileg (cleanest bearish structure: Aug P218/Sep P190 diagonal, $4.5M debit) | multileg does NOT award +2 (NO_NEAR_TENOR, single-session) |
| **WDC** | SHORT | dealer-positioning (SHORT lean high conviction, FEIVR 1.250 extreme), multileg (07-31 P540/P490 deep-ITM vertical, $10.4M debit, near-zero vega) | vol-surface says BUY VOL (weak) — axis conflict |
| **SNDK** | LONG / VOL_LONG | multileg (**+2**, Jan-27 1200/1000 bull put spread, $12.1M credit, capped $7.9M), vol-surface (+1 BUY VOL, VRP −0.0997) | ⚠ sweep-tracker + accumulation both say the *direction* tape is artifact/distribution |
| **IBM** | LONG | dealer-positioning (**LONG lean, best-confirmed rotation name** — DEX+GEX both flipped 07-24 and holding, FEIVR 0.993 calm), leap-radar (3/9, explicitly flagged to swing), accumulation-hunter (ACCUMULATION 1.54, $102M cluster at 227.55) | vol lane DISQUALIFIED (artifact) |

### FAILS confluence → §8 watch-only (single positive agent)
**SMH** (multileg +2 LONG only — sector-rotation flags it SHORT, opposite axis) · **INTC** (multileg +2 LONG only — dealer-positioning flags SHORT) · **HPQ** (multileg +2 LONG only) · **PLTR** (earnings-scout +1 only) · **QCOM** (vol-surface +1 only) · **GLW** (vol-surface +1 only) · **TSEM** (vol-surface +1 only) · **AAPL, AMZN, SHOP, DDOG** (earnings-scout +1 each, single-agent) · **CRWV** (vol-surface +1; accumulation "distribution-leaning" is not a clean positive flag) · **NBIS** (vol-surface SELL VOL vs dealer SHORT vs accumulation WATCH-not-flagged — no 2 agents agree on one direction) · **MU, TSLA** — see below.

**MU** and **TSLA** each have 2 agents flagging but on **opposite axes** (MU: vol-surface BUY VOL vs dealer-positioning SHORT; TSLA: sector-rotation SHORT +1-gate-clearing vs vol-surface BUY VOL). Score them, but the direction is contested — treat the directional and vol theses as separate rows, not one call.

---

## LOAD-BEARING TOOL GATE (Step 3a) — 3-of-4 required for HIGH
Members: `dark-pool block-stratified` · `historical cumulative-premium-flow` · `insights institutional-accumulation` · `options-structure dex`.
`institutional-accumulation` returned **NEUTRAL or DISTRIBUTION on every candidate**; zero DEX flips.
**Expect no name to cite 3-of-4 affirmatively → any raw ≥9 must demote to MEDIUM.**

---

## ARTIFACTS — DO NOT SCORE (verified this run)

1. **SNDK +$146.4M "bullish"** = one `no_side` $124.5M 2027-06-17 C1020 clip (2,500×, 1 trade) **+ $41M of deep-ITM 07-31 put SALES**. `multileg` proved the mechanism **cross-session**: P1390/P1500 opened as a matched spread 07-24, printed bid-side 19:42:28 on 07-28 at δ−0.96/−0.91. **Hedge monetization, not conviction.**
2. **MU +$28.6M / AMAT +$28.0M** = systematic laddered **put WRITING** across 10 and 5 tenors respectively in the last 30 min (~$52M / ~$29.5M collected). **Vol supply, uncapped. Not directional.**
3. **GFS +$7.9M / GEV +$11.4M** = **one put-write ticket each** (GFS 7,938× Jun-27 P45; GEV 200× Dec-28 P1420). No structure.
4. **SPX −$2,986M "bearish"** = 53.7% paired same-timestamp/same-size deep-ITM C7000+P8000 **conversions/boxes**, plus a $1.818B δ0.95 C4000 stock-replacement. **Financing, not direction.**
5. **BKNG bearish confluence-5** = a 4-leg Dec-2028 192/208/212/228 package, ~$75.9M gross netting **~$0.3M**, delta/vega-neutral. Real positioning is **LONG** (deep-ITM stock replacement).
6. **HPQ bearish tag is INVERTED** — Sep-18 P26 OI 487→12,203 with **85% bid-side (9,023 bid vs 1,581 ask) = puts SOLD** → bull put spread + ITM call stock replacement. **HPQ is LONG.**
7. **Closing-cross contamination (systemic).** MU mega-tier 0.803 buy ratio is 72% two prints at 20:08–20:10Z tagged `extended_hours_trade` ($2.264B + $432M of $3.73B). Same for SNDK/AMZN/AAPL/SPY/IVV/QQQ/IBM/ADBE/NOW/UHS/WDC. **Use BLOCK tier, not mega tier** (MU block **0.442 sell-lean**; SNDK block 0.458).
8. **`sector-flow-persistence` Technology 1.0 INFLOW** on a −1.84% XLK / −3.45% SMH day = sign-agnostic gross-flow defect. Also hits **Energy** (1.0 INFLOW vs XLE −1.35%, ETF −$29.1M).
9. **`iv_rank` saturation** — 20+ names at exactly 100. **`LARGE_DARK_POOL`** fires on ~85 of 86. **`oi-trend BUILDING`** 13/13 and 16/16. All zero-discrimination.
10. **`iv_outliers`** dominated by same-day-expiry contracts at 2,000–7,000% IV. Unusable.
11. **`iv-percentile-zscore` `dates_used: 74`** on all 18 names — below the 120-day floor. **All percentiles PROVISIONAL.**
12. **`analyst-vs-flow` returned no analyst field** on all 13 payloads — lane unavailable this run.
13. **`gex-time-series` `zero_gamma_level`/`regime` broken** — SPY ZGL 360.62 vs spot ~740; IWM rows labeled POSITIVE carrying negative `total_gex`. Bug now confirmed on AMAT/WDC/INTC/IBM/ADBE/NOW too. **Use `total_gex` sign only.**
14. **Non-standard/un-split-adjusted strike grids** (exclude): MU 2028-12 P2110/P2390/P2470/P2480/P2500; SNDK 2028-09 P2450/P2460/P2470; WDC 08-28 & 09-04 P860. (BKNG 169.6 is a *legitimate* post-split adjustment — keep.)
15. **`fz`** ticker column has first-char duplication; squeeze screen truncated to A/B. Squeeze lane unusable; RS lane de-mangled and used advisory-only.

---

## MACRO / EVENT GATE — applies to EVERY call
**FOMC decision 2026-07-29 2:00pm ET + Chair Warsh presser 2:30pm ET — TOMORROW.**
PCE 07-31 · NFP 08-07 · CPI ~08-12.
Macro: core PCE **3.41%** YoY sticky · 10Y **4.65%, +27bp/30d rising** · USD weakening · fed funds 3.63% → **hawkish-risk**.
Book is buying protection: **08-07 (NFP) $1.18B puts vs $717M calls**; 07-31 (PCE) $2.50B puts vs $1.98B calls.
`multileg` expiry census: WDC, NBIS, SNDK, MU, SMH, INTC, BE all have **07-29/07-31 event legs straddling the Fed** — these are event trades, NOT directional conviction.

**Every swing horizon on this book contains FOMC. The `event_risk` gate should fire near-universally.**

## CORRELATION (pre-pulled, 30d) — collapse to ONE cluster
MU/SNDK **0.904** · SNDK/SMH 0.875 · MU/AMAT 0.865 · AMAT/SMH 0.864 · MU/SMH 0.856 · SNDK/AMAT 0.850 · BE/SMH 0.687 · BE/NBIS 0.623 · NBIS/SMH 0.623.
→ **MU, SNDK, AMAT, SMH, NBIS, BE, KLAC, WDC are effectively ONE position.** Any book holding more than one is not diversified.

## TAPE
RSP +1.17% > SPY +0.24% > QQQ −0.97% · XLK −1.84% · SMH −3.45% · SOXL −14.52%.
Index rv20 **9.3–11.0** vs AI complex **60–190** (SOXL 170.6, SNDK 141.9, NBIS 138.1, BE 123.3).
**Dispersion regime.** Regime TRANSITIONAL/CHOPPY, SPY below both 20/50 SMA. VRP FAIR both indices.
