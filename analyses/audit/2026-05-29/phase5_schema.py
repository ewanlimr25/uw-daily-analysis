#!/usr/bin/env python3
"""Phase 5 — schema critique: per-score WR, tier-cut reoptimization, holdout stress-test."""
import json, collections, statistics
from pathlib import Path
AUDIT = Path("analyses/audit/2026-05-29")
WIN, LOSS = "WIN", "LOSS"

def wr(rows):
    d=[r for r in rows if r["outcome"] in (WIN,LOSS)]
    return (sum(1 for r in d if r["outcome"]==WIN)/len(d), len(d)) if d else (None,0)

def brier(rows):
    b=[r for r in rows if r.get("claimed_win_rate") is not None and r["outcome"] in (WIN,LOSS)]
    if not b: return None,0
    return statistics.mean([(r["claimed_win_rate"]-(1.0 if r["outcome"]==WIN else 0.0))**2 for r in b]), len(b)

def tier_wr(rows, hi, med):
    """cuts: score>=hi HIGH, med<=score<hi MED, <med LOW."""
    H=[r for r in rows if r.get("raw_score") is not None and r["raw_score"]>=hi]
    M=[r for r in rows if r.get("raw_score") is not None and med<=r["raw_score"]<hi]
    L=[r for r in rows if r.get("raw_score") is not None and r["raw_score"]<med]
    return wr(H),wr(M),wr(L)

def main():
    rows=[json.loads(l) for l in open(AUDIT/"phase_2_outcomes.jsonl")]
    dec=[r for r in rows if r["outcome"] in (WIN,LOSS) and r.get("raw_score") is not None]

    # 1. per-integer-score realised WR
    per_score=[]
    for s in sorted(set(r["raw_score"] for r in dec)):
        w,n=wr([r for r in dec if r["raw_score"]==s])
        per_score.append({"score":s,"n":n,"wr":round(w,3) if w else None})

    # 2. current cuts
    cur=tier_wr(dec,10,7)
    current={"cuts":"HIGH>=10 / MED 7-9 / LOW 3-6","HIGH":cur[0],"MED":cur[1],"LOW":cur[2]}

    # 3. search proposed cuts maximizing monotonicity & HIGH-MED gap (min 15 per tier)
    best=None
    scores=[r["raw_score"] for r in dec]
    lo,hi=min(scores),max(scores)
    for med in range(lo+1,hi):
        for high in range(med+1,hi+1):
            (wH,nH),(wM,nM),(wL,nL)=tier_wr(dec,high,med)
            if None in (wH,wM,wL) or min(nH,nM,nL)<15: continue
            if wH>wM>wL:
                gap=wH-wM
                score=gap+(wM-wL)*0.5
                if best is None or score>best["score"]:
                    best={"score":score,"hi":high,"med":med,"wH":wH,"nH":nH,"wM":wM,"nM":nM,"wL":wL,"nL":nL,"gap":gap}

    # 4. holdout: most recent 20% of reports (by date)
    reps=sorted(set((r["report_date"],r["report_kind"]) for r in rows),
                key=lambda x:(x[0].replace("2026-W","2026-99-W") if x[1]=="weekly" else x[0]))
    n_hold=max(2,-(-len(reps)//5))
    hold=set(reps[-n_hold:]); train=set(reps[:-n_hold])
    dec_tr=[r for r in dec if (r["report_date"],r["report_kind"]) in train]
    dec_ho=[r for r in dec if (r["report_date"],r["report_kind"]) in hold]
    # refit cuts on train
    bestT=None
    for med in range(lo+1,hi):
        for high in range(med+1,hi+1):
            (wH,nH),(wM,nM),(wL,nL)=tier_wr(dec_tr,high,med)
            if None in (wH,wM,wL) or min(nH,nM,nL)<8: continue
            if wH>wM>wL:
                if bestT is None or (wH-wM)>bestT["gap"]:
                    bestT={"hi":high,"med":med,"gap":wH-wM}
    holdout={}
    if bestT:
        (hH,_),(hM,_),(hL,_)=tier_wr(dec_ho,bestT["hi"],bestT["med"])
        (tH,_),(tM,_),(tL,_)=tier_wr(dec_tr,bestT["hi"],bestT["med"])
        bI,_=brier(dec_tr); bO,_=brier(dec_ho)
        holdout={"refit_cuts":bestT,"n_holdout_reports":n_hold,
                 "insample_tier_wr":{"HIGH":round(tH,3) if tH else None,"MED":round(tM,3) if tM else None,"LOW":round(tL,3) if tL else None},
                 "holdout_tier_wr":{"HIGH":round(hH,3) if hH else None,"MED":round(hM,3) if hM else None,"LOW":round(hL,3) if hL else None},
                 "brier_insample":round(bI,4) if bI else None,"brier_holdout":round(bO,4) if bO else None,
                 "monotone_holds_out": (hH is not None and hM is not None and hL is not None and hH>hM>hL)}

    out={"per_score":per_score,"current_cuts":current,"proposed_cuts":best,"holdout":holdout}
    json.dump(out,open(AUDIT/"phase_5_schema.jsonl","w"),indent=1)
    print(json.dumps(out,indent=1,default=str))

if __name__=="__main__":
    main()
