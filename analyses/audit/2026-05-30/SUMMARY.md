# Calibration Audit — 2026-05-30

**Dataset:** 27 reports (22 daily, 5 weekly), 516 calls, **365 resolved** (WIN+LOSS). Thresholds
passed — no DATASET-SIZE-RELAXED. **First run on the C20–C25 method** (daily-bar path-aware
resolution + benchmark-excess + reliability/log-loss + Benjamini-Hochberg). Outcomes resolved on
**real daily OHLC** (chart API the yfinance MCP wraps); citations still **reconstructed** (envelope
rows window_open). **Single UPTREND regime + reconstructed citations ⇒ no finding qualifies P0.**

## Top 3 schema flaws
1. **The long book is negative-edge beta.** BOOK-long 58.0% vs **SPY-long 80.2% base = −22.2pp**;
   every long class trails the index (dark-pool −21, bullish −20, even honest dealer −7). Only the
   shorts (+21pp excess) and hedges beat their benchmark. The rubric scores beta-longs high and
   alpha-shorts low — *the* defect. Phase 3d / Phase 5. Patch **P1.1**.
2. **Overconfidence is localized to the ≥0.80 quote tail.** The ≥0.90 bucket (n=38) realises **53%**;
   0.80–0.90 (n=21) realises 62%. Brier 0.316 / log-loss 1.030 live entirely there. Cap the high
   quotes — not the 05-29 class-specific floors (obsolete: dark-pool realised 63%, not 51%). Phase 3 C25. **P1.2**.
3. **The MED<LOW tier inversion is a direction defect, not a cut defect.** LOW (54%) beats MED (50%)
   under every cut because alpha-shorts score low. Score ≥9 *is* clean (77%, n=31) → raise HIGH 10→9,
   but re-binning can't fix a score inversely correlated with edge. Phase 5. **P1.3 + P2.3**.

## Top 3 tool-tier surprises
1. **Zero tools survive Benjamini-Hochberg.** The entire tier list is BH-insignificant on reconstructed
   citations — the 05-29 run shipped P0 gate-surgery off exactly this noise. Phase 4 / C23.
2. **`term-skew` flipped −13.4 → +7.9pp; `oi-trend` +12.2 → +0.4; `signal-confluence` +17.2 → −1.0.**
   Tool tiers are method-unstable. The 05-29 "demote term-skew" and "add oi-trend/sweep-persistence to
   the gate" recs are **retracted** — they were close-only artifacts. Phase 4.
3. **Only `dark-pool block-stratified` (+14) and `options-structure dex` (+14) are durable across both
   methods.** Those two are the desk's real evidence tools; everything else moved 15–30pp. Phase 4.

## What we'd do Monday
Nothing irreversible — and that's the finding. The corrected method (real OHLC, SPY benchmark, BH,
reliability curve) **demotes all three 2026-05-29 P0s to P1/P2 and retracts two outright.** The single
durable, regime-robust truth is directional: **the desk's long selection is beta you overpaid for
(−22pp vs just buying SPY); its short selection is the alpha (+21pp).** So the Monday move is a *read*,
not a patch — stop sizing long flow as if it were edge, lean into the short book and `dealer_positioning`
(the one honest, least-beta long), and **surface benchmark-excess in the report** so the human sees beta
vs alpha. Hold every rubric re-weight: tool MCs swing 15–30pp with the resolution method and none survive
BH. The HIGH→9 cut and the fundamentals-VETO false-positive rate (2 of 3 VETO'd names won — thin) both
wait for this week's calls to resolve (~06-12). Kelly stays ADVISORY (HIGH expectancy −1.24%, non-monotone
— unchanged and robust). And fix the auditor's own C20 spec: it names an MCP tool that returns close-only;
the real OHLC is in the chart API it wraps.
