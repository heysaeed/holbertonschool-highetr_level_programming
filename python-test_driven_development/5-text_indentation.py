#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = [".", ":", "?"]
    i = 0
    while i < len(text):
        if text[i] in characters:
            print(text[i], end="")
            print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        print(text[i], end="")
        i += 1
