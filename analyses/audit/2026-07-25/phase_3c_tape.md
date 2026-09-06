# Phase 3c — The down-tape experiment (2026-07-25, NEW)

Every audit since 2026-06-27 has pre-registered the same test and been unable to run it:
*does the book's directional selection add anything in a falling tape, or is the long
edge pure beta?* It could not run because the regime **label** is uninformative — 170
rows carry the bare string `TRANSITIONAL` across a period containing both tapes.

**Method.** Stratify by the **realised tape**: the sign of SPY's close-to-close return
over each row's own resolution window. This is a conditioning variable for an audit
statistic ("what did the tape do while this trade was live"), not a tradeable signal, and
must never be used as one.

Result: **159 decided rows in an UP tape, 281 in a DOWN tape** (median SPY window move
+0.93% vs −1.22%). The experiment finally has both arms.

## 1. The book, by tape

| tape | n | book WR | excess | median SPY window |
|---|---|---|---|---|
| UP | 159 | 0.440 | +10.9pp | +0.93% |
| DOWN | 281 | 0.416 | −1.0pp | −1.22% |

## 2. Directional selection conditioned on realised tape

| tape | dir | n | book WR | SPY WR | excess |
|---|---|---|---|---|---|
| UP | long | 62 | 0.500 | 0.274 | **+22.6pp** |
| UP | short | 57 | 0.421 | 0.439 | −1.8pp |
| DOWN | long | 124 | 0.371 | 0.306 | +6.5pp |
| DOWN | short | 73 | 0.507 | 0.644 | **−13.7pp** |

### Paired significance (McNemar exact on discordant pairs, BH FDR 0.10)

Each row carries *both* its own outcome and the same-window SPY outcome, so the correct
test is paired — not the two-sample comparison prior audits used.

| cell | n | book-only wins | SPY-only wins | p | BH |
|---|---|---|---|---|---|
| UP / long | 62 | 18 | 4 | **0.0043** | **YES** |
| ALL / long | 186 | 43 | 21 | **0.0081** | **YES** |
| DOWN / short | 73 | 12 | 22 | 0.1214 | no |
| DOWN / bearish_flow | 57 | 10 | 17 | 0.2478 | no |
| DOWN / long | 124 | 25 | 17 | 0.2800 | no |
| UP / short | 57 | 9 | 10 | 1.0000 | no |
| ALL / short | 130 | 21 | 32 | 0.1690 | no |

**Only the long book survives BH**, and mostly in the up-tape. The short book's
down-tape underperformance is directionally clear (22 discordant pairs against, 12 for)
but **not statistically significant at n=73** — state it as suggestive, not established.

## 3. Did the book pick the right side of the tape?

| tape | n | positioned WITH the tape |
|---|---|---|
| UP | 120 | 63 / 120 = **52.5%** |
| DOWN | 209 | 83 / 209 = **39.7%** |

In a falling tape the fleet was net-**long** six times out of ten. Combined with the
DOWN/short cell above: when the tape fell, the system both leaned the wrong way *and*
its deliberately-selected shorts underperformed a naive index short.

## 4. Empty-board discipline, by tape

| tape | DROP pile | traded book | sized book |
|---|---|---|---|
| UP | 0.462 (n=130) | 0.345 (n=29) | 0.483 (n=29) |
| DOWN | 0.411 (n=197) | 0.429 (n=84) | **0.294 (n=17)** |

**On a falling tape the sized book is the worst pile in the system — 0.294 against a
DROP pile of 0.411, an 11.7pp gap.** The 19-straight-empty-board discipline is not
timidity; on this data it is the single most profitable decision the fleet makes. n=17
sized is thin, so treat the magnitude as indicative and the sign as consistent with
every prior audit.

## 5. Post-freeze, by tape

| tape | n | WR | excess |
|---|---|---|---|
| UP | 132 | 0.447 | +15.2pp |
| DOWN | 161 | 0.379 | −8.3pp |

## Desk read

The experiment ran and the answer is unflattering but narrow. The **long book has a
BH-surviving edge over a same-window SPY long** (p=0.008 overall, p=0.004 in the up-tape)
— that is the one real, replicated, statistically defensible finding in this audit. The
**short book has never demonstrated alpha in any audit**, and in the falling tape it
finally exists in size to test, it trails a naive index short by 13.7pp on a sign that
does not clear significance.

Read this against Phase 3d before acting on any of it: three of the four class-level
"excess" swings that motivated this experiment turned out to be the denominator moving.
What survives that correction is the paired long result — because McNemar tests the
book against its own row-matched benchmark rather than against a stratum average.

Output: `phase_3c_tape.jsonl`, `phase3c_tape.py`.
