#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    ta0 = tuple_a[0] if len(tuple_a) > 0 else 0
    ta1 = tuple_a[1] if len(tuple_a) > 1 else 0
    tb0 = tuple_b[0] if len(tuple_b) > 0 else 0
    tb1 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (ta0 + tb0, ta1 + tb1)
