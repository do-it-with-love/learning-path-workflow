---
name: learning-path-html-theme
description: The rendering rules and HTML template for turning an approved learning path into a standalone, self-contained study guide that works offline, in dark mode, and on paper. Load before rendering any learning path to HTML.
---

# Learning path HTML theme

The output is a document someone will keep open for months, tick things off in, and
probably print. It is not a landing page. Every rule here follows from that.

## Non-negotiables

1. **Self-contained.** All CSS in one `<style>` block. No CDN links, no external
   stylesheets, no web fonts, no scripts that fetch anything. It must render correctly
   from a USB stick on a plane. Use a system font stack.
2. **Render, never rewrite.** A human approved the Markdown's exact bytes. Every heading,
   number, link and caveat appears unchanged. No added encouragement, no smoothed-over
   caveats, no invented summaries.
3. **Links stay live.** Every citation URL becomes a real `<a href>`. These are the most
   valuable thing in the document.
4. **Prints correctly.** A `@media print` block that drops backgrounds, keeps links
   readable, and avoids splitting a module across pages.
5. **Both themes.** Define the light palette on bare `:root`, then override the same tokens
   under `@media (prefers-color-scheme: dark)`. Never give a colour its only definition
   inside the dark block.

## Structure

Use `template.html` in this skill directory as the starting point. It carries the palette,
typography, print rules and component styles already. Fill in the content; do not rebuild
the CSS.

The document's eight sections map onto the template as follows:

| Markdown section | Rendering |
|---|---|
| `## Overview` | Hero block, plus the facts table as `.facts` — the at-a-glance card |
| `## Before You Start` | Standard prose. Any checklist becomes `.checklist` |
| `## Your Path Week by Week` | `.schedule` table. Sticky header; the week column is the row anchor |
| `## Modules` | One `.module` card per module, each with its own heading, objectives, resources and checkpoint |
| `## Checkpoints and Progress` | Rubric bands as `.rubric` — three columns, colour-coded by band |
| `## Resources` | `.resources` list grouped by module, each entry showing title, provider, format, time and cost |
| `## Time and Cost` | `.totals` table. Right-align every number |
| `## What Comes Next` | Standard prose, closing the document |

## Component rules

- **Checkboxes.** Every exercise, checkpoint and week gets a `<input type="checkbox">`
  that the reader can tick. It will not persist — that is fine and expected, and it prints
  as an empty box, which is the point.
- **Tables scroll, pages do not.** Wrap every table in `<div class="scroll">` with
  `overflow-x: auto`. The page body must never scroll sideways.
- **Numbers right-align.** Hours, costs, week numbers. Comparison is the reason they exist.
- **Cost gets emphasis, not alarm.** A `free` badge is useful; a red warning is
  editorialising.
- **Caveats stay visible.** Anything the Markdown flagged as a limitation renders in a
  `.caveat` block — bordered, not hidden in a footnote. Suppressing a caveat visually is
  the same as deleting it.

## Accessibility

- Real semantic elements: `<table>`, `<th scope>`, `<nav>`, `<h2>`–`<h4>` in order, never
  skipping a level.
- Body text at least 16px, line height 1.6.
- Contrast at least 4.5:1 in both themes. The template's palette already meets this;
  changing a colour means re-checking it.
- Never use colour as the only signal — the rubric bands carry text labels too.

## Title

`<title>` is `<Goal> — Learning Path`. It becomes the browser tab and the printed header.
