import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "route_check.py"
SPEC = importlib.util.spec_from_file_location("route_check", SCRIPT)
route_check = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(route_check)


class RouteCheckTests(unittest.TestCase):
    def test_publisher_domains_require_direct_bypass(self):
        missing = route_check.no_proxy_missing("elsevier.com,ieee.org")
        self.assertIn("springer.com", missing)
        self.assertIn("sciencedirectassets.com", missing)

    def test_complete_bypass_list_passes_domain_check(self):
        no_proxy = ",".join(route_check.NO_PROXY_SUFFIXES)
        self.assertEqual(route_check.no_proxy_missing(no_proxy), [])

    def test_proxy_redaction_hides_credentials_and_query(self):
        shown = route_check.redact_proxy("http://user:secret@127.0.0.1:7890/?token=hidden")
        self.assertEqual(shown, "http://127.0.0.1:7890")
