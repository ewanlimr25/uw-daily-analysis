#!/usr/bin/env python3
"""Discipline-integrity eval for the Deliverable C subject edits (C28/C31/C34).

The critical risk for C is NOT 'did the feature land' but 'did it land WITHOUT
activating an unvalidated edge into live scoring'. So each capability assertion is
paired with a discipline assertion (advisory / 0-points / does-not-change-sizing /
never-in-score_components). Deterministic regex over the edited files.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent
CMD = ROOT / ".claude/commands"
AG = ROOT / ".claude/agents"
SCHEMA = ROOT / "schemas/decision_envelope.schema.json"

def rd(p): return p.read_text()
def has(t, *ps): return all(re.search(p, t, re.I | re.S) for p in ps)

daily, weekly = rd(CMD / "daily-analysis.md"), rd(CMD / "weekly-analysis.md")
accum, fund = rd(AG / "accumulation-hunter.md"), rd(AG / "fundamentals-gate.md")
schema = rd(SCHEMA)

CHECKS = [
    # C28 capability + discipline
    ("C28_accum_detector", lambda: has(accum, r"oi decrease-with-volume", r"distribution_flag", r"closing_side"),
     "accumulation-hunter wires `uw oi decrease-with-volume` -> distribution_flag (C28)"),
    ("C28_accum_advisory", lambda: has(accum, r"0 rubric points|0 points", r"0 tier impact|never enters `score_components`|does not lower the\s*accumulation"),
     "C28 in accumulation-hunter is fenced advisory: 0 points / 0 tier impact / not in score_components"),
    ("C28_fund_advisory", lambda: has(fund, r"distribution", r"does NOT.{0,40}tier_adjustment|advisory"),
     "fundamentals-gate uses distribution_flag as advisory corroboration, no tier_adjustment change (C28)"),
    ("C28_schema_field", lambda: has(schema, r'"distribution_flag"', r'"present"', r'"closing_side"'),
     "schema defines distribution_flag advisory block (C28)"),
    ("C28_schema_zero_points", lambda: has(schema, r"distribution_flag.{0,600}0 to raw_score AND 0 to tier_adjustment|distribution_flag.{0,600}never enters score_components"),
     "schema documents distribution_flag as structurally 0-points (C28)"),
    ("C28_daily_envelope_not_scored", lambda: has(daily, r"distribution_flag", r"not.{0,30}`score_components`|0 points, 0 tier impact"),
     "daily envelope carries distribution_flag explicitly OUT of score_components (C28)"),
    ("C28_weekly_envelope", lambda: has(weekly, r"distribution_flag", r"0 points, 0 tier impact|never a `score_components`"),
     "weekly envelope carries distribution_flag advisory (C28)"),
    # C31 capability + discipline
    ("C31_daily_expectancy", lambda: has(daily, r"Expectancy lens", r"payoff ratio", r"not a sizing input|display-only"),
     "daily §7 surfaces per-tier expectancy/payoff as display-only, not a sizing input (C31)"),
    ("C31_weekly_expectancy", lambda: has(weekly, r"Expectancy lens", r"Display-only|display-only", r"win-rate ladder"),
     "weekly §8 surfaces expectancy lens, live sizer stays win-rate ladder (C31)"),
    ("C31_kelly_stays_advisory", lambda: has(daily, r"C3 frac|fractional-Kelly|Kelly sizer stays ADVISORY|Kelly.{0,40}ADVISORY"),
     "C31 explicitly keeps the C3 Kelly sizer ADVISORY (no live-flip)"),
    # C34 capability
    ("C34_daily_invalidation", lambda: has(daily, r"dark-pool price-levels", r"[Ii]nvalidation"),
     "daily §3 anchors invalidation to dark-pool price-levels (C34)"),
    ("C34_weekly_invalidation", lambda: has(weekly, r"dark-pool price-levels", r"[Ii]nvalidation|shelf"),
     "weekly §3 anchors invalidation to dark-pool price-levels (C34)"),
    # schema version bump + backward-compat intent
    ("schema_version_1_2", lambda: has(schema, r'"enum":\s*\[\s*"1.0",\s*"1.1",\s*"1.2"\s*\]'),
     "schema_version enum bumped to include 1.2 (1.0/1.1 retained = backward-compatible)"),
    ("daily_emits_1_2", lambda: has(daily, r'schema_version:\s*"1.2"'),
     "daily command emits schema_version 1.2"),
    ("weekly_emits_1_2", lambda: has(weekly, r'schema_version:\s*"1.2"'),
     "weekly command emits schema_version 1.2"),
]

results = []
for cid, pred, human in CHECKS:
    try:
        ok = bool(pred())
    except Exception as e:
        ok, human = False, human + f" [err {e}]"
    results.append({"text": human, "id": cid, "passed": ok, "evidence": ""})

passed = sum(r["passed"] for r in results)
bench = {"skill_name": "daily/weekly subject edits (C28/C31/C34)",
         "pass_rate": round(passed / len(results), 3),
         "passed": passed, "total": len(results), "detail": results}
(Path(__file__).resolve().parent / "benchmark_subject.json").write_text(json.dumps(bench, indent=2))

print(f"Subject discipline eval: {passed}/{len(results)} ({bench['pass_rate']:.0%})\n")
for r in results:
    print(f"  [{'PASS' if r['passed'] else 'FAIL'}] {r['id']}: {r['text']}")
sys.exit(0 if passed == len(results) else 1)
