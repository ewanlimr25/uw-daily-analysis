# Single-Leg Whale Edge Analysis
**Date:** 2026-05-29  
**Type:** Methodology + Data Structure Research  
**Status:** Pre-backtest findings; see `single_leg_whale_backtest_report.md` for empirical results

---

## Motivation

The question: does a single-leg, large-premium, single-transaction option print on an individual stock carry a predictive edge for next-day price direction?

The hypothesis comes from market microstructure theory:
- **Pan & Poteshman (2006, RFS 19:871):** Only *opening* buy option volume predicts stock returns (~+40bps next day / +1%/week). Closing and institutional hedging flow predicts nothing.
- **Easley, O'Hara & Srinivas (1998):** Large option trades — especially when aggressively hitting the ask — concentrate private information.
- **Chakravarty, Gulen & Mayhew (2004):** Price discovery in options markets occurs disproportionately in single-leg directional trades, not spread/hedging activity.

---

## The Problem with `uw options-flow top-premium-trades`

The CLI's `top-premium-trades` command surfaces the largest-premium option transactions without filtering for trade structure. On a typical trading day, the "top premium" list is dominated by:

| OPRA Condition | Leg type | What it actually represents | Signal quality |
|---|---|---|---|
| `auto`, `slan`, `isoi`, `slai` | single-leg electronic | Electronic directional bets, sweeps | HIGH |
| `slft`, `slcn` | single-leg floor/negotiated | Institutional blocks, negotiated | MEDIUM |
| `mlet`, `mlat`, `mlft`, `mfsl`, `mesl`, `masl`, `mlct` | multi-leg | Spreads, hedges, rolls — NOT directional bets | LOW / noise |
| `cbmo` | cabinet | Deep-OTM near-zero value, portfolio restructuring | TRASH |

**On 2026-05-28, the `cbmo` category alone showed $9.6B "premium"** — purely from size × near-zero contract prices on deep-OTM restructuring. Multi-leg floor trades added another $3.7B. Neither is a directional bet.

The `uw options-flow top-premium-trades` output without condition-code filtering pollutes the signal with multi-leg activity and cabinet orders. A $36M "print" on a floor-negotiated multi-leg spread (`mfsl`/`mlft`) tells you nothing about a trader's directional view.

---

## OPRA Condition Code Taxonomy

The `upstream_condition_detail` field in the `All Options` Parquet files carries OPRA trade condition codes that precisely identify trade structure:

### Single-leg codes (the clean signal lane)
| Code | Full name | Characteristics |
|---|---|---|
| `auto` | Automatic execution | Electronic, market-order or limit-hit; the most common retail/institutional sweep |
| `slan` | Single-Leg Auction, Non-ISO | Auction-mechanism fill; slightly slower, often larger |
| `isoi` | Intermarket Sweep, ISO | Cross-exchange aggressive sweep; urgency signal |
| `slai` | Single-Leg Auction, ISO | Auction + sweep aggression combined |
| `slft` | Single-Leg Floor Trade | Floor-executed institutional block |
| `slcn` | Single-Leg Customer Negotiated | Bilateral institutional negotiation; large blocks |

### Multi-leg codes (exclude for directional analysis)
| Code | Full name | Why excluded |
|---|---|---|
| `mlet` | Multi-Leg Electronic | Spreads, straddles, collars — net position is mixed |
| `mlat` | Multi-Leg Auction | Same, auction-mode |
| `mlft` | Multi-Leg Floor Trade | Institutional spread/roll execution |
| `mfsl` | Multi-Leg Floor, Stock/Option | Delta-hedged option + stock combo |
| `mesl` | Multi-Leg Electronic, Stock/Option | Same, electronic |
| `masl` | Multi-Leg Auction, Stock/Option | Auction-mode delta hedge |
| `mlct` | Multi-Leg Customer | Bilateral multi-leg negotiation |

### Other
| Code | Full name | Note |
|---|---|---|
| `cbmo` | Cabinet Order | Deep-OTM near $0.01 value — portfolio clean-up, not directional |
| `tlet`/`tlat`/`tlft`/`tlct` | Two-Leg variants | Ambiguous (could be straddle or directional) — excluded |

**Volume breakdown on 2026-05-28:**
| Category | Count | Total Premium |
|---|---|---|
| `auto` (single-leg) | 4,916,311 | $12.9B |
| `mlet` (multi-leg) | 1,310,115 | $10.8B |
| `cbmo` (cabinet) | 3,487 | **$9.6B** (inflated by size) |
| `slan` (single-leg) | 2,393,249 | $4.7B |
| `mlat` (multi-leg) | 1,178,403 | $3.2B |
| `mlft` (multi-leg floor) | 3,267 | $2.0B |

---

## Signal Quality Hierarchy

From strongest to weakest, for a directional single-leg call/put:

1. **`auto`/`isoi` + `side=ask` + `size/OI >> 1`**  
   Electronic, aggressive, clearly opening a new position. The Pan-Poteshman "buy-to-open" signal.

2. **`slft`/`slcn` + `side=ask` + large premium**  
   Floor/negotiated institutional block. Less urgency in execution, but potentially more informed — an institution willing to negotiate a block is making a considered bet, not reacting to a data feed.

3. **`slan`/`slai` + `side=ask`**  
   Auction-mode fills; slightly less aggressive. Sometimes used for large orders to minimize market impact.

4. **Any of the above with `size/OI < 0.2`**  
   Likely closing an existing position (rolling out, taking profit, or hedging). Low signal value per Pan-Poteshman.

### The `size / open_interest` ratio (opening pressure)
The single most important discriminator:
- `size / OI >> 1` (e.g., 741× as seen in CRDO on 2026-05-28): **new position from scratch** — strongest opening signal
- `size / OI ≈ 1`: ambiguous (could be opening or closing existing position)
- `size / OI << 0.2`: likely rolling/closing — weak signal or noise

When `OI = 0`, the ratio is infinite (assigned 999.0 in the script). A large print on an OI=0 contract is the purest opening signal possible.

---

## Sample Clean Single-Leg Prints (2026-05-28)

Filtering to: `canceled=false`, condition IN (auto, isoi, slan, slai), `side='ask'`, `equity_type='Common Stock'`, premium > $500K:

| Ticker | Type | Strike | Expiry | DTE | Premium | Delta | OI | Size/OI | Condition |
|---|---|---|---|---|---|---|---|---|---|
| MSFT | call | 440 | Jun 26 | 29 | $9.0M | 0.38 | 2,623 | 3.77× | auto |
| MU | call | 1,300 | Jun '27 | 385 | $5.9M | 0.55 | 315 | 0.77× | auto |
| QCOM | call | 240 | Jan '28 | 602 | $4.2M | 0.68 | 1,243 | 0.40× | auto |
| NVDA | call | 182 | Jun 18 | 21 | $3.2M | 0.91 | 4,642 | 0.20× | auto |
| **CRDO** | **call** | **340** | **Jan '27** | **232** | **$3.0M** | **0.45** | **1** | **741×** | **auto** |
| CRWD | call | 760 | Dec '27 | 567 | $2.7M | 0.58 | 702 | 0.24× | auto |

**CRDO** is the standout: 741 contracts into an OI of 1 — someone built a brand-new position from effectively zero. That's the Pan-Poteshman signal.

**NVDA** at 0.20× OI is likely a hedge or partial roll against an existing large position — much lower signal value.

---

## Aggression Premium (`price - nbbo_ask`)

A positive `paid_over_ask` means the buyer paid above the posted ask — the maximum expression of urgency. Analysis of the 2026-05-28 data showed most large clean prints executed at exactly the ask (`paid_over_ask ≈ 0`), with occasional slight premiums (NVDA at +$0.20). This is expected: at large size, market makers will let you fill at the ask without pushing you above it.

**The aggression signal is binary** — at-or-above ask vs below ask — rather than a continuous "how much above." The below-ask prints (negotiated blocks) are not necessarily less informed; institutions sometimes agree on a mid-market price precisely because the size is too large to absorb at ask.

---

## Key Data Fields in `All Options` Parquet

The raw parquet has all required fields for this analysis:

| Field | Use |
|---|---|
| `upstream_condition_detail` | OPRA condition code — single vs multi leg |
| `side` | `ask` / `bid` / `no_side` — aggression direction |
| `price` | Contract price filled |
| `nbbo_ask` / `nbbo_bid` | Posted quotes at fill time |
| `price - nbbo_ask` | Aggression premium (computed) |
| `size` | Contracts traded |
| `open_interest` | OI at time of trade — `size/OI` = opening pressure ratio |
| `premium` | Total dollar premium = price × size × 100 |
| `underlying_price` | Spot price at time of trade — used as signal entry price |
| `delta` | Directionality of the option |
| `expiry` | Expiry date — `(expiry - trade_date).days` = DTE |
| `equity_type` | Filter to 'Common Stock' only |
| `canceled` | Filter to `false` |

---

## What the `uw` CLI Cannot Do

| Required filter | CLI capability |
|---|---|
| Filter by OPRA condition code | ❌ No `--condition` flag on any command |
| Single-leg-only trades | ❌ `top-premium-trades` includes all conditions |
| `size / OI` opening pressure ratio | ❌ Not a computed field in any tool |
| Aggression (`price - nbbo_ask`) | ❌ Not exposed |
| Per-print trade-level data | ❌ All tools return aggregated/EOD summaries |

**The raw Parquet + DuckDB is the only path to clean single-leg whale analysis.** The `uw options-flow top-premium-trades` output is useful as a first-pass scan but must not be used as a directional signal without condition-code filtering.

---

## Implemented Tool

**`scripts/single_leg_whale.py`** — Scanner + backtest

```
python3 scripts/single_leg_whale.py --scan-date 2026-05-28 [--json]
python3 scripts/single_leg_whale.py --backtest [--min-premium 500000] [--json]
```

- **Scan mode**: Surfaces today's clean single-leg whale prints, ranked by premium, with size/OI ratio, DTE bucket, aggression, and directional bias.
- **Backtest mode**: Grades each signal against the next trading day's EOD price (using `LAST(underlying_price)` as EOD close proxy) and reports stratified win-rates with binomial p-values vs a 50% baseline, plus SPY market-excess.

See `single_leg_whale_backtest_report.md` for empirical results.
