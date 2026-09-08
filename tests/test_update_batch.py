import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from update_batch import UpdateBatch  # noqa: E402


class UpdateBatchTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.runs = self.root / "skill-runs"
        self.runs.mkdir()
        self.input_script = self.root / "collector.py"
        self.input_script.write_text("version = 1\n", encoding="utf-8")
        self.baseline = {"date": "2026-09-07", "dois": ["10.1/old"]}

    def tearDown(self):
        self.temporary.cleanup()

    def batch(self):
        return UpdateBatch(
            self.root,
            script_inputs=(self.input_script,),
            today=lambda: date(2026, 9, 8),
        )

    def write_collection(self, error=None):
        (self.runs / "records_inc.json").write_text("[]", encoding="utf-8")
        audit = {
            "requested_from_date": "2026-09-07",
            "until_date": "2026-09-08",
            "journals": [{"openalex": {"error": error}, "crossref": {"error": None}}],
        }
        (self.runs / "collection_audit.json").write_text(json.dumps(audit), encoding="utf-8")

    def test_completed_valid_stage_is_reusable(self):
        batch = self.batch()
        batch.begin(self.baseline, ["Known title"])
        self.write_collection()
        batch.complete("collection")

        resumed = self.batch()
        resumed.begin(self.baseline, ["Known title"])

        self.assertTrue(resumed.reusable("collection"))

    def test_changed_input_invalidates_all_stages(self):
        batch = self.batch()
        batch.begin(self.baseline, ["Known title"])
        self.write_collection()
        batch.complete("collection")
        self.input_script.write_text("version = 2\n", encoding="utf-8")

        changed = self.batch()
        changed.begin(self.baseline, ["Known title"])

        self.assertFalse(changed.reusable("collection"))

    def test_failed_audit_is_never_reused(self):
        batch = self.batch()
        batch.begin(self.baseline, [])
        self.write_collection(error="timeout")

        with self.assertRaisesRegex(ValueError, "审计无效"):
            batch.complete("collection")

    def test_damaged_artifact_is_not_reused(self):
        batch = self.batch()
        batch.begin(self.baseline, [])
        self.write_collection()
        batch.complete("collection")
        (self.runs / "records_inc.json").write_text("not json", encoding="utf-8")

        self.assertFalse(batch.reusable("collection"))

    def test_invalidation_cascades_to_later_stages(self):
        batch = self.batch()
        batch.begin(self.baseline, [])
        self.write_collection()
        batch.complete("collection")
        for name in ("oa_inc.json", "content_inc.json"):
            (self.runs / name).write_text("[]", encoding="utf-8")
        (self.runs / "content_attempts.json").write_text("{}", encoding="utf-8")
        batch.complete("oa")
        batch.complete("content")

        batch.invalidate_from("oa")

        self.assertTrue(batch.reusable("collection"))
        self.assertFalse(batch.reusable("oa"))
        self.assertFalse(batch.reusable("content"))

    def test_pdf_stage_rejects_a_missing_download(self):
        batch = self.batch()
        batch.begin(self.baseline, [])
        (self.runs / "pdf_probe.json").write_text("[]", encoding="utf-8")
        downloads = [{"status": "exists", "path": "papers/missing.pdf"}]
        (self.runs / "pdf_downloads.json").write_text(json.dumps(downloads), encoding="utf-8")
        (self.runs / "pdf_attempts.json").write_text("{}", encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "无效文件"):
            batch.complete("pdf")

    def test_artifact_shape_must_match_its_contract(self):
        batch = self.batch()
        batch.begin(self.baseline, [])
        self.write_collection()
        batch.complete("collection")
        (self.runs / "records_inc.json").write_text("{}", encoding="utf-8")

        self.assertFalse(batch.reusable("collection"))


if __name__ == "__main__":
    unittest.main()
