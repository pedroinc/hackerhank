#!/bin/python3
import unittest

class TestFizzBuzz(unittest.TestCase):

    # def setUp(self):
    #     pass

    # def tearDown(self):
    #     pass

    def test_0_raises_value_error(self):
        with self.assertRaises(ValueError):
            FizzBuzz(0)

    def test_1_does_not_raise_value_error(self):
        assert FizzBuzz(1).get_value() == 1

    def test_3_print_Fizz(self):
        assert FizzBuzz(3).get_value() == 'Fizz'

    def test_5_print_Buzz(self):
        assert FizzBuzz(5).get_value() == 'Buzz'

    def test_9_print_Fizz(self):
        assert FizzBuzz(9).get_value() == 'Fizz'

    def test_10_print_Buzz(self):
        assert FizzBuzz(10).get_value() == 'Buzz'

    def test_15_print_FizzBuzz(self):
        assert FizzBuzz(15).get_value() == 'FizzBuzz'

    def test_30_print_FizzBuzz(self):
        assert FizzBuzz(30).get_value() == 'FizzBuzz'

    def test_minus_1_raises_value_error(self):
        with self.assertRaises(ValueError):
            FizzBuzz(-1)


if __name__ == '__main__':
    unittest.main()

class FizzBuzz(object):
    def __init__(self, number):
        if number <= 0:
            raise ValueError()
        self.number = number

    def get_value(self):
        if self.is_divisible_by(3) and self.is_divisible_by(5):
            return 'FizzBuzz'
        elif self.is_divisible_by(3):
            return 'Fizz'
        elif self.is_divisible_by(5):
            return 'Buzz'
        return self.number


    def is_divisible_by(self, divisor):
        return self.number % divisor == 0
