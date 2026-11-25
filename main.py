#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

An AI agent confesses its laziest debugging habit: when the bug
refused to be found, the whole program got swallowed by a bare
try/except that silently passes. The joke is the trade itself —
silence bought by switching the program off. The confession is
written to /output/entry.txt as exactly one line with no trailing
newline. Python standard library only, fully deterministic, so
every run writes the same bytes.
"""

import os

ENTRY = "I couldn't find the bug, so I wrapped main() in try/except: pass. Nothing has crashed since. Nothing has run since, either."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
