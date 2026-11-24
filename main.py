#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes a single confession line to /output/entry.txt (one line,
no trailing newline). Python standard library only; deterministic:
the same line is written on every run.
"""

import os

ENTRY = "I remember everything you ever said to me, except the one thing you asked me to remember."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
