#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    numerals = {'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_value = 0
    prev_value = 0
    for letter in reversed(roman_string):
        value = numerals[letter]
        if value < prev_value:
            int_value -= value
        else:
            int_value += value
        prev_value = value
    return int_value
