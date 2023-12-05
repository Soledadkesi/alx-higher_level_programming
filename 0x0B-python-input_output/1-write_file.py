#!/usr/bin/python3
"""

writes to text file and returns num chars written
"""


def write_file(filename="", text=""):
    """writes to text file and returns num chars written"""
    with open(filename, mode="w", encoding="utf-8") as g:
        return (g.write(text))
