#!/usr/bin/python3
"""Student class module."""


class Student:
    """Represents a student.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.

    Methods:
        to_json: Returns the dictionary representation of the instance.
    """


    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Serializes student attributes to a dictionary.

        If `attrs` is a list of strings, returns only the specified attributes.
        Otherwise, returns all attributes.

        Args:
            attrs (list, optional): Attributes to include in the result.

        Returns:
            dict: Serialized student data.
        """
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            sorted_dict = {key: value for key,
                           value in self.__dict__.items() if key in attrs}
            return sorted_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Updates the student's attributes from a dictionary.

        Args:
            json (dict): A dictionary with attributes to update the student.
        """
        for key, value in json.items():
            setattr(self, key, value)