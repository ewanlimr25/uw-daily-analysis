# Phase 7 — Recommendations (propose-only · 2026-05-30)

Every item cites phase + datum. **No edits applied.** The C20–C25 method upgrade changed which
findings survive, so this list also **re-grades the 2026-05-29 recommendations**.

## ‼️ Provenance verdict: NO P0 qualifies this run (C23)

All **365 decided rows are legacy/reconstructed citations** (envelope rows window_open) and the
dataset is a **single UPTREND regime**. Per C23, **P0 requires verbatim-envelope provenance at the
cited N and ≥1 regime** — neither holds. **The 2026-05-29 run shipped three P0s; under the corrected
method none of them qualify as P0.** Everything below is **P1 or P2.** This is the headline process
finding: *the data cannot support an act-before-next-session change yet.*

---

## P1 — clear improvement (not act-before-next-session)

### P1.1 — The long book is negative-edge beta; lean to short-selection + dealer_positioning
- **What:** Surface **benchmark-excess** (realised − SPY same-window) in the daily/weekly report and
  in `signal-confluence-quant`'s sizing logic. Lean the book toward the short engine and the
  least-beta long class; treat generic long flow as beta until it clears the SPY base rate.
- **File:** `.claude/agents/signal-confluence-quant.md`, `.claude/agents/risk-monitor.md`, report templates.
- **Phase / Data:** Phase 3d — BOOK-long 58.0% vs **SPY-long 80.2% = −22.2pp**; BOOK-short 39.7% vs
  SPY-short 20.0% = **+19.7pp**. Every long class has negative excess (dealer −7, bullish −20,
  dark-pool −21); only shorts (+21) and hedges (+33) beat their benchmark.
- **Priority:** P1 (single regime caps it below P0). **Risk:** the −22pp is partly structural
  (low-vol index drift vs single-name variance) — don't over-rotate; the actionable core is *stop
  treating long flow as alpha and start measuring it against SPY.*

### P1.2 — Cap the ≥0.80 win-rate quotes (supersedes 05-29 P0.1's class floors)
- **What:** Cap *quoted* `win_rate` where claimed ≥ 0.80 toward the realised ~0.55–0.62. Do **not**
  use the 05-29 class-specific floors (dark_pool ≤0.55 etc.) — they were fit to **close-only**
  outcomes that no longer hold (dark_pool realised 63%, not 51%).
- **File:** `.claude/agents/signal-confluence-quant.md` (win-rate cap block).
- **Phase / Data:** Phase 3 C25 reliability diagram — the **≥0.90 bucket (n=38) realises 53%**, the
  0.80–0.90 bucket (n=21) realises 62%. The lie is **localized to the high-claim tail**, not
  class-specific. Brier 0.316 / log-loss 1.030 are dominated by this tail.
- **Priority:** P1 (was P0; single regime + the magnitudes shifted under C20). **Risk:** none material — capping demonstrably-overconfident quotes only tightens sizing.

### P1.3 — Raise the HIGH tier cut 10 → 9 (the one 05-29 schema rec that survives)
- **What:** Lower HIGH cut to score ≥ 9.
- **File:** `signal-confluence-quant.md` tier table + embedded rubrics in `daily-analysis.md`/`weekly-analysis.md`.
- **Phase / Data:** Phase 5 — score-9 cohort realises **79% (n=14)**; the ≥9 HIGH bin realises
  **77.4% (n=31)** vs MED 50.6%, a +26.8pp gap (Phase-3 Q5 corroborates: score ≥7 = 69.6%).
- **Priority:** P1-pending-holdout — **holdout has 0 resolved HIGH calls**; re-confirm ~2026-06-12.

### P1.4 — Widen the event_risk gate window for the swing horizon
- **What:** Extend event_risk from ~T+2 to the full swing horizon with graduated severity.
- **File:** `.claude/agents/risk-monitor.md`.
- **Phase / Data:** Phase 6 (carried from 05-29, identical envelope data) — 8/29 (~28%) swing/weekly
  calls carried a high-impact event at T+3–T+5 with a no-op verdict.
- **Priority:** P1. **Risk:** over-firing in a busy macro fortnight; the graduated −0.5 mitigates.

### P1.5 — [AUDITOR] Fix the C20 price-source reference in `calibration-audit.md`
- **What:** The C20 spec says `mcp__yahoo-finance__get_historical_stock_prices` "returns
  open/high/low/close per day (verified)." **It returns close-only.** Real OHLC requires the **chart
  API the MCP wraps** (`query1.finance.yahoo.com/v8/finance/chart`), reachable via stdlib `urllib`
  (closes verified to match the MCP exactly). Update the Phase-2 text to name the chart API and ship
  the `fetch_ohlc.py` pattern as the canonical resolver.
- **File:** `.claude/commands/calibration-audit.md` (Phase 2, C20 block).
- **Phase / Data:** Phase 2 — all three yahoo MCP endpoints returned `{date: close}` (verified
  2026-05-30); the chart API returned real H/L for the same 2026 dates.
- **Priority:** P1 (auditor-method correctness; without it a future maintainer either degrades to
  close-only or wrongly tags everything `data_unavailable`).

---

## P2 — polish / needs more N

- **P2.1 — Demote the `+3 cumulative-premium-flow` rubric line.** Durable NO-INFO across both methods
  (+1.7pp at n=96, the most-cited tool). But reconstructed citations + BH-null → **P2, not P0**
  (was 05-29 P0.3). File: `signal-confluence-quant.md`. Phase 4.
- **P2.2 — Watch the fundamentals-VETO false-positive rate (C24).** 2 of 3 decided CAUTION/VETO names
  WON (67% FP-rate). **n=3 — do NOT loosen the gate** (C24 hard rule); re-measure at ~2026-06-12.
  File: n/a (monitor). Phase 6.
- **P2.3 — The MED<LOW inversion is a directional-scoring defect, not a tier-cut defect.** The rubric
  scores beta-longs in the middle and alpha-shorts low. Investigate a **long/short-split or
  excess-aware score** rather than re-binning. File: `signal-confluence-quant.md`. Phase 5 + 3d.
  Needs more data + a 2nd regime → P2.
- **P2.4 — Route directional `win_rate` away from vol structures + add `quarter` to the documented
  sizing map.** Carried from 05-29 (9 sizing false-positives). File: `signal-confluence-quant.md`. Phase 6.

---

## Re-graded 2026-05-29 recommendations (what the method change overturned)

| 05-29 rec | 2026-05-30 disposition |
|---|---|
| **P0.1** floor WR quotes to class-specific close-only levels | **→ P1.2**, re-localized to the ≥0.80 tail (dark-pool realised 63% not 51%; class floors obsolete) |
| **P0.2** swap gate tools (add `oi-trend` + `sweep-persistence`) | **RETRACTED** — both collapsed to NO-INFO under path-aware resolution; replacements don't work |
| **P0.3** demote cum-flow +3→+1 | **→ P2.1** (direction durable, but reconstructed + BH-null caps priority) |
| **P1.1** re-cut HIGH≥9/MED4–8/LOW<4 | **→ P1.3** (HIGH≥9 survives; but MED<LOW is a *direction* defect, not a cut — refined) |
| **P1.2** widen event_risk window | **→ P1.4** (carried, unchanged) |
| **P1.3** demote `term-skew` (NEGATIVE) | **RETRACTED** — term-skew flipped −13.4→+7.9pp; the sign is a vol-proxy artifact, not a tool defect |
| **P2.3** re-confirm short-vol with intraday | **Partially done** — daily OHLC now available; short-vol/pin still bleed (proxy artifact); keep watching |

## What stays validated — do not touch
- **`dealer_positioning` + `options-structure dex`** — the only class + tool durable across both
  methods (dex +15.5→+14pp; dealer 71% realised, honest). The desk's real directional engine.
- **`bearish_flow` humility** — now revealed as the book's **alpha** (+21pp excess), not just calibrated.
- **Σ-invariant 100%** (Phase 6).
- **C3 Kelly sizer stays ADVISORY** — non-monotone tier expectancy (HIGH −1.24%), robust across both runs.

## DEFER to ~2026-06-12 (this week's calls resolve) / ~2026-06-15 (LEAPs)
All component re-weights (Phase 4 method-unstable + BH-null); the HIGH-cut holdout validation; the
fundamentals-VETO FP-rate; fz C15–C18 and single-leg C19 (0 decided); LEAP calibration (all window_open).
