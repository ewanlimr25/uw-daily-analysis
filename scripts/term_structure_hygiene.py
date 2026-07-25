#!/usr/bin/env python3
"""IV term-structure substrate hygiene — re-derive shape after dropping unusable tenors.

Stdlib-only. On 2026-07-24 raw ``uw options-structure iv-term-structure`` returned
**BACKWARDATION on 39 of 41 scanned names** — a mechanically near-constant label. Re-deriving the
shape after dropping (a) the same-day/expired bucket and (b) tenors too thin to trade **flipped 14
of those 41 to CONTANGO**. The raw label was dominated by 0DTE wing noise: a Friday snapshot puts
`dte_approx = 0` in the first bucket with average IV of 250-480%, which inverts any front-vs-back
comparison regardless of what the real curve does.

Two filters, both necessary and independently motivated:

1. **Drop the 0DTE/expired bucket.** ``front-end-iv-ratio`` at its default ``--near-dte 1`` snaps to
   ``near_dte_actual = 0`` on an expiry day and returns ratios of 2.3-8.7 that say nothing about
   event premium. Every Friday run is affected. Re-read at ``--near-dte 7`` (``NEAR_DTE_DEFAULT``).
2. **Drop tenors below a contract floor.** A tenor quoted off 1-8 contracts is not a price. This
   floor was introduced ad hoc by ``earnings-scout`` on 2026-07-24 (killing EEFT/WK/SNEX/ADNT, whose
   *underlyings* clear the C12 stock-level floor fine) and is exposed here as
   ``MIN_CONTRACTS_DEFAULT`` — a **named, overridable parameter, NOT a frozen constant**. It has not
   been through a pre-registered audit, so it must stay visible and tunable rather than hard-coded.

The distinction this module makes explicit and the raw label cannot: **"FLAT because no near-dated
tenor exists" is not calm.** The RMBS class (2026-07-24: WHR, DIOD, LDOS, COHU) has no listed tenor
under ~28 DTE, so a front-end ratio of exactly 1.000 means *unmeasurable*, not *quiet*. That is
returned as ``NO_NEAR_TENOR``, never as ``FLAT``.

Consumed by ``vol-surface-scout`` (primary classifier) and ``earnings-scout`` (kink-at-the-event
check) — both of which independently re-implemented this logic in the same 2026-07-24 run.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from typing import Sequence

# --- tunable parameters (NOT audit-frozen; see module docstring) ---
MIN_CONTRACTS_DEFAULT = 15  # a tenor quoted off fewer open contracts is not a tradable price
MIN_DTE_DEFAULT = 1         # drop same-day/expired buckets (dte 0) outright
NEAR_DTE_DEFAULT = 7        # tenor used as "front" for the hygiene-adjusted front-end ratio
BACK_DTE_DEFAULT = 30       # tenor used as "back" for the same ratio

# No surviving tenor at/under this DTE => the front is UNMEASURABLE (RMBS class), never "FLAT".
# 2026-07-24 evidence: WHR's first surviving tenor is 28 DTE with earnings 3 days out, so a
# min-DTE test against BACK_DTE alone (30) failed to catch it.
NEAR_TENOR_MAX_DTE = 21

# Relative IV gap (front vs next surviving tenor) needed to call a slope rather than FLAT.
FLAT_BAND_PCT = 2.0
# A mid-curve tenor must exceed BOTH neighbours by this much (relative %) to be a genuine kink.
KINK_MIN_PROMINENCE_PCT = 5.0
# Event kinks are near-dated by nature (an earnings/catalyst hump inside ~2 months). Beyond this
# the curve is sawtooth noise across thin tenors: SOXX 2026-07-24 showed a 7.8%-prominent "kink" at
# 84 DTE built on 460 contracts sitting between 501- and 42-contract neighbours. Scanning the whole
# 875-day curve for the single most prominent bump finds that noise instead of the event.
KINK_MAX_DTE = 60

SHAPE_BACKWARDATION = "BACKWARDATION"
SHAPE_CONTANGO = "CONTANGO"
SHAPE_FLAT = "FLAT"
SHAPE_KINKED = "KINKED"
SHAPE_NO_NEAR_TENOR = "NO_NEAR_TENOR"
SHAPE_INSUFFICIENT = "INSUFFICIENT_DATA"


@dataclass(frozen=True)
class Tenor:
    """One surviving expiry bucket on the curve."""

    dte: int
    iv: float
    # None = the payload carried no contract count at all (distinct from a measured 0).
    contracts: int | None
    expiry: str | None = None

    def to_dict(self) -> dict:
        return {"expiry": self.expiry, "dte": self.dte, "iv": round(self.iv, 4),
                "contracts": self.contracts}


@dataclass(frozen=True)
class Hygiene:
    """Re-derived term structure for one ticker."""

    ticker: str
    raw_shape: str | None
    shape: str
    # Monotonic slope read, kept ALONGSIDE `shape` — a curve can be a contango base with an
    # earnings kink, and neither label alone describes it.
    base_shape: str | None = None
    tenors: tuple[Tenor, ...] = field(default_factory=tuple)
    dropped: tuple[dict, ...] = field(default_factory=tuple)
    flipped: bool = False
    base_flipped: bool = False
    front_end_ratio: float | None = None
    front_end_ratio_tenors: tuple[int, int] | None = None
    kink_dte: int | None = None
    kink_expiry: str | None = None
    kink_prominence_pct: float | None = None
    kink_candidates: tuple[dict, ...] = field(default_factory=tuple)
    slope_front_next_pct: float | None = None
    note: str | None = None

    def to_dict(self) -> dict:
        return {
            "ticker": self.ticker,
            "raw_shape": self.raw_shape,
            "shape": self.shape,
            "base_shape": self.base_shape,
            "flipped": self.flipped,
            "base_flipped": self.base_flipped,
            "n_tenors_kept": len(self.tenors),
            "n_tenors_dropped": len(self.dropped),
            "tenors": [t.to_dict() for t in self.tenors],
            "dropped": list(self.dropped),
            "front_end_ratio": (
                round(self.front_end_ratio, 3) if self.front_end_ratio is not None else None
            ),
            "front_end_ratio_tenors": (
                list(self.front_end_ratio_tenors) if self.front_end_ratio_tenors else None
            ),
            "kink_dte": self.kink_dte,
            "kink_expiry": self.kink_expiry,
            "kink_prominence_pct": (
                round(self.kink_prominence_pct, 1) if self.kink_prominence_pct is not None else None
            ),
            "kink_candidates": list(self.kink_candidates),
            "slope_front_next_pct": (
                round(self.slope_front_next_pct, 1)
                if self.slope_front_next_pct is not None
                else None
            ),
            "note": self.note,
        }


def _first_present(row: dict, keys: Sequence[str]):
    """First key whose value is not None.

    NOT ``row.get(a, row.get(b))``: Python evaluates that default eagerly, so a row carrying the
    primary key with an explicit ``null`` (``{"dte": None, "dte_approx": 7}``) never consults the
    fallback. For ``contracts`` the downstream ``or 0.0`` then turned "field absent" into a measured
    zero and reported ``contracts 0 < 15 (untradable)`` — conflating missing data with a real
    liquidity finding, which is the exact key-guessing failure class this module exists to remove.
    """
    for k in keys:
        v = row.get(k)
        if v is not None:
            return v
    return None


def _num(v) -> float | None:
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    return f if f == f else None  # reject NaN


def extract_tenors(payload: dict) -> list[dict]:
    """Pull the per-expiry rows out of an ``iv-term-structure`` payload.

    The rows live under one of several keys across CLI versions; each candidate key is tried in
    order rather than assumed, because guessing a response key silently produced an all-zero parse
    during the 2026-07-24 run.
    """
    for key in ("term_structure", "expiries", "tenors", "curve", "results", "data"):
        rows = (payload or {}).get(key)
        if isinstance(rows, list) and rows:
            return [r for r in rows if isinstance(r, dict)]
    return []


def normalize_tenors(rows: Sequence[dict]) -> list[Tenor]:
    """Coerce raw rows to ``Tenor`` objects sorted by DTE ascending. Unparseable rows are dropped."""
    out: list[Tenor] = []
    for r in rows:
        dte = _num(_first_present(r, ("dte", "dte_approx", "days_to_expiry")))
        iv = _num(_first_present(r, ("avg_iv", "iv", "implied_volatility")))
        raw_contracts = _first_present(r, ("contracts", "contract_count", "n_contracts"))
        if dte is None or iv is None or iv <= 0:
            continue
        # A genuinely absent contract count is NOT a measured zero; treat it as unknown so the
        # drop_reason says so instead of claiming an untradable tenor.
        contracts = _num(raw_contracts)
        out.append(
            Tenor(
                dte=int(dte),
                iv=iv,
                contracts=int(contracts) if contracts is not None else None,
                expiry=r.get("expiry"),
            )
        )
    return sorted(out, key=lambda t: t.dte)


def _rel_pct(a: float, b: float) -> float:
    """Percent by which ``a`` exceeds ``b``."""
    return 100.0 * (a / b - 1.0) if b else 0.0


def base_shape(tenors: Sequence[Tenor], flat_band_pct: float = FLAT_BAND_PCT) -> tuple[str, float | None]:
    """Monotonic front-vs-next slope, IGNORING any kink. Returns ``(shape, slope_pct)``.

    Reported alongside the kink-aware ``shape`` rather than being replaced by it: on 2026-07-24 the
    mega-caps (AAPL 3d 21.2% -> 5d 25.6% -> 7d 40.9% -> 10d 36.2% -> ... -> 147d 30.5%) are
    simultaneously a contango base AND an earnings hump at the 7 DTE event tenor. Collapsing that to
    one label loses information whichever label wins, so both are emitted.
    """
    if len(tenors) < 2:
        return SHAPE_INSUFFICIENT, None
    slope = _rel_pct(tenors[0].iv, tenors[1].iv)
    if abs(slope) < flat_band_pct:
        return SHAPE_FLAT, slope
    return (SHAPE_BACKWARDATION if slope > 0 else SHAPE_CONTANGO), slope


def find_kink(
    tenors: Sequence[Tenor],
    kink_prominence_pct: float = KINK_MIN_PROMINENCE_PCT,
    kink_max_dte: int = KINK_MAX_DTE,
) -> tuple[Tenor | None, float | None, list[dict]]:
    """Find the NEAREST interior local-max tenor inside the event window.

    Returns ``(tenor, prominence_pct, candidates)``. "Nearest" not "most prominent": an event kink
    is defined positionally by a known catalyst date, so the earliest qualifying hump is the one
    that can be matched to a print. Ranking by prominence instead picked SOXX's 84 DTE sawtooth over
    its real 28 DTE OPEX-cluster hump. ``candidates`` lists every interior local max in the window
    (including sub-threshold ones) so near-misses stay visible instead of vanishing.
    """
    candidates: list[dict] = []
    hit: tuple[Tenor, float] | None = None
    for i in range(1, len(tenors) - 1):
        prev, cur, nxt = tenors[i - 1], tenors[i], tenors[i + 1]
        if cur.dte > kink_max_dte or not (cur.iv > prev.iv and cur.iv > nxt.iv):
            continue
        prom = min(_rel_pct(cur.iv, prev.iv), _rel_pct(cur.iv, nxt.iv))
        candidates.append(
            {
                "dte": cur.dte,
                "expiry": cur.expiry,
                "prominence_pct": round(prom, 1),
                "qualifies": prom >= kink_prominence_pct,
            }
        )
        if prom >= kink_prominence_pct and hit is None:
            hit = (cur, prom)
    return (hit[0] if hit else None), (hit[1] if hit else None), candidates


def classify(
    tenors: Sequence[Tenor],
    flat_band_pct: float = FLAT_BAND_PCT,
    kink_prominence_pct: float = KINK_MIN_PROMINENCE_PCT,
    kink_max_dte: int = KINK_MAX_DTE,
) -> tuple[str, dict]:
    """Classify the surviving curve. Returns ``(shape, detail)``.

    KINKED takes the headline when a qualifying event hump exists, but ``detail`` always carries the
    ``base_shape`` slope read so the monotonic classification is never lost.
    """
    if len(tenors) < 2:
        return SHAPE_INSUFFICIENT, {"base_shape": SHAPE_INSUFFICIENT}

    base, slope = base_shape(tenors, flat_band_pct)
    tenor, prom, candidates = find_kink(tenors, kink_prominence_pct, kink_max_dte)
    detail = {
        "base_shape": base,
        "slope_front_next_pct": slope,
        "kink_candidates": candidates,
    }
    if tenor is not None:
        detail.update(
            {"kink_dte": tenor.dte, "kink_expiry": tenor.expiry, "kink_prominence_pct": prom}
        )
        return SHAPE_KINKED, detail
    return base, detail


def front_end_ratio(
    tenors: Sequence[Tenor], near_dte: int = NEAR_DTE_DEFAULT, back_dte: int = BACK_DTE_DEFAULT
) -> tuple[float | None, tuple[int, int] | None]:
    """Hygiene-adjusted front-end IV ratio: IV at ~``near_dte`` over IV at ~``back_dte``.

    Picks the surviving tenor nearest each target. Returns ``(None, None)`` when the same tenor
    would serve both legs — a ratio of exactly 1.000 from a degenerate pairing is the artifact this
    module exists to expose, not a reading.
    """
    if len(tenors) < 2:
        return None, None
    near = min(tenors, key=lambda t: abs(t.dte - near_dte))
    back = min(tenors, key=lambda t: abs(t.dte - back_dte))
    if near.dte == back.dte or not back.iv:
        return None, None
    return near.iv / back.iv, (near.dte, back.dte)


def apply(
    ticker: str,
    payload: dict | Sequence[dict],
    raw_shape: str | None = None,
    min_contracts: int = MIN_CONTRACTS_DEFAULT,
    min_dte: int = MIN_DTE_DEFAULT,
    near_dte: int = NEAR_DTE_DEFAULT,
    back_dte: int = BACK_DTE_DEFAULT,
    near_tenor_max_dte: int = NEAR_TENOR_MAX_DTE,
    flat_band_pct: float = FLAT_BAND_PCT,
    kink_prominence_pct: float = KINK_MIN_PROMINENCE_PCT,
    kink_max_dte: int = KINK_MAX_DTE,
) -> Hygiene:
    """Run both filters and re-derive the shape. Never raises."""
    if isinstance(payload, dict):
        raw_shape = raw_shape or payload.get("term_structure_type") or payload.get("structure")
        rows = extract_tenors(payload)
    else:
        rows = [r for r in (payload or []) if isinstance(r, dict)]

    all_tenors = normalize_tenors(rows)
    kept: list[Tenor] = []
    dropped: list[dict] = []
    for t in all_tenors:
        if t.dte < min_dte:
            dropped.append({**t.to_dict(), "drop_reason": f"dte {t.dte} < {min_dte} (0DTE/expired)"})
        elif t.contracts is None:
            dropped.append(
                {**t.to_dict(), "drop_reason": "contract count absent from payload (unknown, not zero)"}
            )
        elif t.contracts < min_contracts:
            dropped.append(
                {**t.to_dict(), "drop_reason": f"contracts {t.contracts} < {min_contracts} (untradable)"}
            )
        else:
            kept.append(t)

    # No surviving tenor near the front => unmeasurable, explicitly NOT "calm".
    nearest = min((t.dte for t in kept), default=None)
    if nearest is not None and nearest > near_tenor_max_dte:
        return Hygiene(
            ticker=ticker,
            raw_shape=raw_shape,
            shape=SHAPE_NO_NEAR_TENOR,
            tenors=tuple(kept),
            dropped=tuple(dropped),
            flipped=raw_shape is not None and raw_shape != SHAPE_NO_NEAR_TENOR,
            note=(
                f"nearest surviving tenor is {nearest} DTE (> {near_tenor_max_dte}) — the front end is "
                "UNMEASURABLE, not FLAT (RMBS class); do not read a 1.000 ratio as calm"
            ),
        )

    shape, detail = classify(kept, flat_band_pct, kink_prominence_pct, kink_max_dte)
    ratio, ratio_tenors = front_end_ratio(kept, near_dte, back_dte)
    return Hygiene(
        ticker=ticker,
        raw_shape=raw_shape,
        shape=shape,
        base_shape=detail.get("base_shape"),
        tenors=tuple(kept),
        dropped=tuple(dropped),
        flipped=bool(raw_shape) and shape != raw_shape and shape != SHAPE_INSUFFICIENT,
        base_flipped=bool(raw_shape)
        and detail.get("base_shape") not in (raw_shape, SHAPE_INSUFFICIENT, None),
        front_end_ratio=ratio,
        front_end_ratio_tenors=ratio_tenors,
        kink_dte=detail.get("kink_dte"),
        kink_expiry=detail.get("kink_expiry"),
        kink_prominence_pct=detail.get("kink_prominence_pct"),
        kink_candidates=tuple(detail.get("kink_candidates") or ()),
        slope_front_next_pct=detail.get("slope_front_next_pct"),
        note=None if kept else "no tenor survived the hygiene filters",
    )


def build_report(payloads: dict, **kw) -> dict:
    """Apply hygiene to ``{ticker: payload}``. Reports how many labels the filters flipped."""
    results = [apply(t, p, **kw).to_dict() for t, p in (payloads or {}).items()]
    flipped = [r["ticker"] for r in results if r["flipped"]]
    return {
        "available": True,
        "params": {
            "min_contracts": kw.get("min_contracts", MIN_CONTRACTS_DEFAULT),
            "min_dte": kw.get("min_dte", MIN_DTE_DEFAULT),
            "near_dte": kw.get("near_dte", NEAR_DTE_DEFAULT),
            "back_dte": kw.get("back_dte", BACK_DTE_DEFAULT),
            "near_tenor_max_dte": kw.get("near_tenor_max_dte", NEAR_TENOR_MAX_DTE),
            "kink_max_dte": kw.get("kink_max_dte", KINK_MAX_DTE),
            "kink_prominence_pct": kw.get("kink_prominence_pct", KINK_MIN_PROMINENCE_PCT),
            "min_contracts_is_audit_frozen": False,
        },
        "n_tickers": len(results),
        "n_flipped": len(flipped),
        "flipped": flipped,
        "base_flipped": [r["ticker"] for r in results if r["base_flipped"]],
        "shape_counts": {
            s: sum(1 for r in results if r["shape"] == s) for s in sorted({r["shape"] for r in results})
        },
        "base_shape_counts": {
            s: sum(1 for r in results if r["base_shape"] == s)
            for s in sorted({r["base_shape"] for r in results if r["base_shape"]})
        },
        "results": results,
    }


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument(
        "--file",
        required=True,
        help="JSON {ticker: <iv-term-structure payload>} or JSONL with one such object per line",
    )
    p.add_argument("--min-contracts", type=int, default=MIN_CONTRACTS_DEFAULT)
    p.add_argument("--min-dte", type=int, default=MIN_DTE_DEFAULT)
    p.add_argument("--near-dte", type=int, default=NEAR_DTE_DEFAULT)
    p.add_argument("--back-dte", type=int, default=BACK_DTE_DEFAULT)
    p.add_argument("--near-tenor-max-dte", type=int, default=NEAR_TENOR_MAX_DTE)
    p.add_argument("--kink-max-dte", type=int, default=KINK_MAX_DTE)
    p.add_argument("--kink-prominence-pct", type=float, default=KINK_MIN_PROMINENCE_PCT)
    args = p.parse_args(argv)

    try:
        with open(args.file, encoding="utf-8") as fh:
            payloads = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"available": False, "error": str(exc)[:200], "results": []}, indent=2))
        return 0

    if not isinstance(payloads, dict):
        print(json.dumps({"available": False, "error": "expected a {ticker: payload} object",
                          "results": []}, indent=2))
        return 0

    print(
        json.dumps(
            build_report(
                payloads,
                min_contracts=args.min_contracts,
                min_dte=args.min_dte,
                near_dte=args.near_dte,
                back_dte=args.back_dte,
                near_tenor_max_dte=args.near_tenor_max_dte,
                kink_max_dte=args.kink_max_dte,
                kink_prominence_pct=args.kink_prominence_pct,
            ),
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
