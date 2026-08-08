#!/usr/bin/env python3
"""Validate a decision-envelope JSON file against the repo schema.

Two layers:
  1. A minimal stdlib JSON-Schema check (type / enum / const / required /
     additionalProperties / items / $ref / pattern) against
     ``schemas/decision_envelope.schema.json`` — no ``jsonschema`` dependency.
  2. Cross-field invariants JSON Schema can't express:
       - Σ score_components.points == raw_score   (the quant's own rule)
       - tier must not exceed the band implied by raw_score (demotion is OK)
       - fundamentals_verdict == VETO ⇒ final_size ∈ {veto, skip, watch_only}

Usage:
    python3 scripts/validate_decision.py --file analyses/daily/2026-05-23/decision.json
Exit 0 = valid, 1 = invalid (errors printed), 2 = usage error.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schemas" / "decision_envelope.schema.json"

# raw_score bands → highest tier the score alone justifies (lower tiers always OK).
# HIGH band ≥ 9 (2026-05-30 register P1.3; validator synced by the 2026-06-06 audit
# P1.1 — the stale ≥10 band forced raw-9 calls to be recorded MEDIUM, mis-bucketing
# every downstream tier table: the suppressed raw-9 cohort went 3/4 while the
# recorded-HIGH (≥10) envelope calls went 1/5).
_TIER_RANK = {"DROP": 0, "LOW": 1, "MEDIUM": 2, "HIGH": 3}

# 2026-06-12 audit P1.1: gate-output discipline, mechanically enforced.
# The schema had silently REJECTED the `debate` key (additionalProperties: false
# without it) — the debate gate verdict was recorded on 0 of 151 envelope calls
# ever. On schema >= 1.3 every non-DROP call must carry all nine gate verdicts
# (no-op is a verdict; absence is a missed gate).
_REQUIRED_GATE_KEYS = (
    "regime", "vrp", "panic", "cluster", "sector",
    "fundamentals", "event_risk", "debate", "rubric_regime",
)
_GATE_COMPLETENESS_VERSIONS = ("1.3",)

# 2026-06-12 audit P2.5: schema >= 1.3 must carry the rubric-freeze era stamp
# (rubric_version), else /calibration-audit cannot stratify calls by rubric era.
_RUBRIC_VERSION_REQUIRED_VERSIONS = ("1.3",)

# 2026-06-12 audit P2.5 (P1/F5 dead-letter finding): the regime-conflict and
# correlation-cluster lines are risk-monitor TIER gates applied in Step 2d — they
# are NOT score_components and must never re-enter the score carrying nonzero points.
# A score_components entry whose rubric_line matches one of these signatures AND
# carries points != 0 is rejected. (A points==0 documentation entry is allowed.)
_DEAD_LETTER_LINE_PATTERNS = (
    "market-regime conflict",
    "market regime conflict",
    "regime conflicts with trade",
    "regime conflicts with direction",
    "market-regime conflicts with",
    "correlation cluster",
    "corr-cluster",
)


def _band_max_tier(raw_score: int) -> int:
    if raw_score >= 9:
        return _TIER_RANK["HIGH"]
    if raw_score >= 7:
        return _TIER_RANK["MEDIUM"]
    if raw_score >= 3:
        return _TIER_RANK["LOW"]
    return _TIER_RANK["DROP"]


# ---------- minimal JSON-Schema engine --------------------------------------


_TYPE_CHECKS = {
    "object": lambda v: isinstance(v, dict),
    "array": lambda v: isinstance(v, list),
    "string": lambda v: isinstance(v, str),
    "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
    "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
    "boolean": lambda v: isinstance(v, bool),
    "null": lambda v: v is None,
}


def _check_type(value, type_spec) -> bool:
    types = type_spec if isinstance(type_spec, list) else [type_spec]
    return any(_TYPE_CHECKS[t](value) for t in types)


def _resolve_ref(ref: str, root: dict):
    node = root
    for part in ref.lstrip("#/").split("/"):
        if part:
            node = node[part]
    return node


def _validate(value, schema: dict, root: dict, path: str, errors: list[str]) -> None:
    if "$ref" in schema:
        schema = _resolve_ref(schema["$ref"], root)

    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: expected const {schema['const']!r}, got {value!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} not in enum {schema['enum']}")
    if "type" in schema and not _check_type(value, schema["type"]):
        errors.append(f"{path}: expected type {schema['type']}, got {type(value).__name__}")
        return
    if "pattern" in schema and isinstance(value, str) and not re.search(schema["pattern"], value):
        errors.append(f"{path}: {value!r} does not match pattern {schema['pattern']}")

    if isinstance(value, dict) and ("properties" in schema or "required" in schema):
        for req in schema.get("required", []):
            if req not in value:
                errors.append(f"{path}: missing required key {req!r}")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in props:
                    errors.append(f"{path}: unexpected key {key!r}")
        for key, subval in value.items():
            if key in props:
                _validate(subval, props[key], root, f"{path}.{key}", errors)

    if isinstance(value, list) and "items" in schema:
        for i, item in enumerate(value):
            _validate(item, schema["items"], root, f"{path}[{i}]", errors)


# ---------- cross-field invariants ------------------------------------------


def check_invariants(doc: dict) -> list[str]:
    errors: list[str] = []
    enforce_gates = (
        isinstance(doc, dict) and doc.get("schema_version") in _GATE_COMPLETENESS_VERSIONS
    )

    # P2.5: rubric_version era stamp required on schema >= 1.3.
    if isinstance(doc, dict) and doc.get("schema_version") in _RUBRIC_VERSION_REQUIRED_VERSIONS:
        rv = doc.get("rubric_version")
        if not isinstance(rv, str) or not rv.strip():
            errors.append(
                f"$: rubric_version is required and must be a non-empty string on "
                f"schema_version {doc.get('schema_version')} (got {rv!r}) — the freeze era stamp"
            )

    for i, call in enumerate(doc.get("calls", []) if isinstance(doc, dict) else []):
        if not isinstance(call, dict):
            continue
        cp = f"calls[{i}] ({call.get('ticker', '?')})"

        # P1.1 gate-verdict completeness (schema >= 1.3, non-DROP calls only).
        if enforce_gates and call.get("tier") != "DROP":
            gv = call.get("gate_verdicts")
            if not isinstance(gv, dict):
                errors.append(f"{cp}: gate_verdicts missing on non-DROP call (schema >= 1.3 requires all 9 gate verdicts)")
            else:
                missing = [k for k in _REQUIRED_GATE_KEYS if k not in gv]
                if missing:
                    errors.append(f"{cp}: gate_verdicts missing required key(s) {missing} (no-op is a verdict; absence is a missed gate)")

        comps = call.get("score_components")
        raw = call.get("raw_score")
        if isinstance(comps, list) and isinstance(raw, int):
            total = sum(c.get("points", 0) for c in comps if isinstance(c, dict))
            if total != raw:
                errors.append(f"{cp}: Σ score_components.points ({total}) != raw_score ({raw})")

        # P2.5: dead-letter tier-gate lines must not re-enter the score with points.
        if isinstance(comps, list):
            for j, c in enumerate(comps):
                if not isinstance(c, dict):
                    continue
                line = str(c.get("rubric_line", "")).lower()
                pts = c.get("points", 0)
                if isinstance(pts, (int, float)) and pts != 0 and any(p in line for p in _DEAD_LETTER_LINE_PATTERNS):
                    errors.append(
                        f"{cp}: score_components[{j}] is a dead-letter TIER GATE "
                        f"(regime-conflict / correlation-cluster) carrying {pts} points — "
                        f"these are risk-monitor 2d tier gates, never score_components "
                        f"(rubric_line={c.get('rubric_line')!r})"
                    )

        tier = call.get("tier")
        if isinstance(raw, int) and tier in _TIER_RANK:
            if _TIER_RANK[tier] > _band_max_tier(raw):
                errors.append(f"{cp}: tier {tier} exceeds band for raw_score {raw}")

        if call.get("fundamentals_verdict") == "VETO":
            if call.get("final_size") not in ("veto", "skip", "watch_only"):
                errors.append(
                    f"{cp}: fundamentals_verdict VETO but final_size is "
                    f"{call.get('final_size')!r} (must be veto/skip/watch_only)"
                )

        # C3: capped half-Kelly is floored at 0 and is a fraction in [0, 1].
        kf = call.get("kelly_fraction")
        if isinstance(kf, (int, float)) and not isinstance(kf, bool):
            if kf < 0 or kf > 1:
                errors.append(f"{cp}: kelly_fraction {kf} out of [0, 1] (capped half-Kelly is floored at 0)")
    return errors


# 2026-07-25 audit P1 #5: the instrumentation trio is schema-present (C43, 2026-06-20)
# and mandatory-when-source-present per the agent contracts — but it was never added to
# the orchestrator's calls[] enumeration, so envelopes from 2026-07-20 on dropped the
# keys entirely and C16 / C18 have been untestable for three consecutive audits. These
# are WARNINGS, not errors: a missing key must be visible at emission time without
# retroactively invalidating the 52 historical envelopes the audit reads as its dataset.
def _load_canonical_signal_classes() -> tuple[frozenset, dict]:
    """Read the canonical class list + alias map off the schema (single source of truth).

    Falls back to empty on any read failure so a schema-path problem can never turn
    into a spurious warning storm.
    """
    try:
        schema = json.loads(SCHEMA_PATH.read_text())
        prop = schema["$defs"]["call"]["properties"]["dominant_signal_class"]
        return (frozenset(prop.get("x-canonical-classes", [])),
                dict(prop.get("x-canonical-aliases", {})))
    except Exception:  # pragma: no cover - defensive
        return frozenset(), {}


_CANONICAL_SIGNAL_CLASSES, _CANONICAL_SIGNAL_ALIASES = _load_canonical_signal_classes()


def check_instrumentation_warnings(doc: dict) -> list[str]:
    """Non-fatal instrumentation gaps: keys that should be present-with-explicit-null.

    Returns warning strings. These never affect the exit code — the envelope is still
    valid — but they surface the silent-drop failure mode that made C16/C18 ungradeable.
    """
    warnings: list[str] = []
    for i, call in enumerate(doc.get("calls", []) if isinstance(doc, dict) else []):
        if not isinstance(call, dict):
            continue
        cp = f"calls[{i}] ({call.get('ticker', '?')})"
        cls = call.get("dominant_signal_class")
        section = call.get("section") or ""

        if cls == "dark_pool_accumulation" and "dp_block_to_float_ratio" not in call:
            warnings.append(
                f"{cp}: dark_pool_accumulation row missing 'dp_block_to_float_ratio' key "
                f"(explicit null is required when fz float is unavailable) — the C16 "
                f"float-normalized gate stays untestable without it"
            )
        if cls == "dark_pool_accumulation" and "insider_cluster_flag" not in call:
            warnings.append(
                f"{cp}: dark_pool_accumulation row missing 'insider_cluster_flag' key "
                f"(false = checked-and-absent, null = fz lane skipped) — the C18 "
                f"conjunction gate stays untestable without it"
            )
        if (cls in ("earnings_vol", "high_iv_rank") or "vol" in section) and "implied_move" not in call:
            warnings.append(
                f"{cp}: vol row missing 'implied_move' key — /calibration-audit can only "
                f"resolve this row on the RV-direction proxy, never true IV-vs-RV (C42)"
            )
        if call.get("tier") != "DROP" and "debate_residuals" not in call:
            warnings.append(
                f"{cp}: non-DROP call missing 'debate_residuals' — both {{bull, bear}} "
                f"scalars are mandatory for every debated name (2026-06-12 P1.1)"
            )

        # 2026-08-01 audit P2 #9: keep dominant_signal_class from fragmenting again.
        # Warning, never an error — a hard enum would fail-validate the historical
        # envelopes that ARE the calibration dataset.
        if isinstance(cls, str) and cls and cls not in _CANONICAL_SIGNAL_CLASSES:
            alias = _CANONICAL_SIGNAL_ALIASES.get(cls)
            hint = f" — emit '{alias}'" if alias else ""
            warnings.append(
                f"{cp}: dominant_signal_class {cls!r} is not canonical{hint} "
                f"(schema x-canonical-classes; off-list values force every audit to "
                f"re-implement a collapse before it can group anything)"
            )

        # 2026-08-01 audit item 5: the C16 field shipped and is emitted, but every value
        # was null because fz_enrich's screener row-match rejected the upstream
        # doubled-first-letter Ticker cell (MSFT -> MMSFT). That parse bug is fixed; this
        # warning catches a silent regression of the *value* rather than the key.
        # Scoped to calls whose own fz lane demonstrably RAN (fz_context.available is
        # true): an explicit null remains the correct, contract-mandated value on a
        # graceful fz skip, and must never warn — the hunt is never blocked on fz.
        fzc = call.get("fz_context")
        fz_ran = isinstance(fzc, dict) and fzc.get("available") is True
        if (cls == "dark_pool_accumulation" and fz_ran
                and "dp_block_to_float_ratio" in call
                and call.get("dp_block_to_float_ratio") is None):
            warnings.append(
                f"{cp}: dark_pool_accumulation row has dp_block_to_float_ratio=null "
                f"despite fz_context.available=true — expected a number now that the fz "
                f"float lookup is fixed (2026-08-01); persistent nulls here mean the C16 "
                f"float-normalized gate is still ungradeable"
            )
    return warnings


def validate_doc(doc: dict, schema: dict) -> list[str]:
    """Return a list of validation error strings ([] == valid)."""
    errors: list[str] = []
    _validate(doc, schema, schema, "$", errors)
    errors.extend(check_invariants(doc))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a decision-envelope JSON file")
    parser.add_argument("--file", required=True)
    parser.add_argument(
        "--no-warnings",
        action="store_true",
        help="suppress the non-fatal instrumentation-gap warnings (exit code is unaffected either way)",
    )
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"File not found: {args.file}", file=sys.stderr)
        return 2

    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON in {args.file}: {exc}", file=sys.stderr)
        return 1

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors = validate_doc(doc, schema)
    if errors:
        print(f"INVALID: {args.file}", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    n = len(doc.get("calls", []))
    print(f"OK: {args.file} validates ({n} call(s))")

    # Non-fatal instrumentation gaps (2026-07-25 P1 #5). Printed, never exit-code-bearing.
    if not args.no_warnings:
        warnings = check_instrumentation_warnings(doc)
        if warnings:
            print(f"WARNINGS ({len(warnings)}): instrumentation keys missing — the envelope "
                  f"is valid, but these gaps make gates ungradeable at the next audit", file=sys.stderr)
            for warn in warnings:
                print(f"  ! {warn}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
