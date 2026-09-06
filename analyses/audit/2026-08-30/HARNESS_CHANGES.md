# Harness changes made AFTER the checkpoints were written (2026-08-30)

The seven phase checkpoints (`phase_*.md`) and their `.jsonl` companions are the **audit
record for this cycle and stand as written.** The auditor-side code changes below were applied
during the separate upgrade pass and take effect **from the next cycle** (2026-10-03), when
the scripts are copied forward.

**If you re-run this folder's scripts, the numbers will differ from the checkpoints. That is
by design, and here is exactly how.**

| script | change | effect on a re-run |
|---|---|---|
| `phase2_resolve.py` | **C64** — `resolution_mode == "pin"` now returns the **settlement** rule as the headline `outcome`; the touch rule is retained as `outcome_touch` / `touch_realised_return_pct`, plus `pin_rule: "settlement"`. | `opex_pin` moves **18.2% → 63.6%** (11 rows, +5 WINs). Book WR moves ~+0.7pp. Nothing else changes — only 11 rows resolve through this path. |
| `phase1_parse.py` | Carries `dp_block_to_float_ratio`, `implied_move`, `insider_cluster_flag` and the new `fundamentals_verdict_reason` into the JSONL. **Root cause of the C16 misreport** — the fields were emitted; the parser dropped them. | `phase_1_inventory.jsonl` gains 4 keys. **Already re-run; row count, tallies and every previously-reported figure are unchanged**, so the Phase-1 checkpoint remains accurate. |
| `phase4_tools.py` | **P2 #2** — C16 block reads `calls[].dp_block_to_float_ratio` (schema path) instead of `fz_context.…`, and reports the C62 arms against the **pre-registered, un-refit 0.0010** threshold. | Reports `populated 13 / decided 11 / above 2 / below 9` instead of `NA — not in envelope`. Matches Phase 4.4, which was computed by hand from the schema path. |
| `phase6d_rec_followthrough.py` | **P1 #3** — standing short-generation table (overall + regime-controlled) with two-sided Fisher, framed so **both** failure modes are visible: starvation *and* quota. | New output block. Reproduces Phase 6.5 exactly. |

## Deliberately NOT re-run

`phase_2_outcomes.jsonl` and every downstream `.jsonl` are left as the checkpoints describe.
Re-running Phase 2 under C64 would cascade a changed `opex_pin` through Phases 3–6 and leave
the `.md` checkpoints disagreeing with their own data files. The checkpoints already report
**both** pin rules explicitly (Phase 2, C59 decision table) and annotate the 18.2% as an
instrument artifact everywhere it appears, so no reader is misled.

## For the next audit

- **`opex_pin` figures from 2026-08-22 and earlier were computed under the TOUCH rule and are
  SUPERSEDED, not comparable.** Do not chart them against post-C64 values.
- `fundamentals_verdict_reason` will be `null` on every pre-2026-08-30 envelope by design.
  Grade it on post-change rows only — the same discipline C56 keeps failing to get.
- **C63** (short-vol routing) is now the live registration to grade: post-change `vol_short`
  peer-excess ≥ −5pp on n ≥ 40 decided rows across ≥ 2 regime buckets. Build the peer
  benchmark with `phase_3f_peer_control.json`'s method — **the unselected same-date
  single-name peer set, not SPY**; the index benchmark is biased ~8pp conservative.
