#!/usr/bin/env python3
"""为尚未标注的论文补齐 1–3 个主题标签。

规则优先复用台账现有主题；确实无法用既有细分主题描述时，才使用少数上位主题
（机器学习方法、数据管理与检索、系统与网络安全等）。已有人工标签绝不改写。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "papers.js"
THEME_FILE = ROOT / "data" / "theme-tags.json"

# 主题必须是可解释的研究问题短语，而非期刊或宽泛学科名称。每篇按顺序取最多三项。
TAG_RULES: tuple[tuple[str, str], ...] = (
    ("后门与投毒", r"backdoor|data[ -]?poison|model[ -]?poison|trojan|watermark"),
    ("社会工程与钓鱼", r"phish|social engineering|human factor"),
    ("网络欺骗与蜜罐", r"cyber deception|deception|honeypot|decoy"),
    ("反欺诈", r"fraud|scam"),
    ("供应链与漏洞管理", r"supply chain|vulnerabilit|patch(?:ing)?|cve"),
    ("安全运营自动化", r"security operation|soc\b|threat intelligence|osint|incident response"),
    ("入侵检测与防御", r"intrusion|malware|threat detection|attack detection|network anomaly"),
    ("密码学", r"cryptograph|encrypt(?:ion|ed)?|cipher|signcrypt|signature|zero[ -]?knowledge|\bntru\b|lattice[- ]based|key agreement"),
    ("去中心化系统", r"blockchain|distributed ledger|decentralized"),
    ("隐私保护", r"privacy|private |differential privacy|anonymi[sz]"),
    ("通信与物联网安全", r"\b(iot|6g|5g|vanet|uav|wireless|multicast|industrial control|cyber-physical)\b"),
    ("对抗与鲁棒性", r"adversarial|robust(?:ness)?|evasion|certifi(?:able|ed)|label noise"),
    ("联邦学习", r"federated|split learning"),
    ("图神经网络", r"graph neural|\bgnn\b|graph attention|graph spectral|graph prompting"),
    ("生成模型", r"diffusion|generative|deepfake|image generation"),
    ("强化学习", r"reinforcement learning|\bdeep rl\b|multi-agent reinforcement|markov decision"),
    ("可解释AI", r"explainab|interpretab|attribution|concept-based"),
    ("偏见与公平性", r"fairness|bias|responsible ai|ai harm|ethical ai"),
    ("大模型", r"large language model|\bllm\b|foundation model|language model"),
    ("多模态学习", r"multimodal|multi-modal|vision.language|cross-modal|visible-infrared"),
    ("医学AI", r"medical|clinical|glioma|mri\b|healthcare|biomarker"),
    ("具身智能", r"robot|manipulator|autonomous driving|vehicle|motion prediction|path planning"),
    ("计算机视觉", r"image|video|visual|object detection|recognition|segmentation|re-identification|crowd counting|\bsar\b|pixel-level"),
    ("迁移学习", r"transfer learning|domain adaptation|domain generalization|cross-domain|cross-corpus"),
    ("异常检测", r"anomaly|out-of-distribution|\bood\b|fault detection"),
    ("科学计算AI", r"physics-guided|differential equation|neural operator|scientific computing|reaction-diffusion"),
    ("组合优化", r"combinatorial|optimization|clustering|scheduling|planning domain|answer set programming"),
    ("多标签学习", r"multi-label"),
    ("时间序列与预测", r"time series|forecast|prediction|soft sensing|remaining useful life|\brul\b"),
    ("自然语言处理", r"\btext\b|speech|language processing|summarization|sentiment|emotion recognition"),
    ("数据管理与检索", r"data cleaning|data quality|database|data management|vector search|nearest neighbor|query|retrieval|recommendation|knowledge graph|cache|social network"),
)


def load_papers(path: Path = DATA_FILE) -> list[dict]:
    source = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        payload = json.loads(source)
        if not isinstance(payload, list):
            raise SystemExit(f"解析失败（顶层不是数组）: {path}")
        return payload
    match = re.search(r"=\s*(\[.*\])\s*;?\s*$", source, re.S)
    if not match:
        raise SystemExit(f"解析失败: {path}")
    return json.loads(match.group(1))


def classify(paper: dict) -> list[str]:
    """Return 1–3 topic labels using title/summary evidence and paper direction."""
    text = " ".join(str(paper.get(field) or "") for field in ("title", "summary")).lower()
    tags: list[str] = []
    for tag, pattern in TAG_RULES:
        if re.search(pattern, text, re.I) and tag not in tags:
            tags.append(tag)
        if len(tags) == 3:
            return tags

    direction = str(paper.get("direction") or "")
    # Existing taxonomy did not have a precise label for every general-method, data, or
    # security paper. These fallbacks keep the hotspot denominator complete without
    # pretending that an unrelated fine-grained topic applies.
    if "数据工程" in direction:
        fallback = "数据管理与检索"
    elif "信息安全" in direction:
        fallback = "系统与网络安全"
    else:
        fallback = "机器学习方法"
    if not tags:
        tags.append(fallback)
    return tags


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    parser = argparse.ArgumentParser(description="补齐缺失的论文主题标签")
    parser.add_argument("--write", action="store_true", help="写入 data/theme-tags.json（默认只预览）")
    parser.add_argument("--input", type=Path, default=DATA_FILE, help="待分类论文 JSON 数组或 papers.js")
    args = parser.parse_args()

    themes = json.loads(THEME_FILE.read_text(encoding="utf-8")) if THEME_FILE.exists() else {}
    added: dict[str, list[str]] = {}
    for paper in load_papers(args.input):
        doi = str(paper.get("doi") or "").lower()
        if not doi or themes.get(doi):
            continue
        tags = classify(paper)
        themes[doi] = tags
        added[doi] = tags

    counts = Counter(tag for tags in added.values() for tag in tags)
    action = "将写入" if args.write else "可写入"
    print(f"{action} {len(added)} 篇缺失主题标签的论文。")
    print("本轮标签分布: " + "、".join(f"{tag} {count}" for tag, count in sorted(counts.items())))
    if args.write:
        THEME_FILE.write_text(json.dumps(themes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"已写入: {THEME_FILE}")


if __name__ == "__main__":
    main()
