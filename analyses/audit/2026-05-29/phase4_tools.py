#!/usr/bin/env python3
"""Phase 4 — tool attribution. Class-conditional marginal contribution per uw tool."""
import json, collections, statistics
from pathlib import Path
import importlib.util
spec = importlib.util.spec_from_file_location("p3", "analyses/audit/2026-05-29/phase3_calibration.py")
p3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p3)
canon = p3.canon

AUDIT = Path("analyses/audit/2026-05-29")
WIN, LOSS = "WIN", "LOSS"

def wr(rows):
    d = [r for r in rows if r["outcome"] in (WIN, LOSS)]
    if not d: return None, 0
    return sum(1 for r in d if r["outcome"]==WIN)/len(d), len(d)

def main():
    rows = [json.loads(l) for l in open(AUDIT / "phase_2_outcomes.jsonl")]
    dec = [r for r in rows if r["outcome"] in (WIN, LOSS)]
    for r in dec:
        r["_cls"] = canon(r.get("dominant_signal_class"))

    # all tools
    tool_rows = collections.defaultdict(list)
    for r in dec:
        for t in (r.get("tools_cited") or []):
            tool_rows[t].append(r)

    results = []
    for tool, trows in sorted(tool_rows.items(), key=lambda kv:-len(kv[1])):
        n_with = len(trows)
        if n_with < 5:
            results.append({"tool": tool, "n_with": n_with, "tier": "INSUFFICIENT_N"})
            continue
        # class-conditional marginal contribution
        classes = set(r["_cls"] for r in trows if r["_cls"])
        diffs = []  # (class, diff, class_n)
        win_on_winners = 0; total_win = 0; total_loss = 0; fires_on_loss = 0
        for c in classes:
            cls_all = [r for r in dec if r["_cls"]==c]
            with_c = [r for r in cls_all if tool in (r.get("tools_cited") or [])]
            without_c = [r for r in cls_all if tool not in (r.get("tools_cited") or [])]
            w_with, n1 = wr(with_c); w_without, n2 = wr(without_c)
            if w_with is not None and w_without is not None and n1>=3 and n2>=3:
                diffs.append((c, (w_with-w_without), n1))
        # confounded check: fires on winners vs losers (overall)
        wins = [r for r in dec if r["outcome"]==WIN]
        losses = [r for r in dec if r["outcome"]==LOSS]
        frac_win = sum(1 for r in wins if tool in (r.get("tools_cited") or []))/len(wins) if wins else 0
        frac_loss = sum(1 for r in losses if tool in (r.get("tools_cited") or []))/len(losses) if losses else 0
        if diffs:
            tot = sum(d[2] for d in diffs)
            mc = sum(d[1]*d[2] for d in diffs)/tot if tot else None
        else:
            # fall back to unconditional
            w_with,_ = wr(trows); w_without,_ = wr([r for r in dec if tool not in (r.get("tools_cited") or [])])
            mc = (w_with-w_without) if (w_with is not None and w_without is not None) else None
        # tier
        if mc is None:
            tier = "UNSCORABLE"
        elif frac_win>=0.80 and frac_loss<=0.30:
            tier = "CONFOUNDED"
        elif mc >= 0.10:
            tier = "LOAD-BEARING"
        elif mc >= 0.03:
            tier = "SUPPORTIVE"
        elif mc <= -0.05:
            tier = "NEGATIVE"
        elif abs(mc) <= 0.02:
            tier = "NO-INFO"
        else:
            tier = "SUPPORTIVE" if mc>0 else "NO-INFO"
        results.append({"tool": tool, "n_with": n_with, "mc_pp": round(mc*100,1) if mc is not None else None,
                        "frac_on_win": round(frac_win,2), "frac_on_loss": round(frac_loss,2),
                        "n_classes": len(diffs), "tier": tier,
                        "self_wr": round(wr(trows)[0],3) if wr(trows)[0] is not None else None})

    # fz advisory dims (envelope only)
    fz = {"squeeze_pressure_C15": 0, "float_C16": 0, "analyst_div_C17": 0, "breadth_C18": 0}
    env = [r for r in dec if r.get("source")=="envelope"]
    fz_have = sum(1 for r in env if r.get("fz_context"))
    breadth_have = sum(1 for r in dec if r.get("breadth_cross_check"))

    out = {"tool_table": results, "fz_advisory": {
        "envelope_decided": len(env), "rows_with_fz_context": fz_have,
        "rows_with_breadth": breadth_have,
        "verdict": "INSUFFICIENT_N — all fz/C15-C18 axes below the N>=5 decided floor (envelope reports are too recent; most are window_open). Stay advisory (0 points)."}}
    json.dump(out, open(AUDIT/"phase_4_tools.jsonl","w"), indent=1)
    # print
    print(f"{'TOOL':52} {'N':>4} {'MC_pp':>6} {'win%':>5} {'lose%':>5} {'#cls':>4}  TIER")
    for r in results:
        print(f"{r['tool'][:52]:52} {r['n_with']:>4} {str(r.get('mc_pp')):>6} "
              f"{str(r.get('frac_on_win','')):>5} {str(r.get('frac_on_loss','')):>5} {str(r.get('n_classes','')):>4}  {r['tier']}")
    print("\nfz advisory:", json.dumps(out["fz_advisory"]))

if __name__ == "__main__":
    main()
