# Phase 3c — Tape-conditioned book WR (C49 primary) — 2026-08-01

Tape = realised SPY close-to-close direction over **each row's own resolution window**,
so a row is graded against the market it actually lived through.

## Tape split

| tape | n | book WR | excess | median SPY window |
|---|---|---|---|---|
| UP | 232 | 0.457 | +1.2pp | +0.93% |
| DOWN | 269 | 0.416 | +0.5pp | −1.20% |

Both tapes exist in size for a second consecutive audit (07-25: 159/281). The book's own
win rate moves only **4.1pp** between a rising and a falling market — the stationarity
that C49 predicts and that the excess column hides.

## Direction × tape

| tape | dir | n | book WR | spy WR | excess |
|---|---|---|---|---|---|
| UP | long | 78 | 0.487 | 0.308 | **+17.9pp** |
| UP | short | 92 | 0.402 | 0.533 | −13.1pp |
| DOWN | long | 126 | 0.365 | 0.278 | +8.7pp |
| DOWN | short | 71 | 0.535 | 0.676 | −14.1pp |

The long book carries positive excess in **both** tapes; the short book carries negative
excess in **both**, and by nearly the same magnitude (−13.1 / −14.1). See Phase 3 §3.4 —
the paired McNemar makes `ALL / short` significant at p=0.0115.

## Direction-call accuracy

| tape | n | positioned WITH tape | rate |
|---|---|---|---|
| UP | 174 | 81 | **46.6%** |
| DOWN | 197 | 71 | **36.0%** |

The fleet is positioned against the tape more often than with it in **both** regimes, and
badly so in a falling one (36.0%). It is structurally long-biased into down-tape — 126 of
197 down-tape directional rows were longs. This is the mechanism behind the DOWN/long
cell's thin 0.365 book WR.

## `bearish_flow` by tape (the C19/C53 line)

| tape | n | WR | spy WR | excess |
|---|---|---|---|---|
| UP | 49 | 0.449 | 0.592 | −14.3pp |
| DOWN | 57 | 0.544 | 0.667 | −12.3pp |

Book WR moves 9.5pp; excess moves 2.0pp — and both are **negative in both tapes**. The
07-11 "+29.4pp bearish edge" and 07-18 "the sign reversed" headlines have now been
contradicted by two consecutive windows measured the row-matched way. **C53's closure of
C19 as REFUTED is confirmed, not merely unrebutted.**

## Post-freeze only, by tape

| tape | n | WR | excess |
|---|---|---|---|
| UP | 205 | 0.463 | +2.7pp |
| DOWN | 149 | 0.376 | −5.2pp |

## DROP pile vs traded book, by tape

| tape | DROP | book | sized |
|---|---|---|---|
| UP | 0.467 (199) | 0.394 (33) | 0.500 (30) |
| DOWN | 0.411 (185) | 0.429 (84) | **0.294 (17)** |

The sized book is again the **worst pile in the system in a falling tape** (0.294 vs a
DROP pile of 0.411) — an exact replication of the 07-25 reading (0.294 vs 0.411). In a
rising tape sizing is fine (0.500). The fleet's sizing decision adds value only when the
market is going up, which is another statement of the same long-bias defect.

Output: `phase_3c_tape.jsonl`, `phase_3c_mcnemar.jsonl`.
