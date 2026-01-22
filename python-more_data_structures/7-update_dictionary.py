#!/usr/bin/python3
"""Module qui contient la fonction update_dictionary"""


def update_dictionary(a_dictionary, key, value):
    """Remplace ou ajoute une clé/valeur dans un dictionnaire"""
    a_dictionary[key] = value
    return a_dictionary
