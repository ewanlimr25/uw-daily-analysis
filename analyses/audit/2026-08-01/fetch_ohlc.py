#!/usr/bin/env python3
"""C20 enabler: fetch REAL daily OHLC from the Yahoo chart API the yfinance MCP wraps.

The mcp__yahoo-finance__* tools flatten to close-only in this env; the underlying
chart API carries real high/low. Window covers ATR(14) lookback before the earliest
entry (2026-05-25) through the last available bar (2026-07-02; 07-03 was the
July-4th market holiday).
"""
import urllib.request, json, ssl, datetime, calendar, time, os, sys

AUD = "analyses/audit/2026-08-01"
OUT = f"{AUD}/_ohlc"
os.makedirs(OUT, exist_ok=True)
CTX = ssl.create_default_context()


def epoch(d):
    return calendar.timegm(datetime.datetime.strptime(d, "%Y-%m-%d").timetuple())


P1, P2 = epoch("2026-04-15"), epoch("2026-08-02")


def fetch(sym, tries=4):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
           f"?period1={P1}&period2={P2}&interval=1d")
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=20, context=CTX) as r:
                data = json.load(r)
            res = data["chart"]["result"][0]
            q = res["indicators"]["quote"][0]
            ts = res["timestamp"]
            bars = []
            for i in range(len(ts)):
                if q["close"][i] is None:
                    continue
                d = datetime.datetime.fromtimestamp(ts[i], datetime.UTC).strftime("%Y-%m-%d")
                bars.append({"date": d, "open": q["open"][i], "high": q["high"][i],
                             "low": q["low"][i], "close": q["close"][i]})
            return {"symbol": sym, "bars": bars, "ok": True,
                    "real_ohlc": any(b["high"] != b["low"] for b in bars)}
        except Exception as e:
            if k == tries - 1:
                return {"symbol": sym, "bars": [], "ok": False,
                        "error": f"{type(e).__name__}:{str(e)[:120]}"}
            time.sleep(1.5 * (k + 1))


def main():
    tb = json.load(open(f"{AUD}/_tickers.json"))
    syms = sorted(set(tb) | {"SPY"})
    ok = bad = 0
    manifest = {}
    for i, s in enumerate(syms):
        path = f"{OUT}/{s}.json"
        if os.path.exists(path):
            d = json.load(open(path))
            if d.get("ok") and d.get("bars") and d["bars"][-1]["date"] >= "2026-07-31":
                ok += 1; manifest[s] = len(d["bars"]); continue
        d = fetch(s)
        json.dump(d, open(path, "w"))
        if d["ok"]:
            ok += 1; manifest[s] = len(d["bars"])
        else:
            bad += 1; manifest[s] = d.get("error", "FAIL")
            print(f"  BAD {s}: {d.get('error')}", file=sys.stderr)
        time.sleep(0.2)
        if (i + 1) % 25 == 0:
            print(f"  ...{i+1}/{len(syms)}", file=sys.stderr)
    json.dump(manifest, open(f"{AUD}/_ohlc_manifest.json", "w"), indent=0)
    print(f"FETCH DONE ok={ok} bad={bad} of {len(syms)}")
    spy = json.load(open(f"{OUT}/SPY.json"))
    print("SPY bars:", len(spy["bars"]), "real_ohlc:", spy.get("real_ohlc"),
          "last:", spy["bars"][-1] if spy["bars"] else None)
    # bad list
    bad_syms = [s for s, v in manifest.items() if isinstance(v, str)]
    if bad_syms:
        print("BAD SYMBOLS:", bad_syms)


if __name__ == "__main__":
    main()
