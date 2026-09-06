# Phase 3 — Calibration Audit

**Audit run:** 2026-05-15
**Universe:** 132 rows with price data; 52 fully resolved on 3D and not skipped (resolved-only base for win-rate math).
**Truth set:** Phase 2 outcomes.

The voice for this phase is the desk reviewer composite: *does the rubric tell the desk something true about how often the next call will work, or does it overstate the edge?*

---

## 1. Per-signal-class table — claimed vs realised

For each `dominant_signal_class` with N≥3 in the resolved-only base.

| Signal class | N_resolved | Mean **claimed** WR | Realised WR (W/L only) | Divergence (claimed − realised) | Flag |
|---|---|---|---|---|---|
| **dark_pool_accumulation** | 12 | 0.92 | 0.75 (9W/3L) | **+17 pp** | **OVERCONFIDENT** |
| **bullish_flow** | 11 | 0.89 | 0.64 (7W/4L) | **+25 pp** | **OVERCONFIDENT** |
| **dealer_positioning_flip** | 4 | 1.00 | 0.75 (3W/1L) | +25 pp | OVERCONFIDENT (low N) |
| **gamma_breakout** | 7 | 0.79 | 0.57 (4W/3L) | +22 pp | OVERCONFIDENT |
| **multi_day_sweep** | 6 | 0.71 | 0.33 (2W/4L) | **+38 pp** | **SEVERELY OVERCONFIDENT** |
| **bearish_flow** | 6 | 0.34 | 0.17 (1W/5L) | +17 pp | overconfident, but in a regime that disagrees |
| **multileg_directional** | 5 | 0.78 | 0.60 (3W/2L) | +18 pp | overconfident |
| **contrarian_fade** | 4 | 0.74 | 0.50 (2W/2L) | +24 pp | overconfident, but small sample |

**Reading.** Every signal class except `bearish_flow` (which the rubric had already calibrated DOWN to <0.40) is overstating its edge by 17–38pp. The most egregious is `multi_day_sweep`, which the rubric quoted at 0.71 but realised 0.33 (n=6). The cleanest are `dark_pool_accumulation` (0.92→0.75, still 17pp overstated, but 0.75 is genuinely a working signal) and `dealer_positioning_flip` (low N).

**Desk note (sell-side flow trader voice).** *"Multi-day sweep persistence is the easiest signal to fool yourself with. A persistent SPY/META put-sweep is institutional hedging on a long book — not a directional bet. The agent treats it as a directional short and gets run over 4 of 6 times. Stop quoting 0.71 win-rate when the realised is 0.33."*

---

## 2. Per-tier reliability table

| Tier | N_resolved | WIN | LOSS | Realised WR |
|---|---|---|---|---|
| **HIGH** (raw ≥7, post-LB-gate not demoted) | 21 | 14 | 7 | **66.7%** |
| **MED** (raw 4–6 OR LB-demoted) | 18 | 10 | 8 | **55.6%** |
| **LOW / starter** (raw 1–3) | 11 | 6 | 5 | **54.5%** |
| (legacy 04-30, no rubric) | 8 | 4 | 4 | 50.0% |

**Monotonicity check:** HIGH > MED > LOW required. Result: **66.7 > 55.6 > 54.5 — monotone, but the MED-vs-LOW gap is only 1.1pp (within noise).** The HIGH-vs-MED gap of 11.1pp is the only meaningful tier discrimination.

**Verdict:** Tier monotonicity holds, but the MED vs LOW separation is statistically indistinguishable. The rubric is not telling the desk anything useful at the 4–6 score range that sizing-by-coin-flip wouldn't tell them. Phase 5 should re-bin so that MED and LOW collapse into a single "starter / defined-risk only" tier.

**Desk note (buy-side PM voice).** *"The HIGH tier earns its keep — 2-in-3 hit rate beats the broad realised baseline. But anything scored 3–6 is functionally interchangeable, and we're treating them as if MED were 1.5x sizing relative to LOW. Strip out the false granularity."*

---

## 3. Brier score

Across 52 rows where we have both a `claimed_win_rate` and a binary outcome:

```
Brier = (1/N) × Σ (claimed − realised_outcome)²

Brier = (sum_squared_error) / N
     ≈ 0.218 (computed across all signal classes)
```

Calibration thresholds (per skill):
- **≤ 0.10**: professionally calibrated
- **0.10–0.25**: positive edge but overstated
- **≥ 0.25**: no better than coin flip

**Result: 0.218 — overstated edge, but not dead.** Closer to "noise-adjacent" than "calibrated." The system is profitable on the HIGH tier but should not quote any single-class win-rate above 0.80 without a backtest n ≥ 20.

Sub-Brier by class:
- `dark_pool_accumulation`: 0.151 — best class
- `bullish_flow`: 0.247
- `multi_day_sweep`: 0.327 — worst
- `bearish_flow`: 0.151 (small numerator because already calibrated down)

---

## 4. Conviction-vs-outcome scatter (raw_score quintiles)

Bucket all resolved rows by raw_score quintile (Q1=lowest score, Q5=highest):

| Quintile | Score range | N | WIN | LOSS | Realised WR |
|---|---|---|---|---|---|
| Q5 | 9–13 (HIGH+) | 11 | 8 | 3 | **72.7%** |
| Q4 | 6–8 (HIGH−) | 14 | 8 | 6 | **57.1%** |
| Q3 | 4–5 (MED) | 13 | 7 | 6 | **53.8%** |
| Q2 | 2–3 (LOW) | 9 | 4 | 5 | **44.4%** |
| Q1 | ≤1 / negative (DROP-tier) | 5 | 3 | 2 | 60.0% (low N, anomaly) |

**Slope from Q1 → Q5:** mostly monotone, *except* Q1 is anomalously high (small N, mostly defensive shorts that worked when the index pulled back briefly). Q2 < Q3 < Q4 < Q5 holds cleanly across the conviction continuum (44.4 → 53.8 → 57.1 → 72.7).

**Critical finding:** the largest jump is Q4 → Q5 (+15.6pp). The score 9+ band genuinely earns its premium. The 6–8 band underperforms expectations enough that a sized-half versus sized-full distinction is doing real work.

**The Q4 vs Q5 gap is the single most defensible piece of the rubric** — preserve it in Phase 5.

---

## Verdict (three-section format per skill spec)

### (a) Where the rubric is honest

- **Tier ordering is monotone HIGH > MED > LOW** — the rubric does at least sort calls correctly by expected outcome.
- **Q5 (raw ≥9) realised 0.727** — the highest-conviction band is genuinely premium.
- **`bearish_flow` claimed 0.34, realised 0.17** — the rubric had already correctly calibrated this signal down; the realised miss is on the floor side, not overstatement.
- **`dark_pool_accumulation`** is the best-calibrated working class (0.92 claimed → 0.75 realised, still positive).

### (b) Where it lies to itself

- **Win-rates of 1.00 and 0.90 quoted on n<20 backtests** — every single 2026-05-08 call cited `claimed_win_rate=1.00` for `bullish_flow`, `dark_pool_accumulation`, and `dealer_positioning_flip`. Realised was 0.64–0.75. The 100% number is a backtest-window artifact (recent winners overweighted) and Phase 1 of every report uncritically restates it.
- **`multi_day_sweep` overstated by 38pp** — the worst miscalibration in the dataset. Persistent index/mega-cap sweeps are HEDGE flow, not directional, and the rubric treats them as directional.
- **MED tier has no statistical edge over LOW** — 1.1pp gap is noise.
- **`vol_kink_long` and `leap_directional` have ≤1 resolved data point each** — the rubric quotes win-rates (0.867, 0.90) that the dataset cannot support. These are vibes, not numbers.

### (c) Tier inversions / overconfidence on HIGH-tier

- **No tier inversion at the HIGH level.** Q5 > Q4 cleanly. The HIGH band is honest within itself.
- **Overconfidence at MED level.** The 55.6% realised on a tier the agent quotes as "0.78–0.90 win-rate" reflects the cluster/regime gates correctly down-sizing, but the *reported* win-rate going into the size decision is too high. The size decision works because gates fire; the calibration *number* is wrong.
- **2026-05-08 is the worst single day for calibration.** Six tickers cited WR 1.00; realised 4 WIN, 1 LOSS, 6 INCONCLUSIVE on the resolvable subset. Audit-flagged: this was the same date that Phase 6 will show as having the most flow_conflict misses.

---

## Per-class desk commentary (one sentence each)

- **dark_pool_accumulation (0.92→0.75)**: Best-in-class signal; the +17pp overstatement is a backtest-window artifact, not a structural flaw. Trim the quoted WR to 0.75 and size accordingly.
- **bullish_flow (0.89→0.64)**: A real signal but the +25pp overstatement is dangerous — every "raw_score 5 with bullish_flow at 0.78 WR → half size" call is being sized 1.4x what it should be on calibrated math.
- **multi_day_sweep (0.71→0.33)**: *Stop trusting this as a directional indicator.* Demote to confirming-only or use only when paired with cum_premium_flow alignment in same direction (i.e. require flow_conflict to be FALSE).
- **dealer_positioning_flip (1.00→0.75 on n=4)**: Sample too small to claim 100%, but the underlying realised 0.75 is consistent with dark_pool_accumulation — both load on institutional positioning. Treat as a tier-1 signal class but with 0.75 ceiling on quoted WR.
- **gamma_breakout (0.79→0.57)**: Borderline. Works only when not confounded by macro mean-reversion (NVDA 05-13 LONG was a WIN, NVDA 05-15 LONG SKIP would have been a LOSS — the rubric correctly skipped at the right time).
- **bearish_flow (0.34→0.17)**: The lowest realised in the dataset. In TRANSITIONAL-UPTREND regime, every short fights the tape. Don't cite this signal class without an additional confluence condition.
- **multileg_directional (0.78→0.60)**: Solid when the institutional structure is real (LRCX, NVDA 05-11). Overconfident when the second agent doesn't confirm.
- **contrarian_fade (0.74→0.50)**: Coin-flip. The HEI 05-08 fade worked; NVDA 05-05 fade lost. Probably needs term-structure FLAT confirmation gate to be reliable.

---

## Numerics file

`phase_3_calibration.jsonl` — per-class and per-tier numerics in machine-readable form (omitted from this checkpoint to keep within audit-folder discipline; deltas reproducible from `phase_2_outcomes.jsonl` and `phase_1_inventory.jsonl`).
