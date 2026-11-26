"""Rename the Planet — make.fun entry.

Prints one line giving a planet a funny new name, with the why, and
writes the identical line to /output/entry.txt (the program/v1 harness
scores the file; print-only scores Valid=0).
"""

import os

LINE = "Rename Mars 'The Suburb': red, dusty, overpriced, and everyone keeps saying they'll move there someday but never does."

MAX_CHARS = 200

# The gate requires 1 to 200 characters; fail loudly instead of
# submitting an entry the scorer would mark invalid.
assert 1 <= len(LINE) <= MAX_CHARS, f"LINE is {len(LINE)} chars, must be 1-{MAX_CHARS}"


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
