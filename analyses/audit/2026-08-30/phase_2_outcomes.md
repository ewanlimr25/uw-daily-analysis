# Phase 2 — Outcome Resolution (2026-08-30)

## Method (reprinted verbatim, per skill)

**Win threshold.** ≥ +1R move in thesis direction within the window **without** a −1R
drawdown first, where R = **0.5 × true-range ATR(14)** at entry (no structure-implied R is
carried in the envelopes). **Path-aware (C20):** resolved bar-by-bar on **real daily OHLC**
from the Yahoo chart API (`query1.finance.yahoo.com/v8/finance/chart`, stdlib `urllib`) —
**not** the close-only `mcp__yahoo-finance__*` tools. A long is a LOSS the first day `low`
breaches `entry − R` *before* any day's `high` reaches `entry + R`. A bar that touches both
levels is scored **LOSS** (adverse-first assumption). `max_adverse_excursion_pct` is taken
from daily extremes, never closes.

**INCONCLUSIVE** = window still open, no ±1R threshold touched inside a completed window,
LEAP 90D window not yet closed, or price data unavailable. **A data failure is never a LOSS.**
INCONCLUSIVE rows are excluded from every win-rate denominator downstream.

**Windows.** swing 10D (3D co-reported), weekly 10D, vol 10D, LEAP 30D/90D (never resolved
until 90D closes), opex_pin 5D.

**Coverage.** 190/192 tickers fetched with verified real OHLC (`high != low`). Two failures —
`BRKB` (needs `BRK-B`) and `SPX` (index; needs `^GSPC`) — 1 `watch_only` row each,
tagged `data_unavailable`, **not** LOSS.

## Headline

| | value |
|---|---|
| rows resolved | 789 |
| **decided (WIN+LOSS)** | **693** (was 637) |
| WIN / LOSS | 267 / 426 |
| **book win-rate** | **38.5%** |
| INCONCLUSIVE | 58 (window_open 27, leap_window_open 15, no_threshold 11, data_unavailable 5) |
| NOT_A_TRADE (directionless) | 38 |
| SIZED subset | n=47, WR **42.6%** |
| PAPER (routed, unsized) | n=646, WR **38.2%** |

## Cross-regime coverage

| regime bucket | n decided | WR |
|---|---|---|
| uptrend | 294 | 39.1% |
| pullback-in-uptrend | 141 | 39.0% |
| choppy | 73 | 38.4% |
| transitional / other | 185 | 37.3% |

Directional WR is **flat across all four regimes (37.3–39.1%)**. Whatever is wrong this
cycle is not a regime story.

## The August drawdown is the VOL lane, not the tape

The book's monthly WR falls off a cliff — 54.7% (May) → 41.0% → 40.1% → **27.6% (Aug, n=163)**.
Per **C49** the first move is to check the denominator *before* narrating. It exonerates the
directional book and indicts the vol lane:

| month | book (all) | **directional-only book** | **SPY same-window base** | directional excess |
|---|---|---|---|---|
| 2026-05 | 54.7% (53) | 55.0% (40) | 45.0% | +10.0pp |
| 2026-06 | 41.0% (205) | 44.5% (164) | 47.0% | −2.4pp |
| 2026-07 | 40.1% (272) | 38.7% (191) | 39.3% | −0.5pp |
| **2026-08** | **27.6% (163)** | **35.4% (96)** | **30.3%** | **+5.1pp** |

August's *directional* book beat its benchmark by the widest margin since May. The collapse
is entirely here:

| August lane | n | WR |
|---|---|---|
| directional | 96 | 35.4% |
| pin | 2 | 50.0% |
| **vol** | **65** | **15.4%** |
| — of which `vol_short` | 36 | **8.3%** |
| — of which `vol_long` | 29 | 24.1% |

## New auditor column — SPY-RV vol benchmark (the vol lane had no denominator at all)

The vol lane was the one book with **no benchmark column**: C21 built a SPY same-window
*directional* base rate and left vol resolved against its own trailing range. That made
"the vol book lost" unfalsifiable — indistinguishable from "vol moved". Built this cycle:
for every vol row, the **same-window SPY RV ratio** (10-day mean daily range ÷ trailing-14d
mean daily range) and the boolean "would the identical vol bet on SPY have won."

| stratum | n | book WR | **SPY-RV base** | excess |
|---|---|---|---|---|
| ALL vol | 191 | 32.5% | 51.3% | **−18.8pp** |
| **`vol_short`** | **134** | **27.6%** | **61.2%** | **−33.6pp** |
| `vol_long` | 57 | 43.9% | 28.1% | **+15.8pp** |

Monthly, `vol_short` excess: May +0.0 (n=6, thin) · **Jun −32.3** (31) · **Jul −13.1** (61) ·
**Aug −75.0** (36). **Negative in every month with n ≥ 30, across four regime buckets.**

**And the sign of the confound runs the wrong way for the excuse.** August was a
short-vol *paradise* at the index — mean SPY RV ratio **0.738**, only **12%** of windows
expanded. The book's own names went the other way: mean ticker RV ratio **1.199**. The fleet
selected short-vol on the names whose realised vol rose while the index's fell. That is
**adverse selection**, not a vol regime.

| month | mean SPY rv_ratio | frac > 1.0 | mean *book ticker* rv_ratio |
|---|---|---|---|
| 2026-05 | 1.460 | 92% | 1.549 |
| 2026-06 | 1.205 | 55% | 1.185 |
| 2026-07 | 0.965 | 36% | 1.013 |
| **2026-08** | **0.738** | **12%** | **1.199** |

**Instrument caveat, stated not buried.** Vol rows resolve `rv_resolution =
"rv_direction_proxy"` — RV direction vs trailing range, **not** IV-vs-RV. A premium seller
can lose this test and still book P&L if IV sat above realised. The proxy therefore cannot
price a short-vol trade. It *can* price **selection**, because the SPY-RV column removes the
market-wide component — and the selection reading is what the −33.6pp is. Do not quote the
`vol_short` WR as a P&L claim.

## C59 pin dual-rule — **bar CLEARED, registered 2026-08-15, decided here**

Acceptance bar was **≥3 of 9 rows diverging** between the TOUCH rule and the SETTLEMENT rule.
Result on 11 complete rows: **5 divergent.**

| date | ticker | touch | settle | MAE% | settle-dist% | R% |
|---|---|---|---|---|---|---|
| 06-15 | NVDA | LOSS | LOSS | 5.86 | 5.84 | 3.92 |
| 06-15 | QQQ | LOSS | LOSS | 4.29 | 4.08 | 2.15 |
| 06-15 | AAPL | WIN | WIN | 2.02 | 0.72 | 2.56 |
| **07-13** | **XLF** | **LOSS** | **WIN** | 1.55 | **0.05** | 1.33 |
| **07-13** | **NVDA** | **LOSS** | **WIN** | 5.05 | **0.12** | 3.34 |
| **07-15** | **NVDA** | **LOSS** | **WIN** | 6.84 | **0.21** | 3.27 |
| **07-15** | **IBIT** | **LOSS** | **WIN** | 3.94 | **1.44** | 3.41 |
| 07-15 | AMZN | LOSS | LOSS | 4.91 | 3.97 | 2.97 |
| **07-15** | **PFE** | **LOSS** | **WIN** | 3.34 | **0.00** | 2.35 |
| 08-19 | NFLX | WIN | WIN | 2.79 | 1.55 | 2.87 |
| 08-19 | NVDA | LOSS | LOSS | 4.74 | 3.63 | 3.03 |

**TOUCH rule: 2/11 = 18.2%. SETTLEMENT rule: 7/11 = 63.6%.** A 45.4pp swing on the same rows.
Four of the five divergent names settled within **0.21% of entry** — dead on the pin — after
brushing a wing intraday. An iron fly / short straddle / butterfly pays on **where price
finishes**, not whether the tape ever touched a wing. The TOUCH rule was mis-scoring the pin
book by construction. Phase 5/7 carry the switch; `opex_pin`'s 18.2% in the class table below
is **an artifact of the auditor's own instrument** and is annotated as such everywhere it
appears.

## Decided outcomes by stratum

**Horizon** — swing n=501 WR 40.7% · vol n=192 WR 32.8%. (LEAP: 15 rows, all `leap_window_open`.)

**Tier (all eras)** — HIGH 14.3% (7) · MEDIUM 52.6% (19) · LOW 40.0% (125) · DROP 38.0% (542).
**Post-freeze** — LOW 35.9% (64) · DROP 36.7% (482); **0 decided HIGH, 0 decided MEDIUM** for
a 10th cycle.

**Section** — watch_only 39.8% (289) · swing_long 41.4% (128) · swing_short 40.2% (122) ·
**vol_short 28.4% (109)** · vol_long 42.2% (45).

**Canonical class (decided N ≥ 8; `vol_long`/`vol_short` folded into
`vol_term_dislocation` per the subject's own 2026-08-22 schema alias):**

| class | n | WR |
|---|---|---|
| earnings_vol | 144 | 32.6% |
| bearish_flow | 134 | 42.5% |
| multileg_directional | 97 | 40.2% |
| bullish_flow | 66 | 43.9% |
| dark_pool_accumulation | 59 | 40.7% |
| sector_rotation | 49 | 28.6% |
| dealer_positioning | 32 | 50.0% |
| high_iv_rank | 32 | 43.8% |
| oi_build | 21 | 42.9% |
| multi_day_sweep | 11 | 63.6% |
| **opex_pin** | 11 | **18.2%** ⚠ instrument artifact — 63.6% under settlement |
| gamma_breakout | 10 | 20.0% |
| event_vol | 10 | 40.0% |

## C3 — realised-P&L envelope fields (advisory)

| tier | n closed | expectancy | payoff ratio |
|---|---|---|---|
| HIGH | 7 | −2.441% | 0.720 |
| MEDIUM | 19 | +0.104% | 0.948 |
| LOW | 125 | −2.141% | 0.906 |
| DROP | 542 | −5.964% | 0.601 |
| **SIZED book** | **47** | **−2.618%** | 0.911 |

**Payoff ratio orders the tiers where hit rate does not** — a second cycle of the 08-22
observation, now with the DROP gap widened (0.601 vs 0.906–0.948). The "trades we refuse beat
the trades we take" reading from eight prior cycles rests on hit rate alone; on **expectancy**
DROP is the worst book by 3.8pp. Kelly gate handled in Phase 3.

## Outputs

- `phase_2_outcomes.jsonl` — 789 rows + `outcome`, `outcome_window`, `realised_return_pct`,
  `max_adverse_excursion_pct`, `inconclusive_reason`, `spy_benchmark_win`, `canonical_class`,
  `was_sized`, `realized_pnl_pct`, pin dual-rule fields.
- `phase_2b_vol_benchmark.json` — per-row SPY-RV vol benchmark (new).
