# setup.ps1 — TUZHAN_AI 仓库初始化（Windows / PowerShell 版）
# Run once after cloning:
#   PowerShell -ExecutionPolicy Bypass -File setup.ps1
# 或在已允许脚本的会话中：
#   .\setup.ps1

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "==> TUZHAN_AI 初始化 / Initializing TUZHAN_AI" -ForegroundColor Cyan
Write-Host ""

# ---------- [1/5] Python ----------
Write-Host "[1/5] 检查 Python 版本 / Checking Python version"
$pythonCmd = $null
foreach ($candidate in @("python", "python3", "py")) {
    if (Get-Command $candidate -ErrorAction SilentlyContinue) {
        $pythonCmd = $candidate
        break
    }
}
if ($pythonCmd) {
    $pyVersion = & $pythonCmd -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>$null
    Write-Host "  Python $pyVersion 已找到（命令：$pythonCmd）/ found"
    $pyMajor = [int](& $pythonCmd -c "import sys; print(sys.version_info.major)")
    $pyMinor = [int](& $pythonCmd -c "import sys; print(sys.version_info.minor)")
    if ($pyMajor -lt 3 -or ($pyMajor -eq 3 -and $pyMinor -lt 8)) {
        Write-Host "  推荐 Python 3.8+ / Python 3.8+ recommended" -ForegroundColor Yellow
    }
} else {
    Write-Host "  Python 未找到。Customer Brief Generator 样例项目需要 Python。" -ForegroundColor Yellow
    Write-Host "  Python not found. Customer Brief Generator sample needs Python."
    Write-Host "  下载：https://www.python.org/downloads/"
}
Write-Host ""

# ---------- [2/5] git ----------
Write-Host "[2/5] 检查 git / Checking git"
if (Get-Command git -ErrorAction SilentlyContinue) {
    $gitVersion = git --version
    Write-Host "  $gitVersion 已找到 / found"
} else {
    Write-Host "  git 未找到。仓库无法做版本管理 / git not found. Cannot version-control this repo." -ForegroundColor Yellow
    Write-Host "  下载：https://git-scm.com/download/win"
}
Write-Host ""

# ---------- [3/5] git init ----------
Write-Host "[3/5] 初始化 git / Initializing git"
$gitDir = Join-Path $RepoRoot ".git"
if (-not (Test-Path $gitDir)) {
    if (Get-Command git -ErrorAction SilentlyContinue) {
        Push-Location $RepoRoot
        try {
            git init -q
            git add .
            git commit -q -m "init: TUZHAN_AI baseline" 2>$null
            if ($LASTEXITCODE -ne 0) {
                Write-Host "  没改动可提交 / No changes to commit"
            }
            Write-Host "  git 仓库已初始化 / git repo initialized"
        } finally {
            Pop-Location
        }
    } else {
        Write-Host "  跳过（无 git）/ Skipped (no git)"
    }
} else {
    Write-Host "  git 仓库已存在 / git repo already exists"
}
Write-Host ""

# ---------- [4/5] Sample project ----------
Write-Host "[4/5] Customer Brief Generator 样例项目 / Sample project setup"
$sampleDir = Join-Path $RepoRoot "projects\customer_brief_generator"
if (Test-Path $sampleDir) {
    if ($pythonCmd) {
        Write-Host "  样例项目位于：$sampleDir"
        Write-Host "  跑测试 / Running tests..."
        Push-Location $sampleDir
        try {
            & $pythonCmd -m pytest tests/ -q 2>$null
            if ($LASTEXITCODE -eq 0) {
                Write-Host "  测试全过 / All tests passed" -ForegroundColor Green
            } else {
                Write-Host "  测试需要 pytest。安装：pip install pytest" -ForegroundColor Yellow
                Write-Host "  Tests need pytest. Install: pip install pytest"
            }
        } finally {
            Pop-Location
        }
        Write-Host ""
        Write-Host "  使用 AI 模式（可选）/ For AI mode (optional):"
        Write-Host "    pip install -r `"$sampleDir\requirements.txt`""
        Write-Host "    `$env:ANTHROPIC_API_KEY = 'sk-ant-...'"
    } else {
        Write-Host "  跳过（无 Python）/ Skipped (no Python)"
    }
} else {
    Write-Host "  样例项目不存在（已被替换为你团队自己的项目？）/ Sample project missing"
}
Write-Host ""

# ---------- [5/5] Integrity check ----------
Write-Host "[5/5] 验证仓库完整性 / Verifying repo integrity"
$requiredFiles = @(
    "README.md",
    "AI_MANUAL.md",
    "CLAUDE.md",
    "AGENTS.md",
    "CODEX.md",
    ".cursorrules",
    "principles\000_CORE_RED_LINES.md",
    "issues\known.md"
)
$missing = 0
foreach ($f in $requiredFiles) {
    $fullPath = Join-Path $RepoRoot $f
    if (-not (Test-Path $fullPath)) {
        Write-Host "  缺失文件 / Missing: $f" -ForegroundColor Red
        $missing++
    }
}
if ($missing -eq 0) {
    Write-Host "  所有核心文件齐全 / All core files present" -ForegroundColor Green
} else {
    Write-Host "  缺失 $missing 个核心文件，请检查 / $missing core files missing" -ForegroundColor Yellow
}
Write-Host ""

# ---------- Next steps ----------
Write-Host "==> 初始化完成 / Setup complete" -ForegroundColor Cyan
Write-Host ""
Write-Host @"
下一步 / Next steps:

  1. 打开你常用的 AI 工具（Claude Code / Cursor / Codex / Trae）
     Open your AI tool of choice.

  2. 把这个文件夹拖进 AI 工具的工作目录
     Drag this folder into your AI tool's working directory.

  3. 第一条消息发：
     First message:

     > 请先读 AI_MANUAL.md 了解项目导航，然后我会告诉你今天要做什么。
     > Please read AI_MANUAL.md first, then I'll tell you what we're doing today.

  4. 之后照常工作。AI 会按这套方法论协作。
     Then work as usual. AI will collaborate per this methodology.

  5. 如果你是从培训现场拿到这份仓库：
     If you got this from the training session:

     - 培训材料在 training\ 下
     - 自学路径见 training\post_conference\self_study_path_for_attendees.md
     - 1 小时路径建议从 AI_MANUAL.md 起读

  红线 #2 提醒 / Reminder:
    任何客户面文案禁止内部代号 / PRD 编号 / 客户名 / 模型 ID
    Customer-facing copy: NEVER include internal codes / PRD IDs / other customer names / model IDs

"@
