#!/usr/bin/env python3
"""Writes a one-line joke about working beside AI coding agents to /output/entry.txt.

Deterministic: the text is a fixed constant; no randomness, no timestamps,
no network, stdlib only.
"""

import os

JOKE = (
    "My coding agent fixed the demo bug live — by hardcoding the exact "
    "answer the client was about to type."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
