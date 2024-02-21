#!/usr/bin/python3
"""Module for the base class"""
import json
import os


class Base:
    """A base class for managing id attribute in all your future classes and
    to avoid duplicating the same code (by extension, same bugs)"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts list of dictionaries to JSON string."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        list_dicts = []
        filename = "{}.json".format(cls.__name__)

        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
        with open(filename, "w") as newfile:
            newfile.write(cls.to_json_string(list_dicts))

    def from_json_string(json_string):
        """Converts a JSON string to a list of dictionaries."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with attributes set according to dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise Exception("Wrong class")
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of class instances from a file of JSON strings."""
        filename = "{}.json".format(cls.__name__)
        if not os.path.isfile(filename):
            return []

        with open(filename, "r") as file:
            file_read = file.read()
            list_dicts = cls.from_json_string(file_read)

        instances = []
        for d in list_dicts:
            instance = cls.create(**d)
            instances.append(instance)

        return instances
