#!/usr/bin/env python3
"""Phase 6b — grade the 2026-08-01 P0 intervention (SHORT direction -> watch_only).

The rule was applied to .claude/agents/risk-monitor.md on 2026-08-01 (uncommitted at
audit time). Envelopes dated >= 2026-08-03 are the first post-intervention cohort.
Compliance test: every call with direction == "short" must carry final_size ==
"watch_only" (routing, NOT suppression -- so the short theses must still be PRESENT).

Two failure modes are distinguished:
  * VIOLATION      -- a short call sized above watch_only (rule not applied)
  * SUPPRESSION    -- short theses vanished entirely (rule mis-applied as a ban)
"""
import json

AUDIT = "analyses/audit/2026-08-30"
P0_DATE = "2026-08-03"          # first envelope authored under the new rule
rows = [json.loads(l) for l in open(f"{AUDIT}/phase_1_inventory.jsonl")]

post = [r for r in rows if r["report_date"] >= P0_DATE]
pre = [r for r in rows if r["report_date"] < P0_DATE]

print(f"POST-P0 cohort ({P0_DATE}+): {len(post)} rows from "
      f"{len(set(r['report_date'] for r in post))} envelopes")
print(f"PRE-P0 corpus: {len(pre)} rows\n")

# --- 1. Is the short lane still emitting? (suppression check) -------------------
def share(rs, pred):
    return (sum(1 for r in rs if pred(r)), len(rs))

for label, rs in (("PRE ", pre), ("POST", post)):
    n_short, n = share(rs, lambda r: r["direction"] == "short")
    n_long, _ = share(rs, lambda r: r["direction"] == "long")
    print(f"{label} short rows: {n_short}/{n} ({100*n_short/n:.1f}%) | "
          f"long rows: {n_long}/{n} ({100*n_long/n:.1f}%)")

# --- 2. Routing compliance on post-P0 shorts -----------------------------------
print("\n--- POST-P0 SHORT ROUTING ---")
post_shorts = [r for r in post if r["direction"] == "short"]
sizes = {}
for r in post_shorts:
    sizes[r["final_size"]] = sizes.get(r["final_size"], 0) + 1
print(f"n post-P0 short calls: {len(post_shorts)}")
print("final_size distribution:", dict(sorted(sizes.items(), key=lambda kv: -kv[1])))

SIZED = {"full", "half", "quarter", "starter"}
violations = [r for r in post_shorts if r["final_size"] in SIZED]
print(f"VIOLATIONS (short sized above watch_only): {len(violations)}")
for r in violations:
    print(f"   !! {r['report_date']} {r['ticker']} tier={r['tier']} "
          f"size={r['final_size']} score={r['raw_score']}")

# section routing too (the rule speaks of watch_only routing)
secs = {}
for r in post_shorts:
    secs[r["section"]] = secs.get(r["section"], 0) + 1
print("section distribution:", dict(sorted(secs.items(), key=lambda kv: -kv[1])))

# --- 3. Counterfactual preservation: are shorts still scored/gated? -------------
scored = sum(1 for r in post_shorts if r["raw_score"] is not None)
gated = sum(1 for r in post_shorts if r["gate_verdicts"])
classed = sum(1 for r in post_shorts if r["dominant_signal_class"])
print(f"\nCOUNTERFACTUAL PRESERVATION: raw_score present {scored}/{len(post_shorts)}, "
      f"gate_verdicts present {gated}/{len(post_shorts)}, "
      f"signal_class present {classed}/{len(post_shorts)}")

# --- 4. What the pre-P0 corpus would have routed --------------------------------
pre_shorts_sized = [r for r in pre if r["direction"] == "short" and r["final_size"] in SIZED]
print(f"\nPRE-P0 shorts that WERE sized (the behavior the rule removes): "
      f"{len(pre_shorts_sized)}")
for r in pre_shorts_sized[:20]:
    print(f"   {r['report_date']} {r['ticker']} {r['final_size']} tier={r['tier']}")

# --- 5. Per-envelope post-P0 board shape ---------------------------------------
print("\n--- POST-P0 BOARD BY DATE ---")
by_date = {}
for r in post:
    by_date.setdefault(r["report_date"], []).append(r)
for d in sorted(by_date):
    rs = by_date[d]
    sized = [r for r in rs if r["final_size"] in SIZED]
    shorts = [r for r in rs if r["direction"] == "short"]
    print(f"  {d}: {len(rs):3d} rows | sized {len(sized)} "
          f"({','.join(sorted(set(r['ticker']+':'+r['final_size'] for r in sized))) or '-'}) "
          f"| shorts {len(shorts)} | regime={rs[0]['regime_bucket']}")

json.dump({"post_p0_rows": len(post), "post_p0_shorts": len(post_shorts),
           "violations": len(violations), "scored": scored, "gated": gated},
          open(f"{AUDIT}/phase_6b_p0_compliance.json", "w"), indent=2)
