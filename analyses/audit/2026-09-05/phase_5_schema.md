# Phase 5 — Grading the FROZEN Rubric (2026-09-05)

> **This phase grades. It does not retune.** The rubric is frozen at `2026-06-12`. Every table
> is stratified by `rubric_version`; eras are never pooled. The only change output permitted
> here is a **pre-registration**.

## 5.0 — The finding: the freeze cut the components and left the cuts where they were

The frozen rubric's tier cuts are **HIGH ≥ 9 / MEDIUM 7–8 / LOW 3–6 / DROP ≤ 2**. Those cuts
were set on 2026-05-15 and re-confirmed against a scoring distribution that no longer exists.

On 2026-06-12, audit P0.1/P0.2 removed `uw insights signal-confluence` from scoring (it was a
server-side composite that re-counted the rubric's own inputs), quarantined `signal-backtest`,
and cut the cum-flow line to +1 intent-screened. **Those were correct changes and this audit
does not dispute them.** What was never re-checked is what they did to the arithmetic.

| | pre-freeze | post-freeze |
|---|---|---|
| rows scored | 151 | 727 |
| **mean `raw_score`** | **3.56** | **0.86** |
| p90 `raw_score` | 8 | 3 |
| max `raw_score` | 12 | 7 (once, a weekly `veto`) |
| rows ≥ 9 (HIGH) | 13 | **0** |
| rows ≥ 7 (MEDIUM+) | 27 | **1** |
| mean components per row | 2.56 | 1.68 |
| **mean points per component** | **1.391** | **0.512** |
| components worth ≥ 2 | 178 of 386 (46%) | 145 of 1,220 (**12%**) |
| components worth 3 | 95 of 386 (24.6%) | 33 of 1,220 (**2.7%**) |

The two components that carried the pre-freeze top of the ladder — `uw insights
signal-confluence` (43 awards ≥2) and `uw historical cumulative-premium-flow` (37 awards ≥2) —
are **gone from the post-freeze scoring mass entirely.** Scoring mass per component fell 63%.
The cuts did not move.

### It is a step function at the freeze date, not a market condition

Daily session-max `raw_score`, before and after 2026-06-12:

| | sessions | mean session-max | median | sessions with a HIGH-eligible (≥9) row |
|---|---|---|---|---|
| pre-freeze (05-25 → 06-11) | 14 | 8.36 | **9.0** | **8 of 14** |
| post-freeze (06-12 → 09-04) | 59 | 2.73 | **3.0** | **0 of 59** |

Mann-Whitney **z = 5.65, p = 1.6 × 10⁻⁸**. The session mean drops from 3.83 (06-11) to **0.38
(06-12)** in one session and never recovers across 59 sessions spanning **all four regime
buckets**. A market explanation requires a recovery in at least one bucket; there is none.
The pre/post boundary is the rubric change, and nothing else changed on that date.

### What this means, stated carefully

The HIGH cut now sits **8 points above the post-freeze mean** and above the maximum ever
observed in 727 post-freeze rows. MEDIUM has been reached **once**, by a row that was vetoed.
**Every post-freeze call in this system is DROP or LOW by construction.**

That is the mechanism behind the observation this project has reported for seven consecutive
cycles as "the freeze-lift test is structurally unrunnable" and "the empty conviction book is
the frozen rubric behaving as calibrated." Both statements are true. What is new is that the
emptiness is **arithmetic, not evidence**: the ladder is not declining to promote candidates
because it measured them and found them wanting — its top two rungs were placed out of reach
by a change to the components underneath them, and no one re-derived the cuts.

**The honest counterfactual, stated against my own finding.** Not trading may well be the
right outcome. Realised WR is DROP 0.391 ≈ LOW 0.402, the sized book is 42.6% on n=47, HIGH
(when it existed) realised 0.143, and tier expectancy is negative in every tier but MEDIUM.
Nothing here says the fleet is leaving money on the table — **it probably is not.** The defect
is not "we should be trading more." The defect is that a conviction ladder whose top half is
unreachable **cannot discriminate, cannot be graded, and cannot ever lift its own freeze** —
the test requires post-freeze HIGH/MEDIUM rows that the arithmetic forbids it to produce.
The system has been running an unfalsifiable rubric for 59 sessions.

## 5.1 — Component grading (frozen weights vs measured contribution)

No proposed-weight column. No budget renormalisation. Per C23, BH across the component set.

| component [awarded] | pts | n | WR | base | marg | p | BH |
|---|---|---|---|---|---|---|---|
| `oi_trend_building(+1)` [+1] | 1 | 200 | 0.385 | 0.397 | −1.2 | 0.777 | n |
| **`vol_term_structure(+/−)` [+1]** | 1 | **176** | 0.307 | 0.421 | **−11.4** | **0.002** | **Y** |
| `cum_flow_intent(+1)` [−1] | −1 | 153 | 0.379 | 0.398 | −1.9 | 0.696 | n |
| `multileg_structure(+2)` [+2] | 2 | 114 | 0.404 | 0.392 | +1.1 | 0.879 | n |
| `cum_flow_intent(+1)` [+1] | 1 | 112 | 0.438 | 0.387 | +5.1 | 0.312 | n |
| `cum_flow_intent(+1)` [−3] | −3 | 86 | 0.430 | 0.389 | +4.1 | 0.504 | n |
| `sector_persistence(+1)` [+1] | 1 | 57 | 0.439 | 0.390 | +4.8 | 0.539 | n |
| `accumulation_conjunction(+3)` [+1] | 1 | 53 | 0.434 | 0.391 | +4.3 | 0.613 | n |
| `dealer_dex_flip(+1)` [+1] | 1 | 51 | 0.471 | 0.389 | +8.2 | 0.290 | n |
| `cum_flow_intent(+1)` [+3] | 3 | 42 | 0.476 | 0.389 | +8.7 | 0.319 | n |
| `accumulation_conjunction(+3)` [+3] | 3 | 18 | 0.389 | 0.394 | −0.5 | 1.000 | n |

**One BH survivor — and it is the same composition artifact as Phase 4.1.** Lane-controlled:

| stratum | with | WR | without | WR | marginal |
|---|---|---|---|---|---|
| overall | 272 | 0.360 | — | — | −11.4pp |
| inside VOL | 143 | 0.336 | 79 | 0.342 | **−0.6pp** |
| inside `vol_short` | 99 | 0.253 | 47 | 0.255 | **−0.3pp** |
| inside `vol_long` | 44 | 0.523 | 32 | 0.469 | **+5.4pp** |

Inside its own lane the line contributes **nothing, in either direction**. Its headline
negativity is the `vol_short` deficit shining through the tool that happens to be cited there.
**No weight change is supportable.** All three BH survivors this cycle (two tools, one
component) are lane composition; the fourth candidate, `term_structure_hygiene.py`, is one
month of August. **The rubric table is BH-null in substance for the 13th consecutive cycle.**

The **+3 accumulation conjunction** — the rubric's single largest line — reads **−0.5pp on
n=18 when awarded in full** and +4.3pp on n=53 when halved to +1. The halved award is
outperforming the full one. n=18 is too thin to act on and this is not a proposal; it is the
sixth consecutive cycle in which the largest weight in the rubric has failed to show a
positive contribution at its full value.

## 5.2 — Tier-cut monotonicity

| band | n | WR |
|---|---|---|
| DROP (≤2) | 583 | 0.384 |
| LOW (3–6) | 141 | 0.426 |
| MEDIUM (7–8) | 14 | 0.500 |
| HIGH (≥9) | 13 | **0.385** |

**Monotone ascending: FALSE.** HIGH collapses back to the DROP level. Sixth consecutive cycle
of tier inversion at the top.

Post-freeze only: DROP 0.373 (n=523), LOW 0.412 (n=80), **MEDIUM n=1, HIGH n=0.** The cut
grading cannot run on its own era — for the reason §5.0 establishes.

**Do not propose new cuts from this window.** Re-binning on a single window is the documented
failure mode the freeze exists to prevent, and §5.0 is a *defect report about how the current
cuts came to be orphaned*, not evidence for where new ones belong.

## 5.3 — P0.6 out-of-regime half-cap

OOR n=43 WR 0.326 vs in-regime 0.398 — **−7.3pp, protective, ninth consecutive negative
reading.** **KEEP.** Freeze-lift remains unrunnable (post-freeze HIGH/MEDIUM n=0).

## 5.4 — Pre-registrations emitted this cycle

**C65 — tier-cut re-basing after a component-weight change.**
*Hypothesis:* the frozen cuts (≥9 / 7–8 / 3–6 / ≤2) were calibrated on a pre-2026-06-12
scoring distribution (mean 3.56, p90 8) and are non-discriminating on the post-freeze
distribution (mean 0.86, p90 3, max 7, HIGH-eligible rows 0 of 727).
*Mechanism claim:* removing scoring mass without re-deriving cuts moves the tier boundaries'
**percentile** position, not just their level; the HIGH cut moved from ≈p90 to beyond p100.
*Acceptance bar:* cross-regime ∧ **n ≥ 30 per arm** ∧ BH-surviving at FDR 0.10, where the arms
are candidate re-based bands (e.g. percentile-anchored) measured against realised WR on
post-freeze rows only. *Decision window:* **2026-11-07 or later** — this needs post-freeze
rows scored under a *changed* configuration, which do not yet exist.
*Explicitly NOT proposed here:* any specific new cut. §5.0 diagnoses; it does not prescribe.

**C66 — the vol lane cannot reach a sizeable tier under the frozen rubric.**
*Evidence:* `vol_long` max `raw_score` **4** on 85 rows (median 1); `vol_short` max 5 on 153.
**Neither lane has produced a single MEDIUM or HIGH call in the corpus's entire history.**
Every component that has ever fired on a `vol_long` row is worth **+1**; the rubric's ≥2 lines
(`+3` accumulation conjunction, `+2` multileg) are directional-only by construction. To reach
MEDIUM a vol thesis needs **seven simultaneous +1 lines**, which has never occurred in 238 vol
rows. *Why it matters now:* the 2026-08-30 P0 routed `vol_short` to `watch_only`, leaving
`vol_long` — the one lane with a positive, peer-controlled, 4-regime-robust excess (+8.5pp,
McNemar p=1.5×10⁻⁴, **5-for-5 on every sized row it ever had**) — as the only sizeable vol
expression. It cannot clear DROP. The vol lane is now closed on both legs: one by measured
decision, one by an unexamined scoring gap. *Acceptance bar:* cross-regime ∧ n ≥ 30 per arm ∧
BH-surviving. *Decision window:* **2026-10-31**.
*Note:* this generalises the standing weekly-rubric observation (`vol_term_dislocation` maxes
at 1 point) to the **daily** rubric, and upgrades it from a coverage gap to a live constraint.
