"""
Tests for the CallNotes parsing and the safe-label utility.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from customer_brief_generator import CallNotes, _safe_label, _extract_field


def test_extract_field_finds_customer():
    raw = "客户：客户 A（教育-中型）\n时间：2026-05-08\n"
    assert _extract_field(raw, "客户") == "客户 A（教育-中型）"


def test_extract_field_finds_time():
    raw = "客户：客户 A\n时间：2026-05-08\n"
    assert _extract_field(raw, "时间") == "2026-05-08"


def test_extract_field_returns_none_for_missing():
    raw = "纯笔记，没有标签字段"
    assert _extract_field(raw, "客户") is None


def test_safe_label_strips_special_chars():
    assert _safe_label("客户 A（教育-中型）") == "客户-A-教育-中型"


def test_safe_label_truncates_long():
    very_long = "x" * 100
    assert len(_safe_label(very_long)) <= 30


def test_safe_label_falls_back_to_default():
    assert _safe_label("!!!") == "customer"


def test_call_notes_from_file(tmp_path):
    f = tmp_path / "notes.txt"
    f.write_text("客户：客户 B\n时间：2026-05-09\n\n会议要点 ...", encoding="utf-8")
    notes = CallNotes.from_file(f)
    assert notes.customer_label == "客户 B"
    assert notes.call_date == "2026-05-09"
    assert "会议要点" in notes.raw


def test_call_notes_falls_back_when_header_missing(tmp_path):
    f = tmp_path / "notes.txt"
    f.write_text("纯笔记没标签", encoding="utf-8")
    notes = CallNotes.from_file(f)
    assert notes.customer_label == "客户A"
    # call_date falls back to today; just check it's present.
    assert notes.call_date
