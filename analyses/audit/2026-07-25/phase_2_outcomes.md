# Phase 2 — Outcome Resolution (2026-07-25)

## Definitions (restated verbatim, per skill)

> **WIN** = ≥ +1R move in the thesis direction within the window **without** a −1R
> drawdown first, where **R = 0.5 × true-range ATR(14)** at entry. Path-aware, resolved
> **bar-by-bar on daily OHLC** from the Yahoo chart API (`query1.finance.yahoo.com/v8/finance/chart`).
> A long is a LOSS the first day `low` breaches `entry − R` *before* any day's `high`
> reaches `entry + R`. Symmetric for a short.
>
> **INCONCLUSIVE** = window still open, window closed without either threshold touched,
> LEAP 90D window not yet closed, or price data unavailable. **Excluded from all
> win-rate denominators.** A missing price series is *never* scored a LOSS.

Windows: 0DTE same-day · swing 10D (3D carried) · weekly 10D · LEAP 90D · vol 10D.
Vol rows resolve on **RV direction only** (`vol_resolution="rv_direction_proxy"`) — the
legacy envelopes carry no `implied_move`, so these are **not** calibrated IV-vs-RV outcomes.

## Resolution

| | |
|---|---|
| Rows | 526 |
| **Decided (WIN+LOSS)** | **440** — 187 WIN / 253 LOSS = **42.5%** |
| INCONCLUSIVE | 64 (window_open 47, leap_window_open 9, data_unavailable 5, no_threshold 3) |
| NOT_A_TRADE (directionless) | 22 |
| OHLC coverage | **153 / 155 tickers** (BRKB → ticker-format miss; SPX → index, no chart series) |

## Book cuts

| Cut | n | WR |
|---|---|---|
| SIZED (full/half/quarter/starter) | 46 | 41.3% |
| PAPER (benched) | 394 | 42.6% |
| long | 189 | 41.3% |
| short | 140 | 44.3% |
| vol_long | 21 | 66.7% |
| vol_short | 81 | 39.5% |

## C21 benchmark (per-row `spy_benchmark_win`)

Resolved on 336 directional rows.

| | book | SPY same-window same-direction | excess |
|---|---|---|---|
| long | 41.3% (n=201) | **28.9%** | **+12.4pp** |
| short | 44.3% (n=135) | **54.1%** | **−9.8pp** |

**The tape turned.** For the first time in the audit series the SPY *short* base rate
(54.1%) exceeds the SPY *long* base rate (28.9%) — the resolution windows now contain a
genuinely falling tape. This is the regime every audit since 2026-06-27 has been
waiting for. Phase 3c runs the experiment properly; Phase 3d shows why the excess
column itself must be read with care.

## By regime label

| bucket | n | WR |
|---|---|---|
| uptrend | 160 | 46.2% |
| pullback_in_uptrend | 117 | 44.4% |
| transitional_other | 122 | 38.5% |
| choppy | 41 | 34.1% |

Post-freeze decided **293**; out-of-regime decided **41** (now well past the C24 n≥10
actionable floor).

## C3 — realised-P&L envelope fields

`realized_pnl_pct` populated on every decided directional/vol/pin row; `payoff_ratio`,
`expectancy_pct` and `capped_half_kelly` computed per tier in Phase 3. Still **ADVISORY** —
the live-activation gate is graded there.

Outputs: `phase_2_outcomes.jsonl` (526 rows, Phase-1 fields + outcome/MAE/R/benchmark).
