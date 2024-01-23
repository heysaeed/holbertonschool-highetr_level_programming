#!/usr/bin/python3
for firstDigit in range(0, 9):
    for secondDigit in range(firstDigit + 1, 10):
        if (firstDigit != 8 or secondDigit != 9):
            print("{}{}".format(firstDigit, secondDigit), end=", ")
        else:
            print("{}{}".format(firstDigit, secondDigit))
