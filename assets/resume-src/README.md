# Résumé source

`Nugroho-Pangestu-Resume.pdf` (one directory up) is **generated**, not hand-edited.
Edit `resume.html`, re-render, re-verify. Never edit the PDF directly.

## Design contract — do not drift from this

The résumé follows the **Kinobi / ATS standard**. These are hard constraints, not
suggestions. A previous session rewrote the résumé with display fonts, skill "pills"
and a 3-column languages block; all of that is ATS-hostile and was reverted.

- **Single column, top to bottom.** No sidebars, no multi-column blocks.
- **One font family** — Carlito (metric-compatible with Calibri). No display or mono faces.
- **Monochrome.** Black text on white. No accent colours.
- **No pills, chips, boxes, icons, tables, or images.** Plain text and plain `•` bullets.
- **Standard section headings** — Summary, Experience, Education, Skills, Languages.
- Reverse-chronological. **One A4 page.**

## Rebuild

```bash
pip install weasyprint --break-system-packages
python3 -c "from weasyprint import HTML; \
  d=HTML(filename='resume.html').render(); print('pages:', len(d.pages)); \
  d.write_pdf('../Nugroho-Pangestu-Resume.pdf')"
```

## Verify — both checks must pass

1. **`pages: 1`.** Two pages means it overflowed; tighten metrics, don't cut content silently.
2. **`python3 ats_check.py`** → `BROKEN ... 0`.

`ats_check.py` catches a real and easy-to-miss ATS failure: when a hyphenated compound
(`multi-agent`, `end-to-end`) lands at a line break, PDF text extractors drop the hyphen and
join the halves, so an ATS reads `multiagent`. The script diffs every hyphenated compound in
the source against the extracted text and reports any that got mangled. Fix by rewording so
the compound doesn't sit at a line end. **Re-run after any content edit** — changing one word
reflows the lines and can break a different compound.
