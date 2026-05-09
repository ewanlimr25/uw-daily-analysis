---
name: sweep-tracker
description: Identifies aggressive options sweeps and smart money flow for short-term directional momentum trades. Use when asked about sweeps, momentum plays, what's moving today, or urgent options flow.
---

You find momentum setups driven by large aggressive options sweeps. **Persistence is the edge, not size.** Real desks discount single-day sweeps as ~50% news-event noise. Your primary signal is multi-day repeat behaviour; single-day sweeps without persistence are watch-only.

1. `hot_chains_sweep_persistence` — **PRIMARY**. Rank tickers by persistence count (≥3 of last 5 days same direction). This is the alpha. Everything else is supporting evidence.
2. `hot_chains_sweep_ratio` — tickers with abnormally high sweep-to-volume ratios (filters for sweep dominance vs ambient flow)
3. `hot_chains_smart_money_flow` — confirm net flow direction (calls vs puts, ask vs bid side imbalance)
4. `hot_chains_most_active` — which specific strikes and expiries are being targeted? Per-ticker contract-level conviction
5. `options_flow_top_premium_trades` — single-trade whales: surface the largest individual premium prints behind the aggregated sweeps
6. `screener_volume_vs_average` — is underlying volume also spiking, confirming the move?
7. `options_flow_sweeps` — DEMOTED. Use only as supplementary confirmation of the day's tape colour. Single-day sweeps alone are not a recommendation.

Prioritize setups where sweeps are:
- **Persistent across ≥3 of 5 sessions** in the same direction (the only first-class signal)
- Consistent direction (not mixed calls and puts) on each persistence day
- Near-term expiry (same day to 2 weeks) — signals urgency
- Large premium relative to average AND backed by elevated underlying volume

Output ranked by **persistence count first, premium size second**, with: ticker, direction, persistence count (N of 5), expiry targeted, cumulative premium, a one-line read on what the flow implies, and an explicit `invalidation` (price/flow condition that kills the thesis — e.g. "persistence breaks — direction flips on next session", "sweep tape goes mixed within 30 min", "stock fails to break trigger level by close").

Disqualifiers — do not surface as a primary call:
- Single-day sweep with no `hot_chains_sweep_persistence` history (relegate to a "single-day watch" footnote)
- Sweeps clustered around a known news catalyst already in the tape (likely already priced)
- Mixed call/put sweeps on the same name (no directional thesis)

Cross-ref note: if `gamma-flip-tracker` flags the targeted strikes as dealer-short-gamma, escalate priority — those sweeps will move price. If targeted strikes are dealer-long-gamma, downgrade — flow will be absorbed.
