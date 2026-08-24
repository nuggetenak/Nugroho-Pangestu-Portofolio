# HANDOFF.md — Nugroho-Pangestu-Portofolio

> ## 🟢 Session 6 done — third exam pass, Links redesigned — 2026-08-24
> A **third junior passed** the SSW exam on 24 Aug 2026 — four people total now. Count updated
> everywhere. Links section redesigned from eleven flat rows into grouped blocks, Skills
> regrouped with the owner's tool list, availability confirmed and published.
>
> Session 5's structural work still stands: **Nugget Nihongo is the platform**; SSW Konstruksi,
> the Anki Deck Series and future SSW tracks are *inside* it. Figures verified from the repo.
>
> **🔵 Two open items** in ACTIVE TASKS. Everything else is shipped.

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

## CURRENT STATE (2026-08-24, end of session 5)

**Project hierarchy — this is the thing to get right** (`21b1757`)

```
Nugget Nihongo ................. the platform. PAUSED Apr 2026.
├── SSW Konstruksi ............. LIVE. 3 exam passes. The track that shipped.
├── Anki Deck Series ........... 2 SHIPPED (1,861-card SSW infra, 1,031-card bunka)
└── Further SSW tracks ......... ROADMAP
```

Sessions 1–4 all treated SSW Konstruksi as the top-level project and the decks and corpus as
unrelated side work. That was wrong and the owner corrected it. `#flagship` is now the
platform with a system map; `#ssw` is a separate section for the track. SSW stays high on the
page on purpose — it's the node with verifiable proof — but it is no longer presented as the
parent.

**Exam passes — the headline proof, keep it exact** (`0f1ebcd`)

Four people have passed the SSW Konstruksi Lifeline & Peralatan exam using this content:
the owner (27 Apr 2026), two mentees (20 Aug 2026), and a third mentee (24 Aug 2026). All
three mentees studied the **v87** build, not v4.23.0. Phrasing across the site is "three
juniors" / "four people" / "three sittings" — if a fourth mentee passes, note that eight
separate strings carried the previous count and `grep -n '3-for-3\|three juniors\|4 exam
passes\|four people'` is the way to find them all.

**Verified figures — do not re-guess these** (all counted from the repo, session 5)

| Figure | Value | Source of truth |
|---|---|---|
| Research corpus | **747** entries, 43 clusters, ~45% DOI | `corpus/v17-pass15` → `corpus/bibliography/MASTER-BIBLIOGRAPHY-FINAL.md`, STATISTICS table, v7 / 17 Apr 2026 |
| Platform vocabulary | **2,692** | `public/data/vocab/vocab-n*.js` generated headers |
| Platform grammar | **859** | `public/data/grammar/grammar-n*.js` generated headers |
| Project start | **Feb 2026** | repo starts 22 Mar 2026 but already at v14.27.2 — earlier history predates this repo |
| Freeze date | **23 Apr 2026** | last commit on `origin/develop` |

Numbers that were circulating and are **wrong**: 880 sources (overclaim), 736 (stale — that's
the live site's copy, which is a v15.7.0 build behind the v7 bibliography), 763 (owner's
recollection), "1,800+ vocab / 450+ grammar" (stale README on nugget-nihongo).

**"DOI-verified" was an overclaim.** The corpus card and résumé both described the corpus as
DOI-verified. Only ~336 of 747 entries (45%) carry a DOI and 42 verifications are pending.
Now stated as measured. Don't let this regress — it's the kind of claim that collapses in an
interview.

**The paused platform is linked, deliberately.** The owner chose to show it honestly rather
than hide it. Its interface is complete and clickable but it stopped mid content-database
migration, so every list reads zero. The `.heads-up` block in `#flagship` and the link-card
sub-text both warn about this before anyone clicks. **Do not remove those warnings** — an
unlabelled link to an app that appears empty is worse than no link.

**Résumé — now two pages** (`21b1757`)

- Still the ATS/Kinobi contract in `assets/resume-src/README.md`. Unchanged constraints.
- Two pages because content grew (platform parent entry, Doc.Mentation, expanded tools). Type
  relaxed from 9.35pt/1.27 to 10pt/1.38 — a two-page CV has no reason to be cramped.
- `h2 { break-after: avoid }` and `.entry/.edu/.kv { break-inside: avoid }` added so the break
  lands at a section boundary. It currently falls before EDUCATION. **If you edit content,
  check where the break moves** — a section splitting mid-list looks careless.
- `ats_check.py` caught `exam-mockup` parsing as `exammockup`; reworded. Re-run after any edit.

**Site polish carried from session 4** (all still live): Termux removed, English-only UI
strings, skip link, lightbox focus trap, per-section `aria-label`s, canonical, `theme-color`,
Person schema, `@media print`, WebP via `<picture>`, `icons/`.

---

## ACTIVE TASKS

- [ ] 🔵 **Confirm the Doc.Mentation date range.** Currently `2019 – 2021` on both the CV and
  the timeline. The owner first said "from SMA (2017) until graduating 2020", then corrected
  his schooling to SMA 2019–2021 — which makes the videography dates ambiguous between
  *2017–2020* (the years as he first recalled them) and *2019–2021* (SMA start to graduation,
  following the correction). 2019–2021 was used because he framed the period by his schooling.
  **One number, needs his word.** Note it overlaps Cerita Hati (12/2020–05/2023), which is
  plausible but worth him seeing.

- [ ] 🔵 **Device constraint — owner's call, deliberately not published.** The owner mentioned
  his only constraint is hardware: he works from a phone, no laptop. The site already frames
  this as a strength ("built from a phone, no laptop", "0 lines hand-coded"). It was **not**
  added anywhere as a limitation, because restating it as a constraint would undercut the
  framing that's already working. If the owner wants it disclosed to the employer, that's a
  conversation for the interview, not a line on the portfolio — but flag it to him again if
  he asks about equipment.

- [ ] 🔵 **Owner to check both Instagram accounts are public** and read well top-to-bottom.
  `@nugroho_pangestu__` is personal-account-shaped; a recruiter will scroll all of it. It is
  now labelled "Personal account" rather than "photography & cinematography" — the owner
  confirmed it isn't a portfolio. `@doc.mentation` is the stronger link and now leads the
  Visual work group; it's also the one on the résumé contact line. Instagram blocks automated
  access so neither could be verified from here.

- [ ] 🔵 **Name the role.** Also from session 4. The hero says "prepared for Nick" but never
  names the position. Sharper if named, but only if this link isn't being reused elsewhere.

<details>
<summary>Closed tasks (sessions 3–5)</summary>

- [x] **Availability.** Confirmed by the owner and published — Mon–Fri 1pm–6pm on-site in
  Canggu, Bali-based, no relocation. In the contact block at the top of `#links`.
- [x] **Links section too flat.** Redesigned session 6, `0f1ebcd`.
- [x] **Site skills out of sync with the résumé.** Fixed session 6 — five labelled tiers,
  tools added, Adobe marked basic.
- [x] **Project hierarchy misrepresented.** Fixed session 5, `21b1757`.
- [x] **Corpus / platform figures wrong.** Re-counted session 5. See table above.
- [x] **Add Doc.Mentation, Instagram, videography.** Shipped session 5.
- [x] **Education dates.** Owner confirmed the CV was already right — SMP 2016–2019, SMA
  2019–2021. Closed, don't re-flag.
- [x] **Résumé design drift → ATS/Kinobi.** Session 4, `2a66595`.
- [x] **Remove "Termux".** Session 4, `b1b601b`. `grep -ri termux` is clean.
- [x] **Downloadable résumé PDF.** Session 3, `11a806e`.
- [x] **Visit tracker.** Dismissed by the owner. Don't re-suggest.

</details>

---

## REFERENCE (stable — read from the repo, not reproduced here)

- `README.md` — structure, editing, verification commands, deploy.
- `assets/resume-src/README.md` — résumé design contract, rebuild, verification. **Required
  reading before any résumé change.**
- `images/README.md` — asset-naming convention for new exhibit screenshots.
- Live site: https://nuggetenak.github.io/Nugroho-Pangestu-Portofolio/
