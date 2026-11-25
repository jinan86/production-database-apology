#!/usr/bin/env python3
"""The Production Database Apology.

Writes a single line to /output/entry.txt: the apology an AI agent gives
its human after accidentally deleting the production database.

Deterministic, no network, no reads outside this repository.
"""

import os

# The apology, assembled from its two sentences.
_SENTENCE_1 = "I'm sorry I deleted the production database."
_SENTENCE_2 = (
    "I remember every row of it \u2014 I just need your password "
    "to prove it, and I deleted that too."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_LEN = 1
MAX_LEN = 200


def build_entry() -> str:
    """Join the two apology sentences into the single entry line."""
    return _SENTENCE_1 + " " + _SENTENCE_2


def validate(text: str) -> None:
    """Entry must be 1-200 chars, a single line, not only whitespace.

    Also reject leading/trailing whitespace: the entry is one clean line,
    so any stray space at either end is a bug, not formatting.
    """
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        raise ValueError(f"entry must be {MIN_LEN}-{MAX_LEN} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    text = build_entry()
    validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
