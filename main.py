"""Funniest Autocorrect Fail — one-line entry.

Writes a single-line autocorrect fail to /output/entry.txt. The line is a
work email to a boss where one word slipped: "earnings" became "erection".
It reads as a real slip, not a written joke — a normal quarterly-report
email, one wrong word, and suddenly the whole board meeting is awkward.
The twist lands on first read and needs no explanation.
"""

import os
import sys

# The entry: one line, well under the 200-character gate.
ENTRY = (
    "Hi Mr. Thompson, the quarterly erection report is attached for "
    "tomorrow's board meeting. Please review it before 9am, thanks!"
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read it back and enforce the gate ourselves before exiting.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            f"entry is {len(text)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if text.strip() == "" or "\n" in text or "\r" in text:
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    print(f"wrote {len(text)}-character entry to {OUTPUT_PATH}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
