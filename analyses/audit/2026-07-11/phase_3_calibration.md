# Phase 3 — Calibration Audit (2026-07-11)

## Per-class realised WR + benchmark-excess (C21) — decided-N ≥ 8, BH FDR 0.10
| Class | N | WR | SPY-bench | Excess (pp) | BH |
|---|---|---|---|---|---|
| dark_pool_accumulation | 24 | 0.417 | 0.708 | **−29.2** | **SURVIVES** (p=0.003) |
| bearish_flow | 17 | 0.471 | 0.176 | **+29.4** | **SURVIVES** (p=0.005) |
| bullish_flow | 17 | 0.412 | 0.529 | −11.8 | ns |
| dealer_positioning | 8 | 0.375 | 0.500 | −12.5 | ns |
| multileg_directional | 11 | 0.273 | 0.273 | +0.0 | ns |

*THIN_N appendix (5–7 decided, not headline): earnings_vol (7), high_iv_rank (5).*

### (a) Where the rubric is honest
Nowhere it can prove — the frozen era carries no numeric win-rate to calibrate against (all `NA(substrate)` post-quarantine). The one honest thing: the quant **stopped quoting rates it cannot back**.

### (b) Where it lies to itself — the accumulation lane
`dark_pool_accumulation` claims LOAD-BEARING status (+3 conjunction, the single highest-weighted line) and realises **0.417 vs a 0.708 SPY up-day base rate — −29.2pp, and it SURVIVES multiple-hypothesis correction (p=0.003).** This is not miscalibration, it is **negative edge**: the accumulation longs win only because the tape rose, and they badly lag even that. A flow trader's read: *"institutions printing dark-pool blocks in an up-tape is the tape, not a signal — you're paying 3 points to buy beta at a 29-point discount to just being long SPY."*

### (c) Tier inversion / High-tier overconfidence
HIGH pooled 0.286 (2/7), driven by 4 index/semis shorts 0-for-4 (2026-05-30 HIGH = 0.000, n=3). All 7 HIGH are pre-freeze; the frozen era's only tier is LOW (0.529, n=17). The inversion is a **pre-freeze artifact the freeze correctly halted** — do not re-bin.

### (d) CALIBRATED-BUT-BETA (the desk-critical read)
- `dark_pool_accumulation` −29.2pp, `bullish_flow` −11.8pp, `dealer_positioning` −12.5pp — **the entire long/accumulation complex is negative-excess.** These lanes ride the tape; they do not beat it.
- **`bearish_flow` +29.4pp (p=0.005, SURVIVES)** is the *only* class with real, significant edge — shorts win 0.471 against a 0.176 SPY-short base rate. **The rubric scores this with ZERO points** (the single-leg-put/bearish edge is still advisory C19). *The one thing the system does that beats the market is the one thing it refuses to size.*

## Brier / log-loss
**Brier 0.302, log-loss 0.818 (n=93 legacy numeric-win_rate calls).** ≥0.25 = "no better than coin-flip"; the pre-quarantine substrate-contaminated `win_rate` quotes were overconfident, concentrated (per prior audits) in the ≥0.80 buckets. Post-freeze: **no numeric win_rate exists** → confidence-calibration not computable, which is the correct posture, not a gap.

## raw_score → WR (frozen era)
raw=3: 0.467 (n=15); raw=4/5: n=1 each (SNDK/NVDA, W28, still INCONCLUSIVE) — **frozen-era scatter is essentially a single point at raw=3.** No monotonicity claim possible; nothing to re-bin.

Output: `phase_3_calibration.jsonl` equivalents embedded above.
