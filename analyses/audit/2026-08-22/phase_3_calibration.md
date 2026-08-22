# Phase 3 — Calibration Audit (2026-08-22)

**Provenance: 100% verbatim envelope.** 637 decided rows, 228 of them carrying a
`claimed_win_rate` and an outcome. Eras never pooled where a rubric-era claim is made.

---

## C49 HEADER — read this before any excess sentence below

| statistic | value |
|---|---|
| strata cells (n ≥ 8) | 31 |
| `sd(book WR)` | 0.1110 |
| `sd(benchmark WR)` | 0.1508 |
| **dispersion ratio** | **0.736** |
| OLS `excess_pp = +29.8 − 69.7 × spy_wr` | **R² = 0.519** |
| implied β(bookWR \| spyWR) | +0.30 |
| **benchmark share of excess variance** | **51.9%** |

The wider Phase-3d cell set (36 cells incl. regime×direction) reads harder still: slope
**−86.0**, R² **0.640**, dispersion ratio **0.659**, benchmark share of excess variance
**69.7%**. Book WR ranges [0.200, 0.700] while SPY ranges [0.178, 0.778] — **the book is pinned
near coin-flip on its own ATR and the denominator does the moving.** Every excess number below
is therefore annotated and secondary; **the paired McNemar is the edge test.**

---

## 3.1 — Per-signal-class table (decided N ≥ 8, BH FDR 0.10)

| class | n | realised | claimed | div (pp) | spyWR | excess | p | BH |
|---|---|---|---|---|---|---|---|---|
| `earnings_vol` | 130 | **0.38** | **0.87** | **49.4** | 0.667 | −29.0 | <0.001 | **🚩** |
| `bearish_flow` | 122 | 0.45 | 0.50 | 5.4 | 0.595 | −14.4 | 0.273 | n |
| `multileg_directional` | 88 | 0.40 | 0.56 | **15.7** | 0.349 | +4.8 | 0.004 | **🚩** |
| `bullish_flow` | 61 | 0.43 | 0.52 | 9.3 | 0.279 | +14.8 | 0.187 | n |
| `dark_pool_accumulation` | 58 | 0.40 | 0.55 | **15.8** | 0.382 | +1.5 | 0.023 | **🚩** |
| `sector_rotation` | 48 | **0.29** | 0.54 | **24.4** | 0.244 | +4.7 | 0.001 | **🚩** |
| `high_iv_rank` | 30 | 0.47 | 0.77 | **30.5** | — | — | 0.001 | **🚩** |
| `dealer_positioning` | 29 | 0.52 | 0.60 | 7.9 | 0.448 | +6.9 | 0.491 | n |
| `oi_build` | 18 | 0.44 | — | — | 0.294 | +15.0 | 1.000 | n |
| `multi_day_sweep` | 11 | 0.64 | 0.38 | −25.7 | 0.300 | +33.6 | 0.152 | n |
| `gamma_breakout` | 10 | 0.20 | 0.51 | 31.1 | 0.600 | −40.0 | 0.094 | n |
| `event_vol` | 10 | 0.40 | — | — | 0.000 | +40.0 | 1.000 | n |
| `opex_pin` | 9 | 0.11 | — | — | — | — | 1.000 | n |

`THIN_N` appendix (decided 5–7, never headline): `vol_long` n=5, realised 0.00.

> **`opex_pin` 0.111 is a measurement artifact, not a finding** — C59 (cleared 2026-08-15)
> established 5-of-9 rows resolve as LOSS on a first-touch rule while settling ~0% from entry.
> Retained in the table for continuity; excluded from commentary.

---

## 3.2 — PRIMARY EDGE TEST: tape-conditioned book WR + paired McNemar

BH applied **within** the pre-registered family (7 direction × tape cells), not across the
exploratory class sweep — pooling would be a post-hoc power tax (2026-08-01 method note).

| cell | n | book WR | spy WR | Δ | b | c | p | BH | family |
|---|---|---|---|---|---|---|---|---|---|
| **ALL / long** | **252** | **0.421** | 0.282 | **+13.9pp** | 63 | 28 | **0.0003** | **YES** | primary |
| **DOWN / long** | 155 | 0.381 | 0.226 | **+15.5pp** | 39 | 15 | **0.0015** | **YES** | primary |
| **ALL / short** | **193** | **0.425** | 0.570 | **−14.5pp** | 27 | 55 | **0.0026** | **YES** | primary |
| DOWN / short | 79 | 0.506 | 0.684 | −17.7pp | 12 | 26 | 0.0336 | YES | primary |
| UP / short | 114 | 0.368 | 0.491 | −12.3pp | 15 | 29 | 0.0488 | YES | primary |
| UP / long | 97 | 0.485 | 0.371 | +11.3pp | 24 | 13 | 0.0989 | no | primary |
| ALL (both sides) | 445 | 0.422 | 0.407 | +1.6pp | 90 | 83 | 0.6484 | no | primary |

**Both durable results strengthened again this cycle.**

- **Long edge: 4th consecutive BH-surviving cycle, and its strongest reading yet** — p
  0.0220 (08-15) → **0.0003**, effect +9.7pp → **+13.9pp**, n 214 → 252. Discordant pairs 63:28.
  It is present in **both** tapes (+11.3pp up, +15.5pp down), so it is not a beta artifact.
- **Short deficit: p 0.0088 → 0.0026, −13.1pp → −14.5pp**, and once again **near-identical in
  both tapes** (−12.3pp up / −17.7pp down). Symmetric-across-tape is the **mis-selection**
  signature, not mistiming — this is the 2026-08-01 P0's original justification, now on its
  third independent confirmation with a strictly stronger statistic.

**Direction-call accuracy** (did the book pick the right side of its own window's tape?):
**46.0% on up tape (n=211), 33.5% on down tape (n=245)**. The book is systematically
short-into-strength. Both figures drifted *down* from 48.7% / 36.7%.

**Tape split, whole book:** UP n=285 WR 0.411; DOWN n=352 WR 0.395. `|Δ book WR| = 1.6pp`
across a tape swing that moves the benchmark ~30pp — the C49 mechanism in one line.

**DROP pile vs traded book by tape:** UP — DROP 0.425 (n=240) vs book 0.333 (n=45), sized
0.500 (n=30). DOWN — DROP 0.383 (n=248) vs book 0.423 (n=104), sized 0.294 (n=17).

---

## 3.3 — Reliability, Brier, log-loss

**Brier = 0.2865 · log-loss = 0.7934 · graded n = 228.** Brier is past the 0.25
"no-better-than-coin-flip" line.

| bucket | n | predicted | realised |
|---|---|---|---|
| [0.00, 0.50) | 73 | 0.39 | 0.44 |
| [0.50, 0.55) | 51 | 0.53 | 0.53 ✅ |
| **[0.55, 0.60)** | 35 | 0.57 | **0.23** |
| **[0.60, 0.65)** | 17 | 0.62 | **0.29** |
| [0.65, 0.70) | 7 | 0.66 | 0.57 |
| [0.70, 0.80) | 8 | 0.77 | 0.75 ✅ |
| **[0.80, 0.90)** | 31 | 0.83 | **0.45** |
| [0.90, 1.01) | 6 | 0.93 | 0.50 |

Two separate defects, unchanged in shape for a fourth cycle:

1. **The `[0.55,0.65)` trough** — pooled realised **0.250 on n=52** against a ~0.58 quote.
   Strongly *anti*-predictive: quotes in this band are worse than the 0.44 realised by rows
   quoting *below* 0.50.
   **C56 status (the correct, post-fix denominator):** rows quoted in-band **after** the
   2026-07-25 starter-floor shipped = 22 quoted / **19 decided**, realised **0.211**.
   C56's bar is **n ≥ 30 decided post-fix** — **19 of 30, and it did not move this cycle**
   (only 3 new in-band quotes, 2 decided). The pooled n=52 must not be substituted; that
   substitution is exactly what `signal-confluence-quant.md:71` warns about and it has now
   caught two prior audits. **Not actionable. Third cycle of waiting.**
   Sizing discipline holds regardless: **all 22 post-fix in-band rows are `skip` / `watch_only`
   / `veto` — zero sized, 13 cycles running.**
2. **The confident tail** — [0.80,0.90) realises **0.45 on n=31**. This is the historical
   `earnings_vol` / `high_iv_rank` residue. **The 2026-08-15 P1 #2 fix cut it off at source:
   post-fix, `earnings_vol` is quoted 0 times in 21 rows**, and the entire post-fix quote
   distribution tops out at **0.60** (values: 0.496–0.600, n=11). The tail cannot regrow while
   that class-support check holds.

---

## 3.4 — Conviction-vs-outcome (raw_score → WR)

`-3: 0.40(20) · -2: 0.64(11) · -1: 0.40(47) · 0: 0.43(118) · 1: 0.39(168) · 2: 0.33(114) ·
3: 0.39(64) · 4: 0.40(40) · 5: 0.54(13) · 6: 0.47(15) · 7: 0.71(7) · 8: 0.29(7) · 9: 0.67(6) ·
10: 0.00(3) · 11: 0.33(3) · 12: 0.00(1)`

**Non-monotone throughout.** Score 2 (0.33, n=114) is the worst populated bucket in the whole
ladder and sits *below* score −3 (0.40, n=20). Above score 6 every bucket is n ≤ 7 — the top of
the ladder is unmeasurable, not good.

---

## 3.5 — C3 expectancy + fractional-Kelly activation gate

**GATE: `ADVISORY_ONLY`.** n = 27 closed calls (bar: ≥ 30) **and** tier × expectancy is
**non-monotone** (`LOW −1.784 · MEDIUM −2.239 · HIGH −1.965`). Both legs fail.

| tier | mean realised P&L | payoff ratio | capped half-Kelly | n |
|---|---|---|---|---|
| HIGH | **−2.441%** | 0.72 | 0.0 | 7 |
| MEDIUM | +0.104% | 0.948 | 0.0132 | 19 |
| LOW | −2.249% | 0.929 | 0.0 | 123 |
| DROP | −5.004% | 0.647 | 0.0 | 488 |

**Do not flip `signal-confluence-quant` / `risk-monitor` to the Kelly sizer.** The win-rate
ladder stays the live sizer. (The one encouraging line: DROP's expectancy is by far the worst
even though its *hit rate* is the best — payoff 0.647 vs 0.929/0.948. The DROP pile wins small
and loses big. That is the first metric in eight cycles that says the tier ordering is doing
*something*, and it is a P&L metric, not a hit-rate one.)

---

## 3.6 — Regime stratification + the P0.6 out-of-regime half-cap

| regime | long n / WR / excess | short n / WR / excess |
|---|---|---|
| uptrend | 118 / 0.424 / +23.6pp | 68 / 0.412 / **−29.2pp** |
| pullback_in_uptrend | 51 / 0.510 / +5.9pp | 45 / 0.422 / −22.2pp |
| choppy | 18 / 0.667 / −11.1pp | 36 / **0.222** / −25.0pp |
| transitional_other | 73 / 0.288 / +11.0pp | 47 / 0.574 / +21.2pp |

**The short book is negative-excess in every regime bucket but one**, and its single positive
cell (`transitional_other`, +21.2pp on n=47) is the bucket with the least coherent regime label.

**P0.6 half-cap grading (ACTIONABLE, oor_decided = 43):**

| | n | WR | excess |
|---|---|---|---|
| out-of-regime | 43 | **0.326** | **−23.5pp** |
| in-regime | 594 | 0.407 | +3.6pp |
| `rubric_regime` gated | 300 | 0.363 | −2.9pp |
| ungated | 337 | 0.436 | +5.4pp |

Out-of-regime calls underperform in-regime by **8.1pp** on hit rate and **27pp** on excess —
**seventh consecutive negative measurement. KEEP the half-cap.**

---

## Verdict

### (a) Where the rubric is honest
The **[0.50,0.55) bucket is dead-on** (0.53 predicted, 0.53 realised, n=51) and **[0.70,0.80)**
is honest (0.77 vs 0.75, n=8). `bearish_flow` (5.4pp div), `dealer_positioning` (7.9pp),
`bullish_flow` (9.3pp) are all BH-null on divergence — the fleet quotes those three roughly
straight. And the **long book's edge is real and row-matched**: +13.9pp, p=0.0003, present in
both tapes, four cycles running.

### (b) Where it lies to itself
`earnings_vol` 0.87 → **0.38 on n=130** (49.4pp, BH p<0.001, **sixth** appearance) and
`high_iv_rank` 0.77 → 0.47 (n=30, BH). Both are historical residue — the 08-15 class-support
check has stopped the quoting prospectively and the post-fix cohort shows zero recurrence. The
**live** lies are `sector_rotation` (0.54 quoted, **0.29 realised**, n=48, BH p=0.001 — the
worst class in the book for a third cycle, and precisely what scoring a gross-turnover metric as
if it carried direction should look like), `dark_pool_accumulation` (0.55 → 0.40, n=58, BH) and
`multileg_directional` (0.56 → 0.40, n=88, BH).

### (c) Tier inversion / High-tier overconfidence
**Eighth consecutive cycle.** HIGH realises **0.143 on n=7** — the worst tier in the book —
while **DROP realises 0.404 on n=488** and beats LOW (0.389, n=123). Present in all four eras
and all four regime buckets. Post-freeze there are **0 decided HIGH and 0 decided MEDIUM rows**
against 428 DROP + 62 LOW, so the inversion is un-refutable from post-freeze data alone. The
one countervailing signal is 3.5's expectancy column: DROP's *payoff ratio* (0.647) is far worse
than LOW/MEDIUM (0.929/0.948), so the DROP pile's superior hit rate is bought with an inferior
payoff. Hit-rate tier inversion, P&L tier order intact — that distinction is new this cycle.

### (d) Calibrated-but-beta
**`bearish_flow`** qualifies on the letter of the test but with a caveat: divergence BH-null
(5.4pp) ✅, excess ≤ 0 (−14.4pp) ✅, but its paired McNemar is **p = 0.0331, exploratory-family,
BH-fails** — so per C49 this is a *denominator* reading, not a class finding, and must be
reported as such. Its tape-conditioned book WR barely moves (0.413 up → 0.500 down) while its
benchmark swings 0.524 → 0.672.
**`dark_pool_accumulation`** is the cleaner (d): realised 0.400 in *both* tapes (n=20 up / n=35
down — book WR identical to three decimal places across a 34pp benchmark swing), excess +1.5pp,
McNemar p = 1.000. It rides the tape exactly. Sixth cycle of the same reading.
