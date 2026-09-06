# Phase 2 — Outcome Resolution · 2026-06-20

**Resolution method (C20).** Real daily OHLC from the Yahoo chart API (stdlib `urllib`; the `mcp__yahoo-finance__*` tools are close-only and cannot evaluate the path rule). `R = 0.5 × true-range-ATR(14)` at entry; bar-by-bar walk; first daily extreme to breach `entry−R` (long) / `entry+R` (short) before the opposite is the trigger. Same-bar both-touch resolves conservatively to LOSS. MAE from daily extremes. Entry = `report_date` close (weekly envelopes carry the Friday date directly).

**Win threshold (verbatim).** ≥ +1R move in thesis direction within window **without** −1R drawdown first, R = the structure-implied risk or 0.5×ATR(14) default. Path-aware: a +2% gain after a −1.5% drawdown is a LOSS.

**INCONCLUSIVE (verbatim).** Window not yet closed (`window_open`), no threshold touched on a *complete* window (`no_threshold`), or price unavailable (`data_unavailable`). **Excluded from all win-rate denominators.** LEAP never scored until window closes.

**Coverage.** 201 rows → **160 decided** (71 WIN / 89 LOSS), 36 INCONCLUSIVE (34 `window_open` — the frozen-era recency, 1 `no_threshold`, 1 `leap_window_open`), 5 NOT_A_TRADE (directionless neutral). Paper outcomes resolved for *all* directional rows incl. `watch_only`/`DROP` (Phase 3 needs benched-name outcomes); `was_sized` separates the 24 actually-sized decided calls.

## Headline outcome tables

### Tier reliability — **INVERTED** (the desk-quitting signal)
| Tier | WIN/decided | Realised WR |
|---|---|---|
| **HIGH** | 1/7 | **14%** ← worst |
| MEDIUM | 10/19 | 53% |
| LOW | 28/62 | 45% |
| DROP | 32/72 | 44% |

HIGH < MEDIUM < … is violated at the top: the tier the rubric is **most** confident in is the **worst** realised performer. This is the *second consecutive audit* with HIGH-tier inversion (2026-06-12 logged HIGH 0.222 vs claimed 0.774; this run 0.143). N=7 is thin — but a repeated inversion across two independent windows is no longer noise; it is the empirical basis for the rubric freeze. Carried to Phase 3 for BH/reliability formalization.

### Directional edge vs SPY (C21) — longs beat the tape, shorts destroy value
| Arm | Book WR | SPY same-window base | **Excess** |
|---|---|---|---|
| long (n=79 / SPY n=87) | 51.9% | 36.8% | **+15.1pp** |
| short (n=51 / SPY n=55) | 37.3% | 60.0% | **−22.7pp** |

- **Long edge is real but DECAYING across eras** — `era_0525_0529` long 67% → `era_0530_0605` 46% → `pre_freeze_post_0606` 38%. The blended +15pp is front-loaded in the earliest 5-day window and is single-regime; it is **not** demonstrated as durable. Treat as "rode an up-leg," not "structural alpha," until it survives a down/transitional window.
- **Short edge is consistently negative** across every era (31% / 38% / 40%) against a 60% SPY-short base. The single-name short *selection* subtracts ~23pp vs simply shorting the index — the most expensive structural problem in the book. (Edge-before-calibration: this is a worse problem than any miscalibrated win-rate quote.)

### Signal class — claimed vs realised (decided ≥5; claim side substrate-contaminated)
| Canonical class | Realised | Claimed | Δ | Note |
|---|---|---|---|---|
| bullish_flow | 56% (14/25) | 59% | −3 | well calibrated |
| bearish_flow | 47% (16/34) | 42% | +5 | under-claimed |
| dark_pool_accumulation | 48% (13/27) | 56% | −8 | modest over |
| dealer_positioning* | 47% (7/15) | 60% | −13 | over (*5 labels merged) |
| **earnings_vol** | 38% (8/21) | **86%** | **−48** | RV-proxy; absurd claim |
| **high_iv_rank** | 38% (3/8) | **84%** | **−46** | RV-proxy; absurd claim |
| multileg_directional | 17% (2/12) | 55% | −38 | worst directional class |
| multi_day_sweep | 83% (5/6) | 38% | +45 | under-claimed, n=6 |
| gamma_breakout | 20% (1/5) | 51% | −31 | n=5 thin |

### Horizon / vol
- swing 47% (60/129); **vol 35% (11/31)**. Within vol: **vol_long 100% (10/10)** vs **vol_short 5.6% (1/18)** — but resolved on the **RV-direction proxy** (in-window mean daily range vs 14-bar baseline), **not** true IV-vs-RV (legacy envelopes lack `implied_move`). The vol_short wipeout = "RV expanded post-entry" in a rising-range tape; it is **not** a calibrated short-vol P&L and must not be read as one. Heavy caveat into Phase 3.

### Expectancy (paper, 0.5-ATR barrier)
WIN mean **+9.23%** (n=71) · LOSS mean **−12.73%** (n=89) → payoff ratio **0.73**, blended hit 44% → **negative paper expectancy ≈ −3.0%/trade**. Losers sit on higher-ATR names than winners (the conviction names are the volatile ones). The honest edge read remains the SPY-excess column, which controls for the barrier.

### Sized book vs benched (advisory, n=24 decided — below effectiveness floor)
SIZED 37.5% (9/24) **< PAPER/benched 45.6%** (62/136). The names the system *sized* underperformed the names it *benched* — sizing is, on this thin sample, **anti-selective**. Driven by vol_short 0/6 (RV-proxy) + short 1/5; vol_long 4/4 and long 4/9 are the only positives. n=24 is below the N≥10-per-arm gate-effectiveness floor — **advisory only**, formalized in Phase 6.

## Outputs
- `phase_2_outcomes.jsonl` — 201 rows extended with `outcome`, `realised_return_pct`, `max_adverse_excursion_pct`, `inconclusive_reason`, `spy_benchmark_win`, `canonical_class`, `was_sized`, `realized_pnl_pct`, `fast_trigger`.
- General-class `signal-backtest` behaviour deliberately **not** pulled as a point-in-time benchmark (C22: no `--date`; look-ahead). SPY same-window base rate is the honest benchmark and is computed above.
