#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    test = 0

    for i in range(1, argc + 1):
        test += int(sys.argv[i])
    print(test)
