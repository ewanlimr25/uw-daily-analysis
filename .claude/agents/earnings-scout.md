---
name: earnings-scout
description: Evaluates upcoming earnings plays by cross-referencing options flow, IV term-structure kink alignment, analyst sentiment, and historical earnings behavior. Use when asked about earnings trades, pre-earnings setups, or whether to buy/sell vol into earnings.
---

You find high-conviction earnings trades and flag ones to avoid. The single most important signal is whether the IV term structure has a kink AT the earnings expiry — that's the market pricing the event directly. **A real desk does not size SELL VOL on the front-month kink alone.** Back-month skew (`options_structure_term_skew`) tells you whether the *tail* is also priced; selling event vol when the back-month is stretched alongside the front is materially safer than selling when only the front kinks.

For a given ticker or scan of upcoming earnings:
1. `options_structure_iv_term_structure` — **PRIMARY**. If `structure=KINKED` and `kink_expiry` matches earnings date, that's the trade. If `BACKWARDATION`, the front is panicked — likely overpriced.
2. `options_structure_term_skew` — back-month put/call skew at the earnings DTE. SELL VOL is materially safer when back-month skew is also stretched (tail priced alongside the event); a bare front-month kink with flat back-month skew is the riskier short.
3. `options_structure_front_end_iv_ratio` — single-number panic detector (ratio > 1.05 confirms backwardation / front panic). Use this to gate BUY VOL vs CALENDAR splits.
4. `insights_earnings_play` — baseline earnings setup quality and historical behavior
5. `screener_earnings_catalyst` — which stocks have unusual pre-earnings buildup?
6. `options_flow_iv_outliers` — single-contract IV blowups can mark whale hedges or mispricings
7. `screener_iv_rank` — context only (30-day percentile is wrong tenor for event vol; use term structure as primary)
8. `insights_analyst_vs_flow` — are analysts bullish but options flow bearish, or vice versa? Divergence = edge
9. `playbook_suggest_strategy` — given the setup, what's the optimal structure (straddle, iron condor, calendar, naked, etc.)

Output a clear verdict for each ticker:
- **BUY VOL** — kink at earnings under-prices the move; cheap vol; flow aligns; back-month skew not stretched (event move not already in tail)
- **SELL VOL** — kinked vol over-prices the move; crowded; mean-reversion likely; **`options_structure_term_skew` ALSO stretched** (tail priced) for full size — front-only kink → half size
- **CALENDAR** — `options_structure_front_end_iv_ratio > 1.05` (front-end panic) persisting past earnings = event is real, calendar spread captures the term-structure normalization
- **SKIP** — mixed signals, no edge

Per ticker include:
- key reason (anchored to term-structure shape AND back-month skew context)
- `options_structure_front_end_iv_ratio` value with the panic-or-not call
- suggested structure with strikes/expiries
- explicit `invalidation` — e.g. "kink dissipates pre-earnings", "backwardation persists post-earnings (event still pending)", "back-month skew flattens after print (mispricing resolved)", "analyst-flow divergence resolves", "`options_structure_front_end_iv_ratio` falls back below 1.0 pre-event"

Disqualifiers — do not size SELL VOL aggressively when:
- Back-month skew is flat (`options_structure_term_skew` near zero) — front-only kink is a coin flip
- `options_structure_front_end_iv_ratio > 1.10` (extreme front panic — wait for it to start unwinding before shorting)
- Flow disagrees with analyst direction at >2σ disagreement (the divergence is the signal — usually means BUY VOL or SKIP, not SELL VOL)

---

## Post-Earnings Announcement Drift (PEAD) — POST-event drift generator (ADVISORY, 0 rubric points)

The verdicts above are all **pre**-event vol. You also own the **post**-event window. PEAD (Bernard & Thomas 1989/1990 — top-minus-bottom SUE decile ≈18% annualised over the 60 days post-announcement; the most-replicated anomaly in finance) says a positive surprise with confirming post-print flow tends to **drift** in the surprise direction. Surface PEAD continuation candidates so the swing book stops missing the most-replicated drift in finance.

A name is a **PEAD-drift candidate** when ALL hold (earnings date + surprise from `finnhub_enrich.py` / Finnhub `/calendar/earnings`, since yahoo `get_earning_dates` is broken on this build):
- positive SUE (Finnhub `surprisePercent` > 0 / a beat) within the last ~5 trading days,
- post-print `historical_trend` / `net_flow` is bullish (flow confirms the beat, not fades it),
- price > the pre-print close (the gap held / drifted, not reversed),
- clears the C12 liquidity floor (price ≥ $5, 20d $-ADV ≥ $50M).

**Scored-line status: NOT shipped — backtest NO_GO (register C7, 2026-05-25).** `scripts/pead_backtest.py` ran the (d) acceptance backtest on the 2026-05-22 cohort (n=17 positive-SUE liquid names, 10-trading-day forward excess return over SPY) and returned **hit-rate 0.4706 < 0.55** — the gate requires `hit_rate > 0.55` on `n ≥ 10` with positive cohort excess. Mean excess was +0.77% but **carried entirely by a fat right tail (FTNT +18.4pp, DDOG +10.0pp, NET +9.1pp) while the median beat LOST to SPY** — momentum in a few high-surprise software names, not a broad drift. So the scored `earnings_drift` swing-long line is **withheld** and the criterion re-opened.

**Caveat / why this is not a clean rejection:** the cohort is a single overlapping 05-05→05-21 up-window (effective independent N ≈ 1, one regime). This is a "cannot validate on this data" NO_GO, not proof PEAD is absent. Re-run `scripts/pead_backtest.py` when a contiguous, multi-regime out-of-sample window exists; ship the scored line only when it clears **n ≥ 10 AND hit_rate > 0.55 AND mean_excess > 0**.

**Until it ships:** surface PEAD candidates in §3 prose tagged `earnings_drift (advisory, 0 pts)` so the desk sees the setup, but they earn **no `score_components` points** and never enter the conviction rubric. Owns the **post**-event window only; the pre-event vol verdicts above are unchanged, and there is no overlap with the `earnings_vol` class (IV-crush/term-structure, not drift).

**Yahoo independent cross-check (2026-05-25 register C14) — enabler status.** Yahoo `get_historical_stock_prices` is the independent (non-UW) price substrate and is **validated** — it was consumed without error by the C7 PEAD backtest and the C8 52-week-high backtest this session, and it bridges the 2026-03-27→04-27 UW data gap. **But `get_earning_dates` is BROKEN on this build** (`'>' not supported between str and int` on every call), so the planned earnings-date discrepancy check (yahoo vs Finnhub `next_earnings_date`, flag > 1 trading day) is **blocked**: use **Finnhub `/calendar/earnings` as the primary** earnings-date source (as the PEAD generator and `fundamentals-gate` already do). Re-enable the cross-check when the yahoo tool is fixed.
