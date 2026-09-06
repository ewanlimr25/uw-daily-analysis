# Data correction — 2026-07-27 run

## What happened

`scripts/market_data.py` returned **non-deterministic `change_1d_pct` / `change_5d_pct`** across two invocations with identical arguments (`--as-of 2026-07-27`, same symbol list membership, minutes apart). `last_close` was stable and correct in every case; only the percentage-change denominators moved. The bug therefore lives in how the prior-close index is selected from the returned chart window, not in the price fetch.

The **first** invocation seeded `step0_context.json`, which was handed verbatim to all 10 Phase 1 agents.

## Authoritative source used for the correction

`uw historical trend --symbol <T> --days 7` close-to-close, which is the project-endorsed fallback for price moves. It reconciles exactly with the second `market_data.py` run on every disputed row.

## Corrected rows (wrong value → correct value)

| Symbol | 1d as shipped to agents | 1d CORRECT | 5d as shipped | 5d CORRECT | Severity |
|---|---|---|---|---|---|
| **MU** | −9.09% | **−2.25%** | +6.04% | **+4.01%** | **MATERIAL** |
| **INTC** | −8.54% | **−0.70%** | −3.55% | **−5.55%** | **MATERIAL** |
| **XLK** | −2.33% | **−0.90%** | −0.73% | −0.80% | **MATERIAL** |
| GLOB | +6.63% | +4.28% | +1.27% | +1.08% | moderate |
| BSX | +4.43% | +2.85% | +3.36% | +3.98% | moderate |
| TCOM | +4.07% | +2.59% | +5.47% | +1.31% | moderate |
| COIN | +3.93% | +5.81% | +6.60% | +4.40% | moderate |
| JPM | +1.80% | +0.85% | +4.43% | +5.11% | minor |

Verified UNCHANGED and correct: SPY +0.02%, QQQ −0.31%, IWM +0.60%, RSP +0.75%, SNDK −11.02%, ASML −5.80%, AMD −5.17%, NVDA −4.99%, LITE −6.69%, AMKR −6.54%, LRCX −4.46%, STX −4.07%, COHR −3.92%, DELL −2.42%, TSLA −1.22%/−16.33%, PLTR +7.00%, NOW +6.86%, MSTR +7.61%, ORCL +4.27%, GM +5.32%, LW +7.12%, GOOGL +2.13%, MSFT +1.94%, AAPL +1.17%, COST +1.77%, AMZN −0.31%, USO −8.73%, and all sector ETFs other than XLK.

## Does the tape thesis survive?

**Yes, and it sharpens.** The day is still a semis-led unwind inside a broad-green rotation:
SNDK −11.02%, LITE −6.69%, AMKR −6.54%, ASML −5.80%, AMD −5.17%, NVDA −4.99%, LRCX −4.46%, STX −4.07%, COHR −3.92%, SMH −2.25%, SOXX −2.05% — against MSTR +7.61%, LW +7.12%, PLTR +7.00%, NOW +6.86%, COIN +5.81%, GM +5.32%, DBX +4.62%, ORCL +4.27%, and 65.2% of S&P names green with RSP +0.75% > SPY +0.02%.

XLK at −0.90% rather than −2.33% actually **confirms the within-tech rotation read more cleanly**: the semis sub-complex fell hard while software rallied, so the sector aggregate barely moved. That is the signature of rotation *inside* tech, not a tech-wide selloff.

## Blast radius on Phase 1 conclusions

**Conclusions that STAND (evidence independent of the bad pct):**
- `accumulation-hunter` empty board + the 20:00–20:15Z closing-cross finding — derived from `executed_at` timestamps and `trade_vs_mid`, not price moves.
- `accumulation-hunter` GOOGL/AAPL DISTRIBUTION — broad-sample buy/sell ratios.
- `contrarian-scanner` empty board — z-scores, unaffected.
- `multileg-strategist` SMH / WOLF / INTC **structures** — leg-level prints, timestamps, OI conversion, and (for INTC) an independent Black-Scholes repricing that matched both legs to the penny at S=92.125. Structure findings are robust.
- `dealer-positioning` NVDA and PLTR mechanized DEX flips — computed by `scripts/dex_flip.py` from dated `net_dex`, not price.
- `leap-positioning-radar` empty board — OI/flow gates.
- SNDK-based conclusions everywhere — SNDK's −11.02% was correct.

**Conclusions whose RATIONALE is damaged (findings downgraded):**
1. `vol-surface-scout` **MU BUY VOL** — premised on "realised vol has already outrun implied after today's −9% print." MU fell 2.25%. The negative-VRP tool output (−0.126) is not itself derived from the bad figure, but the agent's own GS percentile read (42.47, NORMAL, vs raw IV rank 79.9) already argued MU's elevation was a single-day artifact — and the single day was smaller than believed. **MU downgraded; it failed the 2-agent confluence gate regardless.**
2. `multileg-strategist` **INTC** narrative framing ("a contrarian bid for the semis washout") — there was no washout in INTC today (−0.70%). The **structure** stands; the *characterisation* does not. Re-framed in the report as ordinary long-horizon positioning rather than knife-catching.
3. `sweep-tracker` and `contrarian-scanner` MU/INTC "falling knife" / "capitulation after −8.5%" framing — the underlying flow observations (bid-side put unwind on MU; call-OI closing on INTC) are tape-derived and stand; the price framing is corrected.

**No confluence-gate outcome changes.** The four names that cleared ≥2 agents (PLTR, SMH, INTC, TSLA) all cleared on structural/flow evidence, and MU/INTC's corrected moves do not add or remove any agent flag.

## Action

Registered as a **P0 data-integrity item for the next `/calibration-audit`**: `scripts/market_data.py` must be made deterministic (pin the prior-close index to an explicit trading-date lookup rather than a positional offset into a variable-length window) and should cross-check against `uw historical trend` closes. Until then, treat `market_data.py` percentage columns as **advisory** and source price moves for the report from `uw historical trend`. The C12 liquidity floor itself (price + dollar-ADV) is **unaffected** — it uses `last_close` and volume, both of which were stable across runs.
