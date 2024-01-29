#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        firstChar = None
    else:
        firstChar = sentence[0]
    return (len(sentence), firstChar)
