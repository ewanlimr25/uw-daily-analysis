# Calibration Meta-Audit — auditing the auditor (and the subjects it audits)

**Run-id:** 2026-05-30 · **Disposition:** findings only (Deliverable A). B (auditor upgrade) and C (subject upgrade) are GATED on a plan you approve.
**Persona:** composite elite desk reviewer — every material judgment is tagged **[PM]** (buy-side, does it make tradable $?), **[FT]** (sell-side flow trader, is the flow read mechanically right?), or **[MMQ]** (market-maker quant, are the greeks/GEX/DEX/VRP/skew claims sound & survivorship-free?).

**Method note.** This document grounds in the *actual artifacts*, not CLAUDE.md summaries: the live `uw`/`fz` binaries (`uw <group> --help` enumerated, 56 + 27 leaf subcommands), the auditor skill `.claude/commands/calibration-audit.md`, the two subjects `daily-analysis.md` / `weekly-analysis.md`, all 16 agents, `schemas/decision_envelope.schema.json`, `scripts/validate_decision.py`, the C1–C19 register, and — most usefully — **the auditor's own most-recent worked output**, the completed 7-phase run at `analyses/audit/2026-05-29/`. That run is treated as a live test case: where the auditor self-reported a blind spot, it is corroborated and quantified here.

Two facts I verified directly that anchor the whole critique:

1. `uw historical trend` has **no `--date` flag and emits no OHLC high/low** — only `--symbol`/`--days`, options-flow metrics + daily close (`uw historical trend --help`, verified 2026-05-30). `uw historical signal-backtest` has **no `--date` flag** either (`--signal-type/--lookback-days/--top-n` only).
2. Yahoo daily bars **do** carry OHLC `high`/`low`/`open`/`close` (verified against the chart API the yfinance MCP wraps). The 2026-05-29 run's claim that "both yfinance MCP endpoints return close-only" (`phase_2_outcomes.md` "Method & data limitation") is **factually wrong** — daily range is available; only intraday-tick range is not.

These two facts collide: **the auditor's Phase 2 instructs a resolution method (`uw historical trend … --date … capture intra-window high/low`, `calibration-audit.md:160`) that its own named tool cannot perform, while overlooking the daily-OHLC source that could perform a weaker but valid version of it.** That is the single highest-leverage finding in this document.

---

## §1 — Current state: the 7 audit phases

| # | Phase | What it *measures* (real backtest) | What it only *asserts* | Input dataset | Method rigor | Known blind spots (self-reported + found here) |
|---|---|---|---|---|---|---|
| 0 | Preflight (`:51-65`) | report inventory count vs 10-daily/3-weekly floor; data-staleness via `available-dates` | — | `analyses/{daily,weekly}/*/report.md` | Mechanical, sound | Staleness check (`:64`) can't fire usefully — `available-dates` ≠ per-ticker coverage |
| 1 | Inventory & Parse (`:68-134`) | extraction completeness; envelope-vs-prose coverage; Σ-points reconcilable | tool citations on legacy rows | reports + `decision.json` sidecars | Strong where envelopes exist (54/516); **weak on 462 legacy prose rows** | tools_cited **reconstructed from prose** for 90% of rows; ~70 free-text `dominant_signal_class` strings collapsed heuristically |
| 2 | Outcome Resolution (`:137-173`) | WIN/LOSS/INCONCLUSIVE per horizon window; realised return; MAE | "path-aware" -1R-first rule; `signal-backtest` as "should-have-been" rate | `uw historical trend` + `signal-backtest` + yfinance | **Compromised** — see §2 | spec calls a `--date`/high-low method the tool lacks; resolved **close-to-close** (path-aware rule silently not enforced); LEAPs 100% `window_open`; vol resolved by a RV-direction *proxy* (no `implied_move`) |
| 3 | Calibration (`:177-208`) | claimed vs realised WR per class; per-tier reliability; **Brier**; raw_score quintiles | that the truth-set benchmark is point-in-time | Phase 2 jsonl | Calibration math is sound; **benchmark is contaminated** | **no SPY/benchmark-excess** (measures calibration, not edge); truth-set rate from a no-`--date` (look-ahead) backtest; no multiple-hypothesis correction; thin-N classes (n=1–2 claims) tabled at −40pp |
| 4 | Tool Attribution (`:211-254`) | class-conditional `winrate_with − winrate_without` per tool; LOAD-BEARING…NEGATIVE tiers; fz axes vs C15–C18 | that MCs are real (they're reconstructed) | Phase 2 jsonl | **Qualitative, not verbatim** | 462/516 citations reconstructed; CONFOUNDED detector structurally cannot fire (sparse citations); no regime split; single UPTREND regime |
| 5 | Schema Critique (`:258-294`) | per-integer-score realised WR; proposed re-weights ∝ MC; tier re-cut; holdout Brier | that the holdout validates HIGH tier | Phase 3/4 jsonl | Honest about overfit risk; **holdout can't test HIGH** | re-cut driven by n=2–10 per-score buckets; holdout = this week's window_open reports (0 resolved HIGH); single regime |
| 6 | Decision-Process Audit (`:298-334`) | Σ-points compliance; sizing-map compliance; **gate-firing rates**; missed-gate ledger | that firing == effectiveness | Phase 1 rows w/ `score_components`+`gate_verdicts` | Compliance math sound | measures whether gates **fire**, never whether they **help** (no VETO/​downgrade counterfactual; false-positive cost of VETOes unmeasured); only 32 rows have structured `gate_verdicts` |
| 7 | Recommendations (`:338-379`) | prioritized propose-only patch list, each cites phase+datum | priorities inherit upstream confidence | Phases 3/4/5/6 | Propose-only discipline intact | ships **P0** changes off Phase-4 reconstructed (non-verbatim) data |
| 8 | Exec Summary (`:383-406`) | ≤400-word desk note | — | all phases | Fine | — |

**One-line state of the union:** the auditor is *structurally excellent* (resumable checkpoints, propose-only, three-lens framing, real Brier/tier/quintile math) but is **running on a crippled outcome-resolution layer and a calibration definition that omits the benchmark** — so it can tell you the rubric *lies to itself* (claimed vs realised) but **cannot yet tell you whether the book has edge** (realised vs SPY). The 2026-05-29 run is a competent audit of a measurement it half-defined.

---

## §2 — Per-phase critique (auditor) + per-step critique (subjects)

### AUDITOR — Phase 0 (Preflight)
**[PM] Strong.** The 10-daily/3-weekly floor with a hard abort + `relax_threshold` banner is correct discipline. **Weak:** the staleness guard (`:64`) compares `available-dates` to "the most recent ticker call," but `available-dates` reports *data-type availability*, not per-ticker price coverage — it cannot detect that AAPL's 30D LEAP window is unresolved. The 2026-05-29 run proves the real staleness problem is **horizon-relative** (all LEAPs `window_open`), which Phase 0 never checks. *Fix lens: [PM].*

### AUDITOR — Phase 1 (Inventory & Parse)
**[FT] Strong** where envelopes exist — 54 structured rows parse cleanly, Σ-points pre-reconciled by `validate_decision.py`. **Weak:** 90% of the dataset (462/516) is legacy prose, and the parser invents `tools_cited` from metric names. Everything Phase 4 builds on those rows is therefore a **reconstruction, not an audit trail**. This is *known* (`phase_4_tools.md` provenance caveat) but the consequence is under-priced: it means the headline tool tiers are hypotheses. The `~70 free-text dominant_signal_class` sprawl (data-quality flag #2) also means per-class N is assembled by fuzzy collapse — a researcher could move `dark_pool_accumulation` from −31.6pp to honest by reclassifying 5 rows. **No controlled-vocabulary enforcement.** *Fix lens: [FT].*

### AUDITOR — Phase 2 (Outcome Resolution) — the critical phase
This is where rigor breaks, and it cascades into 3/4/5.

- **[MMQ] The spec is non-executable as written.** `:160` says "`uw historical trend` — `ticker`, `--date <report_date>`, `--days <window>` … Capture intra-window high/low, drawdown-from-entry." The tool has **neither `--date` nor high/low** (verified). The 2026-05-29 run had to silently substitute yfinance close-to-close. **The auditor's instructions describe a backtest its toolchain can't run.** This is a latent correctness bug that will mislead any future maintainer.
- **[MMQ] Path-awareness is claimed but not delivered.** The win threshold (`:150-154`) is explicitly path-aware ("a +2% gain that came after a −1.5% drawdown is a LOSS… path matters because the invalidation rule would have stopped the trade"). Resolved close-to-close, the −1R-first rule **cannot be evaluated** — an intraday stop-out that closed back inside the band is scored as un-triggered. The run admits this biases toward *fewer* path-losses (i.e. **inflates** WR). Yet daily high/low *is* available (verified) and would let MAE be measured on daily bars — recovering most of the path rule. The auditor abandoned a recoverable measurement on a false "close-only" premise.
- **[FT] The "should-have-been" benchmark has look-ahead baked in.** `:161` quotes `signal-backtest` as "the rate that *should have* been quoted… as of the report's date." The tool has **no `--date`** — it computes over *all available history including data after the report*. The run quoted bullish_flow 76–83% from it. **A benchmark computed with future data cannot judge a point-in-time call.** This contaminates Phase 3's divergence sign.
- **[PM] LEAP is structurally unauditable and the phase has no fallback.** 52 LEAP calls, 0 resolved (30/90D windows open). The phase offers no interim mark-to-market, no "partial-window MAE" disposition — LEAP calibration simply never happens on a rolling basis. For a book that *builds LEAPs*, the audit is blind to a quarter of its output indefinitely.
- **[MMQ] Vol resolution is a proxy of a proxy.** vol_long/vol_short resolved by "realized-vol direction" because legacy data lacks `implied_move` (`:162`). That is **not** an IV-vs-RV vol-P&L; a short-vol trade that *won* on vol-crush while spot drifted is mis-scored. The alarming vol_short 30.9% (Phase 2) is quite possibly a methodology artifact — the run says exactly this (`P2.3`).

### AUDITOR — Phase 3 (Calibration)
- **[PM] The biggest conceptual gap in the entire system: the audit measures calibration, not edge.** Phase 3 compares `claimed_win_rate` vs `realised_win_rate` (`:184-185`). It **never computes benchmark-excess** (realised − SPY same-window same-direction). Yet the *subject* enforces exactly this — `signal-confluence-quant`'s C2 market-excess gate (`signal-confluence-quant.md:54-59`, `scripts/excess_winrate.py`). **The auditor holds the system to a lower bar than the system holds itself.** In a single UPTREND tape, "long 50.0%" (Phase 2) may be *below* the SPY up-day base rate — i.e. the longs have **negative edge** while looking like a coin-flip. The audit cannot currently see this. [PM] This is the finding most likely to change real sizing.
- **[MMQ] No multiple-hypothesis correction.** Phase 3 flags every class with |divergence|>10pp across ~10 classes and Phase 4 tiers 22 tools — ~32 simultaneous tests, zero Bonferroni/FDR/BH. `contrarian_fade` (claim n=1) at −40pp and `gamma_pin` (claim n=2) at −33.9pp are tabled with 🚩 despite being noise. The "(thin claim)" tag is honest but the numbers still flow into the SUMMARY and Phase 5.
- **[MMQ] Brier uses a degenerate label.** `Brier = (claimed − outcome)²` with `outcome ∈ {0,1}` (`:193`). For multi-window horizons the "outcome" is itself a path-ambiguous close-to-close call (Phase 2 limitation), so Brier 0.34 inherits all the resolution noise. Defensible as a *relative* number, dangerous as an absolute "anti-calibrated" verdict.
- **[FT] Single-regime, stated as if general.** Every realised WR is one UPTREND (Apr–May 2026). Phase 3 never stamps "all rates regime-conditional: UPTREND only." A reader takes "dark_pool_accumulation 51.2%" as a property of the signal; it's a property of the signal *in this tape*.

### AUDITOR — Phase 4 (Tool Attribution)
- **[MMQ] The tier list is built on reconstructed citations and shipped as P0.** Phase 7's P0.2/P0.3 (rip `cumulative-premium-flow` + `institutional-accumulation` from the HIGH gate; cut the +3 cum-flow line) rest on Phase-4 MCs derived from prose-reconstructed `tools_cited` on 90% of rows. The provenance caveat says "no single tool's pp figure should be treated as precise" — then P0 changes are proposed off exactly those figures. **Either the data supports a P0 or it doesn't; you can't caveat it to qualitative and then act P0 on it.**
- **[FT] `winrate_with − winrate_without` is confounded by selection, not just class.** Controlling only for `dominant_signal_class` (`:220`) leaves regime, liquidity, and *co-citation* uncontrolled. `cumulative-premium-flow` looks NO-INFO partly because it's cited on *everything* (n=76) — it's the base-rate citation, so `with`≈`without` by construction. That's an artifact of citation ubiquity, not proof of no information.
- **[MMQ] Coverage hole: live gates are not in the tool table.** `front-end-iv-ratio` (the panic gate, `risk-monitor.md:17,42`) and `vanna-charm` (dealer-positioning's squeeze input) **never appear in Phase 4**. The audit scores `term-skew` (−13.4pp) but not the term-structure tool feeding the actual live risk gate. A tool can be load-bearing in the *gate stack* and invisible to *attribution*.

### AUDITOR — Phase 5 (Schema Critique)
- **[MMQ] Re-cut driven by 2–10-obs score buckets.** The HIGH 10→9 move hangs on score-9 = 70% (n=10) and score-13 = 100% (n=2) (`phase_5_schema.md` §C). The holdout *cannot* validate HIGH (0 resolved HIGH calls). The run correctly downgrades this to ACCEPT_WITH_CAVEAT / P1-pending — good — but the deeper issue is that **Phase 5 has no minimum-N gate on the per-score buckets it re-bins on.**
- **[PM] Budget-neutral re-weighting preserves a flawed total.** Phase 5 keeps "sum-to-same-budget" (`:271`). If the *whole rubric* is anti-calibrated (Brier 0.34), reshuffling a fixed budget is rearranging deck chairs — the right question (does *any* additive rubric beat a 2-feature logit of `dex` + `block-stratified`?) is never asked.

### AUDITOR — Phase 6 (Decision-Process Audit)
- **[PM] Measures gate *firing*, never gate *effectiveness*.** Phase 6 reports event_risk fired 21/32, fundamentals 17/30 (`phase_6_decision_audit.md`). It **never** asks: did VETO'd names actually underperform? did −1-tier downgraded names lose more than ungated peers? **The false-positive cost of a VETO is unmeasured** — a fundamentals-gate that VETOes 14 CAUTION/VETO names is only good if those names lose; if they win, the gate is destroying edge. This is the gate-calibration analogue of Phase 3 and it's absent.
- **[FT] Compliance denominator is tiny.** Only 32 rows carry structured `gate_verdicts`; the missed-gate "28% > 20% drift" verdict on event_risk rests on 8/29. Actionable as a hypothesis, thin as a mandate.

### AUDITOR — Phase 7 / Step 8
Propose-only discipline intact (`:377`). The only structural critique is inherited: P0 items lean on Phase-4 reconstructed data (above).

---

### SUBJECT — `/daily-analysis` & `/weekly-analysis` step critique

| Step | What it does | Critique (lens) |
|---|---|---|
| Step 0 — macro/breadth funnel (`daily:44-92`) | FRED 12-series snapshot, `risk market-regime`, `screener bullish-bearish`, `fz breadth` cross-check, liquidity floor | **[PM]** `macro_snapshot_signals` and `breadth_cross_check` are emitted to the envelope but **never scored** — does the macro regime label predict next-session drawdown? Unknown. Advisory forever with no validation path wired into the audit. |
| Step 1 — 11–12 parallel alpha-finders (`daily:93-227`) | each emits signals, 0 self-score | **[FT]** Sound division of labour. The risk is *correlated discovery*: 11 agents on one tape surface the same 3 mega-caps; no de-correlation of *idea sources* before the quant (only post-hoc price-correlation in risk-monitor). |
| Step 2a — `signal-confluence-quant` (`daily:232`) | additive rubric → raw_score, win_rate, size | **[MMQ]** Despite C11 conjunction + C13 routing shipping, the 2026-05-29 tier ladder is still **inverted** (HIGH 53.7% / LOW 55.8%) and HIGH-tier directional **expectancy is negative** (−1.52%, payoff 0.06). The additive model isn't ranking outcomes. The +3 `cumulative-premium-flow` line (`daily:287`+ rubric) is the chief inflator (Phase 4 NO-INFO at n=76). |
| Step 2b — `fundamentals-gate` VETO/CAUTION (`daily:243`) | Finnhub cross-check, tier_adjustment | **[PM]** VETO is a hard kill (`fundamentals-gate.md:50-59`) with **no measured hit-rate**. Distribution-dressed-as-accumulation is a great *thesis*; whether the gate's VETOes are right is never back-tested (Phase 6 gap). |
| Step 2c — bull/bear debate (`daily:249`) | residual confidence, −1 tier if bear≥bull | **[FT]** The debate gate (`risk-monitor.md:48`) is a real downgrade lever whose **predictive value is never audited** — do high-bear-residual names actually underperform? Phase 1 *carries* `debate_residual_confidence` but no phase resolves it against outcome. |
| Step 3a — HIGH-tier load-bearing-tool gate (`daily:273`) | 3-of-5 required tools | **[MMQ]** Phase 4 shows **2 of the 5** gate tools (`cumulative-premium-flow` NO-INFO, `institutional-accumulation` NEGATIVE) don't separate winners — the gate is satisfiable by anti-predictive evidence. |
| Step 4/5 — rubric + sizing (`daily:287-351`) | tier cuts, win-rate→size ladder | **[PM]** Win-rate *quotes* inflated 30pp on dark-pool/vol-surface/gamma-pin (Phase 3). Sizing on hit-rate alone ignores the book's real edge axis (asymmetry/expectancy, payoff 1.47). |
| §2 GEX / §2a 0DTE / single-leg C19 | advisory blocks | **[MMQ]** These three (`next_session_gex`, `next_session_0dte_setup`, single-leg) are emitted but **the audit has no forward-attribution lane for any of them** — GEX regime-call accuracy, 0DTE premium-sell realisation, and C19 put-edge persistence are all validated (if at all) by *separate offline scripts*, not by `/calibration-audit`. |
| Weekly Step 6 — thesis scorecard (`weekly:408`) | intra-week WIN/LOSS per ticker | **[FT]** This is the one place the *subject* self-grades — but it uses its own ad-hoc WIN/LOSS, not the auditor's path-aware definition, so the two disagree silently. |

---

## §3 — Coverage gaps (tools relied-on-but-unaudited, and available-but-unused)

### 3a. Tools the commands USE as evidence but the audit does NOT score
| Tool | Used by | Why it's unaudited | Risk |
|---|---|---|---|
| `options-structure front-end-iv-ratio` | risk-monitor **panic gate** (`:17,42`), vol/earnings agents | absent from Phase 4 table | a live tier-downgrade gate with **zero** measured predictive value |
| `options-structure vanna-charm` | dealer-positioning squeeze flag | absent from Phase 4 | the swing squeeze thesis is unvalidated |
| `historical vrp` | contrarian/vol/earnings VRP gates; risk-monitor VRP gate (`:43`) | absent from Phase 4 | the VRP sign-gate (live) is unmeasured |
| `options-structure gex` / `today-gamma-flip` (next-session map) | §2 advisory + gamma-flip-tracker | Phase 4 scores `gex` at 0.0pp on tiny N; no GEX-**regime-classification-accuracy** metric | the next-session dealer prior is asserted, never scored |
| `options-flow single-leg` (C19) | accumulation/contrarian co-flag | no single-leg lane in Phase 4; validated only by `scripts/single_leg_whale.py` offline | the one *new* edge claim is outside the audit loop |
| `fz breadth` / `fz_context` | Step 0 + fundamentals-gate | Phase 4 has the C15–C18 lane but **0 resolved** rows | advisory indefinitely with no resolution trigger surfaced |
| `macro_snapshot_signals` (FRED) | Step 0 regime framing | no phase resolves macro context → outcome | a whole context layer with no feedback loop |

### 3b. `uw` subcommands AVAILABLE but UNUSED by the commands (missed-edge inventory)
From the 56-subcommand enumeration, the notable idle tools:
- **`oi decrease-with-volume`** — positions being *closed* (distribution). **[PM] This is the literal mechanical signal for "distribution dressed as accumulation"** that fundamentals-gate tries to infer from Finnhub. It's an unused UW primitive that directly serves the VETO thesis. **Strongest single missed-edge item.**
- **`dark-pool price-levels`** — institutional S/R from DP block concentration. **[FT]** Could anchor `invalidation` levels (currently prose-guessed) to a real dealer/institutional level. Cheap precision win.
- **`options-flow greek-screener`** — filter by delta/gamma/vega. **[MMQ]** Would let directional conviction be expressed in *net delta* terms rather than premium counts; refines the bullish/bearish_flow read that Phase 3 shows is a coin-flip (46%).
- **`dark-pool extended-hours`** — pre/post DP blocks; **[FT]** institutional positioning around the close/open that the EOD report misses.
- **`options-flow expiry-heatmap` / `dte-volume-share`** — DTE concentration; **[MMQ]** would sharpen the 0DTE-vs-swing-vs-LEAP horizon tagging the report does by hand.
- **`screener put-call-extremes`** — **DEPRECATED v0.4.0**; correctly avoided. Flag only so the audit can confirm no agent regresses to it.

### 3c. Edge the commands SHOULD capture but structurally can't
- **[PM] Benchmark-relative edge.** The whole stack reports absolute win-rates; neither subject nor auditor closes the loop on "did we beat buy-and-hold SPY at the same horizon?" The subject has the *machinery* (C2/`excess_winrate.py`) but the auditor doesn't use it, so the loop never closes.
- **[MMQ] Regime-conditional everything.** One UPTREND in the dataset → every weight, tier, tool-tier is a single-regime estimate stated as general. No regime-stratified scoring exists in either layer.
- **[PM] Expectancy/payoff as a first-class axis.** Phase 2 found the book's edge is asymmetry (payoff 1.47, +0.50%/trade) concentrated in MEDIUM tier, while sizing keys on hit-rate. The C3 Kelly machinery exists but is gated ADVISORY (correctly — tier-expectancy non-monotone). The *gap* is that nothing sizes on expectancy even advisorily in the report.

---

## §4 — What to ADD for robustness (desk-justified)

Each item names the lens and the edge/$ rationale. These are *capabilities to add*; §5 sequences them.

1. **[AUDITOR][PM] Benchmark-excess win-rate in Phase 3.** Add a column: `realised_excess = realised_WR − SPY_same-window_same-direction_WR`, reusing `scripts/excess_winrate.py` (already the subject's C2 engine). **Edge:** converts "calibration" into "edge" — tells the desk whether a 50% long actually *beat the tape*. Without it the audit can bless a book with negative real edge. This is the #1 add.
2. **[AUDITOR][MMQ] Daily-bar path-aware resolution.** Replace the broken `uw historical trend --date` spec with yfinance daily OHLC (`get_historical_stock_prices`, verified to carry high/low). Compute true-range ATR(14) for R, and a daily-bar MAE so the −1R-first path rule actually runs (intraday-tick still unavailable, but daily high/low recovers ~80% of it). **Edge:** removes the WR-inflation bias the run admits; makes vol_short 30.9% diagnosable instead of a confound.
3. **[AUDITOR][FT] Kill the look-ahead in the truth-set benchmark.** `signal-backtest` has no `--date`; stop quoting it as the point-in-time "should-have-been" rate. Either (a) reconstruct the as-of rate from only pre-report closed calls, or (b) demote it explicitly to "general class behaviour, not a benchmark." **Edge:** stops the audit grading point-in-time calls against future-contaminated numbers.
4. **[AUDITOR][MMQ] Multiple-hypothesis correction + N-floor on every tabled stat.** Apply Benjamini-Hochberg across the per-class/per-tool flag set; hard-suppress any cell with decided-N<8 from headline tables (keep in an appendix). **Edge:** stops −40pp (n=1) noise reaching the SUMMARY and Phase 5 re-cut.
5. **[AUDITOR][PM] Gate-effectiveness (not just gate-firing) in Phase 6.** For each gate, compute realised WR of gated-down vs not-gated names within class, and the **VETO false-positive rate** (VETO'd names that would have won). **Edge:** a VETO that kills winners is negative edge masquerading as prudence; this is the only way to size the cost.
6. **[AUDITOR][MMQ] Per-signal-class decay / half-life.** Resolve each class at multiple horizons already captured (3D/10D, 5D/10D, 30D/90D) and report the WR term-structure — does dark_pool_accumulation edge live at 10D and decay by 30D? **Edge:** tells the desk the *holding period* each signal is actually good for, which the fixed horizon map assumes rather than measures.
7. **[AUDITOR][MMQ] Calibration curve (reliability diagram) + log-loss, not just Brier.** Bucket predicted `win_rate` into deciles, plot realised hit-rate; report log-loss alongside Brier. **Edge:** Brier conflates calibration and resolution; the reliability curve shows *where* on the confidence scale the lying happens (it's the 0.80+ bucket).
8. **[AUDITOR][PM] Advisory-block forward-attribution lanes.** Wire the offline validators into the audit: GEX regime-classification accuracy (does NEGATIVE-gamma call predict next-session realised range expansion?), 0DTE premium-sell realisation, single-leg C19 put-edge persistence. **Edge:** three advisory blocks currently graded (if at all) outside the audit get a calibration home → a real promotion path off advisory.
9. **[AUDITOR][FT] Controlled-vocabulary enforcement at Phase 1.** Map every `dominant_signal_class` to a closed enum at parse time; reject/flag free-text. **Edge:** removes the "reclassify 5 rows to change −31.6pp" fragility.
10. **[SUBJECT][PM] `oi decrease-with-volume` distribution detector into fundamentals-gate / accumulation-hunter.** Add the unused primitive as a mechanical distribution flag feeding the VETO thesis. **Edge:** replaces a Finnhub *inference* of distribution with a direct *flow* observation — exactly the signal the gate exists to catch. (Enters ADVISORY per discipline.)
11. **[SUBJECT][MMQ] Expectancy-aware advisory sizing surfaced in the report.** Even while C3-Kelly stays ADVISORY, print per-tier expectancy/payoff in §6/§7 so the desk sees the asymmetry the hit-rate hides. **Edge:** the book's actual edge (payoff 1.47, MEDIUM-tier-concentrated) becomes visible to the human sizing it.
12. **[BOTH][MMQ] Regime stamp on every persisted number.** Tag every realised stat and every shipped weight with the regime it was estimated in; refuse to apply a single-regime weight as if general. **Edge:** the precondition for ever trusting a re-weight out of sample.

---

## §5 — Prioritized improvement register (candidate criteria C20+)

Continues the C1–C19 numbering. Tag = **[AUDITOR]** (changes `calibration-audit.md`), **[SUBJECT]** (changes daily/weekly/agents/scripts/schema), **[BOTH]**. Every new scored line in a *subject* enters ADVISORY (0 rubric points) until its gate clears — consistent with C1–C19 discipline. Auditor changes are method fixes (no rubric points) and ship once correct.

### P0 — correctness / calibration-breaking (the audit is currently mis-measuring)
| ID | Title | Tag | Lens | Validation gate before it's authoritative |
|---|---|---|---|---|
| **C20** | Daily-bar path-aware resolution (yfinance OHLC; true-range ATR; daily MAE) replacing the non-executable `uw historical trend --date` spec | [AUDITOR] | [MMQ] | Re-resolve the 2026-05-29 cohort; vol_short/0DTE WR must be re-stated under the daily-bar rule and the close-only artifact confirmed-or-refuted. Ship once it reproduces ≥ the close-only numbers without the high/low premise. |
| **C21** | Benchmark-excess win-rate (realised − SPY same-window) as a first-class Phase 3 column | [AUDITOR] | [PM] | Re-run Phase 3 with `excess_winrate.py`; every class WR carries an excess figure + sign. No gate beyond "matches the subject's C2 definition." |
| **C22** | De-look-ahead the truth-set benchmark (`signal-backtest` no-`--date`); demote or reconstruct as-of | [AUDITOR] | [FT] | Phase 2/3 no longer cite a future-contaminated rate as "should-have-been"; the substitution is documented in the checkpoint. |
| **C23** | N-floor (decided-N≥8) + Benjamini-Hochberg across all flagged per-class/per-tool stats | [AUDITOR] | [MMQ] | Thin-N cells (contrarian_fade n=1, gamma_pin n=2) move to appendix; SUMMARY carries only BH-surviving flags. |

### P1 — clear improvement (closes a real blind spot)
| ID | Title | Tag | Lens | Validation gate |
|---|---|---|---|---|
| **C24** | Gate-effectiveness + VETO false-positive measurement in Phase 6 | [AUDITOR] | [PM] | Phase 6 reports gated-vs-ungated WR per gate and a VETO FP-rate; requires ≥10 resolved VETO'd names before the FP-rate is acted on (advisory below). |
| **C25** | Calibration/reliability curve + log-loss alongside Brier | [AUDITOR] | [MMQ] | Reliability deciles + log-loss in Phase 3 output; no external gate. |
| **C26** | Per-signal-class decay/half-life (multi-horizon WR term structure) | [AUDITOR] | [MMQ] | Each class reports WR at its 2 captured windows; ≥8 decided per (class,window). |
| **C27** | Advisory-block forward-attribution lanes (GEX regime accuracy, 0DTE realisation, single-leg C19 persistence) folded into the audit | [BOTH] | [MMQ] | Each lane needs its offline backtest reproduced *inside* a phase checkpoint; the C19/GEX/0DTE promotion thresholds stay as already registered. |
| **C28** | `oi decrease-with-volume` distribution detector → fundamentals-gate/accumulation-hunter (ADVISORY, 0 pts) | [SUBJECT] | [PM] | Promote to a scored VETO-support line only when Phase 6 shows distribution-flagged names underperform the accumulation baseline by ≥10pp on n≥15. |
| **C29** | Controlled-vocabulary enforcement for `dominant_signal_class` at Phase 1 parse | [AUDITOR] | [FT] | Parser maps to closed enum; legacy free-text flagged, not silently collapsed. |

### P2 — robustness / polish (needs more data or is lower-$)
| ID | Title | Tag | Lens | Validation gate |
|---|---|---|---|---|
| **C30** | Regime stamp on every persisted stat + shipped weight; block single-regime weights from being applied as general | [BOTH] | [MMQ] | Mechanical tag; enforced once a 2nd regime exists in the dataset. |
| **C31** | Expectancy/payoff surfaced per-tier in the report (advisory, alongside the live hit-rate ladder) | [SUBJECT] | [PM] | Display-only; the C3 Kelly live-activation gate (n≥30, tier-expectancy monotone) still governs any *sizing* use. |
| **C32** | Co-citation control in Phase 4 tool attribution (partial-out ubiquitous citations like cum-flow) | [AUDITOR] | [FT] | Phase 4 reports a co-citation-adjusted MC beside the raw one; ubiquity-artifact flag on tools cited >60% of rows. |
| **C33** | LEAP rolling interim mark-to-market disposition (so 30/90D builds aren't blind indefinitely) | [AUDITOR] | [PM] | Phase 2 emits `window_open_mtm` partial returns for LEAPs; never scored as WIN/LOSS until the window closes. |
| **C34** | `dark-pool price-levels` → anchor `invalidation` to a real institutional S/R level | [SUBJECT] | [FT] | Display/structure-only; no rubric points. |

### Items explicitly NOT proposed (and why)
- **Re-weighting the additive rubric on this dataset** — single regime, reconstructed citations, close-only outcomes. Phase 5's own holdout can't validate HIGH. Defer all rubric-weight/​tier-cut changes (the 2026-05-29 P0.1–P1.1) until C20–C23 land *and* this week's calls resolve (~2026-06-12) — otherwise the auditor upgrade and the subject re-weight chase each other's noise.
- **Flipping C3-Kelly live** — gate returned ADVISORY_ONLY (tier expectancy non-monotone, HIGH −1.52%). Stays advisory.
- **Promoting any fz C15–C18 or single-leg C19** — 0 resolved rows; INSUFFICIENT_N. Re-test ~2026-06-12.

---

## Bottom line (what the desk should take from this)

**[PM]** The auditor is well-built but is currently grading the system on the wrong axis (calibration, not edge) using a broken outcome-resolution layer. **Fix the auditor first (C20–C23), then re-run, then decide subject re-weights** — sequencing matters because every subject re-weight the 2026-05-29 run proposed was fit on close-only, single-regime, reconstructed-citation data. **[FT]** The one signal that survives every lens is `dealer_positioning`/`options-structure dex` (84% claimed → 80% realised, +15.5pp) — lean the book there. **[MMQ]** The book's real edge is asymmetry (payoff 1.47), not accuracy (51%) — and nothing currently sizes on it. The highest-$ single change is **C21 (benchmark-excess)**: until the audit measures realised − SPY, it cannot certify that the daily/weekly machine produces alpha rather than dressed-up beta.

*— End Deliverable A. Deliverables B (auditor edits) and C (subject edits) await an approved plan.*
