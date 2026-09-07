import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch
from urllib.parse import urlparse

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from fetch_incremental import effective_start_date  # noqa: E402
from journal_collection import collect_journals, load_catalog  # noqa: E402
import run_update  # noqa: E402


CATALOG = [{"journal": "Example Journal", "openalex_issn": "1111-1111", "crossref_issn": "2222-2222"}]


class JournalCollectionTests(unittest.TestCase):
    def test_crossref_only_article_is_collected_and_reported(self):
        def fake_fetch(url):
            if urlparse(url).netloc == "api.openalex.org":
                return {"results": [], "meta": {"next_cursor": None}}
            self.assertNotIn("type%3Ajournal-article", url)
            self.assertIn("cursor=%2A", url)
            return {"message": {"items": [{"DOI": "10.1000/new", "title": ["Publisher-first paper"], "type": "journal-article", "published-online": {"date-parts": [[2026, 9, 6]]}}], "next-cursor": None}}

        records, audit = collect_journals(CATALOG, "2026-09-06", "2026-09-06", fetch_json=fake_fetch, workers=1)

        self.assertEqual([record["doi"] for record in records], ["10.1000/new"])
        self.assertEqual(audit["journals"][0]["crossref_only_dois"], ["10.1000/new"])

    def test_correction_is_excluded_with_an_audit_reason(self):
        def fake_fetch(url):
            if "openalex" in url:
                return {"results": [], "meta": {"next_cursor": None}}
            return {"message": {"items": [{"DOI": "10.1000/correction", "title": ["Correction to: Original paper"], "type": "journal-article"}], "next-cursor": None}}

        records, audit = collect_journals(CATALOG, "2026-09-06", "2026-09-06", fetch_json=fake_fetch, workers=1)

        self.assertEqual(records, [])
        self.assertEqual(audit["journals"][0]["crossref"]["excluded"], {"title:correction": 1})

    def test_article_with_society_in_its_title_is_not_filtered(self):
        def fake_fetch(url):
            if "openalex" in url:
                return {"results": [], "meta": {"next_cursor": None}}
            return {"message": {"items": [{"DOI": "10.1000/society", "title": ["Security for a Digital Society"], "type": "journal-article", "published-online": {"date-parts": [[2026, 9, 6]]}}], "next-cursor": None}}

        records, _ = collect_journals(CATALOG, "2026-09-06", "2026-09-06", fetch_json=fake_fetch, workers=1)

        self.assertEqual([record["doi"] for record in records], ["10.1000/society"])

    def test_online_date_beats_a_later_print_date(self):
        def fake_fetch(url):
            if "openalex" in url:
                return {"results": [{"doi": "https://doi.org/10.1000/date", "display_name": "Date precedence", "publication_year": 2026, "publication_date": "2026-09-05", "type": "article"}], "meta": {"next_cursor": None}}
            return {"message": {"items": [{"DOI": "10.1000/date", "title": ["Date precedence"], "type": "journal-article", "published-print": {"date-parts": [[2026, 10, 1]]}}], "next-cursor": None}}

        records, _ = collect_journals(CATALOG, "2026-09-01", "2026-10-01", fetch_json=fake_fetch, workers=1)

        self.assertEqual(records[0]["date"], "2026-09-05")

    def test_same_doi_from_two_catalog_entries_is_collected_once(self):
        catalog = [
            {"journal": "Example Journal A", "openalex_issn": "1111-1111", "crossref_issn": "2222-2222"},
            {"journal": "Example Journal B", "openalex_issn": "3333-3333", "crossref_issn": "4444-4444"},
        ]

        def fake_fetch(url):
            if "openalex" in url:
                return {"results": [{"doi": "https://doi.org/10.1000/shared", "display_name": "Shared result", "publication_year": 2026, "publication_date": "2026-09-06", "type": "article"}], "meta": {"next_cursor": None}}
            return {"message": {"items": [], "next-cursor": None}}

        records, _ = collect_journals(catalog, "2026-09-06", "2026-09-06", fetch_json=fake_fetch, workers=1)

        self.assertEqual([record["doi"] for record in records], ["10.1000/shared"])

    def test_jcs_crossref_issn_uses_the_journal_issn(self):
        catalog_path = Path(__file__).resolve().parents[1] / "data" / "journals.json"
        catalog = load_catalog(catalog_path)
        journal = next(item for item in catalog if item["journal"] == "Journal of Computer Security")

        self.assertEqual(journal["crossref_issn"], "1875-8924")

    def test_adapter_failure_is_explicit_in_the_audit(self):
        def fake_fetch(url):
            if "openalex" in url:
                return {"results": [], "meta": {"next_cursor": None}}
            raise OSError("publisher index unavailable")

        _, audit = collect_journals(CATALOG, "2026-09-06", "2026-09-06", fetch_json=fake_fetch, workers=1)

        self.assertIn("publisher index unavailable", audit["journals"][0]["crossref"]["error"])

    def test_lookback_does_not_expand_before_the_baseline(self):
        self.assertEqual(effective_start_date("2026-09-06", 7, date(2026, 9, 7)), "2026-08-31")
        self.assertEqual(effective_start_date("2026-08-01", 7, date(2026, 9, 7)), "2026-08-01")

    def test_failed_collection_audit_blocks_follow_up_steps(self):
        with tempfile.TemporaryDirectory() as temporary:
            audit_path = Path(temporary) / "collection_audit.json"
            audit_path.write_text(json.dumps({"journals": [{"journal": "Example Journal", "openalex": {"error": "timeout"}, "crossref": {"error": None}}]}), encoding="utf-8")
            with patch.object(run_update, "COLLECTION_AUDIT", audit_path):
                with self.assertRaisesRegex(SystemExit, "Example Journal"):
                    run_update.require_successful_collection_audit()


if __name__ == "__main__":
    unittest.main()
