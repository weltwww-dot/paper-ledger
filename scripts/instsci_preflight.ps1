# InstSci 批量取 PDF 前预检与清理脚本
# 固化 2026-09-07 实际踩坑的修复：残留浏览器进程占用 profile、浏览器缓存目录未设、
# 上一轮 instsci / broker 残留。跑批量（instsci papers / instsci_batch_local_ip.ps1）前先执行一次。
#
# 用法:
#   powershell -ExecutionPolicy Bypass -File scripts\instsci_preflight.ps1
#   powershell -ExecutionPolicy Bypass -File scripts\instsci_preflight.ps1 -RouteCheck   # 额外跑代理出口自检
#
# 只做清理与检查，不下载任何 PDF；不修改代理/凭据。

param(
    [switch]$RouteCheck
)
$ErrorActionPreference = "Continue"

Write-Host "== InstSci 预检 ==" -ForegroundColor Cyan

# ---------- 1. 浏览器缓存目录（CloakBrowser 免下载） ----------
$Found = $false
$candidates = @(
    $env:CLOAKBROWSER_CACHE_DIR,
    "C:\Users\Administrator\.cloakbrowser",
    "C:\Users\Administrator\Documents\Codex\tools\instsci-venv\Lib\site-packages\instsci\_browsers\cloakbrowser"
) | Where-Object { $_ -and (Test-Path -LiteralPath $_) }

foreach ($c in ($candidates | Select-Object -Unique)) {
    # 目录内存在 chromium-* 或 chrome.exe 才算有效缓存
    $hasChrome = @(Get-ChildItem -LiteralPath $c -Recurse -Filter chrome.exe -ErrorAction SilentlyContinue).Count -gt 0
    if ($hasChrome) {
        $env:CLOAKBROWSER_CACHE_DIR = $c
        Write-Host "[ok] CLOAKBROWSER_CACHE_DIR = $c" -ForegroundColor Green
        $Found = $true
        break
    }
}
if (-not $Found) {
    Write-Host "[warn] 未找到 CloakBrowser 缓存；instsci 首次运行需联网下载 chromium（可能超时）。" -ForegroundColor Yellow
}

# ---------- 2. 清理占用 chrome-profile 的残留 CloakBrowser 进程 ----------
$holders = @(Get-CimInstance Win32_Process -ErrorAction SilentlyContinue |
    Where-Object {
        $_.CommandLine -match '\.cloakbrowser' -and
        $_.CommandLine -match 'instsci\\chrome-profile'
    })
if ($holders.Count -gt 0) {
    Write-Host "[warn] 发现 $($holders.Count) 个残留浏览器进程占用 chrome-profile，正在清理…" -ForegroundColor Yellow
    foreach ($p in $holders) {
        try { Stop-Process -Id $p.ProcessId -Force -ErrorAction Stop } catch { }
    }
    Start-Sleep -Seconds 2
    Write-Host "[ok] 已清理残留浏览器进程" -ForegroundColor Green
} else {
    Write-Host "[ok] 无残留浏览器进程占用 chrome-profile" -ForegroundColor Green
}

# ---------- 3. 清理僵尸 instsci / broker 进程（可选保守：只提示，不强杀） ----------
$zombie = @(Get-CimInstance Win32_Process -ErrorAction SilentlyContinue |
    Where-Object { $_.Name -eq 'instsci.exe' -and $_.CommandLine -match 'session-broker-run' })
if ($zombie.Count -gt 0) {
    Write-Host "[warn] 发现 $($zombie.Count) 个 instsci broker 进程仍在运行（$($zombie.ProcessId -join ', ')）。" -ForegroundColor Yellow
    Write-Host "       若它们属于上一轮已结束的批量，可手动终止：Stop-Process -Id (PID) -Force" -ForegroundColor Yellow
} else {
    Write-Host "[ok] 无残留 instsci broker 进程" -ForegroundColor Green
}

# ---------- 4. 可选：代理出口自检 ----------
if ($RouteCheck) {
    Write-Host ""
    & python (Join-Path $PSScriptRoot "route_check.py")
}

Write-Host ""
Write-Host "== 预检完成：可以开始 InstSci 批量（建议单批 ≤ 25 篇并断点续跑）==" -ForegroundColor Cyan
