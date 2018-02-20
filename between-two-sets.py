#!/bin/python3

import sys


def getTotalX(list_a, list_b):

    x_values = []
    compiled_list = list(set(list_a + list_b))
    compiled_list.sort()

    for x_candidate in range(1, max(compiled_list) + 1):
        dismissed = False

        for num in list_a:
            if x_candidate % num != 0:
                dismissed = True
                break

        if not dismissed:
            for num in list_b:
                if num % x_candidate != 0:
                    dismissed = True
                    break

        if not dismissed:
            x_values.append(x_candidate)

    return len(x_values)


if __name__ == "__main__":

    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)

    print(total)
