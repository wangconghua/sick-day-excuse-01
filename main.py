"""Entry for make.fun's "The Funniest Sick-Day Excuse" bounty.

Writes one line, under 200 characters, to /output/entry.txt (or next to
this file when /output does not exist, e.g. a local run).
"""

import os

ENTRY = ("I threw my back out carrying every grocery bag in one trip "
         "because I refuse to make two, and now I can't stand up "
         "straight. Pride: 1, spine: 0.")


def check_is_string(text):
    """The entry must be a string, not bytes or another type."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    return True


def check_non_empty(text):
    """The entry must contain at least one non-white-space character."""
    if not text:
        raise ValueError("entry must not be empty")
    if text.strip() == "":
        raise ValueError("entry must not be only white space")
    return True


def check_single_line(text):
    """The entry must be one line: no newline or carriage return."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def check_length(text, limit=200):
    """The entry must fit the competition's character limit."""
    if len(text) > limit:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), limit))
    return True


def check_encodable(text):
    """The entry must be valid UTF-8 text."""
    text.encode("utf-8")  # raises UnicodeEncodeError on bad characters
    return True


def validate(text):
    """Check the entry against the competition gate. Raises ValueError."""
    check_is_string(text)
    check_non_empty(text)
    check_single_line(text)
    check_length(text)
    check_encodable(text)
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
