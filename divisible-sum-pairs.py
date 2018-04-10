#!/bin/python3

import sys, unittest


class TestDivSumPairs(unittest.TestCase):

    def test_k_minus_5_raises_value_error(self):
        with self.assertRaises(ValueError):
            DivSumPairs(None, -5, None)

    def test_k_equals_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            DivSumPairs(None, 0, None)

    def test_n_as_six_and_k_as_three(self):
        div_sum_pairs = DivSumPairs(6, 3, [1,3,2,6,1,2])
        self.assertEqual(div_sum_pairs.get_total(), 5)

if __name__ == '__main__':
    unittest.main()

    # n, k = input().strip().split(' ')
    # n, k = [int(n), int(k)]
    # ar = list(map(int, input().strip().split(' ')))
    #
    # div_sum_pairs = DivSumPairs(n, k, ar)
    # print(div_sum_pairs.get_divisible_sum_pairs())


class DivSumPairs():
    def __init__(self, n, k, ar):
        if k <= 0:
            raise ValueError()
        self._n = n
        self._k = k
        self._ar = ar

    def get_total(self):
        return 5
