# Phase 5 — Grading-Schema Critique (2026-08-08)

> **RUBRIC FREEZE (2026-06-12) IN FORCE.** This phase *grades* the frozen rubric. It emits
> **no** weight edits and **no** cut re-bins — only pre-registrations. Every table is
> stratified by `rubric_version`; eras are never pooled.

## 5.1 Frozen-component grading (rubric_version `2026-06-12`)

Marginal contribution per emitted point-line, with tape split. Provenance: verbatim.

| component line | pts | n | WR with | WR w/o | marginal | p | BH | UP tape | DOWN tape |
|---|---|---|---|---|---|---|---|---|---|
| `oi_trend_building(+1)` @ +1 | 1 | 126 | 0.413 | 0.406 | +0.6 | 0.950 | n | +0.5 | +0.8 |
| `vol_term_structure(±)` @ +1 | 1 | 108 | 0.343 | 0.424 | −8.1 | 0.104 | n | −6.2 | −10.3 |
| `cum_flow_intent(+1)` @ −1 | −1 | 105 | 0.381 | 0.414 | −3.3 | 0.556 | n | +0.9 | −8.4 |
| `cum_flow_intent(+1)` @ +1 | 1 | 88 | 0.409 | 0.407 | +0.2 | 1.000 | n | −1.0 | +2.3 |
| `multileg_structure(+2)` @ +2 | 2 | 87 | 0.402 | 0.409 | −0.6 | 0.994 | n | +2.7 | −4.9 |
| `cum_flow_intent(+1)` @ −3 | −3 | 63 | 0.460 | 0.401 | +5.9 | 0.403 | n | +6.1 | +5.3 |
| `sector_persistence(+1)` @ +1 | 1 | 52 | 0.423 | 0.406 | +1.7 | 0.907 | n | −0.2 | +2.7 |
| `signal_confluence(+1)` @ +2 | 2 | 46 | 0.391 | 0.409 | −1.8 | 0.929 | n | +15.8 | −9.5 |
| `accumulation_conjunction(+3)` @ +1 | 1 | 44 | 0.455 | 0.404 | +5.1 | 0.588 | n | +6.1 | +3.7 |
| `cum_flow_intent(+1)` @ +3 | 3 | 42 | 0.476 | 0.402 | +7.4 | 0.409 | n | — | +7.4 |
| `dealer_dex_flip(+1)` @ +1 | 1 | 36 | 0.417 | 0.407 | +1.0 | 1.000 | n | −8.1 | +15.5 |
| `dealer_dex_flip(+1)` @ +3 | 3 | 31 | 0.355 | 0.411 | −5.6 | 0.658 | n | **−29.1** | +3.3 |
| `oi_trend_building(+1)` @ +3 | 3 | 21 | 0.476 | 0.405 | +7.1 | 0.651 | n | +23.3 | −18.0 |
| `earnings_catalyst(±)` @ +1 | 1 | 19 | 0.368 | 0.409 | −4.1 | 0.910 | n | — | −7.7 |
| `accumulation_conjunction(+3)` @ +3 | 3 | 14 | 0.429 | 0.407 | +2.1 | 1.000 | n | — | +0.4 |
| `dealer_dex_flip(+1)` @ +2 | 2 | 9 | 0.667 | 0.403 | +26.3 | 0.206 | n | — | — |
| `sector_persistence(+1)` @ 0 | 0 | 8 | 0.000 | 0.414 | −41.4 | 0.028 | n | — | −43.9 |

**Zero of 17 component lines survive BH for a 10th consecutive cycle.** The smallest raw
p is 0.028 (`sector_persistence` at its 0-point emission, n=8 — below the C23 decided-N≥8
headline floor in spirit and BH-null in fact). No weight is measurably earning its points;
equally, none is measurably *losing* points. **This is the entire case for the freeze:**
re-weighting correlated lines on n=8–126 BH-null single-window data is exactly the failure
mode that produced the cum-flow +2→+3→+1 whipsaw.

Two lines deserve narrative because they feed live pre-registrations:

- **`dealer_dex_flip` @ +3 — C50.** −29.1pp up-tape / +3.3pp down-tape (n=31), essentially
  unmoved from 08-01's −36.0/+4.2 and 07-25's −34.9/+4.1. Three windows, same shape: the
  heaviest DEX conjunction is strongly *negative* in rising tape and roughly neutral in
  falling tape. The signs are consistent but **the arms disagree in sign**, which is
  precisely what C50's acceptance bar forbids clearing on. Carry forward.
- **`accumulation_conjunction` @ +3 — C51.** +2.1pp at the +3 emission (n=14) and +5.1pp
  at the +1 emission (n=44). The single heaviest weight in the rubric still has no
  measurable marginal contribution at the point where it actually pays out. Carry forward;
  n=14 is far from the n≥30-per-arm bar.

## 5.2 Tier-cut monotonicity vs the frozen cuts

Frozen cuts: **HIGH ≥9 / MEDIUM 7–8 / LOW 3–6 / DROP ≤2.**

| band | n | WR |
|---|---|---|
| DROP (≤2) | 403 | 0.407 |
| LOW (3–6) | 112 | 0.402 |
| MED (7–8) | 14 | 0.500 |
| HIGH (≥9) | 13 | 0.385 |

**Monotone ascending DROP→HIGH? NO** — `[0.407, 0.402, 0.500, 0.385]`. The top band is the
second-worst.

Post-freeze only:

| band | n | WR |
|---|---|---|
| DROP (≤2) | 343 | 0.394 |
| LOW (3–6) | 51 | 0.353 |
| MED (7–8) | **1** | 1.000 |
| HIGH (≥9) | **0** | — |

Raw-score → WR across the whole corpus is flat-to-noisy: `-3:0.37(19) · -2:0.70(10) ·
-1:0.38(42) · 0:0.44(105) · 1:0.41(143) · 2:0.36(84) · 3:0.36(52) · 4:0.39(36) ·
5:0.55(11) · 6:0.46(13) · 7:0.71(7) · 8:0.29(7) · 9:0.67(6) · 10:0.00(3) · 11:0.33(3) ·
12:0.00(1)`. There is no monotone slope from low score to high score. **No cut re-bin is
proposed** — that is a freeze violation and the data would not support one anyway.

## 5.3 Freeze-lift check — **CANNOT RUN, 8th consecutive cycle**

The skill requires an explicit freeze-lift grade once ≥30 resolved post-2026-06-12 calls
accrue. **395 post-freeze calls are now resolved** — thirteen times the threshold — and the
lift **still cannot be graded**, because the frozen rubric has emitted:

- **0 decided HIGH** calls
- **0 decided MEDIUM** calls (1 undecided)
- 43 LOW, 352 DROP

There is no tier-monotonicity test to run on empty bands. Post-freeze book WR is **0.390
(n=395), excess −3.3pp**; the 06-27 revised LOW/DROP lift criterion therefore also fails.

**This is worth stating plainly, because eight cycles of "cannot run" is itself the
finding:** the freeze is not what is blocking the lift. The rubric's own conjunction
requirements are. A rubric that in 475 post-freeze rows produced 42 LOW, 426 DROP, and
**one `full`-sized call in the entire 626-row corpus** is not being held back by a sizing
cap — it is structurally incapable of reaching its own top bands. Lifting the freeze would
change nothing. **KEEP the freeze**, and record that the reason has shifted from "we lack
evidence" to "the test is unrunnable by construction."

## 5.4 P0.6 out-of-regime half-cap — **KEEP, protective, 5th consecutive measurement**

| arm | n | WR | excess |
|---|---|---|---|
| out_of_regime | 43 | **0.326** | −23.5pp |
| in_regime | 499 | 0.415 | +0.8pp |
| `rubric_regime` gated | 228 | 0.373 | −9.1pp |
| `rubric_regime` ungated | 314 | 0.433 | +4.3pp |

Δ = **−8.9pp on n=43**, past the actionable floor. The out-of-regime arm has now been
measured five times and is **negative in all five** (−16.7 / −14.3 / −11.9 / −12.0 / −8.9).
The cap down-sizes names that go on to lose. It is protective, not a tax. **KEEP.**

The magnitude has compressed steadily across the five measurements. Noted, not acted on —
a shrinking protective margin is a reason to keep watching, not a reason to loosen.

## 5.5 Regime-stratified direction (context for §3.4)

| regime | dir | n | WR | excess |
|---|---|---|---|---|
| pullback_in_uptrend | long | 51 | 0.510 | +5.9 |
| pullback_in_uptrend | short | 45 | 0.422 | −22.7 |
| choppy | long | 17 | 0.647 | −11.8 |
| choppy | short | 36 | 0.222 | −25.0 |
| transitional_other | long | 70 | 0.271 | +8.5 |
| transitional_other | short | 45 | 0.556 | +20.0 |

`transitional_other / short` at **+20.0pp** is the only positive short cell in the table
and the only one that has ever appeared twice (the 07-04 audit found `choppy / short`
+14.3pp on n=7, which has since inverted to −25.0pp on n=36 — a useful reminder of what a
single-window positive short cell is worth). Under the applied P0 these rows now route to
`watch_only` and keep resolving, so the counterfactual will grade itself.

## 5.6 Vol-lane grading (RV-proxy only)

| class | regime | n | WR |
|---|---|---|---|
| vol_long | uptrend | 15 | 0.533 |
| vol_long | pullback | 5 | 0.800 |
| vol_long | transitional | 10 | 0.500 |
| vol_short | uptrend | 28 | 0.464 |
| vol_short | pullback | 18 | **0.167** |
| vol_short | choppy | 16 | 0.438 |
| vol_short | transitional | 39 | 0.333 |

`vol_short` is the weakest book in the corpus (0.356 blended, n=101) and collapses to 0.167
in pullbacks — short vol into a falling tape, which is the textbook way to lose money in
this lane. This is **not** a calibrated IV-vs-RV result (no `implied_move` in the envelope),
so it cannot support a rubric change. It is the strongest argument yet for the
`implied_move` instrumentation that C43 shipped and that the vol lane still is not using.

## 5.7 Pre-registrations

**Carried forward, unchanged:**
- **C50** — `dealer_dex_flip +3` tape-conditional. Now three windows deep with a consistent
  shape (−29.1 up / +3.3 down, n=31) but the arms disagree in sign, which is the bar's
  explicit disqualifier. Bar: n≥30 per tape arm ∧ both arms same sign ∧ BH-surviving.
- **C51** — `accumulation_conjunction +3`. +2.1pp at the +3 emission on n=14. Bar: n≥30 per
  arm ∧ ≥2 regimes ∧ BH-surviving.
- **C55** — `sector_rotation` re-sourcing. **Applied at 08-01**; 4 post-fix rows, 1 decided.
  Bar for grading the fix: n≥30 decided post-fix rows.
- **C56** — `[0.55,0.65)` quote re-derivation. **Not applied.** Band still realises 0.233
  on n=43. See Phase 7 item 3.

**New this cycle:**
- **C57** — *`vol_short` regime conditioning.* Hypothesis: the `vol_short` lane's edge is
  regime-conditional and negative in pullback/falling tape (0.167 on n=18 vs 0.464 in
  uptrend, n=28). Mechanism claim: short-vol structures lose when realised vol expands, and
  the fleet does not currently condition the lane on trend. Direction of change: add a
  regime gate to `vol-surface-scout` / risk-monitor for `vol_short` structures.
  **Acceptance bar: cross-regime ∧ n≥30 per arm ∧ BH-surviving ∧ resolved against a true
  IV-vs-RV outcome (requires per-call `implied_move` in the envelope — currently absent).**
  Decision window: the first audit after `implied_move` is emitted on ≥30 vol rows.

**No weight edits. No cut re-bins. No freeze lift.**

## Output

`phase_5_schema.jsonl`
