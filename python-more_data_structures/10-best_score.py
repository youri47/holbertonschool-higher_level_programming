#!/usr/bin/python3
"""Module qui contient la fonction best_score"""


def best_score(a_dictionary):
    """Retourne la clé avec la plus grande valeur"""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
