#!/bin/python3

import sys


def mini_max_sum(arr):

    num_elements = len(arr)
    min_value = 999999999999999
    max_value = 0

    sum_max = 0
    sum_min = 0

    for item in arr:
        if item > max_value:
            max_value = item

        if item < min_value:
            min_value = item

    sum_min = sum_list(arr) - max_value
    sum_max = sum_list(arr) - min_value

    return sum_min, sum_max


def sum_list(m_list):
    m_sum = 0
    for item in m_list:
        m_sum = m_sum + item
    return m_sum


if __name__ == "__main__":

    arr = list(map(int, input().strip().split(' ')))
    result = mini_max_sum(arr)
    print(" ".join(map(str, result)))
