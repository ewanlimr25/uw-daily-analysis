#!/usr/bin/env python3
"""Phase 5 (2026-05-30) — tier-cut audit + holdout on the C20 outcomes.
Component RE-WEIGHT is DEFERRED: Phase 4 MCs are method-unstable (term-skew flipped sign;
oi-trend/signal-confluence collapsed) and BH-insignificant on reconstructed citations.
Re-weighting a fixed budget on that basis would chase noise (meta-audit 'NOT proposed')."""
import json, statistics, importlib.util

spec = importlib.util.spec_from_file_location("p3", "analyses/audit/2026-05-30/phase3_calibration_v2.py")
p3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p3)

AUD = "analyses/audit/2026-06-06"

def wr(rows):
    d = [r for r in rows if r["outcome"] in ("WIN", "LOSS")]
    return (sum(1 for r in d if r["outcome"] == "WIN") / len(d), len(d)) if d else (None, 0)

def tiers_for(rows, hi, lo):
    """HIGH if score>=hi, LOW if score<lo, else MED."""
    H = [r for r in rows if r.get("raw_score") is not None and r["raw_score"] >= hi]
    L = [r for r in rows if r.get("raw_score") is not None and r["raw_score"] < lo]
    M = [r for r in rows if r.get("raw_score") is not None and lo <= r["raw_score"] < hi]
    return wr(H), wr(M), wr(L)

def main():
    rows = [json.loads(l) for l in open(f"{AUD}/phase_2_outcomes.jsonl")]
    dec = [r for r in rows if r["outcome"] in ("WIN", "LOSS") and r.get("raw_score") is not None]

    # per-integer score WR
    print("=== per-integer raw_score realised WR ===")
    by_s = {}
    for s in sorted(set(r["raw_score"] for r in dec)):
        sub = [r for r in dec if r["raw_score"] == s]
        w, n = wr(sub); by_s[s] = (w, n)
        print(f"  score {s:>3}: WR={w*100:4.0f}% (n={n})")

    # current cuts (>=10 / 7-9 / 3-6 per signal-confluence-quant live doc; LOW<3 incl <3)
    print("\n=== tier cuts (HIGH>=hi / LOW<lo) — maximize monotonicity ===")
    candidates = [(10, 3), (10, 4), (9, 4), (9, 3), (8, 4), (7, 4), (7, 3)]
    best = None
    for hi, lo in candidates:
        (Hw, Hn), (Mw, Mn), (Lw, Ln) = tiers_for(dec, hi, lo)
        if None in (Hw, Mw, Lw):
            print(f"  HIGH>={hi}/LOW<{lo}: incomplete"); continue
        mono = Hw > Mw > Lw
        gap = Hw - Mw
        print(f"  HIGH>={hi}/LOW<{lo}: HIGH {Hw*100:.1f}%(n{Hn}) MED {Mw*100:.1f}%(n{Mn}) LOW {Lw*100:.1f}%(n{Ln}) "
              f"{'MONOTONE' if mono else 'no'} gapHM={gap*100:+.1f}")
        if mono and (best is None or gap > best[1]):
            best = ((hi, lo), gap)
    print("  -> best monotone cut:", best[0] if best else "NONE monotone")

    # holdout: most-recent 20% of reports (by report_date), refit cut on older 80%
    print("\n=== holdout stress-test (recent 20% of report-dates) ===")
    dates = sorted(set(r["report_date"] for r in rows if r["report_kind"] == "daily"))
    k = max(2, round(len(dates) * 0.2))
    hold_dates = set(dates[-k:])
    train = [r for r in dec if r["report_date"] not in hold_dates]
    test = [r for r in dec if r["report_date"] in hold_dates]
    print(f"  train reports={len(dates)-k} (n_dec={len(train)}) | holdout reports={k} (n_dec={len(test)})")
    hi, lo = (best[0] if best else (9, 4))
    for label, rs in (("train", train), ("holdout", test)):
        (Hw, Hn), (Mw, Mn), (Lw, Ln) = tiers_for(rs, hi, lo)
        def f(x): return f"{x*100:.1f}%" if x is not None else "n/a"
        print(f"  {label} (HIGH>={hi}/LOW<{lo}): HIGH {f(Hw)}(n{Hn}) MED {f(Mw)}(n{Mn}) LOW {f(Lw)}(n{Ln})")

    out = {"per_score": {str(s): {"wr": by_s[s][0], "n": by_s[s][1]} for s in by_s},
           "best_cut": best[0] if best else None,
           "holdout": {"hold_dates": sorted(hold_dates), "n_train": len(train), "n_test": len(test)},
           "reweight": "DEFERRED — Phase 4 MCs method-unstable + BH-null on reconstructed citations"}
    json.dump(out, open(f"{AUD}/phase_5_schema.jsonl", "w"), indent=1, default=str)

if __name__ == "__main__":
    main()
