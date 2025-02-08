"""
Matrix Operations Module

This module provides functions for fundamental matrix operations:
    1. `transpose_matrix(matrix)`: Computes the transpose of a given matrix.
    2. `matrix_multiply(matrix_one, matrix_two)`: Multiplies two matrices.
"""

from typing import List


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Transposes the given matrix.

    :param matrix: A list of lists representing the matrix.
    :return: The transposed matrix.

    :raises ValueError: If the matrix rows have different lengths.

    >>> transpose_matrix([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]

    >>> transpose_matrix([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]

    >>> transpose_matrix([[7]])
    [[7]]

    >>> transpose_matrix([])
    []

    >>> transpose_matrix([[1, 2], [3]])
    Traceback (most recent call last):
    ...
    ValueError: Matrix rows should have the same length
    """

    if not matrix:
        return []

    first_row_len = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_len:
            raise ValueError('Matrix rows should have the same length')

    return list(map(list, zip(*matrix)))


def matrix_multiply(matrix_one: List[List[int]], matrix_two: List[List[int]]) -> List[List[int]]:
    """
    Multiplies two matrices.
    :param matrix_one: The first matrix (list of lists).
    :param matrix_two: The second matrix (list of lists).
    :return: The resulting matrix after multiplication.
    :raises ValueError: If matrices have incompatible dimensions.

    >>> matrix_multiply([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    [[58, 64], [139, 154]]

    >>> matrix_multiply([[2, 4], [3, 6]], [[1, 3], [2, 4]])
    [[10, 22], [15, 33]]

    >>> matrix_multiply([[1]], [[2]])
    [[2]]

    >>> matrix_multiply([[1, 2]], [[3, 4]])
    Traceback (most recent call last):
    ...
    ValueError: First matrix columns should have the same length as the number of rows of second matrix
    """
    first_matrix_rows_len = len(matrix_one)
    first_matrix_columns_len = len(matrix_one[0] if matrix_one else 0)
    second_matrix_rows_len = len(matrix_two)
    second_matrix_columns_len = len(matrix_two[0] if matrix_two else 0)

    if first_matrix_columns_len != second_matrix_rows_len:
        raise ValueError('First matrix columns should have the same length as the number of rows of second matrix')

    result = [[0] * second_matrix_columns_len for _ in range(first_matrix_rows_len)]

    for i in range(first_matrix_rows_len):
        for j in range(second_matrix_columns_len):
            for k in range(first_matrix_columns_len):
                result[i][j] += matrix_one[i][k] * matrix_two[k][j]

    return result
