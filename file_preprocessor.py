"""
Docstring for file_preprocessor

Author: Artiom Guțan <gutsan.artiom@gmail.com>

This is a module to be used before parsing an md file, to eliminate any comments/hashtags (e.g. Obsidian).
A comment, in this sense, is any line that starts with a hashtag "#" and doesn't contain any whitespaces and ends with a new-line character sequence (\n).
While using this module it is recomended to specify what blank line must be deleted along with the hashtag line itself. For this purpose the enum HTagNLStyle exists.

HTagNLStyle.BEFORE will remove the line before the hashtag as follows:
# Example of a header
->
->#hashtag

Just a normal paragraph

---

HTagNLStyle.AFTER, which is the default one, will remove the line after the hashtag as follows:
# Example of a header

->#hashtag
->
Just a normal paragraph

---

HTagNLStyle.ZERO, will remove just the hashtag line:
# Example of a header

->#hashtag

Just a normal paragraph

---

I don't really know if it's useful or not, but I implemented it anyways.

"""

#

import sys
import re
from enum import Enum


class HTagNLStyle(Enum):
    BEFORE = -1
    ZERO = 0
    AFTER = 1


def delete_tags(path: str, style=HTagNLStyle.AFTER) -> str:
    md_file = open(path, "r", encoding="utf-8")
    lines = md_file.readlines()

    for line in lines:
        htag_match = re.fullmatch(r"^\#\S+\n$", line)
        if htag_match:
            try:
                if lines.index(line) != 0 and style.value != 0:
                    lines.pop(lines.index(line) + style.value)
                lines.remove(line)
            except IndexError:
                lines.remove(line)

    contents = "".join(lines)
    md_file.close()

    return contents


if __name__ == "__main__":
    print(delete_tags(sys.argv[1], style=HTagNLStyle.ZERO))
