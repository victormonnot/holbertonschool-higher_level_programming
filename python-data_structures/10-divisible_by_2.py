#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_result = []
    for test in my_list:
        if test % 2:
            list_result.append(False)
        else:
            list_result.append(True)

    return list_result
