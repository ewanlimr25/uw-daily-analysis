"""Tests for scripts/term_structure_hygiene.py.

Fixtures are REAL 2026-07-24 ``uw options-structure iv-term-structure`` rows, so the regression
anchors to the actual artifact: AKAM's ``dte_approx: 0`` bucket carries 393.3% IV, which is what
forced the raw BACKWARDATION label on 39 of 41 scanned names.
"""

from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import term_structure_hygiene as tsh  # noqa: E402


def payload(rows, structure="BACKWARDATION", kink=None):
    return {"symbol": "X", "structure": structure, "kink_expiry": kink, "term_structure": rows}


def row(dte, iv, contracts, expiry=None):
    return {
        "dte_approx": dte,
        "avg_iv": iv,
        "contract_count": contracts,
        "expiry": expiry or f"2026-exp-{dte}",
    }


# Verbatim from `uw options-structure iv-term-structure --symbol AKAM --date 2026-07-24`.
AKAM_REAL = payload(
    [
        {"avg_iv": 3.9329, "contract_count": 145, "dte_approx": 0, "expiry": "2026-07-24"},
        {"avg_iv": 0.6335, "contract_count": 337, "dte_approx": 7, "expiry": "2026-07-31"},
        {"avg_iv": 1.0511, "contract_count": 72, "dte_approx": 14, "expiry": "2026-08-07"},
        {"avg_iv": 0.9210, "contract_count": 20, "dte_approx": 21, "expiry": "2026-08-14"},
        {"avg_iv": 0.8490, "contract_count": 411, "dte_approx": 28, "expiry": "2026-08-21"},
        {"avg_iv": 0.5500, "contract_count": 71, "dte_approx": 175, "expiry": "2027-01-15"},
    ],
    structure="BACKWARDATION",
)


class TestExtraction(unittest.TestCase):
    def test_finds_the_real_term_structure_key(self):
        self.assertEqual(len(tsh.extract_tenors(AKAM_REAL)), 6)

    def test_returns_empty_for_unknown_shape(self):
        self.assertEqual(tsh.extract_tenors({"nope": [1, 2]}), [])
        self.assertEqual(tsh.extract_tenors({}), [])

    def test_normalize_sorts_by_dte_and_drops_bad_rows(self):
        rows = [row(28, 0.5, 100), row(7, 0.9, 100), {"dte_approx": 14}, row(3, 0.0, 100)]
        tenors = tsh.normalize_tenors(rows)
        self.assertEqual([t.dte for t in tenors], [7, 28])  # iv<=0 and missing-iv rows dropped

    def test_normalize_reads_alternate_key_names(self):
        tenors = tsh.normalize_tenors([{"dte": 7, "iv": 0.5, "n_contracts": 50}])
        self.assertEqual((tenors[0].dte, tenors[0].iv, tenors[0].contracts), (7, 0.5, 50))


class TestAbsentVsZeroContracts(unittest.TestCase):
    """An absent contract count must not be reported as a measured zero — that conflated missing
    data with a real liquidity finding (review finding)."""

    def test_absent_count_gets_its_own_drop_reason(self):
        rows = [{"dte_approx": 7, "avg_iv": 0.5}, row(30, 0.4, 100)]
        h = tsh.apply("T", payload(rows))
        reasons = [d["drop_reason"] for d in h.dropped]
        self.assertTrue(any("absent from payload" in r for r in reasons))
        self.assertFalse(any("contracts 0 <" in r for r in reasons))

    def test_measured_zero_is_still_untradable(self):
        rows = [row(7, 0.5, 0), row(30, 0.4, 100)]
        h = tsh.apply("T", payload(rows))
        self.assertTrue(any("contracts 0 <" in d["drop_reason"] for d in h.dropped))

    def test_explicit_null_primary_key_falls_back(self):
        rows = [{"dte": None, "dte_approx": 7, "iv": None, "avg_iv": 0.5, "contract_count": 99},
                row(30, 0.4, 100)]
        tenors = tsh.normalize_tenors(rows)
        self.assertEqual((tenors[0].dte, tenors[0].iv, tenors[0].contracts), (7, 0.5, 99))


class TestZeroDteArtifact(unittest.TestCase):
    def test_akam_raw_backwardation_becomes_kinked_after_hygiene(self):
        h = tsh.apply("AKAM", AKAM_REAL)
        self.assertEqual(h.raw_shape, "BACKWARDATION")
        self.assertEqual(h.shape, tsh.SHAPE_KINKED)
        self.assertTrue(h.flipped)
        # The kink sits at the 2026-08-07 event tenor (earnings 08-06), not at the 0DTE wing.
        self.assertEqual(h.kink_dte, 14)
        self.assertEqual(h.kink_expiry, "2026-08-07")

    def test_the_393pct_zero_dte_bucket_is_dropped_with_a_reason(self):
        h = tsh.apply("AKAM", AKAM_REAL)
        reasons = [d["drop_reason"] for d in h.dropped]
        self.assertTrue(any("0DTE/expired" in r for r in reasons))
        self.assertNotIn(0, [t.dte for t in h.tenors])

    def test_thin_tenor_dropped_by_the_contract_floor(self):
        h = tsh.apply("AKAM", AKAM_REAL)
        # The 21 DTE bucket is quoted off 20 contracts -> survives a floor of 15...
        self.assertIn(21, [t.dte for t in h.tenors])
        # ...but not a floor of 25.
        h2 = tsh.apply("AKAM", AKAM_REAL, min_contracts=25)
        self.assertNotIn(21, [t.dte for t in h2.tenors])

    def test_dropping_zero_dte_flips_a_synthetic_backwardation_to_contango(self):
        # This is the 14-of-41 mechanism in miniature: the real curve rises with DTE (contango),
        # but a 400% 0DTE wing makes the raw front-vs-next comparison read backwardation.
        rows = [row(0, 4.0, 200), row(7, 0.20, 300), row(30, 0.30, 300), row(60, 0.35, 300)]
        h = tsh.apply("T", payload(rows))
        self.assertEqual(h.raw_shape, "BACKWARDATION")
        self.assertEqual(h.shape, tsh.SHAPE_CONTANGO)
        self.assertTrue(h.flipped)


class TestClassify(unittest.TestCase):
    def test_backwardation_when_front_is_rich(self):
        rows = [row(7, 0.90, 100), row(30, 0.60, 100), row(60, 0.55, 100)]
        self.assertEqual(tsh.apply("T", payload(rows)).shape, tsh.SHAPE_BACKWARDATION)

    def test_contango_when_front_is_cheap(self):
        rows = [row(7, 0.30, 100), row(30, 0.45, 100), row(60, 0.50, 100)]
        self.assertEqual(tsh.apply("T", payload(rows)).shape, tsh.SHAPE_CONTANGO)

    def test_flat_inside_the_band(self):
        rows = [row(7, 0.500, 100), row(30, 0.4995, 100), row(60, 0.499, 100)]
        self.assertEqual(tsh.apply("T", payload(rows)).shape, tsh.SHAPE_FLAT)

    def test_kink_requires_prominence_over_both_neighbours(self):
        # +1% hump over both sides is noise, not a kink.
        rows = [row(7, 0.500, 100), row(14, 0.505, 100), row(30, 0.500, 100)]
        self.assertNotEqual(tsh.apply("T", payload(rows)).shape, tsh.SHAPE_KINKED)
        # +20% hump is a kink.
        rows2 = [row(7, 0.500, 100), row(14, 0.600, 100), row(30, 0.500, 100)]
        h = tsh.apply("T", payload(rows2))
        self.assertEqual(h.shape, tsh.SHAPE_KINKED)
        self.assertEqual(h.kink_dte, 14)

    def test_kink_wins_over_a_monotonic_label(self):
        # Front-rich overall, but a genuine mid-curve event hump must not be flattened to a slope.
        rows = [row(7, 0.80, 100), row(14, 0.95, 100), row(30, 0.60, 100), row(60, 0.55, 100)]
        self.assertEqual(tsh.apply("T", payload(rows)).shape, tsh.SHAPE_KINKED)

    def test_nearest_qualifying_kink_wins_not_the_most_prominent(self):
        # An event kink is POSITIONAL (matched to a catalyst date), so the earliest qualifying hump
        # wins even when a bigger one sits further out. Ranking by prominence instead picked SOXX's
        # 84 DTE sawtooth over its real 28 DTE OPEX-cluster hump on 2026-07-24.
        rows = [row(7, 0.50, 100), row(14, 0.60, 100), row(21, 0.50, 100),
                row(28, 0.90, 100), row(35, 0.50, 100)]
        h = tsh.apply("T", payload(rows))
        self.assertEqual(h.kink_dte, 14)
        # Both humps stay visible as candidates so the discarded one is auditable.
        self.assertEqual([c["dte"] for c in h.kink_candidates], [14, 28])

    def test_kink_beyond_the_event_window_is_ignored(self):
        # A prominent bump at 84 DTE on an otherwise-decaying curve is sawtooth noise, not an event.
        rows = [row(7, 0.80, 3120), row(28, 0.70, 1323), row(56, 0.62, 501),
                row(84, 0.69, 460), row(119, 0.64, 42)]
        h = tsh.apply("T", payload(rows))
        self.assertIsNone(h.kink_dte)
        self.assertNotEqual(h.shape, tsh.SHAPE_KINKED)
        # Raising the window admits it, proving the cap is what excluded it.
        self.assertEqual(tsh.apply("T", payload(rows), kink_max_dte=120).kink_dte, 84)

    def test_sub_threshold_humps_are_reported_as_non_qualifying_candidates(self):
        rows = [row(7, 0.500, 100), row(14, 0.505, 100), row(30, 0.500, 100)]
        h = tsh.apply("T", payload(rows))
        self.assertIsNone(h.kink_dte)
        self.assertEqual(len(h.kink_candidates), 1)
        self.assertFalse(h.kink_candidates[0]["qualifies"])

    def test_insufficient_data_with_fewer_than_two_tenors(self):
        self.assertEqual(tsh.apply("T", payload([row(7, 0.5, 100)])).shape, tsh.SHAPE_INSUFFICIENT)
        self.assertEqual(tsh.apply("T", payload([])).shape, tsh.SHAPE_INSUFFICIENT)

    def test_single_surviving_tenor_is_not_reported_as_flipped(self):
        h = tsh.apply("T", payload([row(7, 0.5, 100)]))
        self.assertFalse(h.flipped)  # INSUFFICIENT_DATA is not a contradicting classification


class TestNoNearTenorIsNotCalm(unittest.TestCase):
    def test_rmbs_class_returns_no_near_tenor(self):
        # WHR/DIOD/LDOS/COHU 2026-07-24: nothing listed under ~28 DTE despite imminent earnings.
        rows = [row(56, 0.82, 83), row(84, 0.78, 60), row(147, 0.70, 40)]
        h = tsh.apply("WHR", payload(rows))
        self.assertEqual(h.shape, tsh.SHAPE_NO_NEAR_TENOR)
        self.assertIn("UNMEASURABLE, not FLAT", h.note)

    def test_no_near_tenor_is_never_labelled_flat(self):
        rows = [row(56, 0.80, 83), row(84, 0.80, 60)]
        self.assertNotEqual(tsh.apply("X", payload(rows)).shape, tsh.SHAPE_FLAT)

    def test_whr_real_curve_starting_at_28_dte_is_caught(self):
        # WHR's real 2026-07-24 curve: first surviving tenor 28 DTE with earnings 3 days out.
        # A min-DTE test against BACK_DTE alone (30) missed this; NEAR_TENOR_MAX_DTE (21) catches it.
        rows = [row(28, 0.771, 304), row(56, 0.699, 103), row(119, 0.731, 73), row(147, 0.706, 19)]
        h = tsh.apply("WHR", payload(rows))
        self.assertEqual(h.shape, tsh.SHAPE_NO_NEAR_TENOR)
        self.assertIn("28 DTE", h.note)

    def test_a_genuine_near_tenor_is_not_misflagged(self):
        # IREN's real curve starts at 7 DTE — must classify normally, not NO_NEAR_TENOR.
        rows = [row(7, 1.387, 13585), row(14, 1.328, 2995), row(21, 1.272, 1055),
                row(28, 1.324, 8817), row(56, 1.302, 3299)]
        self.assertNotEqual(tsh.apply("IREN", payload(rows)).shape, tsh.SHAPE_NO_NEAR_TENOR)


class TestBaseShapeIsPreserved(unittest.TestCase):
    def test_kink_does_not_erase_the_monotonic_read(self):
        # AAPL 2026-07-24 shape: contango base (3d 21.2% -> long end ~30%) WITH a 7 DTE event kink.
        rows = [row(3, 0.212, 56168), row(5, 0.256, 16311), row(7, 0.409, 22299),
                row(10, 0.362, 2681), row(14, 0.344, 4261), row(28, 0.311, 11460),
                row(147, 0.305, 2685)]
        h = tsh.apply("AAPL", payload(rows))
        self.assertEqual(h.shape, tsh.SHAPE_KINKED)
        self.assertEqual(h.kink_dte, 7)
        # The monotonic read the ad-hoc 2026-07-24 run reported is retained, not overwritten.
        self.assertEqual(h.base_shape, tsh.SHAPE_CONTANGO)
        self.assertTrue(h.base_flipped)  # raw said BACKWARDATION

    def test_base_shape_matches_shape_when_there_is_no_kink(self):
        rows = [row(7, 0.90, 100), row(30, 0.60, 100)]
        h = tsh.apply("T", payload(rows))
        self.assertEqual(h.shape, h.base_shape)

    def test_report_counts_base_shapes_separately(self):
        rep = tsh.build_report({"AKAM": AKAM_REAL})
        self.assertIn("base_shape_counts", rep)
        self.assertIn("base_flipped", rep)


class TestFrontEndRatio(unittest.TestCase):
    def test_uses_hygiene_adjusted_near_and_back_tenors(self):
        rows = [row(7, 0.90, 100), row(28, 0.60, 100)]
        h = tsh.apply("T", payload(rows))
        self.assertAlmostEqual(h.front_end_ratio, 1.5, places=3)
        self.assertEqual(h.front_end_ratio_tenors, (7, 28))

    def test_zero_dte_bucket_cannot_pollute_the_ratio(self):
        with_zero = tsh.apply("T", payload([row(0, 4.0, 500), row(7, 0.90, 100), row(28, 0.60, 100)]))
        without = tsh.apply("T", payload([row(7, 0.90, 100), row(28, 0.60, 100)]))
        self.assertAlmostEqual(with_zero.front_end_ratio, without.front_end_ratio)

    def test_degenerate_pairing_returns_none_not_one(self):
        # One surviving tenor would serve both legs; a bare 1.000 is the artifact, not a reading.
        h = tsh.apply("T", payload([row(30, 0.5, 100)]))
        self.assertIsNone(h.front_end_ratio)

    def test_akam_hygiene_ratio_matches_the_manual_run_figure(self):
        # 2026-07-24 run computed 14d/28d = 105.11 / 84.90 ~ 1.24 for AKAM.
        h = tsh.apply("AKAM", AKAM_REAL, near_dte=14, back_dte=28)
        self.assertAlmostEqual(h.front_end_ratio, 1.0511 / 0.8490, places=3)
        self.assertAlmostEqual(h.front_end_ratio, 1.238, places=2)


class TestReportAndCLI(unittest.TestCase):
    def test_report_counts_flips(self):
        flipping = payload([row(0, 4.0, 200), row(7, 0.2, 300), row(30, 0.3, 300)])
        stable = payload([row(7, 0.9, 300), row(30, 0.6, 300)], structure="BACKWARDATION")
        rep = tsh.build_report({"A": flipping, "B": stable})
        self.assertEqual(rep["n_tickers"], 2)
        self.assertEqual(rep["flipped"], ["A"])
        self.assertEqual(rep["n_flipped"], 1)

    def test_report_flags_the_contract_floor_as_not_audit_frozen(self):
        rep = tsh.build_report({"A": AKAM_REAL})
        self.assertFalse(rep["params"]["min_contracts_is_audit_frozen"])

    def test_report_is_json_serializable(self):
        json.dumps(tsh.build_report({"AKAM": AKAM_REAL}))

    def test_cli_round_trip(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "ts.json"
            p.write_text(json.dumps({"AKAM": AKAM_REAL}), encoding="utf-8")
            buf = io.StringIO()
            with redirect_stdout(buf):
                rc = tsh.main(["--file", str(p)])
            out = json.loads(buf.getvalue())
        self.assertEqual(rc, 0)
        self.assertTrue(out["available"])
        self.assertEqual(out["results"][0]["shape"], tsh.SHAPE_KINKED)

    def test_cli_missing_file_exits_zero(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = tsh.main(["--file", "/nonexistent/x.json"])
        self.assertEqual(rc, 0)
        self.assertFalse(json.loads(buf.getvalue())["available"])

    def test_cli_rejects_non_object_payload(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "bad.json"
            p.write_text("[1,2,3]", encoding="utf-8")
            buf = io.StringIO()
            with redirect_stdout(buf):
                rc = tsh.main(["--file", str(p)])
        self.assertEqual(rc, 0)
        self.assertFalse(json.loads(buf.getvalue())["available"])


if __name__ == "__main__":
    unittest.main()
