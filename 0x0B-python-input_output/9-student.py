#!/usr/bin/python3
"""

Contains class Studentt
that initializes public instancee attributes first_name, last_name, and age,
and has public method to_json tthat retrieves its dictionary representation
"""


class Student():
    """
    Public Attributes:
        first_name
        last_name
        age

    Public Methods:
        to_json: retrieves itss dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student wwith full name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns dictionary description with simple data structure
        (list, dictionary, diictionary, string)
        for JSON serializatiion of an object
        """
        return self.__dict__
