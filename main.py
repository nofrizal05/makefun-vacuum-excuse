"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes one line of plain text to /output/entry.txt: the funniest excuse
a robot vacuum gives for missing a spot.
Python standard library only.
"""

import os

ENTRY = "I didn't skip that corner — my cliff sensor saw the rug fringe, panicked, and filed it as a staircase to nowhere."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
