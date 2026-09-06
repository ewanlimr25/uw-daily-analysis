# Phase 3d — Is benchmark-excess measuring EDGE, or measuring SPY? (2026-07-25, NEW)

**This is the audit's headline finding, and it is a finding about the auditor.**

## The question

Three consecutive audits have led with the same claim: *"the benchmark-excess sign is
non-stationary — the edge depends on regime."*

| class | 2026-07-11 | 2026-07-18 | 2026-07-25 |
|---|---|---|---|
| `bearish_flow` excess | **+29.4pp** | −3.2pp | −10.8pp |
| long / accumulation excess | −29.2pp | **+10.8pp** | +3.5pp |

Each audit treated the flip as news about the *book*. There is a cheaper explanation
nobody tested: that the flip is news about the *benchmark*.

**H0 (artifact).** Book WR is roughly constant across strata; SPY's benchmark WR is what
moves; therefore `excess = bookWR − spyWR` is mechanically ≈ `−1 × spyWR + const`, and
the "non-stationarity" belongs to the denominator, not the numerator.

**Mechanism if H0 holds.** The resolver is a path-aware **first-touch** test against each
instrument's *own* 0.5 × ATR(14). Single names are more leptokurtic relative to their own
trailing ATR than a diversified index is, so names touch ±R at close to a coin-flip rate
in almost any tape. SPY's first-touch rate, by contrast, swings hard with drift. Excess
then tracks −spyWR by construction.

## Test

34 strata cells (n ≥ 8 each) spanning direction × tape, regime × direction, canonical
class, class × tape, tier, and rubric era. OLS of `excess_pp` on `spy_wr`.

```
OLS  excess_pp = +36.5 + (-80.0) * spy_wr
     slope = -80.0 pp per 1.00 of spyWR        [-100 == pure artifact]
     R^2   = 0.636
     sd(bookWR) = 0.1065   sd(spyWR) = 0.1670   dispersion ratio = 0.638
     book WR range = [0.182, 0.750]   spy WR range = [0.000, 0.800]
```

**Variance decomposition of the excess column: 71.1% of its variance is the benchmark
moving; 28.9% is the book.**

Implied **β(bookWR | spyWR) = 1 + slope/100 = +0.20** — the book's win rate absorbs only
a fifth of any move in the conditions that swing the index's first-touch rate.

### Robustness

| specification | cells | slope | R² | n-weighted slope | R² |
|---|---|---|---|---|---|
| all cells n≥8 | 34 | −80.0 | 0.636 | −77.5 | 0.748 |
| n≥15 | 31 | −83.8 | 0.741 | −78.5 | 0.777 |
| n≥25 | 26 | −88.2 | 0.771 | −80.3 | 0.793 |
| drop extreme spyWR (0.0 / 0.8) | 32 | −87.9 | 0.612 | −76.4 | 0.696 |
| non-overlapping cells only | 8 | −73.0 | 0.319 | −56.6 | 0.581 |

The result strengthens as cells get larger and survives dropping the extreme cells. The
weakest specification (8 non-overlapping cells) still returns −73.

## The money table

Same rows, split by realised tape. If the *book* were what moves, `|Δ book WR|` would be
large. It isn't.

| class | UP bookWR | DOWN bookWR | \|Δ book\| | UP excess | DOWN excess | \|Δ excess\| |
|---|---|---|---|---|---|---|
| bearish_flow | 0.533 | 0.526 | **0.7pp** | +3.3 | −12.3 | **15.6pp** |
| bullish_flow | 0.400 | 0.429 | **2.9pp** | +20.0 | +11.4 | **8.6pp** |
| dark_pool_accumulation | 0.400 | 0.400 | **0.0pp** | −13.3 | +10.0 | **23.3pp** |
| multileg_directional | 0.500 | 0.280 | 22.0pp | +25.0 | −8.0 | 33.0pp |
| **mean** | | | **6.4pp** | | | **20.1pp** |

**Three of four classes have a book win rate that does not move at all between rising
and falling tape, while their excess column moves 9–23pp.** The excess statistic
amplifies stratum noise 3.1×.

`multileg_directional` is the one class whose book *did* genuinely move (0.500 → 0.280).
That is a real regime effect and should be treated as the exception that proves the
method works when there is something to find.

## What this does and does not overturn

**Does not overturn.** Excess remains the right *concept* — a long book that wins 45% in
a tape where SPY-long wins 28% has done something. The C21 rationale stands.

**Does overturn.** Quoting a single-window excess number *as a finding about a signal
class* is not defensible when 71% of its variance is benchmark. Specifically:

1. The 2026-07-11 headline (`bearish_flow` +29.4pp, BH-surviving, "the down-tape edge")
   and the 2026-07-18 reversal headline were **substantially the same rows with a
   different denominator**. `bearish_flow`'s own win rate never moved.
2. **C19 (`single-leg` / bearish-flow accrual) should be closed, not merely blocked.**
   Six audits have logged "bearish_flow scores 0 while showing positive excess" as
   evidence of an unscoreable down-tape edge. Its book WR is 0.53 in both tapes and 0.49
   overall against a 0.48 claim. There is no edge to graduate — there was a benchmark.
3. Every prior "tool sign flipped window-to-window" finding (Phase 4, now eight
   consecutive BH-null tables) has the same candidate explanation.

## Recommended method fix (Phase 7, P0 — auditor only)

Report **book WR conditioned on tape** as the primary column and demote raw excess to a
secondary, with its benchmark WR printed beside it always. Add the
`sd(book)/sd(benchmark)` dispersion ratio to every excess table so a reader can see
whether a quoted excess is the book or the denominator. Registered as **C49**.

Output: `phase_3d_excess_artifact.jsonl`, `phase3d_excess_artifact.py`.
