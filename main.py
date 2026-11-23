"""warmemoji — one emoji, one smile.

The entry is a single 🌞 (U+1F31E SUN WITH FACE): a smiling sun. Its warm
face lands at first glance, sunshine reads as friendly in every culture,
and a sun with a face is unmistakably a deliberate pick rather than the
default smiley — cheerful to a stranger, with no intimacy and no sarcasm.
"""

import os

ENTRY = "🌞"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
