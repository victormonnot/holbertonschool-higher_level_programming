#!/usr/bin/python3
"""
2-matrix_divided
Defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): matrix of integers/floats
        div (int or float): divisor

    Raises:
        TypeError: if matrix is not a list of lists of int/float
        TypeError: if rows are not the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0

    Returns:
        New matrix with divided values rounded to 2 decimals
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(n, (int, float)) for row in matrix for n in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [
        [round(n / div, 2) for n in row]
        for row in matrix
    ]

    return new_matrix
