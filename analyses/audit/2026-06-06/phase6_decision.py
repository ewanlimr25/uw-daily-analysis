#!/usr/bin/env python3
"""Phase 6 (2026-05-30) — decision-process compliance + C24 gate-EFFECTIVENESS.
Compliance replicates 05-29 (same envelope data). NEW: gate downgrade-effectiveness,
VETO/CAUTION false-positive rate, debate-gate effectiveness — all on resolved outcomes
(thin: report advisory below 10 decided/gate; NEVER recommend loosening a gate on thin data)."""
import json, re
from collections import defaultdict, Counter

AUD = "analyses/audit/2026-06-06"
SIZE_ORDER = {"skip": 0, "starter": 1, "quarter": 2, "half": 3, "full": 4}

def size_from_wr(wr):
    if wr is None: return None
    if wr >= 0.70: return "full"
    if wr >= 0.50: return "half"
    return "starter"

def main():
    rows = [json.loads(l) for l in open(f"{AUD}/phase_2_outcomes.jsonl")]
    dec = lambda r: r["outcome"] in ("WIN", "LOSS")
    y = lambda r: 1 if r["outcome"] == "WIN" else 0

    # ---- 1. Sigma-points compliance ----
    struct = [r for r in rows if isinstance(r.get("score_components"), list) and r["score_components"]
              and isinstance(r["score_components"][0], dict)]
    ok_sum = 0
    for r in struct:
        pts = sum(c.get("points", 0) for c in r["score_components"])
        if r.get("raw_score") is not None and pts == r["raw_score"]:
            ok_sum += 1
    print(f"Sigma-points: {ok_sum}/{len(struct)} structured rows reconcile (== raw_score)")

    # ---- 2. Sizing-map compliance (allow gate downgrades; quarter in map) ----
    szrows = [r for r in rows if r.get("claimed_win_rate") is not None and r.get("pre_risk_size")]
    viol = []
    for r in szrows:
        exp = size_from_wr(r["claimed_win_rate"]); act = r["pre_risk_size"]
        if exp is None or act not in SIZE_ORDER: continue
        # violation only if ACTUAL is LARGER than win-rate-implied (upgrade); downgrades OK
        if SIZE_ORDER.get(act, 99) > SIZE_ORDER.get(exp, -1):
            viol.append((r["report_date"], r["ticker"], r["claimed_win_rate"], exp, act))
    print(f"Sizing-map: {len(szrows)-len(viol)}/{len(szrows)} compliant-or-downgraded ({len(viol)} apparent upgrades)")

    # ---- 3. Gate firing rates ----
    gv = [r for r in rows if r.get("gate_verdicts")]
    gates = ["regime", "vrp", "panic", "cluster", "sector", "event_risk", "fundamentals"]
    fired = Counter()
    for r in gv:
        for g in gates:
            v = str(r["gate_verdicts"].get(g, "")).lower()
            if v and not v.startswith("ok") and "no-op" not in v and v not in ("", "na", "none"):
                if g == "fundamentals":
                    if "veto" in v or "caution" in v: fired[g] += 1
                elif re.search(r"-\d|veto|caution|downgrade|-0\.5|-1", v):
                    fired[g] += 1
    print(f"\nGate firing (of {len(gv)} rows w/ gate_verdicts):")
    for g in gates: print(f"  {g}: {fired[g]}")

    # ---- 4. C24 gate EFFECTIVENESS (on decided outcomes) ----
    print("\n=== C24 GATE EFFECTIVENESS (decided only — thin) ===")
    # downgrade-effectiveness: per gate, WR of gated-DOWN decided vs not-gated decided
    eff = {}
    for g in gates:
        downs = [r for r in gv if dec(r) and re.search(r"-\d|veto|caution|downgrade", str(r["gate_verdicts"].get(g, "")).lower())]
        ups = [r for r in gv if dec(r) and not re.search(r"-\d|veto|caution|downgrade", str(r["gate_verdicts"].get(g, "")).lower())]
        dw = (sum(y(r) for r in downs) / len(downs)) if downs else None
        uw = (sum(y(r) for r in ups) / len(ups)) if ups else None
        eff[g] = {"down_n": len(downs), "down_wr": dw, "ungated_n": len(ups), "ungated_wr": uw}
        dws = f"{dw*100:.0f}%" if dw is not None else "n/a"
        uws = f"{uw*100:.0f}%" if uw is not None else "n/a"
        flag = "ADVISORY(<10)" if len(downs) < 10 else ""
        print(f"  {g}: gated-down WR={dws}(n{len(downs)}) vs ungated WR={uws}(n{len(ups)}) {flag}")

    # VETO/CAUTION false-positive rate
    print("\n  fundamentals VETO/CAUTION FP-rate (would-have-won among CAUTION/VETO decided):")
    fund = [r for r in rows if r.get("fundamentals_verdict") in ("VETO", "CAUTION") and dec(r)]
    if fund:
        w = sum(y(r) for r in fund)
        print(f"    CAUTION/VETO decided n={len(fund)} | won={w} -> FP-rate={w/len(fund)*100:.0f}% (ADVISORY, n<10)")
    else:
        print("    n=0 decided CAUTION/VETO -> INSUFFICIENT_N")

    # debate-gate effectiveness
    print("\n  debate-gate effectiveness (bear>=bull downgrade vs bull-won, decided):")
    dbg = [r for r in rows if r.get("debate_residual_confidence") is not None and dec(r)]
    print(f"    debate-resolved decided n={len(dbg)} -> {'INSUFFICIENT_N' if len(dbg)<10 else 'computable'}")

    # ---- 5. Missed-gate ledger (event_risk T+3..T+5) ----
    print("\n=== Missed-gate ledger (event_risk no-op on in-horizon events) ===")
    missed = []
    for r in gv:
        ev = str(r["gate_verdicts"].get("event_risk", "")).lower()
        mer = r.get("macro_event_risk")
        if mer and isinstance(mer, (str, dict)) and ev.startswith("ok") and r.get("horizon") in ("swing", "weekly"):
            missed.append((r["report_date"], r["ticker"], str(mer)[:60]))
    print(f"  candidate missed event_risk: {len(missed)} (vs ~29 applicable -> see 05-29 ~28%)")

    out = {"sigma_ok": ok_sum, "sigma_n": len(struct), "sizing_compliant": len(szrows)-len(viol),
           "sizing_n": len(szrows), "gate_firing": dict(fired), "gate_effectiveness": eff,
           "fund_fp_n": len(fund), "fund_fp_won": (sum(y(r) for r in fund) if fund else 0),
           "debate_decided": len(dbg), "missed_event_n": len(missed)}
    json.dump(out, open(f"{AUD}/phase_6_decision_audit.jsonl", "w"), indent=1, default=str)

if __name__ == "__main__":
    main()
