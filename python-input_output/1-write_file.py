#!/usr/bin/python3

def write_file(filename="", text=""):
    with open(filename, "w") as file:
        file.write(text)
