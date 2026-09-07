import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "fill_theme_tags.py"
SPEC = importlib.util.spec_from_file_location("fill_theme_tags", SCRIPT)
classifier = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(classifier)


class ThemeTagTests(unittest.TestCase):
    def test_preserves_specific_security_topics(self):
        tags = classifier.classify({"title": "Federated Unlearning Activated Backdoor Attacks", "summary": "", "direction": "信息安全"})
        self.assertIn("后门与投毒", tags)
        self.assertIn("联邦学习", tags)

    def test_classifies_data_engineering_fallback(self):
        tags = classifier.classify({"title": "A scalable storage engine", "summary": "", "direction": "数据工程"})
        self.assertEqual(tags, ["数据管理与检索"])

    def test_classifies_general_ai_fallback(self):
        tags = classifier.classify({"title": "A new neural architecture", "summary": "", "direction": "人工智能"})
        self.assertEqual(tags, ["机器学习方法"])
