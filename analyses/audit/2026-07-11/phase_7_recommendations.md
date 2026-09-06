# Phase 7 — Recommendations (2026-07-11) — PROPOSE-ONLY

Provenance is **verbatim** (envelope `score_components`), but the frozen-era dataset is **single-regime (TRANSITIONAL/UPTREND)** — so nothing clears the cross-regime bar and **nothing is P0**. All rubric/tool items are pre-registrations, per the freeze.

## P1 — Keep the freeze + half-cap (freeze-lift check: FAILS to run, 4th cycle)
**What:** Retain the 2026-06-12 rubric freeze and the P0.6 out-of-regime half-cap; do not lift.
**File:** `.claude/commands/daily-analysis.md` + `weekly-analysis.md` Step 5 (no edit — confirmation).
**Phase/Data:** Phase 1/2 — 0 resolved post-freeze HIGH/MED calls (need ≥30); frozen era produced only LOW (0.529, n=17). Freeze-lift precondition structurally unmet.
**Priority:** P1. **Risk:** none — this is the status quo; the risk is lifting on a regime that never produced a HIGH call.

## P1 — Register C48: accumulation-conjunction negative-excess
**What:** Pre-register that the +3 `dark_pool_accumulation` conjunction is negative-excess and should reduce toward +1 OR be gated on the `dark-pool block-stratified` institutional-tier filter (the lone +15.9pp component).
**File:** register only (`analyses/audit/2026-07-11/`), decided by a future cross-regime audit.
**Phase/Data:** Phase 3 — dark_pool_accumulation 0.417 WR vs 0.708 SPY, −29.2pp excess, p=0.003 BH-SURVIVES (n=24); Phase 4 — institutional-accumulation −22.2pp marginal.
**Priority:** P1 (single-regime caps it below P0). **Risk:** the negative excess may be an up-tape artifact — a downtape could invert it; that is exactly why the decision waits for cross-regime data.

## P1 — Sharpen C47 (oi-trend saturation) with fresh outcome evidence
**What:** Carry C47 with strengthened evidence; do not act.
**Phase/Data:** Phase 4 — oi-trend −17.8pp (was −9.2pp); W28 showed `consecutive_build_days == --days` on every liquid name (saturation is universal, not name-specific). Acceptance bar still unmet (single-regime).
**Priority:** P1-carry. **Risk:** none (carry).

## P1 — C19 bearish/short edge: log the second-regime positive accrual
**What:** Record that `bearish_flow` posted +29.4pp benchmark-excess (BH-SURVIVES, p=0.005) this window — continued OOS accrual toward the C19 scored-bearish-line graduation.
**File:** `.claude/commands/*.md` "Single-Leg Whale Persistence" section (register only; no scored line yet).
**Phase/Data:** Phase 3/5 — bearish_flow 0.471 vs 0.176 SPY-short base. Still behind the rolling-WR≥58% / ≥60-day / ≥2-regime gate.
**Priority:** P1. **Risk:** scoring a bearish line prematurely in a tape that has been range-bound-up would size shorts into the one thing that has *lost* (the HIGH-tier index shorts 0-for-4) — keep it advisory until the gate certifies.

## P2 — Model-transition: re-audit after ≥5 resolved post-pin calls
**What:** Schedule a focused re-check of the 2026-07-03 pins once post-pin calls resolve.
**Phase/Data:** Phase 6 — transition CLEAN (0 compliance violations, bear-residual 0.694→0.75) but 0 resolved outcomes; edge-impact unmeasured.
**Priority:** P2. **Risk:** none.

## P2 — Isolate `dark-pool block-stratified` (+15.9pp, n=8)
**What:** Pre-register an isolation test: does the institutional-tier filter alone carry the accumulation edge that the raw tools lose?
**Phase/Data:** Phase 4 — block-stratified +15.9pp vs institutional-accumulation −22.2pp / oi-trend −17.8pp. THIN_N (n=8).
**Priority:** P2 (needs N≥ before action). **Risk:** thin-N false positive.

**Nothing edits a live file. All items are register entries or status confirmations.**
