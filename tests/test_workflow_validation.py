import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from workflow_validation import _run_checks  # noqa: E402


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


if __name__ == "__main__":
    unittest.main()
