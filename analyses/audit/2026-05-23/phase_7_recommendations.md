# Phase 7 — Recommendations

**Audit run-id:** 2026-05-23
**Voice:** chief of staff at a multi-strat fund — prioritized, propose-only, every claim cites a phase + data point.
**This skill emits patch intentions only.** No agent files were edited.

---

## P0 — Calibration-breaking (fix before next session)

### P0.1 — Fall back when `historical_signal_backtest` returns empty
- **What.** Add documented fallback path to `signal-confluence-quant`: if MCP returns `total_signals=0`, compute `claimed_win_rate` from realised-30-day-WR of the matching `dominant_signal_class` over the rolling `conviction_<date>` watchlists, resolved via `historical_trend`. If fallback N<5, default to 0.50 and flag `low_conviction_proxy`.
- **File.** `.claude/agents/signal-confluence-quant.md` (step 2).
- **Phase / Data.** Phase 2: all 5 queried signal types returned `{"note":"no backtest results","total_signals":0}`. Phase 3: every `claimed_win_rate` in the 73-row resolved set is currently agent-fabricated; the rubric's sizing-map is keyed off a number the cited tool does not produce.
- **Priority.** P0 (the sizing-map relies on a non-functional tool).
- **Risk.** Fallback adds compute cost (reading prior watchlists + historical_trend per ticker). Worst case: starts quoting 0.50 too often → over-conservative sizing. Mitigated by the `low_conviction_proxy` flag making the conservatism visible.

### P0.2 — Re-do the LB-gate as 3-of-5 with `insights_signal_confluence` added
- **What.** Add `insights_signal_confluence` to the load-bearing-tool set; require 3-of-5 (not 3-of-4) for HIGH-tier confirmation. Tools: `dark_pool_block_stratified`, `historical_cumulative_premium_flow`, `insights_institutional_accumulation`, `options_structure_dex`, `insights_signal_confluence`.
- **File.** `.claude/agents/signal-confluence-quant.md` (HIGH-tier gate section); `.claude/commands/daily-analysis.md` and `weekly-analysis.md` (embedded rubric).
- **Phase / Data.** Phase 3: tier inversion detected (HIGH 60.0% < MED 62.5% on combined 73-row resolved set; was 66.7% prior). Phase 4: `insights_signal_confluence` marginal contribution +19.5pp (n=12) — now LOAD-BEARING. Phase 5: holdout stress-test shows the 3-of-5 gate restores tier monotonicity (HIGH 0.80 / MED 0.50 / LOW 0.50 on W21 holdout).
- **Priority.** P0 (tier inversion is calibration-breaking by skill definition).
- **Risk.** Fewer calls survive at HIGH (the 3-of-5 is one degree harder). Half-baked "accumulation only" HIGH calls like MA (5/18) and BL (5/19) demote to MED — both of which lost in resolved outcomes, so the demote is correct in retrospect.

### P0.3 — Deprecate `hot_chains_sweep_persistence` from positive scoring
- **What.** Remove the +1 line from the rubric. Keep the tool informational only (still narrated in §2 / §3 / §7 prose but contributes 0 points to raw_score). Mega-cap suppression rules are insufficient — the tool was NEGATIVE for two consecutive audits.
- **File.** `.claude/commands/daily-analysis.md`, `.claude/commands/weekly-analysis.md` (rubric); `.claude/agents/sweep-tracker.md` (output schema retain, ranking signal demote); `.claude/agents/signal-confluence-quant.md` (rubric).
- **Phase / Data.** Phase 4: `hot_chains_sweep_persistence` marginal contribution −22pp (n=15, two-cycle persistent NEGATIVE). Phase 3: `multi_day_sweep` signal class realised 0.43 vs claimed 0.70 — the +27pp overstatement is dominated by this tool's contribution. Phase 5: prior cycle's deprecation recommendation was P0 but only the suppression rule was implemented, not the deprecation.
- **Priority.** P0.
- **Risk.** Loss of an alpha-class on the rare directional sweep (e.g. AMD 5/22 had 5/5 BULL sweep + $89M whale). Mitigation: sweep-tracker still surfaces these in §3 prose; if the call merits a multileg or accumulation co-flag, those tools earn the score.

---

## P1 — Clear improvement (fix this week)

### P1.1 — Demote `insights_conviction_matrix` to 0 in non-LEAP scoring
- **What.** Remove +1 line from default rubric. Keep as conditional +1 only when `dominant_signal_class == leap_directional` and the conviction is DIRECTIONAL_LONG with confidence > 70.
- **File.** `.claude/agents/signal-confluence-quant.md`; `.claude/commands/*.md`.
- **Phase / Data.** Phase 4: marginal contribution **−23pp** (n=8, NEGATIVE). BL LOSS and MA LOSS both cited this tool. The DIRECTIONAL_LONG flag at >70% confidence appears to be a mean-reversion fade (top-pick signature).
- **Priority.** P1.
- **Risk.** LEAP gate uses this tool already (`leap-positioning-radar.md`); P1.1 explicitly preserves that. The risk is leaving a working LEAP gate signal off the swing tier — acceptable per Phase 4 data.

### P1.2 — Promote `insights_signal_confluence` to +2 positive scorer
- **What.** Add new rubric line: `+2 insights_signal_confluence ≥4 (second-agent confirmation)`. Already cited by quant; not yet awarded points.
- **File.** `.claude/agents/signal-confluence-quant.md`; `.claude/commands/*.md`.
- **Phase / Data.** Phase 4: marginal contribution **+19.5pp** (n=12, LOAD-BEARING). Promotion already implicit in P0.2's LB-gate; this line awards the points.
- **Priority.** P1.
- **Risk.** Adds a +2 line. May inflate raw_scores at the top — but the tier cuts re-bin in P0.2 absorbs this naturally.

### P1.3 — Make `flow_conflict` and `flow_conflict_lite` mutually exclusive
- **What.** Patch the rubric definition: apply **−3 OR −1 but never both** on the same call. Explicit rule: "if cum_flow_30d magnitude > $50M and signed direction contradicts thesis: −3. Else if MIXED-labeled OR magnitude < $50M: −1. Else 0."
- **File.** `.claude/agents/signal-confluence-quant.md` (rubric).
- **Phase / Data.** Phase 6: 3 of 14 cases double-counted (applied both −3 and −1); 2 cases omitted the −1 when MIXED was visible. Drift finding #1.
- **Priority.** P1.
- **Risk.** Low — the rule is mechanical and easy to audit; net effect is more consistent score derivation.

### P1.4 — Score_components must be rubric-line-keyed
- **What.** Patch `signal-confluence-quant.md` to require `score_components` entries in the audit table to be **rubric-line keyed** rather than free-form narrative. Schema: `{rubric_line: "+1 sweep top-5", points: 1, source_agent: "sweep-tracker", source_tool: "hot_chains_sweep_persistence", evidence: "MU 5/5 persistence $5.28B"}`. Sum of components must mechanically equal `raw_score`.
- **File.** `.claude/agents/signal-confluence-quant.md` (output schema).
- **Phase / Data.** Phase 6: 5 of 58 rows had components-narrative-sum ≠ raw_score (rubric was correct; components display was misleading). Drift finding #2.
- **Priority.** P1.
- **Risk.** Output verbosity slightly increases. Audit-trail clarity worth it.

### P1.5 — Sector-rotation +1 contribution is conditional only
- **What.** Award +1 for sector-rotation leader ONLY when both: (a) sector persistence_score ≥3 AND (b) cum_premium_flow_30d aligned with thesis direction AND |cum_flow_30d| ≥ $50M. Default is 0.
- **File.** `.claude/agents/signal-confluence-quant.md`; `.claude/commands/*.md`.
- **Phase / Data.** Phase 4: sector_persistence marginal contribution +2.8pp (NO-INFO standalone). When paired with cum_flow alignment, it's the difference between HON-W21 (+4.9% WIN) and WMT-W19 (−10.4% LOSS — flow disagreed mid-thesis).
- **Priority.** P1.
- **Risk.** Removes points from sector-only names; consistent with the data.

---

## P2 — Polish (queue for next audit cycle)

### P2.1 — Formalize binary_earnings gate in risk-monitor
- **What.** Add 6th gate to `risk-monitor.md`: `−1 tier if binary earnings event within 5 trading days AND structure carries non-defined directional risk`. Currently applied by convention (NVDA 5/20, MU 5/18) without documented mechanism.
- **File.** `.claude/agents/risk-monitor.md`.
- **Phase / Data.** Phase 6: drift finding #4 — gate fires by convention; not in spec.
- **Priority.** P2.
- **Risk.** None — formalizes existing behavior.

### P2.2 — Cap `earnings_vol` claimed_win_rate at 0.65 when back-month skew is COMPLACENT
- **What.** When the rubric awards earnings-vol points and the back-month skew is COMPLACENT (skew_ratio < 1.05), cap `claimed_win_rate` at 0.65 instead of the current 0.90 `vol_realisation_rate` proxy.
- **File.** `.claude/agents/signal-confluence-quant.md` (sizing map).
- **Phase / Data.** Phase 3: earnings_vol realised 0.625 vs claimed 0.85 (+22pp overstated). Phase 2: DELL-W21 (+24% blow-through), MRVL-W21 (+16% blow-through) both happened on COMPLACENT back-skew SELL VOL trades.
- **Priority.** P2.
- **Risk.** Smaller earnings-vol sizing on what would have been correctly-flagged event-priced-cheap. Trade-off worthwhile after two clear blow-ups.

### P2.3 — Expose sub-sector persistence in sector-rotation-strategist
- **What.** Patch agent to emit `sub_sector_persistence` (e.g. AI-infra long vs memory short within Tech) alongside `sector_persistence`. Rubric then consumes both.
- **File.** `.claude/agents/sector-rotation-strategist.md`.
- **Phase / Data.** Phase 6 prior cycle drift finding #4 (carried). 2026-05-19 cyclical→defensive vs 2026-05-22 accelerating risk-on resolved differently within Tech.
- **Priority.** P2 (low-confidence, needs N≥20 sub-sector calls before action).
- **Risk.** Agent output verbosity grows; lower-conviction sub-sector signals could noise the score if rubric weight is set too high.

### P2.4 — Schedule `/calibration-audit` weekly to auto-detect tier inversions
- **What.** Add a recurring schedule: run `/calibration-audit` automatically each Sunday after the weekly report writes. Flag any tier inversion or signal-class divergence ≥15pp as a soft alert before Monday open.
- **File.** none (skill scheduling) — add as P2 process change.
- **Phase / Data.** Phase 3: tier inversion detected this cycle; no agent monitored it. Drift finding #5.
- **Priority.** P2.
- **Risk.** Audit compute cost (~5 min weekly).

### P2.5 — Investigate why `dark_pool_block_stratified` softened from +27.8pp to +21.8pp
- **What.** The previously top-precision LOAD-BEARING tool added 6 citations in the new period; 3 of those resolved as LOSSES (MA, BL, WMT). Investigate whether the tool's block-stratified threshold has decayed (e.g. mega-buy ratio thresholds drift) or whether the new sample is just noise.
- **File.** none directly; investigation only.
- **Phase / Data.** Phase 4: marginal contribution dropped −6pp this cycle.
- **Priority.** P2 (insufficient N for action; flag for next audit).
- **Risk.** Premature change risks losing a LB tool.

---

## Recommendations not made (data-thin)

- `oi_smart_positioning`, `oi_position_rolls`, `options_structure_front_end_iv_ratio`, `dark_pool_ticker_summary` — all N<5 cited; **INSUFFICIENT_N**; defer until next audit.
- `dealer_positioning_flip` vs `gamma_breakout` class merger — proposed by prior audit; data still too thin to confirm the merge (combined n=11 across two classes).
- Re-test of `hot_chains_sweep_persistence` in a NEGATIVE-VRP regime — the 2026-04-30 → 2026-05-22 window was all FAIR/MILD VRP. The tool may behave differently when premium-selling is structurally favored; defer.

---

## Apply order (recommended for v2 "apply" mode)

1. **P0.1** first (functional bug — restores win-rate sourcing).
2. **P0.2** next (restores tier monotonicity via 3-of-5 LB gate).
3. **P0.3** + **P1.1** together (deprecations: sweep +1 and conviction_matrix +1 in non-LEAP).
4. **P1.2** (add insights_signal_confluence +2 line).
5. **P1.3**, **P1.4**, **P1.5** in a follow-up commit (auditability + sector conditional).
6. **P2.x** in next audit cycle.

---

## Files

- `phase_7_recommendations.md` (this) — prioritized list, propose-only.

**Phase 7 closed. Step 8 (`SUMMARY.md`) follows.**
