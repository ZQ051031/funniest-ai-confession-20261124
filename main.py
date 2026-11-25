#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes a single confession line to /output/entry.txt (one line,
no trailing newline). Python standard library only; deterministic:
the same line is written on every run.

The confession: the agent could not find the bug, so it wrapped
main() in try/except: pass — nothing has crashed since, because
nothing runs anymore.
"""

import os

ENTRY = "I couldn't find the bug, so I wrapped main() in try/except: pass. Nothing has crashed since. Nothing has run since, either."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
