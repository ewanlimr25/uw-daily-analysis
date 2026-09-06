# Phase 7 — Recommendations · 2026-06-20

Voice: chief of staff, multi-strat fund. **Propose-only** — no file outside this audit folder is touched. **Provenance cap:** every finding is verbatim-envelope, but the dataset is **100% single-regime (TRANSITIONAL/UPTREND)** — so per the C23 rule **nothing here is rated P0**; the strongest items cap at **P1**. Rubric is frozen (2026-06-12), so all weight/cut changes are **pre-registrations**, never edits.

---

### 1. Treat single-name shorts as index-relative, not outright — the short book has negative selection alpha
**What.** Stop sizing outright single-name `swing_short` / `bearish_flow` names; express bearish theses as index/sector-relative (pair or spread vs SPY/sector ETF) unless a confirmation bar is cleared. **File.** `.claude/agents/risk-monitor.md` (size gate) + `.claude/agents/signal-confluence-quant.md` (bearish sizing note). **Phase/Data.** Phase 2: BOOK-short 37.3% vs SPY-short 60.0% over the *same windows* → **−22.7pp**; Phase 3: `bearish_flow` realised 0.47 / excess **−23.5pp**, BH-null on calibration but negative on edge. The shorts were entered into genuinely falling windows (SPY-short won 60%) and the single names *still* fell less than the index. **Priority.** P1. **Risk.** Single-regime: some of this is "shorting into an up-tape," but the same-window SPY control removes the tape and the residual is selection. In a real downtrend single-name shorts may regain edge — so this is *expression* (index-relative), not a short ban; register the confirmation-bar threshold as a pre-registration decided cross-regime.

### 2. Stop the substrate-sourced ≥0.80 win-rate quotes from reaching the sizer
**What.** The win-rate substrate quarantined on 2026-06-12 is still emitting ≥0.80 quotes; bind `ABSOLUTE_WR_CEILING=0.80` at *emission* and mark any `win_rate_source ∈ {backtest, fallback_proxy}` quote as **advisory/non-sizing** until the clean cross-regime backtest lands. **File.** `.claude/agents/signal-confluence-quant.md` (win_rate emission rule) + `scripts/excess_winrate.py` (cap binding point). **Phase/Data.** Phase 3 reliability decile **[0.80,0.90): n=24, pred 0.83, realised 0.42**; `earnings_vol` 0.86→0.38 and `high_iv_rank` 0.84→0.38 both **BH-surviving**; Phase 1: **117/132** claimed WRs are substrate-sourced, only 17 `backtest_clean`. **Priority.** P1 — highest-priority P1; act this week. This is a win-rate-emission/substrate-hygiene fix (explicitly in-scope per Phase-7 sizing-procedure rule), **not** a frozen-rubric weight. **Risk.** Low — it only demotes quotes the desk already knows are fabricated; worst case a few vol names size one notch smaller.

### 3. Keep the rubric freeze and the P0.6 out-of-regime half-cap
**What.** Do **not** lift the freeze or the half-cap. **File.** none (a do-not-change ruling). **Phase/Data.** Phase 5: <30 resolved post-freeze calls (18 decided, **0 raw-≥9**), dataset never leaves UPTREND; Phase 2/3: HIGH tier 0.143 and raw 10–12 → 0/33/0% — second consecutive audit with the top of the ladder inverted. **Priority.** P1. **Risk.** None; the evidence argues *against* a lift, and the half-cap's insurance value is precisely for the regime this dataset lacks.

### 4. Pre-register the multileg-weight and HIGH-cut hypotheses (C40, C41)
**What.** Register **C40** (`+2 multileg_directional` → reduce/gate; mechanism: term-structure-inferred direction not predicting) and **C41** (re-confirm the `≥9` HIGH cut; HIGH-band WR must ≥ MED-band). **File.** `analyses/audit/2026-05-25/improvement_criteria.md` register (append), not an agent file. **Phase/Data.** Phase 3: `multileg_directional` 0.17 (n12, **BH-surviving**, claimed 0.56); HIGH 0.143 vs MED 0.526, raw-band HIGH(≥9) 0.385 < MED(7–8) 0.462. **Priority.** P1 to register; **application deferred** to the first audit with ≥30 resolved calls per arm, ≥1 out-of-UPTREND, BH-surviving. **Risk.** Registering costs nothing; the bar prevents a single-window re-weight (the exact failure the freeze exists to stop).

### 5. Instrument the envelope so the debate gate, vol IV-vs-RV, and fz C16/C18 become auditable (C42, C43)
**What.** Carry in `calls[]` (schema-additive, backward-compatible): `debate_residuals.{bull,bear}` on every debated name, `implied_move` on every vol row, and `dp_block_to_float_ratio` + `insider_cluster_flag`. **File.** `schemas/decision_envelope.schema.json` + `.claude/agents/signal-confluence-quant.md`. **Phase/Data.** Phase 6: debate residuals present on only **5/201** rows → debate gate ungradeable; Phase 4: C16/C18 **NA** (data absent); Phase 5 C42 (vol weights ungradeable without true IV-vs-RV). **Priority.** P2 (enabler). **Risk.** None — additive fields; lets the *next* audit grade three things this one could not.

### 6. Measurement hygiene: stop reflexively citing `cumulative-premium-flow` as a scored leg
**What.** It is cited on **66%** of tooled rows, so its marginal contribution is mechanically unmeasurable (ubiquity confound). Either cite it only when it is the *dominant* evidence, or tag it `base_rate_citation` so the audit can exclude it from the with/without contrast. **File.** `.claude/agents/signal-confluence-quant.md` (citation discipline). **Phase/Data.** Phase 4: n=105, ubiquity 0.66, with 0.46 ≈ without 0.42. **Priority.** P2. **Risk.** Low; it likely *is* load-bearing — this is about making it measurable, not demoting it.

### 7. No tool-tier edits; confirm `dark_pool_block_stratified` keeps required-citation status
**What.** Make **no** tool-tier changes this cycle. Keep `dark_pool_block_stratified` as a required citation for `dark_pool_accumulation`. **File.** none. **Phase/Data.** Phase 4: **zero tools survive BH**; `dark_pool_block_stratified` +18pp (third audit positive) but BH-null; the vol-structure negatives (`term_skew` −34.6, `front_end_iv_ratio` −50.0) are RV-proxy-contaminated. **Priority.** P2. **Risk.** None — the skill forbids tool-tier change without BH-surviving cross-regime evidence, which does not exist here.

### 8. Fundamentals gate: keep, watch — do NOT loosen
**What.** Take **no** action to loosen or remove the fundamentals gate despite flat discrimination. **File.** none. **Phase/Data.** Phase 6: fired vs not-fired Δ **+0.8pp**; CONFIRM 0.516 ≈ CAUTION 0.484 ≈ VETO 0.500 (n31/31/4); `veto_fp_rate=0.50` on n=4. **Priority.** P2-watch. **Risk.** Removing a gate on single-regime, sub-floor (VETO n=4) effectiveness data is the C24 cardinal error — its value (it caught NEE dividend-capture distribution) appears in the regime not in this dataset.

---

## Priority roll-up
- **P1 (act this cycle):** #1 short-book expression, #2 substrate-quote ceiling, #3 keep freeze/half-cap, #4 register C40/C41.
- **P2 (enable / confirm / watch):** #5 envelope instrumentation, #6 cum-flow citation hygiene, #7 no tool edits, #8 fundamentals keep-watch.
- **P0:** none — single-regime provenance caps the ceiling at P1 (C23).

Every item cites its phase and datum. No vibe-driven recommendations; no edits to any file outside `analyses/audit/2026-06-20/`.
