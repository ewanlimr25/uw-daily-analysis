# Calibration Audit — 2026-08-30

**789 verbatim envelope calls** (82 `decision.json`, **82/82 validator-clean**), 190/192 tickers
OHLC-resolved path-aware, **693 decided**, **0 `Σpoints ≠ raw_score`, 0 prose reconstruction**.
Eras never pooled (FROZEN `2026-06-12`: 638). Four regime buckets. 13th audit, 6th cross-regime
cycle. **First subject-side P0 since 2026-08-01, and the first ever on the vol lane.**

## Top 3 schema flaws

1. **The vol lane's SHORT leg is adversely selected — 42% of all risk ever taken.** `vol_short`
   books **31.5%** vs unselected same-date single-name peers at **56.6%** (**−25.1pp**, n=111,
   paired McNemar **b=2 c=57, p<0.0001**), negative and individually significant in **4 of 4
   regime buckets**. `vol_long` runs **+9.5pp** (p=0.0034), 5-for-5 sized. Not the tape: August
   was a short-vol paradise at the index (SPY RV ratio 0.738) while the book's names ran 1.199.
   **20 of 48 sized rows ever are `vol_short`.** Phase 3.2 → **P0**.
2. **`earnings_vol` claims 0.87, realises 0.33 (n=144, BH-surviving)** — the same 110 rows.
   The quote is already fixed (0 quoted post-08-15); the lane under it is not. Phase 3.3.
3. **The ladder is monotone up to where it claims most confidence.** DROP 0.372 → LOW 0.425 →
   MED 0.500 → **HIGH 0.385**; [0.80,0.90) realises **0.45** on a 0.83 claim. Brier 0.286,
   log-loss **0.790 — worse than forecasting a flat 0.5**. Phase 3.4/3.5 → keep the freeze.

## Top 3 tool-tier surprises

1. **The vol toolchain's uniform negativity is a lane artifact.** `term-skew` reads −8.3pp
   overall but **+5.3pp *inside* `vol_short`**. **Do not demote the term-structure readers.**
2. **C61's confound worsened.** `term_structure_hygiene.py` holds −14.2pp (p=0.003) but
   **non-August n=7 of a required 30**, up one row in a week.
3. **C62's starvation is fixed; its bar is not.** Float-ratio emission went **0/55 → 10 of 13**
   August accumulation rows. Still **11 of 30 decided, 2 of a required 10** upper-arm. The prior
   "not emitted" reading was an auditor lookup bug.

## What we'd do Monday

**Stop proposing short-vol structures until an expansion-veto clears them.** Narrow on purpose:
the scouts find vol-expansion candidates *correctly* — that's what `vol_long` says — then sell
vol into the expansion. A sign error, not a dead lane. It survived three falsification attempts,
including the one that mattered: correcting the index-vs-single-name instrument bias makes the
gap **smaller and still −25.1pp**. Caveat stated, not buried — the resolver is an RV-direction
proxy, so this prices **selection, never P&L**. Everything else is discipline. **C60's bar is now
fully met** and we are **not** acting on it: only **4.9%** of its evidence is out-of-sample and
its window opens 2026-10-03. Last cycle's generation floor **worked** — short share 17.6% →
**44.2%** (p=0.0003) with routing compliance still perfect; watch it hasn't become a quota.
Compliance otherwise near-perfect: **5 missed gates in 1,262 non-DROP obligations (0.40%)**, all
nine gates effective. Instrument rather than change: log **why** fundamentals VETOes (VETO 0.524
vs CONFIRM 0.376 — inverted), retire `insider_cluster_flag` (30 populated, **all `False`**).
Keep the freeze, the half-cap (8th negative), every gate, Kelly off.
