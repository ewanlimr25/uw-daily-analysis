# Phase 4 — Tool Attribution

## ⚠️ Provenance caveat (governs the confidence of everything below)

Only the **54 envelope rows** carry **verbatim** `source_tool` strings — and those reports are too recent to have resolved (0 decided; all window_open/watch). For the 462 **legacy** rows, `tools_cited` was **reconstructed by the prose-extraction parsers** from named metrics ("dark-pool buy ratio" → `uw dark-pool block-stratified`, etc.). The marginal contributions below are therefore **structural/qualitative**, not a verbatim audit-trail attribution. They are directionally trustworthy where they **agree with Phase 3** (and they do), but no single tool's pp figure should be treated as a precise realised contribution. Tiering uses class-conditional `winrate_with − winrate_without`, N≥5 to score.

Also note: tool citations are **sparse** (no tool is cited on >25% of either winners or losers), so the **CONFOUNDED** detector (≥80% of winners / ≤30% of losers) structurally cannot fire on this dataset — absence of CONFOUNDED findings is a data property, not a clean bill.

## Tool tier list (N ≥ 5)

| Tool | N | MC (pp) | Tier |
|---|---|---|---|
| `uw options-structure multileg-activity` | 9 | +57.1 | LOAD-BEARING (thin) |
| `uw options-flow multi-day-sweep-persistence` | 11 | +31.9 | LOAD-BEARING |
| `uw dark-pool block-stratified` | 52 | **+25.4** | **LOAD-BEARING** |
| `uw options-structure today-gamma-flip` | 9 | +25.0 | LOAD-BEARING |
| `uw hot-chains sweep-persistence` | 28 | +19.5 | LOAD-BEARING |
| `uw insights signal-confluence` | 16 | +17.2 | LOAD-BEARING |
| `uw options-structure dex` | 37 | **+15.5** | **LOAD-BEARING** |
| `uw historical pc-ratio-zscore` | 5 | +12.9 | LOAD-BEARING (thin) |
| `uw historical oi-trend` | 45 | +12.2 | LOAD-BEARING |
| `uw insights earnings-play` | 6 | +7.6 | SUPPORTIVE |
| `uw historical cumulative-premium-flow` | **76** | **+2.0** | **NO-INFO** |
| `uw options-structure iv-term-structure` | 26 | +0.8 | NO-INFO |
| `uw options-structure gex` | 12 | 0.0 | NO-INFO |
| `uw historical iv-rank` | 11 | +1.2 | NO-INFO |
| `uw options-flow sector-flow-persistence` | 22 | −6.8 | NEGATIVE |
| `uw hot-chains multileg` | 10 | −7.0 | NEGATIVE |
| `uw insights institutional-accumulation` | 5 | −12.6 | NEGATIVE |
| `uw options-structure term-skew` | **56** | **−13.4** | **NEGATIVE** |
| `uw insights dealer-delta-exposure` | 7 | −14.3 | NEGATIVE |
| `uw historical gex` | 9 | −27.2 | NEGATIVE |
| `uw options-structure iv-percentile-zscore` | 6 | −31.7 | NEGATIVE |
| `uw insights conviction-matrix` | 7 | **−40.1** | NEGATIVE |

(19 further tools INSUFFICIENT_N at <5 citations — excluded from tiering.)

## Desk commentary (market-maker quant voice)

- **`uw dark-pool block-stratified` — LOAD-BEARING (+25.4pp, n=52).** The vindication buried inside Phase 3's worst class: the *class* `dark_pool_accumulation` is wildly over-claimed (82.8%→51.2%), but the **block-stratified institutional/retail filter itself separates winners from losers by ~25pp**. The signal is real; the *headline win-rate attached to it* is the fiction. Without this gate, accumulation calls degrade to raw `ticker-summary` noise. Keep it required; kill the win-rate label on top of it.
- **`uw options-structure dex` — LOAD-BEARING (+15.5pp, n=37).** Mirrors Phase 3's one honest class (`dealer_positioning`, 80% realised). DEX/dealer-flip is the load-bearing directional read on the desk. Promote to required citation for any directional swing.
- **`uw hot-chains sweep-persistence` / `multi-day-sweep-persistence` — LOAD-BEARING (+19.5 / +31.9pp).** Multi-day persistence beats single-day premium — the desk's own "persistence FIRST, today's premium SECOND" rule is empirically right. The single-day `top-premium-trades` is INSUFFICIENT_N but the persistence variants carry the weight.
- **`uw historical cumulative-premium-flow` — NO-INFO at n=76.** *The single most-cited evidence tool in the entire book adds +2pp.* It's a comfort-blanket citation — agents reach for it reflexively (`+3 cumulative-premium-flow accretion` is a standard rubric line) but it does not separate winners from losers. **Demote from default citation; it is inflating scores without earning them.**
- **`uw options-structure term-skew` — NEGATIVE (−13.4pp, n=56).** Heavily cited (earnings/vol calls) and **anti-predictive**. This is the tool feeding the `vol_surface` (80%→47%) and `earnings_vol` (58%→43%) miscalibration. Either the agents are misreading term-skew sign, or it's being used to justify trades it shouldn't. Investigate the `vol-surface-scout` / `earnings-scout` prompt logic.
- **`uw insights conviction-matrix` (−40pp) & `institutional-accumulation` (−12.6pp) — NEGATIVE.** The conviction-matrix is the LEAP gate (per memory, the "institutional-accumulation lookback is a fiction param"). Both fire on losers more than winners. These are the tools most in need of either removal or a hard re-interpretation in their agents (`leap-positioning-radar`, `accumulation-hunter`).
- **`uw historical gex` / `iv-percentile-zscore` — NEGATIVE.** Small-N but consistent with the gamma_pin (64%→30%) collapse — the gamma/pin tooling is anti-predictive on this tape.

## `fz` advisory dimensions (C15–C18) — gating the Phase-B promotions

| Axis (criterion) | Decided N | Verdict |
|---|---|---|
| `squeeze_pressure` (C15) | 0 | INSUFFICIENT_N |
| `float_shares` block-norm (C16) | 0 | INSUFFICIENT_N |
| analyst divergence (C17) | 0 | INSUFFICIENT_N |
| insider clusters (C18) | 0 | INSUFFICIENT_N |
| `breadth_cross_check` | 0 decided | INSUFFICIENT_N |

`fz_context` exists only on envelope rows, and **0 envelope rows resolved** (all window_open/watch — the `fz` integration shipped 2026-05-27, two trading days before the audit cutoff). **No `fz` criterion clears its promotion threshold; all of C15–C18 stay advisory (0 rubric points)** — exactly as the calibration discipline requires. Re-test after ≥10 trading days of post-`fz` resolved calls (~2026-06-12).

## Output
- `phase_4_tools.jsonl` — full tool table + fz advisory block. `phase4_tools.py` — reproducible.
