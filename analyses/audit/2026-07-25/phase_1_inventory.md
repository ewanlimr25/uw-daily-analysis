# Phase 1 — Inventory & Parse (2026-07-25)

**Provenance basis: 100% VERBATIM.** All 526 rows come from `decision.json` `calls[]`
via `scripts/validate_decision.py`-clean envelopes. Zero prose reconstruction. Per the
C23 provenance rule this audit is **eligible to rate findings P0** — with the caveat
that P0 findings here land on *auditor method*, not on the frozen subject rubric.

## Dataset

| | |
|---|---|
| Envelopes parsed | **52** (43 daily + 9 weekly) |
| Calls extracted | **526** |
| Unique tickers | 155 |
| Date range | 2026-05-25 → 2026-07-24 |
| New since the 2026-07-18 audit | **63 rows / 6 envelopes** (07-20, 07-21, 07-22, 07-23, 07-24, W30) |
| Envelope schema validation | **52 / 52 pass, 0 failures** |
| `Σ score_components.points ≠ raw_score` | **0** |

## Coverage gap (unchanged, structural)

17 daily + 4 weekly reports predate the decision envelope (legacy prose, ≤2026-05-22).
They were resolved by earlier audits and carry no `score_components` / `win_rate`, so they
are excluded rather than prose-reparsed. This is a **deliberate** exclusion: mixing
reconstructed citations into a verbatim dataset would cap every finding at P1 (C23).

## Stratification (never pooled)

| Rubric era | Rows |
|---|---|
| **`2026-06-12` (FROZEN)** | **375** |
| `era_0530_0605` | 69 |
| `era_0525_0529` | 54 |
| `pre_freeze_post_0606` | 28 |

| Regime bucket (label) | Rows |
|---|---|
| uptrend | 171 |
| transitional_other | 170 |
| pullback_in_uptrend | 128 |
| choppy | 57 |

> **Data-quality flag — the regime label is too coarse to stratify on.** All 170
> `transitional_other` rows carry the bare string `TRANSITIONAL` and span 2026-06-30 →
> 2026-07-23, a period containing *both* rising and falling tape. Every prior audit's
> regime conclusions were drawn on this label. Phase 3c introduces an **empirical tape
> stratification** (sign of SPY's realised return over each row's own window) to replace it.

## Distributions

- **Tier**: DROP 405 / LOW 94 / MEDIUM 20 / HIGH 7. Post-freeze: DROP 343 / LOW 32 / **MEDIUM 0 / HIGH 0**.
- **Direction**: long 214, short 160, vol_short 96, neutral 31, vol_long 25.
- **Horizon**: swing 384, vol 133, LEAP 9.
- **Final size**: watch_only 240, skip 231, starter 35, half 12, veto 7, full 1.
- **Fundamentals verdict**: NA 157, CAUTION 83, CONFIRM 82, VETO 14, absent 190.
- **`win_rate_source`**: `NA(substrate)` 201, `backtest_clean` 91, `backtest` 84, `NA` 62, `fallback_proxy` 33, absent 55.
- **Top signal classes**: bearish_flow 110, earnings_vol 100, multileg_directional 67, bullish_flow 52, dark_pool_accumulation 52.

## Desk read

Sixth straight cycle in which the frozen rubric emitted **zero HIGH and zero MEDIUM**
calls. 375 post-freeze rows produced 32 LOW and 343 DROP. Whatever else this audit
finds, the freeze-lift test still cannot be run — not because the evidence is
ambiguous but because the population it needs does not exist.

Outputs: `phase_1_inventory.jsonl` (526 rows), `_tickers.json`.
