#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
if __name__ == "__main__":
    resultAdd = add(a, b)
    resultSub = sub(a, b)
    resultMul = mul(a, b)
    resultDiv = div(a, b)
    print("{} + {} = {}".format(a, b, resultAdd))
    print("{} - {} = {}".format(a, b, resultSub))
    print("{} * {} = {}".format(a, b, resultMul))
    print("{} / {} = {}".format(a, b, resultDiv))
