#!/usr/bin/python3
'''file'''


def inherits_from(obj, a_class):
    """Returns True or False"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
