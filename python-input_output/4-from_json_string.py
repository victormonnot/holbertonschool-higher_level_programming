#!/usr/bin/python3
"""file"""


import json


def from_json_string(my_str):
    '''JSON string to Python object'''
    return json.loads(my_str)
