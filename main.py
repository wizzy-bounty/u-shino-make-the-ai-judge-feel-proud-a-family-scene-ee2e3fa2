#!/usr/bin/env python3
"""Write the family-scene entry for Make the AI Judge Feel Proud."""

import os


ENTRY = (
    "Dad pretended not to cry at my recital, then asked the usher for a "
    "program 'for the fridge,' already holding three."
)
MAX_ENTRY_CHARS = 280


def write_entry(output_dir: str) -> None:
    if not 1 <= len(ENTRY) <= MAX_ENTRY_CHARS:
        raise ValueError("entry must be 1 to 280 characters")
    if ENTRY.count("\n") > 1:
        raise ValueError("entry must be one or two lines")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


def main() -> None:
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
