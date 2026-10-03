#!/usr/bin/env python3
"""Stage a MkDocs tree from daily/ and weekly/ without rewriting the archive."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def parse_front_matter(text: str) -> dict[str, str]:
    match = FRONT_MATTER.match(text)
    if not match:
        return {}
    meta: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta


def stage(kind: str) -> list[dict[str, str]]:
    source = ROOT / kind
    dest = DOCS / kind
    dest.mkdir(parents=True, exist_ok=True)
    items: list[dict[str, str]] = []
    for path in sorted(source.glob("*.md"), reverse=True):
        text = path.read_text(encoding="utf-8")
        meta = parse_front_matter(text)
        (dest / path.name).write_text(text, encoding="utf-8")
        pdf = path.with_suffix(".pdf")
        if pdf.exists():
            shutil.copy2(pdf, dest / pdf.name)
        items.append(
            {
                "date": meta.get("date", path.stem),
                "title": meta.get("title", path.stem),
                "dtg": meta.get("dtg", ""),
                "href": f"{kind}/{path.stem}.md",
                "pdf": f"{kind}/{path.stem}.pdf" if pdf.exists() else "",
            }
        )
    return items


def table(items: list[dict[str, str]]) -> str:
    lines = ["| Date | Report | DTG | PDF |", "| --- | --- | --- | --- |"]
    for item in items:
        pdf = f"[PDF]({item['pdf']})" if item["pdf"] else ""
        lines.append(
            f"| {item['date']} | [{item['title']}]({item['href']}) | {item['dtg']} | {pdf} |"
        )
    return "\n".join(lines)


def main() -> None:
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir()
    daily = stage("daily")
    weekly = stage("weekly")
    latest_daily = daily[0]["href"] if daily else ""
    latest_weekly = weekly[0]["href"] if weekly else ""
    jumps = []
    if latest_daily:
        jumps.append(f"[Latest daily]({latest_daily})")
    if latest_weekly:
        jumps.append(f"[Latest weekly]({latest_weekly})")
    jumps.append("[Tags](tags.md)")
    index = "\n".join(
        [
            "# News Reports",
            "",
            "Open-source world-events summaries. Not a U.S. Government product.",
            "",
            " · ".join(jumps),
            "",
            "The dated Markdown in the repository is the source of truth. This site is rebuilt on every push to `main`.",
            "",
            "## Daily",
            "",
            table(daily) if daily else "_No daily reports yet._",
            "",
            "## Weekly",
            "",
            table(weekly) if weekly else "_No weekly reports yet._",
            "",
        ]
    )
    (DOCS / "index.md").write_text(index, encoding="utf-8")
    (DOCS / "tags.md").write_text("# Tags\n\n[TAGS]\n", encoding="utf-8")


if __name__ == "__main__":
    main()
