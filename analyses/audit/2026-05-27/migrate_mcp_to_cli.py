#!/usr/bin/env python3
"""Deterministic mcp__uw-pp__* -> `uw <group> <sub>` migration for .claude/ prose.

Driven by mcp-to-cli-mapping.tsv (the 61-row 1:1 table from the 2026-05-27 audit).
Two passes per file:
  Pass A: replace the prefixed token `mcp__uw-pp__<tool>` -> `uw <group> <sub>`.
  Pass B: replace the bare snake_case tool name `<tool>` -> `uw <group> <sub>`
          (word-bounded, longest-first so `..._sector_flow` doesn't clobber
           `..._sector_flow_persistence`).

`--apply` writes in place; default is a dry-run reporting per-file before/after counts.
Run from repo root.
"""
import argparse
import re
import sys
from pathlib import Path

AUDIT_DIR = Path(__file__).resolve().parent
REPO = AUDIT_DIR.parents[2]  # analyses/audit/2026-05-27 -> repo root
TSV = AUDIT_DIR / "mcp-to-cli-mapping.tsv"

# Bare tool names that are too generic / ambiguous to safely substring-replace
# in free prose. They are migrated only in their prefixed form (Pass A).
BARE_SKIP = set()


def load_mapping():
    """tool_name (no prefix) -> 'uw <group> <sub>'."""
    mapping = {}
    for line in TSV.read_text().splitlines()[1:]:
        if not line.strip():
            continue
        mcp_tool, cli_cmd, _flags = line.split("\t")
        tool = mcp_tool.removeprefix("mcp__uw-pp__")
        mapping[tool] = cli_cmd  # cli_cmd already 'uw <group> <sub>'
    return mapping


def migrate_text(text, mapping):
    counts = {"prefixed": 0, "bare": 0}
    # longest tool name first to avoid prefix-collision (sector_flow vs sector_flow_persistence)
    tools = sorted(mapping, key=len, reverse=True)

    # Pass A: prefixed token
    for tool in tools:
        token = "mcp__uw-pp__" + tool
        pat = re.compile(re.escape(token))
        text, n = pat.subn(mapping[tool], text)
        counts["prefixed"] += n

    # Pass B: bare snake_case tool name, word-bounded
    for tool in tools:
        if tool in BARE_SKIP:
            continue
        # (?<![\w-]) / (?![\w-]) keeps us off already-hyphenated CLI output and
        # off longer identifiers; tool names are pure [a-z_].
        pat = re.compile(r"(?<![\w-])" + re.escape(tool) + r"(?![\w-])")
        text, n = pat.subn(mapping[tool], text)
        counts["bare"] += n

    return text, counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes in place")
    ap.add_argument("paths", nargs="*", help="files to migrate (default: .claude commands+agents)")
    args = ap.parse_args()

    mapping = load_mapping()

    if args.paths:
        files = [Path(p).resolve() for p in args.paths]
    else:
        files = sorted((REPO / ".claude/commands").glob("*.md")) + \
                sorted((REPO / ".claude/agents").glob("*.md"))

    grand = {"prefixed": 0, "bare": 0}
    for f in files:
        text = f.read_text()
        new, counts = migrate_text(text, mapping)
        total = counts["prefixed"] + counts["bare"]
        try:
            label = f.relative_to(REPO)
        except ValueError:
            label = f
        if total:
            print(f"{label}: prefixed={counts['prefixed']} bare={counts['bare']} total={total}")
        grand["prefixed"] += counts["prefixed"]
        grand["bare"] += counts["bare"]
        if args.apply and new != text:
            f.write_text(new)

    print(f"\nTOTAL prefixed={grand['prefixed']} bare={grand['bare']} "
          f"sum={grand['prefixed'] + grand['bare']}  "
          f"({'APPLIED' if args.apply else 'DRY-RUN'})")


if __name__ == "__main__":
    main()
