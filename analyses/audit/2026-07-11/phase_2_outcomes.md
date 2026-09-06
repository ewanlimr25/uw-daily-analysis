# Phase 2 — Outcome Resolution (2026-07-11)

**Method (C20 path-aware).** Real daily OHLC pulled from the Yahoo **chart API** (`query1.finance.yahoo.com/v8/finance/chart`, stdlib `urllib`) — **all 129 unique tickers resolved, 0 fetch failures.** Entry = `close` on `report_date`; `R = 0.5 × true-range-ATR(14)` at entry; bar-by-bar path walk (a long is a LOSS the first day `low ≤ entry−R` *before* any day's `high ≥ entry+R`; symmetric for shorts). Windows: swing 3D∧10D→max10, weekly 5D∧10D→max10, LEAP 30D∧90D→max90. INCONCLUSIVE = no ±R hit in window OR forward window not yet available (recent calls). INCONCLUSIVE excluded from all denominators.

> **Chart-API note:** the `[[yahoo_chart_api_2025_anchored]]` "returns prior-year candles" memo is **stale/refuted** — the API returned correct 2026 OHLC for every ticker (SPY 07-10 close 754.95 matches the envelope regime spot exactly). It was a caller-side epoch bug, as the W28 dealer agent independently found for `^VIX`.

## Headline outcomes (non-DROP book)
| Cut | WIN | LOSS | INCONCL | WR |
|---|---|---|---|---|
| Non-DROP, all era | 43 | 63 | 9 | **0.406** |
| DROP (discipline check) | 123 | 135 | 23 | 0.477 |

**The book the system TRADED (non-DROP 0.406) won LESS often than the names it DROPPED (0.477).** Both are path-aware and strict; the read is not "the drops were good trades" but "there was no edge in the surfaced book above the discard pile" — which is exactly why the empty-board discipline (refuse to size) is graded-correct: dropping a 47.7% coin-flip pile costs nothing.

## Tier × era (WR, decided-N) — the tier-inversion evidence
| Era | HIGH | MEDIUM | LOW |
|---|---|---|---|
| 2026-05-15 | 0.500 (4) | 0.444 (9) | 0.526 (19) |
| 2026-05-30 | **0.000 (3)** | 0.455 (11) | 0.302 (43) |
| **2026-06-12 (FROZEN)** | **NA (0)** | **NA (0)** | 0.529 (17) |

## HIGH-tier composition (all 7 are PRE-freeze)
4 index/semis shorts (SMH×3, IWM) **0-for-4**, ORCL long −22.4% LOSS, AAPL & MSFT dark-pool longs path-WIN. Pooled HIGH = 2/7 = **0.286**. The frozen rubric has produced **zero** HIGH calls in a month.

Output: `phase_2_outcomes.jsonl` (396 rows + outcome/realised/MAE/spy_benchmark_win).
