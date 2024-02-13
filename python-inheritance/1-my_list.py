#!/bin/usr/python3
"""
Define MyList inheriting frum list
"""


class MyList(list):
    """
    define attribute of Mylist
    Args:
    inherited class list
    """

    def print_sorted(self):
        """
        sort and print
        """
        sorted_list = sorted(self)
        print(sorted_list)
