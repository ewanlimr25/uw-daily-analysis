# Phase 6 — Decision-Process Audit

**Audit run:** 2026-05-15
**Voice:** buy-side PM doing post-mortem on a fund — clinical, names the agent file.

## Per-call compliance check

For each Phase 1 row with both `score_components` and `gates_fired` populated (i.e. non-legacy), verified:

1. **Quant compliance**: sum of components = raw_score, every component has source_agent + tool, sizing-map honored
2. **Risk-monitor compliance**: each documented gate considered when its trigger condition was active in the macro context

## Aggregate compliance metrics

| Phase | Compliance rate | N | Notes |
|---|---|---|---|
| `signal-confluence-quant` raw_score arithmetic | **96.0%** (24/25) | 25 audited HIGH-tier rows | One discrepancy: 2026-05-11 LRCX raw_score 6 vs reported 5 (the report itself flagged the strict-vs-lenient re-tally) |
| Component → source_agent traceability | **100%** | 25 | Every line ties to a named agent + named tool |
| Sizing map (≥0.65 → full / 0.50–0.65 → half / <0.50 → starter) | **88.0%** (22/25) | 25 | 3 misses on 2026-05-08: TSLA, NVDA, SNDK all received `claimed_win_rate=1.00` (full eligible) but were sized "starter" via panic gate — correct mechanism, but the audit trail described it as a regime decision rather than a backtest-cap |
| `risk-monitor` regime gate fired when applicable | **94.7%** (18/19) | 19 short calls | One miss: 2026-05-12 IWM short-via-multileg where regime gate did NOT fire despite SHORT in UPTREND (treated as long-vanna-squeeze hedge, defensible) |
| `risk-monitor` correlation gate fired when applicable | **86.4%** (19/22) | 22 cluster-eligible rows | 3 misses: SNDK/MU paired-trade (one pair counted), AVGO/SMH 0.703 corr not penalized on 2026-05-08, TSM/NVDA cluster on 2026-05-13 not gated |
| `risk-monitor` flow_conflict (-2) fired when applicable | **70.0%** (7/10) | 10 cum_flow contradicting dominant class | **3 missed-gate cases — see ledger** |
| `risk-monitor` panic gate fired when applicable | **100%** (8/8) | 8 panic-eligible | All panic_iv_ratio > 1.10 cases correctly fired |
| `risk-monitor` sector gate (regime sector OUT) fired when applicable | **80.0%** (4/5) | 5 cases | One miss on 2026-05-13 (META LONG in Comm Svcs +1.0 inflow but flow_conflict was the dominant penalty) |

---

## Missed-gate ledger

| Date | Ticker | Missed gate | What should have fired | What actually fired | Drift recommendation |
|---|---|---|---|---|---|
| 2026-05-08 | NVDA | flow_conflict (-2) | NVDA cum_premium today = -$17.89M BEARISH while raw_score 10 LONG | Only "regime" cited; the audit-trail flagged "flow_conflict" but no -2 deduction shown in score breakdown | Score should have been 8, not 10. risk-monitor correctly downsized to STARTER but the *score* itself was overstated. Patch `signal-confluence-quant.md` to apply -2 immediately when cum_premium contradicts dominant signal direction — not optional. |
| 2026-05-08 | ORCL | flow_conflict (-2) | cum_premium 30d -$330M BEARISH while LONG raw 7 | Marked as "flow_conflict" but no -2 deduction in score breakdown | Same patch as NVDA. |
| 2026-05-08 | MU LONG | flow_conflict (-2) | cum_premium 30d -$135M MIXED bearish-tilt while LONG raw 8 | Note in §7 says "flow_conflict triggers" but score breakdown shows raw 8 unchanged | Same patch. |
| 2026-05-13 | FLR | flow_conflict (-2) | cum_premium 30d -$4M against direction | The report shows the gate label but not the score deduction | Patch as above. (FLR DID end as STARTER, so behavior was correct, but the score-rubric audit trail was inconsistent.) |
| 2026-05-08 | AVGO/SMH cluster | correlation (-1) | corr 0.703 just over threshold | No cluster penalty applied to AVGO | Marginal — borderline case. Recommendation: lower threshold to 0.65 OR explicitly document the 0.70 hard cutoff. |
| 2026-05-13 | TSM/NVDA cluster | correlation (-1) | corr 0.66 below 0.70 threshold but flagged as soft cluster | Soft cluster has no gate currently | Acceptable — no patch needed. |
| Multiple dates | sector flow_conflict | sector_rotation gate | when sector classification inverted within Tech (AI-infra long vs memory short) | gate was binary on sector, not sub-sector | Patch `sector-rotation-strategist.md` to expose intra-sector dispersion — currently the agent narrates it but the gate doesn't consume it. |

**Aggregate missed-gate rate by gate type:**

- flow_conflict: **30%** (3 of 10 cases, the highest miss rate; ABOVE the 20% drift threshold from skill spec)
- correlation: **13.6%** (3 of 22)
- regime: **5.3%** (1 of 19)
- sector: **20%** (1 of 5)
- panic: **0%** (8 of 8 perfect)

---

## Agent-prompt drift detection

### Drift finding #1 — `signal-confluence-quant.md`: flow_conflict not always applied

**Evidence:** flow_conflict missed-gate rate is **30%**, above the 20% drift threshold. The −2 penalty is documented in the rubric but the agent inconsistently applies it during scoring. In every miss, the agent NARRATIVELY noted the conflict but the *numeric score* did not include the −2.

**Recommendation:** patch `signal-confluence-quant.md` to require flow_conflict to be a *mechanical* deduction whenever `cum_premium_flow_30d` direction contradicts the inferred trade direction (the dominant signal class implies). The narrative-only acknowledgment is insufficient — the score itself must reflect it. (This is a P0 patch — directly causes Phase 5 score miscalibration.)

### Drift finding #2 — `signal-confluence-quant.md`: claimed_win_rate ceiling missing

**Evidence:** every 2026-05-08 call cited `claimed_win_rate=1.00`, which Phase 3 showed is a backtest-window artifact. The agent has no mechanism to cap claimed WR.

**Recommendation:** patch `signal-confluence-quant.md` to cap `claimed_win_rate` at **0.85** when `historical_signal_backtest` n < 20 and at **0.75** when n < 10. The cap protects the sizing map from over-quotation.

### Drift finding #3 — `risk-monitor.md`: correlation threshold inconsistent

**Evidence:** correlation gate fired on AAPL/MSTR 0.631 (2026-05-05) but did NOT fire on AVGO/SMH 0.703 (2026-05-08). The 0.70 threshold is documented but the agent doesn't apply it consistently — sometimes treats 0.65–0.70 as hard cluster, sometimes only ≥0.75.

**Recommendation:** patch `risk-monitor.md` to make the corr threshold mechanical: ≥0.70 = cluster (auto -1), 0.60–0.70 = soft watch (no penalty, just journaled). Eliminate the discretionary band.

### Drift finding #4 — `sector-rotation-strategist.md`: doesn't expose intra-sector dispersion

**Evidence:** during W19 and W20, the audit found genuine "AI-infra long vs memory short" intra-Tech rotation that the agent NARRATIVELY identified but never produced as a structured signal that could fire a sector gate (e.g. -1 for "long memory" or +1 for "long AI-infra"). The single-sector tag treats Tech as monolithic, missing the actual rotation.

**Recommendation:** patch `sector-rotation-strategist.md` to emit `sub_sector_persistence` score rather than only `sector_persistence`. Then the rubric's +1 sector-rotation award and the −3 regime conflict can both consume sub-sector signals.

### Drift finding #5 — Phase 1 `sweep-tracker.md`: sweep persistence on indices

**Evidence:** Phase 4 showed `hot_chains_sweep_persistence` as the worst-performing tool (−24pp). The root cause is that persistent SPY/QQQ/META put-sweep is hedge flow, not directional. The agent treats them as directional shorts and the rubric awards +1.

**Recommendation:** patch `sweep-tracker.md` to filter index ETFs (SPY/QQQ/IWM/SPXW) and the largest 10 mega-caps from sweep-persistence direction-rating UNLESS `cum_premium_flow_30d` agrees in same direction. This implements the "sweep persistence is hedge flow until proven directional" thesis.

---

## Score component arithmetic check (per-row)

24 of 25 audited HIGH-tier rows had `Σ score_components == raw_score`. The single outlier:

- **2026-05-11 LRCX**: report itself flagged a "strict vs lenient" re-tally giving 5 vs 6. The lenient version was used (raw 6). Acceptable — flagged in the report.

No other arithmetic errors found.

---

## Per-agent file recommendation summary (for Phase 7)

| File | Drift severity | Patches needed |
|---|---|---|
| `.claude/agents/signal-confluence-quant.md` | **HIGH** | (1) Mechanical flow_conflict deduction; (2) WR ceiling cap by backtest-N |
| `.claude/agents/risk-monitor.md` | MED | Make correlation threshold mechanical (no discretionary band) |
| `.claude/agents/sector-rotation-strategist.md` | MED | Expose sub-sector persistence |
| `.claude/agents/sweep-tracker.md` | MED | Filter index/mega-cap sweeps unless cum_flow agrees |
| `.claude/agents/dealer-positioning-strategist.md` | LOW | (no drift; agent worked correctly) |
| `.claude/agents/accumulation-hunter.md` | LOW | (no drift; load-bearing tool stack worked correctly) |
| `.claude/commands/daily-analysis.md` | MED | Update embedded rubric with Phase 5 re-weights and re-binned tier cuts |
| `.claude/commands/weekly-analysis.md` | MED | Same rubric update |

---

## Numerics file

`phase_6_decision_audit.jsonl` — per-call compliance flags, missed-gate ledger, per-agent drift findings.
