"""Tests for scripts/dex_flip.py — the mechanized +1 DEX-flip rubric line (2026-06-12 P0.4).

The regression cases are drawn from real books so the frozen rule stays anchored to the failures
it was written for:
  * MU / NBIS 2026-07-24 — both PASSED the mechanized test (with whipsaw warnings).
  * SPY / QQQ / IWM 2026-07-24 — deepening negative LEVELS with no sign change; must NOT qualify.
  * MSTR / GOOGL 2026-07-24 — a real flip 1-2 sessions ago; the "latest session" test must reject.
"""

from __future__ import annotations

import io
import json
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import dex_flip as df  # noqa: E402

B = 1_000_000_000.0


def series(pairs):
    """[(ISO date, net_dex_in_billions)] -> rows. Dates MUST be ISO; the module drops non-ISO."""
    return [{"date": d, "net_dex": v * B} for d, v in pairs]


def iso(n):
    """n consecutive ISO dates from 2026-07-07, weekends skipped (real trading sessions)."""
    from datetime import date as _d, timedelta

    out, cur = [], _d(2026, 7, 7)
    while len(out) < n:
        if cur.weekday() < 5:
            out.append(cur.isoformat())
        cur += timedelta(days=1)
    return out


_D14 = iso(14)  # 2026-07-07 .. 2026-07-24

# MU 2026-07-24, reproducing the reported pattern neg -> pos x5 -> neg x4 -> pos x3 -> neg.
# Magnitudes are chosen so the trailing-10 median |net_dex| is EXACTLY the reported 4.865B, hence
# floor 0.25 x 4.865 = 1.216B and ratio |4.06| / 1.216 = 3.3x — the numbers in the 07-24 report.
MU_2026_07_24 = series(
    list(
        zip(
            _D14,
            [-3.9, 4.2, 5.1, 4.5, 5.0, 4.8, -4.9, -5.1, -4.83, -4.9, 4.77, 3.60, 4.96, -4.06],
        )
    )
)

# NBIS 2026-07-24: prior run of exactly 3 positives (+1.207/+1.335/+1.344), flip -0.587.
# Trailing-10 median is exactly the reported 0.903B -> floor 0.226B, ratio 2.6x.
NBIS_2026_07_24 = series(
    list(
        zip(
            _D14,
            [-0.7, 0.8, 0.82, -0.85, -0.87, -0.89, -0.90, -0.902, -0.904, -0.95,
             1.207, 1.335, 1.344, -0.587],
        )
    )
)

# SPY: negative throughout and deepening — the exact "level scored as a flip" failure mode.
SPY_2026_07_24 = series(
    [
        ("2026-07-20", -3.1), ("2026-07-21", -4.24), ("2026-07-22", -8.71),
        ("2026-07-23", -50.52), ("2026-07-24", -38.43),
    ]
)

# MSTR: sign changed 07-22 -> 07-23; by 07-24 the latest session matches its predecessor.
MSTR_2026_07_24 = series(
    [
        ("2026-07-20", 0.9), ("2026-07-21", 1.102), ("2026-07-22", 0.757),
        ("2026-07-23", -0.352), ("2026-07-24", -0.506),
    ]
)


class TestSignHelpers(unittest.TestCase):
    def test_strict_sign_treats_zero_as_signless(self):
        self.assertEqual((df._sign(1.5), df._sign(-1.5), df._sign(0.0)), (1, -1, 0))

    def test_sign_changes_ignores_zeros(self):
        obs = df.normalize(series(list(zip(iso(4), [1, 0, 1, -1]))))
        self.assertEqual(df.count_sign_changes(obs), 1)


class TestNormalize(unittest.TestCase):
    def test_sorts_oldest_first_regardless_of_input_order(self):
        obs = df.normalize(series([("2026-07-24", -1), ("2026-07-21", 2), ("2026-07-22", 3)]))
        self.assertEqual([o.date for o in obs], ["2026-07-21", "2026-07-22", "2026-07-24"])

    def test_drops_rows_missing_date_or_value(self):
        obs = df.normalize(
            [{"date": "2026-07-24", "net_dex": 1.0}, {"net_dex": 2.0}, {"date": "2026-07-23"}]
        )
        self.assertEqual(len(obs), 1)

    def test_drops_unparseable_value_rather_than_coercing(self):
        self.assertEqual(len(df.normalize([{"date": "d", "net_dex": "not-a-number"}])), 0)

    def test_accepts_alternate_key_names(self):
        obs = df.normalize([{"as_of": "2026-07-24", "net_delta_exposure": 5.0}])
        self.assertEqual((obs[0].date, obs[0].net_dex), ("2026-07-24", 5.0))

    def test_tolerates_non_dict_rows(self):
        self.assertEqual(len(df.normalize(["junk", 3, None])), 0)


class TestRegressionMU(unittest.TestCase):
    def test_mu_qualifies_with_dated_evidence(self):
        r = df.evaluate("MU", MU_2026_07_24)
        self.assertTrue(r.qualifies)
        self.assertEqual(r.points, 1)
        self.assertEqual(r.direction, "short")
        self.assertEqual(r.flip_date, "2026-07-24")
        self.assertEqual(r.prior_run_dates, ("2026-07-21", "2026-07-22", "2026-07-23"))
        self.assertGreaterEqual(r.magnitude_ratio, 3.0)
        # The evidence string must cite BOTH sides, per the rubric text.
        self.assertIn("2026-07-23", r.evidence)
        self.assertIn("2026-07-24", r.evidence)

    def test_mu_carries_a_whipsaw_warning(self):
        r = df.evaluate("MU", MU_2026_07_24)
        # neg -> pos x5 -> neg x4 -> pos x3 -> neg is 4 transitions, over the advisory max of 3.
        self.assertEqual(r.sign_changes_in_window, 4)
        self.assertTrue(r.whipsaw_warning)

    def test_nbis_qualifies_but_with_a_smaller_ratio_than_mu(self):
        nbis, mu = df.evaluate("NBIS", NBIS_2026_07_24), df.evaluate("MU", MU_2026_07_24)
        self.assertTrue(nbis.qualifies)
        self.assertTrue(nbis.whipsaw_warning)
        self.assertLess(nbis.magnitude_ratio, mu.magnitude_ratio)


class TestRegressionLevelIsNotAFlip(unittest.TestCase):
    def test_spy_deepening_negative_level_does_not_qualify(self):
        r = df.evaluate("SPY", SPY_2026_07_24)
        self.assertFalse(r.qualifies)
        self.assertEqual(r.points, 0)
        self.assertIn("no sign change", r.reason)
        self.assertIn("level", r.reason)

    def test_stale_flip_two_sessions_ago_does_not_qualify(self):
        r = df.evaluate("MSTR", MSTR_2026_07_24)
        self.assertFalse(r.qualifies)
        # 07-23 is ALREADY negative (same sign as 07-24), so the opposite-signed run is ZERO:
        # the real flip happened 07-22 -> 07-23 and no longer sits on the latest session.
        self.assertEqual(r.prior_run_length, 0)
        self.assertIn("no sign change", r.reason)

    def test_all_positive_history_does_not_qualify(self):
        r = df.evaluate("AAPL", series(list(zip(iso(4), [7.5, 6.3, 4.5, 11.4]))))
        self.assertFalse(r.qualifies)


class TestMagnitudeFloor(unittest.TestCase):
    def test_sign_change_below_floor_is_rejected_as_whipsaw(self):
        rows = series(list(zip(iso(11), [10] * 10 + [-0.5])))
        r = df.evaluate("X", rows)
        self.assertFalse(r.qualifies)
        self.assertIn("magnitude below floor", r.reason)
        self.assertIn("whipsaw", r.reason)

    def test_floor_excludes_the_flip_day_from_its_own_median(self):
        # Prior |dex| all 10 -> median 10, floor 2.5. A flip of -100 must not raise its own bar.
        rows = series(list(zip(iso(11), [10] * 10 + [-100])))
        r = df.evaluate("X", rows)
        self.assertAlmostEqual(r.trailing_median_abs, 10 * 1e9)
        self.assertAlmostEqual(r.magnitude_floor, 2.5 * 1e9)
        self.assertTrue(r.qualifies)

    def test_exact_floor_is_inclusive(self):
        rows = series(list(zip(iso(11), [8] * 10 + [-2.0])))
        r = df.evaluate("X", rows)  # floor = 0.25 * 8 = 2.0
        self.assertTrue(r.qualifies)

    def test_floor_fraction_is_a_parameter(self):
        rows = series(list(zip(iso(11), [8] * 10 + [-2.0])))
        self.assertFalse(df.evaluate("X", rows, floor_frac=0.9).qualifies)


class TestGuardsAndFailClosed(unittest.TestCase):
    def test_insufficient_history_never_qualifies(self):
        r = df.evaluate("X", series(list(zip(iso(2), [5, -5]))))
        self.assertFalse(r.qualifies)
        self.assertIn("insufficient history", r.reason)

    def test_empty_input_never_qualifies(self):
        self.assertFalse(df.evaluate("X", []).qualifies)

    def test_zero_latest_has_no_sign(self):
        rows = series(list(zip(iso(4), [5, 5, 5, 0])))
        r = df.evaluate("X", rows)
        self.assertFalse(r.qualifies)
        self.assertIn("exactly 0", r.reason)

    def test_zero_reading_breaks_the_prior_run(self):
        rows = series(list(zip(iso(5), [5, 5, 0, 5, -5])))
        r = df.evaluate("X", rows)
        self.assertFalse(r.qualifies)  # only d4 is opposite-signed before the flip

    def test_min_prior_run_is_a_parameter(self):
        rows = series(list(zip(iso(3), [5, 5, -5])))
        self.assertFalse(df.evaluate("X", rows, min_prior_run=3).qualifies)
        self.assertTrue(df.evaluate("X", rows, min_prior_run=2).qualifies)

    def test_long_direction_on_a_negative_to_positive_flip(self):
        rows = series(list(zip(iso(11), [-8] * 10 + [6])))
        r = df.evaluate("X", rows)
        self.assertTrue(r.qualifies)
        self.assertEqual(r.direction, "long")


class TestFetchSeries(unittest.TestCase):
    def test_reads_net_dex_and_graceful_skips_bad_dates(self):
        def runner(argv):
            date = argv[argv.index("--date") + 1]
            if date == "2026-07-22":
                return "not json"
            if date == "2026-07-23":
                return json.dumps({"symbol": "MU"})  # no net_dex
            return json.dumps({"date": date, "net_dex": -4.06e9})

        rows, errors = fetch = df.fetch_series("MU", ["2026-07-22", "2026-07-23", "2026-07-24"], runner)
        self.assertEqual(len(rows), 1)
        self.assertEqual(len(errors), 2)
        self.assertIn("no net_dex", errors[1])

    def test_passes_symbol_and_date_to_the_cli(self):
        seen: list[list[str]] = []

        def runner(argv):
            seen.append(list(argv))
            return json.dumps({"date": "2026-07-24", "net_dex": 1.0})

        df.fetch_series("NBIS", ["2026-07-24"], runner)
        self.assertIn("--symbol", seen[0])
        self.assertIn("NBIS", seen[0])
        self.assertIn("--json", seen[0])


class TestReviewHardening(unittest.TestCase):
    def test_iso_guard_rejects_week_dates(self):
        # date.fromisoformat("2026-W30-5") parses on 3.11+ AND is length 10, so a length check alone
        # let a non-YYYY-MM-DD label through and would mis-sort the series.
        self.assertFalse(df._is_iso_date("2026-W30-5"))
        self.assertTrue(df._is_iso_date("2026-07-24"))
        for bad in ("2026-7-24", "26-07-24", "2026/07/24", "2026-07-24T10:00", "", "notadate"):
            self.assertFalse(df._is_iso_date(bad), bad)

    def test_week_date_rows_are_dropped_by_normalize(self):
        obs = df.normalize([{"date": "2026-W30-5", "net_dex": 1.0},
                            {"date": "2026-07-24", "net_dex": 2.0}])
        self.assertEqual([o.date for o in obs], ["2026-07-24"])

    def test_timestamped_dates_are_truncated_to_the_calendar_date(self):
        obs = df.normalize([{"date": "2026-07-24T20:00:00Z", "net_dex": 1.0}])
        self.assertEqual(obs[0].date, "2026-07-24")

    def test_explicit_null_primary_key_falls_back_to_the_alternate(self):
        # Eager .get(a, .get(b)) would have returned None here and dropped a usable row.
        obs = df.normalize([{"date": "2026-07-24", "net_dex": None, "net_delta_exposure": 5.0}])
        self.assertEqual(obs[0].net_dex, 5.0)

    def test_default_runner_raises_on_nonzero_exit(self):
        # A degraded `uw` call that exits non-zero but still prints plausible JSON must NOT feed a
        # scored rubric line.
        import subprocess as sp
        from unittest import mock

        completed = sp.CompletedProcess(["uw"], 1, stdout='{"net_dex": 1.0}', stderr="degraded")
        with mock.patch.object(sp, "run", return_value=completed):
            with self.assertRaises(OSError):
                df._default_runner(["uw", "options-structure", "dex"])

    def test_fetch_series_records_a_nonzero_exit_as_an_error(self):
        def bad_runner(argv):
            raise OSError("exit 1: degraded")

        rows, errors = df.fetch_series("MU", ["2026-07-24"], bad_runner)
        self.assertEqual(rows, [])
        self.assertEqual(len(errors), 1)


class TestCLI(unittest.TestCase):
    def test_file_mode_reports_qualifying_symbols(self):
        payload = {"MU": MU_2026_07_24, "SPY": SPY_2026_07_24}
        path = Path(self.enterContext(_tmpdir())) / "dex.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = df.main(["--file", str(path)])
        out = json.loads(buf.getvalue())
        self.assertEqual(rc, 0)
        self.assertEqual(out["qualifying"], ["MU"])
        self.assertEqual(len(out["results"]), 2)

    def test_missing_file_exits_zero_with_available_false(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = df.main(["--file", "/nonexistent/nope.json"])
        self.assertEqual(rc, 0)
        self.assertFalse(json.loads(buf.getvalue())["available"])


def _tmpdir():
    import tempfile

    return tempfile.TemporaryDirectory()


if __name__ == "__main__":
    unittest.main()
