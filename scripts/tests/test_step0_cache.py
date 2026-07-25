"""Tests for scripts/step0_cache.py — the runner is injected, so no `uw` binary is invoked."""

from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import step0_cache as sc  # noqa: E402


def runner(payload='{"ok": 1}', fail_on=(), record=None):
    """Return a runner that emits ``payload`` unless the argv matches a ``fail_on`` substring."""

    def _r(argv):
        joined = " ".join(argv)
        if record is not None:
            record.append(joined)
        for frag in fail_on:
            if frag in joined:
                raise OSError(f"boom: {frag}")
        return payload

    return _r


class TestRegistryDiscipline(unittest.TestCase):
    def test_every_payload_has_at_least_two_consumers(self):
        """The 2-or-more rule is the entry bar; a single-consumer entry cannot be shared."""
        offenders = [
            p.name
            for p in sc.SHARED_PAYLOADS
            if len(p.consumers) < 2 and "funnel-seed" not in " ".join(p.consumers)
        ]
        self.assertEqual(offenders, [], f"single-consumer entries: {offenders}")

    def test_no_payload_is_per_symbol_except_the_documented_vrp_pair(self):
        """A --symbol fetch is not shareable; vrp is the exception because it has no market mode."""
        for p in sc.SHARED_PAYLOADS:
            if "--symbol" in p.args:
                self.assertTrue(p.name.startswith("vrp_"), f"{p.name} is per-symbol")

    def test_names_are_unique(self):
        names = [p.name for p in sc.SHARED_PAYLOADS]
        self.assertEqual(len(names), len(set(names)))

    def test_iv_rank_entries_use_mode_not_direction(self):
        """Regression on the exact 2026-07-24 flag trap."""
        for name in ("iv_rank_high", "iv_rank_low"):
            args = sc.BY_NAME[name].args
            self.assertIn("--mode", args)
            self.assertNotIn("--direction", args)

    def test_bullish_bearish_entries_do_use_direction(self):
        """The adjacent screener really does take --direction — that is why the trap exists."""
        self.assertIn("--direction", sc.BY_NAME["screener_bullish"].args)
        self.assertIn("--direction", sc.BY_NAME["signal_confluence_bullish"].args)

    def test_earnings_catalyst_is_registered(self):
        """The measured byte-identical duplicate must be covered."""
        self.assertIn("earnings_catalyst", sc.BY_NAME)
        self.assertGreaterEqual(len(sc.BY_NAME["earnings_catalyst"].consumers), 2)


class TestBuildArgv(unittest.TestCase):
    def test_substitutes_date_and_appends_json_flags(self):
        argv = sc.build_argv(sc.BY_NAME["sector_flow"], "2026-07-24")
        self.assertIn("2026-07-24", argv)
        self.assertEqual(argv[-2:], ["--json", "--quiet"])

    def test_substitutes_regime_for_single_leg(self):
        argv = sc.build_argv(sc.BY_NAME["single_leg"], "2026-07-24", regime="bear")
        self.assertIn("bear", argv)

    def test_payload_without_date_placeholder_is_unchanged(self):
        argv = sc.build_argv(sc.BY_NAME["market_regime"], "2026-07-24")
        self.assertNotIn("2026-07-24", argv)


class TestFetchAndCache(unittest.TestCase):
    def test_writes_each_payload_to_its_own_file(self):
        with tempfile.TemporaryDirectory() as td:
            m = sc.build_cache("2026-07-24", td, runner=runner())
            self.assertEqual(m["n_failed"], 0)
            self.assertEqual(m["n_ok"], len(sc.SHARED_PAYLOADS))
            for name, path in m["paths"].items():
                self.assertTrue(Path(path).exists(), name)
                self.assertEqual(json.loads(Path(path).read_text()), {"ok": 1})

    def test_second_run_reuses_the_cache_and_does_not_refetch(self):
        with tempfile.TemporaryDirectory() as td:
            calls: list[str] = []
            sc.build_cache("2026-07-24", td, runner=runner(record=calls))
            first = len(calls)
            m2 = sc.build_cache("2026-07-24", td, runner=runner(record=calls))
            self.assertEqual(len(calls), first, "cached run must issue zero new fetches")
            self.assertTrue(all(e["cached"] for e in m2["entries"]))

    def test_refresh_forces_a_refetch(self):
        with tempfile.TemporaryDirectory() as td:
            calls: list[str] = []
            sc.build_cache("2026-07-24", td, runner=runner(record=calls))
            n = len(calls)
            sc.build_cache("2026-07-24", td, runner=runner(record=calls), refresh=True)
            self.assertEqual(len(calls), 2 * n)

    def test_a_failing_payload_graceful_skips_without_killing_the_run(self):
        with tempfile.TemporaryDirectory() as td:
            m = sc.build_cache(
                "2026-07-24", td, runner=runner(fail_on=("earnings-catalyst",))
            )
            self.assertEqual(m["n_failed"], 1)
            self.assertEqual(m["failed"][0]["name"], "earnings_catalyst")
            self.assertNotIn("earnings_catalyst", m["paths"])
            self.assertGreater(m["n_ok"], 0)  # everything else still succeeded

    def test_non_json_body_is_rejected_before_landing_on_disk(self):
        with tempfile.TemporaryDirectory() as td:
            m = sc.build_cache("2026-07-24", td, runner=runner(payload="<html>rate limited</html>"))
            self.assertEqual(m["n_ok"], 0)
            self.assertEqual(len(list(Path(td).glob("*.json"))), 0)

    def test_only_selects_a_subset(self):
        with tempfile.TemporaryDirectory() as td:
            m = sc.build_cache("2026-07-24", td, runner=runner(), only=["iv_rank_high", "vrp_spy"])
            self.assertEqual(m["n_requested"], 2)
            self.assertEqual(set(m["paths"]), {"iv_rank_high", "vrp_spy"})

    def test_unknown_only_name_is_reported_not_crashed(self):
        with tempfile.TemporaryDirectory() as td:
            m = sc.build_cache("2026-07-24", td, runner=runner(), only=["nope", "vrp_spy"])
            self.assertEqual(m["unknown_names"], ["nope"])
            self.assertEqual(m["n_requested"], 1)

    def test_manifest_carries_the_command_for_auditability(self):
        with tempfile.TemporaryDirectory() as td:
            m = sc.build_cache("2026-07-24", td, runner=runner(), only=["iv_rank_high"])
            self.assertIn("--mode high", m["entries"][0]["command"])

    def test_creates_a_missing_output_directory(self):
        with tempfile.TemporaryDirectory() as td:
            nested = Path(td) / "a" / "b" / "step0_cache"
            m = sc.build_cache("2026-07-24", nested, runner=runner(), only=["vrp_spy"])
            self.assertEqual(m["n_ok"], 1)
            self.assertTrue(nested.exists())


class TestCacheIntegrity(unittest.TestCase):
    def test_truncated_cache_file_is_refetched_not_trusted(self):
        with tempfile.TemporaryDirectory() as td:
            bad = Path(td) / "vrp_spy.json"
            bad.parent.mkdir(parents=True, exist_ok=True)
            bad.write_text('{"truncated": ', encoding="utf-8")  # killed mid-write
            m = sc.build_cache("2026-07-24", td, runner=runner(), only=["vrp_spy"])
            self.assertTrue(m["entries"][0]["ok"])
            self.assertFalse(m["entries"][0]["cached"], "must refetch, not trust the partial file")
            self.assertEqual(json.loads(bad.read_text()), {"ok": 1})

    def test_no_tmp_files_are_left_behind(self):
        with tempfile.TemporaryDirectory() as td:
            sc.build_cache("2026-07-24", td, runner=runner(), only=["vrp_spy", "vrp_qqq"])
            self.assertEqual(list(Path(td).glob("*.tmp")), [])

    def test_valid_cache_is_still_reused(self):
        with tempfile.TemporaryDirectory() as td:
            sc.build_cache("2026-07-24", td, runner=runner(), only=["vrp_spy"])
            m = sc.build_cache("2026-07-24", td, runner=runner(), only=["vrp_spy"])
            self.assertTrue(m["entries"][0]["cached"])


class TestCLI(unittest.TestCase):
    def test_list_mode_prints_the_registry_and_exits_zero(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = sc.main(["--date", "2026-07-24", "--list"])
        out = json.loads(buf.getvalue())
        self.assertEqual(rc, 0)
        self.assertEqual(out["n_payloads"], len(sc.SHARED_PAYLOADS))

    def test_default_out_dir_follows_the_run_folder_convention(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            sc.main(["--date", "2026-07-24", "--only", "___nope___"])
        self.assertIn(
            "analyses/daily/2026-07-24/step0_cache", json.loads(buf.getvalue())["cache_dir"]
        )


if __name__ == "__main__":
    unittest.main()
