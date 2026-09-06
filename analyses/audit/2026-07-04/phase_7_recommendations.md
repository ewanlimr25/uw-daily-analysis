# Phase 7 — Recommendations · 2026-07-04

Voice: chief of staff, multi-strat fund. **Propose-only** — nothing outside `analyses/audit/2026-07-04/` is touched.

**Provenance: 100% verbatim envelope** (first audit with zero reconstructed rows) — the provenance cap does not bind this run. **P0 still requires cross-regime ∧ BH-surviving ∧ act-before-next-session materiality. Nothing clears all three:** the only BH survivors are (i) the two vol liar classes, whose realised WR is RV-proxy-clouded and whose containment (emission cap + empty-book skips) is *already live and verified*, and (ii) `multi_day_sweep`, which fails independence (8 rows = 4 underlyings). **No P0 this run.**

**Continuity vs 2026-06-27 (all four P1s were applied in `23fdab7` — this audit grades them in the wild):**
- *Rec 1 — no short alpha-sizing anywhere* → **CONFIRM.** Short book −22.9pp blended (n=89 benched); −34.3pp uptrend / −21.4pp pullback. New: the choppy stratum's shorts ran +14.3pp (n=7, thin) — the first positive-excess short cell ever observed; a watch-item, not a reversal (n=7, one week, one tape).
- *Rec 2 — long edge is uptrend-conditional* → **CONFIRM + first counter-stratum datum.** Uptrend +29.1pp (n=55) / pullback +6.3pp (n=49, NS) / **choppy −33.3pp (n=3)** — the first decided read of longs off-trend is negative, exactly the trap Rec 2 warned against.
- *Rec 3 — bind ≥0.80 ceiling at emission* → **APPLIED & VERIFIED WORKING.** Zero uncapped leaks post-06-29; the three at-ceiling 0.80 quotes (07-02, `high_iv_rank`, uncapped 0.9207, `backtest_clean`) were all DROP/skip. Close the loop item.
- *Rec 4 — hold freeze + half-cap + gates* → **CONFIRM + UPGRADE.** The OOR half-cap grading crossed its n≥10 floor: **protective on actionable N** (0.25 WR / −21.5pp vs in-regime 0.455 / +0.6pp, n=20). All nine gates net-protective, second clean sweep.

**Freeze-lift verdict: KEEP (cannot run, 4th consecutive).** post_freeze_decided=117 ≫ 30, but HIGH n=0 / MEDIUM n=0; the revised (Rec-7b) criterion also fails on post-freeze book excess −8.8pp.

---

### 1. Fix the `claimed_win_rate = 0.0` emission bug — degenerate quotes must emit `NA(substrate)`, not 0.0
**What.** When the win-rate substrate returns a degenerate 0.0 (empty conditional cell), emit `win_rate: null` / `win_rate_source: "NA(substrate)"` instead of a literal 0.0 forecast. **File.** `.claude/agents/signal-confluence-quant.md` (win-rate emission rule — same section as the 0.80 ceiling). **Phase/Data.** Phase 6 §1: two live multi_day_sweep setups (MRVL 06-08/06-09) quoted 0.0; Phase 3 §3: the [0,0.50) reliability bucket under-claims (pred 0.36 → realised 0.50, n=50), partly this bug. Mirror-image of the ≥0.80 leak the desk already fixed — the rubric now lies pessimistically at the bottom the way it lied optimistically at the top. **Priority.** P1. **Risk.** Minimal — 0.0-quotes currently route to skip (conservative), so the fix changes bookkeeping, not sizing; the risk of *not* fixing is corrupted calibration math in every future audit.

### 2. Keep every protective control — freeze, half-cap (now actionable-protective), OOR cap, all nine gates, Kelly ADVISORY_ONLY
**What.** No loosening anywhere; explicitly re-affirm on upgraded evidence. **File.** `.claude/agents/risk-monitor.md` (hold ruling; no text change strictly required). **Phase/Data.** Phase 3b: OOR n=20 → 0.25 WR / −21.5pp (first actionable protective grading); Phase 6: nine-gate protective sweep; Phase 3 §5: Kelly gate ADVISORY_ONLY (n=25 < 30; all-tier expectancy negative — monotone, but three flavors of losing); Phase 2: sized book 36.1% vs paper 45.2% (the calls we committed to did worst — the empty-book refusal to size is the system's best current behavior). **Priority.** P1 (hold ruling). **Risk.** Opportunity cost if the tape re-accelerates into a clean uptrend; accepted — asymmetry favors insurance while the frozen rubric's sized book has negative excess (−8.8pp, n=117).

### 3. Register C46 + C47; carry C40–C45 unchanged; apply NONE (5th BH-null tool audit)
**What.** Add two pre-registrations: **C46** (multi_day_sweep under-claim + emission integrity; bar: ≥15 distinct underlyings ∧ cross-regime ∧ BH ∧ non-degenerate claims) and **C47** (weekly +3 oi-trend rides a −9.2pp tool with W27-documented Gate-1 saturation; bar: cross-regime ∧ n≥30/arm ∧ BH on artifact-corrected read). Carry C40 (multileg — sign whipsawed again, 3 audits/3 signs), C41 (HIGH cut — still zero post-freeze evidence), C42 (hygiene applied; bar open on substrate + implied_move), C43 (schema enablers — fields still absent), C44 (DEX — mechanism *reinforced*: negative in all three off-uptrend strata), C45 (cum-flow ubiquity 0.56 + W27 §7(1) live failure mode). **File.** pre-registration register (append). **Phase/Data.** Phase 5 §4 in full. **Priority.** P2 (registering is zero-risk). **Risk.** Only procedural: a future audit applying any of these pre-bar.

### 4. Ship the C43 schema enablers this cycle — `implied_move` (+ entry IV), `dp_block_to_float_ratio`, `insider_cluster_flag`
**What.** Additive, backward-compatible envelope fields. Two audits in a row have had their vol verdicts proxy-clouded and their C16/C18 gates untestable for want of three fields. **File.** `schemas/decision_envelope.schema.json` + the emitting agent prompts (`vol-surface-scout`/`earnings-scout` for implied_move; `accumulation-hunter` for float ratio; `fundamentals-gate` for insider flag). **Phase/Data.** Phase 2 (vol book 100% `rv_direction_proxy`, n=52 decided vol rows ungradeable as true IV-vs-RV); Phase 4 fz table (C16/C18 NA). **Priority.** P1 (enabler — it gates three separate open questions and costs a few schema lines). **Risk.** Mild schema bloat; fields sit advisory until audits use them.

### 5. C17 (flow-vs-analyst divergence) — first positive scored read; keep advisory, define the promotion N now
**What.** No promotion (n=13, single-direction, not BH-tested), but the first scored read is positive: divergent rows 0.615 vs short-book 0.422 (+19.3pp). Pre-commit the promotion bar to avoid future goalpost-moving: n≥25 divergent decided ∧ both directions represented ∧ BH-surviving within the fz set. Also fix the W27 fz selector miss (§7(8): SI/analyst fields absent) so C15/C17 cells stop starving. **File.** register + `scripts/fz_enrich.py` (selector fix). **Phase/Data.** Phase 4 fz table. **Priority.** P2. **Risk.** None while advisory.

### 6. Watch-items (no action): choppy-stratum shorts; bull-debate monoculture
**What.** (a) Choppy shorts +14.3pp (n=7) — if the next audit's choppy cells confirm, the "no short alpha" rule earns a regime-conditional exception *hypothesis* (registerable then, not now). (b) Debate residuals show bull side binned at {0.55, 0.65} with bear winning 16/16 decided — healthy skepticism or anchored theatre; the model-transition monitoring (below) will re-measure the distributions under the pinned fleet. **Priority.** P2/watch. **Risk.** Premature action on either would be single-cell overfitting — the exact failure the register exists to stop.

---

## Model-transition section (obligation from `analyses/audit/2026-07-03/agent-model-effort-audit.md` §6)

**Status: pins applied 2026-07-03; ZERO post-pin fleet runs exist** (latest envelope 2026-07-02 ran all-agents-on-inherited-Fable). The §6 re-measurements cannot execute this audit; they are **carried forward as the first-priority section of the next audit**, with the premium-era baselines now frozen here for comparison:

| §6 obligation | Premium-era baseline (this audit) | Next-audit check |
|---|---|---|
| Σ invariant (quant) | 278/278; 0 post-freeze sizing violations | any post-pin Σ mismatch or upgrade-violation = escalation signal |
| 0.80 cap-at-emission | 0 uncapped leaks; 3 at-ceiling caps correctly labeled | any post-pin uncapped ≥0.80 quote = escalation |
| flow_conflict / gate firing | 9-gate firing 0.80–1.00; all protective signs | firing-rate collapse or sign flip on any gate |
| Debate residuals vs premium baseline | bull μ 0.589 σ 0.049 (binned {0.55,0.65}); bear μ 0.705 σ 0.108; n=33; bear won 16/16 decided | distribution shift (KS-style eyeball; wider bull tails OK, collapse-to-single-bin not) |
| VETO/CAUTION FP rate | VETO 0.50 (n=6, advisory) · CAUTION 0.457 (n=46) · CONFIRM 0.489 (n=47) | FP spike on sonnet-tier fundamentals-gate |
| C4 `opening_confirmed` evidence strings | not spot-checked this run (no post-pin envelopes to sample) | **spot-check ≥5 post-pin accumulation citations against raw ΔOI** |
| W23 no-file-writes rule | 0 violations (still never load-tested on sonnet-majority Phase 1) | any unprompted write ⇒ immediate escalation-to-opus for that agent |

**Recommendation (P1, process):** run the next `/calibration-audit` after ≥5 post-pin daily envelopes exist (~2026-07-10), even if that's ahead of the usual weekly cadence — the transition window is the one period where per-agent regression would be silent otherwise.

---

## Priority roll-up
- **P0:** none (BH survivors are proxy-clouded-and-already-contained, or independence-deflated).
- **P1:** #1 fix the 0.0-claim emission bug · #2 hold every protective control (OOR cap now actionable-protective) · #4 ship C43 schema enablers · model-transition early re-audit (~5 post-pin envelopes).
- **P2:** #3 register C46/C47 + carry C40–C45 (apply none) · #5 C17 promotion bar + fz selector fix · #6 watch-items.

Every item cites a Phase-N datum + n. No rubric weight/cut edits, no tool-tier changes, no gate loosening. No file outside `analyses/audit/2026-07-04/` is touched.
