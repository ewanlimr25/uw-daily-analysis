# Behaviors completely off — found during CLI migration (2026-05-27)

Per task criterion 3: anomalies surfaced while migrating `mcp__uw-pp__*` → `uw` CLI and
verifying against the 2026-05-26 baseline. None were *introduced* by the migration —
they are pre-existing in the MCP path too (the two faces share one binary). The migration
made them visible because writing explicit CLI flags forces the real parameter names.

## 1. `insights institutional-accumulation` — `lookback_days` is a FICTION param (genuinely off)

**Severity: HIGH (silent no-op).** The tool's only parameters are `--symbol` and `--date`
(TSV row 25). It has **no** window / lookback parameter. Yet the prose in
`daily-analysis.md`, `weekly-analysis.md`, `leap-positioning-radar.md`, and
`accumulation-hunter.md` passed `lookback_days=5` / `lookback_days=10` and treated the
two as a "5-day primary vs 10-day secondary" pass.

- **Actual behavior:** the window argument was silently ignored under **both** MCP and CLI.
  Every "5-day" and "10-day" institutional-accumulation call returned the **identical
  single-snapshot result**. The multi-window distinction the agents believe they are making
  has never existed.
- **Migration action taken:** removed the fake `` `lookback_days=N` `` flag from prose
  (now reads "a 5-day window" / "a 10-day window" as narrative intent only — no invalid flag
  is emitted to the CLI).
- **Recommended real fix (not done — behavior change, out of migration scope):** source the
  multi-day accumulation window from `uw historical oi-trend --days N` (which *does* take a
  window) and/or `uw historical cumulative-premium-flow --days N`, and treat
  `institutional-accumulation` as the single-date fingerprint it actually is.

## 2. `risk market-regime` — CLI regime string ≠ stored regime string (informational)

`uw risk market-regime` returns `regime = "TRANSITIONAL — Mixed signals, reduce position
size, wait for clarity"`. The `decision.json` stores `regime = "TRANSITIONAL — UPTREND"`.
The orchestrator drops the tool's verbose advisory tail and appends its **own** trend
qualifier (UPTREND/DOWNTREND, derived from SPY trend + breadth `bullish_pct`). Not a bug,
but consumers must **match on the base token** (`TRANSITIONAL` / `BULLISH` / `BEARISH`),
never string-equal the whole field. Base token + breadth (40.1%) reproduce exactly.

## 3. `historical vrp` — classification lives in `.regime`, not `.classification` (informational)

The VRP classification ("FAIR") is returned in the field `regime`, alongside
`interpretation`. There is no `classification` / `vrp_classification` key on the tool output
(that name exists only in the *envelope*). Anything reading VRP must read `.regime`.

## 4. `options-structure gex` — `call_wall` / `put_wall` are derived, not top-level (informational)

The GEX payload exposes `zero_gamma_level`, `regime`, `total_gex`, and `per_strike[]`
(`{strike, net_gex}`) — but **no** top-level `call_wall` / `put_wall`. Those are computed
downstream (call wall = largest +GEX strike above spot; put wall = most −GEX strike below).
Derivation reproduces the recorded 751 / 730 exactly. Any prose citing "call_wall" implies
this derivation, not a field read.

---

**No migrated command produced a CLI error during verification.** All 61 referenced
`uw <group> <subcommand>` forms execute and return valid JSON on data date 2026-05-26.
