# Phase 2 — Per-Agent Design + Precision Audit (FINAL)
**Date:** 2026-06-12. **Coverage:** 16/16 static (Explore deep-read + tool-wiring verification), 14/16 live (11 via subagent spot-checks on 2026-06-11 EOD data; quant / risk-monitor / fundamentals-gate run inline by the lead auditor against the production envelopes and enrichment scripts). **Deferred:** bull/bear behavioral dry-runs (low marginal value; static contract audit complete). Two session-limit interruptions occurred; all completed evidence was recovered (`p2_partial_run1.json`, `p2_recovered_transcripts.json`, `p2_run2.json`). Judge-stage drafts completed for 3 agents (dealer-positioning, leap-radar, sector-rotation — all FIX, all consistent with the lead verdicts below); remaining verdicts are the lead auditor's from static+live evidence.

---

## 0. Envelope precision battery (lead auditor, inline — all 16 envelopes, 151 calls)

| Test | Result |
|---|---|
| Σ score_components == raw_score | **151/151 clean** — the validator invariant genuinely binds |
| Final-size distribution | **full: 0, half: 12, starter: 15, skip: 54, watch_only: 69, veto: 1** — *not one full-size call in the entire envelope era*; 81% end skip/watch-only. Confirms Phase-1 F6: tier labels (7 HIGH, 20 MED) are decoupled from realized capital |
| Dead-letter rubric lines (F5) | **Confirmed**: −3 regime-conflict / −1 corr-cluster appear in `score_components` on **0/151** calls — the published rubric lines never fire as points |
| 0.80 win-rate ceiling | 23 violations, **all 2026-05-25 → 06-05** (0.837–0.933, the vol/earnings lanes); **zero violations 06-08 onward** — the leak was real and the 06-06 fix demonstrably binds now |
| Sub-0.50 sizing floor | exactly 1 violation ever (LLY 06-05, wr 0.392 → half); none since |
| Gate-verdict completeness | `debate` verdict recorded on **0/151 calls** (while `debate_residual_confidence` is set on 56 — debates run, the gate never records); 39 DROP-tier calls have no `gate_verdicts` at all; regime/vrp/panic/cluster/sector each missing on 7–11 calls |
| Fallback proxy | live: AAPL `win_rate 0.424, n=85, fallback_proxy` — n=85 exceeds the documented 30-day window; one market-wide class stat stamped across MU/MRVL/ASML (0.479, n=71 each), confirming Phase-1 F2c/d |

## 0b. Fundamentals-gate live census (inline)
`finnhub_enrich.py NVDA 2026-06-11`: metrics ✓, earnings_surprises ✓ (beat_streak), news ✓ (15), next_earnings ✓ (2026-08-25) — but **`insider_mspr: []` → `insider_signal: "unknown"`**. The ≥2-of-3 VETO logic is structurally a **2-of-2** (earnings_trend + growth/leverage) until the insider feed works; VETO is *harder* to trigger than designed. `fz_enrich.py` ✓ (short_float 1.23%, DTC 1.72, recom 1.25, squeeze LOW — advisory lane functioning).

---

## 1. Final verdict table

| Agent | Verdict | Edge assessment | Decisive evidence |
|---|---|---|---|
| signal-confluence-quant | **FIX** (role KEEP) | Discipline REAL, substrate BROKEN | Envelope discipline is excellent post-06-06 (Σ 151/151, caps/floor bind). But its two core inputs are defective: `signal-backtest` (P1 F2 — clamped windows, ±6pp pagination, no per-ticker mode, flagship class empty) and `signal-confluence` (P1 F1 re-count). C2 market-excess result not recorded in `gate_verdicts`. Fallback proxy n=85 > 30d window |
| risk-monitor | **FIX** (role KEEP) | Gate stack REAL but over-stacked + under-recorded | Debate gate verdict 0/151; event-risk T+3 threshold miscalculation (static find, HIGH); 7–11 calls missing individual gate keys; size compression: 0 full-size ever. Working: mechanical cluster bands (soft 0.664 correctly unpenalized), write-back top-5 correct w/ VETO excluded |
| dealer-positioning-strategist | **FIX (P0)** | UNTESTED + imprecise award | The **+3 line fired 06-11 for MU/MRVL/ASML with no DEX sign flip in any** (MU +27.7B→+33.5B all-positive 10d) — level scored as flip. No flip field exists in the tool (needs N dated calls). Vanna VIX leg unwired. The index flip it reported (SPY −58.1B→+9.3B) was real and exact — capability exists, trigger is unenforced. Judge: FIX/UNTESTED concurs |
| accumulation-hunter | **FIX** | REAL core, overcounted edges | Every envelope number reproduced exactly (AAPL mega buy_ratio 0.787, cum_flow +$82.8M, BUILDING×5). Defects: C11 $50M floor degenerate at mega-cap scale (0.6% MIXED imbalance confirms full +3); C28 flag misattributed on AAPL (put-close labeled call-distribution; "10k-lot 170P" = $10K teenie); retail-tier disqualifier vacuous (tier empty for all names); 5/10-day window claim is a fiction (single-day tool); conviction-matrix gate passed at confidence 15.1 (no floor) |
| earnings-scout | **FIX (P0)** | ILLUSORY as instrumented | PRIMARY gate (KINKED + kink_expiry==ER date) **structurally unreachable** (expired-bucket contamination; unweighted avg_iv). Book's only FULL-size SELL VOL (FDX) rests on an **11-contract tenor** that flips NORMAL at adjacent tenors — and vol-surface-scout's independent live pass could not reproduce it. analyst-vs-flow >2σ disqualifier non-computable. The earnings-vol opportunity set itself is real (MU/ACN/FDX kinks visible in raw arrays) |
| vol-surface-scout | **FIX** | Plausible, degenerate instrumentation | Term-structure classifier degenerate pre-event: **58/61 BACKWARDATION, 0 KINKED, kink_expiry null on every name** (pre-FOMC). PRIMARY Goyal-Saretto percentile runs on **43 of 252 days** (percentile-100 = n=43 claim). VRP-gate ambiguity materialized live (MU SELL VOL on a negative-VRP name). Quoted report numbers reproduced exactly where checkable |
| leap-positioning-radar | **FIX** | UNTESTED (n≈1 emissions) | Gates demonstrably strict (no name passed 6-of-9 tonight; SCHW/DKNG real builds failed honestly) but 4 of 9 gates unwired/mismatched: 10-day window inexpressible, roll breakdown underivable, conviction-matrix same-day classifier vs multi-week mandate + threshold conflict (agent >65 vs rubric >70), deep-dive fundamentals 401. Judge: FIX/UNTESTED concurs |
| sector-rotation-strategist | **FIX** | UNTESTED (n=2 anecdote) | persistence gate **non-binding live: 11/11 sectors ≥0.6** (9 at 1.0) — filters nothing; a **stale integer-scale threshold survives in the invalidation spec** (same bug class as the 2026-05-25 fix); dte-volume-share is market-level only (per-sector claim impossible); GICS-vs-ETF agreement disagreed 4-of-4 in fresh sample (structurally biased to "disagree"). Report numbers reproduced exactly. Judge: FIX/UNTESTED concurs |
| opex-pin-strategist | **FIX** | Mechanics REAL, gates phantom | IWM was a textbook pin (290, 0.15% away, chain-max wall). But probability gates reference a **field that does not exist**; `opex-concentration` cross-ref **empty for every liquid candidate**; agent ranking vs tool `pin_score` produce different orders with no tie-break doctrine; |gex| formula promotes anti-pins its own gate kills |
| contrarian-scanner | **KEEP** (minor fixes) | Plausible + precise | Cleanest live pass: ±2σ productive (4/24 extreme; CL z=4.51), all report numbers exact to rounding, raw-P/C vs z-score discrimination verified. Fixes: "rising z" needs a mechanical data path (dated re-calls); GOOG +2σ missed by the 06-11 report (universe coverage); scored lane one-directional |
| multileg-strategist | **KEEP** (minor fixes) | REAL (verified end-to-end) | IWM 276/274 bear put vertical decoded fully from prints; 0.3 gate productive (removes 0DTE index noise; p50=0.693). Fixes: ticker-regex dependency, `--min-premium` flag doesn't exist, SPX box/financing pollution in top prints |
| sweep-tracker | **KEEP** (narrative role; targeted fix) | n/a scored (line removed); narrative value real | Persistence materializes after layered filters (raw gate passes 20/27 but 16/20 are hedge tape — filters do the work). Fix: per-day same-direction is unverifiable from the tool (`consistency_score` = sessions/5, a misnomer); mega-cap alignment gate field-ambiguous |
| gamma-flip-tracker | **KEEP** (advisory; optional MERGE for fleet cost only) | None claimed (honest) — and the honesty is verified | Live contract fully verified: SPY FULLY_NEGATIVE/null-ZGL + QQQ ZGL 73% from spot → 5% reliability gate **necessary and binding tonight**; walls recomputed = envelope exactly. `today-gamma-flip` warning justified (locks to expired expiry). Issues are upstream tool warts (regime_description false vs own per_strike; flip-date pollution) |
| fundamentals-gate | **FIX** | REAL but degraded to 2-of-2 | Insider leg dead (census above). Otherwise functioning and recorded; NA-never-penalizes honored. Fix: restore/replace insider input (fz `insider-clusters` or Finnhub paid tier), recalibrate VETO bar while one leg is dark |
| bull-researcher | **KEEP** (contract tightening) | n/a (disconfirmation device) | No tools by design; bins ordinal/uncalibrated; no enforcement of no-invention rule; cannot re-audit quant components. Cheap, bounded, cut-only — keep |
| bear-researcher | **KEEP** (contract tightening) | n/a (the system's only adversarial input) | Symmetric to bull; residuals recorded on 56 calls. But note: its gate verdict is never recorded (0/151) — fix lands on risk-monitor |

**No REMOVE verdicts.** The weakest standalone case is gamma-flip-tracker (0-point advisory, SPY/QQQ-only) — exemplary honesty, real consumed output (§2); merging it into dealer-positioning would save fleet cost, not remove a defect.

---

## 2. Cross-agent synthesis

1. **Shared substrate defects dominate per-agent defects.** Three independent live passes hit the same `iv-term-structure` expired-bucket/unweighted-avg_iv contamination (multileg, earnings-scout, vol-surface — the last degenerating to 58/61 BACKWARDATION); two hit GEX self-contradictions (IWM, SPY: regime label vs per-strike walls); `signal-backtest` defects (P1 F2) poison every sizing decision; `signal-confluence` re-count (P1 F1) poisons every entry+score. **Four CLI-layer fixes would repair more measured imprecision than all sixteen agent-file edits combined.**
2. **The scored lines with the heaviest weights have the weakest live verification.** +3 DEX (fired without trigger), +3 accumulation (exact mechanics but degenerate $50M confirmer at mega-cap), +2 confluence (re-count), +1 sector (gate passed 11/11) — versus the *removed* sweep line and *advisory* lanes which are honestly labeled. The rubric's weight ordering is roughly inverse to demonstrated precision.
3. **Agent fences held.** No live evidence of scope encroachment between gamma-flip/dealer-positioning, sweep/multileg, earnings/vol-surface (the C13 router fence). MERGE is nowhere required on overlap grounds.
4. **Phase-1 no-write rules absent** in most agent files (one prior real incident). Cheap standing fix.
5. **Verified-exact reproduction is the norm, not the exception** — across accumulation-hunter, contrarian, dealer (index level), gamma-flip, sector-rotation, vol-surface, the *numbers quoted in reports matched recomputation exactly*. The system's failures are in **gate semantics and statistical substrate**, not in data fidelity or fabrication. That materially raises the credibility of fixing it.

## 3. Residual gaps carried to P3+
- bull/bear behavioral dry-runs (optional; static contracts audited).
- Judge drafts for 13 agents were lost to the session limit; lead verdicts above stand in (the 3 completed judges all agreed with the lead's independent calls).
- P3 must quantify: signal-backtest window-clamp share; tier-vs-outcome monotonicity re-confirmation (due today per the rubric's own ⚠); weekly scorecard inflation; backtest re-runs (single-leg, GEX, 0DTE, PEAD, 52w).
