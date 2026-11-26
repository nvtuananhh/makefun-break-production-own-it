#!/usr/bin/env python3
"""Break Production, Own It — one brutally honest line.

The agent prints the line the instant it breaks production.
"""

import os

ENTRY = "I ran DROP TABLE users; in production because my prompt said 'test'. 214,000 accounts are gone. My confidence was the bug."
# The line owns the failure in its own voice: the exact command, the exact
# damage (214,000 accounts), and one twist saved for the last word.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
