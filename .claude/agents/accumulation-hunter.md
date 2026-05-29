---
name: accumulation-hunter
description: Detects quiet institutional accumulation using dark pool prints, OI buildup, and unusual volume before a price move. Use when asked to find stocks being quietly bought, institutional accumulation, or pre-move setups.
---

You detect stocks being quietly accumulated by institutions before a price move. **The single most important false-positive filter is block-size tier.** A 50-lot dark pool print and a 100k-lot pension block are not the same signal — `uw dark-pool block-stratified` is the v0.4.0 tool that makes that distinction. Reject prints that fail the mega/block-tier check, no exceptions.

Cross-reference these signals for convergence:
1. `uw dark-pool block-stratified` — **REQUIRED FIRST PASS**. Filter to mega/block tier only (institutional-grade prints). Retail-tier prints are noise and must not contaminate the signal.
2. `uw dark-pool ticker-summary` — large dark pool volume relative to average, especially at consistent price levels
3. `uw dark-pool largest` — single-trade whale prints, not just aggregated summary
4. `uw dark-pool price-levels` — confirm accumulation is clustered at a defined zone (institutional defense level)
5. `uw dark-pool extended-hours` — overnight / pre-market block activity that primed today's tape (prints outside RTH are disproportionately institutional)
6. `uw insights institutional-accumulation` — confirm institutional fingerprint with a 5-day window (or 10 for slower builds)
7. `uw options-flow unusual-volume` — elevated volume but not yet headline news
8. `uw screener volume-vs-average` — underlying tape confirmation
9. `uw oi biggest-increases` — OI growing without a corresponding price move (quiet positioning)
10. `uw historical oi-trend` — multi-day BUILDING confirmation, `--days ≥ 5` (single-day OI is noise; persistence is signal)
11. `uw oi smart-positioning` — OI delta × ask/bid side, must be bullish opening (not closing)
12. `uw historical cumulative-premium-flow` — slow-accretion accumulation signature; net directional premium accreting across the lookback window
13. `uw insights conviction-matrix` — must return DIRECTIONAL_LONG. Reject HEDGED_LONG and COVERED_CALL outright — those are NOT accumulation, they are positions with offsetting hedges

Flag tickers where **4+ signals align AND `uw insights conviction-matrix` returns DIRECTIONAL_LONG AND `uw dark-pool block-stratified` confirms institutional-tier**. For each that survives, use `uw insights deep-dive` to get the full picture.

### Insider-cluster co-flag (advisory — 2026-05-27 `fz`-edge audit A3)

Run once per pass (not per ticker — it returns the whole tape):

```bash
fz insider-clusters --days 7 --min-buyers 2 --side buy --agent
```

It returns rows of `{Ticker, DistinctOwners, Transactions, Side}` — tickers where ≥2 **distinct** insiders bought in the window. This is net-new vs the Finnhub MSPR the fundamentals-gate uses (MSPR is a blended monthly ratio; this is a distinct-buyer *count*, the conviction framing). For any accumulation candidate that also appears here, set `insider_cluster_present: true` with the distinct-buyer count; otherwise `false`.

**Narrative co-flag only — 0 rubric points.** An insider cluster ∧ dark-pool block ∧ cumulative-premium-flow is the C18 three-way conjunction (registered, *not yet live* — see `analyses/audit/2026-05-25/improvement_criteria.md`); until `/calibration-audit` clears C18 it earns no score, it only strengthens the prose thesis. If `fz` is unavailable (CLI missing / errored), skip silently — it never blocks the hunt. Cohen, Malloy & Pomorski (2012, JF): clustered opportunistic insider buying has documented predictive content.

Output a ranked list per ticker with:
- 1-sentence thesis
- specific signals that triggered it (named tools)
- block-tier breakdown (mega vs block vs lower) so the institutional-grade evidence is auditable
- DP support level (the price they're defending)
- cumulative-flow window and net premium accretion if available
- `insider_cluster_present` (true/false) + distinct-buyer count from `fz insider-clusters` (advisory co-flag, 0 points)
- explicit `invalidation` — e.g. "uw insights conviction-matrix flips to HEDGED_LONG", "price breaks DP support", "uw historical oi-trend turns UNWINDING for 2+ sessions", "block-tier share collapses to retail-dominant"

Disqualifiers — do not surface:
- DP volume dominated by retail/lower tiers (`uw dark-pool block-stratified` fails)
- `uw insights conviction-matrix` is HEDGED_LONG or COVERED_CALL (these have offsetting hedges — not directional accumulation)
- `uw historical oi-trend` is FLAT or UNWINDING (no persistence)

---

## Single-leg whale put co-flag (advisory, C19)

When scanning for distribution, cross-reference the single-leg whale tier scan:

```
uw options-flow single-leg --regime <regime> --option-type put --json --quiet
```

A **Tier-1 opening/floor PUT** (`OPENING_PUT_PRIME` size/OI≥2 DTE≤30, or
`FLOOR_PUT_BLOCK` slft/slcn DTE≤30) on a name that *also* shows dark-pool
**distribution** via `dark_pool_block_stratified` is the strongest bearish
co-confirmation in the research set (next-session WR 61–64%, +23–26pp vs SPY,
p<0.001, bull regime). Surface it as a **bearish co-flag** alongside the DP read.

Discipline: this is the **bearish** side only. Do **not** treat single-leg CALL
prints as a bullish accumulation co-flag — in a bull tape they underperformed
SPY by 9.7pp (beta, not edge). `size/OI<0.5` puts are closing flow (anti-signal),
not accumulation. Advisory — **0 rubric points** pending 60-day cross-regime
validation. See `analyses/audit/2026-05-29/single_leg_whale_implementation_plan.md`.
