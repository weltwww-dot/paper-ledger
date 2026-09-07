import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "summary_gate.py"
SPEC = importlib.util.spec_from_file_location("summary_gate", SCRIPT)
summary_gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(summary_gate)


def summary(one_line="这是中文摘要。", state="部分 · 已完成中文摘要整理"):
    return f"""# 示例总结

## 基本信息

- **内容状态**: {state}

## 一句话概括

{one_line}

## 问题与动机

当前公开材料未覆盖本节；取得全文后补充。

## 方法

当前公开材料未覆盖本节；取得全文后补充。

## 实验与结果

当前公开材料未覆盖本节；取得全文后补充。

## 贡献与局限

当前公开材料未覆盖本节；取得全文后补充。
"""


class SummaryGateTests(unittest.TestCase):
    def test_accepts_chinese_six_part_summary(self):
        self.assertEqual(summary_gate.validate_markdown("ok.md", summary()), [])

    def test_rejects_english_only_summary(self):
        errors = summary_gate.validate_markdown("english.md", summary("An English-only abstract."))
        self.assertIn("未完成中文翻译", errors[0])

    def test_rejects_missing_section(self):
        errors = summary_gate.validate_markdown("missing.md", summary().replace("## 方法", "## 方法缺失", 1))
        self.assertIn("缺少段落：方法", errors[0])

    def test_partial_summary_cannot_use_placeholder(self):
        errors = summary_gate.validate_markdown("placeholder.md", summary("摘要待补全。"))
        self.assertIn("占位符", errors[0])
