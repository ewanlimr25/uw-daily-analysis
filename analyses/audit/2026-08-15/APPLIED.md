# Applied — 2026-08-15 audit recommendations

Applied by a separate, human-approved upgrade pass (the audit itself is propose-only and
edited nothing outside `analyses/audit/2026-08-15/`). **All changes are freeze-safe:** no
rubric weight, no tier cut, and no gate membership was touched. The rubric stays frozen at
`2026-06-12`.

---

## SHIPPED

### P1 #1 — one canonical tool id per `score_component` ✅

| file | change |
|---|---|
| `schemas/decision_envelope.schema.json` | `source_tool` gains a description + **`x-canonical-tools`** (54 ids: the `uw` CLI surface, `scripts/*.py`, `fz`, `yahoo chart-api`). Deliberately **not** a hard enum — that would retroactively fail-validate the historical envelopes that *are* the calibration dataset (same reasoning as `dominant_signal_class`). |
| `scripts/validate_decision.py` | `_load_canonical_tools()`; two new non-fatal warnings — (a) `source_tool` containing `+` / `/` / `and` / `,` (concatenated citation), (b) off-list spelling. |
| `.claude/agents/signal-confluence-quant.md` | output contract now requires exactly one canonical id per component; **when a rubric line rests on several tools, emit one component PER TOOL** (split the points, or dominant tool carries them and corroborators emit `points: 0`). `Σ points == raw_score` is unchanged. Worked example added to the `score_components` JSON block. |

Evidence: 122 distinct citation strings / 1,225 instances, 60 singletons, 52 concatenations;
**155 citation instances trapped in n<5 labels**; same tool at opposite tiers under two
spellings (`scripts/term_structure_hygiene.py` +34.1pp vs `iv-term-structure hygiene` −39.7pp).

### P1 #2 — no backtest-sourced `win_rate` on classes `signal-backtest` cannot measure ✅

| file | change |
|---|---|
| `schemas/decision_envelope.schema.json` | `win_rate_source` gains **`x-backtest-supported-classes`** = `bullish_flow, bearish_flow, high_iv_rank, volume_spike, dark_pool_accumulation` (verified against `uw historical signal-backtest --help`). |
| `scripts/validate_decision.py` | warns when `win_rate_source ∈ {backtest, backtest_clean}` on any other class (alias-collapsed first). |
| `.claude/agents/signal-confluence-quant.md` | new **Step 0 class-support check** ahead of the clean-query protocol: unsupported class ⇒ do not call the tool, emit `win_rate: null` + `NA(substrate)`, take the Step-e sizing path. |

Evidence: `earnings_vol` is not a supported class yet quoted **0.87 / realised 0.394 on n=109**
(BH p<0.001, 5th appearance) with 12 of 13 quoted rows citing `backtest`. **The rule catches 37
such quotes across the corpus.** Recorded distinction: `high_iv_rank` **is** supported — its
narrower defect (retired `backtest` source on 8 of 16 rows) is already covered by the 2026-06-20
`sizing_eligible_quote` assertion.

### P1 #4 — C15 and C18 retired ✅

| file | change |
|---|---|
| `analyses/audit/2026-05-25/improvement_criteria.md` | C15 **RETIRED** (option (ii) of its own 2026-08-01 re-scope); C18 **RETIRED** as refuted-by-zero-variance; new **status board** for C15–C18 + transferable lesson. |
| `.claude/agents/fundamentals-gate.md` | squeeze axis → permanent advisory; C18 leg dropped from the backfill duty; **C16 backfill duty sharpened** (it is the one live `fz` promotion and it is starved, not refuted). |

**C15's stated blocker is corrected here.** The 2026-08-01 entry blamed `short_float` — wrong.
Post-fix `short_float` populates on 147 rows with real variance (max **30.22%**, 7 rows ≥20%).
The binding leg is **`days_to_cover ≥ 5`, which clears on 2 of 147 rows and never on the high-SI
names**, because the C12 ADV floor guarantees the volume to cover fast. Decisive third reason:
C15's action was "SHORT thesis → −1 tier", and **since the 2026-08-01 P0 no directional short is
sized at all** — the gate is a no-op by construction.

C18: `insider_cluster_flag` observed **20×, `False` every time**. Zero variance cannot gate a
conjunction at any n. C16 and C17 stay OPEN.

### P2 #7 — `dominant_signal_class` enum ✅ (emitter side)

`.claude/agents/signal-confluence-quant.md` now lists the full canonical set and points at the
schema as source of truth, with the drift-label alias map called out. The schema/validator side
already shipped 2026-08-01; **the emitter was the unapplied half**.

### P2 #8 / C59 — auditor pin-resolution rule ✅ **and its bar cleared in-cycle**

`analyses/audit/2026-08-15/phase2_resolve.py` now emits **both** rules for pin rows:
`outcome` (legacy touch: any ±1R excursion = LOSS) and `outcome_settle` (distance from entry at
window END), plus `settle_dist_pct` and `pin_rule_divergent`.

**Result — C59's ≥3-divergence bar is cleared at 5 of 9:**

| | WR | n |
|---|---|---|
| touch rule (legacy, headline) | 0.111 | 9 |
| settlement rule (C59 candidate) | **0.667** | 9 |

**PFE settled at 0.00% from entry and was scored LOSS** on a 3.34% intraday brush; XLF 0.05%,
NVDA 0.12% / 0.21%. The headline was **left on the touch rule** so this cycle stays comparable
with the prior ten audits — the switch is for the next audit, per the registration. `phase_3` and
`phase_5` carry correction blocks: **the `opex_pin` 0.111 and the `opex-pin-strategist` −23.7pp
are auditor artifacts and must not be cited as findings about the lane.**

### P1 #5 / P1 #6 — keep the freeze, keep the half-cap ✅ (decisions, no edit)

Recorded in `phase_5_schema.md` §5.4 / §5.5. Freeze-lift is **unrunnable by construction** for a
9th cycle (425 resolved post-freeze calls, **0 decided HIGH / 0 decided MEDIUM**) — and the
freeze is not the blocker, the conjunction requirements are. Half-cap is protective (−9.6pp,
n=43, negative in all six measurements).

---

## WITHDRAWN

### P1 #3 — re-derive the `[0.55,0.65)` band ❌ **NOT APPLIED**

The recommendation cited **n=49 / realised 0.245 / p = 1×10⁻⁶** — but that is the **pooled
corpus across rubric eras**. C56's bar is **post-fix quoted rows only**, which stand at:

| basis | in-band quoted |
|---|---|
| post starter-floor (2026-07-25+) | **19** |
| post disclosure-rule (2026-08-01+) | **8** |
| **bar** | **n ≥ 30** |

`signal-confluence-quant.md:71` warns about precisely this trap, in writing, because the
2026-08-08 audit fell into it — and this audit fell into it too. Pooling eras to clear a
pre-registration is the same error as the C49 excess-denominator artifact: a bigger, wronger
denominator because it clears a threshold the correct one does not.

**Nothing about the quote changed.** Both live rules keep holding: all 8 post-2026-08-01 in-band
rows resolved `skip`/`watch_only`, zero sized, none cited for an upgrade. The withdrawal and the
corrected counts are recorded in `signal-confluence-quant.md` so the next grader sees that this
trap has now claimed two consecutive audits, with the instruction to **compute the post-fix count
first and write it down before looking at any realised rate.**

---

## Verification

- **70 / 70 decision envelopes still validate** (exit 0). No historical envelope was invalidated.
- New warnings fire correctly and are non-fatal: concatenated `source_tool` (e.g. 2026-07-24
  TSLA/AKAM/FSLR/IWM/BE/IREN), off-list spellings (`uw options-structure dex (dated)`),
  off-list classes (`dealer_positioning_flip`), and **37** unsupported-class backtest quotes
  (first: 2026-05-25 PANW `earnings_vol`).
- **`python3 -m unittest discover -s scripts/tests -p 'test_*.py'` → 423 tests, OK** (was 413;
  **+10 new regression tests** in two classes — `CanonicalSourceToolWarnings` and
  `BacktestClassSupportWarnings` — covering `+`/`/`/`,` concatenation, off-list spellings,
  canonical-is-silent, alias-collapse-before-support-check, `NA(substrate)`-is-silent, and
  never-an-error for both rules).
- **Pre-existing fixture fix:** 14 `source_tool` values in `scripts/tests/test_validate_decision.py`
  used the retired MCP underscore convention (`historical_cumulative_premium_flow`) and tripped
  the new off-list warning in 3 unrelated tests. Canonicalized to `uw historical
  cumulative-premium-flow` etc. Verified first that no test asserts on those literals — they
  appear only as `source_tool` values and in free-text `rubric_line` strings, which are untouched.
- Schema is well-formed: 54 `x-canonical-tools` ids, 5 `x-backtest-supported-classes`.
- No rubric weight, tier cut, or gate membership modified. Freeze intact.
