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
| `fred_macro.py [--limit N]` | daily/weekly **Step 0** | JSON: latest prints + derived signals (yield-curve sign, inflation/labor trend, USD & 10Y direction) for the shared `macro_snapshot` |
| `validate_decision.py --file F` | daily/weekly **Step 9/10** + `/calibration-audit` Phase 1 | Validates `analyses/**/decision.json` against `schemas/decision_envelope.schema.json` + cross-field invariants (Σ component points == raw_score; tier ≤ score band; VETO ⇒ size skip) |

Every fetch script **always exits 0** and prints a valid JSON object — on a
missing key, non-US ticker, or paid-endpoint 403 it emits `available:false`
(or per-section `errors[]`) so the calling agent never parses an empty payload.

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
