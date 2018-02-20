#!/bin/python3

import sys

def simpleArraySum(n, ar):
    sum = 0
    for x in range(0, n):
        sum = sum + ar[x]
    return sum

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))

result = simpleArraySum(n, ar)
print(result)