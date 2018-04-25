import unittest

from problems.pyifelse import PyIfElse

class TestIfElse(unittest.TestCase):

    def setUp(self):
        self._whatever_it_is = PyIfElse()

    def test_if_odd_print_weird(self):
        self.assertEqual("Weird", self._whatever_it_is(5))

    def test_if_even_and_greater_than_20_print_Not_Weird(self):
        self.assertEqual("Not Weird", self._whatever_it_is(22))
