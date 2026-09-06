# Phase 6 — Decision-Process Audit (2026-08-08)

Voice: buy-side PM post-mortem. Clinical, specific, names the file.

## 6.1 Quant compliance (`signal-confluence-quant.md`)

```
Σ score_components.points  =  raw_score  on  523/523 scored rows   (0 violations)
provenance complete (every component has source_agent + source_tool):  TRUE
sizing-map upgrade violations:  1
```

The single violation is historical and known: **2026-06-05 LLY**, `claimed_wr 0.392` →
map-implied `starter`, emitted `half`. It predates the 07-25 band tightening and sits in
the `era_0530_0605` stratum. No post-freeze violations. **No drift patch needed.**

Sizing map audited against the rule live on each row's own `report_date` (a pre-2026-07-25
row quoting in [0.55,0.65) at `half` is era-correct, not a violation), and `quarter` is
included in the size order.

## 6.2 Gate firing rates

| gate | present/fired | rate |
|---|---|---|
| regime | 353/370 | 0.954 |
| vrp | 340/365 | 0.932 |
| panic | 349/365 | 0.956 |
| cluster | 350/369 | 0.949 |
| sector | 341/364 | 0.937 |
| fundamentals | 295/372 | 0.793 |
| event_risk | 369/378 | 0.976 |
| debate | 250/263 | 0.951 |
| rubric_regime | 270/270 | 1.000 |

## 6.3 Gate effectiveness (C24) — does the gate HELP, not just FIRE

A gate is **effective** when the names it fired on realise a *lower* win rate than the
names it left alone. All nine:

| gate | fired WR (n) | not-fired WR (n) | Δ | verdict |
|---|---|---|---|---|
| cluster | 0.379 (306) | 0.632 (19) | **−25.3pp** | effective |
| panic | 0.390 (305) | 0.562 (16) | −17.2pp | effective |
| debate | 0.365 (208) | 0.538 (13) | −17.3pp | effective |
| vrp | 0.384 (297) | 0.542 (24) | −15.8pp | effective |
| regime | 0.394 (310) | 0.500 (16) | −10.6pp | effective |
| sector | 0.391 (297) | 0.478 (23) | −8.7pp | effective |
| fundamentals | 0.395 (261) | 0.418 (67) | −2.3pp | effective (weak) |
| event_risk | 0.391 (325) | 0.778 (9) | −38.7pp | **ADVISORY** (n=9 arm) |
| rubric_regime | 0.373 (228) | — (0) | — | **ADVISORY** (no counter-arm) |

**Every gate with an evaluable arm grades effective. None is anti-effective.** Fourth
consecutive cycle. `cluster` remains the single most valuable gate in the stack at
−25.3pp. This is the mechanism behind the DROP-beats-book result: the risk stack is
correctly identifying the losers and pushing them out of the book.

**Do not loosen anything.** Per the C24 hard rule, a gate's value is insurance against the
regime not yet in the dataset.

## 6.4 VETO false-positive rate and debate effectiveness

```
VETO      WR = 0.500 (n=18)
CAUTION   WR = 0.355 (n=93)
CONFIRM   WR = 0.407 (n=91)
book      WR = 0.408
```

`veto_fp_rate` reads **0.500 on n=18** — VETO'd names would have won as often as the book,
which is anti-effective on its face. The 08-01 audit recorded this as MONITOR at n=16; it
is now n=18 and unchanged in character. The three reasons not to act still hold: (i) n=18
is barely past the C24 evaluable floor, and the rule requires ≥10 decided *and* forbids
loosening on thin data; (ii) the same agent's **CAUTION** verdict grades correctly and
strongly (0.355 vs CONFIRM 0.407 — a −5.2pp discrimination), so the gate's underlying
signal is real and only the top-severity bin reads odd; (iii) most VETO'd names were killed
by other gates anyway, so "would have won if sized" is not their true counterfactual.
**MONITOR. Re-grade at n≥30 VETO'd-and-decided. Do not weaken.**

```
DEBATE:  bear won → WR 0.312 (n=80)   |   bull won → WR 0.125 (n=8)
```

The debate gate is **not theatre** — names where the bear prevailed realise 0.312 and the
gate correctly downgrades them (−17.3pp vs not-fired). The bull-won arm at n=8 is too thin
to read.

## 6.5 Missed-gate ledger — C54 decomposition

> **Denominator rule (C54).** The missed-gate *rate* is computed over **non-DROP rows
> only**. DROP names are eliminated before the full risk stack runs — the fleet's intended
> early-exit optimization. Counting it as non-compliance measures efficiency as drift, and
> doing so mis-flagged `risk-monitor.md` in prior cycles. Each gate is also graded only
> from the date it became a serialized obligation (`debate` and `rubric_regime` post-date
> the freeze; their absence in earlier envelopes is not drift).

| gate | HIGH | MEDIUM | LOW | **NON-DROP (headline)** | DROP (own line) |
|---|---|---|---|---|---|
| regime | 0/7 | 0/20 | 0/111 | **0/138 = 0.000** | 256/488 = 0.525 |
| vrp | 0/7 | 0/20 | 1/111 | **1/138 = 0.007** | 260/488 = 0.533 |
| panic | 0/7 | 0/20 | 0/111 | **0/138 = 0.000** | 261/488 = 0.535 |
| cluster | 0/7 | 0/20 | 1/111 | **1/138 = 0.007** | 256/488 = 0.525 |
| sector | 0/7 | 0/20 | 1/111 | **1/138 = 0.007** | 261/488 = 0.535 |
| fundamentals | 0/7 | 0/20 | 2/111 | **2/138 = 0.014** | 252/488 = 0.516 |
| event_risk | 0/7 | 0/20 | 0/111 | **0/138 = 0.000** | 248/488 = 0.508 |
| debate | 0/0 | 0/0 | 0/49 | **0/49 = 0.000** | 212/426 = 0.498 |
| rubric_regime | 0/0 | 0/0 | 0/49 | **0/49 = 0.000** | 205/426 = 0.481 |

**HEADLINE: 5 missed gates across 1,064 non-DROP gate-obligations = 0.47%.**
**Zero gates exceed the 20% drift threshold. `risk-monitor.md` needs no drift patch.**

For contrast, the DROP-inclusive naive aggregate is **2,518/5,634 = 44.7%** — the figure
C54 exists to forbid as a drift headline. Reporting that number would again mis-flag an
agent whose compliance is, in fact, 99.5%.

## 6.6 Post-P0 cohort gate coverage

Across the 48 post-2026-08-03 rows, all nine gates are absent on exactly the same 22 rows —
a uniform pattern consistent with 22 DROP early-exits, not with selective gate skipping.
The 26 non-DROP rows carry the full nine-gate stack.

## 6.7 — Did the 2026-08-01 recommendations actually land? (Phase 6d)

This section separates *"the agent file was edited"* from *"the emitted data changed."*
The 08-01 audit conflated the two on C18 and reached a wrong conclusion; that is corrected
here.

| rec | status in the emitted data |
|---|---|
| **#1 (P0) shorts → `watch_only`** | ✅ **APPLIED CLEAN.** 6/6 post-P0 short calls routed to `watch_only`; **0** sized violations; counterfactual fully preserved (6/6 carry `raw_score`, `gate_verdicts`, and `dominant_signal_class`). It is routing, not suppression — exactly as specified. |
| **#2 (P1, C55) sector re-source** | ✅ **APPLIED.** Post-P0 `sector_rotation` rows cite the netted `uw risk market-regime` line **4/4**, with **zero** citations of the gross `sector-flow*` family. Pre-P0 rows cited neither explicitly. Outcome effect **ungradeable** — 4 rows, 1 decided. |
| **#3 (P1) `earnings_vol` / `high_iv_rank` quote fix** | ⚠️ **UNVERIFIABLE.** Zero post-P0 rows in either class carry a `claimed_win_rate`, so there is nothing to check. Pre-P0 the defect is intact (0.871 claimed vs 0.404 realised, n=99; 12/13 rows still `win_rate_source: backtest`). The fix may be applied and simply unexercised in a 5-session window — or not applied. Cannot tell from the data. |
| **#4 (P1, C56) `[0.55,0.65)` band** | ⚠️ **PARTIAL.** Post-P0 in-band rows are 2, both `watch_only` (never sized) — the 07-25 starter-floor is holding. But the *quote* was not re-derived: the band still realises **0.233 on n=43** while predicting 0.58. C56 remains open. |
| **#5 (P1) `dp_block_to_float_ratio` + `insider_cluster_flag`** | ⚠️ **EMITTER FIX WORKS; STARVED OF ROWS.** C16 now gradeable in principle, C18 still blocked. See below. |
| **#9 (P2) `dominant_signal_class` enum** | ✅ **APPLIED AND WORKING.** Post-P0: 11 distinct classes, **zero off-list**. Pre-P0: 31 distinct, 14 off-list variants. |

### C16/C18 — correcting the 08-01 audit's measurement, and the real blocker

The 2026-08-01 audit reported *"`insider_cluster_flag` now populates 44/44 post-fix calls —
**C18 unblocked**."* **That number was measured against the wrong denominator.** It counted
rows where the *key* was present, across *all* signal classes. Both fields are only
meaningful for `dark_pool_accumulation` rows — a null on an `earnings_vol` row is correct,
not a defect — so the honest denominator is the 57 accumulation rows in the corpus. Every
one of the 11 that carries the keys:

| date | ticker | `dp_block_to_float_ratio` | `insider_cluster_flag` | `fz` ran |
|---|---|---|---|---|
| 2026-06-23 | CART | null | False | no |
| 2026-07-16 | ASTS / CRNX / DIS | null | null | no |
| 2026-07-17 | ASTS / CDNS | null | False | no |
| 2026-07-30 | AVGO / MA | null | False | no |
| 2026-07-31 | MSFT | null | False | no |
| **2026-08-03** | **GOOGL** | **4.37e-05** | False | **yes** |
| 2026-08-04 | TSM | null | False | no |

**The emitter fix landed and works.** On the single post-fix row where the `fz` lane
actually ran (`fz_context.available = true`), `dp_block_to_float_ratio` is **populated**.
On TSM the `fz` lane did not run, and an explicit null is the contract-mandated
graceful-skip value — correct behaviour, not a bug. My initial read that "the emitter
still writes null" was wrong; the constraint is different and milder.

**The real blockers are two, and they are different for each criterion:**

- **C16 — starved of rows, not of instrumentation.** Only **2** `dark_pool_accumulation`
  rows have been emitted since the fix, and `fz_context.available` is true on just
  179 of 626 calls corpus-wide. At the current rate of ~1 accumulation row per 3 sessions
  with a working `fz` read, reaching a gradeable n will take many months. C16 is on its
  5th untestable audit, but for the first time the reason is throughput, not plumbing.
- **C18 — genuinely blocked, and it is not a sample-size problem.** `insider_cluster_flag`
  is populated on 15 rows corpus-wide and **every single one is `False`.** A boolean that
  has never once been observed `True` has **zero variance** and cannot gate a conjunction
  no matter how many rows accrue. This is not under-powered; it is uninformative. Either
  `fz insider-clusters` is genuinely never firing on this mega-cap universe (the same
  structural problem that makes C15 untestable), or the co-flag is not being read. That
  distinction is worth one debugging session and is the subject of Phase 7 item 4.

**The validator is working correctly** and this correction should not be read as a defect
in it: `scripts/validate_decision.py` emits **92 C16/C18 instrumentation warnings** across
the corpus (e.g. `2026-06-05 JNJ/PGR: dark_pool_accumulation row missing
'dp_block_to_float_ratio' key`). The warnings are non-fatal by design and are concentrated
on historical rows; the recent envelopes I spot-checked simply had no offending rows. The
guard scoped to `fz_context.available is true` has fired zero times because the one row
meeting that condition is correctly populated.

**The generalizable lesson stands, restated accurately:** grade instrumentation by
**population within the rows the field is defined for**, never by key presence across the
whole corpus. The 08-01 error was a denominator error, and it is the same shape as the
C49 denominator artifact this audit exists to police.

## Outputs

`phase_6_decision_audit.jsonl`, `phase_6_missed_gate_c54.jsonl`,
`phase_6b_p0_compliance.json`
