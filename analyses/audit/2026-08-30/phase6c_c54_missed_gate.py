#!/usr/bin/env python3
"""Phase 6c — C54 missed-gate decomposition + live-rubric compliance.

C54 (2026-07-25): the missed-gate RATE is computed over non-DROP rows only.
DROP names are eliminated before the full risk stack runs -- that is the fleet's
intended early-exit optimization, and counting it as non-compliance measures
efficiency as drift. The DROP figure stays visible on its own line so a genuine
future drift confined to DROP rows is not masked.

Also grades compliance against the LIVE rubric only (rows authored under a rule
that actually existed at their report_date) -- the `debate` stage post-dates many
early envelopes, and the [0.55,0.65)->starter floor post-dates 2026-07-25.
"""
import json
from collections import defaultdict

AUDIT = "analyses/audit/2026-08-30"
GATES = ["regime", "vrp", "panic", "cluster", "sector", "fundamentals",
         "event_risk", "debate", "rubric_regime"]
# date each gate became a serialized obligation (before this, absence != drift)
GATE_LIVE_FROM = {
    "regime": "2026-05-25", "vrp": "2026-05-25", "panic": "2026-05-25",
    "cluster": "2026-05-25", "sector": "2026-05-25",
    "fundamentals": "2026-05-25", "event_risk": "2026-05-25",
    "debate": "2026-06-12",        # debate stage serialized from the freeze
    "rubric_regime": "2026-06-12",  # P0.6 half-cap introduced at the freeze
}
TIERS = ["HIGH", "MEDIUM", "LOW", "DROP"]

rows = [json.loads(l) for l in open(f"{AUDIT}/phase_2_outcomes.jsonl")]
# scored directional rows only -- the population the gate stack is obliged to run on
pop = [r for r in rows if r.get("raw_score") is not None]

out = {}
print("=== C54 MISSED-GATE DECOMPOSITION (scored rows; DROP excluded from headline) ===")
print(f"{'gate':14} {'HIGH':>9} {'MEDIUM':>9} {'LOW':>9} | {'NON-DROP':>12} | {'DROP':>12}")
for g in GATES:
    live = [r for r in pop if r["report_date"] >= GATE_LIVE_FROM[g]]
    per_tier = {}
    for t in TIERS:
        sub = [r for r in live if r.get("tier") == t]
        miss = sum(1 for r in sub if g not in (r.get("gate_verdicts") or {}))
        per_tier[t] = {"missed": miss, "n": len(sub),
                       "rate": round(miss / len(sub), 4) if sub else None}
    nd = [r for r in live if r.get("tier") != "DROP"]
    nd_miss = sum(1 for r in nd if g not in (r.get("gate_verdicts") or {}))
    nd_rate = nd_miss / len(nd) if nd else None
    dr = per_tier["DROP"]
    cells = " ".join(
        f"{per_tier[t]['missed']:>3}/{per_tier[t]['n']:<5}" for t in ("HIGH", "MEDIUM", "LOW"))
    hdr = f"{nd_miss:>3}/{len(nd):<4}={nd_rate:.3f}" if nd else "n/a"
    drs = f"{dr['missed']:>3}/{dr['n']:<4}={dr['rate']:.3f}" if dr["n"] else "n/a"
    drift = "  <-- DRIFT" if (nd_rate is not None and nd_rate > 0.20) else ""
    print(f"{g:14} {cells} | {hdr:>12} | {drs:>12}{drift}")
    out[g] = {"live_from": GATE_LIVE_FROM[g], "per_tier": per_tier,
              "non_drop_missed": nd_miss, "non_drop_n": len(nd),
              "non_drop_rate": round(nd_rate, 4) if nd_rate is not None else None,
              "drift_flag": bool(nd_rate is not None and nd_rate > 0.20)}

print("\n=== HEADLINE (C54) ===")
tot_m = sum(v["non_drop_missed"] for v in out.values())
tot_n = sum(v["non_drop_n"] for v in out.values())
print(f"non-DROP missed gates across all nine: {tot_m}/{tot_n} = {tot_m/tot_n:.4f}")
drifting = [g for g, v in out.items() if v["drift_flag"]]
print(f"gates exceeding the 20% non-DROP drift threshold: {drifting or 'NONE'}")
naive = sum(sum(1 for r in pop if g not in (r.get('gate_verdicts') or {})) for g in GATES)
print(f"(DROP-inclusive naive aggregate, for contrast: "
      f"{naive}/{len(pop)*len(GATES)} = {naive/(len(pop)*len(GATES)):.4f} "
      f"-- this is the figure C54 forbids as a drift headline)")

# --- post-P0 cohort compliance (the 2026-08-01 intervention window) --------------
print("\n=== POST-P0 COHORT (2026-08-03+) GATE COVERAGE ===")
post = [r for r in pop if r["report_date"] >= "2026-08-03"]
for g in GATES:
    miss = sum(1 for r in post if g not in (r.get("gate_verdicts") or {}))
    print(f"  {g:14} {miss}/{len(post)} missing")

json.dump(out, open(f"{AUDIT}/phase_6_missed_gate_c54.jsonl", "w"), indent=1)
print("\nwrote phase_6_missed_gate_c54.jsonl")
