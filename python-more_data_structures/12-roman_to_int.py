#!/usr/bin/python3

def roman_to_int(roman_string):
    number = 0
    roman_dict = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
    if type(roman_string) is not str or roman_string is None:
        return 0
    for i in range(1, len(roman_string)):
        if roman_dict[roman_string[i]] <= roman_dict[roman_string[i-1]]:
            number += roman_dict[roman_string[i-1]]
        else:
            number -= roman_dict[roman_string[i-1]]
    number += roman_dict[roman_string[-1]]
    return number
