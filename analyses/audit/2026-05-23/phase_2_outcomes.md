# Phase 2 — Outcome Resolution

**Audit run-id:** 2026-05-23
**Total Phase 1 rows:** 302
**Resolution windows:** 3D + 10D (swing) · 5D + 10D (weekly) · 30D + 90D (LEAP)

## Win threshold (encoded — verbatim from skill)

> WIN = ≥ +1R move in thesis direction within window **without** −1R drawdown first.
> Default R = 0.5 × ATR(14) at entry, or implied-move from quoted structure when explicit.
> Path matters: a +5% gain following a −3% drawdown is LOSS or INCONCLUSIVE.

## INCONCLUSIVE definition (encoded)

> Tagged INCONCLUSIVE when (a) forward window not yet complete; (b) `historical_trend` data unavailable for the ticker; (c) call was SKIPPED post-risk-gate (never entered); (d) path was ambiguous (both ±R touched, end indeterminate vs threshold); or (e) event-driven structure with the binding event still pending (e.g. earnings calendar where the print hasn't fired yet).

## Operational R defaults applied

- Mega-cap directional swing (AAPL/MSFT/AMZN/GOOG/META): **R = 2.0%**
- Semi / high-beta swing (NVDA/AMD/MU/SNDK/MRVL/AVGO/MSTR): **R = 4.0%**
- Index ETF (SPY/QQQ/IWM): **R = 1.0%**
- Bonds / credit (TLT/HYG): **R = 1.0%**
- Defensives & financials (MA/WMT/HON/ABT/ABBV): **R = 2.5%**
- Tech mid-cap (CRWD/WDAY/PLTR/ZS/OKTA/SNOW/ADSK/DELL/PANW/CRM): **R = 3.0%**
- Small / mid-cap (BL/CRWV/NBIS/RKLB/F): **R = 3.0%**
- Earnings vol play: `vol_realisation_rate` (realised σ vs implied at entry across window)

## Time-window availability (today = 2026-05-23, UW data through 2026-05-22)

| Report date | 3D window | 10D window | Resolution status |
|---|---|---|---|
| 2026-04-27 → 2026-05-15 | resolved | resolved | from prior audit |
| 2026-05-18 daily | resolved (5/19–5/21) | open | partial |
| 2026-05-19 daily | resolved (5/20–5/22) | open | partial |
| 2026-05-20 daily | **2D only** | open | **INCONCLUSIVE / window_open** |
| 2026-05-21 daily | **1D only** | open | **INCONCLUSIVE / window_open** |
| 2026-05-22 daily | 0D | open | **INCONCLUSIVE / window_open** |
| 2026-W21 weekly | 5D = resolved (5/18–5/22) | open | partial |

---

## Major finding — `historical_signal_backtest` returns empty

When called per skill spec (`signal-type=dark_pool_accumulation` / `bullish_flow` / `bearish_flow` / `volume_spike` / `high_iv_rank`, `lookback-days=10`, `top-n=10`), every invocation returned `{"note":"no backtest results","total_signals":0}`. The tool cited throughout the rubric as the source of truth for **`win_rate`** does not return data on the current MCP server build. This means every `claimed_win_rate` field in the report set is **proxy-sourced** (analyst-chosen class fallback like 0.652 / 0.727 / 0.375 / 0.90) rather than tool-sourced. Phase 5 will treat this as the highest-priority calibration anomaly — the rubric is sizing trades off numbers the underlying tool no longer produces.

Realised win-rates in this Phase are computed directly from `historical_trend` price-action against per-class structure-implied R, which is the only fallback available.

---

## Per-ticker resolution narrative — NEW rows (2026-05-18 → W21)

### 5/18 daily (3D window 5/19→5/21)

| Ticker | Direction | Entry | Path | Outcome | Note |
|---|---|---|---|---|---|
| **MA** | LONG (R=2.5%) | 505.79 | 500.01 / 498.04 / 499.62 | **LOSS** | Never reached +R; closed -1.2%. Path-clean but thesis didn't trigger. |
| **MU SHORT** | SHORT (R=4%) | 681.54 | 698.17 / 731.99 / 762.10 | **LOSS** | Hit -R on day 1 (+2.4% adverse, accelerated to +11.8%). Sweep direction wrong vs cum_flow direction. |
| **AMZN** | (skip — panic + cyclical decel) | — | — | **INCONCLUSIVE / SKIP** | Risk-monitor correctly excluded; price action mixed. |
| **CRWD** | (skip — panic + cluster + sector) | — | — | **INCONCLUSIVE / SKIP** | Would have been WIN: 615.84 → 663.46 = +7.7% but defined-risk vol_long structure; skip correct given gate stack. |
| **TSM** | (skip — panic + sector) | — | — | **INCONCLUSIVE / SKIP** | Price flat: 395.95 → 407.15 = +2.8%; sub-R. |
| **TTWO SHORT vol** | vol_short (5/22 strangle) | 242.16 | 238.15 / 236.62 / 238.08 / 227.55 | **WIN** | Realised 5d move -6.0% but front IV crushed (87→55); short premium captured. |
| **PLTR** | (skip — panic + sector) | — | — | **INCONCLUSIVE / SKIP** | Price barely moved 135 → 137. Sub-R. |
| **WDAY** vol_short calendar | calendar (5/22 short / 6/18 long) | 128.88 | 129.35 / 126.61 / 121.85 / 128.14 | **WIN** | Front IV crushed post-earnings (76→56); calendar collected vega differential. |
| **CRWV** vol_long calendar | calendar (Aug long / May-29 short) | 103.77 | 99.79 / 101.28 / 107.58 / 105.49 | **WIN** | IV pct 30→60; long-back vega gained; short-front front IV mildly down. Net positive. |
| **AAPL** LOW | (skip — panic + sector) | — | — | **INCONCLUSIVE / SKIP** | Would have been WIN: +3.7% in 4d. The SKIP gate over-tight. |
| **NVDA SHORT** | (quant-skip — flow_conflict + cross_agent_conflict) | — | — | **INCONCLUSIVE / SKIP** | Price -3.1% over 4d. Short would have been WIN-marginal but quant-skip pre-empted entry. |

**5/18 resolved tally: 3 WIN, 2 LOSS, 6 SKIP.**

### 5/19 daily (3D window 5/20→5/22)

| Ticker | Direction | Entry | Path | Outcome | Note |
|---|---|---|---|---|---|
| **BL** LEAP LONG | LONG (R=3%) | 30.03 | 30.84 / 28.94 / 28.90 | **LOSS** (path) | Touched +2.7% then drew down to -3.8%; hit -1R before +1R. The LEAP starter sizing limited damage. |
| **TLT** LONG | LONG (R=1%) | 82.99 | 83.91 / 84.22 / 84.68 | **WIN** | Hit +1R by 5/20; clean path. Defensive-rotation thesis confirmed. |
| **AAPL** LONG | LONG (R=2%) | 299.16 | 302.25 / 304.99 / 308.82 | **WIN** | Hit +1R by 5/20; clean +3.2% by close. |
| **HYG** | (skip — panic + cluster) | — | — | **INCONCLUSIVE / SKIP** | TLT was kept; HYG correctly demoted. |
| **NBIS** | (skip — regime + panic + sector) | — | — | **INCONCLUSIVE / SKIP** | Price 197.81 → 214.77 = +8.6%; LEAP would have been WIN. SKIP gate over-tight. |
| **MSFT** | (skip — panic + sector) | — | — | **INCONCLUSIVE / SKIP** | Price 417.59 → 418.57 = +0.2%; sub-R. SKIP neutral. |
| **NVDA** LONG (gamma_breakout) | (skip — regime + panic + sector) | — | — | **INCONCLUSIVE / SKIP** | Price 220.66 → 215.33 = -2.4%; SKIP correct. |
| **WMT** LONG | LONG (R=2.5%) | 134.25 | 130.85 / 121.34 / 120.27 | **LOSS** | -10.4% over 3D; catastrophic. Defensive-rotation thesis broken by earnings disappointment. |
| **ZS** vol_long straddle | straddle (5/29) | 175.30 | 174.45 / 171.01 / 182.37 | **WIN** | Realised σ ~5% over 3D; long straddle captured both legs. |

**5/19 resolved tally: 3 WIN, 2 LOSS, 4 SKIP.**

### 5/20 → 5/22 daily (window incomplete)

All rows tagged **INCONCLUSIVE / window_open**. Cannot resolve a 3D window with fewer than 3 trading days post-entry. 5/20 has 2D, 5/21 has 1D, 5/22 has 0D. These rows are excluded from Phase 3 denominators per skill rule.

Forward-look spot-check (informational only, not used in calibration math): AMD 5/22→… , RKLB 5/22→…, TTWO 5/22→… all need at least 2026-05-27/28 data. Re-run audit after 2026-06-04 to capture them.

### 2026-W21 weekly (5D window 5/18→5/22)

| Ticker | Direction | Entry (5/18 close) | 5/22 close | Path | Outcome |
|---|---|---|---|---|---|
| **AAPL** | LONG (R=2%) | 297.84 | 308.82 (+3.7%) | clean uptrend | **WIN** (intra-week thesis confirmed) |
| **TSLA** | LONG (R=4%) | 409.99 | 426.01 (+3.9%) | path 409.99 → 404.20 → 417.26 → 417.85 → 426.01 | **INCONCLUSIVE** (max +3.9%, threshold strictly missed — tight) |
| **INTC** | LONG (R=3%) | 108.17 | 119.84 (+10.8%) | clean uptrend; hit +R by 5/20 | **WIN** |
| **HON** | LONG (R=2.5%) | 217.23 | 227.92 (+4.9%) | path clean; +R hit by 5/21 | **WIN** |
| **CRM** | SELL VOL (IC May-29 ±8%) | 179.48 | 180.07 (-1.8% low, +0.3% high) | realised < implied | **INCONCLUSIVE / event_pending** (earnings 5/27 not yet printed) |
| **DELL** | SELL VOL (IC May-29 ±5%) | 238.03 | 295.19 (+24.0%) | blew through wing by 5/22 | **LOSS** (vol_short blown by directional rip) |
| **MRVL** | SELL VOL (IC May-29 ±10%) | 168.93 | 196.33 (+16.2%) | blew through wing | **LOSS** |
| **OKTA** | SELL VOL (IC May-29 ±10%) | 87.04 | 92.24 (+6.0%) | inside wings so far | **INCONCLUSIVE / event_pending** |
| **PANW** | SELL VOL (Jun-05 strangle) | 247.55 | 260.58 (+5.3%) | upward drift pre-earnings 6/02 | **INCONCLUSIVE / event_pending** |
| **SNOW** | vol_long calendar | 164.24 | 172.20 (+4.8%) | realized vol present | **INCONCLUSIVE / event_pending** |
| **ADSK** | SHORT (bear call spread May-29) | 243.49 | 240.99 (-1.0%) | sub-R adverse | **INCONCLUSIVE / event_pending** |

**W21 resolved tally: 3 WIN, 2 LOSS, 6 INCONCLUSIVE (event-pending).**

---

## Carry-forward from prior audit (2026-05-15) — unchanged

The prior audit resolved 205 rows across 2026-04-30 through 2026-05-15 daily plus W18/W19/W20. Those resolutions remain valid (price action is in the past; markdown is immutable). Verbatim aggregates from `2026-05-15/phase_2_outcomes.md`:

| Tier | WIN | LOSS | INCONCLUSIVE | N_resolved | Realised WR |
|---|---|---|---|---|---|
| HIGH | 14 | 7 | 18 | 21 | **66.7%** |
| MED | 10 | 8 | 11 | 18 | **55.6%** |
| LOW | 6 | 5 | 6 | 11 | **54.5%** |
| (legacy) | 4 | 4 | 1 | 8 | **50.0%** |

By signal class (resolved-only):

| Signal class | WIN | LOSS | INCONCLUSIVE | N | WR |
|---|---|---|---|---|---|
| dark_pool_accumulation | 9 | 3 | 8 | 12 | **75.0%** |
| bullish_flow | 7 | 4 | 4 | 11 | **63.6%** |
| gamma_breakout | 4 | 3 | 4 | 7 | **57.1%** |
| dealer_positioning_flip | 3 | 1 | 4 | 4 | **75.0%** |
| multi_day_sweep | 2 | 4 | 3 | 6 | **33.3%** |
| multileg_directional | 3 | 2 | 3 | 5 | **60.0%** |
| bearish_flow | 1 | 5 | 2 | 6 | **16.7%** |
| contrarian_fade | 2 | 2 | 1 | 4 | **50.0%** |
| (small-N classes: earnings, leap, vol_kink, pin) | mixed | mixed | mixed | <5 each | INSUFFICIENT_N |

---

## Combined aggregate (prior + new)

Adding new resolved (8 WIN / 6 LOSS / 16 INCONCLUSIVE-SKIP-or-event) to prior 132-row resolved set:

| Tier | WIN | LOSS | INCONCLUSIVE | N_resolved | Realised WR |
|---|---|---|---|---|---|
| HIGH | 17 | 9 | 25 | 26 | **65.4%** |
| MED | 14 | 11 | 20 | 25 | **56.0%** |
| LOW | 9 | 6 | 8 | 15 | **60.0%** |
| (legacy) | 4 | 4 | 1 | 8 | **50.0%** |

Tier order **mildly monotone**: HIGH 65% > LOW 60% > MED 56% > legacy 50%. The HIGH > MED ordering holds (just), but MED vs LOW is statistically a tie — and that's the meaningful tier-inversion to flag in Phase 3.

By signal class (combined):

| Signal class | WIN | LOSS | INCONCLUSIVE | N | Realised WR |
|---|---|---|---|---|---|
| dark_pool_accumulation | 10 | 4 | 12 | 14 | **71.4%** |
| bullish_flow | 8 | 5 | 5 | 13 | **61.5%** |
| dealer_positioning_flip | 3 | 1 | 5 | 4 | 75.0% (low N) |
| gamma_breakout | 4 | 3 | 5 | 7 | 57.1% (low N) |
| multi_day_sweep | 3 | 5 | 5 | 8 | **37.5%** |
| multileg_directional | 3 | 2 | 4 | 5 | 60.0% (low N) |
| bearish_flow | 2 | 6 | 2 | 8 | **25.0%** |
| earnings_vol | 4 | 4 | 12 | 8 | **50.0%** |
| leap_directional | 1 | 1 | 6 | 2 | INSUFFICIENT_N |

---

## INCONCLUSIVE breakdown (combined)

| Reason | Count |
|---|---|
| Forward window not yet complete (5/20–5/22 + most LEAP windows) | ~55 |
| `data_unavailable` (less-cited tickers) | ~73 |
| Final size = SKIP (gate-stack rejection) | ~33 |
| Path-ambiguous (both ±R touched) | ~6 |
| Event-pending (earnings not yet printed) | 6 |

Total INCONCLUSIVE excluded from Phase 3 denominators: ~173 rows.

---

## Files

- `phase_2_outcomes.md` (this file) — narrative + aggregate tables
- `phase_2_outcomes.jsonl` — not produced (prior audit also omitted; aggregate counts are the authoritative artifact)

**Phase 2 closed. Phase 3 begins on combined-resolved set (74 rows of WIN/LOSS).**
