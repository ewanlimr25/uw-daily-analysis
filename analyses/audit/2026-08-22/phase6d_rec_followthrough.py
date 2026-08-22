#!/usr/bin/env python3
"""Phase 6d — did the 2026-08-01 recommendations actually land in the emitted data?

Grades each applied rec against the post-intervention envelopes (>= 2026-08-03),
distinguishing "the agent file was edited" from "the emitted envelope changed".
The 2026-08-01 audit's own headline error was grading `insider_cluster_flag` by
KEY PRESENCE rather than POPULATION -- that check is redone here explicitly.
"""
import json, glob
from collections import Counter

AUDIT = "analyses/audit/2026-08-22"
P0 = "2026-08-03"
rows = [json.loads(l) for l in open(f"{AUDIT}/phase_2_outcomes.jsonl")]
post = [r for r in rows if r["report_date"] >= P0]
pre = [r for r in rows if r["report_date"] < P0]

print("=" * 78)
print("REC 1 (P0) — SHORT direction -> watch_only")
print("=" * 78)
SIZED = {"full", "half", "quarter", "starter"}
ps = [r for r in post if r["direction"] == "short"]
print(f"  post-P0 shorts: n={len(ps)}; final_size dist={dict(Counter(r['final_size'] for r in ps))}")
print(f"  sized violations: {sum(1 for r in ps if r['final_size'] in SIZED)}")
print(f"  counterfactual preserved (scored+gated+classed): "
      f"{sum(1 for r in ps if r['raw_score'] is not None and r['gate_verdicts'] and r['dominant_signal_class'])}/{len(ps)}")
print(f"  VERDICT: {'APPLIED CLEAN' if not any(r['final_size'] in SIZED for r in ps) else 'VIOLATED'}")

print()
print("=" * 78)
print("REC 2 (P1, C55) — re-source sector_rotation off the NETTED sector line")
print("=" * 78)
for lab, rs in (("pre ", pre), ("post", post)):
    sr = [r for r in rs if r.get("canonical_class") == "sector_rotation"]
    dec = [r for r in sr if r["outcome"] in ("WIN", "LOSS")]
    tools = Counter()
    for r in sr:
        for t in r.get("tools_cited", []):
            tools[t] += 1
    wr = f"{sum(1 for r in dec if r['outcome']=='WIN')/len(dec):.3f}" if dec else "n/a"
    print(f"  {lab}: n={len(sr)} decided={len(dec)} WR={wr}")
    netted = sum(v for k, v in tools.items() if "market_regime" in k or "netted" in k.lower())
    gross = sum(v for k, v in tools.items() if "sector_flow" in k)
    print(f"        tool citations -> netted(market_regime):{netted}  gross(sector_flow*):{gross}")

print()
print("=" * 78)
print("REC 3 (P1) — fix the earnings_vol / high_iv_rank win-rate QUOTES")
print("=" * 78)
for cls in ("earnings_vol", "high_iv_rank"):
    for lab, rs in (("pre ", pre), ("post", post)):
        sub = [r for r in rs if r.get("canonical_class") == cls and r.get("claimed_win_rate") is not None]
        if not sub:
            print(f"  {cls:13} {lab}: no quoted rows")
            continue
        q = [r["claimed_win_rate"] for r in sub]
        dec = [r for r in rs if r.get("canonical_class") == cls and r["outcome"] in ("WIN", "LOSS")]
        wr = sum(1 for r in dec if r["outcome"] == "WIN") / len(dec) if dec else None
        srcs = Counter(r.get("win_rate_source") for r in sub)
        print(f"  {cls:13} {lab}: n_quoted={len(q)} mean_claim={sum(q)/len(q):.3f} "
              f"realised={wr if wr is None else round(wr,3)} (n={len(dec)}) src={dict(srcs)}")

print()
print("=" * 78)
print("REC 4 (P1, C56) — the [0.55,0.65) anti-predictive band")
print("=" * 78)
for lab, rs in (("pre ", pre), ("post", post)):
    q = [r for r in rs if r.get("claimed_win_rate") is not None]
    band = [r for r in q if 0.55 <= r["claimed_win_rate"] < 0.65]
    dec = [r for r in band if r["outcome"] in ("WIN", "LOSS")]
    wr = sum(1 for r in dec if r["outcome"] == "WIN") / len(dec) if dec else None
    sizes = Counter(r["final_size"] for r in band)
    print(f"  {lab}: quoted={len(q)} in-band={len(band)} ({100*len(band)/len(q):.0f}% of quotes) "
          f"realised={wr if wr is None else round(wr,3)} (n={len(dec)})")
    print(f"        in-band final_size dist: {dict(sizes)}")

print()
print("=" * 78)
print("REC 5 (P1) — dp_block_to_float_ratio + insider_cluster_flag POPULATION (C16/C18)")
print("=" * 78)
for field in ("dp_block_to_float_ratio", "insider_cluster_flag"):
    key_present = pop_ = 0
    vals = Counter()
    by_post = [0, 0]
    for f in glob.glob("analyses/daily/*/decision.json") + glob.glob("analyses/weekly/*/decision.json"):
        d = json.load(open(f))
        for c in d.get("calls", []):
            if field in c:
                key_present += 1
                if d["report_date"] >= P0:
                    by_post[0] += 1
                if c[field] is not None:
                    pop_ += 1
                    vals[str(c[field])] += 1
                    if d["report_date"] >= P0:
                        by_post[1] += 1
    print(f"  {field}:")
    print(f"     key present on {key_present} calls; POPULATED (non-null) on {pop_}")
    print(f"     post-P0: key present {by_post[0]}, populated {by_post[1]}")
    print(f"     distinct populated values: {dict(vals)}")
    verdict = ("UNTESTABLE — emitter still writes null" if pop_ < 8 else
               "populated, gradeable")
    if field == "insider_cluster_flag" and set(vals) <= {"False"}:
        verdict = "UNTESTABLE — zero variance (every populated value is False)"
    print(f"     VERDICT: {verdict}")

print()
print("=" * 78)
print("REC 9 (P2) — dominant_signal_class enum drift")
print("=" * 78)
for lab, rs in (("pre ", pre), ("post", post)):
    cls = Counter(r.get("dominant_signal_class") for r in rs if r.get("dominant_signal_class"))
    _s = json.load(open("schemas/decision_envelope.schema.json"))
    canon = set(_s["$defs"]["call"]["properties"]["dominant_signal_class"]
                .get("x-canonical-classes", []))
    off = {k: v for k, v in cls.items() if k not in canon}
    print(f"  {lab}: {len(cls)} distinct classes; off-list={off or 'NONE'}")
