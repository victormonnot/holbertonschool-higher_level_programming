#!/usr/bin/python3
"""file"""


def read_file(filename=""):
    """Print what is in a file"""
    with open(filename, "r", encoding="utf-8") as jsp:
        print(jsp.read())
