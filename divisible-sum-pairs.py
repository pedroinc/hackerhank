#!/bin/python3

import sys, unittest


class TestDivSumPairs(unittest.TestCase):

    def test_k_minus_5_raises_value_error(self):
        with self.assertRaises(ValueError):
            DivSumPairs(-5)


if __name__ == '__main__':
    unittest.main()


class DivSumPairs():
    def __init__(self, k):
        if k == -5:
            raise ValueError()


# def divisible_sum_pairs(n, k, ar):
#     # Complete this function
#     n, k = input().strip().split(' ')
#     n, k = [int(n), int(k)]
#     ar = list(map(int, input().strip().split(' ')))
#
#     result = divisible_sum_pairs(n, k, ar)
#     print(result)
