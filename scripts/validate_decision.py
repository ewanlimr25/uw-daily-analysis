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
    python3 scripts/validate_decision.py --file analyses/2026-05-23.decision.json
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
_TIER_RANK = {"DROP": 0, "LOW": 1, "MEDIUM": 2, "HIGH": 3}


def _band_max_tier(raw_score: int) -> int:
    if raw_score >= 10:
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
    for i, call in enumerate(doc.get("calls", []) if isinstance(doc, dict) else []):
        if not isinstance(call, dict):
            continue
        cp = f"calls[{i}] ({call.get('ticker', '?')})"

        comps = call.get("score_components")
        raw = call.get("raw_score")
        if isinstance(comps, list) and isinstance(raw, int):
            total = sum(c.get("points", 0) for c in comps if isinstance(c, dict))
            if total != raw:
                errors.append(f"{cp}: Σ score_components.points ({total}) != raw_score ({raw})")

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
    return errors


def validate_doc(doc: dict, schema: dict) -> list[str]:
    """Return a list of validation error strings ([] == valid)."""
    errors: list[str] = []
    _validate(doc, schema, schema, "$", errors)
    errors.extend(check_invariants(doc))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a decision-envelope JSON file")
    parser.add_argument("--file", required=True)
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
    return 0


if __name__ == "__main__":
    sys.exit(main())
