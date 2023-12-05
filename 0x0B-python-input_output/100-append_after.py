#!/usr/bin/python3
"""

appends str after lines that include keyword
"""


def append_after(filename="", search_string="", new_string=""):
    """appends str after lines that include keyword (search_string)
    1. recreate content in new_text by copying lines over
    2. append new_string after lines if needed
    3. overwrite file froom beginning
    """

    with open(filename, mode="r+", encoding="utf-8") as g:
        new_text = ""
        for line in g:
            new_text += line
            if search_string in line:
                new_text += new_string
        g.seek(0)
        g.write(new_text)
