# HANDOFF.md — Nugroho-Pangestu-Portofolio

> ## 🟡 Session 2 done, one thing needs the owner's eyes — 2026-08-23
> All 4 🟢 tasks from session 1 are shipped, committed, and pushed to `main` (`d825...` through
> `cdd2828` — see CURRENT STATE below for the full list). The 2 🔵 tasks are still gated on the
> owner exactly as session 1 left them; nothing started there.
>
> **Flagged, not changed:** the owner told the agent (in chat, not in this file) that the
> `bunka` gallery's card screenshots were actually showing SSW Konstruksi content, not
> 日本の文化. Session 2 checked — card back in `bunka-03-kartu-belakang.jpg` has a `日本 文化`
> footer stamped on the card itself, and the site's own caption for `bunka-02` already read
> "kanji + reading (鳥居 / torii)" before this session touched anything. Both point the same
> way: correct as-is. Left every byte of the bunka/lifeline galleries untouched pending the
> owner confirming which image they actually meant — do the same if you're picking this up.

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

## CURRENT STATE (2026-08-23, end of session 2)

- Live and correct as of commit `cdd2828`.
- Stack unchanged: single `index.html`, vanilla CSS + JS, zero dependencies, GitHub Pages.
- Lightbox now supports prev/next + arrow keys + an "N / total" counter, scoped per
  `.gallery-grid` (so v423's 8 don't bleed into v87's 10, etc.) — same `<script>` IIFE, no new
  files. (`d6f688d`)
- 22 of the 24 exhibit screenshots are now served as WebP via `<picture>` with the original
  `.jpg` as fallback (v87-06/07 were already `.webp`, left alone) — 5.1 MB → 2.3 MB for those
  22. `onerror` on each `<img>` now walks up through `this.parentElement` (the new `<picture>`)
  to reach the placeholder `<div>`, since that div is `<picture>`'s sibling now, not `<img>`'s.
  (`3603800`)
- All 18 generic `v423`/`v87` alt-text placeholders replaced with condensed (~6–10 word)
  descriptions pulled from each figcaption. `bunka`/`lifeline` untouched, out of scope for that
  task. (`d96285a`)
- New `icons/` folder: `apple-touch-icon-180.png`, `favicon-32.png`, `favicon-16.png` — same
  mark as the inline SVG favicon (indigo `#2b5580` rounded-rect, "N"), regenerated at each size
  using the site's actual brand font (IBM Plex Mono Bold) rather than a generic system font. The
  original inline SVG `<link>` is untouched and still loads first. (`cdd2828`)
- No build step, no tests, no lint. Verification = grep every `src=`/`href=`/`srcset=` in
  `index.html` against what's on disk + a Node syntax check on both inline `<script>` blocks,
  after every single task, not just at the end.

---

## ACTIVE TASKS

### 🟢 Unblocked — done this session

- [x] **Lightbox prev/next + counter.** Done — `d6f688d`.

- [x] **WebP for the 24 exhibit screenshots.** Done for 22; the other 2 were already `.webp`.
  `3603800`.

- [x] **Alt-text on 18 images.** Done — `d96285a`.

- [x] **`apple-touch-icon` + standard favicon sizes.** Done — `cdd2828`.

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
