import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import run_update  # noqa: E402


class RunUpdateOrchestrationTests(unittest.TestCase):
    def run_no_new(self, refresh):
        batch = Mock()
        with (
            patch.object(run_update, "fetch", return_value=([], batch)) as fetch,
            patch.object(run_update, "run"),
            patch.object(run_update, "validate_workflow"),
            patch.object(run_update, "log"),
        ):
            run_update.update(refresh=refresh)
        return fetch

    def test_update_resumes_same_day_batch_by_default(self):
        fetch = self.run_no_new(refresh=False)
        fetch.assert_called_once_with(resume=True, with_batch=True)

    def test_refresh_forces_network_stages(self):
        fetch = self.run_no_new(refresh=True)
        fetch.assert_called_once_with(resume=False, with_batch=True)

    def test_update_runs_pdf_stage_when_no_new_papers(self):
        batch = Mock()
        batch.reusable.return_value = False
        with (
            patch.object(run_update, "fetch", return_value=([], batch)),
            patch.object(run_update, "run"),
            patch.object(run_update, "acquire_pdfs") as acquire,
            patch.object(run_update, "validate_workflow"),
            patch.object(run_update, "log"),
        ):
            run_update.update(refresh=False)

        acquire.assert_called_once_with()

    def test_pdf_stage_is_reused_only_when_valid(self):
        batch = Mock()
        batch.reusable.return_value = True
        with (
            patch.object(run_update, "fetch", return_value=([{"doi": "10.1/new"}], batch)),
            patch.object(run_update, "run"),
            patch.object(run_update, "acquire_pdfs") as acquire,
            patch.object(run_update, "validate_workflow"),
            patch.object(run_update, "log"),
        ):
            run_update.update(refresh=False)

        batch.reusable.assert_called_once_with("pdf")
        acquire.assert_not_called()


if __name__ == "__main__":
    unittest.main()
