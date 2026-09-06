# Phase 1 — Inventory & Parse (2026-07-11)

**Provenance: VERBATIM.** 396 per-call rows loaded directly from 40 `decision.json` envelopes (33 daily + 7 weekly) via `score_components[].source_tool` — no prose reconstruction. `scripts/validate_decision.py` had already gated every envelope; **0 JSON errors, 0 `Σ points ≠ raw_score` violations** across all 396 rows (the validator invariant holds live).

## Coverage
- **Daily:** 50 report folders; 33 envelope-backed (2026-05-25 → 07-10), 17 legacy (2026-04-30 → 05-22, pre-envelope).
- **Weekly:** 11 folders; 7 envelope-backed (W22 → W28), 4 legacy (W18–W21).
- Legacy reports (21) are a **distinct pre-envelope, pre-freeze rubric era** and are excluded from the frozen-rubric grade by the no-pool-eras rule (they'd need prose parsing and cannot carry `rubric_version`); their calls are not in the 396.

## Rubric-era strata (never pooled)
| Era | Rows | Note |
|---|---|---|
| 2026-05-15 | 54 | pre-freeze |
| 2026-05-30 | 97 | pre-freeze (≥9 HIGH cut set here) |
| **2026-06-12 (FROZEN)** | **245** | current rubric; the analytically-decisive stratum |

## Tier / class distribution (all era)
- Tiers: DROP 281, LOW 88, MEDIUM 20, HIGH 7.
- **Post-freeze (2026-06-12): 245 rows → 26 non-DROP, ALL LOW tier, only 7 sized (non-watch/skip). ZERO HIGH, ZERO MEDIUM.**
- Top classes: bearish_flow 76, earnings_vol 57, multileg_directional 54, bullish_flow 49, dark_pool_accumulation 47, high_iv_rank 25, sector_rotation 17.

## Data-quality flags
- The freeze-lift precondition (≥30 resolved post-freeze HIGH/MED) is **structurally unmeetable this cycle** — the frozen rubric has produced 0 HIGH/MED calls in a month (the empty-board streak: 7–8 consecutive DROP-heavy daily boards + the W28 all-watch-only weekly).
- Index pseudo-tickers (SPX/SPXW/RUT/NDX/VIX) cannot be OHLC-resolved → tagged INCONCLUSIVE(index_or_skip) in Phase 2.

Output: `phase_1_inventory.jsonl` (396 rows).
