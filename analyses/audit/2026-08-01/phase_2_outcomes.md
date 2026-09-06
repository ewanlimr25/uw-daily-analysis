# Phase 2 — Outcome Resolution (2026-08-01)

## Definitions (reprinted verbatim, per skill)

> **WIN** — ≥ +1R move in thesis direction within the window **without** a −1R drawdown
> first, where R = the structure-implied risk, defaulting to **0.5 × ATR(14)** at entry.
> ATR is **true range** — `max(high−low, |high−prev_close|, |low−prev_close|)` — averaged
> over the 14 bars before entry.

> **Path-aware (C20).** A long is a LOSS the first bar whose `low` breaches `entry − R`
> *before* any bar's `high` reaches `entry + R`. Symmetric for a short. A +2% gain that
> arrived after a −1.5% drawdown is a LOSS, because the report's own invalidation rule
> would have stopped it out first.

> **INCONCLUSIVE** — window still open, no directional threshold, or no price data.
> Excluded from every win-rate denominator downstream. **A data failure is never a LOSS.**

Resolution substrate: **Yahoo chart API daily OHLC** (`query1.finance.yahoo.com/v8`,
stdlib `urllib`), 158/160 tickers fetched, real high/low verified. The
`mcp__yahoo-finance__*` tools are close-only in this environment and cannot evaluate the
path rule — not used. SPY reference bar 2026-07-31 close **747.03**.

Windows: swing 10D (3D cross-check), weekly 10D/5D, LEAP 90D/30D, vol 10D RV-proxy.

## Headline

| | |
|---|---|
| Rows | 578 |
| **Decided (WIN+LOSS)** | **501** |
| WIN / LOSS | 218 / 283 |
| **Book win rate** | **43.5%** |
| INCONCLUSIVE | 50 |
| NOT_A_TRADE | 27 |

INCONCLUSIVE reasons: window_open 30, leap_window_open 10, no_threshold 5,
data_unavailable 5. (`directionless` 27 rows are classed NOT_A_TRADE.)
Resolution modes: directional 413, vol 126, pin 9, not_a_trade 27, no_px 2, no_entry_bar 1.

Decided N is up from **440** at 2026-07-25 → **501** (+61).

## By book slice

| Slice | n | WR |
|---|---|---|
| SIZED (full/half/quarter/starter) | 47 | 42.6% |
| PAPER (benched) | 454 | 43.6% |
| long | 207 | 41.5% |
| short | 164 | 46.3% |
| vol_long | 25 | 72.0% |
| vol_short | 96 | 38.5% |

**The sized book again fails to beat the bench** — 42.6% vs 43.6%. Seventh consecutive
audit in which the names the fleet actually sized did no better than the ones it passed on.

## By regime bucket

| Regime | n | WR |
|---|---|---|
| uptrend | 165 | 46.7% |
| pullback_in_uptrend | 117 | 44.4% |
| choppy | 64 | 43.8% |
| transitional_other | 155 | 39.4% |

Post-freeze decided: **354**. Out-of-regime decided: **43** (past the C24 actionable floor).

## C21 benchmark inputs (secondary — see Phase 3c for the primary test)

SPY same-window same-direction benchmark resolved on **390** directional rows;
blended base 42.3%.

- SPY-long base **28.4%** (n=218) vs book-long 41.5% → +13.1pp
- SPY-short base **59.9%** (n=172) vs book-short 46.3% → −13.5pp

These raw excess figures are **not** findings on their own (C49). They are the per-row
inputs to the paired McNemar test in Phase 3c, which is where the edge claim is decided.

## C3 — realised-P&L envelope fields (advisory)

`realized_pnl_pct`, `payoff_ratio`, `expectancy_pct`, `kelly_fraction` computed for all
closed calls and carried in the JSONL. Still **advisory** — see the Phase 3 Kelly gate,
which returns `ADVISORY_ONLY`.

Output: `phase_2_outcomes.jsonl`, `_ohlc/` (158 symbols), `phase2_resolve.py`.
