#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers -- make.fun entry.

Writes one original fortune-cookie line for a software developer,
at most 120 characters, to /output/entry.txt.

Deterministic, offline, standard library only: the same line on
every run, with no randomness, no network and no clock involved.
"""

import os
import sys

ENTRY = "The code you delete today is the only code that will never wake you at 3 a.m."

DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def main(argv):
    """Write ENTRY to the output path and report its length."""
    output_path = argv[0] if argv else os.environ.get(
        "ENTRY_OUTPUT", DEFAULT_OUTPUT_PATH
    )
    if len(ENTRY) > 120:
        raise SystemExit("entry exceeds 120 characters")
    if not ENTRY.strip():
        raise SystemExit("entry is empty")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    print("wrote {} characters to {}".format(len(ENTRY), output_path))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
