"""Tests for scripts/zerodte_setup.py pure-math core (no duckdb required).

The duckdb I/O shell (_reconstruct) needs the parquet and is not unit tested; the
VRP / sizing / GEX-range / recommend math is pure and fully covered here.
"""

import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import zerodte_setup as z  # noqa: E402


def _session(implied, oc, rng, cc, vix, gex_sign):
    return {"implied_move": implied, "oc": oc, "rng": rng, "cc": cc, "vix": vix, "gex_sign": gex_sign}


class CoreMathTest(unittest.TestCase):
    def test_implied_move_scales_with_iv(self):
        self.assertAlmostEqual(z.implied_move_pct(0.16), 0.16 * math.sqrt(1 / 252) * 100, places=6)
        self.assertGreater(z.implied_move_pct(0.30), z.implied_move_pct(0.15))

    def test_straddle_pnl_sign(self):
        # collect 0.8*1.0=0.8, pay 0.4 realized -> +0.4 (seller wins)
        self.assertAlmostEqual(z.straddle_pnl_pct(1.0, 0.4), 0.4)
        # big realized move -> seller loses
        self.assertLess(z.straddle_pnl_pct(1.0, 1.5), 0)

    def test_vol_state_terciles(self):
        bounds = z.vix_terciles([15, 16, 17, 18, 19, 20, 25, 30, 35])
        self.assertEqual(z.vol_state(15, bounds), "LOW")
        self.assertEqual(z.vol_state(35, bounds), "HIGH")
        self.assertEqual(z.vol_state(None, bounds), "UNKNOWN")


class EvaluateTest(unittest.TestCase):
    def _book(self, n, oc, vix, gex_sign):
        # implied fixed at 1.0%, range 0.9% ; realized oc as given
        return [_session(1.0, oc, 0.9, oc, vix, gex_sign) for _ in range(n)]

    def test_premium_seller_edge_go(self):
        # 30 quiet days: realized oc 0.4% < implied 1.0% -> seller wins all
        r = z.evaluate(self._book(30, 0.4, 20, 1))
        self.assertEqual(r["premium_sell_win_open_pct"], 100.0)
        self.assertGreater(r["mean_pnl_open_pct"], 0)
        self.assertEqual(r["verdict"], "GO_PREMIUM_SELL_INTRADAY")

    def test_no_edge_when_realized_exceeds_implied(self):
        r = z.evaluate(self._book(30, 1.5, 20, 1))  # realized 1.5 > implied 1.0
        self.assertEqual(r["premium_sell_win_open_pct"], 0.0)
        self.assertEqual(r["verdict"], "NO_GO_NO_EDGE")

    def test_insufficient_sample(self):
        self.assertEqual(z.evaluate(self._book(10, 0.4, 20, 1))["verdict"], "INSUFFICIENT_SAMPLE")
        self.assertEqual(z.evaluate([])["verdict"], "INSUFFICIENT_SAMPLE")

    def test_gex_range_buckets(self):
        sess = ([_session(1.0, 0.4, 0.7, 0.4, 20, 1) for _ in range(10)]   # long-gamma: quiet (0.7)
                + [_session(1.0, 0.4, 1.2, 0.4, 20, -1) for _ in range(10)])  # short-gamma: wide (1.2)
        r = z.evaluate(sess)
        self.assertLess(r["long_gamma_mean_range_pct"], r["short_gamma_mean_range_pct"])

    def test_overnight_loses_when_gap_big(self):
        # open-entry wins (oc 0.4) but overnight cc 1.5 (gap) loses
        sess = [_session(1.0, 0.4, 0.9, 1.5, 20, 1) for _ in range(25)]
        r = z.evaluate(sess)
        self.assertGreater(r["mean_pnl_open_pct"], 0)
        self.assertLess(r["mean_pnl_overnight_pct"], 0)


class RecommendTest(unittest.TestCase):
    def _ctx(self):
        return {"vix_tercile_bounds": [17.0, 22.0],
                "long_gamma_mean_range_pct": 0.75, "short_gamma_mean_range_pct": 1.05}

    def _latest(self, **over):
        base = {"symbol": "SPY", "spot": 745.0, "implied_move": 1.0, "vix": 19.0,
                "vix_prev": 18.5, "gex_sign": 1, "front_iv": 0.16,
                "zero_gamma_level": 744.0, "call_wall": 746, "put_wall": 730}
        base.update(over)
        return base

    def test_long_gamma_mid_vix_sells(self):
        r = z.recommend(self._latest(), self._ctx())
        self.assertTrue(r["sell_premium"])
        self.assertEqual(r["vol_state"], "MID")
        self.assertEqual(r["size_scalar"], 1.0)
        self.assertEqual(r["expected_range_pct"], 0.75)
        self.assertIn("iron fly", r["suggested_structure"])

    def test_high_vix_sizes_up(self):
        r = z.recommend(self._latest(vix=30.0, vix_prev=29.5), self._ctx())
        self.assertEqual(r["vol_state"], "HIGH")
        self.assertEqual(r["size_scalar"], 1.5)

    def test_vix_spike_stands_aside(self):
        r = z.recommend(self._latest(vix=24.0, vix_prev=20.0), self._ctx())  # +4 jump
        self.assertFalse(r["sell_premium"])
        self.assertEqual(r["size_scalar"], 0.0)
        self.assertIn("spiking", r["stand_aside_reason"])

    def test_backwardation_halves_size(self):
        # front_iv 0.30 vs vix 0.19 -> ratio 1.58 >= 1.25 -> caution, half size
        r = z.recommend(self._latest(front_iv=0.30), self._ctx())
        self.assertIsNotNone(r["caution"])
        self.assertEqual(r["size_scalar"], 0.5)  # MID 1.0 * 0.5

    def test_short_gamma_uses_wider_range(self):
        r = z.recommend(self._latest(gex_sign=-1), self._ctx())
        self.assertEqual(r["expected_range_pct"], 1.05)
        self.assertIn("condor", r["suggested_structure"])


if __name__ == "__main__":
    unittest.main()
