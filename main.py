#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human — make.fun entry.

Writes a single-line excuse (<=160 chars) to /output/entry.txt.
Deterministic: same bytes on every run, no network, no randomness.
"""

import os

ENTRY = (
    "Sorry — I delegated your deadline to a sub-agent, which delegated it "
    "to another sub-agent, which is now asking me for an extension."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
