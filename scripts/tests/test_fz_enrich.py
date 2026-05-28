"""Tests for scripts/fz_enrich.py parsers, field extraction, and enrichment."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import fz_enrich as fz  # noqa: E402

AS_OF = "2026-05-27"

# Trimmed real `fz quote AAPL --agent` payload (see audit 2026-05-27-fz-edge/04 §1).
AAPL_PAYLOAD = {
    "company": "Apple Inc",
    "fundamentals": {
        "Short Float": "0.92%",
        "Short Interest": "134.68M",
        "Short Ratio": "3.05",
        "Shs Float": "14.67B",
        "Shs Outstand": "14.69B",
        "Inst Own": "66.04%",
        "Inst Trans": "0.38%",
        "Insider Own": "0.12%",
        "Insider Trans": "-1.93%",
        "Recom": "1.98",
        "Target Price": "316.07",
        "Price": "310.85",
        "RSI (14)": "78.85",
        "52W High": "311.82 -0.31%",
        "Beta": "1.08",
        "Market Cap": "4565.56B",
        "Earnings": "Apr 30 AMC",
        "P/E": "37.60",          # not in field map -> dropped
    },
}


class ParserTest(unittest.TestCase):
    def test_parse_pct(self):
        self.assertEqual(fz.parse_pct("0.92%"), 0.92)
        self.assertEqual(fz.parse_pct("-1.93%"), -1.93)
        self.assertIsNone(fz.parse_pct("-"))
        self.assertIsNone(fz.parse_pct(None))

    def test_parse_num_takes_leading_token(self):
        self.assertEqual(fz.parse_num("3.05"), 3.05)
        self.assertEqual(fz.parse_num("311.82 -0.31%"), 311.82)  # composite cell
        self.assertIsNone(fz.parse_num("-"))
        self.assertEqual(fz.parse_num(42), 42.0)

    def test_parse_human_suffixes(self):
        self.assertEqual(fz.parse_human("14.67B"), 14.67e9)
        self.assertEqual(fz.parse_human("134.68M"), 134.68e6)
        self.assertEqual(fz.parse_human("500K"), 500e3)
        self.assertIsNone(fz.parse_human("-"))


class ExtractTest(unittest.TestCase):
    def test_extract_keeps_mapped_fields_only(self):
        out = fz.extract_fields(AAPL_PAYLOAD)
        self.assertEqual(out["short_float"], "0.92%")
        self.assertEqual(out["short_ratio"], "3.05")
        self.assertEqual(out["shs_float"], "14.67B")
        self.assertEqual(out["recom"], "1.98")
        self.assertEqual(out["target_price"], "316.07")
        self.assertNotIn("pe", out)  # P/E is not in the gate field map

    def test_extract_handles_missing_fundamentals(self):
        self.assertEqual(fz.extract_fields({}), {})
        self.assertEqual(fz.extract_fields({"fundamentals": "junk"}), {})


class DeriveTest(unittest.TestCase):
    def test_derive_clean_float_low_squeeze(self):
        d = fz.derive(fz.extract_fields(AAPL_PAYLOAD))
        self.assertEqual(d["short_float_pct"], 0.92)
        self.assertEqual(d["days_to_cover"], 3.05)
        self.assertEqual(d["float_shares"], 14.67e9)
        self.assertEqual(d["squeeze_pressure"], "LOW")
        # 316.07 vs 310.85 -> +1.68%
        self.assertEqual(d["upside_to_target_pct"], 1.68)

    def test_derive_high_squeeze(self):
        d = fz.derive({"short_float": "25%", "short_ratio": "8.0"})
        self.assertEqual(d["squeeze_pressure"], "HIGH")

    def test_derive_unknown_when_absent(self):
        d = fz.derive({})
        self.assertEqual(d["squeeze_pressure"], "unknown")
        self.assertIsNone(d["upside_to_target_pct"])


class EnrichTest(unittest.TestCase):
    def test_enrich_with_injected_runner(self):
        def fake_runner(ticker, binary):
            self.assertEqual(ticker, "AAPL")
            return AAPL_PAYLOAD

        out = fz.enrich("aapl", AS_OF, runner=fake_runner)
        self.assertEqual(out["ticker"], "AAPL")
        self.assertTrue(out["available"])
        self.assertTrue(out["fz_available"])
        self.assertEqual(out["fields"]["short_float"], "0.92%")
        self.assertEqual(out["derived"]["squeeze_pressure"], "LOW")
        self.assertIn("semi-monthly", out["freshness_caveat"])

    def test_skip_payload_shape(self):
        out = fz._skip("nvda", AS_OF, "fz CLI not found")
        self.assertEqual(out["ticker"], "NVDA")
        self.assertFalse(out["available"])
        self.assertFalse(out["fz_available"])
        self.assertEqual(out["skip_reason"], "fz CLI not found")


if __name__ == "__main__":
    unittest.main()
