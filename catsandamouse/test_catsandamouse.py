#!/bin/python3
import unittest
from catsandamouse import CatsAndMouse

class TestCatsAndMouse(unittest.TestCase):

    # def __init__(self):
    #     pass

    def test_cat_a_and_cat_b_from_position_1_mouse_escapes(self):
        cats_and_mouse = CatsAndMouse(cat_a=1, cat_b=1, mouse_c=4)
        self.assertEqual(cats_and_mouse.get_answer(), 'Mouse C')


# if __name__ == '__main__':
#     unittest.main()
