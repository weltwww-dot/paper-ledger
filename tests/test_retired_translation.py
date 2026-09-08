import subprocess
import sys
import unittest
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RetiredTranslationTests(unittest.TestCase):
    def test_python_entry_point_refuses_without_model_imports(self):
        result = subprocess.run(
            [sys.executable, ROOT / "scripts" / "translate_summary_abstracts_local.py"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env={**os.environ, "PYTHONUTF8": "1"},
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("翻译入口已停用", result.stderr)
        self.assertNotIn("Argos", result.stderr)


if __name__ == "__main__":
    unittest.main()
