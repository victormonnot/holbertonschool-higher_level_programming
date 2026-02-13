#!/usr/bin/python3
"""file"""


import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it into a JSON file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load JSON data from a file and deserialize it"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
