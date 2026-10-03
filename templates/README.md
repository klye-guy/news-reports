# Intel report PDF template

Markdown is the source of facts and the searchable archive. The PDF is a letter-size render of that same file, not a second writeup. GitHub's Markdown preview and this PDF are supposed to look different: the preview is the archive; the PDF is a print brief.

## Build

From the news-reports repo root (the output directory must already exist):

```bash
templates/build-pdf.sh path/to/report.md path/to/report.pdf
```

Example:

```bash
templates/build-pdf.sh daily/2026-10-03.md daily/2026-10-03.pdf
```

Requires `pandoc`, `node`, and `google-chrome` on PATH. No extra npm packages.

The script runs pandoc (HTML5, section divs, `report.html`, `report.lua`, `report.css`) and then `print-pdf.mjs`, which prints with headless Chrome: letter, CSS page size, backgrounds on, no browser header or footer.

Do not hand-edit the PDF. Do not add facts in the template.
