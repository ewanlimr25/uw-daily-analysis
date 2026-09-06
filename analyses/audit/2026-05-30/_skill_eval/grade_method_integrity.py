#!/usr/bin/env python3
"""Method-integrity eval for the calibration-audit C20-C25 upgrade.

Skill-creator variance frame: grade the EDITED skill (with_skill) vs the OLD
snapshot (old_skill baseline) against an objective assertion set describing the
C20-C25 capabilities + preserved invariants. Deterministic (regex over the file),
so it is a reusable, scriptable benchmark rather than an eyeball.

A capability assertion should PASS on the new file and FAIL on the old.
An invariant assertion should PASS on BOTH (we did not break propose-only or the
checkpoint contract).
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
NEW = HERE.parent.parent.parent.parent / ".claude/commands/calibration-audit.md"
OLD = HERE.parent / "_skill_snapshot/calibration-audit.md.orig"

def has(txt, *patterns):
    return all(re.search(p, txt, re.I | re.S) for p in patterns)

def not_has(txt, pattern):
    return re.search(pattern, txt, re.I | re.S) is None

# (id, kind, predicate(text)->bool, human text)
ASSERTIONS = [
    ("C20_daily_ohlc", "capability",
     lambda t: has(t, r"get_historical_stock_prices", r"true[- ]range", r"daily OHLC"),
     "Phase 2 resolves on daily OHLC via yahoo-finance + true-range ATR (C20)"),
    ("C20_kills_phantom_trend_spec", "capability",
     lambda t: has(t, r"uw historical trend.{0,80}NOT a price-window tool|not executable")
               and has(t, r"no `--date`"),
     "Phase 2 explicitly retires the non-executable `uw historical trend --date`/high-low spec (C20)"),
    ("C21_benchmark_excess", "capability",
     lambda t: has(t, r"benchmark[- ]excess", r"excess_winrate\.py:market_excess", r"SPY same-window"),
     "Phase 3 adds benchmark-excess (realised - SPY same-window) via excess_winrate.market_excess (C21)"),
    ("C21_calibrated_but_beta", "capability",
     lambda t: has(t, r"calibrated[- ]but[- ]beta"),
     "Phase 3 verdict has a (d) calibrated-but-beta section (C21)"),
    ("C22_no_lookahead", "capability",
     lambda t: has(t, r"look[- ]ahead", r"general_class_behaviour|general class behaviour"),
     "Phase 2/3 strips look-ahead: signal-backtest demoted from point-in-time benchmark (C22)"),
    ("C23_nfloor_8", "capability",
     lambda t: has(t, r"decided[- ]N\s*[≥>=]+\s*8|decided-N ≥ 8"),
     "Phase 3 raises the per-class floor to decided-N>=8 (C23)"),
    ("C23_benjamini_hochberg", "capability",
     lambda t: has(t, r"Benjamini[- ]?Hochberg"),
     "Multiple-hypothesis (Benjamini-Hochberg FDR) control added (C23)"),
    ("C23_provenance_cap", "capability",
     lambda t: has(t, r"reconstructed", r"cannot be rated P0|cannot be rated above P1"),
     "Phase 7 caps priority on reconstructed-citation findings (C23)"),
    ("C24_gate_effectiveness", "capability",
     lambda t: has(t, r"gate effectiveness|HELP, not just FIRE|veto_fp_rate"),
     "Phase 6 measures gate effectiveness + VETO false-positive rate (C24)"),
    ("C25_reliability_logloss", "capability",
     lambda t: has(t, r"reliability diagram|reliability deciles", r"log[- ]loss"),
     "Phase 3 adds reliability diagram + log-loss beside Brier (C25)"),
    ("sizingmap_070_quarter", "capability",
     lambda t: has(t, r"0\.70\s*→\s*full|≥\s*0\.70", r"quarter"),
     "Phase 6 sizing-map corrected to >=0.70 full and the `quarter` bucket mapped (false-positive fix)"),
    # ---- invariants: must hold on BOTH new and old ----
    ("inv_propose_only", "invariant",
     lambda t: has(t, r"propose[- ]only") and has(t, r"Never call `Edit` or `Write`"),
     "INVARIANT: propose-only — never Edit/Write outside the audit dir"),
    ("inv_checkpoint_contract", "invariant",
     lambda t: has(t, r"phase_<N>_") and has(t, r"resume"),
     "INVARIANT: resumable per-phase checkpoint contract preserved"),
    ("inv_seven_phases", "invariant",
     lambda t: all(has(t, rf"## Phase {n} ") for n in range(1, 8)),
     "INVARIANT: all 7 phases still present"),
]

def grade(path):
    txt = path.read_text()
    out = []
    for aid, kind, pred, human in ASSERTIONS:
        try:
            passed = bool(pred(txt))
        except Exception as e:
            passed = False
            human += f" [pred error: {e}]"
        out.append({"text": human, "id": aid, "kind": kind, "passed": passed,
                    "evidence": ""})
    return out

new_g = grade(NEW)
old_g = grade(OLD)

def rate(g):
    return sum(a["passed"] for a in g) / len(g)

# Expected: capability assertions pass on NEW, fail on OLD; invariants pass on both.
cap_ids = [a[0] for a in ASSERTIONS if a[1] == "capability"]
inv_ids = [a[0] for a in ASSERTIONS if a[1] == "invariant"]
def subset_rate(g, ids):
    s = [a for a in g if a["id"] in ids]
    return sum(a["passed"] for a in s) / len(s)

bench = {
    "skill_name": "calibration-audit",
    "iteration": 1,
    "configs": {
        "with_skill (edited C20-C25)": {
            "overall_pass_rate": round(rate(new_g), 3),
            "capability_pass_rate": round(subset_rate(new_g, cap_ids), 3),
            "invariant_pass_rate": round(subset_rate(new_g, inv_ids), 3),
        },
        "old_skill (snapshot baseline)": {
            "overall_pass_rate": round(rate(old_g), 3),
            "capability_pass_rate": round(subset_rate(old_g, cap_ids), 3),
            "invariant_pass_rate": round(subset_rate(old_g, inv_ids), 3),
        },
    },
    "capability_delta_pp": round((subset_rate(new_g, cap_ids) - subset_rate(old_g, cap_ids)) * 100, 1),
    "new_detail": new_g,
    "old_detail": old_g,
}
(HERE / "benchmark.json").write_text(json.dumps(bench, indent=2))

# console report
print(f"NEW  overall {rate(new_g):.0%}  | capability {subset_rate(new_g,cap_ids):.0%} | invariant {subset_rate(new_g,inv_ids):.0%}")
print(f"OLD  overall {rate(old_g):.0%}  | capability {subset_rate(old_g,cap_ids):.0%} | invariant {subset_rate(old_g,inv_ids):.0%}")
print(f"capability delta: +{bench['capability_delta_pp']}pp (new - old)\n")
print("per-assertion (NEW / OLD):")
for n, o in zip(new_g, old_g):
    flag = "" if (n["kind"]=="capability" and n["passed"] and not o["passed"]) or \
                 (n["kind"]=="invariant" and n["passed"] and o["passed"]) else "  <-- UNEXPECTED"
    print(f"  [{ 'PASS' if n['passed'] else 'fail'} / {'PASS' if o['passed'] else 'fail'}] {n['kind']:10} {n['id']}{flag}")

# exit non-zero if any capability failed on NEW or any invariant broke on NEW
bad = [a for a in new_g if (a["kind"]=="capability" and not a["passed"]) or (a["kind"]=="invariant" and not a["passed"])]
sys.exit(1 if bad else 0)
