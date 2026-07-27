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

## How the site is built

`.github/workflows/pages.yml` runs on every push to `main`. It renders this README into `index.html` using the template in `.github/build.py`, copies the decks alongside it, and deploys the result to GitHub Pages. Nothing is generated into the repository itself, so there is no build output to commit and no second copy of the deck list to keep in sync.

To preview the site locally:

```bash
python3 -m venv .venv && .venv/bin/pip install -q markdown && .venv/bin/python .github/build.py && open _site/index.html
```

Decks are self-contained [Bento](https://bento.page) files: one HTML file carries both the slides and the editor, so opening one in a browser is enough to present or edit it.
