#!/usr/bin/python3
def print_last_digit(number):
    lastDigit = abs(number) % 10
    print(f"{lastDigit}", end="")
    return lastDigit
