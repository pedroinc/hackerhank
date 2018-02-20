#!/bin/python3

import sys

def breakingRecords(score):

    break_highest_counter = 0
    break_lowest_counter = 0
    highest_value = None
    lowest_value = None
    # i = 0

    for x in score:

        if lowest_value is not None and x < lowest_value:
            break_lowest_counter += 1
            lowest_value = x

        if highest_value is not None and x > highest_value:
            break_highest_counter += 1
            highest_value = x

        if highest_value is None:
            highest_value = x

        if lowest_value is None:
            lowest_value = x

    return break_highest_counter, break_lowest_counter


if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print(" ".join(map(str, result)))
