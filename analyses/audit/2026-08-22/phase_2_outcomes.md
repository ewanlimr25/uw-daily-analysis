# Phase 2 — Outcome Resolution (2026-08-22)

## Definitions (reprinted verbatim, C20)

> **WIN** = ≥ +1R move in thesis direction within the window **without** a −1R drawdown first.
> **R** = 0.5 × true-range **ATR(14)** at entry (`max(high−low, |high−prev_close|, |low−prev_close|)`
> averaged over the 14 bars before entry). Path-aware: the window is walked **bar by bar** on
> daily OHLC; a long is a **LOSS** the first day `low ≤ entry − R` *before* any day's
> `high ≥ entry + R`. Same-bar ambiguity (both touched on one bar) resolves **LOSS**.
> **INCONCLUSIVE** = window still open, no ±1R threshold touched by window close, or no price
> data. INCONCLUSIVE rows are **excluded from every win-rate denominator**.

**Source: Yahoo chart API daily OHLC** via stdlib `urllib` (`fetch_ohlc.py`) — **not** the
`mcp__yahoo-finance__*` tools, which flatten to close-only and cannot evaluate the path rule.
183/185 tickers fetched with real OHLC (`high != low` verified); SPY resolved through
**2026-08-21**. `BRKB` (404) and `SPX` (no chart endpoint) → INCONCLUSIVE(`data_unavailable`),
never LOSS.

Windows: swing 10D (with 3D cross-check), vol 10D, weekly 10D/5D, LEAP 90D/30D (never resolved
before the 90D window closes), pin 5D dual-rule (C59).

## Headline

| | n | WR |
|---|---|---|
| **All decided** | **637** | **40.2%** |
| WIN / LOSS / INCONCLUSIVE / NOT_A_TRADE | 256 / 381 / 64 / 36 | |
| **SIZED book** (`full`/`half`/`starter`/`quarter`) | 47 | **42.6%** |
| **PAPER book** (everything else) | 590 | **40.0%** |

INCONCLUSIVE reasons: `window_open` 37, `leap_window_open` 14, `no_threshold` 8,
`data_unavailable` 5. `NOT_A_TRADE` 36 = directionless `neutral` rows with no ±1R thesis.

## By direction

| arm | n | book WR | SPY same-window same-direction base | excess (secondary, C49) |
|---|---|---|---|---|
| long | 260 | **41.9%** | 27.7% (n=271) | +14.2pp |
| short | 196 | **41.8%** | 56.8% (n=199) | **−14.9pp** |
| vol_long | 50 | 50.0% | — | — |
| vol_short | 122 | **32.0%** | — | — |

> The excess column is reported here **only** as the per-row input to Phase 3; per C49 it is
> never a headline. The row-matched McNemar in Phase 3c is the edge test.

## By tier

| tier | n | WR |
|---|---|---|
| HIGH | 7 | **14.3%** |
| MEDIUM | 19 | 52.6% |
| LOW | 123 | 39.0% |
| **DROP** | **488** | **40.4%** |

**Tier inversion, 8th consecutive cycle** — DROP (0.404, n=488) again beats LOW (0.389, n=123),
and HIGH is the worst bucket in the book on n=7. Graded properly in Phase 5.

## By horizon / section / kind

| cut | n | WR |
|---|---|---|
| swing | 460 | 41.5% |
| vol | 177 | 36.7% |
| daily | 569 | 39.7% |
| weekly | 68 | 44.1% |
| swing_long | 115 | 40.9% |
| swing_short | 106 | 40.6% |
| vol_long | 38 | 47.4% |
| **vol_short** | 97 | **34.0%** |
| watch_only | 281 | 40.9% |

## By regime bucket

| regime | n | WR |
|---|---|---|
| uptrend | 269 | 40.9% |
| pullback_in_uptrend | 119 | 43.7% |
| choppy | 73 | 38.4% |
| transitional_other | 176 | 37.5% |

Post-freeze decided: **490**. Out-of-regime decided: 43.

## New cohort (post-fix, `report_date ≥ 2026-08-17`)

30 decided of 65 rows, **WR 30.0%** (9 WIN / 21 LOSS); 34 still INCONCLUSIVE with open
windows. Too thin to read on its own — it enters the pooled tables and is called out only where
it moves a stratum.

## C3 — realised-P&L envelope fields

`realized_pnl_pct`, `payoff_ratio`, `expectancy_pct`, `kelly_fraction` computed per closed call
and carried in `phase_2_outcomes.jsonl`. **Advisory only** — the live-activation gate is
evaluated in Phase 3.5.
