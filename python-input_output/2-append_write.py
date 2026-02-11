#!/usr/bin/python3
"""file"""


def append_write(filename="", text=""):
    '''append a string in the file and retrun the numbers of characters appended'''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
