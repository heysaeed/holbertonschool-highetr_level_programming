#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = None
    score = -1
    for key, value in a_dictionary.items():
        if value > score:
            best = key
            score = value
    return best
