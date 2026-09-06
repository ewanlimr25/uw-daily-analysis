# Phase 5 — Grading-Schema Critique (2026-06-27)

> **RUBRIC FREEZE (version 2026-06-12) — this phase GRADES the frozen rubric; it does NOT retune it.**
> No re-weighted components, no re-binned cuts as actionable edits. Output = frozen-weight grading
> table + tier-cut monotonicity + freeze-lift check + **pre-registrations** (decided by a FUTURE
> audit). Voice: market-maker quant.

**Frozen rubric under grade:** tier cuts **HIGH ≥9 / MEDIUM 7–8 / LOW 3–6 / drop ≤2**; signed weights
**+3 accumulation-conjunction · +1 mechanized DEX · +1 cum-flow intent-screened · +2 multileg**
(plus the +1 `insights_signal_confluence` corroboration line, graded as context).

**Two binding provenance facts frame everything below (both re-verified this run):**
1. **All raw-≥9 calls are pre-freeze.** raw≥9 decided n=13, `rubric_version=None` for all 13, 0 from
   `2026-06-12`. The frozen ≥9 HIGH cut has **zero resolved calls in its own era** → every tier/cut
   grade is on the *pre-freeze* weights the freeze already replaced. Advisory-on-the-wrong-era.
2. **The decided regime strata are uptrend + pullback only; choppy/selloff (06-23..06-26) is
   window-open** (18 rows, all INCONCLUSIVE, all `window_complete=False`). Cross-regime grading yields
   two columns at most; the cross-regime acceptance bar for every pre-registration is **structurally
   unmeetable by this data.** Nothing in this phase can exceed **P1**.

---

## 1. Component-weight grading (frozen weight vs measured contribution)

Marginal contribution = `winrate_with − winrate_without`. **Headline = Phase 4 class-controlled**
(within `canonical_class`, class-N weighted, BH FDR 0.10). **Regime split = raw `tools_cited`
with-WR** (NOT class-controlled — colour only). Provenance: verbatim `tools_cited` / `score_components`.
**No proposed-weight column** (freeze).

| frozen line | wt | producing agent → tool | Phase-4 class-ctrl marg (n, BH, tier) | raw marg | uptrend with-WR (n) | pullback with-WR (n) | class-level calibration | grade |
|---|---|---|---|---|---|---|---|---|
| accumulation-conjunction | **+3** | accumulation-hunter → `insights_institutional_accumulation` (+ `dark_pool_block_stratified` gate) | **+13.6pp** (n=23, BH n, **LOAD-BEARING**); gate +7.7pp (n=20, BH n) | +6.0pp | 0.429 (14) | 0.667 (9) | `dark_pool_accumulation` real 0.455 / claim 0.554 / **excess +9.1pp** / n=33 / BH n | **SUPPORTED — keep.** The only frozen weight whose tool-chain is coherent with a positive-excess class. No pre-reg. |
| mechanized DEX | **+1** | dealer-positioning-strategist → `options_structure_dex` | **−19.8pp** (n=39, BH n, **NEGATIVE**) | −0.8pp | 0.625 (16) | **0.348 (23)** | `dealer_positioning` real 0.50 / claim 0.60 / **excess −6.2pp** / n=16 / BH n | **OUTCOME-CONTRADICTED.** Largest negative class-ctrl marginal this run; collapses in the only down-leaning stratum. → **pre-reg C44**. |
| cum-flow intent-screened | **+1** | signal-confluence-quant → `historical_cumulative_premium_flow` | **+7.8pp** (n=120, BH n, SUPPORTIVE) — **ubiquity 0.58**, just under the 0.60 confound flag | +7.6pp | 0.474 (78) | 0.548 (42) | (base citation; with≈without is mechanically muted) | **MEASUREMENT-CONFOUNDED.** Cited on 58% of decided rows → +7.8 reads as base-rate, not clean edge. Hygiene, not a weight cut. → **pre-reg C45**. |
| multileg | **+2** | multileg-strategist → `hot_chains_multileg` | **−12.7pp** (n=31, BH n, **NEGATIVE**) | −9.6pp | 0.450 (20) | 0.273 (11) | `multileg_directional` real 0.353 / claim 0.555 / **div +20.2pp** / **excess 0.0** / n=17 / p=0.154 **BH n** | **UNSUPPORTED — overclaimed 20pp, delivers exactly SPY.** *Change vs 06-20:* the class was BH-SURVIVING then (0.17, n=12, −38.8pp); this run it is **no longer BH-surviving** (p=0.154). Lie weakened, weight still unjustified. → **C40 carry-forward**. |
| signal-confluence corrob. | +1 | signal-confluence-quant → `insights_signal_confluence` | +2.1pp (n=50, BH n, SUPPORTIVE) | — | — | — | composite re-count of upstream lanes | context only; ~neutral; no action. |

**Read.** Of the four signed structural weights, exactly **one (+3 accumulation-conjunction) earns its
points** on measured contribution; **+1 DEX and +2 multileg are net-negative class-controlled**; **+1
cum-flow is positive-but-confounded**. None survives BH (no tool has, for the 4th audit running), so
every grade is **structural, not statistically actionable** — it feeds a pre-registration, never an
edit.

---

## 2. Tier-cut monotonicity

Realised WR per integer raw score (all eras, `score_table`):

`-3→1.00(2) · -2→1.00(1) · -1→0.17(6) · 0→0.50(40) · 1→0.57(37) · 2→0.37(27) · 3→0.47(19) ·
4→0.41(27) · 5→0.63(8) · 6→0.42(12) · 7→0.67(6) · 8→0.29(7) · 9→0.67(6) · 10→0.00(3) · 11→0.33(3) ·
12→0.00(1)`

Collapsed into the **frozen cut bands** (raw-score basis, all eras):

| frozen band | raw range | n | realised WR |
|---|---|---|---|
| **HIGH** | ≥9 | 13 | **0.385** ⟵ worst band |
| MEDIUM | 7–8 | 13 | 0.462 |
| LOW | 3–6 | 66 | 0.455 |
| DROP | ≤2 | 113 | **0.487** ⟵ best band |

**Monotonicity status: FAILED / INVERTED.** Required HIGH > MEDIUM > LOW > DROP. Observed **DROP 0.487 >
MEDIUM 0.462 > LOW 0.455 > HIGH 0.385** — the ranking is *reversed at both ends*: the highest-scored
band is the worst, the dropped band is the best. The recorded-`tier` ladder agrees (HIGH 0.143 / MED
0.526 / LOW 0.455 / DROP 0.487, Phase 3) and the inversion is now **three consecutive audits** (06-12
HIGH 0.222; 06-20 0.143; 06-27 0.143).

**The ≥9 collapse.** Within the HIGH band the only supportive cell is **raw=9 → 0.667 (n=6)**; strictly
above it the rubric's maximum scores are its worst predictor: **raw 10/11/12 → 0% (n=3) / 33% (n=3) / 0%
(n=1)**. The top of the conviction ladder is anti-predictive.

**Mechanism (Phase 3).** The 7 HIGH-tier decided calls are 4 semis/small-cap shorts (SMH×3, IWM) 0-for-4
+ 2 faded longs (AAPL, ORCL) + 1 MSFT win — i.e. the **negative-selection short book wearing a HIGH
badge**. The inversion is the short problem concentrated at the top of the score. *Edge-before-
calibration note:* this is an **edge** failure (the rubric routes points to a beta-short book), not a
calibration artifact — `bearish_flow` even *beats* its own claim (real 0.54 / claim 0.42) yet runs
**−21.7pp** vs a free SPY short.

**BINDING PROVENANCE.** All 13 raw-≥9 rows are **pre-freeze** (`rubric_version=None`; 0 from 2026-06-12).
**The frozen ≥9 cut is UNGRADED on its own outcomes.** The inversion above grades the era the freeze
already replaced → it cannot drive any edit; it can only sustain the carry-forward HIGH-cut
pre-registration (**C41**) and the freeze.

---

## 3. Freeze-lift check

**Does this audit accrue ≥30 resolved POST-2026-06-12 calls?** `post_freeze_decided = 58` → **YES, the
count threshold is met.** But the gradeable content is the wrong strata:

| frozen band | post-freeze decided n | WR |
|---|---|---|
| HIGH (≥9) | **0** | — |
| MEDIUM (7–8) | **0** | — |
| LOW (3–6) | 5 | 0.60 |
| DROP (≤2) | 53 | 0.491 |

raw≥9 post-freeze = **0**. The frozen **HIGH and MEDIUM tiers have n=0 resolved calls in their own era.**

**Verdict: FREEZE-LIFT CANNOT RUN — KEEP THE FREEZE.** Although ≥30 post-freeze calls exist, **0** of
them populate the HIGH/MEDIUM bands or clear raw≥9, so the tier monotonicity that a lift must demonstrate
is **structurally ungradeable on frozen-era outcomes** (HIGH≥MED is undefined with both cells empty). The
frozen rubric has produced only LOW/DROP calls — it is doing what the freeze + half-cap intend (denying
the sizer the top bands that historically invert). Post-freeze book: WR 0.50 / n=58 / **excess −2.3pp** —
~coin-flip, slightly negative; **no demonstrated post-freeze edge to justify a lift.**

**P0.6 out-of-regime half-cap — graded, KEEP.**
- `out_of_regime` half-capped names: WR **0.30** / excess **−16.7pp** (n=10) → the cap down-sized losers
  (protective). `in_regime`: WR 0.477 / excess +2.5pp (n=195).
- Rubric regime-gate: gated WR 0.542 / excess +5.5pp (n=24) vs ungated 0.459 / +1.4pp (n=181) → the
  regime gate adds ~+4pp WR and excess. Supportive of keeping regime gating.
- **Half-cap is binding:** 0 `full` `final_size` across all 257 rows (24 starter / 12 half); 5 rows
  carried `pre_risk_size=full`, **all capped** down to starter/half.
- **GATES discipline:** the protective `out_of_regime` arm sits at exactly **n=10**, on the <10-thin
  boundary — per the never-loosen-a-protective-gate-on-thin-data rule this is **KEEP, do not lift**, and
  the protective read is **P1, not robust**.

---

## 4. Pre-registration lane (C-numbered; decided by a FUTURE audit on data that does not yet exist)

Each entry: {rubric line/cut · direction · mechanism · **acceptance bar = cross-regime ∧ n≥30/arm ∧
BH-surviving FDR 0.10** · decision window = future dates}. **None is applied now.**

### New this audit

- **C44 — `+1 mechanized DEX` (`options_structure_dex`) weight is too high / should gate.**
  *Direction:* reduce toward 0 or gate the +1 on a confirming flow leg. *Mechanism:* class-controlled
  marginal **−19.8pp** (n=39, NEGATIVE) and the standalone DEX read collapses to **0.348 (n=23)** in the
  pullback stratum while only the up-leg (0.625, n=16) carries it — i.e. DEX trajectory is reading tape
  beta, not dealer-flow edge, off-uptrend. *Acceptance bar:* cross-regime ∧ n≥30 per arm ∧ BH-surviving
  FDR 0.10. *Decision window:* first audit with ≥30 resolved DEX-cited calls, ≥1 arm out-of-uptrend.
  *Note:* single-engine, BH-null this run → register only.

- **C45 — `+1 cum-flow intent-screened` (`historical_cumulative_premium_flow`) contribution is
  ubiquity-confounded.** *Direction:* hold the weight; **re-measure** its marginal on a base-rate-
  discounted basis. *Mechanism:* cited on **120/205 = 58%** of decided rows (ubiquity 0.58, abutting the
  0.60 confound flag) → `with ≈ without` is mechanically muted; the +7.8pp is plausibly base-rate, not
  clean signal. *Acceptance bar:* the tool's class-controlled marginal stays ≥ +5pp **after** restricting
  to rows where it is not the reflexive base citation (ubiquity <0.40 sub-sample), cross-regime ∧ n≥30 ∧
  BH-surviving. *Decision window:* future audit after citation-hygiene reduces its firing frequency.
  *This is a measurement pre-reg, not a weight cut.*

### Carry-forward (prior pre-registrations — bar status this run)

- **C40 — `+2 multileg_directional` weight too high (06-20).** **BAR NOT CLEARED.** This run: class real
  0.353 / claim 0.555 / **excess 0.0** / n=17, and — importantly — **no longer BH-surviving** (p=0.154,
  vs 06-20's BH-surviving 0.17/n=12/−38.8pp). The directional lie *weakened*; the weight is still
  unjustified (delivers exactly SPY, overclaimed 20pp). Still single-regime, n<30/arm → **register only,
  do not apply.**
- **C41 — re-confirm the `≥9` HIGH cut (06-20).** **BAR NOT CLEARED.** 3rd straight inverted audit
  (HIGH band 0.385 < every other band), but **all evidence pre-freeze; 0 post-freeze raw≥9 calls.** The
  cut cannot be confirmed *or* refuted on its own era. → **keep the freeze + half-cap.**
- **C42 — vol-component ≥0.80 quotes ungradeable pending substrate + true IV-vs-RV (06-20).** **BAR NOT
  CLEARED.** The two BH-surviving miscalibrations are both vol classes (`earnings_vol` claim 0.88→real
  0.38, n=29; `high_iv_rank` claim 0.83→real 0.36, n=11), but both are predominantly vol-mode,
  **RV-direction-proxy-resolved** — the realised is proxy-clouded (no proxy turns a true 0.85 into 0.37,
  but the exact figure is not clean P&L). The fabricated ≥0.80 quote (28/33 `win_rate_source=backtest`,
  the substrate quarantined 06-12) still reaches the sizer. *Fix is **emission** (bind the 0.80 ceiling at
  emit) — a hygiene rec for Phase 7, not a frozen-weight retune.* Hold C42 until (a) substrate quarantine
  lifts with a clean cross-regime backtest **and** (b) envelopes carry `implied_move` for true IV-vs-RV.
- **C43 — schema-additive (`dp_block_to_float_ratio`, `insider_cluster_flag`) to make fz C16/C18
  testable (06-20).** **STILL OPEN / NA.** Phase 4: C16/C18 NA — fields absent from `calls[]`. Additive,
  backward-compatible; an enabler, not a promotion.

**No prior pre-registration has its bar cleared this audit.** The single-regime + pre-freeze constraints
that gate every bar are both still in force.

---

## Verdict

The frozen rubric is graded, not retuned. **Component layer:** only **+3 accumulation-conjunction** is
measured-supported (+13.6pp, the lone positive-excess class chain); **+1 DEX (−19.8pp)** and **+2
multileg (−12.7pp, excess 0.0)** are outcome-contradicted; **+1 cum-flow (+7.8pp)** is positive but
ubiquity-confounded. **Tier cuts:** monotonicity FAILED for the 3rd straight audit (HIGH band 0.385 =
worst, DROP 0.487 = best; ≥9 collapses to 0/33/0% above raw=9) — but **all raw-≥9 evidence is pre-freeze,
so the frozen cut is ungraded on its own outcomes.** **Freeze-lift:** 58 post-freeze decided clears the
count threshold, but the frozen HIGH/MEDIUM bands hold **n=0** → freeze-lift **cannot run; KEEP the
freeze**; the P0.6 half-cap is binding and aggregate-protective (out-of-regime −16.7pp, n=10 thin → KEEP,
don't loosen). **Pre-registrations:** new **C44** (DEX weight) and **C45** (cum-flow ubiquity
re-measurement); carry-forward **C40** (multileg, lie *weakened* to BH-null), **C41** (HIGH cut),
**C42** (vol quote / emission ceiling), **C43** (schema enabler) — **none cleared.**

**Output:** `phase_5_schema.md` · `phase_5_schema.jsonl`.
