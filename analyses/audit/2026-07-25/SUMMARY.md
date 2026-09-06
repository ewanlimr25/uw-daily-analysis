# Calibration Audit — 2026-07-25

Dataset: **526 verbatim envelope calls** (52 `decision.json`, 43 daily + 9 weekly; 52/52
validate clean), 153/155 tickers OHLC-resolved path-aware, **440 decided**, **0
`Σpoints≠raw_score` violations**. Strata never pooled: pre-freeze 05-25 (54) / 05-30 (69)
/ post-0606 (28) / **FROZEN 2026-06-12 (375)**. 8th edge audit — and the first in which
**both tapes exist in size** (159 up-tape vs 281 down-tape decided rows). The down-tape
experiment three audits pre-registered finally ran.

## Top 3 schema flaws

1. **The benchmark-excess column is 71% benchmark.** Across 34 strata cells,
   `excess = +36.5 − 80.0 × spyWR` (R² 0.64; pure artifact = −100), implying
   β(bookWR|spyWR) = **+0.20**. `bearish_flow` books 0.533 up-tape / 0.526 down-tape — a
   0.7pp move — while its excess swings 15.6pp; `dark_pool_accumulation` books 0.400 in
   *both* while its excess swings 23.3pp. **The "non-stationary edge sign" that headlined
   07-11 and 07-18 was the denominator, not the book.** Phase 3d. → C49, **P0 (auditor)**.
2. **The live calibration defect is the mid-band, not the old 0.88s.** All 23 quotes above
   0.80 are *pre-cap legacy* — the 2026-06-06 ceiling binds perfectly (post-freeze max =
   0.80 exactly, zero violations). But **[0.55,0.65) realises 0.133 on 15 post-freeze
   rows**, and 0.55 is the modal post-freeze quote. The rubric's most-used confidence
   statement is anti-predictive. Phase 3.3b. → P1, sizing-procedure (in scope under freeze).
3. **The frozen rubric has emitted 0 HIGH and 0 MEDIUM for a 6th straight cycle** (375
   post-freeze rows → 32 LOW, 343 DROP). Freeze-lift is not unsatisfied, it is
   *structurally unrunnable*. Tier order fails a 4th time: HIGH 0.143 < LOW 0.402 <
   DROP 0.431. Phase 3.2 / 5.3. → Keep freeze, P1.

## Top 3 tool-tier surprises

1. **8th consecutive BH-null tool table** — no tool clears p=0.197. `institutional-accumulation`
   went −22.2 → +18.2 → +9.5pp across three audits; `block-stratified` +15.9 → −2.3 →
   **+1.6pp with WR-with 0.42 vs WR-without 0.42**, a perfectly uninformative gate. The
   07-11 "isolate block-stratified" pre-register stays refuted. Phase 4.
2. **The 34% missed-gate "drift" is an auditor bug.** Every miss is a DROP row (0/7 HIGH,
   0/20 MED, 0/94 LOW, 211/374 DROP). `risk-monitor.md` needs no patch. Phase 6.5 → C54.
3. **C16 and C18 have been untestable for three audits** because the envelope never
   carried the fields; **C15 is untestable by construction** — zero of 18 short rows clear
   the high-short-interest threshold on a mega-cap universe. Phase 4.

## What we'd do Monday

Nothing to the live trading files — but for the first time the reason isn't "wait for a
down-tape." We got one, and it delivered two things. First, the **long book has a real,
BH-surviving, row-matched edge** over a same-window SPY long (McNemar p=0.008 overall,
p=0.004 in the up-tape) — the only statistically defensible edge this system has ever
produced. Second, the short book does not: in a falling tape the fleet was positioned
*with* the tape only **39.7%** of the time, its selected shorts trailed a naive index
short by 13.7pp (p=0.12, ns — suggestive, not proven), and the **sized book was the worst
pile in the system at 0.294 against a DROP pile of 0.411**. Six audits of empty boards
keep grading correct.

The real work is on the auditor, not the subject. Three consecutive headline findings
were substantially artifacts of a benchmark that moves four times as much as the book —
so the fix is to lead with tape-conditioned book win rate and paired McNemar, demote raw
excess, and **close C19 as refuted rather than carrying it a seventh cycle**. Keep the
freeze, keep the out-of-regime half-cap (now actionable at n=41 and protective at
−11.9pp), keep every risk gate (all effective; `cluster` at −29.3pp), and leave Kelly off
at n=26. Then fix the mid-band quote — it is the one live number costing money.
