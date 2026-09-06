import sys
import unittest
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from journal_collection import collect_journals  # noqa: E402


class JournalCollectionTests(unittest.TestCase):
    def test_crossref_only_article_is_collected_and_reported(self):
        catalog = [{"journal": "Example Journal", "openalex_issn": "1111-1111", "crossref_issn": "2222-2222"}]

        def fake_fetch(url):
            if urlparse(url).netloc == "api.openalex.org":
                return {"results": [], "meta": {"next_cursor": None}}
            self.assertNotIn("type%3Ajournal-article", url)
            self.assertIn("cursor=%2A", url)
            return {"message": {"items": [{"DOI": "10.1000/new", "title": ["Publisher-first paper"], "type": "journal-article", "published-online": {"date-parts": [[2026, 9, 6]]}}], "next-cursor": None}}

        records, audit = collect_journals(catalog, "2026-09-06", "2026-09-06", fetch_json=fake_fetch, workers=1)
        self.assertEqual([record["doi"] for record in records], ["10.1000/new"])
        self.assertEqual(audit["journals"][0]["crossref_only_dois"], ["10.1000/new"])

    def test_correction_is_not_a_collectable_article(self):
        catalog = [{"journal": "Example Journal", "openalex_issn": "1111-1111", "crossref_issn": "2222-2222"}]

        def fake_fetch(url):
            if "openalex" in url:
                return {"results": [], "meta": {"next_cursor": None}}
            return {"message": {"items": [{"DOI": "10.1000/correction", "title": ["Correction to: Original paper"], "type": "journal-article"}], "next-cursor": None}}

        records, _ = collect_journals(catalog, "2026-09-06", "2026-09-06", fetch_json=fake_fetch, workers=1)
        self.assertEqual(records, [])

    def test_adapter_failure_is_explicit_in_the_audit(self):
        catalog = [{"journal": "Example Journal", "openalex_issn": "1111-1111", "crossref_issn": "2222-2222"}]

        def fake_fetch(url):
            if "openalex" in url:
                return {"results": [], "meta": {"next_cursor": None}}
            raise OSError("publisher index unavailable")

        _, audit = collect_journals(catalog, "2026-09-06", "2026-09-06", fetch_json=fake_fetch, workers=1)
        self.assertIn("publisher index unavailable", audit["journals"][0]["crossref"]["error"])
