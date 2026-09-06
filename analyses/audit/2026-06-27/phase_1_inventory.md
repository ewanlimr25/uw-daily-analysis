# Phase 1 — Inventory & Parse (2026-06-27)

**Provenance basis: VERBATIM decision-envelope.** All 257 rows are loaded from validated
`decision.json` sidecars (`score_components[].source_tool` read directly). No prose
reconstruction. Sum-points reconciliation is clean (`SUM_POINTS != RAW_SCORE` = **0/205**),
so the validator's Σ-points==raw_score invariant holds on every scored row.

## Coverage

| | Envelopes | Calls | Note |
|---|---|---|---|
| Daily | 24 (2026-05-25 → 06-26) | 233 | |
| Weekly | 5 (W22 → W26) | 24 | |
| **Total** | **29** | **257** | 90 unique tickers + SPY |

Legacy prose-only reports (pre-2026-05-25 daily, pre-W22 weekly — 22 daily + 4 weekly)
carry no envelope and were resolved by prior audits (05-30 / 06-06 / 06-12 / 06-20);
they are a known coverage gap, not re-parsed here. This audit grades the **envelope era only**.

## The regime finally diversified — but the new regime hasn't resolved yet

Every prior audit carried one governing caveat: *single-regime (TRANSITIONAL/UPTREND), zero
downtrend.* That caveat is **partially lifted this run.** Late June broke the tape:

- **06-22/06-23** — SPY & QQQ dealer books flipped **FULLY_NEGATIVE short-gamma**; hard semi/AI
  selloff (SK Hynix HBM slowdown).
- **06-24 → 06-26** — "distribution-into-strength" (flow breadth 35% bullish vs price breadth
  60–64% green), SPY −2.86% 30d, below both 20/50 SMA, regime tagged **CHOPPY**.

Regime-bucket split of the 257 rows: **uptrend 115 · pullback_in_uptrend 124 · choppy 18.**
We now have a non-pure-uptrend stratum to grade — the first time. **Caveat that governs Phase
2–7:** the genuinely off-trend calls (06-23 → 06-26) are the *newest*, so their 3D/10D windows
are mostly still open as of 06-27. The choppy bucket has **0 decided**; only the pullback
stratum (06-05 → 06-18) has resolved. So we can grade *pullback*, not yet *choppy/selloff*.

## Distribution

- **Horizon:** swing 201 · vol 52 · LEAP 4
- **Section:** watch_only 110 · swing_long 61 · swing_short 53 · vol_short 21 · vol_long 11 · leap_disqualified 1
- **Tier:** DROP 158 · LOW 72 · MEDIUM 20 · HIGH 7
- **Direction:** long 113 · short 89 · vol_short 33 · vol_long 13 · neutral 9
- **Final size:** watch_only 141 · skip 78 · **starter 24 · half 12** · veto 2 — **no `full` anywhere** (half-cap binding)
- **Fundamentals verdict:** NA 96 · CONFIRM 47 · CAUTION 46 · VETO 6 · (null 62, legacy/no-gate)
- **win_rate_source:** backtest 84 · backtest_clean 31 · fallback_proxy 33 · NA(substrate) 18 · NA 53 · null 38

### Signal-class fragmentation (Phase-2 canonicalization required)
Top classes: bearish_flow 56 · dark_pool_accumulation 39 · earnings_vol 38 · bullish_flow 35 ·
multileg_directional 26 · high_iv_rank 12 · dealer_positioning 8. A long tail of singleton
dealer*/dex_flip*/distribution labels is collapsed in Phase 2 (`canonical_class`) for cross-audit
comparability — same merge map as 06-20, extended for `single_leg_*`/`sector_*` fragments.

## Two flags that pre-stage the whole audit

1. **POST-FREEZE tier distribution: DROP 96 / LOW 10 / MEDIUM 0 / HIGH 0.** Since the 2026-06-12
   freeze, across 106 calls, the rubric has emitted **not one MEDIUM-or-better call.** The frozen
   `≥9 = HIGH` cut has zero post-freeze instances → its grading remains un-runnable on its own
   outcomes (3rd audit). The book went inert above LOW exactly as the tape deteriorated.

2. **Rubric eras:** 2026-06-12 (post-freeze) 106 · era_0530_0605 69 · era_0525_0529 54 ·
   pre_freeze_post_0606 28. Every downstream table stratifies by `rubric_era`; pooling is banned
   (memory: raw-9 recorded MEDIUM in 05-30→06-05). **All raw-≥9 calls in the dataset are pre-freeze.**

## Data-quality flags
- `final_size=veto` (2) and `fundamentals_verdict=NA/null` (158) are expected — watch-only and
  pre-gate legacy rows. Excluded from sized-book denominators.
- 9 `neutral`-direction rows → NOT_A_TRADE in Phase 2 (directionless; non-pin).
- No GOOG/GOOGL share-class collisions detected this run.

**Outputs:** `phase_1_inventory.jsonl` (257 rows), `_tickers.json` (90 syms).
