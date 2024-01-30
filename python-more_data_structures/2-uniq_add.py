#!/usr/bin/python3

def uniq_add(my_list=[]):
    setlist = set(my_list)
    result = 0
    for int in setlist:
        result += int
    return result
