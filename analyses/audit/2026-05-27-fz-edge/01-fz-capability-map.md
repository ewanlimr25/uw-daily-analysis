# 01 — `fz` capability map (verified)

`fz` = `finviz-pp-cli` v1.0.0, a Go binary at `/Users/ewan/.local/bin/fz`. Source:
`/Users/ewan/printing-press/library/finviz/` (skill: `SKILL.md`, name `pp-finviz`). It screens
Finviz, pulls 84-field fundamentals, tracks insider trades, and reads market breadth **over plain
HTTP with no Elite subscription** (only the bulk `export` needs a token). Every read also persists
to a local SQLite store (`~/.local/share/finviz-pp-cli/data.db`), which is what powers the
change-over-time commands. All output below was produced by live calls on **2026-05-27** (see `04`).

## Invocation model (matches this repo's `uw` CLI pattern)

`fz` is a Bash CLI exactly like the repo's `uw` binary — so integration is the same shape as the
2026-05-27 MCP→CLI migration: a `Bash(fz:*)` permission and direct invocation, no MCP schemas in
context.

- `--agent` expands to `--json --compact --no-input --no-color --yes` (agent-safe, pipeable).
- `--select a,b,c` projects only named fields (dotted paths descend into nested JSON / arrays) —
  critical for keeping agent context small.
- `--data-source auto|live|local` (auto = live with local fallback); `--max-age 30m` freshness hint.
- `--deliver file:<path>|webhook:<url>` routes output; `--rate-limit` default **2 req/s**.
- Exit codes: `0` ok · `2` usage · `3` not found · `5` API error · `7` rate-limited · `10` config.

## Commands relevant to this repo

### `fz quote <T> --agent` — 84 fundamental fields in one call
The payload (verified on AAPL, `04 §1`) carries the fields this repo lists as **absent**:

| Group | Fields (exact Finviz labels) |
|------|------|
| **Short interest** (repo gap) | `Short Float` (% of float short), `Short Interest` (shares), `Short Ratio` (**days-to-cover**), `Option/Short` ("Yes / Yes") |
| **Float / shares** (repo gap) | `Shs Float`, `Shs Outstand` |
| **Ownership** (repo gap) | `Inst Own`, `Inst Trans` (Δ), `Insider Own`, `Insider Trans` (net %) |
| **Analyst** (repo gap) | `Recom` (1.00 strong-buy → 5.00 strong-sell), `Target Price` |
| **Technicals / RS** | `RSI (14)`, `SMA20` `SMA50` `SMA200` (% from), `Beta`, `ATR (14)`, `Volatility` (week/month realized), `Rel Volume`, `Avg Volume`, `52W High`/`52W Low` (% from), `Perf Week…Perf 10Y`, `Perf YTD` |
| **Valuation / quality** | `P/E`, `Forward P/E`, `PEG`, `P/S`, `P/B`, `P/FCF`, `P/C`, `EV/EBITDA`, `EV/Sales`, `ROE`, `ROA`, `ROIC`, `Gross/Oper./Profit Margin`, `Debt/Eq`, `LT Debt/Eq`, `Current/Quick Ratio`, `EPS/Sales Surpr.`, `EPS …Y/Q growth`, `Sales …growth`, `Dividend`, `Payout` |
| **Events / meta** | `Earnings` ("Apr 30 AMC"), `IPO` ("Dec 12, 1980"), `Index` (DJIA/NDX/S&P 500), `Employees`, `Market Cap`, `Income`, `Sales` |

`fz quote --tickers A,B,C` returns the **whole peer group** in one call (peer-breadth comparison).

### `fz screen --filter <codes> --view <v> --signal <s>` — universe screen, no Elite
Raw Finviz filter codes, comma-joined. Verified working (`04 §2`): `cap_midover`, `sec_technology`,
`idx_sp500`, `fa_pe_u20` (P/E<20), and crucially **`sh_short_o15`/`sh_short_o20`** (short float
>15%/>20%), `sh_price_o5`, `sh_avgvol_o…`, `ta_*` signals, `earningsdate_thisweek`.
Views: `overview|valuation|ownership|performance|financial|technical`. `--preset` gives Elite-only
screens free (`volume-surge`, `earnings`, `new-high`, `top-gainers/losers`, `uptrend`,
`trend-reversion`). `--save <name>` turns a screen into a tracked series for `screen-diff`.

### `fz insider-clusters --days N --min-buyers M --side buy|sell` — multi-insider consensus
Surfaces tickers where ≥M **distinct** insiders traded the same side in a window — the conviction
signal a row-by-row Form-4 list hides. Verified (`04 §3`): returned `WHF` with 2 distinct owners,
3 transactions, side `buy`. **Not** a blended ratio (unlike Finnhub MSPR) — it is a distinct-buyer
*count*, a different and conviction-dense framing.

### `fz breadth --group sector|world|etf [--timeframe 1d|1w|…] [--days N]` — quantified breadth
Turns the heatmap into hard numbers. Verified (`04 §4`): `advancers 236`, `decliners 263`,
`pct_green 46.92`, `avg_change`, `median_change`, `top_mover/worst_mover`, `total 503`, timestamped.
`--days N` replays cached snapshots as a trend. A free, **logged** advance-decline series.

### `fz groups --by sector|industry|country --view performance|valuation` — group aggregates
Per-group market cap, P/E, dividend, change, volume — sector valuation/momentum context.

### Change-over-time (local SQLite; needs a prior snapshot / `sync`)
- `fz quote-drift <T> --since DATE` — field-level diff of two fundamental snapshots (which of the
  84 fields moved: short float spike, analyst target cut, P/E re-rate).
- `fz screen-diff <name> --since DATE` — which tickers **entered/left** a saved screen between runs.
- `fz watchlist-digest --since DATE` — per watchlist name: fundamental drift + new insider activity
  + new-news counts, in one read.

### Supporting
`fz prices --ticker T --timeframe d|w|m|i1|i5|i15 --tail N` (OHLCV incl. intraday) ·
`fz news --ticker T` · `fz map` (S&P heatmap) · `fz perf crypto|forex|futures` ·
`fz sync` / `fz workflow archive` (populate the store) · `fz which "<capability>"` (NL routing) ·
`fz agent-context` (machine-readable CLI schema) · `fz doctor` (health check).

## What `fz` is NOT (honest limits — do not over-adopt)

1. **No microstructure.** Zero options flow, greeks, dark pool, IV term structure, GEX/DEX, OI.
   It cannot replace or duplicate a single `uw` tool. Strictly a fundamentals/screen/breadth/insider
   augment **beside** the flow engine.
2. **EOD / delayed, not intraday tick.** Finviz public surfaces are end-of-day for fundamentals
   (intraday only via `prices`). Fine for slow-moving SI/float/fundamentals; **never** for 0DTE timing.
3. **Short interest is the semi-monthly settlement figure (~2-week lag).** Good for squeeze
   *context* and gating, **not** a live borrow signal.
4. **No borrow fee / HTB flag.** `fz` gives short float, days-to-cover, and float — but **not**
   borrow cost or hard-to-borrow status. WebSearch/Ortex still required for that leg. So `fz`
   *partially* closes `AUDIT.md §4`'s "short interest + borrow rate" gap: SI/DTC/float ✅, borrow ❌.
5. **`Recom`/`Target`/earnings/EPS surprise** overlap Finnhub (already integrated). `fz` is a
   cross-source check / fallback there, **not** net-new — *except* `insider-clusters`' distinct-buyer
   framing, which is net-new vs Finnhub's blended MSPR.
6. **Aggregations need history.** `quote-drift`/`screen-diff`/`watchlist-digest` require a prior
   snapshot in the local store (run `fz quote`/`screens run`/`sync` first). Cold-start returns nothing.
