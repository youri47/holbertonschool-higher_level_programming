#!/usr/bin/python3
"""Module qui contient la fonction multiply_by_2"""


def multiply_by_2(a_dictionary):
    """Retourne un nouveau dictionnaire avec les valeurs multipliées par 2"""
    return {key: value * 2 for key, value in a_dictionary.items()}
