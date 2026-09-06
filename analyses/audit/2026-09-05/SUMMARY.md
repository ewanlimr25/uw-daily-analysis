# Calibration Audit — 2026-09-05

**878 verbatim envelope calls** (88 `decision.json`, **88/88 validator-clean**), 205/207
tickers OHLC-resolved path-aware, **751 decided**, **0 `Σpoints ≠ raw_score`, 0 prose
reconstruction**. Eras never pooled (FROZEN `2026-06-12`: 727). Four regime buckets. 14th
audit, 7th cross-regime cycle. **First P0 on the rubric's own arithmetic.**

## Top 3 schema flaws

1. **The frozen tier cuts are unreachable — the rubric is unfalsifiable.** The 2026-06-12
   freeze removed `signal-confluence` from scoring and cut the cum-flow line; mean points per
   component fell **1.391 → 0.512**, mean `raw_score` **3.56 → 0.86**, p90 **8 → 3**, rows ≥9
   (HIGH) **13 → 0 of 727**. The cuts never moved. Daily session-max median **9.0 → 3.0**, a
   step function at the freeze date (**Mann-Whitney z=5.65, p=1.6×10⁻⁸**) with **no recovery in
   any of four regime buckets over 59 sessions**. HIGH now sits 8 points above the post-freeze
   *maximum*. This — not the market — is why the freeze-lift has been unrunnable for seven
   cycles. Phase 5.0 → **P0** (status correction + **C65**; no re-bin).
2. **The vol lane is now closed on both legs, one of them by accident.** `vol_short` books
   **−29.4pp** vs unselected same-date peers (n=129, McNemar **b=2 c=73, p=1.5×10⁻¹⁹**),
   negative in **4 of 4** regimes — last cycle's P0, larger on 18 more rows. But `vol_long`
   (**+8.5pp**, p=1.5×10⁻⁴, **5-for-5 sized**) has a **max `raw_score` of 4 on 85 rows** and
   has never reached MEDIUM: every line that fires on it is worth +1, and the rubric's ≥2 lines
   are directional-only. 20 candidates post-change, **zero sized**. Phase 5.4 → **C66**.
3. **`earnings_vol` is not a flaw — it is the vol P0 in a costume.** 125 of 172 rows carry a
   `vol_short` thesis; split, it is **0.232 (n=99)** vs **0.630 (n=27)**. Its 54.6pp
   "divergence" rests on **13 quoting rows, all May–July**. It has been holding a second
   headline slot for a problem already counted. Phase 3.3.

## Top 3 tool-tier surprises

1. **Both BH survivors are composition, and last cycle's warning caught one.**
   `term-skew` reads −10.8pp overall but **+2.0pp inside `vol_short`** — 91 of 105 citing rows
   are vol rows. **Do not demote the term-structure readers.** Same for the one BH-surviving
   rubric component (`vol_term_structure`: −11.4pp overall, **−0.3pp inside `vol_short`**).
2. **`term_structure_hygiene.py` does *not* wash out — and still cannot be acted on.**
   Negative inside every lane (−21.5pp in VOL, 0-for-10 in `vol_short`). But **27 of 31 citing
   rows are August** and non-August accrual is **n=4 of a required 30** — it went *backwards*.
   C61 stays open. Effectively the **13th consecutive BH-null tool table**.
3. **C18 is dead and contradicts its own fleet.** `insider_cluster_flag`: **30 populated, all
   `False`** (2nd cycle) — while `insider_selling_cluster` is the **most common** new
   `fundamentals_verdict_reason` (9 of 15). Two insider signals, one silent, one dominant.

## What we'd do Monday

**Change nothing about sizing, and write down why the ladder can't be graded.** The trading
behaviour is probably right — DROP 0.391 ≈ LOW 0.402, HIGH realised 0.143, log-loss **0.788 >
ln 2** (the quotes carry negative information). The defect is not that we should trade more; it
is that we have run a conviction rubric for 59 sessions whose top half is arithmetically
unreachable, so it can neither discriminate nor ever satisfy its own lift criterion. Register
it, don't re-bin it — re-binning on one window is the failure the freeze exists to stop.
Everything applied last cycle **worked**: short-vol routing **15/15**, short routing **23/23**,
zero violations, and the generation floor landed **on** its baseline (32.0% → 17.6% → **32.6%**,
p=0.92 vs pre-P0) rather than becoming a quota. Compliance is **5 missed gates in 1,334
non-DROP obligations (0.37%)**, one sizing violation in the whole corpus, all seven comparable
gates effective. Two inversions are instrumentation cases, not removal cases: the fundamentals
verdict is backwards **even after direction control** (VETO'd shorts **0.450** vs non-VETO'd
**0.306**, n=20) and the debate residual runs the same way. **C63 cannot be graded** — 10
decided of 40, one regime bucket, no complete windows; the 0-for-10 is colour. Keep the freeze,
the half-cap (9th negative), the [0.55,0.65) floor (post-change **0.10**, none sized), every
gate, Kelly off.
