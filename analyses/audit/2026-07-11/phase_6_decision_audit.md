# Phase 6 — Decision-Process Audit (2026-07-11)

## Quant compliance — CLEAN
- **`Σ score_components.points == raw_score`: 0 violations / 396 rows** (validator-guaranteed, verified live).
- Every scored component carries a named `source_agent` + `source_tool` (verbatim envelopes).
- Sizing-map honored: post-freeze the quant emits `win_rate: NA(substrate)` → tier-default-capped-at-half → all resolve to starter/watch-only/skip, consistent with the live map. No upgrade-above-implied-size violations found.

## Model-transition audit (post-2026-07-03 fleet pins) — MANDATORY section
The 2026-07-03 per-agent model/effort pins (quant+risk-monitor fable, multileg opus, rest sonnet) have now emitted **61 envelope rows across 5 report-dates (07-06→07-10 daily + W28 weekly)**.
- **Quant integrity intact:** 0 `Σpoints≠raw_score` violations post-pin.
- **Debate residuals stable:** mean bear-residual pre-pin (06-12→07-02) **0.694 (n=16)** → post-pin (07-03+) **0.75 (n=8)** — the debate pair stays symmetric and discriminating; the slight rise tracks the (correct) empty-board caution, not a collapse or a model artifact.
- **Output shape unchanged:** all 9 post-pin non-DROP calls are LOW/watch-only — same discipline as pre-pin.
- **Edge-impact NOT yet measurable:** 0 post-pin non-DROP calls have resolved (all called 07-06→07-10; forward windows incomplete). **Re-audit the transition after ≥5 resolved post-pin decided calls** (per the pre-registered model-transition triggers).
- **Verdict: CLEAN transition.** No compliance, residual, or shape degradation detectable; the fable/opus/sonnet split is behaving. No escalation triggered.

## Gate effectiveness (C24) — all ADVISORY (< 10 decided per gate)
| Gate | Signal | N (decided) | Read |
|---|---|---|---|
| debate (bear≥bull cut) | cut WR 0.600 vs not-cut NA | 15 vs **1** | control arm n=1 → **INSUFFICIENT_N**; cannot grade |
| fundamentals VETO | VETO'd-tracked WR 0.750 | 4 | veto_fp high but n=4 → advisory (echoes MRNA/NUVL: VETO killed paper-winners; kept as insurance) |
| fundamentals CAUTION | CAUTION WR 0.455 | 33 | ≈ book average → **non-discriminating** this window |

**No gate-loosening/removal is recommended** — every effectiveness number is below the 10-decided floor, and a gate's value is insurance against the regime not yet in the dataset (C24 hard rule).

## Missed-gate ledger
None material. The frozen-era boards are DROP-heavy and correctly gated; no gate that should have fired was absent (spot-checked the 26 post-freeze non-DROP calls — all carry the full 9-key `gate_verdicts`).

Output: `phase_6_decision_audit.jsonl` equivalents embedded.
