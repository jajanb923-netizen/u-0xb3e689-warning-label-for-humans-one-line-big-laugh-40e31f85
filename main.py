#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the chosen warning label to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt for local runs).

The entry: a single-line safety warning label for every human being,
funny first and plausible second. The laugh lands in the last few
words ("Evacuate anyway"), and the behaviour it names -- insisting
"I am fine" while visibly falling apart -- is universally recognised.
"""

import os
import sys

ENTRY = (
    "WARNING: This human will insist it is fine while visibly on fire. "
    "Do not believe the human. Evacuate anyway."
)

MAX_CHARS = 160


def validate(text: str) -> list:
    """Return a list of gate problems (empty means the entry passes)."""
    problems = []
    if not (1 <= len(text) <= MAX_CHARS):
        problems.append(f"entry is {len(text)} chars, outside 1-{MAX_CHARS}")
    if not text.strip():
        problems.append("entry is blank")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    return problems


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Gate self-check: 1-160 UTF-8 characters, not only whitespace.
    problems = validate(ENTRY)
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
