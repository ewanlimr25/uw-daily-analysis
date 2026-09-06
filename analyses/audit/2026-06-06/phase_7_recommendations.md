# Phase 7 — Recommendations (propose-only · 2026-06-06)

Every item cites phase + datum. **No edits applied.** This run also grades the *applied*
2026-05-30 P1 register (commit `0314100`, 2026-05-30 15:36) against its first week of live
envelopes — the audit's first **compliance-of-the-fix** pass.

## Provenance verdict (C23)

First run with a **verbatim-envelope decided subset (53 rows)** and a **second regime state**
(06-05 risk-off break). That is enough to support exactly **one P0 — a compliance leak in an
already-shipped, already-validated rule, evidenced verbatim**. All statistical re-rankings
(tool tiers, re-weights) remain BH-null on majority-reconstructed citations → P1 cap holds
for those.

---

## P0 — calibration-breaking, act before next session

### P0.1 — The 0.80 win-rate ceiling is leaking in the vol/earnings lane; enforce it (and fix the stale helper constants)
- **What:** The P1.2 absolute quote ceiling ("never quote `claimed_win_rate` > 0.80") shipped
  05-30 — but **11 post-register envelope rows quote 0.837–0.933**, all of them
  `vol_short`/`vol_long` rows in `earnings_vol`/`high_iv_rank`, quoting the raw
  `signal-backtest` rate (`win_rate_source=backtest`, n=49/89) with no cap applied. Two
  mechanical fixes: (a) state in the cap block that the ceiling applies to **every
  `claimed_win_rate` emitted into the envelope — vol and earnings lanes included**, not just
  the directional sizing path; (b) **`scripts/excess_winrate.py:n_conditional_cap` still
  caps at 0.85 (10≤n<20) / 0.90 (n≥20)** — the deterministic helper the rubric tells the
  quant to use contradicts the documented 0.80/0.80 rule (known latent risk, now realized).
- **File:** `.claude/agents/signal-confluence-quant.md` (cap block — scope language);
  `scripts/excess_winrate.py:n_conditional_cap` (+ its tests).
- **Phase / Data:** Phase 7 verification — 11/69 June envelope rows ≥0.80, **decided ones
  0-for-3** (AVGO 0.878 L, MDT 0.878 L, MU 0.837 L). Phase 3 — `earnings_vol` claimed
  *drifted up* 60.6→72.5% post-register while realising 43.8% (+28.7pp divergence, BH 🚩);
  the ≥0.90 reliability bucket realises 51% (n=39). Verbatim provenance, two regimes,
  enforcement of an already-validated rule → clears the C23 P0 bar.
- **Risk:** none material — this enforces a rule the desk already adopted; uncapped raw
  rates remain visible in `audit_trail`.

---

## P1 — clear improvement

### P1.1 — Sync `validate_decision.py` tier band to the live rubric (≥9 = HIGH)
- **What:** The live rubric (P1.3, applied 05-30) sets HIGH at score ≥9, but the validator
  still enforces ≥10, so every raw-9 call is recorded MEDIUM in the envelope.
- **File:** `scripts/validate_decision.py` (+ `schemas/decision_envelope.schema.json` if the
  band is encoded there; + the memory-noted workaround in the commands can then be removed).
- **Phase / Data:** Phase 5 B2 — five raw-9 envelope calls recorded MEDIUM; the suppressed
  raw-9 cohort went **3/4** while recorded-HIGH (≥10) envelope calls went **1/5**. Every
  future audit's tier table mis-buckets these rows until fixed.
- **Risk:** none — alignment of recorder with rule; historical envelopes stay as-is (audits
  must keep reading them with the era's band in mind).

### P1.2 — Re-tune the event_risk gate: 90% firing = zero information
- **What:** The 05-30 P1.4 widening overshot. Post-register the gate fires on **90% of
  envelope calls** (47/52, vs 62% pre-register) and its downgrades realise **exactly the
  ungated WR (43% vs 43%, n=46+7 decided — above the C24 ≥10 floor)**. Tighten the trigger
  to *named binary events inside the structure's horizon* (earnings print, FOMC, CPI, OPEX)
  with the graduated −0.5 reserved for ambient macro — so the gate ranks rather than stamps.
  **Do not remove the gate** (C24 — and note honestly: it didn't discriminate the 06-05
  break either).
- **File:** `.claude/agents/risk-monitor.md` (event_risk trigger definition).
- **Phase / Data:** Phase 6 §3 — firing 68% blended / 90% post-register; downgrade-
  effectiveness 0pp at reportable N. This is a *correction of the 05-30 P1.4* based on its
  first live week.
- **Risk:** under-firing on a genuinely event-dense week; mitigated by keeping the graduated
  ambient tier rather than deleting it.

### P1.3 — Re-assert the <0.50 ⇒ starter/skip sizing floor (first envelope-era violation)
- **What:** `LLY 2026-06-05` quoted `win_rate 0.392` and pre-risk-sized **half** — the
  ladder maps <0.50 → starter/skip. One row, verbatim, in the newest report, into a risk-off
  tape. Add the floor to the quant's pre-emit checklist (the rule text exists; the slip was
  procedural).
- **File:** `.claude/agents/signal-confluence-quant.md` (sizing checklist).
- **Phase / Data:** Phase 6 §1 — 10 sizing upgrades total: 9 known legacy (May 6–11 + W21),
  1 new envelope-era (LLY). 256/266 compliant otherwise.
- **Risk:** none — restating a live rule.

### P1.4 — Demote the `cumulative-premium-flow` rubric weight (now 3-run-durable NO-INFO)
- **What:** Reduce the rubric points wherever `uw historical cumulative-premium-flow` earns
  them (it is supplemental/arbitration evidence per the rubric — ensure it earns ≤1 and never
  arbitrates alone), and require an intent classifier (the C28 `distribution_flag`, parity /
  ex-div check per the NEE miss) before counting its premium as directional conviction.
- **File:** `.claude/agents/signal-confluence-quant.md`; `sweep-tracker.md` /
  `accumulation-hunter.md` citation language.
- **Phase / Data:** Phase 4 — most-cited tool in the book (n=136), MC −3.5pp, NO-INFO across
  three runs and both resolution methods; qualitative corroboration: the 2026-06-04 NEE
  dividend-arb false-bullish. Reconstructed-majority citations cap this at **P1** (C23);
  BH-null noted.
- **Risk:** the tool may still carry signal *within* a class the blended MC can't see;
  mitigated by demoting (not deleting) and re-testing on the verbatim subset ~06-12+.

---

## P2 — polish / needs more N

- **P2.1 — Envelope observability: store `debate_residual_confidence` as `{bull, bear}`**,
  not one scalar — the skill's debate-gate effectiveness check (bear≥bull downgrade vs
  bull-won) is structurally uncomputable today. The scalar already ranks outcomes
  (≥0.6 → 48% WR vs <0.6 → 33%, n=34) — worth instrumenting properly. Files:
  `schemas/decision_envelope.schema.json` (additive), `bull-researcher.md` /
  `bear-researcher.md` / `risk-monitor.md`. Phase 6 §3.
- **P2.2 — MED<LOW inversion = rubric-direction defect (3rd consecutive run).** The additive
  score pays for beta-long evidence (bullish_flow −17.9pp excess scores mid) and under-scores
  alpha shorts (bearish_flow +7.5pp scores low). Investigate split long/short scoring or an
  excess-aware component — after the June cohort closes. File: `signal-confluence-quant.md`.
  Phases 3d + 5.
- **P2.3 — Watch-items at n<10 (C24 floor, no action):** `cluster` gate downgrades hitting
  winners (71% WR, n=7); `vrp` mildly anti-effective (n=7); `panic` gate strongly effective
  (20% on gated, n=5) — if panic holds at n≥10 it deserves *more* weight. Phase 6 §3.
- **P2.4 — `contrarian_fade` claims (60%) vs realised (12.5%, 1/8, BH 🚩):** smallest class,
  biggest lie. Until n≥15, contrarian-scanner calls should quote the class realised band
  (~0.30–0.45), not 0.60. File: `contrarian-scanner.md`. Phase 3.

---

## Grading the applied 05-30 register (first live week)

| Applied item | Live verdict |
|---|---|
| P1.1 excess gate surfaced | **Working as designed** — no envelope up-sizing; long excess still negative (−17.2pp) but gated |
| P1.2 quote cap ≤0.80 | **LEAKING in the vol lane** → this run's **P0.1** |
| P1.3 HIGH cut ≥9 | **HOLD** — first holdout taste 0/2 (n too thin to revert); validator still mis-records raw-9 → **P1.1** |
| P1.4 event_risk widening | **Overshot** — 90% firing, zero discrimination → this run's **P1.2** |

## What stays validated — do not touch
- **`dealer_positioning` + `options-structure dex` + `dark-pool block-stratified`** — only
  class+tools durable across all three runs (dex +11pp, dark-pool +17pp; dealer 73.3%
  realised, +0.6pp calibration error).
- **`bearish_flow` honesty** (38.3 claimed / 38.6 realised) — though its excess compressed
  to +7.5pp; treat short alpha as regime-conditional.
- **The fundamentals gate** — first stage with reportable positive discrimination
  (gated 39% vs ungated 47%, FP-rate 40% on n=20). C24's worry (VETO killing alpha) is so
  far unfounded.
- **Σ-invariant 100%** (126/126) · **Kelly stays ADVISORY** (HIGH-tier expectancy −1.85%,
  3rd run non-monotone).

## DEFER to ~2026-06-12+ (June cohort + LEAPs resolve)
Component re-weights (BH-null); HIGH-cut holdout (needs ~12 more decided HIGH); pure-VETO
FP-rate (n=2); fz C15/C16/C18 (0 decided) and **C17 analyst-divergence + C28
distribution_flag — both produced first signed evidence in the hypothesized direction
(−37pp / −22pp) — first re-test priority**; single-leg C19 (no envelope fields yet); LEAP
calibration (all `leap_window_open`, earliest closes ~06-12).
