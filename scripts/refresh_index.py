#!/usr/bin/env python3
"""Refresh LATEST_* pointers and INDEX.md after a new report is added."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
daily = sorted((root / "daily").glob("????-??-??.md"))
weekly = sorted((root / "weekly").glob("????-??-??.md"))

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

if daily:
    (root / "LATEST_DAILY.md").write_text(daily[-1].read_text(encoding="utf-8"), encoding="utf-8")
if weekly:
    (root / "LATEST_WEEKLY.md").write_text(weekly[-1].read_text(encoding="utf-8"), encoding="utf-8")

lines = [
    "# Index",
    "",
    "Chronological catalog of archived intel reports. Newest first.",
    "",
    "## Daily",
    "",
    "| Date | File | DTG |",
    "|------|------|-----|",
]
for p in reversed(daily):
    meta, _ = front(p)
    lines.append(f"| {p.stem} | [daily/{p.name}](./daily/{p.name}) | {meta.get('dtg', '')} |")
lines += ["", "## Weekly", "", "| Week ending (Sunday) | File | Period |", "|----------------------|------|--------|"]
for p in reversed(weekly):
    meta, _ = front(p)
    lines.append(f"| {p.stem} | [weekly/{p.name}](./weekly/{p.name}) | {meta.get('period', '')} |")
lines.append("")
(root / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
print(f"Updated LATEST_* and INDEX ({len(daily)} daily, {len(weekly)} weekly)")
