#!/usr/bin/env python3
"""Stage a MkDocs tree from daily/ and weekly/ without rewriting the archive."""

from __future__ import annotations

import re
import shutil
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ASSETS_SRC = ROOT / "templates" / "site-extra.css"
FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
ITEM_TITLE = re.compile(
    r"(?m)^(?:##\s+)?ITEM\s+\d+:\s*(.+)$"
)
SUMMARY_TITLE = re.compile(
    r"(?m)^(DAILY|WEEKLY)\s+WORLD EVENTS INTELLIGENCE SUMMARY\s*$"
)


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


def subject_line(text: str, meta: dict[str, str]) -> str:
    """One-line subject from the first ITEM title, else the summary title, else YAML title."""
    m = ITEM_TITLE.search(text)
    if m:
        return m.group(1).strip()
    # fall back to body summary title + date from meta
    if SUMMARY_TITLE.search(text):
        return meta.get("title", "").strip() or "Intel summary"
    return meta.get("title", "").strip() or "Intel summary"


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


def stage(kind: str) -> list[dict[str, str]]:
    source = ROOT / kind
    dest = DOCS / kind
    dest.mkdir(parents=True, exist_ok=True)
    items: list[dict[str, str]] = []
    for path in sorted(source.glob("????-??-??.md"), reverse=True):
        text = path.read_text(encoding="utf-8")
        meta = parse_front_matter(text)
        (dest / path.name).write_text(text, encoding="utf-8")
        pdf = path.with_suffix(".pdf")
        if pdf.exists():
            shutil.copy2(pdf, dest / pdf.name)
        date = meta.get("date", path.stem)
        items.append(
            {
                "date": date,
                "title": meta.get("title", path.stem),
                "subject": subject_line(text, meta),
                "dtg": meta.get("dtg", ""),
                "period": meta.get("period", ""),
                "href": f"{kind}/{path.stem}.md",
                "pdf": f"{kind}/{path.stem}.pdf" if pdf.exists() else "",
                "month": month_label(date),
            }
        )
    return items


def month_sections(items: list[dict[str, str]], kind: str) -> str:
    if not items:
        return f"_No {kind} reports yet._"
    by_month: dict[str, list[dict[str, str]]] = defaultdict(list)
    order: list[str] = []
    for item in items:
        if item["month"] not in by_month:
            order.append(item["month"])
        by_month[item["month"]].append(item)
    blocks: list[str] = []
    for month in order:
        blocks.append(f"### {month}")
        blocks.append("")
        if kind == "weekly":
            blocks.append("| Week ending | Subject | Report | PDF |")
            blocks.append("| --- | --- | --- | --- |")
            for item in by_month[month]:
                pdf = f"[PDF]({item['pdf']})" if item["pdf"] else ""
                subj = item["subject"].replace("|", "\\|")
                blocks.append(
                    f"| {item['date']} | {subj} | [Open]({item['href']}) | {pdf} |"
                )
        else:
            blocks.append("| Date | Subject | Report | PDF |")
            blocks.append("| --- | --- | --- | --- |")
            for item in by_month[month]:
                pdf = f"[PDF]({item['pdf']})" if item["pdf"] else ""
                subj = item["subject"].replace("|", "\\|")
                blocks.append(
                    f"| {item['date']} | {subj} | [Open]({item['href']}) | {pdf} |"
                )
        blocks.append("")
    return "\n".join(blocks).rstrip() + "\n"


def latest_card(item: dict[str, str] | None, label: str) -> str:
    if not item:
        return f"**{label}:** _none yet_"
    pdf = f" · [PDF]({item['pdf']})" if item["pdf"] else ""
    subj = item["subject"]
    return (
        f"**{label}** — {item['date']}\n\n"
        f"{subj}\n\n"
        f"[Read the report]({item['href']}){pdf}"
    )


def main() -> None:
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir()
    styles = DOCS / "stylesheets"
    styles.mkdir()
    if ASSETS_SRC.exists():
        shutil.copy2(ASSETS_SRC, styles / "extra.css")
    else:
        (styles / "extra.css").write_text("/* placeholder */\n", encoding="utf-8")

    daily = stage("daily")
    weekly = stage("weekly")
    latest_daily = daily[0] if daily else None
    latest_weekly = weekly[0] if weekly else None

    index_parts = [
        "# News Reports",
        "",
        "Open-source world-events intelligence summaries in a US military brief format. "
        "Not a U.S. Government product. Classification: UNCLASSIFIED // FOR INFORMATIONAL USE ONLY.",
        "",
        "## Start here",
        "",
        latest_card(latest_daily, "Latest daily"),
        "",
        latest_card(latest_weekly, "Latest weekly"),
        "",
        "Dated Markdown in the GitHub repository is the source of truth. "
        "This site is rebuilt on every push to `main`. Letter PDFs, when present, are print renders of the same words.",
        "",
        "## Daily archive",
        "",
        month_sections(daily, "daily"),
        "",
        "## Weekly archive",
        "",
        month_sections(weekly, "weekly"),
        "",
    ]
    (DOCS / "index.md").write_text("\n".join(index_parts), encoding="utf-8")
    (DOCS / "tags.md").write_text(
        "# Tags\n\nBrowse reports by tag.\n\n[TAGS]\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
