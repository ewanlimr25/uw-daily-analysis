# Phase 0 — Scope & Inventory
**Audit date:** 2026-06-12 (Friday, pre-market — all "live" spot-checks read the 2026-06-11 EOD data export)
**Auditor stance:** buy-side PM / sell-side flow trader / market-maker quant. Edge audit, not prose review.
**Mandate:** audit `/daily-analysis`, `/weekly-analysis`, and all 16 project agents for (a) real measurable edge, (b) doing the claimed job, (c) precision — claimed edge ≈ measured edge. Propose-only.

## Independence / contamination disclosure

The "fresh opinion first" rule is observed as follows: **no file under `analyses/audit/*` has been or will be opened until Phase 5.** However, the session's project-memory index contains one-line summaries of prior audits (e.g. the 2026-06-06 P0.1 vol-lane cap leak, the C20–C25 auditor upgrade). Those one-liners cannot be unseen; every Phase 1–4 judgment is formed from the source files, live CLI output, and re-run scripts, and any place where a memory one-liner plausibly colored a judgment is flagged inline as `[memory-contamination risk]`. The agent/command files themselves embed prior-audit changelog comments (C-register citations) — these are part of the audited artifact and are treated as *claims to verify*, not as accepted findings.

## Inventory

### Commands (subjects)
| File | Size | Role |
|---|---|---|
| `.claude/commands/daily-analysis.md` | 557 lines | Post-market 2-phase fleet: Step 0 preflight/macro → 11(+1 OPEX) parallel Phase-1 agents → quant → fundamentals-gate(top-5) → bull/bear debate(top-5) → risk-monitor → report + `decision.json` + watchlist write-back |
| `.claude/commands/weekly-analysis.md` | 581 lines | Same fleet on week-range inputs; persistence-weighted rubric; intra-week thesis scorecard; GEX-advisory rolling backtest gate; weekly envelope |
| `.claude/commands/calibration-audit.md` | (out of subject scope) | The auditor itself; consumed in Phase 5 reconciliation only |

### Agents (16; opex-pin-strategist conditional — in-window for weekly this week, OPEX 2026-06-19)

Phase 1 alpha-finders (parallel): sweep-tracker, accumulation-hunter, contrarian-scanner, earnings-scout, gamma-flip-tracker, dealer-positioning-strategist, multileg-strategist, vol-surface-scout, leap-positioning-radar, sector-rotation-strategist, opex-pin-strategist (conditional).
Phase 2 (sequential): signal-confluence-quant (2a) → fundamentals-gate (2b) → bull-researcher / bear-researcher (2c) → risk-monitor (2d).

Per-agent claimed edges (full structured extraction with verbatim quotes: `p0_extraction.json` in this folder):

| Agent | Claimed edge (headline numbers found in the definition) | Cited to | Scored or advisory |
|---|---|---|---|
| sweep-tracker | "single-day sweeps ~50% news-event noise" (uncited); persistence ranking; its own scored line was REMOVED (−22pp two audits) | 2026-05-23 P0.3 | **0 points** — narrative-only unless a co-flag (accum/multileg) scores |
| accumulation-hunter | feeds the +3 conjunction line; single-leg PUT co-flag WR 61–64% +23–26pp p<0.001; insider clusters (Cohen-Malloy-Pomorski 2012) | C19 plan; CMP 2012 | **+3 (conjunction-gated to +1)** scored; insider/single-leg/distribution_flag all advisory 0-pt |
| contrarian-scanner | ±2σ pc-ratio-zscore fades; repeats the C19 PUT numbers uncited | none in-file | **−2** crowded-long deduction; fade candidates; C19 lane advisory |
| earnings-scout | IV-kink/term-skew alignment; PEAD claim (Bernard-Thomas) but own backtest **failed the gate** (hit 0.4706 < 0.55, n=17) | pead_backtest.py | **+1** BUY/SELL VOL line; PEAD advisory 0-pt NO_GO |
| gamma-flip-tracker | none — explicitly "no backtested predictive claim"; walls-as-magnet backtested **NO_GO** | gex_next_session_backtest.py | **0 points** — §2 advisory only |
| dealer-positioning-strategist | "DEX flips precede price moves" (Karsan/SqueezeMetrics, uncited); vanna squeeze 1–2wk BUY | none | **+3 daily / +2 weekly** — the largest scored line |
| multileg-strategist | "spreads more informative than single-leg" (uncited; note: contradicted by Chakravarty et al. 2004 cited in single_leg_whale.py); repeat ≥2 days | none | **+2** directional-structure line |
| vol-surface-scout | Goyal-Saretto IV percentile; Boyer-Vorkink skew (lit only); lottery fade backtested −22pp → WITHHELD | B-V 2014 | **+1** KINKED/BACKWARDATION + VRP-aligned; C6 advisory |
| leap-positioning-radar | 6-of-9 gates, balance-ratio >0.7, conviction >65/70 — all thresholds uncited | none | **+1** conviction-matrix (LEAP-only) + weekly +2 rolls; feeds +3 OI line |
| sector-rotation-strategist | "rotation = highest-Sharpe trades" (uncited); persistence ≥0.6 | none | **+1 conditional** (3 sub-gates); ETF tape advisory 0-pt |
| opex-pin-strategist | ranking formula distance×OI×GEX uncited; structure menu | none | **+1** top-5 pin (OPEX week only) |
| signal-confluence-quant | tier monotonicity HIGH 0.774 (n=31) > MED 0.54; C2 excess gate (longs −22pp beta, shorts +20pp alpha) | 2026-05-23/30 audits | owns rubric math, caps (0.69/0.80), excess/OI-opening/liquidity gates |
| fundamentals-gate | catches "distribution dressed as accumulation"; CMP 2012 insider lit (operationally blocked — Finnhub insider endpoints empty) | CMP 2012 | tier_adjustment 0/−1/VETO (a gate, not points); fz_context advisory |
| bull/bear-researcher | none (by design — disconfirmation, residual confidence bins 0.55–0.95) | n/a | debate gate: bear ≥ bull → −1 tier in 2d |
| risk-monitor | gate stack (9 gates); event-risk gate history: fired 90% w/ zero discrimination, re-scoped 2026-06-06 | own audits | applies −1-tier gates + watchlist write-back (the ONLY writing agent) |

### Scored-vs-advisory map (the honesty boundary)

**Scored (daily rubric):** +3 DEX/vanna · +3 accumulation-conjunction (→+1 unconfirmed) · +2 signal-confluence ≥4 · +2 multileg directional · +1 OI-trend BUILDING · +1 cum-flow intent-screened · +1 conviction-matrix (LEAP-only) · +1 sector-leader (3-gate conditional) · +1 earnings BUY/SELL VOL · +1 KINKED/BACKWARDATION · +1 OPEX pin top-5 · deductions −2 crowded / −3 flow_conflict / −1 lite / −1 cluster / −3 regime.
**Weekly deltas:** OI BUILDING +3 (vs +1), DEX +2 (vs +3), +2 LEAP rolls, sweep line removed in both.
**Tier cuts:** ≥9 HIGH / 7–8 MED / 3–6 LOW / ≤2 drop — **flagged in-file as in-sample-only, "re-confirm ~2026-06-12"** (this audit is the named re-confirmation vehicle).
**Sizing:** win-rate ladder (≥0.70 full / 0.50–0.70 half / <0.50 starter-skip) + three downgrade-only guards (C2 market-excess, C4 OI-opening, C12 liquidity floor) + N-caps (0.69 n<10; 0.80 absolute) + risk-monitor's 9-gate stack.

**Advisory (0 rubric points, must stay out of `calls[]` scoring):** §2 next-session GEX map · §2a 0DTE premium-selling (`zerodte_setup`, the only *validated*-labelled advisory) · single-leg whale C19 · fz lanes (breadth, squeeze/RS funnel, fz_context, insider clusters C15–C18) · ETF flow tape · distribution_flag C28 · expectancy lens C31 · PEAD C7 · 52w-high C8 · lottery fade C6 · Kelly C3 · VRP/term-slope scalers C5/C9 · DP price-level invalidation anchors C34.

### Scripts (15, stdlib-only; 197 unit tests — re-run this morning: **all green**)

| Script | Role | Embedded edge claim / gate |
|---|---|---|
| excess_winrate.py | C12 floor + C2 excess gate + N-caps | floor $5/$50M-ADV; caps 0.69(n<10)/0.80 absolute; excess ≤0 → half, ≤−0.10 → starter |
| oi_opening.py | C4 opening gate | ΔOI ≥20% of day volume; Pan-Poteshman 2006 |
| single_leg_whale.py | C19 research harness | GO if n≥20 ∧ WR≥0.60 ∧ excess≥0.05; PUT tier-1 claim WR 63.5% +26pp p<0.001 (n=266) |
| gex_next_session_backtest.py | §2 advisory honesty gate | H1 vol / H2 walls-magnet vs 50%; last verdict NO_GO_NO_EDGE |
| zerodte_setup.py | §2a validated stack | open-entry short-straddle ~+0.45%/day, 83–97% win (no vol shock in sample) |
| pead_backtest.py | C7 gate | needs hit>0.55 n≥10; measured 0.4706 (n=17) → NO_GO |
| proximity_52w_backtest.py | C8 gate | needs ≥10pp split n≥15; measured 4.2pp → NO_GO |
| kelly_sizing.py | C3 advisory sizer | LIVE only on tier×expectancy monotone n≥30 |
| vol_regime_scaler.py | C5/C9 advisory scalers | LIVE only on tercile-monotone WR n≥30 |
| insider_classify.py | C10 CMP-2012 classifier | shipped; Finnhub insider endpoints currently empty |
| finnhub_enrich.py / fz_enrich.py / fred_macro.py / _env.py / validate_decision.py | enrichment, macro, env, envelope validator | validator enforces Σpoints==raw_score, tier≤band, VETO⇒skip, kelly∈[0,1] |

### Schema
`schemas/decision_envelope.schema.json` versions 1.0/1.1/1.2; advisory blocks (`next_session_gex`, `next_session_0dte_setup`, `breadth_cross_check`, `fz_context`, `distribution_flag`) are top-level / per-call **non-scoring** fields by construction; `additionalProperties:false` throughout; `debate_residual_confidence` enum-pinned to the five bins.

## Historical test window

- **Daily reports:** 31 runs, 2026-04-30 → 2026-06-11. **Envelope era (machine-resolvable): 2026-05-25 → 2026-06-11 (14 envelopes).** 2026-04-30 → 05-22 is prose-only (reconstructed-citation provenance — capped evidence weight).
- **Weekly reports:** W18–W23 (6 runs); envelopes W22–W23 only.
- **Era caveat for outcome math:** envelopes 2026-05-30 → 06-05 record raw-9 calls as MEDIUM (validator band was stale then); tier-keyed analysis on that span must band by `raw_score`, not recorded tier. `[memory-contamination risk: this fact came from the memory index; it will be independently re-verified against the envelopes in P3 before any number relies on it.]`
- **Regime caveat (structural):** the entire window is essentially one UPTREND regime — every internal validation in P3 inherits single-regime confounding. No internal test this audit runs can cure that; it can only be labelled.

## Preliminary cross-cutting red flags from extraction (to be tested in P1–P3, not yet findings)

1. **Advisory lanes carry precise edge numbers** (C19's "WR 63.5%, p<0.001" appears verbatim in 3 agent files, twice uncited) — 0-point discipline holds in the schema, but the prose pushes confidence the rubric doesn't license.
2. **Uncited micro-thresholds everywhere:** balance-ratio 0.7, confidence 65/70, multileg_ratio 0.3, front-IV 1.05/1.10, ZGL ±5%, ≥30% OI shift, VIX_SPIKE 2.0 — none carry derivations. Some are harmless heuristics; the ones that gate scored lines are not.
3. **Phase-1 agents have no explicit no-write rule** in their definitions (risk-monitor is the only authorized writer). A known prior incident (2026-06-05 W23) had two Phase-1 agents writing reports unprompted. Live spot-checks in P2 will therefore carry explicit no-write instructions, and the plan will likely propose a standing hard rule.
4. **cum-premium-flow contradiction:** flagged NO-INFO (−3.5pp MC, n=136) yet still: a rubric +1, a 3-of-5 load-bearing-gate member, the C11 conjunction confirmer, the tie-breaker input, and a required tool in 4+ agents.
5. **`uw insights signal-confluence` triple role** (entry gate, +2 scored line, LB-gate member) — if the tool is a composite of the same DP/OI/flow inputs, this is structural double-counting (P1 hunter probing live).

## Phase plan & deliverables
P0 (this file) → P1 `phase_1_command_methodology.md` → P2 `phase_2_agent_audit.md` (**pause for review**) → P3 `phase_3_internal_validation.md` → P4 `phase_4_external_evidence.md` → P5 `phase_5_reconciliation.md` → P6 `plan.md` (**pause**). Evidence sidecars: `p0_extraction.json` (this phase).
