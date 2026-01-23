#!/usr/bin/python3
"""
Docstring for 3-say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    Docstring for say_my_name
    :param first_name: The first Name
    :param last_name: The last Name
    """

    if not first_name:
        raise TypeError("first_name must be a string")
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
