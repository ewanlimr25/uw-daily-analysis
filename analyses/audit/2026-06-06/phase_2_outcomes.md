# Phase 2 — Outcome Resolution (2026-06-06 run · C20/C21/C22/C33 method)

Method identical to the 2026-05-30 run (`phase2_resolve.py`, adapted only for the new
window and W23): **C20** daily-bar path-aware walk on real OHLC from the Yahoo chart API
(186-ticker universe; 185 + `^VIX`-aliased VIX = **186/186 fetched**, zero `data_unavailable`
price gaps this run); **C21** per-row same-direction SPY benchmark; **C22** no
`signal-backtest` look-ahead; **C33** LEAPs never scored (earliest entry 04-30 has 25 forward
bars < 30 — all `leap_window_open`).

**Tape context this run adds:** Friday **2026-06-05 was a risk-off break** — SPY 752.3 open →
737.6 close (−2.0%), VIX 15.9 → 21.5. Every May call's window now includes a genuine
drawdown test the 05-30 audit never saw.

## Win threshold (verbatim)
> ≥ +1R move in thesis direction within the window **without** −1R drawdown first;
> R = 0.5 × true-range ATR(14) at entry. Same-bar both-touch → LOSS (conservative).
> `window_open` = forward bars not yet available; never scored.

## Headline (432 decided = WIN 207 / LOSS 225, WR 47.9%)

| Bucket | Decided | WR | 2026-05-30 run | Δ |
|---|---|---|---|---|
| **All trades** | **432** | **47.9%** | 50.1% (n=365) | −2.2pp, +67 decided |
| Directional long | 213 | 54.9% | 58.0% | −3.1pp |
| Directional short | 80 | 36.2% | 39.7% | −3.5pp |
| vol_long (RV proxy) | 65 | 81.5% | 84.2% | proxy artifact (unchanged read) |
| vol_short (RV proxy) | 74 | 10.8% | 11.6% | proxy artifact (unchanged read) |
| 0DTE (next session) | 17 | 64.7% | 64.7% | flat |
| opex pin (stay-within 5D) | 10 | 10.0% | 10.0% | flat |
| LEAP | 0 | all window_open (C33) | same | — |

Tiers: HIGH 51.9% (n=54) > MEDIUM 49.1% (n=169) > LOW 47.3% (n=131) — monotone but the
whole ladder spans **4.6pp**; effectively flat.

## ⭐ C21 benchmark-excess — the 06-05 selloff repriced the edge ledger

| Direction | BOOK WR | SPY same-window base | **Excess** | 05-30 excess |
|---|---|---|---|---|
| **Long** | 54.9% (n=213) | 72.2% (n=230) | **−17.2pp** ❌ | −22.2pp |
| **Short** | 36.2% (n=80) | 30.3% (n=76) | **+6.0pp** ✅ | +19.7pp |

1. **Long-selection is still negative edge** (−17pp). The selloff trimmed the SPY-long base
   rate (80.2 → 72.2%) more than it hurt book longs, but the verdict is unchanged: in this
   tape you'd rather have bought the index than the book's long picks.
2. **Short alpha compressed hard: +19.7pp → +6.0pp.** The one-day vol spike lifted the
   SPY-short base rate (20.0 → 30.3%) while book shorts *fell* to 36.2%. The 05-30 read
   ("short selection is the desk's only directional alpha") survives, but at a third of the
   claimed magnitude — short alpha was partly *regime timing*, and one risk-off Friday
   arbitraged a big slice of it away.
3. **June-cohort reality check:** the 69 new calls (06-01…06-05 + W23) are 9/24 decided =
   **37.5% WR** with 14 still open — the fleet walked into the 06-05 break long-tilted.

## Resolution accounting
- **NOT_A_TRADE 116** (watch_only / leap_disqualified / DROP / skip) — Phase 6 input only.
- **INCONCLUSIVE 37** = 16 `leap_window_open` (C33) + 17 `window_open` (June entries) +
  4 `no_threshold` (0DTE single-session, neither ±R touched). **Zero `data_unavailable`** —
  first run with full price coverage (VIX aliased via `^VIX`).
- Ambiguous both-touch bars: 0. Mean MAE on decided directional: 3.65% (median 2.70%).

## Desk read
1. The long book's negative excess is now confirmed **across two regimes** (melt-up and
   risk-off Friday) — it is selection, not a single-regime artifact.
2. Short alpha is real but **regime-sensitive**; +6pp residual after one bad Friday says size
   it as a hedge sleeve, not a profit center.
3. vol_long/vol_short RV-proxy splits (81/11) remain **resolution artifacts** — range expanded
   into June, mechanically failing every short-vol call. Phase 3 keeps vol out of calibration.
4. opex_pin 1/10: pins breach ±R within 5 days in this tape; the stay-within structure
   thesis is not surviving contact.

## Outputs
- `phase_2_outcomes.jsonl` — 585 rows with `outcome`, `realised_return_pct`,
  `max_adverse_excursion_pct`, `R_pct`, `spy_benchmark_win`, `window_open_mtm`,
  `realized_pnl_pct`, `resolution_mode`, `entry_date_used`.
- `phase2_resolve.py`, `fetch_ohlc.py`, `_ohlc/` (real-OHLC cache, 186 symbols).
