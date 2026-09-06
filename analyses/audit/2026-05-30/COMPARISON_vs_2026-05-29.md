# Calibration Audit — 2026-05-30 vs 2026-05-29 (what the method upgrade changed)

The user ran `/calibration-audit` yesterday (2026-05-29), then **updated the skill** (the C20–C25
method register from the 2026-05-30 meta-audit). This doc re-runs it fresh and isolates **what the
method change overturned, what survived, and what now needs re-evaluation.**

## Why the runs differ — the C20–C25 upgrade

| | 2026-05-29 (old method) | 2026-05-30 (new method) |
|---|---|---|
| Outcome resolution | **close-to-close** (degenerate price cache: O=H=L=C) | **C20** real daily OHLC, true-range ATR(14), bar-by-bar −1R-first path walk |
| Benchmark | none (calibration only) | **C21** SPY same-window same-direction base rate → benchmark-excess |
| Truth-set | `signal-backtest` quoted as point-in-time rate (**look-ahead**) | **C22** signal-backtest demoted to colour; SPY base rate is the benchmark |
| Significance | flag every |div|>10pp; N≥5 | **C23** N≥8 floor + Benjamini-Hochberg (FDR 0.10) |
| Gate audit | firing rates only | **C24** + downgrade-effectiveness, VETO false-positive rate |
| Calibration metric | Brier only | **C25** + reliability deciles + log-loss |
| LEAPs | all window_open | **C33** window_open + interim MTM (same net: unscored) |

## Head-to-head metrics

| Metric | 05-29 | 05-30 | Note |
|---|---|---|---|
| Decided (WIN+LOSS) | 328 | **365** | path-aware triggers more intraday stops/targets |
| Overall WR | 47.3% | 50.1% | — |
| Long WR | 50.0% | **58.0%** | uptrend targets tag intraday |
| Short WR | 53.8% | **39.7%** | short stops run on up-wicks the close test missed |
| Brier | 0.34 | **0.316** | + log-loss 1.030 (new) |
| HIGH / MED / LOW | 53.7 / 46.0 / 55.8 | 55.1 / 49.0 / 51.5 | inversion softened, not fixed |
| raw_score Q5 | 53.5% (flat) | **69.6%** | top scores now discriminate |
| Kelly gate | ADVISORY | **ADVISORY** | robust (HIGH expectancy negative both runs) |
| **SPY-long excess** | — *(blind)* | **−22.2pp** | the new headline |

## ⚠️ Findings that REVERSED — re-evaluate these

1. **"Shorts beat longs; book makes money on asymmetry" → "Long selection is beta; short selection
   is the alpha."** The 05-29 absolute-WR read (shorts 54% > longs 50%) becomes, under benchmark-excess:
   longs **−22pp vs SPY**, shorts **+21pp vs SPY**. A desk acting on 05-29 might lean into longs (it's
   an uptrend); the corrected read says the longs are the problem. **Biggest re-evaluation.**
2. **`term-skew` is NOT anti-predictive.** 05-29: −13.4pp NEGATIVE → "demote term-skew" (P1.3). 05-30:
   **+7.9pp**. The sign is a vol-proxy artifact (term-skew sits on vol/earnings rows resolved by an
   RV proxy that swung between runs). **Retract the term-skew demotion.**
3. **The HIGH-tier gate-tool swap doesn't work.** 05-29 P0.2 wanted to add `oi-trend` (+12.2) and
   `hot-chains sweep-persistence` (+19.5) to the gate. Under path-aware they collapse to **+0.4 and
   −2.6 (NO-INFO)**. **Retract the swap.**
4. **The dark-pool "flagship fiction" softens on calibration but hardens on edge.** 05-29:
   dark_pool_accumulation 51.2% realised, "−31.6pp, the most dangerous number." 05-30: realised
   **63.3%** (div only +13) — *better calibrated than thought* — but **−20.8pp excess** (it rode the
   tape, didn't beat it). The problem was mislabeled: it's **beta, not miscalibration.**
5. **The class-specific WR floors are obsolete.** 05-29 P0.1 floored dark-pool ≤0.55 etc. to close-only
   levels. Those levels moved (dark-pool 63%). The right fix is the **≥0.80 quote tail** (reliability
   diagram), not class floors.

## ✅ Findings that SURVIVED both methods — these are robust

- **`dealer_positioning` + `options-structure dex`** = the one honest class + the durable LOAD-BEARING
  tool (dex +15.5→+14pp). The desk's real directional engine.
- **`cumulative-premium-flow` is NO-INFO at the highest citation count** (+2.0→+1.7pp, n=76→96).
- **HIGH-tier directional expectancy is negative; Kelly stays ADVISORY** (HIGH −1.52%→−1.24%).
- **MEDIUM tier carries the book's asymmetry** (payoff 1.47 both runs).
- **Σ-points invariant 100%; sizing ~95% compliant; event_risk window too tight** (T+3–T+5 miss).
- **Raise HIGH cut 10→9** (score-9 cohort ~77–79% both runs) — outcome-driven, holds.

## 🆕 NEW findings only the upgraded method can see
- **Benchmark-excess (C21):** every long class negative, shorts/hedges positive. *The* finding.
- **Reliability diagram (C25):** the lie is the ≥0.80 bucket (realises 53–62%); the rubric is
  *under*-confident on shorts (0–0.40 bucket realises 52%). Brier-as-scalar hid both.
- **Benjamini-Hochberg (C23):** zero tools survive → the whole tool tier list is hypotheses; the
  05-29 P0 tool-surgery was statistically unsupported.
- **Gate-effectiveness (C24):** fundamentals VETO/CAUTION FP-rate 67% (2/3 won) — thin, but the
  question is now askable (05-29 could only measure firing).
- **Provenance/regime cap (C23):** **no finding qualifies P0 this run** — single regime +
  reconstructed citations. The 05-29 run's three P0s are all downgraded.

## 🐞 Auditor-method bug found while running
The updated C20 spec names `mcp__yahoo-finance__get_historical_stock_prices` as the OHLC source
"(verified)." **All three yahoo MCP endpoints return close-only.** The real OHLC is in the **chart
API the MCP wraps** (`query1.finance.yahoo.com/v8/finance/chart`), reachable via stdlib `urllib`
(closes match the MCP exactly). The meta-audit verified the *underlying API*, not the *MCP tool*.
→ **Fix `calibration-audit.md` Phase 2 to name the chart API** (Phase 7 P1.5). Without this, the
next maintainer either tags everything `data_unavailable` or silently degrades to close-only —
the exact failure C20 was written to prevent.

## Net: what to re-evaluate
1. **Re-evaluate the directional thesis of the whole book** — longs are benchmarked-beta, shorts are
   alpha. Surface excess; lean short + dealer. *(P1.1)*
2. **Drop the term-skew and gate-swap edits** from the 05-29 to-do — they're method artifacts. *(retract)*
3. **Re-localize the WR-cap** from class floors to the ≥0.80 tail. *(P1.2)*
4. **Treat all tool/rubric re-weights as DEFERRED** until ~06-12 (BH-null + method-unstable + single regime).
5. **Patch the auditor's own C20 price-source reference.** *(P1.5)*
