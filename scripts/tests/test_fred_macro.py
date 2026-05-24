"""Tests for scripts/fred_macro.py pure transforms and signal derivation."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import fred_macro as fm  # noqa: E402


def _obs(date, value):
    return {"date": date, "value": str(value)}


class SummarizeSeriesTest(unittest.TestCase):
    def test_yoy_computation(self):
        # 13 monthly obs, desc order: latest 310, 12mo ago 300 → +3.33%
        obs = [_obs(f"2026-{m:02d}-01", 310 - i) for i, m in enumerate(range(5, 0, -1))]
        obs += [_obs(f"2025-{m:02d}-01", 305 - i) for i, m in enumerate(range(12, 4, -1))]
        # Ensure exactly 13 points and index 12 is 12 months back.
        obs = obs[:13]
        out = fm.summarize_series("CPIAUCSL", "CPI", "monthly", "yoy", obs)
        self.assertTrue(out["available"])
        self.assertIn("yoy_pct", out)

    def test_skips_missing_dot_marker(self):
        obs = [_obs("2026-05-01", "."), _obs("2026-04-01", "2.5")]
        out = fm.summarize_series("DGS10", "10Y", "daily", "delta30", obs)
        self.assertEqual(out["latest"], 2.5)
        self.assertEqual(out["as_of"], "2026-04-01")

    def test_level_sign_inverted(self):
        out = fm.summarize_series("T10Y2Y", "spread", "daily", "level_sign",
                                  [_obs("2026-05-22", "-0.30")])
        self.assertEqual(out["sign"], "inverted")

    def test_level_sign_normal(self):
        out = fm.summarize_series("T10Y2Y", "spread", "daily", "level_sign",
                                  [_obs("2026-05-22", "0.45")])
        self.assertEqual(out["sign"], "normal")

    def test_mom_level(self):
        out = fm.summarize_series("PAYEMS", "payrolls", "monthly", "mom_level",
                                  [_obs("2026-05-01", "159200"), _obs("2026-04-01", "159050")])
        self.assertEqual(out["mom_change"], 150.0)

    def test_delta30(self):
        obs = [_obs("2026-05-22", "4.50"), _obs("2026-05-01", "4.40"),
               _obs("2026-04-15", "4.20"), _obs("2026-04-01", "4.10")]
        out = fm.summarize_series("DGS10", "10Y", "daily", "delta30", obs)
        self.assertIn("delta_30d", out)
        self.assertEqual(out["value_30d_ago"], 4.20)
        self.assertEqual(out["delta_30d"], 0.30)

    def test_unavailable_when_no_valid_points(self):
        out = fm.summarize_series("DFF", "fed funds", "daily", "level", [_obs("2026-05-01", ".")])
        self.assertFalse(out["available"])


class DeriveSignalsTest(unittest.TestCase):
    def test_signals_assembled(self):
        readings = {
            "T10Y2Y": {"available": True, "sign": "inverted", "latest": -0.2},
            "CPILFESL": {"yoy_pct": 3.1},
            "DGS10": {"available": True, "latest": 4.5, "delta_30d": 0.2},
            "DTWEXBGS": {"delta_30d": -1.0},
            "UNRATE": {"available": True, "latest": 4.1},
            "DFF": {"available": True, "latest": 4.33},
        }
        sig = fm.derive_signals(readings)
        self.assertEqual(sig["yield_curve"], "inverted")
        self.assertEqual(sig["ten_year_30d_direction"], "rising")
        self.assertEqual(sig["usd_30d_direction"], "weakening")
        self.assertEqual(sig["unemployment_rate"], 4.1)
        self.assertEqual(sig["fed_funds"], 4.33)


class BuildSnapshotTest(unittest.TestCase):
    def test_build_snapshot_with_injected_getter(self):
        def fake_getter(url):
            # Return a tiny series regardless of which id is requested.
            return {"observations": [_obs("2026-05-22", "4.50"), _obs("2026-04-01", "4.20")]}

        snap = fm.build_snapshot("KEY", 14, getter=fake_getter)
        self.assertTrue(snap["available"])
        self.assertEqual(snap["source"], "FRED")
        self.assertIn("DGS10", snap["series"])
        self.assertEqual(snap["errors"], [])

    def test_build_snapshot_records_errors(self):
        def boom(url):
            raise fm.FredError("boom")
        snap = fm.build_snapshot("KEY", 14, getter=boom)
        self.assertTrue(snap["available"])
        self.assertEqual(len(snap["errors"]), len(fm.SERIES))
        self.assertFalse(snap["series"]["DGS10"]["available"])


if __name__ == "__main__":
    unittest.main()
