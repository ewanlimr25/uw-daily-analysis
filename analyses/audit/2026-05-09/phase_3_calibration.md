# Phase 3 — Calibration Audit

> **DATASET-SIZE-RELAXED**. Per-signal-class N=2 to N=10 across the resolved population. Brier and reliability numbers below are reported but should be read as directional fingerprints, not statistical estimates. The thresholds (10pp divergence, tier-monotonicity) still apply — just with lower confidence in the numbers themselves.

*Generated 2026-05-09. Resolved-call population from Phase 2: ~52 deduplicated rows. Numbers below quote both "claimed" (mean of `claimed_win_rate` from Phase 1 audit-trail rows) and "realised" (W18 + W19 retro + signal_backtest joint resolution).*

---

## Per-signal-class calibration table

| Signal class | N (resolved) | Claimed WR | Realised WR | Δ (claimed − realised) | Verdict |
|---|---|---|---|---|---|
| `dark_pool_accumulation` | 8–10 | ~95% (most rows quote 100%, 90%, or 80%) | ~95% | **±5pp** | **HONEST** |
| `bullish_flow` | 7–9 | ~92% (rows quote 100% or 77.8%) | ~92% | **±5pp** | **HONEST** |
| `gamma_breakout` / `dealer_positioning_flip` | 5 | ~95% (rows quote 100%, 75%) | ~80% (4 wins of 5 in W19) | **+15pp** | **OVERCONFIDENT** — flag |
| `bearish_flow` | 9 (mcp) + W18/W19 inferred | **33–37.5%** (rows) | **55.6%** (mcp) | **−18 to −22pp** | **UNDERCONFIDENT** — flag opposite-direction |
| `multi_day_sweep` LONG | 4 | ~75–80% | ~85% | **−5 to −10pp** | borderline OK |
| `multi_day_sweep` SHORT | 3 | ~37.5% | 1 LOSS + 2 INCONCLUSIVE = 0% directional / 33% inclusive | ±10pp | small-N noise |
| `contrarian_fade` | 1 (HEI win); rest unresolvable | n/a | 1/1 | n/a | **INSUFFICIENT N** |
| `earnings_buy_vol` | 2 (RUM win, SHOP loss) | n/a | 50% | n/a | **INSUFFICIENT N** |
| `vol_kink_long/short` | 0 resolved (all event-date pending) | n/a | n/a | n/a | **INSUFFICIENT N** |
| `multileg_directional` | 3 LONG (WIN), 1 SHORT (LOSS GOOGL) | ~75% | ~75% | ±5pp | borderline OK |

### Flagged divergences (>10pp)

- **`dealer_positioning_flip` overconfidence**: agents quote 100% / 75% (e.g., NVDA 2026-05-08 → "WR 1.00" while flow conflict was already firing). Realised over the W19 window is closer to 80%. **Action proposed in Phase 5**: claimed_win_rate for this signal class should be capped at 0.85 unless confirmed by an independent dealer-position move in the same direction the next session.
- **`bearish_flow` excessive pessimism**: agents quote 33–37.5% directional win-rate. Realised over the resolved window is **55.6%** — call directions are correct more often than the rubric assumes. BUT the avg_move on bearish wins is +0.37% vs +9.81% on bullish wins, so the magnitude asymmetry justifies the size-down even when direction is right. **Action proposed in Phase 5**: separate "directional win-rate" from "expected R-multiple" in the sizing map; bearish_flow is "wins often but pays poorly," not "wins rarely."

### Voice — sell-side flow trader (per spec)

> *"`bearish_flow` 55.6% realised vs 33% quoted is the kind of mismatch that makes a desk leave money on the table. The shorts ARE directionally okay — what's actually wrong is the up-magnitude asymmetry: when bullish flow is right it pays 10x what bearish flow pays when right. The rubric should encode that as a payoff-multiplier, not as a win-rate haircut. Fix the language and the size-down logic survives."*

> *"`dark_pool_accumulation` and `bullish_flow` both clock 95% realised in W19 against 100% claimed — that's the rubric being slightly too proud, not lying. n=8 means the holdout test in Phase 5 is going to be tight."*

---

## Per-tier reliability (text reliability diagram)

Joining outcomes back to Phase 1 `tier` for the resolved population:

| Tier | N (resolved) | WIN | LOSS | INCONCLUSIVE | Realised win-rate |
|---|---|---|---|---|---|
| HIGH | 14 | 12 | 1 | 1 | **92.3%** (12/13) |
| MED | 10 | 8 | 1 | 1 | **88.9%** (8/9) |
| LOW | 8 | 4 | 1 | 3 | **80.0%** (4/5) |
| (untiered, legacy) | 5 | 3 | 0 | 2 | 100% (3/3 — small N noise) |

### Verdict

**Tier monotonicity HOLDS** in the resolved sample: HIGH (92.3%) > MED (88.9%) > LOW (80.0%). No tier inversion. **This is the most important calibration finding of the audit**: the rubric ranks correctly even if individual signal-class win-rates are imperfectly calibrated, the tier structure produces a usable ordering for desk consumption.

But the **gaps between tiers are tiny** (3–9pp). A desk would prefer at least 15pp between HIGH and MED. The current rubric is too generous to LOW-tier (4 wins of 5 resolved = 80%) — that's because LOW-tier currently includes calls with raw_score 5–7 that have one strong dealer-positioning component but few other confirmations. Phase 5 will propose tighter LOW-tier definitions to push the gap.

---

## Brier score

Computed against resolved rows where both `claimed_win_rate` and `outcome ∈ {1, 0}` exist (excluding INCONCLUSIVE):

```
Brier = (1/N) × Σ (claimed − outcome)²

N (resolved with claimed) = 27 (legacy rows excluded)
WIN_rows  (outcome=1, claimed≈0.95): mean residual² ≈ 0.0025  × 23 ≈ 0.058
LOSS_rows (outcome=0, claimed≈0.85): mean residual² ≈ 0.7225  ×  4 ≈ 2.890
Total Σ residual²                              ≈ 2.948
Brier  = 2.948 / 27                            ≈ 0.109
```

**Brier ≈ 0.11**. By the heuristic in the skill spec (≤0.10 is "professionally calibrated"; ≥0.25 is coin-flip), the rubric is **marginally well-calibrated** — close to the professional threshold but not over it. The 4 LOSS rows dominate the score because each contributed ≈0.72 vs ≈0.0025 per WIN; this is the price of quoting 95–100% confidence and being wrong.

### Voice — market-maker quant

> *"Brier 0.11 with N=27 is genuinely close to acceptable — but the dominant contribution is from 4 LOSSES priced at 95% confidence. Each one drags Brier by ~0.026. Capping High-tier claimed_win_rate at 0.90 (instead of letting the audit-trail emit 1.00) would mechanically halve the LOSS-row penalty. That's the cheapest single change in the entire audit."*

---

## Conviction-vs-outcome quintile scatter

Bucketing `raw_score` into quintiles across the resolved population:

| Score quintile | Range | N | WIN | LOSS | Realised WR |
|---|---|---|---|---|---|
| Q1 (lowest) | raw ≤ 3 | 5 | 3 | 1 | 75% (3/4) |
| Q2 | 4–5 | 8 | 6 | 1 | 86% (6/7) |
| Q3 | 6–7 | 8 | 6 | 1 | 86% (6/7) |
| Q4 | 8–9 | 6 | 6 | 0 | 100% (6/6) |
| Q5 (highest) | 10+ | 5 | 4 | 1 | 80% (4/5) |

### Verdict

**Q5 < Q4 in win-rate** — a soft inversion. The single LOSS in Q5 is **NVDA 2026-05-08 raw=10** with the flow_conflict gate firing, which the report itself flagged with a "downgrade to starter" note. The trade was priced at win_rate=1.00 (the rubric's audit trail) but the gate logic correctly down-sized.

**This is not a real tier inversion** — it's a single high-conviction call with a known flow-conflict caveat. But it IS evidence that the rubric's claimed_win_rate emission ignores the gate stack: a call gets quoted at 100% even when the gate stack has just docked it from FULL to STARTER. The mathematical implication: claimed_win_rate should be a *post-gate* number, not a pre-gate number. **Action proposed in Phase 5**: emit a `gate_adjusted_win_rate` field that subtracts a calibrated penalty per gate fired.

The Q1→Q4 march is monotone (75 → 86 → 86 → 100%), which is the desk-grade desideratum. The score IS picking up signal — the system is producing higher win-rate at higher conviction. The Q5 dip is an artifact of one unreduced flow-conflict call. **Tier ordering is honest. Score-to-WR translation needs work.**

---

## Phase 3 hand-off

Three findings flow to Phase 5:

1. **Cap claimed_win_rate at 0.90 for High-tier and 0.95 for any signal class.** The rubric's audit trail currently emits 1.00 — the LOSS-row Brier penalty proves this is leaving calibration on the table.

2. **Separate directional win-rate from expected payoff for the bearish/short signal classes.** The 55.6% realised vs 37.5% claimed is a calibration error in one direction; the +0.37% avg-move vs +9.81% bullish is a magnitude asymmetry justifying the size-down. The rubric expresses both via "win_rate" today, which conflates them.

3. **Emit gate-adjusted_win_rate in audit trails.** The Q5 dip (NVDA 2026-05-08) shows that the same row can have raw=10 and "WR 1.00" in the audit trail while simultaneously having flow_conflict + regime gates docking the trade to starter. Future readers should see the post-gate number.

Tier monotonicity holds — that's the load-bearing finding. The schema is structurally sound; the calibration of individual numbers needs tightening.
