#!/usr/bin/python3
def islower(c):
    ascii_char = ord(c)
    if (ascii_char <= ord('z') and ascii_char >= ord('a')):
        return True
    else:
        return False
