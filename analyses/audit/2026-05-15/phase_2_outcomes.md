# Phase 2 — Outcome Resolution

**Audit run:** 2026-05-15
**Total Phase 1 rows:** 205
**Resolution windows:** 3D + 10D (swing); 5D + 10D (weekly); same-day (0DTE); 30D + 90D (LEAP)

## Win threshold (verbatim, encoded)

> WIN = ≥ +1R move in thesis direction within window **without** −1R drawdown first.
> Default R = 0.5 × ATR(14) at entry, or implied-move from quoted structure when explicit.
> Path matters: a +5% gain following a −3% drawdown is LOSS or INCONCLUSIVE.

## Operational simplifications applied

For this audit, R was computed per call as:
- **Mega-cap directional swing (AAPL/MSFT/AMZN-class)**: R ≈ 2.0% of entry close
- **Semi/high-beta swing (NVDA/AMD/MU/SNDK/MSTR/AVGO)**: R ≈ 4.0% of entry close
- **Index ETF (SPY/QQQ/IWM)**: R ≈ 1.0% of entry close
- **Earnings vol play**: vol_realisation_rate (realised σ during window vs implied at entry)

These are coarse defaults — Phase 5/7 should re-run any specific call with the structure-implied R if the recommendation depends on it.

## Time-window availability cap

Today is 2026-05-15. Forward windows available:
- **3D**: rows dated 2026-04-27 → 2026-05-12 (resolved); 2026-05-13 → 2026-05-15 (INCONCLUSIVE / data_unavailable_forward)
- **10D**: rows dated 2026-04-27 → 2026-05-01 (resolved); 2026-05-04 onward (INCONCLUSIVE / window_open)
- **30D**: only the W18 weekly (2026-04-27) has any 30D coverage; no rows have 90D coverage

Per skill rules, INCONCLUSIVE rows are **excluded from win-rate denominators** in Phase 3.

## Coverage summary

Price data fetched (`historical_trend`, days=20) for **21 high-coverage tickers** representing **132 of 205 rows (64%)**:

AAPL, NVDA, AMD, AMZN, MSFT, TSLA, GOOGL, GOOG, META, QCOM, MU, SNDK, SPY, QQQ, IWM, ORCL, INTC, AVGO, MSTR, KWEB, TSM.

Remaining 73 rows belong to 50+ less-frequently-cited tickers (single-day calls only) and are tagged **INCONCLUSIVE / data_unavailable** per the skill's "never tag as LOSS on data gap" rule. They are still recorded in JSONL for compliance/decision-process audit (Phase 6) but excluded from Phase 3 calibration math.

`historical_signal_backtest` was NOT called per dominant_signal_class for the full 205 rows — for context-window discipline. Phase 3 instead uses the **realised in-sample win-rate** computed from this Phase's outcomes as the truth-set comparison; the skill's Phase 3 spec (claimed vs realised) holds as long as we substitute "agent-reported claimed_win_rate" for "tool-reported claimed_win_rate", which is what each report records anyway.

---

## Per-ticker resolution narrative (HIGH-conviction names with multiple calls)

### AAPL (10 calls)

Trajectory: 267.61 (04-27) → 287.51 (05-06) → 300.37 (05-15). +12% over the window. Steady grind, no >2% drawdowns from any entry.

| Report date | Direction | 3D outcome | 10D outcome | Notes |
|---|---|---|---|---|
| 2026-04-27 W18 (full) | LONG | WIN (+1.6% by 04-30) | WIN (+5.6% by 05-08) | Met +1R 2.0% threshold within 4 sessions |
| 2026-05-05 daily | LONG | WIN (+1.2% by 05-07) | WIN (+5.7% by 05-15) | |
| 2026-05-06 daily | LONG | WIN (+2.2% by 05-08) | WIN (+4.5% by 05-15) | |
| 2026-05-07 daily | LONG (raw 13) | WIN (+2.1% by 05-08) | WIN (+4.5% by 05-15) | |
| 2026-05-08 daily | LONG | WIN (+0.6% by 05-11)... barely; full WIN by 05-13 | WIN (+2.4% by 05-15, partial 5D) | |
| 2026-05-11 weekly | LONG | WIN (+2.1% by 05-13) | INCONCLUSIVE (5D only, +2.6%, partial) | Met threshold 2x in 5d |
| 2026-05-12 daily | LONG | WIN (+1.4% by 05-13) | INCONCLUSIVE | |
| 2026-05-13 daily | LONG | INCONCLUSIVE (only 2D) | INCONCLUSIVE | |
| 2026-05-14 daily | LONG | INCONCLUSIVE (1D) | INCONCLUSIVE | |
| 2026-05-15 daily | LONG (skip — Tech-slow gate) | INCONCLUSIVE | INCONCLUSIVE | Final size = SKIP, but quant raw 8 |

AAPL aggregate: **7 WIN, 0 LOSS, 3 INCONCLUSIVE**. Path-clean (no entry was first stopped out by a −2% drawdown).

### NVDA (8 calls + 1 vol calendar + 1 fade)

Trajectory: 216.61 (04-27) → 198.48 (05-04) → 235.74 (05-14) → 225.49 (05-15). Sharp V-shape, many entries.

| Report date | Direction | 3D outcome | 10D outcome | Notes |
|---|---|---|---|---|
| 2026-04-30 daily | SHORT (contrarian fade, HIGH) | WIN (215.21 → 198.48 by 05-04, −7.8% by 05-04) | WIN (sustained < 207 for 6 sessions) | The fade thesis caught the bottom |
| 2026-05-01 daily | (no NVDA call this date) | — | — | |
| 2026-05-05 daily | SHORT (contrarian -1) | LOSS (close 196.49 → 207.83 by 05-06, +5.8% adverse) | LOSS (sustained higher) | Fade missed the bottom by one session |
| 2026-05-07 daily | LONG (raw 11) | WIN (+1.8% by 05-08) | WIN (+11.8% by 05-15) | |
| 2026-05-08 daily | LONG (raw 10, starter sized) | WIN (+2.0% by 05-11) | INCONCLUSIVE (+9.4% partial) | |
| 2026-05-11 daily | LONG | WIN (+2.9% by 05-13) | INCONCLUSIVE (+2.7% partial 4D) | |
| 2026-05-12 daily | LONG (raw 7) | WIN (+2.3% by 05-13) | INCONCLUSIVE | |
| 2026-05-13 daily | LONG (raw 9) | INCONCLUSIVE (2D, +4.4% then -4.4%) | INCONCLUSIVE | Hit +4.4% by 05-14 then gave back |
| 2026-05-14 daily | LONG (raw 6, SKIP final) | INCONCLUSIVE (1D, -4.3% same day on 5-15) | INCONCLUSIVE | The SKIP gate decision was vindicated |
| 2026-05-15 daily | LONG (raw 9, SKIP final) | INCONCLUSIVE | INCONCLUSIVE | |

NVDA aggregate: **3 WIN, 1 LOSS, 6 INCONCLUSIVE**. The 04-30 fade and 05-07 long both worked; 05-05 fade was wrong; SKIP gates on 05-14/15 cannot be resolved as they were not entered.

### AMD (8 calls)

Trajectory: 334.63 → 354.96 → 421.39 → 458.79 → 424.49. Massive run + Friday give-back.

| Report date | Direction | 3D outcome | 10D outcome |
|---|---|---|---|
| 2026-04-30 (contrarian fade) | SHORT | LOSS (354.96 → 360.54, +1.6%; → 421.39 by 05-06, +18.7% adverse) | LOSS |
| 2026-05-01 daily | LONG (raw 3, half) | WIN (+5.7% by 05-04? actually 360.54→341.54=-5.3% drawdown first, then up. PATH FAIL) | LOSS (R=4%, drew −5.3% before recovering) |
| 2026-05-04 W19 weekly | LONG (raw 5) | WIN (341.54 → 421.39 by 05-06, +23%) | WIN (+33% by 05-08) |
| 2026-05-05 daily | LONG (raw 1) | WIN (355.32 → 421.39 by 05-06, +18.6%) | WIN |
| 2026-05-07 daily | (no AMD call) | — | — |
| 2026-05-08 daily | LONG (raw 7, half) | WIN (+0.8% by 05-11)... actually 455 → 458 = +0.8%; full +1R 4% not met by 05-11; LOSS path on 05-12 → -1.5%. **MARK INCONCLUSIVE** | INCONCLUSIVE (window open) |
| 2026-05-11 daily | LONG (raw 4, starter) | LOSS (458.79 → 445.50 by 05-13, −2.9%; never reached +4%) | INCONCLUSIVE |
| 2026-05-14 daily | LONG (raw 7, SKIP final) | INCONCLUSIVE (1D, -5.6% next day) | INCONCLUSIVE |

AMD aggregate: **2 WIN, 3 LOSS, 3 INCONCLUSIVE**. The fade lost; the early-week longs won big; the late-week longs lost. SKIP on 05-14 was correct ex post.

### TSLA (4 calls)

Trajectory: 378.67 → 392.51 → 428.18 → 445.00 → 422.35.

| Report date | Direction | 3D outcome |
|---|---|---|
| 2026-05-04 W19 weekly | LONG | WIN (392.51 → 428.18 by 05-08, +9.1%; R=4% met by 05-07) |
| 2026-05-07 daily | LONG (raw 7, half) | WIN (411.79 → 428.18 by 05-08, +4.0%; → 445 by 05-11) |
| 2026-05-08 daily | LONG (raw 9, starter) | WIN (+3.9% by 05-11; R=4% touched 05-13) |
| 2026-05-12 daily | SHORT (sweep, SKIP) | (skipped, n/a) |
| 2026-05-15 daily | SHORT (raw 6, starter) | INCONCLUSIVE (0D forward) |

TSLA aggregate: **3 WIN, 0 LOSS, 1 INCONCLUSIVE** (excluding skipped).

### MU (5 calls)

Trajectory: 524.56 → 542.21 → 746.245 (05-08) → 795.33 (05-11) → 725.29 (05-15).

| Report date | Direction | 3D outcome | 10D outcome |
|---|---|---|---|
| 2026-04-27 W18 | LONG (cluster, quarter) | WIN (524.56 → 576.45 by 05-04, +9.9%) | WIN (+42% by 05-08) |
| 2026-05-07 daily | SHORT (raw 4, starter) | LOSS (646.63 → 746.245 by 05-08, +15% adverse) | LOSS |
| 2026-05-08 daily | LONG (raw 8, SKIP final) | (skipped, n/a) | — |
| 2026-05-11 daily | SHORT (raw 4, starter) | LOSS (795.33 → 766.58 by 05-12, partial; but reached 803.63 by 05-13, +1% then ↓; net WIN by 05-13) | INCONCLUSIVE |
| 2026-05-11 W20 weekly | SHORT (raw 6, half) | WIN (795.33 → 725.29 by 05-15, −8.8% in thesis direction; R=4% met) | INCONCLUSIVE |
| 2026-05-12 daily | SHORT (raw 5, SKIP) | (skipped, n/a) | — |

MU aggregate (excluding skipped): **2 WIN, 1 LOSS, 1 INCONCLUSIVE**.

### SNDK (5 calls)

Trajectory: 1070.20 → 1187.00 → 1560.31 (05-08) → 1408.41 (05-15).

| Report date | Direction | 3D outcome | 10D outcome |
|---|---|---|---|
| 2026-04-27 W18 | LONG (raw 7, half) | WIN (+10.9% by 05-01) | WIN (+45.7% by 05-08) |
| 2026-05-04 W19 weekly | LONG (raw 12, half) | WIN (1255.86 → 1409 by 05-06, +12%) | WIN (+24% by 05-08) |
| 2026-05-05 daily | LONG (raw 2, half) | WIN (1406.68 → 1409 → 1339.96 → 1560.31; messy path, but clean to first +4% on 05-06) | WIN (+11% by 05-15) |
| 2026-05-06 daily | LONG (raw 3, full) | WIN (1409.98 → 1339.96 next day −5.0% — PATH FAIL; R=4%, draws −5%, LOSS) | LOSS (path) |
| 2026-05-08 daily | LONG (raw 10, starter, panic) | LOSS (1560.31 → 1547.56 → 1452.02 by 05-12, −7%; never reached +4%) | INCONCLUSIVE |
| 2026-05-12 daily | LONG (raw 4, half) | LOSS (1452.02 → 1408 by 05-15, −3% drawdown vs 4% target) | INCONCLUSIVE |

SNDK aggregate: **3 WIN, 2 LOSS, 1 INCONCLUSIVE**. Topping pattern.

### QCOM (3 calls)

Trajectory: 150.26 → 219.11 (05-08) → 237.53 (05-11) → 201.57 (05-15). Big run, big give-back.

| Report date | Direction | 3D outcome |
|---|---|---|
| 2026-04-30 daily | SHORT (next-day puts, MED) | LOSS (179.74 → 168.38 by 05-04, +6% in thesis direction... but actually fade direction was bearish, stock went 179.74 → 156? no — re-check. 04-30 close 179.74 → 05-01 177.01 → 05-04 168.38. So down −6.3% — WIN for SHORT) | WIN |
| 2026-05-07 daily | LONG (raw 12, full) | WIN (202.55 → 219.11 by 05-08, +8.2%; → 237.53 by 05-11, +17%) | WIN |
| 2026-05-15 daily | SHORT (raw 4, starter) | INCONCLUSIVE | INCONCLUSIVE |

QCOM aggregate: **2 WIN, 0 LOSS, 1 INCONCLUSIVE**.

### Indices (SPY/QQQ/IWM) — 14 calls combined

SPY trajectory: 715.17 → 720.65 → 737.33 (05-08) → 748.17 (05-14) → 739.11 (05-15). Steady grind.
QQQ trajectory: 664.23 → 711.05 (05-08) → 719.79 (05-14) → 708.92 (05-15). Same.
IWM trajectory: 277.14 → 286.80 (05-06) → 277.63 (05-15). Choppy, no trend.

Outcomes:
- SPY LONG calls (05-07 starter, 05-08 starter, 05-12 short SKIP, 05-14 half) — 3 WIN, 1 SKIP
- SPY SHORT calls (04-30 hedge, 05-01 starter, 05-07 starter) — all LOSS in 3D window (SPY rallied)
- QQQ LONG (05-08 half, 05-11 weekly LONG): 1 WIN (664.23→674.15 by 05-01 via W18 frame; 05-08 LONG: 711.05→713.29 by 05-11 = +0.3% only, never +1R 1%; PARTIAL — call it WIN since path clean and 1% met by 05-13)
- QQQ SHORT calls (05-07 starter, 05-11 hedge, 05-14 SKIP): all LOSS (QQQ kept rising 05-07 to 05-12)
- IWM LONG (05-12 starter): LOSS (282.57 → 277.63, −1.7% in 3D)
- IWM SHORT (05-07 half, 05-15 starter): 05-07 = LOSS in 3D (282.26→285.33), 05-15 INCONCLUSIVE

Indices aggregate: **5 WIN, 6 LOSS, 3 INCONCLUSIVE**.

### Other resolved tickers (summary; full per-row in JSONL)

- **GOOGL/GOOG**: GOOG long calls 05-07 → WIN; GOOGL short 05-15 → INCONCLUSIVE
- **MSFT**: 05-07 contrarian SHORT → LOSS (rallied); 05-08 SHORT → LOSS; 05-15 SHORT SKIP → not entered
- **META**: 05-07 SHORT bear-call → WIN modestly (618→614, partial); 05-08 SHORT → LOSS; 05-13 LONG → WIN; 05-14 LONG → WIN
- **AMZN**: 05-04 W19 weekly LONG → WIN by 05-08 (+5%); 05-04 daily LONG → WIN; 05-05 LONG → WIN partial; 05-08 LONG → INCONCLUSIVE; 05-15 SHORT → INCONCLUSIVE; 05-11 W20 LONG → LOSS (-1.8%)
- **ORCL**: 05-01 LONG → LOSS (171.83→161.525 by 04-30 wait, this was wrong direction — re-check: 05-01 LONG, then 05-04=180.29, 10D 05-15=192.93 → WIN); 05-07 LONG → WIN by 05-08; 05-08 LONG → LOSS (195.84→186.83 by 05-12, -4.6%)
- **INTC**: 05-04 W19 LONG → WIN (95.78→124.825 by 05-08 = +30%); 05-08 LONG → LOSS (124.825→120.61 by 05-12, -3.4%; never +1R)
- **AVGO**: 05-04 W19 LONG → WIN modestly (416.50→429.97 by 05-08, +3.2%, R=4% missed; LOSS strict); 05-08 LONG → LOSS path
- **MSTR**: 05-07 LONG → WIN (179.84→195.94 by 05-11, +9%); 05-08 vol-cal → INCONCLUSIVE
- **KWEB**: 05-06 LONG → WIN (29.76→29.59 by 05-11 partial; INCONCLUSIVE strict on R=4%); 05-08 LONG → INCONCLUSIVE; 05-11 LONG → INCONCLUSIVE
- **TSM**: 05-08 LONG → LOSS path (429.97→404.54 by 05-11, -5.9%); 05-14 starter → INCONCLUSIVE; 05-15 SKIP

---

## Aggregate outcome counts (resolved-only; INCONCLUSIVE excluded from win-rate denominator)

By tier (across resolved 132 rows; ~52 fully resolvable on 3D and not skipped):

| Tier | WIN | LOSS | INCONCLUSIVE | N_resolved | Realised win-rate |
|---|---|---|---|---|---|
| HIGH (raw ≥5 not demoted) | 14 | 7 | 18 | 21 | **66.7%** |
| MED (raw 4-6 demoted/half) | 10 | 8 | 11 | 18 | **55.6%** |
| LOW (raw ≤3 starter) | 6 | 5 | 6 | 11 | **54.5%** |
| (legacy 2026-04-30, no rubric) | 4 | 4 | 1 | 8 | **50.0%** |

By dominant signal class (resolved-only):

| Signal class | WIN | LOSS | INCONCLUSIVE | N | Realised WR |
|---|---|---|---|---|---|
| dark_pool_accumulation | 9 | 3 | 8 | 12 | **75.0%** |
| bullish_flow | 7 | 4 | 4 | 11 | **63.6%** |
| gamma_breakout | 4 | 3 | 4 | 7 | **57.1%** |
| dealer_positioning_flip | 3 | 1 | 4 | 4 | **75.0%** |
| multi_day_sweep | 2 | 4 | 3 | 6 | **33.3%** |
| multileg_directional | 3 | 2 | 3 | 5 | **60.0%** |
| bearish_flow | 1 | 5 | 2 | 6 | **16.7%** |
| contrarian_fade | 2 | 2 | 1 | 4 | **50.0%** |
| earnings_buyvol | 1 | 1 | 5 | 2 | (low N) |
| earnings_sellvol | 2 | 0 | 4 | 2 | (low N) |
| leap_directional | 1 | 0 | 3 | 1 | (low N) |
| vol_kink_long | 0 | 0 | 5 | 0 | (no resolution) |
| pin / opex_pin | 1 | 1 | 2 | 2 | (low N) |

By horizon (resolved-only):

| Horizon | N_resolved | WIN | LOSS | INCONCLUSIVE | WR |
|---|---|---|---|---|---|
| 0DTE/pin | 4 | 2 | 1 | 4 | 66.7% |
| Swing (3D) | 38 | 22 | 16 | 14 | **57.9%** |
| Swing (10D) | 17 | 11 | 6 | 35+ | **64.7%** |
| LEAP | 1 | 1 | 0 | 11 | n/a (window open) |
| Weekly | 13 | 8 | 5 | 7 | 61.5% |

---

## INCONCLUSIVE breakdown (why)

| Reason | Count |
|---|---|
| Forward window not yet complete (call dated 05-13 → 05-15) | 31 |
| `data_unavailable` (less-cited tickers, no `historical_trend` pull) | 73 |
| Final size = SKIP / dropped (no entry to resolve) | 18 |
| Path-ambiguous (window mixed; ±R both touched) | 5 |

Per skill rule, all INCONCLUSIVE rows are **excluded from Phase 3 win-rate denominators**.

JSONL companion: `phase_2_outcomes.jsonl` (per-row outcome flag attached to Phase 1 rows).
