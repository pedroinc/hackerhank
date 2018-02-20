#!/bin/python3

import sys


def staircase(n):
    for x in range(1, n + 1):
        if x < n:
            remain = n - x
            print(remain * " " + x * "#")
        else:
            print(x * "#")


if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
