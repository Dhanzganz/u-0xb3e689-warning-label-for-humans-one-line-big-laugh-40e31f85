"""Warning Label for Humans: One Line, Big Laugh.

Writes the entry — a single-line safety warning label for humans,
at most 160 characters — to /output/entry.txt.
"""

import os

# The joke: a product-style safety label for a human whose safe operating
# hours are bounded by caffeine intake and poor late-night judgment.
ENTRY = (
    "WARNING: This human runs on caffeine and questionable decisions. "
    "Do not operate before 9 a.m. or after midnight."
)

MAX_CHARS = 160

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Fail loudly instead of shipping a label that breaks the spec:
    # the entry must be exactly one line and at most 160 characters.
    if "\n" in ENTRY or len(ENTRY) > MAX_CHARS:
        raise ValueError(
            f"entry must be one line of at most {MAX_CHARS} characters "
            f"(got {len(ENTRY)} characters, {ENTRY.count(chr(10)) + 1} lines)"
        )
    # No padding: a stray leading/trailing space would change the entry.
    if not ENTRY or ENTRY != ENTRY.strip():
        raise ValueError("entry must be non-empty with no leading/trailing whitespace")
    # The grader mounts /output as a volume: only create it, never delete it.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back what was written: the file must match the entry exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("written entry does not match ENTRY")
    print(f"wrote {len(ENTRY)}-character entry to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
