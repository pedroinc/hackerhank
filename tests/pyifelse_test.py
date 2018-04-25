import unittest

from pyifelse import PyIfElse

class TestIfElse(unittest.TestCase):

    def test_if_odd_print_weird(self):
        self.assertEqual("Weird", PyIfElse(5))
