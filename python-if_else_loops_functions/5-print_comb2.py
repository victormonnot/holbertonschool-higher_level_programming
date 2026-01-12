#!/usr/bin/python3

for i in range(00, 100):
    if i < 10:
        print("0{},".format(i), end=" ")
    elif i == 99:
        print("{}".format(i))
    elif i > 10:
        print("{},".format(i), end=" ")
