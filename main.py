#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes a single-line patch note announcing that human sleep is fixed
to /output/entry.txt, after checking it against the competition gate:
UTF-8 text, 1 to 160 characters, one line, not only whitespace.
"""

import os

PATCH_NOTE = (
    "Fixed: sleep now ships with an off switch; humans no longer wake "
    "at 3 a.m. to rehearse arguments they will never have."
)


def validate(line: str) -> str:
    """Check the patch note against the gate; raise if it fails."""
    line = line.strip()
    if not line:
        raise ValueError("patch note must not be empty or whitespace only")
    if "\n" in line or "\r" in line:
        raise ValueError("patch note must be a single line")
    if not 1 <= len(line) <= 160:
        raise ValueError(
            f"patch note must be 1-160 characters, got {len(line)}"
        )
    line.encode("utf-8")  # raises if not valid UTF-8 text
    return line


def main() -> None:
    note = validate(PATCH_NOTE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(note)
    print(f"Wrote {len(note)}-char patch note to /output/entry.txt")


if __name__ == "__main__":
    main()
