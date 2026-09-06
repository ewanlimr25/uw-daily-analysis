# Phase 6 — Decision-Process Audit (2026-07-18)

## Quant compliance (`signal-confluence-quant`)
- **Σ points = raw_score: 375/375** (100%). **Provenance complete: True** (every component names a source_agent + tool).
- **Sizing upgrade-violations: 1** — `LLY` 2026-06-05 (claimed_wr 0.392 → implied `starter`, sized `half`). Single **pre-freeze** legacy edge; not a frozen-era defect. Compliance is effectively perfect and shows no drift.

## Model-transition re-audit (2026-07-03 pins) — CLEARED
The 07-11 P2 deferred this until post-pin calls resolved. They now have (81 decided of 128 post-pin rows):
- **Post-pin quant Σ-compliance: 97/97** (100%) — the pins introduced no scoring drift.
- **Debate residuals stable:** bear 0.705→0.729, bull 0.589→0.571 across the pin boundary (no degradation; consistent with 07-11's 0.694→0.75).
- **Post-pin tier dist: DROP 119 / LOW 9 — 0 HIGH/MED.** The pinned fleet sized 9 rows (8 starter, 1 full) of 128 and dropped the rest.
- **Edge-impact:** post-pin decided WR 31% — but that window (07-06→) was a long-crushing pullback (SNDK −13%, MU −11%, NBIS −13%, MRVL −12%, SMCI −8.5%, AMD −7%), and **the fleet DROPPED every one of those longs.** Nothing it sized blew up. The low paper-WR is the fleet correctly refusing a bad tape. **No escalation triggered; the pins are cleared.**

## Gate firing rates (compliance)
regime 0.94 · vrp 0.92 · panic 0.94 · cluster 0.94 · sector 0.92 · fundamentals 0.82 · event_risk 0.97 · debate 0.91 · rubric_regime 1.0. All healthy.

## Gate EFFECTIVENESS (C24) — the gate stack grades EFFECTIVE this cycle
Downgrade-effective = fired (downgraded) WR **below** not-fired WR (the gate found the losers). Every gate shows the effective direction:

| Gate | fired WR (n) | not-fired WR (n) | Δ | status |
|---|---|---|---|---|
| cluster | 0.398 (201) | 0.688 (16) | **−29.0pp** | OK |
| event_risk | 0.417 (218) | 0.750 (8) | −33.3pp | advisory (n8) |
| vrp | 0.406 (192) | 0.571 (21) | −16.5pp | OK |
| debate | 0.390 (100) | 0.538 (13) | −14.8pp | OK |
| panic | 0.416 (197) | 0.562 (16) | −14.6pp | OK |
| sector | 0.414 (191) | 0.524 (21) | −11.0pp | OK |
| regime | 0.424 (203) | 0.467 (15) | −4.3pp | OK |
| fundamentals | 0.425 (179) | 0.439 (41) | −1.4pp | OK |

Six of eight gates cross the n≥10/arm floor showing genuine downgrade-effectiveness — the risk stack is separating losers, not taxing winners. **Caveat:** gates fire on 90%+ of rows, so the "not-fired" arm is a thin, possibly-cleaner minority; the *direction* is right but the magnitudes are inflated by that asymmetry.

## VETO / fundamentals-gate — ordering inverted, but thin-N (advisory)
VETO 0.625 (n8) > CONFIRM 0.41 (n61) ≈ CAUTION 0.397 (n63). **The fundamentals verdict ordering is inverted** — VETO'd-but-tracked names won *more* than CONFIRM'd names. n_veto=8 (<10) ⇒ **advisory; cannot recommend loosening the gate** (C24 hard rule). The CAUTION vs CONFIRM tiers are also indistinguishable on outcome. Watch item toward n≥10.

## Debate gate
bear_won 0.34 (n47) vs bull_won 0.333 (n3). The debate resolves bear-favored 47 of 50 times, and bear-won names still lose ~66% — consistent with a defensive, empty-board tape. bull_won n=3 too thin to grade.

## Missed-gate ledger
regime 34% · vrp 35% · event_risk 33% · fundamentals 33% of scored directional rows lack the gate key. **Structural, not new drift** — the bulk are DROP/watch rows scored at Phase 1 that never entered the full Phase-2 gate stack (they were dropped before gating). Consistent with prior audits; not evidence of agent-prompt divergence.

Output: `phase_6_decision_audit.jsonl`.
