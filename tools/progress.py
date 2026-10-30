#!/usr/bin/env python3
"""Regenerate the progress bars at the top of README.md.

The README holds two checklists (Alpha 0.1.0 and the main course list) between
marker comments. This script counts the checked items in each one and rewrites
the generated block between ``<!-- progress:start -->`` and
``<!-- progress:end -->``.

Usage:
    python3 tools/progress.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"

BAR_CELLS = 40
ITEM_RE = re.compile(r"^\s*-\s\[([ xX])\]", re.MULTILINE)
BLOCKS = (
    ("alpha", "Alpha 0.1.0", "tasks"),
    ("courses", "Main courses", "courses"),
)


def extract(text: str, name: str) -> str:
    """Return the slice of ``text`` between the given marker pair."""
    start_tag = f"<!-- progress:{name}:start -->"
    end_tag = f"<!-- progress:{name}:end -->"
    try:
        start = text.index(start_tag) + len(start_tag)
        end = text.index(end_tag, start)
    except ValueError as exc:  # pragma: no cover - only on a broken README
        raise SystemExit(f"error: missing progress markers for '{name}'") from exc
    return text[start:end]


def render_bar(percent: int) -> str:
    filled = round(percent / 100 * BAR_CELLS)
    return "\u2588" * filled + "\u2591" * (BAR_CELLS - filled)


def render_row(label: str, checked: int, total: int, unit: str) -> str:
    percent = 0 if total == 0 else round(checked * 100 / total)
    return f"{label:<13} [{render_bar(percent)}] {percent:>3}%  {checked}/{total} {unit}"


def main() -> int:
    text = README.read_text(encoding="utf-8")

    rows = []
    for name, label, unit in BLOCKS:
        items = ITEM_RE.findall(extract(text, name))
        checked = sum(1 for state in items if state in "xX")
        rows.append(render_row(label, checked, len(items), unit))

    generated = "```text\n" + "\n".join(rows) + "\n```"

    start_tag = "<!-- progress:start -->"
    end_tag = "<!-- progress:end -->"
    start = text.index(start_tag) + len(start_tag)
    end = text.index(end_tag, start)
    README.write_text(
        text[:start] + "\n\n" + generated + "\n\n" + text[end:],
        encoding="utf-8",
    )

    print(generated)
    return 0


if __name__ == "__main__":
    sys.exit(main())
