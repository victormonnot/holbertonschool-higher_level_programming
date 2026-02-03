#!/usr/bin/python3
'''file'''


def is_same_class(obj, a_class):
    """Returns True or False"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    if type(obj) is not a_class:
        return False
