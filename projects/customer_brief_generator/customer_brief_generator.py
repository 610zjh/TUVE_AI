"""
Customer Brief Generator
========================

Turns raw sales-call notes into a structured customer brief.

Outputs two artifacts:
  - <date>_<customer-label>_external.md  for the customer
  - <date>_<customer-label>_internal.md  for the internal team

Run:
    python3 customer_brief_generator.py <input_file>

Without ANTHROPIC_API_KEY set, falls back to template-fill mode (no AI call).
"""

from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
PROMPTS_DIR = PROJECT_ROOT / "prompts"
OUTPUT_DIR = PROJECT_ROOT / "output"

# ---------- Red-line guards (Red Line #2 / #3) ----------

INTERNAL_TOKEN_PATTERNS = [
    r"PRD-\d{4,}",
    r"Bug-\d{4,}",
    r"B-\d{4}-\d{4}-[A-Z]",
    r"ADR-\d{4,}",
    r"COMPACT-\d{4,}",
    r"\b(?:claude-|gpt-|anthropic-)[\w\-\.]+",
    r"运维同步回填",
    r"内部代号",
    r"下个迭代",
    r"下个版本上线",
]

UNREDACTED_PII_PATTERNS = [
    r"\b1[3-9]\d{9}\b",                       # CN mobile (full)
    r"\b\d{17}[\dXx]\b",                       # CN ID
    r"\b[\w\.\-]+@[\w\-]+\.[\w\.\-]+\b",       # email (any)
    r"\b\d{16,19}\b",                          # bank-card-like
]


def scan_for_internal_tokens(text: str) -> list[str]:
    """Return list of red-line-#2 violations found in customer-facing text."""
    hits: list[str] = []
    for pattern in INTERNAL_TOKEN_PATTERNS:
        for match in re.findall(pattern, text):
            hits.append(match)
    return hits


def scan_for_unredacted_pii(text: str) -> list[str]:
    """Return list of red-line-#3 violations found anywhere in input."""
    hits: list[str] = []
    for pattern in UNREDACTED_PII_PATTERNS:
        for match in re.findall(pattern, text):
            hits.append(match)
    return hits


# ---------- Core data model ----------


@dataclass
class CallNotes:
    raw: str
    customer_label: str
    call_date: str

    @classmethod
    def from_file(cls, path: Path) -> "CallNotes":
        raw = path.read_text(encoding="utf-8")

        # Try to find customer label and call date in the input header.
        customer_label = _extract_field(raw, "客户") or "客户A"
        call_date = _extract_field(raw, "时间") or datetime.now().strftime(
            "%Y-%m-%d"
        )

        return cls(raw=raw, customer_label=customer_label, call_date=call_date)


def _extract_field(text: str, label: str) -> str | None:
    pattern = rf"^[\-\*]?\s*{re.escape(label)}\s*[:：]\s*(.+)$"
    match = re.search(pattern, text, flags=re.MULTILINE)
    return match.group(1).strip() if match else None


# ---------- AI client (with fallback) ----------


def call_claude(system_prompt: str, user_prompt: str) -> str:
    """Call Anthropic Claude. Falls back to a template-fill on missing key."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return _template_fallback(user_prompt)

    try:
        import anthropic  # type: ignore
    except ImportError:
        print(
            "anthropic package not installed; running in template-fill mode.",
            file=sys.stderr,
        )
        return _template_fallback(user_prompt)

    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=2000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return response.content[0].text


def _template_fallback(user_prompt: str) -> str:
    """Used when no API key — produces a placeholder brief from the prompt."""
    return (
        "[模板填充模式 / Template-fill mode]\n\n"
        "输入笔记 / Input notes:\n"
        f"{user_prompt[:500]}...\n\n"
        "（设置 ANTHROPIC_API_KEY 启用 AI 起草）"
    )


# ---------- Brief generation ----------


def generate_external_brief(notes: CallNotes) -> str:
    system = (PROMPTS_DIR / "draft_external.md").read_text(encoding="utf-8")
    user = f"客户：{notes.customer_label}\n日期：{notes.call_date}\n\n原始笔记：\n{notes.raw}"
    return call_claude(system, user)


def generate_internal_brief(notes: CallNotes) -> str:
    system = (PROMPTS_DIR / "draft_internal.md").read_text(encoding="utf-8")
    user = f"客户：{notes.customer_label}\n日期：{notes.call_date}\n\n原始笔记：\n{notes.raw}"
    return call_claude(system, user)


# ---------- Main flow ----------


def main(input_path: Path) -> int:
    if not input_path.exists():
        print(f"输入文件不存在：{input_path}", file=sys.stderr)
        return 1

    raw = input_path.read_text(encoding="utf-8")

    # Red Line #3 guard: refuse to run on unredacted PII
    pii_hits = scan_for_unredacted_pii(raw)
    if pii_hits:
        print(
            "⚠️  红线 #3 警告：输入笔记似乎含有未脱敏的 PII。请先脱敏后重试。",
            file=sys.stderr,
        )
        print(f"  发现的模式片段（前 3 个）：{pii_hits[:3]}", file=sys.stderr)
        return 2

    notes = CallNotes.from_file(input_path)

    OUTPUT_DIR.mkdir(exist_ok=True)
    base_name = f"{notes.call_date}_{_safe_label(notes.customer_label)}"

    # External brief
    external = generate_external_brief(notes)
    external_violations = scan_for_internal_tokens(external)
    if external_violations:
        print(
            "⚠️  红线 #2 警告：客户面简报含有内部信息片段。请人审后再发：",
            file=sys.stderr,
        )
        for v in external_violations:
            print(f"    - {v}", file=sys.stderr)
    external_path = OUTPUT_DIR / f"{base_name}_external.md"
    external_path.write_text(external, encoding="utf-8")
    print(f"✅ 客户面简报已生成：{external_path}")

    # Internal brief
    internal = generate_internal_brief(notes)
    internal_path = OUTPUT_DIR / f"{base_name}_internal.md"
    internal_path.write_text(internal, encoding="utf-8")
    print(f"✅ 内部简报已生成：{internal_path}")

    print(
        "\n下一步：人审两份简报；客户面简报需通过红线 #2 三道闸（grep / 品牌声音 / 法务）后才能发出。"
    )
    return 0


def _safe_label(label: str) -> str:
    return re.sub(r"[^\w\-]+", "-", label).strip("-")[:30] or "customer"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法：python3 customer_brief_generator.py <input_file>")
        sys.exit(1)
    sys.exit(main(Path(sys.argv[1])))
