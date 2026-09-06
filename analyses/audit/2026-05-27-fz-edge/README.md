# Audit — `fz` (Finviz CLI) edge assessment

**Date:** 2026-05-27 · **Auditor lens:** options trader / market maker / hedge-fund PM
**Subject:** the newly-installed `fz` CLI (`finviz-pp-cli` v1.0.0, binary at `/Users/ewan/.local/bin/fz`)
**Question:** where can `fz` add edge to the `/daily-analysis`, `/weekly-analysis`, and `/calibration-audit` workflows, and what is the strict factual basis for each addition?

> **Why this audit exists.** `fz` is a free, no-auth Finviz screener/fundamentals CLI that
> exposes **exactly the data this repo's own `AUDIT.md §4` flags as "genuinely missing"** —
> short interest, days-to-cover, float, institutional/analyst positioning — plus three
> aggregations Finviz.com does not expose (`insider-clusters`, `breadth`, `quote-drift`).
> This repo is the deepest options-microstructure engine of the three siblings but is
> **fundamentally and structurally blind** to the non-flow context that tells you whether
> a sweep is conviction or an exit. `fz` is the cheapest way to close that blind spot.

## Files in this audit

| File | Purpose |
|------|---------|
| [`01-fz-capability-map.md`](./01-fz-capability-map.md) | What `fz` is — every command, the 84 quote fields, what it is **not** (honest limits). Verified by live calls. |
| [`02-edge-analysis.md`](./02-edge-analysis.md) | Per-workflow edge: 8 findings (E1–E8), each scored Impact/Effort/Edge with the factual basis and the desk objection it answers. |
| [`03-implementation-plan.md`](./03-implementation-plan.md) | Phased plan that respects this repo's calibration discipline: advisory-first (0 rubric points), promote to scored gates only after `/calibration-audit` clears a hit-rate threshold. |
| [`04-evidence-appendix.md`](./04-evidence-appendix.md) | Reproducible `fz` command output backing every claim (run 2026-05-27). |

## Headline finding

`fz quote <T> --agent` returns, **free and in one call**, the data the repo records as
*"Intentionally absent"* (data-sources table) and *"HIGH — genuinely missing"* (`AUDIT.md §4`):
`Short Float`, `Short Interest`, `Short Ratio` (days-to-cover), `Shs Float`, `Inst Own/Trans`,
`Insider Own/Trans`, `Recom` (analyst 1–5), `Target Price`. The single highest-value move is to
feed short-interest + float into `fundamentals-gate` (Phase 2b) and the `risk-monitor` gate stack:
**a bullish sweep into a 25%-short, 8-day-to-cover name is a different trade than the same sweep
into a clean float, and the repo currently cannot tell them apart.**

## Honest limit (read before adopting)

`fz` adds **no** options flow, greeks, dark pool, IV term structure, GEX/DEX, or OI — it cannot
replace or duplicate any UW microstructure tool. It is strictly a **fundamentals / screening /
breadth / insider** augment sitting *beside* the flow engine. Finviz short interest is the
exchange **semi-monthly settlement figure (~2-week lag)** — good for squeeze *context*, not a live
borrow signal — and `fz` does **not** provide borrow fee / hard-to-borrow status (WebSearch/Ortex
still needed for that). See `01 §"What fz is NOT"`.

## Conventions

- **Propose-only.** This audit does not rewrite working agent prompts. Adoption is the separate,
  deliberate step in `03`; new *scored* gates must clear `/calibration-audit` first (the repo's
  own discipline — `improvement_criteria.md`).
- **Severity:** CRITICAL / HIGH / MEDIUM / LOW · **Effort:** S (<1d) / M (1–3d) / L (1wk+) ·
  **Edge:** A=alpha, R=risk, O=operational (mirrors `AUDIT.md`).
- Every quantitative claim resolves to a command in `04-evidence-appendix.md`.
