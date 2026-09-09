#!/bin/bash
# 顺序跑若干 InstSci 批次；每个批次独立日志；命中 WAF/异常活动立即停止后续批次。
# 用法: bash skill-runs/missing_pdf_2026-09-09/run_batches.sh <publisher> <batch_file> [<batch_file> ...]
set -u
PUB="$1"; shift
ROOT="D:/codex/博客网站"
INSTSCI="C:/Users/Administrator/Documents/Codex/tools/bin/instsci.cmd"
unset http_proxy https_proxy HTTP_PROXY HTTPS_PROXY ALL_PROXY all_proxy

WINDIR="$(cd "$ROOT" && pwd -W)"

for B in "$@"; do
  NAME="$(basename "$B")"
  LOG="$ROOT/skill-runs/missing_pdf_2026-09-09/log_${NAME}.log"
  OUT="$WINDIR\\papers\\instsci\\instsci_${NAME}"
  SRC="$WINDIR\\skill-runs\\missing_pdf_2026-09-09\\batches\\${NAME}"
  echo "=== 开始 $NAME ($PUB) ==="
  "$INSTSCI" papers "$SRC" --publisher "$PUB" --institution "中国农业大学" \
    --oa-first --login-timeout 900 --pdf-timeout 120 --concurrency 1 \
    --output "$OUT" > "$LOG" 2>&1
  RC=$?
  echo "=== $NAME 完成 exit=$RC ==="
  tail -c 400 "$LOG"
  if grep -qiE "异常活动|unusual|WAF|captcha|Access Denied|blocked" "$LOG"; then
    echo "!!! 检测到风控/WAF，停止后续批次"
    break
  fi
done
