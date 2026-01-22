#!/usr/bin/python3
"""Module qui contient la fonction square_matrix_simple"""


def square_matrix_simple(matrix=[]):
    """Retourne une nouvelle matrice avec les valeurs au carré"""
    return [[x ** 2 for x in row] for row in matrix]
