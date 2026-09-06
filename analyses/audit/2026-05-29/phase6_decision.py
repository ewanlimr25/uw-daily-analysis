#!/usr/bin/env python3
"""Phase 6 — decision-process audit: quant + risk-monitor compliance."""
import json, collections
from pathlib import Path
AUDIT = Path("analyses/audit/2026-05-29")

def size_band(wr):
    if wr is None: return None
    if wr >= 0.65: return "full"
    if wr >= 0.50: return "half"
    return "starter_or_skip"

def main():
    rows=[json.loads(l) for l in open(AUDIT/"phase_1_inventory.jsonl")]
    # quant compliance: only rows with score_components
    comp_rows=[r for r in rows if r.get("score_components") and all(isinstance(c,dict) for c in r["score_components"])]
    str_comp_rows=[r for r in rows if r.get("score_components") and not all(isinstance(c,dict) for c in r["score_components"])]
    sum_ok=0; sum_bad=[]; named_ok=0; named_bad=0
    for r in comp_rows:
        pts=sum(c.get("points",0) for c in r["score_components"])
        if r.get("raw_score") is not None and pts==r["raw_score"]:
            sum_ok+=1
        elif r.get("raw_score") is not None:
            sum_bad.append((r["report_date"],r["ticker"],pts,r["raw_score"]))
        # named source
        allnamed=all((c.get("source_agent") or c.get("source")) and (c.get("source_tool") or c.get("tool")) for c in r["score_components"])
        if allnamed: named_ok+=1
        else: named_bad+=1
    # sizing-map compliance (envelope rows have win_rate + pre_risk_size)
    sm_rows=[r for r in rows if r.get("claimed_win_rate") is not None and r.get("pre_risk_size")]
    sm_ok=0; sm_violations=[]
    for r in sm_rows:
        want=size_band(r["claimed_win_rate"]); got=str(r["pre_risk_size"]).lower()
        ok = (want=="full" and got=="full") or (want=="half" and got in("half","full")) or \
             (want=="starter_or_skip" and got in("starter","skip","watch_only","half"))
        # be lenient: gates legitimately DOWNGRADE, so allow got<=want; flag only UPGRADES beyond band
        order={"skip":0,"watch_only":0,"starter":1,"half":2,"full":3}
        bandmax={"full":3,"half":2,"starter_or_skip":1}
        if order.get(got,9)<=bandmax.get(want,9):
            sm_ok+=1
        else:
            sm_violations.append((r["report_date"],r["ticker"],r["claimed_win_rate"],got,want))

    # risk-monitor gate firing (envelope rows w/ gate_verdicts)
    env=[r for r in rows if r.get("gate_verdicts")]
    gate_fire=collections.Counter(); gate_applicable=collections.Counter()
    for r in env:
        for g,v in r["gate_verdicts"].items():
            gate_applicable[g]+=1
            s=str(v).lower()
            if not (s.startswith("no-op") or s.startswith("confirm (0)") or s=="confirm" or s.startswith("na")):
                gate_fire[g]+=1
    # event_risk missed-gate ledger: envelope calls with macro_event_risk inside horizon but no event_risk gate fired
    missed=[]
    for r in env:
        mer=r.get("macro_event_risk")
        if mer and r.get("horizon") in ("swing","weekly"):
            ev=r["gate_verdicts"].get("event_risk","")
            if str(ev).lower().startswith("no-op") or not ev:
                # high-impact event present?
                hi=[e for e in mer if isinstance(e,dict) and e.get("impact")=="high"]
                if hi:
                    missed.append((r["report_date"],r["ticker"],hi[0].get("event"),hi[0].get("date")))

    out={
        "quant": {
            "rows_with_dict_components": len(comp_rows),
            "rows_with_string_components_skipped": len(str_comp_rows),
            "sum_eq_rawscore": sum_ok, "sum_mismatch": len(sum_bad),
            "sum_mismatch_examples": sum_bad[:10],
            "all_components_named": named_ok, "components_unnamed": named_bad,
            "compliance_rate": round(sum_ok/len(comp_rows),3) if comp_rows else None,
        },
        "sizing_map": {
            "rows": len(sm_rows), "compliant_or_downgraded": sm_ok,
            "upgrade_violations": len(sm_violations), "examples": sm_violations[:10],
            "compliance_rate": round(sm_ok/len(sm_rows),3) if sm_rows else None,
        },
        "risk_gates": {
            "envelope_rows": len(env),
            "gate_fire_rate": {g: f"{gate_fire[g]}/{gate_applicable[g]}" for g in gate_applicable},
            "event_risk_missed_ledger": missed,
        },
    }
    json.dump(out,open(AUDIT/"phase_6_decision_audit.jsonl","w"),indent=1)
    print(json.dumps(out,indent=1,default=str))

if __name__=="__main__":
    main()
