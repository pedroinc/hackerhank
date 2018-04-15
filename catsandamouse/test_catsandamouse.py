#!/bin/python3
import unittest
from catsandamouse import CatsAndMouse

class TestCatsAndMouse(unittest.TestCase):

    def test_cat_a_and_cat_b_from_position_1_mouse_escapes(self):
        cats_and_mouse = CatsAndMouse(cat_a=1, cat_b=1, mouse_c=4)
        self.assertEqual(cats_and_mouse.get_answer(), 'Mouse C')

    def test_cat_a_from_position_1_cat_b_from_2_mouse_c_from_3_cat_b_wins(self):
        cats_and_mouse = CatsAndMouse(cat_a=1, cat_b=2, mouse_c=3)
        self.assertEqual(cats_and_mouse.get_answer(), 'Cat B')

    def test_cat_a_from_position_1_cat_b_from_2_mouse_c_from_4_cat_b_wins(self):
        cats_and_mouse = CatsAndMouse(cat_a=1, cat_b=2, mouse_c=4)
        self.assertEqual(cats_and_mouse.get_answer(), 'Cat B')

    def test_cat_a_position_0_raises_value_error(self):
        with self.assertRaises(ValueError):
            cats_and_mouse = CatsAndMouse(cat_a=0, cat_b=1, mouse_c=4)

    def test_cat_a_position_minus_1_raises_value_error(self):
        with self.assertRaises(ValueError):
            cats_and_mouse = CatsAndMouse(cat_a=-1, cat_b=1, mouse_c=4)

    def test_cat_b_position_minus_1_raises_value_error(self):
        with self.assertRaises(ValueError):
            cats_and_mouse = CatsAndMouse(cat_a=2, cat_b=-1, mouse_c=4)

    def test_cat_c_position_minus_1_raises_value_error(self):
        with self.assertRaises(ValueError):
            cats_and_mouse = CatsAndMouse(cat_a=2, cat_b=1, mouse_c=-1)

if __name__ == '__main__':
    unittest.main()
