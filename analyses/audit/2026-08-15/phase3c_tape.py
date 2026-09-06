#!/usr/bin/env python3
"""Phase 3c (NEW 2026-07-25) — EMPIRICAL tape stratification.

The last three audits pre-registered the same experiment: "the sign of the
directional edge is non-stationary; a genuine DOWN-tape is the only thing that
separates edge from beta." Regime *labels* cannot run that experiment — the
2026-07-25 dataset shows 122 decided rows carrying the bare label "TRANSITIONAL"
spanning 06-30 -> 07-23, which contains both up- and down-tape windows.

So stratify by the REALISED tape instead: sign of SPY's close-to-close return over
each row's own resolution window. This is not look-ahead for an *audit* statistic —
it is the conditioning variable ("what did the tape actually do while this trade was
live"), used to ask whether the book's directional selection adds anything ON TOP OF
the tape. It must never be used as a live signal.
"""
import json, statistics

AUD = "analyses/audit/2026-08-15"
OHLC = f"{AUD}/_ohlc"
SPY = json.load(open(f"{OHLC}/SPY.json"))["bars"]

rows = [json.loads(l) for l in open(f"{AUD}/phase_2_outcomes.jsonl")]
dec = [r for r in rows if r["outcome"] in ("WIN", "LOSS")]


def entry_idx(bars, date):
    idx = None
    for i, b in enumerate(bars):
        if b["date"] == date:
            return i
        if b["date"] < date:
            idx = i
        else:
            break
    return idx


def spy_window_ret(date, nwin):
    ei = entry_idx(SPY, date)
    if ei is None:
        return None
    fwd = SPY[ei + 1: ei + 1 + nwin]
    if not fwd:
        return None
    return (fwd[-1]["close"] - SPY[ei]["close"]) / SPY[ei]["close"] * 100


for r in dec:
    r["_spy_ret"] = spy_window_ret(r["report_date"], r.get("nwin") or 10)
    r["_tape"] = None if r["_spy_ret"] is None else ("UP" if r["_spy_ret"] > 0 else "DOWN")


def wr(sub):
    w = sum(1 for r in sub if r["outcome"] == "WIN")
    return w, len(sub), (round(w / len(sub), 3) if sub else None)


def excess(sub):
    sb = [r for r in sub if r.get("spy_benchmark_win") is not None]
    if not sb:
        return None, 0
    _, _, bwr = wr(sb)
    spy_wr = sum(1 for r in sb if r["spy_benchmark_win"]) / len(sb)
    return round((bwr - spy_wr) * 100, 1), len(sb)


out = {}

print("=== TAPE SPLIT (SPY close-to-close over each row's own window) ===")
for tape in ("UP", "DOWN"):
    sub = [r for r in dec if r["_tape"] == tape]
    w, n, rwr = wr(sub)
    e, en = excess(sub)
    med = statistics.median([r["_spy_ret"] for r in sub]) if sub else None
    print(f"  tape={tape:4} n={n:3} bookWR={rwr} excess={e}pp  medianSPYwin={med:+.2f}%")
    out[f"tape_{tape}"] = {"n": n, "wr": rwr, "excess_pp": e}

print("\n=== DIRECTIONAL SELECTION CONDITIONED ON REALISED TAPE ===")
print(f"  {'tape':5} {'dir':6} {'n':>4} {'bookWR':>7} {'spyWR':>7} {'excess':>8}")
dir_tape = {}
for tape in ("UP", "DOWN"):
    for d in ("long", "short"):
        sub = [r for r in dec if r["_tape"] == tape and r.get("thesis_direction") == d]
        sb = [r for r in sub if r.get("spy_benchmark_win") is not None]
        if not sb:
            continue
        _, n, bwr = wr(sb)
        spy_wr = round(sum(1 for r in sb if r["spy_benchmark_win"]) / len(sb), 3)
        e = round((bwr - spy_wr) * 100, 1)
        print(f"  {tape:5} {d:6} {n:4} {bwr:7} {spy_wr:7} {e:+8}pp")
        dir_tape[f"{tape}_{d}"] = {"n": n, "wr": bwr, "spy_wr": spy_wr, "excess_pp": e}
out["dir_by_tape"] = dir_tape

# The key symmetry test: does the book's directional CALL beat a coin-flip on tape direction?
print("\n=== DIRECTION-CALL ACCURACY (did the book pick the right side of the tape?) ===")
for tape in ("UP", "DOWN"):
    sub = [r for r in dec if r["_tape"] == tape and r.get("thesis_direction") in ("long", "short")]
    if not sub:
        continue
    right = sum(1 for r in sub
                if (tape == "UP" and r["thesis_direction"] == "long")
                or (tape == "DOWN" and r["thesis_direction"] == "short"))
    print(f"  tape={tape:4} n={len(sub):3} book positioned WITH tape on {right}/{len(sub)} = {right/len(sub)*100:.1f}%")
    out[f"with_tape_{tape}"] = {"n": len(sub), "with": right, "pct": round(right / len(sub) * 100, 1)}

# bearish_flow: the class whose sign has flipped every window
print("\n=== bearish_flow BY TAPE (the non-stationary line, C19 accrual) ===")
for tape in ("UP", "DOWN"):
    sub = [r for r in dec if r["_tape"] == tape and r.get("canonical_class") == "bearish_flow"]
    sb = [r for r in sub if r.get("spy_benchmark_win") is not None]
    if not sb:
        continue
    _, n, bwr = wr(sb)
    spy_wr = round(sum(1 for r in sb if r["spy_benchmark_win"]) / len(sb), 3)
    print(f"  tape={tape:4} n={n:3} WR={bwr} spyWR={spy_wr} excess={(bwr-spy_wr)*100:+.1f}pp")
    out[f"bearish_flow_{tape}"] = {"n": n, "wr": bwr, "spy_wr": spy_wr,
                                   "excess_pp": round((bwr - spy_wr) * 100, 1)}

# post-freeze only, by tape
print("\n=== POST-FREEZE ONLY, BY TAPE ===")
for tape in ("UP", "DOWN"):
    sub = [r for r in dec if r["_tape"] == tape and r.get("post_freeze")]
    w, n, rwr = wr(sub)
    e, en = excess(sub)
    print(f"  tape={tape:4} n={n:3} WR={rwr} excess={e}pp")
    out[f"post_freeze_tape_{tape}"] = {"n": n, "wr": rwr, "excess_pp": e}

# DROP-vs-book by tape (empty-board discipline under a falling tape)
print("\n=== DROP PILE vs TRADED BOOK, BY TAPE ===")
for tape in ("UP", "DOWN"):
    dr = [r for r in dec if r["_tape"] == tape and r["tier"] == "DROP"]
    bk = [r for r in dec if r["_tape"] == tape and r["tier"] in ("LOW", "MEDIUM", "HIGH")]
    sz = [r for r in dec if r["_tape"] == tape and r.get("was_sized")]
    _, dn, dwr = wr(dr); _, bn, bwr_ = wr(bk); _, sn, swr = wr(sz)
    print(f"  tape={tape:4} DROP={dwr}(n{dn})  book={bwr_}(n{bn})  sized={swr}(n{sn})")
    out[f"drop_vs_book_{tape}"] = {"drop_wr": dwr, "drop_n": dn, "book_wr": bwr_,
                                   "book_n": bn, "sized_wr": swr, "sized_n": sn}

json.dump(out, open(f"{AUD}/phase_3c_tape.jsonl", "w"), indent=1)
print("\nwrote phase_3c_tape.jsonl")
