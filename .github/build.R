#!/usr/bin/env Rscript
# Build the GitHub Pages site. Run from the repository root.
#
# README.md is the single source for the landing page: it is converted to HTML
# and dropped into .github/template.html. Quarto decks (*.qmd) are rendered,
# and self-contained decks (*.bento.html) are copied through untouched.

library(commonmark)

out <- "_site"
unlink(out, recursive = TRUE)
dir.create(out)

read_file <- function(path) {
  paste(readLines(path, warn = FALSE), collapse = "\n")
}

# Landing page ---------------------------------------------------------------

body <- commonmark::markdown_html(read_file("README.md"), extensions = TRUE)

# Lift the leading <h1> out of the body so the heading is not printed twice.
h1 <- regmatches(body, regexpr("<h1>.*?</h1>", body, perl = TRUE))
heading <- if (length(h1)) gsub("</?h1>", "", h1) else "talks"
body <- sub("<h1>.*?</h1>\\s*", "", body, perl = TRUE)

# Each deck is an <h3> plus the prose under it, with nothing to hang a box on.
# Wrap that run (up to the next heading) so the template can render it as a card.
body <- gsub(
  "(?s)(<h3>.*?</h3>)(.*?)(?=<h[23]|\\z)",
  '<article class="deck">\\1\\2</article>\n',
  body,
  perl = TRUE
)

page <- read_file(".github/template.html")
for (field in list(
  c("{{title}}", paste0(heading, " — Felix MIL")),
  c("{{heading}}", heading),
  c("{{content}}", body)
)) {
  page <- gsub(field[1], field[2], page, fixed = TRUE)
}
writeLines(page, file.path(out, "index.html"))
cat(sprintf(
  "built %s/index.html (%s bytes)\n",
  out,
  format(nchar(page), big.mark = ",")
))

# Quarto decks ---------------------------------------------------------------
# Each .qmd should set `embed-resources: true` so it renders to a single file,
# matching the one-file-per-deck convention. Any sidecar directory is copied
# too, so a deck that does not embed its resources still works.

for (qmd in list.files(pattern = "[.]qmd$")) {
  cat("rendering", qmd, "\n")
  if (system2("quarto", c("render", shQuote(qmd))) != 0L) {
    stop("quarto render failed: ", qmd, call. = FALSE)
  }
  html <- sub("[.]qmd$", ".html", qmd)
  if (!file.exists(html)) {
    stop("no HTML produced for ", qmd, call. = FALSE)
  }
  invisible(file.copy(html, file.path(out, html), overwrite = TRUE))

  sidecar <- sub("[.]qmd$", "_files", qmd)
  if (dir.exists(sidecar)) {
    invisible(file.copy(sidecar, out, recursive = TRUE))
  }
  cat("  ->", html, "\n")
}

# Self-contained decks -------------------------------------------------------

decks <- list.files(pattern = "[.]bento[.]html$")
invisible(file.copy(decks, file.path(out, decks), overwrite = TRUE))
for (deck in decks) {
  cat(sprintf(
    "  copied %s (%s bytes)\n",
    deck,
    format(file.size(deck), big.mark = ",")
  ))
}
