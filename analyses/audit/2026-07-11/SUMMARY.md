# Calibration Audit — 2026-07-11

Dataset: 396 verbatim envelope calls (40 `decision.json`; 33 daily + 7 weekly), 129 tickers OHLC-resolved path-aware, 0 fetch failures, 0 `Σpoints≠raw_score` violations. Strata: pre-freeze 2026-05-15 (54) / 2026-05-30 (97) / **FROZEN 2026-06-12 (245)** — never pooled. 6th edge audit; **first with a mandatory model-transition section** (2026-07-03 pins).

## Top 3 schema flaws
1. **The +3 accumulation conjunction is significantly negative-excess.** `dark_pool_accumulation` realises 0.417 vs a 0.708 SPY up-day base — **−29.2pp, p=0.003, BH-SURVIVES** (Phase 3); its backing tools read −22.2pp / −17.8pp (Phase 4). The single highest-weighted line rides beta and lags it. → register **C48** (Phase 5), P1.
2. **The one class with real edge is unscored.** `bearish_flow` +29.4pp excess (p=0.005, BH-SURVIVES) — the short/put lane beats the SPY-short base by 29pp; the rubric scores it **0 points** (C19 still advisory). The system's only market-beating behavior is the one it won't size.
3. **The frozen rubric has produced 0 HIGH/MED calls in a month** — freeze-lift fails to run a 4th cycle (needs ≥30 resolved post-freeze HIGH/MED; has 0). Tier inversion (HIGH 0.286, 2/7) is entirely pre-freeze (4 index/semis shorts 0-for-4). Keep freeze + P0.6 half-cap.

## Top 3 tool-tier surprises
1. `uw historical oi-trend` **−17.8pp** (n=54, verbatim) — sharpens C47 from −9.2pp; W28 showed universal `consecutive_build_days == --days` saturation. The +3 OI line's tool is anti-predictive this regime.
2. `uw insights institutional-accumulation` **−22.2pp** (n=16) — the most-negative tool on the board, and it anchors the +3 conjunction.
3. `uw dark-pool block-stratified` **+15.9pp** (n=8, THIN_N) — the lone positive component of the accumulation stack; the institutional/retail *filter* may carry the edge the raw tools destroy. → isolation pre-register (P2).

## Model transition (2026-07-03 pins) — CLEAN
0 quant Σ-violations post-pin; debate bear-residual stable 0.694→0.75; all 9 post-pin non-DROP calls LOW/watch-only. Edge-impact not yet measurable (0 resolved). Re-audit after ≥5 resolved post-pin calls. No escalation triggered.

## What we'd do Monday
Nothing to the live files — and that is the finding. Four cross-checks now agree the desk's edge is short-side and its highest-conviction long lane is negative-excess beta, but every one is single-regime, so the freeze holds: no re-weight, no re-bin, no gate surgery. The DROP pile (0.477) out-performed the traded book (0.406), which is precisely why refusing to size the empty boards is graded-correct, not a failure. Register C48 (accumulation negative-excess) and keep accruing the bearish-line (C19) evidence toward its cross-regime gate. The single most valuable thing that could happen to this rubric is a **down-tape** — it is the only experiment that can tell edge from beta, and we still haven't had one.
