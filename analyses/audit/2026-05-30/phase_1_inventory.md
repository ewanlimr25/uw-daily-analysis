# Phase 1 — Inventory & Parse (2026-05-30 · reused from 2026-05-29)

**Audit run-id:** 2026-05-30 · **Thresholds:** 22 daily ≥ 10 ✅ / 5 weekly ≥ 3 ✅ — no DATASET-SIZE-RELAXED.

## Reuse rationale (verified)

Phase 1 is **pure report-parsing — method-independent.** The C20–C25 skill upgrade changed Phase 2+
(outcome resolution, calibration, attribution), **not** how reports are parsed into rows. The
on-disk reports are **byte-for-byte unchanged** since the 2026-05-29 run (22 daily 04-30→05-29,
5 weekly W18–W22; verified: **zero reports missing** from the 05-29 inventory, none added). Therefore
the 516-row `phase_1_inventory.jsonl` from 2026-05-29 is the correct, complete extraction and is
**reused verbatim** (copied into this run's folder). Re-parsing would reproduce it exactly.

## Coverage (carried)

| Metric | Value |
|---|---|
| Reports parsed | 27 (22 daily, 5 weekly) |
| Calls extracted (after dedup) | **516** (438 daily / 78 weekly) |
| Structured envelope / legacy prose | 54 / 462 |
| Resolvable trade rows (Phase 2 input) | 435 |
| Distinct ticker_base | 173 |
| Rows with `raw_score` / `claimed_win_rate` / `score_components` | 357 / 214 / 253 |

- **By horizon:** swing 290 · weekly 94 · 0DTE 31 · LEAP 16 · vol 4 (+ vol rows carried under sections).
- **By section:** swing_long 195 · swing_short 71 · vol_long 69 · vol_short 58 · 0DTE 19 · leap 13 · opex_pin 10 (+ 85 watch/disqualified/DROP NOT_A_TRADE).

## Data-quality flags (carried from 05-29, still apply)

1. Weekly W22 dates to Friday 2026-05-29 (= daily 05-29 report_date); kept distinct via iso-week key + `report_kind`. Phase 2 maps W→Friday for price entry.
2. ~70 free-text `dominant_signal_class` strings collapsed onto canonical families for any N≥8 stat (Phase 3 CANON map); bespoke singletons excluded from per-class math. **(C29 controlled-vocab enforcement remains a future parser fix.)**
3. Disambiguation suffixes (-LEAP/-HEDGE/-0DTE) stripped to `ticker_base` for price resolution.
4. 31% of rows have no `raw_score`, 59% no `claimed_win_rate` — carried `null`, never imputed.
5. GOOG vs GOOGL kept distinct.

## Provenance note (governs Phase 4/7)
Of the **365 rows that Phase 2 decides, 0 are envelope rows** (the 54 envelope rows shipped 05-25→05-29
and are all window_open). So every decided row's `tools_cited` is **reconstructed from prose**, not a
verbatim `source_tool` audit trail — this caps Phase-7 tool recommendations at P1 (C23).

## Outputs
- `phase_1_inventory.jsonl` — 516 normalized rows (reused). Original build scripts:
  `analyses/audit/2026-05-29/{extract_envelopes.py, consolidate_phase1.py}`.
