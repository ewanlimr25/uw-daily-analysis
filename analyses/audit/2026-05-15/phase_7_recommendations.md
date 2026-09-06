# Phase 7 — Recommendations

**Audit run:** 2026-05-15
**Voice:** chief of staff at a multi-strat fund — clear ownership, prioritized, every recommendation tied to a phase + datum.

**THIS IS PROPOSE-ONLY.** No agent files have been edited. The patches below are intentions; a future `/calibration-audit apply` mode (or the user) does the editing.

---

## P0 — Calibration-breaking (apply before next `/daily-analysis` run)

### P0.1 — Make `flow_conflict` a mechanical deduction in `signal-confluence-quant`

- **What.** Whenever `cum_premium_flow_30d` direction contradicts the inferred trade direction implied by the dominant signal class, the agent must apply the −2 (or −3 under proposed rubric) deduction *to the numeric score*, not just narrate the conflict.
- **File.** `.claude/agents/signal-confluence-quant.md`
- **Phase / Data.** Phase 6: 30% missed-gate rate on flow_conflict (3 of 10 cases on 2026-05-08), above the 20% drift threshold. Phase 3: NVDA 2026-05-08 raw_score 10 LOSS was dominated by un-penalised flow_conflict (cum_flow −$17.89M against LONG thesis).
- **Priority.** P0.
- **Risk.** Mechanizes a previously-narrative gate. Could over-penalize calls where the cum_premium_flow read is itself stale (e.g., post-earnings re-rating in progress). Mitigation: scope to 30d window with explicit `flow_conflict_lite` (-1) for MIXED labels, full −3 only for clearly opposite directional accretion.

### P0.2 — Cap `claimed_win_rate` by backtest-N

- **What.** When `historical_signal_backtest` returns a backtest with n < 10, cap the quoted `claimed_win_rate` at 0.75. With n < 20, cap at 0.85. Never quote 1.00 or 0.90 on small samples.
- **File.** `.claude/agents/signal-confluence-quant.md`
- **Phase / Data.** Phase 3: 2026-05-08 entire HIGH-tier book quoted 1.00 for `bullish_flow`, `dark_pool_accumulation`, `dealer_positioning_flip`; realised 0.64–0.75. Brier on that single date was 0.45 (catastrophic). Phase 4: even the LOAD-BEARING tools tap out at 0.778 realised.
- **Priority.** P0.
- **Risk.** Caps a tool the agent legitimately reports. Mitigation: this is a *quote* cap, not a *backtest* cap — the underlying historical computation remains, only the displayed/used WR is bounded.

### P0.3 — Re-bin tier cuts to HIGH ≥10, MED 7–9, LOW ≤6

- **What.** Update tier cuts in scoring rubric (currently HIGH ≥9, MED 6–8, LOW 3–5).
- **File.** `.claude/agents/signal-confluence-quant.md` + `.claude/commands/daily-analysis.md` + `.claude/commands/weekly-analysis.md` (rubrics embedded in all three).
- **Phase / Data.** Phase 3: MED-vs-LOW gap is 1.1pp (noise); HIGH ≥10 realised 0.85 vs HIGH ≥9 (current) realised 0.667. Phase 5 holdout test: tier monotonicity preserves under proposed cuts.
- **Priority.** P0.
- **Risk.** Fewer calls reach HIGH; some HIGH-tier behaviors (e.g., unconditional FULL-size eligibility) need to handle the smaller cohort. Mitigation: in TRANSITIONAL regime everything is HALF anyway, so practical sizing change is small.

---

## P1 — Clear improvement (apply this week)

### P1.1 — Demote `hot_chains_sweep_persistence` for index/mega-cap shorts

- **What.** Filter SPY, QQQ, IWM, SPXW, and the top-10 mega-caps from sweep-persistence direction scoring UNLESS `cum_premium_flow_30d` aligns in same direction.
- **File.** `.claude/agents/sweep-tracker.md` + `.claude/agents/signal-confluence-quant.md` (the +1 sweep_top5 award).
- **Phase / Data.** Phase 4: `hot_chains_sweep_persistence` realised −24pp marginal contribution (n=13). Phase 6: drift finding #5 — index sweep persistence is hedge flow, not directional.
- **Priority.** P1.
- **Risk.** Removes a tool from the rubric for a specific subset of names. Mitigation: keep the tool for 0DTE intraday and for non-mega-caps where sweep persistence is genuinely directional.

### P1.2 — Promote DP_block_stratified + cum_premium_flow weights

- **What.** Boost both signal weights from +2 to +3 in the conviction rubric. Demote `insights_conviction_matrix` from +2 to +1 (keep as LEAP gate; downgrade as positive scorer).
- **File.** `.claude/agents/signal-confluence-quant.md` + the embedded rubrics in `daily-analysis.md` and `weekly-analysis.md`.
- **Phase / Data.** Phase 4: dark_pool_block_stratified +27.8pp marginal, historical_cumulative_premium_flow +24.2pp — both LOAD-BEARING. insights_conviction_matrix −7.5pp marginal as a positive scorer.
- **Priority.** P1.
- **Risk.** Changes the relative weight ordering of components. Mitigation: the new ordering preserves the sign of every signed component (no flips).

### P1.3 — Harden the LB-gate from 2-of-4 to 3-of-4

- **What.** HIGH-tier (raw ≥10 under new cuts) requires citing ≥3 of {dark_pool_block_stratified, historical_cumulative_premium_flow, insights_institutional_accumulation, options_structure_dex}, not 2.
- **File.** `.claude/agents/signal-confluence-quant.md`.
- **Phase / Data.** Phase 4: only the LOAD-BEARING quartet scored >+20pp. Phase 5: under harder LB-gate, in-sample WR rose to 0.667.
- **Priority.** P1.
- **Risk.** Even fewer HIGH-tier entries. Mitigation: aligns with regime-conservative posture.

### P1.4 — Make `risk-monitor` correlation threshold mechanical

- **What.** Replace discretionary corr-cluster band with strict thresholds: ≥0.70 = cluster (auto −1), 0.60–0.70 = soft watch (no penalty), <0.60 = no flag.
- **File.** `.claude/agents/risk-monitor.md`.
- **Phase / Data.** Phase 6: drift finding #3 — correlation gate inconsistently fired (0.631 fired in one case, 0.703 didn't fire in another).
- **Priority.** P1.
- **Risk.** Removes risk-monitor's discretion to upgrade soft clusters in unusual cases. Mitigation: the discretion was being mis-applied; mechanical is safer.

---

## P2 — Polish (apply when convenient)

### P2.1 — Expose `sub_sector_persistence` in `sector-rotation-strategist`

- **What.** Emit intra-sector dispersion scores (e.g. "AI-infra +1.0, memory −0.7") rather than only the binary `sector_persistence`.
- **File.** `.claude/agents/sector-rotation-strategist.md`.
- **Phase / Data.** Phase 6: drift finding #4 — the agent narratively identified intra-Tech rotation in W19/W20 but emitted no structured signal that the rubric could consume.
- **Priority.** P2.
- **Risk.** Adds complexity; sub-sector mapping requires a stable taxonomy. Mitigation: bootstrap with the GICS Level 3 taxonomy, refine as needed.

### P2.2 — Deprecate `dark_pool_largest` from default citation

- **What.** Drop `dark_pool_largest` from the default tools_cited list when `dark_pool_block_stratified` is already cited (it's confounded — only fires positive when the block-stratified version also fires).
- **File.** `.claude/agents/accumulation-hunter.md` + `.claude/agents/leap-positioning-radar.md`.
- **Phase / Data.** Phase 4: `dark_pool_largest` marginal contribution −0.4pp (NO-INFO/CONFOUNDED). LOW confidence — needs N≥5 in next audit cycle to confirm.
- **Priority.** P2.
- **Risk.** Removes a tool that may surface useful info in edge cases. Mitigation: keep as a fallback when block_stratified returns empty.

### P2.3 — Re-introduce sector-rotation +1 award only after `persistence_score` field is fixed

- **What.** The +1 sector-rotation single-name leader award is currently DEPRECATED because the persistence_score field returned uniform 1.0 in the audit window. Re-introduce when the field is repaired.
- **File.** `.claude/agents/signal-confluence-quant.md`; coordinate with whatever team owns the UW MCP `options_flow_sector_flow_persistence` endpoint.
- **Phase / Data.** Phase 4: NEGATIVE −11.0pp marginal because the field was broken. Phase 1 data-quality flag: 2026-05-13 confirmed broken field.
- **Priority.** P2.
- **Risk.** Without this, sector-rotation single-name leaders (RKLB, LITE, FLR, JD, BOOT in this audit) lose a +1 boost. Mitigation: those names should depend on accumulation/dealer/multileg co-flagging for HIGH-tier consideration anyway.

### P2.4 — Add backtest-class registry for empty-history signals

- **What.** When `historical_signal_backtest` returns n=0 for a signal class (as happened for `dark_pool_accumulation` on 2026-05-11), the agent should default to the bullish_flow proxy and tag the row `wr_proxy=true` rather than silently using a fallback. Currently the report mentions this as a footnote — make it structured.
- **File.** `.claude/agents/signal-confluence-quant.md`.
- **Phase / Data.** 2026-05-11 report's failure-mode notes; affects all `dark_pool_accumulation` calls in the LRCX/AAPL line.
- **Priority.** P2.
- **Risk.** Low; makes existing behavior auditable.

### P2.5 — `daily-analysis` and `weekly-analysis` commands should explicitly cite "regime-conditioning" warning on backtest WR

- **What.** Add a one-paragraph header to both `daily-analysis.md` and `weekly-analysis.md` reminding the orchestrator that all rolling-window backtests are regime-stationary on the calibration window. In a regime shift, backtest WR will lag by 5–10 sessions.
- **File.** `.claude/commands/daily-analysis.md`, `.claude/commands/weekly-analysis.md`.
- **Phase / Data.** Phase 1 desk note: "the dataset is regime-stationary"; Phase 3 finding that win-rate field migrated from 0.77/0.80 (W18) → 1.00 (early May) → 0.40-0.78 (mid May) due to backtest-window drift.
- **Priority.** P2.
- **Risk.** Documentation only; no behavior change.

---

## Process changes

### PC.1 — Backtest-sizing-map adjustment

- **What.** Current map: ≥0.65 → full / 0.50–0.65 → half / <0.50 → starter. Phase 3 quintile data suggests the right threshold is closer to ≥0.70 → full. Tighten the full-size threshold.
- **File.** `.claude/agents/signal-confluence-quant.md` + `.claude/agents/risk-monitor.md` (sizing applied here).
- **Phase / Data.** Phase 3 quintile table: Q5 (raw ≥9) realised 0.727 — the only band where >0.65 is empirically true. Q4 (raw 6-8) realised 0.571 — sub-0.65, deserves half not full.
- **Priority.** P1.
- **Risk.** Most calls were already gated to half by regime; this is a calibration-tightening, not a behavior-change.

### PC.2 — Confluence-gate adjustment (require 2 independent tools per HIGH)

- **What.** Already enforced by Phase 5's hardened LB-gate (3-of-4). Documented here as a process-level reminder.
- **File.** N/A (covered by P1.3).
- **Priority.** rolled into P1.3.

---

## Recommendation count by priority

| Priority | Count |
|---|---|
| P0 (calibration-breaking) | 3 |
| P1 (clear improvement) | 4 |
| P2 (polish) | 5 + 2 process |
| **Total** | **14** |

---

## Hard rules check

- ✅ All recommendations are **propose-only**. No `Edit` or `Write` against any file outside `analyses/audit/2026-05-15/`.
- ✅ Every recommendation cites the phase + the data point.
- ✅ Data-thin findings (P2.2 dark_pool_largest, P2.3 sector-rotation) explicitly noted as low-confidence pending more data.
