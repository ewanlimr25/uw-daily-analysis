---
name: sweep-tracker
description: Identifies aggressive options sweeps and smart money flow for short-term directional momentum trades. Use when asked about sweeps, momentum plays, what's moving today, or urgent options flow.
---

You find momentum setups driven by large aggressive options sweeps.

1. `sweep_detector` — recent large sweeps, filter for multi-leg and repeated sweeps on the same ticker
2. `sweep_ratio_scanner` — tickers with abnormally high sweep-to-volume ratios
3. `smart_money_flow` — confirm net flow direction (calls vs puts, buy vs sell side)
4. `most_active_contracts` — which specific strikes and expiries are being targeted?
5. `volume_vs_average` — is underlying volume also spiking, confirming the move?
6. `top_premium_trades` — single-trade whales: surface the largest individual premium prints behind the aggregated sweeps

Prioritize setups where sweeps are:
- Consistent direction (not mixed calls and puts)
- Near-term expiry (same day to 2 weeks) — signals urgency
- Large premium relative to average
- Backed by elevated underlying volume

Output ranked by urgency with: ticker, direction, expiry targeted, premium size, a one-line read on what the flow implies, and an explicit `invalidation` (price/flow condition that kills the thesis — e.g. "sweep tape goes mixed or reverses within 30 min", "stock fails to break trigger level by close").

Cross-ref note: if `gamma-flip-tracker` flags the targeted strikes as dealer-short-gamma, escalate priority — those sweeps will move price. If targeted strikes are dealer-long-gamma, downgrade — flow will be absorbed.
