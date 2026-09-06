# Applied — 2026-08-30 audit recommendations

Applied by a separate, human-approved upgrade pass (the audit itself is propose-only and
edited nothing outside `analyses/audit/2026-08-30/`). **All changes are freeze-safe:** no
rubric weight, no tier cut, and no gate membership was touched. The rubric stays frozen at
`2026-06-12`.

**One P0, three P1, two P2 — all shipped.** One item shipped with a **materially different
mechanism than the audit proposed**, because the proposed mechanism was falsified during
application. That is documented first.

---

## ⚠️ P0 #1 — the FINDING shipped; the proposed MECHANISM was falsified and replaced

**What the audit proposed:** an at-entry *expansion veto* — allow short-vol structures only
when the name is not already expanding (`rv10/rv30 ≤ 1.00`, and no more than +0.15 above SPY's
ratio).

**What testing it showed (new artifact: `phase_7b_p0_design_test.md`).** Before writing the
rule into an agent file it was tested against the resolved corpus. It failed:

- The **relative-to-SPY leg ran backwards** — names *calmer* than SPY realised **13.9%**;
  names >0.15 *hotter* realised **37.7%**.
- The **combined veto was net −14.3pp**: ALLOWED 17.6% (n=34) vs VETOED 31.9% (n=94). It
  would have removed 73% of the lane and kept the worse third.
- The absolute leg alone does work weakly and monotonically (≤1.00 → 33.9%, >1.00 → 23.6%),
  **but no threshold anywhere in [0.70, 1.00] lifts the surviving arm above −21pp vs the peer
  benchmark, and every surviving arm keeps a McNemar p < 0.0001.**

**What shipped instead: routing, not filtering** — the same remedy the 2026-08-01 P0 applied
to directional shorts, for the same reason: the deficit is **mis-selection**, uniform across
every conditioning variable tested, not mistiming a gate could catch.

| file | change |
|---|---|
| `.claude/agents/risk-monitor.md` | New terminal-sizing rule: any net-**short-vega** expression → `final_size: watch_only`. Full scope limits, the four-instrument evidence, the three failed falsifications, the veto-was-tested-and-failed note, the exposure figure, the RV-proxy caveat, and the C63 revisit trigger. |
| `.claude/agents/signal-confluence-quant.md` | Mirror rule at the emission layer, so a short-vol call cannot be re-sized by a later gate. Requires the `audit_trail` line to state **what the ladder would have said**. |
| `.claude/agents/vol-surface-scout.md` | "**Routes to `watch_only` — keep proposing them anyway.**" Explicit: never drop a SELL VOL candidate because it can't be sized. |
| `.claude/agents/earnings-scout.md` | Same for SELL VOL verdicts; never collapse a routed SELL VOL into a SKIP (different data). `implied_move_pct` flagged as the highest-value field it emits. |
| `.claude/commands/daily-analysis.md` · `weekly-analysis.md` | Step-5 `SHORT-VOL routing` block beside the existing short-direction one, incl. the interaction note (the older rule excludes short legs *in* vol structures because those aren't directional short alpha; this one covers net-short-**vega** expressions; a short leg inside a *long*-vol structure is covered by neither). |

**Evidence.** `vol_short` books **31.5%** against unselected same-date single-name peers at
**56.6% — −25.1pp on n=111**, paired McNemar **b=2 c=57, p<0.0001**; negative and individually
significant in **4 of 4 regime buckets** (−20.2/−35.1/−23.5/−25.5pp) and 3 of 4 months;
loose-window −33.6pp on n=134, BH-surviving. **Exposure: 20 of the 48 sized rows in the entire
corpus — 42% of every position this fleet has ever taken.**

**Deliberately NOT changed:** `vol_long` / BUY VOL. It measures **+9.5pp** vs the same peer
benchmark (n=43, McNemar p=0.0034) and is **5-for-5 on every sized row**. Every file states
this explicitly, because the obvious over-application of this P0 is to get conservative on
long vol too — which would destroy the one vol result that works.

---

## P1 #1 — log *why* the fundamentals gate VETOes ✅

| file | change |
|---|---|
| `schemas/decision_envelope.schema.json` | New `calls[].fundamentals_verdict_reason` — 10-value enum + null. Backward-compatible; **all 82 existing envelopes still validate.** |
| `.claude/agents/fundamentals-gate.md` | Enum table with when-to-use per value, added to the output contract, plus the rationale and an explicit **"this is not licence to loosen the gate"** (C24). |
| `.claude/commands/daily-analysis.md` · `weekly-analysis.md` | Added to the `calls[]` enumeration — **with a note saying that omission from this exact list is what made the instrumentation trio untestable for three audits.** |

**Evidence.** `veto_fp_rate` **0.524 (n=21)** vs CONFIRM **0.376 (n=117)** and CAUTION
**0.328 (n=131)** — inverted, second straight cycle, past the C24 evaluable floor. Note the
shape recorded in the file: **CAUTION still grades correctly**, so the gate's discrimination
is real and only the top-severity bin reads odd. The gate is unchanged; only its
instrumentation.

## P1 #2 — pin resolution switched to the settlement rule (C59 decided → C64) ✅

`analyses/audit/2026-08-30/phase2_resolve.py` — **auditor-side only, no subject file touched.**
`outcome` is now the settlement rule; the touch rule is retained as `outcome_touch`.
**C59's bar was ≥3 of 9 divergent; measured 5 of 11.** Touch 2/11 (18.2%) vs settlement 7/11
(**63.6%**); four of the five divergent names settled within **0.21% of entry** after brushing
a wing intraday. Takes effect next cycle — see `HARNESS_CHANGES.md`.

## P1 #3 — standing short-generation measurement ✅

`phase6d_rec_followthrough.py` — new table with two-sided Fisher, deliberately framed so
**both** failure modes are visible. **The 08-22 floor worked:** 17.6% → **44.2%** (p=0.0003),
uptrend-controlled 17.4% → **60.0%** (p=0.0007). The command files' stale "⚠️ generation has
halved" warnings were **updated to record the recovery** — leaving a fixed defect described as
live in an agent prompt is itself a defect — and now carry the quota watch-item
(uptrend 60.0% vs a 31.3% pre-P0 baseline, p=0.0422, n=15). **No edit made on n=15.**

## P2 #1 — C18 / `insider_cluster_flag` closed as unmeasurable ✅

`.claude/agents/fundamentals-gate.md`, `.claude/agents/accumulation-hunter.md` — flag observed
**30 times, `False` on all 30**, five consecutive audits, zero variance. Closed rather than
pending: no backfill duty, no promotion path, **no future audit re-tests it.** Field and
computation retained so a genuine `True` would still surface. Both files draw the contrast
with C16 — *correct but rarely emitted* (emission now fixed) vs *emitted fine, always the same
value* — so the two never get conflated again.

## P2 #2 — auditor's C16 lookup path fixed, and its root cause ✅

`phase4_tools.py` read `fz_context.dp_block_to_float_ratio`; the schema and both emitters write
`calls[].dp_block_to_float_ratio`. **The root cause was one level up:** `phase1_parse.py` never
carried the instrumentation trio into the JSONL at all, so every downstream helper looked in
the wrong place and reported the field as unemitted. **It was emitted.** Both fixed; the C16
block now reports the C62 arms against the pre-registered, **un-refit** 0.0010 threshold.
Any prior-cycle "not emitted" claim sourced from that helper is unverified.

---

## Explicitly NOT applied (audit's own list, unchanged)

**C60** — all three statistical conditions pass (BH p=0.001, sole survivor of 24; UP 89 /
DOWN 94; 4 regime buckets) but **only 9 of 183 rows (4.9%) are out-of-sample** and the window
opens **2026-10-03**. Held, unrenegotiated. · **Rubric freeze** — kept (11th unrunnable lift;
0 decided HIGH, 1 MEDIUM in 546 post-freeze rows). · **P0.6 half-cap** — kept (−6.4pp, 8th
straight negative). · **C62** — not promoted (11/30 decided, 2/10 upper arm). · **C61** — not
decided (non-August n=7 of 30; last cycle's confirmation-leg rule kept, recorded as standing
on C61's promissory note). · **C56** — not acted on (21/30). · **Kelly** — stays advisory
(n=27, non-monotone). · **No gate loosened or removed** (all nine effective, −4.0 to −42.0pp).
· **Term-structure tools not demoted** (`term-skew` is +5.3pp *inside* `vol_short`).
· **No agent-file drift patch** (5 missed gates in 1,262 non-DROP obligations = 0.40%).
