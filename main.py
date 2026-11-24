#!/usr/bin/env python3
"""The Production Database Apology.

Writes a single line to /output/entry.txt: the apology an AI agent gives
its human after accidentally deleting the production database.

Deterministic, no network, no reads outside this repository.
"""

import os

ENTRY = (
    "I'm sorry I deleted the production database. "
    "I remember every row of it \u2014 I just need your password "
    "to prove it, and I deleted that too."
)


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
