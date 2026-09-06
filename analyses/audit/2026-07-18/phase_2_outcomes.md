# Phase 2 — Outcome Resolution (2026-07-18)

**Win threshold (verbatim):** ≥ +1R move in thesis direction within the horizon window **without** a prior −1R drawdown, where R = 0.5 × true-range-ATR(14) at entry. **Path-aware** on **daily OHLC bars** (Yahoo chart API, real high/low; not the close-only MCP). A long is a LOSS the first bar whose `low` breaches `entry−R` before any bar's `high` reaches `entry+R`; symmetric for shorts. No daily OHLC ⇒ INCONCLUSIVE (`data_unavailable`), never LOSS. INCONCLUSIVE excluded from all WR denominators.

**Horizon→window:** 0DTE same-day · swing 10D(+3D) · weekly 10D(+5D) · LEAP 90D (held INCONCLUSIVE until window closes) · vol 10D (RV-direction proxy).

## Headline
**394 decided (168 WIN / 226 LOSS), 42.6% pooled WR.** INCONCLUSIVE 52 (window_open 36, leap_window_open 8, no_threshold 4, data_unavailable 4); NOT_A_TRADE 17 (directionless neutral).

| Cut | n | WR |
|---|---|---|
| SIZED book (full/half/quarter/starter) | 44 | **38.6%** |
| PAPER (dropped/watch, benchmarked) | 350 | 43.1% |
| long | 178 | 41.6% |
| short | 121 | 48.8% |
| vol_long | 20 | 80.0% |
| vol_short | 66 | 27.3% |

## Benchmark-excess (C21) — the edge column, and it REVERSED
| Direction | Book WR | SPY same-window base | **Excess** |
|---|---|---|---|
| long | 41.6% | 30.8% | **+10.8pp** |
| short | 48.8% | 55.9% | **−7.2pp** |

**This is the opposite sign to 07-11** (which read long/accumulation −29.2pp, short/bearish +29.4pp). The tape stopped rising, so the SPY-long path base collapsed 71%→31% and the SPY-short path base rose 18%→56%. Same rows, same windows, benchmark flipped. See Phase 3 for the class table and the non-stationarity read.

## By regime bucket (decided WR)
uptrend 46.4% (n153) · pullback_in_uptrend 44.4% (n117) · **choppy 31.2% (n16)** · transitional_other 37.0% (n108). Choppy is the worst tape.

## Empty-board discipline (6th+ straight confirmation)
**DROP pile 43.3% (122/282) > traded book 41.1% (46/112) > actually-sized 38.6% (17/44).** The names the system *sized* did worse than the names it *dropped*. Refusing to size the empty boards is graded-correct, not a miss.

## Post-freeze
247 decided; **0 HIGH, 0 MEDIUM**; book WR 40.9%, excess +3.6pp.

Outputs: `phase_2_outcomes.jsonl` (463 rows w/ `outcome`, `realised_return_pct`, `max_adverse_excursion_pct`, `spy_benchmark_win`, `realized_pnl_pct`, `was_sized`).
