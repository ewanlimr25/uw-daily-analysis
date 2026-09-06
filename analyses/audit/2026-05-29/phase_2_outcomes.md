# Phase 2 — Outcome Resolution

## Method & data limitation (read first)

**Price source.** The skill specifies `uw historical trend` for price windows. That CLI tool was inspected and found to carry **options-flow metrics only** (volume, premium, IV-rank, P/C, daily `close`) — **no intraday high/low and no `--date` flag**. Both yfinance MCP endpoints (`get_stock_price_date_range`, `get_historical_stock_prices`) likewise return **close-only** series. Intraday range is therefore **unavailable from any tool in this environment**.

Consequence — outcomes are resolved **close-to-close, path-aware**: an adverse *closing* price hitting −1R before a favorable *closing* price hits +1R = LOSS. Intraday wicks are invisible (a stop that would have triggered intra-session but closed back inside the band is scored as not-triggered). This is a **faithful documented substitute**, not a silent extrapolation, and it biases toward *fewer* path-losses than a true intraday rule. **R = 0.5 × ATR_proxy**, where ATR_proxy = mean |closeₜ − closeₜ₋₁| over the 14 bars preceding entry (a close-range analogue of ATR(14), since true-range needs high/low).

**Windows (trading days after entry close).** 0DTE → next session (+1, abs-move vs R: pin/short-vol WINs if it *stays* within ±R, long-gamma WINs on a ≥R break). swing → 3D **and** 10D. weekly → 5D **and** 10D (entry = Friday close of the iso-week). LEAP → 30D **and** 90D. opex_pin → 5D abs-move vs R. vol_long/vol_short (swing/weekly) → 10D **realized-vol direction** proxy (no `implied_move` in legacy data, so true IV-vs-RV is impossible — WIN if realized σ moved the thesis way).

**Win threshold (verbatim):** *≥ +1R move in thesis direction within the window **without** −1R drawdown first.* Multi-window horizons require both windows to agree; disagreement = INCONCLUSIVE **unless the longer window is decisive**. An incomplete window (full N trading days not yet available) is `window_open`, never a truncated WIN/LOSS.

**Truth-set signal-class rates** (`uw historical signal-backtest`, current snapshot — the tool has no `--date`, so this is a "generally, what does this class do" rate, the best available proxy for "what *should* have been quoted"): bullish_flow **75.9 / 79.3 / 82.8%** (3/5/10D), bearish_flow **41.9%** (flat across windows), high_iv_rank vol-realisation **79.5 / 89.7%**, volume_spike **45.7 / 60.0%**, dark_pool_accumulation **N=0 (uncomputable)**. Saved to `_signal_backtest_truthset.json`.

## Headline results

| Bucket | Decided (W+L) | Win-rate |
|---|---|---|
| **All trades** | **328** | **47.3%** |
| Directional only (signed P&L) | 188 | **51.1%** |
| Daily reports | 275 | 45.8% |
| Weekly reports | 53 | 54.7% |
| 0DTE / pin (abs-move) | 28 | 39.3% |
| swing | 212 | 49.1% |
| weekly horizon | 87 | 44.8% |
| vol (realized-vol proxy) | 132 | 41.7% |
| LEAP | ~0 | n/a (all `window_open`) |

By thesis direction: **long 50.0%** (n=144) · **short 53.8%** (n=52) · **vol_long 53.1%** (n=64) · **vol_short 30.9%** (n=68).

**Directional expectancy (the nuance that rescues a coin-flip hit-rate):** on 188 signed directional calls, WR 51.1% but **mean WIN +2.86% vs mean LOSS −1.95%** → payoff ≈ **1.47**, **expectancy ≈ +0.50%/trade**. The book makes money on *asymmetry*, not on being right more than half the time.

## Resolution accounting

- **NOT_A_TRADE:** 157 (watch_only, leap_disqualified, DROP, and skip-sized rows — kept for the Phase 6 decision audit, **excluded from all win-rate denominators**).
- **INCONCLUSIVE:** 31 — 29 `window_open` (recent swings/weeklies + **all LEAPs**, whose 30/90D windows cannot complete by the 05-28 last bar) + 2 `no_threshold` (never reached ±1R).
- **WIN 155 / LOSS 173.**

## Desk read

1. **Short-vol / pin is the bleeding wound.** vol_short 30.9% and 0DTE/pin 39.3% — the premium-selling and pin trades lose ~2-in-3. Either R is mis-set for these (a 0.5×ATR band is too tight for a "stayed pinned" win) or the book is systematically short gamma into moves it doesn't see coming. Phase 4/5 must isolate whether this is a methodology artifact (tight R on the abs-move test) or a real edge problem. **Flag, do not yet indict.**
2. **Shorts beat longs in an UPTREND tape (53.8% vs 50.0%).** This echoes the 05-21 report's own flagged bull/bear win-rate inversion. The bearish_flow class is the desk's better directional read despite the regime — counter-intuitive and worth Phase 3 scrutiny.
3. **The hit-rate is a coin-flip; the *expectancy* is the story.** 51% directional WR with a 1.47 payoff is a real, if thin, edge. Any rubric that sizes on hit-rate alone (the current win-rate ladder) is sizing on the wrong axis — this is the central input to the Phase 3 C3 Kelly gate.
4. **LEAPs are unauditable on this dataset.** Earliest entry 04-27 + 30 trading days lands mid-June; nothing resolves. LEAP calibration is structurally deferred until ≥30 trading days of post-entry data exist (re-run after ~2026-06-15).

## Outputs

- `phase_2_outcomes.jsonl` — 516 rows = Phase 1 rows extended with `outcome`, `outcome_window`, `realised_return_pct`, `max_adverse_excursion_pct`, `window_detail[]`, `inconclusive_reason`, `entry_px`, `R_dollar`.
- `phase2_resolve.py`, `_signal_backtest_truthset.json`.
