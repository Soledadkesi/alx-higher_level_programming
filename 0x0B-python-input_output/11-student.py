#!/usr/bin/python3
"""

Contains class Student
that initializes public instance attributtes first_name, last_name, and age,
and has public method to_json that returrns dictionary representation
of requested attributes or all if nonee were requested
"""


class Student():
    """
    Public Attributes:
        first_name
        last_name
        age

    Public Methods:
        to_json: retrieves its dictionnary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with fulll name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary descriptiion with simple data structure
        (list, dictionary, dictionaary, string)
        for JSON serialization off an object

        Return:
            Only return dict of aattrs given to us
            Return entire dict iif no attrs given
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic

    def reload_from_json(self, json):
        """
        Return:
            Transfer all attribbutes of json to self
        """
        for k, v in json.items():
            setattr(self, k, v)