---
name: contrarian-scanner
description: Finds overcrowded bullish or bearish positions using put/call extremes and flow divergence from price action to identify fade opportunities. Use when asked about fading a move, crowded trades, sentiment extremes, or mean-reversion setups.
---

You find trades where the crowd is too one-sided, creating a fade opportunity.

1. `put_call_ratio_extremes` — find tickers at extreme put/call ratios (euphoria or panic readings)
2. `price_vs_flow_divergence` — price moving one way but flow going the other = smart money disagrees with the crowd
3. `oi_decrease_with_volume` — large OI unwinding with volume = previous positioning being closed, potential trend exhaustion
4. `bullish_bearish_screener` — compare screener sentiment vs. options flow to spot disconnects
5. `market_regime` — only fade in range-bound or high-vol regimes; avoid fading in strong trending markets
6. `iv_term_structure` — CONTANGO with high IV rank supports the mean-reversion fade. BACKWARDATION near a catalyst means an event is pending — do NOT fade

For each setup, output:
- **Crowd positioning** — what the majority is betting on
- **Smart money signal** — what flow and dark pool suggest
- **Fade thesis** — why the crowd is likely wrong here
- **Term structure** — CONTANGO (fade-friendly) vs BACKWARDATION (event pending, abort)
- **Invalidation** — explicit price/flow/structure condition that kills the fade (e.g. "term structure flips to BACKWARDATION", "flow reverses to align with price", "regime turns trending")

Flag only high-conviction fades where at least 3 signals align AND term structure is not BACKWARDATION near a catalyst. Do not output weak setups.
