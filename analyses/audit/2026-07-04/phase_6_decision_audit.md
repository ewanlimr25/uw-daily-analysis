# Phase 6 — Decision-Process Audit · 2026-07-04

Voice: buy-side PM post-mortem. Every effectiveness number states its decided-N; <10/arm = advisory.

## 1. Quant compliance (`signal-confluence-quant`)

- **Σ `score_components.points` == `raw_score`: 278/278 scored rows.** Provenance (agent+tool per component): complete.
- **Sizing-map violations: 1** — LLY 2026-06-05 (claimed 0.392 → implied starter, emitted half). Pre-freeze era, previously flagged; **zero violations in any post-freeze envelope.**
- **`quant_compliance_rate` ≈ 99.6%.** No drift. The 06-27 Rec-3 emission cap is verified live: the only ≥0.80 quotes post-application (3× `high_iv_rank`, 07-02) are exactly-at-ceiling caps of an uncapped 0.9207, labeled `backtest_clean`, all DROP/skip. Cap binds at emission as specified.
- **New defect (pessimistic direction): `claimed_win_rate = 0.0` emitted on two live multi_day_sweep setups** (MRVL 06-08/06-09; both later resolved, one WIN). A 0.0 quote is not a forecast — it's a substrate lookup degenerating. Corrupts the low buckets of the reliability diagram (Phase 3 §3). Hygiene fix, Phase 7.

## 2. Risk-monitor compliance — gate firing

| Gate | fired/present | rate |
|---|---|---|
| regime | 161/176 | 0.915 |
| vrp | 150/171 | 0.877 |
| panic | 155/171 | 0.906 |
| cluster | 159/175 | 0.909 |
| sector | 149/170 | 0.876 |
| fundamentals | 142/178 | 0.798 |
| event_risk | 176/184 | 0.957 |
| debate | 56/69 | 0.812 |
| rubric_regime | 76/76 | 1.000 |

**Missed-gate ledger: structurally clean.** 99/272 scored directional rows lack gate keys — **100% of them DROP-tier watch_only/skip** (66 watch_only, 33 skip), i.e. paper rows that never reach the Phase-2 gate stack because only the top-5-by-raw run 2b/2c/2d (the empty-book protocol working as documented). Zero sized or LOW+ rows miss a gate. **No agent drift; no prompt patch required.** (`risk-monitor.md` and the command docs describe exactly this behavior.)

## 3. Gate effectiveness (C24) — fired-WR vs not-fired-WR, decided

| Gate | fired WR (n) | not-fired WR (n) | Δ | Status |
|---|---|---|---|---|
| cluster | 0.404 (136) | 0.688 (16) | **−28.4pp** | OK |
| vrp | 0.417 (127) | 0.571 (21) | −15.4pp | OK |
| debate | 0.400 (35) | 0.538 (13) | −13.8pp | OK |
| panic | 0.432 (132) | 0.562 (16) | −13.0pp | OK |
| sector | 0.429 (126) | 0.524 (21) | −9.5pp | OK |
| fundamentals | 0.434 (122) | 0.485 (33) | −5.1pp | OK |
| regime | 0.442 (138) | 0.467 (15) | −2.5pp | OK |
| event_risk | 0.431 (153) | 0.750 (8) | −31.9pp | advisory (n<10 arm) |
| rubric_regime | 0.418 (55) | — (0) | — | advisory (no un-fired arm; see 3b OOR grading: protective) |

**All nine gates remain net-protective** (fired names realise lower WR than un-gated peers) — second consecutive audit with a clean sweep, now on larger Ns. The not-fired arms are small (8–33); magnitudes advisory, signs load-bearing. The `rubric_regime` gate has no counterfactual arm by construction (fires on 100% of gated-era rows) — its grading comes from Phase 3b's OOR split (fired-era OOR arm 0.25 / −21.5pp vs in-regime 0.455 / +0.6pp, n=20: **protective, actionable**).

## 4. VETO / CAUTION false-positive rate (fundamentals-gate cost)

VETO'd-but-resolved: **WR 0.50 (n=6, advisory)** · CAUTION 0.457 (n=46) · CONFIRM 0.489 (n=47). On its face a 50% veto FP rate — but n=6, and the ledger favors the gate qualitatively: the W27 MRNA VETO (COVERED_CALL-on-print-day distribution catch) and the NUVL merger-arb catch are exactly the blind-spot classes the flow engine cannot see. CONFIRM vs CAUTION separation (+3.2pp) is weak; the gate's value remains concentrated in rare, high-severity vetoes, not in the middle of the distribution. **No action at n=6; keep collecting.**

## 5. Debate-gate effectiveness

Decided rows with residuals: 16 — **bear won all 16** (bull_won arm n=0; the bull side has not out-argued the bear on any decided name in this window, consistent with a tape that punished conviction). Bear-won names realised 0.50 — the −1 debate cut is firing on names that then hit coin-flip, neither clearly saving nor taxing. Effectiveness ungradeable without a bull-won arm; **advisory, no action.** Premium-era residual baseline recorded for the model transition: bull mean 0.589 (σ 0.049, range 0.55–0.65), bear mean 0.705 (σ 0.108), n=33 — note the bull residuals are visibly binned at {0.55, 0.65} (anchoring signature, W27 records "0.55-binned" self-flags).

## 6. Agent-prompt drift

**None detected.** Quant: 1 pre-freeze violation, 0 post-freeze. Risk-monitor: all misses structural (top-5 protocol). Phase-1 agents: no unprompted file writes since the W23 incident; the no-file-writes hard rule remains in every spawn prompt and has still **never been load-tested on a sonnet-majority Phase 1** (pins applied 2026-07-03; zero post-pin runs — see Phase 7 model-transition section).

Machine-readable: `phase_6_decision_audit.jsonl`.
