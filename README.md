# talks

Slide decks I have presented, kept as an archive.

Every deck here is a **point-in-time snapshot**, not maintained documentation. A deck is correct on the day it was given and is expected to go stale afterwards. Nothing in this repository should be treated as current: when a deck and a live source disagree, the live source wins. Durable content (decisions, rationale, instructions) belongs in the relevant project's README, docs, or decision records, not here.

## Convention

- One file per deck, filed under the year it was given: `<year>/<YYYY-MM-DD>-<slug>.<ext>`.
- The date in the filename is the date presented, and it is the staleness signal. Never rename a deck to drop it.
- Decks are not edited after the fact. If the content needs to change, that is a new deck with a new date.

## Decks

| Date | Deck | Context |
| --- | --- | --- |
| 2026-07-27 | [R-universe for the OSP R packages](2026/2026-07-27-r-universe-for-osp.bento.html) | Proposal walkthrough for the OSP maintainers. Covers what R-universe is, what it changes for dependency resolution, why builds pass while `R CMD check` does not, and the remaining steps. Status shown is as of 2026-07-21; the live checklist is [OSP r-universe issue #2](https://github.com/Open-Systems-Pharmacology/open-systems-pharmacology.r-universe.dev/issues/2). |

## Formats

`.bento.html` decks are self-contained [Bento](https://bento.page) files: open one in a browser to present or edit it, no install required.
