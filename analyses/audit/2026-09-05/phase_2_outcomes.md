# Phase 2 — Outcome Resolution (2026-09-05)

## Definitions, restated verbatim (they govern every number downstream)

**WIN** = a ≥ +1R move in the thesis direction inside the window **without** a −1R drawdown
first, where **R = 0.5 × true-range ATR(14)** at entry (`max(high−low, |high−prev_close|,
|low−prev_close|)` averaged over the 14 bars *before* entry). Path-aware: the window is
walked bar-by-bar on **daily OHLC**, and a long is a LOSS the first bar whose `low` breaches
`entry − R` before any bar's `high` reaches `entry + R`. A +2% gain that arrived after a −1.5%
drawdown is a LOSS, because the report's own invalidation would have stopped it out first.

**INCONCLUSIVE** = window still open, no threshold touched in a completed window, no price
data, or a directionless (`neutral`) row. **INCONCLUSIVE is excluded from every win-rate
denominator downstream.** A data failure is never scored as a LOSS.

**Windows** — swing 10D (3D cross-check), weekly 10D/5D, vol 10D, LEAP 90D/30D, pin 5D.

## Instrument

Daily OHLC from the **Yahoo chart API** (`query1.finance.yahoo.com/v8/finance/chart`, stdlib
`urllib`), 2026-04-15 → 2026-09-05. **205 of 207 tickers** fetched with real high/low
(`real_ohlc: true`). The two failures are `BRKB` (needs `BRK-B`) and `SPX` (index, needs
`^GSPC`) — **1 row each, both tagged INCONCLUSIVE(`data_unavailable`), neither scored LOSS.**
The `mcp__yahoo-finance__*` tools are not used and cannot be: they flatten to close-only in
this environment and cannot evaluate the path rule (C20).

## Resolution

**878 rows → 296 WIN / 455 LOSS / 83 INCONCLUSIVE / 44 NOT_A_TRADE. Decided n = 751,
book WR = 39.4%.**

| inconclusive reason | n |
|---|---|
| window_open | 51 |
| directionless (`NOT_A_TRADE`) | 44 |
| leap_window_open | 15 |
| no_threshold | 12 |
| data_unavailable | **5** |

Modes: directional 585, vol 235, pin 11 (**C64 settlement rule — headline**), not_a_trade 44,
no price 3.

| cut | n | WR |
|---|---|---|
| SIZED (real risk) | 47 | 42.6% |
| PAPER (benched) | 704 | 39.2% |
| long | 287 | 42.5% |
| short | 233 | 39.9% |
| **vol_long** | 76 | **50.0%** |
| **vol_short** | 146 | **25.3%** |

By regime bucket: uptrend 40.1% (n=314), pullback 39.7% (179), choppy 38.4% (73),
transitional 38.4% (185). **The book is flat across all four regimes** — whatever it is doing,
it is not regime-sensitive.

SPY benchmark resolved on 556 directional rows, blended base 41.0%. Long book +9.3pp over
SPY-long; short book −10.9pp under SPY-short. Both are **secondary** columns (C49) — the
row-matched McNemar in Phase 3 is the finding, not these.

## C64 in force — the pin rule changed and old figures are not comparable

`opex_pin` now resolves on **settlement** (`|close_at_window_end − entry| < R`), with the
legacy touch rule retained as `outcome_touch`. 11 rows: **settlement 7/11 = 63.6%**, touch
2/11 = 18.2%. **Every `opex_pin` figure in the 2026-08-22 audit and earlier was computed under
TOUCH and is SUPERSEDED, not comparable** — do not chart them against this one.

## The vol lane — last cycle's P0, re-measured on +18 rows

Benchmark is the **unselected same-date single-name peer set** (`phase3f_peer_control.py`),
never SPY: for each entry date, the fraction of all single-name tickers whose forward
10-bar mean true range came in *below* their own trailing-14 mean. That is exactly the
resolver's own rule applied to the unselected population, so book and benchmark are the same
measurement on different samples. 63 of 73 entry dates have a complete peer window.

| arm | n | book WR | peer WR | excess |
|---|---|---|---|---|
| **`vol_short` ALL** | **129** | **0.287** | **0.581** | **−29.4pp** |
| `vol_long` ALL | 56 | 0.500 | 0.415 | **+8.5pp** |
| `vol_short` uptrend | 54 | 0.259 | 0.584 | −32.5pp |
| `vol_short` transitional | 40 | 0.325 | 0.572 | −24.7pp |
| `vol_short` pullback | 18 | 0.167 | 0.533 | −36.7pp |
| `vol_short` choppy | 17 | 0.412 | 0.640 | −22.8pp |

Last cycle measured −25.1pp on n=111. **On 18 more rows it is −29.4pp** — negative in 4 of 4
regime buckets, the sign unchanged, the magnitude larger. The P0 was not a window artifact.

**Caveat, stated not buried:** the vol resolver is an **RV-direction proxy**, not a true
IV-vs-RV settle. It prices *selection* — did the lane pick names that got calmer — never P&L.
A short-vol structure can still make money on a name whose range expands modestly.

## C63 — the live registration. **Cannot be graded this cycle, and that is the correct answer.**

C63's bar: post-change `vol_short` peer-excess ≥ −5pp on **n ≥ 40 decided across ≥ 2 regime
buckets**. Post-change (`report_date > 2026-08-30`) there are **15 `vol_short` rows in 5
sessions, 10 provisionally decided, all in one regime bucket (pullback), and none with a
complete forward window or a peer benchmark.** `n = 10 of 40`, `buckets = 1 of 2`. **NOT MET.**

The provisional read is `0 for 10`, consistent in sign with the P0 — but every one of those
rows is `window_complete: false`, so it is colour, not evidence. C63 stays open. Earliest
honest decision window: **2026-10-03**.

## What the post-change rows *do* decide: the P0 shipped and it works as designed

This is gradeable now, and it is clean.

| check | result |
|---|---|
| post-change `vol_short` rows routed to `watch_only` | **15 / 15 — zero violations** |
| post-change directional `short` rows routed to `watch_only` | **23 / 23 — zero violations** |
| `vol_short` share of the vol lane, pre-change | 138/203 = **68.0%** |
| `vol_short` share of the vol lane, post-change | 15/35 = **42.9%** |

Both P0s are **routing, not suppression**, and both are behaving that way: the lane still
generates 15 short-vol candidates in 5 sessions and still writes them down. Watch the
mirror-image failure — the share falling toward zero would mean the scouts learned to stop
proposing, which is the thing the agent files explicitly forbid.

## The finding this phase surfaces for Phase 3 to take apart

`vol_long` — the **only** lane in this corpus with a positive, peer-controlled, regime-robust
excess (+8.5pp, and **5-for-5 on every sized row it has ever had**) — produced **20 candidates
in the 5 post-change sessions and sized none of them.** All 20 are `tier: DROP`, every raw
score ≤ 2.

That is not the risk stack. Across the whole corpus, `vol_long` has a **maximum raw score of 4
on 85 rows** (median 1) and `vol_short` a maximum of 5 on 153 — **neither lane has ever
produced a single MEDIUM or HIGH call.** The directional lane, on the same rubric, reaches 12.
Phase 5 takes this up: it is an arithmetic property of the frozen rubric, not an outcome.
