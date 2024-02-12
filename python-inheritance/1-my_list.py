#!/bin/usr/python3
"""Define MyList inheriting frum list
"""


class MyList(list):
    """define attribute of Mylist
    Args:
    list (int)
    """
    list = []

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
