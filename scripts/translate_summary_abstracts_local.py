#!/usr/bin/env python3
"""Retired translation entry point; no translation model may be invoked."""

from __future__ import annotations

raise SystemExit(
    "翻译入口已停用：请由当前执行 agent 基于可核验原文亲自撰写中文六段式总结；"
    "不得上传文本，也不得调用本地翻译模型。"
)

import os
import re
from pathlib import Path

import ctranslate2
import sentencepiece as spm


ROOT = Path(__file__).resolve().parents[1]
SUMMARY_DIR = ROOT / "summaries"
MODEL_DIR = Path(
    os.environ.get(
        "PAPER_LEDGER_ARGOS_MODEL_DIR",
        r"D:\OpenSourceModels\argos-translate\packages\translate-en_zh-1_9",
    )
)
SECTION_RE = re.compile(r"(## 一句话概括\r?\n\r?\n)([\s\S]*?)(?=\r?\n## |\r?\n---)")
STATUS_RE = re.compile(r"- \*\*内容状态\*\*: 部分 · [^\r\n]+")


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?。！？])\s+", text.strip())
    result: list[str] = []
    for part in parts:
        if len(part) <= 850:
            result.append(part)
            continue
        words = part.split()
        current = ""
        for word in words:
            candidate = f"{current} {word}".strip()
            if current and len(candidate) > 700:
                result.append(current)
                current = word
            else:
                current = candidate
        if current:
            result.append(current)
    return result


def has_chinese(text: str) -> bool:
    return bool(re.search(r"[\u3400-\u9fff]", text))


def clean_translation(text: str) -> str:
    text = text.replace("▁", " ").replace("&#8217;", "’")
    text = re.sub(r"\s+([，。；：！？、）】》])", r"\1", text)
    text = re.sub(r"([（【《])\s+", r"\1", text)
    return re.sub(r"[ \t]+", " ", text).strip()


def translate(text: str, tokenizer: spm.SentencePieceProcessor, translator: ctranslate2.Translator) -> str:
    sentences = split_sentences(text)
    tokenized = [tokenizer.encode(sentence, out_type=str) for sentence in sentences]
    translated_batches = translator.translate_batch(
        tokenized,
        beam_size=4,
        replace_unknowns=True,
        batch_type="tokens",
        max_batch_size=32,
    )
    outputs = [tokenizer.decode(batch.hypotheses[0]) for batch in translated_batches]
    return clean_translation("".join(outputs))


def main() -> None:
    raise SystemExit(
        "翻译入口已停用：请由当前执行 agent 基于可核验原文亲自撰写中文六段式总结；"
        "不得上传文本，也不得调用本地翻译模型。"
    )

    model_path = MODEL_DIR / "model"
    sentencepiece_path = MODEL_DIR / "sentencepiece.model"
    if not model_path.is_dir() or not sentencepiece_path.is_file():
        raise SystemExit(
            "找不到本地 Argos 英译中模型。请检查 PAPER_LEDGER_ARGOS_MODEL_DIR 或默认路径: "
            f"{MODEL_DIR}"
        )

    tokenizer = spm.SentencePieceProcessor(model_file=str(sentencepiece_path))
    translator = ctranslate2.Translator(
        str(model_path), device="cpu", compute_type="int8", inter_threads=1
    )

    changed = 0
    for file in sorted(SUMMARY_DIR.glob("*.md")):
        markdown = file.read_text(encoding="utf-8")
        match = SECTION_RE.search(markdown)
        if not match:
            continue
        source = match.group(2).strip()
        if not source:
            continue
        translated = clean_translation(source) if has_chinese(source) else translate(source, tokenizer, translator)
        if not translated or not has_chinese(translated):
            raise RuntimeError(f"本地模型未返回有效中文: {file.name}")
        next_markdown = markdown[: match.start(2)] + translated + "\n" + markdown[match.end(2) :]
        next_markdown = STATUS_RE.sub(
            "- **内容状态**: 部分 · 已完成中文摘要整理；公开材料未覆盖的段落将在取得全文后补充",
            next_markdown,
            count=1,
        )
        if next_markdown != markdown:
            file.write_text(next_markdown, encoding="utf-8")
            changed += 1
            print(f"[{changed}] {file.name}")

    print(f"本地 Argos 模型完成 {changed} 篇摘要翻译。模型目录: {MODEL_DIR}")


if __name__ == "__main__":
    main()
