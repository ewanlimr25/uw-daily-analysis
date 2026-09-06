# Phase 2 — Outcome Resolution (2026-05-30 run · C20 + C21 + C22 + C33)

**This is the phase the 2026-05-30 skill update rewrote.** The 2026-05-29 run resolved
**close-to-close** off a degenerate price cache (open=high=low=close). This run resolves
on **real daily OHLC** pulled from the Yahoo chart API the yfinance MCP wraps.

## Method — and the tool-spec bug it exposed (read first)

- **C20 daily-bar path-aware resolution.** R = **0.5 × true-range ATR(14)** (TR = max(H−L,
  |H−prevC|, |L−prevC|) over the 14 bars before entry). Each call is walked **bar-by-bar**
  over its horizon window; a long is a **LOSS** the first day `low ≤ entry−R` *before* any
  day `high ≥ entry+R` (symmetric for shorts); MAE is read off the **daily extreme**, not the
  close. Same-bar both-touch → LOSS (conservative; the stop would have pulled you). This
  recovers ~80 % of the true intraday path rule (only intraday-tick ordering is lost).
- **⚠️ Tool-spec bug found (material — feeds Phase 7).** The C20 spec says
  `mcp__yahoo-finance__get_historical_stock_prices` "returns open/high/low/close per day
  (verified)." **It does not** — all three yahoo-finance MCP endpoints return **close-only**
  in this environment (a flat `{date: close}` map; verified 2026-05-30). The real OHLC lives
  in the **chart API the MCP wraps** (`query1.finance.yahoo.com/v8/finance/chart`), reachable
  directly via stdlib `urllib`; its closes match the MCP exactly (NVDA 05-28 C=214.25,
  05-29 C=211.14 ✓). So the 2026-05-29 run's "both yfinance endpoints are close-only" claim
  was **right about the MCP**; the meta-audit's correction was right about the **underlying
  API**. The skill text must name the chart API, not the MCP tool. *(Pulled via
  `fetch_ohlc.py`; 172/173 tickers + SPY OK — only ^VIX failed, an index, never a price row.)*
- **C21 benchmark-excess input.** For every directional row, `spy_benchmark_win` = did a
  **same-direction SPY** bet entered the same day clear +1R_SPY (path-aware, SPY's own ATR)
  over the **same window**. This is the per-row input to the Phase-3 edge column.
- **C22 de-look-ahead.** `uw historical signal-backtest` has **no `--date`** → it is **not**
  quoted as a point-in-time "should-have-been" rate (the 05-29 run's contamination). It is
  carried only as `general_class_behaviour` colour in Phase 3.
- **C33 LEAP discipline.** A 0.5×ATR first-trigger fires in the first ~2 days — that tests a
  2-day move, not a 30/90D thesis. **No LEAP is scored WIN/LOSS**; all carry
  `window_open_mtm` and resolve INCONCLUSIVE (`leap_window_open`). None can have 30 forward
  trading days by the 05-29 last bar anyway.

## Win threshold (verbatim)
> ≥ +1R move in thesis direction within the window **without** −1R drawdown first.
Multi-window horizons resolve on a single first-trigger walk over the **primary** window
(swing/weekly → 10D, 0DTE → next session, LEAP → window_open). `window_open` = the N bars
aren't all available yet; never a truncated WIN/LOSS.

## Headline results (365 decided = WIN 183 / LOSS 182)

| Bucket | Decided | Win-rate | 2026-05-29 (close-only) | Δ |
|---|---|---|---|---|
| **All trades** | **365** | **50.1 %** | 47.3 % (n=328) | +2.8pp, +37 decided |
| Directional long | 176 | **58.0 %** | 50.0 % | **+8.0pp** |
| Directional short | 63 | **39.7 %** | 53.8 % | **−14.1pp** |
| vol_long (RV proxy) | 57 | 84.2 % | 53.1 % | proxy artifact |
| vol_short (RV proxy) | 69 | **11.6 %** | 30.9 % | proxy artifact |
| 0DTE (next session) | 17 | 64.7 % | 39.3 % | +25pp |
| opex pin (stay-within 5D) | 10 | 10.0 % | — | — |
| LEAP | 0 | n/a (all window_open, C33) | n/a | — |

**The path-aware walk decides 37 more calls** than close-only — intraday stops/targets that a
close-to-close test never saw now trigger. Two directional moves flip the narrative vs 05-29:
longs rise (uptrend targets get tagged intraday) and **shorts fall** (short stops get run on
up-wicks the close-only test missed).

## ⭐ The C21 benchmark-excess finding (the number the 05-29 run could not see)

| Direction | BOOK win-rate | SPY same-window same-dir base rate | **Excess (edge)** |
|---|---|---|---|
| **Long** | 58.0 % (n=176) | **80.2 %** (n=202) | **−22.2pp** ❌ |
| **Short** | 39.7 % (n=63) | 20.0 % (n=65) | **+19.7pp** ✅ |

**This reframes the entire book.** In this UPTREND tape a naive same-day SPY long cleared +1R
**80 %** of the time — the book's hand-picked single-name longs cleared it only **58 %**. The
longs are **−22pp of negative edge**: stock-selection on the long side **destroyed value vs
just buying the index**. The shorts, despite a low 39.7 % absolute hit-rate, **beat the
SPY-short base rate by +20pp** — they are the desk's only real directional alpha. The 05-29
run concluded "shorts beat longs, the book makes money on asymmetry"; the benchmark lens
says the truth is narrower and sharper: **short *selection* is the alpha; long *selection* is
beta you overpaid for.**

*Caveat (stated, not buried):* SPY is a low-vol index, so 0.5×ATR_SPY is an easy target in a
trend, while single names carry 2-sided idiosyncratic noise that trips their own ±R. Part of
the −22pp is structural (index drift vs single-name variance). But that **is** the benchmark a
desk is measured against — "could you have just bought SPY?" — and on longs the answer is no.

## Resolution accounting
- **NOT_A_TRADE 85** (watch_only / leap_disqualified / DROP / skip) — kept for Phase 6, excluded from all win-rate denominators.
- **INCONCLUSIVE 66** — 16 LEAP `leap_window_open` (C33) + recent swing/weekly `window_open` + 6 `data_unavailable` (incl. ^VIX rows) + a few `no_threshold`.
- **WIN 183 / LOSS 182.**

## Desk read
1. **The longs are the problem, not the shorts.** −22pp excess on longs is the single most
   important number in this audit. A book whose longs underperform SPY by 22pp in the exact
   regime that favours longs has a **long-selection** defect, not a sizing defect.
2. **Short selection is genuine alpha (+20pp excess).** `bearish_flow` humility (low claimed
   WR) plus real benchmark-beating performance = the one directional engine to lean on.
3. **vol_long 84 % / vol_short 12 % is a proxy artifact — do NOT read as calibration.** With
   true ranges, in-window daily range exceeded the pre-entry baseline almost everywhere
   (late-May range expansion), so the RV-direction proxy is near-deterministic. It measures
   "did range expand," not "did the vol thesis pay." Tagged `rv_direction_proxy`; Phase 3
   reports vol **separately** and never as IV-vs-RV calibration.
4. **pin 10 % (1/10)** and **0DTE 64.7 %** are small-N; pins breached ±R within 5D far more
   than they held.

## Outputs
- `phase_2_outcomes.jsonl` — 516 rows: Phase-1 row + `outcome`, `inconclusive_reason`,
  `realised_return_pct`, `max_adverse_excursion_pct` (daily extreme), `R_pct`, `entry_px`,
  `spy_benchmark_win` (C21), `window_open_mtm` (LEAP, C33), `realized_pnl_pct` (C3),
  `resolution_mode`, `vol_resolution`.
- `phase2_resolve_v2.py`, `fetch_ohlc.py`, `_ohlc/` (real-OHLC cache).
