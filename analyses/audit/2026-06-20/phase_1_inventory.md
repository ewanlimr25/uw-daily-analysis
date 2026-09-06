# Phase 1 — Inventory & Parse · 2026-06-20

**Dataset.** 23 machine-readable decision envelopes (19 daily, 4 weekly), **all 23 valid** against `schemas/decision_envelope.schema.json`. **201 normalized per-call rows** extracted directly from `calls[]` — no prose re-parsing, no `Σ points` reconciliation needed (validator guarantees it; **0 of 201** rows have `Σ score_components.points ≠ raw_score`).

Report span: **2026-05-25 → 2026-06-18** (19 distinct daily dates + weekly W22–W25).

Provenance basis for the whole audit: **verbatim envelope** (`score_components[].source_tool`, `win_rate`, `gate_verdicts` read directly). This clears the C23 provenance bar for headline findings — *except* where stratified-N falls below the decided-N floors (most acute in the frozen-rubric era; see below).

## Breakdown

| Axis | Distribution |
|---|---|
| Kind | daily 182 · weekly 19 |
| Horizon | swing 161 · vol 39 · LEAP 1 |
| Section | watch_only 78 · swing_long 57 · swing_short 38 · vol_short 19 · vol_long 9 |
| Tier | DROP 107 · LOW 67 · MEDIUM 20 · **HIGH 7** |
| Direction | long 96 · short 63 · vol_short 23 · vol_long 11 · neutral 8 |
| Final size | watch_only 102 · skip 70 · **starter 16 · half 12** · veto 1 |
| Fundamentals verdict | NA 67 · (none) 52 · CONFIRM 41 · CAUTION 36 · **VETO 5** |

### Rubric-era stratification (never pool — C23 / P0.1)

| Era | N | Meaning |
|---|---|---|
| `era_0525_0529` | 54 | earliest envelopes, pre-validator-fix |
| `era_0530_0605` | 69 | raw-9 recorded MEDIUM (validator stale, P1.1 not yet applied) |
| `pre_freeze_post_0606` | 28 | post P1.1 validator (≥9=HIGH), pre-freeze weights |
| **`2026-06-12` (FROZEN, live)** | **50** | the rubric the system runs today — **all from 06-12→06-18** |

## Desk read — five structural facts before any outcome is resolved

1. **The book is tiny and defensive.** Of 201 calls only **28 carry real size** (16 starter + 12 half, **0 full**); 102 are `watch_only`, 70 `skip`, 1 `veto`. The fleet is a *rejection machine* — it disqualifies ~86% of what it surfaces. That makes outcome-based gate-effectiveness (Phase 6) structurally thin and means the calibration question is mostly *"are the few names it sizes actually better than the ones it benches?"*

2. **The frozen rubric cannot be outcome-graded today.** The live rubric (`2026-06-12`) has 50 calls, **all dated 06-12→06-18**. With today = 06-20 and last bar = 06-18, none of its swing 3D/10D or vol windows have closed. Phase 3/5 grade it *structurally only*; the outcome evidence still grades the **pre-freeze** weights. This is the freeze-lift checkpoint answering itself: **we are nowhere near the ≥30 resolved post-freeze calls** the P0.6 half-cap lift requires.

3. **Claimed win-rates are substrate-contaminated.** Of 132 rows carrying `win_rate`, **117 are `backtest`/`fallback_proxy`** (the pre-quarantine `signal-backtest` substrate flagged broken in the 2026-06-12 audit) and only **17 are `backtest_clean`**. Every claimed-vs-realised divergence in Phase 3 must be read against this: the "claim" side is mostly a known-bad oracle, so a divergence is as likely a substrate artefact as a rubric lie.

4. **Even some DROP-tier names got sized.** `final_size ∈ {starter,half}` appears on **6 DROP-tier rows** (tier DROP, raw ≤2). Either these are vol-structure rows where tier semantics differ, or a sizing-compliance leak — flagged for Phase 6.

5. **Signal-class labels are fragmented** — see data-quality flags; the dealer family alone is split 5 ways, which will starve every dealer sub-class below the decided-N≥8 floor unless merged.

## Data-quality flags

- **Signal-class label fragmentation (carry into Phase 3/4 as a merge map).**
  - *Dealer family split 5 ways:* `dealer_positioning` (8) · `dealer_positioning_flip` (2) · `dealer_flip` (1) · `dealer-positioning_dex_flip` (1) · `dex_flip_long` (1) → merged = 13 (clears N≥8; split = all sub-floor).
  - *Distribution split:* `dark_pool_distribution` (2) · `distribution` (1).
  - *Single-leg variants:* `bearish_flow_single_leg_put` (1) · `single_leg_whale` (1) sit apart from `bearish_flow` (39) / `bullish_flow` (31).
  - *Conflicted variants:* `multileg_directional_conflicted` (1), `directional_conflict` (1) apart from `multileg_directional` (18).
  - **Decision:** Phase 3/4 score on a *canonicalized* class map (dealer\* → `dealer_positioning`; \*distribution → `dark_pool_distribution`) **and** report the raw split, so a label-hygiene fix can be pre-registered without inflating any class's N dishonestly.
- **Legacy-prose coverage gap (intentional).** 17 legacy daily (`2026-04-30 → 2026-05-22`) + 4 legacy weekly (`W18–W21`) predate the envelope and are **excluded** — they lack `score_components`/`win_rate`/`gate_verdicts`, and were already outcome-resolved by the 05-30 / 06-06 / 06-12 audits. The skill makes the envelope authoritative when present; re-parsing prose would add noise, not signal. Stated as a gap, not silently dropped.
- **Tier skew.** Only 7 HIGH and 20 MEDIUM across the whole set — the conviction reliability diagram (Phase 3) will be HIGH-tier N-starved; any tier-inversion read there is advisory until N grows.

## Outputs
- `phase_1_inventory.jsonl` — 201 rows, one JSON object per call (full field set incl. `rubric_era`, `tools_cited`, `gates_fired`, `fz_*`, `fundamentals_verdict`, `debate_residuals`).
- `_tickers.json` — 74 unique symbols (incl. SPY) for the Phase 2 OHLC fetch.
- `_ohlc/` — real daily OHLC (46 bars, 04-15→06-18) for all 74; SPY real-OHLC sanity-checked ✅.
