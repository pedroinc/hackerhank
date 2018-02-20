#!/bin/python3

import sys


def sum_list(m_list):
    m_sum = 0
    for item in m_list:
        m_sum = m_sum + item
    return m_sum


def diagonal_difference(matrix):

    diagonal_a = []
    diagonal_b = []
    interval = len(matrix) - 1
    counter = 0

    for row in matrix:
        diagonal_a.append(row[counter])
        diagonal_b.append(row[interval])

        counter = counter + 1
        interval = interval - 1

    soma_a = sum_list(diagonal_a)
    soma_b = sum_list(diagonal_b)

    return abs(soma_a - soma_b)


if __name__ == "__main__":

    n = int(input().strip())
    a = []
    for a_i in range(n):
        a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
        a.append(a_t)

    result = diagonal_difference(a)
    print(result)