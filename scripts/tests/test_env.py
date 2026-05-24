"""Tests for scripts/_env.py key resolution."""

import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _env  # noqa: E402


class ParseEnvFileTest(unittest.TestCase):
    def test_missing_file_returns_empty(self):
        self.assertEqual(_env._parse_env_file(Path("/no/such/.env")), {})

    def test_parses_keys_skips_comments_and_quotes(self, ):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / ".env"
            p.write_text(
                "# comment\n"
                "\n"
                'FINNHUB_API_KEY="abc123"\n'
                "FRED_API_KEY = bcd \n"
                "MALFORMED_LINE\n"
                "EMPTY=\n"
            )
            parsed = _env._parse_env_file(p)
        self.assertEqual(parsed["FINNHUB_API_KEY"], "abc123")
        self.assertEqual(parsed["FRED_API_KEY"], "bcd")
        self.assertEqual(parsed["EMPTY"], "")
        self.assertNotIn("MALFORMED_LINE", parsed)


class GetKeyTest(unittest.TestCase):
    def setUp(self):
        self._saved = os.environ.get("FRED_API_KEY")
        os.environ.pop("FRED_API_KEY", None)

    def tearDown(self):
        if self._saved is not None:
            os.environ["FRED_API_KEY"] = self._saved
        else:
            os.environ.pop("FRED_API_KEY", None)

    def test_env_takes_priority(self):
        os.environ["FRED_API_KEY"] = "from_env"
        self.assertEqual(_env.get_key("FRED_API_KEY"), "from_env")
        self.assertTrue(_env.has_key("FRED_API_KEY"))

    def test_missing_everywhere_returns_empty(self):
        self.assertEqual(_env.get_key("DEFINITELY_NOT_A_REAL_KEY_XYZ"), "")
        self.assertFalse(_env.has_key("DEFINITELY_NOT_A_REAL_KEY_XYZ"))

    def test_whitespace_only_env_falls_through(self):
        os.environ["FRED_API_KEY"] = "   "
        # Should not return the whitespace value; falls to repo .env / empty.
        self.assertNotEqual(_env.get_key("FRED_API_KEY"), "   ")


if __name__ == "__main__":
    unittest.main()
