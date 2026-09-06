# Phase 4 — Tool Attribution (2026-05-30 · C23 BH · C32 ubiquity · provenance cap)

## ⚠️ Provenance + significance caveats (govern EVERYTHING below)

1. **Reconstructed citations.** Every DECIDED row is a **legacy prose** row — the 54 envelope
   rows (verbatim `source_tool`) are all window_open. So `tools_cited` is **reconstructed**, not
   a verbatim audit trail. All tiers are **structural/qualitative** → cap Phase-7 at **P1** (C23).
2. **Benjamini-Hochberg kills every flag (C23).** Running ~25 simultaneous
   `winrate_with − winrate_without` tests, **zero tools survive BH at FDR 0.10.** Not one tier
   assignment is statistically significant after multiple-hypothesis correction. The 2026-05-29
   run proposed **P0 gate-surgery** off these same (uncorrected) MCs — that was the C23 failure
   mode, and this run demonstrates it directly: the headline tool tiers are **hypotheses, not
   facts**.
3. **C32 ubiquity does not fire.** Max citation fraction is 0.26 (`cumulative-premium-flow`,
   n=96). Nothing exceeds the 0.60 ubiquity threshold — but citations are so **sparse** (no tool
   on >26% of rows) that the **CONFOUNDED detector structurally cannot fire** either. Absence of
   CONFOUNDED/ubiquity flags is a data property, not a clean bill.

## Tool tier list (N ≥ 5) — with the 2026-05-29 MC beside it

| Tool | N | MC (pp) | 05-29 MC | Tier | Δ |
|---|---|---|---|---|---|
| `uw options-structure today-gamma-flip` | 10 | +63.2 | +25.0 | LOAD-BEARING | tiny-N |
| `uw options-structure multileg-activity` | 9 | +50.6 | +57.1 | LOAD-BEARING | stable |
| `uw options-flow multi-day-sweep-persistence` | 10 | +22.3 | +31.9 | LOAD-BEARING | stable |
| `uw options-flow sector-flow-persistence` | 27 | +15.5 | −6.8 | LOAD-BEARING | **flipped +** |
| **`uw dark-pool block-stratified`** | 59 | **+14.0** | +25.4 | **LOAD-BEARING** | **durable** |
| **`uw options-structure dex`** | 58 | **+14.0** | +15.5 | **LOAD-BEARING** | **durable** |
| `uw insights earnings-play` | 8 | +13.9 | +7.6 | LOAD-BEARING | up |
| `uw options-structure term-skew` | 56 | **+7.9** | **−13.4** | SUPPORTIVE | **SIGN FLIP** |
| `uw historical cumulative-premium-flow` | **96** | **+1.7** | +2.0 | **NO-INFO** | **durable** |
| `uw historical oi-trend` | 51 | **+0.4** | **+12.2** | NO-INFO | **collapsed** |
| `uw insights signal-confluence` | 22 | **−1.0** | **+17.2** | NO-INFO | **collapsed** |
| `uw hot-chains sweep-persistence` | 27 | **−2.6** | **+19.5** | NO-INFO | **collapsed** |
| `uw insights institutional-accumulation` | 6 | −15.1 | −12.6 | NEGATIVE (thin) | durable − |
| `uw historical gex` / `options-structure gex` | 8/12 | −33 / −50 | −27 / 0 | NEGATIVE | durable − |
| `uw insights conviction-matrix` | 7 | −53.1 | −40.1 | NEGATIVE (thin) | durable − |

(23 tools INSUFFICIENT_N at <5 citations, excluded. `*thin*` = N 5–7, provisional.)

## Desk commentary (market-maker quant)

- **Only two tools are durable LOAD-BEARING across BOTH the close-only and path-aware methods:
  `dark-pool block-stratified` (+25→+14) and `options-structure dex` (+15.5→+14).** These are the
  desk's two real evidence tools. Everything else moved — often by 15–30pp — when the resolution
  method changed. *A tool whose tier depends on whether you resolve close-only or path-aware was
  never a measured edge.*
- **`term-skew` flipped sign (−13.4 → +7.9pp) — RETRACT the 05-29 "term-skew is anti-predictive"
  finding.** Both numbers are unreliable: term-skew is cited on vol/earnings rows, whose outcomes
  are **RV-proxy-resolved** (Phase 2). The proxy swung hard between runs (vol_long 53%→84%), so
  term-skew's attribution swung with it. **Neither −13.4 nor +7.9 is trustworthy** — the
  attribution is a function of the vol proxy, not the tool. The 05-29 P1.3 ("demote term-skew")
  was a close-only artifact; kill it.
- **`oi-trend`, `signal-confluence`, `hot-chains sweep-persistence` all collapsed from
  LOAD-BEARING to NO-INFO.** The 05-29 P0.2 wanted to *add* `oi-trend` and `signal-confluence` to
  the HIGH-tier gate as replacements; under path-aware resolution they carry **no signal**. **The
  proposed gate-swap is not robust** — do not ship it.
- **`cumulative-premium-flow` is NO-INFO at the highest citation count in the book (+1.7pp,
  n=96).** This is the one NO-INFO finding durable across both methods. It is the single
  most-cited evidence tool and it does not separate winners — a reflexive comfort citation. But on
  reconstructed citations + no BH survival, demoting its rubric line is a **P1/P2**, not a P0.
- **The negative cluster (`gex`, `conviction-matrix`, `institutional-accumulation`,
  `pc-ratio-zscore`) is durable across both runs** — these consistently fire more on losers. The
  LEAP/gamma tooling remains the most suspect, but all are thin-N and BH-insignificant.

## `fz` advisory dimensions (C15–C18) — gating the Phase-B promotions

| Axis (criterion) | Decided envelope N | Verdict |
|---|---|---|
| squeeze_pressure (C15) / float (C16) / analyst-div (C17) / insider (C18) / breadth | **0** | INSUFFICIENT_N |

`fz_context` exists only on envelope rows, and **0 envelope rows are decided** (all window_open —
`fz` shipped 05-27, two trading days before the cutoff). **No `fz` criterion clears its threshold;
C15–C18 stay advisory (0 pts).** Re-test ~2026-06-12.

## Output
- `phase_4_tools.jsonl` — full tool table with `mc_pp`, `p`, `bh_significant`, `cite_frac`,
  `ubiquity_confounded`, `thin_n`. `phase4_tools_v2.py` — reproducible.
