# Phase 5 — Grading the FROZEN Rubric (2026-08-01)

> **RUBRIC FREEZE — version `2026-06-12`.** This phase *grades*; it does not retune.
> No proposed-weight column, no re-binned cuts, no holdout refit. The only change output
> permitted is a pre-registration. Every table is stratified by `rubric_version`; eras are
> never pooled.

Provenance: 100% verbatim envelope. Regime strata: uptrend / pullback / choppy /
transitional_other, both tapes present.

## 5.1 Component-weight grading (frozen weights vs measured contribution)

`[+N]` is the frozen point value as emitted; `WRwith`/`WRw/o` are class-conditional.

| component line | pts | n | WR with | WR w/o | marginal | p | BH | UP tape | DN tape |
|---|---|---|---|---|---|---|---|---|---|
| `oi_trend_building` | +1 | 104 | 0.490 | 0.421 | +7.0 | 0.181 | no | +12.2 | +3.1 |
| `cum_flow_intent` | −1 | 97 | 0.402 | 0.443 | −4.1 | 0.479 | no | −2.2 | −6.6 |
| `vol_term_structure` | +1 | 96 | 0.396 | 0.444 | −4.9 | 0.393 | no | +3.8 | −11.2 |
| `multileg_structure` | +2 | 79 | 0.443 | 0.434 | +0.9 | 0.952 | no | +8.2 | −7.5 |
| `cum_flow_intent` | +1 | 75 | 0.453 | 0.432 | +2.1 | 0.793 | no | +0.3 | +3.6 |
| `cum_flow_intent` | −3 | 61 | 0.475 | 0.430 | +4.6 | 0.550 | no | +7.1 | +3.2 |
| `sector_persistence` | +1 | 49 | 0.449 | 0.434 | +1.5 | 0.937 | no | −0.8 | +3.6 |
| `signal_confluence` | +2 | 46 | 0.391 | 0.440 | −4.8 | 0.613 | no | +9.3 | −8.4 |
| `cum_flow_intent` | +3 | 42 | 0.476 | 0.431 | +4.5 | 0.663 | no | — | +8.3 |
| `accumulation_conjunction` | +1 | 42 | 0.452 | 0.434 | +1.9 | 0.922 | no | −1.3 | +4.6 |
| **`dealer_dex_flip`** | **+3** | 31 | 0.355 | 0.440 | **−8.6** | 0.438 | no | **−36.0** | +4.2 |
| `dealer_dex_flip` | +1 | 30 | 0.467 | 0.433 | +3.4 | 0.846 | no | −6.1 | +12.4 |
| `earnings_catalyst` | +1 | 19 | 0.368 | 0.438 | −6.9 | 0.713 | no | — | −6.8 |
| `oi_trend_building` | +3 | 19 | 0.474 | 0.434 | +4.0 | 0.896 | no | +18.8 | −17.1 |
| `accumulation_conjunction` | +3 | 14 | 0.429 | 0.435 | −0.7 | 1.000 | no | — | +1.3 |
| `dealer_dex_flip` | +2 | 9 | 0.667 | 0.431 | +23.6 | 0.276 | no | — | — |
| `sector_persistence` | 0 | 8 | 0.000 | 0.442 | −44.2 | 0.019 | no | — | −42.9 |

**Zero of 17 component lines survive BH at FDR 0.10.** This is the ninth consecutive
audit with that result and it is the entire justification for the freeze: six cycles of
re-weighting correlated lines on n=8–31 BH-null data produced the cum-flow +2→+3→+1
whipsaw, a realised false positive.

### Reads worth carrying

- **`dealer_dex_flip` at +3 remains tape-conditional and remains the most dangerous line
  in the rubric.** −36.0pp up-tape vs +4.2pp down-tape on n=31 — a 40pp swing between
  arms. The 07-25 reading was −34.9 / +4.1 on the same n. It has not moved, and it has
  not accumulated the n≥30-per-arm the C50 bar requires. The mechanized DEX-flip test
  fires rarely (twice on 07-24, both killed on flow conflict), so this line will take
  many more cycles to decide.
- **`accumulation_conjunction` +3 is flat.** +1.9pp at the +1 emission (n=42) and
  **−0.7pp at the +3 emission (n=14)**. The system's single heaviest weight has no
  measurable marginal contribution in either tape. C51 stays registered, unmet.
- `sector_persistence` at the 0-point emission reads −44.2pp on n=8 with a nominal
  p=0.019 that does **not** survive BH. Consistent with the Phase 3 `sector_rotation`
  finding (realised 0.25) and with the known turnover-vs-accumulation defect in the
  underlying tool. Not actionable at n=8; noted as corroboration.

## 5.2 Tier-cut grading vs frozen cuts (HIGH ≥9 / MED 7–8 / LOW 3–6 / DROP ≤2)

All eras pooled by raw score:

| band | n | WR |
|---|---|---|
| DROP (≤2) | 377 | 0.430 |
| LOW (3–6) | 97 | 0.454 |
| MED (7–8) | 14 | 0.500 |
| HIGH (≥9) | 13 | **0.385** |

Monotone ascending DROP→HIGH? **No** — `[0.430, 0.454, 0.500, 0.385]`. The first three
bands are correctly ordered; the top band inverts. That is the same shape as the
tier-reliability table in Phase 3 §3.2, and it is the fifth consecutive re-confirmation
that **the ≥9 HIGH cut selects the worst names in the book.**

Post-freeze only:

| band | n | WR |
|---|---|---|
| DROP (≤2) | 317 | 0.420 |
| LOW (3–6) | 36 | 0.472 |
| MED (7–8) | 1 | 1.000 |
| HIGH (≥9) | **0** | — |

## 5.3 Freeze-lift check

Post-freeze resolved calls: **354** — far past the ≥30 trigger. But the tier distribution
is **0 HIGH / 0 MEDIUM / 42 LOW / 385 DROP**.

**The freeze-lift test cannot run for a 7th consecutive cycle.** It is not unsatisfied —
it is *structurally unrunnable*, because the grading evidence a lift requires (HIGH and
MEDIUM tier monotonicity under the frozen weights) cannot exist while the frozen rubric
emits neither tier. **Recommendation: KEEP the freeze.**

This is worth stating plainly rather than repeating as a formality: the frozen rubric has
now run for seven weeks and produced **one** `full`-sized call in the entire corpus. The
freeze is not blocking a lift; the rubric's own conjunction requirements are.

## 5.4 P0.6 out-of-regime half-cap

| arm | n | WR |
|---|---|---|
| out_of_regime | 43 | 0.326 |
| in_regime | 458 | 0.445 |

**Δ = −12.0pp on n=43** — past the actionable floor, and negative in **every audit that
has ever measured it** (−16.7pp at 06-27, −14.3pp at 07-18, −11.9pp at 07-25, −12.0pp now).
The cap is doing exactly what it was built to do. **KEEP.**

Secondary: `rubric_regime` gated rows 0.413 (n=201) vs ungated 0.450 (n=300) — the gate
also correctly identifies weaker names.

## 5.5 Pre-registrations

Carried forward, none cleared this cycle:

- **C50** — `dealer_dex_flip +3` is tape-conditional (−36.0pp UP / +4.2pp DOWN, n=31).
  **Bar:** n≥30 *per tape arm*, BH-surviving, both arms same sign. **Window:** open.
- **C51** — `accumulation_conjunction +3` measures +1.9pp (n=42, +1 emission) and −0.7pp
  (n=14, +3 emission). **Bar:** n≥30 per arm across ≥2 regimes, BH-surviving. **Window:** open.
- **C52** — short-side selection has no alpha in any tape. **Status: this cycle's paired
  McNemar promotes C52 from "suggestive" to met** — see §5.6.

New this cycle:

- **C55** — `sector_rotation` class realises 0.25 (n=32) against a 0.54 claim,
  BH-surviving at p=0.002, corroborated by `sector_persistence`'s 0-point emission at
  −44.2pp (n=8). Hypothesis: the class's evidence line reads `sector-flow-persistence`,
  a **gross-turnover** metric, as though it were net accumulation. **Direction:** demote
  the `sector_persistence +1` line to 0 and re-source the class off
  `market-regime.sector_rotation` (the only netted source). **Bar:** cross-regime,
  n≥30 per arm, BH-surviving. **Decision window:** ≥2 future audits.
- **C56** — the `[0.55,0.65)` win-rate band is anti-predictive (realised ≈0.29 on n=34
  against ~0.58 predicted) and is now the **modal** emission (73.3% of post-fix quotes).
  The 07-25 sizing floor bound the *size* but not the *quote*. **Direction:** re-derive or
  suppress the quote itself in that band. **Bar:** n≥30 post-fix quoted rows.
  **Decision window:** next audit.

**No weight or cut edit is emitted from this phase.** Pre-registrations only, per the freeze.

## 5.6 C52 — short-side selection (bar now met)

The 07-25 registration required "a second independent down-tape" before the short-side
finding could be called. This cycle supplies it, and the row-matched test is now
significant rather than suggestive:

- `ALL / short` paired McNemar **p=0.0115, BH-surviving**, b=24 vs c=46 (n=163).
- Negative in both tapes and by nearly identical magnitude: UP −13.0pp, DOWN −14.1pp.
- Direction-call accuracy 46.6% up-tape / **36.0%** down-tape.
- Sized book in a falling tape **0.294** vs a DROP pile of 0.411 — replicated exactly
  from 07-25.

**C52 is met.** The finding is: the fleet's short *selection* destroys value relative to a
naive same-window index short, and the defect is regime-independent. It is carried into
Phase 7 as the cycle's leading recommendation.

Output: `phase_5_schema.jsonl`, `phase5_schema.py`.
