import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "workflow_gate.py"
SPEC = importlib.util.spec_from_file_location("workflow_gate", SCRIPT)
workflow_gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(workflow_gate)


class WorkflowGateTests(unittest.TestCase):
    def test_accepts_non_research_audit_record(self):
        self.assertIsNone(
            workflow_gate.validate_attempt(
                "10.1/example",
                {"reason": "non_research_document", "note": "核验为非研究性投稿须知页。"},
            )
        )

    def test_rejects_missing_audit_note(self):
        self.assertIn(
            "note",
            workflow_gate.validate_attempt(
                "10.1/example", {"reason": "blocked", "note": ""}
            ),
        )

    def test_rejects_pdf_outside_papers_directory(self):
        ok, detail = workflow_gate.valid_pdf_path("../outside.pdf")
        self.assertFalse(ok)
        self.assertIn("papers/", detail)

    def test_allowed_reasons_are_explicit(self):
        self.assertIsNotNone(
            workflow_gate.validate_attempt("10.1/example", {"reason": "unknown", "note": "证据"})
        )
