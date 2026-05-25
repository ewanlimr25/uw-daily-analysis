"""Tests for scripts/pead_backtest.py — C7 PEAD 10d-forward excess-return backtest."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import pead_backtest as pb  # noqa: E402


def _series(start_price, n_days, daily_ret, start="2026-05-01"):
    """Build a {date: close} trading-day series (skips weekends) from a daily return."""
    import datetime
    out, px, d = {}, float(start_price), datetime.date.fromisoformat(start)
    added = 0
    while added < n_days:
        if d.weekday() < 5:  # Mon-Fri
            out[d.isoformat()] = round(px, 4)
            px *= (1 + daily_ret)
            added += 1
        d += datetime.timedelta(days=1)
    return out


class ForwardReturnTest(unittest.TestCase):
    def test_counts_trading_days_not_calendar(self):
        s = _series(100, 30, 0.01, start="2026-05-01")  # +1%/session
        # report on the first date; entry = next session, exit = 10 sessions later.
        r = pb.forward_return(s, report_date=sorted(s)[0], fwd_days=10)
        self.assertAlmostEqual(r, (1.01 ** 10) - 1, places=4)

    def test_none_when_insufficient_forward_window(self):
        s = _series(100, 5, 0.01)
        self.assertIsNone(pb.forward_return(s, report_date=sorted(s)[0], fwd_days=10))

    def test_none_when_no_post_report_session(self):
        s = _series(100, 12, 0.01)
        self.assertIsNone(pb.forward_return(s, report_date=sorted(s)[-1], fwd_days=10))


class EventExcessTest(unittest.TestCase):
    def test_excess_is_name_minus_spy_same_window(self):
        name = _series(100, 20, 0.02)   # +2%/session
        spy = _series(500, 20, 0.01)    # +1%/session
        prices = {"AMD": name, "SPY": spy}
        ev = pb.EarningsEvent("AMD", sorted(name)[0], surprise_pct=5.0)
        r = pb.event_excess(ev, prices, fwd_days=10)
        self.assertIsNotNone(r)
        self.assertGreater(r["fwd_return_pct"], r["spy_return_pct"])
        self.assertAlmostEqual(r["excess_pct"], round(r["fwd_return_pct"] - r["spy_return_pct"], 3), places=3)

    def test_none_without_spy(self):
        prices = {"AMD": _series(100, 20, 0.01)}
        ev = pb.EarningsEvent("AMD", sorted(prices["AMD"])[0], 5.0)
        self.assertIsNone(pb.event_excess(ev, prices, fwd_days=10))


class RunBacktestTest(unittest.TestCase):
    def _prices(self):
        # SPY flat-ish; names drift per their own series built in each test.
        return {"SPY": _series(500, 25, 0.001)}

    def test_go_when_cohort_beats_spy_n_ge_10(self):
        prices = self._prices()
        events = []
        for i in range(12):
            t = f"T{i}"
            prices[t] = _series(100, 25, 0.005)  # +0.5%/session > SPY +0.1%
            events.append(pb.EarningsEvent(t, sorted(prices[t])[0], surprise_pct=3.0))
        res = pb.run_backtest(events, prices, as_of="2026-12-31")
        self.assertEqual(res["n"], 12)
        self.assertEqual(res["hit_rate"], 1.0)
        self.assertGreater(res["mean_excess_pct"], 0)
        self.assertEqual(res["verdict"], "GO_SHIP_SCORED_LINE")

    def test_insufficient_when_n_below_10(self):
        prices = self._prices()
        events = []
        for i in range(6):
            t = f"T{i}"
            prices[t] = _series(100, 25, 0.005)
            events.append(pb.EarningsEvent(t, sorted(prices[t])[0], 3.0))
        res = pb.run_backtest(events, prices, as_of="2026-12-31")
        self.assertEqual(res["n"], 6)
        self.assertEqual(res["verdict"], "INSUFFICIENT_SAMPLE")

    def test_no_go_when_hit_rate_below_floor(self):
        prices = self._prices()
        events = []
        # 11 names UNDERperform SPY (negative excess) -> hit_rate ~0
        for i in range(11):
            t = f"T{i}"
            prices[t] = _series(100, 25, -0.002)  # falling vs SPY rising
            events.append(pb.EarningsEvent(t, sorted(prices[t])[0], 3.0))
        res = pb.run_backtest(events, prices, as_of="2026-12-31")
        self.assertEqual(res["n"], 11)
        self.assertLessEqual(res["hit_rate"], 0.55)
        self.assertEqual(res["verdict"], "NO_GO_ADVISORY_ONLY")

    def test_negative_surprise_events_excluded(self):
        prices = self._prices()
        prices["MISS"] = _series(100, 25, 0.02)
        ev = [pb.EarningsEvent("MISS", sorted(prices["MISS"])[0], surprise_pct=-4.0)]
        res = pb.run_backtest(ev, prices, as_of="2026-12-31")
        self.assertEqual(res["n"], 0)
        self.assertEqual(res["verdict"], "INSUFFICIENT_SAMPLE")

    def test_lookahead_guard_drops_future_events(self):
        prices = self._prices()
        prices["FUT"] = _series(100, 25, 0.02, start="2026-05-01")
        ev = [pb.EarningsEvent("FUT", "2026-05-01", 3.0)]
        # as_of before the report date -> event dropped
        res = pb.run_backtest(ev, prices, as_of="2026-04-01")
        self.assertEqual(res["n"], 0)

    def test_lookahead_guard_drops_event_whose_exit_postdates_as_of(self):
        # report_date <= as_of but the 10d forward window EXITS after as_of -> must be dropped
        # (strict point-in-time: no consuming prices that postdate the as-of).
        prices = self._prices()
        name = _series(100, 25, 0.02, start="2026-05-01")
        prices["MIDWIN"] = name
        report = sorted(name)[0]                 # 2026-05-01
        as_of = sorted(name)[5]                  # only ~5 sessions after the report
        ev = [pb.EarningsEvent("MIDWIN", report, 3.0)]
        res = pb.run_backtest(ev, prices, as_of=as_of, fwd_days=10)
        self.assertEqual(res["n"], 0)
        self.assertEqual(res["verdict"], "INSUFFICIENT_SAMPLE")


if __name__ == "__main__":
    unittest.main()
