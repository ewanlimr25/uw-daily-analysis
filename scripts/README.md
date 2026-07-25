# scripts/

Stdlib-only Python helpers that extend the markdown agent fleet with two data
sources Unusual Whales does not provide (fundamentals, hard macro) plus a
machine-checkable contract for the daily/weekly decision envelope.

No third-party packages are required — everything runs on a bare Python 3.12
(`Bash(python3:*)` is already allowed). API keys resolve via `_env.py`:
**process env → repo `.env` → documented sibling fallback** (so the Finnhub
secret is never copied out of `claude-trading-agents/.env`).

| Script | Used by | Output |
|---|---|---|
| `finnhub_enrich.py --ticker T --date D [--lookback N]` | `fundamentals-gate` agent (Phase 1.5) | JSON: metrics, earnings-surprise streak, insider MSPR, news catalysts, next-earnings date, and a direction-agnostic bullish/bearish/caution assessment |
| `fz_enrich.py --ticker T --date D` | `fundamentals-gate` agent (Phase 2b) | JSON: raw Finviz fields + a direction-agnostic `derived` block — short float %, days-to-cover, parsed float, `squeeze_pressure`, analyst `recom`, upside-to-target. Shells out to the **`fz` CLI** (`finviz-pp-cli`); the non-flow context (short interest / float / analyst) the UW fleet is blind to. **Advisory (0 rubric points)** — see `analyses/audit/2026-05-27-fz-edge/`. `$FZ_PP_CLI` overrides the binary path. |
| `fred_macro.py [--limit N]` | daily/weekly **Step 0** | JSON: latest prints + derived signals (yield-curve sign, inflation/labor trend, USD & 10Y direction) for the shared `macro_snapshot` |
| `step0_cache.py --date D [--regime R] [--only names] [--refresh] [--list]` | daily/weekly **Step 0 sub-step 1a** | Fetches the ~22 **market-wide** `uw` payloads ONCE into `analyses/daily/<date>/step0_cache/` and prints a manifest (`paths`, per-file `command`, `failed[]`). Registry entry bar: market-wide (no `--symbol`) **and** ≥2 declared consumers. Fixes a measured duplicate — `earnings-scout` and `vol-surface-scout` each fetched a byte-identical 528,504-byte `earnings-catalyst` payload on 2026-07-24. Reuses cached files unless `--refresh` |
| `market_data.py --symbols S1,S2,...` | daily/weekly **Step 0** C12 floor + tape framing; debate lane | Raw Yahoo chart API OHLCV → `c12_pass[]` / `c12_fail[{symbol,reason}]`, `last_close`, `adv_usd_millions`, `change_1d_pct`, `change_5d_pct`, `realized_vol_pct{rv20,rv60}`. Closes the C12 **acquisition** gap: `excess_winrate.py` owns the decision but delegated the fetch, and `uw historical trend` has no OHLC or share volume. Fail-closed — an unfetchable symbol is a C12 FAIL with a reason |
| `dex_flip.py --symbol T --dates D1,D2,... \| --file F` | `dealer-positioning-strategist`; verified by `signal-confluence-quant` | The **scored** +1 mechanized DEX sign-flip line (2026-06-12 audit P0.4). Returns `qualifies`, `direction`, dated `prior_run_*`, `trailing_median_abs_net_dex`, `magnitude_floor`, `magnitude_ratio`, a rubric-ready `evidence` string, plus `sign_changes_in_window` / `whipsaw_warning`. Floor excludes the flip day from its own median; ISO dates required |
| `term_structure_hygiene.py --file F` | `vol-surface-scout`, `earnings-scout` | Re-derives IV term structure after dropping the `dte_approx: 0` bucket and sub-`min_contracts` tenors. Raw label was BACKWARDATION on **39/41** names 2026-07-24; **14 flipped**. Emits kink-aware `shape` **and** monotonic `base_shape`, `front_end_ratio` at `--near-dte 7`, `kink_candidates[]`, and per-tenor `drop_reason`. `NO_NEAR_TENOR` ≠ `FLAT`. `min_contracts` is tunable, **not audit-frozen** |
| `validate_decision.py --file F` | daily/weekly **Step 9/10** + `/calibration-audit` Phase 1 | Validates `analyses/**/decision.json` against `schemas/decision_envelope.schema.json` + cross-field invariants (Σ component points == raw_score; tier ≤ score band; VETO ⇒ size skip) |

Every fetch script **always exits 0** and prints a valid JSON object — on a
missing key, non-US ticker, paid-endpoint 403, or a missing/erroring `fz`
binary it emits `available:false` / `fz_available:false` (or per-section
`errors[]`) so the calling agent never parses an empty payload and a report
never hard-fails on an enrichment source.

## Setup

```bash
cp .env.example .env          # then add FRED_API_KEY (free)
# FINNHUB_API_KEY is optional here — falls back to the sibling repo's .env
```

## Tests

```bash
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
```

Tests inject a fake HTTP getter or subprocess runner, so they never touch the network or the
`uw` binary.

## CLI flag traps (verified 2026-07-24)

`uw screener iv-rank` takes **`--mode high|low`**. Its neighbours `uw screener bullish-bearish` and
`uw insights signal-confluence` take **`--direction bullish|bearish`**. Flag-transfer between them is
the natural error and cost two failed calls; `step0_cache.py` encodes the correct flag per payload
and `test_step0_cache.py` regression-tests it. `uw historical vrp` **requires `--symbol`** — there is
no market-wide mode.
