# Portfolio — Nugroho Pangestu

Single-page portfolio site. **Live:** https://nuggetenak.github.io/Nugroho-Pangestu-Portofolio/

One file — `index.html` — with HTML, CSS and JS all inline. No build step, no
`package.json`, no framework, no dependencies. That simplicity is deliberate: keep it
that way unless something genuinely can't be done without a bundler.

## Structure

```
index.html                        ← the entire site
assets/
  Nugroho-Pangestu-Resume.pdf     ← generated — see assets/resume-src/README.md
  resume-src/                     ← résumé source + ATS verification script
icons/                            ← apple-touch-icon + 32/16px favicons
images/
  profile.jpg
  v423/                           ← Exhibit A–H, current build   (section id="gallery-v423")
  v87/                            ← Exhibit A–J, frozen build    (section id="gallery-v87")
  bunka/                          ← Japanese culture deck        (section id="gallery-bunka")
  lifeline/                       ← SSW infrastructure deck      (section id="gallery-lifeline")
```

Exhibit screenshots are served as WebP via `<picture>` with the original JPEG as fallback.
Naming convention for new screenshots: `images/README.md`.

## Editing

**Screenshots.** Copy or delete a `<figure class="gallery-item">` block inside the relevant
`gallery-*` section. New images pick up the click-to-expand lightbox automatically — no extra
wiring. If a file is missing, a striped placeholder renders in its slot rather than a broken
image icon.

**Résumé.** Don't edit the PDF. Edit `assets/resume-src/resume.html` and re-render — the
rebuild and verification steps are in `assets/resume-src/README.md`.

**Anything else.** Read `HANDOFF.md` first. It carries the working protocol and the current
state of the site.

## Verifying a change

There's no build and no test suite, so verification is manual and non-optional:

```bash
# 1. every referenced asset actually exists on disk
grep -oE '(src|href|srcset)="[^"h][^"]*"' index.html | cut -d'"' -f2 | sort -u | \
  while read -r f; do [ -e "$f" ] || echo "MISSING: $f"; done

# 2. both inline <script> blocks still parse
node --check <(sed -n '/<script>/,/<\/script>/p' index.html | sed '/<\/*script>/d')
```

## Deploying

GitHub Pages is already configured — **Settings → Pages → Deploy from branch: `main` / `(root)`**.
Pushing to `main` publishes; the site is live a minute or two later.

```bash
git add .
git commit -m "describe the change"
git push
```

No terminal handy? **Add file → Upload files** in the GitHub web UI works from a phone browser.
