#!/usr/bin/python3
"""

Contains class Studentt
that initializes public instannce attributes first_name, last_name, and age,
and has public method to_jsonn that returns dictionary representation
of requested attributes or alll if none were requested
"""


class Student():
    """
    Public Attributes:
        first_name
        last_name
        age

    Public Methods:
        to_json: retrieves iits dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes studentt with full name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionaryy description with simple data structure
        (list, dictionaryy, dictionary, string)
        for JSON serialiization of an object

        Return:
            Only returnn dict of attrs given to us
            Return enttire dict if no attrs given
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic
