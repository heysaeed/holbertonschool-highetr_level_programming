#!/usr/bin/python3

def text_indentation(text):
    characters = [".", ":", "!"]
    new_string = ""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        new_string += char
        for x in characters:
            if x == char:
                new_string += "\n"
    return new_string
