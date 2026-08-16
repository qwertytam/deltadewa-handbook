---
description: Scaffold a new handbook page with front matter, nav entry, Part index link and a house-style skeleton
argument-hint: "[part-N] [slug] [\"Nav Title\"]"
disable-model-invocation: true
---

Create a new page: part `$0`, slug `$1`, nav title `$2`.

Load `.claude/skills/handbook-style/SKILL.md` first and follow it.

1. Create `docs/$0/$1.md` with front matter `title: "$2"` and a body that
   starts at `##`. Never add an `#` heading.
2. Add the page to `nav:` in `mkdocs.yml`, inside the `$0` block, positioned
   where a reader would expect it rather than appended at the end.
3. If `docs/$0/index.md` enumerates the Part's pages, add it there too.
4. Draft the skeleton — for a metric page: definition, formula, worked
   example, interpretation, target band, failure modes. For a mechanics page:
   what it is, how it behaves, what the operator does about it.
5. Leave no placeholder text in `docs/` — no `TODO`, no `TBD`. If a section
   cannot be written yet, do not create the section.
6. Run `/verify`. An orphaned page or a missing nav entry fails the strict
   build, so this catches step 2 going wrong.

Report the created path, the nav position, and anything you could not write
without maintainer input.
