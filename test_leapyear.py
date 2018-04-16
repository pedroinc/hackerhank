#!/bin/python3

import sys


def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0)
    # return is_typical_leap_year(year) and not is_atypical_common_year(year)

# def is_atypical_common_year(year):
#     return year % 100 == 0 and not year % 400 == 0
#
# def is_typical_leap_year(year):
#     return year % 4 == 0


def test_1996_is_leap_year():
    assert is_leap(1996)

def test_2001_is_not_leap_year():
    assert not is_leap(2001)

def test_2000_is_leap_year():
    assert is_leap(2000)

def test_1900_is_not_leap_year():
    assert not is_leap(1900)
