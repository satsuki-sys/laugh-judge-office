#!/usr/bin/env python3
"""Make the AI Judge Laugh — one line about office life.

Writes a single office-life joke to /output/entry.txt.
The gate requires UTF-8 text of 1 to 200 characters, one line.
"""

import os

ENTRY = "The office printer only jams on urgent documents, which is how I know it reads the subject line."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
