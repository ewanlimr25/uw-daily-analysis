# Calibration Audit — 2026-06-20

**Dataset.** 23 decision envelopes (19 daily + 4 weekly), 201 calls, all valid. 160 decided on real daily-OHLC path resolution; 74 tickers + SPY. **One caveat governs everything: the entire window is single-regime (TRANSITIONAL/UPTREND) — zero bear/downtrend — so no finding is rated P0**, and the live frozen rubric (2026-06-12) has 0 resolved raw-≥9 calls and cannot yet be graded on its own outcomes.

## Top 3 schema flaws
1. **The conviction ladder is inverted at the top — again.** HIGH tier realised **0.143** (worst of four tiers); raw scores 10/11/12 → **0% / 33% / 0%**. Second consecutive audit (06-12: HIGH 0.222). Phase 3/5. → **Keep the freeze and the half-cap** (Phase 5 freeze-lift; <30 post-freeze outcomes).
2. **Fabricated ≥0.80 win-rates still reach the sizer.** `earnings_vol` 0.86→0.38 and `high_iv_rank` 0.84→0.38, both BH-surviving; the [0.80,0.90) reliability bucket (n=24) delivered 0.42. 117 of 132 quotes come from the substrate quarantined on 06-12. Phase 3. → Patch **P1**.
3. **`+2 multileg_directional` is the one BH-surviving directional lie** — class realised **0.17** (n=12) vs claimed 0.56. Phase 3/5. → Pre-register **C40** (deferred, cross-regime).

## Top 3 tool-tier surprises
1. **No tool survives Benjamini-Hochberg** — tool tiers are method-unstable for the third audit running; every label is structural-only. Phase 4.
2. **`cumulative-premium-flow` is ubiquity-confounded** — cited on 66% of tooled rows, so `with ≈ without` is mechanical. It reads NO-INFO but is almost certainly load-bearing; the fix is measurement hygiene, not demotion. Phase 4.
3. **The vol-structure tools are the strongest negatives** (`term_skew` −34.6pp, `front_end_iv_ratio` −50.0pp) — they are faithfully tagging the overconfident substrate vol classes, not malfunctioning (RV-proxy-contaminated). Phase 4.

## What we'd do Monday
The flow engine has a **long edge and a short problem**. Longs beat same-window SPY by **+15–20pp** (real, but decaying 67%→38% across eras — single-regime, not yet durable); the short book *lost* **22.7pp** to simply shorting the index over the same falling windows — negative selection, not just an up-tape. So Monday: **stop sizing outright single-name shorts — express bearish theses index-relative** (#1), and **bind the 0.80 win-rate ceiling at emission so the fabricated vol quotes stop driving size** (#2). Hold the line on the freeze, the half-cap, and every risk gate — on a tape that never broke, you don't dismantle the insurance. Nothing is P0; the regime that would prove these calls hasn't happened yet.
