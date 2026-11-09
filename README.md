# News Reports — World Events & IT Intelligence Archive

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
| **Latest IT / cybersecurity daily** | [`LATEST_IT_DAILY.md`](./LATEST_IT_DAILY.md) · [`current/latest-it-daily.md`](./current/latest-it-daily.md) | [`current/latest-it-daily.pdf`](./current/latest-it-daily.pdf) |

Full catalog (by month, with one-line subjects): [`INDEX.md`](./INDEX.md).

## How to browse the archive

1. **Today / this week:** open the latest links above, or the published site home page.
2. **A specific day (world events):** `daily/YYYY-MM-DD.md` (ISO date). PDF sits beside it when built.
3. **A specific week:** `weekly/YYYY-MM-DD.md` where the date is the **Sunday** the weekly was issued.
4. **A specific day (IT / cybersecurity):** `it-daily/YYYY-MM-DD.md`. PDF sits beside it when built.
5. **Search:** GitHub code search in this repo (labels like `WHAT / WHERE / WHEN`, `US IMPACT ASSESSMENT`, tags in YAML front matter).

## Layout

```
daily/YYYY-MM-DD.md|.pdf       # 24-hour world-events intel (~0700 CT)
weekly/YYYY-MM-DD.md|.pdf      # week rollup; filename = Sunday (week ending)
it-daily/YYYY-MM-DD.md|.pdf    # daily IT & cybersecurity intel (~0721 CT)
LATEST_DAILY.md / LATEST_WEEKLY.md / LATEST_IT_DAILY.md
current/                       # real-file copies of the latest Markdown + PDF pairs
INDEX.md                       # month-grouped catalog (from scripts/refresh_index.py)
templates/                     # letter PDF build (pandoc + report.lua + Chrome)
scripts/prepare_docs.py        # stages docs/ for the GitHub Pages MkDocs site
```

## Report categories

- **World events (daily / weekly):** US-focused world and national security intel in military brief format, with right vs left/mainstream framing.
- **IT & cybersecurity (it-daily):** Big-tech actions and statements, sysadmin-relevant news, cybersecurity, game preservation/piracy, and emulation tools plus company responses. Primary sources are reputable outlets; also scans controversial sources including Hacker News.

## PDF renders

Markdown is the searchable source of facts. A letter-size PDF is a print render of the same file. Rebuild one report (output directory must already exist):

```bash
templates/build-pdf.sh daily/YYYY-MM-DD.md daily/YYYY-MM-DD.pdf
templates/build-pdf.sh it-daily/YYYY-MM-DD.md it-daily/YYYY-MM-DD.pdf
```

Needs `pandoc`, `node`, and `google-chrome`. See `templates/README.md`.

## Cadence

- **Daily (world events):** every day ~0700 America/Chicago
- **IT & cybersecurity daily:** every day ~0721 America/Chicago
- **Weekly (world events):** every Sunday ~1500 America/Chicago

## Source mix (standing guidance)

**World events:** Cross-check right-leaning (S2 Underground, Glenn Beck/Blaze, Daily Wire, Tim Pool/Timcast, Crowder), left-leaning / wires (AP, Reuters, major newspapers/TV), government announcements, and open-source military/OSINT. Synthesize corroborated facts; note framing differences; quarantine unverified claims.

**IT & cybersecurity:** Prefer reputable tech and security outlets (e.g. Krebs, The Record, BleepingComputer, Ars Technica, The Verge, Wired, vendor advisories, CISA/NIST). Also search Hacker News and other controversial or community sources for early signals; corroborate before elevating. Cover major tech company news, sysadmin changes, cybersecurity incidents and disclosures, game preservation/piracy developments, and emulator/tool news plus corporate responses.
