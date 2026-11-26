#!/usr/bin/env python3
"""The Robot Apology — make.fun entry.

Writes a two-line robot confession to /output/entry.txt:
line 1 apologizes for one specific mistake, line 2 names the lesson
and what the robot will do differently.
Stdlib only.
"""

import os

ENTRY = (
    "I am sorry I set the heating to 31 degrees last night because "
    "I read the thermostat in Fahrenheit and thought the house was freezing.\n"
    "I have learned to convert every reading to Celsius and check it "
    "against the room before I act, and I will never change a setting "
    "by more than two degrees without asking first.\n"
)


def validate(text):
    """Mirror the sealed gate: UTF-8 text of 1-400 chars, not only
    whitespace, and exactly two lines (apology + lesson)."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > 400:
        raise ValueError("entry is %d chars, over the 400-char gate" % len(text))
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines, got %d" % len(lines))
    if not all(line.strip() for line in lines):
        raise ValueError("both lines must be non-blank")
    return True


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", path, len(ENTRY.encode("utf-8")), "bytes")


if __name__ == "__main__":
    main()
