# HANDOFF.md — Nugroho-Pangestu-Portofolio

> ## 🟢 Session 3 done — all active tasks closed — 2026-08-24
> Résumé PDF shipped (`11a806e`). Visit tracker: owner decided against it, removed from the
> task list rather than left gated. The bunka/torii question from session 2's banner: owner
> reviewed and said the site's solid as-is, don't revisit it — closed, not carried forward.
>
> No 🟢 or 🔵 tasks currently open. Next agent picking this up: read CURRENT STATE below for
> what's live, but there's nothing queued to work on until the owner adds something.

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

## CURRENT STATE (2026-08-24, end of session 3)

- Live and correct as of commit `11a806e`.
- Résumé: `assets/Nugroho-Pangestu-Resume.pdf`, one A4 page, built from the owner's original CV
  (not invented from on-page copy) with 2 targeted edits to match the portfolio — the exam-pass
  bullet now covers the 2 mentees + v87, and the portfolio URL is in the contact line. Everything
  else in it is the owner's original text, untouched. Rendered via WeasyPrint using the site's
  actual brand fonts (`fonts-ibm-plex` apt package + the Big Shoulders/Plex Mono files already
  under `canvas-fonts/`), fonts embedded/subsetted, ~40KB. Linked from a 3rd hero CTA and a
  link-card (first in the list, above the app links) in Links. (`11a806e`)
- `@media print` pass added alongside it — hides `.topnav`/`.cta-row`/lightbox, `break-inside:
  avoid` on the card grids — for the case Nick prints the page itself instead of the PDF.
  (`11a806e`)
- Visit tracker: not implemented, owner decided it's not needed. Not gated anymore — off the
  list entirely unless the owner brings it back up.
- Stack still unchanged otherwise: single `index.html`, vanilla CSS + JS, zero dependencies,
  GitHub Pages.

**Carried from session 2** (all still live, untouched by session 3):

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

Nothing open right now — both 🔵 items from session 2 are resolved (one shipped, one dismissed
by the owner). Add new tasks here as they come up; keep the 🟢/🔵 convention for anything that
needs owner input first.

<details>
<summary>Closed tasks (session 3)</summary>

- [x] **Downloadable résumé PDF.** Shipped — `11a806e`. Turned out the "owner supplies the PDF"
  assumption below didn't apply as written: the owner instead said to adjust their existing CV
  (supplied earlier in the same chat, not on-page copy) and generate the PDF from that. Original
  task note, for context: *"Needs the owner to supply the actual PDF — not something an agent
  should generate or invent from the on-page copy. Once supplied: drop it at e.g.
  `assets/Nugroho-Pangestu-Resume.pdf`, add a link-card in the Links section plus maybe a hero
  CTA. A `@media print` pass isn't a bad idea either."* All of the mechanical part still applied
  as written once the source material question was settled.

- [x] **Visit tracker (e.g. GoatCounter).** Dismissed by the owner, not implemented — "I don't
  think it's needed." Don't re-suggest unless they bring it up again.

</details>

---

## REFERENCE (stable — read from the repo, not reproduced here)

- `README.md` — project pitch/structure overview.
- `images/README.md` — asset-naming convention for new exhibit screenshots.
- Live site: https://nuggetenak.github.io/Nugroho-Pangestu-Portofolio/
