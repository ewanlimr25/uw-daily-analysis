"""Tests for scripts/proximity_52w_backtest.py — C8 52-week-high proximity swing backtest."""

import datetime
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import proximity_52w_backtest as pb  # noqa: E402


def _series(prices_by_offset, start="2025-06-01"):
    """Build a {date: close} trading-day series from a list of closes (one per session)."""
    out, d, i = {}, datetime.date.fromisoformat(start), 0
    for px in prices_by_offset:
        while d.weekday() >= 5:
            d += datetime.timedelta(days=1)
        out[d.isoformat()] = px
        d += datetime.timedelta(days=1)
        i += 1
    return out


class Pct52wTest(unittest.TestCase):
    def test_at_high_is_100pct(self):
        s = _series([10, 20, 30])  # high = 30, entry = last = 30
        self.assertAlmostEqual(pb.pct_of_52w_high(s, sorted(s)[-1]), 1.0, places=4)

    def test_below_high(self):
        s = _series([10, 20, 30, 24])  # high 30, entry 24 -> 0.80
        self.assertAlmostEqual(pb.pct_of_52w_high(s, sorted(s)[-1]), 0.80, places=4)

    def test_lookahead_high_only_uses_sessions_upto_entry(self):
        s = _series([10, 20, 18, 50])  # if entry is the 3rd session (18), the 50 must NOT count
        entry = sorted(s)[2]
        # high over [10,20,18] = 20, entry 18 -> 0.90 (the later 50 is excluded)
        self.assertAlmostEqual(pb.pct_of_52w_high(s, entry), 0.90, places=4)


class ForwardReturnTest(unittest.TestCase):
    def test_fwd_return(self):
        s = _series([100, 101, 102, 110])
        r = pb.forward_return(s, entry_date=sorted(s)[0], fwd_days=3)  # 110/100 - 1
        self.assertAlmostEqual(r, 0.10, places=4)

    def test_none_when_insufficient_forward(self):
        s = _series([100, 101])
        self.assertIsNone(pb.forward_return(s, sorted(s)[0], fwd_days=10))


class RunBacktestTest(unittest.TestCase):
    def _name(self, hist_high, entry_px, fwd_px, n_hist=60):
        # history rising to hist_high, then entry_px, then a forward path ending at fwd_px.
        hist = [hist_high * (0.5 + 0.5 * i / n_hist) for i in range(n_hist)]
        hist[-1] = hist_high                      # the 52w high
        tail = [entry_px] + [fwd_px] * 10         # entry then 10 forward sessions at fwd_px
        return _series(hist + tail)

    def test_go_when_near_beats_far_by_10pp(self):
        prices = {}
        # 10 near-high names that go UP, 8 far-from-high names that go DOWN -> big WR split.
        for i in range(10):
            s = self._name(hist_high=100, entry_px=98, fwd_px=105)   # 0.98 of high, +up
            prices[f"NEAR{i}"] = s
        for i in range(8):
            s = self._name(hist_high=100, entry_px=70, fwd_px=68)    # 0.70 of high, down
            prices[f"FAR{i}"] = s
        entry = sorted(prices["NEAR0"])[-11]  # the entry session (11 before end)
        res = pb.run_backtest(prices, entry, fwd_days=10)
        self.assertEqual(res["n_near"], 10)
        self.assertEqual(res["n_far"], 8)
        self.assertGreaterEqual(res["wr_split"], 0.10)
        self.assertEqual(res["verdict"], "GO_SHIP_CONDITIONAL_PLUS_ONE")

    def test_insufficient_when_n_below_15(self):
        prices = {f"NEAR{i}": self._name(100, 98, 105) for i in range(5)}
        prices.update({f"FAR{i}": self._name(100, 70, 68) for i in range(5)})
        entry = sorted(prices["NEAR0"])[-11]
        res = pb.run_backtest(prices, entry, fwd_days=10)
        self.assertEqual(res["n_total"], 10)
        self.assertEqual(res["verdict"], "INSUFFICIENT_SAMPLE")

    def test_no_go_when_split_below_10pp(self):
        # both buckets ~50/50 -> split ~0
        prices = {}
        for i in range(10):
            prices[f"NEAR{i}"] = self._name(100, 98, 105 if i % 2 else 96)
        for i in range(8):
            prices[f"FAR{i}"] = self._name(100, 70, 73 if i % 2 else 69)
        entry = sorted(prices["NEAR0"])[-11]
        res = pb.run_backtest(prices, entry, fwd_days=10)
        self.assertGreaterEqual(res["n_total"], 15)
        self.assertLess(res["wr_split"], 0.10)
        self.assertEqual(res["verdict"], "NO_GO_WITHHOLD")

    def test_mid_band_names_excluded(self):
        # an 85%-of-high name is in neither bucket (between 80 and 95).
        prices = {"MID": self._name(100, 85, 90)}
        entry = sorted(prices["MID"])[-11]
        res = pb.run_backtest(prices, entry, fwd_days=10)
        self.assertEqual(res["n_total"], 0)


if __name__ == "__main__":
    unittest.main()
