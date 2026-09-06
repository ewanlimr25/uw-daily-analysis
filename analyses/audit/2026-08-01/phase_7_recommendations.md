# Phase 7 — Recommendations (2026-08-01)

**PROPOSE-ONLY.** Nothing outside `analyses/audit/2026-08-01/` was written or edited.

Provenance is **100% verbatim** (58/58 validated envelopes) and the dataset is
**cross-regime** (232 up-tape / 269 down-tape decided rows), so the C23 P0 eligibility bar
is met. The rubric freeze is untouched: no weight edits, no cut re-bins.

Voice: chief of staff, multi-strat fund.

---

## P0 — act before the next session

### 1. Stop the fleet from sizing short theses; route them to watch-only

**What.** The short book's negative edge is no longer suggestive — it is BH-surviving on a
row-matched test, and it is regime-independent. Until a short-selection mechanism is
identified and validated, short theses should not receive size; they should be emitted as
context/hedge-flags only. This is a **sizing-procedure** change (explicitly in scope under
the freeze, which governs rubric weights and tier cuts, not the routing of a direction).

**File.** `.claude/agents/risk-monitor.md` (gate stack — add a directional-routing rule);
`.claude/commands/daily-analysis.md` Step 5 sizing; `.claude/agents/signal-confluence-quant.md`
(pre-risk size emission for `direction == short`).

**Phase / Data.** Phase 3 §3.4: `ALL / short` paired McNemar **p=0.0115, BH-surviving**,
b=24 / c=46 on n=163 — the book loses discordant pairs to a naive same-window SPY short
roughly 2:1. Phase 3c: negative in **both** tapes and by the same magnitude (UP −13.0pp,
DOWN −14.1pp) — mis-selection, not mistiming. Direction-call accuracy **36.0%** in a
falling tape. Phase 3c: sized book in a down-tape **0.294** vs a DROP pile of **0.411**,
replicated exactly from 07-25. Phase 5 §5.6: **C52's acceptance bar is now met.**

**Priority.** **P0** — verbatim provenance, cross-regime, BH-surviving, row-matched, and
replicated across two independent windows. This is the first P0 this system has ever
earned against the *subject* rather than the auditor.

**Risk.** This is the audit's most invasive proposal. Three things could go wrong.
(i) The short book is small (163 decided, 47 sized total across both directions) — the
McNemar is significant but the economic sample is modest. (ii) Removing short sizing
removes the fleet's only expression of a bearish view, which in a genuine bear market is
the wrong time to lose it — the C24 insurance principle cuts against acting here.
(iii) The benchmark is a *naive index short*, which in this corpus resolved at 0.595;
"worse than an easy alternative" is not "loses money" (book shorts realised 0.460).
**Mitigation:** implement as routing-to-watch-only, not suppression — keep emitting the
theses and keep resolving them, so the next audit can grade the counterfactual. Do not
delete the short lane.

---

## P1 — clear improvement

### 2. Re-source `sector_rotation` off the netted sector line

**What.** Pre-registered as **C55**. The `sector_rotation` class reads
`options-flow sector-flow-persistence` — a **gross-turnover** metric (net_flow = gross
call$ − put$, sign-agnostic) — as though it measured net accumulation. Re-source the
class's directional read off `uw market-regime`'s `sector_rotation` field, the only netted
source. Registered as a pre-registration under the freeze; **not** a weight edit.

**File.** `.claude/agents/sector-rotation-strategist.md` (evidence line + direction
derivation).

**Phase / Data.** Phase 3 §3.1: realised **0.25 on n=32** against a 0.54 claim,
BH-surviving at **p=0.002** — the worst realised win rate of any class with real N.
Phase 5 §5.1: the `sector_persistence` 0-point emission reads −44.2pp (n=8), corroborating.
Phase 4: `options-flow sector-flow-persistence` marginal −1.0pp (n=57), NO-INFO.

**Priority.** P1 — BH-surviving with real N, and the mechanism is already documented.
Held below P0 only because the fix is a re-derivation whose replacement has not itself
been validated. **Risk.** The netted source may simply be noisier; C55's acceptance bar
(cross-regime, n≥30/arm, BH-surviving) must decide it, not this audit.

### 3. Fix the `earnings_vol` and `high_iv_rank` win-rate quotes

**What.** Both vol-lane classes quote confidence the data has refuted for four to five
consecutive audits. This is a **win-rate emission** item — sizing procedure, in scope under
the freeze. Cap or re-derive the quote for these two classes; do not touch their rubric weight.

**File.** `.claude/agents/signal-confluence-quant.md` (win-rate emission per class).

**Phase / Data.** Phase 3 §3.1: `earnings_vol` claims **0.88**, realises **0.44** on
**n=97**, BH-surviving p<0.001 — the largest and most durable miscalibration in the book.
`high_iv_rank` claims **0.82**, realises **0.50** on n=24, BH-surviving p=0.001. Phase 3
§3.3: the [0.80,0.90) reliability bucket realises 0.43 against 0.83 predicted on n=30.

**Priority.** P1. **Risk.** Both are pre-cap legacy quotes — the 2026-06-06 ceiling already
binds post-freeze emissions to ≤0.80, so part of this is already fixed going forward and
the recommendation risks re-fighting a won battle. Verify the post-freeze subset before
patching; the durable part of the finding is the *realised* 0.44, not the 0.88 quote.

### 4. Fix the `[0.55,0.65)` quote itself, not just its size

**What.** Pre-registered as **C56**. The 07-25 floor worked — every in-band post-fix row
sizes to `skip` — but the band's share of emissions rose from 25.0% to **73.3%** while
realising ≈0.29 against ~0.58 predicted. The rubric's modal confidence statement is
negatively informative. Re-derive or suppress the quote in that range.

**File.** `.claude/agents/signal-confluence-quant.md`.

**Phase / Data.** Phase 3 §3.3/§3.3b: [0.55,0.60) realises **0.27** (n=22), [0.60,0.65)
realises **0.33** (n=12). Post-fix: 11/15 quotes in-band, all sizing to `skip`, 15/15
`backtest_clean`.

**Priority.** P1. **Risk.** Low — the sizing consequence is already neutralised, so this is
about not printing a misleading number to a human reader. Acting before n≥30 post-fix rows
accrue risks fitting to 15 observations; C56's bar should govern.

### 5. Add `dp_block_pct_of_float` to the envelope — C16 is on its 4th untestable audit

**What.** One additive, backward-compatible schema field. The other half of 07-25's P1 #5
shipped and worked; this half did not.

**File.** `schemas/decision_envelope.schema.json`; `.claude/agents/accumulation-hunter.md`.

**Phase / Data.** Phase 4 `fz` table: C16 verdict `NA — per-call DP-block/float ratio not
in envelope`, unchanged across four audits. By contrast `insider_cluster_flag` — shipped
at 07-25 — now populates **44/44** post-fix calls and **unblocks C18** for the next cycle.

**Priority.** P1. **Risk.** None material; additive and validator-safe.

### 6. Keep the freeze. Keep the half-cap. Keep every gate.

**What.** No change — recorded so the decision is explicit.

**Phase / Data.** *Freeze:* Phase 5 §5.3 — 354 resolved post-freeze calls but **0 HIGH and
0 MEDIUM**, so the lift test is structurally unrunnable for a 7th cycle; zero of 17
component lines survive BH for a 9th. *Half-cap:* Phase 5 §5.4 — out-of-regime 0.326 vs
in-regime 0.445, **Δ −12.0pp on n=43**, negative in all four audits that have measured it.
*Gates:* Phase 6 §6.3 — all nine grade effective or advisory, none anti-effective,
`cluster` at −28.0pp. **Priority.** P1.

---

## P2 — polish / monitor

### 7. Monitor `veto_fp_rate` — do **not** loosen

VETO'd names realised **0.562 (n=16)** vs a 0.435 book — anti-effective on its face. But
n=16 is barely past the C24 floor, the same agent's CAUTION verdict grades correctly
(0.369 vs 0.476 CONFIRM), and most VETO'd names were killed by other gates anyway. The
skill's hard rule forbids loosening a gate on thin effectiveness data. Phase 6 §6.4. **P2.**

### 8. Retire or re-scope C15

Of 18 short rows carrying `fz_context`, **zero** clear `short_float ≥20% ∧ days_to_cover ≥5`
— for a second consecutive audit. Squeeze pressure distributes LOW 91 / unknown 44 /
MODERATE 6. C15 is untestable **by construction** on a mega-cap flow universe, not merely
under-powered. Phase 4. **P2.**

### 9. Constrain `dominant_signal_class` to an enum

31 distinct class strings, 12 appearing ≤2 times. Every audit re-implements a
`canonical_class` collapse in `phase2_resolve.py`. An enum in the schema would remove a
standing source of audit-side judgment. Phase 1 data-quality flag. **P2.**

### 10. Pre-registrations carried forward

- **C50** — `dealer_dex_flip +3` tape-conditional: **−36.0pp up-tape / +4.2pp down-tape**
  (n=31), essentially unmoved from 07-25's −34.9/+4.1. Bar: n≥30 per tape arm, both arms
  same sign, BH-surviving. Fires rarely; will take many cycles.
- **C51** — `accumulation_conjunction +3`: +1.9pp at the +1 emission (n=42), **−0.7pp at
  the +3 emission (n=14)**. The heaviest weight in the rubric has no measurable marginal
  contribution. Bar: n≥30 per arm, ≥2 regimes, BH-surviving.
- **C55** (new) — `sector_rotation` re-sourcing; see item 2.
- **C56** (new) — `[0.55,0.65)` quote re-derivation; see item 4.
- **C52** — **MET this cycle**; promoted to item 1 above.

---

## What did NOT change and why

- **No rubric weight or tier-cut edits.** Zero of 17 component lines survive BH for a 9th
  consecutive audit; the freeze exists precisely to stop re-weighting correlated lines on
  n=8–31 BH-null data.
- **No tool tier movements.** Ninth consecutive BH-null tool table; smallest p in the sweep
  is 0.194. `dark-pool block-stratified` now reads WR-with 0.42 vs WR-without 0.44 — the
  07-11 "isolate it" pre-register stays refuted.
- **No gate removals or loosenings.** Every gate grades effective; the one anti-effective
  reading is n=16 and forbidden by hard rule.
- **No agent-file drift patches.** Phase 6 §6.6: **0/42 missed gates on the live rubric
  across all nine gates.** The 67.9% `debate` figure is entirely pre-freeze rows predating
  the stage's existence.
- **No Kelly activation.** Gate returns `ADVISORY_ONLY` at n=27 < 30, tier expectancy
  non-monotone, three of four tiers negative.
