"""
Tests for red-line #2 (customer-facing) and red-line #3 (PII) guards.

Run:
    python3 -m pytest tests/
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from customer_brief_generator import (
    scan_for_internal_tokens,
    scan_for_unredacted_pii,
)


# ---------- Red-line #2: customer-facing copy must not leak internal info ----------


def test_scan_internal_tokens_catches_prd_id():
    text = "本次升级完成 PRD-0042 的所有验收标准。"
    hits = scan_for_internal_tokens(text)
    assert "PRD-0042" in hits


def test_scan_internal_tokens_catches_bug_id():
    text = "已记录 Bug-2026-0509 待下次迭代修复。"
    hits = scan_for_internal_tokens(text)
    assert any("Bug-" in h or "B-" in h for h in hits)


def test_scan_internal_tokens_catches_internal_role_codename():
    text = "运维同步回填后即可看到全部数据。"
    hits = scan_for_internal_tokens(text)
    assert "运维同步回填" in hits


def test_scan_internal_tokens_catches_model_id():
    text = "AI 模型已切换到 claude-opus-4-7 提供更稳定的输出。"
    hits = scan_for_internal_tokens(text)
    assert any("claude-" in h for h in hits)


def test_scan_internal_tokens_clean_text_returns_empty():
    text = "本次升级带来更稳定的内容生成体验。"
    hits = scan_for_internal_tokens(text)
    assert hits == []


def test_scan_internal_tokens_catches_internal_scheduling_phrase():
    text = "下个迭代上线时您将能看到这一功能。"
    hits = scan_for_internal_tokens(text)
    assert "下个迭代" in hits or "下个版本上线" in hits


# ---------- Red-line #3: confidential / PII must not enter AI context ----------


def test_scan_pii_catches_cn_mobile():
    text = "客户对接人手机：13800001234"
    hits = scan_for_unredacted_pii(text)
    assert "13800001234" in hits


def test_scan_pii_catches_email():
    text = "对接人邮箱：customer.contact@example.com"
    hits = scan_for_unredacted_pii(text)
    assert any("@" in h for h in hits)


def test_scan_pii_catches_id_number():
    text = "客户提供的身份证号：110105199001011234"
    hits = scan_for_unredacted_pii(text)
    assert any(len(h) >= 17 for h in hits)


def test_scan_pii_clean_text_returns_empty():
    text = "客户A（教育-中型）的对接人是运营负责人。"
    hits = scan_for_unredacted_pii(text)
    assert hits == []


# ---------- Cross-cutting: realistic input ----------


def test_realistic_internal_brief_clean():
    """Internal briefs are allowed to use internal labels but must redact PII."""
    text = (
        "客户A（教育-中型）的对接人 X 表示对合规非常关心。"
        "我方将在 5/15 之前发合规白皮书。"
    )
    pii = scan_for_unredacted_pii(text)
    internal = scan_for_internal_tokens(text)
    assert pii == []
    assert internal == []


def test_realistic_external_brief_with_violation():
    """External briefs accidentally containing PRD numbers must be flagged."""
    text = (
        "本次升级完成 PRD-0042 的所有验收标准。"
        "下个迭代我们会上线深度看板增强。"
    )
    hits = scan_for_internal_tokens(text)
    assert "PRD-0042" in hits
    assert "下个迭代" in hits
