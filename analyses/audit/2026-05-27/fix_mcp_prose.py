#!/usr/bin/env python3
"""Update residual prose mentions of the 'MCP' data layer to the 'uw' CLI.

Only touches data-path phrases. Leaves `mcp__yahoo-finance__*` and the
`mcp__uw-pp__*` permission wildcard alone (they contain no standalone 'MCP'
word and none of the phrase patterns below match them).
Run from repo root.
"""
import re
from pathlib import Path

# Ordered: longer/more-specific phrases first.
SUBS = [
    (r"backing UW MCP tools", "backing UW `uw` CLI tools"),
    (r"MCP-tool tier list", "CLI-tool tier list"),
    (r"MCP tool tier movements", "CLI tool tier movements"),
    (r"the MCP tools cited", "the `uw` CLI tools cited"),
    (r"each MCP tool cited", "each `uw` CLI tool cited"),
    (r"explicit MCP tool list", "explicit `uw` CLI command list"),
    (r"pulled fresh from MCP tools", "pulled fresh via the `uw` CLI"),
    (r"fresh MCP queries", "fresh `uw` CLI queries"),
    (r"wherever the MCP supports it", "wherever the CLI supports it"),
    (r"the date passed to every MCP tool", "the date passed to every `uw` call"),
    (r"added MCP calls", "added `uw` calls"),
    (r"Cap MCP calls", "Cap `uw` calls"),
    (r"Phase 2 MCP rate-limit hit", "Phase 2 data-fetch failure"),
    (r"When the MCP returns", "When the CLI returns"),
    (r"the MCP returns `", "the CLI returns `"),
    (r"extra MCP calls", "extra `uw` calls"),
]

files = sorted((Path(".claude/commands")).glob("*.md")) + \
        sorted((Path(".claude/agents")).glob("*.md"))

total = 0
for f in files:
    text = f.read_text()
    orig = text
    n_file = 0
    for pat, repl in SUBS:
        text, n = re.subn(pat, repl, text)
        n_file += n
    if n_file:
        f.write_text(text)
        print(f"{f}: {n_file} prose fixes")
        total += n_file

print(f"\nTOTAL prose fixes: {total}")
