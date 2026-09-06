# Phase 7 — Recommendations (2026-08-08)

**Propose-only.** Nothing outside `analyses/audit/2026-08-08/` was edited by this audit.

**Provenance basis: 100% verbatim** (626 rows, 64/64 envelopes validated, zero
prose-reconstruction). The C23 priority cap does not bind this cycle.

**Cross-regime basis:** 219 uptrend / 196 transitional / 130 pullback / 81 choppy decided
rows; 290 up-tape / 252 down-tape by realised window. Third consecutive genuinely
cross-regime dataset.

---

## P0 — act before the next session

**None.**

This is deliberate and is the correct read. The one P0 candidate — the short-book deficit —
was already actioned at 2026-08-01 and this audit's job was to grade that action, not
repeat it. It grades clean (item 1). Nothing else in the data clears the "act before next
session" bar: the calibration defects below are real and BH-surviving, but they are quote
defects on a book that is currently sizing almost nothing, so a session's delay costs
nothing.

---

## P1 — clear improvement

### 1. Confirm the short-routing P0 and record its replication — no change to the rule

**What.** No edit. Record in `risk-monitor.md`'s existing rule block that the 2026-08-08
audit **replicated and strengthened** the evidence, and that the compliance check is clean.

**File.** `.claude/agents/risk-monitor.md` (annotation only, inside the existing
`SHORT direction → watch_only` block).

**Phase / Data.** Phase 3.4: `ALL / short` paired McNemar **p=0.0038** (was 0.0115 at
08-01), BH-surviving, b=25 / c=51, n=181; `UP / short` now clears BH independently
(p=0.0195). Tape-conditioned excess **−14.3pp UP / −14.5pp DOWN** — near-identical for a
second cycle, which is the mis-selection (not mistiming) signature the rule rests on.
Phase 6d: **6/6 post-P0 short calls routed to `watch_only`, 0 sized violations,
counterfactual preserved 6/6** (all carry `raw_score`, `gate_verdicts`,
`dominant_signal_class`). Phase 3.5: direction-call accuracy 36.7% in a falling tape,
replicating 08-01's 36.0%.

**Priority.** P1 (documentation of an already-applied P0).

**Risk.** The post-P0 cohort is 6 short calls over 5 sessions in a near-pure uptrend. This
confirms the rule is being *followed*; it does **not** yet grade the rule's *effect*. Do
not let the clean compliance read be mistaken for outcome validation — the counterfactual
needs ~30 decided watch-only shorts, which on current throughput is roughly a quarter away.
The revisit trigger in the rule (two consecutive cross-regime windows with a non-significant
short-side McNemar) is unmet and moving away, not toward.

### 2. Re-derive the `earnings_vol` and `high_iv_rank` win-rate quotes — they cannot be sourced from `signal-backtest`

**What.** Stop quoting a `backtest`-sourced win rate for these two classes and emit
`NA(substrate)` unless a genuine, in-support source exists.

**File.** `.claude/agents/signal-confluence-quant.md` (win-rate resolution section);
`.claude/agents/earnings-scout.md` and `.claude/agents/vol-surface-scout.md` (the quoting
agents).

**Phase / Data.** Phase 3.1: `earnings_vol` claims **0.871**, realises **0.404** on n=106
— a 47.5pp divergence, BH-surviving at p<0.001, the largest miscalibration in the corpus
and its **fourth** consecutive appearance. `high_iv_rank` claims 0.82, realises 0.500,
n=24, BH at p=0.001. **12 of 13** quoted `earnings_vol` rows carry
`win_rate_source: backtest`. `uw historical signal-backtest` supports only five signal
classes and **`earnings_vol` is not among them** — so a backtested rate for this class
cannot exist and whatever produced 0.87 is an unlabelled proxy. Phase 3.3 shows the
consequence: the [0.80,0.90) reliability bucket holds n=31 at predicted 0.83 / realised
0.45.

**Priority.** P1. Would be P0 if the book were sizing these; it is not (1 `full`-size call
in 626 rows).

**Risk.** Emitting `NA(substrate)` pushes these rows to the conservative end of the sizing
ladder, which will further shrink an already near-empty board. That is the correct trade —
a fabricated 0.87 is worse than an honest "unknown." Note that 08-01 raised this same item
and Phase 6d **could not verify whether it was applied**: zero post-P0 rows in either class
carried a quote. Whoever applies this should confirm against the next emitted vol row
rather than against the agent file.

### 3. Apply C56 — re-derive the `[0.55,0.65)` quote, not just its size

**What.** The 07-25 fix floored in-band quotes to `starter`. That caps the damage but
leaves the number wrong. Re-derive the quote itself so the band stops emitting 0.58 for
outcomes that realise 0.23.

**File.** `.claude/agents/signal-confluence-quant.md` (win-rate ladder).

**Phase / Data.** Phase 3.3 reliability deciles: [0.55,0.60) n=30 predicted 0.57 realised
**0.20**; [0.60,0.65) n=13 predicted 0.62 realised **0.31**. Combined n=43, realised
**0.233** against a 0.58 mean quote — the band is not merely miscalibrated, it is
**informative with the sign inverted**, and it survived its first fix cycle unchanged.
Phase 6d confirms the *size* floor is holding (post-P0 in-band rows are 2, both
`watch_only`, never sized).

**Priority.** P1. **Risk.** Re-deriving a quote inside a frozen rubric is a
sizing-*procedure* change, not a weight change, so it is in scope — but it must not become
a back-door re-weight. Change the number the ladder reads; do not touch component points.

### 4. Debug `insider_cluster_flag` — it has never once been `True` (C18)

**What.** One debugging session to determine whether `fz insider-clusters` genuinely never
fires on this universe, or whether the co-flag is being dropped between
`accumulation-hunter` and the quant.

**File.** `.claude/agents/accumulation-hunter.md`; `scripts/fz_enrich.py`.

**Phase / Data.** Phase 6 §6.7: `insider_cluster_flag` is populated on **15 rows corpus-wide
and every one is `False`**. A boolean with zero observed variance cannot gate a conjunction
at any n — C18 is not under-powered, it is uninformative. Note this **corrects** the 08-01
audit, which reported C18 "unblocked, 44/44" by counting key presence across all signal
classes rather than population within `dark_pool_accumulation` rows.

**Priority.** P1. **Risk.** The likely answer is the C15 answer — mega-cap names do not
produce insider clusters — in which case C18 should be **retired**, not fixed. Either
outcome ends a criterion that has consumed five audits.

### 5. Keep the freeze, the half-cap, and every gate — but record *why* the freeze-lift is unrunnable

**What.** No behavioural change. One correction to the framing in `risk-monitor.md`: the
freeze-lift is not blocked by insufficient evidence, it is **unrunnable by construction**.

**File.** `.claude/agents/risk-monitor.md` (the `rubric_regime` block).

**Phase / Data.** *Freeze:* Phase 5.3 — **395** resolved post-freeze calls (13× the n≥30
threshold) but **0 decided HIGH and 0 decided MEDIUM**; 475 post-freeze rows produced 49
LOW and 426 DROP, and the entire 626-row corpus contains **one** `full`-sized call. Zero of
17 component lines survive BH for a **10th** cycle. *Half-cap:* Phase 5.4 — out-of-regime
**0.326 vs in-regime 0.415, Δ −8.9pp on n=43**, negative in all five audits that have
measured it. *Gates:* Phase 6.3 — all nine effective or advisory, none anti-effective;
`cluster` at −25.3pp. Phase 6.5 — **5 missed gates in 1,064 non-DROP obligations (0.47%)**,
zero gates near the 20% drift threshold.

**Priority.** P1. **Risk.** None — this is a documentation correction plus five explicit
holds. The half-cap's protective margin has compressed monotonically across its five
measurements (−16.7 → −14.3 → −11.9 → −12.0 → −8.9pp); that is a reason to keep watching
it, not to loosen it.

---

## P2 — polish / monitor

### 6. Monitor `veto_fp_rate` — still do not loosen

VETO'd names realise **0.500 (n=18)** against a 0.408 book — anti-effective on its face,
and up from n=16 at 08-01 without changing character. Not actionable: n=18 is barely past
the C24 floor; the same agent's **CAUTION** verdict grades correctly (0.355 vs CONFIRM
0.407); and most VETO'd names were killed by other gates, so "would have won if sized" is
not their counterfactual. The C24 hard rule forbids loosening a gate on thin effectiveness
data. Phase 6.4. **Re-grade at n≥30 VETO'd-and-decided.**

### 7. Retire or re-scope C15

Third consecutive cycle in which **zero of 18** short rows carrying `fz_context` clear
`short_float ≥20% ∧ days_to_cover ≥5`. Squeeze pressure distributes LOW 95 / unknown 46 /
MODERATE 10. This is untestable **by construction** on a mega-cap flow universe, not merely
under-powered. Re-running it a fourth time produces the same zero. Phase 4. **P2.**

### 8. Emit per-call `implied_move` on vol rows

`vol_short` is the weakest book in the corpus — 0.356 blended (n=101), collapsing to
**0.167** in pullbacks (n=18). But every vol row resolves on the RV-direction proxy because
no envelope carries `implied_move`, so none of this is a calibrated IV-vs-RV outcome and
none of it can support a rubric change. The validator already warns on the missing key.
Phase 2, Phase 5.6. **P2** — and the precondition for C57 below.

### 9. Pre-registrations

- **C50** — `dealer_dex_flip +3` tape-conditional: **−29.1pp up-tape / +3.3pp down-tape**
  (n=31), a third consecutive window with the same shape (−34.9/+4.1 at 07-25, −36.0/+4.2
  at 08-01). The arms **disagree in sign**, which is the bar's explicit disqualifier.
  Bar unchanged: n≥30 per tape arm ∧ both arms same sign ∧ BH-surviving. Carry forward.
- **C51** — `accumulation_conjunction +3`: **+2.1pp at the +3 emission (n=14)**, +5.1pp at
  +1 (n=44). The rubric's heaviest weight still shows no marginal contribution where it
  pays out. Bar: n≥30 per arm ∧ ≥2 regimes ∧ BH-surviving. Carry forward.
- **C55** — `sector_rotation` re-sourcing: **APPLIED at 08-01 and verified in the emitted
  data** (4/4 post-fix rows cite the netted `uw risk market-regime` line, zero gross
  `sector-flow*` citations). Effect **ungradeable** — 4 rows, 1 decided. Bar for grading
  the fix: n≥30 decided post-fix rows.
- **C56** — `[0.55,0.65)` quote re-derivation: **not applied**; promoted to item 3 above.
- **C57 (new)** — *`vol_short` regime conditioning.* Hypothesis: the lane's edge is
  regime-conditional and negative in falling tape (0.167 pullback n=18 vs 0.464 uptrend
  n=28). Bar: cross-regime ∧ n≥30 per arm ∧ BH-surviving ∧ **resolved against a true
  IV-vs-RV outcome**, which requires item 8 first. Decision window: first audit after
  `implied_move` is emitted on ≥30 vol rows.

---

## What did NOT change and why

- **No rubric weight or tier-cut edits.** Zero of 17 component lines survive BH for a 10th
  consecutive audit; raw-score → WR is flat across the full 3-to-12 range. The freeze
  exists precisely to stop re-weighting correlated lines on BH-null single-window data.
- **No freeze lift.** 8th consecutive cycle in which the test is structurally unrunnable —
  0 decided HIGH, 0 decided MEDIUM post-freeze.
- **No tool tier movements.** **10th consecutive BH-null tool table**; the smallest p in the
  entire sweep is 0.062 on an n=5 cell. Ten windows, every regime this system has seen,
  and no tool has ever been shown to discriminate outcomes.
- **No gate removals or loosenings.** Every gate with an evaluable arm grades effective;
  the one anti-effective reading (`veto_fp_rate`, n=18) is forbidden by the C24 hard rule.
- **No headline built on benchmark-excess.** Per C49 the primary tests are row-matched. Note
  for the record that this is the *least* denominator-contaminated window measured
  (dispersion ratio 0.886, R² 0.327 on the McNemar cell set, versus ~0.61–0.64 in the prior
  two cycles) — the C49 caveat is weaker than usual, but it is not retired, and the
  Phase-3d cell set still attributes 64.4% of excess variance to the benchmark.
