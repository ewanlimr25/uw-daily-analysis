# Phase 7 — Recommendations (propose-only)

Every item cites the phase + data point. **No edits applied** — these are patch intentions for the user or a future `apply` pass. Method caveats from Phase 2 (close-to-close resolution, no intraday range) and Phase 4 (legacy tool citations reconstructed, not verbatim) bound the confidence; the P0/P1 items are those that survive those caveats because multiple phases corroborate.

---

## P0 — calibration-breaking

### P0.1 — Floor the quoted `win_rate` to realised audit rates per class
- **What:** Cap the per-class `win_rate` *quote* (the sizing input) at the realised rate, not the in-sample backtest: dark_pool_accumulation ≤0.55, vol_surface ≤0.50, gamma_pin ≤0.40, bullish_flow ≤0.55. Keep dealer_positioning / bearish_flow uncapped (honest).
- **File:** `.claude/agents/signal-confluence-quant.md` (the win-rate cap block, currently a flat 0.69 cap).
- **Phase / Data:** Phase 3 — claimed−realised divergence: dark_pool_accumulation **−31.6pp (n=43)**, vol_surface **−33.2pp (n=34)**, gamma_pin −33.9pp, bullish_flow −18.3pp; **Brier 0.34** dominated by these overconfident quotes.
- **Priority:** P0. **Risk:** Over-tightening could under-size a genuinely strong dark-pool setup; mitigated by keeping the *raw* uncapped rate visible in `audit_trail` (already required) so risk-monitor sees what was bounded.

### P0.2 — Fix the HIGH-tier LOAD-BEARING-tool gate set
- **What:** Replace the two non-load-bearing tools in the 3-of-5 gate (`historical cumulative-premium-flow`, `insights institutional-accumulation`) with `hot-chains sweep-persistence` and `historical oi-trend`. New set: dark-pool block-stratified, options-structure dex, hot-chains sweep-persistence, historical oi-trend, insights signal-confluence.
- **File:** `.claude/agents/signal-confluence-quant.md` (HIGH-tier load-bearing-tool gate, line ~126).
- **Phase / Data:** Phase 4 — `cumulative-premium-flow` **NO-INFO (+2.0pp, n=76)**, `institutional-accumulation` **NEGATIVE (−12.6pp, n=5)**; replacements `sweep-persistence` **+19.5pp (n=28)**, `oi-trend` **+12.2pp (n=45)**. A gate satisfiable by a NEGATIVE tool can admit anti-predictive evidence at HIGH conviction.
- **Priority:** P0. **Risk:** The two new tools fire on fewer calls; monitor HIGH-tier admission rate doesn't collapse to zero.

### P0.3 — Demote the `+3 cumulative-premium-flow accretion` line to `+1`
- **What:** Cut the standalone cumulative-premium-flow award from +3 to +1; re-allocate the freed budget to a new `+2 multi-day sweep-persistence` line (sign-preserving, budget-neutral).
- **File:** `.claude/agents/signal-confluence-quant.md` (rubric component table).
- **Phase / Data:** Phase 4 — cumulative-premium-flow is the **single most-cited tool (n=76) at +2.0pp MC (NO-INFO)**; it inflates scores without separating winners. sweep-persistence variants are +19.5/+31.9pp and under-weighted.
- **Priority:** P0. **Risk:** Reduces raw scores across the board → coordinate with the tier-cut move (P1.1) so the HIGH band doesn't empty.

---

## P1 — clear improvement

### P1.1 — Re-bin tier cuts to HIGH ≥9 / MED 4–8 / LOW <4
- **What:** Lower HIGH cut 10→9, raise LOW floor 3→4.
- **File:** `.claude/agents/signal-confluence-quant.md` (tier-cut table, line ~117) + the embedded rubrics in `daily-analysis.md` / `weekly-analysis.md`.
- **Phase / Data:** Phase 5 — current cuts are **inverted** (HIGH 60.0% / MED 48.7% / **LOW 50.9%**); proposed restore monotonicity (**HIGH 64.0% > MED 50.4% > LOW 47.2%**, 13.6pp gap). Score-9 cohort realises 70% (n=10).
- **Priority:** P1 (not P0) — **holdout could not validate** (this week's reports are window_open, 0 resolved HIGH calls). Ship after this week's calls resolve (~2026-06-12) **or** in tandem with P0.3 which shifts the score distribution anyway.
- **Risk:** In-sample-only validation; re-confirm at the next audit before locking.

### P1.2 — Widen the event_risk gate window for the swing horizon
- **What:** event_risk currently fires tightly (~T+2); extend to the full swing horizon with graduated severity (e.g. −1 tier for high-impact ≤T+3, −0.5 for T+4–T+5 inside a 1–4wk swing).
- **File:** `.claude/agents/risk-monitor.md` (event_risk gate).
- **Phase / Data:** Phase 6 — missed-gate ledger: **8/29 (28%) swing/weekly calls** carried a high-impact event (NFP 06-05, AVGO 06-03) at T+4–T+5 with a `no-op` verdict — above the 20% drift threshold.
- **Priority:** P1. **Risk:** Over-firing could blanket-downgrade every swing in a busy macro fortnight; the graduated −0.5 mitigates.

### P1.3 — Investigate `options-structure term-skew` interpretation in the vol agents
- **What:** Audit how `vol-surface-scout` and `earnings-scout` read term-skew sign; it is anti-predictive as currently used. Demote term-skew-driven scored lines to advisory (0 pts) until the read is fixed.
- **File:** `.claude/agents/vol-surface-scout.md`, `.claude/agents/earnings-scout.md`.
- **Phase / Data:** Phase 4 — `options-structure term-skew` **NEGATIVE (−13.4pp, n=56)**; feeds vol_surface (80%→47%) and earnings_vol (58%→43%) miscalibration (Phase 3). vol_short realised 30.9% (Phase 2).
- **Priority:** P1. **Risk:** term-skew may be correctly read but mis-resolved by the close-only vol proxy (Phase 2 limitation) — confirm with a true IV-vs-RV check before deep surgery.

---

## P2 — polish / low-confidence (needs more N)

### P2.1 — Route directional win-rates away from vol structures (C13 hardening)
- **What:** Ensure vol_long/vol_short/condor classes never inherit a directional class's `win_rate` (caused 4+ sizing-map false flags).
- **File:** `signal-confluence-quant.md` (C13 router). **Phase/Data:** Phase 6 sizing-map — CELH/WRBY/DDOG/ABNB 05-06 sized half at directional WR 0.0. **Priority:** P2.

### P2.2 — Add `quarter` to the documented sizing map
- **What:** The rubric emits a `quarter` size bucket not in the documented full/half/starter/skip map. **File:** `signal-confluence-quant.md`. **Phase/Data:** Phase 6 — W18 MU/INTC `quarter` misflagged. **Priority:** P2.

### P2.3 — Re-confirm short-vol / pin edge with a true intraday rule
- **What:** vol_short 30.9% and 0DTE/pin 39.3% (Phase 2) may be partly a close-only-resolution artifact (a 0.5×ATR abs-move band is tight). Re-resolve with intraday high/low once a data source exists; if the bleed persists, the premium-selling / pin program needs an edge review.
- **File:** n/a (audit methodology + `zerodte_setup.py` / opex-pin logic). **Phase/Data:** Phase 2. **Priority:** P2 — **low confidence, the close-only limitation is a confound.**

### P2.4 — LEAP & `fz` (C15–C18) calibration deferred
- **What:** No LEAP call resolved (30/90D windows open) and 0 envelope `fz_context` rows resolved. **File:** n/a. **Phase/Data:** Phase 2 (LEAP all window_open), Phase 4 (fz INSUFFICIENT_N). **Action:** re-run `/calibration-audit` after **~2026-06-15** (LEAP) / **~2026-06-12** (fz) when post-entry windows complete. Keep C15–C18 advisory (0 pts). **Priority:** P2.

---

## What stays as-is (validated — do not touch)
- **`dealer_positioning` class + `options-structure dex` tool** — honest (84%→80%) and load-bearing (+15.5pp). Phase 3 + Phase 4. The rubric's best component; if anything, floor `dex` at +3.
- **`bearish_flow` honest low-claim** (42.5%→44.0%) — the desk's calibrated humility on shorts. Keep.
- **Σ-invariant + rubric-line-keyed components** — 100% compliant (Phase 6). The 2026-05-23 defect is fixed.
- **C3 Kelly sizer stays ADVISORY** — gate returned ADVISORY_ONLY (non-monotone tier expectancy; HIGH −1.52%). Do NOT flip to live (Phase 3 C3 gate).
