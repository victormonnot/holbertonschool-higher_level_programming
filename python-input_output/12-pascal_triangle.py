#!/usr/bin/python3
"""file"""


def pascal_triangle(n):
    """Build a Pascal Triangle"""
    if n <= 0:
        return []

    triangle = [[1]]
    row = [1]

    for i in range(n - 1):
        new_row = [1]
        for j in range(i):
            new_row.append(row[j] + row[j + 1])
        new_row.append(1)
        triangle.append(new_row)
        row = new_row

    return triangle
