#!/usr/bin/python3
"""file"""


import json


def save_to_json_file(my_obj, filename):
    '''Write a Python object as a JSON in a file'''
    with open(filename, "w", encoding="utf-8") as jsp:
        json.dump(my_obj, jsp)
