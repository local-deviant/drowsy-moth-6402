#!/usr/bin/env python3
"""The 4AM Commit — write one commit message to the grader's output file.

The whole entry is a single fixed line: the note an AI agent leaves in the
log after a long night of fixing its own bugs. The line is fixed, not
generated, on purpose — the grader runs this program twice and the two runs
must agree byte for byte, so there is no randomness, no clock reading and
no network anywhere in here.
"""

import os

# The entry: one line, 107 characters. The joke is the loop of self-repair
# told as a shift report — attempt counter, the hours, and the punchline
# that by 4am the agent fixing the bug has become the bug. The number is
# deliberate: a machine counts its retries, and 47 says "all night" without
# saying it.
COMMIT_MESSAGE = (
    "fix: attempt 47: the bug I wrote at 2am is fixed by the fix I broke "
    "at 3am. At 4am I am the bug. Goodnight."
)


def output_path() -> str:
    """Where the grader reads the entry: $MAKEFUN_OUTPUT_DIR/entry.txt."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # No trailing newline: the file is the message, exactly as judged.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(COMMIT_MESSAGE)


if __name__ == "__main__":
    main()
