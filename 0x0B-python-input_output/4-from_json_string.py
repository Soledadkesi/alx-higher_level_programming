#!/usr/bin/python3
"""

returns python data structure frrom JSON string
"""


def from_json_string(my_str):
    """Returns python data struucture from JSON string
    Args:
        my_str: json string reepresentation
    Return:
        python object
    """
    import json

    return json.loads(my_str)
