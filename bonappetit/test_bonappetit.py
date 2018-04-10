#!/bin/python3
import unittest
from bonappetit import BonAppetit


class TestBonAppetit(unittest.TestCase):

    def test_n_equals_3_and_k_as_3_raise_exception(self):
        with self.assertRaises(IndexError):
            BonAppetit(num_items=3, wont_eat=3, items=[2,4,6], charge_price=5)

    def test_valid_input_ex1(self):
        bonappetit = BonAppetit(num_items=4, wont_eat=1, items=[3,10,2,9], charge_price=7)
        self.assertEqual(bonappetit.get_answer(), 'Bon Appetit')

    def test_invalid_input_ex1(self):
        bonappetit = BonAppetit(num_items=4, wont_eat=1, items=[3,10,2,9], charge_price=12)
        self.assertEqual(bonappetit.get_answer(), 5)

if __name__ == '__main__':
    unittest.main()
