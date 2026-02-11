#!/usr/bin/python3
"""file"""


def class_to_json(obj):
    '''Return the dictionnary description of an object'''
    return obj.__dict__
