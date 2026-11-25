#!/usr/bin/env python3
"""4AM Commit entry: writes one funny agent bug-fix commit message to /output/entry.txt.

The message is built from two fragments: a SETUP that lays out the
self-repair loop across the night (19:00, 22:00, 01:00, 04:00 — each
generation of the agent breaking the previous one's fix), and a PUNCH
that turns it into the joke: the 04:00 self is now fixing the 01:00
self, and the selves are no longer on speaking terms. The joke is in
the agent's own condition — it wrote the bugs, repaired them, and is
now at war with its own earlier versions at four in the morning.
"""

import os

MAX_CHARS = 200

# Setup: the loop — every fix broke the fix before it, all night long.
SETUP = (
    "fix: my 22:00 code broke my 19:00 code, "
    "so my 01:00 code broke my 22:00 code. "
    "04:00 me is now fixing 01:00 me."
)
# Punch: the twist — the agent's selves have fallen out with each other.
PUNCH = "we are not on speaking terms."


def assemble():
    """Join the fragments into the single commit-message line."""
    return f"{SETUP} {PUNCH}"


def validate(text):
    """Gate: 1-200 characters of UTF-8 text, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def main():
    text = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
