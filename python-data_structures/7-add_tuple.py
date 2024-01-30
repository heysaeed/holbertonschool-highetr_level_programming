#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    length = len(tuple_a)
    if length < 2:
        tuple_a += (0, 0)
    length = len(tuple_b)
    if length < 2:
        tuple_b += (0, 0)

    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    new_tuple = (a, b)
    return new_tuple
