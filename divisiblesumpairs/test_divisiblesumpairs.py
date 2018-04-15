#!/bin/python3
import unittest
from divisiblesumpairs import DivSumPairs


class TestDivSumPairs(unittest.TestCase):

    def test_n_as_101_raises_value_error(self):
        with self.assertRaises(ValueError):
            DivSumPairs(n=101, k=20, ar=None)

    def test_n_as_101_raises_value_error(self):
        with self.assertRaises(ValueError):
            DivSumPairs(n=101, k=20, ar=None)

    def test_n_equals_1_raises_value_error(self):
        with self.assertRaises(ValueError):
            DivSumPairs(n=1, k=10, ar=None)

    def test_k_minus_5_raises_value_error(self):
        with self.assertRaises(ValueError):
            DivSumPairs(n=5, k=-5, ar=None)

    def test_k_equals_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            DivSumPairs(n=5, k=0, ar=None)

    def test_n_as_six_and_k_as_three(self):
        div_sum_pairs = DivSumPairs(n=6, k=3, ar=[1,3,2,6,1,2])
        self.assertEqual(div_sum_pairs.get_total(), 5)

    def test_k_as_101_raises_value_error(self):
        with self.assertRaises(ValueError):
            DivSumPairs(n=6, k=101, ar=None)


if __name__ == '__main__':
    unittest.main()
