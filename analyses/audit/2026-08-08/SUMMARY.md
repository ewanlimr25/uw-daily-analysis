# Calibration Audit — 2026-08-08

Dataset: **626 verbatim envelope calls** (64 `decision.json`, 53 daily + 11 weekly; 64/64
validate clean), 166/168 tickers OHLC-resolved path-aware, **542 decided**, **0
`Σpoints≠raw_score` violations**. Strata never pooled: pre-freeze 05-25 (54) / 05-30 (69) /
post-0606 (28) / **FROZEN 2026-06-12 (475)**. 10th edge audit; third consecutive
cross-regime cycle (290 up-tape / 252 down-tape). **This cycle's job was to grade the
2026-08-01 P0, not to find a new one.**

## Top 3 schema flaws

1. **`earnings_vol` quotes 0.87 and realises 0.404 on n=106** — a 47.5pp divergence,
   BH-surviving at p<0.001, the largest miscalibration in the corpus and its **fourth**
   appearance. 12 of 13 quoted rows cite `win_rate_source: backtest`, but
   `uw historical signal-backtest` supports only five classes and **`earnings_vol` is not
   one of them** — the number cannot have been measured. `high_iv_rank` is the same defect
   at 0.82 → 0.500 (n=24, BH). Phase 3.1 / 3.3. → **P1 #2**.
2. **The `[0.55,0.65)` band survived its first fix cycle unchanged: realises 0.233 against
   a 0.58 quote (n=43).** The 07-25 starter-floor is holding (post-P0 in-band rows are
   never sized), but the *number* was never re-derived. A bucket that predicts 0.58 and
   delivers 0.23 is informative with the sign inverted. Phase 3.3 / 6.7. → C56, **P1 #3**.
3. **The freeze-lift is not unsatisfied — it is unrunnable by construction, 8th cycle.**
   395 resolved post-freeze calls (13× the threshold) and **0 decided HIGH, 0 decided
   MEDIUM**; 475 post-freeze rows → 49 LOW / 426 DROP, with **one** `full`-sized call in
   the entire corpus. Tier order fails a 6th time (HIGH 0.143 < LOW 0.375 < DROP 0.415).
   The freeze is not what blocks the lift; the rubric's own conjunction requirements are.
   Phase 5.2 / 5.3. → Keep freeze, **P1 #5**.

## Top 3 tool-tier surprises

1. **10th consecutive BH-null tool table.** Smallest p in the sweep is 0.062, on an n=5
   cell. Ten windows across every regime this system has seen, ~20 tests each, and no tool
   has ever survived correction as an outcome discriminator. The rubric's premise that more
   corroborating citations raise conviction is no longer underpowered — it is answered.
2. **The 08-01 "C18 unblocked, 44/44" claim was a denominator error, and this audit
   corrects it.** That figure counted *key presence across all signal classes*; both fields
   are defined only for `dark_pool_accumulation` rows. On the right denominator the emitter
   fix actually **works** (the one post-fix row where `fz` ran is correctly populated) —
   but `insider_cluster_flag` has been observed **15 times and is `False` every time**.
   Zero variance cannot gate a conjunction at any n. C18 is blocked; C16 is merely starved.
   Phase 6.7. → **P1 #4**.
3. **`dark-pool block-stratified` completes a five-cycle collapse to nothing**: +15.9 →
   −2.3 → +1.6 → +1.8 → **+2.1pp**, WR-with 0.42 vs WR-without 0.41. A gate splitting the
   book into two piles of identical win rate. Keep the tool (it is the retail filter by
   construction); grant it no ranking. Phase 4.

## What we'd do Monday

**Nothing urgent — and that is the finding.** The 2026-08-01 P0 routing shorts to
watch-only applied cleanly (**6/6, zero sized violations, counterfactual fully preserved**)
and its justification got *stronger*, not weaker: `ALL / short` paired McNemar moves from
p=0.0115 to **p=0.0038** (b=25/c=51, n=181), `UP / short` now clears BH on its own, and the
deficit is again near-identical in both tapes (−14.3pp up / −14.5pp down) — the
mis-selection signature, not mistiming. Its mirror also held for a third window:
`ALL / long` **p=0.0220**, BH-surviving, the only durable positive edge this system has
produced — though the p-value has risen two cycles running and neither tape arm clears BH
alone. Watch it; do not size on it. Compliance is close to perfect: **5 missed gates in
1,064 non-DROP obligations (0.47%)**, all nine gates effective or advisory with `cluster`
at −25.3pp, one historical sizing violation from June.

So Monday is housekeeping, not surgery. Fix the two numbers the fleet is still telling
itself — the 0.87 `earnings_vol` quote that realises 0.404, and the [0.55,0.65) band that
realises 0.233 — then spend one session on `insider_cluster_flag`, which has cost five
audits and will either start firing or deserves retirement alongside C15. Keep the freeze,
keep the half-cap (out-of-regime −8.9pp on n=43, negative in all five measurements, though
the margin is compressing), keep every gate, leave Kelly off at n=27. One genuinely new
thing to watch: the sized book beat DROP in the up tape for the first time (0.500 vs 0.410,
n=30) while still trailing badly in the down tape (0.294 vs 0.423) — too thin to act on,
but it is the first crack in nine cycles of "the trades we refuse beat the trades we take."
