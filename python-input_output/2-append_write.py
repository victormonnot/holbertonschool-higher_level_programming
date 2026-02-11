#!/usr/bin/python3
"""file"""


def write_file(filename="", text=""):
    '''Write a string in a txt file and return the numbers of characters written'''
    with open(filename, "w", encoding="utf-8") as jsp:
        return jsp.write(text)
