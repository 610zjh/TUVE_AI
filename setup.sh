#!/usr/bin/env bash
# setup.sh — TUZHAN_AI 仓库初始化
# Run once after cloning: bash setup.sh

set -e

echo "==> TUZHAN_AI 初始化 / Initializing TUZHAN_AI"
echo ""

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 1. 验证 Python 版本
echo "[1/5] 检查 Python 版本 / Checking Python version"
if command -v python3 &>/dev/null; then
    PY_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    echo "  Python ${PY_VERSION} 已找到 / found"
    PY_MAJOR=$(python3 -c 'import sys; print(sys.version_info.major)')
    PY_MINOR=$(python3 -c 'import sys; print(sys.version_info.minor)')
    if [ "$PY_MAJOR" -lt 3 ] || ([ "$PY_MAJOR" -eq 3 ] && [ "$PY_MINOR" -lt 8 ]); then
        echo "  ⚠️  推荐 Python 3.8+ / Python 3.8+ recommended"
    fi
else
    echo "  ⚠️  Python3 未找到。Customer Brief Generator 样例项目需要 Python。"
    echo "      Python3 not found. Customer Brief Generator sample needs Python."
fi
echo ""

# 2. 验证 git
echo "[2/5] 检查 git / Checking git"
if command -v git &>/dev/null; then
    echo "  $(git --version) 已找到 / found"
else
    echo "  ⚠️  git 未找到。仓库无法做版本管理 / git not found. Cannot version-control this repo."
fi
echo ""

# 3. 初始化 git 仓库（如果还没初始化）
echo "[3/5] 初始化 git / Initializing git"
if [ ! -d "${REPO_ROOT}/.git" ]; then
    cd "${REPO_ROOT}"
    git init -q
    git add .
    git commit -q -m "init: TUZHAN_AI baseline" || echo "  没改动可提交 / No changes to commit"
    echo "  ✅ git 仓库已初始化 / git repo initialized"
else
    echo "  git 仓库已存在 / git repo already exists"
fi
echo ""

# 4. 安装 Customer Brief Generator 样例项目的依赖（可选）
echo "[4/5] Customer Brief Generator 样例项目 / Sample project setup"
SAMPLE_DIR="${REPO_ROOT}/projects/customer_brief_generator"
if [ -d "${SAMPLE_DIR}" ]; then
    if command -v python3 &>/dev/null; then
        echo "  样例项目位于：${SAMPLE_DIR}"
        echo "  跑测试 / Running tests..."
        if (cd "${SAMPLE_DIR}" && python3 -m pytest tests/ -q 2>/dev/null); then
            echo "  ✅ 测试全过 / All tests passed"
        else
            echo "  ⚠️  测试需要 pytest。安装：pip install pytest"
            echo "      Tests need pytest. Install: pip install pytest"
        fi
        echo ""
        echo "  使用 AI 模式（可选）/ For AI mode (optional):"
        echo "    pip install -r ${SAMPLE_DIR}/requirements.txt"
        echo "    export ANTHROPIC_API_KEY=sk-ant-..."
    else
        echo "  跳过（无 Python）/ Skipped (no Python)"
    fi
else
    echo "  样例项目不存在（已被替换为你团队自己的项目？）/ Sample project missing"
fi
echo ""

# 5. 验证仓库完整性
echo "[5/5] 验证仓库完整性 / Verifying repo integrity"
REQUIRED_FILES=(
    "README.md"
    "AI_MANUAL.md"
    "CLAUDE.md"
    "AGENTS.md"
    "CODEX.md"
    ".cursorrules"
    "principles/000_CORE_RED_LINES.md"
    "issues/known.md"
)
MISSING=0
for f in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "${REPO_ROOT}/${f}" ]; then
        echo "  ❌ 缺失文件 / Missing: ${f}"
        MISSING=$((MISSING + 1))
    fi
done
if [ $MISSING -eq 0 ]; then
    echo "  ✅ 所有核心文件齐全 / All core files present"
else
    echo "  ⚠️  缺失 ${MISSING} 个核心文件，请检查 / ${MISSING} core files missing"
fi
echo ""

# 6. 输出"下一步"
cat <<EOF
==> 初始化完成 / Setup complete

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

     - 培训材料在 training/ 下
     - 自学路径见 training/post_conference/self_study_path_for_attendees.md
     - 1 小时路径建议从 AI_MANUAL.md 起读，用 [4-5 个核心文件]

  红线 #2 提醒 / Reminder:
    任何客户面文案禁止内部代号 / PRD 编号 / 客户名 / 模型 ID
    Customer-facing copy: NEVER include internal codes / PRD IDs / other customer names / model IDs

EOF
