# Applied — 2026-08-22 audit recommendations

Applied by a separate, human-approved upgrade pass (the audit itself is propose-only and
edited nothing outside `analyses/audit/2026-08-22/`). **All changes are freeze-safe:** no rubric
weight, no tier cut, and no gate membership was touched. The rubric stays frozen at
`2026-06-12`.

**There was no P0 this cycle** — the audit found none. All three P1 items shipped.

---

## P1 #1 — short-thesis *generation* restored to the P0's stated intent ✅

| file | change |
|---|---|
| `.claude/agents/risk-monitor.md` | Two sub-bullets under the `SHORT direction → watch_only` rule: (a) the routing is a **terminal sizing decision, never a Phase-1 screening decision** — a short clearing the entry bar must reach `calls[]` with full `raw_score` / `score_components[]` / 9-key `gate_verdicts` / `dominant_signal_class` and `final_size: watch_only`; (b) the **measured drift**, with the self-invalidation argument. |
| `.claude/commands/daily-analysis.md` | **GENERATION FLOOR** paragraph appended to the Step-5 `SHORT-direction routing` block. |
| `.claude/commands/weekly-analysis.md` | Same paragraph on the weekly multiplier-table equivalent. |

**Evidence (Phase 6.5).** Compliance with the *letter* perfect for a third cycle: 28 post-P0
shorts, 25 `watch_only` + 3 `skip`, **0 sizing violations**, counterfactual preserved 28/28. But
short-thesis **generation halved** — short share of the board **32.0% → 17.6%** (Fisher
two-sided **p = 0.00035**), and **holding the regime bucket fixed at `uptrend`, 31.3% → 17.4%
(p = 0.0045)** — regime does not explain it. The rule's own revisit trigger reads a *paired*
McNemar on resolved short rows (`ALL / short` **p = 0.0026**, −14.5pp, BH-surviving, n=193);
starve the lane and the rule becomes unfalsifiable.

**Deliberately not changed:** the routing itself. Shorts still never size. This is about what
reaches the envelope, not what gets traded.

## P1 #2 — `vol_long` canonicalized ✅

| file | change |
|---|---|
| `schemas/decision_envelope.schema.json` | New canonical class **`vol_term_dislocation`** (18 total); new aliases **`vol_long` → `vol_term_dislocation`** and **`vol_short` → `vol_term_dislocation`**; `description` extended with the rationale below. |
| `.claude/agents/signal-confluence-quant.md` | Class list gains `vol_term_dislocation`; new **"A direction is not a signal class"** block naming the 5 drifted rows and the reason for a new class rather than a fold-in. |

**Evidence.** The 08-15 P2 #7 fix collapsed off-list labels **14 → 1**, but the survivor was
**new**: `vol_long` on 5 rows (2026-08-18 LITE / NBIS / AMAT / CRWV / SNDK). `vol_long` and
`vol_short` are values of the **`direction`** field — emitting one as a class is a category
error, and each new off-list label re-fragments a class denominator below the audit's
decided-N ≥ 8 floor.

**Why a new class rather than folding into `high_iv_rank` / `event_vol`.** `high_iv_rank` is one
of the five `x-backtest-supported-classes`. Mapping long-vol dislocations into it would
re-authorize `win_rate_source: backtest` quotes on rows `signal-backtest` cannot measure —
**silently undoing the 2026-08-15 P1 #2 class-support check**. Verified after the edit: a
`backtest_clean` source on `vol_term_dislocation` **warns** (`does not support (supported:
[bearish_flow, bullish_flow, dark_pool_accumulation, high_iv_rank, volume_spike])`), so the new
class correctly takes the `win_rate: null` + `NA(substrate)` path — which is what all 5 rows
already did.

Historical envelopes are **not** rewritten; the validator warning on them now names the target
(`… is not canonical — emit 'vol_term_dislocation'`).

## P1 #3 — confirmation leg required before a hygiene-corrected label sizes a vol trade ✅

| file | change |
|---|---|
| `.claude/agents/vol-surface-scout.md` | New **CONFIRMATION LEG** block: when the hygiene-corrected shape is the proximate justification, require ≥1 independent leg — **VRP sign agreement** (agreement, not mere non-contradiction), **IV-vs-RV gap** with a stated margin, or **flow alignment** in the same structure/tenor. Name the leg and its number in `bias`. No leg ⇒ `watch_only`. |
| `.claude/agents/earnings-scout.md` | Same rule on the verdict path; no leg ⇒ **SKIP** with reason "hygiene kink unconfirmed." `analyst-vs-flow` explicitly excluded as a leg — it is a *direction* signal, not a vol-richness one. |

**The hygiene run itself stays MANDATORY in both agents.** The correction is always applied; it
just no longer *sizes* on its own. Frozen `vol_term_structure(+/−)` point, the `earnings_vol`
0.55 ceiling and every tier cut untouched.

**Evidence — four independent instruments on one lane.** Phase 4: `scripts/term_structure_hygiene.py`
**−16.9pp, n=42, p=0.003 — the first BH-surviving tool result in twelve cycles**, with the rest of
the vol toolchain negative in a block (`term-skew` −10.5/n=93, `front-end-iv-ratio` −10.4/n=40,
`iv-term-structure` −4.8/n=64, `insights earnings-play` −11.2/n=12). Phase 5.1:
`vol_term_structure(+/−)` **−10.3pp on n=137, negative in both tapes** (−6.1 up / −13.4 down).
Phase 2: `vol` 36.7% vs a 40.2% book, **`vol_short` 34.0%**. Phase 3: `earnings_vol` 0.87 → 0.38
(n=130, BH p<0.001).

**Confound recorded in both agent files, not buried:** 36 of the tool's 42 rows are August 2026
(weakest month, 0.318), and its sign is opposite the same script's +34.1pp/n=9 one cycle earlier
under looser citation normalization — this is the first clean measurement. Within-August control
holds (0.194 n=36 vs 0.380 n=71) but is single-regime. **Registered as C61; if C61 fails its bar
this rule reverses in one edit.**

---

## NOT applied (deliberately)

| item | why |
|---|---|
| **P2 #4** fundamentals `veto_reason[]` instrumentation | P2. `veto_fp_rate` has inverted past the book (0.562 → 0.500 → 0.474 → **0.545**, VETO 0.545 > CONFIRM 0.391) but n=22, and **C24 forbids acting on thin gate-effectiveness data**. Watch. |
| **P2 #5** mandatory `dp_block_to_float_ratio` emission | P2. C16 finally has data (9 decided, perfect rank separation, p=0.028) and is pre-registered as **C62 with the threshold fixed at 0.0010**. Raising emission accelerates the test but is not itself a finding. |
| **C56** `[0.55,0.65)` re-derivation | **19 of a required 30** post-fix decided rows, unmoved. Same pooled-denominator trap that caught two prior audits. |
| Any rubric weight / tier cut | Freeze holds — **0 BH survivors in the 19-line component family, 12th cycle**. |
| Sizing the long book | `ALL / long` **+13.9pp, p=0.0003, BH-surviving, 4th cycle, both tapes** — but the tier ladder that would carry it is inverted. Standing strategic question, not a patch. |

## Verification

- `python3 -m unittest discover -s scripts/tests -p 'test_*.py'` → **423 tests, OK**
- All **76/76** decision envelopes still validate clean
- New class round-trip verified: `vol_term_dislocation` validates as canonical **and** still
  warns on a `backtest`-sourced `win_rate` (the P1 #2 check is intact)
