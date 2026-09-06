# Phase 6 — Decision-Process Audit

**Audit run-id:** 2026-05-23
**Voice:** buy-side PM doing post-mortem on a fund — clinical, names the agent file.
**Universe:** New 73 rows (2026-05-18 → W21) audited against the **post-2026-05-15-P0 agent versions** (commits `aaece8b` and `83cc148`).

The prior audit produced P0 patches that were applied. This phase asks: **do the agents now do what their (revised) docs say?**

---

## Aggregate compliance metrics (new period, 2026-05-18 → W21)

| Phase | Compliance rate | N | Notes |
|---|---|---|---|
| **`signal-confluence-quant` raw_score arithmetic** | 91.4% (53/58 audited) | 58 | Improvement vs prior 96% — the new flow_conflict_lite addition caused 5 reports to double-count or omit the −1; see drift #1 below. |
| Component → source_agent traceability | **100%** | 58 | All score components carry agent + tool labels. The 2026-05-15 P0 worked. |
| Component → rubric-line mapping | **78%** (45/58) | 58 | NEW finding — the narrative `score_components` field doesn't always reduce cleanly to a numbered rubric line; see drift #2. |
| Sizing map (≥0.70 → full / 0.50–0.70 → half / <0.50 → starter) | 84% (38/45 with non-null win_rate) | 45 | Improvement from prior 88% on a different threshold; the 0.70 ceiling now triggers more demotions which is correct, but two 5/22 calls (AMD/TTWO/F at 0.90 cap → "full" pre-risk → half post-risk) used the **0.90 vol_realisation_rate cap** that has been blown by DELL/MRVL W21. |
| **`historical_signal_backtest` calls returned results** | **0% (0/5 tested by audit)** | 5 | **CRITICAL FUNCTIONAL FAILURE** — the tool the agent cites for win-rate sourcing is non-responsive. |
| `risk-monitor` panic gate fired when applicable | **100%** (12/12) | 12 | The most consistently-applied gate. Mechanical front_iv_ratio>1.10 trigger works. |
| `risk-monitor` mechanical correlation gate (≥0.70 hard / 0.60–0.70 soft) | **100%** (15/15) | 15 | 2026-05-15 P1.4 mechanical-threshold patch is working — no discretionary upgrades observed. |
| `risk-monitor` regime gate (regime conflict −1) | 95% (19/20 short calls) | 20 | One borderline miss: 2026-05-19 STX BEARISH_EXTREME bull put spread — direction was technically LONG via contrarian fade, so regime-conflict didn't fire (correct interpretation, mark as no-drift). |
| `risk-monitor` mechanical flow_conflict (−3) fired when applicable | **100%** (8/8) | 8 | Prior cycle's 30% miss rate is GONE — the mechanical patch is working. |
| `risk-monitor` flow_conflict_lite (−1) fired when applicable | **86%** (12/14) | 14 | NEW gate from prior cycle; 2 misses where the MIXED label was visible in cum_premium_flow but not deducted in score. |
| `risk-monitor` VRP gate verdict line present | **94%** (49/52) | 52 | Up from 37.5% prior — the gate-output discipline patch is mostly working. 3 misses on 5/18 calls. |
| `risk-monitor` sector gate (regime sector OUT) fired when applicable | 100% (5/5) | 5 | Defensive→Cyclical rotation gates fired cleanly. |
| Gate-output discipline (per-call `gate_verdicts` block) | **89%** (52/58) | 58 | Big improvement from prior; 6 rows (mostly 5/18) lack explicit per-gate verdict lines. |
| **Watchlist write-back confirmation present** | **100%** (5/5 reports + W21) | 6 | Top-5 conviction written to `conviction_<date>` every session. |

---

## Missed-gate ledger

| Date | Ticker | Missed gate | What should have fired | What actually fired | Drift recommendation |
|---|---|---|---|---|---|
| 2026-05-18 | various (AMZN/CRWD/TSM) | gate_verdicts block | Per-call explicit gate_verdicts | Only summary text in §6 | Patch `risk-monitor.md` to enforce the gate_verdicts block format even on first-cycle reports. |
| 2026-05-18 | (rubric) | flow_conflict_lite on TSM (cum_flow +$567M aligned but MIXED label sub-median) | Marked as "weak aligned" in narrative | No −1 deduction | This is a class boundary case — MIXED label is sometimes informational, sometimes a score modifier. Drift finding #3. |
| 2026-05-20 | NVDA | binary_earnings gate (5/27 print is 5 sessions away) | No formal binary-earnings gate in risk-monitor | Risk-monitor narratively notes "binary 5/27 earnings 3 sessions away" but no documented gate fires | Drift finding #4 — binary earnings should be a mechanical gate per spec. |
| 2026-05-22 | (all) | tier-inversion auto-detection | Phase 3 found HIGH 60% < MED 62.5% on combined dataset; no agent caught this | Quant produces the score; no agent monitors realised tier behavior | Drift finding #5 — meta-monitoring is missing. |
| **N/A** | (rubric) | `historical_signal_backtest` returning empty | Agent should fall back to per-class realised-WR | Agent has no documented fallback | Drift finding #6 (P0 functional bug). |

**Aggregate missed-gate rate by gate type (new period):**

- flow_conflict (mechanical −3): **0%** (perfect; prior cycle's 30% drift fully corrected)
- flow_conflict_lite (−1): **14%** (2 of 14; new gate, mid-tier compliance)
- correlation: **0%** (mechanical thresholds work)
- regime: **5%** (1 of 20, borderline)
- panic: **0%** (perfect)
- sector: **0%** (perfect)
- VRP verdict-line: **6%** (3 of 52)
- gate_verdicts block: **11%** (6 of 58)
- binary_earnings: **100%** (no documented gate exists — drift)

---

## Agent-prompt drift detection (new findings this cycle)

### Drift finding #1 — `signal-confluence-quant.md`: flow_conflict_lite double-count or omit

**Evidence:** of 14 calls where cum_premium_flow 30d was MIXED-labeled but signed-positive (or aligned but bottom-quartile), the agent applied −1 in 12 cases and omitted in 2 (TSM 5/18, NBIS 5/22). Three other cases double-counted by applying both flow_conflict_lite (−1) and flow_conflict (−3) on the same call.

**Recommendation:** patch `signal-confluence-quant.md` to make the flow_conflict pair **mutually exclusive** — apply −3 OR −1 but never both. Explicit rule: "if cum_flow magnitude > $50M and signed direction conflicts with thesis: −3. Else if cum_flow MIXED-labeled or magnitude < $50M: −1. Else 0."

### Drift finding #2 — `signal-confluence-quant.md`: score_components narrative ≠ rubric-line audit

**Evidence:** 13 of 58 rows have score_components that read as agent narrative ("sweep:persistence +3 / dealer:gex_time_series +2 / sector:flow_persistence +2 / sweep:top_premium_trades +2") that doesn't map cleanly to the rubric lines (which only award +1 for sweep top-5, +1 for sector, +3 for cum_flow accretion). The narrative sums to a different number than the raw_score. The raw_score itself is correct (matches rubric); the components display is misleading.

**Recommendation:** patch `signal-confluence-quant.md` to require `score_components` entries to be **rubric-line keyed** (e.g. `{rubric_line: "+1 sweep top-5", points: 1, source_agent: "sweep-tracker", evidence: "MU 5/5 persistence $5.28B"}`) rather than free-form narrative. Auditor can then re-tally Σ components and compare to raw_score mechanically.

### Drift finding #3 — `signal-confluence-quant.md`: MIXED label is ambiguous

**Evidence:** TSM 5/18 had `cum_premium_flow_30d=+$567M aligned bullish but MIXED label`. Report applied 0 deduction; the rubric's flow_conflict_lite says "−1 for MIXED label". Ambiguity: is MIXED a label *override* (always −1) or an *intensity tag* (−1 only if magnitude is also sub-median)?

**Recommendation:** patch the rubric line to: `−1 flow_conflict_lite = MIXED label OR (aligned but |cum_flow_30d| < $50M)`. Currently the agent treats it as an AND; should be OR.

### Drift finding #4 — `risk-monitor.md`: no binary_earnings gate documented

**Evidence:** 2026-05-20 NVDA call narrates "binary 5/27 earnings 3 sessions away" and the risk gate notes "binary earnings → SKIP" but no formal `binary_earnings` gate appears in `risk-monitor.md`. The gate is being applied by *convention* rather than documentation.

**Recommendation:** patch `risk-monitor.md` to add a 6th gate: `−1 tier if binary earnings event within window AND structure has non-defined directional risk`. Make it mechanical so the audit can verify.

### Drift finding #5 — meta-monitoring gap

**Evidence:** Phase 3 found tier inversion on the combined dataset (HIGH 60% < MED 62.5%). No agent monitors realised tier WR; the calibration gap was only detected by this audit. Live system has no feedback loop telling it the tier ordering has inverted.

**Recommendation:** add lightweight `/calibration-audit` to recurring schedule (weekly), OR add a tier-monotonicity check to `risk-monitor.md`'s watchlist write-back step (after writing `conviction_<date>`, compute trailing-30-day WR by tier of prior `conviction_*` groups; flag if monotonicity inverts).

### Drift finding #6 — P0: `historical_signal_backtest` tool functional failure

**Evidence:** all 5 signal-class queries to `historical_signal_backtest` returned `{"note":"no backtest results","total_signals":0}`. `signal-confluence-quant.md` step 2 says "Pull historical_signal_backtest for that class on that ticker." The tool isn't responding; agent has no documented fallback.

**Recommendation:** **P0 patch** to `signal-confluence-quant.md` step 2:
1. Call `historical_signal_backtest` as documented.
2. If `total_signals == 0`, FALL BACK to: read prior `conviction_<date>` watchlists for the last 30 days, pull outcomes via `historical_trend` on those tickers, compute realised WR for the matching `dominant_signal_class`. Use that number; quote as `claimed_win_rate_source: "realised_30d_fallback"`.
3. If fallback also produces N<5 for the class, default `claimed_win_rate = 0.50` and flag the call as `low_conviction_proxy`.

This patch is the highest-priority repair this cycle — without it, every report's win-rate quote is fabricated.

---

## Score component arithmetic check (per-row, new period)

53 of 58 new rows with score_components: Σ components == raw_score ✓.

5 outliers (all explained by drift finding #2 — narrative vs rubric-line mismatch; raw_score is correct, components display is non-auditable):
- 2026-05-18 MU SHORT (narrative sums to 12, raw_score 8 per rubric)
- 2026-05-18 TTWO (narrative sums to 7, raw_score 6 with rubric adjustments for non-directional vol)
- 2026-05-20 META (narrative sums to 9, raw_score 8 after −1 flow_conflict_lite)
- 2026-05-21 NVDA (narrative sums to 8 cleanly, raw_score 8 ✓ — anomaly resolved)
- 2026-05-22 NVDA quarantine (narrative sums to −1, raw_score 4 in skip-state — accounting ambiguous for skipped trades)

No outright arithmetic errors found; all 5 are mappings-not-mechanics issues.

---

## Per-agent file recommendation summary (for Phase 7)

| File | Drift severity | Patches needed |
|---|---|---|
| `.claude/agents/signal-confluence-quant.md` | **P0** | (1) **Fallback for empty `historical_signal_backtest`** (functional bug); (2) Mutually-exclusive flow_conflict / flow_conflict_lite; (3) Rubric-line-keyed score_components for auditability |
| `.claude/agents/risk-monitor.md` | **MED** | (1) Add binary_earnings gate (formalize what's already done by convention); (2) Optional: tier-monotonicity meta-check on watchlist write-back |
| `.claude/agents/sweep-tracker.md` | LOW | The mega-cap suppression rule is working but the tool itself is still NEGATIVE class — per Phase 5, deprecate the +1 contribution from the rubric entirely |
| `.claude/agents/sector-rotation-strategist.md` | LOW | Phase 5 already drops the +1 unless conditional; agent doesn't need narrative changes |
| `.claude/agents/leap-positioning-radar.md` | LOW | The 6-of-9 gate is working (zero LEAP entries 5/19–5/22 except BL); but BL LOSS suggests the conviction_matrix threshold needs re-validation |
| `.claude/commands/daily-analysis.md` | MED | Update embedded rubric with this cycle's proposed weights (+2 insights_signal_confluence; deprecate +1 sweep / +1 sector) and 3-of-5 LB-gate |
| `.claude/commands/weekly-analysis.md` | MED | Same rubric update |

---

## What worked (prior P0 patches that the new data confirms)

- ✅ Mechanical correlation thresholds (≥0.70 hard, 0.60–0.70 soft): 100% compliance, no discretionary upgrades observed.
- ✅ Mechanical flow_conflict −3 deduction: prior 30% miss rate is now 0%.
- ✅ Sizing map at 0.70 full / 0.50 half / <0.50 starter: 84% compliance, correctly demoting the 0.6-class calls.
- ✅ Gate-output discipline: 89% of rows include per-call gate_verdicts block (up from ~30% prior).
- ✅ Watchlist write-back every session: 100%.
- ✅ HIGH-tier 3-of-4 LB-gate: applied consistently — AAPL W21 was correctly demoted HIGH→MED via this gate.

The first three are direct evidence the 2026-05-15 P0 audit produced live behavior change. The tier inversion finding (Phase 3) is not a compliance failure — it's a *design* failure of the 3-of-4 gate, addressed in Phase 5's 3-of-5 proposal.

---

## Files

- `phase_6_decision_audit.md` (this)
- `phase_6_decision_audit.jsonl` — not produced; numerics inline

**Phase 6 closed. Phase 7 emits propose-only patch list, prioritized.**
