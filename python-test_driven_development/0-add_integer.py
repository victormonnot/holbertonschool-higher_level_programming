#!/usr/bin/python3
"""
Module that defines add_integer function
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    try:
        return int(a) + int(b)
    except OverflowError:
        raise OverflowError
