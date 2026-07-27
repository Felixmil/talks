# talks

Slide decks I have presented, kept as an archive.

**Published at [felixmil.github.io/talks](https://felixmil.github.io/talks/).** Open a deck there to view or present it in the browser, no download needed.

## Decks

### [R-universe for the OSP R packages](2026-07-27-r-universe-for-osp.bento.html)

**2026-07-27.** Proposal walkthrough for the Open Systems Pharmacology maintainers: what R-universe is, what it changes for dependency resolution, why builds pass while `R CMD check` does not, and the remaining steps to full adoption.

Status shown is as of 2026-07-21; the live checklist is [OSP r-universe issue #2](https://github.com/Open-Systems-Pharmacology/open-systems-pharmacology.r-universe.dev/issues/2).

## Convention

- One file per deck, flat at the repository root: `<YYYY-MM-DD>-<slug>.<ext>`. The date prefix keeps them in chronological order.
- The date in the filename is the date presented, and it is the staleness signal. Never rename a deck to drop it.
- Decks are not edited after the fact. If the content needs to change, that is a new deck with a new date.
- Adding a deck means committing the file and adding a section under **Decks** above. That is the only list to maintain, since the site is generated from this file.

## Formats

Two kinds of deck live here, and both end up as a single HTML file:

- **Bento** (`.bento.html`), self-contained already: one file carries both the slides and the editor, so opening it in a browser is enough to present or edit it.
- **Quarto** (`.qmd`), rendered at build time. Set `embed-resources: true` in the deck's YAML header so it renders to one file like the rest. If it does not, the sidecar `_files` directory is copied too and the deck still works.

## How the site is built

`.github/workflows/pages.yml` runs on every push to `main`. It calls `.github/build.R`, which converts this README into `index.html` using `.github/template.html`, renders any Quarto decks, copies the Bento decks through untouched, and deploys the result to GitHub Pages.

Nothing is generated into the repository itself, so there is no build output to commit and no second copy of the deck list to keep in sync.

To preview the site locally, with R and Quarto installed:

```bash
Rscript .github/build.R && open _site/index.html
```
