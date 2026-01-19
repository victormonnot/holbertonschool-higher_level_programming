#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first_character = sentence[0]
    if sentence == "":
        return (0, None)
    return (length, first_character)
