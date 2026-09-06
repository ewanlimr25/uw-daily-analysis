# Phase 6 — Decision-Process Audit (2026-09-05)

## 6.1 — Quant compliance

| check | result |
|---|---|
| `Σ score_components.points == raw_score` | **753 / 753** |
| every component carries `source_agent` + `source_tool` | **complete** |
| sizing-map **upgrade** violations | **1** |

The single violation: **2026-06-05 LLY** — `claimed_wr` 0.392 implies `starter`, emitted
`half`. One row in 753, pre-freeze, graded against the map live on its own `report_date`.
Gate-driven downgrades below the map size are allowed by construction and are not counted;
only upgrades above the win-rate-implied size are violations.

## 6.2 — Gate firing

| gate | present/fired | rate |
|---|---|---|
| rubric_regime | 505/505 | **1.000** |
| event_risk | 604/613 | 0.985 |
| panic | 584/600 | 0.973 |
| debate | 485/498 | 0.974 |
| regime | 588/605 | 0.972 |
| cluster | 585/604 | 0.969 |
| sector | 576/599 | 0.962 |
| vrp | 575/600 | 0.958 |
| fundamentals | 514/607 | 0.847 |

## 6.3 — Missed-gate ledger (C54 denominator — DROP excluded from the headline)

| gate | HIGH | MEDIUM | LOW | **NON-DROP** | DROP (own line) |
|---|---|---|---|---|---|
| regime | 0/7 | 0/20 | 0/141 | **0/168 = 0.000** | 273/710 = 0.385 |
| vrp | 0/7 | 0/20 | 1/141 | **1/168 = 0.006** | 277/710 = 0.390 |
| panic | 0/7 | 0/20 | 0/141 | **0/168 = 0.000** | 278/710 = 0.392 |
| cluster | 0/7 | 0/20 | 1/141 | **1/168 = 0.006** | 273/710 = 0.385 |
| sector | 0/7 | 0/20 | 1/141 | **1/168 = 0.006** | 278/710 = 0.392 |
| fundamentals | 0/7 | 0/20 | 2/141 | **2/168 = 0.012** | 269/710 = 0.379 |
| event_risk | 0/7 | 0/20 | 0/141 | **0/168 = 0.000** | 265/710 = 0.373 |
| debate | 0/0 | 0/0 | 0/79 | **0/79 = 0.000** | 229/648 = 0.353 |
| rubric_regime | 0/0 | 0/0 | 0/79 | **0/79 = 0.000** | 222/648 = 0.343 |

**Headline: 5 missed gates in 1,334 non-DROP obligations = 0.37%.** No gate approaches the
20% drift threshold. **No agent file is flagged for drift.**

The DROP-inclusive naive aggregate is **33.8%** — the figure C54 exists to forbid as a drift
headline, printed here only for contrast. It measures the fleet's intended early-exit
optimisation, not non-compliance.

**Coverage note.** 39 post-P0 rows carry no gate keys at all, on four sessions (08-04 ×16,
08-18 ×14, 08-07 ×6, 08-20 ×3). **All 39 are `tier: DROP`** — early exit, C54-excluded, and
not a missed gate. Flagged so a future all-tier elevation is not mistaken for this.

## 6.4 — Gate effectiveness (C24)

A gate earns its keep when the arm it fires on realises *worse* than the arm it leaves alone.

| gate | fired WR (n) | not-fired WR (n) | delta | status |
|---|---|---|---|---|
| cluster | 0.362 (489) | 0.632 (19) | **−27.0pp** | effective |
| panic | 0.369 (488) | 0.562 (16) | −19.3pp | effective |
| debate | 0.350 (391) | 0.538 (13) | −18.8pp | effective |
| vrp | 0.365 (479) | 0.520 (25) | −15.5pp | effective |
| sector | 0.369 (480) | 0.478 (23) | −10.9pp | effective |
| regime | 0.372 (492) | 0.471 (17) | −9.9pp | effective |
| fundamentals | 0.369 (426) | 0.412 (85) | −4.3pp | effective |
| event_risk | 0.370 (508) | 0.778 (9) | −40.8pp | **advisory** (n<10) |
| rubric_regime | 0.355 (411) | — (0) | — | **advisory** (no comparison arm) |

**All seven gates with a comparison arm are effective, in the correct direction.** Nothing
here supports loosening or removing any gate, and per C24 nothing would even if it did on
this N.

### The one inversion — and it survives direction control

The **fundamentals verdict ordering is backwards, for the second consecutive cycle**:

| verdict | n | WR |
|---|---|---|
| **VETO** | 25 | **0.520** |
| CONFIRM | 122 | 0.377 |
| CAUTION | 139 | 0.338 |

Last cycle this was reported and left uninstrumented. The obvious confound is composition —
**20 of 25 decided VETOs are short theses** (VETO direction mix: short 20, long 4, vol_long 1)
and the short population has a different base rate. **Direction-controlled, the inversion gets
worse, not better:**

| within short theses | n | WR |
|---|---|---|
| VETO'd | 20 | **0.450** |
| not VETO'd | 49 | 0.306 |
| **delta** | | **+14.4pp — ANTI-EFFECTIVE** |

Within long theses, VETO n=4 WR 0.750 — same sign, too thin to read. Ordering within shorts is
**VETO (0.450) > CONFIRM (0.353) > CAUTION (0.281)** — monotone, and exactly inverted.

n=20 clears C24's ≥10-decided floor, so this is actionable. **It does not license removing the
gate** — C24 is explicit that a gate's value is insurance against the regime not yet in the
dataset, and every one of these VETO'd shorts is routed to `watch_only` anyway, so the gate is
currently costing the desk nothing. What it licenses is finding out *why*, and the instrument
for that shipped last cycle: `fundamentals_verdict_reason`, 15 rows so far.

### Debate gate

`bear_won` 0.327 (n=159) vs `bull_won` 0.211 (n=19). The −1 debate downgrade fires on names
that then *outperform* the names where the bull won. Same inverted shape as the fundamentals
gate, on a thinner bull arm. Advisory; n=19 on one side.

## 6.5 — Follow-through on the last cycle's recommendations

| rec | state |
|---|---|
| **P0 (short-vol routing)** | **15/15 post-change `vol_short` → `watch_only`. Zero violations.** Generation intact: `vol_short` share of the vol lane 68.0% → 42.9%. |
| 2026-08-01 P0 (short routing) | **23/23 post-change shorts → `watch_only`. Zero violations.** |
| **P1 #3 (short-generation floor)** | **Worked, and did not overshoot.** Pre-P0 32.0% → post-P0 starvation 17.6% → **post-floor 32.6%** (Fisher vs pre-floor **p=0.0031**; vs the pre-P0 baseline **p=0.92** — statistically indistinguishable from where it started). Uptrend-controlled: 31.3% → 17.4% → 40.7% (p=0.2492 vs baseline). **Neither starvation nor quota.** Keep watching the uptrend arm. |
| P1 #1 (`fundamentals_verdict_reason`) | Shipped and populating: 15 rows, all post-2026-08-30. `insider_selling_cluster` 9, `news_catalyst_contradicts_thesis` 2, `earnings_surprise_streak_negative` 2, `other` 2. |
| P1 (fix `earnings_vol` / `high_iv_rank` quotes) | `earnings_vol`: **zero quoted rows post-change** (was 13 quotes at mean 0.871 against 0.392 realised). `high_iv_rank`: mean claim 0.818 → **0.600**, realised 0.25 on n=8 — right direction, still overconfident, thin. |
| C56 (anti-predictive [0.55,0.65) floor) | **Binding.** Post-change in-band rows: 11 quoted, realised **0.10 (n=10)**, and **not one was sized** (`watch_only` 5, `skip` 6; pre-change 4 were `starter`). The band is *more* anti-predictive than when it was registered. **Do not lift.** |
| P2 (enum drift) | **Largely fixed.** 31 distinct classes with 14 off-list → **18 classes with 1 off-list** (`vol_long` ×5, already alias-mapped). |
| P2 (retire `insider_cluster_flag`) | **Not applied.** 30 populated, **all `False`** — zero variance, second consecutive cycle. C18 remains untestable. |

## Desk read

The process layer is the healthiest part of this system and it is not close. **0.37% missed
gates on 1,334 non-DROP obligations, 753/753 arithmetic, one sizing violation in the entire
corpus, both P0s at 100% routing compliance with generation demonstrably intact, and a
generation floor that landed on its baseline rather than overshooting it.** Every recommendation
from the last cycle that was applied is measurably working.

Two things are inverted and both are gates rather than scores: the fundamentals verdict
(VETO > CONFIRM > CAUTION, direction-controlled, n=20) and the debate residual (bear-won beats
bull-won, n=19 on the thin side). Neither is a removal case. Both are instrumentation cases,
and the instrument for the first one already exists.
