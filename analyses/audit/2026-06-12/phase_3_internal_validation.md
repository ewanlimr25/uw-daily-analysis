# Phase 3 — Internal Validation (backtest re-runs + outcome grading)
**Date:** 2026-06-12 (evening). All numbers below computed this session from local data (parquet via `uw` CLI / repo scripts / production envelopes). Evidence sidecars: `p3_envelope_calls.json`, `p3_graded_calls.json`; script outputs quoted inline.

**Method caveats (apply throughout):** outcome grading is close-to-close, 5-trading-day forward, direction-signed WIN/LOSS — *not* path-aware (no stop/invalidation modeling); forward windows overlap within the same tape (effective n < nominal n); the resolution window (calls 2026-05-25 → 06-04, resolved through 06-11) **straddles the UPTREND → TRANSITIONAL regime turn** — that is both a limitation and precisely the out-of-regime test the rubric said it needed. Vol-direction calls (n=8) excluded from directional grading.

---

## 1. Headline backtest re-runs: claimed vs measured

| Claim (source) | Claimed | Measured this session | Verdict |
|---|---|---|---|
| 0DTE premium-selling (zerodte_setup.py, §2a advisory) | GO; open-entry ~+0.45%/day at 83–97% win; overnight negative; GEX→range suppression | **GO confirmed**: SPY 95.3% win / +0.302%/day, QQQ 90.7% / +0.392% (n=43); overnight −0.21/−0.43%; gex→range corr −0.39 (long-γ 0.77% vs short-γ 1.22% range) | **CONFIRMED, precise-ish** (mean PnL ~0.30–0.39 vs claimed ~0.45 — modest drift). Cracks: QQQ VIX-tercile sizing non-monotone (MID 0.604 > HIGH 0.459); tail still unsampled. Advisory status appropriate |
| GEX walls-as-magnet (gex_next_session_backtest.py) | NO_GO_NO_EDGE | **NO_GO re-confirmed and then some**: pooled closer-to-wall 26.7% (n=86) vs 50% — walls are statistically significant **anti-magnets**; H1 vol split holds for SPY (0.727 vs 0.444) but inverts for QQQ (n=14) | **CONFIRMED**. §2's "no predictive claim" framing is exactly right |
| Single-leg whale Tier-1 PUT (C19; single_leg_whale.py) | OPENING_PUT_PRIME WR 63.5%, +26pp vs SPY, p<0.001 (n=266); floor-put 61.0%; calls beta −9.7pp; size/OI<0.5 anti-signal | Re-run on refreshed 44-day window (3,855 graded prints): **PRIME WR 0.600 (n=295), +21.9pp, p≈0**; floor-put 0.582 (n=366), +20.1pp; tier ordering holds (T1 0.600 > T2 0.481 > closing 0.457); calls s/OI≥2 DTE≤30 0.495 = **−12.4pp**; closing calls n=1525, −13.0pp, z=−10.4. Month-stable: 0.601 / 0.583 / 0.591 / **0.632 (June, n=19 — first TRANSITIONAL accrual)** | **CONFIRMED with modest decay** (−3.5pp vs claim). This is the strongest internally validated edge in the system — and it sits in a 0-point advisory lane. June data begins the second-regime accrual C19's graduation gate requires |
| PEAD +1 (C7) / 52w-high +1 (C8) | NO_GO (hit 0.4706 < 0.55; split 4.2pp < 10pp) — lines withheld | Gate logic + thresholds verified in code and 197-test suite; cohort re-build not warranted for withheld lanes | **STANDS** (withhold honest; PEAD n=17 single-window caveat remains) |
| Emission caps (excess_winrate.py, P0.1) | 0.69 (n<10) / 0.80 absolute, all lanes, at emission | Envelope census: 23 violations 05-25→06-05 (0.837–0.933, vol/earnings lanes), **0 violations 06-08 onward**; sub-0.50 floor: 1 violation ever (LLY 06-05) | **FIX BINDS NOW** — the leak was real, the patch works |

## 2. `uw historical signal-backtest` substrate (P1 F2, quantified)

Probed `bullish_flow`, 5d lookback, full pagination (n=151 signals; tool self-reports `truncated_signals: 13` *and includes them in the headline*):
- **Window clamping measured:** complete-5d-window rows WR **0.485** (n=136); clamped rows (signal too recent to resolve, graded at latest bar) WR **0.733** (n=15, 9.9% of sample) → headline **0.510**. The recency artifact alone lifts the quote across both the 0.50 ladder boundary (starter/skip → half) and the sign of the read.
- **Pagination instability:** `--top-n` 20/50/100/200 → reported WR **66.7% / 36.1% / 51.4% / 51.0%** — a 30-point, non-monotone swing on an undocumented ranking. The default (20) quotes the most flattering number.
- Implication: every ladder/cap/excess computation downstream consumes a number whose two free parameters (as-of recency, pagination) move it by more than the entire claimed edge of any signal class. The caps contain the *level*; nothing contains the *noise*.

## 3. Tier-monotonicity re-confirmation — **the test the rubric scheduled for today, and it FAILS**

Resolved directional envelope calls (n=50 of 81; 5d close-to-close; SPY same-window direction baseline):

| raw_score band | n | realized WR | SPY-direction base | excess | mean directional return |
|---|---|---|---|---|---|
| HIGH (≥9) | 9 | **0.222** | 0.333 | −0.111 | **−5.1%** |
| MED (7–8) | 14 | **0.214** | 0.429 | −0.214 | −5.8% |
| LOW (3–6) | 27 | **0.444** | 0.481 | −0.037 | −1.8% |

- **Monotonicity is fully inverted** (LOW > HIGH ≈ MED). The in-file claim "≥9 realised 0.774 (n=31)" diverges from this window by **−55pp**; even at n=9, observing ≤2 wins under a true 0.774 has p ≈ 0.001. Allowing generously for method differences (close-only vs path-aware) and overlap, the conclusion stands: **the tier bands carry no out-of-regime information** — P1 F4 (threshold snooping on one regime) is confirmed in live forward data, on schedule.
- Direction cut: longs n=36 WR 0.250 (mean −5.1%) — the additive rubric concentrated conviction in longs exactly into the turn; shorts n=14 WR 0.571, +0.7% mean, but still −7pp vs the SPY-short bet (this window's short wins were tape, not selection).
- **The gate stack earned its keep in the same breath:** final sizes — the 2 `half` calls went 0-for-2 (−7.5% mean), 6 `starter` 0-for-6, while 30 `skip` (WR 0.333) and 11 `watch_only` were correctly not capital; the single VETO would have won (1/1 false positive, consistent with the gate's known FP profile). The compression that makes tiers cosmetic (P2 battery: zero full-size ever) also meant the tier collapse cost little real capital. Both facts belong in the plan: the scoring layer is broken as a *ranker*; the gating layer works as a *brake*.

## 4. Win-rate quote calibration — anti-calibrated, monotonically

| Quoted `win_rate` bucket | n | mean quote | realized | gap |
|---|---|---|---|---|
| < 0.50 | 12 | 0.405 | **0.583** | +0.179 |
| 0.50–0.69 | 23 | 0.567 | **0.174** | −0.394 |
| 0.70–0.80(+leaks) | 13 | 0.811 | **0.385** | −0.426 |

Higher quotes did strictly worse. Combined with §2, the quoted `win_rate` field currently carries **negative rank information** on this window. (The <0.50 bucket outperforming is exactly the C19-style short/put lane the rubric under-weights.)

## 5. Weekly scorecard headline vs resolved outcomes
W22 claims 66.7%, W23 claims 70% intra-week hit rates. Forward-resolved grading of the same period's envelope calls runs 0.227 (early June) – 0.429 (late May). The metrics differ by construction (intra-week flow confirmation vs 5d forward outcome) — but the gap is the size and sign Phase-1 F10 predicts from hindsight grading + survivor universe + INCONCLUSIVE exclusion. Notably the W23 *prose* is more honest than its own headline ("None sized"; "every WIN was bearish… every LOSS was a cyclical long").

## 6. Same-window split (regime sensitivity)
Late-May resolved calls WR 0.429 → early-June 0.227. Every fitted weight in the rubric comes from the regime that ended this week.

## 7. Carried to P4/P6
- The system's only internally-robust edges this session: **(a) Tier-1 single-leg put (advisory, 0 pts), (b) 0DTE premium-selling (advisory, 0 pts), (c) the downgrade-only gate/brake machinery**. The scored rubric layer failed its own scheduled re-confirmation.
- P4 must check: does the put-side/closing-flow asymmetry match Pan-Poteshman-style external evidence (it should); is the "walls anti-magnet" result consistent with published dealer-hedging literature; does the DEX/vanna +3 line have any external support at its current weight.
- P6 plan candidates from P3: rebuild/replace `signal-backtest` (complete-window-only grading, pinned pagination, per-ticker mode or honest market-wide labeling); freeze rubric weights pending cross-regime data; promote C19 along its pre-registered gate as TRANSITIONAL data accrues; keep the brake stack; fix the weekly §0 headline to grade against envelopes.
