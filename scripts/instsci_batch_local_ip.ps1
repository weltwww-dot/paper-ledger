param(
    [Parameter(Mandatory = $true)][string]$DoisFile,
    [string]$Institution = "",
    [string]$Publisher = "auto",
    [Parameter(Mandatory = $true)][string]$OutputDir,
    [int]$LoginTimeout = 900,
    [int]$PdfTimeout = 90,
    [int]$Concurrency = 1
)

$ErrorActionPreference = "Stop"
$Python = (Get-Command python -ErrorAction Stop).Source

# 预检：清理上一轮残留的 CloakBrowser 进程并设置浏览器缓存目录（见 更新工作流.md 9.4）
& powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot "instsci_preflight.ps1")

# Institution IP access is valid only when publisher traffic stays on the local
# network exit. This check deliberately refuses a generic proxy/PAC route.
& $Python (Join-Path $PSScriptRoot "route_check.py") --require-direct
if ($LASTEXITCODE -ne 0) {
    [Console]::Error.WriteLine("Local-direct preflight failed; InstSci will not start.")
    exit $LASTEXITCODE
}

$SkillRunner = "D:\codex\.codex\skills\paper-summarize-fetch\scripts\instsci_batch.ps1"
if (-not (Test-Path -LiteralPath $SkillRunner)) {
    Write-Error "找不到 InstSci 批处理脚本: $SkillRunner"
    exit 2
}

& powershell -NoProfile -ExecutionPolicy Bypass -File $SkillRunner `
    -DoisFile $DoisFile -Institution $Institution -Publisher $Publisher -OutputDir $OutputDir `
    -LoginTimeout $LoginTimeout -PdfTimeout $PdfTimeout -Concurrency $Concurrency
exit $LASTEXITCODE
