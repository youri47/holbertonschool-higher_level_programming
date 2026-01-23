#!/usr/bin/python3
"""
Module pour additionner deux entiers.
"""


def add_integer(a, b=98):
    """
    Additionne deux entiers.

    Args:
        a: premier nombre (int ou float)
        b: deuxième nombre (int ou float), défaut = 98

    Returns:
        int: la somme de a et b en entiers

    Raises:
        TypeError: si a ou b n'est pas un int ou float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
