#!/usr/bin/env python3
"""Retired compatibility entry point; no translation model may be invoked."""

raise SystemExit(
    "翻译入口已停用：请由当前执行 agent 基于可核验原文亲自撰写中文六段式总结；"
    "不得上传文本，也不得调用本地翻译模型。"
)
