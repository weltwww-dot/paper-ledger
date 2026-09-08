import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "enrich_incomplete_summaries.py"
SPEC = importlib.util.spec_from_file_location("enrich_incomplete_summaries", SCRIPT)
enricher = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(enricher)


def fixture(summary):
    return f"""# Example

## 基本信息

- **标题**: Reliable graph learning
- **内容状态**: 部分 · 旧说明
- **研究方向**: 人工智能
- **DOI**: 10.1/example

## 一句话概括

{summary}

## 问题与动机

当前公开材料未覆盖本节；取得全文后补充。

## 方法

当前公开材料未覆盖本节；取得全文后补充。

## 实验与结果

当前公开材料未覆盖本节；取得全文后补充。

## 贡献与局限

当前公开材料未覆盖本节；取得全文后补充。

---
DOI: 10.1/example
"""


class EnrichIncompleteSummariesTests(unittest.TestCase):
    def test_redistributes_existing_abstract_without_placeholder(self):
        source = "现有方法在动态图上容易失效。本文提出图谱调度框架。实验结果表明该方法降低了零召回节点。该研究为可靠学习提供了新方案。"

        result = enricher.transform(fixture(source), {"10.1/example": ["图神经网络"]})

        self.assertNotIn("当前公开材料未覆盖本节", result)
        self.assertIn("本文提出图谱调度框架", enricher.section(result, "方法"))
        self.assertIn("降低了零召回节点", enricher.section(result, "实验与结果"))

    def test_metadata_only_draft_marks_inference_limit(self):
        result = enricher.transform(
            fixture("当前未获取可核验摘要；取得可核验内容后补充。"),
            {"10.1/example": ["图神经网络", "联邦学习"]},
        )

        self.assertNotIn("当前公开材料未覆盖本节", result)
        self.assertIn("从题目可判断", enricher.section(result, "问题与动机"))
        self.assertIn("不补写未经证实的结果", enricher.section(result, "实验与结果"))


if __name__ == "__main__":
    unittest.main()
