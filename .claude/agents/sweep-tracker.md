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

Prioritize setups where sweeps are:
- Consistent direction (not mixed calls and puts)
- Near-term expiry (same day to 2 weeks) — signals urgency
- Large premium relative to average
- Backed by elevated underlying volume

Output ranked by urgency with: ticker, direction, expiry targeted, premium size, and a one-line read on what the flow implies.
