# Daily Market Analysis

Run a full post-market intelligence report using all 5 specialist agents in parallel, then synthesize into an executive summary and detailed breakdown. Save output to `analyses/YYYY-MM-DD.md`.

## Steps

### 1. Get today's date
Use `date` to get the current date in YYYY-MM-DD format. This becomes the filename.

### 2. Run all 5 agents in parallel

Spawn these agents simultaneously — do NOT run them sequentially:

- **sweep-tracker**: Find today's most significant options sweeps and directional momentum plays
- **accumulation-hunter**: Identify tickers with quiet institutional accumulation signals
- **contrarian-scanner**: Surface overcrowded positions and high-conviction fade setups
- **earnings-scout**: Evaluate any upcoming earnings plays with unusual pre-event flow
- **risk-monitor**: Assess the current market regime, correlation risks, and adverse flow alerts

### 3. Synthesize into a report

Combine all agent outputs into a structured markdown report:

```
# Daily Market Analysis — YYYY-MM-DD

## Executive Summary (3-5 bullets)
- Regime: [trending/choppy/high-vol]
- Top sweep: [ticker, direction, why it matters]
- Institutional accumulation: [top 1-2 tickers]
- Biggest risk: [correlation cluster or adverse flow alert]
- Earnings watch: [any high-conviction plays]

## Market Regime
[From risk-monitor — sets the context for everything below]

## Smart Money Flow — Sweeps & Momentum
[From sweep-tracker — ranked list with thesis per ticker]

## Institutional Accumulation
[From accumulation-hunter — ranked list with signals]

## Contrarian / Fade Setups
[From contrarian-scanner — only high-conviction fades]

## Earnings Plays
[From earnings-scout — BUY VOL / SELL VOL / SKIP verdicts]

## Risk Alerts
[From risk-monitor — correlation clusters, adverse flow, sector rotation]

## Watchlist
[Any tickers appearing in 2+ sections = highest conviction, flag these]
```

### 4. Cross-reference for highest conviction

Before saving, scan all sections for tickers that appear in multiple agent outputs. A ticker flagged by 2+ agents = strong signal. Add these to the Watchlist section.

### 5. Save the report

Write the final report to `analyses/YYYY-MM-DD.md` using the Write tool.

Confirm the file was saved and print the executive summary to the chat.
