import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "smart_pdf.py"
SPEC = importlib.util.spec_from_file_location("smart_pdf", SCRIPT)
smart_pdf = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(smart_pdf)


class SmartPdfTests(unittest.TestCase):
    def test_arxiv_record_needs_no_network_probe(self):
        result = smart_pdf.probe({"doi": "10.1/example", "arxiv_id": "2501.01234v2"}, timeout=1)
        self.assertEqual(result["status"], "arxiv")
        self.assertEqual(result["url"], "https://arxiv.org/pdf/2501.01234")

    def test_closed_record_is_recorded_without_network_probe(self):
        result = smart_pdf.probe({"doi": "10.1/example", "is_oa": False}, timeout=1)
        self.assertEqual(result, {"doi": "10.1/example", "status": "not-oa", "url": ""})
