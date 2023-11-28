#!/usr/bin/python3
"""
Locked classs
"""


class LockedClass:
    """
    Prevent user from creatiiing a new instace
    dynamically
    """

    __slots__ = "first_name"
