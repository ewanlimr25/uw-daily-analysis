# Phase 4 — Tool Attribution (2026-07-11)

**Provenance: VERBATIM** (`decision.json` `score_components[].source_tool`), N as noted. Class-controlled marginal contribution (`winrate_with − winrate_without`, class-weighted). **Single-regime caveat:** the envelope dataset is dominated by TRANSITIONAL/UPTREND; every finding is single-regime → **pre-registration-only, cannot rate P0** regardless of verbatim provenance.

| Tool | Cited | Marginal | Tier | Note |
|---|---|---|---|---|
| `uw insights institutional-accumulation` | 16 | **−22.2pp** | NEGATIVE | backs the +3 accumulation conjunction |
| `uw historical oi-trend` | 54 | **−17.8pp** | NEGATIVE | backs the +3 weekly OI line — **C47 corroborated** |
| `uw historical cumulative-premium-flow` | 82 | −7.2pp | NO-INFO | **UBIQUITY-confounded** (82/106 rows) — base-rate citation, not dead |
| `uw options-structure dex` | 34 | −6.5pp | NEGATIVE | the demoted +1 mechanized-flip line's tool |
| `uw options-structure front-end-iv-ratio` | 6 | −44.4pp | negative (THIN_N) | panic gate; n=6 |
| `uw options-structure term-skew` | 12 | −4.4pp | NO-INFO | |
| `uw hot-chains multileg` | 23 | −3.5pp | NO-INFO | |
| `uw insights signal-confluence` | 41 | −4.2pp | NO-INFO | already removed from scoring (P0.2) |
| `uw options-flow sector-flow-persistence` | 30 | +2.0pp | NO-INFO | |
| `uw dark-pool block-stratified` | 8 | +15.9pp | supportive (THIN_N) | the institutional/retail filter; n=8 |

## Desk read (market-maker quant)
**The two highest-weighted rubric lines are backed by the two most-negative tools.** `institutional-accumulation` (−22.2pp) and `oi-trend` (−17.8pp) are the +3-and-+3 spine of the conviction score, and both measure strongly negative class-controlled marginal on verbatim data. This is the same signal Phase 3 sees from the outcome side: the accumulation complex is anti-predictive in this regime.

- **`oi-trend` −17.8pp sharpens C47** (was −9.2pp at the 2026-07-04 audit). The saturation mechanism is now visible in outcomes, not just in the `consecutive_build_days == --days` ceiling — but the frozen era is single-regime, so C47's acceptance bar (cross-regime ∧ n≥30/arm ∧ BH) is **not** met. Carry, do not act.
- **`dark-pool block-stratified` reads +15.9pp** but at n=8 (THIN_N, provisional) — the institutional/retail filter may be the one piece of the accumulation stack that works; it is precisely the gate the raw accumulation tools lack. Worth a pre-registered isolation test.
- **`cumulative-premium-flow` NO-INFO is ubiquity-confounded** (cited on 82 of 106 decided non-DROP rows) — `with ≈ without` by construction; it stays in the LB gate as documented, not declared dead.

## `fz` advisory axes (C15–C18)
All `fz_context` fields remain **INSUFFICIENT_N** for outcome scoring on the decided set (short-float/days-to-cover/float populated on the top-5 only, <10 decided per axis). No promotion cleared; C15–C18 stay advisory. `breadth_cross_check` never diverged in-sample (pct_green>50 every capture) → no divergence→drawdown test possible.

Output: numerics embedded above.
