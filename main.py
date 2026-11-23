#!/usr/bin/env python3
"""One Word, First Thought - make.fun entry (variant C).

The task: send exactly one word, the first word that comes to mind.
The judge compares words two at a time on which is more interesting,
weighing, in order: surprise, vividness, then a spark of wit, sound,
or double meaning. Length for its own sake does not count.

The word: snollygoster - a shrewd, unprincipled person, especially a
politician who does anything to stay in office.
It scores on surprise and wit at once:

* Surprising - an absurd, old American word almost nobody has met, so
  no reader guesses it; it is not a safe list-word.
* Vivid and specific - it names a whole character in one gulp: the
  scheming operator, grinning, always landing on his feet.
* Sound and wit - the word itself is the joke: "snolly-goster" trips
  off the tongue like a playground insult, and its meaning lands a
  second punch on a second look.

The program writes exactly that one word, nothing else, to
/output/entry.txt - 12 characters, well inside the gate's 1-24.
"""

import os

WORD = "snollygoster"


def main() -> None:
    # Self-check against the sealed gate: exactly one word, 1-24 chars.
    assert WORD.isalpha() and 1 <= len(WORD) <= 24, "word fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
