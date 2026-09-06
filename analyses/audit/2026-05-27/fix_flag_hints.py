#!/usr/bin/env python3
"""Context-anchored arg-name corrections (audit cli-migration-audit.md §3).

Line-scoped so the legitimate `dominant_signal_class` field is never touched:
  - lines naming `uw historical oi-trend`: lookback_days hints -> --days
  - lines naming `uw screener volume-vs-average`: min_ratio=N -> --min-volume-ratio N
  - the signal-backtest signal_class= hint (calibration) -> --signal-type
Leaves `uw insights institutional-accumulation` lookback hints alone — that param
does not exist on the tool (pre-existing latent bug, documented in anomalies).
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
        if "uw historical oi-trend" in new:
            # lookback_days=5 / lookback_days≥5 / lookback_days ≥ 5  ->  --days …
            new = re.sub(r"lookback_days\s*=\s*(\d+)", r"--days \1", new)
            new = re.sub(r"lookback_days\s*(≥|>=)\s*(\d+)", r"--days \1 \2", new)
            new = re.sub(r"lookback ≥ (\d+) days", r"--days ≥ \1", new)
        if "uw screener volume-vs-average" in new:
            new = re.sub(r"min_ratio\s*=\s*(\d+)", r"--min-volume-ratio \1", new)
        if "uw historical signal-backtest" in new:
            new = re.sub(r"signal_class\s*=\s*dominant_signal_class",
                         "--signal-type <dominant_signal_class>", new)
        if new != ln:
            lines[i] = new
            changed += 1
    if changed:
        f.write_text("".join(lines))
        print(f"{f}: {changed} flag-hint fixes")
        total += changed

print(f"\nTOTAL flag-hint fixes: {total}")
