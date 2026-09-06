# Phase 5 — Grading the FROZEN Rubric (2026-08-15)

> **RUBRIC FREEZE (2026-06-12 audit P0.1) is in force.** This phase **grades** the frozen
> rubric. It emits **no weight edits and no cut re-bins** — only pre-registrations. Every
> table is stratified by `rubric_version` / era; nothing is pooled across rubric eras.
> Provenance: verbatim envelope `score_components`, 569 scored rows, **0 `Σpoints ≠ raw_score`
> violations**.

## 5.1 Frozen-component grading

Notation `component(frozen_weight)[points_awarded]`. Marginal is class-conditional,
book base = 0.414 (n=572 decided). BH at FDR 0.10 across the component set.

| component line | pts | n | WR with | WR w/o | marginal | p | BH | UP tape | DN tape |
|---|---|---|---|---|---|---|---|---|---|
| `oi_trend_building(+1)` | +1 | 142 | 0.423 | 0.412 | +1.1pp | 0.854 | n | +1.4 | +0.8 |
| **`vol_term_structure(+/-)`** | +1 | **119** | 0.345 | 0.433 | **−8.8pp** | 0.063 | n | −7.6 | −10.3 |
| `cum_flow_intent(+1)` | −1 | 113 | 0.407 | 0.416 | −0.9pp | 0.925 | n | +4.4 | −8.4 |
| `cum_flow_intent(+1)` | +1 | 95 | 0.432 | 0.411 | +2.1pp | 0.756 | n | +2.1 | +2.3 |
| `multileg_structure(+2)` | +2 | 89 | 0.393 | 0.418 | −2.5pp | 0.716 | n | −0.8 | −4.9 |
| `cum_flow_intent(+1)` | −3 | 67 | 0.448 | 0.410 | +3.8pp | 0.609 | n | +2.0 | +5.3 |
| `sector_persistence(+1)` | +1 | 52 | 0.423 | 0.413 | +1.0pp | 0.994 | n | −1.6 | +2.7 |
| `signal_confluence(+1)` | +2 | 46 | 0.391 | 0.416 | −2.5pp | 0.852 | n | +14.4 | −9.5 |
| **`accumulation_conjunction(+3)`** | +1 | 46 | 0.457 | 0.411 | +4.6pp | 0.625 | n | +5.2 | +3.7 |
| `cum_flow_intent(+1)` | +3 | 42 | 0.476 | 0.409 | +6.7pp | 0.467 | n | — | +7.4 |
| `dealer_dex_flip(+1)` | +1 | 42 | 0.476 | 0.409 | +6.7pp | 0.467 | n | +2.4 | +15.5 |
| `dealer_dex_flip(+1)` | +3 | 31 | 0.355 | 0.418 | −6.3pp | 0.603 | n | −30.4 | +3.3 |
| `oi_trend_building(+1)` | +3 | 22 | 0.455 | 0.413 | +4.2pp | 0.847 | n | +17.3 | −18.0 |
| `earnings_catalyst(+/-)` | +1 | 19 | 0.368 | 0.416 | −4.7pp | 0.862 | n | — | −7.7 |
| **`accumulation_conjunction(+3)`** | +3 | 14 | 0.429 | 0.414 | +1.5pp | 1.000 | n | — | +0.4 |
| `dealer_dex_flip(+1)` | +2 | 9 | 0.667 | 0.410 | +25.6pp | 0.223 | n | — | — |
| `vol_term_structure(+/-)` | 0 | 9 | 0.556 | 0.412 | +14.3pp | 0.585 | n | — | — |
| `sector_persistence(+1)` | 0 | 8 | 0.000 | 0.420 | −42.0pp | 0.025 | n | — | −43.9 |

**Zero components survive BH.** The smallest p is 0.025 on an n=8 line
(`sector_persistence` awarded 0 points, 0-for-8) — one expected false positive in an 18-test
sweep, and it is a *zero-point* line, i.e. not a weight at all.

Reading the table as a market-maker: **no frozen weight is earning its points, and none is
demonstrably wrong either.** The three largest-N lines land at +1.1pp (n=142), −8.8pp (n=119)
and −0.9pp (n=113). The **+3 accumulation conjunction** — the single heaviest weight in the
rubric — contributes **+4.6pp at n=46 (p=0.625)** when it awards +1 and **+1.5pp at n=14**
when it awards its full +3. A three-point line producing a statistically indistinguishable
1.5pp is the clearest expression of the tier inversion in Phase 3: the rubric's biggest bet
is not connected to outcomes.

**`vol_term_structure` is the one line worth pre-registering against.** −8.8pp on n=119, the
largest coherent negative in the table, **and it is negative in both tapes** (−7.6 up /
−10.3 down) — so it is not a denominator effect. It is also the rubric line fed by the tools
that Phase 4 scored NEGATIVE (`options-structure term-skew` −7.2pp n=71,
`options-structure front-end-iv-ratio` −7.3pp n=26) and it feeds the classes Phase 3 found
most overconfident (`earnings_vol` 0.87→0.394, `high_iv_rank` 0.79→0.481). Three independent
phases point at the vol-term-structure lane. It still does not survive BH (p=0.063) and it
**does not get an edit** — it gets a pre-registration (C57 below).

`dealer_dex_flip` is genuinely unstable: +25.6pp at [+2] (n=9), +6.7pp at [+1] (n=42), −6.3pp
at [+3] (n=31, and −30.4pp in the up tape). A line whose sign depends on how many points it
awards is measuring something other than what it claims.

## 5.2 Per-source-agent contribution (regime-stratified)

| agent | n | WR | marginal | by regime |
|---|---|---|---|---|
| `signal-confluence-quant` | 345 | 0.429 | +3.7pp | up 0.45(143) · pull 0.48(58) · choppy 0.41(44) · trans 0.38(100) |
| `earnings-scout` | 93 | 0.366 | −5.8pp | up 0.45(42) · pull 0.31(16) · choppy 0.45(11) · **trans 0.21(24)** |
| `multileg-strategist` | 91 | 0.385 | −3.5pp | up 0.32(28) · pull 0.40(20) · choppy 0.46(13) · trans 0.40(30) |
| `sector-rotation-strategist` | 90 | 0.389 | −3.0pp | up 0.47(40) · pull 0.38(8) · choppy 0.46(13) · **trans 0.24(29)** |
| `accumulation-hunter` | 86 | 0.453 | **+4.6pp** | up 0.48(48) · pull 0.38(21) · choppy 0.50(8) · trans 0.44(9) |
| `vol-surface-scout` | 86 | 0.384 | −3.6pp | up 0.38(37) · pull 0.31(16) · choppy 0.44(9) · trans 0.42(24) |
| `dealer-positioning-strategist` | 85 | 0.435 | +2.5pp | up 0.54(39) · pull 0.36(25) · choppy 0.29(7) · trans 0.36(14) |
| `sweep-tracker` | 41 | 0.488 | **+7.9pp** | up 0.48(21) · pull 0.60(5) · choppy 0.60(5) · trans 0.40(10) |
| `opex-pin-strategist` | 11 | 0.182 | **−23.7pp** | up 0.22(9) |

`sweep-tracker` (+7.9pp) and `accumulation-hunter` (+4.6pp) are the only positive contributors
above n=40, and both are positive in **every** populated regime bucket — the most consistent
signal in this phase, though neither is BH-tested here and neither clears N for a P0.
`opex-pin-strategist` at 0.182 on n=11 mirrors the `opex_pin` class result (0.111 on n=9,
Phase 3) — pins resolve as LOSS on any ±1R breach and the agent is being graded on a rule its
structures (iron flies, short straddles) are not designed to satisfy. **This is a resolution-
method mismatch, not necessarily agent failure** — flagged as a method item, not a subject one.

> **⚠ CONFIRMED (applied 2026-08-15, post-publication — C59 resolved in-cycle).** The suspicion
> above is now measured. Re-resolving the 9 pin rows on the **settlement** rule (distance from
> entry at window end) instead of the **touch** rule gives **0.667 vs 0.111, with 5 of 9 rows
> diverging** — past C59's ≥3 bar. **PFE settled at 0.00% from entry and was scored LOSS**; XLF
> 0.05%, NVDA 0.12% / 0.21%. So the **−23.7pp on `opex-pin-strategist` is not an agent finding
> and must not be cited as one** — it is the auditor grading a band-profit structure on a
> breakout rule. This is the only agent row in the table affected; the rest resolve
> directionally, where the touch rule is correct.

## 5.3 Tier-cut monotonicity vs the frozen cuts

Frozen cuts: **HIGH ≥9 / MEDIUM 7–8 / LOW 3–6 / DROP ≤2.**

| band | n | WR |
|---|---|---|
| DROP (≤2) | 428 | 0.411 |
| LOW (3–6) | 117 | 0.419 |
| MEDIUM (7–8) | 14 | 0.500 |
| HIGH (≥9) | 13 | **0.385** |

**Monotone ascending DROP→HIGH? NO** — `[0.411, 0.419, 0.500, 0.385]`. The ladder rises
correctly through MEDIUM and then falls off a cliff at the top band. Eighth cycle of a
non-monotone top.

**Post-freeze only** (`rubric_version 2026-06-12`, n=425 decided):

| band | n | WR |
|---|---|---|
| DROP (≤2) | 368 | 0.399 |
| LOW (3–6) | 56 | 0.393 |
| MEDIUM (7–8) | **1** | 1.000 |
| HIGH (≥9) | **0** | — |

## 5.4 Freeze-lift grading — **UNRUNNABLE, 9th consecutive cycle**

The P0.1 freeze-lift condition is "≥30 resolved post-2026-06-12 calls, then grade tier
monotonicity." The first half is satisfied **14× over: 425 resolved post-freeze calls.**
The second half cannot be evaluated: **0 decided HIGH and 0 decided MEDIUM by tier label**
(1 row in the 7–8 raw-score band). Post-freeze the rubric emits 461 DROP and 60 LOW and
nothing else; the entire corpus contains **one** `full`-sized call.

This must be stated precisely, because it has been mis-framed in past cycles: **the freeze is
not what blocks the lift.** The freeze fixes weights and cuts; it does not prevent a name from
scoring ≥7. What prevents it is the rubric's own conjunction structure — the +3 accumulation
conjunction and the two-distinct-agent entry requirement — which in 521 post-freeze rows has
never co-fired hard enough to clear 7. **Lifting the freeze would not produce the evidence the
lift requires.** Keep the freeze; the blocker is upstream of it.

## 5.5 P0.6 out-of-regime half-cap — grading (6th measurement)

| | n | WR |
|---|---|---|
| out_of_regime | 43 | 0.326 |
| in_regime | 529 | 0.422 |

**Δ = −9.6pp; the cap is PROTECTIVE.** Negative in all six measurements taken to date
(the margin has compressed from earlier cycles but has never changed sign). **Keep the
half-cap.**

## 5.6 Pre-registrations emitted (no edits)

**C57 — `vol_term_structure` line contributes negatively.**
`{rubric_line: vol_term_structure(+/-1); direction: reduce magnitude toward 0 or invert sign;
mechanism claim: the line is fed by tools independently scored NEGATIVE (Phase 4:
term-skew −7.2pp n=71, front-end-iv-ratio −7.3pp n=26) and feeds the two most overconfident
classes in Phase 3 (earnings_vol, high_iv_rank); acceptance bar: cross-regime ∧ n ≥ 30 per
tape arm ∧ BH-surviving at FDR 0.10; decision window: audits 2026-09-05 → 2026-10-31}`.
Current evidence: −8.8pp, n=119, p=0.063, negative in both arms — **short of the bar**.

**C58 — `dealer_dex_flip` weight is unstable in its points-awarded direction.**
`{rubric_line: dealer_dex_flip(+1); direction: collapse to a single fixed +1 award, removing
the multi-point escalation path; mechanism claim: measured contribution reverses sign with
points awarded (+25.6pp at [+2] n=9, +6.7pp at [+1] n=42, −6.3pp at [+3] n=31 incl. −30.4pp
up-tape), which is incompatible with a monotone weight; acceptance bar: cross-regime ∧ n ≥ 30
per award level ∧ BH-surviving; decision window: audits 2026-09-05 → 2026-11-30}`.

**C59 (method, not subject) — `opex_pin` resolution-rule mismatch.**
`{target: auditor Phase-2 resolution map; direction: resolve pin structures on
pin-distance-at-expiry rather than ±1R breach; mechanism claim: iron flies / short straddles
profit from *staying inside* a band, so a ±1R touch that reverts is scored LOSS while the
structure would have paid; evidence: opex_pin class 0.111 (n=9), opex-pin-strategist −23.7pp
(n=11) — an implausible magnitude for a mechanical, well-specified lane; acceptance bar:
re-resolution of the existing 9 rows under both rules, showing divergence ≥ 3 rows;
decision window: next audit}`. This is an **auditor-method** pre-registration and does not
touch the frozen rubric.

**No weight edit, no cut re-bin, and no gate-membership change is emitted by this phase.**

**Output:** `phase_5_schema.jsonl`.
