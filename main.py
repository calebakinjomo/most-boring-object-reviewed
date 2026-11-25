"""Most Boring Object, Reviewed in One Line — make.fun entry.

Writes a single-line review (<= 200 characters) of the most boring
everyday object to /output/entry.txt.

The object: a dustpan. Its one job is to collect dust, yet every sweep
ends the same way — a thin last line of dust escapes back onto the
floor. The joke is the object's own dull failure, told straight.
"""

import os
import sys

# The entry: one line, at most 200 characters, nothing else.
ENTRY = (
    "The dustpan: sweeps up everything except the last line of dust, "
    "which it escorts back onto the floor like a bouncer."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    """Validate the entry and write it to /output/entry.txt."""
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        print(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
