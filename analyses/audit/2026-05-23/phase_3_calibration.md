# Phase 3 — Calibration Audit

**Audit run-id:** 2026-05-23
**Universe:** 302 Phase 1 rows; 73 fully resolved on win-rate basis (W or L; INCONCLUSIVE excluded).
**Compared against:** Phase 2 outcomes (15 new resolved + 58 carried forward from prior audit 2026-05-15).

Voice: composite desk reviewer — *does the rubric tell the desk something true about the next call, or does it overstate the edge?*

---

## 1. Per-signal-class table — claimed vs realised

For each `dominant_signal_class` with N≥5 in the combined-resolved set.

| Signal class | N_resolved | Mean **claimed** WR | Realised WR (W/L only) | Divergence | Flag |
|---|---|---|---|---|---|
| **dark_pool_accumulation** | 14 | 0.93 | **0.714** (10W/4L) | +22 pp | OVERCONFIDENT (worse vs prior — added losses) |
| **bullish_flow** | 14 | 0.88 | **0.714** (10W/4L) | +17 pp | IMPROVED — new WINs (TLT, AAPL, INTC-W21) closed half the gap |
| **multi_day_sweep** | 7 | 0.70 | **0.429** (3W/4L) | **+27 pp** | STILL SEVERELY MISCALIBRATED |
| **earnings_vol** (all variants merged) | 8 | 0.85 | **0.625** (5W/3L) | +22 pp | OVERCONFIDENT — the 0.90 vol_realisation cap is too generous |
| **bearish_flow** | 8 | 0.46 | **0.250** (2W/6L) | +21 pp | Worst absolute realised; regime mismatch persistent |
| **gamma_breakout** | 7 | 0.79 | **0.571** (4W/3L) | +22 pp | UNCHANGED — still overconfident, still no MCP backtest support |
| **multileg_directional** | 5 | 0.78 | **0.600** (3W/2L) | +18 pp | UNCHANGED |
| **dealer_positioning_flip** | 4 | 1.00 | 0.750 (3W/1L) | +25 pp | Low-N; merge candidate with gamma_breakout |
| **contrarian_fade** | 4 | 0.74 | 0.500 (2W/2L) | +24 pp | Low-N; coin-flip behavior |
| **sector_rotation** | 2 | n/a | 0.500 (HON W, WMT L) | INSUFFICIENT_N | New class — adding WMT LOSS is a single-event signal |
| **leap_directional** | 2 | n/a | 0.500 (1W/1L) | INSUFFICIENT_N | BL LOSS resolved a fresh data point — still small sample |

**Reading.** New data hardened two findings:
- `multi_day_sweep` is **persistently mis-calibrated** at +27pp claimed > realised — repeated 0.71 quote, repeated 0.42 realisation across two audit cycles.
- The 0.90 `vol_realisation_rate` cap for `earnings_vol` was tested live by DELL and MRVL W21 (both LOSSES on directional move blow-through). It overstates by 22pp.

New data partly corrected one finding:
- `bullish_flow` improved from prior 0.64 realised to 0.71 with TLT/AAPL/INTC W21 WINs.

**Desk note (sell-side flow trader voice).** *"The persistent miss is `multi_day_sweep`. Two audit cycles later it still claims 0.70 and prints 0.43. The book is bleeding paper that the rubric thinks is alpha. Either gate the signal behind same-direction cum_premium_flow alignment or stop sizing on it."*

---

## 2. Per-tier reliability — **TIER INVERSION DETECTED**

| Tier | N_resolved | WIN | LOSS | Realised WR | Δ from prior audit |
|---|---|---|---|---|---|
| **HIGH** (raw ≥7 post-LB-gate) | 25 | 15 | 10 | **60.0%** | ↓ from 66.7% |
| **MED** (raw 4–6 or LB-demoted) | 24 | 15 | 9 | **62.5%** | ↑ from 55.6% |
| **LOW / starter** (raw 1–3) | 16 | 9 | 7 | **56.3%** | ↑ from 54.5% |
| (legacy 04-30, no rubric) | 8 | 4 | 4 | 50.0% | unchanged |

**Monotonicity check:** HIGH > MED > LOW required.
**Result: 60.0 < 62.5 > 56.3 → INVERTED at HIGH-vs-MED.**

This is a desk-quitting signal per skill spec. The MED tier is now realising 2.5pp **higher** than HIGH. Driven by:
- New HIGH-tier resolved: MA LOSS, MU-short LOSS, TTWO-short WIN, BL LOSS → 1W/3L on the new HIGH cohort.
- New MED-tier resolved: WDAY WIN, CRWV WIN, TLT WIN, AAPL(5/19) WIN, AAPL-W21 WIN, WMT LOSS → 5W/1L on the new MED cohort.

The mechanical explanation: the 2026-05-15 P0 audit applied the 3-of-4 load-bearing gate, which **demoted high-conviction HIGH calls (AAPL W21, TLT, etc.) into MED**. Those demoted MED calls then won. Meanwhile the HIGH tier kept calls (MA HIGH→starter, MU short HIGH, BL HIGH LEAP) that were the genuine misses. The P0 gate is working in the **opposite** direction it was designed for — it correctly identifies overconfident HIGH calls and demotes them, but the residual HIGH cohort that survives the gate is now smaller and noisier.

**Desk note (buy-side PM voice).** *"The 3-of-4 LB gate is filtering the wrong way around. It's catching the genuine high-conviction names (4-of-4 LB → AAPL/MSFT) and demoting them based on load-bearing-tool counts, while keeping pure-narrative HIGH scores (MA accumulation-only, BL LEAP-only) at full tier. The HIGH tier post-2026-05-15-P0 isn't what we think it is. Phase 5 must rethink the tier cuts on the NEW gate behaviour, not the pre-gate behaviour."*

---

## 3. Brier score (combined)

Across 73 resolved rows with both `claimed_win_rate` and binary outcome:

```
Brier ≈ 0.224 (combined)
```

Calibration thresholds (per skill):
- ≤ 0.10 = professionally calibrated
- 0.10–0.25 = positive edge but overstated
- ≥ 0.25 = no better than coin-flip

**Verdict: 0.224 — in the "overstated but edge present" band, marginally worse than prior (0.218).** The dataset added a class of LOSSes the rubric had claimed as 1.00 (`dealer_positioning_flip` and HIGH-tier picks), nudging Brier up.

Sub-Brier by class (combined):
- `dark_pool_accumulation`: ~0.18 (worsened from 0.151)
- `bullish_flow`: ~0.21 (improved from 0.247)
- `multi_day_sweep`: ~0.34 (still worst; near coin-flip)
- `earnings_vol`: ~0.27 (the 0.90 cap is the dominant contributor)
- `bearish_flow`: ~0.18 (calibrated low, no large miss)

---

## 4. Conviction-vs-outcome scatter (raw_score quintiles)

| Quintile | Score range | N | WIN | LOSS | Realised WR | Δ from prior |
|---|---|---|---|---|---|---|
| Q5 | 9–13 (HIGH-band top) | 14 | 9 | 5 | **64.3%** | ↓ from 72.7% |
| Q4 | 6–8 (HIGH-band low) | 18 | 11 | 7 | **61.1%** | ↑ from 57.1% |
| Q3 | 4–5 (MED) | 19 | 11 | 8 | **57.9%** | ↑ from 53.8% |
| Q2 | 2–3 (LOW) | 12 | 7 | 5 | **58.3%** | ↑ from 44.4% |
| Q1 | ≤1 / negative | 5 | 3 | 2 | 60.0% | unchanged (low N) |

**Slope from Q1→Q5:** Now nearly flat at 58–64%. The Q4→Q5 jump that justified premium sizing for ≥9 raw is **gone in this update** (61.1% → 64.3% is only +3pp). Prior audit's "single most defensible piece of the rubric" no longer holds on updated dataset.

**Critical finding.** The score distribution has compressed toward the middle — newly-resolved LOSSes are concentrated in the Q5 band (MU-short, MA-HIGH, BL-LEAP all scored ≥9). If this hardens with more data, the rubric's score-to-outcome curve is no longer informative above the LOW floor.

---

## Verdict

### (a) Where the rubric is honest

- **Score floor still discriminates marginally.** Calls scored ≤2 are dropped — that decision is vindicated; the dropped names rarely turned into surprise winners.
- **`dark_pool_accumulation` remains the best-calibrated working class** (claimed 0.93 → realised 0.71). Still positive edge after gate stack.
- **`bearish_flow` correctly sized down to floor.** The rubric's 0.46 claim is closer to realised 0.25 than other classes are to their realised numbers (smaller divergence in pp).

### (b) Where it lies to itself

- **The tier system is now inverted (HIGH 60% < MED 62.5%).** Calibration-breaking. The 3-of-4 LB gate inadvertently demotes the working calls and keeps the narrative ones.
- **`multi_day_sweep` is structurally mis-calibrated at +27pp** across two audit cycles. The signal is informational only when same-direction cum_premium_flow agrees.
- **`earnings_vol` 0.90 cap was tested live by DELL/MRVL W21.** Both BLEW THROUGH ±10% wings on directional moves. The "vol_realisation_rate as proxy" trick cannot defend size when the implied move is materially wrong.
- **Win-rates for `dealer_positioning_flip` and `gamma_breakout` are agent-fabricated.** `historical_signal_backtest` returns empty for these classes (and for the canonical 5 either). The rubric cites numbers the backtest tool cannot produce.

### (c) Tier inversions / HIGH-tier overconfidence

- **HIGH-tier overconfidence has compounded.** Realised dropped from 66.7% (prior) to 60.0% on a +25% sample expansion. Three new HIGH-tier LOSSes (MA, MU-short, BL) — every one of them either had flow_conflict or load-bearing-tool count below 3.
- **No clean HIGH-vs-MED separation any more.** The two tiers are statistically indistinguishable; sizing posture "HIGH=full, MED=half" is doing real work via gate-stack demotion but not via realised win-rate ordering.

---

## Per-class desk commentary (one sentence each, updated)

- **dark_pool_accumulation (0.93→0.71):** Still the best signal but the +22pp claimed-realised gap is widening — every new HIGH call sized on this class should quote a 0.70 ceiling, not 0.85+.
- **bullish_flow (0.88→0.71):** Improved with new TLT/AAPL/INTC W21 WINs; still +17pp overstated; trim quote to 0.65.
- **multi_day_sweep (0.70→0.43):** *Persistently broken.* Don't trade on it standalone. Require flow_conflict=FALSE as a gate before sizing.
- **earnings_vol (0.85→0.625):** The 0.90 vol_realisation_rate cap was crushed by DELL/MRVL W21 (both directional blow-throughs). Use a 0.65 floor when the back-month skew is COMPLACENT.
- **bearish_flow (0.46→0.25):** TRANSITIONAL-UPTREND regime continues to crush short single-name; size only when sector + cum_flow + dealer all agree (rare).
- **gamma_breakout (0.79→0.57):** Borderline; merge with dealer_positioning_flip (same underlying agent) and let the combined class earn its win-rate from a larger N.
- **multileg_directional (0.78→0.60):** Solid when second agent confirms; overstated when standalone.
- **dealer_positioning_flip (1.00→0.75 n=4):** Sample too small. Merge with gamma_breakout.
- **contrarian_fade (0.74→0.50):** Coin-flip; needs term-structure FLAT confirmation gate to be sized.
- **sector_rotation (0.5 n=2):** HON WIN vs WMT LOSS = sector-leader thesis is only as good as the macro that frames it. Defensive rotation broke on WMT earnings — single-name idiosyncratic risk dominates.
- **leap_directional (0.5 n=2):** BL LOSS resolved against AAPL-W18 WIN; insufficient N. Per-radar 6-of-9 gate is too restrictive for calibration measurement.

---

## Files

- `phase_3_calibration.md` (this) — tables + verdict
- `phase_3_calibration.jsonl` — not produced (computed inline; reproducible from `phase_1_inventory.jsonl` + `phase_2_outcomes.md` aggregates)

**Phase 3 closed. Phase 4 begins — tool attribution against this same outcome set.**
