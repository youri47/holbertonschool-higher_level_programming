#!/usr/bin/python3
"""
Module pour afficher un carré avec des #.
"""


def print_square(size):
    """
    Affiche un carré de taille size avec le caractère #.

    Args:
        size: taille du côté du carré

    Raises:
        TypeError: si size n'est pas un entier
        ValueError: si size est négatif
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
