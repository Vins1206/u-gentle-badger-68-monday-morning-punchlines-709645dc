"""Monday Morning Punchlines — writes a single joke to /output/entry.txt.

Stdlib only. The output is exactly one line of plain text, no trailing
newline, so the gate counts exactly the joke itself (117 characters).
"""

from pathlib import Path

JOKE = (
    "My bed filed for custody of me on Monday mornings. "
    "The judge ruled for the bed, but work still got visitation rights."
)


def main() -> None:
    # Enforce the competition gate locally before writing anything:
    # 1-200 characters, a single line, and not only whitespace.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be one non-blank line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
