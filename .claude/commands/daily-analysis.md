# Daily Market Analysis

Run a full post-market intelligence report by horizon (0DTE / Swing / LEAP), using a two-phase agent fleet. Phase 1 spawns 8 alpha-finding agents in parallel. Phase 2 runs `risk-monitor` against the candidate set surfaced by Phase 1. Score conviction formally, write winners back to the watchlist, and save the report to `analyses/YYYY-MM-DD.md`.

## Operating principle: prefer multi-day metrics

Wherever a multi-day tool exists alongside a single-day equivalent, use the multi-day one. Specifically: prefer `oi_trend` over single-day `biggest_oi_increases`, prefer `trend_analyzer` over single-day metrics, and pull `signal_backtest` win-rates before sizing. Single-day signals are noise; multi-day persistence is the edge. Pass this instruction through to every spawned agent.

## Steps

### 0. Preflight — `daily_synthesis` + date

1. Use `date` to get today's date in YYYY-MM-DD format. This becomes the filename and the `conviction_<date>` watchlist group name.
2. Call `mcp__uw-insights__daily_synthesis` with today's date. This returns the regime classification, top bullish/bearish confluence, and watchlist alerts in a single call. **Pass this synthesis output to every Phase 1 agent** so they don't redundantly call `market_regime` or `signal_confluence`. The synthesis is the shared context anchor for the run.

### 1. Phase 1 — Alpha-finding agents (parallel)

Spawn these 8 agents **simultaneously** in a single batch — do NOT run them sequentially. Hand each one the `daily_synthesis` output from Step 0.

- **gamma-flip-tracker**: Map dealer GEX, zero-gamma levels, and ATM gamma flip strikes for SPY/QQQ/IWM and any liquid name with significant 0DTE volume. Flag pin vs trend regime.
- **sweep-tracker**: Surface today's most aggressive options sweeps; rank by urgency (near-term expiry, premium size, ask-side conviction).
- **accumulation-hunter**: Identify tickers with quiet, multi-day institutional accumulation across dark pool, OI, and smart-money flow.
- **contrarian-scanner**: Find overcrowded positions and high-conviction fade setups; gate on regime.
- **earnings-scout**: Evaluate upcoming earnings plays via IV term-structure kink alignment, pre-event flow, and analyst-vs-flow disagreement.
- **vol-surface-scout**: Scan `iv_term_structure` for KINKED / BACKWARDATION names; flag IV outliers and calendar-spread candidates.
- **multileg-strategist**: Read the structure of institutional flow — verticals, calendars, condors, flies — and infer directional thesis.
- **leap-positioning-radar**: Surface long-dated (DTE > 180) institutional positioning. Demand `conviction_matrix` = DIRECTIONAL_LONG and multi-day `oi_trend` BUILDING.

### 2. Phase 2 — Risk monitor (sequential, consumes Phase 1)

Once all Phase 1 agents return, collect every candidate ticker they surfaced. Spawn **risk-monitor** with that candidate set as input — it must run `mcp__uw-risk__portfolio_correlation` on **today's candidates**, not the static watchlist. This closes the loop: risk is measured against what we're actually considering, not yesterday's leftovers.

### 3. Score conviction (formal rubric)

For every ticker that appeared in any Phase 1 output, compute the conviction score:

```
Conviction score = Σ:
  +3  flagged by gamma-flip-tracker as setting up a regime breakout
  +2  3+ aligned signals in accumulation-hunter
  +2  multi-day OI build (oi_trend BUILDING, > 5 days)
  +2  conviction_matrix = DIRECTIONAL_LONG, confidence > 70
  +1  in sweep-tracker top 5
  +1  in earnings-scout BUY VOL or SELL VOL
  +1  in multileg-strategist with directional structure
  -2  contrarian-scanner flags as overcrowded long
  -1  risk-monitor flags in correlation cluster
  -3  market_regime conflicts with the trade direction
```

Surface every ticker with **score >= 5** in the Executive Summary and in §7 (High-Conviction Cross-Ref).

### 4. Backtest-weighted sizing

For each ticker scoring >= 5, identify its dominant signal class (e.g. "sweep", "accumulation", "gamma_breakout", "leap_oi_build") and call `mcp__uw-historical__signal_backtest` on that signal type. Use the returned `win_rate` to weight position sizing in the Executive Summary:
- win_rate >= 0.65 → full size
- 0.50 <= win_rate < 0.65 → half size
- win_rate < 0.50 → starter / skip

Note the win_rate explicitly next to each top call.

### 5. Write the report

Synthesize everything into the structured markdown below. The report is organized **by trade horizon**, not by agent.

```
# Daily Market Analysis — YYYY-MM-DD

## Executive Summary
- **Regime + GEX state:** <one line, sets the day's bias>
- **Top 0DTE play:** <ticker, setup, invalidation> or "no edge"
- **Top swing build:** <ticker, thesis, invalidation>
- **Top LEAP candidate:** <ticker, scenario, invalidation>
- **Biggest risk:** <correlation cluster or adverse flow>

## 1. Regime & Gamma State
[risk-monitor regime + gamma-flip-tracker GEX state for SPY/QQQ/IWM]

## 2. 0DTE / Intraday Plays
[gamma-flip-tracker per-ticker plays + sweep-tracker urgency-ranked sweeps with near-term expiry]

## 3. Swing Setups (1–6 weeks)
[accumulation-hunter + multileg-strategist + contrarian-scanner + earnings-scout setups, ranked by conviction score]

## 4. LEAP Builds (6–24 months)
[leap-positioning-radar with full DIRECTIONAL_LONG candidates only]

## 5. Volatility Surface
[vol-surface-scout — KINKED names, BACKWARDATION calendars, IV outliers]

## 6. Risk & Correlation
[risk-monitor consuming today's Phase 1 candidates — not static watchlist]

## 7. High-Conviction Cross-Ref
[Formal scoring per the rubric below; surface score >= 5]
```

Embed the conviction-scoring rubric verbatim at the bottom of §7 so future readers can audit the scores:

```
Conviction score = Σ:
  +3  flagged by gamma-flip-tracker as setting up a regime breakout
  +2  3+ aligned signals in accumulation-hunter
  +2  multi-day OI build (oi_trend BUILDING, > 5 days)
  +2  conviction_matrix = DIRECTIONAL_LONG, confidence > 70
  +1  in sweep-tracker top 5
  +1  in earnings-scout BUY VOL or SELL VOL
  +1  in multileg-strategist with directional structure
  -2  contrarian-scanner flags as overcrowded long
  -1  risk-monitor flags in correlation cluster
  -3  market_regime conflicts with the trade direction
```

### 6. Watchlist write-back

Take the top 5 tickers by conviction score (descending) and persist them so tomorrow's `risk-monitor` automatically tracks today's calls:

```
mcp__uw-watchlist__manage_watchlist(
  action="add",
  group="conviction_<YYYY-MM-DD>",
  tickers=[<top_5_by_score>]
)
```

This closes the feedback loop: today's high-conviction names become tomorrow's correlation universe.

### 7. Save and report

Write the final report to `analyses/YYYY-MM-DD.md` using the Write tool. Confirm the file was saved and print the **Executive Summary** section to chat.
