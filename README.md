# talks

Slide decks I have presented, kept as an archive.

**Published at [felixmil.github.io/talks](https://felixmil.github.io/talks/).** Open a deck there to view or present it in the browser, no download needed.

Every deck here is a **point-in-time snapshot**, not maintained documentation. A deck is correct on the day it was given and is expected to go stale afterwards. Nothing in this repository should be treated as current: when a deck and a live source disagree, the live source wins. Durable content (decisions, rationale, instructions) belongs in the relevant project's README, docs, or decision records, not here.

## Convention

- One file per deck, flat at the repository root: `<YYYY-MM-DD>-<slug>.<ext>`. The date prefix keeps them in chronological order.
- The date in the filename is the date presented, and it is the staleness signal. Never rename a deck to drop it.
- Decks are not edited after the fact. If the content needs to change, that is a new deck with a new date.
- Adding a deck means committing the file and adding a row to the table below and a block in `index.html`. Both lists are hand-maintained.
- Leave `.nojekyll` in place. It stops GitHub Pages from running Jekyll, which would otherwise try to interpret the `{{page}}` and `{{title}}` tokens inside a deck as its own template syntax and corrupt the file.

## Decks

| Date | Deck | Context |
| --- | --- | --- |
| 2026-07-27 | [R-universe for the OSP R packages](2026-07-27-r-universe-for-osp.bento.html) | Proposal walkthrough for the OSP maintainers. Covers what R-universe is, what it changes for dependency resolution, why builds pass while `R CMD check` does not, and the remaining steps. Status shown is as of 2026-07-21; the live checklist is [OSP r-universe issue #2](https://github.com/Open-Systems-Pharmacology/open-systems-pharmacology.r-universe.dev/issues/2). |

## Formats

`.bento.html` decks are self-contained [Bento](https://bento.page) files: one HTML file carries both the slides and the editor, so opening it in a browser is enough to present or edit it, with nothing to install.

The links in the table above point at the files on GitHub, which shows their source rather than rendering them. To actually view a deck, use [the published site](https://felixmil.github.io/talks/), or clone the repository and open the file locally.
