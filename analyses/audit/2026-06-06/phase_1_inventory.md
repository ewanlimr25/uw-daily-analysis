# Phase 1 — Inventory & Parse (2026-06-06 audit)

**Dataset:** 27 daily reports (2026-04-30 → 2026-06-05) + 6 weekly reports (W18 → W23) = 33 reports.
Thresholds pass outright (≥10 daily, ≥3 weekly) — **no DATASET-SIZE-RELAXED banner**.
UW data current through 2026-06-05 (matches latest report; preflight clean).

## Method

- **Reused verbatim** the 2026-05-30 audit's consolidated inventory (516 rows, daily through
  2026-05-29 + weekly through W22). Those reports are immutable history; the prior parse
  passed its own zero-row and dedup checks and carried both envelope and prose provenance tags.
- **Extended** with the 6 new reports — daily 2026-06-01…06-05 + weekly 2026-W23 — **all
  envelope-backed**. Every `decision.json` passed `scripts/validate_decision.py` (14, 16, 11,
  7, 15, 6 calls respectively = 69 new rows). Zero prose parsing needed for the extension.
- Dedup on (report_date, report_kind, call_key, horizon): **0 collisions** in the union.
- Extractor: `phase1_extend.py` (this folder). New rows carry the full envelope dimension set
  incl. `fundamentals_verdict`, `debate_residual_confidence`, `fz_context`,
  `breadth_cross_check`, `macro_event_risk`, and the new C28 `distribution_flag` (26 rows).

## Inventory

| Cut | Counts |
|---|---|
| Total rows | **585** (501 daily / 84 weekly) |
| Provenance | **123 envelope** (verbatim) / **462 prose-reconstructed** (legacy) |
| Horizon | swing 379 · weekly 97 · LEAP 52 · 0DTE 31 · vol 26 |
| Section | swing_long 221 · swing_short 84 · vol_long 76 · vol_short 72 · watch_only 54 · leap_disqualified 36 · 0DTE 19 · leap 13 · opex_pin 10 |
| Tier | HIGH 62 · MEDIUM 180 · LOW 159 · DROP 53 · untiered 131 (legacy) |
| Direction | long 308 · short 114 · vol_short 85 · vol_long 75 · neutral 1 · n/a 2 |
| With claimed_win_rate | 267 |
| With score_components | 316 |
| With fz_context | 45 |

## Top signal classes

dark_pool_accumulation 87 · bullish_flow 67 · earnings_vol 60 · bearish_flow 58 ·
multileg_directional 28 · multi_day_sweep 27 · gamma_breakout 27 · leap_directional 21 ·
dealer_positioning_flip 12 · opex_pin 10.

## Data-quality flags (carried from prior parse + new)

1. **Provenance split is the headline constraint (C23):** 462/585 rows (79%) have
   prose-reconstructed `tools_cited` — all tool-tier findings on the blended set stay
   **structural/qualitative**, and P0 recommendations require the 123-row verbatim subset.
2. Earnings class naming drift persists: `earnings_buyvol` (9) vs `earnings_buy_vol` (7) —
   merged downstream in Phase 3/4 as one class.
3. 2026-05-25 was a market holiday (Memorial Day) yet a 4-row daily report exists; its calls
   resolve off the next session's bar (entry_idx falls back to last bar ≤ date… forward bars
   begin 05-26).
4. Weekly rows date to the Friday close of their ISO week (W23 → 2026-06-05).
5. 2026-06-05 daily + W23 weekly calls have **zero forward bars** (last OHLC bar = 06-05);
   they enter Phase 2 as `INCONCLUSIVE / window_open` by construction.

**Output:** `phase_1_inventory.jsonl` (585 rows, machine-readable).
