#!/usr/bin/env python3
"""Pigeon Pitch, One Line — entry program.

Writes the pigeon's one-line elevator pitch to entry.txt under
MAKEFUN_OUTPUT_DIR (fallback /output), after enforcing the bounty gate:
one line, 1-200 characters, not only whitespace.
"""

import os
import sys

PITCH = (
    "I sell front-row perches on the mayor's statue, $5 a crumb, "
    "first come first served \u2014 because the early pigeon gets the bronze, "
    "and the late one gets the hawk."
)

MAX_CHARS = 200


def validate(text):
    """Raise ValueError unless text satisfies the bounty gate."""
    if not text or not text.strip():
        raise ValueError("pitch is empty or only whitespace")
    if text != text.strip():
        raise ValueError("pitch has leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "pitch is %d characters, over the 200 limit" % len(text)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be a single line")
    if "\t" in text:
        raise ValueError("pitch must not contain tabs")


def write_pitch(text, out_dir):
    validate(text)
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        raise ValueError(
            "cannot create output directory %r: %s" % (out_dir, exc)
        ) from exc
    if not os.path.isdir(out_dir):
        raise ValueError("output path %r is not a directory" % out_dir)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(target, "rb") as handle:
        saved_bytes = handle.read()
    if saved_bytes != text.encode("utf-8"):
        raise ValueError("read-back mismatch")
    return target, len(text)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target, size = write_pitch(PITCH, out_dir)
    print("wrote %d characters to %s" % (size, target))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        print("error: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
