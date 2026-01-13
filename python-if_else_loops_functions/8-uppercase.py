#!/usr/bin/python3

def uppercase(str):
    str = str + '\n'
    for i in str:
        if 97 <= ord(i) <= 122:
            i = ord(i) - 32
            print("{}".format(chr(i)), end="")
        else:
            print("{}".format(i), end="")
