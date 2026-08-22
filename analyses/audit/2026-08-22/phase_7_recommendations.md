# Phase 7 — Recommendations (2026-08-22)

**Propose-only.** Nothing outside `analyses/audit/2026-08-22/` was written by this audit.
Every item cites its phase and data point.

**Provenance basis (C23):** 100% verbatim `decision.json` envelope citations across 737 rows /
76 envelopes, 76/76 validating clean, 0 prose reconstruction, 0 `Σpoints ≠ raw_score`
violations. **P0 is therefore available on provenance grounds this cycle** — and no finding
earns it. The rubric stays frozen at `2026-06-12`; every rubric-shaped item below is a
pre-registration, not an edit.

---

## P1 #1 — Restore short-thesis *generation* to the 2026-08-01 P0's stated intent

**What.** The P0 routes directional shorts to `watch_only`; it does **not** authorize the fleet
to stop producing them. Add an explicit instruction that short candidates clearing the entry
bar must still be scored, serialized and written to `calls[]` with a full `score_components[]`
and `gate_verdicts` block, with `final_size: watch_only` — the routing is a *sizing* decision
taken at the end, never a Phase-1 screening decision.

**File.** `.claude/agents/risk-monitor.md` (restate the routing as post-scoring), and
`.claude/commands/daily-analysis.md` + `.claude/commands/weekly-analysis.md` (Phase-1 candidate
union must not pre-filter shorts).

**Phase / Data.** Phase 6.5: post-P0 short share **17.6%** of the board vs **32.0%** pre-P0
(Fisher two-sided **p = 0.00035**); **holding regime fixed at `uptrend`, 17.4% vs 31.3%,
p = 0.0045** — regime does not explain it. Compliance with the letter is perfect (28 post-P0
shorts, 25 `watch_only` + 3 `skip`, **0 sizing violations**, counterfactual fields preserved
28/28). Phase 3.2: the statistic the P0 rests on is `ALL/short` McNemar **−14.5pp, p = 0.0026,
BH-surviving**, and it only stays measurable if shorts keep resolving.

**Priority.** **P1.** Verbatim provenance, cross-regime dataset, clear significance — but it is
a *drift-of-intent* finding, not a calibration break, and the book is not losing money on it
today. Not P0.

**Risk.** Generating shorts the desk will never size costs Phase-1 context budget and can read
as noise on the board. Mitigation is cheap: they are already `watch_only`, already excluded from
sizing, and the counterfactual they feed is the single strongest piece of evidence this system
has produced in twelve audits. The real risk is the other way — if the short book thins to
nothing, the P0 becomes unfalsifiable and we can never learn whether the deficit was regime-
specific.

---

## P1 #2 — Add `vol_long` to the canonical `dominant_signal_class` set (or map it)

**What.** The 2026-08-15 P2 #7 fix collapsed off-list class labels from 14 distinct values to 1
— but the survivor is **new**. Either add `vol_long` to `x-canonical-classes` or instruct the
emitter to map long-vol structures onto the existing `high_iv_rank` / `event_vol` labels. Pick
one and state it in the schema; the emitter is currently inventing a label the validator warns
on.

**File.** `schemas/decision_envelope.schema.json` (`x-canonical-classes`) and
`.claude/agents/signal-confluence-quant.md` (the class list).

**Phase / Data.** Phase 1 data-quality flag #1 + Phase 6.6: validator warns on **5 post-fix rows**
(2026-08-18 LITE, NBIS, AMAT, CRWV, SNDK). All 5 `vol_long` rows in the corpus are post-fix.
Phase 3.1 already has to carry `vol_long` as a THIN_N appendix class (n=5, realised 0.00).

**Priority.** **P1.** Small, mechanical, and it stops the collapse map from growing a
fourteenth time. Each new off-list label silently re-fragments a class denominator, which is the
exact defect P1 #1 spent a cycle fixing on the *tool* side.

**Risk.** Effectively none. Worst case a label is mapped to a class it does not perfectly fit,
which is strictly better than a class of one.

---

## P1 #3 — Require a confirmation leg before a hygiene-corrected term-structure label may size a vol trade

**What.** `scripts/term_structure_hygiene.py` re-derives the IV term structure after dropping
the 0DTE bucket and thin tenors — it *corrects* a label. Where that corrected label is the
proximate justification for a vol structure, require a second, independent confirmation (a VRP
reading, a realised-vs-implied check, or flow alignment) before the structure may be proposed at
better than `watch_only`. This is a **procedure** change in the vol lane, **not** a rubric weight
change — the frozen `vol_term_structure(+/−)` point is untouched.

**File.** `.claude/agents/vol-surface-scout.md` and `.claude/agents/earnings-scout.md`.

**Phase / Data.** Four independent instruments on one lane:
Phase 4 — `scripts/term_structure_hygiene.py` **−16.9pp, n=42, p = 0.003, the first
BH-surviving tool result in twelve cycles**; the rest of the vol toolchain negative in a block
(`term-skew` −10.5/n=93, `front-end-iv-ratio` −10.4/n=40, `iv-term-structure` −4.8/n=64,
`insights earnings-play` −11.2/n=12).
Phase 5.1 — `vol_term_structure(+/−)` **−10.3pp on n=137**, negative in **both** tapes
(−6.1 up / −13.4 down), p = 0.018 raw.
Phase 2 — `vol` horizon realises **36.7%** vs a 40.2% book; **`vol_short` 34.0% (n=97)**.
Phase 3.1/3.3 — `earnings_vol` 0.87 → 0.38 (n=130, BH p<0.001) and `high_iv_rank` 0.77 → 0.47
(n=30, BH) are the confident tail of the reliability diagram.

**Priority.** **P1, deliberately not P0.** The BH survivor is real but **confounded**: 36 of its
42 rows are August 2026, the weakest month in the corpus (0.318 vs 0.401 July / 0.410 June), and
its sign is *opposite* the same script's reading one cycle ago (+34.1pp on n=9) under a looser
normalization. This is the **first clean measurement** of it. The within-August control holds
(0.194 n=36 vs 0.380 n=71; August vol rows 0.174 n=23 vs 0.348 n=23) but is single-regime.
Registered as **C61** (Phase 5.4) for out-of-sample confirmation.

**Risk.** A confirmation leg will suppress some genuine vol dislocations, and the vol lane is
already the thinnest source of sized calls. The mitigating fact is that this lane has produced
**no** sized winner in the post-freeze corpus and four separate instruments say it is where the
book bleeds. A confirmation requirement is also reversible in one edit if C61 fails its bar.

---

## P2 #4 — Register and watch the fundamentals VETO inversion; do **not** loosen it

**What.** Add a standing instrumentation note that `veto_fp_rate` is tracked per audit, and
require the `fundamentals-gate` agent to record *why* it VETOs (which of earnings-surprise
streak / insider MSPR / leverage / news catalyst fired) so a future audit can grade the legs
separately instead of the verdict as a whole.

**File.** `.claude/agents/fundamentals-gate.md` (add a `veto_reason[]` field to its output
contract) and `schemas/decision_envelope.schema.json` (optional additive field).

**Phase / Data.** Phase 6.4a: `veto_fp_rate` **0.562 → 0.500 → 0.474 → 0.545** across four
cycles — it has now converged from *below* the book to *above* it. VETO 0.545 (n=22) >
CONFIRM 0.391 (n=110) > CAUTION 0.342 (n=120): the ordering is inverted end to end. Phase 6.4:
`fundamentals` is simultaneously the weakest gate on downgrade-effectiveness (**−2.2pp**, vs
−26.2 cluster / −18.3 panic / −14.5 vrp).

**Priority.** **P2.** Two instruments agree, but n=22 on the VETO arm and **C24 explicitly
forbids loosening or removing a gate on thin effectiveness data** — a gate's value is insurance
against the regime not yet in the dataset. The actionable move is *instrumentation*, so the next
audit can grade the four VETO legs separately rather than a single blended verdict.

**Risk.** None to the book — this adds a field, changes no behaviour. The risk of *not* doing it
is that the VETO inversion stays uninterpretable for another four cycles.

---

## P2 #5 — Raise the `dp_block_to_float_ratio` emission rate (C16's only blocker)

**What.** The 08-15 backfill duty worked — the field now populates. It just does not populate
often enough. Make the ratio a **required** computation on every `dark_pool_accumulation` and
`oi_build` row where `fz_context.available == true`, rather than a best-effort backfill.

**File.** `.claude/agents/fundamentals-gate.md` (backfill duty → required) and
`.claude/agents/accumulation-hunter.md` (emit float alongside the block).

**Phase / Data.** Phase 4 / Phase 6.6: populated on **10 of 275** calls carrying the key, 9
decided — and it immediately produced the most interesting single pattern in this audit:
**perfect rank separation**, the two largest ratios (0.0023 NBIS, 0.0022 SNDK) the only two
WINs, all seven rows ≤0.00058 LOSS (random-assignment p = 0.028). Pre-registered as **C62** with
the threshold **fixed at 0.0010** so the next audit tests it out of sample instead of re-fitting.
At ~2 populated rows/week, C62's n≥30 bar is ~15 weeks away; at a required-emission rate it is
~4. The validator already flags the misses (2026-08-17 GLD).

**Priority.** **P2.** It is an instrumentation change gating an *advisory* criterion — no rubric
point moves, and C62 cannot be promoted until it clears its own bar.

**Risk.** A float lookup on every accumulation row costs `fz` calls and can fail on ADRs and
recent IPOs. It must **graceful-skip** exactly as the rest of the `fz` layer does — a missing
float must never block or downgrade a call.

---

## Standing decisions — reaffirmed, no change

| item | decision | evidence |
|---|---|---|
| **Rubric freeze `2026-06-12`** | **KEEP** | Phase 5.1: **0 BH survivors in the 19-line component family, 12th cycle.** Phase 5.2: cuts non-monotone at the ≥9 HIGH cut (`[0.395, 0.417, 0.500, 0.385]`), 9th failed re-confirmation. |
| **Freeze-lift** | **UNRUNNABLE, 10th cycle** | Phase 5.2: 489 resolved post-freeze calls (16× the n≥30 bar) against **0 decided HIGH and 0 decided MEDIUM**. The freeze is not the blocker; the fleet's gates are. |
| **P0.6 out-of-regime half-cap** | **KEEP** | Phase 3.6 / 5.3: out-of-regime 0.326 vs in-regime 0.407 (Δ −8.2pp), excess −23.5pp, n=43. **7th consecutive negative measurement.** |
| **Fractional-Kelly sizer** | **STAYS OFF** | Phase 3.5: gate returns `ADVISORY_ONLY` — n=27 (<30) **and** tier×expectancy non-monotone (LOW −1.784 / MED −2.239 / HIGH −1.965). Win-rate ladder remains the live sizer. |
| **All nine risk gates** | **KEEP ALL** | Phase 6.4: every gate with a measurable arm is effective (−8.8pp to −39.8pp). Not one is anti-effective. C24 bars removal. |
| **C56 `[0.55,0.65)` band** | **DO NOT ACT — 3rd cycle waiting** | Phase 3.3: post-fix denominator **19 of a required 30**, did not advance. Pooled n=52 is the era-mixing trap `signal-confluence-quant.md:71` warns about and it has already caught two audits. Sizing discipline holds: all 22 post-fix in-band rows `skip`/`watch_only`/`veto`, **zero sized, 13 cycles**. |
| **C15, C18** | **RETIRED — confirmed dead** | Phase 4: C15's trigger never met (0 HIGH squeeze readings in 198 populated rows; 0 of 22 short rows). C18 `insider_cluster_flag` **`False` 22/22**, zero variance. |
| **C17** | **OPEN, advisory** | Phase 4: n=14 divergent, WR 0.571 vs 0.402 book. Above the N≥5 floor, far below actionable, not BH-tested. |
| **The long book's edge** | **STILL NOT SIZED — and that is still the open question** | Phase 3.2: `ALL/long` **+13.9pp, p = 0.0003, BH-surviving, 4th consecutive cycle and its strongest reading yet**; present in both tapes (+11.3 up / +15.5 down), so not beta. No recommendation is made to size it — the tier ladder that would have to carry it is inverted (Phase 3.4, 5.2) and the vehicle does not exist yet. Flagged as the standing strategic question, not a patch. |

---

## What this audit did *not* find

No P0. No calibration-breaking defect. No agent-prompt drift on any risk gate (0.41% missed-gate
rate across 1,226 non-DROP obligations). No anti-effective gate. No BH-surviving rubric
component. No tool-tier change that survives its own confound.

**Four of the five 2026-08-15 recommendations landed clean and are verifiable in the very next
cohort** (Phase 6.6). For the third consecutive cycle the correct output of this audit is a
short list of instrumentation items and a reaffirmation of the freeze — which is what a
calibration system looks like when it is working.
