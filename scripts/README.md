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

Tests inject a fake HTTP getter, so they never touch the network.
