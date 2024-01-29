#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    newlist = []
    for i in my_list:
        if i % 2 == 0:
            newlist.append(True)
        else:
            newlist.append(False)
    return newlist
