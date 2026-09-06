# Phase 5 — Grading-Schema Critique (2026-07-25)

> **RUBRIC FREEZE (2026-06-12) IN FORCE.** This phase grades the frozen rubric. It emits
> no weight edits and no cut re-bins — only pre-registrations. Every table is stratified
> by `rubric_version`; eras are never pooled.

Provenance: verbatim. Voice: market-maker quant.

## 5.1 Frozen component-line grading

Marginal contribution of each scored line (WR with the line present − WR without),
plus the same contribution conditioned on realised tape (Phase 3c), since Phase 3d
established that stratum-level excess is 71% benchmark.

| component line | pts | n | WR with | WR w/o | marginal | p | BH | UP tape | DOWN tape |
|---|---|---|---|---|---|---|---|---|---|
| `cum_flow_intent` | −1 | 86 | 0.395 | 0.432 | −3.7 | 0.564 | n | +9.5 | −11.8 |
| `oi_trend_building` | +1 | 77 | 0.442 | 0.421 | +2.0 | 0.805 | n | −4.4 | +4.5 |
| `vol_term_structure` | +1 | 73 | 0.384 | 0.433 | −5.0 | 0.462 | n | −7.3 | −3.8 |
| `multileg_structure` | +2 | 67 | 0.418 | 0.426 | −0.8 | 0.993 | n | +9.4 | −8.6 |
| `cum_flow_intent` | +1 | 60 | 0.450 | 0.421 | +2.9 | 0.742 | n | +6.9 | +0.5 |
| `cum_flow_intent` (flow_conflict) | −3 | 50 | 0.460 | 0.421 | +3.9 | 0.669 | n | +6.5 | +3.6 |
| `signal_confluence` | +2 | 46 | 0.391 | 0.429 | −3.8 | 0.719 | n | +11.3 | −8.4 |
| `cum_flow_intent` | +3 | 42 | 0.476 | 0.420 | +5.7 | 0.554 | n | — | +8.2 |
| `sector_persistence` | +1 | 42 | 0.405 | 0.427 | −2.2 | 0.897 | n | −11.6 | +1.9 |
| **`accumulation_conjunction`** | **+1** | 41 | 0.463 | 0.421 | +4.2 | 0.691 | n | −4.4 | +9.2 |
| **`dealer_dex_flip`** | **+3** | 31 | 0.355 | 0.430 | **−7.5** | 0.508 | n | **−34.9** | +4.1 |
| `dealer_dex_flip` | +1 | 24 | 0.417 | 0.425 | −0.9 | 1.000 | n | −20.0 | +8.9 |
| `earnings_catalyst` | +1 | 19 | 0.368 | 0.428 | −5.9 | 0.781 | n | — | −6.8 |
| `oi_trend_building` | +3 | 15 | 0.333 | 0.428 | −9.5 | 0.639 | n | — | −17.1 |
| **`accumulation_conjunction`** | **+3** | 14 | 0.429 | 0.425 | **+0.4** | 1.000 | n | — | +1.3 |
| `dealer_dex_flip` | +2 | 9 | 0.667 | 0.420 | +24.7 | 0.247 | n | — | — |
| `sector_persistence` | 0 | 8 | 0.000 | 0.433 | −43.3 | 0.021 | n | — | −42.9 |

**Zero component lines survive BH at FDR 0.10 across 17 tests.** The lowest raw p is
0.021, on a *zero-point* line at n=8 (a degenerate 0-for-8 cell, not a scored weight).

### Line-by-line read

- **`accumulation_conjunction` +3** — the rubric's single heaviest line. Measured
  marginal **+0.4pp on n=14** (WR-with 0.429 vs base 0.425). It is currently paying 3
  points for nothing measurable. The 2026-07-18 audit's "the negative excess was beta
  all along" verdict is confirmed and completed: it is neither negative nor positive —
  it is **null**. Carried, not actioned; n=14 is far below the n≥30-per-arm bar.
- **`dealer_dex_flip` +3** — **−7.5pp overall, −34.9pp in the up-tape, +4.1pp in the
  down-tape.** The one line whose tape-conditioned split is genuinely wide. This is the
  mechanized DEX line the 2026-06-12 P0.4 work added; the 2026-07-24 daily fired it
  twice (MU, NBIS) and both died on flow-conflict. Pre-registered below.
- **`cum_flow_intent` −3 (flow_conflict)** — the kill switch that produced 19 straight
  empty boards. Marginal **+3.9pp**, positive in both tapes. It is not hurting, and it
  is the mechanism behind the DROP pile's outperformance. Keep.
- **`vol_term_structure` +1** — −5.0pp, negative in both tapes, and it feeds the two
  BH-surviving miscalibrated classes (`earnings_vol`, `high_iv_rank`). Weakest line in
  the rubric on consistency, though still BH-null.

## 5.2 Tier-cut monotonicity vs frozen cuts

Frozen cuts: **HIGH ≥9 / MEDIUM 7–8 / LOW 3–6 / DROP ≤2**.

| band | n | WR |
|---|---|---|
| DROP (≤2) | 327 | 0.431 |
| LOW (3–6) | 87 | 0.402 |
| MED (7–8) | 13 | 0.462 |
| HIGH (≥9) | 13 | 0.385 |

**Monotone ascending DROP→HIGH: FALSE** — `[0.431, 0.402, 0.462, 0.385]`. The cuts do
not order outcomes. DROP outperforms both LOW and HIGH.

Post-freeze only: DROP 0.419 (n=267), LOW 0.308 (n=26), **MED n=0, HIGH n=0.**

## 5.3 Freeze-lift check

The skill requires an explicit freeze-lift grade at ≥30 resolved post-freeze calls.
There are **293** resolved post-freeze calls — the count bar is met — but they contain
**zero HIGH and zero MEDIUM names**, so tier-monotonicity above LOW cannot be evaluated.

**Recommendation: KEEP THE FREEZE (6th consecutive cycle).** The freeze-lift test is
not merely unsatisfied; it is structurally unrunnable, because the frozen rubric no
longer emits the tier population its own lift test requires. That is itself worth
naming as a design fact rather than logging as "insufficient data" a seventh time.

## 5.4 P0.6 out-of-regime half-cap — **ACTIONABLE, PROTECTIVE**

| arm | n | WR | excess |
|---|---|---|---|
| out_of_regime | 41 | **0.317** | −14.3pp |
| in_regime | 399 | 0.436 | +5.2pp |
| Δ | | **−11.9pp** | |

n=41 clears the C24 actionable floor (was n=34 at 07-18, n=20 at 07-04, and the sign has
been negative every time). Out-of-regime names lose materially more. **KEEP the half-cap.**

## 5.5 Pre-registrations (decided by a FUTURE audit, on data that does not yet exist)

| ID | hypothesis | mechanism claim | acceptance bar | decision window |
|---|---|---|---|---|
| **C49** | Auditor: replace raw benchmark-excess as the primary edge column with tape-conditioned book WR + paired McNemar | 71% of excess variance is the benchmark (Phase 3d) | method change; validate by re-deriving 07-11/07-18 headlines and confirming they dissolve | next audit |
| **C50** | `dealer_dex_flip +3` is tape-conditional (negative in up-tape, neutral-positive in down-tape) | DEX flips signal exhaustion, which only pays when the tape is already rolling | cross-regime ∧ n≥30 per tape arm ∧ BH-surviving | ≥2 audits, needs ~60 more DEX-flip rows |
| **C51** | `accumulation_conjunction +3` is over-weighted (measured +0.4pp at n=14) | the conjunction re-counts one dark-pool observation three ways | cross-regime ∧ n≥30 per arm ∧ BH-surviving | ≥3 audits at current fire rate |
| **C52** | Short-side selection has no alpha in any tape and should not be alpha-sized | DOWN/short −13.7pp vs naive index short (p=0.12, ns); direction-call accuracy 39.7% in falling tape | n≥30 decided shorts in a *second* independent down-tape ∧ BH | next genuine down-tape |
| **C53** | Retire C19 (bearish-flow accrual) as refuted rather than blocked | book WR 0.533 UP / 0.526 DOWN — stationary; the "edge" was the denominator | already met: 3 windows, stationary book WR, n=94 | **decide now — see Phase 7** |

**No weight edits and no cut re-bins are emitted by this phase.**

Output: `phase_5_schema.jsonl`.
