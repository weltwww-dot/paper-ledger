import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "summary_quality_gate.py"
SPEC = importlib.util.spec_from_file_location("summary_quality_gate", SCRIPT)
summary_quality_gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(summary_quality_gate)


class SummaryQualityGateTests(unittest.TestCase):
    def test_rejects_empty_public_material_placeholder(self):
        errors = summary_quality_gate.validate_markdown(
            "bad.md", "当前公开材料未覆盖本节；取得全文后补充。"
        )
        self.assertIn("无信息占位", errors[0])

    def test_rejects_manual_confirmation_wording(self):
        errors = summary_quality_gate.validate_markdown("bad.md", "待人工确认结论。")
        self.assertIn("待人工", errors[0])

    def test_rejects_unescaped_html_entity(self):
        errors = summary_quality_gate.validate_markdown("bad.md", "结果为 &lt; 1%。")
        self.assertIn("实体", errors[0])
