#!/usr/bin/env python3
"""Writes one line about a small good thing that happened today at home."""

ENTRY = "My cough woke my daughter at 2 a.m.; she padded in barefoot, blanket dragging, rabbit under one arm, and whispered, \"You can have Mr. Hopps, Dad — he scares the coughs away.\" I slept like a baby."


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
