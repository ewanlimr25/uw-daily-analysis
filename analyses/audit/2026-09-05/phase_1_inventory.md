# Phase 1 — Inventory & Parse (2026-09-05)

**14th calibration audit.** Threshold: 90 daily reports / 19 weekly — both far past the
10-daily-OR-3-weekly floor. **No DATASET-SIZE-RELAXED banner.**

## Source discipline

| | count |
|---|---|
| decision envelopes found | **88** (73 daily + 15 weekly) |
| `scripts/validate_decision.py` clean | **88 / 88** |
| rows extracted | **878** |
| unique tickers | 207 |
| `Σ score_components.points ≠ raw_score` | **0** |
| rows reconstructed from prose | **0** |

Every row in this audit is **verbatim envelope provenance**. Per C23 that means Phase-7
findings are eligible for P0 — the reconstructed-citation cap does not bind this cycle.

**Coverage gap (unchanged, already-audited).** 17 daily reports (2026-04-30 → 2026-05-22) and
4 weekly (W18–W21) predate the envelope and are legacy-prose only. They are *excluded*, not
parsed — prior audits resolved them and they carry no `score_components` / `win_rate`. Parsing
them now would inject a rubric era that no longer exists into frozen-rubric tables.

## Delta vs the 13th audit (2026-08-30)

**+6 envelopes, +89 rows** — 2026-08-31, 09-01, 09-02, 09-03, 09-04 (daily) and W36 (weekly).

New rows by section: `swing_short` 23, `vol_long` 20, `vol_short` 15, `swing_long` 18,
`watch_only` 13. New rows by regime: `pullback_in_uptrend` 50, `uptrend` 39.

Two things worth flagging before any number is computed:

1. **The new window is 56% pullback-regime.** That is the *fourth* distinct regime bucket to
   carry material weight and it is the one the P0.6 half-cap was written for. Grade the
   half-cap on these rows, not on the pooled tail.
2. **`vol_long` 20 vs `vol_short` 15 in the new rows.** Last cycle's P0 said the short-vol leg
   is adversely selected. The generation mix has moved *toward* the long leg since. That is
   C63's evidence accruing — Phase 3 must check whether it is enough (bar: n ≥ 40 decided,
   ≥ 2 regime buckets, post-change).

## Stratification (never pooled)

**Rubric era** — `2026-06-12` (FROZEN) **727**, `era_0530_0605` 69, `era_0525_0529` 54,
`pre_freeze_post_0606` 28. Post-freeze rows are 82.8% of the book.

**Regime bucket** — uptrend 377, transitional_other 211, pullback_in_uptrend 209, choppy 81.
Four buckets with n ≥ 80. This is the 7th cross-regime cycle.

**Out-of-regime (P0.6 half-cap applied)** — 44 rows.

| dimension | breakdown |
|---|---|
| kind | daily 772, weekly 106 |
| horizon | swing 618, vol 244, LEAP 16 |
| section | watch_only 356, swing_short 163, swing_long 151, vol_short 127, vol_long 72, leap_disqualified 7, leap 2 |
| tier | DROP 710, LOW 141, MEDIUM 20, HIGH 7 |
| direction | long 330, short 259, vol_short 153, vol_long 83, neutral 53 |
| fundamentals verdict | NA 283, absent 275, CAUTION 156, CONFIRM 133, **VETO 31** |
| final size | skip 447, watch_only 372, **starter 35, half 12, veto 11, full 1** |

**Signal classes with n ≥ 8** (the C23 floor): `earnings_vol` 172, `bearish_flow` 158,
`multileg_directional` 126, `bullish_flow` 77, `dark_pool_accumulation` 72, `sector_rotation`
57, `high_iv_rank` 35, `vol_term_dislocation` 28, `oi_build` 24, `dealer_positioning` 21,
`multi_day_sweep` 13, `leap_directional` 12, `gamma_breakout` 11, `opex_pin` 11, `event_vol` 11.
Everything below 8 goes to the THIN_N appendix and never to a headline.

## The fact that dominates every table below

**Post-freeze tiers are `DROP` 648 / `LOW` 79 — zero HIGH, zero MEDIUM.** All 7 HIGH and all
20 MEDIUM rows in the dataset were scored under a **pre-freeze** rubric era. The tier ladder
cannot be graded post-freeze at its top two rungs, because the frozen rubric has never once
produced one. Any HIGH/MEDIUM statistic this audit reports is a **pre-freeze artifact** and
must be labelled as such.

**48 sized rows in the entire history**, and the sizing stopped: last sized daily **2026-07-07**,
last sized anything **2026-07-24** (weekly W30, INTC starter). That is **43 consecutive
envelope-backed empty daily boards** through 2026-09-04 — the streak the memory file tracks,
re-derived here from `analyses/daily/*/decision.json` only.

## Data-quality flags

- `win_rate_source` is `NA(substrate)` on 479 rows (54.6%) — the post-quarantine honest null.
  `backtest` (84) and `fallback_proxy` (33) mark pre-quarantine substrate-contaminated quotes;
  weight accordingly, never pool with `backtest_clean` (159).
- `claimed_win_rate` present on **274 / 878** rows (31.2%). Brier / log-loss / reliability
  deciles are computed on that subset only and the N is restated wherever they appear.
- `fundamentals_verdict` null on 275 rows (pre-gate era) and `NA` on 283 — the gate's
  effectiveness denominator is 320, not 878.
- `fundamentals_verdict_reason` is null on every pre-2026-08-30 envelope **by design**
  (last cycle's P1 #1). Grade it only on post-change rows.
- No GOOG/GOOGL share-class collision this cycle. No report yielded zero rows.
