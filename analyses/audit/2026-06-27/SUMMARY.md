# Calibration Audit — 2026-06-27

**Dataset.** 29 envelopes (24 daily + 5 weekly), 257 calls, 205 decided on real daily-OHLC path
resolution. **First audit with a non-pure-uptrend stratum** (late June rolled PULLBACK→CHOPPY, SPY
−2.86% 30d) — but the selloff calls (06-23→06-26) are still window-open, so cross-regime evidence is
*partial*. Every headline below was independently re-derived by three adversarial verifiers (all
CONFIRMED). **Nothing is P0:** all tier/raw evidence is pre-freeze and the frozen 2026-06-12 rubric has
produced **0 HIGH / 0 MEDIUM** decided calls — ungradeable on its own outcomes.

## Top 3 schema flaws
1. **Conviction ladder inverted at the top — 3rd straight audit.** HIGH realised **0.143** (worst tier);
   raw 10/11/12 → **0%/33%/0%**. Regime-invariant. It has a face: the 7 HIGH calls are **4 index-ETF
   shorts (SMH/IWM, 0-for-4) + 2 faded longs** — the negative-selection short book wearing a HIGH badge.
   Phase 3/5 → KEEP freeze; C41. **P1.**
2. **Fabricated ≥0.80 vol quotes still reach the sizer.** `earnings_vol` 0.88→0.38, `high_iv_rank`
   0.83→0.36 — the only two BH-survivors, both vol. The ≥0.80 bucket (n=33) realises **42.4%**, 28/33
   from the substrate quarantined 06-12; Brier 0.306. Phase 3 → bind ceiling at emission. **P1** (C42).
3. **The long "edge" is uptrend-conditional.** +18.7pp matched aggregate, but significant **only** in
   uptrend (+29pp, p=0.003); **zero in the pullback** (+4.9pp, p=0.79). And `bearish_flow` is
   calibrated-but-beta — beats its 0.42 claim (0.54) yet excess **−21.7pp**. Phase 3b. **P1.**

## Top 3 tool-tier surprises
1. **No tool survives Benjamini-Hochberg — 4th audit running.** Every tier label is structural-only.
2. **Only one frozen weight earns its points:** `institutional_accumulation` +13.6pp (n=23); **`+1 DEX`
   (−19.8pp) and `+2 multileg` (−12.7pp) are net-negative** class-controlled.
3. **`cumulative_premium_flow` is ubiquity-confounded** (58% of rows); the vol-structure tools read
   negative because they faithfully sit on the bad vol substrate, not because they're broken.

## What we'd do Monday
The engine still has a **long edge and a short problem** — read both humbly. **Stop sizing shorts for
alpha** (no selection edge in any decided regime; McNemar p=0.0035) — but **REVISE, not strengthen, the
06-20 "express bearish index-relative" rule**: this window the *sized* money that bled was index ETFs (6
of 7 sized shorts, −2.10% mean) while the lone single-name short won — the index preference is refuted.
**Don't up-size longs into the open selloff** (the edge is uptrend-only). **Bind the ≥0.80 vol ceiling at
emission.** And **hold everything protective** — the freeze (lift can't run), the half-cap (now with its
first protective datum, out-of-regime −16.7pp), and all 9 gates (each net-protective). The regime that
proves or breaks these calls is still window-open; on a tape mid-roll you don't dismantle the insurance.
