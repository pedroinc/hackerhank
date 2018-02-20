#!/bin/python3

import sys
from decimal import *


def plus_minus(arr):

    positive = 0
    negative = 0
    zeroes = 0

    for item in arr:
        if item > 0:
            positive = positive + 1
        elif item < 0:
            negative = negative + 1
        else:
            zeroes = zeroes + 1

    return positive, negative, zeroes


def convert_to_decimal(value):
    return round(Decimal(value), 6)


if __name__ == "__main__":

    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    res = plus_minus(arr)
    print(convert_to_decimal(res[0] / n))
    print(convert_to_decimal(res[1] / n))
    print(convert_to_decimal(res[2] / n))
