# Phase 1 — Inventory & Parse

**Audit run-id:** 2026-05-23
**Dataset:** 17 daily reports (2026-04-30 → 2026-05-22) + 4 weekly reports (W18 / W19 / W20 / W21) = **21 reports total**.
**Rows extracted:** **302** structured per-call rows in `phase_1_inventory.jsonl`.

Coverage is well above the 10-daily/3-weekly calibration floor — no DATASET-SIZE-RELAXED banner needed.

---

## Composition

### By report kind / horizon

| Horizon | Rows | Notes |
|---|---|---|
| swing (1–6w, daily) | 248 | Workhorse of the desk; majority of conviction calls live here |
| weekly | 37 | 4 weekly reports × ~9 rows median (intra-week scorecard + next-week book + earnings lookahead) |
| LEAP | 13 | Sparse on purpose — the 6-of-9 LEAP gate genuinely rejects most candidates |

### By section

| Section | Rows |
|---|---|
| swing_long | 177 |
| swing_short | 43 |
| vol_short | 35 |
| vol_long | 32 |
| leap | 11 |
| watch_only / leap_disqualified | 4 |

### By tier (as written in the reports)

| Tier | Rows | Realised gate behavior |
|---|---|---|
| MED | 147 | The middle of the rubric. Most useful for tier-monotonicity calibration. |
| HIGH | 79 | Includes both the pure ≥10 HIGH names and the "HIGH override" SELL-VOL specials. |
| LOW | 76 | Starter/watch grade; many gate-survivors from earnings_vol bucket. |

### By dominant signal class (top 10)

| Signal class | N | Comment |
|---|---|---|
| dark_pool_accumulation | 54 | The dominant equity-long thesis class. Win-rate calibration here is most consequential. |
| bullish_flow | 49 | The fallback / proxy class used when no purer signal dominates. |
| multi_day_sweep | 25 | Cleanest sweep-tracker class; usually carries an explicit 0.375 / 0.90 win-rate. |
| earnings_vol | 21 | Generic; subsumes the buy/sell vol cluster (which legacy tagged as `earnings_buyvol` / `earnings_sellvol`, 19+20 rows) — class taxonomy drift is real. |
| multileg_directional | 20 | Term-structure-anchored structures from multileg-strategist. |
| bearish_flow | 19 | Asymmetric vs `bullish_flow`; smaller N because short setups are gated harder. |
| leap_directional | 17 | The LEAP universe; bucket is sparse for a reason. |
| gamma_breakout | 16 | Newish class; no formal MCP backtest signal-type — claimed_win_rate is null for all 16. |
| dealer_positioning_flip | 14 | DEX-flip thesis — closely related to gamma_breakout; classification overlap to fix. |
| vol_kink_long, contrarian_fade, vanna_squeeze, sector_rotation, opex_pin | 8/8/5/4/3 | Small-N classes — flagged as INSUFFICIENT_N for class-level stats in Phase 3. |

### By final risk-monitor disposition

| final_size | N | Realised behavior |
|---|---|---|
| half | 125 | Modal sizing — TRANSITIONAL regime keeps almost everything at ½R. |
| starter | 108 | Floor sizing for raw < 10 or null-backtest tickers. |
| skip | 43 | Gate-stack rejections (panic / cluster / flow_conflict). |
| full | 25 | Almost entirely the "HIGH override" SELL-VOL class plus a few defined-risk vol structures. |

### Legacy-format rows

20 rows tagged `legacy_format=true` (pre-rubric reports from 2026-04-30 onward). These rows have direction, structure, invalidation, agents — enough for outcome resolution and tool attribution — but `raw_score`, `score_components`, and `claimed_win_rate` are null and excluded from rubric-math denominators in Phase 5.

---

## Format coverage gaps & data-quality flags

1. **Signal-class taxonomy drift.** `earnings_vol`, `earnings_buyvol`, and `earnings_sellvol` are used interchangeably across reports (21 + 19 + 20 rows). They should collapse to a single canonical class (with a directional sub-tag) for Phase 3 calibration to compute correctly. Treated as one bucket downstream with note.
2. **`gamma_breakout` is uncalibrated.** All 16 rows carry `claimed_win_rate=null` because there is no `historical_signal_backtest` signal-type for it — the rubric awards points off a class the backtest engine can't grade. Phase 3 will resolve via direction + window; Phase 5 will recommend either consolidation into `dealer_positioning_flip` or addition of a backtest class.
3. **Overlap between `dealer_positioning_flip` and `gamma_breakout`.** 14 + 16 rows describe nearly the same setup with different labels. Provenance-checked in §7 audit rows: same agent (dealer-positioning-strategist) authors both. Merge candidate.
4. **0DTE plays not enumerated as rows.** All 17 daily reports describe 0DTE pin trades in §2 (iron flies / strangles around dealer walls) but the audit consciously excludes them from the JSONL — they're intraday and resolve same session, not amenable to the same 3D/10D outcome window as swing. No data loss, just scope.
5. **Watch-only / single-signal candidates** (§8) are NOT in the dataset except where re-promoted in subsequent reports. The decision to omit them keeps the calibration set focused on actual desk-actionable calls but means the "false-negative" rate (calls we should have taken but didn't) isn't measurable from this dataset. Flagged for Phase 7 as a known blind spot.
6. **GOOG / GOOGL class-share treatment** is inconsistent. The 2026-05-20 report tagged GOOG explicitly (raw 9 MED); other reports use GOOGL when referring to the same underlying flow. Both flow through Phase 2 as GOOG (Class C is the more liquid options chain).
7. **TTWO's 2026-05-18 row** is genuinely double-counted: §3a sized it as `vol_short` (post-earnings short strangle/calendar) and §3a also sized TTWO short-vol per the dedicated row. The duplicate is intentional in the report (§3b sells the post-event premium, §3a captures the IV-crush calendar). One row written, marked vol_short, captures the trade.
8. **Win-rate sourcing is mixed across reports.** Early reports omit `claimed_win_rate` entirely (legacy); mid-period reports cite the proxy class (`bullish_flow`, `bearish_flow`); recent reports cap at 0.90 for non-directional vol plays via the vol_realisation_rate substitute. Phase 3 will note the systematic 0.90 cap as a near-constant claim that should be calibrated separately.

---

## Read order followed

Daily reports 2026-04-30 → 2026-05-22 (oldest first), then weekly W18 → W21 (oldest first). Prior audit (2026-05-15) was a verified source for rows through 2026-05-15; the new 73 rows extracted today cover 2026-05-18 through 2026-05-22 daily + W21 weekly. No re-derivation of older rows (markdown is immutable; prior parser was correct on spot-check of MA / MU / TTWO / NVDA rows).

---

**Inventory closed. Phase 2 begins on the 302-row JSONL.**
