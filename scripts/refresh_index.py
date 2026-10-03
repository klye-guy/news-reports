#!/usr/bin/env python3
"""Refresh LATEST_* pointers, current/ copies, and INDEX.md after a new report is added."""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

root = Path(__file__).resolve().parents[1]
daily = sorted((root / "daily").glob("????-??-??.md"))
weekly = sorted((root / "weekly").glob("????-??-??.md"))
current = root / "current"

ITEM_TITLE = re.compile(r"(?m)^(?:##\s+)?ITEM\s+\d+:\s*(.+)$")


def front(path: Path):
    text = path.read_text(encoding="utf-8")
    meta = {}
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"')
    return meta, text


def subject_line(text: str, meta: dict) -> str:
    m = ITEM_TITLE.search(text)
    if m:
        return m.group(1).strip()
    return meta.get("title", "").strip()


def month_label(date: str) -> str:
    try:
        y, m, _ = date.split("-")
        names = [
            "",
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        return f"{names[int(m)]} {y}"
    except Exception:
        return date[:7]


def copy_bytes(src: Path, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(src.read_bytes())


def pdf_cell(md: Path) -> str:
    pdf = md.with_suffix(".pdf")
    if not pdf.is_file():
        return ""
    rel = pdf.relative_to(root).as_posix()
    return f"[PDF](./{rel})"


if daily:
    newest = daily[-1]
    copy_bytes(newest, root / "LATEST_DAILY.md")
    copy_bytes(newest, current / "latest-daily.md")
    pdf = newest.with_suffix(".pdf")
    if pdf.is_file():
        copy_bytes(pdf, current / "latest-daily.pdf")

if weekly:
    newest = weekly[-1]
    copy_bytes(newest, root / "LATEST_WEEKLY.md")
    copy_bytes(newest, current / "latest-weekly.md")
    pdf = newest.with_suffix(".pdf")
    if pdf.is_file():
        copy_bytes(pdf, current / "latest-weekly.pdf")


def group_rows(paths: list[Path], kind: str) -> list[str]:
    """Newest-first month sections with subject column."""
    entries = []
    for p in reversed(paths):
        meta, text = front(p)
        date = p.stem
        subj = subject_line(text, meta).replace("|", "\\|")
        entries.append((month_label(date), date, p, meta, subj))

    by_month: dict[str, list] = defaultdict(list)
    order: list[str] = []
    for month, date, p, meta, subj in entries:
        if month not in by_month:
            order.append(month)
        by_month[month].append((date, p, meta, subj))

    lines: list[str] = []
    for month in order:
        lines.append(f"### {month}")
        lines.append("")
        if kind == "daily":
            lines.append("| Date | Subject | Markdown | PDF |")
            lines.append("|------|---------|----------|-----|")
            for date, p, meta, subj in by_month[month]:
                lines.append(
                    f"| {date} | {subj} | [daily/{p.name}](./daily/{p.name}) | {pdf_cell(p)} |"
                )
        else:
            lines.append("| Week ending | Subject | Markdown | PDF |")
            lines.append("|-------------|---------|----------|-----|")
            for date, p, meta, subj in by_month[month]:
                period = meta.get("period", "")
                # keep period discoverable in subject cell footnote-style when useful
                lines.append(
                    f"| {date} | {subj} | [weekly/{p.name}](./weekly/{p.name}) | {pdf_cell(p)} |"
                )
        lines.append("")
    return lines


lines = [
    "# Index",
    "",
    "Chronological catalog of archived intel reports. Newest first, grouped by month.",
    "",
    "Each row uses a one-line subject taken from the report (first ITEM title). "
    "Letter PDFs, when present, sit beside the dated markdown; the latest pair is also in `current/`.",
    "",
    "## Daily",
    "",
]
lines += group_rows(daily, "daily")
lines += [
    "## Weekly",
    "",
]
lines += group_rows(weekly, "weekly")
(root / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
print(f"Updated LATEST_*, current/, and INDEX ({len(daily)} daily, {len(weekly)} weekly)")
