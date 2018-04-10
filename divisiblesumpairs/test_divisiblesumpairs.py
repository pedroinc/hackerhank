#!/bin/python3
import unittest
from divisiblesumpairs import DivSumPairs

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
