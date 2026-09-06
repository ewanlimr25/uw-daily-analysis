# Phase 3 — Calibration Audit (2026-06-27)

Provenance: verbatim envelope. Decided-N ≥ 8 headline floor (C23); 5–7 → appendix. Benjamini-Hochberg
FDR 0.10 across the class set. Claimed = mean envelope `win_rate`. Excess = realised − SPY same-window
same-direction base (C21). Stratified by `rubric_era`; **all raw-≥9 calls are pre-freeze.**

## 1. Per-signal-class table (decided ≥ 8)

| class | n | realised | claimed | div pp | SPY base | **excess** | p | BH |
|---|---|---|---|---|---|---|---|---|
| bearish_flow | 46 | 0.54 | 0.42 | −12.5 | 0.761 | **−21.7** | 0.120 | n |
| dark_pool_accumulation | 33 | 0.46 | 0.55 | +10.0 | 0.364 | **+9.1** | 0.328 | n |
| bullish_flow | 32 | 0.50 | 0.59 | +9.2 | 0.281 | **+21.9** | 0.376 | n |
| **earnings_vol** | 29 | **0.38** | **0.88** | **+49.8** | 0.667 | **−28.7** | **0.000** | **Y** |
| multileg_directional | 17 | 0.35 | 0.56 | +20.2 | 0.353 | 0.0 | 0.154 | n |
| dealer_positioning | 16 | 0.50 | 0.60 | +9.7 | 0.562 | −6.2 | 0.587 | n |
| **high_iv_rank** | 11 | **0.36** | **0.83** | **+46.3** | — | — | **0.002** | **Y** |

Appendix (THIN_N 5–7, not headline): multi_day_sweep 0.857 (n=7) · gamma_breakout 0.333 (n=6).

### (a) Where the rubric is honest
`dark_pool_accumulation` (claim 0.55 / real 0.46) and `dealer_positioning` (0.60 / 0.50) are within a
desk's tolerance — modest overclaim, no BH flag. `bullish_flow` *under*-delivers on hit-rate (0.59→0.50)
but that's the honest cost of chasing sweeps.

### (b) Where it lies to itself — and it's the same two lies as 06-20
**`earnings_vol` claims 0.88, realises 0.38 (n=29, p<0.001, BH-survives). `high_iv_rank` claims 0.83,
realises 0.36 (n=11, p=0.002, BH-survives).** Both are vol classes; both quote ≥0.80 and deliver ~0.37.
*Sell-side read:* these are the desk's "this always works" trades — short premium into an event, fade a
high IV-rank — and they are the two the tape punished hardest when realized vol expanded into the
pullback. **Honesty caveat that 06-20 under-stated:** both classes are dominated by **vol-mode,
RV-proxy-resolved** rows, so the *exact* realised (0.38/0.36) is proxy-clouded — but no proxy artifact
turns a true 0.85 into 0.37. The quote is fabricated; the realised is "clearly not ≥0.80." Fix lives in
emission (cap), not in the resolver.

### (c) Tier inversions / High-tier overconfidence
See §2 — **the inversion is the headline and it is now three audits deep.**

### (d) Calibrated-but-beta (excess ≤ 0 despite honest calibration)
**`bearish_flow` is the cleanest calibrated-but-beta class: realised 0.54 (it even *beats* its 0.42
claim) yet excess −21.7pp** — it "wins" 54% only because shorting anything in a falling tape wins; a
naive SPY short won 76% over the same windows. A desk that reads bearish_flow's 0.54 as edge is paying
for beta it could get for free. `dealer_positioning` is mildly the same (−6.2pp). **This is the
desk-critical read: bearish_flow passes calibration and is still negative edge.**

## 2. Tier reliability — the conviction ladder is inverted at the top (3rd consecutive audit)

| Tier | n | realised WR |
|---|---|---|
| **HIGH** | 7 | **0.143** ⟵ worst |
| MEDIUM | 19 | 0.526 |
| LOW | 66 | 0.455 |
| DROP | 113 | 0.487 |

**HIGH is the worst tier on the board** (06-12: 0.222; 06-20: 0.143; 06-27: 0.143). Monotonicity
requires HIGH > MEDIUM > LOW; we have HIGH < everything.

**Mechanism (new this run — the inversion has a face).** The 7 HIGH-tier decided calls are **4 index/ETF
shorts (SMH 05-28, SMH 05-29, IWM 06-05, SMH 06-10 — 3 semis + 1 small-cap) — 0-for-4 — plus AAPL & ORCL
longs that faded, versus 1 MSFT long win.** The HIGH tier *is* the negative-selection short book wearing
a HIGH badge: the rubric's top scores went to dealer-positioning / bearish-flow index-ETF shorts during
an uptrend, and they got run over. The inversion is not mysterious — it is the short problem (§Phase 2)
concentrated at the top of the score.

**Regime-invariant.** HIGH realises 0.20 (n=5) in uptrend and 0.00 (n=2) in pullback — bad in both
strata we can grade (choppy has 0 decided). Not a regime artifact.

## 3. Brier / log-loss / reliability deciles (graded n=132)

**Brier 0.306** (> 0.25 = worse than a coin-flip). **Log-loss 0.852** — the confident tail is the
cause, exactly as the decile table shows:

| claimed bucket | n | pred | realised |
|---|---|---|---|
| [0.00,0.50) | 48 | 0.36 | 0.50 |
| [0.50,0.55) | 18 | 0.51 | 0.56 |
| [0.55,0.60) | 9 | 0.57 | 0.22 |
| [0.60,0.65) | 9 | 0.62 | 0.22 |
| [0.65,0.70) | 7 | 0.66 | 0.57 |
| [0.70,0.80) | 8 | 0.77 | 0.75 |
| **[0.80,0.90)** | **27** | **0.83** | **0.41** |
| [0.90,1.01) | 6 | 0.93 | 0.50 |

The miscalibration lives almost entirely in the **≥0.80 buckets** (n=33, realised 42.4%) — and 28 of
those 33 quotes carry `win_rate_source=backtest`, i.e. the substrate **quarantined on 06-12**, and 21
of 33 are vol-mode. The fabricated ≥0.80 quote is still reaching the sizer. The low buckets are
*under*-confident (0.36→0.50), which is harmless. **All the damage is the overconfident tail.**

## 4. Conviction-vs-outcome by raw score — inverts at the very top

`-3→1.00(n2) · -1→0.17(n6) · 0→0.50(n40) · 1→0.57(n37) · 2→0.37(n27) · 3→0.47(n19) · 4→0.41(n27) ·
5→0.62(n8) · 6→0.42(n12) · 7→0.67(n6) · 8→0.29(n7) · 9→0.67(n6) · 10→0.00(n3) · 11→0.33(n3) · 12→0.00(n1)`

The slope is noisy-flat through the middle and then **collapses at the top: raw 10/11/12 → 0% / 33% /
0%.** The rubric's maximum scores are its worst predictor. **Provenance cap:** all raw-≥9 calls (n=13,
realised 38.5%) are **pre-freeze** — 0 from rubric_version 2026-06-12. We are grading the rubric era the
freeze already replaced.

## 5. Expectancy + fractional-Kelly gate

| Tier | mean P&L | payoff | half-Kelly |
|---|---|---|---|
| HIGH | −2.44 | 0.72 | 0.0 |
| MEDIUM | +0.10 | 0.95 | 0.013 |
| LOW | −0.73 | 1.00 | 0.0 |
| DROP | −3.70 | 0.57 | 0.0 |

Even on expectancy, HIGH (−2.44) < MEDIUM (+0.10). **Kelly live-activation gate: `ADVISORY_ONLY`** —
n=23 closed < 30 floor (it is incidentally monotone HIGH≥MED≥LOW on this n, but all fractions are
≤0 / floored). The win-rate ladder stays the live sizer; do **not** flip signal-confluence-quant /
risk-monitor to Kelly. (Expectancy here is partly RV-proxy-contaminated via the vol rows — advisory.)

## Verdict

The rubric is honest in the middle (accumulation, dealer-positioning, bullish-flow hit-rates land
within tolerance) and **lies in two reproducible places: (1) the ≥0.80 vol quotes (earnings_vol,
high_iv_rank) — BH-surviving, substrate-sourced, leaking to the sizer; (2) the top of the conviction
ladder, where HIGH/raw-≥9 invert because the rubric awards top conviction to a negative-selection short
book.** And the most expensive read is the quiet one: **`bearish_flow` is calibrated-but-beta (−21.7pp)
— it passes the calibration test and still loses money to a free index short.** None of this is
actionable above P1: the inversion evidence is entirely pre-freeze, and the frozen rubric (§Phase 5)
has produced **zero** HIGH/MEDIUM calls to grade.

**Output:** `phase_3_calibration.jsonl` · `phase_3b_regime.jsonl`.
