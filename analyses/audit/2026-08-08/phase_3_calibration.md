# Phase 3 — Calibration Audit (2026-08-08)

## HEADER — C49 denominator diagnostics (read before any excess sentence below)

Across the **31 strata cells** with n≥8 in the McNemar table:

```
sd(book WR) = 0.1275   sd(benchmark WR) = 0.1438   DISPERSION RATIO = 0.886
OLS:  excess_pp = +21.0 − 51.8 × spy_wr      R² = 0.327
implied β(bookWR | spyWR) = +0.48    benchmark share of excess variance = 32.7%
```

On the wider 15-cell diagnostic set used by Phase 3d (which includes regime×direction
cells): slope **−81.8**, R² **0.564**, dispersion ratio **0.743**, benchmark variance share
**64.4%**.

**Read.** This is the *least* denominator-contaminated window C49 has measured. The prior
two cycles ran slope −80.0 / R² 0.636 (07-25) and −81.9 / R² 0.611 (08-01), with the
benchmark carrying 68–71% of excess variance. Here the McNemar-table cells give a
dispersion ratio of **0.886** — book WR is now moving nearly as much as the benchmark —
and R² drops to 0.327. The excess column is meaningfully more informative this cycle than
last. **It is still not the primary test**, and no finding below leads with it; but the
C49 caveat is materially weaker than it has been, and that is worth recording rather than
reciting the boilerplate. The Phase-3d cell set still reads 64.4%, so the caveat is *not*
retired — the divergence between the two cell sets is itself the reason to keep using
row-matched tests.

---

## 3.1 Per-signal-class table (decided N ≥ 8)

Led by realised WR and the paired-McNemar result; benchmark-excess sits to the right,
annotated, per C49.

| class | n | realised | claimed | div (pp) | McNemar p | BH | spyWR | excess |
|---|---|---|---|---|---|---|---|---|
| `bearish_flow` | 116 | 0.457 | 0.50 | +4.3 | 0.0365 | no | 0.595 | −13.8 |
| `earnings_vol` | 106 | **0.404** | **0.87** | **+47.5** | — | **🚩 Y** (p<0.001) | 0.667 | −27.0 |
| `multileg_directional` | 78 | 0.385 | 0.56 | +17.0 | 0.6776 | **🚩 Y** (p=0.004) | 0.356 | +2.9 |
| `bullish_flow` | 55 | 0.400 | 0.53 | +12.7 | 0.3833 | no | 0.315 | +8.5 |
| `dark_pool_accumulation` | 50 | 0.420 | 0.55 | +13.4 | 1.0000 | no | 0.420 | 0.0 |
| `sector_rotation` | 35 | **0.229** | 0.54 | **+30.7** | 1.0000 | **🚩 Y** (p<0.001) | 0.265 | −3.6 |
| `dealer_positioning` | 27 | 0.519 | 0.60 | +7.8 | 1.0000 | no | 0.481 | +3.7 |
| `high_iv_rank` | 24 | 0.500 | **0.82** | **+32.1** | — | **🚩 Y** (p=0.001) | — | — |
| `oi_build` | 12 | 0.500 | 0.00 | — | 0.6250 | no | 0.333 | +16.7 |
| `multi_day_sweep` | 11 | 0.636 | 0.38 | −25.7 | 0.1250 | no | 0.300 | +33.6 |
| `gamma_breakout` | 9 | 0.222 | 0.51 | +28.9 | 0.3750 | no | 0.556 | −33.3 |
| `opex_pin` | 9 | 0.111 | 0.00 | — | — | no | — | — |

THIN_N appendix (decided 5–7): **empty** this cycle.

### Desk commentary on the BH-surviving divergences

**`earnings_vol` — the single worst lie the rubric tells itself, and it got worse.**
Claims **0.87**, realises **0.404** on n=106. That is a 47.5pp gap on the second-largest
class in the book, BH-surviving at p<0.001, and it is now the *fourth* consecutive audit
carrying it. Twelve of thirteen quoted rows still source `win_rate_source: backtest` —
the pre-quarantine substrate. As memory records, `uw historical signal-backtest` supports
only five signal classes and **`earnings_vol` is not among them**, so a genuine backtested
rate for this class cannot exist; whatever produced 0.87 is a proxy the quant is treating
as measured. A flow trader reading "87% on the earnings vol book" would size it as the
best thing on the desk; it is a coin flip that loses to a naive index bet by 27pp. This
is a *quote* defect, not necessarily a *class* defect — the class's realised 0.404 is
poor but its McNemar is untested for want of a directional benchmark.

**`sector_rotation` — worst realised win rate with real N, second cycle running.**
0.229 on n=35 against a 0.54 claim (BH, p<0.001). The mechanism was diagnosed at 08-01
and the fix (C55, re-source off the netted `uw risk market-regime.sector_rotation` rather
than the gross-turnover `sector-flow-persistence`) **was applied** — Phase 6d confirms the
post-P0 rows now cite the netted line exclusively. But only **4** post-fix rows exist and
**1** is decided. The fix is in the pipe; the evidence that it works does not exist yet.
Note the excess is only −3.6pp: this class is not being beaten by the tape, it is simply
losing on its own terms, which is why the calibration read leads and the excess trails.

**`multileg_directional` — miscalibrated but not edge-negative.** 0.385 realised vs 0.56
claimed (BH, p=0.004) on n=78, yet excess **+2.9pp** and McNemar p=0.68. The quote is
17pp too hot; the underlying book is roughly tape-neutral. Fix the number, keep the lane.

**`high_iv_rank` — 0.82 claimed, 0.500 realised, n=24 (BH, p=0.001).** Same family of
defect as `earnings_vol`, same suspected cause, half the sample. Both are vol-lane quotes.

**`bearish_flow` — honest, and that settles C19 for good.** 0.457 realised against a 0.50
claim, divergence +4.3pp, **not** BH-surviving (p=0.406) on n=116 — the best-calibrated
large class in the book for a second consecutive audit. The 2026-07-25 closure of C19 as
REFUTED continues to look correct. Its negative excess (−13.8pp) is a *direction* fact
about shorts, addressed in §3.4, not a calibration fact about this class.

## 3.2 Per-tier reliability

| Tier | n | realised WR |
|---|---|---|
| HIGH | 7 | **0.143** |
| MEDIUM | 19 | 0.526 |
| LOW | 104 | 0.375 |
| DROP | 412 | **0.415** |

**Monotone (HIGH > MEDIUM > LOW)? NO — 6th consecutive failure.** HIGH remains the worst
tier in the entire corpus and DROP again beats LOW. The HIGH cell has been frozen at n=7 /
0.143 for four audits because the frozen rubric has not emitted a HIGH since the freeze.

Era-stratified (never pooled):

| era | HIGH | MEDIUM | LOW | DROP |
|---|---|---|---|---|
| `era_0525_0529` | 0.25 (4) | 0.556 (9) | 0.579 (19) | 0.571 (21) |
| `era_0530_0605` | 0.00 (2) | 0.500 (10) | 0.400 (25) | 0.419 (31) |
| `pre_freeze_post_0606` | 0.00 (1) | — (0) | 0.353 (17) | 0.500 (8) |
| **`2026-06-12` (FROZEN)** | **— (0)** | **— (0)** | 0.279 (43) | 0.403 (352) |

The frozen era has produced **zero HIGH and zero MEDIUM** decided calls. This is the 8th
consecutive cycle in which the tier-monotonicity re-validation is not merely unsatisfied
but **structurally unrunnable**.

## 3.3 Brier / log-loss / reliability deciles (C25)

```
BRIER = 0.2863    LOG-LOSS = 0.795    graded n = 213
```

Brier sits just above the "no better than coin-flip" 0.25 line. Log-loss of 0.795 against
a 0.693 coin-flip reference confirms the damage is concentrated in confident-and-wrong
quotes, not in diffuse noise.

| bucket | n | predicted | realised | read |
|---|---|---|---|---|
| [0.00,0.50) | 68 | 0.39 | 0.43 | well calibrated |
| [0.50,0.55) | 50 | 0.52 | 0.54 | well calibrated |
| **[0.55,0.60)** | **30** | 0.57 | **0.20** | **anti-predictive** |
| **[0.60,0.65)** | **13** | 0.62 | **0.31** | **anti-predictive** |
| [0.65,0.70) | 7 | 0.66 | 0.57 | thin, ok |
| [0.70,0.80) | 8 | 0.77 | 0.75 | thin, good |
| **[0.80,0.90)** | **31** | 0.83 | **0.45** | **overconfident** |
| [0.90,1.01) | 6 | 0.93 | 0.50 | thin, overconfident |

**The [0.55,0.65) anti-predictive band survives its first fix cycle.** Combined n=43,
realised **0.233** against a 0.58 mean quote. The 07-25 P1 floored these to `starter` and
08-01 registered **C56** to re-derive the quote itself; C56 has not been applied. A bucket
that predicts 0.58 and delivers 0.23 is not merely miscalibrated — it is *informative with
the sign flipped*, and it is the region the rubric emits into most often after the
sub-0.55 band. The ≥0.80 buckets (n=37 combined, realised 0.46) are the `earnings_vol` /
`high_iv_rank` quotes from §3.1 showing up in the diagram.

## 3.4 PRIMARY EDGE TEST — tape-conditioned book WR + paired McNemar (C49)

BH applied **within** the pre-registered primary family (7 direction × tape cells), not
pooled with the exploratory per-class sweep — pooling 30+ auto-generated cells is a
post-hoc power tax and destroyed the primary finding when tried at 08-01.

| cell | n | book WR | spy WR | b | c | p | BH |
|---|---|---|---|---|---|---|---|
| **ALL / short** | **181** | 0.420 | 0.564 | 25 | 51 | **0.0038** | **🚩 YES** |
| **UP / short** | **112** | 0.357 | 0.500 | 13 | 29 | **0.0195** | **🚩 YES** |
| **ALL / long** | **214** | 0.421 | 0.322 | 49 | 28 | **0.0220** | **🚩 YES** |
| UP / long | 95 | 0.474 | 0.358 | 24 | 13 | 0.0989 | no |
| DOWN / short | 69 | 0.522 | 0.667 | 12 | 22 | 0.1214 | no |
| DOWN / long | 119 | 0.378 | 0.294 | 25 | 15 | 0.1539 | no |
| ALL | 395 | 0.420 | 0.433 | 74 | 79 | 0.7465 | no |

### The two findings that matter

**1. The short-book deficit replicated and strengthened — the P0 was right.**
`ALL / short` moves from p=0.0115 (08-01) to **p=0.0038** on n=181, with discordant pairs
b=25 / c=51 — the book loses head-to-head pairs to a naive same-window index short by more
than 2:1. `UP / short` now clears BH independently (p=0.0195). Tape-conditioned book WR:
**UP 0.357 / DOWN 0.522**, against benchmarks of 0.500 / 0.667 — excess −14.3pp and
−14.5pp, *near-identical across tapes for a second consecutive audit*. That equality is
the whole argument: a mistimed book would show a tape-dependent gap; an equal gap in both
tapes is **mis-selection**. The 2026-08-01 P0 (route shorts to `watch_only`) rests on this
result, and this cycle it is stronger, not weaker.

**2. The long-book edge is real and has now replicated three times — but it is decaying.**
`ALL / long` p=0.0220, BH-surviving, n=214, b=49 / c=28. That is three independent windows
(07-25 p=0.0081, 08-01 p=0.0046, now 0.0220) in which the long book beats a row-matched
index long. It is the only durable positive edge this system has produced. **The p-value
has risen in each of the last two cycles and neither tape arm clears BH on its own**
(UP p=0.0989, DOWN p=0.1539). Book-long WR is +11.6pp over benchmark in the up tape and
+8.4pp in the down tape — positive in both, which is more than the shorts can say, but the
margin is thinning. Watch it; do not act on it.

**3. `ALL` is a null (p=0.7465).** The whole book, long and short together, is
indistinguishable from the tape. The two directional findings above are equal and
opposite, and they cancel. That is precisely why the P0 routing change — which removes the
negative half without touching the positive half — is the correct intervention.

## 3.5 Direction-call accuracy

| tape | n | positioned WITH tape | rate |
|---|---|---|---|
| UP | 213 | 100 | 46.9% |
| DOWN | 188 | 69 | **36.7%** |

The fleet is structurally long-biased into a falling tape, replicating 08-01's 36.0%.

## 3.6 DROP pile vs traded book, by tape

| tape | DROP | traded book | sized |
|---|---|---|---|
| UP | 0.410 (n=244) | 0.304 (n=46) | **0.500 (n=30)** |
| DOWN | 0.423 (n=168) | 0.429 (n=84) | **0.294 (n=17)** |

The long-running "DROP beats the book" result has **split by tape** this cycle. In the up
tape the sized book (0.500) now clearly beats DROP (0.410) — the first time sizing has
looked additive. In the down tape it inverts hard: sized 0.294 vs DROP 0.423. The
empty-board discipline is still earning its keep in falling tape; in rising tape the fleet
has started to add value by sizing. n=30 and n=17 respectively — a signal to watch, not to
act on.

## 3.7 C3 — expectancy and the fractional-Kelly live-activation gate

```
KELLY GATE: ADVISORY_ONLY
  n = 27 closed (< 30 required)
  tier expectancy monotone HIGH ≥ MED ≥ LOW?  NO
  {LOW: −1.784, MEDIUM: −2.239, HIGH: −1.965}
```

| tier | mean realised P&L | payoff ratio | capped half-Kelly | n |
|---|---|---|---|---|
| HIGH | −2.441 | 0.72 | 0.0 | 7 |
| MEDIUM | +0.104 | 0.948 | 0.0132 | 19 |
| LOW | −3.523 | 0.808 | 0.0 | 104 |
| DROP | −3.020 | 0.775 | 0.0 | 412 |

**Gate does not pass — both clauses fail.** n=27 < 30, and tier×expectancy is non-monotone.
MEDIUM is the only tier with positive expectancy and it is the only tier with a payoff
ratio near 1.0. **Do not flip `signal-confluence-quant` / `risk-monitor` to the Kelly
sizer.** The win-rate ladder stays the live sizer.

---

## Verdict

### (a) Where the rubric is honest
`bearish_flow` (0.457 vs 0.50 claimed, n=116, BH-null) is genuinely well calibrated for a
second cycle. The sub-0.55 quote buckets ([0.00,0.50) and [0.50,0.55), n=118 combined) are
calibrated to within 4pp. The mechanical integrity is flawless: 0 Σ-violations on 626 rows,
64/64 envelopes valid.

### (b) Where it lies to itself
The vol lane. `earnings_vol` quotes 0.87 and delivers 0.404 (n=106); `high_iv_rank` quotes
0.82 and delivers 0.500 (n=24). Both BH-surviving, both sourcing a `backtest` substrate
that provably cannot support them. `sector_rotation` quotes 0.54 and delivers 0.229 (n=35).
And the [0.55,0.65) band predicts 0.58 while realising 0.233 — a fix was registered as C56
at 08-01 and has not been applied.

### (c) Tier inversions / High-tier overconfidence
HIGH realises 0.143 (n=7), the worst tier in the book, for a 6th consecutive cycle; DROP
(0.415) beats LOW (0.375). Post-freeze the HIGH and MEDIUM bands are **empty** — 8th cycle.
There is no tier-monotonicity test to run, and there will not be one until the rubric's own
conjunction requirements are loosened, which the freeze forbids.

### (d) Calibrated-but-beta
**No class qualifies this cycle under the strict C49 definition** (calibration ✅ **and**
McNemar non-significant **and** excess ≤ 0). `bearish_flow` is the near-miss: calibration ✅
(+4.3pp), excess ≤ 0 (−13.8pp), but its McNemar p=0.0365 sits in the exploratory family
and does **not** survive BH there — so per the rule, its negative excess is a *denominator*
reading and cannot be promoted to a class finding. `dark_pool_accumulation` reads excess
exactly 0.0 with McNemar p=1.000 on n=50 — the purest "rides the tape, neither beats nor
trails it" result in the table, but its 13.4pp calibration gap keeps it out of the
calibrated-but-beta bin too.

## Outputs

`phase_3_calibration.jsonl`, `phase_3b_regime.jsonl`, `phase_3c_tape.jsonl`,
`phase_3c_mcnemar.jsonl`, `phase_3d_excess_artifact.jsonl`.
