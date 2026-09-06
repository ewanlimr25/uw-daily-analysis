# Phase 7 — Recommendations (2026-08-15)

**PROPOSE-ONLY.** No file outside `analyses/audit/2026-08-15/` was edited by this audit.
Every item below cites the phase and the data point that justifies it.

**Provenance basis:** 569/672 rows (84.7%) carry **verbatim** envelope `source_tool`
citations; **zero** prose-reconstructed. The C23 reconstruction cap does not bind. The
remaining P0 constraints do — and the reason there is **no P0 this cycle** is stated in the
verdict below.

---

## P1 #1 — Constrain `source_tool` to one canonical tool identifier per component

**What.** Require `score_components[].source_tool` to be a single canonical tool id (e.g.
`uw options-structure term-skew`), one component per tool, instead of free text. Add the
allowed-id list to the quant agent's output contract and a validator check.

**File.** `.claude/agents/signal-confluence-quant.md` · `scripts/validate_decision.py` ·
`schemas/decision_envelope.schema.json`.

**Phase / Data.** Phase 4: **122 distinct raw citation strings across 1,225 instances; 60
appear exactly once; 52 contain a `+` concatenation; 19 rows have every citation
concatenated. 155 citation instances were trapped in n<5 labels** and silently excluded from
tiering. Atomizing recovered them and lifted the testable tool count 23 → 29. The same tool
scores opposite tiers under different labels: `scripts/term_structure_hygiene.py` **+34.1pp**
vs `iv-term-structure hygiene` **−39.7pp**; `options-structure front-end-iv-ratio` −7.3pp vs
`front-end-iv-ratio` +6.5pp.

**Priority.** P1 — clear improvement. Not P0: it corrects the *auditor's measurement
substrate*, not a live sizing decision, so nothing trades differently next session.

**Risk.** Low. A canonical enum could drop genuinely novel tool combinations into an "other"
bucket; mitigate by emitting one component per tool rather than forcing a merge. The real
risk is inaction: **eleven cycles of Phase 4 tool tiers have been built on fragmented labels**,
and no tool-tier finding is trustworthy until this lands.

---

## P1 #2 — Stop quoting `win_rate` for classes `uw historical signal-backtest` cannot measure

**What.** Where the class is not one of the five `signal-backtest` supports, the quant agent
must emit `win_rate: null` with `win_rate_source: "NA(substrate)"` — never a numeric quote
sourced `backtest`. Add a validator rule rejecting `win_rate_source ∈ {backtest,
backtest_clean}` for unsupported classes.

**File.** `.claude/agents/signal-confluence-quant.md` · `scripts/validate_decision.py`.

**Phase / Data.** Phase 3.1: **`earnings_vol` quotes 0.87 and realises 0.394 on n=109 — a
47.7pp divergence, BH-surviving at p < 0.001, the largest miscalibration in the corpus and its
fifth consecutive appearance.** 12 of 13 quoted rows cite `win_rate_source: backtest`, but
`signal-backtest` does not support `earnings_vol` — the number cannot have been measured.
`high_iv_rank` is the same defect (0.79 → 0.481, n=27, BH). Phase 3.3: the ≥0.80 reliability
bucket realises **0.459 on n=37**, and it is 14 `high_iv_rank` + 12 `earnings_vol` rows —
the entire confident tail of this system is these two classes.

**Priority.** P1. Phase 6.6 shows the fix **half-landed**: `high_iv_rank` improved (claim
0.818 → 0.600, source now 3/3 `backtest_clean`), while `earnings_vol` simply stopped quoting
rather than quoting correctly — the defect is untested, not repaired.

**Risk.** Nulling the quote removes the sizing ladder's input for those classes, pushing them
to the `NA(substrate)` path. Given the classes realise ~0.40–0.48 against 0.79–0.87 quotes,
that is the correct trade: no number beats a number that is wrong by 48 points.

---

## ~~P1 #3 — Re-derive the `[0.55,0.65)` win-rate band~~ — **WITHDRAWN at application time, NOT SHIPPED**

> **This recommendation was wrong and was withdrawn before any edit landed (see `APPLIED.md`).**
> It cites **n=49 / p = 1×10⁻⁶** below — but that is the **pooled corpus across rubric eras**.
> C56's bar is **post-fix quoted rows only**, which stand at **19** (post 2026-07-25
> starter-floor) or **8** (post 2026-08-01 disclosure rule) against a bar of **n ≥ 30**.
> `signal-confluence-quant.md:71` warns about exactly this trap in writing, because the
> 2026-08-08 audit fell into it — and this audit fell into it too. Pooling eras to clear a
> pre-registration is the same error as the C49 excess-denominator artifact: a bigger, wronger
> denominator because it clears a threshold the correct one does not. **The band's `starter`
> floor and disclosure-only rule remain live and are holding** (all 8 post-2026-08-01 in-band
> rows resolved `skip`/`watch_only`, zero sized). The original text is retained below unedited
> as the record of the error.

<details><summary>Original (withdrawn) recommendation</summary>

### P1 #3 — Re-derive the `[0.55,0.65)` win-rate band, not just floor its size

**What.** The 2026-07-25 starter-floor stopped in-band names from being *sized*. It did not
touch the quote that puts them in the band. Re-derive or null the estimator that produces
predictions in `[0.55,0.65)`.

**File.** `.claude/agents/signal-confluence-quant.md` (backtest-sizing-map section).

**Phase / Data.** Phase 3.3: **n=49, mean prediction 0.586, realised 0.245, one-sided
binomial p = 1×10⁻⁶.** Third consecutive cycle, stable, strongly *anti*-predictive — the
band's information content is real with the sign inverted. Phase 6.6: the sizing floor is
holding (all 8 post-cohort in-band rows resolve `skip`/`watch_only`, zero sized), but the
in-band **share of quotes rose 22% → 40%**.

**Priority.** P1 — sizing *procedure*, in scope under the freeze (not a rubric weight or cut).

**Risk.** The band carries 22–40% of all quoted rows; nulling it moves a large share of the
book onto the `NA(substrate)` path and could thin the board further on an already 21-week
empty streak. Acceptable — a board that is empty for the right reason beats one populated by
a 0.586 quote that delivers 0.245.

</details>

---

## P1 #4 — Retire C15 and C18 rather than continue accruing them

**What.** Close `C15` (squeeze / short-interest gate) and `C18` (insider-cluster conjunction)
as **REFUTED-BY-UNMEASURABILITY**, and either fix the `insider_cluster_flag` emitter in the
same session or drop the field. Keep C16 open (starved, not dead) and C17 advisory.

**File.** `analyses/audit/2026-05-25/improvement_criteria.md` (register) ·
`.claude/agents/fundamentals-gate.md` · `scripts/fz_enrich.py`.

**Phase / Data.** Phase 4 `fz` table: **C15's trigger condition (`short_float ≥ 20% ∧ dtc ≥ 5`)
has never once been met — `n_hi_si = 0`, and the squeeze-pressure distribution across 167
populated rows is `LOW` 106 / `MODERATE` 11 / `unknown` 50 with zero `HIGH`.** C18:
`insider_cluster_flag` is populated on 20 of 210 calls and **every populated value is
`False`** — zero variance cannot gate a conjunction at any n; this is its **sixth** cycle
carrying the same finding (Phase 6.6). C16's `dp_block_to_float_ratio` is populated on **7 of
210** — the emitter still writes null; that one is genuinely starved and stays open.

**Priority.** P1. A criterion that *cannot fire* is not pending, it is dead, and carrying it
as "awaiting data" has cost six audits of attention.

**Risk.** Retiring C15 forfeits squeeze context if a high-short-interest regime arrives. Note
the `fz` short-interest field is the exchange semi-monthly settlement figure (~2-week lag) —
squeeze *context*, never a live borrow signal — so little is lost. If a HIGH squeeze regime
appears, re-register it fresh with the observed distribution as the pre-registration basis.

---

## P1 #5 — Keep the rubric freeze; the blocker is upstream of it

**What.** Do not lift the 2026-06-12 freeze. Record explicitly that the lift is **unrunnable
by construction**, and redirect the effort at the conjunction requirements that starve the
upper tiers.

**File.** `.claude/commands/daily-analysis.md` · `.claude/agents/signal-confluence-quant.md`
(no edit now — this is the freeze-lift grading the skill requires).

**Phase / Data.** Phase 5.4: the lift's N precondition is satisfied **14× over — 425 resolved
post-freeze calls** — but there are **0 decided HIGH and 0 decided MEDIUM** post-freeze (521
post-freeze rows → 461 DROP / 60 LOW; **one** `full`-sized call in the entire corpus). Phase
5.3: the frozen cuts are non-monotone at the top (`[0.411, 0.419, 0.500, 0.385]` DROP→HIGH),
8th cycle. Phase 3.4: tier inversion 7th consecutive cycle, present in **all four** rubric
eras and **all four** regime buckets, with DROP (0.420, n=438) beating LOW (0.389, n=108) and
HIGH worst at 0.143 (n=7).

**Priority.** P1 (a "keep" decision with evidence, per the skill's freeze-lift check).

**Risk.** Keeping a freeze indefinitely ossifies a rubric nobody can grade. The mitigation is
to attack the conjunction requirements — but note Phase 5.1 found **no component surviving
BH** (smallest p = 0.025 on an n=8 *zero-point* line), so there is no measured basis to loosen
any specific conjunction. Loosening on no evidence is how the pre-freeze whipsaw happened.

---

## P1 #6 — Keep the P0.6 out-of-regime half-cap

**What.** No change. Recorded as a graded "keep."

**File.** `.claude/agents/risk-monitor.md` (`rubric_regime` gate) — no edit.

**Phase / Data.** Phase 3.6 / 5.5: out-of-regime **0.326 (n=43)** vs in-regime **0.422
(n=529)**, Δ = **−9.6pp**. Negative in all six measurements taken; the margin has compressed
but has never changed sign. `rubric_regime` gate fired: 0.377 (n=252) vs ungated 0.444 (n=320).

**Priority.** P1 (keep-with-evidence).

**Risk.** None from keeping. The cap costs size in a regime the rubric was not fitted to,
which is exactly its purpose.

---

## P2 #7 — Collapse the `dominant_signal_class` enum

**What.** Constrain `dominant_signal_class` to a closed enum; map the drift labels
(`dealer_positioning_flip`, `dealer_flip`, `dex_flip_long`, `dex_flip_short`,
`dealer-positioning_dex_flip`, `dealer_short` → `dealer_positioning`; `sector_leader` →
`sector_rotation`; `multileg_directional_conflicted`, `directional_conflict` →
`multileg_directional`; `distribution` → `dark_pool_distribution`; `none` → null).

**File.** `schemas/decision_envelope.schema.json` · `.claude/agents/signal-confluence-quant.md`.

**Phase / Data.** Phase 1 / 6.6: **31 distinct classes, 16 of them at n ≤ 4**; four labels for
the one dealer-flip mechanism. Carried as REC 9 at 2026-08-08 and **not applied**. The audit
already canonicalizes in Phase 2 (`canonical_class`), which is why this is P2 and not higher —
the measurement is protected, the emitter is just noisy.

**Priority.** P2 — polish. Confidence high, impact low.

**Risk.** A closed enum could suppress a genuinely new signal class; allow an `other` value
with a free-text sidecar field.

---

## P2 #8 — Auditor method: re-resolve `opex_pin` on pin-distance, not ±1R breach

**What.** Change the **auditor's** Phase-2 resolution rule for pin structures. Pre-registered
as **C59**.

**File.** `analyses/audit/*/phase2_resolve.py` (auditor only — the subject fleet is untouched).

**Phase / Data.** Phase 3.1: `opex_pin` realises **0.111 on n=9**; Phase 5.2:
`opex-pin-strategist` reads **−23.7pp on n=11**. Iron flies and short straddles profit from
price *staying inside* a band, so a ±1R touch that reverts is scored LOSS even though the
structure would have paid. An implausible magnitude for a mechanical, well-specified lane.

**Priority.** P2 — and note it is a **method** item: it corrects how the auditor grades, not
how the fleet trades. It cannot be P0/P1 because it changes no trading behaviour.

**Risk.** Re-resolving could flatter a genuinely bad lane. Mitigate by reporting both rules
side-by-side for one cycle before switching (the C59 acceptance bar requires exactly that).

---

## Pre-registrations carried forward (decided by future audits, not this one)

- **C57** — `vol_term_structure(+/−1)` contributes negatively. Current: **−8.8pp, n=119,
  p = 0.063, negative in BOTH tape arms** (−7.6 up / −10.3 down), corroborated by Phase 4
  (`term-skew` −7.2pp n=71; `front-end-iv-ratio` −7.3pp n=26) and Phase 3 (feeds the two most
  overconfident classes). **Short of the bar** (needs BH-surviving ∧ n ≥ 30 per arm).
  Decision window: 2026-09-05 → 2026-10-31.
- **C58** — `dealer_dex_flip` weight is sign-unstable in points awarded (+25.6pp at [+2] n=9,
  +6.7pp at [+1] n=42, −6.3pp at [+3] n=31 incl. −30.4pp up-tape). Decision window:
  2026-09-05 → 2026-11-30.
- **C59** — the `opex_pin` resolution-rule item above (auditor method).
- **C56** — `[0.55,0.65)` band; now escalated to an actionable P1 #3 on n=49 / p = 1×10⁻⁶.

---

## Why there is no P0 this cycle

A P0 means "act before next session." Three things would have to be true, and none is:

1. **No new edge finding demands one.** The only BH-surviving row-matched results are the
   short-book deficit (−13.1pp, p = 0.0088) and its long mirror (+9.7pp, p = 0.0220) — and the
   short finding **already has its P0**, applied 2026-08-01 and now graded APPLIED CLEAN for a
   second consecutive cycle (Phase 6.5), with its evidence intact.
2. **No compliance failure demands one.** Phase 6: 5 missed gates in 1,163 non-DROP
   obligations (0.43%), one sizing violation from June, 569/569 clean score arithmetic, all
   nine gates effective or advisory.
3. **No calibration finding qualifies.** The four BH-surviving divergences (Phase 3.1) are
   *quote* defects, not *edge* defects — `sector_rotation` and `multileg_directional` both
   have McNemar p ≈ 1.0 and excess near zero; they underperform their advertised numbers, not
   the market. Per C21-as-amended-by-C49, a raw excess number may never headline a
   recommendation or justify a priority above P2, and none here does.

**The correct output of this cycle is a housekeeping list, not surgery.** That is the second
consecutive audit where the honest answer is "nothing urgent," and it should be read as the
system working: the last P0 landed, held, and got stronger.
