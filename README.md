# News Reports — World Events Intelligence Archive

Open-source intelligence summaries in a US military brief format, prepared for Kyle Sibley.

**Classification:** UNCLASSIFIED // FOR INFORMATIONAL USE ONLY — Not a U.S. Government product.

## Browse

The site is rebuilt on every push to `main` and published at [klye-guy.github.io/news-reports](https://klye-guy.github.io/news-reports/). Dated Markdown in this repo remains the source of truth. `scripts/prepare_docs.py` stages `daily/` and `weekly/` for MkDocs; it does not rewrite the archive.

## Start here (current reports)

| Report | Path |
|--------|------|
| **Latest daily** | [`LATEST_DAILY.md`](./LATEST_DAILY.md) |
| **Latest weekly** | [`LATEST_WEEKLY.md`](./LATEST_WEEKLY.md) |

## Layout

```
daily/YYYY-MM-DD.md     # 24-hour intel summary (0700 CT cadence)
weekly/YYYY-MM-DD.md    # Week rollup; filename = Sunday (week ending)
LATEST_DAILY.md         # Copy of most recent daily
LATEST_WEEKLY.md        # Copy of most recent weekly
current/                # Latest daily (and weekly) Markdown + letter PDF copies
INDEX.md                # Chronological catalog (auto-maintained)
```

## PDF renders

GitHub Markdown is the searchable source of truth. A letter-size PDF is a print render of the same file, not a second set of facts. GitHub preview and the PDF are meant to look different.

- Letter PDFs, once built, stay beside the dated Markdown (`daily/YYYY-MM-DD.pdf`, `weekly/YYYY-MM-DD.pdf`). Older PDFs are kept. `current/` holds real-file copies of the latest pair.
- `current/latest-daily.md` and `current/latest-daily.pdf` are real-file copies of that latest daily pair (same bytes). `current/latest-weekly.md` and `current/latest-weekly.pdf` match the latest weekly when one exists.
- Rebuild one report (the output directory must already exist):

```bash
templates/build-pdf.sh daily/YYYY-MM-DD.md daily/YYYY-MM-DD.pdf
```

Needs `pandoc`, `node`, and `google-chrome`. See `templates/README.md`.

## How to find things

1. **Today / this week:** open `LATEST_DAILY.md` or `LATEST_WEEKLY.md`.
2. **A specific day:** `daily/YYYY-MM-DD.md` (ISO date).
3. **A specific week:** `weekly/YYYY-MM-DD.md` where the date is the **Sunday** the weekly was issued (covers the prior 7 days).
4. **Search:** use GitHub search in this repo (e.g. `Houthis`, `Hormuz`, `F-35`) — every report has YAML front matter (`type`, `date`, `tags`, `dtg`) plus full plain-text body for grep.

## Report format (each file)

Military intelligence summary structure:

- Header block (DTG, period covered, classification)
- Executive summary
- Numbered items: WHAT/WHERE/WHEN → US IMPACT → SOURCE SYNOPSIS → MEDIA FRAMING (right / left) → CONFIDENCE
- Unconfirmed / watch items
- Source limitations

## Cadence

- **Daily:** every day ~0700 America/Chicago
- **Weekly:** every Sunday ~1500 America/Chicago

## Source mix (standing guidance)

Cross-check right-leaning (S2 Underground, Glenn Beck/Blaze, Daily Wire, Tim Pool/Timcast, Crowder), left-leaning / wires (AP, Reuters, major newspapers/TV), government announcements, and open-source military/OSINT. Synthesize corroborated facts; note framing differences; quarantine unverified claims.
