# Phase 1 — Inventory & Parse · 2026-07-04

**Dataset.** 45 daily + 10 weekly reports on disk. **34 decision envelopes** parsed (28 daily, 6 weekly) → **335 normalized rows**, 118 unique tickers. All 6 envelopes new since the 2026-06-27 audit (`2026-06-29/30`, `2026-07-01/02`, `W26`, `W27`) pass `scripts/validate_decision.py`; W26 was already inside the prior audit's window, so the net-new call count is **78 rows across 5 envelopes**. The 17 pre-2026-05-25 dailies and 4 pre-W22 weeklies are legacy prose (no envelope) — coverage gap unchanged from prior audits; they lack `score_components`/`win_rate` and stay excluded (their outcomes were resolved in the 05-30/06-06 audits and nothing in this run's questions depends on them).

**Provenance: 100% verbatim-envelope.** Zero prose-reconstructed rows. Tool-tier findings this run are NOT provenance-capped.

## Row breakdown

| Axis | Distribution |
|---|---|
| Kind | daily 304 · weekly 31 |
| Rubric era | **2026-06-12 (frozen) 184** · era_0530_0605 69 · era_0525_0529 54 · pre_freeze_post_0606 28 |
| Regime bucket | pullback_in_uptrend 128 · uptrend 122 · **transitional_other 67 (new era)** · choppy 18 |
| Horizon | swing 258 · vol 71 · LEAP 6 |
| Section | watch_only 164 · swing_long 69 · swing_short 61 · vol_short 28 · vol_long 12 · leap_disq 1 |
| Tier | DROP 229 · LOW 79 · MEDIUM 20 · HIGH 7 |
| Direction | long 150 · short 111 · vol_short 47 · vol_long 15 · neutral 12 |
| Fundamentals verdict | None 116 · NA 105 · CAUTION 54 · CONFIRM 51 · VETO 9 |
| Final size | watch_only 181 · skip 112 · starter 26 · half 12 · veto 4 |
| win_rate_source | backtest 84 · NA(substrate) 73 · NA 54 · backtest_clean 53 · none 38 · fallback_proxy 33 |

Top signal classes (raw labels; Phase 2 canonicalizes the dealer*/distribution fragments): bearish_flow 71, earnings_vol 49, dark_pool_accumulation 46, multileg_directional 44, bullish_flow 39, high_iv_rank 15, sector_rotation 11, multi_day_sweep 9, dealer_positioning 8 (+21 single-digit fragments).

## Mechanical checks

- **Σ `score_components.points` == `raw_score`: 335/335.** Zero mismatches (validator-guaranteed on envelopes; re-confirmed here).
- Every row carries `rubric_version` (all envelope-borne; era-banding needed only for pre-1.3 envelopes, handled by changelog banding).
- `post_freeze` rows: 184. `out_of_regime` (regime string carries the half-cap marker): 29.

## Data-quality flags

1. **Post-freeze tier distribution is DROP 167 / LOW 17 / MEDIUM 0 / HIGH 0.** The frozen rubric has *still* never emitted a sized HIGH or MEDIUM call — 4th audit running. The empty-book protocol (07-01 all-DROP board, 07-02 near-empty, W27 no-HIGH/MED) is behaving as designed, but it makes the freeze-lift's HIGH≥MED monotonicity test structurally unrunnable (see Phase 5).
2. **The 06-29→07-02 dailies carry large all-DROP paper books** (28 and 27 calls) — these inflate the DROP/watch_only denominators; Phase 2 carries `was_sized` so the sized-book view stays separable.
3. Signal-class label fragmentation persists in fresh envelopes (`dex_flip_long`, `dex_flip_short`, `multileg_repeat`, `sector_leader` — 1–2 rows each). Canonicalized downstream; a schema-enum pre-registration remains open from prior audits.
4. `win_rate_source`: the post-quarantine labels (`backtest_clean`, `NA(substrate)`, `NA`) now dominate new rows — the 06-27 Rec-3 emission hygiene is visible in the data (Phase 6 verifies the cap itself).
5. Choppy bucket (18 rows, 06-23→06-26) was 100% window-open at the last audit; with bars through 2026-07-02 the 3D windows and most 10D thresholds are now decidable — this is the first audit that can grade the selloff/choppy stratum.

Machine-readable: `phase_1_inventory.jsonl` (335 rows). Ticker universe: `_tickers.json` (118).
