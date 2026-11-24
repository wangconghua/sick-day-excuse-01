"""Entry for make.fun's "The Funniest Sick-Day Excuse" bounty.

Writes one line, under 200 characters, to /output/entry.txt (or next to
this file when /output does not exist, e.g. a local run).
"""

import os

ENTRY = ("I threw my back out carrying every grocery bag in one trip "
         "because I refuse to make two, and now I can't stand up "
         "straight. Pride: 1, spine: 0.")


def validate(text):
    """Check the entry against the competition gate. Raises ValueError."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text:
        raise ValueError("entry must not be empty")
    if text.strip() == "":
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError(
            "entry is %d characters, over the 200 limit" % len(text))
    text.encode("utf-8")  # raises UnicodeEncodeError on bad characters
    return True


def main():
    validate(ENTRY)
    if os.path.isdir("/output"):
        out = "/output/entry.txt"
    else:
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "entry.txt")
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote %s (%d characters)" % (out, len(ENTRY)))


if __name__ == "__main__":
    main()
