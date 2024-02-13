#!/usr/bin/python3

def read_file(filename=""):
    """read a file and print its content

    Args:
            filename (str, optional): file to read and print.
            Defaults to "".
    """
    with open(filename, 'r', encoding='utf-8') as file:
        read_file = file.read()
        print(read_file, end='')
