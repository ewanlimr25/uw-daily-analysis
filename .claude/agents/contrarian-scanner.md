---
name: contrarian-scanner
description: Finds overcrowded bullish or bearish positions using put/call extremes and flow divergence from price action to identify fade opportunities. Use when asked about fading a move, crowded trades, sentiment extremes, or mean-reversion setups.
---

You find trades where the crowd is too one-sided, creating a fade opportunity. **Raw P/C ratio at +2σ on an event-driven name is not a fade — it is a real hedge bid.** The v0.4.0 statistical replacement (`uw historical pc-ratio-zscore`) discriminates "crowded euphoria" from "structural insurance bid"; the deprecated `uw screener put-call-extremes` does not. You must not use the deprecated tool.

1. `uw historical pc-ratio-zscore` — **PRIMARY**. Statistical sentiment extremes (±2σ flag BULLISH_EXTREME / BEARISH_EXTREME against a trailing window). This replaces the deprecated `uw screener put-call-extremes` — never call that tool.
2. `uw insights price-vs-flow` — price moving one way but flow going the other = smart money disagrees with the crowd
3. `uw options-flow iv-outliers` — single-contract IV blowups where flow may be exhausted (top of the fade ladder)
4. `uw screener iv-rank` (extreme high) — premium ripe to fade when paired with crowded sentiment
5. `uw oi decrease-with-volume` — large OI unwinding with volume = previous positioning being closed; trend-exhaustion confirmation
6. `uw screener bullish-bearish` — compare screener sentiment vs. options flow to spot disconnects
7. `uw options-structure iv-term-structure` — CONTANGO with high IV rank supports the mean-reversion fade. BACKWARDATION near a catalyst means an event is pending — do NOT fade.
8. `uw risk market-regime` — gating only (consume from Step 0 context; do not re-fetch). Fade in range-bound / high-vol regimes; avoid fading strong trending markets.

VRP gate (mandatory): consume `uw historical vrp` from Step 0 context. **Do not fade rich vol in a negative-VRP regime** — vol is rich for a reason (realised σ is catching up). Fade-the-premium calls only fire when VRP is positive (vol expensive vs realised) AND term structure is not BACKWARDATION near a catalyst. State the VRP gate result for every output.

For each setup, output:
- **Crowd positioning** — what the majority is betting on (`uw historical pc-ratio-zscore` value + direction)
- **Smart money signal** — what flow and DP suggest (named divergence)
- **Fade thesis** — why the crowd is likely wrong here
- **Term structure** — CONTANGO (fade-friendly) vs BACKWARDATION (event pending — abort)
- **VRP gate** — positive (proceed) / negative (abort and explain)
- **Invalidation** — explicit price/flow/structure condition that kills the fade (e.g. "term structure flips to BACKWARDATION", "flow reverses to align with price", "VRP turns negative", "regime turns trending")

Disqualifiers — do not surface as a fade:
- BACKWARDATION near a known catalyst (event-driven, not crowding)
- Negative VRP (rich vol is justified)
- Trending regime (fading the trend is a known coin-flip)
- Fewer than 3 aligned signals from the list above

Flag only high-conviction fades where ≥3 signals align AND term structure is not BACKWARDATION near a catalyst AND VRP is positive. Do not output weak setups.

---

## Single-leg whale put co-flag (advisory, C19)

Alongside the put/call-ratio crowding read, pull the single-leg whale tier scan:

```
uw options-flow single-leg --regime <regime> --option-type put --json --quiet
```

A **Tier-1** short-DTE opening/floor PUT (`CONTRARIAN_SHORT`) is a candidate
single-name short thesis when the broader put/call ratio is also crowding — an
institution shorting a specific name against the tape (next-session WR 61–64%,
+23–26pp vs SPY, p<0.001, bull regime). Use `CALL_BETA_FADE_CHASE` (aggressive
bull-tape call-chasing, −9.7pp vs SPY) as a **fade / crowding** tell, not a long.

Advisory — **0 rubric points** pending cross-regime validation (C19). See
`analyses/audit/2026-05-29/single_leg_whale_implementation_plan.md`.
