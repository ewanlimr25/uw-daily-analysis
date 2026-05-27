# Changelog

## 2026-05-26 — Report output layout: per-id run folders

- **Each report now gets its own folder with generically-named files.** Daily → `analyses/daily/<YYYY-MM-DD>/{report.md, decision.json}`; weekly → `analyses/weekly/<YYYY-WW>/{report.md, decision.json}` (previously flat `analyses/<date>.md` + `analyses/<date>.decision.json`). All historical reports (19 daily, 5 weekly + 3 envelopes) migrated retroactively; each envelope's `report_path` re-pointed at its sibling `report.md` and re-validated.
- **Updated:** `daily-analysis.md` (Step 9 + intro), `weekly-analysis.md` (Step 10 + anchors + mkdir), `calibration-audit.md` (Phase 1 inventory glob `analyses/daily/*/report.md` + sidecar discovery `analyses/daily/<date>/decision.json`), `CLAUDE.md`, `schemas/decision_envelope.schema.json` description, `scripts/README.md`, `scripts/validate_decision.py` docstring, and the validator test fixture. `Write(analyses/**)` permission already covers the new subfolders. 171 tests green; all three envelopes re-validate. Audit checkpoints (`analyses/audit/<date>/`) unchanged.

Improvement-criteria register implementation (`analyses/audit/2026-05-25/improvement_criteria.md`).
Each entry cites the academic basis + the measured backtest evidence. Gates that resolve
only on out-of-sample data are marked **forward (confirm at 05-30 audit)**.

## 2026-05-25 — P0 batch

- **C11 — conjunction scoring for the accumulation complex.** The `+3` accumulation rubric
  line (DP-block + OI + smart_positioning) now pays full +3 only when `cum_premium_flow_30d`
  confirms (sign-aligned with thesis AND |flow| ≥ $50M); otherwise halved (floored) to +1, in
  `signal-confluence-quant.md` + the daily/weekly embedded rubrics. Evidence: Bailey & López de
  Prado (non-independence of correlated signals inflates apparent edge); 2026-05-23 audit measured
  a tier inversion **HIGH 60.0% < MED 62.5% (n=49)** with the ≥0.80 win-rate appearing only on the
  DP-block ∧ cum_flow ∧ institutional-accum conjunction. Today-gate: halved/full arithmetic is
  schema-valid (Σ score_components.points == raw_score holds; 4 new tests green). Forward
  (confirm at 05-30 audit): HIGH-tier realised WR > MED-tier on the out-of-sample cohort.

- **C12 — liquidity floor on every screened candidate.** New stdlib `scripts/excess_winrate.py`
  (`apply_liquidity_floor`: price ≥ $5 AND 20-day dollar-ADV ≥ $50M, fail-closed) wired into Step 0
  of both commands and as a quant disqualifier. Evidence: Barbon & Buraschi (*Gamma Fragility*) —
  flow effects are strongest and least exitable in the least-liquid names. Today-gate: the live
  `volume_spike` probe returned 6 sub-$50M-ADV micro-ETFs (GIF/BLCN/PEX/IGLD/UTHY/ESGE, 22.2%
  realisation); the floor **excludes all 6 and keeps AMD/MU** (CLI-verified + 9 tests green).
  Forward (confirm at 05-30 audit): 0 sub-floor names in the next report's `calls[]`.

- **C2 — market-excess + tightened N-cap over the existing win-rate cap.** In
  `signal-confluence-quant.md`: the `n<10` cap tightened **0.75 → 0.69** (one notch below the
  0.70 full-size line) and a **downgrade-only market-excess gate** added (signal WR − same-direction
  SPY WR over the same windows; `excess ≤ 0` → cap half, `excess ≤ −0.10` → starter), preserving the
  raw-WR-calibrated ladder rather than rescaling it. `scripts/excess_winrate.py:size_decision` +
  daily/weekly Step-5 note. Evidence: Bollerslev-Tauchen-Zhou (returns are regime-conditional) +
  López de Prado (unconditional multiply-tested WR is inflated). Today-gate **MEASURED & PASS**: the
  live probe set re-run shows **no class full-sizes on a single up-week** — `bullish_flow`
  (n=8/100%, SPY-long benchmark ≈1.0) moves **full → half** (both the 0.69 cap and the +0.00 excess
  gate demote it); `bearish_flow` starter; `volume_spike` skip (floored); `high_iv_rank` half.
  Forward (confirm at 05-30 audit): Brier improves vs the 0.224 baseline.

- **P0 regression run (no live regression).** Fresh `/daily-analysis` (`analyses/2026-05-25.md` + `.decision.json`,
  4 calls, validates) and `/weekly-analysis` (`analyses/weekly/2026-W22.md` + `.decision.json`, 3 calls, validates)
  on the latest 05-22 data (Memorial Day same-data A/B). Pipeline ran end-to-end under the new rubric with no
  breakage; C1 envelope emission smoke-tested green both kinds. All three P0 changes visibly fired on live data:
  C11 conjunction paid FULL on AMD (cum_flow +$354M aligned) and HALVED F (+3→+1, flow <$50M); C12 excluded the
  micro-cap confluence names; **C2 market-excess demoted AMD full→half on both horizons (92.9% WR is up-tape beta,
  excess −0.07) — the headline catch.** Net book strictly more conservative (the crowded high-scorer gated out).
  Discovered (pre-existing, not P0): the sector-rotation `+1` `persistence_score ≥ 3` gate is unsatisfiable — the
  tool returns a 0–1 scale. Flagged for P1.

## 2026-05-25 — P1 batch

- **C7 — Post-Earnings Announcement Drift (PEAD) continuation.** Built `scripts/pead_backtest.py`
  (stdlib; trading-day forward window, SPY-contemporaneous excess, point-in-time exit guard) + 11
  tests, and a POST-event drift generator in `earnings-scout.md`. Evidence: Bernard & Thomas
  (1989/1990) — SUE-decile drift ≈18% annualised/60d. **(d) gate result: NO_GO.** Live backtest on
  the 2026-05-22 cohort (n=17 positive-SUE liquid names) measured **hit-rate 0.4706 < 0.55** (gate
  needs >0.55 on n≥10 + positive excess); mean excess +0.77% but carried entirely by a fat right
  tail (FTNT +18pp, DDOG +10pp, NET +9pp) while the median beat LOST to SPY. Cohort is a single
  overlapping 05-05→05-21 up-window (effective N≈1). Per "no gate, no merge," the scored
  `earnings_drift` line is **withheld**; the generator ships **advisory-only (0 rubric points)** and
  the criterion is **re-opened** pending a contiguous multi-regime out-of-sample window. Earnings
  dates sourced from Finnhub `/calendar/earnings` (yahoo `get_earning_dates` is broken on this build).

- **C4 — opening-confirmed flow (OI-confirmed-opening gate).** New `scripts/oi_opening.py`
  (`oi_opening_confirmed` + `opening_gate_size`) + 14 tests; wired into `signal-confluence-quant.md`
  (downgrade-only sizing gate on the `bullish_flow`/`bearish_flow` classes, parallel to C2's excess
  gate), `sweep-tracker.md` (per-name opening tag, the route back to scoring for P0.3-deprecated
  sweeps when OI-confirmed-opening AND accumulation/multileg co-flagged), and both command Step-5s.
  Evidence: Pan & Poteshman (2006, RFS 19:871) — the predictive option-volume signal is built only
  from buy-to-open volume; the edge disappears without isolating opening flow. Today-gate: aggregate
  gate is implemented + computable from `historical_oi_trend`/`oi_biggest_increases` (both already in
  the fleet; AMD's +81k BUILDING → opening-confirmed in the live run) + 14 tests green. Per-contract
  buy-to-open tool **N1 deliberately NOT built** — deferred until the aggregate shows lift. Forward
  (confirm at 05-30 audit): `bullish_flow`/`multi_day_sweep` realised WR closes ≥10pp of the
  claimed-vs-realised gap.

- **C3 — expectancy / fractional-Kelly sizing (ADVISORY-only until n≥30).** New `scripts/kelly_sizing.py`
  (`payoff_ratio`, `expectancy`, `full_kelly` f*=W−(1−W)/R, `capped_half_kelly` floored-0/capped-0.25,
  `tier_expectancy_monotone` live-activation gate) + 15 tests; 4 optional nullable call fields added to
  `decision_envelope.schema.json` (realized_pnl_pct / payoff_ratio / expectancy_pct / kelly_fraction,
  backward-compatible, schema_version stays 1.1) + a validator invariant (kelly_fraction ∈ [0,1]);
  `/calibration-audit` Phase 2 populates the fields from resolved outcomes and Phase 3 runs the
  activation gate; advisory-only notes in `signal-confluence-quant.md` + `risk-monitor.md`. Evidence:
  Kelly (1956) — f* needs W AND payoff R; half-Kelly ≈75% growth at ≈50% drawdown; 50–100 trades for
  stable estimates. **(d) gate: ADVISORY-ONLY** — the repo has 0 closed calls with realised P&L, so the
  win-rate ladder stays the live sizer; the half-Kelly sizer activates only when tier × expectancy is
  monotone on **n ≥ 30 closed calls** (the closed-loop record accrues from the C1 envelopes as runs
  resume). Infrastructure shipped; live activation deferred to the 05-30+ audits.

## 2026-05-25 — P2 batch

- **C1 — decision-envelope emission: VERIFIED (no code).** This session's regression run wrote
  schema-valid daily (`2026-05-25.decision.json`, 4 calls) + weekly (`2026-W22.decision.json`, 3 calls)
  envelopes with `macro_snapshot_signals` / `next_session_gex` / `next_session_0dte_setup` / per-call
  `win_rate`+`win_rate_n`+`win_rate_source` / `gate_verdicts` / `fundamentals_verdict` /
  `debate_residual_confidence` all populated and `validate_decision.py` exit 0 — C1's (d) smoke test. No fix needed.
- **C8 — 52-week-high proximity gate: backtest NO_GO → +1 WITHHELD.** Built `scripts/proximity_52w_backtest.py`
  + 9 tests. Live backtest (entry 2026-05-08, n=20): near-high (≥95%) WR 0.667 vs far-from-high (<80%) WR
  0.625 — **split 4.2pp < the 10pp gate** (near-high names didn't outperform; laggards mean-reverted up).
  Conditional +1 withheld + re-opened (George & Hwang 2004). Evidence-gated, kept out of the HIGH band (C11).
- **C5 + C9 — VRP-magnitude + term-slope scalers: ADVISORY.** New `scripts/vol_regime_scaler.py` (VRP/slope
  tercile → premium-selling size scalar + `tercile_winrate_monotone` activation gate) + 10 tests; advisory
  notes in `vol-surface-scout.md` + `risk-monitor.md`. Evidence: Bollerslev-Tauchen-Zhou (2009) VRP predicts
  returns; Johnson (2017) term-slope prices variance risk. The VRP *sign* sizing stays live; the *magnitude*
  scaler activates only when premium-selling WR is monotone across terciles on n≥30 accrued obs. **C5 subsumes
  the 05-23 P2.2 earnings_vol cap** (retire once LIVE).
- **C13 — mutually-exclusive signal-class routing: SHIPPED (structural).** Added the routing rule to
  `signal-confluence-quant.md` — each idea → exactly one `dominant_signal_class` with documented precedence
  (multileg > vol-structure; earnings-scout owns KINKED `earnings_vol`; contrarian acks sweep in prose, no
  double-deduction). Acceptance (0 double-counted `score_components` over a 5-report cohort) verified at audit.
  C6 registers through this router. Evidence: Bailey & López de Prado (correlated signals aren't additive).
- **C14 — yahoo cross-check enabler: price-substrate VALIDATED, earnings-date BLOCKED.** Yahoo
  `get_historical_stock_prices` was consumed without error by the C7 + C8 backtests (bridges the
  03-27→04-27 UW gap). `get_earning_dates` is broken on this build → Finnhub `/calendar/earnings` is the
  primary earnings-date source; the yahoo-vs-finnhub discrepancy check is deferred until the tool is fixed.
  Documented in `earnings-scout.md`.
- **C6 — lottery / expensive-skew fade: WITHHELD (regime-gated).** `−2` fade line withheld — the (d) gate
  needs a non-UPTREND regime (current is UPTREND) and top-decile underperformance at p<0.10, and
  `historical_pc_ratio_zscore` standalone backtested NEGATIVE (−22pp). `vol-surface-scout.md` may surface a
  `lottery_score` composite as advisory, routed through C13 (never stacked with `−2 overcrowded-long`).
  Evidence: Boyer & Vorkink (2014).
- **C10 — opportunistic-vs-routine insider weighting: classifier SHIPPED, signal ADVISORY.** New
  `scripts/insider_classify.py` (`is_routine` = same calendar month in ≥3 prior years; point-in-time
  `classify_transactions`; `opportunistic_signal`) + 7 tests; `fundamentals-gate.md` uses opportunistic-only
  MSPR when available. Evidence: Cohen-Malloy-Pomorski (2012) — opportunistic 82bps/mo, routine ≈0. Finnhub
  insider endpoints returned empty on this build (`/stock/insider-transactions` may be premium), so the gate
  falls back to raw MSPR (unknown never penalises); verdict accuracy measured at the next audit.

## 2026-05-25 — post-regression fix (discovered, not in the register)

- **Sector-rotation persistence gate: unit-mismatch fix.** The conditional sector single-name-leader
  `+1` gate (added 05-23 P1.5) required `persistence_score ≥ 3`, but
  `options_flow_sector_flow_persistence` returns a **0–1 sign-consistency fraction** (1.0 = all 5 days
  same sign, 0.8 = 4/5) — so `≥ 3` was structurally unsatisfiable and silently zeroed the gate for
  every sector. Re-baselined to **`≥ 0.6`** (the days-agnostic form of the original ≥3-of-5-days
  intent) across all 7 occurrences (`sector-rotation-strategist.md` ×3, `signal-confluence-quant.md`,
  `risk-monitor.md`, `daily-analysis.md`, `weekly-analysis.md`), each with an inline note that the
  tool returns a 0–1 fraction. The gate now fires; the cum_flow sign + $50M magnitude conditions still
  do the hard discrimination. Surfaced by the weekly quant during the P0 regression run.
