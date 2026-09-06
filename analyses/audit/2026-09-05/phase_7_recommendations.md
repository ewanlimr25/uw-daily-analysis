# Phase 7 — Recommendations (2026-09-05)

**Propose-only.** Nothing outside `analyses/audit/2026-09-05/` was written by this audit.
**Provenance: 100% verbatim envelope** on 878 rows — the C23 reconstructed-citation cap does
not bind, so P0 is available this cycle. It is used **once**.

---

## P0 #1 — The frozen tier cuts are unreachable, and the rubric is therefore unfalsifiable

**What.** Record, in `signal-confluence-quant.md`'s freeze-status block, that the frozen tier
cuts (**HIGH ≥ 9 / MEDIUM 7–8**) sit above the maximum score the frozen rubric can produce —
and that this, not market conditions, is why the freeze-lift test has been unrunnable for
seven consecutive cycles. Do **not** re-bin the cuts. The change is a **status correction plus
the C65 registration**, so that the next audit grades a documented defect instead of
re-deriving it an eighth time.

**File.** `.claude/agents/signal-confluence-quant.md` (the freeze-status paragraph at line
~173, which currently reads the emptiness as "the frozen rubric behaving as calibrated").

**Phase / Data.** Phase 5.0. On 2026-06-12 the audit removed `uw insights signal-confluence`
from scoring and cut the cum-flow line; mean points **per component** fell 1.391 → 0.512 and
components worth 3 fell from 24.6% to 2.7% of awards. **Mean `raw_score` 3.56 → 0.86; p90
8 → 3; rows ≥ 9: 13 → 0 of 727.** Daily session-max median **9.0 → 3.0**, Mann-Whitney
**z = 5.65, p = 1.6 × 10⁻⁸**, a step function at the freeze date with **no recovery in any of
the four regime buckets** across 59 sessions. The components were cut; the cuts were not
re-derived. HIGH now sits 8 points above the post-freeze mean and above the post-freeze
maximum. Corroborating: post-freeze tiers are `LOW 79 / DROP 648`, `HIGH n=0`, `MEDIUM n=1`
(a vetoed weekly row).

**Priority.** P0 — but on the **status text and the registration only**. The trading behaviour
this produces is very possibly correct (DROP 0.391 ≈ LOW 0.402, sized book 42.6% on n=47, HIGH
realised 0.143, tier expectancy negative everywhere but MEDIUM). **This is not "we should be
trading more."** It is P0 because a ladder whose top half is arithmetically unreachable cannot
discriminate, cannot be graded, and **cannot ever satisfy its own freeze-lift criterion** — the
test demands post-freeze HIGH/MEDIUM rows the arithmetic forbids. The system has run an
unfalsifiable rubric for 59 sessions and each audit has re-described the symptom.

**Risk.** The obvious misreading is "lower the cuts and start trading." That would repeat the
exact failure the freeze exists to stop — re-binning on a single window. The mitigation is
built in: the deliverable is a status correction and **C65**, whose acceptance bar
(cross-regime ∧ n ≥ 30 per arm ∧ BH-surviving) cannot be met before **2026-11-07** and needs
rows scored under a changed configuration that do not yet exist. If applied as written, nothing
about sizing changes next session.

---

## P1 #1 — Register C66: the vol lane cannot reach a sizeable tier, and the good leg is now the only leg

**What.** Register **C66** and note the constraint in the vol agents' scope blocks: no vol
thesis can clear DROP under the frozen rubric, so `vol_long` — the only positive-edge lane in
the corpus — is unsizeable by construction. Documentation + registration; **no weight edit**.

**File.** `.claude/agents/vol-surface-scout.md`, `.claude/agents/earnings-scout.md` (scope
notes); register entry alongside C63.

**Phase / Data.** Phase 5.4 / Phase 2. `vol_long` max `raw_score` **4** on 85 rows (median 1);
`vol_short` max 5 on 153; **neither lane has ever produced a MEDIUM or HIGH call.** Every
component that has ever fired on a `vol_long` row is worth +1 — the rubric's ≥2 lines (+3
accumulation conjunction, +2 multileg) are directional-only, so MEDIUM requires seven
simultaneous +1s, never once observed in 238 vol rows. Meanwhile `vol_long` measures **+8.5pp**
against unselected same-date single-name peers (n=56, McNemar b=17 c=1, **p = 1.5 × 10⁻⁴**) and
is **5-for-5 on every sized row it has ever had**. In the five post-change sessions it produced
**20 candidates and sized none** — all DROP, all raw ≤ 2.

**Priority.** P1. The finding is structural and certain; the remedy is a registration whose bar
cannot clear this cycle.

**Risk.** Reads as an argument to hand the vol lane extra points. It is not — `vol_long`'s
edge rests on n=56 paper rows and 5 sized rows, on an **RV-direction proxy that prices
selection and never P&L**. Writing a weight now would be the cum-flow +2→+3→+1 whipsaw again.

---

## P1 #2 — Stop reporting `earnings_vol` as an independent calibration flaw

**What.** Fold the `earnings_vol` divergence into the vol finding wherever it is tracked. It is
not a separate class problem and it has been occupying a second headline slot for a problem
already counted once.

**File.** Audit-side convention (the class table in future `phase_3_calibration.md`); no
subject file changes.

**Phase / Data.** Phase 3.3. **125 of 172** `earnings_vol` rows carry a `vol_short` thesis.
Split: `earnings_vol ∧ vol_short` **n=99, WR 0.232**; `earnings_vol ∧ vol_long` **n=27, WR
0.630**. The class-level 0.325 is a weighted average of the lane already routed to
`watch_only` and the lane that cannot be scored. The 0.87 claim rests on **13 quoting rows,
all May–July**; quoting has since stopped entirely.

**Priority.** P1. Double-counting a P0 across two slots inflates the apparent flaw count and
misdirects the next cycle's attention.

**Risk.** Low. Nothing is dropped — the rows still resolve under the vol lane.

---

## P1 #3 — Instrument the fundamentals VETO inversion; do not touch the gate

**What.** Extend `fundamentals_verdict_reason` (shipped last cycle) to VETO/CAUTION rows on
**short** theses specifically, and add a standing audit line tracking direction-controlled
verdict effectiveness. **No gate change, no threshold change.**

**File.** `.claude/agents/fundamentals-gate.md` (emission scope of the reason field).

**Phase / Data.** Phase 6.4. Pooled: VETO 0.520 (n=25) > CONFIRM 0.377 (n=122) > CAUTION 0.338
(n=139) — inverted, second consecutive cycle. The composition hypothesis (20 of 25 decided
VETOs are shorts) was tested and **fails**: within short theses, VETO'd names realise **0.450
(n=20)** vs non-VETO'd shorts **0.306 (n=49)** — **+14.4pp anti-effective**, with the internal
ordering VETO > CONFIRM > CAUTION monotone and backwards.

**Priority.** P1, instrumentation only. n=20 clears C24's ≥10 floor, but **C24 forbids
loosening a gate on this evidence** and every VETO'd short is routed to `watch_only` anyway, so
the gate currently costs nothing. `insider_selling_cluster` is 9 of 15 reasons so far — the
most likely single explanation and testable.

**Risk.** If the inversion is real and persists, we will have spent two more cycles measuring
instead of acting. Accepted deliberately: a fundamentals VETO is insurance against the tape
that has not happened, and 20 unsized rows in a calm market is the weakest possible ground for
removing it.

---

## P2 #1 — Retire `insider_cluster_flag` and C18 (re-raised, not applied last cycle)

**What.** Drop `insider_cluster_flag` from the envelope and close **C18** as untestable, or
repoint it at a source with variance.

**File.** `schemas/decision_envelope.schema.json`, `.claude/agents/accumulation-hunter.md`.

**Phase / Data.** Phase 4.3 / 6.5. **30 populated values, all `False`** — zero variance, second
consecutive cycle; the C18 conjunction has no upper arm and never will from this source. The
contradiction worth naming: `insider_selling_cluster` is simultaneously the **most common**
`fundamentals_verdict_reason` (9 of 15). Two insider signals, one uniformly silent, one
dominant, reading different sources (`fz insider-clusters` vs the Finnhub MSPR path) with
nothing in the schema saying so.

**Priority.** P2. Costs nothing to carry; costs clarity to leave contradictory.

**Risk.** If `fz insider-clusters` is simply mis-wired rather than genuinely null, retiring the
field discards a real signal. Check the wiring before deleting.

---

## P2 #2 — Restate the Brier / log-loss coverage caveat wherever those scalars appear

**What.** Print `n` beside every calibration scalar and note the shrinking denominator.

**File.** Audit-side (`phase_3_calibration.md` template).

**Phase / Data.** Phase 3.5. `claimed_win_rate` emission: **69% (May) → 50% → 24% → 21% → 9%
(September, 7 of 81 rows)**. That is the `NA(substrate)` honest-null discipline working as
designed, but Brier (0.2852) and log-loss (0.7883) now describe a **shrinking, non-random
residue** — the rows where a clean backtest happened to exist. Their apparent stability versus
last cycle (0.286 / 0.790) should not be read as calibration stability.

**Priority.** P2.

**Risk.** None.

---

## Explicitly NOT recommended

- **No tool-tier movements.** 2 of 26 tools survived BH; `uw options-structure term-skew`
  (−10.8pp overall) is **+2.0pp inside `vol_short`** — composition, exactly as last cycle
  warned. `scripts/term_structure_hygiene.py` is genuinely negative within every lane
  (−21.5pp inside VOL) but **27 of its 31 citing rows are August**, non-August accrual is
  **n=4 of a required 30**, and 22 of 31 sit in one regime bucket. **C61 stays open.**
- **No rubric weight edits and no cut re-bins.** The one BH-surviving component
  (`vol_term_structure`, −11.4pp) is the same artifact: **−0.6pp inside VOL, −0.3pp inside
  `vol_short`, +5.4pp inside `vol_long`.** The table is BH-null in substance for the 13th
  consecutive cycle.
- **Keep the P0.6 out-of-regime half-cap.** −7.3pp protective (OOR 0.326 n=43 vs in-regime
  0.398) — ninth consecutive negative reading.
- **Keep the C56 [0.55,0.65) anti-predictive floor.** Post-change in-band rows realise **0.10
  (n=10)** and **none were sized**. It is binding and the band got worse.
- **Keep Kelly OFF.** Gate returns `ADVISORY_ONLY`: n=27 of 30 closed, and tier × expectancy is
  non-monotone (LOW −1.784 / MEDIUM −2.239 / HIGH −1.965).
- **Do not read the 08-01 short P0 as resolved.** Post-P0 McNemar p=0.4807 — but WR moved
  0.429 → **0.294** and the sign is unchanged. The p-value moved because **n fell** (182 → 51),
  not because the deficit did.
- **C63 cannot be graded.** Post-change `vol_short` is **10 decided of a required 40**, one
  regime bucket of two, none with a complete forward window or peer benchmark. The provisional
  0-for-10 is colour. Earliest honest decision: **2026-10-03.**
