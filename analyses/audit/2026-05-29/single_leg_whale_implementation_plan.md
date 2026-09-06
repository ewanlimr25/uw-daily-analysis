# Single-Leg Whale Edge — Implementation Plan & Signal Quality Hierarchy (MM/Trader Re-analysis)

**Date:** 2026-05-29
**Status:** SHIPPED — `uw options-flow single-leg` live in the `uw` CLI; daily/weekly integration wired; registered advisory criterion **C19** (0 rubric points pending 60-day cross-regime validation).
**Inputs:** `single_leg_whale_edge_analysis.md` (methodology), `single_leg_whale_backtest_report.md` + `single_leg_whale_backtest.json` (empirical evidence).

---

## 1. Re-reading the "Signal Quality Hierarchy" as a trader / market maker

The original research ranked single-leg prints by *execution mechanics* (electronic > floor > auction; opening > closing). The backtest then told us which of those mechanics actually pay. Read through a desk lens, the hierarchy is **not** "which print is most aggressive" — it is **"which print reveals a counterparty who knows something the tape doesn't yet."** Four scenarios, ranked by where the edge actually lives:

### Tier 1 — the informed contrarian put (THE edge)
**Setup:** single-leg, ask-side, **PUT**, `size/OI ≥ 2` (or floor/negotiated block), `DTE ≤ 30`, premium ≥ $500K, common stock, in a **non-collapsing tape**.
**Backtest:** WR **63.5%** (n=266, p<0.001), **+26pp** over the same-direction SPY baseline; floor/neg variant 61.0% (n=328, p<0.001).

**Why a trader gets an edge here:**
- `size/OI ≥ 2` means the position is being **built from scratch** — this is Pan-Poteshman "buy-to-open," the only option flow that carries return predictability. A roll or a close (`size/OI < 0.5`) carries none.
- `DTE ≤ 30` means the buyer is paying maximal theta to be right **soon** — they are not hedging a book, they are pricing a **specific near-term catalyst** (earnings miss, guide-down, regulatory/FDA, channel check). Theta is the cost of conviction; nobody burns it for vague insurance.
- A **put** that is right 63.5% of the time *while SPY rises 62.5% of days* is swimming against a 25-point headwind. That residual, regime-orthogonal hit-rate is the cleanest fingerprint of stock-specific information in the entire dataset.

**Market-maker mechanics (why it can self-fulfil):** the whale buys puts → the dealer **sells** puts → the dealer is **short puts = long delta**, and hedges by **shorting the underlying**. Into a ≤30-DTE clock, if spot drifts toward the strike the dealer's short-gamma forces **more** selling (negative-gamma feedback), and rising put IV (vanna) deepens the hedge. The dealer's hedging *amplifies* the very move the informed buyer predicted. That is the microstructure reason the signal has follow-through rather than mean-reverting.

**Tradeable expressions:** short the underlying / long put / put debit spread / bear call spread on the named ticker, ~1–5 session horizon. The signal is **directional-bearish on a single name**, not a vol trade.

### Tier 2 — opening put, wrong horizon (context, edge decayed)
**Setup:** PUT, `size/OI ≥ 2`, but **DTE > 30**.
**Backtest:** 56.1% in the ≥2 bucket overall, but the 31–90 / 91+ DTE strata collapse to ~49% / ~47% — **no edge**. A long-dated opening put is portfolio insurance / macro hedge, not a stock-specific bet. **Context only, never sized.**

### Tier 3 — the call lane (beta, not alpha — regime-conditioned)
**Setup:** any single-leg **CALL**.
**Backtest:** 52.8% in a bull tape — but **−9.7pp vs the 62.5% SPY baseline**. The institutions printing big calls in an up-tape are **riding the move, not front-running it**. Buying behind them underperforms just holding the index.
- This asymmetry is **regime-specific, not structural.** In a bear/mixed tape the symmetric *informed-call* edge is plausible but **unmeasured** — so the classifier emits `CALL_UNVALIDATED` (context only) outside a bull regime, and `CALL_BETA_NOEDGE` inside one. We do **not** trade calls off this signal until a bear window validates them.

### Tier 4 — the anti-signals (actively fade / avoid)
- **`size/OI < 0.5` (closing/rolling):** 43.7% — *below* a coin flip. Whatever direction it implies, the next session leans the other way. Treat as **AVOID**, and as mild evidence *against* a same-direction thesis.
- **Aggressive call-chasing in a bull tape** (`call`, `size/OI ≥ 2`, `DTE ≤ 30`, bull): `CALL_BETA_FADE_CHASE` — a crowding tell. Useful to **veto** a bullish conviction that is leaning on "big call flow," and as a fade candidate, not a long.

**The one-line desk summary:** *the edge is the lonely short-dated put built from nothing against a rising tape; everything else is either beta, insurance, or exit liquidity.*

---

## 2. Where and when this triggers in the daily / weekly workflow

### Daily (`/daily-analysis`, post-close)
- **Trigger point:** Phase 1, **after Step 0 sets the directional regime** (the classifier needs the regime to grade the call lane). Runs once on the session's All-Options parquet:
  `uw options-flow single-leg --regime <step0_regime> --json --quiet`
- **Consumers:**
  - **`accumulation-hunter`** — a Tier-1 opening/floor PUT on a name that *also* shows dark-pool **distribution** (`dark_pool_block_stratified`) is the strongest bearish co-confirmation in the dataset. The agent surfaces it as a bearish co-flag (advisory).
  - **`contrarian-scanner`** — a Tier-1 short-DTE put aligns with a rising put/call-ratio crowding read for a single-name short thesis.
  - **`risk-monitor` / debate** — `CALL_BETA_FADE_CHASE` is a **veto flag** against any bullish conviction that rests on "large call flow"; `CLOSING_ANTISIGNAL` weakens a same-direction thesis.
- **Surfacing:** Tier-1 names listed under the Swing horizon with `action`, `size/OI`, `DTE`, premium, `base_win_rate`, `market_excess_pp`. **Advisory — 0 conviction-rubric points.**

### Weekly (`/weekly-analysis`)
- **Persistence:** does a name throw **repeat** Tier-1 opening-put prints across the 5-day window? Repeat informed positioning > one-off.
- **OOS scoreboard:** track the realized next-session hit-rate of each week's Tier-1 signals — this is the live out-of-sample accrual toward C19 graduation.

### Grading (criterion C19)
- **Advisory, 0 rubric points** until rolling OOS WR holds **≥ 58% over ≥ 60 trading days spanning ≥ 2 regimes** (the backtest is a single bull window — see caveats in the report). On clearing, promote the Tier-1 opening/floor-put signal to a scored bearish line in `accumulation-hunter` / `contrarian-scanner`; the call side stays advisory until a bear window measures it.
- Calls are **never** auto-scored from this signal in any regime until separately validated.

---

## 3. Evidence (concrete backing)

From `single_leg_whale_backtest_report.md` (32 D→D+1 pairs, Mar–May 2026, SPY up 62.5% of days):

| Signal | n | WR | Excess vs SPY | p | Verdict |
|---|---|---|---|---|---|
| Puts, size/OI≥2, DTE 0–30 | 266 | **63.5%** | **+26pp** | **<0.001** | GO (Tier 1) |
| Puts, size/OI≥2, DTE 8–30 | 68 | **66.2%** | +28.7pp | 0.005 | GO (small n) |
| Floor/neg puts, DTE≤30 | 328 | **61.0%** | +23.5pp | <0.001 | GO (Tier 1) |
| Puts, size/OI≥2 (all DTE) | 503 | 56.1% | +18.6pp | 0.004 | marginal (Tier 2) |
| Calls (any) | 1656 | 52.8% | **−9.7pp** | 0.011 | NO — beta (Tier 3) |
| size/OI<0.5 (closing) | 378 | **43.7%** | — | 0.99 | anti-signal (Tier 4) |

The tier classifier encodes exactly these strata. `internal/analysis/singleleg_test.go` pins the hierarchy (opening-put-prime, floor-block, closing override, DTE decay, call beta/unvalidated, gating) so the mapping cannot silently drift.

---

## 4. Implementation (what shipped)

**`uw` CLI (Go, `/Users/ewan/printing-press/library/unusual-whales`):**
- `internal/analysis/singleleg.go` — pure, testable hierarchy: `SizeOIRatio`, `SizeOIBucket`, `DTEBucket`, `ConditionClass`, `NormalizeRegime`, `ClassifyTier(WhalePrint, regime) → TierResult`, `BinomP`. Encodes the backtested WR/excess/n per tier.
- `internal/analysis/singleleg_test.go` — 12 unit tests (all green) pinning the hierarchy and the binomial test.
- `internal/cli/single_leg.go` — `uw options-flow single-leg` cobra command: filters the All-Options parquet to clean single-leg ask-side ≥$500K common-stock prints, computes size/OI per print, classifies, dedups one signal per (ticker, option_type) by max premium, ranks by tier then premium, emits JSON with per-signal tier/action/win-rate + a tier-label summary + advisory note.
- Registered in `internal/cli/options_flow.go`.
- Flags: `--date --regime --option-type --min-premium --top-n --scored-only --max-tier` + inherited `--json/--compact/--select/--quiet`.

**Verification:** `go build ./...` clean; `go test ./internal/analysis/` green; binary rebuilt (the `uw` symlink resolves to it); live smoke test on 2026-05-28 data returned 488 raw → 104 deduped → 25 emitted (16 scored), top signal a real `FLOOR_PUT_BLOCK` (CONTRARIAN_SHORT, WR 0.61, +23.5pp).

**Why a Go CLI tool (not just the Python script):** the Python `scripts/single_leg_whale.py` remains the **research/backtest** harness (it owns the D→D+1 grading). The `uw` subcommand is the **production scan** the agent fleet calls inline — same parquet substrate, same filters, no extra dependency, condition-code filtering the old `top-premium-trades` lacked.

---

## 5. Integration & docs (this change set)
- `.claude/commands/daily-analysis.md` — Phase-1 single-leg-whale scan step (post-regime) + consumer routing.
- `.claude/commands/weekly-analysis.md` — Tier-1 persistence + OOS scoreboard.
- `.claude/agents/accumulation-hunter.md`, `contrarian-scanner.md` — single-leg put co-flag inputs.
- `scripts/single_leg_whale.py` docstring + `CLAUDE.md` `uw` section — point at the new subcommand.

---

## 6. Caveats / do-not-regress
1. Single bull-regime window — cross-regime validity unproven; stays advisory (C19).
2. EOD price proxy in the backtest (last `underlying_price`), not official close.
3. Next-session only — multi-day decay untested.
4. No transaction costs / underlying-move grading only.
5. Calls are anti-informative **in bull tapes**; do **not** conclude calls are structurally useless — the symmetric edge likely exists in bear regimes and must be measured before use.
