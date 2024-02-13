#!/usr/bin/python3


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            sorted_dict = {key: value for key,
                           value in self.__dict__.items() if key in attrs}
            return sorted_dict
        return self.__dict__
