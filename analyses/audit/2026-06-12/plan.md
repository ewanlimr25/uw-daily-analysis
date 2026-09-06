# 2026-06-12 Audit — Synthesis & Propose-Only Action Plan
**Scope:** `/daily-analysis`, `/weekly-analysis`, all 16 agents, scripts, schema. **Stance:** buy-side PM / flow trader / MM quant. **No file outside `analyses/audit/2026-06-12/` was touched.**
**Evidence chain:** `phase_0_scope.md` (inventory) → `phase_1_command_methodology.md` (fresh methodology audit) → `phase_2_agent_audit.md` (16× static+live, verdicts) → `phase_3_internal_validation.md` (backtest re-runs + 151-call envelope battery + 50-call forward grading) → `phase_4_external_evidence.md` (9 literature lanes, verified citations) → `phase_5_reconciliation.md` (vs 10 prior audits). Sidecars: `p0_extraction.json`, `p1_hunters.json`, `p2_*.json`, `p3_*.json`, `p4_external_evidence.json`, `p5_prior_audits.json`.

---

# Part A — Current-state analysis

## A.1 The central fact
**The system's scored layer and its validated edges have traded places.** The conviction rubric — the thing the entire audit-and-retune apparatus optimizes — failed its own scheduled re-confirmation today (HIGH 0.222 / MED 0.214 / LOW 0.444 on the first post-UPTREND window; quotes anti-calibrated monotonically), while the genuinely validated edges live in lanes the rubric pays **0 points**: the Tier-1 single-leg put signal (re-run this session: WR 0.600, n=295, +21.9pp vs SPY-direction, p≈0, month-stable into the regime turn), the 0DTE VRP harvest (GO re-confirmed, n=43, with honest unsampled-tail caveat), and the GEX→next-day-vol channel (internal corr −0.39; the only dealer-positioning claim with peer-reviewed backing). External evidence ranks the rubric's lanes almost exactly inversely to their weights: the two +3 lines (DP accumulation, DEX flip) are respectively **contradicted** by the dark-pool microstructure literature (Zhu 2014; Comerton-Forde-Putniņš 2015; Hatheway 2017) and **unsupported by any peer-reviewed work** at the claimed horizon.

**What deserves equal emphasis: the plumbing is honest and the brakes work.** Across six agents, every report number checked against raw recomputation matched exactly — zero fabrication. The Σ-invariant holds 151/151; the 0.80 cap and sub-0.50 floor demonstrably bind post-06-06; the gate stack produced zero full-size calls ever and its skips were correct in the turn (skipped calls realized 0.333); advisory quarantine with pre-registered graduation gates (C19, C6, C8) is functioning. The system's measurement culture is real. Its defect is *what the measurements were spent on*: six audit cycles of re-weighting correlated rubric lines on n=8–31, BH-null, single-regime marginal contributions.

## A.2 Where the edge is REAL (keep and protect)
| Edge | Evidence |
|---|---|
| Tier-1 single-leg opening/floor puts (C19, advisory) | Internal: 0.600/n=295/p≈0, stable 4 months incl. June TRANSITIONAL (0.632). External: Johnson-So 2012, XZZ 2010, CW 2010 (bearish option informativeness via short-sale-cost channel); next-session horizon matches published decay. The single best scored-line candidate in the system |
| 0DTE premium-selling (§2a, advisory) | Internal GO re-confirmed (95.3%/90.7% win, +0.30/+0.39%/day, overnight negative). External: VRP family robust; conditioning stack matches where published net-positive results live. Open issues: PnL basis, net-of-cost, tail prior |
| GEX-regime → next-day vol (advisory input to §2a wings) | Internal −0.39 (long-γ 0.77% vs short-γ 1.22% range). External: NPPW RFS 2021, Barbon-Buraschi. Caveat: one replication finds it VIX-subsumed |
| C4 opening-flow gate; ≥$500K floor; LEAP overwriting rejections | Externally endorsed (P-P/GLP opening primacy; Bryzgalova retail pollution; Lakonishok 2007) |
| The brake architecture | Downgrade-only caps/gates + VETO + debate-cut-only; envelope-measured: prevented full-size exposure into the turn |
| Bearish/short side generally | 06-06 audit: shorts +alpha vs longs −beta; P3: shorts profitable in the turn; rubric currently under-pays it |

## A.3 Where the edge is ILLUSORY (as currently instrumented)
1. **Tier bands as a ranker** — failed scheduled re-confirmation; history of threshold-snooping (5→10→9).
2. **`win_rate` quotes** — substrate broken (window clamp +2.5pp recency inflation; 30pp `--top-n` swing; no per-ticker mode; flagship class permanently empty → circular fallback n=85); anti-calibrated on the turn window.
3. **+3 DEX flip / vanna** — fired with no flip on all three names checked live; no flip field exists in the tool; no peer-reviewed support at 1–4wk; level-in-up-tape = beta.
4. **Earnings kink gate as wired** — structurally unreachable (58/61 BACKWARDATION pre-FOMC, kink_expiry always null); FDX full-size rested on an 11-contract tenor not reproducible by a second reader.
5. **Sector persistence ≥0.6** — passed 11/11 sectors (filters nothing); flow-persistence continuation externally reverses.
6. **LEAP "informed positioning" premise** — externally a financing/borrow-fee story ≥2/3 of the time; gates honest but several unwired.
7. **Weekly §0 hit-rate headline** — hindsight-graded, survivor universe, INCONCLUSIVE escape; 66.7–70% claims vs 0.227–0.429 forward-resolved same-period.

## A.4 Where edge is DOUBLE-COUNTED
1. **`uw insights signal-confluence`** — a server-side composite of `dp_accumulation`/`oi_building`/`bullish_flow`, leveraged 4× (funnel seed, entry gate, +2 line, LB-gate slot). The +2 is near-deterministic for accumulation names.
2. **One actor's footprint** can reach ~13 daily / ~16 weekly points (HIGH ≥9) through causally-cascaded lines (DP→OI→premium→DEX→multileg→composite); the 3-of-5 LB gate requires citing three *correlated* tools, measuring citation breadth not evidence independence.
3. **Weekly OI triple-count** (+3 standalone, inside +3 accumulation, inside composite, +2 rolls on LEAPs) — daily's 2026-05-09 demote rationale never propagated.
4. **`cum_premium_flow_30d`** — one scalar, five scoring mechanisms (±4-point swing from a NO-INFO datum).
5. **Penalty side**: one adverse fact can fire quant −3 + sector −1 tier + debate −1 tier (the "haircut, not filter" pathology the event-risk gate already exhibited).
6. **Dead letters**: the −3 regime / −1 cluster "score" lines have never fired as points (0/151) — the published rubric overstates its own discipline.

---

# Part B — Prioritized action plan (propose-only; no edits performed)

> Items are **proposals**. Each carries: rationale → expected edge impact → blast radius → validation step. "Score-neutral re-run" = re-score the 16 existing envelopes under the proposed rubric and diff tier distributions before any live use.

## P0 — stop actively-misleading machinery (this week)

**P0.1 — Freeze the rubric: weights, tier cuts, and gate membership, and stamp `rubric_version` into the envelope.**
No promote/demote/re-bin until a change clears a pre-registered, cross-regime, BH-surviving bar (the register discipline C6/C8 already follow). Audits grade; they do not retune.
*Rationale:* P1-F4 (weights fit to noise, ~90 looks vs ~150 obs), P3 §3 (the last tuning's flagship — HIGH ≥9 — failed its own re-confirmation on schedule), P5 §3 (cum-flow +2→+3→+1 whipsaw was a realized false positive). *Edge impact:* stops the dominant source of self-inflicted noise; preserves cross-audit comparability for the first time. *Blast radius:* process + one additive schema field (1.3) + 2 command files' changelog norms. *Validation:* next two audits grade an unchanged rubric across the TRANSITIONAL regime.

**P0.2 — Collapse `uw insights signal-confluence` to ONE role (Step-0 funnel seed only): delete the +2 scored line, remove it from the 3-of-5 LB gate, and replace its entry-gate role with "two distinct Phase-1 agents" only.**
*Rationale:* P1-F1 (live factor-list proof of re-count; the +19.5pp promotion evidence was selection-confounded; no per-ticker mode exists so the line is non-deterministic anyway; weekly gate/rubric thresholds contradict). *Edge impact:* removes ~2 free points from exactly the correlated names that over-score; directly attacks the single-footprint-HIGH pathway. *Blast radius:* both command rubrics + Step 3/3a + quant agent; no agent deleted. *Validation:* score-neutral re-run on the 16 envelopes — measure how many HIGH/MED calls drop a band and whether P3-graded outcomes improve monotonicity.

**P0.3 — Quarantine `uw historical signal-backtest` as a sizing input until rebuilt; in the interim, size on tier + the C2/C4/C12 gates with `win_rate` emitted as `NA(substrate)` unless from a complete-window, pinned-parameter, dated query.**
Rebuild spec (upstream Go binary, sibling repo): exclude incomplete forward windows from the headline (the tool already counts `truncated_signals` — stop including them), pin and document the ranking under `--top-n`, either implement `--symbol` or rename the output market-wide, and version the methodology string.
*Rationale:* P3 §2 (clamped rows 0.733 vs complete 0.485 — the artifact alone crosses the 0.50 sizing boundary; 30pp pagination swing; envelopes stamp one market-wide stat per ticker; flagship class permanently empty → circular n=85 fallback), P3 §4 (quotes anti-calibrated). *Edge impact:* removes a noise source bigger than any claimed class edge; the caps treated the symptom, this treats the cause. *Blast radius:* quant agent + Step 5 both commands + `excess_winrate.py` call-sites + the uw binary (out-of-repo). *Validation:* reproducibility test (same query, same answer, two consecutive days, pre/post-rebuild) + clamp share = 0 by construction.

**P0.4 — Mechanize or demote the +3 DEX/vanna line: award only on a verified sign change across ≥2 dated `dex` calls within the trailing 5–10 sessions plus a magnitude floor; cite both dated values in `score_components.evidence`. Hold at +1 until a dex-flip backtest (pattern: `single_leg_whale.py`) reports forward excess.**
*Rationale:* P2 (fired 3-for-3 without flips on 06-11; tool has no flip/trajectory field), P4 (no peer-reviewed support at 1–4wk; hedging pressure is intraday mean-reverting; level-in-up-tape = beta, concordant with 05-30's dealer −7pp excess). *Edge impact:* the rubric's largest single award stops being free points. *Blast radius:* dealer-positioning agent + both rubrics. *Validation:* the backtest harness; score-neutral re-run.

**P0.5 — Promote the C19 single-leg put lane along its pre-registered gate, with two refinements from external evidence: condition on short-sale-constraint proxies (fz `short_ratio`/days-to-cover already collected) and keep the call-side NO_GO regime-tagged rather than structural.**
June TRANSITIONAL accrual (0.632, n=19) starts the second-regime requirement; promote to a scored bearish line (+1/+2) only when the standing gate clears (rolling WR ≥58%, ≥60d, ≥2 regimes).
*Rationale:* P3 §1 (strongest validated edge in the system), P4 (Johnson-So channel; GLP warns calls-are-beta is regime-conditional), A.1 (the rubric under-pays the side where the desk's alpha demonstrably lives). *Edge impact:* the first scored line added on a pre-registered, cross-regime, externally-corroborated basis. *Blast radius:* both rubrics + quant + contrarian/accumulation routing (already drafted in C19 plan). *Validation:* the gate itself; then per-tier outcome tracking.

**P0.6 — Regime-freshness guard while in TRANSITIONAL: until the frozen rubric accrues ≥30 resolved TRANSITIONAL-era calls, cap all conviction-tier sizing at half and surface "rubric out-of-regime" in the Executive Summary.**
*Rationale:* every weight was fitted in UPTREND; P3 measured what happened at the boundary (HIGH 0.222). The brake stack already does most of this implicitly — make it explicit and dated. *Edge impact:* protective only. *Blast radius:* risk-monitor + both commands' Step 5. *Validation:* lift automatically at the n≥30 mark.

## P1 — repair instrumentation and recording (next 2 weeks)

**P1.1 — Gate-verdict completeness:** record the `debate` verdict (0/151 today) and the C2 market-excess result in `gate_verdicts`; store debate residuals as `{bull, bear}` (concurs with 06-06 P2.1); require all 8 keys on every non-DROP call. *Validation:* next envelope = 8/8 keys, 100% of calls.
**P1.2 — Spec-drift sweep (one pass, both commands + agents):** weekly confluence gate ≥5 vs rubric ≥4; daily/weekly sub-0.50 sizing wording; LEAP conviction threshold 65 vs 70; thin-window rule inverted (raise the bar or cap size — never lower the HIGH cut); delete the dead-letter −3 regime/−1 cluster *score* lines (the tier gates in 2d already own those facts — one penalty channel per fact); propagate or justify the weekly OI +3 vs daily +1 divergence. *Validation:* grep-level consistency check + validator extension.
**P1.3 — Term-structure substrate fix (repairs 3 agents at once):** exclude expired/0DTE buckets from `iv-term-structure` classification, volume-weight per-expiry IV, add a min-contract floor per tenor (kills the 58/61-BACKWARDATION degeneracy, the unreachable kink gate, and the 11-contract FDX tenor); pin `term-skew` tenor selection; report `dates_used` and require ≥120 lookback days before quoting an IV percentile. Prefer front-end *concavity* (Alexiou 2025) over raw backwardation as the earnings-richness discriminator. *Blast radius:* uw binary + earnings-scout + vol-surface-scout + multileg context. *Validation:* re-run the P2 live battery; expect KINKED to be non-empty and discriminating pre-FOMC.
**P1.4 — Accumulation line repairs:** make the C11 $50M confirmer scale-relative (e.g. ≥X% of the name's 30d options notional) — at mega-cap scale a 0.6% MIXED imbalance currently confirms the full +3; fix C28 distribution_flag attribution (put-close mislabeled as call distribution; premium-size floor for "lots"); align the institutional-accumulation window claim with the single-day CLI reality; add a conviction-matrix confidence floor. Longer-term: pre-register a DP-conjunction backtest (DP-block ∧ scale-relative flow ∧ OI-build → forward excess) — external literature contradicts the premise, so the line's weight should eventually rest on its own measured conjunction edge, not narrative. *Validation:* backtest harness + score-neutral re-run.
**P1.5 — Per-agent wiring fixes from P2 verdicts:** opex-pin (phantom `probability` field; dead `opex-concentration` cross-ref; sign-aware ranking reconciled with the tool's `pin_score`); sector-rotation (market-relative persistence so the gate can bind; purge the stale integer-scale invalidation threshold; fix the per-sector dte-share overclaim); leap-radar (replace unwirable gates 3/7; financing/borrow-fee disqualifier per MPP 2025; catalyst-timing-uncertainty conditioning); sweep-tracker (per-day direction verification or relabel `consistency_score`); contrarian (mechanical dated re-calls for "rising z"; index-fear-extreme framing per P4; the −2 line re-attributed as an informed-continuation penalty). *Validation:* re-run the P2 live protocols.
**P1.6 — Standing no-write rule** ("no file writes, no watchlist mutation, return findings only — risk-monitor's single write-back excepted") in every Phase-1 agent definition. *Rationale:* one real incident; most definitions silent. *Validation:* grep.
**P1.7 — Fundamentals-gate third leg:** insider MSPR is dead → either wire `fz insider-clusters` as the insider leg (advisory C18 framework exists) or re-spec VETO as 2-of-2 explicitly with a tightened bar; event-risk T+3 calculation bug from the static audit fixed alongside. *Validation:* census shows 3 live legs or an honest 2-of-2 spec; VETO FP tracked (currently 1-for-1 wrong this window, ~40% FP prior).
**P1.8 — 0DTE lane restatement:** publish the PnL basis (% of underlying vs premium-collected vs margin), add a net-of-cost line (half-spread + fees per Vilkov), and re-frame promotion criteria as expectancy-with-tail-prior, never win-rate. Keep permanently advisory until a vol-shock day is in sample. *Validation:* restated backtest block in the §2a output.

## P2 — hygiene and observability (this month)

**P2.1** Weekly §0 scorecard graded against the daily envelopes (kill hindsight reconstruction); define the INCONCLUSIVE movement threshold; report the denominator. **P2.2** Citation hygiene: DJKS RFS 2019 for earnings term structure; Johnson-So 2012 for bearish asymmetry; delete or cite the C19 numbers repeated uncited in contrarian-scanner; remove the unsupported "spreads more informative than single-leg" claim from multileg-strategist. **P2.3** Reliability preservation: keep emitting the uncapped rate + n in `audit_trail` (already done) and add a dedicated envelope field so future reliability diagrams aren't polluted by cap point-masses. **P2.4 — RESOLVED 2026-06-12: DECLINED (keep separate).** The optional gamma-flip→dealer-positioning merge was evaluated and rejected — the two carry different model configs (thinking-off mechanical read vs thinking-on synthesis), different horizons (next-session 0DTE vs 1–4wk swing; the split exists to prevent that horizon-bleed), and gamma-flip owns the distinct §2 report section. Marginal fleet-cost saving (one 0-point advisory spawn) < blast radius. Decision documented in both agent files. **P2.5** Validator extensions: gate_verdicts completeness (as-built: **9-key**, since P1.1 added rubric_regime), rubric_version presence, dead-letter line rejection. **P2.6** Fix `excess_winrate.py` SPY-benchmark window construction docs (windows must match the signal windows actually graded — non-reconstructible today; document the truncation rule).

## What NOT to do
- **Do not re-weight any other rubric line this cycle** — that is the failure mode this audit documents (P5 §3.1).
- **Do not remove the gate stack** because tiers failed — the brakes are why the tier failure cost little (P3 §3).
- **Do not un-advisory the GEX walls, PEAD, 52w-high, lottery-fade, or Kelly lanes** — every one of those quarantines is correct on current evidence.
- **Do not treat the June put-lane strength as license to skip C19's gate** — promote through it, not around it.

## Validation calendar
- **~2026-06-26 audit:** grade the frozen rubric on TRANSITIONAL data; C19 OOS scoreboard check; verify P1.1 gate recording on new envelopes.
- **~2026-07-10 audit:** first cross-regime read with ≥30 TRANSITIONAL-era resolved calls; decide P0.6 lift; C19 graduation decision if the 60-day/2-regime gate clears; review the signal-backtest rebuild reproducibility test.
