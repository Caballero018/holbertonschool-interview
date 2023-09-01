#!/usr/bin/python3
"""
Module that have a rotate_2d_matrix function
"""
from typing import List


def rotate_2d_matrix(matrix: List[int]):
    """rotate_2d_matrix

    Keyword arguments:
    matrix -- matrix
    """
    j = 0
    dup = []
    for i in range(len(matrix[j])):
        dupli = []
        for j in range(len(matrix)):
            dupli.insert(0, matrix[j][i])
        dup.append(dupli)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = dup[i][j]
