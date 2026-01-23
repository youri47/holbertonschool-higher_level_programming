#!/usr/bin/python3
"""
Module pour diviser tous les éléments d'une matrice.
"""


def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice par un diviseur.

    Args:
        matrix: liste de listes d'entiers ou floats
        div: nombre par lequel diviser

    Returns:
        Nouvelle matrice avec les résultats arrondis à 2 décimales

    Raises:
        TypeError: si matrix n'est pas une liste de listes d'int/float
        TypeError: si les lignes n'ont pas la même taille
        TypeError: si div n'est pas un nombre
        ZeroDivisionError: si div est égal à 0
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)

    for row in matrix:
        if len(row) == 0:
            raise TypeError(msg)
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(msg)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if isinstance(div, float) and (div != div or div == float('inf') or div == float('-inf')):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
