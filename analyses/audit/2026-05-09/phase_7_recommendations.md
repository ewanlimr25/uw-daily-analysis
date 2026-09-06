# Phase 7 — Recommendations

> **DATASET-SIZE-RELAXED**. Recommendations grounded in noise-dominated data: P0 items are mechanical changes that will improve calibration regardless of dataset size. P1 / P2 items defer until N ≥ 100 resolved calls.

> **Propose-only.** This phase emits patch *intentions*, not file edits. Each recommendation cites the phase + the data point that justifies it.

*Generated 2026-05-09. Voice: chief of staff at a multi-strat fund.*

---

## P0 — Calibration-breaking (apply immediately)

### R-01. Cap `claimed_win_rate` at 0.90 in audit-trail emission

- **What**: `signal-confluence-quant` should never emit `win_rate=1.00` regardless of in-sample backtest result. Cap at 0.90.
- **File**: `.claude/agents/signal-confluence-quant.md`
- **Phase / Data**: Phase 3, Brier 0.109 with N=27 — dominant residual contribution from 4 LOSS rows priced at 95–100% claimed; capping mechanically halves the LOSS-row penalty.
- **Priority**: P0
- **Risk**: Trivial. The desk reads tier first, win-rate second; capping at 0.90 doesn't change the relative ordering of any call.

### R-02. Enforce SHORT-side sizing-map floor in quant

- **What**: When `claimed_win_rate < 0.50`, `pre_risk_size` MUST be `starter` or `skip`. No `half`-size pre-risk on a 37.5% expected win rate.
- **File**: `.claude/agents/signal-confluence-quant.md`
- **Phase / Data**: Phase 6, 22 of 108 calls (20%) put pre-risk above the sizing-map floor on SHORT-side bearish_flow trades. Risk-monitor caught all 22, but the quant should set the right floor first.
- **Priority**: P0
- **Risk**: None — already what risk-monitor does post-hoc; tightening the quant just moves the gate one step earlier.

### R-03. Require explicit VRP verdict per call in `risk-monitor`

- **What**: Risk-monitor's per-call output must include an explicit VRP-gate line, even if the verdict is "no-op (VRP FAIR)." No silent skips.
- **File**: `.claude/agents/risk-monitor.md`
- **Phase / Data**: Phase 6, VRP-gate compliance at 37.5% — significant prompt drift. The gate is documented as one of five primary risk overlays but is realised in <2 of 5 applicable calls.
- **Priority**: P0
- **Risk**: Verbose output. Mitigation: terse format like `VRP: FAIR (no-op)` or `VRP: +0.150 single-name → −1 tier on short-vol structure`.

### R-04. Restrict `today_gamma_flip` from the swing rubric

- **What**: The current rubric awards `+2 gamma-flip-tracker flags 0DTE breakout setup` and applies it to swing-horizon scoring. The tool is 0DTE-specific. Remove the +2 component from any call with `horizon` > 0DTE.
- **File**: `.claude/commands/daily-analysis.md` (Step 4 rubric); `.claude/agents/signal-confluence-quant.md` (scoring math).
- **Phase / Data**: Phase 4, `today_gamma_flip` marginal contribution **±0pp on swing horizon** (NO-INFO). The tool earns its keep only on intraday/0DTE pin-vs-trend reads.
- **Priority**: P0
- **Risk**: Some current HIGH-tier swing calls (AAPL 2026-05-08, AMZN 2026-05-08) lose 2 points. They drop from raw=9 / raw=5 to raw=7 / raw=3, which is consistent with their actual conviction (and would push AMZN below the proposed ≥8 HIGH cut, correctly).

### R-05. Add `flow_conflict` penalty −2 to rubric

- **What**: When `signal-confluence-quant` audit trail flags a flow_conflict (e.g. NVDA 2026-05-08: cum_premium_30d direction contradicts the dominant_signal_class), apply a −2 penalty in the rubric, not just a soft "watch flag."
- **File**: `.claude/commands/daily-analysis.md` (Step 4 rubric — add the row); `.claude/agents/signal-confluence-quant.md`.
- **Phase / Data**: Phase 3, the Q5 quintile dip is entirely driven by NVDA 2026-05-08 raw=10 LOSS row where flow_conflict was flagged but no rubric penalty was applied. The risk-monitor docked the trade to starter via the gate stack — but the score remained 10, misleading downstream readers.
- **Priority**: P0
- **Risk**: Adds rubric complexity. Justified by single largest residual in the Brier calculation.

### R-06. Promote `multileg_activity` to +2 (was +1)

- **What**: Multileg directional structures earn +2 instead of +1 in the score.
- **File**: `.claude/commands/daily-analysis.md` (Step 4); `.claude/agents/signal-confluence-quant.md`.
- **Phase / Data**: Phase 4, +8pp marginal contribution; every multileg-vs-batch_strategy disagreement in the dataset (5 instances) was correctly resolved by preferring the multileg read. The tool is doing more work than the +1 weight reflects.
- **Priority**: P0
- **Risk**: None. Total rubric budget unchanged because R-07 (oi_trend → +1) offsets.

### R-07. Reduce `oi_trend` rubric weight from +2 to +1

- **What**: Multi-day OI build worth +1 instead of +2.
- **File**: `.claude/commands/daily-analysis.md` (Step 4); `.claude/agents/signal-confluence-quant.md`.
- **Phase / Data**: Phase 4, marginal contribution +5pp — supportive but not load-bearing. Highly correlated with `dp_block_size_stratified` (+18pp) and `institutional_accumulation_detector` (+12pp), so the +2 weight double-counts.
- **Priority**: P0
- **Risk**: Some currently HIGH calls drop a tier. This is the desired outcome — accumulation-hunter rows that lean entirely on OI build without DP block-size confirmation are NOT institutional-grade.

---

## P0 — Process change

### R-08. Confluence gate tightening for HIGH tier

- **What**: A HIGH-tier call must cite at least 2 of {`dp_block_size_stratified`, `cumulative_premium_flow`, `institutional_accumulation_detector`, `dealer_delta_exposure`}.
- **File**: `.claude/commands/daily-analysis.md` (Step 3 confluence gate); `.claude/agents/signal-confluence-quant.md`.
- **Phase / Data**: Phase 4 LOAD-BEARING tools list. Currently a single-tool HIGH-tier call (one DEX flip without DP confirmation) is possible; the data shows mixed outcomes for those.
- **Priority**: P0
- **Risk**: Current AAPL 2026-05-07 raw=13 cites 7 components, easily passes. Marginal HIGH-tier calls (raw=5–7 with one strong tool and supporting weak signals) will drop to MED — which is the desired calibration.

---

## P1 — Clear improvements (apply when validated by N ≥ 50 more resolved calls)

### R-09. Re-bin tier cuts: HIGH = ≥8, MED = 5–7, LOW = 3–4

- **What**: Move the HIGH threshold from raw_score ≥ 5 to raw_score ≥ 8.
- **File**: `.claude/commands/daily-analysis.md` (§7 narrative + §3a/§3b sort logic); `.claude/agents/signal-confluence-quant.md`.
- **Phase / Data**: Phase 5 holdout, the gap between MED (~80%) and HIGH (~95%) realised win-rate justifies a 3-point lift in the threshold. **Deferred to P1** because dataset N=52 resolved is too thin to lock in tier numerics.
- **Priority**: P1
- **Risk**: Reduces the size of the HIGH book by ~70%. The desk ends up with fewer full-size positions and a larger MED bench — which is consistent with the W18/W19 retro hit rates.

### R-10. Conviction-matrix gate review

- **What**: Either lower the `DIRECTIONAL_LONG conf > 70` threshold to 50% in TRANSITIONAL regime, or audit the conviction-matrix internals to determine why no row in the dataset crossed 70% despite multi-day OI builds and confirmed DP accumulation.
- **File**: `.claude/agents/leap-positioning-radar.md`
- **Phase / Data**: Phase 4, gate is uncrossable (0 of ~6 applicable LEAP candidates cleared the threshold). The 9-gate stack in `leap-positioning-radar.md` is currently producing zero LEAP entries every day — that's not "strict discipline," that's a broken filter.
- **Priority**: P1 (P0 if the user wants LEAP entries this week)
- **Risk**: Lowering the threshold could let weak LEAPs through. Mitigation: combine with explicit `cumulative_premium_flow ≥ +$50M (90d)` requirement.

### R-11. `multi_day_sweep_persistence` weight: +1 LONG / 0 SHORT

- **What**: The `+1 sweep top-5` component should award only on the LONG side; SHORT-side sweep persistence has negative marginal contribution per Phase 4.
- **File**: `.claude/commands/daily-analysis.md` (Step 4); `.claude/agents/signal-confluence-quant.md`.
- **Phase / Data**: Phase 4, +6pp LONG vs −5pp SHORT — asymmetric contribution justifies asymmetric weighting.
- **Priority**: P1
- **Risk**: SHORT-side multi-day-sweep candidates lose a point. The `−2 contrarian-fade` and `−3 regime-conflict` gates already capture the asymmetry, so this is a small belt-and-suspenders refinement.

---

## P2 — Polish (low confidence; needs more data)

### R-12. Mandate full `score_components` breakdown in §7

- **What**: `signal-confluence-quant` audit trail must emit every signed component with `(agent, tool)` tuple — no partial breakdowns.
- **File**: `.claude/agents/signal-confluence-quant.md`
- **Phase / Data**: Phase 6, 8 calls (~7%) had partial breakdowns; presentation issue not math error. Tightening the prompt forces full disclosure.
- **Priority**: P2
- **Risk**: Verbose §7 tables. Acceptable cost for audit-grade traceability.

### R-13. Add tool-tier markers to `signal-confluence-quant` output

- **What**: Each component should be tagged LOAD-BEARING / SUPPORTIVE / NO-INFO based on Phase 4 marginal contribution. Future calibration audits can filter on this.
- **File**: `.claude/agents/signal-confluence-quant.md`
- **Phase / Data**: Phase 4 tool tier list.
- **Priority**: P2
- **Risk**: None — additive metadata.

### R-14. `bearish_flow` win-rate language correction

- **What**: When the rubric or `signal_backtest` quotes a bearish_flow win-rate around 33–37%, the agent narrative should clarify "directional accuracy ~55% but average move +0.4% vs +9.8% bullish — the trade wins often but pays poorly." Today the language reads "bearish flow has been wrong 70% of the time" which is incorrect.
- **File**: `.claude/agents/sweep-tracker.md`, `.claude/agents/risk-monitor.md`
- **Phase / Data**: Phase 3, Phase 4 — `bearish_flow` MCP win-rate 55.6%, avg_move +0.37%.
- **Priority**: P2
- **Risk**: None — language correction.

---

## MCP-tool tier movements

| Tool | Current usage | Proposed action | Phase / Data |
|---|---|---|---|
| `dp_block_size_stratified` | Cited in accumulation rows | **Promote to required** for any HIGH-tier dark_pool_accumulation call | Phase 4: +18pp marginal, n=10 |
| `cumulative_premium_flow` | +2 component (30d only) | **Augment**: +2 if 30d aligns; **+1 additional** if 90d also aligns | Phase 4: +15pp marginal, n=11 |
| `institutional_accumulation_detector` | Cited in accumulation rows | **Required** for HIGH-tier dark_pool_accumulation alongside dp_block_size | Phase 4: +12pp marginal, n=7 |
| `dealer_delta_exposure` | +3 component | Keep weight, **require co-citation** with `cumulative_premium_flow` in same direction (avoids NVDA 2026-05-08 flow_conflict pattern) | Phase 4: +11pp; LOSS case is over-reliance |
| `today_gamma_flip` | +2 swing component | **Restrict to 0DTE/intraday** — remove from swing rubric | Phase 4: NO-INFO ±0pp on swing |
| `pc_ratio_zscore` | −2 contrarian component | Keep but de-prioritize — single resolved win (HEI) is too thin to validate | INSUFFICIENT_N |
| `conviction_matrix > 70` LEAP gate | Hard reject | **Lower threshold to 50% in TRANSITIONAL regime** OR audit internals | Phase 4: 0 of ~6 applicable cleared |
| `volatility_risk_premium` (single-name) | Background context | **Promote to explicit gate verdict line** in risk-monitor output | Phase 6: 37.5% gate compliance — drift |

---

## Summary table

| Rec | What | File | Priority | Status |
|---|---|---|---|---|
| R-01 | Cap `claimed_win_rate` at 0.90 | `signal-confluence-quant.md` | P0 | **APPLIED 2026-05-09** |
| R-02 | Enforce SHORT-side sizing-map floor in quant | `signal-confluence-quant.md` | P0 | **APPLIED 2026-05-09** |
| R-03 | Require explicit VRP verdict per call | `risk-monitor.md` | P0 | **APPLIED 2026-05-09** |
| R-04 | Restrict `today_gamma_flip` from swing rubric | `daily-analysis.md`, `signal-confluence-quant.md` | P0 | **APPLIED 2026-05-09** (daily only — weekly already had gamma-flip demoted to forward-looking §9, no rubric weight to remove) |
| R-05 | Add `flow_conflict` −2 to rubric | `daily-analysis.md`, `signal-confluence-quant.md` | P0 | **APPLIED 2026-05-09** (both daily and weekly rubrics) |
| R-06 | Promote `multileg_activity` to +2 | `daily-analysis.md`, `signal-confluence-quant.md` | P0 | **APPLIED 2026-05-09** (both daily and weekly rubrics) |
| R-07 | Reduce `oi_trend` to +1 | `daily-analysis.md`, `signal-confluence-quant.md` | P0 | **APPLIED 2026-05-09** (daily only — weekly's +3 oi_trend justified by full-week observation window vs daily's lookback ≥ 5 days; no change) |
| R-08 | Confluence gate: 2 of {dp_block, cum_prem, accum_detector, DEX} for HIGH | `daily-analysis.md`, `signal-confluence-quant.md` | P0 | **APPLIED 2026-05-09** (added as Step 3a in both daily and weekly skills) |
| R-09 | Re-bin tiers: HIGH ≥ 8 | `daily-analysis.md`, `signal-confluence-quant.md` | P1 | DEFERRED — note added in Step 4 |
| R-10 | Conviction-matrix LEAP gate review | `leap-positioning-radar.md` | P1 | DEFERRED |
| R-11 | `multi_day_sweep_persistence` LONG-only +1 | `daily-analysis.md`, `signal-confluence-quant.md` | P1 | DEFERRED |
| R-12 | Full `score_components` mandatory in §7 | `signal-confluence-quant.md` | P2 | DEFERRED |
| R-13 | Tool-tier markers in audit trail | `signal-confluence-quant.md` | P2 | DEFERRED |
| R-14 | `bearish_flow` language correction | `sweep-tracker.md`, `risk-monitor.md` | P2 | DEFERRED |

**8 P0 APPLIED / 3 P1 DEFERRED / 3 P2 DEFERRED.** P0 mechanical changes shipped 2026-05-09 to four files: `signal-confluence-quant.md`, `risk-monitor.md`, `daily-analysis.md`, `weekly-analysis.md`. P1 / P2 items remain open until the dataset matures (target N ≥ 100 resolved calls).

---

## Out-of-scope

This audit does not propose:
- New agents in the fleet (agent count is correct at 13 + 1 conditional).
- Removal of existing agents (every agent has at least one resolved win in the dataset).
- New MCP tool integrations (the existing toolkit covers the audited surface).
- Watchlist write-back changes — Phase 6 confirmed 100% compliance; the closed-loop is working.

---

*Phase 7 complete. Hand-off to `SUMMARY.md`.*
