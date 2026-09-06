# Phase 1 — Inventory & Parse (2026-08-08)

**10th edge audit.** Dataset threshold cleared comfortably: 70 daily / 15 weekly report
folders on disk, of which **64 carry a `decision.json`** (53 daily + 11 weekly). No
DATASET-SIZE-RELAXED banner.

## Provenance basis

**100% verbatim envelope provenance.** All 626 rows come from `decision.json` `calls[]`;
**zero** rows were prose-reconstructed, and there are no `legacy_prose` era rows in the
parsed set (the pre-envelope reports were resolved by earlier audits and are not re-parsed).
523 of 626 rows carry at least one `score_components[].source_tool`. Under C23 this lifts
the priority cap — findings in this audit may reach P0 where the evidence supports it.

**Validation: 64/64 envelopes pass `scripts/validate_decision.py` clean.** Zero
`Σ score_components.points ≠ raw_score` violations across the entire corpus — the ninth
consecutive clean mechanical-integrity result.

## Corpus shape

| Dimension | Breakdown |
|---|---|
| Rows | **626** (was 578 at 2026-08-01; **+48**) |
| Envelopes | 64 (53 daily, 11 weekly) |
| Unique tickers | 168 |
| Kind | daily 558 / weekly 68 |
| Horizon | swing 457 / vol 158 / LEAP 11 |
| Tier | DROP 488 / LOW 111 / MEDIUM 20 / HIGH 7 |
| Direction | long 248 / short 191 / vol_short 108 / neutral 42 / vol_long 37 |
| Final size | skip 285 / **watch_only 284** / starter 35 / half 12 / veto 9 / **full 1** |

### Rubric-era stratification (never pooled downstream)

| Era | Rows |
|---|---|
| **`2026-06-12` (FROZEN)** | **475** |
| `era_0530_0605` | 69 |
| `era_0525_0529` | 54 |
| `pre_freeze_post_0606` | 28 |

### Regime buckets

`uptrend` 219 / `transitional_other` 196 / `pullback_in_uptrend` 130 / `choppy` 81.
Out-of-regime (half-capped) rows: 44. Post-freeze rows: 475.

## The post-P0 cohort (this cycle's reason to exist)

The 2026-08-01 audit's P0 — *SHORT direction → `watch_only`, never sized* — was applied to
`.claude/agents/risk-monitor.md` on 2026-08-01 (still uncommitted in the working tree).
Envelopes dated **2026-08-03 onward are the first cohort authored under the new rule**:
5 daily + 1 weekly (W32), **48 rows, 18 decided, 24 still window-open**.

This cohort is small and almost entirely `uptrend` (40 of 48 rows). It is sufficient to
grade **compliance** with the new rule; it is **not** sufficient to grade the rule's
**effect**. Phase 6d treats those as separate questions and says so.

## Data-quality flags

1. **`dominant_signal_class` enum drift is FIXED post-intervention.** The pre-P0 corpus
   carries 31 distinct class strings with 14 off-list variants (`dealer_positioning_flip` ×7,
   `dealer_short` ×4, `dex_flip_long` ×2, `sector_leader` ×2, `none` ×7, plus 8 singletons).
   The post-P0 cohort carries **11 distinct classes, zero off-list** — 08-01 P2 #9 landed.
   The audit-side `canonical_class` collapse is retained for the historical strata only.
2. **`none` as a signal class (7 rows)** — these are scored rows with no dominant class
   assigned. They are excluded from per-class tables and included in tier/tape tables.
3. **2 tickers unresolvable for OHLC**: `BRKB` (needs `BRK-B`) and `SPX` (needs `^GSPC`).
   Same two as every prior cycle; 166/168 symbols fetched, real high/low verified.
   Affected rows are tagged INCONCLUSIVE `data_unavailable` (5 rows), never LOSS.
4. **`insider_cluster_flag` and `dp_block_to_float_ratio` are present-but-null.**
   The key exists on 164 calls; `dp_block_to_float_ratio` is populated on **1**, and
   `insider_cluster_flag` on **15 — every one of them `False`**. See Phase 6d; this is the
   single most consequential data-quality finding of the cycle and it corrects a claim made
   by the previous audit.
5. **W32 weekly shares report_date 2026-08-07 with the Friday daily** — 15 rows on that
   date across two envelopes. Expected, not a duplicate-call defect; the one-row-per
   (report_date, ticker) rule is applied within envelope kind.

## Outputs

- `phase_1_inventory.jsonl` — 626 rows
- `_tickers.json` — 168 symbols
- `_ohlc/` — 166 symbol bar files, `_ohlc_manifest.json`
