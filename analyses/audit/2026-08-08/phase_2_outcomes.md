# Phase 2 — Outcome Resolution (2026-08-08)

## Definitions (restated verbatim, per skill)

> **WIN** = ≥ +1R move in thesis direction within the window **without** a −1R drawdown
> first, where **R = 0.5 × true-range ATR(14)** at entry (no structure-implied R is carried
> in the envelope). Path-aware: resolution walks **daily OHLC bars** and a long is a LOSS
> the first day `low` breaches `entry − R` *before* any day's `high` reaches `entry + R`.
> **INCONCLUSIVE** = window still open, no threshold touched in a complete window, or price
> data unavailable. INCONCLUSIVE rows are **excluded from all win-rate denominators.**

**Granularity (C20).** OHLC from the Yahoo **chart API** (`query1.finance.yahoo.com/v8`)
via stdlib `urllib` — *not* the `mcp__yahoo-finance__*` tools, which flatten to close-only
in this environment and cannot evaluate the path rule. Real `high`/`low` verified present;
SPY resolves through **2026-08-07** (close 773.26). `max_adverse_excursion_pct` is taken
from the daily extreme, not the daily close.

**Look-ahead (C22).** `uw historical signal-backtest` has no `--date` flag, so its rates
are **not** used as a point-in-time benchmark. The honest benchmark is the SPY same-window
same-direction path result (`spy_benchmark_win`), computed per row on the identical window
and ATR rule.

## Headline

| | n | WR |
|---|---|---|
| **Decided (WIN+LOSS)** | **542** | **40.8%** |
| WIN | 221 | |
| LOSS | 321 | |
| INCONCLUSIVE | 51 | |
| NOT_A_TRADE (directionless) | 33 | |

INCONCLUSIVE reasons: `window_open` 30, `leap_window_open` 11, `no_threshold` 5,
`data_unavailable` 5. Resolution modes: directional 437, vol 144, pin 9, not_a_trade 33.

Decided count is up from 501 (2026-08-01) to **542**; the +41 comes from prior windows
closing plus 18 decided rows in the post-P0 cohort.

## The result that matters

| Cut | n | WR |
|---|---|---|
| **SIZED book** | 47 | **42.6%** |
| **PAPER (unsized / DROP / watch_only)** | 495 | 40.6% |

For the first time in several cycles the sized book **edges out** the paper book (+2.0pp)
rather than trailing it. Do not over-read this: n=47 sized rows across an 11-week corpus,
and the gap is well inside noise. What it does say is that the long-running "the DROP pile
beats the traded book" embarrassment has narrowed — see Phase 3c for the tape-conditioned
version, where it persists in the down tape and reverses in the up tape.

## Direction and benchmark

| Direction | n | Book WR | SPY same-window base | Excess |
|---|---|---|---|---|
| long | 219 | 41.1% | 32.5% (n=231) | **+8.6pp** |
| short | 182 | 41.8% | 55.4% (n=186) | **−13.6pp** |
| vol_long | 31 | 58.1% | — | — |
| vol_short | 101 | 35.6% | — | — |

SPY benchmark resolved on 417 directional rows; blended base 42.7%.

> ⚠️ Per **C49**, these excess numbers are **secondary**. They are printed here because
> Phase 2 is where they are computed, not because they carry a finding. The primary edge
> test is the row-matched paired McNemar in Phase 3c.

## By regime bucket

| Bucket | n | WR |
|---|---|---|
| uptrend | 187 | 42.8% |
| pullback_in_uptrend | 119 | 43.7% |
| choppy | 70 | 38.6% |
| transitional_other | 166 | 37.3% |

Post-freeze decided **395**; out-of-regime decided **43**.

## Vol resolution caveat

All 144 vol rows resolve as `vol_resolution="rv_direction_proxy"` — realised-range ratio
vs the prior 14-bar mean range. The envelopes still do not carry a per-call `implied_move`
that would permit a true IV-vs-RV resolution, so **no vol row in this audit is a calibrated
IV-vs-RV outcome** and Phase 3 does not treat them as one. `vol_short` at 35.6% (n=101) is
the weakest large book in the corpus; `vol_long` at 58.1% (n=31) the strongest.

## C3 — realised-P&L envelope fields (advisory)

`realized_pnl_pct` is populated for every CLOSED directional/vol/pin call.
`payoff_ratio` / `expectancy_pct` / `kelly_fraction` are computed per class in Phase 3 and
remain **ADVISORY** — the live-activation gate is graded there and does not pass.

## Output

`phase_2_outcomes.jsonl` — 626 rows extended with `outcome`, `outcome_window`,
`realised_return_pct`, `max_adverse_excursion_pct`, `inconclusive_reason`,
`spy_benchmark_win`, `canonical_class`, `was_sized`, `realized_pnl_pct`.
