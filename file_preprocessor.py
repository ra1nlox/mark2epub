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


class FilePreprocessor:
    def __init__(self, path: str, style: HTagNLStyle = HTagNLStyle.AFTER):
        """
        Initiates the preprocessor using path to a file and new line style (enum)
        """
        self.md_file = open(path, "r", encoding="utf-8")
        self.lines = self.md_file.readlines()
        self.style = style

    def delete_tags(self):
        """
        Deletes obsidian style tags (check file docstring)
        """
        for line in self.lines:
            htag_match = re.fullmatch(r"^\#\S+\n$", line)
            if htag_match:
                try:
                    if self.style.value != 0:
                        if self.lines.index(line) != 0:
                            self.lines.pop(self.lines.index(line) + self.style.value)
                    self.lines.remove(line)
                except IndexError:
                    self.lines.remove(line)
        return self

    def close(self):
        """
        Closes the file connection
        """
        self.md_file.close()
        return self

    def get(self) -> str:
        """
        :return: Final processed string
        :rtype: str
        """
        self.close()
        return "".join(self.lines)


if __name__ == "__main__":
    print(FilePreprocessor(sys.argv[1], style=HTagNLStyle.ZERO).delete_tags().get())
