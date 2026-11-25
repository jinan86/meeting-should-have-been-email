#!/usr/bin/env python3
"""Write the final one-line entry for make.fun competition
u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9
(The Meeting That Should Have Been an Email) to /output/entry.txt.

Stdlib only, fully deterministic: the entry is a fixed string constant,
so every run writes byte-identical output.
"""

import os

ENTRY = (
    "The calendar invite had an agenda, a purpose, and a clear decision "
    "to make, so we spent fifty minutes confirming none of us had opened it."
)


def main() -> None:
    # Gate self-check (mirrors the competition gate): UTF-8, one line,
    # 1-200 characters, not only whitespace.
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")  # raises if not valid UTF-8

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
