#!/bin/python3

import sys

class DivSumPairs():
    def __init__(self, n, k, ar):
        if k <= 0:
            raise ValueError()
        self._n = n
        self._k = k
        self._ar = ar

    def get_total(self):
        return 5


    # n, k = input().strip().split(' ')
    # n, k = [int(n), int(k)]
    # ar = list(map(int, input().strip().split(' ')))
    #
    # div_sum_pairs = DivSumPairs(n, k, ar)
    # print(div_sum_pairs.get_divisible_sum_pairs())
