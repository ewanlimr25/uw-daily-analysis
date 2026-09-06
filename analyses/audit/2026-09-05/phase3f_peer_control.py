#!/usr/bin/env python3
"""Phase 3f — the vol lane's PEER benchmark (method fixed 2026-08-30, `phase_3f_peer_control.json`).

C63 is the live registration: post-change `vol_short` peer-excess >= -5pp on n >= 40
decided rows across >= 2 regime buckets. The benchmark is the UNSELECTED SAME-DATE
SINGLE-NAME PEER SET, never SPY -- the index benchmark is ~8pp conservative because an
index's realised range compresses relative to its own constituents.

For each entry date d, over every single-name ticker with >= 15 prior bars and a full
forward window, compute the SAME rv_ratio the resolver uses
(mean forward true-range / mean trailing-14 true-range) and record the fraction that
would have satisfied a vol_short thesis (ratio < 1.0). That fraction is the date's
peer WR; a vol_short row's peer-excess is (row WIN) - peer_WR_on_its_own_date.
"""
import json, os, statistics
from collections import defaultdict

AUD = "analyses/audit/2026-09-05"
OHLC = f"{AUD}/_ohlc"
INDEXY = {"SPY", "QQQ", "IWM", "DIA", "VIX", "^VIX", "SPX", "XLE", "XLF", "XLK", "XLV",
          "XLI", "XLU", "XLP", "XLY", "XLB", "XLRE", "XLC", "SMH", "GLD", "SLV", "TLT",
          "HYG", "USO", "ARKK", "EEM", "FXI", "KWEB", "IBIT", "GDX", "XBI", "XOP", "XRT"}

PX = {}
for fn in os.listdir(OHLC):
    d = json.load(open(f"{OHLC}/{fn}"))
    if d.get("ok") and d.get("bars"):
        PX[d["symbol"]] = d["bars"]

SINGLE = {s: b for s, b in PX.items() if s not in INDEXY}


def eidx(bars, date):
    idx = None
    for i, b in enumerate(bars):
        if b["date"] == date:
            return i
        if b["date"] < date:
            idx = i
    return idx


def rv_ratio(bars, ei, nwin=10):
    if ei is None or ei < 15:
        return None
    base = statistics.mean([bars[i]["high"] - bars[i]["low"] for i in range(ei - 14, ei)])
    fwd = bars[ei + 1: ei + 1 + nwin]
    if not base or base <= 0 or len(fwd) < nwin:
        return None
    return statistics.mean([b["high"] - b["low"] for b in fwd]) / base


rows = [json.loads(l) for l in open(f"{AUD}/phase_2_outcomes.jsonl") if l.strip()]
dates = sorted({r["report_date"] for r in rows})

peer = {}
for d in dates:
    ratios = []
    for s, bars in SINGLE.items():
        rr = rv_ratio(bars, eidx(bars, d))
        if rr is not None:
            ratios.append(rr)
    if len(ratios) >= 30:
        peer[d] = [sum(1 for r in ratios if r < 1.0) / len(ratios),
                   round(statistics.median(ratios), 4), len(ratios)]
json.dump(peer, open(f"{AUD}/phase_3f_peer_control.json", "w"), indent=0)
print(f"peer dates built: {len(peer)} of {len(dates)}")


def arm(sel, label):
    ok = [r for r in sel if r["outcome"] in ("WIN", "LOSS") and r["report_date"] in peer]
    if not ok:
        print(f"  {label:<44} n=0"); return None
    bw = sum(1 for r in ok if r["outcome"] == "WIN") / len(ok)
    pw = statistics.mean([peer[r["report_date"]][0] for r in ok])
    # for vol_long the peer WR is the complement (ratio > 1.0)
    if label.startswith("vol_long"):
        pw = 1 - pw
    b = sum(1 for r in ok if r["outcome"] == "WIN" and peer[r["report_date"]][0] < 0.5)
    print(f"  {label:<44} n={len(ok):>4} bookWR={bw:.3f} peerWR={pw:.3f} excess={100*(bw-pw):+6.1f}pp")
    return {"label": label, "n": len(ok), "book_wr": round(bw, 4),
            "peer_wr": round(pw, 4), "excess_pp": round(100 * (bw - pw), 2)}


def is_vs(r):
    return r.get("section") == "vol_short" or r.get("thesis_direction") == "vol_short"


def is_vl(r):
    return r.get("section") == "vol_long" or r.get("thesis_direction") == "vol_long"


print("\n=== VOL LANE vs UNSELECTED SAME-DATE SINGLE-NAME PEERS ===")
out = []
vs = [r for r in rows if is_vs(r)]
vl = [r for r in rows if is_vl(r)]
out.append(arm(vs, "vol_short  ALL"))
out.append(arm(vl, "vol_long   ALL"))

# C63 decision window: the P0 was raised 2026-08-30. Post-change == report_date > 2026-08-30.
POST = "2026-08-30"
print(f"\n=== C63 GRADING (post-change = report_date > {POST}) ===")
vsp = [r for r in vs if r["report_date"] > POST]
out.append(arm(vsp, "vol_short  POST-CHANGE"))
buckets = defaultdict(list)
for r in vsp:
    if r["outcome"] in ("WIN", "LOSS"):
        buckets[r.get("regime_bucket")].append(r)
print(f"  post-change decided by regime bucket: { {k: len(v) for k, v in buckets.items()} }")
dec = sum(len(v) for v in buckets.values())
nb = sum(1 for v in buckets.values() if v)
exc = out[-1]["excess_pp"] if out[-1] else None
bar = (dec >= 40 and nb >= 2 and exc is not None and exc >= -5)
print(f"  C63 BAR: n>=40 ({dec}) AND >=2 regime buckets ({nb}) AND excess>=-5pp ({exc}) -> "
      f"{'CLEARED' if bar else 'NOT MET'}")

print("\n=== vol_short BY REGIME BUCKET (all eras) ===")
for b in sorted({r.get("regime_bucket") for r in vs}):
    out.append(arm([r for r in vs if r.get("regime_bucket") == b], f"vol_short  {b}"))

print("\n=== vol_long BY REGIME BUCKET ===")
for b in sorted({r.get("regime_bucket") for r in vl}):
    out.append(arm([r for r in vl if r.get("regime_bucket") == b], f"vol_long   {b}"))

json.dump({"peer_dates": len(peer), "arms": [o for o in out if o],
           "c63": {"post_change_decided": dec, "regime_buckets": nb,
                   "excess_pp": exc, "cleared": bar}},
          open(f"{AUD}/phase_3f_c63.json", "w"), indent=1)
