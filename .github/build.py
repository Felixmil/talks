#!/usr/bin/env python3
"""Build the Pages site: render README.md into index.html and copy the decks alongside it.

The README is the single source for the site's content. The leading H1 is lifted out
to become the page header, so the heading is not repeated in the body.
"""

import pathlib
import re
import shutil

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="Slide decks I have presented, archived by date.">
<style>
  :root {
    --bg: #0B1120;
    --panel: #141C2E;
    --line: rgba(140,160,190,0.16);
    --text: #EEF2F8;
    --muted: #93A0B5;
    --body: #D7DEEA;
    --accent: #4C8DFF;
    --mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    --sans: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; padding: 0 24px 96px;
    background: var(--bg); color: var(--body);
    font-family: var(--sans); line-height: 1.65;
    -webkit-font-smoothing: antialiased;
  }
  .wrap { max-width: 760px; margin: 0 auto; }

  header { padding: 88px 0 0; }
  .mark {
    display: inline-flex; align-items: center; gap: 10px;
    font-size: 13px; font-weight: 700; letter-spacing: 2.5px;
    color: var(--accent); text-transform: uppercase;
  }
  .mark::before { content: ""; width: 10px; height: 10px; border-radius: 50%; background: var(--accent); }
  header h1 {
    font-size: clamp(38px, 7vw, 56px); font-weight: 900;
    margin: 18px 0 0; letter-spacing: -0.02em; color: var(--text);
  }

  .md > p:first-of-type { font-size: 19px; color: var(--muted); margin-top: 14px; }

  .md h2 {
    font-size: 13px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;
    color: var(--muted); margin: 60px 0 0; padding-bottom: 12px;
    border-bottom: 1px solid var(--line);
  }
  .md h3 { font-size: 23px; font-weight: 700; color: var(--text); margin: 34px 0 0; }
  .md h3 a { color: inherit; text-decoration: none; }
  .md h3 a:hover { color: var(--accent); }
  .md p { margin: 10px 0 0; }
  .md ul { margin: 14px 0 0; padding-left: 20px; }
  .md li { margin: 8px 0 0; }
  .md li::marker { color: var(--accent); }
  .md strong { color: var(--text); }
  .md a { color: var(--accent); }

  .md code {
    font-family: var(--mono); font-size: 0.88em;
    background: var(--panel); border: 1px solid var(--line);
    padding: 1px 6px; border-radius: 5px; color: var(--text);
  }
  .md pre {
    background: var(--panel); border: 1px solid var(--line);
    border-radius: 12px; padding: 18px 20px; overflow-x: auto; margin: 18px 0 0;
  }
  .md pre code { background: none; border: 0; padding: 0; font-size: 14px; }

  .md table { width: 100%; border-collapse: collapse; margin: 18px 0 0; display: block; overflow-x: auto; }
  .md th, .md td { text-align: left; padding: 10px 14px; border-bottom: 1px solid var(--line); }
  .md th { color: var(--muted); font-size: 13px; text-transform: uppercase; letter-spacing: 1px; }

  footer { margin-top: 72px; padding-top: 20px; border-top: 1px solid var(--line); color: var(--muted); font-size: 14px; }
  footer a { color: var(--accent); }
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div class="mark">Talks</div>
    <h1>__HEADING__</h1>
  </header>
  <div class="md">
__CONTENT__
  </div>
  <footer>
    <p>Source: <a href="https://github.com/Felixmil/talks">github.com/Felixmil/talks</a></p>
  </footer>
</div>
</body>
</html>
"""


def main() -> None:
    html = markdown.markdown(
        (ROOT / "README.md").read_text(encoding="utf-8"),
        extensions=["tables", "fenced_code", "sane_lists"],
    )

    # Lift the leading <h1> out of the body and use it as the page header.
    heading = "talks"
    match = re.match(r"\s*<h1>(.*?)</h1>", html, flags=re.DOTALL)
    if match:
        heading = match.group(1).strip()
        html = html[match.end():]

    page = (
        TEMPLATE.replace("__TITLE__", f"{heading} — Felix MIL")
        .replace("__HEADING__", heading)
        .replace("__CONTENT__", html)
    )

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    (OUT / "index.html").write_text(page, encoding="utf-8")

    decks = sorted(ROOT.glob("*.bento.html"))
    for deck in decks:
        shutil.copy2(deck, OUT / deck.name)

    print(f"built _site/index.html ({len(page):,} bytes) + {len(decks)} deck(s)")
    for deck in decks:
        print(f"  {deck.name} ({deck.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
