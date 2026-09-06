# Calibration Audit — 2026-06-06

33 reports · 585 calls · **432 decided** (WR 47.9%) · first audit with a verbatim-envelope
decided subset (53) **and a second regime state** — the 2026-06-05 break (SPY −2.0%, VIX
16→21.5) stress-tested every May call.

## Top 3 schema flaws
1. **The 0.80 quote ceiling shipped 05-30 is leaking**: 11 post-register vol/earnings rows
   quote 0.837–0.933 raw backtest rates (decided: 0-for-3), and the helper script still caps
   at 0.85/0.90. Phase 7 verification + Phase 3 (`earnings_vol` +28.7pp divergence, BH 🚩).
   **Patch P0.1.**
2. **HIGH-tier expectancy negative for the third straight audit** (−1.85%/trade, payoff
   0.58) and the first holdout HIGH calls went 0-for-2 into the break. Kelly stays ADVISORY;
   the ≥9 cut holds but is regime-conditional until June resolves. Phase 3 §5 / Phase 5 C.
3. **MED<LOW inversion persists (3rd run)** — the additive score pays for beta-long evidence
   (bullish_flow −17.9pp excess) and under-scores alpha shorts (+7.5pp). A direction defect,
   not a cut defect. Phase 5 B. Patch P2.2.

## Top 3 tool-tier surprises
1. **`event_risk` gate fires on 90% of post-register calls with zero discrimination**
   (downgraded 43% vs ungated 43%, n=46 — reportable). The 05-30 widening overshot. Phase 6.
   Patch P1.2.
2. **The fundamentals gate is the first stage earning its keep**: gated names 39% vs
   confirmed 47%, FP-rate 40% on n=20 decided. Phase 6 §3.
3. **`cumulative-premium-flow`: most-cited tool (n=136), NO-INFO three runs running**
   (−3.5pp) — corroborated by the NEE dividend-arb miss. Phase 4. Patch P1.4.

## What we'd do Monday
Friday repriced the book's story. Short alpha compressed +19.7pp → **+6.0pp** the first time
the tape actually broke — it was partly regime timing, so run shorts as a hedge sleeve, not
a profit center. Longs stay negative-edge beta (−17.2pp vs SPY, now confirmed in two
regimes). Before the open: enforce the 0.80 ceiling in the vol lane and fix
`excess_winrate.py`'s stale 0.85/0.90 caps (P0.1 — Friday's report emitted six 0.933 quotes);
re-scope `event_risk` to named binary events so it ranks instead of stamps; sync the
validator's HIGH band to ≥9 — the suppressed raw-9s went 3/4 while recorded-HIGHs went 1/5.
Keep sizing off `dealer_positioning` + `dex` + `dark-pool block-stratified` — still the only
evidence that survived all three audits. Re-audit ~06-12 when the June cohort and first
LEAPs close: C17 analyst-divergence (−37pp) and C28 distribution_flag (−22pp) both showed
first signed evidence and are next in line for promotion.
