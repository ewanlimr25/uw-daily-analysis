# Phase 2 — Outcome Resolution (2026-08-15)

## Definitions (reprinted verbatim, per skill requirement)

**Win threshold.** ≥ +1R move in the thesis direction within the window **without** a −1R
drawdown first, where R = **0.5 × ATR(14)** computed as **true range**
(`max(high−low, |high−prev_close|, |low−prev_close|)`) over the 14 bars preceding entry.
Resolution is **path-aware on daily OHLC bars** (C20): the window is walked bar-by-bar and a
long is a LOSS the first day `low` breaches `entry − R` *before* any day's `high` reaches
`entry + R`. `max_adverse_excursion_pct` is taken from the daily extreme, never the close.

**INCONCLUSIVE** — one of: `window_open` (forward window has not closed), `no_threshold`
(window closed without touching ±1R), `data_unavailable` (no OHLC), `leap_window_open`
(LEAP is never resolved before its 90D window closes), `directionless` (`NOT_A_TRADE`).
INCONCLUSIVE rows are **excluded from every win-rate denominator downstream.**

**Horizon→window:** swing 10D (3D carried as `outcome_3d`) · vol 10D · weekly 10D/5D ·
LEAP 90D/30D · opex_pin 5D (pin resolves on ±1R *breach* = LOSS).

**Data source.** Yahoo chart API daily bars via stdlib `urllib` (`_ohlc/`). The
`mcp__yahoo-finance__*` tools are close-only in this environment and **cannot** evaluate the
path rule — not used. `uw historical trend` is **not** a price-window tool (no `--date`, no
high/low) — not used for resolution.

## Headline

| | n | WIN | LOSS | WR |
|---|---|---|---|---|
| **All decided** | **572** | 237 | 335 | **41.4%** |

672 rows → 572 decided, 65 INCONCLUSIVE, 35 NOT_A_TRADE. Resolution modes: directional 471 ·
vol 154 · pin 9 · not_a_trade 35 · no-price 3.

INCONCLUSIVE decomposition: `window_open` 43 (all `report_date ≥ 2026-08-03` — the forward
window has genuinely not closed), `leap_window_open` 11, `no_threshold` 6,
`data_unavailable` **5** (`BRKB`, `SPX` and 3 rows with no entry bar — tagged, never LOSS).

Only **4 of 572** decided rows hit both thresholds on the same bar (`ambiguous_bar`), all
resolved conservatively as LOSS.

## By tier — the inversion, 7th consecutive cycle

| tier | n | WIN | WR |
|---|---|---|---|
| HIGH | 7 | 1 | **14.3%** |
| MEDIUM | 19 | 10 | **52.6%** |
| LOW | 108 | 42 | 38.9% |
| DROP | 438 | 184 | **42.0%** |

Required order is HIGH > MEDIUM > LOW. Realised order is **MEDIUM > DROP > LOW > HIGH**.
The names the fleet refuses (DROP, 42.0%) again beat the names it sizes into LOW (38.9%),
and HIGH remains the worst bucket in the book. All 7 HIGH and 19 MEDIUM decided rows are
**pre-freeze** — the frozen rubric has produced none of either (Phase 5).

## By horizon / section

| | n | WR |
|---|---|---|
| swing | 426 | 42.0% |
| vol | 146 | 39.7% |
| swing_long | 94 | 44.7% |
| swing_short | 99 | 39.4% |
| vol_long | 27 | 55.6% |
| vol_short | 80 | 40.0% |
| watch_only | 272 | 40.1% |

## By direction, with the C21 SPY benchmark

SPY benchmark resolved on **417** directional rows (same entry date, same direction, same
window, same ±1R rule). Blended base 42.7%.

| | book WR | n | SPY same-window base | excess |
|---|---|---|---|---|
| long | 43.3% | 233 | 32.5% (n=231) | **+10.9pp** |
| short | 41.3% | 189 | 55.4% (n=186) | **−14.1pp** |
| vol_long | 54.1% | 37 | — | — |
| vol_short | 35.6% | 104 | — | — |

⚠️ **These excess figures are NOT the edge finding** (C49). They are printed here as Phase-2
inputs only; the primary edge test is the tape-conditioned book WR + row-matched paired
McNemar in Phase 3. This window is a rising tape (39 of 46 new rows are `uptrend`), which
mechanically depresses `SPY-short` base and inflates the short deficit.

## Sized vs paper

| | n | WR |
|---|---|---|
| SIZED (`full/half/quarter/starter`) | 47 | 42.6% |
| PAPER (watch_only / skip / veto — counterfactual preserved) | 525 | 41.3% |

The sized book is +1.3pp over the paper book on n=47 — the first cycle where sized ≥ paper on
the blended number, but far inside noise. Tape-split in Phase 3.

## By regime bucket (cross-regime confirmation)

| bucket | n | WR |
|---|---|---|
| uptrend | 210 | 44.3% |
| pullback_in_uptrend | 119 | 43.7% |
| choppy | 73 | 38.4% |
| transitional_other | 170 | 37.6% |

**425 post-freeze decided** · **43 out-of-regime decided**. Four populated regime buckets:
this is a genuinely cross-regime dataset for the 4th consecutive cycle.

## By canonical signal class (decided n ≥ 8; fragmented labels collapsed)

| class | n | WR |
|---|---|---|
| bearish_flow | 120 | 45.8% |
| earnings_vol | 109 | 39.4% |
| multileg_directional | 80 | 37.5% |
| bullish_flow | 57 | 42.1% |
| dark_pool_accumulation | 53 | 43.4% |
| sector_rotation | 39 | **28.2%** |
| dealer_positioning | 28 | 53.6% |
| high_iv_rank | 27 | 48.1% |
| oi_build | 13 | 46.2% |
| multi_day_sweep | 11 | 63.6% |
| gamma_breakout | 10 | 20.0% |
| opex_pin | 9 | **11.1%** |
| event_vol | 8 | 50.0% |

## C3 — realised-P&L envelope fields (advisory)

`realized_pnl_pct` written for every decided directional/vol/pin row. Mean by tier:

| tier | n | mean realised P&L |
|---|---|---|
| HIGH | 7 | −2.441% |
| MEDIUM | 19 | **+0.104%** |
| LOW | 108 | −1.963% |
| DROP | 438 | −2.870% |

Tier × expectancy is **not monotone** (MEDIUM > HIGH). `payoff_ratio` / `expectancy_pct` /
`kelly_fraction` computed per class in Phase 3; the live-activation gate is graded there.

**Output:** `phase_2_outcomes.jsonl` — 672 rows carrying `outcome`, `outcome_window`/`nwin`,
`realised_return_pct`, `max_adverse_excursion_pct`, `inconclusive_reason`, `spy_benchmark_win`,
`canonical_class`, `was_sized`, `realized_pnl_pct`, `outcome_3d`, `fast_trigger`.
