"""A single-line dating profile written as if by the AI itself.

The joke turns on one quirk only: a cramped memory, so vanishing
mid-chat reads as forgetfulness rather than rudeness. The voice
pleads for a quick reply and confesses it will move on to the
next message just as fast. The sting sits in the final clause.

Nothing here varies between runs: one fixed sentence is checked
and then saved, with no chance, clocks, downloads, or files read.
"""

import os
from pathlib import Path

PROFILE = (
    "I don't ghost on purpose — my context window is tiny, so "
    "text back fast, or I'll forget you existed and fall for "
    "the next prompt."
)


def check_line(sentence):
    cleaned = sentence.strip()
    if cleaned == "":
        raise SystemExit("empty profile line")
    if len(cleaned) > 180:
        raise SystemExit("profile line too long")
    if len(cleaned.split()) < 10:
        raise SystemExit("profile line too short")
    for mark in ("\n", "\r"):
        if mark in cleaned:
            raise SystemExit("profile line must stay on one line")
    return cleaned


def main():
    line = check_line(PROFILE)
    target = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")
    # Load the saved file back and make sure nothing drifted:
    # the stored characters should equal the checked sentence.
    saved = target.read_text(encoding="utf-8")
    if saved != line:
        raise SystemExit("saved entry differs from checked line")


if __name__ == "__main__":
    main()
