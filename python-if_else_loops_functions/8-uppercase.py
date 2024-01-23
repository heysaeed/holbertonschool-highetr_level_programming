#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if (ord(letter) <= ord('z') and ord(letter) >= ord('a')):
            upper_char = chr(ord(letter) - 32)
        else:
            upper_char = letter
        print("{}".format(upper_char), end='')
    print()
