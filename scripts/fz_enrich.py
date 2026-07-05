#!/usr/bin/env python3
"""Finviz (`fz` CLI) fundamentals/short-interest enrichment.

Wraps the ``fz`` CLI (``finviz-pp-cli``) to return, for ONE ticker, a compact
JSON object of the gate-relevant fields the UW microstructure fleet is blind
to — **short interest, days-to-cover, float, institutional/insider ownership,
analyst consensus + target, and price-structure (RSI / SMA / 52-week)**. The
``fundamentals-gate`` (Phase 2b) and Step-0 funnel consume it the same way they
consume ``finnhub_enrich.py``.

It is **direction-agnostic**: it surfaces facts plus a small ``derived`` block
(squeeze pressure, upside-to-target, parsed float) and leaves the long/short
interpretation to the calling agent, which supplies the thesis direction.

Honest limits baked into ``freshness_caveat`` (see ``analyses/audit/
2026-05-27-fz-edge/01``): Finviz short interest is the exchange **semi-monthly
settlement figure (~2-week lag)** — squeeze *context*, not a live borrow
signal — and ``fz`` exposes **no borrow fee / hard-to-borrow** field. All
``fz`` surfaces are EOD/delayed; never use for 0DTE timing.

2026-07-04 (audit P2 #5): fz 1.0.0's quote parser truncates the 84-field grid to
its first snapshot column, so the gate-relevant SI/float/insider/technical fields
are transparently backfilled from the screener ``ownership``/``technical`` views
(quote values win; failures skip silently). Analyst consensus (``recom`` /
``target_price``) exists in no screener view and is reported in ``upstream_gaps``
until the upstream quote parser is fixed — the C17 flow-vs-analyst axis starves
on new data until then, by upstream limitation, not by selection.

Usage:
    python3 scripts/fz_enrich.py --ticker AAPL --date 2026-05-27

Exit code: always 0. When ``fz`` is missing, the ticker is not found, or the
CLI errors, the script still prints a valid JSON object with
``available=false`` / ``fz_available=false`` and a ``skip_reason`` so the
caller never parses an empty payload (mirrors the yahoo-broken / Finnhub-403
graceful-skip pattern). Never hard-fails a report.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from datetime import datetime

TIMEOUT_SECONDS = 30

# Squeeze-pressure thresholds — the canonical desk inputs and the C15 gate cut
# (short float % of float, days-to-cover). Used only for the direction-agnostic
# `derived.squeeze_pressure` label; the SHORT-thesis −1 tier is risk-monitor's.
SQUEEZE_SHORT_FLOAT_PCT = 20.0
SQUEEZE_DAYS_TO_COVER = 5.0

FRESHNESS_CAVEAT = (
    "Finviz short interest is the exchange semi-monthly settlement figure "
    "(~2-week lag) — squeeze context, not a live borrow signal; no borrow "
    "fee / HTB status available. All fields EOD/delayed, never for 0DTE timing."
)

# --- 2026-07-04 upstream regression + screener-view fallback (2026-07-04 audit P2 #5) ---
# fz 1.0.0's quote parser truncates the 84-field fundamentals grid to the FIRST
# snapshot column (~14 valuation fields) — the SI / float / insider / analyst /
# technical fields the gate needs vanished from `fz quote` (first observed live on
# W27, logged as §7(8) "selector miss"; root-caused 2026-07-04 as an upstream parse
# regression, not a selection bug here). The screener views still carry most of
# them per ticker, so `enrich` transparently backfills any missing mapped field
# from `fz screen --tickers <T> --view ownership|technical`. Quote values always
# win; the fallback only fills gaps and never blocks (graceful-skip discipline).
#
# Analyst consensus fields (`recom`, `target_price`) exist in NO screener view —
# they are UPSTREAM-UNRECOVERABLE until finviz-pp-cli fixes its quote parser. The
# payload reports them in `upstream_gaps` so the fundamentals-gate / C17 collection
# can state the reason instead of silently starving.

# Output key -> exact Finviz field label inside the `fundamentals` object.
_FIELD_MAP = {
    "short_float": "Short Float",
    "short_interest": "Short Interest",
    "short_ratio": "Short Ratio",        # days-to-cover
    "shs_float": "Shs Float",
    "shs_outstanding": "Shs Outstand",
    "inst_own": "Inst Own",
    "inst_trans": "Inst Trans",
    "insider_own": "Insider Own",
    "insider_trans": "Insider Trans",
    "recom": "Recom",                    # 1.00 strong-buy .. 5.00 strong-sell
    "target_price": "Target Price",
    "price": "Price",
    "rsi": "RSI (14)",
    "sma20": "SMA20",
    "sma50": "SMA50",
    "sma200": "SMA200",
    "high_52w": "52W High",
    "low_52w": "52W Low",
    "beta": "Beta",
    "market_cap": "Market Cap",
    "earnings": "Earnings",
    "index": "Index",
}

# Output key -> screener-row label, per view, for the quote-grid fallback.
_SCREEN_VIEW_FIELD_MAP = {
    "ownership": {
        "short_float": "Short Float",
        "short_ratio": "Short Ratio",
        "shs_float": "Float",
        "shs_outstanding": "Outstanding",
        "inst_own": "Inst Own",
        "inst_trans": "Inst Trans",
        "insider_own": "Insider Own",
        "insider_trans": "Insider Trans",
        "price": "Price",
        "market_cap": "Market Cap",
    },
    "technical": {
        "rsi": "RSI",
        "sma20": "SMA20",
        "sma50": "SMA50",
        "sma200": "SMA200",
        "high_52w": "52W High",
        "low_52w": "52W Low",
        "beta": "Beta",
        "price": "Price",
    },
}

# Mapped fields available in NEITHER the truncated quote grid NOR any screener view
# (verified against all six views 2026-07-04: recom/target_price are analyst-only
# quote-grid fields; short_interest (absolute shares) and earnings (next date) have
# no screener column either — only short_float/short_ratio survive via `ownership`).
UPSTREAM_UNRECOVERABLE = ("earnings", "recom", "short_interest", "target_price")


class FzError(RuntimeError):
    """Non-transient ``fz`` failure (binary missing, non-zero exit, bad JSON)."""


class FzNotFoundError(FzError):
    """``fz`` returned exit code 3 — ticker not found."""


# ---------- fz invocation (isolated so tests can inject a fake runner) -------


def _fz_binary() -> str | None:
    """Resolve the ``fz`` binary path: ``$FZ_PP_CLI`` override else PATH."""
    override = os.environ.get("FZ_PP_CLI", "").strip()
    if override:
        return override if os.path.exists(override) else None
    return shutil.which("fz")


def _run_fz_quote(ticker: str, binary: str) -> object:
    """Run ``fz quote <T> --agent`` and return parsed JSON. Raises typed errors.

    ``--agent`` expands to ``--json --compact --no-input --no-color --yes``.
    """
    try:
        proc = subprocess.run(  # noqa: S603 - fixed argv, no shell
            [binary, "quote", ticker, "--agent"],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:  # pragma: no cover - env path
        raise FzError(f"fz invocation failed: {exc}") from exc

    if proc.returncode == 3:
        raise FzNotFoundError(f"ticker {ticker} not found (fz exit 3)")
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "").strip()[:200]
        raise FzError(f"fz exit {proc.returncode}: {detail}")
    try:
        return json.loads(proc.stdout)
    except (ValueError, json.JSONDecodeError) as exc:
        raise FzError(f"fz returned non-JSON output: {exc}") from exc


def _run_fz_screen(ticker: str, binary: str, view: str) -> list:
    """Run ``fz screen --tickers <T> --view <view> --agent`` -> list of row dicts.

    The screener payload is a JSON array of label-keyed rows (one per ticker).
    Raises the same typed errors as the quote runner; the caller treats every
    failure as a silent skip (the fallback never blocks enrichment).
    """
    try:
        proc = subprocess.run(  # noqa: S603 - fixed argv, no shell
            [binary, "screen", "--tickers", ticker, "--view", view, "--agent"],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:  # pragma: no cover - env path
        raise FzError(f"fz screen invocation failed: {exc}") from exc

    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "").strip()[:200]
        raise FzError(f"fz screen exit {proc.returncode}: {detail}")
    try:
        rows = json.loads(proc.stdout)
    except (ValueError, json.JSONDecodeError) as exc:
        raise FzError(f"fz screen returned non-JSON output: {exc}") from exc
    return rows if isinstance(rows, list) else []


# ---------- pure parsers -----------------------------------------------------


def parse_pct(raw: object) -> float | None:
    """'0.92%' -> 0.92 ; '-1.93%' -> -1.93 ; '-'/None -> None."""
    if not isinstance(raw, str):
        return None
    s = raw.strip().rstrip("%").strip()
    if s in ("", "-", "N/A"):
        return None
    try:
        return float(s)
    except ValueError:
        return None


def parse_num(raw: object) -> float | None:
    """'3.05' -> 3.05 ; '-' -> None. The first whitespace-token is parsed so
    composite Finviz cells like '311.82 -0.31%' yield the leading number."""
    if not isinstance(raw, str):
        return float(raw) if isinstance(raw, (int, float)) else None
    s = raw.strip().split()[0] if raw.strip() else ""
    if s in ("", "-", "N/A"):
        return None
    try:
        return float(s)
    except ValueError:
        return None


_SUFFIX = {"K": 1e3, "M": 1e6, "B": 1e9, "T": 1e12}


def parse_human(raw: object) -> float | None:
    """'14.67B' -> 14_670_000_000 ; '134.68M' -> 134_680_000 ; '-' -> None."""
    if not isinstance(raw, str):
        return None
    s = raw.strip()
    if s in ("", "-", "N/A"):
        return None
    mult = 1.0
    if s[-1].upper() in _SUFFIX:
        mult = _SUFFIX[s[-1].upper()]
        s = s[:-1]
    try:
        return float(s) * mult
    except ValueError:
        return None


# ---------- transforms -------------------------------------------------------


def extract_fields(resp: object) -> dict:
    """Project the gate-relevant raw Finviz strings out of an ``fz quote`` payload."""
    fundamentals = resp.get("fundamentals", {}) if isinstance(resp, dict) else {}
    if not isinstance(fundamentals, dict):
        fundamentals = {}
    out: dict = {}
    for out_key, label in _FIELD_MAP.items():
        val = fundamentals.get(label)
        if isinstance(val, str) and val.strip() not in ("", "-"):
            out[out_key] = val.strip()
    return out


def derive(fields: dict) -> dict:
    """Direction-agnostic derived block: parsed numerics + squeeze + target gap."""
    short_float = parse_pct(fields.get("short_float"))
    days_to_cover = parse_num(fields.get("short_ratio"))
    float_shares = parse_human(fields.get("shs_float"))
    price = parse_num(fields.get("price"))
    target = parse_num(fields.get("target_price"))

    if short_float is not None and days_to_cover is not None:
        if short_float >= SQUEEZE_SHORT_FLOAT_PCT and days_to_cover >= SQUEEZE_DAYS_TO_COVER:
            squeeze = "HIGH"
        elif short_float >= SQUEEZE_SHORT_FLOAT_PCT / 2:
            # squeeze potential is driven by the % of float short; a low short
            # float can't squeeze regardless of days-to-cover.
            squeeze = "MODERATE"
        else:
            squeeze = "LOW"
    else:
        squeeze = "unknown"

    upside_to_target_pct = None
    if price is not None and target is not None and price > 0:
        upside_to_target_pct = round((target - price) / price * 100, 2)

    return {
        "short_float_pct": short_float,
        "days_to_cover": days_to_cover,
        "float_shares": float_shares,
        "squeeze_pressure": squeeze,
        "recom": parse_num(fields.get("recom")),
        "upside_to_target_pct": upside_to_target_pct,
        "rsi": parse_num(fields.get("rsi")),
    }


def screen_fallback_fields(
    ticker: str, binary: str, missing_keys: set, screen_runner=_run_fz_screen
) -> dict:
    """Recover missing mapped fields from the screener views (quote-grid fallback).

    Pure gap-fill: only keys in ``missing_keys`` are pulled; each view is queried at
    most once and only when it can still contribute. Any screener failure or empty
    result is a silent skip — the fallback never blocks enrichment.
    """
    out: dict = {}
    for view, fmap in _SCREEN_VIEW_FIELD_MAP.items():
        wanted = {k: lbl for k, lbl in fmap.items() if k in missing_keys and k not in out}
        if not wanted:
            continue
        try:
            rows = screen_runner(ticker, binary, view)
        except FzError:
            continue
        row = next(
            (r for r in rows if isinstance(r, dict) and str(r.get("Ticker", "")).upper() == ticker),
            None,
        )
        if row is None:
            continue
        for key, label in wanted.items():
            val = row.get(label)
            if isinstance(val, str) and val.strip() not in ("", "-"):
                out[key] = val.strip()
    return out


# ---------- orchestration ----------------------------------------------------


def enrich(
    ticker: str,
    as_of: str,
    runner=_run_fz_quote,
    binary: str = "fz",
    screen_runner=_run_fz_screen,
) -> dict:
    """Fetch one ticker via ``fz`` and assemble the enrichment payload.

    Quote first; any mapped field the (upstream-truncated) quote grid lacks is
    backfilled from the screener ownership/technical views. Quote values win.
    ``screen_fallback_used`` lists the backfilled keys; ``upstream_gaps`` lists
    mapped fields recoverable from no fz surface (today: recom / target_price).
    """
    sym = ticker.upper()
    resp = runner(sym, binary)
    quote_fields = extract_fields(resp)
    missing = {k for k in _FIELD_MAP if k not in quote_fields}
    fallback = screen_fallback_fields(sym, binary, missing, screen_runner=screen_runner) if missing else {}
    fields = {**fallback, **quote_fields}  # quote wins on any overlap
    return {
        "ticker": sym,
        "as_of": as_of,
        "source": "finviz",
        "available": True,
        "fz_available": True,
        "fields": fields,
        "derived": derive(fields),
        "screen_fallback_used": sorted(fallback.keys()),
        "upstream_gaps": sorted(k for k in UPSTREAM_UNRECOVERABLE if k not in fields),
        "freshness_caveat": FRESHNESS_CAVEAT,
    }


def _skip(ticker: str, as_of: str, reason: str) -> dict:
    return {
        "ticker": ticker.upper(),
        "as_of": as_of,
        "source": "finviz",
        "available": False,
        "fz_available": False,
        "skip_reason": reason,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Finviz (fz CLI) enrichment as JSON")
    parser.add_argument("--ticker", required=True)
    parser.add_argument("--date", required=True, help="As-of date YYYY-MM-DD (freshness tag)")
    args = parser.parse_args()

    try:
        datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        print(json.dumps(_skip(args.ticker, args.date, f"invalid --date {args.date!r}, expected YYYY-MM-DD")))
        return

    binary = _fz_binary()
    if not binary:
        print(json.dumps(_skip(args.ticker, args.date, "fz CLI not found (set $FZ_PP_CLI or install finviz-pp-cli)")))
        return

    try:
        print(json.dumps(enrich(args.ticker, args.date, binary=binary)))
    except FzNotFoundError as exc:
        print(json.dumps(_skip(args.ticker, args.date, str(exc))))
    except FzError as exc:
        print(json.dumps(_skip(args.ticker, args.date, str(exc))))


if __name__ == "__main__":
    main()
