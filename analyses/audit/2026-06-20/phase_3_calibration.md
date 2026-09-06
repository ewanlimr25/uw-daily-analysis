# Phase 3 — Calibration Audit · 2026-06-20

**Provenance:** verbatim envelope (clears C23 for headline). **Two standing caveats on the *claim* side:** (1) 117 of 132 claimed win-rates are `backtest`/`fallback_proxy` — the **pre-quarantine substrate** flagged broken on 2026-06-12; a claimed-vs-realised gap is as likely a broken-oracle artefact as a rubric lie. (2) vol classes (earnings_vol, high_iv_rank) resolve on the **RV-direction proxy**, not true IV-vs-RV. Both caveats are applied in the verdict.

## 1. Per-class table (decided ≥8; BH FDR 0.10)

| class | n | realised | claimed | div pp | SPY-WR | **excess pp** | p | BH |
|---|--:|--:|--:|--:|--:|--:|--:|:--:|
| bearish_flow | 34 | 0.47 | 0.42 | −5.1 | 0.71 | **−23.5** | 0.66 | n |
| dark_pool_accumulation | 27 | 0.48 | 0.56 | +7.9 | 0.33 | **+14.8** | 0.53 | n |
| bullish_flow | 25 | 0.56 | 0.59 | +3.3 | 0.36 | **+20.0** | 0.88 | n |
| earnings_vol | 21 | 0.38 | 0.86 | **+47.8** | 0.00 | (vol) | **0.000** | **Y** |
| dealer_positioning* | 15 | 0.47 | 0.60 | +13.0 | 0.53 | **−6.7** | 0.44 | n |
| multileg_directional | 12 | 0.17 | 0.56 | **+38.8** | 0.25 | −8.3 | **0.014** | **Y** |
| high_iv_rank | 8 | 0.38 | 0.84 | **+46.1** | (vol) | (vol) | **0.009** | **Y** |

*dealer_positioning = 5 fragmented labels merged (Phase-1 flag). Appendix THIN_N (5–7): multi_day_sweep 0.83 (n6), gamma_breakout 0.20 (n5) — excluded from headline.

**Only three divergences survive BH:** `earnings_vol`, `high_iv_rank`, `multileg_directional`. The four flow classes' claimed-vs-realised gaps are **noise** (p 0.44–0.88) once you control for testing 7 classes at once.

## 2. Tier reliability — INVERTED, and it persists
| Tier | n | realised WR |
|---|--:|--:|
| **HIGH** | 7 | **0.143** |
| MEDIUM | 19 | 0.526 |
| LOW | 62 | 0.452 |
| DROP | 72 | 0.444 |

Per-era (inversion persistence): HIGH = 0.25(4) → 0.0(2) → 0.0(1) → no data. **In every era where HIGH has any data, it under-performs its own MEDIUM/LOW tier**, and this is now the *second consecutive audit* (06-12: HIGH 0.222) to log it. N is always tiny (≤4/era), so each instance is individually noise — but the *sign never once flips*. The rubric's top tier has no demonstrated positive resolution.

## 3. Brier / log-loss / reliability deciles
- **Brier = 0.297** (≥0.25 = "no better than coin-flip"). **Log-loss = 0.826** (a calibrated 0.5 coin gives 0.693; the excess is the confident-and-wrong tail). graded_n=115.
- **Reliability diagram localizes the damage:**

| claimed bucket | n | pred mean | realised hit |
|---|--:|--:|--:|
| [0.00,0.50) | 41 | 0.35 | 0.46 |
| [0.50,0.55) | 18 | 0.51 | 0.56 |
| [0.55,0.60) | 8 | 0.57 | 0.25 |
| [0.60,0.65) | 6 | 0.64 | 0.17 |
| [0.65,0.70) | 7 | 0.66 | 0.57 |
| [0.70,0.80) | 8 | 0.77 | 0.75 |
| **[0.80,0.90)** | **24** | **0.83** | **0.42** |
| [0.90,1.01) | 3 | 0.93 | 0.67 |

The rubric is **well-calibrated below 0.55 and in 0.70–0.80**, and **wildly overconfident in [0.80,0.90)** — 24 calls quoted 0.83, delivered 0.42. That bucket breaches the live `ABSOLUTE_WR_CEILING=0.80` (a cap synced 2026-06-06): **24 graded calls carry claimed WR ≥0.80**, so either they predate the cap-sync or the cap isn't binding at emission. Flagged to Phase 6.

## 4. Conviction-vs-outcome (raw_score → realised WR)
`0:0.50(20) 1:0.52(25) 2:0.30(20) 3:0.44(16) 4:0.41(27) 5:0.62(8) 6:0.46(11) 7:0.67(6) 8:0.29(7) 9:0.67(6) 10:0.00(3) 11:0.33(3) 12:0.00(1)`

No monotone slope. **The top of the score ladder is the worst: raw 10/11/12 → 0% / 33% / 0%.** The tier inversion is not a binning artefact — it is baked into the raw score itself. The highest-conviction arithmetic outputs are the biggest losers. (Small N at the top, but it is the same sign as §2 and the 06-12 audit.)

## 5. Expectancy + Kelly live-activation gate
- **Gate: `ADVISORY_ONLY`** — n=21 sized closed calls < 30 floor. The half-Kelly sizer stays parked; the win-rate ladder remains live. **Do NOT flip `signal-confluence-quant`/`risk-monitor` to Kelly.**
- Per-tier paper expectancy is **negative or ~zero everywhere and non-monotone**: HIGH −2.44 · MEDIUM **+0.10** · LOW −0.72 · DROP −5.80. MEDIUM is the only non-negative tier; HIGH sits *below* LOW. There is no tier to size *up* into.

## Verdict (four sections)

**(a) Where the rubric is honest.** `bullish_flow` (claimed 0.59 / realised 0.56), `dark_pool_accumulation` (0.56 / 0.48), and `bearish_flow` (0.42 / 0.47 — actually *under*-claimed) are all BH-null: their quotes are believable. The reliability diagram confirms it — everything the rubric quotes **below 0.55 or in 0.70–0.80** lands.

**(b) Where it lies to itself.** `earnings_vol` (0.86→0.38) and `high_iv_rank` (0.84→0.38) — both BH-surviving, both quoting >0.80 off the **broken substrate**, both RV-proxy-resolved. The fix is *kill the substrate-sourced ≥0.80 quotes*, not retune a weight. `multileg_directional` is the one **directional** lie that survives BH (0.56→0.17, n=12) — and it is not a substrate artefact (it's a structure-inference class), so it is the most actionable miscalibration.

**(c) Tier inversion / HIGH overconfidence.** HIGH realises 0.143 — dead last — and raw 10–12 realise 0/33/0%. Second audit running. The conviction ladder is non-monotone from the score up. This is the empirical mandate for the rubric freeze; nothing here argues for *lifting* it.

**(d) Calibrated-but-beta (edge ≤ 0).** `bearish_flow` is the desk-critical one: **honest about its 47%, but that 47% is −23.5pp vs simply shorting SPY.** It passes calibration and is still negative edge. `dealer_positioning` is mildly beta (−6.7pp). Per the skill's edge-before-calibration rule, **the bearish/short book's negative excess is a worse problem than any of the §(b) overconfident quotes** — a desk loses money on negative-excess long before it loses on an honest-but-wrong number. The long classes (`bullish_flow` +20.0, `dark_pool_accumulation` +14.8) carry genuine positive excess — but Phase 2 shows that long edge **decaying across eras** (single-regime; not yet durable).

## Outputs
- `phase_3_calibration.jsonl` — class table (incl. `realised_excess_pp`, `spy_benchmark_wr`, BH flags), per-era tier reliability, reliability deciles, score table, Brier/log-loss, Kelly gate, tier expectancy.
