# Phase 7b — Pre-application design test of P0 #1 (2026-08-30)

**Status: the P0's FINDING is unchanged and confirmed. Its proposed MECHANISM was falsified
here, before shipping, and replaced.**

Phase 7 P0 #1 proposed an **expansion-veto**: allow short-vol structures only when the name
is not already expanding, testing (a) at-entry `rv10/rv30 ≤ 1.00` and (b) the name's ratio no
more than +0.15 above SPY's. Before writing that rule into an agent file it was tested against
the resolved corpus. **It failed.**

## Test

At-entry, look-ahead-free: annualized close-to-close RV over the 10 sessions **ending at the
entry bar** ÷ the same over 30 sessions (`scripts/market_data.py --rv-windows 10,30` computes
exactly this). Joined to `vol_short` outcomes.

### The absolute leg works, weakly and monotonically

| at-entry `rv10/rv30` | n | WR |
|---|---|---|
| [0.00, 0.85) | 36 | 36.1% |
| [0.85, 1.00) | 20 | 30.0% |
| [1.00, 1.15) | 34 | 23.5% |
| [1.15, ∞) | 38 | 23.7% |

Split at 1.00: contracting/flat **33.9% (n=56)** vs already-expanding **23.6% (n=72)** — +10.3pp
in the intended direction.

### The relative leg runs BACKWARDS

| name ratio − SPY ratio | n | WR |
|---|---|---|
| name calmer than SPY | 36 | **13.9%** |
| +0.00 … +0.15 hotter | 23 | 21.7% |
| **> +0.15 hotter** | 69 | **37.7%** |

The names that looked safest by the relative test were the worst. Shipping leg (b) would have
inverted the filter.

### The combined veto is net negative

| arm | n | WR |
|---|---|---|
| VETOED by the proposed rule | 94 | **31.9%** |
| ALLOWED by the proposed rule | 34 | **17.6%** |

**−14.3pp separation, wrong sign.** The proposed rule would have removed 73% of the lane and
kept the worse third.

## And no at-entry threshold rescues the lane

Absolute leg alone, strict windows, against the unselected same-date single-name peer
benchmark:

| arm | n | book | peers | excess | McNemar |
|---|---|---|---|---|---|
| ALL `vol_short` | 105 | 32.4% | 57.9% | −25.6pp | b=2 c=57, p<0.0001 |
| **ALLOWED (≤1.00)** | 45 | 37.8% | 59.0% | **−21.2pp** | **b=0 c=22, p<0.0001** |
| VETOED (>1.00) | 60 | 28.3% | 57.1% | −28.8pp | b=2 c=35, p<0.0001 |

Sweeping the threshold changes nothing material:

| cut | n | book | peers | excess |
|---|---|---|---|---|
| ≤ 0.70 | 8 | 25.0% | 61.6% | −36.6pp |
| ≤ 0.80 | 26 | 38.5% | 59.6% | −21.2pp |
| ≤ 0.90 | 39 | 35.9% | 59.7% | −23.8pp |
| ≤ 1.00 | 45 | 37.8% | 59.0% | −21.2pp |

**Every surviving arm is 21–37pp below its peer benchmark and every one has a McNemar
p < 0.0001.** The best filter available at entry leaves a book that still loses decisively
to doing nothing.

## Consequence

A filter cannot fix this lane, so the applied change is **routing, not filtering** — the same
remedy the 2026-08-01 P0 applied to directional shorts, and for the same reason: the deficit
is **mis-selection**, uniform across every conditioning variable tested, not mistiming that a
gate could catch.

`vol_short` / short-premium proposals route to **`watch_only`**: still generated, still
scored, still gate-verdicted, still serialized — so the counterfactual keeps resolving and
C63 can grade whether the lane recovers. `vol_long` is explicitly untouched (**+9.5pp**,
McNemar p=0.0034, 5-for-5 on sized rows).

**Method note for future cycles.** The Phase-7 recommendation was written from a correct
finding and a plausible-sounding mechanism. The mechanism was wrong, and only a test caught it.
**Test the proposed remedy against the corpus before writing it into an agent file**, not just
the finding that motivated it.
