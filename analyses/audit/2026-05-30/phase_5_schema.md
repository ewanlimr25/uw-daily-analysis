# Phase 5 — Grading-Schema Critique (2026-05-30)

## A. Component re-weight → **DEFERRED** (was a 05-29 P0/P1)

The 2026-05-29 run proposed specific re-weights (cut `cumulative-premium-flow` +3→+1, add a
`+2 sweep-persistence` line, demote `term-skew`). **Phase 4 of THIS run invalidates the data those
re-weights stood on:**

- `term-skew` flipped −13.4 → **+7.9pp** (the "demote term-skew" rec is retracted);
- `oi-trend` (+12.2 → +0.4), `signal-confluence` (+17.2 → −1.0), `hot-chains sweep-persistence`
  (+19.5 → −2.6) all **collapsed to NO-INFO** — the proposed `sweep-persistence`/`oi-trend`
  additions carry no signal under path-aware resolution;
- **zero tools survive Benjamini-Hochberg.**

Re-weighting a fixed-budget additive rubric on MCs that move 15–30pp with the resolution method —
and that are BH-insignificant on reconstructed citations — is **chasing noise**. **No component
re-weight is proposed this run.** (Only the durable `cumulative-premium-flow` = NO-INFO at n=96
survives as a *direction*, and even that is P1/P2, not P0 — Phase 7.)

## B. Tier-cut audit — per-integer realised WR

| Score | 0–1 | 3 | 4 | 5 | 6 | 7 | 8 | **9** | 10 | 11 | 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| WR | 54–75% | 53% | 47% | 47% | 58% | 54% | 53% | **79%** | 75% | 75% | 100% |
| n | 17 | 38 | 43 | 51 | 33 | 26 | 17 | **14** | 8 | 4 | 2 |

**The lift is sharp and starts at score 9** (79%, n=14). Scores 4–8 are a 47–58% plateau (noise);
scores ≥9 jump to ~77%. This **confirms the Phase-3 Q5 finding** (score ≥7 quintile = 69.6%) and
sharpens it: the real conviction signal lives at **≥9**.

| Cut (HIGH≥hi / LOW<lo) | HIGH | MED | LOW | Monotone? | HIGH−MED gap |
|---|---|---|---|---|---|
| Current (≥10 / <3) | 76.5% (n17) | 52.7% (n222) | 56.0% (n25) | ❌ MED<LOW | +23.8 |
| **≥9 / <4** | **77.4% (n31)** | 50.6% (n170) | 54.0% (n63) | ❌ MED<LOW | **+26.8** |
| ≥8 / <4 | 68.8% (n48) | 50.3% (n153) | 54.0% (n63) | ❌ MED<LOW | +18.4 |

**No cut achieves monotonicity** — because **LOW (54–56%) always beats MED (50–53%)**. This is the
key structural finding and it is NOT a cut problem:

> The lowest-scored calls realise *more* than the mid-scored calls because the **alpha-generating
> shorts** (`bearish_flow`, +21pp excess) score *low* on the additive rubric, while the
> **beta longs** (`bullish_flow`/`dark_pool_accumulation`, −20pp excess) score in the middle. The
> rubric awards points for long-side flow evidence that is beta, and under-scores the short
> selection that is alpha. **The tier inversion and the negative-long-excess finding (Phase 3d)
> are the same defect.** Re-binning cuts cannot fix a score that is inversely correlated with edge.

## C. Holdout stress-test → **INCONCLUSIVE (cannot validate)**

| | HIGH | MED | LOW |
|---|---|---|---|
| Train (18 reports, n=260) @ ≥9/<4 | 77.4% (n31) | 51.5% (n167) | 53.2% (n62) |
| Holdout (recent 4 reports, n=**4**) | **n/a (n0)** | 0.0% (n3) | 100.0% (n1) |

The most-recent 20% of reports are almost entirely **window_open** (this week's swings/LEAPs) →
only **4 decided calls, 0 HIGH** in the holdout. Same blocker as 05-29: **the HIGH tier cannot be
validated out-of-sample** until this week's calls resolve (~2026-06-12).

## Verdict

- **Raising the HIGH cut 10→9** is supported in-sample (captures the clean 77% score-9 cohort) but
  **ACCEPT_WITH_CAVEAT** — holdout has 0 HIGH calls. **P1-pending-holdout**, identical posture to
  05-29 (this is the one 05-29 schema rec that survives re-evaluation, because it's outcome-driven,
  not tool-driven).
- **The MED<LOW inversion is a rubric-DIRECTION defect, not a tier-cut defect.** The additive score
  rewards beta-long evidence and under-weights alpha-short selection. **Fix the directional weighting
  (or split long/short scoring), don't re-bin.** This is the deepest schema finding of the run and it
  is **new** — the 05-29 run mis-attributed the inversion to tier cuts.
- **All component re-weights DEFERRED** (Phase 4 instability + BH-null + reconstructed citations +
  single regime). Revisit after ~2026-06-12 with verbatim-envelope provenance and resolved HIGH calls.

## Output
- `phase_5_schema.jsonl` — per-score WR, cut grid, holdout numerics. `phase5_schema.py` — reproducible.
