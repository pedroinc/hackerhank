import pytest

# Find the sum of all the multiples of 3 or 5 below x.

from problems.euler001 import sum_of_multiples

def test_sum_of_all_multiples_limiter_6_equal_to_8():
    assert sum_of_multiples(limiter=6) == 8

def test_limiter_equals_to_zero_raise_value_error():
    with pytest.raises(ValueError):
        sum_of_multiples(limiter=0)

def test_limiter_equals_to_minus_1_raise_value_error():
    with pytest.raises(ValueError):
        sum_of_multiples(limiter=-1)

def test_limiter_is_greater_than_1000000000_raise_value_error():
    with pytest.raises(ValueError):
        sum_of_multiples(limiter=10**9 + 1)
