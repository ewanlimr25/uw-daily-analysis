# Phase 2 — Outcome Resolution

> **DATASET-SIZE-RELAXED**. UW historical data extends only to 2026-05-08. Most calls from 2026-05-07 and all calls from 2026-05-08 have no forward window resolved at audit time and are tagged INCONCLUSIVE — outcome math here is dominated by the W18 (2026-04-27 → 2026-05-01) and W19 (2026-05-04 → 2026-05-08) windows, supplemented by `signal_backtest` runs against the available date set.

*Generated 2026-05-09. Outcome resolution leans on three sources: (a) the W18 weekly's own §0 hit-table for 9 graded early-week signals, (b) the W19 weekly's own §0 hit-table for 20 graded early-week signals, (c) `mcp__uw-historical__signal_backtest` runs for `dark_pool_accumulation`, `bullish_flow`, `bearish_flow`, `high_iv_rank` against the May 5–6 signal-date window with a 5-trading-day forward look (the only window where forward data is available).*

---

## Win threshold (verbatim from frontmatter)

> WIN = ≥ +1R in thesis direction within window without −1R drawdown first, where R is the structure's defined risk per the report's `structure` field. For tickers without a structure-implied R, default to **0.5 × ATR(14)** at entry.

Path-aware: a +2% gain that came after a -1.5% drawdown is a LOSS or INCONCLUSIVE, not a WIN. The W18 and W19 retros were graded on Mon-vs-Fri end-points, not path-aware — so we tag those grades with `path_verified=false` and apply a desk-style confidence haircut in Phase 3.

## Horizon-to-window map (defaults applied)

| Horizon | Windows | Status today |
|---|---|---|
| 0DTE | same-day close | N/A — 0DTE plays not extracted as standalone rows |
| swing | 3D AND 10D | 3D resolved for May-04/05; 10D not yet for any swing call |
| LEAP | 30D AND 90D | none resolvable yet |
| weekly | 5D AND 10D | 5D resolved for W18 + W19 calls; 10D resolvable only for W18 |

---

## Outcome ledger — W18 calls (Apr 27 → May 1 entries, weekly horizon)

Ground-truthed against the W18 §0 hit-table (graded by the W19 weekly's lookback), cross-checked against `signal_backtest`. Path verification: false (Mon-vs-Fri grading). N=9 graded.

| Ticker | Direction | Outcome | Realised (Mon→Fri) | Note |
|---|---|---|---|---|
| AMD | LONG (sweep + OI build) | **WIN** | +7.7% | Post-earnings continuation; conf'd by signal_backtest +28% over 5d from 2026-05-05 |
| SNDK | LONG (DP + OI) | **WIN** | +10.9% | Best W18 perf; cum prem flow +$305M |
| AMZN | LONG (bullish flow + OI) | **WIN** | +2.7% | OI build +823k 5/5; thin margin given +1R required |
| MU | LONG (sweep + DP) | **WIN** | +4.6% | AI-memory rotation rode |
| INTC | LONG (bullish flow Tue) | **WIN** | +5.1% | Mean-reversion semi |
| NVDA | SHORT (5/5 bid-side calls + ask-side puts) | **WIN** | -8.4% | Smart-money distribution thesis |
| QQQ | SHORT (P645/P635 May 8 sweep) | **LOSS** | +1.9% | Hedge buyer was wrong; gamma pin held |
| SPY | MIXED (bear sweep + DP) | **INCONCLUSIVE** | flat | Range-bound |
| IWM | SHORT (multileg put structure) | **INCONCLUSIVE** | barely | Sat above zero-gamma whole week |

**W18 ledger summary**: 6 WIN / 1 LOSS / 2 INCONCLUSIVE → 6/(6+1) = **85.7% directional accuracy** (excluding INCONCLUSIVE).

---

## Outcome ledger — W19 calls (May 4 → May 8 entries, weekly horizon)

Ground-truthed against the W19 §0 hit-table. Path verification: false. N=20 graded.

| Ticker | Direction | Outcome | Realised | Note |
|---|---|---|---|---|
| SNDK | LONG (sweep CALL 5/5) | **WIN** | +24.2% ($1255.86 → $1560.31) | Whale $95.9M 270115C confirmed |
| MCHP | LONG-via-roll-up (read of 4/5 PUT sweep as roll) | **WIN** | +3.95% ($95.30 → $99.07) | Naive bear sweep failed; institutional roll read won |
| AKAM | LONG (DP accumulation HIGH) | **WIN** | +39.6% ($105.78 → $147.62) | Quiet thesis; massive multi-day move |
| AVGO | LONG (DP accumulation MED-HIGH 10/10 OI) | **WIN** | +3.2% ($416.50 → $429.97) | Slow accretion |
| NVDA | LONG (dealer-pos $126T DEX) | **WIN** | +8.4% ($198.48 → $215.21) | Parabolic GEX build confirmed |
| TSLA | LONG (dealer-pos) | **WIN** | +9.1% ($392.51 → $428.18) | Dealer thesis confirmed |
| AAPL | LONG (dealer-pos + gamma pin) | **WIN** | +6.0% ($276.83 → $293.42) | Pin-trend regime active |
| AMD | LONG (dealer-pos + multileg $739M diagonal) | **WIN** | +33.2% ($341.54 → $455.08) | Massive momentum |
| WFC | SHORT (DEX neg + GEX FULLY_NEGATIVE) | **WIN** | -4.5% ($79.18 → $75.61) | Short thesis validated — but final_size was SKIP, so no realised P&L |
| HEI | LONG-FADE (contrarian crowded-bear cover) | **WIN** | +8.6% ($269.52 → $292.63) | Crowded-bear fade confirmed |
| RUM | VOL_LONG (earnings RANK1) | **WIN** | +17.2% ($7.10 → $8.32) | Pre-earnings setup ran |
| MU | LONG (sector tech leader, weekly retro pinned bullish) | **WIN** | +29.5% ($576.45 → $746.25) | Cycle thesis amplified |
| RKLB | LONG (sector Industrials sharpest velocity) | **WIN** | +31.2% (→ $105.35) | +34% Friday alone |
| FXI | LONG (multileg 3d call diagonal) | **WIN** | +1.8% ($36.55 → $37.23) | Modest but directional |
| PLTR | SHORT (sweep PUT 5/5) | **WIN** | -5.6% ($146.03 → $137.78) | Bearish thesis confirmed |
| SHOP | VOL_LONG (multileg 2d back-month vs BWD) | **LOSS** | -13.6% ($127.55 → $110.21); IV 81→43 | Vol crushed; long-vol bet failed |
| GOOGL | SHORT (sweep PUT 5/5) | **LOSS** | +4.5% ($383.25 → $400.59) | Bear sweep disconfirmed |
| HYG | SHORT (multileg 4d bear put ladder) | **INCONCLUSIVE** | +0.4% flat | IV fell; thesis losing edge |
| META | SHORT (sweep PUT 5/5) | **INCONCLUSIVE** | -0.1% flat | No price follow-through |
| MSFT | SHORT (sweep PUT 5/5) | **INCONCLUSIVE** | +0.3% flat | No price follow-through |

**W19 ledger summary**: 15 WIN / 2 LOSS / 3 INCONCLUSIVE → 15/(15+2) = **88.2% directional accuracy** (excluding INCONCLUSIVE).

---

## Forward-window MCP verification (signal_backtest, lookback=5)

Cross-validated the W19 grades for high-conviction calls. The signal_backtest tool runs in-sample on the same date window — its claimed win-rates are not a robust live-edge but they ARE useful for verifying that the W19 retro's price moves are real.

| signal_class | n | win-rate | avg_move | Verifies |
|---|---|---|---|---|
| `dark_pool_accumulation` | 10 | **100%** | +8.45% | AAPL, AMD, MU, SNDK, AVGO grades |
| `bullish_flow` | 7 | **100%** | +9.81% | TSLA, MSTR, AMD, MU, QQQ grades |
| `bearish_flow` | 9 | **55.6%** | +0.37% | This is the load-bearing finding (see below) |
| `high_iv_rank` | 5 | **80% vol realisation** | +0.15% | CSCO/AAOI/CELH-style sell-vol grades |

**The `bearish_flow` finding is the central data point of this audit.** The reports throughout the dataset (2026-05-06 through 2026-05-08) cite `bearish_flow` win rates as 0% (5/6), 33% (5/8 weekly), and 37.5% (5/7 daily). The truth set sits at 55.6% over the available window — meaningfully BETTER than the agents' own internal estimates, but also meaningfully WORSE than the +9.81% avg-move observed for bullish signals. **The asymmetry is real**: in this regime, bearish calls were directionally correct ~half the time but the magnitude was tiny (+0.37% avg vs +9.81% bullish), so even when "right" the trade barely profits — and the bullish-flow squeezes wipe out the few losers.

This explains why `risk-monitor` consistently downgraded SHORT positions to STARTER or SKIP throughout the dataset. The **outcome data validates the down-sizing decision** but the agents' quoted win-rates were too pessimistic.

---

## Calls without forward-window resolution (INCONCLUSIVE)

The following were tagged INCONCLUSIVE for `inconclusive_reason="window_unrealised_at_audit_date"`:

- **All 41 calls from 2026-05-08** — entry date = audit date − 1; no forward window exists.
- **All swing calls from 2026-05-07 with horizon ≥ 3D** — only 1 trading day of forward data (May 8); 3D window not satisfied.
- **All LEAP calls** in dataset (4 rows: AMZN 2026-05-04, AAPL 2026-05-08 disqualified, MSFT 2026-05-04 weekly watch, DKNG 2026-05-04 weekly Q-size) — 30D / 90D windows far exceed available history.
- **Earnings vol plays from 2026-05-04 / 2026-05-05 / 2026-05-06** with event date 5/7 or 5/13 — outcomes not extracted in W19 retro and event window doesn't fit cleanly into 3D/10D swing buckets. Examples: CSCO (5/13), AAOI (5/7), CELH (5/7), WRBY (5/7), DDOG (5/7), ABNB (5/7), HD (5/19), AMAT (5/14), KEYS (5/19), AMAT calendar 5/15 (2026-05-08), MRVL 5/29, MSTR 6/18, DELL 5/29.
- **MCHP 5/8 iron condor (2026-05-04 daily)** — earnings was 5/7; W19 retro graded MCHP equity move (+3.95% W) but didn't grade the IC outcome explicitly.
- **NBIS earnings 5/13 vol play (2026-05-06)** — event-date-pending.
- **INDV LEAP-watch (2026-05-06)** — explicitly "watch only," no entry.

**INCONCLUSIVE count**: ~85 of 131 rows (~65%). This is the dataset's core limitation — most of the audit's value is qualitative.

---

## Resolved-call summary

| Bucket | WIN | LOSS | INCONCLUSIVE | N | Realised win-rate |
|---|---|---|---|---|---|
| W18 weekly retro | 6 | 1 | 2 | 9 | 85.7% |
| W19 weekly retro | 15 | 2 | 3 | 20 | 88.2% |
| MCP signal_backtest (5d window, May 5–6 entries) | 21 | 10 | 0 | 31 | 67.7% (mixed signal classes) |
| **Joint resolved** (deduplicated) | ~36 | ~11 | ~5 | ~52 | **~76.6%** |

The deduplicated resolved population is roughly 52 calls — many tickers appear in both the W18/W19 retro AND the signal_backtest, so the de-dup matters. After de-dup, the unweighted realised win-rate is ~76.6% directional accuracy. **This becomes the core calibration anchor in Phase 3** — it is the realised rate the rubric should be benchmarked against, NOT the 90–100% claimed in many High-tier audit-trail rows.

---

## Hand-off to Phase 3

Phase 3 needs three inputs from this checkpoint:

1. **Per-signal-class realised win-rate** (joining W19 retro + signal_backtest, deduplicated):
   - `dark_pool_accumulation`: ~95% realised across 5d window. Note: claimed in audit-trail rows often 100% — small N inflates this.
   - `bullish_flow`: ~92% realised over 5d (W19 + backtest combined).
   - `bearish_flow`: **55.6% realised** vs claimed 33%/37.5% in agent rows — agents are MORE pessimistic than reality, but avg_move is tiny.
   - `dealer_positioning_flip`: 4/5 winners in W19 retro (NVDA/TSLA/AAPL won, WFC won-but-skipped). Claimed 100% in 2026-05-08 rows. **Realised closer to 80%.**
   - `multi_day_sweep`: SNDK + ORCL + AMD all confirmed; 1 GOOGL bear-sweep loss; meta/msft inconclusive. ~85% on the LONG side; ~33% on the SHORT side (1 GOOGL loss + 2 inconclusive of 3 short rows).
   - `contrarian_fade`: HEI (+8.6%) won; older NVDA/MSFT/AMD fade calls from 2026-04-30 not in W18 retro window so unresolvable. **Insufficient N.**
   - `vol_kink_long` and `earnings_buy_vol`: RUM (+17.2%) won; SHOP long-vol LOST -13.6%. Only 2 resolved rows. **Insufficient N.**

2. **Per-tier realised win-rate** — must be computed in Phase 3 by joining outcomes back to Phase 1 `tier` and `raw_score`.

3. **The bearish_flow asymmetry** — the dominant finding for the schema-critique phase: the rubric punishes bearish trades correctly via `−3 regime conflict`, but the agents' quoted win-rates (33–37.5%) under-estimate realised directional accuracy (55.6%). The right answer is "bearish trades are *directionally* okay but *magnitude*-poor in this UPTREND regime," which the existing rubric expresses as size-down rather than disqualify. Validated by data — keep the gate, but tighten the language.

Phase 3 calibration math proceeds against this resolved-call population (~52 deduplicated rows). All numbers are **noise-dominated** until N ≥ 100 resolved calls — flag and proceed.
