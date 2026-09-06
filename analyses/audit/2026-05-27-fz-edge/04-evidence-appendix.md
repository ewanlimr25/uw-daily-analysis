# 04 — Evidence appendix (reproducible)

All commands run **2026-05-27** against `fz` (`finviz-pp-cli 1.0.0`, `/Users/ewan/.local/bin/fz`).
Every quantitative claim in `01`–`03` resolves to one of these. Re-run any line to reproduce.

---

## §1 — `fz quote` carries the "intentionally absent" fields

```bash
fz quote AAPL --agent
```

Returned fields (excerpt — the gap-closing ones the repo lists as absent):

```
Short Float    : 0.92%
Short Interest : 134.68M
Short Ratio    : 3.05        # days-to-cover
Shs Float      : 14.67B
Shs Outstand   : 14.69B
Option/Short   : Yes / Yes
Inst Own       : 66.04%
Inst Trans     : 0.38%
Insider Own    : 0.12%
Insider Trans  : -1.93%
Recom          : 1.98        # 1=strong buy … 5=strong sell
Target Price   : 316.07      # vs Price 310.85 → +1.7% to target
RSI (14)       : 78.85
SMA20/50/200   : 5.95% / 13.92% / 18.46%
Beta           : 1.08
ATR (14)       : 5.75
Volatility     : 1.61% 1.94% # week / month realized
52W High/Low   : -0.31% / 59.35%
Earnings       : Apr 30 AMC
IPO            : Dec 12, 1980
```

Full payload is 84 fields incl. P/E 37.60, Fwd P/E 32.32, PEG 2.59, P/FCF 35.34, EV/EBITDA 28.64,
ROE 141.47%, margins, growth, dividend — the complete valuation/quality grid.

**Field projection (verified syntax — matters for the wrapper):**
```bash
# WORKS — unquoted dotted paths, comma-separated (spaces/parens in keys are fine):
fz quote AAPL --agent --select 'fundamentals.Short Float,fundamentals.Short Ratio,fundamentals.Shs Float'
#   → {"fundamentals":{"Short Float":"0.92%","Short Ratio":"3.05","Shs Float":"14.67B"}}
# FAILS — inner double-quotes around keys return an empty object:
fz quote AAPL --agent --select 'fundamentals."Short Float"'   # → {"fundamentals":{}}
# ROBUST — full quote piped to jq (recommended for the enrichment wrapper):
fz quote AAPL --agent | jq -c '{short_float:.fundamentals."Short Float", days_to_cover:.fundamentals."Short Ratio", float:.fundamentals."Shs Float", recom:.fundamentals.Recom, target:.fundamentals."Target Price"}'
#   → {"short_float":"0.92%","days_to_cover":"3.05","float":"14.67B","recom":"1.98","target":"316.07"}
```

**Backs:** E1 (short interest/float), E2 (float), E4 (analyst), E8 (RSI/SMA/52W), and `03` wrapper
syntax. Repo gap: `AUDIT.md §4` "Short interest + borrow rate — genuinely missing"; data-sources
table "Intentionally absent".

---

## §2 — `fz screen` does candidate generation with a short-interest filter (free, no Elite)

```bash
fz screen --filter cap_midover,sh_short_o15 --view overview --agent
```

Returned a live qualified list (excerpt): `AAP` (Advance Auto Parts, +5.68%), `ACHC`, `ACHR`
(Archer Aviation, vol 57.98M), `AEHR` (-5.55%), … — each with Ticker, Company, Sector, Industry,
Market Cap, P/E, Price, Volume. `sh_short_o15` = short float > 15% (squeeze candidate lane).

`fz screen --help` confirms filter/view/signal/preset grammar:
- filters: `cap_large,sec_technology,fa_pe_u20`, `idx_sp500`, `sh_short_o15/o20`, `sh_price_o5`, `earningsdate_thisweek`
- views: `financial|overview|ownership|performance|technical|valuation`
- presets (Elite-free): `dividend-growth, earnings, etf, most-active, new-high, top-gainers, top-losers, trend-reversion, uptrend, volume-surge`
- `--save <name>` enables `screen-diff`.

**Backs:** E3 (squeeze/RS funnel lane + server-side liquidity floor).

---

## §3 — `fz insider-clusters` returns multi-insider consensus (net-new vs MSPR)

```bash
fz insider-clusters --days 7 --min-buyers 2 --side buy --agent
```

```json
[ { "DistinctOwners": 2, "Side": "buy", "Ticker": "WHF", "Transactions": 3 } ]
```

A distinct-buyer **count** (2 owners, 3 transactions), not a blended ratio. **Backs:** E5.

---

## §4 — `fz breadth` turns the heatmap into a logged figure

```bash
fz breadth --group sector --agent
```

```json
{ "advancers": 236, "decliners": 263, "pct_green": 46.92, "avg_change": 0.01,
  "median_change": -0.05, "total": 503, "unchanged": 4,
  "top_mover": "APP", "top_pct": 10.42, "worst_mover": "BSX", "worst_pct": -12.46,
  "timeframe": "1d", "captured_at": "2026-05-27T23:04:20Z", "dataset": "sec_all" }
```

**Backs:** E6 (logged regime cross-check; `--days N` makes it a trend).

---

## §5 — Operational facts (from `fz --help` and `SKILL.md`)

- No auth required except bulk `export` (Finviz Elite token). All screening/quote/insider/breadth = free public HTTP.
- `--agent` = `--json --compact --no-input --no-color --yes`. `--select` projects fields (dotted paths).
- Default rate limit **2 req/s**; response caching on; local SQLite store at `~/.local/share/finviz-pp-cli/data.db`.
- Exit codes: `0/2/3/5/7/10` (ok/usage/not-found/api/rate-limited/config) → drives graceful-skip.
- Source/skill: `/Users/ewan/printing-press/library/finviz/{README.md,SKILL.md}`.

**Backs:** `03` Prerequisites (permission, graceful-skip, wrapper, rate limit).

---

## §6 — Honest-limit checks (claims in `01 §"What fz is NOT"`)

- `fz --help` lists **no** options-flow / greeks / dark-pool / GEX / OI command — confirms `fz`
  cannot duplicate any `uw` microstructure tool (limit #1).
- Finviz short float is the exchange semi-monthly settlement value, ~2-week lag (limit #3); `fz quote`
  exposes no borrow-fee / HTB field (limit #4) — grep the 84-field payload: no such key.
