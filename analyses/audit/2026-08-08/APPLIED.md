# P1 application record — 2026-08-08

Applied by a separate, human-approved upgrade pass (the audit itself is propose-only and
edited nothing outside this folder). **Freeze-safe: no rubric weight and no tier cut was
touched.** All changes are win-rate *quote* / sizing-*procedure* / instrumentation items,
which the 2026-06-12 freeze explicitly leaves in scope.

Test suite: **413 pass** (404 before, +9 new). All **64/64** envelopes still validate clean.

---

## Two of the five recommendations were WRONG and were not applied as written

Recorded prominently because both errors are the *same shape* as defects this audit
programme exists to catch.

### ❌ P1 #3 (apply C56) — NOT APPLIED. The pre-registration's bar is not met.

Phase 7 proposed applying C56 (re-derive the `[0.55,0.65)` quote) on the strength of
Phase 3.3's reliability diagram: **n=43 decided in-band, realised 0.233 against a 0.58
quote.** That number is measured across the **whole corpus, pooling rubric eras.**

C56's actual bar is **n≥30 _post-fix_ quoted rows.** Measured correctly:

```
post-2026-07-25 in-band quoted rows = 13     bar = 30     ->  NOT MET
```

Applying it would have fitted a re-derivation to 13 observations — precisely the failure
mode the freeze exists to prevent, and precisely what the 2026-08-01 entry in
`signal-confluence-quant.md` warned against ("acting now would fit a re-derivation to 15
observations"). **This is the C49 denominator artifact wearing different clothes:**
reaching for a larger, wronger denominator because it clears a threshold the correct one
does not. Instead of applying it, the trap is now documented in the agent file so the next
grader counts post-fix rows *before* reading the pooled rate.

Everything already live stays live (the `starter` floor; disclosure-only / never
upgrade-eligible). Post-fix behaviour confirms both hold: the 2 in-band rows written after
2026-08-01 were both `watch_only`.

### ⚠️ P1 #2 (fix the vol quotes) — ALREADY FIXED. Recorded as verified, not applied.

Phase 6d marked this "UNVERIFIABLE — zero post-P0 rows carry a quote." **That absence was
the verification, and the audit misread it as missing evidence.** Post-fix:

```
earnings_vol : 13 rows, ALL win_rate=null / win_rate_source="NA(substrate)", all skip|watch_only
high_iv_rank :  1 row,      win_rate=null / win_rate_source="NA(substrate)", watch_only
```

The lane stopped quoting these classes entirely — which is *better* than the capped 0.55
the 08-01 rec installed, because `uw historical signal-backtest` does not support
`earnings_vol` at all, so no genuine rate for it can exist. The large pooled divergence
(0.871 → 0.404, n=106) is **pre-fix rows**; grading this lane on the pooled corpus would
misread a fixed defect as a live one. The agent file now says so and forbids restoring a
numeric quote.

---

## What WAS applied

### ✅ P1 #1 — short-routing replication recorded
`.claude/agents/risk-monitor.md`. Records: 6/6 post-rule shorts routed to `watch_only`,
0 sized violations, counterfactual intact (all 6 scored + gated + classed); evidence
strengthened (`ALL / short` McNemar 0.0115 → **0.0038**; `UP / short` now BH-surviving at
0.0195); revisit trigger unmet and receding. Adds two cautions the audit flagged: clean
compliance is **not** outcome validation (6 calls, 5 uptrend sessions), and the **long
mirror is decaying** (p 0.0081 → 0.0046 → 0.0220; neither tape arm clears BH alone; `ALL`
is a null at p=0.7465) — watch, do not up-size.

### ✅ P1 #4 — `insider_cluster_flag` root-caused and FIXED
**This was the cycle's real find.** The audit asked for "one debugging session to determine
whether `fz insider-clusters` genuinely never fires, or whether the co-flag is dropped."

**Answer: neither — it is the doubled-first-letter parse bug, again.** `fz
insider-clusters` reads a **local store** whose `Ticker` cells are corrupted: on
2026-08-08, **14 of 14** distinct tickers were doubled (`PLTR` → `PPLTR`, `XAIR` →
`XXAIR`, `ATTO` → `AATTO`). `accumulation-hunter` matched by exact string equality, so no
lookup ever matched and the flag was serialized `False` all 15 times it appeared — zero
variance, C18 untestable for five audits. **Same bug and same fix as the C16 float lookup
at 2026-08-01 item 5**, one lane over.

- `scripts/fz_enrich.py`: new `insider_cluster_flag()` + `_run_fz_insider_clusters()`.
  Routes matching through the existing doubled-letter-tolerant `_screen_row_matches`, and
  returns **`True` / `False` / `None`** where `None` = lane skipped (empty store, missing
  binary, error) so a dead lane is never scored as a negative observation.
- `scripts/tests/test_fz_enrich.py`: +9 tests, written RED first (verified failing), now
  green — doubled-ticker match, undoubled match, checked-and-absent vs skipped, empty
  store, `fz` failure, `min_buyers` threshold, side filter, malformed rows, blank ticker.
- `.claude/agents/accumulation-hunter.md`: the flag must now be resolved through the
  helper; deriving it from raw CLI rows by string equality is explicitly forbidden.

Live verification — **the flag can finally return `True`**:
```
XAIR -> True      PLTR -> False     AAPL -> False     (missing binary) -> None
```

### ✅ P1 #5 — freeze / half-cap / gates held, with the framing corrected
`.claude/agents/risk-monitor.md`. All five holds recorded (freeze, half-cap, nine gates,
Kelly off, no tool moves). Two substantive additions:

- **The freeze-lift framing is corrected.** It is not blocked by insufficient evidence —
  it is **unrunnable by construction**. 395 resolved post-freeze calls (**13×** the ≥30
  threshold the rule names) and still 0 decided HIGH / 0 decided MEDIUM. The file now warns
  explicitly: **do not read future "≥30 resolved" milestones as progress toward a lift**;
  the binding constraint is band emptiness, not sample size.
- **The half-cap's protective margin is compressing monotonically** (−16.7 → −14.3 → −11.9
  → −12.0 → **−8.9pp**). Held — C24 forbids loosening on this — but flagged for formal
  re-grading if the trend toward zero continues two more cycles.

---

## Not applied (correctly out of scope for a P1 pass)

P2 items 6–9 (monitor `veto_fp_rate`; retire C15; emit per-call `implied_move`;
pre-registrations C50/C51/C55/C57) are unchanged and carried forward.
