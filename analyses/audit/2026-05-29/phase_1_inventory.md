# Phase 1 — Inventory & Parse

**Audit run-id:** 2026-05-29 · **Dataset thresholds:** 22 daily ≥ 10 ✅ / 5 weekly ≥ 3 ✅ — **no DATASET-SIZE-RELAXED banner.**

## Coverage

| Metric | Value |
|---|---|
| Reports parsed | **27** (22 daily, 5 weekly) |
| Calls extracted (after dedup) | **516** |
| — daily / weekly | 438 / 78 |
| — structured envelope / legacy prose | 54 / 462 |
| Distinct trade tickers | 149 |
| Rows carrying `raw_score` | 357 / 516 (69%) |
| Rows carrying a `claimed_win_rate` | 214 / 516 (41%) |
| Rows carrying `score_components` | 253 / 516 (49%) |

**Decision-envelope coverage (the user's note, confirmed):** the machine-resolvable `decision.json` sidecar exists for **this week only** — daily 2026-05-25 → 05-29 (48 calls) and weekly 2026-W22 (6 calls). All validate clean against `schemas/decision_envelope.schema.json` (`validate_decision.py` OK on all 6). The other 21 reports (daily 04-30 → 05-22, weeklies W18–W21) are **legacy prose**, parsed by 7 parallel extraction workers.

## Breakdown

- **By horizon:** swing 323 · weekly 97 · LEAP 52 · 0DTE 31 · vol 13 (+ 124 vol-direction rows carried under swing/weekly sections).
- **By section:** swing_long 196 · swing_short 73 · vol_long 72 · vol_short 62 · watch_only 33 · leap_disqualified 26 · 0DTE 19 · leap 10 · opex_pin 8.
- **By tier:** MEDIUM 169 · LOW 134 · HIGH 60 · DROP 22 · null 131 (legacy rows with no explicit tier).
- **Dominant signal classes (top):** dark_pool_accumulation 68 · bullish_flow 56 · earnings_vol 49 · bearish_flow 45 · multi_day_sweep 26 · multileg_directional 24 · gamma_breakout 22 · leap_directional 18. (Long tail of ~60 bespoke class strings — see data-quality flag below.)
- **Envelope fundamentals_verdict:** CAUTION 14 · CONFIRM 8 · NA 13 · (none) 19.

## Dedup logic

The skill's "one row per (report_date, ticker)" was refined to key on **(report_date, report_kind, call_key, horizon)** because a single ticker legitimately carries distinct-horizon trades that resolve on different windows (e.g. 2026-05-15 AAPL appears as swing_long, opex_pin, **and** leap_disqualified). Same-horizon §3-vs-§7 duplicates collapse to the **richer (audited) row** per the skill's "prefer §7" rule. Only **2** true same-horizon collisions were collapsed (BAC swing 05-05, SPY swing 05-14).

## Data-quality flags

1. **Weekly/daily `report_date` collision.** Weekly W22 dates to Friday **2026-05-29** — identical to the daily 05-29 report_date — and overlaps it on AAPL/MSFT/ORCL/SMH. Resolved by keying weekly rows on the **iso-week** string (`2026-W22`) and carrying `report_kind`. No cross-contamination.
2. **Signal-class string sprawl.** Legacy prose produced ~70 distinct `dominant_signal_class` strings (e.g. `gamma_breakout`, `vol_kink_long`, `dealer_positioning_flip`, `bearish_flow CONFLICTED`). The envelope uses a tighter controlled vocabulary (`bullish_flow`, `bearish_flow`, `dark_pool_accumulation`, …). Phase 3/4 collapse the long tail onto canonical classes for any N≥5 statistic; bespoke singletons are excluded from per-class math.
3. **Disambiguation suffixes.** Prose workers appended `-LEAP / -HEDGE / -0DTE / _HEDGE` to keep multi-role same-ticker calls distinct. A `ticker_base` field strips these for price resolution; the original is retained as `call_key`.
4. **Score/WR coverage is format-dependent.** The richest legacy reports (05-04, 05-07, 05-08, 05-21) print a full §7 audit trail with per-component points; sparser days (04-30, 05-05) print only cross-ref tallies. 31% of rows have no `raw_score` (0DTE pins, vol calendars, hedge sleeves are never run through the conviction rubric) and 59% have no `claimed_win_rate`. These gaps are carried as `null`, never imputed.
5. **`win_rate` capping artifacts.** 05-22 prints `0.90` across five longs (explicitly "capped from bullish_flow 0.929"); 05-21 shows a bull/bear inversion (longs 0.375 vs shorts 0.727 under an UPTREND). Both are real report content, flagged here for Phase 3 calibration.
6. **GOOG vs GOOGL** kept strictly distinct across all workers; no share-class merge.
7. **05-01 risk layer partial** — that report's `risk-monitor` hit a usage cap after 11 calls; gates captured but the risk picture is reconstructed. Relevant to Phase 6 compliance denominators.

## Outputs

- `phase_1_inventory.jsonl` — 516 normalized rows.
- Intermediate: `_envelope_rows.jsonl` (54), `_legacy_{A..G}.jsonl` (462), `extract_envelopes.py`, `consolidate_phase1.py`.
