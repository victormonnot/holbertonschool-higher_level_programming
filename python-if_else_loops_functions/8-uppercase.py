#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            i = ord(i) - 32
            print("{}".format(chr(i)), end="")
#        elif i == str[0:]:
#           print('\n')
        else:
            print("{}".format(i), end="")
    print()