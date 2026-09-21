# News Reports — World Events Intelligence Archive

Private archive of US military-style open-source intelligence summaries prepared for Kyle Sibley.

**Classification:** UNCLASSIFIED // FOR INFORMATIONAL USE ONLY — Not a U.S. Government product.

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
INDEX.md                # Chronological catalog (auto-maintained)
```

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
