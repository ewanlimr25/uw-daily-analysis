# Phase 5 — Grading the FROZEN Rubric (2026-08-30)

> **RUBRIC FREEZE, version `2026-06-12`.** This phase grades; it does not retune. No weight,
> no cut, no gate membership is proposed as an edit. Every table is stratified by
> `rubric_version`; eras are never pooled. The only change output permitted here is a
> **pre-registration**, or the **decision of a registration whose window has opened**.

## 5.1 Frozen component grading (per-line marginal, both tape arms, BH within the 24-line family)

| component line | pts | n | WR with | WR w/o | marginal | p | BH | UP | DOWN |
|---|---|---|---|---|---|---|---|---|---|
| **`vol_term_structure(+/−)`** | +1 | **150** | 0.280 | 0.414 | **−13.4** | **0.001** | **Y** | **−10.7** | **−16.4** |
| `oi_trend_building(+1)` | +1 | 194 | 0.381 | 0.387 | −0.5 | 0.942 | n | +4.6 | −5.7 |
| `cum_flow_intent(+1)` [−1 arm] | −1 | 145 | 0.379 | 0.387 | −0.8 | 0.924 | n | +4.8 | −6.9 |
| `multileg_structure(+2)` | +2 | 108 | 0.407 | 0.381 | +2.6 | 0.640 | n | +7.6 | −3.4 |
| `cum_flow_intent(+1)` [+1 arm] | +1 | 105 | 0.429 | 0.378 | +5.1 | 0.328 | n | +4.5 | +5.9 |
| `cum_flow_intent(+1)` [−3 arm] | −3 | 79 | 0.443 | 0.378 | +6.5 | 0.281 | n | +9.7 | +3.4 |
| `sector_persistence(+1)` | +1 | 55 | 0.418 | 0.382 | +3.6 | 0.678 | n | +2.0 | +4.3 |
| `accumulation_conjunction(+3)` [+1] | +1 | 51 | 0.431 | 0.382 | +5.0 | 0.552 | n | +4.7 | +5.0 |
| `dealer_dex_flip(+1)` [+1] | +1 | 47 | 0.489 | 0.378 | +11.2 | 0.156 | n | +5.4 | +18.4 |
| `signal_confluence(+1)` [+2] | +2 | 46 | 0.391 | 0.385 | +0.6 | 1.000 | n | +17.8 | −6.2 |
| `cum_flow_intent(+1)` [+3] | +3 | 42 | 0.476 | 0.379 | +9.7 | 0.258 | n | — | +10.0 |
| `dealer_dex_flip(+1)` [+3] | +3 | 31 | 0.355 | 0.387 | −3.2 | 0.868 | n | −26.8 | +6.0 |
| `earnings_catalyst(+/−)` | +1 | 29 | 0.345 | 0.387 | −4.2 | 0.793 | n | −4.0 | −5.2 |
| `oi_trend_building(+1)` [+3] | +3 | 29 | 0.483 | 0.381 | +10.2 | 0.348 | n | +19.9 | −1.5 |

(Lines with n < 16 are in `phase_5_schema.jsonl`; none inform a recommendation.)

**One BH survivor and it is the same line C60 named.** `vol_term_structure(+/−)` awards a
point, and rows carrying that point realise **0.280 against a 0.414 book** — negative in
**both** tape arms and, on the wider component-join, negative across **all four lanes it
touches**: `vol_short` 0.275 (n=91) · `vol_long` 0.342 (38) · `long` 0.393 (28) · `short`
0.231 (26). The lane story from Phase 3.2 does not fully absorb it: even inside `vol_long`,
which beats its peer benchmark by +9.5pp, carrying this component costs ~10pp.

## 5.2 **C60 — statistical bar CLEARED, registration NOT decided. Hold.**

Registered 2026-08-22. Bar: cross-regime (≥3 populated buckets) **AND** n ≥ 30 per tape arm
**AND** BH-surviving at FDR 0.10 within the component family. Decision window:
**2026-10-03 audit or later.**

| condition | required | measured | status |
|---|---|---|---|
| BH-surviving in component family | FDR 0.10 | p=0.001, **sole survivor of 24** | ✅ |
| n per tape arm | ≥ 30 | UP **89** (0.292) / DOWN **94** (0.309) | ✅ |
| populated regime buckets | ≥ 3 | **4** — uptrend 91 (0.264), transitional 52 (0.288), choppy 21 (0.476), pullback 19 (0.316) | ✅ |
| decision window open | ≥ 2026-10-03 | **2026-08-30** | ❌ |

**All three statistical conditions pass. The registration is still not decided, and it must
not be.** Rows added since C60 was registered: **9 of 183 — 4.9% of the evidence is genuinely
out-of-sample.** The bar is being cleared by re-resolving the same rows that generated the
hypothesis with a week more forward data. That is exactly the self-grading failure the
decision window exists to prevent, and it is the same mechanism that produced the
cum-flow +2→+3→+1 whipsaw the freeze was imposed to stop.

**Recommendation: hold C60 to 2026-10-03 unchanged.** No re-registration, no threshold
adjustment, no interim half-measure — a registration that gets renegotiated when its numbers
look good is not a registration. On present trajectory it will clear on genuinely fresh data;
the desk should expect that and plan for it rather than front-run it.

## 5.3 Tier-cut monotonicity vs the frozen cuts (HIGH ≥9 / MED 7–8 / LOW 3–6 / DROP ≤2)

| band | n | WR |
|---|---|---|
| DROP (≤2) | 532 | 0.372 |
| LOW (3–6) | 134 | 0.425 |
| MED (7–8) | 14 | 0.500 |
| **HIGH (≥9)** | **13** | **0.385** |

**Monotone ascending DROP → MED, then breaks at the ≥9 cut** — the **10th consecutive failed
re-confirmation** of the HIGH cut. The ladder is well-behaved everywhere the rubric is not
claiming maximum confidence.

**Post-freeze:** DROP 0.358 (472) · LOW 0.411 (73) · MED 1.000 (**n=1**) · HIGH **n=0**.

**Freeze-lift check.** The skill requires grading the P0.6 half-cap and the lift when ≥30
resolved post-freeze calls accrue. 546 have accrued — but **0 decided HIGH and 1 decided
MEDIUM in 11 cycles**. The lift is **unrunnable an 11th time**, and the reason is not the
freeze: the fleet has produced no ≥9 call since 2026-06-12 under a rubric that was frozen
*after* the last one. Lifting the freeze would not create HIGH calls; it would only remove the
protection against re-fitting on the thin data that does exist. **Keep the freeze.**

## 5.4 P0.6 out-of-regime half-cap — **8th consecutive negative reading; KEEP**

| | n | WR | excess |
|---|---|---|---|
| out-of-regime (capped) | 43 | 0.326 | −23.5pp |
| in-regime | 650 | 0.389 | +2.4pp |

Δ = **−6.4pp**, ACTIONABLE at n=43. The cap is **protective**. Also: `rubric_regime` gated
rows 0.338 (n=355) vs ungated 0.435 (n=338). **No lift.**

## 5.5 Pre-registrations

### Open, carried unchanged

- **C60** — `vol_term_structure(+/−)`. Statistical bar met; **window opens 2026-10-03**. Hold.
- **C61** — `scripts/term_structure_hygiene.py`. **Non-August n = 7 of a required 30**
  (Phase 4.2); gained one row in a week. Open, and the confound has not improved.
- **C62** — float-normalized DP block at the fixed 0.0010 threshold. **11 of 30 decided,
  2 of a required 10 in the upper arm** (Phase 4.4). Emission starvation is fixed; the
  class's call rate is now the binding constraint. Open.
- **C56** — the `[0.55,0.65)` anti-predictive band. **21 of 30** post-fix decided rows,
  realised 0.190; **0 rows sized above starter, 14 cycles.** Open.

### New this cycle

### C63 — the vol lane's SHORT leg is adversely selected

```
subject:       vol_short trade PROPOSAL (procedure, not a rubric weight — freeze-safe)
direction:     require an independent expansion-veto before a short-vol structure may be
               proposed; or route vol_short to watch_only pending one
mechanism:     the scouts identify vol-EXPANSION candidates correctly (vol_long beats an
               unselected single-name peer benchmark by +9.5pp, McNemar p=0.0034, and is
               5-for-5 on sized rows). The same identification is then used to SELL vol
               into that expansion. Selected short-vol names run a mean RV ratio of 1.132
               against a same-date peer median of 0.962.
evidence now:  book 31.5% vs unselected same-date single-name peers 56.6% = -25.1pp on
               n=111 strict-window rows; paired McNemar vs the peer-median partner
               b=2 c=57, p<0.0001. 4 of 4 regime buckets negative and each individually
               significant (p=0.0018/0.0034/0.0020/0.0000). 3 of 4 months negative-
               significant. Loose-window: -33.6pp on n=134, BH-surviving in the
               pre-registered vol family. Survives three falsification attempts
               (tape, index-vs-single-name instrument bias, high-vol name selection) --
               the instrument-bias correction makes the deficit SMALLER but not absent,
               and the tape confound runs OPPOSITE to the excuse.
               EXPOSURE: 20 of the 48 sized rows in the entire corpus.
caveat:        resolution is the RV-direction proxy, not IV-vs-RV. The number prices
               SELECTION, never P&L. Closing this properly requires implied_move on
               every vol row (populated 153/789).
acceptance:    already cross-regime, row-matched and BH-surviving on n=111 -- this is
               NOT registered pending evidence. It is registered so that the FIX is
               graded: after a procedure change ships, vol_short's peer-excess must be
               >= -5pp on n >= 40 decided post-change rows across >= 2 regime buckets.
decision:      2026-10-03 audit or later (grading the fix, not the finding)
```

### C64 — pin resolution: switch the headline to the SETTLEMENT rule (auditor-method)

```
subject:       the AUDITOR's opex_pin resolver (method change, C59 successor)
evidence now:  C59's bar was >=3 of 9 divergent rows; measured 5 of 11. TOUCH rule 2/11
               (18.2%), SETTLEMENT rule 7/11 (63.6%) -- a 45.4pp swing on identical rows.
               Four of the five divergent names settled within 0.21% of entry after
               brushing a wing intraday. An iron fly / short straddle / butterfly pays on
               where price FINISHES.
change:        make outcome_settle the headline for resolution_mode == "pin"; retain the
               touch rule as outcome_touch for continuity with the prior 12 audits.
acceptance:    CLEARED by C59 this cycle. Ship in the auditor, not the subject.
decision:      DECIDED 2026-08-30
```

## Hard-rule compliance

No weight, cut, budget or gate membership was edited or proposed as an edit in this phase.
C60's cleared statistics are reported and explicitly **not** acted on.
