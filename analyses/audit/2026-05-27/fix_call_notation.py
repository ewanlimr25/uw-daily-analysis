#!/usr/bin/env python3
"""Flatten residual MCP function-call notation `uw <grp> <sub>(args)` to real CLI
flags, and correct per-tool lookback flag names (audit §3 + §4).

Per-tool flag truth (from mcp-to-cli-mapping.tsv):
  historical trend / cumulative-premium-flow / gex-time-series : --days
  historical iv-percentile-zscore / pc-ratio-zscore            : --lookback-days
  insights institutional-accumulation                          : NO lookback param
                                                                 (fiction -> '<N>-day window')
  watchlist manage                                             : --action / --group / --tickers
Line-anchored so the decision-envelope field `dominant_signal_class` etc. are untouched.
Run from repo root.
"""
import re
from pathlib import Path

files = sorted(Path(".claude/commands").glob("*.md")) + \
        sorted(Path(".claude/agents").glob("*.md"))

total = 0
for f in files:
    lines = f.read_text().splitlines(keepends=True)
    changed = 0
    for i, ln in enumerate(lines):
        new = ln

        # --- watchlist manage function-call -> flags ---
        if "uw watchlist manage(" in new:
            new = re.sub(
                r'uw watchlist manage\(action="add", group="([^"]+)"(?:, tickers=\[<top_5_by_score>\])?\)',
                r"uw watchlist manage --action add --group \1 --tickers <top_5_by_score>",
                new,
            )
            new = re.sub(r'uw watchlist manage\(action="list",\s*\.\.\.\)',
                         "uw watchlist manage --action list", new)

        # --- historical trend ---
        if "uw historical trend" in new:
            new = re.sub(r"start_date\s*=\s*report_date", "--date <report_date>", new)
            new = re.sub(r"trend\(lookback_days\s*=\s*(\d+)\)", r"trend --days \1", new)
            new = re.sub(r"lookback_days\s*=\s*horizon_window", "--days <horizon_window>", new)
            new = re.sub(r"lookback_days\s*=\s*(\d+)", r"--days \1", new)

        # --- --days tools ---
        if "uw historical cumulative-premium-flow" in new or "uw historical gex-time-series" in new:
            new = re.sub(r"lookback_days\s*=\s*(\d+)", r"--days \1", new)

        # --- --lookback-days tools ---
        if "uw historical iv-percentile-zscore" in new or "uw historical pc-ratio-zscore" in new:
            new = re.sub(r"lookback_days\s*=\s*(\d+)", r"--lookback-days \1", new)

        # --- institutional-accumulation: no lookback param exists ---
        if "uw insights institutional-accumulation" in new:
            new = re.sub(r"`lookback_days\s*=\s*(\d+)`", r"a \1-day window", new)

        if new != ln:
            lines[i] = new
            changed += 1
    if changed:
        f.write_text("".join(lines))
        print(f"{f}: {changed} fixes")
        total += changed

print(f"\nTOTAL fixes: {total}")
