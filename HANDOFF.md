# HANDOFF.md — Nugroho-Pangestu-Portofolio

> ## 🟢 Fresh — 2026-08-23, session 1
> First handoff doc for this repo. Site is live and correct as of commit `5aeeffc` — hero
> photo, nav mark, and exhibit-caption language fixes from this session are all in `main`.
> The 6 items below are enhancement ideas the owner approved for a follow-up agent to execute.
> Nothing here is blocked on unfinished prior work; this is a clean starting point.

---

**This is the relay baton**, same convention as the flagship SSW Konstruksi project's
`HANDOFF.md`: one file, always edited in place. Read it, do the work, overwrite this file with
the new state before you hand off. Don't create `HANDOFF_v2.md`.

---

## GETTING STARTED (new agent, new chat, no other context)

```
Repo:   https://github.com/nuggetenak/Nugroho-Pangestu-Portofolio
Branch: main (the only branch — push straight to it, no PR workflow here)
Live:   https://nuggetenak.github.io/Nugroho-Pangestu-Portofolio/ (GitHub Pages, main / root)

git clone https://[token]@github.com/nuggetenak/Nugroho-Pangestu-Portofolio.git
```

The owner pastes a GitHub PAT directly in chat for clone/push access — that's their established
practice across projects, not an oversight. Still good hygiene: don't leave it sitting in
`git remote -v` output or anything else you print after you're done with it.

**What this repo actually is:** one static file, `index.html` — HTML+CSS+JS all inline, no
build step, no `package.json`, no framework. `images/` holds every screenshot. That's the whole
repo. Don't introduce a bundler/build step/framework for any task below unless a task
explicitly needs it — the single-file simplicity is a feature here, not a gap.

Then: PROTOCOL section below, first.

---

## ⚡ PROTOCOL — read this before touching anything

1. This is a portfolio site being sent to a specific recruiter ("Nick") for a real job
   application — treat copy/content changes conservatively. For anything that isn't purely
   mechanical (CSS/asset work), if you're unsure whether a wording change reads right, ask
   rather than guess.
2. Commit-per-task, matching this repo's existing `git log` — one commit per fix, descriptive
   message, no bundling unrelated changes together.
3. Git identity already configured by prior sessions: `user.name "Nugget"`,
   `user.email "nugget@users.noreply.github.com"`. Reuse it.
4. **Don't re-process what the owner already gave you.** Session 1 shipped a face-detected
   recrop of the owner's uploaded profile photo; turned out the owner had already cropped it
   themselves from the original and pushed back on it — see commits `759d98c` → `1eece77` for
   the full story. Lesson: fit assets into the existing layout slot, don't re-author their
   content unless it's explicitly asked for.
5. Before marking any task done, spot-check it the way session 1 did: grep every `src=`/`href=`
   in `index.html` against what's actually on disk (or a live link), rather than assuming a
   path resolves just because it looks right.
6. When you hand off: overwrite this file in place with the new state (boxes ticked, new items
   added if the owner asked for more), and commit it too.

---

## CURRENT STATE (2026-08-23)

- Live and correct as of commit `5aeeffc`.
- Stack: single `index.html`, vanilla CSS + JS, zero dependencies, hosted on GitHub Pages.
- 4 exhibit galleries (v4.23.0 ×8, v87 ×10, 日本の文化 ×3, SSW Lifeline & Infrastruktur ×3 —
  24 screenshots total, ~5.7 MB in `images/`), each wired into one shared lightbox via
  `.gallery-frame` — a script near the end of `index.html` adds `.is-clickable` on load and
  handles open/close.
- No build step, no tests, no lint. Verification so far = manual grep + visual check (PROTOCOL
  §5) — there's no `verify-*.mjs` script in this repo the way the flagship project has one.

---

## ACTIVE TASKS

### 🟢 Unblocked — ready to start, no owner input needed

- [ ] **Lightbox prev/next + counter.** Right now the lightbox shows one image; closing it is
  the only way to see the next one. Add: on open, capture the sibling `.gallery-frame` images
  within the same `.gallery-grid` as an ordered list + current index; prev/next buttons in the
  overlay (reuse `.lightbox-close`'s visual treatment); left/right arrow keys wired the same way
  Escape already is; a small "N / total" counter next to the close button. Stays inside the
  existing `<script>` IIFE — no new files needed.

- [ ] **WebP for the 24 exhibit screenshots.** ~5.7 MB total today as JPEG. Convert each
  (Pillow: `im.save(path, 'WEBP', quality=82)` is a reasonable starting point, worth comparing
  size/quality per image) and serve via `<picture>` with a WebP `<source>` + the existing
  `.jpg` kept as the `<img>` fallback — don't hard-replace `src`. Profile photo and favicon are
  out of scope for this task.

- [ ] **Alt-text on 18 images.** `v423`/`v87` galleries currently have generic alt text
  (`"Screenshot v4.23.0 N"` / `"Screenshot v87 N"`); `bunka`/`lifeline` are already descriptive.
  Rule: take the figcaption text after the `<span class="exhibit-tag">X —</span>` prefix,
  condense to ~6–10 words, use that as `alt`. E.g. figcaption "Beranda — streak counter, a
  daily 'misi,' ..." → `alt="Beranda tab: streak counter and daily misi"`. Mechanical, 18 lines.

- [ ] **`apple-touch-icon` + standard favicon sizes.** Current favicon is an inline SVG
  data-URI (indigo `#2b5580` rounded-rect, white "N", monospace) — regenerate that same mark as
  PNGs (180×180 for apple-touch-icon, 32×32 + 16×16 for favicon), drop them in `images/` or a
  new `icons/`, add the matching `<link>` tags. Keep the existing inline SVG favicon too
  (cheap, already works); this is additive, for the add-to-homescreen/bookmark case.

### 🔵 Gated on an owner decision — ask before starting

- [ ] **Downloadable résumé PDF.** Needs the owner to supply the actual PDF — not something an
  agent should generate or invent from the on-page copy. Once supplied: drop it at e.g.
  `assets/Nugroho-Pangestu-Resume.pdf`, add a link-card in the Links section plus maybe a hero
  CTA ("Download résumé"). A `@media print` pass on `index.html` while in there isn't a bad
  idea either (hide nav/lightbox/expand-badges on print), in case someone prints the page
  itself instead of using the PDF.

- [ ] **Visit tracker (e.g. GoatCounter).** Needs the owner to create the free account and hand
  the agent their site code — not something an agent can sign up for on the owner's behalf.
  Once they have it, the integration itself is one `<script>` tag + a `data-goatcounter`
  attribute.

---

## REFERENCE (stable — read from the repo, not reproduced here)

- `README.md` — project pitch/structure overview.
- `images/README.md` — asset-naming convention for new exhibit screenshots.
- Live site: https://nuggetenak.github.io/Nugroho-Pangestu-Portofolio/
