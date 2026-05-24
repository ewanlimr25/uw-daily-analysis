"""Tests for scripts/gex_next_session_backtest.py pure computation.

The CLI-I/O shell (reconstruct/_run_cli) needs the uw-pp binary and is not unit
tested; the hit-rate math (evaluate/nearest_wall/binom_p/verdict/walls) is pure
and fully covered here with synthetic sessions whose outcomes are known.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import gex_next_session_backtest as bt  # noqa: E402


def _session(date, spot, cw, pw, dom, zgl=None, regime="POSITIVE", total_gex=1.0):
    return {
        "date": date, "spot": spot, "call_wall": cw, "put_wall": pw,
        "dom_strike": dom, "zero_gamma_level": zgl, "regime": regime,
        "total_gex": total_gex,
    }


class NearestWallTest(unittest.TestCase):
    def test_picks_closer_wall(self):
        self.assertEqual(bt.nearest_wall(100, 104, 90), 104)
        self.assertEqual(bt.nearest_wall(100, 110, 98), 98)

    def test_handles_missing_walls(self):
        self.assertEqual(bt.nearest_wall(100, None, 90), 90)
        self.assertIsNone(bt.nearest_wall(100, None, None))


class BinomTest(unittest.TestCase):
    def test_all_hits_is_significant(self):
        self.assertLess(bt.binom_p(30, 30), 0.001)

    def test_below_chance_is_near_one(self):
        self.assertGreater(bt.binom_p(5, 30), 0.99)

    def test_empty_is_nan(self):
        self.assertNotEqual(bt.binom_p(0, 0), bt.binom_p(0, 0))  # NaN != NaN


class WallsFromPerStrikeTest(unittest.TestCase):
    def test_call_above_put_below_dom_overall(self):
        per_strike = [
            {"strike": 90, "net_gex": -50},
            {"strike": 100, "net_gex": 10},
            {"strike": 105, "net_gex": 80},
            {"strike": 110, "net_gex": 20},
        ]
        walls = bt._walls_from_per_strike(per_strike, spot=100)
        self.assertEqual(walls["call_wall"], 105)   # max positive at/above spot
        self.assertEqual(walls["put_wall"], 90)     # most negative below spot
        self.assertEqual(walls["dom_strike"], 105)  # max |net_gex| overall


class EvaluateTest(unittest.TestCase):
    def test_walls_as_perfect_magnets(self):
        sessions = [
            _session("2026-05-01", 100, 104, 90, 104, zgl=99),    # long-gamma (100>=99)
            _session("2026-05-02", 103, 104, 95, 104, zgl=108),   # short-gamma (103<108)
            _session("2026-05-03", 104, 104, 95, 104, zgl=104),
        ]
        r = bt.evaluate(sessions)
        self.assertEqual(r["h2_n"], 2)
        self.assertEqual(r["closer_to_nearest_wall"]["pct"], 100.0)
        self.assertEqual(r["moved_in_pin_direction"]["pct"], 100.0)
        self.assertEqual(r["contained_within_walls"]["pct"], 100.0)
        self.assertEqual(r["closer_to_dominant_gex"]["pct"], 100.0)
        # H1: both buckets populated from the two sane-ZGL day-D sessions.
        self.assertEqual(r["h1_zgl_testable_n"], 2)
        self.assertIs(r["h1_short_gt_long_as_theory"], False)  # short 0.97% < long 3.0%

    def test_walls_repel(self):
        sessions = [
            _session("2026-05-01", 100, 104, 90, 104),
            _session("2026-05-02", 96, 104, 90, 104),   # moved away from 104 toward/below 90
        ]
        r = bt.evaluate(sessions)
        self.assertEqual(r["h2_n"], 1)
        self.assertEqual(r["closer_to_nearest_wall"]["pct"], 0.0)

    def test_unsane_zgl_excluded_from_h1(self):
        # ZGL 50 vs spot 100 is >5% away → not testable.
        sessions = [
            _session("2026-05-01", 100, 104, 90, 104, zgl=50),
            _session("2026-05-02", 103, 104, 95, 104, zgl=None),
        ]
        r = bt.evaluate(sessions)
        self.assertEqual(r["h1_zgl_testable_n"], 0)
        self.assertIsNone(r["h1_short_gt_long_as_theory"])

    def test_missing_walls_skip_h2_pair(self):
        sessions = [
            _session("2026-05-01", 100, None, None, None),
            _session("2026-05-02", 103, 104, 95, 104),
        ]
        r = bt.evaluate(sessions)
        self.assertEqual(r["h2_n"], 0)


class VerdictTest(unittest.TestCase):
    def _result(self, n, pct, p):
        return {"h2_n": n, "closer_to_nearest_wall": {"pct": pct, "p_vs_50": p}}

    def test_insufficient_sample(self):
        self.assertEqual(bt.verdict(self._result(10, 90.0, 0.001)), "INSUFFICIENT_SAMPLE")

    def test_go_when_predictive(self):
        self.assertEqual(bt.verdict(self._result(40, 60.0, 0.01)), "GO_WALLS_PREDICTIVE")

    def test_no_go_at_chance(self):
        self.assertEqual(bt.verdict(self._result(40, 30.0, 0.999)), "NO_GO_NO_EDGE")


if __name__ == "__main__":
    unittest.main()
