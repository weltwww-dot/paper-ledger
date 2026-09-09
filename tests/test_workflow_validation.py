import sys
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from workflow_validation import _layout_check, _run_checks  # noqa: E402


class WorkflowValidationTests(unittest.TestCase):
    def test_runs_checks_in_declared_order(self):
        visited = []
        checks = [
            ("first", lambda: visited.append("first") or 0, "first failed"),
            ("second", lambda: visited.append("second") or 0, "second failed"),
        ]

        _run_checks(checks, "publish 前置", lambda _message: None)

        self.assertEqual(visited, ["first", "second"])

    def test_stops_at_first_failed_check(self):
        visited = []
        checks = [
            ("first", lambda: 1, "first failed"),
            ("second", lambda: visited.append("second") or 0, "second failed"),
        ]

        with self.assertRaisesRegex(SystemExit, "first failed"):
            _run_checks(checks, "", lambda _message: None)

        self.assertEqual(visited, [])

    def test_normalizes_legacy_system_exit(self):
        def legacy_check():
            raise SystemExit(1)

        with self.assertRaisesRegex(SystemExit, "legacy failed"):
            _run_checks([("legacy", legacy_check, "legacy failed")], "", lambda _message: None)

    @patch("workflow_validation.subprocess.run")
    def test_browser_gate_runs_pdf_navigation_regression(self, run):
        run.return_value.returncode = 0
        run.return_value.stdout = ""
        run.return_value.stderr = ""

        _layout_check(lambda _message: None, "publish 前置")

        scripts = [Path(call.args[0][1]).name for call in run.call_args_list]
        self.assertEqual(
            scripts,
            ["layout-overflow-check.js", "latest-collapse-check.js", "pdf-navigation-check.js"],
        )


if __name__ == "__main__":
    unittest.main()
