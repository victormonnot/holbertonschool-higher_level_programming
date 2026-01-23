#!/usr/bin/python3
"""
Module that defines add_integer function
"""


def add_integer(a, b=98):
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    try:
        a = int(a)
    except OverflowError:
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except OverflowError:
        raise TypeError("b must be an integer")

    return a + b

