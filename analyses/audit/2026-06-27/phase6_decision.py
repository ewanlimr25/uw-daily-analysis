#!/usr/bin/env python3
"""Phase 6 — Decision-Process Audit. Compliance + gate effectiveness (C24).
Activation floor: gate-effectiveness verdicts need >=10 decided per arm; below = advisory."""
import json, sys
sys.path.insert(0, "scripts")
from excess_winrate import size_from_winrate  # noqa

AUD = "analyses/audit/2026-06-27"
rows = [json.loads(l) for l in open(f"{AUD}/phase_2_outcomes.jsonl")]
dec = [r for r in rows if r["outcome"] in ("WIN", "LOSS")]
SIZE_RANK = {"skip": 0, "starter": 1, "quarter": 2, "half": 3, "full": 4}


def wr(sub):
    w = sum(1 for r in sub if r["outcome"] == "WIN")
    return (w, len(sub), round(w / len(sub), 3) if sub else None)


def fired(verdict):
    if verdict is None:
        return None
    v = str(verdict).lower()
    if v.startswith("no_op") or v.startswith("pass") or v == "ok" or v.startswith("clear") or v.startswith("confirm"):
        return False
    return True


# ---------- 1. quant compliance ----------
scored = [r for r in rows if r["n_components"] > 0]
sum_ok = sum(1 for r in scored if r["sum_points"] == r["raw_score"])
prov_ok = all(all(c.get("source_agent") and (c.get("source_tool") or c.get("tool"))
                  for c in r["score_components"]) for r in scored)
# sizing-map: only directional (non-vol) rows; upgrade above implied = violation
sizing_viol = []
for r in scored:
    if r["thesis_direction"] in ("vol_long", "vol_short"):
        continue  # vol sizing decoupled from directional win-rate ladder
    cwr = r.get("claimed_win_rate")
    if cwr is None or r.get("pre_risk_size") in (None, "watch_only"):
        continue
    implied = size_from_winrate(cwr)
    if SIZE_RANK.get(r["pre_risk_size"], 0) > SIZE_RANK.get(implied, 0):
        sizing_viol.append({"date": r["report_date"], "ticker": r["ticker"],
                            "claimed_wr": cwr, "implied": implied, "pre_risk": r["pre_risk_size"]})

# ---------- 2. gate firing rates ----------
GATES = ["regime", "vrp", "panic", "cluster", "sector", "fundamentals", "event_risk", "debate", "rubric_regime"]
firing = {}
for g in GATES:
    present = [r for r in rows if g in (r.get("gate_verdicts") or {})]
    fired_rows = [r for r in present if fired(r["gate_verdicts"][g])]
    firing[g] = {"present": len(present), "fired": len(fired_rows),
                 "fire_rate": round(len(fired_rows) / len(present), 3) if present else None}

# ---------- 3. gate effectiveness (downgrade-effectiveness) ----------
eff = {}
for g in GATES:
    present_dec = [r for r in dec if g in (r.get("gate_verdicts") or {})]
    fd = [r for r in present_dec if fired(r["gate_verdicts"][g])]
    nf = [r for r in present_dec if not fired(r["gate_verdicts"][g])]
    w_f, n_f, wr_f = wr(fd)
    w_n, n_n, wr_n = wr(nf)
    advisory = (n_f < 10 or n_n < 10)
    eff[g] = {"fired_decided": n_f, "fired_wr": wr_f, "notfired_decided": n_n, "notfired_wr": wr_n,
              "delta_pp": round((wr_f - wr_n) * 100, 1) if (wr_f is not None and wr_n is not None) else None,
              "advisory_thin_n": advisory}

# ---------- VETO/CAUTION false-positive rate ----------
veto = [r for r in dec if r["fundamentals_verdict"] == "VETO"]
caution = [r for r in dec if r["fundamentals_verdict"] == "CAUTION"]
confirm = [r for r in dec if r["fundamentals_verdict"] == "CONFIRM"]
veto_fp = {"veto_decided": len(veto), "veto_wr": wr(veto)[2],
           "caution_decided": len(caution), "caution_wr": wr(caution)[2],
           "confirm_decided": len(confirm), "confirm_wr": wr(confirm)[2],
           "advisory_thin_n": len(veto) < 10}

# ---------- debate-gate effectiveness ----------
deb = []
for r in dec:
    dr = r.get("debate_residuals") or {}
    b, be = dr.get("bull"), dr.get("bear")
    if b is not None and be is not None:
        deb.append((r, be >= b))  # bear won
bear_won = [r for r, bw in deb if bw]
bull_won = [r for r, bw in deb if not bw]
debate_eff = {"n_with_residuals": len(deb), "bear_won_wr": wr(bear_won)[2], "bear_won_n": len(bear_won),
              "bull_won_wr": wr(bull_won)[2], "bull_won_n": len(bull_won),
              "advisory_thin_n": len(deb) < 10}

# ---------- missed-gate proxy: rows that should have a gate considered but lack the key ----------
# A scored directional row with no 'regime' key = regime gate not recorded.
missed = {}
for g in ["regime", "vrp", "event_risk", "fundamentals"]:
    scored_dir = [r for r in scored if r["thesis_direction"] in ("long", "short", "vol_long", "vol_short")]
    no_key = [r for r in scored_dir if g not in (r.get("gate_verdicts") or {})]
    missed[g] = {"scored_dir": len(scored_dir), "missing_key": len(no_key),
                 "missed_rate": round(len(no_key) / len(scored_dir), 3) if scored_dir else None}

out = {"quant": {"scored_rows": len(scored), "sum_points_ok": sum_ok, "sum_points_total": len(scored),
                 "provenance_complete": prov_ok, "sizing_violations": sizing_viol},
       "gate_firing": firing, "gate_effectiveness": eff, "veto_fp": veto_fp,
       "debate_eff": debate_eff, "missed_gate": missed}
json.dump(out, open(f"{AUD}/phase_6_decision_audit.jsonl", "w"), indent=1)

print(f"QUANT: sum_points {sum_ok}/{len(scored)} | provenance complete={prov_ok} | sizing upgrade-violations={len(sizing_viol)}")
for v in sizing_viol[:10]:
    print("   VIOL", v)
print("\nGATE FIRING (present / fired / rate):")
for g, v in firing.items():
    print(f"  {g:14} {v['fired']:3}/{v['present']:3} = {v['fire_rate']}")
print("\nGATE EFFECTIVENESS (fired WR vs not-fired WR, decided; <10/arm=advisory):")
for g, v in eff.items():
    print(f"  {g:14} fired {str(v['fired_wr']):>5}(n{v['fired_decided']:2}) vs notfired {str(v['notfired_wr']):>5}(n{v['notfired_decided']:2})"
          f"  delta={v['delta_pp']}pp {'[ADVISORY]' if v['advisory_thin_n'] else '[OK]'}")
print(f"\nVETO/CAUTION FP: VETO_wr={veto_fp['veto_wr']}(n{veto_fp['veto_decided']}) "
      f"CAUTION_wr={veto_fp['caution_wr']}(n{veto_fp['caution_decided']}) CONFIRM_wr={veto_fp['confirm_wr']}(n{veto_fp['confirm_decided']}) "
      f"{'[ADVISORY]' if veto_fp['advisory_thin_n'] else '[OK]'}")
print(f"DEBATE: bear_won_wr={debate_eff['bear_won_wr']}(n{debate_eff['bear_won_n']}) "
      f"bull_won_wr={debate_eff['bull_won_wr']}(n{debate_eff['bull_won_n']}) {'[ADVISORY]' if debate_eff['advisory_thin_n'] else '[OK]'}")
print("\nMISSED-GATE (scored directional rows lacking the gate key):")
for g, v in missed.items():
    print(f"  {g:14} {v['missing_key']}/{v['scored_dir']} missing = {v['missed_rate']}")
