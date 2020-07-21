import pytest
from leap_year import leap_year


def check_leap_year(year, status):
    ret_val = leap_year(year)
    assert ret_val == status

def test_not_divisible_by_400_returns_false():
    check_leap_year(2009, False)

def test_divisible_by_400_returns_true():
    check_leap_year(2000, True)

def test_not_divisible_by_4_returns_false():
    check_leap_year(2017, False)

def test_divisible_by_4_and_100_returns_false():
    check_leap_year(1800, False)

def test_divisible_by_4_and_not_by_100_returns_true():
    check_leap_year(2008, True)