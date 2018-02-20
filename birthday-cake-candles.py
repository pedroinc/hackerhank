#!/bin/python3

import sys


def birthday_cake_candles(n, items):

    greater_value = 0

    for x in items:
        if x > greater_value:
            greater_value = x

    return items.count(greater_value)


n = int(input().strip())

if n < 1:
    raise ValueError('colleen birthday should be greater than zero')

if n > 10 ** 5:
    raise ValueError('colleen birthday should be smaller than {0}'.format(10 ** 5))

ar = list(map(int, input().strip().split(' ')))
result = birthday_cake_candles(n, ar)
print(result)
