#!/usr/bin/env python3
"""Refresh LATEST_* pointers, current/ copies, and INDEX.md after a new report is added."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
daily = sorted((root / "daily").glob("????-??-??.md"))
weekly = sorted((root / "weekly").glob("????-??-??.md"))
current = root / "current"


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
    return meta


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

lines = [
    "# Index",
    "",
    "Chronological catalog of archived intel reports. Newest first.",
    "",
    "Letter PDFs, when present, sit beside the dated markdown, and the latest pair is also in current/.",
    "",
    "## Daily",
    "",
    "| Date | File | DTG | PDF |",
    "|------|------|-----|-----|",
]
for p in reversed(daily):
    meta = front(p)
    lines.append(
        f"| {p.stem} | [daily/{p.name}](./daily/{p.name}) | {meta.get('dtg', '')} | {pdf_cell(p)} |"
    )
lines += [
    "",
    "## Weekly",
    "",
    "| Week ending (Sunday) | File | Period | PDF |",
    "|----------------------|------|--------|-----|",
]
for p in reversed(weekly):
    meta = front(p)
    lines.append(
        f"| {p.stem} | [weekly/{p.name}](./weekly/{p.name}) | {meta.get('period', '')} | {pdf_cell(p)} |"
    )
lines.append("")
(root / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
print(f"Updated LATEST_*, current/, and INDEX ({len(daily)} daily, {len(weekly)} weekly)")
