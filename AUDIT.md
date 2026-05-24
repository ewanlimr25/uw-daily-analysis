# uw-daily-analysis — Capability Audit
_Audited: 2026-05-23 · Perspective: options trader / hedge fund PM / MM_

Rubric — **Impact:** CRITICAL/HIGH/MEDIUM/LOW/NICE · **Effort:** S(<1d)/M(1–3d)/L(1wk+) · **Edge:** A=alpha R=risk O=operational. Siblings: `claude-trading-agents`, `stock-deep-dive` (both `/Users/ewan/Development/`).

## 1. What this repo does well
- **Deepest microstructure engine of the three.** One consolidated `uw-pp` MCP server (`mcp__uw-pp__*`, ~58 tools): sweep persistence, stratified dark pool, dealer GEX/DEX/vanna, IV term structure, VRP, OI rolls, OPEX pin, LEAP positioning. Nothing in the set rivals the signal breadth.
- **Only outcome-driven calibration loop.** `/calibration-audit` (`.claude/commands/calibration-audit.md`) resolves past calls path-aware (±1R), Brier-scores conviction, and tier-ranks tools (LOAD-BEARING/SUPPORTIVE/CONFOUNDED/NO-INFO/NEGATIVE). This is the gold standard the siblings lack.
- **Mechanical, non-discretionary gating.** Regime / VRP / front-end-IV panic / correlation-cluster (≥0.70) / sector-rotation gates are *scored*, not narrated (`agents/risk-monitor.md`, `signal-confluence-quant.md`). Removes the discretion that quietly inflates sizing.
- **Win-rate-grounded sizing with sample-size caps** (`historical_signal_backtest`, n<10→.75 / <20→.85 / ≥20→.90, never 1.00) — the most defensible sizing logic in the set.
- **Closed feedback loop:** top-5 conviction names written to `conviction_<date>` watchlist; next day's `watchlist_alerts` flags adverse-flow exits.

## 2. Adopt from sibling repos

> **Status: all five rows applied 2026-05-23.** Finnhub fundamentals via `scripts/finnhub_enrich.py` + `fundamentals-gate` agent (Phase 2b); bull/bear debate via `bull-researcher`/`bear-researcher` (Phase 2c); decision envelope via `schemas/decision_envelope.schema.json` + `scripts/validate_decision.py` (Step 9/10), and `/calibration-audit` Phase 1 now reads it; FRED macro via `scripts/fred_macro.py` in Step 0 (`macro_snapshot` + `event_risk`); `/stock-deep-dive` hand-off on the top-2 (Step 8.5 / §9).

| From | Capability | Why it matters here | Impact | Effort | Edge |
|------|-----------|---------------------|--------|--------|------|
| claude-trading-agents (**FINNHUB**) | Fundamentals filter on HIGH-conviction names: earnings-surprise history, FCF/leverage, insider MSPR, **company-news catalyst stacking** (`dataflows/fetch_finnhub_fundamentals.py`, `fetch_insider_sentiment.py`, `fetch_finnhub_news.py`) | The repo is fundamentally blind. Dark-pool "accumulation" into a name that's about to miss earnings with deteriorating FCF is frequently smart-money **distribution/hedging**, not buying. Cross-referencing an insider-buy cluster + a real catalyst with the UW flow is exactly how a desk separates conviction flow from exit flow. This is the FINNHUB play and it changes expectancy on a whole signal class | CRITICAL | M | A·R |
| claude-trading-agents | Bull/bear adversarial debate on the top-5 names only (`bull-/bear-researcher.md`, 1–2 rounds) | Confluence is **additive** — agreeing signals stack (`+3 DEX +3 accumulation +3 premium flow`) with no agent tasked to kill the trade. Crowded names score highest precisely when they're most consensus. A bounded bear rebuttal before sizing is the missing disconfirmation step | HIGH | M | R |
| claude-trading-agents | Pydantic decision envelope per conviction call (`schemas.py: FinalDecision`) | Output is markdown, so `/calibration-audit` Phase 1 must **re-parse prose** to resolve outcomes — fragile and the weakest link in an otherwise rigorous loop. A structured envelope makes outcomes machine-resolvable and the watchlist programmatically tradeable | HIGH | M | O |
| stock-deep-dive | FRED macro + forward catalyst calendar feeding Step 0 (`phases/phase-6-macro.md`) | `risk_market_regime` gives a label, not a calendar. A swing book sized Tuesday with CPI Wednesday carries un-priced event risk. FRED is free | HIGH | S | R |
| stock-deep-dive | Auto hand-off of top-N names to `/stock-deep-dive` | The fleet is breadth-first and stops at one report row per name. The two repos already share the Phase-1/Phase-8 agents, so the depth drill-down is a near-zero-integration add | MEDIUM | S | O |

## 3. Shared infrastructure to extract
- **The shared UW layer already exists — it's `uw-pp`.** This repo and `stock-deep-dive` both consume the *same* single consolidated server (`mcp__uw-pp__*`, ~58 tools, binary at `/Users/ewan/printing-press/library/unusual-whales/unusual-whales-pp-cli-mcp`), which replaced a legacy 11-server split for speed and token savings. So there is no "server standardization" left to do between those two — they're already aligned. The real shared-infra move is to make `claude-trading-agents` the **third consumer** of `uw-pp`; it currently uses no UW data at all. Trade-off: adds the UW dependency/quota to a repo that's self-contained on Finnhub/yfinance, but it's the only path to options data there.
- **Sizing/conviction logic is shared in spirit but split by language.** This repo encodes the win-rate→size mapping in prompt rubrics; `claude-trading-agents` has it in `kelly.py`. They can't share a package (markdown vs Python). The portable artifact is the **rubric itself** — publish this repo's sample-size-cap table as the canonical sizing rubric the others copy.
- **Net-new shared gap: short-interest + borrow-rate feed.** None of the three has it (see §4). If added, it belongs behind the shared UW/Finnhub layer so all three consume one source.
- **Do not extract** the calibration command as a "library" — it's tightly coupled to this repo's report schema. Better to export the *methodology* (already documented in `calibration-audit.md`) than the implementation.

## 4. Missing capabilities the trader desk would want
**CRITICAL — Fundamental blindness on the names being sized.** Detailed in §2. A flow engine with no earnings/FCF/guidance context will repeatedly size into smart-money exits dressed as accumulation. This is the one gap that materially dents expectancy.

**HIGH — Short interest + borrow rate.** Squeeze setups and hard-to-borrow flags are core to interpreting bullish flow (a sweep into a 30%-SI, HTB name means something very different than into a liquid mega-cap). Not present in the `uw-pp` tool catalog. Genuinely missing and directly flow-relevant.

**MEDIUM — Book-level greeks aggregation.** Per-name GEX/DEX is rich, but there's no net delta/gamma/vega across the recommended conviction book. A desk wants to know its aggregate vol exposure before market open, not just per-ticker.

**MEDIUM — Hard macro calendar.** Has regime, lacks an event calendar (FRED fixes it, §2).

**LOW — Post-earnings drift / IV-crush model.** `earnings-scout` handles SELL-VOL logic; a formal PEAD/crush model would sharpen the earnings sleeve but isn't load-bearing.

**Out-of-scope:** execution/slippage modeling — this is a signal generator feeding a human/OMS, not the OMS. Correct to omit.

## 5. Top 3 actions (P&L-weighted)
1. **Add a fundamentals gate on HIGH-conviction names (FINNHUB).** [CRITICAL·M·A·R] Before the watchlist write-back in `risk-monitor`, pull earnings-surprise history, FCF/leverage, and insider MSPR; **demote or veto** flow that contradicts the underlying (e.g., accumulation signal + imminent likely-miss + negative MSPR). *Edge:* removes a recurring loss pattern — trading flow that's actually distribution. *Sketch:* a Phase-1.5 enrichment agent reusing `claude-trading-agents/dataflows/fetch_finnhub_*.py`; one Finnhub key, ~5 calls/name on the top-5 only (quota-trivial).
2. **Emit a structured decision envelope and refactor calibration to read it.** [HIGH·M·O] Write a `decision.json` (à la `schemas.py: FinalDecision`) beside each `analyses/*.md`; point `/calibration-audit` Phase 1 at JSON. *Edge:* not alpha directly, but it hardens the only validated edge-measurement loop in the set — without it, calibration degrades silently as report prose drifts.
3. **Bull/bear stress-test the top-5 before sizing.** [HIGH·M·R] Insert a bounded 1–2 round debate (Phase 2.5) between the quant score and `risk-monitor`. *Edge:* counters additive-confluence confirmation bias on exactly the crowded names that score highest and hurt most when consensus breaks.
