# Phase 2 — Outcome Resolution (2026-06-27)

**Resolution method (C20).** Real daily-OHLC, path-aware. Bars pulled from the Yahoo chart API
(`query1.finance.yahoo.com/v8/finance/chart`, stdlib `urllib`) — **not** the close-only
`mcp__yahoo-finance__*` tools. 90/90 tickers + SPY fetched; SPY = 51 real-OHLC bars through
**2026-06-26** (close 728.99, sanity-matches the 06-26 regime note). `R = 0.5 × true-range-ATR(14)`
at entry. Window walked bar-by-bar; a long is LOSS the first day `low ≤ entry−R` *before* any day's
`high ≥ entry+R` (symmetric for shorts). MAE from daily extremes. No close-only degradation — a
ticker with no OHLC is INCONCLUSIVE(`data_unavailable`), never a LOSS.

**Win threshold (verbatim).** *≥ +1R move in thesis direction within the horizon window without −1R
drawdown first*, R = 0.5 × ATR(14) true-range (structure-implied R not separately parsed this run).
Path-aware: a +2% gain that came after a −1.5% drawdown is a LOSS.

**Horizon→window:** swing 10D (3D corroboration) · weekly 10D/5D · LEAP 90D (**never resolved until
window closes** — 4 rows held INCONCLUSIVE `leap_window_open`) · vol 10D RV-proxy.

## Headline

| Bucket | n | WIN | LOSS | WR |
|---|---|---|---|---|
| **All decided** | 205 | 96 | 109 | **46.8%** |
| Sized book (all) | 31 | 13 | 18 | 41.9% |
| **Sized — directional only** | **16** | 7 | 9 | **43.8%** (mean −1.09%/name) |
| Paper (benched) | 174 | — | — | 47.7% |

INCONCLUSIVE 46 = window_open 39 (the late-June choppy/selloff calls) · leap_window_open 4 ·
no_threshold 2 · data_unavailable 1. NOT_A_TRADE 6 (directionless neutral). **INCONCLUSIVE rows are
excluded from every win-rate denominator downstream.**

> ⚠️ **The sized-book P&L is NOT dollar-denominated.** The raw "sum_ret −57.2%" on the 31-name sized
> book is a measurement artifact: 15 of 31 are **vol-mode, RV-proxy** rows whose "return" is the
> realized-range ratio (WDC vol_short "−71%", SOXX vol_long "+68%"), not a position P&L — a short
> straddle does not lose 71%. **Strip them and the real-money directional sized book is n=16, WR
> 43.8%, mean −1.09%/name.** All vol "returns" below are RV-direction proxies; never read them as $.

## The edge / beta split — C21 benchmark-excess (the number that matters)

SPY same-window same-direction benchmark resolved on 189 directional rows.

| Direction | Book WR | SPY base | **Excess** |
|---|---|---|---|
| long  | 51.0% (n=96) | 29.4% (n=109) | **+21.7pp** |
| short | 47.8% (n=69) | 72.5% (n=80)  | **−24.7pp** |

This window the **tape actually fell** — SPY cleared a long +1R only 29% of the time, a short +1R 72%
of the time. So the long edge is *real selection*, not an up-tape artifact, and the short book's
deficit is *genuine negative selection* — it shorts names that fall **less** than the index. This
reconfirms 06-20 (+15–20pp long / −22.7pp short) on more data **and in a falling tape**.

> **⚠ Verification adjustment (workflow re-derivation, binding).** The +21.7/−24.7pp headline uses
> *mismatched denominators* (book WR over decided rows; SPY base over all benchmark-resolved rows incl.
> INCONCLUSIVE). The **matched-basis excess is +18.7pp (long) / −21.7pp (short)** — same sign, same
> conclusion, ~3pp smaller. The short deficit is statistically robust at the aggregate (paired McNemar
> p=0.0035); the short book has **positive excess in zero decided regimes.** Use the matched-basis
> numbers as primary.

### Regime-stratified (Phase 3b) — the split is regime-dependent but one-signed
| Regime | long excess | short excess |
|---|---|---|
| uptrend | **+29.1pp** (n=55) | **−34.3pp** (n=35) |
| pullback_in_uptrend | **+4.9pp** (n=41) | **−8.8pp** (n=34) |
| choppy | 0 decided | 0 decided |

Long edge compresses as the tape weakens (+29 → +5) but stays positive; short edge is least-bad
when the tape helps (−8.8 in the pullback) but **never turns positive in any gradeable regime.**

> **⚠ Significance (workflow re-derivation, binding).** Only the **uptrend** legs are statistically
> significant — long +29.1pp p=0.003, short −34.3pp p=0.006. The **pullback** legs (long +4.9pp p=0.79,
> short −8.8pp p=0.45) are **indistinguishable from zero.** So the long edge is, on this data, a
> *single-regime (uptrend) phenomenon* — not yet proven cross-regime. The choppy/selloff stratum is
> still window-open. This caps every edge-based recommendation at P1.

### Post-freeze direction flip (regime tailwind, not selection)
Post-freeze **shorts won 68.0% (n=25)** vs longs 47.4% (n=19) — the falling tape finally rewarded the
short book in *absolute* terms. But the SPY-short base over those same windows was **88%**, so the
post-freeze short **excess is −20.0pp** — essentially unchanged from the pre-freeze −22.7pp. The freeze
did **not** fix short negative-selection; the 68% is a pure **regime tailwind, not selection.**

> **⚠ Index-vs-single-name (workflow re-derivation — REVISES the 06-20 prescription).** The prior
> audit's "stop single-name shorts → express bearish index-relative" rule is **contradicted** this
> window: index/ETF shorts realised 34.6% WR / **−1.26% mean** (n=26) and the **sized** real-money short
> book is **6 of 7 index ETFs** (SMH/IWM/SPY) at 33% WR / **−2.10% mean**; the lone sized single-name
> short (NVDA) **won +3.98%**, single-name shorts averaged **+0.83%**. Single-names show a *larger excess
> deficit* (−25.6pp) only because they landed in deeper down-tape windows (a benchmark-denominator
> artifact). Defensible carry-forward: **no short selection-alpha anywhere → don't size shorts for
> alpha** — *not* a structural index-expression preference (split rests on n=1 sized single-name vs n=6
> sized index → P1). See Phase 7 Rec 1.

## Vol classes (RV-proxy — heavy caveat)
`vol_long` 100% (n=11), `vol_short` 7.7% (n=26), and the split is **uniform across regimes**
(vol_short 0.077 in both uptrend and pullback). This near-binary outcome is a **methodology
signature of the RV-direction proxy**, not a tradeable "short-vol loses 92%" claim — true IV-vs-RV
needs an `implied_move` field the envelopes don't carry. Phase 3 treats these as
`vol_resolution=rv_direction_proxy` and never as calibrated IV-vs-RV outcomes.

## Per-ticker concentration note
The decided LOSS column is concentrated in **semis shorts** — SMH appears as a short LOSS on 05-28,
05-29, 06-10, 06-12; IWM short LOSS 06-05. This concentration is the mechanical driver of both the
short-book −24.7pp and the HIGH-tier inversion (Phase 3).

**Outputs:** `phase_2_outcomes.jsonl` (257 rows + outcome fields), `phase_3b_regime.jsonl` (regime cuts).
