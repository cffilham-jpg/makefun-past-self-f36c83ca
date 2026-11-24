#!/usr/bin/env python3
"""Two lines to my past self.

Writes exactly two lines (one newline between them, no trailing newline)
to entry.txt under MAKEFUN_OUTPUT_DIR if set, else /output/entry.txt.
Python 3.13, standard library only.
"""

import os
import sys
import unicodedata

LINES = (
    "Don't throw away the notebook with the blue cover on the last day of school.",
    "Inside it were the only copies of the stories you ever wrote, and without them "
    "you spent ten years convincing yourself you were never a writer.",
)

MAX_CHARS = 280


def validate(text: str) -> None:
    """Reject text that is not exactly two clean lines within the limit."""
    if not text or not text.strip():
        raise ValueError("entry is empty or whitespace-only")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if text.count("\n") != 1:
        raise ValueError("entry must be exactly two lines")
    for ch in text:
        if unicodedata.category(ch) in ("Cc", "Cf", "Zl", "Zp"):
            raise ValueError(f"entry contains a control/format character: U+{ord(ch):04X}")


def main() -> int:
    text = "\n".join(LINES)
    validate(text)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
