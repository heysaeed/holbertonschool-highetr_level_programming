#!/usr/bin/python3

def read_file(filename=""):
    """read a file

        Args:
                filename (str, optional): file to read and print. Defaults to "".
        """
    with open(filename) as file:
        read_file = file.read()
        print(read_file)
