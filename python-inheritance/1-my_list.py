#!/usr/bin/python3
"""
This module defines the MyList class
"""


class MyList(list):
    """
    MyList adds the ability to print the list elements
    in sorted order without modifying the original list.
    """

    def print_sorted(self):
        """
        Prints list elements in ascending order without altering the original
        list. Utilizes the built-in sorted() function for ordering elements.
        """
        sorted_list = sorted(self)
        print(sorted_list)
