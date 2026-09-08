#!/usr/bin/env python3
"""Own resumable artifacts for one daily update batch.

The batch is reusable only while its baseline, catalog, baseline titles and
fetch implementations are unchanged.  Each stage also validates its JSON
artifacts before reuse; a stale or damaged stage invalidates everything after
it so network work is never skipped on ambiguous evidence.
"""

from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path
from typing import Callable


STAGES = ("collection", "oa", "content", "pdf")
ARTIFACT_FILES = {
    "records": "records_inc.json",
    "audit": "collection_audit.json",
    "oa": "oa_inc.json",
    "content": "content_inc.json",
    "content_attempts": "content_attempts.json",
    "pdf_probe": "pdf_probe.json",
    "pdf_downloads": "pdf_downloads.json",
    "pdf_attempts": "pdf_attempts.json",
}
ARTIFACT_TYPES = {
    "records": list,
    "audit": dict,
    "oa": list,
    "content": list,
    "content_attempts": dict,
    "pdf_probe": list,
    "pdf_downloads": list,
    "pdf_attempts": dict,
}
STAGE_ARTIFACTS = {
    "collection": ("records", "audit"),
    "oa": ("oa",),
    "content": ("content", "content_attempts"),
    "pdf": ("pdf_probe", "pdf_downloads", "pdf_attempts"),
}


class UpdateBatch:
    """Small interface over validation, invalidation and atomic batch state."""

    def __init__(
        self,
        root: Path,
        *,
        script_inputs: tuple[Path, ...] = (),
        today: Callable[[], date] = date.today,
    ) -> None:
        self.root = Path(root)
        self.runs = self.root / "skill-runs"
        self.receipt_path = self.runs / "update_batch.json"
        self.script_inputs = tuple(Path(path) for path in script_inputs)
        self.today = today
        self.receipt: dict = {}

    def begin(self, baseline: dict, baseline_titles: list[str]) -> None:
        identity = {
            "schema": 1,
            "run_date": self.today().isoformat(),
            "baseline_date": baseline.get("date"),
            "fingerprint": self._fingerprint(baseline, baseline_titles),
        }
        previous = self._load_receipt()
        if all(previous.get(key) == value for key, value in identity.items()):
            self.receipt = previous
            self.receipt.setdefault("stages", {})
            return
        self.receipt = {**identity, "stages": {}}
        self._save()

    def reusable(self, stage: str) -> bool:
        self._require_stage(stage)
        if not self.receipt.get("stages", {}).get(stage, {}).get("complete"):
            return False
        if not all(self._valid_json(self.path(name), ARTIFACT_TYPES[name]) for name in STAGE_ARTIFACTS[stage]):
            return False
        if stage == "collection" and not self._valid_collection_audit():
            return False
        if stage == "pdf" and not self._valid_pdf_downloads():
            return False
        return True

    def invalidate_from(self, stage: str) -> None:
        self._require_stage(stage)
        start = STAGES.index(stage)
        stages = self.receipt.setdefault("stages", {})
        for name in STAGES[start:]:
            stages.pop(name, None)
        self._save()

    def complete(self, stage: str) -> None:
        self._require_stage(stage)
        if not all(self._valid_json(self.path(name), ARTIFACT_TYPES[name]) for name in STAGE_ARTIFACTS[stage]):
            raise ValueError(f"{stage} 阶段产物缺失或不是有效 JSON")
        if stage == "collection" and not self._valid_collection_audit():
            raise ValueError("期刊来源审计无效，不能标记为可复用")
        if stage == "pdf" and not self._valid_pdf_downloads():
            raise ValueError("PDF 下载记录指向缺失或无效文件，不能标记为可复用")
        self.receipt.setdefault("stages", {})[stage] = {
            "complete": True,
            "completed_at": self.today().isoformat(),
        }
        self._save()

    def path(self, artifact: str) -> Path:
        """Resolve one canonical batch artifact without leaking file names to callers."""
        try:
            return self.runs / ARTIFACT_FILES[artifact]
        except KeyError as exc:
            raise ValueError(f"未知批次产物: {artifact}") from exc

    def _fingerprint(self, baseline: dict, baseline_titles: list[str]) -> str:
        digest = hashlib.sha256()
        stable_input = {
            "baseline": baseline,
            "baseline_titles": sorted(title.strip() for title in baseline_titles if title.strip()),
        }
        digest.update(json.dumps(stable_input, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        for path in sorted(self.script_inputs, key=lambda item: str(item).lower()):
            digest.update(str(path).encode("utf-8"))
            if not path.is_file():
                digest.update(b"<missing>")
            else:
                digest.update(path.read_bytes())
        return digest.hexdigest()

    def _valid_collection_audit(self) -> bool:
        try:
            audit = json.loads(self.path("audit").read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError):
            return False
        if audit.get("requested_from_date") != self.receipt.get("baseline_date"):
            return False
        if audit.get("until_date") != self.receipt.get("run_date"):
            return False
        journals = audit.get("journals")
        if not isinstance(journals, list) or not journals or not all(isinstance(item, dict) for item in journals):
            return False
        for journal in journals:
            for source in ("openalex", "crossref"):
                source_audit = journal.get(source)
                if not isinstance(source_audit, dict) or source_audit.get("error"):
                    return False
        return True

    def _valid_pdf_downloads(self) -> bool:
        try:
            downloads = json.loads(self.path("pdf_downloads").read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError):
            return False
        for item in downloads:
            if not isinstance(item, dict):
                return False
            if item.get("status") not in {"downloaded", "exists"}:
                continue
            raw_path = str(item.get("path") or "").strip()
            path = Path(raw_path)
            if not path.is_absolute():
                path = self.root / path
            try:
                with path.open("rb") as handle:
                    head = handle.read(5)
                    handle.seek(max(0, path.stat().st_size - 16))
                    tail = handle.read(16)
            except OSError:
                return False
            if not head.startswith(b"%PDF") or b"%EOF" not in tail:
                return False
        return True

    @staticmethod
    def _valid_json(path: Path, expected_type: type) -> bool:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            return isinstance(payload, expected_type)
        except (OSError, UnicodeError, json.JSONDecodeError):
            return False

    def _load_receipt(self) -> dict:
        try:
            payload = json.loads(self.receipt_path.read_text(encoding="utf-8"))
            return payload if isinstance(payload, dict) else {}
        except (OSError, UnicodeError, json.JSONDecodeError):
            return {}

    def _save(self) -> None:
        self.runs.mkdir(parents=True, exist_ok=True)
        temporary = self.receipt_path.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(self.receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        temporary.replace(self.receipt_path)

    @staticmethod
    def _require_stage(stage: str) -> None:
        if stage not in STAGES:
            raise ValueError(f"未知更新阶段: {stage}")
