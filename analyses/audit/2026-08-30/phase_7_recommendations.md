# Phase 7 — Recommendations (2026-08-30)

**Propose-only.** Nothing outside `analyses/audit/2026-08-30/` was edited. Every item cites
its phase and data point. Provenance is **100% verbatim envelope** (82/82 validator-clean,
0 prose reconstruction), so the C23 P0 cap does not bind this cycle.

**One P0 — the first subject-side P0 since 2026-08-01, and the first ever on the vol lane.**

---

## P0 #1 — Stop proposing short-vol structures until an expansion-veto clears

**What.** The vol lane's **short leg is adversely selected**. Require an independent
expansion-veto before any `vol_short` / short-premium structure may be proposed; absent one,
route it to `watch_only`. The long leg is untouched — it works.

**File.** `.claude/agents/vol-surface-scout.md`, `.claude/agents/earnings-scout.md`
(proposal path), `.claude/commands/daily-analysis.md` + `.claude/commands/weekly-analysis.md`
(Step-5 routing block, mirroring the 2026-08-01 short-direction routing paragraph).

**Phase / Data.** Phase 3.2: `vol_short` book **31.5%** vs **unselected same-date single-name
peers 56.6% = −25.1pp** on n=111 strict-window rows; paired McNemar against the peer-median
partner **b=2, c=57, p < 0.0001**. **4 of 4 regime buckets negative and each individually
significant** (uptrend −20.2pp p=0.0018 · pullback −35.1pp p=0.0034 · choppy −23.5pp p=0.0020
· transitional −25.5pp p=0.0000). 3 of 4 months negative-significant. Loose-window −33.6pp on
n=134, BH-surviving in the pre-registered vol family. `vol_long` runs the other way:
**+9.5pp, McNemar p=0.0034**, and **5-for-5 on sized rows**. Phase 3.2 exposure: `vol_short`
is **20 of the 48 sized rows in the entire corpus — 42% of every position the fleet has ever
taken.** Corroborated by Phase 2 (`vol_short` 8.3% in August against an index that contracted
88% of the time), Phase 3.3 (`earnings_vol` claims 0.87, realises 0.33, n=144, BH-surviving)
and Phase 5.1 (`vol_term_structure(+/−)` −13.4pp, the sole BH survivor of 24 component lines).

**Why this is a P0 and not another registration.** It survived three deliberate falsification
attempts. *The tape:* August was a short-vol paradise at the index (mean SPY RV ratio 0.738,
12% of windows expanded) while the book's own names ran 1.199 — the confound runs **opposite**
to the excuse. *The instrument:* single names do contract less often than the index (62.8% vs
79.1% on the same dates), and correcting for it with a single-name peer benchmark still leaves
−25.1pp. *Name selection:* if the fleet merely picked volatile names, `vol_long` would lose
too; it gains. What remains is a **sign error** — the scouts locate vol-expansion candidates
correctly and then sell vol into the expansion.

**Priority.** **P0.** Verbatim provenance at n=111, row-matched, cross-regime, BH-surviving,
and it is the single largest real-money exposure in the book's history.

**Risk.** Two, both stated plainly. (1) **The resolver is an RV-direction proxy, not
IV-vs-RV** — a premium seller can lose this test and still book P&L if IV sat above realised.
The −25.1pp therefore prices **selection**, never P&L, and must never be quoted as a P&L
claim. Both benchmark columns remove the common component, which is what makes the selection
reading survive the caveat. (2) Short-vol is a genuine institutional edge in the right
conditions; a blanket veto could tax the good version. Mitigated by making this a
**veto-with-an-out** (an independent expansion check), not a ban — and by the fact that the
lane is already unsized (38 straight empty daily boards), so this changes what is *proposed*,
not what is currently *held*.

**Registered as C63** (Phase 5.5) so the **fix** is graded: post-change `vol_short` peer-excess
must reach ≥ −5pp on n ≥ 40 decided rows across ≥ 2 regime buckets by the 2026-10-03 audit.

---

## P1 #1 — Log *why* the fundamentals gate VETOes

**What.** Add a required `veto_reason` / `caution_reason` enum to the fundamentals-gate
output and carry it into `decision.json` `calls[]` (advisory, 0 rubric points, never a
`score_components` line).

**File.** `.claude/agents/fundamentals-gate.md`, `schemas/decision_envelope.schema.json`,
the `calls[]` enumeration in both command files.

**Phase / Data.** Phase 6.4: `veto_fp_rate` = **0.524 (n=21)** against CONFIRM **0.376
(n=117)** and CAUTION **0.328 (n=131)** — VETO'd names win **14.8pp more** than confirmed
ones. Trajectory 0.562 → 0.500 → 0.474 → 0.545 → **0.524**; second consecutive cycle with
VETO > CONFIRM, now past the ≥10-decided actionability floor.

**Priority.** **P1.**

**Risk.** None to the book — this is instrumentation only and changes no gate, no score, no
size. The real risk is the opposite one: **do not read this as licence to loosen the gate.**
C24 forbids gate-loosening on effectiveness data, and the fundamentals VETO is the mechanism
that caught the merger-arb and dividend-capture blind spots on the register. Without reasons
logged, the audit can only ever say "VETO'd names win," which is unactionable forever.

---

## P1 #2 — Switch the auditor's pin resolution to the settlement rule (C64)

**What.** For `resolution_mode == "pin"`, make `outcome_settle` the headline outcome and keep
the touch rule as `outcome_touch` for continuity with the prior twelve audits.

**File.** `analyses/audit/<date>/phase2_resolve.py` (**auditor-side only** — no subject file
changes).

**Phase / Data.** Phase 2, C59 decision: bar was ≥3 of 9 divergent rows; measured **5 of 11**.
TOUCH 2/11 = **18.2%**, SETTLEMENT 7/11 = **63.6%** — a 45.4pp swing on identical rows. Four
of the five divergent names settled within **0.21% of entry** after brushing a wing intraday
(XLF 0.05%, NVDA 0.12%, NVDA 0.21%, PFE 0.00%).

**Priority.** **P1.** C59's pre-registered bar is cleared on its own terms.

**Risk.** `opex_pin`'s realised rate jumps 18.2% → 63.6%, which will look like a sudden edge
appearing. It is not — it is the same eleven trades scored against the payoff an iron fly
actually has. Every prior audit's `opex_pin` figure must be treated as superseded, not
compared against.

---

## P1 #3 — Re-measure short generation before it becomes a quota

**What.** No edit yet. Add short share of board (overall and regime-controlled) to the
standing Phase-6 follow-through table and re-measure next cycle.

**File.** none this cycle (auditor watch item).

**Phase / Data.** Phase 6.5: the 08-22 generation floor worked — 17.6% → **44.2%**
(Fisher p = 0.0003), regime-controlled `uptrend` 17.4% → **60.0%** (p = 0.0007). But post-fix
share is now *above* the pre-P0 baseline: 44.2% vs 32.0% overall (p = 0.0896, ns) and
**60.0% vs 31.3% at fixed uptrend regime (p = 0.0422)** on n=15.

**Priority.** **P1** as a measurement obligation, **not** an edit.

**Risk.** Acting now on n=15 would be exactly the single-window overcorrection the freeze
exists to stop — and would be the third swing of the same pendulum. Do nothing but watch.

---

## P2 #1 — Retire `insider_cluster_flag` / C18 rather than re-recommending it

**What.** Mark C18 CLOSED-as-unmeasurable and drop the backfill duty from
`fundamentals-gate.md`; keep the field schema-present but stop treating its absence as a gap.

**File.** `.claude/agents/fundamentals-gate.md` (backfill-duty paragraph),
`.claude/agents/accumulation-hunter.md`.

**Phase / Data.** Phase 6.5: **30 populated values, every one `False`.** Zero variance across
five audits and 15 populations (C18 was already called dead 2026-08-08). The emission fix
worked; the field simply never fires.

**Priority.** **P2.** Housekeeping — it removes a standing duty that cannot pay off.

**Risk.** If insider clustering ever does start firing, the detector is gone. Mitigated by
keeping the schema field and the accumulation-hunter computation; only the *duty* and the
audit's expectation retire.

---

## P2 #2 — Fix the auditor's `fz_context` lookup path

**What.** `phase4_tools.py` reads `fz_context.dp_block_to_float_ratio`; the schema and both
emitters write **`calls[].dp_block_to_float_ratio`**.

**File.** `analyses/audit/<date>/phase4_tools.py` (auditor-side only).

**Phase / Data.** Phase 4.4: the helper reported *"NA — per-call DP-block/float ratio not in
envelope"* while the field was populated on 13 calls, **10 of 13 August `dark_pool_accumulation`
rows**. Corrected inline this cycle.

**Priority.** **P2.**

**Risk.** Any prior-cycle "not emitted" claim sourced from that helper is unverified and
should be re-derived from the schema path before being cited again.

---

## Explicitly NOT recommended

| item | why not |
|---|---|
| **Apply C60** (`vol_term_structure(+/−)` weight) | Phase 5.2: all three statistical conditions pass (BH p=0.001 sole survivor; UP 89 / DOWN 94; 4 regime buckets) — but **only 9 of 183 rows (4.9%) are out-of-sample since registration**, and the window opens **2026-10-03**. Clearing a bar by re-resolving the rows that generated the hypothesis is the self-grading failure the window exists to prevent. **Hold, unchanged, unrenegotiated.** |
| **Lift the rubric freeze** | Phase 5.3: 546 resolved post-freeze rows, **0 decided HIGH, 1 decided MEDIUM**, 11th cycle. The lift is unrunnable and the freeze is not the blocker. |
| **Lift the P0.6 out-of-regime half-cap** | Phase 5.4: −6.4pp (43 vs 650), 8th consecutive negative reading. Cap is protective. |
| **Promote C62** (float-normalized DP block) | Phase 4.4: **11 of 30 decided, 2 of a required 10 in the upper arm.** Separation is +88.9pp but it is the same post-hoc n=9 pattern plus one confirming low-arm row. |
| **Decide C61** (`term_structure_hygiene.py`) | Phase 4.2: **non-August n = 7 of a required 30**, up one row in a week. The confound worsened. Keep last cycle's confirmation-leg rule — it is protective and reversible — but record that it stands on C61's promissory note, not on C61. |
| **Act on C56** (`[0.55,0.65)` band) | Phase 3.5: 21 of 30 post-fix decided. Compliance perfect (0 sized above starter, 14 cycles). Wait. |
| **Flip the Kelly sizer live** | Phase 3.6: gate returns `ADVISORY_ONLY` — n=27 of 30, tier × expectancy non-monotone. |
| **Loosen or remove any risk gate** | Phase 6.4: all nine measurable gates effective (−4.0 to −42.0pp). C24 forbids it regardless. |
| **Demote the term-structure tools** | Phase 4.1: `term-skew` is **+5.3pp *inside* the `vol_short` lane**; its −8.3pp headline is the lane's base rate, not the tool's contribution. The defect is the direction traded, not the instrument. |
| **Any agent-file drift patch** | Phase 6.3: **5 missed gates in 1,262 non-DROP obligations = 0.40%.** No gate near the 20% threshold. |
