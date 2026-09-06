# Phase 2 — Outcome Resolution · 2026-07-04

**Win threshold (verbatim).** ≥ +1R move in thesis direction within window **without** −1R drawdown first; R = 0.5 × true-range-ATR(14) at entry. Path-aware on **daily OHLC bars** (Yahoo chart API, C20) — a bar whose low breaches `entry − R` before any high reaches `entry + R` is a LOSS for a long, symmetric for shorts; same-bar both-thresholds = LOSS (conservative `ambiguous_bar`). **INCONCLUSIVE** = window still open, window complete without either threshold, or no price data (`data_unavailable` — never a LOSS). Vol calls resolve on RV-direction proxy (`rv_direction_proxy` — envelopes still lack `implied_move`; see C42(b)/C43). LEAPs stay INCONCLUSIVE until the 90D window closes. OPEX pins resolve on max-excursion-vs-R over 5D.

**Data.** OHLC fetched 117/118 symbols through **2026-07-02** (07-03 = July-4th holiday; UW data confirmed fresh through 07-02 at preflight). `SPX` (index symbol) unfetchable → its rows are `data_unavailable`. SPY real-OHLC verified (last bar 07-02: H 751.31 / L 740.03).

## Headline

| | n | WIN | LOSS | WR |
|---|---|---|---|---|
| **All decided** | **264** | 116 | 148 | **43.9%** |
| Sized book (starter/half) | 36 | 13 | 23 | **36.1%** |
| Paper book (watch/skip/veto) | 228 | 103 | 125 | 45.2% |

335 rows → 264 decided · 62 INCONCLUSIVE (50 window_open, 6 leap_window_open, 3 no_threshold, 3 data_unavailable) · 9 NOT_A_TRADE (directionless neutral). Decided-N grew 264 vs 205 at 06-27 — the choppy 06-23→06-26 stratum is now decided.

**The sized book underperforms the paper book by −9.1pp.** With the empty-book protocol live since 06-29, "sized" is almost entirely the pre-freeze legacy tail — but it means the calls the system *committed capital to* did worse than the ones it only watched. Carried to Phase 3/6.

## By direction (C21 benchmark beside it)

| Direction | n | WR | SPY same-window base | Excess |
|---|---|---|---|---|
| long | 119 | 48.7% | 31.9% (n=113) | **+16.9pp** |
| short | 90 | 42.2% | 65.2% (n=89) | **−22.9pp** |
| vol_long | 15 | 93.3% | — (RV proxy) | — |
| vol_short | 37 | 13.5% | — (RV proxy) | — |

The vol_long 93% / vol_short 13% split is the **RV-proxy signature** (realised range expanded through the pullback→choppy sequence), not tradeable P&L — unchanged caveat from 06-27.

## By regime bucket (decided)

| Bucket | n | WR |
|---|---|---|
| uptrend | 113 | 46.9% |
| pullback_in_uptrend | 112 | 43.8% |
| **choppy (new — first decided read)** | **14** | **28.6%** |
| transitional_other (empty-book era) | 25 | 40.0% |

## By tier (full table in Phase 3)

HIGH 0.143 (n=7) · MEDIUM 0.526 (n=19) · LOW 0.444 (n=72) · DROP 0.440 (n=166). Post-freeze decided = 117 (LOW 11 / DROP 106 — zero HIGH/MED). Out-of-regime decided = 20 (grading now actionable, Phase 3b).

## C3 advisory expectancy record

`realized_pnl_pct` populated on every closed directional/vol/pin call in `phase_2_outcomes.jsonl`; class-level `payoff_ratio` / `expectancy` / `capped_half_kelly` computed in Phase 3 (`scripts/kelly_sizing.py`). Advisory only — the win-rate ladder remains the live sizer (gate: Phase 3). Still-open calls carry nulls. Per the propose-only invariant, these live in the audit JSONL, not written back into source envelopes.

Machine-readable: `phase_2_outcomes.jsonl` (335 rows, Phase-1 fields + `outcome`, `realised_return_pct`, `max_adverse_excursion_pct`, `spy_benchmark_win`, `canonical_class`, `was_sized`).
