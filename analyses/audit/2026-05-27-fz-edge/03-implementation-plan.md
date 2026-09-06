# 03 — Implementation plan (propose-only)

**Governing principle (this repo's house rule):** new *scored* gates do not ship on a story. They
ship **advisory (0 rubric points) first**, get logged into `decision.json`, and are promoted to
scored only after `/calibration-audit` shows the gate has empirical edge — exactly how C6 (lottery
fade), C7 (PEAD) were withheld and C11 (accumulation conjunction) was gated. This plan honors that.
It mirrors the proven `uw` CLI + `finnhub_enrich.py` integration shape, so there is no new
architecture — only a new data source behind the existing Phase-2b enrichment + Step-0 funnel.

---

## Prerequisites (Phase 0 — operational, do first)

1. **Permission.** Add `"Bash(fz:*)"` to `.claude/settings.json` (mirrors existing `Bash(uw:*)`).
2. **Health probe.** In Step 0 preflight, run `fz doctor` / `fz --version`; on non-zero, set
   `fz_available=false` and **graceful-skip** every `fz` lane (mirrors the yahoo-broken / Finnhub-403
   skip pattern already in the repo). Never hard-fail a report on `fz`.
3. **Enrichment wrapper** `scripts/fz_enrich.py` (mirror of `scripts/finnhub_enrich.py`): given a
   ticker + date, returns compact JSON of only the gate-relevant fields. The robust extraction is
   `fz quote <T> --agent` piped to `jq` (the 84-field labels have spaces/parens, so jq is the
   safest projector):
   ```bash
   fz quote <T> --agent | jq -c '{ticker, short_float: .fundamentals."Short Float", days_to_cover: .fundamentals."Short Ratio", float: .fundamentals."Shs Float", inst_own: .fundamentals."Inst Own", insider_trans: .fundamentals."Insider Trans", recom: .fundamentals.Recom, target: .fundamentals."Target Price", rsi: .fundamentals."RSI (14)", price: .fundamentals.Price}'
   ```
   (`fz`'s own `--select` also works but only with **unquoted** dotted paths — e.g.
   `--select 'fundamentals.Short Float,fundamentals.Short Ratio'`; inner double-quotes return an
   empty object. Verified `04 §1`.) The wrapper keeps agent context small and centralizes the
   field-label mapping + freshness caveat tag.
4. **Guardrails baked into the wrapper:** tag every value `[FZ:<field> EOD <date>]`; note SI is
   semi-monthly settlement; respect 2 req/s; cap to top-5 (quota-trivial, like fundamentals-gate).

---

## Phase A — Advisory adoption (ship now · 0 rubric points · all free)

| ID | Change | File(s) | Output (advisory) |
|----|--------|---------|-------------------|
| **A1** | Add `short_float`, `short_ratio` (days-to-cover), `shs_float`, `inst_own`, `recom`, `target_price` to fundamentals-gate output for the top-5. Verdict text *gains* squeeze/analyst context; `tier_adjustment` **unchanged** (still Finnhub-driven) until B1. | `agents/fundamentals-gate.md`, `scripts/fz_enrich.py` | New fields in the Phase-2b block + `decision.json.calls[].fz_context` |
| **A2** | Log `fz breadth --group sector` in Step 0 `macro_snapshot` as `breadth_advancers/decliners/pct_green`. Cross-check vs `uw risk market-regime`; surface divergence in §6 prose. | `.claude/commands/daily-analysis.md`, `weekly-analysis.md` (Step 0) | `decision.json.breadth_cross_check` |
| **A3** | Add `fz insider-clusters --days 7 --min-buyers 2 --side buy` as a co-flag in accumulation-hunter; set `insider_cluster_present: true/false` + distinct-buyer count. **Narrative only, 0 points.** | `agents/accumulation-hunter.md` | `co_flag` field on accumulation candidates |
| **A4** | Add a squeeze + RS lane to Step 0 top-of-funnel: `fz screen --filter sh_short_o20,sh_price_o5,sh_avgvol_o500 --view ownership` and `fz screen --signal ta_newhigh`. Union into the candidate set fed to Phase-1 agents. Enforce liquidity floor server-side. | Step 0 of both commands | extra funnel rows tagged `source: fz_squeeze` / `fz_rs` |
| **A5** | Add `fz quote --select … Target Price,Recom` to bull/bear-researcher inputs for prose context (upside-to-target, consensus tilt). | `agents/bull-researcher.md`, `bear-researcher.md` | debate prose only |

Phase A is reversible, free, and cannot change sizing — it only enriches context and the envelope.

---

## Phase B — Promote to scored gates (only after calibration clears them)

Each B item is registered as a numbered improvement criterion (**C15–C18**) in
`improvement_criteria.md` with: academic/desk basis, the exact gate mechanic, and a **pass threshold
the gate must clear in `/calibration-audit` before going LIVE** (mirrors C7's 0.55 hit-rate bar that
kept PEAD NO-GO).

| ID | Criterion | Gate mechanic (when LIVE) | Promotion threshold |
|----|-----------|---------------------------|---------------------|
| **C15** | Short-interest squeeze gate (risk-monitor) | SHORT thesis into `Short Float ≥ 20%` AND `Short Ratio ≥ 5` → −1 tier (squeeze trap). LONG momentum into same → squeeze-tailwind note (no size change). | After ≥10 reports carry `short_float`/`short_ratio`, calibration shows short calls into high-SI names underperform (realised WR below class baseline). |
| **C16** | Float-normalized conviction (signal-confluence-quant) | Dark-pool block / OI build pays full accumulation points only if it is ≥ X% of `Shs Float` (X set by backtest); below → halved. Extends the C11 conjunction. | Calibration shows the float-normalized block threshold separates winners from churn (effect size ≥ the C11 conjunction's). |
| **C17** | Analyst-divergence axis (fundamentals-gate) | `Recom`-vs-flow disagreement beyond a band → CAUTION contribution (downside-only, never CONFIRM-only). | Calibration shows flow-vs-analyst divergence has sign on outcomes. |
| **C18** | Insider-cluster conjunction (accumulation-hunter → quant) | `insider_cluster_present` ∧ dark-pool block ∧ cum-flow → +1 to the accumulation line (conjunction-gated like C11). | Calibration shows the 3-way conjunction beats the 2-way (C11) baseline. |

**Discipline:** until a C-item clears, its `fz` field stays advisory (Phase A) and earns 0 points.
This is the single most important constraint — it prevents `fz` from inflating conviction on a
narrative, the exact failure mode the repo's calibration loop exists to prevent.

---

## Phase C — Feedback-loop extension (after A lands)

- **C-loop.** At risk-monitor watchlist write-back, snapshot `fz quote` for each top-5. Next Step 0,
  run `fz quote-drift <T> --since <prev_date>` on the carried `conviction_<date>` group; surface any
  moved field (short-float spike, target cut) as an adverse-fundamentals alert alongside the existing
  flow alerts. Wire the drift output into `/calibration-audit` Phase 1 so fundamentals changes become
  part of the outcome record.

---

## `/calibration-audit` changes

- Phase 1 inventory: capture the new `fz_context` envelope fields per call (no schema break — additive).
- Phase 4 (marginal contribution): add `fz` fields/clusters to the per-signal tool tier-list so they
  are scored LOAD-BEARING / SUPPORTIVE / NO-INFO / NEGATIVE like every other tool — this is what
  authorizes (or kills) each Phase-B promotion.

---

## Verification

1. **Install/health:** `fz --version` → `finviz-pp-cli 1.0.0`; `fz doctor` clean.
2. **Wrapper:** `python3 scripts/fz_enrich.py --ticker AAPL --date 2026-05-27` returns the compact
   field set; kill `fz` (rename binary) → wrapper returns `fz_available:false`, report still completes.
3. **Dry run:** execute one `/daily-analysis` with Phase A lanes ON. Confirm: top-5 carry
   `short_float`/`short_ratio`/`float`; Step 0 logs breadth; squeeze/RS funnel rows appear; **sizing
   is byte-identical to a Phase-A-OFF run** (advisory = no scoring change). 
4. **Envelope:** `python3 scripts/validate_decision.py --file decision.json` still `OK` (additive fields).
5. **Promotion:** only after ≥10 reports, run `/calibration-audit`; promote a C-item to LIVE **only**
   if it clears its threshold; record the decision in the audit `SUMMARY.md`.

## Effort summary

Phase A: **S (<1 day)** — one wrapper script + permission + Step-0/agent prompt edits, all additive.
Phase B/C: **M**, gated on calibration data accruing — no calendar commitment, data-driven promotion.
