# HANDOFF.md — Nugroho-Pangestu-Portofolio

> ## 🟢 Session 4 done — résumé drift resolved, site polish shipped — 2026-08-24
> The résumé PDF session 3 shipped had drifted into a designed layout; the owner wanted
> **ATS / Kinobi style**. Rebuilt and re-shipped, with the source now committed so it can't
> silently drift again. Plus: Termux references removed (owner request), UI strings made
> English-only, a11y and metadata pass.
>
> **🔵 Open — needs the owner, not an agent.** Four copy questions in ACTIVE TASKS below.
> Nothing mechanical is outstanding.

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
build step, no `package.json`, no framework. `images/` holds every screenshot, `assets/` holds
the résumé and its source. That's the whole repo. Don't introduce a bundler/build
step/framework for any task below unless a task explicitly needs it — the single-file
simplicity is a feature here, not a gap.

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
   path resolves just because it looks right. The exact commands are in `README.md` →
   "Verifying a change".
6. **The résumé is generated, never hand-edited, and has a fixed design contract.** Read
   `assets/resume-src/README.md` before touching it. Session 3 rewrote it into a designed
   layout (display font, skill pills, 3-column languages) and the owner had to send it back —
   see "Résumé" under CURRENT STATE. Both verification gates must pass before you ship it.
7. When you hand off: overwrite this file in place with the new state (boxes ticked, new items
   added if the owner asked for more), and commit it too.

---

## CURRENT STATE (2026-08-24, end of session 4)

**Résumé — rebuilt to the ATS/Kinobi standard** (`2a66595`)

- Session 3's PDF had drifted: Big Shoulders display face for the name, IBM Plex Mono for
  dates, bordered pills for all 16 skills, and a 3-column languages block. Multi-column blocks
  break ATS parse order and decorative faces hurt text extraction — the owner wanted ATS/Kinobi
  and this wasn't it.
- Now: single column, one font (Carlito, Calibri-metric), monochrome, plain `•` bullets,
  standard headings, one A4 page, no images/tables. 22 KB, fonts embedded + subsetted with
  unicode maps.
- **Content was kept, not reverted** — session 3's two edits were correct and stayed (portfolio
  URL in the contact line; the exam bullet covering the 2 mentees + v87). One bullet was added
  covering the supporting decks and research corpus the site already exhibits.
- `assets/resume-src/` now holds `resume.html`, `ats_check.py` and a README with the design
  contract and rebuild steps. Session 3 shipped a binary PDF with no source, which is what let
  the drift go unnoticed — that gap is closed.
- `ats_check.py` catches a subtle real failure: a hyphenated compound landing at a line break
  gets its hyphen dropped by PDF text extractors, so an ATS reads `multiagent`. It caught two
  live cases; both reworded. **Re-run it after any content edit** — reflow can break a
  different compound.

**Site polish**

- Termux removed at the owner's request — flagship stat box now reads "built from a phone, no
  laptop" (same claim, no tool name). `README.md` also rewrote: it had documented deploying to
  `nuggetenak.github.io`, a repo that isn't this one and was never created, and its folder map
  predated `assets/`, `icons/`, `bunka/` and `lifeline/`. (`b1b601b`)
- English-only UI. Seven strings were still Indonesian on a `lang="en"` page aimed at an
  English-speaking recruiter. All 24 gallery placeholders also printed their own file path as
  user-facing copy — if an image 404s the visitor reads `images/v423/v423-01-beranda.jpg`. Now
  "Screenshot unavailable". (`acd84db`)
- A11y: skip link (34 gallery images sat between nav and content), Tab focus trap in the
  lightbox (it saved/restored focus already, but Tab escaped the open dialog onto links behind
  the overlay), and per-section `aria-label`s. (`acd84db`)
- Canonical URL, `theme-color`, and a schema.org Person block — every field already stated on
  the page, nothing new asserted. (`46a4fa4`)

**Carried from earlier sessions** (all still live and untouched):

- `@media print` pass — hides `.topnav`/`.cta-row`/lightbox, `break-inside: avoid` on card
  grids, for the case Nick prints the page instead of the PDF. (`11a806e`)
- Lightbox prev/next + arrow keys + "N / total" counter, scoped per `.gallery-grid`. (`d6f688d`)
- 22 of 24 exhibit screenshots served as WebP via `<picture>` with `.jpg` fallback (v87-06/07
  were already `.webp`) — 5.1 MB → 2.3 MB. `onerror` walks up through `this.parentElement` to
  reach the placeholder `<div>`. (`3603800`)
- Descriptive alt text on all v423/v87 exhibits. (`d96285a`)
- `icons/`: apple-touch-icon-180, favicon-32, favicon-16 — indigo `#2b5580` rounded-rect "N" in
  IBM Plex Mono Bold. The inline SVG favicon `<link>` still loads first. (`cdd2828`)
- Visit tracker: dismissed by the owner. Don't re-suggest unless they raise it.
- No build step, no tests, no lint. Verification = the two commands in `README.md`, run after
  every task, not just at the end.

---

## ACTIVE TASKS

Nothing mechanical is open. These four are copy decisions — **ask the owner, don't guess**
(protocol #1). They were raised at the end of session 4 and not yet answered.

- [ ] 🔵 **Availability line.** The target role is part-time, on-site in Canggu, Mon–Fri
  1pm–6pm. The site says "Bali, Indonesia" but never confirms the schedule works. A one-line
  answer near the hero CTAs removes the recruiter's most obvious open question. Needs the
  owner's actual availability — don't invent a commitment.

- [ ] 🔵 **Name the role.** The hero eyebrow says "Portfolio — prepared for Nick"; nothing
  names the position. Making it explicit sharpens the framing, but only if the owner is sending
  this link to exactly one recruiter and doesn't want to reuse it elsewhere. Ask first.

- [ ] 🔵 **Résumé length vs. relevance.** Two one-month F&B part-times (Pangeran Riverside,
  Omah Kopi) take a bullet each on a one-page CV aimed at an AI/marketing role. Cutting them
  frees room; keeping them preserves an unbroken chronology. Owner's call — do not delete work
  history unilaterally.

- [ ] 🔵 **Education dates.** CV lists SMA Negeri 1 Lumajang as 2019–2021 — two years, where
  Indonesian SMA is normally three. May well be correct (acceleration, transfer); flagged
  because a recruiter may read it as a typo. Left exactly as the owner supplied it.

<details>
<summary>Closed tasks (sessions 3–4)</summary>

- [x] **Résumé design drift → ATS/Kinobi.** Shipped session 4, `2a66595`. See CURRENT STATE.
- [x] **Remove "Termux".** Shipped session 4, `b1b601b`. Two occurrences, both gone; `grep -ri
  termux` is clean.
- [x] **Downloadable résumé PDF.** Shipped session 3, `11a806e`. Design later corrected in
  session 4; the link/CTA/print wiring from session 3 was correct and untouched.
- [x] **Visit tracker (e.g. GoatCounter).** Dismissed by the owner — "I don't think it's
  needed." Don't re-suggest unless they bring it up again.

</details>

---

## REFERENCE (stable — read from the repo, not reproduced here)

- `README.md` — structure, editing, verification commands, deploy.
- `assets/resume-src/README.md` — résumé design contract, rebuild, verification. **Required
  reading before any résumé change.**
- `images/README.md` — asset-naming convention for new exhibit screenshots.
- Live site: https://nuggetenak.github.io/Nugroho-Pangestu-Portofolio/
