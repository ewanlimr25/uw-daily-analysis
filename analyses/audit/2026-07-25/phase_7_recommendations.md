# Phase 7 — Recommendations (2026-07-25)

**PROPOSE-ONLY.** Nothing outside `analyses/audit/2026-07-25/` was written or edited.
Provenance is **100% verbatim** (52/52 validated envelopes) and the dataset is now
**cross-regime** (159 up-tape / 281 down-tape decided rows), so the C23 P0 eligibility
bar is met — but note that both P0 items below land on **auditor method**, not on the
frozen subject rubric. The rubric freeze is untouched.

Voice: chief of staff, multi-strat fund.

---

## P0 — act before the next audit

### 1. Stop leading with raw benchmark-excess; make tape-conditioned book WR the primary edge column

**What.** Demote `realised_excess` from headline statistic to a secondary column that
must always be printed beside its benchmark WR and a `sd(book)/sd(benchmark)` dispersion
ratio. Promote **book WR conditioned on realised tape** plus **paired McNemar** (each row
against its own row-matched SPY outcome) to the primary edge test.
**File.** `.claude/skills/calibration-audit/SKILL.md` — Phase 3 §1 (class table spec),
Phase 3 output spec, Phase 7 "edge before calibration" rule.
**Phase / Data.** Phase 3d: across 34 strata cells, `excess_pp = +36.5 − 80.0 × spy_wr`,
R² = 0.636, **71.1% of excess variance is the benchmark moving**; β(bookWR|spyWR) = +0.20.
`bearish_flow` books 0.533 up-tape / 0.526 down-tape (Δ 0.7pp) while its excess moves
15.6pp; `dark_pool_accumulation` books 0.400 in both while its excess moves 23.3pp.
Robust across n≥15, n≥25, extreme-cell exclusion and n-weighting (slope −73 to −88).
**Priority.** **P0** — this is calibration-breaking *for the auditor*. It has produced
three consecutive headline findings (07-11 "+29.4pp bearish edge", 07-18 "the sign
reversed", and the raw form of this run's table) that are substantially artifacts of the
denominator. Registered **C49**.
**Risk.** Over-correction. Excess remains the right concept and the paired long-book
result (§below) survives precisely because McNemar is row-matched. Do not delete the
column — demote and annotate it. If the fix is applied carelessly the audit loses its
only beta control.

---

## P1 — clear improvement

### 2. Close C19 as REFUTED rather than carrying it a seventh cycle

**What.** Retire the C19 bearish-flow/single-leg accrual. Six audits have logged
"`bearish_flow` shows positive excess but scores 0" as evidence of an unscoreable
down-tape edge awaiting graduation.
**File.** `analyses/audit/2026-05-25/improvement_criteria.md` (register entry C19);
note in `CLAUDE.md` §`uw options-flow single-leg`.
**Phase / Data.** Phase 3: `bearish_flow` realised 0.49 vs claimed 0.48 on n=94 (p=0.96
— the best-calibrated large class in the book). Phase 3c/3d: book WR 0.533 up-tape /
0.526 down-tape — stationary; the excess swing was the benchmark. Phase 3c McNemar
DOWN/bearish_flow p=0.2478, ns. Registered **C53**.
**Priority.** P1. **Risk.** The underlying `single_leg` PUT research (WR 0.635, n=266,
2026-05-29) was a *different* measurement on a different substrate. Closing C19 must not
be read as refuting that backtest — only the claim that the daily fleet's `bearish_flow`
class carries unscored edge.

### 3. Fix the missed-gate denominator — the 34% "drift" is DROP rows

**What.** Exclude `tier == DROP` rows from missed-gate denominators, or report the rate
per tier. Stop reporting an aggregate that treats the fleet's early-exit optimization as
non-compliance.
**File.** `.claude/skills/calibration-audit/SKILL.md` — Phase 6 "Missed-gate ledger".
**Phase / Data.** Phase 6.5: regime 0/7 HIGH, 0/20 MEDIUM, 0/94 LOW, **211/374 DROP**;
identical pattern for vrp, event_risk, fundamentals. 3 misses across 121 non-DROP rows.
Registered **C54**.
**Priority.** P1 — it has been mis-flagging `risk-monitor.md` for agent drift that does
not exist. **Risk.** A genuine future drift confined to DROP rows would be masked; keep
the DROP figure visible as a separate line.

### 4. Tighten win-rate emission in the [0.55,0.65) band

**What.** This is a **sizing-procedure** item, explicitly in scope under the freeze (the
freeze governs rubric weights and tier cuts, not the win-rate quote that drives the
sizing map). Either floor quotes in [0.55,0.65) down to the <0.50 starter/skip band, or
require `backtest_clean` provenance before a quote in that range can size.
**File.** `.claude/agents/signal-confluence-quant.md` (win-rate emission + cap logic).
**Phase / Data.** Phase 3.3/3.3b: [0.55,0.65) realised **0.179 overall and 0.133 on 15
post-freeze rows**, against ~0.58 predicted. 0.55 is the modal post-freeze quote (14
rows). Post-freeze `bullish_flow` claims 0.499 and realises 0.250 (n=20).
**Priority.** P1. **Risk.** This band feeds the half-size rung; flooring it pushes more
names to starter/skip and will shrink an already-empty board further. Given DROP has
outperformed the traded book in 6 straight audits, that risk is acceptable — but it does
mean fewer trades, and the desk should expect that.

### 5. Carry the `fz` fields the promotion gates need into the envelope

**What.** Add per-call `dp_block_pct_of_float` (C16) and `insider_cluster_flag` (C18) to
`calls[]`, and fix the `debate_residuals` bin floor (currently no bin below 0.55, which
erased TSLA's 0.42/0.40 residuals on 2026-07-23).
**File.** `schemas/decision_envelope.schema.json` (additive, backward-compatible);
`.claude/agents/fundamentals-gate.md`, `.claude/agents/risk-monitor.md`.
**Phase / Data.** Phase 4 `fz` table: **C16 and C18 have been untestable for three
consecutive audits** because the fields are not in the envelope. Phase 6.6: debate bin
floor defect, carried unfixed since 2026-07-23.
**Priority.** P1. **Risk.** Schema churn; both changes are additive and validator-safe.

### 6. Keep the freeze. Keep the half-cap.

**What.** No change — recorded so the decision is explicit.
**Phase / Data.** Freeze: Phase 5.3 — 293 resolved post-freeze calls but **zero HIGH and
zero MEDIUM**, so the lift test is structurally unrunnable for a 6th cycle. Half-cap:
Phase 5.4 — out-of-regime 0.317 vs in-regime 0.436, **Δ −11.9pp on n=41**, past the
actionable floor, negative in every audit that has measured it. **Priority.** P1.

---

## P2 — polish / monitor

### 7. Monitor the fundamentals VETO false-positive rate — do **not** loosen it

**What.** Track `veto_fp_rate`; take no action now.
**Phase / Data.** Phase 6.4: VETO'd names realised **0.545 (n=11)** vs a 0.425 book —
anti-effective on its face. But n=11 is barely at the C24 floor, 8 of 11 were DROP/LOW
(killed by other gates regardless), and the same agent's CAUTION verdict grades
correctly at 0.375. The skill's hard rule forbids loosening a gate on thin
effectiveness data. **Priority.** P2. **Risk.** Acting on n=11 would remove the gate
that caught the merger-arb blind spot (NUVL) and the ORCL/Pentagon short save.

### 8. Re-scope C15 — the fleet's universe cannot produce the test

**What.** Rewrite C15's acceptance bar or retire it.
**Phase / Data.** Phase 4: of 18 short rows carrying `fz_context`, **zero** clear
`short_float ≥20% ∧ days_to_cover ≥5`. Squeeze-pressure distribution is LOW 91 /
unknown 36 / MODERATE 6. C15 is untestable **by construction** on a mega-cap flow
universe, not merely under-powered. **Priority.** P2.

### 9. Pre-registrations carried forward

**C50** `dealer_dex_flip +3` is tape-conditional (−34.9pp up-tape, +4.1pp down-tape,
n=31) — needs n≥30 per tape arm. **C51** `accumulation_conjunction +3` measured +0.4pp
at n=14 — needs n≥30 per arm across regimes. **C52** short-side selection has no alpha
in any tape (DOWN/short −13.7pp, p=0.1214 ns; direction-call accuracy 39.7% in a falling
tape) — needs a second independent down-tape. None are actionable now; all are recorded
with their acceptance bars in `phase_5_schema.md` §5.5.

---

## What did NOT change and why

- **No rubric weight or tier-cut edits.** Zero of 17 component lines survive BH; the
  freeze exists precisely to stop re-weighting correlated lines on n=8–31 BH-null data.
- **No tool tier movements.** Eighth consecutive BH-null tool table; signs flipped again
  window-to-window, and Phase 3d now supplies the mechanism.
- **No gate removals or loosenings.** Every gate with an evaluable arm grades effective
  (Phase 6.3); the one anti-effective reading is n=11.
- **No Kelly activation.** Gate returns `ADVISORY_ONLY` at n=26 < 30, and all three tier
  expectancies are negative.
