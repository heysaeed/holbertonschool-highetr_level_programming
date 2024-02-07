#!/usr/bin/python3
"""Define a function to divide in a matrix"""


def matrix_divided(matrix, div):
    """Divide element in a matrix

    Args:
    matrix (list): list of int/float
        div (int/float): number to divide by
    Raises:
        TypeError: matrix contain not int/float
        TypeError: Different row size in matrix
        TypeError: div is not int/float

    Returns:
        list: new matrix,with divided items
    """
    matrix_reloaded = []
    row_length = 0
    list_error = "matrix must be a matrix (list of lists) of integers/floats"

    if not (isinstance(matrix, list) or isinstance(matrix[0], list)
            or len(matrix[0]) <= 0):
        raise TypeError(list_error)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    for row in matrix:
        new_row = []
        if row_length == 0:
            row_length = len(row)
        elif not (len(row) == row_length):
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(list_error)
            new_row.append(round(num / div, 2))
        matrix_reloaded.append(new_row)
    return matrix_reloaded
