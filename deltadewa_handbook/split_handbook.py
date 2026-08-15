r"""Split a single HANDBOOK.md into one *.md page per H3.

Split a single HANDBOOK.md into one markdown page per H3, grouped by H2 Part.

Assumptions:
- Source is markdown with md headings (# H1, ## H2 Part, ### H3 Chapter).
- Content between an H2 and its first H3 becomes `<part-slug>/index.md`.
- H1 (title), Preface, Quick Start, Appendices (H2), Footnotes handled
specially.
- Cross-refs like [text](#anchor) that point to now-split targets are rewritten
  to plain-text "See <text>" (anchors won't resolve across pages).
- Literal '$' in prose is escaped as '\$' to keep parser happy.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# ------------- Config -------------

SRC = Path("HANDBOOK.md")
OUT_ROOT = Path("docs")  # workspace root for output markdown files
TOP_GROUP = "Handbook"  # sidebar top-level group name

# Regex helpers
H1_RE = re.compile(r"^#\s+(.+?)\s*$")
H2_RE = re.compile(r"^##\s+(.+?)\s*$")
H3_RE = re.compile(r"^###\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^(```|~~~)")
MD_LINK_ANCHOR_RE = re.compile(r"\[([^\]]+)\]\(#([^)]+)\)")
BARE_AUTOLINK_RE = re.compile(r"<(https?://[^>]+)>")

# Escape $ used as currency/prose (not inside code fences or $...$ math).
# Heuristic: escape "$" followed by a digit or letter that isn't already
# escaped.
CURRENCY_DOLLAR_RE = re.compile(r"(?<!\\)\$(?=\d|[A-Za-z])")


# ------------- Data model -------------


@dataclass
class Chapter:
    """A single H3 chapter, with its lines of content."""

    title: str
    lines: list[str] = field(default_factory=list)

    @property
    def slug(self) -> str:
        """Chapter title to slug for filename.

        Chapter title -> slug for filename (e.g. '### 1.1 Overview' ->
        '1-1-overview').
        """
        return slugify(self.title)


@dataclass
class Part:
    """A single H2 part, with its introduction and chapters."""

    title: str  # e.g. "PART VII — Practical Implementation"
    # intro lines between H2 and first H3
    intro_lines: list[str] = field(default_factory=list)
    chapters: list[Chapter] = field(default_factory=list)

    @property
    def slug(self) -> str:
        """'PART VII — Practical Implementation' -> 'part-7'."""
        m = re.match(r"PART\s+([IVXLCDM]+)", self.title, re.I)
        if m:
            return f"part-{roman_to_int(m.group(1))}"
        if self.title.upper().startswith("APPENDICES"):
            return "appendices"
        return slugify(self.title)


# ------------- Utilities -------------


def roman_to_int(s: str) -> int:
    """Convert a Roman numeral string to an integer."""
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total, prev = 0, 0
    for ch in reversed(s.upper()):
        v = vals[ch]
        total += -v if v < prev else v
        prev = v
    return total


def slugify(text: str) -> str:
    """Convert a string to a URL-friendly slug (lowercase, hyphenated)."""
    text = re.sub(r"[^\w\s-]", "", text.lower())
    text = re.sub(r"[\s_-]+", "-", text).strip("-")
    return text


def escape_currency_dollars(text: str) -> str:
    r"""Escape '$' that would otherwise break *.md (e.g. $10M -> \\$10M)."""
    out, in_fence = [], False
    for line in text.splitlines(keepends=True):
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        out.append(CURRENCY_DOLLAR_RE.sub(r"\\$", line))
    return "".join(out)


def rewrite_cross_refs(text: str, known_anchors: set[str]) -> str:
    """Rewrite cross-references.

    [text](#anchor) -> either kept (if anchor is on same page)
    or 'See text'.
    """

    def repl(m: re.Match[str]) -> str:
        label, anchor = m.group(1), m.group(2)
        if anchor in known_anchors:
            return str(m.group(0))
        return f"See {label}"

    return MD_LINK_ANCHOR_RE.sub(repl, text)


def convert_bare_autolinks(text: str) -> str:
    """Convert bare autolinks.

    <https://example.com> -> [example.com](https://example.com) for
    safety.
    """

    def repl(m: re.Match[str]) -> str:
        url = m.group(1)
        display = re.sub(r"^https?://", "", url).rstrip("/")
        return f"[{display}]({url})"

    return BARE_AUTOLINK_RE.sub(repl, text)


# ------------- Parsing -------------


def parse_handbook(src: Path) -> tuple[str, list[Part]]:
    """Return (h1_title, parts)."""
    title = ""
    parts: list[Part] = []
    current_part: Part | None = None
    current_chapter: Chapter | None = None
    in_fence = False

    for raw in src.read_text(encoding="utf-8").splitlines():
        line = raw + "\n"

        # Track code fences so we don't parse headings inside them
        if FENCE_RE.match(raw.strip()):
            in_fence = not in_fence
            if current_chapter:
                current_chapter.lines.append(line)
            elif current_part:
                current_part.intro_lines.append(line)
            continue

        if not in_fence:
            if m := H1_RE.match(raw):
                title = m.group(1).strip()
                continue
            if m := H2_RE.match(raw):
                current_part = Part(title=m.group(1).strip())
                parts.append(current_part)
                current_chapter = None
                continue
            if m := H3_RE.match(raw):
                if current_part is None:
                    # Handle H3s before any H2 (Preface chapters) by
                    # synthesizing a "Preface" part.
                    current_part = Part(title="Preface")
                    parts.append(current_part)
                current_chapter = Chapter(title=m.group(1).strip())
                current_part.chapters.append(current_chapter)
                continue

        if current_chapter is not None:
            current_chapter.lines.append(line)
        elif current_part is not None:
            current_part.intro_lines.append(line)

    return title, parts


# ------------- Rendering -------------


def render_md(page_title: str, body: str, known_anchors: set[str]) -> str:
    """Return markdown text for a single page.

    Return markdown text for a single page, with frontmatter and rewritten
    links.
    """
    body = rewrite_cross_refs(body, known_anchors)
    body = convert_bare_autolinks(body)
    body = escape_currency_dollars(body)
    frontmatter = f'---\ntitle: "{page_title}"\n---\n\n'
    return frontmatter + body.lstrip("\n")


def write_part(
    part: Part,
    out_root: Path,
    known_anchors: set[str],
) -> list[Path]:
    """Write a single Part to disk, returning the list of written files."""
    written: list[Path] = []
    part_dir = out_root / part.slug
    part_dir.mkdir(parents=True, exist_ok=True)

    if part.intro_lines and any(line.strip() for line in part.intro_lines):
        intro_path = part_dir / "index.md"
        intro_path.write_text(
            render_md("Overview", "".join(part.intro_lines), known_anchors),
            encoding="utf-8",
        )
        written.append(intro_path)

    for ch in part.chapters:
        page_path = part_dir / f"{ch.slug}.md"
        page_path.write_text(
            render_md(ch.title, "".join(ch.lines), known_anchors),
            encoding="utf-8",
        )
        written.append(page_path)

    return written


# ------------- Navigation (docs.json) -------------


def build_nav(parts: list[Part], out_root: Path) -> str:
    """Build a navigation subtree.

    Build a navigation subtree for the mkdocs.yml file.
    """
    part_indent = "  - "
    page_indent = "    - "
    nav_tree: list[str] = []
    nav_tree.append("nav:")
    for part in parts:
        part_dir = out_root / part.slug
        nav_tree.append(f"{part_indent}'{part.title}':")
        if (part_dir / "index.md").exists():
            overview_path = f" '{part.slug}/index.md'"
            nav_tree.append(f"{page_indent}{overview_path}")
        nav_tree.extend(
            f"{page_indent}'{ch.title}': '{part.slug}/{ch.slug}.md'"
            for ch in part.chapters
        )  #
    return "\n".join(nav_tree)


# ------------- Main -------------


def main() -> int:
    """Split HANDBOOK.md into one *.md page per H3 chapter.

    Split HANDBOOK.md into one *.md page per H3 chapter grouped by H2 part.

    WARNING: This script is destructive: it overwrites the output directory.

    Note: Take care in which folder you run this script, as it will overwrite
    the output directory (docs/ by default). The script assumes that the source
    file (HANDBOOK.md) is in the current working directory.
    """
    if not SRC.exists():
        print(f"\nERROR: {SRC.absolute()} not found", file=sys.stderr)
        return 1

    title, parts = parse_handbook(SRC)
    print(f"Parsed H1: {title!r}")
    print(
        f"Found {len(parts)} parts, "
        f"{sum(len(p.chapters) for p in parts)} chapters total",
    )

    # Anchors that survive on the SAME page: only chapter-local ones. Anything
    # else in the source becomes plain-text "See X".
    known_anchors: set[str] = set()  # keep empty = strip all cross-page anchors

    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    for part in parts:
        paths = write_part(part, OUT_ROOT, known_anchors)
        print(f"  {part.slug}: {len(paths)} files")

    nav = build_nav(parts, OUT_ROOT)
    (OUT_ROOT / "nav.yml").write_text(
        nav,
        encoding="utf-8",
    )
    print(f"\nWrote nav skeleton to {OUT_ROOT / 'nav.yml'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
