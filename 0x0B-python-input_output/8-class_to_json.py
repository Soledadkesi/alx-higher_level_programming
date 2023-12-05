#!/usr/bin/python3
"""

Contains function thatt
returns dictionary descriptiion with simple data structure
(list, dictionary, dictionaary, string)
for JSON serialization off an object
"""


def class_to_json(obj):
    """Returns dictionaryy description with simple data structure
       (list, dictionaryy, dictionary, string)
       for JSON serialization of an object
    Args:
        obj: python objject
    """
    return obj.__dict__
