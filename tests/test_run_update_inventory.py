import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import run_update  # noqa: E402


class RunUpdateInventoryTests(unittest.TestCase):
    def test_fetch_excludes_entries_staged_after_the_last_update_baseline(self):
        """A stale baseline must not rediscover papers already present locally."""
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            runs = root / "skill-runs"
            summaries = root / "summaries"
            data = root / "data"
            runs.mkdir()
            summaries.mkdir()
            data.mkdir()

            baseline = {"date": "2026-09-13", "dois": ["10.1000/baseline"]}
            (runs / "last_update.json").write_text(json.dumps(baseline), encoding="utf-8")
            papers = [
                {"doi": "10.1000/baseline", "title": "Baseline paper"},
                {"doi": "10.1000/staged", "title": "Staged in ledger"},
            ]
            (data / "papers.js").write_text(
                "window.PAPERLEDGER_SEED = " + json.dumps(papers) + ";\n",
                encoding="utf-8",
            )
            (summaries / "pending.md").write_text(
                "# Summary-only paper 总结\n\n"
                "- **标题**: Summary-only paper\n"
                "- **DOI**: 10.1000/summary-only\n",
                encoding="utf-8",
            )

            captured = {}

            def fake_run(command, cwd=None):
                command = [str(part) for part in command]
                script = Path(command[1]).name
                if script == "fetch_incremental.py":
                    doi_file = Path(command[command.index("--existing-dois-file") + 1])
                    title_file = Path(command[command.index("--existing-titles-file") + 1])
                    captured["dois"] = json.loads(doi_file.read_text(encoding="utf-8"))
                    captured["titles"] = json.loads(title_file.read_text(encoding="utf-8"))
                    Path(command[command.index("--out") + 1]).write_text("[]", encoding="utf-8")
                    Path(command[command.index("--audit") + 1]).write_text(
                        json.dumps(
                            {
                                "requested_from_date": "2026-09-13",
                                "until_date": date.today().isoformat(),
                                "journals": [
                                    {
                                        "journal": "Example Journal",
                                        "openalex": {"error": None},
                                        "crossref": {"error": None},
                                    }
                                ],
                            }
                        ),
                        encoding="utf-8",
                    )
                elif script == "oa_check.py":
                    Path(command[command.index("-o") + 1]).write_text("[]", encoding="utf-8")
                elif script == "fetch_content.py":
                    Path(command[command.index("-o") + 1]).write_text("[]", encoding="utf-8")
                    Path(command[command.index("--attempts") + 1]).write_text("{}", encoding="utf-8")
                else:
                    self.fail(f"unexpected command: {command}")

            with (
                patch.object(run_update, "ROOT", root),
                patch.object(run_update, "RUNS", runs),
                patch.object(run_update, "LAST_UPDATE", runs / "last_update.json"),
                patch.object(run_update, "DATA_FILE", data / "papers.js"),
                patch.object(run_update, "COLLECTION_AUDIT", runs / "collection_audit.json"),
                patch.object(run_update, "SUMMARIES", summaries, create=True),
                patch.object(run_update, "BATCH_INPUTS", ()),
                patch.object(run_update, "log"),
                patch.object(run_update, "run", side_effect=fake_run),
            ):
                run_update.fetch()

            self.assertEqual(
                {item.lower() for item in captured["dois"]},
                {"10.1000/baseline", "10.1000/staged", "10.1000/summary-only"},
            )
            self.assertEqual(
                set(captured["titles"]),
                {"Baseline paper", "Staged in ledger", "Summary-only paper"},
            )


if __name__ == "__main__":
    unittest.main()
