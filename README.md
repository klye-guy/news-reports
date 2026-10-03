# News Reports — World Events Intelligence Archive

Open-source intelligence summaries in a US military brief format, prepared for Kyle Sibley.

**Classification:** UNCLASSIFIED // FOR INFORMATIONAL USE ONLY — Not a U.S. Government product.

## Browse the site

Readable HTML is published from this repo on every push to `main`:

**[klye-guy.github.io/news-reports](https://klye-guy.github.io/news-reports/)**

That site is the best place to read reports. Dated Markdown here remains the source of truth; `scripts/prepare_docs.py` stages it for MkDocs without rewriting the archive.

## Latest reports

| | Markdown | PDF |
|--|----------|-----|
| **Latest daily** | [`LATEST_DAILY.md`](./LATEST_DAILY.md) · [`current/latest-daily.md`](./current/latest-daily.md) | [`current/latest-daily.pdf`](./current/latest-daily.pdf) |
| **Latest weekly** | [`LATEST_WEEKLY.md`](./LATEST_WEEKLY.md) · [`current/latest-weekly.md`](./current/latest-weekly.md) | [`current/latest-weekly.pdf`](./current/latest-weekly.pdf) |

Full catalog (by month, with one-line subjects): [`INDEX.md`](./INDEX.md).

## How to browse the archive

1. **Today / this week:** open the latest links above, or the published site home page.
2. **A specific day:** `daily/YYYY-MM-DD.md` (ISO date). PDF sits beside it when built.
3. **A specific week:** `weekly/YYYY-MM-DD.md` where the date is the **Sunday** the weekly was issued.
4. **Search:** GitHub code search in this repo (labels like `WHAT / WHERE / WHEN`, `US IMPACT ASSESSMENT`, tags in YAML front matter).

## Layout

```
daily/YYYY-MM-DD.md|.pdf   # 24-hour intel summary (~0700 CT)
weekly/YYYY-MM-DD.md|.pdf  # week rollup; filename = Sunday (week ending)
LATEST_DAILY.md / LATEST_WEEKLY.md
current/                   # real-file copies of the latest Markdown + PDF pair
INDEX.md                   # month-grouped catalog (from scripts/refresh_index.py)
templates/                 # letter PDF build (pandoc + report.lua + Chrome)
scripts/prepare_docs.py    # stages docs/ for the GitHub Pages MkDocs site
```

## PDF renders

Markdown is the searchable source of facts. A letter-size PDF is a print render of the same file. Rebuild one report (output directory must already exist):

```bash
templates/build-pdf.sh daily/YYYY-MM-DD.md daily/YYYY-MM-DD.pdf
```

Needs `pandoc`, `node`, and `google-chrome`. See `templates/README.md`.

## Cadence

- **Daily:** every day ~0700 America/Chicago
- **Weekly:** every Sunday ~1500 America/Chicago

## Source mix (standing guidance)

Cross-check right-leaning (S2 Underground, Glenn Beck/Blaze, Daily Wire, Tim Pool/Timcast, Crowder), left-leaning / wires (AP, Reuters, major newspapers/TV), government announcements, and open-source military/OSINT. Synthesize corroborated facts; note framing differences; quarantine unverified claims.
